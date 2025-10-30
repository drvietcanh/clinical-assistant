"""
ECOG Performance Status (Eastern Cooperative Oncology Group)
Đánh giá thể trạng bệnh nhân ung thư
"""

import streamlit as st


def get_ecog_criteria():
    """Get ECOG performance status criteria"""
    return {
        0: {
            "status": "Hoàn toàn hoạt động",
            "description": "Có thể thực hiện tất cả các hoạt động như trước khi mắc bệnh mà không bị hạn chế",
            "details": "Không có triệu chứng, có thể làm việc bình thường",
            "color": "🟢",
            "prognosis": "Tiên lượng tốt nhất",
            "treatment": "Phù hợp với tất cả các phác đồ điều trị, kể cả thử nghiệm lâm sàng",
            "survival": "Thời gian sống thêm dài nhất"
        },
        1: {
            "status": "Hạn chế hoạt động nặng",
            "description": "Có triệu chứng nhưng vẫn đi lại được. Có thể làm công việc nhẹ hoặc công việc văn phòng",
            "details": "Không thể làm việc nặng nhưng vẫn tự chăm sóc bản thân",
            "color": "🟡",
            "prognosis": "Tiên lượng tốt",
            "treatment": "Phù hợp với hầu hết các phác đồ điều trị tiêu chuẩn",
            "survival": "Thời gian sống thêm tốt"
        },
        2: {
            "status": "Tự chăm sóc được nhưng không thể làm việc",
            "description": "Đi lại được và tự chăm sóc bản thân nhưng không thể làm việc. Thức dậy > 50% thời gian trong ngày",
            "details": "Có thể đi lại nhưng cần nghỉ ngơi nhiều",
            "color": "🟠",
            "prognosis": "Tiên lượng trung bình",
            "treatment": "Có thể điều trị nhưng cần cân nhắc độc tính. Một số phác đồ có thể không phù hợp",
            "survival": "Thời gian sống thêm trung bình"
        },
        3: {
            "status": "Chỉ tự chăm sóc hạn chế",
            "description": "Chỉ tự chăm sóc bản thân hạn chế. Nằm giường hoặc ngồi ghế > 50% thời gian thức",
            "details": "Cần hỗ trợ đáng kể trong sinh hoạt hàng ngày",
            "color": "🔴",
            "prognosis": "Tiên lượng kém",
            "treatment": "Điều trị hạn chế. Chỉ dùng phác đồ nhẹ hoặc best supportive care",
            "survival": "Thời gian sống thêm ngắn"
        },
        4: {
            "status": "Hoàn toàn không thể tự chăm sóc",
            "description": "Hoàn toàn tàn tật. Không thể tự chăm sóc bản thân. Nằm liệt giường hoàn toàn",
            "details": "Cần chăm sóc toàn diện",
            "color": "🔴",
            "prognosis": "Tiên lượng rất kém",
            "treatment": "Chỉ best supportive care / chăm sóc giảm nhẹ. Không phù hợp với hóa trị tích cực",
            "survival": "Thời gian sống thêm rất ngắn (thường < 3 tháng)"
        }
    }


