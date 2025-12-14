"""
Basic Metabolic Panel (BMP)
"""

import streamlit as st
from .normal_ranges import get_normal_range, is_critical, interpret_value, ALL_RANGES


def _format_num(value: float, decimals: int = 1) -> str:
    """Format số, loại bỏ số 0 thừa"""
    rounded = round(value, decimals)
    if rounded == int(rounded):
        return str(int(rounded))
    return f"{rounded:.{decimals}f}".rstrip('0').rstrip('.')


def render():
    """Basic Metabolic Panel"""
    st.subheader("🧪 BMP - Basic Metabolic Panel")
    st.caption("Hóa Sinh Máu Cơ Bản - Chuyển đổi đơn vị SI Units ↔ Conventional")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 📝 Nhập giá trị")
        
        # Electrolytes (no conversion needed - same units)
        na = st.number_input(
            "Natri - Na (mEq/L = mmol/L)", 
            100.0, 180.0, 140.0, 0.1,
            format="%.1f",
            help="Bình thường: 136-145 mEq/L",
            key="na"
        )
        k = st.number_input(
            "Kali - K (mEq/L = mmol/L)", 
            1.0, 10.0, 4.0, 0.1,
            format="%.1f",
            help="Bình thường: 3.5-5.0 mEq/L",
            key="k"
        )
        cl = st.number_input(
            "Clo - Cl (mEq/L = mmol/L)", 
            50.0, 150.0, 100.0, 0.1,
            format="%.1f",
            help="Bình thường: 98-106 mEq/L",
            key="cl"
        )
        co2 = st.number_input(
            "CO2/Bicarbonate (mEq/L = mmol/L)", 
            5.0, 50.0, 25.0, 0.1,
            format="%.1f",
            help="Bình thường: 23-29 mEq/L",
            key="co2"
        )
        
        # BUN with unit conversion
        st.markdown("#### 🔄 BUN (Urea)")
        bun_unit = st.radio(
            "Đơn vị:",
            ["mmol/L (SI - Urea)", "mg/dL (Conventional)"],
            index=0,
            horizontal=True,
            key="bun_unit"
        )
        
        if "mmol/L" in bun_unit:
            bun_input = st.number_input(
                "Urea (mmol/L)", 
                0.0, 70.0, 5.4, 0.1,
                format="%.1f",
                help="Bình thường: 2.5-7.1 mmol/L",
                key="bun_mmol"
            )
            bun = bun_input / 0.357  # Convert to mg/dL
            st.caption(f"≈ {_format_num(bun, 1)} mg/dL (BUN)")
        else:
            bun = st.number_input(
                "BUN (mg/dL)", 
                0.0, 200.0, 15.0, 0.5,
                format="%.1f",
                help="Bình thường: 7-20 mg/dL",
                key="bun_mgdl"
            )
            st.caption(f"≈ {_format_num(bun * 0.357, 1)} mmol/L (Urea)")
        
        # Creatinine with unit conversion
        st.markdown("#### 🔄 Creatinine")
        cr_unit = st.radio(
            "Đơn vị:",
            ["µmol/L (SI - Mặc định)", "mg/dL (Conventional)"],
            horizontal=True,
            key="cr_unit_bmp"
        )
        
        if "µmol/L" in cr_unit:
            cr_input = st.number_input(
                "Creatinine (µmol/L)", 
                0.0, 1500.0, 88.0, 5.0,
                format="%d",
                help="Bình thường: 62-106 µmol/L (nam), 44-80 µmol/L (nữ)",
                key="cr_umol_bmp"
            )
            cr = cr_input / 88.4  # Convert to mg/dL
            st.caption(f"≈ {_format_num(cr, 1)} mg/dL")
        else:
            cr = st.number_input(
                "Creatinine (mg/dL)", 
                0.0, 20.0, 1.0, 0.05,
                format="%.1f",
                help="Bình thường: 0.7-1.2 mg/dL (nam), 0.5-0.9 mg/dL (nữ)",
                key="cr_mgdl_bmp"
            )
            cr_umol = round(cr * 88.4)
            st.caption(f"≈ {cr_umol} µmol/L")
        
        # Glucose with unit conversion
        st.markdown("#### 🔄 Glucose")
        glucose_unit = st.radio(
            "Đơn vị:",
            ["mmol/L (SI - Mặc định)", "mg/dL (Conventional)"],
            horizontal=True,
            key="glucose_unit"
        )
        
        if "mmol/L" in glucose_unit:
            glucose_input = st.number_input(
                "Glucose (mmol/L)", 
                0.0, 33.0, 5.0, 0.1,
                format="%.1f",
                help="Bình thường: 3.9-5.6 mmol/L (đói)",
                key="glucose_mmol"
            )
            glucose = glucose_input * 18.0  # Convert to mg/dL
            st.caption(f"≈ {round(glucose)} mg/dL")
        else:
            glucose = st.number_input(
                "Glucose (mg/dL)", 
                0.0, 600.0, 90.0, 1.0,
                format="%.0f",
                help="Bình thường: 70-100 mg/dL (đói)",
                key="glucose_mgdl"
            )
            st.caption(f"≈ {_format_num(glucose/18.0, 1)} mmol/L")
        
        # Calculate BUN/Cr ratio
        st.markdown("---")
        if cr > 0:
            bun_cr_ratio = bun / cr
            st.info(f"**Tỷ lệ BUN/Cr:** {bun_cr_ratio:.1f}")
            if bun_cr_ratio > 20:
                st.caption("⬆️ Tăng cao: Thiểu năng thận tiền thận, chảy máu tiêu hóa, chế độ ăn giàu protein")
            elif bun_cr_ratio < 10:
                st.caption("⬇️ Thấp: Chế độ ăn ít protein, bệnh gan, SIADH")
            else:
                st.caption("✓ Bình thường (10-20)")
    
    with col2:
        st.markdown("#### 📊 Giải thích kết quả")
        
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
            
            # Translate interpretation to Vietnamese
            interp_vn = interpretation
            interp_vn = interp_vn.replace("CRITICALLY High", "CỰC KỲ CAO")
            interp_vn = interp_vn.replace("CRITICALLY Low", "CỰC KỲ THẤP")
            interp_vn = interp_vn.replace("High", "Cao")
            interp_vn = interp_vn.replace("Low", "Thấp")
            interp_vn = interp_vn.replace("Normal", "Bình thường")
            
            if "CỰC KỲ" in interp_vn:
                st.error(f"**{test_data.get('vn_name', test_name)}:** {value} - {interp_vn} 🚨")
            elif "Cao" in interp_vn or "Thấp" in interp_vn:
                st.warning(f"**{test_data.get('vn_name', test_name)}:** {value} - {interp_vn}")
            else:
                st.success(f"**{test_data.get('vn_name', test_name)}:** {value} - {interp_vn} ✓")
