# -*- coding: utf-8 -*-
# Census round 7 (Oct 2026) — ORIGINAL Arabic periodicals and books, 1919-1938, read in open Internet Archive scans.
# Method: archive.org metadata API -> djvu text for locating -> PDF page images read by eye to confirm every Arabic quote.
# Page numbers are printed page numbers unless marked "pdf p.". Translations are the note author's own, marked as such.
from _lib import note, person

IA = "https://archive.org/details/"
TR = "*(English translation mine.)*"

# ---------------------------------------------------------------- Rida in al-Manar
note("Events", "Al-Manar 25(4), 1924 — Rida on Ankara's Disregard of the Muslim World", {
    "type": "event", "when": "1924",
    "tags": ["event", "verified", "periodical", "contemporary", "hostile", "arabic-primary"]}, """
The vault's [[Rashid Rida]] node rests on Brett Wilson's citation of *al-Manar* 25 (1924): 794. This card goes to the
journal itself (Internet Archive scan of vol. 25, [`Almanar`](https://archive.org/details/Almanar), file `almanar25.pdf`)
and adds the page where Rida writes about Mustafa Kemal by name.

**1. p. 794 — confirmed.** Part 10 of vol. 25, p. 794 (pdf p. 599), under the heading *"Translation of the Qur'an, the
distortion of a translation of it, and doubt cast on it"* (ترجمة القرآن وتحريف ترجمة له والتشكيك فيه). Rida opens: *"The most
important of the events that concern the Islamic world are three; the first is the Turkish Angora government's open
assistance for translating the noble Qur'an and publishing it in Turkish"*, and he says *"the idea of their heretics
(فكرة ملاحدتهم) turned to this work many years ago"* to turn the religious among them away with the Turkish translation,
*"so that it be easy for them to distort the translation and do with it as they like"* (وليسهل عليهم تحريف الترجمة والتصرف فيها
كيفما شاؤوا). Wilson's "their heretical idea" is a fair rendering of *fikrat mulāḥidatihim*. The word is *mulḥid*: heretic or atheist.
No Kemal by name on that page; the Wilson correction in the Rida node stands. {tr}

**2. Part 4, p. 285 — Rida's own verdict on the Kemalists.** Headed *"The abolition of the Caliphate and of the great Islamic
interests by the state"* (إلغاء الخلافة والمصالح الإسلامية الكبرى من الدولة, pdf p. 210). Rida sorts the abolition's defenders into
four parties. Of the second he writes that their whole defence is that the Turks of old wronged the Abbasid caliphate
as these wronged the Ottoman: *"and this is the opinion of Mustafa Kemal and his party, as is known from his speech
which he made the preface to this act"* (وهذا رأي مصطفى كمال وحزبه كما يعلم من خطبته التي جعلها مقدمة لهذا العمل), adding that
*"the motive of these people for these sayings is the whim of politics, which corrupts everything it enters"*. Then,
of the Kemalists as a body: *"for all this these Kemalists believe the Islamic world supports them in all they do,
whether from ignorance, or from desire and submission to the power of the strong ... indeed I say they have come not
to care about the Islamic world, whether it be pleased or angry, if its pleasure or anger does not influence the Turkish
people so as to make it oppose the government"* (بل أقول إنهم أصبحوا لا يبالون بالعالم الإسلامي رضي أم سخط). Of the fourth party,
who object knowing the law and the Muslims' general interest, he says that perhaps only a few names of them have reached the Angora government, for
few of them wrote in the papers, "and our articles in *al-Manar* alone have become a full volume". {tr}

**3. Part 4, pp. 289–291 — the same issue's anthology of Egyptian reaction.** Rida's section *"The opinion of the Egyptians
on the Turkish revolution"* (p. 289) says that many individuals and bodies cabled Mustafa Kemal Pasha, first praising
him as they had at the first blow, now calling him unbeliever and apostate; others wished him back to the faith; and that
the writers most vocal for the Turks were Shaykh Abd al-Aziz Shawish, Amin Bey al-Rafi'i and Muhammad Shakir. The sub-section
on Shawish is covered in [[Abd al-Aziz Shawish]]. Rida's own headings on p. 290 include *"Mustafa Kemal's covetousness of the
Caliphate"* (طمع مصطفى كمال بالخلافة) and, on p. 291, *"the Tatar sedition that corrupts the Turks' beliefs"* (فتنة التتار المفسدة لعقائد الترك; text not analysed here).

**Place in the deck.** The same pen as the [[Rashid Rida]] card, but here the target is Mustafa Kemal and his party by
name, in the first weeks after the [[Abolition of the Caliphate]]: Rida does not call Kemal an unbeliever; he calls the
regime indifferent to the Muslim world.

**Caveats.** Part 4's month is inferred from the part sequence of vol. 25 (it follows the March 1924 events and an
*al-Akhbar* article of 6 March); I did not read the part's own date line. The scan's OCR is poor on this typeface; every
Arabic quote above was read from the page images.

## Sources
- Rashid Rida, ed., *al-Manar* vol. 25, part 4, pp. 285, 289–291 (pdf pp. 210, 214–216) and part 10 p. 794 (pdf p. 599): [archive.org/details/Almanar](https://archive.org/details/Almanar), `almanar25.pdf` · tier P
- Brett Wilson, *IJMES* 41/3 (2009), epigraph and n. 2, for the p. 794 citation (S)
""".replace("{tr}", TR))

