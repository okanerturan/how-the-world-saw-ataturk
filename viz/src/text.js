// Hansard's digitised text misreads "Kemal" (Kliamil, Kcmil, Kernel…). The data quotes it as printed;
// on screen we add the editorial correction in brackets.
const OCR = /\b(Mustap?ha|Mustafa|Moustapha)\s+(Kamil|Kemil|Kcmil|Kliamil|Kernel|Kemai|Keinal|Kenal|Kcmal|Kemel)\b/g;
export const restoreName = (t) => (t ? t.replace(OCR, '$1 $2 [Kemal]') : t);

// The voice's words in English, if the record has them: an English text, or the English translation it carries.
export function englishQuote(g) {
  if (!g.quote_text) return null;
  if (g.quote_lang === 'en') return restoreName(g.quote_text);
  if (g.quote_translation) return restoreName(g.quote_translation);
  if (g.quote_lang) return null;
  // a new record without a language yet: guess from the words
  const q = g.quote_text;
  const words = (q.match(/\b(the|and|of|is|was|to|that|his|he|with|for|in)\b/gi) || []).length;
  const foreign = (q.match(/[^\x00-\x7F’‘“”—–…]/g) || []).length;
  return words >= 2 && foreign < q.length * 0.04 ? restoreName(q) : null;
}
