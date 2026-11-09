# -*- coding: utf-8 -*-
# Census round 14 (Nov 2026) — memoirs, speeches and essays of leaders and thinkers of the Islamic world, Asia and Africa.
# Records: Mohammad Reza Pahlavi (Mission for My Country 1961; Answer to History 1980), Muhammad Asad (The Road to Mecca 1954),
# Mahathir Mohamad (speech 10 Jul 2003; op-ed Nov 2005), Fazlur Rahman (Islam and Modernity 1982).
# Each quote is checked against the text banked in tools/.state/round14/memoirs/src_*.txt.
import json, os, re, sys
from _lib import note

HERE = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(HERE, "tools", ".state", "round14")
BANK = os.path.join(STATE, "memoirs")
NODE = "Leaders and Thinkers of the Muslim World and Asia on Atatürk in Their Own Words"

def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"').replace("­", "")
    s = re.sub(r"-\s*\n", "", s)
    return re.sub(r"\s+", " ", s)

def bank(n):
    return norm(open(os.path.join(BANK, n), encoding="utf-8").read())

R = [
 dict(id="mohammad-reza-pahlavi-1961", voice="Mohammad Reza Pahlavi", role="Shah of Iran; memoir Mission for My Country (1961)", c="Iran", cn="Iran",
      dom="politics", date="1961", era="posthumous", mirror=None, pol="admiring", inten=1,
      saw="Describes the Turkish republic as founded under Atatürk's 'dynamic leadership' after the abolition of an 'archaic caliphate', and compares Turkey's head start over Iran.",
      q="the Turks had abolished their archaic caliphate; and soon afterwards they established a republic under the dynamic leadership of Kemal Ataturk.",
      art="memoir", ev="P", med=None,
      cav="Brief and in passing, so intensity 1. Page 39 is taken from the book's own index ('Ataturk, Kemal, 39'); the archive.org OCR text has no page markers. The next paragraph compares Iran in the 1920s with 'neighbouring Turkey, which my father visited in 1934 to observe the remarkable progress made' (about p. 39-40). The Shah is writing as monarch about his father's republic-or-monarchy choice; the sentence is context for that choice.",
      src="src_mission_for_my_country.txt",
      urls=["https://archive.org/details/mission-for-my-country-mohammad-reza-pahlavi_202605"],
      loc="Mohammad Reza Pahlavi, Mission for My Country (1961), p. 39 (index page)", link="Reza Shah Pahlavi"),
 dict(id="mohammad-reza-pahlavi-1980", voice="Mohammad Reza Pahlavi", role="Shah of Iran (in exile); Answer to History (1980)", c="Iran", cn="Iran",
      dom="politics", date="1980", era="posthumous", mirror=None, pol="witness", inten=1,
      saw="Says his father was greatly influenced by Atatürk's reforms and for a time hoped to emulate his neighbour, and that Atatürk admired his father's efforts.",
      q="Reza Khan had been greatly influenced by the reforms Kemal Ataturk had introduced in Turkey and for a time he hoped to emulate his neighbor's achievements",
      art="memoir", ev="P", med=None,
      cav="The object is Reza Shah's modelling on Atatürk; the Shah states no personal verdict, only calls Atatürk 'the man he had sought to emulate' and recounts the 1934 State visit when the honor guard's standard bearer knelt before Reza Shah (p. 52). Polarity 'admiring' is therefore weak; it could be read as witness. The sentence goes on to say the republic plan failed because 'Persia, unlike Turkey, was an empire'. Page 51 per the book's index; the passage runs onto p. 52 (OCR page header '52 ANSWER TO HISTORY').",
      src="src_answer_to_history.txt",
      urls=["https://archive.org/details/Pahlavi-Answer-To-History"],
      loc="Mohammad Reza Pahlavi, Answer to History (1980), pp. 51-52", link="Reza Shah Pahlavi"),
 dict(id="muhammad-asad-1954", voice="Muhammad Asad (Leopold Weiss)", role="Austrian-born Muslim scholar and writer; memoir The Road to Mecca (1954)", c="Pakistan/Saudi Arabia (memoir 1954)", cn="Pakistan",
      dom="religion", date="1954", era="posthumous", mirror="apostate", pol="hostile", inten=2,
      saw="Says the Turkish struggle first stood 'in the sign of Islam', then that Atatürk forsook religion and rejected Islamic values in his reforms.",
      q="Instead of basing his social revolution on a revived and reinvigorated Islam, Ataturk forsook the spiritual force of religion (which alone had brought him to victory) and made, quite unnecessarily, a rejection of all Islamic values the basis of his reforms.",
      art="memoir", ev="P", med=None,
      cav="Passage is in the Sanusi chapter ('Jihad'), p. 319 (text between the page headers 'JIHAD 319' and '320'), and describes Sayyid Ahmad al-Sanusi's disappointment; the judgement of Atatürk is the narrator's own. Read from the Islamic Book Service (New Delhi, 2004) reprint titled The Road to Makkah as scanned on archive.org; page numbers are that reprint's printed headers. Asad writes in 1954 about events of the 1920s-30s. Further passages: p. 297 (a dialogue set in Iran in the 1930s, Asad asks 'How is it that Ataturk, that petty masquerader who denies all value to Islam, has become to you Muslims a symbol of Muslim revival?'), p. 268 (Reza Khan's 'obvious admiration of Kemal Ataturk' and Iranians' 'fear of losing their religion as the Turks had lost theirs'), p. 272 (Reza Shah seeking 'to emulate Kemal Ataturk in building a vainglorious Western facade'). Same voice and date, so merged into one record; polarity 'conflicted' because he credits the Islamic character of the war of independence. Asad's Islam at the Crossroads (1934) and The Principles of State and Government in Islam were grepped and do not name Atatürk.",
      src="src_road_to_mecca.txt",
      urls=["https://archive.org/details/road-to-mecca_202409"],
      loc="Muhammad Asad, The Road to Mecca (1954), p. 319 (also pp. 268, 272, 297)", link="Abolition of the Caliphate"),
 dict(id="mahathir-2003-07-10", voice="Mahathir Mohamad", role="Prime Minister of Malaysia; speech to the World Ulama Conference, Putrajaya", c="Malaysia", cn="Malaysia",
      dom="politics", date="2003-07-10", era="posthumous", mirror=None, pol="admiring", inten=1,
      saw="Credits Atatürk with saving Turkey from partition by Greece by leading a strong Muslim force, noting that he himself claimed to be a secularist.",
      q="Turkey itself would have become a part of Greece had it not been for Kemal Ataturk who even though he himself claimed to be a secularist, nevertheless lead a strong Muslim Turkish force to expel the Greeks from Anatolia.",
      art="speech", ev="P", med=None,
      cav="Paragraph 27 of the speech 'Islam in Era of Globalisation' (opening of the World Ulama Conference, Marriott Hotel, Putrajaya, 10 Jul 2003), official text on mahathir.com; the speech has numbered paragraphs, no pages. 'lead' is the source's spelling. The remark serves the speech's argument that Muslims need modern knowledge to defend themselves, and calls Atatürk's force 'Muslim'. 2019 wreath-laying at Anıtkabir (see Anıtkabir) carries no sentence by him.",
      src="src_mahathir_2003.txt",
      urls=["https://mahathir.com/malaysia/speeches/2003/2003-07-10.php"],
      loc="Mahathir, 'Islam in Era of Globalisation', 10 Jul 2003, para. 27", link=None),
 dict(id="mahathir-2005-11", voice="Mahathir Mohamad", role="Former Prime Minister of Malaysia; op-ed 'Islam's forsaken renaissance'", c="Malaysia", cn="Malaysia",
      dom="politics", date="2005-11", era="posthumous", mirror="modernization-poster-child", pol="admiring", inten=2,
      saw="Defends Atatürk against Muslim critics: asks whether Turkey would be Muslim without him and says his clear-sightedness saved Islam in Turkey.",
      q="Mustafa Kamal's clear-sightedness saved Islam in Turkey and saved Turkey for Islam.",
      art="article", ev="S", med="Project Syndicate op-ed as printed in the Taipei Times, 10 Nov 2005; Project Syndicate original not opened",
      cav="Written after he left office (1981-2003). The surrounding sentences: 'Many Muslims still condemn the founder of modern Turkey, Mustafa Kamal, because he tried to modernize his country. But would Turkey be Muslim today without Ataturk?' The spelling 'Kamal' is his.",
      src="src_mahathir_2005.txt",
      urls=["http://taipeitimes.com/News/editorials/archives/2005/11/10/2003279592"],
      loc="Mahathir, 'Islam's forsaken renaissance', Taipei Times, 10 Nov 2005 (Project Syndicate)", link=None),
 dict(id="fazlur-rahman-1982", voice="Fazlur Rahman", role="Pakistani-born Islamic modernist scholar, University of Chicago; Islam and Modernity (1982)", c="Pakistan", cn="Pakistan",
      dom="religion", date="1982", era="posthumous", mirror=None, pol="conflicted", inten=2,
      saw="Names Atatürk and Inönü architects of a purely secular school system that expunged religion; says religion's subjugation to politics forced secularism, which is no answer.",
      q="whose two chief architects, Kemal Ataturk and Ismet Inonu, considered it a violation of the sanctity of the secularist principle even to mention the word \"Allah\" in public!",
      art="book", ev="P", med=None,
      cav="Islam and Modernity: Transformation of an Intellectual Tradition (University of Chicago Press, 1982), p. 63 (archive.org scan, printed page headers). Other passages: p. 54 ('despite Atatürk's personal allergy to religion Islam returned to national education — via nationalism'); p. 62 (Atatürk's government, 'under the claim of unifying all education, eliminated the traditional schools'); p. 91 ('Even the great and powerful Atatürk could not reform traditional education'); p. 140 ('it was this pernicious phenomenon [subjugation of religion to politics] that forced Kemal Ataturk to opt for secularism. Secularism is not the answer'). Polarity 'conflicted' because he sees both causes and failure; the dominant tone on education is critical. The scan's OCR spells the name 'Atatiirk'; the quote above is from a clean line.",
      src="src_fazlur_rahman_modernity.txt",
      urls=["https://archive.org/details/FazlurRahmanIslamandModernity"],
      loc="Fazlur Rahman, Islam and Modernity (Chicago, 1982), p. 63 (also pp. 54, 62, 91, 140)", link=None),
]

