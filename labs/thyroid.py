"""
Thyroid Function Tests
"""

import streamlit as st
from .normal_ranges import get_normal_range, is_critical, interpret_value, ALL_RANGES


def render():
    """Thyroid Function Tests"""
    st.subheader("🦋 Thyroid Function Tests")
    st.caption("Chức Năng Tuyến Giáp")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Enter Values")
        
        tsh = st.number_input("TSH (mIU/L)", 0.0, 50.0, 2.0, 0.1)
        ft4 = st.number_input("Free T4 (ng/dL)", 0.0, 5.0, 1.2, 0.1)
        ft3 = st.number_input("Free T3 (pg/mL)", 0.0, 10.0, 3.0, 0.1)
    
    with col2:
        st.markdown("#### Interpretation")
        
        # TSH
        if 0.4 <= tsh <= 4.0:
            st.success(f"**TSH:** {tsh} - Normal ✓")
        elif tsh < 0.4:
            st.warning(f"**TSH:** {tsh} - Low (hyperthyroidism?)")
        else:
            st.warning(f"**TSH:** {tsh} - High (hypothyroidism?)")
        
        # FT4
        if 0.8 <= ft4 <= 1.8:
            st.success(f"**Free T4:** {ft4} - Normal ✓")
        elif ft4 < 0.8:
            st.warning(f"**Free T4:** {ft4} - Low")
        else:
            st.warning(f"**Free T4:** {ft4} - High")
        
        # FT3
        if 2.3 <= ft3 <= 4.2:
            st.success(f"**Free T3:** {ft3} - Normal ✓")
        elif ft3 < 2.3:
            st.warning(f"**Free T3:** {ft3} - Low")
        else:
            st.warning(f"**Free T3:** {ft3} - High")
        
        # Pattern interpretation
        st.markdown("---")
        st.markdown("**Pattern:**")
        if tsh < 0.4 and ft4 > 1.8:
            st.error("⚠️ PRIMARY HYPERTHYROIDISM (Graves', toxic nodule)")
        elif tsh > 4.0 and ft4 < 0.8:
            st.error("⚠️ PRIMARY HYPOTHYROIDISM (Hashimoto's, iodine deficiency)")
        elif tsh > 4.0 and 0.8 <= ft4 <= 1.8:
            st.warning("⚠️ SUBCLINICAL HYPOTHYROIDISM")
        elif tsh < 0.4 and 0.8 <= ft4 <= 1.8:
            st.warning("⚠️ SUBCLINICAL HYPERTHYROIDISM")
        else:
            st.success("✓ Euthyroid (normal thyroid function)")
