"""
Antibiotics Module - Dosing & TDM
Main Router - Imports from antibiotics module
Note: Module package name remains 'antibiotics' for backward compatibility
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

# Standard page setup
setup_page(
    page_title="Kháng sinh (chuyên sâu)",
    page_icon="💊",
    description="Module chuyên sâu về kháng sinh: dữ liệu chi tiết, so sánh và phác đồ điều trị"
)

# ========== SIDEBAR ==========
with st.sidebar:
    st.header("💊 Kháng sinh (chuyên sâu)")
    st.caption("Sub-module **Kháng sinh (chuyên sâu)** – thuộc nhóm *💊 Thuốc & Liều dùng*.")
    
    # Liên kết nhanh tới các module thuốc liên quan
    with st.expander("Liên kết trong nhóm Thuốc & Liều dùng", expanded=False):
        col1, col2 = st.columns(2)
        with col1:
            if st.button("💊 Cơ sở dữ liệu thuốc", use_container_width=True):
                st.switch_page("pages/07_💊_Drug_Database.py")
        with col2:
            if st.button("📊 TDM - Nồng độ thuốc", use_container_width=True):
                st.switch_page("pages/08_📊_TDM.py")
    
    st.markdown("---")
    st.subheader("⚙️ Chọn công cụ")
    
    function_type = st.selectbox(
        "Công cụ:",
        [
            "🔍 Tra cứu & dữ liệu kháng sinh",
            "🔬 So sánh nhiều kháng sinh",
            "📊 So sánh Side-by-Side",
            "🔄 Phác đồ điều trị"
        ]
    )
    
    st.markdown("---")
    render_info_box(
        """
    **📚 Căn cứ khoa học:**
    - FDA Drug Labels (Mỹ)
    - IDSA/ATS Guidelines
    - ASHP/IDSA TDM 2020
    - WHO AWaRe Classification
    
    **💊 Vai trò trong nhóm Thuốc & Liều dùng:**
    - Đây là **module chuyên sâu về kháng sinh**: dữ liệu chi tiết, so sánh, phác đồ điều trị.
    - **Tra cứu & tính liều cơ bản**: dùng module **\"💊 Cơ sở dữ liệu thuốc\"** (entry chính).
    - **TDM kháng sinh (vancomycin, aminoglycoside...)**: dùng module **\"📊 TDM - Theo dõi nồng độ thuốc\"**.
        """,
        type="info",
        title="Thông tin Module"
    )

# ========== MAIN CONTENT ==========

# Route to appropriate function
# Use case-insensitive matching to avoid Unicode case issues
function_type_lower = function_type.lower()

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