banks, bad = {}, []
for r in R:
    banks.setdefault(r["src"], bank(r["src"]))
    if norm(r["q"]) not in banks[r["src"]]:
        bad.append(r["id"])
if bad:
    sys.exit("quote not found in source bank: %s" % bad)
for r in R:
    assert len(r["saw"].split()) <= 25, (r["id"], len(r["saw"].split()))

with open(os.path.join(STATE, "gazes_memoirs.jsonl"), "w", encoding="utf-8") as f:
    for r in R:
        rec = {"id": r["id"], "voice": r["voice"], "voice_type": "person", "role": r["role"], "country": r["c"],
               "country_now": r["cn"], "domain": r["dom"], "date": r["date"], "era": r["era"], "mirror": r["mirror"],
               "polarity": r["pol"], "intensity": r["inten"], "what_they_saw": r["saw"], "quote": r["q"],
               "artifact": r["art"], "evidence": r["ev"], "mediated_by": r["med"], "caveat": r["cav"],
               "node": NODE, "sources": r["urls"]}
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")

nxt = {"mohammad-reza-pahlavi-1961": "Page-image check of p. 39; Hutchinson 1961 print copy",
       "mohammad-reza-pahlavi-1980": "Confirm whether the 1934 'knelt before him' episode is corroborated in Turkish sources",
       "muhammad-asad-1954": "Check pagination against the 1954 first edition; The Road to Mecca lending copy is on archive.org (roadtomecca00asad)",
       "mahathir-2003-07-10": "Malay version of the speech on mahathir.com; chedet.cc posts",
       "mahathir-2005-11": "Open the Project Syndicate original",
       "fazlur-rahman-1982": "Print copy to confirm pagination; Rahman's Islam (1966) chapter on modern developments"}
