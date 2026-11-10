# data/: field reference

This folder holds the archive itself. Each record is one YAML file: one voice speaking about Atatürk at one moment, with its source and the result of an independent check.

This page describes every field. To add a record, start from [`templates/voice.yaml`](templates/voice.yaml) and read [CONTRIBUTING.md](../CONTRIBUTING.md). The machine-readable rules are in [`schema/voice.schema.json`](schema/voice.schema.json) and [`schema/translation.schema.json`](schema/translation.schema.json) (JSON Schema, draft 2020-12). Editors that understand the `# yaml-language-server` line at the top of each file (for example VS Code with the YAML extension) use them to check fields as you type.

## Layout

```
data/
  voices/<YYYY>/<id>.yaml              one record
  translations/tr/<YYYY>/<id>.yaml     the Turkish for that record (machine translation, corrections welcome)
  schema/voice.schema.json             JSON Schema for a record
  schema/translation.schema.json       JSON Schema for a translation file
  templates/voice.yaml                 commented template for a new record
```

- `<id>` is the record's `id`. The file name is always `<id>.yaml`.
- `<YYYY>` is the first four characters of the record's `date`. A record dated `"1938-11-10"` goes in `voices/1938/`. A record dated with a decade, such as `"1980s"`, goes in `voices/1980/`.
- A translation file has the same year folder and file name as its record.
- The records are split into year folders because GitHub shows at most 1,000 files in one folder. 1938 alone has 207 records.
- Files must end in `.yaml`. A `.yml` file is not read.

## A record, annotated

This is `voices/1921/lenin-aralov-1921.yaml`. The comments at the ends of the lines are added here for explanation; they are not in the file. Two long texts are shortened, marked `[…]`.

```yaml
# yaml-language-server: $schema=../../schema/voice.schema.json   # lets editors check the file
id: lenin-aralov-1921                  # = file name; <voice>-<year>, plus a word to tell records apart
voice: Vladimir Lenin                  # who spoke, as the source names them
voice_type: person
role: Chairman of the Council of People's Commissars, Soviet Russia
country: Soviet Russia                 # the polity at the time
country_now: Russia                    # its modern successor
domain: politics
date: "1921"                           # always in quotes; as precise as the source allows
era: contemporary                      # agrees with the date: before 10 Nov 1938
polarity: admiring                     # the speaker's stance, not ours
intensity: 2
mirror: bourgeois-revolutionary        # what the speaker saw in him
artifact: memoir                       # the form the words reach us in
evidence: P                            # source tier(s)
summary: >-                            # OUR words: a neutral paraphrase, at most 25 words
  Briefing his envoy, calls Mustafa Kemal no socialist but a good organiser, talented commander and clever
  statesman leading a bourgeois-national revolution.
quote:                                 # THEIR words, verbatim, in the language of the source
  text: >-
    — Конечно, Мустафа Кемаль-паша не социалист,— говорил Владимир Ильич,— но, по-видимому, хороший
    организатор, талантливый полководец, ведет буржуазно-национальную революцию, прогрессивно настроенный
    человек, умный государственный деятель.
  translation: >-                      # English, because the text is not English
    Of course, Mustafa Kemal Pasha is not a socialist,' Vladimir Ilyich said, 'but he is evidently a good
    organiser, a talented commander, leading a bourgeois-national revolution, a progressive-minded man, a
    clever statesman.
  language: ru
mediated_by: >-                        # second-hand: where we read it, with the page
  S. I. Aralov, Vospominaniya sovetskogo diplomata 1922–1923 (Moscow: IMO, 1960), pp. 34–35, recalling his
  briefing by Lenin
caveat: >-                             # what the reader should be careful about
  Recollected about 38 years later in a Soviet-era memoir; Lenin's words are Aralov's reconstruction. […]
node: World Leaders on Atatürk — Round 30 Sweep   # the research note in vault/
sources:
  - url: https://archive.org/details/vospominaniia_sovetskogo_diplomata_1922_1923
  - url: https://archive.org/download/vospominaniia_sovetskogo_diplomata_1922_1923/vospominaniia_sovetskogo_diplomata_1922_1923_djvu.txt
verification:                          # added by a checker, never by the record's author
  verdict: confirmed
  quote_found: true
  checked_against: >-
    S. I. Aralov, Vospominaniya sovetskogo diplomata 1922–1923 (Moscow: Izd. Instituta mezhdunarodnykh
    otnoshenii, 1960, 224 pp.), archive.org vospominaniia_sovetskogo_diplomata_1922_1923 djvu.txt; scene
    starts p. 34, Lenin's lines on p. 35
  method: archive.org open OCR text read
  note: >-
    Russian verbatim apart from the OCR slip '—: е социалист' (= 'не социалист'). Edition and pages match […]
  checked_on: "2026-11-05"
```

