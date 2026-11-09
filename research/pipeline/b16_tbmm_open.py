# -*- coding: utf-8 -*-
# Census round 8 (Oct 2026) — the internal mirror, open-session minutes: TBMM Zabit Ceridesi (per-sitting PDFs,
# www5.tbmm.gov.tr/tutanaklar/TUTANAK/TBMM/dDD/cCCC/tbmmDDCCCSSS.pdf) plus the Round 7 unmined leads in the closed
# sessions (Gizli Celse Zabitlari, vols. 2 and 4). Page numbers are the printed folios; quotes are de-hyphenated at
# line breaks; English renderings are the project's own and marked "(tr.)".
from _lib import note, person

W = "https://www5.tbmm.gov.tr/tutanaklar/TUTANAK/TBMM/"
H = "https://acikerisim.tbmm.gov.tr/handle/11543/3271"
GC = "TBMM, *Gizli Celse Zabıtları* (revised edition, Ankara: TBMM, 2023) — open access"
BS2 = "https://acikerisim.tbmm.gov.tr/server/api/core/bitstreams/6d06856b-fd5d-4e7a-b7d6-f2d690b06a56/content"
BS4 = "https://acikerisim.tbmm.gov.tr/server/api/core/bitstreams/0dcc2bb5-59aa-4a20-9584-04ab9d3a2af8/content"
ZC = "TBMM, *Zabıt Ceridesi* (Hansard)"
PARENT = "[[TBMM Closed Sessions on the Commander-in-Chief, 1921–1922]]"

# ---------------------------------------------------------------- 1. Gazi and Marshal, 19 Sep 1921 (open)
note("Events", "Gazi and Marshal — The Assembly's Vote of 19 September 1921",
     {"type": "event", "when": "19 September 1921", "tags": ["event", "verified", "turkish", "internal-mirror"]}, """
Days after the battle of the Sakarya ended (the front's motion is dated 14/15 September), the Assembly sat in *open* session on 19 September 1921
(Dönem 1, cilt 12, 79th sitting, pp. 262–265) and voted Mustafa Kemal the rank of Marshal (*müşir*) and the title
**Gazi**. Three gazes:

- **[[Fevzi Çakmak]] and [[İsmet İnönü]]** (p. 263), from the West Front, jointly telegraphed a motion that credits the
  Commander-in-Chief with the victory at the battlefield itself: *"Bizzat muharebe meydanındaki tedabir ile
  muzafferiyetin âmil ve müessiri olmuş olan Başkumandan Mustafa Kemal Paşa Hazretlerine müşirlik rütbesi ve gazilik
  unvanı tevcihini teklif ve istirham ederiz."* ("we propose and request the rank of Marshal and the title of Gazi for
  Commander-in-Chief Mustafa Kemal Pasha, who by his measures on the field itself was the agent and cause of the
  victory", tr.). Both men signed; the dataset keeps one record for each.
- **İbrahim Süreyya (Saruhan) and 62 colleagues** (the agenda heading's count; the Reis speaks of "eighty-odd signatures") (p. 263) filed a bill (2/351) calling him *"vatanın halaskarı ve zaferi
  ahirin âmili"* ("saviour of the homeland and agent of the final victory", tr.) and asking for the honours as the nation's
  sign of thanks. The printed signature list includes Hüsrev, Yunus Nadi, Halil Hulki, Besim Atalay and Mustafa Durak. The law passed by show of hands, *"müttefikan"*.
- **Tunalı Hilmi (Bolu)** (p. 264), after Kemal's thanks ("the true addressee of your award is your army") greeted him with a
  line of verse, *"Bir gaza ettin ki hoşnudeyledin peygamberi"* ("you fought a *ghaza* that pleased the Prophet", tr.).
  See [[Tunalı Hilmi]].

**Reading.** All three are admiring and all three are *requests*: the honours were proposed from the bottom of the chain
(front commanders, then deputies), not given by Kemal's own motion. Within six weeks the same Assembly's closed sitting
was arguing over whether to extend the powers granted in August
([[TBMM Closed Session of 31 October 1921 — Renewing the Commander-in-Chief]]). See also [[Turkish War of Independence]].

## Sources
- """ + ZC + """, Dönem 1, cilt 12, 79. içtima, 19 Eylül 1337 [1921], printed pp. 263–264 (proposal text p. 263, Tunalı Hilmi p. 264) · P — [PDF](""" + W + """d01/c012/tbmm01012079.pdf)
- Page numbers are the printed folios at the foot of each PDF page (checked against the PDF page: p. 263 = PDF p. 11, p. 264 = PDF p. 12). Rumi 1337 = 1921 (the Ottoman fiscal-civil year had been re-aligned with the Gregorian count in 1917).
""")

