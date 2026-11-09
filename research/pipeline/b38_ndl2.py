# -*- coding: utf-8 -*-
# Census round 29 (5 Nov 2026) - NDL Digital Collections, famous-author sweep (Miyake, Mitsukawa, Inoue, Deguchi, Kita, Tokutomi, Hashimoto, Abe, Ozaki). Page images read.
import json, os
from _lib import note
HERE = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(HERE, "tools", ".state", "round29")
os.makedirs(STATE, exist_ok=True)
NDL = "https://dl.ndl.go.jp/pid/"
JN = "Japanese Writers and Activists on Kemal, 1922–1947 — NDL Digital Collections"
def rec(id, voice, role, dom, date, era, mirror, pol, inten, saw, quote, art, cav, src):
    return {"id": id, "voice": voice, "voice_type": "person", "role": role, "country": "Japan", "country_now": "Japan",
            "domain": dom, "date": date, "era": era, "mirror": mirror, "polarity": pol, "intensity": inten,
            "what_they_saw": saw, "quote": quote, "artifact": art, "evidence": "P", "mediated_by": None,
            "caveat": cav, "node": JN, "sources": src}
R = [
 rec("miyake-setsurei-1922-10", "Miyake Setsurei", "Philosopher-critic, editor of Nihon oyobi Nihonjin", "letters", "1922-10", "contemporary",
     "nation-forge-template", "admiring", 2,
     "Marvels that Kemal, fighting Greece and bargaining with the great powers, has made 'a dead man' Turkey rise again and astonished diplomacy.",
     "近頃土耳古のケマルが希臘と戰ひ英佛伊等の强國と談判する所、從來の外交圈に意外の感を齎らしつゝある。土耳古は久しく瀕死の國と呼ばれ、講和會議に死人扱ひせられたるに、今や死人が甦り、新たに强國と對抗するに及ぶ。",
     "article",
     "Essay dated 'Taishō 11, October' (Nihon oyobi Nihonjin), reprinted in Eiyūron (1939), printed p. 10, NDL image 13 (page image read). First clause is the tail of a longer sentence; quote starts mid-sentence. Under the 1939 publication date the essay itself is 1922. Setsurei is also cited as Miyake Yūjirō (pids 1268197, 1267866: list-type mentions only).",
     [NDL+"1261364"]),
 rec("mitsukawa-kametaro-1927", "Mitsukawa Kametarō", "Pan-Asianist activist and writer, Yūzonsha / Kokuryūkai circle", "politics", "1927", "contemporary",
     "anti-colonial-liberator", "admiring", 2,
     "Ranks Kemal with Lenin and Gandhi among the world's 'three great revolutionaries' and calls his revolution patriotic throughout, unlike Lenin's materialism.",
     "ケマル・パシヤはトルコの愛國者であります。それ故彼の行つたトルコ革命は徹頭徹尾愛國の精神が流れて居ります。",
     "book",
     "Sekai ishin ni menseru Nihon (1927), printed p. 32, NDL image 26 (page image read; the scan's spread order is reversed). The 'three great revolutionaries' phrase is reported as what people call him ('稱せられて居ります'), the patriot verdict is Mitsukawa's own. Other Mitsukawa books (1925–1932) mention Kemal only as a movement name or in narration.",
     [NDL+"1277856"]),
 rec("inoue-masaji-1930", "Inoue Masaji", "Japanese politician-publicist, former Foreign Ministry man and emigration promoter", "politics", "1930", "contemporary",
     "nation-forge-template", "admiring", 2,
     "Says Kemal saved Turkey: without him it would have been driven out of Europe, left a dying remnant in Anatolia.",
     "土耳古は彼に依りて救はれた。彼なくば土耳古は歐洲の地より驅逐せられ、亞細亞に於てもアナトリヤの一角に、衰殘の命を寄するの外なき運命に在つた。",
     "book",
     "Ijū to kaitaku (1930), printed p. 107, NDL image 63 (page image read). Chapter profiles Kemal as 'one generation's splendid fellow' aged 43, so it was probably written about 1924 and collected in 1930; the date given is the publication date. A later passage (p. 66 image) says Japan should not imitate Kemal, Lenin or Gandhi but achieve its task by Japanese spirit.",
     [NDL+"1278778"]),
 rec("deguchi-onisaburo-1934", "Deguchi Onisaburō", "Co-founder of the Ōmoto religion", "religion", "1934", "contemporary",
     None, "instrumental", 1,
     "Finds the hearts of Kemal, Mussolini and Hitler closely like his own long-held ideas, and is encouraged to build a new Japan.",
     "ケマルパシヤー、ムッソリニー、ヒットラー等の英雄の心事は窺かに余が常に抱ける思想に酷似したるを見て余は大に意を强うするものである。",
     "book",
     "Tōkan zuihitsu (1934), printed p. 31, NDL image 18 (page image read; the library copy carries pen marks). Entry date not legible; the preceding entry is dated Shōwa 9 (1934). Kemal is one of a trio, claimed as a precedent for Deguchi's own programme.",
     [NDL+"1138051"]),
 rec("kita-reikichi-1937", "Kita Reikichi", "Philosopher and Diet member, brother of Kita Ikki", "politics", "1937", "contemporary",
     None, "admiring", 1,
     "Names Mussolini, Kemal and Hitler together as modern heroes whose trait is a great faith in sound common sense, unlike lecture-hall economists.",
     "ムツソリーニもケマルもヒツトラーも、共に健全なる常識に對する偉大なる信念を有することに近代的英雄としての特色を有するものであつて、",
     "book",
     "Shisō to seikatsu (1937), printed p. 155, NDL image 79 (page image read). Excerpt cut at the comma. Elsewhere in the same book he calls the Kemalist state a fruit of the Greek war (p. 20 image) and wishes for a Kemal-like unifier for Manchuria (image 184).",
     [NDL+"1046880"]),
 rec("tokutomi-soho-1937", "Tokutomi Sohō", "Japanese journalist-historian, publisher of Kokumin Shimbun", "letters", "1937", "contemporary",
     "nation-forge-template", "admiring", 2,
     "Says Atatürk gave Turkey not only unity but a new spirit, reviving a corrupt state with Kemalism and deposing its religious head.",
     "卽ちケマル・アタチユルクといふ人は、土耳古に統一を與へたばかりでなく、土耳古に新たなる精神を與へた。",
     "book",
     "Sensō gaigen (1937), printed p. 103, NDL image 60 (page image read). Different from the 1936 record (Kemal 'learned from Japan'): here a direct verdict on Kemal's work, in a lecture on nations with and without an ideal. Sōhō's 1929 and 1931 statements are already in the dataset.",
     [NDL+"1271494"]),
 rec("hashimoto-kingoro-1939", "Hashimoto Kingorō", "Army colonel, Sakura-kai founder, head of the Greater Japan Youth Party", "military", "1939", "posthumous",
     "modernization-poster-child", "admiring", 2,
     "Holds up Kemal as the model of swift, resolute decision: he made the Turks change dress, write horizontally and drop polygamy within hours.",
     "例へば彼のケマルの如きはあの土耳古人の封建的の服裝を四十六時間にして叩き直し、文字を書くのも橫書に直させる、一夫多妻を一夫一妻にして了つた。",
     "speech",
     "Nihon no yuku michi — senchi kikan daiisshō (1939), a spoken text, printed p. 4, NDL image 4 (page image read). Book dated 1939, hence posthumous era. In 1942 (Seinen ni uttau, p. 99, image 55) he counts 'the late Kemal' with Hitler as having the three traits of a strong leader, a political organisation and the army.",
     [NDL+"1097598", NDL+"1044644"]),
 rec("abe-yoshishige-1941", "Abe Yoshishige", "Philosopher and essayist, later Education Minister", "letters", "1941", "posthumous",
     None, "conflicted", 2,
     "Concedes dictator Kemal really revived Turkey, called 'Father of the Turks', but fears for Turkey after him: one man's rise is brief.",
     "近時のトルコが獨裁者ケマルによつて生氣を得たのは事實であり、彼は實に「トルコの父」とさへ呼ばれて居る。併し彼なき後のトルコの將來が憂慮せられるのは、一國が一人によつて興るのは一時のことであり、",
     "book",
     "Jidai to bunka (1941), essay 'Shakai to kojin', printed p. 63, NDL image 37 (page image read). Written in the present tense about the dictators of the day (essay probably earlier than 1941); the republication in 1949 repeats the lines. Not a funeral-era text.",
     [NDL+"1882546", NDL+"1158825"]),
 rec("ozaki-yukio-1947", "Ozaki Yukio", "Veteran Japanese Diet member, 'father of the constitution'", "politics", "1947", "posthumous",
     "modernization-poster-child", "admiring", 2,
     "Says Kemal's switch to the Latin alphabet alone proves him a head above ordinary heroes, a great success achieved at almost no cost.",
     "而して土のケマルは、先年トルコ文字を廢して、ローマ字を採用した。此一事以て彼が世間普通の豪傑以上に一頭地を拔いてゐることを證するに足る。",
     "book",
     "Kaiko manroku (1947), 'Toruko no senrei', printed p. 103, NDL image 57 (page image read). Hitler is still 'unknown' in the passage, so the essay dates from the early 1930s; 1947 is the book date. Stronger and more personal than the 1934 record (a list with Mussolini and Hitler). The praise rests on the script change and does not touch other reforms.",
     [NDL+"1438901", NDL+"1154057"]),
]
R = [r for r in R if (r.get('id') if isinstance(r,dict) else None) not in {'deguchi-onisaburo-1934','kita-reikichi-1937'}]  # dropped at the check (one of three named exemplars)
body = """
A second sweep of the NDL Digital Collections full text (all 1,545 hits for the Kemal spellings, filtered by author), then the page images, for famous Japanese authors not yet in the census. Nine are added; the Japanese is verbatim from the page images, the glosses are the vault's. Related: [[Japanese Statesmen on Kemal, 1923–1939 — NDL Digital Collections]] and [[More Japanese Voices on Kemal, 1928–1935 — NDL Digital Collections]].

## Miyake Setsurei, October 1922
The philosopher-critic writes, in Nihon oyobi Nihonjin, that Kemal's war with Greece and his bargaining with Britain, France and Italy have given the old diplomatic circle an unexpected shock: 'Turkey, long called a dying country and treated as a dead man at the peace conference, now rises from the dead.' This is a contemporary, uncoached verdict from a major intellectual; the printed form is the 1939 collection Eiyūron, p. 10.

## Mitsukawa Kametarō, 1927
The Pan-Asianist writes that Kemal is a Turkish patriot and that 'the Turkish revolution he made has patriotism flowing through it from beginning to end', in contrast to Lenin the materialist. He also repeats that Lenin, Gandhi and Kemal are called the world's three great revolutionaries.

## Inoue Masaji, 1930
Politician and emigration publicist: Turkey 'was saved by him'; without Kemal it would have been driven out of Europe. In the same book he says Japan must not imitate Kemal, Lenin or Gandhi but do its work by Japanese spirit.

*Census check (5 Nov 2026): Deguchi (1934) and Kita (1937) below are kept as context but not counted as gazes — Kemal appears as one of three named heroes with Mussolini and Hitler.*

## Deguchi Onisaburō, 1934
The Ōmoto leader claims the hearts of the heroes Kemal Pasha, Mussolini and Hitler resemble his own thought and strengthen his resolve to build a new Japan (instrumental).

## Kita Reikichi, 1937
Kemal, Mussolini and Hitler share a great faith in sound common sense, which marks them as modern heroes (p. 155).

## Tokutomi Sohō, 1937
In Sensō gaigen: Atatürk gave Turkey unity and a new spirit. Different from the 1936 'Kemal learned from Japan' claim.

## Hashimoto Kingorō, 1939
The Sakura-kai founder's model of resolute decision: Kemal changed dress, script direction and marriage law within hours.

## Abe Yoshishige, 1941
Conflicted: Kemal revived Turkey and is called Father of the Turks, but a state raised by one man is fragile after him.

## Ozaki Yukio, 1947
Kemal's adoption of the Latin script proves he stands a head above ordinary heroes.

## Read and dry
Not counted: Araki Sadao 1937 (pid 1456106) narrates Turkey 'revived by Kemal'; the page image is not public (IIIF returns 307), so unread. Kōda Rohan, Yoshino Sakuzō: no Kemal Pasha (matches are an Atake-maru ship and Ismail Kemal Bey of Albania). Shiga Shigetaka, Nagata Hidejirō, Yabe Teiji, Sano Manabu, Bose (Japanese translation of Indian Struggle), Kasama Akio: narration, lists or reforms only. Nagayo Yoshirō: a character's line in a novel. Shimomura Kainan 1932: praises the script reform only. Egyptian Mustafa Kamil is also spelled ムスタフア・ケマル in Inoue's Kensōroku; not Atatürk.

## Sources
- https://dl.ndl.go.jp/pid/1261364 (Miyake)
- https://dl.ndl.go.jp/pid/1277856 (Mitsukawa)
- https://dl.ndl.go.jp/pid/1278778 (Inoue)
- https://dl.ndl.go.jp/pid/1138051 (Deguchi)
- https://dl.ndl.go.jp/pid/1046880 (Kita)
- https://dl.ndl.go.jp/pid/1271494 (Tokutomi)
- https://dl.ndl.go.jp/pid/1097598 and https://dl.ndl.go.jp/pid/1044644 (Hashimoto)
- https://dl.ndl.go.jp/pid/1882546 (Abe)
- https://dl.ndl.go.jp/pid/1438901 (Ozaki)
"""
note("Events", JN, {"type": "event", "when": "1922-1947", "tags": ["event", "verified", "japan", "ndl"]}, body)
with open(os.path.join(STATE, "gazes_ndl2.jsonl"), "w", encoding="utf-8") as f:
    for r in R: f.write(json.dumps(r, ensure_ascii=False) + "\n")
print(len(R), "records")
