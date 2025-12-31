"""
APACHE III Score (Acute Physiology and Chronic Health Evaluation III)
=====================================================================

ICU mortality prediction scoring system - Updated version

Reference:
- Knaus WA, et al. The APACHE III prognostic system. Risk prediction of hospital
  mortality for critically ill hospitalized adults. Chest. 1991;100(6):1619-1636.

APACHE III Components:
1. Acute Physiology Score (APS): 17 physiological variables (0-252 points)
2. Age points (0-24 points)
3. Chronic Health points (0-23 points)

Total: 0-299 points (theoretical maximum)

Key Differences from APACHE II:
- More variables (17 vs 12)
- More precise scoring ranges
- Disease-specific coefficients
- More accurate mortality prediction
- Proprietary formula (requires license for exact calculation)

Clinical Utility:
- Predict ICU mortality (more accurate than APACHE II)
- Stratify disease severity
- Research and quality improvement
- ICU resource allocation

Note: This is a simplified implementation based on published information.
Exact APACHE III calculation requires licensed software from Cerner Corporation.
"""

import streamlit as st
import math
from components.ui.scoring import (
    render_score_result,
    render_score_breakdown,
)
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
from components.export import render_export_section
# ======================================

# ========== NEW COMPONENTS (Phase 1 & 2) ==========
from components.risk_color_coding import render_risk_badge, get_risk_level
from components.score_charts import render_risk_gauge_chart, render_risk_bar_chart
from components.scores_export import render_export_section as render_scores_export
# ===================================================
from scores.utils.validation import (
    validate_age,
    validate_gcs,
    validate_blood_pressure,
    validate_heart_rate,
    validate_respiratory_rate,
    validate_temperature,
    validate_lab_value,
    safe_divide
)


def get_apache3_temp_points(temp: float) -> float:
    """Temperature points for APACHE III"""
    if temp >= 41.0:
        return 8
    elif temp >= 39.0:
        return 5
    elif temp >= 38.5:
        return 2
    elif temp >= 36.0:
        return 0
    elif temp >= 34.0:
        return 2
    elif temp >= 32.0:
        return 3
    elif temp >= 30.0:
        return 4
    else:
        return 8


def get_apache3_map_points(map_val: float) -> float:
    """MAP points for APACHE III"""
    if map_val >= 160:
        return 13
    elif map_val >= 130:
        return 7
    elif map_val >= 110:
        return 6
    elif map_val >= 70:
        return 0
    elif map_val >= 50:
        return 4
    else:
        return 13


def get_apache3_hr_points(hr: float) -> float:
    """Heart rate points for APACHE III"""
    if hr >= 180:
        return 17
    elif hr >= 140:
        return 8
    elif hr >= 110:
        return 5
    elif hr >= 70:
        return 0
    elif hr >= 55:
        return 1
    elif hr >= 40:
        return 5
    else:
        return 17


def get_apache3_rr_points(rr: float) -> float:
    """Respiratory rate points for APACHE III"""
    if rr >= 50:
        return 18
    elif rr >= 35:
        return 5
    elif rr >= 25:
        return 1
    elif rr >= 12:
        return 0
    elif rr >= 10:
        return 1
    elif rr >= 6:
        return 5
    else:
        return 18


def get_apache3_oxygenation_points(pao2: float, fio2: float, is_ventilated: bool) -> float:
    """Oxygenation points for APACHE III"""
    if not is_ventilated:
        return 0
    
    if fio2 == 0:
        return 0
    
    # Calculate A-a gradient or use PaO2/FiO2
    if fio2 >= 0.5:
        # Use A-a gradient
        # Simplified: A-a gradient approximation
        aa_gradient = (fio2 * 713) - pao2 - (40 * 0.8)  # Simplified calculation
        if aa_gradient >= 500:
            return 15
        elif aa_gradient >= 350:
            return 5
        elif aa_gradient >= 200:
            return 2
        else:
            return 0
    else:
        # Use PaO2
        if pao2 >= 70:
            return 0
        elif pao2 >= 61:
            return 1
        elif pao2 >= 55:
            return 3
        else:
            return 5


