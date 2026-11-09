# -*- coding: utf-8 -*-
# Census round 29 (5 Nov 2026) - Hellenic Parliament Library digital library (scanned plenary minutes 1910-1936). Page images read.
import json, os
from _lib import note
HERE = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(HERE, "tools", ".state", "round29")
os.makedirs(STATE, exist_ok=True)
LIB = "https://library.parliament.gr/Συλλογές/Κοινοβουλευτική-Συλλογή/Πρακτικά-Συνεδριάσεων/πρακτικά-βουλής-1910-1935"
UF = "https://www.hellenicparliament.gr/UserFiles/f3c70a23-7696-49db-9148-f24dce6a27c8/"
PDF = UF + "ΠΡΒ_Δ.ΕΘΝΟΣΥΝΕΛΕΥΣΗ_Τ.4_1923-1925.pdf"
PDF2 = UF + "ΠΡΒ_Δ.ΕΘΝΟΣΥΝΕΛΕΥΣΗ_Τ.2_1923-1925.pdf"
PDF3 = UF + "ΠΡΒ_ΠΕΡ.Δ_ΣΥΝ.Α_T.2_1933-1934_3.pdf"
JN = "Greek Parliamentarians on Kemal, 1924–1934 — Hellenic Parliament Library"
R = [{
 "id": "gonatas-1925-02-17", "voice": "Stylianos Gonatas", "voice_type": "person",
 "role": "Greek general and deputy, head of the 1922 Revolution and former Prime Minister",
 "country": "Greece", "country_now": "Greece", "domain": "military", "date": "1925-02-17", "era": "contemporary",
 "mirror": None, "polarity": "instrumental", "intensity": 1,
 "what_they_saw": "Says Kemal tirelessly rebuilt his army into a fanatical, well-supplied force, ran Turkey dictatorially, and waited for a chance to attack the Greek front.",
 "quote": "Ἐκ παραλλήλου ὅμως ὁ Κεμὰλ ἀναδιωργάνωνε συντόνως τὸν Στρατόν του. […] Πρὸς δὲ διωκεῖτο δικτατορικῶς ὑπὸ τοῦ Κεμὰλ",
 "artifact": "speech", "evidence": "P",
 "mediated_by": "As summarised in the Πρακτικά (third-person report of the speech; the quoted sentence is the recorder's wording)",
 "caveat": "Δ΄ Εθνοσυνέλευση, Πρακτικά Τόμος 4, session ΡΝ΄ of 17 Feb 1925, printed pp. 382-384 (PDF pages 193-194; page images read). The speech, on the proposed investigating committee into responsibility for the 1922 retreat, uses Kemal's strength to explain the army's collapse and to argue for dictatorship in war and democracy in peace; Kemal is a means to the speaker's argument. Session date read from the heading on p. 371; the speech is in the same sitting (no new heading between pp. 371 and 395). The index entries for Kemal under 'Δ΄ Συντακτική 1924-25' (pp. 387, 393, 395) were checked: those pages in Τ.4 are other speakers on the same debate and do not name him.",
 "node": JN, "sources": [LIB, PDF]}]

