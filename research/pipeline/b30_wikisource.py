# -*- coding: utf-8 -*-
# Census round 21 (Nov 2026) — Wikisource sweep in 30+ languages: Lototsky (uk), Iorga (ro), Nzhdeh x2 and Shant (hy),
# Annadurai (ta), McCabe, Hook, Banerjea, Du Bois (en), Kotko and Petriv (uk).
# Banks in tools/.state/round21/ (raw/rendered Wikisource text). The script refuses to run if a quote is not in its bank.
import json, os, re, sys, unicodedata, urllib.parse
from _lib import note, person

HERE = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(HERE, "tools", ".state", "round21")
NODE = "Wikisource Pens on Mustafa Kemal — Lototsky, Iorga, Nzhdeh, Shant, Annadurai and Others"


def norm(s):
    s = unicodedata.normalize("NFKC", s)
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"').replace("«", '"').replace("»", '"')
    s = re.sub(r"\s+", " ", s)
    s = re.sub(r"\s+([,.;:?!])", r"\1", s)
    return s.strip().lower()


def bank(f):
    return norm(open(os.path.join(STATE, f), encoding="utf-8").read())


def ws(lang, title):
    return "https://%s.wikisource.org/wiki/%s" % (lang, urllib.parse.quote(title.replace(" ", "_"), safe="/_():,-"))


