# -*- coding: utf-8 -*-
# Census round 18 (Nov 2026) — Muslim scholars and poets of the late Ottoman and early Republican world on Mustafa Kemal.
# Seam: archive.org open items in the yakintarihhh2 collection: İsmail Kara's Hilafet Risaleleri vol. 6 (2014), which prints a Turkish
# translation of Mustafa Sabri's Arabic book en-Nekir (Beirut 1924); Sadık Albayrak's 1992 edition of Sabri's Yarın articles
# (item mustafa-sabri-efendi-hilafet-ve-kemalizm-...); the TBMM 2021 volume Istiklal Marsi ve Mehmet Akif Ersoy (item
# istiklal-marsi-ve-mehmet-akif-ersoy), which prints a Turkish police report of 1935. Texts banked in tools/.state/round18/.
# Quotes are checked fuzzily against the OCR (hyphenation removed; OCR slips such as 'aynlığmı' tolerated, threshold 0.93).
import json, os, re, difflib
from _lib import note

HERE = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(HERE, "tools", ".state", "round18")
NODE = "Sabri Efendi and Mehmed Âkif on Mustafa Kemal, 1924–1935"

def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("—", "-").replace("’", "'")
    s = re.sub(r"-\s*\n\s*", "", s)
    s = re.sub(r"\s+", " ", s).lower()
    s = s.replace("ı", "i").replace("â", "a").replace("î", "i").replace("û", "u")
    return s

def bank(n):
    return norm(open(os.path.join(STATE, n), encoding="utf-8").read())

def fuzzy_in(q, text, thr=0.93):
    q = norm(q); n = len(q)
    # anchor on the first 18 characters, then compare windows
    anchor = q[:18]; best = 0.0; pos = text.find(anchor)
    while pos != -1:
        w = text[pos:pos + n + 6]
        r = difflib.SequenceMatcher(None, q, w[:n]).ratio()
        best = max(best, r)
        pos = text.find(anchor, pos + 1)
    return best >= thr, best

