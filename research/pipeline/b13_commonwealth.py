# -*- coding: utf-8 -*-
# Census round 5 — Commonwealth / Malaya primary newspaper evidence.
# Archives: NewspaperSG (browse agent; article pages sit behind a T&C wall), Papers Past (fetch OK),
# Trove (render OK on article pages; search UI needs a browser).
from _lib import note

E = [
("Malaya Muslims Mourn Atatürk, November 1938", "10–27 November 1938", """
**The 1938 Malayan card is a different thing from the 1924 one.**
[[Malay Press and the Fall of the Caliphate]] is scholarly and about the caliphate crisis. This one is newspaper evidence from
NewspaperSG (the National Library Board's digitised archive): what the Singapore and Malayan dailies
printed about local Muslims in the fortnight after the death. A keyword search for *ataturk*,
10–30 November 1938, returned 15 hits; the Muslim-reaction items are below, graded by how far the
text could be confirmed (the archive puts its article pages behind a terms-and-conditions wall, so
body text could only be read through a browse agent).

**Read (two browse retrievals agree).** *Morning Tribune*, 12 November 1938, p. 24: **"LOCAL MUSLIMS MOURN ATATURK'S DEATH."** A *Tribune* staff reporter
writes that Singapore Muslims, members of the All Malaya Muslim Missionary Society, received the news
of Atatürk's death "with profound sorrow"; Muslim shops and business establishments in Chulia Street,
Market Street and Arab Street were closed; the important mosques of the Colony held special prayers
after the Friday congregation; and — the sentence that matters — the report says that **whatever
Muslims elsewhere might think of his reforms, the fact that he was a Muslim leader alone called forth
spontaneous tribute.** (The last two details come from the page-level read only; ⚠️ the reading is a
browse agent's transcription, the OCR is poor, and the wording above is paraphrase, not quotation.)

That is the whole Malayan thesis in one line: the mourning is for the *Muslim leader*, with the
reforms held in brackets — the opposite pole from the Indian "Asian hero" register in
[[India Mourns, November 1938]], and a quiet reversal of 1924, when this same community's press
split over the abolition of the caliphate.

**Headline-level leads (⚠️ agent-reported, body text unconfirmed):**
- *The Straits Budget*, 17 Nov 1938, p. 7, **"NEGRI MUSLIMS AND ATATURK"** — the search-page snippet says
  nearly 300 Muslims met at the Negri Sembilan Indian Association premises in Seremban "as a mark of
  respect." The article page itself shows image clippings only.
- *The Straits Times*, 27 Nov 1938, p. 5, **"Klang Telegram To President Of Turkey"** — snippet: a public
  meeting of over 500 Indian Muslims, Hindus and others at the Town Mosque, Klang, passed a vote of
  condolence. A second agent run returned unrelated body text for this URL, so treat as unresolved.
- *Malaya Tribune*, 19 Nov 1938, p. 19 — **"ASSEMBLY ADJOURNED AS MARK OF RESPECT"** (see
  [[India in the Wires and the Malayan Press, November 1938]]).
- Wire layer around them: *Singapore Free Press* 11 Nov "Dictator Of Turkey Dies" (p. 1); *Morning
  Tribune* 11 Nov "Kemal Ataturk Dead"; *Malaya Tribune* 12 Nov "No Change Likely In Policy Of
  Turkey"; *Straits Budget* 17 Nov "New President Of Turkey Elected"; *Morning Tribune* 30 Nov "Big
  Monument For Kemal Ataturk" — Reuter copy, no editorial view.

**Dug, not found:** Malay/Jawi-language titles (*Warta Malaya*, *Utusan Melayu*) were not reached —
the search run was English-keyword only; a Jawi/Malay query (*Kamal Atatürk*, *Turki*) is the open
next step. No *Straits Times* leader on Atatürk surfaced in the 10–30 Nov hits.

Compare [[Dutch East Indies Press, November 1938]] — across the Strait, Muhammadiyah in Surabaya
observed a minute's silence for "this great Islamite": the same grammar of mourning.

## Sources
- NewspaperSG (National Library Board, Singapore), search *ataturk*, 10–30 Nov 1938; article ids `morningtribune19381112-1.2.107`, `straitsbudget19381117-1.2.15`, `straitstimes19381127-1.2.51`, `maltribune19381119-1.2.124`, `singfreepressb19381111-1.2.6`; base `https://eresources.nlb.gov.sg/newspapers/digitised/article/<id>`. Retrieved via browse agent 2026-10-28 (two runs for the Morning Tribune item); P-tier for the Morning Tribune item, hedged lead for the rest.
"""),

("India in the Wires and the Malayan Press, November 1938", "11–19 November 1938", """
**A primary-source floor under [[India Mourns, November 1938]].** That card rests on Toksoy's
secondary account (via Doğaner 2005): shops closed, legislatures suspended, national mourning. Here
are the contemporary newspaper lines themselves — wire copy, so a *witness* layer rather than a
considered view, but it shows what overseas readers were actually told about India within a day.

**Confirmed, direct fetch (Papers Past, NZ):**
- *Evening Post* (Wellington), 12 Nov 1938, p. 9, **"TRIBUTE TO ATATURK — BOMBAY MUSLIM BUSINESSES"**:
  "BOMBAY, November, 11. Muslim shops and warehouses closed as a tribute to Kamal Ataturk."
- *Press* (Christchurch), 14 Nov 1938, p. 9, in a United Press Association cable: "Moslem shops and
  warehouses in Bombay are closed as a tribute to Kemal." Same cable: the proposal to rename the
  capital Atatürk "is receiving wide support," and messages of appreciation from Hitler, the
  French President and the Soviet.

**Malayan copy of the same story (⚠️ agent-reported, body text unconfirmed — NewspaperSG's article
wall):** *Malaya Tribune*, 19 Nov 1938, p. 19, two United Press items — **"A.I.C.C. OFFICE CLOSED"**
(Allahabad, 11 Nov: the Congress office closed "as a mark of respect," the Congress flag at half
mast, and "both Hindus and Muslims" observed a complete hartal) and **"ASSEMBLY ADJOURNED AS MARK OF
RESPECT"** (New Delhi, 14 Nov: the Central Assembly's sitting adjourned by the President on the
request of Ghulam Bhik Nairang, "Acting Leader of" a party the snippet cuts off before naming). The first snippet is the more striking: **Congress itself, not just the League,
closing for a Turkish Muslim ruler.** A second agent run could not read either body and returned
conflicting text for the Assembly item (a "Johore" assembly) — so the Allahabad/Delhi detail is a
lead until someone reads the page in a browser.

What this adds to the card: (1) the Bombay shop closures are now confirmed in two newspapers, a
week-end wire reaching the Antipodes on 12 November; (2) the *Hindu-and-Muslim* hartal and Congress
flag, if the snippet holds, is a sharper claim than Toksoy's "India most affected after Turkey" — it
makes the grief cross-communal; (3) the Delhi adjournment matches the Punjab Assembly adjournment
already in [[Condolence Telegrams to Ankara, November 1938]]. See also [[Choudhry Rahmat Ali]]'s 11 Nov
telegram ("Asia its heroic apostle of nationalism").

## Sources
- Papers Past: [Evening Post 12 Nov 1938 p. 9](https://paperspast.natlib.govt.nz/newspapers/EP19381112.2.47.2) · [Press 14 Nov 1938 p. 9](https://paperspast.natlib.govt.nz/newspapers/CHP19381114.2.69)
- NewspaperSG: `maltribune19381119-1.2.124`, `maltribune19381119-1.2.126` (search-page snippets, browse agent; bodies not confirmed) — `https://eresources.nlb.gov.sg/newspapers/digitised/article/<id>`
"""),

("New Zealand Leaders on Kemal, November 1938", "11–12 November 1938", """
**Editorials, not wires.** [[New Zealand Press, November 1938]] mainly reads the cable and feature
layer. These are three unsigned leading articles from the same 48 hours, each with a stated
view — and Papers Past serves their full OCR.

**Dunedin *Evening Star*, 11 Nov 1938, p. 8 — "DEATH OF A DICTATOR."** The most conflicted. The paper
begins with the old Western contempt — the "sick man," "corruption, inefficiency, and intrigue," the
atrocities on "the Bulgarians, Armenians, and other minorities" — then pivots: "Perhaps among the
dictators of the present-day world his accomplishments are the greatest." He overcame "the fanatical
religious prejudices of the followers of the Prophet," and "by his public acts there is justification
for applying to him" the term "Saviour of Turkey" — though "his private life left much to be
desired." The editorial's best sentence is a diagnosis of restraint: "He declined to become the
champion of the East against the West, of Islam against Christianity, of subject races against their
masters." It closes uneasy about whether the edifice will "stand without his protecting and
dominating personality."

**Wellington *Evening Post*, 12 Nov 1938, p. 8 — "A GOOD DICTATOR."** The warmest, and the one that
settles the Anzac question: Kamal "will rank among his contemporaries as a good dictator." Its logic
is comparison with the living dictators: he "did not covet a neighbour's vineyard," did not seek "to
regain a lost empire"; he negotiated the population exchange with the Greeks "whom he had a year or
two before driven out of Turkey proper." It credits him militarily — "It was largely due to his
personal initiative, skill, and resource that the Anzacs were unable to reach the Narrows" —
quoting the British Official History on a single divisional commander's "profound" influence (compare [[C.E.W. Bean]] on the same campaign) — and ends with Antony over Caesar: "the good that he did lives
after him, the evil is interred in his bones." Verdict: "If there are any good dictators, Kamal was
one of the best." The Gallipoli victor, mourned by the Dominion that lost men to him.

**Greymouth *Evening Star*, 11 Nov 1938, p. 6 — "KEMAL AND TURKEY."** The shortest and the one that
names the relationship: Britain extends "condolences in the passing of a one-time gallant foe and a
later friend." "He was a Dictator, but he was of a more benevolent type than Hitler, Mussolini, or
Stalin." Closing line: "Were all Dictators like Kemal, there would be less need for concern about
their numbers." It also remembers 1922: relations were "strained during Mr. Lloyd George's
Premiership, war being narrowly averted at one stage partly through Overseas opposition" (see
[[New Zealand Leaders on Kemal at Chanak, September 1922]]).

Pattern: all three praise by *contrast with Hitler and Mussolini* — Atatürk as the proof of a good
dictator — which is the Antipodean version of the mirror in [[Death and State Funeral of Atatürk]]. And
all three stay inside the Empire's frame (Gallipoli, Chanak, Britain's friend); none discusses the
Muslim world beyond the Evening Star's "religious prejudices."

## Sources
- Papers Past (fetched, full OCR): [Evening Star 11 Nov 1938 p. 8](https://paperspast.natlib.govt.nz/newspapers/ESD19381111.2.63) · [Evening Post 12 Nov 1938 p. 8](https://paperspast.natlib.govt.nz/newspapers/EP19381112.2.31) · [Greymouth Evening Star 11 Nov 1938 p. 6](https://paperspast.natlib.govt.nz/newspapers/GEST19381111.2.27)
"""),

("Perth Western Mail on Turkey After Atatürk, 17 November 1938", "17 November 1938", """
**The first Australian leading article in the vault.** The Perth *Western Mail* of 17 November 1938
(p. 6, signed off "(Monday, November 14.)") ran "TURKEY AFTER ATATURK" — a foreign-affairs leader,
not a cable, read in full from Trove.

It opens on an anecdote: at an Ankara reception in 1930 Atatürk declared that "a thousand Turks"
could take his place, and the British ambassador replied, "Excellency, you exaggerate a
thousand times!" Now "Turkey mourns the death of its creator and dictator" and the question is
whether his "westernising reforms" — he is "this Turkish 'Peter the Great'" — will outlive him, and
whether Turkey will keep "the policy of friendship for all and servility to none." The paper's answer is
reassurance through İnönü: his choice "is the best guarantee Great Britain could have that Turkish
policy will continue." It is frank about the cost of the reforms — abolition of the Caliphate,
disestablishment of the Church, opposition in 1926–27 that was "ruthlessly suppressed" — and compares
Turkey's need for peace with the USSR's. It remembers 1922 only as Lloyd George having "backed the
wrong horse," and closes by sending "sincere good wishes" to İnönü, successor to "the first and not
the least successful of the post-war Dictators."

The gaze is instrumental and imperial: Atatürk as a *British interest* (Straits, Montreux, the
£10 million credit, German penetration of the south-east). Nothing about Gallipoli or Anzac — which
sets it apart from the New Zealand leaders in [[New Zealand Leaders on Kemal, November 1938]].

⚠️ **Other Trove items, listed not read:** *West Australian* 15 Nov p. 17 "Monument for Ataturk" (Reuter
wire, read by agent); *Courier-Mail* 10 Nov "Ataturk Seriously Ill"; *Albury Banner* 18 Nov "Ataturk's
Successor"; *Warwick Daily News* 1 Dec "Ataturk's Estate". And a **Workers Star** (Perth, labour
weekly) paragraph, 25 Nov 1938 p. 3, headed "KEMAL ATATURK," which a browse agent transcribed as a
Marxist defence of the Turkish "bourgeois revolution" against "certain illiterate reactionaries" who
had objected to democrats praising a dictator — *agent-reported only; the Trove page's text layer
did not load on re-fetch, so no quotation is made here.* If confirmed it would be the first
Communist-press gaze in the Commonwealth set (compare the Marxist mirror in
[[Death and State Funeral of Atatürk]]).

## Sources
- Trove: [Western Mail (Perth), 17 Nov 1938, p. 6](https://trove.nla.gov.au/newspaper/article/37857887) (rendered and read) · Workers Star 25 Nov 1938 [article 240637647](https://trove.nla.gov.au/newspaper/article/240637647) (agent-reported lead)
"""),

("New Zealand Leaders on Kemal at Chanak, September 1922", "18–20 September 1922", """
**What the Dominion's papers said of Kemal on the eve of Chanak.** The same Papers Past archive gives
the *1922* moment, when Lloyd George's call for Dominion troops (15 September) made the Smyrna victor
the enemy of the week. [[Canada Says Not Yet at Chanak, September 1922]] is the refusal; this is the
acceptance: New Zealand's Parliament backed the Imperial call "without a division" on 19 September, the
*New Zealand Herald* reporting "Dominion's Voice" on the 20th. Three editorials stand in for the press.

**Ashburton *Guardian*, 19 Sept 1922, p. 4 — "THE TURKISH LEADER."** A profile-leader, and the most
interesting for what it owes to Gallipoli: "The mainspring of the Turkish Nationalist movement, the
driving power behind it, is the mind and energy of that Turkish stormy petrel, Mustapha Kemal Pasha."
It remembers that he "snatched away complete victory from the British command" at Suvla, where "the
New Zealanders played a distinguished part" — "the greatest exploit in a tempestuous career" — and
then makes a diplomatic turn: "All through his career his eyes have turned to Britain," a predilection
that "may be utilised" to stabilise the East. Respect and calculation in one paragraph.

**Northern Advocate (Whangarei), 18 Sept 1922, p. 4 — "THE SHADOW OF WAR."** Mocks local rumour-mongers
who had predicted war, but is hostile to the Turks' stance: the Nationalists are "flushed with their
victory over the Greeks," "supported by Moslem opinion in India," possibly tied to "Russian Bolshevists"
and "German Communists." Kemal's army order about a "new task" is "full of significance." Policy: "The
firm policy that they have adopted is the only policy" — while hoping that "through the mercy of Divine
Providence it may prove to be a policy of peace."

**Otago Witness (Dunedin weekly), 19 Sept 1922, p. 40 — "THE WEEK" ("The Menace of Turkey").** Kemal
is "flushed by victory over the Greek armies" and "intent on regaining some, at least, of the
territory" lost — but the editorial blames the Allies: France and Britain "have been backing different
horses," the Kemalists could not have beaten Greece without France's tacit encouragement, and Allied "dilly-dallying" over
Constantinople "is largely responsible for the present situation." It calls for a conference "a thousand
times better than a resort to the futility of fighting."

Compare [[Chanak Crisis]] and [[Gallipoli Campaign]]. The 1922 gaze is the mirror image of 1938's: the
same papers that called him a menace in September 1922 would call him "the Saviour of Turkey" sixteen
years later (see [[New Zealand Leaders on Kemal, November 1938]]).

## Sources
- Papers Past (fetched, full OCR): [Ashburton Guardian 19 Sept 1922](https://paperspast.natlib.govt.nz/newspapers/AG19220919.2.16) · [Northern Advocate 18 Sept 1922](https://paperspast.natlib.govt.nz/newspapers/NA19220918.2.23.1) · [Otago Witness 19 Sept 1922](https://paperspast.natlib.govt.nz/newspapers/OW19220919.2.122) · [New Zealand Herald 20 Sept 1922 "Dominion's Voice"](https://paperspast.natlib.govt.nz/newspapers/NZH19220920.2.63)
"""),
]

for n, when, b in E:
    note("Events", n, {"type": "event", "when": when, "tags": ["event", "verified", "obituary-corpus"]}, b)

print(f"census r5 commonwealth: {len(E)} cards")
