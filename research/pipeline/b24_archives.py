# -*- coding: utf-8 -*-
# Census round 15 (Nov 2026), slug "archives" — heads of state and government in their own words, via the Anıtkabir Special Book.
# Seam: Turkish news sites print the full text visiting leaders write in the "Anıtkabir Özel Defteri". Found with free DuckDuckGo-HTML
# queries through `tools/ms fetch` (html.duckduckgo.com/html/?q=...), articles fetched with `tools/ms fetch` and banked in
# tools/.state/round15/src_*.json. Quotes are Turkish translations (marked) except Imran Khan (English as printed by Daily Sabah).
# Every quote is checked against its bank before anything is written.
import json, os, re, sys
from _lib import note, person

HERE = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(HERE, "tools", ".state", "round15")
NODE = "Leaders in the Anıtkabir Special Book, 2004–2025"

def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"').replace("\xa0", " ")
    s = s.replace("**", "").replace("*", "")
    return re.sub(r"\s+", " ", s)

def bank(n):
    return norm(json.load(open(os.path.join(STATE, "src_%s.json" % n), encoding="utf-8"))["results"][0]["text"])

T = "[translation] "
R = [
 dict(id="putin-2004-12-06-book", voice="Vladimir Putin", role="President of Russia; entry in the Anıtkabir special book", c="Russia", cn="Russia",
      date="2004-12-06", mirror=None, pol="instrumental", inten=2,
      saw="Says Turkey's rebirth as a state is linked to Atatürk's name and that both nations' task is to continue his work.",
      q="Rusya'da Türk halkının büyük oğlu Atatürk'ün hatırasına büyük değer veriliyor. Türk devletinin yeniden doğuşu, O'nun adıyla ilişkilendirilir.",
      bank="hurriyet_putin",
      cav="UPGRADE of the existing putin-2004-12-06 record (Kremlin paraphrase only): the Turkish text of the entry. Hürriyet 6 Dec 2004 prints it in full; the RTİB piece (rtib.org) repeats the same Turkish text. Both are Turkish renderings of a Russian-language entry; the Russian original is not located. Full text continues: 'Ülkelerimiz arasındaki dostluğun gelişiminin başlangıcında da O'nun adı vardır. Bizim görevimiz O'nun hatırasına layık olmak ve O'nun yaptıklarını devam ettirmektir.' Diplomatic occasion; Putin's 2005 Samsun speech is not counted (no view stated).",
      med="Hürriyet 6 Dec 2004 (Turkish translation of the entry); RTİB repeats it",
      urls=["https://www.hurriyet.com.tr/gundem/putin-ataturkun-yaptiklarini-devam-ettirelim-279042", "https://www.rtib.org/tr/haberler/putin-ataturkun-yaptiklarini-devam-ettirelim", "http://en.kremlin.ru/events/president/news/32318"],
      ev="P+J", link="Vladimir Putin"),
 dict(id="putin-2014-12-01", voice="Vladimir Putin", role="President of Russia; entry in the Anıtkabir special book", c="Russia", cn="Russia",
      date="2014-12-01", mirror=None, pol="instrumental", inten=1,
      saw="Says Russia deeply respects Atatürk's memory and values his contribution to establishing friendly relations between the two countries.",
      q="Rusya, Türkiye Cumhuriyeti'nin kurucusu Mustafa Kemal Atatürk'ün anısına derin saygı duyuyor.",
      bank="aa_putin14",
      cav="Turkish rendering of the Russian entry (AA 1 Dec 2014; Sabah 2 Dec 2014 prints the same text, probably from the same wire). Second entry by the same hand ten years after the 2004 one; the wording is now official courtesy and no longer 'continue his work'. Date from AA's report of the day.",
      med="Anadolu Ajansı and Sabah (Turkish translation of the entry)",
      urls=["https://www.aa.com.tr/tr/dunya/putin-turkiyede/96622", "https://www.sabah.com.tr/gundem/2014/12/02/anisina-derin-saygi-duyuyoruz"],
      ev="J", link="Vladimir Putin"),
 dict(id="george-w-bush-2004-06-28", voice="George W. Bush", role="President of the United States; entry in the Anıtkabir special book", c="United States", cn="United States",
      date="2004-06-28", mirror="modernization-poster-child", pol="admiring", inten=2,
      saw="Says Atatürk, leading with reform, founded a Turkey with democracy on equal rights, a shining example; Americans share Turkish admiration.",
      q="Türk insanının Atatürk'e gösterdiği saygı ve hayranlığını paylaşıyoruz. Atatürk, reformculuğa önderlik ederek eşit haklara dayalı demokrasiye sahip Türkiye'yi parlayan bir örnek olarak kurdu.",
      bank="hur_bush",
      cav="Hürriyet ('Çok duygulandım') prints the full Turkish text; Yeni Mesaj of 28.06.2004 (probably from the same agency report) only paraphrases ('eşit haklar ve laik bir demokrasiye dayalı parlayan bir örnek'). The English original is not located; Turkish Wikipedia's visitor list dates the visit 27 June, the press says the morning after Bush arrived in Ankara (the Istanbul NATO summit followed). Courtesy text on the eve of the Istanbul NATO summit.",
      med="Hürriyet (Turkish translation of the entry); Yeni Mesaj paraphrase",
      urls=["https://www.hurriyet.com.tr/gundem/cok-duygulandim-236952", "https://www.yenimesaj.com.tr/anitkabir-ozel-defterini-cia-kalemiyle-imzaladi-H1100793.htm"],
      ev="J", link="George W. Bush"),
 dict(id="charles-2007-11-30", voice="Charles, Prince of Wales (later King Charles III)", role="Heir to the British throne; entry in the Anıtkabir special book", c="United Kingdom", cn="United Kingdom",
      date="2007-11-30", mirror=None, pol="instrumental", inten=1,
      saw="Delighted to pay respects in Atatürk's presence; says Turkey and Britain will keep working for peace and friendship.",
      q="Saygılarımı sunmak üzere Mustafa Kemal Atatürk'ün huzurunda bulunmaktan büyük mutluluk duyuyorum. Türkiye ve İngiltere dünya barışı ve dostluğu için birlikte çalışmayı sürdürecektir.",
      bank="iha_charles",
      cav="Not yet a head of state in 2007. Two Turkish renderings of the English entry differ (İHA as quoted; Milliyet: 'Mustafa Kemal'in mezarında ona saygılarımı sunmaktan mutluluk duyuyorum'); the English original is not located. No evaluation of Atatürk beyond the courtesy line. Date from Turkish Wikipedia's visitor list; the press pieces carry no day.",
      med="İHA and Milliyet (two different Turkish translations)",
      urls=["https://www.iha.com.tr/haber-charlesin-son-duragi-anitkabir-5153", "https://www.milliyet.com.tr/pembenar/prens-charles-anitkabirde-225519"],
      ev="J", link="King Charles III"),
 dict(id="elizabeth-ii-2008-05-13", voice="Elizabeth II", role="Queen of the United Kingdom; entry in the Anıtkabir special book", c="United Kingdom", cn="United Kingdom",
      date="2008-05-13", mirror=None, pol="admiring", inten=1,
      saw="Calls Atatürk a valued friend of the United Kingdom and one of the greatest figures of modern history.",
      q="Birleşik Krallığın büyük değer verdiği bir dostu ve modern tarihin en büyük şahsiyetlerinden biri olan Mustafa Kemal Atatürk'e saygılarımı sunmak, benim için büyük bir onurdur.",
      bank="haberler_liz08",
      cav="Handwritten in English; Hürriyet ('Dünyanın gözü bu yemekteydi') and AA via Haberler print the same Turkish rendering with slightly different case endings ('Atatürk'ün' / 'Atatürk'e'). English original not located. A constitutional monarch's text, in practice drafted with the Foreign Office. Her first state visit in 37 years (the 1971 visit also included a wreath and the book).",
      med="Hürriyet and AA/Haberler (Turkish translation of the entry)",
      urls=["https://www.haberler.com/guncel/ingiltere-kralicesi-elizabeth-anitkabir-de-2-haberi/", "https://www.hurriyet.com.tr/gundem/dunyanin-gozu-bu-yemekteydi-8935699"],
      ev="J", link="Elizabeth II"),
 dict(id="biden-2011-12-02", voice="Joe Biden", role="Vice President of the United States (later President); entry in the Anıtkabir special book", c="United States", cn="United States",
      date="2011-12-02", mirror="nation-forge-template", pol="admiring", inten=2,
      saw="Says peoples seeking a voice in government can draw inspiration from Atatürk's emphasis on democracy; quotes his tenth-anniversary words.",
      q="Bugün dünya çapında insanlar nasıl yönetilecekleri konusunda seslerini yükseltmeye çalışırken, Atatürk'ün Türkiye'nin gelişmesinde kullanılan demokrasinin prensiplerini yaptığı vurgudan ilham alabilirler.",
      bank="iha_biden",
      cav="Only İHA's full text was read (T24 and Haberler carry summaries or a stub). Turkish rendering of an English entry, so the sentence is clumsy; the English original is not located. Biden then quotes Atatürk's tenth-anniversary words as 'Yaptıklarımızın yeterli olduğuna asla inanmıyoruz. Daha ulvi ve büyük başarılara ulaşmaya kararlıyız ve mecburuz' (Turkish rendering). Vice-presidential, not presidential, at the time.",
      med="İHA 2 Dec 2011 (Turkish translation of the entry)",
      urls=["https://www.iha.com.tr/ankara-haberleri/-990"],
      ev="J", link="Joe Biden"),
 dict(id="xi-jinping-2012-02-21", voice="Xi Jinping", role="Vice President of China (later paramount leader); entry in the Anıtkabir special book", c="China", cn="China",
      date="2012-02-21", mirror=None, pol="admiring", inten=1,
      saw="One-line salute in Chinese: 'Mustafa Kemal Atatürk, founder of the Republic of Turkey, long live', without elaboration.",
      q="Türkiye Cumhuriyeti'nin kurucusu Mustafa Kemal Atatürk, sonsuza kadar yaşa",
      bank="hur_xi",
      cav="Turkish rendering of a Chinese entry (Hürriyet; the AA text at A Haber 21 Feb 2012 is identical, same wire). The Chinese original is not located; 'sonsuza kadar yaşa' is the Turkish for the slogan form 'wansui'/'long live'. Xi was Vice President and heir apparent on the visit.",
      med="Hürriyet and AA/A Haber (Turkish translation of the entry)",
      urls=["https://www.hurriyet.com.tr/gundem/sonsuza-kadar-yasa-ataturk-19970645", "https://www.ahaber.com.tr/dunya/2012/02/21/si-cinping-anitkabiri-ziyaret-etti"],
      ev="J", link="Xi Jinping"),
 dict(id="kenyatta-2014-04-08", voice="Uhuru Kenyatta", role="President of Kenya; entry in the Anıtkabir special book", c="Kenya", cn="Kenya",
      date="2014-04-08", mirror="nation-forge-template", pol="admiring", inten=2,
      saw="Atatürk will be remembered for courage, vision and resolve in the independence struggle; a leading figure of the century whose leadership inspires Kenyans.",
      q="Mustafa Kemal Atatürk her zaman cesareti, vizyonu ve Türklerin bağımsızlık mücadelesindeki kararlılığı ile hatırlanacaktır.",
      bank="haberler_kenyatta",
      cav="AA report via Haberler; the same AA text appears on sondakika.com (not independent). Turkish rendering of an English entry; English original not located. The date (8 April 2014) comes from Turkish Wikipedia's visitor list; the AA piece says Gül would receive him 'bugün' at Çankaya.",
      med="AA via Haberler (Turkish translation of the entry)",
      urls=["https://www.haberler.com/guncel/kenya-cumhurbaskani-kenyatta-anitkabir-de-5882345-haberi/"],
      ev="J", link="Uhuru Kenyatta"),
 dict(id="merkel-2016-02-08", voice="Angela Merkel", role="Chancellor of Germany; entry in the Anıtkabir special book", c="Germany", cn="Germany",
      date="2016-02-08", mirror="modernization-poster-child", pol="admiring", inten=1,
      saw="Honours Atatürk as father of the modern Turkish Republic and a pioneer of the way to Europe.",
      q="Türk ve Alman halkları arasındaki özel dostluk ruhu içinde, çağdaş Türkiye Cumhuriyeti'nin Ata'sı ve Avrupa'ya giden yolun mimarı Mustafa Kemal Atatürk'ün anısına, derin saygılarımla.",
      bank="yeniasir_merkel",
      cav="German original from the German Embassy Ankara's own post of the entry (Facebook, 'Gedenkbucheintrag von Bundeskanzlerin Merkel in Anıtkabir', 8 Feb 2016, 5:17 AM; German and Turkish texts with a photo of the page; read via Monid render, 5 Nov 2026). Turkish outlets (Yeni Asır, Ensonhaber) print the embassy's Turkish version, which renders 'Wegbereiter' (pathfinder) as 'mimarı' (architect) and 'Vater' as 'Ata'. Written on the day of the refugee-deal visit to Davutoğlu.",
      med="Deutsche Botschaft Ankara, official post of the entry (German and Turkish), 8 Feb 2016",
      urls=["https://www.facebook.com/almanyabe/photos/a.10150589796897810/10153454159857810/", "https://www.yeniasir.com.tr/gundem/2016/02/08/turkiye-cumhuriyetinin-atasi", "https://www.ensonhaber.com/merkel-anitkabiri-ziyaret-etti-2016-02-08-h10640632"],
      ev="P+J", link="Angela Merkel"),
 dict(id="abbas-2016-10-24", voice="Mahmoud Abbas", role="President of the State of Palestine; entry in the Anıtkabir special book", c="Palestine", cn="Palestine",
      date="2016-10-24", mirror=None, pol="admiring", inten=1,
      saw="Calls him 'the great leader' and appreciates his major role in founding the Turkish Republic; sends Palestinians' greetings to his spirit.",
      q="büyük lider Mustafa Kemal Atatürk'ün Türkiye Cumhuriyeti'nin kuruluş sürecinde gösterdiği büyük rolü takdirle karşılıyoruz.",
      bank="sputnik_abbas",
      cav="AA text republished by Sputnik Türkiye (anlatilaninotesi.com.tr, 24 Oct 2016); Turkish rendering of an Arabic entry, Arabic original not located. Mixes praise of Atatürk with greetings to Erdoğan's government, three months after the July 2016 coup attempt.",
      med="AA via Sputnik Türkiye (Turkish translation of the entry)",
      urls=["https://anlatilaninotesi.com.tr/20161024/abbas-anitkabir-ziyaret-1025444619.html"],
      ev="J", link="Mahmoud Abbas"),
 dict(id="imran-khan-2019-01-04", voice="Imran Khan", role="Prime Minister of Pakistan; entry in the Anıtkabir special book", c="Pakistan", cn="Pakistan",
      date="2019-01-04", mirror="anti-colonial-liberator", pol="admiring", inten=2,
      saw="Calls Atatürk one of the 20th century's greatest statesmen, an inspiration to anti-colonial struggles, and cites Jinnah's praise.",
      q="led the Turkish people in one of the most difficult times, and changed the history of Turks as well as the world, and has been a source of inspiration for those struggling against colonialism throughout the world.",
      bank="dailysabah_imran",
      cav="English as printed by Daily Sabah (4 Jan 2019, 'he wrote in the book'; whether this is Khan's own English or Sabah's back-translation of AA's Turkish is not established; AA's Turkish text is the second source). The entry also quotes Jinnah calling Atatürk 'one of the greatest people who has ever lived' (the Jinnah line is unsourced in the vault, see round 12) and ends 'His glorious struggle for the independence and unity of the Turkish nation will forever remain a golden chapter in the annals of history.'",
      med="Daily Sabah and Anadolu Ajansı 4 Jan 2019",
      urls=["https://www.dailysabah.com/diplomacy/2019/01/04/pakistani-pm-imran-khan-pays-visit-to-anitkabir-mausoleum-of-turkeys-founder-ataturk", "https://www.aa.com.tr/tr/turkiye/pakistan-basbakani-han-anitkabirde/1355808"],
      ev="J", link="Imran Khan", english=True),
 dict(id="scholz-2022-03-14", voice="Olaf Scholz", role="Chancellor of Germany; entry in the Anıtkabir special book", c="Germany", cn="Germany",
      date="2022-03-14", mirror="modernization-poster-child", pol="admiring", inten=1,
      saw="Pays deep respect to Atatürk, 'founder of modern Turkey and great European statesman', and values German-Turkish ties in difficult times.",
      q="Modern Türkiye'nin kurucusu büyük Avrupalı devlet adamı Mustafa Kemal Atatürk'e derin saygıyla.",
      bank="yenicag_scholz",
      cav="Turkish rendering of a German entry. Yeniçağ and Panorama News print the same text; the German Embassy's Instagram post (14 Mar 2022) gives a different Turkish wording ('Çağdaş Türkiye'nin kurucusu ve Avrupalı büyük devlet adamı ... en derin saygılarımla'), which shows both are translations. German original not located. Written days after the start of the Ukraine war (the entry itself says 'in such difficult times').",
      med="Yeniçağ and Panorama News 14–15 Mar 2022 (Turkish translation of the entry)",
      urls=["https://www.yenicaggazetesi.com/almanya-basbakani-olaf-scholz-anitkabiri-ziyaret-etti-mustafa-kemal-ataturke-derin-saygiyla-520455h.htm", "https://panorama-news.de/avrupa/scholz-anitkabir-ziyaret-defterine-neler-yazdi/", "https://www.instagram.com/p/CbFb0hKgtiR/"],
      ev="J", link="Olaf Scholz"),
 dict(id="starmer-2025-10-27", voice="Keir Starmer", role="Prime Minister of the United Kingdom; entry in the Anıtkabir special book", c="United Kingdom", cn="United Kingdom",
      date="2025-10-27", mirror=None, pol="instrumental", inten=1,
      saw="Calls Atatürk 'the father of modern Turkey' and says it is an honour to pay respects, framing it around the UK-Turkey alliance.",
      q="Modern Türkiye'nin babası Mustafa Kemal Atatürk'e saygılarımı sunmak bir onurdur.",
      bank="aksam_starmer",
      cav="Turkish rendering of an English entry; Akşam and Haberler (both AA) print it with 'babası'; another AA-derived version reads 'kurucusu', which shows the rendering varies. English original not located.",
      med="AA via Akşam and Haberler, 27 Oct 2025 (Turkish translation of the entry)",
      urls=["https://www.aksam.com.tr/guncel/starmer-anitkabirde-ozel-defteri-imzaladi-isbirligimiz-buyuyecek/haber-1613844", "https://www.haberler.com/guncel/ingiltere-basbakani-keir-starmer-anitkabir-i-ziyaret-etti-19191212-haberi/"],
      ev="J", link="Keir Starmer"),
]

