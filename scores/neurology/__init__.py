"""
Neurology Scoring Systems
All neurological assessment calculators organized by individual files
"""

from .gcs import render as render_gcs
from .nihss import render as render_nihss
from .ich_score import render as render_ich_score
from .hunt_hess import render as render_hunt_hess


def render_mrs():
    """Modified Rankin Scale Calculator - Placeholder"""
    import streamlit as st
    st.subheader("🧠 mRS - Modified Rankin Scale")
    st.caption("Mức Độ Khuyết Tật Sau Đột Quỵ")
    st.warning("🚧 **Đang phát triển** - Dự kiến hoàn thành: Tuần 3")


def render_neurology_calculator(calculator_id):
    """
    Route to the correct neurology calculator based on ID
    
    Args:
        calculator_id: The ID of the calculator to render
    """
    import streamlit as st
    
    calculators = {
        "GCS": render_gcs,
        "NIHSS": render_nihss,
        "ICH Score": render_ich_score,  # ✅ Implemented
        "Hunt & Hess": render_hunt_hess,  # ✅ Implemented
        "mRS": render_mrs,
    }
    
    calculator_func = calculators.get(calculator_id)
    if calculator_func:
        calculator_func()
    else:
        st.error(f"Calculator '{calculator_id}' not found!")


__all__ = [
    'render_neurology_calculator',
    'render_gcs',
    'render_nihss',
    'render_ich_score',
    'render_hunt_hess',
    'render_mrs',
]

