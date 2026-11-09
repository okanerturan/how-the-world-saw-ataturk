# -*- coding: utf-8 -*-
# Census round 14 (Nov 2026) — famous writers and thinkers in their own words about Atatürk, second pass.
# Records: John Gunther (Inside Europe, ch. XXXI), John Dewey (Angora, the New Turkey, 1924), Harold Nicolson (Curzon: The
# Last Phase, 1934), Richard Coudenhove-Kalergi (Crusade for Pan-Europe, 1943, two passages), Rebecca West (Black Lamb and
# Grey Falcon, 1941). All from openly served archive.org djvu texts (DLI scans); windows of each text are banked in
# tools/.state/round14/src_*.txt and every quote is checked against its bank before anything is written.
import json, os, re, sys
from _lib import note, person

HERE = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(HERE, "tools", ".state", "round14")
NODE = "Famous Pens on Atatürk — Gunther, Dewey, Nicolson, Coudenhove-Kalergi, West"


def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"').replace("­", "")
    s = s.replace("*", "'")
    s = re.sub(r"[-¬]\s*\n", "", s)
    s = re.sub(r"\s+", " ", s)
    return s


def bank(n):
    return norm(open(os.path.join(STATE, n), encoding="utf-8").read())


GUN = "https://archive.org/details/in.ernet.dli.2015.13600"
GUN36 = "https://archive.org/details/insideeurope00gunt"
COU = "https://archive.org/details/dli.ernet.155751"
NIC = "https://archive.org/details/in.ernet.dli.2015.208069"
WV1 = "https://archive.org/details/dli.ernet.12968"
DEW = "https://archive.org/details/impressions_of_soviet_russia"

