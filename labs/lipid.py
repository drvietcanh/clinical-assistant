"""
Lipid Panel
"""

import streamlit as st
from .normal_ranges import get_normal_range, is_critical, interpret_value, ALL_RANGES


def render():
    """Lipid Panel"""
    st.subheader("💊 Lipid Panel")
    st.caption("Mỡ Máu")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Enter Values")
        
        chol = st.number_input("Total Cholesterol (mg/dL)", 0.0, 500.0, 180.0, 1.0)
        ldl = st.number_input("LDL Cholesterol (mg/dL)", 0.0, 300.0, 100.0, 1.0)
        hdl = st.number_input("HDL Cholesterol (mg/dL)", 0.0, 150.0, 50.0, 1.0)
        tg = st.number_input("Triglycerides (mg/dL)", 0.0, 1000.0, 120.0, 1.0)
        
        # Calculate ratios
        if hdl > 0:
            chol_hdl = chol / hdl
            st.info(f"**Total Chol/HDL ratio:** {chol_hdl:.1f}")
            if chol_hdl > 5:
                st.caption("⬆️ High risk (>5)")
            elif chol_hdl < 3.5:
                st.caption("✓ Low risk (<3.5)")
            else:
                st.caption("⚠️ Average risk (3.5-5)")
    
    with col2:
        st.markdown("#### Interpretation")
        
        # Total Cholesterol
        if chol < 200:
            st.success(f"**Total Cholesterol:** {chol} - Desirable ✓")
        elif chol < 240:
            st.warning(f"**Total Cholesterol:** {chol} - Borderline high ⚠️")
        else:
            st.error(f"**Total Cholesterol:** {chol} - High ⬆️")
        
        # LDL
        if ldl < 100:
            st.success(f"**LDL:** {ldl} - Optimal ✓")
        elif ldl < 130:
            st.info(f"**LDL:** {ldl} - Near optimal")
        elif ldl < 160:
            st.warning(f"**LDL:** {ldl} - Borderline high ⚠️")
        elif ldl < 190:
            st.error(f"**LDL:** {ldl} - High ⬆️")
        else:
            st.error(f"**LDL:** {ldl} - Very high ⬆️⬆️")
        
        # HDL
        if hdl < 40:
            st.error(f"**HDL:** {hdl} - Low (⬇️ risk factor)")
        elif hdl < 60:
            st.success(f"**HDL:** {hdl} - Normal ✓")
        else:
            st.success(f"**HDL:** {hdl} - High (✓ protective)")
        
        # Triglycerides
        if tg < 150:
            st.success(f"**Triglycerides:** {tg} - Normal ✓")
        elif tg < 200:
            st.warning(f"**Triglycerides:** {tg} - Borderline high ⚠️")
        elif tg < 500:
            st.error(f"**Triglycerides:** {tg} - High ⬆️")
        else:
            st.error(f"**Triglycerides:** {tg} - Very high ⬆️⬆️")
    
    st.markdown("---")
    st.info("""
    **LDL Goals by Risk:**
    - Very high risk (CAD, DM): <70 mg/dL
    - High risk (2+ risk factors): <100 mg/dL
    - Moderate risk: <130 mg/dL
    - Low risk: <160 mg/dL
    """)