R = [
 dict(id="lototsky-1966", voice="Oleksandr Lototsky", role="Ukrainian People's Republic envoy to Constantinople (1919), minister, memoirist",
      c="Ukrainian People's Republic (émigré)", cn="Ukraine", dom="diplomacy", date="1966", era="posthumous", mirror="modernization-poster-child",
      pol="admiring", inten=2, art="memoir", ev="S", f="p_uk_5606fb.txt",
      saw="Calls the 'rebel general' Mustafa Kemal gifted in military, political, social and cultural fields, who raised Turkish national feeling and renewed the people's psyche.",
      qs=[("Ставши на чолі визвольного руху, він здолав піднести національне почуття турецького народу до найвищого ступня.",
           "Having put himself at the head of the liberation movement, he managed to raise the national feeling of the Turkish people to its highest degree."),
          ("Той характер Кемалевого діла оновив психіку народу, оспалого за дотеперішніх політичних та культурних умовин, і подвигнув той народ до великого самосвідомого чину.",
           "That character of Kemal's work renewed the psyche of a people drowsy under the former political and cultural conditions and moved that people to a great self-conscious deed.")],
      src=ws("uk", "Сторінки минулого (1966)/4/Внутрішнє положення в Туреччині по замиренні"),
      cav="Wikisource transcription (proofread level 3) of O. Lototsky, Сторінки минулого, Part 4 'В Царгороді' (1966), chapter 'Внутрішнє положення в Туреччині по замиренні', scan pages 24-27 of the linked djvu; the page does not give the composition date. The passage uses the name 'Ататюрк', so it was written after 1934, and the author died in 1939 (his death date is from memory, tier M): the text was probably written 1934-39 and published posthumously in 1966. A second passage in the chapter 'По війні та мировій конференції' quotes Kemal's Ankara speech that Turkey became 'the only victor among the vanquished'. Scan not viewed. Translation is the vault's own."),
 dict(id="iorga-1938-10", voice="Nicolae Iorga", role="Romanian historian, former prime minister, university professor",
      c="Romania", cn="Romania", dom="politics", date="1938-10-31", era="contemporary", mirror="nation-forge-template",
      pol="admiring", inten=1, art="speech", ev="S", f="p_ro_ce0954.txt",
      saw="Cites the Turks' grief when Atatürk fell ill as proof that a nation can concentrate in one man who restored the Empire's glory.",
      qs=[("Cînd s'a îmbolnăvit în urmă d. Atatürk, ce adînc sentiment de îngrijorare, de durere a fost în sufletul tuturor Turcilor: pare că ar fi crezut că dispariția aceluia care a restabilit gloria de odinioară a Imperiului, devenit național acum, ar însemna prăbușirea patriei și dispariția națiunii din rîndul popoarelor care înseamnă ceva în lume.",
           "When Mr Atatürk recently fell ill, what a deep feeling of worry and grief there was in the soul of all the Turks: it seems they believed that the disappearance of the man who restored the former glory of the Empire, now become national, would mean the collapse of the homeland and the disappearance of the nation from among the peoples that mean something in the world.")],
      src=ws("ro", "Ce înseamnă astăzi concepția istorică"),
      cav="Opening lecture at the University of Bucharest, 31 Oct 1938 (ten days before Atatürk's death); printed Vălenii-de-Munte, Datina Românească, 1939, extract from Revista Istorică, year XXV, nos. 1-3 (all stated on the Wikisource page). Iorga uses Atatürk as one example (with Hitler and Mussolini) in an argument that nations gather in one leader, and goes on to urge rallying round the Romanian king: the praise serves that argument. Wikisource transcription of the printed pamphlet; scan not viewed. Translation is the vault's own."),
 dict(id="nzhdeh-1932", voice="Garegin Nzhdeh", role="Armenian military commander (Zangezur 1921), political thinker, exile in Bulgaria",
      c="Armenia (émigré in Bulgaria)", cn="Armenia", dom="military", date="1932", era="contemporary", mirror=None,
      pol="hostile", inten=1, art="article", ev="S", f="p_hy_432518.txt",
      saw="Pictures Kemal as drunk with a lucky, accidental victory, his hand bloody, eyeing the Ararat plain from the Araxes and dreaming of ruining it.",
      qs=[("երբ Քեմալը՝ բախտահաս պատահական յաղթութեամբ գինով, իր արնոտ ձեռքը ագռաւի թեւերին իջեցրած՝ Արաքսի ափէն իր պղտոր հայեացքով Արարատեան դաշտն է չափում, զայն մի օր սեւ հողերի վերածելու երազով.",
           "when Kemal, drunk with a lucky accidental victory, his bloody hand lowered on the raven's wings, measures the Ararat plain from the bank of the Araxes with his murky gaze, dreaming of one day turning it into black earth.")],
      src=ws("hy", "Ցեղի ոգու շարժը"),
      cav="'Ցեղի ոգու շարժը' ('The movement of the race's spirit'); the Wikisource header and footnote say it was printed in Sofia in 1932. Sensitive thread (Armenian genocide memory): recorded as Nzhdeh's own rhetoric in a polemical essay, not as the vault's description of Kemal. Translation (including the figurative 'raven's wings') is the vault's own; check with an Armenian reader. Scan not viewed."),
 dict(id="nzhdeh-1937", voice="Garegin Nzhdeh", role="Armenian military commander (Zangezur 1921), political thinker, exile in Bulgaria",
      c="Armenia (émigré in Bulgaria)", cn="Armenia", dom="military", date="1937", era="contemporary", mirror=None,
      pol="hostile", inten=2, art="article", ev="S", f="p_hy_2c3fcc.txt",
      saw="Argues the Bolsheviks, not Kemal, saved Turkey: the Turkish-Soviet alliance, he says, let the 'grey wolf' prevail; calls him 'lucky'.",
      qs=[("Բոլշեւի՚զմը փրկեց Թուրքիան եւ ո՛չ թէ բախտահաս Քեմալը:",
           "Bolshevism saved Turkey, and not the lucky Kemal.")],
      src=ws("hy", "Իմ պատասխանը"),
      cav="'Իմ պատասխանը' ('My answer'), subtitled 'Armenia's tragedy in the light of Turko-Bolshevik documents'; the Wikisource header and footnote say it was printed in Sofia in 1937. Sensitive thread (Armenian genocide memory, Zangezur/Soviet policy): Nzhdeh's own polemic. The essay also quotes Zinoviev ('the Soviet government helps Kemal') and Soviet witnesses to the Lenin-Kemal alliance. Translation is the vault's own. Scan not viewed."),
 dict(id="shant-1925", voice="Levon Shant", role="Armenian playwright, Dashnak leader and educator",
      c="Armenia (émigré)", cn="Armenia", dom="letters", date="1925", era="contemporary", mirror=None,
      pol="hostile", inten=1, art="book", ev="S", f="p_hy_a76db6.txt",
      saw="Reads the Kemalists as the new Westernised Turks, successors of the Ittihadists, expecting them to return under another name when envy topples Kemal.",
      qs=[("Այսինքն` հին թուրքեր եւ նոր թուրքեր, վերջիններս երէկ Իթթիհատական կը կոչուէին, այսօր քեմալական, վաղը նոր անունով մը պիտի իջնեն ասպարէզ, երբ խմբական նախանձը Քեմալին ալ տապալէ:",
           "That is, old Turks and new Turks; the latter were called Ittihadists yesterday, are Kemalists today, and tomorrow will enter the arena under a new name, when factional envy topples Kemal too.")],
      src=ws("hy", "Մեր անկախութիւնը"),
      cav="'Մեր անկախութիւնը' ('Our independence'); the Wikisource header gives the year 1925. Sensitive thread (Armenian genocide memory): Shant's political analysis, in which the Kemalist events are listed after the 'Armenian massacres' as fruits of the Ittihadist mood. Polarity read from the passage as a whole (sceptical continuity thesis), not from an explicit insult. Translation is the vault's own. Scan not viewed."),
 dict(id="annadurai-1960", voice="C. N. Annadurai", role="Dravidian movement leader, later Chief Minister of Madras State (1967-69)",
      c="India", cn="India", dom="politics", date="1960", era="posthumous", mirror="nation-forge-template",
      pol="admiring", inten=1, art="article", ev="S", f="p_ta_e9f79f.txt",
      saw="Writing on Menderes's fall, calls Mustafa Kemal 'praised by the world' and the creator of a new Turkey of renaissance and freedom.",
      qs=[("குவலயம் புகழப் பணியாற்றிய முஸ்தபா கமால், சமைத்தளித்த புதிய துருக்கியில் எழுச்சி, மறுமலர்ச்சி, விடுதலை உணர்ச்சி பூத்திடச் செய்திடும் ஆற்றலையும் பெற்றிருந்தவர்தான், மெண்டாரிஸ்.",
           "Menderes was one who also had the power to make revival, renaissance and the feeling of freedom bloom in the new Turkey that Mustafa Kamal, who had served to the praise of the whole world, had prepared and handed over.")],
      src=ws("ta", "தம்பிக்கு அண்ணாவின் கடிதங்கள் 04, தமிழ் அரசிப் பதிப்பகம், 2003/002"),
      cav="Letter 105 ('பெரிய புள்ளிகள்') of 'தம்பிக்கு அண்ணாவின் கடிதங்கள்' vol. 4 (Tamil Arasi Pathippagam, 2003 edition, as transcribed on ta.wikisource). The page gives no date: the letter discusses the army's seizure of Menderes (the Turkish coup of 27 May 1960), so it dates from mid-1960 (an inference). Passing praise inside an essay about Menderes; letter 106 (page /003) calls Menderes's rise a 'holy war' under 'Kamal Pasha'. Translation is the vault's own. Scan not viewed."),
 dict(id="mccabe-1945", voice="Joseph McCabe", role="British rationalist author and former priest",
      c="United Kingdom", cn="United Kingdom", dom="letters", date="1945", era="posthumous", mirror="secular-rationalist-prophet",
      pol="admiring", inten=2, art="book", ev="S", f="p_en_e2573e.txt",
      saw="Lists Atatürk among the freethinkers: he humanised and modernised Turkey with great vigour and won the title for his 'wonderful work'.",
      qs=[("He humanized and modernized Turkey with great vigor.", None),
          ("They gave him the name Ataturk (the Great Turk) for his wonderful work.", None)],
      src=ws("en", "A Biographical Dictionary of Ancient, Medieval, and Modern Freethinkers"),
      cav="Entry 'Ataturk, President Mustafa Kamal (1881-1938)' in McCabe's A Biographical Dictionary of Ancient, Medieval, and Modern Freethinkers (1945, year stated in the Wikisource header). McCabe also cites Armstrong's Grey Wolf for Atatürk's 'profound contempt for all religion' and adds that he was 'forced to compromise'; the praise is McCabe's own. Whole-page raw wikitext, no scan viewed."),
 dict(id="hook-1943", voice="Sidney Hook", role="American philosopher",
      c="United States", cn="United States", dom="letters", date="1943", era="posthumous", mirror=None,
      pol="hostile", inten=1, art="book", ev="S", f="p_en_39a5a6.txt",
      saw="Lists Atatürk among the 'midget followers' of the dictators' pattern who buried their monarchs.",
      qs=[("A century later, Lenin, Trotsky, Mussolini, Hitler, Ataturk, Metaxas, and other midget followers of the pattern set by the dictators either buried their monarchs or converted the seed of “the most superior” family in the world into paltry retainers.", None)],
      src=ws("en", "The Hero in History/Chapter 3"),
      cav="The Hero in History (John Day, 1943), chapter 3, Wikisource transcription of the scanned book (Page:The Hero in History.djvu/37). A one-clause mention inside a refutation of Wood's gametic theory of monarchy; 'midget' (polarity hostile) is read as a dismissal of the dictators as a type, with Atatürk named among them. Hook does not discuss Atatürk elsewhere in the chapter. Year 1943 from the work's first edition, from memory (tier M); the Wikisource text carries no date. Scan not viewed."),
 dict(id="banerjea-1925", voice="Surendranath Banerjea", role="Indian moderate nationalist, former Bengal minister",
      c="British India", cn="India", dom="politics", date="1925", era="contemporary", mirror="anti-colonial-liberator",
      pol="instrumental", inten=1, art="memoir", ev="S", f="p_en_3ebfe1.txt",
      saw="Credits the Khilafat settlement partly to the 'military triumphs of Kemal Pasha' reinforcing Indian opinion.",
      qs=[("This has now, to a great extent, been achieved, thanks to the insistence of the Government of India backed by public opinion in India and reinforced by the military triumphs of Kemal Pasha.", None)],
      src=ws("en", "A Nation in Making/Chapter 31"),
      cav="A Nation in Making (Oxford, 1925), chapter 31, Wikisource transcription of the scanned book (Page:A Nation in Making.djvu/314, printed page 298 onward). Banerjea writes of presiding over a Muslim meeting on the Khilafat question in 1919 and judges the Sevres revision a victory partly of Kemal's army; no personal assessment of Kemal. Scan not viewed."),
 dict(id="dubois-1928", voice="W. E. B. Du Bois", role="American sociologist, civil rights leader and novelist",
      c="United States", cn="United States", dom="letters", date="1928", era="contemporary", mirror="anti-colonial-liberator",
      pol="admiring", inten=1, art="book", ev="S", f="p_en_60caa1.txt",
      saw="In his novel, the Indian conspirator Kautilya reports having 'sat at the feet of Kemal' in Angora to learn his plans for the darker world.",
      qs=[("There I sat at the feet of Kemal and heard his plans.", None)],
      src=ws("en", "Dark Princess/Part 4"),
      cav="Dark Princess: A Romance (1928), Part IV, spoken by the character Kautilya, a fictional Indian traveller who lists Moscow, Constantinople and Angora on a journey of the darker races. A character's speech in fiction, not Du Bois in his own voice; but the author sends the figure to Kemal as a teacher among the world's leaders, and Du Bois's own non-fiction on Kemal has not been sourced in the vault. Year of publication from memory (tier M); the Wikisource page gives the story time '1926, April - April, 1927'."),
 dict(id="kotko-1930", voice="Kost Kotko", role="Soviet Ukrainian journalist and travel writer",
      c="Soviet Union (Ukrainian SSR)", cn="Ukraine", dom="letters", date="1930", era="contemporary", mirror="bourgeois-revolutionary",
      pol="conflicted", inten=2, art="book", ev="S", f="p_uk_7d53ea.txt",
      saw="Sees a national revolution made by peasants who got little, and asks whether Kemal will put a capitalist 'hat' on his constitution.",
      qs=[("Молодотурки, завівши конституцію, нап'яли на неї, за одним фігуральним виразом, чалму. Чи напне на власну конституцію Кемаль капелюха всеевропейського капіталістичного зразка?",
           "The Young Turks, having introduced a constitution, put a turban on it, in one figurative expression. Will Kemal put on his own constitution a hat of the all-European capitalist pattern?")],
      src=ws("uk", "Щоденник кількох міст/Через Анатолію"),
      cav="Кость Котко, Щоденник кількох міст (Kharkiv: Knyhospilka, 1930), chapter 'Через Анатолію'; Wikisource transcription of the scanned book. The same chapter says the Turkish peasant made the national revolution and 'received nothing for it' apart from the abolition of the ashar, a verdict on Kemalism rather than on the man; in the chapter 'В історичні дні Туреччини' he reports Kemal's order to halve the time for the new alphabet. Soviet-line travel journalism of 1930. Translation is the vault's own. Scan not viewed."),
 dict(id="petriv-1924", voice="Vsevolod Petriv", role="General of the Ukrainian People's Republic army, military author",
      c="Ukrainian People's Republic (émigré)", cn="Ukraine", dom="military", date="1924", era="contemporary", mirror="nation-forge-template",
      pol="admiring", inten=1, art="book", ev="S", f="p_uk_a06d83.txt",
      saw="Names Kemal's army among the 'strong and mighty' armies of the age, praised for its march across all of Asia like Xenophon's Ten Thousand.",
      qs=[("Далі — міцна й могутня армія Кемаля, що дала чудовий приклад мандрівки через цілу Азію, як ті десять тисяч Греків Ксенофонта", "Next, the strong and mighty army of Kemal, which gave a splendid example of a march across the whole of Asia, like those ten thousand Greeks of Xenophon")],
      src=ws("uk", "Суспільство й військо (1924)"),
      cav="Всеволод Петрів, Суспільство й військо: соціально-історичний нарис (Prague-Berlin: Нова Україна, 1924), Wikisource transcription. A one-clause example in a study of mass armies; Petriv gives no wider verdict on Kemal. Translation is the vault's own. Scan not viewed."),
]

