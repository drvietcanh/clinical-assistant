"""
SYNTAX Score
============

Evaluates the complexity of coronary artery disease for patients undergoing PCI.

Reference:
- Sianos G, et al. The SYNTAX Score: an angiographic tool grading the complexity of coronary artery disease. 
  EuroIntervention. 2005;1(2):219-27.
- Serruys PW, et al. Percutaneous coronary intervention versus coronary-artery bypass grafting for severe coronary artery disease. 
  N Engl J Med. 2009;360(10):961-72.

Clinical Utility:
- Assesses coronary artery disease complexity
- Guides decision between PCI and CABG
- Predicts outcomes after PCI
- Used in clinical trials and guidelines

Note: Full SYNTAX Score calculation requires detailed angiographic assessment.
This calculator provides a simplified version for educational purposes.
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


def calculate_syntax_score_simplified(
    number_of_lesions: int,
    total_occlusions: int,
    bifurcations: int,
    trifurcations: int,
    aorto_ostial: int,
    severe_tortuosity: int,
    heavy_calcification: int,
    thrombus: int,
    diffuse_disease: int,
    small_vessels: int
) -> dict:
    """
    Simplified SYNTAX Score calculation
    
    Note: Full SYNTAX Score requires detailed angiographic analysis.
    This is a simplified version for educational purposes.
    
    Args:
        number_of_lesions: Total number of lesions
        total_occlusions: Number of total occlusions
        bifurcations: Number of bifurcations
        trifurcations: Number of trifurcations
        aorto_ostial: Number of aorto-ostial lesions
        severe_tortuosity: Number of lesions with severe tortuosity
        heavy_calcification: Number of heavily calcified lesions
        thrombus: Number of lesions with thrombus
        diffuse_disease: Number of segments with diffuse disease
        small_vessels: Number of small vessel lesions (<2.5mm)
    
    Returns:
        dict with estimated score and interpretation
    """
    # Simplified scoring (actual SYNTAX is much more complex)
    score = 0
    
    # Base points for lesions
    score += number_of_lesions * 2
    
    # Additional complexity factors
    score += total_occlusions * 5
    score += bifurcations * 2
    score += trifurcations * 3
    score += aorto_ostial * 1
    score += severe_tortuosity * 2
    score += heavy_calcification * 2
    score += thrombus * 1
    score += diffuse_disease * 1
    score += small_vessels * 1
    
    # Risk stratification
    if score < 23:
        risk_level = "low"
        interpretation = "Độ phức tạp thấp"
        recommendation = "PCI phù hợp"
        complexity = "Low complexity"
    elif score < 33:
        risk_level = "moderate"
        interpretation = "Độ phức tạp trung bình"
        recommendation = "PCI hoặc CABG đều có thể xem xét"
        complexity = "Intermediate complexity"
    else:
        risk_level = "high"
        interpretation = "Độ phức tạp cao"
        recommendation = "Cân nhắc CABG, đặc biệt ở bệnh nhân đái tháo đường"
        complexity = "High complexity"
    
    return {
        "score": score,
        "risk_level": risk_level,
        "interpretation": interpretation,
        "recommendation": recommendation,
        "complexity": complexity,
        "number_of_lesions": number_of_lesions
    }


def render():
    """SYNTAX Score Calculator (Simplified)"""
    st.markdown(f"""
    <h3 style='text-align: center; color: {COLORS['success']};'>❤️ SYNTAX Score</h3>
    """, unsafe_allow_html=True)
    st.caption("Đánh giá độ phức tạp bệnh động mạch vành (Phiên bản đơn giản hóa)")
    
    st.warning("""
    **⚠️ Lưu ý:** Đây là phiên bản đơn giản hóa của SYNTAX Score. 
    SYNTAX Score đầy đủ yêu cầu đánh giá chi tiết từ phim chụp mạch vành và 
    nên được tính bởi chuyên gia tim mạch can thiệp.
    """)
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'syntax_score':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📋 Đánh giá Phim Chụp Mạch Vành")
        
        shared_inputs = st.session_state.get('shared_inputs', {})
        
        number_of_lesions = st.number_input(
            "Số lượng tổn thương",
            min_value=0,
            max_value=20,
            value=int(shared_inputs.get('number_of_lesions', 1)) if shared_inputs else 1,
            step=1,
            help="Tổng số tổn thương cần can thiệp"
        )
        
        total_occlusions = st.number_input(
            "Tổn thương tắc hoàn toàn",
            min_value=0,
            max_value=10,
            value=int(shared_inputs.get('total_occlusions', 0)) if shared_inputs else 0,
            step=1,
            help="Số tổn thương tắc hoàn toàn (100%)"
        )
        
        bifurcations = st.number_input(
            "Tổn thương phân nhánh (Bifurcation)",
            min_value=0,
            max_value=10,
            value=int(shared_inputs.get('bifurcations', 0)) if shared_inputs else 0,
            step=1,
            help="Số tổn thương ở vị trí phân nhánh"
        )
        
        trifurcations = st.number_input(
            "Tổn thương tam phân (Trifurcation)",
            min_value=0,
            max_value=5,
            value=int(shared_inputs.get('trifurcations', 0)) if shared_inputs else 0,
            step=1,
            help="Số tổn thương ở vị trí tam phân"
        )
        
        aorto_ostial = st.number_input(
            "Tổn thương aorto-ostial",
            min_value=0,
            max_value=5,
            value=int(shared_inputs.get('aorto_ostial', 0)) if shared_inputs else 0,
            step=1,
            help="Tổn thương ở gốc động mạch vành"
        )
        
        severe_tortuosity = st.number_input(
            "Tổn thương có độ cong nặng",
            min_value=0,
            max_value=10,
            value=int(shared_inputs.get('severe_tortuosity', 0)) if shared_inputs else 0,
            step=1,
            help="Tổn thương có độ cong nặng (>90 độ)"
        )
        
        heavy_calcification = st.number_input(
            "Tổn thương vôi hóa nặng",
            min_value=0,
            max_value=10,
            value=int(shared_inputs.get('heavy_calcification', 0)) if shared_inputs else 0,
            step=1,
            help="Tổn thương có vôi hóa nặng"
        )
        
        thrombus = st.number_input(
            "Tổn thương có huyết khối",
            min_value=0,
            max_value=10,
            value=int(shared_inputs.get('thrombus', 0)) if shared_inputs else 0,
            step=1,
            help="Tổn thương có huyết khối"
        )
        
        diffuse_disease = st.number_input(
            "Tổn thương lan tỏa",
            min_value=0,
            max_value=10,
            value=int(shared_inputs.get('diffuse_disease', 0)) if shared_inputs else 0,
            step=1,
            help="Số đoạn mạch có bệnh lan tỏa"
        )
        
        small_vessels = st.number_input(
            "Tổn thương mạch nhỏ (<2.5mm)",
            min_value=0,
            max_value=10,
            value=int(shared_inputs.get('small_vessels', 0)) if shared_inputs else 0,
            step=1,
            help="Số tổn thương ở mạch nhỏ (<2.5mm)"
        )
    
    with col2:
        # Smart Suggestions
        render_suggestions(
            calculator_id="syntax_score",
            calculator_name="SYNTAX Score",
            category="Tim mạch",
            show_related=True,
            show_category=True,
            limit=3
        )
        
        # Educational information
        if CALCULATOR_METADATA_AVAILABLE:
            st.markdown("---")
            render_calculator_education("syntax_score")
        elif CALCULATOR_ENHANCEMENTS_AVAILABLE:
            st.markdown("---")
            render_calculator_explanation(
                title="Về SYNTAX Score",
                content="""
                **SYNTAX Score** đánh giá độ phức tạp bệnh động mạch vành:
                
                **Các yếu tố:**
                - Số lượng và vị trí tổn thương
                - Tắc hoàn toàn
                - Phân nhánh/tam phân
                - Aorto-ostial
                - Độ cong nặng
                - Vôi hóa nặng
                - Huyết khối
                - Bệnh lan tỏa
                - Mạch nhỏ
                
                **Phân tầng:**
                - <23: Độ phức tạp thấp → PCI phù hợp
                - 23-32: Độ phức tạp trung bình → PCI hoặc CABG
                - ≥33: Độ phức tạp cao → Cân nhắc CABG
                """,
                when_to_use="""
                **Sử dụng khi:**
                - Bệnh nhân cần can thiệp mạch vành
                - Quyết định giữa PCI và CABG
                - Đánh giá tiên lượng sau PCI
                """,
                limitations="""
                **Hạn chế:**
                - Cần đánh giá chi tiết từ phim chụp mạch
                - Nên được tính bởi chuyên gia can thiệp
                - Phiên bản này là đơn giản hóa
                """,
                clinical_context="""
                **Bối cảnh lâm sàng:**
                - Score <23: PCI phù hợp
                - Score 23-32: Cân nhắc PCI hoặc CABG
                - Score ≥33: Cân nhắc CABG, đặc biệt ở bệnh nhân đái tháo đường
                """
            )
    
    st.markdown("---")
    
    # Calculate
    if st.button("🔄 Tính SYNTAX Score", type="primary", use_container_width=True):
        result = calculate_syntax_score_simplified(
            number_of_lesions,
            total_occlusions,
            bifurcations,
            trifurcations,
            aorto_ostial,
            severe_tortuosity,
            heavy_calcification,
            thrombus,
            diffuse_disease,
            small_vessels
        )
        
        # Save to history
        save_calculation_to_history(
            calculator_id="syntax_score",
            calculator_name="SYNTAX Score",
            inputs={
                "number_of_lesions": number_of_lesions,
                "total_occlusions": total_occlusions,
                "bifurcations": bifurcations,
                "trifurcations": trifurcations,
                "aorto_ostial": aorto_ostial,
                "severe_tortuosity": severe_tortuosity,
                "heavy_calcification": heavy_calcification,
                "thrombus": thrombus,
                "diffuse_disease": diffuse_disease,
                "small_vessels": small_vessels
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
                "high": COLORS['warning']
            }.get(result['risk_level'], COLORS['info'])
            
            st.markdown(f"""
            <div style="background: white; padding: 20px; border-radius: 8px; border-left: 4px solid {risk_color}; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                <h2 style="color: {risk_color}; margin: 0 0 10px 0;">SYNTAX Score: <strong>{result['score']}</strong></h2>
                <p style="font-size: 1.1em; margin: 5px 0;"><strong>Độ phức tạp:</strong> {result['complexity']}</p>
                <p style="margin: 5px 0;"><strong>Mức độ:</strong> {result['interpretation']}</p>
                <p style="margin: 5px 0;"><strong>Khuyến nghị:</strong> {result['recommendation']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col_result2:
            render_risk_badge(result['risk_level'], result['interpretation'])
        
        # Clinical interpretation
        st.markdown("---")
        st.markdown("### 💡 Hướng dẫn lâm sàng")
        
        if result['risk_level'] == 'high':
            st.warning(f"""
            **⚠️ Độ phức tạp cao (Score ≥33):**
            - Bệnh động mạch vành phức tạp
            - Cân nhắc CABG, đặc biệt ở bệnh nhân đái tháo đường
            - PCI vẫn có thể thực hiện nhưng tiên lượng có thể kém hơn
            - Thảo luận Heart Team
            """)
        elif result['risk_level'] == 'moderate':
            st.info(f"""
            **ℹ️ Độ phức tạp trung bình (Score 23-32):**
            - Bệnh động mạch vành độ phức tạp trung bình
            - PCI hoặc CABG đều có thể xem xét
            - Quyết định dựa trên đặc điểm bệnh nhân và Heart Team
            """)
        else:
            st.success(f"""
            **✅ Độ phức tạp thấp (Score <23):**
            - Bệnh động mạch vành đơn giản
            - PCI phù hợp
            - Tiên lượng tốt với PCI
            """)
        
        # Share and Export
        st.markdown("---")
        col_share1, col_share2 = st.columns(2)
        with col_share1:
            render_share_section(
                calculator_id="syntax_score",
                calculator_name="SYNTAX Score",
                result=result
            )
        with col_share2:
            render_scores_export(
                calculator_name="SYNTAX Score",
                result=result,
                inputs={
                    "Number of lesions": number_of_lesions,
                    "Total occlusions": total_occlusions,
                    "Bifurcations": bifurcations,
                    "SYNTAX Score": result['score']
                }
            )
    
    # History
    st.markdown("---")
    render_history_ui("syntax_score", "SYNTAX Score")
    
    # References
    st.markdown("---")
    references = get_references("syntax_score")
    if references:
        render_references_section(references)
