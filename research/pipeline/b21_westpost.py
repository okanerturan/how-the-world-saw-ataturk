# -*- coding: utf-8 -*-
# Census round 13 (Nov 2026) — famous Western figures, mostly after 1938, in their own words about Atatürk.
# Records: Churchill (The Aftermath, 1929), de Gaulle (Anıtkabir and Dolmabahçe books, Oct 1968), Roncalli (diary, 1938),
# Thatcher (1986 toast, March 1988 TV interview, April 1988 Ankara dinner).
# Source texts were fetched with tools/ms fetch and banked in tools/.state/round13/src_*.txt; every quote is checked
# against its bank before anything is written.
import json, os, re, sys
from _lib import note, person

HERE = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(HERE, "tools", ".state", "round13")
NODE = "Western Statesmen and Churchmen on Atatürk in Their Own Words"

def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"').replace("­", "")
    s = s.replace("\\n", "\n").replace("\\'", "'")
    s = re.sub(r"-\s*\n", "", s)
    return re.sub(r"\s+", " ", s)

def bank(n):
    return norm(open(os.path.join(STATE, n), encoding="utf-8").read())

BEL = "https://dergipark.org.tr/en/pub/ttkbelleten/article/977862"
BELLETEN = "https://belleten.gov.tr/tam-metin/1980/tur"
TH = "https://margaretthatcher.org/document/"
R = [
 dict(id="churchill-1929", voice="Winston Churchill", role="Former Secretary of State for War; author of The World Crisis", c="United Kingdom", cn="United Kingdom",
      dom="letters", date="1929", era="contemporary", mirror="chivalrous-enemy", pol="conflicted", inten=2,
      saw="Calls Kemal a 'Man of Destiny' with a 'Warrior Prince's' qualities and his 1922 offensive 'masterly', yet ties his army to Smyrna's burning.",
      q="His operations were complicated and masterly.",
      art="book", ev="P", med=None,
      cav="Second quote in the same volume, p. 367-368: 'Mustapha Kemal, the Man of Destiny whom we have met in these volumes on the Gallipoli Peninsula ... was furnished with the power, as he already possessed the qualities, of a Warrior Prince.' On p. 419 the same author writes that Kemal's army 'celebrated their triumph by the burning of Smyrna to ashes and by a vast massacre of its Christian population', so the book is both admiring of the general and hostile to the outcome. Page numbers taken from the running heads of the 1929 Thornton Butterworth edition's djvu text (OCR); p. 418 for the quoted line. Existing record churchill-1920 is a different, hostile Commons statement.",
      src=["aftermath.txt"],
      urls=["https://archive.org/stream/in.ernet.dli.2015.209928/2015.209928.The-World_djvu.txt"],
      loc="The World Crisis: The Aftermath (Thornton Butterworth, 1929), ch. XVIII, p. 418 (also pp. 367-368)", link="Winston Churchill"),
 dict(id="de-gaulle-1968-10-25", voice="Charles de Gaulle", role="President of France, state visit to Turkey", c="France", cn="France",
      dom="politics", date="1968-10-25", era="posthumous", mirror="nation-forge-template", pol="admiring", inten=2,
      saw="Writing in the Anıtkabir book, says Atatürk reached the greatest of all glories, national renewal.",
      q="De toutes les gloires Atatürk a atteint la plus grande celle de renouveau national",
      art="quote", ev="S", med="Belleten 51/200 (Aug 1987), TTK conference text on the de Gaulle visit, quoting the Anıtkabir special book (French given in brackets after a Turkish rendering)",
      cav="Second-hand: the Belleten author prints the entry; the book page itself was not seen and the Turkish rendering reads 'The greatest of glories and honours for a man is to give his nation a new life. Atatürk did this.' The same article says de Gaulle's admiration for Atatürk was already known and that he showed it openly during the visit. The INA caption (fresques.ina.fr) confirms the wreath-laying at the mausoleum.",
      src=["src_belleten_degaulle.txt"],
      urls=[BELLETEN, BEL, "https://fresques.ina.fr/de-gaulle/fiche-media/Gaulle00146/voyage-en-turquie.html"],
      loc="Belleten 51 (200), 1987, account of 25 Oct 1968", link="Charles de Gaulle"),
 dict(id="de-gaulle-1968-10-27", voice="Charles de Gaulle", role="President of France, state visit to Turkey", c="France", cn="France",
      dom="politics", date="1968-10-27", era="posthumous", mirror="nation-forge-template", pol="admiring", inten=2,
      saw="At Dolmabahçe, where Atatürk died, writes that he could die because the light shone, the flame burned and the country was marching.",
      q="Atatürk pouvait mourir, puisque la lumière brillait, puisque la flamme brûlait, puisque le pays était en marche",
      art="quote", ev="S", med="Belleten 51/200 (Aug 1987), TTK conference text on the de Gaulle visit (French in brackets after the Turkish rendering)",
      cav="Second-hand: Belleten prints the book entry in French. The same article reports a remark on the flight out of Ankara on 29 Oct, noted by Ambassador Roger Vaurs: 'Vous avez vu vous-même l'influence exercée par un grand homme d'Etat sur son pays, même après sa mort' (not stored as a record: it is a recalled remark, relayed twice). Original Discours et messages text of the 25-28 Oct toasts not found open this round.",
      src=["src_belleten_degaulle.txt"],
      urls=[BELLETEN, BEL],
      loc="Belleten 51 (200), 1987, account of 27 Oct 1968", link="Charles de Gaulle"),
 dict(id="roncalli-1938", voice="Angelo Roncalli (later Pope John XXIII)", role="Apostolic Delegate to Turkey and Greece", c="Turkey (Vatican envoy)", cn="Turkey",
      dom="religion", date="1938", era="funeral", mirror=None, pol="conflicted", inten=2,
      saw="Prays for Atatürk and the Greek Orthodox patriarch, rejecting the cold feelings others held; leaves judgment to the Lord, whom he thinks meek and kind.",
      q="I do not share the cold sentiments entertained by these two lives which have now passed away.",
      art="memoir", ev="S", med="Ezio Bolis (Director, Pope John XXIII Foundation, Bergamo), 'What Was John XXIII Really Like?', EWTN, quoting the diary in English",
      cav="Quoted in English translation by the Foundation director from Roncalli's diary; the Italian original and the Journal of a Soul text were not reached. The diary date given is 19 Oct 1938, which is before Atatürk died (10 Nov), and the speaker says 'In October 1938, when Ataturk ... died' - a slip in the lecture; date stored as 1938 only. The entry joins Atatürk with the Greek Patriarch Chrysostomos; the speaker adds that Roncalli visited the body and prayed. The existing note on Pope John XXIII says only that he told Rome the world had lost a great man; this record rests on the diary.",
      src=["src_ewtn_roncalli.txt"],
      urls=["https://ewtn.com/catholicism/library/what-was-john-xxiii-really-like-5590"],
      loc="Bolis lecture on the Roncalli diaries (entry dated 19 Oct 1938)", link="Pope John XXIII"),
 dict(id="thatcher-1986-02-18", voice="Margaret Thatcher", role="Prime Minister of the United Kingdom, toast to Turgut Özal at No.10", c="United Kingdom", cn="United Kingdom",
      dom="politics", date="1986-02-18", era="posthumous", mirror=None, pol="instrumental", inten=1,
      saw="Calls Atatürk 'Turkey's greatest leader' while toasting Prime Minister Özal and quoting his 1924 line on advancing 'unhalting and undaunted'.",
      q="We remember the stirring words of Turkey's greatest leader, Kemal Atatürk, in 1924",
      art="speech", ev="P", med=None,
      cav="Courtesy toast at a state dinner; the Foundation lists it as a 'speaking text'. The 'greatest leader' judgement is one phrase.",
      src=["src_thatcher_106331.txt"], urls=[TH + "106331"],
      loc="Margaret Thatcher Foundation doc. 106331 (Speech at dinner for Turkish PM Özal, 18 Feb 1986)", link="Margaret Thatcher"),
 dict(id="thatcher-1988-03-23", voice="Margaret Thatcher", role="Prime Minister, interview for Turkish TV (Ali Birand)", c="United Kingdom", cn="United Kingdom",
      dom="politics", date="1988-03-23", era="posthumous", mirror=None, pol="admiring", inten=1,
      saw="Says that, rereading Turkey's history before her visit, 'we all' have tremendous admiration for Atatürk.",
      q="we all had the tremendous admiration for Atatürk",
      art="broadcast", ev="P", med=None,
      cav="COI transcript, embargoed to 4 April 1988; one sentence inside an answer about NATO and the Süleyman exhibition. Interviewer was Turkish; the answer is diplomatic.",
      src=["src_thatcher_107040.txt"], urls=[TH + "107040"],
      loc="Margaret Thatcher Foundation doc. 107040 (TV interview for Turkish TV, 23 Mar 1988)", link="Margaret Thatcher"),
 dict(id="thatcher-1988-04-07", voice="Margaret Thatcher", role="Prime Minister, first British PM on an official visit to Turkey; dinner speech in Ankara", c="United Kingdom", cn="United Kingdom",
      dom="politics", date="1988-04-07", era="posthumous", mirror="modernization-poster-child", pol="admiring", inten=2,
      saw="Names Atatürk a remarkable soldier-statesman and 'one of the towering figures of history', citing Kinross, and says he proves history is made by great men.",
      q="Our particular respect is reserved for that remarkable soldier/statesman Kemal Ataturk",
      art="speech", ev="P", med=None,
      cav="State-visit dinner given by Özal, so the praise is also hospitality. She says she re-read Lord Kinross's biography beforehand and quotes the phrase 'I don't act for public opinion, I act for the nation' (the Kinross attribution is hers; Kinross itself not opened here) and adds 'If ever one needed proof that history is made not by impersonal forces but by great men, Kemal Ataturk provided it.' Date is the Foundation's catalogue date; the document itself gives only 'Ankara' and a COI transcript.",
      src=["src_thatcher_107211.txt"], urls=[TH + "107211"],
      loc="Margaret Thatcher Foundation doc. 107211 (Speech at dinner given by Turkish PM, Ankara, Apr 1988)", link="Lord Kinross"),
]