bad = []
for r in R:
    assert len(r["saw"].split()) <= 25, (r["id"], len(r["saw"].split()))
    if norm(r["q"]) not in bank(r["bank"]):
        bad.append(r["id"])
if bad:
    sys.exit("quote not found in source bank: %s" % bad)

recs = []
for r in R:
    eng = r.get("english")
    recs.append({
        "id": r["id"], "voice": r["voice"], "voice_type": "person", "role": r["role"],
        "country": r["c"], "country_now": r["cn"], "domain": "politics", "date": r["date"], "era": "posthumous",
        "mirror": r["mirror"], "polarity": r["pol"], "intensity": r["inten"], "what_they_saw": r["saw"],
        "quote": r["q"] if eng else T + r["q"], "artifact": "quote", "evidence": r["ev"], "mediated_by": r["med"],
        "caveat": r["cav"], "node": NODE if r["link"] != "Vladimir Putin" else NODE, "sources": r["urls"],
    })
with open(os.path.join(STATE, "gazes_archives.jsonl"), "w", encoding="utf-8") as f:
    for x in recs:
        f.write(json.dumps(x, ensure_ascii=False) + "\n")

with open(os.path.join(STATE, "ledger_archives.md"), "w", encoding="utf-8") as f:
    f.write("| Claim | Node | Status | Sources | Next step |\n|---|---|---|---|---|\n")
    for r in R:
        f.write("| %s (%s, %s): %s | %s | verified %s (Turkish press report of the Anıtkabir special book entry; translation) | %s | %s |\n" % (
            r["voice"], r["role"].split(";")[0], r["date"], (r["q"][:100] + ("…" if len(r["q"]) > 100 else "")), NODE, r["ev"],
            " ; ".join(r["urls"]), "original-language text of the entry (Anıtkabir Özel Defteri volume, ed. Recep Cengiz) if reachable"))

