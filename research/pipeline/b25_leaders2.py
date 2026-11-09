# -*- coding: utf-8 -*-
# Census round 16 (Nov 2026) — leaders2: heads of state/party in their own words, Balkans/USSR seams.
# Seam: archive.org full-text search (tools/fts.py) + open djvu text of Hoxha's Selected Works vol. 6, the 1967 Democratic Front
# report, Letra të zgjedhura vol. 2 (1986), and Beneš, Democracy Today and Tomorrow (1939). Brezhnev 1978 from search-inside only.
# Quotes from open scans are checked against the text banked in tools/.state/round16/*.txt.
import json, os, re
from _lib import note, person

HERE = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(HERE, "tools", ".state", "round16")
NODE = "Hoxha, Beneš, Brezhnev and the Soviet Presidium on Atatürk, 1939–1982"

def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"').replace("—", "-").replace("«", '"').replace("»", '"')
    s = re.sub(r"-\s*\n", "", s)
    s = re.sub(r"\s+", " ", s).lower()
    s = re.sub(r"atat\w*", "ataturk", s)
    s = s.replace("udhë- heqës", "udhëheqës").replace("per- sonality", "personality")
    return s

def bank(n):
    return norm(open(os.path.join(STATE, n), encoding="utf-8").read())

R = [
 dict(id="hoxha-1967-09-14", voice="Enver Hoxha", role="First Secretary of the Party of Labour of Albania; report to the 4th Congress of the Democratic Front", c="Albania", cn="Albania",
      dom="politics", date="1967-09-14", era="posthumous", mirror=None, pol="instrumental", inten=1,
      saw="Warns Greece's 'monarchic fascists' that they forget the blows the Turkish people, led by Kemal, dealt at Venizelos's forces in the Asia Minor war.",
      q="They forgot the heavy blows the brave Turkish people, led by Mustafa Kemal Ataturk dealt at Venizelos's hordes",
      art="speech", ev="P", med=None, src="df.txt",
      cav="English text of the 1974 second edition (Tirana, '8 Nentori'); the OCR page marks 120 and 121 bracket the passage (cited as p. 120-121). Hoxha's frame is a warning to Athens in the Cyprus context, so the Kemal reference is instrumental; the note records no view of the Greek-Turkish war itself. The English is the Albanian publisher's own translation.",
      urls=["https://archive.org/details/ReportOnTheRoleAndTasksOfTheDemocraticFrontForTheCompleteTriumphOfSocialismInAlbania"],
      loc="Hoxha, Report on the Role and Tasks of the Democratic Front... (4th Congress, 14 Sept 1967; Tirana 1974), pp. 120-121", link="Mustafa Kemal Atatürk",
      nxt="Albanian original (Vepra, vol. 33-34?) for the exact wording"),
 dict(id="hoxha-1973-04-30", voice="Enver Hoxha", role="First Secretary of the PLA; letter to the Pakistan-Albania Friendship Association (chaired by a Mr Mustafa Kemal Pasha)", c="Albania", cn="Albania",
      dom="politics", date="1973-04-30", era="posthumous", mirror="modernization-poster-child", pol="admiring", inten=2,
      saw="Thanking a friendship society for a bronze bust, calls Atatürk a great statesman and outstanding political personality who led the Turks toward modernization.",
      q="Mustafa Kemal Ataturku ka qenë një udhëheqës i madh shtetëror e personalitet i shquar politik",
      art="telegram", ev="P", med=None, src="hl2.txt",
      cav="Translation (the vault's): 'Mustafa Kemal Atatürk was a great statesman-leader and an outstanding political personality.' Albanian original in Enver Hoxha, Letra të zgjedhura, vol. 2 (Tiranë: 8 Nëntori, 1986), item 'Përshëndetje drejtuar zotit Mustafa Kemal Pasha, kryetar i Shoqatës së Miqësisë Pakistan-Shqipëri', 30 April 1973, pp. 264-266 (OCR page marks 264, 265, and a misread mark for 266). The passage goes on: Atatürk was known for democratic thought and bold work aimed at 'progress and modernization', for his trust in the young generation, and for goodwill toward the Albanian people. A courtesy letter, but a considered one; the bust was a gift from the Association.",
      urls=["https://archive.org/details/vellimi-1"],
      loc="Hoxha, Letra të zgjedhura, vol. 2 (1986), letter of 30 Apr 1973, pp. 265-266", link="Mustafa Kemal Atatürk",
      nxt="Check the first-edition (1985-86) pagination; the archive.org item 'vellimi-1' holds volumes 1-3"),
 dict(id="hoxha-1981-11-01", voice="Enver Hoxha", role="First Secretary of the PLA; report to the 8th Congress of the Party", c="Albania", cn="Albania",
      dom="politics", date="1981-11-01", era="posthumous", mirror="modernization-poster-child", pol="admiring", inten=2,
      saw="Says Albanians hold special admiration for Atatürk, who freed Turkey from the sultans' imperial complex and set it on a course of democracy and progress.",
      q="The Albanian people have special admiration and respect for Mustafa Kemal Ataturk, that outstanding personality and statesman,",
      art="speech", ev="P", med=None, src="sw6.txt",
      cav="Enver Hoxha, Selected Works, vol. VI (Tirana: 8 Nentori, English), 'Report to the 8th Congress of the PLA', 1 Nov 1981, p. 417 (running head 'REPORT TO THE 8TH CONGRESS OF THE PLA 417'). The OCR prints 'Atattirk'. Continues: he 'liberated Turkey and its valiant people', 'consolidated the unity and genuine independence of the Turkish nation'; Hoxha adds that Atatürk was well disposed to Albania and opposed King Zog, and that Turkey sheltered hundreds of Albanian exiles. Same passage in Spanish, Portuguese, Italian and German editions (fts). The Zog remark is Hoxha's; the vault records no independent confirmation.",
      urls=["https://archive.org/details/20241204_20241204_2331"],
      loc="Hoxha, Selected Works, vol. 6, Report to the 8th Congress of the PLA (1 Nov 1981), p. 417", link="King Zog I",
      nxt="Albanian original (Raport mbi veprimtarinë e KQ, Tiranë 1981)"),
 dict(id="hoxha-1982-11-10", voice="Enver Hoxha", role="First Secretary of the PLA; address to the electors of Tirana", c="Albania", cn="Albania",
      dom="politics", date="1982-11-10", era="posthumous", mirror="secular-rationalist-prophet", pol="admiring", inten=2,
      saw="Honours Atatürk as an outstanding democrat who destroyed the Ottoman Empire and Caliphate, and tells 'pseudo-democrats' to follow him in cutting the Gordian knot.",
      q="We honour and respect the great leader of the Turkish people, Mustafa Kemal Ataturk, who, as an outstanding democrat, destroyed the Ottoman Empire and the Caliphate and set up the new democratic Turkey.",
      art="speech", ev="P", med=None, src="sw6.txt",
      cav="Selected Works, vol. VI, 'Address to the electors', dated 10 Nov 1982 (delivered in electoral zone no. 210, Tirana), p. 618 (running head '618 ENVER HOXHA'; the OCR prints 'Atatirk'). The next sentence: 'Let all the pseudo-democrats and pseudo-socialists who oppress the peoples ... follow the example of Kemal Ataturk who cut the Gordian knot of the Ottoman Empire with his sword.' Part of a tour of Albania's neighbours; the praise is also a barb at Hoxha's contemporaries. The attribution of the page to the 1982 address rests on the continuous run of the speech from p. 598 to p. 620+.",
      urls=["https://archive.org/details/20241204_20241204_2331"],
      loc="Hoxha, Selected Works, vol. 6, Address to the electors (10 Nov 1982), p. 618", link="Mustafa Kemal Atatürk",
      nxt="Albanian original (Vepra, vol. 'Fjalime dhe artikuj 1982')"),
 dict(id="benes-1939", voice="Edvard Beneš", role="Former President of Czechoslovakia; Chicago lectures, Democracy Today and Tomorrow", c="Czechoslovakia (in exile)", cn="Czech Republic",
      dom="politics", date="1939", era="posthumous", mirror=None, pol="conflicted", inten=1,
      saw="Counts Atatürk's dictatorship among the interwar post-war dictatorships, but credits his victory over Greece and 'courageous modernisation' with the authority that kept him in power.",
      q="It must, besides, be remembered that from 1923 the dictatorship of Kemal Ataturk was established in full force in Turkey: his victory over Greece and his courageous modernisation of the whole social, cultural, and national life of Turkey endowed him with sufficient authority to preserve his dictatorship successfully up to his death in 1938.",
      art="book", ev="P", med=None, src="benes.txt",
      cav="Edvard Beneš, Democracy Today and Tomorrow (New York: Macmillan, 1939), p. 90, chapter 'Downfall of postwar democracies'; the lectures were given at the University of Chicago, 1939. Open scan democracytodayto00bene (Univ. of Florida copy); the index lists 'Attaturk, Kemal, 90'. A descriptive aside inside an argument about the rise of Fascism, so both labels (dictatorship, courageous modernisation) are Beneš's.",
      urls=["https://archive.org/details/democracytodayto00bene"],
      loc="Beneš, Democracy Today and Tomorrow (1939), p. 90", link="Mustafa Kemal Atatürk",
      nxt="Masaryk: no Kemal hit in fts; Czech originals (Beneš, Světová válka) unchecked"),
 dict(id="podgorny-1965-01", voice="Nikolai Podgorny", role="Presidium member leading the Supreme Soviet delegation to Turkey; speech in Ankara", c="Soviet Union", cn="Russia",
      dom="diplomacy", date="1965-01", era="posthumous", mirror=None, pol="instrumental", inten=1,
      saw="Invokes the Lenin-and-Atatürk era of Soviet-Turkish friendship as the model for renewing relations, and says Moscow sees no obstacle.",
      q=None, art="speech", ev="S", med="Özer and Güngör 2026, ODÜ SOBİAD 16(2), art. 9, from Soviet sources (Izvestiya 1965)",
      src=None,
      cav="Second-hand: a 2026 article on Soviet sources reports that during the 4-13 January 1965 visit Podgorny 'emphasized the importance of returning to the spirit of friendship and cooperation shaped during the eras of Lenin and Atatürk'. A second paper (Yeşilbursa, Vakanüvis 11(1), 2026, p. 893 on a Soviet call of Nov 1963, the 25th anniversary of Atatürk's death, for relations 'on the principles established by Lenin and Ataturk') reads the formula as an invitation to Turkey to return to 'Kemalist neutrality'. No verbatim quote located; the Izvestiya/Pravda text of the speech is the next step. Same formula in Kosygin's December 1966 and Sunay's 1969 exchanges (also second-hand).",
      urls=["https://dergipark.org.tr/en/download/article-file/5369767", "https://dergipark.org.tr/en/download/article-file/5289202"],
      loc="Özer and Güngör 2026 (Podgorny, Jan 1965); Yeşilbursa 2026 (Soviet call, Nov 1963; Podgorny visit)", link="Soviet Leaders on the Kemalists, 1920–1930",
      nxt="Izvestiya/Pravda 5-6 Jan 1965 (speech at the Grand National Assembly)"),
 dict(id="brezhnev-1978", voice="Leonid Brezhnev", role="General Secretary of the CPSU; speech in the collection Peace, Detente and Soviet-American Relations (1979)", c="Soviet Union", cn="Russia",
      dom="politics", date="1978", era="posthumous", mirror=None, pol="instrumental", inten=1,
      saw="Names Lenin and Atatürk together as the authors of the road on which Soviet-Turkish friendship is to continue.",
      q="the road charted long ago by Lenin and Ataturk.",
      art="speech", ev="J", med=None, src=None,
      cav="Seen only as archive.org search-inside snippets (peacedetenteso00brez, published 1979; and ourcoursepeaceso0000libr, 'Our Course, Peace and Socialism'). The snippet reads '... along the road charted long ago by Lenin and Ataturk. In general I agree with the words of West German Chancellor ...'. The index puts Ecevit and Turkey on p. 223 together, and the preceding snippets welcome the 1978 visit of Prime Minister Ecevit, so the date is 1978 (speech and occasion unidentified; the Ecevit visit was June 1978); the exact page and speech are not confirmed. Both books are lending-only.",
      urls=["https://archive.org/details/peacedetenteso00brez", "https://archive.org/details/ourcoursepeaceso0000libr"],
      loc="Brezhnev, Peace, Detente and Soviet-American Relations (1979), index p. 223 (search-inside, page unseen)", link="Soviet Leaders on the Kemalists, 1920–1930",
      nxt="Borrow the book (Internet Archive) to read p. 223 and name the speech; Pravda 1978"),
]

