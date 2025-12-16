"""
LODS - Logistic Organ Dysfunction Score
=======================================

Organ dysfunction assessment in ICU

Reference:
- Le Gall JR, et al. A new Simplified Acute Physiology Score (SAPS II) based on a
  European/North American multicenter study. JAMA. 1993;270(24):2957-2963.
- Le Gall JR, et al. The Logistic Organ Dysfunction system. A new way to assess 
  organ dysfunction in the intensive care unit. JAMA. 1996;276(10):802-810.

LODS Components:
- 6 organ systems
- Each system: 0-5 points
- Total: 0-22 points

Organ Systems:
1. Neurological (GCS)
2. Cardiovascular (Heart rate, SBP)
3. Renal (Creatinine, Urine output)
4. Pulmonary (PaO2/FiO2)
5. Hematological (Platelets, WBC)
6. Hepatic (Bilirubin, Prothrombin time)

Clinical Utility:
- Organ dysfunction assessment
- ICU mortality prediction
- Research and quality improvement
"""

import streamlit as st
import math
from components.ui.results import render_result_box
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
# ======================================
from scores.utils.validation import (
    validate_gcs,
    validate_blood_pressure,
    validate_heart_rate,
    validate_lab_value,
    safe_divide
)


def get_lods_neuro_points(gcs: int) -> int:
    """Neurological points (GCS)"""
    if gcs >= 15:
        return 0
    elif gcs >= 13:
        return 1
    elif gcs >= 10:
        return 2
    elif gcs >= 6:
        return 3
    elif gcs >= 4:
        return 4
    else:
        return 5


def get_lods_cv_points(hr: float, sbp: float) -> int:
    """Cardiovascular points"""
    # Check for tachycardia or bradycardia
    hr_points = 0
    if hr < 40 or hr > 150:
        hr_points = 1
    
    # Check for hypotension
    sbp_points = 0
    if sbp < 70:
        sbp_points = 2
    elif sbp < 100:
        sbp_points = 1
    
    return max(hr_points, sbp_points)


def get_lods_renal_points(cr: float, urine_output: float) -> int:
    """Renal points"""
    # Creatinine points
    cr_points = 0
    if cr >= 5.0:
        cr_points = 5
    elif cr >= 3.5:
        cr_points = 3
    elif cr >= 2.0:
        cr_points = 1
    
    # Urine output points
    uo_points = 0
    if urine_output < 0.5:
        uo_points = 3
    elif urine_output < 1.0:
        uo_points = 1
    
    return max(cr_points, uo_points)


def get_lods_pulmonary_points(pao2: float, fio2: float, is_ventilated: bool) -> int:
    """Pulmonary points"""
    if not is_ventilated:
        return 0
    
    if fio2 == 0:
        return 0
    
    ratio = (pao2 / fio2) * 100
    
    if ratio < 100:
        return 5
    elif ratio < 200:
        return 3
    elif ratio < 300:
        return 1
    else:
        return 0


def get_lods_hematological_points(platelets: float, wbc: float) -> int:
    """Hematological points"""
    # Platelet points
    plt_points = 0
    if platelets < 50:
        plt_points = 3
    elif platelets < 100:
        plt_points = 1
    
    # WBC points
    wbc_points = 0
    if wbc < 1.0 or wbc > 50.0:
        wbc_points = 1
    
    return max(plt_points, wbc_points)


def get_lods_hepatic_points(bilirubin: float, pt: float) -> int:
    """Hepatic points"""
    # Bilirubin points
    bil_points = 0
    if bilirubin >= 6.0:
        bil_points = 3
    elif bilirubin >= 2.0:
        bil_points = 1
    
    # PT points
    pt_points = 0
    if pt >= 1.5:  # PT ratio >= 1.5
        pt_points = 2
    elif pt >= 1.25:
        pt_points = 1
    
    return max(bil_points, pt_points)


