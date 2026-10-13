"""Generate PWA manifest + service worker."""
from helpers import put

def generate_pwa(report, root, A, T):
    put(root, f"{A}/static/{A}/manifest.json", MANIFEST.replace("__T__", T))
    put(root, f"{A}/static/{A}/sw.js", SW)
    print("  PWA: manifest.json + service worker")

MANIFEST = """{
  "name": "__T__",
  "short_name": "__T__",
  "description": "__T__ - Data Management Portal",
  "start_url": "/",
  "display": "standalone",
  "background_color": "#080c18",
  "theme_color": "#b9f477",
  "icons": [{"src": "/static/portal/icon-192.png", "sizes": "192x192", "type": "image/png"}]
}"""

SW = """const CACHE = 'portal-v1';
const ASSETS = ['/static/portal/style.css','/static/portal/landing.css'];
self.addEventListener('install', e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(ASSETS)));
  self.skipWaiting();
});
self.addEventListener('activate', e => {
  e.waitUntil(caches.keys().then(keys => Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k)))));
  self.clients.claim();
});
self.addEventListener('fetch', e => {
  if (e.request.url.includes('/api/') || e.request.method !== 'GET') return;
  e.respondWith(caches.match(e.request).then(r => r || fetch(e.request).then(res => {
    const clone = res.clone();
    caches.open(CACHE).then(c => c.put(e.request, clone));
    return res;
  })));
});"""
