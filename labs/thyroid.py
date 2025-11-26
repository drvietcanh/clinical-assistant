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
        st.markdown("#### 📝 Nhập Giá trị")
        
        tsh = st.number_input("TSH (mIU/L)", 0.0, 50.0, 2.0, 0.1, format="%.1f")
        ft4 = st.number_input("Free T4 (ng/dL)", 0.0, 5.0, 1.2, 0.1, format="%.1f")
        ft3 = st.number_input("Free T3 (pg/mL)", 0.0, 10.0, 3.0, 0.1, format="%.1f")
    
    with col2:
        st.markdown("#### 📊 Giải Thích")
        
        # TSH
        if 0.4 <= tsh <= 4.0:
            st.success(f"**TSH:** {tsh} - Bình thường ✓")
        elif tsh < 0.4:
            st.warning(f"**TSH:** {tsh} - Thấp (cường giáp?)")
        else:
            st.warning(f"**TSH:** {tsh} - Cao (suy giáp?)")
        
        # FT4
        if 0.8 <= ft4 <= 1.8:
            st.success(f"**Free T4:** {ft4} - Bình thường ✓")
        elif ft4 < 0.8:
            st.warning(f"**Free T4:** {ft4} - Thấp")
        else:
            st.warning(f"**Free T4:** {ft4} - Cao")
        
        # FT3
        if 2.3 <= ft3 <= 4.2:
            st.success(f"**Free T3:** {ft3} - Bình thường ✓")
        elif ft3 < 2.3:
            st.warning(f"**Free T3:** {ft3} - Thấp")
        else:
            st.warning(f"**Free T3:** {ft3} - Cao")
        
        # Pattern interpretation
        st.markdown("---")
        st.markdown("**Phân Loại:**")
        if tsh < 0.4 and ft4 > 1.8:
            st.error("⚠️ CƯỜNG GIÁP NGUYÊN PHÁT (Graves, nhân độc)")
        elif tsh > 4.0 and ft4 < 0.8:
            st.error("⚠️ SUY GIÁP NGUYÊN PHÁT (Hashimoto, thiếu iốt)")
        elif tsh > 4.0 and 0.8 <= ft4 <= 1.8:
            st.warning("⚠️ SUY GIÁP DƯỚI LÂM SÀNG")
        elif tsh < 0.4 and 0.8 <= ft4 <= 1.8:
            st.warning("⚠️ CƯỜNG GIÁP DƯỚI LÂM SÀNG")
        else:
            st.success("✓ Bình giáp (chức năng tuyến giáp bình thường)")
