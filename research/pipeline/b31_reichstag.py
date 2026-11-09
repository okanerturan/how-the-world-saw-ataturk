# -*- coding: utf-8 -*-
# Census round 22 (Nov 2026) — German parliaments on Atatürk.
# (1) Hitler's Reichstag speech of 4 May 1941: German original read on the BSB/MDZ page image (bsb00000613, printed p. 85) -> upgrade file.
# (2) Bundestag plenary protocols 1983-2025 via the DIP API (public key from the DIP docs page): speeches naming Atatürk with a stated view.
# DIP full text (tools/.state/round22/rt/dip_*.txt) and the dserver PDFs (printed page numbers) were read; quotes are checked against the DIP text.
import json, os, re, sys
from _lib import note, person

HERE = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(HERE, "tools", ".state", "round22")
RT = os.path.join(STATE, "rt")


def norm(s):
    return re.sub(r"\s+", " ", s.replace(" ", " ")).strip()


def bank(k):
    return norm(open(os.path.join(RT, "dip_%s.txt" % k), encoding="utf-8").read())


NODE = "German Parliaments on Atatürk — Hitler's Reichstag 1941 and the Bundestag 1983–2025"
DIP = "https://dip.bundestag.de/"
API = "Bundestag DIP API (search.dip.bundestag.de/api/v1/plenarprotokoll-text), public key from the DIP documentation page; printed page checked in the dserver PDF. "