bad = []
for r in R:
    b = bank(r["f"])
    for q, _ in r["qs"]:
        if norm(q) not in b:
            bad.append((r["id"], q[:50]))
if bad:
    sys.exit("quote not found in source bank: %s" % bad)

ENUM_POL = {"admiring", "hostile", "conflicted", "instrumental", "witness"}
out = os.path.join(STATE, "gazes_wikisource.jsonl")
with open(out, "w", encoding="utf-8") as f:
    for r in R:
        assert r["pol"] in ENUM_POL and len(r["saw"].split()) <= 25, (r["id"], len(r["saw"].split()))
        parts = []
        for q, tr in r["qs"]:
            parts.append(q if tr is None else q + " [translation: " + tr + "]")
        rec = {"id": r["id"], "voice": r["voice"], "voice_type": "person", "role": r["role"],
               "country": r["c"], "country_now": r["cn"], "domain": r["dom"], "date": r["date"], "era": r["era"],
               "mirror": r["mirror"], "polarity": r["pol"], "intensity": r["inten"], "what_they_saw": r["saw"],
               "quote": " … ".join(parts), "artifact": r["art"], "evidence": r["ev"],
               "mediated_by": None, "caveat": r["cav"], "node": NODE, "sources": [r["src"]]}
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
        print(r["id"], len(r["saw"].split()))

