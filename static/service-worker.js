/**
 * Service Worker for Clinical Assistant PWA
 * Enables offline functionality and caching
 * 
 * Caching Strategy:
 * - Cache-first: Static assets (CSS, JS, images)
 * - Network-first: Dynamic content (Streamlit routes)
 * - Stale-while-revalidate: API responses
 */

const CACHE_NAME = 'clinical-assistant-v2'; // Updated version for Phase 1
const CALCULATOR_CACHE = 'calculator-cache-v1';
const PROTOCOL_CACHE = 'protocol-cache-v1';
const OFFLINE_URL = '/static/offline.html';

// Resources to cache on install
const STATIC_CACHE_URLS = [
  '/static/styles.css',
  '/static/offline.html',
  '/static/manifest.json',
  '/static/offline.js'
];

// Calculator-related URLs to cache
const CALCULATOR_CACHE_URLS = [
  // Calculator components
  '/components/calculator_enhancements.py',
  '/components/phase1_calculator_metadata.py',
  '/config/calculators.py'
];

// Protocol-related URLs to cache
const PROTOCOL_CACHE_URLS = [
  // Protocol components
  '/components/protocol_version.py',
  '/components/phase1_protocol_enhancer.py',
  '/components/evidence_badge.py',
  '/components/references.py',
  '/protocols/references_config.py',
  '/config/protocol_lists.py',
  '/config/protocol_routing.py'
];

// Install event - cache static resources
self.addEventListener('install', (event) => {
  console.log('[Service Worker] Installing Phase 1 enhanced version...');
  
  event.waitUntil(
    Promise.all([
      // Cache static assets
      caches.open(CACHE_NAME).then((cache) => {
        console.log('[Service Worker] Caching static assets');
        return cache.addAll(STATIC_CACHE_URLS);
      }),
      // Cache calculator resources
      caches.open(CALCULATOR_CACHE).then((cache) => {
        console.log('[Service Worker] Caching calculator resources');
        // Note: These are Python files, so we cache them when accessed
        // The actual caching happens on fetch
        return Promise.resolve();
      }),
      // Cache protocol resources
      caches.open(PROTOCOL_CACHE).then((cache) => {
        console.log('[Service Worker] Caching protocol resources');
        // Note: These are Python files, so we cache them when accessed
        // The actual caching happens on fetch
        return Promise.resolve();
      })
    ]).then(() => {
      // Force activation of new service worker
      return self.skipWaiting();
    }).catch((error) => {
      console.error('[Service Worker] Cache install failed:', error);
    })
  );
});

// Activate event - clean up old caches
self.addEventListener('activate', (event) => {
  console.log('[Service Worker] Activating...');
  
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames.map((cacheName) => {
          // Keep current caches, delete old ones
          if (cacheName !== CACHE_NAME && 
              cacheName !== CALCULATOR_CACHE && 
              cacheName !== PROTOCOL_CACHE) {
            console.log('[Service Worker] Deleting old cache:', cacheName);
            return caches.delete(cacheName);
          }
        })
      );
    })
    .then(() => {
      // Take control of all pages immediately
      return self.clients.claim();
    })
  );
});

// Fetch event - serve from cache or network
self.addEventListener('fetch', (event) => {
  const { request } = event;
  const url = new URL(request.url);
  
  // Skip non-GET requests
  if (request.method !== 'GET') {
    return;
  }
  
  // Skip cross-origin requests (unless needed)
  if (url.origin !== location.origin) {
    return;
  }
  
  // Handle different types of requests
  if (isStaticAsset(request.url)) {
    // Static assets: Cache-first strategy
    event.respondWith(cacheFirst(request));
  } else if (isCalculatorRequest(request.url)) {
    // Calculator requests: Cache calculator resources
    event.respondWith(calculatorCacheStrategy(request));
  } else if (isProtocolRequest(request.url)) {
    // Protocol requests: Cache protocol resources
    event.respondWith(protocolCacheStrategy(request));
  } else if (isStreamlitRoute(request.url)) {
    // Streamlit routes: Network-first with offline fallback
    event.respondWith(networkFirstWithOfflineFallback(request));
  } else {
    // Other requests: Network-first
    event.respondWith(networkFirst(request));
  }
});

/**
 * Check if URL is a static asset
 */
function isStaticAsset(url) {
  return url.includes('/static/') || 
         url.includes('.css') || 
         url.includes('.js') || 
         url.includes('.png') || 
         url.includes('.jpg') || 
         url.includes('.svg') ||
         url.includes('.ico');
}

/**
 * Check if URL is a Streamlit route
 */
function isStreamlitRoute(url) {
  return url.includes('/pages/') || 
         url.includes('/_stcore/') ||
         url === location.origin + '/' ||
         url === location.origin + '/index.html';
}

