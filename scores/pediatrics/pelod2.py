"""
PELOD-2 - Pediatric Logistic Organ Dysfunction Score
ICU severity score for pediatric patients
Mortality prediction based on organ dysfunction

Reference:
Leteurtre S, et al. PELOD-2: an update of the PEdiatric logistic organ dysfunction score.
Crit Care Med. 2013;41(7):1761-1773.
"""

import streamlit as st
import math
from scores.utils.validation import (
    validate_age,
    validate_blood_pressure,
    validate_heart_rate,
    validate_gcs,
    validate_lab_value,
    validate_range,
    validate_positive
)
from components.ui.validation import render_validation_errors
from config.theme import COLORS
from components.ui.scoring import render_score_result
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
# =====================================


def calculate_pelod2(
    neurologic_score=0,
    cardiovascular_score=0,
    renal_score=0,
    respiratory_score=0,
    hematologic_score=0,
    hepatic_score=0
):
    """
    Calculate PELOD-2 Score
    
    Args:
        neurologic_score: 0, 4, or 10 points
        cardiovascular_score: 0, 3, 8, or 13 points
        renal_score: 0, 4, or 9 points
        respiratory_score: 0, 1, or 5 points
        hematologic_score: 0 or 2 points
        hepatic_score: 0, 4, or 9 points
    
    Returns:
        dict with total score and mortality prediction
    """
    total_score = (
        neurologic_score +
        cardiovascular_score +
        renal_score +
        respiratory_score +
        hematologic_score +
        hepatic_score
    )
    
    # Calculate mortality risk using PELOD-2 formula
    # Logit(P) = -7.6687 + (0.1559 × PELOD-2 score)
    logit = -7.6687 + (0.1559 * total_score)
    mortality_risk = 1 / (1 + math.exp(-logit))  # Logistic function
    mortality_percent = mortality_risk * 100
    
    return {
        "total_score": total_score,
        "neurologic_score": neurologic_score,
        "cardiovascular_score": cardiovascular_score,
        "renal_score": renal_score,
        "respiratory_score": respiratory_score,
        "hematologic_score": hematologic_score,
        "hepatic_score": hepatic_score,
        "mortality_percent": mortality_percent
    }


def get_neurologic_score(gcs, seizures):
    """Get neurologic score component"""
    if gcs >= 13:
        return 0
    elif gcs >= 11:
        return 4
    else:  # GCS < 11
        if seizures:
            return 10
        else:
            return 10


def get_cardiovascular_score(heart_rate_percentile, systolic_bp_percentile, lactate, vasoactive_drugs):
    """Get cardiovascular score component"""
    max_score = 0
    
    # Heart rate percentile
    if heart_rate_percentile > 95 or heart_rate_percentile < 5:
        max_score = max(max_score, 3)
    
    # Systolic BP percentile
    if systolic_bp_percentile < 5:
        max_score = max(max_score, 8)
    
    # Lactate
    if lactate >= 5:
        max_score = max(max_score, 8)
    
    # Vasoactive drugs
    if vasoactive_drugs >= 2:
        max_score = max(max_score, 13)
    elif vasoactive_drugs == 1:
        max_score = max(max_score, 8)
    
    return max_score


def get_renal_score(creatinine, creatinine_percentile):
    """Get renal score component"""
    max_score = 0
    
    # Creatinine absolute
    if creatinine >= 2:
        max_score = max(max_score, 9)
    elif creatinine >= 1.2:
        max_score = max(max_score, 4)
    
    # Creatinine percentile
    if creatinine_percentile > 97:
        max_score = max(max_score, 9)
    
    return max_score


def get_respiratory_score(pao2_fio2_ratio, intubated):
    """Get respiratory score component"""
    if intubated:
        if pao2_fio2_ratio < 100:
            return 5
        elif pao2_fio2_ratio < 200:
            return 1
        else:
            return 0
    else:
        if pao2_fio2_ratio < 200:
            return 1
        else:
            return 0


