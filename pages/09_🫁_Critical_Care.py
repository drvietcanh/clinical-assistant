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
    render_rrt_calculator,
    VENTILATOR_ADVANCED_AVAILABLE
)

# Import advanced ventilator functions if available
if VENTILATOR_ADVANCED_AVAILABLE:
    from ventilator import (
        render_comprehensive_calculator,
        render_ardsnet,
        render_initial_settings,
        render_peep_fio2_table
    )
    from ventilator.weaning import render_weaning_calculator as render_weaning_calculator_advanced

# Import individual quick tools from critical_care/ventilator
from critical_care.ventilator import (
    render_ibw_calculator,
    render_tidal_volume_calculator,
    render_peep_calculator,
    render_plateau_pressure_calculator,
    render_weaning_calculator as render_weaning_calculator_basic
)

# Standard page setup
setup_page(
    page_title="Hồi sức",
    page_icon="🫁",
    description="Công cụ hỗ trợ hồi sức cấp cứu và ICU"
)

# ========== SIDEBAR ==========
with st.sidebar:
    st.header("📂 Chọn công cụ")
    
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
    **📚 Module Hồi sức:**
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
    st.header("🫁 Ventilator Management")
    st.caption("Công cụ quản lý máy thở cho ICU")
    
    # Sub-menu for ventilator tools - Organized into 4 clear tabs
    if VENTILATOR_ADVANCED_AVAILABLE:
        vent_tabs = st.tabs([
            "🚀 Quick Tools",
            "🫁 Comprehensive Analysis",
            "📊 Protocols & Settings",
            "🔄 Weaning & Extubation"
        ])
        
        # Tab 1: Quick Tools - For fast decisions
        with vent_tabs[0]:
            st.markdown("### 🚀 Quick Tools")
            st.caption("Công cụ tính toán nhanh cho quyết định lâm sàng")
            st.info("💡 **Sử dụng khi:** Cần tính toán nhanh, đơn giản, không cần phân tích chi tiết")
            
            quick_tools_tabs = st.tabs([
                "📏 IBW",
                "💨 Tidal Volume",
                "📊 PEEP",
                "📈 Plateau Pressure",
                "🔄 RSBI (Quick)"
            ])
            
            with quick_tools_tabs[0]:
                render_ibw_calculator()
            
            with quick_tools_tabs[1]:
                render_tidal_volume_calculator()
            
            with quick_tools_tabs[2]:
                render_peep_calculator()
            
            with quick_tools_tabs[3]:
                render_plateau_pressure_calculator()
            
            with quick_tools_tabs[4]:
                render_weaning_calculator_basic()
        
        # Tab 2: Comprehensive Analysis - For detailed assessment
        with vent_tabs[1]:
            st.markdown("### 🫁 Comprehensive Analysis")
            st.caption("Phân tích tổng hợp với ABG integration, alerts, history, và trends")
            st.info("💡 **Sử dụng khi:** Cần đánh giá chi tiết, theo dõi dài hạn, có ABG results")
            render_comprehensive_calculator()
        
        # Tab 3: Protocols & Settings - Standard protocols
        with vent_tabs[2]:
            st.markdown("### 📊 Protocols & Settings")
            st.caption("Các protocol chuẩn và hướng dẫn cài đặt máy thở")
            st.info("💡 **Sử dụng khi:** Cần tuân thủ protocol chuẩn, cài đặt ban đầu")
            
            protocol_tabs = st.tabs([
                "🫁 ARDSNet Protocol",
                "⚙️ Initial Settings",
                "📊 PEEP/FiO2 Table"
            ])
            
            with protocol_tabs[0]:
                render_ardsnet()
            
            with protocol_tabs[1]:
                render_initial_settings()
            
            with protocol_tabs[2]:
                render_peep_fio2_table()
        
        # Tab 4: Weaning & Extubation - For weaning assessment
        with vent_tabs[3]:
            st.markdown("### 🔄 Weaning & Extubation")
            st.caption("Đánh giá sẵn sàng cai máy thở và extubation")
            st.info("💡 **Sử dụng khi:** Đánh giá khả năng cai máy thở, chuẩn bị extubation")
            render_weaning_calculator_advanced()
    else:
        # Fallback to basic calculator if advanced not available
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

