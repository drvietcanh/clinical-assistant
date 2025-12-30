"""
Diagnosis Module - Differential Diagnosis Generator
Main Router - Imports from diagnosis module
"""

import streamlit as st
from utils.page_helper import setup_page, render_standard_footer
from components.ui import render_info_box, render_hero

from diagnosis import render_ddx_interface

# Standard page setup
setup_page(
    page_title="Chẩn đoán phân biệt",
    page_icon="🩺",
    description="Công cụ hỗ trợ tạo danh sách chẩn đoán phân biệt"
)

# ========== SIDEBAR ==========
with st.sidebar:
    st.header("🩺 Chẩn đoán & Bài viết")
    st.caption("Module **Chẩn đoán phân biệt** – sub-module nhóm *🩺 Chẩn đoán & Bài viết*.")
    
    with st.expander("Liên kết trong nhóm Chẩn đoán & Bài viết", expanded=False):
        col1, col2 = st.columns(2)
        with col1:
            if st.button("📚 Bài viết chuyên sâu", use_container_width=True):
                st.switch_page("pages/12_📚_In_Depth_Articles.py")
        with col2:
            if st.button("📊 Thang điểm & Scores", use_container_width=True):
                st.switch_page("pages/01_📊_Scores.py")
    
    st.markdown("---")
    render_info_box(
        """
        **Chức năng chính:**
        - Gợi ý danh sách chẩn đoán phân biệt theo triệu chứng và hệ cơ quan
        - Liên kết trực tiếp với calculators và phác đồ điều trị liên quan
        
        **Lưu ý:** Công cụ chỉ hỗ trợ, **không thay thế đánh giá lâm sàng**.
        """,
        type="info",
        title="Thông tin Module"
    )

# ========== MAIN CONTENT ==========

# Render DDx interface
render_ddx_interface()

# ========== FOOTER ==========
render_standard_footer(disclaimer=True)

