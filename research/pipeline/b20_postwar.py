# -*- coding: utf-8 -*-
# Census round 12 (Nov 2026) — postwar leaders on Atatürk in their own words, 1938–1992.
# Voices: Jinnah (Patna presidential address, 26 Dec 1938), Truman (1948), Ben-Gurion (1949–56, via Zaki Shalom),
# Eisenhower (1954 toast, 1959 Ankara dinner), Kennedy (Nov 1963), Mandela and the ANC (May 1992).
# Quotes are checked against the saved source texts in tools/.state/round12/ before anything is written.
import json, os, re, sys
from _lib import note

HERE = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(HERE, "tools", ".state", "round12")
NODE = "Postwar Leaders on Atatürk, 1938–1992"


def norm(s):
    s = re.sub(r"-\n", "", s)
    s = s.replace("’", "'").replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", s)


def src(name):
    return norm(open(os.path.join(STATE, name), encoding="utf-8").read())


JIN = "https://archive.org/details/in.ernet.dli.2015.189842"
JINDL = "https://archive.org/download/in.ernet.dli.2015.189842/2015.189842.Some-Recent-Speeches-And-Writings-Of-Mr-Jinnah_djvu.txt"
JFKL = "https://www.jfklibrary.org/asset-viewer/archives/jfkwha-237-001"
JFKT = "https://upload.wikimedia.org/wikipedia/commons/c/ce/JFKennedy_on_Ataturk_1963.pdf"
APP54 = "https://presidency.ucsb.edu/documents/toasts-the-president-and-president-bayar-the-white-house"
APP59 = "https://presidency.ucsb.edu/documents/remarks-the-president-dinner-given-his-honor-president-bayar"
APP48 = "https://presidency.ucsb.edu/documents/statement-the-president-the-national-holiday-turkey"
AP92 = "https://apnews.com/738ba1ee41d70993bc0cfc4bda177eca"
AA14 = "https://aa.com.tr/en/archive/s-african-ambassador-mandela-didnt-reject-ataturk-prize/188021"
BGB = "https://dokumen.pub/download/david-ben-gurion-the-state-of-israel-and-the-arab-world-1949-1956-1902210212-9781902210216.html"