def calculate_lods(params: dict) -> dict:
    """
    Calculate LODS score
    
    Args:
        params: Dictionary with patient parameters
        
    Returns:
        Dictionary with score and interpretation
    """
    total_score = 0
    details = []
    
    # Neurological
    neuro_points = get_lods_neuro_points(params['gcs'])
    total_score += neuro_points
    details.append(f"Thần kinh (GCS {params['gcs']}): {neuro_points} điểm")
    
    # Cardiovascular
    cv_points = get_lods_cv_points(params['hr'], params['sbp'])
    total_score += cv_points
    details.append(f"Tim mạch (HR {params['hr']:.0f}, SBP {params['sbp']:.0f}): {cv_points} điểm")
    
    # Renal
    renal_points = get_lods_renal_points(params['creatinine'], params['urine_output'])
    total_score += renal_points
    details.append(f"Thận (Cr {params['creatinine']:.1f}, UO {params['urine_output']:.1f}): {renal_points} điểm")
    
    # Pulmonary
    if params.get('is_ventilated', False):
        pulm_points = get_lods_pulmonary_points(
            params['pao2'], params['fio2'], params['is_ventilated']
        )
        total_score += pulm_points
        ratio = (params['pao2'] / params['fio2']) * 100 if params['fio2'] > 0 else 0
        details.append(f"Hô hấp (PaO2/FiO2 {ratio:.0f}): {pulm_points} điểm")
    else:
        details.append(f"Hô hấp (không thở máy): 0 điểm")
    
    # Hematological
    heme_points = get_lods_hematological_points(params['platelets'], params['wbc'])
    total_score += heme_points
    details.append(f"Huyết học (PLT {params['platelets']:.0f}, WBC {params['wbc']:.1f}): {heme_points} điểm")
    
    # Hepatic
    hepatic_points = get_lods_hepatic_points(params['bilirubin'], params['pt'])
    total_score += hepatic_points
    details.append(f"Gan (Bilirubin {params['bilirubin']:.1f}, PT {params['pt']:.2f}): {hepatic_points} điểm")
    
    # Interpretation
    if total_score <= 5:
        interpretation = "Suy cơ quan nhẹ"
        severity = "Nhẹ"
        color = "success"
    elif total_score <= 10:
        interpretation = "Suy cơ quan trung bình"
        severity = "Trung bình"
        color = "warning"
    else:
        interpretation = "Suy cơ quan nặng"
        severity = "Nặng"
        color = "error"
    
    return {
        "total_score": total_score,
        "interpretation": interpretation,
        "severity": severity,
        "color": color,
        "details": details,
        "organ_scores": {
            "neurological": neuro_points,
            "cardiovascular": cv_points,
            "renal": renal_points,
            "pulmonary": pulm_points if params.get('is_ventilated', False) else 0,
            "hematological": heme_points,
            "hepatic": hepatic_points
        }
    }


