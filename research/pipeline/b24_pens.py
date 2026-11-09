# -*- coding: utf-8 -*-
# Census round 15 (Nov 2026) — famous pens in their own words, third pass, using archive.org full-text search (tools/fts.py)
# to find passages inside books, then open scans (DLI, Internet Archive) to read them.
# Records: Claude Farrère (1921 preface; 1937 essay in Turkish translation), Halide Edib (Turkey Faces West, 1930),
# Arnold Toynbee (A Study of History vol. VI 1939, vol. VIII 1954), Orhan Pamuk (Other Colors, 2007; snippet only),
# Aziz Nesin (letter to Tahsin Saraç, 9/10 May 1987).  Windows of every open text are banked in tools/.state/round15/.
import json, os, re, sys
from _lib import note, person

HERE = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(HERE, "tools", ".state", "round15")
NODE = "Famous Pens on Atatürk II — Farrère, Halide Edib, Toynbee, Pamuk, Nesin"


def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"').replace("­", "")
    s = re.sub(r"[-¬]\s*\n", "", s)
    s = re.sub(r"(\w)- (\w)", r"\1\2", s)
    s = re.sub(r"\s+", " ", s)
    return s


def bank(n):
    return norm(open(os.path.join(STATE, n), encoding="utf-8").read())


FAR21 = "https://archive.org/details/lextraordinairea00farr"
FARTR = "https://archive.org/details/claude-farrere-turklerin-manevi-gucu"
HAL30 = "https://archive.org/details/in.ernet.dli.2015.183553"
TOY6 = "https://archive.org/details/in.ernet.dli.2015.208032"
TOY8 = "https://archive.org/details/in.ernet.dli.2015.57280"
PAM = "https://archive.org/details/othercolorsessay00pamu"
NES = "https://archive.org/details/aziz-nesin-kac-aptaliz"