people = {
 "George W. Bush": ("President of the United States, 2001–2009", "American", "1946–", "admirer (diplomatic)",
    "On 27 June 2004, on the eve of the Istanbul NATO summit, he wrote in the Anıtkabir book that Atatürk founded Turkey as a shining example of democracy on equal rights."),
 "King Charles III": ("King of the United Kingdom (as Prince of Wales in 2007)", "British", "1948–", "courtesy",
    "On 30 November 2007, as Prince of Wales, he signed the Anıtkabir book with a line of respect and of Anglo-Turkish friendship."),
 "Elizabeth II": ("Queen of the United Kingdom, 1952–2022", "British", "1926–2022", "courtesy",
    "On her 2008 state visit she wrote in the Anıtkabir book that Atatürk was 'a much valued friend of the United Kingdom and one of the great figures of modern history'."),
 "Joe Biden": ("Vice President (2009–2017) and President (2021–2025) of the United States", "American", "1942–", "admirer",
    "As Vice President on 2 December 2011 he wrote that peoples seeking a voice in government can draw inspiration from Atatürk's emphasis on democracy."),
 "Xi Jinping": ("Vice President of China in 2012; later General Secretary and President", "Chinese", "1953–", "salute",
    "On 21 February 2012, as heir apparent, he wrote in Chinese in the Anıtkabir book 'Mustafa Kemal Atatürk, founder of the Republic of Turkey, long live'."),
 "Uhuru Kenyatta": ("President of Kenya, 2013–2022", "Kenyan", "1961–", "admirer",
    "In April 2014 he wrote that Atatürk would be remembered for courage, vision and resolve in the independence struggle, and that his leadership inspires Kenyans."),
 "Angela Merkel": ("Chancellor of Germany, 2005–2021", "German", "1954–", "admirer (diplomatic)",
    "On 8 February 2016 she wrote in the Anıtkabir book of Atatürk as 'Vater der modernen Republik Türkei' and 'Wegbereiter nach Europa' (pioneer of the way to Europe; Turkish outlets rendered it 'architect')."),
 "Mahmoud Abbas": ("President of the State of Palestine", "Palestinian", "1935–", "admirer (diplomatic)",
    "On 24 October 2016 he wrote of 'the great leader Mustafa Kemal Atatürk' and his great role in founding the Turkish Republic."),
 "Imran Khan": ("Prime Minister of Pakistan, 2018–2022", "Pakistani", "1952–", "admirer",
    "On 4 January 2019 he wrote that Atatürk was among the greatest statesmen of the 20th century and an inspiration to anti-colonial struggles."),
 "Olaf Scholz": ("Chancellor of Germany, 2021–2025", "German", "1958–", "admirer (diplomatic)",
    "On 14 March 2022 he wrote of Atatürk as 'founder of modern Turkey and great European statesman'."),
 "Keir Starmer": ("Prime Minister of the United Kingdom, 2024–", "British", "1962–", "courtesy",
    "On 27 October 2025 he wrote in the Anıtkabir book of Atatürk as 'the father of modern Turkey'."),
}
for name, (role, nat, life, stance, desc) in people.items():
    if os.path.exists(os.path.join(HERE, "vault", "People", name + ".md")):
        continue
    person(name, role=role, nat=nat, life=life, stance=stance, tags=["verified", "head-of-state", "anitkabir"],
           body="%s\n\nSee [[%s]] and [[Anıtkabir]].\n\n## Sources\n- Turkish press reports of the Anıtkabir special book entry; see [[%s]].\n" % (desc, NODE, NODE))