def render():
    """LODS Score Calculator"""
    st.subheader("🚨 LODS - Logistic Organ Dysfunction Score")
    st.caption("Đánh giá suy cơ quan trong ICU")
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'lods':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    # Smart Suggestions (sidebar)
    with st.sidebar:
        render_suggestions(
            calculator_id="lods",
            calculator_name="LODS Score",
            category="Cấp cứu",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    st.markdown("""
    **LODS (Logistic Organ Dysfunction Score)** đánh giá mức độ suy cơ quan trong ICU.
    
    **6 hệ cơ quan (mỗi hệ 0-5 điểm):**
    1. **Thần kinh** (GCS)
    2. **Tim mạch** (HR, SBP)
    3. **Thận** (Creatinine, Urine output)
    4. **Hô hấp** (PaO2/FiO2)
    5. **Huyết học** (Platelets, WBC)
    6. **Gan** (Bilirubin, PT)
    
    **Tổng điểm:** 0-22
    """)
    
    st.markdown("---")
    
    # Input section
    st.markdown("### 📝 Thông tin bệnh nhân")
    
    col1, col2 = st.columns(2)
    
    with col1:
        gcs = st.number_input(
            "GCS (3-15):",
            min_value=3,
            max_value=15,
            value=15,
            step=1,
            key="lods_gcs"
        )
        
        hr = st.number_input(
            "Nhịp tim (/phút):",
            min_value=0.0,
            max_value=250.0,
            value=80.0,
            step=1.0,
            key="lods_hr"
        )
        
        sbp = st.number_input(
            "Huyết áp tâm thu (mmHg):",
            min_value=0.0,
            max_value=300.0,
            value=120.0,
            step=1.0,
            key="lods_sbp"
        )
        
        creatinine = st.number_input(
            "Creatinine (mg/dL):",
            min_value=0.0,
            max_value=20.0,
            value=1.0,
            step=0.1,
            key="lods_cr"
        )
        
        urine_output = st.number_input(
            "Lượng nước tiểu (L/ngày):",
            min_value=0.0,
            max_value=10.0,
            value=1.5,
            step=0.1,
            key="lods_uo"
        )
    
    with col2:
        is_ventilated = st.checkbox(
            "Đang thở máy",
            key="lods_ventilated"
        )
        
        if is_ventilated:
            pao2 = st.number_input(
                "PaO₂ (mmHg):",
                min_value=0.0,
                max_value=600.0,
                value=100.0,
                step=1.0,
                key="lods_pao2"
            )
            fio2 = st.number_input(
                "FiO₂ (0.21-1.0):",
                min_value=0.21,
                max_value=1.0,
                value=0.4,
                step=0.01,
                key="lods_fio2"
            )
        else:
            pao2 = 0
            fio2 = 0.21
        
        platelets = st.number_input(
            "Platelets (×10³/µL):",
            min_value=0.0,
            max_value=1000.0,
            value=200.0,
            step=10.0,
            key="lods_plt"
        )
        
        wbc = st.number_input(
            "WBC (×10³/µL):",
            min_value=0.0,
            max_value=100.0,
            value=7.0,
            step=0.1,
            key="lods_wbc"
        )
        
        bilirubin = st.number_input(
            "Bilirubin (mg/dL):",
            min_value=0.0,
            max_value=50.0,
            value=1.0,
            step=0.1,
            key="lods_bilirubin"
        )
        
        pt = st.number_input(
            "PT Ratio (INR tương đương):",
            min_value=0.5,
            max_value=5.0,
            value=1.0,
            step=0.01,
            key="lods_pt"
        )
    
    st.markdown("---")
    
    if st.button("🧮 Tính LODS", type="primary", use_container_width=True):
        # Validate inputs
        validation_errors = []
        
        is_valid_gcs, gcs_error = validate_gcs(gcs)
        if not is_valid_gcs:
            validation_errors.append(gcs_error)
        
        is_valid_sbp, sbp_error = validate_blood_pressure(sbp)
        if not is_valid_sbp:
            validation_errors.append(sbp_error)
        
        is_valid_hr, hr_error = validate_heart_rate(hr)
        if not is_valid_hr:
            validation_errors.append(hr_error)
        
        is_valid_cr, cr_error = validate_lab_value(creatinine, "Creatinine", 0, 20)
        if not is_valid_cr:
            validation_errors.append(cr_error)
        
        is_valid_platelets, platelets_error = validate_lab_value(platelets, "Platelets", 0, 1000)
        if not is_valid_platelets:
            validation_errors.append(platelets_error)
        
        is_valid_wbc, wbc_error = validate_lab_value(wbc, "WBC", 0, 100)
        if not is_valid_wbc:
            validation_errors.append(wbc_error)
        
        is_valid_bilirubin, bilirubin_error = validate_lab_value(bilirubin, "Bilirubin", 0, 50)
        if not is_valid_bilirubin:
            validation_errors.append(bilirubin_error)
        
        if validation_errors:
            st.error("**⚠️ Lỗi validation:**")
            for error in validation_errors:
                st.error(f"- {error}")
            st.stop()
        
        params = {
            'gcs': gcs,
            'hr': hr,
            'sbp': sbp,
            'creatinine': creatinine,
            'urine_output': urine_output,
            'is_ventilated': is_ventilated,
            'pao2': pao2,
            'fio2': fio2,
            'platelets': platelets,
            'wbc': wbc,
            'bilirubin': bilirubin,
            'pt': pt
        }
        
        result = calculate_lods(params)
        
        # Display results
        st.markdown("### 📊 Kết quả")
        
        render_result_box(
            "LODS Score",
            f"{result['total_score']}/22",
            subtitle=result['interpretation'],
            color=result['color'],
            icon="🚨"
        )
        
        st.markdown("---")
        st.markdown("### 📋 Chi tiết theo hệ cơ quan")
        
        organ_names = {
            "neurological": "🧠 Thần kinh",
            "cardiovascular": "❤️ Tim mạch",
            "renal": "🧪 Thận",
            "pulmonary": "🫁 Hô hấp",
            "hematological": "🩸 Huyết học",
            "hepatic": "🩸 Gan"
        }
        
        for organ, score in result['organ_scores'].items():
            col3, col4 = st.columns([3, 1])
            with col3:
                st.markdown(f"**{organ_names[organ]}:**")
            with col4:
                st.markdown(f"**{score}/5 điểm**")
        
        st.markdown("---")
        st.markdown("### 📋 Chi tiết điểm số")
        
        for detail in result['details']:
            st.markdown(f"- {detail}")
        
        st.markdown("---")
        st.markdown("### 💡 Khuyến nghị")
        
        if result['severity'] == "Nhẹ":
            st.success("""
            **✅ Suy cơ quan nhẹ:**
            - Điều trị chuẩn
            - Theo dõi định kỳ
            - Đánh giá lại thường xuyên
            """)
        elif result['severity'] == "Trung bình":
            st.warning("""
            **⚠️ Suy cơ quan trung bình:**
            - Điều trị tích cực
            - Theo dõi sát
            - Hội chẩn chuyên khoa nếu cần
            """)
        else:
            st.error("""
            **🚨 Suy cơ quan nặng:**
            - Điều trị rất tích cực
            - Theo dõi liên tục
            - Hội chẩn đa chuyên khoa
            - Cân nhắc hỗ trợ cơ quan (RRT, ECMO, etc.)
            """)
        
        # Prepare inputs for history and share
        inputs_dict = {
            "GCS": f"{gcs}",
            "Heart Rate": f"{hr:.0f} /min",
            "SBP": f"{sbp:.0f} mmHg",
            "Creatinine": f"{creatinine:.1f} mg/dL",
            "Urine Output": f"{urine_output:.1f} L/ngày",
            "Is Ventilated": "Có" if is_ventilated else "Không",
            "PaO₂": f"{pao2:.0f} mmHg" if is_ventilated else "N/A",
            "FiO₂": f"{fio2:.2f}" if is_ventilated else "N/A",
            "Platelets": f"{platelets:.0f} ×10³/µL",
            "WBC": f"{wbc:.1f} ×10³/µL",
            "Bilirubin": f"{bilirubin:.1f} mg/dL",
            "PT Ratio": f"{pt:.2f}"
        }
        
        results_dict = {
            "LODS Score": f"{result['total_score']}/22",
            "Interpretation": result['interpretation'],
            "Severity": result['severity'],
            "Organ Scores": result['organ_scores']
        }
        
        # Save to history
        save_calculation_to_history(
            calculator_id="lods",
            calculator_name="LODS Score",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Share section
        render_share_section(
            calculator_id="lods",
            calculator_name="LODS Score",
            inputs=inputs_dict,
            results=results_dict,
            show_qr=True
        )
        
        # History section
        st.markdown("---")
        render_history_ui(calculator_id="lods", show_actions=True)
    
    st.markdown("---")
    
    with st.expander("📖 Thông tin về LODS"):
        st.markdown("""
        **LODS (Logistic Organ Dysfunction Score)** đánh giá mức độ suy cơ quan trong ICU.
        
        **6 hệ cơ quan:**
        1. **Thần kinh:** Dựa trên GCS
        2. **Tim mạch:** HR và SBP
        3. **Thận:** Creatinine và lượng nước tiểu
        4. **Hô hấp:** PaO2/FiO2 (nếu thở máy)
        5. **Huyết học:** Platelets và WBC
        6. **Gan:** Bilirubin và PT
        
        **Tài liệu tham khảo:**
        - Le Gall JR, et al. The Logistic Organ Dysfunction system. A new way to assess 
          organ dysfunction in the intensive care unit. JAMA. 1996;276(10):802-810.
        """)
    
    # References section
    references = get_references("LODS")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-01-15",
            show_evidence_level=True,
            show_links=True
        )
    
    st.caption("⚠️ LODS chỉ là công cụ hỗ trợ. Đánh giá lâm sàng toàn diện vẫn là quan trọng nhất.")

