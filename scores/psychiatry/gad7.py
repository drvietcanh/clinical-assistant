"""
GAD-7 - Generalized Anxiety Disorder-7
Sàng lọc và đánh giá rối loạn lo âu lan tỏa
"""

import streamlit as st


# GAD-7 questions in Vietnamese
GAD7_QUESTIONS = [
    "Cảm thấy lo lắng, bồn chồn hoặc căng thẳng",
    "Không thể ngừng lo lắng hoặc không kiểm soát được sự lo lắng",
    "Lo lắng quá nhiều về nhiều thứ khác nhau",
    "Khó thư giãn",
    "Bồn chồn đến mức khó ngồi yên",
    "Dễ khó chịu hoặc cáu kỉnh",
    "Cảm thấy sợ hãi như thể có điều gì đó tồi tệ sắp xảy ra"
]


def calculate_gad7(scores):
    """
    Calculate total GAD-7 score
    
    Args:
        scores: List of 7 scores (0-3 for each question)
    
    Returns:
        int: Total score (0-21)
    """
    return sum(scores)


def interpret_gad7(total_score):
    """
    Interpret GAD-7 score
    
    Args:
        total_score: Total GAD-7 score
    
    Returns:
        dict: Interpretation results
    """
    if total_score < 5:
        return {
            "severity": "Lo âu tối thiểu",
            "color": "🟢",
            "description": "Không có triệu chứng lo âu đáng kể",
            "recommendation": "Không cần can thiệp. Tái đánh giá khi cần thiết.",
            "monitoring": "Theo dõi thường xuyên nếu có yếu tố nguy cơ",
            "level": "minimal"
        }
    elif total_score < 10:
        return {
            "severity": "Lo âu nhẹ",
            "color": "🟡",
            "description": "Có một số triệu chứng lo âu",
            "recommendation": "Watchful waiting, hỗ trợ tâm lý. Kỹ thuật thư giãn, mindfulness.",
            "monitoring": "Tái đánh giá sau 4-6 tuần",
            "level": "mild"
        }
    elif total_score < 15:
        return {
            "severity": "Lo âu mức trung bình",
            "color": "🟠",
            "description": "Lo âu ảnh hưởng đến chức năng hàng ngày",
            "recommendation": "Xem xét điều trị: CBT hoặc thuốc (SSRI/SNRI).",
            "monitoring": "Tái đánh giá sau 2-4 tuần. Theo dõi đáp ứng điều trị.",
            "level": "moderate"
        }
    else:
        return {
            "severity": "Lo âu nặng",
            "color": "🔴",
            "description": "Lo âu nghiêm trọng, ảnh hưởng đáng kể đến cuộc sống",
            "recommendation": "Điều trị tích cực: Kết hợp CBT và thuốc. Chuyển chuyên khoa tâm thần nếu cần.",
            "monitoring": "Theo dõi sát mỗi 1-2 tuần. Đánh giá các rối loạn đồng mắc (trầm cảm, panic).",
            "level": "severe"
        }


