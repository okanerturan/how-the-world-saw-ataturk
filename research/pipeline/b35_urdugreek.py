# -*- coding: utf-8 -*-
# Census round 26 (4 Nov 2026) — Zafar Ali Khan's Kemal elegy, read on the page image of the 1995 Diwan scan.
import json, os
from _lib import note

HERE = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(HERE, "tools", ".state", "round26")
os.makedirs(STATE, exist_ok=True)
NODE = "Zafar Ali Khan — Ataturk Mustafa Kemal Nur Allah Marqadahu, Delhi 12 November 1938"
SRC = "https://archive.org/details/20220402_20220402_2028"
BOOK = ("Diwan-e Zafar Ali Khan, ed. Tanvir Ahmad (Ali Hujwiri Publishers, Lahore, 1995 ed.), p. 210 "
        "(PDF page 210 of the archive.org scan; OCR unusable, page read on the image)")
NODE2 = "Zafar Ali Khan — Angora, a poem in Baharistan (1937)"
SRC2 = "https://archive.org/details/dli.ernet.449733"
Q2 = "مصطفیٰ قائم نہ کرتا گر نظامِ انگورہ کا / کام کرزن نے کیا ہی تھا تمامِ انگورہ کا"
Q = "دنیا سے وہ مجاہدِ اعظم گزر گیا ... صاحب دلو یہ غم ہے غمِ مصطفیٰ کمال"
R = [
 {"id": "zafar-ali-khan-1938-11-poem", "voice": "Zafar Ali Khan", "voice_type": "person",
  "role": "Urdu poet and editor of Zamindar", "country": "British India", "country_now": "India",
  "domain": "letters", "date": "1938-11-12", "era": "funeral", "mirror": "anti-colonial-liberator",
  "polarity": "admiring", "intensity": 2,
  "what_they_saw": "An elegy mourning the 'supreme mujahid' who eased the community's troubles, restored the Turks' honour against the crusaders and stood from Kabul to Ankara for Islam.",
  "quote": Q, "artifact": "poem", "evidence": "P", "mediated_by": None,
  "caveat": "Quote is two half-lines, translation: 'That supreme mujahid has passed from the world ... O men of heart, this grief is the grief of Mustafa Kemal.' Poem titled 'Ataturk Mustafa Kemal, nawwara llahu marqadahu', dated Delhi, 12 Nov 1938. Source: " + BOOK + ", read on the image (4 Nov 2026). Distinct from his 14 Nov Assembly speech. A companion poem 'Congressi ulama' (p. 211, Delhi 13 Nov 1938) ends by asking God to send another Mustafa Kemal; not recorded separately.",
  "node": NODE, "sources": [SRC]},
 {"id": "zafar-ali-khan-1923-angora", "voice": "Zafar Ali Khan", "voice_type": "person",
  "role": "Urdu poet and editor of Zamindar", "country": "British India", "country_now": "India",
  "domain": "letters", "date": "1923", "era": "contemporary", "mirror": "anti-colonial-liberator",
  "polarity": "admiring", "intensity": 2,
  "what_they_saw": "Poem 'Angora': had Mustafa not founded the Angora order, Curzon would have finished Angora; its fame spreads from Kabul to Cairo and Damascus.",
  "quote": Q2, "artifact": "poem", "evidence": "P", "mediated_by": None,
  "caveat": "Translation of the quote: 'Had Mustafa not established the order of Angora / Curzon had already finished off Angora.' Poem 'Angora', printed p. 273 (contents list p. 274; PDF page 295) of Baharistan, Parts 1-2 (Gujrat, 1937, 'forty years of verse'), read on the page image (4 Nov 2026). The poem is undated in the book; the 1923 date is inferred from the reference to Curzon (Lausanne talks, foreign secretary to Jan 1924) and Amanullah Khan, and may be a year or two off. Not a 1919-22 Khilafat-era text.",
  "node": NODE2, "sources": [SRC2]},
]
body = f"""Zafar Ali Khan, editor of *Zamindar*, wrote a funeral-week elegy dated Delhi, 12 November 1938, two days before he read verses on Kemal in the Central Legislative Assembly (see [[Zafar Ali Khan]]).

## What the poem says
Opens "What do you ask of the community of the best of mankind: look, you will find everyone prostrate with grief"; the grief has reached Arabs and non-Arabs alike. Kemal is the "supreme mujahid" (*mujahid-e a'zam*) whose like cannot be found by searching; his resolve eased the community's troubles; he restored the honour of the Turks against the "cross-worshippers" and the "crown of the age" is made to serve; from Kabul to Ankara, from Iran to Egypt, Islam's beauty shone again. Ends with a prayer that the Kaaba's Lord not let the work decay.

Verbatim (Urdu, p. 210): {Q}
Translation (marked): "That supreme mujahid has passed from the world ... O men of heart, this grief is the grief of Mustafa Kemal."

The facing poem on p. 211, "Congressi ulama" (Delhi, 13 Nov 1938), closes by asking God to "send another Mustafa Kemal" against the Congress-aligned clerics.

## Sources
- {SRC} ({BOOK})
"""
note("Events", NODE, {"type": "event", "when": "1938-11-12", "tags": ["event", "verified", "poem", "india"]}, body)
body2 = f"""Poem 'Angora' in *Baharistan* parts 1-2 (Gujrat, 1937), printed p. 273, read on the page image; by [[Zafar Ali Khan]]. Twelve couplets, each hemistich ending 'Angora ka' (of Angora). Kemal is named in the opening line as the founder of the 'order of Angora'; the poet credits it with undoing Curzon's work, humbling Europe's pride, and says Afghanistan's Amanullah Khan is also intoxicated with it and foresees Kabul, Hind, Iraq, Egypt and Syria following its example.

Verbatim (Urdu): {Q2}
Translation (marked): "Had Mustafa not established the order of Angora / Curzon had already finished off Angora."

Dating: undated in the book; probably 1922-24 (Curzon and Amanullah references), inferred, not read.

## Sources
- {SRC2} (Baharistan, Parts 1-2, Gujrat 1937; PDF page 295)
"""
note("Events", NODE2, {"type": "event", "when": "1923", "tags": ["event", "verified", "poem", "india"]}, body2)
with open(os.path.join(STATE, "gazes_urdugreek.jsonl"), "w", encoding="utf-8") as f:
    for r in R: f.write(json.dumps(r, ensure_ascii=False) + "\n")
print(len(R), "records")
