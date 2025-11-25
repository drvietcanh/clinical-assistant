"""
Nursing Care Scales Module
Thang điểm chăm sóc điều dưỡng
"""

from .braden import render as render_braden
from .morse import render as render_morse


def render_nursing_calculator(calculator_id: str):
    """Route to appropriate nursing calculator"""
    calculators = {
        "Braden": render_braden,
        "Morse": render_morse,
    }
    
    if calculator_id in calculators:
        calculators[calculator_id]()
    else:
        import streamlit as st
        st.error(f"Calculator '{calculator_id}' not found in nursing module")