R = [
 dict(id="gunther-1936", voice="John Gunther", role="American foreign correspondent; author of Inside Europe", c="United States", cn="United States",
      dom="press", date="1936", era="contemporary", mirror=None, pol="conflicted", inten=2,
      saw="Calls Atatürk the 'roughneck of dictators' (Hitler a milksop, Mussolini a dandy), a psychopath-patriot who nonetheless remade a rotten nation.",
      q="Kamal Ataturk is the roughneck of dictators.",
      art="book", ev="P", med=None,
      cav="Chapter XXXI 'The Turkish Colossus', pp. 417-424 of the Hamish Hamilton revised illustrated edition (1938 scan, DLI in.ernet.dli.2015.13600; the quoted sentence is on p. 419). First edition January 1936: the chapter's 'Father of Turks' sentence is confirmed in the 1936 impression only by an archive.org search-inside snippet (insideeurope00gunt, lending), so the 1938 text is the one read. Same chapter: 'The blond, blue-eyed combination of patriot and psychopath who is dictator of Turkey'; 'Kamal Ataturk, who strides the Turkish landscape like a colossus'; 'This man ... resembles no one so much as Peter the Great'; and, p. 422, 'Other people have created nations. Kamal's job was harder.' He also counts the 1926 hangings and the slapped Egyptian minister, and says 'it is no tribute to Kamal' that he ejected sultan and caliph. Gunther's anecdotes (the champagne party on the night of the hangings, the slap) are his own reportage and are not checked here.",
      src=["src_gunther.txt"], urls=[GUN, GUN36],
      loc="Inside Europe (Hamish Hamilton, rev. illus. ed., 1938), ch. XXXI, pp. 417-424 (quote p. 419)", link="John Gunther"),
 dict(id="dewey-1924", voice="John Dewey", role="American philosopher, visiting adviser on Turkish education", c="United States", cn="United States",
      dom="letters", date="1924", era="contemporary", mirror="modernization-poster-child", pol="admiring", inten=2,
      saw="Arriving in Angora from tired Constantinople, he concludes the new leaders' instincts are truer than the capital's sophistication and sees pioneer vigour.",
      q="the instincts of the new leaders are truer than the sophisticated wisdom of Constantinople",
      art="article", ev="P", med=None,
      cav="'Angora, the New Turkey', written in 1924 (published in The New Republic that year; reprinted in Impressions of Soviet Russia and the Revolutionary World, 1929, pp. 208-215; the quote falls on about p. 213 between page markers [212] and [214]). Mustafa Kemal is NOT named in either Turkey article; the only mention is a primary school 'named for Mustapha Kemal and the other for his wife'. The gaze is on 'the new leaders' and 'the new rulers' of Turkey. The existing People note says Dewey praised 'Atatürk' in his writing: the text read does not support that for the two 1924 articles; the Report of 1924 was not read.",
      src=["src_dewey.txt"], urls=[DEW],
      loc="Impressions of Soviet Russia and the Revolutionary World (New Republic Inc., 1929), 'Angora, the New Turkey', c. p. 213", link="John Dewey"),
 dict(id="nicolson-1934", voice="Harold Nicolson", role="British diplomat and writer; biographer of Lord Curzon", c="United Kingdom", cn="United Kingdom",
      dom="letters", date="1934", era="contemporary", mirror="chivalrous-enemy", pol="conflicted", inten=2,
      saw="A detached diplomat-historian's sketch: Kemal's career is typically Young Turk, and his luck came from the enmities he made, not friends won.",
      q="he owed his immense good fortune, not to the friendships which he had been able to conciliate, but to the enmities which he had aroused.",
      art="book", ev="P", med=None,
      cav="Curzon: The Last Phase 1919-1925 (Constable, 1934), ch. IV 'Smyrna', p. 116 (page numbers from running heads of DLI scan in.ernet.dli.2015.208069; the other DLI scan 190097 has garbled OCR at this line). He writes it as a diplomat-historian who says a 'detailed estimate' is 'beyond the range of this study'. On p. 352 he calls Poincare 'an adversary more potent and more skilled than any Ismet, than any Mustapha Kemal' (OCR reads 'Msutapha').",
      src=["src_nicolson.txt"], urls=[NIC],
      loc="Curzon: The Last Phase (Constable, 1934), p. 116 (also p. 352)", link="Harold Nicolson"),
 dict(id="coudenhove-kalergi-1943", voice="Richard Coudenhove-Kalergi", role="Founder of the Pan-Europe movement", c="Austria (exile in the United States)", cn="Austria",
      dom="politics", date="1943", era="posthumous", mirror="modernization-poster-child", pol="admiring", inten=2,
      saw="Calls Atatürk Turkey's 'great leader' who took up Western civilization without European pressure, a model for reconciling Europe and Islam.",
      q="embraced without any European pressure all vital elements of Western civilization.",
      art="book", ev="P", med=None,
      cav="Crusade for Pan-Europe: Autobiography of a Man and a Movement (Putnam, 1943), ch. XXVII 'The Future of Asia', around p. 280 (printed page not read; page markers 275 and 282 bracket the passage in the DLI scan dli.ernet.155751). The full sentence: 'The most important step toward such a new understanding between Europe and the Near East has been accomplished by modern Turkey, that recently under its great leader Kemal Ataturk, embraced without any European pressure all vital elements of Western civilization.' Also ch. XIV p. 125: Greece and Turkey 'were blessed with far-sighted and energetic statesmen - Kemal Ataturk, the Turkish dictator, and Eleutherios Venizelos'. Venizelos' admiration of Kemal, told to Coudenhove in Vienna (pp. 125-126), is reported second-hand and not stored as Venizelos' gaze here.",
      src=["src_coudenhove_ch27.txt"], urls=[COU],
      loc="Crusade for Pan-Europe (Putnam, 1943), ch. XXVII c. p. 280 (also ch. XIV pp. 125-126)", link="Richard Coudenhove-Kalergi"),
 dict(id="coudenhove-kalergi-1943-sevres", voice="Richard Coudenhove-Kalergi", role="Founder of the Pan-Europe movement", c="Austria (exile in the United States)", cn="Austria",
      dom="politics", date="1943", era="posthumous", mirror="nation-forge-template", pol="conflicted", inten=2,
      saw="Reads Kemal's refusal of Sèvres as the first great counter-revolution against the Paris treaties, proof that a heroic mind beat diplomacy, and a revisionist's template.",
      q="military power and a heroic mind had proved to be stronger than all diplomatic action.",
      art="book", ev="P", med=None,
      cav="Crusade for Pan-Europe (Putnam, 1943), ch. VIII 'Dismembered Europe', pp. 67-68 (page header 66 precedes and 70 follows in the DLI scan). Same page: 'this victory of Kemal inspired the nationalists in Germany, Hungary, and Bulgaria with new hope ... it would be enforced sooner or later a la Kemal.' The tone is a European federalist's lament that Kemal's success made revisionism fashionable; it is written in 1943, looking back at the 1920s.",
      src=["src_coudenhove_ch8.txt"], urls=[COU],
      loc="Crusade for Pan-Europe (Putnam, 1943), ch. VIII, pp. 67-68", link="Richard Coudenhove-Kalergi"),
 dict(id="west-1941", voice="Rebecca West", role="British novelist and travel writer", c="United Kingdom", cn="United Kingdom",
      dom="letters", date="1941", era="posthumous", mirror=None, pol="witness", inten=1,
      saw="Tosses off that Atatürk's blue eyes show him 'at least half Slav'; elsewhere praises 'the Ataturk's Turkey, robust and gracious'.",
      q="the Ataturk, like some sultans, several viziers, and the flower of the Janissaries, was at least half Slav.",
      art="book", ev="P", med=None,
      cav="Black Lamb and Grey Falcon (Macmillan, 1941), written after a 1937 Yugoslav journey; read in the two-volume 1946 printing (DLI scans). The quote is in vol. I at about p. 633 (page headers 633-634). Other lines: vol. II p. 287 'as they are in the Ataturk's Turkey, robust and gracious'; vol. I p. 316 the Turks of South Serbia 'have remained what the Ataturk would not permit Turks to be any longer'; vol. II p. 452 a Turkish journalist's voice ('the Ataturk has taught us not to be proud of it') which is her reporting, not her own judgement. Polarity is the nearest enum: aside, not an assessment; intensity 1.",
      src=["src_west_v1.txt"], urls=[WV1, "https://archive.org/details/in.ernet.dli.2015.12979"],
      loc="Black Lamb and Grey Falcon (1941; 1946 two-volume printing), vol. I c. p. 633", link="Rebecca West"),
]

