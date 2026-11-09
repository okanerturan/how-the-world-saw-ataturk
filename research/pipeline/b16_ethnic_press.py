# -*- coding: utf-8 -*-
# Census round 8 (Oct 2026) — America's immigrant press 1919-1938 (slug: ethnic_press).
# Route: Chronicling America (Library of Congress) via the loc.gov collection API (fa=language:<lang>, dates=1919/1938),
# page OCR from tile.loc.gov (word_coordinates_url + &full_text=1). Every quote was machine-checked against the page OCR
# (whitespace/hyphenation removed) before it was written here. Translations are the vault's own, marked as such.
from _lib import note

CA = ("Library of Congress, *Chronicling America* (free, public domain), page OCR retrieved Oct 2026 via the loc.gov "
      "collection search and the `tile.loc.gov` text service")
POL = {"admiring": "admiring", "hostile": "hostile", "conflicted": "conflicted", "instrumental": "instrumental"}

ROWS = [
 {
  "id": "la-gaceta-tampa-1930-06",
  "voice": "La Gaceta (Tampa)",
  "role": "Spanish-language daily, Tampa, Florida (cigar-worker readership)",
  "lccn": "sn86002403",
  "date": "1930-06-27",
  "sp": 1,
  "polarity": "hostile",
  "quote": "Todas las dictaduras son malas, antidemocráticas",
  "tr": "All dictatorships are bad, undemocratic",
  "what": "Column lists 'Dictadura de Kemal Pacha en Turquía' with Mussolini, Pilsudski and Stalin and condemns all dictatorships as bad and undemocratic.",
  "caveat": "Unsigned front-page column; the list also names Primo de Rivera, Leguía, Ibáñez and Stalin, so Kemal is one entry in a general indictment.",
  "node": "Tampa's La Gaceta Calls Kemal a Dictator, 1930–1935",
  "lang": "es",
  "place": "Tampa"
 },
 {
  "id": "la-gaceta-tampa-1930-11",
  "voice": "La Gaceta (Tampa)",
  "role": "Spanish-language daily, Tampa, Florida (cigar-worker readership)",
  "lccn": "sn86002403",
  "date": "1930-11-04",
  "sp": 1,
  "polarity": "hostile",
  "quote": "Las leyes para la Dictadura, sean buenas o malas, no existen.",
  "tr": "The laws for the Dictatorship, whether good or bad, do not exist.",
  "what": "Column on workers' rights: under dictatorship the law is the ruler, in Turkey 'Sr. Kemal Pasha', as in Italy, Poland, Russia.",
  "caveat": "Unsigned column; the quoted sentence is the general principle, the Kemal Pasha clause follows it two sentences later.",
  "node": "Tampa's La Gaceta Calls Kemal a Dictator, 1930–1935",
  "lang": "es",
  "place": "Tampa"
 },
 {
  "id": "la-gaceta-tampa-1931-03",
  "voice": "La Gaceta (Tampa)",
  "role": "Spanish-language daily, Tampa, Florida (cigar-worker readership)",
  "lccn": "sn86002403",
  "date": "1931-03-02",
  "sp": 1,
  "polarity": "hostile",
  "quote": "La república en eso imita al extinguido sultanato.",
  "tr": "The republic in this imitates the extinct sultanate.",
  "what": "Column item says Kemal is hanging dervishes and secret-order members, keeping the old custom of hanging the government's enemies, as the sultanate did.",
  "caveat": "OCR of the preceding lines is damaged ('Keraal Pasha', doubled words); the quoted sentence is clean. Unsigned.",
  "node": "Tampa's La Gaceta Calls Kemal a Dictator, 1930–1935",
  "lang": "es",
  "place": "Tampa"
 },
 {
  "id": "la-gaceta-tampa-1932-05",
  "voice": "La Gaceta (Tampa)",
  "role": "Spanish-language daily, Tampa, Florida (cigar-worker readership)",
  "lccn": "sn86002403",
  "date": "1932-05-28",
  "sp": 1,
  "polarity": "conflicted",
  "quote": "Dictador de mano dura",
  "tr": "Hard-handed Dictator",
  "what": "Column on Turkey's friendly ties with both Mussolini and Soviet Russia: Kemal a hard-handed Dictator who befriends all and rules Turks as he sees fit.",
  "caveat": "Unsigned. Same issue's p. 4 carries a British Gallipoli-history item calling Kemal a noble adversary (not a voice of the paper).",
  "node": "Tampa's La Gaceta Calls Kemal a Dictator, 1930–1935",
  "lang": "es",
  "place": "Tampa"
 },
 {
  "id": "la-gaceta-tampa-1934-12",
  "voice": "La Gaceta (Tampa)",
  "role": "Spanish-language daily, Tampa, Florida (cigar-worker readership)",
  "lccn": "sn86002403",
  "date": "1934-12-01",
  "sp": 1,
  "polarity": "admiring",
  "quote": "La medida de Kemal Pasha se inspira en las costumbres norteamericanas.",
  "tr": "Kemal Pasha's measure is inspired by North American customs.",
  "what": "Column on the ban on clerics' street dress, applied to all faiths: Kemal's measure follows American custom; 'Turkey progresses', Muslim priests 'tamed'.",
  "caveat": "Unsigned column item; tone mildly approving and ironic ('amansados').",
  "node": "Tampa's La Gaceta Calls Kemal a Dictator, 1930–1935",
  "lang": "es",
  "place": "Tampa"
 },
 {
  "id": "la-gaceta-tampa-1935-01",
  "voice": "La Gaceta (Tampa)",
  "role": "Spanish-language daily, Tampa, Florida (cigar-worker readership)",
  "lccn": "sn86002403",
  "date": "1935-01-24",
  "sp": 1,
  "polarity": "hostile",
  "quote": "Un sentimentalismo de nuevo cuño, enemigo de la libertad y de la justicia.",
  "tr": "A sentimentality of a new mint, enemy of liberty and of justice.",
  "what": "Answering Keyserling: the masses share 'sentimental life' yoked to the cart of a Mussolini, a Hitler or a Mustafá Kemal, an enemy of liberty.",
  "caveat": "Unsigned; the quoted sentence follows the passage naming Kemal and concerns the whole fascist-style set.",
  "node": "Tampa's La Gaceta Calls Kemal a Dictator, 1930–1935",
  "lang": "es",
  "place": "Tampa"
 },
 {
  "id": "la-gaceta-tampa-1935-11",
  "voice": "La Gaceta (Tampa)",
  "role": "Spanish-language daily, Tampa, Florida (cigar-worker readership)",
  "lccn": "sn86002403",
  "date": "1935-11-01",
  "sp": 1,
  "polarity": "hostile",
  "quote": "El dictador turco pide las islas",
  "tr": "The Turkish dictator asks for the islands",
  "what": "On the Ethiopian crisis: the 'Turkish dictator' offers Britain help against Italy and asks for the Dodecanese; sarcastic about Kemal's 'excess population'.",
  "caveat": "OCR of the island name is damaged ('Ad Dodecaneso'); only the clean clause is quoted. Unsigned.",
  "node": "Tampa's La Gaceta Calls Kemal a Dictator, 1930–1935",
  "lang": "es",
  "place": "Tampa"
 },
 {
  "id": "risorgimento-italiano-1922",
  "voice": "Il Risorgimento Italiano nel Maryland",
  "role": "Italian-language weekly, Baltimore",
  "lccn": "sn89060332",
  "date": "1922-10-21",
  "sp": 1,
  "polarity": "admiring",
  "quote": "un patriota che lavora, indomito ed incorrotto, per salvare quanto è salvabile del suo povero paese",
  "tr": "a patriot who works, indomitable and incorruptible, to save whatever can be saved of his poor country",
  "what": "Profile: Kemal is no longer a rebel but 'the recognised dictator'; unlike Enver and Talaat he is an incorruptible patriot saving his country.",
  "caveat": "Unsigned front-page item (the same page calls him 'il dittatore riconosciuto'); OCR has minor artefacts.",
  "node": "America's Immigrant Press Reads Kemal, 1922–1938",
  "lang": "it",
  "place": "Baltimore"
 },
 {
  "id": "risorgimento-italiano-1929",
  "voice": "Il Risorgimento Italiano nel Maryland",
  "role": "Italian-language weekly, Baltimore",
  "lccn": "sn89060332",
  "date": "1929-01-12",
  "sp": 4,
  "polarity": "instrumental",
  "quote": "rinascita e vitalità dovute sopra tutto all’energia, all’intuito, alla volontà di Kemal Pascià",
  "tr": "rebirth and vitality owed above all to the energy, the intuition, the will of Kemal Pasha",
  "what": "Welcoming the Italo-Turkish pact: Turkey's rebirth and return to European history owed above all to Kemal's energy, intuition and will.",
  "caveat": "Praise framed to celebrate Italy's pact policy (Fascist-era Italian diplomacy), hence instrumental; unsigned.",
  "node": "America's Immigrant Press Reads Kemal, 1922–1938",
  "lang": "it",
  "place": "Baltimore"
 },
 {
  "id": "la-verita-waterbury-1935-05",
  "voice": "La Verità (Waterbury)",
  "role": "Italian-language weekly, Waterbury, Connecticut",
  "lccn": "sn95063190",
  "date": "1935-05-03",
  "sp": 2,
  "polarity": "admiring",
  "quote": "ha riconosciuto i meriti indiscutibili del capo supremo della nuova Turchia",
  "tr": "has recognised the indisputable merits of the supreme head of the new Turkey",
  "what": "Praises Lady Astor's speech hailing 'dictator' Kemal for freeing Turkish women from the harem; credits him with restoring Turkey's political unity.",
  "caveat": "Unsigned column; the paper's loyalty to Italian Fascism is not shown in this passage. The quoted clause is the paper's comment on Astor's speech.",
  "node": "America's Immigrant Press Reads Kemal, 1922–1938",
  "lang": "it",
  "place": "Waterbury"
 },
 {
  "id": "la-verita-waterbury-1935-08",
  "voice": "La Verità (Waterbury)",
  "role": "Italian-language weekly, Waterbury, Connecticut",
  "lccn": "sn95063190",
  "date": "1935-08-16",
  "sp": 3,
  "polarity": "instrumental",
  "quote": "se nella Turchia di Kemal vi e’ persino la legge che regola il modo di vestire e di scrivere",
  "tr": "if in Kemal's Turkey there is even a law regulating the manner of dressing and of writing",
  "what": "Defending Italy against dictatorship charges: Russia, Germany and Kemal's Turkey, which regulates dress and writing, are worse; Italy has no race struggle.",
  "caveat": "Fascist-apologist comparison, not an assessment of Kemal; Kemal is cited as a harsher dictatorship than Italy.",
  "node": "America's Immigrant Press Reads Kemal, 1922–1938",
  "lang": "it",
  "place": "Waterbury"
 },
 {
  "id": "la-sentinella-bridgeport-1934",
  "voice": "La Sentinella (Bridgeport)",
  "role": "Italian-language weekly, Bridgeport, Connecticut",
  "lccn": "sn84020351",
  "date": "1934-09-13",
  "sp": 4,
  "polarity": "instrumental",
  "quote": "risultati come quelli di Mussolini, Stalin, Kemal, Piluski e di altri dittatori riformisti",
  "tr": "results like those of Mussolini, Stalin, Kemal, Piłsudski and other reformist dictators",
  "what": "On a Stamford 'strong mayor' charter: hopes for results like those of Mussolini, Stalin, Kemal, Piłsudski and other 'reformist dictators'.",
  "caveat": "Local-politics argument; Kemal used as one example of a reformist dictator; OCR 'Piluski', 'Tesperimento' in the sentence's opening.",
  "node": "America's Immigrant Press Reads Kemal, 1922–1938",
  "lang": "it",
  "place": "Bridgeport"
 },
 {
  "id": "amerikai-magyar-hirlap-1922",
  "voice": "Amerikai Magyar Hirlap",
  "role": "Hungarian-language newspaper, Youngstown, Ohio",
  "lccn": "sn88078388",
  "date": "1922-11-23",
  "sp": 4,
  "polarity": "admiring",
  "quote": "Kemal villogó kardja alaposan bizonyította be a világnak azt az igazságot",
  "tr": "Kemal's flashing sword thoroughly proved to the world the truth",
  "what": "Greeting to Angora reprinted from Budapest's Pesti Hírlap: Kemal's sword proved a truth; the Angora Assembly likened to Kossuth's 1849 Debrecen parliament.",
  "caveat": "Unsigned; OCR damaged in places. Hungarian-Turkish kinship framing and the Kossuth analogy are the paper's own.",
  "node": "America's Immigrant Press Reads Kemal, 1922–1938",
  "lang": "hu",
  "place": "Youngstown"
 },
 {
  "id": "amerikai-magyar-hirlap-1938",
  "voice": "Amerikai Magyar Hirlap",
  "role": "Hungarian-language newspaper, Youngstown, Ohio",
  "lccn": "sn88078388",
  "date": "1938-04-28",
  "sp": 7,
  "polarity": "conflicted",
  "quote": "A török diktátor tetszik nekünk",
  "tr": "The Turkish dictator pleases us",
  "what": "Wry line after Kemal's flu recovery: the Turkish dictator pleases us because his name reaches the papers only when he is ill.",
  "caveat": "One-line joke in a column; the implied contrast is with noisier dictators (Hitler is the topic of the preceding paragraph).",
  "node": "America's Immigrant Press Reads Kemal, 1922–1938",
  "lang": "hu",
  "place": "Youngstown"
 },
 {
  "id": "svet-cleveland-1923",
  "voice": "Svět (Cleveland)",
  "role": "Czech-language daily, Cleveland, Ohio",
  "lccn": "sn83045068",
  "date": "1923-09-07",
  "sp": 2,
  "polarity": "admiring",
  "quote": "znamená počátek nového období tureckých dějin",
  "tr": "means the beginning of a new period of Turkish history",
  "what": "Essay 'Obrozování Turecka': Lausanne, from which Turkey emerges victor, opens a new era; Kemal's victories drive the Angora national renaissance.",
  "caveat": "Essay is headed with an author's initials in the OCR ('Dr. F. Š.'?), not resolved; page header and column order damaged by OCR.",
  "node": "America's Immigrant Press Reads Kemal, 1922–1938",
  "lang": "cs",
  "place": "Cleveland"
 },
 {
  "id": "svet-cleveland-1922",
  "voice": "Svět (Cleveland)",
  "role": "Czech-language daily, Cleveland, Ohio",
  "lccn": "sn83045068",
  "date": "1922-09-16",
  "sp": 2,
  "polarity": "conflicted",
  "quote": "zbůjnický Turek, drží ve svých rukou osud Evropy",
  "tr": "brigand-like Turk, holds the fate of Europe in his hands",
  "what": "Translating a Plain Dealer editorial: brigand-like Kemal holds Europe's fate, yet is a dazzling hero to Muslims and Hindus.",
  "caveat": "Mediated: the editorial is the Plain Dealer's, printed in translation by Svět as its own take on the day; OCR interleaves columns, so the quoted clause is joined from two lines.",
  "node": "America's Immigrant Press Reads Kemal, 1922–1938",
  "lang": "cs",
  "place": "Cleveland"
 },
 {
  "id": "jednosc-polek-1927",
  "voice": "Jedność Polek (Cleveland)",
  "role": "Polish-language women's weekly, Cleveland",
  "lccn": "sn83035481",
  "date": "1927-12-20",
  "sp": 4,
  "polarity": "admiring",
  "quote": "Burząc stary porządek rzeczy, dał trwałe, niewzruszone podwaliny pod nowy.",
  "tr": "By tearing down the old order of things he gave lasting, unshakable foundations to the new.",
  "what": "Defends Kemal's 36-hour party speech against charges of self-glorification: without him Turkey would be a protectorate; he laid a lasting new foundation.",
  "caveat": "Unsigned column; compares with Kerensky's failure in Russia. OCR damaged in the passage before the quote.",
  "node": "America's Immigrant Press Reads Kemal, 1922–1938",
  "lang": "pl",
  "place": "Cleveland"
 },
 {
  "id": "jednosc-polek-1928-10",
  "voice": "Jedność Polek (Cleveland)",
  "role": "Polish-language women's weekly, Cleveland",
  "lccn": "sn83035481",
  "date": "1928-10-09",
  "sp": 1,
  "polarity": "admiring",
  "quote": "Zasługa to niewątpliwie Mustafa Kemal Paszy.",
  "tr": "The credit for this undoubtedly belongs to Mustafa Kemal Pasha.",
  "what": "Turkey Europeanises and modernises, undoubtedly Kemal's merit: Swiss law, Latin alphabet, spread of literacy.",
  "caveat": "Unsigned news-and-comment column.",
  "node": "America's Immigrant Press Reads Kemal, 1922–1938",
  "lang": "pl",
  "place": "Cleveland"
 },
 {
  "id": "jednosc-polek-1928-12",
  "voice": "Jedność Polek (Cleveland)",
  "role": "Polish-language women's weekly, Cleveland",
  "lccn": "sn83035481",
  "date": "1928-12-18",
  "sp": 4,
  "polarity": "admiring",
  "quote": "Odrodzicielem kraju i narodu w Turcji jest Kemal Pasza.",
  "tr": "The regenerator of the country and the nation in Turkey is Kemal Pasha.",
  "what": "Reports a rumour of crowning Kemal king, which the Turkish press rejects; says Poles grasp his work through Piłsudski's, 'our Polish Washington'.",
  "caveat": "Unsigned column; the Piłsudski analogy is the paper's, anchored to a remark it attributes to a US envoy in Warsaw.",
  "node": "America's Immigrant Press Reads Kemal, 1922–1938",
  "lang": "pl",
  "place": "Cleveland"
 },
 {
  "id": "przewodnik-katolicki-1922",
  "voice": "Przewodnik Katolicki (New Britain)",
  "role": "Polish-language Catholic weekly, New Britain, Connecticut",
  "lccn": "sn88043117",
  "date": "1922-12-15",
  "sp": 9,
  "polarity": "instrumental",
  "quote": "Kemal basza i rząd turecki w Angorze zaśpiewał trustowi amerykańskiemu bardzo miłą piosenkę",
  "tr": "Kemal Pasha and the Turkish government in Angora sang the American trust a very pleasant song",
  "what": "Lausanne editorial: US press dropped its 'cruel Turks' outcry on Standard Oil's orders; Kemal sang the trust a sweet oil tune; Poland should favour Turkey.",
  "caveat": "Unsigned editorial. It also asserts that the Greeks, not the Turks, burned Smyrna; that attribution is contested and is recorded only as the paper's view.",
  "node": "America's Immigrant Press Reads Kemal, 1922–1938",
  "lang": "pl",
  "place": "New Britain"
 },
 {
  "id": "youngstown-slovak-1930",
  "voice": "Youngstownské Slovenské Noviny",
  "role": "Slovak-language newspaper, Youngstown, Ohio",
  "lccn": "sn88078386",
  "date": "1930-01-31",
  "sp": 1,
  "polarity": "admiring",
  "quote": "Nové Turecko má výborného prezidenta v osobe Kemal pašu",
  "tr": "New Turkey has an excellent president in the person of Kemal Pasha",
  "what": "Item on Turkey banning child labour in mines: new Turkey has an excellent president in Kemal Pasha, unlike the US South.",
  "caveat": "Unsigned filler item; the contrast with the US South is the paper's comment.",
  "node": "America's Immigrant Press Reads Kemal, 1922–1938",
  "lang": "sk",
  "place": "Youngstown"
 },
 {
  "id": "glas-svobode-1922",
  "voice": "Glas svobode (Chicago)",
  "role": "Slovenian-language freethought daily, Chicago",
  "lccn": "sn83045203",
  "date": "1922-12-01",
  "sp": 5,
  "polarity": "conflicted",
  "quote": "Da Kemalu ne manjka energije in sposobnosti, je zadostno pokazal.",
  "tr": "That Kemal does not lack energy and ability, he has shown sufficiently.",
  "what": "After Mudanya the sultan is gone and the caliphate lies open to Kemal; he has proved his energy and ability, but rivals loom.",
  "caveat": "Unsigned; also on p. 5 a 'Balkanska zveza' feature wary that Kemal will want to protect Muslims everywhere; the paper's stance is partly inferred from that.",
  "node": "America's Immigrant Press Reads Kemal, 1922–1938",
  "lang": "sl",
  "place": "Chicago"
 },
 {
  "id": "morgen-zhurnal-1934",
  "voice": "Der Morgen Zhurnal (Jewish Morning Journal)",
  "role": "Yiddish-language daily, New York",
  "lccn": "sn83045838",
  "date": "1934-07-25",
  "sp": 7,
  "polarity": "hostile",
  "quote": "ליידען פון אונזערע ברידער אונטער דער טערקישער דיקטאטור",
  "tr": "sufferings of our brothers under the Turkish dictatorship",
  "what": "Editorial on 1934 Thracian pogroms: Turkey made Jews second-class citizens; Jewish bodies must investigate 'sufferings of our brothers' under Kemal Pasha's dictatorship.",
  "caveat": "Yiddish OCR is poor ('דו' for 'די'); the quote is exactly as OCR renders it. Page layout suggests the editorial page but no byline appears.",
  "node": "America's Immigrant Press Reads Kemal, 1922–1938",
  "lang": "yi",
  "place": "New York"
 }
]
NODE1 = "Tampa's La Gaceta Calls Kemal a Dictator, 1930–1935"
NODE2 = "America's Immigrant Press Reads Kemal, 1922–1938"


