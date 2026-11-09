# -*- coding: utf-8 -*-
# Census round 21 (Nov 2026) — Spanish and Italian pens: Ortega Munilla 1922, Ortega y Gasset 1930, Gramsci (Notebook 2),
# La Conquista del Estado 1931, Ramiro Ledesma Ramos 1935. Banks in tools/.state/round21/ (archive.org djvu text).
# Script refuses to run if a quote is not in its bank.
import json, os, re, sys, unicodedata
from _lib import note, person

HERE = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(HERE, "tools", ".state", "round21")
NODE = "Latin Pens on Mustafa Kemal — Ortega Munilla, Ortega y Gasset, Gramsci and Ledesma Ramos"


def norm(s):
    s = unicodedata.normalize("NFKC", s)
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"').replace("‘‘", '"')
    s = re.sub(r"[-¬]\s*\n\s*", "", s)   # line-end hyphens
    s = re.sub(r"\s+", " ", s)
    return s.strip().lower()


def bank(f):
    return norm(open(os.path.join(STATE, f), encoding="utf-8").read())


IA = "https://archive.org/details/"
R = [
 dict(id="ortega-munilla-1922", voice="José Ortega Munilla", role="Spanish novelist, academician and veteran newspaper editor (columnist of ABC)",
      c="Spain", cn="Spain", dom="letters", date="1922-09-16", era="contemporary", mirror=None, pol="admiring", inten=2, art="article",
      ev="P", f="latin_chispas.txt",
      saw="Calls Kemal the awaited war-leader risen from the tombs of the dervishes; the 'dead people' revived, though Turkey's faith is 'mistaken'.",
      q="Y el caudillo esperado surge en Turquía, entre las tumbas de los derviches, bajo la sombra de los cipreses de Stambul. Ese héroe vencedor se llama Mustafá Kemal.",
      tr="And the awaited leader rises in Turkey, among the tombs of the dervishes, under the shadow of the cypresses of Stambul. That victorious hero is called Mustafá Kemal.",
      src=IA + "chispasdelyunque00orte",
      cav="Column 'El triunfo de Turquía', ABC, Saturday 16 September 1922 (dated at its end), collected posthumously in J. Ortega Munilla, Chispas del yunque (Madrid: Prensa Gráfica, 1923) from the open UNC scan; page not shown in the OCR. Written days after the Smyrna fire: it speaks of Greek 'catastrophe' and does not mention the burning. He also calls Turkey's 'power of faith' 'absolutely mistaken, but permanent', and later says the victory leaves Kemal, 'a Turk perhaps devoid of military science', disturbing the world's would-be masters; the praise is for the Turkish revival and its war leader, not for any programme. Ortega Munilla (1856-1922) was the father of Ortega y Gasset; he died 1922 (the book is posthumous)."),
 dict(id="ortega-y-gasset-1930", voice="José Ortega y Gasset", role="Spanish philosopher and essayist",
      c="Spain", cn="Spain", dom="letters", date="1930", era="contemporary", mirror=None, pol="witness", inten=1, art="article",
      ev="P", f="ortega2.txt",
      saw="Cites Kemal's overnight swap of Anatolia's fezzes for Western hats as proof that this age is one of dress uniformity, with no verdict either way.",
      q="En Turquía, Mustafá Kemal siega en un día todas las chechias de Anatolia y las sustituye por el chapeo occidental.",
      tr="In Turkey, Mustafá Kemal mows down in one day all the fezzes of Anatolia and replaces them with the Western hat.",
      src=IA + "ortega-y-gasset.-obras-completas.-tomo-ii-ocr-1963",
      cav="'Para una ciencia del traje popular', preface to Ortiz Echagüe's photograph collection Tipos y trajes de España (published 1930, per Ortega's own footnote); in Obras completas II (El Espectador, 1916-1934), the page after the footer '696' in the 1963 Revista de Occidente OCR, i.e. p. 697 (page numbers are footers in the OCR). One passing sentence used as evidence of a 'uniformist' epoch ('el hecho es terráqueo'); the verb 'siega' (mows down) gives the tone, but he states no approval or blame, so recorded as witness. The sentence also appears in the El Espectador volume (1950s reprints; same text)."),
 dict(id="gramsci-q2-1930", voice="Antonio Gramsci", role="Italian Marxist theorist, imprisoned co-founder of the PCI",
      c="Italy", cn="Italy", dom="letters", date="1930", era="contemporary", mirror=None, pol="witness", inten=1, art="article",
      ev="P", f="gramsci_pn1.txt",
      saw="Notes an author who explains Kemal's reforms as a return to the pure, and takes it as Muslim casuistry; no direct verdict on Kemal.",
      q="Sirdar Ikbal Ali Shah uses this same principle to explain Kemal Pasha's reforms in Turkey: they are not anything “new” but a return to the old, the pure, etc. etc.",
      tr="(published English translation, J. A. Buttigieg and A. Callari; the quoted words are the translators', not Gramsci's Italian)",
      src=IA + "antonio-gramsci-prison-notebooks-volumes-1-3",
      cav="Quaderno 2 (Miscellaneous I), §90 'La nuova evoluzione dell'Islam', Prison Notebooks vol. 1, ed. Buttigieg (Columbia UP, 2011), p. 334; Notebook 2 covers 1929-1933, so '1930' is a mid-range placeholder. Gramsci's view is of Ikbal Ali Shah's apologetic, 'Jesuitism and casuistry' among Muslims, and of Islam's 'national sentiment' against theocratic cosmopolitanism; he judges neither Kemal nor the reforms directly, hence witness. Italian original not read. Two further Kemal mentions in his letters (Lettere dal carcere, to Tania Schucht, 6 May 1929, p. 273 of the Einaudi edition, a Bedouin at Ustica called Kemal 'come il papa del maomettanesimo' after Gramsci told him Kemal had banned polygamy and permitted photographs; and 20 March 1931, 'i Turchi che non hanno accettato le riforme di Kemal') are reported speech or passing, and not recorded as gazes."),
 dict(id="la-conquista-del-estado-1931-03", voice="La Conquista del Estado", voice_type="press", role="Madrid weekly of Ramiro Ledesma Ramos's proto-fascist group",
      c="Spain", cn="Spain", dom="press", date="1931-03-28", era="contemporary", mirror="modernization-poster-child", pol="admiring", inten=2, art="editorial",
      ev="P", f="latin_LaConquistaDelEstado1_03_djvu.txt",
      saw="Runs a multi-column feature on 'the gigantic work of the Turkish revolution', hailing 'the genius of the Dictator' who read his people's aspirations.",
      q="El genio del Dictador Mustafá Kemal",
      tr="The genius of the Dictator Mustafá Kemal (subhead)",
      q2="Un joven general ha comprendido las aspiraciones profundas de sus compatriotas.",
      tr2="A young general has understood the deep aspirations of his compatriots.",
      src=IA + "la-conquista-del-estado-2-01",
      cav="La Conquista del Estado, año I, núm. 3, Madrid, 28 March 1931 (open archive.org scan, file LaConquistaDelEstado1_03; page not shown in the OCR). Unsigned feature in the 'Informaciones' section; the OCR of the main headline is garbled ('la obra gigantesca de la revolución turca' is a reading), so the subhead is quoted. Content tracks a French-style survey (Kemal's abolition of the caliphate, calendar, alphabet, 'Turkey technifies'); it also notes that 'toda oposición es suprimida' and that the Gazi found the people could not adapt to long preparation for democracy, stated without reproach. Authorship by Ledesma Ramos is not established."),
 dict(id="ledesma-ramos-1935", voice="Ramiro Ledesma Ramos (as 'Roberto Lanzas')", role="Spanish fascist ideologue, founder of the JONS",
      c="Spain", cn="Spain", dom="politics", date="1935-11", era="contemporary", mirror="nation-forge-template", pol="admiring", inten=1, art="book",
      ev="S", f="1935-fascismo-en-espana-roberto-lanzas.txt",
      saw="Counts Kemal among the contemporary 'national revolutions' of astonishing success beside Mussolini, Hitler and Stalin, in contrast with Spain.",
      q="En nuestra época, es decir, en nuestros mismos días, las revoluciones nacionales se desarrollan también con éxito pasmoso. Véanse estos nombres que las representan: Mussolini, Kemal, Hitler y -¿por qué no?- Stalin.",
      tr="In our age, that is, in our very days, national revolutions also develop with astonishing success. See these names that represent them: Mussolini, Kemal, Hitler and - why not? - Stalin.",
      src=IA + "1935-fascismo-en-espana-roberto-lanzas",
      cav="¿Fascismo en España? by 'Roberto Lanzas' (Madrid, preface dated November 1935), a pseudonym of Ledesma Ramos per the archive.org item title and the text's own account of La Conquista del Estado; p. 12 by the OCR's footer sequence (chapter on the national revolution and the right). The same sentence appears in the 1942 Breviarios del Pensamiento Español anthology of Ledesma. A single listing, but it places Kemal in the pantheon of successful nationalist revolutions. An earlier piece in La Conquista del Estado no. 23 (24 October 1931, author not shown) speaks of 'la victoria presente del Gasi' and how 'Mustafá Kemal supo uncirse a la lejanía'; not recorded as Ledesma's."),
]
bad = []
for r in R:
    for k in ("q", "q2"):
        if r.get(k) and norm(r[k]) not in bank(r["f"]):
            bad.append((r["id"], k))