R = [
 dict(id="stercken-1992-01-23", voice="Hans Stercken", role="CDU/CSU member of the Bundestag", dom="politics", date="1992-01-23", k="12_73", pol="admiring", inten=1, mirror="modernization-poster-child",
      pdf="https://dserver.bundestag.de/btp/12/12073.pdf", ses="12/73", page="S. 6167",
      saw="Treats the process Atatürk started as unfinished: not every Turk has yet been able to join the road to a 'new civilisation'.",
      q="Natürlich ist der Prozeß, den Atatürk eingeleitet hat, noch nicht abgeschlossen",
      tr="Of course the process that Atatürk set in motion is not yet complete",
      cav="Speaker taken from the protocol's speaker list (Stercken CDU/CSU, 6166 C) and the DIP text (his header precedes the passage, Hirsch's follows). Debate on the human-rights situation in Turkey (Kurdish question), where Poppe (same sitting) is critical. Same speaker, CDU/CSU, 30 Nov 1988 (11/112) also praises Atatürk as giving Turkey 'a new direction' (not recorded separately)."),
 dict(id="poppe-1992-01-23", voice="Gerd Poppe", role="Bündnis 90/Die Grünen member of the Bundestag", dom="politics", date="1992-01-23", k="12_73", pol="conflicted", inten=2, mirror=None,
      pdf="https://dserver.bundestag.de/btp/12/12073.pdf", ses="12/73", page="S. 6171",
      saw="Names the Kemalist dogma of one nation in one state as a founding birth defect of modern Turkey, behind the Kurdish conflict.",
      q="Der Dauerkonflikt mit der kurdischen Minderheit ist der deutlichste Ausdruck für einen der schwersten Geburtsfehler der modernen Türkei: das kemalistische Dogma, die Fiktion von einer Nation in einem Staat.",
      tr="The permanent conflict with the Kurdish minority is the clearest expression of one of the gravest birth defects of modern Turkey: the Kemalist dogma, the fiction of one nation in one state.",
      cav="Sensitive thread (Kurdish question): the vault records the speaker's framing, not its own. Poppe adds that the 'so-called Father of the Turks, Kemal Atatürk' saw this as the only chance to prevent the further break-up of the multi-ethnic state (his words, same page range). The target is the 'Kemalist dogma' and Atatürk by name; polarity conflicted."),
 dict(id="althammer-1983-06-15", voice="Dr. Althammer (CDU/CSU)", role="CDU/CSU member of the Bundestag (as printed in the protocol; first name not given in the DIP text)", dom="politics", date="1983-06-15", k="10_13", pol="instrumental", inten=1, mirror="modernization-poster-child",
      pdf="https://dserver.bundestag.de/btp/10/10013.pdf", ses="10/13", page="S. 793",
      saw="Defends the Turkish army's tie to Atatürk's principles: the man who led Turkey out of an outdated structure towards modern Western development.",
      q="Das Militär in der Türkei hat eine jahrzehntealte Verpflichtung an die Grundsätze Atatürks, der dieses Land aus einer veralteten Struktur herausgeführt und sich bemüht hat, durch seine Grundsätze die Türkei einer modernen westlichen Entwicklung zu öffnen.",
      tr="The military in Turkey has a decades-old commitment to the principles of Atatürk, who led this country out of an outdated structure and tried through his principles to open Turkey to a modern Western development.",
      cav="Used to defend the post-1980 Turkish military regime in a Bundestag debate on Turkey, hence instrumental; the SPD member Luuk replies in the same debate that Atatürk made modern Turkey 'together with the army' and that the hope of that tradition has been 'bitterly disappointed' (not recorded separately). First name not printed in the DIP text; identification beyond the printed name is not attempted."),
 dict(id="emmerlich-1983-09-08", voice="Dr. Emmerlich (SPD)", role="SPD member of the Bundestag (as printed in the protocol; first name not given in the DIP text)", dom="politics", date="1983-09-08", k="10_19", pol="admiring", inten=1, mirror=None,
      pdf="https://dserver.bundestag.de/btp/10/10019.pdf", ses="10/19", page="S. 1313",
      saw="Remembers 'Kemal Atatürk's Turkey' as a safe refuge for many Nazi victims, Ernst Reuter among them, an obligation for German extradition policy.",
      q="daß die Türkei Kemal Atatürks für viele Nazi-Verfolgte — z. B. Ernst Reuter — eine Zufluchtsstätte war, in der sie vor einer Auslieferung sicher sein konnten",
      tr="that Kemal Atatürk's Turkey was a place of refuge for many victims of Nazi persecution, for example Ernst Reuter, where they were safe from extradition",
      cav="Used in a 1983 debate on extradition of Turkish asylum-seekers, to argue a German duty from history; the praise is of the Republic's asylum role, and the speaker's name is printed without a first name."),
 dict(id="fischer-1999-12-16", voice="Joschka Fischer", role="Foreign Minister and Vice-Chancellor of Germany (Bündnis 90/Die Grünen)", dom="diplomacy", date="1999-12-16", k="14_79", pol="admiring", inten=2, mirror="modernization-poster-child",
      pdf="https://dserver.bundestag.de/btp/14/14079.pdf", ses="14/79", page="S. 7228",
      saw="Argues that Atatürk founded the Turkish state on a European orientation, so a European No would collapse Turkey's whole inner state idea.",
      q="daß Atatürk das türkische Staatswesen auf eine europäische Orientierung gegründet hat. Wenn dieses Europa jetzt im Werden Nein sagt, kollabiert im Grunde genommen die gesamte innere Staatsidee der Türkei, die sich nach Europa orientiert",
      tr="that Atatürk founded the Turkish state on a European orientation. If this Europe now in the making says No, the whole inner state idea of Turkey, which is oriented towards Europe, basically collapses",
      cav="Statement to the Bundestag on the Helsinki European Council (Turkey made an EU candidate), answering Wolfgang Gerhardt (FDP). The DIP text carries a stray column label ('Bundesminister Joseph Fischer') inside the sentence, which the quote omits; the PDF page was read. Instrumental use is part of the argument (a case for Turkey's candidacy) but the claim about Atatürk's founding idea is his own."),
 dict(id="fischer-2002-10-29", voice="Joschka Fischer", role="Foreign Minister of Germany (Bündnis 90/Die Grünen)", dom="diplomacy", date="2002-10-29", k="15_4", pol="admiring", inten=1, mirror="modernization-poster-child",
      pdf="https://dserver.bundestag.de/btp/15/15004.pdf", ses="15/4", page="S. 96",
      saw="Names 'the modernizers since Kemal Atatürk' as the civil forces in Turkey that closing the EU door would hurt; modernization means orienting to Europe.",
      q="damit für die zivilen Kräfte in der Türkei und für die Modernisierer seit Kemal Atatürk die Tür schließen; denn Modernisierung in der Türkei bedeutet Orientierung an Europa.",
      tr="you thereby close the door on the civil forces in Turkey and on the modernizers since Kemal Atatürk; for modernization in Turkey means orientation towards Europe.",
      cav="Reply to Wolfgang Schäuble (CDU/CSU) in the foreign-policy debate after the 2002 election; Fischer's speech starts at the header 'Joseph Fischer, Bundesminister des Auswärtigen' on the same protocol. A passing but explicit evaluation (Atatürk as the start of a modernizing line); printed page read as 96 in the PDF header."),
 dict(id="schroeder-2002-12-04", voice="Gerhard Schröder", role="Chancellor of Germany (SPD)", dom="politics", date="2002-12-04", k="15_13", pol="instrumental", inten=1, mirror="modernization-poster-child",
      pdf="https://dserver.bundestag.de/btp/15/15013.pdf", ses="15/13", page="S. 884",
      saw="Calls Atatürk the founder ('Staatsgründer') of a secular Turkey and a German national interest in supporting the forces that want it.",
      q="dass wir ein großes, ein gemeinsames – ich sage: ein nationales – deutsches Interesse daran haben, dass in der Türkei die Kräfte unterstützt werden, die eine säkularisierte Türkei im Sinne ihres Staatsgründers Atatürk wollen und dafür auch einstehen",
      tr="that we have a great, a shared — I say: a national — German interest in supporting in Turkey the forces that want a secularised Turkey in the spirit of its state founder Atatürk and stand up for it",
      cav="Government statement before the Copenhagen European Council, in reply to the CDU/CSU's Turkey line; the speech is Schröder's (header 'Gerhard Schröder, Bundeskanzler', no other speaker header between it and the passage, interjections by Glos, Ramsauer and Merkel noted). Used to argue for EU accession talks, so instrumental."),
 dict(id="weisskirchen-2004-12-16", voice="Gert Weisskirchen", role="SPD member of the Bundestag, foreign-policy spokesman", dom="politics", date="2004-12-16", k="15_148", pol="admiring", inten=2, mirror="modernization-poster-child",
      pdf="https://dserver.bundestag.de/btp/15/15148.pdf", ses="15/148", page="S. 13807",
      saw="Reads Atatürk's 1920s concept as the attempt to Europeanise Turkey and link it to European values, a break with the Ottoman Empire.",
      q="Das Konzept, das Kemal Atatürk in den 20er-Jahren entwickelt hat, ist der Versuch, die Türkei zu europäisieren und den Anschluss an Europa – das betrifft auch die europäischen Werte – zu erreichen.",
      tr="The concept that Kemal Atatürk developed in the 1920s is the attempt to Europeanise Turkey and to gain connection to Europe — which also concerns European values.",
      cav="Debate on the opening of EU accession talks with Turkey (the Bundestag session before the Council of 16-17 December 2004); he continues that the Republic made a 'break with the Ottoman Empire' and that the struggle inside Turkey over this concept is difficult. Speaker per the protocol (last speaker named by the chair, Gert Weisskirchen (Wiesloch)). Printed page 13807 from the PDF header."),
 dict(id="jung-2016-11-10", voice="Franz Josef Jung", role="CDU/CSU member of the Bundestag, former Federal Minister of Defence", dom="politics", date="2016-11-10", k="18_199", pol="admiring", inten=1, mirror="modernization-poster-child",
      pdf="https://dserver.bundestag.de/btp/18/18199.pdf", ses="18/199", page="S. 19806",
      saw="Sets Erdoğan's politics against 'the land of Kemal Atatürk', whose politics he says Erdoğan's now has nothing to do with.",
      q="denkt man an die Entwicklung in der Türkei, im Land Kemal Atatürks, muss man leider feststellen, dass die Politik von Präsident Erdogan mit der Politik von Kemal Atatürk nun wahrlich nichts mehr zu tun hat.",
      tr="if one thinks of the development in Turkey, in the land of Kemal Atatürk, one must unfortunately state that President Erdoğan's politics now truly have nothing to do with the politics of Kemal Atatürk.",
      cav="Debate on the situation in Turkey after the arrest of HDP leaders (Nov 2016). Atatürk is the foil for a criticism of Erdoğan, which is the speaker's main purpose; nothing about Atatürk's own record is argued."),
 dict(id="muentefering-2016-11-10", voice="Michelle Müntefering", role="SPD member of the Bundestag", dom="politics", date="2016-11-10", k="18_199", pol="conflicted", inten=1, mirror=None,
      pdf="https://dserver.bundestag.de/btp/18/18199.pdf", ses="18/199", page="S. 19812",
      saw="Describes Turkey's turn from the West as a course begun by the 'not undisputed' state founder Mustafa Kemal Atatürk, commemorated that day.",
      q="Das ist eine Entwicklung, die von dem nicht unumstrittenen Staatsgründer Mustafa Kemal Atatürk einst begründet wurde und an den übrigens heute in der ganzen Türkei im Rahmen eines Gedenktages erinnert wird.",
      tr="That is a development which was once founded by the not undisputed state founder Mustafa Kemal Atatürk and which, by the way, is being commemorated throughout Turkey today on a day of remembrance.",
      cav="Same debate as Jung (the date, 10 November, is the anniversary of Atatürk's death). She speaks as chair of the Bundestag friendship group with Turkey (her own words in the same speech); the sentence directly follows 'Turkey seems to be turning more and more away from its orientation to the West'. The comment 'not undisputed' is the only evaluation."),
 dict(id="hampel-2018-09-27", voice="Armin-Paulus Hampel", role="AfD member of the Bundestag, foreign-policy speaker", dom="politics", date="2018-09-27", k="19_52", pol="admiring", inten=2, mirror=None,
      pdf="https://dserver.bundestag.de/btp/19/19052.pdf", ses="19/52", page="S. 5420",
      saw="Calls Atatürk the state founder under whom Turkey was NATO's and Europe's cornerstone toward the Orient; today's Turkey, he says, would answer differently.",
      q="Die Türkei war einmal im Sinne des Staatsgründers Kemal Atatürk der Eckpfeiler der NATO, der Eckpfeiler Europas hin zum Orient.",
      tr="Turkey once was, in the spirit of the state founder Kemal Atatürk, the cornerstone of NATO, the cornerstone of Europe towards the Orient.",
      cav="AfD foreign-policy speech in the debate on the EU-Turkey refugee agreement; Hampel then quotes 'there are many cultures but only one civilisation: the European' as Atatürk's answer and adds that 'if you say that today in Ankara or Istanbul you will get other answers'. The identical quotation is repeated in his speech of 30 Sept 2020 (19/179, p. 22564), a second record is not made. The quotation's attribution to Atatürk is the speaker's, not verified here."),
 dict(id="gauland-2025-09-11", voice="Alexander Gauland", role="AfD member of the Bundestag, honorary chairman", dom="politics", date="2025-09-11", k="21_21", pol="instrumental", inten=1, mirror=None,
      pdf="https://dserver.bundestag.de/btp/21/21021.pdf", ses="21/21", page="S. 2170",
      saw="Uses Atatürk's omnipresent image in Turkey, though the secularist founder stands far from Erdoğan's government, as an example of nations honouring their founders.",
      q="So ist im öffentlichen Raum der Türkei das Bild von Kemal Atatürk omnipräsent, obwohl der Begründer der modernen Türkei als Laizist der Regierung Erdoğan so fernsteht",
      tr="Thus in Turkey's public space the image of Kemal Atatürk is omnipresent, although the founder of modern Turkey, as a secularist, stands so far from the Erdoğan government",
      cav="Quote ends before an interjection by Gökay Akbulut (Die Linke); the sentence goes on 'as the German founder of the Reich stood from today's German left'. The point is a German argument about national self-understanding, so Atatürk is an example, not the subject: instrumental, intensity 1."),
]
R = [r for r in R if r['id'] not in {'gauland-2025-09-11'}]  # dropped at the independent check (no stated view)

