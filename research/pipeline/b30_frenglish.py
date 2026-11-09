# -*- coding: utf-8 -*-
# Census round 21 (Nov 2026) — French and British pens on Kemal: Herriot (La Turquie kémaliste 1934), Pernot and Pinon (Revue des Deux Mondes),
# Lucie Delarue-Mardrus (El Arab), Franklin-Bouillon (NYT 25 Sep 1922), Oliver Baldwin (The Questing Beast).
# Texts banked in tools/.state/round21/ ; the script refuses to run if a quote (or its check string) is not found in its bank.
import json, os, re, sys
from _lib import note, person

HERE = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(HERE, "tools", ".state", "round21")


def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"').replace("«", '"').replace("»", '"')
    s = re.sub(r"-\s*\n\s*", "", s)
    return re.sub(r"\s+", " ", s).strip()


def bank(fn):
    return norm(open(os.path.join(STATE, fn), encoding="utf-8").read())


NODE_FR = "French Pens on Kemal, 1920–1944 — Herriot, Pernot, Pinon, Delarue-Mardrus and Franklin-Bouillon"
NODE_OB = "Oliver Baldwin on Kemal, 1932"

R = [
 dict(id="herriot-1934", voice="Édouard Herriot", link="Édouard Herriot", node=NODE_FR, bankfn="ltk/1_djvu.txt",
      role="French Radical leader, former Prime Minister and mayor of Lyon", c="France", cn="France", dom="politics", date="1934",
      mirror="secular-rationalist-prophet", pol="admiring", inten=2, art="speech", ev="S",
      saw="After a 1933 visit, calls Kemal a remarkable statesman who believes in science and reason, a disciple perhaps unconscious of Comte and Descartes.",
      q="Le Ghazi croit à la science, à la raison. Je vous l'ai dit : je me le représente comme un disciple, inconscient peut-être, d'Auguste Comte et de Descartes.",
      chk=["croit à la science, à la raison", "disciple, inconscient peut-être, d'Auguste Comte et de Descartes"],
      tr="The Ghazi believes in science, in reason. I told you: I picture him as a disciple, unconscious perhaps, of Auguste Comte and of Descartes.",
      cite="Herriot, 'De la vieille à la nouvelle Turquie', La Turquie kémaliste no. 1 (1934), pp. 15–28, quote on p. 27 (a lecture to an audience, 'Mesdames et Messieurs')",
      url="https://archive.org/download/la_turquie_kemaliste/La%20Turquie%20Kemaliste/1_djvu.txt",
      cav="Published in the Turkish Press Directorate's own French-language propaganda review, so the venue is Kemalist; the text is Herriot's lecture, signed. Issue date not printed in the OCR (the review began in 1934), hence year-only. Herriot also calls him 'ce remarquable homme d'État' (p. 27) and says he ruled 'non par des gestes de dictature'. OCR reads 'lai' for 'l'ai' (corrected in the quote).",
      nxt="Herriot's 1952 memoir Jadis d'une guerre à l'autre (IA jadisduneguerrel0000edou, lending only): 'je reçus de Mustapha Kemal un accueil spécialement cordial' (snippet, no page)"),
 dict(id="pernot-1922", voice="Maurice Pernot", link="Maurice Pernot", node=NODE_FR, bankfn="La_Question_turque_02.txt",
      role="French journalist and specialist of the Near East, Revue des Deux Mondes", c="France", cn="France", dom="press", date="1922",
      mirror=None, pol="conflicted", inten=2, art="article", ev="S",
      saw="Portrays the Angora leader as adored by his soldiers and esteemed by generals, a national hero, while noting opponents' charges of dictatorship.",
      q="Moustapha Kemal, adoré par les soldats, est estimé par les chefs, même par ceux dont la valeur technique est peut-être supérieure à la sienne.",
      chk=[],
      tr="Moustapha Kemal, adored by the soldiers, is esteemed by the generals, even by those whose technical ability is perhaps superior to his own.",
      cite="Pernot, 'La Question turque' II, 'Angora', Revue des Deux Mondes, 7e période, tome 7 (1922), pp. 549–579, quote on p. 567 (Wikisource page numbers)",
      url="https://fr.wikisource.org/wiki/La_Question_turque/02",
      cav="Wikisource transcription; the issue date within 1922 is not printed in the transcription (tome 7 = early 1922), so year-only. Pernot also calls him 'le jeune dictateur' and reports opponents' charge of 'allures de dictateur'; the 'adoré par les soldats' sentence is Pernot's own judgement, not a quoted source. Mixed: sympathetic portrait of a moderate against Unionist hard-liners, framed for French policy.",
      nxt="Pernot's Le Saint-Siège (1924, IA bwb_T5-AFV-076) p. 184: 'L'effort victorieux de Moustapha Kemal fit échouer, en partie, le plan politique' (a passing mention)"),
 dict(id="pinon-1920", voice="René Pinon", link="René Pinon", node=NODE_FR, bankfn="w3.txt",
      role="French historian and foreign-affairs chronicler of the Revue des Deux Mondes", c="France", cn="France", dom="press", date="1920",
      mirror=None, pol="hostile", inten=2, art="article", ev="S",
      saw="Treats Kemal as the continuator and accomplice of Enver, Talaat and Djemal, and the real head of a Moscow–Constantinople–Berlin plot against the Allies.",
      q="Mustapha Kemal est le continuateur et le complice des Enver, des Talaat et des Djemal.",
      chk=["sous le masque d'un insurgé, Mustapha Kemal est le véritable chef du gouvernement"],
      tr="Mustapha Kemal is the continuator and accomplice of the Envers, Talaats and Djemals.",
      cite="Pinon, 'L'Offensive de l'Asie', Revue des Deux Mondes, 6e période, tome 56 (1920), pp. 799–815, quote on p. 808 (the 'masque d'un insurgé' line on p. 813)",
      url="https://fr.wikisource.org/wiki/L%E2%80%99Offensive_de_l%E2%80%99Asie",
      cav="Wikisource transcription; the piece is dated by the tome (March–April 1920, so 1920), the exact issue is not printed. Written before the Ankara Assembly's victories; Pinon's reading is the 'Unionists in disguise' thesis of the Allied press in 1920, which he states as fact.",
      nxt="Pinon's later Revue des Deux Mondes pieces after 1922 for any change of view"),
 dict(id="delarue-mardrus-1944", voice="Lucie Delarue-Mardrus", link="Lucie Delarue-Mardrus", node=NODE_FR, bankfn="w1.txt",
      role="French novelist and poet", c="France", cn="France", dom="letters", date="1944",
      mirror=None, pol="conflicted", inten=1, art="memoir", ev="S",
      saw="Recalls Kemal's unveiling campaign as a wave 'ordered' from above; some Turkish women preferred suicide to the new era. She mocks his cap decree elsewhere.",
      q="au moment de la vague de libération ordonnée par Kémal-Pacha, certaines dames turques ont préféré se suicider qu'entrer dans cette ère nouvelle qui les épouvantait.",
      chk=[],
      tr="at the moment of the wave of liberation ordered by Kemal Pasha, some Turkish ladies preferred to kill themselves rather than enter this new era that terrified them.",
      cite="Delarue-Mardrus, El Arab, l'Orient que j'ai connu (Lugdunum, 1944), ch. 'Tunis', p. 30; also ch. 'Constantinople', p. 137: 'S'ils avaient pu prévoir les futures casquettes cyclistes ordonnées par Kémal-pacha !'",
      url="https://fr.wikisource.org/wiki/El_Arab,_l%E2%80%99Orient_que_j%E2%80%99ai_connu/Tunis",
      cav="Wikisource transcription (page numbers are the book's). A passing, ironic view: she says 'on ne nous l'a pas dit' (the suicide claim is hearsay) and in the Constantinople chapter she pleaded for the old customs. Posthumous (1944) recollection of a pre-1914 Orient. She also writes that 'avant Kémal Pacha' any passer-by could scold an unveiled woman (p. 31).",
      nxt="Her other Orient books and press pieces; not yet searched"),
 dict(id="franklin-bouillon-1922-09", voice="Henry Franklin-Bouillon", link="Franklin Bouillon", node=NODE_FR, bankfn="franklin_nyt.txt",
      role="French politician and former minister who signed the Ankara Agreement of 1921", c="France", cn="France", dom="diplomacy", date="1922-09-24",
      mirror=None, pol="instrumental", inten=2, art="quote", ev="J", noperson=True,
      saw="Before leaving to meet Kemal, says he has confidence in Kemal's discretion and wisdom, from their telegrams and his knowledge of the man.",
      q="Our exchange of telegrams. our reciprocal friendship and my knowledge of the man leads me to hope",
      chk=["he had every confidence in Kemal's discretion and wisdom"],
      tr="(already English: the New York Times's rendering of his French remarks)",
      cite="'Paris Acclaims Peace in Near East; Will Send Franklin-Bouillon by Fast Cruiser to Advise the Turks', New York Times, 25 September 1922 (Paris dispatch of 24 Sept)",
      url="https://nytimes.com/1922/09/25/archives/paris-acclaims-peace-in-near-east-will-send-franklinbouillon-by.html",
      cav="Single source (J): read only as the archive snippet returned by search, the article itself is paywalled; the quotation is the NYT's English rendering of a French statement, and the OCR full stop after 'telegrams' is kept as printed in the snippet. Wire/press report of a statement, not his own text. Diplomatic purpose (selling Allied terms to Kemal) colours it; he adds that dangers remain.",
      nxt="Franklin-Bouillon's own speeches (Chambre des députés, 1921-22) and La Turquie nouvelle (1921) in Gallica; Poincaré's Histoire politique IV pp. 111-114, 141 treats the Ankara accord (a view of the accord, not of Kemal)"),
 dict(id="oliver-baldwin-1932", voice="Oliver Baldwin", link="Oliver Baldwin", node=NODE_OB, bankfn="baldwin_qb.txt",
      role="British journalist and soldier, son of Stanley Baldwin, later Labour MP", c="United Kingdom", cn="United Kingdom", dom="press", date="1932",
      mirror=None, pol="admiring", inten=1, art="memoir", ev="S",
      saw="Writing of Anatolian peasants, expects things to improve now that Kemal has limited the power of the priesthood.",
      q="Since Mustapha Kemal has limited the power of the priesthood, things will probably be better in the future,",
      chk=["if the Turks are allowed a reasonable period of peace"],
      tr=None,
      cite="Oliver Baldwin, The Questing Beast: An Autobiography (1932), p. 129 (and p. 130 for the Turks 'may become a very different race')",
      url="https://archive.org/details/in.ernet.dli.2015.176458",
      cav="Open scan (Digital Library of India copy of the 1932 book). A passing view inside a travelogue of 1920s Anatolia; the sentence is a prediction about the peasants. Other 'Kemal's in the book are his Circassian fellow-prisoner Yusuf Kemal, not Mustafa Kemal; the other Kemalist mentions (p. 165 the 17 September 1922 march; a later remark that Kemal's portrait hung in Indian Muslim shops) are descriptive. Sentence is cut off at the comma in the printed page; the text continues on p. 130.",
      nxt="Six Prisons and Two Revolutions (1925, IA sixprisonstworev0000unse) for his 1920-21 view of Kemal's rising"),
]