bad = []
for r in R:
    full = bank(r["src"][0])
    q = norm(r["q"])
    if q not in full and q.replace(" ", "") not in full.replace(" ", ""):
        bad.append(r["id"])
if bad:
    sys.exit("quote not found in source bank: %s" % bad)
for r in R:
    assert len(r["saw"].split()) <= 25, (r["id"], len(r["saw"].split()))

with open(os.path.join(STATE, "gazes_westpost.jsonl"), "w", encoding="utf-8") as f:
    for r in R:
        rec = {"id": r["id"], "voice": r["voice"], "voice_type": "person", "role": r["role"], "country": r["c"],
               "country_now": r["cn"], "domain": r["dom"], "date": r["date"], "era": r["era"], "mirror": r["mirror"],
               "polarity": r["pol"], "intensity": r["inten"], "what_they_saw": r["saw"], "quote": r["q"],
               "artifact": r["art"], "evidence": r["ev"], "mediated_by": r["med"], "caveat": r["cav"],
               "node": NODE, "sources": r["urls"]}
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")

nxt = {"churchill-1929": "Page-check against a scan (djvu OCR); p. 418 line",
       "de-gaulle-1968-10-25": "Discours et messages vol. V and Anıtkabir Özel Defteri image",
       "de-gaulle-1968-10-27": "Discours et messages vol. V; Dolmabahçe book image",
       "roncalli-1938": "Italian original in Agende del Pontefice / Il Giornale dell'Anima; confirm entry date",
       "thatcher-1986-02-18": "none", "thatcher-1988-03-23": "none",
       "thatcher-1988-04-07": "Check Kinross for the 'I act for the nation' phrase; confirm date from Hansard-style press record"}
