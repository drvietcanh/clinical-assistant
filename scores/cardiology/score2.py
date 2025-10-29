"""
SCORE2 Calculator
10-year cardiovascular risk for ages 40-69
"""

import streamlit as st


def render():
    """SCORE2 Calculator"""
    st.subheader("📊 SCORE2 - ESC 2021")
    st.caption("Đánh Giá Nguy Cơ Bệnh Tim Mạch 10 Năm (40-69 tuổi)")
    
    st.info("""
    **SCORE2 dự đoán nguy cơ 10 năm mắc:**
    - Nhồi máu cơ tim (tử vong + không tử vong)
    - Đột quỵ (tử vong + không tử vong)
    """)
    
    st.warning("🚧 **Đang phát triển** - Sẽ sớm hoàn thành với đầy đủ tính năng chuyển đổi đơn vị!")
    
    st.markdown("---")
    st.caption("⚠️ Công cụ hỗ trợ lâm sàng - không thay thế đánh giá lâm sàng toàn diện")

