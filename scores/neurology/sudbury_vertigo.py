"""
Sudbury Vertigo Risk Score
===========================

Identifies patients with vertigo who are at increased risk of a serious central diagnosis.

Reference:
- Kerber KA, et al. HINTS to diagnose stroke in the acute vestibular syndrome: 
  three-step bedside oculomotor examination more sensitive than early MRI diffusion-weighted imaging. 
  Stroke. 2009;40(11):3504-3510.
- Various studies on vertigo risk assessment

Sudbury Vertigo Risk Score Components:
- Age ≥60 years
- Headache
- Hypertension
- Diabetes
- Atrial fibrillation
- Focal neurological signs
- Abnormal gait/ataxia
- Nystagmus (central pattern)

Total: 0-8 points

Risk Categories:
- Low risk (0-2 points): Likely peripheral vertigo
- Moderate risk (3-4 points): Need further evaluation
- High risk (≥5 points): High suspicion of central cause

Clinical Utility:
- Early identification of central vertigo
- Guides need for neuroimaging
- Helps differentiate peripheral vs central vertigo
- Used in emergency and neurology
"""

import streamlit as st
from config.theme import COLORS
from scores.utils.validation import validate_age
from components.ui.scoring import render_score_result
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
from components.export import render_export_section
# ======================================


def calculate_sudbury_vertigo_risk(
    age: int,
    headache: bool,
    hypertension: bool,
    diabetes: bool,
    atrial_fibrillation: bool,
    focal_neurological_signs: bool,
    abnormal_gait: bool,
    central_nystagmus: bool
) -> dict:
    """
    Calculate Sudbury Vertigo Risk Score
    
    Args:
        age: Age (years)
        headache: Headache present
        hypertension: Hypertension
        diabetes: Diabetes mellitus
        atrial_fibrillation: Atrial fibrillation
        focal_neurological_signs: Focal neurological signs
        abnormal_gait: Abnormal gait/ataxia
        central_nystagmus: Central pattern nystagmus
    
    Returns:
        Dictionary with score, risk category, and recommendation
    """
    score = 0
    details = []
    
    # Age ≥60
    if age >= 60:
        score += 1
        details.append(f"Tuổi {age} (≥60) → +1 điểm")
    else:
        details.append(f"Tuổi {age} (<60) → 0 điểm")
    
    # Headache
    if headache:
        score += 1
        details.append("Đau đầu → +1 điểm")
    else:
        details.append("Không đau đầu → 0 điểm")
    
    # Hypertension
    if hypertension:
        score += 1
        details.append("Tăng huyết áp → +1 điểm")
    else:
        details.append("Không tăng huyết áp → 0 điểm")
    
    # Diabetes
    if diabetes:
        score += 1
        details.append("Đái tháo đường → +1 điểm")
    else:
        details.append("Không đái tháo đường → 0 điểm")
    
    # Atrial fibrillation
    if atrial_fibrillation:
        score += 1
        details.append("Rung nhĩ → +1 điểm")
    else:
        details.append("Không rung nhĩ → 0 điểm")
    
    # Focal neurological signs
    if focal_neurological_signs:
        score += 1
        details.append("Dấu hiệu thần kinh khu trú → +1 điểm")
    else:
        details.append("Không có dấu hiệu thần kinh khu trú → 0 điểm")
    
    # Abnormal gait/ataxia
    if abnormal_gait:
        score += 1
        details.append("Dáng đi bất thường/ataxia → +1 điểm")
    else:
        details.append("Dáng đi bình thường → 0 điểm")
    
    # Central nystagmus
    if central_nystagmus:
        score += 1
        details.append("Rung giật nhãn cầu kiểu trung ương → +1 điểm")
    else:
        details.append("Không có rung giật nhãn cầu kiểu trung ương → 0 điểm")
    
    # Risk category
    if score <= 2:
        risk_category = "Nguy cơ thấp"
        interpretation = "Có khả năng chóng mặt ngoại biên"
        recommendation = "Điều trị chóng mặt ngoại biên, theo dõi"
    elif score <= 4:
        risk_category = "Nguy cơ trung bình"
        interpretation = "Cần đánh giá thêm để loại trừ nguyên nhân trung ương"
        recommendation = "Đánh giá thần kinh, cân nhắc chụp CT/MRI"
    else:
        risk_category = "Nguy cơ cao"
        interpretation = "Nghi ngờ cao nguyên nhân trung ương (đột quỵ, u não)"
        recommendation = "Chụp CT/MRI não khẩn cấp, đánh giá thần kinh ngay"
    
    return {
        "score": score,
        "risk_category": risk_category,
        "interpretation": interpretation,
        "recommendation": recommendation,
        "details": details
    }


