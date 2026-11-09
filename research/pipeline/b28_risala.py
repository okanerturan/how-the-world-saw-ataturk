# -*- coding: utf-8 -*-
# Census round 19 (Nov 2026) — Egyptian and Arab pens on Ataturk in al-Risala (Cairo), 1935-1946.
# Source: Arabic Wikisource transcription of al-Risala (free API). Pages banked in tools/.state/round19/;
# the script refuses to run if a quote is not in its bank.
import json, os, re, sys, unicodedata, urllib.parse
from _lib import note, person

HERE = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(HERE, "tools", ".state", "round19")
NODE = "Egyptian Pens in al-Risala on Atatürk, 1935–1946"


def norm(s):
    s = unicodedata.normalize("NFKC", s)
    s = re.sub(r"[ً-ٟـ]", "", s)
    s = re.sub("[أإآٱ]", "ا", s).replace("ى", "ي").replace("ة", "ه")
    s = re.sub(r"[«»()\[\]]", " ", s)
    s = re.sub(r"\s+", " ", s)
    return s.strip().lower()


def bank(h):
    return norm(open(os.path.join(STATE, "p_%s.txt" % h), encoding="utf-8").read())


def url(title):
    return "https://ar.wikisource.org/wiki/" + urllib.parse.quote(title.replace(" ", "_"), safe="/_:")


def T(n, t):
    return "مجلة الرسالة/العدد %s/%s" % (n, t)


