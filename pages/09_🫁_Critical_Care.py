"""
Critical Care Module - ICU Tools
Fluid Therapy, Vasopressors, Transfusion, Sedation
"""

import streamlit as st
from utils.page_helper import setup_page, render_standard_footer
from components.ui import render_info_box, render_hero

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
# Use local variable to track availability after import attempt
ventilator_advanced_available = VENTILATOR_ADVANCED_AVAILABLE

if VENTILATOR_ADVANCED_AVAILABLE:
    try:
        from ventilator import (
            render_comprehensive_calculator,
            render_ardsnet,
            render_initial_settings,
            render_peep_fio2_table
        )
        from ventilator.weaning import render_weaning_calculator as render_weaning_calculator_advanced
    except ImportError as e:
        # Fallback if import fails even though VENTILATOR_ADVANCED_AVAILABLE is True
        ventilator_advanced_available = False
        render_comprehensive_calculator = None
        render_ardsnet = None
        render_initial_settings = None
        render_peep_fio2_table = None
        render_weaning_calculator_advanced = None
else:
    # Initialize as None if not available
    render_comprehensive_calculator = None
    render_ardsnet = None
    render_initial_settings = None
    render_peep_fio2_table = None
    render_weaning_calculator_advanced = None

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
    
    # Đồng bộ lựa chọn từ các nút truy cập nhanh (dashboard) với selectbox bên trái
    # Khi user click "Mở Fluid Therapy" / "Mở Vasopressors"..., hàm render_clickable_dashboard_card
    # sẽ set st.session_state['critical_care_tool_selection'] và st.rerun().
    # Ở đây ta đảm bảo selectbox dùng cùng giá trị đó để hiển thị đúng và route tới công cụ tương ứng.
    # Note: Don't set widget key directly - use index parameter instead (see below)
    
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
    
    # If saved_tool exists and was just set by button click (different from selectbox), use it for routing
    # This ensures buttons work correctly by prioritizing the saved_tool value
    if saved_tool and saved_tool in tool_options:
        # Use saved_tool if it's valid - this handles button clicks
        routing_tool_type = saved_tool
    else:
        # Otherwise use selectbox value
        routing_tool_type = tool_type
    
    # Save current selection to session_state
    if tool_type:
        st.session_state['critical_care_tool_selection'] = str(tool_type)
    
    # Use routing_tool_type for actual routing (instead of tool_type)
    tool_type = routing_tool_type
    
    st.markdown("---")
    render_info_box(
        """
    **📚 Nhóm 🫁 Hồi sức & Quy trình:**
    - **Hồi sức (trang hiện tại):** dịch, vasopressor, transfusion, sedation, ventilator, RRT, scenarios...
    - **Phác đồ điều trị:** sepsis, shock, COPD, đột quỵ, AKI, ADRS, sản khoa, da liễu...
    
    **💡 Dựa trên:**
    - Surviving Sepsis Guidelines
    - Hướng dẫn ICU và chuyên khoa quốc tế
    - Thực hành dựa trên bằng chứng
        """,
        type="info",
        title="Thông tin Module"
    )
    
    with st.expander("Liên kết tới Phác đồ điều trị", expanded=False):
        if st.button("📋 Mở Phác đồ điều trị", use_container_width=True):
            st.switch_page("pages/04_📋_Protocols.py")

# ========== MAIN CONTENT ==========

# Main tabs for organizing sub-modules
main_tabs = st.tabs([
    "🫁 Critical Care Tools",
    "🫁 Ventilator",
    "📋 Protocols",
    "📋 Guidelines",
    "📰 Medical News"
])

# Tab 1: Critical Care Tools (Dashboard, Scoring, etc.)
with main_tabs[0]:
    # Route to appropriate calculator
    if "Dashboard" in tool_type:
        render_critical_care_dashboard()
    elif "Scoring" in tool_type:
        render_scoring_calculator()
    
    elif "Ventilator Management" in tool_type:
        st.header("🫁 Ventilator Management")
        st.caption("Công cụ quản lý máy thở cho ICU")
        st.info("💡 **Lưu ý:** Ventilator tools đã được tổ chức trong tab 'Ventilator' phía trên.")
        if st.button("Mở tab Ventilator", use_container_width=True):
            st.session_state['critical_care_open_ventilator_tab'] = True
            st.rerun()
    
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
    if ventilator_advanced_available:
        vent_tab_labels = [
            "🚀 Quick Tools",
            "🫁 Comprehensive Analysis",
            "📊 Protocols & Settings",
            "🔄 Weaning & Extubation"
        ]
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
            ])
            
            with quick_tools_tabs[0]:
                render_ibw_calculator("tab0_")
            
            with quick_tools_tabs[1]:
                render_tidal_volume_calculator("tab0_")
            
            with quick_tools_tabs[2]:
                render_peep_calculator("tab0_")
            
            with quick_tools_tabs[3]:
                render_plateau_pressure_calculator("tab0_")
            
            with quick_tools_tabs[4]:
                render_weaning_calculator_basic("tab0_")
        
        # Tab 2: Comprehensive Analysis - For detailed assessment
        with vent_tabs[1]:
            st.markdown("### 🫁 Comprehensive Analysis")
            st.caption("Phân tích tổng hợp với ABG integration, alerts, history, và trends")
            st.info("💡 **Sử dụng khi:** Cần đánh giá chi tiết, theo dõi dài hạn, có ABG results")
            if render_comprehensive_calculator:
                render_comprehensive_calculator("tab0_comp_")
            else:
                st.error("Comprehensive calculator không khả dụng. Vui lòng kiểm tra module ventilator.")
        
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
                if render_ardsnet:
                    render_ardsnet("tab0_")
                else:
                    st.error("ARDSNet protocol không khả dụng.")
            
            with protocol_tabs[1]:
                if render_initial_settings:
                    render_initial_settings("tab0_")
                else:
                    st.error("Initial settings không khả dụng.")
            
            with protocol_tabs[2]:
                if render_peep_fio2_table:
                    render_peep_fio2_table()
                else:
                    st.error("PEEP/FiO2 table không khả dụng.")
        
        # Tab 4: Weaning & Extubation - For weaning assessment
        with vent_tabs[3]:
            st.markdown("### 🔄 Weaning & Extubation")
            st.caption("Đánh giá sẵn sàng cai máy thở và extubation")
            st.info("💡 **Sử dụng khi:** Đánh giá khả năng cai máy thở, chuẩn bị extubation")
            if render_weaning_calculator_advanced:
                render_weaning_calculator_advanced("tab0_weaning_")
            else:
                st.error("Advanced weaning calculator không khả dụng. Sử dụng basic calculator.")
                render_weaning_calculator_basic("tab0_weaning_")
    else:
        # Fallback to basic calculator if advanced not available
        render_ventilator_calculator("tab0_")
    
    if "ARDS" in tool_type:
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

