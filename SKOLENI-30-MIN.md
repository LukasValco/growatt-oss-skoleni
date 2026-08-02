# Growatt — seznámení pro poruchovou linku

**Kdy:** 7:00–7:30 · **Formát:** MS Teams, bez kamery — jedna sdílená obrazovka, druhá s tímto scénářem

## Údaje pro ukázku

| Údaj | Hodnota |
|---|---|
| Portál | `oss.growatt.com` |
| Server / region | Other Countries and Regions Globally |
| **Sériové číslo měniče** (vyhledáváš) | `TPJ4CD200Z` |
| Sériové číslo dataloggeru | `XGD5BLB26M` |
| Uživatel (End User) | `Tusl01` |
| Elektrárna (Plant) | `Dubné 93` |
| Typ | SPH 4000-10000TL3 BH-UP · 10 000 W |
| Druhý měnič v instalaci | `TPJ4CD201V` |

---

## Cíl setkání

Aby po hovoru se zákazníkem uměli: **dohledat instalaci**, **přečíst provozní stav a základní hodnoty**, **vědět, kde se mění základní parametry**, a **rozpoznat, co předat dál**.

> **Co si mají odnést:**
> 1. Rozpoznám Growatt a dohledám instalaci podle sériového čísla.
> 2. Přečtu, v jakém je stavu — a když nekomunikuje, ověřím po telefonu, jestli elektrárna vyrábí.
> 3. Vím, kde se nastavuje SOC baterie a přetok do sítě.
> 4. Vím, co a komu předat.

---

## Specifika online formátu

- **Sdílej od první minuty.** Bez kamery je obrazovka jediný vizuální kanál.
- **Každou změnu obrazovky oznam slovy.** „Nyní přepnu do portálu."
- **Kurzorem ukazuj, o čem mluvíš,** pomaleji než by ti přišlo přirozené.
- **Mluv o něco pomaleji** — komprese zvuku a sedmá ranní.
- **Místo tichých pauz slovní předěly.** Ticho působí jako výpadek spojení.
- **Dotazy do chatu**, na koncích částí se do něj podívej.

---

## Plán obrazovky

| Čas | Na sdílené obrazovce |
|---|---|
| 7:00 | E-learning — úvodní stránka |
| 7:05 | E-learning → **Modul 2 „Datový model"** |
| 7:08 | **Živý portál OSS** |
| 7:22 | OSS — detail měniče `TPJ4CD200Z` |
| 7:26 | E-learning — přehled modulů |
| 7:28 | E-learning — úvodní stránka |

---

## Příprava — 15 minut předem

- [ ] **Přihlášen v OSS**, `TPJ4CD200Z` dohledané, detail otevřený ve vlastní záložce
- [ ] **Sériové číslo `TPJ4CD200Z` ve schránce**
- [ ] **Otevři si předem „Set the device"** a projdi, co v dialogu je — scénář počítá s tím, že tam najdeš nastavení SOC a přetoku, ale rozložení dialogu si musíš ověřit sám. Podle toho případně uprav bod 5 ukázky.
- [ ] **Nic v dialogu neukládej** — je to ostrý měnič
- [ ] E-learning otevřený na úvodní stránce
- [ ] Vyzkoušené sdílení v Teams a přepínání mezi okny
- [ ] Písmo v prohlížeči na 125 %, zavřené notifikace

---

# SCÉNÁŘ

---

## 7:00–7:03 · Úvod (3 min)

📺 **NA OBRAZOVCE:** e-learning, úvodní stránka. Sdílení spusť ještě před začátkem.

> „Dobré ráno. Dnešní téma je nový typ střídače, se kterým se na lince můžete od podzimu setkat — značka **Growatt**. V září spouštíme nabídku servisu pro tyto střídače, takže od října můžete začít dostávat hovory od zákazníků, kteří mají doma Growatta.
>
> Projdeme čtyři věci. **Co Growatt je** a jak ho rozpoznáte. **Jak dohledáte instalaci** v jejich monitorovacím portálu. **Co si z portálu přečtete** — stav, výrobu, napětí. A **kde se nastavují základní parametry**, jako je minimální nabití baterie nebo přetok do sítě. Vše si ukážeme na živé instalaci.
>
> Dotazy prosím pište průběžně do chatu, budu ho sledovat."

*Krátká odmlka, pak přímo k námitce.*