with open(os.path.join(STATE, "ledger_memoirs.md"), "w", encoding="utf-8") as f:
    f.write("| Claim | Node | Status | Sources | Next step |\n|---|---|---|---|---|\n")
    for r in R:
        f.write("| %s (%s, %s): \"%s\" | %s | verified %s (%s) | %s | %s |\n" % (
            r["voice"], r["role"], r["date"], r["q"][:110].replace("|", "/") + ("..." if len(r["q"]) > 110 else ""),
            NODE, r["ev"], r["loc"], "; ".join(r["urls"][:1]), nxt[r["id"]]))

body = ["""
Round 14 went looking for the famous names of the Islamic world, Asia and Africa speaking about Kemal in their own
books and speeches. Six records survived reading. Every quote was checked against fetched full text before this note was
written, and all are in English as published.

## The pattern

- **The son of the imitator:** [[Reza Shah Pahlavi]]'s son writes twice (1961, 1980) that his father was drawn to the
  Turkish republic and the 'dynamic leadership' behind it, then chose monarchy; the Shah gives facts, not a verdict.
- **The convert's disappointment:** Muhammad Asad (Leopold Weiss) credits the war of independence with an Islamic spirit
  and charges Atatürk with throwing away that force for a rejection of 'all Islamic values' (cf.
  [[Abolition of the Caliphate]]; compare [[Islamic Thinkers on Atatürk in Their Own Words]]).
- **The modernizer-defender:** Mahathir Mohamad in 2003 and 2005 defends him before Muslim audiences: he saved Turkey
  from Greek partition and 'saved Turkey for Islam'.
- **The Chicago reformer:** Fazlur Rahman writes of a purely secular education engineered by Atatürk and Inönü, and says
  secularism 'is not the answer'.
"""]
for r in R:
    body.append("\n## %s, %s (%s)\n" % (r["voice"], r["role"], r["date"]))
    body.append("*%s*\n" % r["saw"])
    body.append("> %s\n" % r["q"])
    body.append("%s Location: %s. Evidence %s%s.%s\n" % (r["cav"], r["loc"], r["ev"], (" (" + r["med"] + ")") if r["med"] else "", (" See [[%s]]." % r["link"]) if r["link"] else ""))

