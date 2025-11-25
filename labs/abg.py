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
        st.markdown("#### 📝 Nhập Giá Trị")
        
        ph = st.number_input("pH", 6.8, 7.8, 7.40, 0.01, format="%.2f")
        pco2 = st.number_input("PaCO₂ (mmHg)", 10.0, 100.0, 40.0, 0.1, format="%.1f")
        po2 = st.number_input("PaO₂ (mmHg)", 30.0, 600.0, 95.0, 1.0, format="%.0f")
        hco3 = st.number_input("HCO₃ (mEq/L)", 5.0, 50.0, 24.0, 0.1, format="%.1f")
        fio2 = st.number_input("FiO₂ (%)", 21.0, 100.0, 21.0, 1.0, format="%.0f")
    
    with col2:
        st.markdown("#### 📊 Giải Thích")
        
        # pH
        if 7.35 <= ph <= 7.45:
            st.success(f"**pH:** {ph} - Bình thường ✓")
        elif ph < 7.35:
            st.error(f"**pH:** {ph} - TOAN MÁU ⚠️")
        else:
            st.error(f"**pH:** {ph} - KIỀM MÁU ⚠️")
        
        # PaCO2
        if 35 <= pco2 <= 45:
            st.success(f"**PaCO₂:** {pco2:.1f} - Bình thường ✓")
        elif pco2 < 35:
            st.warning(f"**PaCO₂:** {pco2:.1f} - Thấp (kiềm hô hấp)")
        else:
            st.warning(f"**PaCO₂:** {pco2:.1f} - Cao (toan hô hấp)")
        
        # HCO3
        if 22 <= hco3 <= 26:
            st.success(f"**HCO₃:** {hco3:.1f} - Bình thường ✓")
        elif hco3 < 22:
            st.warning(f"**HCO₃:** {hco3:.1f} - Thấp (toan chuyển hóa)")
        else:
            st.warning(f"**HCO₃:** {hco3:.1f} - Cao (kiềm chuyển hóa)")
        
        # PaO2/FiO2 ratio
        pf_ratio = po2 / (fio2 / 100)
        st.info(f"**Tỷ lệ P/F:** {pf_ratio:.0f}")
        if pf_ratio >= 400:
            st.success("Oxy hóa bình thường ✓")
        elif pf_ratio >= 300:
            st.warning("Thiếu oxy nhẹ")
        elif pf_ratio >= 200:
            st.warning("Thiếu oxy trung bình (ARDS nhẹ)")
        elif pf_ratio >= 100:
            st.error("Thiếu oxy nặng (ARDS trung bình)")
        else:
            st.error("Thiếu oxy rất nặng (ARDS nặng)")
        
        # Acid-base disorder
        st.markdown("---")
        st.markdown("**Rối Loạn Acid-Base:**")
        
        if ph < 7.35:
            if pco2 > 45:
                st.error("**Toan hô hấp**")
            if hco3 < 22:
                st.error("**Toan Chuyển Hóa**")
        elif ph > 7.45:
            if pco2 < 35:
                st.error("**Kiềm hô hấp**")
            if hco3 > 26:
                st.error("**Kiềm Chuyển Hóa**")
        else:
            st.success("**Bình Thường hoặc Đã Bù**")
