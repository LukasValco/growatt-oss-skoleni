# Scénář živého dema — Growatt OSS pro poruchovou linku

**Formát:** sdílená obrazovka, klikáš v reálném OSS (`oss.growatt.com`), mluvíš k tomu.
**Délka:** ~75 minut včetně nácviku, + dotazy.
**Referenční instalace:** Dubné 93 · end user `Tusl01` · 2× SPH 10000TL3 BH-UP · SN `TPJ4CD200Z`, `TPJ4CD201V`

**Cíl, který musí posluchač na konci umět:** zavolá zákazník se střídačem Growatt → do 3 minut vím, jestli je to problém komunikace, porucha měniče, nebo podvýkon, a komu to předat.

---

## Legenda

| Značka | Význam |
|---|---|
| 🖱 **KLIKÁŠ** | přesná cesta v portálu |
| 💬 **ŘÍKÁŠ** | co u toho povídáš (volně, ne doslova) |
| 👉 **ZDŮRAZNI** | věta, která musí zaznít — na tohle se ptají |
| ⚠️ **PAST** | typická chyba, ukaž ji naživo |

---

## PŘED DEMEM — 10 minut příprava

Bez tohohle se demo rozsype. Odškrtej si:

- [ ] **Přihlášen do OSS předem** — nikdy se nepřihlašuj naživo, zdrží to a riskuješ zamčení účtu (5× špatné heslo = 15 min lock).
- [ ] **Odhlásit se a přihlásit znovu** těsně před začátkem, ať můžeš ukázat výběr serveru. Nebo měj login screen ve druhém okně / anonymním režimu.
- [ ] **Dubné 93 najdi předem** a nech otevřenou v samostatné záložce — ať víš, že je ve stavu Normal a data tečou.
- [ ] **Najdi si předem jednu Offline instalaci.** Dubné 93 je zdravá — Offline ani Fault na ní neukážeš. V Device List → On-Grid Storage seřaď podle `State` nebo `Last update` a najdi něco odpojeného. Měj v samostatné záložce.
- [ ] **Otevři si Data Analysis → Intelligent Alert** — ať víš, kolik tam dnes je pre-warningů.
- [ ] **Záloha:** měj otevřený e-learning (`index.html`). Když portál spadne nebo je pomalý, dojedeš demo na screenshotech — jsou v něm všechny obrazovky, které budeš ukazovat.
- [ ] **Zvětši písmo v prohlížeči na ~125 %** — tabulky v OSS jsou drobné a na sdílené obrazovce nečitelné.
- [ ] **Rozmysli si, na čem ukážeš Set up** (kap. 7). Ideálně na testovací instalaci. Pokud ji nemáš, dialog jen otevřeš a **nic neuložíš** — je to ostrý měnič skutečného zákazníka.
- [ ] Zavři si osobní záložky a notifikace.

> **Pokud posluchači e-learning předem neprošli**, přidej na začátek 10 minut a projdi s nimi modul 2 (datový model) pomaleji — bez něj jim portál nebude dávat smysl.

---

## 0 · Rámec (3 min) — ještě bez portálu

💬 **ŘÍKÁŠ:**
> „Dneska si ukážeme jedinou věc: co dělat, když se vám dovolá zákazník s fotovoltaikou Growatt a řekne, že mu to nefunguje. Nebudeme z vás dělat servisní techniky. Cílem je, abyste do tří minut věděli, jestli je to problém wifiny, porucha měniče, nebo jenom málo svítí slunce — a komu to předat dál. Všechno se odehrává v jednom portálu, který se jmenuje OSS."

👉 **ZDŮRAZNI:** Tři systémy, my používáme jeden:

| Systém | Kdo | My? |
|---|---|---|
| **OSS** `oss.growatt.com` | my, distributoři, instalatéři | ✅ tady pracujeme |
| ShineServer `server.growatt.com` | koncoví uživatelé | jen když nás tam OSS proklikne |
| ShinePhone (mobil) | zákazník, instalatér v terénu | naviguji zákazníka, sám v ní nejsem |

