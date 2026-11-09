# -*- coding: utf-8 -*-
# Census round 20 (Nov 2026) — Soviet voices in Russian open texts: Aralov memoir (1960), Pilnyak (1926).
# Banks in tools/.state/round20/ (aralov.txt = archive.org djvu text, pilnyak.txt = ru.wikisource raw). Script refuses to run if a quote is not in its bank.
import json, os, re, sys, unicodedata, urllib.parse
from _lib import note, person

HERE = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(HERE, "tools", ".state", "round20")
NODE = "Soviet Pens on Mustafa Kemal — Aralov and Pilnyak"


def norm(s):
    s = unicodedata.normalize("NFKC", s).replace("ё", "е")
    s = re.sub(r"¬\s*", "", s)          # djvu line-end hyphens
    s = re.sub(r"[-–—]\s*\n\s*", "", s) if False else s
    s = re.sub(r"\s+", " ", s)
    return s.strip().lower()


def bank(f):
    return norm(open(os.path.join(STATE, f), encoding="utf-8").read())


AR = "https://archive.org/details/vospominaniia_sovetskogo_diplomata_1922_1923"
PI = "https://ru.wikisource.org/wiki/" + urllib.parse.quote("Повесть_о_ключах_и_глине_(Пильняк)", safe="/_():")

R = [
 dict(id="aralov-1960", voice="Semyon Aralov", role="First Soviet ambassador to Ankara (1922-23), memoirist",
      c="Soviet Union", cn="Russia", dom="diplomacy", date="1960", era="posthumous", mirror="bourgeois-revolutionary",
      pol="conflicted", inten=3, art="memoir", ev="P", f="aralov.txt",
      saw="Portrays the Ghazi as a lyrical man hardened by love of country, yet judges that only the bourgeoisie gained from his revolution.",
      q="Гази обладал тонкой, лирической натурой. Любовь к родине, народу заставила его выработать в себе суровый, стойкий характер, необходимый для беспощадной борьбы с врагами Турции.",
      tr="The Ghazi had a delicate, lyrical nature. Love of country and people made him forge in himself a stern, steadfast character, needed for the merciless struggle against Turkey's enemies.",
      q2="Но надежды эти не оправдались. Выиграла от национальной революции и военных побед освободительной армии только буржуазия.",
      tr2="But those hopes were not fulfilled. Only the bourgeoisie gained from the national revolution and the liberation army's victories.",
      src=AR,
      cav="S. I. Aralov, Воспоминания советского дипломата. 1922-1923 (Moscow: Institute of International Relations, 1960), p. 215 (the lyrical-nature portrait, after Kemal asks his wife Latife to play a Tchaikovsky romance at the farewell dinner). The same book, p. 211, in the section on Kemal as leader of the new Turkey: 'Но надежды эти не оправдались. Выиграла от национальной революции и военных побед освободительной армии только буржуазия' (translation: 'But those hopes were not fulfilled. Only the bourgeoisie gained from the national revolution and the liberation army's victories') and that Kemal 'не был последователен в борьбе с феодалами'. Read in the open archive.org scan (djvu text, page numbers from the scan). Events 1922-23, written and published under 1960 Soviet historiography; the book's own preface-level frame is class analysis. Aralov's verdict on Kemal's tactical genius and on the communists' repression is not in the quoted passages."),
 dict(id="pilnyak-1926", voice="Boris Pilnyak", role="Soviet novelist (the 'Tale of the Keys and the Clay', Aegean-Levant travel prose)",
      c="Soviet Union", cn="Russia", dom="letters", date="1926", era="contemporary", mirror=None,
      pol="hostile", inten=1, art="article", ev="S", f="pilnyak.txt",
      saw="A narrator's aside lists Mustafa Kemal Pasha among the region's atrocities: after an ultimatum to the Greeks he shelled the ships and burned Smyrna.",
      q="точно так же, как в тысяча девятьсот двадцать первом году Мустафа Кемаль-паша, обложив тяжелой артиллерией Смирну, предложил грекам в двадцать четыре часа уйти из Смирны",
      tr="just as in 1921 Mustafa Kemal Pasha, having surrounded Smyrna with heavy artillery, offered the Greeks twenty-four hours to leave Smyrna",
      q2=None, tr2=None, src=PI,
      cav="Narrator's aside in fiction ('Повесть о ключах и глине'), not an essay; dated 1921 in the text (the Smyrna fire was September 1922, so the date is Pilnyak's error). The sentence goes on to say Kemal's artillery wrecked the ships in the roads, then 'razed and burned the city, throwing into the sea up to two hundred thousand Greeks'; those figures are Pilnyak's, not the vault's. Sensitive thread (Smyrna 1922): recorded as the narrator's framing, not as established fact. Elsewhere in the same text a character (the communist Aleksandrov) says that 'Mustafa Kemal Pasha and his revolution' are tied to the 'night of Iran, Asia', a persona's speech with no clear verdict. Year of composition taken from the Wikisource metadata (1926); text reproduced from the 1990 Pravda edition of Pilnyak's 'Povest nepogashennoi luny'."),
]
bad = [r["id"] for r in R for k in ("q", "q2") if r[k] and norm(r[k]) not in bank(r["f"])]
if bad:
    sys.exit("quote not found in source bank: %s" % bad)
