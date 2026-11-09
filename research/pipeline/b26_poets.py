# -*- coding: utf-8 -*-
# Census round 17 (Nov 2026) — poets, reformers and the black press, in their own words.
# Records: Kazi Nazrul Islam ("Kamal Pasha", Agni-Veena 1922), Ma'ruf al-Rusafi (ode, Diwan), Mustafa al-Ghalayini
# (Diwan, Haifa 1924/25), Huda Sha'arawi (Istanbul, April 1935), Marcus Garvey (Negro World, 23 Sep 1922),
# The Negro World (front-page editorial, 7 May 1927), Elisaveta Bagryana ("Nova Atlantida", dedicated to Kemal Ataturk).
# Windows of every text are banked in tools/.state/round17/; the script refuses to run if a quote is not in its bank.
import json, os, re, sys, unicodedata
from _lib import note, person

HERE = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(HERE, "tools", ".state", "round17")
NODE = "Poets, Reformers and the Black Press on Atatürk, 1921–1935"


def norm(s):
    s = unicodedata.normalize("NFKC", s)
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"').replace("­", "")
    s = re.sub(r"[ً-ٟـ]", "", s)               # Arabic diacritics, tatweel
    s = re.sub("[أإآٱ]", "ا", s).replace("ى", "ي").replace("ة", "ه")
    s = re.sub(r"[«»()\[\]]", " ", s)
    s = re.sub(r"[-¬]\s*\n", "", s)
    s = re.sub(r"\s+", " ", s)
    return s.strip().lower()


def bank(n):
    return norm(open(os.path.join(STATE, n), encoding="utf-8", errors="ignore").read())


NZ = "https://briqjournal.com/sites/default/files/yazi-ici-dosyalar/2023-09/C4S4_MohammadBas%C4%B1rUlHaqSinha_ENG.pdf"
NZ2 = "https://dunyadaataturk.com/dunya-sairlerinden-ataturk-siirleri"
NZ3 = "https://defencehub.live/threads/kamal-pasha-poem-by-kazi-nazrul-islam-the-national-poet-of-bangladesh.2261"
RUS = "https://dergipark.org.tr/en/download/article-file/786363"
GAL = "https://dergipark.org.tr/tr/download/article-file/1525913"
HUD = "https://archive.org/details/06.0_20210520_20210520_1158"
HUD2 = "https://read.dukeupress.edu/jmews/article/4/1/31/42971/Staging-Turkish-Women-s-EmancipationIstanbul-1935"
NW22 = "https://dangerouspress.org/papers/negro-world/1922-09-23"
NW27 = "https://dangerouspress.org/papers/negro-world/1927-05-07"
BAG = "https://litclub.bg/library/bg/bagryana/140.htm"
BAG2 = "https://chitanka.info/text/11753-nova-atlantida"

