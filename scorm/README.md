# SCORM balíček pro MyGenius

Zabalí e-learning `index.html` do SCORM 1.2 balíčku, který jde nahrát do LMS.

```bash
python3 scorm/build.py
# → scorm/dist/growatt-oss-skoleni-scorm12.zip
```

## Co je uvnitř

| Soubor | K čemu |
|---|---|
| `index.html` | celý kurz včetně obrázků, plus injektovaný SCORM adaptér |
| `imsmanifest.xml` | popis balíčku pro LMS |

Balíček je **jeden SCO** a je **plně offline** — obrázky jsou vložené v souboru, nic se nestahuje z internetu. Velikost cca 2,6 MB.

## Co kurz hlásí do LMS

| Prvek CMI | Kdy se zapisuje |
|---|---|
| `cmi.core.lesson_status` | `incomplete` při prvním spuštění, `completed` po dokončení všech modulů |
| `cmi.core.score.raw` | procento dokončených modulů (0–100) |
| `cmi.suspend_data` | seznam dokončených modulů — díky tomu **postup přežije i přechod na jiný počítač** |
| `cmi.core.lesson_location` | modul, ve kterém uživatel naposledy byl |
| `cmi.core.session_time` | doba strávená v kurzu |
| `cmi.core.exit` | `suspend` při nedokončeném kurzu, prázdné po dokončení |

Zapisuje se při každém stisku **„Dokončit modul"**, jednou za minutu a při zavření okna.

## Pravidlo dokončení

Kurz má **9 obrazovek**, ale tlačítko „Dokončit modul" má jen **7 z nich** — Úvod a Diagnostický tahák ho nemají. Balíček proto počítá dokončení ze **sedmi modulů**, ne z devíti. Tlačítka se počítají za běhu, takže když se v kurzu přibude nebo ubude modul, nemusí se v balíčku nic měnit.

## Nahrání do MyGenius

1. Vytvořit nový kurz typu **SCORM / SCORM 1.2**
2. Nahrát `growatt-oss-skoleni-scorm12.zip` jako celý ZIP (nerozbalovat)
3. Ověřit, že se kurz spustí a že se po dokončení modulu změní stav

Před ostrým nasazením doporučuji **spustit kurz sám za sebe**, projít jeden modul, zavřít a znovu otevřít — musí naskočit tam, kde jsi skončil, a v přehledu musí být vidět rozpracovaný stav.

## Poznámky

- **SCORM 1.2, ne 2004.** Verze 1.2 je nejšířeji podporovaná; pokud MyGenius vyžaduje 2004, dá se manifest upravit.
- **Bez souborů XSD.** Manifest na schémata neodkazuje, takže je nepotřebuje. Většina LMS to takto přijme. Kdyby MyGenius trval na jejich přítomnosti, doplní se do balíčku tři soubory `imscp_rootv1p1p2.xsd`, `adlcp_rootv1p2.xsd` a `imsmd_rootv1p2p1.xsd`.
- **Zdrojový `index.html` se needituje.** Adaptér se vkládá až při buildu, takže veřejná verze na GitHub Pages zůstává bez SCORM kódu.
- **Mimo LMS kurz funguje dál.** Když adaptér nenajde SCORM API, tiše se vypne a postup se ukládá do prohlížeče jako dosud.