def render():
    """Render the GAD-7 calculator"""
    
    st.title("😰 GAD-7 - Generalized Anxiety Disorder")
    st.markdown("""
    ### Sàng Lọc Rối Loạn Lo Âu Lan Tỏa
    
    **GAD-7:**
    - Công cụ sàng lọc rối loạn lo âu được validate
    - 7 câu hỏi đơn giản, nhanh chóng
    - Đánh giá triệu chứng trong 2 tuần qua
    - Sử dụng cho screening và theo dõi điều trị
    
    **Hướng dẫn:**
    - Đánh giá từng triệu chứng dựa trên tần suất xuất hiện
    - Thang điểm: 0 (Không có) → 3 (Gần như mỗi ngày)
    - Tổng điểm: 0-21
    
    **Ứng dụng:**
    - Primary care screening
    - Theo dõi đáp ứng điều trị lo âu
    - Đánh giá mức độ nặng
    """)
    
    st.markdown("---")
    
    # Instructions
    st.info("""
    **Trong 2 tuần qua**, bạn bị làm phiền bao nhiêu lần bởi các vấn đề sau?
    
    Chọn đáp án phù hợp nhất:
    - **0** = Không có
    - **1** = Vài ngày
    - **2** = Hơn nửa số ngày
    - **3** = Gần như mỗi ngày
    """)
    
    st.markdown("---")
    
    # Questions
    st.subheader("📋 Bảng Câu Hỏi")
    
    scores = []
    
    for i, question in enumerate(GAD7_QUESTIONS, 1):
        st.markdown(f"**{i}. {question}**")
        
        score = st.radio(
            "Chọn mức độ:",
            options=[0, 1, 2, 3],
            format_func=lambda x: ["0 - Không có", "1 - Vài ngày", "2 - Hơn nửa số ngày", "3 - Gần như mỗi ngày"][x],
            key=f"gad7_q{i}",
            horizontal=True
        )
        scores.append(score)
        st.markdown("---")
    
    # Calculate button
    if st.button("📊 Tính Điểm & Phân tích", type="primary", use_container_width=True):
        # Calculate total score
        total_score = calculate_gad7(scores)
        
        # Get interpretation
        result = interpret_gad7(total_score)
        
        st.markdown("---")
        st.subheader("📈 Kết quả Đánh giá")
        
        # Display total score
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.metric(
                "Tổng Điểm GAD-7",
                f"{total_score}/21",
                help="Tổng điểm từ 7 câu hỏi"
            )
        
        with col2:
            if result['level'] == "minimal":
                st.success(f"{result['color']} **{result['severity']}**")
            elif result['level'] in ["mild", "moderate"]:
                st.warning(f"{result['color']} **{result['severity']}**")
            else:
                st.error(f"{result['color']} **{result['severity']}**")
        
        st.markdown("---")
        
        # Detailed interpretation
        st.subheader("🎯 Phân tích chi tiết")
        
        st.info(f"""
        **Mức độ:** {result['severity']} (Điểm: {total_score})
        
        **Mô tả:** {result['description']}
        
        **Khuyến nghị điều trị:** {result['recommendation']}
        
        **Theo Dõi:** {result['monitoring']}
        """)
        
        # Score breakdown
        st.markdown("---")
        st.subheader("📊 Phân tích từng Câu Hỏi")
        
        symptom_labels = [
            "1. Lo lắng/căng thẳng",
            "2. Không kiểm soát lo âu",
            "3. Lo nhiều thứ",
            "4. Khó thư giãn",
            "5. Bồn chồn",
            "6. Cáu kỉnh",
            "7. Sợ hãi"
        ]
        
        for i, (label, score) in enumerate(zip(symptom_labels, scores)):
            col1, col2 = st.columns([3, 1])
            with col1:
                st.write(label)
            with col2:
                if score == 0:
                    st.write("🟢 0")
                elif score == 1:
                    st.write("🟡 1")
                elif score == 2:
                    st.write("🟠 2")
                else:
                    st.write("🔴 3")
        
        # Functional impairment
        st.markdown("---")
        st.subheader("🔍 Đánh giá Chức Năng")
        
        functional_impact = st.radio(
            "**Các vấn đề trên đã ảnh hưởng đến công việc, việc nhà, hoặc quan hệ với người khác của bạn đến mức độ nào?**",
            [
                "Không khó khăn",
                "Hơi khó khăn",
                "Rất khó khăn",
                "Cực kỳ khó khăn"
            ],
            help="Câu hỏi bổ sung đánh giá ảnh hưởng chức năng"
        )
        
        if functional_impact != "Không khó khăn":
            st.warning(f"""
            ⚠️ **Ảnh hưởng chức năng:** {functional_impact}
            
            Lo âu đang ảnh hưởng đáng kể đến cuộc sống hàng ngày.
            Can thiệp điều trị được khuyến nghị.
            """)
        
        # Comorbidity screening
        if total_score >= 10:
            st.markdown("---")
            st.subheader("🔍 Sàng Lọc Bệnh Đồng Mắc")
            
            st.warning("""
            **Lưu ý:** Rối loạn lo âu thường đi kèm với:
            - **Trầm cảm** (50-60%) - Nên làm thêm PHQ-9
            - **Rối loạn hoảng sợ (Panic Disorder)**
            - **PTSD**
            - **Rối loạn lo âu xã hội**
            - **OCD**
            
            Xem xét sàng lọc toàn diện nếu có triệu chứng khác.
            """)
    
    # Educational content
    st.markdown("---")
    st.subheader("📚 Thông tin bổ sung")
    
    with st.expander("📋 Phân Loại Mức Độ Lo Âu"):
        st.markdown("""
        ### Phân loại theo điểm GAD-7:
        
        | Điểm | Mức độ | Khuyến nghị |
        |------|--------|-------------|
        | 0-4 | Tối thiểu | Không cần can thiệp |
        | 5-9 | Nhẹ | Watchful waiting, kỹ thuật thư giãn |
        | 10-14 | Trung bình | CBT hoặc thuốc |
        | 15-21 | Nặng | CBT + thuốc, chuyên khoa |
        
        **Cutoff điểm:**
        - GAD-7 ≥ 10: Độ nhạy 89%, độ đặc hiệu 82% cho GAD
        - Cũng sàng lọc tốt cho panic disorder, social anxiety, PTSD
        """)
    
    with st.expander("💊 Lựa Chọn Điều Trị Lo Âu"):
        st.markdown("""
        ### Tâm lý trị liệu:
        
        **Cognitive Behavioral Therapy (CBT):**
        - Lựa chọn đầu tay cho GAD
        - Hiệu quả tương đương thuốc
        - Kéo dài 12-15 buổi
        - Kỹ thuật:
          + Cognitive restructuring
          + Exposure therapy
          + Relaxation training
        
        **Mindfulness-Based Stress Reduction (MBSR):**
        - Hiệu quả cho lo âu
        - 8 tuần training
        - Meditation, yoga
        
        **Kỹ thuật thư giãn:**
        - Progressive muscle relaxation
        - Deep breathing exercises
        - Guided imagery
        
        ### Thuốc:
        
        **SSRI (Lựa chọn đầu tay):**
        - **Escitalopram** 10-20 mg/ngày
        - **Sertraline** 50-200 mg/ngày
        - **Paroxetine** 20-50 mg/ngày
        - Tác dụng: 2-4 tuần
        - Điều trị: 12 tháng sau remission
        
        **SNRI:**
        - **Venlafaxine XR** 75-225 mg/ngày
        - **Duloxetine** 30-60 mg/ngày
        - Hiệu quả tương đương SSRI
        
        **Buspirone:**
        - 15-60 mg/ngày (chia 2-3 lần)
        - Không gây nghiện
        - Chậm tác dụng (2-4 tuần)
        
        **Benzodiazepines (Ngắn hạn):**
        - ⚠️ Chỉ dùng cấp cứu, ngắn hạn (< 2-4 tuần)
        - Nguy cơ nghiện, lệ thuộc
        - Lorazepam 0.5-2 mg khi cần
        - Alprazolam 0.25-0.5 mg khi cần
        
        **Pregabalin:**
        - 150-600 mg/ngày
        - Hiệu quả nhanh hơn SSRI
        - Nguy cơ nghiện ở người có tiền sử
        
        **Hydroxyzine:**
        - 25-100 mg khi cần
        - Không nghiện
        - Gây buồn ngủ
        
        ### Lựa chọn theo mức độ:
        
        **Lo âu nhẹ (5-9):**
        - Thử watchful waiting 4-6 tuần
        - Kỹ thuật thư giãn, exercise
        - CBT nếu bệnh nhân muốn
        
        **Lo âu trung bình (10-14):**
        - CBT (lựa chọn đầu)
        - Hoặc SSRI/SNRI
        - Xem xét preference bệnh nhân
        
        **Lo âu nặng (15-21):**
        - Kết hợp CBT + thuốc
        - Theo dõi sát
        - Chuyên khoa tâm thần
        """)
    
    with st.expander("🔄 Theo Dõi Điều Trị"):
        st.markdown("""
        ### Lịch tái đánh giá GAD-7:
        
        **Giai đoạn cấp (4-8 tuần):**
        - Mỗi 2 tuần
        - Đánh giá đáp ứng
        - Tác dụng phụ
        - Tăng liều nếu cần
        
        **Giai đoạn duy trì:**
        - Mỗi 1-2 tháng
        - GAD-7 định kỳ
        - Điều chỉnh điều trị
        
        **Đáp ứng điều trị:**
        - **Response:** Giảm ≥ 50% điểm GAD-7
        - **Remission:** GAD-7 < 5
        - **Mục Tiêu:** Remission hoàn toàn
        
        **Khi dừng thuốc:**
        - Sau remission ≥ 12 tháng
        - Giảm liều từ từ 4-8 tuần
        - Theo dõi tái phát
        """)
    
    with st.expander("🎯 Chẩn Đoán Phân Biệt"):
        st.markdown("""
        ### GAD-7 sàng lọc tốt cho:
        
        **1. Generalized Anxiety Disorder (GAD):**
        - Lo âu lan tỏa về nhiều vấn đề
        - Khó kiểm soát
        - ≥ 6 tháng
        
        **2. Panic Disorder:**
        - Cơn hoảng sợ tái phát
        - Lo sợ cơn hoảng sợ tiếp theo
        - Tránh né tình huống
        
        **3. Social Anxiety Disorder:**
        - Sợ bị đánh giá
        - Tránh tình huống xã hội
        - Lo âu dự đoán
        
        **4. PTSD:**
        - Tiền sử chấn thương
        - Flashbacks, nightmares
        - Hypervigilance
        
        **5. OCD:**
        - Obsessions (ám ảnh)
        - Compulsions (hành vi cưỡng chế)
        - Lo âu khi không thực hiện ritual
        
        ### Các tình trạng y khoa gây lo âu:
        - **Tim mạch:** Rối loạn nhịp, ACS, pheochromocytoma
        - **Hô hấp:** Asthma, COPD
        - **Nội tiết:** Hyperthyroidism, hypoglycemia
        - **Thần kinh:** TIA, vestibular disorders
        - **Thuốc:** Caffeine, stimulants, corticosteroids
        - **Cai chất:** Alcohol, benzodiazepines
        """)
    
    with st.expander("💡 Kỹ Thuật Tự Quản Lý Lo Âu"):
        st.markdown("""
        ### Kỹ thuật hô hấp:
        
        **Box Breathing (4-4-4-4):**
        1. Hít vào 4 giây
        2. Giữ 4 giây
        3. Thở ra 4 giây
        4. Giữ 4 giây
        5. Lặp lại 5-10 chu kỳ
        
        **Diaphragmatic Breathing:**
        - Thở bằng bụng, không phải ngực
        - Hít vào qua mũi
        - Thở ra qua miệng (chậm hơn)
        - 10-15 phút mỗi ngày
        
        ### Progressive Muscle Relaxation:
        1. Tìm nơi yên tĩnh
        2. Căng nhóm cơ 5-10 giây
        3. Thả lỏng hoàn toàn 20 giây
        4. Lần lượt: bàn chân → chân → đùi → bụng → tay → vai → mặt
        5. Tổng thời gian: 15-20 phút
        
        ### Grounding Technique (5-4-3-2-1):
        Khi lo âu cấp, nhận biết:
        - **5** thứ bạn nhìn thấy
        - **4** thứ bạn chạm được
        - **3** thứ bạn nghe thấy
        - **2** thứ bạn ngửi được
        - **1** thứ bạn nếm được
        
        ### Lối sống:
        - **Exercise:** 30 phút × 5 ngày/tuần
        - **Giấc ngủ:** 7-9 giờ/đêm
        - **Hạn chế caffeine:** < 400 mg/ngày
        - **Tránh alcohol** (có thể làm tăng lo âu)
        - **Mindfulness:** 10-20 phút/ngày
        - **Social support:** Duy trì kết nối
        """)
    
    with st.expander("🔗 GAD-7 + PHQ-9"):
        st.markdown("""
        ### Sàng lọc đồng thời lo âu và trầm cảm:
        
        **Lý do:**
        - 50-60% bệnh nhân GAD có trầm cảm đồng mắc
        - 60% bệnh nhân trầm cảm có lo âu
        - Điều trị có thể khác nhau
        
        **Patterns thường gặp:**
        
        **1. GAD cao + PHQ-9 thấp:**
        - Lo âu đơn thuần
        - CBT + SSRI/SNRI
        - Kỹ thuật thư giãn
        
        **2. GAD thấp + PHQ-9 cao:**
        - Trầm cảm đơn thuần
        - CBT + SSRI
        - Behavioral activation
        
        **3. Cả hai cao:**
        - Mixed anxiety-depression
        - Cần điều trị tích cực
        - SSRI/SNRI + CBT
        - Theo dõi sát
        
        **4. Cả hai thấp:**
        - Có thể không phải rối loạn tâm thần
        - Xem xét nguyên nhân y khoa
        - Stress tình huống?
        
        **Ưu tiên điều trị:**
        - Nếu có ý tưởng tự tử → Ưu tiên trầm cảm
        - Nếu panic attacks → Ưu tiên lo âu
        - Nếu tương đương → Điều trị cả hai
        """)
    
    # References
    st.markdown("---")
    st.caption("""
    **Tài liệu tham khảo:**
    - Spitzer RL, et al. A brief measure for assessing generalized anxiety disorder: the GAD-7. Arch Intern Med. 2006
    - Kroenke K, et al. Anxiety disorders in primary care. Ann Intern Med. 2007
    - Bandelow B, et al. Efficacy of treatments for anxiety disorders. Int Clin Psychopharmacol. 2015
    - NICE Guidelines: Generalised anxiety disorder and panic disorder in adults. 2019
    """)


if __name__ == "__main__":
    render()

