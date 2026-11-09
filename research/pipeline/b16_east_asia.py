# -*- coding: utf-8 -*-
# Census round 8 (Oct 2026) — East Asia, 1919-1938: the first proper primary Chinese and Japanese voices (slug: east_asia).
# Route: Chinese Wikisource (zh.wikisource.org; MediaWiki API search for 凱末爾 / 基瑪爾 / 基馬爾 / 凱馬爾 / 凯末尔, then action=parse of each page)
# and Aozora Bunko (index CSV + HTML of ~500 works by 24 pre-1960 authors, grepped for ケマル / 土耳古 / トルコ革命).
# Every Chinese quotation was machine-checked against the rendered Wikisource page with whitespace removed (Wikisource inserts spaces before proper names).
# Translations are mine and marked "(my translation)". Nothing here is read from a secondary source except where the note says so.
from _lib import note, person

# ---------------------------------------------------------------- people
person("Yun Daiying", role="Communist theorist and Whampoa instructor; writing in Dongfang zazhi (The Eastern Miscellany), 1923", nat="Chinese", life="1895–1931",
  stance="admiring; wants a Chinese Kemal and a Kemal's army",
  tags=["politician", "china", "contemporary", "verified"], body="""
The earliest Chinese **Dongfang zazhi** (東方雜誌, Commercial Press, Shanghai) text in this census, and the bluntest use of Kemal as a *programme for China*.

**"時論的誤點" ("Where current opinion goes wrong"), Dongfang zazhi vol. 20 no. 22, 25 November 1923.** Yun argues that China's civil wars are only a Tang-to-Five-Dynasties
chaos and that every plan on offer ignores the armed classes. To show that foreign pressure is no excuse he reaches for Turkey, "the worst-pressed of all after the war":
*"然而試看凱末爾將軍振臂一呼，居然可以使英法等國失色退讓…君士坦丁堡，仍於洛桑會議以後六星期內雙手奉還"* (my translation: "yet look at General Kemal, who raised one arm and made Britain and France pale and give way... Constantinople handed back within six weeks of the Lausanne Conference"). Then the line the whole text turns on:
*"凱末爾將軍的軍隊，救了將亡國的土耳其。中國亦需要一個凱末爾將軍，亦需要一個凱末爾將軍的軍隊啊!"* (my translation: "General Kemal's army saved a Turkey on the brink of extinction. China too needs a General Kemal, and needs a General Kemal's army!").

**Reading.** Yun's Kemal is the soldier who *refused* the great powers, not a statesman or a reformer; he wants the army (the Whampoa project was months old). That a Communist writes this in the
same year the Comintern line on Ankara cooled (see [[Xiangdao Reads Ankara, 1922–1924]]) shows how far "Kemal" was a floating name for *the leader who wins* before it became a party-political label ([[Kemal in the Kuomintang's Quarrels, 1924–1928]]).

**Caveats.** Wikisource inserts spaces before proper names ("一個 凱末爾將軍"); quotations above are space-normalised. The page cites the journal volume and issue but not page numbers.

## Sources
- 惲代英, 時論的誤點, 東方雜誌 20(22), 25 Nov 1923 — Chinese Wikisource: [zh.wikisource.org/wiki/時論的誤點](https://zh.wikisource.org/wiki/%E6%99%82%E8%AB%96%E7%9A%84%E8%AA%A4%E9%BB%9E) · tier P (transcription; the header gives journal, volume, issue and date)
""")

