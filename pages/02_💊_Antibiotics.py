"""
Antibiotics Module - Optimized UI
Modern interface with tabs: By Infection, By Drug Class, Stewardship
Integrated with existing database and comparison tools
"""

import streamlit as st
from utils.page_helper import setup_page, render_standard_footer
from components.ui import render_info_box, render_hero

from antibiotics import (
    render_antibiotic_lookup,
    render_database,
    render_multi_comparison
)
from antibiotics.comparison import render_comparison
from antibiotics.treatment_algorithms import render_algorithms_page

# Import new UI components
try:
    from antibiotics.ui_antibiotics_view import (
        render_antibiotics_by_infection_view,
        render_antibiotics_by_drug_class_view,
        render_stewardship_view
    )
    NEW_UI_AVAILABLE = True
except ImportError:
    NEW_UI_AVAILABLE = False

# Standard page setup
setup_page(
    page_title="Kháng sinh (chuyên sâu)",
    page_icon="💊",
    description="Module chuyên sâu về kháng sinh: phác đồ điều trị, so sánh và dữ liệu chi tiết"
)

# Hero section with improved design and mobile optimization
st.markdown("""
<style>
.hero-section {
    background: linear-gradient(135deg, #4caf50 0%, #2e7d32 100%);
    color: white;
    padding: 35px 30px;
    border-radius: 20px;
    margin-bottom: 35px;
    text-align: center;
    box-shadow: 0 8px 24px rgba(76,175,80,0.25), 0 4px 8px rgba(0,0,0,0.1);
    position: relative;
    overflow: hidden;
}

@media (max-width: 768px) {
    .hero-section {
        padding: 20px 15px !important;
        margin-bottom: 20px !important;
    }
    
    .hero-section h1 {
        font-size: 2em !important;
        margin: 0 !important;
    }
    
    .hero-section p {
        font-size: 1em !important;
        margin: 12px 0 0 0 !important;
    }
    
    .hero-decoration {
        display: none; /* Hide decorative elements on mobile for performance */
    }
}

@media (min-width: 769px) {
    .hero-decoration {
        position: absolute;
        top: -50%;
        right: -10%;
        width: 300px;
        height: 300px;
        background: rgba(255,255,255,0.1);
        border-radius: 50%;
        filter: blur(60px);
    }
}
</style>

<div class="hero-section">
    <div class="hero-decoration"></div>
    <div style='position: relative; z-index: 1;'>
        <h1 style='margin: 0; color: white; font-size: 2.8em; font-weight: 700; letter-spacing: -0.5px; text-shadow: 0 2px 8px rgba(0,0,0,0.2);'>💊 Kháng sinh (Chuyên sâu)</h1>
        <p style='margin: 15px 0 0 0; color: rgba(255,255,255,0.95); font-size: 1.2em; font-weight: 400; line-height: 1.6;'>
            Phác đồ điều trị • So sánh kháng sinh • Dữ liệu chi tiết
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

# ========== SIDEBAR ==========
with st.sidebar:
    st.header("💊 Kháng sinh")
    st.caption("Module chuyên sâu về kháng sinh")
    
    # Quick links
    with st.expander("🔗 Liên kết nhanh", expanded=False):
        col1, col2 = st.columns(2)
        with col1:
            if st.button("💊 Drug Database", use_container_width=True):
                st.switch_page("pages/07_💊_Drug_Database.py")
        with col2:
            if st.button("📊 TDM", use_container_width=True):
                st.switch_page("pages/08_📊_TDM.py")
    
    st.markdown("---")
    
    # Legacy tools (for backward compatibility)
    st.subheader("⚙️ Công cụ khác")
    legacy_tools = st.selectbox(
        "Công cụ:",
        [
            "🔍 Tra cứu & dữ liệu",
            "🔬 So sánh nhiều kháng sinh",
            "📊 So sánh Side-by-Side",
            "🔄 Phác đồ điều trị (Legacy)"
        ],
        key="legacy_tool_selector"
    )
    
    st.markdown("---")
    render_info_box(
        """
    **📚 Căn cứ khoa học:**
    - IDSA/ATS Guidelines 2019
    - Sanford Guide 2025
    - Surviving Sepsis Campaign 2021
    - WHO AWaRe Classification
    
    **💊 Tính năng:**
    - Phác đồ điều trị theo guideline mới nhất
    - So sánh kháng sinh
    - Dữ liệu chi tiết và tính liều
        """,
        type="info",
        title="Thông tin"
    )

# ========== MAIN CONTENT ==========

# Mobile styles and advanced features injection
try:
    from antibiotics.mobile_ui import (
        inject_mobile_styles,
        inject_swipe_gestures,
        inject_pull_to_refresh,
        inject_card_swipe_actions,
        inject_quick_actions_menu,
        inject_pwa_support,
        inject_offline_indicator
    )
    from antibiotics.performance import (
        inject_lazy_loading,
        inject_image_lazy_loading,
        inject_performance_monitoring
    )
    
    inject_mobile_styles()
    inject_swipe_gestures()
    inject_pull_to_refresh()
    inject_card_swipe_actions()
    inject_quick_actions_menu()
    inject_pwa_support()
    inject_offline_indicator()
    inject_lazy_loading()
    inject_image_lazy_loading()
    inject_performance_monitoring()
except ImportError:
    pass

# Main tabs for new UI with mobile optimization
if NEW_UI_AVAILABLE:
    # Mobile-optimized tabs
    st.markdown("""
    <style>
    @media (max-width: 768px) {
        .stTabs {
            overflow-x: auto;
            -webkit-overflow-scrolling: touch;
            scrollbar-width: none; /* Firefox */
            -ms-overflow-style: none; /* IE/Edge */
        }
        
        .stTabs::-webkit-scrollbar {
            display: none; /* Chrome/Safari */
        }
        
        .stTabs [role="tab"] {
            min-width: 120px;
            padding: 12px 16px;
            font-size: 0.95em;
            white-space: nowrap;
        }
        
        .stTabs [role="tab"][aria-selected="true"] {
            border-bottom: 3px solid #1976D2;
            font-weight: 600;
        }
    }
    </style>
    """, unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4 = st.tabs([
        "🦠 Theo Nhiễm Trùng",
        "💊 Theo Nhóm Thuốc",
        "🔄 Quản lý Kháng Sinh",
        "🔧 Công cụ"
    ])
    
    with tab1:
        # Mobile bottom nav và FAB
        try:
            from antibiotics.mobile_ui import render_mobile_bottom_nav, render_mobile_fab
            render_mobile_bottom_nav(current_tab="infection")
            render_mobile_fab()
        except ImportError:
            pass
        
        render_antibiotics_by_infection_view()
    
    with tab2:
        try:
            from antibiotics.mobile_ui import render_mobile_bottom_nav
            render_mobile_bottom_nav(current_tab="drugs")
        except ImportError:
            pass
        
        render_antibiotics_by_drug_class_view()
    
    with tab3:
        try:
            from antibiotics.mobile_ui import render_mobile_bottom_nav
            render_mobile_bottom_nav(current_tab="stewardship")
        except ImportError:
            pass
        
        render_stewardship_view()
    
    with tab4:
        try:
            from antibiotics.mobile_ui import render_mobile_bottom_nav
            render_mobile_bottom_nav(current_tab="search")
        except ImportError:
            pass
        # Legacy tools in separate tab
        st.markdown("### 🔧 Công cụ")
        st.info("Các công cụ tra cứu và so sánh kháng sinh")
        
        function_type_lower = legacy_tools.lower()
        
        if "tra cứu" in function_type_lower and "dữ liệu" in function_type_lower:
            render_database()
        elif "so sánh nhiều" in function_type_lower:
            render_multi_comparison()
        elif "side-by-side" in function_type_lower:
            render_comparison()
        elif "phác đồ" in function_type_lower:
            render_algorithms_page()
else:
    # Fallback to old UI if new components not available
    st.warning("⚠️ New UI components not available. Using legacy interface.")
    
    function_type_lower = legacy_tools.lower()
    
    if "tra cứu" in function_type_lower and "dữ liệu" in function_type_lower:
        render_database()
    elif "so sánh nhiều" in function_type_lower:
        render_multi_comparison()
    elif "side-by-side" in function_type_lower:
        render_comparison()
    elif "phác đồ" in function_type_lower:
        render_algorithms_page()

# ========== FOOTER ==========
render_standard_footer(disclaimer=False)

