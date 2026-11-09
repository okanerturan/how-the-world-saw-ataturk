# -*- coding: utf-8 -*-
# Census round 16 (Nov 2026), slug "anitkabir" — more entries by visiting leaders and ministers in the Anıtkabir Special Book.
# Seam (from round 15): Turkish news sites print what visiting foreign leaders write in the "Anıtkabir Özel Defteri". Found with free
# DuckDuckGo-HTML queries through `tools/ms fetch`, articles fetched with `tools/ms fetch` and banked in tools/.state/round16/anit/.
# All quotes are Turkish translations (marked) except Kristersson (English as printed by Middle East Monitor). Each quote is checked
# against the banked page text before anything is written.
import glob, json, os, re, sys
from _lib import note, person

HERE = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(HERE, "tools", ".state", "round16")
BANK = os.path.join(STATE, "anit")
NODE = "Ministers, Premiers and Presidents in the Anıtkabir Special Book, 2009–2026"
PRIOR = "Leaders in the Anıtkabir Special Book, 2004–2025"

def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"').replace("\xa0", " ")
    s = s.replace("**", "").replace("*", "")
    return re.sub(r"\s+", " ", s)

PAGES = {}
for f in glob.glob(os.path.join(BANK, "*.json")):
    for r in json.load(open(f, encoding="utf-8"))["results"]:
        PAGES[r["url"]] = norm(r["text"])

def check(rid, q, url):
    t = PAGES.get(url)
    if t is None:
        sys.exit("NO BANK for %s: %s" % (rid, url))
    if norm(q) not in t:
        sys.exit("QUOTE NOT FOUND in bank for %s: %s" % (rid, url))

