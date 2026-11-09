# US immigrant press, 1919–1938 (Chronicling America) — round 8, slug `ethnic_press`

Script `b16_ethnic_press.py`; gazes `scratchpad/gazes8_ethnic_press.jsonl` (23 records); ledger `scratchpad/ledger8_ethnic_press.md`.

## PROMOTED (2 event cards, 23 gazes, all contemporary 1922–1938, tier P)
Polarity: 9 admiring, 6 hostile, 4 conflicted, 4 instrumental. Communities: Spanish (Tampa, 7), Italian (5), Hungarian (2), Czech (2), Polish (4), Slovak (1), Slovenian (1), Yiddish (1).
- **Tampa's La Gaceta Calls Kemal a Dictator, 1930–1935** — "Changas y Chungas" front-page column: 27 Jun 1930, 4 Nov 1930, 2 Mar 1931, 28 May 1932, 1 Dec 1934, 24 Jan 1935, 1 Nov 1935. (The briefed 24 Apr 1934 item was read: factual "El Dictador turco no ha recibido con agrado las palabras de Mussolini", OCR-damaged around "fabricada por la espada de Mustafa Kemal"; not promoted, no clean quote.)
- **America's Immigrant Press Reads Kemal, 1922–1938** — Il Risorgimento Italiano nel Maryland (1922, 1929), La Verità Waterbury (1935 x2), La Sentinella Bridgeport (1934), Amerikai Magyar Hirlap (1922, 1938), Svět Cleveland (1922, 1923), Jedność Polek (1927, 1928 x2), Przewodnik Katolicki (1922), Youngstownské Slovenské Noviny (1930), Glas Svobode (1922), Der Morgen Zhurnal (1934, hostile).

## Seam table (round 8, this task)
| Archive | Method | Works? | Notes |
|---|---|---|---|
| Chronicling America via loc.gov | `$S fetch` of `…/collections/chronicling-america/?q=Kemal&dates=1919/1938-12-31&fa=language:<lang>&fo=json&c=100&sp=N&at=results,pagination` | **YES, flaky** | About 1 call in 3 returns `target_unreachable`: retry loop with 3 s pause. `fa=number_lccn:snXXXX` narrows to one paper (used for La Gaceta, 38 hits). Result `total` field is wrong (3); use `of`. Search is fuzzy: Arkansas Echo (Little Rock) is tagged german. |
| Hebrew-script query | same, `q=קעמאל` with `fa=language:yiddish` | **YES** | 479 hits (OCR variants); Yiddish Tageblatt's English wire pages also come up. |
| Page OCR | plain `curl` of `word_coordinates_url` + `&full_text=1` | YES | Cache by URL; ~1,150 pages read this round. |
| Language filters with zero hits | greek, armenian, arabic, hebrew, russian, ukrainian, croatian | no data | Greek-American, Armenian-American, Arabic-American papers not in loc.gov for this window (also Greek/Arabic/Armenian script queries return nothing). |

Language hit counts (pages containing "Kemal", 1919–38): german 262, polish 201, czech 136, lithuanian 91, slovenian 48, finnish 20, italian 17, hungarian 16, slovak 9, yiddish 5 (Latin-script query) / ~480 (Hebrew-script).

