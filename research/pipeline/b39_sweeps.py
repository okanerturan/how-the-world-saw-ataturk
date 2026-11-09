# -*- coding: utf-8 -*-
# Census rounds 30-31 (5 Nov 2026): notes built directly from the merged records in data/gazes.jsonl,
# so a note and its records cannot drift apart. Round 30: Monid search sweep of 546 world leaders and
# writers (Exa + SerpApi Google Books), leads verified at source. Round 31: contemporary first-hand
# contacts of major figures (letters, meetings), per Okan's first-hand contact rule.
import json, os
from _lib import note
HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data", "gazes.jsonl")

NODES = {
 "World Leaders on Atatürk — Round 30 Sweep": dict(when="1921-2026", tags=["event", "verified", "leaders", "sweep"],
   intro="Heads of state and government, ministers and party leaders found by the round-30 Monid sweep (Exa web search and SerpApi Google Books over 546 names not yet in the census) and verified at the source: official transcripts, presidency and UN sites, the press of record. Wreath-laying, protocol formulas and labels were rejected; each record below is the speaker's own stated view of Atatürk. Translations are marked."),
 "Writers and Thinkers on Atatürk — Round 30 Sweep": dict(when="1943", tags=["event", "verified", "writers", "sweep"],
   intro="Writers found by the round-30 sweep and verified at the source."),
 "Statesmen and Royals in Contact with Kemal, 1919–1938": dict(when="1921-1937", tags=["event", "verified", "contemporary", "contact"],
   intro="Contemporary records for major statesmen and royals: their own words about Kemal, or a documented first-hand contact with him (a letter, a meeting or audience, a substantive exchange). Under the census's first-hand contact rule (5 Nov 2026) such contacts count for major figures even without a stated opinion; form telegrams and protocol do not. Most texts come from the editors' notes in Atatürk'ün Bütün Eserleri and from Şimşir's published British documents."),
 "Funeral Voices — Round 32": dict(when="1938-11", tags=["event", "verified", "funeral"],
   intro="Voices from the weeks of Atatürk's death and funeral (10 November 1938 to January 1939) found in rounds 32–33 and verified at source."),
 "Turkish Writers and Contemporaries on Kemal — Round 33": dict(when="1919-1990", tags=["event", "verified", "turkey"],
   intro="Turkish writers, thinkers, comrades, family and opponents, in their own documented words about Kemal or in documented first-hand contact with him (round 33). Many had vault notes built from the project's original unsourced transcript; these records are what survives verification."),
 "Writers, Scientists and Artists in Contact with Kemal, 1919–1938": dict(when="1919-1938", tags=["event", "verified", "contemporary", "contact"],
   intro="Contemporary records for world-famous writers, scientists and artists: their own words about Kemal, or a documented first-hand contact with him (a letter, a meeting, a substantive exchange), under the census's first-hand contact rule (5 Nov 2026)."),
}

recs = [json.loads(l) for l in open(DATA, encoding="utf-8")]
for node, meta in NODES.items():
    R = sorted([r for r in recs if r["node"] == node], key=lambda r: (r["date"] or "", r["voice"]))
    if not R:
        continue
    parts = [meta["intro"], ""]
    srcs = []
    for r in R:
        parts.append(f"## {r['voice']}, {r['date']}")
        parts.append(f"*{r['role']}* — {r['polarity']}, {r['artifact']}, evidence {r['evidence']}.")
        parts.append("")
        parts.append(r["what_they_saw"])
        parts.append("")
        parts.append(f"> {r['quote']}")
        parts.append("")
        if r.get("mediated_by"):
            parts.append(f"Mediated by: {r['mediated_by']}.")
            parts.append("")
        if r.get("caveat"):
            parts.append(f"⚠️ {r['caveat']}")
            parts.append("")
        for s in r["sources"]:
            if s not in srcs:
                srcs.append(s)
    parts.append("## Sources")
    parts += [f"- {s}" for s in srcs]
    note("Events", node, {"type": "event", "when": meta["when"], "tags": meta["tags"]}, "\n".join(parts))
    print(node, len(R))
