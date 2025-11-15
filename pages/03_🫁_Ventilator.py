"""
Ventilator Module - Mechanical Ventilation Tools
NOTE: This page has been merged into Critical Care module.
Redirecting to Critical Care page with Ventilator Management tool.
"""

import streamlit as st
from utils.page_helper import setup_page, render_standard_footer

# Redirect to Critical Care page
setup_page(
    page_title="Thở Máy",
    page_icon="🫁",
    description="Công cụ tính toán và hướng dẫn cài đặt máy thở"
)

# Show redirect message and button
st.warning("""
**⚠️ Trang này đã được tích hợp vào module Hồi Sức (Critical Care)**

Để sử dụng các công cụ máy thở, vui lòng truy cập:
**🫁 Hồi Sức → Ventilator Management**
""")

st.info("""
**💡 Lý do tích hợp:**
- Tất cả công cụ ICU giờ đã được tập trung tại một nơi
- Workflow liền mạch: Ventilator → Fluid → Vasopressor → Sedation
- Tính năng đầy đủ hơn với ABG integration, History, Trends
""")

if st.button("🫁 Đi đến Hồi Sức - Ventilator Management", type="primary", use_container_width=True):
    # Set the tool selection in session state
    st.session_state['critical_care_tool_selection'] = "🫁 Ventilator Management"
    st.switch_page("pages/09_🫁_Critical_Care.py")

st.markdown("---")

# ========== SIDEBAR ==========
with st.sidebar:
    st.header("⚙️ Chọn Công Cụ (Legacy)")
    st.warning("**Lưu ý:** Các tính năng này vẫn hoạt động nhưng đã được tích hợp vào Critical Care module.")
    
    function_type = st.selectbox(
        "Công cụ:",
        [
            "🫁 Tính Toán Tổng Hợp",
            "🫁 ARDSNet - Tidal Volume",
            "⚙️ Cài Đặt Ban Đầu",
            "📊 Bảng PEEP/FiO2",
            "🔄 Cai Máy Thở - Weaning"
        ],
        key="legacy_ventilator_tool"
    )
    
    st.markdown("---")
    st.info("""
    **📚 Căn cứ khoa học:**
    - ARDSNet Protocol
    - Surviving Sepsis Campaign
    - ATS/ERS Guidelines
    - Lung-Protective Ventilation
    """)

# Keep legacy functionality available but deprecated
with st.expander("📜 Tính Năng Cũ (Deprecated - Vui lòng sử dụng Critical Care)", expanded=False):
    from ventilator import (
        render_ardsnet,
        render_initial_settings,
        render_peep_fio2_table,
        render_comprehensive_calculator
    )
    from ventilator.weaning import render_weaning_calculator
    
    # Route to appropriate function (legacy)
    if "Tính Toán Tổng Hợp" in function_type:
        render_comprehensive_calculator()
    elif "ARDSNet" in function_type:
        render_ardsnet()
    elif "Cài Đặt Ban Đầu" in function_type:
        render_initial_settings()
    elif "PEEP/FiO2" in function_type:
        render_peep_fio2_table()
    elif "Cai Máy Thở" in function_type or "Weaning" in function_type:
        render_weaning_calculator()

# ========== FOOTER ==========
render_standard_footer(disclaimer=False)
