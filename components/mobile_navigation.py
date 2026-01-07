"""
Mobile Navigation Component
Bottom navigation bar for mobile devices
"""

import streamlit as st
from pathlib import Path


def render_mobile_bottom_nav():
    """
    Render bottom navigation bar for mobile devices
    Only shows on screens < 768px
    """
    st.markdown(
        """
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
                padding: 8px 4px;
                text-decoration: none;
                color: #666;
                min-height: 48px;
                transition: all 0.2s;
                -webkit-tap-highlight-color: transparent;
            }
            
            .mobile-nav-item:active {
                background: rgba(0,0,0,0.05);
                transform: scale(0.95);
                transition: transform 0.1s ease;
            }
            
            .mobile-nav-item.active {
                position: relative;
            }
            
            .mobile-nav-item.active::before {
                content: '';
                position: absolute;
                top: 0;
                left: 0;
                right: 0;
                height: 3px;
                background: var(--primary, #2D7DF6);
                border-radius: 0 0 3px 3px;
            }
            
            [data-theme="dark"] .mobile-nav-item {
                color: #b0b0b0;
            }
            
            [data-theme="dark"] .mobile-nav-item:active {
                background: rgba(255,255,255,0.1);
            }
            
            .mobile-nav-item.active {
                color: #2D7DF6;
                font-weight: 600;
            }
            
            [data-theme="dark"] .mobile-nav-item.active {
                color: #64b5f6;
            }
            
            .mobile-nav-item.active .mobile-nav-icon {
                transform: scale(1.1);
                transition: transform 0.2s ease;
            }
            
            .mobile-nav-icon {
                font-size: 24px;
                margin-bottom: 4px;
                transition: transform 0.2s ease;
            }
            
            .mobile-nav-label {
                font-size: 11px;
                font-weight: 500;
            }
            
            /* Add padding to main content to prevent overlap */
            .main .block-container {
                padding-bottom: calc(80px + env(safe-area-inset-bottom)) !important;
                padding-left: 1rem !important;
                padding-right: 1rem !important;
            }
            
            /* Better spacing for 7 items */
            .mobile-nav-item {
                flex: 1 1 calc(14.28% - 4px);
                min-width: 0;
            }
            
            .mobile-nav-label {
                font-size: 10px;
                line-height: 1.2;
                margin-top: 2px;
            }
            
            .mobile-nav-icon {
                font-size: 22px;
                margin-bottom: 2px;
            }
        }
        
        /* Hide on desktop */
        @media (min-width: 769px) {
            #mobile-bottom-nav {
                display: none !important;
            }
        }
        </style>
        
        <nav id="mobile-bottom-nav">
            <a href="/" class="mobile-nav-item" id="nav-home">
                <div class="mobile-nav-icon">🏠</div>
                <div class="mobile-nav-label">Trang chủ</div>
            </a>
            <a href="/pages/07_💊_Drug_Database.py" class="mobile-nav-item" id="nav-drugs">
                <div class="mobile-nav-icon">💊</div>
                <div class="mobile-nav-label">Thuốc</div>
            </a>
            <a href="/pages/01_📊_Scores.py" class="mobile-nav-item" id="nav-scores">
                <div class="mobile-nav-icon">📊</div>
                <div class="mobile-nav-label">Tính toán</div>
            </a>
            <a href="/pages/09_🫁_Critical_Care.py" class="mobile-nav-item" id="nav-critical">
                <div class="mobile-nav-icon">🫁</div>
                <div class="mobile-nav-label">Hồi sức</div>
            </a>
            <a href="/pages/06_🩺_Diagnosis.py" class="mobile-nav-item" id="nav-diagnosis">
                <div class="mobile-nav-icon">🩺</div>
                <div class="mobile-nav-label">Chẩn đoán</div>
            </a>
            <a href="/pages/10_🧭_Decision_Support.py" class="mobile-nav-item" id="nav-support">
                <div class="mobile-nav-icon">🧭</div>
                <div class="mobile-nav-label">Hỗ trợ</div>
            </a>
            <a href="#" class="mobile-nav-item" id="nav-menu" onclick="toggleMobileMenu(event)">
                <div class="mobile-nav-icon">☰</div>
                <div class="mobile-nav-label">Menu</div>
            </a>
        </nav>
        
        <script>
        // Highlight active nav item based on current page
        (function() {
            const currentPath = window.location.pathname;
            const navItems = {
                '/': 'nav-home',
                '/pages/00_🏠_Main_Menu.py': 'nav-home',
                '/pages/07_💊_Drug_Database.py': 'nav-drugs',
                '/pages/02_💊_Antibiotics.py': 'nav-drugs',
                '/pages/21_💊_Pill_Identifier.py': 'nav-drugs',
                '/pages/08_📊_TDM.py': 'nav-drugs',
                '/pages/01_📊_Scores.py': 'nav-scores',
                '/pages/05_🔬_Labs_and_Calculators.py': 'nav-scores',
                '/pages/09_🫁_Critical_Care.py': 'nav-critical',
                '/pages/03_🫁_Ventilator.py': 'nav-critical',
                '/pages/04_📋_Protocols.py': 'nav-critical',
                '/pages/15_📋_Guidelines_Tracker.py': 'nav-critical',
                '/pages/10_📰_Medical_News.py': 'nav-critical',
                '/pages/06_🩺_Diagnosis.py': 'nav-diagnosis',
                '/pages/16_📖_Disease_Encyclopedia.py': 'nav-diagnosis',
                '/pages/13_🏷️_ICD10_Lookup.py': 'nav-diagnosis',
                '/pages/12_📚_In_Depth_Articles.py': 'nav-diagnosis',
                '/pages/19_👥_Patient_Education.py': 'nav-diagnosis',
                '/pages/10_🧭_Decision_Support.py': 'nav-support',
                '/pages/09_🤖_AI_Assistant.py': 'nav-support',
                '/pages/11_💉_Vaccination.py': 'nav-support'
            };
            
            // Find matching nav item
            let activeId = 'nav-home'; // default
            for (const [path, id] of Object.entries(navItems)) {
                if (currentPath.includes(path) || currentPath === path) {
                    activeId = id;
                    break;
                }
            }
            
            // Add active class
            const activeEl = document.getElementById(activeId);
            if (activeEl) {
                activeEl.classList.add('active');
            }
        })();
        
        // Toggle mobile menu (sidebar)
        function toggleMobileMenu(event) {
            event.preventDefault();
            const sidebar = document.querySelector('[data-testid="stSidebar"]');
            if (sidebar) {
                const isExpanded = sidebar.getAttribute('aria-expanded') === 'true';
                sidebar.setAttribute('aria-expanded', (!isExpanded).toString());
                
                // Add overlay
                if (!isExpanded) {
                    const overlay = document.createElement('div');
                    overlay.id = 'mobile-sidebar-overlay';
                    overlay.style.cssText = `
                        position: fixed;
                        top: 0;
                        left: 0;
                        right: 0;
                        bottom: 0;
                        background: rgba(0, 0, 0, 0.5);
                        z-index: 998;
                    `;
                    overlay.onclick = () => toggleMobileMenu(event);
                    document.body.appendChild(overlay);
                } else {
                    const overlay = document.getElementById('mobile-sidebar-overlay');
                    if (overlay) overlay.remove();
                }
            }
        }
        
        // Prevent default link behavior and use Streamlit navigation
        document.querySelectorAll('#mobile-bottom-nav a').forEach(link => {
            link.addEventListener('click', function(e) {
                if (this.id === 'nav-menu') {
                    return; // Let toggleMobileMenu handle it
                }
                
                e.preventDefault();
                const href = this.getAttribute('href');
                if (href && href !== '#') {
                    // Use Streamlit's navigation
                    window.location.href = href;
                }
            });
        });
        
        // Haptic feedback (if supported)
        function hapticFeedback() {
            if ('vibrate' in navigator) {
                navigator.vibrate(10);
            }
        }
        
        // Add haptic feedback to nav items
        document.querySelectorAll('#mobile-bottom-nav .mobile-nav-item').forEach(item => {
            item.addEventListener('touchstart', hapticFeedback, { passive: true });
        });
        </script>
        """,
        unsafe_allow_html=True
    )