def get_treatment_recommendations(ecog_score):
    """
    Get treatment recommendations based on ECOG score
    
    Args:
        ecog_score: ECOG performance status (0-4)
    
    Returns:
        dict: Treatment recommendations
    """
    recommendations = {
        0: {
            "chemotherapy": "✅ Phù hợp với tất cả phác đồ, kể cả liều cao",
            "clinical_trials": "✅ Phù hợp tham gia thử nghiệm lâm sàng",
            "surgery": "✅ Phù hợp phẫu thuật lớn",
            "radiation": "✅ Phù hợp xạ trị tích cực",
            "immunotherapy": "✅ Phù hợp điều trị miễn dịch",
            "monitoring": "Theo dõi định kỳ, đánh giá đáp ứng"
        },
        1: {
            "chemotherapy": "✅ Phù hợp hầu hết phác đồ điều trị",
            "clinical_trials": "✅ Có thể tham gia nhiều thử nghiệm",
            "surgery": "✅ Phù hợp phẫu thuật",
            "radiation": "✅ Phù hợp xạ trị",
            "immunotherapy": "✅ Phù hợp điều trị miễn dịch",
            "monitoring": "Theo dõi sát, đánh giá thể trạng thường xuyên"
        },
        2: {
            "chemotherapy": "⚠️ Cân nhắc liều giảm hoặc phác đồ ít độc tính",
            "clinical_trials": "⚠️ Chỉ một số thử nghiệm chấp nhận",
            "surgery": "⚠️ Xem xét kỹ nguy cơ-lợi ích",
            "radiation": "✅ Có thể xạ trị giảm nhẹ",
            "immunotherapy": "⚠️ Xem xét cẩn thận",
            "monitoring": "Theo dõi sát, hỗ trợ dinh dưỡng và phục hồi chức năng"
        },
        3: {
            "chemotherapy": "❌ Thường không phù hợp với phác đồ tích cực. Chỉ xem xét phác đồ nhẹ đơn thuốc",
            "clinical_trials": "❌ Không phù hợp hầu hết thử nghiệm",
            "surgery": "❌ Không phù hợp phẫu thuật lớn",
            "radiation": "⚠️ Chỉ xạ trị giảm nhẹ triệu chứng",
            "immunotherapy": "❌ Thường không phù hợp",
            "monitoring": "Chăm sóc hỗ trợ tích cực, kiểm soát triệu chứng"
        },
        4: {
            "chemotherapy": "❌ Không phù hợp hóa trị",
            "clinical_trials": "❌ Không phù hợp thử nghiệm",
            "surgery": "❌ Không phù hợp phẫu thuật",
            "radiation": "❌ Chỉ xạ trị giảm nhẹ nếu cần thiết",
            "immunotherapy": "❌ Không phù hợp",
            "monitoring": "Best supportive care, chăm sóc giảm nhẹ, hospice care"
        }
    }
    
    return recommendations.get(ecog_score, recommendations[4])


