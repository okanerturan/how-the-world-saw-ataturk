# Candidates — Funeral delegations (21 Nov 1938) + Dağlı telegram corpus

HUNT seam 5. Round 3 (Oct 2026). Built from: Delpher/KB wires (Havas 13, 17, 25 Nov; Reuter 21 Nov;
Berlin wire 18 Nov), Tüylü Turan 2019 (Spanish press), Uyanıker 2020 (naval logs), Dağlı 2023
(`sources/yabanci-ulkeler-hastalik-vefat.pdf`), a Soviet-archive feature, English/Turkish Wikipedia
(leads only). Built nodes: **PROMOTED** `Foreign Delegations at the Funeral, November 1938` (Events),
`Albert Sarraut`, `Konstantin von Neurath`, `Vladimir Potemkin`, `Bernardo Giner de los Ríos`,
`Noël Fiessinger`.

## A. The delegation table (country · delegate · role · source · tier)

Tier key: P wire/archive · S scholarly · J journalism · T Wikipedia-only (unverified).

| Country | Delegate(s) | Role | Source | Tier | Status |
|---|---|---|---|---|---|
| France | Albert Sarraut | Interior Minister; reached Istanbul 18 Nov; still in Ankara 25 Nov | Havas 17 Nov; Havas 25 Nov; Tüylü Turan | P+S | **PROMOTED** (person node) |
| Germany | Konstantin von Neurath | min. without portfolio, Hitler's envoy; arrives Ankara 19 Nov | Berlin wire 18 Nov; Havas 17/22 Nov | P | **PROMOTED** |
| Italy | Baron Pompeo Aloisi | senior diplomat | Havas 17 Nov; Tüylü Turan | P+S | lead — no node (bio only M; verify) |
| USSR | Vladimir Potemkin; Adm. Yumashev; Amb. Terentyev (+ "Vice-Adm. Toumatuev" in Tüylü Turan — likely the same Yumashev, garbled) | First Deputy FM; fleet cmdr; ambassador | Havas 13/17 Nov; NRC 26 Nov; uwidata (RGAVMF) | P+J | **PROMOTED** |
| UK | Field Marshal Lord Birdwood (for George VI); Adm. Sir Dudley Pound; 200 marines + *Malaya* band; naval attaché H. A. Packer liaised | royal rep; C-in-C Med. | Reuter 21 Nov; Uyanıker | P+S | existing Birdwood node ✅; Pound — lead (T/S only) |
| Greece | Ioannis Metaxas (PM); destroyer *Hydra* (Capt. Ikonomu) | head of govt | Havas 17 Nov | P | existing node ✅ (attendance now announced twice: 12 Nov + 17 Nov) |
| Yugoslavia | Army Gen. **Milutin** Nedić | Min. of Army & Navy (25 Aug 1938–26 Aug 1939) | Havas 17 Nov; Boran 2011 p.512 | P+S+T | **correction** — see C |
| Bulgaria | Minister of War (name?) + detachment | — | Havas 17 Nov | P | name open |
| Romania | Minister of Air (name?) + detachment; *Regina Maria* (Lt-Cdr Macellariu) | — | Havas 17 Nov; Uyanıker | P+S | name open |
| Albania | Minister of Justice (name?) | — | Havas 17 Nov | P | name open |
| Afghanistan | "an uncle of the King" (name?) | Zahir Shah's family | Havas 17 Nov; Tüylü Turan | P+S | name open; **Amanullah contradicted** — see C |
| Iran | military detachment (delegate?) | guard of honour | Havas 17 Nov | P | name open |
| Spain (Republic) | B. Giner de los Ríos; Gen. Riquelme; V-Adm. Matz; R-Adm. Fuentes; Calderón | Negrín cabinet, 18 Nov | Tüylü Turan | S | **PROMOTED** (Giner) |
| League of Nations | "F. Walters"; Aghnides; Erim | Walters was Deputy SG (M) | Tüylü Turan citing LoN bulletin | S | lead — Aghnides (Greek, LoN Disarmament) and "Erim" (Nihat Erim?) unverified |
| 19 more: Belgium, Czechoslovakia, China, Denmark, Egypt, Estonia, Finland, Hungary, Iraq, Japan, Latvia, Lithuania, Netherlands, Norway, Poland, Sweden, Switzerland, Syria, USA | none named | — | English Wikipedia | T | **open** — not in Havas special-delegation list; likely resident ambassadors |

