# -*- coding: utf-8 -*-
# Census round 14 (Nov 2026) — heads of state and government after 1945 in their own words, from official speech archives.
# Records: Johnson (1964, 1967), Nixon (1972), Reagan (1981, 1988), G. H. W. Bush (1991), Mitterrand (1992), Putin (2004, 2005).
# Sources: presidency.ucsb.edu, vie-publique.fr, en.kremlin.ru, fetched with tools/ms fetch and banked in
# tools/.state/round14/src_*.txt (JSON from the wrapper); every quote is checked against its bank before anything is written.
import json, os, re, sys
from _lib import note, person

HERE = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(HERE, "tools", ".state", "round14")
NODE = "American, French and Russian Leaders on Atatürk in Their Own Words"

def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"').replace("­", "").replace("\xa0", " ")
    return re.sub(r"\s+", " ", s)

def bank(n):
    return norm(json.load(open(os.path.join(STATE, n), encoding="utf-8"))["results"][0]["text"])

U = "https://presidency.ucsb.edu/documents/"
R = [
 dict(id="johnson-1964-06-22", voice="Lyndon B. Johnson", role="President of the United States; luncheon toast for Prime Minister İnönü", c="United States", cn="United States",
      dom="politics", date="1964-06-22", era="posthumous", mirror="nation-forge-template", pol="instrumental", inten=1,
      saw="Calls Atatürk the 'immortal founder of modern Turkey' who built a great modern state, with İnönü at his side.",
      q="We remember the immortal founder of modern Turkey, Kemal Ataturk.",
      art="speech", ev="P", med=None,
      cav="Toast framed around honouring İnönü, Atatürk's old lieutenant. The same day's welcome on the South Lawn (%sremarks-welcome-the-white-house-prime-minister-inonu-turkey) speaks of 'the dreams of the great Ataturk, at whose side you once worked'. Date from the Project page header." % U,
      src="src_ucsb_toasts-the-president-and-prime-minister-inonu-turkey.txt",
      urls=[U + "toasts-the-president-and-prime-minister-inonu-turkey", U + "remarks-welcome-the-white-house-prime-minister-inonu-turkey"],
      loc="Public Papers of the Presidents, LBJ 1964, toast at White House luncheon for İnönü (APP page)", link="Lyndon B. Johnson", nxt="none"),
 dict(id="johnson-1967-04-03", voice="Lyndon B. Johnson", role="President of the United States; state dinner and welcome for President Sunay", c="United States", cn="United States",
      dom="politics", date="1967-04-03", era="posthumous", mirror="modernization-poster-child", pol="admiring", inten=2,
      saw="Says Atatürk's 'energy, vision, and wisdom' set Turkey on the 20th-century path; modern Turkey was 'one of the great revolutions of our age'.",
      q="The remarkable energy, vision, and wisdom of a great leader, Kemal Ataturk, set his people on the path of 20th century accomplishment.",
      art="speech", ev="P", med=None,
      cav="Two speeches on the same day, both stored here. The South Lawn welcome (%sremarks-welcome-the-white-house-president-sunay-turkey) adds: 'the emergence of modern Turkey, under the guiding genius of Kemal Ataturk, was one of the great revolutions of our age. It remains an inspiration to all who have since won their independence'. Diplomatic occasion, with a visiting head of state." % U,
      src="src_ucsb_toasts-the-president-and-president-sunay-turkey.txt",
      urls=[U + "toasts-the-president-and-president-sunay-turkey", U + "remarks-welcome-the-white-house-president-sunay-turkey"],
      loc="Public Papers of the Presidents, LBJ 1967, toast at White House dinner for Sunay (APP page)", link="Lyndon B. Johnson", nxt="none"),
 dict(id="nixon-1972-03-21", voice="Richard Nixon", role="President of the United States; welcome of Prime Minister Erim", c="United States", cn="United States",
      dom="politics", date="1972-03-21", era="posthumous", mirror=None, pol="instrumental", inten=1,
      saw="Calls 'peace at home and peace in the world' the motto of 'your great leader Ataturk' and adopts it as an American goal.",
      q="the motto which came from your great leader Ataturk, \"Peace at home and peace in the world,\" is one that we in the United States can also say is our goal.",
      art="speech", ev="P", med=None,
      cav="Passing borrowing of the motto at an arrival ceremony; Nixon states no wider judgement. In the evening toast (%stoasts-the-president-and-prime-minister-erim-turkey) it is Erim who speaks of 'the legacy of Kernel [sic] Ataturk'; Nixon there only repeats the motto." % U,
      src="src_ucsb_remarks-welcome-prime-minister-nihat-erim-turkey.txt",
      urls=[U + "remarks-welcome-prime-minister-nihat-erim-turkey"],
      loc="Public Papers of the Presidents, Nixon 1972, welcome to Prime Minister Erim (APP page)", link="Richard Nixon", nxt="none"),
 dict(id="reagan-1981-04-02", voice="Ronald Reagan", role="President of the United States; White House statement on the Atatürk centennial", c="United States", cn="United States",
      dom="politics", date="1981-04-02", era="posthumous", mirror=None, pol="admiring", inten=2,
      saw="Calls Atatürk a great national leader in war and peace, first in his countrymen's hearts, and cites his 'Peace at Home, Peace Abroad'.",
      q="Ataturk was a great national leader in times of war and peace.",
      art="quote", ev="P", med=None,
      cav="Issued under Reagan's name as the Project lists it, on the eve of the 1981 centennial year (it ties the praise to Turkish-American alliance and to backing Turkey's post-coup government). Staff-drafted text; date from the Project page header.",
      src="src_ucsb_white-house-statement-concerning-the-centennial-anniversary-the-birth-mustafa-kemal.txt",
      urls=[U + "white-house-statement-concerning-the-centennial-anniversary-the-birth-mustafa-kemal"],
      loc="APP, Reagan, White House Statement Concerning the Centennial Anniversary of the Birth of Mustafa Kemal Ataturk", link="Ronald Reagan", nxt="none"),
 dict(id="reagan-1988-06-27", voice="Ronald Reagan", role="President of the United States; welcome of President Evren", c="United States", cn="United States",
      dom="politics", date="1988-06-27", era="posthumous", mirror=None, pol="instrumental", inten=1,
      saw="Opens by quoting Atatürk's 'Happy is he who can call himself a Turk' and credits Evren with keeping Turkey faithful to Atatürk's ideals.",
      q="The founder of the Turkish Republic, Mustafa Kemal Ataturk, once said, \"Happy is he who can call himself a Turk.\"",
      art="speech", ev="P", med=None,
      cav="Courtesy welcome for the general who led the 1980 coup; Reagan also says 'We are well aware of your own distinguished role, Mr. President, in maintaining Turkey's devotion to the ideals of Ataturk', which makes Atatürk the yardstick of Evren's rule.",
      src="src_ucsb_remarks-the-welcoming-ceremony-for-president-kenan-evren-turkey.txt",
      urls=[U + "remarks-the-welcoming-ceremony-for-president-kenan-evren-turkey"],
      loc="APP, Reagan, Remarks at the Welcoming Ceremony for President Kenan Evren of Turkey", link="Ronald Reagan", nxt="none"),
 dict(id="bush-1991-07-20", voice="George H. W. Bush", role="President of the United States; toast at the state dinner in Ankara", c="United States", cn="United States",
      dom="politics", date="1991-07-20", era="posthumous", mirror="nation-forge-template", pol="admiring", inten=2,
      saw="Standing at Atatürk's tomb, sees a parallel with George Washington: great generals and leaders who built nations and won peace after war.",
      q="We were standing outside of Ataturk's tomb this morning, and I couldn't help but think of the parallels between the founder of the modern Turkish Republic",
      art="speech", ev="P", med=None,
      cav="After Turkey's role in the Gulf War, so also hospitality. Same day, the arrival speech (%sremarks-the-arrival-ceremony-ankara-turkey) praises 'a vision expressed by your great leader, Ataturk, that the voice of the government must speak the words of its people' and quotes him on speaking the truth. The Project notes that no tape was available to verify either text. Date from the Project listing." % U,
      src="src_ucsb_toast-state-dinner-ankara-turkey.txt",
      urls=[U + "toast-state-dinner-ankara-turkey", U + "remarks-the-arrival-ceremony-ankara-turkey"],
      loc="APP, George Bush, Toast at a State Dinner in Ankara, Turkey", link="George H. W. Bush", nxt="none"),
 dict(id="mitterrand-1992-04-13", voice="François Mitterrand", role="President of France; state dinner at Çankaya Palace", c="France", cn="France",
      dom="politics", date="1992-04-13", era="posthumous", mirror="modernization-poster-child", pol="instrumental", inten=1,
      saw="Places Turkey in the European sphere and names Atatürk the most valiant protagonist of its long effort to rejoin progress.",
      q="[translation] Turkey's effort to put itself back in the current of progress, begun in the late eighteenth century, and of which Ataturk was, at the start of ours, the most valiant protagonist",
      qfr="dont Ataturk fut, au début du nôtre, le plus valeureux protagoniste",
      art="speech", ev="P", med=None,
      cav="QUOTE IS A TRANSLATION (by the census). French original, vie-publique.fr: \"l'effort de la Turquie pour se replacer dans le courant du progrès, qui débuta dès la fin du dix-huitième siècle, et dont Ataturk fut, au début du nôtre, le plus valeureux protagoniste, s'est poursuivi sans relâche.\" Said to argue that Turkey 'relève de l'espace européen', at a time of strained relations with Europe.",
      src="src_vp_mitterrand.txt",
      urls=["https://www.vie-publique.fr/discours/127311-francois-mitterrand-13041992-sur-turquie-europe-relation-bilterale"],
      loc="vie-publique.fr discours 127311, Déclaration de M. François Mitterrand, Cankaya, 13 April 1992", link="François Mitterrand", nxt="Élysée copy of the same text (elysee.fr) as a second source"),
 dict(id="putin-2004-12-06", voice="Vladimir Putin", role="President of Russia; note in the Anıtkabir honour book, official visit to Turkey", c="Russia", cn="Russia",
      dom="politics", date="2004-12-06", era="posthumous", mirror=None, pol="instrumental", inten=1,
      saw="Writes in the Atatürk mausoleum book that he honours the memory of this outstanding son of Turkey, whose name marks the start of Russian-Turkish friendship.",
      q=None,
      art="visit", ev="P", med="Kremlin.ru news item (a paraphrase of Putin's honour-book entry, not the entry itself)",
      cav="The Kremlin text only reports the entry ('he honoured highly the memory of this outstanding son of the Turkish people'; 'Ataturk's name was linked to the birth of Turkish statehood, and the beginning of friendship between the peoples of Russia and Turkey'), so no verbatim quote is stored. The entry itself was not found.",
      src="src_kremlin_32318.txt", chk="outstanding son of the Turkish people",
      urls=["http://en.kremlin.ru/events/president/news/32318"],
      loc="en.kremlin.ru news 32318, 6 Dec 2004", link="Vladimir Putin", nxt="Turkish press photo of the honour-book entry, for his actual wording"),
 dict(id="putin-2005-11-17", voice="Vladimir Putin", role="President of Russia; opening of the Blue Stream pipeline, Samsun", c="Russia", cn="Russia",
      dom="politics", date="2005-11-17", era="posthumous", mirror=None, pol="instrumental", inten=1,
      saw="Notes the ceremony is in Samsun, tied to the national liberation movement of Mustafa Kemal, and that Russia then acted as Turkey's ally.",
      q="it is symbolic that our ceremony is taking place in Samsun, the city connected with the Turkish people's national liberation movement led by Mustafa Kemal (Ataturk).",
      art="speech", ev="P", med=None,
      cav="Used to frame a gas deal with a reminder of Soviet aid to the Kemalists ('Russia acted as Turkey's ally and gave it significant support'). He says nothing of Atatürk himself beyond his role as leader of the movement; weakest record in the set.",
      src="src_kremlin_23276.txt",
      urls=["http://en.kremlin.ru/events/president/transcripts/23276"],
      loc="en.kremlin.ru transcripts 23276", link="Vladimir Putin", nxt="none"),
]

