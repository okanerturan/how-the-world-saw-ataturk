# -*- coding: utf-8 -*-
# Census round 15 (Nov 2026) — statesmen in their own words, memoirs/speeches read through archive.org full text.
# Seam: tools/fts.py (archive.org full-text search; snippets from lending-only books) + open djvu text of open scans.
# Records: Hitler (Reichstag 4 May 1941; Table Talk 1942), Goebbels diary (1938), Mussolini ("La luna crescente", 1922),
# Lloyd George (Truth about the Peace Treaties, 1938), Attlee (As It Happened, 1954), Nehru (Discovery of India, 1946),
# Khrushchev (Supreme Soviet report, 31 Oct 1959), Brzezinski (Strategic Vision, 2012).
# Quotes from open scans are checked against the text banked in tools/.state/round15/*.txt; quotes from
# lending-only books (Table Talk, Goebbels, Brzezinski) come from full-text-search snippets only and are flagged.
import json, os, re
from _lib import note, person

HERE = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(HERE, "tools", ".state", "round15")
NODE = "Statesmen on Atatürk in Their Own Words, Memoirs and Speeches"

def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"').replace("—", "-").replace("¬", "")
    s = re.sub(r"-\s*\n", "", s)
    return re.sub(r"\s+", " ", s).lower()

def bank(n):
    return norm(open(os.path.join(STATE, n), encoding="utf-8").read())