# ---------------------------------------------------------------- 2. Aug 1921 addenda (closed)
note("Events", "TBMM Closed Sessions, August 1921 — Three More Voices",
     {"type": "event", "when": "5 and 8 August 1921", "tags": ["event", "verified", "turkish", "internal-mirror"]}, """
Addendum to """ + PARENT + """ (Round 7). The same 5 August 1921 closed sitting (vol. 2, 62nd in-ikat) and the 8 August
sitting that followed hold three more voices that the Round 7 card left unread. They are the Round 7 leads for
Tunalı Hilmi, Emin Bey and Hüsrev Bey.

- **Tunalı Hilmi (Bolu)** (5 Aug, pp. 192–193): *"Meclis namına Reis Paşa’nın, Başkumandan Paşa’nın alnından öperek ne
  tabirler varsa hepsini [az görürüm]"* ("on the Assembly's behalf, kissing the President Pasha, the Commander-in-Chief
  Pasha, on the forehead, whatever words there are I would find too little", tr.). The clause breaks at a page and an
  editor's footnote; "az görürüm" is on p. 193. The speech also invites the Pasha to exceed the Assembly's authority.
  See [[Tunalı Hilmi]].
- **Emin Bey (Eskişehir)** (5 Aug, p. 203) is the blunt one: *"Memleketi Yunandan, düşmandan kurtarıp ta böyle bir müddet
  için kendisi diktatör olarak icrayı faaliyet ederse, ben bunda memleket için fayda mülâhaza ederim."* ("if, having saved
  the country from the Greek and the enemy, he acts as dictator for such a period, I see benefit to the country in
  that", tr.); he adds that he would give him *"Padişahlıktan yüksek bir makam olsa dahî"* (even a post higher than the
  sultanate). Set beside [[Rıza Nur]]'s "we are in effect electing a sultan" in the same sitting, the two bracket the
  debate: one deputy objecting to the sultan-like grant, another volunteering it.
- **Hüsrev Bey (Trabzon)** (8 Aug, p. 214), reporting for the Defence Committee, relays that after the retreat *"Avrupalılar"*
  were circulating propaganda *"Mustafa Kemal Paşa’ya kimsenin itimadı kalmadığı"* (that no one trusted Mustafa Kemal any
  longer), and that *"Başkumandanlığın Paşa Hazretlerine tevcihi üzerine bu propagandaların yavaş yavaş kökü sarsılmakta
  olduğu anlaşılmıştır"* ("it has become clear that, with the Commander-in-Chief post assigned to the Pasha, the roots of
  this propaganda are being slowly shaken", tr.). It is a committee report in his voice, so the view is carried
  by him rather than invented for him.

All three are supportive. The edition's footnotes mark words the editor (M. Ünver) added in parentheses; none of the quoted
passages above is inside one.

## Sources
- """ + GC + """, vol. 2: 5 Ağustos 1337 [1921], 62. in-ikat, Tunalı Hilmi pp. 192–193, Emin Bey (Eskişehir) p. 203; 8 Ağustos 1337, 63. in-ikat, Hüsrev Bey p. 214 · P — [repository record](""" + H + """) · [vol. 2 PDF](""" + BS2 + """)
- Folios are the "– N –" markers printed at the foot of each page (PDF page = folio + 1).
""")

