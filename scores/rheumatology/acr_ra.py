"""ACR/EULAR RA Classification Criteria 2010"""
import streamlit as st
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
    if shared and shared.get('calculator_id') == 'acr_ra':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared.get('calculator_name', 'ACR/EULAR RA Classification')}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    st.markdown("<h2 style='text-align: center; color: #F97316;'>🦴 ACR/EULAR RA Classification</h2><p style='text-align: center;'><em>Tiêu chuẩn phân loại viêm khớp dạng thấp</em></p>", unsafe_allow_html=True)
    with st.expander("ℹ️ ACR/EULAR 2010"): st.markdown("Tiêu chuẩn chẩn đoán RA. Cần **≥6 điểm** để chẩn đoán RA.")
    st.markdown("---"); joint = st.radio("A. Số khớp/vị trí", [0,1,2,3,5], format_func=lambda x: ["0đ: Không", "1đ: 1 khớp lớn", "2đ: 2-10 khớp lớn", "3đ: 1-3 khớp nhỏ", "5đ: 4-10 khớp nhỏ hoặc >10 khớp"][x]); serology = st.radio("B. Huyết thanh học", [0,2,3], format_func=lambda x: ["0đ: RF(-) và ACPA(-)", "2đ: RF thấp hoặc ACPA thấp", "3đ: RF cao hoặc ACPA cao"][x]); duration = st.radio("C. Thời gian triệu chứng", [0,1], format_func=lambda x: ["0đ: < 6 tuần", "1đ: ≥ 6 tuần"][x]); acute_phase = st.radio("D. Protein giai đoạn cấp", [0,1], format_func=lambda x: ["0đ: CRP và ESR bình thường", "1đ: CRP hoặc ESR tăng"][x]); total = joint + serology + duration + acute_phase
    if st.button("🔬 Đánh giá ACR/EULAR", type="primary", use_container_width=True):
        if total >= 6: 
            st.error(f"🚨 **{total}/10 điểm - Đáp ứng tiêu chuẩn RA**\n\nCó thể chẩn đoán viêm khớp dạng thấp"); 
            st.info("**Điều trị:** DMARDs sớm (Methotrexate), theo dõi hoạt động bệnh (DAS28/CDAI/SDAI)")
            diagnosis = "RA Positive"
        else: 
            st.success(f"✅ **{total}/10 điểm - Chưa đủ tiêu chuẩn RA**\n\nTheo dõi tiếp, có thể là viêm khớp khác hoặc RA giai đoạn sớm")
            diagnosis = "RA Negative"
        
        # Prepare data for history and share
        inputs_dict = {
            "Joint Involvement": joint,
            "Serology": serology,
            "Duration": duration,
            "Acute Phase": acute_phase
        }
        
        results_dict = {
            "ACR/EULAR Score": f"{total}/10",
            "Diagnosis": diagnosis
        }
        
        # Export section
        from components.export import render_export_section
        render_export_section(
            calculator_id="acr_ra",
            calculator_name="ACR/EULAR RA Classification",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Save to history
        save_calculation_to_history(
            calculator_id="acr_ra",
            calculator_name="ACR/EULAR RA Classification",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Share section
        render_share_section(
            calculator_id="acr_ra",
            calculator_name="ACR/EULAR RA Classification",
            inputs=inputs_dict,
            results=results_dict,
            show_qr=True
        )
        
        # History section
        render_history_ui(calculator_id="acr_ra", show_actions=True)
    
    # Smart Suggestions
    col_main, col_suggestions = st.columns([2, 1])
    with col_suggestions:
        render_suggestions(
            calculator_id="acr_ra",
            calculator_name="ACR/EULAR RA Classification",
            category="Thấp khớp học",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    # References section (always at bottom)
    st.markdown("---")
    references = get_references("ACR/EULAR RA Classification")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            show_evidence_level=True,
            show_links=True
        )
if __name__ == "__main__": render()