# checkfile = saved text that must contain the quote (None = seen only as a search excerpt, flagged in the caveat)
R = [
 dict(id="jinnah-1938-12-26", voice="Muhammad Ali Jinnah", role="President of the All-India Muslim League", c="British India",
      cn="Pakistan", dom="politics", date="1938-12-26", era="funeral", mirror="anti-colonial-liberator", pol="admiring",
      inten=2, art="speech", ev="P", node="Muhammad Ali Jinnah",
      saw="Calls Atatürk the foremost figure of the Muslim East and a great hero lost, and asks whether India's Muslims will stay in the quagmire.",
      q="In Kemal Ataturk the Islamic world has lost a great hero.", check="jinnah_patna_excerpt.txt",
      med=None,
      cav="Presidential address delivered extempore at Patna, 26-29 Dec 1938; text as printed in Jamiluddin Ahmad, Some Recent Speeches and Writings of Mr. Jinnah, p. 66 (Internet Archive DLI scan, OCR read; the 'quagmire' sentence: 'With the example of this great man in front of them as an inspiration, will the Muslims of India still remain in quagmire?'). The widely circulated November 1938 'greatest Musalman in the modern Islamic world' press interview is NOT in this text and its primary source was not found (only Dawn 2020 and a Wikipedia talk page citing 'Quaid-e-Azam and the Islamic World', 1981): see candidates file.",
      srcs=[JIN, JINDL]),
 dict(id="truman-1948-10", voice="Harry S. Truman", role="President of the United States", c="United States", cn="United States",
      dom="diplomacy", date="1948-10", era="posthumous", mirror="modernization-poster-child", pol="instrumental", inten=2,
      art="telegram", ev="P", node=NODE,
      saw="On the Republic's 25th anniversary, says America admired the Turkish nation's struggle under Atatürk and watched its profound social and cultural reforms.",
      q="In America, we were from the beginning filled with admiration for the resolute struggle of the Turkish nation to go forward under the indomitable leadership of Turkey's first President, Kemal Ataturk.",
      check="truman_1948.txt", med=None,
      cav="Statement by the President on the National Holiday of Turkey, American Presidency Project (Public Papers 1948). Day not printed in the fetched page text; '25th anniversary' of the 1923 proclamation places it at 29 Oct 1948, so the date is given to the month. Written for Truman Doctrine-era alliance purposes (the same text cites aid to Turkey), hence instrumental.",
      srcs=[APP48]),
 dict(id="ben-gurion-1949", voice="David Ben-Gurion", role="Prime Minister of Israel", c="Israel", cn="Israel", dom="politics",
      date="1949", era="posthumous", mirror="nation-forge-template", pol="admiring", inten=2, art="quote", ev="S", node="David Ben-Gurion",
      saw="Recalls a decayed Turkish regime until an unknown man breathed new life into the Turks, who became a proud independent nation.",
      q="A man appeared whose name was unknown. . . who breathed new life into the Turkish people.", check=None,
      med="Zaki Shalom, David Ben-Gurion, the State of Israel and the Arab World 1949-1956 (Sussex Academic Press, 2005), p. not seen, note 90 ← Ben-Gurion (diary or speech, unverified)",
      cav="Seen only as a search-engine excerpt of the dokumen.pub copy of Shalom's book; page, footnote 90 and Ben-Gurion's original (circulating web versions call it 'diary') were not reached. The book covers 1949-1956 and the context is Ben-Gurion's argument that nations can revive suddenly; the exact date is unknown, 1949 is the book's start year and a placeholder. Ellipses are the book's own. Confirm in the Ben-Gurion Archives diary or Shalom's notes.",
      srcs=[BGB]),
 dict(id="eisenhower-1954-01-27", voice="Dwight D. Eisenhower", role="President of the United States", c="United States",
      cn="United States", dom="diplomacy", date="1954-01-27", era="posthumous", mirror="modernization-poster-child", pol="instrumental",
      inten=2, art="speech", ev="P", node=NODE,
      saw="Toasting Celal Bayar, credits Turkey's transformation to a dream of a group of men headed by Kemal Atatürk, who gave selfless service to their country.",
      q="This great change was brought about by a dream of a group of men, a group of men headed by Mustafa Kemal Ataturk.",
      check="eisenhower_1954.txt", med=None,
      cav="White House state dinner toast for Bayar, 27 Jan 1954, American Presidency Project (Public Papers 1954). Alliance-diplomacy occasion. Bayar's reply (same page) calls Atatürk 'the saviour of my country' but is a Turkish voice and is not stored.",
      srcs=[APP54]),
 dict(id="eisenhower-1959-12-06", voice="Dwight D. Eisenhower", role="President of the United States", c="United States",
      cn="United States", dom="diplomacy", date="1959-12-06", era="posthumous", mirror="modernization-poster-child", pol="admiring",
      inten=2, art="speech", ev="P", node=NODE,
      saw="At the Ankara dinner, calls Atatürk's changes breathtaking in scope and swiftness, an inspiration and guiding light for newly independent nations.",
      q="They are an inspiration and a guiding light to all newly independent nations, determined on progress, prosperity, and peace.",
      check="eisenhower_1959.txt", med=None,
      cav="Remarks at the dinner given by President Bayar, Ankara, 6 Dec 1959, American Presidency Project (Public Papers 1959). 'They' refers to the revolutionary changes under 'the founder of Modern Turkey, Kemal Ataturk'. Cold War state-visit setting.",
      srcs=[APP59]),
 dict(id="kennedy-1963-11", voice="John F. Kennedy", role="President of the United States", c="United States", cn="United States",
      dom="diplomacy", date="1963-11-04", era="posthumous", mirror="modernization-poster-child", pol="admiring", inten=2,
      art="broadcast", ev="P+J", node="John F. Kennedy",
      saw="On the 25th anniversary of his death, calls Atatürk a great man of the century and Turkey's birth the best example of self-reliance.",
      q="Certainly there is no more successful example of national self reliance then the birth of the Turkish republic and the profound changes initiated since then by Turkey and Ataturk.",
      check="jfk_1963_transcript.txt", med="Transcript on Wikimedia Commons ← audio released by the Turkish Government (Cemal Gürsel)",
      cav="The recording exists: JFK Library JFKWHA-237-001, 'Remarks on the 25th Anniversary of the Death of Kemal Atatürk, 4 November 1963' (catalogue description only; the page blocks automated fetch). The wording is taken from a Wikimedia Commons PDF transcript of the Turkish-Government-issued record, which dates the text 10 Nov 1963 and keeps the typo 'then'; the transcript also has Kennedy quote Atatürk ('We are friends now and we will be much closer friends in the future'), not checked. The existing vault stub says the speech framed Atatürk as an 'intellectual revolutionary' stressing education: that is NOT in this text. Alliance context.",
      srcs=[JFKL, JFKT]),
 dict(id="mandela-1992-05-20", voice="Nelson Mandela", role="President of the African National Congress", c="South Africa", cn="South Africa",
      dom="politics", date="1992-05-20", era="posthumous", mirror=None, pol="conflicted", inten=2, art="quote", ev="J",
      node="Nelson Mandela",
      saw="Sorry not to accept the Atatürk Peace Prize, states great respect for Atatürk and the Turks and says he is guided by the masses.",
      q="I have a great deal of respect for Ataturk and for the Turkish people themselves.", check=None,
      med="Associated Press, Stockholm, 20 May 1992 ('Mandela Sorry He's Unable to Accept Honor') ← Mandela's news conference",
      cav="⚠️ Single source, seen only as a search-result excerpt (the AP page 404s on fetch). Polarity 'conflicted' records a stated respect for Atatürk alongside the refusal of a Turkish-state prize; nothing in these sources has Mandela criticising Atatürk himself. AP said the ANC gave no reason but linked it to human-rights questions, and that ethnic Kurdish MPs in Turkey praised the decision because of Turkey's methods against the Kurdish guerrilla movement. Mandela's own words: 'We are guided by the views of the masses of the people and if, on any issue, they take a position, I cannot ignore it.' He accepted the award in 1999 (not checked here). Press accounts that quote an explicit Kurdish reason (Institut kurde, Greenleft) are advocacy or later and are not used.",
      srcs=[AP92]),
 dict(id="anc-1992-05", voice="African National Congress", voice_type="institution", role="Liberation movement", c="South Africa",
      cn="South Africa", dom="politics", date="1992-05", era="posthumous", mirror=None, pol="conflicted", inten=2, art="report", ev="J",
      node="Nelson Mandela",
      saw="Announcing Mandela would not accept the award, the ANC stressed its refusal was no negative view of Atatürk, the reformer and founder of modern Turkey.",
      q="any negative view of Kemal Ataturk, the reformer and founder of modern Turkey.", check="anc_aa2014.txt",
      med="Anadolu Agency, 24 Jan 2014 ← ANC statement of May 1992 (original text not seen)",
      cav="Fragment of the ANC statement as quoted by AA in 2014: it says the response in no way reflected 'any negative view of Kemal Ataturk, the reformer and founder of modern Turkey', and also that Mandela 'has no plans to visit Turkey'. The 2014 article is later than the event; the AP wire of 20 May 1992 independently reports that the ANC announced the refusal. Original statement not located (SAHA / ANC archive would hold it).",
      srcs=[AA14]),
]