## Fields

Required fields come first. A record may not contain any other top-level key: a misspelt key is an error, not a silent extra field.

| Field | Required | Rule |
|---|---|---|
| `id` | yes | Lowercase letters, digits and hyphens (`^[a-z0-9]+(-[a-z0-9]+)*$`). Unique. Equal to the file name. Convention: `<voice-slug>-<year>`, plus `-<mm>`, `-<dd>` or a word when two records would otherwise share an id: `hemingway-1922`, `le-temps-1922-09-15`, `kerry-2013-03-02-book`. |
| `voice` | yes | The person, newspaper, institution or collective, named as in the source. |
| `voice_type` | yes | `person` · `press` · `institution` · `collective` · `self`. See below. |
| `role` | yes | A short description in English: "Hungarian PM", "Prague daily", "Islamic reformer". |
| `country` | yes | The polity at the time: "British India", "Ottoman Empire", "Dutch East Indies". |
| `country_now` | yes | Its modern successor: "India", "Turkey", "Indonesia". The same as `country` if unchanged. |
| `domain` | yes | `politics` · `letters` · `arts` · `military` · `religion` · `science` · `press` · `sport` · `diplomacy`. The field the voice speaks from. |
| `date` | yes | A quoted string: `"YYYY"`, `"YYYY-MM"`, `"YYYY-MM-DD"`, or a decade `"YYY0s"` such as `"1980s"`. As precise as the source allows, and a real calendar date. |
| `polarity` | yes | `admiring` · `hostile` · `conflicted` · `instrumental` · `witness`. See below. |
| `summary` | yes | Our paraphrase of what they saw in him, in English, in 25 words or fewer (the validator warns above 25). It is never the speaker's words; those go in `quote`. |
| `sources` | yes | A list of at least one source. Each needs a `url` or a `citation`. See below. |
| `era` | no | `contemporary` · `funeral` · `posthumous`. Must agree with the date when the date decides it. |
| `intensity` | no | `1`, `2` or `3`, as a number without quotes. |
| `mirror` | no | One of ten readings of him, listed below. Leave the key out if none fits. |
| `artifact` | no | The form of the testimony. See below. |
| `evidence` | no | Source tiers joined by `+`, e.g. `P`, `P+S`, `S+J`. See below. |
| `quote` | no | The speaker's own words. See below. |
| `mediated_by` | no | The chain when the words are known second-hand: where we read them ← where they took them from. `"Toksoy 2006 ← Cumhuriyet 14 Nov 1938"`. |
| `caveat` | no | What the reader should be careful about: a single source, an inference, an unresolved attribution, an approximate date. |
| `node` | no | The title of the research note in `vault/` that this record belongs to. Optional for new records from contributors. |
| `verification` | no | The independent check. Added by a maintainer or checker, never by the person who added the record. See below. |

### voice_type

| Value | Meaning |
|---|---|
| `person` | A named individual. |
| `press` | A newspaper or magazine speaking as itself: an editorial or a report. An article by a named writer is usually recorded under the writer, as a `person`, with the paper in `role`. |
| `institution` | A parliament, party, ministry, academy, congress or similar body speaking as a body. |
| `collective` | An unnamed crowd or community: "Muhammadiyah meeting, Surabaya". |
| `self` | Atatürk's own words about himself. Kept in the data, not shown in the exhibition. |

### polarity

The stance of the voice towards Atatürk, as the source shows it. It is not our judgement of him.

