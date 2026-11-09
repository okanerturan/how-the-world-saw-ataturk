# -*- coding: utf-8 -*-
# Census round 3 (Oct 2026) — USSR / Caucasus / Central Asia.
# Sources read in full or in substantive snippets; see ledger_eurasia.md for claim-level status.
from _lib import note, person

P = [
("Mehmed Emin Resulzade", dict(role="Founder of the 1918 Azerbaijani Republic; émigré publicist (Istanbul, Warsaw, Berlin, Ankara)", nat="Azerbaijani", life="1884–1955",
  stance="admiring theorist, expelled by the state he admired", tags=["admirer", "exile", "caucasus", "verified"], body="""
The perfect double-edged card: **the admirer the admired state could not afford to host.**

Resulzade, the political leader of the short-lived Azerbaijan Democratic Republic (1918–20), watched
Ankara from exile. He had lived through the Bolshevik conquest of his own republic, so he read the
Anatolian movement as the case that *kept* its independence — and said so. Two texts bracket his
Atatürk:

- **1928**, "The Symbol of the Liberated East" (*Qurtulan Şərqin simvolu*): Gazi Pasha as both an
  independence-fighter "of Washington's stature" and a revolutionary "on the scale of the heroes of
  the French Revolution" — for a colonial or semi-colonial East, independence from outsiders is not
  enough; the nation must also remake itself within.
- **November 1938**, "Brother Turkey, my condolences!" (*Qardaş Türkiyə, başın sağ olsun!*),
  *Qurtuluş* (Berlin), no. 49, pp. 2–5, reprinted in Russian (and rewritten, not merely translated)
  in *Severnyi Kavkaz* (Warsaw), nos. 55–56, pp. 19–22. He credits Atatürk with seeing, when others
  wanted a British protectorate or an American mandate, that salvation lay in "an unconditionally
  independent Turkish state resting on national sovereignty"; he describes the abolition of the Caliphate
  as Atatürk's own radical road; he reads Kemalism as positivism and 15 years of compressed centuries; and
  he uses the funeral to answer the question the "authoritarian regimes born of the war" always
  faced — what happens when the founder dies? — pointing to İnönü's instant election and the
  government's "the Republic is his immortal work" notice as proof the machine ran "like a wound
  clock." The Russian rewrite adds what the Turkish text omits: the Ankara–Moscow relationship,
  including the drowning of [[Mustafa Suphi]]'s party at Trabzon.

**The expulsion.** The BBC Azərbaycanca historian Altay Göyüşov surveys the literature: the date of
Resulzade's leaving Turkey is given variously between 1928 and 1931 (most sources: **1931**);
whether he left or was ejected is disputed, but "the majority prefers the expulsion version"; and
the cause is usually put down to Soviet pressure (Moscow Treaty art. 8, Kars Treaty art. 10, the
1925 treaty renewed with a rumoured secret protocol in 1931). Göyüşov doubts that Moscow could have
forced Ankara's hand in 1931 and points instead to Turkish domestic politics: Atatürk's government
cut aid to the Azerbaijan National Center and closed his *Yeni Kafkasya* in 1927, was folding the
Türk Ocakları (Turkish Hearths) into the party-state, and was ending the Free Party experiment in
1930–31; the Azerbaijani émigrés' independent anti-Soviet organizing no longer fit, and in 1931
all his publications were banned. Resulzade went to Poland, later Berlin and Romania, and regained
Turkish citizenship only in 1947. (Another Azerbaijani account, in the preface to Vilayət Quliyev's
translation, places the expulsion after the October 1933 visit of [[Kliment Voroshilov]] and
Budyonny, who delivered Stalin's complaint about anti-Soviet agitation — **the date is genuinely
unsettled.**)

Both accounts agree on the human point, which Quliyev puts best: he "was not unaware of why
Atatürk took a step he was perhaps inwardly unhappy about", and he did not let private grievance
turn him from the model. He died in Ankara in 1955; the modern Azerbaijani state calls him founder,
and the Heşimova survey of Azerbaijani poetry credits him with assessing Atatürk's struggle
highly (see [[Azerbaijani Poetry of Atatürk]]).

Pair with [[Mustafa Suphi]] (the communist killed at sea) and [[Mustafa Çokay]] — three exiled
Turkic voices who watched Ankara bargain with Moscow and judged the bargain differently.
Context: [[Abolition of the Caliphate]] · [[Death and State Funeral of Atatürk]].

## Sources
- Göyüşov, "Rəsulzadə Türkiyədən niyə getdi?", [BBC Azərbaycanca, 9 Mar 2017 (updated 2024)](https://www.bbc.com/azeri/analysis-39221340) — S/J (historian's analysis)
- Nikpur Cabbarlı (ed.), ["Qardaş Türkiyə, başın sağ olsun!" with full text](https://edebiyyatqazeti.az/news/sience/11325-qardas-turkiye-basin-sag-olsun), *Ədəbiyyat Qəzeti* — text of the 1938 *Qurtuluş* article, S-edited
- Vilayət Quliyev, [Russian-version translation and introduction, *525-ci qəzet*](https://525.az/news/15092-kamal-ataturkun-vefati-munasibeti-ile--meresulzade-ataturk-haqqinda) — S
- [Quliyev on the rediscovered Warsaw text (ZİM)](https://zim.az/elm/elmi-meqaleler/924-mhmmd-min-rsulzad-atatrk-haqqnda.html)
- Heşimova 2024 (DergiPark, below) for the Azerbaijani-historiography frame
""")),

("Mikayıl Müşfik", dict(role="Azerbaijani lyric poet; victim of the 1937–38 purge", nat="Azerbaijani (Soviet)", life="1908–1938",
  stance="admiring — a forbidden poem written under Stalin", tags=["admirer", "poet", "caucasus", "witness", "verified"], body="""
The most striking contemporary card in the Azerbaijani set, and the most dangerous to hold: **a
poem to Atatürk written in 1937, inside the USSR, at the height of the purge.**

Müşfik (born Ismayılzade, 1908–**6 January 1938**), one of the young founders of the new
Azerbaijani Soviet poetic style with Samad Vurgun and Rasul Rza, wrote "Atatürk" in 1937 — a
after "Atatürkism" had become effectively forbidden in Azerbaijan from the early 1930s (Nizami
Cəfərov's periodization, as relayed by Heşimova). The
poem, by the scholarly account, lay unknown for 80 years; it came to light in **2017** through Dr.
Dilkam Ahmet's search of the Turkish press and journals of the Azerbaijani émigrés in Turkey. The
closing lines run (my rendering from the Turkish text): *"O great Atatürk, with you I raise / a glorious
monument in the homeland of words."* He believed he had cut his name into mountains and stone by
writing it, and that this single poem would carry him into history.

Heşimova — the source for all of this — adds that the poem was **one of the grounds for his
prosecution**, charged at the time as "Turkism and pan-Islamism"; he was shot in the purge at 29. Treat that last causal claim as single-source until the NKVD
file is cited, and treat the attribution/dating of the poem itself as dependent on the 2017
discovery (the text is reproduced on a Turkish compilation site of world poets' Atatürk poems — a
second-hand reproduction, not independent authentication).

This is the Azerbaijani gaze at its purest: the admiration as an act of national self-assertion
that cost a life, the same mechanism as [[Kazi Nazrul Islam]] in Bengal but under a censor who
shot. Compare [[Mikhail Frunze]]'s and [[Kliment Voroshilov]]'s official Soviet Kemal; this is the
unofficial one. See [[Azerbaijani Poetry of Atatürk]].

## Sources
- Heşimova, ["20. Yüzyılda Azerbaycan Şiirinde Mustafa Kemal Atatürk"](https://dergipark.org.tr/en/download/article-file/3737657), *Uluslararası Türk Dünyası Bilimsel Araştırmalar Dergisi* 5(1), 2024, §1 (full text read) — S, citing Ahmet 2017 and Nazarlı 2003
- [Wikipedia: Mikayil Mushfig](https://en.wikipedia.org/wiki/Mikayil_Mushfig) (dates; T)
- [Dünyada Atatürk: poems by world poets, no. 20 "Atatürk'e"](https://www.dunyadaataturk.com/dunya-sairlerinden-ataturk-siirleri/) (text reproduced; T)
""")),

("Mustafa Çokay", dict(role="Kazakh Turkestan-autonomy leader; émigré editor of *Yaş Türkistan* (Paris/Berlin)", nat="Kazakh / Turkestani", life="émigré 1920s–1941",
  stance="admiring, conditional — compared the one-party states", tags=["admirer", "exile", "central-asia", "verified"], body="""
Mustafa Çokay (Chokay, Chokaev) — a founder of the Turkestan Autonomy, driven out when it was
crushed — spent two decades in Paris and Berlin editing *Yaş Türkistan* and writing for the
Promethean press. He is the Central Asian counterpart to [[Mehmed Emin Resulzade]]: a Turkic
independence-fighter who treated Kemalist Turkey as the proof-of-concept.

Per the archival study in *MTAD* 10(4) (corresponding author K. Esmagambetov; Chokay's archive at
Paris-Sorbonne, Turkish state archives, the Russian RGVA/RGASPI files, and the periodical run): Çokay **compared the three one-party states
of the era — Bolshevik Russia, Fascist Italy and the Turkish Republic** — and voiced his
"satisfaction" with Kemalist Turkey's progressive domestic policies, a country that, in the abstract's own wording (not Çokay's), was reborn "from its ashes by a miracle"; the Anatolian war of liberation was, for him, a rare case in world history.
He set out his views on the Republic and on Atatürk in *Yaş Türkistan*, and **kept praising
Atatürk's moral support for the Turkestan national cause even after the journal was banned from
entering Turkey** — the same pattern as Resulzade's: banned by the state he admired, still
admiring it. Among the cited pieces: "Les Bolcheviks contre le kemalisme" (*Prométhée*, July 1931),
"L'amitié turco-soviétique" (*Prométhée* 1933), and "Moscow and the Turkish Communist
Party" (*Yaş Türkistan* 1934).

*Lead, not yet verified:* a secondary web source says Çokay published an obituary of Atatürk in
1938 in *Yaş Türkistan* ("how heavy and how sad a loss…"); the issue and quotation need the
primary or a scholarly citation before they enter the ledger.

Why he matters beyond biography: Turkestan was the place where the Turkish and Soviet visions of
the East collided; his reading — admiration for the state-builder, anxiety about the Moscow
friendship — is the exile's version of [[Vladimir Lenin]]'s instrumental one.

## Sources
- [*Modern Türklük Araştırmaları Dergisi* 10(4), Dec 2013, article on Çokay and Atatürk (Esmagambetov): abstract and bibliography, fetched](https://mtad.humanity.ankara.edu.tr/39-1042013-633.php) — S
- Context: [Çokay and *Yaş Türkistan* (academia.edu)](https://www.academia.edu/37592797/MUSTAFA_%C3%87OKAYIN_YURT_DI%C5%9EINDA_Y%C3%9CR%C3%9CTT%C3%9C%C4%9E%C3%9C_T%C3%9CRKISTAN_BA%C4%9EIMSIZLIK_M%C3%9CCADELESI_VE_YA%C5%9E_T%C3%9CRKISTAN_DERGISI)
""")),
]

