# -*- coding: utf-8 -*-
# Census round 23 (Nov 2026) — Indian legislatures on Atatürk: Legislative Assembly 1924, 1925, 1938; Constituent Assembly 1946-49;
# Lok Sabha 1955-66. Source: official reports as digitised by Lok Sabha Secretariat (eparlib.nic.in, mirrored on archive.org)
# and the Government of India Press volume (archive.org in.ernet.dli.2015.13994). Evidence P (OCR text read).
# Banks: tools/.state/round23/ep/*.txt and dli/d1.txt. Refuses to run if an anchor is missing from its bank.
import json, os, re, sys
from _lib import note, person

HERE = os.path.dirname(os.path.abspath(__file__))
ST = os.path.join(HERE, "tools", ".state", "round23")
AR = "https://archive.org/download/"
EP = {"760449": "Constituent Assembly Debates Vol. 1 (reprint 2014), Book 1",
      "760458": "Constituent Assembly Debates Vol. 7 (Book 2)", "760459": "Constituent Assembly Debates Vol. 8 (Book 3)",
      "760688": "Legislative Assembly Debates, 25 Mar 1924", "761482": "Legislative Assembly Debates, 11 Feb 1925",
      "55822": "Lok Sabha Debates, 30 Nov 1955", "2906": "Lok Sabha Debates, 22 Aug 1963", "55402": "Lok Sabha Debates, 25 Aug 1966"}


def norm(s):
    s = re.sub(r"-\s*\n\s*", "", s)          # OCR hyphenation at line ends
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = re.sub(r"\s+", " ", s)
    return s.strip().lower()


def bank(path):
    return norm(open(os.path.join(ST, path), encoding="utf-8", errors="ignore").read())


N1 = "Indian Legislative Assembly Mourns Kemal, 14 November 1938 — Desai, Nairang, Aney, Aikman, Zafar Ali Khan and Sir Abdur Rahim"
N2 = "Indian Legislative Assembly on Kemal, 1924–1925 — Chaman Lall and Motilal Nehru"
N3 = "Constituent Assembly and Lok Sabha on Atatürk, 1946–1966 — Radhakrishnan, Gour, Kamath, Anthony and Brajeshwar Prasad"
D1 = "dli/d1.txt"
U1 = AR + "in.ernet.dli.2015.13994/2015.13994.The-Legislative-Assembly-Debates--vol-vii-Th-1938_djvu.txt"
LAD38 = "Legislative Assembly Debates, vol. VII (Government of India Press, Delhi 1938), 14 Nov 1938, "
OCRC = " Text read from the OCR of the official report; obvious OCR slips are silently corrected in the quote."

