# -*- coding: utf-8 -*-
# Census round 7 (Oct 2026) — contemporary (1919-1938) Asian voices on Kemal (slug: asia_contemp).
# Routes, all free and scriptable: Internet Archive full texts (Indian Digital Library scans: Modern Review, Collected Works
# of Mahatma Gandhi vol. 23, Mohamed Ali's Cocanada address; Sukarno's Dibawah Bendera Revolusi vol. 1), Chinese Wikisource
# (Sun Yat-sen), and KB/Delpher article OCR (Dutch East Indies dailies). Quotations are checked against the OCR text with
# whitespace and line-break hyphens ignored; nothing else is normalised. OCR page numbers are marked "c." where read from running heads.
from _lib import note, person

# ---------------------------------------------------------------- people
person("Sun Yat-sen", role="Founder of the Kuomintang; first provisional president of the Republic of China", nat="Chinese", life="1866–1925",
  stance="admiring of Turkey as an Asian precedent, but never of Kemal by name in these texts; credits Russia for the rescue in one lecture",
  tags=["politician", "china", "contemporary", "verified"], body="""
Two 1924 texts, both printed on Chinese Wikisource, show how the leader of the other end of Asia read the Turkish revival
in the last year of his life. **Neither names Kemal**; both name *Turkey* (土耳其), and the note stays on that line.

**Nationalism, lecture 1 (27 January 1924, Canton).** Sun is arguing that the oppressed will gravitate to Russia. Turkey,
he says, was the "sick man" before the war, joined Germany, was beaten by the Entente and was nearly partitioned: *"後來俄國出來打不平，助他趕走希臘人，修改一切不平等的條約"*
("later Russia came out to even things up, helped it drive off the Greeks and revise all the unequal treaties"). The next
sentences credit "all" of that to Russian help: *"這是靠什麼力量呢？是全靠俄國人的幫助"*. This is the deflating reading: Turkish
recovery as a Soviet success story, used instrumentally.

**"Greater Asianism" (Kobe, 28 November 1924).** Speaking to a Japanese audience, Sun lists Persia, Afghanistan, Arabia and Turkey
among the states that had been Europe's colonies in the age of Japan's treaty revision, then says of Turkey that after the war
it "drove the Europeans out" and "is now a completely independent country", and gives the line he is remembered for:
*"現在亞洲只有兩個頂大的獨立國家；東邊是日本，西邊是土耳其。日本和土耳其，就是亞洲東西兩個大屏障"* (Asia now has two great independent states, Japan in the east and Turkey in the
west, "the two great barricades of Asia"). The same speech holds up "benevolence and righteousness" as the basis of a Pan-Asian league,
so the praise is also an appeal to Tokyo.

**Reading.** An admiring-but-anonymous gaze: Sun sees a *state* and a *position* (the western barricade), not a man. That the man
is missing is itself data; compare [[Chiang Kai-shek]] and [[Ta Kung Pao Mourns, November 1938]], where the Chinese side later gave the barricade a face.

**Caveats.** The texts are Wikisource transcriptions of the Chinese originals; the page does not name the edition. The
Kobe speech is a translation-free primary text but a performance for a Japanese host.

## Sources
- Sun Yat-sen, 三民主義·民族主義第一講 (27 Jan 1924), Chinese Wikisource: [zh.wikisource.org/wiki/三民主義/民族主義第一講](https://zh.wikisource.org/wiki/%E4%B8%89%E6%B0%91%E4%B8%BB%E7%BE%A9/%E6%B0%91%E6%97%8F%E4%B8%BB%E7%BE%A9%E7%AC%AC%E4%B8%80%E8%AC%9B) · tier P (transcription)
- Sun Yat-sen, 大亞洲主義 (28 Nov 1924, Kobe), Chinese Wikisource: [zh.wikisource.org/wiki/大亞洲主義](https://zh.wikisource.org/wiki/%E5%A4%A7%E4%BA%9E%E6%B4%B2%E4%B8%BB%E7%BE%A9) · tier P (transcription)
""")

