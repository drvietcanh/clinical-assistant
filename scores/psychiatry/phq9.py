"""
PHQ-9 - Patient Health Questionnaire-9
Sàng lọc và đánh giá mức độ trầm cảm
"""

import streamlit as st


# PHQ-9 questions in Vietnamese
PHQ9_QUESTIONS = [
    "Ít quan tâm hoặc ít thích thú làm việc",
    "Cảm thấy buồn, chán nản hoặc tuyệt vọng",
    "Khó ngủ, ngủ không say giấc hoặc ngủ quá nhiều",
    "Cảm thấy mệt mỏi hoặc không có năng lượng",
    "Ít thèm ăn hoặc ăn quá nhiều",
    "Cảm thấy tồi tệ về bản thân - hoặc cảm thấy mình là người thất bại hoặc đã làm gia đình hay chính bản thân thất vọng",
    "Khó tập trung vào việc gì đó, chẳng hạn như đọc báo hoặc xem TV",
    "Di chuyển hoặc nói chuyện chậm chạp đến mức người khác có thể nhận ra. Hoặc ngược lại - bồn chồn hoặc không yên đến mức di chuyển nhiều hơn bình thường",
    "Nghĩ rằng tốt hơn là chết đi hoặc tự làm hại bản thân theo một cách nào đó"
]


def calculate_phq9(scores):
    """
    Calculate total PHQ-9 score
    
    Args:
        scores: List of 9 scores (0-3 for each question)
    
    Returns:
        int: Total score (0-27)
    """
    return sum(scores)


def interpret_phq9(total_score):
    """
    Interpret PHQ-9 score
    
    Args:
        total_score: Total PHQ-9 score
    
    Returns:
        dict: Interpretation results
    """
    if total_score < 5:
        return {
            "severity": "Không có / Tối thiểu",
            "color": "🟢",
            "description": "Không có triệu chứng trầm cảm đáng kể",
            "recommendation": "Không cần can thiệp. Tái đánh giá khi cần thiết.",
            "monitoring": "Theo dõi thường xuyên nếu có yếu tố nguy cơ",
            "level": "none"
        }
    elif total_score < 10:
        return {
            "severity": "Trầm cảm nhẹ",
            "color": "🟡",
            "description": "Có một số triệu chứng trầm cảm",
            "recommendation": "Hỗ trợ, watchful waiting. Giáo dục bệnh nhân, vệ sinh giấc ngủ, tập thể dục.",
            "monitoring": "Tái đánh giá sau 4-6 tuần. Xem xét can thiệp nếu không cải thiện.",
            "level": "mild"
        }
    elif total_score < 15:
        return {
            "severity": "Trầm cảm mức trung bình",
            "color": "🟠",
            "description": "Trầm cảm ảnh hưởng đến chức năng hàng ngày",
            "recommendation": "Xem xét điều trị: Tâm lý trị liệu (CBT) hoặc thuốc chống trầm cảm (SSRI).",
            "monitoring": "Tái đánh giá sau 2-4 tuần. Theo dõi sát đáp ứng điều trị.",
            "level": "moderate"
        }
    elif total_score < 20:
        return {
            "severity": "Trầm cảm mức trung bình nặng",
            "color": "🟠",
            "description": "Trầm cảm ảnh hưởng nghiêm trọng đến chức năng",
            "recommendation": "Điều trị tích cực: Kết hợp tâm lý trị liệu VÀ thuốc chống trầm cảm.",
            "monitoring": "Theo dõi sát, tái đánh giá mỗi 1-2 tuần. Cân nhắc hội chẩn tâm thần.",
            "level": "moderate_severe"
        }
    else:
        return {
            "severity": "Trầm cảm nặng",
            "color": "🔴",
            "description": "Trầm cảm rất nặng, có thể cần can thiệp khẩn cấp",
            "recommendation": "Điều trị tích cực: Thuốc + Tâm lý trị liệu. Chuyển tới chuyên khoa tâm thần. Xem xét nhập viện nếu có ý tưởng tự tử.",
            "monitoring": "Theo dõi rất sát (hàng tuần). Đánh giá nguy cơ tự tử. Liên lạc với chuyên khoa tâm thần.",
            "level": "severe"
        }


