"""
SAPS II Score (Simplified Acute Physiology Score II)
=====================================================

Simplified ICU mortality prediction score

Reference:
- Le Gall JR, et al. A new Simplified Acute Physiology Score (SAPS II) based on a
  European/North American multicenter study. JAMA. 1993;270(24):2957-2963.

SAPS II Components:
- 12 physiological variables
- Age
- Type of admission

Total: 0-163 points (theoretical maximum, clinical max usually <100)

Clinical Utility:
- ICU mortality prediction
- Simpler than APACHE II
- Widely used in Europe
- Quality improvement and research
"""

import streamlit as st
import math


def get_age_points(age: int) -> int:
    """Age points"""
    if age < 40:
        return 0
    elif age < 60:
        return 7
    elif age < 70:
        return 12
    elif age < 75:
        return 15
    elif age < 80:
        return 16
    else:
        return 18


def get_hr_points(hr: float) -> int:
    """Heart rate points"""
    if hr < 40:
        return 11
    elif hr < 70:
        return 2
    elif hr < 120:
        return 0
    elif hr < 160:
        return 4
    else:
        return 7


def get_sbp_points(sbp: float) -> int:
    """Systolic blood pressure points"""
    if sbp < 70:
        return 13
    elif sbp < 100:
        return 5
    elif sbp < 200:
        return 0
    else:
        return 2


def get_temp_points(temp: float) -> int:
    """Temperature points"""
    if temp < 39:
        return 0
    else:
        return 3


def get_pao2_fio2_points(pao2: float, fio2: float, is_ventilated: bool) -> int:
    """PaO2/FiO2 points (only if ventilated or CPAP)"""
    if not is_ventilated:
        return 0
    
    ratio = (pao2 / fio2) * 100 if fio2 > 0 else 500
    
    if ratio < 100:
        return 11
    elif ratio < 200:
        return 9
    else:
        return 6


def get_urine_points(urine_output: float) -> int:
    """Urine output points (L/day)"""
    if urine_output < 0.5:
        return 11
    elif urine_output < 1.0:
        return 4
    else:
        return 0


def get_bun_points(bun: float) -> int:
    """Blood urea nitrogen points (mg/dL)"""
    if bun < 28:
        return 0
    elif bun < 84:
        return 6
    else:
        return 10


def get_wbc_points(wbc: float) -> int:
    """White blood cell count points (×10³/μL)"""
    if wbc < 1:
        return 12
    elif wbc < 20:
        return 0
    else:
        return 3


def get_k_points(k: float) -> int:
    """Serum potassium points (mEq/L)"""
    if k < 3:
        return 3
    elif k < 5:
        return 0
    else:
        return 3


def get_na_points(na: float) -> int:
    """Serum sodium points (mEq/L)"""
    if na < 125:
        return 5
    elif na < 145:
        return 0
    else:
        return 1


def get_hco3_points(hco3: float) -> int:
    """Serum bicarbonate points (mEq/L)"""
    if hco3 < 15:
        return 6
    elif hco3 < 20:
        return 3
    else:
        return 0


def get_bilirubin_points(bilirubin: float) -> int:
    """Serum bilirubin points (mg/dL)"""
    if bilirubin < 4:
        return 0
    elif bilirubin < 6:
        return 4
    else:
        return 9


def get_gcs_points(gcs: int) -> int:
    """Glasgow Coma Scale points"""
    if gcs < 6:
        return 26
    elif gcs < 9:
        return 13
    elif gcs < 11:
        return 7
    elif gcs < 14:
        return 5
    else:
        return 0


def get_admission_points(admission_type: str, has_aids: bool, has_hematologic_malignancy: bool, has_metastatic_cancer: bool) -> int:
    """Admission type and chronic disease points"""
    points = 0
    
    if admission_type == "Scheduled surgical":
        points = 0
    elif admission_type == "Medical":
        points = 6
    elif admission_type == "Unscheduled surgical":
        points = 8
    
    # Chronic diseases
    if has_aids:
        points += 17
    if has_hematologic_malignancy:
        points += 10
    if has_metastatic_cancer:
        points += 9
    
    return points


