# -*- coding: utf-8 -*-
# Round 6 — Hansard sweep 1919-1938 + Anglosphere (NZ) editorials.
# Primary routes: Hansard Search API (hansard-api.parliament.uk), Papers Past article pages.
# Record data (verified quotes) lives in scratchpad/b14/specs.py + nz.py; this script writes the notes.
from _lib import note

HOUSE = "https://hansard.parliament.uk"

E = [
("Parliament Meets Kemal, February–March 1920", "26 February – 25 March 1920", """
**The first time Westminster names him, he is a suspect.** In the spring of 1920 the Commons is arguing whether
to evict the Turks from Constantinople (Churchill, on 22 March, speaks of occupying the city "last week") and whether the Cilicia massacres —
Marash, Zeitun and others, January–February 1920 — were organised by the Nationalists. Hansard's own search
(the API behind hansard.parliament.uk, swept 29 Oct 2026 for *Mustapha/Mustafa Kemal*, *Kemal Pasha*, *Kemalist*,
*Angora Government*, *Ataturk* over 1919–1938) returns eight members and ministers who put a view of him in these five weeks:

- **26 Feb, "Turks and Constantinople."** *Lieut.-Colonel Guinness* blames "levies"
  under Kemal for the Marash/Zeitun massacres and predicts that evicting the Turks would hand over the government to the
  Nationalists: *"Mustafa Kemal would become dictator."* *Bonar Law* answers for the Government: "It is quite possible
  that someone like Mustapha Kemal may ignore altogether the instructions from Constantinople and massacres may take place."
- **11 Mar, "Cilicia Massacres."** *Sir H. Greenwood*, answering, says the massacres "are understood to
  have been carried out by irregular troops who are believed to be under the authority of Mustapha Kemal Pasha"; *Ormsby-Gore*
  presses: is Kemal not "the agent of the Committee of Union and Progress" that "organises these massacres"? (The Foreign Office
  line, as a questioner restated it on 15 March, was careful: the Minister had *not* accepted that Kemal was the Committee's agent.)
- **22 Mar, Army Estimates.** *Major-General Sir John Davidson*: "I do not believe that the troops under Mustapha Kemal in Anatolia care anything for our
  occupation of Constantinople," so no saving on the Army. *[[Winston Churchill]]*, as War Secretary, lists "the Turkish
  Nationalists under Mustapha Kemal" among the three anxieties for Mesopotamia and warns of a junction with the Bolsheviks and
  "the hostile forces of Mustapha Kemal."
- **25 Mar, Foreign Affairs.** *H. H. Asquith*: "so long as Mustapha Kemal and his forces are at large, and the Armenians are
  left with an inadequate provision for self-protection, the recurrence of massacre and outrage is only a question of time."
  *Colonel Yate* speaks for loyal Indian Muslims against agitators "in league with Enver Pasha, Mustapha Kemal, and other Young
  Turk leaders who have brought so much ruin on Turkey."

**Reading it.** Seven of the eight are hostile; the eighth (Davidson) is a general sizing up an army. The frame is the Young
Turk Committee and the memory of 1915 (see [[Armenian Genocide]]): Kemal enters British politics cast as Enver's successor and held answerable for the Cilicia
massacres; how far the Nationalist command directed them is a question this record does not settle. Nobody yet calls him a
statesman. (Earlier, 17 Dec 1919, Viscount Bryce in the Lords names him as "in command of a large Turkish force" west of
the Taurus; that is a location, not yet a view.)

Next: [[Parliament on Kemal and the Greeks, 1921–1922]]. See also [[Treaty of Sèvres]].

## Sources
- Hansard (Commons) 26 Feb 1920, "Turks And Constantinople": [page]({H}/Commons/1920-02-26/debates/7dd9498b-3e40-4d22-a1d1-b06729365496/TurksAndConstantinople) — Guinness, ContributionExtId `2533087e-f48b-428e-850d-6bed2453da23`; Bonar Law `a79029b5-046a-446e-bf61-fe2ce02675d3`
- Hansard 11 Mar 1920, "Cilicia Massacres": [page]({H}/Commons/1920-03-11/debates/9ee65e95-7cee-44ac-bedf-15196dd1bb46/CiliciaMassacres) — Greenwood `a6e44ab2-e666-4e43-bb23-6c34f36244db`; Ormsby-Gore `0d42ffd1-6c78-4366-aa60-e1338a33fdc3`; restatement 15 Mar: [page]({H}/Commons/1920-03-15/debates/82eef348-fc35-4ca9-901a-fd305f31c168/MassacresInCilicia)
- Hansard 22 Mar 1920, "Army Estimates, 1920–21" (Davidson `9dbcc6f5-9fdf-4143-845e-dc03abbf1537`): [page]({H}/Commons/1920-03-22/debates/437047e3-3de4-46af-8eff-66422ef77c86/ArmyEstimates192021); "Number Of Land Forces" (Churchill `b08af620-6e0f-4925-917f-32dfa46347b9`): [page]({H}/Commons/1920-03-22/debates/8529f900-db16-4d18-924b-a2cb5745973b/NumberOfLandForces)
- Hansard 25 Mar 1920, "Foreign Affairs" (Asquith `f3a4e338-481d-436b-93df-fa2ee4790dd9`; Yate `b774b49b-ed48-450c-aa91-e4d6eb29ebc7`): [page]({H}/Commons/1920-03-25/debates/2e5028ef-3013-4fec-927b-043d7f107190/ForeignAffairs)
- Tier P (the parliamentary record, full contribution text read via the Hansard Search API). Page slugs follow the canonical form; the site returns 403 to non-browser clients, so the page URLs themselves were not loaded.
"""),

("Parliament on Kemal and the Greeks, 1921–1922", "June 1921 – December 1922", """
**From "rebel" to "great patriot" in two years — and to the man who beat the Coalition.** Between Bryce's "rebel
government under Mustapha Kemal at Angora" (Lords, 23 Jun 1921) and Kenworthy's jibe about "the great victories of Mustapha
Kemal and his army" (Commons, 14 Dec 1922), the Hansard record shows Westminster splitting over the Greco-Turkish war:

- **Hostile — the Armenian and Greek lobby.** *Viscount Bryce* (Lords, "British Mandates," 23 Jun 1921) makes any peace with
  Constantinople or "the rebel government" at Angora conditional on safety for the Christian communities. *Lord Robert Cecil*
  (19 Dec 1921) says the French had "made an arrangement with Mustapha Kemal which involves the complete abandonment of the Christian
  population" in Cilicia. *T. P. O'Connor* (27 Mar 1922) sneers at "M. Bouillon's enlightened statesmen" ([[Franklin Bouillon]]),
  citing an escaped Malta internee who "joined Moustapha Kemal at Angora as a general in his army," and on 26 Jun asks what the
  Government will do about Kemal's Ismid speech, which he says justified atrocities against the Greeks.
- **Lloyd George, twice.** On 22 Dec 1920 he had called Kemal "a mutinous general" and refused to buy "the good will of this
  general" with Smyrna — a passage T. P. O'Connor read back into the House on 8 Feb 1922 to show how far the Coalition had turned.
  On 4 Aug 1922, the month before Smyrna: *"Mustapha Kemal may be a great general and a great patriot; but the head of Islam is in
  Constantinople."* See [[David Lloyd George]].
- **Admiring — the soldier's view.** *Sir Charles Townshend* (30 May 1922), who surrendered at Kut ([[Charles Townshend]]): the
  Allied occupation of Constantinople "at once lit up the Turkish Nationalist party, and created this patriot Kemal, whom the Prime Minister described as a revolting general.
  There have been other revolting generals in history. Washington was one"; he would have gone to Ismid to "say to him, 'For
  heaven's sake, Kemal, moderate your demands'," and ends "I know him well and respect him." This is a Commons speech in his own
  words (the existing person note carries no source).
- **Instrumental — the anti-Coalition left.** *Lieut.-Commander Kenworthy* (14 Dec 1922): "Turkey could have wept bitter tears in vain
  for admission to the League of Nations but for the great victories of Mustapha Kemal and his army" — Kemal as proof that
  Curzon's and Lloyd George's "success of force" had failed.

**A gap worth knowing.** Parliament was in recess through the Chanak weeks, so the Hansard record has no debate for 11 Sept –
mid-Nov 1922. Between 5 Aug and 13 Dec 1922 the sweep finds no contribution in either House containing the words *Kemal*, *Kemalist* or
*Ataturk*; the Lords address debate of 23 Nov and the Commons foreign affairs debate of 24 Nov surface only under *Angora* (see
[[Chanak Crisis]]). The Chanak summer is therefore recoverable from the press, not from Hansard — see
[[New Zealand Editors on Kemal, September 1922 – 1923]] and [[New Zealand Leaders on Kemal at Chanak, September 1922]].

Previous: [[Parliament Meets Kemal, February–March 1920]]. Next: [[Westminster on the Turkish Dictator, 1924–1938]].

## Sources
- Hansard (Lords) 23 Jun 1921, "British Mandates" (Bryce `82f85357-9b42-4ca4-af1c-02178114ae40`): [page]({H}/Lords/1921-06-23/debates/904de8c1-8c17-48ee-a9e0-6a2f42d95ec2/BritishMandates)
- Hansard 19 Dec 1921, "Christian Population In Asia Minor" (Lord Robert Cecil): [page]({H}/Commons/1921-12-19/debates/0f108a5d-d7c6-450b-89bd-962e008fa23c/ChristianPopulationInAsiaMinor)
- Hansard 8 Feb 1922, "Debate On The Address" (O'Connor reading Lloyd George, Vol. 136 cols 1895–97, 22 Dec 1920): [page]({H}/Commons/1922-02-08/debates/f4ae054c-5321-4dff-b06e-4a49dab44b27/DebateOnTheAddress)
- Hansard 27 Mar 1922, "Foreign Affairs" (O'Connor): [page]({H}/Commons/1922-03-27/debates/c899fde6-a1fd-475b-9f9a-a2756dd19631/ForeignAffairs); 26 Jun 1922, "Greece And Turkey": [page]({H}/Commons/1922-06-26/debates/05b935e7-5dd8-4c3a-8d26-ce88e0377d87/GreeceAndTurkey)
- Hansard 30 May 1922, "Near East" (Townshend): [page]({H}/Commons/1922-05-30/debates/1aafc6d6-0a0f-432e-9b1e-9466569af14e/NearEast); 4 Aug 1922, "Near East" (Prime Minister): [page]({H}/Commons/1922-08-04/debates/e8c2fe25-f736-4f36-bd19-4375874f4b5b/NearEast)
- Hansard 14 Dec 1922 (Kenworthy; API section title "Deut To United) States"): [page]({H}/Commons/1922-12-14/debates/0dc5131b-b329-4572-b933-97cfc8608532/DeutToUnitedStates)
- Tier P (full contribution text via the Hansard Search API, swept 29 Oct 2026). Note the API also lists sittings dated July 1932 for Cecil Harmsworth's Under-Secretary answers on "Angora Government (Negotiations)"; Harmsworth left office in 1922, so those items are 1922 sittings mis-dated by the API and were not used.
"""),

("Westminster on the Turkish Dictator, 1924–1938", "May 1924 – June 1938", """
**The long middle: Kemal as a lesson.** After Lausanne the Hansard record goes quiet on Kemal as an enemy and uses him as
an example. Nine members and peers, all from the Hansard Search API sweep:

- **Curzon (Lords, 14 May 1924).** The man who made Lausanne, on Reza Khan's modelling himself on Kemal: "I can foresee that if
  he follows certain lines of policy which have been pursued by Mustapha Kemal in Turkey, he may come to grief at an early stage in
  his own country." ([[Lord Curzon]]; the API prints his name as "Marquess Quezon of Kedleston," a typo.)
- **Mr Pilcher (Commons, 18 Feb 1926, Anglo-Iraq Treaty).** Hostile, with the Mosul dispute as backdrop: "The Indian Moslem
  has discovered exactly the true nature of the Kemal Pasha régime in Angora," persecuting fez-wearers and Moslem prayer, "rulers
  who are definitely librepenseurs and anti-Moslem."
- **Colonel Wedgwood (11 Mar 1929)** — the mirror image: "it is desirable that Mustapha Kemal should introduce [Western ideas] into
  Turkey" and Palestine needs the same.
- **Rear-Admiral Sueter (10 Mar 1932):** Turkey's advice to Geneva "was the best. His Excellency, Kemal Pasha, said that a nation
  should have the army that it needs" — pressed into service for a bigger RAF.
- **Lord Newton (Lords, 20 Apr 1932):** "There is a much greater despot reigning in another country at the present moment, and that is
  Mustapha Kemal, but Mustapha Kemal had the sense not only to start a sham Parliament but to start an Opposition" — and so, he says,
  British Socialists never attack him.
- **Sir H. Croft (29 Mar 1933)** on Indian reform: democratic institutions in Turkey? "Mustapha Kemal put an end to them
  at the end of two years."
- **George Lansbury (11 Jul 1933):** the Turks "took back Constantinople by force... Kemal Pasha was practically able to dictate
  his own terms" — his proof that treaty-signers do not mean what they sign.
- **Hamilton Kerr (29 Jul 1937)** retells Chanak: "Mustafa Kemal had then just arisen as the new dictator of Turkey."
- **Mr de Rothschild (14 Jun 1938)** on Cyprus land law: "It is the same law as ran throughout the East under the Turks...
  before Ataturk revised the laws of Turkey."

A pattern: the only admirers are Wedgwood and de Rothschild; the rest use Kemal for someone else's argument — against
Indian democracy, for arms, for a pacifist moral, against the Socialists — and three of them reach for the word *dictator* or
*despot*. Compare the near-silence after his death in [[Hansard After Atatürk, 1938–1939]] (July 1938 praise by Hudson and
Strabolgi is recorded there).

Previous: [[Parliament on Kemal and the Greeks, 1921–1922]].

## Sources
- Hansard Lords 14 May 1924, "Persia": [page]({H}/Lords/1924-05-14/debates/e7ad5ce0-cd8d-45ca-b56c-4c17c92785f0/Persia) · Commons 18 Feb 1926, "Anglo-Iraq Treaty": [page]({H}/Commons/1926-02-18/debates/0295f9ae-d72c-4f6c-a64a-9d801a389759/AngloIraqTreaty) · 11 Mar 1929, "Women (Disabilities)": [page]({H}/Commons/1929-03-11/debates/18f5c257-7ce0-4c52-b4dd-a1209d88efa3/WomenDisabilities)
- Hansard 10 Mar 1932, "Sir Philip Sassoon's Statement": [page]({H}/Commons/1932-03-10/debates/d37902ec-807a-4e95-a8a4-a48f235e1408/SirPhilipSassoonSStatement) · Lords 20 Apr 1932, "Trade Policy With Russia": [page]({H}/Lords/1932-04-20/debates/ed42df23-676b-41a3-923b-1bf56f6c937a/TradePolicyWithRussia)
- Hansard 29 Mar 1933, "Indian Constitutional Reform": [page]({H}/Commons/1933-03-29/debates/9d643c7d-3a22-4bf0-bdcf-a46ccfe5de4c/IndianConstitutionalReform) · 11 Jul 1933, "Disarmament": [page]({H}/Commons/1933-07-11/debates/abc8d665-f23b-4d6b-8b35-7dccd7ad3e9e/Disarmament) · 29 Jul 1937, "Dominion Affairs": [page]({H}/Commons/1937-07-29/debates/2bc0ea28-89bc-480a-bf0b-e06b1fcb6e08/DominionAffairs) · 14 Jun 1938, "Colonial Office": [page]({H}/Commons/1938-06-14/debates/b7f7c4cd-a57e-42f0-a01e-c128545a6bd1/ColonialOffice)
- Tier P (full contribution text via the Hansard Search API, swept 29 Oct 2026); first names/party for Pilcher and de Rothschild not given in the text, so only "MP" is asserted.
"""),

("New Zealand Editors on Kemal, September 1922 – 1923", "15 September 1922 – 8 October 1923", """
**The Dominion that refused to be asked.** The existing card [[New Zealand Leaders on Kemal at Chanak, September 1922]] has
the opening leaders (18–20 Sept). This card follows the Papers Past leader columns through the crisis, sampled from 100
results for *Kemal* between 15 Sept and 31 Oct 1922 plus 1923, and keeps only editorial opinion; the cabled news and
syndicated biographies ("Who Is Kemal?", "Kemal of the Iron Hand," Clair Price's portrait — see [[Clair Price]]) are not gazes.

**Chanak (September–October 1922).**
- *Dominion* ("Without Prejudice," 15 Sept) jokes that "Kemal Pasha is an unusually tough nut to crack" for Greece, especially with nobody having the price of a
  pair of nutcrackers (a humorous column, partly quoting Clair Price).
- *Southland Times* (22 Sept): "Kemal's undertakings amount to very little" — he denies any neutral zone exists, so expect a
  collision. (30 Sept) Kemal "is extremely dense if he does not read in the revolution a revival of Greek patriotism"; he treats the
  zone "with delightful insouciance," though demanding Smyrna as the conference site is "a cute diplomatic move."
- *Pahiatua Herald* (23 Sept) explains the Angora Government as the Allies' third mistake and says Kemal, "his Government, and his
  followers, defeated the Greeks, and re-united" the Turks (the OCR blurs the words, so no verbatim quote is taken); (30 Sept): "The
  Turkish leader is showing much obstinancy in endeavouring to impose conditions antecedent to the meeting for a final settlement."
- *Gisborne Times* (28 Sept, "Kemal Pasha's 'Bluff'"): "Kemal Pasha is more than a military leader" — a "born political
  strategist" — yet his advance is "pinpricking tactics," not a war aim.
- *Manawatu Standard* (3 Oct) welcomes his conference acceptance but names the cause: over 13,000 New Zealand volunteers
  came forward "to resist the attempt made by Kemal Pasha to subvert the victory of the Allies in the late war."
- *Northern Advocate* (4 Oct, "The Turkish Side"): "Kemal is a strong man" who may see the wisdom of peace, but his Assembly is
  "dominated by men who are little better than military adventurers."
- *The Observer* of London, cabled and printed in the Wellington *Evening Post* (9 Oct, "Muddled Policy"): "The moribund Coalition is
  dead at last, killed by Kemal, as surely as the sparrow killed cock robin." Kemal as the man who ended Lloyd George (compare
  [[Parliament on Kemal and the Greeks, 1921–1922]]).

**After Lausanne.** *Nelson Evening Mail* (6 Mar 1923, "The Dictators of Europe") puts "Mustapha Kemal, having reduced the Caliph to a
cypher," beside Mussolini, Lenin and Trotsky: the army "may at any moment control the political situation." *Auckland Star* (8 Oct
1923, as the Allies leave Constantinople): a "vaguely optimistic faith in the regeneration of the Turk" is baseless; Kemal "is little
more than a military dictator" who may cut Turkey off from the West.

Net: 11 records — six hostile, three conflicted, one witness, one instrumental (the London *Observer*) — and no editor in this window
admires him. The warmth arrives after 1928 ([[New Zealand Editors on the Dictator, 1929–1938]]). Compare the near-unanimous warmth of the
November 1938 cards, e.g. [[New Zealand Press, November 1938]].

## Sources
- Papers Past (fetched article pages, OCR text; tier P): [Dominion 15 Sep 1922](https://paperspast.natlib.govt.nz/newspapers/DOM19220915.2.41) · [Southland Times 22 Sep 1922](https://paperspast.natlib.govt.nz/newspapers/ST19220922.2.17) · [Pahiatua Herald 23 Sep 1922](https://paperspast.natlib.govt.nz/newspapers/PAHH19220923.2.10) · [Gisborne Times 28 Sep 1922](https://paperspast.natlib.govt.nz/newspapers/GIST19220928.2.16) · [Southland Times 30 Sep 1922](https://paperspast.natlib.govt.nz/newspapers/ST19220930.2.18) · [Pahiatua Herald 30 Sep 1922](https://paperspast.natlib.govt.nz/newspapers/PAHH19220930.2.11) · [Manawatu Standard 3 Oct 1922](https://paperspast.natlib.govt.nz/newspapers/MS19221003.2.11) · [Northern Advocate 4 Oct 1922](https://paperspast.natlib.govt.nz/newspapers/NA19221004.2.21.2) · [Evening Post 9 Oct 1922](https://paperspast.natlib.govt.nz/newspapers/EP19221009.2.91) · [Nelson Evening Mail 6 Mar 1923](https://paperspast.natlib.govt.nz/newspapers/NEM19230306.2.24) · [Auckland Star 8 Oct 1923](https://paperspast.natlib.govt.nz/newspapers/AS19231008.2.28.1)
- Search: Papers Past rendered results for `Kemal leader`, 15 Sep – 31 Oct 1922, and `Kemal dictator`, 1923.
"""),

("New Zealand Editors on the Dictator, 1929–1938", "6 March 1929 – 9 August 1938", """
**The same editors, six years on.** A second Papers Past pass (searches *Kemal dictator* 1923, *Ataturk* 1934–38, *Kemal Turkey dictatorship* 1929–38)
finds the leader columns turning, with one paper (the Waikato Times) on record at both ends. Wire stories on his illness and his
June 1937 gift of his fortune ("Father of Turkey") are news, not opinion, and are left out.

- *Waikato Times* (8 Jan 1929, "The New Turkey"): Kemal's westernisation was "done ruthlessly and efficiently," "no opposition of any
  kind was tolerated" and "the terror was as inhuman as any in modern times," with eminent politicians "publicly hanged because they
  dared to disagree with Kemal."
- *Auckland Star* (6 Mar 1929, "When Dictators Succeed," on Amanullah's fall): "As a virtuoso of revolution and dictatorship Kemal towers head
  and shoulders above all other personal and partv autocracies since the World War" (OCR typo kept) — Lenin and Mussolini's
  reforms are "mere surface scratchings by comparison."
- *Feilding Star* (1 Nov 1933, "New Turkey's Decade"): the republic's tenth birthday is also the dictatorship's; "one man is
  responsible," an Italian-style redemption.
- *Waikato Times* (29 Oct 1934, "A Turkish Anniversary"): "the guiding hand of her first and only dictator"; "What has been broken up by
  Kemal Pasha is the Oriental middle ages." The same paper that spoke of terror in 1929 now writes that he has done it "tenderly."
- *Northern Advocate* (9 Aug 1938, "When Dictators Fall," after his first collapse): "Kemal ruled, and has continued to rule,
  with an iron hand," yet Turkey "has advanced economically, socially and intellectually"; the danger is the old factions when he goes.

**Trove (Australia).** Two browse runs on Trove search for September–October 1922 leaders found two candidate articles (Kalgoorlie
Miner 14 Oct 1922 and Sun News-Pictorial 16 Sep 1922, both titled "Mustapha Kemal Pasha"), but Trove's article pages and text
renditions sit behind an Anubis proof-of-work wall for non-browser clients, so neither could be read. Nothing from Trove is quoted here.

Previous: [[New Zealand Editors on Kemal, September 1922 – 1923]].

## Sources
- Papers Past (fetched article pages; tier P): [Waikato Times 8 Jan 1929](https://paperspast.natlib.govt.nz/newspapers/WT19290108.2.22) · [Auckland Star 6 Mar 1929](https://paperspast.natlib.govt.nz/newspapers/AS19290306.2.26) · [Feilding Star 1 Nov 1933](https://paperspast.natlib.govt.nz/newspapers/FS19331101.2.11) · [Waikato Times 29 Oct 1934](https://paperspast.natlib.govt.nz/newspapers/WT19341029.2.27) · [Northern Advocate 9 Aug 1938](https://paperspast.natlib.govt.nz/newspapers/NA19380809.2.17)
"""),
]

for name, when, body in E:
    body = body.replace("{H}", HOUSE)
    note("Events", name, {"type": "event", "when": when, "tags": ["event", "verified", "obituary-corpus"]}, body)
print(len(E), "notes written")
