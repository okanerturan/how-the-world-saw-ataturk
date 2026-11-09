# -*- coding: utf-8 -*-
# Census round 13 (Nov 2026) — Islamic thinkers and leaders on Atatürk in their own words.
# Records: Khomeini (Sahifeh-ye Imam vol. 3 p. 309, via the Imam Khomeini portal), Sayyid Qutb (In the Shade of the
# Qur'an, English trans.), Said Nursi (Afyon prison letter, Şualar 455), Erbakan (1980s remark via Hanioğlu).
# Source texts banked in tools/.state/round13/islamists/; every quote is checked against its bank first.
import json, os, re, sys
from _lib import note

HERE = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(HERE, "tools", ".state", "round13")
BANK = os.path.join(STATE, "islamists")
NODE = "Islamic Thinkers on Atatürk in Their Own Words"

def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"').replace("­", "")
    s = re.sub(r"-\s*\n", "", s)
    return re.sub(r"\s+", " ", s)

def bank(n):
    t = open(os.path.join(BANK, n), encoding="utf-8").read()
    if n.endswith(".json"):
        t = " ".join(r["text"] for r in json.loads(t)["results"])
    return norm(t)

R = [
 dict(id="khomeini-1978", voice="Ruhollah Khomeini", role="Shia marja', later founder of the Islamic Republic of Iran", c="Iran (exile)", cn="Iran",
      dom="religion", date="1978", era="posthumous", mirror="apostate", pol="hostile", inten=1,
      saw="Calls Reza Khan's unveiling policy a shameful imitation of 'the ungodly Ataturk', which brought shame on humanity.",
      q="By imposing ban on Islamic veil for women, Reza Khan’s shameful imitation of the ungodly Ataturk, caused and brought about shame for humanity.",
      art="speech", ev="S", med="English text as quoted by the Imam Khomeini Portal (en.imam-khomeini.ir, n29326) ← Sahifeh-ye Imam vol. 3, p. 309 (Institute for Compilation and Publication of Imam Khomeini's Works); Persian original not read",
      cav="Translation; the portal gives volume and page but not the speech or its date. Vol. 3 of the English Sahifeh series falls between the 1965 end of vol. 1 and the Jan–Apr 1979 vol. 6, so '1978' is an approximation; the vol. 3 PDF could not be fetched to confirm. The object is Reza Shah's policy; Atatürk is named as its model. The same portal page prints a further excerpt from Kashf al-Asrar (p. 189) that does not name Atatürk. Kashf al-Asrar (1943) itself was not read for this round.",
      src=["a1.json"], urls=["http://en.imam-khomeini.ir/en/n29326/Reza-Khan-acted-against-cultural-values-religious-sentiments"],
      loc="Sahifeh-ye Imam vol. 3, p. 309, via en.imam-khomeini.ir/en/n29326", link="Ruhollah Khomeini"),
 dict(id="sayyid-qutb-zilal-1960", voice="Sayyid Qutb", role="Muslim Brotherhood ideologue; Qur'an commentator", c="Egypt", cn="Egypt",
      dom="religion", date="1960", era="posthumous", mirror="apostate", pol="hostile", inten=2,
      saw="Describes Atatürk's movement as uncompromising in its enmity to everything Islamic and as the removal of the last unifying Muslim institution, the Caliphate.",
      q="The clearest example of these was in the case of Ataturk and his movement in Turkey which was uncompromising in its enmity to everything Islamic.",
      art="book", ev="S", med="English translation of Fi Zilal al-Qur'an (In the Shade of the Qur'an, Islamic Foundation trans.) as scanned on archive.org (Volume1Surah12); Arabic original not read",
      cav="Translation. Commentary on Surah 9 (al-Tawbah), section 'Relations with Other Religions', scan p. 118 (further remark on p. 120 about Wilfred Cantwell Smith's reading of Atatürk). Zilal was written 1952–65 and the surah volumes are undated, so '1960' is an approximate midpoint. Two other passages name him: Surah 6 (al-An'am) commentary, scan p. 118, 'Kemal Ataturk, the hero of Turkey', and p. 289, 'the false hero they created'. In these passages Qutb ascribes the secularising project to Jewish, Christian and Zionist forces; that is his attribution and is not endorsed here. Milestones (archive.org MILESTONES_201903, milestones-syed-qutb) was searched and does not name Atatürk. Page numbers come from the scan's printed page footers.",
      src=["zilal_full.txt"], urls=["https://archive.org/details/Volume1Surah12"],
      loc="In the Shade of the Qur'an, Surah 9 commentary, scan p. 118 (also Surah 6, pp. 118, 289)", link="Sayyid Qutb"),
 dict(id="said-nursi-1948", voice="Said Nursi", role="Islamic scholar, founder of the Nur movement", c="Turkey", cn="Turkey",
      dom="religion", date="1948-10", era="posthumous", mirror=None, pol="conflicted", inten=1,
      saw="In an Afyon prison letter, cites Mustafa Kemal's twice-sent cipher requests that he come to Ankara as proof of his own wartime service.",
      q="We have to have this heroic hoja here!",
      art="quote", ev="S", med="Şükran Vahide's biography text hosted by iikv.org (page 330) quoting Nursi's letter to the Afyon governor ← Şualar p. 455 (Eng. tr. Rays, p. 533); the sentence is Nursi's report of Mustafa Kemal's words",
      cav="Nursi's own letter, but the quoted sentence is what he says Mustafa Kemal told him, so it shows how Nursi chose to present the relationship, not an independent record. Date inferred: Vahide places the letter on a 29 October Republic Day while Nursi was in Afyon Prison (1948–49), which leaves only 29 Oct 1948. Movement-sourced hosting; edition attribution of the hosted text unconfirmed. Distinct from the existing 1923 record (the Ankara confrontation). Nursi's 'abominable current of atheism' passage (Lem'alar p. 170, Flashes p. 233) does not name Atatürk and is not stored.",
      src=["nursi_330.txt"], urls=["https://iikv.org/en/kulliyat/bediuzzaman-said-nursi/330", "https://iikv.org/en/kulliyat/bediuzzaman-said-nursi/329"],
      loc="Vahide text p. 330 ← Şualar p. 455 (Rays p. 533)", link="Said Nursi"),
 dict(id="necmettin-erbakan-1980s", voice="Necmettin Erbakan", role="Leader of the Milli Görüş (National Vision) movement; later Prime Minister", c="Turkey", cn="Turkey",
      dom="politics", date="1980", era="posthumous", mirror="internal-mirror", pol="instrumental", inten=1,
      saw="Claims Atatürk, were he alive, would have joined the National Vision movement, recasting Kemalism in Islamist terms.",
      q="Had he lived today, Atatürk would have become a member of the Islamic Vision (Millî Görüş).",
      art="quote", ev="S", med="Hanioğlu, Atatürk: An Intellectual Biography (Princeton UP 2011), Introduction, n. 1 (English rendering; footnote not read) ← Erbakan, 'in the 1980s'",
      cav="Translation by Hanioğlu; the Turkish wording, speech and exact year were not traced (the footnote and Erbakan's original could not be fetched; dokumen.pub is bot-blocked). Date '1980' is a decade placeholder. Hanioğlu treats the remark as an Islamist adoption of 'an unconventional Kemalism', so polarity 'instrumental' follows his reading. Erbakan has no vault person note.",
      src=["src_erbakan_snippet.txt"], urls=["https://degruyterbrill.com/document/doi/10.1515/9781400885572-002/html"],
      loc="Hanioğlu 2011, Introduction, n. 1", link=None),
]

