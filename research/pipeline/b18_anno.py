# -*- coding: utf-8 -*-
# Census round 10 (Nov 2026), slug anno — German and Austrian press and officials, 1924-1933.
# Seams: ANNO search REST (anno.onb.ac.at/anno-suche/rest/search/{simple,complex,snippet}), no key;
# Deutsche Digitale Bibliothek newspaper Solr (api.deutsche-digitale-bibliothek.de/search/index/
# newspaper-issues/select, field plainpagefulltext, no key, full page OCR). ANNO page images/OCR text
# (digital.onb.ac.at, cgi-content/anno) are blocked (Turnstile / TLS reset), so ANNO quotes are
# single-OCR search-index text; DDB items were cross-read in several papers or at page level.
import json, os
from _lib import note, person

D = "https://www.deutsche-digitale-bibliothek.de/newspaper/item/"
A = "https://anno.onb.ac.at/cgi-content/anno?aid="

NADOLNY_Q = "Ich komme von einem neuen Deutschland zu einer neuen Türkei."
NADOLNY_Q2 = "Das deutsche Volk hat das Schicksal des türkischen Volkes in diesen letzten Jahren mit lebhafter und herzlicher Anteilnahme und mit dem Gefühl der Bewunderung verfolgt."
PAPEN_Q = "Damit haben Ew. Exzellenz manch anderem Volke ein Vorbild gegeben."
PAPEN_Q2 = "Ich und viele Deutsche, die die Ehre hatten, mit Ihnen und unter Ihrer Führung zu kämpfen, erinnern sich mit Stolz der ausgezeichneten Waffenbrüderschaft"
V26_Q = "Sie ist nicht nur gegen den Diktator, sondern zugleich gegen seine innere und äußere Politik gerichtet."
V26_Q2 = "das herrschende Diktaturregime alles andere ist als eine Republik"
V29_Q = "Kemal doch ihr „Präsident\", ein typischer Diktator"
V29_Q2 = "Unterdrückung der Presse und der bürgerlichen Freiheiten ist eine der schneidigsten Waffen in ihrer Hand."
AZ24_Q = "politisch konterrevolutionäre Macht geblieben ist und daß Mustafa Kemal, um die von ihm gegründete Republik zu verteidigen, auch die"
AZ30_Q = "der türkische Diktator Kemal-Pascha"
AZ30_Q2 = "Und Kemal-Pascha sitzt mit den Führern der Opposition gegen seine Partei freundschaftlich beisammen, ermutigt sie"

S_NAD = [
 D + "ZUITNJRLCN7JKLURZWDEKBZOREYKQKX2?issuepage=3",
 D + "JT7BKOJKP7HPVLA5FOTHMKHRWKKUNZWL?issuepage=9",
 D + "CDLZ7KDOZQ2NVMQ5IJR52RPFM6IIVANB?issuepage=2"]
S_PAP = [
 D + "FJKUMZ355YLKP7DLCPEKBHDTRBAE7U7V?issuepage=2",
 D + "IL6KPVDUX4BMVKLVT3ABTDMZJDRSN2JR?issuepage=10",
 D + "VQG446GIV37B2LZDN5GHHE4XPCE2WQVC?issuepage=1",
 D + "U7JKQWQMXIZ4G7JUD73BXNU26UDKOSOO?issuepage=2"]
S_V26 = [D + "2QALXUBTAMK5NG63CL5GEJTUMGDJT7MT?issuepage=1"]
S_V29 = [D + "FVBL7RQAXCYGG25XHRW7YH5B7ZNCGEBY?issuepage=5"]
S_AZ24 = [A + "aze&datum=19240307&seite=2"]
S_AZ30 = [A + "aze&datum=19300821&seite=2"]

N1 = "German Statesmen Address Kemal, 1924 and 1933"
N2 = "Vorwärts and the Arbeiter-Zeitung on the Dictator, 1924–1930"