E = [
("Azerbaijani Poetry of Atatürk", "1937–2007", """
The Azerbaijani gaze is a **poetry seam**: the one place in the census where a whole national
literature can be read as a sequence of attitudes. Heşimova's 2024 survey (read in full) gives the
skeleton. Nizami Cəfərov's four phases of Azerbaijani "Atatürkism": positive in the 1920s;
**negative from the early 1930s to the 1950s** (Atatürkism forbidden); "liberal" from the
mid-1950s to mid-1980s; and "romantic" from the late 1980s.

**The 1920s (official, and positive).** The Baku party daily *Kommunist* ran a run of articles
that show the line: "Mustafa Kemal on the Fronts" (18 Aug 1920), "Turkey and the Eastern
Revolution" (16 Nov 1920), "The Ankara Government, the Nationalists and Soviet Russia" (30 Dec
1920), "Lausanne" (6 Jul 1923) and the 1923 parliamentary elections. Azerbaijani liberation was
framed in the same breath as "Turkey's struggle for independence."

**The 1930s (forbidden — and one poem).** [[Mikayıl Müşfik]]'s 1937 "Atatürk," later credited
with helping to condemn him. Alongside, a contested scholarly reading (Güntay Gençalp) that
Hüseyn Cavid's play *İblis* (1918) already stages Atatürk in its protagonist Elhan — Heşimova
flags this as subjective. Also: Ahmet Cevad's volume *Dalga* is recorded among Atatürk's personal
books, inscribed by the poet (Memmedli 2010). And the death of Atatürk was reported in the
Azerbaijani press under tight Moscow control — *Kommunist* and *Gənc İşçi* led, both from Anadolu
Ajansı wires (Aliyeva 2015, quoted by Heşimova).

**1990s–2000s (romantic revival).** After independence the genre explodes:
**Bəxtiyar Vahabzadə**, "Atatürk'ün Babası" (1992; the people "with mountains on their breast"
asking God for a leader to unite them in Atatürk's way); **Zəlimxan Yaqub** (1950–2016), "Atatürk,"
written after days spent in Atatürk's seaside kiosk in Istanbul; **Xəlil Rza Ulutürk**, "Dədə Heydər – Atatürk" (2003),
fusing the Azerbaijani president Heydər Əliyev with the Turkish founder; **Rəfiq Zəka Xəndan**
(1939–99), the book *Atatürkiye* (1993); plus Kabil, Abbas Abdulla, Niftalı Yusifov's long poem
"The Golden-Haired Hero" (2000), Kadir İbaoğlu's *Atatürk Destanı* (2002), Abbasov's 2007 epic, and
the 2004 anthology *Türküm Benim Atatürk'üm* from Baku's Atatürk Center (founded 2001). Ebülfez
Elçibey called himself "Atatürk's soldier."

Read the arc against the mirror: under Moscow, Atatürk is first a fellow anti-imperialist
(1920–22), then a banned name (1930s–50s), then — once the USSR falls — **the model of the
state-builder Azerbaijan wished it had** (Vahabzadə) and a figure to bolt onto its own leader
(Ulutürk). The poems are admiring almost without exception; the interest is what the admiration
stands in for. (Caveat: most of the corpus is post-1991 and thus a *posthumous* gaze; only
Müşfik and the 1920s *Kommunist* material are contemporary.) See [[Mehmed Emin Resulzade]] for the
émigré political counterpart.

## Sources
- Heşimova, ["20. Yüzyılda Azerbaycan Şiirinde Mustafa Kemal Atatürk"](https://dergipark.org.tr/en/download/article-file/3737657), *Uluslararası Türk Dünyası Bilimsel Araştırmalar Dergisi* 5(1), 2024, pp. 1–8 (full text read) — S; she cites Cəfərov 2006, Ahmet 2017, Memmedli 2010, Aliyeva 2015
"""),

("Moscow Mourns, November 1938", "10–13 November 1938", """
The Soviet press said the right words and kept the wrong years silent.

Per Lyulchak's discourse analysis of Soviet and Turkish papers (*ISTORIYA*, 2024): Soviet
periodicals "fully shared the pain and loss of the Turkish people" — telegrams, official messages
and obituaries tracing the life of the "leader of the Turkish nation." But the difficult state of
Soviet–Turkish relations after **Montreux (1936)** shows in the coverage: the obituaries
**"deliberately" pass over the second half of the 1930s**, and that strain is reflected in the level of attention the funeral received. Where the Turkish papers printed only the positive, the
Soviet papers ignored whatever was inconvenient to Moscow–Ankara relations.

The *New York Times* of 13 November 1938 reports the contemporary reading from Moscow: *Pravda*
and *Izvestia* ran **long laudatory biographies of the late Kemal Atatürk and of his successor
İsmet İnönü**, stressing both men's friendliness to the Soviet Union — a cordiality that "may
indicate Moscow's desire to better relations with Angora." Turkish diplomatic compilations of
foreign quotes give lines from *Pravda* (10 Nov: Atatürk "the creator and the pioneer of many reforms" — the
Republic, national banks and industry, railways, the Latin alphabet, women's rights; a list of reforms, not an
obituary of feeling) and *Izvestia* (11 Nov: "the independence movement of the new Turkey depended totally on
Kemal Atatürk… all sincere friends of independent Turkey feel sorrow"; and an undated 1938 *Izvestia* item:
"one of the sincere friends of Turkey, the Soviet Union is in deep sorrow"). (Corrected 2026-10-29: the
"independence movement" line was earlier credited to *Pravda*; on the ministry's page it is captioned *Izvestia*.)
(Do not trust the compilation's attributed first line, "N. S. Khrushchev, President of the Soviet
Union, 10 Nov 1938": Khrushchev held no such office in 1938, so the attribution is an error in the
compilation.)

The card sits at the end of an arc already in the vault: [[Vladimir Lenin]]'s "Turkish Octobrists,"
[[Mikhail Frunze]]'s and [[Kliment Voroshilov]]'s Ankara visits, [[Semyon Aralov]]'s embassy, then the
1938 Soviet obituary that praises the "friend" while skipping the Straits. For the Azerbaijani
view of the same Soviet silence, see [[Mehmed Emin Resulzade]]'s Russian-language article.

## Sources
- Lyulchak, ["'Great Loss for the Turkish People': the Soviet and Turkish Narrative of Mustafa Kemal Ataturk in November 1938"](https://history.jes.su/s207987840033211-1-1), *ISTORIYA* 15:11 (2024), abstract — S (full text not retrievable; references list includes Guseinov 1981 and *Dokumenty vneshnei politiki SSSR* vol. 21)
- ["Russians Hail Inounu as Turkish President; Moscow Newspapers Stress His Friendliness to Soviet," *NYT*, 13 Nov 1938](https://nytimes.com/1938/11/13/archives/russians-hail-inounu-as-turkish-president-moscow-newspapers-stress.html) — J (contemporary; snippet)
- [Turkish Ministry of Culture and Tourism, "Russia" page of foreign tributes](https://ktb.gov.tr/EN-104224/russia.html) — T (quotes; attribution error noted)
- [Istanbul University Press chapter on Turkey, Azerbaijan and Soviet Russia (Lenin's "Turkish Octobrists"; Moscow's hesitation between Kemal and Enver)](https://iupress.istanbul.edu.tr/book/turkish-foreign-policy-during-ataturks-era-1920-1938-caucasia-balkans-middle-east-from-political-economic-social-and-cultural-aspects/chapter/political-social-and-diplomatic-relations-between-republic-of-turkey-and-azerbaijan-and-soviet-russia) — S, snippet
- Lead: [Kasım 1938 Sovyet Basınında Atatürk (academia.edu)](https://academia.edu/37741411/Kas%C4%B1m_1938_Sovyet_Bas%C4%B1n%C4%B1nda_Atat%C3%BCrk)
"""),
]

for n, d in P:
    person(n, **d)
for n, when, b in E:
    note("Events", n, {"type": "event", "when": when, "tags": ["event", "verified"] + (["obituary-corpus"] if "Mourns" in n else ["poetry"])}, b)
print(f"census r3 eurasia: {len(P)} people, {len(E)} cards")
