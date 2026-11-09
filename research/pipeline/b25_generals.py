# -*- coding: utf-8 -*-
# Census round 16 (Nov 2026) — soldiers on Mustafa Kemal in their own words, read in open archive.org scans.
# Seam: tools/fts.py to locate the books, then open DLI/IA djvu text banked in tools/.state/round16/*.txt for verbatim checks.
# Records: Liman von Sanders (1927), Kannengiesser (1927/28), Prince Andrew of Greece (1930), Liddell Hart (1930),
# Wavell (1940), Harington (1940).
import json, os, re
from _lib import note, person

HERE = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(HERE, "tools", ".state", "round16")
NODE = "Soldiers on Mustafa Kemal in Their Own Words, 1915–1940"

def norm(s):
    for a, b in (("’", "'"), ("‘", "'"), ("“", '"'), ("”", '"'), ("—", "-"), ("¬", ""), ("■", "")):
        s = s.replace(a, b)
    s = re.sub(r"-\s*\n", "", s)
    return re.sub(r"\s+", " ", s).lower()

def bank(n):
    return norm(open(os.path.join(STATE, n), encoding="utf-8").read()).replace("auenby", "allenby")

R = [
 dict(id="liman-von-sanders-1927", voice="Otto Liman von Sanders", role="German general, commander of the Fifth Army at Gallipoli; memoir Five Years in Turkey",
      c="Germany", cn="Germany", dom="military", date="1927", era="posthumous", mirror="chivalrous-enemy", pol="admiring", inten=2,
      saw="Gives the 19th Division commander the Anafarta group in August 1915, trusting his energy, and in October 1918 hands over the Army Group to Kemal.",
      q="I had full confidence in his energy.", art="memoir", ev="P", src="sand.txt",
      cav="Five Years in Turkey (English translation, US Naval Institute, 1927), p. 86 (running head '86 FIVE YEARS IN TURKEY'); open DLI scan in.ernet.dli.2015.24341. Same passage, p. 85: 'Mustapha Kemal, who earned his first military laurels in Cyrenaica, was a leader that delighted in responsibility' (OCR reads 'reponsibility'). His farewell order of 31 Oct 1918 (p. 320) hands over to 'H. E. General Mustapha Kemal' 'proved in many a glorious battle'. The German original is Fünf Jahre Türkei (1920). In the same book Liman says Kemal 'did not want' the Seventh Army command in 1918 and 'did not keep it'. He writes as Kemal's commander and later a defeated ally; no later verdict on the president.",
      urls=["https://archive.org/details/in.ernet.dli.2015.24341"], loc="Liman von Sanders, Five Years in Turkey (1927), pp. 85-86, 320", link="Otto Liman von Sanders",
      nxt="German original (Fünf Jahre Türkei, 1920) for the same passage"),
 dict(id="kannengiesser-1927", voice="Hans Kannengiesser", role="German officer, commander of the Turkish 5th Division at Gallipoli; memoir The Campaign in Gallipoli",
      c="Germany", cn="Germany", dom="military", date="1927", era="posthumous", mirror="chivalrous-enemy", pol="admiring", inten=2,
      saw="Recalls Kemal at Gallipoli as a clear-thinking, quiet, self-reliant commander who knew what he wanted; now 'world-famous President of Turkey'.",
      q="The impression that I gained of him during this period was that of a clear-thinking, active, quiet man who knew what he wanted.",
      art="memoir", ev="P", src="kann.txt",
      cav="The Campaign in Gallipoli (Hutchinson, English edition 1928; German Gallipoli, der Wendepunkt des Weltkrieges, 1927), p. 126 (running head '126 THE CAMPAIGN IN GALLIPOLI'); open scan campaigngallipolikannengiesser. The same passage: 'Mustapha Kemal Bey is the now world-famous President of Turkey'; 'He weighed and decided everything for himself, without looking elsewhere for support or agreement'; 'He did not appear to be very strong bodily, although extremely wiry'. A plate in the book is captioned 'Mustapha Kemal Bey, now Pasha and President of the Turkish Republic'. On p. 222 Kannengiesser records the hanging of Djavid Bey 'for rebelling against the government of Mustapha Kemal Pasha' (a fact, no judgement). He had come to take over the 5th Division and agreed that Kemal should conduct the action over the whole front. Neutral voice kept.",
      urls=["https://archive.org/details/campaigngallipolikannengiesser"], loc="Kannengiesser, The Campaign in Gallipoli (1928), p. 126", link="Gallipoli Campaign",
      nxt=""),
 dict(id="prince-andrew-of-greece-1930", voice="Prince Andrew of Greece", role="Greek Army corps commander in Asia Minor 1921; author of Towards Disaster",
      c="Greece", cn="Greece", dom="military", date="1930", era="posthumous", mirror="chivalrous-enemy", pol="admiring", inten=1,
      saw="Says the Greek advance of 1921 might have destroyed the Turkish army but for commanders of 'great military capacity', Kemal and Ismet.",
      q="if it had not been commanded by leaders of great military capacity as Mustapha Kemal Pasha and Ismet Pasha.",
      art="memoir", ev="P", src="and.txt",
      cav="Towards Disaster: The Greek Army in Asia Minor in 1921 (John Murray, 1930), p. 33 (running head 'A NATURALLY STRONG LINE 33'); open scan towardsdisastergreekarmy1921. The quote ends the sentence; the complete clause is 'might almost have caused the destruction of the Turkish Army, if it had not been commanded by leaders of great military capacity as Mustapha Kemal Pasha and Ismet Pasha'. On p. 173 he reports that Turkish officers said Kemal had been 'in the lines' two days earlier 'encouraging and urging his men to a last desperate fight' (a report, no judgement). The book argues the Greek disaster was caused by the Greek command's own decisions, not by the enemy; the voice here is that of a defeated officer on his opponents. Used with neutral voice; Sakarya and Asia Minor are sensitive ground.",
      urls=["https://archive.org/details/towardsdisastergreekarmy1921"], loc="Prince Andrew of Greece, Towards Disaster (1930), p. 33 (also p. 173)", link="Greco-Turkish War",
      nxt=""),
 dict(id="liddell-hart-1930", voice="B. H. Liddell Hart", role="British military historian and strategist; The Real War 1914-1918",
      c="United Kingdom", cn="United Kingdom", dom="military", date="1930", era="posthumous", mirror="chivalrous-enemy", pol="admiring", inten=1,
      saw="Counts Kemal, with Liman von Sanders, among the 'able commanders' Allenby had to outwit in 1918; at Anzac, the 'then unknown' officer.",
      q="in 1918 Allenby had to outwit such able commanders as Liman von Sanders and Mustapha Kemal",
      art="book", ev="P", src="rw.txt",
      cav="The Real War 1914-1918 (Faber, 1930), p. 468 (footer '467' precedes the head 'ANNIHILATION OF THE TURKISH ARMIES'; the book's index gives Megiddo 470 ff.); open DLI scan in.ernet.dli.2015.57906. In the Gallipoli chapter, p. 184: 'the initiative of one opponent, the then unknown Mustapha Kemal, contributed to its unfulfilment' (of the Anzac landing's opportunity). A short remark inside a military history: the record is intensity 1. The existing person note on Liddell Hart already carries a general characterisation without a cited page; this record is the sourced one.",
      urls=["https://archive.org/details/in.ernet.dli.2015.57906"], loc="Liddell Hart, The Real War (1930), pp. 184, 468", link="B.H. Liddell Hart",
      nxt="History of the Second World War / Memoirs and his Fuller correspondence for any later Atatürk remark"),
 dict(id="wavell-1940", voice="Archibald Wavell", role="British field marshal; Allenby: A Study in Greatness (1940)",
      c="United Kingdom", cn="United Kingdom", dom="military", date="1940", era="posthumous", mirror="chivalrous-enemy", pol="admiring", inten=2,
      saw="Calls Kemal one of 'two of the best Turkish commanders' of 1918 and a leader who 'was later to rally and reorganize all Turkey'.",
      q="the future Ataturk, who was to regenerate the Turkish nation", art="book", ev="P", src="wav.txt",
      cav="Allenby: Soldier and Statesman (Harrap, 1946 edition of the 1940 Allenby: A Study in Greatness), p. 236 (index: 'Kemal, Mustapha, Ataturk, 171, 236 and n. 1, 245'); open DLI scan in.ernet.dli.2015.505341. Also p. 245: 'two of the best Turkish commanders, Mustapha Kemal, of the Seventh Army, and Jemal Pasha, of the Fourth'; Aleppo 'rallied and reorganized by no less a leader than Mustapha Kemal Pasha, who was later to rally and reorganize all Turkey'. P. 171: Kemal 'declined to serve under a German staff'. Pagination is the 1946 edition; the 1941 edition (allenbystudyingr0000arch, search-inside) has the same sentences. In Allenby in Egypt (1943), Wavell says Zaghlul 'may have dreamed of a dictatorship like that of Mustapha Kemal' and that the Greeks were 'completely routed by Mustapha Kemal' (context only).",
      urls=["https://archive.org/details/in.ernet.dli.2015.505341"], loc="Wavell, Allenby: Soldier and Statesman, pp. 171, 236, 245", link="Turkish War of Independence",
      nxt="Page numbers in the 1940 first edition"),
 dict(id="harington-1940", voice="Charles Harington", role="British general, commander of Allied forces at Constantinople 1920-23; memoir Tim Harington Looks Back",
      c="United Kingdom", cn="United Kingdom", dom="military", date="1940", era="posthumous", mirror="chivalrous-enemy", pol="conflicted", inten=2,
      saw="Calls Kemal 'a real soldier' who stopped the Greeks on the Sakarya and 'saw his chance' at Afyon; says Allied arms stocks fed his army.",
      q="This must have rejoiced the heart of Mustapha Kemal, a real soldier, who held them up quite definitely on the River Sakaria.",
      art="memoir", ev="P", src="har.txt",
      cav="Tim Harington Looks Back (John Murray, 1940), p. 107 (running heads '107', '109'); open DLI scan in.ernet.dli.2015.176573. P. 109: 'With the Greeks weakened by their detachment in Eastern Thrace, Mustapha Kemal saw his chance and seized it. He struck a bit of the line near Afium Karahissar'. Elsewhere the Chanak commander says that the arms the Allies stored after 1918 were released to the Turks and 'formed the nucleus of the army which Mustapha Kemal built up', and that Kemal 'sent some very difficult men to Constantinople'. He prints Kemal's and Ismet's letters after the Mudania agreement (c. p. 150). Conflicted rather than admiring: professional respect with the grievance of the Chanak commander. Neutral voice on Chanak.",
      urls=["https://archive.org/details/in.ernet.dli.2015.176573"], loc="Harington, Tim Harington Looks Back (1940), pp. 107, 109", link="Chanak Crisis",
      nxt="Page of 'nucleus of the army' passage (c. p. 186)"),
]