💬 „Zákazník má appku v mobilu. Vy máte web. Vidíte to samé, jenom vy toho vidíte víc."

---

## 1 · Přihlášení (4 min)

🖱 **KLIKÁŠ:** `oss.growatt.com/login`

💬 **ŘÍKÁŠ:**
> „Chrome, adresa do záložek. A teď pozor na jedinou věc, kvůli které mi lidi volají nejčastěji ze všeho —"

⚠️ **PAST — ukaž naživo:** rozbal výběr serveru.
> „Musí tady být **Other Countries and Regions Globally**. Ano, zní to divně, Česko není 'other', ale je. Když si vyberete špatně, přihlásíte se, ono to projde, a uvidíte prázdný účet. Žádná chyba, žádná hláška — prostě prázdno. A vy budete půl hodiny hledat zákazníka, který tam je, jenom se koukáte na špatný server."

👉 **ZDŮRAZNI:** Prázdný nebo cizí účet po přihlášení = **vždycky** špatný region. Odhlásit, přihlásit znovu.

💬 Mimochodem: 5× špatné heslo za 5 minut = zámek na 15 minut. Zapomenuté heslo řeší *Forget Password → Retrieve by Email*.

🖱 **KLIKÁŠ:** ikona jazyka vpravo nahoře → ukaž, že jde přepnout na češtinu.
💬 „Já to nechám v angličtině, protože všechny návody i tabulka chybových kódů jsou anglicky. Vy si to přepněte, jak chcete — je to funkčně to samé."

---

## 2 · Orientace v menu (4 min)

🖱 **KLIKÁŠ:** hlavní stránka po přihlášení, projeď kurzorem hlavní menu.

💬 **ŘÍKÁŠ:**
> „Menu vypadá strašidelně, ale devadesát procent času budete v jedné jediné položce."

| Kde | K čemu | Používáme? |
|---|---|---|
| **Monitoring & Management** | elektrárny, zařízení, zákazníci | ✅ **pořád** |
| **Data Analysis → Intelligent Alert** | podvýkon, odchylka výroby | ✅ na diagnostiku |
| Service Hall → Replacement Claim | reklamace / výměna | při eskalaci na servis |
| Supply System → Warranty Query | ověření záruky podle SN | občas |
| PV Plant Design | návrh FVE | ❌ nikdy |
| Organization Management | role a práva | ❌ jen správce |

💬 „Takže: **Monitoring & Management** je váš domov. Zbytek ignorujte."

---

## 3 · Datový model (6 min) — nejdůležitější část celého školení

Tohle **neklikej**, tohle vysvětli. Klidně u toho nakresli na papír / do chatu.

💬 **ŘÍKÁŠ:**
> „Než začnem klikat, musíte pochopit, jak jsou v tom systému věci poskládané. Když tohle pochopíte, portál je najednou logický. Když ne, budete se v něm topit."

```
👤 End User    ... zákazník (majitel)
   └── 🏭 Plant    ... jeho fotovoltaika
         └── 🔌 Device   ... měnič, baterie, wallbox
               ↕
            📡 Datalogger  ... wifi klíč, který to posílá na internet
```

👉 **ZDŮRAZNI — tři věty, které si mají zapamatovat:**

1. **Bez dataloggeru nejsou data.** Datalogger je malý wifi klíč zapojený do měniče. Fotovoltaika může krásně vyrábět, ale když datalogger nejede, v portálu nevidíte nic. To neznamená poruchu.
2. **SN měniče ≠ SN dataloggeru.** Zákazník vám z displeje přečte číslo měniče. To je jiné číslo než na wifi klíči. Když budete něco přidávat, potřebujete SN *dataloggeru* + **Check Code** ze štítku.
3. **Pořadí je pevné:** nejdřív musí existovat zákazník, pak elektrárna, pak zařízení. Nejde to přeskočit.

⚠️ **PAST — a tohle je perla, ukaž ji:**
> „Hybridní měniče — to jsou ty s baterií, řada SPH, což je většina toho, co dneska montujeme — **nejsou** pod záložkou 'On-grid Inverter'. Jsou schované jinde. A ještě líp: jmenují se jinak podle toho, kde zrovna jste."

