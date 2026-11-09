# -*- coding: utf-8 -*-
# Round 8 — Hansard second pass (variant spellings, unread 1922-23 debates) + Canada's Commons, Feb 1923.
# Records: scratchpad/gazes8_hansard2.jsonl. Sources: Hansard Search API (hansard-api.parliament.uk);
# Canadian Parliamentary Historical Resources (parl.canadiana.ca), page images read directly.
from _lib import note

H = "https://hansard.parliament.uk"
C = "https://parl.canadiana.ca/view/oop.debates_HOC1402_01"

E = [
("Kemal in the Commons, Variant Spellings, 1920–1922", "18 February 1920 – 4 August 1922", """
**The first sweep missed the OCR.** [[Parliament Meets Kemal, February–March 1920]] and [[Parliament on Kemal and the Greeks, 1921–1922]]
were built from searches for *Kemal*, *Kemalist*, *Mustapha Kemal*. Hansard's digitised text spells him *Kamil*, *Kemil*, *Kcmil*,
*Kliamil* and *Kernel* (the OCR of "Kemal"), and a second API sweep for those forms (29 Oct 2026) finds ten more contributions that
state a view of him. Spelling is quoted as printed.

**February–March 1920, the massacre months.**
- *Ormsby-Gore* (18 Feb, a question a week before his better-known one of 11 March): "the massacres are being carried out by Mustapha Kamil,
  a Nationalist leader, and his troops, who do not acknowledge the authority of the Sultan."
- *Sir Samuel Hoare* (26 Feb) lumps him with the Committee: "what is the good of pointing your guns at the Sultan when Enver and Mustapha Kliamil are at Sivas?"
  *Earl Winterton* (same debate) sees only a threat: "I do not know who is going to prevent Mustapha Pasha from attacking Constantinople unless there are fortifications there."
- *Lord Robert Cecil* (11 Mar) asks whether it is "not the fact that Mustapha Kemal Pasha has been in constant and close communication with the Turkish Ministry of War."
  *Lieut.-Commander Kenworthy*, the same day, would bomb him: "military camps under the command of Mustapha Kemil which could have been raided by our new long-range aircraft."
- *Major-General Seely* (18 Mar), on air power at sea: "Mustapha Kcmil whom we now know, from the speech of the Foreign Secretary in the House of Lords, to
  have been the source of all the trouble, and probably responsible for most of the massacres."

**Peace partner, 1921–1922.** *Lord Newton* (Lords, 10 Nov 1921) expects "some arrangement with Kemal Pasha" and wants war criminals handed back as the price.
In May–June 1922 the Turcophile bench uses him as the interlocutor: *Sir Charles Townshend* (25 May) cites Kemal's note readiness to negotiate at Ismid and asks the Government to
press Greece; *Aubrey Herbert* ([[Aubrey Herbert]], 22 Jun) asks whether the Government will discuss "terms of settlement immediately with Mustapha Kemal Pasha at Ismid."
(Townshend's 30 May speech is in [[Parliament on Kemal and the Greeks, 1921–1922]].)

**4 August 1922, the turn.** The same day [[David Lloyd George]] concedes that he "may be a great general and a great patriot," Kenworthy tells the House that the Smyrna
inquiry report, "suppressed," "roused all Turkey" and that "the gentleman who is referred to occasionally by Members of this Government as some rebel general is the great
national hero of Turkey, and is looked upon as the wielder of the Sword of the Faithful." Kenworthy had wanted his camps bombed in March 1920; his change of stance is the voice-shift
of the set (see [[Chanak Crisis]]).

**Not here.** The Lords address debate of 23 Nov 1922 and Commons 24 Nov 1922 (read in full): no one names Kemal. Wester Wemyss calls "these Angora Turks" a "rabble" dependent on Moscow
and Lamington defends the Turkish people against Newton; Curzon's 13 Feb 1923 speech names only "Angora" as a place; Mosley, Pringle and McNeill in March 1923 speak of the Angora negotiations,
not of him. These are views of a movement and a capital, so none is recorded. The 22 Dec 1920 Commons sitting that is the source of Lloyd George's "mutinous general" is missing
from both the Hansard Search API and the historic-hansard text; the words survive in T. P. O'Connor's reading of the Official Report (8 Feb 1922, citing Vol. 136 cols 1895, 1897), already in the existing card.

Net: ten records (six hostile, four instrumental, none admiring until Kenworthy's August 1922 speech, which is instrumental). See [[Treaty of Lausanne]] for the settlement all of them were arguing toward.

## Sources
- Hansard Search API (tier P, full contribution text; page URLs follow the canonical form, the site returns 403 to non-browser clients):
  [Ormsby-Gore 18 Feb 1920]({H}/Commons/1920-02-18/debates/44d28adf-66c9-461d-b232-9b8e2a2d34fc/TurkishRuleInConstanixople) (`35a35b5f-ae71-4c07-a0e2-4a83af862081`) ·
  [Hoare `556b32d6-eff0-460e-bcd1-62051fb8e62f`, Winterton `07e5c8d9-2a45-4b21-8d4f-c61c1380caae`, 26 Feb 1920]({H}/Commons/1920-02-26/debates/7dd9498b-3e40-4d22-a1d1-b06729365496/TurksAndConstantinople) ·
  [Cecil `65984c46-cd5c-42d9-bc91-faba0c521ce4`, 11 Mar 1920]({H}/Commons/1920-03-11/debates/9ee65e95-7cee-44ac-bedf-15196dd1bb46/CiliciaMassacres) ·
  [Kenworthy `bef1cafc-c44a-47da-8902-3bab8c96862d`, 11 Mar 1920]({H}/Commons/1920-03-11/debates/0fdaa9ee-e2bf-44b3-ad8b-d3857e53b1bc/MajorTryonSStatement) ·
  [Seely `e8e19b43-a3dc-4510-b1d8-ecdba3f765d8`, 18 Mar 1920]({H}/Commons/1920-03-18/debates/e4618aab-4686-4322-8e6c-cf4d0c4f7779/NavyEstimates192021) ·
  [Newton `09dafedd-b758-411d-9415-3c35ebf9aeea`, Lords 10 Nov 1921]({H}/Lords/1921-11-10/debates/1f5b38ce-1037-4903-9100-91a3c9928297/TurkishWarCriminals) ·
  [Townshend `d3bec44f-037a-45cc-b599-61bbccf9b88f`, 25 May 1922]({H}/Commons/1922-05-25/debates/5ef60763-8eed-44c1-84a1-a6830dc2b1f3/GreeceAndTurkey) ·
  [Herbert `9a174742-2b21-4d98-9310-2d2f648282e1`, 22 Jun 1922]({H}/Commons/1922-06-22/debates/b43dde77-8b22-4aff-81aa-7ce81ca0ae76/NearEast) ·
  [Kenworthy `70a567d0-f705-459d-80b8-3f899a8f27a3`, 4 Aug 1922]({H}/Commons/1922-08-04/debates/e8c2fe25-f736-4f36-bd19-4375874f4b5b/NearEast)
- Negative reads: Lords 23 Nov 1922 (Wester Wemyss `ddcb321c-aba6-429f-a017-ff9614eb7f58`, Lamington `4f9d5eee-4608-4076-acc1-a096be1a072c`); Lords 13 Feb 1923 (Curzon `bc6e9aba-77ae-4cfd-af96-fd54ac13ba7a`); Commons 7 Mar 1923 (Pringle `ec74d062-05b7-4de7-a725-75f8c2c69e83`).
"""),

("Canada's Commons on Chanak, February 1923", "1 February 1923", """
**The House that was told, not asked.** [[Canada Says Not Yet at Chanak, September 1922]] follows the crisis through memoirs and press. The Commons itself met only in the new
session. On 1 February 1923, in the Address debate, Mackenzie King read the House the substance of the British despatch of 15 September 1922
and handed the text to Meighen, as Leader of the Opposition, to read. The Official Report (House of Commons Debates, 14th Parliament, 2nd Session, vol. 1, pp. 30–31)
is the only place in the Canadian record where Kemal is named in this debate:

- The despatch "was to the effect that the British cabinet had decided to resist Turkish aggression upon Europe, and to make exertions to prevent the Allies being
  driven out of Constantinople by Mustapha Kemal," and that "it was not likely that the forces of Mustapha Kemal would attack if a firm front were shown by any large
  number of powers acting together" (p. 31, col. 1). These are King's report of London's words, so the record is a witness record, not King's own opinion.
- King's own point is about procedure: the press had the story before the Government, and the "vital part of the despatch" was the question whether Canada "wished to associate
  themselves with the action the British government were taking."

**What was searched.** The volumes of the 14th Parliament (1922, 1923, 1924 sessions) were searched page-by-page for *Chanak, Kemal, Mustapha, Turks, Angora, Turkey* through
the Library of Parliament's full-text search; apart from the index pages (which list the name), Kemal is named on those two pages only. Meighen's reply and the later Chanak
passages talk of Turkey, the Straits and imperial consultation, not of him, and the 1924 Lausanne debate does not name him. That silence is the finding: the Dominion Parliament argued
about its own autonomy, and Kemal is the occasion. Compare [[Chanak Crisis]], [[Kemal in the Commons, Variant Spellings, 1920–1922]], and [[New Zealand Leaders on Kemal at Chanak, September 1922]].

**Australia.** Not read. The Parliament's Hansard sites (ParlInfo, historichansard.net) block non-browser clients behind a WAF/CAPTCHA; nothing is claimed here (see the candidates file).

## Sources
- House of Commons Debates (Canada), 14th Parliament, 2nd Session, vol. 1, 1 Feb 1923, "The Address — Mr. Mackenzie King," pp. 30–31 (page images read): [seq. 44]({C}/44) · [seq. 45]({C}/45). Library of Parliament / Canadiana, tier P.
"""),
]

for name, when, body in E:
    body = body.replace("{H}", H).replace("{C}", C)
    note("Events", name, {"type": "event", "when": when, "tags": ["event", "verified"]}, body)
print(len(E), "notes written")
