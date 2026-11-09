# -*- coding: utf-8 -*-
# Census round 6 (Oct 2026) — contemporary English-language books, 1919-1938, openly readable on the Internet Archive.
# Method: archive.org advancedsearch + full-text (fts) search, openness check on item metadata (no access-restricted-item),
# djvu text download, search-inside leaf numbers (details/<id>/page/n<k>). Page numbers = printed pages unless marked.
from _lib import note, person

IA = "https://archive.org/details/"

P = [
("Sisley Huddleston", dict(role="Author of *Those Europeans* (1924); English-born journalist writing from Paris (⚠️ biography not from the book)", nat="British (⚠️ from catalogue/bio, not the book)", life="1883–1952 (Internet Archive catalogue)",
  stance="sceptical — credits Kemal's skill, doubts his power and asks whether he has led Turkey into a worse bondage", tags=["journalist", "british", "contemporary", "conflicted", "verified"], body="""
A full chapter, **"Mustapha Kemal: The Napoleon of the New Turkey"** (ch. XVIII, pp. 253–266), in a book of
portraits of "foreign faces". The title promises a Napoleon; the text is cooler. Written in 1924, in the weeks
after the Caliph's deposition, it treats Kemal as the winner of a diplomatic and military game whose real hero
is Angora's *circumstances*.

**What he saw.** On Lausanne: *"Thus the cards were all in the hands of Mustapha Kemal, and it must be
confessed that he played them with real skill"* (p. 258). The Kemalists "stampeded the Greeks" and "frightened the
great Western Powers" and imposed a treaty that "registered the defeat of the Allies" (pp. 255–256). But he
reads Kemal's personal authority as "purely relative": Kemal "must now, sometimes against his better judgment,
follow his followers rather than insist upon his followers following him" (p. 256); he is "a comparatively wise,
sober and moderate man" among fanatics (p. 255), "hardly the leader of supreme power that he might have become"
(p. 261). Citing Maxwell Macartney, he notes that Kemal combined the Presidency of the State, the Assembly,
the Cabinet and the Popular Party — "an extraordinary accumulation of power" (p. 263) — and that Turkey "cannot be
regarded as a European Democracy". The forecast is the sharpest line: *"It is quite possible that within a few
years he will be displaced"* (p. 262); xenophobia, he adds, "is a disease which may prove to be fatal" (p. 265).
He also records the reforms with approval — the Turkish woman "is rejecting the veil and has received the vote" (p. 261). The chapter ends on a question: *"Now Mustapha Kemal has done well in bringing the Turks out of bondage; but has he led them into a bondage which in the end will be even worse?"* (p. 266), though "there is reason to believe that Mustapha Kemal is himself disposed to check the terrible tendency towards xenophobia".

**Not a straight admirer, not an enemy.** He wants Constantinople kept and the Kemalist "insularity" softened;
he regrets that France "helped to place the Allies in the most humiliating position" (p. 258). Compare the
more adulatory [[H.C. Armstrong]] of 1932–33 and the colder [[Arnold J. Toynbee]] of 1922.

**Caveat.** His forecast (displacement) was wrong; the chapter is a snapshot of the moment before the
Republic's consolidation. Page numbers are printed pages (search-inside leaf = printed + 8).

## Sources
- Huddleston, *Those Europeans: Studies of Foreign Faces* (New York & London: Putnam, 1924), ch. XVIII, pp. 253–266 · P — [IA scan, leaf n261 ff.](https://archive.org/details/thoseeuropeansst0000hudd/page/n261/mode/2up?q=Kemal) · [full text](https://archive.org/download/thoseeuropeansst0000hudd/thoseeuropeansst0000hudd_djvu.txt)
- Second scan: https://archive.org/details/thoseeuropeansst006438mbp
""")),

("George Horton", dict(role="'For thirty years consul and consul-general of the United States in the Near East' (title page); in Smyrna until 13 September 1922 (Introduction)", nat="American", life="1860–1942",
  stance="hostile — holds Kemal's army burned Smyrna to exterminate its Christians, and that Christian powers built him up", tags=["diplomat", "american", "contemporary", "smyrna", "antagonist", "verified"], body="""
*The Blight of Asia* (Indianapolis: Bobbs-Merrill, 1926), subtitled "an account of the systematic extermination of
Christian populations by Mohammedans and of the culpability of certain great powers; with the true story of the
burning of Smyrna", by a man who says he was in Smyrna "up until the evening of September 13, 1922, on which date
the city was set on fire by the army of Mustapha Khemal" (Introduction). It is the most-cited hostile
eyewitness-author of the Smyrna literature — and it is on the card here as a *gaze at Kemal*, not as a ruling on
what happened: historians still dispute who set the fire (see [[Burning of Smyrna]]).

**What he saw.** Kemal ("Khemal" throughout) is the author of the destruction and of the larger design:
*"Mustapha Khemal made a stupendous blunder when he burned Smyrna and maltreated its inhabitants"* (p. 167),
because kind treatment would have made the Christians rally to him and "he would have shown himself a really great
man". The torch was applied "systematically" by "the soldiers of Mustapha Khemal in order to exterminate
Christianity in Asia Minor" (p. 142); the plan was "a complete and irretrievable ruin of Christianity in Asia
Minor. Carthago delenda est" (p. 106). Horton's second target is the West: *"Mustapha Khemal, who burned Smyrna
and completed the destruction of the Christians, is a creature of Europe"* (p. 178), and ch. XIV, "The Making of
Mustapha Khemal" (p. 209 ff.), opens: the building-up of Kemal by certain Christian countries "was one of the
unwisest, most pernicious and most dangerous deeds that Occidental diplomacy, intrigue and jealousy has ever
perpetrated". He ties Kemal to Talaat ("Khemal has followed in the footsteps of Talaat", p. 236) and singles out
the French (Franklin-Bouillon "seizing Mustapha Khemal in his arms, kissed him", p. 192 — see [[Franklin Bouillon]])
and the American missionary who "loudly proclaim[ed] Mustapha Khemal the George Washington of Turkey" (p. 221).

**Counterweight.** Seen against [[Arnold J. Toynbee]]'s 1922 reading of Kemal as an "audacious rebel", Horton is the
case for the prosecution; the tone ("the Turk is an anachronism", p. 35) is racial as well as political, which a reader
should keep in view.

**Caveat.** Printed pages are from the 1926 scan (leaf = printed + 26); a 1953 reissue scan has different
leaf numbering (+18).

## Sources
- Horton, *The Blight of Asia* (1926): Introduction; pp. 106, 142, 163, 178, 186, 209–221, 236 · P — [IA scan (1926)](https://archive.org/details/blightofasiaacco00hort/page/n189/mode/2up?q=Khemal) · [full text](https://archive.org/download/blightofasiaacco00hort/blightofasiaacco00hort_djvu.txt)
- 1953 reissue scan: https://archive.org/details/blightofasiaacco0000hort
""")),

("Lysimachos Oeconomos", dict(role="Greek historian, Lecturer in Modern Greek and Byzantine History, King's College, University of London (title page)", nat="Greek", life="1895–1944",
  stance="hostile — holds Kemal's troops and leaders had every interest in destroying Christian Smyrna", tags=["historian", "greek", "contemporary", "smyrna", "antagonist", "verified"], body="""
*The Martyrdom of Smyrna and Eastern Christendom* (London: Allen & Unwin, 1922) is billed as "a file of
overwhelming evidence, denouncing the misdeeds of the Turks in Asia Minor and showing their responsibility for the
horrors of Smyrna", **compiled and prefaced** by Oeconomos. Most of the book is press and eyewitness
testimony from September 1922 (including Daily Telegraph dispatches, which the book
reproduces — their Kemals are theirs, not his). The author's own gaze is the Preface.

**What he saw.** He argues from cui bono: the Greeks had nothing to gain from burning Smyrna, so the guilt falls to
"the one to whom the wicked action was to be beneficial": *"For Kemal Pasha's troops, Christian Smyrna, Giaour
Izmis, was like another Carthage which they had to destroy in order to suppress for ever the focus and the
principal cause of their actual troubles"* (Preface, p. 14); "Kemal's warriors" wanted the city's wealth and women;
and "the Angora National Leaders could not dream of disappointing their barbarous instruments" (p. 15). Part I, ch. I
is headed "Treatment of Christian Minorities … in Kemalist Asia Minor". Kemal is therefore a *commander
responsible*, not (in the preface) a specific incendiary.

**Texture.** Among the compiled documents the book also prints reports that cut against the thesis — a
correspondent who saw "no massacres" in the first days (leaf n67), a dispatch that "Kemal must have given strict
orders to his troops" (leaf n71) — and a Reuter item that Kemal's Order of the Day said molestation of Christians
"will be punished by death" (leaf n98). Leaf numbers are the archive.org scan; printed pages were not checked. A reader can use it as a dossier of what Britain was reading in 1922, alongside
[[Burning of Smyrna]] and [[Paris Reads Smyrna and the Straits, September 1922]].

**Caveat.** Oeconomos was writing for the Greek national cause within weeks of the catastrophe; as with
[[George Horton]], the card records his view of Kemal, not a settled account of the fire.

## Sources
- Oeconomos (comp.), *The Martyrdom of Smyrna and Eastern Christendom* (London: George Allen & Unwin, 1922), Preface pp. 9–24 (Kemal at p. 14–15); ch. III documents · P — [IA scan, leaf n16](https://archive.org/details/martyrdomofsmyrn00oecoiala/page/n16/mode/2up?q=Carthage) · [full text](https://archive.org/download/martyrdomofsmyrn00oecoiala/martyrdomofsmyrn00oecoiala_djvu.txt)
""")),

("Henry Morgenthau Sr.", dict(role="Author of *I Was Sent to Athens* (1929), on the League of Nations Greek refugee settlement (dedicated 'to the creators of the League of Nations'); former US ambassador at Constantinople (⚠️ not from the pages read)", nat="American", life="1856–1946",
  stance="conflicted — 'ablest officer', 'dictator', and the man under whose eye Smyrna's Greek quarter burned", tags=["diplomat", "american", "contemporary", "league-of-nations", "smyrna", "conflicted", "verified"], body="""
*I Was Sent to Athens* (Garden City: Doubleday, Doran, 1929; "in collaboration with French Strother") is Morgenthau's
account of the Greek refugee settlement after 1922. Kemal is a recurring figure (index: pp. 7, 25, 30, 41–42, 48, 91).

**What he saw.** Kemal is first the able organiser: *"Mustapha Kemal, the ablest officer the Turks had had during the
war, now emerged as the political and military leader of an organized movement to defy the whole world, if
necessary, to preserve a Turkish nation in Asia Minor"* (p. 25). He is then the Smyrna defendant: among the
causes of the refugee emergency is "the systematic burning of the Greek quarter of Smyrna by the Turkish troops
under the very eye of Kemal" (pp. 47–48) and a Nationalist programme by which Asia Minor "was to be completely
'Turkeyfied'" (p. 48). On the Franklin-Bouillon agreement, signed "by Kemal for the Turks", he blames French
"greed of French capitalists" for deserting the Greeks (p. 30; [[Franklin Bouillon]]). At the time of his 1923 mission,
Turkey "was now ruled by a single new dictator, Kemal Pasha, whose capital was not Constantinople but … Angora"
under whom "the Turks were making their last stand to preserve their nation" (p. 91).

**Reading.** A Wilsonian humanitarian who is neither Horton's prosecutor nor the admirer: he respects the
soldier, assigns the Nationalists responsibility for the Greek exodus, and in the same book chairs the settlement
that depended on Turkey's cooperation. His 1915–16 ambassadorship is the context readers bring ([[Talat Pasha]]); this book is about 1923 on.

**Caveat.** Ghost-collaborated memoir; passages on Smyrna are summaries in a list of causes, not eyewitness
(the book does not claim he was at Smyrna in 1922). Printed pages from the book's index; leaf = printed + 12.

## Sources
- Morgenthau, *I Was Sent to Athens* (1929), pp. 25, 30, 41–42, 47–48, 91, index "Kemal, Mustapha" · P — [IA scan, leaf n37](https://archive.org/details/iwassenttoathens00morg/page/n37/mode/2up?q=Kemal) · [full text](https://archive.org/download/iwassenttoathens00morg/iwassenttoathens00morg_djvu.txt)
""")),

("Jacques Bainville", dict(role="French historian and Action française journalist; *Dictators* in English translation (J. Lewis May, 1937)", nat="French", life="(not checked)",
  stance="ironic — a 'dictator' chapter that finds him the 'most curious and original' and mocks the speed of his reforms", tags=["historian", "french", "contemporary", "conflicted", "verified"], body="""
In Bainville's *Dictators* (London: Jonathan Cape, 1937; Life and Letters series; English text by J. Lewis May)
Mustapha Kemal is the only non-European among the modern dictators, between Stalin and Mussolini: ch. **"M.
Attaturk, formerly Mustapha Kemal"** (contents: p. 196 ff.). The framing already declares a stance: dictatorships
"can be the best, or the worst, form of government", and the book sorts them by results.

**What he saw.** Among the dictators of "our" time, "the most curious and most original figure" is, he thinks, Kemal (p. 196; the scan's OCR garbles the rest of that sentence). Judged "by the magnitude
of the changes it has wrought in a country", no dictatorship exceeds his. The comparison set is Peter the Great
(forced Europeanisation, the beards-and-fez parallel) with something of Washington and of Genghis Khan in him (his own comparison). The register is Parisian irony: the hat reform was "the battle of the tailors and hatters", for which he had to
"'abolish' the heads of some score or so of obstinate die-hards"; the new Turkish history is compressed "into twenty
pages"; he "annexed the Hittites" and after the Sumerians were brought to light, "Sumerians became the fashion"; and *"He turns out reforms as if they were
being reeled off a film"* (p. 201). He notes the borrowings (the Swiss Code adopted "without a debate"; surnames, "another leaf out of the
European book") and calls him "this amazing dictator" who is "henceforth to be known as Monsieur Attaturk" (p. 202).

**Reading.** Not hostile (the verdict is that Kemal's work is *complete*), not admiring (the reformer is a showman
and the method a dictator's). Compare [[Emil Ludwig]]'s portrait of the same years and [[H.C. Armstrong]].

**Caveats.** (1) English text by a translator; ⚠️ the original French chapter was not checked. (2) The original
French date of the chapter was not checked; the English text already uses "Attaturk", so it postdates the 1934 Surname Law. (3) The OCR is poor in places; quotes are those the scan reproduces legibly.

## Sources
- Bainville, *Dictators*, trans. J. Lewis May (London: Jonathan Cape, 1937; reissued 1940), contents + ch. "M. Attaturk, formerly Mustapha Kemal", pp. 196–205 · P — [IA scan](https://archive.org/details/JacquesBainvilleDictators?q=Mustapha+Kemal) · [full text](https://archive.org/download/JacquesBainvilleDictators/JacquesBainvilleDictators_djvu.txt)
""")),

("Cemal Pasha", dict(role="Young Turk triumvir; Ottoman naval minister; commander of the Fourth Army in Syria; author of *Memories of a Turkish Statesman, 1913–1919* (English ed. 1922)", nat="Ottoman / Turkish", life="1872–1922 (assassinated Tiflis, July 1922)",
  stance="supportive of Kemal as a soldier and as the hope of the national rising — a CUP veteran's endorsement", tags=["ottoman", "unionist", "memoirist", "contemporary", "admiring", "verified"], body="""
The Unionist leader's memoir (London: Hutchinson, 1922; the scan's front matter also names George Grew, US
ambassador to Turkey — ⚠️ his role in the volume was not read) covers Kemal only as a colleague of the war years —
which is exactly its worth. It is a
Young Turk triumvir's judgment of the man who would end the Young Turks' politics.

**What he saw.** In the Syrian command dispute of autumn 1917 Kemal, commander of the Seventh Army, clashed with
the German general von Falkenhayn; Cemal investigated and *"came to the conclusion that Kemal Pasha was entirely in
the right"*, because Kemal "respected all the rights of the Army Commander" while Falkenhayn "claimed the right to
interfere in the affairs of the 7th Army in a way which was inadmissible even in dealing with a Corps Commander"
(ch. VII, "The Battles of Gaza", p. 192). He also records Kemal's earlier achievement at Bitlis and Muş ("had
succeeded in recovering … the province of Bitlis and Mush", p. 182), and the fact that Kemal "disapproved of my
attitude" in staying in Syria. The closing paragraph of ch. VIII looks to the future: *"If God pleases, the Turks will
succeed in saving proud Stamboul and beautiful Smyrna for their country, thanks to the recent national rising under
the leadership of Mustafa Kemal Pasha"* (pp. 237–238).

**Reading.** Cemal's colleague [[Enver Pasha]] is the Young Turk who, in Cemal's account, planned the Baghdad expedition under
Falkenhayn; Cemal sides with Kemal against the German. Compare [[Talat Pasha]].

**Caveat.** A passing view across 700 pages; intensity is moderate (2), not a portrait. Page numbers are the book's.

## Sources
- Djemal Pasha, *Memories of a Turkish Statesman, 1913–1919* (London: Hutchinson, 1922), pp. 182, 192–193, 237–238 · P — [IA scan](https://archive.org/details/39020025953798-memoriesofaturk?q=Mustafa+Kemal) · [full text](https://archive.org/download/39020025953798-memoriesofaturk/HighRes_39020025953798_djvu.txt)
""")),

("Eliot Grinnell Mears", dict(role="American author and editor of *Modern Turkey* (1924), who describes himself as having spent months in Turkey 'as a government official'", nat="American", life="(not checked)",
  stance="admiring — Turkey 'owes its independent position to the genius' of Kemal", tags=["american", "contemporary", "trade", "admiring", "verified"], body="""
*Modern Turkey: A Politico-Economic Interpretation, 1908–1923* (New York: Macmillan, 1924), a multi-author reference work
edited by Mears, with his own General Introduction, written for American businessmen and policymakers.

**What he saw.** Mears's General Introduction (p. 29): *"Turkey of the present day owes its independent position to the
genius of Mustafa Kemal Pasha."* He explains the appeal in Islamic terms ("Mohammedans are deeply stirred by a
contemporary hero whose exploits they can understand. They expect the ruler to be arbitrary, to play favorites, but to
be powerful always") and notes Kemal's "countless difficulties in his efforts to reconcile the varied political views of
his own party". Elsewhere he compares Kemal's caliphate move to Cavour's: Kemal "has wrought politico-religious
changes no less momentous than those of Cavour, but his new departures are more sweeping". The book prints a
photograph of the President with Latife Hanım (list of illustrations, p. 574) and Kemal's Izmir Economic Congress
speeches (1923) — "Those who effect conquests by the sword finish by being beaten by those who employ as their arm
the plough" — as evidence of Angora's openness to foreign capital.

**Reading.** An instrumental-leaning admiration: the praise serves a commercial thesis (invest in Turkey, the
Kemalist state is stable and welcoming). Compare [[Charles H. Sherrill]] and [[Mark L. Bristol]] for the American
business-diplomatic approach to Angora.

**Caveat.** Contributors' chapters are not Mears's views; only the General Introduction is attributed to him. The
scan's OCR of the front matter is poor, so his title and credentials are given only as the book describes them.

## Sources
- Mears (ed.), *Modern Turkey* (New York: Macmillan, 1924), General Introduction, p. 29; later chapters on the Caliphate and the 1923 Economic Congress · P — [IA scan](https://archive.org/details/ModernTurkey?q=genius+of+Mustafa+Kemal) · [full text](https://archive.org/download/ModernTurkey/ModernTurkey_djvu.txt)
""")),

("Rosita Forbes", dict(role="British traveller and author of *Conflict: Angora to Afghanistan* (1931)", nat="British", life="(not checked)",
  stance="conflicted — a modernising achievement she thinks as dangerous to minorities as Abdul Hamid's fanaticism", tags=["traveller", "british", "contemporary", "conflicted", "verified"], body="""
*Conflict: Angora to Afghanistan* (London: Cassell, 1931) opens in Ankara. Its author's preface sets out the
claim of the whole journey — "a decade of intensive modernization, imposed largely by force" on "peoples traditionally
conservative" — and gives Turkey the first and sharpest sentence.

**What she saw.** *"Turkey in Asia was involved in what may well be the last act of the long tragedy in which first
Armenians and then Kurds were cast for the rôle of victims, and it was obvious that the nationalism of Mustafa Kemal can
be as dangerous to the Minorities, whose treatment is a test of civilization, as was the fanaticism of Abdul Hamid."*
(Author's Preface.) In ch. I, "The New Turkey" (pp. 1–5), she meets "the new Turk … nationalist, Kemalist, republican,
and, above all things, incurably optimistic", sees the Ghazi's statues ("the man who conceived, constructed, holds, and
dominates Angora") and describes Kemal in person as "a small man brooding over great schemes" who, in metal, "represents
the spirit of young Turkey, undaunted by anything within itself, yet defiant and always on the defensive". Her verdict on
the Turkish case: "Angora is her vindication".

**Context.** Sir Percy Sykes's Foreword (pp. vii–xvi) calls Turkey's survival "thanks mainly to the genius of Mustafa
Kemal" — but that is Sykes, not Forbes; the vault does not attribute it to her. The pairing of Forbes's sceptical preface
and Sykes's admiring foreword in one volume is itself a window on British opinion in 1931. See also [[Grace Ellison]]'s
*Turkey To-day* (1928).

**Caveat.** Page numbers from the running heads of the 1931 scan: the Author's Preface is unnumbered; ch. I statues
and "small man" passages are pp. 3–4.

## Sources
- Forbes, *Conflict: Angora to Afghanistan* (London: Cassell, 1931), Author's Preface; ch. I "The New Turkey", pp. 1–5 · P — [IA item](https://archive.org/details/conflict-angora-to-afghanistan) · [full text](https://archive.org/download/conflict-angora-to-afghanistan/Forbes%201931%20Conflict%20Angora%20to%20Afghanistan_djvu.txt)
""")),

("Lothrop Stoddard", dict(role="American author of *The New World of Islam* (1921) and *The Rising Tide of Color*", nat="American", life="1883–1950",
  stance="conflicted — respects the officer and the army, fears what he reads as a rising pan-Islamic and Bolshevik-friendly resistance to the West", tags=["american", "contemporary", "orientalist", "conflicted", "verified"], body="""
In *The New World of Islam* (New York: Scribner, 1921), ch. "Nationalism" (pp. 227–238), Kemal is introduced in the
spring-1920 aftermath of Sèvres as one of "new leaders" who appeared after the Young Turk chiefs fled.

**What he saw.** *"… new leaders appeared, notably a young officer of marked military talent, Mustapha Kemal Pasha.
With great energy Mustapha Kemal built up a really creditable army, and from his 'capital,' the city of Angora in the
heart of Asia Minor, he now defied the Allies"* (p. 228). He treats the Sèvres signatories as "nationalist as Mustapha
Kemal himself" and reports Kemal's "I will fight to the end of the world" (p. 229). The frame, though, is Stoddard's
general thesis of an Islamic and "coloured" resurgence: Kemal was "establishing close relations with the Arabs" and
"reaching out northeastward to the Tartars of Transcaucasia", "his efforts … supported by a third ally — Bolshevik
Russia" (pp. 232–233), and "Kemal's hand was clearly apparent in the rebellion against the British in Mesopotamia"
(p. 232). The chapter on "Social Unrest" later warns that Bolshevism will first back and then destroy "nationalists
like Mustapha Kemal" (p. 337).

**Reading.** Not hostile to Kemal personally — he is a competent adversary — but an early model of the Western
"pan-Islam" alarm reading that [[Arnold J. Toynbee]] and [[Charles H. Sherrill]] would, in different keys, take apart.

**Caveat.** The book's racial framework is explicit (it cites the author's *The Rising Tide of Color against White
World-Supremacy*, p. 336 n.); the card records the passage, not an endorsement. Page numbers inferred from running heads (p. 229 header "NATIONALISM 229").

## Sources
- Stoddard, *The New World of Islam* (New York: Scribner, 1921), pp. 227–233, 337 · P — [IA scan](https://archive.org/details/newworldofislam00stodrich?q=Mustapha+Kemal) · [full text](https://archive.org/download/newworldofislam00stodrich/newworldofislam00stodrich_djvu.txt)
""")),

("H. E. Wortham", dict(role="British author of *Mustapha Kemal of Turkey* (London: Holme Press, 1930), 'Makers of the Modern Age' series", nat="British", life="(not checked)",
  stance="conflicted-admiring — 'a great idealist and a great iconoclast' who 'has been entirely ruthless'", tags=["biographer", "british", "contemporary", "conflicted", "verified"], body="""
An early English biography (1930), published as a volume in the *Makers of the Modern Age* series edited by Osbert
Burdett; frontispiece is a *Times* photograph of Kemal addressing the People's Party Congress. The editor's note says the series
"begins with two volumes dealing with the contrasting problems of personal dictatorship and of proletarian rule", and
the book carries a Low cartoon from the *Evening Standard*, "Mustapha Kemal among the other Dictators".

**What he saw.** The first page announces the tension: Kemal "a great idealist and a great iconoclast" (ch. I, pp. 1–3),
a "Cincinnatus" who dislikes flattery — and yet "beneath the debris of old ideas and institutions he has destroyed …
one still observes, as the basis of his policy, the ruthlessness which is the essential characteristic of eastern, as
compared with western, conceptions of government". The index entry "his ruthlessness, 160" points to the key page:
*"Arrest, an apology for trial, the hangman's rope — this trio is a familiar feature of the infancy of the Republic. The
Ghazi Pasha has been entirely ruthless. He has trampled on his enemies and sent personal friends to the gallows"* (p. 159);
his justification must be "that without such harsh medicine Turkey would never have laid the basis of a national life
organised under the rule of law". On dictatorship he is more generous than his contemporaries: Kemal "never lost his
patience with the Assembly — a point in which he stands alone amongst the team of post-war dictators".

**Reading.** A rare 1930 English text that names the hangings of the [[Independence Tribunals]] without either hiding
or relishing them. Compare [[H.C. Armstrong]] (1932–33) and [[Grace Ellison]].

**Caveat.** Page numbers are the book's own. The biography's author is identified only by the title page here.

## Sources
- Wortham, *Mustapha Kemal of Turkey* (London: Holme Press, 1930), ch. I (pp. 1–7) and pp. 159–160 · P — [IA item (Digital Library of India scan)](https://archive.org/details/in.ernet.dli.2015.72607) · [full text](https://archive.org/download/in.ernet.dli.2015.72607/2015.72607.Mustapha-Kemal-Of-Turkey_djvu.txt)
""")),
]

for name, kw in P:
    person(name, **kw)
print("b14_books_en: wrote", len(P), "person notes")