Z = "Ahmad Hasan al-Zayyat"
R = [
 dict(id="azzam-1935", voice="Abd al-Wahhab Azzam", role="Egyptian orientalist and professor (later Egypt's minister to Saudi Arabia)",
      c="Egypt", cn="Egypt", dom="letters", date="1935-07-01", era="contemporary", mirror="apostate", pol="conflicted", inten=2,
      art="article", ev="S", h="bccea4", page=T(104, "النهضة التركية الأخيرة"), issue="al-Risala no. 104, 1 Jul 1935",
      saw="In a serial against 'the Kemalists', says Muslims counted the Ghazi their undisputed hero, yet he led the Kemalists' break with Islam.",
      q="وكان أشدهم إفراطاً في ذلك الغازي مصطفى كمال باشا الذي كان المسلمون جميعهم يعدونه بطل أبطالهم غير مدافع.",
      tr="The most extreme of them in that was the Ghazi Mustafa Kemal Pasha, whom all Muslims used to count the hero of their heroes, beyond dispute.",
      cav="Part of the series 'The Latest Turkish Revival' by Dr Abd al-Wahhab Azzam in al-Risala nos. 101 (10 Jun 1935), 104 (1 Jul), 108 (29 Jul) and 111 (19 Aug, by another hand on music); the quote is from no. 104. In no. 101 he writes that abolishing the caliphate 'was not a necessity required by reform, but an excess the revolution led to'; in no. 108 he faults the Kemalists' policy on women and tells of an Egyptian women's delegate who called the Ghazi 'Atashark'. Mostly he blames 'the Kemalists' collectively; the Ghazi is named for the Qur'an anecdote and as the leader in rejecting Islam. Wikisource transcription; no page image linked.",
      link="Abd al-Wahhab Azzam", nxt="Print pages of nos. 101, 104, 108 (vol. 3); Azzam's own later pieces on Turkey (his 1937 Istanbul visit is al-Risala no. 233, 20 Dec 1937, which only mentions the Ghazi's portrait)"),
 dict(id="zayyat-1935-03", voice="Ahmad Hasan al-Zayyat", role="Editor of al-Risala, Cairo",
      c="Egypt", cn="Egypt", dom="press", date="1935-03-11", era="contemporary", mirror="apostate", pol="conflicted", inten=2,
      art="editorial", ev="S", h="aaf4ee", page=T(88, "إلى أين يساق الأتراك؟"), issue="al-Risala no. 88, 11 Mar 1935",
      saw="Addresses the great Ghazi Atatürk: praises him for reviving the Sick Man, then says he wronged Turkey's history against nature and logic.",
      q="ولكنك ظلمت تاريخك الخاص بمخالفة الطبيعة في التجديد، ومجانبة المنطق في الاصلاح.",
      tr="But you wronged your own history by going against nature in renewal and shunning logic in reform.",
      cav="Editorial 'Where Are the Turks Being Driven?', signed Ahmad Hasan al-Zayyat, addressed to Atatürk in the second person. Just before the quote: 'You mended the broken wing and revived the Sick Man ... your name is the title of its modern history'. Just after: he fears history will record that Atatürk 'revived a state and killed a nation, built a constitution and demolished a creed'. Distinct from al-Zayyat's 14 Nov 1938 obituary editorial already in the dataset. Wikisource transcription; no page image linked.",
      link=Z, nxt="Print page; any reply to this editorial in al-Risala nos. 89-92"),
 dict(id="rafii-1935", voice="Mustafa Sadiq al-Rafi'i", role="Egyptian essayist and traditionalist man of letters (Tanta)",
      c="Egypt", cn="Egypt", dom="letters", date="1935-07-15", era="contemporary", mirror="apostate", pol="hostile", inten=2,
      art="article", ev="S", h="722fd5", page=T(106, "فلسفة الطائشة"), issue="al-Risala no. 106, 15 Jul 1935",
      saw="Through a fictional woman interlocutor: Mustafa Kemal is a rebel, not a reformer, a commander made vain by victory, whose hatred of religion proves it.",
      q="وليس الرجل مصلحاً ألبتة، بل هو قائد زهاه النصر الذي أتفق له",
      tr="The man is not a reformer at all, but a commander made vain by the victory that fell to him.",
      cav="From 'The Philosophy of the Ta'isha' (a column of conversations between the narrator and his female companion), signed Mustafa Sadiq al-Rafi'i, Tanta. The sentence is spoken by the woman character ('she said'), so it is Rafi'i's written voice but a persona's speech. She also says: 'his hatred of religion and its people is the proof that he is a rebel, not a reformer', that he makes Europe's vices 'take Turkish nationality', and that the nation 'was not born of the demolition of mosques and hanging of scholars' but of its mothers and fathers who lacked only a firm commander. Sensitive on religion: reported as the speaker's framing, not the vault's. Wikisource transcription.",
      link="Mustafa Sadiq al-Rafi'i", nxt="Print page; Rafi'i's collected 'Wahy al-Qalam' / 'Ta'isha' columns for a parallel passage"),
 dict(id="tantawi-1935", voice="Ali al-Tantawi", role="Syrian writer and jurist (writing from Mecca)",
      c="Syria", cn="Syria", dom="letters", date="1935-05-20", era="contemporary", mirror="apostate", pol="hostile", inten=1,
      art="article", ev="S", h="5ee8db", page=T(98, "أيا صوفيا"), issue="al-Risala no. 98, 20 May 1935",
      saw="On Hagia Sophia: the page of Islam was closed there 'in the name of this ... Atatürk', as it opened in Muhammad the Conqueror's name.",
      q="وشعروا أن أيا صوفيا قد ختمت فيها صفحة الإسلام، باسم هذا الـ. . (أتاتورك) كما فتحت باسم (محمد الفاتح)!",
      tr="And they felt that in Hagia Sophia the page of Islam had been closed, in the name of this ... (Atatürk), as it was opened in the name of (Muhammad the Conqueror)!",
      cav="Piece 'Aya Sufya' signed Ali al-Tantawi, Mecca; the gap '. .' before '(Atatürk)' is in the transcription (an epithet left out or lost). Same issue family as Amjad al-Tarabulsi's ode of no. 109, which is a separate record. Wikisource transcription.",
      link="Ali al-Tantawi", nxt="Print page; Tantawi's memoirs (Dhikrayat) on his Hagia Sophia reaction"),
 dict(id="aqqad-1945", voice="Abbas Mahmud al-Aqqad", role="Egyptian essayist, poet and critic",
      c="Egypt", cn="Egypt", dom="letters", date="1945-05-14", era="posthumous", mirror="nation-forge-template", pol="admiring", inten=1,
      art="article", ev="S", h="9f97c7", page=T(619, "التربية السياسية"), issue="al-Risala no. 619, 14 May 1945",
      saw="Holds Mustafa Kemal up against Hitler: he spent a fraction of Hitler's armaments yet retook Istanbul with the Allied armies in it.",
      q="واستطاع مع ذلك أن يفتح الآستانة فتحاً ثانياً وفيها جيوش الحلفاء",
      tr="and yet he was able to conquer Istanbul a second time, with the Allied armies in it.",
      cav="Al-Aqqad cites his own earlier line from his book 'Hitler in the Balance' (1940). Argument: Kemal's success rested on shrewdness, not on spending on arms; he also had the Turks regain the forts and abolish the capitulations. A related remark in no. 629 (23 Jul 1945, 'Voice and Personality') says the voices of Churchill and Mustafa Kemal surprised him, and calls Kemal 'the hero of the Turks'; in no. 400 (3 Mar 1941) he lists 'the experiment of Mustafa Kemal in Turkey' among revolutions that needed state power. Passing but in his own words. Wikisource transcription.",
      link="Abbas Mahmud al-Aqqad", nxt="'Hitler fi'l-Mizan' (1940) text for the original line; al-Aqqad's 1938 obituary of Atatürk if any (no. 280 holds only his unrelated column)"),
 dict(id="zaki-mubarak-1938", voice="Zaki Mubarak", role="Egyptian writer and critic (then teaching in Baghdad)",
      c="Egypt", cn="Egypt", dom="letters", date="1938-06-06", era="contemporary", mirror=None, pol="conflicted", inten=1,
      art="article", ev="S", h="29b58a", page=T(257, "ليلى المريضة في العراق"), issue="al-Risala no. 257, 6 Jun 1938",
      saw="Asks why no delegation goes to the Ghazi to remind him that grudge against the Arabs should not erase their gift of faith to Turkey.",
      q="هل فكرت في إرسال وفد إلى الغازي مصطفى كمال يذكره بأن الحقد على العرب الذين خذلوا تركيا في الحرب لا يصح أن ينسيه فضل العرب الأبرار الذين نقلوا إلى تركيا بذور الإيمان بالله والرسول؟",
      tr="Has it thought of sending a delegation to the Ghazi Mustafa Kemal to remind him that grudge against the Arabs who let Turkey down in the war must not make him forget the merit of the righteous Arabs who carried to Turkey the seeds of faith in God and the Prophet?",
      cav="Rhetorical question in an article on the Arabic language abroad, signed Zaki Mubarak, written from Iraq five months before Atatürk's death. Accepts, as the premise, that the Ghazi bears a grudge against the Arabs. Mubarak returns to the theme in no. 433 (20 Oct 1941), saying that because of a foolish article on the Arabs' merit over the Turks 'Atatürk swore he would abandon the Arabic letters'. Wikisource transcription.",
      link="Zaki Mubarak", nxt="Print page; Mubarak's book on Arabic and the Turks if any"),
 dict(id="zaki-mubarak-1942", voice="Zaki Mubarak", role="Egyptian writer and critic",
      c="Egypt", cn="Egypt", dom="letters", date="1942-04-13", era="posthumous", mirror=None, pol="hostile", inten=1,
      art="article", ev="S", h="af17c6", page=T(458, "اجتماع الملائكة في مسجد الفردوس"), issue="al-Risala no. 458, 13 Apr 1942",
      saw="Recalls that 'the late Mustafa Kemal' claimed Adam and Eve were Turks; he found the claim monstrous and wrote to Kemal that they were Arabs.",
      q="كان المرحوم مصطفى كمال زعم أن آدم وحواء من أصل تركيّ، وقد أزعجني هذا الزعم الفظيع",
      tr="The late Mustafa Kemal claimed that Adam and Eve were of Turkish origin, and this monstrous claim disturbed me.",
      cav="Mubarak says he then wrote Kemal a letter arguing from etymology that Adam and Eve were Arabs; no reply or copy of the letter is cited, so the letter is his claim only. The Adam-and-Eve claim attributed to Kemal is Mubarak's report of the Turkish History Thesis era, not checked here. Humorous in tone. Wikisource transcription.",
      link="Zaki Mubarak", nxt="Look for the letter in Mubarak's papers or in al-Risala 1937-38"),
 dict(id="mandur-1944", voice="Muhammad Mandur", role="Egyptian literary critic",
      c="Egypt", cn="Egypt", dom="letters", date="1944-09-25", era="posthumous", mirror="nation-forge-template", pol="admiring", inten=1,
      art="article", ev="S", h="138056", page=T(586, "مكافحة الشكلية"), issue="al-Risala no. 586, 25 Sep 1944",
      saw="Cites Mustafa Kemal and Stalin as proof that determined will overcomes obstacles regardless of collective mind or social laws.",
      q="وأن إرادتنا لابد آتية على كافة الصعاب كما أتى مصطفى كمال على صعاب تركيا وستالين على صعاب روسيا",
      tr="and that our will must surely overcome all obstacles, as Mustafa Kemal overcame Turkey's obstacles and Stalin Russia's.",
      cav="Closing sentence of an essay on 'Combating Formalism', signed Muhammad Mandur, in which Kemal serves as an example of voluntarism; no assessment of his reforms. Instrumental use in a Egyptian reform argument. Wikisource transcription.",
      link="Muhammad Mandur", nxt="none (passing)"),
 dict(id="felix-faris-1938", voice="Felix Faris", role="Lebanese-Egyptian essayist and polemicist",
      c="Egypt", cn="Egypt", dom="letters", date="1938-06-06", era="contemporary", mirror=None, pol="conflicted", inten=2,
      art="article", ev="S", h="78cf0a", page=T(257, "بين الشرق والغرب"), issue="al-Risala no. 257, 6 Jun 1938",
      saw="Calls Atatürk 'the shrewd' who knew the Turkish people's nature, a reformer who weakened every element out of tune with Turkey's spirit.",
      q="تلك حقائق لم تخف على الداهية أتاتورك فأنه عرف ما هي فطرة الشعب التركي وما هي الحالة الاجتماعية التي تتفق وما كمن في حوافزه.",
      tr="These facts were not hidden from the shrewd Atatürk, for he knew what the Turkish people's nature was and what social condition accorded with what lay hidden in its drives.",
      cav="From the first part of 'Between East and West' (continued next issue), signed Felix Faris, replying to an opponent ('al-munazir') who praised Westernising and the end of Ottoman rule; Faris argues the Ottomans did not spread Arab culture, and that Atatürk understood this. Next sentence: 'Thinkers know what this reformer of his state aimed at, weakening every element that did not keep pace with its spirit, so that he made Arabic letters and words his enemy.' Neutral on the Arabic-letters point; reported as the speaker's framing. Wikisource transcription.",
      link="Felix Faris", nxt="Part 2 of the series (no. 258); the opponent's piece"),
 dict(id="ahmad-ramzi-1946", voice="Ahmad Ramzi", role="Egyptian writer and historian ('Bey'), seven years resident in Turkey",
      c="Egypt", cn="Egypt", dom="letters", date="1946-11-18", era="posthumous", mirror="nation-forge-template", pol="conflicted", inten=2,
      art="article", ev="S", h="e6cf06", page=T(698, "الغازي مصطفى كمال"), issue="al-Risala no. 698, 18 Nov 1946",
      saw="Sees the Ghazi as one of the few in the East who acted after long thought; ends by predicting his 'bewildered soul' will be explained.",
      q="إذ هو من الأفراد القلائل في الشرق الذين عملوا بعد تفكير طويل، وأخضعوا أعمالهم لفكرتهم الأولى",
      tr="For he is one of the few individuals in the East who acted after long reflection and made their deeds obedient to their first idea.",
      cav="First instalment of 'The Ghazi Mustafa Kemal: study and analysis of the psychological motives that led him to leadership', signed Ahmad Ramzi Bey ('I write these words after seven years in Turkey'). Closing line of the instalment, verbatim: 'Mustafa Kemal is only one of those [who left the faith's path and will return to it]; the days will reveal much of his bewildered soul'. Ramzi also translated Count Sforza's essay 'Mustafa Kemal the Turkish leader' in nos. 836-838 (Jul 1949) - the text Khalil Mutran was suspected of writing; Sforza is already a voice (1931). Identity of 'Ahmad Ramzi Bey' not established beyond the text. Religion: reported as the speaker's framing. Wikisource transcription.",
      link="Ahmad Ramzi", nxt="Later instalments (nos. 699+); identify Ahmad Ramzi Bey (cf. his 1948-49 al-Risala series on Libya and Mamluk-era history)"),
]