person("Hu Shi", role="Philosopher, Peking University professor; editor of the weekly Duli pinglun (Independent Critic)", nat="Chinese", life="1891–1962",
  stance="analytic and deflating: Kemal's war was against a weak Greek army, so Turkey is no precedent for resisting Japan",
  tags=["letters", "china", "contemporary", "verified"], body="""
After the loss of Manchuria and the Tanggu Truce, the philosopher **Xiong Shili** wrote to Hu Shi asking why China should not fight on as Turkey had ("土耳其有幾多科學設備？而苦戰抗敵矣", *how many scientific facilities did Turkey have, yet it fought hard and beat the enemy*).
Hu printed the letter in *Duli pinglun* with an editor's note dated **21 May 1933**, and answered the Turkish point directly:

*"凯末尔将军所抗之敌已不是1918年停战以前的协约国联军了，不过是那贪横的希腊军队。希腊的政治组织本不坚固，军队也不是劲敌"* (my translation: "The enemy General Kemal fought was no longer the Allied armies that had faced Turkey before the 1918 armistice, but only the grasping Greek army. Greece's political organisation was never solid and its army was no strong foe.")
He goes on: Italy and France were sympathetic, the Allied leaders feared Soviet influence in the new Turkey, all Europe wanted the corner quiet, and Lausanne gave Turkey its sliver of Europe. *"我們應知道新土耳其與希臘的戰爭與今日的中日戰爭是不能相提並論的"* ("The Turko-Greek war and today's Sino-Japanese war are not comparable").

**Reading.** An *instrumental* use of Kemal in the other direction from [[Yun Daiying]]: Hu's case is for restraint, and the way to make it is to cut Kemal's victory down to size. He does not belittle Kemal as a person, only the analogy. The accurate history (Lausanne, Greece's revolution) is Hu's own.

**Caveats.** The Wikisource text is in simplified characters (as printed there); the page gives no issue number. Hu's polarity toward Kemal himself is not stated; the note records his deflation of the *model*.

## Sources
- 胡適, 熊十力《要在根本處注意》一文的編者附言, 獨立評論, 21 May 1933 — Chinese Wikisource: [zh.wikisource.org/wiki/熊十力《要在根本處注意》一文的編者附言](https://zh.wikisource.org/wiki/%E7%86%8A%E5%8D%81%E5%8A%9B%E3%80%8A%E8%A6%81%E5%9C%A8%E6%A0%B9%E6%9C%AC%E8%99%95%E6%B3%A8%E6%84%8F%E3%80%8B%E4%B8%80%E6%96%87%E7%9A%84%E7%B7%A8%E8%80%85%E9%99%84%E8%A8%80) · tier P (transcription)
""")

person("Jiang Tingfu", role="Historian, Tsinghua professor; later diplomat; author of the Commercial Press survey of modern China (1938)", nat="Chinese", life="1895–1965",
  stance="admiring; the template of the leader who 'knew no self' and modernised root and branch",
  tags=["letters", "china", "contemporary", "verified"], body="""
In the survey that made his name, **中國近代史** (Commercial Press, first edition July 1938; the Wikisource text is titled *中國近代史大綱*), Jiang opens with a comparative argument that modern culture decides national strength, and Turkey is his proof (before turning to Japan).

He sets Turkey's late-Ottoman reform ("三心兩意的，不澈底的，無整個計畫的", *half-hearted, incomplete, without a plan*) against what followed the war:
*"土耳其人經過那次大國難以後，一致團結起來，擁護民族領袖基瑪爾，於是始得復興。基瑪爾一心一意爲國家服務，不知有他。他認識了時代的潮流，知道要救國非澈底接受近代的文化不可"* (my translation: "After that great national disaster the Turks united and rallied behind the national leader Kemal, and so recovered. Kemal served the country with a single mind and knew no self. He recognised the current of the age, and knew that to save the country he must accept modern culture to the root."). He credits him with science and industry, and with changing the script: *"甚至改革了土耳其的文字"*, because the old script wasted children's time that could go to "real learning". Then: *"現在土耳其立國的基礎算打穩了"* ("Turkey's foundations are now firmly laid").

**Reading.** A "nation-forge" reading from the historian of the Nationalist state, written in the year Chiang's government moved to Chongqing. Compare [[Chiang Kai-shek]]: Jiang's Turkey is the same *civil-service* Turkey, with no mention of a dictator.

**Caveats.** The July 1938 first-edition date comes from a bookseller's blurb (tier J) and is not on the Wikisource page; the Wikisource text carries the later title. Kemal is "基瑪爾" throughout.

## Sources
- 蔣廷黻, 中國近代史大綱 (總論), Chinese Wikisource: [zh.wikisource.org/wiki/中國近代史大綱](https://zh.wikisource.org/wiki/%E4%B8%AD%E5%9C%8B%E8%BF%91%E4%BB%A3%E5%8F%B2%E5%A4%A7%E7%B6%B1) · tier P (transcription)
- 1938 first-edition date: San Min bookstore listing for the 2026 reprint of the "1938年7月初版" Commercial Press edition · tier J
""")