for r in R:
    assert len(r["saw"].split()) <= 25, (r["id"], len(r["saw"].split()))
    if r["src"]:
        assert norm(r["q"]).rstrip(",") in bank(r["src"]), r["id"]
        print("quote verified:", r["id"])
    else:
        print("no banked text:", r["id"])

with open(os.path.join(STATE, "gazes_leaders2.jsonl"), "w", encoding="utf-8") as f:
    for r in R:
        rec = {"id": r["id"], "voice": r["voice"], "voice_type": "person", "role": r["role"], "country": r["c"],
               "country_now": r["cn"], "domain": r["dom"], "date": r["date"], "era": r["era"], "mirror": r["mirror"],
               "polarity": r["pol"], "intensity": r["inten"], "what_they_saw": r["saw"], "quote": r["q"],
               "artifact": r["art"], "evidence": r["ev"], "mediated_by": r["med"], "caveat": r["cav"],
               "node": NODE, "sources": r["urls"]}
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")

with open(os.path.join(STATE, "ledger_leaders2.md"), "w", encoding="utf-8") as f:
    f.write("| Claim | Node | Status | Sources | Next step |\n|---|---|---|---|---|\n")
    for r in R:
        qs = r["q"] or "(paraphrase of reported speech)"
        f.write("| %s (%s, %s): \"%s\" | %s | verified %s (%s) | %s | %s |\n" % (
            r["voice"], r["role"][:50], r["date"], qs[:110].replace("|", "/") + ("..." if len(qs) > 110 else ""),
            NODE, r["ev"], r["loc"], "; ".join(r["urls"][:1]), r["nxt"] or "none"))