T = "[translation] "
TR = "Turkish rendering of an entry written in English"
R = [
 dict(id="obama-2009-04-06-book", voice="Barack Obama", role="President of the United States; entry in the Anıtkabir special book", c="United States", cn="United States",
      dom="politics", date="2009-04-06", mirror="modernization-poster-child", pol="admiring", inten=2,
      saw="Honoured to pay respects to Atatürk, whose vision, resolve and courage turned Turkey toward democracy and whose legacy inspires generations worldwide.",
      q="Vizyonu, kararlılığı ve cesaretiyle Türkiye Cumhuriyeti'ni demokrasiye yönelten ve mirası tüm dünyaya kuşaklar boyunca ilham vermeye devam eden Mustafa Kemal Atatürk'e saygılarımı sunmak, benim için bir onurdur.",
      qurl="https://www.haberturk.com/gundem/haber/138881-obama-anitkabir-ozel-defterine-ne-yazdi",
      cav=TR + ". Habertürk and T24 print the same wording; Dengegazetesi (6 Apr 2009) gives a looser version ('Vizyonu, ısrarı ve cesareti, ...'), so the exact English is not fixed. The entry goes on to invoke 'Yurtta barış, dünyada barış' and to promise support for Atatürk's vision of Turkey as a modern, prosperous democracy. Separate artifact from the Assembly speech of the same day (record obama-2009).",
      med="Habertürk, Dengegazetesi and T24, 6 Apr 2009 (Turkish translations of the entry)",
      urls=["https://www.haberturk.com/gundem/haber/138881-obama-anitkabir-ozel-defterine-ne-yazdi", "https://t24.com.tr/gundem/obama-elini-yuregine-koyup-ataturku-hissetti,38730", "https://www.dengegazetesi.com.tr/anitkabir-defterine-ne-yazdi-21749h.htm"],
      ev="J", link="Barack Obama"),
 dict(id="hillary-clinton-2009-03-07-book", voice="Hillary Clinton", role="US Secretary of State; entry in the Anıtkabir special book", c="United States", cn="United States",
      dom="diplomacy", date="2009-03-07", mirror=None, pol="instrumental", inten=1,
      saw="Pays respects to the founder of 'this great country' and shows the friendship of the American people; says only that.",
      q="Bu büyük ülkenin kurucusuna saygımızı ve Amerikan halkının dostluğunu göstermek için ülkem adına burayı bir kez daha ziyaret etmekten onur duyuyorum.",
      qurl="https://www.haberturk.com/gundem/haber/132876-hillary-clinton-anitkabirde",
      cav=TR + "; Habertürk, T24 and NTV print the same wording. Atatürk is not named in the quoted line: 'the founder of this great country' is the only reference, hence intensity 1. Habertürk and T24 are dated 7 Mar 2009, NTV 6 Mar 2009 (probably a pre-visit post).",
      med="Habertürk, T24 and NTV, Mar 2009 (Turkish translation of the entry)",
      urls=["https://www.haberturk.com/gundem/haber/132876-hillary-clinton-anitkabirde", "https://t24.com.tr/gundem/clintondan-anitkabir-jesti,33118", "https://www.ntv.com.tr/turkiye/clinton-burada-olmaktan-onur-duyuyorum,wqZdXmBhskSc4jZoaBy6Mw"],
      ev="J", link="Hillary Clinton"),
 dict(id="kerry-2013-03-02-book", voice="John Kerry", role="US Secretary of State; entry in the Anıtkabir special book", c="United States", cn="United States",
      dom="diplomacy", date="2013-03-02", mirror="modernization-poster-child", pol="admiring", inten=2,
      saw="Pays deep respect to Atatürk as a soldier and statesman who pioneered education and independence.",
      q="Eğitim ve bağımsızlığın öncüsü bir asker ve devlet adamı olan Mustafa Kemal Atatürk'e derin saygılarımla. Türk halkına ve bu büyük lidere, Amerikan halkının bir temsilcisi olarak saygılarımı sunmaktan onur ve gurur duyuyorum.",
      qurl="https://www.hurriyet.com.tr/gundem/anitkabir-ozel-defterine-ne-yazdi-22723059",
      cav=TR + ". Hürriyet (2 Mar 2013, credited AA), Akşam and Cumhuriyet print the same Turkish text; all three are probably the same AA wire. Kerry flew out of Ankara after the visit.",
      med="Hürriyet (AA), Akşam and Cumhuriyet, 2 Mar 2013 (Turkish translation of the entry)",
      urls=["https://www.hurriyet.com.tr/gundem/anitkabir-ozel-defterine-ne-yazdi-22723059", "https://www.aksam.com.tr/siyaset/kerry-anitkabir-ozel-defterine-ne-yazdi/haber-173622", "https://www.cumhuriyet.com.tr/haber/kerry-anitkabiri-ziyaret-etti-406944"],
      ev="J", link="John Kerry"),
 dict(id="tillerson-2017-03-30-book", voice="Rex Tillerson", role="US Secretary of State; entry in the Anıtkabir special book", c="United States", cn="United States",
      dom="diplomacy", date="2017-03-30", mirror=None, pol="admiring", inten=2,
      saw="Calls Atatürk the great and eminent leader of the Republic and speaks of his deep respect and admiration.",
      q="Türkiye Cumhuriyeti'nin büyük ve üstün lideri Mustafa Kemal Atatürk'e olan derin saygı ve hayranlığımın bir göstergesi olarak, Amerikan halkının bir temsilcisi sıfatıyla, Türk halkına ve bu büyük lidere saygılarımı sunmaktan derin bir onur duyuyorum.",
      qurl="https://www.sozcu.com.tr/rex-tillerson-buyuk-ve-ustun-lider-mustafa-kemal-ataturke-saygilarimi-sunuyorum-wp1766193",
      cav=TR + ". The quote is the DHA wire as printed by Sözcü. Three agencies give three different Turkish renderings: AA ('büyük ve seçkin lideri ... derin saygı ve takdirle ... bu harika lidere'), İHA ('büyük lideri ... hayranlıklarımla') and DHA (as quoted), so the exact English wording cannot be fixed. Tillerson read the entry aloud (AA). The date 30 Mar 2017 is from the sondakika.com stamp of the DHA copy.",
      med="Sözcü (DHA), İHA via Haberler and AA via Haberler/Sondakika, 30 Mar 2017 (three different Turkish translations)",
      urls=["https://www.sozcu.com.tr/rex-tillerson-buyuk-ve-ustun-lider-mustafa-kemal-ataturke-saygilarimi-sunuyorum-wp1766193", "https://www.haberler.com/guncel/tillerson-anitkabir-i-ziyaret-etti-9439396-haberi/", "https://www.haberler.com/guncel/abd-disisleri-bakani-tillerson-turkiye-de-9439388-haberi/"],
      ev="J", link="Rex Tillerson"),
 dict(id="blinken-2023-02-20-book", voice="Antony Blinken", role="US Secretary of State; entry in the Anıtkabir special book", c="United States", cn="United States",
      dom="diplomacy", date="2023-02-20", mirror=None, pol="instrumental", inten=1,
      saw="Honoured to pay respects to the Turkish nation and to Atatürk; the entry is mostly about earthquake solidarity and the bond between the peoples.",
      q="Türk ulusu ve Büyük Önder Mustafa Kemal Atatürk'e saygılarımı sunmaktan büyük bir onur duyuyorum.",
      qurl="https://www.tgrthaber.com/dunya/turkiyedeki-abdli-bakan-blinkenin-anitkabir-ozel-defteri-2876244",
      cav=TR + ". Written two weeks after the Kahramanmaraş earthquakes; the rest of the entry speaks of the bond between the peoples 'since the birth of the Republic'. TGRT Haber and Şehitler Ölmez print it; whether both repeat one wire was not checked. Courtesy line with no evaluation of Atatürk.",
      med="TGRT Haber and Şehitler Ölmez, 20 Feb 2023 (Turkish translation of the entry)",
      urls=["https://www.tgrthaber.com/dunya/turkiyedeki-abdli-bakan-blinkenin-anitkabir-ozel-defteri-2876244", "https://www.sehitlerolmez.com/abd-disisleri-bakani-blinken-anitkabiri-ziyaret-etti-ozel-deftere-yazi-yazdi"],
      ev="J", link="Antony Blinken"),
 dict(id="herzog-2022-03-09-book", voice="Isaac Herzog", role="President of Israel; entry in the Anıtkabir special book", c="Israel", cn="Israel",
      dom="politics", date="2022-03-09", mirror="modernization-poster-child", pol="admiring", inten=2,
      saw="Calls Atatürk a great visionary and speaks of the wisdom of his legacy of progress and peace.",
      q="Büyük vizyoner Mustafa Kemal Atatürk`ü ebedileştiren bu tarihi mekânı ziyaret etmek farklı bir ayrıcalık.",
      qurl="https://www.cumhuriyet.com.tr/turkiye/israil-cumhurbaskani-isaac-herzog-anitkabir-defterine-ne-yazdi-1914579",
      cav="Turkish rendering (AA) of an entry written partly in English and partly in Hebrew; the Hebrew line is a verse from the Psalms ('Depart from evil and do good; seek peace and pursue it'), reported as such by Cumhuriyet. The entry continues: following the wisdom of this great leader's legacy of progress and peace, 'let us sincerely embrace the many truths of the promise of a safer, more stable world'. Cumhuriyet is dated 10 Mar 2022; the visit date 9 Mar 2022 is taken from the Turkish Wikipedia visitor list, so check against an agency stamp. Cumhuriyet and Yurt Gazetesi are the same AA copy.",
      med="Cumhuriyet and Yurt Gazetesi, 10 Mar 2022 (AA; Turkish translation of the entry)",
      urls=["https://www.cumhuriyet.com.tr/turkiye/israil-cumhurbaskani-isaac-herzog-anitkabir-defterine-ne-yazdi-1914579", "https://www.yurtgazetesi.com.tr/guncel/israil-cumhurbaskani-isaac-herzog-anitkabir-defterine-bunlari-yazdi-h196216.html"],
      ev="J", link="Isaac Herzog"),
 dict(id="hollande-2014-01-27-book", voice="François Hollande", role="President of France; entry in the Anıtkabir special book", c="France", cn="France",
      dom="politics", date="2014-01-27", mirror=None, pol="admiring", inten=2,
      saw="Addresses the statesman who, after great suffering, built modern Turkey and revived friendship with France.",
      q="Büyük acılar sonrası modern Türkiye'yi kurmayı ve Fransa ile dostluğu tekrar canlandırmayı başaran devlet adamına",
      qurl="https://www.aa.com.tr/tr/turkiye/hollande-turkiyede/187515",
      cav=TR + " (French). The line is an address ('to the statesman who ...') and does not name Atatürk in the printed text; the context is the first state visit by a French president in 22 years. AA, Hürriyet, Sözcü, Dünya, Sondakika and Patronlar Dünyası print the same sentence (one AA wire).",
      med="AA, Hürriyet, Sözcü, Dünya and Sondakika, 27 Jan 2014 (Turkish translation of the entry)",
      urls=["https://www.aa.com.tr/tr/turkiye/hollande-turkiyede/187515", "https://www.hurriyet.com.tr/dunya/hollandein-tarihi-ziyareti-basladi-25663527", "https://www.sozcu.com.tr/hollande-bugun-turkiyede-wp447749", "https://www.dunya.com/gundem/22-yil-sonra-ilk-ziyaret-haberi-235918"],
      ev="J", link="François Hollande"),
 dict(id="renzi-2014-12-11-book", voice="Matteo Renzi", role="Prime Minister of Italy; entry in the Anıtkabir special book", c="Italy", cn="Italy",
      dom="politics", date="2014-12-11", mirror=None, pol="instrumental", inten=1,
      saw="Pays deep respect to Atatürk as founder of modern Turkey and promises support for Turkey's path toward the European Union.",
      q="Modern Türkiye'nin kurucusu Mustafa Kemal Atatürk'e derin saygılarımı sunuyorum.",
      qurl="https://www.haberler.com/guncel/italya-basbakani-renzi-ankara-da-6766237-haberi/",
      cav=TR + " (Italian). Haberler (AA) and Haber7 print the same text, one AA wire. The sentences that follow concern Italian-Turkish relations and EU accession.",
      med="Haberler (AA) and Haber7, 11 Dec 2014 (Turkish translation of the entry)",
      urls=["https://www.haberler.com/guncel/italya-basbakani-renzi-ankara-da-6766237-haberi/", "https://www.haber7.com/dis-politika/haber/1245290-italya-basbakani-renzi-ankarada"],
      ev="J", link="Matteo Renzi"),
 dict(id="rutte-2022-03-22-book", voice="Mark Rutte", role="Prime Minister of the Netherlands; entry in the Anıtkabir special book", c="Netherlands", cn="Netherlands",
      dom="politics", date="2022-03-22", mirror=None, pol="instrumental", inten=1,
      saw="Feels privileged to return to Anıtkabir to honour Atatürk's memory; the rest of the entry is about Dutch-Turkish ties.",
      q="Mustafa Kemal Atatürk'ün hatırasını onurlandırmak için yeni bir fırsatla Anıtkabir'e geri geldiğim için ayrıcalıklı hissediyorum.",
      qurl="https://www.turkinfo.nl/hollanda-basbakani-rutte-anitkabir-i-ziyaret-etti/32026",
      cav=TR + " (English). TürkInfo.nl and İktibas Dergisi print the same AA text. 'Geri geldiğim' means he had been there before. As NATO Secretary-General Rutte visited Anıtkabir again on 25 Nov 2024 (Akşam, AA), but no entry text was found.",
      med="TürkInfo.nl and İktibas Dergisi (AA), 22 Mar 2022 (Turkish translation of the entry)",
      urls=["https://www.turkinfo.nl/hollanda-basbakani-rutte-anitkabir-i-ziyaret-etti/32026", "https://iktibasdergisi.com/2022/03/22/hollanda-basbakani-rutte-anitkabirde/"],
      ev="J", link="Mark Rutte"),
 dict(id="tokayev-2022-05-10-book", voice="Kassym-Jomart Tokayev", role="President of Kazakhstan; entry in the Anıtkabir special book", c="Kazakhstan", cn="Kazakhstan",
      dom="politics", date="2022-05-10", mirror=None, pol="admiring", inten=1,
      saw="Remembers Atatürk, founder of the Turkish Republic, with mercy and sends respects to the Turkish people 'whose roots are one with ours'.",
      q="Türkiye Cumhuriyeti kurucusu Mustafa Kemal Atatürk'ü rahmetle anıyor, köklerimiz bir Türk halkına saygılarımı iletiyorum.",
      qurl="https://www.haberler.com/guncel/kazakistan-cumhurbaskani-tokayev-anitkabir-i-14930199-haberi/",
      cav="Turkish rendering (AA) of an entry probably written in Kazakh or Russian; the original is not located. Haberler (AA) and TRT Haber print the same text, one AA wire. The remainder wishes lasting friendship and cooperation.",
      med="Haberler (AA) and TRT Haber, 10 May 2022 (Turkish translation of the entry)",
      urls=["https://www.haberler.com/guncel/kazakistan-cumhurbaskani-tokayev-anitkabir-i-14930199-haberi/", "https://www.trthaber.com/foto-galeri/kazakistan-cumhurbaskani-anitkabiri-ziyaret-etti/46534.html"],
      ev="J", link="Kassym-Jomart Tokayev"),
 dict(id="ilham-aliyev-2024-02-19-book", voice="Ilham Aliyev", role="President of Azerbaijan; entry in the Anıtkabir special book", c="Azerbaijan", cn="Azerbaijan",
      dom="politics", date="2024-02-19", mirror=None, pol="admiring", inten=2,
      saw="Calls Atatürk the great son of the Turkic world, a gifted commander and a genius leader who inscribed the Republic in world history.",
      q="Türk dünyasının büyük evladı, yetenekli komutan ve dahi lider Gazi Mustafa Kemal Atatürk'ün aziz hatırasını en içten saygı ve ihtiramla anıyorum.",
      qurl="https://www.aa.com.tr/tr/gundem/azerbaycan-cumhurbaskani-aliyev-anitkabiri-ziyaret-etti/3141615",
      cav="Turkish rendering (AA) of an entry probably written in Azerbaijani; the original is not located. AA and Kıbrıs Gazetesi print it, one AA wire (the second has a typo, 'edebi' for 'ebedi'). The entry goes on to say that Atatürk 'knew Azerbaijan's joy as his own joy and its grief as his own grief'. Aliyev signed the book on earlier visits (5 Nov 2008, 12 Nov 2013, 15 Jan 2015, 25 Apr 2018 per the Turkish Wikipedia list); those entries were not found.",
      med="AA and Kıbrıs Gazetesi, 19 Feb 2024 (Turkish translation of the entry)",
      urls=["https://www.aa.com.tr/tr/gundem/azerbaycan-cumhurbaskani-aliyev-anitkabiri-ziyaret-etti/3141615", "https://kibrisgazetesi.com/aliyev-anitkabiri-ziyaret-etti/"],
      ev="J", link="Ilham Aliyev"),
 dict(id="boris-johnson-2016-09-27-book", voice="Boris Johnson", role="British Foreign Secretary; entry in the Anıtkabir special book", c="United Kingdom", cn="United Kingdom",
      dom="diplomacy", date="2016-09-27", mirror="modernization-poster-child", pol="admiring", inten=2,
      saw="Calls it a privilege to return to his ancestors' land and honour the founder of modern, free, democratic Turkey, whose vision has been realised.",
      q="Atalarımın topraklarına dönmek, modern, özgür ve demokratik Türkiye'nin kurucusuna saygılarımı sunmak ve Türkiye'nin dünyanın büyük ulusları arasında yeralmasıyla onun vizyonunun nasıl gerçekleştirildiğini görmek büyük bir ayrıcalık",
      qurl="https://www.milliyet.com.tr/siyaset/johnson-anitkabir-ozel-defterine-yazdi-atalarimin-topraklarina-donmek-2317489",
      cav=TR + ". Milliyet and Habertürk print the same AA text. Johnson's great-grandfather Ali Kemal was an Ottoman minister who opposed the national struggle (Habertürk notes it). Foreign Secretary here, later Prime Minister. Atatürk is not named in the quoted line; 'the founder' is the reference.",
      med="Milliyet and Habertürk, 27 Sep 2016 (AA; Turkish translation of the entry)",
      urls=["https://www.milliyet.com.tr/siyaset/johnson-anitkabir-ozel-defterine-yazdi-atalarimin-topraklarina-donmek-2317489", "https://www.haberturk.com/dunya/haber/1302284-ingiltere-disisleri-bakani-johnson-anitkabiri-ziyaret-etti"],
      ev="J", link="Boris Johnson"),
 dict(id="kristersson-2022-11-08-book", voice="Ulf Kristersson", role="Prime Minister of Sweden; entry in the Anıtkabir special book", c="Sweden", cn="Sweden",
      dom="politics", date="2022-11-08", mirror=None, pol="instrumental", inten=1,
      saw="Honoured to visit the Republic founded by Atatürk nearly a century ago; recalls photographs of Atatürk with the Swedish crown prince in 1934.",
      q="It is a great honour for me to visit the Republic of Turkiye, which was founded by Ataturk nearly 100 years ago",
      qurl="https://www.middleeastmonitor.com/20221108-turkiye-swedish-pm-visits-ataturk-mausoleum/", english=True,
      cav="English as printed by Middle East Monitor (an Anadolu Agency photo); Odatv prints the Turkish rendering ('Yaklaşık 100 yıl önce tarafınızca kurulan Türkiye Cumhuriyeti'ni ziyaret etmek benim için büyük bir onurdur'), where the entry addresses Atatürk directly ('founded by you'). Whether the English is the original or an AA translation back from Turkish is not established. Written during the NATO accession row; the entry goes on to mention photographs of Atatürk with Crown Prince Gustaf Adolf at the 1934 opening of the Swedish Embassy.",
      med="Middle East Monitor (English) and Odatv (Turkish), 8 Nov 2022",
      urls=["https://www.middleeastmonitor.com/20221108-turkiye-swedish-pm-visits-ataturk-mausoleum/", "https://www.odatv.com/guncel/isvec-basbakani-kristersson-anitkabiri-ziyaret-etti-257560"],
      ev="J", link="Ulf Kristersson"),
 dict(id="lee-jae-myung-2025-11-24-book", voice="Lee Jae-myung", role="President of South Korea; entry in the Anıtkabir special book", c="South Korea", cn="South Korea",
      dom="politics", date="2025-11-24", mirror=None, pol="instrumental", inten=1,
      saw="Commemorates Atatürk and pledges to advance together for the common prosperity of the two 'blood-brother' nations.",
      q="Atatürk'ü anarak, kan bağıyla bağlı kardeş uluslarımızın ortak refahı için birlikte ilerleyeceğiz.",
      qurl="https://www.aa.com.tr/tr/gundem/guney-kore-devlet-baskani-lee-anitkabiri-ziyaret-etti/3752554",
      cav="Turkish rendering (AA) of a Korean entry; the original is not located. AA, Hürriyet, Odatv, Haberler, Nefes and A Haber print the same sentence, one AA wire. Courtesy line; no evaluation of Atatürk.",
      med="AA, Hürriyet, Odatv and Haberler, 24 Nov 2025 (Turkish translation of the entry)",
      urls=["https://www.aa.com.tr/tr/gundem/guney-kore-devlet-baskani-lee-anitkabiri-ziyaret-etti/3752554", "https://www.hurriyet.com.tr/dunya/guney-kore-devlet-baskani-lee-anitkabiri-ziyaret-etti-43030546", "https://www.odatv.com/dunya/guney-kore-lideri-lee-jae-myung-anitkabiri-ziyaret-etti-120124701"],
      ev="J", link="Lee Jae-myung"),
 dict(id="dan-caine-2026-07-07-book", voice="Dan Caine", role="Chairman of the US Joint Chiefs of Staff; entry in the Anıtkabir special book", c="United States", cn="United States",
      dom="military", date="2026-07-07", mirror=None, pol="admiring", inten=2,
      saw="Writes for the delegation of his deep respect and admiration for Atatürk, the great and distinguished leader of the Republic.",
      q="Türkiye Cumhuriyeti'nin büyük ve seçkin lideri Mustafa Kemal Atatürk'e duyduğum derin saygı ve hayranlık nedeniyle, Amerikan halkının bir temsilcisi olarak Türk milletine ve bu büyük lidere saygılarımı sunmaktan büyük onur ve gurur duyuyorum.",
      qurl="https://www.dunya.com/gundem/abd-genelkurmay-baskani-dan-caine-anitkabiri-ziyaret-etti-haberi-831301",
      cav=TR + ". Written 'on behalf of the delegation' during the 36th NATO Heads of State and Government Summit in Ankara. Dünya, Habertürk (credited AA), Gazete Gerçek and Haberler (23 Jul 2026 repost) print the same text, one AA wire. The wording resembles Tillerson's 2017 entry ('büyük ve seçkin lideri', 'derin saygı ve hayranlık', 'bir temsilcisi'), probably a protocol template drafted by the embassy.",
      med="Dünya, Habertürk (AA), Gazete Gerçek and Haberler, July 2026 (Turkish translation of the entry)",
      urls=["https://www.dunya.com/gundem/abd-genelkurmay-baskani-dan-caine-anitkabiri-ziyaret-etti-haberi-831301", "https://www.haberturk.com/dunya/abd-genelkurmay-baskani-dan-caine-anitkabir-i-ziyaret-etti-3896794", "https://www.gazetegercek.com.tr/abd-genelkurmay-baskani-dan-caine-anitkabir-ozel-defterine-ne-yazdi/230082"],
      ev="J", link="Dan Caine"),
]

