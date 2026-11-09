# -*- coding: utf-8 -*-
# Census round 11 (Nov 2026) — foreign heads of state and parliamentary leaders speaking in the TBMM plenary.
# Source: TBMM, "Tarihe Düşülen Notlar-2: Yabancı Devlet Adamlarının Genel Kurul Konuşmaları" (Feb 2012),
# https://acikerisim.tbmm.gov.tr/handle/11543/122 . Speeches are printed in Turkish as in the TBMM minutes.
# Speaker, office and date are taken from the book's own section headings. Page numbers are PDF pages
# (printed page = PDF page - 11). Quotes were read from rendered page images (PDFKit, tools/.state/round11/).
# The script writes the Events note and the round-11 gazes / ledger files; it also checks every quote
# against the PDF text layer (tools/.state/round11/full.txt) before writing.
import json, os, re, sys
from _lib import note

HERE = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(HERE, "tools", ".state", "round11")
H = "https://acikerisim.tbmm.gov.tr/handle/11543/122"
NODE = "Foreign Statesmen Address the Assembly, 1956–2010"
MED = "TBMM minutes (Turkish interpretation)"

# id, voice, role, country, country_now, domain, date, mirror, polarity, intensity, saw, quote, pdfpage, extra caveat,
# translation, person-note link (or None), headline for the note
R = [
 dict(id="iskender-mirza-1956", voice="İskender Mirza", role="President of Pakistan", c="Pakistan", cn="Pakistan",
      dom="politics", date="1956-07-16", mirror="anti-colonial-liberator", pol="admiring", inten=2,
      saw="Ranks Atatürk among the world's heroes; says the subcontinent's Muslims also took him for a hero and sang of his deeds.",
      q="Atatürk tarihin daima şükranla yâd etmekle şeref kazanacağı ve milletinin mukadderatını tâyindeki hissesi ebediyen yaşayacak olan dünya kahramanları sınıfına dâhildir.",
      pp=14, tr="Atatürk belongs to the class of world heroes whom history will honour with gratitude and whose share in deciding his nation's destiny will live for ever.",
      extra="The same speech pairs him with Jinnah (PDF p. 15). Heading: 'Pakistan Reisicumhuru İskender Mirza', Doksanıncı İnikat, 16 Temmuz 1956."),
 dict(id="muzaffar-ali-1957", voice="Nawab Muzaffar Ali", role="Head of the Pakistani parliamentary delegation", c="Pakistan", cn="Pakistan",
      dom="politics", date="1957-06-07", mirror="anti-colonial-liberator", pol="admiring", inten=1,
      saw="Names Atatürk and Jinnah as the sources of Pakistan's inspiration and says both worked and died for their countries' independence.",
      q="Bu ilham membaını Türkiye ve Pakistan’ın büyük şahsiyetleri olan Atatürk ve Mehmet Ali Cinnah’a karşı duyduğumuz derin hayranlık teşkil etmektedir.",
      pp=18, tr="The source of this inspiration is the deep admiration we feel for Atatürk and Muhammad Ali Jinnah, the great figures of Turkey and Pakistan.",
      extra="Book heading: 'Pakistan Parlamento Heyeti Reisi Nevvab Muzaffer Ali', 7 Haziran 1957. Spelling of the name follows the book.", link="Muhammad Ali Jinnah"),
 dict(id="podgorny-1965", voice="Nikolay Podgorny", role="Head of the Soviet parliamentary delegation", c="Soviet Union", cn="Russia",
      dom="diplomacy", date="1965-01-05", mirror=None, pol="instrumental", inten=2,
      saw="Recalls Atatürk's message of admiration for the Russian people and calls for a return to the good traditions of the Lenin–Atatürk era.",
      q="Türk Milletinin önderi Kemal Atatürk, o zaman vuku bulan hâdiselerin azametini lâyıkıyla takdir etmişti.",
      pp=36, tr="The leader of the Turkish nation, Kemal Atatürk, duly appreciated the magnitude of the events that then took place.",
      extra="Podgorny goes on to quote Atatürk's message to the Soviet government and his 1935 CHP congress remark on Soviet–Turkish friendship (PDF p. 38: 'Lenin ve Atatürk devrinde doğmuş olan iyi geleneklere dönmek zamanı gelmiştir'). Serves a 1965 Soviet bid for better relations. Book heading: 'Sovyet Parlamento Heyeti Başkanı Nikolay Podgorni', 33. Birleşim, 5 Ocak 1965."),
 dict(id="bourguiba-1965", voice="Habib Bourguiba", role="President of Tunisia", c="Tunisia", cn="Tunisia",
      dom="politics", date="1965-03-25", mirror="anti-colonial-liberator", pol="conflicted", inten=2,
      saw="Calls Sakarya Atatürk's miracle and Mustafa Kemal the model hero, yet explains Arab reserve by Atatürk's stance toward religion.",
      q="Sakarya Harbi, Sakarya Zaferi, 20 yaşımın en kuvvetli hâtırası olmuştur.",
      pp=43, tr="The Battle of Sakarya, the Victory of Sakarya, became the strongest memory of my twentieth year.",
      extra="Same speech: 'Sizin Kemalist ihtilâliniz ise, bizlere maya oldu' (PDF p. 48, 'your Kemalist revolution became leaven for us'), and on PDF p. 44 the Arab hesitation is traced to 'bu liderin din ve din müessesesine karşı takındığı tavırlar' (this leader's stance toward religion and religious institutions), with Bourguiba dissenting from the 'very radical judgments'. Heading: 'Tunus Cumhurbaşkanı Habib Burgiba', 25 Mart 1965. Existing person note covers his later Kemalist programme.",
      link="Habib Bourguiba"),
 dict(id="lei-jieqiong-1984", voice="Lei Jieqiong", role="Standing Committee member, National People's Congress of China", c="China", cn="China",
      dom="politics", date="1984-12-05", mirror="emancipator-patriarch", pol="admiring", inten=2,
      saw="Credits Atatürk's initiative with giving Turkish women the vote and says she holds him in deep respect.",
      q="Türk kadınına siyasî haklar tanınmasında silinmez katkılar yapan Yüce Atatürk’e derin saygılar duyuyor",
      pp=50, tr="[We] feel deep respect for the Great Atatürk, who made indelible contributions to the granting of political rights to Turkish women.",
      extra="Speech marked the 50th anniversary of Turkish women's suffrage (1934). Heading: 'Çin Halk Cumhuriyeti Ulusal Halk Kongresi Sürekli Komite Üyesi Lei Jieqiong', 5 Aralık 1984."),
 dict(id="kobayashi-1985", voice="Susumu Kobayashi", role="Member of the Japanese House of Representatives", c="Japan", cn="Japan",
      dom="politics", date="1985-04-23", mirror="modernization-poster-child", pol="admiring", inten=2,
      saw="After visiting Anıtkabir, says he is full of deep respect and admiration for the leader who saved Turkey from national catastrophe.",
      q="bu tarihî lidere en derin saygı ve hayranlık hisleriyle dolu bulunmaktayım.",
      pp=53, tr="I am filled with the deepest feelings of respect and admiration for this historic leader.",
      extra="Heading: 'Japonya Temsilciler Meclisi Üyesi Susumu Kobayashi', 23 Nisan 1985; speech begins PDF p. 52.", link="Anıtkabir"),
 dict(id="zahir-ismail-1988", voice="Tan Sri Dato Mohd Zahir Hacı İsmail", role="Speaker of the Malaysian House of Representatives", c="Malaysia", cn="Malaysia",
      dom="politics", date="1988-04-23", mirror="anti-colonial-liberator", pol="admiring", inten=2,
      saw="Says news of Atatürk's deeds reached colonial Malaya, his pictures hung in homes, and he was himself a fervent admirer in his youth.",
      q="Ben kendim, gençliğimde, ateşli bir Atatürk hayranı idim. Atatürk bir dahi ve en çok muhtaç olduğu anda Türk Milletine Tanrı’nın bir ihsanıdır.",
      pp=61, tr="I myself, in my youth, was an ardent admirer of Atatürk. Atatürk is a genius and a gift of God to the Turkish nation at its moment of greatest need.",
      extra="Same speech: 'O bizi özgür olmağa cesaretlendirdi' (he encouraged us to be free); The speech gives 1947 for liberation from colonial rule, as printed; not checked here. Heading: 'Malezya Millet Meclisi Başkanı Tan Sri Dato Mohd Zahir Hacı İsmail', 23 Nisan 1988."),
 dict(id="kelemen-1991", voice="András Kelemen", role="Hungarian Deputy Minister for Social Security", c="Hungary", cn="Hungary",
      dom="politics", date="1991-04-23", mirror="nation-forge-template", pol="instrumental", inten=1,
      saw="Presents post-communist Hungary as following the path Turkey took under the great leader Kemal Atatürk, its 'big sister'.",
      q="Böylece Macaristan, aynen büyük “ablası” Türkiye’nin 71 yıl önce Büyük önder Kemal Atatürk önderliğinde yaptığı gibi, hürriyet ve kendi kendini yönetme yolunu seçmiş bulunmaktadır.",
      pp=71, tr="Thus Hungary, exactly as its great 'elder sister' Turkey did 71 years ago under the great leader Kemal Atatürk, has chosen the path of freedom and self-government.",
      extra="Also: 'Kemal Atatürk ruhunun korunduğunu görmekteyiz' (PDF p. 72). Heading: 'Macar Sosyal Güvenlik Bakan Yardımcısı Andras Kelemen', 23 Nisan 1991."),
 dict(id="elcibey-1992", voice="Ebülfeyz Elçibey", role="President of Azerbaijan", c="Azerbaijan", cn="Azerbaijan",
      dom="politics", date="1992-06-26", mirror="nation-forge-template", pol="admiring", inten=2,
      saw="Says Azerbaijan's first step is Mustafa Kemal's path, then a state; calls the republic under Mustafa Kemal's leadership a rising voice.",
      q="hele ilkin yolumuz Mustafa Kemal’in yoludur, sonra da devletimizi kuracağız.",
      pp=83, tr="Our first road is Mustafa Kemal's road; after that we will build our state.",
      extra="Also quotes 'Büyük Mustafa Kemal' on building a modern republic. Heading: 'Azerbaycan Cumhurbaşkanı Ebulfez Elçibey', 26 Haziran 1992; name spelt 'Ebulfez Elçibey' in the book. Delivery language not stated by the book."),
 dict(id="haydar-aliyev-1994", voice="Haydar Aliyev", role="President of Azerbaijan", c="Azerbaijan", cn="Azerbaijan",
      dom="politics", date="1994-02-09", mirror="nation-forge-template", pol="admiring", inten=3,
      saw="Bows before the memory of Mustafa Kemal Atatürk as the great figure of the whole Turkic world, who laid the foundation of the Turkish republic.",
      q="böyük insan, bütün Türk dünyasının böyük şahsiyeti Mustafa Kemal Atatürk’ü bir daha yâd edirem; onun gördüğü işlere, onun koyduğu yola öz hörmetimi ve ihtiramımı bildirerem, onun hatırası karşısında baş eğirem.",
      pp=97, tr="I remember once again the great man, the great figure of the whole Turkic world, Mustafa Kemal Atatürk; I express my respect and reverence for his work and the road he laid down, and bow before his memory.",
      extra="Printed in Azerbaijani forms with Turkish glosses in brackets, so the speech was delivered in Azerbaijani Turkish. Heading: 'Azerbaycan Cumhurbaşkanı Haydar Aliyev', 9 Şubat 1994 (PDF pp. 96-97; this passage on 97). He returned on 6 Mayıs 1997 (PDF p. 106ff: 'Böyük Önder Mustafa Kemal Atatürk', visit to Anıtkabir) and 13 Mart 2001 (PDF p. 149ff: 'beşer tarihinin meydana çıkardığı en büyük insanlardan biri'; announces an Atatürk-heritage research centre, p. 156-157) with the same praise; only the 1994 speech is stored as the record. He also cites Atatürk's tenth-anniversary speech at length (PDF p. 101)."),
 dict(id="denktas-1998", voice="Rauf Denktaş", role="President of the Turkish Republic of Northern Cyprus", c="Northern Cyprus (TRNC)", cn="Northern Cyprus (TRNC)",
      dom="politics", date="1998-04-23", mirror="nation-forge-template", pol="instrumental", inten=1,
      saw="Calls the Assembly 'Atatürk's Assembly' and says Turkish Cypriots, as Atatürk's children, have lived by his peace principle while defending their rights.",
      q="Atatürk çocukları olarak, ömrümüzü, bu düstur uğruna, mücadeleyle geçirdik.",
      pp=131, tr="As Atatürk's children, we have spent our lives in struggle for this maxim.",
      extra="Maxim is 'yurtta sulh, cihanda sulh'. Cyprus-negotiation context (the claim of sovereignty for Turkish Cypriots). Heading: 'Kuzey Kıbrıs Türk Cumhuriyeti Cumhurbaşkanı Rauf Denktaş', 23 Nisan 1998. Denktaş also spoke on 21 Ocak 1997 (PDF p. 124, an Atatürk saying on sovereignty) and 15 Nisan 2004 (PDF p. 204, 'Büyük Atatürk’ün Yüce Meclisinde')."),
 dict(id="clinton-1999", voice="Bill Clinton", role="President of the United States", c="United States", cn="United States",
      dom="politics", date="1999-11-15", mirror="modernization-poster-child", pol="admiring", inten=2,
      saw="Recalls Atatürk as the republic's great founder who captured American imagination and says everyone in the chamber is there thanks to him.",
      q="Bugün, hepimiz, Mustafa Kemal Atatürk’ün sayesinde buradayız.",
      pp=143, tr="Today we are all here thanks to Mustafa Kemal Atatürk.",
      extra="Clinton says he came 'during a national tragedy' to convey American solidarity. The previous page (PDF p. 142) has 'Türkiye Cumhuriyetinin büyük kurucusu Kemal Atatürk, Amerika’nın hayallerini, cesur reformlarıyla yakaladı' and the 'Second George Washington' / Time cover remark; he also says Atatürk's greatness grows because he opened Turkey to the world. Heading: 'Amerika Birleşik Devletleri Başkanı William Jefferson Clinton', 15 Kasım 1999."),
 dict(id="prodi-2004", voice="Romano Prodi", role="President of the European Commission", c="European Union", cn="European Union",
      dom="diplomacy", date="2004-01-15", mirror="modernization-poster-child", pol="instrumental", inten=1,
      saw="Says Atatürk set reaching modern-civilisation standards as the clearest goal and that his vision was a full place in the European family of nations.",
      q="O’nun Türkiye vizyonu, Avrupa uluslar ailesi içerisinde tam olarak yer almaktı.",
      pp=180, tr="His vision of Turkey was to take a full place within the family of European nations.",
      extra="Accession-negotiation context; an EU-side reading of Atatürk. Heading: 'Avrupa Birliği Komisyonu Başkanı Romano Prodi', 15 Ocak 2004."),
 dict(id="musharraf-2004", voice="Pervez Musharraf", role="President of Pakistan", c="Pakistan", cn="Pakistan",
      dom="politics", date="2004-01-20", mirror="anti-colonial-liberator", pol="admiring", inten=2,
      saw="Calls Atatürk a hero and says Muslims in the subcontinent often gave his name to their children.",
      q="Kemal Atatürk bir kahramandı. (Alkışlar) Bizim bölgemizde bulunan Müslümanların sık sık kendi çocuklarına verdiği ismin sahibiydi.",
      pp=187, tr="Kemal Atatürk was a hero. (Applause) He was the bearer of a name that Muslims in our region often gave their own children.",
      extra="Same speech pairs Jinnah and Atatürk on peace (PDF p. 191). The vault's existing note says Atatürk was his hero in a general way; this is his stated view in the TBMM. Heading: 'Pakistan Cumhurbaşkanı Pervez Müşerref', 20 Ocak 2004.",
      link="Pervez Musharraf"),
 dict(id="cox-2004", voice="Pat Cox", role="President of the European Parliament", c="European Union", cn="European Union",
      dom="diplomacy", date="2004-03-02", mirror="modernization-poster-child", pol="instrumental", inten=1,
      saw="Tells the Assembly that Turkey, a Muslim country that has struck a balance, carries Atatürk's legacy of a secular democratic republic.",
      q="Burada, Müslüman bir ülke olarak bir denge kurdunuz, Atatürk’ün mirasını taşıyorsunuz.",
      pp=210, tr="Here, as a Muslim country, you have struck a balance; you carry Atatürk's legacy.",
      extra="Answers the 'Christian club' objection to Turkish EU membership. Heading: 'Avrupa Parlamentosu Başkanı Pat Cox', 2 Mart 2004."),
 dict(id="borrell-2004", voice="Josep Borrell Fontelles", role="President of the European Parliament", c="European Union", cn="European Union",
      dom="diplomacy", date="2004-12-03", mirror="secular-rationalist-prophet", pol="instrumental", inten=1,
      saw="Says that although most Turks are Muslim, Atatürk founded the republic and built it on democratic and secular principles.",
      q="Türkiye Cumhuriyeti Atatürk tarafından kurulmuş ve Atatürk tarafından, Türkiye, demokratik ve laik ilkeler üzerine inşa edilmiştir.",
      pp=220, tr="The Republic of Turkey was founded by Atatürk, and by Atatürk Turkey was built on democratic and secular principles.",
      extra="Accession-talks context: the speech answers questions about religion and EU membership. Heading: 'Avrupa Parlamentosu Başkanı Josep Borrell Fontelles', 3 Aralık 2004."),
 dict(id="van-der-linden-2005", voice="René van der Linden", role="President of the Parliamentary Assembly of the Council of Europe", c="Council of Europe", cn="Council of Europe",
      dom="politics", date="2005-11-09", mirror="emancipator-patriarch", pol="admiring", inten=2,
      saw="After visiting Anıtkabir, says Atatürk carried out legal, social and cultural reforms and laid Turkey's foundations; quotes him on women.",
      q="Kendisi bir hukuk ve sosyal politik ve kültürel reformları gerçekleştirmiş, bugünkü Türkiye’nin temellerini atmıştır ve eminim ki, siz de O’nun yolundan gidecek bir parlamentosunuz.",
      pp=229, tr="He carried out legal, socio-political and cultural reforms and laid the foundations of today's Turkey, and I am sure that you will be a parliament that follows his path.",
      extra="He also notes that 9 November was the eve of the anniversary of Atatürk's death and calls the name 'Atatürk' the 'father of the Turks'; urges more women MPs. Heading: 'Avrupa Konseyi Parlamenter Meclisi Başkanı Rene Van Der Linden', 9 Kasım 2005.", link="Anıtkabir"),
 dict(id="barroso-2008", voice="José Manuel Barroso", role="President of the European Commission", c="European Union", cn="European Union",
      dom="diplomacy", date="2008-04-10", mirror="modernization-poster-child", pol="instrumental", inten=1,
      saw="Says Atatürk founded the Assembly to let the Turkish people debate their future and to turn Turkey into a modern republic.",
      q="Büyük Mustafa Kemal Atatürk, Türk halkına meşru bir şekilde geleceklerini tartışma imkânı tanımak adına bu Meclisi kurdu ve Türkiye’yi modern bir cumhuriyete dönüştürmek amacıyla bu Meclisi kurdu",
      pp=240, tr="The Great Mustafa Kemal Atatürk founded this Assembly to give the Turkish people the possibility of legitimately debating their future, and founded it in order to turn Turkey into a modern republic.",
      extra="Heading: 'Avrupa Birliği Komisyonu Başkanı Jose Manuel Barroso', 10 Nisan 2008."),
 dict(id="obama-2009", voice="Barack Obama", role="President of the United States", c="United States", cn="United States",
      dom="politics", date="2009-04-06", mirror="modernization-poster-child", pol="admiring", inten=2,
      saw="After visiting the mausoleum, calls Atatürk a leader who changed history's shape whose greatest legacy is Turkey's living secular democracy.",
      q="kendisi tarihin şeklini değiştiren bir liderdir. Ama Atatürk’ün yaşamına ait en büyük anıt hiçbir şekilde taştan ya da mermerden inşa edilemez, kendisinin bırakmış olduğu en büyük miras Türkiye’nin canlı laik demokrasisidir",
      pp=254, tr="He is a leader who changed the shape of history. But the greatest monument to Atatürk's life cannot be built of stone or marble; the greatest legacy he left is Turkey's living secular democracy.",
      extra="Heading: 'Amerika Birleşik Devletleri Başkanı Barack Hussein Obama', 6 Nisan 2009.", link="Anıtkabir"),
 dict(id="nazarbayev-2009", voice="Nursultan Nazarbayev", role="President of Kazakhstan", c="Kazakhstan", cn="Kazakhstan",
      dom="politics", date="2009-10-22", mirror="nation-forge-template", pol="admiring", inten=2,
      saw="Calls Atatürk a genius whose foresight foretold independence for the other Turkic states; announces his statue in Astana.",
      q="Türkiye Cumhuriyeti’nin kurucusu, dâhi şahsiyet Atatürk daha o zamanlarda bile diğer Türk devletlerinin günün birinde bağımsızlıklarına kavuşacağını büyük bir öngörüşle ifade etmişti.",
      pp=268, tr="The founder of the Republic of Turkey, the genius Atatürk, even then expressed with great foresight that the other Turkic states would one day gain their independence.",
      extra="On PDF p. 269 he reports unveiling a large statue of Mustafa Kemal Atatürk on the Esil river in Astana before his visit. Heading: 'Kazakistan Cumhurbaşkanı Nursultan Nazarbayev', 22 Ekim 2009."),
 dict(id="wulff-2010", voice="Christian Wulff", role="President of Germany", c="Germany", cn="Germany",
      dom="politics", date="2010-10-19", mirror="modernization-poster-child", pol="instrumental", inten=1,
      saw="Supports Turkey's path toward Europe and says Atatürk opened that road; closes by quoting his peace maxim.",
      q="bu yol Büyük Mustafa Kemal Atatürk tarafından açılmıştır.",
      pp=285, tr="This road was opened by the Great Mustafa Kemal Atatürk.",
      extra="The closing quotation (PDF p. 286) is the 'peace at home, peace in the world' maxim. Heading: 'Almanya Federal Cumhuriyeti Cumhurbaşkanı Christian Wulff', 19 Ekim 2010."),
]

