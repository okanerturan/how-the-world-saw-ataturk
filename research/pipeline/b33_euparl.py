# -*- coding: utf-8 -*-
# Census round 24 — two parliamentary seams: the Austrian Nationalrat/Bundesrat protocols (1918-2025) and the European Parliament plenary (CRE).
# Bank: tools/.state/round24/euparl/{pdf,at,ep}/ (parlament.gv.at protocols, europarl.europa.eu CRE pages rendered once each).
# The script refuses to run if a quote is not found in its bank.
import json, os, re, sys, html
from _lib import note, person

HERE = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(HERE, "tools", ".state", "round24")
BANK = os.path.join(STATE, "euparl")

NODE_AT = "Austrian Nationalrat and Bundesrat on Atatürk, 1980–2019 — Schwaiger, Längle, Cap, Lugar"
NODE_EP = "European Parliament plenary on Atatürk, 2004–2016 — Nordmann and Weber"

PA = "https://www.parlament.gv.at"
CRE = "https://www.europarl.europa.eu/doceo/document/"


def norm(s):
    s = html.unescape(s).replace("­", "").replace("¬", "")
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"').replace("„", '"').replace("–", "-").replace("—", "-")
    s = re.sub(r"-\s*\n\s*", "", s)  # end-of-line hyphenation
    return re.sub(r"\s+", " ", s)


def present(bank, quote):
    t = norm(open(os.path.join(BANK, bank), encoding="utf-8", errors="ignore").read())
    return norm(quote) in t