def render():
    """Render Sudbury Vertigo Risk Score interface"""
    import streamlit as st
    
    # st.set_page_config(page_title="Sudbury Vertigo Risk Score", layout="wide")
    
    # Check for shared result
    shared = load_shared_result_from_url()
    
    st.markdown(f"""
    <h3 style='text-align: center; color: {COLORS['success']};'>🧠 Sudbury Vertigo Risk Score</h3>
    <p style='text-align: center; color: #6B7280;'>
    Xác định bệnh nhân chóng mặt có nguy cơ tăng cao chẩn đoán trung ương nghiêm trọng
    </p>
    """, unsafe_allow_html=True)
    
    with st.expander("ℹ️ Giới thiệu về Sudbury Vertigo Risk Score"):
        st.markdown("""
        **Sudbury Vertigo Risk Score** là công cụ xác định bệnh nhân chóng mặt có nguy cơ tăng cao 
        chẩn đoán trung ương nghiêm trọng (như đột quỵ, u não).
        
        ### Các yếu tố nguy cơ (8 yếu tố):
        1. Tuổi ≥60
        2. Đau đầu
        3. Tăng huyết áp
        4. Đái tháo đường
        5. Rung nhĩ
        6. Dấu hiệu thần kinh khu trú
        7. Dáng đi bất thường/ataxia
        8. Rung giật nhãn cầu kiểu trung ương
        
        ### Phân loại nguy cơ:
        - **0-2 điểm:** Nguy cơ thấp - Có khả năng chóng mặt ngoại biên
        - **3-4 điểm:** Nguy cơ trung bình - Cần đánh giá thêm
        - **≥5 điểm:** Nguy cơ cao - Nghi ngờ cao nguyên nhân trung ương
        
        ### Ứng dụng lâm sàng:
        - Xác định sớm chóng mặt trung ương
        - Hướng dẫn nhu cầu chụp hình ảnh thần kinh
        - Giúp phân biệt chóng mặt ngoại biên vs trung ương
        - Dùng trong cấp cứu và thần kinh
        """)
    
    # Input section
    st.markdown("### 📊 Thông tin bệnh nhân")
    
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.number_input(
            "Tuổi (năm)",
            min_value=18,
            max_value=120,
            value=60,
            step=1,
            key="sudbury_age"
        )
        
        headache = st.checkbox(
            "Đau đầu",
            key="sudbury_headache"
        )
        
        hypertension = st.checkbox(
            "Tăng huyết áp",
            key="sudbury_htn"
        )
        
        diabetes = st.checkbox(
            "Đái tháo đường",
            key="sudbury_diabetes"
        )
    
    with col2:
        atrial_fibrillation = st.checkbox(
            "Rung nhĩ",
            key="sudbury_afib"
        )
        
        focal_neurological_signs = st.checkbox(
            "Dấu hiệu thần kinh khu trú",
            key="sudbury_focal",
            help="Yếu liệt, tê bì, rối loạn ngôn ngữ, v.v."
        )
        
        abnormal_gait = st.checkbox(
            "Dáng đi bất thường/ataxia",
            key="sudbury_gait"
        )
        
        central_nystagmus = st.checkbox(
            "Rung giật nhãn cầu kiểu trung ương",
            key="sudbury_nystagmus",
            help="Rung giật nhãn cầu dọc, thay đổi hướng, hoặc không bị ức chế bởi cố định mắt"
        )
    
    if st.button("🔬 Tính điểm Sudbury Vertigo Risk", type="primary", use_container_width=True):
        # Validation
        errors = []
        if age < 18 or age > 120:
            errors.append("Tuổi phải từ 18-120")
        
        if errors:
            render_validation_errors(errors)
        else:
            result = calculate_sudbury_vertigo_risk(
                age=age,
                headache=headache,
                hypertension=hypertension,
                diabetes=diabetes,
                atrial_fibrillation=atrial_fibrillation,
                focal_neurological_signs=focal_neurological_signs,
                abnormal_gait=abnormal_gait,
                central_nystagmus=central_nystagmus
            )
            
            # Display results
            st.markdown("---")
            st.subheader("📋 Kết quả")
            
            if result['score'] <= 2:
                color = COLORS["success"]
                icon = "✅"
            elif result['score'] <= 4:
                color = COLORS["warning"]
                icon = "⚠️"
            else:
                color = COLORS["error"]
                icon = "🚨"

            render_score_result(
                title="Sudbury Vertigo Risk Score",
                score=result['score'],
                interpretation=f"{result['risk_category']}\n({result['interpretation']})",
                color=color,
                icon=icon
            )
            
            # Details
            st.markdown("### 📝 Chi tiết tính điểm")
            for detail in result['details']:
                st.markdown(f"- {detail}")
            
            # Interpretation
            st.markdown("### 💡 Diễn giải và khuyến nghị")
            
            if result['score'] <= 2:
                st.success(f"**{result['risk_category']}** - {result['interpretation']}")
                st.markdown(f"**Khuyến nghị:** {result['recommendation']}")
                st.markdown("""
                **Điều trị:**
                - Điều trị chóng mặt ngoại biên (ví dụ: viêm tiền đình)
                - Thuốc chống nôn, chống chóng mặt
                - Vật lý trị liệu tiền đình nếu cần
                - Theo dõi tại nhà
                
                **Lưu ý:** Nếu triệu chứng không cải thiện hoặc xấu đi, đánh giá lại
                """)
            elif result['score'] <= 4:
                st.warning(f"**{result['risk_category']}** - {result['interpretation']}")
                st.markdown(f"**Khuyến nghị:** {result['recommendation']}")
                st.markdown("""
                **Hành động:**
                - Đánh giá thần kinh đầy đủ
                - Cân nhắc chụp CT/MRI não
                - Đánh giá HINTS exam nếu có thể
                - Theo dõi sát tại bệnh viện
                - Tư vấn thần kinh nếu cần
                
                **Lưu ý:** Không được bỏ sót đột quỵ tiểu não hoặc thân não
                """)
            else:
                st.error(f"**{result['risk_category']}** - {result['interpretation']}")
                st.markdown(f"**Khuyến nghị:** {result['recommendation']}")
                st.markdown("""
                **Hành động ngay:**
                - **Chụp CT/MRI não khẩn cấp**
                - Đánh giá thần kinh toàn diện
                - Tư vấn thần kinh ngay
                - Cân nhắc điều trị đột quỵ nếu phù hợp
                - Theo dõi tại ICU nếu cần
                
                **Nguyên nhân có thể:**
                - Đột quỵ tiểu não/thân não
                - U não
                - Xuất huyết nội sọ
                - Bệnh lý mạch máu trung ương khác
                """)
            
            # Save to history
            save_calculation_to_history(
                calculator_id="sudbury_vertigo",
                calculator_name="Sudbury Vertigo Risk Score",
                inputs={
                    "Tuổi": f"{age}",
                    "Đau đầu": "Có" if headache else "Không",
                    "Tăng huyết áp": "Có" if hypertension else "Không",
                    "Đái tháo đường": "Có" if diabetes else "Không",
                    "Rung nhĩ": "Có" if atrial_fibrillation else "Không",
                    "Dấu hiệu TK khu trú": "Có" if focal_neurological_signs else "Không",
                    "Dáng đi bất thường": "Có" if abnormal_gait else "Không",
                    "Rung giật nhãn cầu trung ương": "Có" if central_nystagmus else "Không"
                },
                result={
                    "Điểm": f"{result['score']}/8",
                    "Nguy cơ": result['risk_category']
                }
            )
            
            # Share and export
            render_share_section(
                calculator_id="sudbury_vertigo",
                calculator_name="Sudbury Vertigo Risk Score"
            )
            
            render_export_section(
                calculator_id="sudbury_vertigo",
                calculator_name="Sudbury Vertigo Risk Score",
                data={
                    "inputs": {
                        "age": age,
                        "headache": headache,
                        "hypertension": hypertension,
                        "diabetes": diabetes,
                        "atrial_fibrillation": atrial_fibrillation,
                        "focal_neurological_signs": focal_neurological_signs,
                        "abnormal_gait": abnormal_gait,
                        "central_nystagmus": central_nystagmus
                    },
                    "result": result
                }
            )
    
    # History
    render_history_ui(calculator_id="sudbury_vertigo", show_actions=True)
    
    # References
    references = get_references("Sudbury Vertigo Risk Score")
    if references:
        render_references_section(references)

