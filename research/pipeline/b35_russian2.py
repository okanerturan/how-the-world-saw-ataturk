# -*- coding: utf-8 -*-
# Census round 26 (Nov 2026) - Soviet leaders in their own words: Voroshilov (Ankara, Oct 1933, Pravda 28 and 29 Oct, read on page images
# re-OCRed/viewed from archive.org PDFs 1933298_9664 and 1933299_3244) and Frunze (report on return from Ankara, 1922, Istoricheskii arkhiv 1960 no. 6).
# Banks in tools/.state/round26/. Voroshilov banks are my transcription from the page image (no machine text is clean); Frunze bank is archive.org djvu text.
import json, os, re, sys, unicodedata
from _lib import note

HERE = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(HERE, "tools", ".state", "round26")
NODE = "Soviet Marshals Greet the Ghazi — Voroshilov in Ankara 1933 and Frunze 1922"


def norm(s):
    s = unicodedata.normalize("NFKC", s).replace("ё", "е")
    s = re.sub(r"(\w)[-¬]\s+(\w)", r"\1\2", s)
    s = re.sub(r"\s+", " ", s)
    return s.strip().lower()


def bank(f):
    return norm(open(os.path.join(STATE, f), encoding="utf-8").read())


P298 = "https://archive.org/details/1933298_9664"
P299 = "https://archive.org/details/1933299_3244"
IA = "https://archive.org/details/istoricheskii-arkhiv-1955_1960_6"

R = [
 dict(id="voroshilov-1933-10-27", voice="Kliment Voroshilov", role="Soviet People's Commissar for Military and Naval Affairs, head of the delegation to the Republic's 10th anniversary",
      c="Soviet Union", cn="Russia", dom="politics", date="1933-10-27", era="contemporary", mirror="anti-colonial-liberator",
      pol="instrumental", inten=2, art="speech", ev="P", f="voroshilov_pravda299.txt",
      saw="Closing his reply to Ismet Pasha in Ankara, salutes Kemal as leader of the national-liberation struggle, tied to both victory and cultural revival.",
      q="Заканчивая свою речь, я выражаю глубокое уважение народов СССР к вождю национально-освободительной борьбы турецкого народа — президенту Турецкой республики Гази Мустафа Кемаль-паше, со славным именем которого связаны как победоносная борьба новой Турции за свою независимость, так и упорная созидательная работа над ее культурным и экономическим возрождением.",
      tr="Concluding my speech, I express the deep respect of the peoples of the USSR for the leader of the Turkish people's national-liberation struggle, President of the Turkish Republic Gazi Mustafa Kemal Pasha, whose glorious name is linked both with the new Turkey's victorious struggle for independence and with the persistent creative work of its cultural and economic revival.",
      src=P299,
      cav="Правда no. 299 (5825), 29 Oct 1933, p. 2, 'Ответная речь тов. Ворошилова' (TASS dispatch from Ankara dated 27 Oct; reply to Ismet Pasha at the dinner on arrival; the sentence closes the speech, before the toast 'за здоровье президента республики'). Read on the page image (300 dpi crop of the archive.org scan; the archive's own OCR is garbage). Official toast at a state visit, so polarity 'instrumental'; text as published by Pravda from TASS, not a stenogram. Page and issue date as printed in the header."),
 dict(id="voroshilov-1933-10-26", voice="Kliment Voroshilov", role="Soviet People's Commissar for Military and Naval Affairs, head of the delegation to the Republic's 10th anniversary",
      c="Soviet Union", cn="Russia", dom="politics", date="1933-10-26", era="contemporary", mirror=None,
      pol="instrumental", inten=1, art="quote", ev="P", f="voroshilov_pravda298.txt",
      saw="In a statement to the Turkish press on landing at Istanbul, says he is especially glad to meet 'the great leader of the new Turkey'.",
      q="Я особенно рад возможностью лично встретить великого вождя новой Турции многоуважаемого президента республики Мустафа Кемаль-пашу",
      tr="I am especially glad of the chance to meet personally the great leader of the new Turkey, the highly esteemed President of the Republic, Mustafa Kemal Pasha",
      src=P298,
      cav="Правда no. 298 (5824), 28 Oct 1933, p. 1, 'Заявление тов. Ворошилова' (TASS, Istanbul, 26 Oct; statement to the Turkish press). Read on the page image. Courtesy greeting on arrival, the sentence continues with Ismet Pasha and Tevfik Rustu Aras; intensity 1. Quoted words are the published (TASS) text."),
 dict(id="frunze-1922", voice="Mikhail Frunze", role="Soviet commander, extraordinary ambassador of Soviet Ukraine to Ankara (Dec 1921), later People's Commissar for Military Affairs",
      c="Soviet Union", cn="Russia", dom="military", date="1922", era="contemporary", mirror=None,
      pol="instrumental", inten=1, art="report", ev="P", f="frunze_ia1960.txt",
      saw="Reporting home from Ankara, cites Kemal first among Turkish leaders who stress friendship and are working to strengthen it.",
      q="Турецкое правительство, начиная от его главы Мустафы Кемаль-паши и кончая депутатами собрания, которое самым недвусмысленным образом подчеркивало свою дружбу и верность принятым обязательствам",
      tr="The Turkish government, from its head Mustafa Kemal Pasha down to the deputies of the Assembly, which has most unambiguously stressed its friendship and loyalty to the obligations undertaken",
      src=IA,
      cav="Frunze's report to the joint session of the Presidium of the VUTsIK and the Council of People's Commissars of Ukraine after his return from Ankara, published as 'О миссии М. В. Фрунзе в Турцию в 1921-1922 гг.', Исторический архив 1960 no. 6, p. 35 (report pp. 31-36; open archive.org scan, djvu text read). Exact meeting date not printed in the passage read (early 1922). This is a diplomatic report on policy, not his private diary: the Ankara diary 'Поездка в Ангору' (Соч. т. I, 1929) was not found open. Frunze also says (p. 35) that Kemal's government will not turn against the USSR."),
]
bad = [r["id"] for r in R if norm(r["q"]) not in bank(r["f"])]
if bad:
    sys.exit("quote not found in source bank: %s" % bad)
