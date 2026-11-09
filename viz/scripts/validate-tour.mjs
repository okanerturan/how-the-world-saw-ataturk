// Check the guided threads: every stop is a record that exists, has passed its check, and has a note.
import { PROLOGUE, PATHS, FINALE, FUNERAL_LEAD } from '../src/tour-paths.js';
import { loadVoices } from '../../tools/lib/records.mjs';
const gazes = new Map(loadVoices().filter((x) => x.data).map((x) => [x.data.id, x.data]));
const verdict = new Map([...gazes].filter(([, r]) => r.verification?.verdict).map(([id, r]) => [id, r.verification.verdict]));
const BAD = new Set(['not-found', 'contradicted']);
const errors = []; const counts = {}; const all = [];
const pathIds = new Set(PATHS.map(p => p.id));
function check(label, sec, extra) {
  if (!sec.title || !sec.line || !Array.isArray(sec.stops)) errors.push(`${label}: missing title/line/stops`);
  const seen = new Set();
  for (const s of sec.stops) {
    if (!gazes.has(s.id)) errors.push(`${label}: id not in gazes: ${s.id}`);
    const v = verdict.get(s.id);
    if (!v) errors.push(`${label}: no check line: ${s.id}`);
    else if (BAD.has(v)) errors.push(`${label}: ${s.id} verdict ${v}`);
    if (seen.has(s.id)) errors.push(`${label}: duplicate stop ${s.id}`);
    seen.add(s.id); all.push(s.id);
    if (!s.note || s.note.length < 40) errors.push(`${label}: short/missing note ${s.id}`);
    counts[v] = (counts[v] || 0) + 1;
  }
  if (extra) extra();
}
check('PROLOGUE', PROLOGUE);
for (const p of PATHS) check(p.id, p, () => {
  if (!/^[a-z0-9]+(-[a-z0-9]+)*$/.test(p.id)) errors.push(`${p.id}: id not kebab`);
  if (!p.question) errors.push(`${p.id}: no question`);
  if (p.stops.length < 8 || p.stops.length > 12) errors.push(`${p.id}: ${p.stops.length} stops`);
  if (!Array.isArray(p.next) || p.next.length < 2 || p.next.length > 3) errors.push(`${p.id}: next count`);
  for (const n of p.next || []) if (!pathIds.has(n) || n === p.id) errors.push(`${p.id}: bad next ${n}`);
});
check('FINALE', FINALE);
// the opening of the 10 November 1938 reading: checked records of the funeral period, none twice
for (const id of FUNERAL_LEAD) {
  const r = gazes.get(id), v = verdict.get(id);
  if (!r) errors.push(`FUNERAL_LEAD: id not in gazes: ${id}`);
  else if (r.era !== 'funeral') errors.push(`FUNERAL_LEAD: ${id} is not of the funeral period (era ${r.era})`);
  if (r && (!v || BAD.has(v))) errors.push(`FUNERAL_LEAD: ${id} has no passing check`);
}
if (new Set(FUNERAL_LEAD).size !== FUNERAL_LEAD.length) errors.push('FUNERAL_LEAD: duplicate id');
const dupAcross = all.filter((x, i) => all.indexOf(x) !== i);
const voices = new Set(all.map(i => gazes.get(i)?.voice));
console.log('stops:', all.length, '| distinct voices:', voices.size, '| PATHS:', PATHS.length);
console.log('per section:', [['prologue', PROLOGUE.stops.length], ...PATHS.map(p => [p.id, p.stops.length]), ['finale', FINALE.stops.length]].map(x => x.join('=')).join(', '));
console.log('verdicts:', JSON.stringify(counts));
console.log('duplicates across sections:', dupAcross.length ? dupAcross : 'none');
console.log(errors.length ? 'ERRORS:\n' + errors.join('\n') : 'OK: all checks passed');
if (errors.length) process.exit(1);
process.exit(errors.length ? 1 : 0);
