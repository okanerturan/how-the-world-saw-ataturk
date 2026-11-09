# -*- coding: utf-8 -*-
# Census round 17 (Nov 2026) — rivals: Ottoman and Turkish figures who opposed, rivalled or broke with Mustafa Kemal.
# Seam: archive.org open djvu texts located with tools/fts.py: Yamauchi's edition of Enver Pasha's letters (Bağlam 1995),
# Murat Bardakçı, Şahbaba (printing Vahdettin's dictated memoir of 1925 and Şerif Paşa's notes), Gültekin's 2025 doctoral thesis on
# Necip Fazıl, Refik Halid Karay's Minelbab İlelmihrab (İnkılâp 2009 ed.), and a DergiPark article quoting Ali Kemal's Peyam-ı Sabah.
# Quotes are checked against the text banked in tools/.state/round17/*.txt (hyphenation at line ends removed).
import json, os, re
from _lib import note, person

HERE = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(HERE, "tools", ".state", "round17")
NODE = "Rivals, Exiles and Islamist Critics on Mustafa Kemal in Their Own Words, 1920–1967"

def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"').replace("—", "-")
    s = re.sub(r"memr-\s*\n\s*lekette", "memlekette", s)
    s = re.sub(r"-\s*\n\s*", "", s)
    s = re.sub(r"\s+", " ", s).lower()
    return s

def bank(n):
    return norm(open(os.path.join(STATE, n), encoding="utf-8").read())

