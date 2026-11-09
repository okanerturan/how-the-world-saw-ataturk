# -*- coding: utf-8 -*-
# Census round 4 (Oct 2026) — Asia / Oceania / telegram corpus.
# Routes: KB/Delpher SRU + OCR resolver (Dutch East Indies dailies, Nov 1938); TBMM Açık Erişim DSpace REST API
# (bitstreams of handle 11543/2467) + local macOS Vision OCR of the scanned telegram forms.
from _lib import note, person

P = [
("Choudhry Rahmat Ali", dict(role="Cambridge law graduate; coiner of the name 'Pakistan' (1933); founder-president of the Pakistan National Movement", nat="Indian Muslim (Punjabi), in exile in England", life="1897–1951",
  stance="admiring — Kemal as 'Asia's heroic apostle of nationalism'", tags=["politics", "asia", "verified"], body="""
The man who coined **"Pakistan"** is also on the roll of condolence telegrams sent to Ankara in
November 1938 — from a London suburb, **Watling, Edgware**, over his own title. The text (read from
the scan of the telegram itself, stamped as received at Ankara on 11 November, addressed to the
Speaker of the Turkish Grand National Assembly):

> "On behalf of the Pakistan National Movement representing Punjab, Frontier Province, Kashmir,
> Sind and Baluchistan I beg your Excellency to accept our heartfelt condolences on the sad demise
> of His Excellency the President Kemal Ataturk, in whom **Turkey has lost its maker, Asia its heroic
> apostle of nationalism and the world one of its greatest statesmen.** While mourning the loss of
> the great President we pray for the glory of the Turkish *millet*. — C. Rahmat Ali, founder
> president of the Pakistan National Movement."

What it shows. Rahmat Ali had issued *Now or Never* from Cambridge in January 1933, the pamphlet
that put the acronym PAKSTAN into print on behalf of "thirty million Muslims" of the five northern
units of India. Five and a half years on, the Pakistan National Movement is a tiny exile body — and
it addresses the Turkish parliament as the voice of the very provinces it claimed. Its Kemal is a
**nation-maker** (*maker*) and a pan-Asian emblem of **nationalism**, not a caliph and not a
reformer of religion: the word "Muslim" appears nowhere in the telegram, the word "nationalism"
does. That is a distinctive angle inside the Indian column, where the 1920s gaze had been
Khilafat-shaped (see [[Khilafat Disillusion, 1924]]) and the mainstream League gaze was Jinnah's
("[[Muhammad Ali Jinnah]]") — and a mirror for a man whose own project would later be written out of
Pakistan's official story (the Cambridge chapter below: his "virtual banishment from Pakistan's history").

*Boundary:* one telegram, formulaic by the genre, sent by a man who needed international
recognition for his movement; it is evidence of what he chose to say to Ankara in 1938, not of
a sustained engagement with Kemalism. Intensity 1–2. Unlike most of the Indian-column nodes it
rests on a **primary document**.

See [[Condolence Telegrams to Ankara, November 1938]], [[India Mourns, November 1938]].

## Sources
- TBMM Library, *Atatürk'ün ölümü dolayısıyla yabancı ülkelerden Büyük Millet Meclisi'ne gelen taziyetnameler*, vol. 1 (`197605293_c1.pdf`, telegram no. 34; scan read directly, 28 Oct 2026) — [acikerisim.tbmm.gov.tr/handle/11543/2467](https://acikerisim.tbmm.gov.tr/handle/11543/2467) (P). The scan is rotated; the text was read from the image.
- "Choudhary Rahmat Ali and his Political Imagination," ch. 3 of *Muslims against the Muslim League* (Cambridge UP) — [cambridge.org](https://cambridge.org/core/books/muslims-against-the-muslim-league/choudhary-rahmat-ali-and-his-political-imagination-pak-plan-and-the-continent-of-dinia/20E77B5DA8462AE0DB44711CBC72599D) (S; Pakistan National Movement founded 1933, later All-Dinia Milli Movement; Foster papers, Centre of South Asian Studies, Cambridge)
- [South Asian Britain, "Choudhary Rahmat Ali"](https://southasianbritain.org/content/choudhary-rahmat-ali) (*Now or Never*, 28 Jan 1933)
""")),
]

