# -*- coding: utf-8 -*-
# Census round 22 (Nov 2026) — signed pieces in the Turkish Press Directorate's review "La Turquie kémaliste" (archive.org la_turquie_kemaliste).
# OCR issue files banked in tools/.state/round22/tk/ ; the script refuses to run if a quote is not found in its bank.
import json, os, re, sys
from _lib import note, person

HERE = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(HERE, "tools", ".state", "round22")
TK = os.path.join(STATE, "tk")


def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"').replace("«", '"').replace("»", '"')
    s = re.sub(r"-\s*\n\s*", "", s)
    return re.sub(r"\s+", " ", s).strip()


FIX = {"extraordinery": "extraordinary"}  # OCR/printer typo in the review text, corrected in the quote


def bank(fn):
    t = norm(open(os.path.join(TK, fn), encoding="utf-8").read())
    for a, b in FIX.items():
        t = t.replace(a, b)
    return t


IA = "https://archive.org/details/la_turquie_kemaliste"
NODE = "La Turquie kémaliste 1935–1938 — Haşim, Wright, Pittard, Ireland and Belge"
VENUE = ("Published in La Turquie kémaliste, the illustrated review of the Turkish Press Directorate (Direction Générale de la Presse, Ministry of the Interior), "
         "a Kemalist state propaganda venue that chose and printed (and for some items translated) what it ran; read in the OCR of archive.org item la_turquie_kemaliste. ")

