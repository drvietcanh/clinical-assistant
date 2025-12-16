"""ACR/EULAR Gout Classification Criteria"""
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
    if shared and shared.get('calculator_id') == 'gout':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared.get('calculator_name', 'Gout Classification')}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    st.markdown("<h2 style='text-align: center; color: #F97316;'>🦴 ACR/EULAR Gout Classification</h2><p style='text-align: center;'><em>Tiêu chuẩn chẩn đoán Gout</em></p>", unsafe_allow_html=True)
    with st.expander("ℹ️ Gout Classification"): 
        st.markdown("**ACR/EULAR 2015** chẩn đoán gout. **Chuẩn vàng:** Thấy tinh thể urat trong dịch khớp. Nếu không có → Dùng điểm số ≥8 để chẩn đoán.")
    
    st.markdown("---")
    crystal = st.radio("Có tinh thể urat trong dịch khớp/tophi?", ["Có", "Không", "Không làm"])
    
    if crystal == "Có": 
        st.success("✅ **Chẩn đoán xác định GOUT**\n\nThấy tinh thể urat → Chuẩn vàng chẩn đoán")
        st.info("**Điều trị:** NSAID/Colchicine (cấp) + Allopurinol/Febuxostat (dự phòng)")
        
        # Prepare data for history and share
        inputs_dict = {
            "Crystal": "Có"
        }
        results_dict = {
            "Diagnosis": "Gout (xác định bằng tinh thể urat)",
            "Treatment": "NSAID/Colchicine (cấp) + Allopurinol/Febuxostat (dự phòng)"
        }
        
        # Export section
        from components.export import render_export_section
        render_export_section(
            calculator_id="gout",
            calculator_name="Gout Classification",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Save to history
        save_calculation_to_history(
            calculator_id="gout",
            calculator_name="Gout Classification",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Share section
        render_share_section(
            calculator_id="gout",
            calculator_name="Gout Classification",
            inputs=inputs_dict,
            results=results_dict,
            show_qr=True
        )
        
        # History section
        render_history_ui(calculator_id="gout", show_actions=True)
    else:
        st.warning("Sử dụng tiêu chuẩn lâm sàng (cần ≥8 điểm):")
        score = 0
        
        pattern = st.radio("Đặc điểm cơn", [0, 1, 2, 3], format_func=lambda x: ["0đ: Không", "1đ: Viêm cổ chân/bàn chân", "2đ: Viêm khớp gối ngón chân cái", "3đ: Đỏ cổ chân/gối ngón chân"][x])
        score += pattern
        
        location = st.checkbox("+1đ: Từng viêm khớp gối ngón chân cái")
        score += 1 if location else 0
        
        time_course = st.radio("Thời gian triệu chứng", [0, 1, 2], format_func=lambda x: ["0đ: Không", "1đ: Bùng phát trong 1 ngày", "2đ: Thuyên giảm trong 14 ngày"][x])
        score += time_course
        
        tophi = st.checkbox("+4đ: Có tophi (hạt gout)")
        score += 4 if tophi else 0
        
        uric_acid = st.radio("Acid uric máu", [0, 2, 3, 4], format_func=lambda x: ["0đ: < 4 mg/dL", "2đ: 4-6", "3đ: 6-8", "4đ: 8-10 hoặc >10"][x])
        score += uric_acid
        
        imaging = st.checkbox("+4đ: X-quang thấy tổn thương gout")
        score += 4 if imaging else 0
        
        if st.button("🔬 Đánh giá Gout", type="primary", use_container_width=True):
            if score >= 8: 
                st.error(f"🚨 **{score} điểm - Chẩn đoán GOUT (theo tiêu chuẩn lâm sàng)**")
                st.info("**Điều trị cấp:** Colchicine/NSAID/Corticosteroid\n\n**Dự phòng:** Allopurinol/Febuxostat khi acid uric > 6 mg/dL")
                
                diagnosis = "Gout (theo tiêu chuẩn lâm sàng)"
            else: 
                st.success(f"✅ **{score} điểm - Chưa đủ tiêu chuẩn Gout lâm sàng**\n\nCân nhắc chẩn đoán khác hoặc chọc dịch khớp tìm tinh thể")
                diagnosis = "Chưa đủ tiêu chuẩn Gout"
            
            # Prepare data for history and share
            inputs_dict = {
                "Crystal": crystal,
                "Pattern": pattern,
                "Location": "Có" if location else "Không",
                "Time course": time_course,
                "Tophi": "Có" if tophi else "Không",
                "Uric acid": uric_acid,
                "Imaging": "Có" if imaging else "Không"
            }
            results_dict = {
                "Score": score,
                "Diagnosis": diagnosis
            }
            
            # Export section
            from components.export import render_export_section
            render_export_section(
                calculator_id="gout",
                calculator_name="Gout Classification",
                inputs=inputs_dict,
                results=results_dict
            )
            
            # Save to history
            save_calculation_to_history(
                calculator_id="gout",
                calculator_name="Gout Classification",
                inputs=inputs_dict,
                results=results_dict
            )
            
            # Share section
            render_share_section(
                calculator_id="gout",
                calculator_name="Gout Classification",
                inputs=inputs_dict,
                results=results_dict,
                show_qr=True
            )
            
            # History section
            render_history_ui(calculator_id="gout", show_actions=True)
    
    # Smart Suggestions
    col_main, col_suggestions = st.columns([2, 1])
    with col_suggestions:
        render_suggestions(
            calculator_id="gout",
            calculator_name="Gout Classification",
            category="Thấp Khớp",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    # References section (always at bottom)
    st.markdown("---")
    references = get_references("Gout Classification")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            show_evidence_level=True,
            show_links=True
        )

if __name__ == "__main__": 
    render()