| Value | Meaning |
|---|---|
| `admiring` | Praise or approval. |
| `hostile` | Attack, condemnation or contempt. |
| `conflicted` | Both at once, or a view that changes within the same text. |
| `instrumental` | Praise or use of him that serves the speaker's own agenda, often diplomatic courtesy. |
| `witness` | Reports, meets or attends without a stated view. |

### era

| Value | Dates |
|---|---|
| `contemporary` | up to 9 November 1938 |
| `funeral` | 10 November to 31 December 1938 |
| `posthumous` | 1939 and later |

If the date settles the era, the two must agree. A date such as `"1938-11"` or `"1938"` does not settle it, and the validator accepts the era you give. (The rule is `eraOf()` in [`tools/lib/records.mjs`](../tools/lib/records.mjs).)

### intensity

| Value | Meaning |
|---|---|
| `1` | A passing mention. |
| `2` | Sustained: an article, a speech, a chapter. |
| `3` | Life- or state-shaping: a policy, a career-long model, a law. |

### mirror

What the speaker saw in him, when one of these ten readings fits. If none fits, leave the key out; do not force one.

| Value | The reading | Examples in the data |
|---|---|---|
| `anti-colonial-liberator` | The leader who defeated the imperial powers; a model for colonised peoples. | Nariman Narimanov, Dong-A Ilbo |
| `secular-rationalist-prophet` | The reformer who put reason, science and secular law above religion. | Édouard Herriot, Colonel Wedgwood MP |
| `volkisch-purifier` | The ethnic-nationalist strongman, as Nazi and völkisch writers saw him. | Adolf Hitler, Hamburger Tageblatt |
| `bourgeois-revolutionary` | A national, non-socialist revolutionary, as Soviet and communist writers saw him. | Vladimir Lenin, Mikhail Frunze |
| `nation-forge-template` | A model for building a modern nation-state from above. | Cai Hesen, Miyake Setsurei |
| `apostate` | The man who turned his country away from Islam. | Abdülmecid II, Abdelhamid Ben Badis |
| `emancipator-patriarch` | The liberator of women, or the father figure who set the terms of that liberation. | Huda Sha'arawi, Ruth Frances Woodsmall |
| `chivalrous-enemy` | The honourable opponent of Gallipoli and the Greek war. | C.E.W. Bean, Claude Farrère |
| `internal-mirror` | The view from inside Turkey: comrades, deputies, rivals and opponents who knew him at close range. | Kâzım Karabekir |
| `modernization-poster-child` | The model of successful Westernising modernisation. | Le Corbusier, Faisal I of Iraq |

### artifact

The form in which the words or act reach us: `quote` · `editorial` · `article` · `poem` · `book` · `speech` · `policy` · `visit` · `telegram` · `memoir` · `artwork` · `monument` · `ceremony` · `nomination` · `broadcast` · `report` · `letter` · `meeting`.

### evidence

The kinds of source behind the record, joined by `+` (pattern `^[PSJFT](\+[PSJFT])*$`).

| Tier | Meaning |
|---|---|
| `P` | Primary: the voice's own text, or contemporary print. |
| `S` | Secondary scholarship. |
| `J` | Journalism. |
| `F` | A figure's own later account. |
| `T` | Tertiary or reference work. |

### quote

The speaker's own words, exactly as printed in the source, in the source's language. Never a paraphrase.