def calculate_saps2(params: dict) -> dict:
    """Calculate SAPS II score"""
    
    score = 0
    details = []
    
    # Age
    age_pts = get_age_points(params['age'])
    score += age_pts
    details.append(f"Tuổi {params['age']} → {age_pts} điểm")
    
    # Heart rate
    hr_pts = get_hr_points(params['heart_rate'])
    score += hr_pts
    details.append(f"Nhịp tim {params['heart_rate']:.0f} /min → {hr_pts} điểm")
    
    # Systolic BP
    sbp_pts = get_sbp_points(params['sbp'])
    score += sbp_pts
    details.append(f"SBP {params['sbp']:.0f} mmHg → {sbp_pts} điểm")
    
    # Temperature
    temp_pts = get_temp_points(params['temperature'])
    score += temp_pts
    details.append(f"Nhiệt độ {params['temperature']:.1f}°C → {temp_pts} điểm")
    
    # PaO2/FiO2 (if ventilated)
    pf_pts = get_pao2_fio2_points(params['pao2'], params['fio2'], params['is_ventilated'])
    score += pf_pts
    if params['is_ventilated']:
        ratio = (params['pao2'] / params['fio2']) * 100 if params['fio2'] > 0 else 500
        details.append(f"PaO₂/FiO₂ = {ratio:.0f} (thở máy) → {pf_pts} điểm")
    else:
        details.append(f"Không thở máy → 0 điểm")
    
    # Urine output
    urine_pts = get_urine_points(params['urine_output'])
    score += urine_pts
    details.append(f"Nước tiểu {params['urine_output']:.1f} L/24h → {urine_pts} điểm")
    
    # BUN
    bun_pts = get_bun_points(params['bun'])
    score += bun_pts
    details.append(f"BUN {params['bun']:.0f} mg/dL → {bun_pts} điểm")
    
    # WBC
    wbc_pts = get_wbc_points(params['wbc'])
    score += wbc_pts
    details.append(f"WBC {params['wbc']:.1f} ×10³/μL → {wbc_pts} điểm")
    
    # Potassium
    k_pts = get_k_points(params['potassium'])
    score += k_pts
    details.append(f"K {params['potassium']:.1f} mEq/L → {k_pts} điểm")
    
    # Sodium
    na_pts = get_na_points(params['sodium'])
    score += na_pts
    details.append(f"Na {params['sodium']:.0f} mEq/L → {na_pts} điểm")
    
    # Bicarbonate
    hco3_pts = get_hco3_points(params['bicarbonate'])
    score += hco3_pts
    details.append(f"HCO₃ {params['bicarbonate']:.0f} mEq/L → {hco3_pts} điểm")
    
    # Bilirubin
    bili_pts = get_bilirubin_points(params['bilirubin'])
    score += bili_pts
    details.append(f"Bilirubin {params['bilirubin']:.1f} mg/dL → {bili_pts} điểm")
    
    # GCS
    gcs_pts = get_gcs_points(params['gcs'])
    score += gcs_pts
    details.append(f"GCS {params['gcs']} → {gcs_pts} điểm")
    
    # Admission type and chronic diseases
    adm_pts = get_admission_points(
        params['admission_type'],
        params['has_aids'],
        params['has_hematologic_malignancy'],
        params['has_metastatic_cancer']
    )
    score += adm_pts
    adm_str = params['admission_type']
    if params['has_aids']:
        adm_str += " + AIDS"
    if params['has_hematologic_malignancy']:
        adm_str += " + Hematologic malignancy"
    if params['has_metastatic_cancer']:
        adm_str += " + Metastatic cancer"
    details.append(f"Loại nhập viện: {adm_str} → {adm_pts} điểm")
    
    # Predicted mortality (logistic regression from original study)
    # Logit(Death) = -7.7631 + 0.0737 × SAPS II + 0.9971 × ln(SAPS II + 1)
    logit = -7.7631 + (0.0737 * score) + (0.9971 * math.log(score + 1))
    predicted_mortality = 100 / (1 + math.exp(-logit))
    
    # Interpretation
    if score < 30:
        interpretation = "Mức độ nặng THẤP"
        mortality_range = "<10%"
        color = "🟢"
    elif score < 40:
        interpretation = "Mức độ nặng TRUNG BÌNH"
        mortality_range = "10-25%"
        color = "🟡"
    elif score < 50:
        interpretation = "Mức độ nặng CAO"
        mortality_range = "25-40%"
        color = "🟠"
    elif score < 60:
        interpretation = "Mức độ nặng RẤT CAO"
        mortality_range = "40-60%"
        color = "🟠"
    else:
        interpretation = "Mức độ nặng CỰC KỲ CAO"
        mortality_range = ">60%"
        color = "🔴"
    
    return {
        'total_score': score,
        'predicted_mortality': predicted_mortality,
        'mortality_range': mortality_range,
        'interpretation': interpretation,
        'color': color,
        'details': details
    }


