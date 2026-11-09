# -*- coding: utf-8 -*-
# Census round 17 (Nov 2026) — exiles, artists and Western women commentators.
# Seam: archive.org full-text search (tools/fts.py) located three open scans; each djvu text is banked in
# tools/.state/round17/ and every quote below is checked against it (OCR spacing/hyphenation normalised).
#   naked.txt   — Clare Sheridan, Naked Truth (1928), archive.org nakedtruth00sher
#   kaleid.txt  — Clare Sheridan, A Turkish Kaleidoscope (1926), archive.org in.ernet.dli.2015.175300
#   mills.txt   — Lady Dorothy Mills, Beyond the Bosphorus (1926), archive.org in.ernet.dli.2015.279689
#   wood.txt    — Ruth Frances Woodsmall, Moslem Women Enter a New World (1936; Bimla reprint), in.ernet.dli.2015.506177
import json, os, re
from _lib import note, person

HERE = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(HERE, "tools", ".state", "round17")
NODE = "Western Women Commentators on Atatürk, 1922–1936 — Sheridan, Mills, Woodsmall"


def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"').replace("—", "-")
    s = re.sub(r"-\s*\n", "", s)
    s = re.sub(r"\b\d{3}\s+LIFE\s+AS\s+A\s+JOURNALIST\b", " ", s)
    s = re.sub(r"\s+", " ", s).lower()
    s = re.sub(r"\s+([;:,.!?])", r"\1", s)
    s = re.sub(r"atat\w*", "ataturk", s)
    return s


def bank(n):
    return norm(open(os.path.join(STATE, n), encoding="utf-8").read())


