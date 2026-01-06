"""
Mobile UI Components for Antibiotics Module
Mobile-optimized components: bottom navigation, FAB, filters sheet, etc.
"""

import streamlit as st
from typing import Optional


def render_mobile_bottom_nav(current_tab: str = "infection"):
    """
    Render bottom navigation bar for mobile devices
    Only shows on screens < 768px
    
    Args:
        current_tab: Current active tab ("infection", "drugs", "stewardship", "search")
    """
    
    nav_items = [
        {"icon": "🦠", "label": "Nhiễm trùng", "key": "infection"},
        {"icon": "💊", "label": "Thuốc", "key": "drugs"},
        {"icon": "🔄", "label": "Quản lý", "key": "stewardship"},
        {"icon": "🔍", "label": "Tìm kiếm", "key": "search"},
    ]
    
    st.markdown("""
    <style>
    /* Mobile Bottom Navigation */
    @media (max-width: 768px) {
        #mobile-bottom-nav {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background: white;
            border-top: 1px solid #e0e0e0;
            box-shadow: 0 -2px 8px rgba(0,0,0,0.1);
            z-index: 9999;
            display: flex;
            justify-content: space-around;
            align-items: center;
            padding: 8px 0;
            padding-bottom: max(8px, env(safe-area-inset-bottom));
            height: 60px;
        }
        
        [data-theme="dark"] #mobile-bottom-nav {
            background: #1e1e1e;
            border-top-color: #333;
        }
        
        .mobile-nav-item {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            flex: 1;
            padding: 4px 8px;
            text-decoration: none;
            color: #666;
            min-height: 48px;
            transition: all 0.2s;
            -webkit-tap-highlight-color: transparent;
            cursor: pointer;
            border: none;
            background: transparent;
        }
        
        .mobile-nav-item:active {
            background: rgba(0,0,0,0.05);
            transform: scale(0.95);
        }
        
        [data-theme="dark"] .mobile-nav-item {
            color: #b0b0b0;
        }
        
        [data-theme="dark"] .mobile-nav-item:active {
            background: rgba(255,255,255,0.1);
        }
        
        .mobile-nav-item.active {
            color: #1976D2;
            font-weight: 600;
        }
        
        [data-theme="dark"] .mobile-nav-item.active {
            color: #64b5f6;
        }
        
        .mobile-nav-icon {
            font-size: 22px;
            margin-bottom: 2px;
            transition: transform 0.2s ease;
        }
        
        .mobile-nav-item.active .mobile-nav-icon {
            transform: scale(1.1);
        }
        
        .mobile-nav-label {
            font-size: 10px;
            font-weight: 500;
            line-height: 1.2;
        }
        
        /* Add padding to main content to prevent overlap */
        .main .block-container {
            padding-bottom: 80px !important;
        }
        
        /* Hide on desktop */
        @media (min-width: 769px) {
            #mobile-bottom-nav {
                display: none !important;
            }
        }
    }
    </style>
    
    <div id="mobile-bottom-nav">
    """, unsafe_allow_html=True)
    
    for item in nav_items:
        active_class = "active" if item["key"] == current_tab else ""
        st.markdown(f"""
        <div class="mobile-nav-item {active_class}" onclick="window.scrollTo({{top: 0, behavior: 'smooth'}})">
            <div class="mobile-nav-icon">{item['icon']}</div>
            <div class="mobile-nav-label">{item['label']}</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)


def render_mobile_fab():
    """
    Render Floating Action Button (FAB) for mobile
    Opens Wizard when clicked
    """
    
    st.markdown("""
    <style>
    @media (max-width: 768px) {
        .mobile-fab-container {
            position: fixed;
            bottom: 80px; /* Above bottom nav */
            right: 20px;
            z-index: 9998;
        }
        
        .mobile-fab-button {
            width: 56px;
            height: 56px;
            border-radius: 50%;
            background: linear-gradient(135deg, #1976D2 0%, #1565C0 100%);
            color: white;
            box-shadow: 0 4px 12px rgba(25,118,210,0.4);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 28px;
            cursor: pointer;
            transition: all 0.3s ease;
            border: none;
            -webkit-tap-highlight-color: transparent;
            text-decoration: none;
        }
        
        .mobile-fab-button:active {
            transform: scale(0.9);
            box-shadow: 0 2px 8px rgba(25,118,210,0.3);
        }
    }
    
    @media (min-width: 769px) {
        .mobile-fab-container {
            display: none !important;
        }
    }
    </style>
    <div class="mobile-fab-container">
    """, unsafe_allow_html=True)
    
    # Use Streamlit button với custom styling
    fab_clicked = st.button("🧙", key="mobile_fab_wizard", help="Bắt đầu Trợ lý Chọn Kháng Sinh", use_container_width=False)
    
    if fab_clicked:
        st.session_state.show_wizard = True
        st.rerun()
    
    st.markdown("</div>", unsafe_allow_html=True)


def render_mobile_filters_button():
    """
    Render filter toggle button for mobile
    Returns True if filters should be shown in sheet
    """
    # Initialize state
    if 'show_mobile_filters' not in st.session_state:
        st.session_state.show_mobile_filters = False
    
    # Trigger button (only show on mobile)
    st.markdown("""
    <style>
    @media (min-width: 769px) {
        #mobile-filter-btn-container {
            display: none !important;
        }
    }
    </style>
    <div id="mobile-filter-btn-container">
    """, unsafe_allow_html=True)
    
    col_filter1, col_filter2 = st.columns([4, 1])
    with col_filter2:
        filter_icon = "✕" if st.session_state.show_mobile_filters else "🔍"
        if st.button(filter_icon, key="mobile_filter_toggle", use_container_width=True, help="Bộ lọc"):
            st.session_state.show_mobile_filters = not st.session_state.show_mobile_filters
            st.rerun()
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    return st.session_state.show_mobile_filters


def render_mobile_filters_sheet_content(protocols_collection, render_filters_func):
    """
    Render filters content inside bottom sheet
    
    Args:
        protocols_collection: ProtocolCollection to filter
        render_filters_func: Function to render filters sidebar
    
    Returns:
        Filters dict
    """
    if not st.session_state.get("show_mobile_filters", False):
        return None
    
    st.markdown("""
    <style>
    @media (max-width: 768px) {
        .mobile-filter-sheet-content {
            position: fixed;
            bottom: 60px; /* Above bottom nav */
            left: 0;
            right: 0;
            background: white;
            border-radius: 20px 20px 0 0;
            box-shadow: 0 -4px 20px rgba(0,0,0,0.2);
            z-index: 10000;
            max-height: 70vh;
            overflow-y: auto;
            padding: 20px 16px;
        }
        
        .mobile-filter-overlay {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 60px;
            background: rgba(0,0,0,0.5);
            z-index: 9999;
        }
        
        .mobile-filter-drag-handle {
            width: 40px;
            height: 4px;
            background: #ccc;
            border-radius: 2px;
            margin: 0 auto 16px;
        }
    }
    
    @media (min-width: 769px) {
        .mobile-filter-sheet-content,
        .mobile-filter-overlay {
            display: none !important;
        }
    }
    </style>
    
    <div class="mobile-filter-overlay" onclick="window.location.reload()"></div>
    <div class="mobile-filter-sheet-content">
        <div class="mobile-filter-drag-handle"></div>
    </div>
    """, unsafe_allow_html=True)
    
    # Render filters inside sheet
    with st.container():
        st.markdown("### 🔍 Bộ lọc")
        st.markdown("---")
        
        # Call the filters function
        filters = render_filters_func(protocols_collection)
        
        col_apply1, col_apply2 = st.columns(2)
        with col_apply1:
            if st.button("✅ Áp dụng", type="primary", use_container_width=True, key="mobile_apply_filters"):
                st.session_state.show_mobile_filters = False
                st.rerun()
        with col_apply2:
            if st.button("🗑️ Xóa", use_container_width=True, key="mobile_clear_filters"):
                st.session_state.show_mobile_filters = False
                # Clear filter state
                for key in ['filter_site', 'filter_severity', 'filter_setting', 'filter_source']:
                    if key in st.session_state:
                        del st.session_state[key]
                st.rerun()
    
    return filters


def inject_mobile_styles():
    """Inject comprehensive mobile styles"""
    
    st.markdown("""
    <style>
    /* Mobile-First Responsive Styles */
    @media (max-width: 768px) {
        /* Typography */
        h1 {
            font-size: 2em !important;
            line-height: 1.2 !important;
        }
        
        h2 {
            font-size: 1.5em !important;
        }
        
        h3 {
            font-size: 1.2em !important;
        }
        
        /* Buttons */
        .stButton > button {
            min-height: 48px !important;
            font-size: 1em !important;
            padding: 12px 16px !important;
            width: 100% !important;
            margin-bottom: 8px !important;
        }
        
        .stButton > button:active {
            transform: scale(0.98);
            opacity: 0.9;
        }
        
        /* Cards */
        .protocol-card,
        .regimen-card {
            width: 100% !important;
            margin-left: 0 !important;
            margin-right: 0 !important;
            padding: 16px !important;
            margin-bottom: 16px !important;
        }
        
        /* Columns - Stack on mobile */
        .stColumns {
            flex-direction: column !important;
        }
        
        .stColumns > div {
            width: 100% !important;
            margin-bottom: 12px !important;
        }
        
        /* Expanders */
        .stExpander {
            font-size: 0.95em !important;
        }
        
        /* Select boxes and inputs */
        .stSelectbox,
        .stMultiselect,
        .stTextInput {
            font-size: 1em !important;
        }
        
        /* Tabs */
        .stTabs {
            overflow-x: auto;
            -webkit-overflow-scrolling: touch;
        }
        
        .stTabs [role="tab"] {
            min-width: 100px;
            padding: 12px 16px;
            font-size: 0.95em;
        }
        
        /* Spacing adjustments */
        .main .block-container {
            padding-left: 1rem !important;
            padding-right: 1rem !important;
            padding-top: 1rem !important;
        }
        
        /* Hero section */
        .hero-section {
            padding: 20px 15px !important;
        }
        
        .hero-section h1 {
            font-size: 2em !important;
        }
        
        .hero-section p {
            font-size: 1em !important;
        }
    }
    
    /* Tablet adjustments */
    @media (min-width: 769px) and (max-width: 1024px) {
        .protocol-card,
        .regimen-card {
            padding: 18px !important;
        }
    }
    </style>
    """, unsafe_allow_html=True)


def inject_pwa_support():
    """
    Inject PWA support - Service worker registration and install prompt
    """
    
    st.markdown("""
    <link rel="manifest" href="/static/manifest.json">
    <meta name="theme-color" content="#4caf50">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="default">
    <meta name="apple-mobile-web-app-title" content="Antibiotics">
    
    <script>
    (function() {
        'use strict';
        
        // Register service worker
        if ('serviceWorker' in navigator) {
            window.addEventListener('load', function() {
                navigator.serviceWorker.register('/static/service-worker.js')
                    .then(function(registration) {
                        console.log('[PWA] Service Worker registered:', registration.scope);
                        
                        // Check for updates
                        registration.addEventListener('updatefound', function() {
                            const newWorker = registration.installing;
                            newWorker.addEventListener('statechange', function() {
                                if (newWorker.state === 'installed' && navigator.serviceWorker.controller) {
                                    // New service worker available
                                    if (confirm('Có phiên bản mới. Bạn có muốn cập nhật không?')) {
                                        newWorker.postMessage({ type: 'SKIP_WAITING' });
                                        window.location.reload();
                                    }
                                }
                            });
                        });
                    })
                    .catch(function(error) {
                        console.log('[PWA] Service Worker registration failed:', error);
                    });
            });
        }
        
        // Install prompt
        let deferredPrompt;
        window.addEventListener('beforeinstallprompt', function(e) {
            e.preventDefault();
            deferredPrompt = e;
            
            // Show install button
            const installButton = document.getElementById('pwa-install-button');
            if (installButton) {
                installButton.style.display = 'block';
                installButton.addEventListener('click', function() {
                    deferredPrompt.prompt();
                    deferredPrompt.userChoice.then(function(choiceResult) {
                        if (choiceResult.outcome === 'accepted') {
                            console.log('[PWA] User accepted install prompt');
                        } else {
                            console.log('[PWA] User dismissed install prompt');
                        }
                        deferredPrompt = null;
                        installButton.style.display = 'none';
                    });
                });
            }
        });
        
        // App installed
        window.addEventListener('appinstalled', function() {
            console.log('[PWA] App installed');
            const installButton = document.getElementById('pwa-install-button');
            if (installButton) {
                installButton.style.display = 'none';
            }
        });
    })();
    </script>
    
    <style>
    @media (max-width: 768px) {
        #pwa-install-button {
            position: fixed;
            bottom: 80px;
            left: 20px;
            background: linear-gradient(135deg, #4caf50 0%, #2e7d32 100%);
            color: white;
            border: none;
            border-radius: 25px;
            padding: 12px 20px;
            font-size: 0.9em;
            font-weight: 600;
            box-shadow: 0 4px 12px rgba(76,175,80,0.4);
            z-index: 9997;
            display: none;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        
        #pwa-install-button:active {
            transform: scale(0.95);
        }
    }
    </style>
    
    <button id="pwa-install-button" aria-label="Cài đặt ứng dụng">
        📱 Cài đặt
    </button>
    """, unsafe_allow_html=True)


def inject_offline_indicator():
    """
    Inject offline/online status indicator
    """
    
    st.markdown("""
    <style>
    @media (max-width: 768px) {
        .offline-indicator {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            background: #f44336;
            color: white;
            padding: 8px;
            text-align: center;
            font-size: 0.85em;
            font-weight: 500;
            z-index: 10003;
            transform: translateY(-100%);
            transition: transform 0.3s ease;
        }
        
        .offline-indicator.show {
            transform: translateY(0);
        }
        
        .offline-indicator.online {
            background: #4caf50;
        }
    }
    </style>
    
    <div class="offline-indicator" id="offline-indicator">
        <span id="offline-message">📡 Đang offline</span>
    </div>
    
    <script>
    (function() {
        'use strict';
        
        const indicator = document.getElementById('offline-indicator');
        const message = document.getElementById('offline-message');
        
        function updateOnlineStatus() {
            if (navigator.onLine) {
                indicator.classList.remove('show');
                indicator.classList.add('online');
                message.textContent = '✅ Đã kết nối lại';
                setTimeout(function() {
                    indicator.classList.remove('show', 'online');
                    message.textContent = '📡 Đang offline';
                }, 3000);
            } else {
                indicator.classList.add('show');
                indicator.classList.remove('online');
                message.textContent = '📡 Đang offline';
            }
        }
        
        window.addEventListener('online', updateOnlineStatus);
        window.addEventListener('offline', updateOnlineStatus);
        
        // Initial check
        updateOnlineStatus();
    })();
    </script>
    """, unsafe_allow_html=True)


def inject_swipe_gestures():
    """
    Inject JavaScript for swipe gesture support
    - Swipe left/right: Switch tabs
    - Swipe up: Open filters
    - Swipe down: Close filters/refresh
    """
    
    st.markdown("""
    <script>
    (function() {
        'use strict';
        
        let touchStartX = 0;
        let touchEndX = 0;
        let touchStartY = 0;
        let touchEndY = 0;
        const minSwipeDistance = 50;
        let isScrolling = false;
        
        // Detect if user is scrolling (to avoid accidental swipes)
        let scrollTimeout;
        document.addEventListener('scroll', function() {
            isScrolling = true;
            clearTimeout(scrollTimeout);
            scrollTimeout = setTimeout(function() {
                isScrolling = false;
            }, 150);
        }, { passive: true });
        
        document.addEventListener('touchstart', function(e) {
            touchStartX = e.changedTouches[0].screenX;
            touchStartY = e.changedTouches[0].screenY;
        }, { passive: true });
        
        document.addEventListener('touchend', function(e) {
            if (isScrolling) return;
            
            touchEndX = e.changedTouches[0].screenX;
            touchEndY = e.changedTouches[0].screenY;
            handleSwipe();
        }, { passive: true });
        
        function handleSwipe() {
            const deltaX = touchEndX - touchStartX;
            const deltaY = touchEndY - touchStartY;
            const absDeltaX = Math.abs(deltaX);
            const absDeltaY = Math.abs(deltaY);
            
            // Only handle swipes if horizontal movement is greater than vertical
            if (absDeltaX > absDeltaY && absDeltaX > minSwipeDistance) {
                // Horizontal swipe
                if (deltaX > 0) {
                    // Swipe right - go to previous tab
                    handleSwipeRight();
                } else {
                    // Swipe left - go to next tab
                    handleSwipeLeft();
                }
            } else if (absDeltaY > absDeltaX && absDeltaY > minSwipeDistance) {
                // Vertical swipe
                if (deltaY < 0) {
                    // Swipe up - open filters
                    handleSwipeUp();
                } else {
                    // Swipe down - close filters or refresh
                    handleSwipeDown();
                }
            }
        }
        
        function handleSwipeLeft() {
            // Switch to next tab
            const tabs = document.querySelectorAll('[role="tab"]');
            let activeIndex = -1;
            tabs.forEach((tab, index) => {
                if (tab.getAttribute('aria-selected') === 'true') {
                    activeIndex = index;
                }
            });
            
            if (activeIndex >= 0 && activeIndex < tabs.length - 1) {
                tabs[activeIndex + 1].click();
            }
        }
        
        function handleSwipeRight() {
            // Switch to previous tab
            const tabs = document.querySelectorAll('[role="tab"]');
            let activeIndex = -1;
            tabs.forEach((tab, index) => {
                if (tab.getAttribute('aria-selected') === 'true') {
                    activeIndex = index;
                }
            });
            
            if (activeIndex > 0) {
                tabs[activeIndex - 1].click();
            }
        }
        
        function handleSwipeUp() {
            // Open filters if not already open
            const filterButton = document.querySelector('[data-testid="baseButton-secondary"][aria-label*="filter"], [key*="mobile_filter"]');
            if (filterButton && !filterButton.classList.contains('active')) {
                filterButton.click();
            }
        }
        
        function handleSwipeDown() {
            // Close filters if open, or trigger refresh
            const filterSheet = document.querySelector('.mobile-filter-sheet-content');
            if (filterSheet && filterSheet.style.display !== 'none') {
                // Close filters
                const closeButton = document.querySelector('[key*="mobile_clear"], [key*="mobile_apply"]');
                if (closeButton) {
                    closeButton.click();
                }
            } else {
                // Could trigger pull-to-refresh here
                // For now, just scroll to top
                window.scrollTo({ top: 0, behavior: 'smooth' });
            }
        }
    })();
    </script>
    """, unsafe_allow_html=True)


def inject_pull_to_refresh():
    """
    Inject pull-to-refresh functionality
    Visual feedback when user pulls down to refresh
    """
    
    st.markdown("""
    <style>
    @media (max-width: 768px) {
        .pull-to-refresh-indicator {
            position: fixed;
            top: 0;
            left: 50%;
            transform: translateX(-50%);
            background: rgba(25, 118, 210, 0.9);
            color: white;
            padding: 12px 24px;
            border-radius: 0 0 20px 20px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.2);
            z-index: 10001;
            display: none;
            align-items: center;
            gap: 8px;
            font-size: 0.9em;
            font-weight: 500;
        }
        
        .pull-to-refresh-indicator.show {
            display: flex;
            animation: slideDown 0.3s ease;
        }
        
        @keyframes slideDown {
            from {
                transform: translateX(-50%) translateY(-100%);
            }
            to {
                transform: translateX(-50%) translateY(0);
            }
        }
    }
    </style>
    
    <div class="pull-to-refresh-indicator" id="pull-to-refresh-indicator">
        <span>🔄</span>
        <span>Đang làm mới...</span>
    </div>
    
    <script>
    (function() {
        'use strict';
        
        let touchStartY = 0;
        let touchCurrentY = 0;
        let isPulling = false;
        const pullThreshold = 80;
        const indicator = document.getElementById('pull-to-refresh-indicator');
        
        document.addEventListener('touchstart', function(e) {
            // Only enable pull-to-refresh when at top of page
            if (window.scrollY === 0) {
                touchStartY = e.touches[0].clientY;
                isPulling = false;
            }
        }, { passive: true });
        
        document.addEventListener('touchmove', function(e) {
            if (window.scrollY === 0 && touchStartY > 0) {
                touchCurrentY = e.touches[0].clientY;
                const pullDistance = touchCurrentY - touchStartY;
                
                if (pullDistance > 0 && pullDistance < pullThreshold * 2) {
                    isPulling = true;
                    // Show indicator
                    if (pullDistance > pullThreshold) {
                        indicator.classList.add('show');
                        indicator.querySelector('span:first-child').style.transform = 'rotate(180deg)';
                    } else {
                        indicator.classList.remove('show');
                        indicator.querySelector('span:first-child').style.transform = 'rotate(0deg)';
                    }
                }
            }
        }, { passive: true });
        
        document.addEventListener('touchend', function(e) {
            if (isPulling && touchStartY > 0) {
                const pullDistance = touchCurrentY - touchStartY;
                
                if (pullDistance > pullThreshold) {
                    // Trigger refresh
                    indicator.classList.add('show');
                    indicator.querySelector('span:first-child').style.animation = 'spin 1s linear infinite';
                    
                    // Reload page after short delay
                    setTimeout(function() {
                        window.location.reload();
                    }, 500);
                } else {
                    // Cancel refresh
                    indicator.classList.remove('show');
                }
            }
            
            touchStartY = 0;
            touchCurrentY = 0;
            isPulling = false;
        }, { passive: true });
        
        // Add spin animation
        const style = document.createElement('style');
        style.textContent = `
            @keyframes spin {
                from { transform: rotate(0deg); }
                to { transform: rotate(360deg); }
            }
        `;
        document.head.appendChild(style);
    })();
    </script>
    """, unsafe_allow_html=True)


def inject_card_swipe_actions():
    """
    Inject card swipe actions
    - Swipe left: Favorite/Unfavorite
    - Swipe right: Share (future)
    """
    
    st.markdown("""
    <style>
    @media (max-width: 768px) {
        .swipeable-card {
            position: relative;
            overflow: hidden;
            transition: transform 0.3s ease;
        }
        
        .swipeable-card.swiping {
            transition: none;
        }
        
        .swipe-action-left,
        .swipe-action-right {
            position: absolute;
            top: 0;
            bottom: 0;
            width: 80px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 24px;
            color: white;
            font-weight: 600;
            opacity: 0;
            transition: opacity 0.3s ease;
        }
        
        .swipe-action-left {
            left: 0;
            background: linear-gradient(90deg, #f44336, #e91e63);
        }
        
        .swipe-action-right {
            right: 0;
            background: linear-gradient(270deg, #2196f3, #1976d2);
        }
        
        .swipeable-card.swipe-left .swipe-action-left,
        .swipeable-card.swipe-right .swipe-action-right {
            opacity: 1;
        }
        
        .swipeable-card.swipe-left {
            transform: translateX(80px);
        }
        
        .swipeable-card.swipe-right {
            transform: translateX(-80px);
        }
    }
    </style>
    
    <script>
    (function() {
        'use strict';
        
        // Add swipe actions to cards
        function initCardSwipe(cardElement) {
            if (cardElement.classList.contains('swipe-initialized')) return;
            cardElement.classList.add('swipe-initialized', 'swipeable-card');
            
            // Add action buttons
            const leftAction = document.createElement('div');
            leftAction.className = 'swipe-action-left';
            leftAction.innerHTML = '⭐';
            leftAction.title = 'Yêu thích';
            
            const rightAction = document.createElement('div');
            rightAction.className = 'swipe-action-right';
            rightAction.innerHTML = '📤';
            rightAction.title = 'Chia sẻ';
            
            cardElement.appendChild(leftAction);
            cardElement.appendChild(rightAction);
            
            let touchStartX = 0;
            let touchCurrentX = 0;
            let isSwiping = false;
            const swipeThreshold = 50;
            
            cardElement.addEventListener('touchstart', function(e) {
                touchStartX = e.touches[0].clientX;
                isSwiping = false;
                cardElement.classList.add('swiping');
            }, { passive: true });
            
            cardElement.addEventListener('touchmove', function(e) {
                if (touchStartX === 0) return;
                
                touchCurrentX = e.touches[0].clientX;
                const deltaX = touchCurrentX - touchStartX;
                
                if (Math.abs(deltaX) > 10) {
                    isSwiping = true;
                    
                    // Prevent scrolling while swiping
                    e.preventDefault();
                    
                    // Apply transform
                    cardElement.style.transform = `translateX(${deltaX}px)`;
                    
                    // Show action based on direction
                    if (deltaX > swipeThreshold) {
                        cardElement.classList.add('swipe-right');
                        cardElement.classList.remove('swipe-left');
                    } else if (deltaX < -swipeThreshold) {
                        cardElement.classList.add('swipe-left');
                        cardElement.classList.remove('swipe-right');
                    } else {
                        cardElement.classList.remove('swipe-left', 'swipe-right');
                    }
                }
            }, { passive: false });
            
            cardElement.addEventListener('touchend', function(e) {
                if (!isSwiping) {
                    cardElement.classList.remove('swiping');
                    return;
                }
                
                const deltaX = touchCurrentX - touchStartX;
                
                if (Math.abs(deltaX) > swipeThreshold) {
                    if (deltaX > 0) {
                        // Swipe right - Share (future)
                        cardElement.classList.add('swipe-right');
                        setTimeout(() => {
                            // Reset
                            cardElement.style.transform = '';
                            cardElement.classList.remove('swipe-right', 'swiping');
                        }, 300);
                    } else {
                        // Swipe left - Favorite
                        cardElement.classList.add('swipe-left');
                        
                        // Trigger favorite action
                        const favoriteButton = cardElement.querySelector('[key*="favorite"], [key*="fav"]');
                        if (favoriteButton) {
                            favoriteButton.click();
                        } else {
                            // Visual feedback
                            leftAction.style.transform = 'scale(1.2)';
                            setTimeout(() => {
                                leftAction.style.transform = '';
                            }, 200);
                        }
                        
                        setTimeout(() => {
                            // Reset
                            cardElement.style.transform = '';
                            cardElement.classList.remove('swipe-left', 'swiping');
                        }, 500);
                    }
                } else {
                    // Reset if not enough swipe
                    cardElement.style.transform = '';
                    cardElement.classList.remove('swipe-left', 'swipe-right', 'swiping');
                }
                
                touchStartX = 0;
                touchCurrentX = 0;
                isSwiping = false;
            }, { passive: true });
        }
        
        // Initialize swipe for existing cards
        function initAllCards() {
            const cards = document.querySelectorAll('.protocol-card, .regimen-card, .regimen-card-mobile');
            cards.forEach(card => {
                initCardSwipe(card);
            });
        }
        
        // Initialize on load
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', initAllCards);
        } else {
            initAllCards();
        }
        
        // Re-initialize when new content is loaded (Streamlit reruns)
        const observer = new MutationObserver(function(mutations) {
            mutations.forEach(function(mutation) {
                mutation.addedNodes.forEach(function(node) {
                    if (node.nodeType === 1) {
                        const cards = node.querySelectorAll ? node.querySelectorAll('.protocol-card, .regimen-card, .regimen-card-mobile') : [];
                        cards.forEach(card => initCardSwipe(card));
                        
                        if (node.classList && (node.classList.contains('protocol-card') || node.classList.contains('regimen-card') || node.classList.contains('regimen-card-mobile'))) {
                            initCardSwipe(node);
                        }
                    }
                });
            });
        });
        
        observer.observe(document.body, {
            childList: true,
            subtree: true
        });
    })();
    </script>
    """, unsafe_allow_html=True)


def inject_quick_actions_menu():
    """
    Inject quick actions menu for long press on cards
    Shows context menu with: Favorite, Share, Copy, Print
    """
    
    st.markdown("""
    <style>
    @media (max-width: 768px) {
        .quick-actions-menu {
            position: fixed;
            bottom: 80px;
            left: 50%;
            transform: translateX(-50%);
            background: white;
            border-radius: 20px;
            box-shadow: 0 8px 24px rgba(0,0,0,0.3);
            z-index: 10002;
            display: none;
            flex-direction: column;
            min-width: 200px;
            padding: 8px;
            animation: slideUp 0.3s ease;
        }
        
        .quick-actions-menu.show {
            display: flex;
        }
        
        @keyframes slideUp {
            from {
                transform: translateX(-50%) translateY(20px);
                opacity: 0;
            }
            to {
                transform: translateX(-50%) translateY(0);
                opacity: 1;
            }
        }
        
        .quick-action-item {
            display: flex;
            align-items: center;
            gap: 12px;
            padding: 16px;
            border-radius: 12px;
            cursor: pointer;
            transition: background 0.2s;
            -webkit-tap-highlight-color: transparent;
        }
        
        .quick-action-item:active {
            background: #f5f5f5;
        }
        
        .quick-action-item .icon {
            font-size: 24px;
        }
        
        .quick-action-item .label {
            font-size: 1em;
            font-weight: 500;
            color: #333;
        }
        
        .quick-actions-overlay {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(0,0,0,0.5);
            z-index: 10001;
            display: none;
        }
        
        .quick-actions-overlay.show {
            display: block;
        }
    }
    </style>
    
    <div class="quick-actions-overlay" id="quick-actions-overlay"></div>
    <div class="quick-actions-menu" id="quick-actions-menu">
        <div class="quick-action-item" data-action="favorite">
            <span class="icon">⭐</span>
            <span class="label">Yêu thích</span>
        </div>
        <div class="quick-action-item" data-action="share">
            <span class="icon">📤</span>
            <span class="label">Chia sẻ</span>
        </div>
        <div class="quick-action-item" data-action="copy">
            <span class="icon">📋</span>
            <span class="label">Sao chép</span>
        </div>
        <div class="quick-action-item" data-action="print">
            <span class="icon">📄</span>
            <span class="label">In</span>
        </div>
    </div>
    
    <script>
    (function() {
        'use strict';
        
        const menu = document.getElementById('quick-actions-menu');
        const overlay = document.getElementById('quick-actions-overlay');
        let longPressTimer = null;
        let longPressTarget = null;
        const longPressDuration = 500; // ms
        
        function showMenu(x, y, targetCard) {
            menu.style.display = 'flex';
            overlay.classList.add('show');
            longPressTarget = targetCard;
            
            // Position menu near touch point
            const menuWidth = menu.offsetWidth;
            const menuHeight = menu.offsetHeight;
            const screenWidth = window.innerWidth;
            const screenHeight = window.innerHeight;
            
            let menuX = x - menuWidth / 2;
            let menuY = y - menuHeight - 20;
            
            // Keep menu on screen
            if (menuX < 10) menuX = 10;
            if (menuX + menuWidth > screenWidth - 10) menuX = screenWidth - menuWidth - 10;
            if (menuY < 10) menuY = y + 20;
            if (menuY + menuHeight > screenHeight - 100) menuY = screenHeight - menuHeight - 100;
            
            menu.style.left = menuX + 'px';
            menu.style.top = menuY + 'px';
            menu.style.transform = 'none';
            menu.classList.add('show');
        }
        
        function hideMenu() {
            menu.classList.remove('show');
            overlay.classList.remove('show');
            longPressTarget = null;
        }
        
        // Long press detection
        document.addEventListener('touchstart', function(e) {
            const card = e.target.closest('.protocol-card, .regimen-card, .regimen-card-mobile');
            if (!card) return;
            
            const touch = e.touches[0];
            longPressTimer = setTimeout(function() {
                // Haptic feedback (if available)
                if (navigator.vibrate) {
                    navigator.vibrate(50);
                }
                
                showMenu(touch.clientX, touch.clientY, card);
            }, longPressDuration);
        }, { passive: true });
        
        document.addEventListener('touchend', function(e) {
            if (longPressTimer) {
                clearTimeout(longPressTimer);
                longPressTimer = null;
            }
        }, { passive: true });
        
        document.addEventListener('touchmove', function(e) {
            if (longPressTimer) {
                clearTimeout(longPressTimer);
                longPressTimer = null;
            }
        }, { passive: true });
        
        // Close menu on overlay click
        overlay.addEventListener('touchstart', function(e) {
            hideMenu();
        }, { passive: true });
        
        // Handle menu actions
        menu.querySelectorAll('.quick-action-item').forEach(item => {
            item.addEventListener('touchstart', function(e) {
                e.stopPropagation();
                const action = this.getAttribute('data-action');
                
                switch(action) {
                    case 'favorite':
                        // Trigger favorite
                        const favButton = longPressTarget?.querySelector('[key*="favorite"], [key*="fav"]');
                        if (favButton) favButton.click();
                        break;
                    case 'share':
                        // Share functionality (future)
                        if (navigator.share && longPressTarget) {
                            const title = longPressTarget.querySelector('h3, h4')?.textContent || 'Protocol';
                            navigator.share({
                                title: title,
                                text: 'Xem phác đồ kháng sinh này',
                                url: window.location.href
                            }).catch(() => {});
                        }
                        break;
                    case 'copy':
                        // Copy to clipboard
                        if (longPressTarget) {
                            const text = longPressTarget.innerText;
                            navigator.clipboard.writeText(text).then(() => {
                                // Visual feedback
                                item.style.background = '#4caf50';
                                setTimeout(() => {
                                    item.style.background = '';
                                }, 300);
                            });
                        }
                        break;
                    case 'print':
                        // Print
                        window.print();
                        break;
                }
                
                hideMenu();
            }, { passive: true });
        });
    })();
    </script>
    """, unsafe_allow_html=True)
