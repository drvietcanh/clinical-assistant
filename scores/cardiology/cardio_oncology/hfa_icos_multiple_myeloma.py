"""
HFA-ICOS Baseline Cardio-Oncology Risk Assessment for Multiple Myeloma Therapies
==================================================================================

Baseline cardiovascular risk assessment for patients with multiple myeloma 
before starting cancer therapy, particularly proteasome inhibitors, 
immunomodulatory drugs (IMiDs), and monoclonal antibodies.

Reference:
- Lyon AR, et al. 2022 ESC Guidelines on cardio-oncology developed in 
  collaboration with the European Hematology Association (EHA), the European 
  Society for Therapeutic Radiology and Oncology (ESTRO) and the International 
  Cardio-Oncology Society (IC-OS). Eur Heart J. 2022;43(41):4229-4361.
- HFA-ICOS Position Paper on Cardio-Oncology Services in Europe.

Risk Factors Assessed:
- Pre-existing cardiovascular disease
- Cardiovascular risk factors (hypertension, diabetes, dyslipidemia)
- Cardiac function (LVEF, BNP/NT-proBNP, troponin)
- Renal function
- Type and dose of planned therapy
- Patient age and comorbidities

Risk Categories:
- Low Risk: Standard monitoring
- Medium Risk: Enhanced monitoring
- High Risk: Intensive monitoring and cardiology consultation
- Very High Risk: Consider alternative therapy or intensive cardioprotection

Clinical Utility:
- Pre-treatment risk stratification
- Guides monitoring intensity
- Helps select appropriate therapy
- Prevents cardiovascular complications
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


def calculate_hfa_icos_multiple_myeloma(
    age: int,
    is_female: bool,
    # Pre-existing cardiovascular disease
    prior_heart_failure: bool = False,
    prior_myocardial_infarction: bool = False,
    prior_stroke: bool = False,
    coronary_artery_disease: bool = False,
    atrial_fibrillation: bool = False,
    valvular_heart_disease: bool = False,
    cardiomyopathy: bool = False,
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
    # Renal function
    egfr: float = None,
    creatinine: float = None,
    # Planned therapy
    therapy_type: str = "proteasome_inhibitor",  # proteasome_inhibitor, imid, monoclonal_ab, combination
    high_dose: bool = False,
    # Other factors
    prior_anthracycline: bool = False,
    radiation_therapy: bool = False,
    multiple_comorbidities: bool = False
) -> dict:
    """
    Calculate HFA-ICOS Baseline Cardio-Oncology Risk for Multiple Myeloma Therapies
    
    Args:
        age: Age (years)
        is_female: Female sex
        prior_heart_failure: Prior heart failure
        prior_myocardial_infarction: Prior MI
        prior_stroke: Prior stroke
        coronary_artery_disease: CAD
        atrial_fibrillation: Atrial fibrillation
        valvular_heart_disease: Valvular heart disease
        cardiomyopathy: Cardiomyopathy
        hypertension: Hypertension
        diabetes: Diabetes
        dyslipidemia: Dyslipidemia
        smoking: Current smoking
        obesity: Obesity (BMI ≥30)
        lvef: Left ventricular ejection fraction (%)
        bnp: BNP (pg/mL)
        nt_probnp: NT-proBNP (pg/mL)
        troponin_elevated: Elevated troponin
        egfr: eGFR (mL/min/1.73m²)
        creatinine: Creatinine (mg/dL)
        therapy_type: Type of planned therapy
        high_dose: High-dose therapy planned
        prior_anthracycline: Prior anthracycline exposure
        radiation_therapy: Prior radiation therapy
        multiple_comorbidities: Multiple comorbidities
    
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
    
    # Pre-existing cardiovascular disease (major risk factors)
    if prior_heart_failure:
        risk_score += 4
        risk_factors.append("Tiền sử suy tim → +4 điểm")
    
    if prior_myocardial_infarction:
        risk_score += 3
        risk_factors.append("Tiền sử nhồi máu cơ tim → +3 điểm")
    
    if coronary_artery_disease:
        risk_score += 2
        risk_factors.append("Bệnh mạch vành → +2 điểm")
    
    if cardiomyopathy:
        risk_score += 3
        risk_factors.append("Bệnh cơ tim → +3 điểm")
    
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
    
    # Cardiovascular risk factors
    if hypertension:
        risk_score += 1
        risk_factors.append("Tăng huyết áp → +1 điểm")
    
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
    
    if creatinine is not None and creatinine > 2.0:
        risk_score += 2
        risk_factors.append(f"Creatinine >2.0 mg/dL ({creatinine:.2f}) → +2 điểm")
    
    # Therapy-related factors
    if therapy_type == "combination":
        risk_score += 2
        risk_factors.append("Điều trị kết hợp → +2 điểm")
    
    if high_dose:
        risk_score += 2
        risk_factors.append("Liều cao → +2 điểm")
    
    if prior_anthracycline:
        risk_score += 2
        risk_factors.append("Tiền sử anthracycline → +2 điểm")
    
    if radiation_therapy:
        risk_score += 1
        risk_factors.append("Xạ trị trước đó → +1 điểm")
    
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
        "total_factors": len(risk_factors)
    }