R = [
 dict(id="clare-sheridan-1922-09", voice="Clare Sheridan", role="British sculptor and journalist; interviewed Mustafa Kemal at Smyrna, September 1922 (memoir of 1928)",
      c="United Kingdom", cn="United Kingdom", dom="letters", date="1922-09", era="contemporary", mirror=None, pol="admiring", inten=2,
      saw="Finds the Ghazi sphinx-like and unfathomable, with 'hard determination' in his blue eyes; calls him the one man who led the Turks to victory.",
      q="His sphinx-like expression and unsmiling ultra-politeness were to me quite unfathomable.",
      art="memoir", ev="P", med=None, src="naked.txt",
      cav="Clare Sheridan, Naked Truth (1928), ch. 'Life as a Journalist', p. 306 (the quote); pp. 302-303 ('the one man who from overwhelming defeat and humiliation had led the Turks to victory'); p. 308 (the sculptor's request, 'I will sit to you in Constantinople'; Latife Hanım 'had captured this adamantine Trotzki, so well worth capturing!'). Written six years after the Smyrna interview and so partly hindsight; the Smyrna fire is in the background, and Sheridan's account of it is not the vault's. Kemal's remarks to her as she records them (the English Government, not the English people, is against him; 'Our feeling against them [the Armenians] has nothing to do with religion') are his, not hers. The sitting for the bust did not take place in this book. Bodurgil's centennial bibliography lists a separate Sheridan article 'Smyrna, September 1922; interview with Mustapha Kemal' (not seen).",
      urls=["https://archive.org/details/nakedtruth00sher"],
      loc="Sheridan, Naked Truth (1928), pp. 302-303, 306, 308", link="Clare Sheridan",
      nxt="Locate the 1922 newspaper original of the Smyrna interview (Bodurgil 1984 entry 284); the 1923 Lausanne-period Sheridan articles the vault note mentions"),
 dict(id="clare-sheridan-1925", voice="Clare Sheridan", role="British sculptor and writer; A Turkish Kaleidoscope, written at the end of a stay in Turkey in 1925",
      c="United Kingdom", cn="United Kingdom", dom="letters", date="1925", era="contemporary", mirror=None, pol="conflicted", inten=2,
      saw="Says the Turks owe their existence as a nation to the Ghazi, but reports terror and an arbitrary tribunal, and repeats a drinking slur.",
      q="Nor had he anything with which to reproach her, except that she hampered his orgies of drunkenness",
      art="book", ev="P", med=None, src="kaleid.txt",
      cav="Clare Sheridan, A Turkish Kaleidoscope (London: Duckworth, 1926), chapter 'Civilisation Revealed', p. 215, about Mustafa Kemal's divorce of Latife Hanım (January 1925; Sheridan's text says the divorce had 'just' happened). Same chapter, p. 214: 'The Turkish people are easily led; and they owe to their Ghazi the fact of their existence to-day as a nation.' and 'Terror reigns, and the Tribunal of Independence is as arbitrary as the Cheka.' The chapter reproduces the hat speech of Inebolu (24 Aug 1925) from the French edition of Cumhuriyet of 29 Aug 1925 and calls its reasoning ('we will, if necessary, sacrifice human lives') one that 'no one is able to explain'. The date is that of the chapter, written on the eve of her departure; the book appeared in 1926. The 'orgies of drunkenness' line is her unsourced gossip, kept as a record of the Western tabloid view and not as fact. Also p. 133: 'During the life of Mustapha Kemal Pasha, yes' (Ankara will stay the capital).",
      urls=["https://archive.org/details/in.ernet.dli.2015.175300"],
      loc="Sheridan, A Turkish Kaleidoscope (1926), pp. 133, 213-220", link="Hat Law",
      nxt="Read the remaining 'Kaleidoscope' chapters (the women's chapter, p. 112 ff.) for further judgements on him"),
 dict(id="dorothy-mills-1926", voice="Lady Dorothy Mills", role="British novelist and travel writer; visited Angora in 1925 (Beyond the Bosphorus, 1926)",
      c="United Kingdom", cn="United Kingdom", dom="letters", date="1926", era="contemporary", mirror=None, pol="conflicted", inten=2,
      saw="Calls him the inspiration and life of new Turkey, 'a God to his followers' with a dictator's power; brilliant, but she doubts his commercial sense.",
      q="Now he is a God to his followers, that is to say to most of the new Turkey, and though his position is nominally but that of President, his power is that of Dictator.",
      art="book", ev="P", med=None, src="mills.txt",
      cav="Lady Dorothy Mills, Beyond the Bosphorus (London: Duckworth, 1926), ch. 'Angora', p. 35 (the quote); p. 34: 'To my great regret I did not have the pleasure of meeting the Ghazi ... The very inspiration and life of new Turkey, he must from all accounts be a man of amazingly powerful personality.' p. 35 goes on: 'Undoubtedly a very brilliant man; but ... he is a trifle over-inclined ... \"to hitch his waggon to a star\"'. She did not meet him, so this is a view from reports and from what she saw in Anatolia; her biographical sketch has errors (e.g. 'Harbin'). p. 36 blames the Turk for 'casting' the Armenians and Greeks 'into the sea', a judgement the vault does not adopt.",
      urls=["https://archive.org/details/in.ernet.dli.2015.279689"],
      loc="Mills, Beyond the Bosphorus (1926), pp. 34-36", link="Mustafa Kemal Atatürk",
      nxt="Her later Turkey pieces (Daily Mail?) unchecked"),
 dict(id="ruth-woodsmall-1936", voice="Ruth Frances Woodsmall", role="American YWCA leader and Near East specialist; author of Moslem Women Enter a New World (1936)",
      c="United States", cn="United States", dom="letters", date="1936", era="contemporary", mirror="emancipator-patriarch", pol="admiring", inten=2,
      saw="Calls him, for the Moslem East as a whole, the leading feminist, whose fearless leadership raised the status of Moslem women.",
      q="For the Moslem East as a whole Kamal Ataturk may be rightly considered the leading feminist.",
      art="book", ev="P", med=None, src="wood.txt",
      cav="Ruth Frances Woodsmall, Moslem Women Enter a New World (1936), p. 69 (index: 'Ataturk, Kamal, 69, 405'); text read in the Bimla reprint, Women in the Changing Islamic System (Delhi), which keeps the original running heads. The next sentence (p. 70): 'Through his fearless leadership he has not only attained his primary objective of social reforms for Turkey, but has also affected the social thought of the entire Moslem world and contributed greatly to the elevation of the status of Moslem women.' Elsewhere (p. 399 of the reprint) she calls him 'the saviour of the new Turkey' whose 'virile and commanding leadership' enabled drastic religious reform. Her observation that the Turkish Women's Union (Kadin Birligi) was dissolved right after the 1935 Istanbul congress is neutral reporting. Woodsmall is a lesser-known name; she is stored for the mid-1930s women's-movement angle, not for fame.",
      urls=["https://archive.org/details/in.ernet.dli.2015.506177"],
      loc="Woodsmall, Moslem Women Enter a New World (1936), pp. 69-70", link="Women's Suffrage in Turkey",
      nxt="Check the 1936 first-edition pagination (reprint p. 399 passage)"),
]

