# -*- coding: utf-8 -*-
# Census round 3 (Oct 2026) — Europe: Toksoy-mined Balkan cards (RO/YU/AL/SE-PL), Spanish press (Tüylü Turan 2019),
# Hungarian pair (Gömbös via Erdem 2009; Magyarság via Rásonyi). Same pipeline as b8/b9.
from _lib import note, person

TOKSOY = ("[Toksoy, \"Atatürk'ün Vefatının Balkanlar ve Ortadoğu Basınındaki Etkilerinin Türkiye'deki Akisleri,\" "
          "*Atatürk Üniversitesi SBE Dergisi*, 2010](https://dergipark.org.tr/en/download/article-file/32009) "
          "— full text in `sources/toksoy-2010-balkan-mideast-press.txt`")

P = [
("Gyula Gömbös", dict(role="Prime Minister of Hungary (Oct 1932 – Oct 1936)", nat="Hungarian", life="d. 1936",
  stance="instrumental admirer — kinship rhetoric in the service of Trianon revision", tags=["statesman", "turanism", "revisionism", "verified"], body="""
The Hungarian prime minister who said it in the plainest words in the census: **"My head is
Turkish."** On 14 October 1932, two weeks into office, he received the Turkish envoy in Budapest
and explained why — three ties: *one race, our Asian-ness*; the high soldierly quality he had
seen in the Turks in the Great War; and **"the great revolution made by your great leader's
genius."** He added that he followed Atatürk's history and language initiatives "with admiration
and attention" (see [[Turkish History Thesis]]).

He then went to Ankara. On **21 October 1933** Atatürk received Gömbös and Foreign Minister
Kálmán Kánya for two hours; to the Hungarian journalists he offered a piece of Turanian theatre
of his own — that in King Géza's day Hungary had been called "Turkey," proved by the inscription
on the Holy Crown of Hungary, *"to Géza, true King of Turkey."* Gömbös's summary of the meeting:
**"Whoever sees and hears His Excellency Kemal Pasha understands why command and leadership are
in his hands"** and "I became convinced that even the most important politicians in Ankara
think of us as kin." The party then sailed to Tekirdağ to open the restored house of the exiled
Prince Rákóczi, 175 Hungarians strong, and Gömbös's Rákóczi speech closed with the Hungarian
anthem.

The gaze has a hook in it. Gömbös's one fixed star was revision of the Trianon settlement;
**his idol was [[Benito Mussolini]] first, Atatürk second** (Erdem), and the Ankara visit was
meant to peel Turkey off the anti-revisionist camp and broker a Turkish–Bulgarian line behind
the Little Entente. Atatürk, whose whole foreign policy was frontiers-as-they-are, gave warmth
and no commitment; when Turkey signed the [[Balkan Pact]] in February 1934 the Hungarian
embassy reported the pact as a Turkish step *against* Turco-Hungarian friendship — and Ankara
spent the next weeks reassuring Budapest by protocol. Turkish diplomatic reports still rate
Atatürk as valuing Gömbös's friendship highly into 1935, and the Turkish press mourned him warmly
in 1936. Compare the kinship idiom with [[Hungary's Parliament Rises, November 1938]] and with
[[Magyarság Reads the Victory, 1920–1923]]: three Hungarian registers of the same man, from
Trianon-shaped hope to state friendship to funeral.

Source caveat: the Istanbul University journal abstract of the Gömbös letter-and-books article
dates his premiership to 1930; Erdem dates it to 1 October 1932, which is the date used here. The
letter and the list of books Gömbös sent Atatürk are the subject of that second article (not
read beyond its abstract).

## Sources
- Erdem, "Atatürk ve Macar Başkanı Gyula Gömbös," *Erdem*, no. 55 (2009) — [full text](https://erdem.gov.tr/tam-metin/223/tur) (fetched; quotes from the Budapest embassy reports, *Turán* 1933, Hungarian legation reports of 1934–35)
- "Macar Başvekili Gyula Gömbös'ün Atatürk'e Gönderdiği Mektup ve Kitaplar Çerçevesinde Türk-Macar Kültürel Münasebetleri," Istanbul University Press / DergiPark journal (journal title not confirmed) — [abstract (İÜ Press)](https://iupress.istanbul.edu.tr/en/journal/rpts/article/macar-basvekili-gyula-gombosun-ataturke-gonderdigi-mektup-ve-kitaplar-cercevesinde-turk-macar-kulturel-munasebetleri) · [DergiPark record](https://dergipark.org.tr/tr/pub/iuydta/article/1117482)
""")),
]