body.append("""
## Dry ends (round 14)

- **Ayub Khan:** *Friends Not Masters* (1967; archive.org `FriendsNotMastersAPoliticalAutobiographyByPresidentAyubKhan_201705`, full OCR grepped for Ataturk/Kemal/Mustafa) never names him The Turkey hits concern the Khilafat movement ('the idea of Khilafat had been abandoned by the Turks themselves'), Menderes, Gürsel and the pacts, not Atatürk.
- **King Hussein of Jordan:** *Uneasy Lies the Head* (archive.org `dli.ernet.524407`, full OCR grepped) has no Ataturk or Kemal hit.
- **Muhammad Asad, other books:** *Islam at the Crossroads* (1934) and *The Principles of State and Government in Islam* have no Atatürk hit by full-text grep.
- **Abul Kalam Azad:** *India Wins Freedom* (archive.org `dli.ernet.526499`) mentions 'followers of Mustafa Kamal Pasha' in Egypt in 1908 only (the Young Turk circle, not the later Atatürk).
- **Ahmed Ben Bella:** the open *Life of Combat* extract (57 KB) has no hit; the biography by Merle is lending-only.
- **Haile Selassie** (*My Life and Ethiopia's Progress*), **Tunku Abdul Rahman**, **Malcolm X**, **Ali Shariati**, **Zahir Shah**, **Boumediene**: the books are lending-only on archive.org and the search-inside route returned 'Item not available' without a login (not circumvented); web searches found no direct sentence.
- **Allama Mashriqi:** only a family-historian article (Nasim Yousaf, 2016) that cites his 18 Oct 1925 letter to Atatürk, his 1926 Cairo Caliphate Conference speech and *Al-Islah* of 18 Nov 1938; no quotation printed. A lead, not a record.

## Sources
- Mohammad Reza Pahlavi, *Mission for My Country* (1961), archive.org `mission-for-my-country-mohammad-reza-pahlavi_202605`.
- Mohammad Reza Pahlavi, *Answer to History* (1980), archive.org `Pahlavi-Answer-To-History`.
- Muhammad Asad, *The Road to Mecca* (1954; Islamic Book Service reprint), archive.org `road-to-mecca_202409`.
- Mahathir Mohamad, 'Islam in Era of Globalisation', 10 Jul 2003, mahathir.com.
- Mahathir Mohamad, 'Islam's forsaken renaissance', Taipei Times, 10 Nov 2005.
- Fazlur Rahman, *Islam and Modernity* (Chicago, 1982), archive.org `FazlurRahmanIslamandModernity`.
""")

note("Events", NODE,
     {"type": "event", "when": "1954–2005",
      "tags": ["event", "verified", "leaders", "islamic-world", "memoir"]},
     "\n".join(body))
print("ok", len(R), "records")