R = [
 dict(id="nazrul-1922", voice="Kazi Nazrul Islam", role="Bengali poet (later national poet of Bangladesh)", c="British India (Bengal)",
      cn="Bangladesh", dom="letters", date="1922", era="contemporary", mirror="anti-colonial-liberator", pol="admiring", inten=3,
      saw="Hails Kemal as the fighter whose sharpened sword sent the enemy to Hades, with the refrain 'Kamal, you have worked a wonder, brother'.",
      q="Kamal Tu Ne Kamal Kiya Bhai", src="nz0.txt", art="poem", ev="J", med=None,
      cav="The Bengali-script text was not retrieved (bn.wikisource does not hold Agni-Veena's 'Kamal Pasha'); the refrain is quoted in Latin transliteration by the peer-reviewed BRIQ article (p. 74) with the translation '(Kamal, you have achieved unbelievable success, brother!)' (TRANSLATION, by the article). Poem 'Kamal Pasha' in Agni-Veena (Calcutta, Kartik 1329 = Oct 1922; composed c. Aug-Sep 1921 according to BRIQ, 'as far as it is known'). Full English rendering ('Brother Kemal, the desperate son of a frenzied mother ... Bravo to your sharpened sword ... Tell me now, who is there on earth not afraid of Turkish sword?') on a forum (defencehub, translator unnamed); a Turkish translation of the poem (from Nurul Huda's English, 1997/1999) is printed in 'Dünya Şairlerinden Atatürk Şiirleri' with a reference to Kemal Özcan Davaz, 'Atatürk, Bangladeş, Kazi Nazrul İslam' (Atatürk Araştırma Merkezi, 2000, pp. 79-97). The poem also names Anwar Pasha (Enver), so it is not a pure Kemalist text; BRIQ reads Nazrul as folding Kemal into pan-Islamic 'Ummah' loyalty. Kemal is the poem's subject, so it counts.",
      urls=[NZ, NZ2, NZ3],
      loc="Agni-Veena (1922), 'Kamal Pasha'; refrain as cited in Sinha, BRIQ 4(4), 2023, p. 74", link="Kazi Nazrul Islam"),
 dict(id="rusafi-1923", voice="Ma'ruf al-Rusafi", role="Iraqi poet, teacher and MP", c="Iraq (British mandate)", cn="Iraq",
      dom="letters", date="1923", era="contemporary", mirror="anti-colonial-liberator", pol="admiring", inten=2,
      saw="Addresses Kemal as 'hero of the Greater East' whose victory over the Greeks threw the West into confusion and lit a new Eastern sun.",
      q="نصرت على بني يونان نصرا أقام الغرب في هرج ومرج", src="ed.txt", art="poem", ev="S", med=None,
      cav="TRANSLATION (this record's): 'You defeated the sons of Yunan with a victory that left the West in tumult and confusion.' Ode 'Ila batal al-sharq al-akbar' ('To the hero of the greater East', 'Büyük Doğu'nun Kahramanına'), whose opening verse puns on 'Mustafa' and 'Kemal'; printed in Diwan al-Rusafi (4th ed., Cairo: I'timad, 1953), p. 440, which in Mustafa Saka's edition carries the heading 'said after Gazi Mustafa Kemal's victory over the Greeks in 1923' (Al-Chalaby, n. 10). Al-Chalaby judges 1923 a possible misprint for 1922 (or the poem postdates Lausanne or the Republic). Arabic text as printed in Al-Chalaby 2019, RumeliDE Dil ve Edebiyat Araştırmaları Dergisi, Ö5, pp. 176-186, and in the compilation 'Dünya Şairlerinden Atatürk Şiirleri' (no. 46). The ode also calls Kemal a Jesus-like healer of the nation and says he saved the girls of Izmir from 'the hands of every lout'; Al-Chalaby adds that 'many Arab poets ignored' the victories. Not to be confused with Rusafi's Turkish-language work; the poem is in classical Arabic.",
      urls=[RUS, NZ2],
      loc="Diwan al-Rusafi (Cairo, 1953), p. 440, as printed in Al-Chalaby, RumeliDE 2019, pp. 176-186", link="Ma'ruf al-Rusafi"),
 dict(id="ghalayini-1924", voice="Mustafa al-Ghalayini", role="Lebanese scholar, grammarian and poet", c="Lebanon (French mandate)",
      cn="Lebanon", dom="letters", date="1924", era="contemporary", mirror="anti-colonial-liberator", pol="admiring", inten=2,
      saw="Holds up Mustafa Kemal and his comrades as the model the Arabs lack, a commander who gathered a broken nation and broke its chains.",
      q="Ey Araplar! İçinizde mücadele ateşini tutuşturacak bir Mustafa Kemal yok mu?", src="f3ffe8.txt", art="poem", ev="S", med=None,
      cav="TRANSLATION ONLY, and a translation of a translation: the quoted line is Ali Benli's Turkish rendering (darulfunun ilahiyat 32/1, 2021, p. 29; Divan n. 74, p. 83) of al-Ghalayini's Arabic; the Arabic verse was not retrieved. Rendered: 'O Arabs! Is there not among you a Mustafa Kemal to kindle the fire of struggle?' Poem in Dîvânu'l-Galâyînî (Haifa: al-Matba'a al-'Abbasiyya, 1924/1925; Benli gives both years), pp. 80-83, written after his imprisonment by the French. Date 1924 is the Diwan's latest possible date, so the poem was written at the latest by then; the exact year was not established.",
      urls=[GAL],
      loc="Dîvânu'l-Galâyînî (Haifa, 1924/25), pp. 80-83, as translated in Benli, darulfunun ilahiyat 32/1 (2021), pp. 28-29", link="Mustafa al-Ghalayini"),
 dict(id="sharawi-1935", voice="Huda Sha'arawi", role="Egyptian feminist, president of the Egyptian Feminist Union", c="Egypt", cn="Egypt",
      dom="politics", date="1935-04", era="contemporary", mirror="emancipator-patriarch", pol="admiring", inten=2,
      saw="At the Istanbul women's congress she tells Atatürk that 'Father of the Turks' is not enough: for the East he is 'Atasharq'.",
      q="فأنا أقول إن هذا لا يكفي بل أنت بالنسبة لنا أتاشرق", src="hs_muq.txt", art="memoir", ev="J", med="Muqaddam, 'Awdat al-hijab (Islamist critique) quoting Sha'arawi's memoirs",
      cav="TRANSLATION (this record's): 'I say that this is not enough: for us you are Atasharq [Father of the East].' Arabic as quoted from her memoirs (Mudhakkirat) by Muhammad Ahmad Isma'il al-Muqaddam, 'Awdat al-hijab, section on Huda Sha'arawi (archive.org 06.0_20210520_20210520_1158; OCR, hamza missing in 'anta'), who cites her memoirs and a Hawwa' article of 1980; he quotes her to condemn her. Not seen in the memoir itself (the Arabic Mudhakkirat Huda Sha'rawi, Dar al-Hilal 1981, is not open). Independent corroboration of the saying: Libal, 'Staging Turkish Women's Emancipation: Istanbul, 1935', JMEWS 4(1), 2008, n. 13 ('reportedly asserted ... Father of the East (Atasark)'). Her speech was in Turkish, without interpreter, at the reception given by Atatürk for the delegates of the 12th IAW congress.",
      urls=[HUD, HUD2],
      loc="Mudhakkirat Huda Sha'rawi as quoted in al-Muqaddam, 'Awdat al-hijab (Arabic OCR); Libal, JMEWS 4(1), 2008, n. 13", link="Huda Sha'arawi"),
 dict(id="garvey-1922", voice="Marcus Garvey", role="UNIA president and Pan-African leader", c="United States (Jamaican-born)", cn="United States",
      dom="politics", date="1922-09-23", era="contemporary", mirror="anti-colonial-liberator", pol="admiring", inten=2,
      saw="Calls Kemal 'the man of the hour' who will lay the foundation of a changed world, and rejects the 'barbarian' charge as British hypocrisy.",
      q="Mustapha Kemal has become the man to the hour, even as the Kaiser was in 1914.", src="nw_1922-09-23.txt", art="speech", ev="P", med=None,
      cav="Front page of The Negro World, vol. XIII no. 6, 23 Sept 1922 ('Marcus Garvey sends message to Negro peoples of the world on war crisis'), section 'Some Reflections on the Eastern Situation' (Dangerous Press OCR of the issue, page number not shown by the OCR; it is the front-page lead). He adds 'Kemal is going to lay the foundation for a changed world', and, on Smyrna, 'They tell us that Kemal is a barbarian ... because they burned Smyrna and killed so many people in Smyrna', answering that the British bombed natives in Africa. Smyrna is a contested thread: this is Garvey's framing of it, not the vault's. His purpose is to warn that Negroes will not fight Britain's war against the Turks (instrumental as well as admiring). Same speech: 'Kemal's teacher was one of the men who fought in the German war as a German general'.",
      urls=[NW22],
      loc="The Negro World, 23 Sept 1922, front page", link="Marcus Garvey"),
 dict(id="negro-world-1927", voice="The Negro World", role="UNIA weekly, New York (Garvey's organ)", c="United States", cn="United States",
      dom="press", date="1927-05-07", era="contemporary", mirror="anti-colonial-liberator", pol="admiring", inten=1,
      saw="Front-page editorial lists Kemal Pasha with Gandhi, Zaghlul, Sun Yat-sen and Chen as 'leaders of courage and vision' whom Africans lack.",
      q="leaders of courage and vision, uncompromising, upstanding men, real patriots", src="nw_1927-05-07.txt", art="editorial", ev="P", med=None,
      cav="Front page of The Negro World, 7 May 1927 (the OCR date reads '1827'), editorial 'What of Marcus Garvey, Negroes!', written while Garvey was in prison; Kemal is one name in a list ('Turkey its Kemal Pasha'), and the editorial's subject is Garvey. A page-one slogan in the same issue repeats 'Turkey her Kemal Pasha'. Dangerous Press OCR.",
      urls=[NW27],
      loc="The Negro World, 7 May 1927, front page", link="Marcus Garvey"),
 dict(id="bagryana-1973", voice="Elisaveta Bagryana", role="Bulgarian poet", c="Bulgaria", cn="Bulgaria",
      dom="letters", date="1973", era="posthumous", mirror="modernization-poster-child", pol="admiring", inten=2,
      saw="Dedicates 'New Atlantis' to Kemal Atatürk: Ankara reborn from the desert, legend turned into life forged with hammer and sledge.",
      q="Легендата става живот (да живее животът!), живот, изкован с млат и чук!", src="bag1.txt", art="poem", ev="P", med=None,
      cav="TRANSLATION (this record's): 'The legend becomes life (long live life!), life forged with hammer and sledge!' Poem 'Nova Atlantida', dedication 'На Кемал Ататюрк'. DATE NOT ESTABLISHED: the only dated printing found is Amazonka. Izbrana lirika v dva toma (Balgarski pisatel, Sofia, 1973), as given by chitanka.info; the surname Atatürk (adopted 1934) and the present tense ('two piercing eyes do not sleep') suggest composition 1934-1938, but that is inference only (tier M). If an earlier printing is found, re-date to the contemporary era. Turkish translation by Hüseyin Mevsim in 'Dünya Şairlerinden Atatürk Şiirleri' (no. 37).",
      urls=[BAG, BAG2, NZ2],
      loc="Elisaveta Bagryana, 'Nova Atlantida', in Amazonka (Sofia, 1973); text at litclub.bg/library/bg/bagryana/140.htm", link="Elisaveta Bagryana"),
]