# ---------------------------------------------------------------- 3. 31 Oct 1921 renewal (closed)
note("Events", "TBMM Closed Session of 31 October 1921 — Renewing the Commander-in-Chief",
     {"type": "event", "when": "31 October 1921", "tags": ["event", "verified", "turkish", "internal-mirror"]}, """
The 5 August 1921 grant of the Commander-in-Chief's powers ran for three months, so on 29–31 October 1921 the Assembly sat
in closed session (vol. 2, pp. 470–480; the page headers read 101st sitting, 29 Oct, then 102nd, 31 Oct) to decide whether
to renew it for three more. Kırşehir's Müfid Efendi moved the extension; Mustafa Kemal was in the chamber and intervenes briefly (p. 480). The speeches are the fullest *person-versus-office* debate in the closed record outside [[Hüseyin Avni Ulaş]]'s
May 1922 quarrel, and a useful cross-section of Assembly opinion in the weeks after Sakarya. Each deputy's stated view of Kemal
(English renderings are the project's own, tr.):

**For continuing, without condition**
- **Müfid Efendi (Kırşehir)** (p. 474) presents the command as welcomed across the country: *"bütün Anadolu’da pek büyük, âli
  fikirlerle karşılanan bu Başkumandanla"*.
- **Cavid Bey (Kars)** (pp. 475–476) argues from the foreign signal: *"Yalnız Başkumandan Paşa, Başkumandanlıkta kalmalıdır."*
  ("only, the Commander-in-Chief Pasha must remain Commander-in-Chief", tr.), because the world knows why the Assembly gave him
  the post and the task is half done.
- **Hüsrev Bey (Trabzon)** (p. 476), speaking "as a soldier": *"Bir kere Mustafa Kemal Paşa’nın, bu şahsiyeti mübeccelenin büyük
  ve aynı zamanda mücerrep ve büyük bir kumandan olması bu vaziyeti doğurmuştur."* ("first, Mustafa Kemal Pasha's being this
  celebrated person, a great and tested commander, has produced this situation", tr.).
- **Tunalı Hilmi (Bolu)** (p. 477): *"Mümkün olsaydı, Allah’ım bana bir ikinci Mustafa Kemal Paşa verseydi."* ("if only it were
  possible, may God give me a second Mustafa Kemal Pasha", tr.).
- **Abdullah Azmi Efendi (Eskişehir)** (p. 479) dismisses the "he will be worn out" objection: *"Paşa Hazretleri bu davayı milli için
  kendisi, herhalde, fedayı nefisle ortaya atıldı."* ("the Pasha threw himself into the national cause in self-sacrifice", tr.).

**For continuing, but pointedly with accountability**
- **Hüseyin Avni Ulaş (Erzurum)** (pp. 474–475) admits the Pasha "has served and will serve" and should stay at the head longer,
  but: *"maddi ve manevi kuvvetin bir zâta tevdii bir millet için zaaftır"* ("the handing of material and moral force to one person
  is a weakness for a nation", tr.), and *"Paşa’yı yıpramayınız"* ("do not wear the Pasha out", tr.).
- **Mustafa Durak (Erzurum)** (p. 478): *"Başkumandan Paşa vazifesine devam etsin ve mesuliyetini müdrik bulunsun."* ("let the
  Commander-in-Chief Pasha continue his duty and be aware of his responsibility", tr.). His 5 August record is in the parent card.
- **Necip Bey (Ertuğrul)** (p. 478) splits trust from form: *"Paşa Hz. ne hepimizin itimadı vardır."* ("we all have confidence
  in the Pasha", tr.) but *"Bendeniz şeklin aleyhindeyim"*, against giving the Assembly's powers wholesale.
- **Lütfü Bey (Malatya)** (p. 479): *"Bunlardan dolayı tevellüd edecek mesuliyet münhasıran Paşa Hazretlerine aiddir."*
  ("responsibility arising from these things belongs solely to the Pasha", tr.), because the Assembly lent him its powers; he
  still concludes they cannot be withdrawn before the aim (driving the enemy "from Izmir into the sea") is reached.

**Reading.** Nobody in the speeches above argues against Kemal personally; the argument is whether concentrating the Assembly's
powers in one man was safe, and how to hold him answerable (other speakers of the same sitting are not covered here). See [[Turkish War of Independence]].

## Sources
- """ + GC + """, vol. 2: 29/31 Teşrinievvel 1337 [1921], 101st–102nd sitting, pp. 470–480 (Müfid p. 474; Hüseyin Avni pp. 474–475; Cavid pp. 475–476; Hüsrev p. 476; Tunalı Hilmi p. 477; Mustafa Durak and Necip p. 478; Abdullah Azmi and Lütfü p. 479) · P — [repository record](""" + H + """) · [vol. 2 PDF](""" + BS2 + """)
- Folios are the "– N –" markers printed at the foot of each page. Words in parentheses are the editor's additions where a footnote says so; none lies inside a quoted passage.
""")

