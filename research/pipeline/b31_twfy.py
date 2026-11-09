# -*- coding: utf-8 -*-
# Census round 22 (Nov 2026) — Westminster after 1938 via TheyWorkForYou (transcription of Hansard; evidence P).
# Banks: tools/.state/round22/<tag>.txt (the fetched TWFY debate pages). Script refuses to run if a quote is not in its bank.
import json, os, re, sys, unicodedata
from _lib import note, person

HERE = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(HERE, "tools", ".state", "round22")
N1 = "Westminster on Atatürk, 1941–1957 — Eden, Selwyn Lloyd, Noel-Baker, Wigg, Davies and Hollis"
N2 = "Westminster on Atatürk, 1988–2004 — Corbyn, MacShane and Patten"
TW = "https://www.theyworkforyou.com"


def norm(s):
    s = unicodedata.normalize("NFKC", s)
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = re.sub(r"\s+", " ", s)
    return s.strip().lower()


def bank(f):
    return norm(open(os.path.join(STATE, f), encoding="utf-8").read())


R = [
 dict(id="churchill-1944-08", voice="Winston Churchill", role="British Prime Minister (Commons statement on Turkey breaking with Germany)", dom="politics", date="1944-08-02", era="posthumous",
      mirror=None, pol="instrumental", inten=2, art="speech", f="churchill1944.txt", tag=N1,
      saw="Cites Kemal's policy of close Russian-Turkish unity, which 'endeavoured to bring to an end the antagonism of centuries', as ground for hope of Turkish-Soviet friendship.",
      q="It was the policy of Mustapha Kemal to bring about close unity of action between the Russian and Turkish people. The elements are all there and he endeavoured to bring to an end the antagonism of centuries.",
      src=TW + "/debates/?id=1944-08-02a.1459.5#g1474.1", loc="War Situation, HC Deb 2 Aug 1944, c1474",
      cav="Statement announcing Turkey had broken off relations with Germany. Churchill states no verdict on Kemal himself; he invokes Kemal's Russian policy to support the new Turkish-Soviet outlook, so recorded as instrumental. Churchill's earlier Commons mentions (22 Mar 1920, 14 Jun 1921 'Kemalist ... sources') are procedural and not recorded here."),
 dict(id="eden-1941-08", voice="Anthony Eden", role="British Foreign Secretary", dom="politics", date="1941-08-06", era="posthumous",
      mirror="modernization-poster-child", pol="admiring", inten=2, art="speech", f="eden1941.txt", tag=N1, pid=None,
      saw="Foreign Secretary tells the Commons the post-war world will have a noble part for 'the Turkey re-created by the genius of Ataturk'.",
      q="In that world the Turkey re-created by the genius of Ataturk will have a noble part to play and, in doing so, Turkey will decide her own course and she will choose her own collaborators.",
      src=TW + "/debates/?id=1941-08-06a.1973.2#g2039.1", loc="Orders of the Day — War Situation, HC Deb 6 Aug 1941, c2039",
      cav="Speech reassuring Turkey that Britain would not trade her interests away; praise is of the state Atatürk 're-created', in a diplomatic setting."),
 dict(id="eden-1942-01", voice="Anthony Eden", role="British Foreign Secretary (report on his Moscow visit)", dom="politics", date="1942-01-08", era="posthumous",
      mirror=None, pol="instrumental", inten=1, art="speech", f="eden1942.txt", tag=N1,
      saw="Calls Atatürk 'the great leader of modern Turkey' and cites his principle of Russo-Turkish understanding as policy whose wisdom grows in war.",
      q="It was a cardinal principle of the policy of modern Turkey, as laid down by Ataturk, the great leader of modern Turkey, that there should be close understanding between Russia and Turkey. The wisdom of that policy becomes daily more apparent amid the vicissitudes of war.",
      src=TW + "/debates/?id=1942-01-08a.43.15#g171.1", loc="War Situation, HC Deb 8 Jan 1942, c171",
      cav="Used to reassure Turkey after Anglo-Soviet talks; Atatürk is invoked for the Russian policy, not assessed as a whole."),
 dict(id="clement-davies-1955-12", voice="Clement Davies", role="Leader of the Liberal Party, MP (Montgomeryshire)", dom="politics", date="1955-12-05", era="posthumous",
      mirror=None, pol="admiring", inten=1, art="speech", f="davies1955.txt", tag=N1,
      saw="Says the Turks established 'their great tradition under that amazing man, Ataturk', but that Turkey should not decide Cyprus.",
      q="Certainly, ever since the Turks established their great tradition under that amazing man, Ataturk, one has had great admiration for these people.",
      src=TW + "/debates/?id=1955-12-05a.32.0#g91.1", loc="Cyprus, HC Deb 5 Dec 1955, c91",
      cav="Cyprus debate (sensitive thread): the praise is a preface to an argument against Turkish interference; recorded as the speaker's framing."),
 dict(id="hollis-1953-10", voice="Christopher Hollis", role="Conservative MP and writer", dom="politics", date="1953-10-28", era="posthumous",
      mirror=None, pol="admiring", inten=1, art="speech", f="hollis1953.txt", tag=N1,
      saw="Credits 'the statesman Kemal Ataturk' with ending the ancient enmity between Greece and Turkey by exchange of populations, a model for Trieste.",
      q="We all know the history of how the ancient enmity between Greece and Turkey was ended by an agreement between those two countries for exchange of populations brought about by the statesman Kemal Ataturk.",
      src=TW + "/debates/?id=1953-10-28a.2808.0#g2835.3", loc="European Affairs and Trieste, HC Deb 28 Oct 1953, c2835",
      cav="Sensitive thread (the 1923 population exchange): this is Hollis's framing, as a precedent for Trieste; the vault does not adopt it."),
 dict(id="selwyn-lloyd-1956-07", voice="Selwyn Lloyd", role="British Foreign Secretary", dom="politics", date="1956-07-19", era="posthumous",
      mirror="chivalrous-enemy", pol="admiring", inten=1, art="speech", f="lloyd1956.txt", tag=N1,
      saw="Foreign Secretary credits Kemal Ataturk and Venizelos with building a new Greek-Turkish friendship, jeopardised by the Cyprus dispute.",
      q="Everyone will bear in mind the work of Kemal Ataturk and Venizelos in building up a new relationship, friendship and alliance.",
      src=TW + "/debates/?id=1956-07-19a.1391.7#g1403.1", loc="Cyprus, HC Deb 19 Jul 1956, c1403",
      cav="Cyprus debate (sensitive thread): speaker's framing. Mirror label is the closest of the ten (the reconciling former enemy); not forced beyond that."),
 dict(id="noel-baker-1956-09", voice="Philip Noel-Baker", role="Labour MP, Nobel Peace laureate (1959)", dom="politics", date="1956-09-14", era="posthumous",
      mirror=None, pol="admiring", inten=1, art="speech", f="nb1956.txt", tag=N1,
      saw="Calls the Venizelos-Mustapha Kemal reconciliation 'historic' and urges Menderes and Karamanlis to repeat it over Cyprus.",
      q="Thirty years ago, after the far more grievous troubles of which I have spoken, Venizelos and Mustapha Kemal made a historic reconciliation.",
      src=TW + "/debates/?id=1956-09-14a.355.5#g355.7", loc="Cyprus, HC Deb 14 Sep 1956, c355",
      cav="Cyprus debate (sensitive thread): speaker's framing. Noel-Baker was an eyewitness of the 1922-23 Lausanne population-exchange talks, which he mentions in the same speech (Nansen)."),
 dict(id="noel-baker-1964-02", voice="Philip Noel-Baker", role="Labour MP, Nobel Peace laureate (1959)", dom="politics", date="1964-02-03", era="posthumous",
      mirror=None, pol="admiring", inten=1, art="speech", f="nb1964.txt", tag=N1,
      saw="Holds up Mustafa Kemal, who taught classes himself, as the model of the literacy campaigner followed by Mexico's Torres Bodet.",
      q="Like Mustafa Kemal, in Turkey, 30 years before him, he set an example by taking classes himself and, in a very short period of years, tens of millions of Mexicans had been taught to read and write.",
      src=TW + "/debates/?id=1964-02-03a.828.0#g875.1", loc="International Development Association Bill, HC Deb 3 Feb 1964, c875",
      cav="The quoted sentence's subject is Torres Bodet; Kemal is the comparison. Admiration is inferred from the comparison."),
 dict(id="wigg-1957-02", voice="George Wigg", role="Labour MP, Army spokesman (later Lord Wigg)", dom="politics", date="1957-02-05", era="posthumous",
      mirror=None, pol="instrumental", inten=2, art="speech", f="wigg1957.txt", tag=N1,
      saw="Notes Conservatives now respect Kemal Ataturk, though Britain tried to knock him off his perch in 1922 and only made him stronger.",
      q="Today, hon. Gentlemen speak in terms of great respect of Kemal Ataturk. There was a time when we tried to knock down Kemal Ataturk.",
      src=TW + "/debates/?id=1957-02-05a.251.4#g332.1", loc="Army Supplementary Estimate, 1956-57, HC Deb 5 Feb 1957, c332",
      cav="Used as a precedent against removing Nasser by force (Suez aftermath): Wigg's point is that the Middle East choice is 'authoritarian regimes based upon the army and chaos'. Wigg, who served in Constantinople in 1923, mentions Kemal in six contributions 1946-57 (24 May 1946, 16 Mar 1953, 29 Jul 1954 on the Turks' goodwill, 24 Jan 1956 'another Kemal or ... Enver Pasha' of Nasser, 8 Nov 1956); this is the fullest statement."),
 dict(id="straw-2003-11", voice="Jack Straw", role="British Foreign Secretary", dom="politics", date="2003-11-20", era="posthumous",
      mirror=None, pol="witness", inten=1, art="speech", f="straw2003.txt", tag=N2,
      saw="Describes 'the major change by Ataturk' as the start of Turkey's secular Governments, in answering on the Istanbul bombings.",
      q="Although Turkey has had secular Governments following the major change by Ataturk, until recently the significance of the most recent election was that by a large majority the Turkish people decided to choose an explicitly Islamic party",
      src=TW + "/debates/?id=2003-11-20.953.0#g960.1", loc="Terrorist Attacks (Istanbul), HC Deb 20 Nov 2003, c960",
      cav="Passing description with no stated judgement; witness. Recorded because Straw was on the target list. Quote is a clause of one sentence, which continues 'no different from Christian Democrat parties...'."),
 dict(id="macshane-2004-06", voice="Denis MacShane", role="Labour MP, Minister for Europe", dom="politics", date="2004-06-23", era="posthumous",
      mirror="modernization-poster-child", pol="instrumental", inten=1, art="speech", f="macshane2004b.txt", tag=N2,
      saw="Presents EU accession as Turkey's 'second great modernisation after that of Ataturk', treating Atatürk's as the first.",
      q="the Turkish nation will embark on its second great modernisation after that of Ataturk.",
      src=TW + "/debates/?id=2004-06-23.1422.0#g1425.0", loc="Turkey (EU Accession), HC Deb 23 Jun 2004, c1425",
      cav="Same phrase in Oral Answers, 15 Jun 2004 ('the second great modernisation of Turkey, after the Ataturk modernisation'). Used for the EU accession case."),
 dict(id="patten-2004-12", voice="John Patten (Lord Patten)", role="Former Education Secretary, Conservative peer", dom="politics", date="2004-12-15", era="posthumous",
      mirror="secular-rationalist-prophet", pol="admiring", inten=1, art="speech", f="patten2004.txt", tag=N2,
      saw="Treats 'the legacy of Kemal Atatürk' as a secular Turkey whose preservation is the reassurance all seek, inside or outside the EU.",
      q="There is also the reassurance that we all seek that the legacy of Kemal Atatürk—Turkey as a secular society—is going to be preserved inside or outside of the European Union and that there is no possibility of a theocratic state emerging in Turkey.",
      src=TW + "/lords/?id=2004-12-15a.1335.0#g1357.0", loc="Turkey and the EU, HL Deb 15 Dec 2004, cc1355-57",
      cav="Column given as the span of Patten's speech (his speech follows Lord Rea's, ends before Lord Dahrendorf's, per the page's citation lines). Also Patten's written question 23 Oct 2006 asks what representations were made over the trial of Ipek Calislar for 'allegedly insulting Kemal Atatürk': a procedural mention, not recorded."),
 dict(id="howell-2011-01", voice="David Howell (Lord Howell of Guildford)", role="Minister of State, Foreign Office, Conservative peer", dom="politics", date="2011-01-13", era="posthumous",
      mirror="modernization-poster-child", pol="admiring", inten=1, art="speech", f="howell2011.txt", tag=N2,
      saw="Calls Atatürk 'the architect of this modern Turkish state', admiring his respect for European institutions and his secular state on European lines.",
      q="No speech about Turkey would be complete without respectful reference to the architect of this modern Turkish state, Kemal Ataturk, his admiration and respect for European institutions, his vision of Turkey in Europe and his creation of a secular Turkish state modelled on European lines.",
      src=TW + "/lords/?id=2011-01-13a.1537.4#g1571.0", loc="Turkey — Debate, HL Deb 13 Jan 2011, col. 1571 (contribution anchor)",
      cav="Government minister's opening speech in a Lords debate on Turkey. Column from the contribution anchor on TheyWorkForYou."),
 dict(id="weidenfeld-2014-10", voice="George Weidenfeld (Lord Weidenfeld)", role="Publisher and writer, crossbench peer", dom="politics", date="2014-10-30", era="posthumous",
      mirror="secular-rationalist-prophet", pol="admiring", inten=1, art="speech", f="weid2014.txt", tag=N2,
      saw="Describes Erdogan as an 'authoritarian Islamist who all but dismantled the western and secular republic of Kemal Ataturk'; the republic is the standard.",
      q="the Prime Minister of Turkey, Erdogan, an authoritarian Islamist who all but dismantled the western and secular republic of Kemal Ataturk, at first denied his NATO allies air landing rights",
      src=TW + "/lords/?id=2014-10-30a.1317.2#g1364.0", loc="Middle East and North Africa — Motion to Take Note, HL Deb 30 Oct 2014, c1364",
      cav="Sensitive thread (Kurds, Kobane): speaker's framing; the quote is a clause of one sentence. Admiration inferred from 'western and secular republic' set against Erdogan."),
 dict(id="glasman-2018-04", voice="Maurice Glasman (Lord Glasman)", role="Political theorist, Labour peer", dom="politics", date="2018-04-19", era="posthumous",
      mirror=None, pol="witness", inten=1, art="speech", f="glasman2018.txt", tag=N2,
      saw="Describes Turkey's current state as 'a very curious combination of Ataturk and the Muslim Brotherhood', an Islamist nationalism, and not a reliable ally.",
      q="under this very curious combination of Ataturk and the Muslim Brotherhood—a certain Islamist nationalism—but it has invaded its friend Syria.",
      src=TW + "/lords/?id=2018-04-19b.1255.3#g1306.0", loc="National Security Situation — Motion to Take Note, HL Deb 19 Apr 2018, c1306",
      cav="Description of Erdogan's Turkey; no judgement of Atatürk as such, so witness. Sensitive thread (Afrin/Kurds): speaker's framing."),
 dict(id="corbyn-1988-03", voice="Jeremy Corbyn", role="Labour MP (later Leader of the Opposition)", dom="politics", date="1988-03-25", era="posthumous",
      mirror=None, pol="hostile", inten=1, art="speech", f="corbyn1988.txt", tag=N2,
      saw="Says the Sèvres promise of Kurdish recognition was never carried out because 'the rise of Kemal Ataturk' ensured it never came to fruition.",
      q="It was not until 1920 and the treaty of Sevres that the Kurdish nation was recognised, but the treaty was never fully carried out or established because of the rise of Kemal Ataturk in Turkey, who ensured that it was never brought to fruition.",
      src=TW + "/debates/?id=1988-03-25a.632.0#g653.0", loc="Adjournment (Easter and Monday 2nd May), HC Deb 25 Mar 1988, c653",
      cav="Sensitive thread (Kurds): Corbyn's framing, in an adjournment speech on the Halabja-era Kurdish plight; the vault does not adopt it. Hostility is mild and implicit (Kemal as the obstacle to Kurdish independence). He repeats it on 6 Jun 1991 (Kurdish People debate, c487: 'Mustafa Kemal led the development of the modern state of Turkey, and the British Government decided to back modern Turkey rather than the aspirations of the Kurdish people'), recorded here once."),
]
R = [r for r in R if r['id'] not in {'weidenfeld-2014-10', 'straw-2003-11', 'glasman-2018-04', 'howell-2011-01', 'churchill-1944-08', 'noel-baker-1964-02'}]  # dropped at the independent check (no stated view / misattributed)