def render():
    """Render SAPS II calculator"""
    
    st.title("🏥 SAPS II Score")
    st.markdown("**Simplified Acute Physiology Score II - Dự đoán tử vong ICU đơn giản hóa**")
    
    # Educational information
    with st.expander("ℹ️ Thông Tin & Cách Sử Dụng"):
        st.markdown("""
        ### 📋 Giới Thiệu
        
        **SAPS II** là thang điểm ICU:
        - Đơn giản hơn APACHE II
        - Dự đoán tử vong bệnh viện
        - Phổ biến ở châu Âu
        - 17 biến số (vs 12 physiological + age + admission)
        
        ### 🎯 Thành Phần
        
        - 12 biến số sinh lý
        - Tuổi
        - Loại nhập viện (medical/surgical)
        - Bệnh mạn tính (AIDS, ung thư, hematologic malignancy)
        
        **Tổng điểm:** 0-163 (thực tế thường <100)
        
        ### 📊 Điểm & Tử Vong
        
        | SAPS II | Tử Vong |
        |---------|---------|
        | <30 | <10% |
        | 30-39 | 10-25% |
        | 40-49 | 25-40% |
        | 50-59 | 40-60% |
        | ≥60 | >60% |
        
        ### ⚠️ Lưu Ý
        
        - Tính trong 24h ĐẦU nhập ICU
        - Lấy giá trị TỆ NHẤT
        - Đơn giản hơn APACHE II (ít biến số hơn)
        
        ### 📚 Tham Khảo
        
        - Le Gall JR, et al. *JAMA* 1993;270:2957-2963
        """)
    
    st.divider()
    
    st.subheader("📝 Nhập Dữ Liệu (Giá trị TỆ NHẤT trong 24h đầu ICU)")
    
    # Demographics
    st.markdown("#### 👤 Thông Tin Chung")
    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("Tuổi", 0, 120, 50, 1)
    with col2:
        gcs = st.number_input("GCS (Glasgow Coma Scale)", 3, 15, 15, 1)
    
    st.divider()
    
    # Vital signs
    st.markdown("#### 🩺 Sinh Hiệu")
    col3, col4, col5 = st.columns(3)
    with col3:
        heart_rate = st.number_input("Nhịp tim (/min)", 0.0, 250.0, 80.0, 1.0)
    with col4:
        sbp = st.number_input("SBP (mmHg)", 0.0, 300.0, 120.0, 1.0)
    with col5:
        temperature = st.number_input("Nhiệt độ (°C)", 20.0, 45.0, 37.0, 0.1)
    
    st.divider()
    
    # Oxygenation (if ventilated)
    st.markdown("#### 🫁 Oxy Hóa")
    is_ventilated = st.checkbox("**Bệnh nhân đang thở máy hoặc CPAP**")
    
    if is_ventilated:
        col6, col7 = st.columns(2)
        with col6:
            pao2 = st.number_input("PaO₂ (mmHg)", 0.0, 700.0, 100.0, 1.0)
        with col7:
            fio2 = st.number_input("FiO₂ (%)", 21.0, 100.0, 21.0, 1.0)
    else:
        pao2 = 100.0
        fio2 = 21.0
    
    st.divider()
    
    # Labs
    st.markdown("#### 🔬 Xét Nghiệm")
    col8, col9 = st.columns(2)
    
    with col8:
        urine_output = st.number_input("Nước tiểu (L/24h)", 0.0, 10.0, 1.5, 0.1)
        bun = st.number_input("BUN (mg/dL)", 0.0, 200.0, 20.0, 1.0)
        st.caption("💡 mmol/L × 2.8 = mg/dL")
        wbc = st.number_input("WBC (×10³/μL)", 0.0, 100.0, 10.0, 0.1)
        potassium = st.number_input("Potassium (mEq/L)", 1.5, 10.0, 4.0, 0.1)
    
    with col9:
        sodium = st.number_input("Sodium (mEq/L)", 80.0, 200.0, 140.0, 1.0)
        bicarbonate = st.number_input("Bicarbonate/HCO₃ (mEq/L)", 0.0, 50.0, 24.0, 1.0)
        bilirubin = st.number_input("Bilirubin (mg/dL)", 0.0, 30.0, 1.0, 0.1)
        st.caption("💡 μmol/L ÷ 17.1 = mg/dL")
    
    st.divider()
    
    # Admission type
    st.markdown("#### 🏥 Loại Nhập Viện & Bệnh Mạn Tính")
    admission_type = st.radio(
        "Loại nhập viện ICU",
        ["Scheduled surgical", "Medical", "Unscheduled surgical"],
        help="Scheduled surgical = Phẫu thuật theo kế hoạch"
    )
    
    col10, col11, col12 = st.columns(3)
    with col10:
        has_aids = st.checkbox("AIDS")
    with col11:
        has_hematologic_malignancy = st.checkbox("Ung thư huyết học")
    with col12:
        has_metastatic_cancer = st.checkbox("Ung thư di căn")
    
    st.divider()
    
    # Calculate
    if st.button("🧮 Tính SAPS II Score", type="primary", use_container_width=True):
        params = {
            'age': age,
            'heart_rate': heart_rate,
            'sbp': sbp,
            'temperature': temperature,
            'is_ventilated': is_ventilated,
            'pao2': pao2,
            'fio2': fio2,
            'urine_output': urine_output,
            'bun': bun,
            'wbc': wbc,
            'potassium': potassium,
            'sodium': sodium,
            'bicarbonate': bicarbonate,
            'bilirubin': bilirubin,
            'gcs': gcs,
            'admission_type': admission_type,
            'has_aids': has_aids,
            'has_hematologic_malignancy': has_hematologic_malignancy,
            'has_metastatic_cancer': has_metastatic_cancer
        }
        
        result = calculate_saps2(params)
        
        # Display results
        st.subheader("📊 Kết Quả")
        
        col_r1, col_r2, col_r3 = st.columns(3)
        
        with col_r1:
            st.metric("**SAPS II**", f"{result['total_score']}")
            st.caption("0-163 (cao = nặng)")
        
        with col_r2:
            st.metric("**Tử Vong Dự Đoán**", f"{result['predicted_mortality']:.1f}%")
            st.caption(f"Khoảng: {result['mortality_range']}")
        
        with col_r3:
            st.markdown(f"### {result['color']}")
            st.markdown(f"**{result['interpretation']}**")
        
        # Details
        with st.expander("📋 Chi Tiết Điểm Số", expanded=True):
            for detail in result['details']:
                st.markdown(f"- {detail}")
        
        # Interpretation
        st.info("""
        **📌 Diễn Giải:**
        
        - SAPS II đơn giản hơn APACHE II
        - Ít biến số hơn, dễ tính
        - Phổ biến ở châu Âu
        - Dự đoán tử vong bệnh viện (không phải ICU)
        """)
        
        if result['total_score'] >= 50:
            st.error("""
            **🚨 SAPS II SCORE RẤT CAO:**
            
            - Nguy cơ tử vong >40%
            - Cần hồi sức tích cực
            - Xem xét tiên lượng và mục tiêu điều trị
            """)
        
        st.warning("""
        ⚠️ **Lưu Ý:**
        - Chỉ là ước tính, không chính xác 100%
        - Nhiều yếu tố khác ảnh hưởng tiên lượng
        - Quyết định dựa trên đánh giá lâm sàng toàn diện
        """)
        
        st.session_state['saps2_result'] = result
