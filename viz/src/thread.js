// THREAD: every voice in the archive, in the order they spoke, set as one continuous line of text that
// winds out in a spiral from 1919 at the centre to today at the rim. The letters are signed-distance
// glyphs; each one is cut heavier or lighter by the tone of his photograph beneath it, the way a
// banknote engraver draws a face with line weight. Far away it is a portrait; close up it is legible.
import * as THREE from 'three';
import TinySDF from '@mapbox/tiny-sdf';
import { loadGazes } from './data.js';
import { englishQuote, restoreName } from './text.js';
import { PROLOGUE, PATHS, FINALE, FUNERAL_LEAD } from './tour-paths.js';
import { TR, LANG, tx, country, mediated, tour, months, decadeLabel, upper, loadVoices, localizePage } from './thread-i18n.js';
import './thread.css';

const $ = (id) => document.getElementById(id);
localizePage();
const BASE = import.meta.env.BASE_URL;
const [{ gazes, byDate }, meta, TRV] = await Promise.all([
  loadGazes(), fetch(`${BASE}photos/photos.json`).then((r) => r.json()), loadVoices(BASE),
]);
// countries and territories only: not the international bodies, nor the few records filed under two countries at once
const NOT_ONE_COUNTRY = /European Union|Council of Europe|International|\/|and diaspora/;
$('count').textContent = tx('count', { n: gazes.length, c: new Set(gazes.map((x) => x.country_now).filter((c) => c && !NOT_ONE_COUNTRY.test(c))).size });
const esc = (t) => String(t ?? '').replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' })[c]);

// the guided routes, in the page's language (keys match scripts that build i18n/thread.tr.json)
const ROUTES = [PROLOGUE, ...PATHS, FINALE].map((r) => {
  const k = r.id ?? (r === PROLOGUE ? 'prologue' : 'finale');
  return { ...r, title: tour(`${k}|title`, r.title), question: r.question && tour(`${k}|question`, r.question), line: r.line && tour(`${k}|line`, r.line),
    stops: r.stops.map((st) => ({ ...st, note: tour(`${k}|stop|${st.id}|note`, st.note), name: st.name && tour(`${k}|stop|${st.id}|name`, st.name) })) };
});
const famous = new Set(ROUTES.flatMap((c) => c.stops.map((s) => s.id)));
const nameOf = new Map(ROUTES.flatMap((c) => c.stops.filter((s) => s.name).map((s) => [s.id, s.name])));
// a voice's fields in the page's language; Turkish falls back to English field by field
const trOf = (g) => TRV.get(g.id) ?? {};
// links into the archive on GitHub: every record can be corrected there, and missing voices suggested
const REPO = 'https://github.com/okanerturan/how-the-world-saw-ataturk';
const editUrl = (path) => `${REPO}/edit/main/${path}`;
const langName = (code) => { try { return new Intl.DisplayNames([LANG], { type: 'language' }).of(code === 'ota' ? 'tr' : code); } catch { return code; } };
const voiceName = (g) => nameOf.get(g.id) ?? (trOf(g).voice ?? g.voice).replace(/\s*\(.*\)$/, '');
const roleOf = (g) => trOf(g).role ?? g.role;
const sawOf = (g) => trOf(g).what_they_saw ?? g.what_they_saw;
const placeOf = (g) => country(g.country_now);
const turkishVoice = (g) => /Turkey|TRNC/.test(g.country_now);
// the words shown as the voice's quote: Turkish (original or translated) or the English the archive gives
const quoteOf = (g) => (TR && trOf(g).quote != null ? trOf(g).quote : englishQuote(g));
const when = (d) => { const [y, m, day] = d.split('-'); return [day && +day, m && months[+m - 1], y].filter(Boolean).join(' '); };

// the portraits the thread can be engraved from: source crop centre and radius in image pixels
const FACES = [
  { key: '1932-official', cx: 285, cy: 255, r: 215, label: '1932', t: 'face_1932', gamma: 1.15 },
  { key: '1922-kalpak', cx: 475, cy: 740, r: 570, label: '1922, kalpak', t: 'face_kalpak', gamma: 0.8 },
  { key: '1922-meurisse', cx: 590, cy: 830, r: 570, label: '1922, Paris press', t: 'face_paris', gamma: 0.9 },
];

// ---------------------------------------------------------------- the text
const SEP = '   ';
// each voice on the thread: their own words in quotation marks, or, when the archive has none in this language,
// the archive's summary of what they saw (set lighter when unwound, and labelled as ours)
const entries = byDate.map((g) => {
  const q = quoteOf(g);
  return { g, kind: q ? 'quote' : 'summary', text: `${upper(voiceName(g), turkishVoice(g))}, ${g.date.slice(0, 4)}: ${q ? `“${q}”` : sawOf(g)}${SEP}` };
});
const RIM = tx('rim', { n: byDate.length });

// ---------------------------------------------------------------- glyph atlas (signed distance fields)
const FS = 48, BUF = 10, RAD = 12, CUT = 0.25;
const sdf = new TinySDF({ fontSize: FS, buffer: BUF, radius: RAD, cutoff: CUT, fontFamily: 'Georgia, "Times New Roman", serif' });
const chars = new Set([...entries.map((e) => e.text).join(''), ...RIM]);
const glyphs = new Map();
{
  const W = 1024; let x = 0, y = 0, row = 0;
  const drawn = [];
  for (const ch of chars) {
    const gl = sdf.draw(ch);
    if (x + gl.width > W) { x = 0; y += row + 1; row = 0; }
    drawn.push([ch, gl, x, y]);
    x += gl.width + 1; row = Math.max(row, gl.height);
  }
  const H = 2 ** Math.ceil(Math.log2(y + row + 1));
  const data = new Uint8Array(W * H);
  for (const [ch, gl, gx, gy] of drawn) {
    for (let j = 0; j < gl.height; j++) data.set(gl.data.subarray(j * gl.width, (j + 1) * gl.width), (gy + j) * W + gx);
    glyphs.set(ch, {
      adv: gl.glyphAdvance / FS, empty: gl.glyphWidth === 0,
      box: [-BUF / FS, (gl.glyphTop + BUF) / FS, gl.width / FS, gl.height / FS],
      uv: [gx / W, gy / H, (gx + gl.width) / W, (gy + gl.height) / H],
    });
  }
  var atlas = new THREE.DataTexture(data, W, H, THREE.RedFormat, THREE.UnsignedByteType);
  atlas.minFilter = THREE.LinearMipmapLinearFilter; atlas.magFilter = THREE.LinearFilter;
  atlas.generateMipmaps = true; atlas.needsUpdate = true;
}

// ---------------------------------------------------------------- the spiral layout
// r = b·φ, angle on screen α = π/2 − φ (clockwise from the top), one turn = one row of height h.
const R = 1000, K = 0.94;                         // disc radius; em size as a share of the row pitch
const all = entries.map((e) => e.text).join('');
const ADV = [...all].reduce((n, ch) => n + (glyphs.get(ch)?.adv ?? 0.5), 0);
let h = Math.sqrt((Math.PI * R * R) / (ADV * K));
const layout = (h) => {
  const b = h / (2 * Math.PI), em = h * K;
  let phi = (2.2 * h) / b;
  const out = [];
  entries.forEach((e, ei) => {
    e.first = out.length;
    for (const ch of e.text) {
      const adv = (glyphs.get(ch)?.adv ?? 0.5) * em, r = b * phi;
      out.push({ ch, phi, ei });
      phi += adv / Math.sqrt(r * r + b * b);
    }
    e.last = out.length - 1;
  });
  return { b, em, out, end: b * phi };
};
let L = layout(h);
for (let k = 0; k < 3; k++) { h *= R / L.end; L = layout(h); }
const { b, em } = L;
const at = (phi, lift = 0) => { const r = b * phi + lift, a = Math.PI / 2 - phi; return [r * Math.cos(a), r * Math.sin(a), a - Math.PI / 2]; };
const charPhi = Float64Array.from(L.out, (c) => c.phi);
const charEntry = Uint16Array.from(L.out, (c) => c.ei);