## New leads
| Lead | Community | Tier | Next step |
|---|---|---|---|
| Der Morgen Zhurnal 28 Jul 1935 p. 6 (22 Kemal hits): a long biographical/feature article on Kemal ("retter fun dem Turkishen folk"…); author unknown | Yiddish | P | Read page image; if it is an opinion piece, an admiring Jewish voice to balance the 1934 hostile one |
| Yidishes Tageblatt 20 Aug 1925 pp. 3 and 6, 20 Oct 1927 p. 4: humorous columns on Kemal and Latife's divorce / "Kemal the boss of Turkey who cannot boss his wife" | Yiddish | P | Yiddish OCR too garbled to quote; needs page image |
| Der Morgen Zhurnal 25 Jul 1934 p. 4 (news on the Thrace pogroms), 13 Nov 1938 p. 8 (funeral) | Yiddish | P | Funeral-era Jewish obituary; read image |
| Yidishes Tageblatt 1921–26 English wire pages: Daily Mail "Kemal is a Sephardic Jew from Salonica" (24 Feb 1921 p. 10), Cilicia synagogue destruction (5 Mar 1922 p. 12), Turkish Jews' loyalty telegram (4 Mar 1926 p. 8) | Yiddish | P | JTA agency copy, no paper voice; useful context only |
| Dziennik Chicagoski (Polish Catholic daily), Sept–Oct 1922: dozens of pages incl. 16 Sep 1922 p. 3 Smyrna "rzeź" report; editorials not isolated | Polish | P | Scan pp. 2/4 editorials for Kemal; strongest hostile Polish Catholic candidate |
| Draugas / Lietuva (Lithuanian, Chicago) 1920–22: 91 pages, 1922-01-30 (11 hits), 1921-08-08 (9) — Lithuanian OCR not read for opinion | Lithuanian | P | Lithuanian-language read needed |
| Glas Svobode (Chicago, Slovenian) 3 Oct, 10 Nov, 14 Nov 1922 editorial page ("Naši uredniški članki") | Slovenian | P | Read the 14 Nov 1922 p. 2 article |
| Uusi Kotimaa / Auttaja (Finnish) 1922-09-28 (8 hits) | Finnish | P | Finnish-language read needed |
| Telegraf (Baltimore, Czech) 1921–25: Dec 1921 p. 8 Sultan/Kemal item, Mar 1925 p. 2 travel story of capture by Kemal's army | Czech | P | 6 Mar 1925 serial is first-person captive's tale, not an editorial: possible witness record |
| Washington Journal (German, DC) 18 Jan 1929 p. 5 "Türkische Kulturreform" feature ("dieser diktierte Umschwung") | German | P | Check if editorial or agency feature; 28 Aug 1925 p. 4 reports Senator King's view (American, not ethnic voice) |
| Der Nordstern (St Cloud, German) 11 Jan 1923 p. 5 (translated Constantinople letter; Armenian lynching incident), 21 Jun 1923 p. 15 Angora sketch | German | P | News, not editorial |
| Tabor Independent (Czech, S. Dakota), 1920–21 | Czech | P | Not read |
| Fascist vs anti-fascist Italian split: only Waterbury (pro-Italy) and Bridgeport hits so far; *L'Italia* (San Francisco), *Il Risorgimento*… | Italian | P | Run `fa=language:italian` with `Mussolini+Kemal` query to catch comparisons |
| Svět (Cleveland) 16 Sep 1922 p. 2: the translated Plain Dealer editorial is a Plain Dealer voice, mediated | Czech | P | Upgrade Plain Dealer row if the Cleveland Plain Dealer itself is on CA |

## ⌀ Dug, nothing yet
- **Greek-American press**: no Greek-language (or Greek-script) pages in Chronicling America for 1919–38; *Atlantis* not digitised there. Next: Greek-American papers on other archives (Hellenic Parliament library?; Library of Congress "Greek American" collection); needs a human.
- **Armenian-American press**: no Armenian-language hits; *Hairenik*, *Asbarez* not on loc.gov. Next: Hairenik archive (hairenik.com) and Armenian Weekly via the Internet Archive.
- **Arabic-American press (al-Hoda, Meraat-ul-Gharb)**: not on loc.gov; Syrian-Lebanese Americans unrepresented.
- **Forverts**: not on loc.gov (digitised at Yiddish Book Center / Historical Jewish Press); loc.gov carries the *Tageblatt* and *Morgen Zhurnal*, which are Orthodox/centrist.
- **German-American**: 262 hits but nearly all agency/wire news; no opinion voice isolated.
- La Gaceta 24 Apr 1934: read; no clean quote.

## Cost
0 paid search/exa/browse calls; ~35 free `$S fetch` calls (retry-heavy); ~1,150 free curl OCR fetches.
