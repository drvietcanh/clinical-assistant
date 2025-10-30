"""
Centor Score (Modified Centor / McIsaac Score)
Đánh giá viêm họng do liên cầu khuẩn nhóm A (Streptococcus pyogenes)
"""

import streamlit as st


def calculate_centor(fever, exudate, nodes, no_cough, age):
    """
    Calculate Modified Centor (McIsaac) Score
    
    Args:
        fever: Fever > 38°C (0-1)
        exudate: Tonsillar exudate (0-1)
        nodes: Tender anterior cervical lymphadenopathy (0-1)
        no_cough: Absence of cough (0-1)
        age: Age in years for age modifier
    
    Returns:
        int: Total Centor score (-1 to 5)
    """
    score = fever + exudate + nodes + no_cough
    
    # Age modifier (McIsaac modification)
    if age < 15:
        score += 1
    elif age >= 45:
        score -= 1
    
    return score


def interpret_centor(score):
    """
    Interpret Centor score
    
    Args:
        score: Centor score (-1 to 5)
    
    Returns:
        dict: Interpretation results
    """
    if score <= 0:
        return {
            "risk": "Rất thấp",
            "color": "🟢",
            "probability": "< 2.5%",
            "recommendation": "KHÔNG cần test hoặc kháng sinh",
            "action": "Điều trị triệu chứng (giảm đau, hạ sốt). Theo dõi tại nhà.",
            "testing": "Không test",
            "antibiotics": "Không kháng sinh",
            "level": "very_low"
        }
    elif score == 1:
        return {
            "risk": "Thấp",
            "color": "🟡",
            "probability": "5-10%",
            "recommendation": "KHÔNG cần test hoặc kháng sinh (trừ dịch tễ đặc biệt)",
            "action": "Điều trị triệu chứng. Tái khám nếu không đỡ sau 3-5 ngày.",
            "testing": "Không test thường quy",
            "antibiotics": "Không kháng sinh",
            "level": "low"
        }
    elif score == 2:
        return {
            "risk": "Trung bình",
            "color": "🟠",
            "probability": "10-17%",
            "recommendation": "XEM XÉT test (Rapid Antigen hoặc throat culture)",
            "action": "Test nếu có sẵn. Điều trị dựa trên kết quả test. Nếu không test → Triệu chứng + theo dõi.",
            "testing": "Rapid Antigen Test (RADT) hoặc throat culture",
            "antibiotics": "Kháng sinh CHỈ nếu test dương tính",
            "level": "moderate"
        }
    elif score == 3:
        return {
            "risk": "Trung bình-cao",
            "color": "🟠",
            "probability": "28-35%",
            "recommendation": "NÊN test (Rapid Antigen hoặc throat culture)",
            "action": "Test để xác định. Kháng sinh nếu test (+). Nếu không test → Xem xét điều trị kinh nghiệm.",
            "testing": "Khuyến cáo test (RADT hoặc culture)",
            "antibiotics": "Kháng sinh nếu test (+) hoặc xem xét empiric",
            "level": "moderate_high"
        }
    else:  # score >= 4
        return {
            "risk": "Cao",
            "color": "🔴",
            "probability": "51-53%",
            "recommendation": "Test hoặc điều trị kinh nghiệm",
            "action": "Test nhanh (RADT). Nếu (+) → Kháng sinh. Nếu (-) → Throat culture xác nhận. HOẶC điều trị kinh nghiệm nếu không test được.",
            "testing": "RADT + culture nếu (-)",
            "antibiotics": "Xem xét điều trị kinh nghiệm (đặc biệt nếu không test)",
            "level": "high"
        }


