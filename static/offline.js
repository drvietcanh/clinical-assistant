/**
 * Offline Support JavaScript
 * Registers service worker and handles offline functionality
 */

(function() {
  'use strict';
  
  // Check if service workers are supported
  if ('serviceWorker' in navigator) {
    // Register service worker
    window.addEventListener('load', () => {
      navigator.serviceWorker.register('/static/service-worker.js')
        .then((registration) => {
          console.log('[PWA] Service Worker registered:', registration.scope);
          
          // Check for updates
          registration.addEventListener('updatefound', () => {
            const newWorker = registration.installing;
            newWorker.addEventListener('statechange', () => {
              if (newWorker.state === 'installed' && navigator.serviceWorker.controller) {
                // New service worker available
                console.log('[PWA] New service worker available');
                showUpdateNotification();
              }
            });
          });
        })
        .catch((error) => {
          console.error('[PWA] Service Worker registration failed:', error);
        });
      
      // Listen for controller changes
      navigator.serviceWorker.addEventListener('controllerchange', () => {
        console.log('[PWA] Service Worker controller changed');
        window.location.reload();
      });
    });
  }
  
  // Online/Offline status indicator
  function createOfflineIndicator() {
    // Check if indicator already exists
    if (document.getElementById('pwa-offline-indicator')) {
      return;
    }
    
    const indicator = document.createElement('div');
    indicator.id = 'pwa-offline-indicator';
    indicator.style.cssText = `
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      background: #f44336;
      color: white;
      text-align: center;
      padding: 10px;
      z-index: 10000;
      display: none;
      font-weight: 500;
      box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    `;
    indicator.textContent = '⚠️ Bạn đang offline - Một số tính năng có thể không khả dụng';
    document.body.insertBefore(indicator, document.body.firstChild);
    
    // Update indicator based on online status
    function updateIndicator() {
      if (!navigator.onLine) {
        indicator.style.display = 'block';
      } else {
        indicator.style.display = 'none';
      }
    }
    
    window.addEventListener('online', updateIndicator);
    window.addEventListener('offline', updateIndicator);
    updateIndicator();
  }
  
  // Install prompt for PWA
  let deferredPrompt;
  
  window.addEventListener('beforeinstallprompt', (e) => {
    // Prevent the mini-infobar from appearing
    e.preventDefault();
    // Stash the event so it can be triggered later
    deferredPrompt = e;
    // Show install button (you can customize this)
    showInstallPrompt();
  });
  
  function showInstallPrompt() {
    // Create install button if it doesn't exist
    if (document.getElementById('pwa-install-button')) {
      return;
    }
    
    const installBtn = document.createElement('button');
    installBtn.id = 'pwa-install-button';
    installBtn.textContent = '📱 Cài đặt ứng dụng';
    installBtn.style.cssText = `
      position: fixed;
      bottom: 20px;
      right: 20px;
      background: #1976d2;
      color: white;
      border: none;
      padding: 12px 20px;
      border-radius: 25px;
      cursor: pointer;
      font-size: 14px;
      font-weight: 500;
      box-shadow: 0 4px 12px rgba(0,0,0,0.3);
      z-index: 9999;
      display: none;
    `;
    
    installBtn.addEventListener('click', async () => {
      if (deferredPrompt) {
        // Show the install prompt
        deferredPrompt.prompt();
        // Wait for the user to respond
        const { outcome } = await deferredPrompt.userChoice;
        console.log('[PWA] User choice:', outcome);
        // Clear the deferred prompt
        deferredPrompt = null;
        installBtn.style.display = 'none';
      }
    });
    
    document.body.appendChild(installBtn);
    
    // Show button after a delay
    setTimeout(() => {
      if (deferredPrompt) {
        installBtn.style.display = 'block';
      }
    }, 3000);
  }
  
  // Initialize when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
      createOfflineIndicator();
    });
  } else {
    createOfflineIndicator();
  }
  
  // Cache API responses (optional - for drug database, etc.)
  function cacheAPIResponse(url, data) {
    if ('caches' in window) {
      caches.open('clinical-assistant-v1').then((cache) => {
        const response = new Response(JSON.stringify(data), {
          headers: { 'Content-Type': 'application/json' }
        });
        cache.put(url, response);
      });
    }
  }
  
  // Expose cache function globally (for use in Streamlit)
  window.cacheAPIResponse = cacheAPIResponse;
  
  // Check if app is installed
  function isInstalled() {
    return window.matchMedia('(display-mode: standalone)').matches ||
           window.navigator.standalone === true;
  }
  
  // Expose utility functions
  window.PWA = {
    isInstalled: isInstalled,
    cacheAPIResponse: cacheAPIResponse,
    updateServiceWorker: () => {
      if ('serviceWorker' in navigator && navigator.serviceWorker.controller) {
        navigator.serviceWorker.controller.postMessage({ type: 'SKIP_WAITING' });
      }
    }
  };
  
  console.log('[PWA] Offline support initialized');
})();

