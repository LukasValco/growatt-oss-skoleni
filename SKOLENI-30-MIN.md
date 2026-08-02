# Growatt — seznámení pro poruchovou linku

**Kdy:** 7:00–7:30 · **Délka:** 30 minut včetně dotazů
**Formát:** sdílená obrazovka, živá ukázka na testovací instalaci
**Publikum:** kolegové z poruchové linky, kteří už pracují v 10+ systémech

---

## Co je cílem (a co není)

**Cíl:** aby věděli, že se můžou setkat s Growattem, poznali ho, našli zákazníka v portálu a řekli, jestli instalace komunikuje. Tím jejich práce končí.

**Není cílem:** aby uměli diagnostikovat, číst chybové kódy, cokoliv nastavovat nebo si něco pamatovat.

> **Tři věty, se kterými mají odejít:**
> 1. Můžu narazit na Growatt. Poznám ho podle jména na střídači.
> 2. Umím zákazníka najít a říct, jestli to komunikuje.
> 3. Všechno ostatní předávám dál — a mám kam.

---

## Co dnes NEŘÍKÁME

Drž se toho. Každá z těchto věcí zabere 5 minut a rozbije dojem „nic vám nepřibývá":

- ❌ Chybové kódy a jejich tabulky
- ❌ Vzdálené nastavení parametrů (SOC, export limit, režimy)
- ❌ Přidávání zákazníka do monitoringu
- ❌ Datový model End User → Plant → Device jako teorii
- ❌ Rozdíl mezi OSS / ShineServer / ShinePhone
- ❌ Intelligent Alert, Historical Data, analýza podvýkonu
- ❌ Záložky typů zařízení (On-Grid Storage vs Hybrid Inverter)

Když se na něco z toho někdo zeptá: **„Dobrá otázka, je to v e-learningu. Dneska to nepotřebujete."**

---

## Příprava — 10 minut předem

- [ ] **Přihlášen v OSS** — ne naživo v 7:00
- [ ] **Testovací instalace otevřená** v druhé záložce, ověřeno že stav je `Normal` a data tečou
- [ ] **SN testovací instalace do schránky** — budeš ho vkládat
- [ ] **Písmo v prohlížeči na 125 %** — v 7 ráno na sdílené obrazovce
- [ ] **E-learning otevřený** jako záloha, kdyby portál nejel
- [ ] Zavřené osobní záložky a notifikace

> ⚠️ **Máš jen jednu testovací instalaci a je zdravá.** Offline ani poruchu neukážeš. Neřeš to — v scénáři je to ošetřené tak, že Offline **popíšeš slovy** a přiznáš, že na to zatím nemáš co ukázat. Nepředstírej.

---

# SCÉNÁŘ

---

## 7:00–7:03 · Úvod (3 min)

*Tohle je nejdůležitější část celého školení. Když tady neuspěješ, zbytek si neposlechnou.*

> „Dobré ráno. Budu tady půl hodiny, ani o minutu víc.
>
> Než začnu, řeknu rovnou to, co si teď myslíte. Že přichází jedenáctý systém, ve kterém máte umět dělat. Vím, v kolika systémech se pohybujete, a chápu, že tohle není zpráva, na kterou jste čekali.
>
> Takže rovnou: **dneska vám nic nepřibývá.** Nebudu vás učit nový systém ovládat. Nebudu po vás chtít, abyste si něco pamatovali. A nic z toho, co dnes ukážu, nebudete potřebovat dřív než někdy v říjnu."

**Pauza.** Nech to dosednout.

> „Co se děje: v září spouštíme nabídku servisu pro střídače značky **Growatt**. To znamená, že někdy od podzimu se vám může ozvat zákazník, který má na zdi Growatta místo SolaXe nebo GoodWe.
>
> A já nechci, aby vás to zaskočilo. Chci, abyste v tu chvíli věděli tři věci: co to je, kde toho zákazníka najdete, a komu to předáte. To je celé. Půl hodiny."