with open(os.path.join(STATE, "ledger_westpost.md"), "w", encoding="utf-8") as f:
    f.write("| Claim | Node | Status | Sources | Next step |\n|---|---|---|---|---|\n")
    for r in R:
        f.write("| %s (%s, %s): \"%s\" | %s | verified %s (%s) | %s | %s |\n" % (
            r["voice"], r["role"][:50], r["date"], r["q"][:110].replace("|", "/") + ("..." if len(r["q"]) > 110 else ""),
            NODE, r["ev"], r["loc"], "; ".join(r["urls"][:1]), nxt[r["id"]]))

person("Margaret Thatcher", role="Prime Minister of the United Kingdom, 1979–1990", nat="British", life="1925–2013",
       stance="admirer (diplomatic)", tags=["admirer", "verified"],
       body="""British Prime Minister who, in speeches and an interview around her April 1988 visit to Ankara (the first full official visit by a British premier), named Atatürk among the towering figures of history. See [[%s]] for the quotes.

## Sources
- Margaret Thatcher Foundation, docs. 106331, 107040, 107211, margaretthatcher.org.
""" % NODE)

body = ["""
Round 13 looked for Western statesmen and churchmen speaking about Atatürk after 1938 in their own words. Seven records
survived reading, from Churchill's memoir of 1929 through de Gaulle's visitor-book entries in October 1968 to Thatcher's
1986–88 speeches. Quotes were checked against the fetched source text before this note was written.

## The pattern

- **The former enemy writes the history:** [[Winston Churchill]] in *The Aftermath* (1929) is the first of the Western
  statesmen to give Kemal the title 'Man of Destiny', while describing the burning of Smyrna and the massacre with
  his army's name on it. The vault already holds his harder statement of 1920.
- **A state-builder reading himself into the mausoleum:** [[Charles de Gaulle]] in 1968 twice wrote Atatürk into the
  Turkish visitor books in the language of national renewal: the Anıtkabir and the Dolmabahçe entries.
- **The envoy who refused to hate:** Roncalli's diary after the death in 1938 ([[Pope John XXIII]]).
- **A prime minister's homework:** [[Margaret Thatcher]] told Özal's dinner in Ankara that she had re-read [[Lord Kinross]]
  and that Atatürk proved history is made by great men.
""".strip()]
for r in R:
    body.append("\n## %s (%s)\n" % (r["voice"], r["date"]))
    body.append("*%s*\n" % r["saw"])
    body.append("> %s\n" % r["q"])
    body.append("%s Location: %s. Evidence %s%s. See [[%s]].\n" % (r["cav"], r["loc"], r["ev"], (" (" + r["med"] + ")") if r["med"] else "", r["link"]))

