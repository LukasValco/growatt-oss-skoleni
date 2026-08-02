# Growatt — seznámení pro poruchovou linku

**Kdy:** 7:00–7:30 · **Formát:** MS Teams, bez kamery — jedna sdílená obrazovka, druhá s tímto scénářem

## Časování textu

Mluvené pasáže mají zhruba **3 700 slov**, což je při běžném prezentačním tempu **26–28 minut čistého mluvení**. Zbytek do třicítky je prostor na klikání, načítání stránek a dotazy. Pasáže označené *(vypustitelné)* můžeš bez ztráty smyslu přeskočit, když se budeš opožďovat.

---

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
| Druhý měnič v instalaci | `TPJ4CD201V` · datalogger `XGD5BLB26G` |
| Alias prvního měniče | `Dehtáře 4` |

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

| Čas | Okno | Kde přesně |
|---|---|---|
| 7:00 | E-learning | **úvodní stránka** (modul „Úvod") |
| 7:04 | E-learning | beze změny |
| 7:06 | E-learning | modul **`2` Datový model** → schéma hierarchie, pak sekce *Dvě různá sériová čísla* |
| 7:09 | **Portál OSS** | přihlašovací stránka → Device List → detail měniče |
| 7:22 | Portál OSS | zůstáváš v **Device Detail** `TPJ4CD200Z` |
| 7:26 | E-learning | **levé menu s moduly** |
| 7:28 | E-learning | zpět na **úvodní stránku** |

---

## Příprava — 15 minut předem

- [ ] **Přihlášen v OSS**, `TPJ4CD200Z` dohledané, detail otevřený ve vlastní záložce
- [ ] **Sériové číslo `TPJ4CD200Z` ve schránce**
- [ ] **Projdi si předem „Set the device"** — po odsouhlasení disclaimeru se otevře dlouhý dialog. Vyzkoušej si, kde je *Load First* a kde *Set Exportlimit*, ať se v něm při ukázce nehledáš.
- [ ] **Nic v dialogu neukládej** — zavírej tlačítkem **Cancel**
- [ ] E-learning otevřený na úvodní stránce
- [ ] Vyzkoušené sdílení v Teams a přepínání mezi okny
- [ ] Písmo v prohlížeči na 125 %, zavřené notifikace

---

# SCÉNÁŘ

---

## 7:00–7:04 · Úvod (4 min)

📺 **NA OBRAZOVCE:** e-learning, **úvodní stránka** (modul „Úvod" s domečkem). Sdílení spusť ještě před začátkem, ať mají na co koukat.

### Téma a co je na obrazovce

> „Dobré ráno. Dnešní téma je nový typ střídače, se kterým se na lince můžete od podzimu setkat — značka **Growatt**. V září spouštíme nabídku servisu pro tyto střídače, takže od října vám mohou volat zákazníci, kteří mají doma Growatta.
>
> To, co teď vidíte na obrazovce, je **e-learning**, který jsem k tomu připravil. Odkaz na něj vám rozešlu, takže ho budete mít k dispozici. **Dnes ho neprocházíme celý** — beru si ho jen jako pomůcku a promítnu z něj dvě tři místa. Je to příručka na později, ne úkol na dnešek.
>
> Program má čtyři části. **Co Growatt je** a jak ho rozpoznáte. **Jak dohledáte instalaci** v jejich monitorovacím portálu. **Co si z portálu přečtete** — v jakém je instalace stavu, kolik vyrábí, jestli má napětí na fázích. A **kde se nastavují základní parametry**, jako minimální nabití baterie nebo povolený přetok do sítě. Většinu si ukážeme naživo, budu klikat v ostrém portálu na skutečné instalaci.
>
> Dotazy prosím pište průběžně do chatu. Budu ho sledovat a odpovím buď rovnou, nebo na konci."

### Otevřeně k tomu, co jim přibývá

*Až po programu. Nejdřív musí vědět, o čem se bavíme.*

> „Ještě než začneme, chci otevřeně pojmenovat dvě věci.
>
> **Za prvé:** ano, přibývá vám další značka a další portál. Nebudu tvrdit opak — vím, s kolika systémy denně pracujete, a ujišťovat vás, že se nic nemění, by nebylo férové.
>
> Co ale mohu upřesnit, je **rozsah**. Nebudete v tom portálu nic opravovat, nebudete nic zakládat a nemusíte si z něj nic pamatovat zpaměti. Dostanete tahák i tenhle e-learning, do kterých se kdykoli podíváte. A hlavně — **postup je stejný jako u SolaXu a GoodWe.** Zákazník zavolá, vy ho podle sériového čísla dohledáte, podíváte se, v jakém je stavu, a podle toho buď poradíte po telefonu, nebo předáte dál. Ten postup znáte. Mění se jen adresa portálu a to, kde přesně které tlačítko sedí.
>
> **Za druhé, a to považuji za podstatnější:** Growatt je **třetí a zároveň poslední značka**, kterou do servisu přidáváme. Mám to potvrzené. Takže tímhle to končí — SolaX, GoodWe, Growatt, a žádný další portál už nepřijde.
>
> A počty nebudou velké. Očekáváme spíš **nižší jednotky instalací**, ne stovky. Servis se rozjíždí v září, první instalace se u nás objeví někdy v říjnu a poroste to postupně, ne nárazem. Máte tedy zhruba dva měsíce, než vám kvůli Growattu vůbec někdo zavolá — a do té doby nemusíte umět vůbec nic. Dnešek berte jako to, že o tom víte a víte, kde si to najít."

**Co musí zaznít:** třetí a poslední značka · nižší počty · e-learning dostanou a dnes ho neprocházíme. Tyhle tři věty rozhodují o tom, jestli si poslechnou zbytek.

---

## 7:04–7:06 · Co je Growatt (2 min)

📺 **NA OBRAZOVCE:** beze změny — pořád úvodní stránka e-learningu.

> „Growatt je čínský výrobce střídačů. Patří mezi největší na trhu, celosvětově je to jeden z nejprodávanějších výrobců a v Česku ho instaluje řada montážních firem. Pro vaši práci je ale podstatné jediné: **plní stejnou funkci jako SolaX nebo GoodWe.** Je to krabice na zdi, která bere stejnosměrný proud z panelů na střeše a dělá z něj střídavý, který se použije v domě.
>
> Rozpoznáte ji podle **typového štítku na měniči**. Je tam uvedeno **Growatt** a typové označení. Když se vás zákazník zeptá, co má za značku, nebo když si nejste jistí, ať vám ten štítek přečte — je na boku té krabice.
>
> Nejčastěji se setkáte s řadou **SPH**. To jsou **hybridní** střídače, tedy takové, které kromě panelů řídí i baterii. Hybridní znamená, že přebytek výroby neposílá rovnou do sítě, ale nejdřív ho uloží do baterie, a večer, když panely nevyrábějí, ho z baterie zase bere. Většina toho, co dneska montujeme, jsou právě hybridy s baterií.
>
> Naše referenční instalace, na které vám to budu ukazovat, má **dva kusy SPH 10000TL3 BH-UP**, každý o výkonu deset kilowattů. Můžete ale narazit i na obyčejné on-grid střídače bez baterie — v portálu jsou pak jen na jiné záložce, jinak se pracuje stejně.
>
> A princip, jak se k datům dostaneme, znáte z ostatních značek. Střídač měří provozní data. K němu je připojený **komunikační modul** — v praxi malý wi-fi adaptér, kterému se říká datalogger. Ten data odesílá přes domácí wi-fi na server výrobce. A my se na ně díváme v monitorovacím portálu. Ten portál se jmenuje **OSS**, adresa je `oss.growatt.com`.
>
> Zákazník má k dispozici mobilní aplikaci a vidí v ní v podstatě to samé co vy. Vy budete pracovat s webovým rozhraním, kde toho vidíte víc a máte i věci, ke kterým se zákazník nedostane."

---

## 7:06–7:09 · Uspořádání a dvě sériová čísla (3 min)

📺 **NA OBRAZOVCE:** v e-learningu klikni v levém menu na **`2` Datový model**. Zůstaň nahoře u sekce **„Hierarchie: End User → Plant → Device"** — je tam nakreslené schéma.

> „Přepnu na druhý modul e-learningu, na schéma. Než se podíváme do portálu, potřebujete vědět, jak je v tom systému všechno poskládané — pak vám ten portál bude dávat smysl a nebudete v něm bloudit."

🖱 Ukaž schéma a projeď ho kurzorem shora dolů.

> „Jsou to **tři úrovně** a je to stejná logika jako u ostatních značek.
>
> Nahoře **zákazník**, v portálu End User — majitel instalace, ten, kdo vám volá. Pod ním **elektrárna**, anglicky Plant, tedy konkrétní fotovoltaika na konkrétní adrese. A pod ní **zařízení** — střídače, baterie, případně wallbox.
>
> A tady pozor: jedna elektrárna může mít **víc než jeden střídač**. Naše referenční instalace je přesně takový případ — jedna elektrárna, dva střídače, každý se svým vlastním komunikačním modulem. Když tedy zákazník řekne, že mu nefunguje fotovoltaika, může být problém jen v jednom ze dvou."

### Dvě různá sériová čísla

📺 **NA OBRAZOVCE:** sjeď v témže modulu níž na sekci **„Dvě různá sériová čísla — nepleť si je"**. Je tam srovnávací tabulka obou čísel i s konkrétními hodnotami z Dubné 93 a pod ní červený rámeček.

> „Sjedu o kousek níž, protože tady je věc, která dělá v praxi nejvíc zmatku. Každá instalace má **dvě sériová čísla** a na první pohled vypadají podobně.
>
> **První je sériové číslo měniče** — v portálu je vedené jako Device SN. Zákazník ho najde na **typovém štítku na boku měniče**. Tady v tabulce vidíte to naše: začíná na T-P-J. **To je číslo, se kterým budete pracovat vy**, podle něj zákazníka dohledáte.
>
> **Druhé je sériové číslo dataloggeru**, tedy toho wi-fi adaptéru. To je na štítku přímo na něm a v tabulce vidíte, že vypadá úplně jinak — začíná na X-G-D. Patří jinému zařízení.
>
> Proč vám to říkám: když se zákazníka zeptáte na sériové číslo a on vám přečte to z wi-fi klíče, budete ho hledat marně a budete si myslet, že ho v systému nemáme. Takže si vždycky ověřte, **odkud to číslo čte** — má to být štítek na samotném měniči, ne na té malé krabičce vedle.
>
> A ještě jedna souvislost, kterou uvidíte za chvíli v portálu: **každý měnič má svůj vlastní datalogger.** Naše instalace má dva měniče, a tedy i dvě různá čísla dataloggerů.
>
> Číslo dataloggeru budete potřebovat jen výjimečně — používá se při zakládání instalace do monitoringu spolu s ověřovacím kódem, takzvaným Check Code. Ale to dělá montážní firma nebo zákazník přes mobilní aplikaci, ne vy. **Vy vyhledáváte podle sériového čísla měniče.**
>
> Za chvíli si obě čísla ukážu přímo v portálu, kde jsou vedle sebe v jednom řádku."

### Komunikace není totéž co výroba

📺 **NA OBRAZOVCE:** beze změny, pořád modul 2.

> „A ještě jedna věc, kterou už asi znáte z jiných značek, ale je natolik důležitá, že ji pro jistotu zopakuji. Ten komunikační modul může přestat fungovat **úplně nezávisle** na tom, jestli elektrárna vyrábí.
>
> Prakticky to znamená: když v portálu uvidíte, že instalace **nekomunikuje**, neznamená to automaticky, že je vadná. Nejčastější příčinou je, že si zákazník **změnil heslo k wi-fi** nebo **vyměnil router**. Ten adaptér se pak nemá kam připojit a přestane data odesílat. Elektrárna přitom může na střeše úplně normálně vyrábět — jen o sobě nedává vědět.
>
> Proč to zdůrazňuji: je to rozdíl mezi tím, jestli pošlete technika na výjezd, nebo jestli se zákazníka po telefonu zeptáte na jednu otázku. **Nekomunikuje neznamená vadné.** Za chvíli si řekneme, jak si přímo při hovoru ověříte, která z těch dvou možností to je."

---

## 7:09–7:22 · Živá ukázka (13 min)

📺 **NA OBRAZOVCE:** přepni na **druhé okno prohlížeče — živý portál OSS**, přihlašovací stránku.

> „Nyní přepnu do portálu a projdeme si to přesně tak, jak to budete dělat vy."

### 1) Přihlášení (2 min)

📺 **NA OBRAZOVCE:** přihlašovací stránka `oss.growatt.com` — černé pozadí, vpravo bílé přihlašovací okno.

> „Adresa je `oss.growatt.com`, najdete ji v taháku a doporučuji si ji dát do záložek. Přihlašovací stránka vypadá takhle — vpravo je klasické okno na účet a heslo."

🖱 **Ukaž čtyři tlačítka nad přihlašovacím oknem:** Mainland of China · United States & Canada · **Other Countries and Regions Globally** · Australia & New Zealand

> „A teď jediná věc, na kterou vás tady chci upozornit, protože je to nejčastější chyba vůbec. Nad přihlašovacím oknem jsou **čtyři tlačítka** a vybírá se jimi server podle regionu. Growatt má servery rozdělené na Čínu, Spojené státy s Kanadou, Austrálii s Novým Zélandem a pak zbytek světa.
>
> Pro nás platí to **třetí zleva: Other Countries and Regions Globally.** Ano, Česká republika je pro Growatt „ostatní země". Když je správně zvolené, svítí zeleně — vidíte to tady.
>
> A proč je to důležité: když si vyberete špatný server, ono vás to **normálně přihlásí**. Nedostanete chybovou hlášku, nedostanete žádné varování. Jenom uvidíte prázdný účet, ve kterém nebude ani jeden zákazník. A vy budete přesvědčení, že toho člověka nemáme v systému.
>
> Takže si to prosím zapamatujte takhle: **prázdný účet po přihlášení znamená špatně zvolený server.** Odhlásit, přihlásit znovu, zkontrolovat tlačítko. Je to i v taháku."

📺 **NA OBRAZOVCE:** po přihlášení — úvodní obrazovka portálu, vlevo tmavé svislé menu.

🖱 Projeď kurzorem **levé svislé menu** shora dolů.

> „Takhle vypadá portál po přihlášení. Vlevo je menu a přiznávám, že na první pohled vypadá docela nabitě — je tam **PV Plant Design**, **Monitoring & Management**, **Service Hall**, **Data Analysis**, **After-sales O&M**, **Supply System**.
>
> Nenechte se tím vystrašit. **Vy budete pracovat prakticky s jedinou položkou**, a to **Monitoring & Management**. Když ji rozkliknu, jsou pod ní **Plant List** — seznam elektráren, **Device List** — seznam zařízení, a **End Users** — seznam zákazníků. To odpovídá přesně těm třem úrovním, které jsme si před chvílí ukázali na schématu.
>
> Zbytek menu je pro projektanty, pro reklamační oddělení a pro správce účtů. Vy tam nemáte co dělat a klidně to ignorujte."

### 2) Dohledání instalace (2 min)

📺 **NA OBRAZOVCE:** `Monitoring & Management` → **`Device List`** → záložka **On-Grid Storage**.

> „Volá zákazník a přečte vám sériové číslo ze štítku na měniči. Jdu do **Device List**, tedy seznamu zařízení."

🖱 Ukaž **záložky nad seznamem:** On-grid Inverter · Off-Grid Storage Inverter · **On-Grid Storage** · WIT · Microgrid Household Energy Storage · EV Charger · Battery · Plug-in Storage

> „Nahoře jsou **záložky podle typu zařízení** — obyčejné on-grid střídače, off-grid, hybridy, nabíječky elektromobilů, baterie a tak dál.
>
> A tady je past, na kterou vás radši připravím dopředu. **Hybridní střídače, tedy ty s baterií — kterých bude většina — jsou pod záložkou `On-Grid Storage`.** Ne pod tou, kterou byste čekali podle názvu. Takže když budete vyhledávat a nic nenajdete, neznamená to, že zákazník v systému není. Zkuste nejdřív přepnout záložku. Je to v taháku."

🖱 Vlož `TPJ4CD200Z` do pole **Serial Number** → **Inquire**

> „Sériové číslo vložím sem, do pole **Serial Number**, a dám **Inquire**. Výsledek je okamžitý. Tímhle jediným krokem vyřídíte drtivou většinu dohledávání."

🖱 Ukaž **řádek s počítadly** nad seznamem: `Abnormal: 0 · Offline: 0 · Standby: 0 · Self Test: 0 · Online: 2 · Total: 2`

> „Než se podíváme na samotný řádek — všimněte si téhle lišty. Je to **rychlý přehled, kolik zařízení je v jakém stavu**.
>
> **Abnormal** znamená hlášenou závadu. **Offline**, že nedorazila data. **Standby** je klidový režim, tedy střídač zrovna nevyrábí, ale nic nehlásí. **Self Test** je probíhající samotest. A **Online** je normální provoz.
>
> U nás jsou dvě zařízení online a nula ve všech ostatních sloupcích, takže je instalace v pořádku. Jedním pohledem."

🖱 Ukaž sloupce **State** a **Lastest Upgrade Time**. Kurzorem ukazuj, o kterém mluvíš.

> „A teď pozor na drobnost, která mate. V té liště nahoře se ten stav jmenuje **Online**, ale ve sloupci **State** u konkrétního řádku je napsáno **Normal**. Je to jedna a tatáž věc — portál na dvou místech jedné obrazovky používá jiné slovo. Zapamatujte si tedy: **zdravý střídač má ve sloupci State napsáno Normal.**
>
> Hned vedle je sloupec **Lastest Upgrade Time**, tedy čas poslední aktualizace údajů. Když je zařízení ve stavu Offline, právě tenhle údaj vám řekne, **jak dlouho už mlčí**. Deset minut je úplně běžné, to se občas stane. Tři týdny už znamenají, že se něco doopravdy stalo."

🖱 Projeď kurzorem zbytek řádku zleva doprava.

> „A ve stejném řádku máte všechno ostatní, aniž byste museli někam proklikávat. **Device SN** je sériové číslo měniče, **Nameplate model** typ, **Affiliated plant** elektrárna, **User Name** zákazník. A tady o kus dál **Datalogger** — to je to druhé sériové číslo, o kterém jsme mluvili. Vidíte, že jsou opravdu různá.
>
> Vpravo je **Daily Generation**, tedy dnešní výroba, **Total output energy** celkově za celou dobu, **Current Power** okamžitý výkon a **Rated Power** jmenovitý výkon měniče.
>
> A všimněte si, že jsou tu **dva řádky** — dva střídače u téže elektrárny, každý se svým dataloggerem. Přesně to, o čem jsem mluvil u schématu."

### 3) Detail měniče — co se z něj dá vyčíst (5 min)

📺 **NA OBRAZOVCE:** **Device Detail** měniče `TPJ4CD200Z` — otevřeš ho dvojklikem na řádek.

🖱 **Dvojklik** na řádek `TPJ4CD200Z`

> „Dvojklikem se dostanu do detailu zařízení. Tohle je obrazovka, kde je toho k vidění nejvíc, a projdeme ji shora dolů. Neříkám vám to proto, abyste si to pamatovali — jen ať víte, co všechno tady je, kdyby se vás zákazník na něco zeptal."

🖱 Ukaž **hlavičku** — Serial Number, Datalogger, User, Plant, Rated Power

> „Úplně nahoře je **identifikace**. Sériové číslo měniče, pod ním sériové číslo dataloggeru, uživatel, elektrárna a jmenovitý výkon. Když někam hlásíte problém, tohle jsou údaje, které opíšete."

🖱 Ukaž **čtyři dlaždice**

> „Pod tím jsou **čtyři dlaždice** a ty vám dají celou energetickou bilanci domu.
>
> **Generation** — kolik elektrárna **vyrobila**. **Battery discharge** — kolik se **vybilo z baterie**. **Feed back to the grid** — kolik šlo **do sítě**, tedy přetok. A **Power consumption** — kolik **spotřeboval dům**.
>
> U každé dlaždice je hodnota za **tento měsíc**, pod ní **dnešek** a **celkový součet** za celou dobu provozu. Když se vás tedy zákazník zeptá, kolik mu to vyrobilo — ať už za dnešek nebo celkově — odpověď je tady a nemusíte nikam chodit."

🖱 Ukaž **Problem List**

> „Následuje **Problem List**, tedy přehled závad. U naší instalace je **prázdný**, což je dobrá zpráva — znamená to, že tenhle střídač zatím nikdy žádnou závadu nenahlásil.
>
> Kdyby tady byl řádek, uvidíte v něm sériové číslo, typ zařízení, **čas, kdy k závadě došlo**, popis problému a případně řešení. Vaším úkolem v takové chvíli je **opsat ten chybový kód do ticketu**. Co který kód znamená, najdete v taháku i v e-learningu — nemusíte je znát zpaměti, je jich několik desítek.
>
> A vpravo nahoře je tlačítko **Export Fault Log**, kterým se dá historie závad stáhnout do souboru. To se hodí, když případ předáváte servisu — přiložíte jim rovnou celý výpis."

🖱 Ukaž **graf SOC**

> „Pod tím je **graf nabití baterie** v procentech, v čase. Na tomhle je hezky vidět, jak se přes den baterie nabíjela — ráno byla někde na třiceti procentech, přes poledne se nabila a odpoledne už drží na stu.
>
> Tenhle graf je užitečný, když si zákazník stěžuje, že mu baterie nevydrží přes noc nebo se vůbec nenabíjí. Tady to buď uvidíte, nebo uvidíte, že je všechno v pořádku."

🖱 Ukaž **FIG parameter comparison**. *(Vypustitelné, když nestíháš.)*

> „Následuje **porovnávací graf**, kde si můžete zvolit, co vykreslit — nabíjecí výkon, vybíjecí, tok do sítě nebo spotřebu domu. Jen ať víte, že to tady je."

🖱 Rozbal **Historical Data**

> „A úplně dole je **Historical Data**, tedy podrobná telemetrie. Střídač posílá kompletní sadu údajů zhruba **každých pět minut** a tady jsou všechny za sebou.
>
> Vypadá to jako výpis z bankovního účtu a je toho opravdu hodně — desítky sloupců. Není potřeba tomu rozumět celému. Ukážu vám **čtyři skupiny sloupců**, které se vám můžou hodit."

| Sloupec | Co říká |
|---|---|
| `Status` | provozní režim — u zdravé instalace `PV Bat Online`, tedy běží panely i baterie |
| `Ppv`, `Vpv1`, `Ppv1` | **výkon a napětí z panelů** — tady vidíte, že elektrárna skutečně vyrábí |
| `Vac1`–`Vac3`, `Fac` | **sdružená napětí mezi fázemi** (~400 V) a frekvence sítě |
| `EpsVac1`–`EpsVac3` | napětí na **zálohovaném výstupu** (~230 V na fázi) |
| `SOC`, `VBat` | nabití a napětí baterie |

> „**Status** je provozní režim. Tady je `PV Bat Online`, tedy běží panely i baterie. Kdyby tam stálo jen `Bat Online`, znamenalo by to, že jede jen baterie a z panelů nic nechodí.
>
> **Ppv a Vpv** jsou výkon a napětí z panelů — když se vás někdo zeptá, jestli elektrárna opravdu vyrábí, odpověď je tady, a je to údaj přímo ze střídače. **Vac1 až Vac3** je napětí sítě a **Fac** frekvence, takže dotaz na napětí vyřešíte odsud.
>
> A tady si dejte pozor na jednu věc, o kterou se dá zakopnout. Uvidíte tam čísla kolem **čtyř set deseti voltů** a mohli byste si říct, že je to strašné přepětí. Není. **Growatt v těchhle sloupcích uvádí sdružené napětí, tedy napětí mezi dvěma fázemi, ne mezi fází a nulou.** Naše síť má sdruženě čtyři sta voltů a na fázi dvě stě třicet. Když tedy chcete napětí na fázi, **vydělte to číslo 1,73** — ze čtyř set deseti vám vyjde dvě stě třicet sedm voltů, což je naprosto v pořádku.
>
> Že je to opravdu tak, poznáte i podle sloupců **EpsVac** o kus dál — to je napětí na zálohovaném výstupu a tam jsou čísla kolem dvou set třiceti. Stejná instalace, stejný okamžik, jednou sdruženě a jednou na fázi.
>
> A **SOC** s **VBat** je nabití a napětí baterie."

### 4) Kde se mění nastavení (4 min)

📺 **NA OBRAZOVCE:** pořád **Device Detail** — tlačítka jsou vpravo nahoře v sekci *Device information overview*.

🖱 Ukaž tlačítka vpravo nahoře: **Editing device · Set the device · Set datalogger · Delete device**

> „A poslední část, kterou vám chci ukázat. Vpravo nahoře jsou čtyři tlačítka. **Editing device** je editace údajů o zařízení, **Delete device** smazání — do toho prosím nikdy nechoďte. Nás zajímají zbylá dvě: **Set the device** je nastavení samotného střídače a **Set datalogger** je nastavení komunikačního modulu."

🖱 Klikni **Set the device**. Objeví se **Disclaimer** — nechej ho chvíli na obrazovce.

> „A všimněte si, co se stane jako první. Portál vás nepustí dál, dokud neodsouhlasíte prohlášení výrobce. Přečtu z něj dvě věty:
>
> *Aby bylo možné tuto funkci zapnout, musíte mít odpovídající kvalifikaci a odborné znalosti pro fotovoltaické systémy.* A dále: *provedení této operace může způsobit poruchu nebo částečnou poruchu fotovoltaického systému nebo střídače; veškeré ztráty nese ten, kdo změnu provedl.*
>
> To není naše opatrnost, to je text Growattu. Berte ho jako měřítko toho, s čím se tady pracuje. Neznamená to, že sem nesmíte — znamená to, že sem nechodíte ze zvědavosti a neměníte věci z vlastní iniciativy. Měníte je tehdy, když o to zákazník požádá a vy víte, co ta změna udělá."

🖱 Zaškrtni **I have read and agree to the disclaimer** → **Yes**. Otevře se dialog **Set Hybrid Inverter**.

> „Po odsouhlasení se otevře dialog **Set Hybrid Inverter**. Nahoře je zase **identifikace** — sériové číslo střídače a dataloggeru. Vždycky si ověřte, že měníte správné zařízení, obzvlášť když má zákazník dva jako tady.
>
> Pod tím je **seznam příkazů** a před každým je kolečko. Funguje to tak, že **vyberete jeden příkaz**, vyplníte u něj hodnotu a odešlete. Neposílá se to celé najednou."

🖱 Ukaž **Load First → Discharge Stopped Soc**

> „Nejčastější požadavek, který od zákazníků uslyšíte, je **minimální nabití baterie**. Je pod položkou **Load First** a jmenuje se **Discharge Stopped Soc**. U naší instalace je nastaveno **deset procent** — to znamená, že se baterie nikdy nevybije pod desetinu kapacity.
>
> Proč to zákazníky zajímá: volají, že jim baterie v noci padá na nulu a ráno nemají z čeho brát. Nebo naopak, že jim zbytečně zůstává skoro plná. Tohle je přesně ta hodnota, která to řídí.
>
> Growatt doporučuje zhruba **deset až patnáct procent v létě a kolem čtyřiceti v zimě**. V zimě vyšší proto, aby v baterii zůstala rezerva pro zálohovaný okruh, kdyby vypadla síť."

🖱 Vyjeď nahoru na **Battery First**

> „Kousek výš je **Battery First** a v něm **Charge Stopped Soc** — do kolika se baterie nabije. Tady je sto procent, tedy do plna.
>
> Pod tím je **Ac Charge**, což je nabíjení baterie ze sítě, a k němu **tři časová okna**. A tohle si zapamatujte, protože vám to ušetří práci: **když si zákazník stěžuje, že se baterie chová divně v určitou denní dobu** — třeba že se mu odpoledne vybíjí, i když svítí — **podívejte se nejdřív sem, na tahle časová okna.** Docela často je to zapomenuté nastavení z instalace, ne závada."

🖱 Sjeď dolů na **Set Exportlimit**

> „A poslední věc — **přetok do sítě**. Je to položka **Set Exportlimit**, dole v seznamu. U naší instalace je **zapnutá** a nastavená na **jedenaosmdesát procent**.
>
> Pozor, ten údaj se jmenuje **Limit Power Rate** a je v **procentech jmenovitého výkonu**, ne ve wattech. U desetikilowattového střídače tedy jedenaosmdesát procent odpovídá zhruba osmi kilowattům.
>
> A tady prosím opatrně: povolený přetok **vychází z podmínek připojení s distributorem**. Není to technická drobnost. Když ho zvýšíte, můžete zákazníka dostat do rozporu s tím, co má schváleno. Když ho omylem snížíte, přijde o výnosy a bude to reklamovat. **Neměňte ho z vlastního uvážení — jen na základě konkrétního zadání.**"

🖱 **Zavři dialog tlačítkem Cancel.** Nic neukládej.

> „Zavírám bez uložení. A ještě dvě věci, které platí pro **jakoukoli** změnu, kterou tady kdy budete dělat.
>
> **Za prvé:** nastavení jde přes datalogger do střídače. Střídač tedy **musí být online**. U instalace ve stavu Offline změna prostě nedojde — a co je horší, dialog se může zatvářit, že se uložila.
>
> **Za druhé:** po uložení si hodnotu **načtěte znovu a ověřte**, že se tam skutečně propsala. A poznamenejte si, co jste změnili, kdy a na čí žádost."

---

## 7:22–7:26 · Jak s tím naložit (4 min)

📺 **NA OBRAZOVCE:** zůstáváš v **Device Detail** `TPJ4CD200Z`, ať mají před sebou konkrétní situaci.

> „Tak. Portál jste viděli, teď to nejdůležitější — **jak s tím naložit u skutečného hovoru.** Tohle je část, kterou byste si z dneška měli odnést, i kdybyste na všechno ostatní zapomněli."

| Zjištěný stav | Postup |
|---|---|
| **Normal**, zákazník hlásí nízkou výrobu | Historical Data → `Ppv`. Porovnejte s tím, co hlásí. Ticket. |
| **Abnormal** | Problem List → opište kód. Případně Export Fault Log. Ticket. |
| **Offline** | Ověřte po telefonu, jestli elektrárna vyrábí — viz níže. Ticket i tak. |
| Nejasná situace | Ticket, případně dotaz na Teams. |

> „Projdu ty čtyři situace, do kterých se dostanete.
>
> **První: stav je Normal, ale zákazník tvrdí, že mu to málo vyrábí.** Tady si ho nejdřív poslechněte — ptejte se, **jak dlouho** to trvá a **o kolik** je to méně. Pak se podívejte do Historical Data na sloupec `Ppv` a do dlaždice s výrobou. Buď uvidíte, že opravdu vyrábí míň než dřív, nebo uvidíte, že vyrábí normálně a zákazník jen srovnává červenec s listopadem. V obou případech založte ticket, ale připište, co jste zjistili — tím kolegům ušetříte půl hodiny.
>
> **Druhá: stav je Abnormal.** To znamená, že střídač sám hlásí konkrétní závadu. Otevřete Problem List, **opište chybový kód** a čas, kdy k závadě došlo. Pokud jich je víc, stáhněte Export Fault Log. Ticket. A zákazníkovi řekněte pravdu — že jeho střídač hlásí závadu, kterou předáváte technikům, a někdo se mu ozve.
>
> **Třetí: stav je Offline.** To je ta situace, o které jsme mluvili — nedorazila data. Podívejte se na Lastest Upgrade Time, ať víte, jak dlouho už. A pak — a tohle je ta nejužitečnější věc dneška — si po telefonu ověříte, jestli elektrárna vyrábí. Za chvíli vám řeknu jak.
>
> **A čtvrtá, nejčastější ze všech: nevíte.** Něco nesedí, něco nevypadá standardně, něčemu nerozumíte. To je naprosto v pořádku. Založte ticket a napište do něj, co vidíte. Nebo se zeptejte na Teams. **Nikdo po vás nechce, abyste opravovali fotovoltaiku po telefonu.**"

### Jak po telefonu ověřit, že elektrárna vyrábí

*Toto je nejužitečnější věc pro stav Offline — v portálu nevidíte nic, ale zákazník stojí u měniče.*

> „Vrátím se k tomu stavu Offline, protože tam máte v ruce nástroj, o kterém možná nevíte.
>
> Když je instalace Offline, jste v portálu **slepí**. Data nedorazila, takže nevíte vůbec nic — ani jestli elektrárna vyrábí, ani jestli má závadu. Ale máte na telefonu zákazníka, který může jít k měniči a podívat se.
>
> Poproste ho, ať se podívá na **kontrolku a displej** na měniči. Podle manuálu Growattu platí jednoduché pravidlo: **když měnič pracuje normálně, kontrolka svítí zeleně a na displeji jsou běžné provozní údaje.** Pokud je signalizace **červená**, jde o závadu a je to případ pro servis.
>
> Takže: **zelená kontrolka a normální displej znamená, že elektrárna běží** a problém je jenom v komunikaci. To je hovor, který dořešíte po telefonu — zeptáte se na wi-fi, na router, na to, jestli se něco neměnilo — a nikam se nejezdí. Naopak **červená znamená skutečnou závadu** a je to úplně jiný ticket.
>
> Tímhle jedním dotazem tedy odlišíte dvě situace, které v portálu vypadají úplně stejně."

### Co napsat do ticketu

> „A poslední věc k eskalaci. Když případ předáváte, snažte se do ticketu dát tohle:
>
> **Značku a typ střídače**, tedy Growatt a označení z portálu. **Sériové číslo.** **Stav**, který jste viděli. Když je Offline, tak i **jak dlouho už**. Když je Abnormal, tak **chybový kód**. Co říkal zákazník a co jste s ním ověřili — třeba jestli měnil router nebo jak svítí kontrolka.
>
> Rozdíl mezi ticketem, kde stojí *‚nefunguje fotovoltaika'*, a ticketem, kde stojí *‚Growatt SPH, sériové číslo takové a takové, stav Offline, poslední data před dvěma týdny, zákazník měnil router, kontrolka na měniči svítí zeleně'* — ten rozdíl je pro kolegy ze servisu **zásadní**. V tom druhém případě už vědí, co mají dělat, a nemusí to celé zjišťovat znovu.
>
> Takže znovu, ve čtyřech slovech: **dohledat, ověřit stav, popsat, předat.** To je celý rozsah toho, co se po vás chce."

---

## 7:26–7:28 · Kam se obrátit (2 min)

📺 **NA OBRAZOVCE:** přepni zpět na **okno s e-learningem** a projeď kurzorem **levé menu s moduly**. Cca 30 sekund, **neprocházej ho**.

> „Nic z toho, co jsem dnes říkal, si nemusíte pamatovat. Budete mít **čtyři opory** a rád bych, abyste je používali."

| Zdroj | K čemu |
|---|---|
| **Tahák** | Jedna stránka pro všechny značky — SolaX, GoodWe, Growatt |
| **E-learning** | Podrobnosti k dohledání. Odkaz rozešlu. |
| **Teams** | Společný chat pro dotazy |
| **Ticket** | Eskalace na reklamace nebo technickou podporu |

> „**Tahák** — jedna stránka, na které budou všechny tři značky pohromadě. SolaX, GoodWe, Growatt. Adresy portálů, kde v každém z nich hledat, co znamenají stavy a nejčastější chybové kódy. To je věc, kterou si vytisknete a máte u telefonu.
>
> **E-learning** — přepnu zpátky na ten, o kterém jsem mluvil na začátku. Vidíte v menu, že má sedm modulů. Je v něm podrobně všechno, co jsme dnes viděli, plus témata, na která jsme se nedostali: chybové kódy i s tabulkami, podrobný postup u stavu Offline, jak se instalace zakládá do monitoringu. Jak jsem říkal, **neprocházíme ho teď společně** a není to úkol. Rozešlu vám odkaz, otevřete si ho kdykoli v klidu. Je to příručka, do které se podíváte, až budete něco potřebovat.
>
> **Teams** — náš společný chat. Ptejte se tam průběžně, i na věci, které vám připadají triviální. Radši se zeptejte třikrát, než jednou špatně poradíte zákazníkovi.
>
> **A ticket** — eskalace na tým reklamací nebo technické podpory. To je normální pracovní postup, ne přiznání, že si nevíte rady.
>
> A pokud v žádném z těch zdrojů něco nenajdete, nebo se ukáže, že potřebujete víc, **doplníme to**. Buď rozšíříme tahák, nebo připravíme krátký návod k tomu konkrétnímu tématu. Stačí napsat na Teams."

---

## 7:28–7:30 · Závěr a dotazy (2 min)

📺 **NA OBRAZOVCE:** klikni v e-learningu na první položku menu — **úvodní stránku**.

> „Shrnu to do čtyř bodů.
>
> **Za prvé** — Growatt rozpoznáte podle štítku, instalaci dohledáte podle **sériového čísla měniče** v portálu `oss.growatt.com`.
> **Za druhé** — ve sloupci **State** přečtete stav (zdravý měnič má *Normal*) a v detailu zařízení výrobu, napětí na fázích i stav baterie.
> **Za třetí** — když je instalace Offline, necháte si po telefonu popsat kontrolku a displej na měniči. Zelená znamená, že vyrábí a jde jen o komunikaci.
> **Za čtvrté** — minimální nabití baterie (*Load First → Discharge Stopped Soc*) a přetok do sítě (*Set Exportlimit*) se mění přes **Set the device**; přetok jen na základě zadání.
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
| Ztratíš se v dialogu `Set Hybrid Inverter` | Je dlouhý. Když nenajdeš položku do deseti sekund, řekni „Podrobný návod k nastavení připravíme zvlášť" a zavři ho. |
| **Nestíháš** | V bodě 3 vynech porovnávací graf a detail elektrárny. **Nezkracuj úvod, nastavení ani část „Jak s tím naložit".** |
| Máš čas navíc | V Historical Data ukaž `Vpv2`/`Ppv2` — jsou nulové, protože je osazený jen jeden string. Dobrá ukázka toho, co v datech jde vyčíst. |
| Nikdo se neptá | Normální v online formátu. „Kdyby vás něco napadlo později, pište na Teams." |

---

## Časový rozpis

| Čas | Část | Na obrazovce | Min |
|---|---|---|---|
| 7:00 | Úvod — program, rozsah, e-learning | e-learning, úvodní stránka | 4 |
| 7:04 | Co je Growatt | beze změny | 2 |
| 7:06 | Uspořádání a dvě sériová čísla | e-learning, modul 2 | 3 |
| 7:09 | **Živá ukázka** | **portál OSS** | **13** |
| 7:22 | Jak s tím naložit + ověření po telefonu | detail měniče | 4 |
| 7:26 | Kam se obrátit | e-learning, moduly | 2 |
| 7:28 | Závěr a dotazy | e-learning, úvod | 2 |
| **7:30** | **konec** | | **30** |

### Rozpad ukázky

| Bod | Co | Min |
|---|---|---|
| 1 | Přihlášení, výběr serveru, menu | 2 |
| 2 | Dohledání `TPJ4CD200Z`, záložky, počítadla, State a Lastest Upgrade Time | 2 |
| 3 | Detail měniče — hlavička, dlaždice, Problem List, grafy, Historical Data | 5 |
| 4 | `Set the device` — disclaimer, SOC baterie, Set Exportlimit | 4 |
