"""
Shock Index Calculator
======================

Shock Index = Heart Rate / Systolic Blood Pressure

A simple, rapid indicator of hemodynamic instability and shock.

Reference:
- Rady MY, et al. Shock index: a re-evaluation in acute circulatory failure. Resuscitation. 1992;23(3):227-34.
- Cannon CM, et al. The shock index and early recognition of sepsis in the emergency department: a pilot study. West J Emerg Med. 2013;14(2):168-74.
- Rady MY, et al. Shock index: an effective predictor of outcome in emergency department patients with suspected sepsis. West J Emerg Med. 2015;16(7):1039-45.

Clinical Utility:
- Rapid assessment of hemodynamic status
- Early detection of shock
- Predicts mortality and need for intensive care
- Simple calculation, no lab tests needed
- Used daily in emergency departments

Normal Shock Index: 0.5-0.7
Elevated (>0.9): Indicates potential shock
"""

import streamlit as st
from config.theme import COLORS
from scores.utils.validation import (
    validate_heart_rate,
    validate_blood_pressure
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


def calculate_shock_index(heart_rate: float, systolic_bp: float) -> dict:
    """
    Calculate Shock Index
    
    Args:
        heart_rate: Heart rate (bpm)
        systolic_bp: Systolic blood pressure (mmHg)
    
    Returns:
        dict with shock index, interpretation, and clinical guidance
    """
    if systolic_bp == 0:
        return {
            "error": "Systolic BP cannot be zero"
        }
    
    shock_index = heart_rate / systolic_bp
    
    # Interpretation based on literature
    if shock_index < 0.5:
        interpretation = "Thấp"
        risk_level = "low"
        clinical_meaning = "Bình thường hoặc có thể do thuốc chẹn beta"
        action = "Theo dõi thường quy"
    elif shock_index <= 0.7:
        interpretation = "Bình thường"
        risk_level = "low"
        clinical_meaning = "Giá trị bình thường"
        action = "Theo dõi thường quy"
    elif shock_index <= 0.9:
        interpretation = "Tăng nhẹ"
        risk_level = "moderate"
        clinical_meaning = "Có thể có bất ổn huyết động nhẹ"
        action = "Theo dõi sát, đánh giá thêm"
    elif shock_index <= 1.2:
        interpretation = "Tăng"
        risk_level = "high"
        clinical_meaning = "Có thể có sốc, cần đánh giá ngay"
        action = "Đánh giá sốc, xem xét hồi sức dịch"
    else:
        interpretation = "Tăng rất cao"
        risk_level = "critical"
        clinical_meaning = "Nguy cơ sốc cao, tiên lượng xấu"
        action = "Hồi sức ngay, cân nhắc ICU"
    
    # Mortality risk (based on studies)
    if shock_index > 1.0:
        mortality_risk = "Tăng cao"
    elif shock_index > 0.9:
        mortality_risk = "Tăng"
    else:
        mortality_risk = "Bình thường"
    
    return {
        "shock_index": round(shock_index, 2),
        "heart_rate": heart_rate,
        "systolic_bp": systolic_bp,
        "interpretation": interpretation,
        "risk_level": risk_level,
        "clinical_meaning": clinical_meaning,
        "action": action,
        "mortality_risk": mortality_risk,
        "normal_range": "0.5-0.7"
    }


def render():
    """Shock Index Calculator"""
    st.markdown(f"""
    <h3 style='text-align: center; color: {COLORS['success']};'>🚨 Shock Index</h3>
    """, unsafe_allow_html=True)
    st.caption("Chỉ số sốc = Nhịp tim / Huyết áp tâm thu - Đánh giá nhanh tình trạng huyết động")
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'shock_index':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📋 Thông số bệnh nhân")
        
        # Pre-fill from shared result if available
        shared_inputs = st.session_state.get('shared_inputs', {})
        
        heart_rate = st.number_input(
            "Nhịp tim (bpm)",
            min_value=0.0,
            max_value=300.0,
            value=float(shared_inputs.get('heart_rate', 80)) if shared_inputs else 80.0,
            step=1.0,
            help="Nhịp tim (nhịp/phút)"
        )
        
        systolic_bp = st.number_input(
            "Huyết áp tâm thu (mmHg)",
            min_value=0.0,
            max_value=300.0,
            value=float(shared_inputs.get('systolic_bp', 120)) if shared_inputs else 120.0,
            step=1.0,
            help="Huyết áp tâm thu (mmHg)"
        )
        
        # Validation
        errors = []
        if heart_rate <= 0:
            errors.append("Nhịp tim phải > 0")
        if systolic_bp <= 0:
            errors.append("Huyết áp tâm thu phải > 0")
        
        if errors:
            st.error("⚠️ Lỗi nhập liệu:")
            for error in errors:
                st.error(f"- {error}")
            return
    
    with col2:
        # Smart Suggestions
        render_suggestions(
            calculator_id="shock_index",
            calculator_name="Shock Index",
            category="Cấp cứu",
            show_related=True,
            show_category=True,
            limit=3
        )
        
        # Educational information
        if CALCULATOR_METADATA_AVAILABLE:
            st.markdown("---")
            render_calculator_education("shock_index")
        elif CALCULATOR_ENHANCEMENTS_AVAILABLE:
            st.markdown("---")
            render_calculator_explanation(
                title="Về Shock Index",
                content="""
                **Shock Index** là chỉ số đơn giản để đánh giá tình trạng huyết động:
                
                **Công thức:**
                Shock Index = Nhịp tim / Huyết áp tâm thu
                
                **Giá trị bình thường:** 0.5-0.7
                
                **Ý nghĩa lâm sàng:**
                - < 0.5: Thấp (có thể do thuốc chẹn beta)
                - 0.5-0.7: Bình thường
                - 0.7-0.9: Tăng nhẹ (theo dõi sát)
                - 0.9-1.2: Tăng (có thể sốc)
                - > 1.2: Tăng rất cao (nguy cơ cao)
                
                **Ưu điểm:**
                - Tính toán nhanh, không cần xét nghiệm
                - Dự đoán tử vong và nhu cầu ICU
                - Dùng hàng ngày trong cấp cứu
                """,
                when_to_use="""
                **Sử dụng khi:**
                - Đánh giá nhanh tình trạng huyết động
                - Nghi ngờ sốc hoặc bất ổn huyết động
                - Theo dõi đáp ứng điều trị
                - Sàng lọc bệnh nhân cần chăm sóc tích cực
                """,
                limitations="""
                **Hạn chế:**
                - Chỉ là công cụ sàng lọc, không thay thế đánh giá lâm sàng
                - Cần kết hợp với các dấu hiệu khác
                - Có thể bị ảnh hưởng bởi thuốc (chẹn beta, thuốc vận mạch)
                """,
                clinical_context="""
                **Bối cảnh lâm sàng:**
                - Shock Index > 0.9: Tăng nguy cơ tử vong
                - Shock Index > 1.0: Nguy cơ tử vong cao, cần hồi sức tích cực
                - Kết hợp với SOFA, qSOFA để đánh giá toàn diện
                """
            )
    
    st.markdown("---")
    
    # Calculate
    if st.button("🔄 Tính Shock Index", type="primary", use_container_width=True):
        result = calculate_shock_index(heart_rate, systolic_bp)
        
        if "error" in result:
            st.error(f"❌ {result['error']}")
            return
        
        # Save to history
        save_calculation_to_history(
            calculator_id="shock_index",
            calculator_name="Shock Index",
            inputs={
                "heart_rate": heart_rate,
                "systolic_bp": systolic_bp
            },
            result=result
        )
        
        # Display result
        st.markdown("### 📊 Kết quả")
        
        # Main result card
        col_result1, col_result2 = st.columns([2, 1])
        
        with col_result1:
            # Shock Index value
            risk_color = {
                "low": COLORS['success'],
                "moderate": "#FFA500",
                "high": COLORS['warning'],
                "critical": COLORS['danger']
            }.get(result['risk_level'], COLORS['info'])
            
            st.markdown(f"""
            <div style="background: white; padding: 20px; border-radius: 8px; border-left: 4px solid {risk_color}; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                <h2 style="color: {risk_color}; margin: 0 0 10px 0;">Shock Index: <strong>{result['shock_index']}</strong></h2>
                <p style="font-size: 1.1em; margin: 5px 0;"><strong>Mức độ:</strong> {result['interpretation']}</p>
                <p style="margin: 5px 0;"><strong>Ý nghĩa lâm sàng:</strong> {result['clinical_meaning']}</p>
                <p style="margin: 5px 0;"><strong>Hành động:</strong> {result['action']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col_result2:
            render_risk_badge(result['risk_level'], result['interpretation'])
        
        # Breakdown
        st.markdown("---")
        st.markdown("### 📋 Chi tiết")
        
        breakdown_data = [
            {"label": "Nhịp tim", "value": f"{result['heart_rate']} bpm"},
            {"label": "Huyết áp tâm thu", "value": f"{result['systolic_bp']} mmHg"},
            {"label": "Shock Index", "value": f"{result['shock_index']}"},
            {"label": "Khoảng bình thường", "value": result['normal_range']},
            {"label": "Nguy cơ tử vong", "value": result['mortality_risk']},
        ]
        
        render_score_breakdown(breakdown_data)
        
        # Clinical interpretation
        st.markdown("---")
        st.markdown("### 💡 Hướng dẫn lâm sàng")
        
        if result['risk_level'] == 'critical':
            st.error(f"""
            **⚠️ Nguy cơ cao:**
            - Shock Index > 1.2 cho thấy tình trạng huyết động rất không ổn định
            - Cần hồi sức ngay lập tức
            - Xem xét chuyển ICU
            - Đánh giá nguyên nhân sốc và điều trị nguyên nhân
            - Theo dõi sát các dấu hiệu sinh tồn
            """)
        elif result['risk_level'] == 'high':
            st.warning(f"""
            **⚠️ Nguy cơ tăng:**
            - Shock Index 0.9-1.2 cho thấy có thể có sốc
            - Cần đánh giá ngay tình trạng huyết động
            - Xem xét hồi sức dịch nếu phù hợp
            - Đánh giá nguyên nhân và điều trị
            - Theo dõi sát, có thể cần ICU
            """)
        elif result['risk_level'] == 'moderate':
            st.info(f"""
            **ℹ️ Theo dõi:**
            - Shock Index 0.7-0.9 cho thấy có thể có bất ổn huyết động nhẹ
            - Theo dõi sát các dấu hiệu sinh tồn
            - Đánh giá thêm nếu có triệu chứng khác
            - Có thể cần điều chỉnh điều trị
            """)
        else:
            st.success(f"""
            **✅ Bình thường:**
            - Shock Index trong khoảng bình thường
            - Tiếp tục theo dõi thường quy
            - Nếu < 0.5, xem xét ảnh hưởng của thuốc chẹn beta
            """)
        
        # Share and Export
        st.markdown("---")
        col_share1, col_share2 = st.columns(2)
        with col_share1:
            render_share_section(
                calculator_id="shock_index",
                calculator_name="Shock Index",
                result=result
            )
        with col_share2:
            render_scores_export(
                calculator_name="Shock Index",
                result=result,
                inputs={
                    "Nhịp tim": f"{heart_rate} bpm",
                    "Huyết áp tâm thu": f"{systolic_bp} mmHg"
                }
            )
    
    # History
    st.markdown("---")
    render_history_ui("shock_index", "Shock Index")
    
    # References
    st.markdown("---")
    references = get_references("shock_index")
    if references:
        render_references_section(references)
