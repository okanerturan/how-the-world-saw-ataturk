# -*- coding: utf-8 -*-
# Census round 3 (Oct 2026) — Asia / Africa / Oceania promotions from candidates/asia-africa-oceania.md.
# Routes: Papers Past article fetch (NZ), DergiPark/ATAM abstract (Qureshi), ORA Oxford accepted manuscript (Zaman),
# JIMK/IIUM abstracts (Malaya), UJ thesis PDF via Wayback (Orakçı), Chiba bibliography (Japan), Toksoy 2010 full text (India).
from _lib import note, person

P = [
("Rabindranath Tagore", dict(role="Poet, Nobel laureate (1913); founder of Visva-Bharati", nat="Indian (Bengali)", life="1861–1941",
  stance="admiring — 'resurgent Asia', and a book request", tags=["letters", "asia", "verified"], body="""
Tagore never met Atatürk, but the paper trail between them is the cleanest literary one the
Indian column has. Three strands, each sourced:

- **Istanbul, 21–22 November 1926.** Tagore's ship put in at Istanbul on the way home from his
  European tour; he stayed aboard in poor health but received the press in his cabin. Eyüp Özveren
  (in Jassal & Turan's edited volume), working from *Cumhuriyet* of 23 Nov 1926, reports him saying
  that the Turkish president "showed us the way to civilization." An *Urdu* correspondent of
  *Rozana Hamdard* — the daily of Muhammad Ali Jauhar's Khilafat-era journalism — asked about
  the Turkish revolution and printed his answer: he held it "in high regard" and believed it
  would shape "a promising future not only for Türkiye, but for the broader Eastern world."
- **The books.** Back in India he wrote to Atatürk asking for books on Turkey and Turkish
  literature for the library at Visva-Bharati; Atatürk sent **41 volumes**, still kept there as
  "treasures of the university" — Vajpayee said so at the Tagore bust unveiling in Ankara.
- **The 1932 travelogue and the 1938 shutdown.** The Indian scholar Ramkrishna Bhattacharya
  (*Frontier*) notes that Tagore commended Kemal Pasha "with unconcealed admiration" in his Persia
  travelogue (*Japane Parasye*, written 1932–33; English *Journey to Persia and Iraq*, p. 31) and in
  a *Modern Review* essay of October 1932 — a pairing of Kemal with [[Reza Shah Pahlavi]] as the
  architects of the two new Asian states. And **classes at Santiniketan were suspended on
  18 November 1938** after Atatürk's death.

His place in the deck: the **poet's version of the "resurgent East" mirror** — a man who spent
the 1910s lecturing against nationalism (*Nationalism*, 1917) yet made an exception for the one
nationalism that had thrown out an empire *and* a priesthood. The exception is the data.

*Caveat:* some popular write-ups (e.g. Indo-Islamic blogs) date a Tagore–Atatürk "meeting" to
1922; the scholarly and press record puts the only contact at the 1926 Istanbul stopover, and
Vajpayee himself says they never met.

See [[Khilafat Disillusion, 1924]], [[India Mourns, November 1938]], [[Kemalism]].

## Sources
- Ramkrishna Bhattacharya, "The World Comes First: Tagore and his Nationalism," *Frontier* 51(45) — [frontierweekly.com](https://frontierweekly.com/articles/vol-51/51-45/51-45-Tagore%20and%20his%20Nationalism.html) (cites *Rabindra-rachanabali* 12:449–50; *Journey to Persia and Iraq*, p. 31; *Modern Review* Oct 1932; Bandyopadhyaya vol. 3:143)
- [Daily Sabah, "When Rabindranath Tagore first visited Istanbul"](https://dailysabah.com/arts/portrait/when-rabindranath-tagore-first-visited-istanbul) — quotes *Rozana Hamdard* (Dec 1926) and Özveren in Jassal & Turan (eds.), citing *Cumhuriyet* 23 Nov 1926
- [Telegraph India, "Tagore bust and avenue in Turkey"](https://telegraphindia.com/india/tagore-bust-and-avenue-in-turkey/cid/965506) · [Anadolu Agency, 2019](https://u.aa.com.tr/en/asia-pacific/iconic-indian-poet-commemorated-in-turkey/1473757) — 41-book gift
""")),

("C.E.W. Bean", dict(role="Australian war correspondent at Gallipoli; official historian of the AIF", nat="Australian", life="1879–1968",
  stance="admiring — respect for the enemy commander, made official", tags=["letters", "military", "oceania", "verified"], body="""
The man who wrote the Anzac legend also, quietly, wrote the first English-language official
dignification of Mustafa Kemal. Ayhan Aktar's account (Honest History, drawn from his chapter in
Walsh & Varnava, *Australia and the Great War*, 2016) lays out the sequence:

- Bean visited the Gallipoli battlefield in 1919 — even before the Mitchell Committee — and spoke
  to the Ottoman officer **Major Zeki** of the 57th Regiment, who told him of Mustafa Kemal's role
  on 25–27 April 1915.
- The "Australian boosting of Mustafa Kemal proceeded from that point, commencing with the
  publication in **1921** of the first volume of the Official History," where Bean wrote of Kemal's
  **"swift determination"** and **"a formidable force under a formidable leader."** Bean "argued
  that Mustafa Kemal's actions had been vital to Ottoman success."
- Aktar's reading, following Jenny Macleod: this respect for the enemy and his commander "probably
  made the Anzac defeat more honourable" — to fail against "an admirable leader and admirable
  race is palatable." Bean, Churchill and Aspinall-Oglander together turned Kemal into "the Man of
  Destiny" on the Allied side; the myth "grew in the turbulent international relations of the early
  1930s."

Earlier still, Bean's *Anzac Book* (1916) had carried his own verse to the Turk — "In life, in
death, you've played the gentleman" — the root of the "noble Turk" discourse (Kent, cited in
Gnida/Baker via *Media International Australia*). That sets the ground the [[Johnnies and Mehmets]]
quote and the 1985 memorial later stood on: Australians had a respectful Kemal in print sixty
years before Anzac Parade.

*Boundary:* Bean's attitude to Atatürk as *president* (the *Gallipoli Mission* of 1948, which
records his return to the peninsula) is not yet read here — only the Official History line is
sourced. Intensity 2.

See [[Gallipoli Campaign]], [[Winston Churchill]], [[Johnnies and Mehmets]].

## Sources
- Ayhan Aktar, ["Rewriting the history of Gallipoli: a Turkish perspective," Honest History, 25 July 2017](https://honesthistory.net.au/wp/rewriting-the-history-of-gallipoli-a-turkish-perspective) (§ on Bean; citing Macleod, *Reconsidering Gallipoli*, Manchester UP 2004, p. 78)
- [Media International Australia article on the "noble Turk" discourse (SAGE)](https://journals.sagepub.com/doi/10.1177/1329878X1013700107) — Bean's *Anzac Book* verse (Kent 1985)
- [ATFMS, "Explore the history"](https://atfms.org.au/the-project/explore-the-history) — the Bean poem text
""")),
]

