"""
DASS-21 - Depression, Anxiety and Stress Scale - 21 items
=========================================================

A 21-item self-report questionnaire measuring depression, anxiety, and stress.

Reference:
- Lovibond SH, Lovibond PF. Manual for the Depression Anxiety Stress Scales. 2nd ed. Sydney: Psychology Foundation; 1995.
- Vietnamese validation studies available

Clinical Utility:
- Widely used in Vietnam for mental health screening
- Validated for Vietnamese population
- Assesses three related negative emotional states
- Quick screening tool (5-10 minutes)

DASS-21 Structure:
- 21 items total
- 7 items per subscale (Depression, Anxiety, Stress)
- Each item scored 0-3
- Subscale scores: 0-21 each
- Total score: 0-63
"""

import streamlit as st
from config.theme import COLORS
from components.ui.scoring import render_score_result, render_score_breakdown
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
# ======================================

# ========== NEW COMPONENTS (Phase 1 & 2) ==========
from components.risk_color_coding import render_risk_badge, get_risk_level
from components.score_charts import render_risk_gauge_chart, render_risk_bar_chart
from components.scores_export import render_export_section as render_scores_export
# ========== PHASE 1: CALCULATOR ENHANCEMENTS ==========
try:
    from components.calculator_enhancements import (
        render_calculator_explanation,
        render_evidence_citation,
        render_result_interpretation
    )
    CALCULATOR_ENHANCEMENTS_AVAILABLE = True
except ImportError:
    CALCULATOR_ENHANCEMENTS_AVAILABLE = False

# ========== PHASE 1: CALCULATOR METADATA ==========
try:
    from components.phase1_calculator_metadata import (
        render_calculator_education,
        render_calculator_result_with_interpretation,
        get_calculator_metadata
    )
    CALCULATOR_METADATA_AVAILABLE = True
except ImportError:
    CALCULATOR_METADATA_AVAILABLE = False
# ===================================================


# DASS-21 Questions in Vietnamese
DASS21_QUESTIONS = {
    "Depression": [
        "Tôi cảm thấy khó có thể tự mình khởi động hoặc làm việc",
        "Tôi cảm thấy không có gì để mong đợi",
        "Tôi cảm thấy buồn và chán nản",
        "Tôi cảm thấy không có động lực để làm bất cứ việc gì",
        "Tôi cảm thấy không đáng giá như một con người",
        "Tôi cảm thấy cuộc sống của tôi vô nghĩa",
        "Tôi không thể cảm nhận được cảm xúc tích cực"
    ],
    "Anxiety": [
        "Tôi cảm thấy miệng khô",
        "Tôi cảm thấy khó thở (không phải do gắng sức)",
        "Tôi cảm thấy run rẩy (ví dụ: ở tay)",
        "Tôi cảm thấy lo lắng rằng có điều gì đó tồi tệ sẽ xảy ra",
        "Tôi cảm thấy tim đập nhanh",
        "Tôi cảm thấy lo lắng không yên",
        "Tôi cảm thấy sợ hãi mà không có lý do rõ ràng"
    ],
    "Stress": [
        "Tôi cảm thấy khó thư giãn",
        "Tôi cảm thấy khó chịu khi phải phản ứng lại với những điều nhỏ nhặt",
        "Tôi cảm thấy mình dễ bị kích động",
        "Tôi cảm thấy khó chịu khi phải dừng lại",
        "Tôi cảm thấy sợ mất kiểm soát",
        "Tôi cảm thấy khó chịu khi không thể ngừng lo lắng",
        "Tôi cảm thấy khó chịu khi phải làm việc gấp"
    ]
}

DASS21_SCALE = [
    "0 - Không áp dụng với tôi",
    "1 - Áp dụng với tôi một phần hoặc đôi khi",
    "2 - Áp dụng với tôi khá nhiều hoặc thường xuyên",
    "3 - Áp dụng với tôi rất nhiều hoặc hầu hết thời gian"
]


