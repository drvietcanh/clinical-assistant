"""
Basic Metabolic Panel (BMP)
"""

import streamlit as st
from .normal_ranges import get_normal_range, is_critical, interpret_value, ALL_RANGES


def render():
    """Basic Metabolic Panel"""
    st.subheader("🧪 BMP - Basic Metabolic Panel")
    st.caption("Hóa Sinh Máu Cơ Bản")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Enter Values")
        
        na = st.number_input("Sodium - Na (mEq/L)", 100.0, 180.0, 140.0, 0.1, key="na")
        k = st.number_input("Potassium - K (mEq/L)", 1.0, 10.0, 4.0, 0.1, key="k")
        cl = st.number_input("Chloride - Cl (mEq/L)", 50.0, 150.0, 100.0, 0.1, key="cl")
        co2 = st.number_input("CO2/Bicarbonate (mEq/L)", 5.0, 50.0, 25.0, 0.1, key="co2")
        bun = st.number_input("BUN (mg/dL)", 0.0, 200.0, 15.0, 0.1, key="bun")
        cr = st.number_input("Creatinine (mg/dL)", 0.0, 20.0, 1.0, 0.01, key="cr")
        glucose = st.number_input("Glucose (mg/dL)", 0.0, 600.0, 90.0, 1.0, key="glucose")
        
        # Calculate BUN/Cr ratio
        if cr > 0:
            bun_cr_ratio = bun / cr
            st.info(f"**BUN/Cr ratio:** {bun_cr_ratio:.1f}")
            if bun_cr_ratio > 20:
                st.caption("⬆️ High ratio: Prerenal azotemia, GI bleeding, high protein diet")
            elif bun_cr_ratio < 10:
                st.caption("⬇️ Low ratio: Low protein diet, liver disease, SIADH")
            else:
                st.caption("✓ Normal ratio (10-20)")
    
    with col2:
        st.markdown("#### Interpretation")
        
        results = {
            "Sodium": na,
            "Potassium": k,
            "Chloride": cl,
            "CO2": co2,
            "BUN": bun,
            "Creatinine": cr,
            "Glucose": glucose
        }
        
        for test_name, value in results.items():
            test_data = ALL_RANGES.get(test_name, {})
            interpretation = interpret_value(test_name, value)
            
            if "CRITICALLY" in interpretation:
                st.error(f"**{test_data.get('vn_name', test_name)}:** {value} - {interpretation}")
            elif "Low" in interpretation or "High" in interpretation:
                st.warning(f"**{test_data.get('vn_name', test_name)}:** {value} - {interpretation}")
            else:
                st.success(f"**{test_data.get('vn_name', test_name)}:** {value} - {interpretation}")