bad = []
for r in R:
    t = bank(r["k"])
    for part in re.split(r"\s…\s", r["q"]):
        if norm(part) not in t:
            bad.append((r["id"], part[:50]))
if bad:
    sys.exit("quote not found in DIP bank: %s" % bad)
for r in R:
    assert len(r["saw"].split()) <= 25, (r["id"], len(r["saw"].split()))

ERA = "posthumous"
CTRY = {"10": ("West Germany", "Germany"), "11": ("West Germany", "Germany")}
with open(os.path.join(STATE, "gazes_reichstag.jsonl"), "w", encoding="utf-8") as f:
    for r in R:
        wp = r["k"].split("_")[0]
        c, cn = CTRY.get(wp, ("Germany", "Germany"))
        cite = "Deutscher Bundestag, Plenarprotokoll %s, session of %s, %s" % (r["ses"], r["date"], r["page"])
        rec = {"id": r["id"], "voice": r["voice"], "voice_type": "person", "role": r["role"], "country": c, "country_now": cn,
               "domain": r["dom"], "date": r["date"], "era": ERA, "mirror": r["mirror"], "polarity": r["pol"],
               "intensity": r["inten"], "what_they_saw": r["saw"],
               "quote": r["q"] + " [translation: " + r["tr"] + "]", "artifact": "speech", "evidence": "P", "mediated_by": None,
               "caveat": API + r["cav"] + " Cited as " + cite + ".", "node": NODE, "sources": [r["pdf"], DIP]}
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")

