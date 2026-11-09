# -*- coding: utf-8 -*-
# Census round 6 (Oct 2026) — contemporary (1919–1937) continental press with stated views (slug: continental_press).
# Routes (both free, scriptable): KB/Delpher SRU (jsru.kb.nl, collection DDD_artikel) + resolver.kb.nl article OCR;
# Gallica services/Issues + services/ContentSearch read through the `fetch` wrapper (fragment-level only).
from _lib import note

KB = "https://resolver.kb.nl/resolve?urn="
GAL = "https://gallica.bnf.fr/ark:/12148/"
OCR = ("Dutch quotations are copied exactly as the KB/Delpher OCR gives them (the OCR of 1920s newspaper print is noisy; "
       "I quote only runs that read cleanly). Confessional labels (Catholic, Protestant, social-democratic) come from the "
       "paper's own KB subtitle where it has one and otherwise from general knowledge of the Dutch press, and are marked as such.")

E = [

# ---------------------------------------------------------------- DUTCH, CALIPHATE
("Dutch Confessional Press and the Fall of the Caliphate, March 1924", "March–July 1924", """
The Grand National Assembly voted the abolition of the caliphate on 3 March 1924, and the Dutch papers of
4–6 March are nearly all wire copy (Reuter, Havas, B.T.A.). This card is about the minority that added a voice.
The pattern is simple: the confessional dailies, Catholic and Protestant, saw a Muslim world and a Christian
minority put at risk by a secularising dictator, and none of them praised it. The liberal and colonial papers mostly
reported. Context: [[Abolition of the Caliphate]]; the Malay-world equivalent is [[Malay Press and the Fall of the Caliphate]].

**Het Centrum** (Utrecht Catholic daily). *Kijkjes op de Wereld*, 6 March 1924 ([article](""" + KB + """ddd:010001277:mpeg21:a0117)):
*"Men kent de feiten: eerst zette Kemal Pacha. de Mussolini der Turken.- den Sultan af"* — Kemal as the Turkish Mussolini,
who deposed the Sultan and so shook the whole Mohammedan world. A passage the OCR garbles carries a Catholic point: Catholic
schools and mission posts in Turkey have been ordered to remove the outward signs of their faith, and the great powers will
do nothing, as they did nothing about the persecution of Armenians and Greeks — *"Een oliebron of kolenveld is wel wat moorden waard !"*
Four days later ([10 March](""" + KB + """ddd:010001280:mpeg21:a0120)) the same column mourns the amiable old caliph and says that
Kemal *"met zijn moderne, wat helaas gelijk staat met antl-religi«use begrippen, heeft vele Oosterlingen geraakt aan wat hun zeer dierbaar is: het geioof"* (OCR as printed);
the clean part is *"heeft vele Oosterlingen geraakt aan wat hun zeer dierbaar is"* — he has struck Easterners at what is dearest to them, their faith.
"Modern" equals, "alas," anti-religious: the Catholic equation in one clause.

**Limburgsch Dagblad** (Catholic daily of Limburg). 12 March ([article](""" + KB + """ddd:010932966:mpeg21:a0009)): "De Turksche regeering dreigt zich
leélijk vast te werken met de afzetting van de kalief," and *"Een golf van godsdiensthaat gaat over Turkije"*, linked to the measures against foreign schools.
The same item concedes that Kemal raised the empire from the humiliation of the war and now wants to school it on the Western last — a conflicted, not simply hostile, reading.
On [19 July](""" + KB + """ddd:010933072:mpeg21:a0157), in a long piece headed "De Islam" that reads as a missionary reflection, the paper expects
*"Dat is zeker, dat het fanatisme zal toenemen"* and asks whether the Angora government's decision will not unite "het moderne heidendom" with the old, making the hope of converting the Muslim still more desperate (OCR garbles one word in that sentence; the gist is as stated).

**De Banier** (staatkundig-gereformeerd, i.e. orthodox Calvinist daily), 13 March ([article](""" + KB + """ddd:010852947:mpeg21:a0003)): in a weekly survey it records that the separation
of church and state was done "op aandrijven van Moestapha Kemal" and adds, noncommittal: *"Of de republiek hiermede versterkt of verzwakt is, blijft altijd nog een groote vraag"* — and turns to a sermon on a world in unrest.

**De Nederlander** (Protestant-Christian historical daily), 20 March ([article](""" + KB + """MMKB15:000693068:mpeg21:a00001)), the leader "Sultan en Khalief": *"Eerst hebben de Turken hun Sultan afgezet en nu is de Khalief gevolgd. Heel verstandig schijnt dat niet. Scheiding van Kerk en Staat klinkt heel aardig, maar voor Oostcrsche volken is die leuze minder gepast."*
Mohammedan faith held the Turks together and made them formidable; the Turks have now thrown their trumps away "ter wille van een Westersche abstractie, die voor hen niet deugt en die zij niet begrijpen." In the same column, in another paragraph, Kemal is "meer krijgsman dan staatsman." The judgement is on the act; it names Kemal only in passing.

**Bataviaasch Nieuwsblad** (Batavia, Dutch East Indies), 13 March ([article](""" + KB + """ddd:011071507:mpeg21:a0005)): the manner of the caliph's expulsion — the paper has just retold it from the Straits press — leads to the sentence *"Daaruit toch blijkt, wat men van de Jong-Turken te wachten heeft."* A colonial paper with Muslim subjects reads the Kemalists as the Young Turks again.

**Dry.** *De Tijd* (the Catholic daily) and *De Standaard* (the Anti-Revolutionary daily) both appear in the KB index for March 1924 but only as wire reports (*De Tijd*, 3 March, Reuter: Kemal's speech of 1 March "werd door de liberalen met geestdrift ontvangen, doch koeltjes door de geloovige en conservatieve minderheid"; 2 and 3 April *Het Centrum* wire reports on the assembly). No editorial of theirs on the abolition was found in the sample. *De Maasbode* appears in the KB index for September 1922 but none of its March 1924 items surfaced.

""" + OCR + """

## Sources
- KB/Delpher articles linked above (tier **P**, newspaper page text): Het Centrum 6 Mar 1924, 10 Mar 1924; Limburgsch Dagblad 12 Mar 1924, 19 Jul 1924; De Banier 13 Mar 1924; De Nederlander 20 Mar 1924; Bataviaasch Nieuwsblad 13 Mar 1924.
- Route: `jsru.kb.nl/sru/sru?version=1.2&operation=searchRetrieve&x-collection=DDD_artikel&query=…` then `resolver.kb.nl/resolve?urn=<id>:ocr`.
"""),

# ---------------------------------------------------------------- DUTCH, DICTATOR
("Dutch Dailies on the Dictator, 1924–1937", "1924–1937", """
Between the caliphate and the funeral ([[Dutch Press, November 1938]]), the Dutch word for Kemal was *dictator*. What the
dailies did with the word divides them. This card follows ten items in the KB/Delpher index, each of them an article with a stated or
implied view, and each from a paper that is not an obvious "Atatürk paper".

**Algemeen Handelsblad** (Amsterdam liberal daily), 29 October 1924 ([article](""" + KB + """ddd:010656761:mpeg21:a0174)), a special correspondent on
"De Turksche dictatuur": Kemal, the correspondent reports, argues that the People's Party saved Turkey and so has the right to exercise its dictatorship, though the constitution speaks of the whole people's sovereignty. *"heeft Moestapha Kemal veel van de extreme fascisten overgenomen"*, the correspondent concludes, the difference being that the fascists openly despise parliament while Kemal "verbergt deze echter achter de comedie van een parlement." The same article asks whether it is right to base a policy on one man's authority.

**De Volkskrant** (Catholic daily), 20 October 1926 ([article](""" + KB + """MMKB12:000137094:mpeg21:a00067)), "Turkije's nieuwste aanwinst": the statue of "den Tunkschen dictator Moestafa Kemal" in Constantinople, in a coat ("gekleede jas"), went up despite religious and artistic protest; *"de krachtfiguur van het moderne Turkije staat thans in een regenjas"* (on his pedestal). It is copied from the *Handelsblad* and the irony is mild.

**De Grondwet** (regional daily; confessional character not checked), 24 June 1929 ([article](""" + KB + """MMGARO01:000174605:mpeg21:a0025)), "Het oude en het nieuwe Turkije": asked whether Angora could bear the full truth, "in een staat waar een volledige dictatuur heerscht", the paper says the uprisings and plots are made by people attached to their fathers' faith, *"die in het hervormingswerk van den dictator een vernietiging zien van den Islam"*, and doubts a whole cultural revolution is possible in the time the dictator allows. Four years later ([28 Oct 1933](""" + KB + """MMGARO01:000177892:mpeg21:a0079), "Kemal Pascha tien jaar dictator") it writes that *"heeft president Kemal pasja, de dictator van het land, een volkomen nieuw rijk gevormd"* — and, in the same article, that democrats, Kurdish leaders and orthodox believers "werden allemaal als misdadigers ... opgehangen."

**De Tijd** (Catholic "godsdienstig-staatkundig dagblad") three times. 16 June 1930 ([verse](""" + KB + """ddd:010532214:mpeg21:a0148)), a comic poem signed Martin Berden: *"Kemal zwaait den dirigeerstok Als dictator in zijn land, Doch critiek wil hij niet hebben"* (verse lines run together), with Turkish journalists dancing to the cell. 30 March 1933 ([article](""" + KB + """ddd:010535257:mpeg21:a0051)), in an essay on what marks fascism, a one-party state is "de dictatuur van Kemal in Turkije op de Republikeinsche Partij", set beside Moscow and Rome. 28 June 1934 ([article](""" + KB + """ddd:010535720:mpeg21:a0003)), *Cosmopolitica*, "De appel van Kemal": waiting and tea-drinking is the motto of the "Turkendictator", and *"een der uitstekendste heerschersdeugden van den ghazi"* is patient waiting for the apple to fall.

**Voorwaarts** (social-democratic daily), 23 August 1930 ([article](""" + KB + """ddd:010212863:mpeg21:a0040)), "Het nieuwe Turkije": Kurdish bitterness has grown under the regime Mustafa Kemal has run since the start of the dictatorship he began exercising in 1923, which has denied every old social and religious form and, "nadat hy al zün tegenstanders met kogel of strop onschadelijk had gemaakt," driven Turkey toward a modern order with gendarmes' bayonets. The line is *"tegenstanders met kogel of strop onschadelijk had gemaakt"*.

**De Telegraaf**, 18 July 1931 ([article](""" + KB + """ddd:110570965:mpeg21:a0001)), "Een geslaagde dictatuur", by Count Carlo Sforza: *"SLECHTS één van de na-oorlogsche dictators, Moestafa Kemal, schijnt een succes te zijn, althans tot dusver."* Kemal alone kept to a policy of self-restraint and gave up the caliphate's world pretensions. Sforza adds that he came to this conviction in 1919 as Italian High Commissioner in Constantinople. The view is Sforza's and is recorded on his note ([[Carlo Sforza]]) as a new, dated, primary utterance; the paper is its carrier.

**Haagsche Courant**, 15 September 1937 ([article](""" + KB + """MMKB04:000149289:mpeg21:a0019)), "Het nieuwe Turkije": Atatürk's democratic experiment of 1930 failed, he rules "volgens dictatoriale principes", yet *"Atatürk's dictatuur een zegen voor het land is geweest"* — he was not a dictator who despised democracy, and rules for his land and people. (The item may be syndicated copy.)

**Not recorded as gazes** (dictator label only, wire or caption): *De Standaard* 29 Dec 1932 (Kemal ordering the prayers in Turkish; "groote ontstemming" in conservative Muslim circles) and 25 Sept 1930 (Ismet "de rechterhand van den Turkschen dictator"); *Haagsche Courant* 30 Dec 1930, which says the reactionaries are "fel tegen Kemal pasja gekant, wegens diens leekenpolitiek"; *De Volkskrant* 25 Oct 1935 ("Op last van den dictator" the census house-arrest). *De Maasbode* did not surface among the roughly 700 articles retrieved.

""" + OCR + """

## Sources
- KB/Delpher articles linked above (tier **P**). Algemeen Handelsblad 29 Oct 1924 · De Volkskrant 20 Oct 1926 · De Grondwet 24 Jun 1929 and 28 Oct 1933 · De Tijd 16 Jun 1930, 30 Mar 1933, 28 Jun 1934 · Voorwaarts 23 Aug 1930 · De Telegraaf 18 Jul 1931 · Haagsche Courant 15 Sep 1937.
- Route: SRU query `Kemal and (dictator or dictatuur or dictatorschap) and date within "01-01-1924 31-12-1937"` (1,390 hits), 300 retrieved and resolved to OCR.
"""),

# ---------------------------------------------------------------- DUTCH, SMYRNA
("Dutch Dailies at Smyrna, September 1922", "12–26 September 1922", """
The Dutch dailies of September 1922 handled Smyrna as wire news. Two items from the KB index show how Kemal appeared
in them; neither is an editorial, and the card is deliberately short. Context: [[Burning of Smyrna]]; Paris
on the same days: [[Paris Reads Smyrna and the Straits, September 1922]].

**De Grondwet**, 18 September 1922 ([article](""" + KB + """MMGARO01:000172985:mpeg21:a0018)), "Telegrammen. De brand-ramp van Smyrna": a Constantinople wire collecting
British refugees' accounts (the fire set on purpose; Turkish soldiers ringing survivors inside the burning area; the Greeks' own retreat marked by arson). The wire's summary: *"De algemeene indruk, door de verhalen alhier gewekt is, dat Moestafa Kemal de schoonste gelegenheid van zijn leven heeft laten voorbijgaan"* — had he held his troops in check he would have won a moral victory greater than over the Greek army. The view is the unnamed correspondent's and the newspaper carries it; the same page prints the Turkish claim that arrested persons confessed to the arson.

**De Volkskrant** (Catholic), 22 September ([article](""" + KB + """MMKB12:000132218:mpeg21:a00020)): the Catholic angle of the Smyrna news is church property (the archbishop's residence destroyed; the cathedral and other Catholic churches spared) and Christians marched inland. It also reports *"Kemal heeft beloofd dat de banken van die maatschappij door hem zullen worden beschermd"* (of Standard Oil) and the hope that the Allies' advice will bring Kemal to respect the neutral zone. No view of Kemal is stated; recorded as witness. On 16 September the same paper printed Kemal's reported peace terms and the fire's toll (60,000 Armenians and Greeks homeless, 1,000+ dead).

**De Standaard** (Anti-Revolutionary), 14–15 September, runs "Britsche persstemmen" and a "De les van Smyrna" passage that draws only a lesson about force and treaties; on 26 September a French commissioner presses "Kemal" to evacuate the neutral zone. No view of him is stated.

""" + OCR + """

## Sources
- KB/Delpher: [De Grondwet 18 Sep 1922](""" + KB + """MMGARO01:000172985:mpeg21:a0018) · [De Volkskrant 22 Sep 1922](""" + KB + """MMKB12:000132218:mpeg21:a00020) · [De Volkskrant 16 Sep 1922](""" + KB + """MMKB12:000132213:mpeg21:a00034) · [De Standaard 14 Sep 1922](""" + KB + """MMKB23:001849065:mpeg21:a00004) (tier **P**).
"""),

# ---------------------------------------------------------------- PARIS 1924-33
("Paris Press on the Caliphate, the Civil Code and the Decade, 1924–1933", "1921–1933", """
A second French card built on Gallica's page-level `ContentSearch` fragments, for the moments between the Smyrna card and the
funeral card: the caliphate (3 March 1924), the Swiss Civil Code (17 February 1926) and the republic's tenth anniversary (29 October 1933).
Fragments are short and cut with "(...)", so only what a fragment shows is claimed. The French OCR is noisy (e.g. "provo qua"); quotations are as the OCR gives them.
Context: [[Abolition of the Caliphate]], [[Turkish Civil Code]].

**La Croix** (Catholic daily). 8 March 1924, page 1 ([issue](""" + GAL + """bpt6k261790c)), "Gazette": under the heading (OCR) *Le « milliard des Congrégations » en Turquie* the paper says that, "En abolissant le califat, le gouvernement d'Angora(...)"
and then: *"Ceux qui leur ont parlé du fameux milliard des Congrégations de France ont sans doute omis de leur dire comment le milliard s'est, évanoui"* — those who told Angora about the famous "billion of the Congregations" in France forgot to say how the billion vanished (and tells "l'histoire du forçat Duez"). The reading — Ankara imitating French anticlerical confiscation, and being misled by it — is an inference from a truncated paragraph.
(A 9 March item cited in the first draft of this card could not be found in the cited issue on re-check and has been withdrawn.) 6 March, page 5 ([issue](""" + GAL + """bpt6k2617882)) the paper's press-review relays L'Écho de Paris (OCR-garbled) that the veneration went "non au calife, mais au sabre, et le sabre est aux mains de Ketnal" [OCR]; this is a relayed paper's view, not La Croix's own, and is not recorded.

**Le Temps**, 19 February 1926, page 6 ([issue](""" + GAL + """bpt6k246148q)): the Turkish Chamber has decided unanimously to adopt the Swiss Civil Code in its entirety, and *"Ce vote consacre la séparation du statut civil et des traditions religieuses"* ("dans'la vie publique et sociale'du peuple turc" [OCR]). Kemal is not named; whether the gloss is the paper's or the dispatch's is not shown. The same day *L'Action française* p.3 sets the item under "TURQUIE La laïcisation de la Turquie", and *La Croix* p.2 prints the Swiss-code news without comment in the fragment.

**L'Action française**, 31 October 1933, page 1 ([issue](""" + GAL + """bpt6k765409w)): apparently on Greek-Turkish friendship (page 2: "Ainsi naquit i'amitiê. gréco-turque" [OCR]), "Depuis l'été de 1922, où *la victoire de Mustapha Kemal provo qua la faillite catastrophique* de la mèga[lomanie]" — the fragment ends there. **Le Populaire** (Socialist), 30 October 1933, page 3 ([issue](""" + GAL + """bpt6k8213624)) heads its Ankara dispatch *"L'anniversaire de la République kemaliste"*; a nearby fragment adds "De grandes fêtes ont été célébrées par les ordres de l'autorité dans toutes les villes de Turquie" (not confirmed to be the same dispatch). *L'Humanité* of 30 October, p.2, reports the military review ("Ce matin, du haut d'une tribune, Mus tapha Kemal" [OCR]) without a stated view in the fragment.

**Dry.** Franklin-Bouillon accord, 20–22 October 1921: *Le Temps* (22 Oct, p.1) says the signing is awaited and that the talks aimed "avant tout à obtenir la libération des prisonniers français"; *L'Humanité* (22 Oct, p.3) reports a rumoured French promise to help Turkey retake Smyrna and Thrace; neither fragment gives a view of Kemal, and the 23rd and 24th (Temps, AF, Humanité, Figaro, Populaire) returned no hit for "Franklin". Lausanne, 25 July 1923: *La Croix* p.5 notes that Ismet signed "avec une plume en or que lui avait envoyé d'Angora Mustapha Kemal"; *L'Humanité* p.3 says the treaty "consacre l'existence de la Turquie libre"; *L'Action française* p.1 relays Achille Mestre on the capitulations. Alphabet (Nov 1928) and women's vote (Dec 1934): nothing Kemal-related in the fragments for 2–3 Nov 1928 and 6–7 Dec 1934 (*Le Temps* 7 Dec 1934 p.3 has the Ankara measure on clerical dress and the Assembly's new seat count only). *L'Humanité* 5 Mar 1924 p.3 ("Plus de Calife, commandeur des Croyants...") has no explicit view in its fragment.

## Sources
- Gallica (tier **P**, fragments via `services/ContentSearch?ark=<issue>&query=<word>`; issue arks by `services/Issues?ark=ark:/12148/<title>/date&date=<year>`): La Croix [8 Mar 1924](""" + GAL + """bpt6k261790c), [9 Mar 1924](""" + GAL + """bpt6k261791r), [6 Mar 1924](""" + GAL + """bpt6k2617882) · Le Temps [19 Feb 1926](""" + GAL + """bpt6k246148q) · L'Action française [31 Oct 1933](""" + GAL + """bpt6k765409w) · Le Populaire [30 Oct 1933](""" + GAL + """bpt6k8213624).
- Title ids: Le Temps cb34431794k · La Croix cb343631418 · L'Humanité cb327877302 · L'Action française cb326819451 · Le Populaire cb34393339w · Le Figaro cb34355551z.
"""),
]

for n, when, b in E:
    note("Events", n, {"type": "event", "when": when, "tags": ["event", "verified", "obituary-corpus"]}, b)

print(f"census r6 continental_press: {len(E)} cards")
