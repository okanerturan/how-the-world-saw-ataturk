# -*- coding: utf-8 -*-
# Census round 25 (4 Nov 2026) — the Anıtkabir special book, 2003–2007, read on the page images
# published by ataturkarsivi.com/pages/anitkabir (scans of the printed compilation "Anıtkabir Özel Defteri":
# each entry's handwritten original beside the compilation's typeset Turkish). Read by the main agent.
import json, os
from _lib import note, person

HERE = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(HERE, "tools", ".state", "round25")
os.makedirs(STATE, exist_ok=True)
NODE = "Anıtkabir Special Book, 2003–2007 — Vajpayee, Olmert, Katsav, Verhofstadt, Balkenende and Others"
SRC = "https://ataturkarsivi.com/pages/anitkabir"
BOOK = ("Anıtkabir Özel Defteri (printed compilation, '1953'ten günümüze Anıtkabir'i ziyaret eden yerli ve yabancı heyet "
        "başkanlarının Atatürk hakkındaki duygu ve düşünceleri'), page images on ataturkarsivi.com")

def rec(i, voice, role, c, date, pol, inten, saw, q, cav, mirror=None, ev="P"):
    return {"id": i, "voice": voice, "voice_type": "person", "role": role, "country": c, "country_now": c,
            "domain": "politics", "date": date, "era": "posthumous", "mirror": mirror, "polarity": pol,
            "intensity": inten, "what_they_saw": saw, "quote": q, "artifact": "quote", "evidence": ev,
            "mediated_by": None, "caveat": cav + " Source: " + BOOK + ", read on the image by the main agent (4 Nov 2026).",
            "node": NODE, "sources": [SRC]}