REC = [
 dict(id="nadolny-1924-06-17", voice="Rudolf Nadolny", voice_type="person",
  role="German envoy (ambassador) to Turkey, presenting credentials", country="Germany", country_now="Germany",
  domain="diplomacy", date="1924-06-17", era="contemporary", mirror=None, polarity="instrumental", intensity=2,
  what_they_saw="Told Kemal the German people had followed Turkey's fate 'with a feeling of admiration' and came from a new Germany to a new Turkey.",
  quote=NADOLNY_Q2, artifact="speech", evidence="P", mediated_by="WTB wire text, printed in Vorwärts 19 Jun 1924 p. 3, Kölnische Zeitung 19 Jun 1924 p. 9, Rheinische Volkswacht 20 Jun 1924 p. 2",
  caveat="Credentials speech: diplomatic register, so recorded as instrumental although the wording is admiring. 'Rudolf' Nadolny identified from the post, not from the wire text (one paper's caption misprints 'Gustav'). Kölnische Zeitung OCR; the other two agree.",
  node=N1, sources=S_NAD),
 dict(id="papen-1933-10-28", voice="Franz von Papen", voice_type="person",
  role="German Vice-Chancellor, telegram on the Republic's tenth anniversary", country="Germany", country_now="Germany",
  domain="politics", date="1933-10-28", era="contemporary", mirror="nation-forge-template", polarity="admiring", intensity=2,
  what_they_saw="Said Kemal's Turkey had given other peoples 'a model' by drawing on its own cultural strengths; recalled German 'brotherhood in arms' under his command.",
  quote=PAPEN_Q, artifact="telegram", evidence="P", mediated_by="Wire text (WTB, Berlin 28 Oct 1933) printed in Süddeutsche Zeitung, Kölnische Zeitung, Schwäbischer Merkur, Münsterländische Volkszeitung 30-31 Oct 1933",
  caveat="Congratulatory telegram: praise is also diplomacy. The wire text is read in four papers' separate OCR; the quote is identical in all.",
  node=N1, sources=S_PAP),
 dict(id="vorwaerts-1926-07-24", voice="Vorwärts", voice_type="press",
  role="Berlin daily, central organ of the SPD", country="Germany", country_now="Germany",
  domain="press", date="1926-07-24", era="contemporary", mirror=None, polarity="conflicted", intensity=2,
  what_they_saw="Front-page analysis of the İzmir verdict: called the regime a dictatorship 'anything but a republic' and the opposition aimed at the dictator and his policy.",
  quote=V26_Q, artifact="article", evidence="P", mediated_by=None,
  caveat="Signed Dr. Artasches Abeghian, on Vorwärts's front page; the paper's stance is read from the piece, which also explains the opposition's monarchist and reactionary character. Single OCR (Deutsche Digitale Bibliothek / FES), legible; page image not re-read.",
  node=N2, sources=S_V26),
 dict(id="vorwaerts-1929-01-10", voice="Vorwärts", voice_type="press",
  role="Berlin daily, central organ of the SPD", country="Germany", country_now="Germany",
  domain="press", date="1929-01-10", era="contemporary", mirror=None, polarity="conflicted", intensity=2,
  what_they_saw="Cast Kemal as the lead 'enlightened absolutist' of the Near East: radical Europeanizer, but a 'typical dictator' who suppresses press and civil freedoms.",
  quote=V29_Q2, artifact="article", evidence="P", mediated_by=None,
  caveat="Unsigned feature 'Europa revolutioniert Vorderasien', p. 5. The piece compares Kemal with Peter and Frederick the Great; polarity is the note's reading of both strands. Single OCR; 'Presie' normalised to 'Presse'.",
  node=N2, sources=S_V29),
 dict(id="arbeiter-zeitung-1924-03-07", voice="Arbeiter-Zeitung (Vienna)", voice_type="press",
  role="Vienna daily, central organ of the Social Democratic Party", country="Austria", country_now="Austria",
  domain="press", date="1924-03-07", era="contemporary", mirror=None, polarity="admiring", intensity=2,
  what_they_saw="Explained the abolition of the Caliphate as Kemal defending his republic against a politically counter-revolutionary power, and Turkey's drive toward progress.",
  quote=AZ24_Q, artifact="article", evidence="P", mediated_by=None,
  caveat="Sympathetic framing rather than personal praise; polarity inferred from the framing. ANNO page text and images could not be opened (bot gate), so the quote is the search-index OCR fragment, fixed by two different search windows; page image not re-read. Subject of the clause (the Caliphate) is read from the neighbouring snippet.",
  node=N2, sources=S_AZ24),
 dict(id="arbeiter-zeitung-1930-08-21", voice="Arbeiter-Zeitung (Vienna)", voice_type="press",
  role="Vienna daily, central organ of the Social Democratic Party", country="Austria", country_now="Austria",
  domain="press", date="1930-08-21", era="contemporary", mirror=None, polarity="conflicted", intensity=2,
  what_they_saw="Called him 'the Turkish dictator' yet reported him sitting amicably with the opposition leaders of the new Free Party and encouraging them.",
  quote=AZ30_Q, artifact="article", evidence="P", mediated_by=None,
  caveat="Dateline Istanbul, mid-August, from Yalova; headline too garbled in OCR to quote. ANNO page not openable (bot gate): fragment from the search index only, page image not re-read. Hyphenation 'Kemal- Pascha' rejoined.",
  node=N2, sources=S_AZ30),
]

