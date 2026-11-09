# -*- coding: utf-8 -*-
# Census round 11 (Nov 2026) — heads of state speaking of Atatürk, mined from open articles that cite
# Bilal N. Şimşir, Atatürk ve Yabancı Devlet Başkanları (TTK, 4 vols, 1993-2001). The compilation itself is not
# openly downloadable and was not touched; every quote below was read in an open article.
# Writes one Events note and a JSONL of gaze records (tools/.state/round11/gazes_simsir.jsonl).
import json, os
from _lib import note

NODE = "Heads of State on Atatürk in Their Own Words, 1926–1933"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tools", ".state", "round11", "gazes_simsir.jsonl")

AKBAS = "https://ataturkilkeleri.deu.edu.tr/ai/uploaded_files/file/yeni%20dergi%2016-17/ismail%20akkas%202.pdf"
KACELI = "https://cdn.istanbul.edu.tr/file/JTA6CLJ8T5/C42184AE688A42C8A7E5F1E745478A38"
ALEX = "https://dergipark.org.tr/tr/download/article-file/2459611"
GOMBOS = "https://academia.edu/98216923/Macar_Ba%C5%9Fvekili_Gyula_G%C3%B6mb%C3%B6s_%C3%BCn_Atat%C3%BCrk_e_G%C3%B6nderdi%C4%9Fi_Mektup_ve_Kitaplar_%C3%87er%C3%A7evesinde_T%C3%BCrk_Macar_K%C3%BClt%C3%BCrel_M%C3%BCnasebetleri"

R = []
def rec(**k):
    base = dict(voice_type="person", domain="diplomacy", era="contemporary", artifact="speech", evidence="S", node=NODE)
    base.update(k)
    R.append(base)

rec(id="amanullah-1928-05-20", voice="Amanullah Khan", role="King of Afghanistan", country="Afghanistan",
    country_now="Afghanistan", domain="politics", date="1928-05-20", mirror="modernization-poster-child",
    polarity="admiring", intensity=2,
    what_they_saw="At the Ankara banquet he called Atatürk his brother and the sole author of Turkey's nine-year rise, and said he felt great affection.",
    quote="Sizi bunun yegâne amili bildiğim cihetle Zatı biraderinize karşı büyük bir hissi muhabbet ve halel-i napezir bir imtina duymaktayım.",
    mediated_by="Akbaş 2008 p. 319 ← Sarıhan p. 35 and Hizmet 22 May 1928 p. 1 (this passage); the opening of the same speech ← Şimşir vol. I p. 34",
    caveat="Ottoman-Turkish text of a speech given in translation at the 20 May 1928 state banquet. Translation: 'Since I know you to be the sole author of this, I feel for you, my brother, great affection and unshakeable (gratitude/regard)'; printed 'imtina' is probably 'imtinan' (gratitude). The Şimşir page is cited by Akbaş for the preceding paragraphs, Sarıhan/Hizmet for this one. A toast between hosts: also counts as ceremony.",
    sources=[AKBAS])

rec(id="zogu-1926-02", voice="Ahmet Zogu (King Zog I)", role="President of Albania (King from 1928)", country="Albania",
    country_now="Albania", domain="politics", date="1926-02-17", mirror="modernization-poster-child",
    polarity="admiring", intensity=2, artifact="report",
    what_they_saw="Told Turkey's first envoy that Turkey's reforms were an example for Muslim countries, Albania above all, and voiced special sympathy for Mustafa Kemal.",
    quote=None,
    mediated_by="Kaceli 2021 ← Şimşir, Atatürk ve Yabancı Devlet Başkanları (1993; Albania sits in vol. I, page not given) ← envoy Tahir Lütfi's report",
    caveat="Paraphrase of the envoy's dispatch; no verbatim words of Zogu. Kaceli gives no page for Şimşir here, so a page check in vol. I is still needed. Zogu was courting Ankara while his regime was weak, hence the instrumental edge.",
    sources=[KACELI])