> „Ještě než začneme — chci pojmenovat jednu věc otevřeně. Ano, přibývá vám další značka a další portál. Nebudu tvrdit opak; vím, s kolika systémy denně pracujete.
>
> Co ale mohu upřesnit, je rozsah. Nebudete v tom portálu nic opravovat a nemusíte si nic pamatovat zpaměti — dostanete tahák i e-learning. A není to od dneška: první reálné instalace očekáváme v říjnu, takže máte zhruba dva měsíce."

**Co musí zaznít:** otevřené přiznání, že něco přibývá. Bez něj nebude zbytek působit věrohodně.

---

## 7:03–7:05 · Co je Growatt (2 min)

📺 **NA OBRAZOVCE:** beze změny.

> „Growatt je čínský výrobce střídačů, patří mezi největší na trhu a v Česku ho instaluje řada montážních firem. Pro vaši práci je podstatné, že **plní stejnou funkci jako SolaX nebo GoodWe.**
>
> Rozpoznáte ho podle typového štítku na měniči — je tam uvedeno **Growatt** a typové označení. Nejčastěji se setkáte s řadou **SPH**, což jsou hybridní střídače s baterií. Naše referenční instalace má dva kusy SPH 4000-10000TL3 BH-UP o výkonu deset kilowattů.
>
> Princip znáte. Střídač měří provozní data, komunikační modul — v praxi malý wi-fi adaptér — je odesílá na server výrobce a my se na ně díváme v monitorovacím portálu. Ten se jmenuje **OSS**, adresa `oss.growatt.com`. Zákazník má k dispozici mobilní aplikaci, vy webové rozhraní."

---

## 7:05–7:08 · Uspořádání a dvě sériová čísla (3 min)

📺 **NA OBRAZOVCE:** e-learning → **Modul 2 „Datový model"**.

> „Přepnu na schéma. Systém má tři úrovně, stejně jako u ostatních značek."

```
Zákazník (End User)          Tusl01
   └── elektrárna (Plant)    Dubné 93
         └── střídač (Device) + komunikační modul (Datalogger)
```

### Dvě různá sériová čísla — nepleťte si je

> „Tady dávejte pozor, protože jsou v tom dvě různá čísla a snadno se popletou."

| | Kde ho zákazník najde | Naše instalace |
|---|---|---|
| **SN měniče** | typový štítek **na boku měniče** | `TPJ4CD200Z` |
| **SN dataloggeru** | štítek **na wi-fi adaptéru**, spolu s Check Code | `XGD5BLB26M` |

> „Obě jsou desetimístná, obě obsahují písmena i číslice, ale patří jinému zařízení. **Vy budete vyhledávat podle sériového čísla měniče.** Číslo dataloggeru potřebujete jen tehdy, když se instalace zakládá do monitoringu — a to nebude vaše agenda, dělá to montážní firma.
>
> Zákazník ho najde na štítku na boku měniče. Pokud tam nedosáhne nebo je štítek špatně čitelný, dá se hledat i podle jména nebo názvu elektrárny."

### Komunikace není totéž co výroba

> „A nyní věc, kterou už asi znáte z jiných značek, ale pro jistotu ji zopakuji. Ten komunikační modul může přestat fungovat **nezávisle** na tom, zda elektrárna vyrábí.
>
> Když v portálu uvidíte, že instalace nekomunikuje, nemusí to znamenat závadu. Nejčastější příčinou je změna hesla k wi-fi nebo výměna routeru. Elektrárna přitom může normálně vyrábět, jen o sobě neodesílá data. Za chvíli si řekneme, jak si to po telefonu ověříte."

---

## 7:08–7:22 · Živá ukázka (14 min)

📺 **NA OBRAZOVCE:** přepni na **živý portál OSS**.

> „Nyní přepnu do portálu a projdeme to tak, jak to budete dělat vy."

### 1) Přihlášení (2 min)

🖱 `oss.growatt.com`

> „Adresa `oss.growatt.com`, najdete ji v taháku. Upozorním na jedinou věc —"

🖱 **Ukaž výběr serveru.**

> „— na tento výběr. Musí být zvolena možnost **Other Countries and Regions Globally**; Česká republika spadá do této skupiny. Při nesprávné volbě se přihlásíte bez chybové hlášky, ale uvidíte prázdný účet. Systém vás na nic neupozorní.
>
> **Prázdný účet po přihlášení znamená nesprávně zvolený server.**"