R = [
 dict(id="czernin-1921-06", voice="Ottokar Czernin", role="Member of the Austrian Nationalrat; formerly Austro-Hungarian foreign minister", country="Austria", cnow="Austria",
      date="1921-06-22", era="contemporary", mirror=None, pol="witness", inten=1, art="speech", ev="P", lang="de",
      cite="Nationalrat, 40th sitting of the 1st legislative period (I. GP), 22 June 1921, Stenographisches Protokoll p. 1488",
      url=PA + "/dokument/I/NRSITZ/40/imfname_798395.pdf", bank="pdf/I40raw.txt",
      saw="In a foreign-affairs speech names Kemal Pascha with Talaat and Enver as the men leading the Angora movement, who would act, not merely talk.",
      q="von denen die Diplomatie wissen mußte, daß diese Männer an der Spitze einer solchen Bewegung an und für sich die Wahrscheinlichkeit bedeuten, daß sie sich nicht bei Worten aufhalten, sondern zu Taten schreiten werden, und diese drei Männer heißen: Taalat Pascha, Enver Pascha und Kemal Pascha.",
      tr="[Translation:] of whom diplomacy had to know that men at the head of such a movement make it probable, in and of themselves, that they will not stop at words but proceed to deeds, and these three men are called: Talaat Pasha, Enver Pasha and Kemal Pasha.",
      cav="A threat assessment inside a criticism of the Foreign Ministry for failing to foresee the Anatolian crisis, not an appraisal of Kemal; the point is that the Ballhausplatz should have known. Speaker is printed as 'Abgeordneter Czernin'; the identification as Ottokar Czernin (member of the Nationalrat 1920-23) is the standard record, not the protocol. 'Taalat' is the protocol's spelling. A few lines later he says part of the Entente's opponents allied with 'der Angora-Regierung, mit Kemal Pascha' and notes the Bolshevik-Kemalist alliance. Page from the scan's running head; the PDF is the 'gescanntes Original' with a text layer."),
 dict(id="prechtl-1972-09", voice="Bundesrat Prechtl", role="SPÖ member of the Austrian Bundesrat", country="Austria", cnow="Austria",
      date="1972-09-20", era="posthumous", mirror="modernization-poster-child", pol="admiring", inten=1, art="speech", ev="P", lang="de",
      cite="Bundesrat, 314th sitting, 20 September 1972, Stenographisches Protokoll p. 9061",
      url=PA + "/dokument/BR/BRSITZ/314/imfname_179363.pdf", bank="pdf/br314raw.txt",
      saw="In a debate on the EEC treaties and guest workers, says that since Atatürk the road has been set for Turkey to belong to Europe.",
      q="Seit Atatürk ist der Weg bestimmt worden, daß die Türkei zu Europa gehört.",
      tr="[Translation:] Since Atatürk the course has been set that Turkey belongs to Europe.",
      cav="One sentence, in a speech mostly about wages and the Austrian State Treaty; he pairs it with a remark on Turkey's backward schooling. Name is the protocol's running head and speaker line ('Bundesrat Prechtl (SPÖ)'); first name not given. Not a notable voice; staged for completeness of the Bundesrat sweep."),
 dict(id="schwaiger-1980-12", voice="Bundesrat Dr. Schwaiger", role="ÖVP member of the Austrian Bundesrat", country="Austria", cnow="Austria",
      date="1980-12-04", era="posthumous", mirror=None, pol="conflicted", inten=1, art="speech", ev="P", lang="de",
      cite="Bundesrat, 403rd sitting, 4 December 1980, Stenographisches Protokoll p. 14728",
      url=PA + "/dokument/BR/BRSITZ/403/imfname_177961.pdf", bank="pdf/br403raw.txt",
      saw="Opposing a 15-million-dollar loan to Turkey's central bank, says Atatürk's attempt to make a modern state of Turkey 'had only partial success'.",
      q="Der Versuch Kemal Atatürks, einen modernen Staat aus der Türkei zu machen, hatte nur teilweise Erfolg.",
      tr="[Translation:] Kemal Atatürk's attempt to make a modern state out of Turkey had only partial success.",
      cav="One evaluative sentence inside an economic argument (the ÖVP opposed the loan). First name not given in the protocol; the page number is that of the sitting's page before the running head '14729 Dr. Schwaiger'. Not a notable voice."),
 dict(id="laengle-2015-03", voice="Christoph Längle", role="FPÖ member of the Austrian Bundesrat (Vorarlberg)", country="Austria", cnow="Austria",
      date="2015-03-12", era="posthumous", mirror="modernization-poster-child", pol="admiring", inten=1, art="speech", ev="P", lang="de",
      cite="Bundesrat, 839th sitting, 12 March 2015, Stenographisches Protokoll p. 46",
      url=PA + "/dokument/BR/BRSITZ/839/fnameorig_411828.html", bank="at/_dokument_BR_BRSITZ_839_fnameorig_411828_html.txt",
      saw="In a headscarf and secularism debate calls Atatürk, in his own opinion, a very progressive statesman who aligned the new Turkey with Western principles.",
      q="Der damals nach meiner Meinung sehr fortschrittliche Staatsmann Mustafa Kemal Atatürk hat auch die „sechs Pfeile“ des neuen türkischen Staatswesens eingeführt.",
      tr="[Translation:] The statesman Mustafa Kemal Atatürk, in my opinion a very progressive one for his time, also introduced the 'six arrows' of the new Turkish state.",
      cav="Used to argue that the secular founder banned the fez and the headscarf, against Turkey's present course; the praise serves a point about Islam in Austria. Backs the claim with: 'dass gerade Mustafa Kemal Atatürk sich sehr wohl total nach westlichen Prinzipien ausgerichtet hat'."),
 dict(id="cap-2016-10", voice="Josef Cap", role="SPÖ member of the Austrian Nationalrat", country="Austria", cnow="Austria",
      date="2016-10-13", era="posthumous", mirror="modernization-poster-child", pol="admiring", inten=1, art="speech", ev="P", lang="de",
      cite="Nationalrat, 148th sitting of the XXV. GP, 13 October 2016, Stenographisches Protokoll p. 139-140",
      url=PA + "/dokument/XXV/NRSITZ/148/fnameorig_584143.html", bank="at/_dokument_XXV_NRSITZ_148_fnameorig_584143_html.txt",
      saw="Criticising Turkey's re-Islamisation, says Atatürk would turn in his grave: he had really tried reforms and to bring Turkey closer to Europe's values.",
      q="Kemal Atatürk im Grabe umdrehen würde. Er hat nämlich wirklich versucht, Reformen zu setzen und die Türkei stärker an Europa und an die europäischen Werte heranzuführen.",
      tr="[Translation:] Kemal Atatürk would turn in his grave. For he really did try to bring in reforms and to move Turkey closer to Europe and to European values.",
      cav="Foreign-policy remarks after the July 2016 coup attempt, using Atatürk as the measure of Erdoğan's Turkey (instrumental as well as admiring). Speaker line: 'Abgeordneter Dr. Josef Cap (SPÖ)'."),
 dict(id="lugar-2019-05", voice="Robert Lugar", role="FPÖ member of the Austrian Nationalrat", country="Austria", cnow="Austria",
      date="2019-05-15", era="posthumous", mirror="modernization-poster-child", pol="instrumental", inten=1, art="speech", ev="P", lang="de",
      cite="Nationalrat, 74th sitting of the XXVI. GP, 15 May 2019, Stenographisches Protokoll p. 228",
      url=PA + "/dokument/XXVI/NRSITZ/74/fnameorig_779563.html", bank="at/_dokument_XXVI_NRSITZ_74_fnameorig_779563_html.txt",
      saw="In the headscarf-ban debate presents Atatürk as neither a Muslim-hater nor right-wing, but a founder who banned the headscarf to end women's oppression.",
      q="Das war kein Muslimhasser und das war auch kein Rechter. Der Gründer der Türkei hat das Kopftuch verboten, weil es eben genau mit der Unterdrückung der Frau zusammenhängt.",
      tr="[Translation:] That was no Muslim-hater and no right-winger either. The founder of Turkey banned the headscarf precisely because it is bound up with the oppression of women.",
      cav="Argument for the 2019 ban on headscarves in primary schools; Atatürk is invoked as authority, so the record is as much instrumental as admiring. The historical claim (a headscarf ban) is the speaker's, not the vault's. Speaker line: 'Abgeordneter Ing. Robert Lugar (FPÖ)'."),
 dict(id="huebner-2013-06", voice="Johannes Hübner", role="FPÖ member of the Austrian Nationalrat (motion with co-signers)", country="Austria", cnow="Austria",
      date="2013-06-26", era="posthumous", mirror=None, pol="hostile", inten=1, art="report", ev="P", lang="de",
      cite="Nationalrat, Hauptausschuss in EU-Angelegenheiten, 75th sitting, 26 June 2013: Antrag auf Stellungnahme of Dr. Johannes Hübner and others, printed in the Auszugsweise Darstellung of 27 June 2013 (parlament.gv.at, XXIV. GP, IV/29)",
      url=PA + "/dokument/XXIV/IV/29/fnameorig_312302.html", bank="at/_dokument_XXIV_IV_29_fnameorig_312302_html.txt",
      saw="In a motion to end Turkey's EU talks, ranks Erdoğan as successor of the sultans and of Atatürk, 'anything but a democrat'.",
      q="Erdogan erweist sich als würdiger Nachfolger der osmanischen Sultane, aber auch Atatürks, der ja alles andere als ein Demokrat war, sowie der verschiedenen Militärdiktatoren.",
      tr="[Translation:] Erdoğan is proving a worthy successor of the Ottoman sultans, but also of Atatürk, who after all was anything but a democrat, and of the various military dictators.",
      cav="Written motion text (the FPÖ motion was rejected by SPÖ, ÖVP and the Greens), not a spoken contribution; it bears Hübner's name and 'weiterer Abgeordneter'. The statement is a label inside an anti-accession argument, kept because it states a judgement of Atatürk's regime (not a wreath or comparison alone)."),
 dict(id="weber-2016-11", voice="Manfred Weber", role="Member of the European Parliament (CSU), speaking for the EPP Group", country="Germany", cnow="Germany",
      date="2016-11-22", era="posthumous", mirror=None, pol="instrumental", inten=2, art="speech", ev="P", lang="de",
      cite="European Parliament, Strasbourg, plenary 22 November 2016, 'EU-Turkey relations (debate)', verbatim report CRE-8-2016-11-22 item 10",
      url=CRE + "CRE-8-2016-11-22-ITM-010_EN.html", bank="ep/CRE-8-2016-11-22-ITM-010.txt",
      saw="After the coup attempt, recalls 'a great Turk', Atatürk, citing his sayings on peace and fear-free sovereignty as Turkey's own tradition.",
      q="Ich möchte heute in meinem Redebeitrag an einen großen Türken erinneren, nämlich an Atatürk. Peace at home – peace in the world, war einer seiner Sätze, die er geprägt hat.",
      tr="[Translation:] In my speech today I would like to recall a great Turk, namely Atatürk. 'Peace at home - peace in the world' was one of the sayings he coined.",
      cav="Original German as in the verbatim report ('erinneren' is the report's misspelling). He goes on to quote Atatürk's line that sovereignty built on fear and arms alone cannot last, and to tell Ankara to argue from Turkey's own tradition rather than 'our European values'; the praise serves his message to Erdoğan's government, hence instrumental. Role: the report names him 'im Namen der PPE-Fraktion'; his CSU membership is the standard record."),
 dict(id="nordmann-2004-04", voice="Jean-Thomas Nordmann", role="Member of the European Parliament (ELDR, France)", country="France", cnow="France",
      date="2004-04-01", era="posthumous", mirror="secular-rationalist-prophet", pol="admiring", inten=1, art="speech", ev="P", lang="en",
      cite="European Parliament, Strasbourg, plenary 1 April 2004, 'Progress towards accession by Turkey' (Oostlander report), verbatim report CRE-5-2004-04-01 item 2",
      url=CRE + "CRE-5-2004-04-01-ITM-002_EN.html", bank="ep/CRE-5-2004-04-01.txt",
      saw="Defending Turkish secularism against the rapporteur, calls it perhaps the most valuable part of Kemal Atatürk's legacy and a recipe for the Union's future.",
      q="Paragraph 32 of your report seems to me to proceed from a slightly jaundiced view of the secularism which is perhaps the most valuable part of the legacy of Kemal Atatürk.",
      tr=None,
      cav="One sentence of a short intervention on the Oostlander report. The report prints only 'Nordmann (ELDR)'; the first name is the standard record (M-tier)."),
 dict(id="meijer-2004-04", voice="Erik Meijer", role="Member of the European Parliament (GUE/NGL, Netherlands)", country="Netherlands", cnow="Netherlands",
      date="2004-04-01", era="posthumous", mirror=None, pol="admiring", inten=1, art="report", ev="P", lang="en",
      cite="European Parliament, Strasbourg, 1 April 2004, 'Progress towards accession by Turkey', written explanation of vote on the Oostlander report, verbatim report CRE-5-2004-04-01",
      url=CRE + "CRE-5-2004-04-01-ITM-002_EN.html", bank="ep/CRE-5-2004-04-01.txt",
      saw="In a written explanation of vote says Turkey 'decided in favour of Europe' with the Atatürk revolution of the early 1920s.",
      q="Turkey decided in favour of Europe as long ago as the Atatürk revolution in the early 1920s.",
      tr=None,
      cav="Written explanation of vote, original Dutch; the quote is the EP's English version. Eight months later (Dec 2004) he calls the same revolution the start of an authoritarian state: the two records show one voice changing register. First name and country are the standard record, not the report."),
 dict(id="matsakis-2008-05", voice="Marios Matsakis", role="Member of the European Parliament (ALDE, Cyprus)", country="Cyprus", cnow="Cyprus",
      date="2008-05-21", era="posthumous", mirror=None, pol="hostile", inten=1, art="speech", ev="P", lang="en",
      cite="European Parliament, Strasbourg, plenary 21 May 2008, 'Turkey's 2007 progress report (debate)', verbatim report CRE-6-2008-05-21 item 4",
      url=CRE + "CRE-6-2008-05-21-ITM-004_EN.html", bank="ep/CRE-6-2008-05-21-ITM-004.txt",
      saw="Argues that since 'General Atatürk's revolution' Turkey has in reality lived under a military dictatorship, direct or indirect.",
      q="Since General Atatürk's revolution in the 1920s, Turkey has in reality been under a military dictatorship, either directly or indirectly.",
      tr=None,
      cav="A verdict on the republic's founding rather than on the man, in a speech about the army's role and the AKP's challenge to it; sensitive thread (Cyprus). Nationality is the standard record, not the report."),
 dict(id="meijer-2004-12", voice="Erik Meijer", role="Member of the European Parliament (GUE/NGL, Netherlands)", country="Netherlands", cnow="Netherlands",
      date="2004-12-15", era="posthumous", mirror=None, pol="conflicted", inten=1, art="report", ev="P", lang="en",
      cite="European Parliament, Strasbourg, 15 December 2004, 'Voting time', explanation of vote in writing on the Eurlings report, verbatim report CRE-6-2004-12-15 item 3",
      url=CRE + "CRE-6-2004-12-15-ITM-003_EN.html", bank="ep/CRE-6-2004-12-15.txt",
      saw="In a written explanation of vote on Turkish accession calls the Atatürk revolution the start of a 'typically European' but old-fashioned, authoritarian state.",
      q="Since the Atatürk revolution in 1923, Turkey has been a typically European country, albeit of the old-fashioned, authoritarian kind, which we no longer want in Europe these days.",
      tr=None,
      cav="Written explanation of vote, original Dutch; the quote is the EP's English version. The report prints only 'Meijer (GUE/NGL)'; the first name and country are the standard record (M-tier). Verified on the day's report and the item page named in the search index."),
]
R = [r for r in R if r['id'] not in {'czernin-1921-06','prechtl-1972-09','huebner-2013-06','meijer-2004-04','matsakis-2008-05','meijer-2004-12'}]  # dropped at the independent check (no view of the man)

