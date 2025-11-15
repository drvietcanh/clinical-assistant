"""
Ventilator Module - Mechanical Ventilation Tools
NOTE: This page has been merged into Critical Care module.
This is a redirect stub for backward compatibility.
"""

import streamlit as st
from utils.page_helper import setup_page, render_standard_footer

# Redirect to Critical Care page
setup_page(
    page_title="Thở Máy",
    page_icon="🫁",
    description="Công cụ tính toán và hướng dẫn cài đặt máy thở (Đã tích hợp vào Critical Care)"
)

# Main redirect message
st.markdown("""
<div style="text-align: center; padding: 40px 20px;">
    <h1 style="color: #e91e63;">🫁 Trang Này Đã Được Tích Hợp</h1>
    <p style="font-size: 1.2em; color: #666; margin: 20px 0;">
        Các công cụ máy thở giờ đã được tích hợp vào module <strong>Hồi Sức (Critical Care)</strong>
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.warning("""
    **⚠️ Thông Báo Quan Trọng:**
    
    Trang này đã được tích hợp vào **🫁 Hồi Sức → Ventilator Management**
    
    **Lý do tích hợp:**
    - ✅ Tất cả công cụ ICU giờ đã được tập trung tại một nơi
    - ✅ Workflow liền mạch: Ventilator → Fluid → Vasopressor → Sedation
    - ✅ Tính năng đầy đủ hơn với ABG integration, History, Trends
    """)
    
    if st.button("🫁 Đi Đến Hồi Sức - Ventilator Management", type="primary", use_container_width=True):
        # Set the tool selection in session state
        st.session_state['critical_care_tool_selection'] = "🫁 Ventilator Management"
        st.switch_page("pages/09_🫁_Critical_Care.py")
    
    st.markdown("---")
    
    st.info("""
    **💡 Hướng dẫn:**
    - Click nút bên trên để chuyển đến trang Critical Care
    - Tất cả tính năng máy thở giờ đã có trong **Hồi Sức → Ventilator Management**
    - Trang mới có đầy đủ tính năng: ABG integration, History, Trends, Alerts
    """)

# ========== SIDEBAR ==========
with st.sidebar:
    st.header("ℹ️ Thông Tin")
    st.warning("""
    **Trang này đã được tích hợp:**
    - Tất cả tính năng giờ có trong **Hồi Sức → Ventilator Management**
    - Vui lòng sử dụng trang mới để có trải nghiệm tốt nhất
    """)
    
    st.markdown("---")
    st.info("""
    **📚 Căn cứ khoa học:**
    - ARDSNet Protocol
    - Surviving Sepsis Campaign
    - ATS/ERS Guidelines
    - Lung-Protective Ventilation
    """)

# ========== FOOTER ==========
render_standard_footer(disclaimer=False)