> „Nemusíte si nic zapisovat. Všechno, co dnes uvidíte, dostanete v taháku a v e-learningu, ke kterému se můžete kdykoliv vrátit."

---

## 7:03–7:06 · Co je Growatt (3 min)

*Bez portálu. Krátce.*

> „Growatt je čínský výrobce střídačů, velký hráč, u nás ho montuje spousta firem. Pro vás je podstatné jediné: **je to další značka, která dělá to samé co SolaX nebo GoodWe.** Mění stejnosměrný proud z panelů na střídavý do domu, u hybridních modelů k tomu řídí baterii.
>
> Poznáte ho jednoduše — zákazník vám přečte, co má napsané na krabici na zdi. Stojí tam **Growatt**. Typicky uvidíte označení začínající **SPH**, to jsou ty hybridní s baterií, kterých bude většina.
>
> Funguje to úplně stejně jako u ostatních značek: střídač měří, malý wifi klíč to posílá na internet, a my se na to díváme v portálu. Jenom ten portál je jiný."

**Co musí zaznít:** Growatt = další značka téhož. Nic principiálně nového.

---

## 7:06–7:10 · Jediná věc, kterou si mají odnést (4 min)

*Tohle je jádro. Když si zapamatují jen jednu věc, tak tuhle.*

> „Než se podíváme do portálu, jedna věc, která vám ušetří nejvíc práce. Platí u Growattu stejně jako u ostatních značek, takže to není nic nového — jen to chci mít jistotu, že to víme všichni.
>
> Ke střídači patří malá krabička, **datalogger** — wifi klíč, který posílá data na internet. A ten může přestat fungovat úplně nezávisle na tom, jestli fotovoltaika funguje.
>
> Prakticky to znamená: když v portálu uvidíte, že instalace **nekomunikuje**, neznamená to, že je rozbitá. Nejčastěji si zákazník změnil heslo od wifi nebo vyměnil router. Fotovoltaika si venku klidně vyrábí dál, jenom nám o tom nepíše."

> „Proč vám to říkám: protože tohle je rozdíl mezi 'pošleme technika za dvě stě kilometrů' a 'pane Nováku, změnil jste heslo od wifi?'. **Nekomunikuje ≠ rozbité.** Když si z dneška odnesete jednu jedinou větu, ať je to tahle."

**Co musí zaznít:** nekomunikuje ≠ rozbité.
**Co neříkat:** slova Offline, Fault, Normal zatím ne. Přijdou u obrazovky.

---

## 7:10–7:21 · Živá ukázka (11 min)

> „A teď se na to podíváme. Ukážu vám přesně to, co budete dělat vy — nic víc."

### 1) Přihlášení (2 min)

🖱 `oss.growatt.com` → přihlašovací stránka

> „Portál se jmenuje **OSS**. Adresa `oss.growatt.com`, dostanete ji v taháku, dejte si ji do záložek.
>
> Jediná věc, na kterou tady dejte pozor —"

🖱 **Ukaž výběr serveru.**

> „— tenhle výběr nahoře. Musí tam být **Other Countries and Regions Globally**. Ano, Česko je 'ostatní země', dává to smysl asi jako všechno ostatní. Když si vyberete špatně, přihlásíte se, projde to bez chyby — a uvidíte prázdný účet. Žádná hláška, prostě prázdno.
>
> Takže: **prázdný účet po přihlášení = špatně zvolený server.** Odhlásit, přihlásit znovu. Je to v taháku."

### 2) Dohledání zákazníka (4 min)

> „Volá zákazník. První otázka, kterou mu položíte, je vždycky stejná: **'Přečtete mi prosím sériové číslo ze střídače?'** Je na displeji nebo na štítku ze strany krabice."

🖱 `Monitoring & Management` → `Device List`

> „V portálu jdete sem — Monitoring and Management, Device List. Seznam zařízení."

🖱 Vlož SN do pole **Serial Number** → **Inquire**

> „Sériové číslo sem, Enter. A je to."

