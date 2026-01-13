"""
Marshall Score
==============

Classification system for traumatic brain injury (TBI) severity based on CT findings.

Reference:
- Marshall LF, et al. The diagnosis of head injury requires a classification based on computed axial tomography. 
  J Neurotrauma. 1992;9 Suppl 1:S287-92.
- Maas AI, et al. Prognostic value of computerized tomography scan characteristics in traumatic brain injury: 
  results from the IMPACT study. J Neurotrauma. 2007;24(2):303-14.

Clinical Utility:
- Classifies TBI severity based on CT
- Predicts outcome in TBI
- Guides treatment decisions
- Used in trauma centers worldwide

Marshall Classification:
- Diffuse Injury I: No visible pathology
- Diffuse Injury II: Cisterns present, shift <5mm, no high/mixed density lesion >25cc
- Diffuse Injury III: Cisterns compressed/absent, shift <5mm, no high/mixed density lesion >25cc
- Diffuse Injury IV: Shift >5mm, no high/mixed density lesion >25cc
- Evacuated Mass Lesion: Any surgically evacuated lesion
- Non-evacuated Mass Lesion: High/mixed density lesion >25cc, not surgically evacuated
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


def classify_marshall(
    visible_pathology: bool,
    cisterns_present: bool,
    midline_shift_mm: float,
    high_density_lesion_cc: float,
    surgically_evacuated: bool
) -> dict:
    """
    Classify TBI according to Marshall Score
    
    Args:
        visible_pathology: Any visible pathology on CT
        cisterns_present: Basal cisterns present
        midline_shift_mm: Midline shift in mm
        high_density_lesion_cc: High/mixed density lesion volume (cc)
        surgically_evacuated: Lesion surgically evacuated
    
    Returns:
        dict with Marshall classification and interpretation
    """
    # Marshall Classification
    if not visible_pathology:
        classification = "Diffuse Injury I"
        risk_level = "low"
        interpretation = "Không có tổn thương rõ ràng"
        mortality = "Thấp (<10%)"
        recommendation = "Theo dõi thường quy"
    elif high_density_lesion_cc > 25:
        if surgically_evacuated:
            classification = "Evacuated Mass Lesion"
            risk_level = "moderate"
            interpretation = "Tổn thương khối đã phẫu thuật"
            mortality = "Trung bình (20-30%)"
            recommendation = "Theo dõi sát sau phẫu thuật"
        else:
            classification = "Non-evacuated Mass Lesion"
            risk_level = "critical"
            interpretation = "Tổn thương khối chưa phẫu thuật"
            mortality = "Cao (>40%)"
            recommendation = "Cân nhắc phẫu thuật khẩn cấp"
    elif midline_shift_mm > 5:
        classification = "Diffuse Injury IV"
        risk_level = "high"
        interpretation = "Lệch đường giữa >5mm, không có tổn thương khối >25cc"
        mortality = "Cao (30-40%)"
        recommendation = "Điều trị tích cực, cân nhắc ICP monitoring"
    elif not cisterns_present:
        classification = "Diffuse Injury III"
        risk_level = "moderate"
        interpretation = "Cisterns bị nén/không thấy, lệch <5mm"
        mortality = "Trung bình (20-30%)"
        recommendation = "Theo dõi sát, cân nhắc ICP monitoring"
    else:
        classification = "Diffuse Injury II"
        risk_level = "low"
        interpretation = "Cisterns còn, lệch <5mm, không có tổn thương khối >25cc"
        mortality = "Thấp (10-20%)"
        recommendation = "Theo dõi thường quy"
    
    return {
        "classification": classification,
        "risk_level": risk_level,
        "interpretation": interpretation,
        "mortality": mortality,
        "recommendation": recommendation,
        "midline_shift_mm": midline_shift_mm,
        "high_density_lesion_cc": high_density_lesion_cc
    }


def render():
    """Marshall Score Calculator"""
    st.markdown(f"""
    <h3 style='text-align: center; color: {COLORS['success']};'>🚨 Marshall Score</h3>
    """, unsafe_allow_html=True)
    st.caption("Phân loại mức độ nặng chấn thương sọ não dựa trên CT scan")
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'marshall_score':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📋 Đánh giá CT Scan")
        
        shared_inputs = st.session_state.get('shared_inputs', {})
        
        visible_pathology = st.checkbox(
            "Có tổn thương rõ ràng trên CT",
            help="Có bất kỳ tổn thương nào thấy rõ trên CT scan",
            value=shared_inputs.get('visible_pathology') == 'Có' if shared_inputs else True
        )
        
        if visible_pathology:
            cisterns_present = st.checkbox(
                "Basal cisterns còn thấy",
                help="Basal cisterns còn thấy rõ trên CT",
                value=shared_inputs.get('cisterns_present') == 'Có' if shared_inputs else True
            )
            
            midline_shift_mm = st.number_input(
                "Lệch đường giữa (mm)",
                min_value=0.0,
                max_value=20.0,
                value=float(shared_inputs.get('midline_shift_mm', 0.0)) if shared_inputs else 0.0,
                step=0.5,
                format="%.1f",
                help="Lệch đường giữa (mm)"
            )
            
            high_density_lesion_cc = st.number_input(
                "Thể tích tổn thương đậm độ cao/hỗn hợp (cc)",
                min_value=0.0,
                max_value=200.0,
                value=float(shared_inputs.get('high_density_lesion_cc', 0.0)) if shared_inputs else 0.0,
                step=1.0,
                format="%.1f",
                help="Thể tích tổn thương đậm độ cao/hỗn hợp (cc)"
            )
            
            if high_density_lesion_cc > 25:
                surgically_evacuated = st.checkbox(
                    "Đã phẫu thuật lấy tổn thương",
                    help="Tổn thương đã được phẫu thuật lấy ra",
                    value=shared_inputs.get('surgically_evacuated') == 'Có' if shared_inputs else False
                )
            else:
                surgically_evacuated = False
        else:
            cisterns_present = True
            midline_shift_mm = 0.0
            high_density_lesion_cc = 0.0
            surgically_evacuated = False
    
    with col2:
        # Smart Suggestions
        render_suggestions(
            calculator_id="marshall_score",
            calculator_name="Marshall Score",
            category="Cấp cứu",
            show_related=True,
            show_category=True,
            limit=3
        )
        
        # Educational information
        if CALCULATOR_METADATA_AVAILABLE:
            st.markdown("---")
            render_calculator_education("marshall_score")
        elif CALCULATOR_ENHANCEMENTS_AVAILABLE:
            st.markdown("---")
            render_calculator_explanation(
                title="Về Marshall Score",
                content="""
                **Marshall Score** phân loại chấn thương sọ não:
                
                **6 phân loại:**
                1. **Diffuse Injury I:** Không có tổn thương rõ
                2. **Diffuse Injury II:** Cisterns còn, lệch <5mm
                3. **Diffuse Injury III:** Cisterns nén, lệch <5mm
                4. **Diffuse Injury IV:** Lệch >5mm
                5. **Evacuated Mass Lesion:** Tổn thương khối đã phẫu thuật
                6. **Non-evacuated Mass Lesion:** Tổn thương khối chưa phẫu thuật
                
                **Tiên lượng:**
                - DI I-II: Tử vong thấp (10-20%)
                - DI III: Tử vong trung bình (20-30%)
                - DI IV: Tử vong cao (30-40%)
                - Mass lesion: Tử vong cao (>40%)
                """,
                when_to_use="""
                **Sử dụng khi:**
                - Bệnh nhân chấn thương sọ não
                - Có CT scan
                - Cần phân loại mức độ nặng
                """,
                limitations="""
                **Hạn chế:**
                - Dựa trên CT scan ban đầu
                - Cần đánh giá lâm sàng kèm theo
                - Không thay thế GCS và đánh giá lâm sàng
                """,
                clinical_context="""
                **Bối cảnh lâm sàng:**
                - DI I-II: Theo dõi thường quy
                - DI III-IV: Cân nhắc ICP monitoring
                - Mass lesion: Cân nhắc phẫu thuật
                """
            )
    
    st.markdown("---")
    
    # Calculate
    if st.button("🔄 Phân loại Marshall", type="primary", use_container_width=True):
        result = classify_marshall(
            visible_pathology,
            cisterns_present if visible_pathology else True,
            midline_shift_mm if visible_pathology else 0.0,
            high_density_lesion_cc if visible_pathology else 0.0,
            surgically_evacuated if (visible_pathology and high_density_lesion_cc > 25) else False
        )
        
        # Save to history
        save_calculation_to_history(
            calculator_id="marshall_score",
            calculator_name="Marshall Score",
            inputs={
                "visible_pathology": "Có" if visible_pathology else "Không",
                "cisterns_present": "Có" if (visible_pathology and cisterns_present) else "N/A",
                "midline_shift_mm": midline_shift_mm if visible_pathology else 0,
                "high_density_lesion_cc": high_density_lesion_cc if visible_pathology else 0,
                "surgically_evacuated": "Có" if surgically_evacuated else "Không"
            },
            result=result
        )
        
        # Display result
        st.markdown("### 📊 Kết quả")
        
        # Main result card
        risk_color = {
            "low": COLORS['success'],
            "moderate": "#FFA500",
            "high": COLORS['warning'],
            "critical": COLORS['danger']
        }.get(result['risk_level'], COLORS['info'])
        
        st.markdown(f"""
        <div style="background: white; padding: 20px; border-radius: 8px; border-left: 4px solid {risk_color}; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
            <h2 style="color: {risk_color}; margin: 0 0 10px 0;">{result['classification']}</h2>
            <p style="font-size: 1.1em; margin: 5px 0;"><strong>Mô tả:</strong> {result['interpretation']}</p>
            <p style="margin: 5px 0;"><strong>Tử vong:</strong> {result['mortality']}</p>
            <p style="margin: 5px 0;"><strong>Khuyến nghị:</strong> {result['recommendation']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Clinical interpretation
        st.markdown("---")
        st.markdown("### 💡 Hướng dẫn lâm sàng")
        
        if result['risk_level'] == 'critical':
            st.error(f"""
            **⚠️ Non-evacuated Mass Lesion:**
            - Tử vong >40%
            - Cân nhắc phẫu thuật khẩn cấp
            - ICP monitoring
            - Điều trị tích cực
            """)
        elif result['risk_level'] == 'high':
            st.warning(f"""
            **⚠️ Diffuse Injury IV:**
            - Tử vong 30-40%
            - Điều trị tích cực
            - Cân nhắc ICP monitoring
            - Theo dõi sát
            """)
        elif result['risk_level'] == 'moderate':
            st.info(f"""
            **ℹ️ Diffuse Injury III hoặc Evacuated Mass Lesion:**
            - Tử vong 20-30%
            - Theo dõi sát
            - Cân nhắc ICP monitoring
            """)
        else:
            st.success(f"""
            **✅ Diffuse Injury I-II:**
            - Tử vong 10-20%
            - Theo dõi thường quy
            - Tiên lượng tốt
            """)
        
        # Share and Export
        st.markdown("---")
        col_share1, col_share2 = st.columns(2)
        with col_share1:
            render_share_section(
                calculator_id="marshall_score",
                calculator_name="Marshall Score",
                result=result
            )
        with col_share2:
            render_scores_export(
                calculator_name="Marshall Score",
                result=result,
                inputs={
                    "Classification": result['classification'],
                    "Mortality": result['mortality']
                }
            )
    
    # History
    st.markdown("---")
    render_history_ui("marshall_score", "Marshall Score")
    
    # References
    st.markdown("---")
    references = get_references("marshall_score")
    if references:
        render_references_section(references)
