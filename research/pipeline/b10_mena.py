# -*- coding: utf-8 -*-
# Census round 3 (Oct 2026) — Middle East & North Africa promotions.
# Sources: Özoğlu (MEI 2019) + Cengiz (GIF 2022) for Ibn Saud; Guenn / Salabi quoting al-Shihab for Ben Badis;
# Wilson (IJMES) for Rida; Toksoy 2010 full text (sources/) for the Cairo and Damascus/Beirut cards.
from _lib import note, person

P = [
("Ibn Saud", dict(role="Founder-king of Saudi Arabia (Abdulaziz Al Saud)", nat="Saudi (Najd/Hejaz)", life="1875–1953",
  stance="pragmatic peer — recognised, courted and never mimicked", tags=["instrumental", "monarch", "diplomacy", "verified"], body="""
The Wahhabi conqueror of the Hejaz looked at Kemalist Turkey the way one state-builder looks at
another: with no admiration to speak of and a lively interest in what the republic could be used
for. The record is a sequence of acts, not a quotation, and it runs on both sides of the
secular/Wahhabi divide.

- **1926.** Proclaimed King of the Hejaz on 8 January, Abdulaziz found Turkey the **first country
  in the world to recognise** his kingdom (May 1926) — a move Hakan Özoğlu reads as pragmatic, not
  ideological, and probably relished by Kemalist officers who despised the Hashemite [[Hussein bin
  Ali]], the Arab Revolt's leader. Ankara sent three envoys at once; the chargé d'affaires reached
  Jeddah on 25 May.
- **The Mecca congress.** On 26 March 1926 Abdulaziz invited Turkish representatives to the Islamic
  Congress he was convening in Mecca — against the grain of an Arab world that wished to isolate
  Turkey after the [[Abolition of the Caliphate]]. Özoğlu's guess is that the Saudis wanted a
  regional ally beyond the Arab world; both new states, he notes, shared one thing: neither was a
  mandate of a Western power. Turkey went (Edip Bey, 25 May) but had refused the Cairo Caliphate
  conference that month on secularist grounds, and in Mecca objected to any political agenda.
- **3 August 1929.** Treaty of friendship signed in Mecca; Article 1 recognises the kingdom's
  independence "with all its territories" — in Özoğlu's words the first document to recognise the
  Saudi kingdom and open relations on an equal footing. The Saudi side ratified in November 1930.
- **22 September 1932.** On the union of Hejaz and Najd as Saudi Arabia, Atatürk sent his
  congratulations among the very first (Özoğlu: "ahead of the rest of the world"). See [[Prince
  Faisal in Ankara, June 1932]] for the prince's own visit that summer.
- **1933–38.** A congratulatory telegram from the king for the Republic's tenth anniversary
  (29 October 1933); ten Saudi students sent to Ankara for flight training (1933); a neutral Turkish
  stance in the 1934 Hejaz–Yemen war that Riyadh welcomed; and in November 1938 a telegram from
  Foreign Minister Faisal on Atatürk's death: *"It is a great loss."*

The deck position is **instrumental, with courtesy**: Ibn Saud neither borrowed Kemalism nor
condemned it, which makes him the control case for the Arab pious right — compare the open hostility
of [[Shakib Arslan]], the theological prosecution of [[Mustafa Sabri Efendi]], and the Hashemite
mirror of [[Hussein bin Ali]]. Diplomatic relations stayed at chargé level from 1926 to 1942.
(Caveat: motive is inference — Cengiz herself notes "few sources about Turkey's motivations".)

## Sources
- Hakan Özoğlu, "Heirs of the Empire: Turkey's Diplomatic Ties with Egypt and Saudi Arabia until the Mid-20th Century," in Tol & Dumke (eds.), *Aspiring Powers, Regional Rivals* (Middle East Institute, 2019), pp. 11–13 — [MEI PDF](https://mei.edu/wp-content/uploads/2020/02/Aspiring-Powers-Regional-Rivals_Feb.11-2020.pdf) (S)
- Sinem Cengiz, ["The Emergence of Saudi-Turkish Relations: Ataturk and Ibn Saud's Pragmatism,"](https://gulfif.org/the-emergence-of-saudi-turkish-relations-ataturk-and-ibn-sauds-pragmatism/) Gulf International Forum, 25 Apr 2022 — footnoted to Şişman, Bostancı (Gazi Univ. PhD 2013), Tevetoğlu (1986), and Başbakanlık Cumhuriyet Arşivi decrees (S/J)
"""
)),

("Abdelhamid Ben Badis", dict(role="Algerian reformist scholar; editor of al-Shihab; founder of the Association of Algerian Muslim Ulama (1931)", nat="Algerian (Constantine)", life="1889–1940",
  stance="conflicted — from 'apostates' to 'the greatest man of modern history'", tags=["conflicted", "religion", "islah", "anti-colonial", "verified"], body="""
The Rorschach test run twice on one man, fourteen years apart.

**1924 — the indictment.** On 28 March 1924, weeks after the [[Abolition of the Caliphate]], Ben Badis
published in *al-Najah* an article titled *"The Great Catastrophe, or the Crimes of the Kemalists
against Islam and the Muslims, and their Apostasy from the Religion."* He admitted he had earlier
praised the Kemalists "because they rose to defend the precincts of the Caliphate" and rescue a great
Muslim nation, and that he knew the Young Turk elite's creed: "we turned a blind eye to their evils
to preserve Islamic unity — and never imagined they would abolish the Caliphate." He charged them
with four crimes: against the caliphate, against the caliph (left "cast on the thresholds of the
Europeans"), against the House of Osman, and against the faith itself. In a reply the following week
he held that no caliph meeting the legal conditions now existed — and that every caliph smelling of
the foreigner (a dig at Sharif [[Hussein bin Ali]], then backed by Britain) should be refused.

**1938 — the obituary.** On Atatürk's death, in *al-Shihab* (the monthly he edited from 1925;
vol. 14, part 9, Ramadan 1357 / Nov. 1938, pp. 1–5) Ben Badis wrote under the title
*"Mustafa Kemal"*: on the 17th of Ramadan "ended the breath of the **greatest man humanity has known
in modern history**, a genius among the greatest geniuses of the East, who appear in different ages
and turn the course of history and create it anew" — "hero of Gallipoli, hero of the Sakarya, the
reviver of Turkey from near-death." Only one aspect of Mustafa Kemal's greatness made "the Muslim's
heart contract" — his stance toward Islam — and there Ben Badis spread the blame: the Caliph
sitting under British guns while issuing a call against the Anatolian fighters; the Shaykh al-Islam
and ulema whose fatwa made Kemal's blood licit; the Sufi orders; and the Muslim peoples who took
up arms alongside their masters. Kemal "did not rebel against Islam but against those who call
themselves Muslims"; he took the Turks' freedom, independence and standing among nations — "which is
not easily recovered if lost" — and Ben Badis answered the ulema who still scolded him by asking what
the countries living under Napoleon's code had given their peoples. He closed with a prayer for his
soul, condolences to the Turks, and congratulations to [[İsmet İnönü]].

Scholars read the reversal two ways. Ben Badis's own pre-1924 sympathy was with the Kemalists as
anti-imperialist resisters, and a writer working to free Algeria from France was naturally drawn to
that; and the 1938 text answers a live quarrel — Egyptian ulema were then hailing King Farouk as
caliph, a prospect Ben Badis (who in May 1938 argued for a *jama'at al-muslimin* in place of any
caliph) wished to forestall. So the same pen that damned the "apostates" in 1924 made the dead president, in 1938, the
standing reproach to clerics whose countries still lived under foreign codes.

In the deck he is **the conflicted card of the Maghreb**, set against the pure hostility of [[Shakib Arslan]]
and of the Egyptian [[Rashid Rida]], whose *al-Manar* he read and whose articles *al-Shihab* reprinted.

## Sources
- Mohamed Guenn (Qen), ["Abd al-Hamid Ibn Badis and the question of the abolition of the Ottoman caliphate,"](https://binbadis.net/archives/919) binbadis.net — surveys the 1924 *al-Najah* articles (nos. 152, 153), the 1938 *al-Shihab* pieces, with notes to Merad, *Le Réformisme musulman en Algérie* (1967) (S)
- Ali Muhammad al-Sallabi, ["Ibn Badis evaluates Mustafa Kemal Atatürk,"](http://www.alsalabi.com/article/141) quoting the Nov. 1938 *al-Shihab* text at length (S/J)
- Mandumah record: ["Ibn Badis's position on Mustafa Kemal's abolition of the Ottoman caliphate: an analytic and critical study"](https://search.mandumah.com/Record/1516739) (title-level corroboration only)
- Primary (not seen in facsimile): Ben Badis, "Mustafa Kamal," *al-Shihab* 14/9 (Nov. 1938), pp. 1–5
"""
)),

("Rashid Rida", dict(role="Syro-Egyptian Salafi theologian; editor of al-Manar; theorist of the caliphate", nat="Syrian-born, Egyptian-based", life="1865–1935",
  stance="hostile — the caliphate's theorist against Ankara's secularism", tags=["antagonist", "religion", "islah", "caliphate", "verified"], body="""
A leading Sunni reformist voice of the 1920s and early 1930s (he died in 1935), and
one whose view of Ankara refused to forgive Ankara its religious policy. In the winter of
1922–23, as the Grand National Assembly severed sultanate from caliphate, Rida serialised in
*al-Manar* what became *al-Khilafa aw al-Imama al-'Uzma* (1923), introducing it as a "gift to the
Turkish people" — an argument that the caliphate was a political-juridical office, not a spiritual
papacy.

After the abolition ([[Abolition of the Caliphate]], March 1924) his journal turned its guns on the
new regime's religious policy. Brett Wilson's IJMES study of the first Turkish Qur'an translations
calls Rida "highly influential in shaping opinion in the Muslim world" and opens with his 1924 verdict: the Ankara government's backing for a Turkish translation was "their heretical idea,"
long headed "toward this action ... in order to turn the devout people among them away from the word
of God," a pretext "to facilitate the distortion of the translation so that they can use it as they
wish" (*al-Manar* 25, 1924, p. 794). Wilson's own correction is part of the record: Mustafa Kemal
had no hand in composing those translations, and the plan Rida saw did not exist as he described it.
That makes the card a clean reading of a mirror: Rida read secular Ankara as a conspirator against the
Arabic Qur'an itself.

Where the Rida card sits: beside the pan-Islamist press line of [[Shakib Arslan]] and the Cairo exile
of [[Mustafa Sabri Efendi]] — and as the hostile twin of [[Abdelhamid Ben Badis]], who took *al-Manar* as
the model for his own journal and who, in 1938, wrote an elegy of a kind Rida never did.

## Sources
- Brett Wilson, ["The First Translations of the Qur'an in Modern Turkey (1924–38),"](https://cambridge.org/core/journals/international-journal-of-middle-east-studies/article/first-translations-of-the-quran-in-modern-turkey-192438/05D8453EF5E1169BD777129F0237565B) *IJMES* 41/3 (2009) — [author PDF](https://macalester.edu/religiousstudies/wp-content/uploads/sites/42/2012/11/TheFirstTranslationsoftheQuraninModernTurkey.pdf), epigraph and n. 2 citing Rida, *al-Manar* 25 (1924): 794 (S)
- [Wikipedia: *The Caliphate or the Supreme Imamate*](https://en.wikipedia.org/wiki/The_Caliphate_or_the_Supreme_Imamate_(book)) — for the 1923 book's date and its framing as a rebuttal to the Kemalists (T, context only)
"""
)),
]