🖱 Projeď kurzorem hlavní menu.

> „Pracovat budete prakticky jen s položkou **Monitoring and Management**."

### 2) Dohledání instalace (3 min)

🖱 `Monitoring & Management` → `Device List` → **On-Grid Storage** → pole **Serial Number** → vlož `TPJ4CD200Z` → **Inquire**

> „Volá zákazník, přečte sériové číslo ze štítku. Vložím ho do pole Serial Number, potvrdím. Výsledek je okamžitý."

⚠️ 🖱 **Ukaž záložky nad seznamem.**

> „Jedna věc, která by vás mohla zdržet: nad seznamem jsou záložky podle typu zařízení. Hybridní střídače najdete pod záložkou **On-Grid Storage**, nikoli pod tou, kterou byste čekali. Pokud tedy vyhledáváte a nic nenajdete, zkuste nejdřív přepnout záložku."

🖱 Ukaž **State** a **Last update**. Kurzorem ukazuj sloupce.

> „Ve výsledku vás nejdřív zajímají dva sloupce. **State** — provozní stav, tady **Normal**, tedy střídač běží. Můžete narazit i na **Waiting**, což znamená, že čeká na dostatečné osvětlení, na **Fault**, tedy hlášenou závadu, a na **Offline**, kdy nedorazila data.
>
> A **Last update** — kdy naposledy data dorazila. U stavu Offline vám tenhle údaj řekne, jak dlouho už to trvá."

### 3) Detail měniče — co se z něj dá vyčíst (6 min)

🖱 **Dvojklik** na zařízení `TPJ4CD200Z`

> „Dvojklikem se dostanu do detailu zařízení. Tady je toho k vidění nejvíc, projdeme to shora."

🖱 Ukaž **hlavičku** — SN, Datalogger, User, Plant, Rated Power

> „V hlavičce je vše, co potřebujete pro identifikaci: sériové číslo měniče, sériové číslo dataloggeru, uživatel — tady `Tusl01`, elektrárna `Dubné 93` a jmenovitý výkon deset kilowattů."

🖱 Ukaž **čtyři dlaždice**

> „Čtyři dlaždice s bilancí — kolik elektrárna **vyrobila**, kolik se **vybilo z baterie**, kolik šlo **do sítě** a kolik **spotřeboval dům**. U každé je dnešek, tento měsíc a celkový součet. Když se zákazník ptá, kolik mu to vyrobilo, odpověď je tady."

🖱 Ukaž **Problem List**

> „**Problem List** — přehled závad. Tady je prázdný, což znamená, že instalace zatím žádnou závadu nehlásila. Pokud tu bude řádek s chybovým kódem, **kód opíšete do ticketu**; význam kódů je v taháku. Vpravo je tlačítko **Export Fault Log**, kterým se dá historie závad stáhnout — hodí se, když to předáváte servisu."

🖱 Ukaž **graf SOC**

> „Graf nabití baterie v procentech. Na tomhle je hezky vidět, jak se přes den baterie nabila z nějakých třiceti procent na sto."

🖱 Ukaž **FIG parameter comparison** a přepni volbu v `Select Parameters`

> „Pod tím je porovnávací graf, kde si můžete zvolit, co chcete vykreslit — nabíjení, vybíjení, tok do sítě, spotřebu domu."

🖱 Rozbal **Historical Data**

> „A tohle je nejpodrobnější část — **Historical Data**, tedy telemetrie zhruba po pěti minutách. Vypadá to jako výpis z účtu a není potřeba tomu rozumět celému, ale ukážu vám čtyři sloupce, které se vám budou hodit."

| Sloupec | Co říká |
|---|---|
| `Status` | provozní režim — u zdravé instalace `PV Bat Online`, tedy běží panely i baterie |
| `Ppv`, `Vpv1`, `Ppv1` | **výkon a napětí z panelů** — tady vidíte, že elektrárna skutečně vyrábí |
| `Vac1`, `Vac2`, `Vac3`, `Fac` | **napětí na jednotlivých fázích a frekvence sítě** |
| `SOC`, `VBat` | nabití a napětí baterie |

> „Když se vás tedy někdo zeptá, jestli má střídač napětí na síti, odpověď najdete ve sloupcích **Vac1 až Vac3**. A jestli vyrábí, poznáte podle sloupce **Ppv**."

### 4) Kde se mění nastavení (3 min)

