"""
PRISM III - Pediatric Risk of Mortality Score
ICU mortality prediction for pediatric patients

Reference:
Pollack MM, et al. The Pediatric Risk of Mortality (PRISM) III Score System.
Pediatr Crit Care Med. 2016;17(7):671-680.
"""

import streamlit as st
import math


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
    
    st.subheader("🏥 PRISM III Score")
    st.caption("Pediatric Risk of Mortality - ICU Mortality Prediction")
    
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
            key="prism3_sbp"
        )
        
        diastolic_bp = st.number_input(
            "HA tâm trương (mmHg)",
            min_value=0,
            max_value=200,
            value=60,
            step=5,
            key="prism3_dbp"
        )
    
    with col2:
        heart_rate = st.number_input(
            "Nhịp tim (bpm)",
            min_value=0,
            max_value=300,
            value=120,
            step=5,
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
            key="prism3_pao2"
        )
        
        pao2_fio2 = st.number_input(
            "PaO₂/FiO₂ ratio",
            min_value=0,
            max_value=600,
            value=300,
            step=10,
            key="prism3_pao2_fio2"
        )
    
    with col2:
        glucose = st.number_input(
            "Glucose (mg/dL)",
            min_value=0,
            max_value=600,
            value=100,
            step=10,
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
        
        st.markdown("### 📊 Kết quả PRISM III")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric(
                "PRISM III Score",
                f"{result['total_score']}/74"
            )
        
        with col2:
            st.metric(
                "Nguy cơ tử vong",
                f"{result['mortality_percent']:.1f}%"
            )
        
        st.markdown("---")
        
        # Interpretation
        if result['total_score'] <= 10:
            st.success(f"""
            **✅ Nguy cơ thấp**
            
            - PRISM III = {result['total_score']}
            - Nguy cơ tử vong: {result['mortality_percent']:.1f}%
            - Tiên lượng tốt
            """)
        elif result['total_score'] <= 20:
            st.info(f"""
            **⚠️ Nguy cơ trung bình**
            
            - PRISM III = {result['total_score']}
            - Nguy cơ tử vong: {result['mortality_percent']:.1f}%
            - Theo dõi sát, điều trị tích cực
            """)
        elif result['total_score'] <= 30:
            st.warning(f"""
            **🚨 Nguy cơ cao**
            
            - PRISM III = {result['total_score']}
            - Nguy cơ tử vong: {result['mortality_percent']:.1f}%
            - Điều trị tối đa, tiên lượng dè dặt
            """)
        else:
            st.error(f"""
            **🚨🚨 Nguy cơ rất cao**
            
            - PRISM III = {result['total_score']}
            - Nguy cơ tử vong: {result['mortality_percent']:.1f}%
            - Tiên lượng xấu, điều trị hỗ trợ tối đa
            """)
    
    st.markdown("---")
    
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