R = [
 dict(id="farrere-1921", voice="Claude Farrère", role="French novelist and former naval officer", c="France", cn="France",
      dom="letters", date="1921", era="contemporary", mirror="chivalrous-enemy", pol="admiring", inten=2,
      saw="Says that were he not French he would fight for Turkey against Greece and England 'aux côtés de mon ami d'Angora, Kemal-pacha'.",
      q="aux côtés de mon ami d'Angora, Kemal-pacha", qbank="aux côtés de mon ami d'Augora, Kemal-pacha",
      art="book", ev="P", med=None,
      cav="Preface (dated in the text to 1921, at the height of the Franco-Turkish quarrel over Cilicia and Syria) to L'extraordinaire aventure d'Achmet pacha Djemaleddine (Flammarion, 1921), p. xviii (the passage ends just above the running head 'AVANT-PROPOS XIX'). The archive.org OCR misreads 'Angora' as 'Augora'; the Turkish translation of the same preface in the Tercüman edition (archive.org claude-farrere-turklerin-manevi-gucu, p. 22) reads 'Ankaralı dostum Kemal Paşa', which fixes the reading. The full sentence: 'si je n'étais Français, de quel bon coeur je me battrais pour la Turquie contre la Grèce, contre l'Angleterre, contre à peu près toute l'Europe, aux côtés de mon ami d'Angora, Kemal-pacha!' Elsewhere in the volume a story's text calls Kemal Gazi 'l'admirable' (p. 156-157), but that line sits inside the fiction and is not counted. The existing People note says Farrère met Kemal in 1922 (his later account, Souvenirs 1953, snippet only, says he met the ghazi 'au lendemain de la Sakharia', i.e. late 1921).",
      src="src_farrere_1921.txt", urls=[FAR21],
      loc="L'extraordinaire aventure d'Achmet pacha Djemaleddine (1921), Avant-propos, p. xviii", link="Claude Farrère and Pierre Loti"),
 dict(id="farrere-1937", voice="Claude Farrère", role="French novelist and former naval officer", c="France", cn="France",
      dom="letters", date="1937", era="contemporary", mirror="modernization-poster-child", pol="conflicted", inten=2,
      saw="Approves Gazi Mustafa Kemal's modernizing and forgives his mistakes as the price of doing anything; faults the republicans for scorning their Ottoman ancestors.",
      q="Bu bakımdan Gazi Mustafa Kemal'i tasvip ediyor ve hatalarından ötürü onu suçlu bulmuyorum.", qbank=None,
      art="book", ev="S", med="Orhan Bahaeddin's Turkish translation (Tercüman '1001 Temel Eser', 1970s); the French original was not seen",
      cav="TRANSLATION, quote is the Turkish text; in English: 'In this respect I approve of Gazi Mustafa Kemal, and I do not hold him guilty for his mistakes.' From the second work in the volume, Türkiye'nin Manevi Kuvvetleri ('The Moral Forces of Turkey'), which the Tercüman introduction says was first published in 1937; the page is printed 212, in a passage where Farrère adds that Turkish women have nothing to complain of 'but that does not mean there is nothing for them to complain of'. Same book, p. 209-210: he deplores that 'Gazi Mustafa Kemal - let us call him Atatürk from now on - and the republican Turks began to despise their forefathers' heritage' ('Buna hakları yok'), and mocks the change of the battleship Yavuz Sultan Selim to plain Yavuz. Evidence S rather than P because it is a translation of a book whose French text was not read; the dating to 1937 rests on the editor's note. Not yet found: the French title and edition (Farrère's 1937 volume).",
      src="src_farrere_tr.txt", urls=[FARTR],
      loc="Türkiye'nin Manevi Kuvvetleri (Tercüman edition), p. 212 (also pp. 209-210)", link="Claude Farrère and Pierre Loti"),
 dict(id="halide-edib-1930", voice="Halide Edib", role="Turkish novelist and nationalist, then in exile", c="Turkey (in exile)", cn="Turkey",
      dom="letters", date="1930", era="contemporary", mirror="internal-mirror", pol="conflicted", inten=2,
      saw="Calls his push for the 1925 Law on the Maintenance of Order a 'superb political game' that turned a democracy into a dictatorship.",
      q="Then Mustafa Kemal Pasha played a superb political game.", qbank=None,
      art="book", ev="P", med=None,
      cav="Turkey Faces West: A Turkish View of Recent Changes and Their Origin (Yale University Press, 1930; the frontispiece credits the Institute of Politics, Williamstown), ch. 'The Turkish Republic', p. 220 (the next running head is 221; scan archive.org in.ernet.dli.2015.183553, a Digital Library of India copy). The context is the March 1925 Law on the Maintenance of Order, after which 'the tribunals suppressed opposition and instituted a reign of terror which lasted nearly two years' and 'the moral responsibility ... rests on the majority in the National Assembly'. She adds, p. 222, that the personality of Mustafa Kemal 'played a great role' but that he, like any 'Great man', was carried by a wave, and, p. 182, that 'few men ... have shown better judgment and capacity than Mustafa Kemal Pasha' on the military and foreign-policy lines. Sensitive thread (Kurdish revolt, Independence Tribunals): the voice is hers, not the vault's.",
      src="src_halide_1930.txt", urls=[HAL30],
      loc="Turkey Faces West (Yale UP, 1930), 'The Turkish Republic', p. 220 (also pp. 182, 221-222)", link="Halide Edib Adıvar"),
 dict(id="toynbee-1939", voice="Arnold J. Toynbee", role="British historian, A Study of History", c="United Kingdom", cn="United Kingdom",
      dom="letters", date="1939", era="posthumous", mirror="nation-forge-template", pol="admiring", inten=2,
      saw="Calls Atatürk's purge of Arabic and Persian words from Turkish a task 'none but a hero could grapple' with, and the 'third Ottoman saviour'.",
      q="the Ghazi set himself a task with which none but a hero could grapple", qbank=None,
      art="book", ev="P", med=None,
      cav="A Study of History vol. VI (Oxford UP, 1939; scan in.ernet.dli.2015.208032), 'The Disintegration of Civilizations', p. 68 (language reform). Toynbee does not spare the method: he says Mustafa Kemal 'had evicted from Turkey an old-established and apparently indispensable Greek and Armenian middle class' on the calculation that the vacuum would force the Turks to do their own work, and he treats the language purge on the same principle ('what an astonishing intellectual stimulus can be given to mentally sluggish peoples (such as his Turks and our English are)'). Same volume, p. 222: 'A totalitarian Westernizer was needed ... in our own day this third Ottoman saviour has appeared in the person of President Mustafa Kemal Ataturk.' The volume appeared in 1939 and was written before Atatürk's death; date and era follow the publication. Adds to the existing 1922 record (Western Question), which is guarded. Sensitive thread (Greek and Armenian populations): Toynbee's framing is recorded as his, not the vault's.",
      src="src_toynbee_v6.txt", urls=[TOY6],
      loc="A Study of History vol. VI (1939), p. 68 (also p. 222)", link="Arnold J. Toynbee"),
 dict(id="toynbee-1954", voice="Arnold J. Toynbee", role="British historian, A Study of History", c="United Kingdom", cn="United Kingdom",
      dom="letters", date="1954", era="posthumous", mirror="nation-forge-template", pol="admiring", inten=2,
      saw="Names his refusal of the Pan-Turan mirage, a visionary march into collision with Russia, 'one of the most signal evidences' of Atatürk's political genius.",
      q="One of the most signal evidences of Ghazi Mustafa Kemal Ataturk's political genius was his clear recognition that a visionary pursuit of this mirage of a Yeni Turan", qbank=None,
      art="book", ev="P", med=None,
      cav="A Study of History vol. VIII (Oxford UP, 1954; the archive.org scan in.ernet.dli.2015.57280 is catalogued 1939 but contains the 1954 text), 'Encounters between Contemporaries', p. 191. The sentence goes on: '... beyond the eastern limits of an Ottoman Turkish national home in Anatolia was bound to bring Turkey into a disastrous headlong collision with a Russia ...'. Same volume, p. 192, Toynbee ends a Greek-Turkish passage with 'the statesmanship of Eleftherios Venizelos and Mustafa Kemal Atatürk', and on p. 262 ff. a section is titled 'The Success of Mustafa Kemal Atatürk in Creating a Turkish National State' (not read here). He lists Atatürk among 'Herodian' figures, with Mehmed Ali, Mahmud II and Reza Shah, in vol. VIII too.",
      src="src_toynbee_v8.txt", urls=[TOY8],
      loc="A Study of History vol. VIII (1954), p. 191 (also p. 192)", link="Arnold J. Toynbee"),
 dict(id="pamuk-2007", voice="Orhan Pamuk", role="Turkish novelist, Nobel laureate 2006", c="Turkey", cn="Turkey",
      dom="letters", date="2007", era="posthumous", mirror="internal-mirror", pol="admiring", inten=2,
      saw="In an essay on Gide's Turkish travels, reads the Hat Law as Atatürk 'striking at the heart of shame' about Turkish clothing before Europeans.",
      q="Ataturk found a way of confronting the shame suffered by all", qbank=None,
      art="article", ev="S", med=None,
      cav="Other Colors: Essays and a Story (Knopf, 2007), the essay 'Andre Gide' (index p. 204; the hat and dress passage falls c. pp. 205-209; the printed page of the sentence is not shown by the snippet). The text is read only as archive.org full-text snippets of a lending item (othercolorsessay00pamu), so the sentence is cut off after 'by all'. Other snippets from the same essay: 'Both Gide and Ataturk see the ugly clothing worn by the Turks'; 'But Ataturk believed that Turkish apparel misrepresented the nation'; the Hat Law is 'in a sense, a way of striking at the heart of shame'; 'Ataturk draws a line between the costume that he rejects ...'. His long Istanbul memoir (2005) gives a more hostile mood (the 'staunch disciples of Ataturk who dominated the press', 'the prohibitions of the Ataturk era') but a snippet was too short to quote as a view of the man. Polarity 'admiring' is the nearest enum for a sympathetic explanation of the reform; it rests on a short excerpt, so treat it as provisional until the printed essay is read.",
      src="src_pamuk_snippet.txt", urls=[PAM],
      loc="Other Colors (2007), essay 'Andre Gide', c. pp. 205-209", link="Orhan Pamuk"),
 dict(id="nesin-1987", voice="Aziz Nesin", role="Turkish satirist and writer", c="Turkey", cn="Turkey",
      dom="letters", date="1987-05", era="posthumous", mirror="internal-mirror", pol="admiring", inten=2,
      saw="In a private letter, counts Mustafa Kemal among Turkey's marvels and the one that astonishes him most, a genius 'despite all his human shortcomings'.",
      q="Ben en çok Mustafa Kemal'e şaşarım", qbank=None,
      art="memoir", ev="P", med=None,
      cav="TRANSLATION of the gloss only; the quote is Turkish. 'I am most astonished by Mustafa Kemal, how such a genius could climb out of that rotten swamp ... despite all his human shortcomings.' Letter of 9/10 May 1987 to the critic Tahsin Saraç, in Aziz Nesin - Tahsin Saraç Mektuplaşmaları (Düşün Yayıncılık, 1995), pp. 131-132 (archive.org aziz-nesin-kac-aptaliz, OCR). Nesin adds: 'Biz küçümencik, adını anmaya değmez işleri kotaramazken - hem de ondan altmış yıl sonra - nasıl yaratmış o mucizeyi' (we cannot manage tiny things sixty years later, how did he create that miracle). The letter's context is the row over claiming Ibn Sina and Mimar Sinan as Turks; Nesin jokes that someday they will take 'Bosnian-descended Mustafa Kemal' too. A different letter in the same book (7 Dec 1988) calling Atatürk 'gerçekten dahi' is Saraç's, not Nesin's, and is not used. Nesin, a satirist who spent years in prison and was otherwise sharp about Atatürk-worship, is the ambivalent internal voice here.",
      src=os.path.join("nesin", "Aziz Nesin - Tahsin Saraç Mektuplaşmaları.txt"), urls=[NES],
      loc="Aziz Nesin - Tahsin Saraç Mektuplaşmaları (1995), pp. 131-132 (letter of 9/10 May 1987)", link="Aziz Nesin"),
]

