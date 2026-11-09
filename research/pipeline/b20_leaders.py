# -*- coding: utf-8 -*-
# Census round 12 (Nov 2026) — famous interwar leaders in their own words about Atatürk / Kemalist Turkey.
# Records: Mussolini (1928 interview), Trotsky (1935 open letter), Ho Chi Minh (L'Humanité, 1 Jan 1924),
# Mao Zedong ("On New Democracy", Jan 1940), Reza Shah (1933 remark to Gerede; June 1934 telegram).
# Source texts were fetched with tools/ms fetch and banked in tools/.state/round12/src_*.txt; every quote is
# checked against its bank before anything is written.
import json, os, re, sys
from _lib import note

HERE = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(HERE, "tools", ".state", "round12")
NODE = "Interwar Leaders on Kemal in Their Own Words"

def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"').replace("­", "")
    s = re.sub(r"-\s*\n", "", s)
    return re.sub(r"\s+", " ", s)

def bank(n):
    return norm(open(os.path.join(STATE, n), encoding="utf-8").read())

R = [
 dict(id="mussolini-1928", voice="Benito Mussolini", role="Prime Minister of Italy (Duce)", c="Italy", cn="Italy",
      dom="politics", date="1928", era="contemporary", mirror="nation-forge-template", pol="admiring", inten=2,
      saw="Tells a Turkish journalist that Kemal is a great personage who has given Turkey its supreme benefit, and praises the Ankara model farm.",
      q="His Excellency Gazi Mustafa Kemal is a great personage who has bestowed the supreme boon and benefit upon Turkey.",
      art="quote", ev="S", med="Doğar 2026 (Contemporary European History 35, fn. 95) ← Çelebi, Türkiye–İtalya Ekonomik İlişkileri 1923–1939, p. 89 ← interview with Yunus Nadi (English rendering of the Turkish text)",
      cav="Second-hand and twice translated; the Yunus Nadi interview itself (Cumhuriyet, 1928; day not given) was not read, so the wording is the article's English. Doğar notes the praise came while Mussolini was courting Ankara and the same year Kemal sent his sons a gift; in Nov 1929 Mussolini sent a tractor to Kemal.  The 1920s Antalya/Anatolia rivalry is not covered by this record.",
      src=["src_dogar_mussolini.txt"],
      urls=["https://www.cambridge.org/core/journals/contemporary-european-history/article/turkish-fields-italian-wheels-mussolinis-gift-of-a-tractor-to-mustafa-kemal-in-1929/06163E26A5C2B34C09F75C05B1482AFE"],
      loc="Doğar, 'Turkish Fields, Italian Wheels', fn. 95; Çelebi p. 89", link="Benito Mussolini"),
 dict(id="ho-chi-minh-1924-01-01", voice="Nguyen Ai Quoc (Ho Chi Minh)", role="Vietnamese Comintern organiser, writing in L'Humanité", c="French Indochina (exile in Paris/Moscow)", cn="Vietnam",
      dom="politics", date="1924-01-01", era="contemporary", mirror="bourgeois-revolutionary", pol="conflicted", inten=2,
      saw="Admires the Turks for tearing up Sèvres and founding a republic, but calls it a bourgeois revolution that serves only the moneyed class.",
      q="But like all bourgeois revolutions, the Turkish revolution is profitable only to one class: the moneyed class.",
      art="article", ev="S", med="English text of the L'Humanité article as printed in Selected Works of Ho Chi Minh, vol. 1 (FLPH), via marxists.org; the French original was not read",
      cav="Kemal is not named in the article; it judges the revolution and the Ankara government (which refused to recognise the Istanbul workers' federation). Entered as the Indochinese communist reading of the Kemalist state. Signed in L'Humanité; the pen-name Nguyen Ai Quoc is inferred from the Selected Works attribution.",
      src=["src_ho_1924.txt"],
      urls=["https://www.marxists.org/reference/archive/ho-chi-minh/works/1924/01/01.htm"],
      loc="L'Humanité, 1 Jan 1924, 'The Workers' Movement in Turkey'", link="Ho Chi Minh"),
 dict(id="trotsky-1935-06-10", voice="Leon Trotsky", role="Exiled Bolshevik leader; lived at Prinkipo 1929–33 by Ankara's leave", c="Soviet Union (exile)", cn="Russia",
      dom="politics", date="1935-06-10", era="contemporary", mirror=None, pol="witness", inten=1,
      saw="Says his confinement in France was harsher than at Prinkipo under the police of Kemal Pasha, implicitly crediting Turkey's lighter hand.",
      q="I was cut off from the outside world more than when I lived on the island of Prinkipo, in Turkey, under the surveillance of the police of Kemal Pasha.",
      art="article", ev="P", med=None,
      cav="An open letter about French treatment, not about Kemal; the comparison is the only statement of view. Also read: on 12 Feb 1929 Trotsky gave the Turkish police at Büyükdere a note for 'the President of the Turkish Republic, Kemal Pasha', saying he came 'not of my own choice' and crossed only 'by submitting to force' (My Life, ch. 44). Not stored separately: it protests the Soviet deportation and states no view of Kemal. No Trotsky text on Kemalism itself was reached this round.",
      src=["src_trotsky_1935.txt"],
      urls=["https://www.marxists.org/archive/trotsky/1935/06/french.htm", "https://www.marxists.org/archive/trotsky/1930/mylife/ch44.htm"],
      loc="An Open Letter to the French Workers, 10 June 1935 (The New International, Aug 1935, pp. 148-151)", link="Leon Trotsky"),
 dict(id="mao-zedong-1940-01", voice="Mao Zedong", role="Chairman of the Chinese Communist Party", c="China", cn="China",
      dom="politics", date="1940-01", era="posthumous", mirror="bourgeois-revolutionary", pol="conflicted", inten=2,
      saw="Concedes Turkey's bourgeois Kemalist dictatorship arose from special conditions, but argues China cannot repeat it and that Kemalist Turkey ended a semi-colony.",
      q="even Kemalist Turkey eventually had to throw herself into the arms of Anglo-French imperialism, becoming more and more of a semi-colony and part of the reactionary imperialist world.",
      art="article", ev="P", med="English text of 'On New Democracy' (Selected Works, vol. 2, FLP) via marxists.org; not the Chinese original",
      cav="Written in Jan 1940, after Atatürk's death (hence era posthumous). It judges Kemalism and 'China's Kemal', not Atatürk personally. The same passage says the 'petty Kemalist dictatorship of the bourgeoisie' emerged 'owing to certain specific conditions (the bourgeoisie's success in repelling Greek aggression and the weakness of the proletariat)'. The vault's person note attributes to Mao a 1936 remark to Edgar Snow ('We are not going to be another Kemal Turkey'); that line was not found in any source read this round and stays unverified.",
      src=["src_mao_new_democracy.txt"],
      urls=["https://www.marxists.org/reference/archive/mao/selected-works/volume-2/mswv2_26.htm"],
      loc="On New Democracy, Selected Works vol. 2 (Jan 1940), passage on the 'bourgeois dictatorship' illusion", link="Mao Zedong"),
 dict(id="reza-shah-1933", voice="Reza Shah Pahlavi", role="Shah of Iran", c="Iran", cn="Iran",
      dom="diplomacy", date="1933", era="contemporary", mirror="nation-forge-template", pol="instrumental", inten=1,
      saw="Tells the Turkish ambassador he very much wants to meet Gazi, and means to visit him with the crown prince in spring 1934.",
      q="Sizin söylediğinize göre Gazi Hazretleri benimle görüşmek istemektedirler. Bende kendileri ile görüşmeyi son derece arzu etmekteyim.",
      art="quote", ev="S", med="Atuk, ÇTTAD XVII/35 (2017), p. 232 ← Hüsrev Gerede, Siyasi Hatıratım 1: İran (Vakit, 1952), p. 265 (ambassador's memoir)",
      cav="Reported in the ambassador's memoir, not a text of the Shah's own; Atuk places it 'early 1933'. Diplomatic courtesy that states a wish to meet rather than a judgement. Translation: 'According to what you tell me, His Excellency Gazi wants to meet me. I too very much wish to meet him.'",
      src=["src_atuk_riza.txt"],
      urls=["https://ataturkilkeleri.deu.edu.tr/wp-content/uploads/2018/03/M.-Volkan-ATUK.pdf"],
      loc="Atuk, 'İran Şahı Rıza Pehlevi'nin Türkiye Ziyareti', ÇTTAD XVII/35, p. 232, n. 57", link="Reza Shah Pahlavi"),
 dict(id="reza-shah-1934-06", voice="Reza Shah Pahlavi", role="Shah of Iran", c="Iran", cn="Iran",
      dom="diplomacy", date="1934-06", era="contemporary", mirror="nation-forge-template", pol="instrumental", inten=1,
      saw="Cables Atatürk as 'dear brother' en route, thanking him for an extraordinarily friendly reception on Turkish soil.",
      q="Türkiye'nin güzel toprağında hakkımda gösterilen fevkalade dostane hüsnü kabulden mütevellit kalbi minnettarlığımı",
      art="telegram", ev="S", med="Kadıoğlu, Çukurova Üniv. SBE Dergisi 34/1 (2025), p. 241 ← Akşam, 14 June 1934 ('Gazi ve Şahinşah Hz. arasında samimi telgraflar')",
      cav="Quoted by Kadıoğlu from Akşam's printed text of the telegram (the article reproduces the clipping as 'Resim 1'); the telegram answers one from Atatürk. Opens 'Muhterem kardeşimden ...' (from my respected brother). Protocol-level courtesy; stored because the speaker is a head of state, intensity 1.",
      src=["src_kadioglu_aksam.txt"],
      urls=["https://dergipark.org.tr/en/download/article-file/3950163"],
      loc="Kadıoğlu 2025, p. 241 ← Akşam 14 Jun 1934", link="Reza Shah Pahlavi"),
]