// instances: one per visible glyph of the thread, plus the rim inscription
const inst = [];
L.out.forEach((c, i) => {
  const gl = glyphs.get(c.ch);
  if (!gl || gl.empty) return;
  const [x, y, rot] = at(c.phi);
  const mid = at(c.phi + (gl.adv * em) / 2 / (b * c.phi), 0.32 * em);
  inst.push({ x, y, rot: at(c.phi + (gl.adv * em) / 2 / (b * c.phi))[2], gl, entry: c.ei, idx: i, sx: mid[0], sy: mid[1], scale: 1 });
});
{
  const RR = R + 2.6 * h, emR = 2.0 * h;
  const text = RIM.repeat(Math.max(1, Math.floor((2 * Math.PI * RR) / ([...RIM].reduce((n, ch) => n + glyphs.get(ch).adv, 0) * emR))));
  const total = [...text].reduce((n, ch) => n + glyphs.get(ch).adv, 0) * emR;
  const sp = (2 * Math.PI * RR - total) / text.length;
  let s = 0;
  for (const ch of text) {
    const gl = glyphs.get(ch), a = Math.PI / 2 - s / RR;
    if (!gl.empty) inst.push({ x: RR * Math.cos(a), y: RR * Math.sin(a), rot: a - Math.PI / 2 - (gl.adv * emR) / 2 / RR, gl, entry: 65535, idx: -1, sx: 0, sy: 0, scale: emR / em, rim: true });
    s += gl.adv * emR + sp;
  }
}
const n = inst.length;
inst.forEach((it, k) => { if (it.rim) return; const e = entries[it.entry]; if (e.i0 == null) e.i0 = k; e.i1 = k; });

// ---------------------------------------------------------------- tone from a photograph
async function toneOf(face) {
  const img = new Image();
  img.src = `${BASE}photos/${face.key}.jpg`;
  await img.decode();
  const S = 420, c = document.createElement('canvas'); c.width = c.height = S;
  const ctx = c.getContext('2d', { willReadFrequently: true });
  ctx.fillStyle = '#fff'; ctx.fillRect(0, 0, S, S);
  const k = S / (2 * face.r);
  ctx.drawImage(img, (face.r - face.cx) * k, (face.r - face.cy) * k, img.naturalWidth * k, img.naturalHeight * k);
  const px = ctx.getImageData(0, 0, S, S).data, lum = new Float32Array(S * S), hist = [];
  for (let k = 0; k < S * S; k++) {
    lum[k] = (0.3 * px[4 * k] + 0.59 * px[4 * k + 1] + 0.11 * px[4 * k + 2]) / 255;
    const dx = (k % S) - S / 2, dy = Math.floor(k / S) - S / 2;
    if (dx * dx + dy * dy < (S / 2) ** 2 && k % 7 === 0) hist.push(lum[k]);
  }
  hist.sort((p, q) => p - q);
  const lo = hist[Math.floor(hist.length * 0.01)], hi = hist[Math.floor(hist.length * 0.985)];
  const tone = new Float32Array(n);
  inst.forEach((it, k) => {
    if (it.rim) { tone[k] = 0.62; return; }
    const u = Math.min(S - 1, Math.max(0, Math.round((it.sx / R / 2 + 0.5) * S)));
    const v = Math.min(S - 1, Math.max(0, Math.round((0.5 - it.sy / R / 2) * S)));
    const l = Math.min(1, Math.max(0, (lum[v * S + u] - lo) / (hi - lo)));
    tone[k] = (1 - l) ** face.gamma;
  });
  return tone;
}

// ---------------------------------------------------------------- scene
if (!document.createElement('canvas').getContext('webgl2')) throw new Error('WebGL 2 is not available in this browser.');
const renderer = new THREE.WebGLRenderer({ antialias: false, powerPreference: 'high-performance' });
renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
renderer.setClearColor(0xf7f5f0);
$('app').append(renderer.domElement);
// phones reclaim the GPU when the page is backgrounded: offer to redraw rather than leave a dead canvas
renderer.domElement.addEventListener('webglcontextlost', (e) => {
  e.preventDefault();
  document.body.classList.remove('ready');
  window.__threadFail?.('The graphics were reset by the device.');
});
renderer.domElement.addEventListener('webglcontextrestored', () => location.reload());
const scene = new THREE.Scene();
const camera = new THREE.OrthographicCamera(-1, 1, 1, -1, -10, 10);

const geo = new THREE.InstancedBufferGeometry();
geo.setAttribute('position', new THREE.Float32BufferAttribute([0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0], 3));
geo.setIndex([0, 1, 2, 0, 2, 3]);
const A = (size, fill) => { const a = new Float32Array(n * size); inst.forEach((it, k) => fill(a, k * size, it)); return new THREE.InstancedBufferAttribute(a, size); };
geo.setAttribute('iPos', A(2, (a, o, it) => { a[o] = it.x; a[o + 1] = it.y; }));
geo.setAttribute('iRot', A(1, (a, o, it) => { a[o] = it.rot; }));
geo.setAttribute('iBox', A(4, (a, o, it) => { a.set(it.gl.box.map((v) => v * it.scale), o); }));
geo.setAttribute('iUV', A(4, (a, o, it) => { a.set(it.gl.uv, o); }));
geo.setAttribute('iEntry', A(1, (a, o, it) => { a[o] = it.entry; }));
geo.setAttribute('iIdx', A(1, (a, o, it) => { a[o] = it.idx < 0 ? 0 : it.idx; }));
const toneA = new THREE.InstancedBufferAttribute(new Float32Array(n), 1), toneB = new THREE.InstancedBufferAttribute(new Float32Array(n), 1);
geo.setAttribute('iToneA', toneA); geo.setAttribute('iToneB', toneB);
// where each glyph lands when its voice unwinds off the spiral: screen px (GL, y up), stagger share, heading flag
const flatAttr = new THREE.InstancedBufferAttribute(new Float32Array(n * 4), 4);
flatAttr.setUsage(THREE.DynamicDrawUsage);
geo.setAttribute('iFlat', flatAttr);
geo.instanceCount = n;

