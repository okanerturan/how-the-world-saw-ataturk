# -*- coding: utf-8 -*-
# Census round 23 (Nov 2026) — second pass through the Congressional Record, bound edition 1957-1992 (GovInfo, free).
# Bank: tools/.state/round23/txt/ = pdftotext of the bound-edition granule PDFs (111 granules with a chamber heading, Senate/House/Extensions).
# The script refuses to run if a quote is not found in its bank. Two-column OCR interleaves, so the check is a word-subsequence/pair
# match inside a window after the anchor (as in b31_congress.py).
import json, os, re, sys, html
from _lib import note, person

HERE = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(HERE, "tools", ".state", "round23")
BANK = os.path.join(STATE, "txt")

NODE = "Senate and House on Atatürk, 1957–1990 — Powell, Sikes, Mathias and Byrd"


def words(s):
    s = html.unescape(s)
    s = s.replace("``", '"').replace("''", '"').replace("’", "'").replace("“", '"').replace("”", '"')
    return re.findall(r"[A-Za-z0-9]+", s.lower())


OCRFIX = {"modem Republic": "modern Republic", "modem state": "modern state"}


def read_bank(fn):
    t = open(os.path.join(BANK, fn), encoding="utf-8", errors="ignore").read()
    t = re.sub(r"\n\s*\d{3,5}\s*\n", "\n", t)  # stray page numbers
    t = re.sub(r"-\n\s*", "", t)
    for a, b in OCRFIX.items():
        t = t.replace(a, b)
    return t


def check(fn, anchor, quote, window=3500):
    t1 = re.sub(r"\s+", " ", read_bank(fn))
    ws = words(quote)
    pairs = set(zip(ws, ws[1:]))
    for m in re.finditer(anchor, t1):
        seg = words(t1[max(0, m.start() - window): m.start() + window])
        have = set(seg)
        spairs = set(zip(seg, seg[1:]))
        miss = [w for w in set(ws) if w not in have]
        if len(miss) <= 2 and len(pairs & spairs) >= 0.75 * len(pairs):
            return True
    return False


GOV = "https://www.govinfo.gov/content/pkg/"


def url_b(g):
    pkg = re.sub(r"-\d+-\d+(-\d+)?$", "", g)
    pkg = re.sub(r"-v\d+$", "", pkg) if False else pkg
    return "%s%s/pdf/%s.pdf" % (GOV, pkg, g)


def mk(g):
    return "GPO-CRECB-" + g