with open(os.path.join(STATE, "ledger_wikisource.md"), "w", encoding="utf-8") as f:
    f.write("| Claim | Node | Status | Sources | Next step |\n|---|---|---|---|---|\n")
    for r in R:
        f.write("| %s (%s): %s | %s | verified S (Wikisource text read) | %s | View the linked scan for the exact printed page |\n"
                % (r["voice"], r["date"], r["saw"], NODE, r["src"]))

P = {r["id"]: r for r in R}


def pn(name, rid, role, nat, life, stance, tags, text):
    r = P[rid]
    person(name, role=role, nat=nat, life=life, stance=stance, tags=tags,
           body="%s\n\nSee [[%s]].\n\n## Sources\n- %s\n" % (text, NODE, r["src"]))


pn("Oleksandr Lototsky", "lototsky-1966", "Ukrainian statesman, UNR envoy to Constantinople, memoirist", "Ukrainian", "1870–1939",
   "admiring (memoir, 1966)", ["diplomat", "ukraine", "verified"],
   "Headed the Ukrainian People's Republic's embassy to Constantinople in 1919. His memoir *Сторінки минулого*, part 4 'В Царгороді' (published 1966), calls the 'rebel general' Mustafa Kemal gifted in every field and credits him with raising Turkish national feeling and renewing the people's psyche.")
