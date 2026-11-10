# HUNT — the Rorschach Census

The campaign document. RESEARCH.md holds method and reading; LEDGER.md holds evidence;
**this file holds the hunt**: who we're looking for, where we've looked, and how. We come back
here every session.

## Mission

Build the maximal catalog of gazes: for **every country**, at least one contemporary
**politician**, one **writer or artist**, and where the record allows, a **soldier, cleric,
scientist, athlete or journalist** of Atatürk's era who said, wrote, painted, legislated or
marched something about him. Working hypothesis (user's, and the vault so far supports it):
no country is empty.

Priorities:
1. **Contemporaries (to 1938)** — the core census.
2. **The funeral fortnight (10–22 Nov 1938)** — the one moment every country looked at once.
3. **Posthumous figures only if major** — Kennedy-tier statesmen, foundational post-colonial
   leaders, reception flashpoints (Mandela, Castro, Musharraf, the 2023 Disney row). No filler.

End state: a dataset dense enough to drive the visualization — a silhouette that genuinely looks
different from every angle because every angle is a sourced gaze.

## The datum schema (the research→viz bridge)

Every **verified** gaze eventually exports one record. Collect toward these fields from day one:

```yaml
id:            kebab-slug
person:        name (or collective: "Sinn Féin press", "KMT officer corps")
country:       polity at the time + modern successor
domain:        politics | letters | arts | military | religion | science | press | sport | diplomacy
era:           contemporary (–1938) | funeral (Nov 1938) | posthumous (1939–)
mirror:        one of the ten taxonomy cards (RESEARCH.md §6)
polarity:      admiring | hostile | conflicted | instrumental | witness
intensity:     1 passing mention · 2 sustained engagement · 3 life- or state-shaping
what_they_saw: one line
artifact:      quote | poem | policy | visit | memoir | artwork | monument | nomination | broadcast
evidence:      P/S/J/F/T (+ LEDGER row)
sources:       [urls, archived]
```

**Datum after round 35 (2026-11-09): 964 gazes (959 checked), 792 voices, 90 countries; admiring 510 (53%), conflicted 138, instrumental 131, hostile 122, witness 63; contemporary 474, funeral 196, posthumous 294.**

**Datum after round 23 (2026-11-04), end of the free-seam campaign: 777 gazes, 635 voices, 75 countries; admiring 387 (50%), hostile 107, conflicted 117, instrumental 110, witness 56; contemporary 399, funeral 180, posthumous 198. Round 23: Indian legislatures 1924–63 (Motilal Nehru, Radhakrishnan, the 1938 condolence with Bhulabhai Desai and Zafar Ali Khan); Congressional Record 1957–90 (Powell, Sikes, Mathias, Byrd). Free seams are exhausted for notable voices; what remains is in 'Only Okan can do these' below.**

**Datum after round 22 (2026-11-03): 759 gazes, 619 voices, 75 countries. Rounds 21–22: Ortega Munilla, Ledesma; Herriot, Pinon, Pernot, Franklin-Bouillon, Oliver Baldwin; Wikisource (Iorga, Nzhdeh ×2, Shant, Lototsky, Kotko, Annadurai, Banerjea, McCabe, Hook); La Turquie kémaliste (Ahmed Haşim, W. L. Wright, Pittard, Ireland, Belge); Westminster via TheyWorkForYou (Eden ×2, Noel-Baker, Selwyn Lloyd, Clement Davies, Hollis, Wigg, MacShane, John Patten, Corbyn); Anzac leaders (Hawke ×2, Howard, Rudd, Abbott ×2, Gillard, Morrison, Peters, Goff); Bundestag (Fischer ×2, Schröder, Weisskirchen, Jung, Müntefering, Hampel, Stercken, Poppe, Althammer, Emmerlich); Congress (Connally, Davis, Pepper ×2, Reynolds, Saylor, Levin, Moynihan, Lantos ×2, Byrd, Gohmert); Hitler 1941 upgraded to the Reichstag protocol's German.**

**Datum after round 20 (2026-11-03): 694 gazes, 561 voices, 73 countries. Round 19: al-Risala via Arabic Wikisource (al-Aqqad, Zayyat, Azzam, Tantawi, Zaki Mubarak ×2, Mandur, Felix Faris, Ahmad Ramzi). Round 20: Aralov, Pilnyak, Deng Zhongxia, Chang Naide; Terada Torahiko via the Aozora mirror. Persian/Urdu (Ganjoor, Rekhta) dry beyond Iqbal.**

**Datum after round 18 (2026-11-03): 680 gazes, 549 voices, 73 countries; admiring 332 (49%), hostile 100, conflicted 107, posthumous 136. Rounds 15–18: the Anıtkabir special book via Turkish press (Elizabeth II, Xi, Merkel, Obama, G. W. Bush, Biden, Charles, Boris Johnson, Hollande, Putin's own 2004 wording and 20 more); Hitler 1941 and Table Talk, Goebbels, Mussolini 1922, Lloyd George 1938, Khrushchev, Nehru 1946, Brzezinski; Toynbee ×2, Farrère ×2, Pamuk, Aziz Nesin; Hoxha ×4, Beneš, Brezhnev; Liman von Sanders, Kannengiesser, Prince Andrew, Liddell Hart, Wavell, Harington; Enver ×3, Vahdettin ×4, Ali Kemal, Necip Fazıl ×2, Mustafa Sabri ×3; Clare Sheridan ×2; Nazrul, al-Rusafi, Huda Sha'arawi, Garvey, Bagryana, C. J. Dennis; Zahir Shah's telegram.**

**Datum after round 14 + follow-ups (2026-11-03): 596 gazes, 487 voices, 72 countries; follow-ups: Emil Ludwig ×2 (1930 interview, 1942), Pope Benedict XVI 2006, Gunther restored to 1936; admiring 48%, hostile+conflicted 183, posthumous 87. Round 14: US presidents Johnson ×2, Nixon, Reagan ×2, G. H. W. Bush (UCSB); Mitterrand; Putin 2004 (paraphrase only); the last Shah ×2; Muhammad Asad ('that petty masquerader'); Mahathir ×2; Fazlur Rahman; John Gunther ('the roughneck of dictators'); Harold Nicolson; Coudenhove-Kalergi ×2. Dropped at check: Putin 2005, Dewey (never names Kemal; the inherited note is corrected), Rebecca West.**

**Datum after round 13 (2026-11-01): 575 gazes, 472 voices, 71 countries; admiring 48%, hostile+conflicted 178, posthumous 71. Round 13: Khomeini, Sayyid Qutb, Said Nursi, Erbakan, Churchill 1929, de Gaulle ×2 (1968 guest books), Thatcher ×3, Roncalli, Weizmann, Sadat, Bhutto. Unsourced and corrected in the vault: Gaddafi 'traitor', Nasser's Kemalist 'blueprint' (his book never names Atatürk).**

**Datum after round 12 (2026-11-01): 561 gazes, 463 voices, 71 countries; admiring 49%, hostile+conflicted 173, contemporary 333, posthumous 59. Round 12 (famous names in their own words): Mao 1940, Mussolini 1928, Ho Chi Minh 1924, Trotsky, Reza Shah, Iqbal 1930 and 1936, Hemingway 1922, Jinnah 1938, Truman, Eisenhower ×2, Kennedy 1963, Ben-Gurion, Mandela 1992. Debunked or unsourced: Einstein 'greatest leader', Mao–Snow 1936 line, Jinnah 'greatest Musalman', MacArthur (earliest Cumhuriyet 1951).**

**Datum after round 11 (2026-11-01): 545 gazes, 450 voices, 69 countries; admiring 49%, hostile+conflicted 170, contemporary 325 (60%), posthumous 52; 88% confirmed or paraphrase-ok. Round 11: 21 foreign statesmen addressing the TBMM 1956–2010 (Bourguiba, Clinton, Obama, Wulff, Musharraf, Nazarbayev, Aliyev, Prodi, Barroso…; originals stored where published) and heads-of-state letters 1926–1933 via Şimşir-citing articles (Amanullah, Alexander I, Gömbös, Zog). Nobel archive settled: one nomination (Venizelos 1934).**

**Datum after round 10 (2026-11-01): 520 gazes, 426 voices, 65 countries; admiring 48%, hostile+conflicted 169, contemporary 321 (62%), second-hand 38%, primary 317; 88% confirmed or paraphrase-ok on independent check. Round 10 targeted notable voices: Stalin, Zinoviev, Chicherin, Radek (P upgrade), Venizelos ×2, Celadet Bedirxan, Khatisian, Papen, Nadolny, Lebrun, Prince Paul, Federzoni, and the TBMM condolence volumes (heads-of-state cables, OCR'd).**

**Datum after round 9 (2026-10-31): 493 gazes, 402 voices, 64 countries; admiring 48%, hostile+conflicted 158, contemporary 304 (62%), second-hand 39%, primary 303; 88% confirmed or paraphrase-ok on independent check.**

**Datum after round 8 (2026-10-30): 488 gazes, 399 voices, 64 countries; admiring 47%, hostile+conflicted 158, contemporary 299 (61%), second-hand 38%, primary 304; 87% confirmed or paraphrase-ok on independent check.**

**Datum after round 7 (2026-10-29): 390 gazes, 340 voices, 64 countries; admiring 49%, hostile+conflicted 122, contemporary 206, second-hand 47%, primary 206.**

**Datum after round 6 (2026-10-29): 336 gazes, 306 voices, 63 countries — past the ~300 threshold set
for revisiting the viz.** Skews moved: admiring 68%→50%, hostile+conflicted 19→95, contemporary (pre-1938)
49→156 (now the largest era), second-hand 70%→51%, primary-tier 41→151. Every record has an independent
check line (`data/checks.jsonl`); 84% confirmed or paraphrase-ok, the rest corrected/hedged.

**Datum layer built (r4, 2026-10-28):** `data/gazes.jsonl`, schema in `data/README.md`, 209 records
from the 74 verified notes; `b12_datum.py` validates it and stamps note frontmatter. **Known skews
(measured):** 68% admiring · 70% second-hand (`mediated_by`), 44% via Toksoy alone · 67% funeral-era ·
`mirror` null for 77% — the ten-card taxonomy fits people, not obituary prose. Next rounds should
buy hostile/conflicted and contemporary (pre-1938) gazes, and primary text.

**Parked viz sketch** (no code until the census is fat): polar layout around the silhouette —
azimuth = mirror card, radius = era, point size = intensity, color = polarity. A gaze is a point;
hovering shows `what_they_saw`; the silhouette re-renders per selected mirror. Revisit when the
dataset exceeds ~300 verified gazes.

## Pipeline — same rigour, staged

```
LEAD (anything: memory, a footnote, a search hit — M allowed, always labeled)
  → CANDIDATE (staged in candidates/<region>.md with tier + next step; NOT in the vault)
  → VERIFIED (sources check out → vault node tagged `verified` + LEDGER row)
  → DATUM (schema fields complete → counts toward the viz)
```

Rules: nothing enters the vault from candidates without a ledger row. M-tier is a work queue, not
a citation. A dry region gets a "dug, found nothing yet" note — absence of evidence is recorded,
not assumed.

## Coverage matrix

● = in vault · ◐ = candidates staged · ○ = open · ⌀ = dug, nothing yet

| Region | Country / polity | Status | Notes |
|---|---|---|---|
| **Anatolia** | Turkey (domestic gaze) | ● ~48 | deepest; queue in `candidates/turkey-domestic.md`; **r9:** the İzmir plot response in the Assembly (1 & 3 Nov 1926) |
| **W. Europe** | United Kingdom | ● ~18 | richest foreign gaze |
| | France | ● 5 | Farrère/Loti, Bouillon, Saint-Exupéry, de Gaulle, Sarraut(funeral) |
| | Germany | ● ~10 | Nazi thread + exile thread |
| | Italy | ● 3 | Mussolini, Sforza, Aloisi |
| | Ireland | ● 2 | Yeats, Sinn Féin/IRA |
| | Austria | ● 1 | Holzmeister |
| | Switzerland | ● 1 | Malche (+ Civil Code source-country) |
| | Norway | ● 1 | Nansen |
| | Spain | ● 2 | **r3:** Two Spains Mourn (both zones' press, Tüylü Turan 2019) + Giner de los Ríos (Republic's funeral mission); Franco-side delegation ❓ |
| | Portugal | ⌀ | r3: dug, nothing; Hemeroteca Digital Lisboa → browser |
| | Netherlands · Belgium | ● 2 cards | Dutch card (Delpher OCR); **r4:** Brussels Stands (parliament standing memorial 16 Nov) |
| | Sweden · Denmark · Finland · Norway | ● 2 cards | **r4:** Helsinki and Stockholm (absorbed r3 thin card); Copenhagen and Oslo |
| **E. Europe / Balkans** | Greece | ● 5 | Venizelos, Metaxas, Trikoupis, Ritsos, Onassis |
| | Poland | ● 2 | Piłsudski + **r4:** Warsaw Compares Him to Washington |
| | Romania | ● 2 | Titulescu + **r3:** Romania Hangs the Black Flags |
| | Yugoslavia | ● 4 | Alexander, Tito + **r3:** Yugoslav Press card; funeral delegate was **Milutin** Nedić (corrected) |
| | Albania | ● 2 | Zog + **r3:** Albanian Press card |
| | Bulgaria | ● 1 | mourning card; r3: the "unnamed general" is "General Jekof" (*Kurun* 22 Nov) — probably Nikola Zhekov (inference) |
| | Hungary | ● 3 | parliament card + **r3:** Gyula Gömbös ("my head is Turkish") + Magyarság Reads the Victory |
| | Czechoslovakia · Baltics | ● 2 cards | **r4:** Prague Reads Its Own Mirror ("we are in a position similar to Turkey's"); Riga, Tallinn and Kaunas (strongman parallel) — Toksoy 2006 digests; originals → browser |
| **USSR / Caucasus / C. Asia** | Soviet Russia | ● ~12 | Lenin→Yutkevich thread + **r3:** Moscow Mourns card, Potemkin (funeral envoy) |
| | Azerbaijan | ● 3 | **r3:** Resulzade (expulsion date 1928–33 unsettled), Mikayıl Müşfik, Azerbaijani Poetry card |
| | Central Asia (Turkic) | ● 1 | **r3:** Mustafa Çokay; Galiev context-only; Kazakh/Uzbek press ⌀ |
| | Armenia · Georgia | ⌀ | r3: one pass each, only polemical hits — needs scholarly route |
| **Mid-East / N. Africa** | Egypt | ● 8 | + **r3:** Rashid Rida (hostile), Cairo Mourns card |
| | Iran | ● 2 | Reza Shah, Khomeini |
| | Iraq | ● 4 | Faisal, al-Kilani + **r4:** Hikmat Sulayman, Bakr Sidqi (Kemalist officers) |
| | Jordan · Hejaz | ● 2 | Abdullah, Hussein |
| | Palestine | ● 1 | al-Husseini |
| | Syria / Lebanon | ● 5 | + **r3:** Damascus and Beirut Weep card |
| | Saudi Arabia | ● 2 | **r3:** Ibn Saud + Prince Faisal in Ankara, June 1932 |
| | Libya · Tunisia | ● 2 | Senussi, Gaddafi; Bourguiba |
| | Morocco | ◐ | Abd el-Krim: 2nd pass, still no direct statement; Kuran TDV + Er 2017 next |
| | Algeria | ● 1 | **r3:** Ben Badis — 1924 condemnation → 1938 eulogy (conflicted); Messali ⌀ |
| | Yemen · Sudan | ● 1 / ⌀ | **r4:** Imam Yahya (instrumental, Polat 2017); Sudan ⌀ |
| **Sub-Saharan Africa** | Ethiopia | ◐ | Haile Selassie parallel — M-weak, speculative |
| | colonial press / South Africa | ● 1 | **r3:** South African Muslims and the Anatolian Cause; Ethiopia, Nigeria/Azikiwe ⌀ |
| | diaspora | ● 2 | Garvey, Du Bois |
| **S. Asia** | India | ● ~10 | + **r3:** Tagore, Khilafat Disillusion 1924, India Mourns card |
| | Pakistan | ● 2 | Jinnah, Musharraf |
| | Bangladesh | ● 1 | Nazrul |
| | Afghanistan | ● 3 | Amanullah, Soraya, Tarzi |
| | Sri Lanka · Burma | ⌀ | r4: two searches, nothing |
| **E. / SE. Asia** | Japan | ● 3 | + **r3:** Japanese Print Culture card (titles-only; NDL texts next) |
| | China | ● 2 | Chiang/KMT, Mao |
| | Thailand | ● 1 | Phibun |
| | Indonesia | ● 2 | Sukarno + **r4:** Dutch East Indies Press (Muhammadiyah silence, Surabaya 15 Nov; Delpher primary) |
| | Vietnam | ● 1 | Ho Chi Minh |
| | Korea | ● 1 | **colonial-press collective card built** (Dong-A Ilbo; SNU scholarship) |
| | Philippines · Malaya | ● 1 | **r3:** Malay Press and the Fall of the Caliphate; Philippines ⌀; NewspaperSG → browser |
| **Americas** | United States | ● ~15 | |
| | Mexico | ● 3 | Calles + **r4:** Mexico Sends Its Greetings (1927–35, Republic Archives), Salvador Pardo Bolland |
| | Colombia | ● 1 | **r4:** Iván Duque (2022 Istanbul lecture, posthumous); contemporary ⌀; relations only from 1959 |
| | Cuba | ● 1 | Castro |
| | Jamaica | ● 1 | Garvey |
| | Argentina | ● 1 | **r3:** Buenos Aires Bust Affair (2010); 1938 press still ○ |
| | Peru | ● 1 | **r3:** José Carlos Mariátegui, "La revolución turca y el Islam" (1925) |
| | Brazil · Chile · rest | ⌀ | r3+r4: no scholarship on LatAm 1938 press; Hemeroteca BR / HNDM / Memoria Chilena are JS-rendered → browser-agent targets |
| | Canada | ● 1 | **r3:** Canada Says Not Yet at Chanak (1922) |
| **Oceania** | Australia | ● | ANZAC case study + **r3:** C.E.W. Bean |
| | New Zealand | ● 1 | **r3:** New Zealand Press card ("roughneck dictator", Waikato Times) |
| **Institutions** | League of Nations · UNESCO · Nobel · Vatican · Olympic | ● partial | LoN funeral delegation; Roncalli; Sherrill/Çambel |
| **Funeral** | delegations + telegrams | ● card + 5 | **r3:** Foreign Delegations card (Havas/Reuter via Delpher); Sarraut, Neurath, Potemkin, Giner de los Ríos, Fiessinger. "28 countries" unsourced; ~17 in Havas |
| | condolence telegrams | ● card | **r4:** Condolence Telegrams to Ankara (TBMM volumes, 99 pages OCR'd); Choudhry Rahmat Ali |

## Source seams, ranked by yield

1. **The Turkish per-country genre** — Turkish academia mass-produces "Atatürk'ün ölümünün X
   basınındaki yankıları" articles (German press ✓ exists, Azerbaijani poetry ✓ exists, local
   Turkish press ✓ exists). **DergiPark, open access, one query per country.** The single best
   seam; it already answered the siren question.
2. **The Şimşir compilations** — Bilâl N. Şimşir (diplomat-historian) published document volumes
   incl. *Atatürk'ün Hastalığı* with "Death: Echoes in France / England" sections; his
   [publication list](https://www.mfa.gov.tr/data/Kutuphane/yayinlar/mensuplar/bilal_simsir.doc)
   is itself a seam map. Acquire alongside Phase 0 books.
3. **The obituary corpus** (RESEARCH §5) — archive-by-archive. **Access reality after testing
   (Aug 2026):** Delpher/KB **WORKS and is scriptable** — recipe:
   `jsru.kb.nl/sru/sru?version=1.2&operation=searchRetrieve&x-collection=DDD_artikel&query=Ataturk and date within "10-11-1938 25-11-1938"`
   (812 records in the funeral window). Gallica SRU is bot-gated (403 → browser queue). Papers
   Past / ANNO untested; Trove needs free key; Chronicling America browser-only; BNA paid;
   TimesMachine sub; Latin American archives browser.
3b. **DergiPark full-text mining works end-to-end** — WebFetch saves the PDF binary locally,
   `pypdf` extracts the text (proven on Toksoy 2010, 36pp → `sources/`). Every per-country
   article in seam 1 can be mined this way, from here, without a browser.
3c. **Papers Past (NZ) works via fetch** on `paperspast.natlib.govt.nz/newspapers/<ID>` (full text);
   its search pages return headlines without links, so article IDs come from web-search snippets.
3e. **TBMM open-access repository (DSpace REST)** works: bitstreams downloadable; text layer junk →
   OCR locally (macOS Vision). Salt Research's "Atatürk in the Press" archive is likely the same platform.
3f. **Browser-grade crawling via Monid (r4)** — `ms render` (context.dev JS render, $0.002),
   `ms shot` (rendered screenshot, $0.002), `ms browse` (tinyfish AI browser agent, $0.016/step,
   async + polled; cap steps). Targets: Hansard, NewspaperSG, Hemeroteca BR, HNDM, Kramerius, Gallica.
3d. **Monid search (r3, Oct 2026)** — Keenable ($0.004, long snippets) and Exa ($0.011) through
   InFlow, plus free tinyfish full-text fetch. Six-region sweep: 93 paid calls, **$0.38 total**.
   Serialise calls (one InFlow call per Mac); stop on any InFlow error.
3g. **archive.org full-text search (found 3 Nov 2026) — searches INSIDE lending-only books, free, no login.**
   `https://archive.org/services/search/beta/page_production/?service_backend=fts&hits_per_page=30&user_query=<q>`;
   `<q>` takes phrases, AND/OR and `identifier:<id>` / `creator:(<name>)` filters, and each hit returns highlighted
   snippets (about 20 words). Proved on Gunther 1936, Ludwig 1930 (1991 reprint), Haile Selassie, Tunku. This reopens
   every "copyrighted / lending-only" dry end at snippet level (Mann, Zweig, Orwell, Koestler, Malraux, Kazantzakis, Ayub…).
   Slow (30–90 s per query); run single queries, not long loops.
4. **The interwiki sweep** — read the *Atatürk* article in every major Wikipedia language
   (Arabic, Greek, Persian, Urdu, Hindi, Japanese, Chinese, Spanish, Russian…). Each language
   community wrote its own emphasis: simultaneously a lead-mine and itself reception data.
5. **Funeral delegation list** — 28 countries; each named delegate is a thread to pull
   (who was Nedić to Yugoslavia, Potemkin to the USSR…).
6. **Nobel nomination archive** — full sweep for every nomination *of* Atatürk, any year (browser).
7. **Anıtkabir Özel Defter** — the state guestbook every visiting leader signs since 1953;
   published compilations reportedly exist (M-lead — verify). If real: the systematic corpus of
   *post-1953 world-leader* gazes.
8. **Turkish MFA embassy info-notes** — embassies publish local Atatürk connections (the Canberra
   note proved it); enumerate mission sites.
9. **Clayer/Giomi/Szurek chapters** — scholarly per-country skeleton (Bulgaria, Cyprus, Albania,
   Yugoslavia, Egypt confirmed in the volume).
10. **Compilation pages** (ataturktoday.com tributes, Pera Palace press page) — T-tier lead-mines;
    never cite directly, always trace upstream.

## Open leads that need a person (updated 9 Nov 2026)

Every free route has been tried for each item below. What is left needs a library, a purchase, a login or a person at a browser. If you can reach one of them, send what you find with the [Suggest a voice](https://github.com/okanerturan/how-the-world-saw-ataturk/issues/new?template=suggest-voice.yml) form; a photograph of the page is enough to work from.

**Library or purchase**
3. Şimşir, *Atatürk ve Yabancı Devlet Başkanları* I–IV (TTK): the incoming letters from heads of state (e.g. Hitler, 23 Nov 1934, vol. I pp. 153–154; Alexander I, vol. IV pp. 261–278).
4. *Anıtkabir Özel Defteri* (ed. Recep Cengiz, Anıtkabir Derneği, 2001; about 20 vols): the master source for 1960–2001 foreign leaders' entries. Saddam Hussein's 1977 entry is known only from a 2004 newspaper extract; the press of the 1990s–2000s rarely prints the text.
5. Landau (ed.), *Atatürk and the Modernization of Turkey* (Westview/Brill, 1984): the 1981 İş Bankası symposium papers, notably **Ali Mazrui**'s 'Africa between the Meiji Restoration and the Legacy of Atatürk' (pp. ~403–410), plus von Beyme, Hale, Stirling, Dodd.
6. Xenophon Stratigos, *Η Ελλάς εν Μικρά Ασία* (1925): on Scribd (account) or as a paid Ko-fi PDF.
7. Frunze, «Поездка в Ангору» (1929 diary), for completeness.

**Borrow on archive.org, one page each**
8. Hitler, *Table Talk* (2 Apr 1942) · Goebbels' diary (Nov 1938) · Pamuk's "André Gide" essay · Brzezinski, *Strategic Vision* · Brezhnev's Minsk speech 1978 (p. 223) · Herriot, *Jadis* · Morand, *Voyages* · Montgomery and Fuller · Ben-Gurion, *My Talks with Arab Leaders* · Salvemini, Musil · Hemingway, *Dateline: Toronto* · Benoist-Méchin, *À destins rompus* (1974) and *Mustapha Kémal ou la mort d'un empire* (1954), to get page numbers for the staged snippets.

**Sites behind bot checks (they need a real browser)**
9. vie-publique.fr and elysee.fr: search "Atatürk" in French presidents' and ministers' speeches (Giscard, Mitterrand, Chirac, Sarkozy, Hollande, Macron).
10. quirinale.it: Napolitano in Ankara, Nov 2009; presidency.ro (Băsescu, Iohannis); casareal.es (Juan Carlos, Felipe VI); gg.govt.nz.
11. UNESDOC: M'Bow's 1981 Atatürk-centenary speech.
12. doria.fi worked through Wayback for Kekkonen; the live site's search could list other Finnish presidential speeches on Turkey.
13. British Newspaper Archive (paid): G. Ward Price's Daily Mail interviews with Kemal.

**Originals and readers**
14. Khomeini, *Sahifeh* vol. 3, Persian · Roncalli's Italian diary · Ben Badis, *al-Shihab* / *al-Najah* · the page in Sadat's book · Bhutto's 1965 speech · the Hebrew (Katsav) and Czech (Špidla) originals of the Anıtkabir entries · Borba / *Govori i članci* IX for Tito's 1954 toast · the English originals of the 1953 and 1963 anniversary messages (MacArthur, Erhard, Douglas-Home, Ayub Khan, Nehru…) and of Luns's 1986 Peace Prize speech.

## Human / browser queue

Re-ranked 2026-11-01 by **who the voices are**, not by archive coverage. The finished product needs
recognisable names, so press sweeps are demoted (see the "notable voices" rule in `tools/AGENT_BRIEF.md`).

**Tier 1 — heads of state, famous writers and leaders, in their own words**
- [ ] **Şimşir, *Atatürk ve Yabancı Devlet Başkanları* I–II** (TTK). The letters between Atatürk and foreign heads of
      state, the single richest notable-voice corpus. Find a library copy or a TTK PDF, then photograph or scan the
      letters with substantive content (not pure protocol).
- [x] **Nobel nomination archive**: done 2026-11-01 without a browser (`show.php?id=7872`, `show_people.php?id=4779`; the
      record pages are server-rendered). There is exactly ONE nomination of Kemal: Peace 1934, nominator E. K. Venizelos ("Member
      of the Greek parliament"), Peace 1934 no. 24-1. The archive comment says he "was on the short list, but no evaluation was
      written". This confirms `venizelos-1934-01-12` at P level for the fact of the nomination.
- [ ] **Anıtkabir Özel Defter** (partly via press, 3 Nov: Benedict XVI 2006 staged; Francis 2014 and Leo XIV 2025 entries do not name Atatürk): check whether the published volumes exist. If they do, they hold the post-1953
      world-leader entries (de Gaulle, Kennedy-era visitors, etc.).
- [ ] **Ulus, 16 Nov 1938, "Yabancı devletleri temsil edecek heyetler"** and **Boran 2011** (*Atatürk Yolu* 47): the
      full funeral delegation list. Every named delegate is a notable-person thread.
- [ ] **hansard.parliament.uk**: an exact-phrase search for the Lloyd George "genius of centuries" quote. A famous name
      with a contested quote, so settle it either way.
- [ ] **NDL digital collection** (login): Japanese Kemal-titled texts. Prioritise named authors (Tokutomi Sohō, Ōkawa
      Shūmei, Uchida Ryōhei).
- [x] **Lending-only memoirs** — done 3 Nov via archive.org full-text search: Malcolm X (no Atatürk; open copy grepped), Haile Selassie (Kemal only as addressee of a protocol letter, p. 173), Tunku *Viewpoints* (no hit). All dry. Was:: Haile Selassie, *My Life and Ethiopia's Progress*;
      Tunku Abdul Rahman, *Viewpoints*; *The Autobiography of Malcolm X*. Look up "Ataturk"/"Kemal" and note the page.
- [x] **Emil Ludwig's 1930 interview** — done 3 Nov: it is NFP **9** Mar 1930, reprinted in *Für die Weimarer Republik und Europa* (1991) pp. 181–187; staged from search snippets (`emil-ludwig-1930-03-09`), plus *The Mediterranean* (1942) p. 548 (`emil-ludwig-1942`). The full NFP page is still worth a human read: (ANNO, behind Cloudflare):
      `anno.onb.ac.at/cgi-content/anno?aid=nfp&datum=19300311&seite=1`. A famous interviewer of dictators.
- [ ] **Putin's Anıtkabir honour-book wording**, 6 Dec 2004 (a Turkish press photo); the Kremlin only paraphrases it. Two searches on 3 Nov found nothing; needs a Milliyet/Hürriyet 7 Dec 2004 print archive.
- [x] **Gunther, *Inside Europe*, 1936 first edition** — yes: the line is in the Harper 1936 printing and four other 1936 copies (archive.org full-text search); `gunther-1936` dated 1936.
- [ ] *al-Shihab*, Nov 1938, and *al-Najah* nos. 152–153 facsimiles (Ben Badis, a major figure; a page-image check).

**Tier 2 — useful only for a named notable inside them**
- [ ] Latin American press (La Prensa, La Nación, O Estado de S. Paulo), Nov 1938. Look only for statements by
      presidents or major writers (Vargas, Ortiz, Cárdenas, Gabriela Mistral, Neruda).
- [ ] BNE Hemeroteca: did Franco's Burgos government send anyone, and did Franco say anything?
- [ ] Toksoy 2006 (*Atatürk Yolu* 37–38) and Lyulchak 2024: mine for named heads of government.

**Demoted — press sweeps with no notable voice** (do only if the press layer is ever needed)
- Chronicling America regional sweep · Gallica SRU sweep · NewspaperSG · Trove key · Kramerius, Hemeroteca Lisboa,
  digi.kansalliskirjasto, digar.ee · UNESDOC p. 69 · the SNU repository item · Hemeroteca BR.

**Automated, no longer needs a human**
- [x] **TBMM condolence volumes**, *Atatürk'ün ölümü dolayısıyla yabancı ülkelerden Büyük Millet Meclisi'ne gelen
      taziyetnameler* I–II (handle 11543/2467). Downloaded via the DSpace 7 API (`/server/api/discover/search/objects`,
      then item → bundles → bitstreams) and OCR'd with `tools/ocr.swift` (macOS Vision) → `sources/tbmm-taziyetname-1938/`.
      Senders include Kārlis Ulmanis and the presidents of the Italian Senate and Chamber.

## Cadence — what a digging session looks like

1. Pick one ○/◐ region from the matrix.
2. Run seams 1, 4, and targeted searches; stage everything found in `candidates/<region>.md`
   with tier labels (M welcome, labeled).
3. Batch-verify the strongest 3–5 candidates (web-corroboration standard, RESEARCH.md §4).
4. Promote survivors: vault node (`verified` tag) + LEDGER rows + matrix update here.
5. Anything requiring books/browser/keys → Human queue above.
6. Recoup: if the session exposed a missing tool or method, amend this file before stopping.