E = [
("Romania Hangs the Black Flags, November 1938", "10–21 November 1938", """
Romania's card is the corpus's best portrait of a **state mourning and a minority mourning at
once**. Per Toksoy's reading of the contemporary Turkish press (*Ulus* 20 Nov, *Kurun* 13 Nov,
*Cumhuriyet* 12 Nov, *Akşam* 13 Nov, *Tan* 13 Nov 1938):

- Every Bucharest daily ran **his photograph and long biographical pieces** on the front page,
  several with his facsimile signature. Official offices were to hang **black flags on 21
  November**, the day of the burial, and a Romanian delegation was announced for the funeral.
- *Universul* called him "one of the greatest men of the time" and "a loyal friend of Romania";
  a second piece in the same paper, signed "Basarya" and described as by a former Ottoman
  minister, named him a founder of the Balkan Entente — see [[Balkan Pact]].
- *Timpul*, under "The Founder of New Turkey Is Dead," ran an **interview two Romanian journalists
  had once had with him**, with Atatürk made to say: *"I never expected reward or gratitude… like
  a gardener who raises flowers with great love and wants nothing from them."* (Provenance of
  the interview not established; it is the Romanian press's own relic.)
- *România*: the sentence it fished out of the early years — "I want to build a country where
  very little politics is done and always work" — and "in one stroke he swept the mildewed
  traditions of the East away."
- *Independența Română*: he will remain "an organizing genius in history, the leader and rescuer
  of a nation." *Curentul*, *Semnalul*, *Viitorul* and others sounded the same note.
- Romanian scholars of the day carried the ideas further. **Prof. George Dragoș**, in the preface
  to his book on Atatürk's life, saw the Turkish awakening as an act of *thought* and ended on
  the picture of the Gazi at his window over the Bosphorus; **Prof. Sabin Opreanu**, who had
  visited Turkey in 1938, made him the front-line general who saved the nation from Western
  imperialism; the historian **Petre Ghiat** (⚠️ Toksoy gives no publication date for the book) prefaced his *Bozkurt Gazi Mustafa Kemal Atatürk'ün
  Buhranlı Hayatı* by calling him a master of war, politics and command unequalled in history
  and used the Grey Wolf as his emblem.
- The **Romanian Turkish-minority press** was a second chorus: *Türk Birliği* (6 Dec 1938) printed
  poems and elegies — "you will not die, Atatürk, while Turkishness exists" — and Toksoy adds,
  separately and not as a claim about this paper, that the Romanian Turkish community regarded him as *its* leader: a 1939 Romanian item calls him "our eternal Chief," and the
  *Çardak* paper devoted an issue to him.

Carol II's Romania was both a Balkan Pact partner and a neighbour with a Turkish minority; the
card's reading is that officialdom, intellectuals and the Turkish minority each saw something different
— a treaty guarantor, a fellow modernizer, a kinsman. For the Romanian statesman of the same
years see [[Nicolae Titulescu]]; for the funeral delegations see [[Foreign Delegations at the Funeral, November 1938]]; the whole corpus: [[Death and State Funeral of Atatürk]].

## Sources
- """ + TOKSOY + """, §D Romanya Basını (pp. 190–195), citing Mustafa Mehmet, "Romanya Türk Basında Atatürk ve Türkiye Cumhuriyeti," *Beşinci Uluslararası Atatürk Kongresi* (Ankara 2005) and Nedret Mağmud, "Romanya'da Atatürk," *Üçüncü Uluslararası Atatürk Sempozyumu* (Ankara 1998)
- Contemporary refs inside Toksoy: *Ulus* 20 Nov 1938 p. 5; *Kurun* 13 Nov p. 10; *Cumhuriyet* 12 Nov p. 5; *Akşam* 13 Nov p. 7; *Tan* 13 Nov p. 9. (Translations are of Toksoy's Turkish; Romanian titles are normalised from his transliterations; the Romanian originals were not seen.)
"""),

("Yugoslav Press, November 1938", "12–14 November 1938", """
Belgrade, Zagreb and Ljubljana: **the Balkan Pact partner's card**, and the one whose editorials
speak most directly to Atatürk's role as a regional guarantor.

- Papers across Yugoslavia gave **12 and 13 November** entirely to him, front-page photographs
  and long, emotional accounts of Turkish grief; public buildings and many houses flew flags at
  half-mast.
- *Pravda* ran twelve major pieces; *Vreme* about twenty, including an editorial recalling the
  moment after **King Alexander's assassination (Marseille, 1934)** when, it says, Atatürk
  cabled the Yugoslavs asking *"Shall I declare mobilization?"* — "a phrase Yugoslavia will never
  forget." (*Vreme*'s own claim; no telegram text seen — see [[Alexander I of Yugoslavia]].)
- *Politika*: "History will inscribe this statesman's name in indelible letters. Atatürk is a man
  of the people; his unbreakable will and powerful intelligence brought him face to face with the
  destiny he defeated, and so he became the **transformer of the new Turkey**" — and, in a second editorial, a recollection of Prime Minister **Milan
  Stojadinović's** first Ankara visit: *"There are eighteen million Turks behind me; they are
  ready, without a word, to sacrifice themselves for Yugoslav brotherhood."* The paper described
  the "chivalrous king" and Atatürk as sharing one conviction — peace for both peoples — and
  noted that Atatürk had followed the king into death four years later.
- *Novosti* (Zagreb), under "The Death of the Great Ally": **"Atatürk's genius did what a
  sultanate could not do in five centuries"** — "our greatest friend and most loyal ally… the
  surest support of Balkan-pact policy."
- Stojadinović sent a condolence telegram; the regents Stanković and Perović (Toksoy: "Kral naibi") called on the Turkish
  ambassador in Belgrade, and a Yugoslav delegation to the funeral was decided.

This is the **alliance reading** of the man — Atatürk as the Balkan Pact's fixed point rather
than as a modernizer — and it is worth setting beside the Albanian and Romanian cards, where the
accent is reform. (Karahasan's later Turkish survey of the Yugoslav press, cited in Toksoy,
credits *Politika* with presenting him as the once-in-a-thousand-years statesman and
*Vreme* with the line that the grave would become "a place of pilgrimage for all Turks.") See
[[Balkan Pact]] and [[Death and State Funeral of Atatürk]].

## Sources
- """ + TOKSOY + """, §E Yugoslavya Basını (pp. 195–197) and footnotes 80–89
- Karahasan, "Mustafa Kemal Atatürk'ün Ölümü Dolayısıyla Yugoslavya Basınının Eseri ve Kişiliği Üzerine Değerlendirmeleri (1938–1988)," *I. Uluslararası Atatürk Sempozyumu* (Ankara 1994), pp. 719–721 (as cited in Toksoy); contemporary refs inside Toksoy: *Tan* 13 Nov 1938 p. 9; *Akşam* 14–15 Nov; *Ulus* 15 Nov; *Kurun* 12–13 Nov; *Cumhuriyet* 12, 14 Nov
- Quotations are via Toksoy's Turkish; the Serbo-Croatian originals were not seen.
"""),

("Albanian Press, November 1938", "13–18 November 1938", """
Tirana in the last year of [[King Zog I]]'s kingdom, under Italian shadow — and an Albanian press
that took the occasion to praise **reform as an example for Albania.** Toksoy, from *Akşam* (14
and 18 Nov 1938) and *Ulus* (14 Nov):

- *Drita*: Atatürk "made his country a Western state, abolished the caliphate and religious
  courts, freed women from the veil" — the revolutionary dimension — and the Albanian nation
  "shares in the great fate of the Turkish nation."
- *Stipi*: to the last minute he was "a veritable saviour" of his nation; in a very short time he
  changed the face of the country and drew a modern state out of the old Turkey, and **"the
  Turkish nation owes its material and moral welfare to him."**
- *Ekspres Poranyi* and *Democratia* are named in the same sentence as the Polish army paper
  (see the Warsaw card); they said he created the new Turkey.
- *Ekorces* (Korçë) ran his portrait on page one and a long life-and-work essay on page two,
  **comparing Mustafa Kemal to Russia's Peter the Great** and closing: "Turkey's name will remain
  in history as the symbol of progress, with its national hero's radiance; Albania feels the
  grief of the Turkish nation."

The Albanian gaze is the only one in the Balkan set that tells its own readers to *follow*: in
a Muslim-majority, newly-secularizing Europe state, Turkey's veil-and-caliphate programme was a
live domestic argument. Compare [[King Zog I]], whose own modernization drew on the Kemalist
model, and the Yugoslav alliance reading in [[Yugoslav Press, November 1938]].

## Sources
- """ + TOKSOY + """, §F Arnavutluk Basını (p. 197) and footnotes 90–93 (*Akşam* 14 Nov 1938 p. 2, "Arnavut Milleti Büyük Kaderimize İştirak Ediyor"; *Akşam* 18 Nov p. 7; *Ulus* 14 Nov p. 3)
- Titles are as Toksoy prints them (*Stipi* may be *Shtypi*); Albanian originals not seen.
"""),

("Two Spains Mourn, November 1938", "10–30 November 1938", """
Spain in November 1938 was in the last third of a civil war — and **both camps' newspapers
reported the death**. Esin Tüylü Turan's survey of the Spanish-language press (2019) rests on a
day-by-day reading of Republican titles (*La Vanguardia*, *Solidaridad Obrera*, *CNT*, *La
Libertad*, *Frente Rojo*…) and
Nationalist-zone provincial dailies (*Diario de Burgos*, *El Diario Palentino*, *El Día de
Palencia*, *Heraldo de Zamora*), plus other titles in the same database (*Diario de la Marina*, *La
Prensa*, *El Progreso*…). What they printed:

- 10–11 Nov: the death, the Turkish government's proclamation ("we will continue the great
  work… the Republic… the youth will follow Atatürk's path") and the presidency question. The
  slips are the charming part — **"Kemal Atakur,"** "Ismail Kemal Atatürk," birth years of 1879
  and 1882, the hour of death given as 9.45.
- Tributes: "a **genius of politics** who instilled his people with faith and confidence by his
  dynamism"; the man who "Europeanized Turkey and made her a power through his nationalist
  movement," who understood his country's strategic place in the Mediterranean and fought for
  economic independence; one report held that **"Father of the Turks" was a title he deserved**.
- 12 Nov: Spain's government sent a condolence message to the Speaker of the Grand National
  Assembly, Abdülhalik Renda, and President **Manuel Azaña** wrote on behalf of the Republic; the
  Turkish Foreign Ministry's thanks were carried by the papers.
- **18 Nov: the Negrín cabinet decided to send a mission to Ankara** — Communications Minister
  **Bernardo Giner de los Ríos**, Gen. Riquelme, Vice-Adm. Matz and Rear-Adm. Fuentes, with the
  chargé Calderón (see [[Foreign Delegations at the Funeral, November 1938]]). A Sunday Times
  story that the mission's plane had crashed at Malta was copied by many papers and then mocked
  in the Spanish press itself on 23 November.
- The funeral narrated in detail: torches before the Assembly, 101-gun salute, "more than
  100,000 expected," the embalming misreported (it was taxidermy-style preservation, as the
  Turkish scholar Boran notes), the funeral on the 21st, the 500,000-lira credit.

The reading: a country that had spent the 1920s watching "Kemal Pasha" through neutral eyes
(Gündüz 2020 on Spanish papers of 1918–23, abstract only) now put him on the page *during* a war
with the same instinct — "a strong man who modernized" — on both sides of the lines. The
Republican state treated it as a **head-of-state funeral that merited a ministerial mission, in the
middle of its own battle for survival**; whether Franco's Burgos sent anyone is unknown. Not yet
established: any Falangist or ABC (Seville) editorial. A circulating one-line Spanish quote
("Atatürk is a lofty mountain peak…" credited to *Arriba*) comes only from a listicle and is
parked in `candidates/europe.md`.

## Sources
- Tüylü Turan, "İspanyolların Gözünden Atatürk'ün Vefatı ve Cenaze Merasimi," *Tarih Okulu Dergisi* XXXIX (2019), [doi:10.14225/JOH1567](https://doi.org/10.14225/JOH1567) — text and 71 footnotes read via [Academia mirror](https://academia.edu/41493219/%C4%B0SPANYOLLARIN_G%C3%96Z%C3%9CNDEN_ATAT%C3%9CRK%C3%9CN_VEFATI_VE_CENAZE_MERAS%C4%B0M%C4%B0) (page numbers of the journal not verified)
- Press citations from that article's notes: *Diario de Burgos* 11–22 Nov 1938; *El Diario Palentino* 11–30 Nov; *CNT* 10 Nov; *Solidaridad Obrera* 11–13 Nov; *La Vanguardia* 11, 16 Nov; *Diario de la Marina* 11–21 Nov; Azaña's telegram per *Atatürk'ün Ölümü Dolayısiyle Yabancı Ülkelerden Büyük Millet Meclisine Gelen Taziyetnameler*, vol. 2 (TBMM)
- Gündüz, "İspanyol Gazetelerinde Türk Millî Mücadelesi…," *Atatürk Araştırma Merkezi Dergisi* 37:103 (2020), [doi:10.33419/aamd.926430](https://doi.org/10.33419/aamd.926430) — abstract only
"""),

("Magyarság Reads the Victory, 1920–1923", "Dec 1920 – 1923", """
An eyewitness's account of how **Hungary's press first read Kemal Pasha** — before there was a
republic, a president or an Atatürk. In "Atatürk Özgürlük Savaşı'nın Macar Basınında Yankıları,"
the Hungarian Turkologist **László Rásonyi** (who writes that he himself was in Istanbul for the
Gazi's triumphal entry) takes two Budapest dailies to stand for the whole press:

- ***Pesti Hírlap*** (founded 1840) — the old, cautious paper, which relayed the French, British
  and American press and so, Rásonyi says, repeated the Greek victory reports as written, in the
  *Sèvres-and-Trianon mentality*.
- ***Magyarság*** ("Hungarianness"), founded at the end of December 1920 by people who did not
  believe the hostile news about the Turks, **sent its own correspondents to Turkey in mid-war,**
  and became "the defender of Turkish interests." Rásonyi's chronological abstract of its
  columns: 14 Jan 1921, joy that the Turks had breached the Greek front in three places (First
  İnönü); a lecture by the Turkish consul in Budapest on the beginnings of Turkish
  modernization; 5 Aug 1921, scepticism of Athens's victory bulletins ("the Greek agency has not
  accustomed us to news of victory"); 7 and 27 Sep, 7 Oct, "great sympathy for Kemal Pasha"; 23
  Oct, **Europe bows its head to "small-minded" treaties; Turkey did not — "because at its head
  stood a Kemal Pasha and a country capable of solving things."**
- September 1922: *"Kemal Pasha drove the Greeks out of Anatolia"*; the leading article **"The
  Sick Man"** (6 Sep 1922) turns the epithet round — the Paris-world's "sacred" treaties were
  broken by the "Sick Man" shaking his tired arm; *"Where are the Sick Men of Central Europe? Will
  our own Mustafa Kemal come out of the beehive of time?"* — evidently Hungary's wounded self-pity
  borrowing the Turkish victory.
- 9 Oct 1922: leading article **"The Rising Crescent"** — the Turkish cavalry in Istanbul, the
  crescent as "the sword of racial consciousness and heroic resistance… an example for all
  oppressed peoples." And at Lausanne the paper credited "two exceptional men, Mustafa Kemal Pasha
  and İsmet İnönü."

The Hungarian mirror here is **Trianon**: Atatürk as the proof that a defeated Central-European
nation could still throw down a dictated peace. It was a bearable thing to think about Turks —
and an unbearable thing to think about Hungary — which is why the paper kept coming back to it.
Compare [[Gyula Gömbös]] (the same hope as policy) and [[Hungary's Parliament Rises, November 1938]] (the same man mourned). See also [[Treaty of Sèvres]], [[Treaty of Lausanne]],
[[Greco-Turkish War]].

## Sources
- L. Rásonyi, "Atatürk Özgürlük Savaşı'nın Macar Basınında Yankıları," *Belleten* XLV, pp. 79–86 — [DergiPark PDF](https://dergipark.org.tr/en/download/article-file/2523850) (read in full; quotations are Rásonyi's/the journal's Turkish renderings of the Hungarian; the exact issue date was not given in the page text)
"""),
]

for name, kw in P:
    person(name, **kw)
for n, when, b in E:
    tags = ["event", "verified"] + (["obituary-corpus"] if "1938" in when else [])
    note("Events", n, {"type": "event", "when": when, "tags": tags}, b)

print(f"census r3 europe: {len(P)} people, {len(E)} events")
