"""
Symptom Checker Module - Redirected to Differential Diagnosis
This page has been integrated into the Differential Diagnosis page with Quick Mode
"""

import streamlit as st
from utils.page_helper import setup_page, render_standard_footer

# Standard page setup
setup_page(
    page_title="Kiểm tra Triệu chứng",
    page_icon="🩺",
    description="Đã được tích hợp vào Chẩn đoán phân biệt"
)

# ========== REDIRECT MESSAGE ==========
st.info("""
### 🔄 Trang này đã được tích hợp vào **Chẩn đoán phân biệt**

**Chức năng "Kiểm tra Triệu chứng" hiện có trong trang "🩺 Chẩn đoán phân biệt" với chế độ Quick Mode:**
- ✅ Nhập triệu chứng trước (Quick Mode)
- ✅ Tự động gợi ý scenario phù hợp
- ✅ Chẩn đoán phân biệt đầy đủ với scoring chi tiết
- ✅ Rule-out-first prioritization
- ✅ Demographics và risk factors
- ✅ Workup suggestions theo mức độ khẩn cấp

**Vui lòng sử dụng trang "🩺 Chẩn đoán phân biệt" thay thế.**
""")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🩺 Chuyển đến Chẩn đoán phân biệt (Quick Mode)", type="primary", use_container_width=True):
        # Set quick mode in session state before redirecting
        st.session_state['ddx_mode'] = "⚡ Chế độ nhanh (Nhập triệu chứng trước)"
        st.switch_page("pages/06_🩺_Diagnosis.py")

st.markdown("---")

# ========== SIDEBAR ==========
with st.sidebar:
    st.header("🩺 Kiểm tra Triệu chứng")
    st.caption("**Đã được tích hợp vào Chẩn đoán phân biệt**")
    
    st.markdown("---")
    st.info("""
    **📌 Lưu ý:**
    - Trang này đã được tích hợp vào **Chẩn đoán phân biệt**
    - Sử dụng chế độ **Quick Mode** trong trang Chẩn đoán phân biệt
    - Có đầy đủ tính năng và nhiều hơn so với trang cũ
    """)
    
    if st.button("🩺 Chuyển đến Chẩn đoán phân biệt", use_container_width=True):
        st.session_state['ddx_mode'] = "⚡ Chế độ nhanh (Nhập triệu chứng trước)"
        st.switch_page("pages/06_🩺_Diagnosis.py")

# Footer
render_standard_footer(disclaimer=True)

