#!/usr/bin/env python3
"""archive.org full-text search: snippets from INSIDE books, including lending-only ones (free, no login).

usage: python3 -I tools/fts.py '<query>' [hits=20]
  query examples:  '"roughneck of dictators"'   'Kemal AND identifier:insideeurope00gunt'
                   'Ataturk AND creator:(Koestler)'   '"Mustapha Kemal" AND title:(diaries)'
Each hit prints identifier, year, title, creator, then the highlighted snippets ({{{term}}}).
Slow (30-90 s); run one query at a time. Snippets only: quote at most a sentence, cite the identifier.
"""
import json, sys, urllib.parse, urllib.request

q = sys.argv[1]
n = sys.argv[2] if len(sys.argv) > 2 else "20"
u = ("https://archive.org/services/search/beta/page_production/?service_backend=fts&hits_per_page=" + n
     + "&user_query=" + urllib.parse.quote(q))
try:
    d = json.load(urllib.request.urlopen(u, timeout=150))
except Exception as e:
    sys.exit("fts error: %s" % e)


def walk(o):
    if isinstance(o, dict):
        if "hits" in o and isinstance(o["hits"], dict) and "hits" in o["hits"]:
            print("total", o["hits"].get("total"))
            for h in o["hits"]["hits"]:
                f = h.get("fields", {})
                print("*", f.get("identifier"), f.get("year") or f.get("date"), (f.get("title") or "")[:70], f.get("creator") or "")
                for t in ((h.get("highlight") or {}).get("text") or []):
                    print("    ", t.replace("\n", " ")[:500])
        for v in o.values():
            walk(v)
    elif isinstance(o, list):
        for v in o:
            walk(v)


walk(d)
