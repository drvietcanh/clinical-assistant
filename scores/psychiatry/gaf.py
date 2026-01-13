"""
GAF - Global Assessment of Functioning
======================================

Assesses overall psychological, social, and occupational functioning.

Reference:
- American Psychiatric Association. Diagnostic and Statistical Manual of Mental Disorders, 4th ed. (DSM-IV). 1994.
- Used in DSM-IV for Axis V assessment

Clinical Utility:
- Assesses overall functioning
- Used in psychiatric evaluations
- Important for treatment planning
- Validated in Vietnamese studies

GAF Scale: 0-100
- 91-100: Superior functioning
- 81-90: Good functioning
- 71-80: Mild symptoms
- 61-70: Moderate symptoms
- 51-60: Moderate to severe symptoms
- 41-50: Serious symptoms
- 31-40: Major impairment
- 21-30: Severe impairment
- 11-20: Some danger
- 1-10: Persistent danger
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


def interpret_gaf(score: int) -> dict:
    """
    Interpret GAF Score
    
    Args:
        score: GAF score (0-100)
    
    Returns:
        dict with interpretation and recommendations
    """
    if score >= 91:
        level = "Superior"
        risk_level = "low"
        description = "Chức năng xuất sắc, không có triệu chứng"
        recommendation = "Không cần điều trị"
    elif score >= 81:
        level = "Good"
        risk_level = "low"
        description = "Chức năng tốt, triệu chứng tối thiểu"
        recommendation = "Theo dõi, không cần điều trị"
    elif score >= 71:
        level = "Mild"
        risk_level = "low"
        description = "Triệu chứng nhẹ, ảnh hưởng tối thiểu"
        recommendation = "Theo dõi, can thiệp nhẹ nếu cần"
    elif score >= 61:
        level = "Moderate"
        risk_level = "moderate"
        description = "Triệu chứng trung bình, ảnh hưởng một số chức năng"
        recommendation = "Cân nhắc điều trị"
    elif score >= 51:
        level = "Moderate-Severe"
        risk_level = "moderate"
        description = "Triệu chứng trung bình-nặng, ảnh hưởng đáng kể"
        recommendation = "Nên điều trị"
    elif score >= 41:
        level = "Serious"
        risk_level = "high"
        description = "Triệu chứng nghiêm trọng, suy giảm chức năng"
        recommendation = "Cần điều trị tích cực"
    elif score >= 31:
        level = "Major Impairment"
        risk_level = "high"
        description = "Suy giảm chức năng lớn, ảnh hưởng nghiêm trọng"
        recommendation = "Cần điều trị tích cực, có thể nhập viện"
    elif score >= 21:
        level = "Severe Impairment"
        risk_level = "critical"
        description = "Suy giảm chức năng nặng"
        recommendation = "Cần nhập viện, điều trị tích cực"
    elif score >= 11:
        level = "Some Danger"
        risk_level = "critical"
        description = "Có nguy cơ tự làm hại bản thân hoặc người khác"
        recommendation = "Nhập viện ngay, điều trị khẩn cấp"
    else:
        level = "Persistent Danger"
        risk_level = "critical"
        description = "Nguy cơ cao tự làm hại bản thân hoặc người khác"
        recommendation = "Nhập viện khẩn cấp, điều trị ngay"
    
    return {
        "score": score,
        "level": level,
        "risk_level": risk_level,
        "description": description,
        "recommendation": recommendation
    }


def render():
    """GAF Score Calculator"""
    st.markdown(f"""
    <h3 style='text-align: center; color: {COLORS['success']};'>🧠 GAF - Global Assessment of Functioning</h3>
    """, unsafe_allow_html=True)
    st.caption("Đánh giá tổng quát chức năng tâm thần, xã hội và nghề nghiệp (Đã được nghiên cứu tại Việt Nam)")
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'gaf':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📋 Đánh giá GAF")
        
        shared_inputs = st.session_state.get('shared_inputs', {})
        
        st.info("""
        **Hướng dẫn:** Đánh giá tổng quát chức năng tâm thần, xã hội và nghề nghiệp của bệnh nhân.
        Xem xét cả triệu chứng tâm thần và mức độ suy giảm chức năng.
        """)
        
        gaf_score = st.slider(
            "GAF Score",
            min_value=0,
            max_value=100,
            value=int(shared_inputs.get('gaf_score', 70)) if shared_inputs else 70,
            step=1,
            help="GAF Score từ 0-100"
        )
        
        # Show ranges
        st.markdown("#### Thang điểm GAF:")
        st.markdown("""
        - **91-100:** Chức năng xuất sắc
        - **81-90:** Chức năng tốt
        - **71-80:** Triệu chứng nhẹ
        - **61-70:** Triệu chứng trung bình
        - **51-60:** Triệu chứng trung bình-nặng
        - **41-50:** Triệu chứng nghiêm trọng
        - **31-40:** Suy giảm chức năng lớn
        - **21-30:** Suy giảm chức năng nặng
        - **11-20:** Có nguy cơ
        - **1-10:** Nguy cơ cao
        """)
    
    with col2:
        # Smart Suggestions
        render_suggestions(
            calculator_id="gaf",
            calculator_name="GAF",
            category="Tâm thần",
            show_related=True,
            show_category=True,
            limit=3
        )
        
        # Educational information
        if CALCULATOR_METADATA_AVAILABLE:
            st.markdown("---")
            render_calculator_education("gaf")
        elif CALCULATOR_ENHANCEMENTS_AVAILABLE:
            st.markdown("---")
            render_calculator_explanation(
                title="Về GAF",
                content="""
                **GAF (Global Assessment of Functioning)** đánh giá:
                
                **Chức năng:**
                - Tâm thần
                - Xã hội
                - Nghề nghiệp
                
                **Thang điểm:** 0-100
                
                **Phân tầng:**
                - 91-100: Xuất sắc
                - 81-90: Tốt
                - 71-80: Nhẹ
                - 61-70: Trung bình
                - 51-60: Trung bình-nặng
                - 41-50: Nghiêm trọng
                - 31-40: Suy giảm lớn
                - 21-30: Suy giảm nặng
                - 11-20: Có nguy cơ
                - 1-10: Nguy cơ cao
                """,
                when_to_use="""
                **Sử dụng khi:**
                - Đánh giá tâm thần tổng quát
                - Lập kế hoạch điều trị
                - Theo dõi tiến triển
                - Đánh giá chức năng
                """,
                limitations="""
                **Hạn chế:**
                - Đánh giá chủ quan
                - Cần đánh giá bởi chuyên gia
                - Không thay thế chẩn đoán
                """,
                clinical_context="""
                **Bối cảnh lâm sàng:**
                - Đã được nghiên cứu tại Việt Nam
                - Sử dụng trong đánh giá tâm thần
                - Quan trọng cho lập kế hoạch điều trị
                """
            )
    
    st.markdown("---")
    
    # Calculate
    if st.button("🔄 Đánh giá GAF", type="primary", use_container_width=True):
        result = interpret_gaf(gaf_score)
        
        # Save to history
        save_calculation_to_history(
            calculator_id="gaf",
            calculator_name="GAF",
            inputs={
                "gaf_score": gaf_score
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
                <h2 style="color: {risk_color}; margin: 0 0 10px 0;">GAF Score: <strong>{result['score']}/100</strong></h2>
                <p style="font-size: 1.1em; margin: 5px 0;"><strong>Mức độ:</strong> {result['level']}</p>
                <p style="margin: 5px 0;"><strong>Mô tả:</strong> {result['description']}</p>
                <p style="margin: 5px 0;"><strong>Khuyến nghị:</strong> {result['recommendation']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col_result2:
            render_risk_badge(result['risk_level'], result['level'])
        
        # Clinical interpretation
        st.markdown("---")
        st.markdown("### 💡 Hướng dẫn lâm sàng")
        
        if result['risk_level'] == 'critical':
            st.error(f"""
            **⚠️ Nguy cơ cao (Score ≤30):**
            - Suy giảm chức năng nặng hoặc có nguy cơ
            - Cần nhập viện và điều trị khẩn cấp
            - Đánh giá nguy cơ tự làm hại
            - Theo dõi sát
            """)
        elif result['risk_level'] == 'high':
            st.warning(f"""
            **⚠️ Nguy cơ tăng (Score 31-50):**
            - Triệu chứng nghiêm trọng hoặc suy giảm chức năng lớn
            - Cần điều trị tích cực
            - Cân nhắc nhập viện
            - Theo dõi sát
            """)
        elif result['risk_level'] == 'moderate':
            st.info(f"""
            **ℹ️ Nguy cơ trung bình (Score 51-70):**
            - Triệu chứng trung bình đến trung bình-nặng
            - Nên điều trị
            - Theo dõi định kỳ
            """)
        else:
            st.success(f"""
            **✅ Nguy cơ thấp (Score ≥71):**
            - Chức năng tốt, triệu chứng nhẹ hoặc không có
            - Theo dõi thường quy
            - Can thiệp nhẹ nếu cần
            """)
        
        # Share and Export
        st.markdown("---")
        col_share1, col_share2 = st.columns(2)
        with col_share1:
            render_share_section(
                calculator_id="gaf",
                calculator_name="GAF",
                result=result
            )
        with col_share2:
            render_scores_export(
                calculator_name="GAF",
                result=result,
                inputs={
                    "GAF Score": gaf_score
                }
            )
    
    # History
    st.markdown("---")
    render_history_ui("gaf", "GAF")
    
    # References
    st.markdown("---")
    references = get_references("gaf")
    if references:
        render_references_section(references)