R += [{
 "id": "kondylis-1924-06-21", "voice": "Georgios Kondylis", "voice_type": "person",
 "role": "Greek general and deputy, later Prime Minister and regent",
 "country": "Greece", "country_now": "Greece", "domain": "military", "date": "1924-06-21", "era": "contemporary",
 "mirror": "chivalrous-enemy", "polarity": "admiring", "intensity": 1,
 "what_they_saw": "Calls Kemal's resistance to the Greek army 'masterly' and says comparing it shows the difference between the two sides' commanders.",
 "quote": "Ἀρκεῖ νὰ συγκρίνητε τὴν ἀριστοτεχνικὴν ἀντίστασιν τὴν ὁποίαν ὁ Μουσταφᾶ Κεμὰλ ἀντέταξε κατὰ τοῦ Ἑλληνικοῦ στρατοῦ διὰ νὰ κατανοήσητε τὴν διαφορὰν τῶν Ἀρχηγῶν.",
 "artifact": "speech", "evidence": "P",
 "mediated_by": None,
 "caveat": "Δ΄ Εθνοσυνέλευση, Πρακτικά Τόμος 2, session ΞΒ΄ of 21 June 1924 (heading on p. 354), printed pp. 361-362 (PDF pages 183-184; page images read). The passage continues Kondylis's reply in the debate on the army's responsibility for the Asia Minor defeat and sits between his rebuttal of Mazarakis (p. 361) and Minister Pangalos's reply (p. 362). The praise serves his argument that Greek command, not the soldiers, failed. Same Kondylis who is cited in 1933 as acting premier (see note); this is the only first-person view of Kemal found for him.",
 "node": JN, "sources": [LIB, PDF2]},
 {
 "id": "chatzigiannis-1934-01-26", "voice": "D. Chatzigiannis", "voice_type": "person",
 "role": "Greek deputy (initial D. as printed)",
 "country": "Greece", "country_now": "Greece", "domain": "politics", "date": "1934-01-26", "era": "contemporary",
 "mirror": "nation-forge-template", "polarity": "instrumental", "intensity": 1,
 "what_they_saw": "Holds up Kemal as a classic model of statecraft: legalised his revolt through a National Assembly while all-powerful, abolished caliphate and dynasty, paid deputies well.",
 "quote": "Τὸ παράδειγμα τοῦ Κεμάλ Μουσταφᾶ θὰ παραμείνῃ κλασσικὸν ὑπόδειγμα ἀπὸ πολιτειακῆς ἀπόψεως. Ἐπαναστατήσας εἰς τὰ βάθη τῆς Μικρᾶς Ἀσίας ἐνομιμοποίησε τὸ κίνημά του διὰ τῆς μεγάλης ἐθνοσυνελεύσεως ἐκπροσωπούσης τὴν θέλησιν τοῦ Τουρκικοῦ λαοῦ, ἐνῷ οὐσιαστικῶς αὐτὸς ἦτο παντοδύναμος.",
 "artifact": "speech", "evidence": "P",
 "mediated_by": None,
 "caveat": "Βουλή Δ΄ περίοδος Α΄ σύνοδος Τόμος 2, part 3, session ΡΑ΄ of Friday 26 Jan 1934 (heading on p. 1780), printed pp. 1828-1829 (PDF page 153; page image read; verbatim stenographic text). Said in the debate on raising deputies' allowances, which the speaker supports: Kemal is a rhetorical example (the Turkish Assembly pays its members 37,000 drachmas a month). A minor deputy; the initial D. is the only forename given.",
 "node": JN, "sources": [LIB, PDF3]}]
