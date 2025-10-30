"""
GI/Hepatology Scoring Systems
Gastrointestinal and Liver disease calculators
"""

from .child_pugh import render as render_child_pugh
from .meld import render as render_meld
from .rockall import render as render_rockall
from .glasgow_blatchford import render as render_glasgow_blatchford


def render_gi_calculator(calculator_id):
    """
    Route to the correct GI/Hepatology calculator based on ID
    
    Args:
        calculator_id: The ID of the calculator to render
    """
    import streamlit as st
    
    calculators = {
        "Child-Pugh": render_child_pugh,
        "MELD": render_meld,
        "Rockall Score": render_rockall,
        "Glasgow-Blatchford": render_glasgow_blatchford,
    }
    
    calculator_func = calculators.get(calculator_id)
    if calculator_func:
        calculator_func()
    else:
        st.error(f"Calculator '{calculator_id}' not found!")


__all__ = [
    'render_gi_calculator',
    'render_child_pugh',
    'render_meld',
    'render_rockall',
    'render_glasgow_blatchford',
]

