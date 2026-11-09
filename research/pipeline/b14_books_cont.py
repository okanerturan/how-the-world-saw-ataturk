# -*- coding: utf-8 -*-
# Census round 6 (Oct 2026) — continental-language books, 1919–1938 (slug: books_cont).
# Method: full-text downloads ONLY from items the Internet Archive serves openly (its `_djvu.txt`);
# Gallica monographs read as ContentSearch fragments (view numbers, not printed pages) through the
# `fetch` wrapper. Every French/German quotation is checked verbatim against the OCR text; long-s and
# line-break hyphens are normalised, nothing else. Page numbers are the book's printed pages unless
# marked "view".
from _lib import person

P = [

("Berthe Georges-Gaulis", dict(role="French journalist and author; guest of Mustafa Kemal at Ankara, Nov–Dec 1921",
  nat="French", life="",
  stance="admiring witness — the French reporter who told Paris what Angora was, and whom Kemal asked to do exactly that",
  tags=["journalist", "admirer", "france", "contemporary", "verified"], body="""
Her *Angora, Constantinople, Londres* (Paris, 1922) is a book of three capitals, and an early
chapter is a portrait: **"Moustafa Kémal Pacha"**, opening on p. 25. She had been in Anatolia
earlier in 1921 ("l'entretien interrompu six mois auparavant"), came back for a second stay at Ankara in
**November–December 1921** (weeks after the Franklin-Bouillon accord — see [[Franklin Bouillon]]), and writes as a woman
who has been the pasha's houseguest at his hillside house ("Tchan-Kaya," Çankaya) and says so.

**What she saw.** A maker of an epoch, not a soldier: *"On peut dire que, sans lui, l'Islam aurait mis
cinquante ans de plus à trouver sa route"* (p. 25). The man himself she renders as will plus patience —
*"un infatigable lutteur,"* "d'un désintéressement absolu" (p. 43), "le caractère le plus complexe, le plus
nuancé qui se puisse allier avec une sincérité parfaite" — and the book's one reported aside, from an opponent who had
been attacking him and then stopped, "Oui, il est bon, sincèrement bon, bon comme aucun autre" (p. 43).
She prints her own notes from an evening at Çankaya on the voice ("de l'acier dans ce timbre," p. 44) and quotes
his 1917 Aleppo report to Talat and Enver as proof that he had never been anyone's tool (pp. 29–30).

**Why this is also an instrumental gaze.** The access was the bargain. On her return he told her
(p. 40): *"vous serez complètement mon hôte … nous ne vous demanderons qu'une chose : nous faire mieux
connaître chez vous, y détruire les légendes, si vous les jugez fausses une fois de plus."* She
accepted the commission and says she was "plus libre dans ses paroles et dans ses jugements que je ne
le fus à Angora" (p. 40) — and the result is exactly the legend-destroying portrait he asked for. The
Franco-Turkish *rapprochement* of October 1921 needed such a voice in Paris. Compare [[Grace Ellison]] (the
English woman guest of the same years) and [[Claude Farrère and Pierre Loti]] (the French romantic
option).

**Caveat.** Everything here is her book's own account of the visit; the Çankaya interviews are
unrecorded elsewhere in the vault.

## Sources
- Georges-Gaulis, *Angora, Constantinople, Londres* (Paris, 1922; publisher not read from the scan) — pp. 25, 29–30, 40, 43–44. Full text, open: [archive.org/details/angoraconstantin00geor](https://archive.org/details/angoraconstantin00geor) (`_djvu.txt`) · tier P
""")),

("E. Nicol", dict(role="French pamphleteer; author of *Angora et la France: une réponse à M. Franklin-Bouillon* (Paris, Feb 1922)",
  nat="French (identity not established)", life="",
  stance="hostile — the answer to the Angora lobby, written from the Entente side",
  tags=["pamphleteer", "hostile", "france", "contemporary", "verified"], body="""
A 36-page pamphlet (the text's last page head reads 36) dated **Paris, 18 February 1922**, written in reply to the lecture in which [[Franklin Bouillon]],
home from the Angora mission, "rompit le silence." Nicol is not otherwise identified in the sources I
have; the voice is that of the Entente-first argument against the Angora deal, defending the Allied line of the
Treaty of Sèvres ([[Treaty of Sèvres]]).

**What he saw.** Kemal as the *front* of a movement whose essence is hostility to Europe. *"La xénophobie
et la haine de l'Europe sont l'essence même du kémalisme"* (p. 15) — and the pamphlet's own twist on
Franklin-Bouillon's "grand ami": the generalissimo is "un des officiers qui se distinguèrent le plus
sous les ordres des Allemands pendant la guerre contre les Alliés," in disgrace only because of
his rivalry with Enver, recalled through Liman von Sanders' intervention (p. 24, page head lost in the OCR
between pp. 23 and 25). Franklin-Bouillon's remark to Kemal at Ankara ("La France joue son honneur. Vous,
vous jouez votre vie") is turned into an index of European naïveté: the "Turc astucieux" must have smiled
at an interlocutor whose candour can only have deepened the nationalists' contempt for "ces imbéciles
d'Européens si facile à rouler" (pp. 26–27). He ends by arguing that the Kemalists need only be starved
of European arms and supplies "pour le voir s'émietter" (p. 36).

**Why it matters.** This is the other half of the Franco-Turkish argument of 1921–22: a *French* anti-Angora
voice, February 1922, seven months before the Kemalist victory at Smyrna ([[Burning of Smyrna]]) that made its
forecast of a movement that would "s'émietter" without European arms look wrong.

## Sources
- E. Nicol, *Angora et la France: une réponse à M. Franklin-Bouillon* (Paris: Société générale d'imprimerie et d'édition, 1922) — pp. 15, 24, 26–27, 36. Full text, open: [archive.org/details/angoraetlafrance00nico](https://archive.org/details/angoraetlafrance00nico) (`_djvu.txt`) · tier P
""")),

("Michel Paillarès", dict(role="French journalist in Constantinople (editor-publisher, *Le Bosphore*); author of *Le Kémalisme devant les Alliés* (1922)",
  nat="French", life="",
  stance="hostile — the Constantinople chronicler of the Entente line",
  tags=["journalist", "hostile", "france", "contemporary", "verified"], body="""
Paillarès landed in Constantinople "juste vingt-neuf ans" before October 1921 (so in 1892) and published the more-than-350
pages of *Le Kémalisme devant les Alliés* (Éditions du Bosphore, Péra and Paris, 1922): a
chronicle of 1919–1921 — "L'entrée en scène du kémalisme," the Treaty of Sèvres, the Angora accord,
"vers la paix d'Orient" — stitched from his own articles and the Allied press.

**What he saw.** A xenophobe whose moderation is a mask. In the opening of the chapter on the French
policy (1920, by position in the book): *"Les tendances de Moustafa Kemal sont nettement xénophobes. Son programme se résume en
ces quatre mots : La Turquie aux Turcs !"* — and the omission of Syria and Arabia from his programme "c'est
uniquement pour endormir les méfiances de l'Entente" (p. 65). Late in the book he retells Lloyd George's question to a minister of the Erivan republic, "De ces deux maux,
le bolchevisme et le kémalisme, lequel choisiriez-vous ?", and draws the moral himself: under the Soviets the Christians
"ont au moins la certitude de n'être pas massacrés" (p. 346). The book argues for Entente coercion and for the Armenian and
Christian side; its Kemal is a danger to be "maté," not a partner.

**Caveat.** The book is a compilation of dated chronicle and press excerpts: this vault records only sentences
in the author's own narrative (pp. 65, 346), not the quoted dispatches. The 1920 dating of p. 65 rests on
its place in the book's chronology. Compare [[Franklin Bouillon]]'s optimism, which Paillarès's work
was trying to undo.

## Sources
- Paillarès, *Le Kémalisme devant les Alliés* (Constantinople/Paris: Éditions du Bosphore, 1922) — avant-propos; pp. 65, 346. Full text, open: [archive.org/details/lekmalismedeva00pail](https://archive.org/details/lekmalismedeva00pail) (`_djvu.txt`; page numbers read from the running heads, which the OCR garbles in places) · tier P
""")),

("Noëlle Roger", dict(role="French-language travel writer; *En Asie Mineure: la Turquie du Ghazi* (1930; preface by Gabriel Hanotaux)",
  nat="French-language author", life="",
  stance="admiring — the eyes that make resistance seem folly",
  tags=["travel-writer", "admirer", "contemporary", "verified"], body="""
A 1930 travel book on Anatolia whose title already names the sovereign: the *Ghazi*. Hanotaux, the old
Quai d'Orsay hand, wrote the preface; the author travels through Anatolia and collects Kemal anecdotes
"soir après soir" from the people she meets.

**What she saw.** Charisma as a physical fact. *"Ces yeux du Ghazi, d'un bleu ardoise sous les grands
sourcils blonds, on ne peut plus les oublier"* — *"un regard droit et clairvoyant qui pénètre les intentions
secrètes, et si chargé de volonté que toute résistance semblerait une folie"* (p. 61); a man who cannot
bear to be lied to and "déteste les compliments, les flatteries, le lyrisme officiel" (p. 62). She relays his
reply to a flatterer who compared him with Alexander and Napoleon ("Je m'appelle tout simplement Mustapha
Kémal … Mustapha Kémal de la Turquie," p. 62) and his reported saying of the two Mustapha Kemals, one
mortal, "l'autre … qui incarne la nation et qui vivra en elle éternellement" (p. 65). The political
sentence is short: "Mustapha Kémal avait sauvé l'Anatolie et libéré Constantinople" (p. 69).

**Caveat.** The anecdotes are other people's, unattributed ("dit un jeune homme"); what is firsthand is
the portrait and the framing. Nationality is not stated in the text I read; the pen-name's owner is not identified here.

## Sources
- Noëlle Roger, *En Asie Mineure: la Turquie du Ghazi* (1930; preface Gabriel Hanotaux; imprint not read from the scan) — pp. 61–62, 65, 69. Full text, open: [archive.org/details/enasiemineurelat00noel](https://archive.org/details/enasiemineurelat00noel) (`_djvu.txt`; page numbers read from the running heads) · tier P
""")),

("Herbert Melzig", dict(role="German author; *Kamâl Atatürk: Untergang und Aufstieg der Türkei* (Frankfurt a. M.: Societäts-Verlag, 1937)",
  nat="German", life="",
  stance="admiring — Atatürk as the stern schoolmaster of a nation, written under National Socialism",
  tags=["biographer", "admirer", "germany", "contemporary", "verified"], body="""
A 293-page biography with sixteen plates (1937); the jacket text claims it goes "über alle bisherigen Beiträge zu diesem Thema weit hinausreichend". It runs
from the café speech at Salonika in 1906 to the republic's building-site; the book's argument is
that the Ottoman collapse was necessary and Kemal alone saw it.

**What he saw.** The *Führer eines auferstehenden Volkes* (p. 157 or 158; the page head is lost in the scan) who outwits the sultanate by letting the
caliph's name be prayed while the nation's liberation is prayed alongside it (p. 156) — and the question
every German reader of 1937 would ask, answered with care: *"Er handelte nicht wie ein Diktator nach
westlichem Muster"* (p. 265); and in the closing pages *"Seine 'Diktatur' ist nichts anderes als die harte
Schule der Republik, die zur Freiheit erziehen will"* (p. 274), where the president-for-life is "der erste
Lehrer des Volkes, ein strenger, unnachsichtiger und doch gütiger Lehrer" (pp. 274–275) and *Atatürk*, "Vater der
Türken," is glossed in a footnote as the honorific the Turkish people gave him.

**The German frame.** This is the Frankfurt, non-Party German register of the Atatürk image
(compare [[Emil Ludwig]] in exile and [[Nazi Outreach to the Muslim World]] for the Party's own use): the
word *Diktatur* is kept in quotation marks and defended as pedagogy, not embraced as the model. It also
repeats, without comment, the national-movement line that the Armenian deportations were the "Exzessen" in
which the people took no part (Erzurum paragraph, near p. 93–95; exact page not fixed) — flagged here as the book's own account, not the
vault's.

## Sources
- Melzig, *Kamâl Atatürk: Untergang und Aufstieg der Türkei* (Frankfurt a. M.: Societäts-Verlag, 1937) — pp. 156, 157–158, 265, 274–275. Full text, open (Gdańsk University digital library scan on the Internet Archive): [archive.org/details/pbc.gda.pl.Kamal_Ataturk_Melzig_H](https://archive.org/details/pbc.gda.pl.Kamal_Ataturk_Melzig_H) (`_djvu.txt`; page numbers are the book's, printed at page foot) · tier P
""")),

("Peregrinus", dict(role="Pseudonymous German travel writer; *Peregrinus auf großer Fahrt, Bd. 2: Quer durch Kleinasien* (Leipzig: Otto Janke, 1932)",
  nat="German", life="",
  stance="conflicted — respect for the liberator, doubts about the man ('liebt nur die Türkei, seinen Staat und sich selbst')",
  tags=["travel-writer", "conflicted", "germany", "contemporary", "verified"], body="""
A Weimar-era bicycle-and-steamer travelogue across Anatolia, in a jokey first-person voice. The
volume that reached the Internet Archive via the Polish RCIN library has the title page, publisher and
printer, but not the author's real name; the pseudonym is all this vault can give.

**What he saw.** Two Kemals at once. The traveller who arrives in Istanbul on Republic Day sees "des Werkes
Kemal Paschas" in flags (early, in the Constantinople chapter; page not fixed), looks at the monument of the "Befreier und Gründer der 'modernen' Türkei" (p. 27), and
yet reports from a Turkish friend that "die Achtung, mit der man vom Gazi sprach, mehr der Furcht oder sklavischer
Unterordnung entsprang" than any understanding of what Kemal was aiming at (pp. 26–27). He calls him in so many words
the "Diktator" — "denn das war und ist nun einmal der Gazi" (p. 27) — whose opponents "wurden mit echt
tartarischer Gründlichkeit beseitigt" (p. 27) — and then, on the German
hope that Kemal was Germany-friendly (the rumour of the 1920s): *"Das ist durchaus unrichtig. Kemal Pascha hat
für jeden Staat eine freundliche 'Maske', sofern er daraus einen Nutzen für seine Türkei ziehen kann …
Der Gazi liebt nur die Türkei, seinen Staat und — sich selbst"* (p. 29). A quotation attributed to the friend
"Talaat," so the judgment is partly second-hand.

**Why it matters.** A German voice that is neither the biographer's praise nor the Party's use, from
1932, and one of very few that *refuses* the "Germany's friend" legend while still granting the liberation.

## Sources
- "Peregrinus," *Peregrinus auf großer Fahrt, 2: Quer durch Kleinasien* (Leipzig: Otto Janke, 1932; Fraktur, long-s normalised in quotations) — pp. 26–27, 29. Full text, open (RCIN Poland scan on the Internet Archive): [archive.org/details/rcin.org.pl.WA51_146655_PTG12303-2-r1932_Peregrinus-auf-bd2_124114](https://archive.org/details/rcin.org.pl.WA51_146655_PTG12303-2-r1932_Peregrinus-auf-bd2_124114) (`_djvu.txt`; page numbers printed at page foot) · tier P
""")),

("Bertrand Bareilles", dict(role="French author (1859–1933 per Gallica authority record); *Le Drame oriental: d'Athènes à Angora* (Paris, 1923)",
  nat="French", life="1859–1933",
  stance="hostile-leaning, conflicted — sneering at the constitution-maker, granting the Islamic hero",
  tags=["author", "hostile", "france", "contemporary", "verified"], body="""
A 1923 book whose title runs "d'Athènes à Angora". In the fragments read, it sets Kemal beside every other
Ottoman improviser and does not flatter him.

**What he saw (Gallica fragments, view numbers).** The Angora constitution is one of a line of Ottoman paper
reforms — *"Le Tanzimat de Rechid Pacha, la Constitution de Midhat, celle de Talaat, celle de Mustapha Kemal
demeureront comme des modèles d'acrobatie levantine"* (view 193) — the constituent assembly a "machine improvisée"
from which *"Mustapha Kemal a confisqué tous les pouvoirs qu'il a partagés avec ses lieutenants"* (view 196);
Angora is "la Satrapie de Mustapha Kemal" (view 129). Yet the same chapter calls him
*"le type modernisé de ces héros qui, à diverses époques de l'histoire et en des circonstances analogues, se sont révélés
comme les porte-drapeaux de l'Islam, tels Salaheddine"* (view 198) — a Saladin, not a clerk. The "dictateur" in view 199 holds power only by a delegation of the
assembly.

**Caveat.** Read as ContentSearch fragments of the Gallica scan, not as a continuous text; the argument
of the whole book (and whether "Le Drame oriental" is Greek-sympathising overall) is inferred from the
fragments and the title, and wants a full read. Quoted numbers are Gallica view indices.

## Sources
- Bareilles, *Le Drame oriental: d'Athènes à Angora* (Paris, 1923) — [Gallica ark:/12148/bpt6k9734946p](https://gallica.bnf.fr/ark:/12148/bpt6k9734946p), ContentSearch "Kemal" / "dictateur" / "héros", views 129, 193, 196, 198, 199 · tier P (fragments)
""")),

("Jacques Kayser", dict(role="French radical journalist and later deputy (1900–1963 per Gallica authority record); *L'Europe et la Turquie nouvelle* (Paris, 1922)",
  nat="French", life="1900–1963",
  stance="instrumental — the case for treating Angora as a government, written to be believed in Paris",
  tags=["journalist", "instrumental", "france", "contemporary", "verified"], body="""
A 1922 Paris essay-book on the new Turkey for a European readership, arguing from the Treaty of Sèvres to
the Angora regime: the view that France should deal with the government that existed.

**What he saw (Gallica fragments).** Kemal as the **consequence of the treaty**: it was "l'article 139 du Traité" that
"a cimenté sous une commune injure l'alliance de tous les Musulmans, et qui a permis à Mustapha Kemal de réussir"
(view 68). As a pragmatist of the Soviet connection — "Mustapha Kemal a saisi le rameau d'olivier que lui
tendait Tchitcherine, mais il a interdit l'accès de son territoire aux propagandistes de Moscou" (view 105), after
which the author "aurait tort de reprocher à Mustapha Kemal son attitude en cette occasion" (view 106). Angora in
the book is a "gouvernement régulier" constituted on 23 April with Kemal re-elected unanimously "à chaque
scrutin" (view 80). (Gallica's authority record gives 1900 as his birth year, which would make the author twenty-two.)

**Caveat.** Fragments only (the book was not read in continuous text); the conclusion — an advocate's, not
an apologist's — is taken from the few passages that evaluate rather than narrate. Page references are Gallica views;
view 80 corresponds to printed p. 68.

## Sources
- Kayser, *L'Europe et la Turquie nouvelle* (Paris, 1922) — [Gallica ark:/12148/bpt6k3403660t](https://gallica.bnf.fr/ark:/12148/bpt6k3403660t), ContentSearch "Kemal", views 68, 80, 105, 106 · tier P (fragments)
""")),

("Pietro Canonica", dict(role="Italian sculptor; modelled Mustafa Kemal's bust at Ankara, 1926",
  nat="Italian", life="b. 1869",
  stance="admiring witness — the sculptor who found a Piedmontese soldier in the Ghazi",
  tags=["artist", "admirer", "italy", "contemporary", "verified"], body="""
Canonica, Turin-born sculptor and favourite of the Savoy court, travelled to Ankara in **1926** to make the
president's bust and left an account, written decades later, of the sittings. The passage survives in a
2025 article by Carla Scicchitano (Istituto Italiano di Cultura, Istanbul) that quotes his unpublished
memoir in the Museo Canonica archive (*Ricordi della mia vita*, c. 1945–50).

**What he saw.** A simple host — "mi ricevette semplicemente, nella sua abitazione, una modesta palazzina arredata
con gusto, ma senza lusso, come una casa borghese" — coffee, then the pose; "un'ora dopo … il busto era già impostato e somigliante."
And a character read through his own caste: *"Egli era un uomo semplice, molto distinto nei modi al pari dei
nostri soldati lombardi e piemontesi d'antico stampo."* — a man of few words, "riflessivo e acuto osservatore," whose face
turned now imperious, now of "una dolcezza quasi infantile che commuove."

**Caveat.** (1) The words are a late memoir (c. 1945–50) of a 1926 act; the dated artefact is the bust and the
sittings, the text is retrospective. (2) The source is a secondary article quoting an unpublished archive
document; I have not seen the memoir itself. Vault status: second-hand, S-tier.

## Sources
- Carla Scicchitano, "La figura di Pietro Canonica, artista testimone del suo tempo e la sua casa-museo alla Fortezzuola di Villa Borghese," p. 41 (opening), quoting Canonica, *Ricordi della mia vita* (typescript, c. 1945–50, Archivio Storico Museo Canonica): [iicistanbul.esteri.it/…/PIETROCANONICAdigital_compressed.pdf](https://iicistanbul.esteri.it/wp-content/uploads/2025/05/PIETROCANONICAdigital_compressed.pdf) · tier S
""")),
]

for name, kw in P:
    person(name, **kw)

print(f"census r6 books_cont: {len(P)} people")