R = [
 dict(id="enver-pasha-1921-05", voice="Enver Pasha", role="Former Ottoman War Minister, in Moscow; letter to Mustafa Kemal", c="Soviet Russia", cn="Russia",
      dom="politics", date="1921-05", era="contemporary", mirror=None, pol="conflicted", inten=2,
      saw="Writes to Kemal as a brother, praising his ability but begging him not to turn his success into the rule of one person.",
      q="Şimdi muvaffakiyetinize bakarak, size iğvâ edenlere uyup memlekette bir şahsın veyâ yalnız bir kısmının tahakkümüne doğru gitmeyiniz.",
      art="quote", ev="P", med=None, src="yamauchi_enver.txt",
      cav="Turkish original (Ottoman-style transliteration by Yamauchi); the vault's translation: 'Now that you are succeeding, do not follow those who lead you astray towards the domination of the country by one person or one group.' Letter No. 97, undated (May 1921), Moscow to Ankara, printed in Yamauchi's documents section; OCR page markers 205-207 bracket the letter, the sentence falls just after the marker 207 (cited as pp. 205-208). Enver's archive reference given by Yamauchi: Klasör 7/Mustafa Kemal Dosyası. Immediately before, Enver writes that he had valued Kemal's ability since his own War Ministry ('İktidârınızı ... takdir ettim'). The letter also reports his claim that Kemal's circle had made him the dictator of an 'Ankara Communist Party'. Enver's own account of his conduct, written to a man he saw as a rival.",
      urls=["https://archive.org/details/masayuki-yamauchi-hosnut-olamams-adam-enver-pasa-0-baglam-libgen.li-1"],
      loc="Yamauchi, Hoşnut Olamamış Adam — Enver Paşa: Türkiye'den Türkistan'a (Bağlam, 1995), letter No. 97, pp. 205-208", link="Enver Pasha",
      nxt="Check against the Arı İnan / Aydemir editions of the same letter"),
 dict(id="enver-pasha-1921-07-17", voice="Enver Pasha", role="Former Ottoman War Minister, in Moscow; letter to Mustafa Kemal", c="Soviet Russia", cn="Russia",
      dom="politics", date="1921-07-17", era="contemporary", mirror=None, pol="hostile", inten=2,
      saw="Answers an article in Hâkimiyet-i Milliye by charging Kemal with treating him and his friends as obstacles to personal ambition and lying about them.",
      q="Şimdi muvaffakiyet belirince tabi'i maksadınızı gösterdiniz. Beni ve arkadaşlarımı şahsi emellerinize engel sayıyorsunuz.",
      art="quote", ev="P", med=None, src="yamauchi_enver.txt",
      cav="Turkish original; vault translation: 'Now that success is in sight you have naturally shown your aim. You regard me and my friends as obstacles to your personal ambitions.' Letter No. 118, Enver (Moscow) to Mustafa Kemal (Ankara), 17 July 1921, sent after Enver read Hâkimiyet-i Milliye's article against him in the Istanbul papers (Yamauchi's archive ref: Klasör 7/Mustafa Kemal Dosyası). It ends: 'I regret to see that the personal character I have known since Tripoli has not changed in the position you have reached ... I pity you, beaten by your personal ambition and made so small.' Pages: OCR marker 233 falls inside the letter (cited as pp. 233-234).",
      urls=["https://archive.org/details/masayuki-yamauchi-hosnut-olamams-adam-enver-pasa-0-baglam-libgen.li-1"],
      loc="Yamauchi, Hoşnut Olamamış Adam (Bağlam, 1995), letter No. 118, pp. 233-234", link="Enver Pasha",
      nxt="Hâkimiyet-i Milliye article of early July 1921 (the target of the letter)"),
 dict(id="enver-pasha-1921-07-22", voice="Enver Pasha", role="Former Ottoman War Minister, in Moscow; letter to Cemal Pasha in Kabul", c="Soviet Russia", cn="Russia",
      dom="politics", date="1921-07-22", era="contemporary", mirror=None, pol="conflicted", inten=1,
      saw="Tells Cemal that in Anatolia Mustafa Kemal personally regards him as a rival, yet he claims no movement against Kemal.",
      q="Anadolu'da Mustafa Kemal Paşa şahsen beni rakib telâkki",
      art="quote", ev="P", med=None, src="yamauchi_enver.txt",
      cav="Turkish original; vault translation: 'in Anatolia Mustafa Kemal Pasha personally regards me as a rival'. Letter No. 120, Enver to Cemal Pasha (Kabul), 22 July 1921; the same letter says Kemal had a Hâkimiyet-i Milliye article written 'aimed only at me' and that 'we have no movement against Mustafa Kemal Pasha, on the contrary we try to calm the negative friends'. Written to an ally, not to Kemal; cited as pp. 234-235 (OCR marker 235 follows the sentence).",
      urls=["https://archive.org/details/masayuki-yamauchi-hosnut-olamams-adam-enver-pasa-0-baglam-libgen.li-1"],
      loc="Yamauchi, Hoşnut Olamamış Adam (Bağlam, 1995), letter No. 120, pp. 234-235", link="Enver Pasha", nxt=None),
 dict(id="vahideddin-1921-03-23", voice="Mehmed VI Vahideddin", role="Last Ottoman Sultan; talking to the British High Commissioner Rumbold", c="Ottoman Empire", cn="Turkey",
      dom="politics", date="1921-03-23", era="contemporary", mirror=None, pol="hostile", inten=2,
      saw="Tells Rumbold that Kemal is a revolutionary, whom twenty years in London would turn back to his old self.",
      q="Londra'da yirmi veya otuz sene oturtsanız ve sonra 24 saatliğine dağın tepesine götürseniz derhal eski halini alır",
      art="quote", ev="S", med="Rumbold to Curzon, 23 Mar 1921 (Şimşir, İngiliz Belgelerinde...) ← Bardakçı 1998/2006", src="bardakci_sahbaba.txt",
      cav="Bardakçı's Turkish rendering of Vahideddin's words as reported in Sir Horace Rumbold's English dispatch; the sentence is a back-translation, not the Sultan's own Turkish. Vahideddin also said Kemal 'is a revolutionary' and that Bekir Sami was 'a Circassian, all the same', and that a forced caliph would be 'an instrument in the hands of wolves who like foggy weather' (same page). The date 23 March 1921 is taken from Bardakçı's chapter note for this chapter ('a two-and-a-half-hour private interview'), which the OCR does not attach by number to this passage; treat the day as inferred, the year as safe. Cited from the 2006 İnkılâp edition, p. 215 (OCR folio).",
      urls=["https://archive.org/details/sahbaba-murat-bardakci"],
      loc="Bardakçı, Şahbaba (İnkılâp, 2006; first ed. Pan 1998), p. 215", link="Mehmed VI Vahideddin",
      nxt="Şimşir, İngiliz Belgelerinde Atatürk vol. III for the English original"),
 dict(id="vahideddin-1924-03-11", voice="Mehmed VI Vahideddin", role="Last Ottoman Sultan, in exile at San Remo; letter to the head of the Egyptian ulema", c="Italy", cn="Italy",
      dom="religion", date="1924-03-11", era="contemporary", mirror="apostate", pol="hostile", inten=2,
      saw="After the abolition of the caliphate, says Kemal and his comrades won against the Greeks by Muslim love, then turned on the sharia.",
      q="Mustafa Kemal ve hempaları Müslümanlar'ın sevgisi, Osmanlılar'ın şehameti ve Allah'ın inayetiyle Yunanlılara galip geldi",
      art="quote", ev="S", med="Vahideddin letter of 11 Mar 1924 ← Bardakçı 2006", src="bardakci_sahbaba.txt",
      cav="Turkish rendering by Bardakçı of a letter (presumably Arabic) to Sheikh Muhammad Farraj al-Minyawi, head of the Egyptian Ulema Union. The sentence goes on (marked '(...ama)'): 'but they at once turned against the sharia that was its source'. The following lines, partly garbled in the OCR, list the veil lifted, women in bars and cafés, Muslim-Christian marriage allowed, polygamy abolished, hajj made 'a pretext', and that Kemal 'humiliated the caliphate and the House of Osman'. Vahideddin's own list of grievances; the vault does not endorse it. Cited p. 377 (OCR folio).",
      urls=["https://archive.org/details/sahbaba-murat-bardakci"],
      loc="Bardakçı, Şahbaba (İnkılâp, 2006), p. 377", link="Mehmed VI Vahideddin",
      nxt="The Egyptian press publication of the letter (Mar 1924)"),
 dict(id="vahideddin-1924", voice="Mehmed VI Vahideddin", role="Last Ottoman Sultan, in exile at San Remo; notes taken by Şerif Paşa", c="Italy", cn="Italy",
      dom="politics", date="1924", era="contemporary", mirror=None, pol="hostile", inten=2,
      saw="Says Kemal was sent to Anatolia by the palace and openly rebelled; neither Damad Ferid nor Tevfik Pasha could bring him to heel.",
      q="Bildiğiniz gibi Mustafa Kemal Paşa'yı Anadolu'ya biz gönderdik ve o açık bir şekilde bize isyan etti.",
      art="memoir", ev="S", med="Şerif Paşa's French notes of talks with Vahideddin (1924-25) ← Bardakçı 2006, Belge 2", src="bardakci_sahbaba.txt",
      cav="Belge 2 in Bardakçı's documents section: Turkish translation of parts of Şerif Paşa's French record of private conversations at San Remo, 1924-25; the year is the range's start. The same notes list Kemal's 'different roles' (hiding behind the defence of the country to keep leading the movement, running propaganda against the palace, accusing it of taking foreign money) and call the accusations 'lies'. Bardakçı also quotes the sentence in the body (p. 215) in slightly different words as from 'his memoirs'. Not the Sultan's own text but a courtier's record; the book's own page for Belge 2 is not legible in the OCR.",
      urls=["https://archive.org/details/sahbaba-murat-bardakci"],
      loc="Bardakçı, Şahbaba (İnkılâp, 2006), Belgeler, Belge 2 (Şerif Paşa's notes); body quotation p. 215", link="Mehmed VI Vahideddin",
      nxt="Şerif Paşa's French original"),
 dict(id="vahideddin-1925", voice="Mehmed VI Vahideddin", role="Last Ottoman Sultan, in exile at San Remo; memoir dictated to his chief aide Avni Paşa", c="Italy", cn="Italy",
      dom="politics", date="1925", era="contemporary", mirror=None, pol="hostile", inten=2,
      saw="In his dictated memoir recalls that when Kemal's attacks on him and his dynasty appeared in the papers, his time to decide had come.",
      q="Ertesi gün Mustafa Kemal'in şahsımız ve hanedanımız aleyhinde tefevvühâtını gazetelerde görünce, benim de karar verecek zamanım geldi.",
      art="memoir", ev="S", med="Bardakçı 2006, Belge 1 (facsimile in the Sultan's and Avni Paşa's hand)", src="bardakci_sahbaba.txt",
      cav="Turkish original (Ottoman style). Belge 1, 'Sultan Vahideddin'in Hatıraları (1925)', dictated at San Remo to Avni Paşa and left unfinished; the first four paragraphs are the Sultan's own hand, the rest Avni's. Bardakçı removed some phrases (marked with dots), for example the sentence on Kemal as the aide he sent to Anatolia ('...Mustafa Kemal'in ..... karşısında kalmıştım'). The passage describes the day after a meeting in which a visitor offered him a reduced caliphate if he would recognise Ankara; the sequence places it shortly before his departure in November 1922 (the OCR is garbled there). The page number of Belge 1 is not legible in the OCR.",
      urls=["https://archive.org/details/sahbaba-murat-bardakci"],
      loc="Bardakçı, Şahbaba (İnkılâp, 2006), Belgeler, Belge 1", link="Mehmed VI Vahideddin",
      nxt="Topkapı / family copy of the manuscript"),
 dict(id="ali-kemal-1920-05-06", voice="Ali Kemal", role="Journalist, editor of Peyam-ı Sabah, former Interior Minister", c="Ottoman Empire", cn="Turkey",
      dom="press", date="1920-05-06", era="contemporary", mirror=None, pol="hostile", inten=2,
      saw="Calls Kemal a false partisan who dresses in hypocrisy, has declared a crescent-against-the-cross jihad and deceives the naive believers.",
      q="sahte bir taraftar, bir riya kisvesine bürünerek, haça karşı hilal cihadını açmış, ehli imanın safdillerini aldatan",
      art="editorial", ev="S", med="Çakmak 2019, p. 416 ← Peyam-ı Sabah, 6 May 1920", src="cakmak_alikemal.txt",
      cav="Turkish original as quoted by Fevzi Çakmak (historian, not the marshal), 'Milli Mücadele Dönemi Türk Mizahında Muhalif Bir Kimlik: Ali Kemal', Tarih İncelemeleri Dergisi 34/2 (2019), 413-441, DOI 10.18513/egetid.661569, citing note 15 'Peyam-ı Sabah, 6 Mayıs 1920'. Vault translation: 'a false partisan, who, wrapped in the cloak of hypocrisy, has opened a crescent jihad against the cross, deceiving the simple-hearted of the faithful'. Çakmak places the phrase in his own sentence about Kemal in Havza, so it is a quotation of the editorial, not a full text of it. The same article says Ali Kemal called the Ankara deputies 'small fellows' (23 Apr 1920) and named Kemal among the 'bloody and cruel' members of the Union and Progress circle (7 May 1920). Ali Kemal was lynched on 6 Nov 1922.",
      urls=["https://dergipark.org.tr/tr/download/article-file/892240"],
      loc="Çakmak, Tarih İncelemeleri Dergisi 34/2 (2019), p. 416, n. 15", link="Ali Kemal",
      nxt="Peyam-ı Sabah, 6 May 1920 (İSAM archive holds the 'Mustafa Kemal'in Musahharalıkları' pieces)"),
 dict(id="necip-fazil-1943-11-19", voice="Necip Fazıl Kısakürek", role="Poet, editor of Büyük Doğu, later the best-known Islamist-conservative critic of Kemalism", c="Turkey", cn="Turkey",
      dom="letters", date="1943-11-19", era="posthumous", mirror=None, pol="admiring", inten=2,
      saw="Imagines Atatürk rising from his tomb in the Ethnographic Museum, in marshal's uniform, to lead the nation when the world is reckoned up.",
      q="Bir gün Atatürk dirilecektir!!!",
      art="article", ev="S", med="Gültekin 2025, p. 52 ← Büyük Doğu, 1st series, no. 10, 19 Nov 1943, p. 2 ('Atatürk Dirilecektir!')", src="gultekin_necip.txt",
      cav="Turkish original, as printed in Deniz Gültekin's 2025 Istanbul University doctoral thesis 'Necip Fazıl Kısakürek'in Perspektifinden Atatürk ve Cumhuriyet Devrimlerinin Yansımaları' (p. 52, footnote 122). In the war year the article is wholly admiring: 'On that day the person at our head ... will be none other than Atatürk'. Gültekin notes the contrast with Necip Fazıl's later, opposition phase in the second series of Büyük Doğu (from 1948), when he serialised Rıza Nur's Hayat ve Hatıratım. Stored as the 1943 face of a voice usually counted hostile; the 1967 record is the other.",
      urls=["https://archive.org/details/yakintarihhh2"],
      loc="Gültekin, İstanbul Üniversitesi doktora tezi (2025), p. 52, n. 122", link="Necip Fazıl Kısakürek",
      nxt="Büyük Doğu no. 10 (1943) scan"),
 dict(id="necip-fazil-1967", voice="Necip Fazıl Kısakürek", role="Poet and Islamist-conservative critic; defendant in the 1967 B.D. Fikir Kulübü case", c="Turkey", cn="Turkey",
      dom="letters", date="1967", era="posthumous", mirror=None, pol="conflicted", inten=2,
      saw="In court denies that his 'false heroes' lecture meant Atatürk, calling the charge as strained as reading a hint into the colour black.",
      q="Atatürk'ü sahte kahraman olarak gösterdiğimiz iddiası, siyah renkten bahseden bir adamın, Atatürk İstiklal Savaşında siyah astragan kalpak giydi",
      art="speech", ev="S", med="Gültekin 2025, pp. 349-350 ← Necip Fazıl, B.D. Fikir Kulübü Davası ve Müdafaalarım", src="gultekin_necip.txt",
      cav="Turkish original; the quotation ends mid-sentence at the edge of a footnote break (the sentence continues: 'diye ille onu ima ettiğimizi öne sürmekten veya beyaz kumaşı anlatırken kefen bezini telmih ettiğimize kadar hayal makinesini işlemekten daha tuhaftır!'). The thesis says the lecture 'Tarihimizde Sahte Kahramanlar' named Mustafa Reşid and Midhat Pasha as false heroes, and that the prosecution read it as a veiled attack on Atatürk, a charge under Law 5816; the thesis author's own view is that the denial was made to escape the penalty, which is his reading, not Necip Fazıl's. The vault records only that the defendant denied the target. No direct statement of view of Atatürk by Necip Fazıl in this period is quoted.",
      urls=["https://archive.org/details/yakintarihhh2"],
      loc="Gültekin, İstanbul Üniversitesi doktora tezi (2025), pp. 349-350", link="Necip Fazıl Kısakürek",
      nxt="Necip Fazıl, B.D. Fikir Kulübü Davası ve Müdafaalarım (the defence text)"),
 dict(id="refik-halid-karay-1964", voice="Refik Halid Karay", role="Satirist, Damad Ferid cabinet's Director of Posts and Telegraphs in 1919, exiled 1922-1938", c="Turkey", cn="Turkey",
      dom="letters", date="1964", era="posthumous", mirror=None, pol="conflicted", inten=1,
      saw="Recalling 1919, says the Istanbul officials trying to keep the government in hand against Kemal were people of limited power and grasp.",
      q="Mustafa Kemal Paşa'nın rakipleri bu kudrette, bu idrakte adamlardı!",
      art="memoir", ev="P", med=None, src="karay_minelbab.txt",
      cav="Turkish original; Minelbab İlelmihrab was first serialised in 1924 (per the edition's note) and published in book form in 1964 with notes (the text here is the 2009 İnkılâp edition, which says so). Karay writes of Istanbul in the weeks before the Sivas Congress, and the clause is about the Istanbul side, not a judgement of Kemal. He was an Istanbul minister's official then, and a rival of Kemal in that sense; he was exiled by the Ankara government in 1922 and allowed back in 1938. The OCR places the passage near folios 282-283; the exact page is not certain. A passing view, kept at intensity 1.",
      urls=["https://archive.org/details/refik-halit-karay-bugu-nu-n-saraylisi"],
      loc="Karay, Minelbab İlelmihrab (İnkılâp, 2009), ch. 'Sivas Kongresi'nden Evvel İstanbul Neler Yapıyor...', near pp. 282-283", link="Refik Halid Karay",
      nxt="Karay's 1938-1950 newspaper writing on Atatürk (not found open)"),
]

