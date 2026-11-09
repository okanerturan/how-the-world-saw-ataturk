# -*- coding: utf-8 -*-
# Census round 18 (Nov 2026) — four poems on Ataturk by named poets, 1933-1939.
# Records: C. J. Dennis (Melbourne Herald, 1933), Amjad al-Tarabulsi (al-Risala no. 109, 5 Aug 1935),
# Mahmud Ghunaym (al-Risala no. 281, 21 Nov 1938), Nawab Sir Nizamat Jung (Islamic Culture, Jan 1939).
# Windows of every text are banked in tools/.state/round18/; the script refuses to run if a quote is not in its bank.
import json, os, re, sys, unicodedata
from _lib import note, person

HERE = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(HERE, "tools", ".state", "round18")
NODE = "Four Poems on Atatürk — Melbourne, Damascus, Cairo and Hyderabad, 1933–1939"


def norm(s):
    s = unicodedata.normalize("NFKC", s)
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"').replace("­", "")
    s = re.sub(r"[ً-ٟـ]", "", s)
    s = re.sub("[أإآٱ]", "ا", s).replace("ى", "ي").replace("ة", "ه")
    s = re.sub(r"[«»()\[\]]", " ", s)
    s = re.sub(r"[-¬]\s*\n", "", s)
    s = re.sub(r"\s+", " ", s)
    return s.strip().lower()


def bank(n):
    return norm(open(os.path.join(STATE, n), encoding="utf-8", errors="ignore").read())


MM = "http://middlemiss.org/lit/authors/denniscj/newspapers/herald/1933/works/kemal.html"
PC = "https://poetry.com/poem/6412/kemal---the-posh-pasha"
WS109 = "https://ar.wikisource.org/wiki/مجلة_الرسالة/العدد_109/أياصوفيا"
WS281 = "https://ar.wikisource.org/wiki/مجلة_الرسالة/العدد_281/أتاتورك"
IC = "https://archive.org/stream/in.ernet.dli.2015.92011/2015.92011.Islamic-Culturevol13january1939_djvu.txt"

