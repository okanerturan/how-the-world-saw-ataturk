# Candidates — contemporary (1919–1937) continental press with stated views

Round 6 (Oct 2026, `b14_continental_press.py`). Free routes only: KB/Delpher SRU + resolver OCR, Gallica `Issues` + `ContentSearch` via the `fetch` wrapper, ANNO not used (page text blocked; nothing needed from the listing).

**PROMOTED (4 cards, 25 gaze records; 24 press records + 1 upgrade on [[Carlo Sforza]]; all era = contemporary):**
Dutch Confessional Press and the Fall of the Caliphate, March 1924 (7: Het Centrum x2, Limburgsch Dagblad x2, De Banier, De Nederlander, Bataviaasch Nieuwsblad) · Dutch Dailies on the Dictator, 1924–1937 (10 + Sforza) · Dutch Dailies at Smyrna, September 1922 (2) · Paris Press on the Caliphate, the Civil Code and the Decade, 1924–1933 (5: La Croix x2, Le Temps 1926, L'Action française 1933, Le Populaire 1933).
Polarity of the 25: hostile 10 · conflicted 8 · admiring 4 · witness 3.

## Seams (what worked)

| Archive | Method | Works? | Notes |
|---|---|---|---|
| Delpher SRU | `jsru.kb.nl/sru/sru?...x-collection=DDD_artikel&query=Kemal and (...) and date within "dd-mm-yyyy dd-mm-yyyy"&maximumRecords=50&startRecord=N` direct with urllib | yes, no key | The record has **no newspaper title**. Get it by fetching `https://resolver.kb.nl/resolve?urn=<id>` (HTML; `<title>` = "Paper » date - Art. n") and the OCR from `...urn=<id>:ocr` (XML, `<title>` + `<p>`). Both free, no throttle seen at 4 threads. Strip a trailing `:ocr` from the SRU identifier before the HTML call |
| Gallica | `services/Issues` and `services/ContentSearch` **only through `ms fetch`** | yes | Direct curl hits Cloudflare. Fetch takes 1–2 min per batch of 4–5 urls, so run in the background. Returns ≤3 snippets per page; many dispatches are wire copy |
| Gallica La Croix | title ark `cb343631418` | yes | `Issues` returned 306–309 issues a year (1921–28, 1933); 1934 Issues call did not return |
| ANNO | not used | — | |

Confessional papers *are* in DDD_artikel: De Tijd (subtitle "godsdienstig-staatkundig dagblad"), Het Centrum, De Banier (staatkundig gereformeerd), De Nederlander, De Standaard, De Volkskrant (Catholic), Limburgsch Dagblad, De Maasbode (appears for Sept 1922, none seen for 1924). Their editorials are rare; most items are Reuter/Havas copy that every paper printed.

## Leads

| Lead | Tier | Next step |
|---|---|---|
| De Standaard (ARP) editorial on the caliphate or on the Turkish prayers decree (29 Dec 1932 is wire) | P | Query `Standaard`-filtered pages with `kalifaat` Mar 1924 in the Delpher UI (title facet); SRU has no title index |
| De Maasbode / De Tijd leaders on Smyrna (Sept 1922) and on the caliphate | P | Delpher UI newspaper facet "De Maasbode", 1922-09-13..25 and 1924-03-04..08 |
| Het Centrum 6 Mar 1924 "Kijkjes op de Wereld": the Catholic-schools passage is OCR-garbled | P | Page image via Delpher viewer (`delpher.nl/nl/kranten/view?...`) |
| De Grondwet (MMGARO01): which paper? | — | Identify publisher/confession; two records currently carry "confessional character not checked" |
| La Croix 8 Mar 1924 p.1 "Gazette": the "milliard des Congrégations" paragraph is cut at "(...)" | P | Gallica viewer page 1, 8 Mar 1924 (bot-gated; browser run) to read the whole paragraph; would upgrade the record from inferred-hostile |
| La Croix 6 Mar 1924 p.5 relays *L'Écho de Paris* ("la vénération allait ... au sabre, et le sabre est aux mains de Kemal") | P (fragment, OCR garbled) | L'Écho de Paris, 5–6 Mar 1924 itself (find its Gallica title ark; not looked up) |
| Le Temps leaders (Oct 1921 Franklin-Bouillon; 5 Mar 1924; 1926 Civil Code) | P | Fragment searches with other query words (`Kémal`, `Angora`, `Ghazi`, `dictateur`) |
| Alphabet reform Nov 1928, women's vote Dec 1934 in French/Dutch press | P | ⌀ French fragments for 2–3 Nov 1928 and 6–7 Dec 1934 found nothing Kemal-related; try dates 5–10 days later and Dutch SRU `letters and Turksche and Latijnsche` 1928-11 |
| L'Humanité on the caliphate (5 Mar 1924 p.3 "Plus de Calife...") | P | Fragment has no explicit view; read page 3 in a browser (Communist reading is likely admiring/conflicted) |
| Voorwaarts / Het Volk (SDAP) on the caliphate and on 1930 repression | P | One Voorwaarts record done (23 Aug 1930); Het Volk wire only so far |
| Algemeen Handelsblad 29 Oct 1924 is by "een bijzonderen correspondent" | P | Identify the correspondent |
| Haagsche Courant 15 Sep 1937 "Het nieuwe Turkije" series | P | Check whether syndicated from a German/English source (series 11 and 15 Sep 1937) |

⌀ dug, nothing yet: Franklin-Bouillon/Ankara Agreement Oct 1921 (Temps, Humanité fragments are news only; AF, Figaro, Populaire, Croix returned no hit on 22–25 Oct); Lausanne July 1923 (news and the Mestre quote only); alphabet 1928 and women's vote 1934 in Paris.


**Held back after source check (2026-10-29):** La Croix 9 Mar 1924 — quoted fragments not found in cited ark `bpt6k261791r`; record withdrawn from the dataset and note. Next: locate the correct 9 Mar 1924 issue ark and re-run ContentSearch.

## Round 8 (Oct 2026, `b16_gallica2.py`, slug gallica2) — French press 1920–1924, Gallica fragments

**PROMOTED (4 cards, 12 gaze records, all contemporary; records in `scratchpad/gazes8_gallica2.jsonl`):** Paris Press and the Cilicia War, February 1920 (1: Le Matin, hostile) · Paris Dailies on Kemal's Victory, 11–17 September 1922 (5: Le Temps x2, L'Humanité, Le Populaire, L'Action française) · Paris Press and the Franklin-Bouillon Accord, October 1921 (0 records; dry-end card) · Paris Dailies and the Abolition of the Caliphate, March 1924 (6: La Croix 7 Mar, Le Temps, Journal des débats, Le Petit Journal, L'Humanité, Le Populaire). Polarity: witness 5 · hostile 2 · admiring 2 · instrumental 2 · conflicted 1. Journal des débats and Le Petit Journal are new voices for France.