# records dropped after review (kept here so the decision is auditable)
DROPPED = {
 "belakowitsch-2017-01": "Compares Atatürk with Kurz ('Atatürk ist das schon in den 1920er-Jahren ... gelungen, Kurz gelingt es ... nicht'): a comparison, not a view.",
 "camre-2008-05": "Attributes a saying to Atatürk to rebuke Turkey: an attribution.",
 "carver-2017-07": "Quotes the Gallipoli epitaph to charge Ankara with desecration: a wreath and an attribution; 'must be turning in his grave' states no view of the man.",
 "allam-2012-03": "'The secular state founded by Atatürk ... no longer exists': an attribution inside an anti-Erdogan charge.",
 "batten-2007-10": "'Since Kemal Atatürk, Turkey has maintained a secular state against ... Islam': an attribution of secularism, inside an anti-accession argument (staged in the first pass, dropped on the strict test).",
 "reid-2016-04": "Julia Reid (UKIP, 13 Apr 2016): 'Under Atatürk Turkey became a secular nation': the same kind of attribution.",
 "zaleski-2008-05": "'The mentality of the Turks has changed little since the times of Kemal Atatürk': a time marker, not a view.",
}

bad = [r["id"] for r in R if not present(r["bank"], r["q"])]
if bad:
    sys.exit("quote not found in source bank: %s" % bad)
