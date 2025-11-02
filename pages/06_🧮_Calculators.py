"""
Clinical Calculators - Common Formulas
Tập trung các công thức tính toán thông dụng hàng ngày
BMI, BSA, eGFR, và các công thức khác
"""

import streamlit as st
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

# Import calculators
from scores.metabolism.bmi_ibw_bsa import render as render_bmi_ibw_bsa
from scores.metabolism.osmolality import render as render_osmolality
from scores.metabolism.anion_gap import render as render_anion_gap
from scores.metabolism.corrected_calcium import render as render_corrected_calcium
from scores.metabolism.fena import render as render_fena
from scores.metabolism.hba1c_eag import render as render_hba1c_eag
from scores.metabolism.winter_formula import render as render_winter_formula
from scores.metabolism.free_t4_index import render as render_free_t4_index

from scores.nephrology.egfr import render as render_egfr

st.set_page_config(page_title="Calculators - Clinical Assistant", page_icon="🧮", layout="wide")

# ========== HEADER ==========
st.markdown("""
<h1 style='text-align: center; color: #0EA5E9;'>🧮 Clinical Calculators</h1>
<p style='text-align: center;'><em>Các công thức tính toán thông dụng hàng ngày trong lâm sàng</em></p>
""", unsafe_allow_html=True)

st.markdown("---")

# ========== SIDEBAR ==========
with st.sidebar:
    st.header("⚙️ Chọn Calculator")
    
    calculator_type = st.selectbox(
        "Calculator:",
        [
            "📏 BMI | IBW | BSA",
            "🧪 eGFR/GFR Calculator",
            "💧 Osmolality & Gap",
            "⚖️ Anion Gap",
            "🦴 Corrected Calcium",
            "🧪 FENa",
            "📊 HbA1c ↔ eAG",
            "🌡️ Winter Formula",
            "🔬 Free T4 Index"
        ]
    )
    
    st.markdown("---")
    st.info("""
    **💡 Các calculator thông dụng:**
    
    **Cơ thể:**
    - BMI, IBW, BSA
    
    **Chức năng thận:**
    - eGFR (chẩn đoán CKD)
    
    **Xét nghiệm:**
    - Osmolality, Anion Gap
    - Corrected Ca, FENa
    - HbA1c, T4 Index
    """)
    
    st.markdown("---")
    st.caption("**💊 Liên quan:** Các calculator này cần thiết cho điều chỉnh liều thuốc")

# ========== MAIN CONTENT ==========

# Route to appropriate calculator
if "BMI" in calculator_type or "IBW" in calculator_type or "BSA" in calculator_type:
    render_bmi_ibw_bsa()

elif "eGFR" in calculator_type or "GFR" in calculator_type:
    render_egfr()

elif "Osmolality" in calculator_type:
    render_osmolality()

elif "Anion Gap" in calculator_type:
    render_anion_gap()

elif "Corrected" in calculator_type or "Calcium" in calculator_type:
    render_corrected_calcium()

elif "FENa" in calculator_type:
    render_fena()

elif "HbA1c" in calculator_type or "eAG" in calculator_type:
    render_hba1c_eag()

elif "Winter" in calculator_type:
    render_winter_formula()

elif "T4" in calculator_type or "Free" in calculator_type:
    render_free_t4_index()

# ========== FOOTER ==========
st.markdown("---")
st.caption("🧮 **Clinical Calculators** - Công cụ tính toán lâm sàng thông dụng")
st.caption("⚠️ Chỉ mục đích tham khảo - Luôn xác minh với hướng dẫn địa phương")