bad = []
for r in R:
    full = bank(r["src"])
    q = norm(r["qbank"] or r["q"])
    if q not in full:
        bad.append(r["id"])
if bad:
    sys.exit("quote not found in source bank: %s" % bad)
for r in R:
    assert len(r["saw"].split()) <= 25, (r["id"], len(r["saw"].split()))

with open(os.path.join(STATE, "gazes_pens.jsonl"), "w", encoding="utf-8") as f:
    for r in R:
        rec = {"id": r["id"], "voice": r["voice"], "voice_type": "person", "role": r["role"], "country": r["c"],
               "country_now": r["cn"], "domain": r["dom"], "date": r["date"], "era": r["era"], "mirror": r["mirror"],
               "polarity": r["pol"], "intensity": r["inten"], "what_they_saw": r["saw"], "quote": r["q"],
               "artifact": r["art"], "evidence": r["ev"], "mediated_by": r["med"], "caveat": r["cav"],
               "node": NODE, "sources": r["urls"]}
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")

nxt = {"farrere-1921": "Souvenirs (1953, bwb_P9-BJT-078, lending) for the 1921 meeting with the Ghazi; Farrère's newspaper pieces 1921-22 on Gallica",
       "farrere-1937": "Find the French original and its title/date (Farrère 1937); verify page against it",
       "halide-edib-1930": "None; compare with The Turkish Ordeal (1928) record",
       "toynbee-1939": "Read the whole of vol. VI footnotes on Kemal (pp. 67-68, 222); Survey of International Affairs 1925 vol. I for the 1925 verdict",
       "toynbee-1954": "Vol. VIII p. 262 ff 'The Success of Mustafa Kemal Atatürk in Creating a Turkish National State'",
       "pamuk-2007": "Read the printed essay 'André Gide' in Other Colors; Pamuk's Nobel lecture and Istanbul (2005) pp. 116, 123, 157-158",
       "nesin-1987": "Aziz Nesin's journal 1958-1995 (Düşün 1996) and his essays on Atatürk for a second voice"}
