"""
HFA-ICOS Baseline Cardio-Oncology Risk Assessment for HER2-Targeted Therapies
==============================================================================

Baseline cardiovascular risk assessment for patients before starting HER2-targeted
therapies (trastuzumab, pertuzumab, T-DM1, lapatinib, neratinib) for HER2-positive cancers.

Reference:
- Lyon AR, et al. 2022 ESC Guidelines on cardio-oncology.

Special Considerations:
- Left ventricular dysfunction (especially trastuzumab)
- Heart failure risk
- Prior anthracycline exposure
- Age
"""

import streamlit as st
from scores.utils.validation import validate_age
from components.ui.validation import render_validation_errors
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.export import render_export_section


def calculate_hfa_icos_her2(
    age: int,
    is_female: bool,
    prior_heart_failure: bool = False,
    prior_myocardial_infarction: bool = False,
    coronary_artery_disease: bool = False,
    hypertension: bool = False,
    diabetes: bool = False,
    lvef: float = None,
    bnp: float = None,
    prior_anthracycline: bool = False,
    anthracycline_dose: float = None,  # mg/m²
    egfr: float = None,
    multiple_comorbidities: bool = False
) -> dict:
    """Calculate HFA-ICOS Risk for HER2-Targeted Therapies"""
    risk_score = 0
    risk_factors = []
    
    if age >= 70:
        risk_score += 3
        risk_factors.append(f"Tuổi ≥70 ({age} tuổi) → +3 điểm")
    elif age >= 60:
        risk_score += 2
        risk_factors.append(f"Tuổi 60-69 ({age} tuổi) → +2 điểm")
    elif age >= 50:
        risk_score += 1
        risk_factors.append(f"Tuổi 50-59 ({age} tuổi) → +1 điểm")
    
    if prior_heart_failure:
        risk_score += 5
        risk_factors.append("Tiền sử suy tim → +5 điểm")
    
    if prior_myocardial_infarction:
        risk_score += 3
        risk_factors.append("Tiền sử nhồi máu cơ tim → +3 điểm")
    
    if coronary_artery_disease:
        risk_score += 2
        risk_factors.append("Bệnh mạch vành → +2 điểm")
    
    # LVEF is critical for HER2-targeted therapy
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
    
    # Prior anthracycline is very important
    if prior_anthracycline:
        risk_score += 4
        risk_factors.append("Tiền sử anthracycline → +4 điểm")
        if anthracycline_dose is not None:
            if anthracycline_dose >= 300:
                risk_score += 2
                risk_factors.append(f"Liều anthracycline cao (≥300 mg/m²) → +2 điểm")
            elif anthracycline_dose >= 240:
                risk_score += 1
                risk_factors.append(f"Liều anthracycline trung bình (240-299 mg/m²) → +1 điểm")
    
    if hypertension:
        risk_score += 1
        risk_factors.append("Tăng huyết áp → +1 điểm")
    
    if diabetes:
        risk_score += 2
        risk_factors.append("Đái tháo đường → +2 điểm")
    
    if egfr is not None and egfr < 60:
        risk_score += 2
        risk_factors.append(f"eGFR <60 ({egfr:.1f}) → +2 điểm")
    
    if multiple_comorbidities:
        risk_score += 2
        risk_factors.append("Nhiều bệnh kèm theo → +2 điểm")
    
    if risk_score >= 15:
        risk_category = "Rất cao"
        risk_icon = "🔴"
    elif risk_score >= 10:
        risk_category = "Cao"
        risk_icon = "🟠"
    elif risk_score >= 6:
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
        "total_factors": len(risk_factors)
    }