person("Wang Jingwei", role="KMT left-wing leader; later head of the Nanjing collaborationist regime", nat="Chinese", life="1883–1944",
  stance="instrumental in 1927; scornful of the 'Kemal as saviour' idea in 1928",
  tags=["politician", "china", "contemporary", "verified"], body="""
Two Wang Jingwei texts (Chinese Wikisource, from his *Collected Works*) use Kemal as a counter in the KMT split. Neither is an evaluation of Kemal, and both are about China.

**Wuhan, 22 September 1927 — 寧漢合作之經過.** Explaining why the Wuhan and Nanjing wings reunited, Wang says the party must teach cadres *why communism failed elsewhere*: in Germany after the war, in Hungary, in Italy, in Russia (the NEP), and *"其在土耳其，何以經國會拯之於垂危，而基瑪爾仍然驅逐共產黨？"* (my translation: "and in Turkey, why, after the national assembly had rescued it from peril, did Kemal nevertheless expel the Communists?"). Kemal is the **anti-Communist precedent** within an argument that "anti-communism alone does not make a loyal Kuomintang member". Instrumental, intensity 1.

**Letter to the KMT France branch, 7 April 1928 — 覆駐法總支部函** (*Wang Jingwei quanji*, 初集, Shanghai: Sanmin, 1929, pp. 136–157). Wang attacks Wu Zhihui's December 1927 article for flattering the generals; he quotes Wu as saying the party might be handed to the armed comrades because *"幸而有凱馬爾其人，國民黨就算成功，不幸而有張作霖其人，就讓第二個國民黨死"* ("if fortunate there is a Kemal, the Kuomintang counts as a success; if unfortunately a Zhang Zuolin, let the second Kuomintang die"). Wang's own comment on this is on the generals (*"其對於武人呵諛逢惡，一至於此"*, "he panders to the militarists this far"); he does not evaluate Kemal. That makes Wu Zhihui's utterance the gaze (see [[Kemal in the Kuomintang's Quarrels, 1924–1928]]) and Wang its hostile reader.

## Sources
- 汪精衛, 寧漢合作之經過 (speech, Wuhan Political Branch, 22 Sep 1927), Chinese Wikisource: [zh.wikisource.org/wiki/寧漢合作之經過](https://zh.wikisource.org/wiki/%E5%AF%A7%E6%BC%A2%E5%90%88%E4%BD%9C%E4%B9%8B%E7%B6%93%E9%81%8E) · tier P (transcription)
- 汪精衛, 覆駐法總支部函 (7 Apr 1928), in 汪精衛全集 初集 (上海: 三民公司, 1929), pp. 136–157, Chinese Wikisource: [zh.wikisource.org/wiki/覆駐法總支部函](https://zh.wikisource.org/wiki/%E8%A6%86%E9%A7%90%E6%B3%95%E7%B8%BD%E6%94%AF%E9%83%A8%E5%87%BD) · tier P (transcription; edition and pages as given on the page)
""")

person("Fuse Katsuji", role="Japanese journalist (Osaka/Tokyo press), author of a book on Soviet Eastern policy; read in a Chinese translation, 1926", nat="Japanese", life="",
  stance="admiring of the soldier ('雄略'), explanatory about the Russian aid, matter-of-fact about the arrests of Communists",
  tags=["press", "japan", "contemporary", "verified"], body="""
**布施勝治**'s book on Soviet Eastern policy was put into Chinese as **世界赤禍之源泉，俄國東方政策** (Wikisource: author 布施勝治, 1926, translated by the 中華民國聖道會; scan index NLC416-01jh004898-13069 from the National Library of China). Chapter 6, "土耳其革命與俄羅斯" ("The Turkish revolution and Russia", scan pp. 76–88), is the first Japanese journalistic Kemal narrative in this census, and it reached China through an anti-Bolshevik translator.

The shape of the chapter: England's plan to swallow Turkey; Sèvres as "the death-knell"; *"當此危急存亡之秋，於瀕死半月間，遂有英雄出，是爲凱馬爾"* (my translation: "at that hour of crisis, with the half-moon dying, a hero arose, and he was Kemal"). Of the victory of 1921 he says it was owed *"固由凱馬爾之雄略，及土人愛國心"* ("to Kemal's bold strategy and the Turks' patriotism") but that without Russian help the exhausted Turkish army could not have beaten Britain's Greek proxy. Fuse's thesis is Soviet: "Lenin and Kemal shook hands from afar", Russia helped Turkey to independence and democracy and **not** to communism, and he names the price: *"凱馬爾自司米爾納急遽引歸，受保守派之要求，逮捕共產黨員，及其他過激分子，一網打盡"* ("Kemal rushed back from Smyrna and, at the conservatives' demand, arrested the Communists and other extremists in one sweep"; a large part were freed at the Soviet ambassador's request).

**Reading.** Admiration for the general inside an anti-Bolshevik frame: Kemal is useful to Japan and China as the case of a nationalist who could take Soviet help without becoming Soviet. Compare Cai Hesen's December 1922 view of the same arrests in [[Xiangdao Reads Ankara, 1922–1924]].

**Caveats.** The Japanese original is not on Wikisource and was not seen; quotations are from the Chinese rendering (the translator's wording, not Fuse's). The chapter-list entry "凱馬爾之勃興" (*Kemal's rise*) is a section title in the translation.

## Sources
- 布施勝治 (tr. 中華民國聖道會), 世界赤禍之源泉，俄國東方政策, 第六章 土耳其革命與俄羅斯 (1926), Chinese Wikisource: [zh.wikisource.org/wiki/世界赤禍之源泉，俄國東方政策/土耳其革命與俄羅斯](https://zh.wikisource.org/wiki/%E4%B8%96%E7%95%8C%E8%B5%A4%E7%A6%8D%E4%B9%8B%E6%BA%90%E6%B3%89%EF%BC%8C%E4%BF%84%E5%9C%8B%E6%9D%B1%E6%96%B9%E6%94%BF%E7%AD%96/%E5%9C%9F%E8%80%B3%E5%85%B6%E9%9D%A9%E5%91%BD%E8%88%87%E4%BF%84%E7%BE%85%E6%96%AF) · tier P (transcription of the Chinese translation); index page: [zh.wikisource.org/wiki/世界赤禍之源泉，俄國東方政策](https://zh.wikisource.org/wiki/%E4%B8%96%E7%95%8C%E8%B5%A4%E7%A6%8D%E4%B9%8B%E6%BA%90%E6%B3%89%EF%BC%8C%E4%BF%84%E5%9C%8B%E6%9D%B1%E6%96%B9%E6%94%BF%E7%AD%96)
""")

