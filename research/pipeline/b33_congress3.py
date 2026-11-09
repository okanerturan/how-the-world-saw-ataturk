# -*- coding: utf-8 -*-
# Census round 24 (Nov 2026) — closing the US Congressional Record seam (GovInfo, free).
# Banks (tools/.state/round24/txt/):
#   CREC-*.txt       daily edition 1994-2026, HTML text of the 86 granules found by the GovInfo web search (Ataturk, Kemal Pasha, Mustafa Kemal ...).
#   GPO-CRECB-*.txt  pdftotext of bound-edition granule / Appendix-volume PDFs not read in rounds 22-23 (1920-1992).
# The script refuses to run if a quote is not found in its bank. Two-column OCR interleaves, so the check is a word/pair match
# inside a window after the anchor (as in b31_congress.py / b32_congress2.py).
import json, os, re, sys, html
from _lib import note, person

HERE = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(HERE, "tools", ".state", "round24")
BANK = os.path.join(STATE, "txt")

NODE = "Congressional Record Closing Pass — King, Owen, Davis, Sirovich, Pepper, Knowland and Others"


def words(s):
    s = html.unescape(s)
    s = s.replace("``", '"').replace("''", '"').replace("’", "'").replace("“", '"').replace("”", '"')
    return re.findall(r"[A-Za-z0-9]+", s.lower())


def read_bank(fn):
    t = open(os.path.join(BANK, fn), encoding="utf-8", errors="ignore").read()
    t = re.sub(r"\n\s*\d{3,5}\s*\n", "\n", t)
    t = re.sub(r"-\n\s*", "", t)
    return t


def check(fn, anchor, quote, window=3500):
    t1 = re.sub(r"\s+", " ", read_bank(fn))
    ws = words(quote)
    pairs = set(zip(ws, ws[1:]))
    for m in re.finditer(anchor, t1):
        seg = words(t1[max(0, m.start() - window): m.start() + window])
        have = set(seg)
        spairs = set(zip(seg, seg[1:]))
        miss = [w for w in set(ws) if w not in have]
        if len(miss) <= 2 and len(pairs & spairs) >= 0.75 * len(pairs):
            return True
    return False


GOV = "https://www.govinfo.gov/content/pkg/"


def url_b(g):  # bound edition: GPO-CRECB-<yyyy>-pt<N>[-v<V>]-<n>[-<m>] -> package without the granule suffix
    pkg = re.sub(r"-\d+(-\d+)?$", "", g)
    return "%s%s/pdf/%s.pdf" % (GOV, pkg, g)


def url_d(g):  # daily edition: CREC-<date>-pt1-Pg...
    day = re.match(r"(CREC-\d{4}-\d{2}-\d{2})", g).group(1)
    return "%s%s/html/%s.htm" % (GOV, day, g)


R = []


def add(**k):
    R.append(k)


# ---------------------------------------------------------------- contemporary: 1921-1938
add(id="king-1921-12", voice="William H. King", role="U.S. Senator from Utah (Democrat)", date="1921-12-22", era="contemporary", mirror=None, pol="hostile", inten=2,
    cite="Senate, 22 December 1921, Congressional Record vol. 62 (bound), p. ~691 (granule CRECB-1922-pt1-v62-16-1)",
    saw="Presenting his resolution on the Pontic Greeks, says the evidence is conclusive and only outside force can restrain 'the bloody hands of Mustapha Kemal'.",
    q="Unless some steps shall be taken by forces outside of Turkey to restrain the bloody hands of Mustapha Kemal, there would seem to be no hope of salvation for these unfortunate people, whose only offense is that they are Christians",
    g="GPO-CRECB-1922-pt1-v62-16-1", anchor="bloody hands of Mustapha",
    cav="His own words in the Senate; the resolutions, the Ecumenical Patriarchate statements ('tyrant of Asia Minor') and the mass-meeting texts he has printed with them are not counted. Sensitive thread (Pontic Greeks, 1919-23): the speech is King's advocacy and his framing, not the vault's. He repeats the charge on 2 Feb 1922 (p. ~2048). Page from the OCR running heads; the scan is two-column.")
