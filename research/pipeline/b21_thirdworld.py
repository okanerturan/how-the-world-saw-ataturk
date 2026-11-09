# -*- coding: utf-8 -*-
# Census round 13 (Nov 2026) — decolonisation-era and postwar leaders in their own words about Atatürk.
# Records: Weizmann (Trial and Error, 1949), Sadat (In Search of Identity, 1978), Bhutto (Karachi speech, 13 Jun 1965),
# Gaddafi (essay of 22 Nov 2002). Each quote is checked against the text banked in tools/.state/round13/src_*.txt.
import json, os, re, sys
from _lib import note

HERE = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(HERE, "tools", ".state", "round13")
NODE = "Postwar and Third World Leaders on Atatürk in Their Own Words"

def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"').replace("­", "")
    s = re.sub(r"-\s*\n", "", s)
    return re.sub(r"\s+", " ", s)

def bank(n):
    return norm(open(os.path.join(STATE, n), encoding="utf-8").read())

R = [
 dict(id="weizmann-1949", voice="Chaim Weizmann", role="Zionist leader, first President of Israel; memoir of his Nov 1938 Turkey visit", c="Britain/Palestine (memoir 1949)", cn="Israel",
      dom="politics", date="1949", era="posthumous", mirror=None, pol="instrumental", inten=1,
      saw="Recalls Atatürk sending officials to Palestine to see if Zionist methods could revive Turkey, and why he sought Turkish mediation with the Arabs in 1938.",
      q="Ataturk had sent a number of Government representatives to Palestine to see whether our methods could not be applied to the revival of Turkey.",
      art="memoir", ev="P", med=None,
      cav="Written in 1949 about events up to 1938, so era is posthumous although the claim is about Atatürk's lifetime. Weizmann reports Atatürk's act and Turkey's 'progressive record'; he states no personal verdict on Atatürk and his purpose is to explain why Turkish mediation with the Arabs seemed worth trying. The sentence runs over the page break 459/460 ('Kemal' ends p. 459). Text read from the open Digital Library of India scan (OCR). No mention of Atatürk's death (he reached Istanbul on 27 Nov 1938).",
      src=["src_weizmann_459_460.txt"],
      urls=["https://archive.org/details/in.ernet.dli.2015.475020"],
      loc="Weizmann, Trial and Error (Harper, 1949), pp. 459-460", link=None),
 dict(id="sadat-1978", voice="Anwar Sadat", role="President of Egypt; memoir of his boyhood and Military Academy years (1930s)", c="Egypt (memoir 1978)", cn="Egypt",
      dom="politics", date="1978", era="posthumous", mirror="anti-colonial-liberator", pol="admiring", inten=3,
      saw="Recalls a photograph of Atatürk in the family home, and taking him as his ideal at the military academy.",
      q="At the academy, Ataturk continued to be my ideal. I started to read books on the Turkish Revolution",
      art="memoir", ev="P", med="Read through search-engine text snippets of three online copies (slideshare, dokumen.pub, vdoc.pub); the printed book (Harper & Row 1978) was not opened and the page of this passage is not known",
      cav="Memoir written 1975-77, so the admiration is retrospective, and Sadat wrote it as president after breaking with Nasser's legacy. The earlier Zahran passage (about p. 12) says there was a photograph of Atatürk in the family's Cairo house, that his father called him 'a great man', and that 'Kemal Atatürk was idealized in the Islamic world; his name was familiar as a leader who wanted to liberate and rebuild his country.' Sadat also names H. C. Armstrong's The Gray Wolf as the book he was absorbed in on arriving at the War Ministry. Time (20 Mar 1978) says the same at second hand. Snippets are OCR (the name prints as 'Atatiirk' in some); intensity 3 on the strength of the career-long ideal he describes, not on page-checked text.",
      src=["src_sadat_snippets.txt"],
      urls=["https://vdoc.pub/documents/in-search-of-identity-55mp0n3fjru0", "https://slideshare.net/slideshow/in-search-of-identity-by-president-sadat/281066621"],
      loc="Sadat, In Search of Identity (1978), the 'Zahran' passage (c. p. 12) and the academy passage", link=None),
 dict(id="bhutto-1965-06-13", voice="Zulfikar Ali Bhutto", role="Foreign Minister of Pakistan (later Prime Minister)", c="Pakistan", cn="Pakistan",
      dom="politics", date="1965-06-13", era="posthumous", mirror=None, pol="witness", inten=1,
      saw="Says Atatürk and his companions found a revived Caliphate incompatible with their political ideas and abolished it.",
      q="finding a resusciated Caliphate incompatible with their political ideas",
      art="speech", ev="P", med="Search-engine snippet of the bhutto.org PDF (direct fetch was blocked); page not known",
      cav="A historical account with no stated judgement of Atatürk, hence witness. 'resusciated' is the PDF's own spelling. A second Bhutto sentence on Atatürk, 'We will have to raise from our soil an Ataturk or a Jinnah who will mobilize our people', is in the bhutto.org collection of speeches 1948-1966 but the individual speech and date were not identified, so it is NOT stored (see candidates file).",
      src=["src_bhutto_1965.txt"],
      urls=["https://bhutto.org/wp-content/uploads/2020/12/Pakistan-and-the-Muslim-World-Zulfikar-Ali-Bhutto.pdf"],
      loc="Bhutto, 'Pakistan and the Muslim World', speech to the Pakistan Islamic Council for International Affairs, Karachi, 13 June 1965", link=None),
 dict(id="gaddafi-2002-11-22", voice="Muammar Gaddafi", role="Leader of Libya", c="Libya", cn="Libya",
      dom="politics", date="2002-11-22", era="posthumous", mirror=None, pol="hostile", inten=1,
      saw="Writing against Turkish EU entry, says the Latin alphabet Turkey adopted is not really Latin and has corrupted Latin orthography.",
      q="Even the Latin alphabet it has adopted is not really Latin. It has actually corrupted Latin orthography.",
      art="article", ev="P", med="English text on algaddafi.org (a Gaddafi-legacy site), dated '22.11.2002' on the page; original place of publication not given",
      cav="Hostility is aimed at the alphabet reform, not at Atatürk by name. Atatürk appears once, in passing: 'The problem does not lie with the older generation of Turkish politicians who continue to hold Ataturk and his teachings sacred.' The text does NOT support the vault's person note, which says Gaddafi called Atatürk a 'catastrophic traitor' for abolishing the Caliphate; no such statement was found.",
      src=["src_gaddafi_2002.txt"],
      urls=["https://algaddafi.org/turkey-europe-and-the-bin-ladenists"],
      loc="Gaddafi, 'Turkey, Europe and the Bin-Ladenists', 22 Nov 2002", link="Muammar Gaddafi"),
]