new_people = {
 "Enver Hoxha": ("First Secretary of the Party of Labour of Albania, 1948–1985", "Albanian", "1908–1985", "admirer (instrumental in 1967)",
    "Between 1967 and 1982 he named Atatürk four times, each time favourably: as the victor over Venizelos's forces, a 'great statesman', and an 'outstanding democrat' who destroyed the Caliphate."),
 "Edvard Beneš": ("President of Czechoslovakia, 1935–1938 and 1945–1948", "Czechoslovak", "1884–1948", "conflicted",
    "In his Chicago lectures (1939) he lists Atatürk's dictatorship among the interwar dictatorships, but credits his victory and 'courageous modernisation' for its authority."),
 "Nikolai Podgorny": ("Soviet head of state, 1965–1977", "Soviet", "1903–1983", "instrumental",
    "On his January 1965 visit to Ankara he urged a return to the friendship of the Lenin and Atatürk eras (second-hand report)."),
 "Leonid Brezhnev": ("General Secretary of the CPSU, 1964–1982", "Soviet", "1906–1982", "instrumental",
    "In a 1978 speech he names Lenin and Atatürk as the authors of the road of Soviet-Turkish friendship (search-inside snippet)."),
}
for name, (role, nat, life, stance, desc) in new_people.items():
    if os.path.exists(os.path.join(HERE, "vault", "People", name + ".md")):
        continue
    person(name, role=role, nat=nat, life=life, stance=stance, tags=["verified", "statesman"],
           body="%s See [[%s]] for the quotes and sources.\n\n## Sources\n- See [[%s]].\n" % (desc, NODE, NODE))