person("Mohamed Ali Jauhar", role="Khilafat leader; editor of the *Comrade* and *Hamdard*; president of the Indian National Congress, 1923", nat="Indian (British India)", life="1878–1931",
  stance="admiring of Kemal's war, bitter once the Caliphate fell (the bitterness itself is not yet sourced here)",
  tags=["politician", "india", "khilafat", "contemporary", "verified"], body="""
The Khilafat movement's most famous orator, in the last quarter of 1923, on the eve of the break.

**Cocanada, December 1923** (session from 26 December). As president of the thirty-eighth session of the Indian National Congress he lays out
the Allied record against the Khilafat and says of Lausanne: *"it was Great Britain herself that was the chief obstacle in the path of Ghazi Mustafa Kemal Pasha to the very end of this tragic tale"*
(Afzal Iqbal's *Select Writings and Speeches of Maulana Mohamed Ali*, vol. 2, p. 133; separate print of the address, p. 86).
Kemal is the victim of British hostility, the Greeks "her own brutal nominee and agent". The speech defends the Khilafat as an institution and
never doubts that Ankara is its protector; it was delivered three months before the Assembly abolished it. See [[Abolition of the Caliphate]] and the arc in [[Khilafat Disillusion, 1924]].

**What is not here.** The *"Khilafatists' 1924 bitterness in their own words"* is, for Mohamed Ali, **not in the open scans I could read**:
I found no passage on the abolition itself in the two-volume *Select Writings* (1969), and *My Life: A Fragment* gave no OCR hit for Kemal. The
institutional voice of that bitterness is the cable of Shaukat Ali and Mufti Kifayatullah in [[Gaya to Angora — Indian Voices on Kemal, 1922–1924]].

## Sources
- Mohamed Ali, Presidential Address, Indian National Congress, Cocanada, Dec 1923 — in *Select Writings and Speeches of Maulana Mohamed Ali*, ed. Afzal Iqbal, vol. 2 (Lahore, 1969), p. 133 (page from running heads): [archive.org/details/selectedwritings02afza](https://archive.org/details/selectedwritings02afza) (`_djvu.txt`) · tier P
- Separate printing, *Presidential Address of Maulana Mohamed Ali … Thirty Eighth Annual Session of the Indian National Congress held at Cocanada*, p. 86: [archive.org/details/dli.ministry.18951](https://archive.org/details/dli.ministry.18951) · tier P
""")

# ---------------------------------------------------------------- events
E = []

