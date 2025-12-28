"""
HFA-ICOS Baseline Cardio-Oncology Risk Assessment for Multi-Targeted Kinase Inhibitors (CML)
=============================================================================================

Baseline cardiovascular risk assessment for patients with chronic myeloid leukemia (CML)
before starting multi-targeted kinase inhibitors (TKIs) such as imatinib, 
dasatinib, nilotinib, bosutinib, ponatinib.

Reference:
- Lyon AR, et al. 2022 ESC Guidelines on cardio-oncology developed in 
  collaboration with the European Hematology Association (EHA), the European 
  Society for Therapeutic Radiology and Oncology (ESTRO) and the International 
  Cardio-Oncology Society (IC-OS). Eur Heart J. 2022;43(41):4229-4361.

Special Considerations for TKIs:
- QT prolongation risk (especially nilotinib, dasatinib)
- Vascular events (especially ponatinib)
- Hypertension
- Pleural/pericardial effusions (dasatinib)
- Pulmonary hypertension (dasatinib)

Risk Categories:
- Low Risk: Standard monitoring
- Medium Risk: Enhanced monitoring
- High Risk: Intensive monitoring and cardiology consultation
- Very High Risk: Consider alternative therapy or intensive cardioprotection
"""

import streamlit as st
from scores.utils.validation import validate_age, validate_lab_value
from components.ui.validation import render_validation_errors
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
from components.export import render_export_section
# ======================================


