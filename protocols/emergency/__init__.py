"""
Emergency Protocols
Sepsis, shock, and critical care protocols organized by individual files
"""

from .sepsis import render as render_sepsis
from .stroke import render as render_stroke
from .gi_bleeding import render as render_gi_bleeding
from .dka import render as render_dka
from .electrolytes import render as render_electrolytes


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
    'render_stroke',
    'render_gi_bleeding',
    'render_dka',
    'render_electrolytes',
]