E.append(("Gaya to Angora — Indian Voices on Kemal, 1922–1924", "1922–1924", """
The Khilafat arc in the voices that lived it, from the pre-break high to the cable of March 1924. [[Khilafat Disillusion, 1924]] gives the
shape from scholars; this card gives the **documents**, read in the Calcutta *Modern Review*'s printed summaries of the Congress sessions and
its April 1924 Notes (Internet Archive scans, Indian Digital Library; page numbers are read from OCR running heads and marked "c.").

**December 1922, Gaya: the high.** The Indian National Congress, moved by Sarojini Naidu, resolved: *"This Congress congratulates Ghazi Kemal Pasha and the Turkish nation on their recent successes"* and pledged India to the struggle for Turkey's "free and independent status", with the Arabian peninsula "freed from all non-Muslim control" (Modern Review, Jan 1923, c. pp. 129–130). It was carried "by a large majority" after an amendment substituting "foreign control" was defeated. The same week the **Jamiat-ul-Ulema** went further:
it "congratulated Mustapha Kemal and the Kemalists on their victories" and decided to give him, as "The Great Crusader", *"the title of Mujadid-i-Khilafat ( Saviour of the Khilafat )"* for giving the Khilafat "re-birth" (c. pp. 182–183). **Dr M. A. Ansari**, presiding over the Khilafat Conference weeks after the Sultanate fell ([[Abolition of the Sultanate]]), said he disbelieved the reports of a split between Sultanate and Khilafat, was *"sure that the Kemalists would obey the religious injunctions"*, and that if the Turks erred the Mussalmans would seek correction by representation (c. p. 182). The praise is already conditional on the Khilafat.

**December 1923: Mohamed Ali** at Cocanada makes Britain the "chief obstacle" in Kemal's path (see [[Mohamed Ali Jauhar]]).

**March 1924: the cable.** After the Assembly's law of 3 March, Angora sent the Central Khilafat Committee a telegram, signed "Ghazi Mustafa Kemal" in the Modern Review's print, giving its reasons: the Khilafat office "being essentially contained in the sense and meaning of Government and Republic" was abolished, and a separate office "proved to be disturbing". Shaukat Ali (president, Central Khilafat Committee) and Mufti Kifayatullah (president, Jamiat-ul-Ulema) answered
"as resolved in a special joint meeting" of both bodies, addressing "Your Highness": *"The news so far received from Turkey regarding the abolition of the Khilafat has caused deep distress and consternation among your Indian Muslim brethren."* They disclaim any wish to keep the Khilafat "as a monopoly of any particular family"; they say Indian Muslims had expected Kemal to "revive Islam's fundamental institution, the Khilafat, purging it of such excrescences"; and that "the entire abolition … destroys all our expectations". They ask the Assembly to "reconsider" and to receive a delegation (Modern Review, April 1924, Notes, c. pp. 507–509). The tone is the whole story: courtesy, grievance, and an appeal from the Assembly to the man.

**Gandhi, 21 March 1924.** Interviewed at Poona by a *Liverpool Post*/*Mercury* correspondent: "I asked Gandhi concerning Kemal Pasha's deposition of the Khalif. Gandhi replied that it did not affect Hindu-Muslim unity which, however, he confessed was not so strong as formerly" (*The Hindu*, 14 Apr 1924; *Collected Works* vol. 23, p. 295). The sentence is the interviewer's paraphrase, and it is the only place the volume names Kemal (text and index); Gandhi's letter of 5 March to Mahomed Ali (no. 127) speaks of "the Khilafat resolution in the Turkish Assembly" and says "the future of Islam rests in the hands of the Mussulmans of India" without naming him. Gandhi's view of Kemal is, in the sources open to me, **a view of Hindu-Muslim unity**; compare [[Mahatma Gandhi]].

**What is missing.** Mohamed Ali's and Shaukat Ali's own spoken bitterness after March 1924 is not in the open scans I searched (I found no mid-1924 speech on it in the *Select Writings*); the cable is the strongest documentary substitute.

## Sources
- *The Modern Review* (Calcutta, ed. Ramananda Chatterjee), Jan 1923 (Congress, Khilafat Conference and Jamiat proceedings) — [archive.org/details/dli.calcutta.09830](https://archive.org/details/dli.calcutta.09830) · April 1924 Notes, cable text — [archive.org/details/dli.calcutta.09831](https://archive.org/details/dli.calcutta.09831) (the catalogue label says Jul–Dec 1923; the scan contains the 1924 issues) and a second scan [archive.org/details/in.ernet.dli.2015.144814](https://archive.org/details/in.ernet.dli.2015.144814) · tier P
- *The Collected Works of Mahatma Gandhi*, vol. XXIII (March 1922–May 1924), Ahmedabad 1967: "Interview to *Liverpool Post* and *Mercury*", pp. 293–295; letter to Mahomed Ali, 5 Mar 1924 — [archive.org/details/in.ernet.dli.2015.162047](https://archive.org/details/in.ernet.dli.2015.162047) · tier P
"""))

