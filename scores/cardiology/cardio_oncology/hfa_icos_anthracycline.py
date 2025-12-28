"""
HFA-ICOS Baseline Cardio-Oncology Risk Assessment for Anthracycline Chemotherapy
=================================================================================

Baseline cardiovascular risk assessment for patients before starting anthracycline
chemotherapy (doxorubicin, epirubicin, daunorubicin, idarubicin) for various cancers.

Reference:
- Lyon AR, et al. 2022 ESC Guidelines on cardio-oncology.

Special Considerations:
- Cumulative dose-dependent cardiotoxicity
- Left ventricular dysfunction
- Heart failure risk
- Age
- Prior cardiac disease
- Concomitant radiation therapy
"""

import streamlit as st
from scores.utils.validation import validate_age
from components.ui.validation import render_validation_errors
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.export import render_export_section


def calculate_hfa_icos_anthracycline(
    age: int,
    is_female: bool,
    prior_heart_failure: bool = False,
    prior_myocardial_infarction: bool = False,
    coronary_artery_disease: bool = False,
    hypertension: bool = False,
    diabetes: bool = False,
    lvef: float = None,
    bnp: float = None,
    planned_dose: float = None,  # mg/m²
    anthracycline_type: str = "doxorubicin",  # doxorubicin, epirubicin, daunorubicin, idarubicin
    concomitant_radiation: bool = False,
    egfr: float = None,
    multiple_comorbidities: bool = False
) -> dict:
    """Calculate HFA-ICOS Risk for Anthracycline Chemotherapy"""
    risk_score = 0
    risk_factors = []
    
    # Age is very important for anthracyclines
    if age >= 70:
        risk_score += 4
        risk_factors.append(f"Tuổi ≥70 ({age} tuổi) → +4 điểm")
    elif age >= 60:
        risk_score += 3
        risk_factors.append(f"Tuổi 60-69 ({age} tuổi) → +3 điểm")
    elif age >= 50:
        risk_score += 2
        risk_factors.append(f"Tuổi 50-59 ({age} tuổi) → +2 điểm")
    elif age >= 40:
        risk_score += 1
        risk_factors.append(f"Tuổi 40-49 ({age} tuổi) → +1 điểm")
    
    if prior_heart_failure:
        risk_score += 5
        risk_factors.append("Tiền sử suy tim → +5 điểm")
    
    if prior_myocardial_infarction:
        risk_score += 4
        risk_factors.append("Tiền sử nhồi máu cơ tim → +4 điểm")
    
    if coronary_artery_disease:
        risk_score += 3
        risk_factors.append("Bệnh mạch vành → +3 điểm")
    
    # LVEF is critical
    if lvef is not None:
        if lvef < 50:
            risk_score += 5
            risk_factors.append(f"LVEF <50% ({lvef}%) → +5 điểm")
        elif lvef < 55:
            risk_score += 3
            risk_factors.append(f"LVEF 50-54% ({lvef}%) → +3 điểm")
    
    if bnp is not None:
        if bnp > 400:
            risk_score += 3
            risk_factors.append(f"BNP >400 pg/mL ({bnp} pg/mL) → +3 điểm")
        elif bnp > 200:
            risk_score += 2
            risk_factors.append(f"BNP 200-400 pg/mL ({bnp} pg/mL) → +2 điểm")
    
    # Planned dose is critical
    if planned_dose is not None:
        if anthracycline_type == "doxorubicin":
            if planned_dose >= 450:
                risk_score += 5
                risk_factors.append(f"Liều doxorubicin ≥450 mg/m² ({planned_dose} mg/m²) → +5 điểm")
            elif planned_dose >= 300:
                risk_score += 3
                risk_factors.append(f"Liều doxorubicin 300-449 mg/m² ({planned_dose} mg/m²) → +3 điểm")
            elif planned_dose >= 250:
                risk_score += 2
                risk_factors.append(f"Liều doxorubicin 250-299 mg/m² ({planned_dose} mg/m²) → +2 điểm")
        elif anthracycline_type == "epirubicin":
            if planned_dose >= 900:
                risk_score += 5
                risk_factors.append(f"Liều epirubicin ≥900 mg/m² ({planned_dose} mg/m²) → +5 điểm")
            elif planned_dose >= 600:
                risk_score += 3
                risk_factors.append(f"Liều epirubicin 600-899 mg/m² ({planned_dose} mg/m²) → +3 điểm")
        elif anthracycline_type == "daunorubicin":
            if planned_dose >= 550:
                risk_score += 5
                risk_factors.append(f"Liều daunorubicin ≥550 mg/m² ({planned_dose} mg/m²) → +5 điểm")
            elif planned_dose >= 400:
                risk_score += 3
                risk_factors.append(f"Liều daunorubicin 400-549 mg/m² ({planned_dose} mg/m²) → +3 điểm")
        elif anthracycline_type == "idarubicin":
            if planned_dose >= 150:
                risk_score += 5
                risk_factors.append(f"Liều idarubicin ≥150 mg/m² ({planned_dose} mg/m²) → +5 điểm")
            elif planned_dose >= 100:
                risk_score += 3
                risk_factors.append(f"Liều idarubicin 100-149 mg/m² ({planned_dose} mg/m²) → +3 điểm")
    
    if concomitant_radiation:
        risk_score += 3
        risk_factors.append("Xạ trị đồng thời → +3 điểm")
    
    if hypertension:
        risk_score += 2
        risk_factors.append("Tăng huyết áp → +2 điểm")
    
    if diabetes:
        risk_score += 2
        risk_factors.append("Đái tháo đường → +2 điểm")
    
    if egfr is not None and egfr < 60:
        risk_score += 2
        risk_factors.append(f"eGFR <60 ({egfr:.1f}) → +2 điểm")
    
    if multiple_comorbidities:
        risk_score += 2
        risk_factors.append("Nhiều bệnh kèm theo → +2 điểm")
    
    if risk_score >= 18:
        risk_category = "Rất cao"
        risk_icon = "🔴"
    elif risk_score >= 12:
        risk_category = "Cao"
        risk_icon = "🟠"
    elif risk_score >= 7:
        risk_category = "Trung bình"
        risk_icon = "🟡"
    else:
        risk_category = "Thấp"
        risk_icon = "🟢"
    
    return {
        "risk_score": risk_score,
        "risk_category": risk_category,
        "risk_icon": risk_icon,
        "risk_factors": risk_factors,
        "total_factors": len(risk_factors),
        "anthracycline_type": anthracycline_type,
        "planned_dose": planned_dose
    }