def assess_suicide_risk(question_9_score):
    """
    Assess suicide risk based on question 9
    
    Args:
        question_9_score: Score for question 9 (0-3)
    
    Returns:
        dict: Suicide risk assessment
    """
    if question_9_score == 0:
        return {
            "risk": "Không có",
            "color": "🟢",
            "action": "Không cần can thiệp đặc biệt về vấn đề này"
        }
    elif question_9_score == 1:
        return {
            "risk": "Có ý nghĩ (vài ngày)",
            "color": "🟡",
            "action": "Đánh giá thêm. Hỏi về kế hoạch, phương tiện. Tăng cường hỗ trợ."
        }
    elif question_9_score == 2:
        return {
            "risk": "Có ý nghĩ (hơn nửa số ngày)",
            "color": "🟠",
            "action": "Đánh giá chi tiết nguy cơ tự tử. Xem xét an toàn. Hội chẩn tâm thần khẩn."
        }
    else:  # score == 3
        return {
            "risk": "Có ý nghĩ (gần như mỗi ngày)",
            "color": "🔴",
            "action": "CẤP CỨU: Đánh giá ngay nguy cơ tự tử. Không để bệnh nhân một mình. Chuyển tới cơ sở tâm thần hoặc cấp cứu."
        }


def render():
    """Render the PHQ-9 calculator"""
    
    st.title("🧠 PHQ-9 - Patient Health Questionnaire")
    st.markdown("""
    ### Sàng Lọc & Đánh Giá Trầm Cảm
    
    **PHQ-9:**
    - Công cụ sàng lọc trầm cảm được validate rộng rãi
    - 9 câu hỏi dựa trên tiêu chí DSM-5
    - Đánh giá triệu chứng trong 2 tuần qua
    - Sử dụng cho screening, chẩn đoán, và theo dõi điều trị
    
    **Hướng dẫn:**
    - Đánh giá từng triệu chứng dựa trên tần suất xuất hiện
    - Thang điểm: 0 (Không có) → 3 (Gần như mỗi ngày)
    - Tổng điểm: 0-27
    
    **Ứng dụng:**
    - Primary care screening
    - Theo dõi đáp ứng điều trị
    - Điều chỉnh liều thuốc
    - Đánh giá tái phát
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
    
    for i, question in enumerate(PHQ9_QUESTIONS, 1):
        st.markdown(f"**{i}. {question}**")
        
        score = st.radio(
            "Chọn mức độ:",
            options=[0, 1, 2, 3],
            format_func=lambda x: ["0 - Không có", "1 - Vài ngày", "2 - Hơn nửa số ngày", "3 - Gần như mỗi ngày"][x],
            key=f"phq9_q{i}",
            horizontal=True
        )
        scores.append(score)
        
        # Special warning for question 9 (suicide)
        if i == 9 and score > 0:
            st.warning("⚠️ **Quan trọng:** Có ý nghĩ tự tử - cần đánh giá ngay!")
        
        st.markdown("---")
    
    # Calculate button
    if st.button("📊 Tính Điểm & Phân Tích", type="primary", use_container_width=True):
        # Calculate total score
        total_score = calculate_phq9(scores)
        
        # Get interpretation
        result = interpret_phq9(total_score)
        
        # Get suicide risk
        suicide_risk = assess_suicide_risk(scores[8])  # Question 9
        
        st.markdown("---")
        st.subheader("📈 Kết Quả Đánh Giá")
        
        # Display total score
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.metric(
                "Tổng Điểm PHQ-9",
                f"{total_score}/27",
                help="Tổng điểm từ 9 câu hỏi"
            )
        
        with col2:
            if result['level'] == "none":
                st.success(f"{result['color']} **{result['severity']}**")
            elif result['level'] in ["mild", "moderate"]:
                st.warning(f"{result['color']} **{result['severity']}**")
            else:
                st.error(f"{result['color']} **{result['severity']}**")
        
        st.markdown("---")
        
        # Detailed interpretation
        st.subheader("🎯 Phân Tích Chi Tiết")
        
        st.info(f"""
        **Mức độ:** {result['severity']} (Điểm: {total_score})
        
        **Mô tả:** {result['description']}
        
        **Khuyến nghị điều trị:** {result['recommendation']}
        
        **Theo dõi:** {result['monitoring']}
        """)
        
        # Suicide risk assessment
        if scores[8] > 0:
            st.markdown("---")
            st.subheader("⚠️ Đánh Giá Nguy Cơ Tự Tử")
            
            if suicide_risk['color'] == "🔴":
                st.error(f"""
                {suicide_risk['color']} **Nguy cơ: {suicide_risk['risk']}**
                
                **Hành động:** {suicide_risk['action']}
                
                **Đánh giá bổ sung:**
                - Có kế hoạch cụ thể không?
                - Có phương tiện không?
                - Tiền sử tự tử trước đây?
                - Có hỗ trợ xã hội không?
                - Có sử dụng chất kích thích không?
                
                **Liên hệ ngay:**
                - Đường dây nóng tâm lý: 1900 0115
                - Cấp cứu: 115
                - Chuyển khoa tâm thần khẩn cấp
                """)
            else:
                st.warning(f"""
                {suicide_risk['color']} **Nguy cơ: {suicide_risk['risk']}**
                
                **Hành động:** {suicide_risk['action']}
                """)
        
        # Score breakdown
        st.markdown("---")
        st.subheader("📊 Phân Tích Từng Câu Hỏi")
        
        # Create a chart
        symptom_labels = [
            "1. Mất hứng thú",
            "2. Buồn/chán nản",
            "3. Rối loạn giấc ngủ",
            "4. Mệt mỏi",
            "5. Thay đổi ăn uống",
            "6. Cảm giác tội lỗi",
            "7. Khó tập trung",
            "8. Chậm chạp/bồn chồn",
            "9. Ý nghĩ tự tử"
        ]
        
        for i, (label, score) in enumerate(zip(symptom_labels, scores)):
            col1, col2 = st.columns([3, 1])
            with col1:
                st.write(label)
            with col2:
                bar_length = score * 25  # 25% per point
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
        st.subheader("🔍 Đánh Giá Chức Năng")
        
        functional_impact = st.radio(
            "**Các vấn đề trên đã ảnh hưởng đến công việc, việc nhà, hoặc quan hệ với người khác của bạn đến mức độ nào?**",
            [
                "Không khó khăn",
                "Hơi khó khăn",
                "Rất khó khăn",
                "Cực kỳ khó khăn"
            ],
            help="Câu hỏi bổ sung đánh giá ảnh hưởng chức năng (không tính điểm)"
        )
        
        if functional_impact != "Không khó khăn":
            st.warning(f"""
            ⚠️ **Ảnh hưởng chức năng:** {functional_impact}
            
            Điều này cho thấy các triệu chứng trầm cảm đang ảnh hưởng đáng kể đến cuộc sống hàng ngày.
            Can thiệp điều trị được khuyến nghị mạnh mẽ hơn.
            """)
    
    # Educational content
    st.markdown("---")
    st.subheader("📚 Thông Tin Bổ Sung")
    
    with st.expander("📋 Phân Loại Mức Độ Trầm Cảm"):
        st.markdown("""
        ### Phân loại theo điểm PHQ-9:
        
        | Điểm | Mức độ | Khuyến nghị |
        |------|--------|-------------|
        | 0-4 | Không có / Tối thiểu | Không cần can thiệp |
        | 5-9 | Nhẹ | Hỗ trợ, watchful waiting |
        | 10-14 | Trung bình | CBT hoặc thuốc |
        | 15-19 | Trung bình nặng | CBT + thuốc |
        | 20-27 | Nặng | Điều trị tích cực, chuyên khoa |
        
        **Lưu ý:**
        - PHQ-9 ≥ 10 có độ nhạy 88% và độ đặc hiệu 88% cho major depression
        - Cần đánh giá lâm sàng toàn diện, không chỉ dựa vào điểm số
        - Xem xét các chẩn đoán phân biệt (rối loạn lưỡng cực, lo âu, v.v.)
        """)
    
    with st.expander("💊 Lựa Chọn Điều Trị"):
        st.markdown("""
        ### Tâm lý trị liệu:
        
        **Cognitive Behavioral Therapy (CBT):**
        - Hiệu quả tương đương thuốc cho trầm cảm nhẹ-trung bình
        - Lựa chọn đầu tay cho trầm cảm nhẹ
        - Kéo dài 12-16 buổi
        - Tỷ lệ tái phát thấp hơn
        
        **Các phương pháp khác:**
        - Interpersonal therapy (IPT)
        - Problem-solving therapy
        - Mindfulness-based therapy
        - Behavioral activation
        
        ### Thuốc chống trầm cảm:
        
        **SSRI (Lựa chọn đầu tay):**
        - Sertraline 50-200 mg/ngày
        - Escitalopram 10-20 mg/ngày
        - Fluoxetine 20-60 mg/ngày
        - Tác dụng: 2-4 tuần
        - Điều trị: 6-12 tháng (đợt đầu), 1-2 năm (tái phát)
        
        **SNRI:**
        - Venlafaxine XR 75-225 mg/ngày
        - Duloxetine 30-60 mg/ngày
        
        **Bupropion:**
        - XL 150-300 mg/ngày
        - Tốt cho mệt mỏi, tăng cân
        - Tránh nếu co giật
        
        **Mirtazapine:**
        - 15-45 mg trước ngủ
        - Tốt cho mất ngủ, mất cân
        
        ### Phối hợp:
        - Trầm cảm trung bình nặng trở lên: CBT + thuốc
        - Hiệu quả cao hơn điều trị đơn độc
        - Giảm tỷ lệ tái phát
        
        ### Không đáp ứng:
        - Tăng liều
        - Chuyển sang SSRI khác
        - Phối hợp thuốc
        - ECT (trầm cảm nặng, không đáp ứng)
        """)
    
    with st.expander("🔄 Theo Dõi Điều Trị"):
        st.markdown("""
        ### Lịch tái đánh giá PHQ-9:
        
        **Giai đoạn cấp (4-8 tuần đầu):**
        - Mỗi 1-2 tuần
        - Đánh giá đáp ứng điều trị
        - Theo dõi tác dụng phụ
        - Đánh giá nguy cơ tự tử
        
        **Giai đoạn duy trì:**
        - Mỗi 1-2 tháng
        - Đánh giá triệu chứng còn sót
        - Điều chỉnh điều trị nếu cần
        
        **Đáp ứng điều trị:**
        - **Response:** Giảm ≥ 50% điểm PHQ-9
        - **Remission:** PHQ-9 < 5
        - **Mục tiêu:** Remission hoàn toàn
        
        **Khi dừng thuốc:**
        - Chỉ sau remission ≥ 6-12 tháng
        - Giảm liều dần trong 4-6 tuần
        - Theo dõi sát triệu chứng tái phát
        - PHQ-9 định kỳ mỗi tháng × 3 tháng
        """)
    
    with st.expander("⚠️ Đánh Giá Nguy Cơ Tự Tử Chi Tiết"):
        st.markdown("""
        ### Yếu tố nguy cơ cao:
        
        **Yếu tố nguy cơ chính:**
        - Có kế hoạch tự tử cụ thể
        - Có phương tiện (thuốc, vũ khí)
        - Tiền sử tự tử trước đây
        - Nam giới, tuổi cao
        - Sống một mình, cô lập
        - Lạm dụng chất
        - Bệnh cơ thể mãn tính
        - Mất mát gần đây
        
        **Câu hỏi sàng lọc:**
        1. "Bạn có nghĩ rằng cuộc sống không đáng sống không?"
        2. "Bạn có nghĩ về cái chết hoặc chết đi không?"
        3. "Bạn có nghĩ về việc tự làm hại bản thân không?"
        4. "Bạn có kế hoạch cụ thể không?"
        5. "Bạn có phương tiện thực hiện không?"
        6. "Bạn có ý định thực hiện không?"
        
        **Đánh giá chi tiết nếu (+):**
        - **I**deation: Ý tưởng
        - **P**lan: Kế hoạch
        - **M**eans: Phương tiện
        - **I**ntent: Ý định
        
        **Can thiệp:**
        - Nguy cơ thấp: Theo dõi sát, tăng hỗ trợ
        - Nguy cơ trung bình: Hội chẩn tâm thần khẩn
        - Nguy cơ cao: Nhập viện tâm thần
        - Nguy cơ cấp tính: Cấp cứu ngay
        
        **An toàn môi trường:**
        - Loại bỏ phương tiện tự tử
        - Không để bệnh nhân một mình
        - Thông báo gia đình
        - Lập kế hoạch an toàn (safety plan)
        """)
    
    with st.expander("🎯 PHQ-9 vs Công Cụ Khác"):
        st.markdown("""
        ### So sánh với các công cụ sàng lọc khác:
        
        **PHQ-9:**
        - ✅ Ngắn gọn (9 câu)
        - ✅ Dễ tính điểm
        - ✅ Dựa trên DSM-5
        - ✅ Đánh giá mức độ nặng
        - ✅ Theo dõi điều trị
        - ❌ Không đánh giá lo âu
        
        **PHQ-2 (Siêu ngắn):**
        - Chỉ 2 câu (câu 1 + 2 của PHQ-9)
        - Screening nhanh
        - Nếu (+) → Làm PHQ-9 đầy đủ
        
        **GAD-7 (Lo âu):**
        - 7 câu đánh giá lo âu
        - Thường làm cùng PHQ-9
        - Nhiều BN có cả trầm cảm + lo âu
        
        **BDI-II (Beck Depression Inventory):**
        - 21 câu hỏi
        - Dài hơn, chi tiết hơn
        - Ít dùng trong primary care
        
        **MADRS (Montgomery-Åsberg):**
        - Đánh giá bởi clinician
        - Dùng trong nghiên cứu
        - Nhạy cảm với thay đổi
        
        **HAM-D (Hamilton Depression Scale):**
        - Đánh giá bởi clinician
        - 17-21 items
        - Gold standard trong nghiên cứu
        - Mất thời gian
        """)
    
    # References
    st.markdown("---")
    st.caption("""
    **Tài liệu tham khảo:**
    - Kroenke K, et al. The PHQ-9: validity of a brief depression severity measure. J Gen Intern Med. 2001
    - Spitzer RL, et al. Validation and utility of a self-report version of PRIME-MD. JAMA. 1999
    - American Psychiatric Association. DSM-5 Diagnostic Criteria for Major Depressive Disorder. 2013
    - NICE Guidelines: Depression in adults: treatment and management. 2022
    """)


if __name__ == "__main__":
    render()