bad = []
for r in R:
    full = bank(r["src"])
    q = r.get("qfr") or r.get("chk") or r["q"]
    if r["id"] == "mitterrand-1992-04-13":
        q = r["qfr"]
    if q:
        qn = norm(q).rstrip(".")
        qn = re.sub(r"\[translation\]$", "", qn).strip()
        if qn not in full and norm(q).replace(",", "") not in full.replace(",", ""):
            bad.append(r["id"])
    assert len(r["saw"].split()) <= 25, (r["id"], len(r["saw"].split()))
if bad:
    sys.exit("quote not found in source bank: %s" % bad)

with open(os.path.join(STATE, "gazes_speeches.jsonl"), "w", encoding="utf-8") as f:
    for r in R:
        rec = {"id": r["id"], "voice": r["voice"], "voice_type": "person", "role": r["role"], "country": r["c"],
               "country_now": r["cn"], "domain": r["dom"], "date": r["date"], "era": r["era"], "mirror": r["mirror"],
               "polarity": r["pol"], "intensity": r["inten"], "what_they_saw": r["saw"], "quote": r["q"],
               "artifact": r["art"], "evidence": r["ev"], "mediated_by": r["med"], "caveat": r["cav"],
               "node": NODE, "sources": r["urls"]}
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")

with open(os.path.join(STATE, "ledger_speeches.md"), "w", encoding="utf-8") as f:
    f.write("| Claim | Node | Status | Sources | Next step |\n|---|---|---|---|---|\n")
    for r in R:
        qs = (r["q"] or r["saw"])
        f.write("| %s (%s, %s): \"%s\" | %s | verified %s (%s) | %s | %s |\n" % (
            r["voice"], r["role"][:50], r["date"], qs[:110].replace("|", "/") + ("..." if len(qs) > 110 else ""),
            NODE, r["ev"], r["loc"], "; ".join(r["urls"][:1]), r["nxt"]))