person("Ishiwara Kanji", role="Imperial Japanese Army officer, planner of the Manchurian Incident; strategist of the Tōa Renmei", nat="Japanese", life="1889–1949",
  stance="admiring in passing: Kemal as the rare ruler who held politics and strategy in one person",
  tags=["military", "japan", "posthumous", "verified"], body="""
Ishiwara's **戦争史大観** ("A Panoramic View of War History", Aozora Bunko text) is a lecture first given at Changchun in July 1929, "corrected" at Shinkyō in May 1938 and Kyoto in January 1940, and published in April 1941. In the first part, on how decisive and attritional wars shape the relation of politics and command, he says the ideal is a sovereign who is also the commander and holds both *"政戦両略"* ("politics and strategy") in one person; that has been almost impossible since Frederick the Great and Napoleon:

*"最近に於てはケマル・パシャとか蒋介石、フランコ将軍等は大体それであり、また第二次欧州大戦に於てはヒットラーがそれであるが如くドイツ側から放送されているが、それは将来戦史的に充分検討を要する"* (my translation: "In recent times Kemal Pasha, Chiang Kai-shek and General Franco are more or less this, and in the Second European War Hitler is broadcast from the German side as being it, but that will need thorough examination by future war historians.").

**Reading.** A soldier's one-line placing of Kemal in the *dictator-general* club, with Chiang as a peer. Admiring in the minimal sense (an example of the ideal), hedged about the others. **Dating caveat:** the sentence refers to the Second European War, so it belongs to the 1938–1940 revisions or the 1941 printing, **not** the 1929 lecture. The record is therefore dated 1941 and counted posthumous.

**Boundary.** No Ishiwara text on Turkey from the 1920s was found. The Aozora Bunko holds only three Ishiwara works.

## Sources
- 石原莞爾, 戦争史大観 (lecture Changchun, July 1929; corrected 1938 and 1940; published 8 Apr 1941), Aozora Bunko card 000230, work 55635: [aozora.gr.jp/cards/000230/files/55635_49037.html](https://www.aozora.gr.jp/cards/000230/files/55635_49037.html) · tier P (open-text transcription; the preface dates the publication, and the first-part heading gives the lecture and revision dates)
""")

# ---------------------------------------------------------------- events
E = []