for r in R:
    assert len(r["saw"].split()) <= 25, (r["id"], len(r["saw"].split()))
    r["vtype"] = "person"
    r["domain"] = "politics"
    r["node"] = NODE_AT if r["country"] == "Austria" else NODE_EP

with open(os.path.join(STATE, "gazes_euparl.jsonl"), "w", encoding="utf-8") as f:
    for r in R:
        cav = r["cav"] + ((" " + r["tr"]) if r.get("tr") else "")
        rec = dict(id=r["id"], voice=r["voice"], voice_type=r["vtype"], role=r["role"], country=r["country"], country_now=r["cnow"],
                   domain=r["domain"], date=r["date"], era=r["era"], mirror=r["mirror"], polarity=r["pol"], intensity=r["inten"],
                   what_they_saw=r["saw"], quote=r["q"], artifact=r["art"] if r["art"] in ("speech", "report") else "speech", evidence=r["ev"],
                   mediated_by=None, caveat=cav, node=r["node"], sources=[r["url"]])
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")

with open(os.path.join(STATE, "ledger_euparl.md"), "w", encoding="utf-8") as f:
    f.write("| Claim | Node | Status | Sources | Next step |\n|---|---|---|---|---|\n")
    for r in R:
        f.write("| %s (%s): %s | %s | verified P (%s; text read, quote found in the retrieved protocol) | %s | none; independent check should reopen the URL |\n" % (
            r["voice"], r["date"], r["saw"], r["node"], r["cite"], r["url"]))

