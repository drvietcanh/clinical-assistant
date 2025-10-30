"""
Respiratory Scoring Systems
All respiratory and pulmonary calculators organized by individual files
"""

from .curb65 import render as render_curb65
from .psi_port import render as render_psi_port
from .wells_pe import render as render_wells_pe
from .smartcop import render as render_smartcop
from .bode import render as render_bode


def render_bode():
    """BODE Index Calculator - Placeholder"""
    import streamlit as st
    st.subheader("🫁 BODE Index")
    st.caption("Tiên Lượng COPD")
    st.warning("🚧 **Đang phát triển** - Dự kiến hoàn thành: Tuần 4")


def render_respiratory_calculator(calculator_id):
    """
    Route to the correct respiratory calculator based on ID
    
    Args:
        calculator_id: The ID of the calculator to render
    """
    import streamlit as st
    
    calculators = {
        "CURB-65": render_curb65,
        "PSI/PORT": render_psi_port,
        "SMART-COP": render_smartcop,
        "BODE Index": render_bode,
        "Wells PE": render_wells_pe,
    }
    
    calculator_func = calculators.get(calculator_id)
    if calculator_func:
        calculator_func()
    else:
        st.error(f"Calculator '{calculator_id}' not found!")


__all__ = [
    'render_respiratory_calculator',
    'render_curb65',
    'render_psi_port',
    'render_smartcop',
    'render_bode',
    'render_wells_pe',
]

