"""
CAM - Confusion Assessment Method
Đánh giá hôn mê lú lẫn (Delirium)
"""

import streamlit as st
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions

def render():
    """Render CAM calculator"""
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'cam':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    st.title("🧠 CAM - Confusion Assessment Method")
    st.caption("Chẩn đoán Delirium")
    
    st.markdown("""
    **CAM (Confusion Assessment Method):**
    - Công cụ chẩn đoán delirium nhanh
    - Dựa trên 4 tiêu chí chính
    - Độ nhạy: 94-100%, Độ đặc hiệu: 90-95%
    - Thời gian: 2-5 phút
    """)
    
    with st.expander("ℹ️ Giới thiệu CAM"):
        st.markdown("""
        **CAM** chẩn đoán delirium dựa trên 4 tiêu chí.
        
        **Chẩn đoán Delirium:** Cần có cả:
        - Tiêu chí 1 (Khởi phát cấp + dao động) VÀ
        - Tiêu chí 2 (Giảm chú ý) VÀ
        - Tiêu chí 3 (Tư duy rối loạn) HOẶC 4 (Ý thức thay đổi)
        """)
    
    st.markdown("---")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("📋 Tiêu chí CAM")
        
        feature1 = st.checkbox(
            "**1. Khởi phát cấp và dao động**\n\nCó thay đổi cấp tính trạng thái tâm thần so với baseline? Có dao động trong ngày không?",
            help="Thay đổi cấp tính và dao động trong ngày"
        )
        
        feature2 = st.checkbox(
            "**2. Giảm chú ý**\n\nKhó tập trung, dễ bị phân tâm, khó theo dõi câu chuyện?",
            help="Khó tập trung, dễ phân tâm"
        )
        
        feature3 = st.checkbox(
            "**3. Tư duy rối loạn**\n\nSuy nghĩ không mạch lạc, câu chuyện lan man, ý tưởng không rõ ràng?",
            help="Tư duy không mạch lạc"
        )
        
        feature4 = st.checkbox(
            "**4. Thay đổi mức độ ý thức**\n\nTỉnh táo bình thường / Li bì / Lơ mơ / Hôn mê",
            help="Thay đổi mức độ ý thức"
        )
        
        st.markdown("---")
        
        if st.button("🔬 Đánh giá CAM", type="primary", use_container_width=True):
            has_delirium = feature1 and feature2 and (feature3 or feature4)
            
            if has_delirium:
                st.error("""
                🚨 **DƯƠNG TÍNH - Chẩn đoán DELIRIUM**
                
                **Đáp ứng đủ tiêu chí CAM:**
                - ✅ Tiêu chí 1: Khởi phát cấp + dao động
                - ✅ Tiêu chí 2: Giảm chú ý
                - ✅ Tiêu chí 3 hoặc 4
                
                **Xử trí:**
                1. Tìm nguyên nhân (nhiễm trùng, thuốc, rối loạn chuyển hóa...)
                2. Điều trị nguyên nhân
                3. Không dùng thuốc (trừ kích động nguy hiểm)
                4. Định hướng lại, môi trường yên tĩnh
                5. Huy động gia đình
                """)
            else:
                st.success("""
                ✅ **ÂM TÍNH - Không đủ tiêu chí Delirium**
                
                Không đáp ứng tiêu chí CAM. Tuy nhiên:
                - Theo dõi tiếp
                - Đánh giá lại nếu có thay đổi
                - Cân nhắc nguyên nhân khác của thay đổi tâm thần
                """)
            
            # Prepare data for history and share
            inputs_dict = {
                "Tiêu chí 1 (Khởi phát cấp + dao động)": "Có" if feature1 else "Không",
                "Tiêu chí 2 (Giảm chú ý)": "Có" if feature2 else "Không",
                "Tiêu chí 3 (Tư duy rối loạn)": "Có" if feature3 else "Không",
                "Tiêu chí 4 (Thay đổi ý thức)": "Có" if feature4 else "Không"
            }
            
            results_dict = {
                "Kết quả CAM": "Dương tính - Delirium" if has_delirium else "Âm tính - Không có Delirium",
                "Tiêu chí đáp ứng": f"1: {feature1}, 2: {feature2}, 3: {feature3}, 4: {feature4}"
            }
            
            # Export section
            from components.export import render_export_section
            render_export_section(
                title="CAM",
                inputs=inputs_dict,
                results=results_dict
            ,
                calculator_name="CAM"
            )
            
            # Save to history
            save_calculation_to_history(
                calculator_id="cam",
                calculator_name="CAM",
                inputs=inputs_dict,
                results=results_dict
            )
            
            # Share section
            render_share_section(
                calculator_id="cam",
                calculator_name="CAM",
                inputs=inputs_dict,
                results=results_dict,
                show_qr=True
            )
            
            # History section
            render_history_ui(calculator_id="cam", show_actions=True)
            
            with st.expander("📋 Phân loại Delirium"):
                st.markdown("""
                **3 kiểu delirium:**
                - **Hyperactive:** Kích động, ảo giác
                - **Hypoactive:** Lơ mơ, ít nói (dễ bỏ sót)
                - **Mixed:** Kết hợp
                """)
    
    with col2:
        # Smart Suggestions
        render_suggestions(
            calculator_id="cam",
            calculator_name="CAM",
            category="Tâm Thần",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    # Educational content
    st.markdown("---")
    st.subheader("📚 Thông tin bổ sung")
    
    with st.expander("📋 Tiêu chí CAM chi tiết"):
        st.markdown("""
        **Chẩn đoán Delirium cần:**
        - ✅ Tiêu chí 1: Khởi phát cấp + dao động
        - ✅ Tiêu chí 2: Giảm chú ý
        - ✅ Tiêu chí 3 HOẶC 4
        
        **Nguyên nhân thường gặp:**
        - Nhiễm trùng (UTI, pneumonia...)
        - Thuốc (anticholinergic, benzodiazepine...)
        - Rối loạn chuyển hóa
        - Thiếu oxy
        - Đau, mất ngủ
        """)
    
    # References section (Phase 1)
    st.markdown("---")
    references = get_references("CAM")
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
        - Inouye SK, et al. Clarifying confusion: the confusion assessment method. A new method for detection of delirium. Ann Intern Med. 1990;113(12):941-8.
        - Wei LA, et al. The Confusion Assessment Method: a systematic review of current usage. J Am Geriatr Soc. 2008;56(5):823-30.
        """)

if __name__ == "__main__":
    render()

