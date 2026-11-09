# -*- coding: utf-8 -*-
# Census round 7 (Oct 2026) — the internal mirror, primary: the First Assembly's closed-session minutes
# (TBMM Gizli Celse Zabıtları, revised ed. 2023, open on acikerisim.tbmm.gov.tr) plus page-cited memoirs
# (Rıza Nur, Karabekir, Atay) read from open Internet Archive scans. Printed page numbers; quotes de-hyphenated
# at line breaks; English renderings are the project's own and marked "(tr.)".
from _lib import note, person

H = "https://acikerisim.tbmm.gov.tr/handle/11543/3271"
GC = "TBMM, *Gizli Celse Zabıtları* (revised edition, Ankara: TBMM, 2023) — open access"
BS2 = "https://acikerisim.tbmm.gov.tr/server/api/core/bitstreams/6d06856b-fd5d-4e7a-b7d6-f2d690b06a56/content"
BS3 = "https://acikerisim.tbmm.gov.tr/server/api/core/bitstreams/5fe786e1-4f37-41d4-831c-1eaf46ca410d/content"

EV = "TBMM Closed Sessions on the Commander-in-Chief, 1921–1922"

note("Events", EV, {"type": "event", "when": "August 1921 – November 1922", "tags": ["event", "verified", "turkish", "internal-mirror"]}, """
In the First Grand National Assembly the people who sat closest to Mustafa Kemal argued with him to his face. The
closed ("gizli", *hafi*) sittings were published only in 1980 and re-edited by the Assembly's own library in 2023
(*Gizli Celse Zabıtları*, four volumes; vol. 2 = 17 Mar 1921 – 25 Feb 1922, vol. 3 = 6 Mar 1922 – 27 Feb 1923). They
are the best primary witness to the **internal mirror** (RESEARCH.md §6, card 9): the Assembly voted him
Commander-in-Chief on 5 August 1921 — with the Greek army advancing on Ankara — and each renewal re-opened the
question *which of the Assembly's powers the Commander-in-Chief might exercise*. This card holds seven speakers,
quoted in the edition's transliterated Turkish with the project's own English renderings (tr.).

**5 August 1921 (vol. 2, 62nd sitting, pp. 187–211).** The agenda item is "the creation of a Commander-in-Chief
office and its assignment to Assembly President Mustafa Kemal Pasha" (p. 187).
- **[[Rıza Nur]]** (p. 205) accepts military powers but not legislative ones: *"Bence manası düşünülürse biz adeta
  bir Padişah intihap ediyoruz."* — "to my mind, if its meaning is thought through, we are in effect electing a
  sultan" (tr.). He adds that he cannot grasp why the Pasha asks for it.
- **Taki Efendi (Sivas)** (p. 193) opposes the *title* — "I do not find the Commander-in-Chief duty useful at all"
  ("Alelıtlak Başkumandanlık vazifesini müfid görmüyorum") — fearing that after the fall of Eskişehir every
  failure would be pinned on him: *"Fakat Mustafa Kemal Paşa bu milletin alemdarıdır."* — "but Mustafa Kemal
  Pasha is this nation's standard-bearer" (tr.).
- **Mustafa Durak (Erzurum)** (p. 203), a self-described "committee man for twenty-two years", is pleased by
  Kemal's assurance that the Assembly's life is his to protect and expects trust to grow when he commands: *"…milletin
  ve askerin itimadı artacaktır."* ("…the confidence of the nation and the soldier will increase", tr.), yet asks for
  amendments that keep executive power with the Assembly.

**4 and 6 May 1922 (vol. 3, pp. 365–405).** After Sakarya the question is whether article 2 of the 1921 law —
the Commander-in-Chief's power to act in the Assembly's place — should be withdrawn. Two Erzurum and Trabzon voices
split exactly on person versus office:
- **[[Hüseyin Avni Ulaş]]** (4 May, p. 372): *"Bir adama bin iş verilmez efendiler, hakkınızı kıskanınız."* — "a man is
  not given a thousand jobs, gentlemen; be jealous of your right" (tr.). Two days later (6 May, p. 405), after
  Kemal had reacted angrily: *"Paşa Hazretlerinin fedakârlığının derecesini bilmeyen kimse yoktur."* — "there is no
  one who does not know the degree of the Pasha's sacrifice" (tr.).
- **[[Ali Şükrü Bey]]** (4 May, p. 375): the office "does not rest on a person", yet *"…bendenizce Reis Paşa
  Hazretlerinin de Başkumandanlıkta kalması lâzımdır"* — "in my view the President Pasha too must remain in the
  Commander-in-Chief post" (tr.) — while arguing that the emergency which justified lending him the Assembly's legislative powers had passed (p. 375).

**18 September 1922 and 6 November 1922 (vol. 3).** With the army at the Straits, the cabinet itself speaks.
**[[Rauf Orbay]]**, prime minister, defends consulting the army's head in secret session: *"Mustafa Kemal Paşa
Meclisi Âliniz tarafından intihap edilmiş Başkumandandır."* (p. 905; "…is the Commander-in-Chief elected by your August
Assembly", tr.). On 6 November, as Refet Pasha is sent to take over Thrace "in the name of the government and the
Commander-in-Chief", **[[Ziya Hurşit]]** erupts: *"Ankara'da bir imparatorluk mu tesis edeceğiz? Katiyyen reddederiz.
Başkumandan kimseyi temsil edemez."* (p. 1174; "are we going to found an empire in Ankara? We reject it categorically.
The Commander-in-Chief cannot represent anyone", tr.).

**Reading.** The record does not show a faction that denied the war-leader: even the hardest speakers (Hüseyin Avni,
Ali Şükrü) concede his sacrifice or the need for the post. What the minutes record is a *constitutional* quarrel —
one man, one Assembly, whose powers? — in the voice of men who would later be pushed out of politics or, in
Ziya Hurşit's case, executed after the 1926 İzmir plot. See [[Independence Tribunals]], [[Turkish War of Independence]],
[[Abolition of the Sultanate]].

## Sources
- """ + GC + """, vol. 2: sitting 62 (5 Ağustos 1337 [1921]), pp. 187–211 (Rıza Nur p. 205, Taki Efendi p. 193, Mustafa Durak p. 203) · P — [repository record](""" + H + """) · [vol. 2 PDF](""" + BS2 + """)
- """ + GC + """, vol. 3: 4 Mayıs 1338 [1922] pp. 365–383; 6 Mayıs 1338 p. 405; 18 Eylül 1338 pp. 904–905; 6 Teşrinisani 1338 pp. 1173–1174 · P — [vol. 3 PDF](""" + BS3 + """)
- Page numbers are the printed folios of the 2023 edition (PDF page = folio). Dates: Rumi 1337/1338 years converted to 1921/1922.
""")

