"""
FENa Calculator - Kết quảs Display UI Components
Handles all results display sections
"""

import streamlit as st
from config.theme import COLORS


def render_results_display(fena, interpretation, on_diuretics):
    """
    Render results display section
    
    Args:
        fena: Calculated FENa value
        interpretation: dict with keys: interpretation, color, cause
        on_diuretics: bool indicating if patient is on diuretics
    """
    st.markdown("### 📊 Kết quả")
    
    color = interpretation["color"]
    interpretation_text = interpretation["interpretation"]
    cause = interpretation["cause"]
    
    if color == COLORS["info"]:
        st.info(f"""
        **FENa = {fena:.2f}%**
        
        **{interpretation_text}**
        
        {cause}
        """)
    elif color == COLORS["warning"]:
        st.warning(f"""
        **FENa = {fena:.2f}%**
        
        **{interpretation_text}**
        
        {cause}
        """)
    else:
        st.error(f"""
        **FENa = {fena:.2f}%**
        
        **{interpretation_text}**
        
        {cause}
        """)
    
    st.caption("< 1%: Prerenal | > 2%: Intrinsic")
    
    if on_diuretics:
        st.error(f"""
        ⚠️ **CẢNH BÁO:** Bệnh nhân đang dùng lợi tiểu!
        
        FENa = {fena:.2f}% có thể KHÔNG chính xác.
        
        Lợi tiểu làm tăng FENa giả tạo → Có thể chẩn đoán nhầm prerenal thành intrinsic renal.
        
        **Khuyến nghị:** Dùng FEUrea hoặc đánh giá lâm sàng.
        """)


def render_calculation_details(u_na, p_na, u_cr_mgdl, p_cr_mgdl, fena):
    """
    Render calculation details expander
    
    Args:
        u_na: Urine Sodium
        p_na: Plasma Sodium
        u_cr_mgdl: Urine Creatinine (mg/dL)
        p_cr_mgdl: Plasma Creatinine (mg/dL)
        fena: Calculated FENa value
    """
    with st.expander("🧮 Chi tiết tính toán"):
        st.markdown(f"""
        **Công thức FENa:**
        ```
        FENa (%) = (U-Na × P-Cr) / (P-Na × U-Cr) × 100
        ```
        
        **Giá trị của bạn:**
        - U-Na = {u_na:.1f} mEq/L
        - P-Na = {p_na:.1f} mEq/L
        - U-Cr = {u_cr_mgdl:.1f} mg/dL
        - P-Cr = {p_cr_mgdl:.1f} mg/dL
        
        **Tính toán:**
        ```
        FENa = ({u_na:.1f} × {p_cr_mgdl:.1f}) / ({p_na:.1f} × {u_cr_mgdl:.1f}) × 100
        FENa = {(u_na * p_cr_mgdl):.1f} / {(p_na * u_cr_mgdl):.1f} × 100
        FENa = {fena:.2f}%
        ```
        
        **Giải thích:**
        - Tử số: U-Na × P-Cr = Lượng Na được lọc
        - Mẫu số: P-Na × U-Cr = Lượng Na được thải
        - Ratio × 100 = % Na được lọc ra nước tiểu
        """)

