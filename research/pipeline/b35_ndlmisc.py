# -*- coding: utf-8 -*-
# Census round 26 (4 Nov 2026) — Japanese statesmen on Kemal from NDL Digital Collections full text, and Pope John Paul II at Anitkabir 1979.
import json, os
from _lib import note
HERE = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(HERE, "tools", ".state", "round26")
os.makedirs(STATE, exist_ok=True)
NDL = "https://dl.ndl.go.jp/pid/"
JN = "Japanese Statesmen on Kemal, 1923–1939 — NDL Digital Collections"
JPN = "Pope John Paul II at Anıtkabir, 28 November 1979"
def rec(id, voice, role, dom, date, era, mirror, pol, inten, saw, quote, art, ev, med, cav, node, src, country="Japan", cn="Japan"):
    return {"id": id, "voice": voice, "voice_type": "person", "role": role, "country": country, "country_now": cn,
            "domain": dom, "date": date, "era": era, "mirror": mirror, "polarity": pol, "intensity": inten,
            "what_they_saw": saw, "quote": quote, "artifact": art, "evidence": ev, "mediated_by": med,
            "caveat": cav, "node": node, "sources": src}
OCR = " Text from the NDL full-text (OCR) API; "
R = [
 rec("nakano-seigo-1923-03-20", "Nakano Seigō", "Member of the House of Representatives, journalist, later Tōhōkai leader", "politics", "1923-03-20",
     "contemporary", "anti-colonial-liberator", "admiring", 2,
     "Hails 'a young man named Kemal Pasha' raising the crescent flag against Sèvres as a gratifying defiance by a coloured nation.",
     "彼の將に滅亡せんとする土耳古より「ケマルパシヤ」なる一靑年が弦月旗を提げて起つたるときに",
     "speech", "P", None,
     "Diet speech on recognising Soviet Russia, 20 March 1923, stenographic record (Roshia shōnin ron). Quote read on the page image (printed p. 19, NDL image 13). Translation of the gist is the vault's; quote is the original Japanese. Kemal is used as an argument for Russo-Japanese rapprochement (instrumental element).",
     JN, [NDL+"965639"]),
 rec("tokutomi-soho-1929", "Tokutomi Sohō", "Japanese journalist-historian, publisher of Kokumin Shimbun", "letters", "1929",
     "contemporary", "nation-forge-template", "admiring", 1,
     "Names Kemal Pasha as, after Mussolini, the most striking example of the 'personality politics' the world now demands in place of party politics.",
     "而して次に最も著しき例は、土耳其新興國のケマル·パシャである。",
     "book", "P", None,
     "Nihon teikoku no ichi tenki (Minyūsha, 1929), ch. 39 'Jinbutsu seiji', printed p. 210 (NDL OCR; page image not read). Same stable passage gives Kemal as an exemplar for criticising Japanese party politics.",
     JN, [NDL+"1272265"]),
 rec("tokutomi-soho-1936", "Tokutomi Sohō", "Japanese journalist-historian, publisher of Kokumin Shimbun", "letters", "1936",
     "contemporary", "nation-forge-template", "instrumental", 2,
     "Insists Kemal Pasha at least rose with Japan as his ideal, part of a claim that Egypt, Turkey and India copied Japan.",
     "尠くともケマルパシヤだけは、間違ひなく、日本を理想として起つたもので、これは決して疑ひを容れないのであります。",
     "book", "P", None,
     "Warera no Nihon seishin (1936), printed p. 110, read on the page image (NDL image 65); a lecture text. The same claim appears in Gendai Nihon to sekai no ugoki (1931, pid 1268736, 'Kemal Pasha ... also learned from Japan'). It is Tokutomi's Japan-centred appropriation, not a report of Kemal's own view.",
     JN, [NDL+"1261236", NDL+"1268736"]),
 rec("ashida-hitoshi-1939", "Ashida Hitoshi", "Diplomat-politician, later Prime Minister of Japan (1948)", "politics", "1939",
     "posthumous", "modernization-poster-child", "admiring", 2,
     "Calls Kemal an extraordinary genius whose courage and strategy in building new Turkey from the Ottoman corpse rival any Western statesman's.",
     "一九三八年の十一月までこの職に在つたケマルは最も異常な天才であつた。",
     "book", "P", None,
     "Barukan (1939), ch. 'Torukō no seiji', NDL image 32 (printed ~p. 49–50). OCR only. Also on p. 27 (image): 'fortunately there was one Kemal Pasha ... the endurance and patriotism of Turks is truly admirable'. Written after the death (posthumous era).",
     JN, [NDL+"1877434"]),
 rec("ozaki-yukio-1934", "Ozaki Yukio", "Veteran Japanese Diet member, 'father of the constitution'", "politics", "1934",
     "contemporary", None, "admiring", 1,
     "Lists Kemal with Mussolini and Hitler as dictator-heroes of the post-war world, noting Kemal's more than ten years of 'rarely seen success'.",
     "ムツソリニとケマルとは共に十餘年を經てゐるから、其の人物性行及び事業は旣によく全世界に知られ、世にも稀れなる成功を示しておる。",
     "book", "P", None,
     "Kindai kairaku-roku (1934), printed p. 268 (NDL image 77). OCR only. Ozaki calls them 'successful dictators' without moral endorsement; admiring on the success only.",
     JN, [NDL+"1223756"]),
 rec("john-paul-ii-1979-11-28", "Pope John Paul II", "Head of the Catholic Church and of Vatican City; entry in the Anıtkabir special book", "religion", "1979-11-28",
     "posthumous", None, "admiring", 2,
     "Writes in the mausoleum book that God raises the right leaders; reportedly tells Korutürk his admiration for Atatürk rests on Turkey's tolerance.",
     "Le gouvernement des peuples est dans les mains du Seigneur. Il suscite au moment opportun les chefs qui leur conviennent ...",
     "visit", "P+J", "Talks wording: Milliyet 30 Nov 1979 p. 10 (via gastearsivi.com OCR) and Belenli & Birbudak 2021 (Belgi 22, pp. 589–622)",
     "The quote is the French original reconstructed from the Vatican's Spanish text (vatican.va libro-oro-ataturk, 28 Nov 1979); the vault has seen only the Spanish ('El gobierno de los pueblos está en las manos del Señor. Él suscita en el momento oportuno los jefes que les conviene...') and the Turkish of Belenli & Birbudak, so the French is a back-translation: treat the quote as a translation of the entry. Turkish press (Milliyet 30 Nov 1979 p. 10) separately reports his words to President Korutürk that bowing at Anıtkabir 'before the saviour of Turkey and founder of its democratic republic' he was the first pope to do so, and that 'admiration for Atatürk and the Turkish State' rests on its treatment of minorities (Turkish text; the same sentences printed in Belenli & Birbudak 2021). The entry does not name Atatürk.",
     JPN, ["https://www.vatican.va/content/john-paul-ii/es/speeches/1979/november/documents/hf_jp-ii_spe_19791128_libro-oro-ataturk.html",
           "https://www.gastearsivi.com/gazete/milliyet2/1979-11-30/10",
           "https://dergipark.org.tr/en/download/article-file/1692331"], "Vatican City", "Vatican City"),
]
R = [r for r in R if r.get('id') not in {'tokutomi-soho-1929'}]  # dropped at the independent check (list items / no view of Kemal)
R[-1]["quote"] = "[translation, from the Spanish of vatican.va] El gobierno de los pueblos está en las manos del Señor. Él suscita en el momento oportuno los jefes que les conviene, porque el amor a la libertad y el respeto del derecho hacen grande a una nación"
body = f"""Full-text search of the National Diet Library's Digital Collections (NDL Lab API `lab.ndl.go.jp/dl/api/book/search`, OCR text at `.../fulltext-json/<pid>`) for ケマル・パシャ and spelling variants turns up about 270 interwar Japanese books. The notable voices below had not been in the census. All items are marked インターネット公開 (open to the public). Japanese quotes are verbatim; English glosses are the vault's translations.

## Nakano Seigō, 20 March 1923
In the Diet, arguing for recognition of Soviet Russia, he calls the rise of 'a young man named Kemal Pasha' under the crescent flag against the Sèvres treaty something 'we all feel gratified by', and sees Russia behind Turkey (printed p. 19; page image read, NDL pid 965639). A use of Kemal for his own policy.

## Tokutomi Sohō, 1929 and 1936
1929: Kemal is, after Mussolini, the most striking case of the 'man-based politics' the world wants (pid 1272265). 1936: 'at least Kemal Pasha undoubtedly rose with Japan as his ideal, which is beyond doubt' (printed p. 110, page image read, pid 1261236). The 1931 lecture book repeats the Kemal-as-pupil claim (pid 1268736).

## Ashida Hitoshi, 1939
In a book on the Balkans: 'Kemal ... was the most extraordinary genius', his courage and strategy 'second to no statesman of the Powers'; Turkey's endurance 'truly admirable' (pid 1877434, OCR only).

## Ozaki Yukio, 1934
Kemal and Mussolini as 'dictators who succeeded', 'rarely seen success' after a decade (pid 1223756, printed p. 268, OCR only).

## Other hits, not staged (passing or second-hand)
Ōkawa Shūmei (already in the census); Shimomura Kainan 1935 (wants 'a Mussolini, a Hitler, a Kemal Pasha' for Japan, but says admirers see only the stage show; pid 1273386, pp. 243, 271) and 1941; Takabatake Motoyuki 1928/1930 (Kemal a 'small' hero beside Mussolini; pids 1444148, 1268554); Shinmura Izuru 1941 (doubts the Turkish script reform's results; pid 1126363); Ōtani Kōzui 1929 (pid 1465913). No hits for Kita Ikki, Uchida Ryōhei (the Kokuryūkai's 1926 Tanabe and 1931 Saishin Ajia taikan books are in the result set but not read), Inukai or Tōyama Mitsuru in the full text.

## Sources
- https://dl.ndl.go.jp/pid/965639 (Nakano, 1923)
- https://dl.ndl.go.jp/pid/1272265 and https://dl.ndl.go.jp/pid/1261236 and https://dl.ndl.go.jp/pid/1268736 (Tokutomi)
- https://dl.ndl.go.jp/pid/1877434 (Ashida, 1939)
- https://dl.ndl.go.jp/pid/1223756 (Ozaki, 1934)
"""
note("Events", JN, {"type": "event", "when": "1923-1939", "tags": ["event", "verified", "japan", "ndl"]}, body)
body2 = f"""On 28 November 1979, during the first papal visit to Turkey, John Paul II laid a wreath at Anıtkabir and wrote in the visitors' book (in French). The Vatican publishes the entry as *Libro de oro del Mausoleo de Atatürk*: 'The government of peoples is in the hands of the Lord. He raises up at the right moment the leaders that suit them, because love of liberty and respect for law make a nation great, but it is God who guarantees the future.' (Spanish text; translation by the vault.) The entry does not name Atatürk.

In the official talks with President Fahri Korutürk the same evening, Milliyet (30 Nov 1979, p. 10) reports him as saying he was the first pope to bow at Anıtkabir 'before the saviour of Turkey and founder of its democratic republic', praising the 'modern and secular Turkish State' for its treatment of religious and ethnic communities, and adding that 'my admiration for Atatürk and the Turkish State rests on these facts' (Turkish report; the same sentences in Belenli and Birbudak 2021). Indirect report, not a transcript. Compare [[Leaders in the Anıtkabir Special Book, 2004–2025]] for later entries.

## Sources
- https://www.vatican.va/content/john-paul-ii/es/speeches/1979/november/documents/hf_jp-ii_spe_19791128_libro-oro-ataturk.html
- https://www.gastearsivi.com/gazete/milliyet2/1979-11-30/10 (Milliyet OCR mirror)
- https://dergipark.org.tr/en/download/article-file/1692331 (Belenli and Birbudak, Belgi 22, 2021)
"""
note("Events", JPN, {"type": "event", "when": "1979-11-28", "tags": ["event", "verified", "vatican", "anitkabir"]}, body2)
with open(os.path.join(STATE, "gazes_ndlmisc.jsonl"), "w", encoding="utf-8") as f:
    for r in R: f.write(json.dumps(r, ensure_ascii=False) + "\n")
print(len(R), "records")