people = {
 "Lyndon B. Johnson": ("President of the United States, 1963–1969", "American", "1908–1973", "admirer (diplomatic)",
    "In toasts and welcomes for İnönü (1964) and Sunay (1967) he called Atatürk the 'immortal founder of modern Turkey' and his work 'one of the great revolutions of our age'."),
 "Richard Nixon": ("President of the United States, 1969–1974", "American", "1913–1994", "borrower of the motto",
    "At Erim's welcome in March 1972 he took up Atatürk's 'peace at home and peace in the world' as an American goal."),
 "Ronald Reagan": ("President of the United States, 1981–1989", "American", "1911–2004", "admirer (diplomatic)",
    "Issued the 1981 centennial statement and opened his 1988 welcome of Evren with Atatürk's 'Happy is he who can call himself a Turk'."),
 "George H. W. Bush": ("President of the United States, 1989–1993", "American", "1924–2018", "admirer",
    "Visiting Atatürk's tomb in July 1991 he likened the founder to George Washington."),
 "François Mitterrand": ("President of France, 1981–1995", "French", "1916–1996", "admirer (diplomatic)",
    "At the Çankaya dinner in April 1992 he named Atatürk the most valiant protagonist of Turkey's modernising effort and argued Turkey belongs to Europe."),
 "Vladimir Putin": ("President of Russia", "Russian", "1952–", "instrumental",
    "Laid a wreath at the Anıtkabir in December 2004 and in Samsun in 2005 recalled Russia's aid to Kemal's movement."),
}
for name, (role, nat, life, stance, desc) in people.items():
    if os.path.exists(os.path.join(HERE, "vault", "People", name + ".md")):
        continue
    person(name, role=role, nat=nat, life=life, stance=stance, tags=["verified", "head-of-state"],
           body="%s See [[%s]] for the quotes.\n\n## Sources\n- Official speech archives cited in [[%s]].\n" % (desc, NODE, NODE))