R = [
 dict(id="powell-1957-08", voice="Adam Clayton Powell Jr.", role="U.S. Representative from New York (Harlem)", date="1957-08-27", mirror="modernization-poster-child", pol="admiring", inten=2,
      cite="Extensions of Remarks (House), 27 August 1957, Congressional Record vol. 103 (bound), pp. ~16181-16182 (granule CRECB-1957-pt12-4-3)",
      saw="Sends Republic Day greetings and sketches Atatürk's revolution, calling the transformation of Turkey since 1919 admirable and its modernisation 'the goal of Kemal Ataturk'.",
      q="No one can fail to admire the courage with which this country has tackled its huge tasks. Turkey, under Mustafa Kemal Ataturk, set out to be a modern nation and became a healthy republic with amazing vitality.",
      g="1957-pt12-4-3", anchor="No one can fail to admire",
      cav="Delivered as one of his greetings on the anniversaries of the Bandung Conference states ('I announced that I would address the United States Congress each time there was an anniversary'); the account of the reforms reads like embassy-supplied material, so it is a courtesy text as well as a view. Page numbers from the running heads (OCR)."),
 dict(id="humphrey-1963-02", voice="Hubert H. Humphrey", role="U.S. Senator from Minnesota (Democrat)", date="1963-02-05", mirror=None, pol="instrumental", inten=1,
      cite="Senate, 5 February 1963, Congressional Record vol. 109 (bound), pp. ~1794-1796 (granule CRECB-1963-pt2-3-1)",
      saw="Rebutting an article on Turkish-Soviet drift, calls the 1921 treaty of 'the revolutionary governments of Ataturk and Lenin' a natural accommodation of two ostracised states.",
      q="A treaty of friendship between the revolutionary governments of Ataturk and Lenin was a not unnatural accommodation between two countries which at that particular juncture of history were ostracized from Europe.",
      g="1963-pt2-3-1", anchor="revolutionary governments of Ataturk",
      cav="His own remarks, defending Turkey's loyalty against a printed article (the article, which calls Atatürk and Lenin 'close friends and allies', is not counted). He ends: 'The proud land of Ataturk has no hankering to become entangled in the meshes of Soviet economic imperialism.' Atatürk is an argument, not the subject; two-column OCR."),
 dict(id="sikes-1975-10", voice="Robert L. F. Sikes", role="U.S. Representative from Florida (Democrat)", date="1975-10-02", mirror="modernization-poster-child", pol="admiring", inten=1,
      cite="House of Representatives, 2 October 1975, Congressional Record vol. 121 (bound), p. ~31479 (granule CRECB-1975-pt24-5-2)",
      saw="Arguing to lift the Turkish arms embargo, credits 'the strong leadership of Ataturk' with giving the Turks a new concept of national responsibility and progress.",
      q="Following World War I, the Turks developed a new concept under the strong leadership of Ataturk-Mustafa Kemal-of national responsibility and progress.",
      g="1975-pt24-5-2", anchor="strong leadership of Ataturk",
      cav="One sentence in the Cyprus arms-embargo debate, a defence of Turkey against the 'Terrible Turks' talk; the praise serves the argument. State from his own colleague's reference ('the distinguished gentleman from Florida') and the standard record. Page from running head."),
 dict(id="mathias-1981-07", voice="Charles McC. Mathias", role="U.S. Senator from Maryland (Republican)", date="1981-07-30", mirror="modernization-poster-child", pol="admiring", inten=3,
      cite="Senate, 30 July 1981, 'Reflections on Ataturk Centenary', Congressional Record vol. 127 (bound), pp. 18675-18676 (granule CRECB-1981-pt14-2-1)",
      saw="Marks the centennial: Atatürk shaped Turkey 'from the ruins of a decaying empire', a charismatic rationalist and organiser whose legacy is Turkey's challenge.",
      q="His extraordinary determination, dedication, and dynamic leadership combined with an unwavering vision of Turkey's role in the world drove him to a relentless reform of Turkey's social and political structure.",
      q2="From a defeated, divided dynasty torn between East and West, he created a modern democratic republic with an unwavering commitment to the West.",
      g="1981-pt14-2-1", anchor="extraordinary determination",
      cav="A full statement of his own (about 1,000 words) headed 'Reflections on Ataturk Centenary', quoting Atatürk and Toynbee. State and party from the standard record, not the passage. The OCR misreads some letters ('Kemv.l'); quotes taken from clean lines."),
 dict(id="coelho-1985-06", voice="Tony Coelho", role="U.S. Representative from California (Democrat)", date="1985-06-04", mirror=None, pol="instrumental", inten=1,
      cite="House of Representatives, 4 June 1985, Congressional Record vol. 131 (bound), p. ~13989 (granule CRECB-1985-pt10-6-1)",
      saw="In an Armenian resolution debate, calls Kemal 'the George Washington of Turkey' and his reported 1926 acknowledgment significant, 'by the father of the current Government'.",
      q="This is a significant acknowledgment by the father of the current Government of Turkey and I find it intriguing that the current Government of Turkey does not accept it",
      g="1985-pt10-6-1", anchor="significant acknowledgment by the father",
      cav="Sensitive thread (the Armenian question): the Representative's framing and his attribution of a 1926 Los Angeles Examiner interview, which the vault does not test here. Earlier in the same speech: 'a Mr. Kemal, who is recognized by all of Turkey as the George Washington of Turkey.' Page from running head."),
 dict(id="aspin-1985-12", voice="Les Aspin", role="U.S. Representative from Wisconsin (Democrat)", date="1985-12-12", mirror=None, pol="instrumental", inten=1,
      cite="House of Representatives, 12 December 1985 (H.J. Res. 192 debate), Congressional Record vol. 131 (bound), p. ~36164 (granule CRECB-1985-pt26-2-1)",
      saw="Arguing for the Armenian remembrance resolution, says 'Kemal Ataturk, the founder of the Turkish Republic, himself denounced the massacre of millions'.",
      q="Most significantly, Kemal Ataturk, the founder of the Turkish Republic, himself denounced the massacre of \"millions\" of Armenians.",
      g="1985-pt26-2-1", anchor="Most significantly, Kemal Ataturk",
      cav="Sensitive thread (the Armenian question): the speaker's framing, resting on the 1926 interview he cites in the next sentence. He uses Atatürk to separate the Republic from the Ottoman governments. State and party from the standard record."),
 dict(id="simon-1986-04", voice="Paul Simon", role="U.S. Senator from Illinois (Democrat)", date="1986-04-22", mirror=None, pol="instrumental", inten=1,
      cite="Senate, 22 April 1986, Congressional Record vol. 132 (bound), p. ~8251 (granule CRECB-1986-pt6-7-1)",
      saw="In a remembrance speech on the Armenians, states that Atatürk, founder of modern Turkey, condemned the genocide, citing a 1926 article.",
      q="Third, we know that Kemal Ataturk, founder of modern Turkey, condemned the genocide.",
      g="1986-pt6-7-1", anchor="Third, we know that Kemal Ataturk", frags=["Third, we know that Kemal Ataturk,", "founder of modern Turkey,", "demned the genocide. In a 1926 article"],
      cav="Sensitive thread (the Armenian question): the speaker's framing and attribution, not the vault's. The two-column OCR interleaves his lines with another column; the sentence was rebuilt from the alternating lines of the middle column ('Third, we know that Kemal Ataturk,' / 'founder of modern Turkey, con-' / 'demned the genocide'); the column is read as his because it follows his 'we must restate the facts as we know them'. State and party from the standard record."),
 dict(id="levin-1990-02", voice="Carl Levin", role="U.S. Senator from Michigan (Democrat)", date="1990-02-20", mirror=None, pol="instrumental", inten=1,
      cite="Senate, 20 February 1990 (S.J. Res. 212 debate), Congressional Record vol. 136 (bound), p. ~2025 (granule CRECB-1990-pt2-3-2)",
      saw="In the Armenian commemoration debate, says Atatürk 'himself acknowledged the crimes of the earlier government', citing the 1926 Los Angeles Examiner interview.",
      q="In an interview published in the Los Angeles Examiner on August 1, 1926, Ataturk himself acknowledged the crimes of the earlier government.",
      g="1990-pt2-3-2", anchor="Ataturk himself acknowledged",
      cav="Sensitive thread (the Armenian question): the Senator's framing and attribution, which the vault does not endorse. A second, later dated statement by an existing voice (he made the same point in 1985 and 1994)."),
 dict(id="wilson-1990-02", voice="Pete Wilson", role="U.S. Senator from California (Republican)", date="1990-02-20", mirror=None, pol="instrumental", inten=1,
      cite="Senate, 20 February 1990 (S.J. Res. 212 debate), Congressional Record vol. 136 (bound), p. ~2038 (granule CRECB-1990-pt2-3-2)",
      saw="Supporting the Armenian resolution, says it should be no surprise that Atatürk, 'revered in Turkish history', renounced the Ottoman 'massacres of millions'.",
      q="So it should come as no surprise that the founder of the modern Republic of Turkey, someone revered in Turkish history, Kemal Ataturk, explicitly renounced what he termed the \"massacres of millions\" by the Ottoman regime.",
      g="1990-pt2-3-2", anchor="someone revered in Turkish history",
      cav="Sensitive thread (the Armenian question): the Senator's framing. The same passage is repeated in the 22 Feb 1990 sitting (granule CRECB-1990-pt2-5-2). Party and state from the standard record and the letter from California's Governor's office printed there; OCR reads 'modem' for 'modern' (corrected)."),
 dict(id="dole-1990-02", voice="Bob Dole", role="U.S. Senator from Kansas, Senate Republican leader (Republican)", date="1990-02-21", mirror=None, pol="instrumental", inten=1,
      cite="Senate, 21 February 1990 (S.J. Res. 212 debate), Congressional Record vol. 136 (bound), p. ~2245 (granule CRECB-1990-pt2-4-2)",
      saw="Urging passage of the Armenian resolution, says the Ottoman Empire, not the Republic, is at issue and that Atatürk 'accepted the fact'.",
      q="Germany accepted the fact. Ataturk accepted the fact.",
      g="1990-pt2-4-2", anchor="Germany accepted the fact",
      cav="Sensitive thread (the Armenian question): the Senator's framing; 'the fact' is the Armenian genocide in his argument. Earlier the same day he says he will include 'statements by Ataturk and his acknowledgment of the genocide' (the exhibit he then entered is a staff paper, not his words). The Turkish government's side disputed the 1926 interview; the vault does not decide that here. Page from running head (OCR)."),
 dict(id="byrd-1990-02", voice="Robert C. Byrd", role="U.S. Senator from West Virginia (Democrat)", date="1990-02-21", mirror="modernization-poster-child", pol="admiring", inten=2,
      cite="Senate, 21 February 1990 (S.J. Res. 212 debate), Congressional Record vol. 136 (bound), pp. ~2156-2160 (granule CRECB-1990-pt2-4-2)",
      saw="In a long speech against the Armenian resolution, praises Atatürk: a secular Western-oriented republic with no model in 1923, 'but succeed it did'.",
      q="It did not come about simply by coincidence. When Ataturk founded the Turkish Republic in 1923, there was no single example in the world to suggest that the adventure on which she was launched might succeed, but succeed it did.",
      g="1990-pt2-4-2", anchor="When Ataturk founded the Turkish Republic",
      cav="Sensitive thread: he is speaking against the Armenian commemorative resolution (Dole's S.J. Res. 212) and uses Atatürk to argue Turkey's value to the West; this record states his view of Atatürk only. A second, earlier statement than his 2007 one already in the dataset. Page from running head (OCR)."),
]
R = [r for r in R if r['id'] not in {'simon-1986-04','dole-1990-02','aspin-1985-12','levin-1990-02','humphrey-1963-02','coelho-1985-06','wilson-1990-02'}]  # dropped at the independent check (no stated view / misattributed)

