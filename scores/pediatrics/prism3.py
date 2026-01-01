"""
PRISM III - Pediatric Risk of Mortality Score
ICU mortality prediction for pediatric patients

Reference:
Pollack MM, et al. The Pediatric Risk of Mortality (PRISM) III Score System.
Pediatr Crit Care Med. 2016;17(7):671-680.
"""

import streamlit as st
import math
from scores.utils.validation import (
    validate_age,
    validate_blood_pressure,
    validate_heart_rate,
    validate_respiratory_rate,
    validate_temperature,
    validate_gcs,
    validate_lab_value
)
from components.ui.validation import render_validation_errors
from config.theme import COLORS
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
# =====================================


def calculate_prism3(variables):
    """
    Calculate PRISM III Score
    
    Args:
        variables: dict with PRISM III variables
    
    Returns:
        dict with total score and mortality prediction
    """
    score = 0
    
    # Age component
    if variables.get('age_months', 0) < 1:
        score += variables.get('age_score', 0)
    else:
        score += variables.get('age_score', 0)
    
    # Add all component scores
    score += variables.get('systolic_bp_score', 0)
    score += variables.get('diastolic_bp_score', 0)
    score += variables.get('heart_rate_score', 0)
    score += variables.get('temperature_score', 0)
    score += variables.get('mental_status_score', 0)
    score += variables.get('pupils_score', 0)
    score += variables.get('acidosis_score', 0)
    score += variables.get('total_co2_score', 0)
    score += variables.get('pao2_score', 0)
    score += variables.get('pao2_fio2_score', 0)
    score += variables.get('glucose_score', 0)
    score += variables.get('potassium_score', 0)
    score += variables.get('creatinine_score', 0)
    score += variables.get('bun_score', 0)
    score += variables.get('wbc_score', 0)
    score += variables.get('platelets_score', 0)
    score += variables.get('pt_ptt_score', 0)
    score += variables.get('bilirubin_score', 0)
    
    # Calculate mortality risk
    # PRISM III uses complex logistic regression
    # Simplified: Logit(P) = α + β × PRISM III score
    # Approximate: Logit(P) = -6.9098 + (0.3145 × PRISM III)
    logit = -6.9098 + (0.3145 * score)
    mortality_risk = 1 / (1 + math.exp(-logit))
    mortality_percent = mortality_risk * 100
    
    return {
        "total_score": score,
        "mortality_percent": mortality_percent,
        "variables": variables
    }


def get_age_score(age_months):
    """Get age component score"""
    if age_months < 1:  # < 1 month
        return 7
    elif age_months < 12:  # 1-11 months
        return 3
    else:  # ≥ 12 months
        return 0


def get_bp_score(systolic_bp, diastolic_bp, age_months):
    """Get blood pressure scores"""
    systolic_score = 0
    diastolic_score = 0
    
    # Age-adjusted BP percentiles (simplified)
    # In practice, would use age/sex-specific charts
    
    # Systolic BP
    if systolic_bp < 50 or systolic_bp > 200:
        systolic_score = 7
    elif systolic_bp < 60 or systolic_bp > 160:
        systolic_score = 5
    elif systolic_bp < 70 or systolic_bp > 140:
        systolic_score = 2
    
    # Diastolic BP
    if diastolic_bp < 30 or diastolic_bp > 120:
        diastolic_score = 7
    elif diastolic_bp < 40 or diastolic_bp > 100:
        diastolic_score = 5
    elif diastolic_bp < 50 or diastolic_bp > 90:
        diastolic_score = 2
    
    return systolic_score, diastolic_score


def get_heart_rate_score(heart_rate, age_months):
    """Get heart rate score"""
    if heart_rate < 30 or heart_rate > 220:
        return 7
    elif heart_rate < 40 or heart_rate > 180:
        return 5
    elif heart_rate < 50 or heart_rate > 160:
        return 2
    return 0