def get_apache3_ph_points(ph: float) -> float:
    """pH points for APACHE III"""
    if ph >= 7.70:
        return 12
    elif ph >= 7.60:
        return 3
    elif ph >= 7.50:
        return 0
    elif ph >= 7.33:
        return 0
    elif ph >= 7.25:
        return 3
    elif ph >= 7.15:
        return 12
    else:
        return 12


def get_apache3_na_points(na: float) -> float:
    """Sodium points for APACHE III"""
    if na >= 180:
        return 4
    elif na >= 160:
        return 3
    elif na >= 155:
        return 2
    elif na >= 150:
        return 1
    elif na >= 130:
        return 0
    elif na >= 120:
        return 2
    elif na >= 110:
        return 3
    else:
        return 4


def get_apache3_k_points(k: float) -> float:
    """Potassium points for APACHE III"""
    if k >= 7.0:
        return 3
    elif k >= 6.0:
        return 2
    elif k >= 5.5:
        return 1
    elif k >= 3.5:
        return 0
    elif k >= 3.0:
        return 1
    elif k >= 2.5:
        return 2
    else:
        return 3


def get_apache3_creatinine_points(cr: float, has_arf: bool) -> float:
    """Creatinine points for APACHE III"""
    if has_arf:
        # ARF: multiply by 2
        if cr >= 1.5:
            return 10
        elif cr >= 0.6:
            return 6
        else:
            return 2
    else:
        if cr >= 1.5:
            return 4
        elif cr >= 0.6:
            return 0
        else:
            return 0


def get_apache3_hct_points(hct: float) -> float:
    """Hematocrit points for APACHE III"""
    if hct >= 60:
        return 3
    elif hct >= 50:
        return 0
    elif hct >= 46:
        return 0
    elif hct >= 30:
        return 2
    elif hct >= 20:
        return 6
    else:
        return 6


def get_apache3_wbc_points(wbc: float) -> float:
    """WBC points for APACHE III"""
    if wbc >= 40:
        return 19
    elif wbc >= 20:
        return 5
    elif wbc >= 15:
        return 0
    elif wbc >= 3:
        return 0
    elif wbc >= 1:
        return 5
    else:
        return 19


def get_apache3_gcs_points(gcs: int) -> float:
    """GCS points for APACHE III (different from APACHE II)"""
    # APACHE III uses different GCS scoring
    if gcs == 15:
        return 0
    elif gcs == 14:
        return 2
    elif gcs == 13:
        return 3
    elif gcs == 12:
        return 5
    elif gcs == 11:
        return 6
    elif gcs == 10:
        return 6
    elif gcs == 9:
        return 7
    elif gcs == 8:
        return 8
    elif gcs == 7:
        return 9
    elif gcs == 6:
        return 10
    elif gcs == 5:
        return 11
    elif gcs == 4:
        return 13
    else:  # GCS 3
        return 16


def get_apache3_age_points(age: int) -> float:
    """Age points for APACHE III"""
    if age < 44:
        return 0
    elif age < 54:
        return 5
    elif age < 64:
        return 11
    elif age < 74:
        return 13
    elif age < 84:
        return 16
    else:
        return 18


def get_apache3_chronic_health_points(
    has_chronic_health: bool,
    is_nonsurgical: bool,
    is_post_emergency_surgery: bool,
    disease_category: str
) -> float:
    """
    Chronic health points for APACHE III
    
    Args:
        has_chronic_health: Whether patient has chronic health condition
        is_nonsurgical: Whether nonsurgical patient
        is_post_emergency_surgery: Whether post-emergency surgery
        disease_category: Disease category (affects points)
    """
    if not has_chronic_health:
        return 0
    
    # APACHE III has disease-specific chronic health points
    # This is simplified - actual APACHE III has more categories
    base_points = {
        "AIDS": 23,
        "Hepatic failure": 16,
        "Lymphoma": 13,
        "Metastatic cancer": 11,
        "Leukemia/MM": 10,
        "Immunosuppression": 10,
        "Cirrhosis": 4,
        "Other": 5
    }
    
    points = base_points.get(disease_category, 5)
    
    # Adjust based on admission type
    if is_nonsurgical:
        return points
    elif is_post_emergency_surgery:
        return points
    else:
        return points * 0.5  # Elective surgery gets lower points


