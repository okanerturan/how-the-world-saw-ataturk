# -*- coding: utf-8 -*-
# Census round 5 (Oct 2026) — the hostile and conflicted hunt.
# Seams: Olson (Oriente Moderno 1989) + van Bruinessen (Dersim) for Kurdish voices; Ter-Matevosyan (Turkish Studies 2015, 2025)
# for Armenian and Soviet/Comintern readings; Tezak thesis (Vanderbilt) + Watenpaugh for Arsuzi; Vahide's Nursi biography
# (iikv.org) for Ankara 1923; Toynbee 1922 full text (archive.org) for the Western Question; Wagemakers + Arabic quoters for al-Banna.
from _lib import note, person

P = [
("Nuri Dersimi", dict(role="Koçgiri/Dersim Kurdish nationalist, Xoybûn member, memoirist of Dersim", nat="Kurdish (Dersim)", life="Dersim-born; memoir published 1952",
  stance="hostile chronicler — the Kurdish memoirist of Dersim 1937–38", tags=["antagonist", "kurdish", "memoirist", "verified"], body="""
The Kurdish pen behind most of what the world knows from the *Kurdish* side of the Dersim
campaign. His memoir *Kürdistan tarihinde Dersim* (Aleppo, 1952) is the source Martin van
Bruinessen relies on first in his survey of the [[Dersim Rebellion]], with two cautions that
belong on the card: Dersimi had left the region before the main operations began, so **he was
not an eyewitness** of the massacres; and he wanted to show Dersim as more nationalist than it
was. Van Bruinessen finds the account "on the whole reliable", and says its main lines are
"to a large extent confirmed" by the official military history of the campaign — except the
poison-gas claim, which he says cannot be substantiated.

**What he saw.** Of the army's 1938 offensive he writes, in van Bruinessen's translation:
*"Thousands of these women and children perished ... because the army bricked up the entrances
of the caves."* He also tells how the army offered a cease-fire in the winter of 1937 and used it
to lure [[Seyid Riza]] to Erzincan, where Riza and ten others were tried in haste and executed
before President Atatürk's visit — haste van Bruinessen attributes to the officials' wish not to
let the local people petition the president for mercy (the later foreign minister İhsan Sabri
Çağlayangil narrates the trial "with apparent feelings of shame" in his memoirs).

**What this card does not say.** No sentence of Dersimi's about Atatürk *as a person* is in the
sources read, so the "hostile" tag is the vault's inference from the memoir's content, not his stated view of Atatürk; his gaze falls on the state and its army in the president's last two years. His
earlier meeting with Kemal's movement is on the card [[Koçgiri Leaders Write to Ankara, 1920]],
where Olson cites his memoir as the source of the Koçgiri telegram of November 1920. A claim
that Mustafa Kemal offered him a parliamentary candidacy in 1919, which he refused, appears
only on Wikipedia and is not promoted here.

## Sources
- [van Bruinessen, "The Dersim rebellion" (survey, Univ. Utrecht; archived PDF)](https://web.archive.org/web/20130521155242/http:/www.let.uu.nl/~Martin.vanBruinessen/personal/publications/Dersim_rebellion.pdf) — notes 10–18 · S
- [Olson, "The Koçgiri Kurdish Rebellion in 1921 and the Draft Law for a Proposed Autonomy of Kurdistan", *Oriente Moderno* 69 (1989)](https://doi.org/10.1163/22138617-0690106006) · S
""")),

("Zaki al-Arsuzi", dict(role="Arab nationalist philosopher and teacher of Antioch; League of National Action; forerunner of Ba'thism", nat="Syrian (Alexandretta/Antioch)", life="1899–1968",
  stance="hostile to the Kemalist claim on the Sanjak — an oblique card with no sentence on Atatürk", tags=["antagonist", "arab", "hatay", "verified"], body="""
The Sanjak of Alexandretta (Hatay) fight of 1936–39 is where Arab nationalism met Kemalist
Turkey head-on, and Arsuzi was its Arab schoolmaster. Raised in Antioch from 1904, he
studied at the Institut Laïc in Beirut and at the Sorbonne, joined the League of National Action
in 1933 and returned to the Sanjak as its representative in 1934, teaching at a high school
where, he wrote of his pupils, there were "no longer Muslims and Christians in the class" but
Arabs. In Tezak's phrase he was "one of Turkey's fiercest opponents": the League wanted to
overthrow French rule *and* to resist Turkish control, and kept its distance from the National
Bloc for the same reason. In June 1938 Alawite women demonstrated outside the Antioch prison
for his release (U.S. consular telegram, 1 July 1938, as Tezak cites it; ⚠️ that he was jailed by then is
inferred from the protest, not stated in the passages checked). Watenpaugh's 1996 article, as Tezak summarises it, links the Sanjak crisis and Arsuzi to
the emergence of the Ba'thist movement.

**The gaze, stated honestly.** Nothing the read sources print is a sentence by Arsuzi about
Mustafa Kemal. What is on the record is the identity line he drew against the Kemalist
program — in the Complete Works (vol. 3, 1975, pp. 291–92, as cited by Watenpaugh and Tezak):
*"I was before that an Arab, I felt that I had been born into an Arab family, I felt that I was
different from my neighbors, the Turks, in taste and way of life."* — and his opposition to
the Turkish claim on the Sanjak that Ankara pressed from 1936 and that was settled in Turkey's favour
in 1938–39 (the legal background is the 1921 Ankara Agreement, confirmed at [[Treaty of Lausanne]]
per an Arabic press summary, not checked against the treaty). Most of his writing on the crisis dates from the
1940s–50s, so every quotation is a retrospective view. Tezak's thesis is an undergraduate
honors thesis; the Watenpaugh article (*IJMES* 28:3, 1996) is the scholarly anchor, read here
only as abstract.

Cross-read: the Syrian Social Nationalist view of the same fight, [[Antoun Saadeh]].

## Sources
- [Tezak, honors thesis on the Sanjak of Alexandretta (Vanderbilt)](https://ir.vanderbilt.edu/bitstreams/c5ca1883-ed5d-4c24-ba79-de72568df165/download) — chapter on "The Arab Nation", fn. 106, 136–150, 310–313 · S− (undergraduate thesis)
- [Watenpaugh, "'Creating Phantoms': Zaki al-Arsuzi, the Alexandretta Crisis, and the Formation of Modern Arab Nationalism in Syria", *IJMES* 28:3 (1996)](https://academia.edu/3069658/_Creating_Phantoms_Zaki_al_Arsuzi_the_Alexandretta_Crisis_and_the_Formation_of_Modern_Arab_Nationalism_in_Syria) (abstract only) · S
""")),

("Hassan al-Banna", dict(role="Founder and Supreme Guide of the Society of the Muslim Brothers (Ismailia, 1928)", nat="Egyptian", life="1906–1949",
  stance="hostile — grieved the abolition; the Brotherhood's founding reflex", tags=["antagonist", "islamist", "egypt", "verified"], body="""
The Brotherhood's founder is the first great Islamist for whom Kemal's act is *background
weather*. The sentence that Arabic writers on every side of the Brotherhood quote from his
memoir *Mudhakkirat al-Da'wa wa'l-Da'iya* ("Memoirs of the Call and the Caller"), recalling the
mid-1920s:

> «لقد قامت تركيا بانقلابها الكامل، وأعلن مصطفى كمال باشا إلغاء الخلافة وفصل الدولة عن الدين في أمة كانت إلى بضع سنوات في عرف الدنيا جميعًا مقرّ أمير المؤمنين»
> ("Turkey carried out its complete coup, and Mustafa Kemal Pasha announced the abolition of the caliphate and the separation of state from religion, in a nation that until a few years earlier was, in the world's reckoning, the seat of the Commander of the Faithful.")

It is a lament, not an indictment, and the card should not inflate it: the quoting writers
(an Arabic research site, and a polemical anti-Brotherhood site) both present it as al-Banna
mourning a fall, and the second says his memoir ties the Society's 1928 founding to the
abolition. The scholarly reading supplies the rest of the position: Wagemakers shows that
al-Banna, unlike [[Ali Abd al-Raziq]] and in line with [[Rashid Rida]], treated the caliphate
as "the symbol of Islamic unity", made working for its return a Brotherhood priority, and
imagined a spiritual-league version of it. Kemal is the man who made the question urgent;
al-Banna's answer is institutional, not personal.

**Limits.** The memoir is retrospective; the passages were verified only through two
independent quoters, not the printed page; and no al-Banna statement naming Atatürk in the
1930s has been found. He sits in the hostile column as the first link in the chain that runs
to [[Sayyid Qutb]].

## Sources
- [Arabic Center for Research (acrseg.org), "al-Islam al-siyasi wa-ihya' al-khilafa"](https://acrseg.org/39488) — quotes the memoir passage · J
- [Whiteink, "Falsifying Ottoman history for the Islamic project" (Arabic)](https://whiteink.info/falsifying-ottoman-history-for-the-islamic-project-and-creating-the-sacred-history-of-the-ottoman-empire-12-full-page-134/) — same quote, independent quoter · J
- [Wagemakers, *The Muslim Brotherhood in Jordan* (CUP 2020), ch. "The Early Muslim Brotherhood's Political Thought"](https://www.cambridge.org/core/books/abs/muslim-brotherhood-in-jordan/early-muslim-brotherhoods-political-thought/9948C2666ECF6FBB5AB4E3DB0BAFFD5F) — on his caliphate position (snippet read) · S
""")),
]

