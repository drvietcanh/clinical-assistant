/**
 * Enhanced Service Worker for Clinical Assistant
 * Caches calculators, protocols, and drug database for offline use
 */

const CACHE_NAME = 'clinical-assistant-v2';
const CACHE_VERSION = '2.0.0';

// Resources to cache
const CACHE_RESOURCES = [
    // Static assets
    '/static/styles.css',
    '/static/offline.js',
    '/static/manifest.json',
    '/static/service-worker-enhanced.js',
    
    // Main pages
    '/',
    '/pages/01_📊_Scores.py',
    '/pages/04_📋_Protocols.py',
    '/pages/07_💊_Drug_Database.py',
    '/pages/09_🫁_Critical_Care.py',
    
    // Data files (if available)
    '/config/calculators.py',
    '/config/navigation_config.py',
];

// Cache strategies
const CACHE_STRATEGIES = {
    'network-first': ['/api/', '/data/'],
    'cache-first': ['/static/', '/config/'],
    'stale-while-revalidate': ['/pages/']
};

// Install event - cache resources
self.addEventListener('install', (event) => {
    console.log('[SW] Installing service worker...');
    
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then((cache) => {
                console.log('[SW] Caching resources...');
                return cache.addAll(CACHE_RESOURCES);
            })
            .then(() => {
                console.log('[SW] Service worker installed');
                return self.skipWaiting(); // Activate immediately
            })
            .catch((error) => {
                console.error('[SW] Cache installation failed:', error);
            })
    );
});

// Activate event - clean up old caches
self.addEventListener('activate', (event) => {
    console.log('[SW] Activating service worker...');
    
    event.waitUntil(
        caches.keys()
            .then((cacheNames) => {
                return Promise.all(
                    cacheNames
                        .filter((name) => name !== CACHE_NAME)
                        .map((name) => {
                            console.log('[SW] Deleting old cache:', name);
                            return caches.delete(name);
                        })
                );
            })
            .then(() => {
                console.log('[SW] Service worker activated');
                return self.clients.claim(); // Take control of all pages
            })
    );
});

// Fetch event - serve from cache, fallback to network
self.addEventListener('fetch', (event) => {
    // Skip non-GET requests
    if (event.request.method !== 'GET') {
        return;
    }
    
    // Skip cross-origin requests
    if (!event.request.url.startsWith(self.location.origin)) {
        return;
    }
    
    event.respondWith(
        caches.match(event.request)
            .then((cachedResponse) => {
                // Return cached version if available
                if (cachedResponse) {
                    console.log('[SW] Serving from cache:', event.request.url);
                    return cachedResponse;
                }
                
                // Otherwise fetch from network
                console.log('[SW] Fetching from network:', event.request.url);
                return fetch(event.request)
                    .then((response) => {
                        // Don't cache non-successful responses
                        if (!response || response.status !== 200 || response.type !== 'basic') {
                            return response;
                        }
                        
                        // Clone the response
                        const responseToCache = response.clone();
                        
                        // Cache the response
                        caches.open(CACHE_NAME)
                            .then((cache) => {
                                cache.put(event.request, responseToCache);
                            });
                        
                        return response;
                    })
                    .catch(() => {
                        // Network failed, return offline page if available
                        if (event.request.destination === 'document') {
                            return caches.match('/offline.html');
                        }
                        return new Response('Offline', { status: 503 });
                    });
            })
    );
});

// Message event - handle messages from main thread
self.addEventListener('message', (event) => {
    console.log('[SW] Message received:', event.data);
    
    if (event.data && event.data.type === 'SKIP_WAITING') {
        self.skipWaiting();
    }
    
    if (event.data && event.data.type === 'CACHE_URLS') {
        const urls = event.data.urls || [];
        caches.open(CACHE_NAME)
            .then((cache) => {
                return cache.addAll(urls);
            })
            .then(() => {
                event.ports[0].postMessage({ success: true });
            })
            .catch((error) => {
                event.ports[0].postMessage({ success: false, error: error.message });
            });
    }
});

// Background sync (if supported)
if ('sync' in self.registration) {
    self.addEventListener('sync', (event) => {
        console.log('[SW] Background sync:', event.tag);
        
        if (event.tag === 'sync-data') {
            event.waitUntil(syncData());
        }
    });
}

function syncData() {
    // Sync cached data when back online
    return fetch('/api/sync')
        .then((response) => response.json())
        .then((data) => {
            console.log('[SW] Data synced:', data);
        })
        .catch((error) => {
            console.error('[SW] Sync failed:', error);
        });
}

console.log('[SW] Enhanced service worker loaded');