E.append(("The Modern Review on Kemal, 1923–1924", "1923–1924", """
A Bengali Hindu monthly, edited in Calcutta by Ramananda Chatterjee (the Notes are unsigned; they are attributed here to the editor by role), watched Kemal for two years and its
verdicts are among the more interesting non-Muslim Indian readings: **sympathy for Turkey's independence, scepticism toward the Khilafat, and
a use of Kemal as an argument in Indian quarrels.** Page numbers are read from OCR running heads ("c."). Four editorial records:

- **March 1923 (c. pp. 396–397): the aeroplane fund.** Noting Indian papers' indignation at British bombing of Waziristan villages, the Notes say they have not seen similar comments on *"the Fund that is being raised by the Musalmans in India to buy and present Mustapha Kemal Pasha with an aeroplane"*: an aeroplane given to Angora "must kill innocent persons, too, including women and children", so silence would be indirect support. A moral objection to the *instrument*, not to the man; the next paragraph complains that Muslims who give lakhs to the Turks never relieve Muslim flood victims in Bengal.
- **April 1924 (c. pp. 508–510): the abolition.** After printing the Central Khilafat Committee's cable ([[Gaya to Angora — Indian Voices on Kemal, 1922–1924]]) the Notes work through the Turkish case: Turkey "is rightly entitled to refuse to maintain the office within her territories"; "Ghazi Kemal Pasha and his followers are entirely against the secular aspect of Pan-Islamism … He is a thorough-going nationalist of the Western type."
  A "non-Muslim" suggests Muslims elect a spiritual head as Catholics elect a Pope. Understanding without enthusiasm.
- **July 1924 (c. pp. 115–116): the test case.** Rebuking a Bengal conference's praise of the assassin Gopinath Saha, whose mover had taunted "where was non-violence when the Congress congratulated Kemal Pasha on his victories?", the Notes defend the Gaya resolution: *"Mustapha Kemal Pasha fought to make and keep his country free"* and "Hence he was right in fighting"; the assassin's case is different. Kemal is cited as the *legitimate* use of force.
- **October 1924 (c. pp. 471–472): the snub.** Arguing that Indian Muslims should not over-identify with foreign Muslims, the Notes ask *"Did the Turks of Angora treat the telegrams and letters of the Central Khilafat Committee of India with due consideration?"* and claim Kemal never acknowledged the long telegram, and held that Indians "have not made sacrifices" for the Turks. The Notes also add that the independent Muslim states "have fought against one another as frequently and bitterly as Christian countries". Kemal's silence is used as evidence in a Hindu-Muslim argument.

**A fifth voice in the same pages.** The economist **Benoy Kumar Sarkar**, in the April 1923 issue ("The Economics of the Rhineland", section "The New Germany and Kemal Pasha"), says that "from Manila to Morocco" the whole East "has been spiritualized by the Turkish successes under Kemal Pasha", and that the example reached Young Germany as well. (The OCR of the standfirst is noisy and no quote is printed.) The Modern Review of Jan–Jun 1925 also remarks, in an article on China whose author I did not identify, that "only in one quarter has Kemal Pasha, luckily for Asia, succeeded" in raising Asia's reputation while no "Kemal Pashas" are forthcoming in China — not recorded as a gaze here.

**Why it matters.** Between them these notes give a non-Muslim Indian public sphere's Kemal: war hero (July 1924), nationalist who dismissed the Khilafat (April 1924), and a symbol Muslims were spending money on (March 1923). Compare the Muslim voices in [[Khilafat Disillusion, 1924]]; and the Indian viewpoint of [[Rabindranath Tagore]] and [[Jawaharlal Nehru]].

## Sources
- *The Modern Review* vol. XXXIII (Jan–Jun 1923): Notes, March 1923; Sarkar, April 1923 — [archive.org/details/dli.calcutta.09830](https://archive.org/details/dli.calcutta.09830) · tier P
- *The Modern Review*, April 1924 — [archive.org/details/dli.calcutta.09831](https://archive.org/details/dli.calcutta.09831); July and October 1924 (vol. XXXVI) — [archive.org/details/dli.calcutta.09832](https://archive.org/details/dli.calcutta.09832) · tier P
"""))