R = [
 dict(id="mustafa-sabri-1924", voice="Mustafa Sabri Efendi", role="Last Ottoman Shaykh al-Islam, in exile in Beirut and Cairo", c="Lebanon (French mandate)", cn="Lebanon",
      dom="religion", date="1924", era="contemporary", mirror="apostate", pol="hostile", inten=3,
      saw="Argues that Kemal split caliphate from sultanate not to reform Turkish rule but to take power for himself.",
      q="Çünkü Mustafa Kemal hilafet-saltanat ayrılığını Türk idaresini ıslah etmek için ortaya atmış değildir.",
      art="book", ev="P", med="Turkish translation (Kara, Hilafet Risaleleri 6, 2014) of the Arabic en-Nekir ala Munkiri'n-Nime mine'd-Din ve'l-Hilafe ve'l-Umme (Beirut, Matbaatu'l-Abbasiye, 1342/1924)", src="hr6.txt",
      cav="Quoted from the Turkish translation by the volume's translator (the Arabic original was not read); the OCR has 'aynlığmı', read as 'ayrılığını'. The next paragraph says the Kemalists had 'only two aims': first, to take the sultanate from the Ottoman house by force and transfer it to Mustafa Kemal and to separate the caliphate from it; the transfer to the Assembly was 'nothing other than hiding the real intent'. Kara dates the book to 1923, first finished 1 Receb 1342 / 7 Feb 1924, with a 15-page appendix of 20 Mar 1924 after the caliphate fell. Sabri's own judgment; the vault does not endorse it. Cited by the editor's pagination as risale 59 ('Hilafetin Saltanattan Tefriki'), listed at p. 405 of the volume; the printed folio is not legible in the OCR (archive.org scan, PDF pp. 403-405).",
      urls=["https://archive.org/details/yakintarihhh2"],
      loc="Mustafa Sabri, en-Nekir (Beirut 1924), Turkish tr. in İsmail Kara (ed.), Hilafet Risaleleri 6 (2014), risale 59, scan pp. 403-405", link="Mustafa Sabri Efendi",
      nxt="Arabic original (Beirut 1342); Kara's own summary in the volume"),
 dict(id="mustafa-sabri-1927", voice="Mustafa Sabri Efendi", role="Former Shaykh al-Islam; writer for the newspaper Yarın (Gümülcine/İskeçe, Western Thrace)", c="Greece", cn="Greece",
      dom="religion", date="1927", era="contemporary", mirror="apostate", pol="hostile", inten=2,
      saw="Mocks praise of Kemal's Dolmabahçe remark on Allah's shadow, saying the Ankara head of government himself admits he is not that.",
      q="Nasıl ki Ankara hükümet reisi de kendi itirafiyle zıllullah değildir.",
      art="article", ev="S", med="Albayrak 1992 (reprint of Yarın articles)", src="sabri92.txt",
      cav="Article 'Cuhela Marifetleri' (printed pp. 406-408 of Albayrak's edition; the OCR reads 'Nasil ki ... hükü- met'). The speech is Mustafa Kemal's Dolmabahçe address of July 1927, in which, as Sabri reports it, he said the palace now belonged to the nation, not to 'Zıllullah'; Sabri quotes Ağaoğlu Ahmed in Milliyet, 7 July 1927 ('Mustafa Kemal Allah'ın gölgesi değil, milletin gölgesidir'). Sabri then adds that he, unlike others, is not afraid of Mustafa Kemal when he criticises his words. DATE UNCERTAIN: the closest source note in Albayrak's print is 'Yarın, sayı: 2, 29/7/1927, sh: 2-3', which sits at the end of the next piece, so the issue of this article is inferred, year only. Sabri's own judgment; the vault does not endorse it.",
      urls=["https://archive.org/details/mustafa-sabri-efendi-hilafet-ve-kemalizm-arastirma-yayinlari-415-sayfa-1992"],
      loc="Mustafa Sabri, 'Cuhela Marifetleri', Yarın (İskeçe), 1927/28, in Albayrak (ed.), Hilafet ve Kemalizm (Araştırma Yayınları, 1992), pp. 406-408", link="Mustafa Sabri Efendi",
      nxt="Yarın, İskeçe, issue 2 (29 Jul 1927) in the original"),
 dict(id="mustafa-sabri-1928", voice="Mustafa Sabri Efendi", role="Former Shaykh al-Islam; writer for the newspaper Yarın (İskeçe, Western Thrace)", c="Greece", cn="Greece",
      dom="religion", date="1928-06-23", era="contemporary", mirror="apostate", pol="hostile", inten=2,
      saw="Calls Kemal a rebel against Sultan Vahideddin and judges his separation of state from religion to be irreligion.",
      q="Merhum Sultan Vahidüddin'e ve hükümetine Anadolu'da Mustafa Kemal asi geldiği zaman",
      art="article", ev="S", med="Albayrak 1992 ← Yarın, no. 23, 23 Jun 1928, pp. 2-4", src="sabri92.txt",
      cav="Article 'Sıyrılan İkinci Maske (Abdülmecid Komedisi)', aimed at the Cairo paper Müsavat and at Abdülmecid II; the print's citation 'Yarı[n], sayı: 23, 23 Haziran 1928, sh: 2-4' closes it. The sentence runs on: 'it is unnecessary to repeat here how far Abdülmecid secretly and openly backed this rebellion'. Quoted in Bardakçı's Şahbaba (p. 276 in the 1998 edition, with 'âsi'), via Albayrak. In the same article Sabri writes that Kemal's act, 'dinden devleti ayırması', is 'dinsizlik' (irreligion) while a religionless government can be imagined outside Islam but a religionless caliphate cannot (OCR slightly garbled, so paraphrased). Pages 172-173 of the 1992 print. Sabri's own judgment; the vault does not endorse it.",
      urls=["https://archive.org/details/mustafa-sabri-efendi-hilafet-ve-kemalizm-arastirma-yayinlari-415-sayfa-1992", "https://archive.org/details/sahbaba-murat-bardakci"],
      loc="Mustafa Sabri, 'Sıyrılan İkinci Maske', Yarın no. 23, 23 Jun 1928, in Albayrak (ed.), Hilafet ve Kemalizm (1992), pp. 170-173; quoted in Bardakçı, Şahbaba, p. 276", link="Mustafa Sabri Efendi",
      nxt="Yarın no. 23 in the original"),
 dict(id="mehmed-akif-1935", voice="Mehmed Âkif Ersoy", role="Poet of the national anthem, in exile in Egypt; reported in Antakya", c="Hatay (French mandate of Syria)", cn="Turkey",
      dom="letters", date="1935-08", era="contemporary", mirror=None, pol="hostile", inten=1,
      saw="Reported as saying Kemal owed life, honour and position to Rauf Orbay and repaid the debt by trying to ruin him.",
      q="Gazi paşa def'atla hayatını, şerefini ve mevkiini Rauf beye medyundur.",
      art="quote", ev="J", med="Turkish police/intelligence report of 6 Sept 1935 on 'İslâm şairi Akif', printed in TBMM, İstiklâl Marşı ve Mehmet Âkif Ersoy (2021), Belgeler", src="tbmm_akif.txt",
      cav="Not Âkif's own text: a typed Turkish report on Âkif's three weeks in Antakya (he left on 31 Aug 1935 after a telegram), from a hostile informant, in OCR with errors ('mevki- ini'). It quotes him: 'Rauf bey returned to Turkey but cannot get a position, because the Gazi cannot bear Rauf', and that Kemal, at the Topal Osman affair and the Sivas Congress time, had been shielded by Rauf, 'but this gratitude produced the opposite result: instead of doing him a kindness he worked to destroy Rauf'. The same report says Âkif called the abolition of the caliphate the greatest irreligion and called the hat 'entirely unbelief' (statements about the reforms, not named as Kemal's). Whether Âkif's remark was accurately reported is unchecked. Mehmet Âkif is otherwise on record as having said nothing unfavourable about Mustafa Kemal (Derin Tarih no. 81, 2018, snippet).",
      urls=["https://archive.org/details/istiklal-marsi-ve-mehmet-akif-ersoy"],
      loc="TBMM, İstiklâl Marşı ve Mehmet Âkif Ersoy (2021), Belgeler section, report 'İslâm şairi Akif' (6 Eylül 1935), OCR text", link="Mehmet Akif Ersoy",
      nxt="Archive original (BCA); confirm authorship and who the informant was"),
]

