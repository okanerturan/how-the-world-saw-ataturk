// Start a new record from the template:
//
//   npm run new -- "Albert Lebrun" 1938-11-10            → data/voices/1938/albert-lebrun-1938.yaml
//   npm run new -- "Albert Lebrun" 1938-11-10 --id albert-lebrun-1938-11-10
//
// Fills in id, voice, date and (when the date decides it) era; everything else stays as the template's commented
// blanks. Never overwrites an existing file.
import { existsSync, readFileSync, writeFileSync, mkdirSync } from 'node:fs';
import { join, dirname } from 'node:path';
import YAML from 'yaml';
import { ROOT, VOICES, walk, rel, yearOf, eraOf } from './lib/records.mjs';

const TEMPLATE = join(ROOT, 'data', 'templates', 'voice.yaml');
const SCHEMA_LINE = '# yaml-language-server: $schema=../../schema/voice.schema.json';
const DATE_RE = new RegExp(JSON.parse(readFileSync(join(ROOT, 'data', 'schema', 'voice.schema.json'), 'utf8')).properties.date.pattern);

function fail(en, tr) {
  console.error(`${en}\n${tr}`);
  process.exit(1);
}

// ---- arguments
const argv = process.argv.slice(2);
let id = null;
const pos = [];
for (let i = 0; i < argv.length; i++) {
  if (argv[i] === '--id') id = argv[++i];
  else if (argv[i].startsWith('--id=')) id = argv[i].slice(5);
  else pos.push(argv[i]);
}
const [voice, date] = pos;
if (!voice || !date || pos.length > 2) {
  fail('usage: npm run new -- "<voice name>" <date>   e.g. npm run new -- "Albert Lebrun" 1938-11-10',
       'kullanım: npm run new -- "<ses adı>" <tarih>   örnek: npm run new -- "Albert Lebrun" 1938-11-10');
}
if (!DATE_RE.test(date)) {
  fail(`date "${date}" must be YYYY, YYYY-MM, YYYY-MM-DD or a decade like 1980s`,
       `tarih "${date}" YYYY, YYYY-AA, YYYY-AA-GG ya da 1980s gibi bir on yıl olmalı`);
}

// ---- id: <voice-slug>-<year>, transliterating Turkish and other Latin letters
function slugify(s) {
  return s
    .replace(/[ıİ]/g, 'i').replace(/ß/g, 'ss').replace(/[æÆ]/g, 'ae').replace(/[œŒ]/g, 'oe').replace(/[øØ]/g, 'o')
    .replace(/[łŁ]/g, 'l').replace(/[đĐðÐ]/g, 'd').replace(/[þÞ]/g, 'th')
    .normalize('NFKD').replace(/[̀-ͯ]/g, '')
    .toLowerCase().replace(/['’`]/g, '').replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '');
}
if (!id) {
  const slug = slugify(voice);
  if (!slug) {
    fail('could not make an id from this name (no Latin letters); give one with --id, e.g. --id sun-yat-sen-1924',
         'bu addan kimlik üretilemedi (Latin harfi yok); --id ile verin, örnek: --id sun-yat-sen-1924');
  }
  id = `${slug}-${/s$/.test(date) ? date : yearOf(date)}`;
}
if (!/^[a-z0-9]+(-[a-z0-9]+)*$/.test(id)) {
  fail(`id "${id}" must be lowercase letters, digits and hyphens`, `kimlik "${id}" yalnızca küçük harf, rakam ve tire içermeli`);
}

const file = join(VOICES, yearOf(date), `${id}.yaml`);
const taken = walk(VOICES).find((p) => p.endsWith(`/${id}.yaml`) || p.endsWith(`\\${id}.yaml`));
if (existsSync(file) || taken) {
  const alt = date.length >= 7 ? `${id.replace(/-\d{4}s?$/, '')}-${date}` : `${id}-<word>`;
  fail(`${rel(taken ?? file)} already exists; not overwriting it. Pick another id, e.g. --id ${alt}`,
       `${rel(taken ?? file)} zaten var; üzerine yazılmadı. Başka bir kimlik seçin, örnek: --id ${alt}`);
}

// ---- fill the template
const era = eraOf(date);
const scalar = (v) => YAML.stringify(v, { lineWidth: 0 }).trim(); // quotes the name only when YAML needs it
const values = { id, voice: scalar(voice), date: JSON.stringify(date), ...(era ? { era } : {}) };

// Replace `key:` (optionally commented out, as era is in the template) with `key: value`, keeping any trailing
// comment at its column. A key the template lacks is added above the first field.
function setKey(text, key, value) {
  const re = new RegExp(`^(?:#\\s*)?${key}:[ \\t]*(?:""|'')?([ \\t]*#.*)?$`, 'm');
  const m = text.match(re);
  if (!m) {
    const lines = text.split('\n');
    const at = lines.findIndex((l) => /^[a-z_]+:/.test(l));
    lines.splice(at < 0 ? lines.length : at, 0, `${key}: ${value}`);
    return lines.join('\n');
  }
  let line = `${key}: ${value}`;
  if (m[1]) {
    const col = m[0].length - m[1].trimStart().length;
    line = line.padEnd(Math.max(col, line.length + 2)) + m[1].trimStart();
  }
  return text.replace(re, () => line);
}

const SKELETON = `${SCHEMA_LINE}
# New voice record. Fill in every field below; see data/README.md. Write only what the source says.
# Yeni ses kaydı. Aşağıdaki alanları doldurun; bkz. data/README.md. Yalnızca kaynağın söylediğini yazın.
id:
voice:
voice_type:        # person | press | institution | collective
role:
country:
country_now:
domain:            # politics | letters | arts | military | religion | science | press | sport | diplomacy
date: ""
# era:
polarity:          # admiring | hostile | conflicted | instrumental | witness
summary: >-

sources:
  - url:
    # citation: ""  # full citation when there is no link / bağlantı yoksa tam künye
# quote:
#   text: >-
#
#   language:
`;

let text = existsSync(TEMPLATE) ? readFileSync(TEMPLATE, 'utf8') : SKELETON;
// the template's schema line is written for data/voices/<YYYY>/ already; make sure it is there and right
text = /^# yaml-language-server: \$schema=.*$/m.test(text)
  ? text.replace(/^# yaml-language-server: \$schema=.*$/m, SCHEMA_LINE)
  : `${SCHEMA_LINE}\n${text}`;
for (const [k, v] of Object.entries(values)) text = setKey(text, k, v);

mkdirSync(dirname(file), { recursive: true });
writeFileSync(file, text, { flag: 'wx' }); // wx: fail rather than overwrite, even in a race
console.log(rel(file));
console.log(`Fill in the empty fields (the comments explain each one), then: npm run validate -- ${rel(file)}`);
console.log(`Boş alanları doldurun (her alanın açıklaması yanında), sonra: npm run validate -- ${rel(file)}`);