| Kde jsi | Záložka pro hybrid (SPH) |
|---|---|
| hlavní **Device List** | 🔶 **On-Grid Storage** |
| **detail elektrárny** → Device List | 🔶 **Hybrid Inverter** |

💬 „Takže když hledáte měnič a záložka je prázdná — neznamená to, že zákazník neexistuje. Znamená to, že jste na špatné záložce. Tohle vás bude štvát první měsíc, pak si zvyknete."

---

## 4 · Dohledání zákazníka (10 min) — LIVE na Dubné 93

💬 **ŘÍKÁŠ:**
> „Zvoní telefon. První otázka, kterou zákazníkovi položíte, je vždycky stejná: **'Přečtete mi sériové číslo z měniče?'** Je na displeji nebo na štítku ze strany. Když ho má, jste doma za dvacet sekund. Ukážu vám tři cesty a proč tuhle chcete."

### Cesta C — přes SN ⭐ (začni tou, kterou budou používat nejvíc)

🖱 **KLIKÁŠ:** `Monitoring & Management → Device List` → záložka **On-Grid Storage** → do pole *Serial Number* vlož `TPJ4CD200Z` → **Inquire**

💬 „Sériové číslo, Enter, hotovo. Tohle je devadesát procent vašich hovorů."

🖱 Ukaž řádek výsledku a projdi sloupce prstem:

| Sloupec | Na co se dívám |
|---|---|
| **State** | Normal / Waiting / Offline / Fault ← **první pohled vždycky sem** |
| SN / Alias | identifikace |
| Datalogger | SN wifi klíče |
| Daily Generation | kolik dnes vyrobil |
| Full hours | plné hodiny — výtěžnost |
| **Last update** | kdy naposledy poslal data ← **klíčové u Offline** |

👉 **ZDŮRAZNI:** „Dva sloupce. **State** a **Last update**. Z těch dvou už poznáte, o čem ten hovor bude."

### Cesta A — přes jméno

🖱 **KLIKÁŠ:** `Monitoring & Management → End User` → do pole *Add account* napiš `Tusl` → **Inquire**

💬 „Když zákazník sériové číslo nemá — je na zahradě, nechce lézt k měniči — hledám podle jména nebo mailu. Stačí dvě tři písmena, hledá to jako 'obsahuje'."

💬 Ukaž, co seznam nabízí: účet, alias, telefon, datum registrace, počet zařízení, instalatér. Klik na řádek → detail (editace, reset hesla, přidání prohlížecího účtu).

### Cesta B — přes elektrárnu

🖱 **KLIKÁŠ:** `Monitoring & Management → Plant List` → název `Dubné` → **Inquire**. Pak klikni na **Advanced Screening** a jen ukaž rozbalený filtr.

💬 „A když neví vůbec nic — jen 'mám to u Českých Budějovic' — je tady Advanced Screening: region, instalatér, výkon panelů, datum instalace, i sériové číslo. Tohle je poslední záchrana, ne první volba."

---

## 5 · Diagnostika jedné instalace (15 min) — jádro celého školení

💬 **ŘÍKÁŠ:**
> „Zákazníka mám. Teď se pojďme podívat, jak zjistím, co se s tou fotovoltaikou vlastně děje. Vezmeme to na Dubné 93 od začátku do konce, přesně tak, jak to budete dělat vy."

### 5.1 Stav — 5 sekund

🖱 **KLIKÁŠ:** zpátky na výsledek v Device List, ukaž sloupec **State**.

| Stav | Co to je | První reakce |
|---|---|---|
| 🟢 **Normal** | běží a vyrábí normálně | OK, koukám dál na čísla |
| 🔵 **Waiting** | čeká na podmínky | ráno/večer/mraky — **není to porucha** |
| ⚫ **Offline** | nedorazila data | problém **komunikace** — wifi, router, datalogger |
| 🔴 **Fault** | měnič hlásí chybový kód | porucha, jdu hledat kód |

