# -*- coding: utf-8 -*-
# Census round 22 (Nov 2026) — Australian and New Zealand leaders on Atatürk, Anzac and Gallipoli speeches.
# Sources: Australian PM Transcripts (pmtranscripts.pmc.gov.au, query?transcript=ID XML, banked in tools/.state/round22/anzac/)
# and beehive.govt.nz speeches. The script refuses to run if a quote is not found in its bank.
import json, os, re, sys
from _lib import note, person

HERE = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(HERE, "tools", ".state", "round22")
B = os.path.join(STATE, "anzac")


def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", s).strip()


def bank(fn):
    return norm(open(os.path.join(B, fn), encoding="utf-8").read())


PM = "https://pmtranscripts.pmc.gov.au/release/transcript-"
JM = ("The 'Johnnies and Mehmets' / 'your sons are now lying in our bosom' text that Anzac speakers attribute to Atatürk is itself contested: no 1934 original has been found, "
      "it first appears in print in 1953 via Interior Minister Şükrü Kaya's recollection, and the 'Johnnies and Mehmets' clause is a 1978 Australian addition (see [[Johnnies and Mehmets]]). "
      "So this is a speaker's view of the Atatürk of the Anzac legend, spoken at a commemorative or diplomatic occasion that rewards praise. ")

