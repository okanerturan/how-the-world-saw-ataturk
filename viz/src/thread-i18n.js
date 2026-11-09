// Thread in two languages. English is the archive's own; Turkish comes from i18n/ (machine-translated with
// Gemini, see scripts/translate-tr.py). The language is chosen by ?lang=, then a remembered choice, then the browser.
import EN from '../i18n/thread-ui.en.json';
import TRD from '../i18n/thread.tr.json';   // { ui, countries: {en: tr}, mediated: {en: tr}, tour: {key: tr} }

const pick = () => {
  const q = new URLSearchParams(location.search).get('lang');
  if (q === 'tr' || q === 'en') { try { localStorage.setItem('thread-lang', q); } catch {} return q; }
  try { const s = localStorage.getItem('thread-lang'); if (s === 'tr' || s === 'en') return s; } catch {}
  return (navigator.languages ?? [navigator.language]).some((l) => /^tr\b/i.test(l ?? '')) ? 'tr' : 'en';
};
export const LANG = pick();
export const TR = LANG === 'tr';
const UI = TR ? { ...EN, ...TRD.ui } : EN;
export const tx = (k, v = {}) => String(UI[k] ?? EN[k] ?? k).replace(/\{(\w)\}/g, (_, x) => v[x] ?? '');
export const country = (c) => (TR ? TRD.countries[c] ?? c : c);
export const mediated = (m) => (TR ? TRD.mediated[m] ?? m : m);
export const tour = (key, en) => (TR ? TRD.tour[key] ?? en : en);
export const months = tx('months').split(',');
// decades with Turkish vowel-harmony suffixes: 1920'ler, 1930'lar …
const SUF = { 0: "'ler", 1: "'lar", 2: "'ler", 3: "'lar", 4: "'lar", 5: "'ler", 6: "'lar", 7: "'ler", 8: "'ler", 9: "'lar" };
export const decadeLabel = (d) => (TR ? `${d}${d % 100 === 0 ? "'ler" : SUF[(d / 10) % 10]}` : `${d}s`);
export const upper = (s, turkish) => (TR && turkish ? s.toLocaleUpperCase('tr') : s.toUpperCase());

// per-voice Turkish fields, only those still matching the English they were translated from
export async function loadVoices(base) {
  if (!TR) return new Map();
  try { return new Map(Object.entries(await (await fetch(`${base}gazes.tr.json`)).json())); } catch { return new Map(); }
}

// put the page's static words into the chosen language
export function localizePage() {
  document.documentElement.lang = LANG;
  document.title = tx('page_title');
  document.querySelectorAll('[data-t]').forEach((el) => { el.textContent = tx(el.dataset.t); });
  document.querySelectorAll('[data-tp]').forEach((el) => { el.placeholder = tx(el.dataset.tp); });
  const sw = document.getElementById('lang');
  if (sw) {
    sw.textContent = TR ? 'English' : 'Türkçe';
    sw.onclick = (e) => { e.preventDefault(); const u = new URL(location.href); u.searchParams.set('lang', TR ? 'en' : 'tr'); location.href = u; };
  }
}