bad = []
for r in R:
    full = bank(r["src"][0])
    q = norm(r["q"])
    if q not in full:
        bad.append(r["id"])
if bad:
    sys.exit("quote not found in source bank: %s" % bad)
for r in R:
    assert len(r["saw"].split()) <= 25, (r["id"], len(r["saw"].split()))

with open(os.path.join(STATE, "gazes_writers.jsonl"), "w", encoding="utf-8") as f:
    for r in R:
        rec = {"id": r["id"], "voice": r["voice"], "voice_type": "person", "role": r["role"], "country": r["c"],
               "country_now": r["cn"], "domain": r["dom"], "date": r["date"], "era": r["era"], "mirror": r["mirror"],
               "polarity": r["pol"], "intensity": r["inten"], "what_they_saw": r["saw"], "quote": r["q"],
               "artifact": r["art"], "evidence": r["ev"], "mediated_by": r["med"], "caveat": r["cav"],
               "node": NODE, "sources": r["urls"]}
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")

nxt = {"gunther-1936": "Page-check 1936 impression (HathiTrust / lending) for identical text; first edition pagination",
       "dewey-1924": "New Republic 1924 original issue; Dewey's Report on Turkish education for any naming of Mustafa Kemal",
       "nicolson-1934": "Nicolson's 1919-23 diaries (Harold Nicolson: Diaries and Letters) for a personal view",
       "coudenhove-kalergi-1943": "Printed page; Pan-Europa journal 1920s-30s for a contemporary statement (Gallica/ANNO)",
       "coudenhove-kalergi-1943-sevres": "None",
       "west-1941": "Printed page of the 1941 first edition"}