R = [
 dict(id="hawke-1990", voice="Bob Hawke", role="Prime Minister of Australia (1983–1991)", c="Australia", dom="politics", date="1990-04-25", era="posthumous",
      pol="admiring", inten=2, art="speech", mirror="chivalrous-enemy", f="pm_8010.txt", tid="8010",
      title="Speech at Lone Pine Ceremony, Gallipoli, 25 April 1990",
      saw="At Lone Pine on the 75th anniversary, honours the Turkish dead as inspired by the leadership of a 'Man of Destiny', Kemal Atatürk.",
      q="dying in defence of their homeland, inspired by the indomitable leadership of a Man of Destiny, Mustaf a Kemal known to history as Kemal Ataturk.",
      cav="OCR text of the transcript (the name is printed 'Mustaf a Kemal'; the space is the transcript's). In the Ankara dinner speech two days earlier (PM Transcripts 8008, 23 April 1990, garbled OCR) Hawke calls him 'the great Mustapha Kema[l] Ataturk' whose Gallipoli defence 'demonstrated the singular qualities of leadership' and says the 1934 tribute 'written by Ataturk' shows 'complete reconciliation of former enemies'. " + JM),
 dict(id="hawke-1991", voice="Bob Hawke", role="Prime Minister of Australia (1983–1991)", c="Australia", dom="politics", date="1991-05-09", era="posthumous",
      pol="admiring", inten=1, art="speech", mirror="chivalrous-enemy", f="pm_8295.txt", tid="8295",
      title="Speech at Parliamentary dinner for President Özal of Turkey, Canberra, 9 May 1991",
      saw="Tells President Özal that Atatürk's leadership and skill at Gallipoli paved the way for his building of the modern Turkish state.",
      q="the leadership and skill displayed by Kemal Ataturk in defending his homeland at Gallipoli paved the way for his building of the modern state of Turkey.",
      cav="A toast-style speech to a visiting head of state; praise is partly occasion. " + JM),
 dict(id="howard-2000", voice="John Howard", role="Prime Minister of Australia (1996–2007)", c="Australia", dom="politics", date="2000-04-25", era="posthumous",
      pol="admiring", inten=1, art="speech", mirror="chivalrous-enemy", f="pm_22690.txt", tid="22690",
      title="Turkish International Service at Mehmetcik Abide, 25 April 2000",
      saw="At the Gallipoli international service, pays tribute to 'the great Kemal Ataturk' for the reconciliation of the nations after 1915.",
      q="I want to pay tribute to successive leaders of the Republic of Turkey, particularly the great Kemal Ataturk for the way in which the nations were reconcilled after the campaigns of 1915.",
      cav="Spelling 'reconcilled' is the transcript's. Delivered at Gallipoli in the presence of the Turkish and New Zealand prime ministers. Two days earlier in Ankara (PM Transcripts 22713, 23 April 2000) Howard called the Turks 'honoured' opponents but the pronoun is not clearly Atatürk, so that passage is not used; on 26 April in Paris (11503) a journalist, not Howard, characterises Ataturk's 1934 words as helping reconcile former enemies. " + JM),
 dict(id="rudd-2010", voice="Kevin Rudd", role="Prime Minister of Australia (2007–2010, 2013)", c="Australia", dom="politics", date="2010-04-25", era="posthumous",
      pol="admiring", inten=1, art="speech", mirror="chivalrous-enemy", f="pm_17247.txt", tid="17247",
      title="Speech at the Anzac Day national ceremony, Australian War Memorial, Canberra, 25 April 2010",
      saw="Says the Turks have embraced Australians in peace and that Atatürk's words about Johnnies and Mehmets 'speak to us still down the ages'.",
      q="the words of Ataturk (who saw no difference between our Johnnies and their Mehmets) speak to us still down the ages.",
      cav="The line adopts the Anzac-legend attribution without hedging. In a 2008 Lone Pine planting speech (PM Transcripts 16100, 4 September 2008) Rudd likewise says Turkey's leader Kemal Ataturk 'offered solace to the parents of those young Australians' in 1934. " + JM),
 dict(id="gillard-2012", voice="Julia Gillard", role="Prime Minister of Australia (2010–2013)", c="Australia", dom="politics", date="2012-04-25", era="posthumous",
      pol="witness", inten=1, art="speech", mirror="chivalrous-enemy", f="pm_18532.txt", tid="18532",
      title="Dawn Service address, Gallipoli, 25 April 2012",
      saw="Describes the Turkish commander as a skilled enemy 'destined to become a great leader' who ordered his men to attack and to die.",
      q="a skilled enemy lay in wait, led by a man destined to become a great leader. ... for which Ataturk ordered his men not only to attack but to die.",
      cav="The quote joins two passages of the same speech (marked with an ellipsis; the first does not name him, the second names Ataturk). Descriptive more than praising; the 'Johnnies' words are not quoted in this speech. Polarity witness: a stated view of his generalship, not of the man as statesman. " + JM),
 dict(id="abbott-2015-04-22", voice="Tony Abbott", role="Prime Minister of Australia (2013–2015)", c="Australia", dom="politics", date="2015-04-22", era="posthumous",
      pol="admiring", inten=2, art="quote", mirror="chivalrous-enemy", f="pm_24389.txt", tid="24389",
      title="Joint press conference with Prime Minister Davutoğlu, Ankara, 22 April 2015",
      saw="Calls Atatürk's message to the grieving mothers of Australia wise and magnanimous, from a 'truly great inspirational leader' whose legacy lives on.",
      q="That was the wise and magnanimous message of a truly great inspirational leader whose legacy lives on in modern Turkey.",
      cav="Spoken beside the Turkish prime minister on the eve of the Gallipoli centenary; occasion-bound praise. " + JM),
 dict(id="abbott-2015-04-24", voice="Tony Abbott", role="Prime Minister of Australia (2013–2015)", c="Australia", dom="politics", date="2015-04-24", era="posthumous",
      pol="admiring", inten=1, art="quote", mirror="modernization-poster-child", f="pm_24393.txt", tid="24393",
      title="Doorstop interview, HMAS Anzac, Anzac Cove, 24 April 2015",
      saw="Credits the Atatürk legacy for making peaceful, prosperous, reasonably pluralist Turkey a beacon to the Islamic world.",
      q="This is why Turkey has, for so long, thanks in large measure to the Ataturk legacy, been such a beacon to the Islamic World.",
      cav="Here Abbott speaks of Atatürk as state-builder, not of the Anzac words; an off-the-cuff doorstop. The same week (PM Transcripts 24391, Istanbul 23 April 2015) he called Mustafa Kemal Ataturk 'a worthy and resourceful leader, who embraced his fallen enemies as sons of Turkey'. " + JM),
 dict(id="turnbull-2016", voice="Malcolm Turnbull", role="Prime Minister of Australia (2015–2018)", c="Australia", dom="politics", date="2016-04-25", era="posthumous",
      pol="admiring", inten=1, art="speech", mirror="chivalrous-enemy", f="pm_40312.txt", tid="40312",
      title="Anzac Day national ceremony commemorative address, Canberra, 25 April 2016",
      saw="Says Mustafa Kemal Atatürk, the Turkish leader, would comfort the mothers of Australia for their 'Johnnies' as Turkish mothers grieved their 'Mehmets'.",
      q="In the years to come their leader Mustafa Kemal Ataturk would comfort the mothers of Australia for the loss of their 'Johnnies' just as the mothers of Turkey grieved the loss of their 'Mehmets'.",
      cav="Quotes the Anzac-legend formula in his own paraphrase and frames Atatürk as the Turks' wartime leader. " + JM),
 dict(id="morrison-2019-03-20", voice="Scott Morrison", role="Prime Minister of Australia (2018–2022)", c="Australia", dom="politics", date="2019-03-20", era="posthumous",
      pol="conflicted", inten=2, art="quote", mirror="modernization-poster-child", f="pm_42211.txt", tid="42211",
      title="Press conference, Canberra, 20 March 2019",
      saw="Invokes Atatürk against Erdoğan after the Christchurch remarks: Atatürk sought to make a modern, embracing nation and made a promise to Australians.",
      q="Ataturk sought to transform his country into a modern nation, an embracing nation, and I think these comments are at odds with that spirit and the promise that was made to Australians",
      cav="Instrumental as much as admiring: Atatürk is used as a standard to rebuke Turkey's president Erdoğan over his remarks after the Christchurch attacks (the press conference calls them 'highly offensive' and 'reckless'). Same day on 2GB (PM Transcripts 42207) Morrison said Erdoğan's comments were 'very much at odds with what Ataturk said', and on 28 March (42235) that Erdoğan 'had failed on the promise made by Ataturk to the mothers of Anzacs'. Polarity conflicted: he treats Atatürk as a benchmark Erdoğan fails, not as an object of study. " + JM),
 dict(id="peters-2007", voice="Winston Peters", role="New Zealand Foreign Minister (2005–2008; later Deputy Prime Minister)", c="New Zealand", dom="politics", date="2007-04-25", era="posthumous",
      pol="admiring", inten=1, art="speech", mirror="chivalrous-enemy", f="nz_peters2007.txt", tid=None,
      url="https://www.beehive.govt.nz/speech/anzac-day-dawn-service-address-gallipoli",
      title="Anzac Day Dawn Service address, Gallipoli, 25 April 2007",
      saw="Says Atatürk, a divisional commander at Gallipoli and later founder of the Republic, paved the way for reconciliation with generous words.",
      q="it was Mustafa Kemal Atatürk, a divisional commander at Gallipoli and later founder of the Turkish Republic, who paved the way for reconciliation.",
      cav="Not a prime minister at the time (Foreign Minister, delivering the government's address). A near-identical passage appears in Nathan Guy's 2012 Gallipoli speech, i.e. the ministry's stock text. " + JM),
 dict(id="peters-2024", voice="Winston Peters", role="New Zealand Deputy Prime Minister and Foreign Minister", c="New Zealand", dom="politics", date="2024-04-25", era="posthumous",
      pol="admiring", inten=1, art="speech", mirror="chivalrous-enemy", f="nz_peters2024.txt", tid=None,
      url="https://www.beehive.govt.nz/speech/anzac-commemorative-address-–-dawn-service-gallipoli-türkiye",
      title="Anzac Commemorative Address, Dawn Service, Gallipoli, 25 April 2024",
      saw="Says 'Major General and later President' Atatürk's words to Anzac mothers spoke to the friendship between former enemies.",
      q="Major General and later President Ataturk's words to ANZAC mothers after the Gallipoli campaign spoke to that friendship",
      cav="Quotes the words as 'You are now lying in the soil of a friendly country. Therefore, rest in peace.' without the 'Johnnies' clause. Peters speaks as Deputy Prime Minister and Foreign Minister. " + JM),
 dict(id="goff-2001", voice="Phil Goff", role="New Zealand Minister of Foreign Affairs and Trade (1999–2005)", c="New Zealand", dom="politics", date="2001-04-25", era="posthumous",
      pol="admiring", inten=1, art="speech", mirror="chivalrous-enemy", f="nz_goff2001.txt", tid=None,
      url="https://www.beehive.govt.nz/node/10329",
      title="ANZAC Dawn Service speech, Gallipoli, 25 April 2001",
      saw="Calls Atatürk the 'gallant Turkish commander' and founder of the Republic whose generous words are the foundation of NZ–Turkey friendship.",
      q="It was Mustafa Kemal Ataturk, the gallant Turkish commander, and later the founder of the Turkish Republic, who said that the fallen rest in the soil of a friendly country.",
      cav="Government delegation leader, not prime minister. Goff later became Labour leader and High Commissioner to the UK. " + JM),
]
R = [r for r in R if r['id'] not in {'turnbull-2016', 'peters-2024'}]  # dropped at the independent check (no stated view)

