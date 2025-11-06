"""
Antibiotics Module - Dosing & TDM
Main Router - Imports from antibiotics module
"""

import streamlit as st
from utils.page_helper import setup_page, render_standard_footer

from antibiotics import (
    render_antibiotic_lookup,
    render_database,
    render_multi_comparison
)
from antibiotics.comparison import render_comparison
from antibiotics.treatment_algorithms import render_algorithms_page

# Standard page setup
setup_page(
    page_title="Kháng Sinh",
    page_icon="💊",
    description="Tra cứu kháng sinh, so sánh liều dùng và chỉ định"
)

# ========== SIDEBAR ==========
with st.sidebar:
    st.header("⚙️ Chọn Công Cụ")
    
    function_type = st.selectbox(
        "Công cụ:",
        [
            "🔍 Tra Cứu & Dữ Liệu Kháng Sinh",
            "🔬 So Sánh Nhiều Kháng Sinh",
            "📊 So Sánh Side-by-Side",
            "🔄 Phác Đồ Điều Trị"
        ]
    )
    
    st.markdown("---")
    st.info("""
    **📚 Căn cứ khoa học:**
    - FDA Drug Labels (Mỹ)
    - IDSA/ATS Guidelines
    - ASHP/IDSA TDM 2020
    - WHO AWaRe Classification
    
    **💡 Tính liều theo thận:**
    Xem module "💊 Tra Cứu Thuốc" → 
    "🧮 Tính Liều Theo eGFR/CrCl"
    """)

# ========== MAIN CONTENT ==========

# Route to appropriate function
if "Tra Cứu" in function_type and "Dữ Liệu" in function_type:
    render_database()

elif "So Sánh Nhiều" in function_type:
    render_multi_comparison()

elif "Side-by-Side" in function_type:
    render_comparison()

elif "Phác Đồ" in function_type:
    render_algorithms_page()

# ========== FOOTER ==========
render_standard_footer(disclaimer=False)