def render():
    """Render HFA-ICOS Anthracycline Risk Assessment"""
    st.set_page_config(page_title="HFA-ICOS Anthracycline Risk", layout="wide")
    shared = load_shared_result_from_url()
    
    st.markdown("""
    <h2 style='text-align: center; color: #10B981;'>❤️ HFA-ICOS Cardio-Oncology Risk Assessment</h2>
    <p style='text-align: center; color: #6B7280;'>
    Anthracycline Chemotherapy<br>
    Đánh giá nguy cơ tim mạch trước điều trị anthracycline
    </p>
    """, unsafe_allow_html=True)
    
    with st.expander("ℹ️ Giới thiệu"):
        st.markdown("""
        **HFA-ICOS Baseline Cardio-Oncology Risk Assessment for Anthracycline Chemotherapy**
        đánh giá nguy cơ tim mạch trước khi bắt đầu điều trị anthracycline.
        
        ### Đặc điểm:
        - **Độc tính phụ thuộc liều tích lũy**
        - Suy chức năng thất trái
        - Nguy cơ suy tim
        - Tuổi là yếu tố quan trọng
        - Xạ trị đồng thời làm tăng nguy cơ
        
        ### Ngưỡng liều an toàn:
        - **Doxorubicin:** <250 mg/m² (thấp), 250-450 mg/m² (trung bình), ≥450 mg/m² (cao)
        - **Epirubicin:** <600 mg/m² (thấp), 600-900 mg/m² (trung bình), ≥900 mg/m² (cao)
        - **Daunorubicin:** <400 mg/m² (thấp), 400-550 mg/m² (trung bình), ≥550 mg/m² (cao)
        - **Idarubicin:** <100 mg/m² (thấp), 100-150 mg/m² (trung bình), ≥150 mg/m² (cao)
        
        ### Theo dõi:
        - LVEF trước điều trị (bắt buộc)
        - LVEF mỗi 3 tháng trong và sau điều trị
        - BNP/NT-proBNP
        - Troponin
        """)
    
    age = st.number_input("Tuổi (năm)", min_value=18, max_value=120, value=65, key="anthra_age")
    is_female = st.selectbox("Giới tính", ["Nam", "Nữ"], key="anthra_sex") == "Nữ"
    
    st.markdown("### ❤️ Bệnh tim mạch có sẵn")
    col1, col2 = st.columns(2)
    with col1:
        prior_heart_failure = st.checkbox("Tiền sử suy tim", key="anthra_hf")
        prior_myocardial_infarction = st.checkbox("Tiền sử nhồi máu cơ tim", key="anthra_mi")
    with col2:
        coronary_artery_disease = st.checkbox("Bệnh mạch vành", key="anthra_cad")
    
    st.markdown("### 💓 Chức năng tim (QUAN TRỌNG)")
    col1, col2 = st.columns(2)
    with col1:
        lvef = st.number_input("LVEF (%) ⚠️ Bắt buộc", min_value=0.0, max_value=100.0, value=None, key="anthra_lvef")
    with col2:
        bnp = st.number_input("BNP (pg/mL)", min_value=0.0, max_value=10000.0, value=None, key="anthra_bnp")
    
    st.markdown("### 💊 Thông tin điều trị anthracycline")
    col1, col2 = st.columns(2)
    with col1:
        anthracycline_type = st.selectbox(
            "Loại anthracycline",
            ["doxorubicin", "epirubicin", "daunorubicin", "idarubicin"],
            format_func=lambda x: {
                "doxorubicin": "Doxorubicin",
                "epirubicin": "Epirubicin",
                "daunorubicin": "Daunorubicin",
                "idarubicin": "Idarubicin"
            }[x],
            key="anthra_type"
        )
    with col2:
        planned_dose = st.number_input(
            "Liều tích lũy dự kiến (mg/m²)",
            min_value=0.0,
            max_value=2000.0,
            value=None,
            step=10.0,
            format="%.1f",
            key="anthra_dose"
        )
    
    concomitant_radiation = st.checkbox("Xạ trị đồng thời", key="anthra_rt")
    
    st.markdown("### 🔴 Yếu tố nguy cơ")
    col1, col2 = st.columns(2)
    with col1:
        hypertension = st.checkbox("Tăng huyết áp", key="anthra_htn")
    with col2:
        diabetes = st.checkbox("Đái tháo đường", key="anthra_dm")
    
    egfr = st.number_input("eGFR (mL/min/1.73m²)", min_value=0.0, max_value=200.0, value=None, key="anthra_egfr")
    multiple_comorbidities = st.checkbox("Nhiều bệnh kèm theo", key="anthra_comorb")
    
    if st.button("🔬 Đánh giá nguy cơ", type="primary", use_container_width=True):
        if lvef is None:
            st.warning("⚠️ LVEF là bắt buộc để đánh giá nguy cơ với anthracycline")
        else:
            result = calculate_hfa_icos_anthracycline(
                age, is_female, prior_heart_failure, prior_myocardial_infarction,
                coronary_artery_disease, hypertension, diabetes, lvef, bnp,
                planned_dose, anthracycline_type, concomitant_radiation, egfr, multiple_comorbidities
            )
            
            st.markdown("---")
            st.markdown("### 📋 Kết quả")
            
            if result["risk_category"] == "Rất cao":
                st.error(f"{result['risk_icon']} **NGUY CƠ RẤT CAO** - {result['risk_score']} điểm")
            elif result["risk_category"] == "Cao":
                st.warning(f"{result['risk_icon']} **NGUY CƠ CAO** - {result['risk_score']} điểm")
            elif result["risk_category"] == "Trung bình":
                st.info(f"{result['risk_icon']} **NGUY CƠ TRUNG BÌNH** - {result['risk_score']} điểm")
            else:
                st.success(f"{result['risk_icon']} **NGUY CƠ THẤP** - {result['risk_score']} điểm")
            
            st.metric("Tổng điểm", f"{result['risk_score']}")
            
            if result['risk_factors']:
                st.markdown("**Yếu tố nguy cơ:**")
                for factor in result['risk_factors']:
                    st.markdown(f"- {factor}")
            
            st.markdown("### 💡 Khuyến nghị")
            if result["risk_category"] in ["Rất cao", "Cao"]:
                st.markdown("""
                - Tư vấn tim mạch BẮT BUỘC trước điều trị
                - LVEF phải ≥50% trước khi bắt đầu
                - Xem xét bảo vệ tim mạch (ACEi/ARB, beta-blocker)
                - Theo dõi LVEF mỗi 3 tháng (bắt buộc)
                - BNP/NT-proBNP mỗi 3 tháng
                - Troponin mỗi chu kỳ
                - Cân nhắc giảm liều hoặc thay thế nếu nguy cơ rất cao
                - Ngừng điều trị nếu LVEF giảm >10% và <50%
                """)
            else:
                st.markdown("""
                - LVEF trước điều trị (bắt buộc)
                - Theo dõi LVEF mỗi 3 tháng
                - BNP/NT-proBNP mỗi 3-6 tháng
                - Troponin mỗi chu kỳ
                - Theo dõi triệu chứng suy tim
                """)
            
            save_calculation_to_history(
                calculator_id="hfa_icos_anthracycline",
                calculator_name="HFA-ICOS Anthracycline Risk",
                inputs={
                    "Tuổi": f"{age}",
                    "LVEF": f"{lvef}%" if lvef else "N/A",
                    "Loại": anthracycline_type,
                    "Liều": f"{planned_dose} mg/m²" if planned_dose else "N/A"
                },
                result={"Điểm": result["risk_score"], "Phân loại": result["risk_category"]}
            )
            
            render_share_section(calculator_id="hfa_icos_anthracycline", calculator_name="HFA-ICOS Anthracycline Risk")
            render_export_section(calculator_id="hfa_icos_anthracycline", calculator_name="HFA-ICOS Anthracycline Risk", data={"result": result})
    
    render_history_ui(calculator_id="hfa_icos_anthracycline", show_actions=True)
    references = get_references("HFA-ICOS Anthracycline Risk")
    if references:
        render_references_section(references)