def calculate_hfa_icos_cml(
    age: int,
    is_female: bool,
    # Pre-existing cardiovascular disease
    prior_heart_failure: bool = False,
    prior_myocardial_infarction: bool = False,
    prior_stroke: bool = False,
    coronary_artery_disease: bool = False,
    atrial_fibrillation: bool = False,
    valvular_heart_disease: bool = False,
    peripheral_artery_disease: bool = False,
    # Cardiovascular risk factors
    hypertension: bool = False,
    diabetes: bool = False,
    dyslipidemia: bool = False,
    smoking: bool = False,
    obesity: bool = False,
    # Cardiac function
    lvef: float = None,
    bnp: float = None,
    nt_probnp: float = None,
    troponin_elevated: bool = False,
    qtc_prolonged: bool = False,
    # Renal function
    egfr: float = None,
    # Planned TKI therapy
    tki_type: str = "imatinib",  # imatinib, dasatinib, nilotinib, bosutinib, ponatinib
    # TKI-specific risks
    prior_qt_prolongation: bool = False,
    prior_vascular_event: bool = False,
    prior_pleural_effusion: bool = False,
    # Other factors
    multiple_comorbidities: bool = False
) -> dict:
    """
    Calculate HFA-ICOS Baseline Cardio-Oncology Risk for CML TKI Therapy
    
    Returns:
        Dictionary with risk category, score, and recommendations
    """
    risk_score = 0
    risk_factors = []
    
    # Age
    if age >= 75:
        risk_score += 3
        risk_factors.append(f"Tuổi ≥75 ({age} tuổi) → +3 điểm")
    elif age >= 65:
        risk_score += 2
        risk_factors.append(f"Tuổi 65-74 ({age} tuổi) → +2 điểm")
    elif age >= 55:
        risk_score += 1
        risk_factors.append(f"Tuổi 55-64 ({age} tuổi) → +1 điểm")
    
    # Pre-existing cardiovascular disease
    if prior_heart_failure:
        risk_score += 4
        risk_factors.append("Tiền sử suy tim → +4 điểm")
    
    if prior_myocardial_infarction:
        risk_score += 3
        risk_factors.append("Tiền sử nhồi máu cơ tim → +3 điểm")
    
    if coronary_artery_disease:
        risk_score += 2
        risk_factors.append("Bệnh mạch vành → +2 điểm")
    
    if peripheral_artery_disease:
        risk_score += 2
        risk_factors.append("Bệnh động mạch ngoại biên → +2 điểm")
    
    if valvular_heart_disease:
        risk_score += 2
        risk_factors.append("Bệnh van tim → +2 điểm")
    
    if atrial_fibrillation:
        risk_score += 2
        risk_factors.append("Rung nhĩ → +2 điểm")
    
    if prior_stroke:
        risk_score += 2
        risk_factors.append("Tiền sử đột quỵ → +2 điểm")
    
    # Cardiac function
    if lvef is not None:
        if lvef < 40:
            risk_score += 4
            risk_factors.append(f"LVEF <40% ({lvef}%) → +4 điểm")
        elif lvef < 50:
            risk_score += 2
            risk_factors.append(f"LVEF 40-49% ({lvef}%) → +2 điểm")
    
    if bnp is not None:
        if bnp > 400:
            risk_score += 3
            risk_factors.append(f"BNP >400 pg/mL ({bnp} pg/mL) → +3 điểm")
        elif bnp > 200:
            risk_score += 2
            risk_factors.append(f"BNP 200-400 pg/mL ({bnp} pg/mL) → +2 điểm")
    
    if nt_probnp is not None:
        if nt_probnp > 2000:
            risk_score += 3
            risk_factors.append(f"NT-proBNP >2000 pg/mL ({nt_probnp} pg/mL) → +3 điểm")
        elif nt_probnp > 1000:
            risk_score += 2
            risk_factors.append(f"NT-proBNP 1000-2000 pg/mL ({nt_probnp} pg/mL) → +2 điểm")
    
    if troponin_elevated:
        risk_score += 3
        risk_factors.append("Troponin tăng → +3 điểm")
    
    # TKI-specific risks
    if qtc_prolonged or prior_qt_prolongation:
        risk_score += 3
        risk_factors.append("QT kéo dài hoặc tiền sử → +3 điểm")
    
    if prior_vascular_event:
        risk_score += 3
        risk_factors.append("Tiền sử biến cố mạch máu → +3 điểm")
    
    if prior_pleural_effusion:
        risk_score += 2
        risk_factors.append("Tiền sử tràn dịch màng phổi → +2 điểm")
    
    # Cardiovascular risk factors
    if hypertension:
        risk_score += 2  # Higher weight for TKIs
        risk_factors.append("Tăng huyết áp → +2 điểm")
    
    if diabetes:
        risk_score += 2
        risk_factors.append("Đái tháo đường → +2 điểm")
    
    if dyslipidemia:
        risk_score += 1
        risk_factors.append("Rối loạn lipid máu → +1 điểm")
    
    if smoking:
        risk_score += 1
        risk_factors.append("Hút thuốc → +1 điểm")
    
    if obesity:
        risk_score += 1
        risk_factors.append("Béo phì (BMI ≥30) → +1 điểm")
    
    # Renal function
    if egfr is not None:
        if egfr < 30:
            risk_score += 3
            risk_factors.append(f"eGFR <30 ({egfr:.1f}) → +3 điểm")
        elif egfr < 60:
            risk_score += 2
            risk_factors.append(f"eGFR 30-59 ({egfr:.1f}) → +2 điểm")
    
    # TKI type-specific risk
    if tki_type == "ponatinib":
        risk_score += 3
        risk_factors.append("Ponatinib (nguy cơ mạch máu cao) → +3 điểm")
    elif tki_type == "nilotinib":
        risk_score += 2
        risk_factors.append("Nilotinib (nguy cơ QT cao) → +2 điểm")
    elif tki_type == "dasatinib":
        risk_score += 2
        risk_factors.append("Dasatinib (nguy cơ tràn dịch) → +2 điểm")
    
    if multiple_comorbidities:
        risk_score += 2
        risk_factors.append("Nhiều bệnh kèm theo → +2 điểm")
    
    # Determine risk category
    if risk_score >= 15:
        risk_category = "Rất cao"
        risk_color = "error"
        risk_icon = "🔴"
    elif risk_score >= 10:
        risk_category = "Cao"
        risk_color = "warning"
        risk_icon = "🟠"
    elif risk_score >= 6:
        risk_category = "Trung bình"
        risk_color = "info"
        risk_icon = "🟡"
    else:
        risk_category = "Thấp"
        risk_color = "success"
        risk_icon = "🟢"
    
    return {
        "risk_score": risk_score,
        "risk_category": risk_category,
        "risk_color": risk_color,
        "risk_icon": risk_icon,
        "risk_factors": risk_factors,
        "total_factors": len(risk_factors),
        "tki_type": tki_type
    }


