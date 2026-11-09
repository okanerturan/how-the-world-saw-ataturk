# -*- coding: utf-8 -*-
# Census round 22 (Nov 2026) — US Congressmen on Atatürk in the Congressional Record (GovInfo, free).
# Banks in tools/.state/round22/congress/: HTML granules (CREC, 1994+) and pdftotext of the bound-edition granule PDFs (CRECB, 1873–1998).
# The script refuses to run if a quote is not found in its bank. Bound-edition scans are two-column OCR, so for those
# the check is a word-subsequence match inside a window after the anchor (columns interleave in the text layer).
import json, os, re, sys, html
from _lib import note, person

HERE = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(HERE, "tools", ".state", "round22")
BANK = os.path.join(STATE, "congress")

NODE = "Congressional Record Pens on Atatürk — Connally, Pepper, Levin, Moynihan, Byrd, Lantos and Others"


def words(s):
    s = html.unescape(s)
    s = s.replace("``", '"').replace("''", '"').replace("’", "'").replace("“", '"').replace("”", '"')
    return re.findall(r"[A-Za-z0-9]+", s.lower())


OCRFIX = {"like\u00b7uhood": "likelihood", "sin~e": "since", "TUrkey": "Turkey"}


def read_bank(fn):
    t = open(os.path.join(BANK, fn), encoding="utf-8", errors="ignore").read()
    m = re.search(r"<pre>(.*?)</pre>", t, re.S)
    if m:
        t = html.unescape(m.group(1))
    t = re.sub(r"-\n\s*", "", t)
    for a, b in OCRFIX.items():
        t = t.replace(a, b)
    return t


def check(fn, anchor, quote, window=4500):
    """HTML (daily edition): the quote's words must run contiguously. Bound-edition scans (two-column OCR, columns interleave
    line by line): every quote word must occur in the window around the anchor and >= 75% of the quote's word pairs must occur adjacent."""
    t1 = re.sub(r"\s+", " ", read_bank(fn))
    ws = words(quote)
    if fn.endswith(".htm"):
        return " ".join(ws) in " ".join(words(t1))
    pairs = set(zip(ws, ws[1:]))
    for m in re.finditer(anchor, t1):
        seg = words(t1[max(0, m.start() - window): m.start() + window])
        have = set(seg)
        spairs = set(zip(seg, seg[1:]))
        miss = [w for w in set(ws) if w not in have]
        if len(miss) <= 2 and len(pairs & spairs) >= 0.75 * len(pairs):
            return True
    return False


CITE_B = "Congressional Record (bound edition)"
GOV = "https://www.govinfo.gov/content/pkg/"


def url_b(pkg, g):
    return "%s%s/pdf/%s.pdf" % (GOV, pkg, g)


def url_c(day, g):
    return "%sCREC-%s/html/%s.htm" % (GOV, day, g)


US = dict(c="United States", cn="United States", dom="politics", ar="speech", ev="P")

