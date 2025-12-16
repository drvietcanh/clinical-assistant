"""
Antibiotics Module - Dosing & TDM
Main Router - Imports from antibiotics module
Note: Module package name remains 'antibiotics' for backward compatibility
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
    page_title="Kháng sinh",
    page_icon="💊",
    description="Tra cứu kháng sinh, so sánh liều dùng và chỉ định"
)

# ========== SIDEBAR ==========
with st.sidebar:
    st.header("⚙️ Chọn công cụ")
    
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
    st.info("""
    **📚 Căn cứ khoa học:**
    - FDA Drug Labels (Mỹ)
    - IDSA/ATS Guidelines
    - ASHP/IDSA TDM 2020
    - WHO AWaRe Classification
    
    **💡 Tính liều theo thận:**
    Xem module "💊 Tra cứu kháng sinh" → 
    "🧮 Tính liều theo eGFR/CrCl"
    """)

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

