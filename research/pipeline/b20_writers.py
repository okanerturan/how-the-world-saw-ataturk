# -*- coding: utf-8 -*-
# Census round 12 (Nov 2026) — famous writers and thinkers in their own words: Muhammad Iqbal (two texts) and Ernest Hemingway
# (Toronto Daily Star, Oct 1922). Open texts only: archive.org djvu OCR of Iqbal's two books, Wikisource corroboration of the 1936
# statement, and public reprints of the Star dispatches. Writes two Events notes and tools/.state/round12/gazes_writers.jsonl.
import json, os
from _lib import note

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tools", ".state", "round12", "gazes_writers.jsonl")
os.makedirs(os.path.dirname(OUT), exist_ok=True)

N1 = "Iqbal on Turkey and Atatürk, 1930–1936"
N2 = "Hemingway Reads Kemal, Toronto Star October 1922"

RECON = "https://archive.org/stream/dli.ministry.19661/E01934_The_Reconstruction_of_Religious_Thought_In_Islam_djvu.txt"
SPEECH = "https://archive.org/stream/in.ernet.dli.2015.51949/2015.51949.Speeches-And-Statements-Of-Iqbal_djvu.txt"
WS = "https://en.wikisource.org/wiki/Islam_and_Ahmadism"
H9 = "https://thegrandarchive.wordpress.com/hamid-bey-wears-shirt-tucked-in-when-seen-by-star"
H19 = "https://bookreadfree.com/140492/3471837"
HJ = "https://doi.org/10.1353/tsl.2012.0029"

R = []
def rec(**k):
    base = dict(voice_type="person", era="contemporary", evidence="S", mediated_by=None)
    base.update(k)
    R.append(base)

rec(id="iqbal-1930", voice="Muhammad Iqbal", role="Poet-philosopher of Indian Islam", country="British India", country_now="Pakistan/India",
    domain="letters", date="1930", mirror=None, polarity="admiring", intensity=2,
    what_they_saw="Calls Turkey's ijtihad on the caliphate perfectly sound and Turkey the one Muslim nation roused from dogmatic slumber; Atatürk is not named.",
    quote="Personally, I believe the Turkish view is perfectly sound.", artifact="book", node=N1, sources=[RECON],
    caveat="Lecture VI, 'The Principle of Movement in the Structure of Islam' (lectures given 1928–29; Lahore 1930, Oxford 1934). Mustafa Kemal is never named: the object is 'Turkey' and 'the Turk'. Page numbers (c. 149–150 caliphate; 154 'dogmatic slumber') derived from running heads in the 1934 scan dli.ministry.19661, not from a printed-page check.")
rec(id="iqbal-1936", voice="Muhammad Iqbal", role="Poet-philosopher of Indian Islam", country="British India", country_now="Pakistan/India",
    domain="letters", date="1936", mirror=None, polarity="conflicted", intensity=3,
    what_they_saw="Defends Atatürk against Nehru's charge that Turkey left Islam: abolishing the caliphate expressed Islam's spirit; the Swiss code and Turkish Quran were errors.",
    quote="In the abolition of the Caliphate which since the days of Omayyads had practically become a kind of Empire it is only the spirit of Islam that has worked out through the Ataturk.",
    artifact="article", node=N1, sources=[SPEECH, WS],
    caveat="'Islam and Ahmadism' (Reply to Questions Raised by Pandit J. L. Nehru), 1936; month not confirmed. Speeches and Statements of Iqbal, ed. Shamloo (Lahore 1944), pp. 134–137, 141 (page numbers from running heads of the scan). Wording of the quoted sentence also found on Wikisource. Also: 'The adoption of the Swiss code with its rule of inheritance is certainly a serious error' and that he regards Quran recitation in Turkish 'as a serious error of judgment'.")