pn("Nicolae Iorga", "iorga-1938-10", "Romanian historian and former prime minister", "Romanian", "1871–1940",
   "admiring (31 Oct 1938)", ["historian", "romania", "verified"],
   "In his opening lecture of 31 October 1938 at the University of Bucharest, Iorga cites the Turks' grief at Atatürk's illness as the example of a nation concentrated in one leader, the man who 'restored the former glory of the Empire, now national'; the example serves his plea to rally round the king.")
pn("Garegin Nzhdeh", "nzhdeh-1932", "Armenian military commander and political thinker", "Armenian", "1886–1955",
   "hostile (1932, 1937)", ["soldier", "armenia", "verified"],
   "Armenian commander of Zangezur in 1921, later an exile in Bulgaria. Two Sofia-printed polemics are on Wikisource: in 1932 Kemal is drunk on a lucky victory and eyes Ararat; in 1937 Nzhdeh argues that 'Bolshevism saved Turkey, and not the lucky Kemal'. Sensitive thread (Armenian genocide memory): his words, not the vault's framing.")
pn("Levon Shant", "shant-1925", "Armenian playwright and Dashnak leader", "Armenian", "1869–1951",
   "hostile (1925)", ["writer", "armenia", "verified"],
   "In 'Our independence' (1925) he reads the Kemalists as the new, Western-varnished Turks, the Ittihadists of yesterday, who will return under another name when factional envy topples Kemal. Sensitive thread (Armenian genocide memory).")