bad = [r["id"] for r in R if norm(r["q"]) not in bank(r["h"])]
if bad:
    sys.exit("quote not found in source bank: %s" % bad)
for r in R:
    assert len(r['saw'].split()) <= 25, (r['id'], len(r['saw'].split()))
    r["u"] = url(r["page"])

with open(os.path.join(STATE, "gazes_risala.jsonl"), "w", encoding="utf-8") as f:
    for r in R:
        rec = {"id": r["id"], "voice": r["voice"], "voice_type": "person", "role": r["role"],
               "country": r["c"], "country_now": r["cn"], "domain": r["dom"], "date": r["date"], "era": r["era"],
               "mirror": r["mirror"], "polarity": r["pol"], "intensity": r["inten"], "what_they_saw": r["saw"],
               "quote": r["q"] + " [translation: " + r["tr"] + "]", "artifact": r["art"], "evidence": r["ev"], "mediated_by": None,
               "caveat": "Cited as %s, Wikisource page '%s'. %s" % (r["issue"], r["page"], r["cav"]),
               "node": NODE, "sources": [r["u"]]}
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")

with open(os.path.join(STATE, "ledger_risala.md"), "w", encoding="utf-8") as f:
    f.write("| Claim | Node | Status | Sources | Next step |\n|---|---|---|---|---|\n")
    for r in R:
        f.write("| %s (%s, %s): \"%s\" | %s | verified S (%s, ar.wikisource transcription) | %s | %s |\n" % (
            r["voice"], r["role"], r["date"], r["q"].replace("|", "/"), NODE, r["issue"], r["u"], r["nxt"]))