const uniforms = {
  uAtlas: { value: atlas }, uEm: { value: em }, uMix: { value: 0 }, uReveal: { value: 0 },
  uHover: { value: -1 }, uSel: { value: -1 }, uPx: { value: 1 }, uLit: { value: 0 },
  // two unwinding slots: x = the voice coming off the spiral, y = the one winding back
  uFE: { value: new THREE.Vector2(-1, -1) }, uFU: { value: new THREE.Vector2(0, 0) }, uFEm: { value: new THREE.Vector2(22, 22) },
  uFOff: { value: new THREE.Vector4() }, uScreen: { value: new THREE.Vector2(1, 1) }, uViewS: { value: 1 }, uViewRot: { value: 0 },
  uRect: { value: new THREE.Vector4() }, uClear: { value: 0 }, uDpr: { value: 1 },
};
const mat = new THREE.ShaderMaterial({
  uniforms, transparent: true, depthTest: false, depthWrite: false, side: THREE.DoubleSide,
  vertexShader: /* glsl */`
    attribute vec2 iPos; attribute float iRot; attribute vec4 iBox; attribute vec4 iUV;
    attribute float iEntry; attribute float iIdx; attribute float iToneA; attribute float iToneB; attribute float iMark;
    attribute vec4 iFlat;
    uniform float uEm, uMix, uReveal, uHover, uSel, uLit, uViewS, uViewRot;
    uniform vec2 uFE, uFU, uFEm, uScreen; uniform vec4 uFOff;
    varying vec2 vUV; varying float vTone, vState, vReveal, vMark, vFlat, vHead, vMine;
    mat2 rot(float a) { float c = cos(a), s = sin(a); return mat2(c, s, -s, c); }
    void main() {
      vec2 q = position.xy;
      vec2 l0 = vec2(iBox.x + q.x * iBox.z, iBox.y - q.y * iBox.w);
      vec2 w = iPos + rot(iRot) * l0 * uEm;
      vec4 clip = projectionMatrix * viewMatrix * vec4(w, 0.0, 1.0);
      // unwinding: the voice's letters leave the spiral one after another, like thread pulled off a spool,
      // turn upright and settle into lines of type on the screen
      float slot = abs(iEntry - uFE.x) < 0.5 ? 0.0 : (abs(iEntry - uFE.y) < 0.5 ? 1.0 : -1.0);
      float t = 0.0;
      if (slot > -0.5) {
        float u = slot < 0.5 ? uFU.x : uFU.y;
        t = clamp(u * 2.4 - iFlat.z * 1.4, 0.0, 1.0);
        t = t * t * (3.0 - 2.0 * t);
      }
      vMine = slot > -0.5 ? 1.0 : 0.0; vFlat = t; vHead = iFlat.w;
      if (t > 0.0) {
        vec4 a = projectionMatrix * viewMatrix * vec4(iPos, 0.0, 1.0);
        vec2 pS = (a.xy * 0.5 + 0.5) * uScreen;
        vec2 pF = iFlat.xy + (slot < 0.5 ? uFOff.xy : uFOff.zw);
        float da = iRot - uViewRot; da = atan(sin(da), cos(da));
        vec2 p = mix(pS, pF, t) + vec2(0.0, 40.0 * sin(3.14159 * t));
        p += rot(da * (1.0 - t)) * l0 * mix(uEm * uViewS, slot < 0.5 ? uFEm.x : uFEm.y, t);
        clip = vec4(p / uScreen * 2.0 - 1.0, 0.0, 1.0);
      }
      vUV = vec2(mix(iUV.x, iUV.z, q.x), mix(iUV.y, iUV.w, q.y));
      vTone = mix(iToneA, iToneB, uMix);
      vState = abs(iEntry - uSel) < 0.5 ? 2.0 : (abs(iEntry - uHover) < 0.5 ? 1.0 : 0.0);
      vReveal = clamp((uReveal - iIdx) / 900.0, 0.0, 1.0);
      vMark = uLit > 0.5 ? (iMark > 0.5 ? 1.0 : -1.0) : 0.0;
      gl_Position = clip;
    }`,
  fragmentShader: /* glsl */`
    uniform sampler2D uAtlas; uniform float uPx, uClear, uDpr; uniform vec4 uRect;
    varying vec2 vUV; varying float vTone, vState, vReveal, vMark, vFlat, vHead, vMine;
    void main() {
      float d = (1.0 - texture2D(uAtlas, vUV).r - ${CUT.toFixed(2)}) * ${RAD.toFixed(1)};  // atlas px, + outside
      float t = vTone;
      float fw = fwidth(d);
      // far away the weight draws the portrait; up close it is capped so the words stay letters
      float thr = mix(-0.7, mix(7.0, 2.6, smoothstep(6.0, 18.0, uPx)), pow(t, 1.25));   // uPx: screen px per em
      thr = mix(thr, 0.35, vFlat);                                                      // unwound: plain book weight
      float aa = max(fw * 0.75, 0.3);
      float a = 1.0 - smoothstep(thr - aa, thr + aa, d);
      a *= mix(mix(0.32, 1.0, smoothstep(0.02, 0.4, t)), 1.0, vFlat);
      vec3 ink = vec3(0.04), red = vec3(0.89, 0.04, 0.09);
      if (vMine < 0.5) {
        // a clearing in the engraving where the unwound voice is set
        vec2 o = max(max(uRect.xy - gl_FragCoord.xy, gl_FragCoord.xy - uRect.zw), 0.0);
        a *= 1.0 - 0.92 * uClear * (1.0 - smoothstep(0.0, 60.0 * uDpr, length(o)));
      }
      if (vFlat > 0.0 && vState > 1.5) { ink = mix(red, vHead > 1.5 ? vec3(0.36, 0.33, 0.29) : vHead > 0.5 ? red : vec3(0.07), vFlat); a = max(a, (1.0 - smoothstep(0.6 - aa, 0.6 + aa, d)) * (1.0 - vFlat)); }
      else if (vState > 1.5) { ink = red; a = max(a, (1.0 - smoothstep(0.6 - aa, 0.6 + aa, d))); }
      else if (vState > 0.5) { ink = mix(ink, vec3(0.89, 0.04, 0.09), 0.75); }
      else if (vMark > 0.5) { ink = vec3(0.86, 0.05, 0.1); a = max(a, 0.55 * (1.0 - smoothstep(1.2 - aa, 1.2 + aa, d))); }
      else if (vMark < -0.5) { a *= mix(0.3, 1.0, vFlat); }
      a *= vReveal;
      if (a < 0.004) discard;
      gl_FragColor = vec4(ink, a);
    }`,
});
const mesh = new THREE.Mesh(geo, mat);
mesh.frustumCulled = false;
scene.add(mesh);

// ---------------------------------------------------------------- the faces
let face = 0;
const tones = await Promise.all(FACES.map(toneOf));
toneA.array.set(tones[face]); toneA.needsUpdate = true;
toneB.array.set(tones[face]); toneB.needsUpdate = true;
let morph = null;
function setFace(i) {
  if (i === face) return;
  toneA.array.set(toneB.array.map((v, k) => v * uniforms.uMix.value + toneA.array[k] * (1 - uniforms.uMix.value))); toneA.needsUpdate = true;
  toneB.array.set(tones[i]); toneB.needsUpdate = true;
  uniforms.uMix.value = 0; morph = { t0: performance.now() };
  face = i; drawFaces();
}
const dedupe = (t) => { const m = t.match(/^(.+?)\1$/); return m ? m[1] : t; };
const photoOf = (key) => meta.find((p) => p.key === key);
function drawFaces() {
  const p = photoOf(FACES[face].key);
  $('faces').innerHTML = `<div class="sc">${esc(tx('engraved_from'))}</div>
    <div class="row">${FACES.map((f, i) => `<button data-i="${i}" class="${i === face ? 'on' : ''}">${esc(tx(f.t))}</button>`).join('')}</div>
    <div class="credit">${p ? `<a href="${esc(p.page)}" target="_blank" rel="noopener">${esc(p.title)}</a> · ${esc(dedupe(p.artist ?? ''))} · ${esc(p.license)}${p.archive ? ` · ${esc(p.archive)}` : ''}` : ''}</div>`;
  $('faces').querySelectorAll('button').forEach((bt) => (bt.onclick = () => setFace(+bt.dataset.i)));
}
drawFaces();

// ---------------------------------------------------------------- the view
const view = { x: 0, y: 0, s: 1, rot: 0 };   // world centre, px per world unit, roll
let fitS = 1, flight = null;
const availW = () => (innerWidth > 900 ? innerWidth - 340 : innerWidth);
function resize() {
  renderer.setSize(innerWidth, innerHeight, false);
  fitS = Math.min(availW(), innerHeight - 40) / (2 * (R + 4.5 * h)) * 0.98;
  if (view.s < fitS) view.s = fitS;
}
const homeX = () => -((innerWidth - availW()) / 2) / fitS;
resize(); view.s = fitS; view.x = homeX();
addEventListener('resize', resize);
const rowPx = () => h * view.s;
const toWorld = (cx, cy) => {
  const dx = (cx - innerWidth / 2) / view.s, dy = -(cy - innerHeight / 2) / view.s, c = Math.cos(view.rot), s = Math.sin(view.rot);
  return [view.x + c * dx - s * dy, view.y + s * dx + c * dy];
};
const toScreen = (x, y) => {
  const dx = x - view.x, dy = y - view.y, c = Math.cos(-view.rot), s = Math.sin(-view.rot);
  return [innerWidth / 2 + (c * dx - s * dy) * view.s, innerHeight / 2 - (s * dx + c * dy) * view.s];
};
const wrap = (a) => Math.atan2(Math.sin(a), Math.cos(a));
const smooth = (a, b2, t) => { t = Math.min(1, Math.max(0, (t - a) / (b2 - a))); return t * t * (3 - 2 * t); };
const uprightAt = (x, y) => Math.atan2(y, x) - Math.PI / 2;

