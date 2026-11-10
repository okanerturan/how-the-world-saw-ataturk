# Agent brief — census research rounds

Shared instructions for every research agent. Consolidated 2026-11-01 from the round 3–8 briefs. The task
prompt names your **slug**, your **round number N**, your **script number** and your **candidates file**.

## Read first
`HUNT.md` (mission, datum schema, coverage, seams), `RESEARCH.md` §4 (what "verified" means) and §6 (the ten
mirrors), the top of `LEDGER.md` (evidence tiers P/S/J/F/T/M), `data/README.md` (gaze record schema and the
checks), and the most recent `bNN_*.py` scripts for the style of verified nodes.

## Paid web access — only through `tools/ms`
`S=research/pipeline/ms`
- `$S search "q" [n] [snippet_len 180–10000]` Keenable $0.004 · `$S exa "q" [n]` $0.011 · `$S fetch URL…` free full text
  (DergiPark PDFs, Papers Past, Gallica ContentSearch, loc.gov JSON, Wikisource all work) · `$S render URL`
  $0.002 JS page · `$S shot URL out.png` $0.002 · `$S browse URL "goal" [steps] [stealth]` **$0.016/step**.
- One call at a time. **Never run `$S` in the background or leave a call in flight when you stop**: a call killed
  mid-flight leaves `/tmp/inflow.lock` stale and blocks everyone. If the wrapper seems blocked for more than
  5 minutes, run `pgrep -fl "inflow aep"`. If it prints nothing and `/tmp/inflow.lock` exists, the lock is stale:
  `rmdir /tmp/inflow.lock`. (`pgrep -x inflow` always matches the vault daemon, so don't use it.)
- **Exit 99 / "INFLOW STOPPED": stop all wrapper use, do not retry**, finish with free sources, and say so in your
  report. Exit 3 = a provider failed; you may try another engine once.
- Budget per agent unless the task says otherwise: ≤ 15 search/exa, ≤ 2 browse runs (≤ 25 steps), ≤ 30
  render/shot. Free direct APIs (archive.org, Hansard API, Delpher SRU, Chronicling America tiles, TBMM PDFs,
  Aozora) may be called with curl/python directly, politely, with short sleeps.
- `browse` output is an AI agent's report, not a document. Before quoting anything from it, confirm the text by
  a second retrieval of the page itself (one NewspaperSG transcription was partly hallucinated).
- Do not use the WebSearch/WebFetch tools.
- **Free: archive.org full-text search** — `python3 -I tools/fts.py '<query>' [hits]` returns snippets from inside
  books, including lending-only ones, without a login (filters: `identifier:`, `creator:(...)`, `title:(...)`, phrases,
  AND/OR). Slow (30–90 s per query): run single queries in the foreground, never a long loop. Snippets only: quote
  ≤ a sentence, cite identifier + page if the snippet or the book's index shows it. Open items (no
  `access-restricted-item`) can be read in full via `/download/<id>/<file>_djvu.txt`.

## Evidence standard
A gaze is verified only if ≥ 1 S- or P-tier source (or ≥ 2 independent J-tier sources) supports the specific
claim, and you have read the supporting text. Training memory is tier M: fine for leads, never for a claim.
Record dry ends honestly ("⌀ dug, nothing yet"). Prefer fewer solid nodes. Sensitive threads (Armenian
genocide memory, Kurdish revolts, Smyrna 1922, Law 5816 in Turkey): full sourcing, neutral voice — never adopt a
speaker's framing as the vault's own.

**Books:** download full text only where it is served openly (Internet Archive open items, HathiTrust full
view, Gallica, Gutenberg). For copyrighted or lending-only items, use search-inside snippets and page numbers
only. Keep quotes to a sentence or two. A site that answers a script with a bot check is opened in a real
browser instead; a login or a loan needs an account of the person running the hunt.

## What you write (only these; other agents work in parallel)
1. `bNN_<slug>.py` — modelled on recent scripts: `from _lib import note, person`; tags include "verified";
   every body ends with `## Sources`. Wikilinks only to notes that exist or that your script creates; never
   across a line break. **Note titles must not contain `: * " \ / < > | ? #`** (Obsidian forbids them) — use
   " — " for a colon. Before naming a note, `ls vault/People vault/Events` and `grep` `data/gazes.jsonl` for the
   voice; never duplicate an existing note — add a dated record pointing at it instead. Run the script once.
   Do not run b5/b6/b12 or edit other scripts.
2. Your candidates file — mark promotions, add tiered leads with next steps, record dry ends.
3. `tools/.state/round<N>/ledger_<slug>.md` — LEDGER rows (`| Claim | Node | Status | Sources | Next step |`).
4. `tools/.state/round<N>/gazes_<slug>.jsonl` — one record per gaze, exactly per `data/README.md` (field order,
   enums, ≤ 25-word `what_they_saw`, verbatim quotes only; translated quotes marked as translation, original in
   the note). Cite the exact location (book+page, issue+page, contribution URL, Gallica ark+view) so the checker
   can find it. Validate before finishing.
Do not edit `data/gazes.jsonl`, `data/checks.jsonl`, `LEDGER.md`, `HUNT.md` or `README.md`; the main agent
merges after the independent check.

## Priorities (as of round 10)
**Notable voices first (user's rule, 1 Nov 2026):** the finished product needs recognisable names: heads of state,
ministers, famous writers, revolutionaries and religious leaders, in their own words. A random journalist or an anonymous
editorial has no impact; stage it only if the paper is itself a major institution taking a striking stance.
The dataset is 48% admiring, 62% contemporary, ~39% second-hand. Buy primary, contemporary (1919–1938) and
non-admiring voices first. A wire report is not a gaze; a passing mention with no stated view is not a gaze.

**First-hand contact rule (user, 5 Nov 2026):** for a MAJOR figure (head of state or government, world-famous writer,
scientist, artist or religious leader), a documented first-hand connection with Kemal counts even with no stated
opinion: a letter to or from him (e.g. Einstein's 1933 request letter), a meeting or audience, an exchange of
substance. Stage it with polarity `witness` (or the polarity the text supports), artifact `letter` or `meeting`,
and `what_they_saw` saying plainly what the contact was. Pure protocol (form congratulations, wreath-laying,
signature-only guestbook entries) still fails, and the rule does not apply to minor figures.

## Report back (final message, concise)
Records written (by era and polarity), notes created, upgrades to existing notes, dry ends, items needing a
human or browser, seam notes (archive · method · works?), paid calls used, any InFlow problem.
