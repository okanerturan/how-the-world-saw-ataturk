# -*- coding: utf-8 -*-
# Census round 10 (Nov 2026) — Soviet and communist named voices on Kemal and the Kemalists, 1920-1930.
# All texts read in full on marxists.org (Zinoviev at Baku, Stalin 1920 and 1927, M. N. Roy in Inprecor,
# Rosmer in The Militant) or in a documentary edition mirrored on marxistleninists.org (Chicherin 1920).
import json, os
from _lib import note, links

NODE = "Soviet Leaders on the Kemalists, 1920–1930"
BAKU = "https://www.marxists.org/history/international/comintern/baku/ch01.htm"
ST20 = "https://www.marxists.org/reference/archive/stalin/works/1920/11/30.htm"
ST27 = "https://www.marxists.org/reference/archive/stalin/works/1927/05/13.htm"
ROY = "https://marxists.org/history/international/comintern/inprecor/1922/v02n089-oct-17-1922-Inprecor.pdf"
ROS = "https://marxists.org/archive/rosmer/1930/01/turkey.htm"
CHI = "http://marxistleninists.org/Soviet%20Archives/Bolshevik%20Leaders%20Correspondence/1920/april%2023%20%201920.htm"
RAD = "https://marxists.org/archive/radek/1922/radek04.htm"