R = [
 dict(id="cj-dennis-1933", voice="C. J. Dennis", role="Australian poet ('The Sentimental Bloke'), Melbourne Herald verse-writer",
      c="Australia", cn="Australia", dom="letters", date="1933", era="contemporary", mirror="modernization-poster-child",
      pol="admiring", inten=2, art="poem", ev="P", med=None, src="mm.txt",
      saw="Comic ode to 'Kemal - The Posh Pasha': sultans' scimitars and bow-strings gone, veils banished, a nation made 'wide-awake, up to date' by one man.",
      q="To the joy of the males he has banished the veils From the faces of Bosphorous belles.",
      cav="Light verse in Dennis's 'Den' signature, printed in the Melbourne Herald in 1933 (middlemiss.org's index lists it under 'Works in the Herald 1933'; the day was not given). Its headnote ties it to 'the 10th anniversary' of the Turkish republic (so late Oct or Nov 1933) and says Kemal 'fought against the Anzacs at Gallipoli, is spoken of by General Sir Harry Chauvel as a very great man' (headnote, so Dennis or the Herald's, and Chauvel's remark is reported, not sourced here). The Oriental clichés (harems, hookahs, bastinado) are the poem's own. Text verified on the Perry Middlemiss transcription of the Herald; the Herald page image itself (Trove) not seen.",
      urls=[MM, PC], loc="The Herald (Melbourne), 1933, 'Kemal - The Posh Pasha' (transcription at middlemiss.org)", link="C. J. Dennis"),
 dict(id="tarabulsi-1935", voice="Amjad al-Tarabulsi", role="Damascene poet and writer (signed 'Damascus')",
      c="Syria (French mandate)", cn="Syria", dom="letters", date="1935-08-05", era="contemporary", mirror="apostate",
      pol="hostile", inten=2, art="poem", ev="S", med=None, src="ws_fe1ea6.txt",
      saw="Rebukes Atatürk by name over Hagia Sophia: casting off the Arabs was ugly, casting off the faith uglier, and the West will devour him.",
      q="لئِنْ كان قُبحاً نَبْذكَ العُرْبَ جانباً ... فَنَبْذُك للدينِ المقَدَّسُ أقبح",
      cav="TRANSLATION (this record's): 'If your casting the Arabs aside was ugly, your casting aside the sacred faith is uglier.' Poem 'Ayasufya' (Hagia Sophia), a long qasida opening with an epigraph by Hafiz Ibrahim ('Ayasofya, the hour of parting has come'), printed in al-Risala (Cairo) no. 109, 5 Aug 1935, text from the Arabic Wikisource transcription of the issue; page number not given there. Atatürk is addressed twice by name ('Atatürk, do not let your command deceive you'; 'Atatürk, beware a leap from the sons of the West') and the second half of the poem is aimed at him, so he is the addressee, though the occasion is the church-mosque. Closes: 'Beware the West ... their peace is an armed peace.' The author is identified only by the signature 'Amjad al-Tarabulsi, Damascus'; his dates were not established.",
      urls=[WS109], loc="al-Risala (Cairo) no. 109, 5 Aug 1935, 'Ayasufya' by Amjad al-Tarabulsi (ar.wikisource transcription)", link="Amjad al-Tarabulsi"),
 dict(id="ghunaym-1938", voice="Mahmud Ghunaym", role="Egyptian poet and essayist (signs 'Kom Hamada')",
      c="Egypt", cn="Egypt", dom="letters", date="1938-11-21", era="funeral", mirror="nation-forge-template",
      pol="admiring", inten=2, art="poem", ev="S", med=None, src="ws_9d0084.txt",
      saw="Elegy: Kemal 'died on his bed like Ibn al-Walid', reviver of a dead nation above Mussolini and Hitler, though the caliphate troubles him.",
      q="ما مات فرد وورى بل هوى ... من أفقه فلك من الأفلاك",
      cav="TRANSLATION (this record's): 'It was no mere man who died and was buried: a sphere fell from its horizon among the spheres.' The essay-elegy 'Atatürk' (three verses, then prose) in al-Risala no. 281, 21 Nov 1938; Arabic from the Wikisource transcription of the issue, page not given there. Prose, verbatim: 'Mustafa died the death of Ibn al-Walid on his bed' (مات مصطفى ميتة ابن الوليد على فراشه). Admiring with reservations: he asks whether the Caliphate's end was an act of heresy or of surgery and leaves it to history, calls the Latin alphabet and hat 'imposed' and the regime a dictatorship he leans to approve while fearing for Turkey after him. Not the same issue or author as the al-Zayyat editorial of 14 Nov 1938, which is already in the dataset.",
      urls=[WS281], loc="al-Risala (Cairo) no. 281, 21 Nov 1938, 'Ataturk' by Mahmud Ghunaym (ar.wikisource transcription)", link="Mahmud Ghunaym"),
 dict(id="nizamat-jung-1939", voice="Nawab Sir Nizamat Jung", role="Hyderabad (Deccan) judge, scholar and poet; contributor to Islamic Culture",
      c="British India (Hyderabad State)", cn="India", dom="letters", date="1939-01", era="posthumous", mirror=None,
      pol="conflicted", inten=2, art="poem", ev="P", med=None, src="ic.txt",
      saw="Elegy: an outlaw who made a fallen nation great, 'relentless, heartless', a hero who defied Europe, his darkest deeds left to God's mercy.",
      q="Relentless, heartless — to be strong, With stormy will he strode along",
      cav="Original English verse, five quatrains headed '[Died on the 10th of November 1938] May he rest in peace!', in Islamic Culture (Hyderabad), vol. XIII no. 1, January 1939, p. 98 per the contents page (item VIII). Composition date within Nov 1938 - Jan 1939 inferred from the heading, so 'posthumous' by publication date only. Last stanza: 'A bearer of the Prophet's name! His darkest deeds God's mercy claim, Who gave him power - to save once more A Moslem nation's honour, fame.' Nizamat Jung (1871-1955) is placed from memory (tier M); the volume gives only his name and title. Text read from the open archive.org OCR (identifier in.ernet.dli.2015.92011).",
      urls=[IC], loc="Islamic Culture (Hyderabad) 13/1, Jan 1939, p. 98, 'Ghazi Mustapha Kamal Pasha - A Poem'", link="Nizamat Jung"),
]