**La Croix 9 Mar 1924 resolved:** the "Et, puisque Mustapha Kemal prétend inaugurer" fragment is in the **7 March 1924** issue, `bpt6k261789f`, view 1 (found by ContentSearch "inaugurer" across 5–9 March; it is in no 9 March view). The 9 Mar ark `bpt6k261791r` only has "a inauguré le musée Henner". The same view shows the surrounding text ("cette intolérance jeune-turque ... s'efforce de détruire [les écoles] que la France a multipliées", "des journaux comme le Temps, toujours prêts à saluer la « laïcité »"). Record `la-croix-1924-03-07` is the replacement.

### Seams (what worked, what failed)
| Archive | Method | Works? | Notes |
|---|---|---|---|
| Gallica `Issues` | `$S fetch .../services/Issues?ark=ark:/12148/<title>/date&date=<yr>` | yes | New title ids confirmed: Le Matin `cb328123058` (1920, 1925, 1936 ok), Journal des débats `cb39294634r`, Le Petit Journal `cb32895690j`. `cb34429768g` (Écho de Paris guess) and `cb34425632p` (L'Œuvre guess) return HTTP 400: ids still unknown. Several single calls failed first time (Figaro 1920/1925, Croix 1925) and succeeded on retry |
| Gallica `ContentSearch` | `$S fetch` batches of 5 | yes, **but results do not come back in request order** | Match results to requests by `url`, never by position (an earlier sweep script mislabelled titles that way). The search is fuzzy: "Marache" stems to "marche" (market reports); "Franklin" matches racehorses; accents are folded. After a few hundred URL fetches the fetch route went to HTTP 429 with 10–13 minute lockouts (shared quota); retries inside the lockout just burn time |
| Gallica SRU, `texteBrut`, page text | `$S fetch` | no | SRU returned nothing; `f1.texteBrut` is `bot_blocked` |

### Leads
| Lead | Tier | Next step |
|---|---|---|
| Le Matin 1921–24 and Écho de Paris, L'Œuvre (no Issues for these years/titles in hand) | P | Find the title arks (Gallica title page) and rerun the Oct 1921 / Mar 1924 / Sept 1922 sweeps; Matin and Écho are the dailies most likely to carry a strong anti- or pro-Kemal leader |
| Le Matin 13 Feb 1920 p.3 "il dicte ses volontés" — who is "il"? | P | Page image in a browser |
| Journal des débats, 5 Mar 1924 p.1: who signs the long account of the Caliph's fall? | P | Page image |
| Sheikh Said (Feb–Jun 1925), Izmir plot trials (Jul–Aug 1926), alphabet (Nov 1928), Hatay (Dec 1936–Jul 1937) | P | See dry ends below; retry with different cue words (`dictateur`, `Kurdistan`, `Gazi`, `Atatürk`) after the quota recovers; 1937 Issues for Figaro/Matin not loaded |
| Cilicia soldiers' war: Marash, Aintab, Urfa (Feb–Apr 1920) | P | Cue words that survive the stemmer: `Aïntab`, `Maraš`, `Mouslimié`, `kémalistes`, `nationalistes turcs`; also Humanité Mar–Apr 1920 |

⌀ dug, nothing usable: **Franklin-Bouillon accord Oct 1921** (Angora/kémalistes/Franklin on 21–29 Oct: Temps, Figaro, Humanité, AF, Croix, Populaire — all dispatch or Chamber reporting; Le Populaire 26 Oct only hopes the accord outlives the Bekir Sami one); **Sheikh Said** (4–6 Mar 1925, Temps/Figaro/Huma/AF/Croix/Matin/Débats: one AF line about Fethi at the station, nothing else); **Izmir plot** (AF 27 Aug 1926 has only a one-line wire "complot contre Kemal", the rest of that sweep was rate-limited); **alphabet** (3, 4, 10 Nov 1928 sweep launched but rate-limited out, no result); **Hatay/Sanjak** (Temps, Humanité, AF, Croix, Populaire on 12–15 Dec 1936 and 28–29 Jan 1937, Alexandrette/Turquie queries: League Council reporting; no fragment names Atatürk; Croix 29 Jan 1937 view 2 has "Le règlement de la question d'Alexandrette", no Kemal; 1934 surname law: only Temps 26 Nov 1934 wire). **Atatürk by name** in French press 1936–37 remains unfound by this method: the dispatches say "la Turquie", "Ankara".


## Round 10 (Nov 2026, `b18_anno.py`, slug anno) — German and Austrian press and officials

**PROMOTED (2 cards, 6 records, all contemporary; `tools/.state/round10/gazes_anno.jsonl`):** German Statesmen Address Kemal, 1924 and 1933 (Nadolny, Papen) · Vorwärts and the Arbeiter-Zeitung on the Dictator, 1924–1930 (Vorwärts x2, Arbeiter-Zeitung x2; Austria's first records). Polarity: instrumental 1 · admiring 2 · hostile 1 · conflicted 2. New person notes: Franz von Papen, Rudolf Nadolny.

### Seams
| Archive | Method | Works? | Notes |
|---|---|---|---|
| ANNO search | `https://anno.onb.ac.at/anno-suche/rest/search/{simple,complex,snippet}` (no key). `complex?text=&title=&dateFrom=YYYY-MM-DD&dateTo=&sort=DATE|RELEVANCE&from=1&facets=true`; `snippet?documentId=ANNO_aze19300821&query=` returns 3–5 OCR lines per page with page numbers | yes | Words are ANDed across the whole issue, no proximity, so names near "Kemal" need the snippet step. `title=` takes the paper name (e.g. "Arbeiter Zeitung", "Reichspost"). **Page text/images are blocked**: `anno.onb.ac.at/cgi-content/anno...` gives a Turnstile page (also through `ms fetch` and `ms render`), `digital.onb.ac.at` resets TLS. So every ANNO quote is search-index OCR with no second pass |
| Deutsche Digitale Bibliothek newspapers | `https://api.deutsche-digitale-bibliothek.de/search/index/newspaper-issues/select?q=plainpagefulltext:"A B"~25&fq=paper_title:"Vorwärts"&fq=publication_date:[1924-01-01T00:00:00Z TO 1924-12-31T23:59:59Z]&fl=id,paper_title,publication_date,pagenumber,plainpagefulltext&wt=json` | yes, no key | Open Solr with **full page OCR text** and proximity (`~N`). The id before the first `-` is the item id: `deutsche-digitale-bibliothek.de/newspaper/item/<ID>?issuepage=<n>`. `paper_title` is tokenised (use phrase `"Vorwärts"`). Holds Vorwärts, Berliner Tageblatt, Kölnische Zeitung, Münchner Neueste Nachrichten, Volksstimme, Süddeutsche; NOT Vossische, Frankfurter Zeitung, Germania, Rote Fahne. The `deutsche-digitale-bibliothek.de/search/newspaper` web page is behind an anti-bot wall |
| Compact Memory | not tried | — | |

### Leads
| Lead | Tier | Next step |
|---|---|---|
| Vorwärts 10 Sep 1930 p3 (Izmir municipal elections, "Was wird Kemal Pascha tun?") and 4 Jan 1929 p3 ("Türkischer Beschneidungskrieg. Kemal als Schiedsrichter") | P | Read in DDB item pages; third and fourth SPD-centre records |
| Die Stunde (Vienna) 19 Aug 1930 p3 "Ein Diktator, den die Diktatur langweilt" | P (ANNO fragment) | Tabloid; low priority |
| Volksblatt (Halle, SPD) 1 Nov 1929 p13: "der Dank — der Kemal und Mussolini, der Hugenberg und Hitler nach der großen Befreiungsschlacht" | P | Regional SPD; maybe a hostile record |
| Hindenburg's Handschreiben to Kemal carried by Nadolny, Sept 1925 (Bergedorfer Zeitung 17 Sep 1925: news only) | P | Find the text of the letter |
| Emil Ludwig interview, Dec 1926 serial of Kemal's war memoirs (Berliner Tageblatt 17 Apr 1926 etc.) | P | These are Kemal's own words; self-type or Ludwig lead |
| Karl Radek on the Smyrna victory (Rote Fahne leader, 23 Sep 1922; Börsen-Zeitung 24 Sep 1922 p3 is column-garbled, Freiheit 17 Dec 1920 p2 attacks Enver and Kemal) | P | Find an intact reprint |

⌀ dug, nothing yet: Stresemann, Seeckt, Spengler, Rathenau, Brüning, Hugenberg, Ludendorff, Mackensen near "Kemal" in DDB (only incidental co-occurrence); Dollfuss, Schuschnigg, Miklas, Hainisch, Seipel, Schober in ANNO (hit counts are AND-matches, no statement found); Thomas Mann, Karl Kraus, Zweig, Tucholsky, Freud, Werfel: no statement on Kemal located in the press seams (their own books/letters not tried). Goebbels' article of 11 Nov 1938 is on the Paris murder, not Atatürk. Smyrna 1922 and Lausanne 1923 leaders in Arbeiter-Zeitung (13, 18, 20 Sep 1922) are mostly Reuters wire.


## Round 21 (Nov 2026, `b30_wikisource.py`, slug wikisource) — Wikisource sweep, 34 languages

**PROMOTED (1 card, 12 records; `tools/.state/round21/gazes_wikisource.jsonl`, all evidence S, no scan viewed):** Wikisource Pens on Mustafa Kemal — Lototsky, Iorga, Nzhdeh, Shant, Annadurai and Others. Polarity: admiring 6 (Lototsky, Iorga, Annadurai, McCabe, Du Bois [a novel's character], Petriv) · hostile 4 (Nzhdeh ×2, Shant, Hook) · conflicted 1 (Kotko) · instrumental 1 (Banerjea). Era: contemporary 8, posthumous 4. New countries: Ukraine (Lototsky, Kotko, Petriv), plus Iorga for Romania and a Tamil voice (Annadurai). New person notes: Oleksandr Lototsky, Nicolae Iorga, Garegin Nzhdeh, Levon Shant, C. N. Annadurai, Joseph McCabe, Sidney Hook, Surendranath Banerjea, Kost Kotko, Vsevolod Petriv. Du Bois already had a note (record added, note not rewritten). Dropped as duplicates or handled elsewhere: Bainville *Les Dictateurs* (already in the dataset via the English translation), René Pinon 1920 and Maurice Pernot (round 21 `frenglish`), Sukarno's Indonesian essays (already the *Sukarno Reads Kemal* card).

### Seams
| Archive | Method | Works? | Notes |
|---|---|---|---|
| Wikisource search API | `https://<lang>.wikisource.org/w/api.php?action=query&list=search&srsearch=<term>&srlimit=50&format=json` | yes, free | 2 s sleeps still draw 429s on bursts (de, el, sr, da, he, ur; retried at 7-12 s). Several langs (sq, lv, uz, kk, tt) have **no Wikisource of their own** (HTTP 302 to Wikimedia). Hebrew: prefix `כ` makes `כמאל` a 145k-hit noise query; use `אתאתורק`, which gives 0 |
| `index.php?action=raw&title=T` | raw wikitext | yes, but **chapters transcluded from `Page:` namespace come back as a 100-byte `<pages index=... />` stub** | Fall back to `action=render` (HTML, strip tags) to get the actual text; the page-number templates then show up as noise JSON, and each scan page number is in them (`Page:<book>.djvu/<n>`) |

### One line per language
- **en** (10-28 hits per term): promoted McCabe 1945, Hook 1943, Banerjea 1925, Du Bois 1928 (novel). Leads: Lowell Thomas, *With Lawrence in Arabia* ch. 29 (1924: Kemal 'undoubtedly hopes to seize the scepter' of the Caliphate; one clause, left out); 1922 Britannica 'Mustapha Kemal' entry (unsigned; 'dissolute life', 'reckless courage and ambition'; a possible institution record); *The Young Moslem Looks at Life* ch. 6 (author not checked); asides in *My American Lectures* (author not checked) and *Algeria from Within* ch. 12 are passing.
- **fr** (9-36 hits): Bainville *Les Dictateurs* (already in), Pinon and Pernot (frenglish agent), Loti's 1920 book ch. 20 (Kemal named only as a fact), Istrati (guide's hearsay), Trotsky *Ma vie* (already in). Nothing new left.
- **de** (1-14 hits): Lepsius *Todesgang* (hits are the family name Kendji-Zade-Kemal), Karl May (fictional Kemal Bey); leads for a human: *Der Sturm* contents list names Mieczysław Szczuka's **Fotomontage Kemal Pascha (1924)** on p. 193, an artwork; *Merkur* 401 (1981) pp. 1105-17 G. A. Sonnenhol, 'Atatürk heute' (German ex-ambassador in Ankara; contents list only).
- **el** (2 hits): dry. Pavlos Nirvanas 'hordes of Kemal' (passing) and Ventiris on an Ismail Kemal.
- **pl** (0-5 hits): not read; the titles (*Trzy serca*, *Wesele hrabiego Orgaza*, *Romans w puszczy*) are novels, probably a character name.
- **cs** (1-3): dry (Ottův slovník hits are Kemal Pasha-zade, the 16th-century historian).
- **hu** (0-5): dry (anonymous school texts, a humorous feuilleton that uses 'Kemál basa').
- **ro** (2-4): **promoted Nicolae Iorga**, university opening lecture 31 Oct 1938; Istrati's *Spovedania unui învins* is a guide's hearsay (dry).
- **bg** (1-2): dry (an agent file naming a person called Kemal).
- **sr** (6-10): dry. Ćorović's history (Zogu's republic 'on the pattern of Kemal Pasha's Turkey', passing); a folk song with a different Kemal-bey.
- **hr** (1): dry. **sl** (2-4): *Skozi okno vlaka* has an old Muslim calling Kemal 'Antichrist' in a dialogue (author not checked, a character's speech); *V Macedonijo* a passing aside; *Nova doba* contents list names **D. Vaka, 'Mustafa Kemal in Kemalisti'** (Demetra Vaka Brown?) but the article has no text page.
- **uk** (20-34): **promoted Lototsky (memoir pub. 1966), Kotko 1930, Petriv 1924**. Leads: Lev Velychko, 'Реакція та опозиція в Туреччині' (*Східний Світ* 1927, hostile to the opposition; translated from Russian, author a Soviet Orientalist); unsigned 'З подій і питань старого року' (*Літопис політики* 1923, Berlin: 'not Kemal or Ismet but Poincaré tore up Sèvres'); Chekanovsky in *Воля* 1920 (passing); Nazaruk's *Роксоляна* hits unread (probably names).
- **sv, da, no, nl, et, lt, ms** (0 hits each): dry; nl has one anonymous Haagsche Courant item of 4 Dec 1934 on the surname 'Atatürk' (wire-style, not a gaze).
- **fi** (0-3): dry for text; *Väinö J. Vatanen* author page lists a signed article, Hakkapeliitta 3 Jun 1930, 'Salonikilaisen pikkukauppiaan pojasta Turkin diktaattoriksi' (Kansalliskirjasto digi link, not on Wikisource; Vatanen is minor).
- **lv, sq, uz, kk, tt**: no Wikisource exists. **he** (0 for Atatürk): dry. **ka** (1): dry (a medieval poet).
- **hy** (9-51): **promoted Nzhdeh 1932 and 1937, Shant 1925**. Leads: Katchaznouni's *Ազգ և հայրենիք* (1923-24) lists Mustafa Kemal among nationally effective men of mixed descent, no verdict; Wikisource holds the Soviet Armenian Encyclopedia entry ՀՍՀ/ԱԹԱԹՅՈՒՐՔ and ՀՍՀ/ԹՈՒՐՔԻԱ (anonymous, posthumous).
- **az** (5-20): lead only: Rasulzade, *Stalinlə ixtilal xatirələri* ('Moskvada iki il'): reports Stalin saying Atatürk was a capable statesman and revolutionary who should have taken more power, and notes a 1921 article in Stalin's Commissariat organ *Zhizn natsionalnostei* predicting Ankara's fall; composition date is not on the page and Stalin and Rasulzade are both in the dataset, so left unstaged. Also: Ağaoğlu's *Sərbəst insanlar ölkəsində* (translator's note only; Atatürk not named); Atatürk's own *Nitq* (self type); Əli Volkan interview (modern).
- **id** (3-7): dry for new voices: Sukarno's essays are the existing card (Indonesianisme dan Pan-Asiatisme, Me-"muda"-kan Pengertian Islam, Apa Sebab Turki..., Tabir Adalah Lambang Perbudakan, Saya Kurang Dinamis?). Not yet checked against the card: *Tabir Adalah Lambang Perbudakan* ('Lihatlah Kemal Ataturk, lihatlah Nabi kita sendiri') and *Sarinah* (1947).
- **ta** (8-11): **promoted Annadurai 1960**. Leads: Periyar *Kudi Arasu* original not on Wikisource, only Karunanandam's biography paraphrase (modern, 'Kamal Pasha's reform civilised the Turks' as Periyar's argument); the 1930 Erode music-conference presidential address by K. Ponnaiah Pillai citing 'Kamal Pasha' on music (via the *Dravidan* paper; a passing mention); Karunanidhi, *Nenjukku Neethi* (passing, Kamal Pasha's death in 1938).
- **hi** (3-8): dry. Antarrashtriya Gyankosh (1943) entry 'कमाल अता तुर्क' is an anonymous-compiler encyclopedia entry; Premchand, *Rangbhoomi* ch. 10 (1925): a character, John Sevak, says Mustafa Kemal was a rebel the country thirsted to kill and is now the nation's life 'because he succeeded' (a character's speech; lead for a fiction record, Premchand not in the dataset).
- **ur** (1-11): dry (titles are classical and Delhi prose where kamal is a common word; not read in full).

## Round 22 — German parliaments (slug `reichstag`, script b31_reichstag.py)
- **Promoted (12 Bundestag records, evidence P, DIP + dserver PDF page):** Stercken 1992, Poppe 1992, Althammer 1983, Emmerlich 1983, Joschka Fischer 1999 and 2002, Schröder 2002, Weisskirchen 2004, Jung 2016, Müntefering 2016, Hampel (AfD) 2018, Gauland (AfD) 2025. Staging: tools/.state/round22/gazes_reichstag.jsonl.
- **Hitler 4 May 1941 German original found** (Reichstag 4. WP, Bd. 460 = bsb00000613, 6. Sitzung, printed p. 85 right column, image 86): 'Der große geniale Neuschöpfer der jungen Türkei gab als erster ein wunderbares Vorbild für die Erhebung der damals vom Glück verlassenen und vom Schicksal so entsetzlich geschlagenen Verbündeten.' Upgrade file tools/.state/round22/upgrade_hitler-1941-05-04.json (wording is Neuschöpfer der jungen Türkei, not Neugestalter der neuen Türkei).
- **Reichstag full-text (IIIF search across bsb00000010-143 and 613, terms Kemal, Atatürk, Angora, Ankara, Gasi, Ghasi):** dry for any speech about Kemal in the Weimar volumes. Only hits: Kemal Midhat Bey (1918, Armenian speech), a Reichstag condolence cable from the Turkish Grand National Assembly on Ebert's death (Angora, 1925), embassy-building and treaty annexes. The Reichstag did not sit between 30 Sep 1938 and 30 Jan 1939, so no Göring announcement of Atatürk's death exists in the protocols (not checked in the 30 Jan 1939 speech, whose OCR is poor). Volume 613 (1939-42) OCR is garbled Fraktur (T read as B), so a negative there is not proof.
- **Bundestag leads not promoted:** Gernot Erler 2004-10-28 (15/135: 'seit 81 Jahren gibt es die moderne, von Kemal Atatürk gegründete Türkei', congratulation on the Republic Day), Schwall-Düren same day, Christian Schmidt 1993-09-24 (12/177, 'seit Kemal Atatürk eindeutig nach Westen orientiert'), Frau Luuk (SPD) 1983-06-15, Volker Beck interjection 2002-12-19, Hampel 2020-09-30 (same quotation as 2018), Stercken 1988-11-30 (11/112), Brandt/Schmidt/Kohl/Genscher/Merkel/Wagenknecht/Özdemir did not turn up in a full scan of all 5,808 protocols for 'Atatürk|Kemal' (no hit attributed to them; Kemalism/Kemalist hits by others about the army, Kurds and the EU are many: 12/218 1994, 13/160 1997, 13/212 1998 etc. not read speaker by speaker).
- **Austrian Nationalrat:** not tried (no easy free full text found within budget).