rec(id="hemingway-1922", voice="Ernest Hemingway", role="Toronto Daily Star correspondent (aged 23)", country="Canada", country_now="Canada",
    voice_type="person", domain="press", date="1922-10-09", mirror=None, polarity="witness", intensity=1,
    what_they_saw="Sardonic reporting: Kemal bans alcohol in Anatolia while he and his staff drink; he is 'hand in glove with the Soviets'.",
    quote="This devotion to the laws of the prophet does not prevent Kemal himself and his staff from liking their liquor",
    artifact="article", node=N2, sources=[H9, H19],
    mediated_by="Reprint in Hemingway, Dateline: Toronto (Scribner's 1985), via The Archive of American Journalism",
    caveat="Tone is reportorial irony, not a stated verdict; polarity 'witness' is the nearest enum. The 19 Oct 1922 piece 'Waiting for an Orgy' says 'Kemal is hand in glove with the Soviets and his entry will wipe out the greatest Russian sanctuary.' A scholar (Studies in the Novel/TSL 2012) quotes a 19 Oct dispatch, Dateline p. 296, 'All the East says that Mustapha Kemal is a great man'; that sentence was NOT found in the reprints read, so it is not used.")

with open(OUT, "w", encoding="utf-8") as f:
    for r in R:
        order = ["id","voice","voice_type","role","country","country_now","domain","date","era","mirror","polarity","intensity",
                 "what_they_saw","quote","artifact","evidence","mediated_by","caveat","node","sources"]
        f.write(json.dumps({k: r[k] for k in order}, ensure_ascii=False) + "\n")

body1 = f"""
Muhammad Iqbal, the poet-philosopher who is often called the spiritual father of Pakistan, wrote about Turkey twice at
length in prose, six years apart, and the two texts do not say the same thing. The existing card [[Allama Iqbal]] says the
general was admired and the legislator was not; the texts below show that split in his own words, with one correction:
in the 1936 text it is not the abolition of the caliphate that troubles him.

**1930 (lectures of 1928–29), the admiring register.** In *The Reconstruction of Religious Thought in Islam*, Lecture VI,
Iqbal treats Turkey as the proof that *ijtihad* (independent legal reasoning) is alive. On the caliphate: "Turkey's Ijtihad is
that according to the spirit of Islam the Caliphate or Imamate can be vested in a body of persons, or an elected Assembly."
Then, in the first person: "Personally, I believe the Turkish view is perfectly sound." He adds that "the republican form of
government is not only thoroughly consistent with the spirit of Islam, but has also become a necessity". A few pages later:
"Turkey alone has shaken off its dogmatic slumber, and attained to self-consciousness." **Mustafa Kemal is not named in the
chapter** (a text search of the 1934 scan for Mustafa, Kemal, Ataturk and Angora finds nothing); the gaze is on the Republic
and on "the Turk". The abolition itself ([[Abolition of the Caliphate]], 1924) is therefore endorsed as a Turkish act of
ijtihad, with the caution that the Assembly, not a single caliph, now holds the office.

**1936, the conflicted register.** Jawaharlal Nehru ([[Jawaharlal Nehru]]) had written in the *Modern Review* that Turkey
had ceased to be a Muslim country. Iqbal's reply, "Islam and Ahmadism", answers by naming Atatürk. He sets him in a line of
"men who came after" the reformers: "Zaghlul Pasha, Mustafa Kamal and Raza Shah", who "relying on their healthy instincts,
had the courage to rush into sun-lit space and do, even by force, what the new conditions of life demanded". Then he goes
through the "innovations" one at a time:

- materialist outlook: useful "against mulla-cult and Sufi-craft";
- dress and the Latin script ([[Alphabet Reform]]): Islam "has no specific language, no specific dress";
- Quran recitation in Turkish: "a serious error of judgment", since Arabic is "the only non-European language which has a future";
- excluding the licensed clergy: the Ataturk "has done what would have delighted the heart of an Ibn Taimiyya or a Shah Wali Ullah";
- the Swiss code with its inheritance rule ([[Turkish Civil Code]]): "certainly a serious error ... excusable in a people furiously desiring to go ahead";
- the caliphate: "it is only the spirit of Islam that has worked out through the Ataturk";
- Pan-Turanianism: "I do not think that the Ataturk is inspired by Pan-Turanianism".

The verdict is mixed but sympathetic, and Iqbal's own condition is stated: Islam's test is loyalty to the unity of God and the
finality of the Prophet, not national dress. The tone toward Atatürk is that of a defence counsel who still marks his client's
errors.

**Not yet found.** Iqbal's Persian and Urdu verse on Turkey (e.g. in *Bal-i-Jibril*, *Zarb-i-Kalim*, *Javid Nama*): no open
text with a translation naming Mustafa Kemal was located in this round.

## Sources
- Iqbal, *The Reconstruction of Religious Thought in Islam* (Oxford 1934 ed.), Lecture VI, archive.org scan dli.ministry.19661: {RECON} (S)
- Iqbal, "Islam and Ahmadism" / "Reply to Questions Raised by Pandit J. L. Nehru" (1936), in *Speeches and Statements of Iqbal*, ed. Shamloo (Lahore 1944), pp. 134–141: {SPEECH} (S, OCR of a scan)
- Wikisource, "Islam and Ahmadism" (corroborates the quoted sentences): {WS} (S)
"""
note("Events", N1, {"type": "event", "when": "1930–1936", "tags": ["event", "verified", "letters", "iqbal", "conflicted"]}, body1)

