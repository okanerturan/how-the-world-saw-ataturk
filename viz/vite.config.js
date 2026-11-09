import { defineConfig } from 'vite';

// each build asks for its own data files, so a cached gazes.json from an older build is never mixed with newer code
export default defineConfig({
  define: { __DATA_VERSION__: JSON.stringify(Date.now().toString(36)) },
  base: './',
  build: { target: 'es2022' },
});
