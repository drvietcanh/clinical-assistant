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
                padding-bottom: 80px !important;
                padding-left: 1rem !important;
                padding-right: 1rem !important;
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
                <div class="mobile-nav-label">Thang điểm</div>
            </a>
            <a href="/pages/04_📋_Protocols.py" class="mobile-nav-item" id="nav-guidelines">
                <div class="mobile-nav-icon">📋</div>
                <div class="mobile-nav-label">Guideline</div>
            </a>
            <a href="#" class="mobile-nav-item" id="nav-personal" onclick="toggleMobileMenu(event)">
                <div class="mobile-nav-icon">⭐</div>
                <div class="mobile-nav-label">Tủ cá nhân</div>
            </a>
        </nav>
        
        <script>
        // Highlight active nav item based on current page
        (function() {
            const currentPath = window.location.pathname;
            const navItems = {
                '/': 'nav-home',
                '/pages/07_💊_Drug_Database.py': 'nav-drugs',
                '/pages/01_📊_Scores.py': 'nav-scores',
                '/pages/04_📋_Protocols.py': 'nav-guidelines'
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
        
        // Toggle mobile menu (for Tủ cá nhân)
        function toggleMobileMenu(event) {
            event.preventDefault();
            // Open sidebar (Streamlit's built-in sidebar)
            const sidebarToggle = document.querySelector('[data-testid="stSidebar"]');
            if (sidebarToggle) {
                // Trigger sidebar open
                window.parent.postMessage({type: 'streamlit:setFrameHeight', height: '100%'}, '*');
            }
        }
        
        // Prevent default link behavior and use Streamlit navigation
        document.querySelectorAll('#mobile-bottom-nav a').forEach(link => {
            link.addEventListener('click', function(e) {
                if (this.id === 'nav-personal') {
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
        </script>
        """,
        unsafe_allow_html=True
    )


def render_mobile_swipe_gestures():
    """
    Add swipe gesture support for mobile navigation
    """
    st.markdown(
        """
        <script>
        // Swipe gesture detection for mobile
        (function() {
            let touchStartX = 0;
            let touchEndX = 0;
            let touchStartY = 0;
            let touchEndY = 0;
            
            const minSwipeDistance = 50;
            
            document.addEventListener('touchstart', function(e) {
                touchStartX = e.changedTouches[0].screenX;
                touchStartY = e.changedTouches[0].screenY;
            }, { passive: true });
            
            document.addEventListener('touchend', function(e) {
                touchEndX = e.changedTouches[0].screenX;
                touchEndY = e.changedTouches[0].screenY;
                handleSwipe();
            }, { passive: true });
            
            function handleSwipe() {
                const deltaX = touchEndX - touchStartX;
                const deltaY = touchEndY - touchStartY;
                
                // Only handle horizontal swipes (ignore vertical scrolling)
                if (Math.abs(deltaX) > Math.abs(deltaY) && Math.abs(deltaX) > minSwipeDistance) {
                    if (deltaX > 0) {
                        // Swipe right - could open sidebar or go back
                        console.log('Swipe right detected');
                    } else {
                        // Swipe left - could close sidebar or go forward
                        console.log('Swipe left detected');
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

