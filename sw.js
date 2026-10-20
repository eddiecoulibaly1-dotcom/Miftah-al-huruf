const CACHE='miftah-final-1.0.0';
const CORE=['./','./index.html','./app.js','./manifest.webmanifest','./data/ocr-index.json','./data/technical-text.txt','./assets/technique.pdf'];
self.addEventListener('install',e=>e.waitUntil(caches.open(CACHE).then(c=>c.addAll(CORE)).then(()=>self.skipWaiting())));
self.addEventListener('activate',e=>e.waitUntil(caches.keys().then(keys=>Promise.all(keys.filter(k=>k!==CACHE).map(k=>caches.delete(k)))).then(()=>self.clients.claim())));
self.addEventListener('fetch',e=>{if(e.request.method!=='GET')return;e.respondWith(caches.match(e.request).then(c=>c||fetch(e.request).then(r=>{if(r.ok&&new URL(e.request.url).origin===location.origin){const copy=r.clone();caches.open(CACHE).then(cache=>cache.put(e.request,copy))}return r}).catch(()=>caches.match('./index.html'))))});
