"""CDAI - Clinical Disease Activity Index for RA"""
import streamlit as st
import streamlit.components.v1 as components
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
# =====================================
from scores.utils.validation import (
    validate_range
)
from config.theme import COLORS
from components.ui.scoring import render_score_result

def render():
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'cdai':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared.get('calculator_name', 'CDAI')}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    st.markdown(f"<h3 style='text-align: center; color: {COLORS['success']};'>🦴 CDAI</h3><p style='text-align: center;'><em>Chỉ số hoạt động lâm sàng RA</em></p>", unsafe_allow_html=True)
    with st.expander("ℹ️ CDAI"): st.markdown("**CDAI** = TJC + SJC + PGA + EGA. Không cần xét nghiệm, tính nhanh.")
    st.markdown("---"); tjc = st.number_input("TJC - Số khớp đau (0-28)", 0, 28, 0, format="%d"); sjc = st.number_input("SJC - Số khớp sưng (0-28)", 0, 28, 0, format="%d"); pga = st.slider("PGA - Bệnh nhân đánh giá (cm, 0-10)", 0.0, 10.0, 5.0, 0.1); ega = st.slider("EGA - Bác sĩ đánh giá (cm, 0-10)", 0.0, 10.0, 5.0, 0.1); cdai = tjc + sjc + pga + ega
    if st.button("🔬 Tính CDAI", type="primary", use_container_width=True):
        # Validate inputs
        validation_errors = []
        
        # TJC validation (0-28)
        is_valid_tjc, tjc_error = validate_range(tjc, 0, 28, "TJC (Số khớp đau)")
        if not is_valid_tjc:
            validation_errors.append(f"TJC: {tjc_error}")
        
        # SJC validation (0-28)
        is_valid_sjc, sjc_error = validate_range(sjc, 0, 28, "SJC (Số khớp sưng)")
        if not is_valid_sjc:
            validation_errors.append(f"SJC: {sjc_error}")
        
        # PGA validation (0-10)
        is_valid_pga, pga_error = validate_range(pga, 0.0, 10.0, "PGA (Bệnh nhân đánh giá)")
        if not is_valid_pga:
            validation_errors.append(f"PGA: {pga_error}")
        
        # EGA validation (0-10)
        is_valid_ega, ega_error = validate_range(ega, 0.0, 10.0, "EGA (Bác sĩ đánh giá)")
        if not is_valid_ega:
            validation_errors.append(f"EGA: {ega_error}")
        
        
        if cdai <= 2.8: status = "Thuyên giảm"; color = COLORS["success"]; icon = "✅"
        elif cdai <= 10: status = "Hoạt động thấp"; color = COLORS["success"]; icon = "🟢"
        elif cdai <= 22: status = "Hoạt động trung bình"; color = COLORS["warning"]; icon = "⚠️"
        else: status = "Hoạt động cao"; color = COLORS["error"]; icon = "🚨"
        
        render_score_result(
            title="CDAI Score",
            score=f"{cdai:.1f}",
            interpretation=status,
            color=color,
            icon=icon
        )
        
        # Prepare data for history and share
        inputs_dict = {
            "TJC": tjc,
            "SJC": sjc,
            "PGA": f"{pga:.1f}",
            "EGA": f"{ega:.1f}"
        }
        
        results_dict = {
            "CDAI": f"{cdai:.1f}",
            "Status": status
        }
        
        # Export section
        from components.export import render_export_section
        render_export_section(
                title="CDAI",
                inputs=inputs_dict,
                results=results_dict
        ,
                calculator_name="CDAI"
            )
        
        # Save to history
        save_calculation_to_history(
            calculator_id="cdai",
            calculator_name="CDAI",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Share section
        render_share_section(
            calculator_id="cdai",
            calculator_name="CDAI",
            inputs=inputs_dict,
            results=results_dict,
            show_qr=True
        )
        
        # History section
        render_history_ui(calculator_id="cdai", show_actions=True)
    
    # Smart Suggestions
    col_main, col_suggestions = st.columns([2, 1])
    with col_suggestions:
        render_suggestions(
            calculator_id="cdai",
            calculator_name="CDAI",
            category="Thấp khớp học",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    # References section (always at bottom)
    st.markdown("---")
    references = get_references("CDAI")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            show_evidence_level=True,
            show_links=True
        )
if __name__ == "__main__": render()

