# -*- coding: utf-8 -*-
# Census round 9 (Oct 2026) — the İzmir plot in the Assembly: the opening of the fourth session
# (1 Nov 1926) and the congratulations motions (3 Nov 1926), Dönem 2, cilt 27. Per-sitting PDFs:
# www5.tbmm.gov.tr/tutanaklar/TUTANAK/TBMM/dDD/cCCC/tbmmDDCCCSSS.pdf. Page numbers are the printed
# folios; the 1926 text layer is OCR-degraded (ç/ş, ligatures), so quotes are de-hyphenated and
# obvious OCR errors normalised, with the raw forms named in the notes.
from _lib import note

W = "https://www5.tbmm.gov.tr/tutanaklar/TUTANAK/TBMM/"
ZC = "TBMM, *Zabıt Ceridesi* (Hansard)"
S1 = W + "d02/c027/tbmm02027001.pdf"   # 1 Nov 1926, birinci içtima
S2 = W + "d02/c027/tbmm02027002.pdf"   # 3 Nov 1926, ikinci içtima

note("Events", "The Assembly Congratulates the Gazi after the İzmir Plot, 1 and 3 November 1926",
     {"type": "event", "when": "1 and 3 November 1926",
      "tags": ["event", "verified", "turkish", "internal-mirror"]}, """
The Grand National Assembly opened its fourth session on 1 November 1926, five months after the İzmir
assassination plot. The opening speech is Kemal's own account of the plot; the motions tabled on
3 November are the chamber's answer. Read together they show an Assembly with no voice for the accused
and no language for the plot except loyalty.

- **Mustafa Kemal (1 November, printed p. 2).** *"Bu teşebbüsatın son tezahürü olarak meydana çıkan
  suikast hâdisesi, naçiz şahsımıza taallûku itibariyle değil, fakat Türk Milletinin merdane evsafına
  yaraşmayan ve Millet Vekâleti gibi yüksek bir mertebei itibarı vasıtai tecavüz kılmağı düşünecek
  kadar tereddi eden irticaî bir zihniyet göstermek itibariyle mucibi teessür olmuştur."* ("The
  assassination incident that appeared as the latest manifestation of this enterprise has been a
  cause of grief not because it concerned our humble person, but because it showed a reactionary
  mentality so degenerate as to think of violating the high dignity of the Assembly as a means of
  attack on the Turkish nation's manly qualities", tr.). The framing is the point: the target was not
  the man but the nation and the Assembly, so the plot becomes an attack on the constitutional order.
- **Refik Bey (Konya, 3 November, pp. 17–18).** *"Aziz Müncimiz ve büyük dahimiz Reisicumhur Gazi
  Mustafa Kemal Paşa Hazretlerinin hayatına müteveccih olarak tertip edilen mel'un suikastın akim
  kalmasından ve binnetice vatanın muhakkak bir felâketten kurtulmasından Milletçe duyulan nihayetsiz
  meserretleri bir defa daha izhar eden Meclisi Âlinin kalbi memnuniyet ve tebrikâtını Reisicumhur
  Hazretlerine iblağ etmek üzere..."* ("I propose ... to convey to the President the Assembly's
  heartfelt satisfaction and congratulations, which once more express the boundless joy felt by the
  nation at the failure of the cursed plot against the life of our dear saviour and great genius, the
  President Gazi Mustafa Kemal Pasha, and consequently at the homeland's deliverance from certain
  disaster", tr.). He went on: *"O hainler niçin Gazi'yi öldürmek istiyorlardı?"* ("Why did those
  traitors want to kill the Gazi?", tr.), and answered that it was because the Gazi had grasped the
  nation's highest existence with his genius and saved it. The Assembly elected the delegation of
  fifteen by lot the same day.
- **Süleyman Sırrı Bey (Bozok, 3 November, p. 18).** *"Gazi Paşa Hazretleri Çankaya'dadır. Kafile
  kafile gider, arzı tebrikât eyleriz."* ("The Gazi Pasha is at Çankaya. We can go in groups and
  convey our congratulations", tr.). A practical suggestion, and a measure of how close the chamber
  felt to him.
- **Tunalı Hilmi (Zonguldak, 3 November, p. 18).** *"Türk'ün tarihi bir sözü vardır: Ölümlerden ölüm
  beğen. Ben yerlerinde olsa idim idamı tercih ederdim. Yani terakkiperverler namı altında yaşamış
  olanlar Gazi'nin huzuruna çıkmak için bilmem bu ölümü tercih edebilirler mi?"* ("The Turk has a
  historic saying: of deaths, choose the best. If I were in their place I would prefer execution.
  That is, those who lived under the name of Progressives — I wonder whether they could prefer this
  death in order to appear before the Gazi?", tr.). The jab is at the banned Terakkiperver
  Cumhuriyet Fırkası, not at Kemal: the plot is used to settle an old party score.
- **Tunalı Hilmi again (1 November, pp. 2 and 5)**, during the speech itself, called out *"Yaşasın
  Cumhuriyet..."* (p. 2) and *"Yaşa Gazi..."* (p. 5); Refik Bey (Konya) called out *"Yaşa, büyük
  Gazi..."* and *"Yaşasın Gazi"* (p. 6). The interjections are printed in the minutes as part of the
  speech.

**Reading.** The open record after 1923 is the loyal record (Round 8). The İzmir plot does not break
that pattern: the only named opponents in the chamber are the already-banned Progressives, and the
only emotions recorded are grief for the Gazi and satisfaction at the trials. The fifteen-man
delegation, elected by lot, went to Çankaya; the minutes do not record what was said there. For the
dataset the card is a cluster of admiring and instrumental gazes, all contemporary, all Turkish, all
tier P. See [[Independence Tribunals]] and [[Nutuk]].

## Sources
- """ + ZC + """, Dönem 2, cilt 27, birinci içtima, 1 Teşrinisani 1926, printed pp. 2–6 (opening speech; plot passage p. 2; Tunalı Hilmi pp. 2 and 5; Refik Bey p. 6) · P — [PDF](""" + S1 + """)
- """ + ZC + """, Dönem 2, cilt 27, ikinci içtima, 3 Teşrinisani 1926, printed pp. 11–18 (motions and speeches pp. 17–18) · P — [PDF](""" + S2 + """)
- Page numbers are the printed folios at the foot of each PDF page (1 Nov: PDF p. 2 = printed p. 2; 3 Nov: PDF p. 7 = printed p. 17). The 1926 text layer is OCR-degraded; quotes are de-hyphenated and normalised. The raw forms behind them are *Müncilmi'Z* (Müncimiz), *Mileltinİn* (Milletinin), *mertelbei* (mertebei), *zihnayet* (zihniyet), *hiçin* (niçin), *Cumıhuriyet* (Cumhuriyet), *mıel'un* (mel'un), *hayâtına* (hayatına), *ıb'ir felalkeltitlen kürtulma'sından* (bir felâketten kurtulmasından; a heavier reconstruction, flagged), *Gazi' nirı* (Gazi'nin). The two Tunalı Hilmi interjections of 1 November are separate utterances at different points in the speech (p. 2 and p. 5), printed together here for brevity.
""")
