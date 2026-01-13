"""
HACOR Score
===========

Predicts failure of non-invasive ventilation (NIV) in patients with acute respiratory failure.

Reference:
- Duan J, et al. Prediction of NIV failure in patients with acute respiratory failure: The HACOR score. 
  Intensive Care Med. 2016;42(9):1377-88.

Clinical Utility:
- Predicts NIV failure within 48 hours
- Helps guide decision for intubation
- Validated for acute respiratory failure
- Simple 5-component score

HACOR Components:
1. H - Heart rate
2. A - Acidosis (pH)
3. C - Consciousness (GCS)
4. O - Oxygenation (PaO2/FiO2)
5. R - Respiratory rate

Score: 0-25 points
"""

import streamlit as st
from config.theme import COLORS
from scores.utils.validation import (
    validate_heart_rate,
    validate_respiratory_rate,
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


def calculate_hacor_score(
    heart_rate: int,
    ph: float,
    gcs: int,
    pao2_fio2: float,
    respiratory_rate: int
) -> dict:
    """
    Calculate HACOR Score
    
    Args:
        heart_rate: Heart rate (bpm)
        ph: Arterial pH
        gcs: Glasgow Coma Scale
        pao2_fio2: PaO2/FiO2 ratio
        respiratory_rate: Respiratory rate (/min)
    
    Returns:
        dict with score, risk level, and NIV failure prediction
    """
    score = 0
    breakdown = []
    
    # H - Heart rate
    if heart_rate >= 125:
        score += 5
        breakdown.append({"label": "H - Heart rate ≥125 bpm", "points": 5, "value": f"{heart_rate} bpm"})
    elif heart_rate >= 105:
        score += 3
        breakdown.append({"label": "H - Heart rate 105-124 bpm", "points": 3, "value": f"{heart_rate} bpm"})
    else:
        breakdown.append({"label": "H - Heart rate <105 bpm", "points": 0, "value": f"{heart_rate} bpm"})
    
    # A - Acidosis (pH)
    if ph < 7.25:
        score += 4
        breakdown.append({"label": "A - pH <7.25", "points": 4, "value": f"{ph:.2f}"})
    elif ph < 7.30:
        score += 2
        breakdown.append({"label": "A - pH 7.25-7.29", "points": 2, "value": f"{ph:.2f}"})
    else:
        breakdown.append({"label": "A - pH ≥7.30", "points": 0, "value": f"{ph:.2f}"})
    
    # C - Consciousness (GCS)
    if gcs <= 8:
        score += 4
        breakdown.append({"label": "C - GCS ≤8", "points": 4, "value": f"{gcs}"})
    elif gcs <= 11:
        score += 2
        breakdown.append({"label": "C - GCS 9-11", "points": 2, "value": f"{gcs}"})
    else:
        breakdown.append({"label": "C - GCS ≥12", "points": 0, "value": f"{gcs}"})
    
    # O - Oxygenation (PaO2/FiO2)
    if pao2_fio2 < 125:
        score += 4
        breakdown.append({"label": "O - PaO2/FiO2 <125", "points": 4, "value": f"{pao2_fio2:.0f}"})
    elif pao2_fio2 < 175:
        score += 2
        breakdown.append({"label": "O - PaO2/FiO2 125-174", "points": 2, "value": f"{pao2_fio2:.0f}"})
    else:
        breakdown.append({"label": "O - PaO2/FiO2 ≥175", "points": 0, "value": f"{pao2_fio2:.0f}"})
    
    # R - Respiratory rate
    if respiratory_rate >= 35:
        score += 4
        breakdown.append({"label": "R - Respiratory rate ≥35/min", "points": 4, "value": f"{respiratory_rate}/min"})
    elif respiratory_rate >= 30:
        score += 2
        breakdown.append({"label": "R - Respiratory rate 30-34/min", "points": 2, "value": f"{respiratory_rate}/min"})
    else:
        breakdown.append({"label": "R - Respiratory rate <30/min", "points": 0, "value": f"{respiratory_rate}/min"})
    
    # Risk stratification
    if score < 5:
        risk_level = "low"
        interpretation = "Nguy cơ thấp"
        niv_failure_risk = "Thấp (<15%)"
        recommendation = "Tiếp tục NIV, theo dõi"
    elif score <= 14:
        risk_level = "moderate"
        interpretation = "Nguy cơ trung bình"
        niv_failure_risk = "Trung bình (15-50%)"
        recommendation = "Theo dõi sát, đánh giá lại thường xuyên"
    elif score <= 20:
        risk_level = "high"
        interpretation = "Nguy cơ cao"
        niv_failure_risk = "Cao (50-75%)"
        recommendation = "Cân nhắc đặt nội khí quản sớm"
    else:
        risk_level = "critical"
        interpretation = "Nguy cơ rất cao"
        niv_failure_risk = "Rất cao (>75%)"
        recommendation = "Nên đặt nội khí quản ngay"
    
    return {
        "score": score,
        "max_score": 25,
        "breakdown": breakdown,
        "risk_level": risk_level,
        "interpretation": interpretation,
        "niv_failure_risk": niv_failure_risk,
        "recommendation": recommendation
    }


def render():
    """HACOR Score Calculator"""
    st.markdown(f"""
    <h3 style='text-align: center; color: {COLORS['success']};'>🫁 HACOR Score</h3>
    """, unsafe_allow_html=True)
    st.caption("Dự đoán thất bại thở máy không xâm lấn (NIV) trong suy hô hấp cấp")
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'hacor':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📋 Thông số bệnh nhân")
        
        shared_inputs = st.session_state.get('shared_inputs', {})
        
        heart_rate = st.number_input(
            "**H** - Heart rate (Nhịp tim)",
            min_value=0,
            max_value=300,
            value=int(shared_inputs.get('heart_rate', 100)) if shared_inputs else 100,
            step=1,
            help="Nhịp tim (bpm)"
        )
        
        ph = st.number_input(
            "**A** - pH (Arterial pH)",
            min_value=6.5,
            max_value=7.6,
            value=float(shared_inputs.get('ph', 7.35)) if shared_inputs else 7.35,
            step=0.01,
            format="%.2f",
            help="pH động mạch (bình thường: 7.35-7.45)"
        )
        
        gcs = st.number_input(
            "**C** - GCS (Glasgow Coma Scale)",
            min_value=3,
            max_value=15,
            value=int(shared_inputs.get('gcs', 15)) if shared_inputs else 15,
            step=1,
            help="Glasgow Coma Scale (3-15)"
        )
        
        pao2_fio2 = st.number_input(
            "**O** - PaO₂/FiO₂ ratio",
            min_value=0.0,
            max_value=600.0,
            value=float(shared_inputs.get('pao2_fio2', 200.0)) if shared_inputs else 200.0,
            step=1.0,
            format="%.0f",
            help="PaO2/FiO2 ratio (bình thường: >300)"
        )
        
        respiratory_rate = st.number_input(
            "**R** - Respiratory rate (Nhịp thở)",
            min_value=0,
            max_value=60,
            value=int(shared_inputs.get('respiratory_rate', 20)) if shared_inputs else 20,
            step=1,
            help="Nhịp thở (/min)"
        )
        
        # Validation
        errors = []
        if ph < 6.5 or ph > 7.6:
            errors.append("pH phải trong khoảng 6.5-7.6")
        if gcs < 3 or gcs > 15:
            errors.append("GCS phải trong khoảng 3-15")
        
        if errors:
            st.error("⚠️ Lỗi nhập liệu:")
            for error in errors:
                st.error(f"- {error}")
            return
    
    with col2:
        # Smart Suggestions
        render_suggestions(
            calculator_id="hacor",
            calculator_name="HACOR Score",
            category="Hô hấp",
            show_related=True,
            show_category=True,
            limit=3
        )
        
        # Educational information
        if CALCULATOR_METADATA_AVAILABLE:
            st.markdown("---")
            render_calculator_education("hacor")
        elif CALCULATOR_ENHANCEMENTS_AVAILABLE:
            st.markdown("---")
            render_calculator_explanation(
                title="Về HACOR Score",
                content="""
                **HACOR Score** dự đoán thất bại NIV trong 48 giờ:
                
                **5 yếu tố:**
                1. **H** - Heart rate ≥125: 5 điểm, 105-124: 3 điểm
                2. **A** - pH <7.25: 4 điểm, 7.25-7.29: 2 điểm
                3. **C** - GCS ≤8: 4 điểm, 9-11: 2 điểm
                4. **O** - PaO2/FiO2 <125: 4 điểm, 125-174: 2 điểm
                5. **R** - Respiratory rate ≥35: 4 điểm, 30-34: 2 điểm
                
                **Tổng điểm: 0-25**
                
                **Phân tầng nguy cơ:**
                - <5: Nguy cơ thấp (<15% thất bại)
                - 5-14: Nguy cơ trung bình (15-50%)
                - 15-20: Nguy cơ cao (50-75%)
                - >20: Nguy cơ rất cao (>75%)
                """,
                when_to_use="""
                **Sử dụng khi:**
                - Bệnh nhân đang thở máy không xâm lấn (NIV)
                - Suy hô hấp cấp
                - Cần đánh giá nguy cơ thất bại NIV
                - Quyết định đặt nội khí quản
                """,
                limitations="""
                **Hạn chế:**
                - Dự đoán thất bại trong 48 giờ
                - Cần đánh giá lại thường xuyên
                - Kết hợp với đánh giá lâm sàng
                - Không thay thế quyết định lâm sàng
                """,
                clinical_context="""
                **Bối cảnh lâm sàng:**
                - Score <5: Tiếp tục NIV, theo dõi
                - Score 5-14: Theo dõi sát, đánh giá lại
                - Score ≥15: Cân nhắc đặt nội khí quản
                - Score >20: Nên đặt nội khí quản ngay
                """
            )
    
    st.markdown("---")
    
    # Calculate
    if st.button("🔄 Tính HACOR Score", type="primary", use_container_width=True):
        result = calculate_hacor_score(
            heart_rate,
            ph,
            gcs,
            pao2_fio2,
            respiratory_rate
        )
        
        # Save to history
        save_calculation_to_history(
            calculator_id="hacor",
            calculator_name="HACOR Score",
            inputs={
                "heart_rate": heart_rate,
                "ph": ph,
                "gcs": gcs,
                "pao2_fio2": pao2_fio2,
                "respiratory_rate": respiratory_rate
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
                <h2 style="color: {risk_color}; margin: 0 0 10px 0;">HACOR Score: <strong>{result['score']}/{result['max_score']}</strong></h2>
                <p style="font-size: 1.1em; margin: 5px 0;"><strong>Mức độ nguy cơ:</strong> {result['interpretation']}</p>
                <p style="margin: 5px 0;"><strong>Nguy cơ thất bại NIV:</strong> {result['niv_failure_risk']}</p>
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
            **⚠️ Nguy cơ rất cao (Score >20):**
            - Nguy cơ thất bại NIV >75%
            - Nên đặt nội khí quản ngay
            - Tránh trì hoãn đặt nội khí quản
            - Chuẩn bị sẵn sàng cho đặt nội khí quản
            """)
        elif result['risk_level'] == 'high':
            st.warning(f"""
            **⚠️ Nguy cơ cao (Score 15-20):**
            - Nguy cơ thất bại NIV 50-75%
            - Cân nhắc đặt nội khí quản sớm
            - Theo dõi rất sát
            - Đánh giá lại sau 1-2 giờ
            """)
        elif result['risk_level'] == 'moderate':
            st.info(f"""
            **ℹ️ Nguy cơ trung bình (Score 5-14):**
            - Nguy cơ thất bại NIV 15-50%
            - Theo dõi sát
            - Đánh giá lại thường xuyên
            - Chuẩn bị sẵn sàng cho đặt nội khí quản nếu cần
            """)
        else:
            st.success(f"""
            **✅ Nguy cơ thấp (Score <5):**
            - Nguy cơ thất bại NIV <15%
            - Tiếp tục NIV
            - Theo dõi thường quy
            - Đánh giá lại định kỳ
            """)
        
        # Share and Export
        st.markdown("---")
        col_share1, col_share2 = st.columns(2)
        with col_share1:
            render_share_section(
                calculator_id="hacor",
                calculator_name="HACOR Score",
                result=result
            )
        with col_share2:
            render_scores_export(
                calculator_name="HACOR Score",
                result=result,
                inputs={
                    "Heart rate": f"{heart_rate} bpm",
                    "pH": f"{ph:.2f}",
                    "GCS": gcs,
                    "PaO2/FiO2": f"{pao2_fio2:.0f}",
                    "Respiratory rate": f"{respiratory_rate}/min"
                }
            )
    
    # History
    st.markdown("---")
    render_history_ui("hacor", "HACOR Score")
    
    # References
    st.markdown("---")
    references = get_references("hacor")
    if references:
        render_references_section(references)