# ---------------------------------------------------------------- Shawish
person("Abd al-Aziz Shawish", role="Egyptian writer; contributor to the Cairo daily *al-Akhbar*, quoted at length in *al-Manar* 25(4), 1924",
  nat="Egyptian (⚠️ per the page: *al-Manar* names him among the Egyptians who wrote for the Turks)", life="",
  stance="conflicted — defends the Turks and honours Kemal's stature, blames him for abolishing the Caliphate",
  tags=["journalist", "egypt", "contemporary", "conflicted", "verified", "arabic-primary"], body="""
Rashid Rida's *al-Manar* printed, in its 1924 vol. 25 part 4 (pp. 289–291), a section headed *"The opinion of Shaykh Shawish on
Kemal, the Kemalists and the Unionists"* (رأي الشيخ شاويش في كمال والكماليين والاتحاديين). Rida introduces Shawish as the most
learned of the Egyptian pro-Turkish writers and says the shaykh's three *al-Akhbar* articles under the title
*"The Kemalist Bomb"* (القنبلة الكمالية) began in the issue of 3 Rajab 1342 / 6 March 1924, "describing the fame and Islamic
standing Mustafa Kemal Pasha had won". What the page then quotes ("then he said, verbatim") is a conflicted voice.

**What he saw.** A leader who might have stopped at a middle course: *"Mustafa Kemal could have been content, on the
caliphate question, with the middle way that stood in the days of the Caliph Abdülmecid — that settlement which barred the
Caliph from interfering in or contacting the political affairs of the Turkish state, and in which neither the Caliph nor the House
of Osman had done anything to call for changing it, let alone erasing it"* (لقد كان يمكن أن يكتفي مصطفى كمال في مسألة الخلافة
بالنحو الوسط الذي كان قائماً لعهد جلالة الخليفة عبد المجيد ... ما يدعو إلى تغييره بله محوه; *al-Manar* 25(4), p. 290). And a Kemal who had
wanted the title: *"One day the Ghazi aspired to be Caliph, as I learned when I came down to Angora; nothing stopped him
but his fear that an internal disturbance would threaten the kingdom before the peace was complete"* (لقد طمح الغازي ذات يوم أن
يكون الخليفة كما علمت عند هبوطي أنقرة ...; p. 290). Rida frames the passage with the heading *"Mustafa Kemal's covetousness of the
Caliphate"* and the remark that if Kemal had died or withdrawn after the peace conference "he would have held a station no leader in
history reaches" — an opinion Rida says many thinkers shared with the shaykh. {tr}

Compare [[Rashid Rida]] (the editor who quotes him, and who is harder on the Kemalists), [[Abdelhamid Ben Badis]] (the same
"we praised them until the Caliphate fell" arc, written two weeks later in Algeria) and [[Ahmad Shawqi]].

**Caveats.** Mediated by Rida's reprint: the three *al-Akhbar* articles themselves were not seen (Egyptian press, not located on open
scans). I could not tell which of the three articles p. 290 reproduces; the date on the gaze record is the year only. Rida's page 291
continues in a sharper register about Tatars and Unionists, and I have not attributed that part to Shawish.

## Sources
- *al-Manar* 25 (4), pp. 289–291 (pdf pp. 214–216): [archive.org/details/Almanar](https://archive.org/details/Almanar), `almanar25.pdf` · tier P (a primary periodical quoting a primary newspaper)
""".replace("{tr}", TR))