# Tab 2: Ventilator (integrated from Ventilator page)
with main_tabs[1]:
    st.header("🫁 Ventilator Management")
    st.caption("Công cụ quản lý máy thở cho ICU")
    
    # Check if should open from redirect
    if st.session_state.get('critical_care_open_ventilator', False):
        st.session_state['critical_care_open_ventilator'] = False
    
    # Check if specific tool should be opened
    vent_tool_to_open = st.session_state.get('ventilator_tool_to_open', None)
    default_vent_tab = 0
    default_sub_tab = 0
    is_rsbi = False
    
    if vent_tool_to_open:
        if vent_tool_to_open == 'rsbi':
            default_vent_tab = 0
            default_sub_tab = 4
            is_rsbi = True
        elif vent_tool_to_open in ['weaning', 'sbt']:
            default_vent_tab = 3
        elif vent_tool_to_open == 'peep_fio2':
            default_vent_tab = 2
            default_sub_tab = 2
        if 'ventilator_tool_to_open' in st.session_state:
            del st.session_state['ventilator_tool_to_open']
    
    # Sub-menu for ventilator tools
    if ventilator_advanced_available:
        vent_tab_labels = [
            "🚀 Quick Tools",
            "🫁 Comprehensive Analysis",
            "📊 Protocols & Settings",
            "🔄 Weaning & Extubation"
        ]
        vent_tabs = st.tabs(vent_tab_labels)
        
        with vent_tabs[0]:
            st.markdown("### 🚀 Quick Tools")
            quick_tools_tabs = st.tabs([
                "📏 IBW", "💨 Tidal Volume", "📊 PEEP",
                "📈 Plateau Pressure", "🔄 RSBI (Quick)"
            ])
            with quick_tools_tabs[0]:
                render_ibw_calculator("tab1_")
            with quick_tools_tabs[1]:
                render_tidal_volume_calculator("tab1_")
            with quick_tools_tabs[2]:
                render_peep_calculator("tab1_")
            with quick_tools_tabs[3]:
                render_plateau_pressure_calculator("tab1_")
            with quick_tools_tabs[4]:
                render_weaning_calculator_basic("tab1_")
        
        with vent_tabs[1]:
            st.markdown("### 🫁 Comprehensive Analysis")
            if render_comprehensive_calculator:
                render_comprehensive_calculator("tab1_comp_")
            else:
                st.error("Comprehensive calculator không khả dụng.")
        
        with vent_tabs[2]:
            st.markdown("### 📊 Protocols & Settings")
            protocol_tabs = st.tabs([
                "🫁 ARDSNet Protocol",
                "⚙️ Initial Settings",
                "📊 PEEP/FiO2 Table"
            ])
            with protocol_tabs[0]:
                if render_ardsnet:
                    render_ardsnet("tab1_")
                else:
                    st.error("ARDSNet protocol không khả dụng.")
            with protocol_tabs[1]:
                if render_initial_settings:
                    render_initial_settings("tab1_")
                else:
                    st.error("Initial settings không khả dụng.")
            with protocol_tabs[2]:
                if render_peep_fio2_table:
                    render_peep_fio2_table()
                else:
                    st.error("PEEP/FiO2 table không khả dụng.")
        
        with vent_tabs[3]:
            st.markdown("### 🔄 Weaning & Extubation")
            if render_weaning_calculator_advanced:
                render_weaning_calculator_advanced("tab1_weaning_")
            else:
                st.error("Advanced weaning calculator không khả dụng.")
                render_weaning_calculator_basic("tab1_weaning_")
    else:
        render_ventilator_calculator("tab1_")

# Tab 3: Protocols
with main_tabs[2]:
    st.info("📋 **Protocols** - Đang tích hợp. Vui lòng sử dụng sidebar để truy cập.")
    if st.button("Mở trang Protocols", use_container_width=True):
        st.switch_page("pages/04_📋_Protocols.py")

# Tab 4: Guidelines
with main_tabs[3]:
    st.info("📋 **Guidelines Tracker** - Đang tích hợp. Vui lòng sử dụng sidebar để truy cập.")
    if st.button("Mở Guidelines Tracker", use_container_width=True):
        st.switch_page("pages/15_📋_Guidelines_Tracker.py")

# Tab 5: Medical News
with main_tabs[4]:
    st.info("📰 **Medical News** - Đang tích hợp. Vui lòng sử dụng sidebar để truy cập.")
    if st.button("Mở Medical News", use_container_width=True):
        st.switch_page("pages/10_📰_Medical_News.py")

# ========== FOOTER ==========
render_standard_footer(disclaimer=False)

