"""
THRIVE Score
============

Predicts functional outcome after endovascular thrombectomy for acute ischemic stroke.

Reference:
- Flint AC, et al. THRIVE score predicts ischemic stroke outcomes and thrombolytic bleeding risk in VISTA. 
  Stroke. 2013;44(10):2853-9.
- Nogueira RG, et al. Thrombectomy 6 to 24 Hours after Stroke with a Mismatch between Deficit and Infarct. 
  N Engl J Med. 2018;378(1):11-21.

Clinical Utility:
- Predicts functional outcome after thrombectomy
- Helps guide treatment decisions
- Validated for endovascular therapy
- Simple 5-component score

THRIVE Components:
1. T - Age
2. H - Hypertension
3. R - NIHSS
4. I - Hyperglycemia (Glucose)
5. V - Infarct volume (ASPECTS or imaging)

Score: 0-9 points
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


def calculate_thrive_score(
    age: int,
    hypertension: bool,
    nihss: int,
    glucose_mmol: float,
    aspects_score: int = None,
    infarct_volume_ml: float = None
) -> dict:
    """
    Calculate THRIVE Score
    
    Args:
        age: Patient age (years)
        hypertension: History of hypertension
        nihss: NIHSS score
        glucose_mmol: Blood glucose (mmol/L)
        aspects_score: ASPECTS score (0-10) - if available
        infarct_volume_ml: Infarct volume in mL - if available
    
    Returns:
        dict with score, risk level, and outcome prediction
    """
    score = 0
    breakdown = []
    
    # T - Age
    if age >= 80:
        score += 3
        breakdown.append({"label": "T - Age ≥80", "points": 3, "value": f"{age} tuổi"})
    elif age >= 60:
        score += 2
        breakdown.append({"label": "T - Age 60-79", "points": 2, "value": f"{age} tuổi"})
    else:
        breakdown.append({"label": "T - Age <60", "points": 0, "value": f"{age} tuổi"})
    
    # H - Hypertension
    if hypertension:
        score += 1
        breakdown.append({"label": "H - Hypertension", "points": 1, "value": "Có"})
    else:
        breakdown.append({"label": "H - Hypertension", "points": 0, "value": "Không"})
    
    # R - NIHSS
    if nihss >= 20:
        score += 3
        breakdown.append({"label": "R - NIHSS ≥20", "points": 3, "value": f"{nihss}"})
    elif nihss >= 11:
        score += 2
        breakdown.append({"label": "R - NIHSS 11-19", "points": 2, "value": f"{nihss}"})
    else:
        breakdown.append({"label": "R - NIHSS <11", "points": 0, "value": f"{nihss}"})
    
    # I - Hyperglycemia (Glucose)
    if glucose_mmol >= 11.1:
        score += 2
        breakdown.append({"label": "I - Glucose ≥11.1 mmol/L", "points": 2, "value": f"{glucose_mmol} mmol/L"})
    elif glucose_mmol >= 8.3:
        score += 1
        breakdown.append({"label": "I - Glucose 8.3-11.0 mmol/L", "points": 1, "value": f"{glucose_mmol} mmol/L"})
    else:
        breakdown.append({"label": "I - Glucose <8.3 mmol/L", "points": 0, "value": f"{glucose_mmol} mmol/L"})
    
    # V - Infarct volume (using ASPECTS or volume)
    if aspects_score is not None:
        if aspects_score <= 4:
            score += 2
            breakdown.append({"label": "V - ASPECTS ≤4", "points": 2, "value": f"{aspects_score}"})
        elif aspects_score <= 7:
            score += 1
            breakdown.append({"label": "V - ASPECTS 5-7", "points": 1, "value": f"{aspects_score}"})
        else:
            breakdown.append({"label": "V - ASPECTS ≥8", "points": 0, "value": f"{aspects_score}"})
    elif infarct_volume_ml is not None:
        if infarct_volume_ml >= 100:
            score += 2
            breakdown.append({"label": "V - Infarct volume ≥100 mL", "points": 2, "value": f"{infarct_volume_ml} mL"})
        elif infarct_volume_ml >= 50:
            score += 1
            breakdown.append({"label": "V - Infarct volume 50-99 mL", "points": 1, "value": f"{infarct_volume_ml} mL"})
        else:
            breakdown.append({"label": "V - Infarct volume <50 mL", "points": 0, "value": f"{infarct_volume_ml} mL"})
    else:
        breakdown.append({"label": "V - Infarct volume/ASPECTS", "points": 0, "value": "Chưa có"})
    
    # Risk stratification
    if score <= 2:
        risk_level = "low"
        interpretation = "Nguy cơ thấp"
        good_outcome_probability = "Cao (>60%)"
        recommendation = "Tiên lượng tốt sau thrombectomy"
    elif score <= 5:
        risk_level = "moderate"
        interpretation = "Nguy cơ trung bình"
        good_outcome_probability = "Trung bình (30-60%)"
        recommendation = "Tiên lượng trung bình, điều trị tích cực"
    elif score <= 7:
        risk_level = "high"
        interpretation = "Nguy cơ cao"
        good_outcome_probability = "Thấp (10-30%)"
        recommendation = "Tiên lượng xấu, cân nhắc điều trị tích cực"
    else:
        risk_level = "critical"
        interpretation = "Nguy cơ rất cao"
        good_outcome_probability = "Rất thấp (<10%)"
        recommendation = "Tiên lượng rất xấu, thảo luận với gia đình"
    
    return {
        "score": score,
        "max_score": 11,
        "breakdown": breakdown,
        "risk_level": risk_level,
        "interpretation": interpretation,
        "good_outcome_probability": good_outcome_probability,
        "recommendation": recommendation,
        "age": age,
        "nihss": nihss
    }


def render():
    """THRIVE Score Calculator"""
    st.markdown(f"""
    <h3 style='text-align: center; color: {COLORS['success']};'>🧠 THRIVE Score</h3>
    """, unsafe_allow_html=True)
    st.caption("Dự đoán kết cục chức năng sau thrombectomy ở bệnh nhân đột quỵ thiếu máu cục bộ")
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'thrive_score':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📋 Tiêu chí Đánh giá")
        
        shared_inputs = st.session_state.get('shared_inputs', {})
        
        age = st.number_input(
            "**T** - Age (Tuổi)",
            min_value=0,
            max_value=120,
            value=int(shared_inputs.get('age', 70)) if shared_inputs else 70,
            step=1,
            help="Tuổi bệnh nhân (năm)"
        )
        
        hypertension = st.checkbox(
            "**H** - Hypertension (Tăng huyết áp)",
            help="Tiền sử tăng huyết áp",
            value=shared_inputs.get('hypertension') == 'Có' if shared_inputs else False
        )
        
        nihss = st.number_input(
            "**R** - NIHSS (NIH Stroke Scale)",
            min_value=0,
            max_value=42,
            value=int(shared_inputs.get('nihss', 15)) if shared_inputs else 15,
            step=1,
            help="NIHSS score (0-42)"
        )
        
        glucose_mmol = st.number_input(
            "**I** - Glucose (Đường huyết)",
            min_value=0.0,
            max_value=30.0,
            value=float(shared_inputs.get('glucose_mmol', 6.0)) if shared_inputs else 6.0,
            step=0.1,
            format="%.1f",
            help="Đường huyết (mmol/L)"
        )
        
        st.markdown("#### **V** - Infarct Volume/ASPECTS")
        use_aspects = st.checkbox(
            "Sử dụng ASPECTS score",
            help="Nếu có ASPECTS score, chọn option này",
            value=shared_inputs.get('use_aspects') == 'Có' if shared_inputs else True
        )
        
        if use_aspects:
            aspects_score = st.number_input(
                "ASPECTS Score",
                min_value=0,
                max_value=10,
                value=int(shared_inputs.get('aspects_score', 8)) if shared_inputs else 8,
                step=1,
                help="ASPECTS score (0-10)"
            )
            infarct_volume_ml = None
        else:
            infarct_volume_ml = st.number_input(
                "Infarct Volume (mL)",
                min_value=0.0,
                max_value=500.0,
                value=float(shared_inputs.get('infarct_volume_ml', 0.0)) if shared_inputs else None,
                step=1.0,
                format="%.1f",
                help="Thể tích nhồi máu (mL)"
            )
            aspects_score = None
    
    with col2:
        # Smart Suggestions
        render_suggestions(
            calculator_id="thrive_score",
            calculator_name="THRIVE Score",
            category="Thần kinh",
            show_related=True,
            show_category=True,
            limit=3
        )
        
        # Educational information
        if CALCULATOR_METADATA_AVAILABLE:
            st.markdown("---")
            render_calculator_education("thrive_score")
        elif CALCULATOR_ENHANCEMENTS_AVAILABLE:
            st.markdown("---")
            render_calculator_explanation(
                title="Về THRIVE Score",
                content="""
                **THRIVE Score** dự đoán kết cục sau thrombectomy:
                
                **5 yếu tố:**
                1. **T** - Age ≥80: 3 điểm, 60-79: 2 điểm
                2. **H** - Hypertension: 1 điểm
                3. **R** - NIHSS ≥20: 3 điểm, 11-19: 2 điểm
                4. **I** - Glucose ≥11.1: 2 điểm, 8.3-11.0: 1 điểm
                5. **V** - ASPECTS ≤4: 2 điểm, 5-7: 1 điểm
                
                **Tổng điểm: 0-11**
                
                **Phân tầng:**
                - ≤2: Nguy cơ thấp (>60% kết cục tốt)
                - 3-5: Nguy cơ trung bình (30-60%)
                - 6-7: Nguy cơ cao (10-30%)
                - ≥8: Nguy cơ rất cao (<10%)
                """,
                when_to_use="""
                **Sử dụng khi:**
                - Bệnh nhân đột quỵ thiếu máu cục bộ
                - Đang xem xét thrombectomy
                - Cần dự đoán kết cục sau điều trị
                """,
                limitations="""
                **Hạn chế:**
                - Dự đoán kết cục sau thrombectomy
                - Cần đánh giá lâm sàng toàn diện
                - Không thay thế quyết định lâm sàng
                """,
                clinical_context="""
                **Bối cảnh lâm sàng:**
                - Score ≤2: Tiên lượng tốt
                - Score 3-5: Tiên lượng trung bình
                - Score ≥6: Tiên lượng xấu
                """
            )
    
    st.markdown("---")
    
    # Calculate
    if st.button("🔄 Tính THRIVE Score", type="primary", use_container_width=True):
        result = calculate_thrive_score(
            age,
            hypertension,
            nihss,
            glucose_mmol,
            aspects_score if use_aspects else None,
            infarct_volume_ml if not use_aspects else None
        )
        
        # Save to history
        save_calculation_to_history(
            calculator_id="thrive_score",
            calculator_name="THRIVE Score",
            inputs={
                "age": age,
                "hypertension": "Có" if hypertension else "Không",
                "nihss": nihss,
                "glucose_mmol": glucose_mmol,
                "aspects_score": aspects_score if use_aspects else None,
                "infarct_volume_ml": infarct_volume_ml if not use_aspects else None
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
                <h2 style="color: {risk_color}; margin: 0 0 10px 0;">THRIVE Score: <strong>{result['score']}/{result['max_score']}</strong></h2>
                <p style="font-size: 1.1em; margin: 5px 0;"><strong>Mức độ nguy cơ:</strong> {result['interpretation']}</p>
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
            **⚠️ Nguy cơ rất cao (Score ≥8):**
            - Khả năng kết cục tốt <10%
            - Tiên lượng rất xấu sau thrombectomy
            - Cần thảo luận kỹ với gia đình
            - Cân nhắc điều trị tích cực nhưng cần đánh giá từng trường hợp
            """)
        elif result['risk_level'] == 'high':
            st.warning(f"""
            **⚠️ Nguy cơ cao (Score 6-7):**
            - Khả năng kết cục tốt 10-30%
            - Tiên lượng xấu
            - Cần điều trị tích cực
            - Tư vấn cho gia đình về tiên lượng
            """)
        elif result['risk_level'] == 'moderate':
            st.info(f"""
            **ℹ️ Nguy cơ trung bình (Score 3-5):**
            - Khả năng kết cục tốt 30-60%
            - Tiên lượng trung bình
            - Điều trị tích cực
            - Theo dõi sát
            """)
        else:
            st.success(f"""
            **✅ Nguy cơ thấp (Score ≤2):**
            - Khả năng kết cục tốt >60%
            - Tiên lượng tốt sau thrombectomy
            - Tiếp tục điều trị tích cực
            """)
        
        # Share and Export
        st.markdown("---")
        col_share1, col_share2 = st.columns(2)
        with col_share1:
            render_share_section(
                calculator_id="thrive_score",
                calculator_name="THRIVE Score",
                result=result
            )
        with col_share2:
            render_scores_export(
                calculator_name="THRIVE Score",
                result=result,
                inputs={
                    "Age": f"{age} tuổi",
                    "Hypertension": "Có" if hypertension else "Không",
                    "NIHSS": nihss,
                    "Glucose": f"{glucose_mmol} mmol/L",
                    "ASPECTS": aspects_score if use_aspects else "N/A",
                    "Infarct Volume": f"{infarct_volume_ml} mL" if not use_aspects else "N/A"
                }
            )
    
    # History
    st.markdown("---")
    render_history_ui("thrive_score", "THRIVE Score")
    
    # References
    st.markdown("---")
    references = get_references("thrive_score")
    if references:
        render_references_section(references)
