# -*- coding: utf-8 -*-
from _lib import person

P = [
("Aristotle Onassis", dict(role="Shipping magnate", nat="Greek (born Smyrna)", life="1906–1975",
  stance="refugee created by the victory", tags=["victim", "observer"], body="""
A Greek teenager in cosmopolitan Ottoman Smyrna when the nationalist army broke the Greek lines and
entered the city in 1922. In the chaos and the fire that followed, his family lost its entire shipping
fortune overnight and several relatives were imprisoned or killed. He escaped to Argentina stateless
and penniless.

The trauma forged the worldview: governments, borders and laws are fragile, and the only real
security is capital and leverage. The [[Burning of Smyrna]] took his homeland and manufactured the
hyper-pragmatic ruthlessness that made him. Compare [[Ernest Hemingway]], reporting the same weeks.
""")),

("William Birdwood", dict(role="British Field Marshal, commander of ANZAC at Gallipoli", nat="British", life="1865–1951",
  stance="old enemy, mourner", tags=["former-enemy", "military"], body="""
Locked in a bloody months-long stalemate with Atatürk at [[Gallipoli Campaign]] until forced to
organise the total Allied evacuation. Rather than lifelong bitterness, the trenches produced mutual
respect.

Twenty-three years later Britain sent the 73-year-old Birdwood to represent the Empire at the state
funeral in Ankara, 21 November 1938. Too ill to march in the procession, he saluted the passing
coffin of the man who had handed him the greatest defeat of his career from the balcony of the
Ankara Halkevi, held upright on his feet — a tribute Turkish coverage recorded with deep
appreciation. (The popular retelling — swollen feet, refused boots, civilian shoes on the march — is
embellishment; Turkish fact-checkers have worked over the photo lore.)
""")),

("Rauf Orbay", dict(role="Ottoman naval hero; first PM of the provisional government", nat="Turkish", life="1881–1964",
  stance="founding ally, exiled dissident", tags=["turkish", "dissident"], body="""
The captain who was forced to sign the Armistice of Mudros in 1918, surrendering the empire. Desperate
to save the nation he joined Atatürk in Anatolia and became one of the founding leaders of the
resistance and the first prime minister of the provisional government.

Like [[Kâzım Karabekir]] he was a conservative who believed in democracy and the preservation of the
Caliphate, and he broke publicly with Atatürk over the consolidation of absolute power. He was not
spared: in 1926, under the [[Independence Tribunals]] following the İzmir assassination plot, he was
tried and sentenced in absentia and spent a decade in European exile — the conservative patriots who
fought for Turkey's survival, steamrolled by the radicalism they had enabled.
""")),

("Albert Malche", dict(role="Professor of pedagogy, University of Geneva", nat="Swiss", life="1876–1956",
  stance="commissioned auditor", tags=["adviser", "education"], body="""
By 1932 Atatürk had reformed the alphabet, the laws and the government and was furious at the
Darülfünun, the old Ottoman university in Istanbul, which he judged conservative and quietly
resistant. He hired Malche to audit it. The report declared the institution hopelessly outdated —
exactly what was wanted — and gave political cover to abolish the entire university in 1933 and fire
two-thirds of its faculty.

The vacuum that created is what allowed Turkey to absorb hundreds of Jewish and dissident German
academics fleeing Hitler. Malche handed over the blueprint for an intellectual purge that doubled as
a rescue operation. See [[1933 University Reform]], [[Philipp Schwartz]], [[Ernst Reuter]].
""")),

("Sabiha Gökçen", dict(role="World's first female combat pilot; adopted daughter of Atatürk", nat="Turkish", life="1913–2001",
  stance="engineered symbol", tags=["turkish", "women", "family", "military"], body="""
To prove women in the new republic were fully equal, Atatürk did not stop at the vote — he engineered
a female warrior. When his adopted daughter showed interest in aviation he enrolled her in the
Turkish Aviation Academy and sent her to the Soviet Union for advanced training.

In 1937 she became the first female combat pilot in world history, and not only in airshows: he
deployed her on live missions in the suppression of the [[Dersim Rebellion]]. A young secular
Westernised woman dropping bombs on conservative tribal rebels was the ultimate manifestation of
Kemalist ideology — modernisation armed and airborne. Compare [[Vecihi Hürkuş]], the aviator the same
state crushed, and [[Afet İnan]], the other adopted daughter built into an instrument.
""")),

("Abdul Hamid II", dict(role="Sultan of the Ottoman Empire", nat="Ottoman", life="1842–1918",
  stance="first jailer", tags=["ottoman", "antagonist"], body="""
Long before the British or the Greeks, Atatürk's first enemy was his own emperor. Abdul Hamid ruled
through a vast secret police network. In 1905 a young captain named Mustafa Kemal, stationed in
Damascus and Istanbul, formed a secret society with fellow officers, reading banned Rousseau and
Voltaire and plotting against the absolute monarchy.

The Sultan's spies infiltrated it. Kemal was arrested, held in the notorious Red Prison and
interrogated for months, then exiled to a remote cavalry regiment in Syria rather than executed. The
stint as a political prisoner under a paranoid theocratic monarch hardened his lifelong conviction
that the dynasty was an archaic institution that had to be destroyed.
""")),

("Zübeyde Hanım", dict(role="Mother of Mustafa Kemal", nat="Ottoman Turkish", life="1857–1923",
  stance="the founding paradox", tags=["family", "personal"], body="""
A woman of the old empire: deeply traditional, fiercely pious, always veiled, praying five times a
day, and set on her son becoming an imam or scholar of Islamic law. He defied her, secretly sitting
the entrance exams for the secular military academy.

Despite that chasm he worshipped her — writing constant affectionate letters throughout the war while
dismantling the institutions she revered, and keeping her safe in Ankara. She died in early 1923,
just before the Republic was proclaimed. Shortly afterwards, standing at her grave in Izmir, over the
tomb of everything traditional and religious about the Ottoman past, he swore a public oath to defend
the secular republic with his life.
""")),

("Mustafa Suphi", dict(role="Founder and chairman of the Communist Party of Turkey", nat="Turkish", life="1883–1921",
  stance="murdered rival", tags=["victim", "communist", "turkish"], body="""
In early 1921, believing the nationalist movement needed proletarian leadership, Suphi and fourteen
members of his central committee travelled from Soviet Russia to Anatolia to join the war. Ankara saw
an internal threat. On arrival in Trabzon they met state-orchestrated mob violence and were forced
onto a boat to be "deported" back to Russia; out on the Black Sea a nationalist captain intercepted
them and all fifteen were murdered and thrown into the sea.

It was never proven that Atatürk ordered it, but the [[Black Sea Incident]] decapitated Turkish
communism and guaranteed the revolution stayed nationalist and state-capitalist. See [[Şefik Hüsnü]].
""")),

("Alexander Parvus", dict(role="Marxist theoretician and financier; born Israel Gelfand", nat="Russian-Jewish", life="1867–1924",
  stance="unlikely economic architect", tags=["theorist", "economics"], body="""
A brilliant, controversial Marxist with a talent for getting rich, who lived in Istanbul for five
years before WWI trading grain and weapons and became a financial adviser to the Young Turks.

His argument: Marxist theory was wrong about the Ottoman Empire. Turkey was being strangled by
European imperialism, and the answer was not a workers' revolution but a strong national bourgeoisie
backed by state power — state-owned railways, factories and banks to break European monopolies. A
decade later that exact framework became [[Devletçilik]], statism, one of the [[Six Arrows]]. The man
who helped fund the Russian Revolution supplied the blueprint for Turkey's explicitly non-Marxist
economy.
""")),

("Alexander I of Yugoslavia", dict(role="King of Yugoslavia", nat="Yugoslav", life="1888–1934",
  stance="ally, assassinated", tags=["ally", "monarch"], body="""
A battle-hardened monarch trying to hold together a volatile multi-ethnic kingdom, and Atatürk's
closest European partner as fascism rose. The two were the twin pillars of the 1934 [[Balkan Pact]]
alongside Greece and Romania, pledging mutual defence against fascist expansion.

In October 1934 he was assassinated in Marseille by a Bulgarian nationalist working with Croatian
fascists. Atatürk was deeply shaken, judging the pact to have lost its strongest anchor and reading
the killing as the opening shot of the coming world war. See [[Nicolae Titulescu]], [[Josip Broz
Tito]].
""")),

("Mehmet Akif Ersoy", dict(role="Poet; author of the Turkish national anthem", nat="Turkish", life="1873–1936",
  stance="ally turned voluntary exile", tags=["turkish", "literary", "conflicted"], body="""
A devout traditional Islamic scholar who rode across Anatolia during the darkest days of the war
preaching in mosques to recruit soldiers. In 1921 he won parliament's competition for a national
anthem with the *İstiklal Marşı* — a soaring religious battle cry invoking the grace of God and the
martyrdom of soldiers. It was adopted unanimously.

Then came secularisation. Horrified by the [[Abolition of the Caliphate]] and the [[Hat Law]], he
went into voluntary exile in Egypt, spending over a decade in Cairo teaching Turkish and translating
the Quran. The standing irony of the republic: a fiercely secular state legally required to stand
each day and sing a deeply religious anthem written by a man who fled the country in protest at its
secularism.
""")),

("Vecihi Hürkuş", dict(role="Fighter pilot and aircraft designer", nat="Turkish", life="1896–1969",
  stance="punished pioneer", tags=["victim", "turkish", "military"], body="""
Shot down Russian planes in WWI, survived a POW camp, became one of the most decorated pilots of the
War of Independence — and was also an engineering talent who wanted Turkey building its own aircraft.
In 1924, scavenging parts from downed enemy planes, he built the first Turkish-made aeroplane, the
Vecihi K-VI.

The new bureaucracy crushed him. Asked for a test-flight permit, the state said it could not license
the plane because nobody was qualified to inspect it. He flew it anyway; they arrested him for flying
without a licence, confiscated the aircraft and fined him heavily. He spent his life fighting a
state-monopolised economy that wanted modernisation but feared individual initiative outside state
control. Contrast [[Sabiha Gökçen]], aviation the state chose to celebrate. See [[Devletçilik]].
""")),

("Mark L. Bristol", dict(role="US High Commissioner in Istanbul", nat="American", life="1868–1939",
  stance="pragmatist", tags=["diplomat", "observer"], body="""
American policy after WWI was shaped by Wilsonian idealism and missionary lobbying, both fiercely
anti-Turkish. Bristol watched the nationalist movement gaining strength in Anatolia and concluded the
European treaties carving up Turkey were fantasies. He fought a years-long bureaucratic war against
his own State Department and the missionary groups, sending blunt reports arguing Atatürk was going
to win and Washington needed to negotiate rather than indulge imperial daydreams. His pragmatism
prevailed and the US normalised relations. See [[James Harbord]], [[Clair Price]].
""")),

("Aubrey Herbert", dict(role="British intelligence officer, MP, 'Lawrence of the Balkans'", nat="British", life="1880–1923",
  stance="ignored prophet", tags=["observer", "diplomat"], body="""
A nearly blind British aristocrat who spoke fluent Turkish and had spent years before WWI travelling
the Ottoman Empire, developing a deep sympathetic understanding of the Turks. During the War of
Independence he tried desperately to warn [[David Lloyd George]] that backing the Greek invasion was
catastrophic, because men like Mustafa Kemal would never surrender. He even went to Germany for a
secret, controversial interview with the exiled [[Enver Pasha]] to untangle the region's politics.

The establishment ignored him, and the [[Chanak Crisis]] and the collapse of the government followed
exactly as he had predicted.
""")),

("Clare Sheridan", dict(role="Sculptor and journalist", nat="British", life="1885–1970",
  stance="advocate", tags=["observer", "women"], body="""
Cousin of [[Winston Churchill]], and already a scandal in London for going to Moscow to sculpt Lenin
and Trotsky. In 1922, with Britain on the brink of war with Turkey, she went to Ankara.

She spent days interviewing and sculpting Atatürk and returned writing glowing articles describing —
against the British press portrait of a bloodthirsty warlord — a brilliant, charismatic statesman with
piercing blue eyes and a razor-sharp intellect. Her pro-Kemalist pieces infuriated the establishment
and her cousin, and helped humanise him to the European public just as the Lausanne negotiations
opened. Compare [[Grace Ellison]].
""")),

("Pyotr Wrangel", dict(role="Commander of the White Army", nat="Russian", life="1878–1928",
  stance="stranded contemporary", tags=["observer", "exile"], body="""
The final commander of the anti-communist White Army. Defeated in Crimea in late 1920, he evacuated
his remaining forces and civilians on over a hundred ships, depositing nearly 150,000 starving
Russians into British-occupied Istanbul.

The resulting overlap is absurd and instructive: Atatürk was secretly taking Lenin's gold to fight
the British, while the British were simultaneously sheltering the remnants of the Tsar's anti-Soviet
army in the old Ottoman capital. Wrangel lived on a yacht in the Bosphorus trying to keep an exiled
army together while the Kemalist revolution ran just across the water — a standing reminder of why
Atatürk played Moscow and London against each other so effectively.
""")),

("Nezihe Muhiddin", dict(role="Feminist organiser", nat="Turkish", life="1889–1958",
  stance="erased pioneer", tags=["victim", "women", "turkish"], body="""
In 1923, before the Republic was fully established, she and a group of women founded the Women's
People Party to demand full political equality. The Kemalist government refused to charter it and
forced her to downgrade it into a non-political "Women's Union."

She kept campaigning, running independent female candidates in local elections to force the
government's hand — and was therefore treated as a political threat. In 1927 the government
orchestrated a smear campaign, raided her organisation and pushed her out of leadership. When full
suffrage arrived in 1934 it came top-down, with the state taking all the credit and the woman who had
led the grassroots fight deliberately written out. See [[Women's Suffrage in Turkey]].
""")),

("Celadet Bedir Khan", dict(role="Kurdish intellectual and linguist", nat="Kurdish", life="1893–1951",
  stance="mirror nationalist", tags=["kurdish", "antagonist", "linguist"], body="""
A Kurdish aristocrat who fled to French-mandate Syria after the Kemalist crackdowns and, watching
from exile, recognised that the [[Alphabet Reform]] was a devastatingly effective instrument for
building a modern national identity.

So he copied it. In Syria he developed a Latin-based alphabet for Kurmanji — the Hawar alphabet — and
published a magazine to standardise the language. The exact modernist linguistic machinery Atatürk
used to forge the "New Turk," redeployed to forge a modern Kurdish identity that would go on to
challenge the Turkish state directly. See [[Ihsan Nuri Pasha]].
""")),

("Nihal Atsız", dict(role="Pan-Turkist ideologue", nat="Turkish", life="1905–1975",
  stance="ultranationalist critic", tags=["antagonist", "nationalist", "turkish"], body="""
Atatürk's nationalism was civic and geographically bounded — a Turk was anyone inside the borders of
the Republic, and foreign conquest was explicitly rejected. To the far right that was cowardice.

Atsız held Turkish identity to be a matter of blood and genetics, not citizenship, and wanted a
racially pure empire uniting Turkic peoples from Anatolia to Central Asia. Through the 1930s and 40s
he attacked the Kemalist state, hated the "Peace at home, peace in the world" doctrine as pacifist
betrayal of Turkey's martial destiny, openly admired Nazi racial policy, and published magazines
attacking the government for employing leftists and non-Turks. The racialised extreme that Atatürk
actively suppressed. Compare [[Enver Pasha]].
""")),

("Dürrüşehvar Sultan", dict(role="Ottoman princess, daughter of the last Caliph", nat="Ottoman / Indian", life="1914–2006",
  stance="displaced royal", tags=["ottoman", "women", "exile"], body="""
Ten years old when the [[Abolition of the Caliphate]] gave her family hours to leave the country. The
imperial family fled to France and lived in near-poverty, stripped of wealth and status.

On the other side of the world, Mir Osman Ali Khan, the Nizam of Hyderabad and reportedly the richest
man alive, saw an opportunity to attach his dynasty to Ottoman prestige, and in 1931 arranged her
marriage to his eldest son Azam Jah. The wedding in France was a global media event. She moved to
India and became a prominent, highly educated advocate for women's rights and healthcare in
Hyderabad — a pen stroke in Ankara sending an Ottoman princess into French exile and out again as a
modernising royal in colonial India. Daughter of [[Abdulmejid II]].
""")),

("Alexander Rüstow", dict(role="Sociologist and economist", nat="German", life="1885–1963",
  stance="exile sheltered by Turkey", tags=["exile", "german-exiles", "economics"], body="""
Fled the Gestapo in 1933 and was granted asylum and a professorship at Istanbul University, where he
lived and taught for fifteen years.

From there he watched [[Devletçilik]] — a heavy, state-planned nationalist economy — with totalitarian
economies in Germany and the USSR on one side and collapsing laissez-faire markets on the other, and
tried to theorise a middle path. In 1938, still based in Istanbul, he took it to the Walter Lippmann
Colloquium in Paris and coined the term **neoliberalism**: free markets plus a state strong enough to
prevent monopolies and ensure social welfare. The intellectual foundation of modern Western
capitalism, conceptualised by a refugee watching the Kemalist state industrialise from scratch.
""")),

("Sergei Yutkevich", dict(role="Film director", nat="Soviet", life="1904–1985",
  stance="hired propagandist", tags=["observer", "communist", "arts"], body="""
For the Republic's 10th anniversary in 1933 Atatürk wanted a cinematic spectacle and Turkey had no
film industry to make one, so he invited the masters of state propaganda. Yutkevich was dispatched
from Moscow and brought the full aesthetic weight of Soviet cinema — sweeping montage, monumental
angles, glorified industry and masses — to direct *Ankara: Heart of Turkey*.

The result is a strange artifact: the visual language of proletarian revolution applied to a fiercely
nationalist capitalist state, with Atatürk featured alongside [[Kliment Voroshilov]]. Foreign tools,
domestic supremacy — the same move as with [[Vladimir Lenin]]'s guns.
""")),

("Agatha Christie", dict(role="Novelist", nat="British", life="1890–1976",
  stance="cultural witness", tags=["observer", "literary"], body="""
A frequent Orient Express passenger between 1926 and 1932, on a line terminating in Istanbul, and so
physically present at the peak of the cultural revolution — watching the fez outlawed overnight,
Arabic script vanish from street signs in favour of Latin letters, and the old imperial capital
dragged into European modernity.

She wrote parts of *Murder on the Orient Express* (1934) in Room 411 of the Pera Palace. The novel
captures exactly that transitional atmosphere: the fading romanticised "Orient" colliding with the
sleek rationalist modernity being enforced on the country.
""")),

("Charles Townshend", dict(role="British general", nat="British", life="1861–1924",
  stance="defeated observer", tags=["former-enemy", "military"], body="""
Commanded the British forces at the disastrous 1916 Siege of Kut al-Amara and surrendered his entire
army to the Ottomans — one of the worst defeats in British military history — then spent the rest of
the war as a high-status prisoner in an island villa near Istanbul.

When the empire collapsed in 1918 he helped negotiate the armistice, believing the Sick Man of Europe
was finally dead and his humiliation avenged. A few years later he watched from Europe as a young
Ottoman officer resurrected the Turkish military and shattered the British-backed Greek army — living
just long enough to see that the empire's death had accidentally produced something far more unified
and harder to beat.
""")),

("Ali Kemal", dict(role="Ottoman liberal journalist and Interior Minister", nat="Ottoman Turkish", life="1867–1922",
  stance="domestic enemy, lynched", tags=["antagonist", "victim", "turkish"], body="""
A brilliant journalist and briefly Interior Minister for the Sultan's government, who despised the
nationalist movement and argued the only survival route was peaceful diplomacy and submission to a
British mandate. In his paper he attacked Atatürk and called the nationalist army a band of reckless
thugs who would bring final destruction on Turkey.

He bet wrong. After the 1922 victory he was kidnapped from an Istanbul barbershop by nationalist
sympathisers, intended for a treason trial in Ankara. General Nureddin Pasha intercepted the convoy
and orchestrated a mob that lynched him in the street, hanging his body from a railway bridge.

**The irony:** his descendants fled to the United Kingdom — the empire he had wanted Turkey to submit
to. His great-grandson, Boris Johnson, became its Prime Minister.
""")),

("Philipp Schwartz", dict(role="Professor of pathology; organiser of the academic rescue", nat="Jewish-Hungarian/Austrian", life="1894–1977",
  stance="rescue architect", tags=["exile", "german-exiles", "science"], body="""
Fired from Goethe University Frankfurt the moment Hitler took power in 1933. Recognising what was
coming for Jewish academics, he fled to Switzerland and founded the Emergency Committee of German
Scientists Abroad.

While other countries were closing their doors he travelled quietly to Ankara and met a Kemalist
government desperate for modern scientific minds to staff its new secular universities. He negotiated
a historic deal, personally securing visas and academic appointments for hundreds of Europe's most
brilliant Jewish and anti-fascist scholars and physicians. They built modern Turkey's medical and
scientific infrastructure from scratch, and the republic served as a sanctuary from the Holocaust.
See [[1933 University Reform]], [[Albert Malche]], [[Albert Einstein]].
""")),

("Ahmed al-Senussi", dict(role="Grand Sheikh of the Senussi Sufi order", nat="Libyan", life="1873–1933",
  stance="ally, discarded", tags=["religious", "victim"], body="""
During the darkest days of the war the Sultan issued a fatwa declaring Atatürk an apostate who must
be killed, and Atatürk urgently needed religious legitimacy of his own. He found it in al-Senussi, a
holy warrior of immense prestige across the Islamic world who had fought Italian and British
imperialists.

Invited to Ankara in 1921, al-Senussi travelled Anatolia preaching in mosques, rallying conservative
peasants to the army by framing the war as a jihad to save the Caliphate. He was highly effective.
The moment the war was won, the secular agenda emerged: the Caliphate abolished, religious orders
suppressed, and the sheikh who had supplied the spiritual cover quietly forced into exile. He died in
Saudi Arabia.
""")),

("Henry Ford", dict(role="Industrialist", nat="American", life="1863–1947",
  stance="industrial idol", tags=["influence", "economics"], body="""
Atatürk was as interested in American industrial efficiency as in European law, seeing "Fordism" —
mass production of machinery and tractors — as the weapon to drag the Anatolian peasant out of the
Middle Ages. Through the 1920s his government courted the Ford Motor Company, and in 1929 struck a
deal for an assembly plant in Tophane, Istanbul, one of the first free-trade zones in Turkish
history. The two exchanged admiring correspondence and Atatürk bought Ford tractors for his own model
farms in Ankara. While European intellectuals debated the philosophy of the republic, he was looking
at Detroit. See [[Devletçilik]].
""")),

("Afet İnan", dict(role="Historian; adopted daughter of Atatürk", nat="Turkish", life="1908–1985",
  stance="engineered academic", tags=["turkish", "family", "women"], body="""
Atatürk wanted to rewrite Turkey's past as well as its future, and rather than rely on established
academics he built one. Under his direct patronage she was sent to Geneva to study sociology and
history through to a doctorate, then returned as the primary academic vehicle for the [[Turkish
History Thesis]] — the state theory that ancient Turks founded Sumerian, Hittite and Egyptian
civilisation and that Turkish was the root of all human language.

She became a towering figure in the new academic establishment, publishing and chairing historical
congresses to enforce the narrative. A clean illustration of the project's depth: he used his own
family to engineer a new historical consciousness. Compare [[Sabiha Gökçen]].
""")),

("Fikriye Hanım", dict(role="Companion of Atatürk during the War of Independence", nat="Turkish", life="d. 1924",
  stance="personal casualty", tags=["personal", "victim", "women"], body="""
During the hardest days of the war she lived with him in Ankara, managing his household and serving
as his closest confidante, and was deeply in love with him. She had severe tuberculosis, and as the
war ended he sent her to a sanatorium in Munich.

While she was in Europe he abruptly married [[Latife Uşşaki]]. Devastated, she ignored her doctors,
fled the sanatorium and travelled back to Ankara to see him. At the gates of the Çankaya mansion
Latife reportedly ordered the guards to refuse her entry. Turned away, she drew a pistol and shot
herself. Her death remains one of the most heavily censored personal shadows over the founding of the
republic.
""")),

("Nikolaos Trikoupis", dict(role="Commander-in-Chief of Greek forces in Anatolia", nat="Greek", life="1868–1956",
  stance="captured enemy, treated with chivalry", tags=["former-enemy", "military"], body="""
Captured by Turkish cavalry at the decisive Battle of Dumlupınar in 1922 and brought to Atatürk's
command tent expecting humiliation or summary execution after a war of atrocities on both sides.
Instead Atatürk stood, shook his hand and offered him a cigarette.

*"Sit down, General, you must be tired… War is a game of chance. The best of generals can sometimes
be defeated. You did your duty fully; the responsibility rests with destiny. Do not be sorrowful."*
He then informed Trikoupis of something the Greek did not know, his communications having been cut:
Athens had promoted him to Commander-in-Chief days earlier. Treated as a high-status prisoner and
eventually returned to Greece, he reportedly sent a wreath to Atatürk's funeral.
""")),

("Halet Çambel", dict(role="Archaeologist and Olympic fencer", nat="Turkish", life="1916–2014",
  stance="the republic's answer to Hitler", tags=["turkish", "women", "nazi-thread"], body="""
In 1936 she and her teammate Suat Fetgeri Aşeni became the first Muslim women to compete in the
Olympic Games, in Berlin — living products of the secular modernising revolution.

During the games a German official offered to introduce her to Adolf Hitler. She refused outright,
saying later she would never shake the hand of a dictator who stood against the enlightened humanist
values she believed the new Turkish Republic represented. The closing symmetry of this whole
transcript: while [[Adolf Hitler]] was admiring Atatürk's ethnic state-building from a distance,
Atatürk's own state-sponsored female athletes were refusing to meet him. She went on to a major
archaeological career. See [[Charles H. Sherrill]].
""")),

("Carlo Sforza", dict(role="Italian High Commissioner in Istanbul", nat="Italian", life="1872–1952",
  stance="pragmatic defector", tags=["diplomat", "observer"], body="""
Italy had been promised a large chunk of southwestern Anatolia. Sforza looked at the mobilising
nationalist forces and concluded, while the British and French were still treating the Turks as a
dying race, that European imperialism in Turkey was finished.

Defying the British, he opened secret channels with Atatürk, quietly pulled Italian troops out of
Anatolia without a fight, and allowed the nationalists to buy — and sometimes simply take — Italian
weapons and ammunition for use against the Greeks. His defection broke the united Allied front before
the war was even over: proof that Atatürk's most useful weapon was often the fractured greed of the
Europeans. Compare [[Franklin Bouillon]].
""")),

("İsmet İnönü", dict(role="Prime Minister; second President of Turkey", nat="Turkish", life="1884–1973",
  stance="closest ally and successor", tags=["turkish", "inner-circle", "successor"], body="""
Atatürk's closest friend, chief negotiator and eventual successor — and his temperamental opposite.
Atatürk was a manic chain-smoking visionary who stayed up until dawn drinking and philosophising;
İnönü was a cold, sober, calculating bureaucrat who went to bed early and despised chaos. Atatürk was
the architect; İnönü was the general contractor who actually built the state.

At Lausanne he reportedly used his partial deafness to simply not hear [[Lord Curzon]]'s threats,
refusing anything less than full sovereignty ([[Treaty of Lausanne]]). The relationship frayed badly
in the final years as the drinking worsened, and Atatürk dismissed him as Prime Minister in 1937 —
yet on Atatürk's death in 1938 the state universally recognised only İnönü could hold the country
together.

He took over as WWII erupted and spent six years playing Nazi Germany, the Soviet Union and Britain
against each other, keeping Turkey out of the deadliest war in history. He preserved the republic; he
just had to do it in the shadow of a man larger than life.
""")),

("Fridtjof Nansen", dict(role="Polar explorer, League of Nations diplomat", nat="Norwegian", life="1861–1930",
  stance="demographic engineer", tags=["diplomat", "observer"], body="""
The League tasked the famous explorer-turned-diplomat with solving the refugee crisis created by the
Turkish victory. His conclusion was that as long as ethnic minorities remained on the "wrong" side of
the borders the two nations would fight again.

His solution was the 1923 [[Greco-Turkish Population Exchange]]: an unprecedented demographic swap
sorted entirely by religion, expelling over 1.2 million Greek Orthodox Christians to Greece and
around 400,000 Muslims to Turkey. Traumatic and devastating for communities that had lived together
for centuries — and accepted by both Atatürk and Athens. It permanently homogenised both states and
ended the territorial wars by physically removing the populations being fought over.
""")),

("Bruno Taut", dict(role="Modernist architect", nat="German-Jewish", life="1880–1938",
  stance="exile sheltered by Turkey", tags=["exile", "german-exiles", "builder"], body="""
A world-renowned modernist who fled Nazi Germany first to Japan and then, in 1936, to Turkey, where
he headed the architecture department at the Academy of Fine Arts in Istanbul and designed major
educational buildings blending European modernism with Turkish motifs.

When Atatürk died in November 1938 the government needed someone to design the catafalque for the
state funeral — and chose not a Turkish architect but the German-Jewish refugee. Severely asthmatic,
Taut poured his remaining strength into the monumental design and died a month after Atatürk. He was
granted an unprecedented honour: the only non-Muslim buried in Edirnekapı Martyrs' Cemetery. See
[[Clemens Holzmeister]], [[Anıtkabir]].
""")),

("Enver Pasha", dict(role="Ottoman Minister of War, one of the Three Pashas", nat="Ottoman Turkish", life="1881–1922",
  stance="rival, boxed out", tags=["ottoman", "antagonist", "military"], body="""
The charismatic imperial romantic who dreamed of a Pan-Turkic empire running from Istanbul to Central
Asia — the exact opposite of what Atatürk built. After the 1918 defeat he fled to Germany, then
Soviet Russia, and watched from exile with burning jealousy as Atatürk fought a deliberately
defensive, realistic war for Anatolia's borders alone.

He repeatedly tried to undermine him and swoop back to take control of the nationalist movement, and
Atatürk — knowing him for a reckless imperialist — boxed him out completely. Unable to win
politically, Enver went to Central Asia to lead a cavalry rebellion against the Bolsheviks and carve
his empire by force, and was killed in a suicidal charge against the Red Army in 1922 — the same year
Atatürk secured Turkey's modern borders by pragmatic statecraft. See [[Talat Pasha]], [[Nihal
Atsız]], [[Aubrey Herbert]].
""")),
]

for name, kw in P:
    person(name, **kw)
print(f"batch4: {len(P)} people")