add(id="owen-1923-01", voice="Robert L. Owen", role="U.S. Senator from Oklahoma (Democrat)", date="1923-01-26", era="contemporary", mirror="anti-colonial-liberator", pol="admiring", inten=2,
    cite="Senate, 26 January 1923, 'Mustapha Kemal — Conditions in Near East', Congressional Record vol. 64 (bound), p. ~2487 (granule CRECB-1923-pt3-v64-4-1)",
    saw="Introduces Kemal's address to the American people as 'remarkable': an educated man speaking for Turks who, like the Founders, want to be rid of outside domination.",
    q="here is a man who speaks the American language, though he be a Turk; a man who is highly educated; one who is informed with regard to the history of the nations of the world",
    q2="He is entitled to a hearing.",
    g="GPO-CRECB-1923-pt3-v64-4-1", anchor="remarkable address",
    cav="Owen's own introduction (about 200 words); the Herald interview and the address he has printed ('Kemal demands absolute independence for Turkey', including the 'George Washington' remark) are Kemal's and are not counted. Senator King answers him in the same sitting (see his record). Cited alongside the Lausanne conference, a month into its first session.")
add(id="king-1923-01", voice="William H. King", role="U.S. Senator from Utah (Democrat)", date="1923-01-26", era="contemporary", mirror=None, pol="hostile", inten=2,
    cite="Senate, 26 January 1923, Congressional Record vol. 64 (bound), p. ~2488 (granule CRECB-1923-pt3-v64-4-1)",
    saw="Answering Owen, calls Kemal Pasha's appeal to America 'a most adroit and intriguing document' that seeks to blunt criticism of Kemalist treatment of Christians.",
    q="The appeal by Kemal Pasha, to which the Senator refers, is a most adroit and intriguing document.",
    q2="the barbarities perpetrated by the Kemalists and the Turks upon Christian minorities",
    g="GPO-CRECB-1923-pt3-v64-4-1", anchor="most adroit",
    cav="His own words in reply to Owen; he goes on to review the Armenian case. Sensitive thread (Armenians, Greeks): the speaker's framing. Two-column OCR; the second fragment is taken from the next lines of the same speech and joined with an ellipsis.")
add(id="berger-1927-01", voice="Victor L. Berger", role="U.S. Representative from Wisconsin (Socialist)", date="1927-01-18", era="contemporary", mirror=None, pol="hostile", inten=2,
    cite="House of Representatives, 18 January 1927, Congressional Record vol. 68 (bound), pp. ~1881-1882 (granule CRECB-1927-pt2-v68-10-2)",
    saw="Opposing ratification of the Lausanne treaty, denounces Kemal Pasha as a 'murderous tyrant' under whom Greeks and Armenians were slaughtered; refuses to speak of a 'New Turkey'.",
    q="Under the barbaric reign of Kemal Pasha millions of Greeks and Armenians have been ruthlessly slaughtered.",
    q2="big business and moral cowardice demand that we make a treaty with this murderous tyrant",
    g="GPO-CRECB-1927-pt2-v68-10-2", anchor="murderous tyrant",
    cav="His own speech (the Socialist congressman's remarks on Mexico, the army bill and Turkey); the passages he quotes from Bishop Manning and from Bishop Cannon's article ('The Turkey of Kemal is as bankrupt morally as that of the Sultan') are not counted. Sensitive thread (Armenian and Greek massacres, the Lausanne ratification fight): the speaker's framing, not the vault's. Two-column OCR.")
add(id="davis-1933-01", voice="James J. Davis", role="U.S. Senator from Pennsylvania (Republican), former Secretary of Labor", date="1933-01-03", era="contemporary", mirror="modernization-poster-child", pol="admiring", inten=1,
    cite="Senate, 3 January 1933, Congressional Record vol. 76 (bound), p. ~1195 (granule CRECB-1933-pt2-v76-1-1); the same words are quoted as his in Sherrill's address printed by him on 24 March 1934 (vol. 78, p. ~5299)",
    saw="Hails Kemal's Christmas Day 1932 ban on the narcotic trade as a 'magnificent Christmas gift' that makes Turkey's President one of the leading figures of the anti-narcotic war.",
    q="The world, and especially America, received this magnificent Christmas gift in the form of a ban on that day on the narcotic trade by President Mustapha Kemal, of Turkey.",
    q2="This makes the President of Turkey one of the outstanding leaders in the international antinarcotic war.",
    g="GPO-CRECB-1933-pt2-v76-1-1", anchor="Christmas gift", frags_q=["The world, and especially America, received this", "Christmas gift in the form of a ban on that day on the narcotic trade by President Mustapha Kemal, of Turkey"],
    frags_q2=["This makes the President of Turkey one of the outstanding leaders in the"],
    cav="Davis's own paragraph beside the Washington Star and Washington Herald cuttings that he has printed (not counted: 'Kemal places ban on narcotic trade'). In the 24 March 1934 sitting he introduces Ambassador Sherrill's radio address on Kemal's narcotics crusade, saying 'the gigantic strides Mustafa Kemal has made' in transforming his nation; that sentence is a second statement of the same view. A second Davis record already exists (22 April 1943). Two-column OCR.")
