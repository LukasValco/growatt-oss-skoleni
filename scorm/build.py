#!/usr/bin/env python3
"""
Sestaví SCORM 1.2 balíček z index.html.

Zdrojový kurz se needituje — adaptér se injektuje až při buildu,
takže webová verze na GitHub Pages zůstává čistá.

    python3 scorm/build.py

Výstup: scorm/dist/growatt-oss-skoleni-scorm12.zip
"""

import os
import re
import sys
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "index.html")
OUT_DIR = os.path.join(ROOT, "scorm", "dist")
ZIP_NAME = "growatt-oss-skoleni-scorm12.zip"

TITLE = "Growatt OSS — školení pro poruchovou linku"
IDENT = "GROWATT-OSS-PORUCHOVA-LINKA"

# ── Adaptér vkládaný PŘED hlavní skript kurzu ────────────────────────────────
# Musí běžet dřív, než kurz přečte localStorage — tím se do něj propíše
# postup uložený v LMS a kurz sám o SCORMu nemusí vědět.
PRE = r"""
<script>
/* ===== SCORM 1.2 adaptér — část 1/2 (před kurzem) ===================== */
(function () {
  "use strict";

  /* --- localStorage nemusí být v iframu LMS dostupný --------------- */
  try {
    window.localStorage.setItem("__scormtest", "1");
    window.localStorage.removeItem("__scormtest");
  } catch (e) {
    var mem = {};
    try {
      Object.defineProperty(window, "localStorage", {
        configurable: true,
        value: {
          getItem: function (k) { return Object.prototype.hasOwnProperty.call(mem, k) ? mem[k] : null; },
          setItem: function (k, v) { mem[k] = String(v); },
          removeItem: function (k) { delete mem[k]; }
        }
      });
    } catch (e2) { /* nic víc nezmůžeme */ }
  }

  /* --- vyhledání API v hierarchii oken ----------------------------- */
  function search(win, depth) {
    var n = 0;
    while (win && n < depth) {
      try { if (win.API) return win.API; } catch (e) { /* cross-origin */ }
      if (!win.parent || win.parent === win) break;
      win = win.parent;
      n += 1;
    }
    return null;
  }

  var api = search(window, 12);
  if (!api) { try { if (window.opener) api = search(window.opener, 12); } catch (e) {} }

  var S = window.SCORM = {
    api: api,
    ok: false,
    finished: false,
    started: new Date().getTime(),
    get: function (k) {
      if (!this.ok) return "";
      try { return String(this.api.LMSGetValue(k)); } catch (e) { return ""; }
    },
    set: function (k, v) {
      if (!this.ok) return;
      try { this.api.LMSSetValue(k, String(v)); } catch (e) {}
    },
    commit: function () {
      if (!this.ok) return;
      try { this.api.LMSCommit(""); } catch (e) {}
    }
  };

  if (!api) {
    if (window.console) console.info("SCORM: API nenalezeno, kurz běží samostatně.");
    return;
  }

  var res = "";
  try { res = String(api.LMSInitialize("")); } catch (e) {}
  var err = "0";
  try { err = String(api.LMSGetLastError()); } catch (e) {}
  S.ok = (res === "true") || (err === "0") || (err === "101");

  if (!S.ok) {
    if (window.console) console.warn("SCORM: LMSInitialize selhalo, chyba " + err);
    return;
  }

  /* --- postup uložený v LMS přeneseme do localStorage -------------- */
  var sd = S.get("cmi.suspend_data");
  if (sd) {
    try {
      var parsed = JSON.parse(sd);
      if (Object.prototype.toString.call(parsed) === "[object Array]") {
        window.localStorage.setItem("ossEDone_v2", sd);
      }
    } catch (e) {}
  }

  var status = S.get("cmi.core.lesson_status");
  if (!status || status === "not attempted" || status === "") {
    S.set("cmi.core.lesson_status", "incomplete");
  }
  S.commit();
})();
</script>
"""

