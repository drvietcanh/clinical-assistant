"""
qSOFA (Quick SOFA) Score
Sepsis-3 screening tool
"""

import streamlit as st
from scores.references_config import get_references
from components.references import render_references_section
from scores.utils.validation import (
    validate_gcs,
    validate_blood_pressure,
    validate_respiratory_rate
)
from components.ui.scoring import render_score_result, render_score_breakdown
from components.calculation_history import save_calculation_to_history
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions


def render():
    """qSOFA (Quick SOFA) Calculator"""
    st.subheader("🩺 qSOFA (Quick SOFA)")
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
            category="Cấp Cứu",
            show_related=True,
            show_category=True,
            limit=3
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
                risk_level = "CONCERNING FOR SEPSIS"
                color = "#dc3545"  # red
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
                risk_level = "Intermediate Risk"
                color = "#fd7e14"  # orange
                icon = "⚡"
                interpretation = """
                **Consider:**
                - Close monitoring
                - Reassess frequently
                - Look for other sepsis signs
                """
            else:
                risk_level = "Low Risk"
                color = "#28a745"  # green
                icon = "✅"
                interpretation = """
                **Interpretation:**
                - Low probability of sepsis
                - Routine monitoring
                - Reassess if clinical change
                """
            
            with col2:
                st.markdown("### Kết quả")
                
                # Use render_score_result for main score display
                render_score_result(
                    title="qSOFA Score",
                    score=score,
                    interpretation=risk_level,
                    mortality=None,
                    color=color,
                    icon=icon,
                    size="large"
                )
                
                st.markdown(interpretation)
            
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
                    title="Tiêu Chí qSOFA",
                    subscores=criteria_scores,
                    total_score=score
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
            
            # Export section
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
            from components.calculation_history import render_history_ui
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