add(id="sirovich-1934-04", voice="William I. Sirovich", role="U.S. Representative from New York (Democrat)", date="1934-04-24", era="contemporary", mirror="modernization-poster-child", pol="conflicted", inten=2,
    cite="House of Representatives, 24 April 1934, hour-long special order 'The Administration of President Roosevelt', Congressional Record vol. 78 (bound), pp. ~7233-7234 (granule CRECB-1934-pt7-v78-6-2)",
    saw="Calls Kemal Pasha 'the dictator of Turkey' yet credits his liberalism, women's liberation and education with creating a new nation 'dedicated to the principles of liberalism and progressivism'.",
    q="Kemal Pasha, the dictator of Turkey. What a name to conjure with.",
    q2="a new nation with new ideals, dedicated to the principles of liberalism and progressivism",
    g="GPO-CRECB-1934-pt7-v78-6-2", anchor="Kemal Pasha, the dictator", frags_q2=["a new nation with new ideals, dedicated to the principles of liberalism and progressivism"],
    cav="His own words, one passage in a survey of dictators (Mussolini, Hitler, Dollfuss, Stalin, Kemal) used to argue that the New Deal is none of them: Kemal is ranked as a dictator whose reforms nonetheless worked ('Turkey is growing and developing under the benign influence of occidental civilization'). The paragraph sits in two columns of OCR with hyphenation broken, so the quote is rebuilt from adjacent lines. Sirovich was a physician and playwright and chaired the House Patents Committee.")
add(id="pittman-1935-01", voice="Key Pittman", role="U.S. Senator from Nevada, chairman of the Foreign Relations Committee (Democrat)", date="1935-01-23", era="contemporary", mirror=None, pol="admiring", inten=1,
    cite="Radio address of 23 January 1935 for the World Narcotic Defense Association, printed in the Senate 28 February 1935, Congressional Record vol. 79 (bound), p. ~2715 (granule CRECB-1935-pt3-v79-6-1)",
    saw="In a radio appeal for a US narcotics law, cites Turkey stopping the opium poppy 'under the leadership of their great President Mustafa Kemal' as a standard America has not reached.",
    q="Turkey, which supplied most of the opium of the world, whose people made a living out of it, under the leadership of their great President Mustafa Kemal, stopped producing the opium poppy and hemp!",
    g="GPO-CRECB-1935-pt3-v79-6-1", anchor="great President Mustafa Kemal",
    cav="His own broadcast, which he asked to have printed; the address of ex-Vice President Curtis and the announcer's remarks around it are not counted. One sentence. Speaker confirmed by the heading 'Address of Hon. Key Pittman'. Two-column OCR.")
# ---------------------------------------------------------------- posthumous: 1947-1956
add(id="hand-1947-05", voice="T. Millet Hand", role="U.S. Representative from New Jersey (Republican), opponent of the Greek-Turkish aid bill", date="1947-05-07", era="posthumous", mirror=None, pol="hostile", inten=1,
    cite="House of Representatives, 7 May 1947, Greek-Turkish aid debate (H.R. 2616), Congressional Record vol. 93 (bound), p. ~4738 (granule CRECB-1947-pt4-6-2)",
    saw="Arguing there is no democracy to defend in Turkey, calls Kemal Pasha's rule 'practically the first rigid dictatorship' that 'knew all about dictatorship long before' Hitler, Mussolini and Stalin.",
    q="in modern times under practically the first rigid dictatorship, that of Kemal Pasha, who knew all about dictatorship long before Hitler, Mussolini, and Stalin.",
    g="GPO-CRECB-1947-pt4-6-2", anchor="rigid dictatorship, that of Kemal", frags_q=["rigid dictatorship, that of Kemal Pasha, who knew all about dictatorship long", "Hitler, Mussolini, and Stalin"],
    cav="Speaker established from the sequence in the transcript (Eaton yields to Hand, then to Hale; the passage ends the Hand speech). The scan interleaves the columns; the quote is rebuilt from adjacent lines. The 'unnamed opponent' lead of round 22 is this passage. A label with a stated judgement of the regime, intensity 1.")