body = """
The Hellenic Parliament Library has scanned the plenary minutes of 1910–1936 as image PDFs (no text layer, polytonic type). Three speeches have been found in which a Greek parliamentarian gives his own view of Kemal; two are third-person summaries (marked) and one is verbatim stenography. Greek–Turkish history is sensitive: these are reported as the speakers' views, not the vault's.

## Georgios Kondylis, 21 June 1924
In the Fourth National Assembly debate on the army's responsibility for the Asia Minor defeat (session ΞΒ΄), the general answered that the Greek army 'did not fight' as it could for want of competent commanders, and added, as summarised in the Πρακτικά: 'It is enough to compare the masterly resistance that Mustafa Kemal put up against the Hellenic army to understand the difference between the commanders.' Source: Πρακτικά Τόμος 2, pp. 361–362. The praise serves his argument against the Greek command.

*Original (p. 362):* «Ἀρκεῖ νὰ συγκρίνητε τὴν ἀριστοτεχνικὴν ἀντίστασιν τὴν ὁποίαν ὁ Μουσταφᾶ Κεμὰλ ἀντέταξε κατὰ τοῦ Ἑλληνικοῦ στρατοῦ διὰ νὰ κατανοήσητε τὴν διαφορὰν τῶν Ἀρχηγῶν.»

## Stylianos Gonatas, 17 February 1925
In the same Assembly, the head of the 1922 Revolution reviewed responsibility for the collapse. As summarised in the Πρακτικά, he said that during 1922 Kemal 'reorganised his army tirelessly', that it 'was no longer the irregulars of the first days of the occupation but an army with plentiful cadres and materiel and with the fanaticism of fighting, as it saw it, for altars and hearths', and that Turkey was directed dictatorially by Kemal. Kemal then waited for the chance to attack, which the Greek army's move from Asia Minor to Thrace gave him. The speech uses this to argue that dictatorship suits armies in war and democracy suits states. Source: Τόμος 4, pp. 382–384, session ΡΝ΄ (17 Feb 1925).

*Original (p. 383):* «Καὶ ὁ Στρατὸς τοῦ Κεμὰλ δὲν ἦσαν πλέον οἱ ἀντάρται τῶν πρώτων ἡμερῶν τῆς κατοχῆς, ἀλλὰ Στρατὸς μὲ ἄφθονα στελέχη καὶ ἄφθονον ὑλικὸν καὶ μὲ τὸν φανατισμόν, ὅτι ἠγωνίζετο, κατὰ τὴν ἀντίληψίν του, ὑπὲρ βωμῶν καὶ ἑστιῶν.»

## D. Chatzigiannis, 26 January 1934
A deputy (forename initial only), arguing in the Chamber for higher parliamentary allowances, calls Kemal's example 'a classic model from the point of view of statecraft': he revolted in the depths of Asia Minor, legitimised the movement through the Grand National Assembly representing the Turkish people's will while in fact being all-powerful, abolished a centuries-old Caliphate and the dynasty of the Sultans, and gave his deputies 37,000 drachmas a month. Verbatim stenographic text, Βουλή Δ΄ περίοδος Α΄, Τόμος 2 part 3, pp. 1828–1829, session ΡΑ΄.

*Original (p. 1828):* «Τὸ παράδειγμα τοῦ Κεμάλ Μουσταφᾶ θὰ παραμείνῃ κλασσικὸν ὑπόδειγμα ἀπὸ πολιτειακῆς ἀπόψεως. Ἐπαναστατήσας εἰς τὰ βάθη τῆς Μικρᾶς Ἀσίας ἐνομιμοποίησε τὸ κίνημά του διὰ τῆς μεγάλης ἐθνοσυνελεύσεως ἐκπροσωπούσης τὴν θέλησιν τοῦ Τουρκικοῦ λαοῦ, ἐνῷ οὐσιαστικῶς αὐτὸς ἦτο παντοδύναμος.»

## What is digitised, and what was read
Scanned volumes: Γ΄ Εθνοσυνέλευση 1920–22 (5 vols), Δ΄ Εθνοσυνέλευση 1923–25 (5 vols), Βουλή 1926–35, Ε΄ Εθνοσυνέλευση 1935, Αναθεωρητική 1936, plus subject and name indexes 1909–1936 and 1946–1967. Parliament did not sit 1936–1946, so there are no November 1938 condolence speeches. The files sit behind an edge filter that refuses plain downloads; a real browser session with the library page as referer retrieves them.

Read (OCR for the word Κεμάλ and its spellings on every page, then page images of each hit and of the neighbouring pages): Δ΄ Εθνοσυνέλευση Τ.1, Τ.2, Τ.3, Τ.4 (pp. 380–395 as images), Τ.5; Γ΄ Εθνοσυνέλευση Τ.5 (both parts); Βουλή 1930–31 Σύν.Γ Τ.1 parts 1–3; Σύν.Α Τ.2 1933–34 parts 1–3; Σύν.Β 1934 parts 1–3. The Ankara agreements debate of 20 Nov 1930 (Michalakopoulos, Venizelos, Tsaldaris, Kafantaris) names only Ismet Pasha and the Turkish government; the Balkan Pact debate of 1934 and the Entente Cordiale sitting of 15 Sep 1933 (Kondylis reading Tsaldaris's telegram and greetings to the Turkish Assembly and President) contain courtesy but no stated view of Kemal. Γ΄ Τ.5 p. 2052: a deputy mentions refugees fleeing 'the pursuit of Kemal' (passing mention, no view). The index to the Γ΄ Εθνοσυνέλευση lists earlier Kemal passages (e.g. 'Ἐπίθεσις Βουλγαρίας καὶ Κεμάλ', 'Κεμαλικοὶ διωγμοί') in the 1921 volumes, not yet read.

OCR is unreliable on these polytonic scans (Κ often becomes ΙΚ or Ῥ), so a negative OCR result is weaker than a page-image read.

## Sources
- https://library.parliament.gr/Συλλογές/Κοινοβουλευτική-Συλλογή/Πρακτικά-Συνεδριάσεων/πρακτικά-βουλής-1910-1935
- https://www.hellenicparliament.gr/UserFiles/f3c70a23-7696-49db-9148-f24dce6a27c8/ΠΡΒ_Δ.ΕΘΝΟΣΥΝΕΛΕΥΣΗ_Τ.2_1923-1925.pdf (pp. 361–362)
- https://www.hellenicparliament.gr/UserFiles/f3c70a23-7696-49db-9148-f24dce6a27c8/ΠΡΒ_Δ.ΕΘΝΟΣΥΝΕΛΕΥΣΗ_Τ.4_1923-1925.pdf (pp. 382–384)
- https://www.hellenicparliament.gr/UserFiles/f3c70a23-7696-49db-9148-f24dce6a27c8/ΠΡΒ_ΠΕΡ.Δ_ΣΥΝ.Α_T.2_1933-1934_3.pdf (pp. 1828–1829)
"""
note("Events", JN, {"type": "event", "when": "1924-1934", "tags": ["event", "verified", "greece", "parliament"]}, body)

