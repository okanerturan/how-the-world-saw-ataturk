// Give every source link an archived copy, so the archive survives link rot.
// For each source with a `url` and no `archived`, ask the Wayback Machine for an existing snapshot and write it into
// the record. With --save, ask the Wayback Machine to archive pages that have no snapshot yet (slow: about one a minute).
// Only adds `archived:` lines; nothing else in the files changes.
//
//   node tools/archive-sources.mjs [--save] [--limit N] [--cache file.json]
import { readFileSync, writeFileSync, existsSync } from 'node:fs';
import YAML from 'yaml';
import { loadVoices, rel } from './lib/records.mjs';

const arg = (k, d) => { const i = process.argv.indexOf(`--${k}`); return i > 0 ? process.argv[i + 1] : d; };
const SAVE = process.argv.includes('--save'), LIMIT = +arg('limit', 0), CACHE = arg('cache', null);
const UA = { 'User-Agent': 'how-the-world-saw-ataturk source archiver (+https://github.com/okanerturan/how-the-world-saw-ataturk)' };
const cache = CACHE && existsSync(CACHE) ? JSON.parse(readFileSync(CACHE, 'utf8')) : {};
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

async function snapshot(url) {
  if (url in cache) return cache[url]?.url ?? null;
  try {
    const r = await fetch(`https://archive.org/wayback/available?url=${encodeURIComponent(url)}`, { headers: UA, signal: AbortSignal.timeout(30000) });
    const s = (await r.json()).archived_snapshots?.closest;
    return s?.available ? s.url.replace(/^http:/, 'https:') : null;
  } catch { return null; }
}
async function save(url) {
  try {
    const r = await fetch(`https://web.archive.org/save/${url}`, { headers: UA, redirect: 'follow', signal: AbortSignal.timeout(180000) });
    const m = (r.url + (r.headers.get('content-location') ?? '')).match(/\/web\/(\d{14})\//);
    return m ? `https://web.archive.org/web/${m[1]}/${url}` : null;
  } catch { return null; }
}

let files = 0, added = 0, missing = 0, looked = 0;
for (const { file, text, doc } of loadVoices()) {
  if (doc.errors.length) continue;
  const sources = doc.get('sources');
  if (!YAML.isSeq(sources)) continue;
  let changed = false;
  for (const item of sources.items) {
    if (!YAML.isMap(item) || !item.get('url') || item.get('archived')) continue;
    if (LIMIT && looked >= LIMIT) break;
    looked++;
    const url = String(item.get('url'));
    let a = await snapshot(url);
    if (!a && SAVE) { a = await save(url); await sleep(10000); }
    if (a) { item.set('archived', a); changed = true; added++; } else missing++;
  }
  if (changed) {
    const header = text.match(/^(#.*\n)+/)?.[0] ?? '';
    writeFileSync(file, header + doc.toString({ lineWidth: 110, minContentWidth: 40, indentSeq: true }).replace(/^(#.*\n)+/, ''));
    files++;
    console.log(`  ${rel(file)}`);
  }
}
console.log(`${added} archived links added in ${files} files; ${missing} sources still without a copy${SAVE ? '' : ' (run with --save to create them)'}`);