# banks: ed.txt is the Rusafi Arabic as printed in the Al-Chalaby article text (ap0.txt)
SRC_ALIAS = {"ed.txt": "ap0.txt"}
bad = []
for r in R:
    full = bank(SRC_ALIAS.get(r["src"], r["src"]))
    q = norm(r["q"])
    if q not in full:
        bad.append(r["id"])
if bad:
    sys.exit("quote not found in source bank: %s" % bad)
for r in R:
    assert len(r["saw"].split()) <= 25, (r["id"], len(r["saw"].split()))

with open(os.path.join(STATE, "gazes_poets.jsonl"), "w", encoding="utf-8") as f:
    for r in R:
        rec = {"id": r["id"], "voice": r["voice"], "voice_type": "press" if r["dom"] == "press" else "person", "role": r["role"],
               "country": r["c"], "country_now": r["cn"], "domain": r["dom"], "date": r["date"], "era": r["era"],
               "mirror": r["mirror"], "polarity": r["pol"], "intensity": r["inten"], "what_they_saw": r["saw"],
               "quote": r["q"], "artifact": r["art"], "evidence": r["ev"], "mediated_by": r["med"], "caveat": r["cav"],
               "node": NODE, "sources": r["urls"]}
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")

nxt = {"nazrul-1922": "Bengali-script text of 'Kamal Pasha' (Nazrul Rachanabali, Bangla Academy vol. 1) and Davaz 2000 pp. 79-97; 'Anwar' and 'Ranabheri' for Enver/war context",
       "rusafi-1923": "Diwan al-Rusafi scan; Al-Chalaby is the translator-analyst, a second reading of 'Ila batal al-sharq al-akbar' with its publication date (Iraqi press 1922-23)",
       "ghalayini-1924": "Arabic original of the poem in Divan al-Ghalayini (Haifa, 1924/25, pp. 80-83); date it",
       "sharawi-1935": "Mudhakkirat Huda Sha'rawi (Dar al-Hilal 1981) page; Turkish and Egyptian press April 1935 (al-Muqattam, Cumhuriyet)",
       "garvey-1922": "Marcus Garvey Papers (Hill, ed.) vol. XI/XII for the same speech with a page; later Garvey on Kemal (Philosophy and Opinions, Blackman)",
       "negro-world-1927": "More Negro World leaders on Turkey (Oct-Nov 1923 Republic; March 1924 Caliphate); Dangerous Press has a per-issue search",
       "bagryana-1973": "Date the poem: Bagryana's 1930s Turkey journey or an early collection (Zvezda na moryaka, 1932?; M only)"}