for r in R:
    assert len(r["saw"].split()) <= 25, (r["id"], len(r["saw"].split()))
    assert norm(r["q"]).rstrip(".") in bank(r["src"]), r["id"]
    print("quote verified:", r["id"])
    # supporting quotes named in the caveats
extra = {"naked.txt": ["the one man who from overwhelming defeat and humiliation had led the Turks to victory",
                       "had captured this adamantine Trotzki, so well worth capturing!"],
         "kaleid.txt": ["they owe to their Ghazi the fact of their existence to-day as a nation",
                        "Terror reigns, and the Tribunal of Independence is as arbitrary as the Cheka"],
         "mills.txt": ["The very inspiration and life of new Turkey, he must from all accounts be a man of amazingly powerful personality"],
         "wood.txt": ["Through his fearless leadership he has not only attained his primary objective of social reforms for Turkey"]}
for f, qs in extra.items():
    b = bank(f)
    for q in qs:
        assert norm(q) in b, (f, q)
print("supporting quotes verified")

with open(os.path.join(STATE, "gazes_exiles.jsonl"), "w", encoding="utf-8") as f:
    for r in R:
        rec = {"id": r["id"], "voice": r["voice"], "voice_type": "person", "role": r["role"], "country": r["c"],
               "country_now": r["cn"], "domain": r["dom"], "date": r["date"], "era": r["era"], "mirror": r["mirror"],
               "polarity": r["pol"], "intensity": r["inten"], "what_they_saw": r["saw"], "quote": r["q"],
               "artifact": r["art"], "evidence": r["ev"], "mediated_by": r["med"], "caveat": r["cav"],
               "node": NODE, "sources": r["urls"]}
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")

with open(os.path.join(STATE, "ledger_exiles.md"), "w", encoding="utf-8") as f:
    f.write("| Claim | Node | Status | Sources | Next step |\n|---|---|---|---|---|\n")
    for r in R:
        qs = r["q"]
        f.write("| %s (%s, %s): \"%s\" | %s | verified %s (%s) | %s | %s |\n" % (
            r["voice"], r["role"][:50], r["date"], qs[:110].replace("|", "/") + ("..." if len(qs) > 110 else ""),
            NODE, r["ev"], r["loc"], "; ".join(r["urls"][:1]), r["nxt"] or "none"))

new_people = {
 "Lady Dorothy Mills": ("British novelist and travel writer", "British", "", "conflicted",
    "She visited Angora in 1925 without meeting the Ghazi and wrote of him as 'a God to his followers' with a dictator's power."),
 "Ruth Frances Woodsmall": ("American YWCA leader and writer on Muslim women", "American", "", "admirer (women's rights)",
    "In 1936 she called him 'the leading feminist' of the Moslem East."),
}
for name, (role, nat, life, stance, desc) in new_people.items():
    if os.path.exists(os.path.join(HERE, "vault", "People", name + ".md")):
        continue
    person(name, role=role, nat=nat, life=life, stance=stance, tags=["verified", "observer", "women"],
           body="%s See [[%s]] for the quotes and sources.\n\n## Sources\n- See [[%s]].\n" % (desc, NODE, NODE))

