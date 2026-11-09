# -*- coding: utf-8 -*-
# Census round 33 (6 Nov 2026): verification of the original unsourced transcript (raw.txt).
# Appends a "Census check" block to People notes whose transcript-derived claims were refuted or are
# unsupported. Runs after the people builders (b0-b4) in the rebuild loop; the block is re-added on
# every build. See LEDGER § "Round 33: raw.txt cross-check".
import os
HERE = os.path.dirname(os.path.abspath(__file__))
PEOPLE = os.path.join(HERE, "vault", "People")
MARK = "## Census check (raw.txt verification, Nov 2026)"

CHECKS = {
 "W.B. Yeats": "Refuted: *A Vision* (1925 and 1937 texts) never names Kemal or Turkey, and *On the Boiler* (1939) has no reference to him. The 'Nietzschean figure' reading above has no source in Yeats.",
 "H.G. Wells": "Unsupported: no Wells text treats Turkey as a vanguard state; Kemal appears only in a list of dictators in *The Shape of Things to Come* (1933).",
 "B.R. Ambedkar": "Corrected: the claim that he repeatedly pointed to Turkey in the Hindu Code Bill debates is wrong (the Turkey mentions in *Writings and Speeches* vol. 14 are other members'). His documented statement is the Nov 1935 interview: 'I feel the greatest respect for Kemal Pasha' (vol. 17/1, pp. 237–238) — see the census record.",
 "Lord Kinross": "Corrected: *Atatürk* was published in 1964 (US edition 1965). 'Commissioned by the British government' is unsourced.",
 "Vladimir Mayakovsky": "Unsupported: his poems on Wikisource never name Kemal (\"Пятый Интернационал\", 1922, praises Angora, not Kemal), and no visit to Turkey was found.",
 "Joseph Grew": "Unsupported: the dinners till dawn and the 'terrifyingly intelligent' line are not in the searchable text of *Turbulent Era* (1952). His documented impression is in the census record.",
 "Percy Loraine": "Partly confirmed: the friendship is in his own words ('Ataturk regarded me as a personal friend'); the poker games and his weeping at the funeral are unsourced. His own verdicts (June and Nov 1938 despatches) are in the census records.",
 "Nicolae Titulescu": "Unsupported: the 'greatest statesman in Europe' line and a 1938 eulogy were not found. Only the October 1933 two-hour meeting is documented (British annual report for 1933).",
 "Henry Ford": "Unsupported: no 'admiring correspondence' between Ford and Kemal was found.",
 "Agatha Christie": "Unsupported: the Pera Palace Room 411 story has no source, and none of her searchable works mentions Kemal.",
 "Józef Piłsudski": "Unsupported: the 'empty chair' legend could not be traced to any source; treat it as apocrypha (reception history, not history).",
 "Clemens Holzmeister": "Corrected: he worked in Ankara from 1927, so 'fleeing the rising fascist tide' does not fit his first Turkish period (he returned in 1938 after the Anschluss).",
 "Antoun Saadeh": "Nuanced: the Hatay-as-betrayal framing is confirmed, but the target of the 1942 al-Zawba'a text is Jamil Mardam's National Bloc rather than Kemal's ideology.",
 "Agop Dilaçar": "Refuted/unsupported: his own TV interview never says he proposed the surname 'Atatürk'; a 2019 article reports the reverse — Atatürk proposed 'Dilaçar' to him.",
 "Sabiha Gökçen": "Nuanced: by her own (ghost-written) memoir she asked to take part in the Dersim operation and Kemal agreed subject to Marshal Çakmak's consent; 'he deployed her' overstates.",
 "Fidel Castro": "Wordings resolved (round 34): the documented words are from his audience for Health Minister Aktuna's delegation, Havana, 13 Mar 1997, in Mehmet Domaç's notes taken in the room ('Atatürk büyük insan, büyük asker, İngilizleri nasıl yendi?'; 'Asker ve fikir adamı Atatürk önemli insan olarak tarihe geçti') and in Aktuna's press account ('Bu kadar büyük bir devrim yaptım ama Atatürk'ün yaptıklarını başaramadım'). See the census record. 'A star that fell on your country' and 'governed even after his death' appear only in posts from 2020–2023; his 1996 Habitat speech in Istanbul does not mention Atatürk.",
 "Vecihi Hürkuş": "Unsupported: an arrest is not documented; sources say only that he was punished in 1925 and later barred from the profession.",
}

n = 0
for name, text in CHECKS.items():
    p = os.path.join(PEOPLE, name + ".md")
    if not os.path.exists(p):
        print("missing note:", name); continue
    s = open(p, encoding="utf-8").read()
    if MARK in s:
        s = s[:s.index(MARK)].rstrip() + "\n"
    s = s.rstrip() + "\n\n" + MARK + "\n⚠️ " + text + "\n"
    open(p, "w", encoding="utf-8").write(s)
    n += 1
print(n, "people notes flagged")
