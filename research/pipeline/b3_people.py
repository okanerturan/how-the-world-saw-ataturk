# -*- coding: utf-8 -*-
from _lib import person

P = [
("Franklin Bouillon", dict(role="French diplomat and former cabinet minister", nat="French", life="1870–1937",
  stance="negotiator who defected", tags=["diplomat", "observer"], body="""
Sent to Ankara in 1921 to dictate terms to the nationalist rebels, he was comprehensively outmanoeuvred
by Atatürk's leverage and personal charisma. Realising the French army could not hold southern
Anatolia against disciplined Kemalist forces, he essentially went rogue: he negotiated and signed the
Treaty of Ankara, ending the Franco-Turkish War, formally recognising Atatürk's government and
shattering the united Allied front. The British were furious — Atatürk had weaponised French war
weariness to break the European blockade. See [[Carlo Sforza]], who did the same for Italy.
""")),

("Mustafa Sabri Efendi", dict(role="Last Shaykh al-Islām of the Ottoman Empire", nat="Ottoman Turkish", life="1869–1954",
  stance="theological arch-enemy", tags=["antagonist", "islamist", "exile"], body="""
The highest religious authority in the Sunni Islamic world, appointed by the Sultan, and an
uncompromising opponent of the nationalist movement — he issued fatwas condemning Atatürk and his
soldiers to death as rebels. When the war was won and the Sultanate and Caliphate abolished he fled
to Egypt, spending the rest of his life writing dense, furious treatises condemning Atatürk as an
apostate who had permanently crippled the spiritual unity of Islam. Those writings remain the
intellectual bedrock of hardline anti-Kemalist Islamism. See [[Said Nursi]], [[Sayyid Qutb]].
""")),

("B.H. Liddell Hart", dict(role="Military historian and theorist", nat="British", life="1895–1970",
  stance="professional admirer", tags=["observer", "military"], body="""
Viewed Atatürk purely through operational brilliance while British politicians lamented Turkey's
rise. Analysing his command at [[Gallipoli Campaign]] and his grand strategy in the [[Greco-Turkish
War]], Hart saw the master of the "indirect approach" — a general who never wasted men in frontal
assaults when a psychological or logistical flank could be turned. He taught the campaigns in Western
military academies, arguing the rarest part of the genius was knowing exactly when to stop fighting
and start negotiating, never letting military victory outrun supply lines. Also biographer to [[T.E.
Lawrence]].
""")),

("Amin al-Rihani", dict(role="Writer, founder of Arab-American literature", nat="Lebanese-American", life="1876–1940",
  stance="admirer", tags=["admirer", "literary"], body="""
While conservative Arabs mourned the Caliphate he watched the Kemalist revolution with fascination
and approval. With the Arab world under British and French mandate in the late 1920s, he argued the
Arab nations needed to learn from Atatürk's ruthless pragmatism — that true sovereignty would arrive
only when they produced their own uncompromising unifier, someone who could separate mosque from
state, break the clerics and build identity on modernisation rather than religious nostalgia. Compare
[[Sati' al-Husri]], [[Taha Hussein]].
""")),

("Lord Curzon", dict(role="British Foreign Secretary, former Viceroy of India", nat="British", life="1859–1925",
  stance="defeated adversary", tags=["antagonist", "diplomat"], body="""
The embodiment of British imperial arrogance, sent to Lausanne in 1923 to force the Kemalist
delegation into a subordinate role in the new order. Instead [[İsmet İnönü]] famously used his partial
deafness to simply not hear the threats, refusing anything short of total sovereignty. Curzon wrote
furious letters home about "Asiatic" Turkish stubbornness, but he was a realist: he recognised he had
been outplayed militarily and politically and signed the [[Treaty of Lausanne]] on Atatürk's terms.
""")),

("Percy Loraine", dict(role="British Ambassador to Turkey", nat="British", life="1880–1961",
  stance="close personal friend", tags=["diplomat", "friend"], body="""
Appointed in 1933 to repair the relationship with Ankara. Rather than play the haughty imperial envoy
he treated Atatürk as an absolute equal, and the two found a shared sense of humour, a taste for
late-night debate and a passion for poker — becoming genuine friends who stayed up until dawn
drinking and playing cards at the presidential palace. That personal channel bypassed formal
diplomacy and solidified the UK-Turkey alliance that mattered when WWII came. He was reportedly one of
the few foreign dignitaries to weep openly at the funeral. See [[King Edward VIII]].
""")),

("Muammar Gaddafi", dict(role="Leader of Libya", nat="Libyan", life="1942–2011",
  stance="fierce detractor", tags=["antagonist"], body="""
Built his regime on a volatile mix of Arab nationalism, socialism and Islamic populism, and read
Atatürk not as an anti-imperialist hero but as a catastrophic traitor. By abolishing the Caliphate,
imposing the Latin alphabet and turning Turkey's back on the Middle East to face Europe, Atatürk had
in his view abandoned the Islamic world to Western imperialism. He used Kemalism as a rhetorical
punching bag: the definitive example of a nation losing its soul by mimicking its colonisers. Compare
[[Gamal Abdel Nasser]], who drew the opposite conclusion.

(Source check, Nov 2026: this characterisation is inherited from the transcript. The one sourced Gaddafi
text found so far, the 2002 essay "Turkey, Europe and the Bin-Ladenists", attacks the alphabet reform but
names Atatürk only once, neutrally; no source for "traitor" has been found. See [[Postwar and Third World
Leaders on Atatürk in Their Own Words]].)
""")),

("Alija Izetbegović", dict(role="First President of Bosnia and Herzegovina", nat="Bosnian", life="1925–2003",
  stance="critic, partially converted", tags=["conflicted"], body="""
In *The Islamic Declaration* he sharply criticised the secular reforms, arguing that forcing Western
culture onto a Muslim population produces a spiritually empty, schizophrenic society. Then he had to
fight an existential war for his people's survival in the 1990s, and the perspective shifted. He
never accepted [[Kemalism]] ideologically, but he acknowledged the necessity of Atatürk's military
pragmatism — that without that ruthless state-building violence the Turkish nation would have been
erased from the map of Europe, exactly the fate he was trying to avoid for Bosnia.
""")),

("Clair Price", dict(role="Journalist", nat="American", life="c. 1890s–1960s",
  stance="explainer", tags=["observer"], body="""
The early-1920s American public was isolationist and heavily prejudiced against the "Terrible Turk."
Price travelled to Anatolia and became one of the first Westerners to explain the Kemalist movement
accurately to English-speaking readers. *The Rebirth of Turkey* (1923) dismantled the fanatic
stereotype and presented Atatürk as a rational modernizer, helping shift American policy from
missionary-driven hostility toward pragmatic recognition. See [[Mark L. Bristol]], [[James Harbord]].
""")),

("Ahmad Shawqi", dict(role="Poet, 'Prince of Poets'", nat="Egyptian", life="1868–1932",
  stance="admirer, then devastated", tags=["conflicted", "literary"], body="""
The emotional whiplash of the Arab world in two poems. In 1922, when the Greek army was pushed into
the Aegean, he wrote a soaring epic calling Atatürk the *"Khalid of the Turks"* — after Khalid ibn
al-Walid, the undefeated general of early Islam — and hailing him as the saviour of the Muslim world.

Two years later came the [[Abolition of the Caliphate]]. The man he had immortalised as a holy
warrior had destroyed a 1,300-year-old institution, and Shawqi answered with a famous elegy mourning
the Caliphate. *(Corrected Oct 2026 from the printed text:* the elegy does not retract the praise or
call him an apostate — "أأقول من أحيا الجماعة ملحد…؟", shall I call the one who revived the community
an unbeliever? — but urges "Convey the advice to the Ghazi." See
[[Shawqi's Two Poems on the Ghazi, 1922–1924 (al-Shawqiyyat)]].*)
""")),

("Munis Tekinalp", dict(role="Ideologue of Turkish nationalism; born Moiz Cohen", nat="Ottoman Jewish (Salonica)", life="1883–1961",
  stance="radical Kemalist", tags=["ideologue", "turkish"], body="""
An Orthodox Jewish scholar from Thessaloniki who concluded the multi-ethnic Ottoman model was dead
and that his community's only survival route was total assimilation into the new republic. He changed
his name under the [[Surname Law]] logic and became one of the most fervent ideologues of
[[Kemalism]], writing foundational texts on complete secularisation and publishing a "Ten
Commandments" for Turkish Jews — abandon French and Ladino, speak only Turkish in public, Turkify
your names, adopt the secular nationalist identity wholesale. Still contested: visionary pragmatist
who protected his community, or a man who erased his own heritage.
""")),

("Ernst Reuter", dict(role="German Social Democrat, later Mayor of West Berlin", nat="German", life="1889–1953",
  stance="exile sheltered by Turkey", tags=["exile", "german-exiles"], body="""
Thrown into a concentration camp when the Nazis took power; released under international pressure in
1935 and granted asylum and employment in Turkey. He spent over a decade in Ankara, learned fluent
Turkish, became a professor of urban planning and helped design the modern infrastructure of the
capital.

He returned to Germany after the war and became the legendary Mayor of West Berlin who led the city
through the 1948 Soviet blockade — crediting his survival and his ability to rebuild a democratic
Germany to the sanctuary Atatürk's republic gave him. See [[1933 University Reform]], [[Philipp
Schwartz]].
""")),

("Sheikh Said", dict(role="Zaza-Kurdish Sunni cleric and rebel leader", nat="Kurdish (Ottoman/Turkish)", life="d. 1925",
  stance="armed antagonist", tags=["antagonist", "kurdish", "victim"], body="""
Viewed Atatürk as an apostate destroying the fabric of society. The [[Abolition of the Caliphate]],
the closure of religious schools and the ban on the fez sent a cultural shockwave through the
conservative eastern provinces, and in 1925 he launched a mass armed rebellion under the green flag
of Islam demanding Sharia, the Caliphate and the Sultan. It was an existential threat to the project;
Atatürk answered with overwhelming force and had him executed. See [[Sheikh Said Rebellion]].
""")),

("Prince Takamatsu", dict(role="Japanese prince, brother of Emperor Hirohito", nat="Japanese", life="1905–1987",
  stance="imperial envoy", tags=["diplomat"], body="""
Sent by Hirohito on a publicised 1931 state visit to Ankara. Japan viewed Turkey as a kindred spirit —
a martial, disciplined nation that had adopted Western technology and organisation without
surrendering to Western empires. He presented Atatürk with a hand-forged samurai sword as a symbol of
martial respect; it is still displayed at [[Anıtkabir]]. No formal alliance followed, but the visit
shows how heavily Japan weighed the Turkish case. See [[Ōkawa Shūmei]].
""")),

("Halide Edib Adıvar", dict(role="Novelist, feminist, nationalist", nat="Turkish", life="1884–1964",
  stance="founding ally turned dissident", tags=["turkish", "dissident", "women"], body="""
A founding mother of the revolution who did not merely write propaganda: she enlisted, fought at the
front and was promoted to corporal. She and Atatürk were initially close allies.

Once the war was won their visions diverged violently. She wanted a multi-party democracy; he
believed rapid top-down modernisation required a one-party dictatorship. When she helped form an
opposition party in 1924 he crushed it, and facing a purge the heroine of the revolution fled her own
country in 1926. She spent over a decade in exile in Europe and the US, writing about the brilliance
of the revolution while attacking the cult of personality of the man who led it. Compare [[Kâzım
Karabekir]], [[Rauf Orbay]].
""")),

("Periyar E. V. Ramasamy", dict(role="Founder of the Dravidian movement", nat="Indian (Tamil)", life="1879–1973",
  stance="messianic admirer", tags=["admirer", "reformer"], body="""
A militant atheist who spent his life attacking the Hindu caste system and Brahmin clerical power. He
celebrated the [[Abolition of the Caliphate]] and the closure of the Sharia courts, and held Atatürk
up in his newspaper *Kudi Arasu* as the ultimate weapon against religious apologists: if the Turks —
stereotyped as fierce religious warriors — could recognise theology was holding them back and purge
it from government, Indians had no excuse for clinging to caste. Compare [[B.R. Ambedkar]], who made
the legal version of the same argument.
""")),

("Semyon Aralov", dict(role="First Soviet Ambassador to Turkey", nat="Soviet", life="1880–1969",
  stance="ally, outplayed", tags=["diplomat", "communist"], body="""
Sent by Lenin in 1922 to funnel gold and weapons to Ankara so the Turks would keep fighting the
British, while pulling the new republic into the communist orbit. His memoirs are an intimate portrait
— late-night dinners, heavy drinking, intense philosophical argument — and full of admiration for
Atatürk's tactical genius.

He was comprehensively outplayed. Atatürk took every rouble and rifle, won his war, then arrested and
crushed the Turkish communist party, defeating the ideological half of Aralov's mission without a
shot fired at the Red Army. See [[Mustafa Suphi]], [[Şefik Hüsnü]], [[Mikhail Frunze]].
""")),

("Talat Pasha", dict(role="Ottoman Interior Minister, one of the Three Pashas", nat="Ottoman Turkish", life="1874–1921",
  stance="repudiated predecessor", tags=["ottoman", "antagonist"], body="""
Principal architect of the [[Armenian Genocide]] and one of the dictators who dragged the empire into
WWI. He fled to Germany at the collapse and was assassinated there in 1921.

Atatürk despised him, [[Enver Pasha]] and the whole Young Turk leadership as reckless imperial
gamblers who had destroyed the nation for Pan-Turkic fantasies. Consolidating power, he drew an
uncompromising line: the new republic would be strictly defensive, confined to its national borders
and severed from the crimes and debts of the Ottoman past, with the exiled leadership formally banned
from returning.
""")),

("Mehmed VI Vahideddin", dict(role="36th and last Sultan of the Ottoman Empire", nat="Ottoman", life="1861–1926",
  stance="displaced sovereign", tags=["ottoman", "monarch", "victim"], body="""
In 1919, hoping to appease the Allies, he dispatched a young general named Mustafa Kemal to eastern
Anatolia to disband the remaining Ottoman units and suppress nationalist resistance. It was a fatal
miscalculation: once clear of Istanbul, Kemal used the official mandate to do the exact opposite and
launched the [[Turkish War of Independence]].

When he then signed the [[Treaty of Sèvres]] the Kemalists declared him a traitor. After the
[[Abolition of the Sultanate]] in 1922 he fled out the back door of his palace aboard the British
warship HMS *Malaya*, and died in exile in Italy — the last of a dynasty that had terrified Europe for
six centuries. His cousin [[Abdulmejid II]] inherited the empty title.
""")),

("Abdulmejid II", dict(role="Last Caliph of Islam", nat="Ottoman", life="1868–1944",
  stance="erased figurehead", tags=["ottoman", "victim"], body="""
When the Sultanate was abolished in 1922 the Caliphate was not; parliament stripped the title of all
political power and "elected" Abdulmejid — a refined intellectual, accomplished painter and patron of
the arts — as a purely spiritual figurehead confined to an Istanbul palace.

His existence was a magnet for anti-republican forces: crowds gathered like subjects whenever he rode
to Friday prayers. Atatürk concluded the republic could never be secure while an Ottoman held the
title, and in March 1924 abolished it entirely, giving Abdulmejid and his family twenty-four hours to
leave Turkey forever. His daughter was [[Dürrüşehvar Sultan]]. See [[Abolition of the Caliphate]].
""")),

("Said Nursi", dict(role="Islamic scholar, founder of the Nur movement", nat="Kurdish-Turkish", life="1877–1960",
  stance="spiritual dissident", tags=["antagonist", "islamist", "turkish"], body="""
Initially supported the nationalist war and was invited to Ankara in 1922 to address the new
parliament. Horrified by the aggressively secular direction, he and Atatürk had a famously heated
argument — Atatürk allegedly shouting that Nursi was trying to drag the nation back into the dark
ages.

Concluding that armed rebellion was futile and political opposition would be crushed, he withdrew
entirely and spent decades under house arrest or in prison writing the *Risale-i Nur*, a vast Quranic
commentary arguing for a "spiritual jihad" of education and quiet faith as the way to outlast the
secular state. The Nur movement remains one of the most powerful Islamic networks in Turkey — the
intellectual resistance that proved far harder to kill than [[Sheikh Said]]'s armed one.
""")),

("Ihsan Nuri Pasha", dict(role="Kurdish commander, leader of the Republic of Ararat", nat="Kurdish", life="1893–1976",
  stance="separatist antagonist", tags=["antagonist", "kurdish"], body="""
An ethnic Kurdish officer from the Ottoman military who mutinied as Ankara centralised power and
enforced strict Turkish nationalism — banning Kurdish in public, closing Kurdish schools. In 1927 he
led a mass uprising in the east and declared the independent Republic of Ararat, holding off Kemalist
forces for three years and creating a deeply embarrassing crisis for Ankara.

The state answered with the full modernised weight of the army, including the republic's first
widespread use of aerial bombardment. The [[Ararat Rebellion]] was crushed in 1930 and he fled to
Iran, leaving the unresolved conflict that runs to the present. See [[Celadet Bedir Khan]],
[[Nelson Mandela]].
""")),

("Şefik Hüsnü", dict(role="Founder of the Communist Party of Turkey (TKP)", nat="Turkish", life="1887–1959",
  stance="suppressed ally", tags=["victim", "communist", "turkish"], body="""
Turkish communists actively supported the [[Turkish War of Independence]] as a legitimate
anti-imperialist struggle. Once power was secured Atatürk had no intention of sharing it or letting
Soviet ideology infect the republic: the TKP was banned, its papers shut, its organisers hunted.
Hüsnü spent almost his entire life in and out of Kemalist prisons or in exile — the living limit of
Atatürk's tolerance for competing foreign ideologies. See [[Mustafa Suphi]], [[Nâzım Hikmet]].
""")),

("Lord Kinross", dict(role="Historian; Patrick Balfour", nat="Scottish", life="1904–1976",
  stance="canonical Western biographer", tags=["observer", "biographer"], body="""
Essentially commissioned by the British government in the 1950s to write a definitive biography.
*Atatürk: The Rebirth of a Nation* (1960) became an international bestseller. Writing during the Cold
War, with Turkey a vital NATO ally against the USSR, Kinross painted a highly sympathetic portrait —
not hiding the ruthlessness or the heavy drinking, but framing the authoritarianism as justified by
the modernisation it achieved. For decades this was the lens through which Western politicians and
academics saw Turkey, fixing Atatürk's Western reputation as enlightened despot rather than tyrant.
""")),

("Mikhail Frunze", dict(role="Red Army commander and strategist", nat="Soviet", life="1885–1925",
  stance="ally", tags=["ally", "communist", "military"], body="""
Fresh from defeating the White Army in Crimea, he was sent by Lenin on a sensitive diplomatic mission
to Ankara in late 1921. He spent weeks with Atatürk and the Turkish high command; the two military men
bonded over a shared strategic reality — both fighting proxy armies funded by Britain and France. His
glowing reports to Moscow kept the gold and weapons flowing at the most critical juncture of the war.
He too was carved into the [[Republic Monument]] behind Atatürk. See [[Kliment Voroshilov]].
""")),

("Clemens Holzmeister", dict(role="Architect", nat="Austrian", life="1886–1983",
  stance="builder of the new capital", tags=["exile", "builder"], body="""
Atatürk despised the political and religious baggage of Istanbul and needed a new secular capital, so
he chose Ankara — then a dusty, malarial provincial town — and imported Europe to build it. Fleeing
the rising fascist tide, Holzmeister relocated with dozens of other German and Austrian planners and
became chief architect of the republic, designing the Grand National Assembly, the Ministry of
Defence and the presidential palace. He manifested the ideology in concrete: a Bauhaus-inflected
European city planted on the Anatolian steppe as a deliberate break from Ottoman Islamic
architecture. See [[Bruno Taut]].
""")),

("Seyid Riza", dict(role="Alevi-Kurdish tribal leader of Dersim", nat="Kurdish (Alevi)", life="d. 1937",
  stance="rebel, executed", tags=["antagonist", "kurdish", "victim"], body="""
The Kemalist state demanded a centralised homogenous nation, fundamentally incompatible with the
autonomous tribal structures of eastern Anatolia. Dersim (modern Tunceli) had been left largely alone
even by the Ottomans, who could not project power into its mountains. Atatürk refused to tolerate a
state within a state, and when barracks and secular law arrived in 1937 Seyid Riza rebelled.

The response was apocalyptic — a modernised campaign including Air Force sorties flown partly by
[[Sabiha Gökçen]] — producing thousands of civilian deaths and mass deportations. Riza was captured
and hanged. See [[Dersim Rebellion]].
""")),

("Joseph Grew", dict(role="First US Ambassador to the Republic of Turkey", nat="American", life="1880–1965",
  stance="diarist", tags=["diplomat", "observer"], body="""
Ambassador 1927–1932, and the source historians lean on for what interacting with Atatürk was
actually like. Atatürk despised formal diplomatic protocol and forced ambassadors to adapt to his
chaotic schedule: Grew's diaries (*Turbulent Era*) describe being summoned to the palace late at
night for enormous alcohol-fuelled dinners that turned into grinding intellectual debates running to
six or seven in the morning, with Atatürk chain-smoking, drinking heavily and relentlessly quizzing
European diplomats on Roman history and linguistic theory. Grew came away exhausted and mesmerised,
calling him one of the most terrifyingly intelligent, dominating figures of the century. Compare
[[Semyon Aralov]] and [[Percy Loraine]], who described the same nights.
""")),

("Ziya Gökalp", dict(role="Sociologist, ideological father of Turkish nationalism", nat="Turkish", life="1876–1924",
  stance="mentor, outgrown", tags=["theorist", "turkish"], body="""
Argued in the empire's dying days that a multi-ethnic religious patchwork was doomed, and proposed
"Turkism": adopt Western science and technology, ground identity strictly in Turkish culture and
language, push Islam out of the political sphere into the private moral one.

Atatürk turned the theory into state law with terrifying efficiency — *"My flesh and bones belong to
my parents, but my beliefs belong to Ziya Gökalp"* — then went further and faster than Gökalp had
ever advocated, dismantling religious institutions with a radicalism that surprised his own mentor.
He died in 1924 as the revolution was accelerating: the architect of a house he never had to live in.
""")),

("Kâzım Karabekir", dict(role="General; commander of the Eastern Army", nat="Turkish", life="1882–1948",
  stance="indispensable ally, then purged", tags=["turkish", "dissident", "military"], body="""
Without him there is no republic. In 1919 the Istanbul government ordered Karabekir — a respected
conservative general commanding the only intact army in eastern Anatolia — to arrest the rebellious
Mustafa Kemal. He walked into the headquarters, saluted, and said *"I and my army are at your
command, Pasha."* That single act of insubordination started the war.

They were fundamentally different men: Karabekir was devout, conservative and wanted a gradual
democratic transition, and he was horrified by the [[Abolition of the Caliphate]] and the enforcement
of secularism. When he helped form an opposition party in 1924 Atatürk purged him ruthlessly —
arrested, tried for treason before a Kemalist tribunal, then a decade of quiet house arrest, returning
to politics only after Atatürk's death. See [[Independence Tribunals]], [[Rauf Orbay]].
""")),

("Nâzım Hikmet", dict(role="Poet", nat="Turkish", life="1902–1963",
  stance="admirer of the general, prisoner of the state", tags=["victim", "literary", "communist", "turkish"], body="""
The greatest Turkish poet of the century and a passionate romantic communist. He idolised the
anti-imperialist struggle and wrote poetry supporting the nationalist army during the war — but he
wanted a proletarian revolution, and Atatürk was building a fiercely nationalist state-capitalist
republic. He refused to stop writing Marxist poetry, and spent over a decade in Kemalist prisons.

He respected Atatürk the anti-imperialist general and despised Atatürk the bourgeois dictator. His
translator into Greek was [[Yiannis Ritsos]]. See [[Şefik Hüsnü]].
""")),

("Tevfik Fikret", dict(role="Late-Ottoman poet", nat="Ottoman Turkish", life="1867–1915",
  stance="posthumous muse", tags=["literary", "influence"], body="""
Died before the republic existed, yet Atatürk held him in something close to religious reverence. A
poet of blazing humanism and secularism who attacked religious dogma, clerical corruption and Islamic
traditionalism at a time when doing so was taboo, arguing for reason, science and a global
brotherhood of humanity.

His forbidden poems circulated secretly among military cadets; decades later the President quoted him
from memory and credited him with breaking the psychological chains of Ottoman religious fatalism —
*"He is the one who created my worldview."* The whole cultural revolution reads as an attempt to build
the society Fikret had written.
""")),

("Fevzi Çakmak", dict(role="Chief of the General Staff, Field Marshal", nat="Turkish", life="1876–1950",
  stance="loyal paradox", tags=["turkish", "military", "inner-circle"], body="""
A devout, practising, highly conservative Muslim who never drank and prayed five times a day — the
exact demographic that opposed the cultural revolution — and, alongside Atatürk, the only other man
to hold the rank of Field Marshal. He was unflinchingly loyal.

Atatürk purged conservative generals like [[Kâzım Karabekir]] but trusted Çakmak completely, because
Çakmak held absolutely that the military must stay out of politics. He silently oversaw the army
while the Caliphate was abolished, the shrines closed and Islamic dress banned. He proved the rule of
the system: personal piety was tolerated, so long as it never challenged the supremacy of the secular
state.
""")),

("Agop Dilaçar", dict(role="Linguist; born Hagop Martayan", nat="Armenian (Istanbul)", life="1895–1979",
  stance="architect of the new language", tags=["turkish", "linguist", "paradox"], body="""
A brilliant Armenian linguist who spoke over a dozen languages — an improbable figure in a fiercely
nationalist Turkish state so soon after the [[Armenian Genocide]]. But Atatürk was obsessed with
purging Turkish of Arabic and Persian influence to reach its "pure" Central Asian roots, recognised
the man's genius, and personally recruited him.

Atatürk renamed him *Dilaçar* — "Language Opener." He became the first Secretary General of the
Turkish Language Association, instrumental in designing the Latin-based alphabet and researching the
language's etymology. In a striking twist, when the [[Surname Law]] passed in 1934 it was reportedly
Dilaçar, the ethnic Armenian, who proposed the surname parliament bestowed on the President:
*Atatürk*. See [[Alphabet Reform]], [[Turkish History Thesis]].
""")),

("Latife Uşşaki", dict(role="Atatürk's wife, 1923–1925", nat="Turkish", life="1898–1975",
  stance="wife; personal collision", tags=["turkish", "women", "personal"], body="""
Wealthy, fiercely intelligent, educated in Paris and London — exactly the modern Westernised woman he
wanted as the face of the new republic. She defied Ottoman convention: refused the veil, rode on
horseback with him to military reviews, campaigned alongside him for women's political rights.

The marriage imploded in two years. He wanted a liberated modern woman in public and total submission
at home, hosting loud all-night drinking sessions with his political circle; she refused to be a prop,
argued with him openly, criticised the drinking and demanded to be treated as an equal. Unable to
tolerate being challenged in his own house he unilaterally divorced her in 1925. She lived the rest
of her life in seclusion and never spoke publicly about the marriage — a standing symbol of the
friction between his public feminism and his dictatorial temperament. See [[Fikriye Hanım]].
""")),

("Mahmut Esat Bozkurt", dict(role="Minister of Justice", nat="Turkish", life="1892–1943",
  stance="executor of the legal revolution", tags=["turkish", "inner-circle"], body="""
Atatürk was the visionary; Bozkurt swung the sledgehammer at the Ottoman legal system. Told to
abolish Sharia, he skipped the gradual transition and the drafting committee entirely and sent
translators to Europe.

In 1926 he presented parliament with translated copies of the Swiss Civil Code, the Italian Penal
Code and the German Commercial Code — if the goal is to become a modern Western nation, adopt the
best laws the West has already written — and forced them through, replacing centuries of Islamic
jurisprudence overnight. He defended it by saying a nation's laws should rest on the realities of
life, not on supposed revelations from the sky. See [[Turkish Civil Code]].
""")),

("James Harbord", dict(role="US Army general", nat="American", life="1866–1947",
  stance="assessor", tags=["observer", "military"], body="""
In 1919 the United States was seriously considering a mandate over Anatolia and Armenia, and Wilson
sent Harbord to assess whether it was feasible. He travelled deep into Anatolia and met the
rebellious officer Mustafa Kemal at Sivas.

The British and French were telling Washington the nationalists were a disorganised band of bandits.
Harbord interviewed Kemal extensively and concluded the Europeans were delusional: this was a
brilliant, organised commander leading a determined mass movement, and any US occupation would need
hundreds of thousands of troops and end in an unwinnable guerrilla war. Largely on that assessment
the Senate refused the mandate. See [[Mark L. Bristol]].
""")),

("Otto Liman von Sanders", dict(role="Prussian general commanding Ottoman forces at Gallipoli", nat="German", life="1855–1929",
  stance="superior who yielded", tags=["military", "german"], body="""
Appointed by the Ottomans to command the defence of the Dardanelles in 1915, he found an obscure
lieutenant colonel repeatedly clashing with his high command. Mustafa Kemal correctly predicted the
Anzac Cove and Suvla Bay landings and begged for reinforcements; when the command hesitated he
committed what amounted to mutiny, ordering his troops forward on his own initiative — *"I am not
ordering you to attack, I am ordering you to die."*

Rather than court-martial him, Liman von Sanders recognised that those instincts had saved the
peninsula and handed him command of the entire Anafartalar front. The Prussian aristocrat yielded to
the local officer, and the legend that made a president was born. See [[Gallipoli Campaign]].
""")),
]

for name, kw in P:
    person(name, **kw)
print(f"batch3: {len(P)} people")
