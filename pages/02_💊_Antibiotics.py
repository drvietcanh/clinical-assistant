"""
Antibiotics Module - Dosing & TDM
Main Router - Imports from antibiotics module
"""

import streamlit as st
from utils.page_helper import setup_page, render_standard_footer

from antibiotics import (
    render_antibiotic_lookup,
    render_database,
    render_dosing_calculator,
    render_multi_comparison
)
from drugs import render_interaction_checker

# Standard page setup
setup_page(
    page_title="Kháng Sinh",
    page_icon="💊",
    description="Hướng dẫn liều dùng, điều chỉnh thận, theo dõi nồng độ thuốc"
)

# ========== SIDEBAR ==========
with st.sidebar:
    st.header("⚙️ Chọn Công Cụ")
    
    function_type = st.selectbox(
        "Công cụ:",
        [
            "🧮 Tính Liều Theo eGFR/CrCl",
            "🔬 So Sánh Nhiều Kháng Sinh",
            "🔍 Tra Cứu & Dữ Liệu Kháng Sinh",
            "🔍 Kiểm Tra Tương Tác Thuốc"
        ]
    )
    
    st.markdown("---")
    st.info("""
    **📚 Căn cứ khoa học:**
    - FDA Drug Labels (Mỹ)
    - IDSA/ATS Guidelines
    - ASHP/IDSA TDM 2020
    - WHO AWaRe Classification
    """)

# ========== MAIN CONTENT ==========

# Route to appropriate function
if "Tính Liều Theo eGFR" in function_type or "CrCl" in function_type:
    render_dosing_calculator()

elif "So Sánh Nhiều" in function_type:
    render_multi_comparison()

elif "Tra Cứu" in function_type or "Dữ Liệu" in function_type:
    render_database()

elif "Tương Tác" in function_type:
    render_interaction_checker()

# ========== FOOTER ==========
render_standard_footer(disclaimer=False)