def url(r):
    return f"https://www.loc.gov/resource/{r['lccn']}/{r['date']}/ed-1/?sp={r['sp']}"

def bullet(r):
    return (f"- **{r['voice']}**, {r['date']}, p. {r['sp']} ({r['polarity']}). *{r['what']}* "
            f"Original ({r['lang']}, OCR-verbatim): “{r['quote']}” — English (vault translation): “{r['tr']}”. "
            f"[page]({url(r)}). _Caveat: {r['caveat']}_")

def sources(rows):
    return "\n".join(f"  - [{r['voice']}, {r['date']}, p. {r['sp']}]({url(r)})" for r in rows)

E1 = """
Tampa's *La Gaceta*, the Spanish-language daily of the cigar-makers of Ybor City and West Tampa, ran a front-page column,
**"Changas y Chungas"**, that kept returning to Kemal as a type: the **Dictator**. The earlier card
[[Spanish-Language Newspapers Across the Americas Read Kemal, 1922–1935]] holds two *La Gaceta* items (14 Oct 1930,
21 Feb 1935). This card adds seven more from the 1930–35 run, read as page OCR. The column's habit is a litany of rulers (Italy, Poland, Turkey, Russia, Cuba, Venezuela) — each a name for the same fault; the column's own targets, to judge by these items, were as often
Machado's Cuba and Mussolini's Italy as Ankara. Kemal is almost never discussed on his own account; he is a
data point in an argument about dictatorship. Two lines are exceptions: the 2 Mar 1931 item (hanging dervishes —
"the republic imitates the extinct sultanate") and the 28 May 1932 characterisation (a hard-handed Dictator who is
also an "intelligent gentleman" and gets on with everyone from Mussolini to Stalin). The one admiring item (1 Dec 1934, the clergy-dress ban) is
in the same voice: tolerant, ironic, American-inflected.

""" + "\n".join(bullet(r) for r in ROWS if r['node'] == NODE1) + """

**Not recorded:** *La Gaceta* wire items on Kemal (6 Dec 1934 voting rights for women, 4 Jan 1936 Spanish-Turkish treaty
"el patriota Kemal Pasha", Nov 1938 death notices, 16 Mar 1938 Bonardi's Franco-and-Kemal passage) — agency or reprinted copy.

## Sources
- """ + CA + """.
""" + sources([r for r in ROWS if r['node'] == NODE1]) + """
- Tier P (newspaper page, OCR confirmed). The OCR of 1930s Tampa pages is rough; quotes were restricted to clauses that survive it.
"""