# ---- second batch (Γ΄ Εθνοσυνέλευση 1921-22 and Βουλή 1932) ----
PDFE1 = UF + "ΠΡΒ_Γ.ΕΘΝΟΣΥΝΕΛΕΥΣΗ_Τ.1_1920-1922.pdf"
PDFE4 = UF + "ΠΡΒ_Γ.ΕΘΝΟΣΥΝΕΛΕΥΣΗ_Τ.4_1920-1922.pdf"
PDFS2 = UF + "newΠΡΒ_ΠΕΡ.Β_ΣΥΝ.Δ_T.1_1931-1932_2.pdf"
JN2 = "Greek Deputies on Kemal, 1921–1932 — Hellenic Parliament Library"
SUM = "As summarised in the Πρακτικά (third-person report of the speech; the quoted sentence is the recorder's wording)"
def rec2(id, voice, role, dom, date, pol, mirror, saw, quote, art, med, cav, src):
    return {"id": id, "voice": voice, "voice_type": "person", "role": role, "country": "Greece", "country_now": "Greece",
            "domain": dom, "date": date, "era": "contemporary", "mirror": mirror, "polarity": pol, "intensity": 1,
            "what_they_saw": saw, "quote": quote, "artifact": art, "evidence": "P", "mediated_by": med,
            "caveat": cav, "node": JN2, "sources": src}