R = [
 dict(id="cox-1937-06", voice="Eugene E. Cox", role="U.S. Representative from Georgia", date="1937-06-30", era="contemporary", mirror=None, pol="hostile", inten=1,
      cite="House of Representatives, 30 June 1937, Congressional Record vol. 81 (bound), p. 6637 (granule CRECB-1937-pt6-v81-8-1)",
      saw="Names labour 'in Turkey under Kemal Pasha' with labour under Mussolini, Hitler and Stalin as the warning for America under a union 'czar'.",
      q="I have but to look at labor in Turkey under Kemal Pasha, to learn what will be the plight of labor in America under the despotism of John L. Lewis or any other man who attains to the stature of a labor czar.",
      bank="CRECB-1937-pt6-v81-8-1.txt", anchor="labor in Turkey under Kemal Pasha",
      url=url_b("GPO-CRECB-1937-pt6-v81", "GPO-CRECB-1937-pt6-v81-8-1"),
      cav="A one-clause example in an anti-CIO speech ('Mr. COX. Mr. Speaker, several days ago the House very kindly granted me 1 hour'); Kemal is lined up with the dictators as a labour despot. No more is said about him. Page from the OCR running head; scan OCR."),
 dict(id="reynolds-1939-04", voice="Robert R. Reynolds", role="U.S. Senator from North Carolina", date="1939-04-13", era="contemporary", mirror=None, pol="admiring", inten=1,
      cite="Senate, 13 April 1939, Congressional Record vol. 84 (bound), pp. ~4219-4222 (granule CRECB-1939-pt4-v84-12-1)",
      saw="In an aside on Mussolini's seizure of Albania, calls Atatürk 'that great man' who did more for Turkey than any other since its founding.",
      q="that great man Ataturk who did more for Turkey than any other man since Turkey was established as a nation, happened to be born in Salonika.",
      bank="CRECB-1939-pt4-v84-12-1.txt", anchor="that great man Ataturk",
      url=url_b("GPO-CRECB-1939-pt4-v84", "GPO-CRECB-1939-pt4-v84-12-1"),
      cav="Speaker identified from the transcript sequence ('Mr. REYNOLDS obtained the floor'); the two-column scan OCR interleaves with other speakers' lines, and the OCR reads 'sin~e' for 'since' (corrected). An aside, not the topic of the speech (Albania, Salonika, the European crisis)."),
 dict(id="connally-1942-10", voice="Tom Connally", role="U.S. Senator (Democrat, Texas); chairman of the Foreign Relations Committee", date="1942-10-29", era="posthumous", mirror="modernization-poster-child", pol="admiring", inten=2,
      cite="Senate, 29 October 1942, Congressional Record vol. 88 (bound), pp. ~8679-8680 (granule CRECB-1942-pt7-8-1)",
      saw="Marks the Republic's 19th anniversary: 'the late great Kemal Ataturk', whose reforms rested on four foundations, none dependent on one man's life.",
      q="The reforms and projects of Kemal Ataturk stood upon four square national foundations: peace, prosperity, honor, and strength. These foundations are not dependent upon one man's life or popularity for their execution.",
      bank="CRECB-1942-pt7-8-1.txt", anchor="four square national foundations",
      url=url_b("GPO-CRECB-1942-pt7", "GPO-CRECB-1942-pt7-8-1"),
      cav="A formal felicitation to Turkey read with unanimous consent ('I feel certain that I am voicing the wishes of the United States Senate'), delivered in wartime when Turkey's neutrality was under Allied pressure; courtesy as well as view. Party, state and committee chairmanship are from the standard biographical record, not from the passage."),
 dict(id="davis-1943-04", voice="James J. Davis", role="U.S. Senator (Pennsylvania)", date="1943-04-22", era="posthumous", mirror="modernization-poster-child", pol="admiring", inten=2,
      cite="Senate, 22 April 1943, Congressional Record vol. 89 (bound), p. ~3693 (granule CRECB-1943-pt3-15-1)",
      saw="Marks the National Assembly's 24th anniversary: Atatürk's leadership brought a 'veritable social revolution' with no fascist badges or mass hysteria.",
      q="Twenty-four years ago today, representatives from nearly every part of Turkey came to Ankara at the invitation of the late great Turkish leader, Kemal Ataturk, and laid the foundations of a new Turkey",
      bank="CRECB-1943-pt3-15-1.txt", anchor="late great Turkish leader",
      url=url_b("GPO-CRECB-1943-pt3", "GPO-CRECB-1943-pt3-15-1"),
      cav="Heading 'Twenty-fourth anniversary of foundation of the Turkish National Assembly'; the same speech quotes Wendell Willkie's *One World* on Turkey (not counted). Senator's state from the standard record (only one Senator Davis served in 1943), not from the passage."),
 dict(id="pepper-1947-04", voice="Claude Pepper", role="U.S. Senator from Florida (Democrat), opponent of the Greek-Turkish aid bill", date="1947-04-17", era="posthumous", mirror=None, pol="instrumental", inten=2,
      cite="Senate, 17 April 1947, Congressional Record vol. 93 (bound), pp. ~3593-3596 (granule CRECB-1947-pt3-13-1)",
      saw="Cites Atatürk's record to argue communism has no foothold in Turkey, and credits him with building a strong army and government.",
      q="Anyone who has ever heard of Ataturk and his party and his government, which is now carried on by his chosen successor, President Inonu, knows that there is not any likelihood of communism getting a foothold in Turkey.",
      q2="Finally Ataturk took advantage of the strife which existed in Europe and developed a strong army and a strong government in Turkey",
      bank="CRECB-1947-pt3-13-1.txt", anchor="heard of Ataturk", anchor2="Finally Ataturk",
      url=url_b("GPO-CRECB-1947-pt3", "GPO-CRECB-1947-pt3-13-1"),
      cav="Truman Doctrine debate: Pepper argues against the bill, so Atatürk is used as evidence for his case (no communist threat; the Dardanelles question). The OCR reads 'like·uhood' for 'likelihood' (corrected); the second quote is rebuilt from the interleaved two-column text layer (the source reads 'de- veloped', 'gov- ernment')."),
 dict(id="pepper-1950-12", voice="Claude Pepper", role="U.S. Senator from Florida (Democrat), reporting on a trip abroad", date="1950-12-22", era="posthumous", mirror="modernization-poster-child", pol="admiring", inten=1,
      cite="Senate, 22 December 1950, Congressional Record vol. 96 (bound), p. ~16974 (granule CRECB-1950-pt12-20-1)",
      saw="Reporting on a trip, says the 'new Turkey oriented to the West' rests on the 'splendid edifice' Kemal Pasha built after the First World War.",
      q="There is a new Turkey oriented to the West which has risen upon the splendid edifice established by Kemal Pasha after World War I.",
      bank="CRECB-1950-pt12-20-1.txt", anchor="Kemal Pasha",
      url=url_b("GPO-CRECB-1950-pt12", "GPO-CRECB-1950-pt12-20-1"),
      cav="A one-sentence aside in a long report on Greece, Turkey and Israel; page from the OCR running heads (the scan interleaves columns). The speaker is read from the transcript sequence (Pepper in colloquy with Brewster)."),
 dict(id="lehman-1955-05", voice="Herbert H. Lehman", role="U.S. Senator from New York (Democrat)", date="1955-05-22", era="posthumous", mirror=None, pol="hostile", inten=1,
      cite="Senate, 31 May 1955, Congressional Record vol. 101 (bound), pp. ~7231-7237 (granule CRECB-1955-pt6-3-1); address delivered 22 May 1955 at Town Hall, New York, printed at his request",
      saw="In an Armenian Independence Day address, names 'the Turkey of Kemal Pasha' and Lenin's Russia as joined in the conspiracy that destroyed the Armenian Republic.",
      q="But no armies marched and no ships of war sailed to the rescue when the Turkey of Kemal Pasha and the Russia of Lenin and Trotsky joined, despite formal agreement and covenants to the contrary, in a dread conspiracy to destroy the Armenian Republic.",
      bank="CRECB-1955-pt6-3-1.txt", anchor="Kemal Pasha",
      url=url_b("GPO-CRECB-1955-pt6", "GPO-CRECB-1955-pt6-3-1"),
      cav="Sensitive thread (the Armenian question): this is the speaker's framing of the 1920 war against the first Armenian Republic, not the vault's. His own address, inserted in the Record at his request ('I ask unanimous consent that my remarks on that occasion be printed'); delivered at a rally and printed nine days later, so the date is the address date. He does not discuss Atatürk beyond this name."),
 dict(id="saylor-1956-05", voice="John P. Saylor", role="U.S. Representative from Pennsylvania (coal district)", date="1956-05-07", era="posthumous", mirror=None, pol="instrumental", inten=2,
      cite="Extensions of Remarks, 7 May 1956, Congressional Record vol. 102 (bound), p. ~7669 (granule CRECB-1956-pt6-6-3)",
      saw="Offers Mustafa Kemal as a model for coal-state members of Congress: a 'fervent patriot' banished for his views who later became Ataturk and President.",
      q="He was a fervent patriot who as a youth learned that his political views were not acceptable to incumbent government leaders; in fact, he was at one time banished to Damascus for publicly expressing his views.",
      bank="CRECB-1956-pt6-6-3.txt", anchor="Mustafa Kemal",
      url=url_b("GPO-CRECB-1956-pt6", "GPO-CRECB-1956-pt6-6-3"),
      cav="From an address to the American Mining Congress (Cincinnati) printed in the Extensions of Remarks; an analogy for the coal industry's lobbying ('we took somewhat the same course of action that Mustafa Kemal followed'), so Atatürk is a vehicle for the speaker's point. Two-column OCR; quote rebuilt from the interleaved lines."),
 dict(id="levin-1994-04", voice="Carl Levin", role="U.S. Senator from Michigan (Democrat)", date="1994-04-19", era="posthumous", mirror=None, pol="instrumental", inten=2,
      cite="Senate, 19 April 1994, 'The Genocide of Armenians', Congressional Record vol. 140, no. 43, p. S38 (granule CREC-1994-04-19-pt1-PgS38)",
      saw="In an Armenian genocide commemoration, cites Atatürk as having recognised the crimes, quoting a 1926 interview he says Atatürk gave.",
      q="Indeed, the founder of modern Turkey, Kemal Ataturk, recognized the crimes committed by the Ottoman Empire. As I've discussed on this floor before, in a 1926 interview Ataturk himself stated that those responsible \"should have been made to account for the lives of millions of our Chistian subjects who were ruthlessly driven en masse from their homes and massacred.\"",
      bank="CREC-1994-04-19-pt1-PgS38.htm", anchor="founder of modern Turkey, Kemal Ataturk",
      url=url_c("1994-04-19", "CREC-1994-04-19-pt1-PgS38"),
      cav="Sensitive thread (the Armenian genocide): the Senator's framing and his attribution, which the vault does not endorse or test here; the 1926 interview is his citation ('Chistian' is the Record's misprint). He uses Atatürk to separate present-day Turkey from the Ottoman crimes."),
 dict(id="moynihan-1999-10", voice="Daniel Patrick Moynihan", role="U.S. Senator from New York (Democrat)", date="1999-10-18", era="posthumous", mirror="modernization-poster-child", pol="admiring", inten=1,
      cite="Senate, 18 October 1999, introduction of S. 1746 (U.S.-Turkey Free Trade Agreement Act of 1999), Congressional Record vol. 145, no. 141, p. S12786 (granule CREC-1999-10-18-pt1-PgS12786)",
      saw="Opens a Turkey free-trade bill with Atatürk as 'legendary': he built a western-oriented, secular state from the ruins of the Ottoman Empire.",
      q="Turkey has played a singular role at the crossroads of East and West since 1923, when the legendary Mustafa Kemal \"Ataturk\" built a western-oriented, secular state out of the ashes of the collapsed 600-year old Ottoman Empire.",
      bank="CREC-1999-10-18-pt1-PgS12786.htm", anchor="legendary Mustafa Kemal",
      url=url_c("1999-10-18", "CREC-1999-10-18-pt1-PgS12786"),
      cav="Introductory framing of a trade bill (the bill's purpose was to open talks on a Turkey FTA), so the praise sets the case for the bill."),
 dict(id="lautenberg-2003-11", voice="Frank R. Lautenberg", role="U.S. Senator from New Jersey (Democrat)", date="2003-11-25", era="posthumous", mirror="modernization-poster-child", pol="admiring", inten=1,
      cite="Senate, 25 November 2003, S. Res. 273 (condemning the Istanbul bombings), Congressional Record vol. 149, p. S16044 (granule CREC-2003-11-25-pt1-PgS16044-3)",
      saw="After the Istanbul bombings, says that since Atatürk founded modern Turkey it has been admired worldwide as a progressive Muslim democracy.",
      q="Since Mustafa Kemal Ataturk founded modern Turkey in 1923, Turkey has been admired by western and non-western countries alike as an apotheosis of progressive Muslim democracy.",
      bank="CREC-2003-11-25-pt1-PgS16044-3.htm", anchor="Mustafa Kemal Ataturk founded modern Turkey",
      url=url_c("2003-11-25", "CREC-2003-11-25-pt1-PgS16044-3"),
      cav="Spoken in a resolution of condolence and solidarity after the 15 and 20 November 2003 attacks; the sentence is about Turkey's reputation more than about the man (hence intensity 1). Mitch McConnell moved the resolution but his words in the same entry are procedural."),
 dict(id="lantos-2005-09", voice="Tom Lantos", role="U.S. Representative from California (Democrat), ranking member of the House International Relations Committee", date="2005-09-27", era="posthumous", mirror="modernization-poster-child", pol="instrumental", inten=1,
      cite="Extensions of Remarks, 27 September 2005, 'Speech of Pakistani President Pervez Musharraf...', Congressional Record vol. 151, p. E1958 (granule CREC-2005-09-27-pt1-PgE1958)",
      saw="Says he urged Musharraf to follow 'the great modernizer' Atatürk, and that Atatürk would admire Musharraf's path.",
      q="I urged him to follow the example of the great modernizer Mustafa Kemal Ataturk, the founder of the modern, secular Republic of Turkey, a nation with which President Musharraf is intimately familiar. He has, in fact, blazed a trail that I believe Ataturk himself would admire.",
      bank="CREC-2005-09-27-pt1-PgE1958.htm", anchor="great modernizer Mustafa Kemal Ataturk",
      url=url_c("2005-09-27", "CREC-2005-09-27-pt1-PgE1958"),
      cav="Lantos's own introduction to Musharraf's speech to the American Jewish Congress; Atatürk is the standard he held up to a Muslim head of state, which makes the praise partly diplomatic. Party, committee role and state are from the standard record, not from the passage."),
 dict(id="lantos-2006-05", voice="Tom Lantos", role="U.S. Representative from California (Democrat)", date="2006-05-19", era="posthumous", mirror="secular-rationalist-prophet", pol="admiring", inten=2,
      cite="Extensions of Remarks, 19 May 2006, '125th Anniversary of Birth of Kemal Ataturk, Founder of Modern Turkey', Congressional Record vol. 152, no. 63, p. E917 (granule CREC-2006-05-19-pt1-PgE917-2)",
      saw="Honours Atatürk on his 125th birth anniversary as the revolutionary who showed Islam and modernity are compatible, an example 'for our own era'.",
      q="I rise today, May 19, to commemorate the 125th anniversary of the birth of the founder of modern Turkey, Mustafa Kemal Ataturk, a post-World War I revolutionary leader who demonstrated that Islam and modernity are fully compatible. His example provides instruction and hope for our own era.",
      bank="CREC-2006-05-19-pt1-PgE917-2.htm", anchor="125th anniversary of the birth",
      url=url_c("2006-05-19", "CREC-2006-05-19-pt1-PgE917-2"),
      cav="A full commemorative statement (alphabet reform, 'his leadership style', secularism) in the Extensions of Remarks; it also quotes Atatürk's own words. Delivered in the period of Lantos's active support for the Turkey-US relationship and while he also backed Armenian-genocide recognition, which this statement does not mention."),
 dict(id="byrd-2007-10", voice="Robert C. Byrd", role="U.S. Senator from West Virginia (Democrat), President pro tempore emeritus", date="2007-10-29", era="posthumous", mirror="modernization-poster-child", pol="admiring", inten=2,
      cite="Senate, 29 October 2007, S. Res. 358 (friendship between the United States and Turkey), Congressional Record vol. 153, p. S13524 (granule CREC-2007-10-29-pt1-PgS13524)",
      saw="On Republic Day, describes Mustafa Kemal, later Atatürk, as a war hero who rejected the outdated modes of empire and chose reform and modernisation.",
      q="Kemal, who was later given the name Ataturk, meaning \"father of the Turks,\" rejected the crumbling structures and outdated modes of empire and embraced instead a platform of reform and modernization, a legacy that continues in Turkey to this day and to this hour.",
      bank="CREC-2007-10-29-pt1-PgS13524.htm", anchor="who was later given the name Ataturk",
      url=url_c("2007-10-29", "CREC-2007-10-29-pt1-PgS13524"),
      cav="Cosponsor's statement on the 84th anniversary of the Republic, in the week the House was debating an Armenian genocide resolution; the vault does not read a link into the statement. Title and state are from the standard record."),
 dict(id="gohmert-2014-01", voice="Louie Gohmert", role="U.S. Representative from Texas (Republican)", date="2014-01-15", era="posthumous", mirror="secular-rationalist-prophet", pol="admiring", inten=1,
      cite="House of Representatives, 15 January 2014, 'Conflict in the Middle East', Congressional Record vol. 160, p. H468 (granule CREC-2014-01-15-pt1-PgH468); the same theme in his 7 January 2014 floor speech (p. H9)",
      saw="Argues, on Egypt's constitution, that Atatürk defeated radical Islam in Turkey and that Turkey rose because of it.",
      q="this is something that Ataturk fought against and was able to overcome in Turkey so many decades ago. And because he was able to overcome and overwhelm radical Islam in Turkey, Turkey has surged to the forefront over the past decades in all kinds of areas.",
      bank="CREC-2014-01-15-pt1-PgH468.htm", anchor="Ataturk fought against",
      url=url_c("2014-01-15", "CREC-2014-01-15-pt1-PgH468"),
      cav="A floor aside in a special-order speech about the Egyptian referendum; Atatürk is used as proof for Gohmert's argument about the Muslim Brotherhood and the Egyptian constitution. On 7 January (p. H9) he says Atatürk 'overran radical Islam' and Turkey 'bloomed'."),
]
R = [r for r in R if r['id'] not in {'cox-1937-06','lehman-1955-05','lautenberg-2003-11'}]  # dropped at the independent check (no stated view of Atatürk)

