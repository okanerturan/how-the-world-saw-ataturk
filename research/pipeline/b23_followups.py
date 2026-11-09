# -*- coding: utf-8 -*-
# Census follow-ups (3 Nov 2026), done by the main agent on the human/browser queue.
# Seam: archive.org full-text search (services/search/beta/page_production/?service_backend=fts) returns
# highlighted snippets from lending-only books without a login; open DLI/mbp scans give full djvu text.
# Records: Emil Ludwig 1930 (Neue Freie Presse interview, via the 1991 reprint, snippets only),
# Emil Ludwig 1942 (The Mediterranean, p. 548, open scan), Pope Benedict XVI 2006 (Anıtkabir book, two press reports).
# Writes tools/.state/followups/gazes_followups.jsonl and rewrites the inherited Emil Ludwig note with sources.
import json, os
from _lib import person

HERE = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(HERE, "tools", ".state", "followups")
os.makedirs(STATE, exist_ok=True)

LUD30 = "https://archive.org/details/furdieweimarerre0000ludw"
LUD42 = "https://archive.org/details/mediterraneansag027841mbp"
DW = "https://dw.com/en/popes-trip-to-turkey-starts-on-conciliatory-note/a-2251303"
AN = "https://asianews.it/news-en/Dialogue-between-Christians-and-Muslims-is-a-vital-necessity,-says-Pope-7875.html"

