"""
Offline Support Component
Displays offline status indicator and PWA install prompt
"""

import streamlit as st
from pathlib import Path


def render_offline_indicator():
    """
    Render enhanced offline status indicator in the UI
    Shows when user is offline with better styling and information
    """
    st.markdown(
        """
        <div id="streamlit-offline-indicator" style="display: none;">
            <div style="
                background: linear-gradient(135deg, #f44336 0%, #d32f2f 100%); 
                color: white; 
                padding: 12px 20px; 
                text-align: center; 
                position: fixed; 
                top: 0; 
                left: 0; 
                right: 0; 
                z-index: 10000; 
                box-shadow: 0 4px 6px rgba(0,0,0,0.3);
                font-weight: 500;
                display: flex;
                align-items: center;
                justify-content: center;
                gap: 10px;
            ">
                <span style="font-size: 1.2em;">⚠️</span>
                <span>Bạn đang offline - Drug Database đã cache vẫn hoạt động</span>
            </div>
        </div>
        <style>
            /* Add padding to body when offline indicator is shown */
            body:has(#streamlit-offline-indicator[style*="display: block"]) {
                padding-top: 50px;
            }
        </style>
        <script>
            // Update indicator based on online status
            function updateOfflineIndicator() {
                const indicator = document.getElementById('streamlit-offline-indicator');
                if (indicator) {
                    if (!navigator.onLine) {
                        indicator.style.display = 'block';
                        // Add padding to main content
                        document.body.style.paddingTop = '50px';
                    } else {
                        indicator.style.display = 'none';
                        document.body.style.paddingTop = '0';
                    }
                }
            }
            
            window.addEventListener('online', () => {
                updateOfflineIndicator();
                // Show brief success message
                console.log('[PWA] Back online');
            });
            window.addEventListener('offline', () => {
                updateOfflineIndicator();
                console.log('[PWA] Gone offline');
            });
            updateOfflineIndicator();
        </script>
        """,
        unsafe_allow_html=True
    )


def render_pwa_info():
    """
    Render PWA installation info and status
    """
    with st.expander("📱 Cài Đặt Ứng Dụng (PWA)", expanded=False):
        st.markdown("""
        **Progressive Web App (PWA)** - Cài đặt ứng dụng để:
        - ✅ Hoạt động offline
        - ✅ Truy cập nhanh từ màn hình chính
        - ✅ Trải nghiệm như app native
        
        **Cách cài đặt:**
        1. **Chrome/Edge:** Click icon "Cài đặt" trong thanh địa chỉ
        2. **Safari (iOS):** Share → Add to Home Screen
        3. **Firefox:** Menu → Install
        
        **Tính năng offline (Enhanced):**
        - ✅ Cache static assets (CSS, JS, images)
        - ✅ Cache drug database đã tải (348+ thuốc)
        - ✅ Offline search trong drug database
        - ✅ Cache calculator definitions
        - ✅ Offline fallback page khi mất kết nối
        - ✅ Service Worker tự động cache dữ liệu
        
        **💡 Mẹo sử dụng offline:**
        - Truy cập Drug Database khi online để cache dữ liệu
        - Search và filters sẽ hoạt động với dữ liệu đã cache
        - Drug detail pages sẽ hiển thị nếu đã tải trước đó
        """)
        
        # Check if PWA is installed
        st.markdown(
            """
            <script>
            function checkPWAInstalled() {
                const isInstalled = window.matchMedia('(display-mode: standalone)').matches ||
                                   window.navigator.standalone === true;
                if (isInstalled) {
                    window.parent.postMessage({type: 'pwa-installed', value: true}, '*');
                }
            }
            checkPWAInstalled();
            </script>
            """,
            unsafe_allow_html=True
        )
        
        # Show cache status
        if st.button("🔄 Xóa Cache & Tải Lại", help="Xóa cache và tải lại service worker"):
            st.markdown(
                """
                <script>
                if ('serviceWorker' in navigator) {
                    navigator.serviceWorker.getRegistrations().then(function(registrations) {
                        for(let registration of registrations) {
                            registration.unregister();
                        }
                        caches.keys().then(function(names) {
                            for (let name of names) {
                                caches.delete(name);
                            }
                        });
                        alert('Cache đã được xóa. Trang sẽ tự động tải lại...');
                        window.location.reload();
                    });
                }
                </script>
                """,
                unsafe_allow_html=True
            )


def render_offline_status():
    """
    Render enhanced current offline/online status with cache information
    """
    st.markdown(
        """
        <div id="pwa-status-indicator" style="padding: 12px; border-radius: 8px; margin: 10px 0; border: 1px solid #e0e0e0;">
            <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 10px;">
                <div>
                    <strong>Trạng thái kết nối:</strong> 
                    <span id="pwa-status-text">Đang kiểm tra...</span>
                </div>
                <div id="pwa-cache-status" style="font-size: 0.9em; color: #666;">
                    <span id="pwa-cache-text">Cache: Đang kiểm tra...</span>
                </div>
            </div>
        </div>
        <script>
            function updateStatus() {
                const statusEl = document.getElementById('pwa-status-indicator');
                const textEl = document.getElementById('pwa-status-text');
                
                if (navigator.onLine) {
                    statusEl.style.background = '#e8f5e9';
                    statusEl.style.borderColor = '#4caf50';
                    textEl.innerHTML = '✅ <strong>Online</strong> - Kết nối internet hoạt động';
                } else {
                    statusEl.style.background = '#fff3cd';
                    statusEl.style.borderColor = '#ffc107';
                    textEl.innerHTML = '⚠️ <strong>Offline</strong> - Drug Database đã cache vẫn hoạt động';
                }
            }
            
            function updateCacheStatus() {
                const cacheTextEl = document.getElementById('pwa-cache-text');
                if (!cacheTextEl) return;
                
                if ('caches' in window) {
                    caches.keys().then(function(names) {
                        const hasCache = names.length > 0;
                        if (hasCache) {
                            cacheTextEl.innerHTML = '💾 Cache: <strong style="color: #4caf50;">Đã có</strong> (' + names.length + ' cache)';
                        } else {
                            cacheTextEl.innerHTML = '💾 Cache: <strong style="color: #ff9800;">Chưa có</strong>';
                        }
                    }).catch(function() {
                        cacheTextEl.innerHTML = '💾 Cache: Không xác định';
                    });
                } else {
                    cacheTextEl.innerHTML = '💾 Cache: Không hỗ trợ';
                }
            }
            
            window.addEventListener('online', updateStatus);
            window.addEventListener('offline', updateStatus);
            updateStatus();
            updateCacheStatus();
            
            // Check service worker
            if ('serviceWorker' in navigator) {
                navigator.serviceWorker.ready.then(function(registration) {
                    if (registration) {
                        const statusText = document.getElementById('pwa-status-text');
                        if (statusText && navigator.onLine) {
                            statusText.innerHTML += '<br><small style="font-weight: normal;">✅ Service Worker đã sẵn sàng - Offline mode enabled</small>';
                        }
                    }
                    updateCacheStatus();
                });
                
                // Also check after a delay
                setTimeout(updateCacheStatus, 2000);
            }
        </script>
        """,
        unsafe_allow_html=True
    )

