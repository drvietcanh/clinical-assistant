"""
SCORE2-OP Calculator
Cardiovascular risk for older persons (≥70 years)
"""

import streamlit as st


def render():
    """SCORE2-OP Calculator"""
    st.subheader("👴 SCORE2-OP - ESC 2021")
    st.caption("Đánh Giá Nguy Cơ Tim Mạch Ở Người Cao Tuổi (≥70 tuổi)")
    
    st.info("""
    **SCORE2-OP (Older Persons) dành cho người ≥70 tuổi**
    
    Dự đoán nguy cơ 5-10 năm mắc bệnh tim mạch.
    """)
    
    st.warning("🚧 **Đang phát triển** - Sẽ sớm hoàn thành!")
    
    st.markdown("---")
    st.caption("⚠️ Công cụ hỗ trợ lâm sàng - không thay thế đánh giá lâm sàng toàn diện")