body = ["""
Round 16 looked for heads of state and party in regions the census had thin: the Balkans, the Soviet bloc, Latin America, Asia, and the
Middle East. The archive.org full-text search found seven usable voices, and one of them (Enver Hoxha) turned out to be a
sustained admirer over fifteen years: the Albanian Communist leader's praise of a Muslim, secularizing, non-communist statesman is the
most surprising result.

## The pattern

- **The Albanian dictator's Atatürk:** [[Enver Hoxha]] wrote and said it four times. In 1967 he used the victory over Greece as a warning in the Cyprus
  quarrel; in a letter of 8 September 1981 he thanked the municipality of Gölcük for a bronze portrait of Atatürk and called him a great statesman; in 1981 and 1982 he
  put him in his party report and electoral address as an 'outstanding democrat' who destroyed the Caliphate. He also says Atatürk
  opposed [[King Zog I]], which is Hoxha's own reading and is not confirmed elsewhere in the census.
- **The Czechoslovak exile:** [[Edvard Beneš]], writing in 1939, treats Atatürk as one of the interwar dictators and also credits his modernization with the authority that kept him in power.
- **The Soviet formula 'Lenin and Atatürk':** from the 25th anniversary of his death in November 1963 Moscow's rhetoric returns to the early-1920s friendship. [[Nikolai Podgorny]] (1965) and
  [[Leonid Brezhnev]] (1978) use it; Podgorny's Assembly speech of 5 January 1965 is in the TBMM record (stored once, under the Assembly note); Brezhnev's line, from his Minsk speech of 25 June 1978, is seen only as a search-inside snippet. See also [[Nikita Khrushchev]] (1959) and [[Soviet Leaders on the Kemalists, 1920–1930]].
"""]
for r in R:
    body.append("\n## %s (%s)\n" % (r["voice"], r["date"]))
    body.append("*%s*\n" % r["saw"])
    if r["q"]:
        body.append("> %s\n" % r["q"])
    body.append("%s Location: %s. Evidence %s. See [[%s]].\n" % (r["cav"], r["loc"], r["ev"], r["link"]))