💬 **ŘÍKÁŠ** (většina zařízení bude mít Normal, tak to rovnou vysvětli):
> „Zdravý měnič tady má napsáno **Normal**, ne 'Online' — to slovo tam vůbec neuvidíte. Je to proto, že tenhle sloupec míchá dvě věci dohromady. Buď nám datalogger nedoručil data, a pak je tam **Offline** a o měniči nevíme nic. Nebo data dorazila, a pak je tam to, co o sobě říká sám měnič: **Normal** že jede, **Waiting** že čeká na světlo, **Fault** že má poruchu."

👉 **ZDŮRAZNI — tohle je nejdůležitější věta dema:**
> „**Offline neznamená rozbité.** Offline většinou znamená, že zákazníkovi umřela wifina nebo si změnil heslo na routeru. Ta fotovoltaika si tam venku klidně vesele vyrábí, jenom nám o tom nepíše. Kdežto **Fault** znamená, že měnič sám říká 'mám konkrétní problém'. To jsou dva úplně jiné hovory a dvě jiná řešení. Když si tohle spletete, pošlete zbytečně technika za dvě stě kilometrů kvůli přehozenému heslu od wifi."

### 5.2 Detail elektrárny

🖱 **KLIKÁŠ:** `Plant List` → **dvojklik** na Dubné 93

💬 Projdi čtyři sekce:

| Sekce | Co tam čtu |
|---|---|
| **Plant At a Glance** | stav, počet zařízení, typ, výkon panelů, celková výroba, výnos. Odkaz *More plant information* → adresa a instalační údaje |
| **Generation information** | graf výkonu, přepínač Time / Day / Month / Year — **trend** |
| **Device List** | zařízení po záložkách (tady je hybrid pod **Hybrid Inverter**!) |
| **Plant operation log** | historie poruch: čas, typ závady, čas obnovy, řešení |

👉 **ZDŮRAZNI** u operation logu:
> „Tady je prázdno. A to je dobrá zpráva — znamená to, že tahle instalace nikdy neměla poruchu. Když sem přijdete a bude tu deset řádků, čtete si historii toho zákazníka: co se dělo, kdy, a jestli se to samo spravilo. To je první věc, kterou chcete vědět, než začnete něco vymýšlet."

🖱 Ukaž graf výroby, přepni **Day → Month**.
💬 „Zákazník říká 'vyrábí to míň'. Přepnu na měsíc a hned vidím, jestli má pravdu, nebo jestli jenom týden pršelo."

### 5.3 Detail měniče — hlavní diagnostická obrazovka

🖱 **KLIKÁŠ:** v detailu elektrárny → záložka **Hybrid Inverter** → **dvojklik** na SPH 10000TL3 BH-UP

💬 „Tohle je obrazovka, na které strávíte nejvíc času."

| Prvek | Co říká |
|---|---|
| **4 KPI dlaždice** | Generation / Battery discharge / Feed back to the grid / Power consumption |
| **Problem List** | poruchy zařízení + *Export Fault Log* ← **tady najdeš chybový kód** |
| **Real-time SOC graph** | nabití baterie v % |
| **FIG parameter comparison** | nabíjení / vybíjení / síť / spotřeba v jednom grafu |
| **Historical Data** | kompletní telemetrie po ~5 minutách |

🖱 **KLIKÁŠ:** **Historical Data** → nech načíst tabulku

💬 **ŘÍKÁŠ:**
> „Vypadá to jak výpis z účtu a je toho děsně moc. Nemusíte tomu rozumět celému. Zajímá vás sedm sloupců."

| Parametr | Co z toho poznám |
|---|---|
| `Ppv / Ppv1 / Ppv2` | výkon PV celkem a po stringách |
| `Vpv1 / Vpv2` | napětí stringů — **výrazná asymetrie = zastíněný nebo odpojený string** |
| `SOC` | nabití baterie; trvale nízké = problém baterie |
| `Vac1 / Vac2 / Vac3` | napětí na fázích; mimo rozsah → kód 3xx |
| `Fac` | frekvence sítě; kolísá → kód 304 |
| `Pdischarge / Pcharge` | nabíjení a vybíjení baterie |
| `PacToGrid / PacToUser` | kam energie teče — do sítě / do domu |