# ---- person notes (each voice appears once as a person except al-Zayyat, who exists)
seen = set()
for r in R:
    if r["link"] == Z or r["link"] in seen:
        continue
    seen.add(r["link"])
    rs = [x for x in R if x["link"] == r["link"]]
    srcs = "\n".join("- %s, '%s': %s" % (x["issue"], x["page"], x["u"]) for x in rs)
    person(r["link"], role=r["role"], nat="Egyptian" if r["cn"] == "Egypt" else "Syrian", life="",
           stance="%s (%s)" % (r["pol"], ", ".join(x["date"][:4] for x in rs)),
           tags=["writer", "egypt" if r["cn"] == "Egypt" else "syria", "verified", "arabic-primary", "al-risala"],
           body="""%s. Writing in *al-Risala* (Cairo): %s

See [[%s]].

## Sources
%s
""" % (r["role"], " ".join(x["saw"] for x in rs), NODE, srcs))

parts = []
for r in R:
    parts.append("""## %s — *al-Risala*, %s

*%s*

> %s
> (translation: %s)

%s See [[%s]].
""" % (r["voice"], r["issue"].replace("al-Risala ", ""), r["saw"], r["q"], r["tr"],
       "Wikisource page: " + r["page"] + ".", r["link"]))
body = """Ten pieces from the Cairo weekly *al-Risala* (founded 1933 by Ahmad Hasan al-Zayyat), read from the Arabic Wikisource transcription of each issue and quoted at one or two sentences. The weekly's writers are the Egyptian and Arab literary establishment of the 1930s-40s; several are hostile over the caliphate, the Latin alphabet or Hagia Sophia, a few admire the soldier-statesman. Religion and the caliphate are recorded in each author's own framing, not the vault's. See also [[Ahmad Hasan al-Zayyat]], [[Four Poems on Atatürk — Melbourne, Damascus, Cairo and Hyderabad, 1933–1939]], [[Abolition of the Caliphate]], [[Hat Law]].

%s
## Sources
%s
""" % ("\n".join(parts), "\n".join("- %s, '%s': %s" % (r["issue"], r["page"], r["u"]) for r in R))
note("Events", NODE, {"type": "event", "when": "1935–1946", "tags": ["event", "verified", "egypt", "arabic-primary", "al-risala"]}, body)
print("ok", len(R))