bad = []
for r in R:
    r["bank"] = mk(r["g"]) + ".txt"
    r["url"] = url_b(mk(r["g"]))
    for k in ("q", "q2"):
        if not r.get(k):
            continue
        frags = r.get("frags") if k == "q" and r.get("frags") else [r[k]]
        if not all(check(r["bank"], r["anchor"], fr) for fr in frags):
            bad.append((r["id"], k))
if bad:
    sys.exit("quote not found in source bank: %s" % bad)
for r in R:
    assert len(r["saw"].split()) <= 25, (r["id"], len(r["saw"].split()))
    r["era"] = "posthumous"

with open(os.path.join(STATE, "gazes_congress2.jsonl"), "w", encoding="utf-8") as f:
    for r in R:
        q = r["q"] + ((" … " + r["q2"]) if r.get("q2") else "")
        rec = {"id": r["id"], "voice": r["voice"], "voice_type": "person", "role": r["role"],
               "country": "United States", "country_now": "United States", "domain": "politics", "date": r["date"], "era": r["era"],
               "mirror": r["mirror"], "polarity": r["pol"], "intensity": r["inten"], "what_they_saw": r["saw"],
               "quote": q, "artifact": "speech", "evidence": "P", "mediated_by": None,
               "caveat": r["cav"] + " Cited as " + r["cite"] + ".", "node": NODE, "sources": [r["url"]]}
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")