for r in R:
    if r.get("english"):
        check(r["id"], r["q"], r["qurl"])
    else:
        check(r["id"], r["q"], r["qurl"])
    for u in r["urls"]:
        if u not in PAGES:
            print("WARN: source not banked:", r["id"], u)

recs = []
for r in R:
    eng = r.get("english")
    recs.append({
        "id": r["id"], "voice": r["voice"], "voice_type": "person", "role": r["role"],
        "country": r["c"], "country_now": r["cn"], "domain": r["dom"], "date": r["date"], "era": "posthumous",
        "mirror": r["mirror"], "polarity": r["pol"], "intensity": r["inten"], "what_they_saw": r["saw"],
        "quote": r["q"] if eng else T + r["q"], "artifact": "quote", "evidence": r["ev"], "mediated_by": r["med"],
        "caveat": r["cav"], "node": NODE, "sources": r["urls"],
    })
with open(os.path.join(STATE, "gazes_anitkabir.jsonl"), "w", encoding="utf-8") as f:
    for x in recs:
        f.write(json.dumps(x, ensure_ascii=False) + "\n")

with open(os.path.join(STATE, "ledger_anitkabir.md"), "w", encoding="utf-8") as f:
    f.write("| Claim | Node | Status | Sources | Next step |\n|---|---|---|---|---|\n")
    for r in R:
        f.write("| %s (%s, %s): %s | %s | verified %s (Turkish press report of the Anıtkabir special book entry; %s) | %s | %s |\n" % (
            r["voice"], r["role"].split(";")[0], r["date"], (r["q"][:100] + ("…" if len(r["q"]) > 100 else "")), NODE, r["ev"],
            "English as printed" if r.get("english") else "translation",
            " ; ".join(r["urls"]), "original-language text of the entry (Anıtkabir Özel Defteri volume, ed. Recep Cengiz) if reachable"))

