# -*- coding: utf-8 -*-
# Census round 4 (Oct 2026) — Europe: the Toksoy 2006 pair (Atatürk Yolu 37-38 + CTAD Güz 2006) finally read in full.
# Cards: Czechoslovakia (post-Munich), Baltic trio, Denmark+Norway, Finland+Sweden, Poland (deeper), Belgium.
# Delpher SRU (Dutch wires) used for contemporary context only (Czech presidency vacancy, Teschen mines).
from _lib import note

AY = ("[Toksoy, \"Avrupa Gazetelerinde Atatürk'ün Ölümüyle İlgili Olarak Çıkan Haber ve Yorumların Türk Basınına Yansıması,\" "
      "*Atatürk Yolu* 10/37–38 (May–Nov 2006), pp. 141–186](https://dergipark.org.tr/en/download/article-file/20592) "
      "([record](https://dergipark.org.tr/tr/pub/ankuayd/article/22558)) — full text banked in `sources/toksoy-2006-atatürk-yolu-european-press.txt`")
CT = ("[Toksoy, \"Atatürk'ün Cenaze Töreninde Yabancı Devlet Temsilcilerinin Verdikleri Beyanatlar ve Yorumlar,\" "
      "*Cumhuriyet Tarihi Araştırmaları Dergisi* (Güz 2006), pp. 143–171]"
      "(https://makale.isam.org.tr/server/api/core/bitstreams/155bd36a-8026-4b72-8db2-284fde81ae00/content) "
      "— full text in `sources/toksoy-2006-ctad-foreign-representatives.txt`")
CAVEAT = ("Paper titles in Toksoy are phonetic and sometimes garbled (she is working from Turkish newspaper "
          "digests, chiefly *Ayın Tarihi* Nov 1938, *Ulus*, *Cumhuriyet*, *Akşam*, *Kurun*, *Tan*); the identifications "
          "below are mine and marked \"presumably.\" The foreign originals were not seen.")

