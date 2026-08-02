# Growatt — seznámení pro poruchovou linku

**Kdy:** 7:00–7:30 · **Délka:** 30 minut včetně dotazů
**Formát:** sdílená obrazovka, živá ukázka na testovací instalaci
**Publikum:** kolegové z poruchové linky, kteří už pracují v 10+ systémech

---

## Co je cílem (a co není)

**Cíl:** aby věděli, že se můžou setkat s Growattem, poznali ho, našli zákazníka v portálu, přečetli základní stav a věděli, co předat dál.

**Není cílem:** aby to uměli vyřešit, znali chybové kódy zpaměti nebo cokoliv nastavovali.

> **Tři věty, se kterými mají odejít:**
> 1. Můžu narazit na Growatt. Poznám ho podle jména na střídači.
> 2. Najdu zákazníka podle sériového čísla a přečtu, v jakém je stavu.
> 3. Popíšu, co vidím, a předám dál — a mám kam.

---

## Princip: ukázat, ale neučit

Ukazuj klidně víc, než si zapamatují. Cílem je, aby to **jednou viděli** a věděli, že to existuje — ne aby to uměli. U každého detailu, který se otevře, máš připravenou odkládací větu:

> 🗣 **„Tohle je v taháku, nemusíte si to pamatovat."**
> 🗣 **„Detaily jsou v e-learningu, kdykoliv se k tomu vrátíte."**
> 🗣 **„Na tohle uděláme samostatný návod, až to bude aktuální."**
> 🗣 **„Tohle vy dělat nebudete, jen ať víte, že to jde."**

Používej je bez váhání. Drží tempo a zároveň nikoho neodbydou.

---

## Co jen zmíníš a odložíš

Tyhle věci **ukaž nebo zmiň jednou větou** a jdi dál. Nerozvádět:

| Téma | Jak to odbýt |
|---|---|
| Chybové kódy | „Kód opíšete do ticketu. Co znamená, je v taháku." |
| Vzdálené nastavení (SOC, výkon do sítě) | „Jde to i přenastavit, ale to nebudete dělat vy." |
| Přidání zákazníka do monitoringu | „Zakládá to montér přes mobilní appku." |
| Grafy, historie, analýza výroby | „Je toho tady spousta, nepotřebujete to." |
| ShineServer / ShinePhone | „Zákazník má appku, vy máte tenhle web." |

---

## Příprava — 10 minut předem

- [ ] **Přihlášen v OSS** — ne naživo v 7:00
- [ ] **Testovací instalace otevřená** v druhé záložce, ověřeno že stav je `Normal` a data tečou
- [ ] **SN testovací instalace do schránky** — budeš ho vkládat
- [ ] **Písmo v prohlížeči na 125 %** — v 7 ráno na sdílené obrazovce
- [ ] **E-learning otevřený** jako záloha, kdyby portál nejel
- [ ] Zavřené osobní záložky a notifikace

> ⚠️ **Máš jen jednu testovací instalaci a je zdravá.** Offline ani poruchu neukážeš. Scénář to řeší tak, že to **přiznáš nahlas** — a využiješ toho: prázdný Problem List a prázdný operation log jsou samy o sobě dobrá ukázka toho, jak vypadá zdravá instalace.

---

# SCÉNÁŘ

---

## 7:00–7:03 · Úvod (3 min)

*Nejdůležitější část celého školení. Když tady neuspěješ, zbytek si neposlechnou.*

> „Dobré ráno. Budu tady půl hodiny, ani o minutu víc.
>
> Než začnu, řeknu rovnou to, co si teď myslíte. Že přichází jedenáctý systém, ve kterém máte umět dělat. Vím, v kolika systémech se pohybujete, a chápu, že tohle není zpráva, na kterou jste čekali.
>
> Takže rovnou: **dneska vám nic nepřibývá.** Ukážu vám toho možná víc, než budete potřebovat — ale nechci, abyste si to pamatovali. Chci, abyste to jednou viděli a věděli, že to existuje."

**Pauza.** Nech to dosednout.

> „Co se děje: v září spouštíme nabídku servisu pro střídače značky **Growatt**. Reálně se vám první zákazník ozve nejdřív někdy v říjnu. Takže máte spoustu času.
>
> Za těch třicet minut chci, abyste odcházeli se třemi věcmi: co Growatt je, kde toho zákazníka najdete, a co s tím uděláte dál. Všechno ostatní dostanete napsané."