people = {
 "Barack Obama": ("President of the United States, 2009–2017", "American", "1961–", "admirer (diplomatic)",
    "On 6 April 2009, his first visit to Turkey as President, he wrote in the Anıtkabir book that Atatürk's 'vision, tenacity and courage' put Turkey on the path of democracy and that his legacy inspires generations. He addressed the Assembly the same day."),
 "Hillary Clinton": ("US Secretary of State, 2009–2013", "American", "1947–", "courtesy",
    "On 7 March 2009, as Secretary of State, she signed the Anıtkabir book with a line of respect to 'the founder of this great country'."),
 "John Kerry": ("US Secretary of State, 2013–2017", "American", "1943–", "admirer (diplomatic)",
    "On 2 March 2013 he wrote in the Anıtkabir book of Atatürk as a soldier and statesman who pioneered education and independence."),
 "Rex Tillerson": ("US Secretary of State, 2017–2018", "American", "1952–", "admirer (diplomatic)",
    "On 30 March 2017 he wrote in the Anıtkabir book of his deep respect and admiration for Atatürk, 'the great and eminent leader'."),
 "Antony Blinken": ("US Secretary of State, 2021–2025", "American", "1962–", "courtesy",
    "On 20 February 2023, two weeks after the earthquakes, he wrote in the Anıtkabir book of his honour in paying respects to Atatürk and the Turkish nation."),
 "Isaac Herzog": ("President of Israel, 2021–", "Israeli", "1960–", "admirer (diplomatic)",
    "On his March 2022 visit he wrote in the Anıtkabir book of 'the great visionary' Atatürk and his legacy of progress and peace, and added a Hebrew verse from the Psalms."),
 "François Hollande": ("President of France, 2012–2017", "French", "1954–", "admirer (diplomatic)",
    "On 27 January 2014, the first state visit by a French president in 22 years, he wrote in the Anıtkabir book to the statesman who rebuilt Turkey after great suffering and revived friendship with France."),
 "Matteo Renzi": ("Prime Minister of Italy, 2014–2016", "Italian", "1975–", "courtesy",
    "On 11 December 2014 he wrote in the Anıtkabir book of his deep respect for Atatürk, 'founder of modern Turkey', and his support for Turkey's EU path."),
 "Mark Rutte": ("Prime Minister of the Netherlands, 2010–2024; NATO Secretary-General from 2024", "Dutch", "1967–", "courtesy",
    "On 22 March 2022 he wrote in the Anıtkabir book that he felt privileged to return and honour Atatürk's memory."),
 "Kassym-Jomart Tokayev": ("President of Kazakhstan, 2019–", "Kazakh", "1953–", "admirer (kinship)",
    "On 10 May 2022 he wrote in the Anıtkabir book that he remembered Atatürk with mercy and sent respects to the Turkish people, 'whose roots are one with ours'."),
 "Ilham Aliyev": ("President of Azerbaijan, 2003–", "Azerbaijani", "1961–", "admirer (kinship)",
    "On 19 February 2024 he wrote in the Anıtkabir book of Atatürk as 'the great son of the Turkic world, a gifted commander and genius leader'."),
 "Boris Johnson": ("British Foreign Secretary 2016–2018; Prime Minister 2019–2022", "British", "1964–", "admirer (diplomatic)",
    "On 27 September 2016, as Foreign Secretary, he wrote in the Anıtkabir book of honouring 'the founder of modern, free and democratic Turkey'. He is a great-grandson of Ali Kemal, who opposed the national struggle."),
 "Ulf Kristersson": ("Prime Minister of Sweden, 2022–", "Swedish", "1963–", "courtesy",
    "On 8 November 2022 he wrote in the Anıtkabir book of the honour of visiting the Republic Atatürk founded nearly a century earlier."),
 "Lee Jae-myung": ("President of South Korea, 2025–", "South Korean", "1963–", "courtesy",
    "On 24 November 2025 he wrote in the Anıtkabir book, 'commemorating Atatürk', of advancing together with the 'blood-brother' Turkish nation."),
 "Dan Caine": ("Chairman of the US Joint Chiefs of Staff, 2025–", "American", "1968–", "admirer (diplomatic)",
    "On 7 July 2026, during the NATO summit in Ankara, he wrote in the Anıtkabir book of his deep respect and admiration for Atatürk, 'the great and distinguished leader'."),
}
for name, (role, nat, life, stance, desc) in people.items():
    if os.path.exists(os.path.join(HERE, "vault", "People", name + ".md")):
        continue
    extra = " See also [[Ali Kemal]]." if name == "Boris Johnson" else ""
    person(name, role=role, nat=nat, life=life, stance=stance, tags=["verified", "head-of-state", "anitkabir"],
           body="%s\n\nSee [[%s]] and [[Anıtkabir]].%s\n\n## Sources\n- Turkish press reports of the Anıtkabir special book entry; see [[%s]].\n" % (desc, NODE, extra, NODE))

