"""
Offline Support Component
Displays offline status indicator and PWA install prompt
"""

import streamlit as st
from pathlib import Path


def render_offline_indicator():
    """
    Render offline status indicator in the UI
    Shows when user is offline
    """
    st.markdown(
        """
        <div id="streamlit-offline-indicator" style="display: none;">
            <div style="background: #f44336; color: white; padding: 10px; text-align: center; 
                        position: fixed; top: 0; left: 0; right: 0; z-index: 10000; 
                        box-shadow: 0 2px 4px rgba(0,0,0,0.2);">
                ⚠️ Bạn đang offline - Một số tính năng có thể không khả dụng
            </div>
        </div>
        <script>
            // Update indicator based on online status
            function updateOfflineIndicator() {
                const indicator = document.getElementById('streamlit-offline-indicator');
                if (indicator) {
                    if (!navigator.onLine) {
                        indicator.style.display = 'block';
                    } else {
                        indicator.style.display = 'none';
                    }
                }
            }
            
            window.addEventListener('online', updateOfflineIndicator);
            window.addEventListener('offline', updateOfflineIndicator);
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
        
        **Tính năng offline:**
        - Cache static assets (CSS, JS, images)
        - Cache drug database đã tải
        - Cache calculator definitions
        - Offline fallback page khi mất kết nối
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
    Render current offline/online status
    """
    st.markdown(
        """
        <div id="pwa-status-indicator" style="padding: 10px; border-radius: 8px; margin: 10px 0;">
            <strong>Trạng thái kết nối:</strong> 
            <span id="pwa-status-text">Đang kiểm tra...</span>
        </div>
        <script>
            function updateStatus() {
                const statusEl = document.getElementById('pwa-status-indicator');
                const textEl = document.getElementById('pwa-status-text');
                
                if (navigator.onLine) {
                    statusEl.style.background = '#e8f5e9';
                    statusEl.style.color = '#2e7d32';
                    textEl.textContent = '✅ Online - Kết nối internet hoạt động';
                } else {
                    statusEl.style.background = '#ffebee';
                    statusEl.style.color = '#c62828';
                    textEl.textContent = '⚠️ Offline - Không có kết nối internet';
                }
            }
            
            window.addEventListener('online', updateStatus);
            window.addEventListener('offline', updateStatus);
            updateStatus();
            
            // Check service worker
            if ('serviceWorker' in navigator) {
                navigator.serviceWorker.ready.then(function(registration) {
                    if (registration) {
                        const statusText = document.getElementById('pwa-status-text');
                        if (statusText) {
                            statusText.textContent += ' | ✅ Service Worker đã sẵn sàng';
                        }
                    }
                });
            }
        </script>
        """,
        unsafe_allow_html=True
    )

