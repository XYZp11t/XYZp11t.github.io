// @ts-check
import { defineConfig } from 'astro/config';

// https://astro.build/config
export default defineConfig({
  site: 'https://tu-dominio.com',
  base: '/',
  trailingSlash: 'ignore',
  build: {
    assets: 'assets',
  },
  vite: {
    ssr: {
      external: ['three']
    },
    optimizeDeps: {
      include: ['three']
    }
  },
  server: {
    port: 4321,
    host: true
  }
});
