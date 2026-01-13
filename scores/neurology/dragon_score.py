"""
DRAGON Score
============

Prognostic score for predicting poor outcome (mRS 4-6) at 3 months in acute ischemic stroke patients.

Reference:
- Strbian D, et al. Predicting outcome of IV thrombolysis-treated ischemic stroke patients: The DRAGON score. Neurology. 2012;78(6):427-32.
- Strbian D, et al. The DRAGON score predicts functional outcome in acute ischemic stroke patients treated with intravenous thrombolysis. Int J Stroke. 2013;8(5):372-6.

Clinical Utility:
- Predicts poor functional outcome (mRS 4-6) at 3 months
- Helps guide treatment decisions and patient counseling
- Validated for patients treated with IV thrombolysis
- Simple 6-component score

DRAGON Components:
1. D - Pre-stroke disability (mRS)
2. R - Age
3. A - Glucose (blood sugar)
4. G - Onset to treatment time
5. O - NIHSS
6. N - Normal CT scan (no early ischemic changes)
"""

import streamlit as st
from config.theme import COLORS
from scores.utils.validation import (
    validate_age,
    validate_lab_value
)
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


def calculate_dragon_score(
    pre_stroke_mrs: int,
    age: int,
    glucose_mmol: float,
    onset_to_treatment_hours: float,
    nihss: int,
    normal_ct: bool
) -> dict:
    """
    Calculate DRAGON Score
    
    Args:
        pre_stroke_mrs: Pre-stroke modified Rankin Scale (0-5)
        age: Patient age (years)
        glucose_mmol: Blood glucose (mmol/L)
        onset_to_treatment_hours: Time from symptom onset to treatment (hours)
        nihss: NIHSS score
        normal_ct: Normal CT scan (no early ischemic changes)
    
    Returns:
        dict with score, risk level, and outcome prediction
    """
    score = 0
    breakdown = []
    
    # D - Pre-stroke disability (mRS)
    if pre_stroke_mrs >= 1:
        score += 1
        breakdown.append({"label": "D - Pre-stroke disability (mRS ≥1)", "points": 1, "value": f"mRS {pre_stroke_mrs}"})
    else:
        breakdown.append({"label": "D - Pre-stroke disability (mRS ≥1)", "points": 0, "value": f"mRS {pre_stroke_mrs}"})
    
    # R - Age
    if age >= 80:
        score += 2
        breakdown.append({"label": "R - Age ≥80", "points": 2, "value": f"{age} tuổi"})
    elif age >= 65:
        score += 1
        breakdown.append({"label": "R - Age 65-79", "points": 1, "value": f"{age} tuổi"})
    else:
        breakdown.append({"label": "R - Age <65", "points": 0, "value": f"{age} tuổi"})
    
    # A - Glucose
    if glucose_mmol >= 8.0:
        score += 1
        breakdown.append({"label": "A - Glucose ≥8.0 mmol/L", "points": 1, "value": f"{glucose_mmol} mmol/L"})
    else:
        breakdown.append({"label": "A - Glucose <8.0 mmol/L", "points": 0, "value": f"{glucose_mmol} mmol/L"})
    
    # G - Onset to treatment time
    if onset_to_treatment_hours > 3:
        score += 1
        breakdown.append({"label": "G - Onset to treatment >3h", "points": 1, "value": f"{onset_to_treatment_hours}h"})
    else:
        breakdown.append({"label": "G - Onset to treatment ≤3h", "points": 0, "value": f"{onset_to_treatment_hours}h"})
    
    # O - NIHSS
    if nihss >= 15:
        score += 2
        breakdown.append({"label": "O - NIHSS ≥15", "points": 2, "value": f"{nihss}"})
    elif nihss >= 10:
        score += 1
        breakdown.append({"label": "O - NIHSS 10-14", "points": 1, "value": f"{nihss}"})
    else:
        breakdown.append({"label": "O - NIHSS <10", "points": 0, "value": f"{nihss}"})
    
    # N - Normal CT scan
    if normal_ct:
        score += 1
        breakdown.append({"label": "N - Normal CT (no early changes)", "points": 1, "value": "Có"})
    else:
        breakdown.append({"label": "N - Normal CT (no early changes)", "points": 0, "value": "Không"})
    
    # Risk stratification based on score
    if score <= 2:
        risk_level = "low"
        interpretation = "Nguy cơ thấp"
        poor_outcome_risk = "Thấp (<10%)"
        good_outcome_probability = "Cao (>70%)"
        recommendation = "Tiên lượng tốt, điều trị tích cực"
    elif score <= 4:
        risk_level = "moderate"
        interpretation = "Nguy cơ trung bình"
        poor_outcome_risk = "Trung bình (10-50%)"
        good_outcome_probability = "Trung bình (30-70%)"
        recommendation = "Theo dõi sát, điều trị tích cực"
    elif score <= 6:
        risk_level = "high"
        interpretation = "Nguy cơ cao"
        poor_outcome_risk = "Cao (50-80%)"
        good_outcome_probability = "Thấp (10-30%)"
        recommendation = "Tiên lượng xấu, cân nhắc điều trị tích cực"
    else:
        risk_level = "critical"
        interpretation = "Nguy cơ rất cao"
        poor_outcome_risk = "Rất cao (>80%)"
        good_outcome_probability = "Rất thấp (<10%)"
        recommendation = "Tiên lượng rất xấu, thảo luận với gia đình"
    
    return {
        "score": score,
        "max_score": 8,
        "breakdown": breakdown,
        "risk_level": risk_level,
        "interpretation": interpretation,
        "poor_outcome_risk": poor_outcome_risk,
        "good_outcome_probability": good_outcome_probability,
        "recommendation": recommendation,
        "age": age,
        "nihss": nihss
    }