# ---------------------------------------------------------------- 4. 29 Oct 1923 Republic (open)
note("Events", "Republic Day in the Assembly, 29 October 1923",
     {"type": "event", "when": "29 October 1923", "tags": ["event", "verified", "turkish", "internal-mirror"]}, """
On the evening of 29 October 1923 the Second Assembly (Dönem 2, cilt 3, 43rd sitting) amended the Constitution so that
*"Türkiye Devletinin şekli Hükümeti Cumhuriyettir"* ("the form of government of the Turkish State is a Republic", tr.; article 1,
carried with *"Yaşasın Cumhuriyet"* calls) and then elected the first President.

**The vote.** The sitting's president announced: *"Türkiye Cumhuriyeti için yapılan intihapta reye iştirak eden azanın adedi
158 dir. Yüz elli sekiz âza müttefikan Ankara Mebusu Gazi Mustafa Kemal Paşa Hazretlerini Cumhuriyet Riyasetine
intihabetmişlerdir."* (p. 99; "158 members took part … all 158 elected Ankara deputy Gazi Mustafa Kemal Pasha President of the
Republic", tr.) — the dataset's record for the Assembly as an institution. Kemal answered from the rostrum, thanking the Assembly and asking for its continued trust and support. Tunalı Hilmi interjects "Gazi arkadaşım…" ("my Gazi friend", tr.) as he starts.

**What the debate did not do.** Deputies argued two things: the presidential term (Emin Bey of Eskişehir wanted two
electoral periods and a President "outside party, as the father of the nation", *"fırka haricinde ve milletin babası"*, pp. 97–98) and
article 2 (Islam as the state religion, defended by Şeyh Safvet of Urfa, who read the Republic as a return to the Rightly Guided
Caliphs, and by another elderly member who called the new government God's own). The minutes show no speaker opposing Kemal's election
by name; Emin Bey's remark is about the office, not the man, so it is not recorded as a gaze.

## Sources
- """ + ZC + """, Dönem 2, cilt 3, 43. içtima, 29 Teşrinievvel 1339 [1923], printed pp. 98–100; vote announcement p. 99 (PDF p. 21) · P — [PDF](""" + W + """d02/c003/tbmm02003043.pdf)
- The text layer is two interleaved columns; the quotes above were checked against the column-separated text. Rumi 1339 = 1923.
""")

# ---------------------------------------------------------------- 5. Lausanne / caliph, March 1923 (closed)
note("Events", "TBMM Closed Session on Lausanne and the Caliph, March 1923",
     {"type": "event", "when": "5 March 1923", "tags": ["event", "verified", "turkish", "internal-mirror"]}, """
Four months after the sultanate was abolished (see [[Abolition of the Sultanate]]) and with the Lausanne talks stalled, the
Assembly debated in closed session (vol. 4, 4th–5th sitting, 4–5 March 1923) whether to dismiss the cabinet, with a motion that
puts the Pasha-or-Caliph question in so many words. **Mustafa Bey (Karahisar-ı Şarki)** moved a three-article motion (pp. 168–170):
- It calls Kemal and the Assembly's founders the saviours: *"Gazi âli şânımız ve sebebi necatımız Mustafa Kemal Paşa Hazretleri"*
  ("our exalted Gazi and the reason of our salvation, Mustafa Kemal Pasha", tr., p. 169).
- But it names the quarrel plainly: *"Reisi Hükûmet Gazi Mustafa Kemal Paşa Hazretleri mi, yoksa Halife Abdülmecit Hazretleri
  midir?"* ("is it Head of Government Gazi Mustafa Kemal Pasha, or Caliph Abdülmecid?", tr., p. 169), and demands a 20-man
  committee to merge constitutions, an end to "groupism", and the cabinet's immediate fall.

He does not appear to propose removing Kemal; the gaze is conflicted: gratitude to the leader, anxiety about a two-headed state,
and an appeal to the Assembly's old unity. See [[Abolition of the Caliphate]] and [[Abdulmejid II]].

**Hüseyin Avni, same sitting.** On 4 March (vol. 4, pp. 114–116) [[Hüseyin Avni Ulaş]] urges a "Başkumandan Paşa" to go back to the army and leave
politics; the text is ambiguous whether this addresses Kemal or İsmet, and it is therefore left out of the dataset (Round 7 had
reached the same view). Another line in the same speech ("they say there are two parties in the Assembly, one on Mustafa Kemal's
side, his sycophants…") reports European rumour and is not his view.

## Sources
- """ + GC + """, vol. 4: 5 Mart 1339 [1923], 5th sitting, 4th session, pp. 168–170 (Mustafa Bey's motion, p. 169 for the quoted passages); 4 Mart 1339, 4th sitting, pp. 113–116 · P — [repository record](""" + H + """) · [vol. 4 PDF](""" + BS4 + """)
- The deputy is "Karahisarışarki Mebusu Mustafa", p. 170; there are several deputies called Mustafa in the volume, so identify by constituency.
""")