🖱 Ukaž tlačítka vpravo nahoře: **Editing device · Set the device · Set datalogger · Delete device**

> „A poslední věc, kterou vám chci ukázat. Vpravo nahoře jsou čtyři tlačítka. Nás zajímají dvě: **Set the device** je nastavení samotného střídače, **Set datalogger** je nastavení komunikačního modulu."

🖱 Otevři **Set the device** a projdi položky. **Neukládej nic.**

> „Tady se mění provozní parametry na dálku. Dvě, o které jde nejčastěji:
>
> **Minimální nabití baterie** — hodnota, pod kterou se baterie nevybije. Zákazníci volají, že jim baterie v noci padá na nulu, nebo naopak že jim zůstává zbytečně plná. Growatt doporučuje zhruba deset až patnáct procent v létě a čtyřicet procent v zimě, protože v zimě se má něco nechat pro zálohovaný okruh.
>
> **Přetok do sítě** — kolik výkonu smí elektrárna posílat do distribuční sítě.
>
> Nastavení se posílá přes datalogger do střídače, takže **musí být online**. U instalace ve stavu Offline změna nedojde — dialog se může tvářit, že se uložila, ale ve střídači nebude. Proto se po každé změně hodnota načítá zpátky a ověřuje."

⚠️ Řekni jednou větou, nezdržuj se:

> „A ještě jedna věc: povolený přetok vychází z **podmínek připojení s distributorem**. Neměňte ho z vlastního uvážení — jen na základě konkrétního zadání."

🖱 **Zavři dialog bez uložení.**

---

## 7:22–7:26 · Jak s tím naložit (4 min)

📺 **NA OBRAZOVCE:** zůstáváš v detailu měniče.

> „Shrnu, jak to používat u hovoru."

| Zjištěný stav | Postup |
|---|---|
| **Normal**, zákazník hlásí nízkou výrobu | Historical Data → `Ppv`. Porovnejte s tím, co hlásí. Ticket. |
| **Fault** | Problem List → opište kód. Případně Export Fault Log. Ticket. |
| **Offline** | Ověřte po telefonu, jestli elektrárna vyrábí — viz níže. Ticket i tak. |
| Nejasná situace | Ticket, případně dotaz na Teams. |

### Jak po telefonu ověřit, že elektrárna vyrábí

*Toto je nejužitečnější věc pro stav Offline — v portálu nevidíte nic, ale zákazník stojí u měniče.*

> „Když je instalace Offline, v portálu jste slepí — data nedorazila. Ale zákazník se může jít na měnič podívat a vy z toho poznáte, jestli řešíte výpadek komunikace, nebo skutečnou závadu.
>
> Poproste ho, ať se podívá na **kontrolku a displej** na měniči. Podle manuálu platí: **když měnič pracuje normálně, kontrolka svítí zeleně a na displeji jsou běžné provozní údaje.** Pokud je signalizace **červená**, jde o závadu a je to případ pro servis.
>
> Takže: zelená kontrolka a normální displej znamená, že elektrárna běží a problém je pouze v komunikaci — nejspíš wi-fi, router nebo změna hesla. To je hovor, který se řeší po telefonu, ne výjezdem."

> „Rozdíl mezi ticketem ‚nefunguje fotovoltaika' a ticketem ‚Growatt SPH, stav Offline, poslední data před dvěma týdny, zákazník měnil router, kontrolka na měniči svítí zeleně' je pro kolegy ze servisu zásadní."

---

## 7:26–7:28 · Kam se obrátit (2 min)

📺 **NA OBRAZOVCE:** e-learning, přehled modulů. Cca 30 sekund, **neprocházej ho**.

| Zdroj | K čemu |
|---|---|
| **Tahák** | Jedna stránka pro všechny značky — SolaX, GoodWe, Growatt |
| **E-learning** | Podrobnosti k dohledání. Odkaz rozešlu. |
| **Teams** | Společný chat pro dotazy |
| **Ticket** | Eskalace na reklamace nebo technickou podporu |

> „Nyní přepnu na e-learning, který jsem k tomu připravil. Je v něm podrobně vše, co jsme dnes viděli, plus témata, na která jsme se nedostali — chybové kódy, postup u stavu Offline, zakládání instalace do monitoringu.
>
> **Neprocházíme ho teď společně.** Rozešlu vám odkaz, je to webová stránka, otevřete si ji kdykoli. Není to úkol a není nutné projít ho celý — je to příručka.
>
> A pokud v něm něco nenajdete, doplníme to. Buď rozšíříme tahák, nebo připravíme krátký návod. Stačí napsat na Teams."