note("Events", N1, {"type": "event", "when": "17 June 1924 and 28 October 1933",
     "tags": ["event", "verified", "german", "diplomacy"]}, """
Two German official voices, nine years apart, both printed from the same news-agency wire in several
dailies. Neither is a private opinion: one is a credentials speech, the other a congratulatory telegram.
That is why they are recorded as an instrumental and an admiring gaze with the register named.

- **Rudolf Nadolny, 17 June 1924 (Ankara).** The German envoy, presenting his letter of credence to
  the President, began *"Ich komme von einem neuen Deutschland zu einer neuen Türkei."* ("I come from a
  new Germany to a new Turkey", tr.) and said: *"Das deutsche Volk hat das Schicksal des türkischen Volkes in diesen letzten Jahren mit lebhafter und herzlicher Anteilnahme und mit dem Gefühl der Bewunderung verfolgt."* ("The German people have followed the fate of the Turkish people in these last years with lively and warm sympathy and with a feeling of admiration", tr.). The speech reopens official relations; the
  wording is courtesy that also states a German hope for a partner. Text from the WTB wire:
  Vorwärts 19 Jun 1924, p. 3; Kölnische Zeitung 19 Jun 1924, p. 9; Rheinische Volkswacht 20 Jun 1924, p. 2
  (three separate OCR runs agree on the passage, apart from OCR noise). Kemal's reply follows in the
  same reports and is not used here.
- **Franz von Papen, 28 October 1933 (Berlin).** The Vice-Chancellor wired the Republic's tenth-anniversary
  greeting: *"Unter Ihnen hat die tapfere osmanische Nation sich auf ihre eigensten kulturellen
  Kraftquellen besonnen und daraus neue Stärke und neue Energien für den Wiederaufstieg geschöpft. Damit
  haben Ew. Exzellenz manch anderem Volke ein Vorbild gegeben."* ("Under you the brave Ottoman nation
  has recalled its own cultural sources of strength and drawn from them new strength and new energy for
  its rise. In doing so Your Excellency has given many another people a model", tr.). He added that he
  and *"viele Deutsche, die die Ehre hatten, mit Ihnen und unter Ihrer Führung zu kämpfen"* remembered
  with pride *"der ausgezeichneten Waffenbrüderschaft"* ("the excellent brotherhood in arms", tr.).
  Printed 30–31 October 1933 in Süddeutsche Zeitung p. 1, Kölnische Zeitung p. 10, Schwäbischer Merkur p. 2
  and Münsterländische Volkszeitung p. 2; the text is identical in all four.

**Reading.** Both men speak as the Weimar and the Nazi-era German state, and both reach for the Great
War: Nadolny for a Germany reborn, Papen for a shared front. Papen's phrase *Vorbild* ("model") puts
Kemal's Turkey inside the same German story as [[Hitler's Atatürk, 1933–1938]], five months after
Hitler took office. Papen later served as ambassador in Ankara (1939–44), outside this card's
period. See [[Otto Liman von Sanders]] for the earlier German command on the Turkish front.

## Sources
- WTB wire, Angora 17 Jun 1924, as printed: Vorwärts (Berlin) 19 Jun 1924, p. 3 · P — [Deutsche Digitale Bibliothek](""" + S_NAD[0] + """)
- Kölnische Zeitung 19 Jun 1924, p. 9 · P — [DDB](""" + S_NAD[1] + """)
- Rheinische Volkswacht 20 Jun 1924, p. 2 · P — [DDB](""" + S_NAD[2] + """)
- WTB wire, Berlin 28 Oct 1933, as printed: Münsterländische Volkszeitung 30 Oct 1933, p. 2 · P — [DDB](""" + S_PAP[0] + """)
- Kölnische Zeitung 30 Oct 1933, p. 10 · P — [DDB](""" + S_PAP[1] + """)
- Süddeutsche Zeitung 30 Oct 1933, p. 1 · P — [DDB](""" + S_PAP[2] + """)
- Schwäbischer Merkur 31 Oct 1933, p. 2 · P — [DDB](""" + S_PAP[3] + """)
- Access: Deutsche Digitale Bibliothek newspaper index (`api.deutsche-digitale-bibliothek.de/search/index/newspaper-issues/select`, field `plainpagefulltext`), page OCR text; quotes normalised for OCR spacing and hyphenation only.
""")