add(id="powell-1956-07", voice="Adam Clayton Powell Jr.", role="U.S. Representative from New York (Harlem)", date="1956-07-25", era="posthumous", mirror="modernization-poster-child", pol="admiring", inten=2,
    cite="Extensions of Remarks (House), 25 July 1956, Congressional Record vol. 102 (bound), granule CRECB-1956-pt11-1-3",
    saw="Sends advance Republic Day greetings and credits the 'dynamic leadership of Ataturk' with the reform programme that turned a backward country into a modern state.",
    q="Under the dynamic leadership of Ataturk a vigorous reform program was started and quick progress was registered in industrialization and modernization of the country.",
    g="GPO-CRECB-1956-pt11-1-3", anchor="dynamic leadership of Ataturk",
    cav="The first of the greetings of the Bandung-conference kind that he also sent in 1957 (staged separately); the economic summary reads like embassy-supplied material, so it is a courtesy text as well as a view. OCR 'ind~pendence', 'started ~nd' repaired. Printed page number (A-series) not legible in the OCR.")
# ---------------------------------------------------------------- daily edition 1994-2026
add(id="wexler-2001-10", voice="Robert Wexler", role="U.S. Representative from Florida (Democrat)", date="2001-10-31", era="posthumous", mirror="modernization-poster-child", pol="admiring", inten=2,
    cite="Extensions of Remarks (House), 31 October 2001, 'Tribute to the Government of the Republic of Turkey', Congressional Record vol. 147, pp. E1969-E1970 (granule CREC-2001-10-31-pt1-PgE1969-3)",
    saw="On Republic Day, says Turkey became the secular, modern democracy Atatürk envisioned and calls him one of the twentieth century's greatest leaders.",
    q="Over the past seventy-eight years, Turkey has emerged as the secular and modern democracy that Kemal Ataturk envisioned in 1923.",
    q2="one of the twentieth century's greatest leaders, Mustafa Kemal Ataturk",
    g="CREC-2001-10-31-pt1-PgE1969-3", anchor="seventy-eighth anniversary",
    cav="His own Republic Day felicitation, written seven weeks after 11 September to praise Turkey's support. Ankara-friendly courtesy text as well as a view.")
add(id="maloney-2006-05", voice="Carolyn B. Maloney", role="U.S. Representative from New York (Democrat)", date="2006-05-18", era="posthumous", mirror=None, pol="hostile", inten=1,
    cite="Extensions of Remarks (House), 18 May 2006, Congressional Record vol. 152, p. E874 (granule CREC-2006-05-18-pt1-PgE874)",
    saw="In a Pontian Greek remembrance statement, says the Ottoman 'genocide' of Christians was practised 'largely under the leadership of Kemal Ataturk'.",
    q="From 1916 to 1923, largely under the leadership of Kemal Ataturk, the Ottoman Empire began to practice a ferocious genocide of the Christian population within its borders.",
    g="CREC-2006-05-18-pt1-PgE874", anchor="largely under the leadership of Kemal",
    cav="Sensitive thread (Pontic Greeks, 1914-23). A summary of the Pan-Pontian Federation's case which she adopts; the dating 'from 1916' and the attribution to Kemal are the speaker's framing and do not follow the standard chronology (Mustafa Kemal commanded on Ottoman fronts from 1915 and led the national movement from 1919). The vault does not adopt the framing.")
add(id="dreier-2007-02", voice="David Dreier", role="U.S. Representative from California (Republican), ranking member of the Rules Committee", date="2007-02-13", era="posthumous", mirror=None, pol="instrumental", inten=1,
    cite="House of Representatives, 13 February 2007, debate on H. Con. Res. 63 (Iraq), Congressional Record vol. 153, p. H1479 (granule CREC-2007-02-13-pt1-PgH1479-6)",
    saw="In the Iraq-war debate, says the US should have learned from Atatürk's creation of the modern Turkish state, where religious parties' role in politics was limited.",
    q="we should have learned the lessons from a neighbor of Iraq, from the creation in the 20th century of the Turkish state, modern Turkish state, by Ataturk, the father of that state, where the ability of religious parties, for example, to insert themselves into the political process was significantly limited.",
    g="CREC-2007-02-13-pt1-PgH1479-6", anchor="lessons from a neighbor of Iraq",
    cav="Floor aside in the rule debate on the Iraq resolution; Atatürk is a model for his Iraq argument.")
