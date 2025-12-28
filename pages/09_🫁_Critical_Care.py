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
    render_scenarios_calculator,
    render_dirc_calculator,
    VENTILATOR_ADVANCED_AVAILABLE,
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
    st.header("🫁 Hồi sức (ICU)")
    st.caption("Module **Hồi sức** – thuộc nhóm *🫁 Hồi sức & Quy trình* (bao gồm cả Ventilator).")
    
    # Tool options with consistent naming
    tool_options = [
        "🏠 Dashboard",
        "📊 Scoring Systems",
        "🫁 Ventilator Management",
        "🫁 ARDS Protocols",
        "🦠 Sepsis Protocols",
        "💉 Shock Management",
        "🩺 RRT Calculator",
        "🎯 Clinical Scenarios",
        "💧 Fluid Therapy",
        "💉 Vasopressors",
        "💉 Tính liều thuốc tim mạch",
        "💧 Enhanced Infusion Calculator",
        "💉 Multiple Infusions",
        "⚡ Electrolyte Calculator",
        "📈 Titration Guide",
        "✅ Safety Checker",
        "⚙️ Custom Presets",
        "⚡ Shock Index",
        "🔗 Links to Scores",
        "🩸 Transfusion",
        "💤 Sedation & Analgesia",
        "💉 Drug Infusion (DIRC)",
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
    **📚 Nhóm 🫁 Hồi sức & Quy trình:**
    - **Hồi sức (trang hiện tại):** dịch, vasopressor, transfusion, sedation, ventilator, RRT, scenarios...
    - **Phác đồ điều trị:** sepsis, shock, COPD, đột quỵ, AKI, ADRS, sản khoa, da liễu...
    
    **💡 Dựa trên:**
    - Surviving Sepsis Guidelines
    - Hướng dẫn ICU và chuyên khoa quốc tế
    - Thực hành dựa trên bằng chứng
    """)
    
    with st.expander("Liên kết tới Phác đồ điều trị", expanded=False):
        if st.button("📋 Mở Phác đồ điều trị", use_container_width=True):
            st.switch_page("pages/04_📋_Protocols.py")

# ========== MAIN CONTENT ==========

# Route to appropriate calculator
if "Dashboard" in tool_type:
    render_critical_care_dashboard()
    
elif "Scoring" in tool_type:
    render_scoring_calculator()
    
elif "Ventilator Management" in tool_type:
    st.header("🫁 Ventilator Management")
    st.caption("Công cụ quản lý máy thở cho ICU")
    
    # Check if specific tool should be opened
    vent_tool_to_open = st.session_state.get('ventilator_tool_to_open', None)
    default_vent_tab = 0
    default_sub_tab = 0
    is_rsbi = False
    
    if vent_tool_to_open:
        if vent_tool_to_open == 'rsbi':
            default_vent_tab = 0  # Quick Tools tab
            default_sub_tab = 4  # RSBI tab
            is_rsbi = True
        elif vent_tool_to_open in ['weaning', 'sbt']:
            default_vent_tab = 3  # Weaning & Extubation tab
        elif vent_tool_to_open == 'peep_fio2':
            default_vent_tab = 2  # Protocols & Settings tab
            default_sub_tab = 2  # PEEP/FiO2 Table
        # Clear after using
        if 'ventilator_tool_to_open' in st.session_state:
            del st.session_state['ventilator_tool_to_open']
    
    # Sub-menu for ventilator tools - Organized into 4 clear tabs
    if VENTILATOR_ADVANCED_AVAILABLE:
        vent_tab_labels = [
            "🚀 Quick Tools",
            "🫁 Comprehensive Analysis",
            "📊 Protocols & Settings",
            "🔄 Weaning & Extubation"
        ]
        if default_vent_tab is not None and 0 <= default_vent_tab < len(vent_tab_labels):
            vent_tabs = st.tabs(vent_tab_labels, selected=default_vent_tab)
        else:
            vent_tabs = st.tabs(vent_tab_labels)
        
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
            ], selected=default_sub_tab if is_rsbi else None)
            
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
            ], selected=default_sub_tab if default_vent_tab == 2 else None)
            
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
    
elif "Clinical Scenarios" in tool_type or "Scenarios" in tool_type:
    render_scenarios_calculator()
    
elif "Fluid" in tool_type:
    st.header("💧 Fluid Therapy Calculator")
    st.caption("Tính toán dịch truyền, bù dịch, và điều chỉnh điện giải")
    render_fluid_calculator()
    
elif "Vasopressor" in tool_type:
    st.header("💉 Vasopressor Dosing Guide")
    st.caption("Hướng dẫn liều và titration vasopressor")
    render_vasopressor_guide()

elif "Tính liều thuốc tim mạch" in tool_type:
    try:
        from components.cardiovascular_calculator import render_cardiovascular_calculator
        render_cardiovascular_calculator()
    except ImportError as e:
        st.error(f"Không thể tải module tính liều thuốc tim mạch: {str(e)}")
        st.info("Vui lòng kiểm tra file components/cardiovascular_calculator.py")

elif "Enhanced Infusion" in tool_type:
    try:
        from components.enhanced_infusion_calculator import render_enhanced_infusion_calculator
        render_enhanced_infusion_calculator()
    except ImportError as e:
        st.error(f"Không thể tải Enhanced Infusion Calculator: {str(e)}")
        st.info("Vui lòng kiểm tra file components/enhanced_infusion_calculator.py")

elif "Multiple Infusions" in tool_type:
    try:
        from components.multiple_infusions_calculator import render_multiple_infusions_calculator
        render_multiple_infusions_calculator()
    except ImportError as e:
        st.error(f"Không thể tải Multiple Infusions Calculator: {str(e)}")
        st.info("Vui lòng kiểm tra file components/multiple_infusions_calculator.py")

elif "Electrolyte Calculator" in tool_type:
    try:
        from components.electrolyte_calculator import render_electrolyte_calculator
        render_electrolyte_calculator()
    except ImportError as e:
        st.error(f"Không thể tải Electrolyte Calculator: {str(e)}")
        st.info("Vui lòng kiểm tra file components/electrolyte_calculator.py")

elif "Titration Guide" in tool_type:
    try:
        from components.titration_calculator import render_titration_calculator
        render_titration_calculator()
    except ImportError as e:
        st.error(f"Không thể tải Titration Guide: {str(e)}")
        st.info("Vui lòng kiểm tra file components/titration_calculator.py")

elif "Safety Checker" in tool_type:
    try:
        from components.safety_checker import render_safety_checker
        render_safety_checker()
    except ImportError as e:
        st.error(f"Không thể tải Safety Checker: {str(e)}")
        st.info("Vui lòng kiểm tra file components/safety_checker.py")

elif "Custom Presets" in tool_type:
    try:
        from components.custom_presets_manager import render_custom_presets_manager
        render_custom_presets_manager()
    except ImportError as e:
        st.error(f"Không thể tải Custom Presets Manager: {str(e)}")
        st.info("Vui lòng kiểm tra file components/custom_presets_manager.py")

elif "Shock Index" in tool_type:
    try:
        from components.shock_index_calculator import render_shock_index_calculator
        render_shock_index_calculator()
    except ImportError as e:
        st.error(f"Không thể tải Shock Index Calculator: {str(e)}")
        st.info("Vui lòng kiểm tra file components/shock_index_calculator.py")

elif "Links to Scores" in tool_type:
    try:
        from components.score_links import (
            render_gcs_link,
            render_rass_link,
            render_anion_gap_link,
            render_qtc_link,
            render_sofa_link
        )
        
        st.markdown("## 🔗 Links to Existing Scores")
        st.markdown("""
        Các calculator đã có sẵn trong **Scores** module.
        Click vào link để mở trực tiếp.
        """)
        
        st.markdown("---")
        render_gcs_link()
        st.markdown("---")
        render_rass_link()
        st.markdown("---")
        render_anion_gap_link()
        st.markdown("---")
        render_qtc_link()
        st.markdown("---")
        render_sofa_link()
        
    except ImportError as e:
        st.error(f"Không thể tải Score Links: {str(e)}")
        st.info("Vui lòng kiểm tra file components/score_links.py")
    
elif "Transfusion" in tool_type:
    render_transfusion_calculator()
    
elif "Sedation" in tool_type or "Analgesia" in tool_type:
    render_sedation_calculator()

elif "Drug Infusion" in tool_type or "DIRC" in tool_type:
    render_dirc_calculator()

# ========== FOOTER ==========
render_standard_footer(disclaimer=False)