**Pauza. Nech je vidět, že to je jeden krok.**

> „Tohle je devadesát procent toho, co budete v tomhle portálu dělat. Najít zákazníka podle sériového čísla. Když ho nemá po ruce, jde hledat i podle jména nebo názvu elektrárny, ale to je v e-learningu — sériové číslo je nejrychlejší a nejspolehlivější."

### 3) Co si přečíst (4 min)

🖱 Ukaž nalezený řádek. **Ukazuj myší, o kterém sloupci mluvíš.**

> „A teď to hlavní. V tom řádku jsou dva sloupce, které vás zajímají. Zbytek ignorujte."

🖱 Ukaž **State**

> „**State** — stav. Tady vidíte **Normal**, což znamená, že střídač normálně jede. To je stav, který uvidíte nejčastěji.
>
> Můžou tam být i jiné hodnoty. **Waiting** znamená, že čeká na světlo — ráno, večer, pod mrakem. Není to porucha. **Fault** znamená, že střídač sám hlásí konkrétní problém. A **Offline** — to je přesně to, o čem jsem mluvil před chvílí. Nedorazila data. Nejspíš wifina, ne porucha."

> „Přiznám se rovnou: máme zatím jednu jedinou testovací instalaci a ta je zdravá, takže vám Offline ani poruchu naživo neukážu. Až budeme mít reálné zákazníky, ukážu vám to na živém příkladu."

🖱 Ukaž **Last update**

> „Druhý sloupec — **Last update**. Kdy naposledy dorazila data. Když je stav Offline, tohle vám řekne, jak dlouho už. Jestli deset minut, tak asi nic. Jestli tři týdny, je něco fakt špatně."

> „**State a Last update.** Dva sloupce. Z těch dvou už poznáte, o čem ten hovor bude."

### 4) Detail — jen ukázat, že existuje (1 min)

🖱 Dvojklik na zařízení → detail

> „Když na to dvakrát kliknete, otevře se detail — výroba, grafy, historie. Nebudu to procházet, nepotřebujete to. Jen ať víte, že to tady je, kdyby se vás zákazník ptal, kolik včera vyrobil."

🖱 Zavři to. **Nikam dál neklikej.**

---

## 7:21–7:25 · Co s tím dál (4 min)

> „Takže zákazníka máte, stav vidíte. Co dál? Tohle je ta nejdůležitější tabulka dneška."

| Co vidíte | Co uděláte |
|---|---|
| **Normal** a zákazník si stěžuje na výrobu | Zeptejte se, jak dlouho a o kolik. Založte ticket. |
| **Offline** | Zeptejte se: neměnil jste heslo od wifi? router? Když ano — víme, kde je problém. Ticket. |
| **Fault** | Nechte si přečíst, co je na displeji, a zapište to. Ticket. |
| **Cokoliv nejasného** | Ticket. Nebo se zeptejte na Teams. |

> „Všimněte si, že na konci každého řádku je **ticket**. To je záměr.
>
> **Po vás se nechce, abyste to vyřešili.** Po vás se chce, abyste zákazníka našli, řekli, co vidíte na obrazovce, a předali to dál se smysluplným popisem. Rozdíl mezi ticketem 'nefunguje fotovoltaika' a ticketem 'Growatt SPH, stav Offline, poslední data před dvěma týdny, zákazník měnil router' je pro kolegy ze servisu obrovský.
>
> A to je celé, co po vás chci. Najít, podívat se, popsat, předat."

---

## 7:25–7:28 · Kam se obrátit (3 min)

> „Nic z toho si nemusíte pamatovat. Máte čtyři záchranné sítě a rád bych, abyste je používali."

| Kde | Na co |
|---|---|
| **Tahák** | Jedna stránka, všechny značky pohromadě — SolaX, GoodWe, Growatt. Adresa portálu, kde hledat, co znamenají stavy. |
| **E-learning** | Když si budete chtít něco dohledat nebo projít v klidu. Odkaz pošlu. |
| **Teams** | Náš společný chat. Zeptejte se, klidně blbě. Radši třikrát než jednou špatně. |
| **Ticket** | Eskalace na reklamace nebo technickou podporu. |

