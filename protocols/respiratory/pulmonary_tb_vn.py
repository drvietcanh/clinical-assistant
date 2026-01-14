"""
Pulmonary Tuberculosis Protocol (VN Local)

Wrapper around the existing TB protocol with Vietnam-oriented workflow notes.
"""

import streamlit as st

from .pulmonary_tb import render as render_tb_core


def render():
    st.subheader("🫁 Lao phổi (VN Protocol)")
    st.caption("Khung VN (CTCLQG Lao & Bệnh phổi / Bộ Y tế) – bổ sung quy trình thực hành tại VN")

    st.info(
        """
        **Ghi chú triển khai (VN):**
        - Sẽ bổ sung luồng báo cáo/ghi nhận theo CTCLQG, chỉ định xét nghiệm và chuyển tuyến.
        - Ưu tiên: kiểm soát lây nhiễm, GeneXpert/Xpert Ultra, đánh giá kháng Rifampicin, liên hệ chương trình chống lao.
        """
    )

    st.markdown("---")
    render_tb_core()