for r in R:
    b = bank(r["bankfn"])
    q = norm(r["q"])
    checks = r["chk"] if r["chk"] else [r["q"]]
    for c in checks + ([r["q"]] if r["chk"] and r["id"] not in ("herriot-1934",) else []):
        if norm(c) not in b:
            sys.exit("not found in bank: %s :: %s" % (r["id"], c[:60]))
    assert len(r["saw"].split()) <= 25, r["id"]

with open(os.path.join(STATE, "gazes_frenglish.jsonl"), "w", encoding="utf-8") as f:
    for r in R:
        qq = r["q"] + (" [translation: " + r["tr"] + "]" if r["tr"] else "")
        rec = {"id": r["id"], "voice": r["voice"], "voice_type": "person", "role": r["role"],
               "country": r["c"], "country_now": r["cn"], "domain": r["dom"], "date": r["date"],
               "era": "posthumous" if r["date"] >= "1939" else "contemporary",
               "mirror": r["mirror"], "polarity": r["pol"], "intensity": r["inten"], "what_they_saw": r["saw"],
               "quote": qq, "artifact": r["art"], "evidence": r["ev"],
               "mediated_by": "New York Times 25 Sep 1922 (English rendering)" if r["id"].startswith("franklin") else None,
               "caveat": "Cited as %s. %s" % (r["cite"], r["cav"]),
               "node": r["node"], "sources": [r["url"]]}
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")

