// Export the dataset for people who want one file instead of 900 YAML files:
//
//   npm run export   → dist/voices.json  every record, as an array; `verification` is reduced to its `verdict`
//                      dist/voices.csv   one row per record with the key fields, the quote and the first source;
//                                        UTF-8 with a byte-order mark so Excel shows Turkish letters correctly
//
// dist/ is not committed. Run `npm run validate` first: files that do not parse are skipped here.
import { mkdirSync, writeFileSync } from 'node:fs';
import { join } from 'node:path';
import { ROOT, loadVoices, rel } from './lib/records.mjs';

const OUT = join(ROOT, 'dist');

const records = [];
let skipped = 0;
for (const { file, data } of loadVoices()) {
  if (!data || typeof data !== 'object' || Array.isArray(data)) { skipped++; console.error(`skipped (does not parse): ${rel(file)}`); continue; }
  const { verification, ...rest } = data;
  records.push({ ...rest, verdict: verification?.verdict ?? null, file: rel(file).split('\\').join('/') });
}
// chronological, then by id ("1938" sorts before "1938-11", which is fine for a spreadsheet)
records.sort((a, b) => String(a.date).localeCompare(String(b.date)) || a.id.localeCompare(b.id));

mkdirSync(OUT, { recursive: true });
writeFileSync(join(OUT, 'voices.json'), JSON.stringify(records, null, 2) + '\n');

// ---- CSV
const COLUMNS = {
  id: (r) => r.id,
  date: (r) => r.date,
  era: (r) => r.era,
  voice: (r) => r.voice,
  voice_type: (r) => r.voice_type,
  role: (r) => r.role,
  country: (r) => r.country,
  country_now: (r) => r.country_now,
  domain: (r) => r.domain,
  polarity: (r) => r.polarity,
  intensity: (r) => r.intensity,
  mirror: (r) => r.mirror,
  artifact: (r) => r.artifact,
  evidence: (r) => r.evidence,
  summary: (r) => r.summary,
  quote: (r) => r.quote?.text,
  quote_language: (r) => r.quote?.language,
  quote_translation: (r) => r.quote?.translation,
  mediated_by: (r) => r.mediated_by,
  caveat: (r) => r.caveat,
  source_url: (r) => r.sources?.find((s) => s?.url)?.url,
  source_citation: (r) => r.sources?.find((s) => s?.citation)?.citation,
  sources: (r) => r.sources?.length ?? 0,
  verdict: (r) => r.verdict,
  file: (r) => r.file,
};

// RFC 4180 quoting. A cell that starts with = + - @ is prefixed with ' so spreadsheets do not run it as a formula.
function cell(v) {
  if (v == null) return '';
  let s = String(v);
  if (/^[=+\-@\t\r]/.test(s)) s = `'${s}`;
  return /[",\r\n]/.test(s) ? `"${s.replace(/"/g, '""')}"` : s;
}
const lines = [Object.keys(COLUMNS).join(','), ...records.map((r) => Object.values(COLUMNS).map((f) => cell(f(r))).join(','))];
writeFileSync(join(OUT, 'voices.csv'), '\uFEFF' + lines.join('\r\n') + '\r\n');

console.log(`dist/voices.json, dist/voices.csv: ${records.length} records${skipped ? `, ${skipped} skipped (run npm run validate)` : ''}`);
