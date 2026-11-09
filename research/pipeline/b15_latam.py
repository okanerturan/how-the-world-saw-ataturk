# -*- coding: utf-8 -*-
# Census round 7 (Oct 2026) — Spanish-language contemporary press 1922-1935, read as page OCR from
# Chronicling America (Library of Congress, free) and the Internet Archive newspaper collections.
from _lib import note

CA = ("Library of Congress, *Chronicling America* (free, public domain), page OCR retrieved Oct 2026 via the "
      "loc.gov collection search (`fa=language:spanish`) and the `tile.loc.gov` text service")

E1 = """
Latin America's own newspapers are walled off (Brazil's CAPTCHA, UFDC login), but the **Spanish-language
press of the United States** was written for Mexican, Puerto Rican, Cuban and Spanish immigrant readers
and sits open in *Chronicling America*. Searching its Spanish-language pages for "Mustafá Kemal" returns
dozens of 1922–23 wire reports (Smyrna, Chanak, Mudanya, in *El Mundo* and *El Imparcial* of San Juan and
*La Prensa* of San Antonio). Those are agency copy. This card keeps only the **pieces with a view** —
profiles, columns and editorial-page items — read as page OCR. Quotations are from the OCR text (line-break
hyphenation joined); the OCR is rough, so every quote was restricted to a phrase that survives it.

**1922–23: the Napoleon and the saviour.**
- *El Imparcial* (San Juan, Puerto Rico), 11 Nov 1922, p. 4, "El Caudillo de Angora: Mustafá Kemal": Turkey
  "the first of the sold peoples to rise"; Kemal sober and silent, condemning "las locuras panturcas" and
  wanting a Turkey "que no sojuzgue ni sea sojuzgada"; hauled before a hostile Parliament he is, in the
  words printed, "aclamado como salvador"; "the Islam, ailing, waits on Mustafá". The byline reads
  "Camie Rerría" in the OCR (unresolved). The earliest Puerto Rican gaze in the census.
- *La Prensa* (San Antonio), 27 Nov 1922, p. 3, "Con Mustafá Kemal": a Paris dispatch reprinting Ricardo
  Eaton's account (from the "Revista Semanaria") of reaching Smyrna on 12–13 September, the day of the
  fire. Refugees "hungry, thirsty, wretched", Armenians "shot by hundreds"; and, in the same piece, Kemal
  "el dios del día", slim, in khaki, "the impression of a European chief", who "tiene un guía: Napoleón".
  The seeing is a Frenchman's; the Texan paper's choice to print it is what is recorded.
- *El Tucsonense* (Tucson), 17 Feb 1923, p. 7, Sección Editorial, "¿Quién es Mustafá Kemal Pashá?": a
  Spanish-Jewish ancestry legend, German military schooling, and the verdict that he is a "real dictador",
  the "esperanza y el terror" of nations broken by war; no one has yet called him "el Napoleón del Cercano
  Oriente", the writer says, but journalists will. Awe with an edge of alarm.

**1926–1930: the columnists turn on the Dictator.**
- *La Opinión* (Los Angeles, Mexican-exile readership), 27 Oct 1926, p. 2, "Los Napoleones de Papel Cartón":
  Kemal as the European-educated democrat who "acaba de dar un gigantesco paso atrás" by proposing polygamy,
  the Revolution betrayed for "el serrallo". The claim itself is unsupported here — it is what the paper
  printed, a rumour in 1926 Los Angeles. The hostile reading is the point.
- *La Opinión*, 26 Jul 1928, p. 3, column signed "Marco Polo": "Mustaphá Kemal es un dictador ante quien"
  Mussolini, Pilsudski and Primo de Rivera "son todavía hijos de la Democracia"; then a long extract from
  *Le Temps* describing one party, no opposition, an entirely official press.
- *La Opinión*, 3 Feb 1929, p. 2, Angora dispatch: Kemal can be argued with, but "no cabe negarle que es el
  campeón de la renovación"; fez, veil and Latin alphabet are the proof, enforced by "la espada del dictador".
- *La Opinión*, 16 May 1929, p. 3, "Crónica de Turquía" by **Pedro Maco**, "Especial para La Opinión": the
  tourist correspondents see hats and palaces; beyond that Kemal is "un batallador", an iron will and, as
  the saviour of the country, "la fuerza de un símbolo", though a reactionary force persists.
- *La Gaceta* (Tampa), 14 Oct 1930, p. 1: "Turquía es una 'república' por el presidente Kemal Pacha";
  the opposition party moved to make him "presidente perpetuo", he refused, "pero él sabe que será
  presidente hasta que le convenga" (OCR-damaged). Tampa's column files Kemal in a list of Latin dictators
  (Mussolini, Pilsudski, Leguía, Ibáñez, Stalin) on 27 Jun 1930.

**1935: Kemal as an argument in Spanish Republican politics.** *La Gaceta* (Tampa), 21 Feb 1935, p. 1, column
"Changas y Chungas": in the Turkish Assembly 16 of 17 deputies (the column's count) are educated women and the
17th a peasant mayor. "La Dictadura produjo el milagro. Esclavas ayer, hoy mujeres 'libres'." But "Mustafá
Kemal las llamó a la Asamblea y mañana, si así lo quiere, puede devolverlas al hogar o la cocina; pero la
República española no pudo hacer lo mismo cuando comprobó su error. La Dictadura crea y destruye a su gusto
y conveniencia; la democracia ha de medir sus pasos." Kemal as a case in an argument about the Spanish
Republic's women's vote, admired for the outcome and warned against for the method.

What the cluster shows: the Spanish-language Americas received Kemal first as a wire-service **Napoleon**
(1922–23), then, from the mid-1920s, as a **Dictator** — admired for the reforms, distrusted for the means.
The "emancipator" language (veil, vote, alphabet) is present from 1929 and so is its price.

**Dug, not recorded:** wire reports (the Nov 1938 Laredo and Tampa death notices, Aug 1928 "Latin alphabet"
dispatch in *El Tucsonense*, UP stories in *La Opinión* of 1929–33 incl. 13 May 1931 "Las mujeres de
Turquía han votado contra su emancipador", 7 Jun 1930 translated "Mustafa Kemal, un gran hombre de Estado,
habla con un gran historiador", 14 Jun 1929 "Las mujeres turcas") — informative, but agency or translated
copy with no identifiable voice.

## Sources
- """ + CA + """. Pages (all `https://www.loc.gov/resource/<lccn>/<date>/ed-1/?sp=<n>`):
  [El Imparcial, 11 Nov 1922, p. 4](https://www.loc.gov/resource/sn88073003/1922-11-11/ed-1/?sp=4) ·
  [La Prensa, 27 Nov 1922, p. 3](https://www.loc.gov/resource/sn83045395/1922-11-27/ed-1/?sp=3) ·
  [El Tucsonense, 17 Feb 1923, p. 7](https://www.loc.gov/resource/sn95060694/1923-02-17/ed-1/?sp=7) ·
  [La Opinión, 27 Oct 1926, p. 2](https://www.loc.gov/resource/sn81004351/1926-10-27/ed-1/?sp=2) ·
  [La Opinión, 26 Jul 1928, p. 3](https://www.loc.gov/resource/sn81004351/1928-07-26/ed-1/?sp=3) ·
  [La Opinión, 3 Feb 1929, p. 2](https://www.loc.gov/resource/sn81004351/1929-02-03/ed-1/?sp=2) ·
  [La Opinión, 16 May 1929, p. 3](https://www.loc.gov/resource/sn81004351/1929-05-16/ed-1/?sp=3) ·
  [La Gaceta, 14 Oct 1930, p. 1](https://www.loc.gov/resource/sn86002403/1930-10-14/ed-1/?sp=1) ·
  [La Gaceta, 21 Feb 1935, p. 1](https://www.loc.gov/resource/sn86002403/1935-02-21/ed-1/?sp=1)
- Tier P (newspaper page, OCR confirmed). Quotes are from OCR, which is noisy; a human should view the page
  image before any quote is printed beyond this vault.
"""

