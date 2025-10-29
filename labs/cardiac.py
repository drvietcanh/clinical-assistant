"""
Cardiac Markers
"""

import streamlit as st
from .normal_ranges import get_normal_range, is_critical, interpret_value, ALL_RANGES


def render():
    """Cardiac Markers"""
    st.subheader("❤️ Cardiac Markers")
    st.caption("Dấu Ấn Tim Mạch")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Enter Values")
        
        trop_i = st.number_input("Troponin I (ng/mL)", 0.0, 10.0, 0.02, 0.01)
        bnp = st.number_input("BNP (pg/mL)", 0.0, 5000.0, 50.0, 10.0)
        ckmb = st.number_input("CK-MB (ng/mL)", 0.0, 50.0, 2.0, 0.1)
    
    with col2:
        st.markdown("#### Interpretation")
        
        # Troponin I
        if trop_i < 0.04:
            st.success(f"**Troponin I:** {trop_i} - Normal ✓")
        else:
            st.error(f"**Troponin I:** {trop_i} - ELEVATED ⚠️ (suggests MI)")
        
        # BNP
        if bnp < 100:
            st.success(f"**BNP:** {bnp} - Normal ✓")
        elif bnp < 400:
            st.warning(f"**BNP:** {bnp} - Borderline")
        else:
            st.error(f"**BNP:** {bnp} - Elevated (suggests HF)")
        
        # CK-MB
        if ckmb < 5:
            st.success(f"**CK-MB:** {ckmb} - Normal ✓")
        else:
            st.warning(f"**CK-MB:** {ckmb} - Elevated")
    
    st.markdown("---")
    st.info("""
    **Troponin:** Rises 3-4h after MI, peaks 12-24h, stays elevated 7-10 days
    
    **BNP:** 
    - <100: HF unlikely
    - 100-400: Possible HF
    - >400: HF likely
    
    **CK-MB:** Less specific than troponin, can be elevated in muscle injury
    """)
