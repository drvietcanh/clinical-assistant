"""
FENa Calculator - Input Form UI Components
Handles all input fields and form sections
"""

import streamlit as st


def _format_num(value: float, decimals: int = 1) -> str:
    """Format số, loại bỏ số 0 thừa"""
    rounded = round(value, decimals)
    if rounded == int(rounded):
        return str(int(rounded))
    return f"{rounded:.{decimals}f}".rstrip('0').rstrip('.')


def render_input_form():
    """
    Render the input form section for FENa calculator
    
    Returns:
        dict: Input values with keys: p_na, p_cr_mgdl, u_na, u_cr_mgdl, on_diuretics
    """
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 🔬 Xét nghiệm máu (Plasma)")
        
        # Plasma Sodium
        p_na = st.number_input(
            "**Plasma Sodium (P-Na)** mEq/L:",
            min_value=100.0,
            max_value=180.0,
            value=140.0,
            step=1.0,
            format="%.1f",
            help="Bình thường: 135-145 mEq/L"
        )
        
        # Plasma Creatinine
        st.markdown("#### Plasma Creatinine (P-Cr)")
        p_cr_unit = st.radio(
            "Đơn vị:",
            ["mg/dL", "µmol/L (SI)"],
            horizontal=True,
            key="p_cr_unit"
        )
        
        if "mg/dL" in p_cr_unit:
            p_cr = st.number_input(
                "P-Cr (mg/dL):",
                min_value=0.1,
                max_value=20.0,
                value=1.5,
                step=0.1,
                format="%.1f",
                help="Bình thường: 0.7-1.3 mg/dL"
            )
            p_cr_mgdl = p_cr
            p_cr_umol = round(p_cr * 88.4)
            st.caption(f"≈ {p_cr_umol} µmol/L")
        else:
            p_cr = st.number_input(
                "P-Cr (µmol/L):",
                min_value=0.0,
                max_value=1800.0,
                value=133.0,
                step=5.0,
                format="%d",
                help="Bình thường: 62-115 µmol/L"
            )
            p_cr_mgdl = p_cr / 88.4
            st.caption(f"≈ {_format_num(p_cr_mgdl, 1)} mg/dL")
        
        st.markdown("---")
        st.markdown("### 💧 Xét nghiệm nước tiểu (Urine)")
        
        # Urine Sodium
        u_na = st.number_input(
            "**Urine Sodium (U-Na)** mEq/L:",
            min_value=1.0,
            max_value=300.0,
            value=20.0,
            step=1.0,
            format="%.1f",
            help="Random urine sample"
        )
        
        # Urine Creatinine
        st.markdown("#### Urine Creatinine (U-Cr)")
        u_cr_unit = st.radio(
            "Đơn vị:",
            ["mg/dL", "mmol/L (SI)"],
            horizontal=True,
            key="u_cr_unit"
        )
        
        if "mg/dL" in u_cr_unit:
            u_cr = st.number_input(
                "U-Cr (mg/dL):",
                min_value=1.0,
                max_value=500.0,
                value=50.0,
                step=5.0,
                format="%.1f",
                help="Varies widely"
            )
            u_cr_mgdl = u_cr
            st.caption(f"≈ {_format_num(u_cr / 11.3, 1)} mmol/L")
        else:
            u_cr = st.number_input(
                "U-Cr (mmol/L):",
                min_value=0.1,
                max_value=50.0,
                value=4.4,
                step=0.5,
                format="%.1f",
                help="Varies widely"
            )
            u_cr_mgdl = u_cr * 11.3
            st.caption(f"≈ {round(u_cr_mgdl)} mg/dL")
        
        st.markdown("---")
        
        # Check if on diuretics
        on_diuretics = st.checkbox(
            "⚠️ Bệnh nhân đang dùng lợi tiểu (diuretics)",
            help="FENa không đáng tin cậy nếu dùng lợi tiểu. Cân nhắc dùng FEUrea thay thế."
        )
        
        if on_diuretics:
            st.warning("""
            **Lưu ý:** Lợi tiểu làm tăng FENa giả tạo
            
            → FENa không đáng tin cậy!
            
            **Khuyến nghị:** Dùng **FEUrea** thay thế (không bị ảnh hưởng bởi lợi tiểu)
            """)
    
    return {
        "p_na": p_na,
        "p_cr_mgdl": p_cr_mgdl,
        "u_na": u_na,
        "u_cr_mgdl": u_cr_mgdl,
        "on_diuretics": on_diuretics
    }

