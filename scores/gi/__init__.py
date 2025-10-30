"""
GI/Hepatology Scoring Systems
Gastrointestinal and Liver disease calculators
"""

from .child_pugh import render as render_child_pugh
from .meld import render as render_meld
from .meld_na import render as render_meld_na
from .ranson import render as render_ranson
from .rockall import render as render_rockall
from .glasgow_blatchford import render as render_glasgow_blatchford
from .bisap import render as render_bisap


def render_gi_calculator(calculator_id):
    """
    Route to the correct GI/Hepatology calculator based on ID
    
    Args:
        calculator_id: The ID of the calculator to render
    """
    import streamlit as st
    
    calculators = {
        "BISAP": render_bisap,
        "Child-Pugh": render_child_pugh,
        "MELD": render_meld,
        "MELD-Na": render_meld_na,
        "Ranson": render_ranson,
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
    'render_meld_na',
    'render_ranson',
    'render_rockall',
    'render_glasgow_blatchford',
]