R = [
 rec("vajpayee-2003-09-17", "Atal Bihari Vajpayee", "Prime Minister of India", "India", "2003-09-17", "admiring", 2,
     "Homage to 'a great patriot, an intrepid warrior and a charismatic leader' who inspired all Asia; salutes his democracy, secularism, social justice.",
     "I come to pay homage to a great patriot, an intrepid warrior and a charismatic leader. Mustafa Kemal Ataturk led his people through the darkest hours of war and invasion, to freedom and into the modern age.",
     "Handwritten in English, signed 'A. B. Vajpayee, Prime Minister of India, September 17, 2003'. Continues: 'Ataturk inspired not only the Turkish people, but all Asia. We salute his vision of democracy, secularism and social justice, and remain committed to these noble principles.'",
     mirror="anti-colonial-liberator"),
 rec("olmert-2007-02-15", "Ehud Olmert", "Prime Minister of Israel", "Israel", "2007-02-15", "admiring", 2,
     "'A Role Model of Courage, vision and Patriotism' who gave hope to his people and to others who followed his example.",
     "A Role Model of Courage vision and Patriotism – who helped create a new hope for his people and for many others who took example from him.",
     "Handwritten in English, 15 Feb 2007, headed 'In honor of the father of Modern Turkey Kamal Ata-Turk'; continues 'The People of Israel look at this great hero of the turkish people with admiration and respect.' Signed 'Ehud Olmert, Prime Minister, the state of Israel'."),
 rec("katsav-2003-07-08", "Moshe Katsav", "President of Israel", "Israel", "2003-07-08", "admiring", 2,
     "A great leader of rare courage, leadership and responsibility; his legacy and 'Peace at home, peace in the world' inspire free nations.",
     "[translation] Milletini nadir görülen bir cesaret, liderlik ve sorumluluk birleşimi içerisinde yönlendirmiş olan büyük bir lider, vizyon ve inanç insanına, şahsım ve İsrail halkı adına derin saygı ve takdirlerimi sunuyorum.",
     "Handwritten in Hebrew (dated 8 Tammuz 5763 / 8.7.2003); the quote is the compilation's printed Turkish translation ('To a great leader who guided his nation with a rare combination of courage, leadership and responsibility, a man of vision and faith, I offer deep respect on my own behalf and that of the people of Israel'). The Hebrew was not transcribed. Continues: his legacy and vision inspire all freedom-loving democratic nations; 'Yurtta Sulh, Cihanda Sulh' is a message of peace for all humanity."),
 rec("verhofstadt-2004-01-26", "Guy Verhofstadt", "Prime Minister of Belgium", "Belgium", "2004-01-26", "admiring", 2,
     "Founder of modern Turkey and a great statesman of world history, whose courageous reforms opened Turkey's road to Europe eighty years ago.",
     "[translation] Kendisi Dünya tarihinde büyük bir devlet adamı olarak yerini almıştır. Cesurca yaptığı reformlar ile ülkesine Avrupa yolunu açmıştır.",
     "Handwritten in Dutch, Ankara 26 Jan 2004 ('… mijn respect en waardering uit te drukken voor Mustafa Kemal Atatürk, de grondlegger van het moderne Turkije. Hij heeft zich in de wereldgeschiedenis een plaats verworven als een groot staatsman …'); the quote is the compilation's Turkish ('He has taken his place in world history as a great statesman. With his courageous reforms he opened the road to Europe for his country'). Ends: the secular state, equality of men and women, the right to education — 'Mustafa Kemal Atatürk, a man of vision, saw this eighty years ago'.",
     mirror="modernization-poster-child"),
 rec("parvanov-2003-10-07", "Georgi Parvanov", "President of Bulgaria", "Bulgaria", "2003-10-07", "admiring", 1,
     "Respect for the work of the first builder of the Republic of Turkey; wishes Turks to keep and develop his ideological and political legacy.",
     "С почит и уважение към делото на първостроителя на Република Турция!",
     "Handwritten in Bulgarian, 7.X.2003 (transcribed from handwriting): 'With respect and esteem for the work of the first builder of the Republic of Turkey! With wishes to the people and the country to preserve and develop the ideological and political legacy of Mustafa Kemal Atatürk!' The compilation's Turkish agrees in substance but is looser ('cause of the Leader and First Founder')."),
 rec("balkenende-2003-10-08", "Jan Peter Balkenende", "Prime Minister of the Netherlands", "Netherlands", "2003-10-08", "admiring", 1,
     "Honours 'the great Turkish leader' who articulated the young republic's European aspirations, quoting his words on progress toward civilization.",
     "I am delighted and honoured to be here, at this historic moment in Turkey's European aspirations, as articulated for the Young Republic by its Founder, Kemal Atatürk.",
     "Handwritten in English, 8 October 2003; continues 'In memory of the great Turkish leader who said, \"The Turkish people have both the ability and the determination to progress, without hesitation or disenchantment, along the path of civilization.\"' Atatürk as the author of Turkey's EU vocation."),
 rec("schuster-2003-12-16", "Rudolf Schuster", "President of Slovakia", "Slovakia", "2003-12-16", "admiring", 2,
     "Addressing Atatürk: his statesman's mind and vision left an extraordinary heritage of independence and national self-confidence, 'inspirational for us as well'.",
     "you have left your descendants – thanks to your statesman's mind and vision – an extraordinary heritage of independence and well-founded, national self-confidence which is inspirational for us as well.",
     "Handwritten in English, Ankara, 16 Dec 2003, addressed 'Mr. Statesman, Dear General Mustafa Kemal Atatürk'; also: 'I agree with your conviction that politicians and statesmen must look for sources of certainty in their people if they are to inspire and lead' and 'I bow down before your everlasting memorial.'"),
 rec("spidla-2003", "Vladimír Špidla", "Prime Minister of the Czech Republic", "Czech Republic", "2003", "admiring", 1,
     "Bows before the memory of the founder of the Republic; his 'peace at home' thought and modernizing drive still bear fruit.",
     "[translation] 80 sene önce, Türkiye Cumhuriyetini kendi liderliğinde Türk halkıyla birlikte kuran Kemal Atatürk'ün anısının önünde saygıyla eğiliyorum.",
     "Handwritten in Czech (not transcribed); the quote is the compilation's Turkish ('I bow with respect before the memory of Kemal Atatürk, who 80 years ago founded the Republic of Turkey together with the Turkish people under his leadership'). Undated on the page; '80 years ago' and his premiership (2002–04) give 2003. Continues: the ideas expressed in 'peace at home, peace in the world' and the modernization of an independent democratic country 'continue to bear fruit'."),
 rec("jettou-2004-04-20", "Driss Jettou", "Prime Minister of Morocco", "Morocco", "2004-04-20", "admiring", 2,
     "A great statesman, 'one of the greatest people of our time', who built a country with universal radiance today.",
     "[translation] Allah, bu büyük devlet adamına mağfiret etsin. Zamanımızın en büyük insanlarından biriydi ve günümüzde evrensel ışıltısı olan bir ülke kurdu.",
     "Handwritten in Arabic, 20.04.2004; the quote is the compilation's Turkish ('May God forgive this great statesman. He was one of the greatest people of our time and built a country with universal radiance today'). 'Great statesman' is the compilation's rendering of 'rajul' (a man), and 'forgive' renders 'enveloped in His mercy'. Reading of the Arabic (last word of line 3 unclear): 'رجل تغمده الله برحمته كان من أعظم رجال هذا العصر وبنى بلدا له إشعاع …'."),
 rec("rahmonov-2006-01-19", "Emomali Rahmonov", "President of Tajikistan", "Tajikistan", "2006-01-19", "admiring", 1,
     "Pledges to honour the memory of the Republic's founder, 'the great son of the Turkish people', Mustafa Kemal Pasha Atatürk.",
     "Мо хотираи асосгузори Ҷумҳурии Туркия, фарзанди бузурги халқи турк Мустафо Камол пошшо Отатуркро пос хоҳем дошт",
     "[translation] 'We shall honour the memory of the founder of the Republic of Turkey, the great son of the Turkish people, Mustafa Kemal Pasha Atatürk.' Handwritten in Tajik, 19.01.06, signed 'Э. Раҳмонов, Президенти Ҷумҳурии Тоҷикистон'; transcribed from handwriting (Tajik-specific letters normalized)."),
 rec("jeffery-2006-04-26", "Michael Jeffery", "Governor-General of Australia", "Australia", "2006-04-26", "admiring", 2,
     "From Gallipoli 'emerged the great military commander' who founded modern Turkey; Australia will never forget his postwar friendship and words to the mothers.",
     "Australia will never forget Atatürk's symbol of friendship in the years following the war, and to this day his words to the mothers of those who died continue to resonate amongst the Australian people.",
     "Handwritten in English, 26 April 2006; earlier: 'for Turkey it was a place where national honour was restored and from which emerged the great military commander, Mustafa Kemal Atatürk, founder and leader of the modern Turkish Republic.' The 'words to the mothers' are the contested 'Johnnies and Mehmets' text (see [[Johnnies and Mehmets]])."),
 rec("talat-2005-08-02", "Mehmet Ali Talat", "President of the Turkish Republic of Northern Cyprus", "Cyprus", "2005-08-02", "admiring", 2,
     "His military, economic and enlightenment victories lit the way for Turkish Cypriots; 'the road you opened was the road to a humane life'.",
     "Açtığın yol insanca yaşama yoluydu. Bu ışıkla yürümeye devam ediyoruz.",
     "Handwritten in Turkish, 2 Aug 2005, addressed to 'Türkiye Cumhuriyetinin kurucusu, Büyük Atatürk'; also: his military, economic development and enlightenment successes 'have been the light of the Turkish Cypriots too'; 'yurtta barış dünyada barış'. Country recorded as Cyprus (TRNC, recognised only by Turkey)."),
]
BORAN = "https://archive.org/details/gelisiguzelkitapo2"
EXTRA = [
 {"id": "yul-brynner-1962-04", "voice": "Yul Brynner", "voice_type": "person", "role": "American film actor, chosen to play Atatürk in a planned film",
  "country": "United States", "country_now": "United States", "domain": "arts", "date": "1962-04", "era": "posthumous", "mirror": None,
  "polarity": "admiring", "intensity": 2,
  "what_they_saw": "Preparing to play him on film, calls Atatürk 'a true hero' and fears he cannot live up to the role.",
  "quote": "[translation] Atatürk, gerçek bir kahramandır. Kendimi onun yerine koyabilmek bana ürperti veriyor.",
  "artifact": "quote", "evidence": "S",
  "mediated_by": "Milliyet, 13 Apr 1962, as quoted in Tunç Boran, Mekân ve Siyaset İlişkisi Bağlamında Anıtkabir (1938-1973), PhD thesis, Ankara University, 2011, p. ~315 (n. 1503)",
  "caveat": "Turkish of the newspaper report ('Atatürk is a true hero. Putting myself in his place makes me shiver'). In the Anıtkabir special book he wrote 'Size karşı büyük bir saygı ve hürmet duyuyorum' ('I feel great respect and reverence for you'). The film was never made. Thesis read as open full text on archive.org (item gelisiguzelkitapo2, 'Anıtkabir mekan').",
  "node": NODE, "sources": [BORAN]},
 {"id": "nzz-1938-11", "voice": "Neue Zürcher Zeitung", "voice_type": "press", "role": "Swiss daily, Zurich",
  "country": "Switzerland", "country_now": "Switzerland", "domain": "press", "date": "1938-11", "era": "funeral", "mirror": None,
  "polarity": "admiring", "intensity": 2,
  "what_they_saw": "The funeral as Atatürk's 'last victory': Hitler's and Stalin's envoys side by side, fascists, democrats and communists bowing at his coffin.",
  "quote": "[translation] Atatürk'ün cenaze töreni, onun son zaferi oldu. … Tabutunun önünde Faşistler, Demokratlar ve Komünistler eğildiler.",
  "artifact": "article", "evidence": "S",
  "mediated_by": "Orhan Koloğlu, Mazlum Milletler Devrimleri ve Türk Devrimi (Kaynak, 2004), p. 81, as quoted in Boran 2011 (thesis, ch. on the funeral, n. 250)",
  "caveat": "Turkish rendering of the NZZ report on the 21 Nov 1938 funeral ('Atatürk's funeral was his last victory. Before his coffin all his opponents fell silent. Turkish and German soldiers marched in one line behind it; in another, the representatives of Stalin and Hitler side by side; both Valencia and General Franco sent flowers. Fascists, Democrats and Communists bowed before his coffin.'). The German original and exact date not seen (NZZ archive is subscription-only). A major paper's striking stance, kept under the notable-voices rule; it is also the census's own Rorschach thesis in one sentence.",
  "node": "Death and State Funeral of Atatürk", "sources": [BORAN]},
]
R += EXTRA
for r in R:
    assert len(r["what_they_saw"].split()) <= 25, r["id"]