with open(os.path.join(STATE, "ledger_congress2.md"), "w", encoding="utf-8") as f:
    f.write("| Claim | Node | Status | Sources | Next step |\n|---|---|---|---|---|\n")
    for r in R:
        f.write("| %s (%s): %s | %s | verified P (Congressional Record, GovInfo bound-edition PDF text layer; text read) | %s | page number from the printed volume / check on loc.gov |\n" % (
            r["voice"], r["date"], r["saw"], NODE, r["url"]))

EXISTING = {"Carl Levin", "Robert C. Byrd"}  # person notes already exist from round 22
voices = {}
for r in R:
    voices.setdefault(r["voice"], []).append(r)
PEOPLE_TAGS = ["verified", "us-congress", "congressional-record"]
for v, rs in voices.items():
    if v in EXISTING:
        continue
    stance = "; ".join("%s (%s)" % (x["pol"], x["date"][:4]) for x in rs)
    body = "%s.\n\n" % rs[0]["role"]
    for x in rs:
        body += "- %s: %s See [[%s]].\n" % (x["date"], x["saw"], NODE)
    body += "\n## Sources\n" + "\n".join("- %s — %s" % (x["cite"], x["url"]) for x in rs) + "\n"
    person(v, role=rs[0]["role"], nat="American", life="", stance=stance, tags=PEOPLE_TAGS, body=body)


