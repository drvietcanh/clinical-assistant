"""
Liver Function Tests (LFT)
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
    """Liver Function Tests"""
    st.subheader("🫀 LFT - Liver Function Tests")
    st.caption("Chức Năng Gan - Chuyển đổi đơn vị Bilirubin µmol/L ↔ mg/dL")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 📝 Nhập Giá trị")
        
        alt = st.number_input("ALT/SGPT (U/L)", 0.0, 1000.0, 30.0, 1.0, format="%.0f")
        ast = st.number_input("AST/SGOT (U/L)", 0.0, 1000.0, 25.0, 1.0, format="%.0f")
        alp = st.number_input("ALP (U/L)", 0.0, 1000.0, 80.0, 1.0, format="%.0f")
        
        # Bilirubin with unit conversion
        st.markdown("#### 🔄 Bilirubin")
        bili_unit = st.radio(
            "Đơn vị Bilirubin:",
            ["µmol/L (SI - Mặc định)", "mg/dL (Conventional)"],
            horizontal=True,
            key="bili_unit"
        )
        
        use_si_bili = "µmol/L" in bili_unit
        
        # Total Bilirubin
        if use_si_bili:
            bili_t_input = st.number_input(
                "Bilirubin Total (µmol/L)",
                0.0, 500.0, 13.7, 1.0,
                format="%.1f",
                help="Bình thường: 3-17 µmol/L",
                key="bili_t_umol"
            )
            bili_t = bili_t_input / 17.1  # Convert to mg/dL
            st.caption(f"≈ {_format_num(bili_t, 2)} mg/dL")
        else:
            bili_t = st.number_input(
                "Bilirubin Total (mg/dL)",
                0.0, 30.0, 0.8, 0.1,
                format="%.1f",
                help="Bình thường: 0.2-1.0 mg/dL",
                key="bili_t_mgdl"
            )
            st.caption(f"≈ {_format_num(bili_t * 17.1, 1)} µmol/L")
        
        # Direct Bilirubin
        if use_si_bili:
            bili_d_input = st.number_input(
                "Bilirubin Direct (µmol/L)",
                0.0, 250.0, 3.4, 0.5,
                format="%.1f",
                help="Bình thường: 0-5 µmol/L",
                key="bili_d_umol"
            )
            bili_d = bili_d_input / 17.1  # Convert to mg/dL
            st.caption(f"≈ {_format_num(bili_d, 1)} mg/dL")
        else:
            bili_d = st.number_input(
                "Bilirubin Direct (mg/dL)",
                0.0, 15.0, 0.2, 0.1,
                format="%.1f",
                help="Bình thường: 0-0.3 mg/dL",
                key="bili_d_mgdl"
            )
            st.caption(f"≈ {_format_num(bili_d * 17.1, 1)} µmol/L")
        
        # Calculate indirect bilirubin
        bili_i = bili_t - bili_d
        if use_si_bili:
            st.info(f"**Bilirubin Indirect:** {bili_i * 17.1:.1f} µmol/L (≈ {bili_i:.1f} mg/dL)")
        else:
            st.info(f"**Bilirubin Indirect:** {bili_i:.1f} mg/dL (≈ {bili_i * 17.1:.1f} µmol/L)")
        
        st.markdown("---")
        albumin = st.number_input("Albumin (g/dL)", 0.0, 10.0, 4.0, 0.1, format="%.1f", key="lft_alb")
        tp = st.number_input("Total Protein (g/dL)", 0.0, 15.0, 7.0, 0.1, format="%.1f", key="lft_tp")
        
        # Calculate ratios
        if ast > 0:
            ast_alt_ratio = ast / alt
            st.info(f"**AST/ALT ratio:** {ast_alt_ratio:.2f}")
            if ast_alt_ratio > 2:
                st.caption("⬆️ >2: Alcoholic liver disease")
            elif ast_alt_ratio < 1:
                st.caption("⬇️ <1: Viral or drug-induced hepatitis")
            else:
                st.caption("✓ Ratio 1-2")
    
    with col2:
        st.markdown("#### 📊 Giải thích")
        
        results = {
            "ALT": alt,
            "AST": ast,
            "ALP": alp,
            "Bilirubin_Total": bili_t,
            "Bilirubin_Direct": bili_d,
            "Albumin": albumin,
            "Total_Protein": tp
        }
        
        for test_name, value in results.items():
            test_data = ALL_RANGES.get(test_name, {})
            interpretation = interpret_value(test_name, value)
            
            if "CRITICALLY" in interpretation:
                st.error(f"**{test_data.get('vn_name', test_name)}:** {value} - {interpretation}")
            elif "Low" in interpretation or "High" in interpretation:
                st.warning(f"**{test_data.get('vn_name', test_name)}:** {value} - {interpretation}")
            else:
                st.success(f"**{test_data.get('vn_name', test_name)}:** {value} - {interpretation}")
    
    # Patterns
    st.markdown("---")
    with st.expander("📊 Các Mẫu LFT Thường gặp"):
        st.markdown("""
        **Mẫu Tổn Thương Tế Bào Gan (ALT, AST ⬆️⬆️):**
        - Viêm gan virus (A, B, C)
        - Do thuốc (acetaminophen, statin)
        - Viêm gan thiếu máu cục bộ
        - Viêm gan tự miễn
        
        **Mẫu Ứ Mật (ALP, Bilirubin ⬆️⬆️):**
        - Tắc đường mật
        - Xơ đường mật nguyên phát
        - Do thuốc (kháng sinh, steroid)
        - Bệnh thâm nhiễm
        
        **Mẫu Hỗn Hợp (Tất cả tăng cao):**
        - Nhiễm khuẩn huyết
        - Suy tim với ứ đọng gan
        - Xơ gan
        """)
