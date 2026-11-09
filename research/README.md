# research/

How the archive was built. None of this is needed to contribute; it is here so the method can be checked.

| | |
|---|---|
| `RESEARCH.md` | the question, the method, and the ten "mirrors" (what each voice saw in him) used in the `mirror` field |
| `HUNT.md` | the search log: which archives were searched, how, and what is still open |
| `LEDGER.md` | every decision and correction, round by round, including the source-check corrections |
| `candidates/` | leads found but not yet turned into records — a good place to start if you want to help |
| `pipeline/` | the scripts and agent brief used during the census (Oct–Nov 2026). They read the dataset's first format (`data/gazes.jsonl`, now one YAML file per voice) and call paid search services through `ms`; they are kept as a record of the method and will not run as they are. |

The census was run largely by AI research agents searching public archives (newspaper archives such as Gallica, Delpher, Hansard, Chronicling America and the TBMM minutes; digital libraries; scholarship), each record extracted from a research note in `../vault/`, and then re-checked by a separate checker that re-opened the source. The check is stored in each record's `verification` block.
