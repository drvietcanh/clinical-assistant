"""
Thang điểm hôn mê Glasgow (GCS)
Consciousness level assessment
"""

import streamlit as st
from config.theme import COLORS
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
from components.export import render_export_section
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

from scores.utils.validation import validate_gcs as validate_gcs_score
from components.ui.scoring import render_score_result, render_score_breakdown


def render():
    """Thang điểm hôn mê Glasgow Calculator"""
    st.markdown(f"<h2 style='text-align: center; color: {COLORS['success']};'>🧠 Thang điểm hôn mê Glasgow (GCS)</h2>", unsafe_allow_html=True)
    st.caption("<p style='text-align: center;'>Đánh giá Mức độ ý thức</p>", unsafe_allow_html=True)
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'gcs':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📋 Thang đánh giá")
        
        # Eye Opening (E)
        st.markdown("#### 👁️ Mở mắt (Eye Opening)")
        eye_options = {
            "Spontaneous (Tự nhiên)": 4,
            "To speech (Khi gọi)": 3,
            "To pain (Khi đau)": 2,
            "None (Không mở)": 1
        }
        eye_response = st.radio(
            "Phản ứng mở mắt:",
            list(eye_options.keys()),
            key="gcs_eye"
        )
        eye_score = eye_options[eye_response]
        
        # Verbal Response (V)
        st.markdown("#### 🗣️ Phản ứng lời nói (Verbal Response)")
        verbal_options = {
            "Oriented (Tỉnh táo, định hướng đúng)": 5,
            "Confused (Lẫn lộn)": 4,
            "Inappropriate words (Nói lung tung)": 3,
            "Incomprehensible sounds (Rên rỉ)": 2,
            "None (Không nói)": 1
        }
        verbal_response = st.radio(
            "Phản ứng lời nói:",
            list(verbal_options.keys()),
            key="gcs_verbal"
        )
        verbal_score = verbal_options[verbal_response]
        
        # Motor Response (M)
        st.markdown("#### 💪 Phản ứng vận động (Motor Response)")
        motor_options = {
            "Obeys commands (Làm theo lệnh)": 6,
            "Localizes pain (Định vị đau)": 5,
            "Withdraws from pain (Rút tay khi đau)": 4,
            "Flexion to pain (Cử động bất thường)": 3,
            "Extension to pain (Duỗi cứng)": 2,
            "None (Không cử động)": 1
        }
        motor_response = st.radio(
            "Phản ứng vận động:",
            list(motor_options.keys()),
            key="gcs_motor"
        )
        motor_score = motor_options[motor_response]
    
    with col2:
        # Smart Suggestions
        render_suggestions(
            calculator_id="gcs",
            calculator_name="GCS Score",
            category="Thần kinh",
            show_related=True,
            show_category=True,
            limit=3
        )
        
        # Educational information - Enhanced with Phase 1 Metadata
        if CALCULATOR_METADATA_AVAILABLE:
            st.markdown("---")
            render_calculator_education("gcs")
        elif CALCULATOR_ENHANCEMENTS_AVAILABLE:
            st.markdown("---")
            render_calculator_explanation(
                title="Về GCS Score",
                content="Glasgow Coma Scale đánh giá mức độ ý thức...",
                when_to_use="Sử dụng khi...",
                limitations="Hạn chế...",
                clinical_context="Bối cảnh lâm sàng..."
        )
    
    if st.button("🧮 Tính GCS", type="primary"):
            # Validate GCS components (total should be 3-15)
            total_score = eye_score + verbal_score + motor_score
            
            # Validation is implicit since we use radio buttons with fixed values
            # But we can add a check for safety
            if total_score < 3 or total_score > 15:
                st.error("**⚠️ Lỗi: GCS phải từ 3-15**")
                st.stop()
            
            # Determine severity and color
            if total_score >= 14:
                severity = "Chấn thương sọ não nhẹ (Mild TBI)"
                risk_level_code = "low"
                color = COLORS["success"]
                icon = "✅"
            elif total_score >= 9:
                severity = "Chấn thương sọ não trung bình (Moderate TBI)"
                risk_level_code = "moderate"
                color = COLORS["warning"]
                icon = "⚠️"
            else:
                severity = "Chấn thương sọ não nặng (Severe TBI)"
                risk_level_code = "very_high"
                color = COLORS["error"]
                icon = "🚨"
            
            with col2:
                st.markdown("### 📊 Kết quả")
                
                # Display score with color coding badge
                st.markdown(f"## GCS Score = {total_score}/15")
                render_risk_badge(
                    risk_level=risk_level_code,
                    label=severity,
                    value=total_score
                )
                
                # Use render_score_result for main score display
                render_score_result(
                    title="GCS Score",
                    score=total_score,
                    interpretation=severity,
                    mortality=None,
                    color=color,
                    icon=icon,
                    size="large"
                )
                
                # Enhanced result interpretation with Phase 1 metadata
                if CALCULATOR_METADATA_AVAILABLE:
                    render_calculator_result_with_interpretation(
                        calculator_id="gcs",
                        result=f"GCS Score: {total_score}/15",
                        result_value=float(total_score)
                )
            
            # Use render_score_breakdown for component scores
            render_score_breakdown(
                title="Điểm Từng Thành phần",
                subscores={
                    "👁️ Mở mắt (E)": eye_score,
                    "🗣️ Lời nói (V)": verbal_score,
                    "💪 Vận động (M)": motor_score
                },
                total_score=total_score
            )
            
            # Visual Charts
            st.markdown("---")
            st.markdown("### 📊 Biểu Đồ Nguy Cơ")
            col_chart1, col_chart2 = st.columns(2)
            
            with col_chart1:
                render_risk_gauge_chart(
                    value=total_score,
                    min_value=3,
                    max_value=15,
                    thresholds={
                        'Severe': 8,
                        'Moderate': 13,
                        'Mild': 14
                    },
                    title="GCS Score"
                )
            
            with col_chart2:
                render_risk_bar_chart(
                    value=total_score,
                    thresholds={
                        'Severe': 8,
                        'Moderate': 13,
                        'Mild': 14
                    },
                    max_value=15,
                    title="Severity Level",
                    show_value=True
                )
            
            st.markdown("---")
            st.markdown(f"**Chi tiết:** E{eye_score} V{verbal_score} M{motor_score}")
            st.markdown(f"- Mở mắt: {eye_response}")
            st.markdown(f"- Phản ứng lời nói: {verbal_response}")
            st.markdown(f"- Phản ứng vận động: {motor_response}")
            
            st.markdown("---")
            st.markdown("### 💊 Ý nghĩa lâm sàng")
            
            # Enhanced interpretation with Phase 1
            if CALCULATOR_ENHANCEMENTS_AVAILABLE:
                recommendations = []
                if total_score >= 14:
                    recommendations.append("Theo dõi lâm sàng")
                    recommendations.append("CT scan nếu có triệu chứng")
                    recommendations.append("Thường hồi phục tốt")
                elif total_score >= 9:
                    recommendations.append("Nhập viện theo dõi")
                    recommendations.append("CT scan sọ não")
                    recommendations.append("Theo dõi sát các dấu hiệu tăng áp lực nội sọ")
                    recommendations.append("Có thể cần can thiệp")
                else:
                    recommendations.append("**ĐẶT NỘI KHÍ QUẢN NGAY** (GCS ≤8)")
                    recommendations.append("Nhập ICU")
                    recommendations.append("CT scan khẩn cấp")
                    recommendations.append("Theo dõi áp lực nội sọ")
                    recommendations.append("Có thể cần phẫu thuật")
                
                render_result_interpretation(
                    result=f"{total_score}/15",
                    interpretation=severity,
                    recommendations=recommendations,
                    risk_level=risk_level_code.replace("_", "") if risk_level_code else None
                )
            else:
                # Fallback to original
                if total_score >= 14:
                    st.success("""
                    **GCS 14-15: Chấn thương sọ não nhẹ**
                    - Theo dõi lâm sàng
                    - CT scan nếu có triệu chứng
                    - Thường hồi phục tốt
                    """)
                elif total_score >= 9:
                    st.warning("""
                    **GCS 9-13: Chấn thương sọ não trung bình**
                    - Nhập viện theo dõi
                    - CT scan sọ não
                    - Theo dõi sát các dấu hiệu tăng áp lực nội sọ
                    - Có thể cần can thiệp
                    """)
                else:
                    st.error("""
                    **GCS ≤8: Chấn thương sọ não nặng**
                    - **ĐẶT NỘI KHÍ QUẢN NGAY** (GCS ≤8)
                    - Nhập ICU
                    - CT scan khẩn cấp
                    - Theo dõi áp lực nội sọ
                    - Có thể cần phẫu thuật
                    - Tiên lượng xấu
                    """)
            
            # Additional warnings
            if total_score <= 8:
                st.error("""
                **⚠️ QUAN TRỌNG:**
                - GCS ≤8 = Mất khả năng bảo vệ đường thở
                - Chỉ định đặt nội khí quản
                - Nguy cơ hít sặc cao
                """)
            
            with st.expander("📚 Tài liệu tham khảo"):
                st.markdown("""
                **Thang điểm hôn mê Glasgow (GCS)**
                
                **Thang điểm (3-15):**
                
                **Mở mắt (Eye Opening) (1-4):**
                - 4: Tự nhiên (Spontaneous)
                - 3: Khi gọi (To speech)
                - 2: Khi đau (To pain)
                - 1: Không mở (None)
                
                **Phản ứng lời nói (Verbal Response) (1-5):**
                - 5: Tỉnh táo, định hướng đúng (Oriented)
                - 4: Lẫn lộn (Confused)
                - 3: Nói lung tung (Inappropriate words)
                - 2: Rên rỉ (Incomprehensible sounds)
                - 1: Không nói (None)
                
                **Phản ứng vận động (Motor Response) (1-6):**
                - 6: Làm theo lệnh (Obeys commands)
                - 5: Định vị đau (Localizes pain)
                - 4: Rút tay khi đau (Withdraws from pain)
                - 3: Gấp cứng khi đau (decorticate) (Flexion to pain)
                - 2: Duỗi cứng khi đau (decerebrate) (Extension to pain)
                - 1: Không cử động (None)
                
                **Phân loại chấn thương sọ não:**
                - GCS 14-15: Chấn thương sọ não nhẹ (Mild TBI)
                - GCS 9-13: Chấn thương sọ não trung bình (Moderate TBI)
                - GCS 3-8: Chấn thương sọ não nặng (Severe TBI)
                
                **Chỉ định đặt nội khí quản:**
                - GCS ≤8 (mất khả năng bảo vệ đường thở)
                
                **Xác nhận giá trị:**
                - Được xác nhận rộng rãi trong chấn thương, phẫu thuật thần kinh, hồi sức cấp cứu
                - Tiêu chuẩn vàng để đánh giá mức độ ý thức
                """)
            
            # Prepare data for history and share
            inputs_dict = {
                "Eye Opening": eye_response,
                "Verbal Response": verbal_response,
                "Motor Response": motor_response,
                "Eye Score": eye_score,
                "Verbal Score": verbal_score,
                "Motor Score": motor_score
            }
            
            results_dict = {
                "GCS Total": f"{total_score}/15",
                "Severity": severity,
                "Risk Level": risk_level_code,
                "Details": f"E{eye_score} V{verbal_score} M{motor_score}",
                "Eye Score": eye_score,
                "Verbal Score": verbal_score,
                "Motor Score": motor_score
            }
            
            # Export section (new component)
            st.markdown("---")
            render_scores_export(
                calculator_name="GCS Score",
                inputs=inputs_dict,
                results=results_dict,
                specialty="Thần kinh"
            )
            
            # Keep old export for compatibility
            st.markdown("---")
            render_export_section(
                title="GCS Score",
                inputs=inputs_dict,
                results=results_dict,
                calculator_name="GCS Score"
            )
            
            # Save to history
            save_calculation_to_history(
                calculator_id="gcs",
                calculator_name="GCS Score",
                inputs=inputs_dict,
                results=results_dict
            )
            
            # Share section
            render_share_section(
                calculator_id="gcs",
                calculator_name="GCS Score",
                inputs=inputs_dict,
                results=results_dict,
                show_qr=True
            )
            
            # History section
            st.markdown("---")
            render_history_ui(calculator_id="gcs", show_actions=True)
    
    # References section
    references = get_references("GCS")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-01-15",
            show_evidence_level=True,
            show_links=True
        )