bad = []
for r in R:
    if norm(r["q"]) not in bank(r["src"]):
        bad.append(r["id"])
if bad:
    sys.exit("quote not found in source bank: %s" % bad)
for r in R:
    assert len(r["saw"].split()) <= 25, (r["id"], len(r["saw"].split()))

with open(os.path.join(STATE, "gazes_poems.jsonl"), "w", encoding="utf-8") as f:
    for r in R:
        rec = {"id": r["id"], "voice": r["voice"], "voice_type": "person", "role": r["role"],
               "country": r["c"], "country_now": r["cn"], "domain": r["dom"], "date": r["date"], "era": r["era"],
               "mirror": r["mirror"], "polarity": r["pol"], "intensity": r["inten"], "what_they_saw": r["saw"],
               "quote": r["q"], "artifact": r["art"], "evidence": r["ev"], "mediated_by": r["med"], "caveat": r["cav"],
               "node": NODE, "sources": r["urls"]}
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")

nxt = {"cj-dennis-1933": "Trove: Herald (Melbourne) Oct-Nov 1933 page image for the exact date; Chauvel's own words on Kemal (Chauvel papers, AWM)",
       "tarabulsi-1935": "Amjad al-Tarabulsi's diwan or Risala print page 1935; author's dates; other replies to the Hagia Sophia conversion in al-Risala/al-Fath",
       "ghunaym-1938": "Print page in al-Risala vol. 6 (1938); Ghunaym's later diwan",
       "nizamat-jung-1939": "Islamic Culture p. 98 scan check; Nizamat Jung's dates from a biography; Hyderabad Urdu press Nov 1938"}
with open(os.path.join(STATE, "ledger_poems.md"), "w", encoding="utf-8") as f:
    f.write("| Claim | Node | Status | Sources | Next step |\n|---|---|---|---|---|\n")
    for r in R:
        f.write("| %s (%s, %s): \"%s\" | %s | verified %s (%s) | %s | %s |\n" % (
            r["voice"], r["role"], r["date"], r["q"].replace("|", "/"), NODE, r["ev"], r["loc"], r["urls"][0], nxt[r["id"]]))

# ---- vault notes
for r in R:
    pass
