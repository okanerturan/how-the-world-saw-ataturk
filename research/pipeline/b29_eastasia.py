# -*- coding: utf-8 -*-
# Census round 20 (Nov 2026) — East Asia: two further Chinese pens on Kemal from zh.wikisource (Deng Zhongxia 1923, Chang Naide 1927).
# Pages banked in tools/.state/round20/ (zh_*.txt, first line = page title); the script refuses to run if a quote is not in its bank.
import glob, json, os, sys, urllib.parse
from _lib import note, person

HERE = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(HERE, "tools", ".state", "round20")
NODE = "Kemal in the Chinese Peasant and Federalist Debates, 1923–1927"


def bank(title):
    for f in glob.glob(os.path.join(STATE, "zh_*.txt")):
        t = open(f, encoding="utf-8").read()
        if t.split("\n", 1)[0] == title:
            return t
    sys.exit("no bank for " + title)


def url(t):
    return "https://zh.wikisource.org/wiki/" + urllib.parse.quote(t.replace(" ", "_"), safe="/_:")


R = [
 dict(id="deng-zhongxia-1923-12", voice="Deng Zhongxia", link="Deng Zhongxia", role="Early Chinese Communist and labour-movement leader (writing in Zhongguo Qingnian)",
      c="China", cn="China", dom="politics", date="1923-12-29", mirror="anti-colonial-liberator", pol="instrumental", inten=1,
      art="article", ev="S", page="論農民運動", issue="Zhongguo Qingnian no. 11, signed 中夏, dated 29 Dec 1923 (Wikisource note)",
      saw="Cites Kemal's Turkish revolution as proof that peasants make revolutions: Kemal 'and the others' had much peasant help, the whole country following him.",
      q="土耳其的革命，基玛尔等得农民的帮助不小。",
      tr="In Turkey's revolution, Kemal and the others had no small help from the peasants.",
      cav="From 'On the Peasant Movement' (论农民运动), Wikisource transcription in simplified characters; the page header names the author as 鄧中夏 and the notes field gives the date 1923-12-29 and the original venue (Zhongguo Qingnian no. 11). Later in the piece he asks why, with no serfdom, 'the whole country followed the Nationalist Party leader Kemal' to drive the Greek army across the straits: 'why Turkey too had no serfdom, yet the whole country followed ... Kemal'. Kemal is an argument, not the subject; spelled 基玛尔. Instrumental use in a recruiting argument for the peasant movement.",
      nxt="Print page of Zhongguo Qingnian no. 11; Deng's other 1923-24 pieces for Turkey"),
 dict(id="chang-naide-1927", voice="Chang Naide (常乃惪, Chang Yansheng)", link="Chang Naide", role="Chinese historian and journalist, Youth Party (Xingshi) ideologue",
      c="China", cn="China", dom="politics", date="1927", mirror="internal-mirror", pol="instrumental", inten=1,
      art="article", ev="S", page="聯治救國的步驟", issue="Xingshi Zhoubao (醒獅週報), serial 'Lianzhi jiuguo de buzhou', from Oct 1927 (Wikisource note)",
      saw="Cites General Kemal's one victory over Greece as quick national revival, then argues China's vast size makes that path a dream.",
      q="如同基玛尔将军，一战胜了希腊，便可统一土耳其而复兴旧业",
      tr="as with General Kemal, who by winning one battle against Greece could unify Turkey and restore the old enterprise",
      cav="Wikisource transcription (marked textquality 50%, simplified characters) of a long serial on federal self-government; the header names the author 常乃惪 and the notes cite Wei Xiumei's study identifying him with 常燕生 and the serial's appearance in Xingshi from Oct 1927. The exact issue is not given, so the date is year-only. Kemal is a foil for Chinese warlordism, not admired or criticised in himself: the sentence continues that Chinese conditions are far larger and different.",
      nxt="Identify the Xingshi issue; Chang Naide's other writing on Turkey"),
]
for r in R:
    b = bank(r["page"])
    if r["q"] not in b:
        sys.exit("quote not found in bank: %s" % r["id"])
    assert len(r["saw"].split()) <= 25, r["id"]
    r["u"] = url(r["page"])

with open(os.path.join(STATE, "gazes_eastasia.jsonl"), "w", encoding="utf-8") as f:
    for r in R:
        rec = {"id": r["id"], "voice": r["voice"], "voice_type": "person", "role": r["role"],
               "country": r["c"], "country_now": r["cn"], "domain": r["dom"], "date": r["date"], "era": "contemporary",
               "mirror": r["mirror"], "polarity": r["pol"], "intensity": r["inten"], "what_they_saw": r["saw"],
               "quote": r["q"] + " [translation: " + r["tr"] + "]", "artifact": r["art"], "evidence": r["ev"], "mediated_by": None,
               "caveat": "Cited as %s, Wikisource page '%s'. %s" % (r["issue"], r["page"], r["cav"]),
               "node": NODE, "sources": [r["u"]]}
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")

with open(os.path.join(STATE, "ledger_eastasia.md"), "w", encoding="utf-8") as f:
    f.write("| Claim | Node | Status | Sources | Next step |\n|---|---|---|---|---|\n")
    for r in R:
        f.write("| %s (%s, %s): \"%s\" | %s | verified S (%s, zh.wikisource transcription) | %s | %s |\n" % (
            r["voice"], r["role"], r["date"], r["q"], NODE, r["issue"], r["u"], r["nxt"]))

for r in R:
    person(r["link"], role=r["role"], nat="Chinese", life="", stance="%s (%s)" % (r["pol"], r["date"][:4]),
           tags=["china", "verified", "chinese-primary", "wikisource"],
           body="""%s. %s

> %s
> (translation: %s)

See [[%s]].

## Sources
- %s, '%s': %s
""" % (r["role"], r["saw"], r["q"], r["tr"], NODE, r["issue"], r["page"], r["u"]))

parts = []
for r in R:
    parts.append("""## %s — %s

*%s*

> %s
> (translation: %s)

Wikisource page: %s. See [[%s]].
""" % (r["voice"], r["date"], r["saw"], r["q"], r["tr"], r["page"], r["link"]))
body = """Two further Chinese voices on Kemal, found by phrase search of Chinese Wikisource for the transliterations 基玛尔 / 基瑪爾 / 凱末爾 and read on the page; both use Kemal as an argument in a Chinese debate rather than describing him. The same seam's other hits are already in the vault: see [[Xiangdao Reads Ankara, 1922–1924]], [[Kemal in the Kuomintang's Quarrels, 1924–1928]] and [[Kemal as a Chinese Yardstick, 1933–1940]].

%s
## Sources
%s
""" % ("\n".join(parts), "\n".join("- %s, '%s': %s" % (r["issue"], r["page"], r["u"]) for r in R))
note("Events", NODE, {"type": "event", "when": "1923–1927", "tags": ["event", "verified", "china", "chinese-primary", "wikisource"]}, body)
print("ok", len(R))