bad = [r["id"] for r in R if norm(r["q"]).replace(" ", "") not in bank(r["src"][0]).replace(" ", "")]
if bad:
    sys.exit("quote not found in source bank: %s" % bad)
for r in R:
    assert len(r["saw"].split()) <= 25, (r["id"], len(r["saw"].split()))

with open(os.path.join(STATE, "gazes_thirdworld.jsonl"), "w", encoding="utf-8") as f:
    for r in R:
        rec = {"id": r["id"], "voice": r["voice"], "voice_type": "person", "role": r["role"], "country": r["c"],
               "country_now": r["cn"], "domain": r["dom"], "date": r["date"], "era": r["era"], "mirror": r["mirror"],
               "polarity": r["pol"], "intensity": r["inten"], "what_they_saw": r["saw"], "quote": r["q"],
               "artifact": r["art"], "evidence": r["ev"], "mediated_by": r["med"], "caveat": r["cav"],
               "node": NODE, "sources": r["urls"]}
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")

nxt = {"weizmann-1949": "Page-image check of pp. 459-460 in a print copy; Weizmann Papers for 1938 Istanbul talks",
       "sadat-1978": "Open a print or lending copy to get the page of the academy passage; Revolt on the Nile (1957) for an earlier version",
       "bhutto-1965-06-13": "Open the PDF in a browser to confirm the page; identify the 'Ataturk or a Jinnah' speech and date",
       "gaddafi-2002-11-22": "Original Libyan/Arabic or Jamahiriya press text of 22 Nov 2002"}
