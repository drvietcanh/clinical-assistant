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

# Hero section
st.markdown("""
<div style='
    background: linear-gradient(135deg, #4caf50 0%, #2e7d32 100%);
    color: white;
    padding: 30px 25px;
    border-radius: 16px;
    margin-bottom: 30px;
    text-align: center;
'>
    <h1 style='margin: 0; color: white; font-size: 2.5em;'>💊 Kháng sinh (Chuyên sâu)</h1>
    <p style='margin: 12px 0 0 0; color: rgba(255,255,255,0.95); font-size: 1.1em;'>
        Phác đồ điều trị • So sánh kháng sinh • Dữ liệu chi tiết
    </p>
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

# Main tabs for new UI
if NEW_UI_AVAILABLE:
    tab1, tab2, tab3, tab4 = st.tabs([
        "🦠 By Infection",
        "💊 By Drug Class",
        "🔄 Stewardship",
        "🔧 Tools"
    ])
    
    with tab1:
        render_antibiotics_by_infection_view()
    
    with tab2:
        render_antibiotics_by_drug_class_view()
    
    with tab3:
        render_stewardship_view()
    
    with tab4:
        # Legacy tools in separate tab
        st.markdown("### 🔧 Legacy Tools")
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

