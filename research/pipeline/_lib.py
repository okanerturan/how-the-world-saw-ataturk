import os, re

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "vault")


def note(folder, name, fm, body):
    d = os.path.join(ROOT, folder)
    os.makedirs(d, exist_ok=True)
    lines = ["---"]
    for k, v in fm.items():
        if isinstance(v, list):
            lines.append(f"{k}: [{', '.join(v)}]")
        else:
            lines.append(f"{k}: {v}")
    lines.append("---")
    lines.append("")
    lines.append(f"# {name}")
    lines.append("")
    lines.append(body.strip())
    lines.append("")
    path = os.path.join(d, name + ".md")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    return path


def person(name, **kw):
    fm = {
        "type": "person",
        "role": kw.get("role", ""),
        "nationality": kw.get("nat", ""),
        "lifespan": kw.get("life", ""),
        "stance": kw.get("stance", ""),
        "tags": ["person"] + kw.get("tags", []),
    }
    return note("People", name, fm, kw["body"])


def links(*items):
    return "\n\n## Threads\n" + "\n".join(f"- [[{i}]]" for i in items)
