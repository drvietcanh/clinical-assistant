"""
CIWA-Ar - Clinical Institute Withdrawal Assessment for Alcohol
Đánh giá mức độ nặng cai rượu
"""

import streamlit as st
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions

def calculate_ciwa(nausea, tremor, sweating, anxiety, agitation, tactile, auditory, visual, headache, orientation):
    """Tính CIWA-Ar score"""
    total = nausea + tremor + sweating + anxiety + agitation + tactile + auditory + visual + headache + orientation
    
    if total < 8:
        severity = "Nhẹ"; management = "Theo dõi, không cần thuốc"; color = "green"
    elif total <= 15:
        severity = "Trung bình"; management = "Cân nhắc benzodiazepine"; color = "orange"
    else:
        severity = "Nặng"; management = "Benzodiazepine ngay, theo dõi ICU"; color = "red"
    
    return {"total_score": total, "severity": severity, "management": management, "color": color}

def render():
    """Render CIWA-Ar calculator"""
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'ciwa':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    st.title("🍺 CIWA-Ar - Clinical Institute Withdrawal Assessment")
    st.caption("Đánh giá mức độ nặng cai rượu")
    
    st.markdown("""
    **CIWA-Ar (Clinical Institute Withdrawal Assessment for Alcohol - Revised):**
    - Đánh giá mức độ nặng cai rượu
    - Hướng dẫn điều trị benzodiazepine
    - Thang điểm: 0-67
    - Đánh giá lại mỗi 1-4 giờ
    """)
    
    with st.expander("ℹ️ Giới thiệu CIWA-Ar"):
        st.markdown("""
        **CIWA-Ar** đánh giá mức độ nặng cai rượu, hướng dẫn điều trị benzodiazepine.
        
        **Thang điểm:** 0-67
        
        **Phân loại:**
        - < 8: Nhẹ - Không cần thuốc
        - 8-15: Trung bình - Cân nhắc benzodiazepine
        - > 15: Nặng - Benzodiazepine ngay, theo dõi ICU
        """)
    
    st.markdown("---")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("📝 Đánh giá triệu chứng")
        
        nausea = st.slider("1. Buồn nôn/Nôn", 0, 7, 0, help="0=Không, 7=Nôn liên tục")
        tremor = st.slider("2. Run", 0, 7, 0, help="0=Không, 7=Run nặng")
        sweating = st.slider("3. Đổ mồ hôi", 0, 7, 0, help="0=Không, 7=Đổ nhiều mồ hôi")
        anxiety = st.slider("4. Lo âu", 0, 7, 0, help="0=Không, 7=Lo âu nặng")
        agitation = st.slider("5. Kích động", 0, 7, 0, help="0=Không, 7=Kích động liên tục")
        tactile = st.slider("6. Ảo giác xúc giác", 0, 7, 0, help="0=Không, 7=Ảo giác xúc giác liên tục")
        auditory = st.slider("7. Ảo giác thính giác", 0, 7, 0, help="0=Không, 7=Ảo giác rõ")
        visual = st.slider("8. Ảo giác thị giác", 0, 7, 0, help="0=Không, 7=Ảo giác rõ")
        headache = st.slider("9. Đau đầu", 0, 7, 0, help="0=Không, 7=Đau đầu nặng")
        orientation = st.slider("10. Định hướng", 0, 4, 0, help="0=Định hướng đầy đủ, 4=Không định hướng")
        
        if st.button("🔬 Tính CIWA-Ar", type="primary", use_container_width=True):
            result = calculate_ciwa(nausea, tremor, sweating, anxiety, agitation, tactile, auditory, visual, headache, orientation)
            score_color = {"green": "#28a745", "orange": "#fd7e14", "red": "#dc3545"}[result["color"]]
            
            st.markdown(f"""
            <div style='background: linear-gradient(135deg, {score_color}22 0%, {score_color}44 100%); 
                        padding: 30px; border-radius: 15px; border-left: 5px solid {score_color}; margin: 20px 0;'>
                <h2 style='color: {score_color}; margin: 0; text-align: center;'>
                    CIWA-Ar: {result['total_score']}/67
                </h2>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
            <div style='background-color: {score_color}22; padding: 20px; border-radius: 10px; border: 2px solid {score_color};'>
                <h3 style='color: {score_color};'>🎯 Mức độ: {result['severity']}</h3>
                <p style='font-size: 1.2em;'><strong>Điều trị:</strong> {result['management']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.info("""
            **Khuyến cáo điều trị:**
            - **< 8:** Không cần benzodiazepine, theo dõi
            - **8-15:** Lorazepam 1-2mg hoặc Diazepam 5-10mg
            - **> 15:** Lorazepam 2-4mg hoặc Diazepam 10-20mg, đánh giá lại mỗi 1h
            
            **Đánh giá lại:** Mỗi 1-4 giờ tùy mức độ
            """)
            
            # Prepare data for history and share
            inputs_dict = {
                "Buồn nôn/Nôn": nausea,
                "Run": tremor,
                "Đổ mồ hôi": sweating,
                "Lo âu": anxiety,
                "Kích động": agitation,
                "Ảo giác xúc giác": tactile,
                "Ảo giác thính giác": auditory,
                "Ảo giác thị giác": visual,
                "Đau đầu": headache,
                "Định hướng": orientation
            }
            
            results_dict = {
                "Tổng điểm CIWA-Ar": f"{result['total_score']}/67",
                "Mức độ": result['severity'],
                "Điều trị": result['management']
            }
            
            # Export section
            from components.export import render_export_section
            render_export_section(
                title="CIWA-Ar",
                inputs=inputs_dict,
                results=results_dict
            ,
                calculator_name="CIWA-Ar"
            )
            
            # Save to history
            save_calculation_to_history(
                calculator_id="ciwa",
                calculator_name="CIWA-Ar",
                inputs=inputs_dict,
                results=results_dict
            )
            
            # Share section
            render_share_section(
                calculator_id="ciwa",
                calculator_name="CIWA-Ar",
                inputs=inputs_dict,
                results=results_dict,
                show_qr=True
            )
            
            # History section
            render_history_ui(calculator_id="ciwa", show_actions=True)
    
    with col2:
        # Smart Suggestions
        render_suggestions(
            calculator_id="ciwa",
            calculator_name="CIWA-Ar",
            category="Tâm Thần",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    # Educational content
    st.markdown("---")
    st.subheader("📚 Thông tin bổ sung")
    
    with st.expander("💊 Điều trị chi tiết"):
        st.markdown("""
        **Benzodiazepine:**
        - **Lorazepam:** 1-4mg IV/PO q1-4h
        - **Diazepam:** 5-20mg IV/PO q1-4h
        - **Chlordiazepoxide:** 25-100mg PO q4-6h
        
        **Bổ sung:**
        - Thiamine 100mg IV/IM
        - Folate 1mg PO
        - Multivitamin
        - Magnesium nếu thiếu
        """)
    
    # References section (Phase 1)
    st.markdown("---")
    references = get_references("CIWA-Ar")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            show_evidence_level=True,
            show_links=True
        )
    else:
        st.caption("""
        **Tài liệu tham khảo:**
        - Sullivan JT, et al. Assessment of alcohol withdrawal: the revised clinical institute withdrawal assessment for alcohol scale (CIWA-Ar). Br J Addict. 1989;84(11):1353-7.
        - Mayo-Smith MF. Pharmacological management of alcohol withdrawal. A meta-analysis and evidence-based practice guideline. JAMA. 1997;278(2):144-51.
        """)

if __name__ == "__main__":
    render()

