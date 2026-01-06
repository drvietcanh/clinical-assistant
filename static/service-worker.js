/**
 * Service Worker for Antibiotics Module
 * Provides offline support and caching
 */

const CACHE_NAME = 'antibiotics-v1';
const OFFLINE_URL = '/offline.html';

// Resources to cache on install
const CACHE_RESOURCES = [
    '/',
    '/pages/02_💊_Antibiotics.py',
    '/offline.html',
    '/static/css/main.css',
    '/static/js/main.js'
];

// Install event - cache resources
self.addEventListener('install', function(event) {
    event.waitUntil(
        caches.open(CACHE_NAME).then(function(cache) {
            console.log('[Service Worker] Caching resources');
            return cache.addAll(CACHE_RESOURCES).catch(function(err) {
                console.log('[Service Worker] Cache addAll failed:', err);
            });
        })
    );
    self.skipWaiting(); // Activate immediately
});

// Activate event - clean up old caches
self.addEventListener('activate', function(event) {
    event.waitUntil(
        caches.keys().then(function(cacheNames) {
            return Promise.all(
                cacheNames.map(function(cacheName) {
                    if (cacheName !== CACHE_NAME) {
                        console.log('[Service Worker] Deleting old cache:', cacheName);
                        return caches.delete(cacheName);
                    }
                })
            );
        })
    );
    return self.clients.claim(); // Take control of all pages
});

// Fetch event - serve from cache, fallback to network
self.addEventListener('fetch', function(event) {
    // Skip non-GET requests
    if (event.request.method !== 'GET') {
        return;
    }
    
    // Skip cross-origin requests
    if (!event.request.url.startsWith(self.location.origin)) {
        return;
    }
    
    event.respondWith(
        caches.match(event.request).then(function(response) {
            // Return cached version if available
            if (response) {
                return response;
            }
            
            // Otherwise fetch from network
            return fetch(event.request).then(function(response) {
                // Don't cache non-successful responses
                if (!response || response.status !== 200 || response.type !== 'basic') {
                    return response;
                }
                
                // Clone response for caching
                const responseToCache = response.clone();
                
                caches.open(CACHE_NAME).then(function(cache) {
                    cache.put(event.request, responseToCache);
                });
                
                return response;
            }).catch(function(error) {
                // Network failed, return offline page for navigation requests
                if (event.request.mode === 'navigate') {
                    return caches.match(OFFLINE_URL);
                }
                
                // For other requests, return error
                throw error;
            });
        })
    );
});

// Message event - handle messages from main thread
self.addEventListener('message', function(event) {
    if (event.data && event.data.type === 'SKIP_WAITING') {
        self.skipWaiting();
    }
    
    if (event.data && event.data.type === 'CACHE_URLS') {
        event.waitUntil(
            caches.open(CACHE_NAME).then(function(cache) {
                return cache.addAll(event.data.urls);
            })
        );
    }
});
