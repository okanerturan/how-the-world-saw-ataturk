# -*- coding: utf-8 -*-
# Census round 2 (Aug 2026) — obituary-corpus country cards.
# Primary routes: Delpher OCR harvest (NL), Toksoy 2010 full text (sources/), GHDI document (DE).
from _lib import note

E = [
("Dutch Press, November 1938", "10–25 November 1938", """
**The first fully machine-harvested country card.** The Dutch national corpus (KB/Delpher) holds
**812 articles** in the funeral window alone, queryable by SRU from this project (recipe in
HUNT.md seam 3) — and the article OCR resolves, so the primary prose is in hand:

- **10 Nov** — the Reuter flash, one line: *"President Kemal Ataturk is overleden."*
- **12 Nov** — the Istanbul scenes, wired to Dutch readers: an endless stream of people crossing
  the Galata Bridge toward Dolmabahçe; a great silent crowd; flags at half-mast on every
  building; and **students on the Square of the Nation swearing to defend the republican
  principles Atatürk established**.
- **13 Nov** — a Havas dispatch from Athens: [[Ioannis Metaxas]] will attend the interment, and
  **Salonika renames the street of Atatürk's birth after him** (see [[Salonika Names His Street,
  November 1938]]).
- **24 Nov** — three papers carry an "Ataturk-Universiteit" story: the mourning already turning
  into institutions.

A neutral small country with no stake in Anatolia, watching closely — the control group of the
obituary corpus. See [[Death and State Funeral of Atatürk]].

## Sources
- KB/Delpher SRU + OCR resolver (urns incl. `ddd:010664486:mpeg21:a0010`,
  `MMRHCG03:163502019:mpeg21:a00052`, `ddd:010664491:mpeg21:a0074`), harvested 2026-08-03
"""),

("Salonika Names His Street, November 1938", "12 November 1938", """
A Havas wire from Athens, 12 November 1938 — caught in the Dutch corpus's OCR — carries two
facts in three lines:

1. **[[Ioannis Metaxas]] will attend Atatürk's interment** — the contemporary corroboration the
   ledger's ⚠️ row was waiting for: the Greek dictator went in person to bury the man who had
   destroyed the Greek army sixteen years earlier.
2. **The Salonika city council voted to give Atatürk's name to the street where he was born.**
   His birth city — Ottoman Selânik, Greek Thessaloniki since 1912, emptied of its Muslims by
   the [[Greco-Turkish Population Exchange]] — chose mourning over grievance and named his
   birth street for him. (The birth house became the Atatürk Museum; the street gesture of
   November 1938 is its origin.)

The Greek press chorus around it, per Toksoy's corpus: *Proia* — "if Turkey loses its great founder,
Greece loses a great and trusted friend" (Toksoy's footnote 16; this line was earlier misattributed here to *Estia*) —
*Estia*, which called Atatürk "a good patron of Turkish-Greek relations," and *Elinikon Mellon* in the same key. The Greek
mirror's full arc: [[Eleftherios Venizelos]] → [[Greco-Turkish Population Exchange]] →
[[Nikolaos Trikoupis]] → this street sign.

## Sources
- Havas via Delpher OCR (`ddd:010664491:mpeg21:a0074`, 13 Nov 1938 print) · [Toksoy 2010](https://dergipark.org.tr/en/download/article-file/32009), §Yunanistan (full text in `sources/`)
"""),

("Tehran Falls Silent, November 1938", "November 1938", """
Iran's card, from Toksoy's corpus: when the news arrived, **all Tehran became a silent,
motionless city in deep mourning** — and the phrase the Iranian public reached for was
**"Atatürk ölmez" — Atatürk does not die.** The papers gave him sweeping coverage — black-bordered front pages and praise of "the creator of the
new Turkey" — under headlines such as "The Great Mourning of the Eastern World" and "Mankind Has Lost Its
Greatest Man." (The phrase "guardian of independence, its head for twenty years" belongs to the Cairo daily
*al-Ahram*, quoted just before the Iran section in Toksoy, not to the Iranian press.)

The card sits on top of the state layer already in the vault: [[Reza Shah Pahlavi]], the
imitator-king who had made his only foreign trip to see Atatürk in 1934. The street grief of
1938 and the [[Ruhollah Khomeini]] reaction of 1979 are the two poles of the Iranian mirror —
the census now has both.

## Sources
- [Toksoy 2010](https://dergipark.org.tr/en/download/article-file/32009), §C İran Basını (full text in `sources/`)
"""),

("Palestine at the Radios, November 1938", "November 1938", """
The corpus's most striking contrast card. Per the contemporary reporting mined by Toksoy
(*Cumhuriyet*, 19 Nov 1938: "Palestine weeping for our Ata"): **"there is no country in the
world as affected by this death as Palestine. For three days the entire Palestinian people
gathered at their radios listening to Ankara's broadcasts — even shedding tears."**

Hold it against the vault's existing Palestinian card: [[Haj Amin al-Husseini]], the Mufti who
considered Atatürk Islam's great betrayer. **The leader despised him; the street wept for him.**
No single pairing in the census demonstrates better that "the X gaze" is never one gaze — the
Rorschach test runs *within* nations, not just between them. (Method note: the report reaches us
through the Turkish press's own eyes — a gaze upon a gaze; treat the "no country more affected"
superlative as Turkish framing, the radio-listening scenes as the datum.)

## Sources
- [Toksoy 2010](https://dergipark.org.tr/en/download/article-file/32009), §E Filistin Basını, citing *Cumhuriyet* 19 Nov 1938, p. 4 (full text in `sources/`)
"""),

("Hungary's Parliament Rises, November 1938", "November 1938", """
Hungary — zero nodes a week ago — turns out to have observed the death at state level: **both
chambers of the Hungarian parliament opened their sessions with a commemoration of Atatürk.**
*Pesti Naplo*: "the whole universe joins this great mourning… thanks to Atatürk, Turkey's
external and economic position is now excellent." And the writer **İmre Barcs** contributed the
strangest epithet in the corpus so far — an essay on the **"Bozkurt General"** (the Grey Wolf
General) who rose from the wreckage of the Central Powers' collapse in the tragic autumn of 1918
— a Hungarian writing about a fellow loser-state that fought its way back out.

The Turanist kinship framing (Hungarians and Turks as cousins) gave Hungarian admiration its own
flavor: not anti-colonial, not fascist-admiring — *familial*. Candidate thread: Barcs himself,
and the "Macar basınında Atatürk" literature. See [[Historiography of Atatürk]].

## Sources
- [Toksoy 2010](https://dergipark.org.tr/en/download/article-file/32009), §Hungary passages (full text in `sources/`)
"""),

("Ta Kung Pao Mourns, November 1938", "November 1938", """
China's card, and one of the census's most complete foreign readings. Per Toksoy's corpus,
Atatürk was esteemed in China "like a great statesman of China itself," and ***Ta Kung Pao*** —
the country's great daily — wrote: **"The death of this beloved father of a great nation leaves
a vast void not only in Turkey but on our continent and in the whole world. It was he who drove
the foreign invaders from Turkey and then, harboring not the smallest grudge, built the most
sincere bonds of friendship with them — treaties of amity even with nations that had risen
against Turkey in enmity. A terrifying enemy of invaders, and the most reliable friend of any
who renounced their designs."**

That is the full "Sick Man of Asia" reading in one paragraph — the same lesson [[Chiang
Kai-shek]]'s KMT had made required reading, delivered as a eulogy. Pair with [[Mao Zedong]]'s
cooler verdict for the complete Chinese mirror.

## Sources
- [Toksoy 2010](https://dergipark.org.tr/en/download/article-file/32009), §G Çin Basını (full text in `sources/`)
"""),

("Hamburger Tageblatt, November 1938", "November 1938", """
The German card, standing on a curated primary document: **German History in Documents and
Images (GHDI)** presents two *Hamburger Tageblatt* texts from two issues — the obituary of 10 November 1938 (p. 2,
"Vom Rebell zum Vater der Türken"), admiring the national revitalization (military reorganization,
educational reform, the veil, the Latin alphabet), **plus, a month later (10 December 1938, pp. 1–2), an
essay attributed to Atatürk himself, "The Leader and His People"** (the two are not printed together) — the leader who serves his own interest is "only a second-rate man" — printed by a
Nazi paper as leadership doctrine.

GHDI's editorial frame matches Ihrig's thesis exactly: Nazi Germany read Atatürk's "new national
consciousness" as a model of the leadership it valued in itself. This card gives the [[Adolf
Hitler]] node its documentary floor — a real Nazi-era newspaper page, translated and curated by
a scholarly project, doing precisely what Ihrig says the German press did. (The "eclipsed
Kristallnacht" formulation remains a page-level Ihrig check — this card neither proves nor needs
it.)

## Sources
- [GHDI: "Admiration for Atatürk, Turkey's Leader (1938)"](https://germanhistorydocs.org/en/nazi-germany-1933-1945/admiration-for-atatuerk-turkeys-leader-1938) · [History Studies: Reflections of Atatürk's Death on the German Newspapers](https://www.historystudies.net/eng/reflections-of-ataturks-death-on-the-german-newspapers_1146)
"""),
]

for n, when, b in E:
    note("Events", n, {"type": "event", "when": when, "tags": ["event", "verified", "obituary-corpus"]}, b)

print(f"census r2: {len(E)} country cards")
