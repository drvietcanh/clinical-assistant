"""
Arterial Blood Gas (ABG)
"""

import streamlit as st
from .normal_ranges import get_normal_range, is_critical, interpret_value, ALL_RANGES


def render():
    """Arterial Blood Gas"""
    st.subheader("💨 ABG - Arterial Blood Gas")
    st.caption("Khí Máu Động Mạch")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Enter Values")
        
        ph = st.number_input("pH", 6.8, 7.8, 7.40, 0.01)
        pco2 = st.number_input("PaCO₂ (mmHg)", 10.0, 100.0, 40.0, 0.1)
        po2 = st.number_input("PaO₂ (mmHg)", 30.0, 600.0, 95.0, 1.0)
        hco3 = st.number_input("HCO₃ (mEq/L)", 5.0, 50.0, 24.0, 0.1)
        fio2 = st.number_input("FiO₂ (%)", 21.0, 100.0, 21.0, 1.0)
    
    with col2:
        st.markdown("#### Interpretation")
        
        # pH
        if 7.35 <= ph <= 7.45:
            st.success(f"**pH:** {ph} - Normal ✓")
        elif ph < 7.35:
            st.error(f"**pH:** {ph} - ACIDEMIA ⚠️")
        else:
            st.error(f"**pH:** {ph} - ALKALEMIA ⚠️")
        
        # PaCO2
        if 35 <= pco2 <= 45:
            st.success(f"**PaCO₂:** {pco2} - Normal ✓")
        elif pco2 < 35:
            st.warning(f"**PaCO₂:** {pco2} - Low (respiratory alkalosis)")
        else:
            st.warning(f"**PaCO₂:** {pco2} - High (respiratory acidosis)")
        
        # HCO3
        if 22 <= hco3 <= 26:
            st.success(f"**HCO₃:** {hco3} - Normal ✓")
        elif hco3 < 22:
            st.warning(f"**HCO₃:** {hco3} - Low (metabolic acidosis)")
        else:
            st.warning(f"**HCO₃:** {hco3} - High (metabolic alkalosis)")
        
        # PaO2/FiO2 ratio
        pf_ratio = po2 / (fio2 / 100)
        st.info(f"**P/F ratio:** {pf_ratio:.0f}")
        if pf_ratio >= 400:
            st.success("Normal oxygenation ✓")
        elif pf_ratio >= 300:
            st.warning("Mild hypoxemia")
        elif pf_ratio >= 200:
            st.warning("Moderate hypoxemia (Mild ARDS)")
        elif pf_ratio >= 100:
            st.error("Severe hypoxemia (Moderate ARDS)")
        else:
            st.error("Very severe hypoxemia (Severe ARDS)")
        
        # Acid-base disorder
        st.markdown("---")
        st.markdown("**Acid-Base Disorder:**")
        
        if ph < 7.35:
            if pco2 > 45:
                st.error("**Respiratory Acidosis**")
            if hco3 < 22:
                st.error("**Metabolic Acidosis**")
        elif ph > 7.45:
            if pco2 < 35:
                st.error("**Respiratory Alkalosis**")
            if hco3 > 26:
                st.error("**Metabolic Alkalosis**")
        else:
            st.success("**Normal or Compensated**")