def render():
    """Render HFA-ICOS Multiple Myeloma Risk Assessment interface"""
    st.set_page_config(page_title="HFA-ICOS Multiple Myeloma Risk", layout="wide")
    
    # Check for shared result
    shared = load_shared_result_from_url()
    
    st.markdown("""
    <h2 style='text-align: center; color: #10B981;'>❤️ HFA-ICOS Cardio-Oncology Risk Assessment</h2>
    <p style='text-align: center; color: #6B7280;'>
    Multiple Myeloma Therapies<br>
    Đánh giá nguy cơ tim mạch trước điều trị đa u tủy xương
    </p>
    """, unsafe_allow_html=True)
    
    with st.expander("ℹ️ Giới thiệu về HFA-ICOS Multiple Myeloma Risk Assessment"):
        st.markdown("""
        **HFA-ICOS Baseline Cardio-Oncology Risk Assessment for Multiple Myeloma Therapies** 
        là công cụ đánh giá nguy cơ tim mạch trước khi bắt đầu điều trị đa u tủy xương.
        
        ### Các yếu tố đánh giá:
        - **Bệnh tim mạch có sẵn:** Suy tim, nhồi máu cơ tim, bệnh mạch vành, bệnh van tim
        - **Yếu tố nguy cơ tim mạch:** Tăng huyết áp, đái tháo đường, rối loạn lipid máu
        - **Chức năng tim:** LVEF, BNP/NT-proBNP, troponin
        - **Chức năng thận:** eGFR, creatinine
        - **Loại điều trị:** Proteasome inhibitors, IMiDs, kháng thể đơn dòng, điều trị kết hợp
        
        ### Phân loại nguy cơ:
        - **Thấp (0-5 điểm):** Theo dõi tiêu chuẩn
        - **Trung bình (6-9 điểm):** Theo dõi tăng cường
        - **Cao (10-14 điểm):** Theo dõi chuyên sâu và tư vấn tim mạch
        - **Rất cao (≥15 điểm):** Cân nhắc điều trị thay thế hoặc bảo vệ tim mạch chuyên sâu
        
        ### Ứng dụng lâm sàng:
        - Phân tầng nguy cơ trước điều trị
        - Hướng dẫn cường độ theo dõi
        - Giúp lựa chọn điều trị phù hợp
        - Phòng ngừa biến chứng tim mạch
        """)
    
    # Input section
    st.markdown("### 📊 Thông tin bệnh nhân")
    
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.number_input(
            "Tuổi (năm)",
            min_value=18,
            max_value=120,
            value=65,
            step=1,
            key="hfa_icos_mm_age"
        )
    
    with col2:
        is_female = st.selectbox(
            "Giới tính",
            ["Nam", "Nữ"],
            key="hfa_icos_mm_sex"
        ) == "Nữ"
    
    # Pre-existing cardiovascular disease
    st.markdown("### ❤️ Bệnh tim mạch có sẵn")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        prior_heart_failure = st.checkbox("Tiền sử suy tim", key="hfa_icos_mm_hf")
        prior_myocardial_infarction = st.checkbox("Tiền sử nhồi máu cơ tim", key="hfa_icos_mm_mi")
        coronary_artery_disease = st.checkbox("Bệnh mạch vành", key="hfa_icos_mm_cad")
    
    with col2:
        atrial_fibrillation = st.checkbox("Rung nhĩ", key="hfa_icos_mm_afib")
        valvular_heart_disease = st.checkbox("Bệnh van tim", key="hfa_icos_mm_valve")
        cardiomyopathy = st.checkbox("Bệnh cơ tim", key="hfa_icos_mm_cm")
    
    with col3:
        prior_stroke = st.checkbox("Tiền sử đột quỵ", key="hfa_icos_mm_stroke")
    
    # Cardiovascular risk factors
    st.markdown("### 🔴 Yếu tố nguy cơ tim mạch")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        hypertension = st.checkbox("Tăng huyết áp", key="hfa_icos_mm_htn")
        diabetes = st.checkbox("Đái tháo đường", key="hfa_icos_mm_dm")
    
    with col2:
        dyslipidemia = st.checkbox("Rối loạn lipid máu", key="hfa_icos_mm_dyslipid")
        smoking = st.checkbox("Hút thuốc", key="hfa_icos_mm_smoking")
    
    with col3:
        obesity = st.checkbox("Béo phì (BMI ≥30)", key="hfa_icos_mm_obesity")
    
    # Cardiac function
    st.markdown("### 💓 Chức năng tim")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        lvef = st.number_input(
            "LVEF (%)",
            min_value=0.0,
            max_value=100.0,
            value=None,
            step=1.0,
            format="%.1f",
            key="hfa_icos_mm_lvef"
        )
    
    with col2:
        bnp = st.number_input(
            "BNP (pg/mL)",
            min_value=0.0,
            max_value=10000.0,
            value=None,
            step=1.0,
            format="%.1f",
            key="hfa_icos_mm_bnp"
        )
    
    with col3:
        nt_probnp = st.number_input(
            "NT-proBNP (pg/mL)",
            min_value=0.0,
            max_value=50000.0,
            value=None,
            step=1.0,
            format="%.1f",
            key="hfa_icos_mm_ntprobnp"
        )
    
    troponin_elevated = st.checkbox("Troponin tăng", key="hfa_icos_mm_troponin")
    
    # Renal function
    st.markdown("### 🫘 Chức năng thận")
    
    col1, col2 = st.columns(2)
    
    with col1:
        egfr = st.number_input(
            "eGFR (mL/min/1.73m²)",
            min_value=0.0,
            max_value=200.0,
            value=None,
            step=1.0,
            format="%.1f",
            key="hfa_icos_mm_egfr"
        )
    
    with col2:
        creatinine = st.number_input(
            "Creatinine (mg/dL)",
            min_value=0.0,
            max_value=10.0,
            value=None,
            step=0.1,
            format="%.2f",
            key="hfa_icos_mm_creat"
        )
    
    # Planned therapy
    st.markdown("### 💊 Điều trị dự kiến")
    
    col1, col2 = st.columns(2)
    
    with col1:
        therapy_type = st.selectbox(
            "Loại điều trị",
            ["proteasome_inhibitor", "imid", "monoclonal_ab", "combination"],
            format_func=lambda x: {
                "proteasome_inhibitor": "Proteasome Inhibitor",
                "imid": "IMiD (Immunomodulatory Drug)",
                "monoclonal_ab": "Monoclonal Antibody",
                "combination": "Điều trị kết hợp"
            }[x],
            key="hfa_icos_mm_therapy"
        )
    
    with col2:
        high_dose = st.checkbox("Liều cao", key="hfa_icos_mm_highdose")
    
    # Other factors
    st.markdown("### 📋 Yếu tố khác")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        prior_anthracycline = st.checkbox("Tiền sử anthracycline", key="hfa_icos_mm_anthra")
    
    with col2:
        radiation_therapy = st.checkbox("Xạ trị trước đó", key="hfa_icos_mm_rt")
    
    with col3:
        multiple_comorbidities = st.checkbox("Nhiều bệnh kèm theo", key="hfa_icos_mm_comorb")
    
    if st.button("🔬 Đánh giá nguy cơ", type="primary", use_container_width=True):
        # Validation
        errors = []
        if age < 18 or age > 120:
            errors.append("Tuổi phải từ 18-120")
        if lvef is not None and (lvef < 0 or lvef > 100):
            errors.append("LVEF phải từ 0-100%")
        if egfr is not None and (egfr < 0 or egfr > 200):
            errors.append("eGFR phải từ 0-200")
        
        if errors:
            render_validation_errors(errors)
        else:
            result = calculate_hfa_icos_multiple_myeloma(
                age=age,
                is_female=is_female,
                prior_heart_failure=prior_heart_failure,
                prior_myocardial_infarction=prior_myocardial_infarction,
                prior_stroke=prior_stroke,
                coronary_artery_disease=coronary_artery_disease,
                atrial_fibrillation=atrial_fibrillation,
                valvular_heart_disease=valvular_heart_disease,
                cardiomyopathy=cardiomyopathy,
                hypertension=hypertension,
                diabetes=diabetes,
                dyslipidemia=dyslipidemia,
                smoking=smoking,
                obesity=obesity,
                lvef=lvef,
                bnp=bnp,
                nt_probnp=nt_probnp,
                troponin_elevated=troponin_elevated,
                egfr=egfr,
                creatinine=creatinine,
                therapy_type=therapy_type,
                high_dose=high_dose,
                prior_anthracycline=prior_anthracycline,
                radiation_therapy=radiation_therapy,
                multiple_comorbidities=multiple_comorbidities
            )
            
            # Display results
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
            
            if result["risk_category"] == "Rất cao":
                st.markdown("""
                **Nguy cơ rất cao (≥15 điểm):**
                
                1. **Tư vấn tim mạch bắt buộc** trước khi bắt đầu điều trị
                2. **Cân nhắc điều trị thay thế** nếu có thể
                3. **Theo dõi chuyên sâu:**
                   - Siêu âm tim mỗi 3 tháng
                   - BNP/NT-proBNP mỗi chu kỳ điều trị
                   - Troponin trước mỗi chu kỳ
                   - ECG mỗi chu kỳ
                4. **Bảo vệ tim mạch:**
                   - ACEi/ARB nếu không chống chỉ định
                   - Beta-blocker nếu cần
                   - Statin nếu có chỉ định
                5. **Theo dõi sát triệu chứng suy tim**
                """)
            elif result["risk_category"] == "Cao":
                st.markdown("""
                **Nguy cơ cao (10-14 điểm):**
                
                1. **Tư vấn tim mạch** trước khi bắt đầu điều trị
                2. **Theo dõi tăng cường:**
                   - Siêu âm tim mỗi 6 tháng
                   - BNP/NT-proBNP mỗi 2-3 chu kỳ
                   - ECG mỗi 2-3 chu kỳ
                3. **Bảo vệ tim mạch:**
                   - Xem xét ACEi/ARB
                   - Kiểm soát các yếu tố nguy cơ
                4. **Theo dõi triệu chứng**
                """)
            elif result["risk_category"] == "Trung bình":
                st.markdown("""
                **Nguy cơ trung bình (6-9 điểm):**
                
                1. **Theo dõi tiêu chuẩn:**
                   - Siêu âm tim mỗi 6-12 tháng
                   - BNP/NT-proBNP mỗi 3-6 tháng
                   - ECG mỗi 3-6 tháng
                2. **Kiểm soát yếu tố nguy cơ:**
                   - Điều trị tăng huyết áp, đái tháo đường
                   - Kiểm soát lipid máu
                3. **Theo dõi triệu chứng**
                """)
            else:
                st.markdown("""
                **Nguy cơ thấp (0-5 điểm):**
                
                1. **Theo dõi tiêu chuẩn:**
                   - Siêu âm tim mỗi 12 tháng
                   - BNP/NT-proBNP mỗi 6-12 tháng
                   - ECG mỗi 6-12 tháng
                2. **Kiểm soát yếu tố nguy cơ cơ bản**
                3. **Theo dõi triệu chứng**
                """)
            
            # Save to history
            save_calculation_to_history(
                calculator_id="hfa_icos_multiple_myeloma",
                calculator_name="HFA-ICOS Multiple Myeloma Risk",
                inputs={
                    "Tuổi": f"{age}",
                    "Giới tính": "Nữ" if is_female else "Nam",
                    "Loại điều trị": therapy_type
                },
                result={
                    "Điểm nguy cơ": result["risk_score"],
                    "Phân loại": result["risk_category"]
                }
            )
            
            # Share and export
            render_share_section(
                calculator_id="hfa_icos_multiple_myeloma",
                calculator_name="HFA-ICOS Multiple Myeloma Risk"
            )
            
            render_export_section(
                calculator_id="hfa_icos_multiple_myeloma",
                calculator_name="HFA-ICOS Multiple Myeloma Risk",
                data={
                    "inputs": {
                        "age": age,
                        "sex": "female" if is_female else "male",
                        "therapy_type": therapy_type
                    },
                    "result": result
                }
            )
    
    # History
    render_history_ui(calculator_id="hfa_icos_multiple_myeloma", show_actions=True)
    
    # References
    references = get_references("HFA-ICOS Multiple Myeloma Risk")
    if references:
        render_references_section(references)