def render():
    """Render the ECOG Performance Status calculator"""
    
    st.title("🎗️ ECOG Performance Status")
    st.markdown("""
    ### Đánh Giá Thể Trạng Bệnh Nhân Ung Thư
    
    **ECOG (Eastern Cooperative Oncology Group):**
    - Thang đo thể trạng được sử dụng rộng rãi nhất trong ung thư học
    - Đánh giá khả năng tự chăm sóc và hoạt động của bệnh nhân
    - Từ 0 (hoàn toàn khỏe mạnh) đến 4 (liệt giường hoàn toàn)
    
    **Ý nghĩa lâm sàng:**
    - **Quyết định điều trị:** Phác đồ hóa trị, phẫu thuật, tham gia thử nghiệm
    - **Tiên lượng:** Thời gian sống thêm
    - **Theo dõi:** Đánh giá đáp ứng và tiến triển bệnh
    
    **Ứng dụng:**
    - Tất cả loại ung thư
    - Clinical trials (tiêu chí chọn bệnh nhân)
    - Theo dõi longitudinal
    - Quyết định chăm sóc cuối đời
    """)
    
    st.markdown("---")
    
    # Selection section
    st.subheader("📋 Chọn Mức Độ Thể Trạng")
    
    st.info("""
    **Hướng dẫn:** Chọn mô tả phù hợp nhất với tình trạng hiện tại của bệnh nhân
    """)
    
    ecog_options = get_ecog_criteria()
    
    # Create selection options with detailed descriptions
    selected_ecog = st.radio(
        "**Chọn ECOG Performance Status:**",
        options=[0, 1, 2, 3, 4],
        format_func=lambda x: f"ECOG {x}: {ecog_options[x]['status']}",
        help="Chọn mức độ phù hợp nhất"
    )
    
    # Display selected status details
    selected_info = ecog_options[selected_ecog]
    
    st.markdown("---")
    st.subheader("📊 Mô Tả Chi Tiết")
    
    st.info(f"""
    **{selected_info['color']} ECOG {selected_ecog}: {selected_info['status']}**
    
    **Mô tả:** {selected_info['description']}
    
    **Chi tiết:** {selected_info['details']}
    """)
    
    # Show all levels for comparison
    with st.expander("👀 Xem tất cả các mức độ ECOG"):
        for score, info in ecog_options.items():
            st.markdown(f"""
            **{info['color']} ECOG {score}: {info['status']}**
            - {info['description']}
            """)
            st.markdown("---")
    
    if st.button("📈 Phân Tích Đầy Đủ", type="primary", use_container_width=True):
        st.markdown("---")
        st.subheader("🎯 Đánh Giá & Khuyến Nghị")
        
        # Prognosis
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric(
                "ECOG Score",
                selected_ecog,
                help="Điểm thể trạng (0-4)"
            )
        
        with col2:
            if selected_ecog <= 1:
                st.success(f"**Tiên lượng:** {selected_info['prognosis']}")
            elif selected_ecog == 2:
                st.warning(f"**Tiên lượng:** {selected_info['prognosis']}")
            else:
                st.error(f"**Tiên lượng:** {selected_info['prognosis']}")
        
        st.markdown("---")
        
        # Treatment recommendations
        st.subheader("💊 Khuyến Nghị Điều Trị")
        
        treatment_rec = get_treatment_recommendations(selected_ecog)
        
        st.info(f"""
        **Hóa trị liệu:**  
        {treatment_rec['chemotherapy']}
        
        **Thử nghiệm lâm sàng:**  
        {treatment_rec['clinical_trials']}
        
        **Phẫu thuật:**  
        {treatment_rec['surgery']}
        
        **Xạ trị:**  
        {treatment_rec['radiation']}
        
        **Điều trị miễn dịch:**  
        {treatment_rec['immunotherapy']}
        
        **Theo dõi:**  
        {treatment_rec['monitoring']}
        """)
        
        # Prognosis and survival
        st.markdown("---")
        st.subheader("📈 Tiên Lượng & Thời Gian Sống Thêm")
        
        st.warning(f"""
        **Tổng quan:** {selected_info['survival']}
        
        **Lưu ý quan trọng:**
        - Thời gian sống thêm phụ thuộc nhiều vào:
          + Loại ung thư
          + Giai đoạn bệnh
          + Đáp ứng điều trị
          + Các yếu tố tiên lượng khác
        - ECOG là một trong nhiều yếu tố tiên lượng
        - Cần đánh giá tổng thể lâm sàng
        """)
        
        # Special recommendations based on score
        if selected_ecog >= 3:
            st.markdown("---")
            st.error("""
            ### ⚠️ Khuyến Nghị Đặc Biệt - ECOG 3-4
            
            **Ưu tiên:**
            1. **Chăm sóc hỗ trợ (Supportive Care):**
               - Kiểm soát đau
               - Kiểm soát buồn nôn/nôn
               - Hỗ trợ dinh dưỡng
               - Phòng ngừa biến chứng
            
            2. **Cân nhắc chăm sóc giảm nhẹ (Palliative Care):**
               - Tư vấn sớm về chăm sóc giảm nhẹ
               - Thảo luận về mục tiêu điều trị
               - Kế hoạch chăm sóc cuối đời (nếu ECOG 4)
            
            3. **Đánh giá lại:**
               - Một số bệnh nhân có thể cải thiện với supportive care
               - Xem xét lại khả năng điều trị sau khi thể trạng cải thiện
               - Tái đánh giá ECOG sau 1-2 tuần
            
            4. **Thảo luận với bệnh nhân/gia đình:**
               - Giải thích trung thực về tiên lượng
               - Thảo luận về lựa chọn điều trị
               - Advance care planning
               - Hospice care nếu thích hợp
            """)
    
    # Educational content
    st.markdown("---")
    st.subheader("📚 Thông Tin Bổ Sung")
    
    with st.expander("📊 ECOG vs Karnofsky Performance Scale"):
        st.markdown("""
        ### So sánh hai thang đo thể trạng:
        
        | ECOG | Mô tả | Karnofsky (%) | Mô tả Karnofsky |
        |------|-------|---------------|-----------------|
        | 0 | Hoàn toàn hoạt động | 100 | Bình thường, không triệu chứng |
        | 0 | | 90 | Hoạt động bình thường, triệu chứng nhẹ |
        | 1 | Hạn chế hoạt động nặng | 80 | Hoạt động bình thường với nỗ lực |
        | 1 | | 70 | Tự chăm sóc, không hoạt động bình thường |
        | 2 | Không thể làm việc | 60 | Cần hỗ trợ thỉnh thoảng |
        | 2 | | 50 | Cần hỗ trợ đáng kể |
        | 3 | Tự chăm sóc hạn chế | 40 | Tàn tật, cần chăm sóc đặc biệt |
        | 3 | | 30 | Tàn tật nặng |
        | 4 | Không tự chăm sóc | 20 | Bệnh rất nặng, cần nhập viện |
        | 4 | | 10 | Hấp hối |
        
        **ECOG:**
        - ✅ Đơn giản hơn (5 mức)
        - ✅ Dễ nhớ
        - ✅ Được sử dụng rộng rãi trong trials
        - ✅ Inter-rater reliability tốt hơn
        
        **Karnofsky:**
        - Chi tiết hơn (11 mức: 0-100%)
        - Phức tạp hơn
        - Ít phổ biến trong practice hiện đại
        - Vẫn dùng trong một số trials cũ
        
        **Khuyến cáo:** Sử dụng ECOG trong hầu hết trường hợp
        """)
    
    with st.expander("🎯 Cách Đánh Giá ECOG Chính Xác"):
        st.markdown("""
        ### Nguyên tắc đánh giá:
        
        **1. Đánh giá thực tế, không "mong muốn":**
        - Đánh giá những gì bệnh nhân thực sự LÀM
        - Không phải những gì họ CÓ THỂ làm
        - Không phải những gì họ MUỐN làm
        
        **2. Câu hỏi gợi ý:**
        
        **ECOG 0 vs 1:**
        - "Anh/chị có thể làm việc bình thường không?"
        - "Có hoạt động nào bị hạn chế không?"
        - ECOG 0: Không hạn chế gì
        - ECOG 1: Không thể làm việc nặng
        
        **ECOG 1 vs 2:**
        - "Anh/chị có thể đi làm không?"
        - "Có thể làm việc nhẹ không?"
        - ECOG 1: Có thể làm việc nhẹ
        - ECOG 2: Không thể làm việc gì
        
        **ECOG 2 vs 3:**
        - "Anh/chị dành bao nhiêu % thời gian thức ở trên giường?"
        - ECOG 2: < 50% thời gian
        - ECOG 3: > 50% thời gian
        
        **ECOG 3 vs 4:**
        - "Anh/chị có thể tự đi vệ sinh không?"
        - "Có thể tự ăn không?"
        - ECOG 3: Vẫn tự chăm sóc cơ bản (hạn chế)
        - ECOG 4: Không thể tự chăm sóc gì
        
        **3. Đánh giá trong tuần qua:**
        - Không đánh giá trong ngày xấu nhất
        - Không đánh giá trong ngày tốt nhất
        - Đánh giá mức độ trung bình trong 1 tuần qua
        
        **4. Nguyên nhân:**
        - Đánh giá thể trạng THỰC TẾ
        - Không phân biệt do ung thư hay do bệnh kèm
        - Nếu bệnh nhân có COPD nặng → ECOG vẫn phản ánh thực tế
        """)
    
    with st.expander("💊 ECOG và Quyết Định Điều Trị"):
        st.markdown("""
        ### Vai trò của ECOG trong điều trị:
        
        **1. Clinical Trials:**
        - Hầu hết trials yêu cầu ECOG 0-1 hoặc 0-2
        - Trials phase I thường chỉ nhận ECOG 0-1
        - Một số trials giảm nhẹ chấp nhận ECOG 2-3
        
        **2. Hóa trị liệu:**
        
        **ECOG 0-1:**
        - Phù hợp tất cả phác đồ
        - Liều chuẩn
        - Ít cần điều chỉnh
        
        **ECOG 2:**
        - Xem xét giảm liều 20-25%
        - Chọn phác đồ ít độc tính
        - Theo dõi sát tác dụng phụ
        - Hỗ trợ tích cực (G-CSF, EPO, dinh dưỡng)
        
        **ECOG 3:**
        - Chỉ phác đồ đơn thuốc, liều thấp
        - Hoặc best supportive care
        - Cân nhắc nguy cơ-lợi ích kỹ
        - Cần có đáp ứng tốt mới xem xét
        
        **ECOG 4:**
        - Không hóa trị
        - Best supportive care
        - Palliative/hospice care
        
        **3. Phẫu thuật:**
        
        **ECOG 0-1:**
        - Phù hợp phẫu thuật lớn
        - Nguy cơ phẫu thuật thấp
        
        **ECOG 2:**
        - Cân nhắc nguy cơ phẫu thuật cao
        - Có thể cải thiện với prehabilitation
        - Xem xét phẫu thuật nhỏ hơn
        
        **ECOG 3-4:**
        - Thường không phẫu thuật
        - Chỉ cấp cứu (tắc ruột, chảy máu)
        
        **4. Xạ trị:**
        - ECOG 0-2: Xạ trị triệt căn nếu chỉ định
        - ECOG 3-4: Chỉ xạ trị giảm nhẹ (đau xương, chèn ép, v.v.)
        
        **5. Immunotherapy:**
        - Hầu hết trials yêu cầu ECOG 0-1
        - Real-world có thể ECOG 2
        - Cẩn trọng với ECOG 3 (độc tính không đoán trước)
        - Không dùng với ECOG 4
        """)
    
    with st.expander("📈 ECOG và Tiên Lượng"):
        st.markdown("""
        ### ECOG là yếu tố tiên lượng độc lập:
        
        **Median survival theo ECOG (tổng quát):**
        - **ECOG 0:** 12+ tháng (tùy loại ung thư)
        - **ECOG 1:** 9-12 tháng
        - **ECOG 2:** 4-6 tháng
        - **ECOG 3:** 1-3 tháng
        - **ECOG 4:** < 1 tháng
        
        **Lưu ý:** Con số này rất khác nhau tùy:
        - Loại ung thư
        - Giai đoạn
        - Điều trị
        - Đáp ứng điều trị
        
        **Ví dụ cụ thể - Ung thư phổi không tế bào nhỏ giai đoạn IV:**
        - ECOG 0-1 với targeted therapy: Median OS ~20-30 tháng
        - ECOG 2: ~10-12 tháng
        - ECOG 3-4: ~2-4 tháng
        
        **Ung thư đại trực tràng di căn:**
        - ECOG 0-1 với hóa trị: Median OS ~24-30 tháng
        - ECOG 2: ~12-18 tháng
        - ECOG 3-4: ~3-6 tháng
        
        **ECOG giảm = Tiến triển bệnh:**
        - ECOG giảm từ 0→1 hoặc 1→2: Có thể tiến triển bệnh
        - Cần đánh giá lại bệnh (CT scan, v.v.)
        - Xem xét thay đổi điều trị
        """)
    
    with st.expander("🔄 Theo Dõi ECOG Trong Điều Trị"):
        st.markdown("""
        ### Tần suất đánh giá:
        
        **Trong quá trình điều trị:**
        - Mỗi chu kỳ hóa trị
        - Trước mỗi infusion
        - Khi có thay đổi lâm sàng
        
        **Ý nghĩa thay đổi ECOG:**
        
        **ECOG cải thiện:**
        - ✅ Đáp ứng điều trị tốt
        - ✅ Có thể tăng cường điều trị
        - ✅ Tiên lượng tốt hơn
        
        **ECOG ổn định:**
        - ✅ Bệnh kiểm soát
        - ✅ Tiếp tục điều trị hiện tại
        
        **ECOG giảm:**
        - ⚠️ Cảnh báo tiến triển bệnh
        - ⚠️ Tác dụng phụ điều trị
        - ⚠️ Bệnh lý kèm theo
        - Cần đánh giá ngay:
          + Imaging (CT, MRI)
          + Xét nghiệm
          + Đánh giá tác dụng phụ
          + Đánh giá bệnh kèm
        
        **Xử trí khi ECOG giảm:**
        1. Xác định nguyên nhân
        2. Điều trị nguyên nhân nếu có thể
        3. Xem xét điều chỉnh điều trị ung thư
        4. Tăng cường supportive care
        5. Nếu ECOG giảm xuống 3-4 → Cân nhắc best supportive care
        """)
    
    # References
    st.markdown("---")
    st.caption("""
    **Tài liệu tham khảo:**
    - Oken MM, et al. Toxicity and response criteria of the Eastern Cooperative Oncology Group. Am J Clin Oncol. 1982
    - Sørensen JB, et al. Performance status assessment in cancer patients. Cancer. 1993
    - Buccheri G, et al. Karnofsky and ECOG performance status scoring in lung cancer. Eur Respir J. 1996
    - Conill C, et al. Performance status assessment in cancer patients. Cancer. 1990
    """)


if __name__ == "__main__":
    render()