body.append("""
## Not stored, and dry ends (round 13)

- **John Paul II, 28 Nov 1979:** the Holy See publishes his dedication in the Golden Book of the Anıtkabir (vatican.va, Spanish only): 'El gobierno de los pueblos está en las manos del Señor. El suscita en el momento oportuno los jefes que les conviene, porque el amor a la libertad y el respeto del derecho hacen grande a una nación, pero es Dios quien garantiza el porvenir.' It does not name Atatürk, so it states no view of him and is held out of the dataset.
- **Paul VI, July 1967:** the Istanbul addresses on vatican.va (airport, diplomatic corps) were read for 'Atatürk' and 'fondateur'; no mention.
- **Fidel Castro:** the bust and the 1961 Nâzım Hikmet–Nutuk story are covered in [[Fidel Castro]]; the new 'compared with our revolution, the entire cultural revolution made by Atatürk is far above this' line appears only on a blog (islaplus.com) and is not stored.
- **Kissinger, Perón, Vargas, Che Guevara:** nothing found in the open web search budget.

## Sources
- Winston S. Churchill, *The World Crisis: The Aftermath* (London: Thornton Butterworth, 1929), archive.org item in.ernet.dli.2015.209928.
- 'General De Gaulle'ün Türkiye'yi Ziyareti (25–30 Ekim 1968)', *Belleten* 51/200 (Aug 1987), belleten.gov.tr/tam-metin/1980/tur; INA, fresques.ina.fr/de-gaulle/fiche-media/Gaulle00146.
- Ezio Bolis, 'What Was John XXIII Really Like?', EWTN Library.
- Margaret Thatcher Foundation docs. 106331, 107040, 107211.
- John Paul II, Golden Book dedication, vatican.va/content/john-paul-ii/es/speeches/1979/november/documents/hf_jp-ii_spe_19791128_libro-oro-ataturk.html.
""")

note("Events", NODE,
     {"type": "event", "when": "1929–1988",
      "tags": ["event", "verified", "heads-of-state", "statesmen", "religion"]},
     "\n".join(body))
print("ok", len(R), "records")
