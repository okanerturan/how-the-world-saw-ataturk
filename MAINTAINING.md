# Maintaining the archive

For the maintainer and anyone helping review. Contributors start with [CONTRIBUTING.md](CONTRIBUTING.md).

## Reviewing a pull request

1. The automatic check (`npm run validate`) must be green. Its annotations point at the line to fix.
2. Open the source. Does it exist, does it say what the record says, is the quote verbatim and in the original
   language? If you can't open it, ask the contributor for a scan or the page, or merge without `verification`.
3. Read the summary: neutral, ≤ 25 words, nothing the source doesn't say.
4. Moderation. This archive is published from Turkey, where Law 5816 makes insulting Atatürk's memory a crime. It
   documents what historical voices said, with sources, and hostile voices belong in it. It does not publish the
   contributor's own opinions, insults, or text written for the archive. When a record is hostile, check that the
   wording is the source's, the source is real, and the summary describes rather than repeats. Close anything else
   with a short reason.
5. A pull request should not add or change `verification` for its own records. The validator flags it.
6. Merge. The record is now in the data; it reaches the exhibition once verified.

## Verifying a record

Someone other than the record's author re-opens the source and fills in `verification`:

```yaml
verification:
  verdict: confirmed          # confirmed · paraphrase-ok · partial · secondary-only · unreachable · not-found · contradicted
  quote_found: true
  checked_against: "Gallica, Le Temps 11 Nov 1938, p. 2, col. 3"
  method: read the page scan
  note: what you found, in a sentence or two
  checked_on: "2026-11-12"
  checked_by: your-github-handle
```

`not-found` and `contradicted` keep the record in the data (so the failure is documented) but out of the exhibition.
When re-checking, move the old block under `earlier:`.

Records waiting for a check: `npm run validate` lists them in its summary.

## Turkish translations

`node tools/translate-tr.mjs` translates every missing or stale field (needs the `agy` CLI with Gemini 4 Argon) and
leaves human corrections alone. Quotes spoken in Turkish are copied verbatim, never translated or modernised. People
who fix a translation add themselves to `reviewed_by`.

## Research agents

Agents adding records follow the same rules as people: `npm run new -- "Voice" YYYY-MM-DD`, fill in the fields from
the source, quote verbatim in the original language, add `sources` with page and an archived copy
(`npm run archive` finds or creates one), `npm run validate`. A different agent or person does the `verification`.
The older pipeline and its brief are in `research/pipeline/` for reference.

## Publishing the exhibition

```
npm ci && (cd viz && npm ci && npm run build)
wrangler pages deploy viz/dist --project-name the-long-thread --branch main
```

## Open data clean-ups

- 5 records have `quote.needs_split: true`: several passages and translations interleaved in one text.
- Some voices appear under slightly different names across records; a shared voice list is planned.
- Some sources have no archived copy yet: `npm run archive` adds existing Wayback snapshots, `npm run archive -- --save`
  asks the Wayback Machine to save the rest (about one a minute; some sites refuse).
