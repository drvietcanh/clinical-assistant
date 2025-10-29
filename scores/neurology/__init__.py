"""
Neurology Scoring Systems
All neurological assessment calculators organized by individual files
"""

from .gcs import render as render_gcs


def render_nihss():
    """NIHSS Score Calculator - Placeholder"""
    import streamlit as st
    st.subheader("🧠 NIHSS - NIH Stroke Scale")
    st.caption("Mức Độ Nặng Đột Quỵ")
    st.warning("🚧 **Đang phát triển** - Dự kiến hoàn thành: Tuần 2")
    st.info("""
    **NIHSS đánh giá:**
    - Level of consciousness
    - Gaze
    - Visual fields
    - Facial palsy
    - Motor arm/leg
    - Ataxia
    - Sensory
    - Language
    - Dysarthria
    - Extinction/inattention
    
    **Tổng điểm:** 0-42
    """)


def render_ich_score():
    """ICH Score Calculator - Placeholder"""
    import streamlit as st
    st.subheader("🧠 ICH Score")
    st.caption("Tiên Lượng Xuất Huyết Nội Sọ")
    st.warning("🚧 **Đang phát triển** - Dự kiến hoàn thành: Tuần 3")


def render_hunt_hess():
    """Hunt & Hess Scale Calculator - Placeholder"""
    import streamlit as st
    st.subheader("🧠 Hunt & Hess Scale")
    st.caption("Phân Loại Xuất Huyết Dưới Nhện")
    st.warning("🚧 **Đang phát triển** - Dự kiến hoàn thành: Tuần 3")


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
        "ICH Score": render_ich_score,
        "Hunt & Hess": render_hunt_hess,
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

