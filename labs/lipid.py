"""
Lipid Panel với các công thức tính chuyên sâu
Bao gồm: Friedewald, Sampson equation (cho TG cao), các tỉ lệ lipid
"""

import streamlit as st
import math
from .normal_ranges import get_normal_range, is_critical, interpret_value, ALL_RANGES


def _format_num(value: float, decimals: int = 1) -> str:
    """Format số, loại bỏ số 0 thừa"""
    rounded = round(value, decimals)
    if rounded == int(rounded):
        return str(int(rounded))
    return f"{rounded:.{decimals}f}".rstrip('0').rstrip('.')


def calculate_ldl_friedewald(chol: float, hdl: float, tg: float) -> float:
    """
    Tính LDL bằng công thức Friedewald
    LDL = Total Chol - HDL - (TG / 5) [mg/dL]
    LDL = Total Chol - HDL - (TG / 2.2) [mmol/L]
    Chỉ chính xác khi TG < 400 mg/dL (< 4.5 mmol/L)
    """
    if tg >= 400:
        return None  # Không chính xác khi TG >= 400
    ldl = chol - hdl - (tg / 5.0)
    return max(0, ldl)  # LDL không thể âm


def calculate_ldl_sampson(chol: float, hdl: float, tg: float) -> float:
    """
    Tính LDL bằng công thức Sampson (2020)
    Chính xác hơn khi TG >= 400 mg/dL
    LDL = Total Chol - HDL - TG/5 - (non-HDL - TG/5) * (TG/150) * 0.45
    """
    non_hdl = chol - hdl
    vldl_estimate = tg / 5.0
    if non_hdl <= vldl_estimate:
        return 0
    ldl = chol - hdl - vldl_estimate - (non_hdl - vldl_estimate) * (tg / 150.0) * 0.45
    return max(0, ldl)


def calculate_ldl_martin_hopkins(chol: float, hdl: float, tg: float) -> float:
    """
    Tính LDL bằng công thức Martin/Hopkins (2013)
    Sử dụng bảng hệ số động thay vì hệ số cố định 5
    Đơn giản hóa: sử dụng hệ số 5 cho TG < 150, tăng dần đến 9 cho TG > 400
    """
    if tg < 150:
        factor = 5.0
    elif tg < 300:
        factor = 5.0 + (tg - 150) / 150 * 1.5  # 5.0 đến 6.5
    elif tg < 400:
        factor = 6.5 + (tg - 300) / 100 * 1.5  # 6.5 đến 8.0
    else:
        factor = 8.0 + (tg - 400) / 100 * 1.0  # 8.0 đến 9.0 (cho TG rất cao)
    
    ldl = chol - hdl - (tg / factor)
    return max(0, ldl)