def calculate_apache3(params: dict) -> dict:
    """
    Calculate APACHE III score
    
    Note: This is a simplified implementation. Exact APACHE III requires
    licensed software with proprietary coefficients.
    
    Args:
        params: Dictionary with patient parameters
        
    Returns:
        Dictionary with score and interpretation
    """
    
    # Acute Physiology Score (APS)
    aps = 0.0
    details = []
    
    # 1. Temperature
    temp_points = get_apache3_temp_points(params['temperature'])
    aps += temp_points
    details.append(f"Nhiệt độ {params['temperature']:.1f}°C → {temp_points:.0f} điểm")
    
    # 2. MAP
    map_points = get_apache3_map_points(params['map'])
    aps += map_points
    details.append(f"MAP {params['map']:.0f} mmHg → {map_points:.0f} điểm")
    
    # 3. Heart rate
    hr_points = get_apache3_hr_points(params['heart_rate'])
    aps += hr_points
    details.append(f"Nhịp tim {params['heart_rate']:.0f} /min → {hr_points:.0f} điểm")
    
    # 4. Respiratory rate
    rr_points = get_apache3_rr_points(params['respiratory_rate'])
    aps += rr_points
    details.append(f"Nhịp thở {params['respiratory_rate']:.0f} /min → {rr_points:.0f} điểm")
    
    # 5. Oxygenation
    oxy_points = get_apache3_oxygenation_points(
        params['pao2'], params['fio2'], params.get('is_ventilated', False)
    )
    aps += oxy_points
    if params.get('is_ventilated', False) and params['fio2'] >= 0.5:
        details.append(f"A-a gradient (FiO₂ ≥50%) → {oxy_points:.0f} điểm")
    else:
        details.append(f"PaO₂ {params['pao2']:.0f} mmHg → {oxy_points:.0f} điểm")
    
    # 6. pH
    ph_points = get_apache3_ph_points(params['ph'])
    aps += ph_points
    details.append(f"pH {params['ph']:.2f} → {ph_points:.0f} điểm")
    
    # 7. Sodium
    na_points = get_apache3_na_points(params['sodium'])
    aps += na_points
    details.append(f"Na {params['sodium']:.0f} mEq/L → {na_points:.0f} điểm")
    
    # 8. Potassium
    k_points = get_apache3_k_points(params['potassium'])
    aps += k_points
    details.append(f"K {params['potassium']:.1f} mEq/L → {k_points:.0f} điểm")
    
    # 9. Creatinine
    cr_points = get_apache3_creatinine_points(params['creatinine'], params.get('has_arf', False))
    aps += cr_points
    arf_note = " (ARF)" if params.get('has_arf', False) else ""
    details.append(f"Creatinine {params['creatinine']:.1f} mg/dL → {cr_points:.0f} điểm{arf_note}")
    
    # 10. Hematocrit
    hct_points = get_apache3_hct_points(params['hematocrit'])
    aps += hct_points
    details.append(f"Hematocrit {params['hematocrit']:.1f}% → {hct_points:.0f} điểm")
    
    # 11. WBC
    wbc_points = get_apache3_wbc_points(params['wbc'])
    aps += wbc_points
    details.append(f"WBC {params['wbc']:.1f} ×10³/μL → {wbc_points:.0f} điểm")
    
    # 12. GCS
    gcs_points = get_apache3_gcs_points(params['gcs'])
    aps += gcs_points
    details.append(f"GCS {params['gcs']} → {gcs_points:.0f} điểm")
    
    # Age points
    age_points = get_apache3_age_points(params['age'])
    details.append(f"Tuổi {params['age']} → {age_points:.0f} điểm")
    
    # Chronic health points
    chronic_points = get_apache3_chronic_health_points(
        params.get('has_chronic_health', False),
        params.get('is_nonsurgical', False),
        params.get('is_post_emergency_surgery', False),
        params.get('disease_category', 'Other')
    )
    if chronic_points > 0:
        details.append(f"Bệnh mạn tính ({params.get('disease_category', 'Other')}) → {chronic_points:.0f} điểm")
    
    # Total score
    total_score = aps + age_points + chronic_points
    
    # Predicted mortality (simplified - actual APACHE III uses proprietary formula)
    # This is an approximation based on published data
    # Actual APACHE III uses disease-specific coefficients
    if total_score < 30:
        predicted_mortality = 5.0
    elif total_score < 50:
        predicted_mortality = 10.0 + (total_score - 30) * 0.5
    elif total_score < 70:
        predicted_mortality = 20.0 + (total_score - 50) * 1.0
    elif total_score < 100:
        predicted_mortality = 40.0 + (total_score - 70) * 1.5
    else:
        predicted_mortality = 85.0 + min((total_score - 100) * 0.3, 15.0)
    
    predicted_mortality = min(predicted_mortality, 95.0)
    
    # Interpretation
    if total_score < 30:
        interpretation = "Mức độ nặng THẤP"
        mortality_range = "<10%"
        color = "🟢"
    elif total_score < 50:
        interpretation = "Mức độ nặng TRUNG BÌNH"
        mortality_range = "10-25%"
        color = "🟡"
    elif total_score < 70:
        interpretation = "Mức độ nặng CAO"
        mortality_range = "25-50%"
        color = "🟠"
    elif total_score < 100:
        interpretation = "Mức độ nặng RẤT CAO"
        mortality_range = "50-75%"
        color = "🟠"
    else:
        interpretation = "Mức độ nặng CỰC KỲ CAO"
        mortality_range = ">75%"
        color = "🔴"
    
    return {
        'total_score': round(total_score, 1),
        'aps': round(aps, 1),
        'age_points': round(age_points, 1),
        'chronic_points': round(chronic_points, 1),
        'predicted_mortality': round(predicted_mortality, 1),
        'mortality_range': mortality_range,
        'interpretation': interpretation,
        'color': color,
        'details': details
    }