👉 **ZDŮRAZNI — trik, který stojí za celé školení:**
> „Nejužitečnější je porovnat **Vpv1 a Vpv2**. Jsou to dvě větve panelů. Když jedna dává tři sta voltů a druhá padesát, něco je s tou druhou — spadl na ni strom, zarostla, uvolnil se konektor. Zákazník vám bude tvrdit, že 'to vyrábí míň', a vy mu z kanceláře řeknete, která polovina střechy má problém. To je moment, kdy si vás zákazník zamiluje."

### 5.4 Podvýkon — Intelligent Alert

🖱 **KLIKÁŠ:** `Data Analysis → Intelligent Alert → Inverter Pre-warning List`

💬 **ŘÍKÁŠ:**
> „Klasický hovor: 'vyrábí mi to míň než loni'. Jak poznáte, jestli má pravdu, nebo jestli si to jenom myslí?"

🖱 Ukaž filtr **Deviation Rate** a vysvětli: vyšší číslo = větší odchylka od normálu = hůř. Pokud je instalace v seznamu → **View Data**.

💬 „Tohle porovná jeho výrobu se **stejným modelem měniče ve stejném regionu** za posledních deset dní. Když klesli všichni, pršelo. Když klesl jenom on, je něco špatně u něj. Tímhle jedním klikem odlišíte počasí od poruchy — a ušetříte si dvacet minut dohadování."

💬 U Dubné 93: *1 Normal plant, 0 pre-warning* → zdravá instalace, žádná odchylka.

### 5.5 A teď to, co na Dubném neuvidíme

🖱 **KLIKÁŠ:** přepni na **záložku s Offline instalací**, kterou sis připravil.

💬 **ŘÍKÁŠ:**
> „Dubné 93 je zdravá instalace, na ní vám poruchu neukážu. Tak jsem si vytáhl jinou. Podívejte se na **Last update** — naposledy poslala data [datum]. Tohle je typický Offline hovor a řeší se úplně jinak než porucha."

Postup u Offline, řekni ho jako čtyři otázky na zákazníka:
1. Kdy naposledy poslal data? (*Last update* / operation log)
2. Svítí něco na měniči? Je pod napětím?
3. Neměnil jste heslo od wifi? Neměnil jste router?
4. **Je to 2,4 GHz síť?** — datalogger 5 GHz neumí

💬 „Řešení je skoro vždycky stejné: překonfigurovat datalogger přes ShinePhone. Zákazníka tím provedete po telefonu, nikam se nejezdí."

---

## 6 · Chybové kódy — kdy volat koho (6 min)

💬 **ŘÍKÁŠ:**
> „Když je stav Fault, najdete kód v Problem Listu nebo ho zákazník přečte z displeje. Nemusíte znát všechny kódy. Musíte poznat tři skupiny — protože podle nich se rozhodujete, co uděláte."

| Skupina | Co to je | Kdo to řeší |
|---|---|---|
| **3xx** — síť, AC | 300 napětí mimo rozsah · 302 chybí síť · 304 frekvence · 305 přetížení zálohy | často **zákazník sám** (jistič) nebo se to spraví samo |
| **2xx** — DC, panely | 200 AFCI oblouk · 201 svodový proud · 202 vysoké napětí · 203 nízká izolace | **elektrikář** |
| **1xx / 4xx** — vnitřek měniče | 101–110 komunikace, relé, firmware · 400–428 bus, IGBT, teplota | restart **jednou**, pak **servis** |

👉 **ZDŮRAZNI — bezpečnost, tohle řekni pomalu:**
> „U kódů 1xx a 4xx: **nikdy** nikomu neřeknete, ať otevře měnič. Ani zákazníkovi, ani 'sousedovi, co je šikovnej'. Uvnitř je stejnosměrné napětí, které zabíjí. Do měniče smí jenom člověk s elektrotechnickou kvalifikací a jakýkoli neoprávněný zásah ruší záruku. Když si nejste jistí — servis."