bad = [r["id"] for r in R if norm(r["q"]) not in bank(r["f"])]
if bad:
    sys.exit("quote not found in source bank: %s" % bad)
for r in R:
    assert len(r["saw"].split()) <= 25, (r["id"], len(r["saw"].split()))
    assert len(re.findall(r"[.!?](?:\s|$)", r["q"])) <= 3, r["id"]  # "hon." abbreviations inflate the count

with open(os.path.join(STATE, "gazes_twfy.jsonl"), "w", encoding="utf-8") as f:
    for r in R:
        rec = {"id": r["id"], "voice": r["voice"], "voice_type": "person", "role": r["role"],
               "country": "United Kingdom", "country_now": "United Kingdom", "domain": r["dom"], "date": r["date"], "era": r["era"],
               "mirror": r["mirror"], "polarity": r["pol"], "intensity": r["inten"], "what_they_saw": r["saw"],
               "quote": r["q"], "artifact": r["art"], "evidence": "P",
               "mediated_by": None, "caveat": r["loc"] + ". Transcription at TheyWorkForYou of the official Hansard. " + r["cav"],
               "node": r["tag"], "sources": [r["src"]]}
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")

with open(os.path.join(STATE, "ledger_twfy.md"), "w", encoding="utf-8") as f:
    f.write("| Claim | Node | Status | Sources | Next step |\n|---|---|---|---|---|\n")
    for r in R:
        f.write("| %s, %s: %s | %s | verified P (TWFY page read, quote matched) | %s | Compare with hansard.parliament.uk column if exact column needed |\n"
                % (r["voice"], r["loc"], r["pol"], r["tag"], r["src"]))