R = [
    {"id": "emil-ludwig-1930-03-09", "voice": "Emil Ludwig", "voice_type": "person",
     "role": "German biographer, interviewer of the era's dictators", "country": "Germany", "country_now": "Germany",
     "domain": "press", "date": "1930-03-09", "era": "contemporary", "mirror": None, "polarity": "conflicted", "intensity": 2,
     "what_they_saw": "A cold rationalist beside whom Napoleon seems half a dreamer; sincerely wants to be a democrat, 'and yet he is a dictator'.",
     "quote": "Ein Mann, neben dem Napoleon als halber Träumer erscheint, national, mißtrauisch gegen alle anderen Völker, besessen von einer einzigen Idee, zugleich ihr Diener und ihr Herr, verachtet der Gasi alle Motive, die sich in Zahlen nicht ausdrücken lassen",
     "artifact": "article", "evidence": "P", "mediated_by": None,
     "caveat": "[translation] 'A man beside whom Napoleon appears half a dreamer, national, mistrustful of all other peoples, possessed by a single idea, at once its servant and its master, the Ghazi despises every motive that cannot be expressed in numbers.' 'Besuch bei Mustafa Kemal', Neue Freie Presse (Vienna), 9 March 1930, pp. 2 and 4 (read on the ANNO page image of p. 2, 4 Nov 2026, via a headed browser that passed ANNO's automatic check). Same page, section 'Der Diktator als Vollstrecker des Volkswillens': 'Ja, Kemal hat zum Demokraten das Streben und die Ueberzeugung, es zu sein. … Und doch ist er Diktator.' Also: 'der Gasi ist der Mann ohne Phantasie, das stilisiert er, darauf ist er stolz' (via the 1991 reprint, Für die Weimarer Republik und Europa, pp. 181–187). Contrast Ludwig's 1942 portrait of a 'blue, dreamy gaze' with 'a touch of the poet'.",
     "node": "Emil Ludwig", "sources": ["https://anno.onb.ac.at/cgi-content/anno?aid=nfp&datum=19300309&seite=2", LUD30]},
    {"id": "emil-ludwig-1942", "voice": "Emil Ludwig", "voice_type": "person",
     "role": "German biographer, interviewer of the era's dictators", "country": "Germany", "country_now": "Germany",
     "domain": "letters", "date": "1942", "era": "posthumous", "mirror": "modernization-poster-child", "polarity": "admiring", "intensity": 3,
     "what_they_saw": "Kemal 'towers above the dictators of our day': he smashed Sèvres, freed women from the harem, and deposed the caliph without taking his place.",
     "quote": "No new government attracted the admiration of the world immediately after the First World War so much as Turkey under Kemal Pasha, who towers above the dictators of our day.",
     "artifact": "book", "evidence": "P", "mediated_by": None,
     "caveat": "Emil Ludwig, The Mediterranean: Saga of a Sea (Whittlesey House/McGraw-Hill, 1942), pp. 548–549, open archive.org scan mediterraneansag027841mbp (running head '548 ] KEMAL PASHA'). Same passage: he describes Kemal 'from personal acquaintance' with 'a blue, dreamy gaze that betrayed a touch of the poet'; freeing women 'would be enough in itself to immortalize him'; 'the new, enlightened despot and lawgiver'; and 'the thing that proved his courageous genius above all was the fact that he deposed the caliph without putting himself in his place'. He also calls the 1923 Greek-Turkish population exchange, 'painful though it be', a success — his framing, not the census's.",
     "node": "Emil Ludwig", "sources": [LUD42]},
    {"id": "benedict-xvi-2006-11-28", "voice": "Pope Benedict XVI", "voice_type": "person",
     "role": "Pope; visit to Anıtkabir on his apostolic journey to Turkey", "country": "Vatican City", "country_now": "Vatican City",
     "domain": "religion", "date": "2006-11-28", "era": "posthumous", "mirror": None, "polarity": "instrumental", "intensity": 1,
     "what_they_saw": "In the Anıtkabir book, adopts the founder's 'peace at home, peace in the world' as his own wish for a bridge between religions.",
     "quote": "I gladly make my own the words of the founder of the Turkish Republic: I wish 'peace at home, peace in the world'",
     "artifact": "quote", "evidence": "J", "mediated_by": "AsiaNews and Deutsche Welle reports of the Anıtkabir book entry, 28 Nov 2006",
     "caveat": "Courtesy text on a visit that followed the Regensburg speech controversy. Wording varies between reports: AsiaNews 'In this land, meeting place and crossroads of different religions and cultures, hinge between Asia and Europe, I gladly make my own the words of the founder of the Turkish Republic'; DW 'I am pleased to adopt the words of the founder of the Turkish republic as my own'; Zenit (relayed) says he wrote in English. Atatürk is not named, only 'the founder'. Pope Francis (2014) and Pope Leo XIV (2025) signed the same book without mentioning Atatürk.",
     "node": "Pope Benedict XVI", "sources": [AN, DW]},
    {"id": "zahir-shah-1938-11-11", "voice": "Mohammed Zahir Shah", "voice_type": "person",
     "role": "King of Afghanistan; telegram to Abdülhalik Renda, President of the Grand National Assembly", "country": "Afghanistan", "country_now": "Afghanistan",
     "domain": "diplomacy", "date": "1938-11-11", "era": "funeral", "mirror": None, "polarity": "admiring", "intensity": 1,
     "what_they_saw": "Beyond the condolence formula: Atatürk's distinguished services to the noble Turkish nation will never be forgotten, and his foundations of progress endure.",
     "quote": "[translation] the distinguished services which he rendered to the noble Turkish nation will, God willing, never be forgotten by young and old of that brotherly nation",
     "artifact": "telegram", "evidence": "P", "mediated_by": None,
     "caveat": "Persian typed in Latin letters, Kabul 11/11/38 16:30 via radio, received Ankara; TBMM condolence volume II (handle 11543/2467), PDF p. 39 (stamped 36). Telegraphic transliteration as typed (words run together): 'khedamatebarguzida hamelatenajibe turkiakardast inshallahaz nazarekhord wabuzurgeanmelate beradarfaramosh nashudaniast' (= khedamat-e barguzida … ba millat-e najib-e Turkia karda ast, inshallah az nazar-e khord wa buzurg-e an millat-e baradar faramush-nashudani ast). Also: 'mutainetaraqi wataali' (solid foundations of progress and elevation) left by the late Atatürk, and 'we count the grief of our Turkish brothers as our own'. Signed 'mohdzahidshah padshahe afghanistan'. Read from the page image by the main agent (3 Nov 2026); the transliteration is uncertain in places, the quoted clause is clear.",
     "node": "Condolence Telegrams to Ankara, November 1938", "sources": ["https://acikerisim.tbmm.gov.tr/handle/11543/2467"]},
    {"id": "terada-torahiko-1924", "voice": "Terada Torahiko", "voice_type": "person",
     "role": "Japanese physicist and essayist (Tokyo Imperial University)", "country": "Japan", "country_now": "Japan",
     "domain": "science", "date": "1924", "era": "contemporary", "mirror": None, "polarity": "admiring", "intensity": 1,
     "what_they_saw": "Amid the US anti-Japanese exclusion crisis, holds up Kemal Pasha as a great man: heroes never die out in any age.",
     "quote": "ケマルパシャなんか偉いものだ。いつの世になっても英雄は絶えないな。",
     "artifact": "quote", "evidence": "S", "mediated_by": "Nakaya Ukichirō, 'Sensei o meguru hanashi', section 28 'Hainichi mondai', first printed in Torahiko kenkyū no. 8 (Terada Torahiko zenshū vol. 14 supplement, Iwanami, 13 May 1937)",
     "caveat": "[translation] 'Now Kemal Pasha, there's a great man. Heroes never die out, in any age.' Spoken by Terada (d. 1935) to his students and recalled by his pupil, the physicist Nakaya Ukichirō; the remark belongs to the time 'when the anti-Japanese question was much discussed' (the 1924 US Immigration Act), so dated c. 1924. Same passage: national independence needs 'positive morality' rather than 'do-nothing-ism'. Text: Aozora Bunko card 57460 (base text Nakaya Ukichirō shū vol. 1, Iwanami 2000), found by grepping the aozorabunko_text mirror (3 Nov 2026).",
     "node": "Terada Torahiko", "sources": ["https://www.aozora.gr.jp/cards/001569/card57460.html"]},
    {"id": "rodney-adamson-1943-07-01", "voice": "Rodney Adamson", "voice_type": "person",
     "role": "Progressive Conservative MP for York West, Canadian House of Commons", "country": "Canada", "country_now": "Canada",
     "domain": "politics", "date": "1943-07-01", "era": "posthumous", "mirror": "emancipator-patriarch", "polarity": "conflicted", "intensity": 2,
     "what_they_saw": "An absolute dictator like Hitler and Mussolini, yet unlike them an emancipator of women, which made Turkey advancing and peaceable.",
     "quote": "In every way he was an absolute dictator, just as much a dictator as the dictators of Germany and Italy. But he had a different idea from them about the emancipation of women.",
     "artifact": "speech", "evidence": "P", "mediated_by": None,
     "caveat": "House of Commons Debates, 19th Parliament, 4th Session, 1 July 1943, p. 4245 (War Appropriation—Labour, on wartime day nurseries); read on the page image at Canadiana (oop.debates_HOC1904_04, image 1129) by the main agent, 4 Nov 2026. Continues: 'He did not believe that woman's part was kirchen, kuchen, kindern, as Hitler did, and to-day we find as a consequence that Turkey is an advancing, go-ahead country that is capable of living at peace with its neighbours.' Speaker identified as 'Mr. ADAMSON' by LiPaD (the speech runs on from p. 4244). Found through LiPaD search results supplied by Okan (LiPaD sits behind an interactive Cloudflare check). Other LiPaD hits (Stockwell Day 2004, Nicholls 2013, Assadourian 2001, Reed 1999, Genuis 2015) state no view of Atatürk.",
     "node": "Rodney Adamson", "sources": ["https://parl.canadiana.ca/view/oop.debates_HOC1904_04/1129", "https://www.lipad.ca/search/?q=ataturk"]},
    {"id": "john-m-kelly-1983-11-30", "voice": "John M. Kelly", "voice_type": "person",
     "role": "Fine Gael TD for Dublin South-Central, constitutional lawyer and former Attorney General", "country": "Ireland", "country_now": "Ireland",
     "domain": "politics", "date": "1983-11-30", "era": "posthumous", "mirror": "modernization-poster-child", "polarity": "conflicted", "intensity": 1,
     "what_they_saw": "Turkey's 'great leader' forced Westernisation to end its peripherality: script, veils and fezes scrapped, 'a brutal thing to do to people'.",
     "quote": "The Turks were under the disadvantages, as their great leader, Ataturk, saw it, of being culturally and economically peripheral to Europe. He made them scrap the Arabic writing which they used for their language, he made them scrap their veils and their fezes, making them dress like western Europeans. That was, I suppose, a brutal thing to do to people.",
     "artifact": "speech", "evidence": "S", "mediated_by": "Database of Parliamentary Speeches in Ireland, 1919–2013 (Herzog and Mikhaylov, Harvard Dataverse doi:10.7910/DVN/6MZN76), speechID 2109508, a transcription of the Dáil official report",
     "caveat": "Dáil Éireann, Export Promotion (Amendment) Bill, 1983: Second Stage (Resumed), 30 Nov 1983, col. after 661. He offers Japan and Turkey as models of nations that broke with tradition to sell to the world. The official report on oireachtas.ie sits behind an interactive human-verification check and was not opened, so evidence S. Other Dáil hits in the dataset state no view: Lynch 1973 and Ahern 2003 (a wreath), a 1922 speech on refusing to fight 'the war of the oil owners against Kemal Pasha' (attributed in the dataset to Cosgrave, doubtfully), Kelly 1987 ('isolated as the Turks were before Ataturk'), Higgins 1991 (an ironic comparison), Broughan 2003 (an attributed promise).",
     "node": "John M. Kelly", "sources": ["https://doi.org/10.7910/DVN/6MZN76"]},
    {"id": "billy-hughes-1922-09-29", "voice": "Billy Hughes", "voice_type": "person",
     "role": "Prime Minister of Australia", "country": "Australia", "country_now": "Australia",
     "domain": "politics", "date": "1922-09-29", "era": "contemporary", "mirror": None, "polarity": "hostile", "intensity": 1,
     "what_they_saw": "In the Chanak crisis, warns Mustapha Kemal not to forget what Australia's entry into war means, while wanting 'a fair deal' for the Turks.",
     "quote": "We are for peace, and we want the Turks to have a fair deal, but if war is to come Mustapha Kemal must not forget what the entry into war by Australia means.",
     "artifact": "quote", "evidence": "J", "mediated_by": "Australian press wire, Melbourne 29 Sept 1922: 'Menace to Kemal', Kalgoorlie Miner 30 Sept 1922, p. 5 (Trove 93229155); same statement summarised in The Register (Adelaide) 30 Sept 1922, p. 11, 'Kemal Must Look Out' (Trove 64124806)",
     "caveat": "Said to reporters after the House of Representatives adjourned, amplifying his statement in the House that day; the preceding sentence: 'We shall do so again, if necessity arises, and it will be well if Mustapha Kemal remembers this.' In the House he also said 'Australia had no bias against Kemal' and that the Allies 'could yield nothing to force, but everything to reason' (The Register's report). Read on Trove via a headed browser, 4 Nov 2026. A deterrent warning to an adversary, so polarity hostile at intensity 1; Commonwealth Hansard for 29 Sept 1922 not read.",
     "node": "Billy Hughes", "sources": ["https://trove.nla.gov.au/newspaper/article/93229155", "https://trove.nla.gov.au/newspaper/article/64124806"]},
]
for r in R:
    assert len(r["what_they_saw"].split()) <= 25, r["id"]