def sec(r):
    q2 = ("\n>\n> %s" % r["q2"]) if r.get("q2") else ""
    return "## %s — %s\n\n%s\n\n> %s%s\n\n**Source.** %s — <%s>\n\n**Caveat.** %s\n" % (
        r["voice"], r["date"], r["saw"], r["q"], q2, r["cite"], r["url"], r["cav"])


body = ("Four statements by members of the US Congress (eleven were staged; the independent check dropped seven that state no view of Atatürk or were misattributed: Simon's line is Riegle's) from the bound edition of the *Congressional Record*, 1957–1990, found through the GovInfo full-text search "
        "(\"Ataturk\", collection CRECB) and read in the PDF text layer of 111 granules (Senate, House and Extensions of Remarks sittings; the 1957–1992 range left over from "
        "[[Congressional Record Pens on Atatürk — Connally, Pepper, Levin, Moynihan, Byrd, Lantos and Others]]). Each is the member's own words; articles, letters and "
        "staff papers that members had printed in the Record are not counted (Kennedy 1959, Sparkman 1958, Jenner 1958, Dole's AHEPA letter 1985 and the Bowles lecture were checked and dropped). "
        "**Evidence P** (the official record). The scans are two-column OCR with some interleaving, so page numbers are approximate (from running heads) and quotes were rebuilt from the "
        "interleaved lines. Six of the eleven are Armenian-question debates (Coelho 1985, Aspin 1985, Simon 1986, Levin, Wilson and Dole 1990): those are the speakers' framing, not the vault's. "
        "The 1981 centennial statement (Mathias) is the fullest.\n\n"
        "Names: " + ", ".join("[[%s]]" % v for v in voices) + ".\n\n"
        + "\n".join(sec(r) for r in R)
        + "\n## Sources\n- GovInfo, *Congressional Record* (CRECB): https://www.govinfo.gov/app/collection/crecb\n"
        + "\n".join("- %s — %s" % (r["cite"], r["url"]) for r in R) + "\n")
note("Events", NODE, {"type": "event", "when": "1957–1990", "tags": ["event", "verified", "united-states", "us-congress", "congressional-record"]}, body)
print("ok", len(R), "records,", len(voices), "people")