for r in R:
    if r["src"]:
        assert norm(r["q"]).rstrip(",") in bank(r["src"]), r["id"]
        print("quote verified:", r["id"])
    else:
        print("no banked text:", r["id"])

with open(os.path.join(STATE, "gazes_rivals.jsonl"), "w", encoding="utf-8") as f:
    for r in R:
        rec = {"id": r["id"], "voice": r["voice"], "voice_type": "person", "role": r["role"], "country": r["c"],
               "country_now": r["cn"], "domain": r["dom"], "date": r["date"], "era": r["era"], "mirror": r["mirror"],
               "polarity": r["pol"], "intensity": r["inten"], "what_they_saw": r["saw"], "quote": r["q"],
               "artifact": r["art"], "evidence": r["ev"], "mediated_by": r["med"], "caveat": r["cav"],
               "node": NODE, "sources": r["urls"]}
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")

with open(os.path.join(STATE, "ledger_rivals.md"), "w", encoding="utf-8") as f:
    f.write("| Claim | Node | Status | Sources | Next step |\n|---|---|---|---|---|\n")
    for r in R:
        qs = r["q"] or "(paraphrase)"
        f.write("| %s (%s, %s): \"%s\" | %s | verified %s (%s) | %s | %s |\n" % (
            r["voice"], r["role"][:50], r["date"], qs[:110].replace("|", "/") + ("..." if len(qs) > 110 else ""),
            NODE, r["ev"], r["loc"], "; ".join(r["urls"][:1]), r["nxt"] or "none"))