FTS = "snippet"  # marker for quotes seen only in full-text-search snippets
R = [
 dict(id="hitler-1941-05-04", voice="Adolf Hitler", role="Führer and Reich Chancellor; Reichstag speech on the Balkan campaign", c="Germany", cn="Germany",
      dom="politics", date="1941-05-04", era="posthumous", mirror="volkisch-purifier", pol="admiring", inten=1,
      saw="Calls the unnamed 'reconstructor of the new Turkey' great and ingenious, who gave the beaten allies 'the first example of resurrection'.",
      q="The great and ingenious reconstructor of the new Turkey gave his Allies, beaten by fate, the first example of resurrection.",
      art="speech", ev="P", med=None, src="balk.txt",
      cav="Reichstag speech of 4 May 1941, BBC translation as posted on archive.org (adolf-hitler-on-the-balkans-campaign, 'Translated by BBC'); Atatürk is not named, but the sentence follows 'Turkey had been our ally in the World War'. Translated quote; the German original was not located (de.wikisource has no page; try Domarus). Used to praise Turkey's neutrality ('thanks to the realistic attitude of her State leadership') against Yugoslavia, so partly instrumental. Existing Hitler records: 1933, 1938 telegram, 'teacher' 1938.",
      urls=["https://archive.org/details/adolf-hitler-on-the-balkans-campaign"],
      loc="Hitler, Reichstag speech 4 May 1941 (BBC translation), archive.org adolf-hitler-on-the-balkans-campaign", link="Adolf Hitler",
      nxt="German original (Domarus II; Reichstag protocols) as second source"),
 dict(id="hitler-table-talk-1942", voice="Adolf Hitler", role="Führer; table talk at headquarters", c="Germany", cn="Germany",
      dom="politics", date="1942-08", era="posthumous", mirror="volkisch-purifier", pol="admiring", inten=2,
      saw="Holds that Kemal Pasha 'acted wisely' after seizing power, and that the speed with which he rid himself of his clergy is a remarkable chapter.",
      q="The rapidity with which Mustapha Kemal Ataturk rid himself of his parsons makes one of the most remarkable chapters",
      art="memoir", ev="J", med="Trevor-Roper (ed.), Hitler's Secret Conversations 1941-1944 (1961 US ed.; Table Talk, Bormann notes)", src=None,
      cav="Seen only as archive.org full-text-search snippets (hitlerssecretcon0000hrtr; snippet cuts off at 'chapters'). The book's index lists 'Ataturk; Kemal, 233, 372, 566' (snippet pages not shown), and the chapter heading on the same conversation reads 'Boris the Fox of Bulgaria—Political plots—Wisdom of Kemal Ataturk'. Other snippets from the same book: 'That's why Kemal Pasha acted wisely, immediately after the seizure' and 'Kemal Ataturk, who had nothing to do with his compatriots' (a racial aside on Kurds and Asia Minor). Date 1942-08 is the task's lead (1 Aug 1942), not read off the page: confirm. Table Talk is a record of Bormann's notes, not Hitler's own writing.",
      urls=["https://archive.org/details/hitlerssecretcon0000hrtr"],
      loc="Hitler's Secret Conversations 1941-1944 (Trevor-Roper), index pp. 233, 372, 566; archive.org hitlerssecretcon0000hrtr (search-inside)", link="Adolf Hitler",
      nxt="Open the page in a borrowed copy or the Weinberg 2008 edition for the exact date and page"),
 dict(id="goebbels-1938-11", voice="Joseph Goebbels", role="Reich Propaganda Minister; diary", c="Germany", cn="Germany",
      dom="politics", date="1938-11", era="funeral", mirror=None, pol="conflicted", inten=1,
      saw="On Ismet Inönü's election, notes that he is well disposed to Germany, 'which could not always be said of Kemal Pasha'.",
      q="Er ist gut zu uns eingestellt, was man von Kemal Pascha nicht immer sagen konnte.",
      art="memoir", ev="P", med=None, src=None,
      cav="Search-inside snippet of Die Tagebücher von Joseph Goebbels: sämtliche Fragmente (archive.org dietagebuchervon0003goeb; the snippet starts at 'gewählt.', i.e. 'elected'), so the entry date (about 11-12 Nov 1938, Inönü's election) is inferred and the page not seen. Translation: 'He is well disposed toward us, which could not always be said of Kemal Pasha.' Same book, an earlier entry (12 June 1937): 'Über Kemal Paschas abenteuerliches Leben weiter gelesen' (reading a biography of Kemal) — no judgement. The English Goebbels Diaries 1942-43 have only an editor's note on Atatürk.",
      urls=["https://archive.org/details/dietagebuchervon0003goeb"],
      loc="Goebbels, Tagebücher, archive.org dietagebuchervon0003goeb (search-inside; entry date and page unseen)", link="Adolf Hitler",
      nxt="Read the Nov 1938 entry in the Fröhlich edition (Teil I, Bd 6) for date and surrounding text"),
 dict(id="mussolini-1922-09", voice="Benito Mussolini", role="Fascist leader, journalist (article in Il Popolo d'Italia circle; reprinted 1930)", c="Italy", cn="Italy",
      dom="politics", date="1922-09", era="contemporary", mirror="nation-forge-template", pol="instrumental", inten=2,
      saw="Reads Kemal's victory over Greece as definitive for Anatolia, the product of French arming against Britain, and a lesson that Europe needs a lasting peace.",
      q="La vittoria di Kemal pascià, è definitiva per ciò che riguarda il territorio anatolico.",
      art="article", ev="P", med=None, src="mus.txt",
      cav="Article 'La luna crescente' (about 2,000 words), Benito Mussolini, Tempi della Rivoluzione Fascista (1930), pp. 108-110ff, archive.org TempiDellaRivoluzioneFascista (open). Translation: 'Kemal Pasha's victory is definitive as regards Anatolian territory.' The OCR printed 'cbe', corrected to 'che'. The original publication date is not printed in the scan; September 1922 is inferred from the closing line about 'the flames of the burning of Smyrna'. Mussolini's frame: Kemal's march on Smyrna is 'a sort of compensation' for France's thwarted Ruhr march; 'La morale della vittoria kemalista' is that Europe needs fifty years of peace. Smyrna is mentioned only as a date marker; the census records no view of the fire itself. Predates and differs in tone from the 1928 interview record.",
      urls=["https://archive.org/details/TempiDellaRivoluzioneFascista"],
      loc="Mussolini, Tempi della Rivoluzione Fascista (1930), 'La luna crescente', pp. 108-110ff", link="Benito Mussolini",
      nxt="Identify the periodical and date (Opera Omnia vol. XVIII or Il Popolo d'Italia, Sept-Oct 1922)"),
 dict(id="lloyd-george-1938", voice="David Lloyd George", role="Former Prime Minister; memoir The Truth About the Peace Treaties (1938)", c="United Kingdom", cn="United Kingdom",
      dom="politics", date="1938", era="contemporary", mirror="chivalrous-enemy", pol="conflicted", inten=2,
      saw="Describes Kemal as an unexpected 'portent' at the Conference, the Gallipoli commander who stopped the British at Suvla, who rallied Turkish pride; Allied intelligence 'unintelligent'.",
      q="It was owing to his prompt and daring leadership that the ineffective and bungled British attack at Suvla Bay had been checked, and the last hope of forcing the Dardanelles in the Great War for ever lost.",
      art="memoir", ev="P", med=None, src="lg.txt",
      cav="Vol. II, p. 1285 (running heads 'EUROPEAN AND ASIATIC TURKEY 1285'; the quote sits between that head and '1286'), open DLI scan in.ernet.dli.2015.523826. Same chapter, p. 1292: 'Kemal roused the pride of a governing caste'; elsewhere he calls Turkey's rule a 'misgoverning' of centuries. Written in 1938 about 1920; hostile to the Greek enterprise he himself had backed in Parliament (see his 1920 and 1922 records). Chapter headings: 'Mustapha Kemal takes the field', 'Kemal the strong man of Turkey'.",
      urls=["https://archive.org/details/in.ernet.dli.2015.523826"],
      loc="Lloyd George, The Truth About the Peace Treaties, vol. II (1938), p. 1285 (also p. 1292)", link="David Lloyd George",
      nxt="Chapter 'Kemal the strong man of Turkey' (not read in full) for a stronger passage"),
 dict(id="attlee-1954", voice="Clement Attlee", role="Labour leader, Prime Minister 1945-51; memoir As It Happened (1954)", c="United Kingdom", cn="United Kingdom",
      dom="politics", date="1954", era="posthumous", mirror="chivalrous-enemy", pol="witness", inten=1,
      saw="Attlee, a Suvla Bay veteran, says British forces might have held the Sari Bair height but for Kemal Pasha commanding the Turkish division there.",
      q="But for Mustapha Kemal Pasha being in command of a Turkish Division at the crucial point, we might have held that height.",
      art="memoir", ev="P", med=None, src="attlee.txt",
      cav="As It Happened (Heinemann, 1954), p. 41 (index 'Kemal Pasha, Mustapha, 41'); open scan in.ernet.dli.2015.150132. A single-sentence acknowledgement of a Gallipoli opponent, intensity 1; no wider verdict. Different editions paginate it at 41, 53, 61.",
      urls=["https://archive.org/details/in.ernet.dli.2015.150132"],
      loc="Attlee, As It Happened (1954), p. 41", link="Gallipoli Campaign",
      nxt=""),
 dict(id="nehru-1946", voice="Jawaharlal Nehru", role="Indian National Congress leader; The Discovery of India (written 1944, published 1946)", c="British India", cn="India",
      dom="politics", date="1946", era="posthumous", mirror="anti-colonial-liberator", pol="conflicted", inten=2,
      saw="Says Atatürk's secular reforms cost him orthodox Moslem admiration but won the young, and that eliminating the Khilafat's core collapsed the Indian Khilafat movement.",
      q="This very policy, however, made him more popular among the younger generation of both Hindus and Moslems.",
      art="book", ev="P", med=None, src="doi2.txt",
      cav="The Discovery of India, ch. 'Kemal Pasha; Nationalism in Asia: Iqbal', pp. 416-417 (the book's index: 'Kemal Pasha, The Ataturk, 416-17'); open scans dli.scoerat.12288 (clean text) and in.gov.ignca.14765. Same passage: 'Kemal Pasha was naturally popular in India with Moslems and Hindus alike. He had not only rescued Turkey from foreign domination and disruption but had foiled the machinations of European imperialist powers, especially England'; 'The Ataturk partly destroyed the dream structure that had gradually grown up in the Indian Moslem mind'; 'when the core itself was eliminated by the Ataturk the superstructure collapsed'. Written in Ahmadnagar Fort 1944. Nehru's existing record is 1934 (Glimpses). A later Nehru letter to chief ministers (c. Aug 1951, Letters to Chief Ministers vol. 2, p. 459) says Kamal Ataturk 'drove out the allied occupation forces from Turkey and later defeated the Greek Army, which was supported by the British' (context only, not stored).",
      urls=["https://archive.org/details/dli.scoerat.12288jawaharlalnehruthediscoveryofindia9aug1942to28march1945", "https://archive.org/details/in.gov.ignca.14765"],
      loc="Nehru, The Discovery of India (1946), pp. 416-417", link="Jawaharlal Nehru",
      nxt=""),
 dict(id="khrushchev-1959-10-31", voice="Nikita Khrushchev", role="Soviet Premier; report to the USSR Supreme Soviet, 31 Oct 1959", c="Soviet Union", cn="Russia",
      dom="politics", date="1959-10-31", era="posthumous", mirror=None, pol="instrumental", inten=1,
      saw="Reproaching Turkey over US bases, recalls friendlier days when its policy was shaped by 'such an outstanding leader as Kemal Ataturk'.",
      q="We sincerely want our relations to be built in the spirit of friendliness and cooperation typical of the fairly recent past when the policy of Turkey was shaped by such an outstanding leader as Kemal Ataturk,",
      art="speech", ev="P", med=None, src="khr.txt",
      cav="'The international situation and Soviet foreign policy: report given at the third session of the U.S.S.R. Supreme Soviet on October 31, 1959' (Crosscurrents Press, 1960), p. 17 (page number printed after the passage), open scan TheInternationalSituationAndSovietForeignPolicyReportGivenAtThe (file ISSFP_djvu.txt). Official English translation. Used as a reproach to the Menderes-era government, so instrumental. The passage was taken from Khrushchev Speaks (index 'Ataturk, Mustafa Kemal, 402') too. Khrushchev Remembers was searched: nothing.",
      urls=["https://archive.org/details/TheInternationalSituationAndSovietForeignPolicyReportGivenAtThe"],
      loc="Khrushchev, report to the Supreme Soviet, 31 Oct 1959 (Crosscurrents Press 1960), p. 17", link="Mustafa Kemal Atatürk",
      nxt="Russian original (Pravda 1 Nov 1959) as a second source"),
 dict(id="brzezinski-2012", voice="Zbigniew Brzezinski", role="US National Security Adviser 1977-81; Strategic Vision (2012)", c="United States", cn="United States",
      dom="politics", date="2012", era="posthumous", mirror="nation-forge-template", pol="admiring", inten=2,
      saw="Calls Atatürk Turkey's 'successful' modernizer, guided by a historic vision, whose secularization from above set the model that failed in China and elsewhere.",
      q="Because Ataturk imposed secularization from above in 1924,",
      art="book", ev="J", med=None, src=None,
      cav="Search-inside snippets only (archive.org strategicvisiona0000brze; pages not shown), so the evidence is J rather than P. Other snippets: 'The ambitious nationalist mystique of Ataturk was contagious among fervent younger Turks'; 'In firmly promoting it, Ataturk was guided by a historic vision'; a contrast with 'China's failed equivalents of Turkey's successful Ataturk. Mao Zedong was a self-destructive equivalent'. The quote is a fragment because the snippet stops there (the sentence goes on about Europeans' view of Turkish democracy). Also The Grand Chessboard (1997): 'No Russian Ataturk is now in sight' (restricted copy grandchessboarda00brze_0).",
      urls=["https://archive.org/details/strategicvisiona0000brze"],
      loc="Brzezinski, Strategic Vision (2012), archive.org strategicvisiona0000brze (search-inside, page unseen); Grand Chessboard (1997)", link="Mustafa Kemal Atatürk",
      nxt="Page numbers and full sentences from a borrowed copy"),
]

