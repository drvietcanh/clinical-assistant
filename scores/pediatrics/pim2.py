"""
PIM2 - Pediatric Index of Mortality 2
ICU mortality prediction for pediatric patients

Reference:
- Slater A, et al. PIM2: a revised version of the Paediatric Index of Mortality.
  Intensive Care Med. 2003;29(2):278-285.

PIM2 Components (10 variables):
1. Systolic BP
2. Pupils (fixed/dilated)
3. Base excess
4. FIO2
5. PaO2
6. Elective admission
7. Recovery from surgery
8. Bypass cardiac surgery
9. High-risk diagnosis
10. Low-risk diagnosis

Score: 0-100+ points (logistic regression)
Mortality risk: Calculated from score

Clinical Utility:
- ICU mortality prediction
- Risk stratification
- Quality assessment
"""

import streamlit as st
import math
from utils.formatters import format_number


def calculate_pim2(
    systolic_bp: float,
    pupils_fixed: bool,
    base_excess: float,
    fio2: float,
    pao2: float,
    elective_admission: bool,
    recovery_from_surgery: bool,
    bypass_cardiac_surgery: bool,
    high_risk_diagnosis: bool,
    low_risk_diagnosis: bool
) -> dict:
    """
    Calculate PIM2 Score
    
    Args:
        systolic_bp: Systolic blood pressure (mmHg)
        pupils_fixed: Fixed/dilated pupils (True/False)
        base_excess: Base excess (mEq/L)
        fio2: Fraction of inspired oxygen (0.21-1.0)
        pao2: Partial pressure of oxygen (mmHg)
        elective_admission: Elective admission (True/False)
        recovery_from_surgery: Recovery from surgery (True/False)
        bypass_cardiac_surgery: Bypass cardiac surgery (True/False)
        high_risk_diagnosis: High-risk diagnosis (True/False)
        low_risk_diagnosis: Low-risk diagnosis (True/False)
    
    Returns:
        dict with total score, mortality risk, and interpretation
    """
    score = 0
    
    # 1. Systolic BP
    if systolic_bp < 55:
        score += 23.2
    elif systolic_bp < 65:
        score += 16.1
    elif systolic_bp < 75:
        score += 10.3
    elif systolic_bp < 85:
        score += 4.7
    # 85-115: 0 points (normal)
    elif systolic_bp > 135:
        score += 3.1
    
    # 2. Pupils (fixed/dilated)
    if pupils_fixed:
        score += 23.4
    
    # 3. Base excess
    if base_excess < -20:
        score += 21.9
    elif base_excess < -15:
        score += 11.3
    elif base_excess < -10:
        score += 4.3
    elif base_excess < -5:
        score += 0.9
    # -5 to 5: 0 points (normal)
    elif base_excess > 5:
        score += 0.3
    
    # 4. FIO2 (if >0.21, calculate P/F ratio)
    if fio2 > 0.21:
        pf_ratio = pao2 / fio2
        if pf_ratio < 100:
            score += 11.7
        elif pf_ratio < 200:
            score += 6.4
        elif pf_ratio < 300:
            score += 2.2
        # ≥300: 0 points
    
    # 5. Elective admission
    if elective_admission:
        score -= 1.3  # Reduces risk
    
    # 6. Recovery from surgery
    if recovery_from_surgery:
        score -= 1.8  # Reduces risk
    
    # 7. Bypass cardiac surgery
    if bypass_cardiac_surgery:
        score -= 1.8  # Reduces risk
    
    # 8. High-risk diagnosis
    if high_risk_diagnosis:
        score += 6.3
    
    # 9. Low-risk diagnosis
    if low_risk_diagnosis:
        score -= 4.2  # Reduces risk
    
    # Calculate mortality risk
    # PIM2 formula: Logit(P) = -4.8842 + (0.3333 × PIM2 score)
    logit = -4.8842 + (0.3333 * score)
    mortality_risk = 1 / (1 + math.exp(-logit))
    mortality_percent = mortality_risk * 100
    
    # Interpretation
    if mortality_percent < 5:
        risk_category = "Thấp"
        color = "success"
    elif mortality_percent < 15:
        risk_category = "Trung bình"
        color = "warning"
    else:
        risk_category = "Cao"
        color = "error"
    
    return {
        "total_score": score,
        "mortality_percent": mortality_percent,
        "risk_category": risk_category,
        "color": color,
        "systolic_bp": systolic_bp,
        "pupils_fixed": pupils_fixed,
        "base_excess": base_excess,
        "fio2": fio2,
        "pao2": pao2,
        "pf_ratio": pao2 / fio2 if fio2 > 0.21 else None
    }