def get_temperature_score(temp_c):
    """Get temperature score"""
    if temp_c < 30 or temp_c >= 40:
        return 7
    elif temp_c < 33 or temp_c >= 39:
        return 5
    elif temp_c < 35 or temp_c >= 38.5:
        return 2
    return 0


def get_mental_status_score(gcs, seizures):
    """Get mental status score"""
    if gcs <= 3:
        if seizures:
            return 7
        else:
            return 5
    elif gcs <= 8:
        if seizures:
            return 5
        else:
            return 3
    elif gcs <= 13:
        if seizures:
            return 3
        else:
            return 1
    return 0


def get_pupils_score(pupil_reactive):
    """Get pupils score"""
    if not pupil_reactive:
        return 7
    return 0


def get_acidosis_score(ph):
    """Get acidosis score"""
    if ph < 7.0:
        return 7
    elif ph < 7.2:
        return 5
    elif ph < 7.3:
        return 2
    return 0


def get_total_co2_score(total_co2):
    """Get total CO2 score"""
    if total_co2 < 5:
        return 7
    elif total_co2 < 10:
        return 5
    elif total_co2 < 15:
        return 2
    elif total_co2 > 50:
        return 2
    return 0


def get_pao2_score(pao2):
    """Get PaO2 score"""
    if pao2 < 40:
        return 7
    elif pao2 < 50:
        return 5
    elif pao2 < 60:
        return 2
    return 0


def get_pao2_fio2_score(pao2_fio2):
    """Get PaO2/FiO2 score"""
    if pao2_fio2 < 50:
        return 7
    elif pao2_fio2 < 100:
        return 5
    elif pao2_fio2 < 150:
        return 2
    return 0


def get_glucose_score(glucose_mgdl):
    """Get glucose score"""
    if glucose_mgdl < 40:
        return 7
    elif glucose_mgdl < 60:
        return 5
    elif glucose_mgdl > 400:
        return 5
    elif glucose_mgdl > 300:
        return 2
    return 0


def get_potassium_score(potassium):
    """Get potassium score"""
    if potassium < 2.5:
        return 7
    elif potassium < 3.0:
        return 5
    elif potassium > 6.5:
        return 7
    elif potassium > 5.5:
        return 5
    return 0


def get_creatinine_score(creatinine, age_months):
    """Get creatinine score (age-adjusted)"""
    # Age-adjusted thresholds (simplified)
    if age_months < 12:
        if creatinine >= 1.2:
            return 7
        elif creatinine >= 0.9:
            return 5
        elif creatinine >= 0.7:
            return 2
    else:
        if creatinine >= 2.0:
            return 7
        elif creatinine >= 1.5:
            return 5
        elif creatinine >= 1.2:
            return 2
    return 0


def get_bun_score(bun):
    """Get BUN score"""
    if bun >= 100:
        return 7
    elif bun >= 50:
        return 5
    elif bun >= 30:
        return 2
    return 0


def get_wbc_score(wbc):
    """Get WBC score"""
    if wbc < 1.0:
        return 7
    elif wbc < 2.5:
        return 5
    elif wbc > 40:
        return 5
    elif wbc > 30:
        return 2
    return 0


def get_platelets_score(platelets):
    """Get platelets score"""
    if platelets < 10:
        return 7
    elif platelets < 30:
        return 5
    elif platelets < 50:
        return 2
    return 0


def get_pt_ptt_score(pt_inr, ptt):
    """Get PT/PTT score"""
    max_score = 0
    
    if pt_inr >= 3.0:
        max_score = max(max_score, 7)
    elif pt_inr >= 2.0:
        max_score = max(max_score, 5)
    
    if ptt >= 100:
        max_score = max(max_score, 7)
    elif ptt >= 70:
        max_score = max(max_score, 5)
    
    return max_score


def get_bilirubin_score(bilirubin, age_months):
    """Get bilirubin score (age-adjusted)"""
    # Age-adjusted (simplified)
    if age_months < 1:
        if bilirubin >= 15:
            return 7
        elif bilirubin >= 12:
            return 5
    else:
        if bilirubin >= 10:
            return 7
        elif bilirubin >= 5:
            return 5
        elif bilirubin >= 3:
            return 2
    return 0


