"""
Dengue Fever Protocol (VN Local)

Wrapper around the existing Dengue protocol with Vietnam-oriented notes.
"""

import streamlit as st

from .dengue_fever import render as render_dengue_core


def render():
    st.subheader("🦟 Sốt Xuất huyết Dengue (VN Protocol)")
    st.caption("Khung VN (Bộ Y tế/CTCLQG) – hiện là bản ghi chú bổ sung, vẫn dùng nội dung WHO hiện có")

    st.info(
        """
        **Ghi chú triển khai (VN):**
        - Sẽ bổ sung liên kết/tóm tắt theo tài liệu chính thức Bộ Y tế và hướng dẫn tuyến cơ sở/tuyến tỉnh.
        - Ưu tiên: phân tầng dấu hiệu cảnh báo, chỉ định nhập viện, phác đồ dịch theo Hct và mạch/HA.
        """
    )

    st.markdown("---")
    render_dengue_core()