# ── Adaptér vkládaný ZA hlavní skript kurzu ──────────────────────────────────
POST = r"""
<script>
/* ===== SCORM 1.2 adaptér — část 2/2 (za kurzem) ======================= */
(function () {
  "use strict";
  var S = window.SCORM;
  if (!S || !S.ok) return;

  /* Úvod a Tahák nemají tlačítko „Dokončit modul“, takže se dá dokončit
     jen tolik modulů, kolik je těch tlačítek. */
  var TOTAL = document.querySelectorAll("button.btn-done").length || 7;

  function doneCount() {
    try {
      var a = JSON.parse(window.localStorage.getItem("ossEDone_v2") || "[]");
      return a.length;
    } catch (e) { return 0; }
  }

  function activeIndex() {
    var items = document.querySelectorAll("#nav li");
    for (var i = 0; i < items.length; i += 1) {
      if (items[i].className.indexOf("active") !== -1) return i;
    }
    return 0;
  }

  function push() {
    var n = Math.min(doneCount(), TOTAL);
    var pct = Math.round((n / TOTAL) * 100);
    S.set("cmi.suspend_data", window.localStorage.getItem("ossEDone_v2") || "[]");
    S.set("cmi.core.lesson_location", String(activeIndex()));
    S.set("cmi.core.score.min", "0");
    S.set("cmi.core.score.max", "100");
    S.set("cmi.core.score.raw", String(pct));
    S.set("cmi.core.lesson_status", n >= TOTAL ? "completed" : "incomplete");
    S.commit();
  }

  /* doneModule() se volá z atributu onclick, tedy přes window */
  var orig = window.doneModule;
  if (typeof orig === "function") {
    window.doneModule = function () {
      var r = orig.apply(this, arguments);
      push();
      return r;
    };
  }

  function two(n) { return (n < 10 ? "0" : "") + n; }
  function sessionTime(ms) {
    var s = Math.floor(ms / 1000);
    var h = Math.floor(s / 3600);
    var m = Math.floor((s % 3600) / 60);
    return two(h) + ":" + two(m) + ":" + two(s % 60);
  }

  function finish() {
    if (S.finished) return;
    S.finished = true;
    push();
    S.set("cmi.core.session_time", sessionTime(new Date().getTime() - S.started));
    S.set("cmi.core.exit", S.get("cmi.core.lesson_status") === "completed" ? "" : "suspend");
    S.commit();
    try { S.api.LMSFinish(""); } catch (e) {}
  }

  window.addEventListener("beforeunload", finish);
  window.addEventListener("pagehide", finish);
  window.addEventListener("unload", finish);

  /* výchozí zápis hned po načtení + průběžný commit */
  push();
  window.setInterval(function () { if (!S.finished) push(); }, 60000);
})();
</script>
"""

MANIFEST = """<?xml version="1.0" encoding="UTF-8"?>
<manifest identifier="{ident}" version="1.0"
          xmlns="http://www.imsproject.org/xsd/imscp_rootv1p1p2"
          xmlns:adlcp="http://www.adlnet.org/xsd/adlcp_rootv1p2">
  <metadata>
    <schema>ADL SCORM</schema>
    <schemaversion>1.2</schemaversion>
  </metadata>
  <organizations default="ORG-1">
    <organization identifier="ORG-1">
      <title>{title}</title>
      <item identifier="ITEM-1" identifierref="RES-1" isvisible="true">
        <title>{title}</title>
        <adlcp:masteryscore>100</adlcp:masteryscore>
      </item>
    </organization>
  </organizations>
  <resources>
    <resource identifier="RES-1" type="webcontent" adlcp:scormtype="sco" href="index.html">
      <file href="index.html"/>
    </resource>
  </resources>
</manifest>
"""


def build():
    if not os.path.exists(SRC):
        sys.exit("Nenalezen " + SRC)

    html = open(SRC, encoding="utf-8").read()

    if "SCORM 1.2 adaptér" in html:
        sys.exit("Zdroj už adaptér obsahuje — build se pouští nad čistým index.html.")

    m = re.search(r"<script>\s*\nconst MODULES", html)
    if not m:
        sys.exit("Nenalezen hlavní skript kurzu (const MODULES).")

    start = m.start()
    end = html.index("</script>", start) + len("</script>")

    out = html[:start] + PRE.strip() + "\n" + html[start:end] + "\n" + POST.strip() + html[end:]

    os.makedirs(OUT_DIR, exist_ok=True)
    zip_path = os.path.join(OUT_DIR, ZIP_NAME)

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        z.writestr("index.html", out)
        z.writestr("imsmanifest.xml", MANIFEST.format(ident=IDENT, title=TITLE))

    src_kb = os.path.getsize(SRC) / 1024
    zip_kb = os.path.getsize(zip_path) / 1024
    print("Hotovo: " + zip_path)
    print("  index.html   %8.0f kB" % src_kb)
    print("  balíček      %8.0f kB" % zip_kb)
    n = len(re.findall(r"<button[^>]*doneModule\(\)[^>]*>", out))
    print("  dokončitelných modulů: %d" % n)


if __name__ == "__main__":
    build()
