# Candidates — Hansard sweep 1919–1938 and Anglosphere editorials (round 6)

Script `b14_hansard_anglo.py` (5 Events, 41 gaze records in `scratchpad/gazes6_hansard_anglo.jsonl`).
Method: Hansard Search API (Spoken + Written, 12 search terms, 1919-01-01 to 1938-11-09, 186 unique contributions;
every one containing *Kemal/Kamal/Ataturk/Kemalist* read in context) and Papers Past (rendered search pages → fetched
article pages). Already in the vault and not duplicated: [[Hansard After Atatürk, 1938–1939]] (Hudson, Strabolgi 1938),
[[New Zealand Leaders on Kemal at Chanak, September 1922]], [[New Zealand Press, November 1938]]; person notes for
Lloyd George, Curzon, Churchill, Townshend, Franklin Bouillon, Clair Price exist and were left untouched (see ledger "upgrade" rows).

| Lead | Country | Domain | Era | What's claimed | Tier | Next step |
|---|---|---|---|---|---|---|
| ~~Hansard, Feb–Mar 1920 (8 voices)~~ **PROMOTED** (Event) | UK | politics | contemporary | Kemal enters Westminster as the successor to Enver: Guinness "would become dictator"; Asquith "so long as Mustapha Kemal and his forces are at large…" | P | — |
| ~~Hansard 1921–22 (Bryce, Cecil, O'Connor ×2, Townshend, Lloyd George ×2, Kenworthy)~~ **PROMOTED** (Event) | UK | politics | contemporary | Hostile Armenian/Greek lobby vs Townshend's "I know him well and respect him"; Lloyd George "great general and a great patriot" 4 Aug 1922 | P | Fetch 22 Dec 1920 Commons debate (Vol 136 cols 1895-97) to replace the second-hand "mutinous general" record |
| ~~Hansard 1924–1938 (9 voices)~~ **PROMOTED** (Event) | UK | politics | contemporary | Kemal as exemplar: Newton "greater despot", Croft/Lansbury/Sueter use him; Wedgwood/de Rothschild admire | P | — |
| ~~NZ leaders Sep 1922–Oct 1923 (11)~~ **PROMOTED** (Event) | New Zealand (+ London *Observer*) | press | contemporary | 6 hostile, 3 conflicted; Observer: Coalition "killed by Kemal" | P | — |
| ~~NZ leaders 1929–1938 (5)~~ **PROMOTED** (Event) | New Zealand | press | contemporary | Waikato Times 1929 "terror as inhuman as any" → 1934 "broken up… the Oriental middle ages" | P | — |
| Hansard Sept–Oct 1922 (Chanak weeks) | UK | politics | contemporary | ⌀ dug, nothing: Parliament in recess; no Kemal contribution 5 Aug–13 Dec 1922 | P (negative) | Nothing in Hansard; use the press (Times, Observer, Daily Mail, Morning Post) for British leaders — via a UK archive that serves openly (BNA is paywalled; Internet Archive for *The Times* digests only) |
| Lords 23 Nov 1922 (Newton, Wester Wemyss) and Commons 24 Nov 1922 (Capt. Berkeley), Mosley/Pringle/McNeill March 1923, Curzon 13 Feb 1923 (35,000 chars) | UK | politics | contemporary | Surface only under "Angora Government" — views of the Ankara government, not of Kemal by name | ⚠️ unread beyond the keyword | Read for Lausanne-era characterisations ("Ismet", "the Turks") and decide whether a government-level gaze belongs in the dataset |
| Hansard July 1938 Anglo-Turkish credit debate (Dalton, Nicholson, Sir John Simon, Templemore) | UK | politics | contemporary | Contributions found by "Ataturk" search only for Hudson and Strabolgi (already recorded); Dalton/Nicholson/Simon/Templemore mention Turkey without naming him | P (negative) | Read in full for implicit views |
| Hansard written answers (Written.json) 1919–38 | UK | politics | — | ⌀ dug, nothing: no Written contribution matched Kemal/Ataturk (sweep returned Spoken only) | P (negative) | — |
| API date artefact | UK | — | — | 1932-07 sittings listing Harmsworth/Malone/Herbert on Angora/Cilicia are 1922 sittings with a wrong year | J-inference | Report to Hansard/Parliament data team; do not cite |
| Trove (Australia): Kalgoorlie Miner 14 Oct 1922 p.4 "MUSTAPHA KEMAL PASHA." (article 93230845, ~1,481 words, personality analysis — looks like a leader or feature); Sun News-Pictorial (Melbourne) 16 Sep 1922 "MUSTAPHA KEMAL PASHA." (article 273899825, illustrated, likely a caption) | Australia | press | contemporary | Found via two browse runs (agent-reported, 19 steps each; the first, on the new search UI, returned an empty list; the second, on the classic `newspaper/result` URL, found these two). Article pages and `/rendition/…txt` are behind an Anubis proof-of-work wall for fetch and for render (the render returns page chrome without the article text) | ⚠️ agent-reported, unconfirmed — no text read, no quote taken | **Needs a human/browser:** open https://trove.nla.gov.au/newspaper/article/93230845 and copy the text; decide if the Kalgoorlie piece is an editorial. Trove API v3 (free key) would also work |
| Papers Past 1930–37 leaders beyond the five found (Press, Evening Post, Dominion, Otago Daily Times) | New Zealand | press | contemporary | A fetched sample of 1934–38 hits for "Ataturk" was almost entirely cable copy (illness Aug/Oct 1938, "Father of Turkey" June 1937); the leader-type hits sit in 1929–36 "Dictators of Europe", "The New Turkey" columns | P (partial) | Fetch: WT 5 Jun 1936 "The New Turkey", NZH 14 Dec 1937 "Changes in Turkey", Evening Star 4 Apr 1936 "Strong Men of Asia" (appears to be a serial feature, not a leader), Auckland Star 23 May 1936 "A Nation Remade" (visitor's article, praises "this extraordinary man") |
| Papers Past Oct 1923 "Turkey's Destiny" (Evening Star 26 Dec 1923) | New Zealand/UK | press | contemporary | Reprint of a *Reynolds's News* writer: "Kemal's Dynastic Dream", "the Dictator" | ⚠️ wire/feature, not editorial | Reynolds's News gaze if located at source |
| Canada, Australia, South Africa, India Hansards (Commons of Canada debates; Australian Parliamentary Debates 1922-23; Indian Legislative Assembly Debates) | Dominions | politics | contemporary | Not dug | — | Canadian Parliament has an open full-text API; Australian Hansard is searchable on ParlInfo; Indian Legislative Assembly debates on archive.org |


## Round 8 (hansard2) — script `b16_hansard2.py`, 11 records in `scratchpad/gazes8_hansard2.jsonl`, 2 Events

| Lead | Result |
|---|---|
| Lords 23 Nov 1922 / Commons 24 Nov 1922 / Curzon 13 Feb 1923 / Mosley, Pringle, McNeill Mar 1923 | **Read in full; ⌀ no contribution names Kemal.** Wester Wemyss ("these Angora Turks... a rabble", Lords 23 Nov) is a view of the movement, not of him; not recorded. Lamington, Berkeley, Noel Buxton, O'Connor 24 Nov: Angora/Turkish Government only. |
| Lloyd George 22 Dec 1920 original (Vol 136 cols 1895-97) | **⌀ not retrievable free**: Commons sittings for 10-23 Dec 1920 are absent from both the Hansard Search API and historic-hansard (only Lords present). Text stands verbatim via O'Connor 8 Feb 1922 (ledger "upgrade" row). Next: printed Official Report or hansard.parliament.uk in a browser. |
| Sweep: Ghazi, Angora, Turkish Nationalists, Turkish dictator, President of Turkey, Gazi, Kemal Pasha, Ataturk, Moustapha/Mustapha/Mustafa, 1919-38 both Houses, Spoken+Written | Search is fuzzy (phrases not matched exactly). Only genuinely new find was **OCR variant spellings** (Kamil, Kemil, Kcmil, Kliamil, Kernel): **PROMOTED** 10 records (Event "Kemal in the Commons: Variant Spellings, 1920-1922"). "Ghazi" hits are King Ghazi of Iraq (1936); "President of Turkey" 18 Nov 1936 (Mander) is a visit question; Written answers: nothing. Skipped passing mentions with no view: Parmoor 1924, Macquisten 1933, Emrys-Evans 1936, Wedgwood 1931 ("Gazi Kemal Pasha" asked for his views on Moslem Congress), Curzon 30 Mar 1922 / 9 Nov 1921, Bryce 17 Dec 1919, Craig Nov 1920. |
| Canada House of Commons 1922-24 | **PROMOTED** (witness): Mackenzie King 1 Feb 1923, pp. 30-31. lipad.ca is behind Cloudflare (403); used the Library of Parliament's parl.canadiana.ca instead (open; search-within-volume `search/page?q0.0=TERM&pkey=oop.debates_HOC1402_01`, page images via IIIF read by eye, no OCR text served). Kemal is named only there; Meighen's remarks and the 1924 Lausanne debate do not name him. Not read: 1922 session (vols HOC1401_01-04; Parliament did not meet in Sept 1922) beyond index hits. |
| Australia Hansard 1922-23 | **Needs a human/browser.** historichansard.net returns a BitNinja CAPTCHA; ParlInfo returns an Azure WAF challenge. Not circumvented. Parliament was not sitting in Sept 1922; try the Feb-Mar 1923 sittings and Hughes's Chanak cables. |
| API date artefact (1932-07 items by Herbert/Williams on "Kemalist" Asia Minor) | Still unresolved: really 1922; not used. |

## Round 15 (Nov 2026) — UK prime ministers before 1997, historic Hansard

⌀ dug: the Commons sitting indexes for 10–23 Nov 1938 (`api.parliament.uk/historic-hansard/sittings/1938/nov/<d>`, fetched free) have no tribute, question or statement on Atatürk's death; the Lords sittings of 15 Nov and others the same fortnight carry none either. Neville Chamberlain is therefore a dry end for Nov 1938. DuckDuckGo `site:api.parliament.uk/historic-hansard` queries (Baldwin, MacDonald, Attlee, Macmillan) returned no relevant sitting page; the engine does not index sitting text well. Method note: the sitting index pages are free to fetch and list section titles with word counts, so scanning titles for TURKEY/KEMAL/PRESIDENT is cheap, but 1923–38 questions on Turkey would need a day-by-day scan. UK head-of-state/government via the Anıtkabir book now covered: Elizabeth II 2008, Charles 2007, Starmer 2025 (see asia-africa-oceania.md round 15).

## Round 22 (Nov 2026) — TheyWorkForYou, Commons and Lords after 1938 (`b31_twfy.py`, 16 records, 2 Events, 13 People)

Seam: `theyworkforyou.com/search/?q=<term>&o=p` groups by speaker (with `pid`); `&pid=<id>&o=o` lists that speaker's hits with snippet and debate URL; debate pages carry full text and "Citation: HC/HL Deb ... cNNN". Free, plain curl with a browser UA works. Quote search is fuzzy on the speaker field (use `pid`, not `speaker:"Name"`). Terms Ataturk and Kemal give different sets: run both. Staged: Churchill 2 Aug 1944 (new), Eden 1941 and 1942, Clement Davies 1955, Hollis 1953, Selwyn Lloyd 1956, Noel-Baker 1956 and 1964, Wigg 5 Feb 1957, Straw 2003, MacShane 2004, Patten 2004, Howell 2011, Weidenfeld 2014, Glasman 2018, Corbyn 1988.

| Lead | Result |
|---|---|
| Churchill 1920, 1921 ("Kemalist ... sources"), Mar 1922 (Abu Kemal, place name) | Procedural/earlier; 1920 already recorded; no new record |
| Wigg 1946, 1953, 1954, 1956 (x2) | Anecdotes of Constantinople 1923 and Nasser-as-Kemal; the 1957 speech is the fullest; others cited in its caveat |
| Corbyn 6 Jun 1991 | Same stance as 1988; folded into the 1988 caveat |
| Hilary Benn Jun 2007 | ⌀ dug: listed under "Kemal" in the grouped list but the speaker filter returned no snippet; not read. Next: open the Jun 2007 sitting by date on TWFY |
| Nicolson 18 Mar 1943 ("Percy Lorraine in his relations with Kemal Attaturk") | Praise is of the ambassador; no view of Kemal; not recorded. Harold Nicolson's note exists |
| Onslow (Lords, 2001, 2002, 2006), Lord Balfe, Marlesford, Ramsbotham, Sandwich, Duncan, Clwyd, Rea (Dec 2004: "intensely nationalistic unitary state", Kurdish framing) | Seen in snippets; second-rank names; not staged. Rea 15 Dec 2004 and Onslow 18 Oct 2001 / 24 Sep 2002 ("secular, tyrannical, modernising") are the strongest if wanted |
| Baldwin, MacDonald, Chamberlain, Attlee, Macmillan, Wilson, Heath, Callaghan, Major, Blair, Cameron | ⌀ none appears in the Ataturk, Kemal, Kemalist or "Kemal Pasha" grouped lists |
| Eden other than 1941/42, Selwyn Lloyd other than Jul 1956, Noel-Baker (2 hits only) | ⌀ nothing further |
| Lloyd George, Bonar Law, Asquith, Cecil etc. | Already voices; no stronger statement checked |
| Churchill "Atatürk" | ⌀ no hit under the Ataturk spelling; only "Mustapha Kemal" (Aug 1944) |
| Commons 10–23 Dec 1920 | Still absent (see round 8) |

## Round 22 (anzac) — script `b31_anzac.py`, 12 records in `tools/.state/round22/gazes_anzac.jsonl`, 1 Event + 9 People

Seam: Australian PM Transcripts (pmtranscripts.pmc.gov.au) works for free: `/?body=<term>&items_per_page=100` lists hits (HTML), `/query?transcript=<id>` returns XML with full text. The `search?search_api_fulltext` and `/query?transcript=Term` forms do not. 21 hits for "Ataturk"; "Atatürk" and "Kemal" add none. Beehive via DuckDuckGo `site:beehive.govt.nz` + `$S fetch` of speech pages.

| Lead | Result |
|---|---|
| ~~Hawke 1990 ×, 1991~~ **PROMOTED** (Lone Pine 25 Apr 1990; Özal dinner 9 May 1991; Ankara dinner 23 Apr 1990 only in caveat, garbled OCR) | P |
| ~~Howard 2000, Rudd 2010, Gillard 2012, Abbott 2015 ×2, Turnbull 2016, Morrison 2019~~ **PROMOTED** | P |
| ~~NZ: Peters 2007 and 2024, Goff 2001~~ **PROMOTED** (ministers, not PMs) | P |
| Menzies, Holt, Whitlam, Fraser, Keating, Hayden | ⌀ dug, nothing: no PM Transcripts hit for Ataturk/Kemal; Hayden (GG) is not in that archive. Next step: ParlInfo (Hansard, Keating 1990s Gallipoli visits) and the Governor-General's speech archive (gg.gov.au) |
| Albanese | ⌀ no hit in PM Transcripts (archive appears to end before his Gallipoli speeches); try pm.gov.au |
| Howard 2000-04-23 (Ecevit presser), 2000-04-26 (Paris), 2006 (Laws) | Mentions only (secularism aside, journalist's framing); not promoted |
| Abbott 2013-12-12 ("immortal words of Ataturk"), 2015-04-23 Istanbul, 2015-05-12 House motion; Rudd 2008-09-04; Morrison 2019-03-20 (2GB), 2019-03-28 | Additional same-voice passages, cited in caveats only |
| NZ: Clark, Lange, Bolger, Muldoon, Ardern, Hipkins | ⌀ dug, nothing: Clark 2005 release names only the Ataturk research centre; Key 2015 Dawn Service and Luxon 2025 Chunuk Bair/Gallipoli speeches never name him. Beehive covers only 1999+; Lange/Muldoon/Bolger need NZ Hansard or Papers Past (to 1989 only for some papers). Hipkins/Ardern not found via DDG |
| Other beehive speeches naming him (Nathan Guy 2012, Jonathan Coleman 2013, Phil Goff 2008, Sandra Lee 2002, Peters 2008 Mehmetcik) | Minister-level, near-identical stock text; not recorded |
| ParlInfo | Not tried (bot protection risk) |


## Round 23 (parliaments) — script `b32_parliaments.py`, 14 records in `tools/.state/round23/gazes_parliaments.jsonl`, 3 Events, 12 People

| Lead | Result |
|---|---|
| ~~India: Legislative Assembly 14 Nov 1938 condolence (Desai, Nairang, Aney, Aikman, Zafar Ali Khan, Sir Abdur Rahim)~~ **PROMOTED** | P. archive.org `in.ernet.dli.2015.13994` (Govt of India Press vol. VII), pp. 2954–57. Nripendra Sircar and Jinnah's party not quoted; Sircar only agreed to adjourn |
| ~~India: Legislative Assembly 1924–25 (Chaman Lall 25 Mar 1924; Motilal Nehru 11 Feb 1925)~~ **PROMOTED** | P. eparlib.nic.in items 760688, 761482 on archive.org |
| ~~India: Constituent Assembly + Lok Sabha (Radhakrishnan, Gour, Brajeshwar Prasad, Kamath ×2, Frank Anthony)~~ **PROMOTED** | P. Found with `tools/fts.py` (free) over `eparlib.nic.in.*` items; full text downloadable (open items) |
| India, unstaged leads (OCR text read, view weak or speaker unsure) | Harchandrai Vishindas, LAD 6 Mar 1924 p.1252 (Abolition of the Khilafat "a lesson which the Government of India should take advantage of"); Faleiro, Lok Sabha 5 May 1986 (Kemal "a towering figure ... reformist to Islam", Muslim Women Bill); Ansar Harvani 8 Dec 1961 (national dress, Kemal); K. C. Sharma 5 Apr 1963 ("Ataturk in Turkey and Nehru in India"); Sri Lal/Council of State 1927 vol. I p.569 (speaker unread); Madras Legislative Assembly condolence resolution Nov 1938 (`tamildigitallibrary.004637`, pp.91-97, unread); Legislative Assembly vol. IV 1940 (`dli.ernet.237836`) "under the guidance of the late lamented Mustafa Kemal Pasha" (speaker unread); LAD 1933 vol. 4 ("famous Kamal Pasha", unread); Pakistan CA debates 1947-48 (CAPD_I_3, CAPD_III_3 mention Kamal Pasha; out of scope but a free seam) |
| India, ⌀ dug, nothing: Maulana Azad, Lohia, Syama Prasad Mookerjee, Vajpayee, Hiren Mukerjee, Masani, Indira Gandhi | No hit for any of them in the archive.org full text of the Lok Sabha/CA items returned for the Kemal/Ataturk/Kamal queries. Only the ~30 items archive.org indexes are searched; the rest of eparlib is not full-text-searchable from outside (rest/discover endpoint unreachable) |
| Canada, LiPaD (lipad.ca) | ⌀ blocked: Cloudflare 403 for curl and `ms fetch`; `ms render` 404. Needs a human browser to search Meighen/Bennett/Pearson/Diefenbaker |
| Canada, openparliament.ca (1994–2026; via `ms render`, search page) | ⌀ only back-benchers: Stockwell Day 2004 (describes Atatürk's republic, no verdict), Lalonde 2003, Ménard 2004, Vellacott ×2, Dzerowicz ×2, Nicholls ×2, Obhrai 2011, Acan 2025 (all brief Republic Day/Children's Day member statements). No Mulroney, Chrétien or Trudeau hit |
| Ireland, Oireachtas, round 24: Seanad 1922-2026 and Dáil 2014-2026 via per-sitting XML on data.oireachtas.ie (free, no WAF) | **Seam closed.** Broughan Dáil 18 Dec 2019 PROMOTED (b33). Dry ends: Baxter 1936 (dictator list), Moffatt/Connor 1999 (Kurdish policy, 'pre Ataturk'), Byrne 2025 (airport-naming list), Atatürk Airport condolences 2016 (Flanagan, Nash, Feighan). Seanad 2020-26 and Dáil 2020-26 hits were Kamala/Mustafa false positives. Superseded note: | Ireland, Oireachtas (old) | ⌀ search not reachable: the API has no full-text parameter; the website search ignores `term` on server render (JS) and `/en/search/` sits behind an AWS WAF challenge. De Valera, Cosgrave, Lemass, MacBride, Cruise O'Brien, FitzGerald, Haughey, Robinson untested. Next step: human browser at oireachtas.ie/en/debates/find/?q=Ataturk, or download the per-sitting XML (data.oireachtas.ie/akn/ie/debateRecord/...) and grep |
