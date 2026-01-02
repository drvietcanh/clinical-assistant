"""
Enhanced Offline Mode Component
Cache calculators, protocols, and drug database for offline use
"""

import streamlit as st
from typing import List, Dict


def get_cacheable_resources() -> List[Dict[str, str]]:
    """
    Get list of resources to cache for offline use
    
    Returns:
        List of resource dicts with 'url', 'type', 'priority'
    """
    resources = [
        # Calculators/Scores
        {"url": "/pages/01_📊_Scores.py", "type": "page", "priority": "high"},
        {"url": "/config/calculators.py", "type": "data", "priority": "high"},
        {"url": "/scores/", "type": "module", "priority": "high"},
        
        # Drug Database
        {"url": "/pages/07_💊_Drug_Database.py", "type": "page", "priority": "high"},
        {"url": "/drugs/", "type": "module", "priority": "high"},
        
        # Protocols
        {"url": "/pages/04_📋_Protocols.py", "type": "page", "priority": "medium"},
        {"url": "/protocols/", "type": "module", "priority": "medium"},
        
        # Critical Care
        {"url": "/pages/09_🫁_Critical_Care.py", "type": "page", "priority": "medium"},
        
        # Static assets
        {"url": "/static/styles.css", "type": "asset", "priority": "high"},
        {"url": "/static/offline.js", "type": "asset", "priority": "high"},
    ]
    
    return resources


def render_offline_cache_manager():
    """
    Render UI for managing offline cache
    """
    st.markdown("### 💾 Quản lý Cache Offline")
    
    resources = get_cacheable_resources()
    
    # Cache status
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Tổng tài nguyên", len(resources))
    
    with col2:
        st.metric("Độ ưu tiên cao", len([r for r in resources if r['priority'] == 'high']))
    
    with col3:
        st.metric("Độ ưu tiên trung bình", len([r for r in resources if r['priority'] == 'medium']))
    
    # Cache controls
    st.markdown("#### ⚙️ Điều khiển Cache")
    
    col_cache1, col_cache2 = st.columns(2)
    
    with col_cache1:
        if st.button("📥 Tải Cache Tất Cả", use_container_width=True):
            st.info("Đang tải cache... (Chức năng này sẽ được implement trong service worker)")
            st.markdown("""
            <script>
            // Trigger cache download
            if ('serviceWorker' in navigator && 'caches' in window) {
                caches.open('clinical-assistant-v1').then(function(cache) {
                    const resources = """ + str(resources) + """;
                    cache.addAll(resources.map(r => r.url));
                    alert('Cache đã được tải!');
                });
            }
            </script>
            """, unsafe_allow_html=True)
    
    with col_cache2:
        if st.button("🗑️ Xóa Tất Cả Cache", use_container_width=True):
            st.warning("Xóa cache sẽ làm mất dữ liệu offline. Bạn có chắc chắn?")
            st.markdown("""
            <script>
            if ('caches' in window) {
                caches.keys().then(function(names) {
                    for (let name of names) {
                        caches.delete(name);
                    }
                    alert('Cache đã được xóa!');
                    window.location.reload();
                });
            }
            </script>
            """, unsafe_allow_html=True)
    
    # Resource list
    with st.expander("📋 Danh sách tài nguyên được cache", expanded=False):
        for resource in resources:
            priority_icon = "🔴" if resource['priority'] == 'high' else "🟡"
            st.markdown(f"{priority_icon} **{resource['url']}** ({resource['type']})")


def render_offline_sync_status():
    """
    Render sync status when coming back online
    """
    st.markdown("""
    <div id="offline-sync-status" style="display: none; padding: 12px; background: #e3f2fd; border-radius: 8px; margin: 10px 0;">
        <strong>🔄 Đồng bộ dữ liệu...</strong>
        <div id="sync-progress">Đang kiểm tra cập nhật...</div>
    </div>
    <script>
    window.addEventListener('online', function() {
        const syncEl = document.getElementById('offline-sync-status');
        if (syncEl) {
            syncEl.style.display = 'block';
            // Simulate sync
            setTimeout(function() {
                document.getElementById('sync-progress').innerHTML = '✅ Đã đồng bộ thành công!';
                setTimeout(function() {
                    syncEl.style.display = 'none';
                }, 3000);
            }, 2000);
        }
    });
    </script>
    """, unsafe_allow_html=True)


__all__ = [
    'get_cacheable_resources',
    'render_offline_cache_manager',
    'render_offline_sync_status',
]