# --- Hitler 4 May 1941: German original (upgrade of record hitler-1941-05-04) ---
HQ = ("Der große geniale Neuschöpfer der jungen Türkei gab als erster ein wunderbares Vorbild für die Erhebung der damals vom Glück verlassenen "
      "und vom Schicksal so entsetzlich geschlagenen Verbündeten.")
HCTX = ("Die Türkei war im Weltkrieg unser Verbündeter. Sein unglücklicher Ausgang lastete auf diesem Land genau so schwer wie auf uns selbst. " + HQ +
        " Während sich nun die Türkei dank der realistischen Haltung ihrer Staatsführung die Unabhängigkeit des eigenen Entschlusses wahrte, fiel Jugoslawien den britischen Intrigen zum Opfer.")
HSRC = "https://www.digitale-sammlungen.de/en/view/bsb00000613?page=86"
upg = {"id": "hitler-1941-05-04", "action": "upgrade", "quote_de": HQ,
       "quote_en_bbc": "The great and ingenious reconstructor of the new Turkey gave his Allies, beaten by fate, the first example of resurrection.",
       "quote_en_check": "The great, ingenious re-creator of the young Turkey gave as the first a wonderful model for the rising of the allies, at that time abandoned by fortune and so terribly beaten by fate.",
       "context_de": HCTX,
       "location": "Verhandlungen des Deutschen Reichstags, 4. Wahlperiode 1939, Bd. 460 (BSB bsb00000613), 6. Sitzung, Sonntag den 4. Mai 1941, printed p. 85 (image 86), right column, section (C)",
       "url": HSRC, "evidence": "P",
       "notes": "The German is 'Neuschöpfer der jungen Türkei', not 'Neugestalter der neuen Türkei'; the BBC rendering 'reconstructor of the new Turkey' and 'first example of resurrection' is a loose translation. Read on the page image (full-text index of the Reichstag site lacks this volume; the MDZ OCR is garbled Fraktur but reads 'Neuschöpker der jungen Türkei'). Atatürk is not named; the sentence is preceded by 'Die Türkei war im Weltkrieg unser Verbündeter'."}