note("Events", NODE,
     {"type": "event", "when": "1920–1930",
      "tags": ["event", "verified", "hostile-hunt", "communist"]}, """
Round 9 recorded the Comintern as an institution. This card adds the **named** voices, each in their own
words: what Zinoviev, Stalin, Chicherin, M. N. Roy, Karakhan and Alfred Rosmer wrote or said about
Mustafa Kemal or about "the Kemalists". Most of them say it in two registers at once: an ally against
Britain, and a bourgeois dictator who will not stay one.

- **Zinoviev at Baku, 1 September 1920.** Opening the Congress of the Peoples of the East, he said the
  Soviet government supports Kemal and in the same breath told the delegates not to follow him: *"We do not
  for one moment forget that the movement headed by Kemal is not a Communist movement."* On Kemal's reverence
  for the Caliph: *"what Kemal's government is now doing in Turkey, supporting the power of the Sultans, you
  ought not to do, even if this line be dictated by religious considerations."* And: *"the policy which is being
  pursued by the present people's government in Turkey is not the policy of the Communist International, it is
  not our policy. And at the same time we say that we are ready to help any revolutionary struggle against the
  British Government."* (Stenographic report, 1st session; Zinoviev's speech.)
- **Chicherin to the Politburo, 28 June 1920.** The Foreign Commissar pressed for the promised arms: delay *"will
  force Mustafa Kemal to look at us as talkers and deceivers, and what is even more important, revolutionary
  Turkey can be crushed"* (English translation of the Russian documentary edition, No. 70). He describes
  Ankara as "revolutionary Turkey" in an internal memo, not in propaganda.
- **Stalin, Pravda, 30 November 1920.** In an interview on the Caucasus he said the Entente was "flirting
  furiously with the Kemalists", who were "probably executing a certain swing to the Right", and that the
  anti-colonial struggle *"will lead to victory together with the Kemalists, if they do not betray the cause
  of the liberation of the oppressed peoples, or in spite of them, if they should land in the camp of the
  Entente."* The text names "the Kemalists", not Kemal.
- **Radek, Fourth Congress, November 1922.** Primary text (Riddell translation of the proceedings, pp. 727–735):
  *"If they capitulate, then the role of Kemal Pasha is finished, haggling over the fate of Turkey will resume,
  and the Turkish people will be sold for baksheesh."* This is the same speech already recorded as
  `karl-radek-1922` from a WSWS relay; the primary text adds the Kemal sentence and the Rauf Orbay and Refet
  Pasha attribution of the persecutions. See [[The Comintern's Verdict on Kemal, 1922–1928]].
- **M. N. Roy, Inprecor, 17 October 1922.** *"The Turkish Victory"* credits the Turks with having challenged
  "European Imperialism" successfully, then turns on Kemal for stopping at the Straits: *"like a military
  dictator devoid of any revolutionary inspiration or outlook, he hitched himself to the yoke of French
  Imperialism intriguing against British Imperialism."* (p. 671; the OCR of the PDF is noisy, the sentence is
  de-hyphenated.)
- **Karakhan in Ankara, December 1929.** On arrival he said of the new Turkey: *"What I have seen, especially in
  this regard, is not strange to me. They are the same ideas and the same state of mind that prevails in our
  country."* Known to the vault only through Rosmer's English rendering.
- **Alfred Rosmer, The Militant, 18 January 1930.** The Left Opposition reading of the same visit: *"Kemal
  governs Turkey as an absolute autocrat by basing himself on a 'monolithic' party and having workers who
  criticize it thrown into prison. Stalin is not Kemal; but ... he would like well enough to resemble him."*
- **Stalin, 13 May 1927.** Asked at Sun Yat-sen University whether a Kemalist revolution was possible in China:
  *"A Kemalist revolution is a revolution of the top stratum, a revolution of the national merchant bourgeoisie,
  arising in a struggle against the foreign imperialists, and whose subsequent development is essentially
  directed against the peasants and workers, against the very possibility of an agrarian revolution."* He
  allowed that in Turkey "the struggle against imperialism could end with a curtailed anti-imperialist
  revolution on the part of the Kemalists", and named Zinoviev, Radek and Trotsky as the opposition that
  confused the two cases.

**Reading.** Between 1920 and 1927 the Soviet line moves from "support, with a warning" to a class label
("top stratum", "bourgeois"). By 1930 the opposition is using Kemal as a mirror for Stalin. None of these
voices is hostile in the way the Turkish liberal or royalist press was hostile; the Soviet reading of Kemal
is mostly about what the Soviet reader should not do or become. Mustafa Suphi's killing in January 1921 and
the 1925 and 1927 repressions are the background (see [[Mustafa Suphi]], [[Şefik Hüsnü]], [[Vladimir Lenin]]).
""" + links("The Comintern's Verdict on Kemal, 1922–1928", "Mustafa Suphi", "Vladimir Lenin") + """

## Sources
- Zinoviev, speech at the First Congress of the Peoples of the East, Baku, 1 Sept 1920 (first session), stenographic report ch. 1 · P/S — [text](""" + BAKU + """)
- Chicherin, memorandum to the Politburo, 28 June 1920, in *Bolshevistskoe rukovodstvo. Perepiska 1912–1927*, ed. Kvashonkin et al., 1996, No. 70 (RTsKhIDNI f. 5 op. 2 d. 314 l. 12); English translation on marxistleninists.org · S, translation unchecked against the Russian — [page](""" + CHI + """)
- Stalin, "The Situation in the Caucasus", interview, *Pravda* No. 269, 30 Nov 1920 (Works, vol. 4) · P — [text](""" + ST20 + """)
- Radek, report on the Eastern question, Fourth Comintern Congress, Nov 1922 (*Toward the United Front*, Haymarket, pp. 727–735) · P — [text](""" + RAD + """)
- M. N. Roy, "The Turkish Victory", *International Press Correspondence* vol. 2 no. 89, 17 Oct 1922, p. 671 (contents list p. 671; page 672 begins after "financial magnates") · P — [PDF](""" + ROY + """)
- Stalin, "Talk with Students of the Sun Yat-Sen University", 13 May 1927 (Works, vol. 9), question "Is a Kemalist revolution possible in China?" · P — [text](""" + ST27 + """)
- A. R. (Alfred Rosmer, as filed by the Marxists Internet Archive), "Karakhan Takes a Pleasant Trip to Turkey", *The Militant* vol. 3 no. 3, 18 Jan 1930, p. 7 · P for Rosmer's view, J for Karakhan's words — [text](""" + ROS + """)
""")

def rec(id, voice, vt, role, country, now, domain, date, era, mirror, pol, inten, saw, quote, art, ev, med, cav, src):
    return dict(id=id, voice=voice, voice_type=vt, role=role, country=country, country_now=now, domain=domain,
                date=date, era=era, mirror=mirror, polarity=pol, intensity=inten, what_they_saw=saw, quote=quote,
                artifact=art, evidence=ev, mediated_by=med, caveat=cav, node=NODE, sources=src)