def get_antibiotic_regimen():
    """Get antibiotic treatment regimens for strep pharyngitis"""
    return {
        "first_line": {
            "name": "Penicillin / Amoxicillin",
            "regimens": [
                "**Penicillin V:** 500 mg PO 2-3 lần/ngày × 10 ngày",
                "**Amoxicillin:** 500 mg PO 2 lần/ngày × 10 ngày (hoặc 1000 mg 1 lần/ngày)",
                "**Benzathine Penicillin G:** 1.2 triệu units IM × 1 lần (tuân thủ 100%, tiện cho người khó uống thuốc)"
            ],
            "notes": "Lựa chọn đầu tay. Chi phí thấp, hiệu quả cao, phổ hẹp (không làm rối loạn vi sinh vật)."
        },
        "allergy": {
            "name": "Dị ứng Penicillin (không nặng)",
            "regimens": [
                "**Cephalexin:** 500 mg PO 2 lần/ngày × 10 ngày",
                "**Cefadroxil:** 1 g PO 1 lần/ngày × 10 ngày",
                "**Azithromycin:** 500 mg ngày 1, sau đó 250 mg ngày 2-5 (5 ngày)",
                "**Clarithromycin:** 250 mg PO 2 lần/ngày × 10 ngày"
            ],
            "notes": "Cephalosporin: < 1% cross-reactivity với penicillin. Macrolides: Kháng thuốc tăng (10-15%), nên dùng nếu thật sự dị ứng penicillin."
        },
        "severe_allergy": {
            "name": "Dị ứng Penicillin nặng (anaphylaxis)",
            "regimens": [
                "**Azithromycin:** 500 mg ngày 1, sau đó 250 mg ngày 2-5",
                "**Clarithromycin:** 250 mg PO 2 lần/ngày × 10 ngày",
                "**Clindamycin:** 300 mg PO 3 lần/ngày × 10 ngày"
            ],
            "notes": "TRÁNH cephalosporin. Macrolides/Clindamycin là lựa chọn."
        }
    }