body = ["""
Round 17 went after the European exiles, artists and scholars who worked in Atatürk's Turkey, and after famous Western women who wrote about
him. The exiles were a dry end: none of the famous names left a statement about him in a text we could open. The women yielded
four records from open scans found by the archive.org full-text search, led by [[Clare Sheridan]], whose two books give both
a face-to-face portrait (Smyrna, 1922) and a hostile-leaning 1925 chapter.

## The pattern

- **Sheridan the portraitist, then the sceptic:** in 1922 [[Clare Sheridan]] saw 'the one man' who led the Turks from defeat to victory and a
  face she could not read; by 1925 (A Turkish Kaleidoscope) she wrote of terror, an arbitrary tribunal and the hat speech as an order nobody could
  explain. Compare [[Grace Ellison]], who stayed admiring.
- **A view from hearsay:** [[Lady Dorothy Mills]] never met him but sums him up in a paragraph: 'a God to his followers', a dictator in fact, brilliant but impractical about trade.
- **The feminist label:** [[Ruth Frances Woodsmall]] (1936) is the earliest clean statement in the census that he was the Moslem East's 'leading feminist'. See [[Women's Suffrage in Turkey]].
"""]
for r in R:
    body.append("\n## %s (%s)\n" % (r["voice"], r["date"]))
    body.append("*%s*\n" % r["saw"])
    body.append("> %s\n" % r["q"])
    body.append("%s Location: %s. Evidence %s. See [[%s]].\n" % (r["cav"], r["loc"], r["ev"], r["link"]))

body.append("""
## Not stored, and dry ends (round 17)

- **Eleanor Roosevelt, My Day (1935-62):** the GWU search page is behind a Cloudflare challenge; the Keenable/DuckDuckGo seam finds only columns that mention Turkey, not him. My Day of 29 March 1937 (md054603) praises Julian Bryan's films of the 'mechanized nation' but names no one; the 4 Feb 1954 column (Bayar's visit) and 28 Nov 1958 (Saygun's oratorio) do not name him either. No stated view found. The vault note's 'she noted by the mid-1930s Turkey had women judges...' remains unsourced.
- **Albert Einstein:** the 1933 letter is to İnönü; no Atatürk line (already in the vault note). No new genuine statement found.
- **Bruno Taut:** letter to Mihara of 8 Aug 1938 (Akademie der Künste, We Refugees Archive) says nothing of Atatürk; Akcan's article and a METU dissertation on the catafalque are secondary and quote no remark by Taut about him. His Turkish diary is not online.
- **Béla Bartók:** the DergiPark paper on Bartók and Saygun (article-file 1208069) and other items have no statement by Bartók about Atatürk; the trip was at Atatürk's request, per a Turkish source.
- **Paul Hindemith:** the Idil article on his three reports (1935-37) mentions Atatürk only as background; Hindemith's letter of 13 Feb 1935 to his publisher gives no view.
- **Ernst Reuter, Auerbach, Spitzer, Rüstow, Röpke, Neumark, Holzmeister:** only secondary statements that they served Atatürk's reforms. Röpke's Turkish articles 'on the role of Atatürk' (Masala and Kama, Springer 2018, ch. 2) and a footnote that Röpke would endorse Atatürk's 'I am a dictator in order to prevent potential dictatorship' are leads, not records; paywalled. Neumark's *Zuflucht am Bosporus* (1980) and Hirsch's memoir (Anılarım) are lending-only with no snippet hit. Edzard Reuter's quotation on women's rights (dunyadaataturk.com) is the son's, post-war, and unreferenced.
- **Ella Maillart, The Cruel Way (1947):** only Kemal Atatürk mentioned by a Black Sea wireless operator ('Kemal Ataturk died eight months ago, and we need fifteen more leaders like him'), pp. 38-39: not her view. No Annemarie Schwarzenbach hit.
- **Rose Macaulay:** The Towers of Trebizond (1956) is fiction; the narrator's remarks on Atatürk are a character's. Vita Sackville-West, Passenger to Teheran (1926): no Kemal hit in the full text search.
- **Freya Stark, Seferis, Andrić, Le Corbusier, Josephine Baker, Chaplin, Fairbanks:** no usable hit.

## Sources
- Clare Sheridan, Naked Truth (1928); A Turkish Kaleidoscope (1926). Lady Dorothy Mills, Beyond the Bosphorus (1926). Ruth Frances Woodsmall, Moslem Women Enter a New World (1936). All read in archive.org open scans, identifiers in each record.
- GWU Eleanor Roosevelt Papers, My Day (md054603 and others); We Refugees Archive (Taut to Mihara, 8 Aug 1938).
""")
note("Events", NODE, {"type": "event", "when": "1922–1936", "tags": ["event", "verified", "women", "observers"]}, "\n".join(body))
print("ok", len(R), "records")