---

## 7:28–7:30 · Závěr a dotazy (2 min)

📺 **NA OBRAZOVCE:** úvodní stránka e-learningu.

> „Shrnu to do čtyř bodů.
>
> **Za prvé** — Growatt rozpoznáte podle štítku, instalaci dohledáte podle **sériového čísla měniče** v portálu `oss.growatt.com`.
> **Za druhé** — v detailu zařízení přečtete stav, výrobu, napětí na fázích i stav baterie.
> **Za třetí** — když je instalace Offline, necháte si po telefonu popsat kontrolku a displej na měniči. Zelená znamená, že vyrábí a jde jen o komunikaci.
> **Za čtvrté** — minimální nabití baterie a přetok do sítě se nastavují přes **Set the device**; přetok jen na základě zadání.
>
> Tolik ode mě. Podívám se do chatu — máte nějaké dotazy?"

*Chvíli počkej. V online formátu trvá déle, než se někdo ozve.*

---

## Připravené odpovědi na dotazy

**„Proč zase další systém?"**
> „Protože je to jiný výrobce a má vlastní portál — stejně jako SolaX má svůj. Sloučit to nelze."

**„Musíme se to učit nazpaměť?"**
> „Ne. Právě proto vznikl tahák a e-learning."

**„Jaký objem to bude?"**
> „Zpočátku minimální. Servis se spouští v září, první instalace očekáváme v říjnu, objem poroste postupně."

**„Můžeme tedy zákazníkovi přenastavit baterii sami?"**
> „Minimální nabití ano, pokud o to zákazník požádá — jen si vždy poznamenejte původní hodnotu a po uložení ověřte, že se změna propsala. Přetok do sítě ne bez zadání, ten vychází z podmínek připojení."

**„Co když si nebudu vědět rady?"**
> „Založíte ticket nebo se zeptáte na Teams. To je správný postup, nikoli selhání."

**„A co [detail, na který neznáš odpověď]?"**
> „Dobrý dotaz, na který teď nemám odpověď. Zjistím to a napíšu na Teams." — a pak to skutečně udělej.

---

## Když se něco pokazí

| Situace | Řešení |
|---|---|
| Portál není dostupný | Dokonči ukázku na snímcích v e-learningu |
| Nepodaří se přihlásit | Neopakuj pokusy, po pěti se účet zamkne na 15 minut |
| `Set the device` vypadá jinak, než čekáš | Neimprovizuj do hloubky — „Rozložení si projdeme v samostatném návodu", a jdi dál |
| **Nestíháš** | Zkrať bod 3 ukázky (grafy). **Nezkracuj úvod, nastavení ani část „Jak s tím naložit".** |
| Máš čas navíc | V Historical Data ukaž `Vpv2`/`Ppv2` — jsou nulové, protože je osazený jen jeden string. Dobrá ukázka toho, co v datech jde vyčíst. |
| Nikdo se neptá | Normální v online formátu. „Kdyby vás něco napadlo později, pište na Teams." |

---

## Časový rozpis

| Čas | Část | Na obrazovce | Min |
|---|---|---|---|
| 7:00 | Úvod — program a rozsah | e-learning, úvod | 3 |
| 7:03 | Co je Growatt | beze změny | 2 |
| 7:05 | Uspořádání a dvě sériová čísla | e-learning, modul 2 | 3 |
| 7:08 | **Živá ukázka** | **portál OSS** | **14** |
| 7:22 | Jak s tím naložit + ověření po telefonu | detail měniče | 4 |
| 7:26 | Kam se obrátit | e-learning, moduly | 2 |
| 7:28 | Závěr a dotazy | e-learning, úvod | 2 |
| **7:30** | **konec** | | **30** |

### Rozpad ukázky

| Bod | Co | Min |
|---|---|---|
| 1 | Přihlášení, výběr serveru, menu | 2 |
| 2 | Dohledání `TPJ4CD200Z`, záložky, State a Last update | 3 |
| 3 | Detail měniče — hlavička, dlaždice, Problem List, grafy, Historical Data | 6 |
| 4 | `Set the device` — SOC baterie a přetok do sítě | 3 |