if bad:
    sys.exit("quote not found in source bank: %s" % bad)
for r in R:
    print(r["id"], len(r["saw"].split()))

with open(os.path.join(STATE, "gazes_latin.jsonl"), "w", encoding="utf-8") as f:
    for r in R:
        q = r["q"] + (" " + r["q2"] if r.get("q2") else "")
        t = r["tr"] + (" " + r["tr2"] if r.get("tr2") else "")
        rec = {"id": r["id"], "voice": r["voice"], "voice_type": r.get("voice_type", "person"), "role": r["role"],
               "country": r["c"], "country_now": r["cn"], "domain": r["dom"], "date": r["date"], "era": r["era"],
               "mirror": r["mirror"], "polarity": r["pol"], "intensity": r["inten"], "what_they_saw": r["saw"],
               "quote": q + " [translation: " + t + "]", "artifact": r["art"], "evidence": r["ev"],
               "mediated_by": None, "caveat": r["cav"], "node": NODE, "sources": [r["src"]]}
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")

with open(os.path.join(STATE, "ledger_latin.md"), "w", encoding="utf-8") as f:
    f.write("| Claim | Node | Status | Sources | Next step |\n|---|---|---|---|---|\n")
    rows = [
     ("Ortega Munilla, 'El triunfo de Turquía', ABC 16 Sep 1922 (Chispas del yunque, 1923)", "verified P (archive.org UNC scan, read)", R[0]["src"], "Page number in the 1923 book; ABC hemeroteca view of 16 Sep 1922"),
     ("Ortega y Gasset, 'Para una ciencia del traje popular' (1930), OC II p. 697: Kemal and the fezzes", "verified P (1963 OCR, read; passing mention, witness)", R[1]["src"], "Confirm the print page and the first publication (preface to Ortiz Echagüe, 1930)"),
     ("Gramsci, Quaderno 2 §90, PN vol. 1 p. 334: Kemal's reforms as a 'return to the pure' (Ikbal Ali Shah)", "verified P (English translation, scan read; Gramsci's view of Kemal not stated)", R[2]["src"], "Read the Italian original (Gerratana ed., Q2 §90) and date the note"),
     ("La Conquista del Estado no. 3, 28 Mar 1931: 'El genio del Dictador Mustafá Kemal'", "verified P (open scan, read; unsigned)", R[3]["src"], "Find the source of the feature and the print page"),
     ("Ledesma Ramos / 'Roberto Lanzas', ¿Fascismo en España? (Nov 1935), p. 12: Kemal among the national revolutions", "verified S (text copy, read; also in the 1942 anthology)", R[4]["src"], "Check the 1935 print edition page"),
    ]
    for a, b, c, d in rows:
        f.write("| %s | %s | %s | %s | %s |\n" % (a, NODE, b, c, d))