| Key | Rule |
|---|---|
| `text` | Required when `quote` is present. The words as printed. Omitted words are marked `…`. No translation inside this field. |
| `language` | ISO 639-1 code (`en`, `tr`, `fr`, `de`, `ar`, `ru` …), or `ota` for Ottoman Turkish in Arabic script. |
| `translation` | An English translation, when `text` is not English. |
| `note` | An editorial note about the passage. |
| `is_translation` | `true` when `text` is itself a translation and the original is not available (for example a Turkish news agency's rendering of an English guest-book entry). |
| `needs_split` | `true` when several passages and their translations are mixed together in `text`. It marks older records that still need cleaning up. Do not use it in new records. |

### sources

A list. Each item needs a `url` or, when there is no link, a `citation`.

| Key | Rule |
|---|---|
| `url` | A link starting with `http://` or `https://`. |
| `archived` | A Wayback Machine (`https://web.archive.org/web/…`) or archive.today (`archive.ph`) copy of the link. Open the copy before adding it: for a site behind a bot check the archive often holds only the check page, and such a link is left out. |
| `citation` | A full citation: author, title, publisher or archive, year, page. Required when there is no `url`. |
| `page` | Page, column or folio. Text or a whole number. |
| `label` | A short name for the source. |
| `accessed` | When the link was read: `"YYYY-MM-DD"`. |

Give the page wherever the source has pages, in `page` or inside `citation`.

### verification

The independent check. Someone other than the record's author re-opens the cited source and writes down what they found. A contributor never adds this block to their own record. On a pull request, the validator flags any change to a `verification` block for the maintainer's review.

| Key | Rule |
|---|---|
| `verdict` | Required. One of the verdicts below. |
| `quote_found` | `true` or `false`: whether the quote was found in the source. |
| `checked_against` | What the checker read: the source, edition or page, and the passage found. |
| `method` | How the source was read: for example a fetch of the page, a page image read by eye, a PDF text extraction. |
| `note` | What the check found that the reader should know. |
| `resolution` | How a problem found by the check was fixed in the record. |
| `checked_on` | The date of the check, `"YYYY-MM-DD"`. |
| `checked_by` | Who checked: a name or GitHub handle. |
| `earlier` | A list of previous checks of this record, in the same shape. When you re-check a record, move the old check here. |

#### Verdicts

| Verdict | Meaning | Shown in the exhibition |
|---|---|---|
| `confirmed` | The source was re-opened; the quote is there and the record is supported. | yes |
| `paraphrase-ok` | The source supports the summary; there is no verbatim quote to test, or the wording differs. | yes |
| `partial` | The source supports part of the record; another part (a date, an attribution, a clause) is not supported. The `note` says which. | yes |
| `secondary-only` | Only a secondary source could be read; the original was not seen. | yes |
| `unreachable` | The cited source could not be opened (paywall, removed page, no copy available). | yes |
| `not-found` | The source was read and does not contain the quote or the claim. | no |
| `contradicted` | The source says something different: another speaker, another date, another publication. | no |

Checks made before the public release sometimes call the summary `what_they_saw`, its earlier name, and refer to local copies of sources and to research scripts that are not in this repository.

## Writing YAML

- Put dates in double quotes: `date: "1938"`. Without quotes, `1938` is read as a number and fails.
- For long text, write `>-` after the key and put the text on the following lines, indented two spaces more than the key. Inside such a block, colons, quote marks and apostrophes need no escaping.
- On one line, a value that contains `: ` (colon and space) or starts with a quote mark must be put in double quotes.
- Indent with spaces, never tabs.
- `intensity` is a number without quotes. `quote_found` and `is_translation` are `true` or `false` without quotes.

## Translation files

`translations/tr/<YYYY>/<id>.yaml` holds the Turkish for the record with the same id. All current files were machine-translated, and each says so in its first line and in `translated_by`. Turkish originals are not translated: when the quote is already Turkish, the file repeats it and sets `quote_kind: original-turkish`.

This is `translations/tr/1926/rabindranath-tagore-1926.yaml`:

```yaml
# Turkish for data/voices/1926/rabindranath-tagore-1926.yaml. Machine translation; corrections welcome.
# source_fingerprints: which English each field was translated from. Leave them as they are.
# yaml-language-server: $schema=../../../schema/translation.schema.json
id: rabindranath-tagore-1926
voice: Rabindranath Tagore
role: Şair, Nobel ödüllü
quote: bize uygarlığın yolunu gösterdi
quote_kind: translated
summary: >-
  İstanbul'da basına Türk cumhurbaşkanının uygarlığın yolunu gösterdiğini söyledi ve devrime Doğu dünyası
  adına büyük değer verdi.
caveat: Hiç karşılaşmadılar; tek temas 1926'daki uğrama ziyaretiydi.
mediated_by: Özveren, Jassal & Turan içinde ← Cumhuriyet 23 Kasım 1926; Rozana Hamdard Aralık 1926
verification_note: >-
  Gazetecilik ürünü ikincil kaynak; alıntı Türkçeden İngilizceye geri çeviridir; "they never met" kontrol
  edilmedi.
verification_method: kaynak getirme
translated_by: "machine: Gemini 4 Argon (2026-11-08)"
source_fingerprints:
  voice: d51ef5f1e69f
  role: 4335f073f951
  quote: 835350f6371a
  summary: 8b21f1a95f81
  caveat: fef678b36ce4
  mediated_by: ae1411d056bc
  verification_note: fc3cb852cd47
  verification_method: ad8cee67138e
```

| Key | Rule |
|---|---|
| `id` | Required. The id of an existing record in the same year folder. |
| `voice`, `role`, `summary`, `caveat`, `mediated_by` | Turkish for the record's field of the same name. Names usually stay as they are. |
| `quote` | The quote in Turkish: the speaker's own words if they are Turkish, otherwise a translation. |
| `quote_kind` | `original-turkish` (the speaker's own Turkish) or `translated`. |
| `verification_note`, `verification_method` | Turkish for `verification.note` and `verification.method`. |
| `translated_by` | Who translated: `"machine: <model> (<date>)"`, or a name or GitHub handle. |
| `reviewed_by` | A list of names or GitHub handles of people who reviewed the Turkish. |
| `source_fingerprints` | For each translated field, a fingerprint of the English it was translated from. |

No other keys are allowed.

### Fingerprints and stale fields

A fingerprint is the first 12 hexadecimal characters of the SHA-1 hash of the English text of a field. For `quote`, the hashed text combines `quote.text`, `quote.translation` and `quote.note` in one string. The code is `translatable()`, `quoteString()` and `fingerprint()` in [`tools/lib/records.mjs`](../tools/lib/records.mjs).

When someone edits the English of a record, the fingerprints of the changed fields no longer match. Those Turkish fields are "stale": the exhibition shows the English for them until they are translated again. The validator reports stale fields as notices, not errors, and prints the new fingerprint to use once the field has been retranslated.

### Correcting a Turkish translation

1. Edit the Turkish text in the translation file.
2. Leave `source_fingerprints` as it is. The fingerprint records which English you translated from, and that has not changed.
3. Add your name or GitHub handle to `reviewed_by`, for example `reviewed_by: [your-handle]`.

If the validator says a field is stale, translate it again from the record's current English, then set that field's fingerprint to the value the validator prints.

## What the exhibition shows

A record appears in the exhibition when all of these hold:

- it has a `verification` block;
- its verdict is not `not-found` or `contradicted`;
- its `voice_type` is not `self`.

Every other record stays in the data. A new record can therefore be merged before it has been checked; it appears on the site once someone other than its author has re-opened the source and a `verification` block has been added. The exhibition shows each record's check next to its source.

The Turkish exhibition uses a translated field only while its fingerprint matches. Otherwise, and for records without a translation file, it shows the English.

## The validator

`npm run validate` (the code is [`tools/validate.mjs`](../tools/validate.mjs)) checks every record and translation file. It runs on pull requests and on pushes to `main`, and you can run it locally:

```sh
npm run validate                                          # check everything
npm run validate -- data/voices/1938/lebrun-1938.yaml     # check everything, report only on this file
npm run validate -- --quiet                               # report errors only
```

It reports errors (the run fails), warnings and notices (the run passes). It checks:

- YAML syntax;
- the schema: required fields, unknown keys (with a suggestion for a misspelling), allowed values, types and formats;
- that `id` equals the file name and is unique;
- that the file is in the year folder of its `date`, and that the date is a real calendar date;
- that `era` agrees with `date`;
- the length of `summary` (warning above 25 words);
- that no `<placeholder>` from the template is left in a value;
- that `quote.text` contains no translation (it belongs in `quote.translation`);
- possible duplicates: the same voice on the same date (warning);
- translation files: schema, a matching record in the same year folder, empty fields, and stale fields (notice);
- on a pull request: any change to a `verification` block (notice, for the maintainer).