---

## 7:03–7:06 · Co je Growatt (3 min)

*Bez portálu. Krátce.*

> „Growatt je čínský výrobce střídačů, velký hráč, montuje ho u nás spousta firem. Pro vás je podstatné jediné: **je to další značka, která dělá to samé co SolaX nebo GoodWe.**
>
> Poznáte ho jednoduše — zákazník vám přečte, co má napsané na krabici na zdi. Stojí tam **Growatt**. Většinou uvidíte označení začínající **SPH** — to jsou hybridní střídače s baterií, těch bude nejvíc."

> „Jak to funguje, znáte z ostatních značek. Střídač měří, malý wifi klíč posílá data na internet, my se na to díváme v portálu. Portál se jmenuje **OSS**. Zákazník k tomu má mobilní appku, vy máte tenhle web — vidíte to samé, jen vy toho vidíte víc."

---

## 7:06–7:09 · Jak je to poskládané (3 min)

> „Jedna věc na úvod, ať vám portál dává smysl. Je to poskládané ve třech patrech — stejně jako u ostatních značek."

```
👤 Zákazník
   └── 🏭 Jeho fotovoltaika
         └── 🔌 Střídač  +  📡 wifi klíč (datalogger)
```

> „A teď to nejdůležitější, co dneska řeknu. Ten **wifi klíč** může přestat fungovat úplně nezávisle na tom, jestli fotovoltaika jede.
>
> Prakticky: když v portálu uvidíte, že instalace **nekomunikuje**, neznamená to, že je rozbitá. Nejčastěji si zákazník změnil heslo od wifi nebo vyměnil router. Fotovoltaika si venku klidně vyrábí dál, jenom nám o tom nepíše."

> „Proč to zdůrazňuju: tohle je rozdíl mezi 'pošleme technika za dvě stě kilometrů' a 'pane Nováku, měnil jste heslo od wifi?'. **Nekomunikuje ≠ rozbité.** Když si z dneška odnesete jednu jedinou větu, ať je to tahle."

---

## 7:09–7:22 · Živá ukázka (13 min)

> „A teď se na to podíváme. Projdeme to tak, jak to budete dělat vy."

### 1) Přihlášení (2 min)

🖱 `oss.growatt.com`

> „Adresa `oss.growatt.com`, dostanete ji v taháku. Jediná věc, na kterou tady dejte pozor —"

🖱 **Ukaž výběr serveru.**

> „— tenhle výběr nahoře. Musí tam být **Other Countries and Regions Globally**. Ano, Česko je 'ostatní země'. Když si vyberete špatně, přihlásíte se, projde to bez chyby — a uvidíte prázdný účet. Žádná hláška, prostě prázdno.
>
> **Prázdný účet po přihlášení = špatně zvolený server.** Je to v taháku."

🖱 Po přihlášení krátce projeď kurzorem menu.

> „Menu vypadá bohatě, ale vy budete v jedné jediné položce — **Monitoring and Management**. Zbytek klidně ignorujte."

### 2) Dohledání zákazníka (4 min)

> „Volá zákazník. První otázka je vždycky stejná: **'Přečtete mi prosím sériové číslo ze střídače?'** Je na displeji nebo na štítku ze strany."

🖱 `Monitoring & Management` → `Device List` → vlož SN do **Serial Number** → **Inquire**

> „Sériové číslo sem, Enter. A je to. Tohle je devadesát procent toho, co tady budete dělat."

⚠️ **Ukaž záložky nad seznamem** — stojí to 20 sekund a ušetří to hodiny:

> „Jedna past, na kterou vás radši připravím. Nad seznamem jsou záložky podle typu zařízení. Hybridní střídače — ty s baterií, kterých bude většina — jsou pod záložkou **On-Grid Storage**. Ne pod tou, kde byste je čekali.
>
> Takže když hledáte a nic nenajdete, neznamená to, že zákazník neexistuje. Zkuste přepnout záložku. Je to v taháku."

💬 Doplň jednou větou:

> „Když sériové číslo nemá po ruce, jde hledat i podle jména nebo názvu elektrárny. Postup je v e-learningu — sériové číslo je nejrychlejší."

### 3) Co si přečíst v seznamu (3 min)

🖱 Ukaž nalezený řádek. **Ukazuj myší, o kterém sloupci mluvíš.**

> „V tom řádku jsou dva sloupce, které vás zajímají. Zbytek ignorujte."

🖱 **State**

> „**State** — stav. Tady vidíte **Normal**, což znamená, že střídač normálně jede. To uvidíte nejčastěji.
>
> Můžou tam být i jiné hodnoty: **Waiting** — čeká na světlo, ráno nebo pod mrakem, není to porucha. **Fault** — střídač sám hlásí konkrétní problém. A **Offline** — to je to, o čem jsem mluvil, nedorazila data. Nejspíš wifina."

> „Přiznám se rovnou: máme zatím jednu testovací instalaci a ta je zdravá, takže vám Offline ani poruchu naživo neukážu. Až budeme mít reálné zákazníky, doplníme to."

🖱 **Last update**

> „Druhý sloupec — **Last update**, kdy naposledy dorazila data. Když je stav Offline, tohle řekne, jak dlouho už. Deset minut je nic, tři týdny je problém."

> „**State a Last update.** Z těch dvou poznáte, o čem ten hovor bude."

### 4) Detail střídače (3 min)

🖱 Dvojklik na zařízení

> „Když na to dvakrát kliknete, otevře se detail. Projedu to rychle, nemusíte si to pamatovat — jen ať víte, co tady je, kdyby se vás zákazník ptal."

🖱 Ukaž **dlaždice s výrobou** a graf

> „Nahoře je výroba — kolik vyrobil dnes, tento měsíc, celkem. Když se zákazník ptá 'kolik mi to včera udělalo', odpověď je tady."

🖱 Ukaž **Problem List**

> „A tohle je pro vás užitečné: **Problem List**, seznam poruch. Vidíte, že je prázdný — a to je dobrá zpráva, znamená to, že tahle instalace nikdy neměla problém. Když sem přijdete a bude tam řádek s chybovým kódem, **opíšete ten kód do ticketu**. Co který kód znamená, je v taháku a v e-learningu, nemusíte to znát."

### 5) Detail elektrárny (1 min)

🖱 Přejdi na detail elektrárny (Plant)

> „A ještě o patro výš — detail celé elektrárny. Adresa, výkon panelů, kolik zařízení. A historie poruch, která je tady taky prázdná.
>
> To je všechno, co potřebujete vidět. Zbytek portálu klidně ignorujte."

🖱 **Konec ukázky. Dál neklikej.**

---

## 7:22–7:26 · Co s tím dál (4 min)

> „Zákazníka máte, stav vidíte. Co dál? Tohle je nejdůležitější tabulka dneška."

| Co vidíte | Co uděláte |
|---|---|
| **Normal**, ale zákazník si stěžuje na výrobu | Zeptejte se, jak dlouho a o kolik. Ticket. |
| **Offline** | Zeptejte se: neměnil jste heslo od wifi? router? Ticket i tak. |
| **Fault** | Opište kód z Problem Listu nebo z displeje. Ticket. |
| **Cokoliv nejasného** | Ticket. Nebo se zeptejte na Teams. |

> „Všimněte si, že na konci každého řádku je **ticket**. To je záměr.
>
> **Po vás se nechce, abyste to vyřešili.** Po vás se chce, abyste zákazníka našli, popsali, co vidíte, a předali to dál. Rozdíl mezi ticketem 'nefunguje fotovoltaika' a ticketem 'Growatt SPH, stav Offline, poslední data před dvěma týdny, zákazník měnil router' je pro kolegy ze servisu obrovský.
>
> Najít, podívat se, popsat, předat. To je celé."

---

## 7:26–7:28 · Kam se obrátit (2 min)

> „Nic z toho si nemusíte pamatovat. Máte čtyři záchranné sítě."

| Kde | Na co |
|---|---|
| **Tahák** | Jedna stránka, všechny značky — SolaX, GoodWe, Growatt. Adresy, kde hledat, co znamenají stavy, chybové kódy. |
| **E-learning** | Podrobnosti, když si je budete chtít dohledat. Odkaz pošlu. |
| **Teams** | Náš společný chat. Ptejte se, klidně blbě. |
| **Ticket** | Eskalace na reklamace nebo technickou podporu. |

🖱 **Ukaž e-learning — 30 sekund.** Otevři ho, projeď kurzorem sidebar s moduly, zavři. **Neprocházej ho.**