rec(id="zogu-1931-12", voice="Ahmet Zogu (King Zog I)", role="King of Albania", country="Albania",
    country_now="Albania", domain="politics", date="1931-12-05", mirror=None,
    polarity="instrumental", intensity=2, artifact="report",
    what_they_saw="After four years of rupture he told Turkey's chargé he respected Atatürk and highly praised what he had done for Turkey.",
    quote=None,
    mediated_by="Kaceli 2021 ← Şimşir, Atatürk ve Yabancı Devlet Başkanları (1993; vol. I, page not given) ← chargé Zeki Haki's report",
    caveat="Paraphrase of a diplomat's report; the only words quoted in the article ('there are sacred things associating Albania with Turkey') concern Turkey, not Atatürk. Page not given. Context: reopening of the Albanian embassy; King Zog's own motive was to restore relations.",
    sources=[KACELI])

rec(id="alexander-i-1933-09-28", voice="Alexander I of Yugoslavia", role="King of Yugoslavia", country="Yugoslavia",
    country_now="Serbia", domain="politics", date="1933-09-28", mirror="nation-forge-template",
    polarity="admiring", intensity=2, artifact="report",
    what_they_saw="Before meeting him, told the Turkish envoy in Bucharest that Atatürk was an epoch-defining leader and that he admired him as administrator, organiser and reformer.",
    quote="Gazi Mustafa Kemal’in döneme damgasını vurmuş bir lider olduğu ve idareci, teşkilatçı, inkılapçı olarak yaptıklarına hayran olduğu",
    mediated_by="Tarih ve Gelecek 2022 ← BCA 030.10.251.696.22 (Hamdullah Suphi's report of 28 Sep 1933); the same article cites Şimşir vol. IV p. 261 for the visit",
    caveat="Turkish summary by the envoy in indirect speech ('he is said to admire'), quoted in the article; the King's own words are not preserved. Pre-Balkan-Pact courtship.",
    sources=[ALEX])

rec(id="alexander-i-1933-10-04", voice="Alexander I of Yugoslavia", role="King of Yugoslavia", country="Yugoslavia",
    country_now="Serbia", domain="politics", date="1933-10-04", mirror="nation-forge-template",
    polarity="admiring", intensity=2, artifact="report",
    what_they_saw="After meeting him at Dolmabahçe he said Atatürk's bearing, voice and gaze marked a rare man, and agreement with this exceptional man would be easy.",
    quote="Hali, tavrı, konuşması, başı, bakışı ve sesi derhal insan üzerinde nadir bir adam karşısında bulunduğumuzu düşündüren bir tesir bırakıyor.",
    mediated_by="Tarih ve Gelecek 2022 pp. 533 ← BCA 030.10.251.696.22 (Turkish report of the King's remarks); same article cites Şimşir vol. IV pp. 261, 278 for the visit",
    caveat="Turkish rendering of remarks reported from the visit; original language (French or Serbian) not given. Second line, same source: 'Devrin bu faik adamı ile anlaşmanın kolay olacağına dair bir intiba hasıl ettim' ('I formed the impression that agreement with this outstanding man of the age would be easy'). Motive: building the Balkan Pact.",
    sources=[ALEX])

rec(id="gombos-1933-10", voice="Gyula Gömbös", role="Prime Minister of Hungary", country="Hungary",
    country_now="Hungary", domain="politics", date="1933-10", mirror=None,
    polarity="instrumental", intensity=2,
    what_they_saw="After the Ankara audience called meeting the founder of the new Turkey a very great honour and said Turkish politicians saw Hungarians as kin.",
    quote="Yeni Türkiye'yi kuranla görüşmek benim için çok büyük bir şerefti.",
    mediated_by="Altaş 2022 (Yakın Dönem Türkiye Araştırmaları) ← Çolak (Gömbös statement after the 20–22 Oct 1933 Ankara visit)",
    caveat="Footnote numbers in the open copy are garbled, so the exact Çolak page is not confirmed; Turkish rendering of a Hungarian statement. Gömbös's interest was Turanism and Trianon revision (see his 1932 record). The 18 Sep 1934 letter attributed to him is word-for-word the Németh letter in the presidential archive, so it is not counted.",
    sources=[GOMBOS])