E2 = """
Chronicling America holds the foreign-language press of the United States. Searching it for Kemal (`fa=language:<lang>`, 1919–38)
gives, by hit count: German 262 pages, Polish 201, Czech 136, Lithuanian 91, Slovenian 48, Hungarian 16, Italian 17, Slovak 9, Finnish 20,
Yiddish ~480 (Hebrew-script query), Spanish (see [[Spanish-Language Newspapers Across the Americas Read Kemal, 1922–1935]]).
**Greek, Armenian, Arabic and Hebrew return zero**: the Greek-American, Armenian-American (*Hairenik*, *Asbarez*)
and Syrian-Lebanese (*al-Hoda*, *Meraat-ul-Gharb*) papers are not on loc.gov for these years. Most hits are agency copy from the
1922 Smyrna and Chanak weeks; this card keeps only **items with a stated view**.

What the communities saw, in short:

- **Hungarians** saw a kinsman. *Amerikai Magyar Hirlap* (Youngstown, 23 Nov 1922) reprinted a Budapest *Pesti Hírlap* greeting, "Üdvözlet Angorába", comparing the Angora Assembly to Kossuth's 1849 Debrecen parliament; by 1938 the same paper could joke about "the Turkish dictator".
- **Poles** split by paper, not by creed. The Cleveland women's weekly *Jedność Polek* (1927–28) made Kemal the Turkish Piłsudski, a "regenerator"; the Connecticut Catholic weekly *Przewodnik Katolicki* (Dec 1922) read him through oil politics and Polish interest, and blamed the American press's change of tune on Standard Oil.
- **Czechs** in Cleveland first printed a hostile-but-awed Plain Dealer editorial ("brigand", yet a hero to Muslims and Hindus) at Smyrna time, then a respectful essay on Lausanne as the start of a new Turkish era.
- **Italians** used him. The Baltimore weekly praised him as an "incorruptible patriot" (1922) and credited him with the Italo-Turkish pact (1929); Connecticut papers of 1934–35 used Kemal as a stick or a comparison in arguments about Mussolini's own dictatorship.
- **Slovaks** (Youngstown, 1930) and **Slovenes** (Chicago, 1922) offer a mild praise and a Balkan wariness.
- **Yiddish**: the New York *Morgen Zhurnal* (25 Jul 1934) wrote of "the sufferings of our brothers under the Turkish dictatorship" after the Thracian pogroms. This is the hardest-edged Jewish voice found; the Yiddish Daily Tageblatt's English wire pages (1921–26) carry the Daily Mail's "Sephardic Jew from Salonica" rumour and Cilicia reports but no view of the paper's own.

""" + "\n".join(bullet(r) for r in ROWS if r['node'] == NODE2) + """

**Dug, nothing usable:** *Washington Journal* (German, DC) and *Der Nordstern* (German, St Cloud) — German-language news and
a Jan 1929 reprinted feature on Turkish reforms ("dieser diktierte Umschwung"), no editorial voice; *Dziennik Chicagoski*,
*Draugas*, *Lietuva* (Lithuanian), *Auttaja* (Finnish): daily Smyrna-week wire copy not read to the bottom; *Tabor Independent* (Czech, S. Dakota) not read.

## Sources
- """ + CA + """.
""" + sources([r for r in ROWS if r['node'] == NODE2]) + """
- Tier P (newspaper page, OCR confirmed). Translations are the vault's own, not the papers'. Hungarian, Polish, Czech, Slovak, Slovenian and Yiddish OCR is noisy: quotes are the clauses that survive it.
"""

note("Events", NODE1, {"type": "event", "when": "1930 – 1935", "tags": ["event", "verified", "united-states", "spanish-language-press"]}, E1)
note("Events", NODE2, {"type": "event", "when": "1922 – 1938", "tags": ["event", "verified", "united-states", "immigrant-press"]}, E2)
print("census r8 ethnic press: 2 events,", len(ROWS), "gazes")