for r in R:
    print(r["id"], len(r["saw"].split()))

with open(os.path.join(STATE, "gazes_soviet.jsonl"), "w", encoding="utf-8") as f:
    for r in R:
        rec = {"id": r["id"], "voice": r["voice"], "voice_type": "person", "role": r["role"],
               "country": r["c"], "country_now": r["cn"], "domain": r["dom"], "date": r["date"], "era": r["era"],
               "mirror": r["mirror"], "polarity": r["pol"], "intensity": r["inten"], "what_they_saw": r["saw"],
               "quote": r["q"] + " [translation: " + r["tr"] + "]", "artifact": r["art"], "evidence": r["ev"],
               "mediated_by": None, "caveat": r["cav"], "node": NODE, "sources": [r["src"]]}
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")

with open(os.path.join(STATE, "ledger_soviet.md"), "w", encoding="utf-8") as f:
    f.write("| Claim | Node | Status | Sources | Next step |\n|---|---|---|---|---|\n")
    f.write("| Aralov (1960 memoir, p. 215; also p. 211): lyrical nature / only the bourgeoisie gained | %s | verified P (archive.org open scan, read) | %s | Print-page check of pp. 211 and 215 against the 1960 edition |\n" % (NODE, AR))
    f.write("| Pilnyak (1926, 'Повесть о ключах и глине'): Smyrna aside | %s | verified S (ru.wikisource text, read; narrator aside, year error in source) | %s | First publication (journal year) and a print check |\n" % (NODE, PI))

person("Boris Pilnyak", role="Soviet novelist", nat="Soviet", life="1894–1938", stance="hostile (1926 aside)",
       tags=["writer", "russia", "verified", "russian-primary"],
       body="""Russian novelist and travel writer, shot in 1938. In his Aegean and Levant travel prose 'Повесть о ключах и глине' (1926) a narrator's parenthesis lists Mustafa Kemal Pasha's shelling and burning of Smyrna beside the Dardanelles dead and the Janissary massacres; the year is misdated 1921. Fiction, a narrator's framing, on a sensitive thread. See [[%s]].

## Sources
- %s
""" % (NODE, PI))

body = """Two Soviet-era Russian texts read in full-text open copies. **Semyon Aralov**, the first Soviet ambassador in Ankara, remembers Kemal in his 1960 memoir (see his note [[Semyon Aralov]]): a man of 'delicate, lyrical nature' hardened by love of country, whose revolution, Aralov concludes in Marxist terms, helped only the bourgeoisie. **Boris Pilnyak**, the novelist, makes Kemal a name in a catalogue of the region's massacres, in a narrator's aside (sensitive thread; the framing is Pilnyak's).

## Semyon Aralov, *Воспоминания советского дипломата* (1960), pp. 211 and 215

> %s
> (translation: %s)

Second passage, p. 211: *%s* (translation: %s)

See [[Semyon Aralov]], [[Mikhail Frunze]], [[Kliment Voroshilov]].

## Boris Pilnyak, *Повесть о ключах и глине* (1926)

> %s
> (translation: %s)

Narrator's aside; the text misdates the Smyrna events to 1921. See [[Boris Pilnyak]].

## Sources
- Aralov: %s
- Pilnyak: %s
""" % (R[0]["q"], R[0]["tr"], R[0]["q2"], R[0]["tr2"], R[1]["q"], R[1]["tr"], AR, PI)
note("Events", NODE, {"type": "event", "when": "1926–1960", "tags": ["event", "verified", "russia", "russian-primary"]}, body)
print("ok")
