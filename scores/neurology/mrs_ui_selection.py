"""
mRS Calculator - Selection UI Components
Handles grade selection and display
"""

import streamlit as st
from .mrs_data import MRS_GRADES


def render_selection():
    """Render the mRS grade selection UI"""
    
    st.markdown("### 🩺 Chọn Mức Độ Chức Năng")
    
    st.info("""
    **Hướng dẫn:** Chọn mức độ phù hợp nhất với tình trạng chức năng hiện tại của bệnh nhân.
    
    **Câu hỏi then chốt:**
    1. Bệnh nhân có thể **đi lại** mà không cần người hỗ trợ không? (Dùng gậy OK)
       - Có → mRS 0-3
       - Không → mRS 4-5
    
    2. Bệnh nhân có thể **tự chăm sóc bản thân** (tắm, vệ sinh, ăn uống) không?
       - Có → mRS 0-3
       - Không → mRS 4-5
    
    3. Bệnh nhân có **nằm liệt giường** và **không tự chủ tiểu tiện** không?
       - Có → mRS 5
       - Không → mRS 0-4
    """)
    
    selected_mrs = st.radio(
        "Chọn mRS Grade:",
        list(MRS_GRADES.keys()),
        format_func=lambda x: MRS_GRADES[x]["name"],
        help="Chọn grade phù hợp nhất với khả năng chức năng của bệnh nhân"
    )
    
    # Display selected grade details
    mrs_info = MRS_GRADES[selected_mrs]
    
    with st.expander(f"📖 Chi tiết mRS {selected_mrs}", expanded=True):
        st.markdown(mrs_info["desc"])
    
    return selected_mrs, mrs_info

