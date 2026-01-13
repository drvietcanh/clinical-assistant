"""
SEDAN Score
===========

Predicts risk of symptomatic intracerebral hemorrhage (sICH) after intravenous thrombolysis (tPA).

Reference:
- Strbian D, et al. Predicting outcome of IV thrombolysis-treated ischemic stroke patients: 
  The DRAGON score. Neurology. 2012;78(6):427-32.
- Strbian D, et al. Symptomatic intracranial hemorrhage after stroke thrombolysis: 
  The SEDAN score. Neurology. 2012;78(10):729-35.

Clinical Utility:
- Predicts symptomatic ICH after tPA
- Helps guide treatment decisions
- Validated for IV thrombolysis
- Simple 6-component score

SEDAN Components:
1. S - Sugar (Glucose)
2. E - Early infarct signs (on CT)
3. D - Dense artery sign (on CT)
4. A - Age
5. N - NIHSS

Score: 0-6 points
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


def calculate_sedan_score(
    glucose_mmol: float,
    early_infarct_signs: bool,
    dense_artery_sign: bool,
    age: int,
    nihss: int
) -> dict:
    """
    Calculate SEDAN Score
    
    Args:
        glucose_mmol: Blood glucose (mmol/L)
        early_infarct_signs: Early infarct signs on CT
        dense_artery_sign: Dense artery sign on CT
        age: Patient age (years)
        nihss: NIHSS score
    
    Returns:
        dict with score, risk level, and sICH prediction
    """
    score = 0
    breakdown = []
    
    # S - Sugar (Glucose)
    if glucose_mmol >= 12.0:
        score += 1
        breakdown.append({"label": "S - Glucose ≥12.0 mmol/L", "points": 1, "value": f"{glucose_mmol} mmol/L"})
    else:
        breakdown.append({"label": "S - Glucose <12.0 mmol/L", "points": 0, "value": f"{glucose_mmol} mmol/L"})
    
    # E - Early infarct signs
    if early_infarct_signs:
        score += 1
        breakdown.append({"label": "E - Early infarct signs", "points": 1, "value": "Có"})
    else:
        breakdown.append({"label": "E - Early infarct signs", "points": 0, "value": "Không"})
    
    # D - Dense artery sign
    if dense_artery_sign:
        score += 1
        breakdown.append({"label": "D - Dense artery sign", "points": 1, "value": "Có"})
    else:
        breakdown.append({"label": "D - Dense artery sign", "points": 0, "value": "Không"})
    
    # A - Age
    if age >= 75:
        score += 1
        breakdown.append({"label": "A - Age ≥75", "points": 1, "value": f"{age} tuổi"})
    else:
        breakdown.append({"label": "A - Age <75", "points": 0, "value": f"{age} tuổi"})
    
    # N - NIHSS
    if nihss >= 10:
        score += 2
        breakdown.append({"label": "N - NIHSS ≥10", "points": 2, "value": f"{nihss}"})
    else:
        breakdown.append({"label": "N - NIHSS <10", "points": 0, "value": f"{nihss}"})
    
    # Risk stratification
    if score <= 1:
        risk_level = "low"
        interpretation = "Nguy cơ thấp"
        sich_risk = "Thấp (<2%)"
        recommendation = "Nguy cơ sICH thấp, có thể điều trị tPA"
    elif score <= 3:
        risk_level = "moderate"
        interpretation = "Nguy cơ trung bình"
        sich_risk = "Trung bình (2-5%)"
        recommendation = "Nguy cơ sICH trung bình, cân nhắc cẩn thận"
    elif score <= 5:
        risk_level = "high"
        interpretation = "Nguy cơ cao"
        sich_risk = "Cao (5-10%)"
        recommendation = "Nguy cơ sICH cao, cân nhắc kỹ trước khi điều trị tPA"
    else:
        risk_level = "critical"
        interpretation = "Nguy cơ rất cao"
        sich_risk = "Rất cao (>10%)"
        recommendation = "Nguy cơ sICH rất cao, cân nhắc không điều trị tPA"
    
    return {
        "score": score,
        "max_score": 6,
        "breakdown": breakdown,
        "risk_level": risk_level,
        "interpretation": interpretation,
        "sich_risk": sich_risk,
        "recommendation": recommendation,
        "age": age,
        "nihss": nihss
    }


def render():
    """SEDAN Score Calculator"""
    st.markdown(f"""
    <h3 style='text-align: center; color: {COLORS['success']};'>🧠 SEDAN Score</h3>
    """, unsafe_allow_html=True)
    st.caption("Dự đoán nguy cơ xuất huyết nội sọ có triệu chứng (sICH) sau điều trị tPA")
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'sedan_score':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📋 Tiêu chí Đánh giá")
        
        shared_inputs = st.session_state.get('shared_inputs', {})
        
        glucose_mmol = st.number_input(
            "**S** - Sugar (Glucose - Đường huyết)",
            min_value=0.0,
            max_value=30.0,
            value=float(shared_inputs.get('glucose_mmol', 6.0)) if shared_inputs else 6.0,
            step=0.1,
            format="%.1f",
            help="Đường huyết (mmol/L)"
        )
        
        early_infarct_signs = st.checkbox(
            "**E** - Early infarct signs (Dấu hiệu nhồi máu sớm trên CT)",
            help="Có dấu hiệu nhồi máu sớm trên CT scan",
            value=shared_inputs.get('early_infarct_signs') == 'Có' if shared_inputs else False
        )
        
        dense_artery_sign = st.checkbox(
            "**D** - Dense artery sign (Dấu hiệu động mạch đậm)",
            help="Có dấu hiệu động mạch đậm trên CT (dense MCA sign)",
            value=shared_inputs.get('dense_artery_sign') == 'Có' if shared_inputs else False
        )
        
        age = st.number_input(
            "**A** - Age (Tuổi)",
            min_value=0,
            max_value=120,
            value=int(shared_inputs.get('age', 70)) if shared_inputs else 70,
            step=1,
            help="Tuổi bệnh nhân (năm)"
        )
        
        nihss = st.number_input(
            "**N** - NIHSS (NIH Stroke Scale)",
            min_value=0,
            max_value=42,
            value=int(shared_inputs.get('nihss', 10)) if shared_inputs else 10,
            step=1,
            help="NIHSS score (0-42)"
        )
    
    with col2:
        # Smart Suggestions
        render_suggestions(
            calculator_id="sedan_score",
            calculator_name="SEDAN Score",
            category="Thần kinh",
            show_related=True,
            show_category=True,
            limit=3
        )
        
        # Educational information
        if CALCULATOR_METADATA_AVAILABLE:
            st.markdown("---")
            render_calculator_education("sedan_score")
        elif CALCULATOR_ENHANCEMENTS_AVAILABLE:
            st.markdown("---")
            render_calculator_explanation(
                title="Về SEDAN Score",
                content="""
                **SEDAN Score** dự đoán nguy cơ sICH sau tPA:
                
                **5 yếu tố:**
                1. **S** - Glucose ≥12.0 mmol/L: 1 điểm
                2. **E** - Early infarct signs: 1 điểm
                3. **D** - Dense artery sign: 1 điểm
                4. **A** - Age ≥75: 1 điểm
                5. **N** - NIHSS ≥10: 2 điểm
                
                **Tổng điểm: 0-6**
                
                **Phân tầng nguy cơ sICH:**
                - ≤1: Nguy cơ thấp (<2%)
                - 2-3: Nguy cơ trung bình (2-5%)
                - 4-5: Nguy cơ cao (5-10%)
                - 6: Nguy cơ rất cao (>10%)
                """,
                when_to_use="""
                **Sử dụng khi:**
                - Bệnh nhân đột quỵ thiếu máu cục bộ
                - Đang xem xét điều trị tPA
                - Cần đánh giá nguy cơ sICH
                """,
                limitations="""
                **Hạn chế:**
                - Dự đoán nguy cơ sICH sau tPA
                - Cần đánh giá lâm sàng toàn diện
                - Không thay thế quyết định lâm sàng
                """,
                clinical_context="""
                **Bối cảnh lâm sàng:**
                - Score ≤1: Nguy cơ thấp, có thể điều trị tPA
                - Score 2-3: Cân nhắc cẩn thận
                - Score ≥4: Nguy cơ cao, cân nhắc kỹ trước khi điều trị
                """
            )
    
    st.markdown("---")
    
    # Calculate
    if st.button("🔄 Tính SEDAN Score", type="primary", use_container_width=True):
        result = calculate_sedan_score(
            glucose_mmol,
            early_infarct_signs,
            dense_artery_sign,
            age,
            nihss
        )
        
        # Save to history
        save_calculation_to_history(
            calculator_id="sedan_score",
            calculator_name="SEDAN Score",
            inputs={
                "glucose_mmol": glucose_mmol,
                "early_infarct_signs": "Có" if early_infarct_signs else "Không",
                "dense_artery_sign": "Có" if dense_artery_sign else "Không",
                "age": age,
                "nihss": nihss
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
                <h2 style="color: {risk_color}; margin: 0 0 10px 0;">SEDAN Score: <strong>{result['score']}/{result['max_score']}</strong></h2>
                <p style="font-size: 1.1em; margin: 5px 0;"><strong>Mức độ nguy cơ:</strong> {result['interpretation']}</p>
                <p style="margin: 5px 0;"><strong>Nguy cơ sICH:</strong> {result['sich_risk']}</p>
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
            **⚠️ Nguy cơ rất cao (Score 6):**
            - Nguy cơ sICH >10%
            - Cân nhắc KHÔNG điều trị tPA
            - Thảo luận kỹ với gia đình về nguy cơ
            - Xem xét các phương pháp điều trị khác
            """)
        elif result['risk_level'] == 'high':
            st.warning(f"""
            **⚠️ Nguy cơ cao (Score 4-5):**
            - Nguy cơ sICH 5-10%
            - Cân nhắc kỹ trước khi điều trị tPA
            - Thảo luận với gia đình về nguy cơ
            - Theo dõi sát sau điều trị
            """)
        elif result['risk_level'] == 'moderate':
            st.info(f"""
            **ℹ️ Nguy cơ trung bình (Score 2-3):**
            - Nguy cơ sICH 2-5%
            - Cân nhắc cẩn thận
            - Có thể điều trị tPA nhưng cần theo dõi sát
            """)
        else:
            st.success(f"""
            **✅ Nguy cơ thấp (Score ≤1):**
            - Nguy cơ sICH <2%
            - Nguy cơ thấp, có thể điều trị tPA
            - Theo dõi thường quy
            """)
        
        # Share and Export
        st.markdown("---")
        col_share1, col_share2 = st.columns(2)
        with col_share1:
            render_share_section(
                calculator_id="sedan_score",
                calculator_name="SEDAN Score",
                result=result
            )
        with col_share2:
            render_scores_export(
                calculator_name="SEDAN Score",
                result=result,
                inputs={
                    "Glucose": f"{glucose_mmol} mmol/L",
                    "Early infarct signs": "Có" if early_infarct_signs else "Không",
                    "Dense artery sign": "Có" if dense_artery_sign else "Không",
                    "Age": f"{age} tuổi",
                    "NIHSS": nihss
                }
            )
    
    # History
    st.markdown("---")
    render_history_ui("sedan_score", "SEDAN Score")
    
    # References
    st.markdown("---")
    references = get_references("sedan_score")
    if references:
        render_references_section(references)
