"""
Mini-Mental State Examination (MMSE)
Screening cognitive impairment ở bệnh nhân cao tuổi
"""

import streamlit as st

def render_mmse(score_id: str = "MMSE"):
    """Render MMSE calculator"""
    
    st.markdown("### Mini-Mental State Examination (MMSE)")
    st.markdown("**Screening cognitive impairment**")
    st.info("""
    **MMSE** là công cụ screening phổ biến nhất cho cognitive impairment.
    Điểm số từ 0-30, cắt điểm <24 gợi ý cognitive impairment.
    
    **Thời gian thực hiện:** ~10 phút
    """)
    
    st.markdown("---")
    
    st.markdown("#### Hướng dẫn đánh giá")
    st.warning("""
    ⚠️ **Lưu ý:** Calculator này chỉ để tính điểm sau khi đã đánh giá bệnh nhân.
    Cần thực hiện đầy đủ 11 mục theo hướng dẫn chuẩn.
    """)
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**1. Orientation (10 điểm)**")
        orientation_time = st.number_input("Thời gian (5 điểm):", min_value=0, max_value=5, value=0, key="mmse_orientation_time")
        orientation_place = st.number_input("Địa điểm (5 điểm):", min_value=0, max_value=5, value=0, key="mmse_orientation_place")
        
        st.markdown("**2. Registration (3 điểm)**")
        registration = st.number_input("Nhắc lại 3 từ (3 điểm):", min_value=0, max_value=3, value=0, key="mmse_registration")
        
        st.markdown("**3. Attention & Calculation (5 điểm)**")
        attention = st.selectbox(
            "Tính toán (5 điểm):",
            ["0 điểm", "1 điểm", "2 điểm", "3 điểm", "4 điểm", "5 điểm"],
            key="mmse_attention"
        )
        attention_score = int(attention.split()[0])
        
        st.markdown("**4. Recall (3 điểm)**")
        recall = st.number_input("Nhớ lại 3 từ (3 điểm):", min_value=0, max_value=3, value=0, key="mmse_recall")
        
        st.markdown("**5. Language (2 điểm)**")
        language_naming = st.number_input("Đặt tên đồ vật (2 điểm):", min_value=0, max_value=2, value=0, key="mmse_naming")
    
    with col2:
        st.markdown("**6. Language (1 điểm)**")
        language_repetition = st.number_input("Lặp lại câu (1 điểm):", min_value=0, max_value=1, value=0, key="mmse_repetition")
        
        st.markdown("**7. Language (3 điểm)**")
        language_command = st.selectbox(
            "Thực hiện lệnh (3 điểm):",
            ["0 điểm", "1 điểm", "2 điểm", "3 điểm"],
            key="mmse_command"
        )
        command_score = int(language_command.split()[0])
        
        st.markdown("**8. Language (1 điểm)**")
        language_reading = st.number_input("Đọc và làm theo (1 điểm):", min_value=0, max_value=1, value=0, key="mmse_reading")
        
        st.markdown("**9. Language (1 điểm)**")
        language_writing = st.number_input("Viết câu (1 điểm):", min_value=0, max_value=1, value=0, key="mmse_writing")
        
        st.markdown("**10. Construction (1 điểm)**")
        construction = st.number_input("Vẽ hình (1 điểm):", min_value=0, max_value=1, value=0, key="mmse_construction")
    
    # Calculate total
    total_score = (orientation_time + orientation_place + registration + 
                   attention_score + recall + language_naming + 
                   language_repetition + command_score + language_reading + 
                   language_writing + construction)
    
    st.markdown("---")
    
    # Results
    st.markdown("#### Kết quả")
    st.markdown(f"### **Điểm số: {total_score}/30**")
    
    # Interpretation
    if total_score >= 24:
        st.success("**Bình thường (24-30 điểm)**")
        st.markdown("""
        - Không có bằng chứng cognitive impairment
        - Nếu có triệu chứng lâm sàng, xem xét đánh giá sâu hơn (MoCA)
        """)
    elif total_score >= 18:
        st.warning("**Mild cognitive impairment (18-23 điểm)**")
        st.markdown("""
        - Gợi ý mild cognitive impairment hoặc mild dementia
        - Cần đánh giá thêm (MoCA, neuropsychological testing)
        - Xem xét nguyên nhân: Alzheimer, vascular, mixed, etc.
        """)
    elif total_score >= 10:
        st.error("**Moderate cognitive impairment (10-17 điểm)**")
        st.markdown("""
        - Gợi ý moderate dementia
        - Cần đánh giá chuyên khoa thần kinh/geriatric
        - Đánh giá khả năng sống độc lập
        """)
    else:
        st.error("**Severe cognitive impairment (0-9 điểm)**")
        st.markdown("""
        - Gợi ý severe dementia
        - Cần hỗ trợ nhiều trong ADL
        - Đánh giá goals of care
        - Xem xét chăm sóc giảm nhẹ
        """)
    
    st.markdown("---")
    
    # Notes
    with st.expander("📝 Lưu ý về MMSE"):
        st.markdown("""
        **Ưu điểm:**
        - Phổ biến, dễ sử dụng
        - Thời gian ngắn (~10 phút)
        - Độ nhạy tốt với moderate-severe dementia
        
        **Nhược điểm:**
        - Kém nhạy với mild cognitive impairment
        - Bị ảnh hưởng bởi giáo dục, ngôn ngữ
        - Không đánh giá executive function tốt
        
        **Khi nào dùng:**
        - Screening cognitive impairment
        - Theo dõi diễn biến
        - Nghiên cứu và đánh giá
        
        **Khi nào không dùng:**
        - Bệnh nhân không biết đọc/viết
        - Bệnh nhân có khiếm khuyết thị giác/nhận thức nghiêm trọng
        - Cần đánh giá chi tiết hơn → dùng MoCA
        """)
    
    # References
    st.markdown("#### References")
    st.markdown("""
    - Folstein MF, et al. "Mini-mental state". A practical method for grading the cognitive state of patients for the clinician. J Psychiatr Res. 1975;12(3):189-198.
    - Tombaugh TN, McIntyre NJ. The mini-mental state examination: a comprehensive review. J Am Geriatr Soc. 1992;40(9):922-935.
    """)