with open(os.path.join(STATE, "ledger_poets.md"), "w", encoding="utf-8") as f:
    f.write("| Claim | Node | Status | Sources | Next step |\n|---|---|---|---|---|\n")
    for r in R:
        f.write("| %s (%s, %s): \"%s\" | %s | verified %s (%s) | %s | %s |\n" % (
            r["voice"], r["role"][:50], r["date"], r["q"][:110].replace("|", "/") + ("..." if len(r["q"]) > 110 else ""),
            NODE, r["ev"], r["loc"], "; ".join(r["urls"][:1]), nxt[r["id"]]))

person("Ma'ruf al-Rusafi", role="Iraqi poet, teacher, Ottoman and Iraqi MP", nat="Iraqi", life="1875–1945",
       stance="admiring in a classical ode", tags=["writer", "anti-colonial-liberator", "verified"],
       body="""Baghdad's best-known neoclassical poet, a former Ottoman deputy and teacher in Istanbul who returned to Iraq in 1921. His ode to the 'hero of the Greater East' (*Ila batal al-sharq al-akbar*), printed in his *Diwan* (Cairo, 1953, p. 440), names Mustafa Kemal in its first verse, says he beat the Greeks with a victory that left 'the West in tumult', and likens him to a Jesus healing the nation's cracks. Ahmet Farman Saeed Al-Chalaby (2019) notes that many Arab poets passed over the victories in silence. See [[%s]].

## Sources
- Al-Chalaby, A. F. S., 'Ma'ruf er-Rusafi'nin Mustafa Kemal Atatürk Hakkında yazdığı şiire bir bakış', *RumeliDE* Ö5 (2019), pp. 176-186: %s
""" % (NODE, RUS))