R = [
 dict(id="bhulabhai-desai-1938-11", voice="Bhulabhai Desai", role="Leader of the Opposition (Congress), Central Legislative Assembly", country="British India", cn="India", dom="politics",
      date="1938-11-14", era="funeral", mirror="modernization-poster-child", pol="admiring", inten=2, art="speech", bk=D1,
      anchors=["one of the most courageous of world reformers", "in a day he established the equality of man and"],
      q="He was, according to our humble appreciation, one of the most courageous of world reformers. In a day he abolished the purdah, in a day he established the equality of man and woman",
      saw="Moves the House's condolence: Kemal swept away every convention in the way of progress and left a lesson for India.",
      loc=LAD38 + "p. 2954", src=U1, tag=N1,
      cav="Desai asks that sympathy be conveyed to Ismet Inonu; he calls Kemal's 'courage' a legacy 'particularly applicable' to India." + OCRC),
 dict(id="nairang-1938-11", voice="Ghulam Bhik Nairang", role="Muslim member for East Punjab, Central Legislative Assembly", country="British India", cn="India", dom="politics",
      date="1938-11-14", era="funeral", mirror=None, pol="admiring", inten=2, art="speech", bk=D1,
      anchors=["veritable messiah of modern turkey", "it was given to mustafa kemal pasha to effect such marvellous changes"],
      q="It was given to Mustafa Kemal Pasha to effect such marvellous changes as to make him a veritable Messiah of modern Turkey",
      saw="As a Muslim, calls Kemal the most prominent figure in Asia, who revived a dead polity, a 'veritable Messiah of modern Turkey'.",
      loc=LAD38 + "pp. 2954-55", src=U1, tag=N1,
      cav="He also asks that the House adjourn for the day in respect." + OCRC),
 dict(id="aney-1938-11", voice="M. S. Aney", role="Member for Berar, Central Legislative Assembly (Congress Nationalist)", country="British India", cn="India", dom="politics",
      date="1938-11-14", era="funeral", mirror=None, pol="admiring", inten=2, art="speech", bk=D1,
      anchors=["in him the world has lost a towering personality", "the rare gift of bringing back to life the dead"],
      q="In him the world has lost a towering personality. He belonged to that race of great men who had the rare good fortune and the rare gift of bringing back to life the dead",
      saw="Calls Kemal a towering personality who revived Turkey like the Phoenix, admired most for the courage of his reforms.",
      loc=LAD38 + "p. 2955", src=U1, tag=N1, cav="He quotes a Sanskrit maxim that success depends on the mettle of the man." + OCRC),
 dict(id="aikman-1938-11", voice="A. Aikman", role="Bengal European member, Central Legislative Assembly", country="British India", cn="India", dom="politics",
      date="1938-11-14", era="funeral", mirror="nation-forge-template", pol="admiring", inten=1, art="speech", bk=D1,
      anchors=["an outstanding figure, a soldier, a diplomat and a nation builder"],
      q="in the passing of Kemal Pasha there has been lost to civilization an outstanding figure, a soldier, a diplomat and a nation builder",
      saw="For the European Group, mourns Kemal as soldier, diplomat and above all nation builder, a unique example of what one man's courage can do.",
      loc=LAD38 + "pp. 2955-56", src=U1, tag=N1, cav="Initials as printed; full name not given in the report." + OCRC),
 dict(id="zafar-ali-khan-1938-11", voice="Zafar Ali Khan", role="Urdu poet and editor of Zamindar, Muslim League member for East Central Punjab", country="British India", cn="India", dom="politics",
      date="1938-11-14", era="funeral", mirror=None, pol="admiring", inten=2, art="speech", bk=D1,
      anchors=["more to the mussalman world than to any other section of humanity", "one of the greatest figures of the modern age"],
      q="Mustafa Kemal Pasha's death means more to the Mussalman world than to any other section of humanity.",
      saw="Reads an Urdu elegy and calls Kemal 'one of the greatest figures of the modern age', correcting himself to 'the greatest'; asks for a holiday.",
      loc=LAD38 + "pp. 2956-57", src=U1, tag=N1,
      cav="The Urdu verses are printed in transliteration in the report; they are not quoted here. He threatens that the Muslim League will walk out unless the House adjourns." + OCRC),
 dict(id="abdur-rahim-1938-11", voice="Sir Abdur Rahim", role="President of the Central Legislative Assembly", country="British India", cn="India", dom="politics",
      date="1938-11-14", era="funeral", mirror="nation-forge-template", pol="admiring", inten=2, art="speech", bk=D1,
      anchors=["not only saved turkey", "a far-seeing statesman he laid a new foundation, a very strong foundation for the national life of his people"],
      q="Kemal Ataturk not only saved Turkey from political annihilation by his military genius, but as a far-seeing statesman he laid a new foundation, a very strong foundation for the national life of his people",
      saw="As President, allows the unusual condolence for a foreign ruler: Kemal's influence on Asia has 'no parallel in the history of modern times'.",
      loc=LAD38 + "p. 2957", src=U1, tag=N1,
      cav="He adjourned the House as a mark of respect once Nripendra Sircar and Desai agreed, and promised to convey sympathy to Ismet Inonu." + OCRC),
 dict(id="chaman-lall-1924-03", voice="Diwan Chaman Lall", role="Labour leader, member for West Punjab, Legislative Assembly", country="British India", cn="India", dom="politics",
      date="1924-03-25", era="contemporary", mirror="anti-colonial-liberator", pol="admiring", inten=1, art="speech", bk="ep/eparlib.nic.in.760688.txt",
      anchors=["it was not the government of india but the sword of mustapha kemal pasha"],
      q="it was not the Government of India but the Sword of Mustapha Kemal Pasha.",
      saw="In the passports-for-the-Khilafat-delegation adjournment debate, credits Kemal's sword, not Government of India diplomacy, with revising the Treaty of Sevres.",
      loc="Legislative Assembly Debates, vol. IV pt. III, 25 Mar 1924, p. 2214", src=AR + "eparlib.nic.in.760688/", tag=N2,
      cav="Said as the Chair stopped him from turning the debate into one on foreign policy; the Khilafat delegation to Angora was to present congratulatory addresses to 'Ghazi Mustafa Kamal Pasha'." + OCRC),
 dict(id="motilal-nehru-1925-02", voice="Motilal Nehru", role="Leader of the Swaraj Party, member for the Cities of the United Provinces", country="British India", cn="India", dom="politics",
      date="1925-02-11", era="contemporary", mirror=None, pol="admiring", inten=1, art="speech", bk="ep/eparlib.nic.in.761482.txt",
      anchors=["now that is a government of the people by themselves", "can keep all the dignity attached to that position on", "a person of the distinction of mustapha kemal"],
      q="Now that is a government of the people by themselves, and if a person of the distinction of Mustapha Kemal Pasha and his position in the country as the head of the administration, can keep all the dignity attached to that position on £40 a month",
      saw="Arguing for a modest President's salary, holds up Kemal, head of the Turkish administration on £40 a month, as a government of the people.",
      loc="Legislative Assembly Debates, vol. I pt. II, 11 Feb 1925, President's Salary Bill, p. 975", src=AR + "eparlib.nic.in.761482/", tag=N2,
      cav="He prefaces it 'I do not know how far it is correct' (a newspaper report). Instrumental use of Kemal as a model of frugal republican leadership; 'Pasha' OCR-corrected from 'Fasha'. Father of Jawaharlal Nehru." + OCRC),
 dict(id="radhakrishnan-1947-01", voice="S. Radhakrishnan", role="Philosopher; member of the Constituent Assembly (United Provinces), later President of India", country="India", cn="India", dom="politics",
      date="1947-01-20", era="posthumous", mirror="secular-rationalist-prophet", pol="admiring", inten=1, art="speech", bk="ep/eparlib.nic.in.760449.txt",
      anchors=["kemal pasha's defiant creation of a secular turkey", "the days of religious states are over"],
      q="Allenby's liberating campaigns in Egypt, Lawrence's adventures in Arabia, Kemal Pasha's defiant creation of a secular Turkey, point out that the days of religious States are over.",
      saw="Arguing against partition, names Kemal Pasha's 'defiant creation of a secular Turkey' as proof that the days of religious states are over.",
      loc="Constituent Assembly of India Debates, vol. II, 20 Jan 1947 (Objectives Resolution), p. 272", src=AR + "eparlib.nic.in.760449/", tag=N3,
      cav="Speaker identified from the nearest preceding speaker line ('Sir S. Radhakrishnan (United Provinces: General)'); the page header 272 precedes the passage." + OCRC),
 dict(id="hari-singh-gour-1946-12", voice="Hari Singh Gour", role="Jurist, founder of Sagar University; member of the Constituent Assembly (C.P. and Berar)", country="India", cn="India", dom="politics",
      date="1946-12-19", era="posthumous", mirror="secular-rationalist-prophet", pol="admiring", inten=2, art="speech", bk="ep/eparlib.nic.in.760449.txt",
      anchors=["kemal pasha ata-turk saw the futility and unwisdom of combining politics with religion", "the first thing he did was to put an end to pakistan"],
      q="Kemal Pasha Ata-Turk saw the futility and unwisdom of combining politics with religion. The first thing he did was to put an end to Pakistan and establish the Republic of Turkey.",
      saw="In the Constituent Assembly's first session, tells Muslims that Kemal Pasha saw the unwisdom of mixing religion and politics; urges them to reject Jinnah's Pakistan.",
      loc="Constituent Assembly of India Debates, vol. I, 19 Dec 1946, p. 149 (page header 150 follows the passage)", src=AR + "eparlib.nic.in.760449/", tag=N3,
      cav="Gour's 'Pakistan' here means the old Ottoman Caliphate-Sultanate arrangement (his own use of the word); the vault does not adopt his framing of Muslim politics. Speaker header 'Dr. Sir Hari Singh Gour (C. P. and Berar' precedes the passage." + OCRC),
 dict(id="brajeshwar-prasad-1948-11", voice="Brajeshwar Prasad", role="Member of the Constituent Assembly (Bihar)", country="India", cn="India", dom="politics",
      date="1948-11-09", era="posthumous", mirror=None, pol="instrumental", inten=2, art="speech", bk="ep/eparlib.nic.in.760458.txt",
      anchors=["the system of government set up by hitler, mussolini, kemal ataturk and stalin represent the indirect forms of democracy", "the whole of germany, italy and turkey were behind the dictators", "the records of mushtapha kemal and mussolini are as good as that of the leaders of parliamentary democracy"],
      q="The system of government set up by Hitler, Mussolini, Kemal Ataturk and Stalin represent the indirect forms of democracy. The whole of Germany, Italy and Turkey were behind the dictators.",
      saw="Against parliamentary democracy, lists Kemal with Hitler, Mussolini and Stalin as builders of 'indirect' democracy; later, his record is 'as good' as parliamentarians'.",
      loc="Constituent Assembly of India Debates, vol. VII, 9 Nov 1948, pp. 373-374", src=AR + "eparlib.nic.in.760458/", tag=N3,
      cav="Speaks for 'philosopher-kings' and one-party rule; the same speech says 'Germany, Italy and Turkey rose to grand heights under Hitler, Mussolini and Kemal Ataturk' and 'the records of Mushtapha Kemal and Mussolini are as good as that of the leaders of parliamentary democracy' (p. 374). Sensitive framing (fascist comparison) is the speaker's own." + OCRC),
 dict(id="kamath-1949-05", voice="Hari Vishnu Kamath", role="Member of the Constituent Assembly, later Lok Sabha member (Praja Socialist)", country="India", cn="India", dom="politics",
      date="1949-05-16", era="posthumous", mirror="anti-colonial-liberator", pol="admiring", inten=1, art="speech", bk="ep/eparlib.nic.in.760459.txt",
      anchors=["at the close of world war i, kemal ataturk with his ragged army stood alone against many of the powerful countries of europe and beat them back"],
      q="At the close of World War I, Kemal Ataturk with his ragged army stood alone against many of the powerful countries of Europe and beat them back.",
      saw="Opposing the Commonwealth decision, holds up Kemal and his 'ragged army' as proof that small nations can stand alone against the Powers.",
      loc="Constituent Assembly of India Debates, vol. VIII, 16 May 1949, p. 23", src=AR + "eparlib.nic.in.760459/", tag=N3,
      cav="Speaker taken from the running header '[Shri H. V. Kamath]' on the preceding page; he returns to Kemal on 7 Sept 1949 (the Roman-script reform, as an argument against prejudice towards English)." + OCRC),
 dict(id="frank-anthony-1955-11", voice="Frank Anthony", role="Leader of the Anglo-Indian community, nominated member of the Lok Sabha", country="India", cn="India", dom="politics",
      date="1955-11-30", era="posthumous", mirror=None, pol="instrumental", inten=1, art="speech", bk="ep/eparlib.nic.in.55822.txt",
      anchors=["mustafa kemal ata turk stamped out black-marketing in foodgrains because he introduced whipping"],
      q="Mustafa Kemal Ata Turk stamped out black-marketing in foodgrains because he introduced whipping.",
      saw="Opposing abolition of whipping, cites Kemal Ataturk as the ruler who stamped out black-marketing by introducing it.",
      loc="Lok Sabha Debates, 30 Nov 1955, Abolition of Whipping Bill, c. 804", src=AR + "eparlib.nic.in.55822/", tag=N3,
      cav="Used for Anthony's own argument; an unverified claim about Kemal's policy, recorded only as his view." + OCRC),
 dict(id="kamath-1963-08", voice="Hari Vishnu Kamath", role="Lok Sabha member (Praja Socialist), Hoshangabad", country="India", cn="India", dom="politics",
      date="1963-08-22", era="posthumous", mirror=None, pol="instrumental", inten=1, art="speech", bk="ep/eparlib.nic.in.2906.txt",
      anchors=["remember that kemal ataturk of turkey as soon as he came to power"],
      q="Remember that Kemal Ataturk of Turkey as soon as he came to power, for a small reform like stopping spitting in the streets prescribed flogging",
      saw="In the no-confidence debate on corruption, says Kemal prescribed flogging for spitting and ended the habit by making an example of six people.",
      loc="Lok Sabha Debates, 22 Aug 1963 (no-confidence motion), cols. c. 2174-75 (OCR 2175)", src=AR + "eparlib.nic.in.2906/", tag=N3,
      cav="Kamath repeats the story on 17 Apr 1963 and 25 Aug 1966 (flogging bill debates), always as a model of drastic penalty. Column from OCR page header '2175 Motion'." + OCRC),
]

