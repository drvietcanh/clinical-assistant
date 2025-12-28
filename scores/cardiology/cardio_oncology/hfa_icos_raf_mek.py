"""
HFA-ICOS Baseline Cardio-Oncology Risk Assessment for Combination RAF and MEK Inhibitors
========================================================================================

Baseline cardiovascular risk assessment for patients before starting combination
RAF and MEK inhibitors (e.g., dabrafenib + trametinib, vemurafenib + cobimetinib)
for BRAF-mutant cancers (melanoma, NSCLC, etc.).

Reference:
- Lyon AR, et al. 2022 ESC Guidelines on cardio-oncology.

Special Considerations:
- Left ventricular dysfunction
- Hypertension
- QT prolongation
- Pyrexia
- Ocular toxicity
"""

import streamlit as st
from scores.utils.validation import validate_age
from components.ui.validation import render_validation_errors
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.export import render_export_section


def calculate_hfa_icos_raf_mek(
    age: int,
    is_female: bool,
    prior_heart_failure: bool = False,
    prior_myocardial_infarction: bool = False,
    coronary_artery_disease: bool = False,
    hypertension: bool = False,
    diabetes: bool = False,
    lvef: float = None,
    bnp: float = None,
    qtc_prolonged: bool = False,
    egfr: float = None,
    multiple_comorbidities: bool = False
) -> dict:
    """Calculate HFA-ICOS Risk for RAF/MEK Inhibitors"""
    risk_score = 0
    risk_factors = []
    
    if age >= 75:
        risk_score += 3
        risk_factors.append(f"Tuổi ≥75 → +3 điểm")
    elif age >= 65:
        risk_score += 2
        risk_factors.append(f"Tuổi 65-74 → +2 điểm")
    
    if prior_heart_failure:
        risk_score += 4
        risk_factors.append("Tiền sử suy tim → +4 điểm")
    
    if prior_myocardial_infarction:
        risk_score += 3
        risk_factors.append("Tiền sử nhồi máu cơ tim → +3 điểm")
    
    if coronary_artery_disease:
        risk_score += 2
        risk_factors.append("Bệnh mạch vành → +2 điểm")
    
    if lvef is not None and lvef < 50:
        risk_score += 3
        risk_factors.append(f"LVEF <50% ({lvef}%) → +3 điểm")
    
    if bnp is not None and bnp > 400:
        risk_score += 2
        risk_factors.append(f"BNP >400 → +2 điểm")
    
    if qtc_prolonged:
        risk_score += 3
        risk_factors.append("QT kéo dài → +3 điểm")
    
    if hypertension:
        risk_score += 2
        risk_factors.append("Tăng huyết áp → +2 điểm")
    
    if diabetes:
        risk_score += 1
        risk_factors.append("Đái tháo đường → +1 điểm")
    
    if egfr is not None and egfr < 60:
        risk_score += 2
        risk_factors.append(f"eGFR <60 → +2 điểm")
    
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
    """Render HFA-ICOS RAF/MEK Inhibitors Risk Assessment"""
    st.set_page_config(page_title="HFA-ICOS RAF/MEK Risk", layout="wide")
    shared = load_shared_result_from_url()
    
    st.markdown("""
    <h2 style='text-align: center; color: #10B981;'>❤️ HFA-ICOS Cardio-Oncology Risk Assessment</h2>
    <p style='text-align: center; color: #6B7280;'>
    Combination RAF and MEK Inhibitors<br>
    Đánh giá nguy cơ tim mạch trước điều trị RAF/MEK inhibitors
    </p>
    """, unsafe_allow_html=True)
    
    with st.expander("ℹ️ Giới thiệu"):
        st.markdown("""
        **HFA-ICOS Baseline Cardio-Oncology Risk Assessment for RAF/MEK Inhibitors**
        đánh giá nguy cơ tim mạch trước khi bắt đầu điều trị kết hợp RAF và MEK inhibitors.
        
        ### Đặc điểm:
        - Suy chức năng thất trái
        - Tăng huyết áp
        - Kéo dài QT
        - Sốt
        """)
    
    age = st.number_input("Tuổi (năm)", min_value=18, max_value=120, value=65, key="raf_mek_age")
    is_female = st.selectbox("Giới tính", ["Nam", "Nữ"], key="raf_mek_sex") == "Nữ"
    
    st.markdown("### ❤️ Bệnh tim mạch có sẵn")
    prior_heart_failure = st.checkbox("Tiền sử suy tim", key="raf_mek_hf")
    prior_myocardial_infarction = st.checkbox("Tiền sử nhồi máu cơ tim", key="raf_mek_mi")
    coronary_artery_disease = st.checkbox("Bệnh mạch vành", key="raf_mek_cad")
    
    st.markdown("### 🔴 Yếu tố nguy cơ")
    hypertension = st.checkbox("Tăng huyết áp", key="raf_mek_htn")
    diabetes = st.checkbox("Đái tháo đường", key="raf_mek_dm")
    
    st.markdown("### 💓 Chức năng tim")
    col1, col2 = st.columns(2)
    with col1:
        lvef = st.number_input("LVEF (%)", min_value=0.0, max_value=100.0, value=None, key="raf_mek_lvef")
    with col2:
        bnp = st.number_input("BNP (pg/mL)", min_value=0.0, max_value=10000.0, value=None, key="raf_mek_bnp")
    
    qtc_prolonged = st.checkbox("QT kéo dài", key="raf_mek_qtc")
    egfr = st.number_input("eGFR (mL/min/1.73m²)", min_value=0.0, max_value=200.0, value=None, key="raf_mek_egfr")
    multiple_comorbidities = st.checkbox("Nhiều bệnh kèm theo", key="raf_mek_comorb")
    
    if st.button("🔬 Đánh giá nguy cơ", type="primary", use_container_width=True):
        result = calculate_hfa_icos_raf_mek(
            age, is_female, prior_heart_failure, prior_myocardial_infarction,
            coronary_artery_disease, hypertension, diabetes, lvef, bnp,
            qtc_prolonged, egfr, multiple_comorbidities
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
            - Tư vấn tim mạch bắt buộc
            - Theo dõi LVEF mỗi 3 tháng
            - ECG mỗi chu kỳ (QT interval)
            - Kiểm soát huyết áp chặt chẽ
            """)
        else:
            st.markdown("""
            - Theo dõi tiêu chuẩn
            - Siêu âm tim mỗi 6 tháng
            - ECG mỗi 3-6 tháng
            """)
        
        save_calculation_to_history(
            calculator_id="hfa_icos_raf_mek",
            calculator_name="HFA-ICOS RAF/MEK Risk",
            inputs={"Tuổi": f"{age}"},
            result={"Điểm": result["risk_score"], "Phân loại": result["risk_category"]}
        )
        
        render_share_section(calculator_id="hfa_icos_raf_mek", calculator_name="HFA-ICOS RAF/MEK Risk")
        render_export_section(calculator_id="hfa_icos_raf_mek", calculator_name="HFA-ICOS RAF/MEK Risk", data={"result": result})
    
    render_history_ui(calculator_id="hfa_icos_raf_mek", show_actions=True)
    references = get_references("HFA-ICOS RAF/MEK Risk")
    if references:
        render_references_section(references)

