"""
GMAWS (Glasgow Modified Alcohol Withdrawal Scale)
==================================================

Assesses and monitors severity of alcohol withdrawal symptoms (AWS).

Reference:
- Shaw GK, et al. Detoxification: the use of benzodiazepines. 
  Alcohol Alcohol. 1995;30(6):765-770.
- Various studies on alcohol withdrawal assessment

GMAWS Components (10 items):
1. Agitation
2. Orientation
3. Hallucinations
4. Tremor
5. Sweating
6. Nausea/Vomiting
7. Anxiety
8. Paroxysmal sweats
9. Tactile disturbances
10. Auditory disturbances

Each item scored 0-7 points
Total: 0-70 points

Severity Categories:
- 0-9: Mild withdrawal
- 10-19: Moderate withdrawal
- 20-29: Severe withdrawal
- ≥30: Very severe withdrawal (risk of seizures/DTS)

Clinical Utility:
- Standardized assessment of alcohol withdrawal
- Guides benzodiazepine dosing
- Monitors treatment response
- Used in emergency and psychiatry
- Helps prevent complications (seizures, DTS)
"""

import streamlit as st
from components.ui.validation import render_validation_errors
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
from components.export import render_export_section
# ======================================


def calculate_gmaws(
    agitation: int,
    orientation: int,
    hallucinations: int,
    tremor: int,
    sweating: int,
    nausea_vomiting: int,
    anxiety: int,
    paroxysmal_sweats: int,
    tactile_disturbances: int,
    auditory_disturbances: int
) -> dict:
    """
    Calculate GMAWS Score
    
    Args:
        agitation: Agitation score (0-7)
        orientation: Orientation score (0-7)
        hallucinations: Hallucinations score (0-7)
        tremor: Tremor score (0-7)
        sweating: Sweating score (0-7)
        nausea_vomiting: Nausea/Vomiting score (0-7)
        anxiety: Anxiety score (0-7)
        paroxysmal_sweats: Paroxysmal sweats score (0-7)
        tactile_disturbances: Tactile disturbances score (0-7)
        auditory_disturbances: Auditory disturbances score (0-7)
    
    Returns:
        Dictionary with GMAWS score, severity, and treatment recommendation
    """
    total_score = (
        agitation +
        orientation +
        hallucinations +
        tremor +
        sweating +
        nausea_vomiting +
        anxiety +
        paroxysmal_sweats +
        tactile_disturbances +
        auditory_disturbances
    )
    
    # Severity categories
    if total_score < 10:
        severity = "Nhẹ"
        interpretation = "Triệu chứng cai rượu nhẹ"
        recommendation = "Theo dõi, điều trị triệu chứng nhẹ"
        benzodiazepine = "Không cần hoặc liều thấp"
    elif total_score < 20:
        severity = "Trung bình"
        interpretation = "Triệu chứng cai rượu trung bình"
        recommendation = "Điều trị benzodiazepine, theo dõi sát"
        benzodiazepine = "Liều trung bình (ví dụ: chlordiazepoxide 25-50mg q6h)"
    elif total_score < 30:
        severity = "Nặng"
        interpretation = "Triệu chứng cai rượu nặng"
        recommendation = "Điều trị benzodiazepine tích cực, theo dõi ICU"
        benzodiazepine = "Liều cao (ví dụ: chlordiazepoxide 50-100mg q4-6h)"
    else:
        severity = "Rất nặng"
        interpretation = "Triệu chứng cai rượu rất nặng - Nguy cơ co giật/DTS"
        recommendation = "Điều trị tích cực tại ICU, phòng ngừa co giật"
        benzodiazepine = "Liều rất cao (ví dụ: chlordiazepoxide 100mg q2-4h hoặc diazepam IV)"
    
    return {
        "total_score": total_score,
        "severity": severity,
        "interpretation": interpretation,
        "recommendation": recommendation,
        "benzodiazepine": benzodiazepine,
        "risk_seizures": total_score >= 30
    }


