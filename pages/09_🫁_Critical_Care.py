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
    render_sedation_calculator,
    render_scoring_calculator,
    render_critical_care_dashboard,
    render_ventilator_calculator,
    render_ards_protocols,
    render_sepsis_protocols,
    render_shock_management,
    render_rrt_calculator
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
    
    # Tool options with consistent naming
    tool_options = [
        "🏠 Dashboard",
        "📊 Scoring Systems",
        "🫁 Ventilator Management",
        "🫁 ARDS Protocols",
        "🦠 Sepsis Protocols",
        "💉 Shock Management",
        "🩺 RRT Calculator",
        "💧 Fluid Therapy",
        "💉 Vasopressors",
        "🩸 Transfusion",
        "💤 Sedation & Analgesia"
    ]
    
    # Use saved tool selection or default
    saved_tool = st.session_state.get('critical_care_tool_selection', None)
    default_index = 0
    
    if saved_tool and saved_tool in tool_options:
        default_index = tool_options.index(saved_tool)
    
    tool_type = st.selectbox(
        "Công cụ:",
        tool_options,
        index=default_index,
        key="critical_care_tool_selector"
    )
    
    # Save current selection
    if tool_type:
        st.session_state['critical_care_tool_selection'] = str(tool_type)
    
    st.markdown("---")
    st.info("""
    **📚 Module Hồi Sức:**
    - Tính toán dịch truyền và điện giải
    - Hướng dẫn liều vasopressor
    - Tính toán truyền máu và chế phẩm máu
    - Giao thức an thần và giảm đau
    
    **💡 Dựa trên:**
    - Surviving Sepsis Guidelines
    - Hướng dẫn ICU quốc tế
    - Thực hành dựa trên bằng chứng
    """)

# ========== MAIN CONTENT ==========

# Route to appropriate calculator
if "Dashboard" in tool_type:
    render_critical_care_dashboard()
    
elif "Scoring" in tool_type:
    render_scoring_calculator()
    
elif "Ventilator Management" in tool_type:
    render_ventilator_calculator()
    
elif "ARDS" in tool_type:
    render_ards_protocols()
    
elif "Sepsis" in tool_type:
    render_sepsis_protocols()
    
elif "Shock" in tool_type:
    render_shock_management()
    
elif "RRT" in tool_type:
    render_rrt_calculator()
    
elif "Fluid" in tool_type:
    st.header("💧 Fluid Therapy Calculator")
    st.caption("Tính toán dịch truyền, bù dịch, và điều chỉnh điện giải")
    render_fluid_calculator()
    
elif "Vasopressor" in tool_type:
    st.header("💉 Vasopressor Dosing Guide")
    st.caption("Hướng dẫn liều và titration vasopressor")
    render_vasopressor_guide()
    
elif "Transfusion" in tool_type:
    render_transfusion_calculator()
    
elif "Sedation" in tool_type or "Analgesia" in tool_type:
    render_sedation_calculator()

# ========== FOOTER ==========
render_standard_footer(disclaimer=False)