E.append(("Sarekat Islam and the Cheribon Telegram, 1922–1923", "1922–1923", """
Before the Malay and Dutch press of 1924 ([[Malay Press and the Fall of the Caliphate]], [[Dutch Confessional Press and the Fall of the Caliphate, March 1924]]) there was the
**other side of the arc**: the Netherlands Indies Muslims at their most pro-Kemal, read in colonial Dutch dailies on Delpher (KB article OCR; tier P).

**The Cheribon telegram, October–November 1922.** After the Greek rout, the Al-Islam Congress at Cheribon, led by Tjokroaminoto, resolved to send Kemal congratulations. The Bataviaasch Nieuwsblad's Preanger editor, a year later, summed it up: "allerwege juichte men over de door Moestafa Kemal behaalde overwinning. Op het Al-Islamcongres dat in October 1922 te Cheribon werd gehouden, werd dan ook besloten aan Moestafa Kemal telegrafisch gelukwenschen te zenden; Arabieren betaalden de kosten van het telegram" (28 Nov 1923, "Indië en Angora", art. 87). The Sumatra-Bode of 27 Nov 1922 reports **Tjokroaminoto's circular** (in *Oetoesan Hindia*) about "het beruchte telegram aan Kemal Pasha": a committee member had taken an uncorrected draft to the post office "zonder mede weten van de leiding", containing two words, *ennemi décimé*, that offended Dutch neutrality toward Greece; Tjokroaminoto wanted the congressists to know that *"hij zelf noch de leiding van het congres, iets te maken heeft met de gevolgen"*. The paper's editor, signing "J. B.", comforts him: no such telegram would be forwarded "zoolang Angora niet officieel door onze Regeering erkend is". The telegram, in other words, was a **demonstration** that colonial control turned into a legal incident.

**The Sarekat Islam congress at Madiun, February 1923.** The congress opened on Saturday 17 February with some 1,500 present. The Nieuwe Rotterdamsche Courant's special correspondent (22 Mar 1923): *Hadji Salim* gave the report on the Cheribon congress and "verheerlijkte Moestafa Kemal Pasha en drong aan op erkenning van het Kalifaat". Het Nieuws van den Dag (24 Feb 1923) has the resolution: *"Moestafa Kemal Pasha werd verheerlijkt en hierbij werd tevens aangedrongen op erkenning van het Kalifaat als hoofd van den Mohammedaanschen godsdienst."* That is the knot of 1923: glorify the victor, defend the Caliphate he was about to abolish. The correspondent also notes that the school pupils sang the Internationale and the mood was "geprononceerd Islamietisch" against communism.

**The 1924 afterlife.** In May–June 1924, a communist speaker at a Sarekat Islam meeting in Bandung taunted Tjokro and Salim for saying "met geen woord" about the Caliphate question (Bataviaasch Nieuwsblad 26 May 1924; NRC 24 Jun 1924) — the reaction on the left to the leaders' silence, with no word on Kemal. The Preanger-bode (13 Aug 1924) reports a Sarekat Islam meeting's plan to send a delegate to the **Caliphate congress in Cairo** ("dit zal de heer Salim moeten zijn, indien er geld is").

**Boundary.** These are Dutch newspapers reporting Indonesian speakers; none gives a Sarekat Islam text in Malay. The 'Oetoesan Hindia' circular and the Malay-language press are the next step (Perpusnas/KITLV, not in Delpher).

## Sources
- Bataviaasch Nieuwsblad, 28 Nov 1923, "Indië en Angora" (Slot): [resolver.kb.nl/resolve?urn=ddd:011040484:mpeg21:a0087:ocr](https://resolver.kb.nl/resolve?urn=ddd:011040484:mpeg21:a0087:ocr) · tier P
- Sumatra-Bode, 27 Nov 1922, "Verschoningscirculaire": [resolver.kb.nl/resolve?urn=MMKB19:002117124:mpeg21:a00001:ocr](https://resolver.kb.nl/resolve?urn=MMKB19:002117124:mpeg21:a00001:ocr) · tier P
- Nieuwe Rotterdamsche Courant, 22 Mar 1923, "S.I.congres": [resolver.kb.nl/resolve?urn=ddd:010026490:mpeg21:a0122:ocr](https://resolver.kb.nl/resolve?urn=ddd:010026490:mpeg21:a0122:ocr) · Het Nieuws van den Dag voor Nederlandsch-Indië, 24 Feb 1923: [resolver.kb.nl/resolve?urn=ddd:010219529:mpeg21:a0171:ocr](https://resolver.kb.nl/resolve?urn=ddd:010219529:mpeg21:a0171:ocr) · tier P
- Bataviaasch Nieuwsblad, 26 May 1924: [resolver.kb.nl/resolve?urn=ddd:011040634:mpeg21:a0006:ocr](https://resolver.kb.nl/resolve?urn=ddd:011040634:mpeg21:a0006:ocr) · De Preanger-bode, 13 Aug 1924: [resolver.kb.nl/resolve?urn=MMKB08:000141370:mpeg21:a0002:ocr](https://resolver.kb.nl/resolve?urn=MMKB08:000141370:mpeg21:a0002:ocr) · tier P
"""))

