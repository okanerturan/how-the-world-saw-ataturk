# viz/ — the Thread

The exhibition at https://ataturk.fyi: every checked voice in the archive, in the order they spoke, set
as one line of text that spirals out from 1919 at the centre to today at the rim. Each letter is cut heavier where his
photograph is dark, so from a distance the text draws his portrait. Click a voice and it unwinds into a straight line
of type with its sources and its check. Turkish and English (Turkish by browser language, `?lang=en|tr` to choose).
Every voice has its own address, `/#<record id>`, which opens straight on that voice; "share" under an open voice
copies it (or opens the phone's share sheet).

```
npm install          # in the repo root too: the data build uses ../tools/lib
npm run dev          # builds public/gazes.json from ../data, then serves on localhost
npm run build        # → dist/, a static site
```

| | |
|---|---|
| `scripts/build-data.mjs` | `../data/voices` → `public/gazes.json` (only records with a passing `verification`), `../data/translations/tr` → `public/gazes.tr.json` (only fields whose fingerprint still matches) |
| `src/thread.js` | the whole room: signed-distance glyphs on instanced quads (three.js), the portrait tone, unwinding, guided threads, search, light-ups, the source sheet |
| `src/thread-i18n.js`, `i18n/` | interface text in English and Turkish; country names, guided-tour notes in Turkish |
| `src/tour-paths.js` | the guided threads (each stop is a record id; `node scripts/validate-tour.mjs` checks they all exist), and `FUNERAL_LEAD`, the records that open the "10 November 1938" reading (every record with `era: funeral` follows them) |
| `public/photos/` | the three public-domain portraits the text can be engraved from, credits in `photos.json` |
| `public/og.jpg`, `favicon.svg`, `apple-touch-icon.png` | the picture shown when the link is shared, and the tab icon. `index.html` names the picture by its full address (`https://ataturk.fyi/og.jpg`): change it there if the site moves |

Voices whose words the archive has in the reader's language appear as quotes in quotation marks; the others appear as
the archive's summary, set lighter and labelled as a summary, never as their words. Every source sheet links to its
record on GitHub so anyone can propose a correction.

Graphics need WebGL 2. Apps' built-in browsers sometimes switch it off; the page then says so and offers to open in
the phone's browser.
