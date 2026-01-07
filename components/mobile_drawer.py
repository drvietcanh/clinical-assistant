"""
Mobile Drawer Component
Drawer/modal sidebar for mobile devices
"""

import streamlit as st


def render_mobile_drawer_trigger():
    """
    Render a trigger button to open mobile drawer
    Should be placed in the main content area
    """
    st.markdown(
        """
        <style>
        @media (max-width: 768px) {
            .mobile-drawer-trigger {
                position: fixed;
                top: 1rem;
                left: 1rem;
                z-index: 1000;
                background: var(--primary, #2D7DF6);
                color: white;
                border: none;
                border-radius: 50%;
                width: 48px;
                height: 48px;
                font-size: 1.5rem;
                box-shadow: 0 2px 8px rgba(0,0,0,0.2);
                cursor: pointer;
                display: flex;
                align-items: center;
                justify-content: center;
                touch-action: manipulation;
            }
            
            .mobile-drawer-trigger:active {
                transform: scale(0.95);
            }
        }
        
        @media (min-width: 769px) {
            .mobile-drawer-trigger {
                display: none;
            }
        }
        </style>
        
        <button class="mobile-drawer-trigger" onclick="toggleMobileDrawer()" aria-label="Mở menu">
            ☰
        </button>
        
        <script>
        function toggleMobileDrawer() {
            const sidebar = document.querySelector('[data-testid="stSidebar"]');
            if (sidebar) {
                const isExpanded = sidebar.getAttribute('aria-expanded') === 'true';
                sidebar.setAttribute('aria-expanded', (!isExpanded).toString());
                
                // Add/remove overlay
                let overlay = document.getElementById('mobile-drawer-overlay');
                if (!isExpanded) {
                    if (!overlay) {
                        overlay = document.createElement('div');
                        overlay.id = 'mobile-drawer-overlay';
                        overlay.style.cssText = `
                            position: fixed;
                            top: 0;
                            left: 0;
                            right: 0;
                            bottom: 0;
                            background: rgba(0, 0, 0, 0.5);
                            z-index: 998;
                            transition: opacity 0.3s ease;
                        `;
                        overlay.onclick = toggleMobileDrawer;
                        document.body.appendChild(overlay);
                    }
                    overlay.style.opacity = '1';
                } else {
                    if (overlay) {
                        overlay.style.opacity = '0';
                        setTimeout(() => overlay.remove(), 300);
                    }
                }
            }
        }
        
        // Close drawer when clicking outside
        document.addEventListener('click', function(e) {
            const sidebar = document.querySelector('[data-testid="stSidebar"]');
            const trigger = document.querySelector('.mobile-drawer-trigger');
            if (sidebar && sidebar.getAttribute('aria-expanded') === 'true') {
                if (!sidebar.contains(e.target) && !trigger.contains(e.target)) {
                    toggleMobileDrawer();
                }
            }
        });
        </script>
        """,
        unsafe_allow_html=True
    )


def render_mobile_drawer_styles():
    """
    Add CSS styles for mobile drawer behavior
    Should be called once in app initialization
    """
    st.markdown(
        """
        <style>
        @media (max-width: 768px) {
            /* Drawer behavior for sidebar */
            [data-testid="stSidebar"] {
                position: fixed !important;
                top: 0 !important;
                left: 0 !important;
                height: 100vh !important;
                width: 85% !important;
                max-width: 320px !important;
                z-index: 999 !important;
                transform: translateX(-100%);
                transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
                box-shadow: 2px 0 8px rgba(0,0,0,0.15);
                overflow-y: auto;
                -webkit-overflow-scrolling: touch;
                padding-bottom: env(safe-area-inset-bottom);
            }
            
            [data-testid="stSidebar"][aria-expanded="true"] {
                transform: translateX(0);
            }
            
            /* Prevent body scroll when drawer is open */
            body:has([data-testid="stSidebar"][aria-expanded="true"]) {
                overflow: hidden;
            }
            
            /* Add padding to main content when drawer is open */
            .main:has([data-testid="stSidebar"][aria-expanded="true"]) {
                margin-left: 0;
            }
        }
        
        @media (min-width: 769px) {
            [data-testid="stSidebar"] {
                transform: translateX(0) !important;
                position: relative !important;
            }
        }
        </style>
        """,
        unsafe_allow_html=True
    )