for r in R:
    assert len(r["saw"].split()) <= 25, (r["id"], len(r["saw"].split()))
    if r["src"]:
        assert norm(r["q"]).replace("cbe", "che") in bank(r["src"]).replace("cbe", "che") or norm(r["q"].rstrip(",")) in bank(r["src"]), r["id"]
        print("quote verified:", r["id"])
    else:
        print("snippet-only:", r["id"])

with open(os.path.join(STATE, "gazes_statesmen.jsonl"), "w", encoding="utf-8") as f:
    for r in R:
        rec = {"id": r["id"], "voice": r["voice"], "voice_type": "person", "role": r["role"], "country": r["c"],
               "country_now": r["cn"], "domain": r["dom"], "date": r["date"], "era": r["era"], "mirror": r["mirror"],
               "polarity": r["pol"], "intensity": r["inten"], "what_they_saw": r["saw"], "quote": r["q"],
               "artifact": r["art"], "evidence": r["ev"], "mediated_by": r["med"], "caveat": r["cav"],
               "node": NODE, "sources": r["urls"]}
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")

with open(os.path.join(STATE, "ledger_statesmen.md"), "w", encoding="utf-8") as f:
    f.write("| Claim | Node | Status | Sources | Next step |\n|---|---|---|---|---|\n")
    for r in R:
        qs = r["q"]
        f.write("| %s (%s, %s): \"%s\" | %s | verified %s (%s) | %s | %s |\n" % (
            r["voice"], r["role"][:50], r["date"], qs[:110].replace("|", "/") + ("..." if len(qs) > 110 else ""),
            NODE, r["ev"], r["loc"], "; ".join(r["urls"][:1]), r["nxt"] or "none"))

