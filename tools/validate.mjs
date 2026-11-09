// Validate the dataset: every record in data/voices/<YYYY>/<id>.yaml and every translation in
// data/translations/<lang>/<YYYY>/<id>.yaml.
//
//   npm run validate                      check everything
//   npm run validate -- <path> [...]      check everything, but report only on these files or folders
//   npm run validate -- --quiet           report errors only
//
// Exits 1 when there is at least one error; warnings and notices never fail the run. Under GitHub Actions
// (GITHUB_ACTIONS set) it also prints workflow commands, so problems show up as annotations on the pull request,
// and on a pull request (GITHUB_BASE_REF set) it flags changes to a record's `verification` block for review.
import { readFileSync, readdirSync, existsSync, appendFileSync } from 'node:fs';
import { join, relative, basename, dirname, resolve, sep } from 'node:path';
import { execFileSync } from 'node:child_process';
import YAML from 'yaml';
import Ajv2020 from 'ajv/dist/2020.js';
import addFormats from 'ajv-formats';
import { ROOT, VOICES, TRANSLATIONS, walk, rel, yearOf, eraOf, translatable, fingerprint } from './lib/records.mjs';

const SUMMARY_WARN = 25;  // words: an editorial guideline, so a longer summary warns but never fails
const GITHUB = !!process.env.GITHUB_ACTIONS;

const args = process.argv.slice(2);
const QUIET = args.includes('--quiet');
// npm runs scripts from the package root; INIT_CWD is where the command was typed
const only = args.filter((a) => !a.startsWith('--')).map((a) => posix(relative(ROOT, resolve(process.env.INIT_CWD ?? process.cwd(), a))));

// ---------------------------------------------------------------------------------------------------------------
// schemas

const readJson = (p) => JSON.parse(readFileSync(join(ROOT, p), 'utf8'));
const voiceSchema = readJson('data/schema/voice.schema.json');
const translationSchema = readJson('data/schema/translation.schema.json');
const ajv = new Ajv2020({ allErrors: true, verbose: true, strict: true, strictRequired: false, allowUnionTypes: true });
addFormats(ajv);
const checkVoice = ajv.compile(voiceSchema);
const checkTranslation = ajv.compile(translationSchema);
const DATE_RE = new RegExp(voiceSchema.properties.date.pattern);

// ---------------------------------------------------------------------------------------------------------------
// problems: collected first, printed grouped by file at the end

const problems = []; // { path, line, col, level: 'error'|'warning'|'notice', message }

// `at` is a path into the YAML document (['sources', 0, 'url']); the problem is placed on the deepest key or list
// item of that path that exists in the file. It may also be a ready { line, col }.
function report(entry, level, message, at = [], extra = {}) {
  const pos = Array.isArray(at) ? locate(entry, at) : at;
  problems.push({ path: entry.path, line: pos.line, col: pos.col, level, message, ...extra });
}

function locate(entry, path) {
  const { doc, lineCounter } = entry;
  let node = doc?.contents;
  let offset = node?.range?.[0] ?? 0;
  for (const seg of path) {
    if (YAML.isMap(node)) {
      const pair = node.items.find((p) => String(YAML.isScalar(p.key) ? p.key.value : p.key) === String(seg));
      if (!pair) break;
      offset = pair.key?.range?.[0] ?? offset;
      node = pair.value;
    } else if (YAML.isSeq(node)) {
      const item = node.items[Number(seg)];
      if (!item) break;
      offset = item.range?.[0] ?? offset;
      node = item;
    } else break;
  }
  return lineCounter ? lineCounter.linePos(offset) : { line: 1, col: 1 };
}

// the value exactly as written in the file, e.g. 000123 rather than the number 123 it parses to
function sourceText(entry, path) {
  const node = entry.doc?.getIn(path, true);
  return YAML.isScalar(node) && node.range ? entry.text.slice(node.range[0], node.range[1]).trim() : null;
}

function posix(p) { return p.split(sep).join('/'); }

function load(file) {
  const text = readFileSync(file, 'utf8');
  const lineCounter = new YAML.LineCounter();
  const doc = YAML.parseDocument(text, { prettyErrors: true, lineCounter });
  return { file, path: posix(rel(file)), text, doc, lineCounter, data: doc.errors.length ? null : doc.toJS() };
}