body = ["""
Round 15 found that Turkish news sites print what visiting foreign leaders write in the Anıtkabir special book (see [[%s]]). Round 16 adds
fifteen entries by heads of state, prime ministers, foreign ministers and one general, 2009–2026, again from Turkish wire copy (AA, DHA, İHA)
republished by several outlets. Every quote below was checked against the fetched page text. All are Turkish translations except
Kristersson's, which Middle East Monitor printed in English; no original-language text has been located. Where agencies disagree on the
Turkish wording (Obama, Tillerson) the note says so: the exact English is not fixed.

## What they chose to say

- **The US, four secretaries and a general:** [[Hillary Clinton]] (2009) pays respects to 'the founder of this great country'; [[John Kerry]] (2013) calls Atatürk 'a soldier and statesman who pioneered education and independence'; [[Rex Tillerson]] (2017) writes of 'deep respect and admiration' for 'the great and eminent leader'; [[Antony Blinken]] (2023) offers a courtesy line two weeks after the earthquakes; [[Dan Caine]] (2026) repeats the Tillerson formula almost word for word on behalf of the delegation, which suggests a protocol template. [[Barack Obama]] (2009) is the fullest: Atatürk's 'vision, tenacity and courage put the Republic of Turkey on the path of democracy' and his legacy 'continues to inspire the whole world'.
- **Europe:** [[François Hollande]] (2014) addresses 'the statesman who, after great suffering, built modern Turkey'; [[Matteo Renzi]] (2014) calls him 'founder of modern Turkey' and promises support on the EU road; [[Mark Rutte]] (2022) feels 'privileged' to return to honour his memory; [[Ulf Kristersson]] (2022) speaks of the Republic Atatürk founded and recalls photographs of him with the Swedish crown prince in 1934; [[Boris Johnson]] (2016) writes of returning to his ancestors' land and of the founder of 'modern, free and democratic Turkey'.
- **Kinship and the Turkic world:** [[Ilham Aliyev]] (2024) writes the longest and warmest entry, 'genius leader' and 'great son of the Turkic world'; [[Kassym-Jomart Tokayev]] (2022) sends respects to a people 'whose roots are one with ours'.
- **Peace and the Middle East:** [[Isaac Herzog]] (2022) calls Atatürk 'the great visionary' and speaks of the wisdom of his legacy of progress and peace, then adds a Hebrew verse from the Psalms.
- **Courtesy from Asia:** [[Lee Jae-myung]] (2025) writes 'commemorating Atatürk' and pledges common prosperity with the 'blood-brother' nation.

## How to read these

The book is signed on a protocol visit, so the lines are chosen by the visitor's staff for the host. Praise is cheap here; what is
telling is the angle each visitor picks: democracy (Obama), education (Kerry), the European road (Renzi), kinship (Aliyev, Tokayev),
family history (Johnson), peace (Herzog). Several entries name Atatürk only by the epithet 'founder' (Clinton, Hollande, Johnson), and
the quoted lines are the visitors' own choice of what to say before the tomb.

"""% PRIOR]
for r in R:
    body.append("\n## %s (%s)\n" % (r["voice"], r["date"]))
    body.append("*%s*\n" % r["saw"])
    body.append("> %s\n" % (r["q"] if r.get("english") else T + r["q"]))
    body.append("%s Evidence %s. See [[%s]].\n" % (r["cav"], r["ev"], r["link"]))

