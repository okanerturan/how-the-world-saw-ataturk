# -*- coding: utf-8 -*-
# Census round 1 (Aug 2026) — promotions from candidates/ per HUNT.md pipeline.
# Every node here carries sources; tag: verified.
from _lib import note, person

P = [
("Shakib Arslan", dict(role="Pan-Islamist publicist, 'Prince of Eloquence'", nat="Lebanese (Druze); Geneva exile", life="1869–1946",
  stance="hostile mirror — the pan-Islamist prosecutor", tags=["antagonist", "islamist", "verified"], body="""
The interwar Muslim world's most tireless publicist — *Amir al-Bayan*, the Prince of Eloquence —
running his campaign for Islamic nationalism from Geneva exile through his journal *La Nation
arabe*. An ardent Ottomanist who had lobbied to preserve the Caliphate after WWI, he became, in
William Cleveland's phrase, **particularly hostile to Atatürk**: for Arslan, political
independence was worthless if it was used to imitate the West rather than preserve cultural
integrity, and the [[Abolition of the Caliphate]] in March 1924 fixed Kemalism as his negative
pole and sharpened intra-Islamic tensions across the interwar decades.

His place in the deck: the **articulate hostile card** of the apostate mirror — where [[Mustafa
Sabri Efendi]] prosecuted Atatürk in theology and [[Sayyid Qutb]] later systematized the
rejection, Arslan prosecuted him in the international press, from Europe itself. Same milieu of
exiled anti-Kemalist pan-Islamism that intersected [[Haj Amin al-Husseini]]'s networks.

## Sources
- [Cleveland, *Islam Against the West: Shakib Arslan and the Campaign for Islamic Nationalism* (U Texas Press)](https://www.goodreads.com/book/show/714292.Islam_Against_the_West) · [1914-1918-online encyclopedia entry](https://encyclopedia.1914-1918-online.net/article/arslan-shakib-amir/) · [Wikipedia](https://en.wikipedia.org/wiki/Shakib_Arslan)
""")),

("The Korean Colonial Press", dict(role="Collective gaze — Korea under Japanese rule", nat="Korean", life="1920s–1930s",
  stance="coded admiration — liberation read as self-statement", tags=["movement", "anti-colonial", "verified"], body="""
From the early 1920s, *Dong-A Ilbo* — flagship newspaper of the Korean national movement, founded
1920 — covered "Kemal Pasha" frequently, presenting Turkey as a country whose history ran
parallel to Korea's own. Korean intellectuals under Japanese rule took him and his state-building
as an example for regaining independence; the paper's portrait ran from "ambitious revolutionary"
to "founder of the new country."

Why this card matters beyond its region: a **colonized press writing about another nation's
liberation under the censor's eye** — the admiration itself was a coded self-statement, the same
mechanism as [[Sinn Féin and the IRA]] in Ireland and [[Kazi Nazrul Islam]] in Bengal, operating
under a censorship regime harsher than either. Dedicated Korean scholarship exists: a Seoul
National University repository study on "the image of Kemal Pasha as a statesman in modern Korea
and its evolution."

*Rigour note: the SNU item's author/year still need completing (the repository page is
JS-gated to automation) — LEDGER row open.*

## Sources
- [SNU repository: 근현대 韓國에서 케말 파샤의 政治家像과 그 추이](https://s-space.snu.ac.kr/handle/10371/154969) · [Dong-A Ilbo history](https://en.wikipedia.org/wiki/The_Dong-A_Ilbo)
""")),
]

E = [
("Bulgarian Mourning, November 1938", "10–22 November 1938", """
**The first completed country card of the obituary corpus** — built from Nurcan Toksoy's study of
the Balkan and Middle Eastern press reaction (mining contemporary *Kurun*, *Akşam* and *Ulus*
reports) and İbrahim Tatarlı's "Bulgar Basınında Atatürk."

What the neighbor did when the news came:
- A memorial gathering in the **hall of the Bulgarian Academy of Sciences**, attended by the
  Romanian and Greek ambassadors, members of parliament and professors, opened by the president
  of the Turkish-Bulgarian Friendship Society with a moment of respect (*Kurun*, 22 Nov 1938).
- A press chorus across **Slovo, Utro, Dines, Zorya, La Parole Bulgare** — *Slovo*, whose director **Todor Pavlov Kojuharov** (1892–1945; director 1926–44, Transport Minister in
  the Toshev cabinet of 1935) signed a tribute; and *Mir*, which carried a separate article signed
  "Pavlov, former Bulgarian ambassador to Ankara" (Toksoy; whether that Pavlov is the same man as Kojuharov is
  not established, and Toksoy's biographical note on Kojuharov does not call him an ambassador).
- The headline that belongs in the eventual exhibit: **"After the death of this exceptional and
  Great Man, the world is not as interesting as it used to be."**

Bulgaria had spent the 1930s in coups and in tension over its Turkish minority — and still the
grief chorus ran. The same Toksoy corpus stages further cards: Greek papers (*Estia*: "if Turkey
loses its founder, Greece loses a great and trusted friend"), Hungary's *Pesti Naplo*, Swedish
press quotes, Romania's black flags on official buildings on funeral day. Full extracted text
banked at `sources/toksoy-2010-balkan-mideast-press.txt`.

See [[Death and State Funeral of Atatürk]], [[Balkan Pact]], [[Ioannis Metaxas]].

## Sources
- [Toksoy, "Atatürk'ün Vefatının Balkanlar ve Ortadoğu Basınındaki Etkilerinin Türkiye'deki Akisleri," *Atatürk Üniversitesi SBE Dergisi*, 2010 (PDF)](https://dergipark.org.tr/en/download/article-file/32009) — full text in `sources/` · Tatarlı, "Bulgar Basınında Atatürk" (cited therein) · contemporary refs: *Kurun* 14/16/22 Nov 1938, *Akşam* 12/16/18 Nov 1938, *Ulus* 17 Nov 1938
"""),
]

for name, kw in P:
    person(name, **kw)
for n, when, b in E:
    note("Events", n, {"type": "event", "when": when, "tags": ["event", "verified", "obituary-corpus"]}, b)

print(f"census r1: {len(P)} people, {len(E)} events")