R = [
 dict(id="ahmed-hasim-1935", voice="Ahmed Haşim", role="Turkish symbolist poet (1884–1933), essayist", c="Turkey", cn="Turkey", dom="letters",
      date="1935-12", era="contemporary", mirror="internal-mirror", pol="admiring", inten=2, art="article", ev="S", f="10_djvu.txt",
      saw="Describes meeting Atatürk in person at Dolmabahçe: an ageless, luminous face, the man who 'made an era of centuries grow old'.",
      q="Le visage de l'Homme qui a fait vieillir une ère longue de siècles, tout comme ceux des dieux anciens ne porte aucune trace de l'âge.",
      tr="The face of the Man who made an era of many centuries grow old, like those of the ancient gods, bears no trace of age.",
      q2="Le grand bienfait de ce jour pour moi fut de voir de près ce visage jeune et légendaire.",
      tr2="The great gift of this day for me was to see this young and legendary face close up.",
      cav=VENUE + "French translation of a short essay 'Atatürk' printed under the heading 'Quelques essais d'Ahmed Hasim' in no. 10 (December 1935), two years after Haşim's death; the Turkish original and its date are not located (the text speaks of a meeting 'last week' at Dolmabahçe 'autour de la nouvelle écriture', which suggests the alphabet consultations of August 1928, an inference not verified). Page not shown in the OCR. Translator not named. Evidence S (a posthumous translation chosen by the review), not the poet's own printing."),
 dict(id="walter-wright-1936", voice="Walter L. Wright Jr.", role="President of Robert College and the American College for Girls, Istanbul", c="United States", cn="United States", dom="letters",
      date="1936-08", era="contemporary", mirror="modernization-poster-child", pol="admiring", inten=2, art="article", ev="P", f="14_djvu.txt",
      saw="Credits Atatürk as the leader of extraordinary courage who grasped the infant nation's vitality and drove the invaders into the sea.",
      q="Defeated, humiliated, exhausted, the people of Turkey found a leader of extraordinary ability and courage.",
      tr=None,
      q2="Under his leadership the people of Turkey swept the invaders into the sea",
      tr2=None,
      cav=VENUE + "Signed English original, 'Romance and Revolution', no. 14 (August 1936); a Turkish translation ('Cazibe ve devrim') exists in the archive.org item. Page not shown in the OCR. Wright, a Protestant educator in Istanbul whose colleges operated under the Republic's regulation, writes for a Turkish government review; an American college head is a recognisable but not disinterested witness. In the same piece he calls the Turkish state 'a pattern for other nations' dissatisfied with ineffective governments (his words, not quoted here). Evidence P (signed original), venue noted."),
 dict(id="pittard-1937", voice="Eugène Pittard", role="Geneva anthropologist and professor, spokesman of the foreign scholars at the 2nd Turkish History Congress", c="Switzerland", cn="Switzerland", dom="science",
      date="1937-10", era="contemporary", mirror=None, pol="admiring", inten=2, art="speech", ev="S", f="21-22_djvu.txt",
      saw="Speaking for foreign scholars before the President, praises the Turkish History Society's energy as matching 'the builder of the country', the Republic's glorious architect.",
      q="Son énergie va de pair avec celle du constructeur même du pays, de l'édificateur glorieux de la République.",
      tr="Its energy goes hand in hand with that of the very builder of the country, the glorious architect of the Republic.",
      q2="Au nom des savants étrangers réunis ici, j'adresse mes hommages respectueux à Monsieur le Président de la République Turque, chef suprême de cet Etat.",
      tr2="In the name of the foreign scholars gathered here, I address my respectful homage to the President of the Turkish Republic, supreme head of this State.",
      cav=VENUE + "'Allocution de M. Eugène Pittard, professeur à l'Université de Genève, au nom des savants étrangers', printed in the double issue no. 21-22 (header 'Décembre 1937'), reproducing his address at the 2nd Turkish History Congress, which the same issue says opened on 20 October 1937 at Dolmabahçe in Atatürk's presence; the exact day of the address is not printed, so the date is month-only. Atatürk is not named in the quoted lines: the referents are 'le constructeur du pays' and 'Monsieur le Président de la République', i.e. Atatürk, who was present (the issue's own report). Pittard also says he was 'témoin objectif — et non pas le thuriféraire' of a Turkish effort of 36 years' acquaintance. A diplomatic speech of thanks to a host: the praise is partly occasion. Page not shown in the OCR."),
 dict(id="philip-ireland-1938", voice="Philip W. Ireland", role="Harvard government scholar of the Middle East (F.R.G.S., M.A. Oxon, Ph.D.)", c="United States", cn="United States", dom="science",
      date="1938-10", era="contemporary", mirror=None, pol="admiring", inten=1, art="article", ev="P", f="27_djvu.txt",
      saw="Names national unity together with Atatürk's leadership as one of the primary elements of strength of the new Turkey.",
      q="national unity, which together with the leadership of Atatürk, has been one of the primary elements of strength of the new Turkey",
      tr=None, q2=None, tr2=None,
      cav=VENUE + "Signed English original, 'Land of Pioneers', no. 27 (October 1938, the fifteenth-anniversary number, published a month before Atatürk's death); a Turkish translation ('Öncüler ülkesi') is in the archive.org item. The byline gives him as of the Department of Government, Harvard University; nothing else is verified about him. A passing evaluative clause inside a travel-and-development article (he also speaks of 'the many reforms instituted by Atatürk'); intensity 1. Page not shown in the OCR."),
 dict(id="burhan-belge-1938-12", voice="Burhan Belge", role="Director General of the Press, Turkish writer and Atatürk's circle", c="Turkey", cn="Turkey", dom="press",
      date="1938-12", era="funeral", mirror="internal-mirror", pol="instrumental", inten=2, art="article", ev="P", f="28_djvu.txt",
      saw="After Atatürk's death, calls him a fortunate chief who finished his work and handed the national 'cause' to İnönü, so the course continues.",
      q="Atatürk a été un Chef heureux qui a éprouvé la joie d'achever son œuvre",
      tr="Atatürk was a fortunate Chief who felt the joy of completing his work",
      q2="Atatürk a dirigé la lutte pour la libération et a fait la Révolution.",
      tr2="Atatürk led the struggle for liberation and made the Revolution.",
      cav=VENUE + "Signed article by the head of the Press Directorate that publishes the review, 'D'Atatürk à İnönü', no. 28 (December 1938), the first issue after the funeral; the same issue opens with an unsigned editorial on 'La mort d'Atatürk'. The purpose is reassurance of foreign readers about continuity under İnönü ('nul, parmi nos amis de l'étranger, ne doit en douter'), hence instrumental, and Belge was an official of the regime, not an independent voice. Turkish translation 'Atatürk'den İnönü'ye' is in the item. Page not shown in the OCR."),
]

bad = []
for r in R:
    b = bank(r["f"])
    for k in ("q", "q2"):
        if r[k] and norm(r[k]) not in b:
            bad.append((r["id"], k))
if bad:
    sys.exit("quote not found in source bank: %s" % bad)
for r in R:
    assert len(r["saw"].split()) <= 25, (r["id"], len(r["saw"].split()))

ISSUE = {"ahmed-hasim-1935": "no. 10 (December 1935), 'Quelques essais d'Ahmed Hasim — Atatürk'",
         "walter-wright-1936": "no. 14 (August 1936), 'Romance and Revolution'",
         "pittard-1937": "no. 21-22 (December 1937), 'Allocution de M. Eugène Pittard'",
         "philip-ireland-1938": "no. 27 (October 1938), 'Land of Pioneers'",
         "burhan-belge-1938-12": "no. 28 (December 1938), 'D'Atatürk à İnönü'"}