E = [
("Koçgiri Leaders Write to Ankara, 1920", "1919–November 1920", """
The earliest *Kurdish* gaze on Mustafa Kemal in the census, and a double one: Kurds in the
Koçgiri and Dersim country who first heard him as a would-be ally, then answered him with
an ultimatum. Robert Olson's article (*Oriente Moderno*, 1989), built on [[Nuri Dersimi]]'s
memoir, gives the sequence.

- **The audience.** A Koçgiri leader (the excerpt read prints him as "... Beg, the son of
  Koçgirili Mustafa Paşa"; Wikipedia names him Alişan Bey) told Mustafa Kemal that the Kurds
  were working for an autonomous Kurdistan "as proclaimed in President Wilson's Fourteen
  Points". Kemal replied that Wilson's principles were "worthless for the peoples of the east"
  and told the young Kurds to cooperate with his nationalist representatives in Dersim;
  he said the Erzurum Congress (23 July–7 Aug 1919) had committed "all of Kurdistan" to him.
  Olson's judgment: it was this harsh answer that made the young Kurds cut their link with the
  Society for the Rise of Kurdistan in Istanbul and move toward rebellion.
- **The declaration.** On 15 November 1920, after a meeting of Kurdish leaders, they sent Ankara
  a declaration demanding an answer by 24 November on five points: whether Ankara officially
  accepted the Kurdish autonomy agreed by the Sultan's government; its stance toward an autonomous
  Kurdistan; release of Kurdish prisoners in Elaziz, Malatya, Sivas and Erzincan; withdrawal of
  Turkish officials from Kurdish-majority areas; and withdrawal of the troops sent to Koçgiri.
  Olson reads the rebellion as an attempt to seize on Articles 62 and 64 of the [[Treaty of Sèvres]].

The ambivalence is in the sequence: they wrote to Ankara *as the possible grantor* of the
autonomy Istanbul had promised. The Kemalist side's later reading of the same events is the
[[Sheikh Said Rebellion]] and [[Dersim Rebellion]] story.

**Caveats.** The excerpt of Olson I read is OCR text of the printed article; the leader's
name is partly cut off; the declaration's details come through Olson's footnotes to Dersimi,
*Kurdistan* (p. 143). Mustafa Kemal's own 1923 autonomy hints are a separate thread (van Bruinessen).

## Sources
- [Olson, "The Koçgiri Kurdish Rebellion in 1921 and the Draft Law for a Proposed Autonomy of Kurdistan", *Oriente Moderno* 69/1–6 (1989), pp. 41–56](https://doi.org/10.1163/22138617-0690106006) · S
"""),

("Ihsan Nuri's Ararat Papers, 1927–1930", "1919–1930", """
The vault card [[Ihsan Nuri Pasha]] gives the rebel; this card gives the **turn**. A review
essay on the Hoybun/ARF archive (the Ağrı headquarters' reports and the Hoybun centre's answers
for 1927–1930, kept by the Armenian Revolutionary Federation) reads İhsan Nuri's path as a
change of mind about Mustafa Kemal's movement:

- **1919–1920: sympathiser.** Back in Istanbul after the war, he still saw himself as an Ottoman
  officer, was less "Kurdist" than the *Jin* newspaper circle, and — although citing Wilson's
  principles — thought the Kurds should support the movement Mustafa Kemal had started.
- **1927–1930: commander.** As Hoybun's extraordinary commissioner on Ararat (code name "Cemşit")
  he ran the [[Ararat Rebellion]]'s military and civil structure. The essay's verdict is that
  even for him Kurdish nationalism "could not go beyond" a reaction to the Turkish nationalism
  the Kemalist elite practised, and that he was a candidate to be the **Kurds' Mustafa Kemal** with
  a residue far weaker than Mustafa Kemal's Ottoman one.
- **The answer from Ankara.** A Hoybun-organisation study records that a cabinet meeting
  chaired by President Mustafa Kemal Atatürk on 28 December 1929 decided on a punitive operation
  on Ararat (citing Göktaş 1991). By autumn 1930 İhsan Nuri was forced to take refuge in Iran,
  which the essay says he did not regard as a "defeat".

**Caveats.** Both studies are Turkish-language; the review essay's author and its parent book
(*Ağrı Dağı'nda Cumhuriyet Kurmak*) are not captured in the page text, so the evidence is
scholarly-secondary on archival letters, not the letters themselves. The Hoybun article is
DergiPark's "Hoybun Örgütü: Kürt Milliyetçiliğinde Yeni Bir Evre". Connect: [[Celadet Bedir Khan]] (Hoybun's president), [[Ararat Rebellion]].

## Sources
- [Kürt Araştırmaları, review essay on the Ağrı Dağı papers (ARF archive file 1662)](https://kurdarastirmalari.com/details/agri-daginda-cumhuriyet-kurmak-yeni-belgeler-isiginda-agri-syani) · S−
- [DergiPark, "Hoybun Örgütü: Kürt Milliyetçiliğinde Yeni Bir Evre"](https://dergipark.org.tr/tr/download/article-file/798293) · S
"""),

("Armenian Readings of Kemalism, 1920s", "1920s", """
**A national calamity looks at the winner.** In 2024–25 Vahram Ter-Matevosyan (American
University of Armenia) published a survey of how Armenians read Kemalism in the 1920s
(*Turkish Studies* 26/1, pp. 120–141). The AUA release summarises the finding in a line the
census needs: unlike "the favorable and celebratory nature of the overwhelming majority" of
European, Middle Eastern, North African, Balkan and South Asian observations, **Armenian views
"bore the imprint of national calamity, despair, and division".**

What the abstract and release add:
- Both Soviet-Armenian and Diaspora observers were well versed in Kemalist principles and reforms
  and used the terms "Kemalism" and "Kemalocracy" in the early 1920s — earlier than many observers
  who followed Turkish domestic politics closely; by the mid-1920s "Kemalism" was everywhere in
  Armenian and Russian periodicals and debates.
- Their reason for watching was different from other nations': "the extraordinary events of the
  Armenian Genocide" (see [[Armenian Genocide]]) made the motive to monitor Turkey's domestic
  transformation fundamentally different.
- The article's main contrast is between Soviet and Diaspora Armenian interpretations.

**What is not yet in hand.** The article itself is paywalled; only the abstract, the release and
a footnote citation (*Hairenik* Monthly, Aug. 1925, no. 10 (31), p. 121 — the ARF's Boston
organ) were readable, so **no individual Armenian author's words are quoted here.** Each named
voice is a lead (see `candidates/hostile-gazes.md`). [[Treaty of Lausanne]] is the moment the
sources locate the diaspora's hopes ending, but the Armenian National Delegation's own reading
of Kemal is not in this card.

## Sources
- [Ter-Matevosyan, "Armenian interpretations of Kemalism: rethinking diaspora and Soviet intellectual debates in the 1920s", *Turkish Studies* 26/1 (2025), 120–141](https://www.tandfonline.com/doi/full/10.1080/14683849.2024.2376659) (abstract only) · S
- [AUA Newsroom release, 19 July 2024](https://newsroom.aua.am/2024/07/19/dr-vahram-ter-matevosyan-published-in-turkish-studies-journal) · J (summary of S)
"""),

("The Comintern's Verdict on Kemal, 1922–1928", "1922–1928", """
The Communist International could not decide whether Mustafa Kemal was an ally or a gendarme,
and said both, in print, for six years — while the Turkish party it sponsored
([[Mustafa Suphi]], [[Şefik Hüsnü]]) was being jailed or killed by him.

- **Fourth Congress, Nov–Dec 1922: the Open Letter.** "Open Letter to the Communists and Working Masses of Turkey", presented by the TKP
  delegate Orhan (Sadrettin Celal Antel) and unanimously adopted: the workers and peasants of Turkey had been "a living
  example of a revolutionary independence movement", but Ankara was "ready to come to terms with
  the imperialists for the sake of certain concessions in favour of the Turkish big bourgeoisie",
  wanted to rid itself of the class-conscious representatives "in preparation for an understanding
  with imperialism", and wished "to appear at the Lausanne conference as a truly bourgeois
  Government". The Congress "protests emphatically against this barbarous act" yet is "willing to
  support any government or political party which does not play the part of a gendarme of imperialism".
- **Karl Radek, 23 Nov 1922.** Telling the persecuted Turkish communists: *"The task of defending
  Turkish sovereignty, which has great international revolutionary importance, is not over. You
  should defend yourself against your persecutors ... but ... historically the moment for the
  liberation struggle has not arrived."*
- **1927: the Soviet commentators.** Vladimir Osetrov, writing as "Irandoust" in the party press,
  called Kemalism an "authentic mass revolution" with both revolutionary and counter-revolutionary
  sides: *"the future of Kemalism depends on its anti-imperialistic character, otherwise the
  possible compromise with imperialism would mean the crisis of Kemalism and its program."*
  The same year "Bekar Ferdi" — Şefik Hüsnü's pseudonym — wrote that the Kemalists brought the
  national bourgeoisie to power through forced measures against possible opposition, had taken a
  wrong turn by trusting the West toward a "capitalist path", and hoped that repression would
  push the Turkish working class to the communists; a second 1927 piece told Chinese
  communists to learn from Kemalism's hijack by the bourgeoisie.
- **The summary arc.** Ter-Matevosyan: "Initially viewed as an ally in the struggle against the West,
  Kemalism was later treated mainly negatively by the Communist regime", before a more favourable
  revisit in the 1960s.

**Provenance.** The Open Letter and Radek lines come through the WSWS "Foundation of Modern
Turkey" series (a partisan Trotskyist source, J) quoting the Comintern protocols, with the
primary Turkish-party documents attributed there to Akbulut & Tunçay, *Türkiye Komünist
Partisi'nin Kuruluşu* (2020). The 1927 lines are Ter-Matevosyan's, via a blog's long extracts
from his work (J relaying S), whose abstract and book are the scholarly anchor. Neither letter
nor commentators ever write of "Atatürk" the person: the gaze is on his government and system.

## Sources
- [Ter-Matevosyan, "Kemalism and Communism: From Cooperation to Complication", *Turkish Studies* 16/4 (2015)](http://tandfonline.com/doi/full/10.1080/14683849.2015.1081071) (abstract) · S
- [Democracy and Class Struggle blog, extracts of Ter-Matevosyan on Irandoust and Ferdi](https://democracyandclasstruggle.blogspot.com/2015/12/kemalism-and-communism-1920-30s-prelude.html) · J
- [WSWS, "The Foundation of Modern Turkey, the Communist International"](https://wsws.org/en/special/library/foundations-turkey/03.html) · J (partisan; quotes Comintern protocols)
"""),

("Nursi in Ankara, 1922–1923", "1922–April 1923", """
A deeper, biography-sourced companion to the vault's second-hand [[Said Nursi]] card — the
"famously heated argument" with Atatürk there is, in the Vahide biography, a more specific
and more interesting scene.

**Invited, applauded.** Said Nursi arrived in Ankara in 1922 to a hero's welcome: the
Assembly's record notes the applause as he mounted the platform, congratulated the veterans of
the War of Independence and led a prayer. He had come hoping to steer the new republic toward
a Qur'an-based order. What he found, in his own words, was "an abominable current of atheism".

**The Ten Points.** On 19 January 1923 he circulated a ten-point letter to the deputies stressing
the obligatory prayers: those who neglect their religious duties are "not fit to govern"; the
Assembly has taken the Sultanate and must answer the Caliphate's duties too, or discord follows.
Karabekir read it to Mustafa Kemal ([[Kâzım Karabekir]]). Vahide says about sixty deputies began
praying regularly, so that the Assembly's prayer room had to be enlarged.

**The shouting match.** The Assembly's president — Mustafa Kemal — told him angrily in front of
many deputies: *"We are in need of heroic hojas like you. We called you here in order to benefit
from your elevated ideas, but you came here and immediately started writing things about the
prayers, and have caused differences amongst us."* Nursi replied, angry in turn: *"Pasha!
Pasha! After belief, the most elevated truth in Islam is the obligatory prayers. Those who do
not perform the prayers are traitors, and the opinions of traitors are to be rejected."*

**The courtship.** Per Vahide, Kemal swallowed his anger; two days later they spoke for two
hours; he offered Nursi the post of General Preacher of the Eastern Provinces at 300 liras,
a seat in the Assembly, and a position in the Dar'ül-Hikmet. Nursi refused, saying "The New
Said wants to work for the next world and cannot work with you, but he will not interfere with
you either." Kemal was one of the 163 of 200 deputies endorsing 150,000 liras for the eastern
university Nursi proposed. At the station, on 17 April 1923, he asked Nursi's view of statues;
the reply was that the Qur'an attacks idols, and that "statues of Muslims are monuments like
hospitals, schools, orphanages, mosques, and roads."

So: a courted dissenter who would not be co-opted. The hostility is conditional and
theological, and "conflicted" is the truer word for 1922–23. The later prisons and the *Risale-i
Nur* are the other half of the Nursi story (see [[Sheikh Said Rebellion]] for the armed
contrast and [[Abolition of the Caliphate]]).

**Provenance and caveat.** The source is Şükran Vahide's biography as hosted by the Risale-i
Nur Kulliyat site of a Nur-movement publisher (iikv.org; author/edition attribution to be
confirmed); its facts come from Nursi's own *Tarihçe-i Hayat*, *Lem'alar*, *Şualar* and
*Emirdağ Lahikası*, and from Şahiner's hagiographic life — so the dramatic dialogue is the
movement's memory, not an independent record. Lewis (*Emergence*, p. 381) supports only the
side-fact of the summer-1922 opposition group in the Assembly.

## Sources
- [Vahide, Bediuzzaman Said Nursi biography (Risale-i Nur Kulliyat), pp. 184–188](https://iikv.org/en/kulliyat/bediuzzaman-said-nursi/187) (and pp. [185](https://iikv.org/en/kulliyat/bediuzzaman-said-nursi/185), [186](https://iikv.org/en/kulliyat/bediuzzaman-said-nursi/186), [188](https://iikv.org/en/kulliyat/bediuzzaman-said-nursi/188)) · S (movement-sourced)
"""),

("Toynbee on the Audacious Rebel, 1922", "1922", """
A deeper primary-source companion to the vault's [[Arnold J. Toynbee]] card. The man who
edited Britain's 1916 Blue Book on the Armenians (under Lord Bryce) turned, after reporting the Greek-Turkish war
for the *Manchester Guardian* in 1921–22, into the Western world's most prominent academic
Turkophile — "his conversion from institutional Philhellenism to unapologetic Turkophilia"
(Chrissochoidis) went with his resignation of the Koraes chair in 1924, under a cloud.

*The Western Question in Greece and Turkey* (1922) has one sustained passage on Mustafa Kemal,
and it begins with a refusal: *"In regard to Mustafa Kemal Pasha I have therefore only to say that
he is not a Jew; not a member of that group of politicians who controlled the Committee of Union
and Progress ... and not under suspicion of making money or other personal gain out of his present
position."* Toynbee had not met him ("I have not met Mustafa Kemal Pasha in the flesh"), because
British policy barred him from visiting the Nationalist leaders in 1921. What he does say:

> "Once there, he taught his countrymen a new answer to an old riddle. ... He proved by a personal demonstration that a Turk can be his own master in Anatolia without having to wait for a better world, and under his inspiration the National Movement sprang to life."

(The riddle is footnoted: *"Where is a Turk his own master?"* — answer, traditionally, *"In Hell."*)
He calls Kemal an "audacious rebel" condemned by the Ottoman officials, and adds: *"I can certify
that he is not a 'Kemalist.' He is a Turkish Nationalist."* Elsewhere the same book condemns the
Greek destruction of Turkish villages (quoting a commission of inquiry), which is why Toynbee
sits in this deck at all: the same mind that had written the Armenian Blue Book wrote this,
and the Greek side judged it betrayal.

**Why "conflicted".** The 1922 text on Kemal is guardedly sympathetic; the conflict is Toynbee's
arc (Blue Book 1916; Turkophile 1922; later mixed verdicts on the one-party state, not yet
sourced here). The deck keeps both. See [[Eleftherios Venizelos]] for the Greek mirror, [[Greco-Turkish War]].

## Sources
- [Toynbee, *The Western Question in Greece and Turkey* (1922), full text, archive.org](https://archive.org/stream/westernquestioni00toynrich/westernquestioni00toynrich_djvu.txt) — chapter "Greek and Turkish Government", pp. 178–180 · P
- [Chrissochoidis, "Toynbee's 1921 Anatolian letters", *Modern Greek* (Hoover)](https://ahifworld.net/uploads/1/1/7/1/117198244/7_ilias_chrissochoidis.pdf) · S
- [H-Diplo review 988 of Giannakopoulos on Toynbee](https://networks.h-net.org/node/28443/discussions/6590413/h-diplo-article-review-988-giannakopoulos%C2%A0-%E2%80%9C-world-safe-empires%C2%A0) · S
"""),
]

for name, kw in P:
    person(name, **kw)
for n, when, b in E:
    note("Events", n, {"type": "event", "when": when, "tags": ["event", "verified", "hostile-hunt"]}, b)

print(f"census r5 hostile: {len(P)} people, {len(E)} events")