E = [
("Khilafat Disillusion, 1924", "1922–1926", """
The conflicted card the Indian column was missing: not one man's opinion but **the arc of a whole
movement's feeling**, from adulation to shock to grudging acceptance.

M. Naeem Qureshi's *Atatürk Araştırma Merkezi Dergisi* article gives the shape. From his rise,
Kemal "had attracted wide support from among the Muslims of British India" — an adulation that
grew out of pan-Islam and "basically his apparent defence of the caliphate." Even the separation
of sultanate and caliphate in **November 1922** "created no widespread stir." **The clash came
only in March 1924**, and "the reaction in India was instantaneous and sharp, but somehow the break
was soon repaired" — after the shock, "Indian public opinion, spearheaded by those who understood
the Turkish predicament, began to tilt again in favour of the nationalists."

Faridah Zaman (Brill chapter, accepted manuscript) adds the machinery of disillusion:

- **Lausanne (1923)**: celebrated in the streets of Delhi, but with "nervousness that the caliphate
  did not appear to be a part of the future imagined by Turkish nationalists." *Muslim Outlook*
  (Lahore), 23 Nov 1923 captures the mix.
- **The cautious optimists**: the 1922 shift to an elected-assembly caliphate had Ameer Ali and
  Muhammad Barkatullah "cautiously optimistic."
- **March 1924**: "for some the realization of their worst fears." The All-India Khilafat
  Conference of **May 1924** resolved to send another delegation — this time **to Ankara**, "to
  remove such misunderstandings" — and **the Government of India refused its members passports**
  (Sadiq, *The Turkish Revolution and the Indian Freedom Movement*, 1983).
- **The brothers**: Muhammad Ali Jauhar's and Shaukat Ali's movement, having sent a delegation to
  Europe in 1920, now turned its energy to the Cairo (1926) and Mecca (1926) congresses; Shaukat Ali
  wrote to the Shaykh al-Azhar that the khilafat's future belonged to "a world Muslim conference."
  Neither brother is sourced here with a first-person Atatürk statement — the card is the
  movement's, not theirs.
- **The reversal**: by 1930 [[Allama Iqbal]] was calling Turkey's abolition a radical act of
  *ijtihad* — "perfectly sound."

*Recorded gap:* the exact words of the Ali brothers on Kemal in 1924 (*Hamdard*, *Comrade*) have
not been read; the *Hamdard*–Tagore link is on the [[Rabindranath Tagore]] node.

Compare [[Abolition of the Caliphate]], [[Khilafat Movement]], [[Aga Khan III]], [[Mahatma Gandhi]].

## Sources
- M. Naeem Qureshi, ["Muslims of British India and the Kemalist Reform in Turkey: Iqbal, Jinnah and Atatürk, 1924–1938," *Atatürk Araştırma Merkezi Dergisi* XII (35), 1996, pp. 379–386](https://atamdergi.gov.tr/ozet/807/eng)
- Faridah Zaman, "The Khilafat Movement in Europe and the Reimagining of Authority in Islam," in Soumen Mukherjee (ed.), *Empire, Religion, and Identity* (Brill Indological Library) — [accepted manuscript, Oxford ORA](https://ora.ox.ac.uk/objects/uuid:bf4cf9f8-0d86-41d8-9213-752ace9be015/files/sr781wh913), §4 "From Caliphate to Congress"
"""),

("India Mourns, November 1938", "November 1938", """
India's funeral-fortnight card, from Toksoy's corpus and one Indian scholarly footnote.

Per Toksoy (drawing on Doğaner, *Atatürk Dergisi*, 2005): India was **"the country most affected
by Atatürk's death after Turkey itself."** The Indian press called him **"the Creator of
Independent Turkey, the Hero-Apostle of Asian Nationalism"** — "a pride of the whole East,"
"the greatest hero of the age" — and held that his reforms showed all Asian peoples the road to
progress and independence. **Shops were closed, legislative sittings suspended, and national
mourning proclaimed; mevlids were read in mosques and memorial days arranged.**

The Bengali counterpart: Ramkrishna Bhattacharya records that **classes and activities at
Santiniketan were suspended on 18 November 1938** — the day before Atatürk's coffin boarded the
*Yavuz* — [[Rabindranath Tagore]]'s school marking the death of "the great Pasha."

Set against [[Khilafat Disillusion, 1924]]: the same subcontinent that went cold in March 1924 was,
fourteen years on, mourning him as an *Asian* hero rather than a *caliphal* one — the mirror had
changed from Islam to Asia. Compare [[Palestine at the Radios, November 1938]], 
[[Tehran Falls Silent, November 1938]], [[Ta Kung Pao Mourns, November 1938]].

## Sources
- [Toksoy 2010](https://dergipark.org.tr/en/download/article-file/32009), §F "Hindistan Basını" (full text in `sources/`), citing Yasemin Doğaner, "Millet Liderini Uğurluyor," *Atatürk Dergisi* IV/4 (2005), pp. 49–50
- Ramkrishna Bhattacharya, ["The World Comes First," *Frontier* 51(45)](https://frontierweekly.com/articles/vol-51/51-45/51-45-Tagore%20and%20his%20Nationalism.html) (citing Bandyopadhyaya vol. 3:143)
"""),

("Malay Press and the Fall of the Caliphate", "1924–1930s", """
Malaya is the census's first **indifference** card: the place where the Caliphate's fall mattered
*less* than Istanbul or Delhi assumed. Sourced in three layers of Malaysian scholarship:

- An IIUM thesis on the Muslims of Malaya after 1924, built on British records, the Kuala Lumpur
  archives and contemporary newspapers, finds that "while some Muslims (mainly the Arabs and
  Indian Muslims) expressed their support for the Caliphate, most of them, particularly the
  **Malay-Muslims, showed little interest**" — a result of the tangled relations between the Malay
  Courts, the Malay-Muslims and the British. But the abolition "did not bring an end to the
  Muslims' interest in Turkey; it continued during Mustafa Kemal Atatürk's era."
- A study of the Kelantan religious-council magazine *Pengasuh* (JIMK 14(1), 2017) revisits how
  the 1924 caliphate question was argued in its pages — keyword **Mustafa Kemal**, the dissolver.
- A Shajarah (IIUM) article on Malaysian history textbooks summarises the received narrative: the
  dissolution "led educated Malays to take a negative stance towards Turkish nationalism"
  as contrary to Islamic law; **Abdul Kadir Adabi** is named as a Malay intellectual who
  denounced it; yet *Pengasoh*, *al-Ikhwan* and *Saudara* kept covering Turkey, and Malays
  "positively responded to some elements of Turkish nationalism." (Secondary-on-secondary; the
  claim is the textbook's.)

The shape: **Malay court + British control = muffled Caliphate sentiment; Kaum Muda reformist
press = sustained but divided interest in Turkey.** Compare the Dutch East Indies press, which
a Cambridge University Press book chapter (snippet read; title not extracted) says was "overall
unconcerned" with the Ottoman defeat and "supportive of Mustafa Kemal's actions" until a Surabaya
Caliphate Committee formed in October 1924 (see [[Sukarno]]).

*Recorded gap:* NLB NewspaperSG (the Straits Times / *Malaya Tribune* / *Warta Malaya* archive)
blocks automated fetch; the Nov 1938 Malayan press is a browser-queue item.

See [[Abolition of the Caliphate]], [[Khilafat Disillusion, 1924]].

## Sources
- ["The Impact of the Fall of the Ottoman Caliphate on the Muslims in Malaya" (IIUM student repository thesis)](https://studentrepo.iium.edu.my/entities/publication/105a300c-4170-4fb3-8e3f-ee8d249d497e/full) — abstract read via search; author/title page not extracted
- ["Majalah Pengasuh dan Persoalan Khalifah," *Jurnal Islam dan Masyarakat Kontemporari* 14(1), 2017](https://journal.unisza.edu.my/jimk/index.php/jimk/article/view/193) · [IREP IIUM companion abstract](https://irep.iium.edu.my/100436)
- ["The Consciousness of Türkiye in Malaysia: Ottoman History in Malaysian Secondary History Textbooks (1989–2022)," *Al-Shajarah*](https://journals.iium.edu.my/shajarah/index.php/shaj/article/view/1719)
"""),

("New Zealand Press, November 1938", "10–14 November 1938", """
**First contemporary Oceanian press card — and Papers Past is machine-readable.** A dated search
of the National Library of New Zealand archive returns ten articles with "Ataturk" in 11–12 November
1938 alone, from papers across the country: *Marlborough Express* ("One of Ataturk's Generals"),
*Evening Post* ("Ataturk's Successor"), *Hawke's Bay Herald-Tribune* ("Creator of Modern Turkey is
Dead"), *Waikato Times* ("Ruled by Character"), *Wairarapa Times-Age* ("President of Turkey"),
*Taranaki Daily News*, *Nelson Evening Mail*, *Manawatu Standard*, *Poverty Bay Herald*, *Auckland
Star* and others, with a pictorial follow-up on 14 December (not read).

The texts read so far:

- **Wire layer (11 Nov, Press Association).** Istanbul: "The majority of Turkish Parliamentarians
  have decided to support the former Premier, Ismet Inonu, as the successor to Kamal Ataturk, who
  died yesterday... The burial will take place in a magnificent mausoleum. Photographs draped in
  crepe have replaced the stock in the majority of shop windows here." (*Wairarapa Times-Age*.)
- **Feature layer (12 Nov, *Waikato Times*, p. 9).** The most colourful and **conflicted** NZ item:
  *"Ruled by Character — 'Roughneck Dictator'."* Atatürk is "a personification of dictatorship
  carried to its greatest extreme — yet more rational than other European dictators," "the blonde,
  blue-eyed combination of patriot and psychopath," a man who "has been described as the
  'roughneck of dictators'," "like Hitler... the son of a minor Customs official"; "no man has ever
  betrayed more masters than has Ataturk, but always from motives of his own honest views of
  patriotism." It credits the westernisation, the Chanak standoff and Lausanne, repeats that he
  "hanged all members of the opposition" after 1926, claims **"Ataturk hated Great Britain"**, and
  closes on the 1936 fortification of the Dardanelles.

Reception data, not biography: the piece mixes real events with period errors (the "Kamal"
spelling, the hated-Britain line) — which is exactly why it is a **Rorschach card**: a Dominion
that had sent the Anzacs to Gallipoli reads the man who beat them through the 1930s dictator
template, with a sneer and a bow in the same paragraph. See [[Gallipoli Campaign]], 
[[Chanak Crisis]], [[C.E.W. Bean]].

*Access note for the next researcher:* the Papers Past search page returns headlines only (links
stripped); article IDs surface via web-search snippets, and `paperspast.natlib.govt.nz/newspapers/<ID>`
fetches full OCR text. IDs read: `WT19381112.2.87`, `WAITA19381112.2.50`; headline-only: `NEM19381111.2.50`,
`TDN19381111.2.47`. Unread candidates: `MS19381112.2.28`, `MS19381112.2.100` ("Renaming Capital"),
`NA19381214.2.81`.

## Sources
- [Papers Past, Waikato Times 12 Nov 1938 p. 9, "Ruled by Character"](https://paperspast.natlib.govt.nz/newspapers/WT19381112.2.87) (P)
- [Papers Past, Wairarapa Times-Age 12 Nov 1938, "President of Turkey"](https://paperspast.natlib.govt.nz/newspapers/WAITA19381112.2.50) (P)
- [Papers Past dated search, "Ataturk," 11–12 Nov 1938](https://paperspast.natlib.govt.nz/newspapers?query=Ataturk&start_date=11-11-1938&end_date=12-11-1938) (P — result list of ten headlines, read 2026-10-28)
"""),

("South African Muslims and the Anatolian Cause, 1919–1923", "1919–1923", """
The Union of South Africa's contribution to the Atatürk record is **money, resolutions and a
refusal** — Africa's earliest documented material support for the Anatolian nationalists.

Serhat Orakçı's University of Johannesburg MA thesis (2007), built on the South African National
Archives (SAB GG series) and Turkish archival works (Uçar), gives three facts:

1. **The Muslim dilemma.** British subjects who could not openly side with the Ottomans in the
   Great War (one printer even renamed "the Ottoman Printing House" the "Union Printing House" in
   July 1914), they nonetheless held protest meetings in 1919: the Pretoria branch of the
   Transvaal Mohammedan Congress and Johannesburg's Hamidia Islamic Society both endorsed the
   All-India Muslim League's 19 March 1919 resolution that Istanbul and Palestine remain under
   Ottoman control.
2. **The money.** "Between 1919 and 1923, **£875 out of £130,250.00** foreign aid was sent to the
   Empire from the South African Muslims. All of these funds were used during the Turkish War of
   Liberation (1919–22) and for the construction of the new Turkish Republic in 1923." (Before
   that: £200 from Cape Town, £700 from the Transvaal and £650 from Durban to the Ottoman Red
   Crescent in the 1911–12 wars.)
3. **The Chanak refusal.** In September 1922, when Britain asked the Dominions for troops against
   Turkey's advance on the Straits, the Union of South Africa — Smuts unwilling to risk a repeat of
   the 1914 Rebellion — **declined to send a contingent**, "the first instance in which the Prime
   Minister of South Africa made a decision on foreign relations diametrically opposed to the
   wishes of the Imperial Government" (Wheeler, cited by Orakçı); as a Lausanne signatory it later
   became a guarantor of Turkey's borders. See [[Chanak Crisis]], [[Treaty of Lausanne]].

Polarity: **instrumental-admiring** — South Africa's Muslims gave to the cause of Ankara in the
vocabulary of the Caliphate, not of Kemalism; the card sits next to [[Khilafat Disillusion, 1924]].
No 1938 South African press yet read. *Lead (single-source, unverified):* a second UJ thesis
says Turkish archives record 17,634 lira and £875 from South African Muslims received by Mustafa
Kemal personally — not checked against Orakçı's figure.

## Sources
- Serhat Orakçı, *A Historical Analysis of the Emerging Links between the Ottoman Empire and South Africa between 1861–1923*, MA, University of Johannesburg, Oct 2007, §4.3–5.4 — [Wayback copy](https://web.archive.org/web/20110831201139/http:/ujdigispace.uj.ac.za:8080/dspace/bitstream/10210/3241/1/Orakci.pdf) (citing SAB GG Vols. 686 and 1024; Uçar pp. 331–335; Wheeler p. 6)
"""),

("Japanese Print Culture on Kemal Pasha, 1922–1939", "1922–1939", """
Japan already holds [[Ōkawa Shūmei]] and a Takamatsu visit; this card widens the lens to the
whole **printed conversation** — and it is enormous.

Shimizu's bibliography (Chiba University, 2013) combs the Japanese holdings of 1910–1939 and finds
**876 magazine articles and 936 books** touching Turkey. Items with Kemal (ケマル / ケマール) in the
title run to dozens, from the war years to the death. The shape of the list is itself a mirror
reading:

- **1922–23: the victory read as Pan-Asian.** Gaikō Jihō: "Kemal Pasha's war victory and
  Pan-Islamism" (1922); Kaizō: "Kemal Pasha" (1922); Ōkawa's *Problems of Resurgent Asia*
  includes "Fifty years of the Young Turk Party" (1922).
- **1927–28: an audience record.** Two magazine pieces (bio of Yamamoto Eisuke not checked) under his
  name carry "Record of a meeting with Kemal Pasha" and "The brave man of new Turkey" (*Kaizō* 1927;
  *Kaigai* 1928); the same year *Daichōwa* printed "Kemal Pasha, Gandhi and Chiang Kai-shek" — the
  three-leader template that Chinese papers later reuse (see [[Ta Kung Pao Mourns, November 1938]]).
- **1931–1936: the dictator register.** "Kemal Pasha, hero" in *Sen'yū* (veterans' magazine, 1931);
  "Kemal Pasha and the fez" (1931); Naitō Tomohide's "Kemal and Mussolini" (1930), "A fascist beyond
  the fascists" (*Sekai Chishiki* 1932) and "Behind the great man's private life" (1935); a 1935
  Kōdansha anthology of the world's great orators gives him the chapter "A hot-blooded man of love,
  sword and speech"; and a 1936 *Akatsuki* piece titled "Dictator Kemal Pasha."
- **1933: the Indian exile's reading.** Rash Behari Bose — the Indian nationalist exiled in
  Japan — wrote "Kemal Pasha and the New Turkey" in *Daiajia* (Greater Asia), and co-authored with
  Nakatani Takeyo *Revolutionary Asia: A Survey* (1930) with a chapter on "the guiding principle
  of revolutionary Turkey and Mustafa Kemal."
- **1938–39: the death.** *Dai Ajia Shugi* No. 68 runs "The Late President Kemal" (credited, in
  Japanese transliteration, to "Hüsrev Gerede") beside Kanda Masatane's "Impressions of President
  Kemal"; *Kaikyōken* (the Islamic-world research institute's journal) runs Nohara Shirō's
  "Biography of Kemal Atatürk" and a 1939 chronology plus a translation of his Nov 1937 speech; the
  Foreign Ministry's research department publishes "The life of the late President Kemal" (*Kaikyō
  Jijō*, 1939); and **Ōkawa Shūmei closes the sequence in *Shin-Ajia* (New Asia) vol. 1 no. 2, 1939 (month not
  given) — "Kemal Pasha, builder of the new Turkey."** (Corrected 2026-10-29: an earlier version put
  this in *Kōron*, December 1939; Shimizu's bibliography lists it under *Shin-Ajia* 1(2), published by
  the South Manchuria Railway's East Asia Economic Research Bureau. Titles only; the article itself is unread.)

A reading, labelled as such: the **vocabulary shifts three times** — victory (Pan-Asian, 1922),
dictator-peer (fascist comparisons, 1930–36), and Islamic-world intelligence (the 1938–39 journals
on the Islamic world, including a Foreign Ministry piece). The same man, three registers, in one language.

*Boundary:* the bibliography lists titles, not contents; no article has been read. The claim is
that these were *printed*, not what they said.

## Sources
- Shimizu Ken (清水 建, as extracted), "解題 日本におけるトルコ関係文献（1910〜1939）" and the bibliography tables, Chiba University, 2013, no. 232, pp. 113–132 — [PDF](https://opac.ll.chiba-u.jp/da/curator/900116900/2013no.232_113_132.pdf) (S)
"""),
]

for name, kw in P:
    person(name, **kw)
for n, when, b in E:
    note("Events", n, {"type": "event", "when": when, "tags": ["event", "verified", "obituary-corpus"]}, b)

print(f"census r3 asia_africa: {len(P)} people, {len(E)} events")
