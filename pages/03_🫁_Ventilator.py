"""
Ventilator Module - Mechanical Ventilation Tools
Main Router - Imports from ventilator module
"""

import streamlit as st
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from ventilator import (
    render_ardsnet,
    render_initial_settings,
    render_peep_fio2_table
)

st.set_page_config(page_title="Thở Máy - Clinical Assistant", page_icon="🫁", layout="wide")

# ========== HEADER ==========
st.title("🫁 Thở Máy - Hỗ Trợ Hô Hấp")
st.markdown("Công cụ tính toán và hướng dẫn cài đặt máy thở")
st.markdown("---")

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
st.markdown("---")
st.caption("🫁 Dữ liệu dựa trên ARDSNet và các hướng dẫn quốc tế")
st.caption("⚠️ Luôn cá thể hóa theo tình trạng lâm sàng bệnh nhân")
st.caption("🗂️ Modular architecture - Easy to maintain and expand")