E = [
("Dutch East Indies Press, November 1938", "10–28 November 1938", """
**The colony read the death in Dutch, from two sides of a desk.** The KB/Delpher corpus holds the
Netherlands-Indies dailies of November 1938 — *Bataviaasch Nieuwsblad* and *Het Nieuws van den Dag
voor Nederlandsch-Indië* (Batavia), *Soerabaijasch Handelsblad* and *De Indische Courant*
(Surabaya), *De Sumatra Post* (Medan) — and their pages on Atatürk resolve to OCR text. What they
print is two gazes that barely touch: a **colonial-European one**, which reads Atatürk as the
Eastern ruler who beat the East with the West; and, in two Surabaya dailies, one small glimpse of
an **Indonesian Muslim one**, in a Muhammadiyah meeting hall.

## The Muslim glimpse — Muhammadiyah, Surabaya, mid-November 1938

On the evening of **15 November 1938** (reported 16 Nov), the Surabaya branch of
**Muhammadiyah** held a public meeting "under great interest from the native side" (*Soerabaijasch
Handelsblad*). The paper's one line on Atatürk: the meeting was opened and *"the death of Ataturk
was commemorated by a minute's silence."* *De Indische Courant*, reporting the same evening at
length, adds the texture: the local chairman "commemorated Mustafa Kemal Atatürk in a few words" and
"asked those present to honour the memory of **this great Islamite** with a few moments of silence";
one of the audience then recited a fitting prayer from the Qur'an in Arabic, translated into
Malay; and the chairman, "taking Kemal Pasha's death once more as his point of departure," gave a
reflection on life and death and urged the audience always to strive for the good. Present, taking
notes: the colonial political police (PID) in the persons of an assistant-*wedono* and two
police *mantri*.

The meeting itself was about something else — two Al-Azhar graduates were to lecture on **Muslims in
Europe**; the Yugoslav propagandist Moestapha Ramadan fell ill on arrival from Borneo, and his
companion H. Idris of Bengkulu told, in Malay, of their 1934 journey Cairo–Piraeus–Belgrade–Sarajevo
(99 mosques, one Islamic university). So the Atatürk moment is a *preface*: a modernist Muslim
association, hearing the news, spends a minute on the man who had abolished the Caliphate and
the Arabic script, and calls him a great Muslim. The label is the reporter's rendering of Malay or
Dutch speech, and the sample is one branch in one city — not a position of Muhammadiyah as a whole.
It nonetheless marks where the 1920s quarrel stood by 1938: no protest, a prayer.

## The colonial-European gaze

- **11 Nov, *Het Nieuws van den Dag* (Batavia), "Einde ?"**: "Kemal Atatürk was a Prometheus. He did
  the superhuman. *With the West he conquered the East, with the East the West.* Out of scattered
  remains he forged a proud people, out of ruins a steel-strong state." No ascetic dictator, it adds
  — the gypsies played till grey dawn and "when the Ghazi feasted he knew no measure and no time" —
  and the liver disease "dragged him to the grave." The same issue ran "Kemal Atatürk the
  exuberant!" (a dance-floor anecdote).
- **10 Nov, *Soerabaijasch Handelsblad*, "De culturele en oeconomische opbouw"**: to make a modern
  state "after Western example" Atatürk had first to strip the Muslim clergy of their influence —
  separation of state and religion, abolition of the Caliphate, the Latin script as "a means to
  end the rule of the clergy over the people", women's emancipation, the end of the fez.
- **11 Nov, same paper**: "Kemal Atatürk's greatest gift: to make the right enemies."
- **19 Nov, *Bataviaasch Nieuwsblad*, children's page "Voor de oudere Jeugd"**: Atatürk made Turkey,
  "in a few years, from a backward Asiatic land into an excellently organised Western state."
- **21 Nov, *Bataviaasch Nieuwsblad*, G. Nypels (⚠️ byline and the title "Bij den dood van Kemal Atatürk" are not confirmed: the OCR carries neither)**: the longest and
  most revealing piece, a correspondent's reminiscence of Ankara in 1920–21. The body text says it
  (our translation of the Dutch; it is not a headline): Turkey was made by "this man with the iron will,
  with the great intelligence and the ruthlessness necessary for this East." He
  tells of the *hodjas* who elected the general president of their parliament so as to keep him from
  drinking, of Kemal's "deadly hatred" of the clergy, of the fez ban; closes on the "great unknown"
  of how many Anatolians remain secret followers of the old ways "with Oriental cunning." Admiration
  and orientalism in one breath, in a colonial daily read by a Muslim-majority colony's
  Dutch-reading class.
- **28 Nov, *De Sumatra Post*, "De Voorproever van Atatürk"** (borrowed from the *Bataviaasch
  Nieuwsblad*): John Gunther's phrase that Atatürk was the "roughneck" among dictators, next to
  whom Hitler was a "milksop" and Mussolini a "perfumed dandy"; and the story of an Englishman, a deserter turned carpet dealer in Istanbul, who passed as a Turk to serve as his
  food-taster.
- **11 Nov, *De Sumatra Post***: Aneta-ANP wire — Minister Patijn calls at the Turkish
  legation in The Hague "to convey the condolences of the Netherlands Government."
- **19 Nov, *De Sumatra Post***, Transocean wire from Istanbul: the throne room at Dolmabahçe,
  with "the black, the mourning colour of the Western world, wholly absent, in accordance with
  Muslim tradition" — a reporter's gloss on a ceremony Turkey itself had designed.

## Reading

The Indies editors needed no Muslim translation of Atatürk: they had a ready Prometheus and a ready
"Oriental" in the same sentence. What the colony's Muslims thought has to be read from the margins —
a Surabaya meeting minute, a police note-taker, a prayer in two languages — and the Malay-language
press (*Pewarta Deli*, *Pemandangan*, *Soeara Moehammadijah*) is not in this corpus. Cf.
[[Malay Press and the Fall of the Caliphate]] for the earlier debate across the Straits, [[Sukarno]]
for the nationalist reading of Kemal that came later, and [[Dutch Press, November 1938]] for the
metropolitan counterpart. See [[Death and State Funeral of Atatürk]], [[Kemalism]].

## Sources
- Soerabaijasch Handelsblad, 16 Nov 1938, "Vergadering Mohammadijah" — KB/Delpher `ddd:011121218:mpeg21:a0100:ocr` (P)
- De Indische Courant (Surabaya), 16 Nov 1938, "Moslims in Europa. Bezoek van Zuid-Slavischen propagandist. Moestafa Kemal Ataturk herdacht" — `ddd:010286302:mpeg21:a0062:ocr` (P) — a second, independent report of the same meeting
- Het Nieuws van den Dag voor Nederlandsch-Indië, 11 Nov 1938, "Einde ?" and "Kemal Atatürk de uitbundige!" — `ddd:010227760:mpeg21:a0220:ocr`, `a0217` (P)
- Soerabaijasch Handelsblad, 10 Nov 1938 `ddd:011121213:mpeg21:a0008:ocr`; 11 Nov `ddd:011121214:mpeg21:a0153:ocr` (P)
- Bataviaasch Nieuwsblad, 19 Nov `ddd:010863962:mpeg21:a0260:ocr`; 21 Nov (Nypels) `ddd:011122903:mpeg21:a0177:ocr` (P)
- De Sumatra Post, 11 Nov `ddd:010382452:mpeg21:a0118:ocr`; 19 Nov `ddd:010382459:mpeg21:a0143:ocr`; 28 Nov `ddd:010382465:mpeg21:a0200:ocr` (P)
- Retrieved via KB SRU (`jsru.kb.nl`, collection `DDD_artikel`) and the resolver `resolver.kb.nl/resolve?urn=…`, 28 Oct 2026
"""),
("Condolence Telegrams to Ankara, November 1938", "10–16 November 1938", """
**The same news, one hundred cables.** Within hours of 10 November 1938 the Turkish Grand National
Assembly — whose Speaker, **Abdülhalik Renda**, was also acting head of state — began receiving
telegrams from heads of state, parliaments, ambassadors, émigré committees, Muslim communities and
students abroad. The Assembly's library bound the lot as two volumes, *Atatürk'ün ölümü dolayısıyla
yabancı ülkelerden Büyük Millet Meclisi'ne gelen taziyetnameler* (vol. 1: 38 scanned pages; vol. 2: 61), each
telegram pasted on its original PTT form with a typed index at the end. The set is digitised and
scriptable (the library's DSpace REST API serves the PDFs; the built-in text layer is useless
garbage, but the scans are clear and can be read by an OCR pass or by eye). What follows is a reading
of **the scans themselves**: primary documents, with the OCR checked against the page image for the
Asian and Pakistani items. It is a record of **what the sender chose to tell Ankara**, in the
formulae of the genre — not of private feeling.

## Heads of state and parliaments (selected)

| From | Sender | The gist (translated; French, English, German or Italian originals) |
|---|---|---|
| United States | [[Franklin D. Roosevelt]], the White House | "devotion to his country won for him the respect of the entire world" |
| Germany | [[Adolf Hitler]] (as Reich Chancellor); Field Marshal Göring (Reichstag) | Hitler: "a great soldier, a brilliant statesman and a historical personality… in the creation of the new Turkish state Atatürk set himself a monument whose existence will outlast generations." Göring: grief "on behalf of the whole Greater German Reichstag" |
| Japan | Emperor Hirohito; [[Prince Takamatsu]]; the president of the Japan–Turkey society (a Tokugawa) | Hirohito: "I learn with deep affliction of the death of … Kamal Ataturk"; Takamatsu in English, "profound sorrow"; the society: "the friends of Turkey in Japan share" the grief |
| Italy | the King, from Pisa; Senate (Federzoni); Chamber (Ciano) — via the Italian embassy, 12 Nov | the Chamber: Atatürk the "architect of the rebirth of the Turkish nation" |
| Australia | Prime Minister Joseph Lyons, Canberra | "illustrious statesman and founder of the Turkish Republic" |
| Afghanistan | King Zahir Shah (Persian, Latin-script transliteration) | grief for the Turkish brother nation; Afghan envoy Esendal and the Turks in Kabul also wired |
| Iran | Hassan Esfandiari, for the nation and the Majlis (addressed to the Speaker) | "the Iranian nation and parliament share the sorrows of the noble Turkish nation" |
| Iraq | King Ghazi; the Chamber of Deputies, which **suspended its sitting** | the Chamber charged its president to convey its condolences "to the great saviour" |
| Syria | President Hashim al-Atassi | "profoundly afflicted… the Syrian people" |
| Saudi Arabia | Abdul Aziz (Riyadh) | listed in the index (text not read) |
| Transjordan | Emir [[Abdullah I of Jordan]] (Amman, 10 Nov) | condolences to "the noble Turkish nation" |
| Egypt | King Farouk; Wafd leader Nahhas Pasha; Chamber president Baha ed-Din Barakat | Farouk: "illustrious patriot, regenerator of the new Turkey"; Nahhas: "Turkey and the East"; the Chamber: "glorious hero, renovator and creator of greater Turkey" |
| Palestine | [[Haj Amin al-Husseini]] (from Beirut); Jewish General Council of Palestine (Isaac Ben-Zvi, chairman); "the Turks of Haifa" | Husseini: "the Arab nation of Palestine presents through you to the noble Turkish people its moved condolences for the irreparable loss … the great Atatürk"; the Jewish Council: "great founder, regenerator of new Turkey" |
| Spain | President Manuel Azaña (Barcelona) | "best wishes for the continuity of his great work" |
| Albania, Bulgaria, Romania, Hungary, Yugoslavia, Estonia, Latvia, Poland, Sweden, Denmark, Norway, Switzerland, Luxembourg, Mexico, USSR (Kalinin, index only) | King Zog, Tsar Boris III, King Carol II, Regent Horthy, the Yugoslav Senate and Chamber, Paets, Ulmanis, Mościcki, King Gustaf V, King Christian X, King Haakon, Baumann (Swiss Federal Council), Grand Duchess Charlotte, Lázaro Cárdenas | the genre; the Speaker of the Bulgarian Sobranie, Stoycho Moshanov (Sofia, 10 Nov; the telegram is in French, here translated): "the death of its renovator and great head of state" |
| Émigrés | [[Mehmed Emin Resulzade]] (Warsaw): "in the name of National Azerbaijan"; Mir Yakub (Paris), Azerbaijani National Committee | the second adds that "Azerbaijan, groaning under foreign domination" mourns |

**Missing from the index:** no cable from Mussolini, no Chinese or Siamese government, no message in
the volumes from Reza Shah, Chiang Kai-shek or the Government of India — either sent elsewhere or
not sent; the absence is a datum only if confirmed.

## The Muslim and colonial world writes to the Assembly directly

The more distinctive sheets are from **communities that had no state to speak for them**:

- **British India.** The **Punjab Legislative Assembly**, Lahore: "on Premier's motion Punjab Assembly
  **adjourned as a mark of respect** to the late Ghazi Kemal Ataturk," offering sympathy "on the sad
  demise of the first President of the Turkish Republic" — signed by the Speaker. Also **Begum
  Dr Ansari** (Delhi) and the **Muslims of Jaipur State**; the index also has an unread entry for "Hindistan, Kongre Başkanı". **[[Choudhry Rahmat Ali]]** (London) — see his own note.
- **Southern Africa.** The **Transvaal Muslim Association** (Johannesburg): "Kemal Ataturk **Ghazi**,
  Islam and saviour of Muslim honour"; the **Young Indian Social Reform Society of South
  Africa**: "one of the foremost *social reformers* of our time … he built modern Turkey out of
  the ashes of convention-ridden decaying Ottoman empire"; Muslim communities at **Ermelo**,
  **Lichtenburg** and Port Elizabeth; the **Zoutpansberg Indian Congress**. Cf. [[South African Muslims and the Anatolian Cause, 1919–1923]].
- **East Africa.** Muslims of **Eldoret** (Kenya); "the Muslim population of East Africa,"
  Jamia mosque, Nairobi; a Muslim body at **Tanga**.
- **Malaya.** Penang: a Muslim Turkish union and the Penang Muslim Merchants Society, "may Allah
  rest his soul in peace" (compare [[Malay Press and the Fall of the Caliphate]]).
- **Beyond the borders.** Turkish Muslim communities in **Skopje, Bitola, Kumanovo, Plovdiv**, the
  Turks and the Islamic community of Finland; Armenian and Jewish voices (the mayor of **Kırıkhan**, Stepan Faraoyan;
  *Keter Zion Ankara* society and a Sephardic congregation in Brooklyn); the Turkish tradesmen of Nicosia (Cyprus); a Berlin student, Fazıl Yinal, who proposes that Atatürk's seat in
  the Assembly be kept for ever and his name called at every roll-call — the one letter on file that
  is also a proposal.

## Reading

Two things stand out. **First, the genre is universal, the register is not.** Fascist and Nazi
heads, Soviet and Western democrats, kings and republicans all write "regenerator," "reformer,"
"founder"; only the Islamic and colonial senders talk about **Islam, Asia, honour, the East** (Rahmat
Ali's "Asia its heroic apostle of nationalism"; Nahhas's "Turkey and the East"; the Transvaal
Muslims' "saviour of Muslim honour") — the very claim the Atatürk Turkey had spent fifteen years
declining. **Second, who wrote is a map of who felt entitled to write:** the Sovereign of Japan to
a speaker, the Punjab's Speaker to a President, a Cape Indian reform society to a prime minister.
The map has no Chinese or Indian-government cable on it.

*Boundary:* about 90 numbered items in the typed indexes. Nearly all Latin-script sheets were read
in OCR; sheets in Arabic script (Tripoli, Lebanon) and a few unclear ones were not, and the Kalinin,
Spanish-Senate and Saudi sheets are known here from the index only. Senders' first names are taken from the sheets or index and spellings are
the OCR's where not clear; roles for lesser senders (Tokugawa, Ansari, Faraoyan) are as signed.

See [[Death and State Funeral of Atatürk]], [[Foreign Delegations at the Funeral, November 1938]].

## Sources
- TBMM Library (Açık Erişim), handle 11543/2467: vol. 1 `197605293_c1.pdf` (nos. 1–38) and vol. 2 `197605294_c2.pdf` — [acikerisim.tbmm.gov.tr/handle/11543/2467](https://acikerisim.tbmm.gov.tr/handle/11543/2467). Items read: Riga/Ulmanis, Rio de Janeiro, Rome, Italian Senate and Chamber (12 Nov), Riad, Saint-Louis Réunion, Salonica, Sofia ×4, Stockholm, Tallinn, Tanga, Tehran, Tirana, Tokyo ×4, Warsaw ×3, Washington, Watling (Rahmat Ali), Vevey (Abbas Hilmi II), Amsterdam, Antakya (Hatay), Athens, Alexandria, Amman, Baghdad ×2, Barcelona, Belgrade, Berlin ×7, Bern, Beirut ×3, Brooklyn ×2, Bucharest ×3, Budapest, Cairo ×4, Canberra, Damascus, Delhi, Eldoret, Ermelo, Kabul ×2, Lahore, Lichtenburg, London ×2, Luxembourg, Mexico, Moscow, Nairobi, Nicosia, Oslo, Paris ×6, Penang, Pisa, Port Elizabeth, Prague (P — primary telegrams)
- The telegrams are dated by the Ankara receipt stamp 10–16 Nov 1938. OCR produced locally (macOS Vision); the Rahmat Ali and Punjab Assembly sheets (vol. 1 no. 34; vol. 2 no. 39) were additionally read from the page images.
- For the 12-Nov Italian items: cover note of the Italian embassy in Ankara, 12 Nov 1938 (same volume).
"""),
]

for n, kw in P:
    person(n, **kw)
for n, when, b in E:
    note("Events", n, {"type": "event", "when": when, "tags": ["event", "verified", "obituary-corpus"]}, b)

print(f"census r4 asia: {len(P)} people, {len(E)} events")
