// Writing records the way the repo keeps them: dates quoted, long text as folded blocks, no empty fields.
import YAML, { Scalar } from 'yaml';

export const clean = (o) => Object.fromEntries(Object.entries(o).filter(([, v]) => v !== null && v !== undefined && v !== false && !(Array.isArray(v) && !v.length)));

export function toYaml(obj, header = '') {
  const doc = new YAML.Document(obj);
  YAML.visit(doc, {
    Pair(_, pair) {
      const k = pair.key?.value;
      if (YAML.isScalar(pair.value) && typeof pair.value.value === 'string') {
        if (['date', 'checked_on', 'accessed'].includes(k)) pair.value.type = Scalar.QUOTE_DOUBLE;
        else if (pair.value.value.length > 90 && !['url', 'archived'].includes(k)) pair.value.type = Scalar.BLOCK_FOLDED;
      }
    },
  });
  return `${header ? `${header}\n` : ''}${doc.toString({ lineWidth: 110, minContentWidth: 40, indentSeq: true })}`;
}

export const TRANSLATION_HEADER = (lang, rel) => [
  `# ${lang === 'tr' ? 'Turkish' : lang} for ${rel}. Machine translation; corrections welcome.`,
  '# source_fingerprints: which English each field was translated from. Leave them as they are.',
  '# yaml-language-server: $schema=../../../schema/translation.schema.json',
].join('\n');