# ritual mentions (not stored): who, date, PDF page, what
RITUAL = [
 ("Serdar Fahir Hikmat, head of the Iranian Majlis delegation", "1958-11-01", "20-21", "calls Atatürk 'büyük Türk milletinin kurucusu' while recalling Reza Shah's 1934 visit (24 years before); formula only"),
 ("Hüber Reymon, President of the Swiss Council of States", "1989-04-23", "64", "'Cumhuriyetin Kurucusu Mustafa Kemal Atatürk’ün eseri olan ülkenizin'; descriptor only"),
 ("Ahmed Urai, President of the Malaysian Senate", "1990-04-23", "68", "closes hoping Atatürk's 'Yurtta Sulh Cihanda Sulh' guides us; slogan"),
 ("Abdildin Serikbolsun, Chairman of the Kazakh Supreme Council", "1992-04-23", "74-75", "quotes Atatürk on world brotherhood and calls him 'büyük devlet adamı'; one-clause epithet"),
 ("Aleksander Kwaśniewski, President of Poland", "2000-04-14", "164", "'Mustafa Kemal Atatürk’ün Türkiye Cumhuriyetini kurduğu dönemde' ; chronology only"),
 ("Sahad Muradov, Speaker of Turkmenistan", "2000-04-23", "168-169", "'Büyük Atatürk’ün yarattığı' Assembly, quotes sovereignty and peace sayings; ceremonial for the 80th anniversary"),
 ("Leonid Kuchma, President of Ukraine", "2000-11-23", "172, 175", "dates Atatürk's 1919 landing and quotes his 'economy, science and knowledge' victories line; no stated view"),
 ("Shimon Peres, President of Israel", "2007-11-13", "232", "opens by quoting Atatürk on future generations; no stated view of him"),
 ("Aníbal Cavaco Silva, President of Portugal", "2009-05-12", "262, 264", "calls the people one 'Atatürk’ün gurur duyduğu' and quotes 'Beşeriyet tek bir vücuttur'; quotation only"),
 ("Yusuf Raza Gilani, Prime Minister of Pakistan", "2010-12-07", "289", "Ankara's Jinnah Avenue and Islamabad's Atatürk Avenue as a symbol of friendship; street names only"),
 ("Almazbek Atambayev, President of Kyrgyzstan", "2012-01-12", "310", "notes the First Assembly elected Mustafa Kemal Atatürk its president; historical fact"),
]
DRY = [
 "No mention of Atatürk or Kemal: Irak Mebusan Meclisi Reisi Abdülvahap Mercan (15 Nisan 1955), Sukarno (24 Nisan 1959), Gerstenmaier (1 Nisan 1964), Flanagan (1986), Lulling (1987), Denktaş 10 Haziran 1993, 21 Ocak 1997 aside, Cengiç (1992), the two Ilham Aliyev speeches (2004, 2008), Yudhoyono (2010), Abbas (2007), Buzek (2011).",
]

