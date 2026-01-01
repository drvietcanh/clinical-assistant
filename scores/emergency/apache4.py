"""
APACHE IV Score (Acute Physiology and Chronic Health Evaluation IV)
=====================================================================

ICU mortality prediction scoring system - Latest version (2006)

Reference:
- Zimmerman JE, et al. Acute Physiology and Chronic Health Evaluation (APACHE) IV: 
  hospital mortality assessment for today's critically ill patients. 
  Crit Care Med. 2006;34(5):1297-1310.

APACHE IV Components:
1. Acute Physiology Score (APS): Multiple physiological variables
2. Age points
3. Chronic Health points
4. Disease-specific coefficients

Key Improvements over APACHE III:
- Updated with more recent patient data (2002-2003)
- More accurate mortality prediction
- Disease-specific risk adjustment
- Better calibration for modern ICU populations

Clinical Utility:
- Predict ICU mortality (most accurate APACHE version)
- Stratify disease severity
- Research and quality improvement
- ICU resource allocation

Note: This is a simplified implementation. Exact APACHE IV calculation 
requires licensed software from Cerner Corporation. This calculator provides
an approximation based on published methodology.
"""

import streamlit as st
from config.theme import COLORS
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


def get_apache4_temp_points(temp: float) -> float:
    """Temperature points for APACHE IV (similar to APACHE III but refined)"""
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


def get_apache4_map_points(map_val: float) -> float:
    """MAP points for APACHE IV"""
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


def get_apache4_hr_points(hr: float) -> float:
    """Heart rate points for APACHE IV"""
    if hr >= 180:
        return 17
    elif hr >= 140:
        return 8
    elif hr >= 110:
        return 5
    elif hr >= 70:
        return 0
    elif hr >= 55:
        return 5
    elif hr >= 40:
        return 13
    else:
        return 17


def get_apache4_rr_points(rr: float, is_ventilated: bool) -> float:
    """Respiratory rate points for APACHE IV"""
    if is_ventilated:
        # On ventilator - different scoring
        if rr >= 50:
            return 17
        elif rr >= 35:
            return 11
        elif rr >= 25:
            return 6
        elif rr >= 12:
            return 0
        elif rr >= 10:
            return 1
        else:
            return 8
    else:
        # Spontaneous breathing
        if rr >= 50:
            return 17
        elif rr >= 35:
            return 11
        elif rr >= 25:
            return 6
        elif rr >= 12:
            return 0
        elif rr >= 10:
            return 1
        else:
            return 8


def get_apache4_oxygenation_points(fio2: float, pao2: float, paco2: float, ph: float, is_ventilated: bool) -> float:
    """Oxygenation points for APACHE IV"""
    if is_ventilated or fio2 >= 0.5:
        # Calculate A-a gradient
        aa_gradient = (fio2 * (760 - 47)) - (paco2 / 0.8) - pao2
        if aa_gradient >= 500:
            return 14
        elif aa_gradient >= 350:
            return 11
        elif aa_gradient >= 200:
            return 6
        else:
            return 0
    else:
        # Spontaneous breathing - use PaO2
        if pao2 < 55:
            return 11
        elif pao2 < 60:
            return 9
        elif pao2 < 70:
            return 7
        else:
            return 0


def get_apache4_ph_points(ph: float) -> float:
    """pH points for APACHE IV"""
    if ph >= 7.7:
        return 12
    elif ph >= 7.6:
        return 3
    elif ph >= 7.5:
        return 0
    elif ph >= 7.33:
        return 0
    elif ph >= 7.25:
        return 3
    elif ph >= 7.15:
        return 12
    else:
        return 12


def get_apache4_na_points(na: float) -> float:
    """Sodium points for APACHE IV"""
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
        return 4
    else:
        return 4


def get_apache4_k_points(k: float) -> float:
    """Potassium points for APACHE IV"""
    if k >= 7.0:
        return 4
    elif k >= 6.0:
        return 3
    elif k >= 5.5:
        return 1
    elif k >= 3.5:
        return 0
    elif k >= 3.0:
        return 1
    elif k >= 2.5:
        return 2
    else:
        return 4