with open(os.path.join(STATE, "upgrade_hitler-1941-05-04.json"), "w", encoding="utf-8") as f:
    json.dump(upg, f, ensure_ascii=False, indent=1)

with open(os.path.join(STATE, "ledger_reichstag.md"), "w", encoding="utf-8") as f:
    f.write("| Claim | Node | Status | Sources | Next step |\n|---|---|---|---|---|\n")
    f.write("| Hitler 4 May 1941 Reichstag: German original 'der große geniale Neuschöpfer der jungen Türkei' (upgrade of hitler-1941-05-04) | %s | verified P (page image read, printed p. 85) | %s | none |\n" % (NODE, HSRC))
    for r in R:
        f.write("| %s (%s): %s | %s | verified P (DIP full text + dserver PDF page, read) | %s | none |\n" % (r["voice"], r["date"], r["saw"], NODE, r["pdf"]))

SP = {"Joschka Fischer": ("German", "b. 1948", "foreign minister", "fischer-1999-12-16"), "Gerhard Schröder": ("German", "b. 1944", "chancellor", "schroeder-2002-12-04"),
      "Gert Weisskirchen": ("German", "", "SPD foreign-policy spokesman", "weisskirchen-2004-12-16"), "Franz Josef Jung": ("German", "b. 1949", "politician", "jung-2016-11-10"),
      "Michelle Müntefering": ("German", "", "politician", "muentefering-2016-11-10"), "Armin-Paulus Hampel": ("German", "", "AfD politician", "hampel-2018-09-27"),
      "Hans Stercken": ("German", "", "CDU politician", "stercken-1992-01-23"),
      "Gerd Poppe": ("German", "", "Bündnis 90 politician", "poppe-1992-01-23")}