note("Events", N2, {"type": "event", "when": "March 1924 – January 1929",
     "tags": ["event", "verified", "german", "austrian", "press", "hostile-gazes"]}, """
The two great Social Democratic dailies of the German-speaking world read Kemal as a modernizer who
was also a dictator. Neither paper is hostile to the reforms; both are uneasy with the method.

- **Arbeiter-Zeitung (Vienna), 7 March 1924, p. 2.** On the abolition of the Caliphate the paper's
  analysis (OCR fragment) says the Caliphate had remained a *"politisch konterrevolutionäre Macht geblieben ist und daß Mustafa Kemal, um die von ihm gegründete Republik zu verteidigen, auch die"* (the clause breaks off there; "remained a politically counter-revolutionary power, and that Kemal, to defend the republic he founded, also …", tr.). The
  neighbouring snippets (OCR heavily damaged) say he first tried to win the religious authority of the
  Caliphate for the new republic, and set the move against a people held back by ignorance and
  fanaticism; the paper's line is that Europeanization justifies the step. No praise of the man, but no
  protest. See [[Abolition of the Caliphate]].
- **Vorwärts (Berlin), 24 July 1926, p. 1.** Front-page article *"Der Kampf um Kemal. Die Hintergründe des
  Urteils von Smyrna"*, by Dr. Artasches Abeghian, on the İzmir verdict (15 death sentences). It reads the
  opposition as monarchist, Young Turk and clerical: *"Sie ist nicht nur gegen den Diktator, sondern
  zugleich gegen seine innere und äußere Politik gerichtet."* ("It is directed not only against the
  dictator but equally against his domestic and foreign policy", tr.), and calls the system *"das herrschende
  Diktaturregime"*, which is *"alles andere … als eine Republik"* ("anything but a republic", tr.). It also
  says his reforms *"oft auf soziale und kulturelle Rückständigkeit des Landes keine Rücksicht nehmen"*
  ("often take no account of the country's social and cultural backwardness", tr.) in the
  opposition's account. Hostile to the system, unsparing about the opposition. See [[Independence Tribunals]].
- **Vorwärts, 10 January 1929, p. 5.** Feature *"Europa revolutioniert Vorderasien — Gegen Turban, Harem,
  Schleier, Fez"*: Kemal is *"der Alleinherrscher der Türkei"*, *"ein typischer Diktator"*, first among the
  region's *"aufgeklärte Monarchen"* in the pace of reform. Reform is carried by an *"radikalen
  Rationalismus"* that is intolerant of minorities, and *"Unterdrückung der Presse und der bürgerlichen
  Freiheiten ist eine der schneidigsten Waffen in ihrer Hand."* ("suppression of the press and of civil
  freedoms is one of their sharpest weapons", tr.). A conflicted reading: Peter-the-Great Europeanizer and
  dictator.
- **Arbeiter-Zeitung, 21 August 1930, p. 2.** From Istanbul: *"der türkische Diktator Kemal-Pascha"* spends
  the summer at Yalova, and the paper reports that *"Kemal-Pascha sitzt mit den Führern der Opposition
  gegen seine Partei freundschaftlich beisammen, ermutigt sie"* ("sits with the leaders of the
  opposition to his own party in friendly company and encourages them", tr.) — the Free Party episode.

**Reading.** The word "Diktator" is the Social Democrats' own, used neutrally and as a charge. On
quality and reach these are the first Austrian and SPD-centre voices in the dataset. Thin: the 1924 and 1930
Vienna pieces rest on search-index OCR (the ANNO page viewer is gated), and the 1926 and 1929 Berlin pieces
on a single DDB OCR each.

## Sources
- Vorwärts (Berlin) 24 Jul 1926, p. 1, "Der Kampf um Kemal" · P — [DDB](""" + S_V26[0] + """)
- Vorwärts 10 Jan 1929, p. 5, "Europa revolutioniert Vorderasien" · P — [DDB](""" + S_V29[0] + """)
- Arbeiter-Zeitung (Vienna) 7 Mar 1924, p. 2 · P — [ANNO](""" + S_AZ24[0] + """) (search-index snippet via `anno.onb.ac.at/anno-suche/rest/search/snippet?documentId=ANNO_aze19240307`)
- Arbeiter-Zeitung 21 Aug 1930, p. 2 · P — [ANNO](""" + S_AZ30[0] + """) (snippet, `ANNO_aze19300821`)
- OCR note: Vorwärts quotes are single-OCR from the Friedrich-Ebert-Stiftung scan via DDB, with "Presie" read as "Presse" and line-break hyphens joined; Arbeiter-Zeitung quotes are fragments from the ANNO search index, hyphenation rejoined.
""")