add(id="schmidt-2008-05", voice="Jean Schmidt", role="U.S. Representative from Ohio (Republican)", date="2008-05-22", era="posthumous", mirror="modernization-poster-child", pol="admiring", inten=2,
    cite="Extensions of Remarks (House), 22 May 2008, 'Commemorating May 19 as Ataturk, Youth and Sports Day in Turkey', Congressional Record vol. 154, p. E1094 (granule CREC-2008-05-23-pt1-PgE1094)",
    saw="Marks 19 May as the day 'a great leader began his journey' and says his vision of a pro-Western, secular, democratic state under the rule of law quickly became reality.",
    q="Ataturk had a vision for Turkey and he set about reforming her. His vision of a pro-western, secular, and democratic state under the rule of law quickly became reality.",
    g="CREC-2008-05-23-pt1-PgE1094", anchor="Ataturk had a vision",
    cav="Her own statement, which also quotes Kennedy and MacArthur on Atatürk (those quotations are not counted). Text closely parallels statements by Foxx, Cohen and Poe in other years, i.e. a template supplied by the Turkish-American lobby; a courtesy text as well as a view.")
add(id="foxx-2009-05", voice="Virginia Foxx", role="U.S. Representative from North Carolina (Republican), co-chair of the Turkish Study Group", date="2009-05-19", era="posthumous", mirror="modernization-poster-child", pol="admiring", inten=2,
    cite="Extensions of Remarks (House), 19 May 2009, '128th Anniversary of the Birth of Kemal Ataturk, Founder of Modern Turkey', Congressional Record vol. 155, p. E1196 (granule CREC-2009-05-19-pt1-PgE1196-3)",
    saw="On his 128th birthday calls Atatürk 'a unique and inspirational figure', an impatient reformer, and urges Muslim leaders to take inspiration from his revolution.",
    q="Ataturk was a unique and inspirational figure who laid the foundation for the Republic of Turkey.",
    q2="By any measure, Ataturk was an historic reformer.",
    g="CREC-2009-05-19-pt1-PgE1196-3", anchor="unique and inspirational figure",
    cav="Her own statement; near-identical in structure to Tom Lantos's 2006 statement (a staged record), which she follows. She also spoke on 15 Oct 2007 ('the visionary leader of modern Turkey', Armenian resolution debate), 22 Apr 2008 and 28 May 2010 (a birthday-party speech by a 16-year-old, not counted).")
add(id="connolly-2010-11", voice="Gerry Connolly", role="U.S. Representative from Virginia (Democrat), co-chair of the Congressional Caucus on Turkey", date="2010-11-18", era="posthumous", mirror="modernization-poster-child", pol="admiring", inten=1,
    cite="Extensions of Remarks (House), 18 November 2010, 'Honoring the Republic of Turkey's 87th Republic Day', Congressional Record vol. 156, pp. E1984-E1985 (granule CREC-2010-11-18-pt1-PgE1984-4)",
    saw="On Republic Day, credits 'the visionary leadership of Mustafa Kemal Ataturk and his successors' with turning Turkey into a modern, secular state allied with the democracies.",
    q="Under the visionary leadership of Mustafa Kemal Ataturk and his successors, Turkey transformed itself into a modern, secular state allied with the democracies of Europe and the Americas.",
    g="CREC-2010-11-18-pt1-PgE1984-4", anchor="visionary leadership of Mustafa Kemal",
    cav="One of the Republic Day extensions of November 2010 (Whitfield, Cohen, Sessions, Shuster, Towns, Wilson, Delahunt and Foxx wrote similar paragraphs); he is the one who names Atatürk's leadership as 'visionary'. Caucus courtesy text.")
