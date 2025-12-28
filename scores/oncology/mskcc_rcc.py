"""
MSKCC (Memorial Sloan-Kettering Cancer Center) Risk of Recurrence for Renal Cell Carcinoma
========================================================================================

Predicts risk of recurrence after nephrectomy for localized renal cell carcinoma (RCC).

Reference:
- Kattan MW, et al. A postoperative prognostic nomogram for renal cell carcinoma. 
  J Urol. 2001;166(1):63-67.
- Motzer RJ, et al. Survival and prognostic stratification of 670 patients with 
  advanced renal cell carcinoma. J Clin Oncol. 1999;17(8):2530-2540.

MSKCC Risk Factors:
- T stage (T1, T2, T3a, T3b, T3c, T4)
- Tumor size
- Histologic subtype (clear cell, papillary, chromophobe, etc.)
- Fuhrman grade (1-4)
- Symptoms at presentation
- Performance status

Risk Categories:
- Low Risk: 0-1 risk factors
- Intermediate Risk: 2 risk factors
- High Risk: 3+ risk factors

Clinical Utility:
- Post-nephrectomy risk stratification
- Guides surveillance intensity
- Helps determine need for adjuvant therapy
- Used in urologic oncology
"""

import streamlit as st
from scores.utils.validation import validate_age
from components.ui.validation import render_validation_errors
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
from components.export import render_export_section
# ======================================


def calculate_mskcc_rcc(
    t_stage: str,  # T1, T2, T3a, T3b, T3c, T4
    tumor_size: float,  # cm
    histologic_subtype: str,  # clear_cell, papillary, chromophobe, other
    fuhrman_grade: int,  # 1-4
    symptoms_at_presentation: bool = False,
    performance_status: int = 0,  # ECOG 0-4
    age: int = None
) -> dict:
    """
    Calculate MSKCC Risk of Recurrence for RCC
    
    Args:
        t_stage: T stage (T1, T2, T3a, T3b, T3c, T4)
        tumor_size: Tumor size (cm)
        histologic_subtype: Histologic subtype
        fuhrman_grade: Fuhrman grade (1-4)
        symptoms_at_presentation: Symptoms at presentation
        performance_status: ECOG performance status (0-4)
        age: Age (years)
    
    Returns:
        Dictionary with risk category, score, and recommendations
    """
    risk_factors = []
    risk_score = 0
    
    # T stage
    t_stage_points = {
        "T1": 0,
        "T2": 1,
        "T3a": 2,
        "T3b": 3,
        "T3c": 3,
        "T4": 4
    }
    
    if t_stage in t_stage_points:
        points = t_stage_points[t_stage]
        if points > 0:
            risk_score += points
            risk_factors.append(f"T stage {t_stage} → +{points} điểm")
    
    # Tumor size
    if tumor_size >= 10:
        risk_score += 2
        risk_factors.append(f"Kích thước u ≥10 cm ({tumor_size} cm) → +2 điểm")
    elif tumor_size >= 7:
        risk_score += 1
        risk_factors.append(f"Kích thước u 7-9.9 cm ({tumor_size} cm) → +1 điểm")
    
    # Histologic subtype
    if histologic_subtype == "clear_cell":
        # Clear cell is standard, no additional points
        pass
    elif histologic_subtype in ["papillary", "chromophobe"]:
        # Generally better prognosis
        pass
    else:
        # Other subtypes may have different prognosis
        risk_score += 1
        risk_factors.append(f"Loại mô học: {histologic_subtype} → +1 điểm")
    
    # Fuhrman grade
    if fuhrman_grade >= 4:
        risk_score += 2
        risk_factors.append(f"Fuhrman grade {fuhrman_grade} → +2 điểm")
    elif fuhrman_grade == 3:
        risk_score += 1
        risk_factors.append(f"Fuhrman grade {fuhrman_grade} → +1 điểm")
    
    # Symptoms at presentation
    if symptoms_at_presentation:
        risk_score += 1
        risk_factors.append("Có triệu chứng khi chẩn đoán → +1 điểm")
    
    # Performance status
    if performance_status >= 2:
        risk_score += 1
        risk_factors.append(f"ECOG ≥2 ({performance_status}) → +1 điểm")
    
    # Age (older age may be a factor)
    if age and age >= 75:
        risk_score += 1
        risk_factors.append(f"Tuổi ≥75 ({age} tuổi) → +1 điểm")
    
    # Determine risk category
    if risk_score <= 1:
        risk_category = "Thấp"
        risk_color = "success"
        risk_icon = "🟢"
        recurrence_risk = "5-10%"
    elif risk_score == 2:
        risk_category = "Trung bình"
        risk_color = "info"
        risk_icon = "🟡"
        recurrence_risk = "15-25%"
    else:  # risk_score >= 3
        risk_category = "Cao"
        risk_color = "warning"
        risk_icon = "🟠"
        recurrence_risk = "30-50%"
    
    return {
        "risk_score": risk_score,
        "risk_category": risk_category,
        "risk_color": risk_color,
        "risk_icon": risk_icon,
        "recurrence_risk": recurrence_risk,
        "risk_factors": risk_factors,
        "total_factors": len(risk_factors)
    }


