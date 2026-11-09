# -*- coding: utf-8 -*-
# Census round 3 — HUNT seam 5: the funeral delegations (21 Nov 1938) + Dağlı's telegram/letter corpus.
# Primary route: Delpher (KB) Havas/Reuter wires of 13-26 Nov 1938, resolved to OCR; scholarly layer:
# Tüylü Turan 2019 (Spanish press), Uyanıker 2020 (naval logs), Dağlı 2023 (sources/ PDF).
from _lib import note, person

DELPHER = "http://resolver.kb.nl/resolve?urn="

EVENT = ("Foreign Delegations at the Funeral, November 1938", "17–25 November 1938", """
**The seam-5 table, built from the wires.** Atatürk's state funeral in Ankara on 21 November 1938
([[Death and State Funeral of Atatürk]]) is usually summarised as "28 countries" — a number that
this card could not source. What *can* be sourced is a layered record: a **Havas dispatch of 17
November** that named the special delegations in advance (it ran in at least four Dutch papers), a
**22 November post-event report** repeating the list in the past tense, Reuter's account of the
cortege, and the scholarly layer (Tüylü Turan 2019 on the Spanish press; Uyanıker 2020 on the
navy's logs; the Soviet archival reports summarised in a Turkish-press feature). The rank each
capital sent is a measurable weight of regard — and the list contains two corrections to what the
vault had inherited from Wikipedia.

## The three rings

1. **At sea (19 Nov, Istanbul).** Six foreign warships anchored off Haydarpaşa and escorted the
   *Yavuz* carrying the coffin toward İzmit: British battleship *Malaya* (Admiral Sir Dudley Pound,
   C-in-C Mediterranean), Soviet destroyer *Moskva* (Black Sea Fleet commander Admiral Yumashev),
   French cruiser *Émile Bertin* (Capt. Robert Battet), Romanian destroyer *Regina Maria*, Greek
   destroyer *Hydra*, German cruiser *Emden* (Kapitän zur See Paul Wever). An Italian warship was
   to come but did not arrive in time (Uyanıker 2020, n.62, citing Atabey 2012). Irony noted in the
   Turkish literature: *Malaya* was the ship that carried the last sultan into exile on 17
   November 1922; Ankara raised no objection to her coming.
2. **On land (21 Nov, Ankara).** Special delegations of statesmen, plus **military detachments
   from Britain, France, Iran, Greece, Bulgaria, Yugoslavia and Romania** (Havas) — the "nine
   armed detachments" of the English Wikipedia sentence, of which it names the British, Iranian
   and Yugoslav. The foreign delegates saluted the coffin from the balcony of Ankara Palace on
   20 November, and followed it, behind the family and cabinet, on 21 November.
3. **Geneva.** The League of Nations sent its deputy chief and two officials (Spanish press, citing
   the League's own monthly bulletin).

## The table

Tiers: **P** = contemporary wire/archive; **S** = scholarly article citing contemporary press or
archives; **J** = journalism citing archives; **T** = Wikipedia only (a country-name with no
delegate and no second source — treat as unverified).

| Country | Delegate(s) | Role | Source | Tier |
|---|---|---|---|---|
| France | [[Albert Sarraut]] | Interior Minister, head of delegation; reached Istanbul 18 Nov; still in Ankara on 25 Nov | Havas 17 Nov · Havas 25 Nov · Tüylü Turan 2019 | P+S |
| Germany | [[Konstantin von Neurath]] | Minister without portfolio; "the Führer will be represented by a delegation under Neurath", arriving 19 Nov | Berlin wire 18 Nov · Havas 17 Nov | P |
| Italy | Baron Pompeo Aloisi | senior diplomat, ex-delegate to the League | Havas 17 Nov · Tüylü Turan 2019 | P+S |
| USSR | [[Vladimir Potemkin]]; Adm. Yumashev; Amb. Terentyev | First Deputy Foreign Commissar; fleet commander; ambassador | Havas 13 Nov · Havas 17 Nov · NRC 26 Nov · Soviet archive summary | P+J |
| United Kingdom | Field Marshal Lord Birdwood (for George VI); Adm. Sir Dudley Pound; 200 marines and the band of *Malaya* | royal representative; C-in-C Mediterranean | Reuter 21 Nov · Havas 17 Nov · Uyanıker 2020 | P+S |
| Greece | [[Ioannis Metaxas]] | Prime Minister, in person; destroyer *Hydra* (Capt. Ikonomu) + army detachment | Havas 17 Nov · Havas 12 Nov via [[Salonika Names His Street, November 1938]] | P |
| Yugoslavia | Army Gen. Nedić (⚠️ **Milutin** by inference from the minister list; the sources give only "Nedić"/"minister of war") | Minister of the Army and Navy; plus military detachments | Havas 17 Nov ("minister of war") · Boran 2011 p.512 via Tüylü Turan · ministers list | P+S+T |
| Bulgaria | Minister of War (name not in wire) + detachment | — | Havas 17 Nov | P |
| Romania | Minister of Air (name not in wire) + detachment; destroyer *Regina Maria* (Lt-Cdr Macellariu) | — | Havas 17 Nov · Uyanıker 2020 | P+S |
| Albania | Minister of Justice (name not in wire) | — | Havas 17 Nov | P |
| Afghanistan | "an uncle of the King" (name not in wire) | royal envoy of Zahir Shah | Havas 17 Nov · Tüylü Turan 2019 (Afghan commission in Istanbul 18 Nov) | P+S |
| Iran | military detachment (named delegate not found) | guard of honour | Havas 17 Nov | P |
| Spain (Republic) | Bernardo Giner de los Ríos (Communications), Gen. Riquelme, Vice-Adm. Matz, Rear-Adm. Fuentes, chargé Calderón | cabinet decision of 18 Nov under Negrín | Tüylü Turan 2019 (Spanish press) | S |
| League of Nations | "F. Walters" (given as Secretary-General; F. P. Walters was in fact Deputy Secretary-General — M), Aghnides (Disarmament Section), Erim (Political Section) | secretariat | Tüylü Turan 2019 citing the League bulletin | S |
| Belgium, Czechoslovakia, China, Denmark, Egypt, Estonia, Finland, Hungary, Iraq, Japan, Latvia, Lithuania, Netherlands, Norway, Poland, Sweden, Switzerland, Syria, United States | — | listed as "dignitaries" with no name | English Wikipedia | T |

## What the inherited list got wrong

- **"Milan Nedić for Yugoslavia" is the wrong Nedić.** The Minister of the Army and Navy from 25
  August 1938 to 26 August 1939 was Army General **Milutin** Nedić (1882–1945); **Milan** Nedić
  (1877–1946) — the later head of Serbia's German-installed puppet government — only became minister
  in August 1939 and in 1938 held no such post. The scholarly source (Boran 2011, via Tüylü Turan)
  says only "Defence Minister Nedić"; the Wikipedia table, and the vault card until this round,
  attached the name that history remembers. The Spanish press also announced Prime Minister
  Stojadinović would come; Havas and Boran say the War Minister did. ⚠️ The first name "Milutin" is our
  inference from the minister's tenure (Aug 1938–Aug 1939); no source read here gives it, and Havas speaks of
  "military detachments", not specifically a guard of honour.
- **Amanullah Khan's attendance is contradicted, not corroborated.** Havas's 17 November list gives
  Afghanistan as represented "by an uncle of the King" — i.e. Zahir Shah's family, the dynasty that
  replaced Amanullah — and Tüylü Turan has an Afghan commission arriving in Istanbul on 18 November.
  No contemporary or scholarly source seen puts the exiled ex-king in Ankara. The Wikipedia
  Afghanistan–Turkey page (T) says only that he "made a special attendance" from Rome, with no
  citation. See [[Amanullah Khan]].
- **The headline counts disagree.** "Seventeen nations" (Wikipedia) fits the
  Havas special-delegation list almost exactly; "28 countries" (vault inheritance) and the 32-name
  Wikipedia table could not be traced to a primary source this round. One plausible reconciliation
  (inference): Reuter's order of march puts "delegations of foreign powers, members of the Turkish
  parliament, the diplomatic corps" behind the family and cabinet, so a 28-country count may
  include resident envoys rather than 28 dispatched delegations.

## Two portraits from the margins

- **Potemkin stayed.** The Soviet First Deputy Commissar was announced on 13 November, laid a
  wreath on the Atatürk monument on 15 November and at the coffin on 20 November, met the foreign
  committees with İnönü on 22 November — and was, by NRC's Istanbul correspondent on 25 November,
  "the last of the foreign representatives to leave," his long stay noted in diplomatic circles:
  İnönü, newly president, had asked him to delay. The funeral doubled as the first Soviet–Turkish
  talks of the post-Atatürk era.
- **Sarraut stayed too** — Havas, 25 November: the French interior minister "has not yet returned
  from Ankara, where he attended the interment", so the premier took his portfolio ad interim.

## Before the funeral: the letters of strangers (Dağlı 2023)

Erkan Dağlı's article mines the Presidential Archive (CA) for what ordinary foreigners sent during
the illness and after. Named senders, with what they wrote:

- **Abdullah I of Jordan**, April 1938 telegram: read of the illness in the paper, "anxious and
  distressed" ([[Abdullah I of Jordan]]; CA 01008484-2).
- **Dr André Pirim (of the Kasapyan family, for Turkey's Armenian Catholics)** and **Archbishop
  Boğos Kireçyan**, spiritual head of the Armenian Catholics, 2–3 April 1938: wishes for health and prayers that Atatürk shelter the young
  republic "for years under your wings" (CA 01019988-116, -106).
- **İvan Dimitrof**, a Sofia teacher, 8 August 1938: a folk cure for the swollen belly — a short
  length of wood pressed upright on the navel, the "Tree of Life" (CA 01019578-80).
- **Raul D. Gherculescu**, 20 October 1938, son of a Romanian military attaché whom Atatürk had
  met in Sofia in 1913: "I keep the dearest memories of my childhood of you" (CA 01019989-148).
- **Herta Seitner** (German woman recommending a doctor, 25 Oct), **Milan Bukelitsa**, merchant of
  Valjevo, Serbia (26 Oct: wishes "for the happiness of the Turkish and Balkan peoples"),
  **Wilhelm Bauer** and **Walter Hüller** (Germans), **Rose Reichenbach** (medication advice) and
  **Dr Jean Billac** (a French physician offering a cure, with patient addresses as proof; 21
  Oct) — the grassroots tail of a famous illness.
- **Professor Noël Fiessinger**, the Paris physician who examined him on four trips, cabled
  condolences after the death (CA 02011847-86) — see [[Noël Fiessinger]].
- **Four schoolboys of Comilla Zilla School, Bengal**, wrote after the death that they hoped his
  soul would sleep in peace (CA 01016478-142).

Dağlı also reproduces press tributes (Pester Lloyd, NZZ, Kölnische Volkszeitung, Völkischer
Beobachter, Zora, Al-Ahram, the New York *World-Telegram*, Atinaika Nea); the Italian *Giornale
d'Italia* of 12 November ignored the death and ran "İsmet İnönü" instead. Those are the country
cards' business ([[Dutch Press, November 1938]], [[Bulgarian Mourning, November 1938]]).

## What this card does not yet settle
Names of the Bulgarian, Romanian, Albanian and Afghan envoys; the Iranian, Japanese, Polish,
Hungarian and American delegates; whether Francoist Spain sent anyone; the origin of "28". The
Ulus issue of 16 November 1938 ("Yabancı devletleri temsil edecek heyetler") and Boran 2011 (Atatürk
Yolu 47, pp. 488–520) almost certainly hold the full list — see `candidates/funeral-delegations.md`.

## Sources
- Havas via KB/Delpher: [17 Nov, "De begrafenis van Kemal Ataturk"](%sddd:011154698:mpeg21:a0014:ocr) · [17 Nov, Handelsblad-type copy](%sMMKB27:021093077:mpeg21:a00077:ocr) · [17 Nov, "Voorbereiding"](%sddd:010018135:mpeg21:a0116:ocr) · [13 Nov, Potemkin](%sKBNRC01:000055598:mpeg21:a0084:ocr) · [22 Nov, "Kemal Ataturk's uitvaart"](%sddd:010607514:mpeg21:a0062:ocr) · [25 Nov, Sarraut](%sddd:011154706:mpeg21:a0097:ocr) · [25 Nov, NRC, Potemkin](%sKBNRC01:000055669:mpeg21:a0041:ocr) · [18 Nov, Berlin wire](%sddd:011122900:mpeg21:a0009:ocr) · [Reuter 21 Nov](%sddd:011122906:mpeg21:a0115:ocr) (P)
- Tüylü Turan, "İspanyolların Gözünden Atatürk'ün Vefatı ve Cenaze Merasimi", *Tarih Okulu Dergisi* 2019, [doi:10.14225/JOH1567](https://doi.org/10.14225/JOH1567) (S)
- Uyanıker, "Atatürk'ün Vefatı Sonrası Deniz Kuvvetlerindeki Hazırlıklar ve Gemi Jurnalleri Işığında Donanmanın Atatürk'e Vedası", *Akademik Tarih ve Düşünce Dergisi* 7/3 (2020), pp. 1867–1913, [PDF](https://tigindergisi.com.tr/Makaleler/3e72c116-a40c-4c1b-bbb4-6a78f36febb3.Pdf) (S)
- Boran, "Atatürk'ün Cenaze Töreni: Yas ve Metanet", *Atatürk Yolu* 47 (2011), pp. 488–520 — cited at second hand through Tüylü Turan (S)
- [Dağlı, *Pamukkale Üniv. SBE Dergisi* 57 (2023), pp. 119–136](https://doi.org/10.30794/pausbed.1170334), full text in `sources/` (S; Cumhurbaşkanlığı Arşivi refs as cited)
- ["The secret report to Stalin", United World International](http://uwidata.com/32284-the-secret-report-to-stalin) (J, citing RGAVMF f. r-1678 and AVPRF)
- [Anadolu Ajansı photo feature, Nov 2025](https://aa.com.tr/tr/kultur/arsiv-fotograflari-buyuk-onder-ataturkun-son-yolculugundaki-kederi-gozler-onune-seriyor/3738866) (J)
- [Wikipedia: State funeral of Mustafa Kemal Atatürk](https://en.wikipedia.org/wiki/State_funeral_of_Mustafa_Kemal_Atat%%C3%%BCrk) · [Ministry of Defence (Yugoslavia)](https://en.wikipedia.org/wiki/Federal_Secretariat_of_People%%27s_Defence) (T)
""" % ((DELPHER,)*9))

