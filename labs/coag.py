"""
Coagulation Panel
"""

import streamlit as st
from .normal_ranges import get_normal_range, is_critical, interpret_value, ALL_RANGES


def render():
    """Coagulation Panel"""
    st.subheader("🩸 Coagulation Panel")
    st.caption("Đông Máu")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Enter Values")
        
        pt = st.number_input("PT (seconds)", 0.0, 100.0, 12.0, 0.1)
        inr = st.number_input("INR", 0.0, 10.0, 1.0, 0.1)
        aptt = st.number_input("aPTT (seconds)", 0.0, 150.0, 30.0, 0.1)
        d_dimer = st.number_input("D-dimer (µg/mL)", 0.0, 10.0, 0.3, 0.1)
    
    with col2:
        st.markdown("#### Interpretation")
        
        # INR
        if inr < 1.2:
            st.success(f"**INR:** {inr} - Normal ✓")
        elif inr < 2.0:
            st.info(f"**INR:** {inr} - Mildly elevated")
        elif inr <= 3.5:
            st.warning(f"**INR:** {inr} - Therapeutic range")
        elif inr < 5:
            st.warning(f"**INR:** {inr} - High ⚠️")
        else:
            st.error(f"**INR:** {inr} - CRITICALLY HIGH ⚠️")
        
        # aPTT
        if 25 <= aptt <= 35:
            st.success(f"**aPTT:** {aptt} - Normal ✓")
        elif aptt < 25:
            st.warning(f"**aPTT:** {aptt} - Short")
        elif aptt <= 80:
            st.warning(f"**aPTT:** {aptt} - Prolonged")
        else:
            st.error(f"**aPTT:** {aptt} - Markedly prolonged ⚠️")
        
        # D-dimer
        if d_dimer < 0.5:
            st.success(f"**D-dimer:** {d_dimer} - Normal ✓")
        else:
            st.warning(f"**D-dimer:** {d_dimer} - Elevated (not specific)")
    
    st.markdown("---")
    st.info("""
    **INR Therapeutic Ranges:**
    - Atrial fibrillation: 2.0-3.0
    - Mechanical valve (mitral): 2.5-3.5
    - Mechanical valve (aortic): 2.0-3.0
    - DVT/PE: 2.0-3.0
    
    **D-dimer:**
    - High sensitivity, low specificity
    - Elevated in: VTE, DIC, surgery, trauma, cancer, pregnancy
    - Normal D-dimer effectively rules out VTE
    """)