new_people = {
 "Joseph Goebbels": ("Reich Propaganda Minister", "German", "1897–1945", "mild reservation",
    "His diary notes, on İnönü's election in November 1938, that the new president is well disposed to Germany, 'which could not always be said of Kemal Pasha'."),
 "Nikita Khrushchev": ("Soviet Premier, 1958–1964", "Soviet", "1894–1971", "instrumental",
    "In his Supreme Soviet report of 31 October 1959 he held up the Turkey of 'such an outstanding leader as Kemal Ataturk' against the Turkey of US missile bases."),
 "Clement Attlee": ("British Prime Minister, 1945–1951", "British", "1883–1967", "chivalrous opponent",
    "A Suvla Bay veteran, he wrote in 1954 that the British might have held the Sari Bair height 'but for Mustapha Kemal Pasha being in command of a Turkish Division at the crucial point'."),
 "Zbigniew Brzezinski": ("US National Security Adviser, 1977–1981", "American", "1928–2017", "admirer (strategist)",
    "In *Strategic Vision* (2012) he cites Atatürk as Turkey's 'successful' modernizer, guided by a historic vision, against China's failed equivalents."),
}
for name, (role, nat, life, stance, desc) in new_people.items():
    if os.path.exists(os.path.join(HERE, "vault", "People", name + ".md")):
        continue
    person(name, role=role, nat=nat, life=life, stance=stance, tags=["verified", "statesman"],
           body="%s See [[%s]] for the quote and sources.\n\n## Sources\n- See [[%s]].\n" % (desc, NODE, NODE))