E2 = """
Two items found by full-text search inside the Internet Archive's newspaper scans (volunteer uploads of
Spanish-language dailies, OCR by Tesseract) fill the **Spain** and **Argentina** gaps for the years before
1938. Spain's existing card ([[Two Spains Mourn, November 1938]]) is a funeral card; these are earlier.

**La Correspondencia de Valencia, 2 Feb 1924 (no. 19228), p. 1 — "Visiones de Oriente".** A series on the
East; this instalment is on "La Asamblea de Angora y el despertar nacional de Turquía". It follows Kemal
from the 1921 Sakarya victory and the Mudanya terms to the verdict that, "si fué admirable la labor de
Mustafá Kemal cómo organizador y conductor de la fuerza militar", his political action mattered more: "la
gran creación de Mustafá Kemal fué la Asamblea de Angora, la Gran Asamblea Nacional que ha forjado la nueva
Turquía." A sympathetic, analytical Spanish reading in the first months of the Republic. The series author is
not given in the OCR.

**La Correspondencia de Valencia, 24 Mar 1925 (no. 19583), p. 1 — "La Turquía nueva".** The opposite
temper: a translated traveller's sketch of Angora as "la Piojosa", a fortress villa on Çankaya, soldiers
clearing the roads, and a rumour that a girl who tried to force the barrier "estaba muerta". The Ghazi,
"horror al ruido", is said to have "nervios enfermos, y su pobre cerebro, que el alcohol no ha
respetado"; in the flesh he is not tall and nervous as imagined but a "hombre de talla mediana", with eyes
that make Turkish friends ask "ojos de soñador... o de alcohólico". The writer adds that Kemal tells France
he is the child of the Revolution and Berlin that Frederick the Great is his model. An early Spanish
newspaper insult, set beside an admiring piece in the same paper a year earlier.

**El Orden (Santa Fe, Argentina), 20 Nov 1933, p. 3 — headed, in the OCR, "Mustafa Kemal sobre Turquía".** Ahead of the 29 Oct
1933 tenth anniversary: a photograph and a feature calling him "verdadero creador de la nueva Turquía".
It lists the unveiled women now "en las universidades" and in restaurants, the abolished caliphate and fez,
the Western codes (German commercial, Italian penal, Swiss civil), free seed and a farmers' bank, the
tobacco monopoly, and the depression's effect. "La modernización y nacionalización eran sus ideales."
This is the first contemporary Argentine newspaper in the census; the piece is probably agency copy, which
the OCR cannot settle. Argentina's *La Prensa* and *La Nación* stay unread.

## Sources
- [Internet Archive: La Correspondencia de Valencia no. 19228, 2 Feb 1924](https://archive.org/details/LaCorrespondencia_Valencia_19228_19240202) — text `.../download/LaCorrespondencia_Valencia_19228_19240202/..._djvu.txt`
- [Internet Archive: La Correspondencia de Valencia no. 19583, 24 Mar 1925](https://archive.org/details/LaCorrespondencia_Valencia_19583_19250324)
- [Internet Archive: Diario El Orden (Santa Fe, Argentina), 20 Nov 1933](https://archive.org/details/DiarioElOrden19331120)
- Found with the Internet Archive full-text-search endpoint (`archive.org/services/search/beta/page_production`).
  Tier P (newspaper issue OCR); the OCR is rough — check page images before external quotation.
"""

note("Events", "Spanish-Language Newspapers Across the Americas Read Kemal, 1922–1935",
     {"type": "event", "when": "1922 – 1935", "tags": ["event", "verified", "latin-america"]}, E1)
note("Events", "Valencia and Santa Fe Read Kemal, 1924–1933",
     {"type": "event", "when": "1924 – 1933", "tags": ["event", "verified", "latin-america"]}, E2)
print("census r7 latam: 2 events")