def get_apache4_cr_points(cr: float, is_aki: bool) -> float:
    """Creatinine points for APACHE IV"""
    if is_aki:
        # Acute kidney injury - higher points
        if cr >= 3.5:
            return 8
        elif cr >= 2.0:
            return 6
        elif cr >= 1.5:
            return 4
        else:
            return 0
    else:
        # Chronic or normal
        if cr >= 3.5:
            return 4
        elif cr >= 2.0:
            return 3
        elif cr >= 1.5:
            return 2
        else:
            return 0


def get_apache4_hct_points(hct: float) -> float:
    """Hematocrit points for APACHE IV"""
    if hct >= 60:
        return 4
    elif hct >= 50:
        return 2
    elif hct >= 46:
        return 0
    elif hct >= 30:
        return 0
    elif hct >= 20:
        return 2
    else:
        return 4


def get_apache4_wbc_points(wbc: float) -> float:
    """White blood cell count points for APACHE IV"""
    if wbc >= 40:
        return 4
    elif wbc >= 20:
        return 2
    elif wbc >= 15:
        return 1
    elif wbc >= 3:
        return 0
    elif wbc >= 1:
        return 2
    else:
        return 4


def get_apache4_gcs_points(gcs: float) -> float:
    """GCS points for APACHE IV (15-GCS)"""
    return 15 - gcs


def get_apache4_age_points(age: float) -> float:
    """Age points for APACHE IV"""
    if age >= 75:
        return 24
    elif age >= 65:
        return 16
    elif age >= 55:
        return 8
    elif age >= 45:
        return 4
    else:
        return 0


def get_apache4_chronic_health_points(
    has_immunosuppression: bool,
    has_hepatic_failure: bool,
    has_cirrhosis: bool,
    has_lymphoma: bool,
    has_metastatic_cancer: bool,
    has_leukemia: bool,
    has_aids: bool
) -> float:
    """Chronic health points for APACHE IV"""
    points = 0
    
    if has_immunosuppression:
        points += 10
    if has_hepatic_failure or has_cirrhosis:
        points += 16
    if has_lymphoma:
        points += 13
    if has_metastatic_cancer:
        points += 11
    if has_leukemia:
        points += 10
    if has_aids:
        points += 17
    
    return points


def estimate_apache4_mortality(apache4_score: float, diagnosis_category: str = "General") -> float:
    """
    Estimate mortality risk from APACHE IV score
    
    Note: This is a simplified estimation. Actual APACHE IV uses 
    complex disease-specific equations that require licensed software.
    """
    # Simplified mortality estimation based on score ranges
    # Actual APACHE IV uses logistic regression with disease-specific coefficients
    
    if apache4_score < 20:
        base_mortality = 0.02  # 2%
    elif apache4_score < 40:
        base_mortality = 0.05  # 5%
    elif apache4_score < 60:
        base_mortality = 0.10  # 10%
    elif apache4_score < 80:
        base_mortality = 0.20  # 20%
    elif apache4_score < 100:
        base_mortality = 0.35  # 35%
    elif apache4_score < 120:
        base_mortality = 0.50  # 50%
    elif apache4_score < 140:
        base_mortality = 0.65  # 65%
    else:
        base_mortality = 0.80  # 80%
    
    # Adjust based on diagnosis category (simplified)
    adjustments = {
        "Cardiac": 1.1,
        "Respiratory": 1.15,
        "Neurological": 1.2,
        "Sepsis": 1.25,
        "Trauma": 0.9,
        "Post-operative": 0.95,
        "General": 1.0
    }
    
    adjusted_mortality = base_mortality * adjustments.get(diagnosis_category, 1.0)
    adjusted_mortality = min(adjusted_mortality, 0.95)  # Cap at 95%
    
    return adjusted_mortality * 100  # Return as percentage


