"""
MuLBSTA Score
=============

MuLBSTA Score for predicting mortality in viral pneumonia.

Reference:
- Guo L, et al. Development and validation of a mortality risk prediction model for patients with viral pneumonia. 
  J Infect. 2020;81(3):453-460.
- Validated for COVID-19, influenza, and other viral pneumonias

Clinical Utility:
- Predicts mortality risk in viral pneumonia
- Particularly useful for COVID-19 and influenza
- Helps guide treatment intensity and ICU admission decisions
- Important for resource-limited settings

MuLBSTA Components:
1. Multilobular infiltration (on imaging)
2. Lymphopenia (<0.8 x 10^9/L)
3. Bacterial coinfection
4. Smoking history
5. Thrombocytopenia (<100 x 10^9/L)
6. Age (≥60 years)

Score: 0-22 points
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


def calculate_mulbsta_score(
    multilobular_infiltration: bool,
    lymphopenia: bool,
    bacterial_coinfection: bool,
    smoking_history: bool,
    thrombocytopenia: bool,
    age: int
) -> dict:
    """
    Calculate MuLBSTA Score
    
    Args:
        multilobular_infiltration: Multilobular infiltration on imaging
        lymphopenia: Lymphocyte count <0.8 x 10^9/L
        bacterial_coinfection: Bacterial coinfection present
        smoking_history: History of smoking
        thrombocytopenia: Platelet count <100 x 10^9/L
        age: Patient age (years)
    
    Returns:
        dict with score, risk level, and mortality prediction
    """
    score = 0
    breakdown = []
    
    # Multilobular infiltration: 5 points
    if multilobular_infiltration:
        score += 5
        breakdown.append({"label": "Multilobular infiltration", "points": 5, "value": "Có"})
    else:
        breakdown.append({"label": "Multilobular infiltration", "points": 0, "value": "Không"})
    
    # Lymphopenia: 4 points
    if lymphopenia:
        score += 4
        breakdown.append({"label": "Lymphopenia (<0.8 x 10⁹/L)", "points": 4, "value": "Có"})
    else:
        breakdown.append({"label": "Lymphopenia (<0.8 x 10⁹/L)", "points": 0, "value": "Không"})
    
    # Bacterial coinfection: 4 points
    if bacterial_coinfection:
        score += 4
        breakdown.append({"label": "Nhiễm khuẩn đồng nhiễm", "points": 4, "value": "Có"})
    else:
        breakdown.append({"label": "Nhiễm khuẩn đồng nhiễm", "points": 0, "value": "Không"})
    
    # Smoking history: 3 points
    if smoking_history:
        score += 3
        breakdown.append({"label": "Tiền sử hút thuốc", "points": 3, "value": "Có"})
    else:
        breakdown.append({"label": "Tiền sử hút thuốc", "points": 0, "value": "Không"})
    
    # Thrombocytopenia: 2 points
    if thrombocytopenia:
        score += 2
        breakdown.append({"label": "Giảm tiểu cầu (<100 x 10⁹/L)", "points": 2, "value": "Có"})
    else:
        breakdown.append({"label": "Giảm tiểu cầu (<100 x 10⁹/L)", "points": 0, "value": "Không"})
    
    # Age ≥60: 4 points
    if age >= 60:
        score += 4
        breakdown.append({"label": "Tuổi ≥60", "points": 4, "value": f"{age} tuổi"})
    else:
        breakdown.append({"label": "Tuổi ≥60", "points": 0, "value": f"{age} tuổi"})
    
    # Risk stratification based on score
    if score <= 5:
        risk_level = "low"
        interpretation = "Nguy cơ thấp"
        mortality_risk = "Thấp (<5%)"
        recommendation = "Điều trị ngoại trú hoặc nội trú thường quy"
    elif score <= 11:
        risk_level = "moderate"
        interpretation = "Nguy cơ trung bình"
        mortality_risk = "Trung bình (5-15%)"
        recommendation = "Nội trú, theo dõi sát, cân nhắc điều trị tích cực"
    elif score <= 17:
        risk_level = "high"
        interpretation = "Nguy cơ cao"
        mortality_risk = "Cao (15-30%)"
        recommendation = "Nội trú điều trị tích cực, cân nhắc ICU"
    else:
        risk_level = "critical"
        interpretation = "Nguy cơ rất cao"
        mortality_risk = "Rất cao (>30%)"
        recommendation = "ICU ngay, điều trị tích cực tối đa"
    
    return {
        "score": score,
        "max_score": 22,
        "breakdown": breakdown,
        "risk_level": risk_level,
        "interpretation": interpretation,
        "mortality_risk": mortality_risk,
        "recommendation": recommendation,
        "age": age
    }


def render():
    """MuLBSTA Score Calculator"""
    st.markdown(f"""
    <h3 style='text-align: center; color: {COLORS['success']};'>🫁 MuLBSTA Score</h3>
    """, unsafe_allow_html=True)
    st.caption("Dự đoán nguy cơ tử vong trong viêm phổi do virus (COVID-19, cúm, ...)")
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'mulbsta':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📋 Tiêu chí Đánh giá")
        
        # Pre-fill from shared result if available
        shared_inputs = st.session_state.get('shared_inputs', {})
        
        multilobular = st.checkbox(
            "**M** - Multilobular infiltration (Tổn thương đa thùy trên hình ảnh)",
            help="Tổn thương đa thùy trên X-quang hoặc CT ngực",
            value=shared_inputs.get('multilobular') == 'Có' if shared_inputs else False
        )
        
        lymphopenia = st.checkbox(
            "**L** - Lymphopenia (Giảm bạch cầu lympho)",
            help="Số lượng bạch cầu lympho <0.8 x 10⁹/L",
            value=shared_inputs.get('lymphopenia') == 'Có' if shared_inputs else False
        )
        
        bacterial_coinfection = st.checkbox(
            "**B** - Bacterial coinfection (Nhiễm khuẩn đồng nhiễm)",
            help="Có bằng chứng nhiễm khuẩn đồng nhiễm",
            value=shared_inputs.get('bacterial_coinfection') == 'Có' if shared_inputs else False
        )
        
        smoking = st.checkbox(
            "**S** - Smoking history (Tiền sử hút thuốc)",
            help="Tiền sử hút thuốc lá",
            value=shared_inputs.get('smoking') == 'Có' if shared_inputs else False
        )
        
        thrombocytopenia = st.checkbox(
            "**T** - Thrombocytopenia (Giảm tiểu cầu)",
            help="Số lượng tiểu cầu <100 x 10⁹/L",
            value=shared_inputs.get('thrombocytopenia') == 'Có' if shared_inputs else False
        )
        
        age = st.number_input(
            "**A** - Age (Tuổi)",
            min_value=0,
            max_value=120,
            value=int(shared_inputs.get('age', 50)) if shared_inputs else 50,
            step=1,
            help="Tuổi bệnh nhân (năm)"
        )
        
        # Validation
        errors = []
        if age < 0:
            errors.append("Tuổi phải ≥ 0")
        
        if errors:
            st.error("⚠️ Lỗi nhập liệu:")
            for error in errors:
                st.error(f"- {error}")
            return
    
    with col2:
        # Smart Suggestions
        render_suggestions(
            calculator_id="mulbsta",
            calculator_name="MuLBSTA Score",
            category="Hô hấp",
            show_related=True,
            show_category=True,
            limit=3
        )
        
        # Educational information
        if CALCULATOR_METADATA_AVAILABLE:
            st.markdown("---")
            render_calculator_education("mulbsta")
        elif CALCULATOR_ENHANCEMENTS_AVAILABLE:
            st.markdown("---")
            render_calculator_explanation(
                title="Về MuLBSTA Score",
                content="""
                **MuLBSTA Score** dự đoán nguy cơ tử vong trong viêm phổi do virus:
                
                **6 yếu tố:**
                1. **M** - Multilobular infiltration (5 điểm)
                2. **L** - Lymphopenia <0.8 x 10⁹/L (4 điểm)
                3. **B** - Bacterial coinfection (4 điểm)
                4. **S** - Smoking history (3 điểm)
                5. **T** - Thrombocytopenia <100 x 10⁹/L (2 điểm)
                6. **A** - Age ≥60 (4 điểm)
                
                **Tổng điểm: 0-22**
                
                **Phân tầng nguy cơ:**
                - ≤5: Nguy cơ thấp (<5% tử vong)
                - 6-11: Nguy cơ trung bình (5-15%)
                - 12-17: Nguy cơ cao (15-30%)
                - ≥18: Nguy cơ rất cao (>30%)
                """,
                when_to_use="""
                **Sử dụng khi:**
                - Bệnh nhân viêm phổi do virus (COVID-19, cúm, ...)
                - Cần đánh giá nguy cơ tử vong
                - Quyết định mức độ điều trị và nơi điều trị
                - Phân bổ tài nguyên trong đại dịch
                """,
                limitations="""
                **Hạn chế:**
                - Dựa trên nghiên cứu ban đầu, cần validation thêm
                - Các yếu tố có thể thay đổi theo thời gian
                - Cần kết hợp với đánh giá lâm sàng
                - Không thay thế quyết định lâm sàng
                """,
                clinical_context="""
                **Bối cảnh lâm sàng:**
                - Đặc biệt hữu ích cho COVID-19 và cúm
                - Giúp phân tầng bệnh nhân trong đại dịch
                - Hướng dẫn quyết định ICU và điều trị tích cực
                - Quan trọng cho các nước có nguồn lực hạn chế
                """
            )
    
    st.markdown("---")
    
    # Calculate
    if st.button("🔄 Tính MuLBSTA Score", type="primary", use_container_width=True):
        result = calculate_mulbsta_score(
            multilobular,
            lymphopenia,
            bacterial_coinfection,
            smoking,
            thrombocytopenia,
            age
        )
        
        # Save to history
        save_calculation_to_history(
            calculator_id="mulbsta",
            calculator_name="MuLBSTA Score",
            inputs={
                "multilobular": "Có" if multilobular else "Không",
                "lymphopenia": "Có" if lymphopenia else "Không",
                "bacterial_coinfection": "Có" if bacterial_coinfection else "Không",
                "smoking": "Có" if smoking else "Không",
                "thrombocytopenia": "Có" if thrombocytopenia else "Không",
                "age": age
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
                <h2 style="color: {risk_color}; margin: 0 0 10px 0;">MuLBSTA Score: <strong>{result['score']}/{result['max_score']}</strong></h2>
                <p style="font-size: 1.1em; margin: 5px 0;"><strong>Mức độ nguy cơ:</strong> {result['interpretation']}</p>
                <p style="margin: 5px 0;"><strong>Nguy cơ tử vong:</strong> {result['mortality_risk']}</p>
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
            **⚠️ Nguy cơ rất cao (Score ≥18):**
            - Nguy cơ tử vong >30%
            - Cần nhập ICU ngay lập tức
            - Điều trị tích cực tối đa
            - Theo dõi sát các dấu hiệu sinh tồn
            - Xem xét các biện pháp hỗ trợ hô hấp
            """)
        elif result['risk_level'] == 'high':
            st.warning(f"""
            **⚠️ Nguy cơ cao (Score 12-17):**
            - Nguy cơ tử vong 15-30%
            - Nội trú điều trị tích cực
            - Cân nhắc nhập ICU
            - Theo dõi sát, đánh giá thường xuyên
            - Chuẩn bị các biện pháp hỗ trợ nếu cần
            """)
        elif result['risk_level'] == 'moderate':
            st.info(f"""
            **ℹ️ Nguy cơ trung bình (Score 6-11):**
            - Nguy cơ tử vong 5-15%
            - Nội trú điều trị
            - Theo dõi sát các dấu hiệu sinh tồn
            - Đánh giá lại thường xuyên
            - Cân nhắc điều trị tích cực nếu diễn biến xấu
            """)
        else:
            st.success(f"""
            **✅ Nguy cơ thấp (Score ≤5):**
            - Nguy cơ tử vong <5%
            - Có thể điều trị ngoại trú hoặc nội trú thường quy
            - Theo dõi thường quy
            - Đánh giá lại nếu có diễn biến xấu
            """)
        
        # Share and Export
        st.markdown("---")
        col_share1, col_share2 = st.columns(2)
        with col_share1:
            render_share_section(
                calculator_id="mulbsta",
                calculator_name="MuLBSTA Score",
                result=result
            )
        with col_share2:
            render_scores_export(
                calculator_name="MuLBSTA Score",
                result=result,
                inputs={
                    "Multilobular infiltration": "Có" if multilobular else "Không",
                    "Lymphopenia": "Có" if lymphopenia else "Không",
                    "Bacterial coinfection": "Có" if bacterial_coinfection else "Không",
                    "Smoking history": "Có" if smoking else "Không",
                    "Thrombocytopenia": "Có" if thrombocytopenia else "Không",
                    "Age": f"{age} tuổi"
                }
            )
    
    # History
    st.markdown("---")
    render_history_ui("mulbsta", "MuLBSTA Score")
    
    # References
    st.markdown("---")
    references = get_references("mulbsta")
    if references:
        render_references_section(references)