## B. Dağlı 2023 — the people in the telegram corpus

Mined from `sources/yabanci-ulkeler-hastalik-vefat.pdf` (text via `pdftotext`; pypdf not installed here).
All are CA = Cumhurbaşkanlığı Arşivi references as printed by Dağlı. Tier S for the existence/content
of each letter (Dağlı's reading of archive files), not for anything beyond.

| Sender | Date · place | What they wrote | CA ref | Disposition |
|---|---|---|---|---|
| Abdullah I of Jordan | Apr 1938 | "I read of your illness in the newspaper; I am anxious and distressed" | 01008484-2 | existing node `Abdullah I of Jordan`: add as ledger upgrade |
| Dr André Pirim (Kasapyan family) | 2 Apr 1938 | Turkey's Armenian Catholics wish "the permanent existence" and health of "our great leader" | 01019988-116 | in card |
| Archbp Boğos Kireçyan | 3 Apr 1938 | "may the young Turkish Republic be sheltered beneath your wings for years" | 01019988-106 | **lead**: Armenian Catholic head's loyalty address; sensitive thread — pair with an Armenian-community card, neutral voice |
| İvan Dimitrof, teacher, Sofia | 8 Aug 1938 | folk cure: wooden stick pressed on navel, "Tree of Life" | 01019578-80 | in card (colour) |
| Raul D. Gherculescu | 20 Oct 1938 | son of Romanian military attaché met in Sofia 1913; "I treasure your memory from my childhood" | 01019989-148 | in card; link to Bulgarian-period Atatürk biography |
| Herta Seitner (German) | 25 Oct 1938 | recommends a doctor; letter read to Refik Saydam | 01019989-45 | in card |
| Milan Bukelitsa, merchant, Valjevo | 26 Oct 1938 | "for the happiness of Turkish and Balkan peoples" | 01019989-329 | in card |
| Wilhelm Bauer; Walter Hüller; Rose Reichenbach (Germans) | Oct 1938 | healing wishes; medication advice | — | in card |
| Dr Jean Billac (France) | 21 Oct 1938 | offers to cure cirrhosis, "I have always been your admirer", encloses patient addresses | 01019989-99 | in card |
| Prof. Noël Fiessinger | Nov 1938 | condolence cable from Paris | 02011847-86 | **PROMOTED** (person node) |
| Four pupils, Comilla Zilla School, Bengal | Nov 1938 | letter of grief, "may his soul sleep in peace" | 01016478-142 | in card; Bengal thread → `Kazi Nazrul Islam` |
| Aladar V. Simonffy (Pester Lloyd, 10 Nov) | press | compares Atatürk to Sultan Orhan and Mussolini ("what the Duce is for Italy today"); popular, "some opponents", "the most advanced man of his nation and time" | 01008485-62/63 | **lead** Hungarian card (with Çolak 2003) |
| Danail Krapçeff (Zora, 11 Nov) | press | "Atatürk did not extend Turkey's borders…but gathered shattered forces"; "fire temperament" will be missed | 01008485-64/65 | **lead** — supplements `Bulgarian Mourning, November 1938` |
| Al-Ahram (11 Nov) | press | "the man who tore up treaties… died"; greater than Hitler, Mussolini, Roosevelt | 01008485-6/7 | **lead** Egypt card (other agent) |
| New York World-Telegram (11 Nov) | press | "Sultan and Caliph in reality"; "Turkey's New Deal" | 01008485-8/10 | lead US card |
| Atinaika Nea (21 Nov) | press | "Happy dead" (Plutarch); Balkan peoples weep too | 01008485-1/3 | lead Greek card |
| Kölnische Volkszeitung (11 Nov); Völkischer Beobachter (11 Nov) | press | "all the German people take part sincerely"; VB repeats Hitler's 1933 interview | 01008485-59/61 | Germany cards (other agents) |
| Giornale d'Italia (12 Nov) | press | ignored the death; ran "İsmet İnönü" | 01008485-8 | lead — Italian silence is itself a datum |

Dry: Dağlı names **no** head-of-state letters beyond Abdullah I; the royal/presidential cables are in
the TBMM volumes below.

## C. Corrections to existing vault text (also in ledger_funeral.md)

- **Nedić**: `Death and State Funeral of Atatürk` says "Milan Nedić for Yugoslavia". The Yugoslav
  Army & Navy minister in Nov 1938 was **Milutin** Nedić; Milan became minister only Aug 1939.
- **Amanullah**: Havas, 17 Nov (four Dutch papers): Afghanistan represented "by an uncle of the
  King". No source puts Amanullah in Ankara. Downgrade ⚠️ → "contradicted for the official delegation;
  private attendance unattested." The line in `Amanullah Khan` ("the delegation lists … include the
  exiled king") should be removed.
- **Counts**: "17 nations" ≈ Havas special delegations; "28 countries" and Wikipedia's 32 names
  unsourced; and **Time's "every foreign diplomat"** line quoted in Wikipedia belongs to the 1953
  reburial, not 1938.

## D. Next steps / open leads

| Lead | Tier | Next step |
|---|---|---|
| Ulus, 16 Nov 1938, "Yabancı devletleri temsil edecek heyetler" | P | Not online in anything fetched; Ulus archive (TBMM/Milli Kütüphane browser) — likely the full delegate list |
| Boran 2011, Atatürk Yolu 47, pp. 488–520 (DOI 10.1501/Tite_0000000334) | S | DergiPark page found (ankuayd/article/22469) but PDF id not resolved by `fetch`; Academia copy truncated — get via browser |
| Uzun 2009 (Atatürk Yolu 43) and Üçüncü 2013 (JASSS 6/7) | S | Both funeral-ceremony studies; fetch via DergiPark |
| Atabey 2012, "Atatürk'e Denizden Yapılan Cenaze Töreni", AAMD 28/83 | S | Naval ring + Italian ship |
| TBMM, *Atatürk'ün Ölümü Dolayısıyla Yabancı Ülkelerden Büyük Millet Meclisine Gelen Taziyetnameler* c.1–2 (acikerisim.tbmm.gov.tr, 11543/2467) | P | **Largest unmined corpus**: every foreign head of state/parliament condolence; tr-Wikipedia quotes dozens (Roosevelt, Carol II, Baumann, Kalinin, Litvinov, Onni Talas, Azeri émigré Mehdiyev…). Download PDF, mine by country. |
| RGAVMF f. r-1678 / AVPRF reports (Yumashev 28 Nov; Soviet embassy "Atatürk's death and funeral") | P | uwidata feature only; Russian archive route |
| British: Sonyel, *Belleten* 25/140 (1971), "İngiliz Belgelerinin Işığı Altında Atatürk'ün Son Günleri" | S | FO 371 on Loraine, Pound, Birdwood |
| Pompeo Aloisi; Dudley Pound; Milutin Nedić | M/T | Bios not yet verified here; candidates for round 4 person nodes |
| Greek, Romanian, Bulgarian war/air/justice ministers by name | P | Delpher 21–22 Nov regional dailies + Gallica/ANNO |
| Franco's Spain at the funeral? | P | Diario de Burgos 20–24 Nov (Tüylü Turan cites it but names only Republic's mission) |
| Afghan "uncle of the King" | P | Candidates (M): Hashim Khan, Shah Mahmud Khan, Shah Wali Khan — resolve via Afghan/Turkish press |
| NYT "Ataturk" editorial, 11 Nov 1938 | P | `nytimes.com/1938/11/11/archives/ataturk.html` — leads to US card |