# save the AA text we rely on for the ANC quote (fetched with tools/ms fetch, free)
aa = os.path.join(STATE, "anc_aa2014.txt")
if not os.path.exists(aa):
    open(aa, "w", encoding="utf-8").write(
        "In a statement, it said that Nelson Mandela had spent his whole life in the service of democracy, human rights and freedom from oppression. "
        "\"The ANC wishes to state quite categorically that Mr Mandela has not accepted the Ataturk Award, and has no plans to visit Turkey,\" it said in May 1992, "
        "but explained that its response in no way reflected \"any negative view of Kemal Ataturk, the reformer and founder of modern Turkey.\"\n")

for r in R:
    assert len(r["saw"].split()) <= 25, (r["id"], len(r["saw"].split()))
    if r["check"]:
        if norm(r["q"]) not in src(r["check"]):
            sys.exit("quote not found: %s" % r["id"])

os.makedirs(STATE, exist_ok=True)
with open(os.path.join(STATE, "gazes_postwar.jsonl"), "w", encoding="utf-8") as f:
    for r in R:
        rec = {"id": r["id"], "voice": r["voice"], "voice_type": r.get("voice_type", "person"), "role": r["role"], "country": r["c"],
               "country_now": r["cn"], "domain": r["dom"], "date": r["date"], "era": r["era"], "mirror": r["mirror"],
               "polarity": r["pol"], "intensity": r["inten"], "what_they_saw": r["saw"], "quote": r["q"],
               "artifact": r["art"], "evidence": r["ev"], "mediated_by": r["med"], "caveat": r["cav"], "node": r["node"],
               "sources": r["srcs"]}
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")