with open(os.path.join(STATE, "ledger_writers.md"), "w", encoding="utf-8") as f:
    f.write("| Claim | Node | Status | Sources | Next step |\n|---|---|---|---|---|\n")
    for r in R:
        f.write("| %s (%s, %s): \"%s\" | %s | verified %s (%s) | %s | %s |\n" % (
            r["voice"], r["role"][:50], r["date"], r["q"][:110].replace("|", "/") + ("..." if len(r["q"]) > 110 else ""),
            NODE, r["ev"], r["loc"], "; ".join(r["urls"][:1]), nxt[r["id"]]))

person("John Gunther", role="American journalist; author of the 'Inside' books", nat="American", life="1901–1970",
       stance="sceptical admirer", tags=["observer", "journalist", "verified"],
       body="""Chicago Daily News correspondent in Europe and author of *Inside Europe* (1936), a bestseller that profiled the continent's dictators one chapter at a time. His chapter on Atatürk, 'The Turkish Colossus', calls him 'the roughneck of dictators' and 'the dictator-type carried to its ultimate extreme', and also the man who 'took a nation that was centuries deep in rot, pulled it to its feet, wiped its face, re-clothed it, transformed it, made it work'. See [[%s]].

## Sources
- John Gunther, *Inside Europe*, ch. XXXI, Hamish Hamilton revised illustrated ed. (1938), DLI scan on archive.org (in.ernet.dli.2015.13600).
""" % NODE)

person("Richard Coudenhove-Kalergi", role="Founder of the Pan-Europe movement", nat="Austrian (Japanese-Austrian-Bohemian)", life="1894–1972",
       stance="admirer, with reservations about revisionism", tags=["admirer", "intellectual", "verified"],
       body="""Austrian count who founded the Pan-European Union in 1923. In his 1943 autobiography *Crusade for Pan-Europe* he names Atatürk a 'great leader' whose Turkey took up Western civilization 'without any European pressure', and elsewhere warns that Kemal's defiance of Sèvres taught Germany, Hungary and Bulgaria to demand treaty revision 'a la Kemal'. He also reports that [[Eleftherios Venizelos]] told him in Vienna that Kemal's Turkey had become 'an integral part of Western civilization'. See [[%s]].

## Sources
- R. N. Coudenhove-Kalergi, *Crusade for Pan-Europe* (Putnam, 1943), DLI scan on archive.org (dli.ernet.155751), ch. VIII, XIV, XXVII.
""" % NODE)

person("Harold Nicolson", role="British diplomat, biographer and diarist", nat="British", life="1886–1968",
       stance="detached", tags=["observer", "diplomat", "verified"],
       body="""Diplomat and writer whose *Curzon: The Last Phase* (1934) is the standard British account of the Lausanne years seen from the Foreign Office. On Mustafa Kemal he is unsentimental: the career is 'typically Young Turk', and the luck came from the enmities. See [[%s]] and [[Lord Curzon]].

## Sources
- Harold Nicolson, *Curzon: The Last Phase 1919–1925* (Constable, 1934), p. 116, DLI scan on archive.org (in.ernet.dli.2015.208069).
""" % NODE)