def render():
    """DRAGON Score Calculator"""
    st.markdown(f"""
    <h3 style='text-align: center; color: {COLORS['success']};'>🧠 DRAGON Score</h3>
    """, unsafe_allow_html=True)
    st.caption("Dự đoán kết cục xấu (mRS 4-6) ở bệnh nhân đột quỵ thiếu máu cục bộ điều trị tPA")
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'dragon_score':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📋 Tiêu chí Đánh giá")
        
        shared_inputs = st.session_state.get('shared_inputs', {})
        
        pre_stroke_mrs = st.number_input(
            "**D** - Pre-stroke mRS (Modified Rankin Scale trước đột quỵ)",
            min_value=0,
            max_value=5,
            value=int(shared_inputs.get('pre_stroke_mrs', 0)) if shared_inputs else 0,
            step=1,
            help="mRS trước đột quỵ (0 = không có khuyết tật, 5 = tàn tật nặng)"
        )
        
        age = st.number_input(
            "**R** - Age (Tuổi)",
            min_value=0,
            max_value=120,
            value=int(shared_inputs.get('age', 70)) if shared_inputs else 70,
            step=1,
            help="Tuổi bệnh nhân (năm)"
        )
        
        glucose_mmol = st.number_input(
            "**A** - Glucose (Đường huyết)",
            min_value=0.0,
            max_value=30.0,
            value=float(shared_inputs.get('glucose_mmol', 6.0)) if shared_inputs else 6.0,
            step=0.1,
            format="%.1f",
            help="Đường huyết (mmol/L). Bình thường: 4-6 mmol/L"
        )
        
        onset_to_treatment_hours = st.number_input(
            "**G** - Onset to treatment time (Thời gian từ khởi phát đến điều trị)",
            min_value=0.0,
            max_value=24.0,
            value=float(shared_inputs.get('onset_to_treatment_hours', 2.0)) if shared_inputs else 2.0,
            step=0.1,
            format="%.1f",
            help="Thời gian từ khi khởi phát triệu chứng đến khi điều trị (giờ)"
        )
        
        nihss = st.number_input(
            "**O** - NIHSS (NIH Stroke Scale)",
            min_value=0,
            max_value=42,
            value=int(shared_inputs.get('nihss', 10)) if shared_inputs else 10,
            step=1,
            help="NIHSS score (0-42)"
        )
        
        normal_ct = st.checkbox(
            "**N** - Normal CT scan (CT bình thường, không có dấu hiệu thiếu máu sớm)",
            help="CT scan không có dấu hiệu thiếu máu sớm (ASPECTS = 10)",
            value=shared_inputs.get('normal_ct') == 'Có' if shared_inputs else False
        )
    
    with col2:
        # Smart Suggestions
        render_suggestions(
            calculator_id="dragon_score",
            calculator_name="DRAGON Score",
            category="Thần kinh",
            show_related=True,
            show_category=True,
            limit=3
        )
        
        # Educational information
        if CALCULATOR_METADATA_AVAILABLE:
            st.markdown("---")
            render_calculator_education("dragon_score")
        elif CALCULATOR_ENHANCEMENTS_AVAILABLE:
            st.markdown("---")
            render_calculator_explanation(
                title="Về DRAGON Score",
                content="""
                **DRAGON Score** dự đoán kết cục xấu (mRS 4-6) ở 3 tháng:
                
                **6 yếu tố:**
                1. **D** - Pre-stroke disability (mRS ≥1): 1 điểm
                2. **R** - Age ≥80: 2 điểm, 65-79: 1 điểm
                3. **A** - Glucose ≥8.0 mmol/L: 1 điểm
                4. **G** - Onset to treatment >3h: 1 điểm
                5. **O** - NIHSS ≥15: 2 điểm, 10-14: 1 điểm
                6. **N** - Normal CT: 1 điểm
                
                **Tổng điểm: 0-8**
                
                **Phân tầng nguy cơ:**
                - ≤2: Nguy cơ thấp (<10% mRS 4-6)
                - 3-4: Nguy cơ trung bình (10-50%)
                - 5-6: Nguy cơ cao (50-80%)
                - ≥7: Nguy cơ rất cao (>80%)
                """,
                when_to_use="""
                **Sử dụng khi:**
                - Bệnh nhân đột quỵ thiếu máu cục bộ điều trị tPA
                - Cần dự đoán kết cục chức năng
                - Tư vấn cho bệnh nhân và gia đình
                - Quyết định điều trị tích cực
                """,
                limitations="""
                **Hạn chế:**
                - Chỉ áp dụng cho bệnh nhân điều trị tPA
                - Dự đoán kết cục ở 3 tháng
                - Cần kết hợp với đánh giá lâm sàng
                - Không thay thế quyết định lâm sàng
                """,
                clinical_context="""
                **Bối cảnh lâm sàng:**
                - Score ≤2: Tiên lượng tốt, điều trị tích cực
                - Score 3-4: Theo dõi sát, điều trị tích cực
                - Score ≥5: Tiên lượng xấu, cân nhắc điều trị tích cực
                - Score ≥7: Tiên lượng rất xấu, thảo luận với gia đình
                """
            )
    
    st.markdown("---")
    
    # Calculate
    if st.button("🔄 Tính DRAGON Score", type="primary", use_container_width=True):
        result = calculate_dragon_score(
            pre_stroke_mrs,
            age,
            glucose_mmol,
            onset_to_treatment_hours,
            nihss,
            normal_ct
        )
        
        # Save to history
        save_calculation_to_history(
            calculator_id="dragon_score",
            calculator_name="DRAGON Score",
            inputs={
                "pre_stroke_mrs": pre_stroke_mrs,
                "age": age,
                "glucose_mmol": glucose_mmol,
                "onset_to_treatment_hours": onset_to_treatment_hours,
                "nihss": nihss,
                "normal_ct": "Có" if normal_ct else "Không"
            },
            result=result
        )
        
        # Display result
        st.markdown("### 📊 Kết quả")
        
        # Main result card
        col_result1, col_result2 = st.columns([2, 1])
        
        with col_result1:
            risk_color = {
                "low": COLORS['success'],
                "moderate": "#FFA500",
                "high": COLORS['warning'],
                "critical": COLORS['danger']
            }.get(result['risk_level'], COLORS['info'])
            
            st.markdown(f"""
            <div style="background: white; padding: 20px; border-radius: 8px; border-left: 4px solid {risk_color}; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                <h2 style="color: {risk_color}; margin: 0 0 10px 0;">DRAGON Score: <strong>{result['score']}/{result['max_score']}</strong></h2>
                <p style="font-size: 1.1em; margin: 5px 0;"><strong>Mức độ nguy cơ:</strong> {result['interpretation']}</p>
                <p style="margin: 5px 0;"><strong>Nguy cơ kết cục xấu (mRS 4-6):</strong> {result['poor_outcome_risk']}</p>
                <p style="margin: 5px 0;"><strong>Khả năng kết cục tốt:</strong> {result['good_outcome_probability']}</p>
                <p style="margin: 5px 0;"><strong>Khuyến nghị:</strong> {result['recommendation']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col_result2:
            render_risk_badge(result['risk_level'], result['interpretation'])
        
        # Breakdown
        st.markdown("---")
        st.markdown("### 📋 Chi tiết điểm số")
        
        breakdown_data = [
            {"label": item["label"], "value": f"{item['value']} (+{item['points']} điểm)" if item['points'] > 0 else f"{item['value']} (0 điểm)"}
            for item in result['breakdown']
        ]
        breakdown_data.append({"label": "**Tổng điểm**", "value": f"**{result['score']}/{result['max_score']}**"})
        
        render_score_breakdown(breakdown_data)
        
        # Clinical interpretation
        st.markdown("---")
        st.markdown("### 💡 Hướng dẫn lâm sàng")
        
        if result['risk_level'] == 'critical':
            st.error(f"""
            **⚠️ Nguy cơ rất cao (Score ≥7):**
            - Nguy cơ kết cục xấu (mRS 4-6) >80%
            - Khả năng kết cục tốt <10%
            - Tiên lượng rất xấu
            - Cần thảo luận kỹ với gia đình về tiên lượng
            - Cân nhắc điều trị tích cực nhưng cần đánh giá từng trường hợp
            """)
        elif result['risk_level'] == 'high':
            st.warning(f"""
            **⚠️ Nguy cơ cao (Score 5-6):**
            - Nguy cơ kết cục xấu (mRS 4-6) 50-80%
            - Khả năng kết cục tốt 10-30%
            - Tiên lượng xấu
            - Cần điều trị tích cực và theo dõi sát
            - Tư vấn cho gia đình về tiên lượng
            """)
        elif result['risk_level'] == 'moderate':
            st.info(f"""
            **ℹ️ Nguy cơ trung bình (Score 3-4):**
            - Nguy cơ kết cục xấu (mRS 4-6) 10-50%
            - Khả năng kết cục tốt 30-70%
            - Theo dõi sát và điều trị tích cực
            - Đánh giá lại thường xuyên
            """)
        else:
            st.success(f"""
            **✅ Nguy cơ thấp (Score ≤2):**
            - Nguy cơ kết cục xấu (mRS 4-6) <10%
            - Khả năng kết cục tốt >70%
            - Tiên lượng tốt
            - Tiếp tục điều trị tích cực
            """)
        
        # Share and Export
        st.markdown("---")
        col_share1, col_share2 = st.columns(2)
        with col_share1:
            render_share_section(
                calculator_id="dragon_score",
                calculator_name="DRAGON Score",
                result=result
            )
        with col_share2:
            render_scores_export(
                calculator_name="DRAGON Score",
                result=result,
                inputs={
                    "Pre-stroke mRS": pre_stroke_mrs,
                    "Age": f"{age} tuổi",
                    "Glucose": f"{glucose_mmol} mmol/L",
                    "Onset to treatment": f"{onset_to_treatment_hours}h",
                    "NIHSS": nihss,
                    "Normal CT": "Có" if normal_ct else "Không"
                }
            )
    
    # History
    st.markdown("---")
    render_history_ui("dragon_score", "DRAGON Score")
    
    # References
    st.markdown("---")
    references = get_references("dragon_score")
    if references:
        render_references_section(references)