> „Tohle je e-learning, který jsem k tomu udělal. Je v něm podrobně všechno, co jsme dnes viděli, plus věci, na které jsme se nedostali — chybové kódy, co dělat u Offline, jak se zákazník přidává do monitoringu.
>
> **Neprocházíme ho teď spolu.** Pošlu vám na něj odkaz, je to webová stránka, otevřete si ji kdykoliv v klidu. Není to domácí úkol a nemusíte ho projít celý — je to spíš příručka, do které se podíváte, až budete něco potřebovat.
>
> A co v něm nenajdete nebo se ukáže, že potřebujete víc — doděláme. Buď doplníme tahák, nebo uděláme krátký návod. Řekněte si o to na Teams."

---

## 7:28–7:30 · Závěr a dotazy (2 min)

> „Shrnu to do tří vět.
>
> **Za prvé** — od podzimu se můžete setkat se střídačem Growatt, poznáte ho podle jména na krabici.
> **Za druhé** — najdete zákazníka podle sériového čísla v portálu OSS a podíváte se na State a Last update.
> **Za třetí** — popíšete, co vidíte, a předáte dál. Vyřešit to není vaše práce.
>
> Máte nějaké dotazy?"

---

## Připravené odpovědi na dotazy

**„Proč zase další systém?"**
> „Protože je to jiný výrobce a má vlastní portál — stejně jako SolaX má svůj. Nedá se to sloučit. Ale prakticky v něm budete dělat jednu věc: vyhledávat podle sériového čísla."

**„Musíme se to učit nazpaměť?"**
> „Ne. Proto je tahák a e-learning. Chci, abyste věděli, že to existuje a kde to hledat."

**„Kolik toho bude?"**
> „Zpočátku minimum. Servis se spouští v září, reálné instalace se začnou objevovat v říjnu a poroste to postupně. Nebude to náraz."

**„Co když nebudu vědět, co s tím?"**
> „Založíte ticket nebo se zeptáte na Teams. To je správná odpověď, ne selhání."

**„A co [detail, na který nemáš odpověď]?"**
> „Dobrá otázka. Zjistím a napíšu na Teams." — a pak to fakt udělej.

**„Máme na to nějaký čas navíc?"**
> *Připrav si odpověď podle toho, jak to máte nastavené. Vyhýbavá odpověď ti sebere důvěru, kterou sis budoval třicet minut.*

---

## Když se něco pokazí

| Problém | Řešení |
|---|---|
| Portál nejede | Dojedeš demo na screenshotech v e-learningu — jsou tam všechny obrazovky |
| Nemůžeš se přihlásit | Nezkoušej třikrát, zamkne se to na 15 minut. Jeď z e-learningu. |
| Testovací instalace je Offline | Ideální! Ukaž to jako živý příklad „nekomunikuje ≠ rozbité" |
| **Nestíháš** | Zkrať část 7:03–7:06 a v ukázce vynech bod 5 (detail elektrárny). **Nikdy nekracuj úvod a část „co s tím dál".** |
| Máš čas navíc | Vrať se do detailu střídače a ukaž graf výroby za měsíc — hezky se na tom vysvětluje „počasí versus porucha" |
| Rozjede se debata o zahlcení systémy | Nech ji chvíli běžet, neodbývej ji. Pak: „Souhlasím, a proto je dnešek na půl hodiny a proto po vás nechci, abyste si něco pamatovali." |

---

## Časový rozpis

| Čas | Část | Min |
|---|---|---|
| 7:00 | Úvod — odzbrojení | 3 |
| 7:03 | Co je Growatt | 3 |
| 7:06 | Jak je to poskládané + nekomunikuje ≠ rozbité | 3 |
| 7:09 | **Živá ukázka** | **13** |
| 7:22 | Co s tím dál — eskalace | 4 |
| 7:26 | Kam se obrátit | 2 |
| 7:28 | Závěr a dotazy | 2 |
| **7:30** | **konec** | **30** |

### Rozpad ukázky

| Bod | Co | Min |
|---|---|---|
| 1 | Přihlášení + výběr serveru + menu | 2 |
| 2 | Dohledání podle SN + past se záložkami | 4 |
| 3 | State a Last update | 3 |
| 4 | Detail střídače — výroba, Problem List | 3 |
| 5 | Detail elektrárny *(vynechatelné)* | 1 |
