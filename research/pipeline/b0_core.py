# -*- coding: utf-8 -*-
from _lib import note, person, links

# ---------------- HUB ----------------
note("", "Mustafa Kemal Atatürk", {
    "type": "person",
    "role": "Founder and first President of the Republic of Turkey",
    "nationality": "Ottoman / Turkish",
    "lifespan": "1881–1938",
    "tags": ["person", "hub", "moc"],
}, """
The gravitational centre of this vault. Ottoman officer at [[Gallipoli Campaign]], commander of the
[[Turkish War of Independence]], first President of the Republic, and author of a cultural revolution
that rewrote a nation's alphabet, law, dress, calendar and historical self-image inside fifteen years.

He was the first leader to tear up a post-WWI treaty imposed by the victorious Allies and make it
stick ([[Treaty of Lausanne]]). That single fact is why the admirer list in this vault is so
ideologically incoherent: fascists, communists, anti-colonial nationalists, Zionists, feminists,
popes and pan-Africanists all looked at Ankara and saw their own project reflected back. He worked as
a kind of global Rorschach test.

## Maps of Content
- [[MOC — Admirers]]
- [[MOC — Antagonists and Victims]]
- [[MOC — Inner Circle and Turkish Figures]]
- [[MOC — Foreign Observers and Diplomats]]
- [[MOC — Exiles Turkey Sheltered]]
- [[MOC — Events]]
- [[MOC — Concepts]]
- [[Source — Reddit thread and transcript]]

## Core threads
- [[Kemalism]] · [[Abolition of the Caliphate]] · [[Alphabet Reform]] · [[Devletçilik]]
- [[Nazi Racial Hierarchy]] — the conversation this whole thread grew out of
- [[10 Kasım]] · [[Death and State Funeral of Atatürk]] · [[Nutuk]] · [[Historiography of
  Atatürk]] — the verified 10 Kasım layer (sources attached, tag `verified`)
""")

note("", "Source — Reddit thread and transcript", {
    "type": "meta", "tags": ["meta", "source"],
}, """
Everything here is extracted from `raw.txt`, a chat transcript that begins with a Reddit exchange on
the internal structure of Nazi racial ideology ([[Nazi Racial Hierarchy]], [[Nazi Outreach to the
Muslim World]]) and then pivots — at the question *"what was Hitler's take on post-Ottoman Turkish
peoples and the likes of Atatürk?"* — into a long, ever-expanding catalogue of historical figures
orbiting [[Mustafa Kemal Atatürk]].

**Caveat carried over from the source:** the transcript is a chat-assistant answer, not a vetted
history. Several claims in it are contested, apocryphal, or repeated verbatim in later sections of
the same transcript (Lloyd George, Gandhi, Mao, Sherrill, Trotsky, Reza Shah, Dewey, Roncalli,
Venizelos all appear twice). Notes flagged `verify: contested` mark the ones most worth checking
against a real source before you repeat them.

Named literature in the transcript: Stefan Ihrig *Atatürk in the Nazi Imagination*; David Motadel
*Islam and Nazi Germany's War*; Jeffrey Herf *Nazi Propaganda for the Arab World*; Robert Wistrich
*A Lethal Obsession*; Francis Nicosia *Nazi Germany and the Arab World*; Norman Stillman *The Jews of
Arab Lands in Modern Times*; Zvi Yehuda *The New Babylonian Diaspora*; Lord Kinross *Atatürk: The
Rebirth of a Nation*.
""")