E.append(("Xiangdao Reads Ankara, 1922–1924", "1922–1924", """
The Chinese Communist Party's weekly **嚮導** (*Xiangdao*, "The Guide"; Shanghai, from 13 September 1922) printed, in the very first months of its life, five items that name Kemal, all on Chinese Wikisource.
Together they are the earliest Chinese *political* reading of him in this census, and the only one in which a voice **turns on him** inside three months.

- **Cai Hesen (蔡和森), "祝土耳其國民黨的勝利" ("Congratulations to the Turkish Nationalist Party on its victory"), no. 3, 27 Sept 1922.** The Smyrna victory is hailed as the best model for oppressed peoples: *"最偉大最有革命精神的基瑪爾將軍統率他的國民黨起事於安戈拉"* (my translation: "General Kemal, the greatest and most revolutionary, led his Nationalist Party in revolt at Angora"). Cai's two conditions: stay rooted in the masses, and stay allied with Soviet Russia. China's KMT, he closes, is "in the same position": *what should it think?*
- **君宇, "土耳其國民軍勝利的國際價値" (international value of the Turkish nationalist army's victory), no. 3.** The victory is "not Muslims beating Christians, nor yellow beating white", but an oppressed nation beating imperialism; *"誰都曉得，基瑪爾能有如此成功，是一半得力於蘇俄帮助的緣故"* ("everyone knows Kemal's success is half owed to Soviet help"). The signature is a pen name (conventionally identified as Gao Junyu; M-tier attribution).
- **Cai Hesen, "中德俄三國聯盟…" (4 Oct 1922) and "福建人民當助革命軍復建革命政府" (2 Nov 1922).** Kemal as Sun's template: *"孫中山之爲中華民族獨立運動的革命家，正如基瑪爾之爲土耳其民族獨立運動的革命家而不爲共產主義或「過激主義」運動的革命家一樣"* ("Sun Yat-sen is to the Chinese independence movement what Kemal is to Turkey's: a revolutionary of national independence and **not** of communism or 'extremism'"). It is a defence of Sun against the charge of Bolshevism, using Kemal; the Fujian piece wants China to "set up a revolutionary government as Turkey did" (Canton as Ankara).
- **Unsigned editorial, "國民黨應否復建革命政府", no. 10, 1922.** Replying to Cai, the editors agree that *"我們看見土耳其革命政府的勝利，自然非常欣悅，非常羨慕"* ("seeing the Turkish revolutionary government's victory we are naturally delighted and envious"), but argue Ankara could win because it lay by Russia and out of the imperialists' reach, whereas Canton lies beside Hong Kong. (Likely Chen Duxiu's own hand; not stated.)
- **Cai Hesen, "洛桑會議與土耳其", no. 14, 27 Dec 1922 — the turn.** Lausanne is "the complete loss" of Turkey's victory because Kemal "fell into the French imperialist Bouillon's trick"; *"基瑪爾這種舉動，不但對於共產黨爲罪惡，對於國民運動也爲罪惡，險些兒成了自殺的政策"* ("Kemal's act, the arrest of Communists, is a crime against the Communists and against the national movement too, almost suicide as policy"). He calls Ankara the government of the Turkish **bourgeoisie**, which would drift from Russia when it felt safe, and ends hoping the lesson turns Ankara back to the Soviet side. That is a *conflicted* gaze in the exact sense: admired in September, disowned as class traitor in December.
- **述之 (pen name; conventionally Peng Shuzhi), "我們爲什麽反對國民黨之軍事行動", no. 85, 1924.** In passing, as proof that revolutionary parties win by rooting in the masses: *"我們試看波爾塞維克黨與基馬爾黨之成功"* ("look at the success of the Bolshevik and Kemalist parties"). The same issue run (no. 56, 1924, "土耳其放逐敎主", by 獨秀 / Chen Duxiu) only relays the wire on the abolition of the Caliphate and carries no view, and is therefore not recorded.

**Reading.** The Smyrna victory stirs the Chinese Communists as a *model and a rebuke*, then the arrests of Turkish Communists turn the model into a lesson. Compare [[Sun Yat-sen]], who in 1924 named Turkey but never Kemal and credited Russia; the Xiangdao writers name Kemal repeatedly and say the same thing about Russia.

**Caveats.** Pen-name attributions are the page's (獨秀, 述之, 君宇) or standard identifications. Issue numbers as given on the pages (嚮導/第014期/洛桑會議與土耳其 and similar).

## Sources
- 蔡和森, 祝土耳其國民黨的勝利, 嚮導 no. 3 (27 Sep 1922) — [zh.wikisource.org/wiki/祝土耳其國民黨的勝利](https://zh.wikisource.org/wiki/%E7%A5%9D%E5%9C%9F%E8%80%B3%E5%85%B6%E5%9C%8B%E6%B0%91%E9%BB%A8%E7%9A%84%E5%8B%9D%E5%88%A9) · tier P
- 君宇, 土耳其國民軍勝利的國際價値, 嚮導 no. 3 (1922) — [zh.wikisource.org/wiki/土耳其國民軍勝利的國際價値](https://zh.wikisource.org/wiki/%E5%9C%9F%E8%80%B3%E5%85%B6%E5%9C%8B%E6%B0%91%E8%BB%8D%E5%8B%9D%E5%88%A9%E7%9A%84%E5%9C%8B%E9%9A%9B%E5%83%B9%E5%80%BC) · tier P
- 蔡和森, 中德俄三國聯盟與國際帝國主義及陳炯明之反動 (4 Oct 1922) — [zh.wikisource.org/wiki/中德俄三國聯盟與國際帝國主義及陳炯明之反動](https://zh.wikisource.org/wiki/%E4%B8%AD%E5%BE%B7%E4%BF%84%E4%B8%89%E5%9C%8B%E8%81%AF%E7%9B%9F%E8%88%87%E5%9C%8B%E9%9A%9B%E5%B8%9D%E5%9C%8B%E4%B8%BB%E7%BE%A9%E5%8F%8A%E9%99%B3%E7%82%AF%E6%98%8E%E4%B9%8B%E5%8F%8D%E5%8B%95) · tier P
- 蔡和森, 福建人民當助革命軍復建革命政府 (2 Nov 1922) — [zh.wikisource.org/wiki/福建人民當助革命軍復建革命政府](https://zh.wikisource.org/wiki/%E7%A6%8F%E5%BB%BA%E4%BA%BA%E6%B0%91%E7%95%B6%E5%8A%A9%E9%9D%A9%E5%91%BD%E8%BB%8D%E5%BE%A9%E5%BB%BA%E9%9D%A9%E5%91%BD%E6%94%BF%E5%BA%9C) · tier P
- 國民黨應否復建革命政府, 嚮導 no. 10 (1922) — [zh.wikisource.org/wiki/國民黨應否復建革命政府](https://zh.wikisource.org/wiki/%E5%9C%8B%E6%B0%91%E9%BB%A8%E6%87%89%E5%90%A6%E5%BE%A9%E5%BB%BA%E9%9D%A9%E5%91%BD%E6%94%BF%E5%BA%9C) · tier P
- 蔡和森, 洛桑會議與土耳其, 嚮導 no. 14 (27 Dec 1922) — [zh.wikisource.org/wiki/洛桑會議與土耳其](https://zh.wikisource.org/wiki/%E6%B4%9B%E6%A1%91%E6%9C%83%E8%AD%B0%E8%88%87%E5%9C%9F%E8%80%B3%E5%85%B6) · tier P
- 述之, 我們爲什麽反對國民黨之軍事行動, 嚮導 no. 85 (1924) — [zh.wikisource.org/wiki/我們爲什麽反對國民黨之軍事行動](https://zh.wikisource.org/wiki/%E6%88%91%E5%80%91%E7%82%BA%E4%BB%80%E9%BA%BD%E5%8F%8D%E5%B0%8D%E5%9C%8B%E6%B0%91%E9%BB%A8%E4%B9%8B%E8%BB%8D%E4%BA%8B%E8%A1%8C%E5%8B%95) · tier P
- 獨秀, 土耳其放逐敎主, 嚮導 no. 56 (1924) — [zh.wikisource.org/wiki/土耳其放逐敎主](https://zh.wikisource.org/wiki/%E5%9C%9F%E8%80%B3%E5%85%B6%E6%94%BE%E9%80%90%E6%95%8E%E4%B8%BB) · tier P (context only)
"""))

