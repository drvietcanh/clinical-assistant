"""
Ventilator Module - Mechanical Ventilation Tools
Main Router - Imports from ventilator module
"""

import streamlit as st
from utils.page_helper import setup_page, render_standard_footer

from ventilator import (
    render_ardsnet,
    render_initial_settings,
    render_peep_fio2_table
)

# Standard page setup
setup_page(
    page_title="Thở Máy",
    page_icon="🫁",
    description="Công cụ tính toán và hướng dẫn cài đặt máy thở"
)

# ========== SIDEBAR ==========
with st.sidebar:
    st.header("⚙️ Chọn Công Cụ")
    
    function_type = st.selectbox(
        "Công cụ:",
        [
            "🫁 ARDSNet - Tidal Volume",
            "⚙️ Cài Đặt Ban Đầu",
            "📊 Bảng PEEP/FiO2"
        ]
    )
    
    st.markdown("---")
    st.info("""
    **📚 Căn cứ khoa học:**
    - ARDSNet Protocol
    - Surviving Sepsis Campaign
    - ATS/ERS Guidelines
    - Lung-Protective Ventilation
    """)

# ========== MAIN CONTENT ==========

# Route to appropriate function
if "ARDSNet" in function_type:
    render_ardsnet()

elif "Cài Đặt Ban Đầu" in function_type:
    render_initial_settings()

elif "PEEP/FiO2" in function_type:
    render_peep_fio2_table()

# ========== FOOTER ==========
render_standard_footer(disclaimer=False)