for name, kw in P:
    person(name, **kw)

E = [
("Prince Faisal in Ankara, June 1932", "8 June 1932 (15-day visit)", """
The first high-level Saudi visit to Turkey, in the summer the kingdom was born. Prince **Faisal bin
Abdulaziz** — twenty-seven, the kingdom's first foreign minister and later King Faisal — left Jeddah on
10 April 1932 on a long tour of the states that had recognised the Saudi state, and reached Istanbul
on **8 June** aboard the Soviet ship *Kotovsky*. His fifteen-day Turkish tour took in Istanbul and then
Ankara, where **Atatürk received him**; though he was not a head of state, Turkey gave him its highest
honours — a ceremonial guard and a band — and the Saudi press at the time praised the welcome.

His arrival statement is the datum: *"I am here as a representative of a foreign government; however, I
come here as someone who feels the pain of separation and longs for unity with the sibling country.
Historical and political events that took place in the recent past have surely failed the sincerity
and fellowship that our people feel for each other. Our two peoples are brothers and will remain so."*
Özoğlu reads the warmth as a signal to the world that Turkey despised the ex-ruler of the Hejaz, Sharif
[[Hussein bin Ali]], and preferred the Saudis to the Hashemites; the Saudi dislike of reviving the
caliphate was a further reason for Ankara's friendliness.

Faisal came back to the subject six years on: when Atatürk died, as Foreign Minister he cabled Ankara
that the Saudis learned of the death with great regret — "a great loss." See [[Ibn Saud]] for the
father's side of the relationship.

## Sources
- [Özoğlu, MEI 2019](https://mei.edu/wp-content/uploads/2020/02/Aspiring-Powers-Regional-Rivals_Feb.11-2020.pdf), pp. 12–13 (S) · [Cengiz, GIF 2022](https://gulfif.org/the-emergence-of-saudi-turkish-relations-ataturk-and-ibn-sauds-pragmatism/), citing Tevetoğlu, "Bugünkü Türk-Suudi Dostluğuna İlk Adım: Gazi Mustafa Kemal-Faysal bin Abdülaziz Görüşmesi (1932)" (*Studies on Turkish-Arab Relations*, 1986) and Bostancı (Gazi Univ. PhD 2013) quoting the Turkish daily press
"""),

("Cairo Mourns, November 1938", "11–20 November 1938", """
Egypt's card, from Toksoy's corpus of the funeral window. A great mood of mourning "blew over Cairo
in particular," and **every Egyptian paper of 11 November** ran pieces on Atatürk. Three voices
stand out:

- ***Al-Ahram*** wrote: *"Mustafa Kemal is dead — or rather Atatürk is dead. The father of the Turkish
  nation and the greatest man the last centuries have produced ... the man who tore up treaties,
  refused to recognise what the powers had decided, made nations respect him"* — and then went
  for the rank order: history will record that he was the greatest man in the world, **"greater than
  Hitler, greater than Mussolini, greater than Roosevelt"**, since they led orderly, advanced states,
  while he found "a nation that had been given the name *the dying man*" and gave it his own spirit.
  "The whole Eastern world offers the Turkish nation its deepest condolences."
- **Hafız Ramazan Paşa**, a member of the Egyptian senate, told the press: *"Without Kemal Atatürk,
  would we have seen a new Turkey? Perhaps not. Would Egypt have found its present position?"* — and
  explained why Egypt's question was part of his answer: he had met Mustafa Kemal in **1912**, passing
  through Egypt with his officers to relieve Tripolitania ("already then I saw he had an unbeatable
  will"), and again in Ankara ten years later "at the peak of glory"; at **Lausanne** in 1922 "the Egyptian
  question was an important subject", and it "was concluded thanks to Atatürk's success."
- ***Al-Belağ*** carried the account of the Egyptian women's representative [[Huda Sha'arawi]]'s talk with
  Atatürk, with its praise for the revolution in Turkish women's rights, which "all the Turkish people
  admired" him for.

Hold it against the Cairo of the 1920s: [[Rashid Rida]]'s *al-Manar*, the exile of [[Mustafa Sabri
Efendi]], and the poet [[Ahmad Shawqi]]'s admiring-then-devastated arc. By 1938 the newspapers, at least,
had settled into mourning. (Method
note: the Egyptian papers reach us through Turkish dailies' translations — *Cumhuriyet*, 12 and 20 Nov
1938 — and the *Ayın Tarihi* digest; superlatives like *al-Ahram*'s rank order are the paper's own, and
the Hafız Ramazan quote is Egyptian self-interest talking about Lausanne.)

## Sources
- [Toksoy 2010](https://dergipark.org.tr/en/download/article-file/32009), §III-B "Mısır Basını" (full text in `sources/`), citing *Cumhuriyet* 12 Nov 1938 p.3 and 20 Nov 1938 p.9 ("Kemal Atatürk'le Müzakerelerim"), *Ayın Tarihi* no. 194 and *Yabancı Gözüyle Cumhuriyet Türkiye'si*, pp. 245–6
"""),

("Damascus and Beirut Weep, November 1938", "11–21 November 1938", """
Syria and Lebanon's card, from Toksoy's corpus. On the first Friday after the news the preacher at the
**Great Umayyad Mosque in Damascus** announced the death to the congregation and "the huge mosque
resounded with sobbing"; the call to prayer was then sounded in every mosque in the city in honour of
his soul and the funeral prayer in absentia was held. *Al-Ayyam* put a full-page portrait of him on its
13 November front page. The Beirut papers all ran pieces. The notes in the corpus:

- ***Elifba*** (Damascus), one of Syria's oldest papers, in its lead article: *"one of the greatest
  personalities and most formidable geniuses of a century"* who dedicated the fruit of his struggle to
  his nation, steered Turkey's ship "through terrible storms to the shore of safety" and **asked
  neither a throne from his people nor left an heir behind him**: "we can describe Atatürk as an
  international man ... the Turkish nation will feel the emptiness more than we do."
- ***Al-Taqaddum*** (Aleppo), columnist Şükrü Kender: Turkey, "the sick man" of Europe's politicians,
  stood at the brink at war's end when one man said *no — Turkey has not died* — and made her walk with
  the great powers; "what he achieved was of the nature of miracles."
- ***Savt al-Ahrar*** (Beirut) gave pages and called his death **"the greatest loss for all the nations of
  the East"**; *Essabah* (Aleppo) the same: a loss for "all the Eastern peoples who badly need his like."
- ***L'Orient*** (Beirut), "Atatürk is the miracle of humanity"; ***An-Nahar***, "one of the rare geniuses";
  and ***Ebabil*** (Beirut): *"the man who drove out the sultans, who shattered armies ... the greatest
  enemy of tyranny, founder of the eternal regime of Kemalism ... died."*
- ***Al-Qabas*** (Damascus): "we Syrians share the grief with all our hearts; our greatest consolation is
  to follow the road the great genius drew."

Set it beside the vault's other Levantine voices — [[Antoun Saadeh]], [[Sati' al-Husri]], [[Amin al-Rihani]] —
and against [[Shakib Arslan]], the Lebanese pan-Islamist who prosecuted Atatürk from Geneva: the street and
the press of Damascus and Beirut mourned in a register the Geneva exile never used. (Method note: all quotes come through Turkish dailies' translations of
the Arabic — *Akşam* and *Cumhuriyet*, 14–21 Nov 1938, and *Ayın Tarihi* — so wording is
Turkish-mediated; what is solid is *who wrote what and where*.)

## Sources
- [Toksoy 2010](https://dergipark.org.tr/en/download/article-file/32009), §III-A "Suriye ve Lübnan Basını" (full text in `sources/`), citing *Kurun* 13–14 Nov 1938, *Cumhuriyet* 14 & 19 Nov 1938 ("Şam'da ve Beyrut'ta"), *Akşam* 21 Nov 1938 p.4, and *Ayın Tarihi* pp. 193–194
"""),
]

for n, when, b in E:
    note("Events", n, {"type": "event", "when": when, "tags": ["event", "verified", "obituary-corpus"]}, b)

print(f"census r3 mena: {len(P)} people, {len(E)} events")