# ---- verify quotes against the text layer -------------------------------------------------
def norm(s):
    s = s.replace("­", "")
    s = re.sub(r"-\n", "", s)
    s = re.sub(r"\s+", " ", s)
    return s
full = norm(open(os.path.join(STATE, "full.txt"), encoding="utf-8").read())
bad = [r["id"] for r in R if norm(r["q"]) not in full]
if bad:
    # hyphenated line-end words in the layer can differ ('Mus-\ntafa'), retry without hyphen/space differences
    full2 = full.replace(" ", "")
    bad = [i for i in bad if norm([r for r in R if r["id"] == i][0]["q"]).replace(" ", "") not in full2]
if bad:
    sys.exit("quote not found in text layer: %s" % bad)
for r in R:
    assert len(r["saw"].split()) <= 25, (r["id"], len(r["saw"].split()))

def pr(n):
    return "PDF p. %d (printed p. %d)" % (n, n - 11)

# ---- gazes file -------------------------------------------------------------------------
os.makedirs(STATE, exist_ok=True)
with open(os.path.join(STATE, "gazes_statesmen.jsonl"), "w", encoding="utf-8") as f:
    for r in R:
        cav = "TBMM Tarihe Düşülen Notlar-2 (2012), %s. Speech printed in Turkish as in the TBMM minutes. Translation: \"%s\" %s" % (pr(r["pp"]), r["tr"], r["extra"])
        rec = {"id": r["id"], "voice": r["voice"], "voice_type": "person", "role": r["role"], "country": r["c"],
               "country_now": r["cn"], "domain": r["dom"], "date": r["date"], "era": "posthumous", "mirror": r["mirror"],
               "polarity": r["pol"], "intensity": r["inten"], "what_they_saw": r["saw"], "quote": r["q"],
               "artifact": "speech", "evidence": "P", "mediated_by": MED, "caveat": cav, "node": NODE, "sources": [H]}
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")