def link(n):
    return "[[%s]]" % n

PEOPLE = {
 "Anthony Eden": ("British Foreign Secretary and Prime Minister", "1897–1977", "admiring (1941, 1942)", ["eden-1941-08", "eden-1942-01"],
   "As Foreign Secretary he told the Commons on 6 August 1941 that the post-war world would have a noble part for 'the Turkey re-created by the genius of Ataturk', and on 8 January 1942 called Atatürk 'the great leader of modern Turkey'."),
 "Philip Noel-Baker": ("British Labour MP, disarmament campaigner, Nobel Peace Prize 1959", "1889–1982", "admiring (1956, 1964)", ["noel-baker-1956-09"],
   "Called the Venizelos-Mustapha Kemal reconciliation 'historic' in the Cyprus debate of 14 September 1956."),
 "Selwyn Lloyd": ("British Foreign Secretary 1955–60, later Speaker of the Commons", "1904–1978", "admiring (1956)", ["selwyn-lloyd-1956-07"],
   "In the Cyprus debate of 19 July 1956 he named 'the work of Kemal Ataturk and Venizelos' in building a Greek-Turkish friendship."),
 "George Wigg": ("Labour MP and Army spokesman, later Lord Wigg", "1900–1983", "instrumental (1957)", ["wigg-1957-02"],
   "A soldier in Constantinople in 1923, he returns to Kemal across 1946–57; on 5 February 1957 he reminds the Commons that Britain tried to knock Kemal Ataturk down in 1922 'and they failed'."),
 "Clement Davies": ("Leader of the Liberal Party 1945–56", "1884–1962", "admiring (1955)", ["clement-davies-1955-12"],
   "In the Cyprus debate of 5 December 1955 he spoke of 'that amazing man, Ataturk' and the great Turkish tradition."),
 "Christopher Hollis": ("Conservative MP and writer", "1902–1977", "admiring (1953)", ["hollis-1953-10"],
   "In the Trieste debate of 28 October 1953 he credited 'the statesman Kemal Ataturk' with ending the Greek-Turkish enmity."),
 "Denis MacShane": ("Labour MP and Minister for Europe 2002–05", "1948–", "instrumental (2004)", ["macshane-2004-06"],
   "Argued in June 2004 that EU accession would be Turkey's 'second great modernisation after that of Ataturk'."),
 "John Patten": ("Conservative Education Secretary 1992–94, Lord Patten", "1945–", "instrumental (2004)", ["patten-2004-12"],
   "In the Lords on 15 December 2004 he spoke of the legacy of Kemal Atatürk, 'Turkey as a secular society', as the thing all seek to preserve."),
 "Jeremy Corbyn": ("Labour MP, Leader of the Opposition 2015–20", "1949–", "hostile (1988)", ["corbyn-1988-03"],
   "In March 1988 he blamed 'the rise of Kemal Ataturk' for the non-implementation of the Sèvres provisions on the Kurds; he repeated the point in June 1991."),
}
byid = {r["id"]: r for r in R}
for name, (role, life, stance, ids, text) in PEOPLE.items():
    nodes = sorted({byid[i]["tag"] for i in ids})
    body = text + " See " + " and ".join(link(n) for n in nodes) + ".\n\n## Sources\n" + "\n".join("- %s (%s)" % (byid[i]["src"], byid[i]["loc"]) for i in ids)
    person(name, role=role, nat="British", life=life, stance=stance, tags=["politics", "uk", "verified", "hansard"], body=body)