# ---------------------------------------------------------------- Shawqi
note("Events", "Shawqi's Two Poems on the Ghazi, 1922–1924 (al-Shawqiyyat)", {
    "type": "event", "when": "1922–1924",
    "tags": ["event", "verified", "poem", "contemporary", "conflicted", "arabic-primary"]}, """
The [[Ahmad Shawqi]] card gives the whiplash in a paragraph and no text. Here are the verses, from an open scan of
*al-Shawqiyyat* vol. 1 (the political, historical and social poems), Dar al-'Awda, Beirut, with Muhammad Husayn Haykal's preface from
the first edition and an editor's glosses ([`elshandawily1184`](https://archive.org/details/elshandawily1184), "al-Shawqiyyat j. 1").
Page numbers below are the printed ones.

**1. "The victory of the Turks in war and politics" (p. 59).** The poem opens with the line that gave the card its
phrase: *"Allahu akbar, how many wonders in the conquest — O Khalid of the Turks, renew Khalid of the Arabs!"*
(الله أكبر، كم في الفتح من عجب · يا خالد الترك جدد خالد العرب). The editor's note 1 on that page: "Khalid of the Turks: meant is the Ghazi
Mustafa Pasha Kemal; and Khalid of the Arabs is Khalid ibn al-Walid". Later lines praise him for sparing the monks and
the cross in war (*"your sword never committed a shameful act; the sanctity of monks and the cross was not violated"*) and
for answering peace with peace, and the poem turns to Lausanne, where *"a calamity came upon them from you"* (the editor identifies
the "calamity", *dāhiya*, as İsmet Pasha, the Turkish delegate, noting he was said to be hard of hearing). The reference to
Lausanne puts the text after the conference opened on 20 November 1922; the scan gives no date. {tr}

**2. "The Caliphate of Islam" (خلافة الإسلام, pp. 105–107).** It begins: *"The wedding songs came back as echoes of wailing,
and you were mourned amid the landmarks of joy"* (عادت أغاني العرس رجع نواح · ونُعيتِ بين معالم الأفراح; p. 105). On p. 106
the mourning spreads: *"Mosques and pulpits cried out for you; kingdoms wept and lamented ... Syria asks, and Iraq and Persia:
has an effacer effaced the Caliphate from the earth?"* (الشام تسأل والعراق وفارس · أمحا من الأرض الخلافة ماح؟). Then he turns on
the new Turkey: *"Prayer wept — and that is the mischief of a trifler with the law, rowdy in judgment, insolent"* (بكت الصلاة، وتلك فتنة عابث بالشرع، عربيد القضاء، وقاح), and
*"Shall I say that he who revived the community is an apostate, and that he who restored rights is a libertine?"*
(أأقول من أحيا الجماعة ملحد · وأقول من رد الحقوق إباحي؟; p. 107). The conflict is the whole poem: he refuses the word
*apostate* and still demands the Caliphate back. He ends with: *"Convey the advice to the Ghazi, that he may take it; the steed
returns after bolting. Pride has given the president its wine to drink; what will you do with one felled by drink?"*
(أدّوا إلى الغازي النصيحةَ يَنتصحْ · إن الجوادَ يثوبُ بعد جماح ؛ إن الغرورَ سقى الرئيسَ براحِه · كيف احتيالُك في صريع الراح؟; p. 107).
The editor's note 7 identifies "the Ghazi" as Mustafa Kemal "and also the 'president' of the second verse". {tr}

**What the two poems show.** The 1922 poet claims Kemal for the Arab-Islamic line of conquerors; the 1924 poet does not
retract, and does not curse: he asks the Ghazi to reconsider. The vault's one-line "effectively retracting the praise" is too hard;
the text refuses the charge of apostasy.

**Caveats.** (a) The scan gives no first-publication dates; the 1922 date comes from the poem's Lausanne reference and the card, the
1924 date from the abolition the poem mourns. (b) The editor's footnote on p. 105 dates the abolition "1923"; it was 3 March 1924,
so that note is the editor's error, not Shawqi's. (c) I read the verses from page images of pp. 59, 105–107; the OCR text is unreliable
for poetry. (d) the volume's introduction (reproduced in the scan) says the poet wrote more about the Turks and the Caliph than about the Arabs and the Prophet; not
quoted here.

## Sources
- Ahmad Shawqi, *al-Shawqiyyat*, vol. 1, Dar al-'Awda (Beirut), pp. 59, 105–107 (pdf pp. 60, 106–108): [archive.org/details/elshandawily1184](https://archive.org/details/elshandawily1184) · tier P (the poems themselves)
""".replace("{tr}", TR))