body.append("""
## Not stored, and dry ends (round 16)

- **No hits under the author's own name in archive.org full-text search:** Tito, Perón, Pilsudski (and Masaryk, Mikoyan), Kim Il-sung, Deng Xiaoping, Park Chung-hee, Zhou Enlai (the fts matched his books but showed no Kemal text), Makarios, Karamanlis, Georgios and Andreas Papandreou, Ceaușescu, Zhivkov, Begin, Cárdenas and Vargas (the only 'Cárdenas' hit is Eduardo, a Spanish writer). Haya de la Torre: five open works (Por la emancipación de América Latina, Teoría y táctica del aprismo, Treinta años de aprismo, a 1931 speech) have no Kemal or Atatürk. Aflaq and Antoun Saadeh: open texts have no match.
- **Fidel Castro:** the only hit is his 'Reflections' of 8 April 2009 on Obama, which reports that Obama 'pay[ed] tribute to Mustafa Kemal Ataturk' on arriving in Turkey. This is a description, not Castro's view; the claim that Castro admired Atatürk comes from a 2016 condolence-book entry by Turkey's opposition leader, not from Castro.
- **Ben-Gurion, *My Talks with Arab Leaders* (1973):** snippets include '(Ataturk was also a dictator)' and 'who was also a cautious man' (about the Englishman Armstrong), but the speaker of each is not shown. A lead only; borrow the book.
- **Sadat, *Speeches and Interviews* (1975):** snippets of Sadat's tale of his father's fascination with Atatürk and the Cairo photograph. Another lead for the existing Sadat 1978 record; speaker and page not shown.
- **Khrushchev beyond 1959:** the 1963 volume *Khrushchev Speaks* indexes Atatürk at p. 402; probably the same 1959 report, unconfirmed.
- **Indian prime ministers, German chancellors:** a search of pib.gov.in/pmindia.gov.in found no Vajpayee, Singh or Modi statement; a Schröder photo of 2004 hangs an Atatürk portrait behind him but he states no view. Kosygin (December 1966) laid a wreath at Anıtkabir; no statement found.
- **Bourguiba:** no new text; 1965 stands.
- **Not reached:** Faisal I and Nuri al-Said, Syngman Rhee, Marcos, Allende, Calles, Gorbachev, Kim Il-sung's memoirs *With the Century*, Chiang's diary.

## Sources
- archive.org full-text search and open scans; the identifier of each is given in the record above.
- DergiPark: Özer and Güngör 2026; Yeşilbursa 2026.
""")
note("Events", NODE, {"type": "event", "when": "1939–1982", "tags": ["event", "verified", "statesmen", "memoirs"]}, "\n".join(body))
print("ok", len(R), "records")
