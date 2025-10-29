"""
Emergency Protocols
Sepsis, shock, and critical care protocols organized by individual files
"""

from .sepsis import render as render_sepsis


def render_shock():
    """Shock Management Protocol - Placeholder"""
    import streamlit as st
    st.subheader("💔 Quản Lý Sốc")
    st.caption("Phân Loại và Xử Trí Sốc")
    st.warning("🚧 **Đang phát triển** - Dự kiến hoàn thành: Tuần 2")
    st.info("""
    **Các loại sốc:**
    - Sốc nhiễm trùng (Septic shock)
    - Sốc giảm thể tích (Hypovolemic shock)
    - Sốc tim (Cardiogenic shock)
    - Sốc phân bố (Distributive shock)
    - Sốc tắc nghẽn (Obstructive shock)
    """)


__all__ = [
    'render_sepsis',
    'render_shock',
]