for r in R:
    ok, ratio = fuzzy_in(r["q"], bank(r["src"]))
    print("%-22s %s %.3f" % (r["id"], "OK" if ok else "FAIL", ratio))
    assert ok, r["id"]

with open(os.path.join(STATE, "gazes_ulema.jsonl"), "w", encoding="utf-8") as f:
    for r in R:
        rec = {"id": r["id"], "voice": r["voice"], "voice_type": "person", "role": r["role"], "country": r["c"],
               "country_now": r["cn"], "domain": r["dom"], "date": r["date"], "era": r["era"], "mirror": r["mirror"],
               "polarity": r["pol"], "intensity": r["inten"], "what_they_saw": r["saw"], "quote": r["q"],
               "artifact": r["art"], "evidence": r["ev"], "mediated_by": r["med"], "caveat": r["cav"],
               "node": NODE, "sources": r["urls"]}
        assert len(r["saw"].split()) <= 25, r["id"]
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")

with open(os.path.join(STATE, "ledger_ulema.md"), "w", encoding="utf-8") as f:
    f.write("| Claim | Node | Status | Sources | Next step |\n|---|---|---|---|---|\n")
    for r in R:
        qs = r["q"]
        f.write("| %s (%s, %s): \"%s\" | %s | verified %s (%s) | %s | %s |\n" % (
            r["voice"], r["role"][:50], r["date"], qs[:110].replace("|", "/") + ("..." if len(qs) > 110 else ""),
            NODE, r["ev"], r["loc"], "; ".join(r["urls"][:1]), r["nxt"] or "none"))