E.append(("Sukarno Reads Kemal, 1928–1940", "1928–1940", """
A deeper, primary-text note on a voice that [[Sukarno]] covers only second-hand: **what Sukarno actually wrote about Kemal**, from *Dibawah Bendera
Revolusi* vol. 1 (Internet Archive scan; essay titles, dates as the volume prints them; the scan's printed page numbers are unreadable, so each is located by Archive.org leaf, "n").

1. **"Indonesianisme dan Pan-Asiatisme" (July 1928, leaf n88).** On the Indonesian celebration of the Chinese nationalists' victory he writes that the 1905 victory of Japan was felt by Asia as a victory over Europe *"sebagaimana kemenangan Mustafa Kemal Pasha dipadang peperangan Afiun Karahisar oleh seluruh dunia Asia dirasakan pula sebagai suatu kemenangan Timur di atas Barat"*. Kemal is the second Asian victory in the series; the list is Pan-Asian propaganda.
2. **"Kongres Kaum Ibu" (Dec 1928, leaf n124).** For the women's congress at Yogyakarta: *"Tidakkah Mustapha Kemal Pasha juga berkata, bahwa kita punya kemerdekaan, kebangsaan, kekuasaan …"* depends on how well women are educated. An authority cited, unsourced.
3. **Letter 8 from Ende to A. Hassan (22 Feb 1936, leaf n375).** Islam must fight orthodoxy to catch up with a thousand years: this is what Kemal meant, he writes, when he said *"Islam tidak menyuruh orang duduk termenung sehari-hari di dalam mesjid memutarkan tashbih, tetapi Islam ialah perjoangan"*.
4. **Letter 9 (22 Apr 1936, leaf n378).** Backwardness explains why so many Muslims cannot understand *"sahnya beberapa aturan-aturan-baru yang diadakan oleh Kemal Ataturk atau Riza Khan Pahlawi atau Jozef Stalin"*. Kemal in a list with Stalin, without comment on the means.
5. **"Apa sebab Turki memisah agama dari negara?" (Panji Islam, 1940, leaf n484).** The long essay on the Ottoman "caesaro-papism" ends with the arrival of *"tokoh raksasa Mustafa Kemal Pasya"* who "separated religion from state"; Sukarno says he only *reports* Turkey's reasons, and when the paper *Adil* objects that Kemal was "not an ulama", he replies: "Kemal Ataturk bukan 'ulama Islam'" — granted — but asks whether only ulama may build a state. The 1940 essay is posthumous by the dataset's cut (after November 1938), but it is the fullest text and the Kemal–Sukarno link that later accounts cite.

**Reading.** Across twelve years the register moves from *Asian victory* (1928) to *secular argument for Indonesian Muslims* (1936–40), exactly the thread the Sukarno card describes in a sentence. The earlier texts are the more informative on the contemporary gaze: before Pancasila, Kemal is a flag in the Pan-Asian parade. **Caveats.** The saying in (2) and (3) is not sourced by Sukarno; the edition behind the Archive.org volume is not stated on the scan, so spelling may be modernised; the month for (1) is inferred from the *Keng Po* date of 9 July.

## Sources
- Sukarno, *Dibawah Bendera Revolusi*, vol. 1 (Jakarta, [Panitya Dibawah Bendera Revolusi]), full text on Internet Archive: [archive.org/details/soekarno-dibawah-bendera-revolusi-1](https://archive.org/details/soekarno-dibawah-bendera-revolusi-1) (`_djvu.txt`/`_djvu.xml`; leaf numbers from the djvu pages) · tier P
"""))

for name, when, body in E:
    note("Events", name, {"type": "event", "when": when, "tags": ["event", "verified", "contemporary"]}, body)
print(len(E), "event notes and 2 person notes written")