R = [
 rec("zinoviev-baku-1920", "Grigory Zinoviev", "person", "Comintern president, opening the Baku Congress", "Soviet Russia", "Russia", "politics",
     "1920-09-01", "contemporary", None, "conflicted", 2,
     "Said Soviet Russia supports Kemal against Britain, but that his Sultan-and-Caliph policy is not communist and the Eastern delegates must not imitate it.",
     "We do not for one moment forget that the movement headed by Kemal is not a Communist movement.",
     "speech", "P", None, "English translation of the stenographic report as published on marxists.org.", [BAKU]),
 rec("stalin-pravda-1920-11", "Joseph Stalin", "person", "Bolshevik commissar for nationalities", "Soviet Russia", "Russia", "politics",
     "1920-11-30", "contemporary", None, "conflicted", 2,
     "Said the Kemalists fight the Entente and Russia will back them, but flagged a likely swing to the Right and a betrayal of colonial liberation.",
     "this struggle will lead to victory together with the Kemalists, if they do not betray the cause of the liberation of the oppressed peoples, or in spite of them, if they should land in the camp of the Entente.",
     "article", "P", None, "Names 'the Kemalists', not Kemal himself; interview with a Pravda correspondent, Works vol. 4.", [ST20]),
 rec("chicherin-politburo-1920-06", "Georgy Chicherin", "person", "Soviet People's Commissar for Foreign Affairs", "Soviet Russia", "Russia", "diplomacy",
     "1920-06-28", "contemporary", None, "instrumental", 1,
     "In a Politburo memo pressed for the promised arms, warning that delay would make Mustafa Kemal see Moscow as talkers and deceivers.",
     "will force Mustafa Kemal to look at us as talkers and deceivers, and what is even more important, revolutionary Turkey can be crushed",
     "report", "S", None, "Quote is an English translation of the Russian document as mirrored on marxistleninists.org; Russian original not seen; page ref is the document number (No. 70), not a printed page.", [CHI]),
 rec("mn-roy-inprecor-1922-10", "M. N. Roy", "person", "Indian Comintern leader, writing in Inprecor", "India (Comintern)", "India", "politics",
     "1922-10-17", "contemporary", "anti-colonial-liberator", "conflicted", 2,
     "Hailed the Turkish victory as proof an Eastern nation can beat European imperialism, but called Kemal a military dictator who yoked himself to French imperialism.",
     "like a military dictator devoid of any revolutionary inspiration or outlook, he hitched himself to the yoke of French Imperialism intriguing against British Imperialism.",
     "article", "P", None, "Quoted from a noisy PDF text layer; wording reconstructed from OCR; page 671.", [ROY]),
 rec("stalin-sun-yat-sen-1927", "Joseph Stalin", "person", "General Secretary of the CPSU(b)", "Soviet Union", "Russia", "politics",
     "1927-05-13", "contemporary", None, "hostile", 2,
     "Defined a Kemalist revolution as a top-stratum revolution of the national merchant bourgeoisie, turned against peasants and workers, and unsuitable for China.",
     "A Kemalist revolution is a revolution of the top stratum, a revolution of the national merchant bourgeoisie, arising in a struggle against the foreign imperialists, and whose subsequent development is essentially directed against the peasants and workers, against the very possibility of an agrarian revolution.",
     "speech", "P", None, "Gaze is on 'the Kemalist revolution' as a type, used as a foil for China, not on Mustafa Kemal personally.", [ST27]),
 rec("karakhan-ankara-1929-12", "Lev Karakhan", "person", "Soviet Deputy Commissar for Foreign Affairs", "Soviet Union", "Russia", "diplomacy",
     "1929-12", "contemporary", None, "instrumental", 1,
     "On arriving in Ankara praised the new Turkey as self-reliant and said its ideas and state of mind matched the Soviet Union's.",
     "They are the same ideas and the same state of mind that prevails in our country.",
     "visit", "J", "Rosmer, The Militant, 18 Jan 1930, p. 7 (English rendering of Karakhan's Ankara remark)", "Praise of Turkey, not of Kemal by name; known only via Rosmer's English rendering.", [ROS]),
 rec("rosmer-militant-1930", "Alfred Rosmer", "person", "French syndicalist-communist, Left Opposition", "France", "France", "press",
     "1930-01-18", "contemporary", "internal-mirror", "hostile", 2,
     "Wrote that Kemal governs Turkey as an absolute autocrat through a monolithic party and jails critical workers, and that Stalin envied the model.",
     "Kemal governs Turkey as an absolute autocrat by basing himself on a \"monolithic\" party and having workers who criticize it thrown into prison.",
     "article", "P", None, "Signed 'A.R.'; attribution to Rosmer is the Marxists Internet Archive's filing.", [ROS]),
]
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tools", ".state", "round10", "gazes_comintern.jsonl")
os.makedirs(os.path.dirname(out), exist_ok=True)
with open(out, "w", encoding="utf-8") as f:
    for r in R:
        assert len(r["what_they_saw"].split()) <= 25, r["id"]
        f.write(json.dumps(r, ensure_ascii=False) + "\n")
print(len(R), "records ->", out)