with open(os.path.join(STATE, "ledger_thirdworld.md"), "w", encoding="utf-8") as f:
    f.write("| Claim | Node | Status | Sources | Next step |\n|---|---|---|---|---|\n")
    for r in R:
        f.write("| %s (%s, %s): \"%s\" | %s | verified %s (%s) | %s | %s |\n" % (
            r["voice"], r["role"], r["date"], r["q"][:110].replace("|", "/") + ("..." if len(r["q"]) > 110 else ""),
            NODE, r["ev"], r["loc"], "; ".join(r["urls"][:1]), nxt[r["id"]]))

body = ["""
Round 13 looked for the leaders of decolonisation and the postwar Middle East, Africa and Asia speaking about Kemal in
their own words. Four records survived reading. Most of the big names were dry (see *Dry ends*), and one result
corrects an existing claim in the vault. Each quote was checked against fetched text before this note was written.

## The pattern

- **The boyhood hero:** Anwar Sadat's memoir has Atatürk's photograph in the family house and a cadet's ideal; the
  admiration is retrospective (1978), written by a president who had broken with [[Gamal Abdel Nasser]]'s legacy.
- **The partner who wanted something:** Chaim Weizmann in 1949 recalls Atatürk sending officials to see Zionist
  settlement in Palestine, and why he thought Ankara could mediate with the Arabs in 1938 — usefulness, not a verdict.
- **The historian-statesman:** Zulfikar Ali Bhutto in 1965 recounts the end of the Caliphate; see
  [[Abolition of the Caliphate]] and [[Khilafat Movement]].
- **The dismissive neighbour:** Muammar Gaddafi in 2002 sneers at the Latin alphabet; the vault's claim that he called
  Atatürk a traitor is not backed by this text (see [[Muammar Gaddafi]]).
"""]
for r in R:
    body.append("\n## %s, %s (%s)\n" % (r["voice"], r["role"], r["date"]))
    body.append("*%s*\n" % r["saw"])
    body.append("> %s\n" % r["q"])
    body.append("%s Location: %s. Evidence %s%s.%s\n" % (r["cav"], r["loc"], r["ev"], (" (" + r["med"] + ")") if r["med"] else "", (" See [[%s]]." % r["link"]) if r["link"] else ""))

body.append("""
## Dry ends (round 13)

- **Nasser:** *The Philosophy of the Revolution* (1954; archive.org `dli.ernet.449321`, full OCR text grepped) never names Kemal or Atatürk; its one Turkey hit is his mother's Turkish descent. No Nasser speech with a sentence on Atatürk was reached. The Nasser–Menderes hostility (Baghdad Pact, 1955) is well documented in secondary sources but those give no Nasser line on Atatürk. See [[Gamal Abdel Nasser]].
- **Jabotinsky:** the open web gives only his 1908–11 *Le Jeune Turc* period (Springer chapter, 2020); no 1920s Kemal article was located. See [[Ze'ev Jabotinsky]].
- **Nkrumah, Nyerere, Senghor, Indira Gandhi, Lee Kuan Yew:** no statement of theirs on Atatürk found (Lee appears in the *Diplomat*/Harvard commentary as a comparison drawn by others, and the blurb of *From Third World to First* names Atatürk only in the publisher's text).
- **Mahathir:** laid a wreath at Anıtkabir on 25 July 2019 (Malay Mail, Bernama); no sentence by him on Atatürk found.
- **Arafat, King Hussein, Saddam, the Assads:** not reached within the search budget.

## Sources
- Chaim Weizmann, *Trial and Error* (Harper, 1949), pp. 459–460, archive.org `in.ernet.dli.2015.475020`.
- Anwar Sadat, *In Search of Identity* (Harper & Row, 1978), via text snippets of online copies.
- Zulfikar Ali Bhutto, 'Pakistan and the Muslim World', Karachi, 13 June 1965, bhutto.org.
- Muammar Gaddafi, 'Turkey, Europe and the Bin-Ladenists', 22 Nov 2002, algaddafi.org.
- Gamal Abdel Nasser, *The Philosophy of the Revolution* (1954), archive.org `dli.ernet.449321`.
""")

note("Events", NODE,
     {"type": "event", "when": "1949–2002",
      "tags": ["event", "verified", "heads-of-state", "leaders", "postwar"]},
     "\n".join(body))
print("ok", len(R), "records")
