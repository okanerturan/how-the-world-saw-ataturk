Türkçe için: [CONTRIBUTING.tr.md](CONTRIBUTING.tr.md)

# Contributing

This archive grows when people add voices they have found in sources and fix errors they have seen. This page says what is accepted, what evidence is needed, how to send it, and what happens next.

You can write issues and pull request descriptions in Turkish or English.

## Where to start

If you have a voice and its source in hand, go to [Three ways to help](#three-ways-to-help). If you want to help and are looking for something to do, these are open now:

- About 300 quotes have no English translation ([#6](https://github.com/okanerturan/how-the-world-saw-ataturk/issues/6)).
- The Turkish translations were made by machine and need readers ([#9](https://github.com/okanerturan/how-the-world-saw-ataturk/issues/9)).
- Every record needs someone to re-open its source: see [Checking a record](#checking-a-record). Eleven records cite a source nobody could open ([#5](https://github.com/okanerturan/how-the-world-saw-ataturk/issues/5)).
- Some texts are known to exist and have not been reached. The issues titled "Wanted" name four of them; [`research/candidates/`](research/candidates/) and the section "Open leads that need a person" in [`research/HUNT.md`](research/HUNT.md) list more, by region.

## What counts as a voice

A voice is an identifiable person, newspaper, institution or collective expressing a view of Atatürk, at a known time, in a source you can point to. Some examples already in the archive:

- a person: Rabindranath Tagore telling the Istanbul press in November 1926 that the Turkish president "showed us the way to civilization" (`data/voices/1926/rabindranath-tagore-1926.yaml`);
- a newspaper: the Swedish daily Aftonbladet in November 1938 (`data/voices/1938/aftonbladet-1938.yaml`);
- an institution: the Fourth Congress of the Communist International in 1922 (`data/voices/1922/comintern-4th-congress-1922.yaml`);
- a collective: the Al-Islam Congress of Java Muslims at Cheribon in October 1922 (`data/voices/1922/al-islam-congress-cheribon-1922-10.yaml`). A collective has no single named speaker, but the source identifies the group, the place and the date.

For major figures (heads of state, well-known writers, scientists, religious leaders) documented first-hand contact with him also counts, even when they state no view: a meeting, a visit, a letter. An example is Edward VIII's visit in September 1936 (`data/voices/1936/edward-viii-1936-09.yaml`). Such records usually have `polarity: witness`.

One record is one voice at one moment. If the same person spoke about him twice, with different views or years apart, that is two records.

## What is not accepted

- Personal opinions about Atatürk, yours or anyone else's, that have not been published in a source.
- Claims without a source, or with a source that does not contain the passage.
- Social media posts by private individuals.
- Insults, in a suggestion or in comments.
- Anything written for this archive: statements made to us, or given at our request. A voice must come from a source that exists independently of the archive.
- Quotation websites, collections of sayings and images with a quote on them, as sources. If a well-known quote has no traceable source, it cannot go in as that person's words. If you can find where it was first printed, that source is a contribution.

## Evidence standards

- **Prefer primary sources:** the speaker's own text, a newspaper of the time, a parliamentary record, a letter, an archive document. A scholarly book or article that quotes the primary source is fine; record the chain in `mediated_by`, for example `"Toksoy 2006 ← Cumhuriyet 14 Nov 1938"`.
- **Give the page.** For a book, a journal or a printed newspaper, give the page (or column or folio). For a website, give the link, and if possible an archived copy from the [Wayback Machine](https://web.archive.org/).
- **Quote verbatim, in the original language.** Copy the words exactly as the source prints them, including old spelling and misprints: if a paper prints "Piluski" for Piłsudski, the quote keeps "Piluski", the translation says Piłsudski, and `caveat` notes the misprint. Mark left-out words with `…`. If the quote is not in English, add an English translation in its own field (`quote.translation`). Do not put a translation in place of the original. If the source itself gives only a translation (a Turkish newspaper's version of a speech made in German, say), quote that as printed and set `quote.is_translation: true`.
- **The summary is ours.** `summary` is a neutral paraphrase, in English, of what the voice saw in him, in 25 words or fewer. It reports what they said ("Called him…", "Praised…", "Condemned…") and adds no judgement of our own.
- **Describe the speaker as the source does.** `role` says who they were when they spoke, in a few words. Leave out what they became later.
- **Write down your doubts.** If there is only one source, if the date is approximate, or if the attribution is uncertain, say so in `caveat`.
- **Polarity is the speaker's stance, as the source shows it.** It is not our view of the speaker, and not our view of Atatürk.

The full list of fields and allowed values is in [data/README.md](data/README.md).

## Three ways to help

In order of ease. A record's `summary` and `role` are written in English. If you would rather write in Turkish, use an issue form; the maintainer or another contributor can write the record from it.

### 1. Open an issue with a form

You only need a GitHub account. Choose a form:

- [Suggest a voice / Söz öner](https://github.com/okanerturan/how-the-world-saw-ataturk/issues/new?template=suggest-voice.yml): a voice that is not in the archive yet.
- [Correction / Düzeltme](https://github.com/okanerturan/how-the-world-saw-ataturk/issues/new?template=correction.yml): something wrong in a record.
- [Check a record / Kayıt doğrula](https://github.com/okanerturan/how-the-world-saw-ataturk/issues/new?template=check-record.yml): you re-opened a record's source and can say what it prints.
- [Translation fix / Çeviri düzeltmesi](https://github.com/okanerturan/how-the-world-saw-ataturk/issues/new?template=translation.yml): a better Turkish wording.

Before suggesting a voice, search for the name in the [exhibition](https://ataturk.fyi) or in this repository, to see whether it is already there. The maintainer or another contributor turns a good suggestion into a record and links it in the issue.

### 2. Add or edit a file in the browser

No software is needed; GitHub's web editor is enough.

To add a record:

1. Open the [template](data/templates/voice.yaml), click "Raw", and copy all of it.
2. Go to `data/voices/` and open the year folder of the voice's date, for example `data/voices/1938/`.
3. Click "Add file", then "Create new file". GitHub will ask you to fork the repository first; accept.
4. Name the file `<id>.yaml`, for example `firstname-lastname-1938.yaml`. If there is no folder for the year yet, start from `data/voices/` instead and type the year and a slash before the file name, for example `1951/firstname-lastname-1951.yaml`; GitHub creates the folder.
5. Paste the template and fill it in. Delete the optional lines you do not use, or leave them commented out.
6. Click "Commit changes…", then "Propose changes". GitHub opens a page for a pull request; click "Create pull request".

To correct a record, open its file, click the pencil icon ("Edit this file"), make the change, and continue from step 6.

The automatic check then runs on your pull request. If it reports a problem, it points to the line. Open the file from the "Files changed" tab of your pull request and edit it again; the pull request updates itself.

### 3. Work on your own computer

You need Git and Node.js 20 or later. Fork the repository on GitHub, clone your fork, and in its folder run:

```sh
npm install
npm run new -- "Voice Name" 1938-11-10   # writes data/voices/1938/voice-name-1938.yaml from the template
# fill in the new file
npm run validate                          # must end with OK
```

`npm run new` fills in `id`, `voice`, `date`, and `era` when the date decides it. It never overwrites a file. If the id is taken, or the name has no Latin letters (Chinese, Arabic, Russian …), give the id yourself with `--id`, for example `npm run new -- "Voice Name" 1938-11-10 --id voice-name-1938-11-10`. `npm run validate -- <file>` reports on one file only.

Then commit, push to your fork, and open a pull request.

## Fixing a Turkish translation

The Turkish text for each record is in `data/translations/tr/<YYYY>/<id>.yaml`, with the same year folder and file name as the record. These files were made by machine translation, and many can be improved.

1. Open the file and edit the Turkish text.
2. Leave `source_fingerprints` as it is. It records which English text the field was translated from, and correcting the Turkish does not change that.
3. Add yourself to `reviewed_by`:

   ```yaml
   reviewed_by:
     - your-github-handle
   ```

When `quote_kind` is `original-turkish`, the quote is the speaker's own Turkish, copied from the record. Correct it only to match the source, and correct `quote.text` in the record too.

If you prefer not to edit files, use the [Translation fix / Çeviri düzeltmesi](https://github.com/okanerturan/how-the-world-saw-ataturk/issues/new?template=translation.yml) form.

## Checking a record

Every record must be checked by someone other than the person who added it. The checker re-opens the cited source and looks for the quote, the speaker, the date and the occasion.

To send a check, use the [Check a record / Kayıt doğrula](https://github.com/okanerturan/how-the-world-saw-ataturk/issues/new?template=check-record.yml) form: name the record, say what you opened (the link, or the book and its page) and whether the words are there as quoted. If they differ, copy the source's wording. The maintainer writes your result into the record's `verification` block (see [data/README.md](data/README.md#verification)) with your name in `checked_by`.

A check that finds a problem is as welcome as one that confirms. Records whose check fails stay in the data, marked as such, and leave the exhibition.

Never add a `verification` block to a record you added yourself.

## What happens after you contribute

1. **Automatic check.** The validator (`npm run validate`) runs on every pull request. Errors must be fixed before a merge; warnings and notices do not block it.
2. **Maintainer review.** The maintainer reads the record against its source and may ask for changes or make small edits. The validator flags any change to a `verification` block so that the maintainer looks at it.
3. **Merge.** A merged record is part of the data at once. It appears in the exhibition only after someone other than its author has re-opened the source and filled in `verification`.

An issue is closed with a link to the new or corrected record, or with the reason it was not accepted.

## Moderation and the law

This archive is published from Turkey. Under Law No. 5816 (Atatürk Aleyhine İşlenen Suçlar Hakkında Kanun), insulting the memory of Atatürk is a crime.

The archive documents what historical voices said about him, each with its source. That includes hostile voices. A hostile record states who said it, when, and where it was printed, in a neutral summary and a short verbatim quotation. It records the speaker's view; it does not adopt it.

Every contribution is reviewed by the maintainer before it is merged. Issues, pull requests and comments that are opinion or abuse will be closed. See the [code of conduct](CODE_OF_CONDUCT.md).

## AI tools

You may use AI tools to search for voices, find sources or draft a translation. But you must have read the passage in the source yourself: the page, the scan or the printed text, not a summary of it. Never submit a quote you have not seen in the source. AI tools can produce quotes, page numbers and references that look real and do not exist.

If an AI tool helped you find something, say so in the issue or pull request.

## Licence of contributions

By contributing, you agree that your contribution is published under the project's licences: [CC BY 4.0](LICENSE-DATA.md) for data and text (`data/`, `vault/`, `research/`, translations) and [MIT](LICENSE) for code (`tools/`, `viz/`). Quotations remain the words of their speakers. Your name stays in the Git history of the files you changed.