person("Franz von Papen", role="German Vice-Chancellor (1933–34), later ambassador in Ankara", nat="German",
       life="1879–1969", stance="invoked the Great War alliance",
       tags=["german", "diplomacy"], body="""
Vice-Chancellor of Hitler's first cabinet. On 28 October 1933 he telegraphed Kemal on the Republic's tenth
anniversary, saying Kemal's Turkey had given other peoples "ein Vorbild" and recalling the German
"Waffenbrüderschaft" under Kemal's command. Full text and sources on [[German Statesmen Address Kemal, 1924 and 1933]].

## Sources
- See [[German Statesmen Address Kemal, 1924 and 1933]] (four newspaper reprints of the wire text, 30–31 Oct 1933).
""")
person("Rudolf Nadolny", role="German diplomat, first postwar envoy (ambassador) to Turkey", nat="German",
       life="1873–1953", stance="courteous, admiring in form",
       tags=["german", "diplomacy"], body="""
On 17 June 1924 he presented his credentials to Kemal at Angora, speaking of a "neuen Deutschland" meeting a
"neuen Türkei" and of the German people's "Gefühl der Bewunderung". See [[German Statesmen Address Kemal, 1924 and 1933]].

## Sources
- See [[German Statesmen Address Kemal, 1924 and 1933]] (WTB text in Vorwärts, Kölnische Zeitung, Rheinische Volkswacht, 19-20 Jun 1924).
""")

if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tools", ".state", "round10")
    os.makedirs(out, exist_ok=True)
    keys = ["id","voice","voice_type","role","country","country_now","domain","date","era","mirror","polarity",
            "intensity","what_they_saw","quote","artifact","evidence","mediated_by","caveat","node","sources"]
    with open(os.path.join(out, "gazes_anno.jsonl"), "w", encoding="utf-8") as f:
        for r in REC:
            assert len(r["what_they_saw"].split()) <= 25, r["id"]
            f.write(json.dumps({k: r[k] for k in keys}, ensure_ascii=False) + "\n")
