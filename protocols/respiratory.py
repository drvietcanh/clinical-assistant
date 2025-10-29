"""
Respiratory Protocols
COPD, Asthma, and respiratory emergency protocols
"""

import streamlit as st


def render_copd():
    """COPD Exacerbation Protocol"""
    st.subheader("🫁 COPD Exacerbation")
    st.caption("Cơn Cấp COPD - Xử Trí Theo GOLD 2023")
    
    st.warning("🚧 **Đang phát triển** - Dự kiến hoàn thành: Tuần 2")
    
    st.info("""
    **COPD exacerbation protocol:**
    - Đánh giá mức độ nặng
    - Bronchodilators
    - Corticosteroids
    - Antibiotics (nếu có chỉ định)
    - Oxygen therapy
    - NIV criteria
    """)


def render_asthma():
    """Acute Asthma Protocol"""
    st.subheader("🫁 Cơn Hen Cấp")
    st.caption("Xử Trí Cơn Hen Theo GINA")
    
    st.warning("🚧 **Đang phát triển** - Dự kiến hoàn thành: Tuần 2")
    
    st.info("""
    **Acute asthma management:**
    - Phân loại mức độ nặng
    - SABA + Anticholinergics
    - Corticosteroids
    - Magnesium sulfate
    - Tiêu chí nhập ICU
    """)