with open(os.path.join(STATE, "gazes_anitbook.jsonl"), "w", encoding="utf-8") as f:
    for r in R:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

NAT = {"United States": "American", "Switzerland": "Swiss", "India": "Indian", "Israel": "Israeli", "Belgium": "Belgian", "Bulgaria": "Bulgarian", "Netherlands": "Dutch",
       "Slovakia": "Slovak", "Czech Republic": "Czech", "Morocco": "Moroccan", "Tajikistan": "Tajik",
       "Australia": "Australian", "Cyprus": "Turkish Cypriot"}
for r in [x for x in R if x not in EXTRA]:
    person(r["voice"], role=r["role"], nat=NAT[r["country"]], life="", stance="%s (%s)" % (r["polarity"], r["date"][:4]),
           tags=["verified", "anitkabir-book"],
           body="%s. Wrote in the Anıtkabir special book on %s: \"%s\" See [[%s]].\n\n## Sources\n- %s\n" % (
               r["role"], r["date"], r["quote"], NODE, BOOK))

body = ["""Page images of the printed compilation *Anıtkabir Özel Defteri* (entries by visiting heads of state and government,
with the handwritten original beside the compilation's Turkish), published as a gallery on ataturkarsivi.com. Read on the
images, not via press reports. The 2003–2007 entries add twelve voices: an Indian prime minister saluting the warrior who
"inspired not only the Turkish people, but all Asia"; two Israeli leaders; Belgian, Dutch and Czech premiers who read
him as the author of Turkey's road to Europe; Slovak, Bulgarian and Tajik presidents; a Moroccan prime minister; the
Governor-General of Australia; the Turkish Cypriot president. The King of Sweden's entry (30 May 2006) recalls only his
grandfather's visit and is not counted; the gallery's "Sampaio" images show Parvanov's entry, so Sampaio is not counted.
Earlier visitors-book records (Merkel, Elizabeth II, Xi, Obama and others) come from press reports: see
[[Leaders in the Anıtkabir Special Book, 2004–2025]].
"""]
for r in R:
    body.append("## %s (%s)\n\n> %s\n\n%s\n" % (r["voice"], r["date"], r["quote"], r["caveat"]))
body.append("## Sources\n- %s\n- %s\n" % (BOOK, SRC))
note("Events", NODE, {"type": "event", "when": "2003–2007", "tags": ["event", "verified", "anitkabir-book"]}, "\n".join(body))
person("Yul Brynner", role="Actor", nat="American (Russian-born)", life="1920–1985", stance="admiring (1962)", tags=["verified", "arts"],
       body="Cast to play Atatürk in a planned film, he visited Anıtkabir in April 1962, wrote 'Size karşı büyük bir saygı ve hürmet duyuyorum' in the special book and told reporters: 'Atatürk is a true hero. Putting myself in his place makes me shiver.' The film was never made. See [[%s]].\n\n## Sources\n- Milliyet, 13 Apr 1962, via Tunç Boran, Anıtkabir (1938-1973), PhD thesis, Ankara University 2011 (archive.org gelisiguzelkitapo2).\n" % NODE)
print("anitbook: %d records" % len(R))
