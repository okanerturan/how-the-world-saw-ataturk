# -*- coding: utf-8 -*-
import os, re, collections
from _lib import ROOT, note

# ---- collect all people + their frontmatter ----
people = {}
for fn in os.listdir(os.path.join(ROOT, "People")):
    if not fn.endswith(".md"):
        continue
    name = fn[:-3]
    txt = open(os.path.join(ROOT, "People", fn), encoding="utf-8").read()
    fm = txt.split("---")[1]
    def get(k):
        m = re.search(rf"^{k}: (.*)$", fm, re.M)
        return m.group(1).strip() if m else ""
    people[name] = dict(role=get("role"), stance=get("stance"), tags=get("tags"))

def bullets(names):
    out = []
    for n in sorted(names, key=lambda s: s.lower()):
        p = people[n]
        out.append(f"- [[{n}]] — *{p['role']}* · {p['stance']}")
    return "\n".join(out)

def has(n, *tags):
    return any(t in people[n]["tags"] for t in tags)

def stance_has(n, *words):
    s = people[n]["stance"].lower()
    return any(w in s for w in words)

admirers = [n for n in people if has(n, "admirer", "imitator", "ally", "parallel", "influence", "convert") ]
antagonists = [n for n in people if has(n, "antagonist", "victim", "dissident", "conflicted")]
turkish = [n for n in people if has(n, "turkish", "ottoman", "inner-circle", "family", "personal", "kurdish")]
diplo = [n for n in people if has(n, "diplomat", "observer", "biographer", "military")]
exiles = [n for n in people if has(n, "exile", "german-exiles")]
nazi = [n for n in people if has(n, "nazi-thread")]
women = [n for n in people if has(n, "women")]
literary = [n for n in people if has(n, "literary", "arts")]

note("Maps", "MOC — Admirers", {"type": "moc", "tags": ["moc"]}, f"""
Everyone who looked at Ankara and liked what they saw — allies, imitators, students and
ideological borrowers. The incoherence of this list is the point: see [[Mustafa Kemal Atatürk]].

{bullets(admirers)}
""")

note("Maps", "MOC — Antagonists and Victims", {"type": "moc", "tags": ["moc"]}, f"""
Enemies, reactionaries, purged allies, and people the revolution simply ran over.

{bullets(antagonists)}
""")

note("Maps", "MOC — Inner Circle and Turkish Figures", {"type": "moc", "tags": ["moc"]}, f"""
The Ottoman old guard, the founding circle, the family, and the Turks and Kurds who lived inside
the revolution rather than watching it.

{bullets(turkish)}
""")

note("Maps", "MOC — Foreign Observers and Diplomats", {"type": "moc", "tags": ["moc"]}, f"""
Ambassadors, correspondents, generals and biographers — the people who explained Turkey to the
outside world, or failed to.

{bullets(diplo)}
""")

note("Maps", "MOC — Exiles Turkey Sheltered", {"type": "moc", "tags": ["moc"]}, f"""
The strangest through-line in the vault: a fiercely nationalist, anti-communist one-party state that
became a sanctuary — for Stalin's greatest enemy, for hundreds of Jewish academics fleeing Hitler,
and for failed modernizers from Kabul.

The mechanism was not primarily humanitarian. The [[1933 University Reform]] fired two-thirds of the
Istanbul faculty and created a vacuum that Europe's persecuted intellectuals were recruited to fill.

{bullets(exiles)}
""")

note("Maps", "MOC — The Nazi Thread", {"type": "moc", "tags": ["moc"]}, f"""
The conversation these notes grew out of, before it pivoted to Atatürk. Start at [[Nazi Racial
Hierarchy]] and [[Nazi Outreach to the Muslim World]].

{bullets(nazi)}
""")

note("Maps", "MOC — Women of the Revolution", {"type": "moc", "tags": ["moc"]}, f"""
[[Women's Suffrage in Turkey]] arrived in 1934, ahead of France and Italy — granted from the top,
which meant crushing the woman who had demanded it from below.

{bullets(women)}
""")

note("Maps", "MOC — Writers and Artists", {"type": "moc", "tags": ["moc"]}, f"""
Poets, novelists, film-makers and the people who fixed Atatürk's image in culture.

{bullets(literary)}
""")

ev = sorted(f[:-3] for f in os.listdir(os.path.join(ROOT, "Events")) if f.endswith(".md"))
co = sorted(f[:-3] for f in os.listdir(os.path.join(ROOT, "Concepts")) if f.endswith(".md"))
note("Maps", "MOC — Events", {"type": "moc", "tags": ["moc"]},
     "Chronological spine of the vault.\n\n" + "\n".join(f"- [[{e}]]" for e in ev))
note("Maps", "MOC — Concepts", {"type": "moc", "tags": ["moc"]},
     "Ideas, doctrines and machinery.\n\n" + "\n".join(f"- [[{c}]]" for c in co))

# ---- link audit ----
existing = set()
for d, _, fs in os.walk(ROOT):
    for f in fs:
        if f.endswith(".md"):
            existing.add(f[:-3])

broken = collections.defaultdict(list)
for d, _, fs in os.walk(ROOT):
    for f in fs:
        if not f.endswith(".md"):
            continue
        txt = open(os.path.join(d, f), encoding="utf-8").read()
        # normalise wikilinks broken across newlines
        txt = re.sub(r"\[\[([^\]]*?)\]\]", lambda m: "[[" + " ".join(m.group(1).split()) + "]]", txt)
        for target in re.findall(r"\[\[([^\]|#]+)", txt):
            t = target.strip()
            if t not in existing:
                broken[t].append(f[:-3])

for t, srcs in sorted(broken.items()):
    print(f"BROKEN: {t!r}  <- {sorted(set(srcs))}")
print(f"\nnotes: {len(existing)} | broken targets: {len(broken)}")