const isObject = (x) => x !== null && typeof x === 'object' && !Array.isArray(x);
const fieldName = (segs) => segs.reduce((s, p) => (/^\d+$/.test(String(p)) ? `${s}[${p}]` : s ? `${s}.${p}` : String(p)), '');
const words = (s) => String(s).split(/\s+/).filter((w) => /[\p{L}\p{N}]/u.test(w)).length;

// template text left in place, e.g. summary: <summary in English / İngilizce özet>
function placeholders(entry, value, path = []) {
  if (typeof value === 'string' && /^\s*<[^<>]+>\s*$/.test(value)) {
    report(entry, 'error', `\`${fieldName(path)}\` still has the template's placeholder; replace it with real text`, path);
  } else if (value && typeof value === 'object') {
    for (const [k, v] of Object.entries(value)) placeholders(entry, v, [...path, Array.isArray(value) ? Number(k) : k]);
  }
}

// ---------------------------------------------------------------------------------------------------------------
// YAML syntax errors

const SYNTAX_HINT = {
  BLOCK_AS_IMPLICIT_KEY: 'a value that contains ": " must be in quotes',
  MULTILINE_IMPLICIT_KEY: 'check the indentation; a value that contains ": " must be in quotes',
  DUPLICATE_KEY: 'this key appears twice; keep one',
  TAB_AS_INDENT: 'indent with spaces, not tabs',
  MISSING_CHAR: 'a quote or bracket is not closed',
  BAD_INDENT: 'check the indentation of this line',
};

function syntaxErrors(entry) {
  for (const err of entry.doc.errors) {
    const [pos] = err.linePos ?? [{ line: 1, col: 1 }];
    const first = err.message.split('\n')[0].replace(/ at line \d+, column \d+:?$/, '');
    const hint = SYNTAX_HINT[err.code];
    report(entry, 'error', `YAML syntax: ${first}${hint ? ` (${hint})` : ''}`, pos);
  }
}

// ---------------------------------------------------------------------------------------------------------------
// schema errors, rewritten as short instructions

const PATTERN_HINT = {
  id: 'use lowercase letters, digits and hyphens only, e.g. rabindranath-tagore-1926',
  date: 'write "YYYY", "YYYY-MM", "YYYY-MM-DD" or a decade like "1980s", in quotes',
  evidence: 'write source tiers joined by +, e.g. P or P+S (P primary, S secondary, J journalism, F later own account, T tertiary)',
  language: 'use a two-letter ISO 639-1 code (en, tr, fr …) or ota for Ottoman Turkish',
  url: 'a link must start with http:// or https:// (put a book or archive reference in `citation` instead)',
  archived: 'use a web.archive.org or archive.today (archive.ph) link',
  accessed: 'write it as "YYYY-MM-DD"',
};

function closest(word, options) {
  let best = null, bestD = Infinity;
  for (const o of options) {
    const d = distance(String(word).toLowerCase(), String(o).toLowerCase());
    if (d < bestD) [best, bestD] = [o, d];
  }
  return bestD <= Math.max(2, Math.floor(String(word).length / 3)) ? best : null;
}

function distance(a, b) { // Levenshtein
  const row = Array.from({ length: b.length + 1 }, (_, i) => i);
  for (let i = 1; i <= a.length; i++) {
    let prev = row[0]; row[0] = i;
    for (let j = 1; j <= b.length; j++) {
      const cur = row[j];
      row[j] = Math.min(row[j] + 1, row[j - 1] + 1, prev + (a[i - 1] === b[j - 1] ? 0 : 1));
      prev = cur;
    }
  }
  return row[b.length];
}

const pointer = (p) => p.split('/').slice(1).map((s) => s.replace(/~1/g, '/').replace(/~0/g, '~'));
const showValue = (v) => (typeof v === 'string' ? `"${v}"` : JSON.stringify(v));

// an empty value: a required field must be filled in, an optional one may simply be deleted
function emptyMessage(name, segs, schema) {
  if (segs.length === 1 && schema.required?.includes(segs[0])) return `\`${name}\` is empty; fill it in`;
  if (segs.at(-1) === 'url') return `\`${name}\` is empty; add the link, or delete the line and give a \`citation\``;
  return `\`${name}\` is empty; fill it in or delete the line`;
}

function schemaErrors(entry, errors, schema) {
  // A `type` error on a path says enough; drop other complaints about the same value. The sub-errors of an
  // anyOf (source needs url or citation) are replaced by one message for the anyOf itself.
  const typed = new Set(errors.filter((e) => e.keyword === 'type').map((e) => e.instancePath));
  const seen = new Set();
  for (const err of errors) {
    if (err.schemaPath.includes('/anyOf/')) continue;
    if (err.keyword !== 'type' && typed.has(err.instancePath)) continue;
    const segs = pointer(err.instancePath);
    const name = fieldName(segs);
    const last = segs.at(-1);
    let at = segs, msg;
    switch (err.keyword) {
      case 'required': {
        const key = err.params.missingProperty;
        msg = key === 'sources'
          ? 'missing `sources`: add at least one source with a url or a citation'
          : `missing \`${name ? `${name}.` : ''}${key}\``;
        break;
      }
      case 'additionalProperties': {
        const key = err.params.additionalProperty;
        const allowed = Object.keys(err.parentSchema.properties ?? {});
        const guess = closest(key, allowed);
        at = [...segs, key];
        msg = `unknown key \`${key}\`${name ? ` in ${name}` : ''}; ${guess ? `did you mean \`${guess}\`?` : `allowed: ${allowed.join(', ')}`}`;
        break;
      }
      case 'enum': {
        if (err.data === null || err.data === '') { msg = emptyMessage(name, segs, schema); break; }
        const allowed = err.params.allowedValues.filter((v) => v !== null);
        const guess = closest(err.data, allowed);
        msg = `\`${name}\` is ${showValue(err.data)}; ${guess ? `did you mean ${guess}? ` : ''}allowed: ${allowed.join(' · ')}`;
        break;
      }
      case 'type': {
        const want = err.params.type;
        if (err.data === null) msg = emptyMessage(name, segs, schema);
        else if (want === 'string' || String(want).startsWith('string')) msg = `\`${name}\` must be text; put the value in quotes: ${last}: "${sourceText(entry, segs) ?? err.data}"`;
        else if (want === 'array') msg = `\`${name}\` must be a list; start each item with "- "`;
        else if (want === 'object') msg = `\`${name}\` must be a block of indented key: value lines`;
        else if (want === 'integer') msg = `\`${name}\` must be a whole number, without quotes`;
        else if (want === 'boolean') msg = `\`${name}\` must be true or false, without quotes`;
        else msg = `\`${name}\` must be ${want}`;
        break;
      }
      case 'pattern': {
        const hint = segs.includes('source_fingerprints')
          ? 'a fingerprint is 12 lowercase hex characters; leave the value as it was'
          : PATTERN_HINT[last] ?? `must match ${err.params.pattern}`;
        msg = `\`${name}\` is ${showValue(err.data)}; ${hint}`;
        break;
      }
      case 'anyOf':
        msg = `\`${name}\` needs a \`url\` or, when there is no link, a \`citation\``;
        break;
      case 'minItems':
        msg = last === 'sources' ? '`sources` is empty: add at least one source with a url or a citation' : `\`${name}\` is empty`;
        break;
      case 'minLength':
        msg = emptyMessage(name, segs, schema);
        break;
      case 'format':
        msg = `\`${name}\` is ${showValue(err.data)}; write a real date as "YYYY-MM-DD"`;
        break;
      case 'uniqueItems':
        msg = `\`${name}\` lists the same entry twice`;
        break;
      default:
        msg = `\`${name || 'file'}\` ${err.message}`;
    }
    const key = `${err.instancePath}|${msg}`;
    if (seen.has(key)) continue;
    seen.add(key);
    report(entry, 'error', msg, at);
  }
}

// ---------------------------------------------------------------------------------------------------------------
// records

const ERA_SPAN = { contemporary: 'up to 9 Nov 1938', funeral: '10 Nov–31 Dec 1938', posthumous: '1939 on' };
const INLINE_TRANSLATION = /\[\s*(english\s+)?translation\b|\btranslation\s*:/i;

function realDate(d) {
  if (!/^\d{4}-\d{2}-\d{2}$/.test(d)) return true;
  const [y, m, day] = d.split('-').map(Number);
  const t = new Date(Date.UTC(y, m - 1, day));
  return t.getUTCMonth() === m - 1 && t.getUTCDate() === day;
}

const records = walk(VOICES).map(load);
const byId = new Map();        // id -> entry (first file to claim it)
const byVoiceDate = new Map(); // "voice|date" -> entry

for (const e of records) {
  if (!e.data) { syntaxErrors(e); continue; }
  const d = e.data;
  if (!isObject(d)) { report(e, 'error', 'the file is empty or is not a list of key: value lines'); e.data = null; continue; }
  if (!checkVoice(d)) schemaErrors(e, checkVoice.errors, voiceSchema);
  placeholders(e, d);

  const name = basename(e.file, '.yaml');
  const folder = posix(relative(VOICES, dirname(e.file)));
  if (typeof d.id === 'string' && d.id !== name) {
    report(e, 'error', `id \`${d.id}\` does not match the file name; rename the file to ${d.id}.yaml or set id: ${name}`, ['id']);
  }
  if (typeof d.id === 'string') {
    const other = byId.get(d.id);
    if (other) report(e, 'error', `id \`${d.id}\` is already used by ${other.path}; ids must be unique (add -<mm>, -<dd> or a word)`, ['id']);
    else byId.set(d.id, e);
  }

  if (typeof d.date === 'string' && DATE_RE.test(d.date)) {
    const y = yearOf(d.date);
    if (folder !== y) report(e, 'error', `date ${d.date} belongs in data/voices/${y}/; move this file to data/voices/${y}/${name}.yaml`, ['date']);
    if (!realDate(d.date)) report(e, 'error', `date ${d.date} is not a real calendar date`, ['date']);
    const era = eraOf(d.date);
    if (typeof d.era === 'string' && era && d.era !== era) {
      report(e, 'error', `era is ${d.era}, but date ${d.date} is ${era} (${ERA_SPAN[era]}); set era: ${era}`, ['era']);
    }
  }

  if (typeof d.summary === 'string') {
    const n = words(d.summary);
    // an editorial guideline, not a validity rule: long summaries warn, never fail
    if (n > SUMMARY_WARN) report(e, 'warning', `summary has ${n} words; keep it to ${SUMMARY_WARN} or fewer (their own words go in quote)`, ['summary']);
  }

  const q = d.quote;
  if (isObject(q) && typeof q.text === 'string' && q.needs_split !== true) {
    if (/^\s*\[translation\]/i.test(q.text)) {
      report(e, 'error', 'quote.text starts with "[translation]"; remove it and set quote.is_translation: true', ['quote', 'text']);
    } else if (INLINE_TRANSLATION.test(q.text)) {
      report(e, 'error', 'quote.text contains a translation; move the English into quote.translation (or set quote.needs_split: true)', ['quote', 'text']);
    }
  }

  // same voice on the same date: often one statement entered twice
  if (typeof d.voice === 'string' && d.date != null) {
    const key = `${d.voice.trim().toLowerCase()}|${d.date}`;
    const other = byVoiceDate.get(key);
    if (other) report(e, 'warning', `possible duplicate of ${other.path} (same voice and date); merge them if it is the same statement`, ['voice']);
    else byVoiceDate.set(key, e);
  }
}

// ---------------------------------------------------------------------------------------------------------------
// files that the loader would silently skip

function strayFiles(dir) {
  if (!existsSync(dir)) return;
  for (const ent of readdirSync(dir, { withFileTypes: true })) {
    const p = join(dir, ent.name);
    if (ent.name.startsWith('.')) continue;
    if (ent.isDirectory()) { strayFiles(p); continue; }
    if (ent.name.endsWith('.yaml') || ent.name.endsWith('.md')) continue;
    const entry = { path: posix(rel(p)) };
    if (ent.name.endsWith('.yml')) report(entry, 'error', `rename to ${ent.name.slice(0, -4)}.yaml; .yml files are not read`, { line: 1, col: 1 });
    else report(entry, 'warning', 'not a .yaml file; only .yaml files are read here', { line: 1, col: 1 });
  }
}
strayFiles(VOICES);
strayFiles(TRANSLATIONS);

// ---------------------------------------------------------------------------------------------------------------
// translations

const FIELDS = Object.keys(translatable({}));
const recordIds = [...byId.keys()];
const translated = new Set();
let translationCount = 0;
const languages = existsSync(TRANSLATIONS)
  ? readdirSync(TRANSLATIONS, { withFileTypes: true }).filter((d) => d.isDirectory()).map((d) => d.name)
  : [];

for (const lang of languages) {
  for (const file of walk(join(TRANSLATIONS, lang))) {
    const e = load(file);
    translationCount++;
    if (!e.data) { syntaxErrors(e); continue; }
    const t = e.data;
    if (!isObject(t)) { report(e, 'error', 'the file is empty or is not a list of key: value lines'); continue; }
    if (!checkTranslation(t)) schemaErrors(e, checkTranslation.errors, translationSchema);
    placeholders(e, t);
    if (typeof t.id !== 'string') continue;

    const name = basename(file, '.yaml');
    const folder = posix(relative(join(TRANSLATIONS, lang), dirname(file)));
    if (t.id !== name) report(e, 'error', `id \`${t.id}\` does not match the file name; rename the file to ${t.id}.yaml or set id: ${name}`, ['id']);
    const rec = byId.get(t.id);
    if (!rec) {
      const guess = closest(t.id, recordIds);
      report(e, 'error', `no record with id \`${t.id}\` in data/voices/${guess ? `; did you mean ${guess}?` : ''}`, ['id']);
      continue;
    }
    translated.add(`${lang}|${t.id}`);
    const y = yearOf(rec.data.date);
    if (folder !== y) report(e, 'error', `the record is dated ${rec.data.date}; move this file to data/translations/${lang}/${y}/${name}.yaml`, ['id']);

    // Stale: the same rule the exhibition build uses. A translated field counts only while its fingerprint matches
    // the record's current English; otherwise the site shows the English.
    const src = translatable(rec.data);
    const stale = [], gone = [];
    for (const k of FIELDS) {
      if (t[k] == null) continue;
      if (typeof t[k] === 'string' && !t[k].trim() && src[k]) report(e, 'error', `\`${k}\` is empty but the English has text; translate it or remove the line`, [k]);
      if (t.source_fingerprints?.[k] === fingerprint(src[k])) continue;
      if (src[k] == null) gone.push(k); else stale.push(k);
    }
    const n = stale.length + gone.length;
    if (n) {
      const parts = [];
      if (stale.length) parts.push(`retranslate ${stale.join(', ')} from the current English, then set source_fingerprints ${stale.map((k) => `${k}: ${fingerprint(src[k])}`).join(', ')}`);
      if (gone.length) parts.push(`remove ${gone.join(', ')} (the record no longer has ${gone.length > 1 ? 'them' : 'it'})`);
      report(e, 'notice', `${n} stale field${n > 1 ? 's' : ''} (shown in English on the site): ${parts.join('; ')}`, [stale[0] ?? gone[0]], { stale: n });
    }
  }
}

// ---------------------------------------------------------------------------------------------------------------
// pull requests: a change to `verification` must be looked at by a maintainer (it decides what the site shows).
// Returns the set of data files the pull request touches, or null when this is not a pull request.

function pullRequestChanges() {
  const baseRef = process.env.GITHUB_BASE_REF;
  if (!baseRef) return null;
  const base = `origin/${baseRef}`;
  const git = (...a) => execFileSync('git', a, { cwd: ROOT, encoding: 'utf8', stdio: ['ignore', 'pipe', 'ignore'], maxBuffer: 64 << 20 });
  let changed;
  try { changed = git('diff', '--name-only', base, '--', 'data'); } catch { return null; } // no base: skip silently
  const diff = git('diff', '--name-status', '-M', base, '--', 'data/voices');
  const canon = (v) => JSON.stringify(v ?? null, (k, x) => (isObject(x) ? Object.fromEntries(Object.entries(x).sort(([a], [b]) => (a < b ? -1 : 1))) : x));
  const byPath = new Map(records.map((r) => [r.path, r]));
  for (const line of diff.split('\n').filter(Boolean)) {
    const [status, a, b] = line.split('\t');
    if (status.startsWith('D')) continue;
    const now = byPath.get(/^[RC]/.test(status) ? b : a);
    if (!now?.data) continue;
    let before = null;
    if (status !== 'A') { try { before = YAML.parse(git('show', `${base}:${a}`)); } catch { before = null; } }
    if (canon(before?.verification) === canon(now.data.verification)) continue;
    if (before) report(now, 'notice', 'this pull request changes `verification`: a maintainer must review it (it decides what the site shows)', ['verification']);
    else if (now.data.verification) report(now, 'notice', 'a new record arrives with `verification`: it is added by a maintainer after checking the source, not by the contributor; a maintainer must review it', ['verification']);
  }
  return new Set(changed.split('\n').filter(Boolean));
}
const prFiles = pullRequestChanges();

// ---------------------------------------------------------------------------------------------------------------
// output

const untranslated = languages.flatMap((lang) => recordIds.filter((id) => !translated.has(`${lang}|${id}`)).map((id) => `${lang}:${id}`));
const shown = problems
  .filter((p) => !only.length || only.some((o) => p.path === o || p.path.startsWith(`${o}/`)))
  .sort((a, b) => (a.path < b.path ? -1 : a.path > b.path ? 1 : a.line - b.line || a.col - b.col));
const count = (lvl) => shown.filter((p) => p.level === lvl).length;
const errors = count('error'), warnings = count('warning');
const staleFields = shown.reduce((n, p) => n + (p.stale ?? 0), 0), staleFiles = shown.filter((p) => p.stale).length;

const color = (process.stdout.isTTY || GITHUB) && !process.env.NO_COLOR;
const paint = (code, s) => (color ? `\x1b[${code}m${s}\x1b[0m` : s);
const LEVEL = { error: paint(31, 'error  '), warning: paint(33, 'warning'), notice: paint(36, 'notice ') };

let current = null;
for (const p of shown) {
  if (QUIET && p.level !== 'error') continue;
  if (p.path !== current) { console.log(`${current ? '\n' : ''}${paint(4, p.path)}`); current = p.path; }
  console.log(`  ${paint(2, `${p.line}:${p.col}`.padEnd(7))} ${LEVEL[p.level]}  ${p.message}`);
}

// GitHub annotations: one workflow command per problem. On a pull request, warnings and notices are annotated only
// on the files it touches (older ones stay in the log above); errors are always annotated, since they fail the run.
const esc = (s) => String(s).replace(/%/g, '%25').replace(/\r/g, '%0D').replace(/\n/g, '%0A');
const escProp = (s) => esc(s).replace(/:/g, '%3A').replace(/,/g, '%2C');
if (GITHUB) {
  for (const p of shown) {
    if (p.level !== 'error' && (QUIET || (prFiles && !prFiles.has(p.path)))) continue;
    console.log(`::${p.level} file=${escProp(p.path)},line=${p.line},col=${p.col}::${esc(p.message)}`);
  }
}

if (untranslated.length && !only.length && !QUIET) {
  console.log(`\n${untranslated.length} record${untranslated.length > 1 ? 's have' : ' has'} no translation yet (the site shows English): ${untranslated.slice(0, 8).join(', ')}${untranslated.length > 8 ? ', …' : ''}`);
}
const summary = `${records.length} records, ${translationCount} translations: ${errors} error${errors === 1 ? '' : 's'}, ` +
  `${warnings} warning${warnings === 1 ? '' : 's'}, ${staleFields} stale translation field${staleFields === 1 ? '' : 's'}` +
  (staleFiles ? ` in ${staleFiles} file${staleFiles === 1 ? '' : 's'}` : '');
console.log(`\n${errors ? paint(31, 'FAIL') : paint(32, 'OK')}  ${summary}`);

// the job summary page on GitHub: the totals and every error and warning
if (GITHUB && process.env.GITHUB_STEP_SUMMARY) {
  const rows = shown.filter((p) => p.level !== 'notice').slice(0, 200)
    .map((p) => `| ${p.level} | \`${p.path}:${p.line}\` | ${p.message.replace(/\|/g, '\\|')} |`);
  const md = [`### Data validation: ${errors ? 'failed' : 'passed'}`, '', summary, ''];
  if (rows.length) md.push('| | file | problem |', '|---|---|---|', ...rows, '');
  appendFileSync(process.env.GITHUB_STEP_SUMMARY, md.join('\n') + '\n');
}

process.exit(errors ? 1 : 0);