def event(tag, when, intro, ids):
    body = intro + "\n\n"
    for i in ids:
        r = byid[i]
        body += "## %s (%s)\n\n> %s\n\n%s %s\n\n" % (r["voice"], r["date"], r["q"], r["loc"] + ".", r["cav"])
    body += "## Sources\n" + "\n".join("- %s" % byid[i]["src"] for i in ids) + "\n"
    note("Events", tag, {"type": "event", "when": when, "tags": ["event", "verified", "uk", "hansard", "politics"]}, body)

ids1 = [r["id"] for r in R if r["tag"] == N1]
ids2 = [r["id"] for r in R if r["tag"] == N2]
event(N1, "1941–1964",
 "Found through TheyWorkForYou's search of the historic Commons record (a transcription of Hansard). In wartime, Eden uses Atatürk's 'genius' to court Turkey (Churchill's 2 Aug 1944 line on Kemal's Russian policy states no view and is not counted); in the Cyprus years (1955-56) Davies, Selwyn Lloyd and Noel-Baker cite the Atatürk-Venizelos reconciliation as a model, and in 1957 Wigg uses Britain's failure to topple Kemal in 1922 as a lesson. Existing person note: [[Winston Churchill]] (earlier Commons records are in [[Parliament Meets Kemal, February–March 1920]]).", ids1)
event(N2, "1988–2018",
 "The same search for the later decades. Atatürk is now a standard for a secular Turkey: Patten and MacShane invoke him in the EU-accession years; Corbyn blames his rise for the failure of the Sèvres promise to the Kurds (sensitive thread, speaker's framing). Earlier records: [[Hansard After Atatürk, 1938–1939]].", ids2)
print(len(R), "records ok")