body.append("""
## Dry ends and leads (round 16)

- **Tito, 13 April 1954:** an Instagram post (yugoslavyagocmenleri, 9 Nov 2023) and a column by Can Hacıoğlu (2eylul.com.tr, 'Mareşal Tito'nun önemi') give the line 'Sizi hayatım boyunca daima ilham kaynağı olarak yaşattım' ('I have kept you alive as an inspiration all my life'), written in a white uniform. No 1954 newspaper or book citation found, so it is not stored. Milliyet, 14 Apr 1954, p. 1 is the Wikipedia reference for the visit.
- **Koizumi, 10 January 2006:** Hürriyet (AA) prints the entry ('Türkiye Cumhuriyeti'nin kurucusu büyük Atatürk'e en derin saygılarım ve Türkiye-Japonya dostluğunun daha da gelişmesi temennisiyle'), but only one outlet was found, so it is held.
- **Stubb, 1 October 2024:** AA, Patronlar Dünyası and Haber Ekspres print the entry; Atatürk appears only as founder of the Republic in a line about the 1924 Finnish-Turkish treaty, so it was left out as a bare mention.
- **Entries not found:** Medvedev (2010), Abe (2013), Blair, Cameron (İHA, only 'signed'), Macron, Modi, Meloni, Sánchez, Orbán, Zelensky, Nazarbayev, Lukashenko (16 Apr 2019), Mirziyoyev (19 Feb 2020, signed; text not printed), Nawrocki (23 Jun 2026, signed), Rousseff (7 Oct 2011), Correa (15 Mar 2012), Prabowo, Anwar Ibrahim (Jan 2026), Duda, Vučić, Niinistö. Dan Caine's NATO-summit visit is the only one of the July 2026 delegations that printed text for a leader; the Luxembourg permanent representative also wrote that 'Yurtta sulh, cihanda sulh' reflects the alliance's spirit.
- **Pre-1990 entries (Heuss 1957, Sukarno 1959, Ayub Khan 1959, Nixon 1956, Adenauer 1954, Hussein 1960):** DuckDuckGo found no online text; the Atatürk Araştırma Merkezi Dergisi article on Indonesia (atamdergi.gov.tr 1071) has no mention of the visit. The printed volumes of *Anıtkabir Özel Defteri* (ed. Recep Cengiz, 1953–) and Milliyet/Cumhuriyet microfilm for the visit days are the way in.
- **Academic compilations:** DuckDuckGo queries for DergiPark articles on the book returned only a stylistic study of vol. 23 (Öner, Çukurova) and library catalogue records; no article that prints foreign leaders' entries was found.
- **Celebrities:** Elon Musk (9 Nov 2017), Aamir Khan (17 Oct 2017), Kevin Costner (29 Oct 2007) and Douglas Fairbanks Jr. (1954) appear in the Turkish Wikipedia list; no text of an entry was found.

## Sources
- Turkish press reports (Habertürk, T24, Dengegazetesi, NTV, Hürriyet, Akşam, Cumhuriyet, Sözcü, Haberler, Sondakika, TGRT Haber, Şehitler Ölmez, Yurt Gazetesi, AA, Dünya, Haber7, TürkInfo.nl, İktibas Dergisi, TRT Haber, Kıbrıs Gazetesi, Milliyet, Odatv, Gazete Gerçek) and Middle East Monitor: the exact URLs are listed under each record.
- Turkish Wikipedia, 'Anıtkabir ziyaretçileri listesi' (dates of visits only).
""")

note("Events", NODE,
     {"type": "event", "when": "2009–2026",
      "tags": ["event", "verified", "heads-of-state", "anitkabir"]},
     "\n".join(body))
print("ok", len(recs), "records")