FILE = {"10_djvu.txt": "10", "14_djvu.txt": "14", "21-22_djvu.txt": "21-22", "27_djvu.txt": "27", "28_djvu.txt": "28"}
for r in R:
    r["cite"] = "La Turquie kémaliste " + ISSUE[r["id"]]
    r["url"] = IA + "  (file " + r["f"] + ")"

with open(os.path.join(STATE, "gazes_tkemaliste.jsonl"), "w", encoding="utf-8") as f:
    for r in R:
        q = r["q"] + (" [translation: " + r["tr"] + "]" if r["tr"] else "")
        if r["q2"]:
            q += " … " + r["q2"] + (" [translation: " + r["tr2"] + "]" if r["tr2"] else "")
        rec = {"id": r["id"], "voice": r["voice"], "voice_type": "person", "role": r["role"],
               "country": r["c"], "country_now": r["cn"], "domain": r["dom"], "date": r["date"], "era": r["era"],
               "mirror": r["mirror"], "polarity": r["pol"], "intensity": r["inten"], "what_they_saw": r["saw"],
               "quote": q, "artifact": r["art"], "evidence": r["ev"],
               "mediated_by": ("La Turquie kémaliste (Turkish Press Directorate) translation" if r["ev"] == "S" else None),
               "caveat": r["cav"] + " Cited as " + r["cite"] + ".", "node": NODE, "sources": [IA]}
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")

with open(os.path.join(STATE, "ledger_tkemaliste.md"), "w", encoding="utf-8") as f:
    f.write("| Claim | Node | Status | Sources | Next step |\n|---|---|---|---|---|\n")
    for r in R:
        f.write("| %s (%s): %s | %s | verified %s (archive.org OCR djvu text, read; Kemalist state review) | %s | print-page number from a paper copy |\n" % (
            r["voice"], r["date"], r["saw"], NODE, r["ev"], IA + " " + r["f"]))

NAT = {"ahmed-hasim-1935": ("Turkish", "1884–1933", "poet"), "walter-wright-1936": ("American", "", "educator"),
       "pittard-1937": ("Swiss", "1867–1962", "anthropologist"), "philip-ireland-1938": ("American", "", "scholar"),
       "burhan-belge-1938-12": ("Turkish", "", "press official")}
LIFE = {"pittard-1937": ""}  # lifespans from memory are not recorded
for r in R:
    nat, life, tag = NAT[r["id"]]
    person(r["voice"], role=r["role"], nat=nat, life="", stance="%s (%s)" % (r["pol"], r["date"][:4]),
           tags=["verified", tag.replace(" ", "-"), "kemaliste-review"],
           body="%s. Voice in the Turkish Press Directorate's review *La Turquie kémaliste*; see [[%s]].\n\n## Sources\n- %s: %s\n" % (r["role"], NODE, r["cite"], IA))


def sec(r):
    tr = ""
    if r["tr"]:
        tr = "\n> (translation: %s)" % r["tr"]
    t2 = ""
    if r["q2"]:
        t2 = "\n>\n> %s" % r["q2"] + ("\n> (translation: %s)" % r["tr2"] if r["tr2"] else "")
    return "## %s — %s\n\n%s\n\n> %s%s%s\n\n**Caveat.** %s\n" % (r["voice"], r["cite"], r["saw"], r["q"], tr, t2, r["cav"])


body = ("Five signed pieces from *La Turquie kémaliste*, the bimonthly (French, German and English) illustrated review of the Turkish Press Directorate, read in the "
        "OCR text at archive.org. **Every item comes from a Kemalist state propaganda venue**: the review chose its contributors, printed or translated what suited it, "
        "and its foreign pens were guests or contacts of the regime. Names: [[Ahmed Haşim]], [[Walter L. Wright Jr.]], [[Eugène Pittard]], [[Philip W. Ireland]] and [[Burhan Belge]].\n\n"
        + "\n".join(sec(r) for r in R)
        + "\n## Sources\n- Internet Archive, *La Turquie kémaliste* (1934–1948), item la_turquie_kemaliste: " + IA + "\n"
        + "\n".join("- %s" % r["cite"] for r in R) + "\n")
note("Events", NODE, {"type": "event", "when": "1935–1938", "tags": ["event", "verified", "turkey", "kemaliste-review"]}, body)
print("ok", len(R))