💬 Tři nejčastější hovory, které vás čekají:

| Situace | Co je za tím | Co zákazníkovi řeknete |
|---|---|---|
| Zařízení **Offline** | změna hesla wifi, výměna routeru, 5 GHz, slabý signál, výpadek napájení | provedu vás překonfigurováním v ShinePhone |
| **„Datalogger already exists"** při přidávání | SN už je registrované pod jiným účtem | najít původní účet a odregistrovat, nebo požádat Growatt support o uvolnění |
| **Prázdný účet** po přihlášení | špatný region | odhlásit, přihlásit s *Other Countries and Regions Globally* |

---

## 7 · Vzdálené nastavení parametrů (8 min)

💬 **ŘÍKÁŠ:**
> „Teď něco, co znáte od SolaXu. Tam běžně měníte minimální a maximální SOC baterie, zapínáte asymetrii, měníte export control. Otázka zní, jak je to u Growattu. Odpověď: umí to taky, jenom se to jmenuje jinak a je to schované jinde. A u jedné z těch věcí je správná odpověď 'tohle nesaháme'."

🖱 **KLIKÁŠ:** `Device List` → najdi zařízení → sloupec **Operate** → ikona **Set up** (ozubené kolo)

⚠️ **PAST — dialog otevři, ale nic neukládej.** Klikáš v ostrém prostředí do měniče skutečného zákazníka. Ukaž položky, projdi je, ale **neuloží se nic**. Pokud máš testovací instalaci, udělej to na ní.

👉 **ZDŮRAZNI hned na začátku:**
> „Tohle už není diagnostika. Diagnostika je čtení — koukáte se a nic nerozbijete. Tohle je **zápis do cizího měniče**. Můžete zákazníkovi změnit chování celé fotovoltaiky a výši účtu za elektřinu. Takže pravidlo číslo jedna: **z vlastní iniciativy tady neměníme nic.** Jenom když o to zákazník sám požádá, nebo když vám to zadá servis."

### 7.1 Minimální SOC baterie — tohle měnit smíte

💬 „Nejčastější požadavek. Zákazník volá, že mu baterie v noci padá na nulu a ráno nemá z čeho brát."

🖱 Ukaž: kategorie **Load First** → parametr **Discharge Stopped SOC**

| Parametr | Co dělá |
|---|---|
| **Discharge Stopped SOC** | minimum v %, pod které baterie neklesne |
| **Discharge Power Rate** | jak rychle se smí vybíjet |

💬 „Growatt doporučuje **10 až 15 procent v létě** a **40 procent v zimě**. Ta zimní rezerva není náhoda — málo se vyrábí a když spadne síť, má v baterii něco zůstat pro zálohovaný okruh."

### 7.2 Režimy a časová okna — dřív než zavoláte poruchu

🖱 Ukaž tři režimy: **Load First / Battery First / Grid First** a u nich časové úseky.

👉 **ZDŮRAZNI — tohle vám ušetří spoustu zbytečných hovorů:**
> „Když si zákazník stěžuje, že se baterie chová divně v určitou denní dobu — třeba že se mu večer vybíjí do sítě — nehledejte poruchu. Podívejte se na časová okna režimů. Hrozně často je to zapomenuté nastavení z instalace, ne závada."

### 7.3 Export control — tohle NEMĚNÍTE

🖱 Ukaž cestu: **Advance set → Register**

| Registr | Hodnota | Význam |
|---|---|---|
| `202` | `1` | zapne omezení dodávky |
| `201` | např. `3000` | povolený výkon do sítě ve **wattech** |

👉 **ZDŮRAZNI — řekni to natvrdo:**
> „Vidíte, že se to zadává přímo do registrů. Žádné hezké menu, holá čísla. A hlavně: povolený výkon do sítě **není technická drobnost, plyne ze smlouvy o připojení s distributorem.** Když ho zvednete, dostanete zákazníka do rozporu s podmínkami připojení. Když ho omylem shodíte na nulu, přijde o výnosy a bude to reklamovat. Na lince tohle **neděláme** — předáváme na servis nebo na toho, kdo to připojoval."