bad = []
for r in R:
    for k, a in (("q", "anchor"), ("q2", "anchor2")):
        if r.get(k):
            parts = r[k]
            if not check(r["bank"], r[a], parts):
                bad.append((r["id"], k))
if bad:
    sys.exit("quote not found in source bank: %s" % bad)
for r in R:
    assert len(r["saw"].split()) <= 25, (r["id"], len(r["saw"].split()))

for r in R:
    r["src"] = r["url"]

with open(os.path.join(STATE, "gazes_congress.jsonl"), "w", encoding="utf-8") as f:
    for r in R:
        q = r["q"] + ((" … " + r["q2"]) if r.get("q2") else "")
        rec = {"id": r["id"], "voice": r["voice"], "voice_type": "person", "role": r["role"],
               "country": "United States", "country_now": "United States", "domain": "politics", "date": r["date"], "era": r["era"],
               "mirror": r["mirror"], "polarity": r["pol"], "intensity": r["inten"], "what_they_saw": r["saw"],
               "quote": q, "artifact": "speech", "evidence": "P", "mediated_by": None,
               "caveat": r["cav"] + " Cited as " + r["cite"] + ".", "node": NODE, "sources": [r["src"]]}
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")

with open(os.path.join(STATE, "ledger_congress.md"), "w", encoding="utf-8") as f:
    f.write("| Claim | Node | Status | Sources | Next step |\n|---|---|---|---|---|\n")
    for r in R:
        f.write("| %s (%s): %s | %s | verified P (Congressional Record, GovInfo %s; text read) | %s | page number from the printed volume / check on loc.gov |\n" % (
            r["voice"], r["date"], r["saw"], NODE, "bound-edition PDF text layer" if "CRECB" in r["bank"] else "daily-edition HTML", r["src"]))