def render():
    """PIM2 Score Calculator"""
    st.subheader("👶 PIM2 - Pediatric Index of Mortality 2")
    st.caption("ICU Mortality Prediction for Pediatric Patients")
    
    st.info("""
    **PIM2** là công cụ dự đoán tử vong trong ICU cho bệnh nhân nhi.
    Sử dụng 10 biến số để tính điểm và dự đoán nguy cơ tử vong.
    """)
    
    st.markdown("---")
    
    # Input section
    col1, col2 = st.columns(2)
    
    with col1:
        systolic_bp = st.number_input(
            "**Huyết áp tâm thu (mmHg):**",
            min_value=0.0,
            max_value=300.0,
            value=100.0,
            step=1.0,
            key="pim2_sbp",
            help="Huyết áp tâm thu khi nhập ICU"
        )
        
        pupils_fixed = st.checkbox(
            "**Đồng tử cố định/giãn:**",
            value=False,
            key="pim2_pupils",
            help="Đồng tử không phản xạ với ánh sáng"
        )
        
        base_excess = st.number_input(
            "**Base Excess (mEq/L):**",
            min_value=-30.0,
            max_value=20.0,
            value=0.0,
            step=0.1,
            key="pim2_be",
            help="Base excess từ khí máu động mạch"
        )
        
        fio2 = st.number_input(
            "**FIO₂ (Fraction of Inspired Oxygen):**",
            min_value=0.21,
            max_value=1.0,
            value=0.21,
            step=0.01,
            key="pim2_fio2",
            help="Nồng độ oxy trong khí thở vào (0.21 = room air, 1.0 = 100%)"
        )
        
        pao2 = st.number_input(
            "**PaO₂ (mmHg):**",
            min_value=0.0,
            max_value=500.0,
            value=100.0,
            step=1.0,
            key="pim2_pao2",
            help="Áp suất riêng phần oxy trong máu động mạch"
        )
    
    with col2:
        elective_admission = st.checkbox(
            "**Nhập viện theo kế hoạch (Elective):**",
            value=False,
            key="pim2_elective",
            help="Nhập viện theo kế hoạch (không phải cấp cứu)"
        )
        
        recovery_from_surgery = st.checkbox(
            "**Hồi phục sau phẫu thuật:**",
            value=False,
            key="pim2_recovery",
            help="Bệnh nhân đang hồi phục sau phẫu thuật"
        )
        
        bypass_cardiac_surgery = st.checkbox(
            "**Phẫu thuật tim có bypass:**",
            value=False,
            key="pim2_bypass",
            help="Phẫu thuật tim có sử dụng bypass"
        )
        
        high_risk_diagnosis = st.checkbox(
            "**Chẩn đoán nguy cơ cao:**",
            value=False,
            key="pim2_high_risk",
            help="Chẩn đoán có nguy cơ tử vong cao (ví dụ: suy gan, suy thận nặng, ung thư di căn)"
        )
        
        low_risk_diagnosis = st.checkbox(
            "**Chẩn đoán nguy cơ thấp:**",
            value=False,
            key="pim2_low_risk",
            help="Chẩn đoán có nguy cơ tử vong thấp (ví dụ: hen phế quản, nhiễm trùng đường tiết niệu)"
        )
    
    st.markdown("---")
    
    # Calculate
    if st.button("**Tính PIM2 Score**", type="primary", use_container_width=True):
        result = calculate_pim2(
            systolic_bp,
            pupils_fixed,
            base_excess,
            fio2,
            pao2,
            elective_admission,
            recovery_from_surgery,
            bypass_cardiac_surgery,
            high_risk_diagnosis,
            low_risk_diagnosis
        )
        
        # Display result
        st.markdown("### 📊 Kết quả")
        
        # Total score
        st.metric("**PIM2 Score:**", f"{result['total_score']:.2f} điểm")
        
        # Mortality risk with color
        if result["color"] == "success":
            st.success(f"## Nguy cơ Tử vong: {result['mortality_percent']:.1f}%")
        elif result["color"] == "warning":
            st.warning(f"## Nguy cơ Tử vong: {result['mortality_percent']:.1f}%")
        else:
            st.error(f"## Nguy cơ Tử vong: {result['mortality_percent']:.1f}%")
        
        st.markdown(f"**Phân loại:** {result['risk_category']}")
        
        st.markdown("---")
        st.markdown("### 📋 Chi tiết Điểm số")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Huyết áp tâm thu", f"{format_number(systolic_bp)}", "mmHg")
            if result['pf_ratio']:
                st.metric("P/F Ratio", f"{format_number(result['pf_ratio'])}", help="PaO₂/FIO₂ ratio")
        
        with col2:
            st.metric("Base Excess", f"{format_number(base_excess)}", "mEq/L")
            st.metric("FIO₂", f"{format_number(fio2 * 100)}", "%")
        
        with col3:
            st.metric("PaO₂", f"{format_number(pao2)}", "mmHg")
            if pupils_fixed:
                st.error("⚠️ Đồng tử cố định")
            else:
                st.success("✅ Đồng tử bình thường")
        
        with col4:
            if elective_admission:
                st.success("✅ Nhập viện theo kế hoạch")
            if recovery_from_surgery:
                st.success("✅ Hồi phục sau phẫu thuật")
            if bypass_cardiac_surgery:
                st.info("ℹ️ Phẫu thuật tim bypass")
            if high_risk_diagnosis:
                st.error("⚠️ Chẩn đoán nguy cơ cao")
            if low_risk_diagnosis:
                st.success("✅ Chẩn đoán nguy cơ thấp")
        
        st.markdown("---")
        st.markdown("### 📖 Bảng Điểm PIM2")
        
        import pandas as pd
        
        scoring_data = {
            "Biến số": [
                "Huyết áp tâm thu (mmHg)",
                "Đồng tử cố định/giãn",
                "Base Excess (mEq/L)",
                "P/F Ratio (nếu FIO₂ >0.21)",
                "Nhập viện theo kế hoạch",
                "Hồi phục sau phẫu thuật",
                "Phẫu thuật tim bypass",
                "Chẩn đoán nguy cơ cao",
                "Chẩn đoán nguy cơ thấp"
            ],
            "Điểm": [
                "0-23.2 (tùy mức độ)",
                "23.4 (nếu có)",
                "0-21.9 (tùy mức độ)",
                "0-11.7 (tùy P/F ratio)",
                "-1.3 (giảm nguy cơ)",
                "-1.8 (giảm nguy cơ)",
                "-1.8 (giảm nguy cơ)",
                "+6.3",
                "-4.2 (giảm nguy cơ)"
            ]
        }
        
        st.dataframe(pd.DataFrame(scoring_data), use_container_width=True, hide_index=True)
        
        st.markdown("---")
        st.markdown("### 🎯 Phân Loại Nguy cơ")
        
        risk_data = {
            "Nguy cơ tử vong": ["<5%", "5-15%", ">15%"],
            "Phân loại": ["Thấp", "Trung bình", "Cao"],
            "Hành động": [
                "Theo dõi định kỳ",
                "Theo dõi sát, cân nhắc can thiệp",
                "Can thiệp tích cực, tối ưu hóa điều trị"
            ]
        }
        
        st.dataframe(pd.DataFrame(risk_data), use_container_width=True, hide_index=True)
        
        st.markdown("---")
        st.markdown("### 📚 Tài Liệu Tham Khảo")
        
        st.markdown("""
        1. **Slater A, et al.** PIM2: a revised version of the Paediatric Index of Mortality.
           Intensive Care Med. 2003;29(2):278-285.
        
        2. **Pollack MM, et al.** The Pediatric Risk of Mortality (PRISM) III Score System.
           Pediatr Crit Care Med. 2016;17(7):671-680.
        
        3. **Leteurtre S, et al.** PELOD-2: an update of the PEdiatric logistic organ dysfunction score.
           Crit Care Med. 2013;41(7):1761-1773.
        """)
        
        st.caption("⚠️ PIM2 chỉ là công cụ hỗ trợ. Đánh giá lâm sàng toàn diện vẫn là quan trọng nhất.")


