// which character of the thread lies under a world point
function charAt(x, y) {
  const r = Math.hypot(x, y);
  if (r > R + h) return -1;
  const fa = ((Math.PI / 2 - Math.atan2(y, x)) % (2 * Math.PI) + 2 * Math.PI) % (2 * Math.PI);
  const k = Math.round((r - 0.33 * em - b * fa) / h);
  const phi = fa + 2 * Math.PI * k;
  if (phi < charPhi[0] || phi > charPhi[charPhi.length - 1]) return -1;
  let lo = 0, hi = charPhi.length - 1;
  while (lo < hi) { const m = (lo + hi + 1) >> 1; charPhi[m] <= phi ? (lo = m) : (hi = m - 1); }
  return lo;
}

// ---------------------------------------------------------------- input
const pointers = new Map();
let drag = null, moved = 0;
const cv = renderer.domElement;
cv.addEventListener('pointerdown', (e) => {
  cv.setPointerCapture(e.pointerId);
  pointers.set(e.pointerId, [e.clientX, e.clientY]);
  drag = { x: e.clientX, y: e.clientY }; moved = 0;
  if (!overType(e)) stopGuided();
  leaveTitle();
});
cv.addEventListener('pointermove', (e) => {
  if (!pointers.has(e.pointerId)) { hover(e); return; }
  const prev = pointers.get(e.pointerId);
  pointers.set(e.pointerId, [e.clientX, e.clientY]);
  if (pointers.size === 2) {
    const [p, q] = [...pointers.values()], other = p === pointers.get(e.pointerId) ? q : p;
    const d0 = Math.hypot(prev[0] - other[0], prev[1] - other[1]), d1 = Math.hypot(e.clientX - other[0], e.clientY - other[1]);
    zoomAt((e.clientX + other[0]) / 2, (e.clientY + other[1]) / 2, d1 / Math.max(1, d0));
    moved += 10; return;
  }
  const [x0, y0] = toWorld(prev[0], prev[1]), [x1, y1] = toWorld(e.clientX, e.clientY);
  view.x -= x1 - x0; view.y -= y1 - y0; flight = null;
  moved += Math.abs(e.clientX - prev[0]) + Math.abs(e.clientY - prev[1]);
});
const up = (e) => {
  pointers.delete(e.pointerId);
  if (moved < 5 && drag && overType(e)) { drag = null; return; }
  if (moved < 5 && drag && !overType(e)) {
    const ci = charAt(...toWorld(e.clientX, e.clientY));
    if (ci >= 0) select(charEntry[ci]); else windBack();
    // if the type now covers the place you clicked, slide his face aside so you can see where it came from
    if (ci >= 0 && cur && view.s > fitS * 1.3 && e.clientX > rect[0] - 40 && e.clientX < cur.left + cur.w + 80) {
      const [x, y] = toWorld(e.clientX, e.clientY), [vx, vy] = viewFor(x, y, ...cur.spot, view.s, view.rot);
      flyTo(vx, vy, view.s, view.rot, 1400);
    }
  }
  drag = null;
};
cv.addEventListener('pointerup', up); cv.addEventListener('pointercancel', up);
function zoomAt(cx, cy, f) {
  const [wx, wy] = toWorld(cx, cy);
  view.s = Math.min(view.s * f, 64 / h);
  view.s = Math.max(view.s, fitS * 0.9);
  const [nx, ny] = toWorld(cx, cy);
  view.x += wx - nx; view.y += wy - ny;
}
addEventListener('wheel', (e) => {
  if (e.target.closest('#sheet, #cap, #index')) return;
  e.preventDefault(); stopGuided(); leaveTitle(); flight = null;
  zoomAt(e.clientX, e.clientY, Math.exp(-e.deltaY * (e.ctrlKey ? 0.01 : 0.0022)));
}, { passive: false });

const tip = $('tip');
const overType = (e) => cur && cur.u > 0.5 && e.clientX > rect[0] && e.clientX < rect[2] && e.clientY > rect[1] && e.clientY < rect[3];
function hover(e) {
  if (uniforms.uReveal.value < n) return;
  if (overType(e)) { uniforms.uHover.value = -1; tip.hidden = true; cv.style.cursor = 'default'; return; }
  const ci = charAt(...toWorld(e.clientX, e.clientY));
  const ei = ci >= 0 ? charEntry[ci] : -1;
  uniforms.uHover.value = ei;
  cv.style.cursor = ei >= 0 ? 'pointer' : 'grab';
  if (ei < 0) { tip.hidden = true; return; }
  const g = byDate[ei];
  tip.hidden = false;
  tip.innerHTML = `<b>${esc(voiceName(g))}</b> · ${esc(when(g.date))} · ${esc(placeOf(g))}`;
  tip.style.left = `${e.clientX + 14}px`; tip.style.top = `${e.clientY + 16}px`;
}