# ---------------- EVENTS ----------------
E = [
("Gallipoli Campaign", "1915", """
Allied attempt to force the Dardanelles. A then-obscure lieutenant colonel, [[Mustafa Kemal Atatürk]],
correctly predicted the Anzac Cove and Suvla Bay landings, went over the head of the German command,
and issued the order that made his legend: *"I am not ordering you to attack, I am ordering you to die."*

Its afterlife is remarkable: three of the commanders who lost there — [[Winston Churchill]],
[[William Birdwood]], [[Otto Liman von Sanders]] — all ended up publicly honouring him.
"""),
("Turkish War of Independence", "1919–1923", """
Launched when [[Mehmed VI Vahideddin]] dispatched Mustafa Kemal to Anatolia to *suppress* nationalist
resistance and he did the exact opposite. Sustained by [[Kâzım Karabekir]]'s intact eastern army,
Soviet gold funnelled through [[Mikhail Frunze]] and [[Semyon Aralov]] on [[Vladimir Lenin]]'s orders,
and the fracturing of the Allied front by [[Franklin Bouillon]] and [[Carlo Sforza]].

Ended the empire, produced the [[Treaty of Lausanne]], and became the template studied by
[[Ho Chi Minh]], [[Mao Zedong]], [[Sinn Féin and the IRA]] and half the anti-colonial world.
"""),
("Greco-Turkish War", "1919–1922", """
The Greek invasion of Anatolia, backed by [[David Lloyd George]] and driven by [[Eleftherios
Venizelos]]'s *Megali Idea*. Broken at Dumlupınar, where [[Nikolaos Trikoupis]] was captured. Its
aftermath — the [[Burning of Smyrna]] and the [[Greco-Turkish Population Exchange]] — created
[[Aristotle Onassis]] the refugee and haunted [[Ernest Hemingway]] the young reporter.
"""),
("Chanak Crisis", "1922", """
Turkish forces advanced on the British garrison at Chanak; the British public and military refused a
second war. The humiliation collapsed [[David Lloyd George]]'s coalition government and ended his
career. [[Aubrey Herbert]] had predicted it exactly. [[Sinn Féin and the IRA]] read it as a masterclass.
"""),
("Treaty of Sèvres", "1920", """
The partition treaty [[Mehmed VI Vahideddin]] signed, which would have erased Turkey from the map.
Torn up by force — the reason [[Adolf Hitler]] and every revanchist in interwar Europe studied Ankara.
Germany's analogue was Versailles.
"""),
("Treaty of Lausanne", "1923", """
The only time after WWI that a defeated nation forced the victorious Allies back to the table and
rewrote its own peace treaty. [[İsmet İnönü]] negotiated it against [[Lord Curzon]], reportedly
weaponising his own partial deafness to simply not hear British threats.
"""),
("Abolition of the Sultanate", "1922", """
Ended six centuries of Ottoman rule and sent [[Mehmed VI Vahideddin]] out the back door of his palace
onto a British warship. Left the [[Abolition of the Caliphate]] as unfinished business, with
[[Abdulmejid II]] installed as a powerless spiritual figurehead.
"""),
("Abolition of the Caliphate", "March 1924", """
The single most consequential pen stroke in this vault. Ended a 1,300-year institution overnight and
gave [[Abdulmejid II]] twenty-four hours to leave the country.

Its blast radius: it devastated [[Ahmad Shawqi]] and [[Mehmet Akif Ersoy]], blindsided [[Mahatma
Gandhi]] mid-[[Khilafat Movement]], triggered [[Sheikh Said Rebellion]], destroyed [[Hussein bin
Ali]]'s dynasty, was pretexted on a letter from [[Aga Khan III]], delighted [[Periyar E. V.
Ramasamy]] and [[B.R. Ambedkar]], appalled [[Allama Iqbal]], [[Haj Amin al-Husseini]] and [[Muammar
Gaddafi]], and became the founding grievance of [[Sayyid Qutb]] and [[Ruhollah Khomeini]].
"""),
("Hat Law", "1925", """
State-mandated European headwear, on pain of criminal penalty. Immortalised — of all places — in
[[Antoine de Saint-Exupéry]]'s *The Little Prince*. Alienated [[Mehmet Akif Ersoy]]; copied by
[[King Zog I]] and [[Plaek Phibunsongkhram]].
"""),
("Alphabet Reform", "1928", """
Arabic script replaced by a purpose-built Latin alphabet in a matter of months, severing the
population from a thousand years of its own written record. Designed with [[Agop Dilaçar]].
Reverse-engineered against the Turkish state by [[Celadet Bedir Khan]] for Kurdish; admired as
revolutionary technique by [[Vladimir Mayakovsky]]; deplored as civilisational suicide by
[[Muammar Gaddafi]].
"""),
("Surname Law", "1934", """
Required every citizen to take a Western-style family name. Moiz Cohen became [[Munis Tekinalp]];
Hagop Martayan became [[Agop Dilaçar]]; and Dilaçar reportedly proposed the surname parliament
bestowed on the President himself — *Atatürk*, Father of the Turks.
"""),
("Turkish Civil Code", "1926", """
[[Mahmut Esat Bozkurt]] replaced Sharia with wholesale translations of the Swiss Civil Code, Italian
Penal Code and German Commercial Code. Centuries of jurisprudence swapped out in a single
parliamentary session. Cited as precedent by [[B.R. Ambedkar]] when drafting the Hindu Code Bill.
"""),
("Balkan Pact", "1934", """
Defensive alliance of Turkey, Greece, Romania and Yugoslavia built against [[Benito Mussolini]] and
[[Adolf Hitler]]. Architected with [[Nicolae Titulescu]] and [[Alexander I of Yugoslavia]], sustained
even by the Greek fascist [[Ioannis Metaxas]]. Alexander's assassination in Marseille in 1934 pulled
out its European anchor.
"""),
("Greco-Turkish Population Exchange", "1923", """
[[Fridtjof Nansen]]'s brutal arithmetic: 1.2 million Orthodox Christians expelled to Greece, ~400,000
Muslims to Turkey, sorted by religion. It permanently homogenised both states and ended their
territorial wars by physically removing the populations in dispute.
"""),
("Burning of Smyrna", "1922", """
The Greek and Armenian quarters of Izmir burned as the nationalist army took the city. It stripped
[[Aristotle Onassis]] of a family fortune and a homeland and, by his own account, manufactured the
ruthlessness that made him.
"""),
("Sheikh Said Rebellion", "1925", """
[[Sheikh Said]]'s armed uprising under the green flag of Islam, demanding restoration of Sharia and
the Caliphate. Crushed; Said executed. It hardened the regime's conviction that religious
conservatism was a lethal, active threat, and licensed far harsher enforcement of secularism.
"""),
("Ararat Rebellion", "1927–1930", """
[[Ihsan Nuri Pasha]] declared an independent Republic of Ararat and held off Ankara for three years.
Crushed with the republic's first use of mass aerial bombardment.
"""),
("Dersim Rebellion", "1937–1938", """
[[Seyid Riza]]'s revolt in the Alevi-Kurdish mountains, answered with an apocalyptic military
campaign — including combat sorties flown by [[Sabiha Gökçen]]. Thousands of civilian dead, mass
deportations, Riza hanged. The final violent consolidation of the Kemalist state.
"""),
("Black Sea Incident", "January 1921", """
[[Mustafa Suphi]] and fourteen leaders of the Communist Party of Turkey were forced onto a boat at
Trabzon and murdered at sea. Never formally traced to Atatürk, it decapitated Turkish communism and
guaranteed the revolution stayed nationalist and state-capitalist. See also [[Şefik Hüsnü]].
"""),
("1933 University Reform", "1933", """
Using [[Albert Malche]]'s audit as cover, the old Ottoman Darülfünun was abolished and two-thirds of
its faculty fired. The vacancy it created was filled by [[Philipp Schwartz]] with hundreds of Jewish
and dissident academics fleeing Hitler — [[Ernst Reuter]], [[Alexander Rüstow]], [[Bruno Taut]] among
them. A purge and a rescue operation running through the same door. See [[Albert Einstein]].
"""),
("Independence Tribunals", "1920s", """
Emergency revolutionary courts. After the 1926 İzmir assassination plot they were turned on the
regime's own founders — [[Rauf Orbay]] sentenced in absentia, [[Kâzım Karabekir]] tried, [[Halide
Edib Adıvar]] driven abroad.
"""),
("Women's Suffrage in Turkey", "1930–1934", """
Full suffrage granted in 1934, ahead of France and Italy. Granted top-down — which required
politically crushing [[Nezihe Muhiddin]], who had been demanding it from below since 1923. Praised by
[[Huda Sha'arawi]] and [[Eleanor Roosevelt]]; embodied by [[Sabiha Gökçen]] and [[Halet Çambel]].
"""),
("Khilafat Movement", "1919–1924", """
Indian Muslim campaign against British dismantling of the Caliphate, which [[Mahatma Gandhi]] joined
to forge Hindu-Muslim unity. Atatürk abolished the Caliphate himself in 1924 and the movement
evaporated. See [[Muhammad Ali Jinnah]], [[Allama Iqbal]], [[Aga Khan III]].
"""),
("Armenian Genocide", "1915", """
Perpetrated by the Ottoman CUP government under [[Talat Pasha]]. The transcript's Nazi thread argues
the regime read it as a *successful precedent* — Hitler's alleged 1939 line, *"Who, after all, speaks
today of the annihilation of the Armenians?"* Also the subject of the Blue Book that [[Arnold J.
Toynbee]] co-authored before switching sides, and the shadow over [[Agop Dilaçar]]'s career.
"""),
("Republic Monument", "1928, Taksim Square", """
Atatürk had Soviet commanders [[Kliment Voroshilov]] and [[Mikhail Frunze]] carved into the monument
standing behind him. Two Red Army marshals still stand permanently memorialised in the centre of a
NATO country's largest city.
"""),
("Anıtkabir", "Ankara", """
Atatürk's mausoleum. [[Charles de Gaulle]] laid a wreath here in 1968; the samurai sword from
[[Prince Takamatsu]] is still on display; [[Bruno Taut]] designed the catafalque for the 1938 funeral
at which [[William Birdwood]] saluted the coffin from the Halkevi balcony.
"""),
]
for n, when, b in E:
    note("Events", n, {"type": "event", "when": when, "tags": ["event"]}, b)

