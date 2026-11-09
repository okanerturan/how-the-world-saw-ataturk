# -*- coding: utf-8 -*-
# Census round 27 (4 Nov 2026) — deeper NDL pass: Shimomura Kainan, Otani Kozui, Takabatake Motoyuki, Kokuryukai. Page images read.
import json, os
from _lib import note
HERE = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(HERE, "tools", ".state", "round27")
os.makedirs(STATE, exist_ok=True)
NDL = "https://dl.ndl.go.jp/pid/"
JN = "More Japanese Voices on Kemal, 1928–1935 — NDL Digital Collections"
def rec(id, voice, vt, role, dom, date, mirror, pol, inten, saw, quote, art, cav, src):
    return {"id": id, "voice": voice, "voice_type": vt, "role": role, "country": "Japan", "country_now": "Japan",
            "domain": dom, "date": date, "era": "contemporary", "mirror": mirror, "polarity": pol, "intensity": inten,
            "what_they_saw": saw, "quote": quote, "artifact": art, "evidence": "P", "mediated_by": None,
            "caveat": cav, "node": JN, "sources": src}
R = [
 rec("shimomura-kainan-1935", "Shimomura Kainan", "person", "Asahi Shimbun executive, later minister and NHK president", "press", "1935", None, "admiring", 2,
     "Kemal is 'certainly great', but Japanese admirers only cheer his stage performance and do not know the toil behind the script reform.",
     "いふまでもなくたしかに彼等はエライ、しかしそれは思ひ切つてズバ〳〵やつてのける、舞臺の上の武者振りだけ見て遠くからヤンヤ〳〵といふに止まつてる。",
     "book",
     "Honkegaeri (Shijō Shobō, 1935), essay 'Mussolini ya Kemal Pasha', printed pp. 502-503 (NDL image 271, read on the page image). 'They' = Mussolini, Hitler, Kemal. The facing page praises Kemal's resolve in replacing the Arabic script (not quoted). Also p. 447/NDL image 243 wishes for 'a Mussolini, a Hitler, a Kemal Pasha' for Japan. Essay date not shown; book year used. Translation of gist is the vault's.",
     [NDL+"1273386"]),
 rec("otani-kozui-1929", "Ōtani Kōzui", "person", "Buddhist leader, 22nd abbot of Nishi Hongan-ji, explorer and publicist", "religion", "1929", "nation-forge-template", "admiring", 1,
     "Lists President Kemal Pasha with Piłsudski and Primo de Rivera as leaders whose dictatorships restored national strength; Japan needs the same.",
     "トルコのケマルパシヤ大統領の如き、スペインのプリモ・ド・リヴエラ宰相の如き、皆獨裁政治によりてその國勢を回復せり。",
     "book",
     "Teikoku no zento (Daijōsha Tokyo branch, 1929), printed p. 12 (NDL image 14, read on the page image). Passing but explicit judgment inside an argument that Japan needs party-free deliberation. Not an endorsement of dictatorship as such, per the author.",
     [NDL+"1465913"]),
 rec("takabatake-motoyuki-1928", "Takabatake Motoyuki", "person", "Translator of Das Kapital, turned state-socialist ideologue", "letters", "1928", None, "conflicted", 1,
     "Kemal, Reza Khan, Gandhi and Zaghlul are famed champions against white domination, but 'in the end small' beside Mussolini.",
     "ケマルパシヤやリザ、カーンや、さてはガンジーやザクルールやは、白人專制に對抗する傑士として有名であるが、規局は小であり",
     "book",
     "Mussolini to sono shisō (Jitsugyō no Sekai-sha, 1928), printed p. 116 (NDL image 71, read on the page image). The OCR 'regyoku' is the page's furigana reading of 結局 (garbled); the quote keeps the page's printed form as read. Polarity rated conflicted: respect for the anti-white stance, belittling in rank.",
     [NDL+"1444148"]),
 rec("kokuryukai-1931", "Kokuryūkai (Black Dragon Society)", "institution", "Japanese pan-Asianist society, publisher of Saishin Ajia taikan", "politics", "1931", "anti-colonial-liberator", "admiring", 2,
     "Calls Kemal 'Turkey's hero' who, when Greece invaded, raised volunteers in Anatolia and founded the Ankara assembly.",
     "土耳古の英傑ケマル·パシヤは、小亞細亞の要地までも奪はれては遂に國家を滅亡に陷らしむる外なきを憂ひ、奮然蹶起して自ら義勇軍を組織し",
     "book",
     "Saishin Ajia taikan (Kokuryūkai Shuppanbu, 1931), printed p. 347 (NDL image 195, read on the page image); 'Kemal Pasha's rising' is the margin head. The book is a Kokuryūkai-edited compendium, so the voice is the society's editorial one, not a named author. Same book, pp. 196-203, relays his reforms (OCR).",
     [NDL+"1903286"]),
]
body = f"""A deeper pass over the National Diet Library's Digital Collections (NDL Lab full-text API, then the page images) adds four voices left as leads in round 26. Japanese quotes are verbatim from the page images; glosses are the vault's.

## Shimomura Kainan, 1935
The Asahi executive and later minister writes that people everywhere talk of the greatness of Mussolini, Hitler and Kemal Pasha: 'needless to say they are indeed great, but people only cheer from afar at the stage performance'. On the facing page he praises the resolve with which Kemal moved the capital to Ankara and replaced the Arabic script, which Japanese, he says, hardly know (*Honkegaeri*, 1935, pp. 502-503; pid 1273386).

*Census check (5 Nov 2026): the three entries below (Ōtani, Takabatake, the Kokuryūkai) are kept as context but not counted as gazes — Kemal appears in lists of exemplars or as an editorial epithet, not as the author's stated view.*

## Ōtani Kōzui, 1929
The Nishi Hongan-ji abbot lists President Kemal Pasha with Piłsudski and Primo de Rivera as leaders who restored national strength by strong rule (*Teikoku no zento*, 1929, p. 12; pid 1465913).

## Takabatake Motoyuki, 1928
In his Mussolini book he names Kemal Pasha, Reza Khan, Gandhi and Zaghlul as famous champions against 'white despotism', yet 'in the end small' beside Mussolini (p. 116; pid 1444148). His 1930 *Eiyū sūhai to kanban shinri* (pid 1268554, p. 28) only lists Kemal among the idol-heroes of nations and is not counted.

## Kokuryūkai, 1931
The Black Dragon Society's compendium *Saishin Ajia taikan* calls him 'Turkey's hero Kemal Pasha' who rose and raised volunteers against the Greek invasion (p. 347; pid 1903286).

## Not counted
Shinmura Izuru 1941 (*Kokugo mondai seigi*, pid 1126363, p. 43) says the outcome of Kemal's script change is hard to judge and hearsay reports of failure exist; that is a view on the reform, not on the man.

## Sources
- https://dl.ndl.go.jp/pid/1273386 (Shimomura)
- https://dl.ndl.go.jp/pid/1465913 (Ōtani)
- https://dl.ndl.go.jp/pid/1444148 and https://dl.ndl.go.jp/pid/1268554 (Takabatake)
- https://dl.ndl.go.jp/pid/1903286 (Kokuryūkai)
- https://dl.ndl.go.jp/pid/1126363 (Shinmura)
"""
note("Events", JN, {"type": "event", "when": "1928-1935", "tags": ["event", "verified", "japan", "ndl"]}, body)
with open(os.path.join(STATE, "gazes_milliyet.jsonl"), "w", encoding="utf-8") as f:
    for r in R: f.write(json.dumps(r, ensure_ascii=False) + "\n")
print(len(R), "records")