body = ["""
Round 18 looked for Muslim scholars, poets and religious figures of the late Ottoman and early Republican world who said something
in their own words about Mustafa Kemal. The dataset was thin here and so is this round: four records, three of them from the last
Ottoman Shaykh al-Islam, Mustafa Sabri Efendi, whose texts are open on archive.org, and one reported remark of the poet Mehmed Âkif (kept here as context only: the census check judged an unnamed informant's report, written to portray him as hostile, too weak to count as his gaze).
All four are hostile. The sources are an edition of Turkish translations of Sabri's work and a printed police report; nothing here is
a manuscript read in an archive.

## The pattern

- **The theologian's charge:** [[Mustafa Sabri Efendi]] wrote in 1924 that Kemal separated the caliphate from the sultanate not to
  reform Turkish rule but to take power himself (a translation of his Arabic book, printed in Kara's *Hilafet Risaleleri* 6); in
  1927 he mocked the Dolmabahçe remark about Allah's shadow; in 1928 he called Kemal a rebel against Sultan Vahideddin and wrote
  that separating state from religion was irreligion. All three are his own judgments, set out in the quotations below as he gave them.
- **The poet:** [[Mehmet Akif Ersoy]] has no Kemal text in the open sources checked. The one record is a 1935 report by a hostile
  informant, so it counts as reported speech only.
"""]
for r in R:
    body.append("\n## %s (%s)\n" % (r["voice"], r["date"]))
    body.append("*%s*\n" % r["saw"])
    body.append("> %s\n" % r["q"])
    body.append("%s Location: %s. Evidence %s. See [[%s]].\n" % (r["cav"], r["loc"], r["ev"], r["link"]))

body.append("""
## Not stored, and dry ends (round 18)

- **Mehmed Âkif's poems and letters:** the Safahat poems of the War of Independence period and the Cairo letters were not found as an open text with a stated view of Kemal. TBMM's 2021 volume prints only the 1935 report above; Dücane Cündioğlu's *Akife Dair* (open) discusses Kemal only in the Qur'an-translation commission (a 1,000-lira advance, the TBMM decision) and denies the story that Kemal gave Âkif 10,000 liras. Mehmet Kaplan's 'Atatürk ve Mehmet Âkif' (Türk Dili, Dec 1986, pp. 500-501) is the author's comparison, not Âkif's words.
- **İskilipli Âtıf Hoca:** *Frenk Mukallitliği ve Şapka* (1924) was not read itself; the open doctoral thesis on the Hat Law (yakintarihhh2) summarises it and the Atıf Hoca trial (Dec 1925) without printing a statement by him about Kemal. The book text and his statements (published by Ümit Doğan, 2021) are the next step.
- **Şeyh Senusî (Ahmad al-Sharif al-Sanusi):** a Yeni Gün interview with Celal Nuri, printed in *Hilafet Risaleleri* 6, has the Libyan leader calling the Assembly's legitimacy 'above every suspicion' and referring to Mustafa Kemal's 'national and religious jihad'; the date is not given in the print and the words are Celal Nuri's report of a conversation, so it is a lead only.
- **Elmalılı Hamdi Yazır, Babanzâde Ahmed Naim, Said Halim Pasha, Musa Carullah Bigiyev, Abdürreşid İbrahim, Zahid el-Kevserî, Süleyman Hilmi Tunahan, Abdülhakim Arvasi, Gümüşhanevî line:** full-text searches (archive.org fts) gave no usable first-hand statement of a view of Kemal. Kevserî appears only in Mısıroğlu's footnotes; Carullah only in the Qur'an-translation row; Tunahan only in Uğur Mumcu and theses.
- **Said Nursi, Necip Fazıl:** skipped as already voices.

## Sources
- archive.org open texts: Kara (ed.), Hilafet Risaleleri 6 (2014); Albayrak (ed.), Mustafa Sabri, Hilafet ve Kemalizm (1992); TBMM, İstiklâl Marşı ve Mehmet Âkif Ersoy (2021); Bardakçı, Şahbaba.
""")
note("Events", NODE, {"type": "event", "when": "1924–1935", "tags": ["event", "verified", "religion", "ulema"]}, "\n".join(body))
print("ok", len(R), "records")