# ---------------- CONCEPTS ----------------
C = [
("Kemalism", """
The exportable ideological product: secular, authoritarian, top-down modernisation carried out by a
military vanguard in a one-party state, aimed at forging a homogenous national identity out of
imperial wreckage. Its "Six Arrows" were republicanism, nationalism, populism, statism
([[Devletçilik]]), secularism and revolutionism.

Copied wholesale by [[Reza Shah Pahlavi]], [[Habib Bourguiba]], [[King Zog I]], [[Plaek
Phibunsongkhram]], [[Amanullah Khan]], [[Gamal Abdel Nasser]], [[Pervez Musharraf]] and — with the
polarity reversed — [[Celadet Bedir Khan]] and [[Sati' al-Husri]]. Studied and rejected by [[Mao
Zedong]]. Treated as the enemy by [[Sayyid Qutb]], [[Ruhollah Khomeini]], [[Mustafa Sabri Efendi]] and
[[Said Nursi]].
"""),
("Devletçitlik placeholder", ""),
("Devletçilik", """
Statism: state-owned railways, factories and banks, built to break European economic monopolies.
Its intellectual origin is startling — [[Alexander Parvus]], the Marxist who helped finance the
Russian Revolution, argued during his Istanbul years that the Ottoman answer was not proletarian
revolution but a state-backed national bourgeoisie. Observing it from Istanbul in the 1930s,
[[Alexander Rüstow]] coined the word *neoliberalism* looking for a middle path. Its industrial idol
was [[Henry Ford]]; its casualty was [[Vecihi Hürkuş]].
"""),
("Turkish History Thesis", """
State-sponsored pseudohistory claiming the ancient Turks as the foundational race of Sumerian,
Hittite and Egyptian civilisation, with Turkish as the root of all human language (the Sun Language
Theory). Its principal academic vehicle was [[Afet İnan]], an adopted daughter built into a
credentialled historian for the purpose. Partly seeded by [[H.G. Wells]]'s *Outline of History*.
"""),
("Nazi Racial Hierarchy", """
The transcript's opening argument: Nazi racial ideology was tiered, not a single ladder. Nordic
Germans at the top; other Germans and northern Europeans below; Slavs as *Untermenschen* marked for
subjugation and demographic elimination under [[Lebensraum]]; Black Africans near the bottom.

Jews were not the bottom rung — they were placed *outside* the hierarchy as its negation: an active,
parasitic counter-force whose function was to dissolve racial civilisation as such. Hence a
qualitatively different genocide: Slavs were to be worked to death and displaced for territory, Jews
were to be exterminated everywhere without exception. The Office of Racial Policy formally framed the
laws as dividing "Jews" from people of "German and related blood" rather than Aryan from non-Aryan.

Arabs, South Asians and other non-Europeans sat in a deliberately ambiguous middle — not an oversight
but a structural feature enabling tactical suspension of racial categories when useful. See [[Nazi
Outreach to the Muslim World]]. Turks were the exception that proves the shape: consistently
*elevated*, ascribed genuine racial value, on account of the infatuation documented in [[Adolf
Hitler]] and [[Carl Schmitt]].
"""),
("Lebensraum", """
The drive to clear eastern territory for German settlement — the engine of the eliminationist logic
aimed at Slavs. Arabs and South Asians posed no equivalent territorial obstacle, which is precisely
why the ideology could afford to be flexible about them. See [[Nazi Racial Hierarchy]].
"""),
("Nazi Outreach to the Muslim World", """
Instrumental, not ideological. David Motadel's argument: Nazi courting of Muslim and Arab populations
was a wartime tool for destabilising the British and French empires, with racial categories
selectively suspended rather than abandoned.

Mechanisms: [[Haj Amin al-Husseini]]'s Arabic broadcasts and SS recruitment; Johann von Leers
grafting Nazi conspiracy frameworks onto existing Quranic and jurisprudential language about Jews
(Jeffrey Herf's thesis); [[Walter Gross]] assuring [[Rashid Ali al-Kilani]] that Nazi theory rated
Arabs a "very high caste"; German orientalist scholars manufacturing Islam/National-Socialism
parallels; Muslim SS formations beyond Handschar — the Eastern Turkic corps, Skanderbeg,
Caucasian-Mohammedan. Hitler made *The Lives of a Bengal Lancer* compulsory viewing for the SS.

The counterweight: [[Subhas Chandra Bose]] got nothing, because *Mein Kampf* treats the British
Empire as a civilisational achievement worth preserving for keeping Indians under European control.
"""),
("Village Institutes", """
Köy Enstitüleri — rural children given secular, scientific and practical training and sent back as
teachers. The Kemalist education revolution as a state-scale experiment in [[John Dewey]]'s
pragmatism.
"""),
("Six Arrows", """
Republicanism, Nationalism, Populism, Statism ([[Devletçilik]]), Secularism, Revolutionism. The formal
doctrine of [[Kemalism]].
"""),
]
for n, b in C:
    if not b.strip():
        continue
    note("Concepts", n, {"type": "concept", "tags": ["concept"]}, b)

print("core done")
