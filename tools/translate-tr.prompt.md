You are translating records from a scholarly archive into Turkish. The archive collects what people around the world said about Mustafa Kemal Atatürk, 1919–2026. Each record has the speaker (voice), their role, their own words (quote), a one-line English summary of what they saw in him (summary), a research note (caveat) with citations, how the words reached us (mediated_by), and a verification note and method (verification_note, verification_method). Each item below carries only the fields that need translating. The Turkish will be shown to Turkish readers on a public exhibition site. Translate every record in the JSON below and return the same records with Turkish text.

Rules:
1. Accuracy over elegance. Never add, soften, sharpen or editorialise. Hostile or admiring statements stay exactly as hostile or admiring. Keep hedges ("perhaps", "reportedly") and uncertainty.
2. quote:
   - If the quote is in Turkish (including Ottoman-era Turkish in Latin letters, old spelling, or Turkish without diacritics), return it UNCHANGED, character for character, and set quote_kind "original-turkish". Never modernise it.
   - If it starts with "[translation]", that text is already a translation of words whose original is not available: if it is Turkish, return it without the "[translation]" prefix and set quote_kind "original-turkish"; otherwise translate it into Turkish (drop the prefix) and set "translated".
   - If it contains an original-language passage followed by "[English translation: '…']", translate from the ORIGINAL language passage (use the English only as a check) and return only the Turkish.
   - Any other language (English, French, German, Arabic, Persian, Indonesian, …): translate faithfully into Turkish from that language and set "translated".
   - "Mustapha Kliamil", "Mustapha Kamil", "Mustafa Kernel" and similar are OCR misreadings of "Mustafa Kemal": write "Mustafa Kemal". The marker "[Kemal]" should not appear in the Turkish.
   - Keep how the speaker names him (Mustafa Kemal, Kemal Pasha → Mustafa Kemal Paşa, the Ghazi → Gazi, Atatürk, Kemalists → Kemalistler). Write "Angora" as "Ankara" only if the speaker clearly means the city in a neutral way; otherwise keep "Angora".
   - If quote is null, return null and quote_kind "none".
   - Return the quote without surrounding quotation marks.
3. voice: the speaker's name. Keep personal names as they are (no Turkish respelling of foreign names; Turkish people keep their Turkish spelling). Translate only descriptive parts, e.g. "Salonika city council" → "Selanik Belediye Meclisi", "The Times (London)" stays "The Times (Londra)".
4. role, summary: natural, clear modern Turkish. Use Turkish conventions for places and events: Smyrna → İzmir (keep "Smyrna" only inside a quoted original title), Constantinople → İstanbul, Salonika → Selanik, Angora → Ankara, Dardanelles/Gallipoli → Çanakkale/Gelibolu as appropriate, the War of Independence → Kurtuluş Savaşı, Grand National Assembly → Türkiye Büyük Millet Meclisi (TBMM), Lausanne → Lozan, the caliphate → hilafet.
5. caveat, mediated_by, verification_note and verification_method (research notes): translate the prose fully into Turkish. Keep unchanged: titles of books, newspapers and archives, article titles, page numbers, volume/issue numbers, call numbers, URLs, file names, and any passage quoted in its original language (inside quote marks). Abbreviations like "p." → "s.", "vol." → "c.", "no." → "sayı" when citing. Dates in prose: "18 Sept 1922" → "18 Eylül 1922".
6. Keep null as null. Keep "id" unchanged. Return exactly the fields you were given (plus quote_kind when you were given a quote). Output only the JSON object matching the schema: {"items": [...]} with one item per input record, in the same order.
7. Glossary: "believers" (religious people) → "dindarlar" or "Müslümanlar" as the context requires; never "inananlar", which reads in Turkish as "those who believed in him".

Records:
