// Reading the dataset: one YAML file per voice in data/voices/<year>/<id>.yaml, and per-voice translations in
// data/translations/<lang>/<year>/<id>.yaml. Shared by the validator, the exhibition build and the scripts.
import { readFileSync, readdirSync, statSync, existsSync } from 'node:fs';
import { createHash } from 'node:crypto';
import { join, relative, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import YAML from 'yaml';

export const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..', '..');
export const VOICES = join(ROOT, 'data', 'voices');
export const TRANSLATIONS = join(ROOT, 'data', 'translations');

export function walk(dir) {
  if (!existsSync(dir)) return [];
  const out = [];
  for (const name of readdirSync(dir).sort()) {
    const p = join(dir, name);
    if (statSync(p).isDirectory()) out.push(...walk(p));
    else if (name.endsWith('.yaml')) out.push(p);
  }
  return out;
}

// "1938-11-10" → "1938"; "1980s" → "1980"
export const yearOf = (date) => String(date ?? '').slice(0, 4);
export const voicePath = (id, date) => join(VOICES, yearOf(date), `${id}.yaml`);
export const translationPath = (lang, id, date) => join(TRANSLATIONS, lang, yearOf(date), `${id}.yaml`);
export const rel = (p) => relative(ROOT, p);

export function readYaml(file) {
  const text = readFileSync(file, 'utf8');
  const doc = YAML.parseDocument(text, { prettyErrors: true });
  return { file, text, doc, data: doc.errors.length ? null : doc.toJS() };
}

export const loadVoices = () => walk(VOICES).map(readYaml);
export const loadTranslations = (lang) => walk(join(TRANSLATIONS, lang)).map(readYaml);

// A quote as one string, the form the first version of the dataset used. Translation fingerprints hash this,
// so it must stay stable: "[translation] " marks a text that is itself a translation; a trailing bracket carries
// the English translation and an optional editorial note.
export function quoteString(q) {
  if (!q || q.text == null) return null;
  let s = (q.is_translation ? '[translation] ' : '') + q.text;
  if (q.translation != null) s += ` [${q.note ? `${q.note}; ` : ''}English translation: '${q.translation}']`;
  return s;
}

export const fingerprint = (t) => createHash('sha1').update(t ?? '').digest('hex').slice(0, 12);

// the English source text of each translatable field of a voice record
export const translatable = (v) => ({
  voice: v.voice ?? null,
  role: v.role ?? null,
  quote: quoteString(v.quote),
  summary: v.summary ?? null,
  caveat: v.caveat ?? null,
  mediated_by: v.mediated_by ?? null,
  verification_note: v.verification?.note ?? null,
  verification_method: v.verification?.method ?? null,
});

// era from a date: contemporary up to his death, funeral to the end of 1938, posthumous after
export function eraOf(date) {
  const d = String(date);
  if (/^\d{3}0s$/.test(d)) return +d.slice(0, 4) >= 1940 ? 'posthumous' : null;
  if (d < '1938-11-10') return d.length < 10 && d.startsWith('1938') ? null : 'contemporary';
  if (d <= '1938-12-31') return 'funeral';
  return 'posthumous';
}