# one person note per voice
voices = {}
for r in R:
    voices.setdefault(r["voice"], []).append(r)
PEOPLE_TAGS = ["verified", "us-congress", "congressional-record"]
for v, rs in voices.items():
    stance = "; ".join("%s (%s)" % (x["pol"], x["date"][:4]) for x in rs)
    body = "%s.\n\n" % rs[0]["role"]
    for x in rs:
        body += "- %s: %s See [[%s]].\n" % (x["date"], x["saw"], NODE)
    body += "\n## Sources\n" + "\n".join("- %s — %s" % (x["cite"], x["src"]) for x in rs) + "\n"
    person(v, role=rs[0]["role"], nat="American", life="", stance=stance, tags=PEOPLE_TAGS, body=body)


def sec(r):
    q2 = ("\n>\n> %s" % r["q2"]) if r.get("q2") else ""
    return "## %s — %s\n\n%s\n\n> %s%s\n\n**Source.** %s — <%s>\n\n**Caveat.** %s\n" % (
        r["voice"], r["date"], r["saw"], r["q"], q2, r["cite"], r["src"], r["cav"])


body = ("Fifteen statements by members of the US Congress, found by full-text search of the *Congressional Record* in the GovInfo API (collections CREC, 1994 on, and CRECB, "
        "the bound edition, 1873 on) and read in the GovInfo granule text (daily edition) or the PDF text layer (bound edition). Each is the member's own words on the floor or in "
        "the Extensions of Remarks; newspaper articles and letters that members had printed in the Record are not counted. **Evidence P** (the official record). "
        "The bound-edition scans are two-column OCR with some interleaving, so page numbers are approximate (from running heads) and quotes were rebuilt from the interleaved lines. "
        "The Armenian-question item (Levin) is the speakers' framing, not the vault's.\n\n"
        "Names: " + ", ".join("[[%s]]" % v for v in voices) + ".\n\n"
        + "\n".join(sec(r) for r in R)
        + "\n## Sources\n- GovInfo, *Congressional Record* (CREC / CRECB): https://www.govinfo.gov/app/collection/crecb\n"
        + "\n".join("- %s — %s" % (r["cite"], r["src"]) for r in R) + "\n")
note("Events", NODE, {"type": "event", "when": "1937–2014", "tags": ["event", "verified", "united-states", "us-congress", "congressional-record"]}, body)
print("ok", len(R), "records,", len(voices), "people")