pn("C. N. Annadurai", "annadurai-1960", "Dravidian leader, Chief Minister of Madras State 1967–69", "Indian (Tamil)", "1909–1969",
   "admiring (1960)", ["politician", "india", "verified"],
   "In a 1960 weekly letter to his 'thambi' (younger brother) on the Turkish coup against Menderes, he calls Mustafa Kemal one who 'served to the praise of the whole world' and built the new Turkey of revival and freedom. Compare [[Periyar E. V. Ramasamy]].")
pn("Joseph McCabe", "mccabe-1945", "British rationalist author, former priest", "British", "1867–1955",
   "admiring (1945)", ["writer", "united-kingdom", "verified"],
   "His 1945 Biographical Dictionary of Freethinkers lists 'Ataturk, President Mustafa Kamal', who 'humanized and modernized Turkey with great vigor' and got his title 'for his wonderful work', while noting (after Armstrong) his contempt for religion.")
pn("Sidney Hook", "hook-1943", "American philosopher", "American", "1902–1989",
   "hostile (1943 aside)", ["philosopher", "united-states", "verified"],
   "In *The Hero in History* (1943) Atatürk appears once, among the 'midget followers of the pattern set by the dictators' who buried their monarchs.")
pn("Surendranath Banerjea", "banerjea-1925", "Indian moderate nationalist, former Bengal minister", "Indian", "1848–1925",
   "instrumental (1925)", ["politician", "india", "verified"],
   "In his memoir *A Nation in Making* (1925) he treats the revision of the Sèvres settlement, which he had championed at a Muslim meeting in London in 1919, as helped by 'the military triumphs of Kemal Pasha'.")
