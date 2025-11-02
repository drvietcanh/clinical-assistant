"""
Comprehensive Metabolic Panel (CMP)
"""

import streamlit as st
from .normal_ranges import get_normal_range, is_critical, interpret_value, ALL_RANGES


def render():
    """Comprehensive Metabolic Panel"""
    st.subheader("🧪 CMP - Comprehensive Metabolic Panel")
    st.caption("CMP = BMP + LFT")
    
    st.info("CMP bao gồm tất cả các xét nghiệm trong BMP và một số xét nghiệm gan")
    
    tabs = st.tabs(["BMP Components", "Liver Components", "Additional"])
    
    with tabs[0]:
        render_bmp()
    
    with tabs[1]:
        col1, col2 = st.columns(2)
        
        with col1:
            albumin = st.number_input("Albumin (g/dL)", 0.0, 10.0, 4.0, 0.1, format="%.1f")
            total_protein = st.number_input("Total Protein (g/dL)", 0.0, 15.0, 7.0, 0.1)
            calcium = st.number_input("Calcium (mg/dL)", 0.0, 20.0, 9.5, 0.1)
        
        with col2:
            for test_name, value in [("Albumin", albumin), ("Total_Protein", total_protein), ("Calcium", calcium)]:
                test_data = ALL_RANGES.get(test_name, {})
                interpretation = interpret_value(test_name, value)
                
                if "CRITICALLY" in interpretation:
                    st.error(f"**{test_data.get('vn_name', test_name)}:** {value} - {interpretation}")
                elif "Low" in interpretation or "High" in interpretation:
                    st.warning(f"**{test_data.get('vn_name', test_name)}:** {value} - {interpretation}")
                else:
                    st.success(f"**{test_data.get('vn_name', test_name)}:** {value} - {interpretation}")