# --- bank check ---
bad = 0
banks = {}
for r in R:
    b = banks.setdefault(r["bk"], bank(r["bk"]))
    for a in r["anchors"]:
        if norm(a) not in b:
            print("MISSING", r["id"], a); bad += 1
if bad:
    sys.exit("anchor check failed")
for r in R:
    assert len(r["saw"].split()) <= 25, (r["id"], len(r["saw"].split()))
    assert len(re.findall(r"[.!?](?:\s|$)", r["q"])) <= 2, r["id"]

with open(os.path.join(ST, "gazes_parliaments.jsonl"), "w", encoding="utf-8") as f:
    for r in R:
        rec = {"id": r["id"], "voice": r["voice"], "voice_type": "person", "role": r["role"], "country": r["country"], "country_now": r["cn"],
               "domain": r["dom"], "date": r["date"], "era": r["era"], "mirror": r["mirror"], "polarity": r["pol"], "intensity": r["inten"],
               "what_they_saw": r["saw"], "quote": r["q"], "artifact": r["art"], "evidence": "P", "mediated_by": None,
               "caveat": r["loc"] + ". Official report digitised by the Lok Sabha Secretariat / Government of India Press, via archive.org OCR. " + r["cav"],
               "node": r["tag"], "sources": [r["src"]]}
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
with open(os.path.join(ST, "ledger_parliaments.md"), "w", encoding="utf-8") as f:
    f.write("| Claim | Node | Status | Sources | Next step |\n|---|---|---|---|---|\n")
    for r in R:
        f.write("| %s, %s: %s | %s | verified P (archive.org OCR of the official report read, anchors matched) | %s | Check against the page image for the column or page if a print edition is needed |\n"
                % (r["voice"], r["loc"], r["pol"], r["tag"], r["src"]))