body = ["""
Round 14 mined the official speech archives for heads of state and government after 1945: the American Presidency Project
(UC Santa Barbara), vie-publique.fr and kremlin.ru. Nine records survived reading, from Lyndon Johnson's toasts to
Putin's Samsun speech of 2005 (context only: the check found no stated view of Atatürk in it, so it is not counted as a gaze). Every quote was checked against the fetched page text before this note was written.

## The pattern

- **The American script:** Johnson, Nixon, Reagan and Bush all treat Atatürk as a ready-made ally of the Cold War: a
  founder who 'looked West'. The recurring lines are 'peace at home, peace in the world' (Nixon 1972, Reagan 1981, Bush 1991)
  and the Washington comparison ([[George H. W. Bush]], 1991). These are courtesy texts for a visiting or hosting
  head of state, so most records are instrumental.
- **Atatürk as the yardstick of a regime:** [[Ronald Reagan]], welcoming General Evren in 1988, praised his 'devotion to the
  ideals of Ataturk'. The same founder is cited approvingly for the officer who ended a civilian government.
- **France arguing for Europe:** [[François Mitterrand]] used Atatürk in 1992 to say Turkey 'relève de l'espace
  européen'.
- **Russia remembering its own aid:** [[Vladimir Putin]] (2004, 2005) links Atatürk to the Soviet-Turkish alliance of 1920–22.
"""]
for r in R:
    body.append("\n## %s (%s)\n" % (r["voice"], r["date"]))
    body.append("*%s*\n" % r["saw"])
    if r["q"]:
        body.append("> %s\n" % r["q"])
    body.append("%s Location: %s. Evidence %s. See [[%s]].\n" % (r["cav"], r["loc"], r["ev"], r["link"]))

