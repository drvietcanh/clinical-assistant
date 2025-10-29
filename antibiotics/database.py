"""
Antibiotic Database and Lookup Functions
"""

import streamlit as st
import pandas as pd


def render_antibiotic_lookup():
    """Antibiotic Lookup Tool"""
    st.subheader("🔍 Tra Cứu Kháng Sinh")
    st.caption("Tìm kiếm thông tin kháng sinh theo tên hoặc chỉ định")
    
    st.warning("🚧 **Đang phát triển** - Dự kiến hoàn thành: Tuần 2")
    
    st.info("""
    **Tra cứu kháng sinh:**
    - Liều dùng chuẩn
    - Điều chỉnh theo chức năng thận
    - Chỉ định
    - Tác dụng phụ
    - Tương tác thuốc
    """)
    
    # Preview
    search = st.text_input("🔍 Tìm kiếm kháng sinh:", placeholder="Ví dụ: Ceftriaxone, Sepsis...")
    
    if search:
        st.info(f"Đang tìm kiếm: **{search}**")
        st.write("Kết quả sẽ hiển thị ở đây khi hoàn thành...")


def render_database():
    """Antibiotic Database Viewer"""
    st.subheader("📊 Cơ Sở Dữ Liệu Kháng Sinh")
    st.caption("Danh sách đầy đủ kháng sinh và hướng dẫn sử dụng")
    
    st.warning("🚧 **Đang phát triển** - Dự kiến hoàn thành: Tuần 3")
    
    st.info("""
    **Cơ sở dữ liệu bao gồm:**
    - Danh sách kháng sinh
    - Phân loại theo nhóm
    - Liều dùng chi tiết
    - Điều chỉnh theo chức năng thận/gan
    - Guidelines quốc tế
    """)