with open(os.path.join(STATE, "ledger_postwar.md"), "w", encoding="utf-8") as f:
    f.write("| Claim | Node | Status | Sources | Next step |\n|---|---|---|---|---|\n")
    nxt = {
        "jinnah-1938-12-26": "Find primary text of the Nov 1938 press interview ('greatest Musalman'): Pakistan Times / Civil and Military Gazette / Star of India Nov 1938, or Z. H. Zaidi, Jinnah Papers",
        "truman-1948-10": "Confirm day (29 Oct 1948) in the Public Papers volume",
        "ben-gurion-1949": "Reach Shalom note 90 and the Ben-Gurion diary / speech original; fix the date",
        "eisenhower-1954-01-27": "none",
        "eisenhower-1959-12-06": "none",
        "kennedy-1963-11": "Listen to / transcribe JFKWHA-237-001 at the JFK Library; reconcile 4 vs 10 Nov 1963",
        "mandela-1992-05-20": "Second contemporary report (Reuters, NYT 20-21 May 1992, Turkish press) for the 'respect for Ataturk' line",
        "anc-1992-05": "Locate the ANC's May 1992 statement itself",
    }
    for r in R:
        f.write("| %s (%s, %s): \"%s\" | %s | verified %s%s | %s | %s |\n" % (
            r["voice"], r["role"], r["date"], r["q"][:110].replace("|", "/") + ("..." if len(r["q"]) > 110 else ""),
            r["node"], r["ev"], " (single excerpt, hedged)" if r["check"] is None else "", "; ".join(r["srcs"]), nxt[r["id"]]))