// ---------------------------------------------------------------- the sheet: one voice, every source
const byVoice = new Map();
byDate.forEach((g, i) => { const k = g.voice; byVoice.has(k) ? byVoice.get(k).push(i) : byVoice.set(k, [i]); });
const notesOf = new Map();
for (const r of ROUTES) for (const st of r.stops) (notesOf.get(st.id) ?? notesOf.set(st.id, []).get(st.id)).push({ route: r, note: st.note });
const idxOf = new Map(byDate.map((g, i) => [g.id, i]));
const VERDICT = new Set(['confirmed', 'partial', 'paraphrase-ok', 'secondary-only', 'unreachable']);
function sheet(ei) {
  const el = $('sheet');
  if (ei == null || ei < 0) { el.hidden = true; return; }
  const g = byDate[ei], tr = trOf(g), q = quoteOf(g);
  const orig = g.quote_text ? restoreName(g.quote_text) : null;
  // the original under the shown words: in Turkish only when we translated it; in English whenever it differs
  const showOrig = orig && orig !== q && (!TR || tr.quote_kind === 'translated' || tr.quote == null);
  // a text that is itself a rendering (a Turkish paper's version of a foreign speaker) is 'as printed', not the original
  const origLabel = [tx(g.quote_is_translation ? 'as_printed' : 'original'), g.quote_lang && langName(g.quote_lang)].filter(Boolean).join(' · ');
  const also = byVoice.get(g.voice).filter((i) => i !== ei);
  const cd = g.check_detail ?? {};
  const art = g.artifact ? tx(`art_${g.artifact}`) : '';
  el.hidden = false;
  el.innerHTML = `
    <button class="x" aria-label="${esc(tx('close'))}">×</button>
    <div class="sc">${esc(when(g.date))} &nbsp;·&nbsp; ${esc(placeOf(g))}</div>
    <h3>${esc(voiceName(g))}</h3>
    <div class="role">${esc(roleOf(g))}</div>
    ${q ? `<div class="kind">${esc(tx('their_words'))}</div><blockquote>“${esc(q)}”</blockquote>` : ''}
    ${showOrig ? `<p class="orig"><span class="sc">${esc(origLabel)}</span> “${esc(orig)}”</p>` : ''}
    ${g.quote_is_translation ? `<p class="mt">${esc(tx('only_translation'))}</p>` : ''}
    ${TR && tr.quote_kind === 'translated' ? `<p class="mt">${esc(tx('translated_note'))}</p>` : ''}
    <p class="saw"><span class="sc">${esc(tx('summary_label'))}</span> ${esc(sawOf(g))}</p>
    ${(notesOf.get(g.id) ?? []).map((x) => `<p class="note"><span class="sc">${esc(x.route.title)}</span> ${esc(x.note)}</p>`).join('')}
    <dl>
      <dt>${esc(tx('form'))}</dt><dd>${esc(art)}${g.mediated_by ? `, ${esc(tx('via', { x: tr.mediated_by ?? mediated(g.mediated_by) }))}` : `, ${esc(tx('first_hand'))}`}</dd>
      ${g.caveat ? `<dt>${esc(tx('caveat'))}</dt><dd>${esc(tr.caveat ?? g.caveat)}</dd>` : ''}
    </dl>
    ${VERDICT.has(g.check) ? `<div class="sc">${esc(tx('verification'))}</div>
    <p class="verdict v-${esc(g.check)}">${esc(tx(`v_${g.check}`))}</p>
    <dl>
      ${cd.against ? `<dt>${esc(tx('checked_against'))}</dt><dd class="brk">${esc(cd.against)}</dd>` : ''}
      ${cd.method ? `<dt>${esc(tx('method'))}</dt><dd>${esc(tr.check_method ?? cd.method)}</dd>` : ''}
      ${cd.issue ? `<dt>${esc(tx('check_note'))}</dt><dd>${esc(tr.check_issue ?? cd.issue)}</dd>` : ''}
      ${cd.on ? `<dt>${esc(tx('checked_on'))}</dt><dd>${esc(when(cd.on))}</dd>` : ''}
    </dl>` : ''}
    ${also.length ? `<div class="also"><div class="sc">${esc(tx('elsewhere'))}</div>${also.map((i) =>
      `<a href="#" data-e="${i}">${esc(byDate[i].date.slice(0, 4))}</a>`).join(' ')}</div>` : ''}
    <div class="sc">${esc(tx(g.sources_from_note ? 'sources_from_note' : 'sources'))}</div>
    <ol class="src">${g.sources.map((x) => `<li>${x.url ? `<a href="${esc(x.url)}" target="_blank" rel="noopener">${x.label ? `${esc(x.label)}<br>` : ''}<span>${esc(x.url)}</span></a>` : esc(x.label ?? '')}${x.page ? ` · ${esc(x.page)}` : ''}${x.archived ? ` <a class="arch" href="${esc(x.archived)}" target="_blank" rel="noopener">${esc(tx('archived_copy'))}</a>` : ''}</li>`).join('') || `<li>${esc(tx('none_recorded'))}</li>`}</ol>
    <div class="edit">
      <a href="#" class="share">${esc(tx('share_voice'))}</a>
      <a href="${esc(editUrl(g.path))}" target="_blank" rel="noopener">${esc(tx('edit_record'))}</a>
      ${TR && tr.path ? `<a href="${esc(editUrl(tr.path))}" target="_blank" rel="noopener">${esc(tx('edit_translation'))}</a>` : ''}
      <span>${esc(tx('edit_hint', { x: g.id }))}</span>
    </div>`;
  el.querySelector('.x').onclick = () => { sheet(null); relayout(); };
  el.querySelector('.share').onclick = (e) => { e.preventDefault(); share(ei, e.currentTarget); };
  el.querySelectorAll('[data-e]').forEach((a) => (a.onclick = (e) => { e.preventDefault(); goTo(+a.dataset.e); }));
  el.scrollTop = 0;
}
// ---------------------------------------------------------------- unwinding: a voice comes off the spiral as upright type
const DPR = () => renderer.getPixelRatio();
const wide = () => innerWidth > 900;
const sheetOpen = () => !$('sheet').hidden && wide();
const areaOf = () => { const l = wide() ? 340 : 0; return { l, r: innerWidth - (sheetOpen() ? Math.min(430, innerWidth - 48) + 34 : 0) }; };
// greedy word wrap of one voice's text: a heading line (NAME, YEAR:), then the words
function wrapVoice(ei, maxW, fem) {
  const arr = [...entries[ei].text], hLen = [...(entries[ei].text.match(/^.*?, \d{4}: /)?.[0] ?? '')].length;
  const adv = (ch) => (glyphs.get(ch)?.adv ?? 0.5) * fem;
  const pos = new Array(arr.length), widths = [0];
  let i = 0, x = 0, line = 0;
  while (i < arr.length) {
    if (arr[i] === ' ') { x += adv(' '); i++; if (i === hLen && x > 0) { line++; widths[line] = 0; x = 0; } continue; }
    let j = i, w = 0;
    while (j < arr.length && arr[j] !== ' ') w += adv(arr[j++]);
    if (x > 0 && x + w > maxW) { line++; widths[line] = 0; x = 0; }
    for (let k = i; k < j; k++) { pos[k] = [x, line]; x += adv(arr[k]); }
    widths[line] = x; i = j;
  }
  return { pos, lines: line + 1, w: Math.max(...widths), hLen };
}
let cur = null, old = null;          // the voice unwound now, and the one winding back
// where the camera was before the first voice was opened; closing the voice rewinds the camera there,
// in step with the letters going home
let restView = null;
const WIND_BACK = 1.8;               // seconds for the letters, and the camera, to go back
const capEl = $('cap');
function layoutVoice(ei) {
  const { l, r } = areaOf(), aw = r - l;
  const split = aw >= 980;                                  // wide: type on the left, his face on the right
  const maxW = Math.min(600, split ? aw * 0.5 - 40 : aw - (wide() ? 96 : 32));
  let fem = wide() ? 25 : 19, W, para, lineH, gap, capH, top;
  for (;;) {
    W = wrapVoice(ei, maxW, fem); lineH = fem * 1.38; gap = fem * 0.45;
    para = W.lines * lineH + gap;
    capEl.style.width = `${Math.max(W.w, Math.min(maxW, 340))}px`;
    capH = capEl.offsetHeight;
    if (para + 18 + capH <= innerHeight - (wide() ? 90 : 120) || fem <= 14) break;
    fem--;
  }
  const blockW = Math.max(W.w, Math.min(maxW, 340));
  const left = split ? l + Math.max(56, aw * 0.25 - blockW / 2) : l + (aw - blockW) / 2;
  top = wide() ? Math.max(60, (innerHeight - para - 18 - capH) / 2) : Math.max(56, innerHeight - 16 - capH - 18 - para);
  // where his face should sit: right half when split, else in the space the type leaves
  const spot = split ? [l + aw * 0.75, innerHeight / 2] : wide() ? [l + aw / 2, Math.max(80, top / 2)] : [innerWidth / 2, Math.max(70, (top + 40) / 2)];
  const e = entries[ei], N = Math.max(1, e.i1 - e.i0);
  for (let k = e.i0; k <= e.i1; k++) {
    const ci = inst[k].idx - e.first, [x, line] = W.pos[ci] ?? [0, 0];
    const yCss = top + fem + line * lineH + (line > 0 ? gap : 0);
    flatAttr.array.set([left + x, innerHeight - yCss, (k - e.i0) / N, ci < W.hLen ? 1 : e.kind === 'summary' ? 2 : 0], k * 4);
  }
  flatAttr.clearUpdateRanges(); flatAttr.addUpdateRange(e.i0 * 4, (e.i1 - e.i0 + 1) * 4); flatAttr.needsUpdate = true;
  capEl.style.left = `${left}px`; capEl.style.top = `${top + para + 18}px`; capEl.style.width = `${blockW}px`;
  return { ei, fem, left, top, w: blockW, h: para + 18 + capH, spot, off: [0, 0] };
}
function unwind(ei) {
  if (cur?.ei === ei) return;
  const back = old?.ei === ei ? old.u : 0;
  if (cur) { old = { ...cur, u: cur.u }; } else if (old?.ei === ei) old = null;
  cur = ei >= 0 ? { ...layoutVoice(ei), u: back } : null;
  document.body.classList.toggle('unwound', !!cur);
  if (!cur) capEl.style.pointerEvents = 'none';      // it fades out with the paper; hidden once the letters are home
  else if (!old && uniforms.uClear.value < 0.05) rect = rectOf(cur);
}
const rectOf = (c) => [c.left - 40, c.top - 34, c.left + c.w + 40, c.top + c.h + 26];
let rect = [0, 0, 0, 0];