# ---------------------------------------------------------------- al-Fath
note("Events", "Al-Fath (Cairo), 1927–1938 — Khatib's Weekly on Ankara", {
    "type": "event", "when": "1927–1938",
    "tags": ["event", "verified", "periodical", "contemporary", "hostile", "arabic-primary"]}, """
*Al-Fath* ("The Conquest") was the Cairo weekly of the Salafi publicist Muhibb al-Din al-Khatib, an "Islamic, scholarly and moral
newspaper" (صحيفة إسلامية علمية أخلاقية, as its 1927 masthead says), that kept up a steady line against Kemalist Turkey. The Internet Archive holds it
in 100-issue batches ([`efath-moheb-elden-elkheeb`](https://archive.org/details/efath-moheb-elden-elkheeb)). Three
datable pieces, read from the page images:

**27 October 1927 — "Ankara and the Islamic religion" (no. 68, year 2, Thursday 2 Jumada I 1346; p. 280).** In a column headed *al-Tamhis*
("the sifting"), the paper answers the Liberal-Constitutionalist daily *al-Siyasa*, which that week had reprinted telegrams from
Ankara carrying Mustafa Kemal's speech "said to have lasted thirty-six hours" (presumably the Great Speech, *Nutuk*, of mid-October 1927; the identification is mine), and
notes that *al-Akhbar* had to run the headline *"Mustafa Kemal's disowning of Islam"* (براءة مصطفى كمال من الإسلام) over some of his
words. The paper's verdict on the Kemalists: *"The Kemalists in Ankara are liars in their claim of 'intellectual freedom'"*, and,
a few lines on: *"they wish their hands to be let loose in Egypt as well, so that they might make this nation taste, many
times over, the torment of consciences that has befallen the Turkish nation from their Kemalist masters"* (إنهم يتمنون أن تطلق
أيديهم في مصر أيضاً فيذيقوا هذه الأمة من تعذيب الضمائر أضعاف ما نزل بالأمة التركية من سادتهم الكماليين). {tr}

**Late March 1936 — Arabic expelled (p. 950, pdf p. 1395 of the 426–530 batch; issue of 1 Muharram 1355).** In an editorial on the
translation of the Qur'an, the paper sets Ankara beside Tehran: *"Atatürk expelled Arabic from the Turks' language in the worst of
expulsions, and last year the Shah of Persia followed him, purging his tongue of Arab words and the Arabic language"*
(فإن «أتاتورك» طرد العربية من لغة الأتراك شر طردة، وقفاه في العام الماضي شاه العجم). It cites an *al-Balagh* piece of 17 March 1936,
so the issue is the next one; I did not read the masthead of this issue, only the cover leaf, which shows "1 Muharram 1355". {tr}

**Late December 1938 — "Kemalist propaganda in Syria" (no. 634, 7 Dhu'l-Qa'da 1357 / c. 29 Dec 1938; pp. 827–830).** Part 2 of an unsigned travel series, *Four
Months in the Levant*. The piece describes what it calls the Kemalists' efforts to spread irreligious propaganda among Syrians and the failure of Syria's leaders to answer it. On the death: *"When Atatürk died, the preachers held the funeral prayer in absentia for him in the Umayyad
Mosque, and a *fitna* nearly arose because of it"* (ولما مات أتاتورك أقام الدعاة صلاة الغائب عليه في مسجد بني أمية وكادت تحدث بسبب ذلك فتنة;
p. 829), and: *"What adds to the pain is that the Syrian papers, all of them, performed the function of Kemalist propaganda on the
occasion of Kemal Atatürk's death, blackening long columns with embellishing his history and listing his 'reforms'"* (ومما يزيد في
الألم أن الصحف السورية بأجمعها قامت بوظيفة الدعاية الكمالية لمناسبة موت كمال أتاتورك فسودت الصحائف الطوال بتزويق تاريخه وتعداد (إصلاحاته);
p. 829). The same page names Dr. Abd al-Rahman Shahbandar's *al-Ayyam* article days before the death, and charges Ankara's government with the
Alexandretta affair. It is the hostile twin of the Great Umayyad Mosque scene in the vault's Damascus and Beirut cards, seen from Cairo, and the
counter-voice to [[Abdelhamid Ben Badis]]'s Constantine elegy printed in the same weeks. {tr}

**Caveats.** The *Four Months in the Levant* author is not named on the pages seen; the attribution is to the paper. Issue numbers
and dates were read from mastheads (1927: full; 1938: "634 ... 7 Dhu'l-Qa'da 1357") and the 1936 date is inferred. The 1927 *al-Akhbar* headline is reported
by *al-Fath*, not seen. *Al-Fath* has dozens more Kemal items in 1926–1938 (OCR hits: 80 in the 1926–28 batch alone); these three are the ones page-confirmed.

## Sources
- *al-Fath* no. 68, 27 Oct 1927, p. 280 (batch 1–125, pdf p. 1080); no. 634, c. 29 Dec 1938, pp. 827–830 (batch 631–730, pdf pp. 77–80); issue of 1 Muharram 1355 (c. 26 Mar 1936), p. 950 (batch 426–530, pdf p. 1395): [archive.org/details/efath-moheb-elden-elkheeb](https://archive.org/details/efath-moheb-elden-elkheeb) · tier P
""".replace("{tr}", TR))

