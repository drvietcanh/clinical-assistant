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

# Main tabs for organizing sub-modules
main_tabs = st.tabs([
    "🩺 Differential Diagnosis",
    "📖 Disease Encyclopedia",
    "🏷️ ICD-10 Lookup",
    "📚 In-Depth Articles",
    "👥 Patient Education"
])

# Tab 1: Differential Diagnosis
with main_tabs[0]:
    render_ddx_interface()

# Tab 2: Disease Encyclopedia
with main_tabs[1]:
    st.info("📖 **Disease Encyclopedia** - Đang tích hợp.")
    if st.button("Mở Disease Encyclopedia", use_container_width=True):
        st.switch_page("pages/16_📖_Disease_Encyclopedia.py")

# Tab 3: ICD-10 Lookup
with main_tabs[2]:
    st.info("🏷️ **ICD-10 Lookup** - Đang tích hợp.")
    if st.button("Mở ICD-10 Lookup", use_container_width=True):
        st.switch_page("pages/13_🏷️_ICD10_Lookup.py")

# Tab 4: In-Depth Articles
with main_tabs[3]:
    st.info("📚 **In-Depth Articles** - Đang tích hợp.")
    if st.button("Mở In-Depth Articles", use_container_width=True):
        st.switch_page("pages/12_📚_In_Depth_Articles.py")

# Tab 5: Patient Education
with main_tabs[4]:
    st.info("👥 **Patient Education** - Đang tích hợp.")
    if st.button("Mở Patient Education", use_container_width=True):
        st.switch_page("pages/19_👥_Patient_Education.py")

# ========== FOOTER ==========
render_standard_footer(disclaimer=True)