function caption(ei) {
  const g = byDate[ei], guided = document.body.dataset.mode === 'read', stop = guided ? reading.stops[gi] : null;
  capEl.hidden = false; capEl.style.pointerEvents = '';
  capEl.innerHTML = guided
    ? `<div class="sc">${esc(reading.title)} &nbsp;·&nbsp; ${esc(tx('i_of_n', { i: gi + 1, n: reading.stops.length }))}</div>
      <div class="meta">${esc(when(g.date))} · ${esc(placeOf(g))} · ${esc(roleOf(g))}${entries[ei].kind === 'summary' ? ` · <b class="ours">${esc(tx('summary_note'))}</b>` : ''}</div>
      ${stop.note ? `<p class="note">${esc(stop.note)}</p>` : ''}
      <div class="acts"><a href="#" id="c-prev">${esc(tx('prev'))}</a><a href="#" id="c-next">${esc(tx('next'))}</a>
        <a href="#" id="c-pause">${esc(tx(paused ? 'go_on' : 'pause'))}</a><a href="#" id="c-src">${esc(tx('sources_n', { n: g.sources.length }))}</a><a href="#" id="c-share">${esc(tx('share'))}</a><a href="#" id="c-stop">${esc(tx('stop'))}</a></div>
      <div class="prog"><i id="c-prog"></i></div>`
    : `<div class="sc">${esc(when(g.date))} &nbsp;·&nbsp; ${esc(placeOf(g))}</div>
      <div class="meta">${esc(roleOf(g))}${entries[ei].kind === 'summary' ? ` · <b class="ours">${esc(tx('summary_note'))}</b>` : ''}</div>
      <div class="acts"><a href="#" id="c-src">${esc(tx('sources_notes'))}</a><a href="#" id="c-share">${esc(tx('share'))}</a><a href="#" id="c-x">${esc(tx('wind_back'))}</a></div>`;
  const on = (id, f) => $(id) && ($(id).onclick = (ev) => { ev.preventDefault(); f(); });
  on('c-prev', () => startGuided(gi - 1));
  on('c-next', () => startGuided(gi + 1));
  on('c-pause', () => { paused = !paused; $('c-pause').textContent = tx(paused ? 'go_on' : 'pause'); if (!paused && dwell) dwell.t0 = performance.now() - dwell.done; });
  on('c-src', () => { if (guided && !paused) $('c-pause').click(); sheet(ei); relayout(); });
  on('c-share', () => { if (guided && !paused) $('c-pause').click(); share(ei, $('c-share')); });
  on('c-stop', () => { stopGuided(); windBack(); });
  on('c-x', () => windBack());
}
// keep the unwound voice where it is when the sheet slides in or out, or the window changes: shift it, don't re-set it
function relayout() {
  if (!cur) return;
  const was = cur, c = layoutVoice(cur.ei);
  cur = { ...c, u: was.u, off: [was.left + was.off[0] - c.left, c.top - was.top + was.off[1]] };
}
addEventListener('resize', () => { if (cur) relayout(); });

// the address bar and the tab's name follow the open voice, so the page can be shared or bookmarked at that voice
const linkOf = (g) => `${location.origin}${location.pathname}${location.search}#${g.id}`;
const hashEi = () => { try { return idxOf.get(decodeURIComponent(location.hash.slice(1))); } catch { return undefined; } };
function address(ei) {
  const g = byDate[ei];
  document.title = g ? `${voiceName(g)}, ${g.date.slice(0, 4)} · ${tx('mast_title')}` : tx('page_title');
  try { history.replaceState(null, '', g ? `#${g.id}` : location.pathname + location.search); } catch { /* a sandboxed frame */ }
}
// share one voice: the phone's own share sheet where there is one, otherwise its link is copied
async function share(ei, a) {
  const g = byDate[ei], url = linkOf(g), q = quoteOf(g), who = `${voiceName(g)}, ${g.date.slice(0, 4)}`;
  const text = q ? `“${q.length > 220 ? `${q.slice(0, 217).trimEnd()}…` : q}” ${who}` : who;
  if (navigator.share && matchMedia('(pointer: coarse)').matches) {
    try { await navigator.share({ text, url }); return; } catch (e) { if (e?.name === 'AbortError') return; }
  }
  let ok = false;
  try { await navigator.clipboard.writeText(url); ok = true; } catch {
    const ta = Object.assign(document.createElement('textarea'), { value: url });
    ta.style.cssText = 'position:fixed;opacity:0'; document.body.append(ta); ta.select();
    try { ok = document.execCommand('copy'); } catch { /* nothing left to try */ }
    ta.remove();
  }
  if (!ok) { prompt(tx('copy_prompt'), url); return; }
  a.dataset.was ??= a.textContent;
  a.textContent = tx('link_copied'); clearTimeout(a._t); a._t = setTimeout(() => { a.textContent = a.dataset.was; }, 1800);
}
function select(ei, open = false) {
  uniforms.uSel.value = ei; tip.hidden = true;
  address(ei);
  if (ei < 0) { sheet(null); unwind(-1); return; }
  if (!restView) restView = flight ? { ...flight.to } : { x: view.x, y: view.y, s: view.s, rot: view.rot };
  sheet(open ? ei : null);
  caption(ei);
  unwind(ei);
}
function flyTo(x, y, s, rot, dur) {
  const dist = Math.hypot(x - view.x, y - view.y);
  const mid = Math.min(view.s, s, Math.max(fitS, (Math.min(innerWidth, innerHeight) * 0.9) / Math.max(1, dist)));
  flight = { from: { ...view }, to: { x, y, s, rot: view.rot + wrap(rot - view.rot) }, mid, t0: performance.now(), dur: dur ?? 1600 + Math.min(1600, dist * 1.2) };
}
// the view that puts world point (x, y) at screen point (sx, sy)
const viewFor = (x, y, sx, sy, s, rot) => {
  const dx = (sx - innerWidth / 2) / s, dy = -(sy - innerHeight / 2) / s, c = Math.cos(rot), si = Math.sin(rot);
  return [x - (c * dx - si * dy), y - (si * dx + c * dy)];
};
const posOf = (ci, lift = 0.33 * em) => at(charPhi[ci], lift);
const home = () => flyTo(homeX(), 0, fitS, 0, 1900);
// close the open voice: its letters wind back onto the spiral while the camera returns to where the reader was
function windBack() {
  if (!cur) return false;
  select(-1);
  if (restView) flyTo(restView.x, restView.y, restView.s, restView.rot, WIND_BACK * 1000);
  return true;
}
// show where on his face the voice came from: a little closer, upright, beside the unwound type
function showSpot(ei, s = fitS * 1.7) {
  const e = entries[ei], [x, y] = posOf(Math.floor((e.first + e.last) / 2));
  const [vx, vy] = viewFor(x, y, ...cur.spot, s, 0);
  flyTo(vx, vy, s, 0);
}
function goTo(ei) {
  stopGuided(); leaveTitle(); closeMenuOnPhone();
  select(ei);
  showSpot(ei);
}

// ---------------------------------------------------------------- threads to follow: guided readings
const famousInOrder = byDate.map((g, i) => (famous.has(g.id) ? i : -1)).filter((i) => i >= 0);
let reading = { title: tx('famous_title'), stops: famousInOrder.map((i) => ({ ei: i })) };
let gi = -1, paused = false, dwell = null;
function readRoute(r) {
  reading = { title: r.title, line: r.question ?? r.line, stops: r.stops.map((st) => ({ ei: idxOf.get(st.id), note: st.note })).filter((x) => x.ei != null) };
  startGuided(0);
}
function readList(title, list) { reading = { title, stops: list.map((i) => ({ ei: i })) }; startGuided(0); }
function startGuided(i = 0) {
  leaveTitle(); closeMenuOnPhone();
  document.body.dataset.mode = 'read';
  const N = reading.stops.length;
  gi = (i + N) % N;
  const ei = reading.stops[gi].ei;
  select(ei);
  showSpot(ei);
  // time to read it: about 16 letters a second once it has settled, and a breath
  dwell = { t0: performance.now() + 2200, len: 2600 + ((entries[ei].last - entries[ei].first) / 16) * 1000, done: 0 };
  drawRoutes();
}
function stopGuided() {
  if (document.body.dataset.mode !== 'read') return;
  document.body.dataset.mode = 'free';
  dwell = null; paused = false;
  if (cur) caption(cur.ei); else capEl.hidden = true;
  drawRoutes();
}
function leaveTitle() { document.body.classList.add('begun'); if (document.body.dataset.mode === 'intro') document.body.dataset.mode = 'free'; }