def get_hematologic_score(platelets, wbc, d_dimer):
    """Get hematologic score component"""
    if platelets < 50 or wbc < 2.5 or d_dimer >= 2:
        return 2
    return 0


def get_hepatic_score(bilirubin, pt_inr):
    """Get hepatic score component"""
    max_score = 0
    
    if bilirubin >= 4:
        max_score = max(max_score, 9)
    elif bilirubin >= 2:
        max_score = max(max_score, 4)
    
    if pt_inr >= 2:
        max_score = max(max_score, 9)
    elif pt_inr >= 1.5:
        max_score = max(max_score, 4)
    
    return max_score


def render():
    """Render PELOD-2 Calculator"""
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'pelod2':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared.get('calculator_name', 'PELOD-2')}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    st.markdown(f"<h2 style='text-align: center; color: {COLORS['success']};'>🏥 PELOD-2 Score</h2>", unsafe_allow_html=True)
    st.caption("<p style='text-align: center;'>Pediatric Logistic Organ Dysfunction Score - ICU Mortality Prediction</p>", unsafe_allow_html=True)
    
    st.info("""
    **PELOD-2** đánh giá mức độ suy đa cơ quan ở trẻ em ICU và dự đoán nguy cơ tử vong.
    
    **6 Hệ thống cơ quan:**
    - Thần kinh (Neurologic)
    - Tim mạch (Cardiovascular)
    - Thận (Renal)
    - Hô hấp (Respiratory)
    - Huyết học (Hematologic)
    - Gan (Hepatic)
    
    **Điểm số:** 0-33 (càng cao = càng nặng)
    """)
    
    st.markdown("---")
    
    # Input section
    col_main, col_suggestions = st.columns([2, 1])
    
    with col_suggestions:
        # Smart Suggestions
        render_suggestions(
            calculator_id="pelod2",
            calculator_name="PELOD-2",
            category="Nhi Khoa",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    with col_main:
        st.markdown("### 📋 Thông tin bệnh nhân")
    
    col1, col2 = st.columns(2)
    
    with col1:
        age_months = st.number_input(
            "Tuổi (tháng)",
            min_value=0,
            max_value=216,  # 18 years
            value=60,
            step=1,
            key="pelod2_age"
        )
        
        weight_kg = st.number_input(
            "Cân nặng (kg)",
            min_value=0.5,
            max_value=100.0,
            value=20.0,
            step=0.5,
            format="%.1f",
            key="pelod2_weight"
        )
    
    st.markdown("---")
    
    # Neurologic
    st.markdown("### 🧠 Thần kinh (Neurologic)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        gcs = st.number_input(
            "Thang điểm hôn mê Glasgow (GCS) - Thang điểm hôn mê Glasgow",
            min_value=3,
            max_value=15,
            value=15,
            step=1,
            key="pelod2_gcs"
        )
    
    with col2:
        seizures = st.checkbox(
            "Có co giật",
            key="pelod2_seizures"
        )
    
    neurologic_score = get_neurologic_score(gcs, seizures)
    
    st.info(f"**Điểm Thần kinh:** {neurologic_score} điểm")
    
    st.markdown("---")
    
    # Cardiovascular
    st.markdown("### ❤️ Tim mạch (Cardiovascular)")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        heart_rate = st.number_input(
            "Nhịp tim (bpm)",
            min_value=0,
            max_value=300,
            value=100,
            step=5,
            key="pelod2_hr"
        )
    
    with col2:
        systolic_bp = st.number_input(
            "HA tâm thu (mmHg)",
            min_value=0,
            max_value=200,
            value=100,
            step=5,
            key="pelod2_sbp"
        )
    
    with col3:
        lactate = st.number_input(
            "Lactate (mmol/L)",
            min_value=0.0,
            max_value=20.0,
            value=1.0,
            step=0.5,
            format="%.1f",
            key="pelod2_lactate"
        )
    
    with col4:
        vasoactive_drugs = st.number_input(
            "Số thuốc vận mạch",
            min_value=0,
            max_value=5,
            value=0,
            step=1,
            key="pelod2_vasoactive",
            help="Số loại thuốc vận mạch đang dùng (Dopamine, Norepinephrine, Epinephrine, etc.)"
        )
    
    # Simplified percentile calculation (would need age/sex-specific charts in real app)
    hr_percentile = 50  # Placeholder - would calculate from age/sex
    sbp_percentile = 50  # Placeholder
    
    cardiovascular_score = get_cardiovascular_score(hr_percentile, sbp_percentile, lactate, vasoactive_drugs)
    
    st.info(f"**Điểm Tim mạch:** {cardiovascular_score} điểm")
    
    st.markdown("---")
    
    # Renal
    st.markdown("### 🧪 Thận (Renal)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        creatinine = st.number_input(
            "Creatinine (mg/dL)",
            min_value=0.1,
            max_value=10.0,
            value=0.8,
            step=0.1,
            format="%.1f",
            key="pelod2_cr"
        )
    
    with col2:
        creatinine_percentile = st.number_input(
            "Creatinine percentile",
            min_value=0,
            max_value=100,
            value=50,
            step=5,
            key="pelod2_cr_percentile",
            help="Percentile của creatinine theo tuổi/giới"
        )
    
    renal_score = get_renal_score(creatinine, creatinine_percentile)
    
    st.info(f"**Điểm Thận:** {renal_score} điểm")
    
    st.markdown("---")
    
    # Respiratory
    st.markdown("### 🫁 Hô hấp (Respiratory)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        pao2_fio2 = st.number_input(
            "PaO₂/FiO₂ ratio",
            min_value=0,
            max_value=600,
            value=300,
            step=10,
            key="pelod2_pao2_fio2"
        )
    
    with col2:
        intubated = st.checkbox(
            "Đang thở máy",
            key="pelod2_intubated"
        )
    
    respiratory_score = get_respiratory_score(pao2_fio2, intubated)
    
    st.info(f"**Điểm Hô hấp:** {respiratory_score} điểm")
    
    st.markdown("---")
    
    # Hematologic
    st.markdown("### 🩸 Huyết học (Hematologic)")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        platelets = st.number_input(
            "Tiểu cầu (×10³/µL)",
            min_value=0,
            max_value=1000,
            value=200,
            step=10,
            key="pelod2_platelets"
        )
    
    with col2:
        wbc = st.number_input(
            "Bạch cầu (×10³/µL)",
            min_value=0.0,
            max_value=50.0,
            value=8.0,
            step=0.5,
            format="%.1f",
            key="pelod2_wbc"
        )
    
    with col3:
        d_dimer = st.number_input(
            "D-dimer (mg/L)",
            min_value=0.0,
            max_value=10.0,
            value=0.5,
            step=0.1,
            format="%.1f",
            key="pelod2_ddimer"
        )
    
    hematologic_score = get_hematologic_score(platelets, wbc, d_dimer)
    
    st.info(f"**Điểm Huyết học:** {hematologic_score} điểm")
    
    st.markdown("---")
    
    # Hepatic
    st.markdown("### 🫀 Gan (Hepatic)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        bilirubin = st.number_input(
            "Bilirubin (mg/dL)",
            min_value=0.0,
            max_value=30.0,
            value=1.0,
            step=0.5,
            format="%.1f",
            key="pelod2_bili"
        )
    
    with col2:
        pt_inr = st.number_input(
            "PT/INR",
            min_value=0.5,
            max_value=10.0,
            value=1.0,
            step=0.1,
            format="%.2f",
            key="pelod2_inr"
        )
    
    hepatic_score = get_hepatic_score(bilirubin, pt_inr)
    
    st.info(f"**Điểm Gan:** {hepatic_score} điểm")
    
    st.markdown("---")
    
    # Calculate score
    if st.button("🧮 Tính PELOD-2", type="primary", use_container_width=True):
        # Validate inputs
        validation_errors = []
        
        # Age validation (0-216 months = 0-18 years)
        is_valid_age, age_error = validate_age(age_months, 0, 216)
        if not is_valid_age:
            validation_errors.append(f"Tuổi (tháng): {age_error}")
        
        # Weight validation
        is_valid_weight, weight_error = validate_positive(weight_kg, "Cân nặng")
        if not is_valid_weight:
            validation_errors.append(f"Cân nặng: {weight_error}")
        elif weight_kg < 0.5:
            validation_errors.append("Cân nặng phải ≥ 0.5 kg")
        elif weight_kg > 100.0:
            validation_errors.append("Cân nặng phải ≤ 100 kg (kiểm tra lại)")
        
        # GCS validation
        is_valid_gcs, gcs_error = validate_gcs(gcs)
        if not is_valid_gcs:
            validation_errors.append(f"GCS: {gcs_error}")
        
        # Heart rate validation
        is_valid_hr, hr_error = validate_heart_rate(heart_rate)
        if not is_valid_hr:
            validation_errors.append(f"Nhịp tim: {hr_error}")
        
        # SBP validation
        is_valid_sbp, sbp_error = validate_blood_pressure(systolic_bp)
        if not is_valid_sbp:
            validation_errors.append(f"Huyết áp tâm thu: {sbp_error}")
        
        # Lactate validation
        is_valid_lactate, lactate_error = validate_lab_value(lactate, "Lactate", 0.0, 20.0)
        if not is_valid_lactate:
            validation_errors.append(f"Lactate: {lactate_error}")
        
        # Vasoactive drugs validation
        is_valid_vaso, vaso_error = validate_range(vasoactive_drugs, 0, 5, "Số thuốc vận mạch")
        if not is_valid_vaso:
            validation_errors.append(f"Số thuốc vận mạch: {vaso_error}")
        
        # Creatinine validation
        is_valid_cr, cr_error = validate_lab_value(creatinine, "Creatinine", 0.1, 10.0)
        if not is_valid_cr:
            validation_errors.append(f"Creatinine: {cr_error}")
        
        # Creatinine percentile validation
        is_valid_cr_percentile, cr_percentile_error = validate_range(creatinine_percentile, 0, 100, "Creatinine percentile")
        if not is_valid_cr_percentile:
            validation_errors.append(f"Creatinine percentile: {cr_percentile_error}")
        
        # PaO2/FiO2 validation
        is_valid_pao2_fio2, pao2_fio2_error = validate_lab_value(pao2_fio2, "PaO₂/FiO₂", 0, 600)
        if not is_valid_pao2_fio2:
            validation_errors.append(f"PaO₂/FiO₂: {pao2_fio2_error}")
        
        # Platelets validation
        is_valid_platelets, platelets_error = validate_lab_value(platelets, "Tiểu cầu", 0, 1000)
        if not is_valid_platelets:
            validation_errors.append(f"Tiểu cầu: {platelets_error}")
        
        # WBC validation
        is_valid_wbc, wbc_error = validate_lab_value(wbc, "Bạch cầu", 0.0, 50.0)
        if not is_valid_wbc:
            validation_errors.append(f"Bạch cầu: {wbc_error}")
        
        # D-dimer validation
        is_valid_ddimer, ddimer_error = validate_lab_value(d_dimer, "D-dimer", 0.0, 10.0)
        if not is_valid_ddimer:
            validation_errors.append(f"D-dimer: {ddimer_error}")
        
        # Bilirubin validation
        is_valid_bili, bili_error = validate_lab_value(bilirubin, "Bilirubin", 0.0, 30.0)
        if not is_valid_bili:
            validation_errors.append(f"Bilirubin: {bili_error}")
        
        # PT/INR validation
        is_valid_inr, inr_error = validate_lab_value(pt_inr, "PT/INR", 0.5, 10.0)
        if not is_valid_inr:
            validation_errors.append(f"PT/INR: {inr_error}")
        
        if validation_errors:
            render_validation_errors(validation_errors)
            return
        
        result = calculate_pelod2(
            neurologic_score,
            cardiovascular_score,
            renal_score,
            respiratory_score,
            hematologic_score,
            hepatic_score
        )
        
        st.markdown("### 📊 Kết quả PELOD-2")
        
        # Determine color and interpretation
        if result['total_score'] == 0:
            interpretation = "Không có suy đa cơ quan"
            color = COLORS["success"]
            icon = "✅"
        elif result['total_score'] <= 5:
            interpretation = "Suy đa cơ quan nhẹ"
            color = COLORS["info"]
            icon = "⚠️"
        elif result['total_score'] <= 15:
            interpretation = "Suy đa cơ quan trung bình-nặng"
            color = COLORS["warning"]
            icon = "🚨"
        else:
            interpretation = "Suy đa cơ quan rất nặng"
            color = COLORS["error"]
            icon = "🆘"

        render_score_result(
            title="PELOD-2 Score",
            score=result['total_score'],
            interpretation=interpretation,
            mortality=f"Tử vong: {result['mortality_percent']:.1f}%",
            color=color,
            icon=icon,
            size="large",
            max_score=33
        )
        
        # Prepare data for history and share
        inputs_dict = {
            "Tuổi (tháng)": age_months,
            "Cân nặng (kg)": weight_kg,
            "GCS": gcs,
            "Co giật": "Có" if seizures else "Không",
            "Nhịp tim (bpm)": heart_rate,
            "HA tâm thu (mmHg)": systolic_bp,
            "Lactate (mmol/L)": lactate,
            "Số thuốc vận mạch": vasoactive_drugs,
            "Creatinine (mg/dL)": creatinine,
            "Creatinine percentile": creatinine_percentile,
            "PaO2/FiO2 ratio": pao2_fio2,
            "Đang thở máy": "Có" if intubated else "Không",
            "Tiểu cầu (×10³/µL)": platelets,
            "Bạch cầu (×10³/µL)": wbc,
            "D-dimer (mg/L)": d_dimer,
            "Bilirubin (mg/dL)": bilirubin,
            "PT/INR": pt_inr
        }
        
        results_dict = {
            "PELOD-2 Score": f"{result['total_score']}/33",
            "Nguy cơ tử vong": f"{result['mortality_percent']:.1f}%",
            "Điểm Thần kinh": result['neurologic_score'],
            "Điểm Tim mạch": result['cardiovascular_score'],
            "Điểm Thận": result['renal_score'],
            "Điểm Hô hấp": result['respiratory_score'],
            "Điểm Huyết học": result['hematologic_score'],
            "Điểm Gan": result['hepatic_score']
        }
        
        # Export section
        from components.export import render_export_section
        render_export_section(
                title="PELOD-2",
                inputs=inputs_dict,
                results=results_dict
        ,
                calculator_name="PELOD-2"
            )
        
        # Save to history
        save_calculation_to_history(
            calculator_id="pelod2",
            calculator_name="PELOD-2",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Share section
        render_share_section(
            calculator_id="pelod2",
            calculator_name="PELOD-2",
            inputs=inputs_dict,
            results=results_dict,
            show_qr=True
        )
        
        # History section
        render_history_ui(calculator_id="pelod2", show_actions=True)
    
    # References section (always at bottom)
    st.markdown("---")
    references = get_references("PELOD-2")
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
            **Leteurtre S, et al. PELOD-2: an update of the PEdiatric logistic organ dysfunction score.**
            *Crit Care Med.* 2013;41(7):1761-1773.
            
            **PELOD-2 Components:**
            - **Neurologic:** GCS (0, 4, 10 points)
            - **Cardiovascular:** HR percentile, SBP percentile, lactate, vasoactive drugs (0, 3, 8, 13 points)
            - **Renal:** Creatinine absolute và percentile (0, 4, 9 points)
            - **Respiratory:** PaO₂/FiO₂ ratio, intubation status (0, 1, 5 points)
            - **Hematologic:** Platelets, WBC, D-dimer (0, 2 points)
            - **Hepatic:** Bilirubin, PT/INR (0, 4, 9 points)
            
            **Mortality Prediction:**
            - Logit(P) = -7.6687 + (0.1559 × PELOD-2 score)
            - P = 1 / (1 + exp(-Logit))
            """)