def render():
    """Render APACHE IV calculator"""
    
    # st.title("📊 APACHE IV Score")
    st.markdown(f"""
    <h2 style='text-align: center; color: {COLORS['success']};'>📊 APACHE IV Score</h2>
    <p style='text-align: center;'><em>Dự đoán tử vong ICU - Phiên bản mới nhất (2006)</em></p>
    """, unsafe_allow_html=True)
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'apache4':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    # Educational information
    with st.expander("ℹ️ Thông tin & cách sử dụng"):
        st.markdown("""
        ### 📋 Giới Thiệu
        
        **APACHE IV** là phiên bản mới nhất của hệ thống APACHE:
        - Phát triển năm 2006 với dữ liệu từ 2002-2003
        - Chính xác hơn APACHE II và APACHE III
        - Sử dụng công thức dự đoán tử vong cập nhật
        - Điều chỉnh theo từng loại bệnh cụ thể
        
        ### 🎯 Các thành phần
        
        1. **Acute Physiology Score (APS):** Nhiều biến số sinh lý
        2. **Điểm tuổi:** 0-24 điểm
        3. **Điểm bệnh mạn tính:** 0-23+ điểm
        4. **Hệ số điều chỉnh theo bệnh:** Tùy chẩn đoán chính
        
        ### ⚠️ Lưu ý
        
        - Đây là phiên bản **ĐƠN GIẢN HÓA**
        - APACHE IV chính xác yêu cầu phần mềm có bản quyền từ Cerner
        - Kết quả dự đoán tử vong là ước tính, không thay thế đánh giá lâm sàng
        """)
    
    st.divider()
    
    # Smart Suggestions
    col_sugg1, col_sugg2 = st.columns([2, 1])
    with col_sugg2:
        render_suggestions(
            calculator_id="apache4",
            calculator_name="APACHE IV",
            category="Cấp cứu",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    # Input section
    st.subheader("📝 Nhập thông tin")
    
    # Basic info
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 👤 Thông tin Cơ bản")
        age = st.number_input("Tuổi", 0, 120, 60, 1, format="%d")
        
        diagnosis_category = st.selectbox(
            "Chẩn đoán chính",
            ["General", "Cardiac", "Respiratory", "Neurological", "Sepsis", "Trauma", "Post-operative"],
            index=0,
            help="Chọn nhóm chẩn đoán chính để điều chỉnh dự đoán"
        )
    
    with col2:
        st.markdown("#### 🫁 Hỗ trợ Hô hấp")
        is_ventilated = st.checkbox("Đang thở máy", help="Bệnh nhân đang thở máy")
        
        fio2 = st.number_input(
            "FiO₂ (%)",
            21.0, 100.0, 21.0, 1.0,
            format="%.0f",
            help="Nồng độ oxy trong khí thở vào"
        ) / 100.0  # Convert to fraction
    
    st.divider()
    
    # Vital signs
    st.markdown("#### 🩺 Sinh hiệu")
    
    col3, col4, col5 = st.columns(3)
    
    with col3:
        temperature = st.number_input(
            "Nhiệt độ (°C)",
            30.0, 45.0, 37.0, 0.1,
            format="%.1f"
        )
        
        map_val = st.number_input(
            "MAP (mmHg)",
            30.0, 200.0, 80.0, 1.0,
            format="%.0f",
            help="Mean Arterial Pressure"
        )
    
    with col4:
        heart_rate = st.number_input(
            "Nhịp tim (bpm)",
            30, 250, 80, 1,
            format="%d"
        )
        
        respiratory_rate = st.number_input(
            "Nhịp thở (/min)",
            0, 60, 18, 1,
            format="%d"
        )
    
    with col5:
        gcs = st.number_input(
            "GCS",
            3.0, 15.0, 15.0, 0.5,
            format="%.1f",
            help="Glasgow Coma Scale"
        )
    
    st.divider()
    
    # Blood gases
    st.markdown("#### 🔬 Khí máu động mạch")
    
    col6, col7, col8 = st.columns(3)
    
    with col6:
        pao2 = st.number_input(
            "PaO₂ (mmHg)",
            20.0, 600.0, 100.0, 1.0,
            format="%.0f"
        )
    
    with col7:
        paco2 = st.number_input(
            "PaCO₂ (mmHg)",
            15.0, 120.0, 40.0, 1.0,
            format="%.0f"
        )
    
    with col8:
        ph = st.number_input(
            "pH",
            6.8, 7.8, 7.4, 0.01,
            format="%.2f"
        )
    
    st.divider()
    
    # Labs
    st.markdown("#### 🧪 Xét nghiệm")
    
    col9, col10, col11, col12 = st.columns(4)
    
    with col9:
        sodium = st.number_input(
            "Na⁺ (mEq/L)",
            100.0, 200.0, 140.0, 1.0,
            format="%.0f"
        )
        
        potassium = st.number_input(
            "K⁺ (mEq/L)",
            1.0, 10.0, 4.0, 0.1,
            format="%.1f"
        )
    
    with col10:
        creatinine = st.number_input(
            "Creatinine (mg/dL)",
            0.1, 15.0, 1.0, 0.1,
            format="%.1f"
        )
        
        is_aki = st.checkbox(
            "AKI (Suy thận cấp)",
            help="Có suy thận cấp (AKI)"
        )
    
    with col11:
        hematocrit = st.number_input(
            "Hematocrit (%)",
            10.0, 70.0, 40.0, 0.1,
            format="%.1f"
        )
    
    with col12:
        wbc = st.number_input(
            "WBC (×10³/μL)",
            0.0, 100.0, 7.0, 0.1,
            format="%.1f"
        )
    
    st.divider()
    
    # Chronic health
    st.markdown("#### 🏥 Bệnh mạn tính")
    
    col13, col14 = st.columns(2)
    
    with col13:
        has_immunosuppression = st.checkbox("Ức chế miễn dịch")
        has_hepatic_failure = st.checkbox("Suy gan")
        has_cirrhosis = st.checkbox("Xơ gan")
        has_lymphoma = st.checkbox("Lymphoma")
    
    with col14:
        has_metastatic_cancer = st.checkbox("Ung thư di căn")
        has_leukemia = st.checkbox("Bệnh bạch cầu")
        has_aids = st.checkbox("AIDS")
    
    st.divider()
    
    # Calculate button
    if st.button("🧮 Tính APACHE IV", type="primary", use_container_width=True):
        # Validate inputs
        validation_errors = []
        
        is_valid_age, age_error = validate_age(age, 0, 120)
        if not is_valid_age:
            validation_errors.append(f"Tuổi: {age_error}")
        
        is_valid_gcs, gcs_error = validate_gcs(gcs)
        if not is_valid_gcs:
            validation_errors.append(f"GCS: {gcs_error}")
        
        if validation_errors:
            from components.ui.validation import render_validation_errors
            render_validation_errors(validation_errors)
            return
        
        # Calculate APACHE IV score
        aps = 0
        details = []
        
        # Temperature
        temp_points = get_apache4_temp_points(temperature)
        aps += temp_points
        details.append(f"Nhiệt độ {temperature:.1f}°C → {temp_points} điểm")
        
        # MAP
        map_points = get_apache4_map_points(map_val)
        aps += map_points
        details.append(f"MAP {map_val:.0f} mmHg → {map_points} điểm")
        
        # Heart rate
        hr_points = get_apache4_hr_points(heart_rate)
        aps += hr_points
        details.append(f"Nhịp tim {heart_rate} bpm → {hr_points} điểm")
        
        # Respiratory rate
        rr_points = get_apache4_rr_points(respiratory_rate, is_ventilated)
        aps += rr_points
        details.append(f"Nhịp thở {respiratory_rate} /min ({'thở máy' if is_ventilated else 'tự thở'}) → {rr_points} điểm")
        
        # Oxygenation
        oxy_points = get_apache4_oxygenation_points(fio2, pao2, paco2, ph, is_ventilated)
        aps += oxy_points
        if is_ventilated or fio2 >= 0.5:
            details.append(f"A-a gradient (FiO₂ {fio2*100:.0f}%) → {oxy_points} điểm")
        else:
            details.append(f"PaO₂ {pao2:.0f} mmHg → {oxy_points} điểm")
        
        # pH
        ph_points = get_apache4_ph_points(ph)
        aps += ph_points
        details.append(f"pH {ph:.2f} → {ph_points} điểm")
        
        # Sodium
        na_points = get_apache4_na_points(sodium)
        aps += na_points
        details.append(f"Na⁺ {sodium:.0f} mEq/L → {na_points} điểm")
        
        # Potassium
        k_points = get_apache4_k_points(potassium)
        aps += k_points
        details.append(f"K⁺ {potassium:.1f} mEq/L → {k_points} điểm")
        
        # Creatinine
        cr_points = get_apache4_cr_points(creatinine, is_aki)
        aps += cr_points
        details.append(f"Creatinine {creatinine:.1f} mg/dL ({'AKI' if is_aki else 'bình thường'}) → {cr_points} điểm")
        
        # Hematocrit
        hct_points = get_apache4_hct_points(hematocrit)
        aps += hct_points
        details.append(f"Hematocrit {hematocrit:.1f}% → {hct_points} điểm")
        
        # WBC
        wbc_points = get_apache4_wbc_points(wbc)
        aps += wbc_points
        details.append(f"WBC {wbc:.1f} ×10³/μL → {wbc_points} điểm")
        
        # GCS
        gcs_points = get_apache4_gcs_points(gcs)
        aps += gcs_points
        details.append(f"GCS {gcs:.1f} → {gcs_points} điểm")
        
        # Age
        age_points = get_apache4_age_points(age)
        details.append(f"Tuổi {age} → {age_points} điểm")
        
        # Chronic health
        chronic_points = get_apache4_chronic_health_points(
            has_immunosuppression,
            has_hepatic_failure,
            has_cirrhosis,
            has_lymphoma,
            has_metastatic_cancer,
            has_leukemia,
            has_aids
        )
        if chronic_points > 0:
            details.append(f"Bệnh mạn tính → {chronic_points} điểm")
        
        # Total score
        total_score = aps + age_points + chronic_points
        
        # Estimate mortality
        estimated_mortality = estimate_apache4_mortality(total_score, diagnosis_category)
        
        # Display results
        st.subheader("📊 Kết quả")

        # Risk category
        if estimated_mortality < 5:
            risk_category = "Thấp"
            risk_level_code = "low"
        elif estimated_mortality < 15:
            risk_category = "Trung bình"
            risk_level_code = "moderate"
        elif estimated_mortality < 30:
            risk_category = "Cao"
            risk_level_code = "high"
        else:
            risk_category = "Rất cao"
            risk_level_code = "very_high"

        # Display score with color coding badge
        st.markdown(f"## APACHE IV Score = {total_score:.0f}")
        render_risk_badge(
            risk_level=risk_level_code,
            label=f"Nguy cơ {risk_category}",
            value=total_score,
        )

        col_r1, col_r2, col_r3 = st.columns(3)

        with col_r1:
            st.metric(
                "**APACHE IV Score**",
                f"{total_score:.0f}",
            )

        with col_r2:
            st.metric(
                "**APS**",
                f"{aps:.0f}",
                help="Acute Physiology Score",
            )

        with col_r3:
            st.metric(
                "**Dự đoán tử vong**",
                f"{estimated_mortality:.1f}%",
                delta=f"{diagnosis_category}",
            )

        st.markdown(f"### {risk_category.upper()}")
        
        # Visual Charts
        st.markdown("---")
        st.markdown("### 📊 Biểu Đồ Nguy Cơ")
        col_chart1, col_chart2 = st.columns(2)

        with col_chart1:
            render_risk_gauge_chart(
                value=total_score,
                min_value=0,
                max_value=150,
                thresholds={
                    "Low": 40,
                    "Moderate": 60,
                    "High": 100,
                },
                title="APACHE IV Score",
            )

        with col_chart2:
            render_risk_bar_chart(
                value=total_score,
                thresholds={
                    "Low": 40,
                    "Moderate": 60,
                    "High": 100,
                },
                max_value=150,
                title="Risk Level",
                show_value=True,
            )

        # Score breakdown
        with st.expander("📋 Chi tiết điểm số", expanded=True):
            st.markdown("#### Acute Physiology Score (APS)")
            for detail in details[:12]:  # First 12 are APS components
                st.markdown(f"- {detail}")

            st.markdown("#### Điểm bổ sung")
            for detail in details[12:]:  # Age and chronic health
                st.markdown(f"- {detail}")
        
        # Recommendations
        st.markdown("---")
        st.markdown("### 💡 Lưu ý")
        
        st.info("""
        **📌 Quan trọng:**
        
        - Đây là phiên bản **ĐƠN GIẢN HÓA** của APACHE IV
        - APACHE IV chính xác yêu cầu phần mềm có bản quyền từ Cerner Corporation
        - Dự đoán tử vong là ước tính, không thay thế đánh giá lâm sàng
        - Kết quả chỉ mang tính tham khảo cho nghiên cứu và đánh giá chất lượng
        
        **So sánh với APACHE II/III:**
        - APACHE IV chính xác hơn với dữ liệu cập nhật (2002-2003)
        - Sử dụng công thức dự đoán tử vong phức tạp hơn
        - Điều chỉnh theo từng loại bệnh cụ thể
        """)
        
        # Prepare inputs and results
        inputs_dict = {
            "Age": f"{age} tuổi",
            "Diagnosis Category": diagnosis_category,
            "Ventilated": "Có" if is_ventilated else "Không",
            "Temperature": f"{temperature:.1f}°C",
            "MAP": f"{map_val:.0f} mmHg",
            "Heart Rate": f"{heart_rate} bpm",
            "Respiratory Rate": f"{respiratory_rate} /min",
            "GCS": f"{gcs:.1f}",
            "PaO₂": f"{pao2:.0f} mmHg",
            "PaCO₂": f"{paco2:.0f} mmHg",
            "pH": f"{ph:.2f}",
            "Sodium": f"{sodium:.0f} mEq/L",
            "Potassium": f"{potassium:.1f} mEq/L",
            "Creatinine": f"{creatinine:.1f} mg/dL",
            "Hematocrit": f"{hematocrit:.1f}%",
            "WBC": f"{wbc:.1f} ×10³/μL"
        }
        
        results_dict = {
            "APACHE IV Score": f"{total_score:.0f}",
            "APS": f"{aps:.0f}",
            "Estimated Mortality": f"{estimated_mortality:.1f}%",
            "Risk Category": risk_category,
            "Risk Level Code": risk_level_code,
        }

        # Export section (new component)
        st.markdown("---")
        render_scores_export(
            calculator_name="APACHE IV",
            inputs=inputs_dict,
            results=results_dict,
            specialty="Cấp cứu & Hồi sức",
        )

        # Keep old export for compatibility
        st.markdown("---")
        render_export_section(
            title="APACHE IV",
            inputs=inputs_dict,
            results=results_dict,
            calculator_name="APACHE IV",
        )
        
        # Save to history
        save_calculation_to_history(
            calculator_id="apache4",
            calculator_name="APACHE IV",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Share section
        render_share_section(
            calculator_id="apache4",
            calculator_name="APACHE IV",
            inputs=inputs_dict,
            results=results_dict,
            show_qr=True
        )
        
        # History section
        st.markdown("---")
        render_history_ui(calculator_id="apache4", show_actions=True)
        
        # References section
        references = get_references("APACHE IV")
        if references:
            render_references_section(
                references=references,
                title="📚 Tài liệu tham khảo",
                last_updated="2024-01-15",
                show_evidence_level=True,
                show_links=True
            )
        
        st.session_state['apache4_result'] = {
            'score': total_score,
            'mortality': estimated_mortality,
            'risk_category': risk_category
        }
    
    # Always show references at the bottom
    st.markdown("---")
    references = get_references("APACHE IV")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-01-15",
            show_evidence_level=True,
            show_links=True
        )
    else:
        with st.expander("📚 Tài liệu tham khảo"):
            st.markdown("""
            **APACHE IV Score**
            
            **Reference:**
            Zimmerman JE, Kramer AA, McNair DS, Malila FM. Acute Physiology and Chronic Health 
            Evaluation (APACHE) IV: hospital mortality assessment for today's critically ill patients. 
            Crit Care Med. 2006;34(5):1297-1310.
            
            **Key Features:**
            - Updated with data from 2002-2003
            - More accurate than APACHE II/III
            - Disease-specific risk adjustment
            - Requires licensed software for exact calculation
            
            **Note:**
            This calculator provides a simplified approximation. For exact APACHE IV calculation, 
            please use licensed software from Cerner Corporation.
            """)
    
    st.markdown("---")
    st.caption("⚠️ Công cụ hỗ trợ lâm sàng - không thay thế đánh giá lâm sàng toàn diện")