def render():
    """Render HFA-ICOS CML TKI Risk Assessment interface"""
    st.set_page_config(page_title="HFA-ICOS CML TKI Risk", layout="wide")
    
    shared = load_shared_result_from_url()
    
    st.markdown("""
    <h2 style='text-align: center; color: #10B981;'>❤️ HFA-ICOS Cardio-Oncology Risk Assessment</h2>
    <p style='text-align: center; color: #6B7280;'>
    Multi-Targeted Kinase Inhibitors (CML)<br>
    Đánh giá nguy cơ tim mạch trước điều trị CML bằng TKI
    </p>
    """, unsafe_allow_html=True)
    
    with st.expander("ℹ️ Giới thiệu"):
        st.markdown("""
        **HFA-ICOS Baseline Cardio-Oncology Risk Assessment for CML TKI Therapy**
        đánh giá nguy cơ tim mạch trước khi bắt đầu điều trị CML bằng TKI.
        
        ### Đặc điểm TKI:
        - **Imatinib:** Nguy cơ thấp nhất
        - **Dasatinib:** Tràn dịch màng phổi, tăng áp phổi
        - **Nilotinib:** Kéo dài QT, biến cố mạch máu
        - **Bosutinib:** Tiêu chảy, tăng men gan
        - **Ponatinib:** Nguy cơ mạch máu cao nhất
        
        ### Theo dõi đặc biệt:
        - ECG (QT interval) - đặc biệt với nilotinib
        - Huyết áp - tất cả TKI
        - Siêu âm tim - dasatinib (tăng áp phổi)
        - Dấu hiệu tràn dịch - dasatinib
        """)
    
    # Inputs (similar structure to multiple_myeloma but with TKI-specific fields)
    st.markdown("### 📊 Thông tin bệnh nhân")
    
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.number_input("Tuổi (năm)", min_value=18, max_value=120, value=65, step=1, key="hfa_icos_cml_age")
    
    with col2:
        is_female = st.selectbox("Giới tính", ["Nam", "Nữ"], key="hfa_icos_cml_sex") == "Nữ"
    
    # Pre-existing cardiovascular disease
    st.markdown("### ❤️ Bệnh tim mạch có sẵn")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        prior_heart_failure = st.checkbox("Tiền sử suy tim", key="hfa_icos_cml_hf")
        prior_myocardial_infarction = st.checkbox("Tiền sử nhồi máu cơ tim", key="hfa_icos_cml_mi")
        coronary_artery_disease = st.checkbox("Bệnh mạch vành", key="hfa_icos_cml_cad")
    
    with col2:
        atrial_fibrillation = st.checkbox("Rung nhĩ", key="hfa_icos_cml_afib")
        valvular_heart_disease = st.checkbox("Bệnh van tim", key="hfa_icos_cml_valve")
        peripheral_artery_disease = st.checkbox("Bệnh động mạch ngoại biên", key="hfa_icos_cml_pad")
    
    with col3:
        prior_stroke = st.checkbox("Tiền sử đột quỵ", key="hfa_icos_cml_stroke")
    
    # Cardiovascular risk factors
    st.markdown("### 🔴 Yếu tố nguy cơ tim mạch")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        hypertension = st.checkbox("Tăng huyết áp", key="hfa_icos_cml_htn")
        diabetes = st.checkbox("Đái tháo đường", key="hfa_icos_cml_dm")
    
    with col2:
        dyslipidemia = st.checkbox("Rối loạn lipid máu", key="hfa_icos_cml_dyslipid")
        smoking = st.checkbox("Hút thuốc", key="hfa_icos_cml_smoking")
    
    with col3:
        obesity = st.checkbox("Béo phì (BMI ≥30)", key="hfa_icos_cml_obesity")
    
    # Cardiac function
    st.markdown("### 💓 Chức năng tim")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        lvef = st.number_input("LVEF (%)", min_value=0.0, max_value=100.0, value=None, step=1.0, format="%.1f", key="hfa_icos_cml_lvef")
    
    with col2:
        bnp = st.number_input("BNP (pg/mL)", min_value=0.0, max_value=10000.0, value=None, step=1.0, format="%.1f", key="hfa_icos_cml_bnp")
    
    with col3:
        nt_probnp = st.number_input("NT-proBNP (pg/mL)", min_value=0.0, max_value=50000.0, value=None, step=1.0, format="%.1f", key="hfa_icos_cml_ntprobnp")
    
    col4, col5 = st.columns(2)
    
    with col4:
        troponin_elevated = st.checkbox("Troponin tăng", key="hfa_icos_cml_troponin")
    
    with col5:
        qtc_prolonged = st.checkbox("QT kéo dài", key="hfa_icos_cml_qtc")
    
    # Renal function
    st.markdown("### 🫘 Chức năng thận")
    
    egfr = st.number_input("eGFR (mL/min/1.73m²)", min_value=0.0, max_value=200.0, value=None, step=1.0, format="%.1f", key="hfa_icos_cml_egfr")
    
    # Planned TKI therapy
    st.markdown("### 💊 Điều trị TKI dự kiến")
    
    col1, col2 = st.columns(2)
    
    with col1:
        tki_type = st.selectbox(
            "Loại TKI",
            ["imatinib", "dasatinib", "nilotinib", "bosutinib", "ponatinib"],
            format_func=lambda x: {
                "imatinib": "Imatinib",
                "dasatinib": "Dasatinib",
                "nilotinib": "Nilotinib",
                "bosutinib": "Bosutinib",
                "ponatinib": "Ponatinib"
            }[x],
            key="hfa_icos_cml_tki"
        )
    
    # TKI-specific risks
    st.markdown("### ⚠️ Yếu tố nguy cơ đặc biệt TKI")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        prior_qt_prolongation = st.checkbox("Tiền sử QT kéo dài", key="hfa_icos_cml_qt_hist")
    
    with col2:
        prior_vascular_event = st.checkbox("Tiền sử biến cố mạch máu", key="hfa_icos_cml_vasc")
    
    with col3:
        prior_pleural_effusion = st.checkbox("Tiền sử tràn dịch màng phổi", key="hfa_icos_cml_pleural")
    
    multiple_comorbidities = st.checkbox("Nhiều bệnh kèm theo", key="hfa_icos_cml_comorb")
    
    if st.button("🔬 Đánh giá nguy cơ", type="primary", use_container_width=True):
        errors = []
        if age < 18 or age > 120:
            errors.append("Tuổi phải từ 18-120")
        if lvef is not None and (lvef < 0 or lvef > 100):
            errors.append("LVEF phải từ 0-100%")
        
        if errors:
            render_validation_errors(errors)
        else:
            result = calculate_hfa_icos_cml(
                age=age,
                is_female=is_female,
                prior_heart_failure=prior_heart_failure,
                prior_myocardial_infarction=prior_myocardial_infarction,
                prior_stroke=prior_stroke,
                coronary_artery_disease=coronary_artery_disease,
                atrial_fibrillation=atrial_fibrillation,
                valvular_heart_disease=valvular_heart_disease,
                peripheral_artery_disease=peripheral_artery_disease,
                hypertension=hypertension,
                diabetes=diabetes,
                dyslipidemia=dyslipidemia,
                smoking=smoking,
                obesity=obesity,
                lvef=lvef,
                bnp=bnp,
                nt_probnp=nt_probnp,
                troponin_elevated=troponin_elevated,
                qtc_prolonged=qtc_prolonged,
                egfr=egfr,
                tki_type=tki_type,
                prior_qt_prolongation=prior_qt_prolongation,
                prior_vascular_event=prior_vascular_event,
                prior_pleural_effusion=prior_pleural_effusion,
                multiple_comorbidities=multiple_comorbidities
            )
            
            st.markdown("---")
            st.markdown("### 📋 Kết quả đánh giá nguy cơ")
            
            if result["risk_category"] == "Rất cao":
                st.error(f"{result['risk_icon']} **NGUY CƠ RẤT CAO** - Điểm số: {result['risk_score']}")
            elif result["risk_category"] == "Cao":
                st.warning(f"{result['risk_icon']} **NGUY CƠ CAO** - Điểm số: {result['risk_score']}")
            elif result["risk_category"] == "Trung bình":
                st.info(f"{result['risk_icon']} **NGUY CƠ TRUNG BÌNH** - Điểm số: {result['risk_score']}")
            else:
                st.success(f"{result['risk_icon']} **NGUY CƠ THẤP** - Điểm số: {result['risk_score']}")
            
            st.metric("Tổng điểm nguy cơ", f"{result['risk_score']}")
            st.metric("Số yếu tố nguy cơ", f"{result['total_factors']}")
            
            if result['risk_factors']:
                st.markdown("**Các yếu tố nguy cơ:**")
                for factor in result['risk_factors']:
                    st.markdown(f"- {factor}")
            
            # Clinical recommendations
            st.markdown("### 💡 Khuyến nghị lâm sàng")
            
            tki_name = {"imatinib": "Imatinib", "dasatinib": "Dasatinib", "nilotinib": "Nilotinib", 
                       "bosutinib": "Bosutinib", "ponatinib": "Ponatinib"}[result["tki_type"]]
            
            if result["risk_category"] in ["Rất cao", "Cao"]:
                st.markdown(f"""
                **Nguy cơ cao/rất cao với {tki_name}:**
                
                1. **Tư vấn tim mạch bắt buộc** trước khi bắt đầu
                2. **Theo dõi chuyên sâu:**
                   - ECG mỗi chu kỳ (đặc biệt với nilotinib - QT interval)
                   - Huyết áp mỗi lần khám
                   - Siêu âm tim mỗi 3-6 tháng
                   - BNP/NT-proBNP mỗi 3-6 tháng
                3. **Theo dõi đặc biệt:**
                   - Dasatinib: Dấu hiệu tràn dịch màng phổi, tăng áp phổi
                   - Nilotinib/Ponatinib: Biến cố mạch máu, ECG
                4. **Bảo vệ tim mạch:**
                   - Kiểm soát huyết áp chặt chẽ
                   - Xem xét ACEi/ARB
                   - Statin nếu có chỉ định
                """)
            else:
                st.markdown(f"""
                **Nguy cơ thấp/trung bình với {tki_name}:**
                
                1. **Theo dõi tiêu chuẩn:**
                   - ECG mỗi 3-6 tháng
                   - Huyết áp mỗi lần khám
                   - Siêu âm tim mỗi 6-12 tháng
                2. **Kiểm soát yếu tố nguy cơ**
                3. **Theo dõi triệu chứng**
                """)
            
            save_calculation_to_history(
                calculator_id="hfa_icos_cml",
                calculator_name="HFA-ICOS CML TKI Risk",
                inputs={"Tuổi": f"{age}", "TKI": tki_name},
                result={"Điểm nguy cơ": result["risk_score"], "Phân loại": result["risk_category"]}
            )
            
            render_share_section(calculator_id="hfa_icos_cml", calculator_name="HFA-ICOS CML TKI Risk")
            render_export_section(calculator_id="hfa_icos_cml", calculator_name="HFA-ICOS CML TKI Risk", data={"inputs": {"age": age, "tki_type": tki_type}, "result": result})
    
    render_history_ui(calculator_id="hfa_icos_cml", show_actions=True)
    
    references = get_references("HFA-ICOS CML TKI Risk")
    if references:
        render_references_section(references)