bad = [r["id"] for r in R if norm(r["q"].split(" ... ")[0]) not in bank(r["f"]) or (" ... " in r["q"] and norm(r["q"].split(" ... ")[1]) not in bank(r["f"]))]
if bad:
    sys.exit("quote not found in source bank: %s" % bad)
for r in R:
    assert len(r["saw"].split()) <= 25, (r["id"], len(r["saw"].split()))
    r["url"] = r.get("url") or (PM + r["tid"])
    r["cn"] = r["c"]

NODE = "Anzac Day Leaders on Atatürk, 1990–2024 — Australian and New Zealand Speeches"
with open(os.path.join(STATE, "gazes_anzac.jsonl"), "w", encoding="utf-8") as f:
    for r in R:
        rec = {"id": r["id"], "voice": r["voice"], "voice_type": "person", "role": r["role"],
               "country": r["c"], "country_now": r["cn"], "domain": r["dom"], "date": r["date"], "era": r["era"],
               "mirror": r["mirror"], "polarity": r["pol"], "intensity": r["inten"], "what_they_saw": r["saw"],
               "quote": r["q"], "artifact": r["art"], "evidence": "P", "mediated_by": None,
               "caveat": r["cav"] + "Cited as: " + r["title"] + ".", "node": NODE, "sources": [r["url"]]}
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")