with open(os.path.join(STATE, "ledger_frenglish.md"), "w", encoding="utf-8") as f:
    f.write("| Claim | Node | Status | Sources | Next step |\n|---|---|---|---|---|\n")
    for r in R:
        f.write("| %s (%s, %s): \"%s\" | %s | verified %s (%s) | %s | %s |\n" % (
            r["voice"], r["role"], r["date"], r["q"].replace("|", "/"), r["node"], r["ev"], r["cite"], r["url"], r["nxt"]))

for r in R:
    if r.get("noperson"):
        continue
    tr = "\n> (translation: %s)" % r["tr"] if r["tr"] else ""
    person(r["link"], role=r["role"], nat="French" if r["c"] == "France" else "British", life="",
           stance="%s (%s)" % (r["pol"], r["date"][:4]),
           tags=["verified", "french-primary" if r["c"] == "France" else "british-primary"],
           body="""%s. %s

> %s%s

See [[%s]].

## Sources
- %s: %s
""" % (r["role"], r["saw"], r["q"], tr, r["node"], r["cite"], r["url"]))


def section(r):
    tr = "\n> (translation: %s)" % r["tr"] if r["tr"] else ""
    link = "[[%s]]" % r["link"]
    return """## %s — %s

*%s*

> %s%s

%s. %s Cited as: %s.
""" % (r["voice"], r["date"], r["saw"], r["q"], tr, link, r["cav"], r["cite"])


fr = [r for r in R if r["node"] == NODE_FR]
body = """Five French voices on Kemal found by archive.org full-text search (the Herriot lecture in the Turkish Press Directorate's review, with the open djvu read) and by phrase search of French Wikisource (the two Revue des Deux Mondes pieces and Delarue-Mardrus), plus Franklin-Bouillon's statement of September 1922 as reported by the New York Times. Related: [[Franklin Bouillon]], and the earlier [[Western Statesmen and Churchmen on Atatürk in Their Own Words]].

%s
## Sources
%s
""" % ("\n".join(section(r) for r in fr), "\n".join("- %s: %s" % (r["cite"], r["url"]) for r in fr))
note("Events", NODE_FR, {"type": "event", "when": "1920–1944", "tags": ["event", "verified", "france", "french-primary"]}, body)

ob = [r for r in R if r["node"] == NODE_OB][0]
body = """A passing but approving remark in a British memoir of 1920s Anatolia. %s

## Sources
- %s: %s
""" % (section(ob).split("\n", 2)[2], ob["cite"], ob["url"])
note("Events", NODE_OB, {"type": "event", "when": "1932", "tags": ["event", "verified", "britain", "british-primary"]}, body)
print("ok", len(R))