R2 = [
 rec2("antoniadis-1921-04-01", "A. Antoniadis", "Greek deputy (initial A. as printed)", "politics", "1921-04-01", "hostile", None,
  "Urges taking Eskişehir to cut the enemy's communications and make Kemal harmless, and 'Let Kemal be crushed' as every Greek's watchword.",
  "καὶ προσθέτει ὅτι τὸ σύνθημα πάντων τῶν Ἑλλήνων πρέπει νὰ εἶναι: «Κατασυντριβήτω ὁ Κεμάλ».",
  "speech", SUM,
  "Γ΄ Εθνοσυνέλευση, Πρακτικά Τόμος 1, session ΚΘ΄ of 1 April 1921 (heading p. 476), printed p. 485 (PDF page 243; page image read). Third-person summary of a deputy's speech in the debate on the Allied (London) proposals to revise the Treaty of Sèvres; the Cato 'Delenda Carthago' slogan is his. Minor deputy; forename not given.",
  [LIB, PDFE1]),
 rec2("matesis-1922-05-18", "A. Matesis", "Greek deputy and interpellator on the Christian massacres in Asia Minor (initial A. as printed)", "politics", "1922-05-18", "hostile", None,
  "Says Kemal repaid Pontic Greeks' protection of Muslims with the horrific tragedy of Pontus, and called his note to the High Commissioners ironic and insolent.",
  "Τὴν ἀμοιβὴν διὰ τὰς ὑπηρεσίας ταύτας ἔδωκεν ὁ Κεμὰλ διὰ τῆς φρικιαστικῆς τραγῳδίας τοῦ πολυπαθοῦ Πόντου.",
  "speech", SUM,
  "Γ΄ Εθνοσυνέλευση, Πρακτικά Τόμος 4, session ΞΖ΄ of 18 May 1922 (heading read from a thumbnail of the page), printed pp. 2621-2622 (PDF pages 144-145; page images read). Matesis interpellates, with Tsoukalas and Sotiriadis, on the massacres of Christians by the 'Kemalists'; the summary has him blame Kemal personally for Pontus and describe Kemal's letter of 15 Feb 1922 to the three High Commissioners as written 'with excessive irony and insolence'. Greek war-time parliamentary rhetoric; the vault does not adopt its framing.",
  [LIB, PDFE4]),
 rec2("tsaldaris-1932-03-31", "Panagis Tsaldaris", "Leader of the People's Party, later Prime Minister", "politics", "1932-03-31", "instrumental", None,
  "Tells Venizelos that Kemal, sworn to the National Pact, lost no war material under Venizelos's treaty and accepted none of the compromises offered.",
  "Γνωρίζετε ἐν τούτοις, κύριε Πρόεδρε τῆς Κυβερνήσεως, τὸ Ἐθνικὸν Συμβόλαιον τοῦ Κεμάλ, καὶ γνωρίζετε ἀκόμη ὅτι διὰ τῆς συνθήκης, τὴν ὁποίαν σεῖς εἴχατε κάμει, αὐτὸς δὲν ἐστερήθη οὐδενὸς ὑλικοῦ πρὸς ἐξακολούθησιν τῆς ἐκστρατείας. Δυστυχῶς ὁ Κεμὰλ οὐδὲν ἐκ τούτων ἐδέχετο.",
  "speech", None,
  "Βουλή Β΄ περίοδος Δ΄ σύνοδος, Τόμος 1 part 2, session Ν΄ of Thursday 31 March 1932, printed p. 660 (PDF page 137; page image read; verbatim stenography). The two sentences are about 20 lines apart (the first runs to the end of the left column, the second is in the right column). In the 1920-22 policy debate with Prime Minister Venizelos, Tsaldaris argues that agreeing terms with Kemal was never easy; Kemal is a means to his argument. Venizelos's reply (p. 671) only reports Tsaldaris's suggestion of peace with Kemal and states no view of Kemal; not staged.",
  [LIB, PDFS2]),
]
R += R2
body2 = """
Three more Greek parliamentary voices on Kemal, from the Γ΄ Εθνοσυνέλευση of 1921–22 and the Chamber of 1932. The Greek is verbatim from the page images; Antoniadis and Matesis are third-person summaries in the Πρακτικά, Tsaldaris is verbatim stenography. This is wartime and party rhetoric on a sensitive subject, reported as the speakers' views, not the vault's.

## A. Antoniadis, 1 April 1921
In the debate on the Allied proposals to revise the Treaty of Sèvres (session ΚΘ΄), a deputy urged that the army take Eskişehir, cut the enemy's communications and so 'make Kemal harmless', and ended with the Roman Cato's 'Carthage must be destroyed' as a model for the Greeks' watchword: 'Let Kemal be crushed.' Source: Τόμος 1, p. 485. Minor deputy.

*Original:* «καὶ προσθέτει ὅτι τὸ σύνθημα πάντων τῶν Ἑλλήνων πρέπει νὰ εἶναι: «Κατασυντριβήτω ὁ Κεμάλ».»

## A. Matesis, 18 May 1922
Interpellating, with Tsoukalas and Sotiriadis, on the massacres of Christians by the 'Kemalists', Matesis said that the Greeks of Trebizond and the Church had sheltered their Muslim fellow-citizens in the world war, and that 'Kemal gave the reward for these services through the horrific tragedy of long-suffering Pontus.' He added that Kemal's letter of 15 February 1922 to the three High Commissioners, saying the measures were meant to put down a revolt, was written with excessive irony and insolence. Source: Τόμος 4, pp. 2621–2622, session ΞΖ΄.

*Original (p. 2621):* «Τὴν ἀμοιβὴν διὰ τὰς ὑπηρεσίας ταύτας ἔδωκεν ὁ Κεμὰλ διὰ τῆς φρικιαστικῆς τραγῳδίας τοῦ πολυπαθοῦ Πόντου.»

## Panagis Tsaldaris, 31 March 1932
Leader of the People's Party, answering Prime Minister Venizelos on the policy of 1920–22: Kemal held to the National Pact; the treaty Venizelos made left him not deprived of anything needed to continue the campaign; and 'unfortunately Kemal accepted none of this' (the compromises over Thrace and Asia Minor that the Greek government offered Britain). The point serves his argument against Venizelos's hindsight. Source: Βουλή, Τόμος 1 part 2, p. 660, session Ν΄.

*Original:* «Γνωρίζετε ἐν τούτοις, κύριε Πρόεδρε τῆς Κυβερνήσεως, τὸ Ἐθνικὸν Συμβόλαιον τοῦ Κεμάλ, καὶ γνωρίζετε ἀκόμη ὅτι διὰ τῆς συνθήκης, τὴν ὁποίαν σεῖς εἴχατε κάμει, αὐτὸς δὲν ἐστερήθη οὐδενὸς ὑλικοῦ πρὸς ἐξακολούθησιν τῆς ἐκστρατείας. Δυστυχῶς ὁ Κεμὰλ οὐδὲν ἐκ τούτων ἐδέχετο.»

## Read and not counted
These name Kemal or 'the Kemalists' without a view of Kemal himself: Γ΄ Τόμος 1 (session ΚΖ΄ p. 453, Tsoukalas quoting Curzon that Venizelos proposed to crush Kemal with 100,000 men; session ΚΗ΄ p. 464, P. Argyropoulos calling the Kemalists the Young Turk Committee under another name; session ΚΑ΄ p. 292, a rhetorical question about Kemal's concentrated forces; Vasilakakis p. 379 on Kemalist atrocities); Γ΄ Τόμος 4 (Baltatzis, Foreign Minister, 18 May 1922, pp. 2611–2614, on 'Kemalist savagery' and the 'Independence Courts'; Tsoukalas p. 2625 reading an Istanbul paper that calls Kemal and his circle malefactors; p. 2914 a passing mention); Βουλή 1932 p. 671 (Venizelos reporting Tsaldaris's proposal); Βουλή 1934 p. 1828 (Chatzigiannis, in the first note). Δ΄ Τόμος 3, 5 and the 1930–31 and 1931–32 volumes otherwise show no Kemal.

## Sources
- https://library.parliament.gr/Συλλογές/Κοινοβουλευτική-Συλλογή/Πρακτικά-Συνεδριάσεων/πρακτικά-βουλής-1910-1935
- https://www.hellenicparliament.gr/UserFiles/f3c70a23-7696-49db-9148-f24dce6a27c8/ΠΡΒ_Γ.ΕΘΝΟΣΥΝΕΛΕΥΣΗ_Τ.1_1920-1922.pdf (p. 485)
- https://www.hellenicparliament.gr/UserFiles/f3c70a23-7696-49db-9148-f24dce6a27c8/ΠΡΒ_Γ.ΕΘΝΟΣΥΝΕΛΕΥΣΗ_Τ.4_1920-1922.pdf (pp. 2621–2622)
- https://www.hellenicparliament.gr/UserFiles/f3c70a23-7696-49db-9148-f24dce6a27c8/newΠΡΒ_ΠΕΡ.Β_ΣΥΝ.Δ_T.1_1931-1932_2.pdf (p. 660)
"""
note("Events", JN2, {"type": "event", "when": "1921-1932", "tags": ["event", "verified", "greece", "parliament"]}, body2)
with open(os.path.join(STATE, "gazes_grparl.jsonl"), "w", encoding="utf-8") as f:
    for r in R: f.write(json.dumps(r, ensure_ascii=False) + "\n")
print(len(R), "records")