with open(os.path.join(STATE, "ledger_pens.md"), "w", encoding="utf-8") as f:
    f.write("| Claim | Node | Status | Sources | Next step |\n|---|---|---|---|---|\n")
    for r in R:
        f.write("| %s (%s, %s): \"%s\" | %s | verified %s (%s) | %s | %s |\n" % (
            r["voice"], r["role"][:50], r["date"], r["q"][:110].replace("|", "/") + ("..." if len(r["q"]) > 110 else ""),
            NODE, r["ev"], r["loc"], "; ".join(r["urls"][:1]), nxt[r["id"]]))

person("Orhan Pamuk", role="Turkish novelist, Nobel laureate in literature 2006", nat="Turkish", life="b. 1952",
       stance="sympathetic analyst, wary of the cult", tags=["writer", "internal-mirror", "verified"],
       body="""Istanbul novelist whose *Snow* (2002) fills a provincial town with Atatürk monuments and 'Atatürk and painting' lectures, and whose memoir *Istanbul* (2003) remembers the 'staunch disciples of Atatürk' who ran the press. In his essay on André Gide's Turkish travels in *Other Colors* (2007) he reads the Hat Law as a way of 'striking at the heart of shame', Atatürk finding 'a way of confronting the shame suffered by all' Turks. See [[%s]] and [[Hat Law]].

## Sources
- Orhan Pamuk, *Other Colors* (Knopf, 2007), essay 'Andre Gide' (archive.org full-text snippets, othercolorsessay00pamu).
- Orhan Pamuk, *Istanbul: Memories and the City* (2005), index entries for Atatürk (snippets only).
""" % NODE)

