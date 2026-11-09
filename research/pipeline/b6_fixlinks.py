# -*- coding: utf-8 -*-
import os, re
from _lib import ROOT

fixed = 0
for d, _, fs in os.walk(ROOT):
    for f in fs:
        if not f.endswith(".md"):
            continue
        p = os.path.join(d, f)
        txt = open(p, encoding="utf-8").read()
        new = re.sub(r"\[\[([^\]]*?)\]\]",
                     lambda m: "[[" + " ".join(m.group(1).split()) + "]]",
                     txt, flags=re.S)
        if new != txt:
            open(p, "w", encoding="utf-8").write(new)
            fixed += 1

# strict re-audit: links must be single-line
existing = {f[:-3] for d, _, fs in os.walk(ROOT) for f in fs if f.endswith(".md")}
broken, total = set(), 0
for d, _, fs in os.walk(ROOT):
    for f in fs:
        if not f.endswith(".md"):
            continue
        txt = open(os.path.join(d, f), encoding="utf-8").read()
        assert "\n" not in "".join(re.findall(r"\[\[[^\]]*\]\]", txt, re.S)), f
        for t in re.findall(r"\[\[([^\]|#]+)\]\]", txt):
            total += 1
            if t not in existing:
                broken.add((t, f[:-3]))

for t, src in sorted(broken):
    print(f"BROKEN: {t!r} <- {src}")
print(f"rewrapped {fixed} files | {len(existing)} notes | {total} links | {len(broken)} broken")