### 7.4 Asymetrie — u Growattu není co nastavovat

💬 **ŘÍKÁŠ:**
> „A tady je rozdíl proti SolaXu, kvůli kterému byste jinak hledali půl hodiny. Naše SPH TL3 BH-UP jsou **asymetrické konstrukčně** — umí do každé fáze poslat jiný výkon a mají to napevno. Není to funkce, kterou byste zapínali. Takže když v nastavení hledáte přepínač asymetrie, nehledejte — není tam, protože být nemusí."

💬 „Když to zákazník řeší kvůli požadavku distributora, není to věc linky. Projektant nebo servis."

### 7.5 Postup, který platí vždy

💬 Šest kroků, projeď je rychle:

1. **Ověř oprávnění** — žádá zákazník, nebo servis? Víš, co změna udělá?
2. **Zkontroluj stav** — musí být **Normal**. Na Offline měnič nastavení nedorazí.
3. **Zapiš si původní hodnotu** — bez toho se nevrátíš zpátky.
4. **Proveď změnu** — parametr → hodnota → heslo → uložit.
5. **Ověř zpětně** — načti hodnotu znovu, opravdu se uložila?
6. **Zaznamenej** — co, kdy, na čí žádost, z čeho na co.

👉 **ZDŮRAZNI bod 2:**
> „Na Offline měnič nastavení nedojde. Dialog se může zatvářit, že se uložilo, ale v měniči to nebude. Proto se po každé změně hodnota načítá zpátky."

---

## 8 · Přidání zákazníka do monitoringu (5 min)

💬 **ŘÍKÁŠ:**
> „Poslední situace: zákazník volá, a vy ho v portálu vůbec nevidíte. Buď je nový, nebo ho nikdo nenavázal na náš účet."

👉 **ZDŮRAZNI:** Pořadí. **End User → Plant → Datalogger (SN + Check Code).** Nejde přeskočit.

🖱 **KLIKÁŠ:** `Plant List → Add Plant` — jen **ukaž formulář, nevyplňuj ho**.

💬 Projeď pole: Plant Name, Plant Type (Residential), Installation Date, PV Panels Power, Assigned user, Country = Czech Republic, Time Zone = **GMT +1**, Installer.

💬 **ŘÍKÁŠ:**
> „Ale upřímně — z kanceláře to budete dělat málokdy. Devětkrát z deseti to zakládá zákazník nebo montér v terénu přes mobilní appku ShinePhone, a vy ho po telefonu navigujete: Add Plant → Add Datalogger → naskenovat QR ze štítku → nastavit wifinu."

⚠️ **PAST — nejčastější důvod, proč se párování nepovede:**
> „**Dvě celé čtyři gigahertz.** Zákazník musí být připojený na 2,4 GHz síť, ne na 5 GHz. Datalogger pětku neumí. Většina moderních routerů má obojí pod stejným názvem a telefon se sám přehodí na pětku — a párování prostě neprojde a nikdo neví proč. Tohle je nejčastější příčina selhání ze všech."

⚠️ **A jedno varování:** funkce *Import to distributor/installer* nasdílí zákazníka jinému OSS účtu se **stejnými právy** — včetně mazání zařízení a přenastavení měniče. Používat vědomě.

---

## 9 · Závěr a tahák (3 min)

🖱 **KLIKÁŠ:** otevři e-learning → modul **Diagnostický tahák**

💬 **ŘÍKÁŠ:**
> „Nic z toho si nemusíte pamatovat. Tady je tahák — vytiskněte si ho a mějte u telefonu. Šest kroků diagnostiky, stavy zařízení, nejdůležitější kódy, kdo co řeší."

**Zopakuj šest vět, se kterými mají odejít:**

1. Server pro Česko = **Other Countries and Regions Globally**. Prázdný účet = tohle.
2. Hybridy SPH jsou pod **On-Grid Storage** (hlavní Device List) nebo **Hybrid Inverter** (detail elektrárny).
3. Zdravý měnič = **Normal**, ne „Online". A **Offline = komunikace, Fault = porucha** — dva jiné hovory.
4. Datalogger jede jen na **2,4 GHz**.
5. Kódy **1xx a 4xx** — neotevírat měnič, volat servis.
6. **Export limit neměníme.** Minimální SOC na žádost zákazníka ano — a vždy ověřit, že se změna doopravdy uložila.

