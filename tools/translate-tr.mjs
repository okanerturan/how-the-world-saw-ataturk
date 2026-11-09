// Keep the Turkish translations up to date: translate every field that is missing or whose English has changed
// since it was translated (its fingerprint no longer matches), and leave everything else — including human
// corrections — alone. Quotes spoken in Turkish are copied verbatim, never translated or modernised.
//
// Maintainers only: needs the `agy` CLI (Antigravity) with access to Gemini 4 Argon.
//   node tools/translate-tr.mjs [--jobs 6] [--batch 10] [--model gemini-4-argon-medium] [--dry]
import { readFileSync, writeFileSync, mkdirSync, existsSync, mkdtempSync, rmSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { tmpdir } from 'node:os';
import { execFile } from 'node:child_process';
import { promisify } from 'node:util';
import { loadVoices, readYaml, translatable, fingerprint, translationPath, yearOf, rel } from './lib/records.mjs';
import { toYaml, clean, TRANSLATION_HEADER } from './lib/yaml-out.mjs';

const run = promisify(execFile);
const arg = (k, d) => { const i = process.argv.indexOf(`--${k}`); return i > 0 ? process.argv[i + 1] : d; };
const JOBS = +arg('jobs', 6), BATCH = +arg('batch', 10), MODEL = arg('model', 'gemini-4-argon-medium'), DRY = process.argv.includes('--dry');
const PROMPT = readFileSync(new URL('translate-tr.prompt.md', import.meta.url), 'utf8');
const FIELDS = ['voice', 'role', 'quote', 'summary', 'caveat', 'mediated_by', 'verification_note', 'verification_method'];
const turkish = (q) => q && ['tr', 'ota'].includes(q.language) && !q.translation;

// what each record still needs
const work = [];
for (const { data: v } of loadVoices()) {
  if (!v) continue;
  const src = translatable(v), file = translationPath('tr', v.id, v.date);
  const t = existsSync(file) ? readYaml(file).data ?? {} : {};
  const need = FIELDS.filter((f) => src[f] != null && (t[f] == null || t.source_fingerprints?.[f] !== fingerprint(src[f])));
  if (need.length) work.push({ v, src, file, t, need });
}
console.log(`${work.length} records need Turkish for ${work.reduce((n, w) => n + w.need.length, 0)} fields`);
if (DRY || !work.length) process.exit(0);

const SCHEMA = { type: 'object', required: ['items'], properties: { items: { type: 'array', items: { type: 'object', required: ['id'],
  properties: Object.fromEntries([['id', { type: 'string' }], ['quote_kind', { type: 'string', enum: ['original-turkish', 'translated', 'none'] }], ...FIELDS.map((f) => [f, { type: ['string', 'null'] }])]) } } } };

async function translate(batch) {
  const items = batch.map((w) => Object.fromEntries([['id', w.v.id], ...w.need.filter((f) => !(f === 'quote' && turkish(w.v.quote))).map((f) => [f, w.src[f]])]));
  const ask = items.filter((x) => Object.keys(x).length > 1);
  let got = {};
  if (ask.length) {
    const wd = mkdtempSync(join(tmpdir(), 'tr-'));
    try {
      writeFileSync(join(wd, 's.json'), JSON.stringify(SCHEMA));
      const { stdout } = await run('agy', ['-p', PROMPT + JSON.stringify(ask, null, 1), '--model', MODEL, '--output-format', 'json',
        '--json-schema', join(wd, 's.json'), '--disable-slash-commands', '--print-timeout', '900s'], { cwd: wd, maxBuffer: 64 << 20, timeout: 1_000_000 });
      const d = JSON.parse(stdout), o = d.structured_output ?? JSON.parse(d.response);
      got = Object.fromEntries(o.items.map((x) => [x.id, x]));
    } finally { rmSync(wd, { recursive: true, force: true }); }
  }
  let n = 0;
  for (const w of batch) {
    const x = got[w.v.id] ?? {}, t = { ...w.t }, fp = { ...(w.t.source_fingerprints ?? {}) };
    for (const f of w.need) {
      let val = x[f];
      if (f === 'quote' && turkish(w.v.quote)) { val = w.v.quote.text; t.quote_kind = 'original-turkish'; }
      else if (f === 'quote' && val != null) t.quote_kind = x.quote_kind === 'original-turkish' && w.v.quote?.is_translation ? 'original-turkish' : 'translated';
      if (val == null) continue;
      t[f] = val; fp[f] = fingerprint(w.src[f]); n++;
    }
    const out = clean({ id: w.v.id, ...Object.fromEntries(FIELDS.flatMap((f) => (f === 'quote' ? [['quote', t.quote], ['quote_kind', t.quote_kind]] : [[f, t[f]]]))),
      translated_by: t.translated_by ?? `machine: ${MODEL}`, reviewed_by: t.reviewed_by, source_fingerprints: fp });
    mkdirSync(dirname(w.file), { recursive: true });
    writeFileSync(w.file, toYaml(out, TRANSLATION_HEADER('tr', `data/voices/${yearOf(w.v.date)}/${w.v.id}.yaml`)));
  }
  return n;
}

const batches = [];
for (let i = 0; i < work.length; i += BATCH) batches.push(work.slice(i, i + BATCH));
let done = 0, fields = 0;
const queue = [...batches];
await Promise.all(Array.from({ length: JOBS }, async () => {
  while (queue.length) {
    const b = queue.shift();
    try { fields += await translate(b); } catch (e) { console.log(`  batch failed (${b[0].v.id}…): ${e.message.split('\n')[0]}`); }
    console.log(`  ${++done}/${batches.length} batches, ${fields} fields`);
  }
}));
console.log(`done: ${fields} fields translated; rerun to retry anything missing (${rel(translationPath('tr', 'x', '2000')).replace(/2000\/x\.yaml$/, '')})`);