body2 = f"""
[[Ernest Hemingway]] reached Constantinople on 30 September 1922, at the height of the [[Chanak Crisis]], and wrote some
twenty dispatches for the *Toronto Daily Star* in the weeks the Greeks evacuated Thrace and the Kemalist army stood outside the
city. The existing card has him reporting Atatürk with "stark awe"; the dispatches read differently. What they show is a
young reporter's sardonic, sceptical Kemal, seen mostly at second hand.

- **9 October 1922**, "Hamid Bey Wears Shirt Tucked In When Seen by Star": after an interview with Hamid Bey, "next to Kemal,
  perhaps the most powerful man in the Angora government", Hemingway notes that Kemal has banned alcohol, cards and
  backgammon in Anatolia: "This devotion to the laws of the prophet does not prevent Kemal himself and his staff from liking
  their liquor."
- **19 October 1922**, "Waiting for an Orgy": the fear is of the "cutthroats, robbers, bandits, thugs and Levantine pirates"
  gathered in the city, waiting for "the triumphal entry of Mustapha Kemal Pasha's troops"; and a Russian-refugee paragraph that
  ends: "Kemal is hand in glove with the Soviets and his entry will wipe out the greatest Russian sanctuary." A Greek
  interlocutor calls him "that bandit Kemal" (the Greek's words, not Hemingway's).

Verdict: no stated judgment of the man, only an ironic eye. Polarity is recorded as witness, intensity 1.

**Unverified lead.** A 2012 article in the journal *TSL* (doi 10.1353/tsl.2012.0029) quotes Hemingway from *Dateline: Toronto*,
p. 296: "All the East says that Mustapha Kemal is a great man", and, on 23 October (pp. 299–300), a passage that has the Earl of
Balfour denounce Kemal as a bandit "for sale to the highest bidder". Neither sentence was found in the reprints read here, so
they are not used. A direct read of *Dateline: Toronto* pp. 293–300 (Internet Archive item `datelinetorontoc00hemi`, lending
only) would settle it; the 24 October piece "Turks Beginning to Show Distrust of Kemal Pasha" is the likeliest place for a
stated view and was not retrieved.

## Sources
- Hemingway, "Hamid Bey Wears Shirt Tucked In When Seen by Star", *Toronto Daily Star*, 9 Oct 1922, reprinted from *Dateline: Toronto* (Scribner's 1985): {H9} (S)
- Hemingway, "Waiting for an Orgy", *Toronto Daily Star*, 19 Oct 1922: {H19} (S, public reprint)
- "Dirty, White Candles: Ernest Hemingway's Encounter with the East", *TSL* (2012): {HJ} (J, for the unverified lead only)
"""
note("Events", N2, {"type": "event", "when": "1922-10", "tags": ["event", "verified", "press", "hemingway", "greco-turkish-war"]}, body2)
print("ok", len(R), "records")
