# -*- coding: utf-8 -*-
# Datum layer: validates data/gazes.jsonl and writes a per-note summary of its records back into
# the frontmatter of the vault notes they come from (gazes, polarity, mirror, era), so Dataview
# can slice the vault by the same fields the visualization will use. Run after b0–b11, before b5.
import json, os, re, sys
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.abspath(__file__))
VAULT = os.path.join(ROOT, "vault")
DATA = os.path.join(ROOT, "data", "gazes.jsonl")

ENUMS = {
    "voice_type": {"person", "press", "institution", "collective", "self"},
    "domain": {"politics", "letters", "arts", "military", "religion", "science", "press", "sport", "diplomacy"},
    "era": {"contemporary", "funeral", "posthumous"},
    "mirror": {None, "anti-colonial-liberator", "secular-rationalist-prophet", "volkisch-purifier",
               "bourgeois-revolutionary", "nation-forge-template", "apostate", "emancipator-patriarch",
               "chivalrous-enemy", "internal-mirror", "modernization-poster-child"},
    "polarity": {"admiring", "hostile", "conflicted", "instrumental", "witness"},
    "intensity": {1, 2, 3},
    "artifact": {"quote", "editorial", "article", "poem", "book", "speech", "policy", "visit", "telegram",
                 "memoir", "artwork", "monument", "ceremony", "nomination", "broadcast", "report", "letter", "meeting"},
}
FIELDS = ["id", "voice", "voice_type", "role", "country", "country_now", "domain", "date", "era", "mirror",
          "polarity", "intensity", "what_they_saw", "quote", "artifact", "evidence", "mediated_by",
          "caveat", "node", "sources"]
DATUM_KEYS = ("gazes", "polarity", "mirror", "era")


def note_paths():
    out = {}
    for folder in ("People", "Events", "Concepts"):
        d = os.path.join(VAULT, folder)
        for f in os.listdir(d):
            if f.endswith(".md"):
                out[f[:-3]] = os.path.join(d, f)
    return out


def load():
    recs, errs, ids = [], [], set()
    for n, line in enumerate(open(DATA, encoding="utf-8"), 1):
        if not line.strip():
            continue
        r = json.loads(line)
        if list(r) != FIELDS:
            errs.append(f"line {n}: fields {sorted(set(FIELDS) ^ set(r))}")
        for k, allowed in ENUMS.items():
            if r.get(k) not in allowed:
                errs.append(f"line {n} ({r.get('id')}): {k}={r.get(k)!r}")
        if r["id"] in ids:
            errs.append(f"line {n}: duplicate id {r['id']}")
        ids.add(r["id"])
        recs.append(r)
    return recs, errs


def write_frontmatter(path, summary):
    text = open(path, encoding="utf-8").read()
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    lines = [l for l in m.group(1).split("\n") if l.split(":", 1)[0] not in DATUM_KEYS]
    lines += [f"{k}: {v}" for k, v in summary.items()]
    open(path, "w", encoding="utf-8").write("---\n" + "\n".join(lines) + "\n---\n" + text[m.end():])


recs, errs = load()
paths = note_paths()
errs += [f"{r['id']}: unknown node {r['node']!r}" for r in recs if r["node"] not in paths]
if errs:
    print("gazes.jsonl INVALID:\n  " + "\n  ".join(errs[:40]))
    sys.exit(1)

by_node = defaultdict(list)
for r in recs:
    by_node[r["node"]].append(r)
for node, rs in by_node.items():
    def uniq(k):
        return "[" + ", ".join(sorted({r[k] for r in rs if r[k]})) + "]"
    write_frontmatter(paths[node], {"gazes": len(rs), "polarity": uniq("polarity"),
                                    "mirror": uniq("mirror"), "era": uniq("era")})

pol = Counter(r["polarity"] for r in recs)
print(f"datum: {len(recs)} gazes from {len({r['voice'] for r in recs})} voices in {len(by_node)} notes"
      f" | {dict(pol)}")
