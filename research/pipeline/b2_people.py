# -*- coding: utf-8 -*-
from _lib import person

P = [
("Marcus Garvey", dict(role="Founder of the Pan-African movement", nat="Jamaican", life="1887–1940",
  stance="admirer", tags=["admirer", "anti-colonial"], body="""
In the 1920s white global supremacy was practically unquestioned in the West. Garvey used *The Negro
World* to celebrate Atatürk — not out of any interest in Turkish domestic policy, but because a
non-white, non-Christian nation had met the British and French empires on the battlefield and won. He
pointed to Ankara to argue that European invincibility was a myth, urging people of African descent
toward the same uncompromising militancy.
""")),

("W.E.B. Du Bois", dict(role="Sociologist and civil rights leader", nat="American", life="1868–1963",
  stance="observer / admirer", tags=["admirer", "observer"], body="""
Wrote about the Kemalist victory in his work on the "awakening of the East," placing Atatürk
alongside leaders in Japan and India as evidence that the global colour line and European colonial
hegemony were beginning to fracture. Compare [[Marcus Garvey]], who drew the militant lesson from the
same event.
""")),

("Sinn Féin and the IRA", dict(role="Irish republican movement", nat="Irish", life="1919–1922 context",
  stance="partisan observers", tags=["movement", "anti-colonial"], body="""
Irish republicans were fighting the same empire at the same moment, and the nationalist press
followed the [[Turkish War of Independence]] with intense partisan interest. The [[Chanak Crisis]] of
1922 — Britain forced to back down and rewrite the [[Treaty of Sèvres]] — was read as a masterclass.
*An Phoblacht* drew direct parallels between the two struggles: proof that the British Empire was
overextended and could be beaten by a movement willing to fight a grinding war of attrition.
""")),

("Ernest Hemingway", dict(role="Novelist; then a 23-year-old foreign correspondent", nat="American", life="1899–1961",
  stance="witness", tags=["observer", "literary"], body="""
Covered the [[Greco-Turkish War]] for the *Toronto Star* in 1922 and was physically present for the
chaotic aftermath of the victory. His writing is haunted by the suffering of the refugee columns, but
he reported the geopolitical earthquake with stark awe: Atatürk had upended the calculus of the
Western powers, and the shock in Europe was the realisation that the "Turk" they had buried had risen
to dictate terms. Compare [[Aristotle Onassis]], who lived the other side of the same weeks.
""")),

("Gamal Abdel Nasser", dict(role="President of Egypt", nat="Egyptian", life="1918–1970",
  stance="imitator", tags=["imitator", "anti-colonial"], body="""
While conservative Arabs disliked the secularism, a generation of Arab officers looked at their own
corrupt British-backed monarchies and wanted a "Turkish solution." Nasser and the Free Officers
overthrew King Farouk in 1952 on a blueprint heavily indebted to [[Kemalism]]: the military as
vanguard of the state, aggressive secularisation of public institutions, seizure of national assets
from foreign powers. The divergence: Nasser's project leaned into Arab socialism rather than Turkish
nationalism. Compare [[Sati' al-Husri]], who supplied the theory.

(Source check, Nov 2026: this is an analytical comparison inherited from the transcript, not Nasser's own
words. His *Philosophy of the Revolution* (1954) never names Kemal or Atatürk, and no Nasser statement on
Atatürk has been found yet.)
""")),

("Charles de Gaulle", dict(role="Leader of Free France, founder of the Fifth Republic", nat="French", life="1890–1970",
  stance="kindred spirit", tags=["admirer", "state-builder"], body="""
Both were military officers who refused to accept their nations' defeat (France 1940, Turkey 1918),
defied their own governments, rallied resistance from nothing, and created new republics under strong
executive power. On a state visit in 1968 de Gaulle laid a wreath at [[Anıtkabir]] and praised
Atatürk not as a conqueror but as the architect of a sovereign destiny — recognising the exact
uncompromising nationalism he claimed for France.
""")),

("Kliment Voroshilov", dict(role="Marshal of the Soviet Union", nat="Soviet", life="1881–1969",
  stance="ally, memorialised", tags=["ally", "communist"], body="""
Instrumental in facilitating the gold and weapons [[Vladimir Lenin]] sent to Ankara in the early
1920s. The mutual respect between the Turkish and Soviet commands ran deep enough that Atatürk had
Voroshilov's likeness carved into the [[Republic Monument]] in Taksim Square, unveiled 1928 — so a
high-ranking Soviet commander still stands permanently behind Atatürk in the heart of a major NATO
country. See also [[Mikhail Frunze]], [[Sergei Yutkevich]].
""")),

("Ōkawa Shūmei", dict(role="Pan-Asianist theorist", nat="Japanese", life="1886–1957",
  stance="promoter", tags=["admirer", "nationalist"], body="""
Japanese intellectuals and imperial theorists aggressively promoted Atatürk's story at home. Japan
had shocked the world by beating Russia in 1905; Turkey's 1922 victory over the British and French
read as ultimate vindication of the pan-Asianist worldview — proof the "Eastern" world could eject
Western powers if it adopted Western military science and industrial discipline. See [[Prince
Takamatsu]].
""")),

("Sati' al-Husri", dict(role="Intellectual father of Arab nationalism", nat="Syrian-born Ottoman", life="1880–1968",
  stance="ideological borrower", tags=["imitator", "theorist"], body="""
The central irony of modern Middle Eastern history: secular Arab nationalism was largely adapted from
the man who abolished the Ottoman Empire. A former Ottoman official, al-Husri watched Atatürk replace
a multi-ethnic religious empire with a state grounded purely in language, history and ethnicity — and
copied the homework. His framework for a unified Arab state argued that Arabs must unite on Arabic
language and shared history, explicitly rejecting Islamic solidarity as a failed, outdated concept.
That framework eventually drove the Ba'ath parties in Syria and Iraq. Compare [[Gamal Abdel Nasser]],
[[Antoun Saadeh]], [[Amin al-Rihani]].
""")),

("Arnold J. Toynbee", dict(role="Historian", nat="British", life="1889–1975",
  stance="propagandist turned advocate", tags=["observer", "convert"], body="""
During WWI he was one of Britain's most effective anti-Ottoman propagandists, co-authoring for the
Political Intelligence Department the Blue Book documenting the [[Armenian Genocide]], used to
justify dismantling the empire.

Then in 1921 he went to Anatolia for the *Manchester Guardian*. Witnessing the discipline of the
nationalist forces and the atrocities of the Greek army produced a total paradigm shift. He
wrote *The Western Question in Greece and Turkey* (1922), breaking completely with British policy.
The reversal was controversial enough to cost him his professorship at King's College London.

*Correction (Oct 2026): the transcript said he interviewed Atatürk. His own book says the
opposite: "Though I have not met Mustafa Kemal Pasha in the flesh, I can certify that…" (1922).
See [[Toynbee on the Audacious Rebel, 1922]].*
""")),

("Benito Mussolini", dict(role="Fascist dictator of Italy", nat="Italian", life="1883–1945",
  stance="admirer, rebuffed; then existential threat", tags=["antagonist", "admirer"], body="""
An early and vocal admirer: before the 1922 March on Rome he watched Ankara closely and read the
Turkish military's takeover and violent ejection of foreign powers as a proto-fascist triumph of
national will over weak democratic diplomacy.

The admiration was entirely one-sided. Atatürk regarded him as a dangerous megalomaniac whose
Mediterranean ambitions directly threatened Turkish sovereignty — Italy already held the Dodecanese a
few miles off the coast. When the Italian ambassador hinted at territorial concessions in southern
Anatolia, Atatürk reportedly left the room, returned in full field marshal's uniform, and told him to
inform Rome that if Mussolini wanted Anatolia he could come and try. Fear of Mussolini was the
primary driver of the [[Balkan Pact]] and of the late-1930s rapprochement with Britain and France.
See [[Ioannis Metaxas]], [[Nicolae Titulescu]], [[Adolf Hitler]].
""")),

("Ho Chi Minh", dict(role="Vietnamese revolutionary leader", nat="Vietnamese", life="1890–1969",
  stance="student", tags=["admirer", "anti-colonial", "communist"], body="""
As a young man in early-1920s Paris writing for the anti-colonial paper *Le Paria*, he wrote several
articles meticulously analysing Atatürk's victories over the French and British in Anatolia. For him
the [[Turkish War of Independence]] was not a distant Middle Eastern conflict but proof of concept
for Indochina: the French military was not invincible, and a disciplined nationalist army could bleed
a colonial power until it went home.
""")),

("Nicolae Titulescu", dict(role="Romanian diplomat, two-time President of the League of Nations", nat="Romanian", life="1882–1941",
  stance="ally", tags=["ally", "diplomat"], body="""
Believed the only way to stop a second world war was a wall of regional alliances, and found his
strongest partner in Atatürk. Together they architected the 1934 [[Balkan Pact]] — Turkey, Romania,
Greece, Yugoslavia — against Mussolini and Hitler. He publicly revered Atatürk as the greatest
statesman in Europe; on his death in 1938 he said the world had lost the only man who understood how
to stabilise the East, and predicted the Balkans would now collapse into the coming war. They did.
""")),

("Plutarco Elías Calles", dict(role="President of Mexico", nat="Mexican", life="1877–1945",
  stance="parallel secularizer", tags=["parallel", "secularist"], body="""
Mexico and Turkey ran the two most aggressive state secularisation programmes in the world
simultaneously. A fiercely anti-clerical former general, Calles stripped the Catholic Church of
power, wealth and its educational monopoly — igniting the Cristero War — while monitoring Atatürk's
dismantling of the Caliphate and religious courts. The Mexican press cited the Kemalist revolution as
proof that a modern republic must break clerical political power to survive. Both generals saw
organised religion as a parasitic force keeping peasants backward and loyal to foreign powers: the
Vatican for Calles, the clerics and outside patrons for Atatürk.
""")),

("John Dewey", dict(role="Philosopher and educational reformer", nat="American", life="1859–1952",
  stance="invited architect", tags=["adviser", "education"], body="""
Invited personally to Turkey in 1924, immediately after the [[Abolition of the Caliphate]], to
redesign the national school system from the ground up. He spent months travelling Anatolia,
astounded by the sheer political will of the Kemalists and treating Turkey as a real-world laboratory
for progressive education.

His report argued for practical, secular, vocational schooling over rote memorisation — teaching
peasants to farm better, build infrastructure and participate civically — and became the foundational
blueprint of Turkish secular education and, later, the [[Village Institutes]]. His two 1924 *New
Republic* articles praise "the new leaders" of Angora but never name Mustafa Kemal (checked in census
round 14; the transcript's claim that he praised Atatürk by name is unsupported).
Compare [[John F. Kennedy]]'s 1963 framing.
""")),

("H.G. Wells", dict(role="Novelist and historian", nat="British", life="1866–1946",
  stance="mutual admiration", tags=["admirer", "literary"], body="""
An advocate of a secular world state guided by science and reason. Atatürk had *The Outline of
History* translated into Turkish, read it obsessively, and drew on it in formulating the [[Turkish
History Thesis]]. Wells reciprocated, treating the abolition of the Caliphate and forced
secularisation as a monumental triumph of rationalism over dogma and citing Turkey as a vanguard
state.
""")),

("Josip Broz Tito", dict(role="Founder and leader of Yugoslavia", nat="Yugoslav", life="1892–1980",
  stance="admirer / parallel", tags=["admirer", "state-builder", "communist"], body="""
Faced Atatürk's exact problem: forging one sovereign nation from a fractured, multi-ethnic,
multi-religious territory formerly ruled by empires. He expressed deep admiration and studied the
method closely — a highly disciplined military, a unifying national myth, strict secularism binding a
diverse population. He also replicated the independent line, defying Stalin as Atatürk had defied the
British, holding a volatile region together on force of will and personal charisma. See [[Alexander I
of Yugoslavia]].
""")),

("Yiannis Ritsos", dict(role="Poet", nat="Greek", life="1909–1990",
  stance="ideological admirer", tags=["admirer", "literary", "communist"], body="""
A committed communist persecuted at home who, despite the traumatic Greek-Turkish history, viewed
Atatürk through pure anti-imperialist solidarity. He translated [[Nâzım Hikmet]] into Greek, bridging
a vast cultural divide. He and the Greek radical left quietly respected the Kemalist revolution as a
successful violent rejection of Western capitalist imperialism — even though Atatürk was a staunch
nationalist who jailed communists. Compare [[Eleftherios Venizelos]], who reached the same peace by
the opposite route.
""")),

("B.R. Ambedkar", dict(role="Chief architect of India's Constitution", nat="Indian", life="1891–1956",
  stance="legal admirer", tags=["admirer", "reformer"], body="""
Born Dalit, he spent his life dismantling the legal scaffolding of caste. Where [[Mahatma Gandhi]] and
[[Subhas Chandra Bose]] read Atatürk through anti-imperialism, Ambedkar read him through law: the
[[Abolition of the Caliphate]] and the replacement of Sharia courts with the [[Turkish Civil Code]]
proved a modern state had both the right and the duty to forcibly eradicate oppressive religious law.
Drafting the Hindu Code Bill — modernising civil law, granting women equal inheritance — he pointed
repeatedly to Turkey to argue that real democracy required total separation of religious dogma from
state law. Compare [[Periyar E. V. Ramasamy]].
""")),

("King Zog I", dict(role="King of Albania", nat="Albanian", life="1895–1961",
  stance="imitator (flawed)", tags=["imitator", "monarch"], body="""
Mimicked the cultural decrees closely — banned the veil, outlawed the fez, forced European dress,
instituted a secular civil code — while doing the structural opposite: where Atatürk abolished the
monarchy for a republic, Zog declared himself King in 1928. Without grassroots legitimacy or a
battle-tested military apparatus the reforms stayed fragile and met sustained tribal resistance. One
of the purest cases of copying the aesthetics without the foundations. Compare [[Plaek
Phibunsongkhram]].
""")),

("Grace Ellison", dict(role="Writer and women's rights advocate", nat="British", life="1877–1935",
  stance="advocate", tags=["observer", "women"], body="""
The British press painted the nationalists as fanatics and warlords. Ellison defied her own
government, travelled to Ankara in 1922, and secured extensive interviews with Atatürk and the
Kemalist leadership. *An Englishwoman in Angora* shocked British readers with an account of a
brilliant secular modernizer actively planning the emancipation of Turkish women. Her writing helped
shift Western opinion and forced London to recognise it was fighting a legitimate progressive
national movement. Compare [[Clare Sheridan]], [[Clair Price]].
""")),

("Taha Hussein", dict(role="Writer, 'Dean of Arabic Literature'", nat="Egyptian", life="1889–1973",
  stance="admirer", tags=["admirer", "literary"], body="""
Argued Egypt's future lay not with the conservative traditionalist Arab world but with the
"Mediterranean" sphere of Western rationalism, and cited Atatürk's cultural revolution as the
definitive model: proof that a nation with Islamic heritage could strip away centuries of religious
stagnation, adopt Western scientific thought and radically reform its education system without losing
itself. Compare [[Amin al-Rihani]].
""")),

("King Edward VIII", dict(role="King of the United Kingdom", nat="British", life="1894–1972",
  stance="reconciled monarch", tags=["monarch", "diplomatic"], body="""
In 1936 he took a Mediterranean cruise and specifically requested a stop in Istanbul. Fourteen years
earlier British warships had their guns trained on that city during the [[Chanak Crisis]]. Atatürk
went to the docks personally and physically helped the King out of his boat; they spent days touring
and discussing European diplomacy, and Edward was reportedly completely charmed. A significant
diplomatic coup — formally ending post-WWI hostility and cementing the UK-Turkey alignment that held
as WWII approached. See [[Percy Loraine]].
""")),

("T.E. Lawrence", dict(role="British officer, 'Lawrence of Arabia'", nat="British", life="1888–1935",
  stance="adversary turned admirer", tags=["admirer", "former-enemy"], body="""
He had spent years on a guerrilla campaign to shatter Ottoman control of the Middle East, so the
revival of Turkish power should have read as the undoing of his life's work. Instead he recognised
the military and political genius: the Ottoman Empire was corrupt and doomed, but the new republic
was a legitimate, vital national movement. In the late 1920s he reportedly told his biographer [[B.H.
Liddell Hart]] that Mustafa Kemal was one of the greatest leaders of the era, and allegedly offered to
travel to Turkey on a diplomatic mission — seeing him as the only statesman in the region operating
on strategic reality rather than imperial fantasy. Fought alongside [[Faisal I of Iraq]] and [[Hussein
bin Ali]].
""")),

("Antoine de Saint-Exupéry", dict(role="Aviator and author", nat="French", life="1900–1944",
  stance="cultural witness", tags=["literary", "observer"], body="""
The most widely read reference to Kemalist reform hides in *The Little Prince*. Asteroid B-612 is
discovered in 1909 by a Turkish astronomer whose findings the International Astronomical Congress
ignores because he wears Ottoman robes. Then: *"Fortunately… a Turkish dictator made a law that his
subjects, under pain of death, should change to European costume."* He returns in 1920 in an elegant
Western suit and the Congress accepts the discovery.

A direct reference to the [[Hat Law]] and the clothing reforms. The tone gently satirises European
superficiality, but it cemented Atatürk's cultural revolution into global pop culture — and records
how shocking the forced Westernisation looked from outside.
""")),

("Plaek Phibunsongkhram", dict(role="Prime Minister of Thailand", nat="Thai", life="1897–1964",
  stance="imitator", tags=["imitator", "nationalist"], body="""
After the 1932 revolution stripped the Siamese absolute monarchy of power, Phibun launched a cultural
revolution explicitly modelled on [[Kemalism]]. His "Cultural Mandates" made Western dress compulsory
— barring people from public transport without hats and shoes — reformed the Thai language, and
changed the country's name from Siam to Thailand to promote an ethno-nationalist identity. The
Atatürk playbook applied to force a highly traditional society into a modernised militarised mould.
""")),

("Józef Piłsudski", dict(role="Founding father of the Second Polish Republic", nat="Polish", life="1867–1935",
  stance="kindred state-builder", tags=["ally", "state-builder"], body="""
Like Atatürk, a military commander who forged a nation from the wreckage of WWI and immediately had
to fight a brutal war (against the Soviets) to secure its borders. Both were authoritarian modernizers
whose countries sat between hostile empires — Germany and the USSR for Poland; the Soviets and the
Anglo-French Mediterranean fleets for Turkey. Warm ties came easily, helped by the fact that the
Ottoman Empire had been the only major power never to recognise the partition of Poland, keeping a
symbolic empty chair for a Polish ambassador for over a century. Each saw the other as a bulwark
against Soviet expansion.
""")),

("Emil Ludwig", dict(role="Biographer", nat="German-Jewish", life="1881–1948",
  stance="interviewer", tags=["observer", "literary"], body="""
The most famous biographer in the world in the 1920s–30s, with exclusive interviews of Stalin and
Mussolini to his name. He interviewed Atatürk in 1930 and was astounded by his total lack of
religious or historical sentimentality. He compared him to Napoleon with one key difference: Napoleon
was consumed by imperial hubris, while Atatürk knew exactly where to stop. Ludwig described a
terrifying, Nietzschean willpower directed entirely at rational domestic state-building rather than
foreign conquest — a ruthless dictator using absolute power to force a nation toward secularism,
science and the Enlightenment. Compare [[W.B. Yeats]], who reached a similar reading through
mysticism.
""")),

("David Lloyd George", dict(role="Prime Minister of the United Kingdom", nat="British (Welsh)", life="1863–1945",
  stance="arch-nemesis", tags=["antagonist", "former-enemy"], body="""
The man most responsible for trying to wipe Turkey off the map of Europe: a staunch Philhellene who
heavily backed the Greek invasion of Anatolia. His grand strategy was shattered when the Turkish army
routed the Greeks and marched on Chanak, and the British public and military refused another war. The
[[Chanak Crisis]] collapsed his coalition government and ended his career; he never held power again.

Even in defeat he recognised the scale of what beat him — but the famous concession attributed to
him, *"Humanity rarely produces a genius in centuries. It is our bad luck that the great genius of our
era was granted to the Turkish nation,"* has no trace in Hansard, and Parliament was in recess in the
window where the scene is usually set. Its traceable life begins in Turkish popular history (an ATAM
journal article, then Turgut Özakman's *Şu Çılgın Türkler*, then the *Kurtuluş* TV series) — a
perfect specimen of the apocrypha-as-data tier. [[Aubrey Herbert]] had warned him exactly what was
coming at Chanak.
""")),

("Mahatma Gandhi", dict(role="Leader of the Indian independence movement", nat="Indian", life="1869–1948",
  stance="conflicted; ultimately alienated", tags=["conflicted"], body="""
His relationship with the Kemalist legacy runs through the [[Khilafat Movement]]: in the early 1920s
he allied with Indian Muslims protesting the British dismantling of the Caliphate, using it to forge
Hindu-Muslim unity against British rule, and heavily praised "Kemal Pasha" for his bravery and
rejection of British imperialism.

Then in 1924 Atatürk abolished the Caliphate himself, in the name of secularism, and Gandhi was
politically blindsided. A pacifist who believed religion and politics were inseparable, he was deeply
unsettled by the ruthless secular militarism. He continued to respect the man who broke the spell of
European invincibility while treating him as a cautionary tale of a leader who chose the sword over
spiritual truth. His antagonist [[Subhas Chandra Bose]] drew precisely the opposite conclusion.
""")),

("Sayyid Qutb", dict(role="Ideologue of the Muslim Brotherhood", nat="Egyptian", life="1906–1966",
  stance="reactionary anti-admirer", tags=["antagonist", "islamist"], body="""
Built his radical ideology as a direct reactionary response to [[Kemalism]]. The 1924 [[Abolition of
the Caliphate]] and the stripping of Islamic law from the Turkish constitution were, to him, the most
catastrophic and humiliating events in modern Islamic history. He wrote extensively on the "poison"
of Western secular nationalism injected into the Muslim world. His entire political project — a state
governed strictly by religious law — was designed to reverse the Kemalist template. See [[Ruhollah
Khomeini]], [[Mustafa Sabri Efendi]], [[Said Nursi]].
""")),

("Ruhollah Khomeini", dict(role="Founder of the Islamic Republic of Iran", nat="Iranian", life="1902–1989",
  stance="reactionary anti-admirer", tags=["antagonist", "islamist"], body="""
The other pole of the anti-Kemalist reaction alongside [[Sayyid Qutb]]. He read the abolition of the
Caliphate and the secularisation of Turkish law as civilisational catastrophe, and built a state
designed to ensure no secular dictator could ever again dismantle religious authority. Note the local
irony: the Iranian revolution he led was a delayed backlash against [[Reza Shah Pahlavi]]'s attempt to
import Kemalism.
""")),

("Mao Zedong", dict(role="Leader of the Chinese Communist Party", nat="Chinese", life="1893–1976",
  stance="student, then explicit rejecter", tags=["observer", "communist"], body="""
Studied the [[Turkish War of Independence]] closely during the Long March, fascinated by the strategy
of abandoning the corrupt occupied capital, retreating into the rugged heartland and building a
revolutionary army from the peasantry.

The admiration had a hard limit. In "On New Democracy" (January 1940) he asked "where is China's
Kemal?" and dismissed the "petty Kemalist dictatorship of the bourgeoisie" — see [[Interwar Leaders on
Kemal in Their Own Words]]. (Source check, Nov 2026: the often-quoted line to Edgar Snow in 1936, "We are
not going to be another Kemal Turkey", has no source found yet.) He respected the ejection of foreign imperialists but condemned [[Kemalism]] as a bourgeois
dictatorship — Atatürk had allied with the military and capitalist classes instead of making a
proletarian revolution, so Turkey would inevitably fall back under Western economic control. His
enemy [[Chiang Kai-shek]] studied the same case and copied it.
""")),

("Charles H. Sherrill", dict(role="Olympic sprinter, IOC member, US Ambassador to Turkey", nat="American", life="1867–1936",
  stance="admirer / biographer", tags=["admirer", "diplomat"], body="""
Obsessed with physical vitality, discipline and national energy, he interviewed Atatürk for hours as
ambassador from 1932 and wrote the glowing, widely read *A Year's Embassy to Mustafa Kemal*. Viewing
the world through sport, he praised the drive to modernise Turkish youth through state athletics and
physical education, and tried to recruit Turkey into the international sporting community — casting
Atatürk as the ultimate coach who whipped an exhausted nation back into fighting shape. See [[Halet
Çambel]].
""")),

("Eleanor Roosevelt", dict(role="Human rights advocate, US First Lady", nat="American", life="1884–1962",
  stance="admirer (women's rights)", tags=["admirer", "women"], body="""
Central to drafting the UN Universal Declaration of Human Rights, she often reflected on the sheer
speed of the Kemalist cultural revolution. American and European women fought decades-long
generational battles against their own democratic governments for the vote; Atatürk simply mandated
it from the top. She noted that by the mid-1930s Turkey had women serving as judges, doctors and
members of parliament — an embarrassment to Western politicians still arguing women were unfit for
public life. See [[Women's Suffrage in Turkey]], [[Huda Sha'arawi]], [[Nezihe Muhiddin]].
""")),

("Ioannis Metaxas", dict(role="Fascist dictator of Greece", nat="Greek", life="1871–1941",
  stance="pragmatic ally", tags=["ally", "former-enemy"], body="""
Seized power in 1936, fourteen years after the [[Greco-Turkish War]] — and instead of stoking
anti-Turkish hatred, built a warm, deeply pragmatic alliance. Both were authoritarian modernizers
terrified of [[Benito Mussolini]]'s Mediterranean ambitions, and they reinforced the [[Balkan Pact]]
to guard each other's backs. When Atatürk died in 1938 Metaxas ordered official state mourning across
Greece for the man who had destroyed the Greek army, declaring Greece had lost a vital friend and an
irreplaceable pillar of regional stability. And he went in person: the delegation lists record
Metaxas leading Greece's delegation at the [[Death and State Funeral of Atatürk]], and a
contemporary Havas wire of 12 November 1938 — caught in the Dutch press corpus — announced his
attendance at the interment. The same dispatch carried Salonika's gesture: the renaming of
Atatürk's birth street ([[Salonika Names His Street, November 1938]]).
""")),

("Aga Khan III", dict(role="Spiritual leader of the Ismaili Muslims", nat="Indian / global", life="1877–1957",
  stance="petitioner, accidentally weaponised", tags=["religious", "antagonist"], body="""
In late 1923, with rumours swirling that the Caliphate would be dismantled, the Aga Khan and Syed
Ameer Ali wrote a highly publicised letter to Ankara pleading for its preservation as the last great
symbol of global Islamic unity.

Atatürk weaponised it. Because both signatories were subjects of the British Empire he took the
letter to parliament as proof that the Caliphate was a Trojan horse for British interference — and
used the plea for Islamic unity as the exact pretext for the [[Abolition of the Caliphate]] days
later, in March 1924.
""")),

("Antoun Saadeh", dict(role="Founder of the Syrian Social Nationalist Party", nat="Lebanese/Syrian", life="1904–1949",
  stance="ideological twin, territorial enemy", tags=["antagonist", "nationalist"], body="""
Ideologically near-identical to Atatürk — a secular, authoritarian nationalist wanting a powerful
modern state free of clerical control — and violently opposed to him over territory. Through
diplomatic manoeuvre and military pressure on the French, Atatürk engineered the annexation of the
Sanjak of Alexandretta (Hatay) in the late 1930s. Saadeh read it not as anti-imperialism but as
betrayal: Atatürk as a new kind of imperialist carving up the Syrian homeland. A clean demonstration
that the Middle East's new secular nationalisms would clash over borders exactly as the empires they
replaced had.
""")),

("W.B. Yeats", dict(role="Poet and Nobel laureate", nat="Irish", life="1865–1939",
  stance="mystical admirer", tags=["admirer", "literary"], body="""
In *A Vision*, his esoteric account of the cyclical nature of history and personality, Yeats was
preoccupied with the "Great Man" — the Nietzschean figure capable of destroying a decaying historical
cycle and forging a new one — and explicitly named "Mustafa Kemal" as a contemporary example. Not a
politician or a general to Yeats but a manifestation of pure historical will, imposing his own
reality on the collapse of an ancient empire. Compare [[Emil Ludwig]].
""")),

("Vladimir Mayakovsky", dict(role="Futurist poet", nat="Soviet", life="1893–1930",
  stance="fellow-revolutionary observer", tags=["observer", "literary", "communist"], body="""
In the 1920s the USSR and Kemalist Turkey were Europe's two great revolutionary pariahs, and
Mayakovsky travelled there during the window of mutual admiration. His poetry celebrated industry,
speed and the destruction of the bourgeois world, and he found a parallel in the dizzying chaotic
energy of the new Turkish state — noting the poverty and the heavy-handedness, but praising the
absolute severance from the "archaic" Ottoman past. For a moment the Soviet avant-garde read the
[[Alphabet Reform]], the new clothes and the new laws as a parallel track to their own engineered
future. See [[Sergei Yutkevich]].
""")),

("Kazi Nazrul Islam", dict(role="National poet of Bangladesh", nat="Bengali", life="1899–1976",
  stance="admirer", tags=["admirer", "literary", "anti-colonial"], body="""
In 1921, with the [[Greco-Turkish War]] still raging, he wrote the ferocious poem *Kemal Pasha*. He
cared nothing for Middle Eastern geopolitical nuance — what mattered was that a non-Western army was
slaughtering the proxy forces of the British Empire. The poem is a visceral celebration of violence
against oppressors, portraying Atatürk as an unstoppable force of vengeance for the colonised world.
It became a rallying cry in Bengal, recited by students and militants, and cemented Atatürk as a
mythological figure in South Asian anti-colonial literature.
""")),
]

for name, kw in P:
    person(name, **kw)
print(f"batch2: {len(P)} people")