E.append(("Kemal in the Kuomintang's Quarrels, 1924–1928", "1924–1928", """
Once the KMT was in power, Kemal stopped being a distant liberator and became a *label thrown in factional fights*. Four short voices, all on Chinese Wikisource, show it.

- **KMT Canton Municipal Special Party Branch, youth members' congress, 20 July 1924.** Praising Sun Yat-sen in a manifesto: *"以較俄羅斯之列寧、土耳其之凱末爾，我們實覺其無消遜色"* (my translation: "compared with Russia's Lenin and Turkey's Kemal, we feel he is in no way inferior"). And: had the nation rallied behind him, China "would not now look with envy to Russia and Turkey". Kemal as a benchmark of greatness and an object of envy at once, and a 1924 sequel to [[Xiangdao Reads Ankara, 1922–1924]]. (Hedged: "消遜" appears so in the transcription.)
- **"湖北一黨員" (a Hubei party member), "共產黨打倒之湖北", Chinese KMT Weekly, 1926.** A right-winger attacking the Communists in Hubei, claiming that the Northern Expedition is fought for Sun Yat-sen's doctrine, not Lenin's, and that after victory *"土耳其基瑪爾將軍之舉措，共產黨是最怕不過的"* ("what General Kemal did in Turkey is what the Communists fear most"). Kemal's expulsion of Communists as the anti-Red **model**; instrumental. The page cites the periodical's PDF file name as 1926, vol. 2 no. 6; the author is pseudonymous.
- **Wu Zhihui (吳敬恆/稚暉), December 1927, via Wang Jingwei's letter of 7 April 1928.** Wang quotes Wu's article "讀了汪先生的兩件大事": if the party must be handed to the generals, *"幸而有凱馬爾其人，國民黨就算成功，不幸而有張作霖其人，就讓第二個國民黨死"* ("if fortunately there is a Kemal, the Kuomintang counts as a success; if unfortunately a Zhang Zuolin, let a second Kuomintang die"). Kemal is the **good strongman** against whom the warlord is measured. Wang Jingwei, who is quoting it to show Wu panders to militarists, is the hostile reader ([[Wang Jingwei]]). Second-hand: the article itself was not seen.
- **"小白", "敬告國人莫被蔣介石所惑" ("Warning: do not be taken in by Chiang Kai-shek"), June 1927.** An anti-Chiang tract (the page cites a Canadiana scan, `sfu.00001_19270620`) says Chiang has turned against the Communists not out of principle but over power; his April speech means *"豈非明明欲做土耳其之基瑪爾。意大利之蒙梭利尼。爲個人軍事獨裁之專制政體乎"* (my translation: "does it not plainly mean he wants to be Turkey's Kemal, Italy's Mussolini, a one-man military dictatorship?"). The target is Chiang. Kemal is simply the name for the **personal military dictator**. This is the earliest Chinese text in the census that uses him that way, and its Kemal is a hostile type, not a study.

**Reading.** Between 1924 and 1928 the same name moves from benchmark (Canton youth), to anti-Communist template (Hubei right), to the strongman the party might need (Wu), to the dictator the Left fears Chiang will become (the tract). It is the same man read from four chairs, and a pre-echo of how [[Chiang Kai-shek]] would later be written about as Kemal's Chinese student.

**Caveats.** Four voices of different weight; "小白" and "湖北一黨員" are pseudonyms; Wu is second-hand. The Hubei and "小白" texts are Wikisource transcriptions of periodicals and a pamphlet whose editions are cited only by file name.

## Sources
- 中國國民黨廣州市特別黨部青年黨員大會宣言 (20 Jul 1924, 民國十三年七月二十日) — [zh.wikisource.org/wiki/中國國民黨廣州市特別黨部青年黨員大會宣言](https://zh.wikisource.org/wiki/%E4%B8%AD%E5%9C%8B%E5%9C%8B%E6%B0%91%E9%BB%A8%E5%BB%A3%E5%B7%9E%E5%B8%82%E7%89%B9%E5%88%A5%E9%BB%A8%E9%83%A8%E9%9D%92%E5%B9%B4%E9%BB%A8%E5%93%A1%E5%A4%A7%E6%9C%83%E5%AE%A3%E8%A8%80) · tier P
- 湖北一黨員, 共產黨打倒之湖北, 中國國民黨週刊 1926 — [zh.wikisource.org/wiki/共產黨打倒之湖北](https://zh.wikisource.org/wiki/%E5%85%B1%E7%94%A2%E9%BB%A8%E6%89%93%E5%80%92%E4%B9%8B%E6%B9%96%E5%8C%97) · tier P
- 汪精衛, 覆駐法總支部函 (7 Apr 1928), 汪精衛全集 初集 (1929), pp. 136–157 — [zh.wikisource.org/wiki/覆駐法總支部函](https://zh.wikisource.org/wiki/%E8%A6%86%E9%A7%90%E6%B3%95%E7%B8%BD%E6%94%AF%E9%83%A8%E5%87%BD) · tier P (Wu's words second-hand)
- 小白, 敬告國人莫被蔣介石所惑 (June 1927) — [zh.wikisource.org/wiki/敬告國人莫被蔣介石所惑](https://zh.wikisource.org/wiki/%E6%95%AC%E5%91%8A%E5%9C%8B%E4%BA%BA%E8%8E%AB%E8%A2%AB%E8%94%A3%E4%BB%8B%E7%9F%B3%E6%89%80%E6%83%91) · tier P
"""))