add(id="cohen-2012-11", voice="Steve Cohen", role="U.S. Representative from Tennessee (Democrat), co-chair of the Congressional Turkey Caucus", date="2012-11-13", era="posthumous", mirror="modernization-poster-child", pol="admiring", inten=2,
    cite="Extensions of Remarks (House), 13 November 2012, 'Remembering Kemal Ataturk', Congressional Record vol. 158, p. E1741 (granule CREC-2012-11-13-pt1-PgE1741-2)",
    saw="Marking the anniversary of Atatürk's death, calls him the leader who turned an agrarian society into a modern, secular, Western-facing model, 'a great man and a great leader'.",
    q="Kemal Ataturk, the leader of modern Turkey who transformed that country from an agrarian society caught in the past to a modern, secular and forward looking western model.",
    q2="I join my friends in paying tribute to a great man and a great leader.",
    g="CREC-2012-11-13-pt1-PgE1741-2", anchor="premature death of Kemal Ataturk",
    cav="His own statement, which also quotes Kennedy and a Churchill line of unverified provenance on Atatürk (not counted). Cohen made similar statements on 19 May 2011, 17 May 2012, 17 Nov 2010 and 26 Oct 2023.")
add(id="gosar-2015-01", voice="Paul Gosar", role="U.S. Representative from Arizona (Republican)", date="2015-01-30", era="posthumous", mirror=None, pol="instrumental", inten=1,
    cite="Extensions of Remarks (House), 30 January 2015, 'Freedom of Speech in Turkey', Congressional Record vol. 161, p. E136 (granule CREC-2015-01-30-pt1-PgE136-2)",
    saw="Criticising the Erdogan government's arrests of journalists, says Turkey is drifting from 'the tolerant secular nation founded by Kemal Ataturk' and that 'the Turkey founded by Ataturk deserves our support'.",
    q="Turkey is drifting away from the tolerant secular nation founded by Kemal Ataturk almost 100 years ago and towards religious extremism and authoritarianism.",
    q2="The Turkey founded by Ataturk deserves our support.",
    g="CREC-2015-01-30-pt1-PgE136-2", anchor="drifting away from the tolerant secular nation",
    cav="Uses Atatürk as the benchmark against which he measures Erdogan; the statement mirrors the Gülenist critique of the government. Atatürk is evoked, not analysed.")
add(id="king-2016-01", voice="Steve King", role="U.S. Representative from Iowa (Republican)", date="2016-01-11", era="posthumous", mirror="modernization-poster-child", pol="instrumental", inten=1,
    cite="House of Representatives, 11 January 2016, 'Egypt Talking Points', Congressional Record vol. 162, pp. H264-H267 (granule CREC-2016-01-11-pt1-PgH264)",
    saw="Praising Egypt's President Sisi, recalls Atatürk as the bridge between East and West, and hopes Sisi could become 'the Ataturk for the world' bridging Muslim and Christian worlds.",
    q="When I look at the work that was done by Ataturk in Turkey, how he provided a bridge between the East and the West, and that has been drifting back a bit the other way under Erdogan",
    q2="could become the Ataturk for the world to bring about that bridge between the Muslim world and the Christian world and the West",
    g="CREC-2016-01-11-pt1-PgH264", anchor="work that was done by Ataturk",
    cav="One-minute-style floor speech on Egypt; Atatürk is the template for what he wants Sisi to be. The second fragment follows after the page break to H267. A second King remark, 13 July 2017 (p. H5823), says Atatürk 'for 40 years, moved Turkey to the West' (not staged separately).")
add(id="wilson-2020-10", voice="Joe Wilson", role="U.S. Representative from South Carolina (Republican)", date="2020-10-30", era="posthumous", mirror="modernization-poster-child", pol="admiring", inten=1,
    cite="Extensions of Remarks (House), 30 October 2020, Congressional Record vol. 166, p. E1002 (granule CREC-2020-10-30-pt1-PgE1002-2)",
    saw="On the 97th Republic Day calls Atatürk 'the visionary leader of modern Turkey' under whom the country rose from ashes into a stable, growing democracy.",
    q="It was on this day in 1923 when Mustafa Kemal Ataturk, the visionary leader of modern Turkey, became its first President. Under his leadership, Turkey rose from the ashes of a war-torn country into a confident, stable, and growing democracy.",
    g="CREC-2020-10-30-pt1-PgE1002-2", anchor="visionary leader of modern Turkey",
    cav="His own felicitation. Similar lines in his 18 Nov 2010 Republic Day extension (p. E1964) and, on the floor on 27 Feb 2023 (p. H886), 'our recognition of Kemal Ataturk and his success in creating a democracy in the Middle East'; on 11 Jan 2024 he mentions laying a wreath at Anıtkabir (a ceremony, no stated view).")