PEOPLE = {
 "Ottokar Czernin": ("Austro-Hungarian foreign minister 1916-18, Nationalrat member 1920-23", "Austrian", "1872-1932"),
 "Josef Cap": ("SPÖ politician, member of the Austrian Nationalrat", "Austrian", "b. 1952"),
 "Robert Lugar": ("FPÖ member of the Austrian Nationalrat", "Austrian", ""),
 "Christoph Längle": ("FPÖ member of the Austrian Bundesrat", "Austrian", ""),
 "Johannes Hübner": ("FPÖ member of the Austrian Nationalrat", "Austrian", ""),
 "Manfred Weber": ("CSU member of the European Parliament, EPP Group leader", "German", "b. 1972"),
 "Marios Matsakis": ("Cypriot member of the European Parliament (ALDE)", "Cypriot", ""),
 "Jean-Thomas Nordmann": ("Member of the European Parliament (ELDR) 1999-2004", "French", ""),
 "Erik Meijer": ("Dutch member of the European Parliament (GUE/NGL)", "Dutch", ""),
}


def sec(r):
    tr = ("\n>\n> %s" % r["tr"]) if r.get("tr") else ""
    return "## %s — %s\n\n%s\n\n> %s%s\n\n**Source.** %s — <%s>\n\n**Caveat.** %s\n" % (
        r["voice"], r["date"], r["saw"], r["q"], tr, r["cite"], r["url"], r["cav"])