E.append(("Kemal as a Chinese Yardstick, 1933–1940", "1933–1940", """
Three further Wikisource texts show how Kemal worked as a *measure* in the decade of defeat and war, from three social positions. Next to [[Hu Shi]] (1933) and [[Jiang Tingfu]] (1938):

- **Funeral couplet for Chen Jiongming, 1933.** Chen (the Cantonese warlord-federalist who had broken with Sun) died in September 1933; the *Chen Gong Jingcun Rongailu* (陳公競存榮哀錄) prints the couplets sent by mourners. The Shanghai No. 1 Branch of the 中國致公黨 sent one in which Kemal and Hitler are the dictators Chen refused to be: *"政治不主獨裁凱末爾豈可作"* and, on the other line, *"希德婁何足云"* (my translation, tentative since couplets are elliptical: "in politics he did not favour dictatorship, how could he have been a Kemal?" and "what is Hitler worth mentioning?"). The couplet before it, from the Cuba branch, invokes Mussolini. Kemal belongs here to a **list of 1930s strongmen**, not as a hero.
- **Chen Jitang, Istanbul, Dec 1936–Jan 1937 (memoir).** The Guangdong strongman, on a tour of Europe that ended in the Xi'an Incident, passes through Turkey after Bulgaria: *"但在凯末尔实行革命后，一切均有改革进步。人民禁用包头巾，违者拘禁，可见其政令之严。惟工业仍不发达，失业者甚多，到处可见乞丐"* (my translation: "but since Kemal carried out his revolution everything has been reformed and has advanced. People are forbidden headscarves on pain of arrest, which shows how strict his decrees were. Yet industry is still undeveloped, many are unemployed and beggars are everywhere."). A one-paragraph, mixed, soldier's-eye verdict (improvement, rigour, poverty). The *Autobiography Draft* text is dated 1974 on Wikisource, written long after the visit; the account is a memoir and the visit dates are placed from its context (the Xi'an Incident, 12 December 1936).
- **Chiang Kai-shek, National Day message, 10 October 1940.** Chiang's *Double Ten* address to the army and people lists the models of "national construction through hardship": the USA's eight-year war, Soviet Russia, and *"再說土耳其的復興…凱末爾奮起救國，也是在國家疆土日蹙，經濟力量日衰，軍隊解體，内政散漫之中，衝破空前的艱難，領導軍民，堅苦作戰，收復失地，達到土耳其的解放。此後更盡瘁於建國建軍，厲行種種改革，黽勉十年，方完成復興之偉業。這種堅毅奮發，苦幹實幹的精神，都應爲我們所效法"* (my translation: "And again Turkey's revival: Kemal rose to save the country amid shrinking territory, falling economic strength, a dissolving army and disorder at home; he broke through unprecedented difficulties, led soldiers and people in hard fighting, recovered lost land and achieved Turkey's liberation. After that he spent himself on building the state and army, and pressed through all manner of reforms, labouring ten years before the work of revival was complete. This spirit of resolute, strenuous and practical effort is what we should emulate.") This is a first-hand Chiang text, where the existing [[Chiang Kai-shek]] note reports his study programme at second hand. Chiang here draws the Turkish moral for China's war of resistance; note that he names the *ten years of building* after the war. Posthumous (two years after Kemal's death); recorded under the existing Chiang node.

**Passing mention, not recorded.** Lu Xun, in "奇怪（一）" (*Huabian wenxue*, 14 Aug 1934), jokes that a gas-mask scheme to separate men and women would be even better than *"凱末爾將軍治國以前的土耳其女人的面幕"* ("the veils of Turkish women before General Kemal ruled"). No view of Kemal; context only.

## Sources
- 陳公競存榮哀錄/輓章 (1933), Chinese Wikisource (transclusion of the scan 陳公競存榮哀錄.pdf, pp. 18–66): [zh.wikisource.org/wiki/陳公競存榮哀錄/輓章](https://zh.wikisource.org/wiki/%E9%99%B3%E5%85%AC%E7%AB%B6%E5%AD%98%E6%A6%AE%E5%93%80%E9%8C%84/%E8%BC%93%E7%AB%A0) · tier P (transcription; the year of Chen's death is general knowledge, M)
- 陈济棠, 陈济棠自传稿 (page year 1974): [zh.wikisource.org/wiki/陈济棠自传稿](https://zh.wikisource.org/wiki/%E9%99%88%E6%B5%8E%E6%A3%A0%E8%87%AA%E4%BC%A0%E7%A8%BF) · tier P (memoir, late)
- 蔣中正, 中華民國二十九年國慶紀念吿全國軍民書 (10 Oct 1940): [zh.wikisource.org/wiki/中華民國二十九年國慶紀念吿全國軍民書](https://zh.wikisource.org/wiki/%E4%B8%AD%E8%8F%AF%E6%B0%91%E5%9C%8B%E4%BA%8C%E5%8D%81%E4%B9%9D%E5%B9%B4%E5%9C%8B%E6%85%B6%E7%B4%80%E5%BF%B5%E5%90%BF%E5%85%A8%E5%9C%8B%E8%BB%8D%E6%B0%91%E6%9B%B8) · tier P (transcription)
- 魯迅, 奇怪（一）, 花邊文學 (14 Aug 1934): [zh.wikisource.org/wiki/奇怪（一）](https://zh.wikisource.org/wiki/%E5%A5%87%E6%80%AA%EF%BC%88%E4%B8%80%EF%BC%89) · tier P (context only)
"""))

for name, when, body in E:
    note("Events", name, {"type": "event", "when": when, "tags": ["event", "verified", "china", "contemporary"]}, body)