with open(os.path.join(STATE, "gazes_followups.jsonl"), "w", encoding="utf-8") as f:
    for r in R:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

person("Emil Ludwig", role="Biographer", nat="German-Jewish", life="1881–1948",
       stance="interviewer, later admirer", tags=["observer", "literary", "verified"],
       body="""The most famous biographer of the 1920s–30s (*Napoleon*, *Bismarck*), known for long interviews with
Mussolini and Stalin. He visited Mustafa Kemal in Ankara and wrote it up as "Besuch bei Mustafa Kemal" for the
Vienna *Neue Freie Presse* of 9 March 1930. The text, read here only in search snippets of a 1991 reprint, paints
the Ghazi as a cold rationalist: "Ein Mann, neben dem Napoleon als halber Träumer erscheint … verachtet der Gasi
alle Motive, die sich in Zahlen nicht ausdrücken lassen" (a man beside whom Napoleon seems half a dreamer); he
"styles himself" a man without imagination; he sincerely wants to be a democrat, "Und doch ist er Diktator".

Twelve years later, in exile, the portrait had softened into legend. In *The Mediterranean* (1942) Kemal
"towers above the dictators of our day", has "a blue, dreamy gaze that betrayed a touch of the poet", freed
women in a deed "far more revolutionary than anything achieved for women's suffrage in the West", and proved
"his courageous genius" by deposing the caliph "without putting himself in his place". The same man, two
mirrors: the cold engineer of 1930 and the poet-lawgiver of 1942.

The inherited version of this note (from the source transcript) said Ludwig compared Atatürk to Napoleon. The 1930
text does, but the other way round from the legend: beside Kemal, Napoleon looks "half a dreamer"; the "knew where to
stop" gloss is not in it.
Compare [[W.B. Yeats]].

## Sources
- Emil Ludwig, "Besuch bei Mustafa Kemal", *Neue Freie Presse*, 9 Mar 1930, pp. 2, 4 (ANNO page image read); reprinted in *Für die Weimarer Republik und Europa* (Peter Lang, 1991), pp. 181–187 (archive.org furdieweimarerre0000ludw, full-text-search snippets).
- Emil Ludwig, *The Mediterranean: Saga of a Sea* (Whittlesey House, 1942), pp. 548–549 (archive.org mediterraneansag027841mbp, open).
""")