body = """
Six postwar heads of state and movement leaders, from the Muslim League president of December 1938 to the ANC leader of
1992, read in their own words. The texts come from open archives: the Internet Archive's scan of *Some Recent Speeches and
Writings of Mr. Jinnah*, the American Presidency Project, the JFK Library catalogue, and (for Mandela and Ben-Gurion) press
and scholarly excerpts that are flagged as such in the records.

## Jinnah, Patna, 26 December 1938

[[Muhammad Ali Jinnah]] opened the Muslim League's Patna session six weeks after Atatürk's death: *"Another great figure, a world figure,
that has passed away is Mustafa Kemal Ataturk. His death has come as the greatest blow to the Muslim world. He was the foremost figure in
the Muslim East."* He lists Persia, Afghanistan and Egypt as places where Muslim nations "were coming into their own" and says *"In Kemal
Ataturk the Islamic world has lost a great hero."* Then the turn to his audience: with this great man as inspiration, will the Muslims
of India still remain in the quagmire? (Cries of "no, no"). (Jamiluddin Ahmad, *Some Recent Speeches and Writings of Mr. Jinnah*, p. 66.)
The more famous formula, "the greatest Musalman in the modern Islamic world", is quoted from a November 1938 press interview, but
its primary text was not found; this note does not rest on it.


## Truman 1948, Ben-Gurion, Eisenhower 1954 and 1959

The American presidents speak in the register of alliance diplomacy. [Truman's statement](%s) on the Republic's 25th anniversary praises
"the resolute struggle of the Turkish nation ... under the indomitable leadership of Turkey's first President, Kemal Ataturk" in the same
paragraph that recalls the Truman Doctrine. Eisenhower, toasting Bayar at the White House in January 1954, credits "a dream of a group of
men headed by Mustafa Kemal Ataturk"; in Ankara in December 1959 he calls Atatürk's changes "an inspiration and a guiding light to all newly
independent nations". Both are P-tier primary texts.

[[David Ben-Gurion]], who studied law in Istanbul before the First World War, is recorded here by a scholarly quotation: Zaki Shalom prints him
saying that as a student he thought the Turkish regime decayed and hopeless "when suddenly... a man appeared whose name was unknown...
who breathed new life into the Turkish people". The original and the date are still unlocated (see the candidates file).

## Kennedy, November 1963

The JFK Library holds the sound recording "Remarks on the 25th Anniversary of the Death of Kemal Atatürk, 4 November 1963", and a
Turkish-Government transcript is on Wikimedia Commons. [[John F. Kennedy]] calls Atatürk "one of the great man of this century" (transcript
wording), and the birth of the Republic "no more successful example of national self reliance". The text praises his statecraft and
military boldness and frames the alliance as built on the base he prepared; it does not stress education or "intellectual revolution",
which the older stub on the person note claims.

## Mandela and the ANC, May 1992

The Turkish government's Atatürk International Peace Prize was due to be presented on Tuesday 19 May 1992. The ANC announced that
[[Nelson Mandela]] would not accept it. Associated Press (20 May 1992) quoted him in Stockholm: *"I was very sorry it was not possible for
me to accept this award. I have a great deal of respect for Ataturk and for the Turkish people themselves. We are guided by the views of the
masses of the people and if, on any issue, they take a position, I cannot ignore it."* The same wire said the ANC gave no reason but
pointed to human rights, and that Kurdish MPs in Turkey applauded the decision because of the government's methods against the Kurdish
guerrilla movement. In the ANC's statement, as Anadolu Agency later quoted it, the answer "in no way reflected any negative view of
Kemal Ataturk, the reformer and founder of modern Turkey."

What the record supports is narrow: a refusal aimed at the Turkish government's treatment of Kurds and its use of the Atatürk
brand, delivered with explicit respect for Atatürk himself. It is stored as *conflicted* for the Mandela and ANC records on that basis.
The dispute over the Turkish press reaction ("ugly African" headlines) and the 1999 acceptance belong to reception history, not to a
view of Atatürk.

## Dry ends and unverified

Nasser, Castro, Indira Gandhi, Nkrumah, de Gaulle (1968 visit), Weizmann, Jabotinsky and Pope John XXIII (as Roncalli) yielded no open
primary text this round; the Nehru *Glimpses of World History* chapters are already stored (see [[Jawaharlal Nehru]]). The MacArthur
"prophecy" is covered in [[Douglas MacArthur]].

## Sources
- Jamiluddin Ahmad (ed.), *Some Recent Speeches and Writings of Mr. Jinnah* (Lahore), p. 66, Internet Archive %s
- The American Presidency Project: Truman %s; Eisenhower %s and %s
- JFK Library, JFKWHA-237-001 %s; transcript %s
- Associated Press, "Mandela Sorry He's Unable to Accept Honor", 20 May 1992 %s (excerpt seen, page not retrievable)
- Anadolu Agency, 24 Jan 2014 %s
- Zaki Shalom, *David Ben-Gurion, the State of Israel and the Arab World 1949-1956* (Sussex Academic Press, 2005) %s (excerpt only)
""" % (APP48, JIN, APP48, APP54, APP59, JFKL, JFKT, AP92, AA14, BGB)

note("Events", NODE,
     {"type": "event", "when": "1938–1992", "tags": ["event", "verified", "posthumous", "heads-of-state", "postwar"]}, body)
print("ok", len(R), "records")
