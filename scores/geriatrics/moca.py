"""
Montreal Cognitive Assessment (MoCA)
Screening MCI và dementia
Nhạy hơn MMSE với mild cognitive impairment
"""

import streamlit as st

def render_moca(score_id: str = "MoCA"):
    """Render MoCA calculator"""
    
    st.markdown("### Montreal Cognitive Assessment (MoCA)")
    st.markdown("**Screening Mild Cognitive Impairment (MCI) và dementia**")
    st.info("""
    **MoCA** nhạy hơn MMSE trong phát hiện MCI và early dementia.
    Điểm số từ 0-30, cắt điểm <26 gợi ý cognitive impairment.
    
    **Thời gian thực hiện:** ~10 phút
    """)
    
    st.markdown("---")
    
    st.warning("""
    ⚠️ **Lưu ý:** Calculator này chỉ để tính điểm sau khi đã đánh giá bệnh nhân.
    Cần sử dụng form MoCA chuẩn để đánh giá đầy đủ.
    """)
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**1. Visuospatial/Executive (5 điểm)**")
        visuo_trail = st.number_input("Trail Making (1 điểm):", min_value=0, max_value=1, value=0, key="moca_visuo_trail")
        visuo_cube = st.number_input("Vẽ hình khối (1 điểm):", min_value=0, max_value=1, value=0, key="moca_visuo_cube")
        visuo_clock = st.number_input("Vẽ đồng hồ (3 điểm):", min_value=0, max_value=3, value=0, key="moca_visuo_clock")
        
        st.markdown("**2. Naming (3 điểm)**")
        naming = st.number_input("Đặt tên 3 con vật (3 điểm):", min_value=0, max_value=3, value=0, key="moca_naming")
        
        st.markdown("**3. Memory (không tính điểm)**")
        st.caption("Nhắc lại 5 từ (chỉ để test recall)")
        
        st.markdown("**4. Attention (6 điểm)**")
        attention_digit = st.number_input("Forward digit span (2 điểm):", min_value=0, max_value=2, value=0, key="moca_attention_digit")
        attention_backward = st.number_input("Backward digit span (2 điểm):", min_value=0, max_value=2, value=0, key="moca_attention_backward")
        attention_tapping = st.number_input("Tapping (1 điểm):", min_value=0, max_value=1, value=0, key="moca_attention_tapping")
        attention_subtract = st.number_input("Serial 7s (3 điểm):", min_value=0, max_value=3, value=0, key="moca_attention_subtract")
    
    with col2:
        st.markdown("**5. Language (3 điểm)**")
        language_fluency = st.number_input("Sentence repetition (2 điểm):", min_value=0, max_value=2, value=0, key="moca_language_fluency")
        language_fluency2 = st.number_input("Verbal fluency (1 điểm):", min_value=0, max_value=1, value=0, key="moca_language_fluency2")
        
        st.markdown("**6. Abstraction (2 điểm)**")
        abstraction = st.number_input("Abstract thinking (2 điểm):", min_value=0, max_value=2, value=0, key="moca_abstraction")
        
        st.markdown("**7. Delayed Recall (5 điểm)**")
        recall = st.number_input("Nhớ lại 5 từ (5 điểm):", min_value=0, max_value=5, value=0, key="moca_recall")
        
        st.markdown("**8. Orientation (6 điểm)**")
        orientation_date = st.number_input("Ngày tháng (1 điểm):", min_value=0, max_value=1, value=0, key="moca_orientation_date")
        orientation_month = st.number_input("Tháng (1 điểm):", min_value=0, max_value=1, value=0, key="moca_orientation_month")
        orientation_year = st.number_input("Năm (1 điểm):", min_value=0, max_value=1, value=0, key="moca_orientation_year")
        orientation_day = st.number_input("Thứ (1 điểm):", min_value=0, max_value=1, value=0, key="moca_orientation_day")
        orientation_place = st.number_input("Địa điểm (1 điểm):", min_value=0, max_value=1, value=0, key="moca_orientation_place")
        orientation_city = st.number_input("Thành phố (1 điểm):", min_value=0, max_value=1, value=0, key="moca_orientation_city")
        
        # Education adjustment
        education = st.selectbox(
            "Trình độ học vấn:",
            ["≤12 năm", ">12 năm"],
            key="moca_education"
        )
    
    # Calculate total
    visuo_total = visuo_trail + visuo_cube + visuo_clock
    attention_total = attention_digit + attention_backward + attention_tapping + attention_subtract
    language_total = language_fluency + language_fluency2
    orientation_total = orientation_date + orientation_month + orientation_year + orientation_day + orientation_place + orientation_city
    
    total_score = (visuo_total + naming + attention_total + 
                   language_total + abstraction + recall + orientation_total)
    
    # Education adjustment (add 1 point if ≤12 years education)
    if "≤12 năm" in education and total_score < 30:
        total_score += 1
        st.info("Đã điều chỉnh +1 điểm cho bệnh nhân có trình độ học vấn ≤12 năm")
    
    st.markdown("---")
    
    # Results
    st.markdown("#### Kết quả")
    st.markdown(f"### **Điểm số: {min(total_score, 30)}/30**")
    
    # Interpretation
    if total_score >= 26:
        st.success("**Bình thường (26-30 điểm)**")
        st.markdown("""
        - Không có bằng chứng cognitive impairment
        - Nếu có triệu chứng lâm sàng, xem xét đánh giá thêm
        """)
    elif total_score >= 18:
        st.warning("**Mild Cognitive Impairment (18-25 điểm)**")
        st.markdown("""
        - Gợi ý MCI hoặc early dementia
        - Cần đánh giá thêm (neuropsychological testing, imaging)
        - Theo dõi và can thiệp sớm
        """)
    else:
        st.error("**Dementia (0-17 điểm)**")
        st.markdown("""
        - Gợi ý moderate-severe dementia
        - Cần đánh giá chuyên khoa
        - Đánh giá khả năng sống độc lập
        - Xem xét hỗ trợ và chăm sóc
        """)
    
    st.markdown("---")
    
    # Comparison with MMSE
    with st.expander("📊 So sánh MoCA vs MMSE"):
        st.markdown("""
        | Tiêu chí | MoCA | MMSE |
        |----------|------|------|
        | Nhạy với MCI | ✅ Tốt hơn | ⚠️ Kém |
        | Nhạy với dementia | ✅ Tốt | ✅ Tốt |
        | Đánh giá Executive | ✅ Có | ❌ Không |
        | Thời gian | ~10 phút | ~10 phút |
        | Giáo dục ảnh hưởng | Ít hơn | Nhiều hơn |
        
        **Khuyến nghị:**
        - Screening ban đầu: MoCA (nhạy hơn với MCI)
        - Theo dõi diễn biến: Có thể dùng cả hai
        - Bệnh nhân ít học: MoCA có điều chỉnh
        """)
    
    # References
    st.markdown("#### References")
    st.markdown("""
    - Nasreddine ZS, et al. The Montreal Cognitive Assessment, MoCA: a brief screening tool for mild cognitive impairment. J Am Geriatr Soc. 2005;53(4):695-699.
    - MoCA Test. https://www.mocatest.org
    """)
