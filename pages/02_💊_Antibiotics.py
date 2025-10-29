"""
Antibiotics Module - Dosing & TDM
Main Router - Imports from antibiotics module
"""

import streamlit as st
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from antibiotics import (
    render_crcl,
    render_vancomycin,
    render_aminoglycoside,
    render_antibiotic_lookup,
    render_database
)

st.set_page_config(page_title="Kháng Sinh - Clinical Assistant", page_icon="💊", layout="wide")

# ========== HEADER ==========
st.title("💊 Kháng Sinh - Tính Liều & TDM")
st.markdown("Hướng dẫn liều dùng, điều chỉnh thận, theo dõi nồng độ thuốc")
st.markdown("---")

# ========== SIDEBAR ==========
with st.sidebar:
    st.header("⚙️ Chọn Công Cụ")
    
    function_type = st.selectbox(
        "Công cụ:",
        [
            "🧮 Tính CrCl (Cockcroft-Gault)",
            "💉 Vancomycin - Tính Liều",
            "💊 Aminoglycoside - Tính Liều",
            "🔍 Tra Cứu Kháng Sinh",
            "📊 Cơ Sở Dữ Liệu"
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
if "CrCl" in function_type:
    render_crcl()

elif "Vancomycin" in function_type:
    render_vancomycin()

elif "Aminoglycoside" in function_type:
    render_aminoglycoside()

elif "Tra Cứu" in function_type:
    render_antibiotic_lookup()

elif "Cơ Sở Dữ Liệu" in function_type:
    render_database()

# ========== FOOTER ==========
st.markdown("---")
st.caption("💊 Dữ liệu dựa trên hướng dẫn quốc tế và các nghiên cứu lâm sàng")
st.caption("⚠️ Chỉ mục đích tham khảo - Luôn xác minh với hướng dẫn địa phương")
st.caption("🗂️ Modular architecture - Easy to maintain and expand")