person("Mustafa al-Ghalayini", role="Lebanese scholar, grammarian and poet", nat="Lebanese", life="1886–1944",
       stance="admiring, as a model for the Arabs", tags=["writer", "anti-colonial-liberator", "verified"],
       body="""The author of *Jami' al-durus al-'arabiyya*, imprisoned by the French after 1920 and a supporter of Faisal. His *Diwan* (Haifa, 1924/25) contains a poem on the Anatolian struggle in which he shows Mustafa Kemal as the leader who gathered a divided people and broke its chains, then asks: 'O Arabs! Is there not among you a Mustafa Kemal?' (quoted in Turkish translation by Ali Benli, 2021). See [[%s]].

## Sources
- Ali Benli, 'Mustafa el-Galâyînî'nin Şiir Anlayışı ve Siyasi Şiirleri', *darulfunun ilahiyat* 32/1 (2021), pp. 1-34, esp. pp. 27-29: %s
""" % (NODE, GAL))

person("Elisaveta Bagryana", role="Bulgarian poet", nat="Bulgarian", life="",
       stance="admiring", tags=["writer", "modernization-poster-child", "verified"],
       body="""Bulgaria's best-known woman poet. Her poem *Nova Atlantida* (New Atlantis) is dedicated 'To Kemal Atatürk': Ankara, 'daughter and queen of the steppes', is a risen Atlantis, the old tales of Harun al-Rashid are dead, and the legend has become life forged with hammer and sledge. Its date is not established (see the record's caveat). See [[%s]].

## Sources
- Elisaveta Bagryana, 'Nova Atlantida' (litclub.bg): %s; Amazonka (Sofia, 1973) per %s
""" % (NODE, BAG, BAG2))