with open(os.path.join(STATE, "ledger_statesmen.md"), "w", encoding="utf-8") as f:
    f.write("| Claim | Node | Status | Sources | Next step |\n|---|---|---|---|---|\n")
    for r in R:
        f.write("| %s (%s, %s) in the TBMM plenary: \"%s\" | %s | verified P (page image, %s) | TBMM handle 11543/122 | none |\n"
                % (r["voice"], r["role"], r["date"], r["q"][:110].replace("|", "/") + ("..." if len(r["q"]) > 110 else ""), NODE, pr(r["pp"])))

# ---- Events note ------------------------------------------------------------------------
sections = {}
for r in R:
    y = int(r["date"][:4])
    k = "1956–1965 — the first guests" if y < 1970 else ("1984–1999 — anniversary speeches and the new Turkic states" if y < 2000 else "2004–2010 — Europe, Washington and the Turkic world")
    sections.setdefault(k, []).append(r)

body = ["""
Between 1955 and 2011 foreign statesmen spoke from the rostrum of the Turkish Grand National Assembly 48 times, and the
Assembly's own press office collected the texts in *Tarihe Düşülen Notlar-2* (2012). The speeches are printed in Turkish
as in the plenary minutes; where the speaker used another language the Turkish is the interpreter's. This note reads the
whole book for **who said what about Atatürk** and stores the voices that actually characterise him. The speaker, office and
date come from the book's own headings; every stored quotation was read from a rendered page image, not only from the
text layer. Page numbers are PDF pages, with the printed page number in brackets (PDF page minus 11).

## What counts

A speaker who only names him ("the Republic founded by Atatürk"), recites the *Yurtta sulh, cihanda sulh* slogan or quotes him
without stating a view is a *ritual mention* and is not stored as a gaze. The eleven of those are listed in
`candidates/funeral-delegations.md` (Round 11). The two earliest speeches, 1955 and 1959 (Sukarno), do not mention him at all.

## The pattern

- **Admiration for the liberator**: Pakistan (Mirza 1956, Muzaffar Ali 1957, Musharraf 2004) and Malaysia (Zahir 1988) remember
  him as the colonised world's hero, [[Muhammad Ali Jinnah]]'s counterpart.
- **The post-Soviet turn**: Elçibey, Haydar Aliyev and Nazarbayev treat him as the model for a new Turkic state; the Soviet delegate of 1965
  had instead appealed to the Lenin–Atatürk friendship.
- **The European and American register**: from 1999 the Commission and Parliament presidents, Clinton, Obama and Wulff cite
  him as the author of Turkey's secular, modernising, European direction. That is praise with a purpose; it is stored as
  *instrumental* where the sentence serves the speaker's own pitch (accession talks), *admiring* where it states a view of the man.
- **The single conflicted voice**: [[Habib Bourguiba]] in 1965.

""".strip()]