# ---------------------------------------------------------------- 6. Surname 24 Nov 1934 (open)
note("Events", "The Name Atatürk in the Assembly, 24 November 1934",
     {"type": "event", "when": "24 November 1934", "tags": ["event", "verified", "turkish", "internal-mirror"]}, """
The Surname Law (see [[Surname Law]]) had passed earlier in 1934; on 24 November 1934 the Assembly (Dönem 4, cilt 25, 7th sitting,
p. 35) handed the President the name itself. The bill read: *"Kemal Öz adlı Cumhur reisimize Atatürk soy adı verilmiştir."*
("the surname Atatürk is given to our President named Kemal Öz", tr.) — the bill names him "Kemal Öz".

- **Prime Minister [[İsmet İnönü]]** introduced it, saying the Assembly had a debt and a right to choose the name of the "Great Leader":
  *"İnanıyoruz ki (Atatürk) adı ile Büyük Türk ulusu en büyük oğluna en büyük, en saygılı hitabını yapmış olacaktır."* ("we believe
  that with the name Atatürk the great Turkish nation will have made its greatest, most respectful address to its greatest son",
  tr.). There was no debate: the Reis asked for speakers on the whole, heard none, and the bill passed *"ittifakla"*.
- **The Interior Committee (Dahiliye Encümeni)** had met the same day and reported: *"Türk ulusuna tam istiklâlini kazandıran ve
  ulusa gerçek tarihinin ve öz dilinin yolunu gösteren Ulu Cumhur Reisimize (Atatürk) soy adının verilmesi çok yerinde
  görülmüş"* ("finding it most fitting that the surname Atatürk be given to our great President, who gave the Turkish nation its
  full independence and showed it its true history and its own language", tr.).

**Note.** The name has been legally protected since Law no. 5816 (1951; see the candidates file for its origins);
this note reproduces only the 1934 minutes. The minutes show a one-minute exchange, which is itself the evidence: by 1934 the
Assembly did not debate Kemal, it performed him (the contrast with 1921 is the point of [[TBMM Closed Session of 31 October 1921 — Renewing the Commander-in-Chief]]).

## Sources
- """ + ZC + """, Dönem 4, cilt 25, 7. inikat, 24 Teşrinisani 1934, printed p. 35 (inferred from neighbouring folios 34 and 36; the digits are lost in the scan's OCR) · P — [PDF](""" + W + """d04/c025/tbmm04025007.pdf)
""")

