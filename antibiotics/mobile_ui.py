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