P = [
("Albert Sarraut", dict(role="French statesman; Interior Minister; head of France's funeral delegation", nat="French", life="1872–1962",
  stance="admiring mourner (by his own stated word) — and, in one Dutch daily's reading, a sign of the West's courtship of Ankara", tags=["funeral-delegate", "diplomat", "verified"], body="""
Radical-Socialist senator, twice premier (1933, 1936) and twice Governor-General of French
Indochina (1911–14, 1917–19), Interior Minister in the Daladier government of 1938 (Britannica).
When Atatürk died, Paris did not send an ambassador: it sent **Sarraut himself**, at the head of a
delegation that reached Istanbul on 18 November (Tüylü Turan 2019, from the Spanish press) and
that Havas announced on the 17th. A Dutch daily read the choice as a signal in its own right — that
"the French Minister of the Interior personally headed a delegation" to meet German and British
delegations there "shows the great weight the Western powers now attach to Turkey's friendship"
(Nov 17). He stayed through the week: on 25 November Havas reported him "not yet returned from
Ankara, where he attended the interment," the premier covering his portfolio.

**What he said himself.** Sarraut had been France's ambassador in Ankara, and Toksoy's 2006 survey of
the Turkish press (from *Ulus*, 15 Nov 1938, and *Akşam*/*Tan*) reports a tribute he wrote for the
Turkish papers: Atatürk was "a sincere and loyal friend" of France, and "I felt admiration and
affection for him." On arriving for the ceremony he told the press (*Akşam*, 20 Nov 1938) that he had
felt "deep admiration" for Atatürk ever since his embassy years (translations from Toksoy's Turkish).
The polarity is therefore **admiring on Sarraut's own stated word**; the "courtship of Ankara" reading
is the Dutch daily's comment on the choice of envoy, not anything Sarraut said.


The sharp edge of the card: the man who stood in the cortege for a modernising republic's founder
was, seven months earlier, the minister who (April 1938) called for "methodical, energetic and
prompt action to rid our country of the too numerous undesirable elements" among the refugees
fleeing the Spanish Civil War (Wikipedia; T). The same funeral drew a delegation from that war's
Republican side ([[Bernardo Giner de los Ríos]]). France's other presence at the deathbed was
medical — [[Noël Fiessinger]]. Context: [[Foreign Delegations at the Funeral, November 1938]],
[[Death and State Funeral of Atatürk]].

## Sources
- Havas via Delpher: [17 Nov](%sddd:011154698:mpeg21:a0014:ocr) · [17 Nov commentary](%sddd:010540439:mpeg21:a0058:ocr) · [25 Nov](%sddd:011154706:mpeg21:a0097:ocr) (P)
- Tüylü Turan 2019, *Tarih Okulu Dergisi*, [doi:10.14225/JOH1567](https://doi.org/10.14225/JOH1567) (S) · [Britannica](https://britannica.com/biography/Albert-Sarraut) (T/J) · [Wikipedia](https://en.wikipedia.org/wiki/Albert-Pierre_Sarraut) (T)
- Toksoy 2006, *Atatürk Yolu* 10/37–38, [full text](https://dergipark.org.tr/en/download/article-file/20592), pp. 150–151 and n. 25–27, 59 (Sarraut's tributes and statement; S)
""" % ((DELPHER,)*3))),

("Konstantin von Neurath", dict(role="German diplomat; Hitler's envoy to the funeral", nat="German", life="1873–1956",
  stance="instrumental (⚠️ the vault's inference) — the Reich's courtesy call", tags=["funeral-delegate", "nazi-era", "verified"], body="""
Foreign Minister of Germany from 1932 until Hitler sacked him on 4 February 1938 in the
Blomberg–Fritsch shake-up, he was kept on as a minister without portfolio to soothe foreign
opinion; later Reich Protector of Bohemia and Moravia (1939–43) and, after Nuremberg, a convicted
war criminal (Wikipedia; Nuremberg transcript; T).

On 18 November 1938 — eight days after Kristallnacht, on the same Dutch front pages that carried
the pogrom's fallout — a Berlin wire announced that "the Führer will be represented at the burial
of Kemal Atatürk by a delegation under Minister von Neurath," arriving in Ankara the next day;
Havas's list and the 22 November post-event report name him. So Berlin sent a diplomat of the old
Wilhelmstrasse school rather than a Party figure — an **inference**, but a pointed one given
that the man it chose had been removed from the foreign ministry nine months earlier. The German
warship off Istanbul, the cruiser *Emden* under Kapitän zur See Paul Wever, took part in the sea
procession, and a Soviet admiral's report records tension when *Emden*'s officers photographed the
Soviet destroyer at close range. German press pages of those days are the subject of the German-press
cards; Hitler's own line to Turkish visitors is in [[Adolf Hitler]]. Context:
[[Foreign Delegations at the Funeral, November 1938]].

## Sources
- Berlin wire, 18 Nov 1938, via Delpher: [ddd:011122900:mpeg21:a0009](%sddd:011122900:mpeg21:a0009:ocr) · [Havas 17 Nov](%sddd:011154698:mpeg21:a0014:ocr) · [22 Nov](%sddd:010607514:mpeg21:a0062:ocr) (P)
- Uyanıker 2020 (*Emden*, Capt. Wever) (S) · [Wikipedia](https://en.wikipedia.org/wiki/Konstantin_von_Neurath) · [Jewish Virtual Library](https://jewishvirtuallibrary.org/jsource/Holocaust/Neurath.html) (T)
""" % ((DELPHER,)*3))),

("Vladimir Potemkin", dict(role="Soviet First Deputy Foreign Commissar; historian of diplomacy", nat="Soviet (Russian)", life="1874–1946",
  stance="instrumental — Moscow's envoy and the last guest to leave", tags=["funeral-delegate", "diplomat", "verified"], body="""
A Moscow schoolteacher turned Bolshevik educator, Potemkin entered diplomacy in 1922 and served as
Soviet envoy in **Greece (1929–32), Italy (1932–34) and France (1934–37)** before becoming First
Deputy People's Commissar for Foreign Affairs (1937–40); from 1940 People's Commissar of Education
of the RSFSR and editor of the multi-volume *History of Diplomacy* (Great Soviet Encyclopedia
entry; JSTOR review). Moscow named him as its funeral representative on 13 November (Havas), and
he sailed to Istanbul aboard the destroyer *Moskva* with Black Sea Fleet commander Admiral Yumashev
and Ankara ambassador Terentyev: 4 officers and 100 men, 40 of the officers going on to Ankara. They
laid wreaths at the Atatürk monument (15 Nov) and at the coffin (20 Nov); a secret Soviet naval
order of 12 November told sailors to go ashore in groups of three to five and not to discuss state
affairs. İnönü met the foreign committees on 22 November.

The telling detail comes from the Dutch press of 25–26 November: Potemkin was **the last of the
foreign representatives to leave Ankara**, and his long stay drew comment in diplomatic circles —
the new president İnönü, once a friend of good relations with Russia and now worried about
"friction" between the two countries, had asked him to put off his departure for a few days.
The burial of the founder doubled as the opening round of Soviet–Turkish business under his
successor. (The Soviet side had cabled condolences from Kalinin and Litvinov on 11 November;
Turkish Wikipedia, T.) Context: [[Foreign Delegations at the Funeral, November 1938]]; the
Soviet-era relationship runs through [[Semyon Aralov]] and [[Kliment Voroshilov]].

## Sources
- Delpher: [NRC, Havas 13 Nov](%sKBNRC01:000055598:mpeg21:a0084:ocr) · [NRC 25–26 Nov](%sKBNRC01:000055669:mpeg21:a0041:ocr) · [Havas 17 Nov](%sddd:011154698:mpeg21:a0014:ocr) (P)
- ["The secret report to Stalin", United World International](http://uwidata.com/32284-the-secret-report-to-stalin) (J; cites RGAVMF f. r-1678 l.1 d.32 and AVPRF) · Tüylü Turan 2019 (S)
- [Great Soviet Encyclopedia entry](https://encyclopedia2.thefreedictionary.com/Vladimir+Petrovich+Potemkin) · [Wikipedia](http://en.wikipedia.org/wiki/Vladimir_Potemkin) (T/S)
""" % ((DELPHER,)*3))),

("Bernardo Giner de los Ríos", dict(role="Spanish architect-politician; Minister of Communications, Transport and Public Works (Republic)", nat="Spanish", life="1888–1970",
  stance="witness — a Republic at war mourns a founder", tags=["funeral-delegate", "spanish-civil-war", "verified"], body="""
A school-building architect (school inspector in Levante, builder of many Madrid schools) and
Republican deputy, he held the Communications, Transport and Public Works portfolio through the whole of the Civil War,
then went into exile — Santo Domingo, Mexico, Paris — and served the Republic-in-exile as secretary
general of the presidency (Wikipedia; T).

On 18 November 1938, a cabinet meeting under Prime Minister Juan Negrín decided to send a
commission to Ankara "to represent the Spanish Republic," and it consisted of Giner de los Ríos,
General Riquelme, Vice-Admiral Matz, Rear-Admiral Fuentes and the Republic's representative in
Ankara, Calderón (Tüylü Turan 2019, from the Spanish press). With the war nearing its end, the
Republic spent five senior men on a funeral far from its front — the same Republic whose refugees
the French delegation's leader ([[Albert Sarraut]]) had been moving to curb that spring. The
Spanish press also chewed on a **rumour that the generals' aeroplane had crashed at Malta** (a
*Sunday Times* item copied by agencies), which another paper mocked on 23 November: the plane
that "crashed" at Malta had gone on to Ankara. Whether Franco's Burgos sent anyone is **not
established**: Tüylü Turan's corpus is Nationalist- and Republican-zone press and reports only the
Republican commission. Context: [[Foreign Delegations at the Funeral, November 1938]].

## Sources
- Tüylü Turan, "İspanyolların Gözünden Atatürk'ün Vefatı ve Cenaze Merasimi", *Tarih Okulu Dergisi* 2019, [doi:10.14225/JOH1567](https://doi.org/10.14225/JOH1567), citing *El Progreso*, *Diario de la Marina*, *La Prensa*, *Diario de Burgos*, *CNT* and others, 12–30 Nov 1938 (S)
- [Wikipedia: Bernardo Giner de los Ríos](https://en.wikipedia.org/wiki/Bernardo_Giner_de_los_R%C3%ADos) (T)
""")),

("Noël Fiessinger", dict(role="Paris professor of medicine; Atatürk's foreign consultant, 1938", nat="French", life="1881–1946",
  stance="witness — the clinician who named the end in June", tags=["physician", "witness", "verified"], body="""
The Paris professor of medicine whom Prime Minister Celâl Bayar urged Atatürk to call in from Paris. Per
Dağlı (2023), citing Kocatürk, Kodal and others, he examined Atatürk in Ankara on **28 March 1938**
(reassuring: a month and a half of rest), again aboard the yacht *Savarona* in Istanbul on **8–10
June**, again in Istanbul on **6 September** when the first abdominal puncture was done, and was
consulted **by telephone** during the October coma; the death report of 10 November names his
diagnosis — "hepatite sclérocongestive éthylique" — made with Prof. Neşet Ömer İrdelp. The official
communiqués spelled him "Piesenje."

His private prognosis is the source's most quoted passage: at Interior Minister [[Şükrü Kaya]]'s
dinner table in June 1938, after Atatürk had told Kaya "talk about everything, everything,"
Fiessinger said: *"Now we are all aboard a ship that has met with an accident... With medicine's
help and nature's, Atatürk could live two more years. But tonight we go to bed and might find him
dead of an intestinal or brain haemorrhage. So take now the measures the Republic's safety
requires"* (Şehsuvaroğlu 1981:77, via Dağlı). After the death he cabled condolences from Paris
(Presidential Archive 02011847-86) — one of the few named foreigners in Dağlı's corpus who was
neither head of state nor stranger. A French physician at the bedside, a French minister at the grave:
[[Albert Sarraut]]. Context: [[Foreign Delegations at the Funeral, November 1938]].

## Sources
- Dağlı, "Yabancı Ülkelerden Atatürk'ün Hastalığı ve Vefatı İçin Gönderilen Kişisel Telgraflar", *Pamukkale Üniv. SBE Dergisi* 57 (2023), pp. 119–136, [doi:10.30794/pausbed.1170334](https://doi.org/10.30794/pausbed.1170334) (S; full text in `sources/`)
- [Atatürk Ansiklopedisi: Noel Fiessinger (1881–1946)](https://ataturkansiklopedisi.gov.tr/bilgi/noel-fiessinger-1881-1946/) (S/T, as cited by Dağlı)
""")),
]

if __name__ == "__main__":
    name, when, body = EVENT
    note("Events", name, {"type": "event", "when": when, "tags": ["event", "verified", "obituary-corpus"]}, body)
    for n, kw in P:
        person(n, **kw)
    print("ok:", name, len(P), "people")