# ---------------------------------------------------------------- 7. 11 Nov 1938 (open)
note("Events", "The Assembly Meets Without Atatürk, 11 November 1938",
     {"type": "event", "when": "11 November 1938", "tags": ["event", "verified", "turkish", "internal-mirror", "obituary-corpus"]}, """
Atatürk died on Thursday 10 November 1938 at 9:05. On Friday 11 November the Assembly (Dönem 5, cilt 27, 3rd sitting, pp. 16–18)
met twice: first to hear the news and stand in silence, then to elect his successor and swear him in. Three voices, all in the minutes:

- **Assembly President Abdülhalik Renda** called him *"Büyük Halaskarımız"* ("our great Liberator", tr.): *"Büyük Halaskarımızın ölümünden
  hepimizin ve bütün milletin duyduğu elemin ne kadar büyük ve derin olduğunu dündenberi gerek kendimizde ve gerek millette
  gördüğümüz büyük acılarla anlıyoruz"* ("we have understood how great and deep the grief felt by all of us and the whole nation
  is, from the great pains we see in ourselves and in the nation since yesterday", tr.), proposed to postpone speeches, and asked
  the members to stand for **five minutes** of silence (*"ayakta, beş dakika sükût"*); the minutes record "sobs and weeping".
- **Prime Minister Celâl Bayar**'s notice reports the death 'with irreparable pain and grief': *"terki hayat ettiklerini onulmaz
  acı ve teessürlerle arzederim."* (p. 16), accompanied by the doctors' report.
- **[[İsmet İnönü]]**, elected President by 348 votes *"müttefikan"* (unanimously), said in his address: *"fevkalâde hizmetlerini bu günkü Türk
  Devletinin bünyesinde tam ve temiz eserler olarak tecessüm etmiş görüyoruz"* ("we see his extraordinary services embodied as complete
  and clean works in the structure of today's Turkish State", tr., p. 17) and that *(Kemal Atatürk)* would live on in the nation's heart.

The five minutes of standing silence is a data point for the "5-minute → 2-minute" lead in the candidates file: the Assembly stood
five minutes on the first day, before any program for 10 November existed. See [[Death and State Funeral of Atatürk]] and [[10 Kasım]].

## Sources
- """ + ZC + """, Dönem 5, cilt 27, 3. inikat, 11 Teşrinisani 1938, printed pp. 16–17 (PDF pp. 2–3) · P — [PDF](""" + W + """d05/c027/tbmm05027003.pdf)
""")

# ---------------------------------------------------------------- person: Tunalı Hilmi
person("Tunalı Hilmi", role="Bolu deputy (1921–23) and Zonguldak deputy (1923–), First and Second Grand National Assemblies", nat="Turkish", life="dates not established in these sources",
  stance="reliably admiring of the Commander-in-Chief in 1921; in 1924 insisted the caliphate was not 'abolished'", tags=["turkish", "contemporary", "admiring", "conflicted", "verified"], body="""
Speaks in the minutes under "Tunalı Hilmi Bey", for Bolu in the First Assembly and for Zonguldak in the Second. Four of his lines on
Mustafa Kemal survive in the minutes read in this round:

- **5 August 1921** (closed, vol. 2, pp. 192–193): he would kiss the Pasha on the forehead and finds all praise too little
  (*"…alnından öperek ne tabirler varsa hepsini [az görürüm]"*).
- **19 September 1921** (open, cilt 12, p. 264): greets the new Gazi with *"Bir gaza ettin ki hoşnudeyledin peygamberi"*.
- **31 October 1921** (closed, vol. 2, p. 477): *"Mümkün olsaydı, Allah’ım bana bir ikinci Mustafa Kemal Paşa verseydi."*
- **3 March 1924** (open, Dönem 2, cilt 7, 2nd sitting, PDF pp. 19–20): in the caliphate-abolition debate he refuses the word
  *ilga* (abolition): *"Hilâfet ilga edilmiyor. Hilâfetin makamı kaldırılıyor."* ("the caliphate is not abolished; the caliphate's
  office is being removed", tr.), adding that the caliphate and the imamate are "here" (in the Assembly). The line is not a statement about Kemal and is not in the dataset.

A reader who knew only the 1921 lines would take him for a hagiographer; the 1924 speech shows a deputy who could back the
leader and still object, in the same breath, to the leader's reform. See [[Gazi and Marshal — The Assembly's Vote of 19 September 1921]] and
[[TBMM Closed Session of 31 October 1921 — Renewing the Commander-in-Chief]].

## Sources
- """ + GC + """, vol. 2, pp. 192–193 and 477 · P — [vol. 2 PDF](""" + BS2 + """)
- """ + ZC + """, Dönem 1, cilt 12, 79th sitting, p. 264 · P — [PDF](""" + W + """d01/c012/tbmm01012079.pdf)
- """ + ZC + """, Dönem 2, cilt 7, 2nd sitting (3 Mart 1340 [1924]) · P — [PDF](""" + W + """d02/c007/tbmm02007002.pdf)
""")

print("census r8 tbmm_open: 7 events, 1 person")