body = ["""
Turkish news sites print what visiting foreign leaders write in the Anıtkabir special book (Anıtkabir Özel Defteri), in Turkish
translation, within hours of the ceremony. Round 15 found twelve entries by heads of state and government, one for each of eleven
voices plus a second entry for Putin. Every quote below was checked against the fetched page text. All are Turkish translations
except Imran Khan's, which Daily Sabah printed in English; no original-language text has been located, so the exact words in
English, German, Russian, Chinese or Arabic remain unverified. The value is that the lines are the leaders' own choices of what
to say before the tomb.

## What they chose to say

- **Europe's road:** [[Angela Merkel]] (2016) and [[Olaf Scholz]] (2022) each call Atatürk a European: 'Wegbereiter nach Europa' (pioneer of the way to Europe), 'great European statesman'. Both entries are about the German-Turkish relationship at moments of strain (the refugee deal, the Ukraine war).
- **Anti-colonial inspiration:** [[Imran Khan]] (2019) is the one who gives a reason: a source of inspiration for those fighting colonialism, and he cites Jinnah. [[Uhuru Kenyatta]] (2014) says his leadership inspired Kenya's own transformation. [[Mahmoud Abbas]] (2016) appreciates his role in founding the Republic.
- **Democracy and reform for America:** [[George W. Bush]] (2004) praises equal-rights democracy and reform; [[Joe Biden]] (2011) points to Atatürk's democratic emphasis for peoples seeking a voice, and quotes his Tenth Anniversary Speech.
- **Britain's courtesy:** [[Elizabeth II]] (2008), [[King Charles III]] (2007) and [[Keir Starmer]] (2025) pay respects; only Elizabeth says anything of him ('a much valued friend... one of the great figures of modern history'), and Starmer calls him 'the father of modern Turkey'.
- **Russia and China:** [[Vladimir Putin]] wrote in 2004 that the rebirth of the Turkish state 'is linked to his name' and that continuing his work is both nations' task; in 2014 he shortened this to respect for his memory. [[Xi Jinping]] (2012) wrote one line: 'long live' the founder.
"""]
for r in R:
    body.append("\n## %s (%s)\n" % (r["voice"], r["date"]))
    body.append("*%s*\n" % r["saw"])
    body.append("> %s\n" % (r["q"] if r.get("english") else T + r["q"]))
    body.append("%s Evidence %s. See [[%s]].\n" % (r["cav"], r["ev"], r["link"]))