def render():
    """Render MSKCC RCC Risk of Recurrence interface"""
    st.set_page_config(page_title="MSKCC RCC Risk", layout="wide")
    
    shared = load_shared_result_from_url()
    
    st.markdown("""
    <h2 style='text-align: center; color: #10B981;'>🎗️ MSKCC Risk of Recurrence</h2>
    <p style='text-align: center; color: #6B7280;'>
    Renal Cell Carcinoma (RCC)<br>
    Dự đoán nguy cơ tái phát sau cắt thận ở ung thư thận
    </p>
    """, unsafe_allow_html=True)
    
    with st.expander("ℹ️ Giới thiệu về MSKCC Risk of Recurrence"):
        st.markdown("""
        **MSKCC (Memorial Sloan-Kettering Cancer Center) Risk of Recurrence** 
        dự đoán nguy cơ tái phát sau cắt thận ở bệnh nhân ung thư thận khu trú.
        
        ### Các yếu tố nguy cơ:
        - **T stage:** Giai đoạn T (T1-T4)
        - **Kích thước u:** Đường kính lớn nhất (cm)
        - **Loại mô học:** Clear cell, papillary, chromophobe, khác
        - **Fuhrman grade:** Độ biệt hóa (1-4)
        - **Triệu chứng khi chẩn đoán:** Có/không
        - **Thể trạng (ECOG):** 0-4
        
        ### Phân loại nguy cơ:
        - **Thấp (0-1 điểm):** Nguy cơ tái phát 5-10%
        - **Trung bình (2 điểm):** Nguy cơ tái phát 15-25%
        - **Cao (≥3 điểm):** Nguy cơ tái phát 30-50%
        
        ### Ứng dụng lâm sàng:
        - Phân tầng nguy cơ sau cắt thận
        - Hướng dẫn cường độ theo dõi
        - Giúp quyết định điều trị bổ trợ
        - Dùng trong ung thư học tiết niệu
        """)
    
    st.markdown("### 📊 Thông tin bệnh nhân")
    
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.number_input(
            "Tuổi (năm)",
            min_value=18,
            max_value=120,
            value=65,
            step=1,
            key="mskcc_age"
        )
    
    with col2:
        performance_status = st.selectbox(
            "ECOG Performance Status",
            [0, 1, 2, 3, 4],
            format_func=lambda x: f"ECOG {x}",
            key="mskcc_ecog"
        )
    
    st.markdown("### 🔬 Thông tin khối u")
    
    col1, col2 = st.columns(2)
    
    with col1:
        t_stage = st.selectbox(
            "T Stage",
            ["T1", "T2", "T3a", "T3b", "T3c", "T4"],
            key="mskcc_tstage"
        )
    
    with col2:
        tumor_size = st.number_input(
            "Kích thước u (cm)",
            min_value=0.1,
            max_value=30.0,
            value=5.0,
            step=0.1,
            format="%.1f",
            key="mskcc_size"
        )
    
    col3, col4 = st.columns(2)
    
    with col3:
        histologic_subtype = st.selectbox(
            "Loại mô học",
            ["clear_cell", "papillary", "chromophobe", "other"],
            format_func=lambda x: {
                "clear_cell": "Clear Cell",
                "papillary": "Papillary",
                "chromophobe": "Chromophobe",
                "other": "Khác"
            }[x],
            key="mskcc_histo"
        )
    
    with col4:
        fuhrman_grade = st.selectbox(
            "Fuhrman Grade",
            [1, 2, 3, 4],
            key="mskcc_grade"
        )
    
    symptoms_at_presentation = st.checkbox(
        "Có triệu chứng khi chẩn đoán",
        key="mskcc_symptoms"
    )
    
    if st.button("🔬 Tính toán nguy cơ", type="primary", use_container_width=True):
        errors = []
        if age < 18 or age > 120:
            errors.append("Tuổi phải từ 18-120")
        if tumor_size < 0.1 or tumor_size > 30:
            errors.append("Kích thước u phải từ 0.1-30 cm")
        if fuhrman_grade < 1 or fuhrman_grade > 4:
            errors.append("Fuhrman grade phải từ 1-4")
        
        if errors:
            render_validation_errors(errors)
        else:
            result = calculate_mskcc_rcc(
                t_stage=t_stage,
                tumor_size=tumor_size,
                histologic_subtype=histologic_subtype,
                fuhrman_grade=fuhrman_grade,
                symptoms_at_presentation=symptoms_at_presentation,
                performance_status=performance_status,
                age=age
            )
            
            st.markdown("---")
            st.markdown("### 📋 Kết quả đánh giá nguy cơ")
            
            if result["risk_category"] == "Cao":
                st.warning(f"{result['risk_icon']} **NGUY CƠ CAO** - Điểm số: {result['risk_score']}")
            elif result["risk_category"] == "Trung bình":
                st.info(f"{result['risk_icon']} **NGUY CƠ TRUNG BÌNH** - Điểm số: {result['risk_score']}")
            else:
                st.success(f"{result['risk_icon']} **NGUY CƠ THẤP** - Điểm số: {result['risk_score']}")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.metric("Tổng điểm nguy cơ", f"{result['risk_score']}")
            
            with col2:
                st.metric("Nguy cơ tái phát", result["recurrence_risk"])
            
            if result['risk_factors']:
                st.markdown("**Các yếu tố nguy cơ:**")
                for factor in result['risk_factors']:
                    st.markdown(f"- {factor}")
            
            # Clinical recommendations
            st.markdown("### 💡 Khuyến nghị lâm sàng")
            
            if result["risk_category"] == "Cao":
                st.markdown("""
                **Nguy cơ cao (≥3 điểm):**
                
                1. **Theo dõi chuyên sâu:**
                   - CT scan ngực/bụng mỗi 3-6 tháng trong 2 năm đầu
                   - Sau đó mỗi 6-12 tháng đến 5 năm
                   - Xét nghiệm chức năng thận định kỳ
                
                2. **Cân nhắc điều trị bổ trợ:**
                   - Xem xét liệu pháp miễn dịch bổ trợ (nếu phù hợp)
                   - Thảo luận với bệnh nhân về lợi ích/nguy cơ
                
                3. **Theo dõi triệu chứng:**
                   - Giáo dục bệnh nhân về dấu hiệu tái phát
                   - Tái khám định kỳ
                """)
            elif result["risk_category"] == "Trung bình":
                st.markdown("""
                **Nguy cơ trung bình (2 điểm):**
                
                1. **Theo dõi tiêu chuẩn:**
                   - CT scan ngực/bụng mỗi 6 tháng trong 2 năm đầu
                   - Sau đó mỗi 12 tháng đến 5 năm
                   - Xét nghiệm chức năng thận định kỳ
                
                2. **Theo dõi triệu chứng:**
                   - Tái khám định kỳ
                   - Giáo dục bệnh nhân về dấu hiệu tái phát
                """)
            else:
                st.markdown("""
                **Nguy cơ thấp (0-1 điểm):**
                
                1. **Theo dõi tiêu chuẩn:**
                   - CT scan ngực/bụng mỗi 12 tháng trong 3-5 năm
                   - Xét nghiệm chức năng thận định kỳ
                
                2. **Theo dõi triệu chứng:**
                   - Tái khám định kỳ
                   - Giáo dục bệnh nhân về dấu hiệu tái phát
                """)
            
            save_calculation_to_history(
                calculator_id="mskcc_rcc",
                calculator_name="MSKCC RCC Risk",
                inputs={
                    "T Stage": t_stage,
                    "Kích thước u": f"{tumor_size} cm",
                    "Fuhrman grade": f"{fuhrman_grade}",
                    "Loại mô học": histologic_subtype
                },
                result={
                    "Điểm nguy cơ": result["risk_score"],
                    "Phân loại": result["risk_category"],
                    "Nguy cơ tái phát": result["recurrence_risk"]
                }
            )
            
            render_share_section(
                calculator_id="mskcc_rcc",
                calculator_name="MSKCC RCC Risk"
            )
            
            render_export_section(
                calculator_id="mskcc_rcc",
                calculator_name="MSKCC RCC Risk",
                data={
                    "inputs": {
                        "t_stage": t_stage,
                        "tumor_size": tumor_size,
                        "histologic_subtype": histologic_subtype,
                        "fuhrman_grade": fuhrman_grade
                    },
                    "result": result
                }
            )
    
    render_history_ui(calculator_id="mskcc_rcc", show_actions=True)
    
    references = get_references("MSKCC RCC Risk")
    if references:
        render_references_section(references)