body = """
Round 17 asked where the poets, reformers and the black press of the colonised world stood on Kemal, in their own words.
Seven records came out solid; the rest of the target list is in the candidates files as dry ends. Most Arab poets
did not write about him: Al-Chalaby (2019) says 'many' ignored the victories.

## Kazi Nazrul Islam (1921-22), 'Kamal Pasha'

*%(nz)s*

> %(nzq)s  (refrain; translation by the BRIQ article: 'Kamal, you have achieved unbelievable success, brother!')

The poem in *Agni-Veena* (Oct 1922) greets the Turkish army's sword as vengeance for the colonised; a forum English
version has 'Bravo to your sharpened sword ... who is there on earth not afraid of Turkish sword?'. It also names
Anwar Pasha, and BRIQ reads Nazrul as folding Kemal into pan-Islamic loyalty. See [[Kazi Nazrul Islam]], [[Greco-Turkish War]].

## Ma'ruf al-Rusafi and Mustafa al-Ghalayini, two Arab odes

*%(ru)s*

> %(ruq)s
> (translation: 'You defeated the sons of Yunan with a victory that left the West in tumult and confusion.')

*%(ga)s*

> %(gaq)s  (Turkish translation by Benli; the Arabic was not retrieved)

See [[Ma'ruf al-Rusafi]], [[Mustafa al-Ghalayini]], [[Ahmad Shawqi]] for the better-known Arab ode.

## Huda Sha'arawi (April 1935), 'Atasharq'

*%(hu)s*

> %(huq)s
> (translation: 'I say that this is not enough: for us you are Atasharq [Father of the East].')

She spoke in Turkish to Atatürk at the reception for the delegates of the Istanbul congress of the International Alliance
of Women. Our text is the Arabic as quoted from her memoirs by an Islamist critic, who cites it to condemn her; Libal (2008)
independently reports the saying. See [[Huda Sha'arawi]], [[Women's Suffrage in Turkey]].

## Marcus Garvey and The Negro World (1922, 1927)

*%(ga2)s*

> %(ga2q)s

Garvey's front-page message of 23 September 1922, days after Smyrna, makes Kemal the man around whom 'the world revolves',
tells his followers they will not be used in Britain's war against the Turks, and answers the 'barbarian' charge by pointing
at British bombing in Africa. That is his framing of a disputed event (see [[Burning of Smyrna]]), not the vault's. *%(nw)s*

> %(nwq)s

See [[Marcus Garvey]].

## Elisaveta Bagryana, 'New Atlantis'

*%(ba)s*

> %(baq)s
> (translation: 'The legend becomes life (long live life!), life forged with hammer and sledge!')

Collected in *Сърце човешко* (1932, 1936 editions; dated 1936 at the census check); the dedication 'To Kemal Atatürk' implies the 1934 surname, so the 1936 edition. See [[Elisaveta Bagryana]].

## Sources
%(src)s
""" % dict(nz=R[0]["saw"], nzq=R[0]["q"], ru=R[1]["saw"], ruq=R[1]["q"], ga=R[2]["saw"], gaq=R[2]["q"],
           hu=R[3]["saw"], huq=R[3]["q"], ga2=R[4]["saw"], ga2q=R[4]["q"], nw=R[5]["saw"], nwq=R[5]["q"],
           ba=R[6]["saw"], baq=R[6]["q"],
           src="\n".join("- %s: %s" % (r["loc"], r["urls"][0]) for r in R))
note("Events", NODE, {"type": "event", "when": "1921–1935", "tags": ["event", "verified", "writers", "anti-colonial"]}, body)
print("ok", len(R))