/**
 * Check if URL is a calculator-related request
 */
function isCalculatorRequest(url) {
  return url.includes('/Scores') ||
         url.includes('calculator') ||
         url.includes('/config/calculators');
}

/**
 * Check if URL is a protocol-related request
 */
function isProtocolRequest(url) {
  return url.includes('/Protocols') ||
         url.includes('protocol') ||
         url.includes('/config/protocol');
}

/**
 * Calculator cache strategy: Network-first, cache for offline
 */
async function calculatorCacheStrategy(request) {
  try {
    // Try network first
    const networkResponse = await fetch(request);
    if (networkResponse.ok) {
      // Cache successful responses
      const cache = await caches.open(CALCULATOR_CACHE);
      cache.put(request, networkResponse.clone());
    }
    return networkResponse;
  } catch (error) {
    console.log('[Service Worker] Calculator network failed, trying cache:', error);
    // Try cache
    const cachedResponse = await caches.match(request);
    if (cachedResponse) {
      return cachedResponse;
    }
    // Fallback to network-first strategy
    return networkFirst(request);
  }
}

/**
 * Protocol cache strategy: Network-first, cache for offline
 */
async function protocolCacheStrategy(request) {
  try {
    // Try network first
    const networkResponse = await fetch(request);
    if (networkResponse.ok) {
      // Cache successful responses
      const cache = await caches.open(PROTOCOL_CACHE);
      cache.put(request, networkResponse.clone());
    }
    return networkResponse;
  } catch (error) {
    console.log('[Service Worker] Protocol network failed, trying cache:', error);
    // Try cache
    const cachedResponse = await caches.match(request);
    if (cachedResponse) {
      return cachedResponse;
    }
    // Fallback to network-first strategy
    return networkFirst(request);
  }
}

/**
 * Cache-first strategy: Check cache first, fallback to network
 */
async function cacheFirst(request) {
  try {
    const cachedResponse = await caches.match(request);
    if (cachedResponse) {
      return cachedResponse;
    }
    
    const networkResponse = await fetch(request);
    if (networkResponse.ok) {
      const cache = await caches.open(CACHE_NAME);
      cache.put(request, networkResponse.clone());
    }
    return networkResponse;
  } catch (error) {
    console.error('[Service Worker] Cache-first failed:', error);
    // Return offline page for navigation requests
    if (request.mode === 'navigate') {
      return caches.match(OFFLINE_URL);
    }
    throw error;
  }
}

/**
 * Network-first strategy: Try network first, fallback to cache
 */
async function networkFirst(request) {
  try {
    const networkResponse = await fetch(request);
    if (networkResponse.ok) {
      const cache = await caches.open(CACHE_NAME);
      cache.put(request, networkResponse.clone());
    }
    return networkResponse;
  } catch (error) {
    console.log('[Service Worker] Network failed, trying cache:', error);
    const cachedResponse = await caches.match(request);
    if (cachedResponse) {
      return cachedResponse;
    }
    // Return offline page for navigation requests
    if (request.mode === 'navigate') {
      return caches.match(OFFLINE_URL);
    }
    throw error;
  }
}

/**
 * Network-first with offline fallback for Streamlit routes
 */
async function networkFirstWithOfflineFallback(request) {
  try {
    const networkResponse = await fetch(request);
    if (networkResponse.ok) {
      // Cache successful responses
      const cache = await caches.open(CACHE_NAME);
      cache.put(request, networkResponse.clone());
    }
    return networkResponse;
  } catch (error) {
    console.log('[Service Worker] Network failed, checking cache:', error);
    
    // Try cache first
    const cachedResponse = await caches.match(request);
    if (cachedResponse) {
      return cachedResponse;
    }
    
    // For navigation requests, return offline page
    if (request.mode === 'navigate') {
      const offlinePage = await caches.match(OFFLINE_URL);
      if (offlinePage) {
        return offlinePage;
      }
    }
    
    // Return error response
    return new Response('Offline - No cached content available', {
      status: 503,
      statusText: 'Service Unavailable',
      headers: { 'Content-Type': 'text/plain' }
    });
  }
}

/**
 * Message handler for cache management
 */
self.addEventListener('message', (event) => {
  if (event.data && event.data.type === 'SKIP_WAITING') {
    self.skipWaiting();
  }
  
  if (event.data && event.data.type === 'CACHE_URLS') {
    event.waitUntil(
      caches.open(CACHE_NAME).then((cache) => {
        return cache.addAll(event.data.urls);
      })
    );
  }
  
  if (event.data && event.data.type === 'CLEAR_CACHE') {
    event.waitUntil(
      caches.delete(CACHE_NAME).then(() => {
        return caches.open(CACHE_NAME);
      })
    );
  }
});