def render():
    """Render PRISM III Calculator"""
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'prism3':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared.get('calculator_name', 'PRISM III')}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    st.markdown(f"<h2 style='text-align: center; color: {COLORS['success']};'>🏥 PRISM III Score</h2>", unsafe_allow_html=True)
    st.caption("<p style='text-align: center;'>Pediatric Risk of Mortality - ICU Mortality Prediction</p>", unsafe_allow_html=True)
    
    st.info("""
    **PRISM III** đánh giá nguy cơ tử vong ở trẻ em ICU dựa trên:
    - Tuổi
    - Vital signs
    - Labs
    - Neurologic status
    
    **Score range:** 0-74 (càng cao = nguy cơ càng cao)
    """)
    
    st.markdown("---")
    
    # Patient info
    st.markdown("### 📋 Thông tin bệnh nhân")
    
    col1, col2 = st.columns(2)
    
    with col1:
        age_months = st.number_input(
            "Tuổi (tháng)",
            min_value=0,
            max_value=216,
            value=24,
            step=1,
            format="%d",
            key="prism3_age"
        )
    
    with col2:
        gender = st.radio(
            "Giới tính:",
            ["Nam", "Nữ"],
            horizontal=True,
            key="prism3_gender"
        )
    
    st.markdown("---")
    
    # Vital Signs
    st.markdown("### 🩺 Vital Signs")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        systolic_bp = st.number_input(
            "HA tâm thu (mmHg)",
            min_value=0,
            max_value=300,
            value=100,
            step=5,
            format="%d",
            key="prism3_sbp"
        )
        
        diastolic_bp = st.number_input(
            "HA tâm trương (mmHg)",
            min_value=0,
            max_value=200,
            value=60,
            step=5,
            format="%d",
            key="prism3_dbp"
        )
    
    with col2:
        heart_rate = st.number_input(
            "Nhịp tim (bpm)",
            min_value=0,
            max_value=300,
            value=120,
            step=5,
            format="%d",
            key="prism3_hr"
        )
        
        temperature = st.number_input(
            "Nhiệt độ (°C)",
            min_value=25.0,
            max_value=45.0,
            value=37.0,
            step=0.1,
            format="%.1f",
            key="prism3_temp"
        )
    
    with col3:
        gcs = st.number_input(
            "GCS",
            min_value=3,
            max_value=15,
            value=15,
            step=1,
            format="%d",
            key="prism3_gcs"
        )
        
        seizures = st.checkbox(
            "Có co giật",
            key="prism3_seizures"
        )
    
    with col4:
        pupil_reactive = st.checkbox(
            "Đồng tử phản xạ ánh sáng",
            value=True,
            key="prism3_pupils"
        )
    
    st.markdown("---")
    
    # Labs
    st.markdown("### 🔬 Xét nghiệm")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        ph = st.number_input(
            "pH",
            min_value=6.5,
            max_value=7.6,
            value=7.4,
            step=0.01,
            format="%.2f",
            key="prism3_ph"
        )
        
        total_co2 = st.number_input(
            "Total CO₂ (mEq/L)",
            min_value=5.0,
            max_value=60.0,
            value=25.0,
            step=1.0,
            format="%.1f",
            key="prism3_tco2"
        )
        
        pao2 = st.number_input(
            "PaO₂ (mmHg)",
            min_value=0,
            max_value=600,
            value=100,
            step=10,
            format="%d",
            key="prism3_pao2"
        )
        
        pao2_fio2 = st.number_input(
            "PaO₂/FiO₂ ratio",
            min_value=0,
            max_value=600,
            value=300,
            step=10,
            format="%d",
            key="prism3_pao2_fio2"
        )
    
    with col2:
        glucose = st.number_input(
            "Glucose (mg/dL)",
            min_value=0,
            max_value=600,
            value=100,
            step=10,
            format="%d",
            key="prism3_glucose"
        )
        
        potassium = st.number_input(
            "K⁺ (mEq/L)",
            min_value=0.0,
            max_value=10.0,
            value=4.0,
            step=0.1,
            format="%.1f",
            key="prism3_k"
        )
        
        creatinine = st.number_input(
            "Creatinine (mg/dL)",
            min_value=0.1,
            max_value=10.0,
            value=0.8,
            step=0.1,
            format="%.1f",
            key="prism3_cr"
        )
        
        bun = st.number_input(
            "BUN (mg/dL)",
            min_value=0,
            max_value=200,
            value=15,
            step=5,
            format="%d",
            key="prism3_bun"
        )
    
    with col3:
        wbc = st.number_input(
            "WBC (×10³/µL)",
            min_value=0.0,
            max_value=100.0,
            value=8.0,
            step=0.5,
            format="%.1f",
            key="prism3_wbc"
        )
        
        platelets = st.number_input(
            "Tiểu cầu (×10³/µL)",
            min_value=0,
            max_value=1000,
            value=200,
            step=10,
            format="%d",
            key="prism3_platelets"
        )
        
        pt_inr = st.number_input(
            "PT/INR",
            min_value=0.5,
            max_value=10.0,
            value=1.0,
            step=0.1,
            format="%.2f",
            key="prism3_inr"
        )
        
        ptt = st.number_input(
            "aPTT (seconds)",
            min_value=0,
            max_value=200,
            value=30,
            step=5,
            format="%d",
            key="prism3_ptt"
        )
        
        bilirubin = st.number_input(
            "Bilirubin (mg/dL)",
            min_value=0.0,
            max_value=30.0,
            value=1.0,
            step=0.5,
            format="%.1f",
            key="prism3_bili"
        )
    
    st.markdown("---")
    
    # Calculate scores
    if st.button("🧮 Tính PRISM III", type="primary", use_container_width=True):
        # Validate inputs
        validation_errors = []
        
        # Age validation (0-216 months = 0-18 years)
        is_valid_age, age_error = validate_age(age_months, 0, 216)
        if not is_valid_age:
            validation_errors.append(f"Tuổi (tháng): {age_error}")
        
        # Blood pressure validation
        is_valid_bp, bp_error = validate_blood_pressure(systolic_bp, diastolic_bp)
        if not is_valid_bp:
            validation_errors.append(f"Huyết áp: {bp_error}")
        
        # Heart rate validation
        is_valid_hr, hr_error = validate_heart_rate(heart_rate)
        if not is_valid_hr:
            validation_errors.append(f"Nhịp tim: {hr_error}")
        
        # Temperature validation
        is_valid_temp, temp_error = validate_temperature(temperature, "celsius")
        if not is_valid_temp:
            validation_errors.append(f"Nhiệt độ: {temp_error}")
        
        # GCS validation
        is_valid_gcs, gcs_error = validate_gcs(gcs)
        if not is_valid_gcs:
            validation_errors.append(f"GCS: {gcs_error}")
        
        # Lab values validation
        is_valid_ph, ph_error = validate_lab_value(ph, "pH", 6.5, 7.6)
        if not is_valid_ph:
            validation_errors.append(f"pH: {ph_error}")
        
        is_valid_tco2, tco2_error = validate_lab_value(total_co2, "Total CO₂", 5.0, 60.0)
        if not is_valid_tco2:
            validation_errors.append(f"Total CO₂: {tco2_error}")
        
        is_valid_pao2, pao2_error = validate_lab_value(pao2, "PaO₂", 0, 600)
        if not is_valid_pao2:
            validation_errors.append(f"PaO₂: {pao2_error}")
        
        is_valid_pao2_fio2, pao2_fio2_error = validate_lab_value(pao2_fio2, "PaO₂/FiO₂", 0, 600)
        if not is_valid_pao2_fio2:
            validation_errors.append(f"PaO₂/FiO₂: {pao2_fio2_error}")
        
        is_valid_glucose, glucose_error = validate_lab_value(glucose, "Glucose", 0, 600)
        if not is_valid_glucose:
            validation_errors.append(f"Glucose: {glucose_error}")
        
        is_valid_k, k_error = validate_lab_value(potassium, "K⁺", 0.0, 10.0)
        if not is_valid_k:
            validation_errors.append(f"K⁺: {k_error}")
        
        is_valid_cr, cr_error = validate_lab_value(creatinine, "Creatinine", 0.1, 10.0)
        if not is_valid_cr:
            validation_errors.append(f"Creatinine: {cr_error}")
        
        is_valid_bun, bun_error = validate_lab_value(bun, "BUN", 0, 200)
        if not is_valid_bun:
            validation_errors.append(f"BUN: {bun_error}")
        
        is_valid_wbc, wbc_error = validate_lab_value(wbc, "WBC", 0.0, 100.0)
        if not is_valid_wbc:
            validation_errors.append(f"WBC: {wbc_error}")
        
        is_valid_platelets, platelets_error = validate_lab_value(platelets, "Tiểu cầu", 0, 1000)
        if not is_valid_platelets:
            validation_errors.append(f"Tiểu cầu: {platelets_error}")
        
        is_valid_inr, inr_error = validate_lab_value(pt_inr, "PT/INR", 0.5, 10.0)
        if not is_valid_inr:
            validation_errors.append(f"PT/INR: {inr_error}")
        
        is_valid_ptt, ptt_error = validate_lab_value(ptt, "aPTT", 0, 200)
        if not is_valid_ptt:
            validation_errors.append(f"aPTT: {ptt_error}")
        
        is_valid_bili, bili_error = validate_lab_value(bilirubin, "Bilirubin", 0.0, 30.0)
        if not is_valid_bili:
            validation_errors.append(f"Bilirubin: {bili_error}")
        
        if validation_errors:
            render_validation_errors(validation_errors)
            return
        
        # Calculate component scores
        age_score = get_age_score(age_months)
        sbp_score, dbp_score = get_bp_score(systolic_bp, diastolic_bp, age_months)
        hr_score = get_heart_rate_score(heart_rate, age_months)
        temp_score = get_temperature_score(temperature)
        mental_score = get_mental_status_score(gcs, seizures)
        pupils_score = get_pupils_score(pupil_reactive)
        acidosis_score = get_acidosis_score(ph)
        tco2_score = get_total_co2_score(total_co2)
        pao2_score = get_pao2_score(pao2)
        pao2_fio2_score = get_pao2_fio2_score(pao2_fio2)
        glucose_score = get_glucose_score(glucose)
        k_score = get_potassium_score(potassium)
        cr_score = get_creatinine_score(creatinine, age_months)
        bun_score = get_bun_score(bun)
        wbc_score = get_wbc_score(wbc)
        platelets_score = get_platelets_score(platelets)
        pt_ptt_score = get_pt_ptt_score(pt_inr, ptt)
        bili_score = get_bilirubin_score(bilirubin, age_months)
        
        variables = {
            'age_months': age_months,
            'age_score': age_score,
            'systolic_bp_score': sbp_score,
            'diastolic_bp_score': dbp_score,
            'heart_rate_score': hr_score,
            'temperature_score': temp_score,
            'mental_status_score': mental_score,
            'pupils_score': pupils_score,
            'acidosis_score': acidosis_score,
            'total_co2_score': tco2_score,
            'pao2_score': pao2_score,
            'pao2_fio2_score': pao2_fio2_score,
            'glucose_score': glucose_score,
            'potassium_score': k_score,
            'creatinine_score': cr_score,
            'bun_score': bun_score,
            'wbc_score': wbc_score,
            'platelets_score': platelets_score,
            'pt_ptt_score': pt_ptt_score,
            'bilirubin_score': bili_score
        }
        
        result = calculate_prism3(variables)
        
        if result['total_score'] <= 10:
            interpretation = "Nguy cơ thấp"
            color = COLORS["success"]
            icon = "✅"
            prognosis = "Tiên lượng tốt"
        elif result['total_score'] <= 20:
            interpretation = "Nguy cơ trung bình"
            color = COLORS["info"]
            icon = "⚠️"
            prognosis = "Theo dõi sát, điều trị tích cực"
        elif result['total_score'] <= 30:
            interpretation = "Nguy cơ cao"
            color = COLORS["warning"]
            icon = "🚨"
            prognosis = "Điều trị tối đa, tiên lượng dè dặt"
        else:
            interpretation = "Nguy cơ rất cao"
            color = COLORS["error"]
            icon = "🆘"
            prognosis = "Tiên lượng xấu, điều trị hỗ trợ tối đa"

        render_score_result(
            title="PRISM III Score",
            score=result['total_score'],
            interpretation=interpretation,
            mortality=f"Tử vong: {result['mortality_percent']:.1f}%",
            color=color,
            icon=icon,
            size="large",
            max_score=74
        )
        
        st.info(f"💡 **Tiên lượng:** {prognosis}")
        
        # Prepare data for history and share
        inputs_dict = {
            "Tuổi (tháng)": age_months,
            "Giới tính": gender,
            "HA tâm thu (mmHg)": systolic_bp,
            "HA tâm trương (mmHg)": diastolic_bp,
            "Nhịp tim (bpm)": heart_rate,
            "Nhiệt độ (°C)": temperature,
            "GCS": gcs,
            "Pupils": pupils,
            "pH": ph if 'ph' in locals() else None,
            "PaO2 (mmHg)": pao2 if 'pao2' in locals() else None,
            "FIO2": fio2 if 'fio2' in locals() else None,
            "Glucose (mg/dL)": glucose if 'glucose' in locals() else None,
            "K+ (mEq/L)": potassium if 'potassium' in locals() else None,
            "Creatinine (mg/dL)": creatinine if 'creatinine' in locals() else None,
            "BUN (mg/dL)": bun if 'bun' in locals() else None,
            "WBC (×10³/µL)": wbc if 'wbc' in locals() else None,
            "Tiểu cầu (×10³/µL)": platelets if 'platelets' in locals() else None,
            "Bilirubin (mg/dL)": bilirubin if 'bilirubin' in locals() else None
        }
        
        results_dict = {
            "PRISM III Score": f"{result['total_score']}/74",
            "Nguy cơ tử vong": f"{result['mortality_percent']:.1f}%"
        }
        
        # Export section
        from components.export import render_export_section
        render_export_section(
                title="PRISM III",
                inputs=inputs_dict,
                results=results_dict
        ,
                calculator_name="PRISM III"
            )
        
        # Save to history
        save_calculation_to_history(
            calculator_id="prism3",
            calculator_name="PRISM III",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Share section
        render_share_section(
            calculator_id="prism3",
            calculator_name="PRISM III",
            inputs=inputs_dict,
            results=results_dict,
            show_qr=True
        )
        
        # History section
        render_history_ui(calculator_id="prism3", show_actions=True)
    
    # Smart Suggestions
    col_main, col_suggestions = st.columns([2, 1])
    with col_suggestions:
        render_suggestions(
            calculator_id="prism3",
            calculator_name="PRISM III",
            category="Nhi Khoa",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    # References section (always at bottom)
    st.markdown("---")
    references = get_references("PRISM III")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            show_evidence_level=True,
            show_links=True
        )
    else:
        with st.expander("📚 Tài liệu tham khảo"):
            st.markdown("""
            **Pollack MM, et al. The Pediatric Risk of Mortality (PRISM) III Score System.**
            *Pediatr Crit Care Med.* 2016;17(7):671-680.
            
            **PRISM III Variables:**
            - Age
            - Vital signs (BP, HR, Temperature)
            - Neurologic (GCS, seizures, pupils)
            - Blood gas (pH, CO₂, PaO₂, PaO₂/FiO₂)
            - Metabolic (Glucose, K⁺, Creatinine, BUN)
            - Hematologic (WBC, Platelets, PT/PTT)
            - Hepatic (Bilirubin)
            
            **Score Range:** 0-74
            **Mortality Risk:** Calculated using logistic regression
            """)

