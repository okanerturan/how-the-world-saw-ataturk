# -*- coding: utf-8 -*-
# Census round 5 (Oct 2026) — Europe, primary newspaper evidence (slug: europe_primary).
# Method seam: Gallica's own page-level search service (services/ContentSearch) returns the OCR'd
# page text around a hit for any issue ark; Hansard's public search API (hansard-api.parliament.uk)
# returns full contribution text. Both read through the paid-free `fetch` wrapper. See LEDGER rows.
from _lib import note

GAL = "https://gallica.bnf.fr/ark:/12148/"
CAVEAT_OCR = ("Gallica's OCR is noisy; every French quotation below is copied exactly as the OCR gives it, "
              "with obvious misreadings flagged [OCR] rather than silently mended. The page text was read as "
              "search-hit fragments (Gallica's `ContentSearch` service), not as whole articles, so what follows is "
              "what the fragments say and no more.")

E = [

# ---------------------------------------------------------------- PARIS 1938
("Paris Reads the Death, 11–12 November 1938", "11–12 November 1938", """
The French press of the morning after is the first card in the census built on the newspaper pages
themselves rather than on a Turkish digest of them. It is also the card where the left–right split
is plainest, and where the day's other news is part of the evidence: the same front pages carry
the Kristallnacht pogrom (night of 9–10 Nov) and the Munich-aftermath arguments over colonies and
armaments, so every paper reads the death of the Turkish president through whatever it was already
afraid of.

**Le Figaro, 11 Nov 1938** (conservative daily; [issue](""" + GAL + """bpt6k4100383)). Front page:
**"Hommage à Mustapha Kemal"**, signed by a former French ambassador at Ankara (the byline is OCR-garbled and
I do not resolve it), opens: *"Dans le jeu troublé de l'Europe, une des cartes maîtresses vient d'être
abattue par le destin"* — a master card of Europe's troubled game struck down by fate — and has him
*"orgueilleux de son œuvre civilisatrice,"* yet speaking of his victories *"avec modestie."* The same page's report
from Istanbul puts the new state *"sur les ruines d'un empire disparate"* and says: *"A Stamboul, il n'y a
plus de pleureuses officielles, mais un peuple en pleurs veille sur son cercueil."* Page 6 turns to the
category problem that Paris could not avoid: *"Ce n'était pas comme Hitler ou Mussolini, l'homme du peuple arrivé au
pouvoir et dans cet Etat également totalitaire, le mot de dictateur était soigneusement proscrit"* — he was not,
like Hitler or Mussolini, a man of the people risen to power, and in this equally totalitarian state the word
"dictator" was carefully avoided. Page 2, on the fez, still calls him *"le président-dictateur."* The same
page 6 notes with satisfaction that the Franco-Turkish friendship treaty of 4 July had "consacré la reprise de
l'influence française en Turquie."

**L'Humanité, 11 Nov 1938** (Communist daily; [issue](""" + GAL + """bpt6k4076255)). The photo caption on the
front page, under the Berlin pogrom headlines, gives the party line in one clause: Kemal Atatürk, *"qui libéra la
Turquie du joug du califat et des visées anglaises, et dont la disparition peut favoriser la poussée
hitlérienne"* — who freed Turkey from the caliphate's yoke and from British designs, and whose disappearance may
favour the Hitlerite push [OCR "anglâises"]. The page-3 obituary then splits the portrait. It lists the
reforms (caliphate, religious courts, harem, veil and fez, Latin letters), and adds in the same breath:
*"Disons cependant que le gouvernement d'Ataturk exerça une répression féroce contre le mouvement socialiste et
communiste."* — Let us say, however, that his government exercised a ferocious repression against the socialist
and communist movement. But it closes by asking whether the death of the man *"qui basa la politique extérieure
de son pays sur l'indépendance nationale, l'amitié avec l'U.R.S.S. et la France"* will not let "Turkish reaction"
allow Hitlerite penetration of the Near East to grow. The Communist paper's Atatürk is both jailer of its
comrades and a bulwark against Berlin, and it wrote both in the same column — the clearest *conflicted*
gaze in the French set.

**Le Temps, 11 Nov 1938** (the semi-official establishment daily; [issue](""" + GAL + """bpt6k263753p)). Index
line on the front page: "Mort de Kemal Ataturk," with the full retrospective on page 2, which recalls the
Constantinople of 1919, *"délaissée par le commandeur des croyants et où la langue grecque était plus parlée
que le turc,"* and ends on Turkey as *"leader de l'Entente balkanique, promotrice du pacte oriental"* that "has
marked its place in the world." Fragment-level only here: the Temps card is a record of how official Paris
filed the death, not of a stated judgement.

**L'Action française, 11–12 Nov 1938** (royalist–nationalist; [11 Nov](""" + GAL + """bpt6k767243x),
[12 Nov](""" + GAL + """bpt6k7672449)). 11 Nov, front page "La mort de Kemal Ataturk," and on page 2 the paper's
own reading: *"Le grand secret de Kemal n'aura-t-il pas été de comprendre que derrière la dentelle romantique de
l'empire ottoman [OCR "denteile"], il n'y avait plus rien, sinon des hommes prêts à défendre le sol national"* — the
Ottoman lace had nothing behind it but men ready to defend the national soil — and, in the same
column, *"Kemal Ataturk, le « père de la patrie », disparaît au moment où l'Occident, plus que jamais, a les
regards tournés vers les Dardanelles."* It is a national-soil reading, with the Straits as the
point. The next day's page 5 carries a press-review item headed (as the OCR gives it) "Kemal Ataturk. Il y a des
enseignements à tirer de la vie du dictateur," which relays two other Paris papers: *L'Intransigeant*'s
Gallus ("Le dictateur de la Turquie vient de mourir et il sera passionnant d'observer ce qui va se passer dans
son pays") and Pierre Dominique in *La République* — whom the Action française item identifies, with
relish, as "ex-président fondateur de la section d'Action française de Sartène" — on the hanged old Turks and
conspirators, and on people who do not understand "qu'une révolution est tout autre chose qu'une bergerie." The
item's question *"Oui ou non, Kemal Ataturk a-t-il sauvé l'Etat ?"* is answered *"Tous les Turcs dignes de ce nom
répondent oui."* (Whose answer the last sentence is — the paper's or the quoted columnist's — the fragments do not show;
treat it as the review's.) The same page 2 of 12 Nov also prints an agency report that the Turkish Assembly had
voted to rename Ankara "Ataturk"; I have not checked it against the Turkish record, and Ankara's name did not
change, so read it as a wire error or a rumour.

**The rest, in headlines.** *Le Populaire* (Socialist), 11 Nov: "Le président Ataturk est mort," with a
"La vie de Kemal Ataturk" box. *Le Petit Parisien*, 11 Nov, front page: **"Kemal Atatürk, le père de la Turquie,
est mort"**. *L'Ouest-Éclair*
(Rennes), 11 Nov, p. 4, interviews a Turk it calls "Burhaneddin Bey": Atatürk *"mérite d'être tenu comme le
plus grand réformateur que l'Orient ait créé"* — and the interviewer asks whether, he gone, "une réaction est-elle
possible" (unresolved speaker; his, not the paper's, gaze). On 12 Nov *Le Figaro* (p. 3) prints a session report — apparently the Turkish Assembly's — that opens with the
government's communication on the death of *"le grand chef libérateur, Kemal Ataturk"* and five minutes of silence.

**What the split shows.** The Right (*Figaro*, *Temps*, *Action française*) read him through the
Straits and French influence and could not decide whether to say "dictator"; the Left (*Humanité*) read him
through Berlin and its own prisoners. Toksoy's digests put Turkish pathos in the foreground; the Paris pages, in the fragments read,
have exactly one line of it (the *Figaro* people in tears) and spend the rest on strategy. For the official French side of the funeral see
[[Foreign Delegations at the Funeral, November 1938]] and [[Albert Sarraut]]; for the German mirror of the same
week see [[Hamburger Tageblatt, November 1938]]; the event itself is [[Death and State Funeral of Atatürk]].

Caveat: """ + CAVEAT_OCR + """

## Sources
- Le Figaro, 11 Nov 1938, pp. 1, 2, 6 — Gallica [bpt6k4100383](""" + GAL + """bpt6k4100383) (12 Nov: [bpt6k410039g](""" + GAL + """bpt6k410039g))
- L'Humanité, 11 Nov 1938, pp. 1, 3 — Gallica [bpt6k4076255](""" + GAL + """bpt6k4076255)
- Le Temps, 11 Nov 1938, pp. 1–2, 8 — Gallica [bpt6k263753p](""" + GAL + """bpt6k263753p)
- L'Action française, 11 Nov 1938 pp. 1–2 [bpt6k767243x](""" + GAL + """bpt6k767243x); 12 Nov pp. 2, 5 [bpt6k7672449](""" + GAL + """bpt6k7672449)
- Le Populaire 11 Nov [bpt6k8232199](""" + GAL + """bpt6k8232199) · Le Petit Parisien 11 Nov [bpt6k6647367](""" + GAL + """bpt6k6647367) · L'Ouest-Éclair 11 Nov [bpt6k661436g](""" + GAL + """bpt6k661436g)
- Method: Gallica `services/ContentSearch?ark=<issue>&query=<word>` returns page-numbered OCR fragments; issue arks from `services/Issues?ark=<title>/date&date=1938`. Tier **P** (the newspaper pages, read as OCR fragments).
"""),

# ---------------------------------------------------------------- PARIS 1922
("Paris Reads Smyrna and the Straits, September 1922", "13–17 September 1922", """
In the week Smyrna burned (13–14 Sept) and the Chanak crisis opened, Paris was the one Allied capital that had
already signed its own separate peace with Ankara — the Franklin-Bouillon agreement of October 1921 (see
[[Franklin Bouillon]]) — and its press shows it. The pages below are 16–17 Sept 1922, read as OCR fragments
(see the caveat); the editorial voices are thinner here than in 1938, and where a fragment is a wire dispatch
rather than the paper's own words I say so.

**L'Action française, 16 Sept 1922** ([issue](""" + GAL + """bpt6k761346q)). Front page, on the war scare in the
Balkans: *"Après les déclarations de Fehti bey, celles de Moustapha Kemal, encore plus récentes et encore plus autorisées,
ne laissent pas paraître que les Turcs aient des idées déraisonnables"* — Fethi Bey's statements, then
Kemal's still-fresher and more authoritative ones, do not suggest the Turks have unreasonable ideas — and, in the
same column, *"De même, Moustapha Kemal semble modéré."* The same issue's page 2 runs the heading **"La victoire
turque et la question d'Orient"** and prints the dispatch "Moustapha Kemal pose ses conditions" (Angora, 12 Sept),
beside the Smyrna fire story: *"L'incendie de Smyrne. Smyrne est en flammes"*, with the wire's line that the
fire may have been set by Turkish irregulars who "arrived a few hours before Kemal Pasha made his entry into
Smyrna." The paper's frame is the one its politics predicted: the Turks as moderate victors, London as
the aggravator. (That last clause is my reading of the pairing, not a sentence in the fragments.)

**L'Humanité, 16 Sept 1922** ([issue](""" + GAL + """bpt6k4005235)). The Communist daily treats the crisis as an imperialist game: on page 1, *"l'Angleterre et la France capitalistes se livrent à la politique de force
qui réserve au monde les lendemains les plus tragiques."* Its page 3 dispatch (Berlin, 15 Sept) lists the Allies'
tangled promises — *"L'Angleterre a fait des promesses catégoriques à la Grèce; la France et l'Italie ont conclu des
pactes et avec le Royaume-Uni et avec Kemal"* — which is a wire summary, not the paper's own voice; on Kemal
himself the fragments give no personal judgement.

**Le Temps, 16–17 Sept 1922** (official Paris; [16 Sept](""" + GAL + """bpt6k244864h), [17 Sept](""" + GAL + """bpt6k244865w)).
The paper carries the burning ("Smyrne en feu… brûle depuis douze heures") as a dispatch, and reports Kemal's two
other faces in the same page: that he *"a édicté la peine de mort contre tous les soldats qui commettraient des excès"*
and "se déclara prêt à participer à une conférence de paix." On 17 Sept it prints the Allies' joint resolution:
a solemn warning to *"Moustapha Kemal"* not to violate the neutral zone, and reinforcements for the Allied
garrisons if he did. Page 1 of 16 Sept argues that the *"évacuation forcée de l'Anatolie, y compris Smyrne, par l'armée grecque"*
changes the whole shape of the problem. So France's official daily printed, in one issue, the
edict against atrocities and the fire.

**Le Figaro, 16 Sept 1922** ([issue](""" + GAL + """bpt6k293339r)) carries the Smyrna-fire dispatch and the Allied
resolution (reinforce the "drapeaux alliés" if Kemal threatened the Straits); no editorial fragment on him.

**Reading.** Nothing here is the Burning of Smyrna as a verdict — see [[Burning of Smyrna]] and the
Armenian-Greek record in [[Armenian Genocide]] for what the history says; this card is only how four Paris papers
placed Mustafa Kemal that week: moderate (*Action française*), a belligerent to be warned yet pledged to peace and
punishing excess (*Temps*), a pawn in the imperialists' game (*Humanité*). For the English-speaking side of the same
fortnight see [[Chanak Crisis]] and [[Canada Says Not Yet at Chanak, September 1922]].

Caveat: """ + CAVEAT_OCR + """ The Action française and Humanité attributions rest on front-page fragments; whether
each is the paper's editorial or a quoted dispatch could not be seen.

## Sources
- L'Action française, 16 Sept 1922, pp. 1–2 — Gallica [bpt6k761346q](""" + GAL + """bpt6k761346q)
- L'Humanité, 16 Sept 1922, pp. 1, 3 — Gallica [bpt6k4005235](""" + GAL + """bpt6k4005235)
- Le Temps, 16 Sept 1922 pp. 1–2 [bpt6k244864h](""" + GAL + """bpt6k244864h); 17 Sept [bpt6k244865w](""" + GAL + """bpt6k244865w)
- Le Figaro, 16 Sept 1922 pp. 1–2 — Gallica [bpt6k293339r](""" + GAL + """bpt6k293339r)
- Tier **P** (OCR fragments of the newspaper pages via Gallica `ContentSearch`).
"""),

# ---------------------------------------------------------------- HANSARD
("Hansard After Atatürk, 1938–1939", "1938–1939", """
A negative proof and a small positive record, both from Hansard's own public search (the API behind
hansard.parliament.uk, `hansard-api.parliament.uk/search/contributions/Spoken.json`, queried 28 Oct 2026; every result
below is the full text of a recorded contribution).

**Negative: the Lloyd George line is not in Hansard.** The famous sentence attributed to David Lloyd George —
Mustafa Kemal as "the genius of centuries" or similar, repeated in Turkish columns and textbooks — returns
**0 hits** for the exact phrase *"genius of centuries"* in Spoken contributions for 1 Jan 1919–31 Dec 1939, and
0 hits with no date limit at all (Commons and Lords together). A control: the single word "genius" over 1922–23 returns 53
contributions, so the engine is live and honours phrase queries. A combined query ("Lloyd George" Kemal genius, 1919–39)
also returns 0; the only contributions matching "Mustapha Kemal" between August and December 1922 are
two (4 Aug, *Near East*, and 14 Dec, a debate on American debt), which I did not read and which are not the quote. This
confirms what the ledger row for [[David Lloyd George]] already carried from secondary sources: the line has no
parliamentary source (Parliament was in recess through the Chanak weeks, and the Commons hits for 1922 are 4 Aug and 14 Dec). It cannot, of course, exclude a speech
or an interview elsewhere; it removes only the parliamentary home people give it.

**Negative: no tribute in either House.** Spoken searches over 10 Nov–31 Dec 1938 for *Kemal*, *Ataturk*,
*Kamal Ataturk* and *"Turkish President"* return **0 hits**; Written answers for Nov 1938–Jan 1939 for *Kemal* and
*Ataturk*, 0. Nor does "Turkey" in the sittings of 10–25 Nov turn up any tribute (the five hits are a clearing-arrangements
answer, a Russia trade question, a minorities debate and two speeches in the Palestine debate on 24 Nov that
mention the Turkish army in 1917–18). The Commons that week was sitting; on the Hansard record, neither House
stopped to mark the death of the man whose government Britain had just backed with an armaments credit (the
Anglo-Turkish Bill of July 1938, debated below). Mourning came elsewhere — see [[Death and State Funeral of Atatürk]].

**Positive: eight MPs and peers who did mention him (Jul 1938–Oct 1939).**
- **Lord Strabolgi, 18 Jul 1938** (Lords, Anglo-Turkish Armaments Credit Bill): *"everyone who knows the Leader of
  the Turks, Ataturk, or as he was formerly known, Mustapha Kemal, admires his great qualities as a soldier, as well
  as a statesman, and the Leader and rejuvenator of his people."* The Turkish peasant, he says, is "the finest
  character that I have ever met."
- **Mr R. S. Hudson, 4 Jul 1938** (Commons, the same Bill): *"Ever since Ataturk got control he has been pursuing a policy
  of economic and industrial development in that country. It is very largely as a result of his personal drive that
  so much progress has been made."* Ataturk the developmental statesman, in a credit-guarantee debate.
- **Mr Adams, 28 Feb 1939** (Commons, *Spain* debate): *"Turkey under Kemal Ataturk was a brilliant and
  excellent example of how a totalitarian State can respect its international obligations."* Used as a counter-example:
  a good dictatorship exists, so Franco's fascism is a different matter.
- **Colonel Llewellin, 16 Mar 1939** (Navy Estimates): *"Turkey, under Ataturk, was almost a dictatorship, but it was not
  in any way allied to the Rome-Berlin axis."* Turned the other way, to argue a friendlier line towards the Franco regime.
  Two speakers, on opposite sides of the Spain argument, reach for the same Turkey.
- **Mr Vernon Bartlett, 2 Mar 1939** (Commons): *"there was once a dictator, Kemal Ataturk, who made a speech
  lasting four days"* — a joke about Hitler's length, and the only mention in the set that treats him as a legend of
  oratory.
- **Mr Foot and Mr Malcolm MacDonald, 3 May 1939** (Commons, *Cyprus (Press and Film Censorship)*): Foot asks
  why "the Cyprus authorities last year banned the film of the funeral of Kemal Ataturk and the film of a recent
  wedding in the Greek Royal Family, while films depicting Nazi and Fascist activities were allowed." MacDonald, for the
  Colonial Office: the censorship board is "composed partly of officials and partly of non-officials," and he is "unable to say
  what reasons may have guided them." So the colonial authorities in Cyprus kept the funeral off the island's cinema screens
  in November 1938 — the reason is not recorded in Hansard, and the Greek–Turkish politics of the island make it an
  obvious guess rather than a finding.
- **Lord Snell, 26 Oct 1939** (Lords, the week of the Anglo-Franco-Turkish treaty): getting a whole people to change its point of view in one
  generation "was done in Turkey as the result of the wise planning and sane outlook of perhaps the greatest of her modern sons.
  Kemal Atatiirk [sic, Hansard] has thus bequeathed to Europe a modernised Turkey."
- **Viscount Halifax, 26 Oct 1939** (Lords, same debate, as Foreign Secretary): *"The foundations for that friendship were, as the noble Lord
  said, laid by the master hand of Kemal Atatürk, and have been constantly developed under the distinguished guidance
  of his successor, President General Inönü."*

The pattern is the Rorschach one in miniature: the House said nothing at his death, but when it needed an exemplar —
for a credit bill, for the Spanish argument, for a treaty — it reached for him. See [[Winston Churchill]] and
[[Lord Curzon]] for the earlier British gazes, and [[Treaty of Lausanne]].

Caveat: Hansard's search covers its own indexed text; spellings (Atatiirk/Ataturk/Atatürk, Mustapha/Mustafa) were tried in several
forms; a mention under another transliteration or inside a table could escape. Debate section IDs: Strabolgi `3bc64e63-0d16-4836-b296-4a66f58bd544`,
Hudson `27ea970b-b2c7-4064-b39f-0f006860189d`, Adams `ca678499-3544-43c1-8331-81f0cfcb4e46`, Llewellin `f40b7ab7-e4d7-4b7f-b629-3178761d0294`,
Bartlett `08a9f896-7e5d-400f-b583-84ebee007954`, Cyprus `404d30b1-1af8-4697-90bf-a635daa96e47`, Snell/Halifax `c60e1b5e-c728-4feb-bb0f-314734960f6e`.

## Sources
- [Hansard search API, exact phrase "genius of centuries"](https://hansard-api.parliament.uk/search/contributions/Spoken.json?queryParameters.searchTerm=%22genius%20of%20centuries%22&queryParameters.startDate=1919-01-01&queryParameters.endDate=1939-12-31) — 0 results
- [Hansard, Anglo-Turkish (Armaments Credit) Agreement Bill, Lords 18 Jul 1938](https://hansard.parliament.uk/Lords/1938-07-18/debates/3bc64e63-0d16-4836-b296-4a66f58bd544/AngloTurkishArmamentsCreditAgreementBill) · [Commons 4 Jul 1938](https://hansard.parliament.uk/Commons/1938-07-04/debates/27ea970b-b2c7-4064-b39f-0f006860189d/AngloTurkishArmamentsCreditAgreementBill)
- [Hansard, Cyprus (Press and Film Censorship), 3 May 1939](https://hansard.parliament.uk/Commons/1939-05-03/debates/404d30b1-1af8-4697-90bf-a635daa96e47/CyprusPressAndFilmCensorship)
- [Hansard, The War: Reply to Herr von Ribbentrop, Lords 26 Oct 1939](https://hansard.parliament.uk/Lords/1939-10-26/debates/c60e1b5e-c728-4feb-bb0f-314734960f6e/TheWarReplyToHerrVonRibbentrop)
- Spain debate 28 Feb 1939, Navy Estimates 16 Mar 1939, Privy Seal Office 2 Mar 1939: Hansard section IDs above (hansard.parliament.uk/<house>/<date>/debates/<id>)
- Tier **P** (official parliamentary record, full text).
"""),
]

for n, when, b in E:
    note("Events", n, {"type": "event", "when": when, "tags": ["event", "verified", "obituary-corpus"]}, b)

print(f"census r5 europe_primary: {len(E)} cards")