def calculate_dass21(depression_scores, anxiety_scores, stress_scores):
    """
    Calculate DASS-21 scores
    
    Args:
        depression_scores: List of 7 scores (0-3) for depression items
        anxiety_scores: List of 7 scores (0-3) for anxiety items
        stress_scores: List of 7 scores (0-3) for stress items
    
    Returns:
        dict with subscale scores, total score, and interpretations
    """
    depression_total = sum(depression_scores) * 2  # Multiply by 2 to get DASS-42 equivalent
    anxiety_total = sum(anxiety_scores) * 2
    stress_total = sum(stress_scores) * 2
    
    total_score = depression_total + anxiety_total + stress_total
    
    # Interpret depression
    if depression_total < 10:
        dep_severity = "Bình thường"
        dep_level = "normal"
    elif depression_total < 14:
        dep_severity = "Nhẹ"
        dep_level = "mild"
    elif depression_total < 21:
        dep_severity = "Trung bình"
        dep_level = "moderate"
    elif depression_total < 28:
        dep_severity = "Nặng"
        dep_level = "severe"
    else:
        dep_severity = "Rất nặng"
        dep_level = "extremely_severe"
    
    # Interpret anxiety
    if anxiety_total < 8:
        anx_severity = "Bình thường"
        anx_level = "normal"
    elif anxiety_total < 10:
        anx_severity = "Nhẹ"
        anx_level = "mild"
    elif anxiety_total < 15:
        anx_severity = "Trung bình"
        anx_level = "moderate"
    elif anxiety_total < 20:
        anx_severity = "Nặng"
        anx_level = "severe"
    else:
        anx_severity = "Rất nặng"
        anx_level = "extremely_severe"
    
    # Interpret stress
    if stress_total < 15:
        stress_severity = "Bình thường"
        stress_level = "normal"
    elif stress_total < 19:
        stress_severity = "Nhẹ"
        stress_level = "mild"
    elif stress_total < 26:
        stress_severity = "Trung bình"
        stress_level = "moderate"
    elif stress_total < 34:
        stress_severity = "Nặng"
        stress_level = "severe"
    else:
        stress_severity = "Rất nặng"
        stress_level = "extremely_severe"
    
    # Overall risk level
    max_level = max(
        ["normal", "mild", "moderate", "severe", "extremely_severe"].index(dep_level),
        ["normal", "mild", "moderate", "severe", "extremely_severe"].index(anx_level),
        ["normal", "mild", "moderate", "severe", "extremely_severe"].index(stress_level)
    )
    
    if max_level >= 4:
        overall_risk = "critical"
        overall_interpretation = "Rất nặng"
    elif max_level >= 3:
        overall_risk = "high"
        overall_interpretation = "Nặng"
    elif max_level >= 2:
        overall_risk = "moderate"
        overall_interpretation = "Trung bình"
    elif max_level >= 1:
        overall_risk = "low"
        overall_interpretation = "Nhẹ"
    else:
        overall_risk = "low"
        overall_interpretation = "Bình thường"
    
    return {
        "depression_score": depression_total,
        "anxiety_score": anxiety_total,
        "stress_score": stress_total,
        "total_score": total_score,
        "depression_severity": dep_severity,
        "anxiety_severity": anx_severity,
        "stress_severity": stress_severity,
        "depression_level": dep_level,
        "anxiety_level": anx_level,
        "stress_level": stress_level,
        "overall_risk": overall_risk,
        "overall_interpretation": overall_interpretation
    }