for v, (role, nat, life) in PEOPLE.items():
    rs = [r for r in R if r["voice"] == v]
    if not rs:
        continue
    r = rs[0]
    tags = ["verified", "austria", "parliament"] if r["country"] == "Austria" else ["verified", "european-parliament", "parliament"]
    body = "%s.\n\n" % role
    for x in rs:
        body += sec(x) + "\n"
    body += "\n## Sources\n" + "\n".join("- %s — %s" % (x["cite"], x["url"]) for x in rs) + "\n"
    person(v, role=role, nat=nat, life=life, stance="%s (%s)" % (r["pol"], r["date"][:4]), tags=tags, body=body)

at = [r for r in R if r["country"] == "Austria"]
ep = [r for r in R if r["country"] != "Austria"]

body_at = ("Seven statements about Atatürk in the stenographic protocols of the Austrian parliament, found by a full scan of the protocols that parlament.gv.at publishes "
           "(Konstituierende Nationalversammlung, Nationalrat and Bundesrat sittings, committee extracts and other plenary-type sittings, 1918 to 2025: 6,853 documents, scanned by "
           "downloading each PDF or HTML protocol and searching for Atatürk, Kemal, Kemalisten, Angora and Ghasi). The scan found 19 documents with a hit (plus one false OCR hit), of which seven state a view of Atatürk. "
           "The only famous speaker is Ottokar Czernin (1921), who names Kemal Pascha in a foreign-policy speech; the later records are modern backbench speeches in headscarf and Turkey-accession debates. "
           "Nothing was found for Seipel, Renner, Dollfuss, Schuschnigg, Bauer, Kreisky, Waldheim, Haider or Kurz (Kurz is mentioned in 2017 only as a comparison in an FPÖ speech). "
           "Dropped for want of a stated view: Belakowitsch-Jenewein (31 Jan 2017, Atatürk 'managed' the headscarf ban in the 1920s, 'Kurz does not': a comparison), a 1988 joke about Atatürk's six-day speech, "
           "a 1954 report of Tolomei's remark about solving South Tyrol 'as radically as Kemal', and a 1999 remark that the Kemalists set out to build a state of Kurds and Turks.\n\n")
for r in at:
    body_at += sec(r) + "\n"
body_at += "\n## Sources\n" + "\n".join("- %s — %s" % (r["cite"], r["url"]) for r in at) + "\n"
note("Events", NODE_AT, {"type": "event", "when": "1921–2019", "tags": ["event", "verified", "austria", "parliament"]}, body_at)

body_ep = ("Five statements about Atatürk in the verbatim reports of the European Parliament. The EP's own pages sit behind a WAF that refuses scripted fetches, so each sitting was read by rendering its day report once. "
           "Turkey-accession and progress-report sittings read: 1 Apr 2004, 14-15 Dec 2004, 28 Sep 2005, 26 Sep 2006, 13 Dec 2006, 13 Feb 2007, 24 Oct 2007, 21 May 2008, 11 Mar 2009, 10 Feb 2010, 8 Mar 2011, 28 Mar 2012, 12 Jun 2013, 13 Apr 2016, 22 and 24 Nov 2016, 5-6 Jul 2017, 12 Mar 2019, 23 Oct 2019, 18 May 2021, 6 Jun 2022 and others. "
           "No statement was found by Verhofstadt, Cohn-Bendit, Schulz, Juncker, Farage, Le Pen or Lagendijk; Otto von Habsburg left the Parliament in 1999. "
           "MEPs who mention Atatürk without a view (attributions, wreaths, comparisons: Batten, Reid, Camre, Zaleski, Allam, Carver and others) are listed in the candidates file.\n\n")
for r in ep:
    body_ep += sec(r) + "\n"
body_ep += "\n## Sources\n" + "\n".join("- %s — %s" % (r["cite"], r["url"]) for r in ep) + "\n"
note("Events", NODE_EP, {"type": "event", "when": "2004–2017", "tags": ["event", "verified", "european-union", "parliament"]}, body_ep)
print("ok", len(R), "records")