with open(os.path.join(STATE, "ledger_anzac.md"), "w", encoding="utf-8") as f:
    f.write("| Claim | Node | Status | Sources | Next step |\n|---|---|---|---|---|\n")
    for r in R:
        f.write("| %s (%s): %s | %s | verified P (official transcript read) | %s | — |\n" % (r["voice"], r["date"], r["saw"], NODE, r["url"]))

PEOPLE = {"Bob Hawke": "Australian", "John Howard": "Australian", "Kevin Rudd": "Australian", "Julia Gillard": "Australian",
          "Tony Abbott": "Australian", "Scott Morrison": "Australian",
          "Winston Peters": "New Zealander", "Phil Goff": "New Zealander"}
for name, nat in PEOPLE.items():
    rs = [r for r in R if r["voice"] == name]
    lines = "\n".join("- %s — %s: %s <%s>" % (r["date"], r["title"], r["saw"], r["url"]) for r in rs)
    person(name, role=rs[0]["role"], nat=nat, life="", stance="; ".join("%s (%s)" % (r["pol"], r["date"][:4]) for r in rs),
           tags=["verified", "anzac"],
           body="%s. Speeches on Atatürk and Gallipoli; see [[%s]] and [[Johnnies and Mehmets]].\n\n%s\n\n## Sources\n%s\n" % (rs[0]["role"], NODE, lines, "\n".join("- %s" % r["url"] for r in rs)))

def sec(r):
    return "## %s — %s (%s)\n\n%s\n\n> %s\n\n**Caveat.** %s\n\nSource: <%s>\n" % (r["voice"], r["title"], r["date"], r["saw"], r["q"], r["cav"], r["url"])

body = ("Twelve records of Australian and New Zealand leaders speaking of Atatürk at Anzac and Gallipoli occasions, from Hawke (1990) to Peters (2024), read in the "
        "Australian PM Transcripts archive (official, evidence P) and on beehive.govt.nz. The pattern: Atatürk is always the generous former enemy of the 'Johnnies and Mehmets' legend, "
        "never the reformer, except when Morrison invokes him against Erdoğan in 2019 and Abbott in 2015 nods to the secular 'beacon'. "
        "Not found: Menzies, Holt, Whitlam, Fraser, Keating (no PM Transcripts hits for Ataturk or Kemal), nor New Zealand's Clark, Key (2015 Dawn Service speech never names him) or Luxon (2025 Gallipoli and Chunuk Bair speeches do not). "
        "See [[Johnnies and Mehmets]] and [[Gallipoli Campaign]].\n\n" + "\n".join(sec(r) for r in R)
        + "\n## Sources\n" + "\n".join("- %s" % r["url"] for r in R) + "\n- Australian PM Transcripts, search https://pmtranscripts.pmc.gov.au/?body=Ataturk&items_per_page=100\n")
note("Events", NODE, {"type": "event", "when": "1990–2024", "tags": ["event", "verified", "australia", "new-zealand", "anzac"]}, body)
print("ok", len(R))
