"""
Epworth Sleepiness Scale (ESS)
Đánh giá mức độ buồn ngủ ban ngày
"""

import streamlit as st


def calculate_epworth(scores):
    """
    Calculate Epworth Sleepiness Scale score
    
    Args:
        scores: List of 8 situation scores (0-3 each)
    
    Returns:
        int: Total ESS score (0-24)
    """
    return sum(scores)


def interpret_epworth(total_score):
    """
    Interpret Epworth Sleepiness Scale score
    
    Args:
        total_score: Total ESS score
    
    Returns:
        dict: Interpretation results
    """
    if total_score <= 5:
        return {
            "level": "Bình thường thấp",
            "color": "🟢",
            "description": "Mức độ buồn ngủ ban ngày trong giới hạn bình thường thấp",
            "recommendation": "Không có dấu hiệu buồn ngủ quá mức ban ngày",
            "action": "Không cần can thiệp",
            "osa_risk": "Nguy cơ thấp OSA",
            "severity": "normal_low"
        }
    elif total_score <= 10:
        return {
            "level": "Bình thường cao",
            "color": "🟡",
            "description": "Mức độ buồn ngủ ban ngày trong giới hạn bình thường cao",
            "recommendation": "Theo dõi. Đánh giá vệ sinh giấc ngủ.",
            "action": "Cải thiện thói quen ngủ. Tái đánh giá nếu có triệu chứng.",
            "osa_risk": "Nguy cơ trung bình OSA",
            "severity": "normal_high"
        }
    elif total_score <= 15:
        return {
            "level": "Buồn ngủ vừa phải",
            "color": "🟠",
            "description": "Buồn ngủ ban ngày mức độ vừa phải - cần đánh giá thêm",
            "recommendation": "Xem xét nguyên nhân. Sàng lọc rối loạn giấc ngủ (OSA, narcolepsy).",
            "action": "Đánh giá tiền sử chi tiết. Xem xét nghiên cứu giấc ngủ (polysomnography) nếu có yếu tố nguy cơ OSA.",
            "osa_risk": "Nguy cơ cao OSA",
            "severity": "moderate"
        }
    else:  # > 15
        return {
            "level": "Buồn ngủ nặng",
            "color": "🔴",
            "description": "Buồn ngủ ban ngày mức độ nặng - BẤT THƯỜNG",
            "recommendation": "CẦN đánh giá chuyên khoa. Nghi ngờ cao rối loạn giấc ngủ.",
            "action": "Chuyển chuyên khoa giấc ngủ/ENT. Polysomnography. Đánh giá OSA, narcolepsy, và các rối loạn giấc ngủ khác.",
            "osa_risk": "Nguy cơ rất cao OSA",
            "severity": "severe"
        }


def get_osa_screening_questions():
    """Get additional OSA screening questions (STOP-BANG components)"""
    return {
        "questions": [
            "Ngáy to có người khác nghe thấy?",
            "Thường cảm thấy mệt/buồn ngủ ban ngày?",
            "Có ai thấy bạn ngừng thở khi ngủ?",
            "Có tăng huyết áp?"
        ],
        "high_risk_factors": [
            "BMI > 35",
            "Tuổi > 50",
            "Vòng cổ to (Nam > 43 cm, Nữ > 41 cm)",
            "Nam giới"
        ]
    }


# ESS Situations in Vietnamese
ESS_SITUATIONS = [
    {
        "situation": "Ngồi đọc sách",
        "description": "Đọc sách, báo, tài liệu"
    },
    {
        "situation": "Xem TV",
        "description": "Xem tivi, phim"
    },
    {
        "situation": "Ngồi yên tại nơi công cộng",
        "description": "Ví dụ: rạp hát, cuộc họp, hội nghị"
    },
    {
        "situation": "Ngồi trên xe > 1 giờ (không lái)",
        "description": "Là hành khách trên xe ô tô, xe bus"
    },
    {
        "situation": "Nằm nghỉ buổi chiều",
        "description": "Khi hoàn cảnh cho phép nghỉ ngơi"
    },
    {
        "situation": "Ngồi nói chuyện với người khác",
        "description": "Trò chuyện, trao đổi bình thường"
    },
    {
        "situation": "Ngồi yên sau bữa trưa (không uống rượu)",
        "description": "Sau bữa trưa, không có uống đồ có cồn"
    },
    {
        "situation": "Ngồi trong xe khi dừng vài phút do tắc đường",
        "description": "Đang lái xe, dừng đèn đỏ hoặc kẹt xe"
    }
]