person("Hüseyin Avni Ulaş", role="Erzurum deputy, First Grand National Assembly", nat="Turkish", life="b. 1887 (Hacettepe thesis abstract)",
  stance="loyal opponent of concentrated power — hostile to the office's powers, admiring of the man's sacrifice", tags=["dissident", "turkish", "contemporary", "conflicted", "verified"], body="""
Erzurum deputy in the last Ottoman parliament and, after it was dissolved, in the First Assembly at Ankara
(Hacettepe thesis abstract, below). He is the most frequent speaker of the closed sittings — roughly 150 interventions in
vol. 2 and 300 in vol. 3 by a header count — and the one who most often addresses Mustafa Kemal directly as "Paşam".

**4 May 1922 — the office, not the man.** Against the clause that lets the Commander-in-Chief act in place of the
Assembly: *"Bir adama bin iş verilmez efendiler, hakkınızı kıskanınız"* (vol. 3, p. 372; "a man is not given a thousand
jobs, gentlemen; be jealous of your right", tr.). He asks for a separate Commander-in-Chief law and warns that respect "is
for nations, not persons" ("şahıslarda değil efendiler"). He insists his criticism is addressed "to the
deputyship", not to anyone present.

**6 May 1922 — the same man, two days on.** Kemal had answered sharply (Hüseyin Avni refers to "zırlamak"), and he
replies: *"Paşa Hazretlerinin fedakârlığının derecesini bilmeyen kimse yoktur"* (p. 405; "there is no one who does not
know the degree of the Pasha's sacrifice", tr.), recalling that he sent Kemal to the representative committee and was
a witness to his sacrifice, and promising to say everything to him "in plain language" rather than whisper behind his
back. This is a gaze that is hostile and admiring *at once*, which is why the dataset keeps two records
(see [[TBMM Closed Sessions on the Commander-in-Chief, 1921–1922]]).

Later accounts treat him as a leading figure of the Second Group; a 2022 column reports a 25 November 1922 motion by
Second Group members including him aimed at barring Kemal from the next parliament (secondary, not read in the minutes).

## Sources
- """ + GC + """, vol. 3, 4 Mayıs 1338 [1922] p. 372; 6 Mayıs 1338 p. 405 · P — [repository record](""" + H + """) · [PDF](""" + BS3 + """)
- [Hüseyin Avni (Ulaş) Bey: Hayatı ve Siyasi Faaliyetleri (Hacettepe University thesis, abstract)](https://openaccess.hacettepe.edu.tr/items/b027a4a3-8d57-4cae-a8cc-561f342e11cd/full) · S
- [Rıdvan Akın, "Creating a liberal democrat from a fierce opponent of Atatürk" (column, 2022)](http://en.12punto.com.tr/columnists/ridvan-akin/creating-a-liberal-democrat-from-a-fierce-opponent-of-ataturk-150522) · J
""")