L = lambda n: "[[%s]]" % n
byid = {r["id"]: r for r in R}

PEOPLE = {
 "Bhulabhai Desai": ("Indian lawyer and Congress Leader of the Opposition in the Central Legislative Assembly", "1877–1946", "admiring (1938)", ["bhulabhai-desai-1938-11"], N1,
   "Opened the Assembly's condolence on 14 November 1938: Kemal was 'one of the most courageous of world reformers', who in a day abolished the purdah."),
 "Ghulam Bhik Nairang": ("Punjab lawyer and Muslim member of the Central Legislative Assembly", "1878–1952", "admiring (1938)", ["nairang-1938-11"], N1,
   "Called Kemal, for a Muslim, 'a veritable Messiah of modern Turkey' and the most prominent figure in Asia."),
 "M. S. Aney": ("Marathi nationalist, member for Berar in the Central Legislative Assembly", "1880–1971", "admiring (1938)", ["aney-1938-11"], N1,
   "Called Kemal 'a towering personality' who brought Turkey back to life like the Phoenix."),
 "Zafar Ali Khan": ("Urdu poet and editor of Zamindar, Muslim League member", "1873–1956", "admiring (1938)", ["zafar-ali-khan-1938-11"], N1,
   "Read an elegy to Kemal in the Assembly on 14 November 1938 and asked for a holiday in his memory."),
 "Sir Abdur Rahim": ("President of the Central Legislative Assembly 1935–45", "1867–1952", "admiring (1938)", ["abdur-rahim-1938-11"], N1,
   "Allowed the condolence for a foreign ruler because Kemal's influence on Asia had 'no parallel in the history of modern times'."),
 "Diwan Chaman Lall": ("Indian trade-union leader and member of the Legislative Assembly", "1892–1973", "admiring (1924)", ["chaman-lall-1924-03"], N2,
   "In March 1924 credited 'the Sword of Mustapha Kemal Pasha', not the Government of India, with the revision of the Treaty of Sevres."),
 "Motilal Nehru": ("Allahabad lawyer, Swaraj Party leader, father of Jawaharlal Nehru", "1861–1931", "admiring (1925)", ["motilal-nehru-1925-02"], N2,
   "On 11 February 1925 held up Kemal, head of the Turkish administration on £40 a month, as the model for the Assembly's President's pay."),
 "S. Radhakrishnan": ("Philosopher, Vice-President (1952) and President (1962) of India", "1888–1975", "admiring (1947)", ["radhakrishnan-1947-01"], N3,
   "Named 'Kemal Pasha's defiant creation of a secular Turkey' in January 1947 as proof that religious states were finished."),
 "Hari Singh Gour": ("Jurist and Constituent Assembly member", "1870–1949", "admiring (1946)", ["hari-singh-gour-1946-12"], N3,
   "In the Assembly's first session told Muslim members that Kemal saw the unwisdom of combining politics with religion."),
 "Hari Vishnu Kamath": ("Constituent Assembly and Lok Sabha member", "1907–1982", "admiring (1949), instrumental (1963)", ["kamath-1949-05", "kamath-1963-08"], N3,
   "Uses Kemal across 1949-66: the ragged army that stood alone (16 May 1949), the Roman script, and the flogging of spitters as a model of drastic penalty."),
 "Frank Anthony": ("Leader of the Anglo-Indian community, nominated Lok Sabha member", "1908–1993", "instrumental (1955)", ["frank-anthony-1955-11"], N3,
   "Cited Kemal as having stamped out black-marketing by introducing whipping (30 November 1955)."),
 "Brajeshwar Prasad": ("Constituent Assembly member from Bihar", "1910s-", "instrumental (1948)", ["brajeshwar-prasad-1948-11"], N3,
   "Named Kemal with Hitler, Mussolini and Stalin as builders of 'indirect' democracy in his Constituent Assembly speech against parliamentarism (9 November 1948)."),
}
for name, (role, life, stance, ids, node, text) in PEOPLE.items():
    body = text + " See " + L(node) + ".\n\n## Sources\n" + "\n".join("- %s (%s)" % (byid[i]["src"], byid[i]["loc"]) for i in ids)
    person(name, role=role, nat="Indian", life=life, stance=stance, tags=["politics", "india", "verified", "parliament"], body=body)