def render():
    """Render HFA-ICOS HER2-Targeted Therapies Risk Assessment"""
    st.set_page_config(page_title="HFA-ICOS HER2 Risk", layout="wide")
    shared = load_shared_result_from_url()
    
    st.markdown("""
    <h2 style='text-align: center; color: #10B981;'>❤️ HFA-ICOS Cardio-Oncology Risk Assessment</h2>
    <p style='text-align: center; color: #6B7280;'>
    HER2-Targeted Therapies<br>
    Đánh giá nguy cơ tim mạch trước điều trị HER2-targeted therapies
    </p>
    """, unsafe_allow_html=True)
    
    with st.expander("ℹ️ Giới thiệu"):
        st.markdown("""
        **HFA-ICOS Baseline Cardio-Oncology Risk Assessment for HER2-Targeted Therapies**
        đánh giá nguy cơ tim mạch trước khi bắt đầu điều trị HER2-targeted therapies.
        
        ### Đặc điểm:
        - Suy chức năng thất trái (đặc biệt với trastuzumab)
        - Nguy cơ suy tim
        - Tiền sử anthracycline làm tăng nguy cơ đáng kể
        - Tuổi là yếu tố quan trọng
        
        ### Theo dõi:
        - LVEF trước điều trị (bắt buộc)
        - LVEF mỗi 3 tháng trong điều trị
        - BNP/NT-proBNP
        """)
    
    age = st.number_input("Tuổi (năm)", min_value=18, max_value=120, value=65, key="her2_age")
    is_female = st.selectbox("Giới tính", ["Nam", "Nữ"], key="her2_sex") == "Nữ"
    
    st.markdown("### ❤️ Bệnh tim mạch có sẵn")
    col1, col2 = st.columns(2)
    with col1:
        prior_heart_failure = st.checkbox("Tiền sử suy tim", key="her2_hf")
        prior_myocardial_infarction = st.checkbox("Tiền sử nhồi máu cơ tim", key="her2_mi")
    with col2:
        coronary_artery_disease = st.checkbox("Bệnh mạch vành", key="her2_cad")
    
    st.markdown("### 💓 Chức năng tim (QUAN TRỌNG)")
    col1, col2 = st.columns(2)
    with col1:
        lvef = st.number_input("LVEF (%) ⚠️ Bắt buộc", min_value=0.0, max_value=100.0, value=None, key="her2_lvef")
    with col2:
        bnp = st.number_input("BNP (pg/mL)", min_value=0.0, max_value=10000.0, value=None, key="her2_bnp")
    
    st.markdown("### 💊 Tiền sử anthracycline (QUAN TRỌNG)")
    prior_anthracycline = st.checkbox("Tiền sử anthracycline", key="her2_anthra")
    if prior_anthracycline:
        anthracycline_dose = st.number_input("Liều anthracycline tích lũy (mg/m²)", min_value=0.0, max_value=1000.0, value=None, key="her2_anthra_dose")
    else:
        anthracycline_dose = None
    
    st.markdown("### 🔴 Yếu tố nguy cơ")
    col1, col2 = st.columns(2)
    with col1:
        hypertension = st.checkbox("Tăng huyết áp", key="her2_htn")
    with col2:
        diabetes = st.checkbox("Đái tháo đường", key="her2_dm")
    
    egfr = st.number_input("eGFR (mL/min/1.73m²)", min_value=0.0, max_value=200.0, value=None, key="her2_egfr")
    multiple_comorbidities = st.checkbox("Nhiều bệnh kèm theo", key="her2_comorb")
    
    if st.button("🔬 Đánh giá nguy cơ", type="primary", use_container_width=True):
        if lvef is None:
            st.warning("⚠️ LVEF là bắt buộc để đánh giá nguy cơ với HER2-targeted therapy")
        else:
            result = calculate_hfa_icos_her2(
                age, is_female, prior_heart_failure, prior_myocardial_infarction,
                coronary_artery_disease, hypertension, diabetes, lvef, bnp,
                prior_anthracycline, anthracycline_dose, egfr, multiple_comorbidities
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
                - Theo dõi LVEF mỗi 3 tháng (bắt buộc)
                - BNP/NT-proBNP mỗi 3 tháng
                - Xem xét ACEi/ARB nếu có chỉ định
                - Ngừng điều trị nếu LVEF giảm >10% và <50%
                """)
            else:
                st.markdown("""
                - LVEF trước điều trị (bắt buộc)
                - Theo dõi LVEF mỗi 3 tháng
                - BNP/NT-proBNP mỗi 3-6 tháng
                - Theo dõi triệu chứng suy tim
                """)
            
            save_calculation_to_history(
                calculator_id="hfa_icos_her2",
                calculator_name="HFA-ICOS HER2 Risk",
                inputs={"Tuổi": f"{age}", "LVEF": f"{lvef}%" if lvef else "N/A"},
                result={"Điểm": result["risk_score"], "Phân loại": result["risk_category"]}
            )
            
            render_share_section(calculator_id="hfa_icos_her2", calculator_name="HFA-ICOS HER2 Risk")
            render_export_section(calculator_id="hfa_icos_her2", calculator_name="HFA-ICOS HER2 Risk", data={"result": result})
    
    render_history_ui(calculator_id="hfa_icos_her2", show_actions=True)
    references = get_references("HFA-ICOS HER2 Risk")
    if references:
        render_references_section(references)