person("Ali Şükrü Bey", role="Trabzon deputy; voice of the First Assembly's opposition", nat="Turkish", life="1884–1923",
  stance="would keep Kemal in command but strip the command of the Assembly's powers; killed in Ankara, March 1923", tags=["dissident", "turkish", "contemporary", "conflicted", "verified"], body="""
Trabzon deputy, journalist and former naval officer, described in an academic study as "prominent with his opposing
character in the Assembly", criticising the government "at almost every session" — including on the extension of the
Commander-in-Chief law, the Independence Courts, and the Lausanne talks (Erdem abstract below).

**4 May 1922.** In the closed sitting on whether the 1921 law was still needed he recalled that he had voted for it when
"the enemy was standing there and the government proposed leaving Ankara" (vol. 3, p. 365), and held that the post is
necessary — *"zaten hiçbir ordu Başkumandansız olamaz"* — and an office, not a person, but that *"bendenizce Reis Paşa
Hazretlerinin de Başkumandanlıkta kalması lâzımdır"* ("in my view the President Pasha too must remain in the
Commander-in-Chief post", tr., p. 375). He denies the cabinet's argument that withdrawing the law's second article would signal no confidence in the
Commander-in-Chief (pp. 375, 382).

**The end.** Ali Şükrü was killed in Ankara on 27 March 1923. The study cited below links his killing to Topal Osman,
commander of Kemal's guard; who ordered it, and what Kemal knew, is argued in the scholarship and is **not**
asserted here. This note records only his words on the floor.

## Sources
- """ + GC + """, vol. 3, 4 Mayıs 1338 [1922], pp. 365, 374–375, 382 · P — [repository record](""" + H + """) · [PDF](""" + BS3 + """)
- [The Opposition of Trabzon M.P. Ali Şükrü Bey in the First Grand National Assembly of Turkey (Erdem abstract)](https://erdem.gov.tr/ozet/192/eng) · S
- [Ali Şükrü Bey, Wikipedia (for dates)](https://en.wikipedia.org/wiki/Ali_%C5%9E%C3%BCkr%C3%BC_Bey) · J
""")

person("Ziya Hurşit", role="Lâzistan deputy, First Grand National Assembly; later condemned in the 1926 İzmir plot", nat="Turkish", life="1890–1926",
  stance="constitutionalist critic of the Commander-in-Chief's powers; executed 14 July 1926 for the İzmir plot", tags=["dissident", "turkish", "contemporary", "hostile", "verified"], body="""
First-term deputy for Lâzistan (Rize). A Salt Research authority record says he sat on the Yozgat Independence Court but
"parted ways" with Mustafa Kemal and was condemned to death for the attempt on Kemal's life (İzmir, June 1926). The
minutes show the earlier quarrel.

**6 November 1922 — "an empire in Ankara?"** As the cabinet reports that Refet Pasha is taking Thrace over "in the name of
the government and of the Commander-in-Chief", Ziya Hurşit interrupts: *"Bu, nerede görülmüştür? … Tesellüm, Hükûmet namına
olur. Başkumandan namına ne demektir? Ankara'da bir imparatorluk mu tesis edeceğiz? Katiyyen reddederiz. Başkumandan kimseyi
temsil edemez."* (vol. 3, p. 1174; "where has this ever been seen? … Taking over is done in the government's name. What
does 'in the Commander-in-Chief's name' mean? Are we going to found an empire in Ankara? We reject it categorically. The
Commander-in-Chief cannot represent anyone", tr.). The next page continues that the Commander-in-Chief stands at the head
of the armies "under the orders of the Cabinet". On 22 November he repeats that the Commander-in-Chief "is the Assembly's
Commander-in-Chief, not an independent one" (p. 1291). The target is an office and a drift; Kemal is not named in the line.

**Care.** The 1926 plot is documented history (court record and secondary accounts); this note takes no side on its
reach and quotes only what is in the minutes.

## Sources
- """ + GC + """, vol. 3, 6 Teşrinisani 1338 [1922], pp. 1173–1175; 22 Teşrinisani p. 1291 · P — [repository record](""" + H + """) · [PDF](""" + BS3 + """)
- [Salt Research authority record: Lazistan Mebusu Ziya Hurşit Paşa](https://archives.saltresearch.org/handle/123456789/23203) · S
- [İzmir plot, Wikipedia (execution date)](https://en.wikipedia.org/wiki/%C4%B0zmir_plot) · J
""")

print("census r7 internal: 1 event, 3 people")