def render():
    """Render the Epworth Sleepiness Scale calculator"""
    
    st.title("😴 Epworth Sleepiness Scale")
    st.markdown("""
    ### Đánh Giá Mức Độ Buồn Ngủ Ban Ngày
    
    **Epworth Sleepiness Scale (ESS):**
    - Bảng câu hỏi tự đánh giá buồn ngủ ban ngày
    - 8 tình huống thường ngày
    - Điểm từ 0-24
    - Công cụ sàng lọc rối loạn giấc ngủ (đặc biệt OSA)
    
    **Ứng dụng:**
    - Sàng lọc Obstructive Sleep Apnea (OSA)
    - Đánh giá narcolepsy
    - Theo dõi điều trị rối loạn giấc ngủ
    - Đánh giá an toàn lái xe
    
    **Thang điểm:**
    - 0-5: Bình thường thấp
    - 6-10: Bình thường cao
    - 11-15: Buồn ngủ vừa phải
    - 16-24: Buồn ngủ nặng (bất thường)
    
    **Lưu ý:**
    - ESS > 10: Cần đánh giá rối loạn giấc ngủ
    - ESS > 15: Nguy cơ cao OSA
    - Không thay thế polysomnography
    - Chủ quan (self-report)
    """)
    
    st.markdown("---")
    
    # Instructions
    st.info("""
    **Hướng dẫn:**
    
    Với mỗi tình huống bên dưới, hãy cho biết **khả năng bạn sẽ ngủ gật hoặc ngủ** (không chỉ cảm thấy mệt):
    
    - **0 = Không bao giờ** ngủ gật
    - **1 = Ít khi** ngủ gật
    - **2 = Vừa phải** có khả năng ngủ gật
    - **3 = Rất có khả năng** ngủ gật
    
    Nếu bạn không làm một số hoạt động gần đây, hãy tưởng tượng nó sẽ ảnh hưởng đến bạn như thế nào.
    """)
    
    st.markdown("---")
    
    # ESS Questions
    st.subheader("📋 8 Tình Huống Đánh giá")
    
    scores = []
    
    for i, item in enumerate(ESS_SITUATIONS, 1):
        st.markdown(f"### {i}. {item['situation']}")
        st.caption(item['description'])
        
        score = st.radio(
            "Khả năng ngủ gật:",
            options=[0, 1, 2, 3],
            format_func=lambda x: [
                "0 - Không bao giờ",
                "1 - Ít khi",
                "2 - Vừa phải",
                "3 - Rất có khả năng"
            ][x],
            key=f"ess_q{i}",
            horizontal=True
        )
        scores.append(score)
        
        st.markdown("---")
    
    # Calculate button
    if st.button("📊 Tính Điểm ESS", type="primary", use_container_width=True):
        # Calculate total
        total_score = calculate_epworth(scores)
        
        # Get interpretation
        result = interpret_epworth(total_score)
        
        st.markdown("---")
        st.subheader("📈 Kết quả Đánh giá")
        
        # Display score
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric(
                "Điểm ESS",
                f"{total_score}/24",
                help="Tổng điểm Epworth Sleepiness Scale"
            )
        
        with col2:
            if result['severity'] in ["normal_low", "normal_high"]:
                st.success(f"{result['color']} {result['level']}")
            elif result['severity'] == "moderate":
                st.warning(f"{result['color']} {result['level']}")
            else:
                st.error(f"{result['color']} {result['level']}")
        
        st.markdown("---")
        
        # Score breakdown
        st.subheader("📊 Phân tích từng Tình Huống")
        
        for i, (item, score) in enumerate(zip(ESS_SITUATIONS, scores), 1):
            col1, col2 = st.columns([4, 1])
            with col1:
                st.write(f"{i}. {item['situation']}")
            with col2:
                if score == 0:
                    st.write("🟢 0")
                elif score == 1:
                    st.write("🟡 1")
                elif score == 2:
                    st.write("🟠 2")
                else:
                    st.write("🔴 3")
        
        st.markdown("---")
        
        # Interpretation
        st.subheader("🎯 Phân tích & Khuyến nghị")
        
        if result['severity'] in ["normal_low", "normal_high"]:
            st.success(f"""
            ### {result['color']} {result['level']}
            
            **Điểm ESS: {total_score}/24**
            
            **Đánh giá:** {result['description']}
            
            **Khuyến nghị:** {result['recommendation']}
            
            **Xử trí:** {result['action']}
            """)
            
            if result['severity'] == "normal_high":
                st.info("""
                **Lưu ý với điểm 6-10:**
                - Vẫn trong giới hạn bình thường
                - Cải thiện vệ sinh giấc ngủ có thể có lợi
                - Tái đánh giá nếu có triệu chứng khác (ngáy, ngừng thở khi ngủ)
                """)
                
        else:
            st.warning(f"""
            ### {result['color']} {result['level']}
            
            **Điểm ESS: {total_score}/24** - BẤT THƯỜNG
            
            **Đánh giá:** {result['description']}
            
            **Nguy cơ OSA:** {result['osa_risk']}
            
            **Khuyến nghị:** {result['recommendation']}
            
            **Xử trí:** {result['action']}
            """)
            
            # Additional OSA screening
            st.markdown("---")
            st.subheader("🔍 Sàng Lọc Bổ Sung - Nguy Cơ OSA")
            
            osa_questions = get_osa_screening_questions()
            
            st.markdown("**Các câu hỏi bổ sung (STOP-BANG components):**")
            for q in osa_questions['questions']:
                st.markdown(f"- {q}")
            
            st.markdown("**Yếu tố nguy cơ cao:**")
            for f in osa_questions['high_risk_factors']:
                st.markdown(f"- {f}")
            
            st.info("""
            **Nếu có ≥ 3 câu trả lời "Có":**
            - Nguy cơ cao OSA
            - Khuyến cáo polysomnography (nghiên cứu giấc ngủ)
            - Chuyển chuyên khoa giấc ngủ/ENT
            """)
            
            st.markdown("---")
            st.error("""
            ### ⚠️ Cảnh Báo An Toàn
            
            **Với ESS > 10, đặc biệt > 15:**
            - **Nguy cơ tai nạn lái xe tăng 2-3 lần**
            - Cân nhắc hạn chế lái xe đường dài
            - Không lái xe khi buồn ngủ
            - Cần đánh giá và điều trị trước khi lái xe chuyên nghiệp
            
            **Các nghề nghiệp nguy hiểm:**
            - Lái xe (taxi, bus, xe tải)
            - Vận hành máy móc nặng
            - Công việc cao (xây dựng)
            - Cần đánh giá fit-to-work
            """)
    
    # Educational content
    st.markdown("---")
    st.subheader("📚 Thông tin bổ sung")
    
    with st.expander("😴 Về Obstructive Sleep Apnea (OSA)"):
        st.markdown("""
        ### OSA - Ngưng thở khi ngủ do tắc nghẽn:
        
        **Định nghĩa:**
        - Tắc nghẽn đường thở trên lặp lại khi ngủ
        - → Giảm/ngừng thở → Giảm oxy máu → Thức giấc
        - → Phân mảnh giấc ngủ → Buồn ngủ ban ngày
        
        **Triệu chứng:**
        
        **Ban đêm:**
        - Ngáy to, không đều
        - Ngừng thở (người khác chứng kiến)
        - Thức giấc nghẹt thở, thở hổn hển
        - Đi tiểu nhiều lần
        - Ra mồ hôi đêm
        - Khô miệng khi thức dậy
        
        **Ban ngày:**
        - Buồn ngủ quá mức (ESS > 10)
        - Mệt mỏi mãn tính
        - Đau đầu buổi sáng
        - Khó tập trung
        - Giảm trí nhớ
        - Thay đổi tâm trạng, cáu gắt
        
        **Yếu tố nguy cơ:**
        - Béo phì (BMI > 30)
        - Vòng cổ to (Nam > 43 cm, Nữ > 41 cm)
        - Tuổi cao
        - Nam giới (gấp 2-3 lần nữ)
        - Tăng huyết áp
        - Hút thuốc, uống rượu
        - Tắc mũi mãn tính
        - Amidan to
        - Cằm lùi (retrognathia)
        - Tiền sử gia đình
        
        **Biến Chứng:**
        - Tăng huyết áp (50-60%)
        - Bệnh tim mạch, đột quỵ
        - Rối loạn nhịp tim
        - Đái tháo đường type 2
        - Tai nạn giao thông (gấp 2-3 lần)
        - Giảm chất lượng cuộc sống
        - Tăng tử vong
        
        **Chẩn Đoán:**
        - **Polysomnography (PSG):** Gold standard
        - AHI (Apnea-Hypopnea Index):
          + < 5: Bình thường
          + 5-15: OSA nhẹ
          + 15-30: OSA trung bình
          + > 30: OSA nặng
        
        **Điều Trị:**
        - **CPAP:** Lựa chọn đầu tay
        - Giảm cân (nếu béo phì)
        - Tránh rượu, thuốc ngủ
        - Ngủ nghiêng (không ngửa)
        - Phẫu thuật (nếu có chỉ định)
        - Oral appliances
        """)
    
    with st.expander("📊 Độ Chính Xác Của ESS"):
        st.markdown("""
        ### ESS trong sàng lọc OSA:
        
        **Độ nhạy/đặc hiệu (cutoff > 10):**
        - Độ nhạy: 40-60% (không cao lắm)
        - Độ đặc hiệu: 60-80%
        - → ESS KHÔNG thay thế PSG
        
        **Ý nghĩa:**
        - ESS > 10: Cần đánh giá thêm (PSG)
        - ESS ≤ 10: KHÔNG loại trừ OSA
        - Nhiều OSA vẫn có ESS bình thường
        
        **Giá trị:**
        - Sàng lọc ban đầu
        - Đánh giá mức độ buồn ngủ chủ quan
        - Theo dõi điều trị (ESS giảm sau CPAP)
        - Đơn giản, nhanh, miễn phí
        
        **Hạn chế:**
        - Chủ quan (self-report)
        - Người già thường underreport
        - Một số người "quen" với buồn ngủ
        - Không đánh giá chất lượng giấc ngủ
        - Không phân biệt OSA vs rối loạn khác
        
        **Nên kết hợp:**
        - STOP-BANG questionnaire
        - Berlin Questionnaire
        - Đánh giá lâm sàng
        - Oximetry đêm (screening)
        - PSG (chẩn đoán xác định)
        """)
    
    with st.expander("💤 Cải Thiện Vệ Sinh Giấc Ngủ"):
        st.markdown("""
        ### Sleep Hygiene - Thói quen ngủ tốt:
        
        **1. Thời gian ngủ:**
        - Ngủ và thức đều giờ (kể cả cuối tuần)
        - Đủ 7-9 giờ/đêm
        - Tránh ngủ trưa quá lâu (< 30 phút)
        
        **2. Môi trường:**
        - Tối, yên tĩnh, mát (18-20°C)
        - Giường chỉ để ngủ (không làm việc, xem TV)
        - Nệm và gối thoải mái
        
        **3. Trước khi ngủ:**
        - Không caffeine sau 2h chiều
        - Không rượu trước ngủ 3-4h
        - Không bữa ăn nặng trước ngủ 2-3h
        - Không tập thể dục nặng trước ngủ 3-4h
        - Tắt điện thoại, máy tính 1h trước ngủ
        
        **4. Thói quen thư giãn:**
        - Đọc sách (không sách điện tử)
        - Nghe nhạc nhẹ nhàng
        - Meditation, yoga nhẹ
        - Tắm nước ấm
        
        **5. Nếu không ngủ được:**
        - Không nằm trằn trọc > 20 phút
        - Dậy, đi ra phòng khác
        - Làm việc nhẹ nhàng, thư giãn
        - Quay lại giường khi buồn ngủ
        
        **6. Tránh:**
        - Xem đồng hồ liên tục
        - Lo lắng về việc không ngủ được
        - Uống nhiều nước trước ngủ (đi tiểu đêm)
        - Sử dụng điện thoại trên giường
        """)
    
    with st.expander("🚗 An Toàn Lái Xe"):
        st.markdown("""
        ### ESS và an toàn lái xe:
        
        **Nghiên cứu:**
        - ESS > 10: Nguy cơ tai nạn xe tăng 2-3 lần
        - ESS > 15: Nguy cơ tăng 4-7 lần
        - Tương đương với BAC 0.05-0.08%
        
        **Khuyến cáo:**
        
        **ESS 0-10:**
        - Lái xe bình thường
        - Chú ý dấu hiệu buồn ngủ khi lái
        
        **ESS 11-15:**
        - Cẩn trọng khi lái xe đường dài
        - Nghỉ mỗi 2h
        - Không lái xe khi mệt
        - Xem xét đánh giá rối loạn giấc ngủ
        
        **ESS > 15:**
        - Hạn chế lái xe
        - KHÔNG lái xe chuyên nghiệp cho đến khi điều trị
        - Cần đánh giá và điều trị OSA
        - Tái đánh giá sau điều trị
        
        **Lái xe chuyên nghiệp:**
        - Lái taxi, bus, xe tải
        - Cần ESS ≤ 10 (một số nơi)
        - Nếu OSA: Cần điều trị CPAP tuân thủ
        - Tái đánh giá định kỳ
        
        **Dấu hiệu cảnh báo khi lái:**
        - Chớp mắt liên tục
        - Không nhớ vài km vừa lái
        - Lái chệch làn
        - Ngáp liên tục
        - → Dừng xe, nghỉ ngay!
        """)
    
    with st.expander("🔬 Các Công Cụ Sàng Lọc Khác"):
        st.markdown("""
        ### So sánh các questionnaires:
        
        **Epworth Sleepiness Scale (ESS):**
        - 8 câu hỏi
        - Đánh giá buồn ngủ ban ngày
        - Đơn giản, nhanh
        - Không đặc hiệu cho OSA
        
        **STOP-BANG:**
        - 8 câu hỏi Yes/No
        - Dành riêng cho OSA
        - Độ nhạy cao (90%)
        - ≥ 3/8: Nguy cơ cao OSA
        - Components: Snoring, Tired, Observed apnea, Pressure (BP), BMI, Age, Neck, Gender
        
        **Berlin Questionnaire:**
        - 10 câu hỏi, 3 nhóm
        - Sàng lọc OSA
        - ≥ 2 nhóm high-risk: Nguy cơ cao OSA
        
        **NoSAS Score:**
        - 5 components
        - Nhanh hơn STOP-BANG
        - Score ≥ 8: Nguy cơ cao OSA
        
        **Khuyến cáo sử dụng:**
        - ESS: Đánh giá buồn ngủ ban ngày
        - STOP-BANG: Sàng lọc OSA (độ nhạy cao)
        - Kết hợp: ESS > 10 + STOP-BANG ≥ 3 → Rất khuyến cáo PSG
        """)
    
    # References
    st.markdown("---")
    st.caption("""
    **Tài liệu tham khảo:**
    - Johns MW. A new method for measuring daytime sleepiness: the Epworth sleepiness scale. Sleep. 1991;14(6):540-545
    - Johns MW. Reliability and factor analysis of the Epworth Sleepiness Scale. Sleep. 1992;15(4):376-381
    - Kapur VK, et al. Clinical Practice Guideline for Diagnostic Testing for Adult OSA. JCSM. 2017
    - Chung F, et al. STOP-BANG Questionnaire: A practical approach to screen for OSA. Chest. 2016
    """)


if __name__ == "__main__":
    render()

