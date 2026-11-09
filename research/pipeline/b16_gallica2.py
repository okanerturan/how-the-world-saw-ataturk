# -*- coding: utf-8 -*-
# Census round 8 (Oct 2026) — French press, 1920–1924, second Gallica sweep (slug: gallica2).
# Method: Gallica services/Issues (issue arks) + services/ContentSearch (page-level OCR fragments), read via the `fetch` wrapper.
from _lib import note

GAL = "https://gallica.bnf.fr/ark:/12148/"
METH = ("Every quotation below is a Gallica `ContentSearch` fragment copied exactly as the OCR gives it (so \"Moustapha\", \"Mustapha\", "
        "\"Kernal\" for Kemal and other OCR slips are kept, marked [OCR] where they matter). Fragments are short and are cut with \"(...)\"; "
        "\"PAG_n\" is Gallica's view number (the n-th image of the issue, not always the printed page). Only what a fragment shows is claimed.")

E = [

# ---------------------------------------------------------------- CILICIA 1920
("Paris Press and the Cilicia War, February 1920", "February 1920", """
The French garrison of Marash left the town on 10–12 February 1920 under Turkish fire, the opening disaster of the Cilicia war against Kemal's
nationalists. This card is about what the Paris dailies of 11–27 February 1920 let slip about Kemal himself. It is thin: nearly every
fragment is Havas copy. """ + METH + """

**Le Matin**, 13 February 1920, view 3 ([issue](""" + GAL + """bpt6k5731487)): a passage on the Constantinople government and the Allies says of
someone *"En rapports étroits [avec] Mustapha Kemal, i'hornme des Enver îocha et des ïalaat, il dicte ses vülontés à eus les gouvernements"* [OCR] —
Kemal as the man of Enver Pasha and Talaat, the wartime Young Turk chiefs, dictating to every government. The OCR does not show whether the
closing "il" is Kemal or someone close to him, so the hostile reading rests on the Enver–Talaat label, which attaches to Kemal in either case.
The same issue, view 1, has the paper's peace-terms line that France would "se contentant en Cilicie d'un traitement préférentiel peur son commerce [OCR]"
(no view of Kemal). *L'Humanité* of the same day (view 1) attacks the cost of the "expédition de Syrie et de Cilicie" ("deux millions par jour") without naming Kemal.

**Wire only.** *Le Temps*, 11 February, view 2: the Constantinople Chamber, "constituée par des députés nationalistes qui obéissent au mot d'ordre
de Moustapha Kemal pacha", made the talks laborious; 27 February, view 1: "On affirme ... que Moustapha Kemal a reçu de Constantinople l'ordre de cesser
toute action contre les forces françaises". *La Croix*, *L'Action française*, *L'Humanité*, *Le Figaro* returned no Kemal fragment on 13–14 February.
Dug further for the soldiers' war (Marash, Aintab, Urfa): the search stems "Marache" to "marche" and returns market reports; nothing usable.

## Sources
- Le Matin, 13 Feb 1920, view 3 — Gallica [bpt6k5731487](""" + GAL + """bpt6k5731487). Le Temps [11 Feb](""" + GAL + """bpt6k243918b) · [27 Feb 1920](""" + GAL + """bpt6k243934h). L'Humanité [13 Feb 1920](""" + GAL + """bpt6k299579d).
- Tier **P** (OCR fragments of the newspaper pages via `services/ContentSearch?ark=<issue>&query=<word>`; issue arks from `services/Issues?ark=ark:/12148/<title>/date&date=1920`). Le Matin title id cb328123058.
"""),

# ---------------------------------------------------------------- SMYRNA, SECOND READING
("Paris Dailies on Kemal's Victory, 11–17 September 1922", "11–17 September 1922", """
A second pass over the Smyrna fortnight, complementing [[Paris Reads Smyrna and the Straits, September 1922]] (which reads 13–17 September from
*L'Action française*, *L'Humanité*, *Le Figaro*, *Le Temps*). This one looks at 11, 12, 14, 15 and 17 September and keeps only fragments in which the paper
itself, not a dispatch, judges Kemal. Most of the fragments are Havas or Times relays ("Vive Kemal pacha", the "réception triomphale" at Smyrna). """ + METH + """

**Le Temps**, 11 September, view 1 ([issue](""" + GAL + """bpt6k2448592)), answers the London *Evening Standard*: *"On pourrait répondre [aux] insinuations de l'Evening Standard que Moustapha Kemal et ses officiers d'état-major ne sont pas des « paysans incultes »"*, and cites General Townshend (back from Angora) on "le remarquable effort industriel d'Angora". The semi-official daily is defending Kemal's competence against the British press, four days before it shifts to warning notes on the Straits. On 15 September, view 1 ([issue](""" + GAL + """bpt6k2448634)), a political paragraph says *"Moustapha Kemal se rend parfaitement compte que les Français, les Anglais et les autres alliés s'opposeraient ensemble à une tentative quelconque [sur] Constantinople"* — a cool analyst's reading of him as a realist (whether the sentence is the paper's or a correspondent's is not shown).

**L'Humanité**, 11 September, view 3 ([issue](""" + GAL + """bpt6k400518q)): *"Kemal peut cependant '.atteindre l'impérialisme britannique en Asie"* [OCR], by a rapprochement with the Arabs of Mesopotamia and Palestine or by working Afghanistan — the Communist daily reads the victory as a blow at British imperialism, with no word of admiration for the man.

**Le Populaire** (Socialist), 11 September, view 1 ([issue](""" + GAL + """bpt6k8181715)), is wary: *"Que Fehrid bey et Mustapha Kernal écoulent certains conseils qui leur viennent de Moscou, un nouveau conflit s'ensuivra dans les Balkans"* [OCR "Kernal", "écoulent" for "écoutent"], with all central Europe drawn in. View 3 of the same issue adds that "Kemal pacha" was encouraged by the Sublime Porte itself, "à l'exception de certains éléments pro-britanniques amis de Damad Ferid pacha" — the sentence is cut there.

**L'Action française**, 17 September, view 3 ([issue](""" + GAL + """bpt6k7613473)): a short fragment, its lead-in cut: *"Moyistapha Kémal se méfie et il a rai son"* [OCR: "Moustapha Kémal se méfie et il a raison"] — Kemal is wary, and right to be. What he is wary of, and whether the line is the paper's own view, the fragment does not show. (View 1 of the same issue: "Constantinople par les forces de Mustapha Kemal, constituerait un événement désastreux", a dispatch.) The 15 September issue also relays unnamed papers that say Kemal's victory "est d'un exemple pernicieux" and teaches the Germans that a treaty can be shed by force; the fragment does not show whose view that is, so it is not recorded.

**Dry.** *La Croix* 14 September, view 1 has a headline fragment "Mustapha Kemal pacha ... atrocités grecque[s]" and view 2 the Havas line that Kemal will hold responsible the Greeks who committed atrocities; no editorial voice. *Le Figaro* and *La Croix*: dispatches only. *Le Temps* 17 September, view 3 carries an interview in which someone calls Kemal "un homme toujours bien équilibré" — the speaker's name is not in the fragment.

## Sources
- Le Temps [11 Sep 1922](""" + GAL + """bpt6k2448592) · [15 Sep 1922](""" + GAL + """bpt6k2448634). L'Humanité [11 Sep 1922](""" + GAL + """bpt6k400518q). Le Populaire [11 Sep 1922](""" + GAL + """bpt6k8181715). L'Action française [17 Sep 1922](""" + GAL + """bpt6k7613473) · [15 Sep](""" + GAL + """bpt6k761345b). La Croix [14 Sep 1922](""" + GAL + """bpt6k261334k). Le Figaro [17 Sep 1922](""" + GAL + """bpt6k293340p).
- Tier **P** (Gallica `ContentSearch` OCR fragments; issue arks from `services/Issues`).
"""),

# ---------------------------------------------------------------- ANKARA ACCORD OCT 1921
("Paris Press and the Franklin-Bouillon Accord, October 1921", "20–29 October 1921", """
The Franco-Turkish (Ankara) agreement was initialled by Henry Franklin-Bouillon and Yusuf Kemal Bey on 20 October 1921, ending the Cilicia war on terms that handed Ankara the evacuated zone. The press fought over it, but through the fragments Gallica returns the dailies of 21–29 October are almost all dispatch and parliamentary reporting; Kemal himself is rarely named and no editorial voice on him survives the search. Recorded as a dry end so that nobody repeats it. """ + METH + """

What the fragments do show. *Le Temps*, 23 October, view 2 ([issue](""" + GAL + """bpt6k2445369)) heads its dispatch "L'accord franco-turc ... L'accord franco-kémaliste a été signé hier", and view 3 carries Briand's Chamber statement that "l'Assemblée d'Angora a accepté de régler, en accord avec nous, nos intérêts particuliers de frontière en Syrie et en Cilicie". *Le Figaro*, 23 October, view 3 ([issue](""" + GAL + """bpt6k293010q)) prints the Turkish information bureau's note on what the accord covers. *L'Action française*, 25 October, view 3 ([issue](""" + GAL + """bpt6k761020t)): "La satisfaction règne à Constantinople". *Le Populaire*, 26 October, view 3 ([issue](""" + GAL + """bpt6k817852r)), relays the Turkish papers' report that the "convention franco-kémaliste" was ratified in Angora by a large majority and adds: "Il faut espérer que l'accord d'Angora ne restera pas lettre morte comme celui qui fut signé à Londres avec Bekir Sami" — hope with a memory of the broken London agreement, aimed at the Allies' good faith rather than at Kemal. *Le Temps*, 28 October, view 3 ([issue](""" + GAL + """bpt6k244541r)) records a deputy in the Chamber debate rejecting Franklin-Bouillon's "politique absolue, magnifique sur le papier" for a "politique libérale ... plus humaine et par conséquent plus française". *L'Humanité*, 22 October, view 3 ([issue](""" + GAL + """bpt6k400193b)) reports the rumoured French promise to help Turkey retake Smyrna and Thrace and an official denial. None of these is a judgment of Kemal, so none is recorded.

Next step (not done, Gallica's fetch route began returning 429 rate limits with retry-after times of 10–13 minutes): look for the October–November 1921 leaders in *Le Matin* (issues not loaded for 1921), *L'Écho de Paris*, *Le Journal des débats* and *L'Œuvre*, and the Chamber debate of 28 October in the *Journal officiel* rather than the press.

## Sources
- Le Temps [23 Oct](""" + GAL + """bpt6k2445369) · [28 Oct 1921](""" + GAL + """bpt6k244541r). Le Figaro [23 Oct 1921](""" + GAL + """bpt6k293010q). L'Action française [25 Oct 1921](""" + GAL + """bpt6k761020t). Le Populaire [26 Oct 1921](""" + GAL + """bpt6k817852r). L'Humanité [22 Oct 1921](""" + GAL + """bpt6k400193b).
- Tier **P** (Gallica `ContentSearch` OCR fragments).
"""),

# ---------------------------------------------------------------- CALIPHATE 1924
("Paris Dailies and the Abolition of the Caliphate, March 1924", "4–7 March 1924", """
The Grand National Assembly abolished the caliphate on 3 March 1924. The Paris dailies of 4–7 March are mostly Havas copy; this card keeps the places where
a paper speaks in its own voice about Kemal. It extends [[Paris Press on the Caliphate, the Civil Code and the Decade, 1924–1933]], which reads La Croix of 6 and 8 March, and it corrects that card: a La Croix item first attributed to 9 March is in fact in the **7 March** issue. Context: [[Abolition of the Caliphate]]. """ + METH + """

**La Croix** (Catholic), 7 March 1924, view 1 ([issue](""" + GAL + """bpt6k261789f)) — the second article of a series (the text refers to "le premier article dans la Croix du 4 mars"). The fragments run: a protest against *"cette intolérance jeune-turque qui, incapable de mettre sur pied des écoles, s'efforce de détruire celles que la France a multipliées dans le monde ottoman"*; then *"Je sais bien les excuses que donnent à cette politique sectaire des journaux comme le Temps, toujours prêts à saluer la « laïcité »"*; then *"Mustapha Kemal ne ferme pas les écoles chrétiennes, disent(...)Et, puisque Mustapha Kemal prétend inaugurer(...)"* — a Catholic paper doubting the line that Kemal spares Christian schools and, by name, reproaching *Le Temps* for applauding Turkish secularism. This is the quotation of the withdrawn 9 March record, now found in its right issue; the truncation after "prétend inaugurer" means the paper's full sentence is not shown.

**Le Temps**, 5 March, view 1 ([issue](""" + GAL + """bpt6k2453995)), leader on the Turkish decisions: *"La politique laïque et nationale qui se développe ainsi"*, and, in contrast with the Caliph's protest, *"En revanche, ces principes sont compris et maintenus par Moustapha Kemal pacha"* [OCR "Moustapha' Kemal paclia"]. The same view shows the counter-voices it reports: that the suppression "indigne les musulmans de l'Inde" and that "on va trop loin". Which principles the leader means is cut off in the fragments.

**Journal des débats**, 5 March, view 1 ([issue](""" + GAL + """bpt6k490711v)): a long account of the fall of the Caliph names *"Moustafa Kémal le Victorieux"* as the man whose "contrôle le plus strict" over the new elections removed most hodjas and brought in partisans of the lay regime, says he "vivait à l'occidentale" with a wife unveiled, and that he "aurait voulu qu'on ne bannit pas [OCR: \"ho bannit\"] les membres de la famille impériale" and had put down a motion (\"présenté à cet effet une motion\") to that effect.

**Le Petit Journal**, 5 March, view 1 ([issue](""" + GAL + """bpt6k628753x)): "Le raisonnement de Mustapha Kemal pacha et de ses partisans est des plus simples" and a clause that Kemal and the Assembly "n'avaient pas osé bou[le]verser" — an explaining voice, no judgment in the fragment.

**L'Humanité**, 5 March, view 3 ([issue](""" + GAL + """bpt6k401251s)), under "Après la suppression": the speech Kemal gave on Saturday "n'était que le prélude des décisions importantes que vient d'adopter l'Assemblée nationale turque". **Le Populaire**, 4 March, view 3 ([issue](""" + GAL + """bpt6k818709n)): "Le discours de Kemal ... Mustapha Kernel a relevé la volonté ferme de la nation turque d'assurer des bases solides au régime républicain" [OCR]. Both report; neither judges.

## Sources
- La Croix [7 Mar 1924](""" + GAL + """bpt6k261789f). Le Temps [5 Mar 1924](""" + GAL + """bpt6k2453995). Journal des débats [5 Mar 1924](""" + GAL + """bpt6k490711v). Le Petit Journal [5 Mar 1924](""" + GAL + """bpt6k628753x). L'Humanité [5 Mar 1924](""" + GAL + """bpt6k401251s). Le Populaire [4 Mar 1924](""" + GAL + """bpt6k818709n).
- Tier **P** (Gallica `ContentSearch` OCR fragments; issue arks from `services/Issues`). Title ids: Le Temps cb34431794k · La Croix cb343631418 · Journal des débats cb39294634r · Le Petit Journal cb32895690j · L'Humanité cb327877302 · Le Populaire cb34393339w.
"""),
]

for n, when, b in E:
    note("Events", n, {"type": "event", "when": when, "tags": ["event", "verified", "obituary-corpus"]}, b)

print(f"census r8 gallica2: {len(E)} cards")