for r in R:
    assert len(r["saw"].split()) <= 25, (r["id"], len(r["saw"].split()))
    assert norm(r["q"]).rstrip(".") in bank(r["src"]), r["id"]
    print("quote verified:", r["id"])

with open(os.path.join(STATE, "gazes_generals.jsonl"), "w", encoding="utf-8") as f:
    for r in R:
        rec = {"id": r["id"], "voice": r["voice"], "voice_type": "person", "role": r["role"], "country": r["c"],
               "country_now": r["cn"], "domain": r["dom"], "date": r["date"], "era": r["era"], "mirror": r["mirror"],
               "polarity": r["pol"], "intensity": r["inten"], "what_they_saw": r["saw"], "quote": r["q"],
               "artifact": r["art"], "evidence": r["ev"], "mediated_by": None, "caveat": r["cav"],
               "node": NODE, "sources": r["urls"]}
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")

with open(os.path.join(STATE, "ledger_generals.md"), "w", encoding="utf-8") as f:
    f.write("| Claim | Node | Status | Sources | Next step |\n|---|---|---|---|---|\n")
    for r in R:
        qs = r["q"]
        f.write("| %s (%s, %s): \"%s\" | %s | verified %s (%s) | %s | %s |\n" % (
            r["voice"], r["role"][:50], r["date"], qs[:110].replace("|", "/") + ("..." if len(qs) > 110 else ""),
            NODE, r["ev"], r["loc"], r["urls"][0], r["nxt"] or "none"))