bad = []
for r in R:
    full = " ".join(bank(s) for s in r["src"])
    if norm(r["q"]) not in full and norm(r["q"]).replace(" ", "") not in full.replace(" ", ""):
        bad.append(r["id"])
if bad:
    sys.exit("quote not found in source bank: %s" % bad)
for r in R:
    assert len(r["saw"].split()) <= 25, (r["id"], len(r["saw"].split()))

with open(os.path.join(STATE, "gazes_leaders.jsonl"), "w", encoding="utf-8") as f:
    for r in R:
        rec = {"id": r["id"], "voice": r["voice"], "voice_type": "person", "role": r["role"], "country": r["c"],
               "country_now": r["cn"], "domain": r["dom"], "date": r["date"], "era": r["era"], "mirror": r["mirror"],
               "polarity": r["pol"], "intensity": r["inten"], "what_they_saw": r["saw"], "quote": r["q"],
               "artifact": r["art"], "evidence": r["ev"], "mediated_by": r["med"], "caveat": r["cav"],
               "node": NODE, "sources": r["urls"]}
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")

with open(os.path.join(STATE, "ledger_leaders.md"), "w", encoding="utf-8") as f:
    f.write("| Claim | Node | Status | Sources | Next step |\n|---|---|---|---|---|\n")
    for r in R:
        nxt = {"mussolini-1928": "Cumhuriyet 1928 Yunus Nadi interview, or Çelebi p. 89, to confirm wording and date",
               "ho-chi-minh-1924-01-01": "L'Humanité 1 Jan 1924 on Gallica (cb327877302) to confirm the French and byline",
               "trotsky-1935-06-10": "none",
               "mao-zedong-1940-01": "Chinese original (Xin minzhu zhuyi lun) and the Snow 1936 line in Red Star Over China",
               "reza-shah-1933": "Gerede, Siyasi Hatıratım I p. 265 (book); Şimşir for letters",
               "reza-shah-1934-06": "Akşam 14 Jun 1934 page 1 image"}[r["id"]]
        f.write("| %s (%s, %s): \"%s\" | %s | verified %s (%s) | %s | %s |\n" % (
            r["voice"], r["role"], r["date"], r["q"][:110].replace("|", "/") + ("..." if len(r["q"]) > 110 else ""),
            NODE, r["ev"], r["loc"], "; ".join(r["urls"][:1]), nxt))