person("Aziz Nesin", role="Turkish satirist, novelist and humorist", nat="Turkish", life="1915–1995",
       stance="astonished, unsentimental", tags=["writer", "internal-mirror", "verified"],
       body="""Turkey's best-known satirist, jailed under several governments. His private letters to the critic Tahsin Saraç, published as *Aziz Nesin - Tahsin Saraç Mektuplaşmaları* (1995), include, in May 1987, a list of what he is glad Turkey has: Nasreddin Hoca, Yunus, Sinan, Nâzım, and Mustafa Kemal. 'Ben en çok Mustafa Kemal'e şaşarım' ('Mustafa Kemal astonishes me most'), he writes, a genius who rose out of that swamp 'despite all his human shortcomings'. See [[%s]] and [[Nâzım Hikmet]].

## Sources
- Aziz Nesin and Tahsin Saraç, *Mektuplaşmaları* (Düşün Yayıncılık, 1995), pp. 131-132 (archive.org aziz-nesin-kac-aptaliz, OCR).
""" % NODE)

TOY_Q = {r["id"]: r for r in R}
body = """
Round 15 asked a free archive.org full-text search (tools/fts.py) what famous pens had said about Atatürk inside books still
in copyright, then read the open scans where there were any. Seven records were staged. Most of the famous names produced
nothing usable (see the candidates file), but five voices stated a view in their own words.

## Claude Farrère (1921 and 1937)

*%(f21)s*

> %(f21q)s

The French naval officer turned novelist put it in a 1921 preface, in the middle of France's own quarrel with Ankara
over Cilicia: were he not French, he would fight for Turkey against Greece and England 'aux côtés de mon ami d'Angora,
Kemal-pacha'. Sixteen years later, in the book published in Turkish as *Türkiye'nin Manevi Kuvvetleri* (translation,
quoted in Turkish), he is more reserved. %(f37)s He also scolds the republicans for scorning the Ottoman inheritance.
See [[Claude Farrère and Pierre Loti]].

## Halide Edib (1930), a 'superb political game'

*%(h30)s*

> %(h30q)s

Her book *Turkey Faces West* (1930), written in exile, take the 1925 Law on the Maintenance of Order and
the Independence Tribunals as the hinge from democracy to dictatorship, and she puts the 'moral responsibility' on the
Assembly majority while giving Mustafa Kemal credit for the cunning. See [[Halide Edib Adıvar]], [[Independence Tribunals]].

## Arnold Toynbee (1939 and 1954)

*%(t39)s*

> %(t39q)s

Volume VI of *A Study of History* sets the Ghazi among the Ottoman 'saviours' who tried to Westernize their state, calls him
the 'third Ottoman saviour' and a 'totalitarian Westernizer', and, on the language reform, 'a hero'. Toynbee does not look away from the method: he describes the expulsion of an
'indispensable Greek and Armenian middle class' as a calculation (his framing, not the vault's). See [[Alphabet Reform]], [[Greco-Turkish Population Exchange]]. Volume
VIII (1954) adds *%(t54)s*

> %(t54q)s

See [[Arnold J. Toynbee]].

## Orhan Pamuk (2007), the shame of the hat

*%(p)s*

> %(pq)s

In *Other Colors* Pamuk puts Atatürk next to André Gide and reads the Hat Law as aimed at shame before Europe's eyes.
The text is read by search-inside snippet only. See [[Orhan Pamuk]], [[Hat Law]].

## Aziz Nesin (1987), the astonished satirist

*%(n)s*

> %(nq)s

A private letter, not a column: after a joke about Turks claiming Ibn Sina and Mimar Sinan, Nesin counts his blessings,
and the Gazi is the one he most marvels at. See [[Aziz Nesin]].

## Sources
%(src)s
""" % dict(f21=R[0]["saw"], f21q=R[0]["q"], f37=R[1]["saw"], h30=R[2]["saw"], h30q=R[2]["q"], t39=R[3]["saw"], t39q=R[3]["q"],
           t54=R[4]["saw"], t54q=R[4]["q"], p=R[5]["saw"], pq=R[5]["q"], n=R[6]["saw"], nq=R[6]["q"],
           src="\n".join("- %s: %s" % (r["loc"], r["urls"][0]) for r in R))
note("Events", NODE, {"type": "event", "when": "1921–2007", "tags": ["event", "verified", "writers", "intellectuals"]}, body)
print("ok", len(R))