new_people = {
 "Necip Fazıl Kısakürek": ("Poet, editor of Büyük Doğu, Islamist-conservative critic of Kemalism", "Turkish", "1904–1983", "conflicted (admiring in 1943, accused of veiled hostility in 1967)",
    "The two faces on file: a 1943 article imagining Atatürk's return, and a 1967 courtroom denial that his 'false heroes' lecture meant Atatürk."),
 "Refik Halid Karay": ("Satirist and novelist, Damad Ferid cabinet official, exiled 1922–1938", "Turkish", "1888–1965", "conflicted (rival in 1919, later reconciled)",
    "An Istanbul official of 1919 who was exiled by Ankara and wrote in his memoir that Kemal's rivals in the capital were people of small capacity."),
}
for name, (role, nat, life, stance, desc) in new_people.items():
    if os.path.exists(os.path.join(HERE, "vault", "People", name + ".md")):
        continue
    person(name, role=role, nat=nat, life=life, stance=stance, tags=["verified", "rival"],
           body="%s See [[%s]] for the quotes and sources.\n\n## Sources\n- See [[%s]].\n" % (desc, NODE, NODE))

body = ["""
Round 17 went looking for the people who stood on the other side of Mustafa Kemal: the sultan he served, the Unionist who lost
the leadership race, the journalist the mob killed, the satirist who was exiled, and an Islamist poet. The seam was archive.org's
open Turkish texts, found with the full-text search, rather than the news archives. The result is eleven records, nine of them from
1920 to 1925, and nearly all hostile or conflicted. What they say in their own voices is mostly a list of grievances: that
Kemal rebelled against the sultan who sent him, that he wanted to rule alone, that he used faith as cover.

## The pattern

- **The sultan's three versions of a rebellion:** [[Mehmed VI Vahideddin]] says the same thing to a British envoy (1921), to
  a courtier in exile (1924) and in a memoir dictated in 1925: the palace sent Kemal to Anatolia and he rebelled. In March
  1924 he adds a religious charge, in a letter to Egyptian clergy. Two of the four are second-hand and one is a back-translation
  from English.
- **Enver, the rival who knew him:** [[Enver Pasha]]'s own letters to Kemal and Cemal, May-July 1921, print the quarrel in his
  words: first the plea not to rule alone, then, after Hâkimiyet-i Milliye attacked him, the charge of personal ambition.
- **The journalist:** [[Ali Kemal]] in Peyam-ı Sabah (6 May 1920) calls Kemal a false partisan who has opened a jihad of the
  crescent against the cross; the text reaches us through a 2019 article.
- **The poet:** [[Necip Fazıl Kısakürek]] praised Atatürk in 1943 and was tried in 1967 for a lecture the prosecution read as a hit on him. The
  vault stores both, as they are.
- **The satirist:** [[Refik Halid Karay]] on the weakness of Kemal's Istanbul rivals.
"""]
for r in R:
    body.append("\n## %s (%s)\n" % (r["voice"], r["date"]))
    body.append("*%s*\n" % r["saw"])
    if r["q"]:
        body.append("> %s\n" % r["q"])
    body.append("%s Location: %s. Evidence %s. See [[%s]].\n" % (r["cav"], r["loc"], r["ev"], r["link"]))