body.append("""
## Dry ends (round 15)

- **Historic Hansard, prime ministers:** the Commons sittings of 10–23 November 1938 were scanned by title; there is no tribute, question or statement on Atatürk's death on any of them, and no Lords sitting of the fortnight carries one (the Lords paid tribute in October 1939, already stored). Targets Baldwin, MacDonald, Chamberlain, Attlee, Eden, Macmillan, Wilson, Callaghan and Major did not turn up in the DuckDuckGo site: searches, which index few sitting pages by content.
- **Not reached:** Indian PMs (pib, mea), Kohl and Schröder (Anıtkabir searches returned nothing), Gorbachev, Khrushchev, Medvedev (visited May 2010, entry text not found), Japanese PMs (Abe 2013: AA reports the signing, not the words), UN Secretaries-General.
- **Entries by Blair, Cameron, Macron, Hollande, Mirziyoyev, Zelensky, Tokayev, Shehbaz Sharif:** searched; no printed text found, or no mention of Atatürk. Zelensky's 2019 and 2023 visits and his wife's 2023 comment are reported without an entry.
- **Other entries known to exist but not yet read:** Tito (1954), Heuss (1957), Sukarno (1959), Ayub Khan (1959), Eisenhower (already stored), Asad (2004), Rousseff (2011), Correa (2012), Hollande (2014), Lukashenko (2019), Duda, Vučić, Niinistö, Stubb. The 1953- volumes *Anıtkabir Özel Defteri* (ed. Recep Cengiz) reproduce earlier entries.

## Sources
- Turkish press reports (Hürriyet, Milliyet, İHA, AA and its republishers, Akşam, Haberler, Sabah, Yeni Asır, Ensonhaber, Yeniçağ, Panorama News, Sputnik Türkiye, Daily Sabah): the exact URLs are listed under each record.
- President of Russia, en.kremlin.ru, news 32318 (Putin 2004, paraphrase).
- Turkish Wikipedia, 'Anıtkabir ziyaretçileri listesi' (dates of visits only).
""")

note("Events", NODE,
     {"type": "event", "when": "2004–2025",
      "tags": ["event", "verified", "heads-of-state", "anitkabir"]},
     "\n".join(body))
print("ok", len(recs), "records")