person("Rebecca West", role="British novelist, journalist and travel writer", nat="British", life="1892–1983",
       stance="aside", tags=["observer", "writer", "verified"],
       body="""In *Black Lamb and Grey Falcon* (1941), a book about Yugoslavia, Atatürk appears by the way, in several asides. She sets the Turks of Ottoman Macedonia against 'the Turks as they are in the Ataturk's Turkey, robust and gracious', and notes that his blue eyes make him 'at least half Slav'. See [[%s]].

## Sources
- Rebecca West, *Black Lamb and Grey Falcon* (Macmillan, 1941), 1946 two-volume printing, DLI scans on archive.org (dli.ernet.12968, in.ernet.dli.2015.12979).
""" % NODE)

body = ["""
Round 14 (second pass on writers and thinkers) searched the open full-text copies on archive.org, mostly Digital Library
of India scans, for what famous pens actually wrote about Atatürk. Six records were staged; the independent check
kept four (Gunther, Nicolson, Coudenhove-Kalergi twice). [[John Dewey]] and [[Rebecca West]] are discussed below but not counted
as gazes: Dewey never names Kemal, and West's line is an aside about his eyes. None of them is a eulogy: the keenest is [[John Gunther]]'s cheerfully
shocked profile of 1936, and the warmest ([[John Dewey]] in 1924) never names Mustafa Kemal.

## John Gunther (1936), 'the roughneck of dictators'

*%s*

> %s

In *Inside Europe*, chapter XXXI, 'The Turkish Colossus', Gunther gives the Gazi seven names, a bronze statue 'in a
dinner-jacket (with the trousers cuffed)', and a character: 'the dictator-type carried to its ultimate extreme, the
embodiment of totalitarian rule by character'. The 1926 hangings, the champagne party and the slap for the fez-wearing
Egyptian minister are all there, and so is the verdict on the work: 'He took a nation that was centuries deep in rot,
pulled it to its feet, wiped its face, re-clothed it, transformed it, made it work.' He insists the credit is shared
('Kamal, alone, it may be said, does not deserve credit for all this') and spends a page on the mother, the illness and
the blue eyes. The comparison is with [[Benito Mussolini]] and [[Adolf Hitler]]. %s Evidence P.

## John Dewey (1924), the new leaders' instincts

*%s*

> %s

Dewey went to Angora by train from Constantinople in 1924 and wrote it up for *The New Republic* (the book says all its articles first appeared there). He
describes the 'astonishment and resentment' at the move of the capital, the plateau 'treeless as far as the eye can
reach', and then: 'After only a few hours in Angora, the mood changes.' Mustafa Kemal is not named; the only trace is a
school named for him and one for his wife. So the Dewey card ([[John Dewey]]) rests, in this text, on the praise of
'the new leaders' and on the line that Constantinople 'seems not old but tired'. %s Evidence P.

## Harold Nicolson (1934), luck made of enemies

*%s*

> %s

[[Lord Curzon]]'s biographer treats Mustafa Kemal as a case rather than a hero. His career 'is typically Young Turk';
what sets it apart is that he was spared the suspicion of the Sultan and the occupying powers because he had quarrelled
with Enver, Talaat, Djemal and Djavid in 1912 and with the German generals in 1917. %s Evidence P.

## Richard Coudenhove-Kalergi (1943), two readings

*%s*

> %s

*%s*

> %s

The founder of the Pan-Europe movement uses Kemal twice in his autobiography: once as the 'great leader' whose Turkey
joined Western civilization on its own initiative and could be a pattern for the 'Mohammedan nations', and once as the
man whose refusal of Sèvres began the counter-revolution against the treaties of Paris (see [[Treaty of Lausanne]]). He
also reports that [[Eleftherios Venizelos]] told him in Vienna that Kemal's Turkey 'had become an integral part of
Western civilization'. %s %s Evidence P.

## Rebecca West (1941), the blue eyes

*%s*

> %s

An aside in *Black Lamb and Grey Falcon*, a book whose real subject is Yugoslavia: King Alexander goes to
Constantinople to see Mustapha Kemal, 'who smiled at him with eyes which revealed that the Balkans had once more played
their trick on the Turk' (see [[Balkan Pact]] and [[Alexander I of Yugoslavia]]). Her other mentions are admiring in
tone, but they are by-the-way. %s Evidence P.

## Not stored, and dry ends (round 14)

- **Emil Ludwig:** the interview of 3 Nov 1929 at Çankaya (printed in the *Neue Freie Presse*, 11 March 1930, and the *Berliner
  Tageblatt*) is retold in Turkish columns (Alev Coşkun, cumhuriyetdaily.com, 10 Nov 2023) with Ludwig's remarks that
  Kemal 'studied important people' and 'was a thinker as well as a man of action'. The original page is on ANNO
  (anno.onb.ac.at), which now answers with a Cloudflare Turnstile check; no bypass was attempted, so the existing card
  [[Emil Ludwig]] remains a lead. A human can pull *NFP* 11 March 1930 p. 1 in a browser.
- **Spengler:** *Jahre der Entscheidung* (1933) and *The Hour of Decision* (1934), both full texts on archive.org, were searched for
  Kemal/Türk: the Japanese victory of 1905 and 'die Türkei' appear as part of the coloured world's awakening, but
  Kemal and Atatürk are not named.
- **John Dos Passos:** *Orient Express* (1927) names 'Mustapha Kemal' only in other people's mouths in 1921 (an American
  businessman's 'Kemal! He's finished... Like hell he is', and Turkish army doctors: 'The Turks are all in Angora with
  Mustapha Kemal'); no stated view of his own.
- **Gertrude Bell:** *Letters*, vol. II, two passing mentions of 'Muftafa Kemal' (1920), no view.
- **Subhas Chandra Bose:** *The Indian Struggle* calls the abolition of the caliphate 'the extraordinary step'; no assessment of Kemal.
- **Orwell, Koestler, Malraux, Pound, Christie, Sheean, Shaw, Yeats, Kazantzakis, Mann, Zweig, Rolland:** one or two
  archive.org full-text queries each (search-inside snippets); no passage with a stated view surfaced. Not exhaustive: the
  search-inside engine is weak on in-copyright books.
- **Nâzım Hikmet:** one paid search (Turkish) found only secondary retellings of the 1921 Ankara meeting; no verse text.
- **Yahya Kemal, Peyami Safa, Hafız İbrahim:** one full-text query each; nothing usable.

## Sources
- John Gunther, *Inside Europe* (Hamish Hamilton, rev. illus. ed. 1938), DLI scan archive.org/details/in.ernet.dli.2015.13600.
- John Dewey, *Impressions of Soviet Russia and the Revolutionary World* (1929), archive.org/details/impressions_of_soviet_russia.
- Harold Nicolson, *Curzon: The Last Phase* (Constable, 1934), archive.org/details/in.ernet.dli.2015.208069.
- R. N. Coudenhove-Kalergi, *Crusade for Pan-Europe* (Putnam, 1943), archive.org/details/dli.ernet.155751.
- Rebecca West, *Black Lamb and Grey Falcon* (Macmillan, 1941), archive.org/details/dli.ernet.12968 and in.ernet.dli.2015.12979.
- Oswald Spengler, *Jahre der Entscheidung* (1933), archive.org/details/OswaldSpenglerJahreDerEntscheidung.
""" % (
    R[0]["saw"], R[0]["q"], R[0]["loc"] + ".",
    R[1]["saw"], R[1]["q"], R[1]["loc"] + ".",
    R[2]["saw"], R[2]["q"], R[2]["loc"] + ".",
    R[3]["saw"], R[3]["q"], R[4]["saw"], R[4]["q"], R[3]["loc"] + ".", R[4]["loc"] + ".",
    R[5]["saw"], R[5]["q"], R[5]["loc"] + ".",
)]

note("Events", NODE,
     {"type": "event", "when": "1924–1943",
      "tags": ["event", "verified", "writers", "intellectuals"]},
     "\n".join(body))
print("ok", len(R), "records")