// 10 November 1938: the voices of the weeks after his death, lit across his face and read with the best-known
// names first (the curated opening), then people, institutions and newspapers; voices without their own words last
const NOV10 = tx('nov10_title');
const funeral = (() => {
  const lead = new Map(FUNERAL_LEAD.map((id, k) => [id, k]));
  const tier = (g) => (lead.has(g.id) ? (quoteOf(g) ? 0 : 0.5) : (quoteOf(g) ? 1 : 4) + (g.voice_type === 'person' ? 0 : g.voice_type === 'press' ? 2 : 1));
  return byDate.map((g, i) => i).filter((i) => byDate[i].era === 'funeral')
    .sort((p, q) => tier(byDate[p]) - tier(byDate[q]) || (lead.get(byDate[p].id) ?? 0) - (lead.get(byDate[q].id) ?? 0) || p - q);
})();
function readFuneral() { if (lit?.label !== NOV10) light(NOV10, funeral); readList(NOV10, funeral); }

// ---------------------------------------------------------------- the index: search, threads, light-ups, names
const routesEl = $('routes');
function drawRoutes() {
  const cur = document.body.dataset.mode === 'read' ? reading.title : null;
  routesEl.innerHTML = [`<li class="day${cur === NOV10 ? ' on' : ''}"><a href="#" data-r="day"><b>${esc(NOV10)}</b><span>${esc(tx('nov10_line'))}</span><i>${esc(tx('n_voices', { n: funeral.length }))}</i></a></li>`,
    ...ROUTES.map((r, k) => `<li class="${cur === r.title ? 'on' : ''}"><a href="#" data-r="${k}"><b>${esc(r.title)}</b><span>${esc(r.question ?? r.line ?? '')}</span><i>${esc(tx('n_voices', { n: r.stops.length }))}</i></a></li>`),
    `<li class="${cur === tx('famous_title') ? 'on' : ''}"><a href="#" data-r="all"><b>${esc(tx('famous_title'))}</b><span>${esc(tx('famous_line'))}</span><i>${esc(tx('n_voices', { n: famousInOrder.length }))}</i></a></li>`].join('');
  routesEl.querySelectorAll('a').forEach((a) => (a.onclick = (e) => {
    e.preventDefault();
    if (a.dataset.r === 'day') readFuneral();
    else if (a.dataset.r === 'all') { reading = { title: tx('famous_title'), stops: famousInOrder.map((i) => ({ ei: i })) }; startGuided(0); }
    else readRoute(ROUTES[+a.dataset.r]);
  }));
}
drawRoutes();

// light-ups: categories that mark their voices across the face
const markAttr = new THREE.InstancedBufferAttribute(new Float32Array(n), 1);
geo.setAttribute('iMark', markAttr);
const DOMAIN = (d) => d && tx(`dom_${d}`), KIND = (k) => ['press', 'institution', 'collective'].includes(k) && tx(`kind_${k}`);
const decade = (g) => +`${g.date.slice(0, 3)}0`;
const tally = (f) => { const m = new Map(); byDate.forEach((g, i) => { const k = f(g); if (k) (m.get(k) ?? m.set(k, []).get(k)).push(i); }); return m; };
const GROUPS = [
  [tx('grp_who'), [...tally((g) => DOMAIN(g.domain)), ...tally((g) => KIND(g.voice_type))]],
  [tx('grp_when'), [...tally((g) => tx(+g.date.slice(0, 4) < 1923 ? 'era_war' : +g.date.slice(0, 4) < 1939 ? 'era_republic' : 'era_after'))]],
  [tx('grp_decade'), [...tally(decade)].sort((a, c) => a[0] - c[0]).map(([d, l]) => [decadeLabel(d), l])],
  [tx('grp_from'), [...tally((g) => placeOf(g))].sort((a, c) => c[1].length - a[1].length).slice(0, 18)],
];
let lit = null;
function light(label, list) {
  if (lit && lit.label === label) { label = null; list = null; }
  lit = label ? { label, list } : null;
  const set = new Set(list ?? []);
  inst.forEach((it, k) => { markAttr.array[k] = set.has(it.entry) ? 1 : 0; });
  markAttr.needsUpdate = true;
  uniforms.uLit.value = lit ? 1 : 0;
  $('lit').hidden = !lit;
  if (lit) {
    $('lit').innerHTML = `<span class="sc">${esc(tx('lit'))}</span> <b>${esc(label)}</b> · ${esc(tx('n_voices', { n: list.length }))}
      <a href="#" id="lit-read">${esc(tx('read_them'))}</a> <a href="#" id="lit-x">${esc(tx('clear'))}</a>`;
    $('lit-read').onclick = (e) => { e.preventDefault(); readList(label, list); };
    $('lit-x').onclick = (e) => { e.preventDefault(); light(lit.label); };
  }
  document.querySelectorAll('#cats a').forEach((a) => a.classList.toggle('on', lit?.label === a.dataset.l));
}
$('cats').innerHTML = GROUPS.map(([head, items]) => `<div class="grp"><div class="sc">${head}</div>${items.map(([l, list]) =>
  `<a href="#" data-l="${esc(l)}">${esc(l)} <i>${list.length}</i></a>`).join('')}</div>`).join('');
const catMap = new Map(GROUPS.flatMap(([, items]) => items));
$('cats').querySelectorAll('a').forEach((a) => (a.onclick = (e) => { e.preventDefault(); leaveTitle(); light(a.dataset.l, catMap.get(a.dataset.l)); }));

// names: the famous, A to Z by surname
const sur = (nm) => nm.replace(/\s+(MP|Pasha|Paşa|Bey)$/i, '').split(/\s+/).at(-1);
const names = [...new Map(famousInOrder.map((i) => [voiceName(byDate[i]), i])).entries()].sort((a, c) => sur(a[0]).localeCompare(sur(c[0]), TR ? 'tr' : 'en'));
$('names').innerHTML = names.map(([nm, i]) => `<li><a href="#" data-e="${i}">${esc(nm)}</a> <i>${byDate[i].date.slice(0, 4)}</i></li>`).join('');
$('names').querySelectorAll('a').forEach((a) => (a.onclick = (e) => { e.preventDefault(); goTo(+a.dataset.e); }));

// search: any voice, country or role
const fold = (t) => t.normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/ı/g, 'i').toLowerCase();
const hay = byDate.map((g) => fold(`${voiceName(g)} ${g.voice} ${g.country_now} ${placeOf(g)} ${g.country} ${g.role} ${roleOf(g)} ${g.date.slice(0, 4)}`));
$('q').addEventListener('input', () => {
  const q = fold($('q').value.trim());
  const res = q.length < 2 ? [] : hay.map((t, i) => (q.split(/\s+/).every((w) => t.includes(w)) ? i : -1)).filter((i) => i >= 0);
  $('results').innerHTML = res.slice(0, 40).map((i) => `<li><a href="#" data-e="${i}">${esc(voiceName(byDate[i]))}</a> <i>${byDate[i].date.slice(0, 4)} · ${esc(placeOf(byDate[i]))}</i></li>`).join('')
    + (res.length > 1 ? `<li class="more"><a href="#" id="q-lit">${esc(tx('light_all', { n: res.length }))}</a></li>` : '') + (q.length >= 2 && !res.length ? `<li class="more">${esc(tx('nothing'))}</li>` : '');
  $('results').querySelectorAll('[data-e]').forEach((a) => (a.onclick = (e) => { e.preventDefault(); goTo(+a.dataset.e); }));
  if ($('q-lit')) $('q-lit').onclick = (e) => { e.preventDefault(); light(`“${$('q').value.trim()}”`, res); };
});