person("Pope Benedict XVI", role="Pope (2005–2013)", nat="German", life="1927–2022",
       stance="courtesy", tags=["religion", "visitor", "verified"],
       body="""On 28 November 2006, two months after his Regensburg lecture had angered much of the Muslim world, Benedict
XVI began his Turkey journey at Anıtkabir. In the special book he wrote that in this land, "meeting place and
crossroads of different religions and cultures", he gladly made "my own the words of the founder of the Turkish
Republic": "peace at home, peace in the world". He does not name Atatürk; the founder's maxim is borrowed as a
bridge. Angelo Roncalli, apostolic delegate in Istanbul in the 1930s, later became [[Pope John XXIII]]. His successors Francis
(2014) and Leo XIV (2025) signed the same book without mentioning Atatürk. See [[Mustafa Kemal Atatürk]].

## Sources
- AsiaNews, 28 Nov 2006, "Dialogue between Christians and Muslims is a vital necessity, says Pope" (asianews.it, art. 7875).
- Deutsche Welle, 28 Nov 2006, "Pope's trip to Turkey starts on conciliatory note" (dw.com a-2251303).
""")
person("Terada Torahiko", role="Physicist and essayist", nat="Japanese", life="1878–1935",
       stance="admirer (in passing)", tags=["scientist", "writer", "verified"],
       body="""Physicist at Tokyo Imperial University and one of the most loved essayists of modern Japan. His pupil Nakaya
Ukichirō, later famous for his work on snow crystals, recorded his table talk in "Sensei o meguru hanashi" (1936–37). When
the anti-Japanese exclusion question was in the air (the 1924 US Immigration Act), Terada told his students that Japan's
independence needed great scholars and "positive morality", and added: "ケマルパシャなんか偉いものだ。いつの世になっても英雄は
絶えないな。" ("Now Kemal Pasha, there's a great man. Heroes never die out, in any age."). Compare [[Ishiwara Kanji]].

## Sources
- Nakaya Ukichirō, "Sensei o meguru hanashi", §28, *Torahiko kenkyū* no. 8 (Iwanami, 13 May 1937); Aozora Bunko card 57460.
""")
person("Rodney Adamson", role="Canadian MP (Progressive Conservative, York West)", nat="Canadian", life="1901–1954",
       stance="conflicted (1943)", tags=["politics", "canada", "verified", "hansard"],
       body="""Agar Rodney Adamson, Conservative member for York West, argued in the Commons on 1 July 1943 for state-run wartime
nurseries and held up Turkey as proof that "the civilization of any country is in direct ratio with the emancipation of
its women": Atatürk "was an absolute dictator, just as much a dictator as the dictators of Germany and Italy", but unlike
Hitler he rejected "kirchen, kuchen, kindern". See [[Mustafa Kemal Atatürk]].

## Sources
- House of Commons Debates (Canada), 1 July 1943, p. 4245 (Canadiana, oop.debates_HOC1904_04, image 1129).
""")
person("John M. Kelly", role="Irish constitutional lawyer and Fine Gael politician", nat="Irish", life="1931–1991",
       stance="conflicted (1983)", tags=["politics", "ireland", "verified"],
       body="""John Maurice Kelly, author of *The Irish Constitution* and Attorney General (1977), told the Dáil on 30 November 1983 that
Turkey's "great leader, Ataturk" had forced his people out of their peripherality to Europe, scrapping script, veils and
fezes: "That was, I suppose, a brutal thing to do to people." See [[Mustafa Kemal Atatürk]].

## Sources
- Dáil Éireann, 30 Nov 1983 (Export Promotion (Amendment) Bill), via the Database of Parliamentary Speeches in Ireland (Harvard Dataverse, doi:10.7910/DVN/6MZN76), speechID 2109508.
""")
person("Billy Hughes", role="Prime Minister of Australia (1915–1923)", nat="Australian", life="1862–1952",
       stance="hostile (1922)", tags=["politics", "australia", "verified"],
       body="""Australia's wartime Prime Minister answered Lloyd George's Chanak appeal in September 1922 by backing Britain and
warning the Turkish leader: "it will be well if Mustapha Kemal remembers this … if war is to come Mustapha Kemal must not
forget what the entry into war by Australia means", while telling the House that "Australia had no bias against Kemal".
See [[Mustafa Kemal Atatürk]] and [[David Lloyd George]].

## Sources
- Kalgoorlie Miner, 30 Sept 1922, p. 5, "Menace to Kemal" (Trove 93229155); The Register (Adelaide), 30 Sept 1922, p. 11 (Trove 64124806).
""")
print("followups: %d records" % len(R))