new_people = {
 "Hans Kannengiesser": ("German officer, commander of the Turkish 5th Division at Gallipoli", "German", "1875–1945", "respectful comrade",
    "He took over the 5th Division at Gallipoli in August 1915 and remembered Kemal there as 'a clear-thinking, active, quiet man who knew what he wanted'."),
 "Charles Harington": ("British general, Allied commander at Constantinople 1920–1923", "British", "1872–1940", "professional respect with a grievance",
    "He called Kemal 'a real soldier' who held the Greeks on the Sakarya, and thought the Allies' own stored arms formed the nucleus of his army."),
 "Archibald Wavell": ("British field marshal and biographer of Allenby", "British", "1883–1950", "chivalrous opponent's biographer",
    "In his Allenby biography (1940) he names Kemal among the two best Turkish commanders of 1918 and the leader 'who was to regenerate the Turkish nation'."),
 "Prince Andrew of Greece": ("Greek general, author of Towards Disaster", "Greek", "1882–1944", "respect for an opponent",
    "Writing of 1921, he says the Turkish army was commanded by 'leaders of great military capacity' like Kemal and Ismet."),
}
for name, (role, nat, life, stance, desc) in new_people.items():
    if os.path.exists(os.path.join(HERE, "vault", "People", name + ".md")):
        continue
    person(name, role=role, nat=nat, life=life, stance=stance, tags=["verified", "military"],
           body="%s See [[%s]] for the quote and sources.\n\n## Sources\n- See [[%s]].\n" % (desc, NODE, NODE))

