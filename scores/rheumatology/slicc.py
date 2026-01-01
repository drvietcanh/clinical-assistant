"""SLICC Classification Criteria for SLE"""
import streamlit as st
from config.theme import COLORS
from components.ui.scoring import render_score_result
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
# =====================================
def render():
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'slicc':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared.get('calculator_name', 'SLICC Criteria')}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    st.markdown(f"<h3 style='text-align: center; color: {COLORS['success']};'>🦋 SLICC Criteria</h3><p style='text-align: center;'><em>Tiêu chuẩn Lupus ban đỏ hệ thống</em></p>", unsafe_allow_html=True)
    with st.expander("ℹ️ SLICC 2012"): st.markdown("**SLICC 2012** chẩn đoán SLE. Cần **≥4 tiêu chuẩn** (ít nhất 1 lâm sàng + 1 miễn dịch) HOẶC **Lupus nephritis + ANA/anti-dsDNA**")
    st.markdown("---"); st.markdown("### Lâm sàng (Clinical):"); acute_cutaneous = st.checkbox("1. Da cấp (hồng bướm...)"); chronic_cutaneous = st.checkbox("2. Da mạn (lupus disoid...)"); oral_ulcers = st.checkbox("3. Loét miệng"); alopecia = st.checkbox("4. Rụng tóc"); arthritis = st.checkbox("5. Viêm khớp"); serositis = st.checkbox("6. Viêm màng (màng phổi/tim)"); renal = st.checkbox("7. Thận (protein niệu)"); neuro = st.checkbox("8. Thần kinh (co giật, loạn thần)"); hemolytic = st.checkbox("9. Thiếu máu tan máu"); leukopenia = st.checkbox("10. Giảm bạch cầu/lympho"); thrombocytopenia = st.checkbox("11. Giảm tiểu cầu"); clinical_score = sum([acute_cutaneous, chronic_cutaneous, oral_ulcers, alopecia, arthritis, serositis, renal, neuro, hemolytic, leukopenia, thrombocytopenia])
    st.markdown("### Miễn dịch (Immunologic):"); ana = st.checkbox("1. ANA (+)"); anti_dsdna = st.checkbox("2. Anti-dsDNA"); anti_sm = st.checkbox("3. Anti-Sm"); antiphospholipid = st.checkbox("4. Antiphospholipid Ab"); low_complement = st.checkbox("5. Giảm complement (C3, C4, CH50)"); coombs = st.checkbox("6. Coombs test (+)"); immuno_score = sum([ana, anti_dsdna, anti_sm, antiphospholipid, low_complement, coombs]); total = clinical_score + immuno_score
    if st.button("🔬 Đánh giá SLICC", type="primary", use_container_width=True):
        lupus_nephritis_positive = renal and (ana or anti_dsdna)
        if (total >= 4 and clinical_score >= 1 and immuno_score >= 1) or lupus_nephritis_positive: 
            render_score_result(
                title="Kết quả SLICC (SLE)",
                score=f"{total} tiêu chuẩn",
                interpretation=f"**Đáp ứng tiêu chuẩn SLE (SLICC 2012)**\n\n- Lâm sàng: {clinical_score}\n- Miễn dịch: {immuno_score}",
                mortality="DƯƠNG TÍNH",
                color=COLORS['error'],
                icon="🚨"
            )
            st.info("**Điều trị:** Hydroxychloroquine + Glucocorticoid ± Immunosuppressants")
            diagnosis = "SLE Positive"
        else: 
            render_score_result(
                title="Kết quả SLICC (SLE)",
                score=f"{total} tiêu chuẩn",
                interpretation=f"**Chưa đủ tiêu chuẩn SLE**\n\n- Lâm sàng: {clinical_score}\n- Miễn dịch: {immuno_score}\n\nTheo dõi tiếp, cân nhắc bệnh khác",
                mortality="ÂM TÍNH",
                color=COLORS['success'],
                icon="✅"
            )
            diagnosis = "SLE Negative"
        
        # Prepare data for history and share
        inputs_dict = {
            "Acute Cutaneous": "Yes" if acute_cutaneous else "No",
            "Chronic Cutaneous": "Yes" if chronic_cutaneous else "No",
            "Oral Ulcers": "Yes" if oral_ulcers else "No",
            "Alopecia": "Yes" if alopecia else "No",
            "Arthritis": "Yes" if arthritis else "No",
            "Serositis": "Yes" if serositis else "No",
            "Renal": "Yes" if renal else "No",
            "Neuro": "Yes" if neuro else "No",
            "Hemolytic": "Yes" if hemolytic else "No",
            "Leukopenia": "Yes" if leukopenia else "No",
            "Thrombocytopenia": "Yes" if thrombocytopenia else "No",
            "ANA": "Yes" if ana else "No",
            "Anti-dsDNA": "Yes" if anti_dsdna else "No",
            "Anti-Sm": "Yes" if anti_sm else "No",
            "Antiphospholipid": "Yes" if antiphospholipid else "No",
            "Low Complement": "Yes" if low_complement else "No",
            "Coombs": "Yes" if coombs else "No"
        }
        
        results_dict = {
            "Total Criteria": f"{total}",
            "Clinical Score": f"{clinical_score}",
            "Immuno Score": f"{immuno_score}",
            "Diagnosis": diagnosis
        }
        
        # Export section
        from components.export import render_export_section
        render_export_section(
                title="SLICC Criteria",
                inputs=inputs_dict,
                results=results_dict
        ,
                calculator_name="SLICC Criteria"
            )
        
        # Save to history
        save_calculation_to_history(
            calculator_id="slicc",
            calculator_name="SLICC Criteria",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Share section
        render_share_section(
            calculator_id="slicc",
            calculator_name="SLICC Criteria",
            inputs=inputs_dict,
            results=results_dict,
            show_qr=True
        )
        
        # History section
        render_history_ui(calculator_id="slicc", show_actions=True)
    
    # Smart Suggestions
    col_main, col_suggestions = st.columns([2, 1])
    with col_suggestions:
        render_suggestions(
            calculator_id="slicc",
            calculator_name="SLICC Criteria",
            category="Thấp khớp học",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    # References section (always at bottom)
    st.markdown("---")
    references = get_references("SLICC Criteria")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            show_evidence_level=True,
            show_links=True
        )
if __name__ == "__main__": render()