// the index drawer on phones
const closeMenuOnPhone = () => { if (innerWidth <= 900) document.body.classList.remove('menu'); };
$('menu').onclick = () => document.body.classList.toggle('menu');
$('read').onclick = (e) => { e?.preventDefault(); readRoute(ROUTES[0]); };
$('explore').onclick = (e) => { e.preventDefault(); leaveTitle(); };
$('hello-read').onclick = (e) => { e.preventDefault(); readRoute(ROUTES[0]); };
$('hello-day').onclick = (e) => { e.preventDefault(); readFuneral(); };
addEventListener('keydown', (e) => {
  if (e.target.closest('input')) return;
  if (e.key === 'ArrowRight' || e.key === 'ArrowLeft') {
    e.preventDefault(); leaveTitle();
    const d = e.key === 'ArrowRight' ? 1 : -1;
    if (gi < 0) { const c = charAt(view.x, view.y); const here = c >= 0 ? charEntry[c] : 0; gi = reading.stops.findIndex((x) => x.ei >= here) - (d > 0 ? 1 : 0); }
    startGuided(gi + d);
  } else if (e.key === 'Escape') { stopGuided(); if (!windBack()) home(); }
  else if (e.key === '/') { e.preventDefault(); document.body.classList.add('menu'); $('q').focus(); }
  else if (e.key === '+' || e.key === '=') zoomAt(innerWidth / 2, innerHeight / 2, 1.5);
  else if (e.key === '-') zoomAt(innerWidth / 2, innerHeight / 2, 1 / 1.5);
});

// ---------------------------------------------------------------- the loop
const t0 = performance.now(), REVEAL = hashEi() != null ? 1400 : 7500;   // a link to one voice: no long opening
const ease = (t) => (t < 0.5 ? 4 * t * t * t : 1 - (-2 * t + 2) ** 3 / 2);
let prev = performance.now(), booted = false;
function frame(now) {
  const dt = Math.min(0.05, (now - prev) / 1000), rdt = Math.min(0.3, (now - prev) / 1000); prev = now;
  // the thread writes itself, centre outward, at an even pace in radius
  const rt = Math.min(1, (now - t0) / REVEAL);
  const revealChar = Math.floor(L.out.length * rt * rt);
  uniforms.uReveal.value = rt >= 1 ? n + 1e6 : revealChar;
  const st = $('stylus');
  if (rt < 1) {
    const ci = Math.min(L.out.length - 1, revealChar);
    const [sx, sy] = toScreen(...posOf(ci, 0.3 * em));
    st.hidden = false; st.style.transform = `translate(${sx}px, ${sy}px)`;
    $('year').textContent = byDate[charEntry[ci]].date.slice(0, 4);
  } else st.hidden = true;

  if (morph) { const t = Math.min(1, (now - morph.t0) / 2600); uniforms.uMix.value = ease(t); if (t >= 1) morph = null; }

  if (flight) {
    const t = Math.min(1, (now - flight.t0) / flight.dur), e = ease(t), f = flight;
    const ls = t < 0.5 ? Math.log(f.from.s) + (Math.log(f.mid) - Math.log(f.from.s)) * ease(t * 2)
      : Math.log(f.mid) + (Math.log(f.to.s) - Math.log(f.mid)) * ease(t * 2 - 1);
    view.s = Math.exp(ls);
    view.x = f.from.x + (f.to.x - f.from.x) * e; view.y = f.from.y + (f.to.y - f.from.y) * e;
    view.rot = f.from.rot + (f.to.rot - f.from.rot) * e;
    if (t >= 1) flight = null;
  } else if (document.body.dataset.mode !== 'read') {
    // free: the page turns so the text you are reading stands upright, and rights itself as you step back
    const u = smooth(9, 22, rowPx());
    const target = Math.hypot(view.x, view.y) > 3 * h ? wrap(uprightAt(view.x, view.y)) * u : 0;
    view.rot += wrap(target - view.rot) * Math.min(1, dt * 2.5);
  }

  // unwinding and winding back
  if (cur) cur.u = Math.min(1, cur.u + rdt / 2.2);
  if (old) { old.u = Math.max(0, old.u - rdt / WIND_BACK); if (old.u <= 0) old = null; }
  if (!cur && !old) { if (!capEl.hidden && capEl.style.pointerEvents === 'none') capEl.hidden = true; if (!flight) restView = null; }
  if (cur) for (const k of [0, 1]) cur.off[k] *= Math.max(0, 1 - dt * 5);
  uniforms.uFE.value.set(cur?.ei ?? -1, old?.ei ?? -1);
  uniforms.uFU.value.set(cur?.u ?? 0, old?.u ?? 0);
  uniforms.uFEm.value.set(cur?.fem ?? 20, old?.fem ?? 20);
  uniforms.uFOff.value.set(cur?.off[0] ?? 0, cur?.off[1] ?? 0, old?.off[0] ?? 0, old?.off[1] ?? 0);
  {
    // the paper clearing: full while a voice is open; while one winds back it holds until the last letters are
    // nearly home (the first letters of the text leave last), then fades as they land
    const target = cur ? 1 : old ? Math.min(1, old.u / 0.3) : 0;
    uniforms.uClear.value += (target - uniforms.uClear.value) * Math.min(1, rdt * (cur ? 3 : 8));   // real time, also on slow phones
  }
  if (cur) { const to = rectOf(cur); rect = rect.map((v, k) => v + (to[k] - v) * Math.min(1, dt * 6)); }
  { const d = DPR(); uniforms.uRect.value.set(rect[0] * d, (innerHeight - rect[3]) * d, rect[2] * d, (innerHeight - rect[1]) * d); uniforms.uDpr.value = d; }
  uniforms.uScreen.value.set(innerWidth, innerHeight);
  if (cur) capEl.style.transform = `translate(${cur.off[0]}px, ${-cur.off[1]}px)`;
  capEl.style.opacity = cur ? Math.min(1, Math.max(0, cur.u * 2.4 - 1.4)) : 0;
  // guided: hold while it is read, then on to the next
  if (dwell && document.body.dataset.mode === 'read') {
    if (paused) dwell.t0 = now - dwell.done;
    dwell.done = Math.max(0, now - dwell.t0);
    const pr = $('c-prog'); if (pr) pr.style.width = `${Math.min(100, (dwell.done / dwell.len) * 100)}%`;
    if (dwell.done >= dwell.len) { dwell = null; startGuided(gi + 1); }
  }
  if (rt >= 1 && !flight && document.body.dataset.mode !== 'read') {
    const c = charAt(view.x, view.y);
    $('year').textContent = rowPx() > 9 && c >= 0 ? byDate[charEntry[c]].date.slice(0, 4) : '';
  }

  const w = innerWidth / view.s / 2, hh = innerHeight / view.s / 2;
  camera.left = -w; camera.right = w; camera.top = hh; camera.bottom = -hh;
  camera.position.set(view.x, view.y, 5); camera.rotation.set(0, 0, view.rot);
  camera.updateProjectionMatrix();
  uniforms.uPx.value = view.s * em; uniforms.uViewS.value = view.s; uniforms.uViewRot.value = view.rot;
  renderer.render(scene, camera);
  if (!booted) { booted = true; document.body.classList.add('ready'); $('fail').hidden = true; }
  requestAnimationFrame(frame);
}
requestAnimationFrame(frame);
document.body.dataset.mode = 'intro';
// a link to one voice (#record-id) opens straight on that voice
if (hashEi() != null) { goTo(hashEi()); document.fonts?.ready.then(() => cur && relayout()); }
addEventListener('hashchange', () => { const ei = hashEi(); if (ei != null && ei !== cur?.ei) goTo(ei); });
if (import.meta.env.DEV) window.__thread = { renderer, mesh, view, uniforms, inst, h, em, n, state: () => ({ cur: cur && cur.u, old: old && old.u, restView }) };