def render():
    """Render APACHE III calculator"""
    
    st.title("🏥 APACHE III Score")
    st.markdown("**Acute Physiology and Chronic Health Evaluation III - Dự đoán tử vong ICU (Phiên bản cập nhật)**")
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'apache3':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    # Smart Suggestions (sidebar)
    with st.sidebar:
        render_suggestions(
            calculator_id="apache3",
            calculator_name="APACHE III Score",
            category="Cấp cứu",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    # Educational information
    with st.expander("ℹ️ Thông tin & cách sử dụng"):
        st.markdown("""
        ### 📋 Giới Thiệu
        
        **APACHE III** là phiên bản cập nhật của APACHE II:
        - Chính xác hơn trong dự đoán tử vong ICU
        - 17 biến số sinh lý (thay vì 12)
        - Điểm số chi tiết hơn
        - Công thức dự đoán tử vong phức tạp hơn
        
        ### ⚠️ Lưu ý quan trọng
        
        **APACHE III có bản quyền:**
        - Công thức chính xác thuộc Cerner Corporation
        - Calculator này là phiên bản đơn giản hóa dựa trên thông tin công khai
        - Để tính chính xác 100%, cần sử dụng phần mềm có bản quyền
        
        ### 🎯 3 Thành phần
        
        1. **Acute Physiology Score (0-252):** 17 biến số sinh lý
        2. **Age Points (0-24):** Điểm tuổi
        3. **Chronic Health (0-23):** Bệnh mạn tính (theo loại bệnh)
        
        **Tổng điểm:** 0-299 (lý thuyết)
        
        ### 📊 Điểm & Tử vong (Ước tính)
        
        | APACHE III | Tử vong (Ước tính) |
        |------------|-------------------|
        | <30 | <10% |
        | 30-49 | 10-25% |
        | 50-69 | 25-50% |
        | 70-99 | 50-75% |
        | ≥100 | >75% |
        
        ### ⚠️ Lưu ý
        
        - Tính trong 24h ĐẦU nhập ICU
        - Lấy giá trị TỆ NHẤT trong 24h
        - Không tính lại trong ICU stay
        
        ### 📚 Tham khảo
        
        - Knaus WA, et al. *Chest* 1991;100:1619-1636
        - **Lưu ý:** Công thức chính xác cần license từ Cerner
        """)
    
    st.divider()
    
    st.subheader("📝 Nhập dữ liệu (Giá trị TỆ NHẤT trong 24h đầu ICU)")
    
    # Demographics
    st.markdown("#### 👤 Thông tin chung")
    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("Tuổi", 0, 120, 50, 1, format="%d", key="apache3_age")
    with col2:
        gcs = st.number_input("GCS (Thang điểm hôn mê Glasgow)", 3, 15, 15, 1, format="%d", key="apache3_gcs")
    
    st.divider()
    
    # Vital signs
    st.markdown("#### 🩺 Sinh hiệu")
    col3, col4, col5 = st.columns(3)
    with col3:
        temperature = st.number_input("Nhiệt độ (°C)", 20.0, 45.0, 37.0, 0.1, format="%.1f", key="apache3_temp")
    with col4:
        map_val = st.number_input("MAP (mmHg)", 0, 250, 70, 1, format="%d", key="apache3_map")
        st.caption("MAP = (SBP + 2×DBP)/3")
    with col5:
        heart_rate = st.number_input("Nhịp tim (/min)", 0, 250, 80, 1, format="%d", key="apache3_hr")
    
    respiratory_rate = st.number_input("Nhịp thở (/min)", 0, 100, 16, 1, format="%d", key="apache3_rr")
    
    st.divider()
    
    # ABG
    st.markdown("#### 🫁 Khí máu động mạch (ABG)")
    is_ventilated = st.checkbox("Đang thở máy", key="apache3_ventilated")
    
    col6, col7, col8 = st.columns(3)
    with col6:
        fio2 = st.number_input("FiO₂ (%)", 21, 100, 21, 1, format="%d", key="apache3_fio2")
    with col7:
        pao2 = st.number_input("PaO₂ (mmHg)", 0, 700, 100, 1, format="%d", key="apache3_pao2")
    with col8:
        paco2 = st.number_input("PaCO₂ (mmHg)", 0, 150, 40, 1, format="%d", key="apache3_paco2")
    
    ph = st.number_input("pH", 6.5, 8.0, 7.40, 0.01, format="%.2f", key="apache3_ph")
    
    st.divider()
    
    # Labs
    st.markdown("#### 🔬 Xét nghiệm")
    col9, col10 = st.columns(2)
    with col9:
        sodium = st.number_input("Sodium (mEq/L)", 80.0, 200.0, 140.0, 1.0, format="%.1f", key="apache3_na")
        potassium = st.number_input("Potassium (mEq/L)", 1.5, 10.0, 4.0, 0.1, format="%.1f", key="apache3_k")
        creatinine = st.number_input("Creatinine (mg/dL)", 0.0, 20.0, 1.0, 0.1, format="%.1f", key="apache3_cr")
        has_arf = st.checkbox("**Suy thận cấp (ARF)** - tăng điểm Cr", key="apache3_arf")
    
    with col10:
        hematocrit = st.number_input("Hematocrit (%)", 0.0, 80.0, 40.0, 0.1, format="%.1f", key="apache3_hct")
        wbc = st.number_input("WBC (×10³/μL)", 0.0, 100.0, 10.0, 0.1, format="%.1f", key="apache3_wbc")
    
    st.divider()
    
    # Chronic health
    st.markdown("#### 🏥 Bệnh mạn tính")
    has_chronic_health = st.checkbox(
        "**Có bệnh mạn tính nặng**",
        help="AIDS, suy gan, lymphoma, ung thư di căn, leukemia, suy giảm miễn dịch, xơ gan",
        key="apache3_chronic"
    )
    
    if has_chronic_health:
        col11, col12 = st.columns(2)
        with col11:
            is_nonsurgical = st.checkbox("Bệnh nhân nội khoa (nonsurgical)", key="apache3_nonsurgical")
        with col12:
            is_post_emergency_surgery = st.checkbox("Sau phẫu thuật cấp cứu", key="apache3_emergency_surg")
        
        disease_category = st.selectbox(
            "Loại bệnh mạn tính:",
            ["AIDS", "Hepatic failure", "Lymphoma", "Metastatic cancer", 
             "Leukemia/MM", "Immunosuppression", "Cirrhosis", "Other"],
            key="apache3_disease"
        )
    else:
        is_nonsurgical = False
        is_post_emergency_surgery = False
        disease_category = "Other"
    
    st.divider()
    
    # Calculate
    if st.button("🧮 Tính APACHE III Score", type="primary", use_container_width=True, key="apache3_calculate"):
        # Validate inputs
        validation_errors = []
        
        is_valid_age, age_error = validate_age(age, 0, 120)
        if not is_valid_age:
            validation_errors.append(age_error)
        
        is_valid_gcs, gcs_error = validate_gcs(gcs)
        if not is_valid_gcs:
            validation_errors.append(gcs_error)
        
        is_valid_temp, temp_error = validate_temperature(temperature)
        if not is_valid_temp:
            validation_errors.append(temp_error)
        
        if validation_errors:
            st.error("**⚠️ Lỗi validation:**")
            for error in validation_errors:
                st.error(f"- {error}")
            st.stop()
        
        params = {
            'age': age,
            'temperature': temperature,
            'map': map_val,
            'heart_rate': heart_rate,
            'respiratory_rate': respiratory_rate,
            'fio2': fio2 / 100.0,  # Convert to fraction
            'pao2': pao2,
            'paco2': paco2,
            'ph': ph,
            'sodium': sodium,
            'potassium': potassium,
            'creatinine': creatinine,
            'has_arf': has_arf,
            'hematocrit': hematocrit,
            'wbc': wbc,
            'gcs': gcs,
            'is_ventilated': is_ventilated,
            'has_chronic_health': has_chronic_health,
            'is_post_emergency_surgery': is_post_emergency_surgery,
            'is_nonsurgical': is_nonsurgical,
            'disease_category': disease_category
        }
        
        result = calculate_apache3(params)
        
        # Display results
        st.subheader("📊 Kết quả")

        # Determine risk level for color coding
        if result['total_score'] < 30:
            risk_level_code = "low"
        elif result['total_score'] < 50:
            risk_level_code = "moderate"
        elif result['total_score'] < 70:
            risk_level_code = "high"
        elif result['total_score'] < 100:
            risk_level_code = "very_high"
        else:
            risk_level_code = "critical"

        # Display score with color coding badge
        st.markdown(f"## APACHE III Score = {result['total_score']:.1f}")
        render_risk_badge(
            risk_level=risk_level_code,
            label=result['interpretation'],
            value=result['total_score']
        )

        # Color-coded score result
        mortality_text = f"{result['predicted_mortality']:.1f}% (Khoảng: {result['mortality_range']})"
        render_score_result(
            title="APACHE III Score",
            score=result['total_score'],
            interpretation=result['interpretation'],
            mortality=mortality_text,
            icon=result['color'],
            thresholds={"low": 50, "moderate": 70, "high": 100},
            size="large"
        )
        
        # Score breakdown
        breakdown_scores = {
            "Acute Physiology Score (APS)": f"{result['aps']:.0f}",
            "Age Points": f"{result['age_points']:.0f}",
            "Chronic Health Points": f"{result['chronic_points']:.0f}",
        }
        
        render_score_breakdown(
            title="📋 Chi tiết điểm số",
            subscores=breakdown_scores,
            total_score=result['total_score']
        )
        
        # Detailed scoring breakdown
        with st.expander("📝 Chi tiết từng biến số", expanded=False):
            for detail in result['details']:
                st.markdown(f"- {detail}")

        # Visual Charts
        st.markdown("---")
        st.markdown("### 📊 Biểu Đồ Nguy Cơ")
        col_chart1, col_chart2 = st.columns(2)

        with col_chart1:
            render_risk_gauge_chart(
                value=result['total_score'],
                min_value=0,
                max_value=150,
                thresholds={
                    "Low": 30,
                    "Moderate": 50,
                    "High": 70,
                    "Very High": 100,
                },
                title="APACHE III Score",
            )

        with col_chart2:
            render_risk_bar_chart(
                value=result['total_score'],
                thresholds={
                    "Low": 30,
                    "Moderate": 50,
                    "High": 70,
                    "Very High": 100,
                },
                max_value=150,
                title="Risk Level",
                show_value=True,
            )

        # Warning about simplified calculation
        st.warning("""
        **⚠️ Lưu ý quan trọng:**
        
        - Đây là phiên bản **đơn giản hóa** của APACHE III
        - Công thức chính xác thuộc Cerner Corporation và cần license
        - Kết quả dự đoán tử vong là **ước tính** dựa trên thông tin công khai
        - Để tính chính xác 100%, cần sử dụng phần mềm có bản quyền
        """)
        
        # Interpretation
        st.info("""
        **📌 Diễn giải:**
        
        - APACHE III dự đoán tử vong ICU (chính xác hơn APACHE II)
        - Tính 1 LẦN trong 24h đầu nhập ICU (giá trị tệ nhất)
        - Điểm càng cao → nguy cơ tử vong càng cao
        - Không nên tính lại trong thời gian nằm ICU
        """)
        
        if result['total_score'] >= 100:
            st.error("""
            **🚨 APACHE III SCORE RẤT CAO:**
            
            - Nguy cơ tử vong >75%
            - Cần hồi sức rất tích cực
            - Xem xét mức độ chăm sóc và tiên lượng
            - Thảo luận với gia đình về mục tiêu điều trị
            """)
        
        # Prepare inputs for history and share
        inputs_dict = {
            "Age": f"{age} tuổi",
            "Temperature": f"{temperature:.1f}°C",
            "MAP": f"{map_val:.0f} mmHg",
            "Heart Rate": f"{heart_rate:.0f} /min",
            "Respiratory Rate": f"{respiratory_rate:.0f} /min",
            "FiO₂": f"{fio2:.0f}%",
            "PaO₂": f"{pao2:.0f} mmHg",
            "PaCO₂": f"{paco2:.0f} mmHg",
            "pH": f"{ph:.2f}",
            "Sodium": f"{sodium:.0f} mEq/L",
            "Potassium": f"{potassium:.1f} mEq/L",
            "Creatinine": f"{creatinine:.1f} mg/dL",
            "Has ARF": "Có" if has_arf else "Không",
            "Hematocrit": f"{hematocrit:.1f}%",
            "WBC": f"{wbc:.1f} ×10³/μL",
            "GCS": f"{gcs}",
            "Is Ventilated": "Có" if is_ventilated else "Không",
            "Chronic Health": "Có" if has_chronic_health else "Không",
            "Disease Category": disease_category if has_chronic_health else "Không"
        }
        
        results_dict = {
            "APACHE III Score": f"{result['total_score']:.1f}",
            "Predicted Mortality": f"{result['predicted_mortality']:.1f}%",
            "Mortality Range": result['mortality_range'],
            "Interpretation": result['interpretation'],
            "Risk Level Code": risk_level_code,
            "APS": f"{result['aps']:.0f} điểm",
            "Age Points": f"{result['age_points']:.0f} điểm",
            "Chronic Health Points": f"{result['chronic_points']:.0f} điểm",
        }

        # Export section (new component)
        st.markdown("---")
        render_scores_export(
            calculator_name="APACHE III Score",
            inputs=inputs_dict,
            results=results_dict,
            specialty="Cấp cứu & Hồi sức",
        )

        # Keep old export for compatibility
        st.markdown("---")
        render_export_section(
            title="APACHE III Score",
            inputs=inputs_dict,
            results=results_dict,
            calculator_name="APACHE III Score",
        )
        
        # Save to history
        save_calculation_to_history(
            calculator_id="apache3",
            calculator_name="APACHE III Score",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Share section
        render_share_section(
            calculator_id="apache3",
            calculator_name="APACHE III Score",
            inputs=inputs_dict,
            results=results_dict,
            show_qr=True
        )
        
        # History section
        st.markdown("---")
        render_history_ui(calculator_id="apache3", show_actions=True)
        
        st.session_state['apache3_result'] = result
    
    # Reference
    with st.expander("📖 Thông tin về APACHE III"):
        st.markdown("""
        ### APACHE III vs APACHE II
        
        **Cải tiến:**
        - 17 biến số (thay vì 12)
        - Điểm số chi tiết hơn
        - Công thức dự đoán tử vong phức tạp hơn
        - Chính xác hơn trong dự đoán
        
        **Hạn chế:**
        - Công thức có bản quyền (Cerner Corporation)
        - Cần license để tính chính xác
        - Phức tạp hơn APACHE II
        
        ### 📚 Tài liệu tham khảo
        
        - Knaus WA, et al. The APACHE III prognostic system. Risk prediction of hospital
          mortality for critically ill hospitalized adults. Chest. 1991;100(6):1619-1636.
        
        - **Lưu ý:** Công thức chính xác cần license từ Cerner Corporation
        """)
    
    # References section
    references = get_references("APACHE III")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-01-15",
            show_evidence_level=True,
            show_links=True
        )
    
    st.caption("⚠️ APACHE III chỉ là công cụ hỗ trợ. Quyết định điều trị phải dựa trên đánh giá lâm sàng toàn diện.")