def render():
    """Lipid Panel với các công thức tính chuyên sâu"""
    st.subheader("💊 Lipid Panel - Công Thức Tính Chuyên Sâu")
    st.caption("Mỡ Máu - Chuyển đổi đơn vị mmol/L ↔ mg/dL | Tính LDL khi TG cao")
    
    # Unit selection
    st.markdown("#### 🔄 Chọn Đơn Vị")
    unit_system = st.radio(
        "Hệ đơn vị:",
        ["mmol/L (SI Units - Mặc định)", "mg/dL (Conventional)"],
        horizontal=True,
        key="lipid_unit_system"
    )
    
    use_si = "mmol/L" in unit_system
    
    # Option: nhập LDL trực tiếp hoặc tính từ công thức
    st.markdown("#### 📋 Chế Độ Nhập")
    input_mode = st.radio(
        "Chế độ:",
        ["Tự động tính LDL từ công thức", "Nhập LDL trực tiếp"],
        horizontal=True,
        key="lipid_input_mode"
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 📝 Nhập Giá trị")
        
        # Total Cholesterol
        st.markdown("**Total Cholesterol**")
        if use_si:
            chol_input = st.number_input(
                "Total Cholesterol (mmol/L)",
                0.0, 15.0, 4.7, 0.1,
                format="%.1f",
                help="Bình thường: <5.2 mmol/L",
                key="chol_mmol"
            )
            chol = chol_input * 38.67  # Convert to mg/dL for calculations
            st.caption(f"≈ {round(chol)} mg/dL")
        else:
            chol = st.number_input(
                "Total Cholesterol (mg/dL)",
                0.0, 500.0, 180.0, 1.0,
                format="%.0f",
                help="Bình thường: <200 mg/dL",
                key="chol_mgdl"
            )
            st.caption(f"≈ {_format_num(chol/38.67, 1)} mmol/L")
        
        # HDL
        st.markdown("**HDL Cholesterol**")
        if use_si:
            hdl_input = st.number_input(
                "HDL Cholesterol (mmol/L)",
                0.0, 5.0, 1.3, 0.1,
                format="%.1f",
                help="Nam >1.0, Nữ >1.3 mmol/L",
                key="hdl_mmol"
            )
            hdl = hdl_input * 38.67
            st.caption(f"≈ {round(hdl)} mg/dL")
        else:
            hdl = st.number_input(
                "HDL Cholesterol (mg/dL)",
                0.0, 150.0, 50.0, 1.0,
                format="%.0f",
                help="Nam >40, Nữ >50 mg/dL",
                key="hdl_mgdl"
            )
            st.caption(f"≈ {_format_num(hdl/38.67, 1)} mmol/L")
        
        # Triglycerides
        st.markdown("**Triglycerides**")
        if use_si:
            tg_input = st.number_input(
                "Triglycerides (mmol/L)",
                0.0, 20.0, 1.4, 0.1,
                format="%.1f",
                help="Bình thường: <1.7 mmol/L",
                key="tg_mmol"
            )
            tg = tg_input * 88.57  # Convert to mg/dL for calculations
            st.caption(f"≈ {round(tg)} mg/dL")
        else:
            tg = st.number_input(
                "Triglycerides (mg/dL)",
                0.0, 2000.0, 120.0, 1.0,
                format="%.0f",
                help="Bình thường: <150 mg/dL",
                key="tg_mgdl"
            )
            st.caption(f"≈ {_format_num(tg/88.57, 1)} mmol/L")
        
        # LDL - tự động tính hoặc nhập trực tiếp
        st.markdown("**LDL Cholesterol**")
        if input_mode == "Tự động tính LDL từ công thức":
            # Tính LDL tự động
            if tg < 400:
                ldl_calculated = calculate_ldl_friedewald(chol, hdl, tg)
                if ldl_calculated is not None:
                    ldl = ldl_calculated
                    if use_si:
                        st.info(f"**LDL (Friedewald):** {_format_num(ldl/38.67, 2)} mmol/L ({round(ldl)} mg/dL)")
                    else:
                        st.info(f"**LDL (Friedewald):** {round(ldl)} mg/dL ({_format_num(ldl/38.67, 2)} mmol/L)")
                    st.caption("✓ Công thức Friedewald (chính xác khi TG < 400 mg/dL)")
                else:
                    ldl = 0
                    st.warning("⚠️ TG ≥ 400 mg/dL: Công thức Friedewald không chính xác")
            else:
                # TG >= 400, sử dụng Sampson hoặc Martin/Hopkins
                ldl_sampson = calculate_ldl_sampson(chol, hdl, tg)
                ldl_martin = calculate_ldl_martin_hopkins(chol, hdl, tg)
                ldl = ldl_sampson  # Mặc định dùng Sampson
                
                if use_si:
                    st.warning(f"**LDL (Sampson 2020):** {_format_num(ldl/38.67, 2)} mmol/L ({round(ldl)} mg/dL)")
                    st.caption(f"LDL (Martin/Hopkins 2013): {_format_num(ldl_martin/38.67, 2)} mmol/L ({round(ldl_martin)} mg/dL)")
                else:
                    st.warning(f"**LDL (Sampson 2020):** {round(ldl)} mg/dL ({_format_num(ldl/38.67, 2)} mmol/L)")
                    st.caption(f"LDL (Martin/Hopkins 2013): {round(ldl_martin)} mg/dL ({_format_num(ldl_martin/38.67, 2)} mmol/L)")
                st.caption("⚠️ TG ≥ 400 mg/dL: Sử dụng công thức Sampson (2020) hoặc Martin/Hopkins (2013)")
        else:
            # Nhập LDL trực tiếp
            if use_si:
                ldl_input = st.number_input(
                    "LDL Cholesterol (mmol/L)",
                    0.0, 10.0, 2.6, 0.1,
                    format="%.1f",
                    help="Mục tiêu: <2.6 mmol/L",
                    key="ldl_mmol"
                )
                ldl = ldl_input * 38.67
                st.caption(f"≈ {round(ldl)} mg/dL")
            else:
                ldl = st.number_input(
                    "LDL Cholesterol (mg/dL)",
                    0.0, 300.0, 100.0, 1.0,
                    format="%.0f",
                    help="Mục tiêu: <100 mg/dL",
                    key="ldl_mgdl"
                )
                st.caption(f"≈ {_format_num(ldl/38.67, 1)} mmol/L")
    
    with col2:
        st.markdown("#### 📊 Interpretation")
        
        # Total Cholesterol
        if chol < 200:
            st.success(f"**Total Cholesterol:** {round(chol)} - Desirable ✓")
        elif chol < 240:
            st.warning(f"**Total Cholesterol:** {round(chol)} - Borderline high ⚠️")
        else:
            st.error(f"**Total Cholesterol:** {round(chol)} - High ⬆️")
        
        # LDL
        if ldl < 100:
            st.success(f"**LDL:** {round(ldl)} - Optimal ✓")
        elif ldl < 130:
            st.info(f"**LDL:** {round(ldl)} - Near optimal")
        elif ldl < 160:
            st.warning(f"**LDL:** {round(ldl)} - Borderline high ⚠️")
        elif ldl < 190:
            st.error(f"**LDL:** {round(ldl)} - High ⬆️")
        else:
            st.error(f"**LDL:** {round(ldl)} - Very high ⬆️⬆️")
        
        # HDL
        if hdl < 40:
            st.error(f"**HDL:** {round(hdl)} - Low (⬇️ risk factor)")
        elif hdl < 60:
            st.success(f"**HDL:** {round(hdl)} - Normal ✓")
        else:
            st.success(f"**HDL:** {round(hdl)} - High (✓ protective)")
        
        # Triglycerides
        if tg < 150:
            st.success(f"**Triglycerides:** {round(tg)} - Normal ✓")
        elif tg < 200:
            st.warning(f"**Triglycerides:** {round(tg)} - Borderline high ⚠️")
        elif tg < 500:
            st.error(f"**Triglycerides:** {round(tg)} - High ⬆️")
        else:
            st.error(f"**Triglycerides:** {round(tg)} - Very high ⬆️⬆️")
    
    st.markdown("---")
    
    # Tính các chỉ số lipid chuyên sâu
    st.markdown("#### 🔬 Các Chỉ Số Lipid Chuyên Sâu")
    
    if hdl > 0 and chol > 0:
        # Non-HDL Cholesterol
        non_hdl = chol - hdl
        st.markdown("**1. Non-HDL Cholesterol** (Total Chol - HDL)")
        if use_si:
            st.info(f"**Non-HDL:** {_format_num(non_hdl/38.67, 2)} mmol/L ({round(non_hdl)} mg/dL)")
        else:
            st.info(f"**Non-HDL:** {round(non_hdl)} mg/dL ({_format_num(non_hdl/38.67, 2)} mmol/L)")
        
        # Interpretation Non-HDL
        if non_hdl < 130:
            st.caption("✓ Optimal (<130 mg/dL)")
        elif non_hdl < 160:
            st.caption("⚠️ Near optimal (130-159 mg/dL)")
        elif non_hdl < 190:
            st.caption("⬆️ Borderline high (160-189 mg/dL)")
        elif non_hdl < 220:
            st.caption("⬆️⬆️ High (190-219 mg/dL)")
        else:
            st.caption("⬆️⬆️⬆️ Very high (≥220 mg/dL)")
        
        # Remnant Cholesterol
        remnant = chol - ldl - hdl
        st.markdown("**2. Remnant Cholesterol** (Total Chol - LDL - HDL)")
        if use_si:
            st.info(f"**Remnant Chol:** {_format_num(remnant/38.67, 2)} mmol/L ({round(remnant)} mg/dL)")
        else:
            st.info(f"**Remnant Chol:** {round(remnant)} mg/dL ({_format_num(remnant/38.67, 2)} mmol/L)")
        st.caption("Remnant cholesterol = VLDL + IDL (nguy cơ tim mạch độc lập)")
        
        # Các tỉ lệ
        st.markdown("**3. Các Tỉ Lệ Lipid**")
        
        # Total Chol/HDL
        chol_hdl_ratio = chol / hdl
        st.markdown(f"**• Total Chol/HDL:** {chol_hdl_ratio:.2f}")
        if chol_hdl_ratio < 3.5:
            st.caption("✓ Low risk (<3.5)")
        elif chol_hdl_ratio < 5.0:
            st.caption("⚠️ Average risk (3.5-5.0)")
        else:
            st.caption("⬆️ High risk (>5.0)")
        
        # LDL/HDL
        if ldl > 0:
            ldl_hdl_ratio = ldl / hdl
            st.markdown(f"**• LDL/HDL:** {ldl_hdl_ratio:.2f}")
            if ldl_hdl_ratio < 2.0:
                st.caption("✓ Low risk (<2.0)")
            elif ldl_hdl_ratio < 3.0:
                st.caption("⚠️ Average risk (2.0-3.0)")
            else:
                st.caption("⬆️ High risk (>3.0)")
        
        # TG/HDL
        if hdl > 0:
            tg_hdl_ratio = tg / hdl
            st.markdown(f"**• TG/HDL:** {tg_hdl_ratio:.2f}")
            if use_si:
                # mmol/L: <0.87 lý tưởng, >2.62 quá cao
                if tg_hdl_ratio < 0.87:
                    st.caption("✓ Lý tưởng (<0.87)")
                elif tg_hdl_ratio < 1.74:
                    st.caption("⚠️ Bình thường (0.87-1.74)")
                elif tg_hdl_ratio < 2.62:
                    st.caption("⬆️ Cao (1.74-2.62)")
                else:
                    st.caption("⬆️⬆️ Quá cao (>2.62)")
            else:
                # mg/dL: <2.0 lý tưởng, >6.0 quá cao
                if tg_hdl_ratio < 2.0:
                    st.caption("✓ Lý tưởng (<2.0)")
                elif tg_hdl_ratio < 4.0:
                    st.caption("⚠️ Bình thường (2.0-4.0)")
                elif tg_hdl_ratio < 6.0:
                    st.caption("⬆️ Cao (4.0-6.0)")
                else:
                    st.caption("⬆️⬆️ Quá cao (>6.0)")
        
        # Non-HDL/HDL
        non_hdl_hdl_ratio = non_hdl / hdl
        st.markdown(f"**• Non-HDL/HDL:** {non_hdl_hdl_ratio:.2f}")
        if non_hdl_hdl_ratio < 3.0:
            st.caption("✓ Low risk (<3.0)")
        elif non_hdl_hdl_ratio < 3.6:
            st.caption("⚠️ Average risk (3.0-3.6)")
        else:
            st.caption("⬆️ High risk (>3.6)")
        
        # Atherogenic Index of Plasma (AIP)
        if tg > 0 and hdl > 0:
            aip = math.log10(tg / hdl)
            st.markdown("**4. Atherogenic Index of Plasma (AIP)** = log₁₀(TG/HDL)")
            st.info(f"**AIP:** {aip:.3f}")
            if aip < -0.3:
                st.caption("✓ Low risk (<-0.3)")
            elif aip < 0.1:
                st.caption("⚠️ Average risk (-0.3 to 0.1)")
            else:
                st.caption("⬆️ High risk (>0.1)")
            st.caption("AIP > 0.1: Tăng nguy cơ xơ vữa động mạch và kháng insulin")
        
        # Castelli Risk Index
        st.markdown("**5. Castelli Risk Index**")
        st.info(f"**Castelli I (Total Chol/HDL):** {chol_hdl_ratio:.2f}")
        if ldl > 0:
            st.info(f"**Castelli II (LDL/HDL):** {ldl_hdl_ratio:.2f}")
        
        # Atherogenic Coefficient
        atherogenic_coeff = (chol - hdl) / hdl
        st.markdown("**6. Atherogenic Coefficient** = (Total Chol - HDL)/HDL")
        st.info(f"**Atherogenic Coefficient:** {atherogenic_coeff:.2f}")
        if atherogenic_coeff < 3.0:
            st.caption("✓ Low risk (<3.0)")
        elif atherogenic_coeff < 4.0:
            st.caption("⚠️ Average risk (3.0-4.0)")
        else:
            st.caption("⬆️ High risk (>4.0)")
    
    st.markdown("---")
    
    # Thông tin về công thức
    with st.expander("ℹ️ Thông Tin Về Các Công Thức Tính LDL"):
        st.markdown("""
        **1. Công thức Friedewald (1972)**
        - LDL = Total Chol - HDL - (TG / 5) [mg/dL]
        - LDL = Total Chol - HDL - (TG / 2.2) [mmol/L]
        - **Chỉ chính xác khi TG < 400 mg/dL (< 4.5 mmol/L)**
        - Không chính xác khi: TG ≥ 400, nhịn ăn < 12h, chylomicronemia
        
        **2. Công thức Sampson (2020) - Khuyến nghị cho TG cao**
        - Chính xác hơn khi TG ≥ 400 mg/dL
        - LDL = Total Chol - HDL - TG/5 - (non-HDL - TG/5) × (TG/150) × 0.45
        - Được khuyến nghị bởi AHA/ACC 2022
        
        **3. Công thức Martin/Hopkins (2013)**
        - Sử dụng hệ số động thay vì hệ số cố định 5
        - Hệ số tăng từ 5 (TG < 150) đến 9 (TG > 400)
        - Chính xác hơn Friedewald khi TG cao
        
        **Lưu ý:** Khi TG ≥ 400 mg/dL, nên đo LDL trực tiếp hoặc sử dụng công thức Sampson/Martin-Hopkins.
        """)
    
    st.info("""
    **LDL Goals by Risk (mg/dL):**
    - Very high risk (CAD, DM): <70 mg/dL (<1.8 mmol/L)
    - High risk (2+ risk factors): <100 mg/dL (<2.6 mmol/L)
    - Moderate risk: <130 mg/dL (<3.4 mmol/L)
    - Low risk: <160 mg/dL (<4.1 mmol/L)
    
    **Non-HDL Goals by Risk (mg/dL):**
    - Very high risk: <100 mg/dL
    - High risk: <130 mg/dL
    - Moderate risk: <160 mg/dL
    - Low risk: <190 mg/dL
    """)