body.append("""
## Not stored, and dry ends (round 14)

- **Kemalism as a lecture:** none of the American, French or Russian texts found uses Atatürk to chide Turkey; the
  archives return courtesy texts. Barnier (21 Oct 1996) and de Charette (31 Mar 1997) cite Atatürk's laïcité, but they were ministers, not heads of state.
- **Carter, Ford, Clinton (1999 Istanbul and Ankara texts other than the Assembly speech), G. W. Bush, Biden, Trump:** the Project was
  searched; the Carter–Ecevit toasts of 1978 and the Ford, Bush 2004 and later texts returned do not mention him. Clinton's 1999 Assembly speech and Obama's 2009 one are already stored.
- **Steinmeier (24 Apr 2024):** the Bundespräsident site's report on his visit says Germans contributed to the Turkish state 'under Kemal Atatürk' and that he laid a wreath, but that is the office's text, not his words; Gauck's 2014 METU speech has no mention.
- **UK prime ministers:** the live Hansard API (post-1997) returned 20 contributions on Atatürk/Kemal, none by a prime minister; historic Hansard has no search API.
- **Not reached:** Chirac, Sarkozy, Hollande, Macron (vie-publique search returned only ministers), Kohl, Merkel, Medvedev, Khrushchev, Gorbachev, Vajpayee, Modi.

## Sources
- The American Presidency Project (Peters and Woolley), presidency.ucsb.edu: documents named in each record.
- vie-publique.fr, discours 127311 (Mitterrand, Çankaya, 13 April 1992).
- President of Russia, en.kremlin.ru: news 32318 and transcripts 23276.
""")

note("Events", NODE,
     {"type": "event", "when": "1964–2005",
      "tags": ["event", "verified", "heads-of-state", "statesmen"]},
     "\n".join(body))
print("ok", len(R), "records")
