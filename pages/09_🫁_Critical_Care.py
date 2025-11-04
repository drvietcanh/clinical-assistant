"""
Critical Care Module - ICU Tools
Fluid Therapy, Vasopressors, Transfusion, Sedation
"""

import streamlit as st
from utils.page_helper import setup_page, render_standard_footer

from critical_care import (
    render_fluid_calculator,
    render_vasopressor_guide,
    render_transfusion_calculator,
    render_sedation_calculator
)

# Standard page setup
setup_page(
    page_title="Hồi Sức",
    page_icon="🫁",
    description="Công cụ hỗ trợ hồi sức cấp cứu và ICU"
)

# ========== SIDEBAR ==========
with st.sidebar:
    st.header("📂 Chọn Công Cụ")
    
    tool_type = st.selectbox(
        "Công cụ:",
        [
            "💧 Fluid Therapy",
            "💉 Vasopressors",
            "🩸 Transfusion",
            "💉 Sedation & Analgesia"
        ],
        key="critical_care_tool"
    )
    
    st.markdown("---")
    st.info("""
    **📚 Critical Care Module:**
    - Fluid therapy calculations
    - Vasopressor dosing guides
    - Blood product transfusions
    - Sedation & analgesia protocols
    
    **💡 Dựa trên:**
    - Surviving Sepsis Guidelines
    - ICU protocols
    - Evidence-based practices
    """)

# ========== MAIN CONTENT ==========

st.info(f"""
**Công cụ đang sử dụng:** {tool_type}
""")

st.markdown("---")

# Route to appropriate calculator
if "Fluid" in tool_type:
    st.header("💧 Fluid Therapy Calculator")
    st.caption("Tính toán dịch truyền, bù dịch, và điều chỉnh điện giải")
    render_fluid_calculator()
    
elif "Vasopressor" in tool_type:
    st.header("💉 Vasopressor Dosing Guide")
    st.caption("Hướng dẫn liều và titration vasopressor")
    render_vasopressor_guide()
    
elif "Transfusion" in tool_type:
    render_transfusion_calculator()
    
elif "Sedation" in tool_type:
    render_sedation_calculator()

# ========== FOOTER ==========
render_standard_footer(disclaimer=False)