E = [

# ---------------------------------------------------------------- CZECHOSLOVAKIA
("Prague Reads Its Own Mirror, November 1938", "11–16 November 1938", """
The most pointed card in the corpus, because the mourners were looking at themselves. In
November 1938 Czechoslovakia was a state in the middle of being dismantled: the Munich settlement
was weeks old, President Edvard Beneš was gone, and a Dutch daily of 12 November reports Prague's
council of ministers under Prime Minister Syrový, with Slovak and Carpatho-Ukrainian ministers at
the table, preparing the election of Beneš's successor (Foreign Minister Chvalkovský, as sole
candidate) and talking of a single-party concentration. The same page reports Ankara's National Assembly
meeting to elect İsmet İnönü to succeed Atatürk. Two republics were choosing a successor to
a founder that week; only one of them was choosing from strength.

What the Czech papers wrote, per Toksoy's reading of the Turkish press digests (*Cumhuriyet* 14
and 16 Nov, *Ulus* 15 Nov, *Ayın Tarihi* Nov 1938):

- ***České slovo*** (presumably the Prague daily) saw him as "the man who gave the new Turkey its
  soul" and **openly said the Czechs envied the Turks such a leader — "because today we find
  ourselves in a position similar to Turkey's at the time Mustafa Kemal appeared on the world
  stage."** It added that he had made Turkey a state "on the British parliamentary model," built
  a strong industry, and presented "a picture of a miracle in the Muslim world."
- ***Lidové noviny*** ("Lidove Novini"): among the most precious figures of the post-war world; a
  constructive patriot and "the embodiment of iron will"; Turkey's rebirth "one of the greatest
  events of modern history."
- ***Lidové listy***: the greatest figure in Turkish history. ***Bohemia***: the man who left
  behind **"a national state that does not fear the future."** ***Prager Tagblatt*** (the
  German-language daily): under his leadership a wholly renewed Turkey would play an important role in world
  politics.
- "All the Czechoslovak press," Toksoy summarises, wrote that his qualities were beyond valuation
  and had won Turkey a first-rank international place.

Read it as a mirror, not a portrait. The line that matters is not the praise but the **comparison
of conditions**: a defeated, partitioned, humiliated state that had been rescued once by
a single will — the exact parable a country reeling from Munich might want to read in the
press without saying it about its own politics. "Bohemia" praising a founder who left "a national
state that does not fear the future" is, in November 1938, nearly an elegy for what Prague had
lost. (That reading is interpretation; the quotations are the evidence.) It also sits
oddly beside the cards of the two Czechoslovak neighbours that did the carving: for Hungary's
side see [[Hungary's Parliament Rises, November 1938]] and for Poland's,
[[Warsaw Compares Him to Washington, November 1938]]; a Dutch wire of 19 November has Czech miners
in Petrvald striking underground against the Polish seizure of the Teschen mines, the same day
the papers carried Atatürk's lying-in-state crush.

What this card is not: a Beneš node. Beneš, who as foreign minister had been in the Little
Entente–Balkan Pact orbit ([[Balkan Pact]]), has no sourced statement here; Beneš's own view
remains open.

Caveat: """ + CAVEAT + """ The *České slovo* sentence is the best-documented because Toksoy
prints it twice (in the section on Czechoslovakia and again in her conclusion).

## Sources
- """ + AY + """, §H pp. 172–173 + fn. 112–114, and conclusion pp. 184–185
- Dutch daily (Drents Archief), "Buitenlandsch Overzicht," 12 Nov 1938 — [KB resolver](https://resolver.kb.nl/resolve?urn=MMDA03:000115816:mpeg21:a0001:ocr) (Delpher SRU; Czech cabinet, Syrový, presidential succession; İnönü's election)
- Dutch wire, Venlo paper 22 Nov 1938 ("Latere Berichten"), [MMGAVL01:000025699:mpeg21:a0019](https://resolver.kb.nl/resolve?urn=MMGAVL01:000025699:mpeg21:a0019:ocr) (Prague 21 Nov, Chvalkovský's candidacy) · Dutch daily 19 Nov 1938, [MMRHCE01:000045873:mpeg21:a0053](https://resolver.kb.nl/resolve?urn=MMRHCE01:000045873:mpeg21:a0053:ocr) (Petrvald miners; Atatürk lying-in-state crush)
"""),

# ---------------------------------------------------------------- BALTIC
("Riga, Tallinn and Kaunas, November 1938", "11–16 November 1938", """
The three Baltic republics are the strongest strongman parallel in the census, and their November
1938 press is the place to see it. By then all three were authoritarian: Lithuania's Antanas
Smetona had held power since the December 1926 coup; Estonia's Konstantin Päts staged a
self-coup on 12 March 1934 (ruling thereafter in the so-called Era of Silence); Latvia's Kārlis
Ulmanis dissolved parliament and parties on the night of 15–16 May 1934. (Background from
Wikipedia's biographies; not part of the Toksoy corpus.) Their papers read a dead modernising
leader through that lens — and in the Latvian case the lens is almost explicit.

Per Toksoy's reading of the Turkish press (*Akşam* and *Kurun* 16 Nov, *Ulus* 15 Nov, *Cumhuriyet* 15–16
Nov, *Tan* 16 Nov, *Ayın Tarihi* Nov 1938):

**Latvia.** All the papers ran long pieces. The semi-official ***Brīvā Zeme*** ("Free Land," the
Ulmanis government's organ) gave over **whole pages** to him, under the headline **"The Man Who
Transcended the Centuries"**: **"Atatürk was the greatest of the statesmen of our time and the
most remarkable representative of the modern principle of leadership. With a revolution beyond
description he proved that a strong and sound personality could be created in the life of a
nation and state. He raised his state, which had been cut off from Europe, to the European level
and gave it a modern form of state. All of this happened in such a short time that it is more
accurate to call it a leap than an evolution."** *Jaunākās Ziņas* ran a biography with photograph
under "The Great Founder of Ankara," calling his work eternal and his legacy the surest foundation
of a "better and happier future," and saying he had given Turkish youth a life unimaginable
before independence; the army paper *Latvijas Kareivis* ran his picture with long articles.

**Estonia.** ***Uus Eesti*** wrote that he had achieved a "marvellous Renaissance" in Turkey and
pursued a bold foreign policy; ***Postimees*** that he had fulfilled a historic task, brought the Muslim world closer to
modern civilisation and raised the social level of women; ***Päevaleht*** ran, under the title
"Servant and Master of His People," extracts from [[Emil Ludwig]]'s biography.

**Lithuania.** The press had been carrying health bulletins from Istanbul and Ankara before the
death and printed longer articles after it, placing him first among contemporary statesmen. The semi-official
***Lietuvos Aidas*** (Smetona's government paper) wrote that he had "released new flames from the
heart of a nation animated by an active life" and built a state "incomparably newer and more perfect than the old," with
universities, village schools, an academy of fine arts, a conservatory and a youth organisation, women in an
important position, merchant shipping greatly strengthened, newspapers read by all classes —
"Turkey deserves the admiration of the whole world."

Note the shared grammar: the semi-official papers of regimes that had themselves suspended parliamentary politics praise **leadership
as a principle** (the Latvian phrase), **speed** ("a leap rather than an evolution"), and the state
as built from above. This is [[Kemalism]] read as an export model by neighbours who were
running the same experiment on a smaller scale, and it is a different register from the Nordic
liberal-democratic cards ([[Copenhagen and Oslo, November 1938]]). The hedge: these are
papers of the regimes, summarised by Turkish digests, and we do not know what
individual Baltic editors privately meant. What is solid is that the regimes' own organs chose these words.

Leads kept open: Atatürk's own letter of 12 March 1935 to Konstantin Päts appointing Ragıp Raif
envoy (Özden 2009, citing Şimşir); Päts's reported 1931 "kindred nation" letter (T-tier only so far); the
Lithuanian press, which Toksoy's footnote 68 in the 2010 article says wrote widely.

Caveat: """ + CAVEAT + """

## Sources
- """ + AY + """, §K pp. 177–178 and fn. 126–132
- Wikipedia, background only: [Antanas Smetona](https://en.wikipedia.org/wiki/Antanas_Smetona) · [Konstantin Päts](https://en.wikipedia.org/wiki/Konstantin_Päts) · [Kārlis Ulmanis](https://en.wikipedia.org/wiki/Kārlis_Ulmanis)
"""),

# ---------------------------------------------------------------- DENMARK + NORWAY
("Copenhagen and Oslo, November 1938", "11–16 November 1938", """
Denmark and Norway, the liberal-democratic end of the same corpus, and the card that supersedes
the one-line Danish listicle quote. Per Toksoy's reading of the Turkish press (*Akşam* 16
Nov p. 2 — headline "Danish Papers Speak of Atatürk and His Work with Admiration" — plus *Kurun*,
*Cumhuriyet*, *Tan* 16 Nov, *Ayın Tarihi*):

**Denmark.**
- ***Berlingske Tidende*** gave the longest portrait: "Atatürk died in the prime of his life, but
  his work will live in history as an epic of heroism. He made it as both a fighter and a statesman.
  **Quite unlike many of those who founded their power by the sword, he sheathed his sword after
  winning victory.** To understand his military work one must remember the Turkey that followed the
  World War: a state in ruins, a beaten army, a nation exhausted and in despair. Yet … he dictated
  national Turkey to the defeated at Lausanne in June 1923." He left "a Westernised modern state"; wearing the hat and learning the
  new alphabet were "not mere externals"; the new state was "the firmest support of the policy of peace";
  he settled Mosul and Hatay, built industry and railways. (See [[Treaty of Lausanne]], [[Hat Law]] and
  [[Alphabet Reform]].)
- ***Social-Demokraten*** : he did what no state expected, making a strong country of the "sick man."
  ***Børsen***: the man who tore up Sèvres and rebuilt his homeland in eighteen years (see [[Treaty of Sèvres]]).
- ***Kristeligt Dagblad*** (Toksoy's "Cristing Dagblat"): the man who worked wonders, spared nothing for his nation and
  crushed every plot — then a line worth keeping: **"The arm that wields the sword is worthy of holding
  the sceptre; his motto became the watchword of the grey wolf."**
- ***Nationaltidende*** : the supreme figure of personality and talent, creator of "the most
  tremendous event of the twentieth century"; he turned a half-Eastern nation, which recognised the caliph and religion as
  the sole power, into a modern, secular, national state — "radical change" meaning
  the discarding of symbols "rooted in the spirit of the East"; a foreign policy that "will remain a model in history":
  debts settled by friendly agreement, the Straits re-fortified, Hatay settled "without shedding
  blood." This is very probably the source of the listicle's "greatest miracle of the twentieth
  century" headline line (same paper, same "greatest event of the century" idea; the wording differs). (See [[Abolition of the Caliphate]].)

**Norway.** The papers gave the news wide space, printed his biography and praised his work.
***Dagbladet*** wrote that Turkey had now buried the label "sick man" entirely and that this was Atatürk's
achievement; ***Nationen*** (Toksoy's "La Nation Agraire," presumably the agrarian daily) put him first among
the heads of state who made a new country; ***Morgenbladet*** ("Le Morgen Bladet"): one of
his country's greatest men; a fourth paper, which Toksoy prints as "Morges Handels" (presumably
*Handels- og Sjøfartstidende*), called him the creator of the new Turkey who "drew it a secure road."

The distinctive thing: Scandinavian conservatives and liberals see the **sword sheathed**. The
Danish papers praise him precisely for not becoming what they feared (*Berlingske*'s contrast with
others who "founded power by the sword"), at a moment when the Baltic strongmen
([[Riga, Tallinn and Kaunas, November 1938]]) were praised for the opposite. And *Kristeligt Dagblad*'s
sceptre-and-sword line is the one place where the democratic press admits the
other half.

Caveat: """ + CAVEAT + """

## Sources
- """ + AY + """, §K pp. 178–180 and fn. 133–136
"""),

# ---------------------------------------------------------------- FINLAND + SWEDEN
("Helsinki and Stockholm, November 1938", "11 November – 7 December 1938", """
Toksoy's 2010 article quotes "the Swedish papers" (via *Ulus*, 14 Nov 1938): **"Had he not existed,
there would be no modern Turkey. But the Turks will raise their standing still further by
following his extraordinary work."** That line closely matches what his 2006 article prints for
the Finnish *Hufvudstadsbladet* (below); the "Swedish papers" attribution may be a different
digest of the same wire, or may mean Finland's Swedish-language press. Unresolved; the Finnish
originals would settle it. *(This card absorbed the round-3 "Stockholm and Warsaw" entry.)*

**Finland.** Papers gave him wide columns (*Kurun* 14 Nov p. 4, *Ulus* 15 Nov p. 5, *Cumhuriyet* 16 Nov p. 2):
- ***Svenska Pressen*** (the Swedish-language daily; Toksoy: "Svenska Pressen") leader: "Among all the
  leaders, Atatürk occupies a very important place in the size of the work of revolution he
  brought about in his country."
- ***Hufvudstadsbladet*** (Toksoy: "Hufvud Stadbladet"): **"Atatürk was an extraordinary statesman,
  one of the most important figures of post-war world history. Without Atatürk the new Turkey could
  not exist."**
- ***Helsingin Sanomat***: "among the great statesmen of our time … his military qualities and his
  tremendous record in his country's revolution are very great. **Without Atatürk, Turkey could not
  have been a great state.**" ***Uusi Suomi***: great revolutionary; Turkey without him could not be a great state.

And an official voice, from the second Toksoy article: **Onni Talas**, Finland's ambassador in
Ankara, who learned of the death in Budapest, said (as reported in *Ulus*, 7 December 1938,
under the headline "Atatürk Belonged Not to Turkey but to All Humanity"): "The death of
Atatürk, the great man of our century, grieved us as much as the Turkish nation. This great man
belonged not only to the Turkish nation but to all humanity. … On my travels in Turkey I saw
new Turkey blessed with great progress in every field. I observe an astonishing development
especially in the economy. What I saw gave me great hopes. I hope Finland and Turkey will be able to build very
good economic relations from now on." Toksoy's gloss: Finland's Atatürk is **the greatest reformer
in economics** — and the "gaze" is that of a small trading state asking what a modernising
economy can buy.

**Sweden.** Beyond the one-liner: *Aftonbladet* (via *Cumhuriyet*) called the rebuilding of
Turkey "an astonishing, complete revolution" and said the final victory of November 1922, when the
last sultan left his land (i.e. the end of the Sultanate; see [[Abolition of the Sultanate]]), had been hailed
with enthusiasm across the East, and that his subsequent decisions astonished the world by "the
speed of execution." *Göteborgs Handels- och Sjöfartstidning* ("Goeteborg Handels") praised the
state-builder who made a national Turkish state "out of the Ottoman remnants" and rationalised
agriculture systematically; *Svenska Dagbladet* said he had saved the homeland from partition
and that states now wished to deal with Turkey; *Nya Dagligt Allehanda* that in fourteen years his work had left deep marks
on world history; *Social-Demokraten* and *Dagens Nyheter* that under him Turkey became a modern state and he was, among
post-war heads of state, "the most remarkable," first saving Turkey and then creating a new state with a new
constitution, culture and ideal; and *Stockholms-Tidningen* that he was "not only the master of his country but
an excellent organiser" as statesman.

The stray: Toksoy files under Finland a piece by "Albert Saro" in "Parl Suvar" (*Ulus* 11 Nov p. 3)
praising his heroism and genius and calling him "a loyal and honest friend" whose loss is a loss for world
peace. Plausibly a Paris paper ("Parl Suvar" = presumably *Paris-soir*) and the French statesman Albert Sarraut, who led France's funeral delegation ([[Albert Sarraut]]), misfiled under Finland by the digest — an inference; not counted here.

Caveat: """ + CAVEAT + """

## Sources
- """ + AY + """, §H pp. 173–174 + fn. 115–117 (Finland); §J pp. 174–175 + fn. 118–121 (Sweden)
- """ + CT + """, p. 166 and fn. 96 (Talas)
- [Toksoy 2010, *Atatürk Üniversitesi SBE Dergisi*](https://dergipark.org.tr/en/download/article-file/32009), intro fn. 6 (*Ulus* 14 Nov 1938 p. 1) — the "Swedish papers" quote; full text in `sources/toksoy-2010-balkan-mideast-press.txt`
"""),

# ---------------------------------------------------------------- POLAND
("Warsaw Compares Him to Washington, November 1938", "11–21 November 1938", """
Poland, from Toksoy 2006's own Polish section (§E; *Cumhuriyet* 12 and
14 Nov, *Akşam* 13 and 15 Nov, *Tan* 12, 13 and 16 Nov, *Kurun* 14 Nov, *Ulus* 15 Nov, *Ayın Tarihi* Nov 1938):

- Polish papers gave the news wide space, issued **night editions** carrying the news on page one,
  and shared the Turks' grief. Their recurring figure: **he created the new Turkey as Washington
  created the United States** (the *Illustrowany Kuryer Codzienny*, presumably, wrote: "Atatürk saved Turkey
  by force of arms and created the new Turkey as Washington created the United States; his work
  has shown its effect even in great international affairs"). Many called him a **legendary
  man**.
- ***Polska Zbrojna*** (the army paper) dwelt on the adoption of the Latin alphabet and his service
  to civilisation. ***Kurier Poranny*** told in detail how he re-made a country;
  ***Kurier Warszawski*: "A long road has been travelled. A magnificent work has been created. All of
  this is the work of Atatürk"** — urging that the work be taken as a model in future. ***Goniec Warszawski***: his
  death is "an event of international character"; in fifteen years he made Turkey a modern
  state, reformed an army which became the strongest in the Balkans and Near East, and through his
  "dominant foreign policy" made Turkey a very important element in world politics.
- ***Polska***, the semi-official daily, stressed his patriotism and military genius and the victories
  that opened "a new page in the life of the nation" (*Akşam*, *Ulus*): **"Atatürk made the new Turkey with the
  sword and ordered it with his genius.** There is no field his creative spirit and ardent patriotism did not touch.
  He was the first to understand that the source of all old Turkey's disasters was the
  sultans' regime, which allowed foreign states to interfere in Ottoman internal affairs. He saved Turkey from the
  veil and from partition. … Today Turkey has many friends near her and across Europe." Then
  Lausanne: the treaty was accepted first by **Poland, "bound to Turkey by traditional friendships
  for a hundred and fifty years"** — and Turkey is now "a factor to be reckoned with in international
  politics"; the Ottoman "sick man" is cured and has regained his old energy, a miracle that is Atatürk's.
- Ambassador **Sokolnicki** (Toksoy: "Sokolniski"; presumably Michał Sokolnicki, Warsaw's envoy in
  Ankara — an inference) told *Express Poranny* that under Atatürk Turkey had resumed its role
  as the key in the Near East and **balanced Eastern Europe**, guaranteeing the independence of the peoples of
  that part of the world.

The political frame is [[Józef Piłsudski]]'s unfinished project of tying Poland to Turkey and the
Balkan states (note the Pact: [[Balkan Pact]]), which a recent Polish study finds was held back by the
two states' diverging relations with the USSR. Two details rise above the praise: "Washington" is the founder-statesman comparison of choice (and a
sword-then-constitution one); and the ambassador's "balances Eastern Europe" is the one sentence where a Pole openly states what Turkey is
for. A Dutch wire of 19 November, the same week, has Czech miners striking against Poland's seizure of the Teschen
mines ([[Prague Reads Its Own Mirror, November 1938]]) — the Poland that wrote these obituaries was also, that month, in a bitter mining dispute with
its southern neighbour, which is part of the mirror.

One mislabel to clear: Toksoy's Polish section also prints a *Barcelona "Vansuar"* paper
(*La Vanguardia*) calling him the victor of Sakarya and conqueror of İzmir and "the
military genius, statesman and philosopher" — that is the Spanish card; see
[[Two Spains Mourn, November 1938]].

Caveat: """ + CAVEAT + """

## Sources
- """ + AY + """, §E pp. 168–170 + fn. 92–101
- [Pressto/AMU, "Attempts at Poland's cooperation with the Kemalist Turkey in the Balkan Entente period"](https://pressto.amu.edu.pl/index.php/bp/article/view/52457) — abstract read only
- Dutch daily 19 Nov 1938, [MMRHCE01:000045873:mpeg21:a0053](https://resolver.kb.nl/resolve?urn=MMRHCE01:000045873:mpeg21:a0053:ocr) (Petrvald miners)
"""),

# ---------------------------------------------------------------- BELGIUM
("Brussels Stands, November 1938", "11–20 November 1938", """
Belgium's card, built from Toksoy 2006 twice and confirming the earlier *La Libre Belgique* listicle line against a scholarly source.

**The press** (as reported by *Akşam* 12 Nov p. 2 and *Ayın Tarihi* Nov 1938, pp. 182):
all papers ran biographies and photographs. ***Le Soir*** stressed the importance of Lausanne and his extraordinary
reforms, "so great that the world is still astonished before them." ***La Nation belge*** called him a great statesman who saved
his nation in every respect. ***L'Indépendance belge*** called him the most tenacious and unflinching revolutionary
of the age, the man who gave his nation a national consciousness, and ended by urging that his
great work be continued, which "is of great importance especially for Turkey and for Europe." ***Le
Peuple*** (the Socialist daily) described him as the first Turkish statesman to strengthen new Turkey's international position and **establish
close friendship with Soviet Russia**. ***La Libre Belgique***, after the biography, said his
work raised Turkey's status, prestige and authority and that **"no statesman has given his nation
such great service in so short a time"** — the sentence the listicle had attributed to it,
now with a scholarly home.

**The parliament.** On 16 November 1938 the Belgian parliament held a memorial for him (*Ulus* 17 Nov
p. 3): the speaker invited the deputies to **rise** and delivered an address on him.

**The funeral.** The Belgian government named a former ambassador to Ankara as King Leopold III's
extraordinary representative; the 2010 Toksoy article spells him "Roymond", the 2006 CTAD article "Deryınon" (the digest
spelling is unstable; likely a single man — name unresolved), with chargé d'affaires Rothe on the delegation (*Akşam* 18 Nov
p. 7). On arrival he told reporters, in the line that has become the card's epigraph (*Akşam*, 20 Nov p. 3, "The Sun at Çankaya"): **"I
have the good fortune to have known Atatürk personally. I have a deep respect for him. When I was in Ankara
I always looked at the sun. But I did not see the sun on the horizon; I saw it in Çankaya. For the true
sun was the sun called Atatürk in Çankaya. Atatürk's loss is a great loss not only for Turkey but for the whole
world."**

The party-political spread is the interesting thing: papers of different camps (by my own,
background-knowledge labels, *Le Soir* liberal, *La Libre Belgique* Catholic, *Le Peuple* Socialist) each find their own
Atatürk — the Soviet-friendship one, the national-awakening one, the prestige-builder. Compare the same exercise in [[Dutch Press, November 1938]], and the
foreign-delegation list in [[Foreign Delegations at the Funeral, November 1938]]. Belgium had no node in the census before this one.

Caveat: """ + CAVEAT + """

## Sources
- """ + AY + """, §G p. 172 + fn. 106–111
- """ + CT + """, p. 165 and fn. 94 (the "sun at Çankaya" statement)
"""),
]

for n, when, b in E:
    note("Events", n, {"type": "event", "when": when, "tags": ["event", "verified", "obituary-corpus"]}, b)

print(f"census r4 europe: {len(E)} country cards")