## Round 4 additions (asia / b11_asia)

- **TBMM condolence volumes mined** (handle 11543/2467): PDFs retrievable via the DSpace 7 REST API; OCR via
  macOS Vision. Built `Condolence Telegrams to Ankara, November 1938` (Events). Nothing in the volumes
  names a Reza Shah, Chiang Kai-shek or Mussolini cable (index-based). Index-only/unread: Kalinin (USSR),
  Abdul Aziz (Saudi), Spanish Senate president, Arabic-script Lebanese sheets.
- **Dağlı 2023 remainder**: the press tributes it quotes (Pester Lloyd/Simonffy, Zora/Krapçeff, Al-Ahram,
  NY World-Telegram, Atinaika Nea, Kölnische Volkszeitung, VB, Giornale d'Italia) are already listed in
  table B; no further named senders in the text beyond the Comilla pupils. Remaining value is in the
  press-quote texts themselves (Dağlı §4.1–4.6) — feed to the Hungary/Bulgaria/Egypt cards.
- **New named delegates/senders**: none for the funeral delegation list itself; the telegram volumes add
  who *wrote* rather than who *came*. Joseph Lyons (Australia) wired the Assembly, confirming that the
  Dominions wrote separately from London.
- Lead: Salt Research "Atatürk in the Press: November 10 Archive" (~1,000 clippings) — check DSpace API.

## Round 10 (taziyet) — the TBMM condolence volumes read against the page images

Corpus: `sources/tbmm-taziyetname-1938/c1.pdf`, `c2.pdf` (PDF pages below); images rendered into
`tools/.state/round10/taziyet_png/`. **PROMOTED** `Heads of State Write to the Assembly, November 1938`
(Events; 10 new records in `tools/.state/round10/gazes_taziyet.jsonl`). Ledger: `ledger_taziyet.md`.

New gazes (all P, era funeral): Federzoni/Italian Senate (c1 p7), Lebrun (c2 p49), Baumann/Swiss Federal Council
(c2 p19), Prince Paul (c2 p10), Yugoslav Senate (c2 p11), Ćirić (c2 p12), Mercouriou of Salonica (c1 p11),
Hermann Jansen (c2 p15), George Clerk (c2 p43), Romanian women's associations (c2 p25).

Upgrades of existing records (same telegram, not duplicated): Nahhas (c2 p26, quote available), Azaña (c2 p10,
now primary, admiring), Ciano/Italian Chamber (c1 p8), Hitler (c2 p14, German original, "Reiches"), Hirohito
(c1 p28, French original), Roosevelt (c1 p35), Rahmat Ali (c1 p36), Lyons (c2 p28), Husseini (c2 p21), Farouk (c2 p6).

### Protocol only (sent condolences; words do not characterise): candidate "they sent condolences" layer
| Sender | Vol · PDF page |
|---|---|
| Karlis Ulmanis (Latvia) | c1 p3 |
| Abdulaziz / Ibn Saud (Riyadh, Arabic in Latin letters) | c1 p9 |
| Boris III (Bulgaria) | c1 p13 |
| Gustaf V (Sweden) | c1 p16 |
| Konstantin Päts (Estonia) | c1 p17 |
| Zog (Albania) | c1 p25 |
| Prince Takamatsu | c1 p27 |
| Hirohito (French; "vive affliction") | c1 p28 |
| Tokugawa Iemasa for the Japan–Turkey society ("grand chef") | c1 p30 |
| Ignacy Mościcki | c1 p32 |
| Abbas Hilmi II (Vevey, Turkish) | c1 p37 |
| Hatay head of state Sökmen / Assembly president Türkmen | c2 pp4–5 |
| Emir Abdullah (Turkish) | c2 p7 |
| Iraqi Chamber; King Ghazi (Baghdad) | c2 pp8–9 |
| Göring (Reichstag; "ihres großen Präsidenten", borderline honorific, judged protocol) | c2 p15 |
| Carol II | c2 p23 |
| Horthy | c2 p25 |
| Hashim al-Atassi ("éminent chef") | c2 p29 |
| Zahir Shah (Persian in Latin letters; services-not-forgotten clause, needs a Persian reader) | c2 p39 |
| Christian X | c2 p41 |
| Grand Duchess Charlotte; Lázaro Cárdenas ("su gran presidente") | c2 p45 |
| Haakon VII | c2 p48 |
| Victor Emmanuel III (Pisa) | c2 p53 |
| Resulzade (Turkish) | c1 p34 |

### Dry ends
- Kalinin: index only, no sheet in c2 (c2 p46 is the Turkish ambassador in Moscow).
- INC president / Subhas Chandra Bose: no sheet. The index line "Hindistan, Kongre Başkanı" matches the
  Zoutpansberg Indian Congress sheet (c2 p44, South Africa), adjacent to the Israel Council sheet in the same
  order. The Wikipedia lead on Bose is not supported by the volume.
- Pages without text: c2 p56 is a photograph; p57 and index pp58–61 only.

## Round 11 — foreign statesmen in the TBMM plenary (`b19_statesmen.py`, slug `statesmen`)

Source: TBMM, *Tarihe Düşülen Notlar-2: Yabancı Devlet Adamlarının Genel Kurul Konuşmaları* (Feb 2012), handle
https://acikerisim.tbmm.gov.tr/handle/11543/122 (314 PDF pages; printed page = PDF page − 11). Note: the bundled
`sources/tbmm-foreign-statesmen-2012/text.txt` is truncated at the 1965 Bourguiba speech; the full text layer was
re-extracted with PDFKit (`tools/.state/round11/full.txt`). All 48 speeches were searched for Atatürk / Kemal / Gazi / Mustafa.
Speaker, office and date are from the book's headings. Stored quotes were read from rendered page images (`tools/.state/round11/p*.png`).

### Promoted (21 records, node *Foreign Statesmen Address the Assembly, 1956–2010*; era posthumous, evidence P)
Mirza 1956-07-16 (PDF 14) · Nawab Muzaffar Ali 1957-06-07 (18) · Podgorny 1965-01-05 (36, 38) · Bourguiba 1965-03-25 (43–44, 48; conflicted) ·
Lei Jieqiong 1984-12-05 (50) · Kobayashi 1985-04-23 (53) · Zahir Hacı İsmail 1988-04-23 (61) · Kelemen 1991-04-23 (71) ·
Elçibey 1992-06-26 (83) · Haydar Aliyev 1994-02-09 (97; also 1997, 2001: one record) · Denktaş 1998-04-23 (131; also 1997, 2004) ·
Clinton 1999-11-15 (142–143) · Prodi 2004-01-15 (180) · Musharraf 2004-01-20 (187) · Cox 2004-03-02 (210) · Borrell 2004-12-03 (220) ·
Van der Linden 2005-11-09 (229) · Barroso 2008-04-10 (240) · Obama 2009-04-06 (254) · Nazarbayev 2009-10-22 (268–269) · Wulff 2010-10-19 (285).
Existing person notes (Bourguiba, Musharraf, Jinnah, Anıtkabir) are linked from the Events note, not duplicated; the records'
`node` is the Events note, which carries the quote text.

### Ritual mention (not stored)
- Serdar Fahir Hikmat (Iranian delegation head), 1958-11-01, PDF 20–21: "founder of the great Turkish nation" while recalling Reza Shah's 1934 visit.
- Hüber Reymon (Swiss Council of States), 1989-04-23, PDF 64: "Cumhuriyetin Kurucusu ... eseri".
- Ahmed Urai (Malaysian Senate), 1990-04-23, PDF 68: slogan closing.
- Abdildin Serikbolsun (Kazakh Supreme Council), 1992-04-23, PDF 74–75: quotes Atatürk, one epithet.
- Kwaśniewski (Poland), 2000-04-14, PDF 164: chronology.
- Sahad Muradov (Turkmenistan), 2000-04-23, PDF 168–169: ceremonial, sovereignty and peace sayings.
- Kuchma (Ukraine), 2000-11-23, PDF 172, 175: dates 1919 landing; quotes economy-and-science line.
- Peres (Israel), 2007-11-13, PDF 232: opens with an Atatürk quotation.
- Cavaco Silva (Portugal), 2009-05-12, PDF 262, 264: quotation only.
- Gilani (Pakistan), 2010-12-07, PDF 289: Jinnah Avenue / Atatürk Avenue.
- Atambayev (Kyrgyzstan), 2012-01-12, PDF 310: First Assembly elected Mustafa Kemal president.

### Dry ends
⌀ dug, no mention of Atatürk: Mercan (Iraq, 1955), Sukarno (24 Nisan 1959), Gerstenmaier (1964), Flanagan (1986), Lulling (1987),
Denktaş 1993/1999/2003, Cengiç (Bosnia 1992), İlham Aliyev 2004/2008, Yudhoyono 2010, Abbas 2007, Buzek 2011. The brief's
"Pakistani leader about 1954" is İskender Mirza, 16 Temmuz 1956 per the book heading.

### Next steps
- The book does not say in which language each speech was delivered; Azerbaijani speeches print Azerbaijani forms with Turkish glosses.
- Aliyev 1997 and 2001, Denktaş 1997 and 2004 could become extra dated records if repeat speeches are wanted.