for k in sorted(sections):
    body.append("\n## " + k + "\n")
    for r in sections[k]:
        link = (" See [[%s]]." % r["link"]) if r.get("link") else ""
        body.append("### %s, %s (%s)\n" % (r["voice"], r["role"], r["date"]))
        body.append("*%s*\n" % r["saw"])
        body.append("> %s\n" % r["q"])
        body.append("Translation: %s %s. %s%s\n" % ('"' + r["tr"] + '"', "(" + pr(r["pp"]) + ")", r["extra"], link))

body.append("""
## Dry ends

- No mention of Atatürk in the speeches of 1955 (Iraq's Mercan), Sukarno 1959, Gerstenmaier 1964, the two İlham Aliyev
  speeches, Yudhoyono, Abbas and Buzek. Sukarno's views are on his own note: [[Sukarno]].
- The Iranian delegate of 1958 recalls [[Reza Shah Pahlavi]]'s 1934 visit and calls Atatürk the "founder of the great Turkish
  nation", a formula only.

## Sources
- TBMM Başkanlığı, *Tarihe Düşülen Notlar-2: Yabancı Devlet Adamlarının Genel Kurul Konuşmaları*, Ankara, February 2012,
  https://acikerisim.tbmm.gov.tr/handle/11543/122 (PDF, 314 pages; rendered and read page by page).
- Each speech is a TBMM Tutanak Dergisi transcript; the printed language is Turkish, interpreted where the speaker used another.
""")

note("Events", NODE,
     {"type": "event", "when": "1956–2010",
      "tags": ["event", "verified", "tbmm", "posthumous", "heads-of-state"]},
     "\n".join(body))
print("ok", len(R), "records")
