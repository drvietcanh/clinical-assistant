"""
Vaccination Module - Vaccine Information and Schedules
Comprehensive vaccine information for Vietnam
"""

import streamlit as st
from utils.page_helper import setup_page, render_standard_footer

from vaccination import (
    render_vaccination_home,
    render_vaccine_search,
    render_vaccine_detail,
    render_schedule_viewer,
    render_price_comparison,
    render_general_info
)

# Standard page setup
setup_page(
    page_title="Tiêm chủng và Vắc xin",
    page_icon="💉",
    description="Thông tin toàn diện về tiêm chủng, lịch tiêm, giá cả và phác đồ tiêm các loại vắc xin tại Việt Nam"
)

# ========== SIDEBAR ==========
with st.sidebar:
    st.header("⚙️ Chọn chức năng")
    
    function_type = st.selectbox(
        "Chức năng:",
        [
            "🏠 Trang chủ",
            "🔍 Tra cứu vắc xin",
            "📅 Lịch tiêm chủng",
            "💰 Giá cả vắc xin",
            "📚 Thông tin chung"
        ],
        key="vaccination_function_selector"
    )
    
    st.markdown("---")
    st.info("""
    **💉 Tiêm chủng:**
    - Vắc xin cho trẻ em
    - Vắc xin cho người lớn
    - Lịch tiêm chủng
    - Giá cả tham khảo
    - Phác đồ tiêm
    
    **📋 Phân loại:**
    - Bắt buộc (TCMR)
    - Khuyến nghị
    
    **💡 Lưu ý:**
    - Giá chỉ mang tính tham khảo
    - Liên hệ cơ sở y tế để biết giá chính xác
    """)

# ========== MAIN CONTENT ==========

# Route to appropriate function
if "Trang chủ" in function_type:
    render_vaccination_home()
elif "Tra cứu" in function_type:
    render_vaccine_search()
elif "Lịch tiêm" in function_type:
    render_schedule_viewer()
elif "Giá cả" in function_type:
    render_price_comparison()
elif "Thông tin chung" in function_type:
    render_general_info()
else:
    render_vaccination_home()

# Footer
render_standard_footer()