def render():
    """Render GMAWS interface"""
    import streamlit as st
    
    st.set_page_config(page_title="GMAWS", layout="wide")
    
    # Check for shared result
    shared = load_shared_result_from_url()
    
    st.markdown("""
    <h2 style='text-align: center; color: #10B981;'>🧠 GMAWS</h2>
    <p style='text-align: center; color: #6B7280;'>
    Glasgow Modified Alcohol Withdrawal Scale<br>
    Đánh giá và theo dõi mức độ nặng của các triệu chứng cai rượu (AWS)
    </p>
    """, unsafe_allow_html=True)
    
    with st.expander("ℹ️ Giới thiệu về GMAWS"):
        st.markdown("""
        **GMAWS (Glasgow Modified Alcohol Withdrawal Scale)** là thang điểm đánh giá 
        và theo dõi mức độ nặng của các triệu chứng cai rượu (AWS).
        
        ### Các thành phần (10 mục, mỗi mục 0-7 điểm):
        1. **Agitation (Bồn chồn):** 0-7
        2. **Orientation (Định hướng):** 0-7
        3. **Hallucinations (Ảo giác):** 0-7
        4. **Tremor (Run):** 0-7
        5. **Sweating (Đổ mồ hôi):** 0-7
        6. **Nausea/Vomiting (Buồn nôn/Nôn):** 0-7
        7. **Anxiety (Lo âu):** 0-7
        8. **Paroxysmal Sweats (Đổ mồ hôi từng cơn):** 0-7
        9. **Tactile Disturbances (Rối loạn xúc giác):** 0-7
        10. **Auditory Disturbances (Rối loạn thính giác):** 0-7
        
        ### Phân loại mức độ:
        - **0-9 điểm:** Nhẹ
        - **10-19 điểm:** Trung bình
        - **20-29 điểm:** Nặng
        - **≥30 điểm:** Rất nặng (nguy cơ co giật/DTS)
        
        ### Ứng dụng lâm sàng:
        - Đánh giá chuẩn hóa cai rượu
        - Hướng dẫn liều benzodiazepine
        - Theo dõi đáp ứng điều trị
        - Dùng trong cấp cứu và tâm thần
        - Giúp phòng ngừa biến chứng (co giật, DTS)
        """)
    
    # Input section
    st.markdown("### 📊 Đánh giá triệu chứng (mỗi mục 0-7 điểm)")
    
    st.markdown("**Hướng dẫn:** 0 = Không có, 1-3 = Nhẹ, 4-5 = Trung bình, 6-7 = Nặng")
    
    col1, col2 = st.columns(2)
    
    with col1:
        agitation = st.slider(
            "1. Agitation (Bồn chồn)",
            min_value=0,
            max_value=7,
            value=0,
            step=1,
            key="gmaws_agitation"
        )
        
        orientation = st.slider(
            "2. Orientation (Định hướng)",
            min_value=0,
            max_value=7,
            value=0,
            step=1,
            key="gmaws_orientation",
            help="0 = Định hướng tốt, 7 = Rất lú lẫn"
        )
        
        hallucinations = st.slider(
            "3. Hallucinations (Ảo giác)",
            min_value=0,
            max_value=7,
            value=0,
            step=1,
            key="gmaws_hallucinations"
        )
        
        tremor = st.slider(
            "4. Tremor (Run)",
            min_value=0,
            max_value=7,
            value=0,
            step=1,
            key="gmaws_tremor"
        )
        
        sweating = st.slider(
            "5. Sweating (Đổ mồ hôi)",
            min_value=0,
            max_value=7,
            value=0,
            step=1,
            key="gmaws_sweating"
        )
    
    with col2:
        nausea_vomiting = st.slider(
            "6. Nausea/Vomiting (Buồn nôn/Nôn)",
            min_value=0,
            max_value=7,
            value=0,
            step=1,
            key="gmaws_nausea"
        )
        
        anxiety = st.slider(
            "7. Anxiety (Lo âu)",
            min_value=0,
            max_value=7,
            value=0,
            step=1,
            key="gmaws_anxiety"
        )
        
        paroxysmal_sweats = st.slider(
            "8. Paroxysmal Sweats (Đổ mồ hôi từng cơn)",
            min_value=0,
            max_value=7,
            value=0,
            step=1,
            key="gmaws_paroxysmal"
        )
        
        tactile_disturbances = st.slider(
            "9. Tactile Disturbances (Rối loạn xúc giác)",
            min_value=0,
            max_value=7,
            value=0,
            step=1,
            key="gmaws_tactile",
            help="Cảm giác bò, ngứa, nóng rát"
        )
        
        auditory_disturbances = st.slider(
            "10. Auditory Disturbances (Rối loạn thính giác)",
            min_value=0,
            max_value=7,
            value=0,
            step=1,
            key="gmaws_auditory",
            help="Nghe thấy tiếng động, giọng nói"
        )
    
    if st.button("🔬 Tính điểm GMAWS", type="primary", use_container_width=True):
        result = calculate_gmaws(
            agitation=agitation,
            orientation=orientation,
            hallucinations=hallucinations,
            tremor=tremor,
            sweating=sweating,
            nausea_vomiting=nausea_vomiting,
            anxiety=anxiety,
            paroxysmal_sweats=paroxysmal_sweats,
            tactile_disturbances=tactile_disturbances,
            auditory_disturbances=auditory_disturbances
        )
        
        # Display results
        st.markdown("---")
        st.markdown("### 📋 Kết quả GMAWS")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric("Điểm GMAWS", f"{result['total_score']}/70")
        
        with col2:
            st.metric(
                "Mức độ",
                result['severity']
            )
        
        # Interpretation
        st.markdown("### 💡 Diễn giải và khuyến nghị điều trị")
        
        if result['total_score'] < 10:
            st.success(f"**{result['severity']}** - {result['interpretation']}")
            st.markdown(f"**Khuyến nghị:** {result['recommendation']}")
            st.markdown(f"**Benzodiazepine:** {result['benzodiazepine']}")
        elif result['total_score'] < 20:
            st.info(f"**{result['severity']}** - {result['interpretation']}")
            st.markdown(f"**Khuyến nghị:** {result['recommendation']}")
            st.markdown(f"**Benzodiazepine:** {result['benzodiazepine']}")
            st.markdown("""
            - Theo dõi sát mỗi 4-6 giờ
            - Điều chỉnh liều theo triệu chứng
            - Bổ sung thiamin, folate, multivitamin
            """)
        elif result['total_score'] < 30:
            st.warning(f"**{result['severity']}** - {result['interpretation']}")
            st.markdown(f"**Khuyến nghị:** {result['recommendation']}")
            st.markdown(f"**Benzodiazepine:** {result['benzodiazepine']}")
            st.markdown("""
            - **Theo dõi tại ICU hoặc đơn vị chuyên khoa**
            - Điều trị benzodiazepine tích cực
            - Theo dõi sát mỗi 2-4 giờ
            - Phòng ngừa co giật
            - Bổ sung thiamin, folate
            - Điều trị hỗ trợ
            """)
        else:
            st.error(f"**{result['severity']}** - {result['interpretation']}")
            st.markdown(f"**Khuyến nghị:** {result['recommendation']}")
            st.markdown(f"**Benzodiazepine:** {result['benzodiazepine']}")
            st.markdown("""
            - **Điều trị tại ICU ngay lập tức**
            - Benzodiazepine liều cao, có thể cần IV
            - Phòng ngừa co giật (có thể cần thêm thuốc chống co giật)
            - Theo dõi sát liên tục
            - Điều trị hỗ trợ toàn diện
            - Cân nhắc dexmedetomidine nếu cần
            - Bổ sung thiamin, folate, multivitamin
            - Theo dõi dấu hiệu DTS (Delirium Tremens)
            """)
        
        if result['risk_seizures']:
            st.error("⚠️ **NGUY CƠ CO GIẬT CAO** - Cần phòng ngừa và điều trị tích cực")
        
        # Save to history
        save_calculation_to_history(
            calculator_id="gmaws",
            calculator_name="GMAWS",
            inputs={
                "Bồn chồn": f"{agitation}",
                "Định hướng": f"{orientation}",
                "Ảo giác": f"{hallucinations}",
                "Run": f"{tremor}",
                "Đổ mồ hôi": f"{sweating}",
                "Buồn nôn/Nôn": f"{nausea_vomiting}",
                "Lo âu": f"{anxiety}",
                "Đổ mồ hôi từng cơn": f"{paroxysmal_sweats}",
                "Rối loạn xúc giác": f"{tactile_disturbances}",
                "Rối loạn thính giác": f"{auditory_disturbances}"
            },
            result={
                "Điểm": f"{result['total_score']}/70",
                "Mức độ": result['severity']
            }
        )
        
        # Share and export
        render_share_section(
            calculator_id="gmaws",
            calculator_name="GMAWS"
        )
        
        render_export_section(
            calculator_id="gmaws",
            calculator_name="GMAWS",
            data={
                "inputs": {
                    "agitation": agitation,
                    "orientation": orientation,
                    "hallucinations": hallucinations,
                    "tremor": tremor,
                    "sweating": sweating,
                    "nausea_vomiting": nausea_vomiting,
                    "anxiety": anxiety,
                    "paroxysmal_sweats": paroxysmal_sweats,
                    "tactile_disturbances": tactile_disturbances,
                    "auditory_disturbances": auditory_disturbances
                },
                "result": result
            }
        )
    
    # History
    render_history_ui(calculator_id="gmaws", show_actions=True)
    
    # References
    references = get_references("GMAWS")
    if references:
        render_references_section(references)