os.makedirs(os.path.dirname(OUT), exist_ok=True)
FIELDS = ["id","voice","voice_type","role","country","country_now","domain","date","era","mirror","polarity","intensity","what_they_saw","quote","artifact","evidence","mediated_by","caveat","node","sources"]
with open(OUT, "w", encoding="utf-8") as f:
    for r in R:
        f.write(json.dumps({k: r[k] for k in FIELDS}, ensure_ascii=False) + "\n")

body = f"""
Round 11 mined open-access articles that quote **Bilal N. Şimşir's** four-volume *Atatürk ve Yabancı Devlet Başkanları* /
*Atatürk and Foreign Heads of State* (TTK, 1993–2001; vol. I Afghanistan–China), the standard collection of heads of
state's letters and conversations with Atatürk. The compilation is not openly downloadable and was not used; what follows
is what the articles print. Most of the book's correspondence is protocol (see the end), so the harvest is small and
confined to heads of state who said what they thought of the man. Everything is Turkish-language: the articles print the
Turkish version of what was said or written in French, Albanian or Hungarian.

## Amanullah Khan, banquet at Ankara, 20 May 1928

The first foreign sovereign received in the new capital. Atatürk's toast warned him on Afghanistan's "serious and delicate"
position and urged reform; Amanullah answered, in the passage Akbaş prints from Sarıhan and the newspaper *Hizmet*:
*"Aziz Türkiye'nin faaliyet ve kudret numunesi olan Zatı Devletinizin ... bugünkü terakkiyatı ben ve aziz milletim
memnuniyet ve iftihar dolu gözler ile görmekteyiz ... Sizi bunun yegâne amili bildiğim cihetle Zatı biraderinize karşı
büyük bir hissi muhabbet ve halel-i napezir bir imtina duymaktayım."* (He sees Turkey's nine-year rise "with eyes full of
satisfaction and pride" and counts Atatürk its "only author"; "imtina" is probably *imtinan*, gratitude.) Earlier in the
speech he set the two struggles side by side: the Turkish nation rose "under your guidance" while the Afghans rose under his.
(Akbaş 2008, pp. 318–319; Şimşir vol. I pp. 33–34 for the speeches.) The farewell remark on 1 June, *"Türkler Afganlıların
ağabeyleridir"* ("the Turks are the Afghans' elder brothers"), concerns the nation, not the man, and is not counted.
Amanullah fell the next year; see [[Amanullah Khan]] for what he tried to copy.

## Ahmet Zogu (King Zog I), 1926 and 1931

Two reports in Kaceli's chapter, both from Turkish diplomats' dispatches that she cites to Şimşir (vol. I, no page given).
**17 Feb 1926:** receiving Turkey's first minister, Tahir Lütfi, President Zogu praised the Turkish reforms as an example for all
Muslim countries and "especially for Albania" and "stated his special sympathy for Mustafa Kemal". **5 Dec 1931:** after four
years without a Turkish envoy, the King told the chargé Zeki Haki of his respect for Atatürk and his high praise for what
Atatürk had done for Turkey's development. Paraphrase only; no verbatim words of Zog about Atatürk survive in the article.
The contrast with the vault's [[King Zog I]] note is the point: the man who copied the decrees and crowned himself in 1928
told the Republic's envoys he admired the model. Kaceli also quotes his 19 April 1925 letter to Mustafa Kemal, which speaks
only of the treaty of friendship and is protocol.

## Alexander I of Yugoslavia, September–October 1933

Before the Dolmabahçe meeting of 4 October 1933 (the visit that opened the road to the [[Balkan Pact]]), the Turkish minister
in Bucharest, Hamdullah Suphi, reported on 28 Sep that the King *"Gazi Mustafa Kemal'in döneme damgasını vurmuş bir lider
olduğu ve idareci, teşkilatçı, inkılapçı olarak yaptıklarına hayran olduğu"* (that Atatürk was a leader who had stamped the
age and that he admired what he had done as administrator, organiser and reformer). After the meeting the King is quoted:
*"Hali, tavrı, konuşması, başı, bakışı ve sesi derhal insan üzerinde nadir bir adam karşısında bulunduğumuzu düşündüren bir
tesir bırakıyor"* (his manner, bearing, speech, head, gaze and voice at once give the impression of facing a rare man) and
*"Devrin bu faik adamı ile anlaşmanın kolay olacağına dair bir intiba hasıl ettim"*. Both are Turkish reports of French or
Serbian remarks, from the archive file BCA 030.10.251.696.22 as printed in a 2022 article that cites Şimşir vol. IV pp. 261
and 278 for the visit. A year later he was dead in Marseille (see [[Alexander I of Yugoslavia]]). The thank-you telegram
exchange after the visit (gratitude for the reception) is protocol.

## Gyula Gömbös, October 1933

On his Ankara visit of 20–22 October 1933 the Hungarian premier is quoted as saying that meeting *"Yeni Türkiye'yi kuranla"*
("the founder of the new Turkey") had been *"çok büyük bir şeref"*, and that he was sure even the most important Turkish
politicians thought of the Hungarians as kin. His motive was Turanist and revisionist, as the earlier [[Gyula Gömbös]]
record explains. His 18 September 1934 letter with 27 volumes of Hungarian history is the same text as a letter written for
him by the Turkologist Gyula Németh and speaks of respect for the Republic, not for Atatürk, so it is listed but not counted.

## Protocol only (senders named in the articles, no stated view of him)

- **Amanullah's Lausanne telegram, July 1923:** sent through the Afghan envoy Sultan Ahmed Han to Mustafa Kemal at İzmir,
  celebrating "our peace feast" for the Emir and the nation; Atatürk's reply of 27 July 1923 is printed (Şimşir vol. I
  pp. 12–13, via a 2008 DEÜ thesis). Described as the only head of state to congratulate him on Lausanne. No view of the man.
- **Horthy, 1933:** wished Atatürk "many more years" in service of the brother nation on the Republic's tenth anniversary
  (Şimşir vol. III p. XVII, via Çolak 2003); condolences in 1938.
- **Atatürk's reply to Roosevelt's tenth-anniversary message** (Şimşir vol. I pp. 233–235, Turkish and English): Roosevelt's own
  text is not quoted in the open article that cites it.
- Alexander's and Atatürk's thank-you telegrams after the Dolmabahçe visit; Zog's April 1925 and January 1926 letters.

## Sources
- İsmail Akbaş, "Afgan Kralı Emanullah Han'ın Türkiye Gezisi", *Çağdaş Türkiye Tarihi Araştırmaları Dergisi* VII/16-17
  (2008), pp. 311–333, {AKBAS}
- Ilirjana Kaceli, "Economic, Social and Cultural Relations Between the Republic of Turkey and Albania", Istanbul University
  Press chapter (2021), {KACELI}
- "Yugoslavya Kralı I. Alexander'in Atatürk ile Görüşmesi (4 Ekim 1933)", *Tarih ve Gelecek Dergisi* 8/2 (June 2022),
  pp. 520–534, {ALEX}
- Seyithan Altaş, "Macar Başvekili Gyula Gömbös'ün Atatürk'e Gönderdiği Mektup ve Kitaplar Çerçevesinde Türk-Macar Kültürel
  Münasebetleri", *Yakın Dönem Türkiye Araştırmaları* (2022), {GOMBOS}
- Bilal N. Şimşir, *Atatürk ve Yabancı Devlet Başkanları*, 4 vols., TTK, Ankara 1993–2001 (cited through the articles above,
  never opened).
"""
note("Events", NODE, {"type": "event", "when": "1926–1933",
     "tags": ["event", "verified", "heads-of-state", "simsir", "modernization-poster-child"]}, body)
print("ok", len(R), "records")