# ---- add further records here (Appendix volumes) ----
EXTRA = os.path.join(STATE, "extra_records.py")
if os.path.exists(EXTRA):
    exec(open(EXTRA, encoding="utf-8").read())


SAW = {
 "king-1921-12": "Presenting his Pontic Greeks resolution, says only outside force can restrain 'the bloody hands of Mustapha Kemal'.",
 "owen-1923-01": "Introduces Kemal's address to America as 'remarkable': an educated man, speaking for Turks who, like the Founders, want freedom from outside domination.",
 "king-1923-01": "Answering Owen, calls Kemal Pasha's appeal to America 'a most adroit and intriguing document' meant to soften criticism of Kemalist treatment of Christians.",
 "berger-1927-01": "Opposing the Lausanne treaty, denounces Kemal Pasha as a 'murderous tyrant' under whom Greeks and Armenians were slaughtered; rejects talk of a 'New Turkey'.",
 "davis-1933-01": "Hails Kemal's Christmas Day 1932 narcotics ban as a 'magnificent Christmas gift' making Turkey's President an outstanding anti-narcotics leader.",
 "sirovich-1934-04": "Calls Kemal Pasha 'the dictator of Turkey' yet credits his reforms with creating a new nation 'dedicated to the principles of liberalism and progressivism'.",
 "pittman-1935-01": "In a radio appeal for a US narcotics law, cites Turkey's end of opium growing under 'their great President Mustafa Kemal'.",
 "hand-1947-05": "Arguing Turkey is no democracy, calls Kemal Pasha's rule 'practically the first rigid dictatorship', older than Hitler's, Mussolini's and Stalin's.",
 "dreier-2007-02": "In the Iraq debate, says the US should have learned from Atatürk's creation of modern Turkey, where religious parties' political role was limited.",
 "schmidt-2008-05": "Marking 19 May, says Atatürk's vision of a pro-Western, secular, democratic state under the rule of law quickly became reality.",
 "connolly-2010-11": "On Republic Day credits 'the visionary leadership of Mustafa Kemal Ataturk' with making Turkey a modern, secular state allied with the democracies.",
 "cohen-2012-11": "Marking Atatürk's death anniversary, calls him the leader who made an agrarian society a modern, secular, Western-facing model: 'a great man'.",
 "gosar-2015-01": "Criticising Erdogan's arrests of journalists, says Turkey is drifting from 'the tolerant secular nation founded by Kemal Ataturk', which 'deserves our support'.",
 "king-2016-01": "Praising Egypt's Sisi, recalls Atatürk as a bridge between East and West and hopes Sisi can become 'the Ataturk for the world'.",
 "culkin-1941-03": "Arguing the US cannot fight every dictatorship, lists Turkey: 'Kemal Ataturk was a dictator, and so is his successor'.",
 "kefauver-1947-04": "Reporting on a trip supporting Truman's aid, says Turkey 'is continuing the development program begun by her former President Ataturk'.",
 "bolton-1948-04": "Recalls a talk in Ankara about 'the great Kemal Pasha-Ataturk' who unveiled women and changed language and capital; 'religion, too, went'.",
 "knowland-1953-10": "Judging Egypt's Naguib after an Asian tour, says he has 'some of the zeal that Kemal Ataturk had' in modernising Turkey.",
 "dorn-1956-07": "Condemning the 1955 Istanbul riots, says the Turks in one night 'ruined the work of their great leader, Kemal Ataturk'.",
 "javits-1978-05": "In his report on Turkey and Greece, dates Turkey's Western ties to Atatürk's 'forced-draft westernization' and cites the Ataturk-Venizelos accord as a model.",
 "pepper-1942-04": "Praises Atatürk's 'thorough and radical revolution' and says that under him and Inönü the Turks made 'greater strides forward than any other people'.",
}
for r in R:
    if r["id"] in SAW:
        r["saw"] = SAW[r["id"]]