bad = []
for r in R:
    full = " ".join(bank(s) for s in r["src"])
    if norm(r["q"]) not in full:
        bad.append(r["id"])
if bad:
    sys.exit("quote not found in source bank: %s" % bad)
for r in R:
    assert len(r["saw"].split()) <= 25, (r["id"], len(r["saw"].split()))

with open(os.path.join(STATE, "gazes_islamists.jsonl"), "w", encoding="utf-8") as f:
    for r in R:
        rec = {"id": r["id"], "voice": r["voice"], "voice_type": "person", "role": r["role"], "country": r["c"],
               "country_now": r["cn"], "domain": r["dom"], "date": r["date"], "era": r["era"], "mirror": r["mirror"],
               "polarity": r["pol"], "intensity": r["inten"], "what_they_saw": r["saw"], "quote": r["q"],
               "artifact": r["art"], "evidence": r["ev"], "mediated_by": r["med"], "caveat": r["cav"],
               "node": NODE, "sources": r["urls"]}
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")

NXT = {"khomeini-1978": "Fetch Sahifeh vol. 3 (date and Persian original of p. 309); read Kashf al-Asrar (1943) in Persian for Reza Shah-era passages",
       "sayyid-qutb-zilal-1960": "Arabic Fi Zilal commentary on Surah 9 (al-Tawbah) to confirm wording and edition date; Qutb's own Arabic for the Surah 6 passages",
       "said-nursi-1948": "Şualar p. 455 in Turkish; Afyon prison chronology to confirm 29 Oct 1948",
       "necmettin-erbakan-1980s": "Hanioğlu n. 1 (Turkish source and date); Erbakan speeches on Atatürk in TBMM or Milli Görüş publications"}