body = ["""
Round 15 read statesmen's memoirs, diaries, table talk and speeches through the archive.org full-text search (snippets
from inside lending-only books) and the open scans of the rest. Nine records, from Mussolini's article on the Greek defeat
(1922) to Brzezinski's 2012 book. They are mostly short, and the pattern is as informative as the praise.

## The pattern

- **The enemy remembered:** [[David Lloyd George]] (1938) and [[Clement Attlee]] (1954) both place Kemal at Suvla Bay: the officer who
  stopped the British. For Lloyd George he is also the unforeseen 'portent' of the peace conference; for Attlee a single sentence of reluctant credit (kept in this note, not counted as a gaze: the check found no stated view).
- **Hitler and his circle:** the Reichstag speech of 4 May 1941 (BBC translation) never names him but calls the 'reconstructor of the new Turkey'
  'great and ingenious'; the table talk of 1942 calls Kemal's quick riddance of the clergy 'one of the most remarkable chapters'; and
  [[Joseph Goebbels]] in 1938 notes that [[İsmet İnönü]]'s Turkey is friendlier than Kemal's was. See also [[Adolf Hitler]].
- **A rival dictator reading the war:** [[Benito Mussolini]], 1922, treats the victory as a fact of great-power politics: French arms against British designs, a definitive settlement of Anatolia.
- **Atatürk as a Cold War instrument:** [[Nikita Khrushchev]] (1959) recalls an outstanding Atatürk against the Turkey of US missile bases.
- **The reformer assessed from India:** [[Jawaharlal Nehru]] (written 1944) is the most analytic: the popularity that waned with the orthodox but rose among the young, and the Khilafat movement that collapsed once its Turkish core was removed.
- **The strategist:** [[Zbigniew Brzezinski]] uses Atatürk as the template of top-down modernization.
"""]
for r in R:
    body.append("\n## %s (%s)\n" % (r["voice"], r["date"]))
    body.append("*%s*\n" % r["saw"])
    body.append("> %s\n" % r["q"])
    body.append("%s Location: %s. Evidence %s. See [[%s]].\n" % (r["cav"], r["loc"], r["ev"], r["link"]))

body.append("""
## Not stored, and dry ends (round 15)

- **Ciano:** the *Diary 1937-1943* and *Hidden Diary* index one entry on Kemal (p. 183 in the Hidden Diary); the snippets show only a passing mention. Not stored.
- **Nixon, *Leaders*; Kissinger:** no hits for Atatürk under Nixon's authorship. Kissinger, *Years of Upheaval* (1982) mentions a Shah wanting a secular state 'in the reformist mold of Kemal Ataturk': a description of the Shah's aim, not Kissinger's view.
- **Eden:** *Facing the Dictators* indexes one Atatürk entry (p. 529) and a line on his ships order after a visit; no stated view. Macmillan, Golda Meir, Dayan, Peres, Gorbachev (his only hit is an Ikeda dialogue footnote), Tito, Zia-ul-Haq, Suharto, Saddam Hussein: no results under their authorship.
- **Balfour, NYT 1 Oct 1922, 'Most terrible of all the terrible Turks':** not reached; the full-text search finds no Balfour text with Kemal.
- **Not reached:** de Gaulle's *Mémoires*, Arafat, Hafez al-Assad, Woodrow Wilson, Chiang Kai-shek diary (existing record stands).

## Sources
- archive.org full-text search and open scans; the identifier of each is given in the record above.
""")
note("Events", NODE, {"type": "event", "when": "1922–2012", "tags": ["event", "verified", "statesmen", "memoirs"]}, "\n".join(body))
print("ok", len(R), "records")