# ---------------------------------------------------------------- al-Zayyat / al-Risala
person("Ahmad Hasan al-Zayyat", role="Editor and owner of the Cairo weekly *al-Risala* (the 14 Nov 1938 issue, no. 280, carries his front-page editorial)",
  nat="Egyptian", life="",
  stance="admiring, with a pointed reservation — Kemal a genius of a leader, but not a prophet of the Turks",
  tags=["editor", "egypt", "funeral", "admiring", "verified", "arabic-primary"], body="""
*Al-Risala* (1933–1953) was the Cairo weekly of Egyptian literary Arabism; its masthead on the Monday after Atatürk's death
(14 November 1938 / 22 Ramadan 1357, year 6, no. 280, [open scan](https://archive.org/details/AAlexandrina-230539)) carries Atatürk's
photograph and a front-page editorial *"The Ghazi Kemal Atatürk"* (الغازي كمال أتاتورك), pp. 1841–1842 by the contents page, signed by the
editor, Ahmad Hasan al-Zayyat. It is the Egyptian literary press's counterweight to [[Abdelhamid Ben Badis]] and to the *al-Fath* line.

**What he saw.** First the name: *"Perhaps 'Kemal Atatürk' is weaker than 'Mustafa Kemal' as a sign of a leader's state-building, of a
people's genius in one man, of a government reaching maturity in one chief, and of the history of a renaissance in one life! For 'Mustafa Kemal'
is the name on all of that, engraved in ears and minds by the guiding fates and the creative genius over twenty years"* (ربما كان
(كمال أتاتورك) أضعف من (مصطفى كمال) في الدلالة ... فإن (مصطفى كمال) اسم على كل أولئك نقشته في الآذان والأذهان الأقدار المصرّفة والعبقرية الخلاقة
في مدى عشرين سنة), "whereas 'Atatürk' is a title they gave the soaring eagle after it had folded its talons and tucked its wing" (p. 1841). Then the
man: *"Mustafa Kemal, God have mercy on him, was not a man of chance and luck whom an empty field raised to heroism and the stupidity of the
nation drove into leadership"* (لم يكن مصطفى كمال رحمه الله رجلاً من رجال المصادفة والحظ، يرفعه إلى البطولة خلو الميدان، ويدفعه إلى الزعامة غباء الأمة;
p. 1842), but one of the chosen few on whom God lays the guidance of a flock about to stray. He lists the farm boy, the rebel at school and in the
army, Çanakkale-to-Lausanne, the replacing of the Caliphate by the republic, the hat for the fez, the separation of the world from religion,
the new script, the equality of man and woman in right, and Turkey's entry into the League of Nations. And then he disputes a comparison: "They said: if Muhammad, in the human sense, is the
meaning of the Arabs, then Mustafa Kemal in that sense is the meaning of the Turks" — *"but they forgot that Muhammad's renaissance is steered by a Qur'an and
upheld by revelation, and that its hold on hearts comes from the mind's conviction, not from the severity of the sultan"* (وقد فاتهم أن نهضة محمد
يسددها قرآن ويسندها وحي، وأن نوطتها في القلوب آتية من اقتناع العقل لا من شدة السلطان). He ends by wondering whether the Turks will hold to their
road to the West now that the voice has fallen silent; the closing sentence (read from the OCR of p. 1842, not confirmed on the image) credits him with
"courage of heart, quickness of mind, originality of opinion, cleanness of hand and soundness of conscience" (شجاعة قلب وبراعة ذهن وأصالة رأي وطهارة يد وسلامة ضمير)
and prays God to cover him with His mercy. {tr}

**Caveats.** Funeral-era (14 Nov 1938), admiring. The editorial's Arabic is quoted from the page images (pdf pp. 768–769 of the open
scan); the end of p. 1841 (the photograph beside the opening) is low resolution, so I quote only the sentences read cleanly.

## Sources
- *al-Risala* no. 280, Monday 14 Nov 1938 (year 6), editorial pp. 1841–1842 (pdf pp. 768–769): [archive.org/details/AAlexandrina-230539](https://archive.org/details/AAlexandrina-230539) · tier P
""".replace("{tr}", TR))