body = ["""
Round 12 looked for the interwar world's best-known political leaders speaking about Kemal in their own words. Six
records survived reading. Most of the big names were dry (see *Dry ends*): the open web gave a few leaders who wrote or
spoke at length about Kemalism (Mao, Ho Chi Minh) and several who only touched him in passing (Trotsky, Reza Shah).
Quotes were checked against the fetched source text before this note was written.

## The pattern

- **Admiration from a rival strongman:** [[Benito Mussolini]], 1928, praised Kemal to a Turkish journalist in the same
  years Rome was trying to win Ankara's goodwill (the tractor gift of November 1929).
- **Communists who weigh the revolution and find it bourgeois:** [[Ho Chi Minh]] in 1924 admires the Turks' victory and
  then says it served only one class; [[Mao Zedong]] in 1940 uses 'Kemalist Turkey' as the example China must *not* follow.
  Both are the Comintern line the vault tracks in [[The Comintern's Verdict on Kemal, 1922–1928]].
- **The exile:** [[Leon Trotsky]], who spent 1929–33 on Büyükada by Ankara's leave ([[MOC — Exiles Turkey Sheltered]]),
  mentions Kemal Pasha's police only to compare them favourably with France's.
- **Courtesies of state:** [[Reza Shah Pahlavi]] before and during his 1934 visit.
""".strip()]