body = ["""
Round 16 looked for soldiers who fought with or against Mustafa Kemal, or studied him later, in the open scans of their
memoirs on archive.org (the full-text search found the books; the open text was then read for the exact passage and page).
Six records. They are short, and all six are respectful: no soldier in the open texts calls him anything but capable.

## The pattern

- **The commander above him:** [[Otto Liman von Sanders]] (1927) trusted the 19th Division's commander with the Anafarta group
  ('I had full confidence in his energy') and in October 1918 handed over the whole Army Group to him. [[Hans Kannengiesser]]
  (1927) was alongside him on the peninsula and remembered a quiet, self-reliant officer who 'weighed and decided everything for himself'.
- **The opposing army, 1921-22:** [[Prince Andrew of Greece]] (1930) writes of the Greek advance that the Turks owed their survival
  to commanders of 'great military capacity', Kemal and Ismet; [[Charles Harington]] (1940), the Allied commander at Constantinople,
  calls him 'a real soldier' who held the Greeks on the Sakarya and 'saw his chance' at Afyon, but also says that arms the Allies
  had stored fed his army. This is the only conflicted voice of the six.
- **The historians of the war:** [[B.H. Liddell Hart]] (1930) puts Kemal with Liman von Sanders among the 'able commanders' Allenby
  had to outwit; [[Archibald Wavell]] (1940), Allenby's biographer, names him among 'two of the best Turkish commanders' of 1918 and
  the future Atatürk 'who was to regenerate the Turkish nation'.
"""]
for r in R:
    body.append("\n## %s (%s)\n" % (r["voice"], r["date"]))
    body.append("*%s*\n" % r["saw"])
    body.append("> %s\n" % r["q"])
    body.append("%s Location: %s. Evidence %s. See [[%s]].\n" % (r["cav"], r["loc"], r["ev"], r["link"]))

body.append("""
## Dry ends (round 16)

- **Ian Hamilton, *Gallipoli Diary* (1920):** the open Gutenberg text (vols 1-2) never names Kemal. Falkenhayn, *General Headquarters 1914-1916*: no mention of Kemal in the open scan.
- **Aspinall-Oglander, *Military Operations: Gallipoli* vol. 1:** names Mustafa Kemal as the 19th Division's commander ('the future President') but states no view in the open volume; vol. 2 is lending-only.
- **Carl Mühlmann, *Der Kampf um die Dardanellen* (1927):** calls him 'der jetzige Gebieter der Türkei' in passing; narrative, no stated view.
- **T. E. Lawrence, *Seven Pillars* (1922 text, pp. 571-573):** Kemal appears as the Turkish staff officer to whom Feisal's propaganda was aimed ('too keen on the Turkishness of their mission'), who 'begged Feisal not to play into Jemal's hands'; Lawrence reports his plans and states no judgement of him. Not stored.
- **Townshend, *My Campaign in Mesopotamia* (1920), Kress von Kressenstein, Ludendorff, Monash, Keith Murdoch, Mannerheim:** no hit in the archive.org full-text search under author for Kemal. **Montgomery, *A Concise History of Warfare* (1972):** two index entries (pp. 299, 306) for Kemal; lending-only, snippet shows only 'distinguished himself in repelling the Australians'; not stored. **J. F. C. Fuller, *Military History of the Western World* (1956):** narrates Anafarta, no stated view in the snippets. Rommel, Patton, Hammerstein, Frunze: not found. Aralov (Russian): the one search returned nothing under his name.
- **Not reached:** Aralov's *Воспоминания советского дипломата* (Russian print, not on archive.org full text), Frunze's Ankara report (Russian archive), Papoulas and Stratigos (Greek), Monash's letters, Allenby's own despatches.

## Sources
- archive.org open scans; the identifier of each is given in the record above.
""")
note("Events", NODE, {"type": "event", "when": "1915–1940", "tags": ["event", "verified", "military", "memoirs"]}, "\n".join(body))
print("ok", len(R), "records")