# ---------------------------------------------------------------- Ben Badis primary
note("Events", "Al-Shihab, Nov 1938 — Ben Badis's 'Mustafa Kemal, Rahimahu Allah' in the Original", {
    "type": "event", "when": "1938-11",
    "tags": ["event", "verified", "periodical", "funeral", "arabic-primary"]}, """
The [[Abdelhamid Ben Badis]] node reports the November 1938 *al-Shihab* eulogy from summaries (Guenn, al-Sallabi) and says the facsimile
was not seen. It is in the Internet Archive: [`Alshehab-mag`](https://archive.org/details/Alshehab-mag), file `alchihab-09-14.pdf`
(45 pages). The part's masthead: *al-Shihab*, Constantine, part 9 of vol. 14, "Ramadan 1357 / November 1938"; the contents page
adds that the part came out on Friday 8 Dhu'l-Qa'da 1357 (30 December 1938), later than the cover month.
The article is titled **"مصطفى كمال رحمه الله"** and is **signed *Abd al-Hamid ibn Badis*** (pdf pp. 4–8; the last page prints "134"; the pages
carrying printed numbers are 131–134, so the article runs about pp. 130–134 of the volume).

What the vault's summaries say is confirmed in the Arabic text:
- Opening: *"On the seventeenth of the great month of Ramadan the breath of the greatest man humanity has known in modern
  history was stifled, and of one of the greatest geniuses of the East"* (في السابع عشر من رمضان المعظم خنقت أنفاس أعظم رجل عرفته البشرية في
  التاريخ الحديث، وعبقري من أعظم عباقرة الشرق). He calls him the hero of Gallipoli, the hero of the Sakarya, and "the reviver of Turkey from near-death".
- On Islam (p. 132, the last line, to p. 133): *"Mustafa Kemal rebelled, in truth, a headlong, sweeping rebellion — but he did not rebel
  against Islam; he rebelled against those who are called Muslims"* (ثار مصطفى كمال حقيقة ثورة جامحة جارفة ولكنه لم يثر على الإسلام وإنما ثار على هؤلاء الذين
  يسمون بالمسلمين). The "responsible" ones are the Caliph, whom he describes sitting in his palace under British guns, "silent, or rather moving
  in their hands as the machine moves", issuing the call to jihad against Kemal; the Shaykh al-Islam and ulema whose "decree" shed Kemal's blood; the
  Sufi shaykhs; and the Muslim peoples who had been the Sultan's and took up arms with his enemies. {tr}
- On the law (p. 133): *"So he abolished the false Caliphate, cut the hand of those 'ulama from rule, set aside the Mejelle and uprooted the tree of
  the Tariqa-s' zaqqum from its roots"* (فالغى الخلافة الزائفة وقطع يد أولئك العلماء عن الحكم فرفض مجلة الأحكام واقتلع شجرة زقوم الطرقية من جذورها), and: "yes, Mustafa Atatürk
  took the Shari'a rulings from the Turks; but he alone is not responsible for that" — they can take them back "when and as they like", and the
  Muslim countries living under Napoleon's code are asked what *their* ulama have said (p. 133–134).
- End (p. 134): *"God have mercy on Mustafa, may the scale of his good deeds weigh heavy"*; condolences to "the noble Turkish nation, in which we have
  grandsons and maternal uncles", and congratulations to the new president İsmet İnönü (see [[İsmet İnönü]]).

**Upgrade for the vault.** The 1938 record `ben-badis-1938` can now be marked primary (the text is his, signed) rather than reported by Guenn and al-Sallabi:
cite *al-Shihab* 14/9, pp. 131–134 (pdf pp. 5–8). The page is the same utterance, so no new gaze record. Two corrections to the existing
node: the part's cover month is November 1938 (Ramadan 1357), but the contents page puts publication on 30 December 1938; and the page range "pp. 1–5" of the
node is the part's own pagination.

The same part prints *"A star falls and a star rises"* (نجم يهوي ونجم يسطع, p. 135, a second tribute/ode addressed to "O Mustafa", read here only in
the OCR) and short biographies of Atatürk and İnönü (pp. 139, 142); not analysed.

## Sources
- *al-Shihab* 14/9 (Constantine, Nov 1938), "Mustafa Kemal rahimahu Allah", signed Abd al-Hamid ibn Badis: [archive.org/details/Alshehab-mag](https://archive.org/details/Alshehab-mag), `alchihab-09-14.pdf` pdf pp. 3–8 · tier P
""".replace("{tr}", TR))
