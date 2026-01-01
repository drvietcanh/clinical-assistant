"""SCORAD - SCORing Atopic Dermatitis"""
import streamlit as st
from config.theme import COLORS
# import streamlit.components.v1 as components
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
from components.ui.scoring import render_score_result
# =====================================
from scores.utils.validation import (
    validate_range
)
from components.ui.validation import render_validation_errors

def render():
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'scorad':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared.get('calculator_name', 'SCORAD')}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    st.markdown(f"<h3 style='text-align: center; color: {COLORS['success']};'>🩹 SCORAD</h3><p style='text-align: center;'><em>Điểm viêm da cơ địa</em></p>", unsafe_allow_html=True)
    with st.expander("ℹ️ SCORAD"): st.markdown("**SCORAD** đánh giá mức độ viêm da cơ địa. **Điểm:** 0-103")
    st.markdown("---"); extent = st.slider("A. % Diện tích bị ảnh hưởng (Rule of 9s)", 0, 100, 10); erythema = st.slider("B1. Đỏ", 0, 3, 0); edema = st.slider("B2. Phù/Sần", 0, 3, 0); oozing = st.slider("B3. Chảy nước/Vảy", 0, 3, 0); excoriation = st.slider("B4. Trầy xước", 0, 3, 0); lichenification = st.slider("B5. Dày da", 0, 3, 0); dryness = st.slider("B6. Khô da", 0, 3, 0); intensity = erythema + edema + oozing + excoriation + lichenification + dryness; itch = st.slider("C1. Ngứa (0-10)", 0, 10, 0); sleep_loss = st.slider("C2. Mất ngủ (0-10)", 0, 10, 0); subjective = itch + sleep_loss; total = extent/5 * 0.7 + intensity * 7/2 + subjective
    if st.button("🔬 Tính SCORAD", type="primary", use_container_width=True):
        # Validate inputs
        validation_errors = []
        
        # Extent validation (0-100%)
        is_valid_extent, extent_error = validate_range(extent, 0, 100, "Diện tích bị ảnh hưởng")
        if not is_valid_extent:
            validation_errors.append(f"Diện tích: {extent_error}")
        
        # Intensity scores validation (0-3)
        intensity_scores = [erythema, edema, oozing, excoriation, lichenification, dryness]
        score_names = ["Đỏ", "Phù/Sần", "Chảy nước/Vảy", "Trầy xước", "Dày da", "Khô da"]
        for score, name in zip(intensity_scores, score_names):
            is_valid_score, score_error = validate_range(score, 0, 3, name)
            if not is_valid_score:
                validation_errors.append(f"{name}: {score_error}")
        
        # Itch validation (0-10)
        is_valid_itch, itch_error = validate_range(itch, 0, 10, "Ngứa")
        if not is_valid_itch:
            validation_errors.append(f"Ngứa: {itch_error}")
        
        # Sleep loss validation (0-10)
        is_valid_sleep, sleep_error = validate_range(sleep_loss, 0, 10, "Mất ngủ")
        if not is_valid_sleep:
            validation_errors.append(f"Mất ngủ: {sleep_error}")
        
        if validation_errors:
            render_validation_errors(validation_errors)
            return
        
        if total < 25: severity = "Nhẹ"; color = COLORS["success"]; icon = "🟢"
        elif total < 50: severity = "Trung bình"; color = COLORS["warning"]; icon = "🟠"
        else: severity = "Nặng"; color = COLORS["error"]; icon = "🔴"
        
        st.markdown("---")
        render_score_result(
            title="SCORAD Score",
            score=f"{total:.1f}/103",
            interpretation=severity,
            mortality="",
            color=color,
            icon=icon,
            size="large"
        )
        
        # Prepare data for history and share
        inputs_dict = {
            "Extent": f"{extent}%",
            "Erythema": erythema, "Edema": edema, "Oozing": oozing,
            "Excoriation": excoriation, "Lichenification": lichenification, "Dryness": dryness,
            "Itch": itch, "Sleep Loss": sleep_loss
        }
        
        results_dict = {
            "SCORAD Score": f"{total:.1f}/103",
            "Severity": severity
        }
        
        # Export section
        from components.export import render_export_section
        render_export_section(
                title="SCORAD",
                inputs=inputs_dict,
                results=results_dict
        ,
                calculator_name="SCORAD"
            )
        
        # Save to history
        save_calculation_to_history(
            calculator_id="scorad",
            calculator_name="SCORAD",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Share section
        render_share_section(
            calculator_id="scorad",
            calculator_name="SCORAD",
            inputs=inputs_dict,
            results=results_dict,
            show_qr=True
        )
        
        # History section
        render_history_ui(calculator_id="scorad", show_actions=True)
    
    # Smart Suggestions
    col_main, col_suggestions = st.columns([2, 1])
    with col_suggestions:
        render_suggestions(
            calculator_id="scorad",
            calculator_name="SCORAD",
            category="Da liễu",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    # References section (always at bottom)
    st.markdown("---")
    references = get_references("SCORAD")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            show_evidence_level=True,
            show_links=True
        )
if __name__ == "__main__": render()

