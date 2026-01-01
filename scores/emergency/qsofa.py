"""
qSOFA (Quick SOFA) Score
Sepsis-3 screening tool
"""

import streamlit as st
from config.theme import COLORS
from scores.utils.validation import (
    validate_gcs,
    validate_blood_pressure,
    validate_respiratory_rate
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


def render():
    """qSOFA (Quick SOFA) Calculator"""
    # st.subheader("🩺 qSOFA (Quick SOFA)")
    st.markdown(f"""
    <h3 style='text-align: center; color: {COLORS['success']};'>🩺 qSOFA (Quick SOFA)</h3>
    """, unsafe_allow_html=True)
    st.caption("Tiêu chuẩn Sepsis-3 để sàng lọc nhiễm trùng huyết")
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'qsofa':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### Thông số bệnh nhân")
        
        rr = st.number_input(
            "Nhịp thở (/phút)",
            min_value=0,
            max_value=60,
            value=20,
            step=1,
            help="Normal: 12-20 /min"
        )
        
        sbp = st.number_input(
            "Huyết áp tâm thu (mmHg)",
            min_value=0,
            max_value=300,
            value=120,
            step=1,
            help="Normal: 90-120 mmHg"
        )
        
        gcs = st.number_input(
            "Glasgow Coma Scale (GCS) - Thang điểm hôn mê Glasgow",
            min_value=3,
            max_value=15,
            value=15,
            step=1,
            help="Normal: 15; Coma: 3"
        )
    
    with col2:
        # Smart Suggestions
        render_suggestions(
            calculator_id="qsofa",
            calculator_name="qSOFA",
            category="Cấp cứu",
            show_related=True,
            show_category=True,
            limit=3
        )
        
        # Educational information - Enhanced with Phase 1 Metadata
        if CALCULATOR_METADATA_AVAILABLE:
            st.markdown("---")
            # Use Phase 1 calculator metadata system
            render_calculator_education("qsofa")
        elif CALCULATOR_ENHANCEMENTS_AVAILABLE:
            st.markdown("---")
            render_calculator_explanation(
                title="Về qSOFA Score",
                content="""
                **qSOFA (Quick SOFA)** là công cụ sàng lọc nhanh cho sepsis:
                
                - Phần của Sepsis-3 definition (2016)
                - Sử dụng 3 tiêu chí lâm sàng đơn giản
                - Không cần xét nghiệm
                - qSOFA ≥2: Nguy cơ tử vong cao, cần đánh giá thêm
                
                **3 tiêu chí:**
                1. Nhịp thở ≥22/min
                2. Huyết áp tâm thu ≤100 mmHg
                3. GCS <15
                
                **Tổng điểm: 0-3**
                """,
                when_to_use="""
                **Sử dụng qSOFA khi:**
                - Bệnh nhân nghi ngờ nhiễm trùng
                - Cần sàng lọc nhanh sepsis
                - Không có sẵn xét nghiệm (SOFA cần xét nghiệm)
                - Sử dụng ở ED, ward, ngoại trú
                """,
                limitations="""
                **Hạn chế:**
                - Chỉ là công cụ sàng lọc, không chẩn đoán
                - qSOFA <2 không loại trừ sepsis
                - Cần kết hợp với đánh giá lâm sàng
                - SOFA score chính xác hơn nhưng cần xét nghiệm
                """,
                clinical_context="""
                **Bối cảnh lâm sàng:**
                - **qSOFA ≥2:** Nguy cơ tử vong cao, cần đánh giá SOFA đầy đủ
                - Nếu qSOFA ≥2 + nhiễm trùng → Sepsis (Sepsis-3)
                - qSOFA <2 nhưng nghi ngờ cao → Vẫn cần đánh giá thêm
                - qSOFA không thay thế SOFA trong ICU
                """
            )
            
            # Evidence citation
            render_evidence_citation(
                citation_text="Singer M, et al. The Third International Consensus Definitions for Sepsis and Septic Shock (Sepsis-3). JAMA. 2016;315(8):801-10.",
                doi="10.1001/jama.2016.0287",
                pmid="26903338"
            )
        
        if st.button("🔢 Tính qSOFA", type="primary", use_container_width=True):
            # Validate inputs
            validation_errors = []
            
            is_valid_rr, rr_error = validate_respiratory_rate(rr)
            if not is_valid_rr:
                validation_errors.append(rr_error)
            
            is_valid_sbp, sbp_error = validate_blood_pressure(sbp)
            if not is_valid_sbp:
                validation_errors.append(sbp_error)
            
            is_valid_gcs, gcs_error = validate_gcs(gcs)
            if not is_valid_gcs:
                validation_errors.append(gcs_error)
            
            if validation_errors:
                st.error("**⚠️ Lỗi validation:**")
                for error in validation_errors:
                    st.error(f"- {error}")
                st.stop()
            
            score = 0
            details = []
            
            if rr >= 22:
                score += 1
                details.append("✓ Respiratory rate ≥22 /min (+1)")
            else:
                details.append("✗ Respiratory rate <22 /min (0)")
            
            if sbp <= 100:
                score += 1
                details.append("✓ Systolic BP ≤100 mmHg (+1)")
            else:
                details.append("✗ Systolic BP >100 mmHg (0)")
            
            if gcs < 15:
                score += 1
                details.append("✓ Altered mentation (GCS <15) (+1)")
            else:
                details.append("✗ GCS = 15 (0)")
            
            # Determine risk level and color
            if score >= 2:
                risk_level_code = "very_high"  # For color coding component
                risk_level = "CONCERNING FOR SEPSIS"
                color = COLORS["error"]
                icon = "⚠️"
                interpretation = """
                **Action Required:**
                - Assess for infection source
                - Consider blood cultures
                - Start antibiotics if indicated
                - Monitor closely
                - Calculate full SOFA score
                """
            elif score == 1:
                risk_level_code = "moderate"  # For color coding component
                risk_level = "Intermediate Risk"
                color = COLORS["warning"]
                icon = "⚡"
                interpretation = """
                **Consider:**
                - Close monitoring
                - Reassess frequently
                - Look for other sepsis signs
                """
            else:
                risk_level_code = "low"  # For color coding component
                risk_level = "Low Risk"
                color = COLORS["success"]
                icon = "✅"
                interpretation = """
                **Interpretation:**
                - Low probability of sepsis
                - Routine monitoring
                - Reassess if clinical change
                """
            
            with col2:
                st.markdown("### Kết quả")
                
                # Modern Result Card for qSOFA
                color_hex = color
                
                bg_color = {
                    COLORS["error"]: COLORS["error_light"],
                    COLORS["warning"]: COLORS["warning_light"],
                    COLORS["success"]: COLORS["success_light"]
                }.get(color, COLORS["info_light"])
                
                # Risk Level Label for VN
                risk_vn = "Nguy cơ Cao (Sepsis)" if score >= 2 else ("Nguy cơ Trung bình" if score == 1 else "Nguy cơ Thấp")

                st.markdown(f"""
                <div style="background: {bg_color}; border-radius: 12px; padding: 24px; border: 1px solid {color_hex}; text-align: center; margin-bottom: 24px;">
                    <h3 style="color: {color_hex}; margin: 0 0 8px 0; font-size: 1.1em; text-transform: uppercase; letter-spacing: 0.5px;">qSOFA Score</h3>
                    <div style="font-size: 4em; font-weight: 700; color: {color_hex}; line-height: 1;">
                        {score}<span style="font-size: 0.5em; color: {color_hex}; opacity: 0.8;">/3</span>
                    </div>
                    <div style="background: {color_hex}; color: white; display: inline-block; padding: 6px 16px; border-radius: 20px; font-weight: 600; margin-top: 12px;">
                        {risk_vn}
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                # Clinical Action Card
                st.markdown(f"""
                <div style="background: white; border-radius: 8px; padding: 16px; border-left: 4px solid {color_hex}; box-shadow: 0 1px 2px rgba(0,0,0,0.05); margin-bottom: 16px;">
                    <strong style="display: block; margin-bottom: 8px; color: #495057;">Khuyến nghị lâm sàng:</strong>
                    <div style="color: #212529; white-space: pre-line; line-height: 1.5;">{risk_level}</div>
                </div>
                """, unsafe_allow_html=True)
                
                # Interpretation detail
                if not CALCULATOR_METADATA_AVAILABLE:
                    st.info(interpretation.replace("**Interpretation:**", "**Giải thích:**").replace("**Action Required:**", "**Cần làm gì:**").replace("**Consider:**", "**Cân nhắc:**"))
                else:
                    render_calculator_result_with_interpretation(
                        calculator_id="qsofa",
                        result=f"qSOFA Score: {score}/3",
                        result_value=float(score)
                    )
            
            # Build breakdown of criteria
            criteria_scores = {}
            if rr >= 22:
                criteria_scores["Nhịp thở ≥22"] = 1
            if sbp <= 100:
                criteria_scores["HA tâm thu ≤100"] = 1
            if gcs < 15:
                criteria_scores["GCS <15"] = 1
            
            if criteria_scores:
                render_score_breakdown(
                    title="Tiêu chí qSOFA",
                    subscores=criteria_scores,
                    total_score=score
                )
            
            # Visual Charts
            st.markdown("---")
            st.markdown("### 📊 Biểu Đồ Nguy Cơ")
            col_chart1, col_chart2 = st.columns(2)
            
            with col_chart1:
                render_risk_gauge_chart(
                    value=score,
                    min_value=0,
                    max_value=3,
                    thresholds={
                        'Low': 0,
                        'Moderate': 1,
                        'High': 2
                    },
                    title="qSOFA Score"
                )
            
            with col_chart2:
                render_risk_bar_chart(
                    value=score,
                    thresholds={
                        'Low': 0,
                        'Moderate': 1,
                        'High': 2
                    },
                    max_value=3,
                    title="Risk Level",
                    show_value=True
                )
            
            st.markdown("---")
            st.markdown("### Chi tiết")
            for detail in details:
                st.write(detail)
            
            # Prepare inputs and results for export/history
            inputs_dict = {
                "Respiratory Rate": f"{rr} /min",
                "Systolic BP": f"{sbp} mmHg",
                "GCS": str(gcs)
            }
            
            results_dict = {
                "qSOFA Score": f"{score}/3",
                "Risk Level": risk_level,
                "Details": "\n".join(details) if details else "Không có tiêu chí nào"
            }
            
            # Export section (new component)
            render_scores_export(
                calculator_name="qSOFA",
                inputs=inputs_dict,
                results=results_dict,
                specialty="Cấp cứu & Hồi sức"
            )
            
            # Keep old export for compatibility
            st.markdown("---")
            from components.export import render_export_section
            render_export_section(
                title=f"qSOFA = {score}/3",
                inputs=inputs_dict,
                results=results_dict,
                calculator_name="qSOFA",
                filename="qsofa_result"
            )
            
            # Save to history
            save_calculation_to_history(
                calculator_id="qsofa",
                calculator_name="qSOFA",
                inputs=inputs_dict,
                results=results_dict
            )
            
            # Share section
            render_share_section(
                calculator_id="qsofa",
                calculator_name="qSOFA",
                inputs=inputs_dict,
                results=results_dict,
                show_qr=True
            )
            
            # History section
            st.markdown("---")
            render_history_ui(calculator_id="qsofa", show_actions=True)
            
            # References section
            references = get_references("qSOFA")
            if references:
                render_references_section(
                    references=references,
                    title="📚 Tài liệu tham khảo",
                    last_updated="2024-01-15",
                    show_evidence_level=True,
                    show_links=True
                )
    
    # Always show references at the bottom
    references = get_references("qSOFA")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-01-15",
            show_evidence_level=True,
            show_links=True
        )
    
    st.markdown("---")
    st.info("""
    **Next Steps:**
    - If qSOFA ≥2 → Calculate full **SOFA score**
    - Consider **Sepsis Bundle** protocol
    - Review **Antibiotic** selection
    """)