with open(os.path.join(STATE, "ledger_islamists.md"), "w", encoding="utf-8") as f:
    f.write("| Claim | Node | Status | Sources | Next step |\n|---|---|---|---|---|\n")
    for r in R:
        f.write("| %s (%s, %s): \"%s\" | %s | verified %s (%s) | %s | %s |\n" % (
            r["voice"], r["role"], r["date"], r["q"][:110].replace("|", "/") + ("..." if len(r["q"]) > 110 else ""),
            NODE, r["ev"], r["loc"], "; ".join(r["urls"][:1]), NXT[r["id"]]))

body = ["""
Round 13 looked for the best-known Islamic thinkers and leaders speaking about Atatürk in their own words. Four records
survived reading; the neutral task here is to record what each says and where, not to adopt any of it. Quotes were
checked against the fetched source text before this note was written, and all but Nursi's are English translations.

## The pattern

- **Reform as a foreign import:** [[Ruhollah Khomeini]] names Atatürk only as the model Reza Khan copied when banning the
  veil ([[Reza Shah Pahlavi]]); the target of the sentence is the Shah's policy.
- **The Caliphate as the wound:** [[Sayyid Qutb]], in his Qur'an commentary, treats Atatürk's movement as openly hostile to
  Islam and as the removal of the last unifying institution ([[Abolition of the Caliphate]]).
- **A contested personal relationship:** [[Said Nursi]], late in life, cites Mustafa Kemal's wish to have him in Ankara.
- **A Turkish counter-move:** Necmettin Erbakan's 1980s remark that Atatürk would have joined the National Vision movement
  is read by Hanioğlu as an Islamist adoption of Kemalism, not a judgement of the man.
""".strip()]

for r in R:
    body.append("\n## %s, %s (%s)\n" % (r["voice"], r["role"], r["date"]))
    body.append("*%s*\n" % r["saw"])
    body.append("> %s\n" % r["q"])
    body.append("%s Location: %s. Evidence %s (%s).%s\n" % (r["cav"], r["loc"], r["ev"], r["med"], (" See [[%s]]." % r["link"]) if r["link"] else ""))

body.append("""
## Other Qutb passages (same work, same stance)

The Surah 6 commentary calls the Turkish experiment one 'carried out by the false hero they created' and says Qutb's
Western and Zionist adversaries later 'tried not to repeat the mistake they made with Kemal Ataturk'; the Surah 5
commentary names 'the nationalist hero, Ataturk' in a passage on the abolition of Islamic rule. These are Qutb's
attributions of the secularising project to outside forces and are recorded as his, not as findings.

## Dry ends (round 13)

- **Abul A'la Mawdudi:** Nasr (*The Vanguard of the Islamic Revolution*, UC Press, n. on Mawdudi) says his Khilafat
  involvement made him suspicious of Kemal and that he saw Kemalism as godless secularism; that is Nasr's paraphrase.
  The open English texts on archive.org (*The Question of Dress* 1929, *Towards Understanding Islam*, *Come Let Us Change
  This World*, *Al-Jihad fi'l-Islam*, *Insights into Islamic Thought*) contain no Kemal or Atatürk. *The Question of Dress*
  lists Turkey among countries where 'Eastern nationalists' impose foreign dress, without naming Atatürk. Nothing stored.
- **Hassan al-Banna:** nothing beyond the existing memoir record was searched this round; see [[Hassan al-Banna]].
- **Ali Shariati, Rashid Rida, Shakib Arslan:** not searched (Rida and Arslan already have 1924–28 records; Shariati was out of budget).
- **Qutb, *Milestones*:** read in two archive.org scans; the words Kemal, Atatürk do not appear.

## Sources
- Imam Khomeini Portal, 'Reza Khan acted against cultural values, religious sentiments', en.imam-khomeini.ir/en/n29326, citing *Sahifeh-ye Imam* vol. 3, p. 309.
- Sayyid Qutb, *In the Shade of the Qur'an* (English trans., Islamic Foundation), archive.org/details/Volume1Surah12.
- Şükran Vahide, text hosted at iikv.org/en/kulliyat/bediuzzaman-said-nursi/330 (Nursi, *Şualar* p. 455).
- M. Şükrü Hanioğlu, *Atatürk: An Intellectual Biography* (Princeton UP 2011), Introduction, via degruyterbrill.com/document/doi/10.1515/9781400885572-002/html.
""")

note("Events", NODE,
     {"type": "event", "when": "1943–1980s",
      "tags": ["event", "verified", "islamist", "religion"]},
     "\n".join(body))
print("ok", len(R), "records")