person("José Ortega Munilla", role="Spanish novelist and newspaper editor", nat="Spanish", life="1856–1922", stance="admiring (Sept 1922)",
       tags=["writer", "spain", "verified", "spanish-primary"],
       body="""Novelist, academician and long-time editor of El Imparcial, father of the philosopher Ortega y Gasset. In his ABC column 'El triunfo de Turquía' (16 September 1922) he greets Mustafá Kemal as the leader the world war had failed to produce and sees a 'dead people' resurrected. See [[%s]].

## Sources
- %s
""" % (NODE, R[0]["src"]))
person("José Ortega y Gasset", role="Spanish philosopher and essayist", nat="Spanish", life="1883–1955", stance="witness (1930)",
       tags=["writer", "spain", "verified", "spanish-primary"],
       body="""One passing sentence in a 1930 preface: Kemal 'mows down' Anatolia's fezzes in a day and puts on the Western hat, evidence for Ortega that this age is one of uniform dress. No verdict. See [[%s]].

## Sources
- %s
""" % (NODE, R[1]["src"]))
person("Antonio Gramsci", role="Italian Marxist theorist", nat="Italian", life="1891–1937", stance="witness (Prison Notebooks 2)",
       tags=["writer", "italy", "verified", "italian-primary"],
       body="""In Prison Notebook 2 (§90, on the 'new evolution of Islam') Gramsci notes that Sirdar Ikbal Ali Shah explains Kemal Pasha's reforms as a return to the pure, and takes that as an example of Muslim casuistry; he sees Islam's 'national sentiment' as the coming heresy against theocratic cosmopolitanism. A search of the English Prison Notebooks vol. 1 and the Letters found no sustained judgment of Kemal. See [[%s]].

## Sources
- %s
""" % (NODE, R[2]["src"]))
person("Ramiro Ledesma Ramos", role="Spanish fascist ideologue, founder of the JONS", nat="Spanish", life="1905–1936", stance="admiring (1931, 1935)",
       tags=["writer", "spain", "verified", "spanish-primary"],
       body="""Founder of the weekly La Conquista del Estado (1931), whose 28 March 1931 issue praised 'the genius of the Dictator Mustafá Kemal', and, as 'Roberto Lanzas' in ¿Fascismo en España? (1935), he lists Kemal beside Mussolini, Hitler and Stalin as the face of successful national revolution. See [[%s]].

## Sources
- %s
- %s
""" % (NODE, R[4]["src"], R[3]["src"]))

body = """Five Spanish and Italian pens, read in open archive.org copies. **José Ortega Munilla** (ABC, 1922) greets Kemal as the awaited victor; **Ortega y Gasset** (1930) uses the hat reform as an example of an age of uniform dress; **Antonio Gramsci** (Prison Notebook 2) treats an apologist's reading of Kemal's reforms as casuistry; **La Conquista del Estado** (1931) hails the Dictator's genius; **Ramiro Ledesma Ramos** (1935) counts Kemal among the national revolutions. See [[José Ortega Munilla]], [[José Ortega y Gasset]], [[Antonio Gramsci]], [[Ramiro Ledesma Ramos]].

"""
for r in R:
    body += "## %s (%s)\n\n> %s%s\n> (translation: %s%s)\n\n%s\n\n" % (
        r["voice"], r["date"], r["q"], (" " + r["q2"]) if r.get("q2") else "", r["tr"], (" " + r["tr2"]) if r.get("tr2") else "", r["cav"])
body += "## Sources\n" + "\n".join("- %s" % r["src"] for r in R) + "\n"
note("Events", NODE, {"type": "event", "when": "1922–1935", "tags": ["event", "verified", "spain", "italy", "spanish-primary"]}, body)
print("ok")