🖱 **Krátce ukaž e-learning** — proklikni sidebar, ať vidí, že existuje.

> „E-learning je referenční materiál, ne domácí úkol. Nemusíte ho procházet celý. Když si ho chcete projít, začněte moduly o přihlášení a dohledání zákazníka — zbytek je na dohledávání, až to budete potřebovat.
>
> A ještě jednou: **první reálný hovor přijde nejdřív někdy v říjnu.** Máte čas. Nemusíte nic umět dnes."

---

## 7:28–7:30 · Závěr a dotazy (2 min)

> „Shrnu to do tří vět a končíme.
>
> **Za prvé** — od podzimu se můžete setkat se střídačem Growatt. Poznáte ho podle jména na krabici.
> **Za druhé** — najdete zákazníka podle sériového čísla v portálu OSS a podíváte se na dva sloupce: State a Last update.
> **Za třetí** — popíšete, co vidíte, a předáte to dál. Vyřešit to není vaše práce.
>
> To je všechno. Máte nějaké dotazy?"

---

## Připravené odpovědi na dotazy

Nejpravděpodobnější otázky a jak na ně:

**„Proč zase další systém?"**
> „Protože je to jiný výrobce a má vlastní portál — stejně jako SolaX má svůj. Nedá se to sloučit. Ale prakticky v něm budete dělat jednu jedinou věc: vyhledávat podle sériového čísla. Nic víc."

**„Musíme se to učit nazpaměť?"**
> „Ne. Proto je tahák a e-learning. Chci, abyste věděli, že to existuje a kde to hledat — ne abyste to uměli."

**„Kolik toho bude?"**
> „Zpočátku minimum. Servis se spouští v září, reálné instalace se u nás začnou objevovat v říjnu a poroste to postupně. Nebude to náraz."

**„Co když nebudu vědět, co s tím?"**
> „Tak založíte ticket nebo se zeptáte na Teams. To je správná odpověď, ne selhání. Nikdo po vás nechce, abyste opravovali fotovoltaiku po telefonu."

**„Máme na to nějaký čas navíc?"**
> *Na tohle si připrav odpověď podle toho, jak to máte nastavené — je to legitimní otázka a vyhýbavá odpověď ti sebere důvěru.*

**„Bude to i pro střídače X?"**
> *Když neznáš odpověď: „Nevím, zjistím a napíšu na Teams." A pak to fakt udělej.*

---

## Když se něco pokazí

| Problém | Řešení |
|---|---|
| Portál nejede | Dojedeš demo na screenshotech v e-learningu — jsou tam všechny obrazovky |
| Nemůžeš se přihlásit | Nezkoušej třikrát, zamkne se to na 15 minut. Jeď z e-learningu. |
| Testovací instalace je Offline | Ideální! Ukaž to jako živý příklad a vysvětli na tom „nekomunikuje ≠ rozbité" |
| Nestíháš | Zkrať část 7:03–7:06 (co je Growatt) a zkrácený detail v ukázce. **Nikdy nekracuj úvod a část „co s tím dál".** |
| Rozjede se debata o zahlcení systémy | Nech ji chvíli běžet, neodbývej ji. Pak: „Souhlasím, a proto je dnešek na půl hodiny a proto po vás nechci, abyste si něco pamatovali." |

---

## Časový rozpis

| Čas | Část | Min |
|---|---|---|
| 7:00 | Úvod — odzbrojení | 3 |
| 7:03 | Co je Growatt | 3 |
| 7:06 | Nekomunikuje ≠ rozbité | 4 |
| 7:10 | **Živá ukázka** | **11** |
| 7:21 | Co s tím dál — eskalace | 4 |
| 7:25 | Kam se obrátit | 3 |
| 7:28 | Závěr a dotazy | 2 |
| **7:30** | **konec** | **30** |