for r in R:
    body.append("\n## %s, %s (%s)\n" % (r["voice"], r["role"], r["date"]))
    body.append("*%s*\n" % r["saw"])
    body.append("> %s\n" % r["q"])
    body.append("%s Location: %s. Evidence %s%s. See [[%s]].\n" % (r["cav"], r["loc"], r["ev"], (" (" + r["med"] + ")") if r["med"] else "", r["link"]))

body.append("""
## Dry ends (round 12)

- **Piłsudski:** Chmielowska, *Balcanica Posnaniensia* 17 (2010) pp. 59–66, describes his Balkan–Turkey security concept; the open page is the abstract only and prints no Piłsudski sentence on Kemal. See [[Józef Piłsudski]].
- **Chiang Kai-shek:** one record already exists (National Day message, 10 Oct 1940). *Modern Asian Studies* (Cambridge, 2026, 'The question of Islam and the Muslim citizen in Republican China') says Chiang kept a book on the Turkish revolution in his car and 'often skimmed' it 'as noted in his diary', citing Wang Qisheng, *Zhongguo tushu pinglun* 4 (2011) p. 26 — a paraphrase, not a quote. See [[Chiang Kai-shek]].
- **Masaryk, Beneš, Hindenburg, Ludendorff, Franco, Salazar:** no open text with a sentence by the leader himself was reached in 11 searches. Hindenburg was already ⌀ in `candidates/books.md`; the Condolence volumes name no Franco or Salazar cable (`candidates/funeral-delegations.md`).
- **Mussolini's Taksim monument telegram of 1928** ('Türkiye Reisicumhuru Gazi Mustafa Kemal Paşa Hazretlerine ...') circulates in blog form only; unsourced to a newspaper, so not stored.

## Sources
- Mehmet Doğar, 'Turkish Fields, Italian Wheels: Mussolini's Gift of a Tractor to Mustafa Kemal in 1929', *Contemporary European History* 35 (2026), cambridge.org.
- Ho Chi Minh, 'The Workers' Movement in Turkey', *L'Humanité*, 1 Jan 1924, marxists.org/reference/archive/ho-chi-minh/works/1924/01/01.htm.
- Leon Trotsky, 'An Open Letter to the French Workers', 10 June 1935, marxists.org/archive/trotsky/1935/06/french.htm; *My Life*, ch. 44, marxists.org.
- Mao Zedong, 'On New Democracy', Jan 1940, *Selected Works*, vol. 2, marxists.org/reference/archive/mao/selected-works/volume-2/mswv2_26.htm.
- M. Volkan Atuk, 'İran Şahı Rıza Pehlevi'nin Türkiye Ziyareti', ÇTTAD XVII/35 (2017), ataturkilkeleri.deu.edu.tr; Ahmet Murat Kadıoğlu, Çukurova Üniv. SBE Dergisi 34/1 (2025), dergipark.org.tr/en/download/article-file/3950163.
""")

note("Events", NODE,
     {"type": "event", "when": "1924–1940",
      "tags": ["event", "verified", "heads-of-state", "leaders", "communist"]},
     "\n".join(body))
print("ok", len(R), "records")