byid = {r["id"]: r for r in R}
for name, (nat, life, tag, rid) in SP.items():
    r = byid[rid]
    person(name, role=r["role"], nat=nat, life="", stance="%s (%s)" % (r["pol"], r["date"][:4]),
           tags=["verified", tag.replace(" ", "-"), "bundestag"],
           body="%s. Spoke of Atatürk in the Bundestag on %s; see [[%s]].\n\n## Sources\n- Deutscher Bundestag, Plenarprotokoll %s, %s: %s\n" % (r["role"], r["date"], NODE, r["ses"], r["page"], r["pdf"]))


def sec(r):
    return "## %s — %s, %s\n\n%s\n\n> %s\n> (translation: %s)\n\n**Caveat.** %s\n" % (
        r["voice"], r["ses"], r["date"], r["saw"], r["q"], r["tr"], r["cav"])


body = ("Two seams in German parliamentary record. (1) The **Reichstag**: the German original of [[Adolf Hitler]]'s speech of 4 May 1941, read on the page image of "
        "the Bayerische Staatsbibliothek's digitised *Verhandlungen des Reichstags*. (2) The **Bundestag**: the plenary protocols in the DIP database, scanned in full for "
        "Atatürk and Kemal; the records below are the speeches in which a named member states a view of him.\n\n"
        "## Hitler, Reichstag, 4 May 1941 — the German original\n\n"
        "In the speech on the Balkan campaign Hitler says of Turkey, the former ally of the World War:\n\n"
        "> " + HQ + "\n> (translation: The great, ingenious creator of the young Turkey was the first to give a wonderful model for the rising of the allies, then abandoned by fortune and so terribly struck by fate.)\n\n"
        "Atatürk is not named. The speech reads 'Neuschöpfer der jungen Türkei' (not 'Neugestalter der neuen Türkei'); the BBC translation in the dataset record "
        "('reconstructor of the new Turkey', 'first example of resurrection') is loose. It is followed by praise of the Turkish state leadership's 'realistic attitude'; "
        "the passage serves a contrast with Yugoslavia. Place: Reichstag, 4. Wahlperiode, 6. Sitzung, Sonntag den 4. Mai 1941, printed p. 85, right column (C); "
        "BSB bsb00000613, image 86: " + HSRC + "\n\n"
        "## Bundestag speeches\n\n" + "\n".join(sec(r) for r in R) +
        "\n## Sources\n- " + HSRC + " (Reichstag 4 May 1941, p. 85)\n- Deutscher Bundestag, DIP: " + DIP + "\n"
        + "\n".join("- Plenarprotokoll %s: %s" % (r["ses"], r["pdf"]) for r in R) + "\n")
note("Events", NODE, {"type": "event", "when": "1941; 1983–2025", "tags": ["event", "verified", "germany", "parliament"]}, body)
print("ok", len(R))