pn("Kost Kotko", "kotko-1930", "Soviet Ukrainian journalist and travel writer", "Ukrainian (Soviet)", "",
   "conflicted (1930)", ["writer", "ukraine", "verified"],
   "His travel diary *Щоденник кількох міст* (Kharkiv, 1930) reads Kemalism through Marxist eyes: a national revolution made by the peasant, who got only the end of the tithe, and the question whether Kemal will fit his constitution with a capitalist hat.")
pn("Vsevolod Petriv", "petriv-1924", "General of the Ukrainian People's Republic army", "Ukrainian", "1883–1948",
   "admiring (1924 aside)", ["soldier", "ukraine", "verified"],
   "In *Суспільство й військо* (Prague-Berlin, 1924) he lists 'the strong and mighty army of Kemal' with the Galician and Czech armies as models of cohesion, for its march across all of Asia.")

QB = lambda r, i=0: "> %s\n> (translation: %s)\n" % (r["qs"][i][0], r["qs"][i][1]) if r["qs"][i][1] else "> %s\n" % r["qs"][i][0]
body = """Texts in Wikisource editions in five languages (Ukrainian, Romanian, Armenian, Tamil, English), found by a keyword sweep of 30+ Wikisource languages for Kemal and Atatürk. Wikisource transcriptions, tier S; none of the linked scans was viewed. Kemal and Atatürk were not found in a usable named text in the Swedish, Danish, Norwegian, Dutch, Finnish, Estonian, Lithuanian, Hebrew and Georgian Wikisources (see the candidates file).

## Ukrainian — Lototsky (memoir, published 1966), Kotko (1930), Petriv (1924)

[[Oleksandr Lototsky]], the Ukrainian People's Republic's envoy in Constantinople, remembers Kemal as the gifted 'rebel general':

%s
[[Kost Kotko]], a Soviet Ukrainian travel writer, 1930:

%s
[[Vsevolod Petriv]], a UNR general, 1924: 'the strong and mighty army of Kemal' as a model of an army that held together.

## Romanian — Nicolae Iorga, 31 October 1938

[[Nicolae Iorga]], opening lecture, University of Bucharest:

%s
## Armenian — Nzhdeh (1932, 1937) and Shant (1925)

Sensitive thread (Armenian genocide memory); each is the author's own polemic.

[[Garegin Nzhdeh]], 1932:

%s
Nzhdeh, 1937: *Bolshevism saved Turkey, and not the lucky Kemal.* (translation)

[[Levon Shant]], 1925:

%s
## Tamil — C. N. Annadurai, 1960

[[C. N. Annadurai]], letter 105 to his 'thambi':

%s
## English — McCabe (1945), Hook (1943), Banerjea (1925), Du Bois (1928)

[[Joseph McCabe]]: *He humanized and modernized Turkey with great vigor.* [[Sidney Hook]]: Atatürk among the 'midget followers of the pattern set by the dictators'. [[Surendranath Banerjea]]: the Khilafat settlement 'reinforced by the military triumphs of Kemal Pasha'. [[W.E.B. Du Bois]], in the novel *Dark Princess*, has a character say 'There I sat at the feet of Kemal and heard his plans' (fiction, a character's speech).

## Sources
%s""" % (QB(P["lototsky-1966"]) + QB(P["lototsky-1966"], 1), QB(P["kotko-1930"]), QB(P["iorga-1938-10"]), QB(P["nzhdeh-1932"]), QB(P["shant-1925"]), QB(P["annadurai-1960"]),
         "\n".join("- %s (%s): %s" % (r["voice"], r["date"], r["src"]) for r in R))
note("Events", NODE, {"type": "event", "when": "1924–1966", "tags": ["event", "verified", "wikisource"]}, body)
print("ok")