def render():
    """Render the Centor Score calculator"""
    
    st.title("🦠 Centor Score (Modified)")
    st.markdown("""
    ### Đánh Giá Viêm Họng Do Liên Cầu Khuẩn
    
    **Centor Score / Modified Centor (McIsaac Score):**
    - Công cụ lâm sàng dự đoán viêm họng do Streptococcus pyogenes (GAS)
    - Giúp quyết định: Test? Kháng sinh?
    - Tránh lạm dụng kháng sinh không cần thiết
    
    **4 tiêu chí Centor gốc (1981):**
    1. Sốt > 38°C
    2. Có mủ/bạch sấu amidan
    3. Hạch cổ trước to, đau
    4. Không ho
    
    **Modified Centor (McIsaac, 1998):** + Điều chỉnh theo tuổi
    - < 15 tuổi: +1 điểm
    - 15-44 tuổi: 0 điểm
    - ≥ 45 tuổi: -1 điểm
    
    **Điểm: -1 đến 5**
    
    **Lưu ý:**
    - Centor giúp GIẢM test/kháng sinh không cần thiết
    - Không thay thế clinical judgment
    - Test (RADT/culture) vẫn là gold standard
    """)
    
    st.markdown("---")
    
    # Input section
    st.subheader("📋 Đánh Giá Lâm Sàng")
    
    # Age
    age = st.number_input(
        "**Tuổi (năm)**",
        min_value=1,
        max_value=120,
        value=25,
        step=1,
        help="Tuổi của bệnh nhân"
    )
    
    st.markdown("---")
    
    # Clinical features
    st.markdown("### 🌡️ Các Triệu Chứng Lâm Sàng")
    
    fever = st.checkbox(
        "**Sốt > 38°C (100.4°F)**",
        help="Nhiệt độ đo được > 38°C hoặc tiền sử sốt trong 24h qua"
    )
    
    exudate = st.checkbox(
        "**Có mủ hoặc bạch sấu (exudate) trên amidan**",
        help="Màng trắng hoặc mủ bám trên amidan khi khám họng"
    )
    
    nodes = st.checkbox(
        "**Hạch cổ trước to và đau**",
        help="Anterior cervical lymphadenopathy (hạch có thể sờ thấy và đau khi ấn)"
    )
    
    no_cough = st.checkbox(
        "**Không ho**",
        help="Không có triệu chứng ho (GAS ít gây ho, virus thường có ho)"
    )
    
    st.markdown("---")
    
    # Calculate button
    if st.button("📊 Tính Centor Score", type="primary", use_container_width=True):
        # Convert checkboxes to int
        fever_score = 1 if fever else 0
        exudate_score = 1 if exudate else 0
        nodes_score = 1 if nodes else 0
        no_cough_score = 1 if no_cough else 0
        
        # Calculate score
        total_score = calculate_centor(fever_score, exudate_score, nodes_score, no_cough_score, age)
        
        # Get interpretation
        result = interpret_centor(total_score)
        
        st.markdown("---")
        st.subheader("📈 Kết Quả Đánh Giá")
        
        # Display scores
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric(
                "Centor Score",
                total_score,
                help="Điểm từ -1 đến 5"
            )
        
        with col2:
            st.metric(
                "Xác suất GAS",
                result['probability'],
                help="Khả năng viêm họng do Streptococcus pyogenes"
            )
        
        with col3:
            if result['level'] in ["very_low", "low"]:
                st.success(f"{result['color']} {result['risk']}")
            elif result['level'] in ["moderate", "moderate_high"]:
                st.warning(f"{result['color']} {result['risk']}")
            else:
                st.error(f"{result['color']} {result['risk']}")
        
        st.markdown("---")
        
        # Score breakdown
        st.subheader("📊 Chi Tiết Điểm Số")
        
        components = [
            ("🌡️ Sốt > 38°C", fever_score),
            ("🔴 Mủ/bạch sấu amidan", exudate_score),
            ("🔵 Hạch cổ trước to, đau", nodes_score),
            ("❌ Không ho", no_cough_score),
        ]
        
        # Age modifier
        if age < 15:
            age_modifier = 1
            age_text = f"👶 Tuổi < 15 ({age} tuổi): +1 điểm"
        elif age >= 45:
            age_modifier = -1
            age_text = f"👴 Tuổi ≥ 45 ({age} tuổi): -1 điểm"
        else:
            age_modifier = 0
            age_text = f"🧑 Tuổi 15-44 ({age} tuổi): 0 điểm"
        
        for label, score in components:
            col1, col2 = st.columns([3, 1])
            with col1:
                st.write(label)
            with col2:
                if score == 1:
                    st.write("✅ +1")
                else:
                    st.write("⬜ 0")
        
        st.markdown(age_text)
        
        st.markdown("---")
        
        # Recommendations
        st.subheader("🎯 Khuyến Nghị Xử Trí")
        
        if result['level'] in ["very_low", "low"]:
            st.success(f"""
            ### ✅ Nguy Cơ {result['risk']} - {result['probability']}
            
            **Xác suất viêm họng do GAS: {result['probability']}**
            
            **Khuyến nghị:** {result['recommendation']}
            
            **Xử trí:** {result['action']}
            
            ---
            
            **💊 Điều trị triệu chứng:**
            - Giảm đau/hạ sốt: Paracetamol hoặc Ibuprofen
            - Súc miệng nước muối ấm
            - Uống nhiều nước
            - Nghỉ ngơi
            
            **📝 Tư vấn:**
            - Viêm họng thường do virus → Tự khỏi 3-7 ngày
            - Tái khám nếu: Sốt cao kéo dài, khó nuốt nặng, khó thở
            """)
            
        elif result['level'] in ["moderate", "moderate_high"]:
            st.warning(f"""
            ### ⚠️ Nguy Cơ {result['risk']} - {result['probability']}
            
            **Xác suất viêm họng do GAS: {result['probability']}**
            
            **Khuyến nghị:** {result['recommendation']}
            
            **Test:** {result['testing']}
            
            **Kháng sinh:** {result['antibiotics']}
            
            **Xử trí:** {result['action']}
            """)
            
            st.info("""
            ### 🧪 Phương Pháp Test:
            
            **1. Rapid Antigen Detection Test (RADT):**
            - Kết quả: 5-10 phút
            - Độ nhạy: 70-90%
            - Độ đặc hiệu: 95-99%
            - Nếu (+) → Điều trị
            - Nếu (-) → Xem xét throat culture ở trẻ em
            
            **2. Throat Culture:**
            - Gold standard
            - Kết quả: 24-48 giờ
            - Độ nhạy: 90-95%
            - Chỉ định: RADT (-) ở trẻ em/thanh thiếu niên
            
            **Điều trị triệu chứng trong khi chờ kết quả test**
            """)
            
        else:  # high risk
            st.error(f"""
            ### 🚨 Nguy Cơ {result['risk']} - {result['probability']}
            
            **Xác suất viêm họng do GAS: {result['probability']}**
            
            **Khuyến nghị:** {result['recommendation']}
            
            **Test:** {result['testing']}
            
            **Kháng sinh:** {result['antibiotics']}
            
            **Xử trí:** {result['action']}
            """)
            
            st.warning("""
            ### ⚠️ Lưu Ý Quan Trọng:
            
            **Với điểm ≥ 4, xác suất GAS > 50%:**
            - Test nhanh (RADT) nếu có sẵn
            - Nếu không test → Xem xét điều trị kinh nghiệm
            - Đặc biệt nếu:
              + Tiền sử sốt thấp khớp
              + Tiếp xúc với GAS pharyngitis
              + Dịch tễ GAS cao trong cộng đồng
            """)
        
        # Antibiotic regimens if indicated
        if result['level'] in ["moderate_high", "high"] or (result['level'] == "moderate" and total_score >= 2):
            st.markdown("---")
            st.subheader("💊 Phác Đồ Kháng Sinh (Nếu Chỉ Định)")
            
            regimens = get_antibiotic_regimen()
            
            # First-line
            with st.expander("✅ Lựa Chọn Đầu Tay (Không Dị Ứng)", expanded=True):
                st.markdown(f"### {regimens['first_line']['name']}")
                for reg in regimens['first_line']['regimens']:
                    st.markdown(f"- {reg}")
                st.info(f"**Lưu ý:** {regimens['first_line']['notes']}")
            
            # Allergy
            with st.expander("⚠️ Dị Ứng Penicillin (Không Nặng)"):
                st.markdown(f"### {regimens['allergy']['name']}")
                for reg in regimens['allergy']['regimens']:
                    st.markdown(f"- {reg}")
                st.info(f"**Lưu ý:** {regimens['allergy']['notes']}")
            
            # Severe allergy
            with st.expander("🚨 Dị Ứng Penicillin Nặng"):
                st.markdown(f"### {regimens['severe_allergy']['name']}")
                for reg in regimens['severe_allergy']['regimens']:
                    st.markdown(f"- {reg}")
                st.warning(f"**Lưu ý:** {regimens['severe_allergy']['notes']}")
            
            st.info("""
            **Điều trị đủ 10 ngày (trừ Azithromycin 5 ngày):**
            - Giảm nguy cơ sốt thấp khớp
            - Giảm lây lan
            - Giảm biến chứng hóa mủ
            
            **Triệu chứng cải thiện trong 2-3 ngày:**
            - Nếu không đỡ → Tái đánh giá (có thể không phải GAS hoặc có biến chứng)
            """)
    
    # Educational content
    st.markdown("---")
    st.subheader("📚 Thông Tin Bổ Sung")
    
    with st.expander("🎯 Cách Sử Dụng Centor Score"):
        st.markdown("""
        ### Hướng dẫn áp dụng:
        
        **Bước 1: Đánh giá lâm sàng**
        - Khai thác triệu chứng
        - Khám họng: Amidan sưng? Có mủ?
        - Sờ hạch cổ
        - Đo nhiệt độ
        
        **Bước 2: Tính điểm Centor**
        - Áp dụng 4 tiêu chí + tuổi
        - Điểm từ -1 đến 5
        
        **Bước 3: Quyết định xử trí**
        
        **Điểm ≤ 0:**
        - Không test, không kháng sinh
        - Điều trị triệu chứng
        
        **Điểm 1:**
        - Thường không test/kháng sinh
        - Trừ dịch tễ đặc biệt
        
        **Điểm 2-3:**
        - Test (RADT hoặc culture)
        - Kháng sinh nếu (+)
        
        **Điểm ≥ 4:**
        - Test hoặc điều trị kinh nghiệm
        - Xác suất cao GAS (>50%)
        
        **Đặc biệt lưu ý:**
        - Trẻ em < 3 tuổi: GAS hiếm, thường virus
        - Người lớn: Virus thường gặp hơn
        - Dịch tễ: Mùa đông-xuân, trường học, quân đội
        """)
    
    with st.expander("🦠 Về Streptococcus pyogenes (GAS)"):
        st.markdown("""
        ### Viêm họng do liên cầu khuẩn nhóm A:
        
        **Đặc điểm:**
        - Vi khuẩn Gram (+), chuỗi
        - Lây qua đường hô hấp (giọt bắn)
        - Hay gặp nhất ở trẻ 5-15 tuổi
        - Ít gặp < 3 tuổi và người lớn
        
        **Triệu chứng:**
        - Đau họng đột ngột, nặng
        - Sốt cao (thường > 38.5°C)
        - Amidan đỏ, sưng, có mủ/bạch sấu
        - Hạch cổ to, đau
        - Đau đầu, đau bụng (đặc biệt trẻ em)
        - **KHÔNG** ho, sổ mũi (nếu có → Nghĩ virus)
        
        **Biến chứng:**
        
        **1. Hóa mủ (hiếm với kháng sinh):**
        - Áp xe quanh amidan
        - Áp xe hầu họng
        - Viêm xoang, viêm tai giữa
        - Viêm hạch cổ hóa mủ
        
        **2. Không hóa mủ (hiếm nếu điều trị):**
        - **Sốt thấp khớp (Rheumatic Fever):**
          + 2-3 tuần sau viêm họng
          + Viêm khớp, viêm cơ tim, bệnh van tim
          + Phòng: Kháng sinh đủ liều, đủ ngày
        
        - **Viêm cầu thận (PSGN):**
          + 1-2 tuần sau viêm họng
          + Phù, tăng huyết áp, suy thận
          + Kháng sinh KHÔNG phòng được PSGN
        
        - **PANDAS (hiếm):**
          + Rối loạn thần kinh tự miễn
          + OCD, tics
        
        **Điều trị giảm:**
        - Biến chứng hóa mủ
        - Sốt thấp khớp (99%)
        - Lây lan
        - Triệu chứng (giảm 1-2 ngày)
        
        **KHÔNG giảm:**
        - Viêm cầu thận (PSGN)
        """)
    
    with st.expander("⚠️ Giới Hạn Của Centor Score"):
        st.markdown("""
        ### Centor không phải là công cụ hoàn hảo:
        
        **Hạn chế:**
        
        **1. Không áp dụng cho:**
        - Trẻ < 3 tuổi (GAS hiếm, thường virus)
        - Có biểu hiện nghiêm trọng (khó thở, tiếng khò khè)
        - Nghi ngờ mononucleosis (EBV)
        - Nghi ngờ diphtheria, epiglottitis
        
        **2. Không phân biệt:**
        - GAS vs virus chính xác 100%
        - Cần test để xác định chắc chắn
        
        **3. Bị ảnh hưởng bởi:**
        - Dịch tễ địa phương (prevalence GAS)
        - Mùa (đông-xuân GAS cao hơn)
        - Tuổi (trẻ em cao hơn người lớn)
        
        **4. Không thay thế:**
        - Clinical judgment
        - Test lab nếu cần thiết
        - Đánh giá biến chứng
        
        **Tình huống đặc biệt cần test/điều trị:**
        - Tiền sử sốt thấp khớp
        - Tiền sử GAS pharyngitis tái phát
        - Tiếp xúc với case GAS
        - Dịch outbreak GAS
        - Immunocompromised
        """)
    
    with st.expander("🌍 Hướng Dẫn Quốc Tế"):
        st.markdown("""
        ### So sánh các hướng dẫn:
        
        **IDSA (Infectious Diseases Society of America) 2012:**
        - Test tất cả bệnh nhân nghi ngờ GAS (trừ rõ ràng virus)
        - RADT (+) → Điều trị
        - RADT (-) ở trẻ em → Throat culture
        - Không khuyến cáo test ở người lớn nếu RADT (-)
        
        **NICE (UK) 2018:**
        - Sử dụng FeverPAIN hoặc Centor Score
        - Điểm thấp → Không test, không kháng sinh
        - Điểm cao → Test hoặc empiric antibiotics
        - Delayed prescription option
        
        **Canadian Guidelines:**
        - Tương tự IDSA
        - Nhấn mạnh Centor để giảm test không cần thiết
        
        **Choosing Wisely:**
        - KHÔNG test/điều trị nếu rõ ràng virus
        - Centor ≤ 2 → Không test thường quy
        
        **Xu hướng:**
        - Giảm lạm dụng kháng sinh
        - Sử dụng clinical decision rules (Centor)
        - RADT point-of-care
        - Antimicrobial stewardship
        """)
    
    with st.expander("💡 Delayed Prescription Strategy"):
        st.markdown("""
        ### Chiến lược kê đơn trì hoãn:
        
        **Khái niệm:**
        - Kê đơn kháng sinh nhưng khuyên bệnh nhân chỉ dùng nếu:
          + Không đỡ sau 2-3 ngày
          + Triệu chứng nặng lên
        
        **Áp dụng khi:**
        - Centor 2-3 (nguy cơ trung bình)
        - Bệnh nhân/gia đình muốn "yên tâm" có thuốc
        - Khó tái khám (vùng xa)
        
        **Lợi ích:**
        - Giảm 40% số người dùng kháng sinh
        - Bệnh nhân hài lòng
        - Giảm kháng thuốc
        
        **Hướng dẫn:**
        ```
        "Tôi kê đơn kháng sinh cho anh/chị, nhưng chỉ dùng nếu:
        - Sau 2-3 ngày không đỡ
        - Triệu chứng nặng lên
        - Sốt cao kéo dài
        
        Hầu hết viêm họng do virus và tự khỏi 3-5 ngày.
        Hãy thử điều trị triệu chứng trước.
        
        Nếu không cần dùng kháng sinh → Rất tốt!
        Nếu cần → Bắt đầu ngay và uống đủ 10 ngày."
        ```
        
        **Điều trị triệu chứng trong khi chờ:**
        - Paracetamol/Ibuprofen
        - Súc miệng nước muối ấm
        - Uống nhiều nước
        - Nghỉ ngơi
        - Tái khám nếu nặng lên
        """)
    
    # References
    st.markdown("---")
    st.caption("""
    **Tài liệu tham khảo:**
    - Centor RM, et al. The diagnosis of strep throat in adults in the emergency room. Med Decis Making. 1981
    - McIsaac WJ, et al. Empirical validation of guidelines for the management of pharyngitis. JAMA. 2004
    - Shulman ST, et al. Clinical Practice Guideline for Strep Pharyngitis. CID. 2012 (IDSA)
    - NICE Guideline: Sore throat (acute). 2018
    """)


if __name__ == "__main__":
    render()

