"""
MMSE - Mini Mental State Exam
Đánh giá nhận thức
"""

import streamlit as st
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions


def render():
    """Render MMSE calculator"""
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'mmse':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    st.title("🧠 MMSE - Mini Mental State Exam")
    st.caption("Đánh giá nhận thức - Sàng lọc suy giảm nhận thức")
    
    st.markdown("""
    **MMSE (Mini Mental State Examination):**
    - Công cụ sàng lọc suy giảm nhận thức phổ biến
    - Thang điểm: 0-30
    - Thời gian: 5-10 phút
    - Điểm cắt: < 24-27 (tùy trình độ học vấn)
    """)
    
    st.markdown("---")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("📝 Nhập điểm từng phần")
        
        orientation = st.number_input(
            "Định hướng (0-10)",
            min_value=0,
            max_value=10,
            value=10,
            format="%d",
            help="Ngày, tháng, năm, mùa, địa điểm"
        )
        
        registration = st.number_input(
            "Ghi nhớ (0-3)",
            min_value=0,
            max_value=3,
            value=3,
            format="%d",
            help="Nhắc lại 3 từ"
        )
        
        attention = st.number_input(
            "Chú ý (0-5)",
            min_value=0,
            max_value=5,
            value=5,
            format="%d",
            help="Đếm ngược từ 100, đánh vần ngược"
        )
        
        recall = st.number_input(
            "Nhớ lại (0-3)",
            min_value=0,
            max_value=3,
            value=3,
            format="%d",
            help="Nhắc lại 3 từ đã nói trước đó"
        )
        
        language = st.number_input(
            "Ngôn ngữ (0-9)",
            min_value=0,
            max_value=9,
            value=9,
            format="%d",
            help="Đặt tên, nhắc lại câu, làm theo lệnh, đọc, viết, vẽ"
        )
        
        total = orientation + registration + attention + recall + language
        
        if st.button("🔬 Tính MMSE", type="primary", use_container_width=True):
            # Interpret score
            if total >= 27:
                status = "Bình thường"
                color = "#28a745"
                level = "normal"
            elif total >= 21:
                status = "Suy giảm nhẹ"
                color = "#fd7e14"
                level = "mild"
            elif total >= 10:
                status = "Suy giảm trung bình"
                color = "#fd7e14"
                level = "moderate"
            else:
                status = "Suy giảm nặng"
                color = "#dc3545"
                level = "severe"
            
            st.markdown(f"""
            <div style='background: linear-gradient(135deg, {color}22 0%, {color}44 100%); 
                        padding: 30px; border-radius: 15px; border-left: 5px solid {color}; margin: 20px 0;'>
                <h2 style='color: {color}; margin: 0; text-align: center;'>
                    MMSE: {total}/30
                </h2>
                <p style='text-align: center; margin-top: 10px; font-size: 1.2em; font-weight: bold;'>
                    {status}
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            # Detailed breakdown
            st.markdown("### 📊 Chi tiết điểm:")
            st.markdown(f"""
            - **Định hướng:** {orientation}/10
            - **Ghi nhớ:** {registration}/3
            - **Chú ý:** {attention}/5
            - **Nhớ lại:** {recall}/3
            - **Ngôn ngữ:** {language}/9
            - **Tổng điểm:** {total}/30
            """)
            
            # Interpretation
            st.markdown("---")
            st.markdown("### 💡 Giải thích:")
            
            if level == "normal":
                st.success("""
                **✅ Bình thường (≥27 điểm)**
                
                - Không có bằng chứng suy giảm nhận thức trên test này
                - Nếu có triệu chứng, cân nhắc nguyên nhân khác
                """)
            elif level == "mild":
                st.warning("""
                **⚠️ Suy giảm nhẹ (21-26 điểm)**
                
                - Có thể là MCI (Mild Cognitive Impairment)
                - Cần đánh giá thêm
                - Theo dõi tiến triển
                """)
            elif level == "moderate":
                st.warning("""
                **⚠️ Suy giảm trung bình (10-20 điểm)**
                
                - Có thể là Dementia
                - Cần đánh giá lâm sàng chi tiết
                - Xét nghiệm máu, chẩn đoán hình ảnh
                """)
            else:
                st.error("""
                **🚨 Suy giảm nặng (<10 điểm)**
                
                - Dementia nặng
                - Cần đánh giá và điều trị tích cực
                - Hội chẩn thần kinh
                """)
            
            # Prepare data for history and share
            inputs_dict = {
                "Định hướng": orientation,
                "Ghi nhớ": registration,
                "Chú ý": attention,
                "Nhớ lại": recall,
                "Ngôn ngữ": language
            }
            
            results_dict = {
                "Tổng điểm MMSE": f"{total}/30",
                "Mức độ": status,
                "Phân loại": level
            }
            
            # Export section
            from components.export import render_export_section
            render_export_section(
                calculator_id="mmse",
                calculator_name="MMSE",
                inputs=inputs_dict,
                results=results_dict
            )
            
            # Save to history
            save_calculation_to_history(
                calculator_id="mmse",
                calculator_name="MMSE",
                inputs=inputs_dict,
                results=results_dict
            )
            
            # Share section
            render_share_section(
                calculator_id="mmse",
                calculator_name="MMSE",
                inputs=inputs_dict,
                results=results_dict,
                show_qr=True
            )
            
            # History section
            from components.calculation_history import render_history_ui
            render_history_ui(calculator_id="mmse", show_actions=True)
    
    with col2:
        # Smart Suggestions
        render_suggestions(
            calculator_id="mmse",
            calculator_name="MMSE",
            category="Tâm Thần",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    # Educational content
    st.markdown("---")
    st.subheader("📚 Thông tin bổ sung")
    
    with st.expander("📋 Phân loại mức độ"):
        st.markdown("""
        | Điểm | Mức độ | Ý nghĩa |
        |------|--------|---------|
        | ≥27 | Bình thường | Không có suy giảm nhận thức |
        | 21-26 | Suy giảm nhẹ | MCI có thể |
        | 10-20 | Suy giảm trung bình | Dementia |
        | <10 | Suy giảm nặng | Dementia nặng |
        
        **Lưu ý:** Điểm cắt có thể thay đổi theo trình độ học vấn
        """)
    
    with st.expander("🔄 MMSE vs MoCA"):
        st.markdown("""
        **MMSE:**
        - Thời gian: 5-10 phút
        - Điểm cắt: < 24-27
        - Phù hợp sàng lọc nhanh
        
        **MoCA:**
        - Thời gian: 10-15 phút
        - Điểm cắt: < 26
        - Nhạy hơn với MCI
        - Phù hợp bệnh nhân giáo dục cao
        """)
    
    # References section (Phase 1)
    st.markdown("---")
    references = get_references("MMSE")
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
        - Folstein MF, Folstein SE, McHugh PR. "Mini-mental state". A practical method for grading the cognitive state of patients for the clinician. J Psychiatr Res. 1975;12(3):189-98.
        - Tombaugh TN, McIntyre NJ. The mini-mental state examination: a comprehensive review. J Am Geriatr Soc. 1992;40(9):922-35.
        """)


if __name__ == "__main__":
    render()