def render():
    """DASS-21 Calculator"""
    st.markdown(f"""
    <h3 style='text-align: center; color: {COLORS['success']};'>🧠 DASS-21</h3>
    """, unsafe_allow_html=True)
    st.caption("Thang đo Trầm cảm, Lo âu và Stress - 21 mục (Đã được nghiên cứu tại Việt Nam)")
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'dass21':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    st.info("""
    **Hướng dẫn:** Đọc từng câu và chọn mức độ phù hợp nhất với bạn trong **tuần qua**.
    """)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📋 Câu hỏi DASS-21")
        
        shared_inputs = st.session_state.get('shared_inputs', {})
        
        # Depression subscale
        st.markdown("#### 🟦 Trầm cảm (Depression)")
        depression_scores = []
        for i, question in enumerate(DASS21_QUESTIONS["Depression"]):
            score = st.radio(
                question,
                options=[0, 1, 2, 3],
                format_func=lambda x: DASS21_SCALE[x],
                horizontal=True,
                key=f"dep_{i}",
                index=int(shared_inputs.get(f"dep_{i}", 0)) if shared_inputs else 0
            )
            depression_scores.append(score)
        
        st.markdown("---")
        
        # Anxiety subscale
        st.markdown("#### 🟨 Lo âu (Anxiety)")
        anxiety_scores = []
        for i, question in enumerate(DASS21_QUESTIONS["Anxiety"]):
            score = st.radio(
                question,
                options=[0, 1, 2, 3],
                format_func=lambda x: DASS21_SCALE[x],
                horizontal=True,
                key=f"anx_{i}",
                index=int(shared_inputs.get(f"anx_{i}", 0)) if shared_inputs else 0
            )
            anxiety_scores.append(score)
        
        st.markdown("---")
        
        # Stress subscale
        st.markdown("#### 🟥 Stress")
        stress_scores = []
        for i, question in enumerate(DASS21_QUESTIONS["Stress"]):
            score = st.radio(
                question,
                options=[0, 1, 2, 3],
                format_func=lambda x: DASS21_SCALE[x],
                horizontal=True,
                key=f"stress_{i}",
                index=int(shared_inputs.get(f"stress_{i}", 0)) if shared_inputs else 0
            )
            stress_scores.append(score)
    
    with col2:
        # Smart Suggestions
        render_suggestions(
            calculator_id="dass21",
            calculator_name="DASS-21",
            category="Tâm thần",
            show_related=True,
            show_category=True,
            limit=3
        )
        
        # Educational information
        if CALCULATOR_METADATA_AVAILABLE:
            st.markdown("---")
            render_calculator_education("dass21")
        elif CALCULATOR_ENHANCEMENTS_AVAILABLE:
            st.markdown("---")
            render_calculator_explanation(
                title="Về DASS-21",
                content="""
                **DASS-21** đánh giá 3 trạng thái cảm xúc tiêu cực:
                
                **3 tiểu thang:**
                1. **Trầm cảm (Depression)** - 7 câu
                2. **Lo âu (Anxiety)** - 7 câu
                3. **Stress** - 7 câu
                
                **Tổng cộng:** 21 câu hỏi
                
                **Thang điểm:** 0-3 mỗi câu
                - 0: Không áp dụng
                - 1: Đôi khi
                - 2: Thường xuyên
                - 3: Hầu hết thời gian
                
                **Điểm số:** Nhân đôi để so sánh với DASS-42
                """,
                when_to_use="""
                **Sử dụng khi:**
                - Sàng lọc sức khỏe tâm thần
                - Đánh giá trầm cảm, lo âu, stress
                - Theo dõi đáp ứng điều trị
                - Nghiên cứu và khảo sát
                """,
                limitations="""
                **Hạn chế:**
                - Tự báo cáo, có thể không chính xác
                - Không thay thế chẩn đoán lâm sàng
                - Cần đánh giá bởi chuyên gia
                - Có thể bị ảnh hưởng bởi các yếu tố khác
                """,
                clinical_context="""
                **Bối cảnh lâm sàng:**
                - Đã được nghiên cứu và validate tại Việt Nam
                - Phù hợp với văn hóa Việt Nam
                - Sử dụng rộng rãi trong nghiên cứu và lâm sàng
                - Hữu ích cho sàng lọc ban đầu
                """
            )
    
    st.markdown("---")
    
    # Calculate
    if st.button("🔄 Tính DASS-21", type="primary", use_container_width=True):
        result = calculate_dass21(depression_scores, anxiety_scores, stress_scores)
        
        # Save to history
        save_calculation_to_history(
            calculator_id="dass21",
            calculator_name="DASS-21",
            inputs={
                **{f"dep_{i}": s for i, s in enumerate(depression_scores)},
                **{f"anx_{i}": s for i, s in enumerate(anxiety_scores)},
                **{f"stress_{i}": s for i, s in enumerate(stress_scores)}
            },
            result=result
        )
        
        # Display result
        st.markdown("### 📊 Kết quả")
        
        # Main result cards
        col_dep, col_anx, col_stress = st.columns(3)
        
        with col_dep:
            dep_color = COLORS['info'] if result['depression_level'] == 'normal' else COLORS['warning'] if result['depression_level'] in ['mild', 'moderate'] else COLORS['danger']
            st.markdown(f"""
            <div style="background: white; padding: 15px; border-radius: 8px; border-left: 4px solid {dep_color};">
                <h4 style="color: {dep_color}; margin: 0;">Trầm cảm</h4>
                <h3 style="margin: 5px 0;">{result['depression_score']}</h3>
                <p style="margin: 0;">{result['depression_severity']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col_anx:
            anx_color = COLORS['info'] if result['anxiety_level'] == 'normal' else COLORS['warning'] if result['anxiety_level'] in ['mild', 'moderate'] else COLORS['danger']
            st.markdown(f"""
            <div style="background: white; padding: 15px; border-radius: 8px; border-left: 4px solid {anx_color};">
                <h4 style="color: {anx_color}; margin: 0;">Lo âu</h4>
                <h3 style="margin: 5px 0;">{result['anxiety_score']}</h3>
                <p style="margin: 0;">{result['anxiety_severity']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col_stress:
            stress_color = COLORS['info'] if result['stress_level'] == 'normal' else COLORS['warning'] if result['stress_level'] in ['mild', 'moderate'] else COLORS['danger']
            st.markdown(f"""
            <div style="background: white; padding: 15px; border-radius: 8px; border-left: 4px solid {stress_color};">
                <h4 style="color: {stress_color}; margin: 0;">Stress</h4>
                <h3 style="margin: 5px 0;">{result['stress_score']}</h3>
                <p style="margin: 0;">{result['stress_severity']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Breakdown
        st.markdown("---")
        st.markdown("### 📋 Chi tiết điểm số")
        
        breakdown_data = [
            {"label": "Trầm cảm (Depression)", "value": f"{result['depression_score']} - {result['depression_severity']}"},
            {"label": "Lo âu (Anxiety)", "value": f"{result['anxiety_score']} - {result['anxiety_severity']}"},
            {"label": "Stress", "value": f"{result['stress_score']} - {result['stress_severity']}"},
            {"label": "Tổng điểm", "value": f"{result['total_score']}"},
        ]
        
        render_score_breakdown(breakdown_data)
        
        # Clinical interpretation
        st.markdown("---")
        st.markdown("### 💡 Hướng dẫn lâm sàng")
        
        if result['overall_risk'] == 'critical':
            st.error("""
            **⚠️ Mức độ rất nặng:**
            - Cần đánh giá ngay bởi chuyên gia tâm thần
            - Xem xét điều trị tích cực
            - Đánh giá nguy cơ tự tử
            - Có thể cần nhập viện
            """)
        elif result['overall_risk'] == 'high':
            st.warning("""
            **⚠️ Mức độ nặng:**
            - Cần đánh giá bởi chuyên gia
            - Xem xét điều trị (thuốc và/hoặc tâm lý trị liệu)
            - Theo dõi sát
            """)
        elif result['overall_risk'] == 'moderate':
            st.info("""
            **ℹ️ Mức độ trung bình:**
            - Cần theo dõi và đánh giá thêm
            - Xem xét can thiệp sớm
            - Giáo dục và hỗ trợ
            """)
        else:
            st.success("""
            **✅ Mức độ nhẹ/Bình thường:**
            - Theo dõi thường quy
            - Giáo dục về sức khỏe tâm thần
            - Tái đánh giá khi cần
            """)
        
        # Share and Export
        st.markdown("---")
        col_share1, col_share2 = st.columns(2)
        with col_share1:
            render_share_section(
                calculator_id="dass21",
                calculator_name="DASS-21",
                result=result
            )
        with col_share2:
            render_scores_export(
                calculator_name="DASS-21",
                result=result,
                inputs={
                    "Depression Score": result['depression_score'],
                    "Anxiety Score": result['anxiety_score'],
                    "Stress Score": result['stress_score'],
                    "Total Score": result['total_score']
                }
            )
    
    # History
    st.markdown("---")
    render_history_ui("dass21", "DASS-21")
    
    # References
    st.markdown("---")
    references = get_references("dass21")
    if references:
        render_references_section(references)