body.append("""
## Not stored, and dry ends (round 17)

- **Talat Pasha:** Yamauchi's edition prints only his letter of 29 Nov 1918 to Enver (no Kemal); Yamauchi's text says that in December 1920 Talat offered the British to send a delegate to Kemal, but the letter itself is not printed. Nothing stated about Kemal in Talat's own words.
- **Cemal Pasha:** the 2 Oct 1920 letter from Herat to Kemal (No. 25) is a report on Afghanistan; it curses the Istanbul government but states no view of Kemal. The 1922 memoir stands.
- **Abdülmecid II:** Bardakçı's *Şahbaba* prints the *Yeşil Kitab* (1924) with his first proclamation and a March 1924 statement; neither names Kemal. A 1920 protest letter to Kemal is mentioned but not quoted. Nothing stated.
- **Mustafa Sabri Efendi (lead):** *Şahbaba*, p. 276, quotes his *Hilâfet-i Muazzama-i İslâmiyye*: 'Mustafa Kemal âsi geldiği zaman ...' calling Kemal a rebel; the date and wording come through Bardakçı and Albayrak, so not stored. The pamphlet itself (Hilafet Risaleleri, vol. 5-6, ed. İsmail Kara, open on archive.org item yakintarihhh2) is the next step.
- **Sheikh Said:** the court record (Şark İstiklal Mahkemesi: Şeyh Said İsyanı, open on archive.org, yakintarihhh2) has him speaking of 'the government' and of jihad to enforce the sharia; the fatwa against Mustafa Kemal rests on M. Şerif Fırat's unsourced memoir and is not in the court file. No stated view of Kemal by Sheikh Said himself.
- **Seyid Rıza (Dersim 1937):** not searched; no solid source in reach, and the thread is sensitive.
- **Mustafa Suphi:** nothing found in open texts beyond secondary mentions; the Baku congress stenography (1920) is the place to look.
- **Rıza Tevfik, Prince Sabahaddin, Halide Edib, Said Nursi, Rauf Orbay, Karabekir, Şefik Hüsnü:** no new text. Rıza Tevfik appears in *Şahbaba* only in a joking letter about Mustafa Sabri on the camel road to Mecca (no statement on Kemal).
- **Refik Halid Karay:** *Sürgün* has no Kemal statement of his own (one fictional character calls himself an admirer of the Gazi); the single usable line is the Minelbab clause above. His later writing on Atatürk was not found open.
- **Darülfünun Grevi (1971), Ali Kemal's 6 Apr 1922 column:** lending-only, snippet seen, not stored.

## Sources
- archive.org open texts: Yamauchi (1995), Bardakçı (2006), Gültekin (2025), Karay (2009).
- DergiPark: Çakmak, Tarih İncelemeleri Dergisi 34/2 (2019).
""")
note("Events", NODE, {"type": "event", "when": "1920–1967", "tags": ["event", "verified", "rivals", "memoirs"]}, "\n".join(body))
print("ok", len(R), "records")