DROP = {'culkin-1941-03','berger-1927-01','dreier-2007-02','dorn-1956-07','powell-1956-07','gosar-2015-01','maloney-2006-05','kefauver-1947-04','javits-1978-05','celler-1953-04','bolton-1948-04','hand-1947-05','pittman-1935-01','connolly-2010-11','wilson-2020-10'}  # dropped at the independent check (wrong speaker, inserted text, or no view of the man)
R = [r for r in R if r["id"] not in DROP]

bad = []
for r in R:
    g = r["g"]
    r["bank"] = g + ".txt"
    r["url"] = url_d(g) if g.startswith("CREC-") else url_b(g)
    for k in ("q", "q2"):
        if not r.get(k):
            continue
        frs = r.get("frags_" + k) or [r[k]]
        if not all(check(r["bank"], r.get("anchor_" + k) or r["anchor"], fr) for fr in frs):
            bad.append((r["id"], k))
if bad:
    sys.exit("quote not found in source bank: %s" % bad)
if os.environ.get("CHECKONLY"):
    sys.exit("check ok: %d records" % len(R))
for r in R:
    assert len(r["saw"].split()) <= 25, (r["id"], len(r["saw"].split()))

with open(os.path.join(STATE, "gazes_congress3.jsonl"), "w", encoding="utf-8") as f:
    for r in R:
        q = r["q"] + ((" … " + r["q2"]) if r.get("q2") else "")
        rec = {"id": r["id"], "voice": r["voice"], "voice_type": "person", "role": r["role"],
               "country": "United States", "country_now": "United States", "domain": "politics", "date": r["date"], "era": r["era"],
               "mirror": r["mirror"], "polarity": r["pol"], "intensity": r["inten"], "what_they_saw": r["saw"],
               "quote": q, "artifact": "speech", "evidence": "P", "mediated_by": None,
               "caveat": r["cav"] + " Cited as " + r["cite"] + ".", "node": NODE, "sources": [r["url"]]}
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")

with open(os.path.join(STATE, "ledger_congress3.md"), "w", encoding="utf-8") as f:
    f.write("| Claim | Node | Status | Sources | Next step |\n|---|---|---|---|---|\n")
    for r in R:
        f.write("| %s (%s): %s | %s | verified P (Congressional Record, GovInfo; text read) | %s | page number from the printed volume where marked ~ |\n" % (
            r["voice"], r["date"], r["saw"], NODE, r["url"]))

EXISTING = {"James J. Davis", "Adam Clayton Powell Jr.", "Claude Pepper"}  # person notes already exist
voices = {}
for r in R:
    voices.setdefault(r["voice"], []).append(r)
PEOPLE_TAGS = ["verified", "us-congress", "congressional-record"]
for v, rs in voices.items():
    if v in EXISTING:
        continue
    stance = "; ".join("%s (%s)" % (x["pol"], x["date"][:4]) for x in rs)
    body = "%s.\n\n" % rs[0]["role"]
    for x in rs:
        body += "- %s: %s See [[%s]].\n" % (x["date"], x["saw"], NODE)
    body += "\n## Sources\n" + "\n".join("- %s — %s" % (x["cite"], x["url"]) for x in rs) + "\n"
    person(v, role=rs[0]["role"], nat="American", life="", stance=stance, tags=PEOPLE_TAGS, body=body)


def sec(r):
    q2 = ("\n>\n> %s" % r["q2"]) if r.get("q2") else ""
    return "## %s — %s\n\n%s\n\n> %s%s\n\n**Source.** %s — <%s>\n\n**Caveat.** %s\n" % (
        r["voice"], r["date"], r["saw"], r["q"], q2, r["cite"], r["url"], r["cav"])


NOTE_INTRO = os.path.join(STATE, "node_intro.txt")
intro = open(NOTE_INTRO, encoding="utf-8").read() if os.path.exists(NOTE_INTRO) else ""
body = (intro + "\n\nNames: " + ", ".join("[[%s]]" % v for v in voices) + ".\n\n"
        + "\n".join(sec(r) for r in R)
        + "\n## Sources\n- GovInfo, *Congressional Record* (CREC daily, CRECB bound): https://www.govinfo.gov/app/collection/crecb\n"
        + "\n".join("- %s — %s" % (r["cite"], r["url"]) for r in R) + "\n")
note("Events", NODE, {"type": "event", "when": "1921–2020", "tags": ["event", "verified", "united-states", "us-congress", "congressional-record"]}, body)
print("ok", len(R), "records,", len(voices), "people")