person("C. J. Dennis", role="Australian poet; Melbourne Herald verse-writer", nat="Australian", life="1876–1938", stance="admiring (comic ode, 1933)",
       tags=["poet", "australia", "verified", "contemporary"],
       body="""Clarence Michael James Stanislaus Dennis wrote *The Songs of a Sentimental Bloke* and, from the 1920s, daily light verse for the Melbourne *Herald*. In 1933 he
turned the Turkish republic's tenth anniversary into a comic ode, *Kemal - The Posh Pasha*. See [[Four Poems on Atatürk — Melbourne, Damascus, Cairo and Hyderabad, 1933–1939]].

## Sources
- The Herald (Melbourne) 1933, transcription: %s
""" % MM)
person("Amjad al-Tarabulsi", role="Damascene poet", nat="Syrian", life="", stance="hostile (1935 Hagia Sophia ode)",
       tags=["poet", "syria", "verified", "contemporary", "arabic-primary"],
       body="""Signs 'Damascus'. His long qasida on Hagia Sophia, printed in *al-Risala* (Cairo) in August 1935, turns on Atatürk himself. See [[Four Poems on Atatürk — Melbourne, Damascus, Cairo and Hyderabad, 1933–1939]], [[Abolition of the Caliphate]].

## Sources
- al-Risala no. 109, 5 Aug 1935: %s
""" % WS109)
person("Mahmud Ghunaym", role="Egyptian poet and essayist", nat="Egyptian", life="", stance="admiring with reservations (Nov 1938)",
       tags=["poet", "egypt", "verified", "funeral", "arabic-primary"],
       body="""Signs 'Kom Hamada'. In *al-Risala* of 21 November 1938 he printed three verses and an essay on the death. See [[Four Poems on Atatürk — Melbourne, Damascus, Cairo and Hyderabad, 1933–1939]], [[Ahmad Hasan al-Zayyat]], [[Death and State Funeral of Atatürk]].

## Sources
- al-Risala no. 281, 21 Nov 1938: %s
""" % WS281)
person("Nizamat Jung", role="Hyderabad judge, scholar and poet", nat="Indian (Hyderabad State)", life="", stance="conflicted (January 1939 elegy)",
       tags=["poet", "india", "verified", "posthumous"],
       body="""Contributor to *Islamic Culture* (Hyderabad), whose first number of the new Hyderabad series (January 1939) closes its articles with his English poem on Mustafa Kemal. See [[Four Poems on Atatürk — Melbourne, Damascus, Cairo and Hyderabad, 1933–1939]], [[Death and State Funeral of Atatürk]].

## Sources
- Islamic Culture 13/1 (Jan 1939), p. 98: %s
""" % IC)

body = """Four poems by named poets, from four continents' worth of readers, each read from a text and quoted at two lines or fewer.

## C. J. Dennis, 'Kemal - The Posh Pasha' (Melbourne Herald, 1933)

*%(a)s*

> %(aq)s

A comic ode in the Sentimental Bloke's own idiom: scimitars, bow-strings and hookahs are 'memories dim' since the Turks 'learned pep and vim' from Kemal, and the old die-hards 'sigh for the days of the fez'. The headnote ties it to the republic's tenth anniversary and to Gallipoli. See [[C. J. Dennis]], [[Gallipoli Campaign]], [[Hat Law]].

## Amjad al-Tarabulsi, 'Ayasufya' (al-Risala, 5 August 1935)

*%(b)s*

> %(bq)s
> (translation: 'If your casting the Arabs aside was ugly, your casting aside the sacred faith is uglier.')

A hostile qasida over the closing of Hagia Sophia as a place of worship: it tells Atatürk not to be fooled by his obeyed rule, that the West loves as the wolf loves the sheep, and that the East will be fattened and slaughtered by it. See [[Amjad al-Tarabulsi]], [[Abolition of the Caliphate]].

## Mahmud Ghunaym, 'Atatürk' (al-Risala, 21 November 1938)

*%(c)s*

> %(cq)s
> (translation: 'It was no mere man who died and was buried: a sphere fell from its horizon among the spheres.')

Three verses of elegy followed by an essay that calls him a reviver of the dead and weighs the abolition of the caliphate. See [[Mahmud Ghunaym]], [[Ahmad Hasan al-Zayyat]] for the editor's own piece a week earlier.

## Nizamat Jung, 'Ghazi Mustapha Kamal Pasha' (Islamic Culture, January 1939)

*%(d)s*

> %(dq)s

An English elegy that does not hide its unease: 'Heedless alike of right and wrong', yet a hero who defied Europe, and whose 'darkest deeds God's mercy claim'. See [[Nizamat Jung]].

## Sources
%(src)s
""" % dict(a=R[0]["saw"], aq=R[0]["q"], b=R[1]["saw"], bq=R[1]["q"], c=R[2]["saw"], cq=R[2]["q"], d=R[3]["saw"], dq=R[3]["q"],
           src="\n".join("- %s: %s" % (r["loc"], r["urls"][0]) for r in R))
note("Events", NODE, {"type": "event", "when": "1933–1939", "tags": ["event", "verified", "poets", "arabic-primary"]}, body)
print("ok", len(R))