for r in R:
    print(r["id"], len(r["saw"].split()))

with open(os.path.join(STATE, "gazes_russian2.jsonl"), "w", encoding="utf-8") as f:
    for r in R:
        rec = {"id": r["id"], "voice": r["voice"], "voice_type": "person", "role": r["role"],
               "country": r["c"], "country_now": r["cn"], "domain": r["dom"], "date": r["date"], "era": r["era"],
               "mirror": r["mirror"], "polarity": r["pol"], "intensity": r["inten"], "what_they_saw": r["saw"],
               "quote": r["q"] + " [translation: " + r["tr"] + "]", "artifact": r["art"], "evidence": r["ev"],
               "mediated_by": None, "caveat": r["cav"], "node": NODE, "sources": [r["src"]]}
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")

with open(os.path.join(STATE, "ledger_russian2.md"), "w", encoding="utf-8") as f:
    f.write("| Claim | Node | Status | Sources | Next step |\n|---|---|---|---|---|\n")
    f.write("| Voroshilov, Pravda 299 (29 Oct 1933) p. 2, reply at Ankara: Kemal 'вождь национально-освободительной борьбы' | %s | verified P (page image read) | %s | Check Izvestia same day and DVP SSSR XVI for the stenogram | \n" % (NODE, P299))
    f.write("| Voroshilov, Pravda 298 (28 Oct 1933) p. 1, Istanbul statement: 'великого вождя новой Турции' | %s | verified P (page image read) | %s | none | \n" % (NODE, P298))
    f.write("| Frunze, report 1922 (Ist. arkhiv 1960 no. 6, p. 35): Kemal and government stress friendship | %s | verified P (open djvu text) | %s | Find Соч. т. I diary 'Поездка в Ангору' | \n" % (NODE, IA))

body = """Two Soviet military leaders on Mustafa Kemal in their own published words, both courtesy-diplomatic in register.

## Kliment Voroshilov, Ankara, October 1933

At the dinner of Ismet Pasha on arrival, Voroshilov (see [[Kliment Voroshilov]]) closed his reply with this, as printed in *Правда* no. 299, 29 Oct 1933, p. 2:

> %s
> (translation: %s)

On landing at Istanbul two days before he told the Turkish press, *Правда* no. 298, 28 Oct 1933, p. 1:

> %s
> (translation: %s)


*Census check (5 Nov 2026): Frunze's 1922 report is kept as context but not counted as a gaze — Kemal is named only as head of a list of Turkish leaders.*

## Mikhail Frunze, report on the Ankara mission, 1922

Frunze (see [[Mikhail Frunze]]) reporting to the Ukrainian VUTsIK and Sovnarkom, *Исторический архив* 1960 no. 6, p. 35:

> %s
> (translation: %s)

## Sources
- Pravda 299: %s
- Pravda 298: %s
- Istoricheskii arkhiv 1960 no. 6: %s
""" % (R[0]["q"], R[0]["tr"], R[1]["q"], R[1]["tr"], R[2]["q"], R[2]["tr"], P299, P298, IA)
note("Events", NODE, {"type": "event", "when": "1922–1933", "tags": ["event", "verified", "russia", "russian-primary"]}, body)
print("ok")
