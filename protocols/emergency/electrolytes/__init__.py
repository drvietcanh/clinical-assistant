"""
Electrolyte Emergency Protocols Module
"""

import streamlit as st
from .hyperkalemia import render as render_hyperkalemia
from .hyponatremia import render as render_hyponatremia
from .hypomagnesemia import render as render_hypomagnesemia
from .hypophosphatemia import render as render_hypophosphatemia
from .hypocalcemia import render as render_hypocalcemia


def render():
    """Electrolyte Emergency Protocols"""
    st.subheader("⚡ Electrolyte Emergency Protocols")
    st.caption("Hyperkalemia, Hyponatremia, Hypomagnesemia, Hypophosphatemia, Hypocalcemia")
    
    st.markdown("---")
    
    # Electrolyte selection
    electrolyte = st.radio(
        "**Chọn tình trạng:**",
        [
            "Hyperkalemia (Tăng kali máu)",
            "Hyponatremia (Hạ natri máu)",
            "Hypomagnesemia (Hạ magie máu)",
            "Hypophosphatemia (Hạ phospho máu)",
            "Hypocalcemia (Hạ canxi máu)"
        ],
        key="electrolyte_type"
    )
    
    st.markdown("---")
    
    if "Hyperkalemia" in electrolyte:
        render_hyperkalemia()
    elif "Hyponatremia" in electrolyte:
        render_hyponatremia()
    elif "Hypomagnesemia" in electrolyte or "magie" in electrolyte.lower():
        render_hypomagnesemia()
    elif "Hypophosphatemia" in electrolyte or "phospho" in electrolyte.lower():
        render_hypophosphatemia()
    elif "Hypocalcemia" in electrolyte or "canxi" in electrolyte.lower():
        render_hypocalcemia()


__all__ = [
    'render',
    'render_hyperkalemia',
    'render_hyponatremia',
    'render_hypomagnesemia',
    'render_hypophosphatemia',
    'render_hypocalcemia'
]