def event(tag, when, intro, ids):
    body = intro + "\n\n"
    for i in ids:
        r = byid[i]
        body += "## %s (%s)\n\n> %s\n\n%s. %s\n\n" % (r["voice"], r["date"], r["q"], r["loc"], r["cav"])
    body += "## Sources\n" + "\n".join("- %s" % s for s in sorted({byid[i]["src"] for i in ids})) + "\n"
    note("Events", tag, {"type": "event", "when": when, "tags": ["event", "verified", "india", "parliament", "politics"]}, body)

event(N1, "1938-11-14",
 "At the start of business on 14 November 1938 the Leader of the Opposition, Bhulabhai Desai, asked the President of the Central Legislative Assembly (Delhi) to let the House record its loss at Kemal's death; five more voices followed and the President himself spoke warmly before adjourning the House as a mark of respect. The Muslim League asked for the adjournment; Nripendra Sircar, for the Government, did not object. Broader Indian reaction: [[India Mourns, November 1938]].",
 [r["id"] for r in R if r["tag"] == N1])
event(N2, "1924-1925",
 "Two Legislative Assembly speeches. Chaman Lall (25 March 1924) in the debate on passports for the Khilafat delegation to Angora: Kemal's sword, not British diplomacy, had won revision of Sevres. Motilal Nehru (11 February 1925) used Kemal's £40 salary as head of the administration in the debate on the President's pay. Earlier Indian reactions: [[Gaya to Angora — Indian Voices on Kemal, 1922–1924]]; later: [[Jawaharlal Nehru]]. (A third voice of the 1924 debates, Harchandrai Vishindas on 6 March 1924, said the abolition of the Caliphate was 'a lesson' the Government of India should take, and is noted in the candidates file.)",
 [r["id"] for r in R if r["tag"] == N2])
event(N3, "1946-1966",
 "Found by archive.org full-text search over the Lok Sabha Secretariat's digitised debates. In the Constituent Assembly Kemal is a weapon in the argument over religion and the state (Gour, Radhakrishnan, against Jinnah's Pakistan) and over strong government (Brajeshwar Prasad); after independence he becomes an example in Lok Sabha: the ragged army (Kamath 1949), whipping and flogging (Anthony 1955, Kamath 1963). Nehru's own view: [[Jawaharlal Nehru]].",
 [r["id"] for r in R if r["tag"] == N3])
print(len(R), "records ok")