def render_mobile_swipe_gestures():
    """
    Add swipe gesture support for mobile navigation
    Enhanced with sidebar toggle and pull-to-refresh
    """
    st.markdown(
        """
        <script>
        // Enhanced swipe gesture detection for mobile
        (function() {
            let touchStartX = 0;
            let touchEndX = 0;
            let touchStartY = 0;
            let touchEndY = 0;
            let touchStartTime = 0;
            let isScrolling = false;
            
            const minSwipeDistance = 50;
            const maxSwipeTime = 300; // ms
            const maxVerticalDistance = 30; // px - ignore if scrolling
            
            document.addEventListener('touchstart', function(e) {
                touchStartX = e.changedTouches[0].screenX;
                touchStartY = e.changedTouches[0].screenY;
                touchStartTime = Date.now();
                isScrolling = false;
            }, { passive: true });
            
            document.addEventListener('touchmove', function(e) {
                const deltaY = Math.abs(e.changedTouches[0].screenY - touchStartY);
                if (deltaY > maxVerticalDistance) {
                    isScrolling = true;
                }
            }, { passive: true });
            
            document.addEventListener('touchend', function(e) {
                touchEndX = e.changedTouches[0].screenX;
                touchEndY = e.changedTouches[0].screenY;
                const touchDuration = Date.now() - touchStartTime;
                
                if (touchDuration < maxSwipeTime && !isScrolling) {
                    handleSwipe();
                }
            }, { passive: true });
            
            function handleSwipe() {
                const deltaX = touchEndX - touchStartX;
                const deltaY = touchEndY - touchStartY;
                
                // Only handle horizontal swipes (ignore vertical scrolling)
                if (Math.abs(deltaX) > Math.abs(deltaY) && Math.abs(deltaX) > minSwipeDistance) {
                    const sidebar = document.querySelector('[data-testid="stSidebar"]');
                    
                    if (deltaX > 0) {
                        // Swipe right - open sidebar
                        if (sidebar && sidebar.getAttribute('aria-expanded') !== 'true') {
                            const menuBtn = document.querySelector('.mobile-drawer-trigger, #nav-menu');
                            if (menuBtn) {
                                menuBtn.click();
                            }
                        }
                    } else {
                        // Swipe left - close sidebar
                        if (sidebar && sidebar.getAttribute('aria-expanded') === 'true') {
                            const menuBtn = document.querySelector('.mobile-drawer-trigger, #nav-menu');
                            if (menuBtn) {
                                menuBtn.click();
                            }
                        }
                    }
                }
            }
        })();
        </script>
        """,
        unsafe_allow_html=True
    )


def render_mobile_optimizations():
    """
    Additional mobile optimizations
    """
    st.markdown(
        """
        <style>
        /* Mobile-specific optimizations */
        @media (max-width: 768px) {
            /* Prevent text selection on buttons (better UX) */
            button, .stButton>button {
                -webkit-user-select: none;
                -moz-user-select: none;
                -ms-user-select: none;
                user-select: none;
                -webkit-tap-highlight-color: transparent;
            }
            
            /* Better scrolling */
            body {
                -webkit-overflow-scrolling: touch;
            }
            
            /* Prevent zoom on input focus (iOS) */
            input, select, textarea {
                font-size: 16px !important;
            }
            
            /* Larger hit areas for small interactive elements */
            .stCheckbox, .stRadio {
                min-height: 48px;
                padding: 8px 0;
            }
            
            /* Better spacing for mobile */
            .stMarkdown {
                margin-bottom: 1rem;
            }
            
            /* Hide unnecessary elements on mobile */
            .stDeployButton {
                display: none;
            }
        }
        </style>
        """,
        unsafe_allow_html=True
    )

