// Build the exhibition's data from the archive (../data): public/gazes.json (English) and public/gazes.tr.json (Turkish).
// A record appears only once it has been checked: it needs a `verification` whose verdict is not not-found/contradicted.
// Turkish fields are used only while their fingerprint still matches the English they were translated from.
import { writeFileSync, mkdirSync, readFileSync, existsSync } from 'node:fs';
import { loadVoices, loadTranslations, translatable, fingerprint, quoteString, rel } from '../../tools/lib/records.mjs';

const out = new URL('../public/', import.meta.url);
const SHOW = new Set(['confirmed', 'partial', 'paraphrase-ok', 'secondary-only', 'unreachable']);

// a record with no source links falls back to the lines of its vault note's "## Sources" that name the voice
const vault = new URL('../../vault/', import.meta.url);
const notes = {};
function noteSources(node, v) {
  if (!node) return [];
  if (!(node in notes)) {
    let text = '';
    for (const sub of ['', 'People/', 'Events/', 'Concepts/']) {
      const f = new URL(`${sub}${node}.md`, vault);
      if (existsSync(f)) { text = readFileSync(f, 'utf8'); break; }
    }
    notes[node] = (text.split(/^## Sources\s*$/m)[1]?.split(/^## /m)[0] ?? '').split('\n').filter((l) => l.startsWith('- ')).map((l) => l.slice(2));
  }
  const words = `${v.voice} ${v.mediated_by ?? ''}`.split(/[^\p{L}]+/u).filter((w) => w.length >= 6);
  const res = [];
  for (const l of notes[node].filter((l) => words.some((w) => new RegExp(`(?<!\\p{L})${w}(?!\\p{L})`, 'u').test(l)))) {
    const label = l.split(/`| — /)[0].trim().replace(/[,\s]+$/, '');
    for (const [u] of l.matchAll(/https?:\/\/[^\s)>\]]+/g)) res.push({ url: u, label });
    for (const m of l.matchAll(/ddd:(\d+):mpeg21:(a\d{4})/g)) res.push({ url: `https://resolver.kb.nl/resolve?urn=ddd:${m[1]}:mpeg21:${m[2]}`, label });
  }
  return res;
}

const gazes = [], hidden = { unverified: 0, failed: 0 };
for (const { file, data: v } of loadVoices()) {
  if (!v) continue;                                        // a broken file: the validator reports it
  const verdict = v.verification?.verdict;
  if (!verdict) { hidden.unverified++; continue; }
  if (!SHOW.has(verdict)) { hidden.failed++; continue; }
  const q = v.quote ?? null;
  let sources = (v.sources ?? []).map((s) => ({ url: s.url ?? null, label: s.label ?? s.citation ?? null, archived: s.archived ?? null, page: s.page ?? null }));
  let fromNote = false;
  if (!sources.some((s) => s.url)) { const f = noteSources(v.node, v); if (f.length) { sources = [...sources, ...f]; fromNote = true; } }
  gazes.push({
    id: v.id, path: rel(file), voice: v.voice, voice_type: v.voice_type, role: v.role, country: v.country, country_now: v.country_now,
    domain: v.domain, date: String(v.date), era: v.era ?? null, mirror: v.mirror ?? null, polarity: v.polarity, intensity: v.intensity ?? null,
    what_they_saw: v.summary, artifact: v.artifact ?? null, evidence: v.evidence ?? null, mediated_by: v.mediated_by ?? null,
    caveat: v.caveat ?? null, node: v.node ?? null, sources, sources_from_note: fromNote,
    quote: quoteString(q), quote_text: q?.text ?? null, quote_lang: q?.language ?? null, quote_translation: q?.translation ?? null,
    quote_is_translation: !!q?.is_translation, quote_note: q?.note ?? null,
    check: verdict,
    check_detail: { against: v.verification.checked_against ?? null, method: v.verification.method ?? null, issue: v.verification.note ?? null, on: v.verification.checked_on ?? null, quote_found: v.verification.quote_found ?? null },
  });
}
mkdirSync(out, { recursive: true });
writeFileSync(new URL('gazes.json', out), JSON.stringify({ built: new Date().toISOString(), gazes }));
console.log(`gazes.json: ${gazes.length} records shown; ${hidden.unverified} waiting for a check, ${hidden.failed} not shown (not-found/contradicted)`);

// Turkish, field by field
const byId = new Map(loadVoices().filter((x) => x.data).map((x) => [x.data.id, x.data]));
const tr = {}; let stale = 0, files = 0;
const MAP = { voice: 'voice', role: 'role', quote: 'quote', summary: 'what_they_saw', caveat: 'caveat', mediated_by: 'mediated_by', verification_note: 'check_issue', verification_method: 'check_method' };
for (const { file, data: t } of loadTranslations('tr')) {
  const v = t && byId.get(t.id);
  if (!v) continue;
  files++;
  const src = translatable(v), o = { path: rel(file) };
  for (const [k, outKey] of Object.entries(MAP)) {
    if (t[k] == null) continue;
    if (t.source_fingerprints?.[k] === fingerprint(src[k])) o[outKey] = t[k]; else stale++;
  }
  if (o.quote != null) o.quote_kind = t.quote_kind ?? 'translated';
  tr[t.id] = o;
}
writeFileSync(new URL('gazes.tr.json', out), JSON.stringify(tr));
console.log(`gazes.tr.json: ${files} Turkish files, ${stale} stale fields shown in English until retranslated`);