---

## 10 · Nácvik hovoru (10 min) — nepřeskakuj

Tohle je část, ze které si odnesou nejvíc. Ty hraješ zákazníka, oni klikají v portálu. Sdílenou obrazovku předej jim, ať to opravdu dělají sami.

**Hovor 1 — Offline (nejčastější)**
> „Dobrý den, mám od vás fotovoltaiku a od pátku mi v mobilu neukazuje vůbec nic. Předtím to šlo normálně."

*Očekávaná reakce:* zeptat se na SN → Device List → State = Offline → Last update → otázka na wifi/router/heslo → 2,4 GHz → navigace přes ShinePhone.
*Past, do které spadnou:* začnou řešit poruchu měniče. Zastav je: „Offline není porucha."

**Hovor 2 — podvýkon**
> „Loni v červnu mi to dělalo víc. Teď to vyrábí sotva půlku. Něco se rozbilo?"

*Očekávaná reakce:* najít instalaci → State = Normal → graf výroby Month → Intelligent Alert / Deviation Rate → Historical Data, porovnat Vpv1 vs Vpv2.
*Past:* uvěří zákazníkovi bez ověření. Nauč je nejdřív odlišit počasí.

**Hovor 3 — Fault**
> „Bliká mi na tom červená a je tam napsáno tři sta dva."

*Očekávaná reakce:* kód 302 = chybí AC → „zkontrolujte prosím jistič" → zákazník to vyřeší sám za dvě minuty.
*Past:* eskalují na servis. Ukaž jim v tabulce, že tohle je zákazník sám.

**Hovor 4 — žádost o změnu nastavení** (tenhle je zákeřný schválně)
> „Dobrý den, soused má taky Growatta a říkal, že si nechal zvýšit, kolik toho může posílat do sítě. Můžete mi to prosím taky přenastavit? A ještě bych chtěl, aby mi baterie nešla pod třicet procent."

*Očekávaná reakce:* rozdělit to na dvě věci. **Minimální SOC = ano** (Set up → Load First → Discharge Stopped SOC, ověřit stav Normal, zapsat původní hodnotu, po uložení načíst zpátky). **Export limit = ne** — vysvětlit, že vychází ze smlouvy o připojení, a předat na servis.
*Past:* udělají obojí, nebo naopak odmítnou obojí. Správně je rozdělit — a umět zákazníkovi vysvětlit proč.

---

## Když se demo nepovede

| Problém | Co uděláš |
|---|---|
| OSS je pomalý nebo nedostupný | přepneš na e-learning a dojedeš to na screenshotech — jsou tam všechny obrazovky |
| Nemůžeš se přihlásit | nezkoušej třikrát, zamkne se to; jeď ze screenshotů |
| Dubné 93 je zrovna Offline | ideální! Ukaž to jako živý příklad Offline a diagnostiku dojeď na jiné instalaci |
| Nestíháš čas | vynech kapitolu 8 (přidání do monitoringu) — je nejmíň častá; **nikdy nevynechávej kapitolu 5, 7.3 a 10** |

---

## Časový rozpis

| # | Část | Min | Kumulativně |
|---|---|---|---|
| 0 | Rámec | 3 | 3 |
| 1 | Přihlášení | 4 | 7 |
| 2 | Orientace v menu | 4 | 11 |
| 3 | Datový model | 6 | 17 |
| 4 | Dohledání zákazníka | 10 | 27 |
| 5 | **Diagnostika** | **15** | 42 |
| 6 | Chybové kódy | 6 | 48 |
| 7 | **Vzdálené nastavení** | **8** | 56 |
| 8 | Přidání do monitoringu | 5 | 61 |
| 9 | Závěr a tahák | 3 | 64 |
| 10 | **Nácvik hovoru** | **10** | **74** |
