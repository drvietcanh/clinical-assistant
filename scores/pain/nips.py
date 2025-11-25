"""
NIPS - Neonatal Infant Pain Scale
Thang điểm đánh giá đau ở trẻ sơ sinh (0-2 tháng)
"""

import streamlit as st


def render():
    """NIPS Pain Scale Calculator"""
    st.markdown("""
    <h2 style='text-align: center; color: #0EA5E9;'>👶 NIPS - Neonatal Infant Pain Scale</h2>
    <p style='text-align: center;'><em>Thang điểm đánh giá đau ở trẻ sơ sinh (0-2 tháng)</em></p>
    """, unsafe_allow_html=True)
    
    with st.expander("ℹ️ Giới thiệu"):
        st.markdown("""
        **NIPS (Neonatal Infant Pain Scale)** là thang điểm quan sát hành vi để đánh giá đau ở trẻ sơ sinh.
        
        **Chỉ định:**
        - Trẻ sơ sinh 0-2 tháng tuổi
        - Trẻ non tháng và đủ tháng
        - Sau thủ thuật, chấn thương, phẫu thuật
        
        **6 Tiêu chí (mỗi tiêu chí 0-1 điểm):**
        1. **Facial Expression (Biểu hiện khuôn mặt)**
        2. **Cry (Khóc)**
        3. **Breathing Patterns (Kiểu thở)**
        4. **Arms (Tay)**
        5. **Legs (Chân)**
        6. **State of Arousal (Trạng thái tỉnh táo)**
        
        **Tổng điểm: 0-7**
        """)
    
    st.markdown("---")
    
    st.subheader("📝 Đánh Giá Đau")
    
    # Facial Expression
    st.markdown("### 1️⃣ Facial Expression (Biểu hiện khuôn mặt)")
    facial_score = st.radio(
        "Biểu hiện khuôn mặt:",
        [
            "0 - Khuôn mặt thư giãn, bình thường",
            "1 - Nhăn mặt, cau mày, nếp nhăn trên trán"
        ],
        key="nips_facial"
    )
    facial = int(facial_score[0])
    
    # Cry
    st.markdown("### 2️⃣ Cry (Khóc)")
    cry_score = st.radio(
        "Khóc:",
        [
            "0 - Không khóc, yên lặng",
            "1 - Khóc nhẹ, rên rỉ, hoặc khóc to"
        ],
        key="nips_cry"
    )
    cry = int(cry_score[0])
    
    # Breathing Patterns
    st.markdown("### 3️⃣ Breathing Patterns (Kiểu thở)")
    breathing_score = st.radio(
        "Kiểu thở:",
        [
            "0 - Thở đều, bình thường",
            "1 - Thở không đều, nhanh, nín thở > 5 giây"
        ],
        key="nips_breathing"
    )
    breathing = int(breathing_score[0])
    
    # Arms
    st.markdown("### 4️⃣ Arms (Tay)")
    arms_score = st.radio(
        "Vị trí và cử động tay:",
        [
            "0 - Thư giãn, cử động bình thường",
            "1 - Căng thẳng, co rút, duỗi thẳng"
        ],
        key="nips_arms"
    )
    arms = int(arms_score[0])
    
    # Legs
    st.markdown("### 5️⃣ Legs (Chân)")
    legs_score = st.radio(
        "Vị trí và cử động chân:",
        [
            "0 - Thư giãn, cử động bình thường",
            "1 - Căng thẳng, co rút, duỗi thẳng"
        ],
        key="nips_legs"
    )
    legs = int(legs_score[0])
    
    # State of Arousal
    st.markdown("### 6️⃣ State of Arousal (Trạng thái tỉnh táo)")
    arousal_score = st.radio(
        "Trạng thái tỉnh táo:",
        [
            "0 - Ngủ yên hoặc tỉnh táo, bình tĩnh",
            "1 - Không yên, kích động, quấy khóc"
        ],
        key="nips_arousal"
    )
    arousal = int(arousal_score[0])
    
    st.markdown("---")
    
    if st.button("📊 Tính Điểm NIPS", type="primary", use_container_width=True):
        total_score = facial + cry + breathing + arms + legs + arousal
        
        st.markdown("## 📊 Kết Quả")
        
        # Interpret score
        if total_score == 0:
            severity = "Không đau"
            color = "#10b981"
            icon = "✅"
            interpretation = "Trẻ sơ sinh không có dấu hiệu đau"
        elif total_score <= 2:
            severity = "Đau nhẹ"
            color = "#fbbf24"
            icon = "😐"
            interpretation = "Đau nhẹ, cần theo dõi"
        elif total_score <= 4:
            severity = "Đau vừa"
            color = "#f59e0b"
            icon = "😣"
            interpretation = "Đau vừa, cần điều trị giảm đau"
        else:
            severity = "Đau nặng"
            color = "#ef4444"
            icon = "😰"
            interpretation = "Đau nặng, cần điều trị ngay lập tức"
        
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, {color}22 0%, {color}44 100%); 
                    padding: 30px; border-radius: 15px; border-left: 5px solid {color}; margin: 20px 0;'>
            <h2 style='color: {color}; margin: 0; text-align: center;'>
                {icon} NIPS = {total_score}/7
            </h2>
            <p style='text-align: center; font-size: 1.1em; margin-top: 10px;'>
                {severity}
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Breakdown
        st.markdown("### 📋 Chi Tiết Điểm Số:")
        st.markdown(f"""
        - **Facial Expression (Khuôn mặt):** {facial}/1
        - **Cry (Khóc):** {cry}/1
        - **Breathing Patterns (Thở):** {breathing}/1
        - **Arms (Tay):** {arms}/1
        - **Legs (Chân):** {legs}/1
        - **State of Arousal (Tỉnh táo):** {arousal}/1
        
        **Tổng:** {total_score}/7
        """)
        
        st.markdown(f"**Diễn giải:** {interpretation}")
        
        # Treatment recommendations
        st.markdown("---")
        st.markdown("### 💊 Khuyến Nghị Điều Trị")
        
        if total_score == 0:
            st.success("**✅ Không cần điều trị giảm đau**")
        elif total_score <= 2:
            st.info("""
            **💊 Đau nhẹ (NIPS 1-2):**
            
            **Điều trị:**
            - **Non-pharmacological:**
              - Ôm ấp, da kề da
              - Cho bú, ngậm núm vú
              - Quấn tã, tạo môi trường yên tĩnh
            - **Pharmacological (nếu cần):**
              - Paracetamol: 10-15 mg/kg mỗi 4-6 giờ (max 60 mg/kg/ngày)
            
            **Theo dõi:**
            - Đánh giá lại sau 30-60 phút
            - Mục tiêu: NIPS ≤ 2
            """)
        elif total_score <= 4:
            st.warning("""
            **💊 Đau vừa (NIPS 3-4):**
            
            **Điều trị:**
            - **Non-pharmacological:** (như trên)
            - **Pharmacological:**
              - Paracetamol: 15 mg/kg mỗi 4-6 giờ
              - Cân nhắc Morphine: 0.05 mg/kg IV mỗi 4-6 giờ (nếu đau do thủ thuật/phẫu thuật)
            
            **Theo dõi:**
            - Đánh giá lại sau 30 phút
            - Mục tiêu: NIPS ≤ 2
            """)
        else:
            st.error("""
            **🚨 Đau nặng (NIPS 5-7):**
            
            **Điều trị khẩn:**
            - **Non-pharmacological:** (như trên)
            - **Pharmacological:**
              - **Morphine IV:** 0.05-0.1 mg/kg mỗi 2-4 giờ
              - Hoặc **Fentanyl IV:** 1-2 µg/kg bolus, sau đó 0.5-1 µg/kg/h
              - Kết hợp Paracetamol
            
            **Theo dõi:**
            - Đánh giá lại sau 15-30 phút
            - Mục tiêu: NIPS ≤ 2 trong vòng 1 giờ
            - Theo dõi tác dụng phụ: ức chế hô hấp, bú kém
            
            **Cảnh báo:**
            - Đau nặng ở trẻ sơ sinh cần điều trị ngay lập tức
            - Cân nhắc nguyên nhân đau (nhiễm trùng, chấn thương, thiếu máu...)
            - Trẻ sơ sinh dễ bị ức chế hô hấp với opioid → theo dõi sát
            """)
        
        with st.expander("📚 Hướng Dẫn Sử Dụng"):
            st.markdown("""
            ### 🎯 Cách Đánh Giá:
            
            1. **Quan sát trẻ trong 1-2 phút:**
               - Không làm trẻ chú ý
               - Quan sát khi trẻ nghỉ ngơi và khi có kích thích (nếu có)
            
            2. **Đánh giá từng tiêu chí:**
               - Chọn mức độ phù hợp nhất cho mỗi tiêu chí
               - Dựa trên quan sát hành vi, không phải hỏi trẻ
            
            3. **Tính tổng điểm:**
               - Cộng điểm của 6 tiêu chí
               - Tổng điểm: 0-7
            
            ### 📋 Khi Nào Đánh Giá:
            - Khi trẻ vào viện
            - Trước và sau thủ thuật (chích, lấy máu, đặt catheter...)
            - Trước và sau điều trị giảm đau
            - Mỗi 2-4 giờ ở trẻ nội trú
            - Sau phẫu thuật: Mỗi 1-2 giờ trong 24 giờ đầu
            - Khi có dấu hiệu đau (khóc, không yên, nhăn mặt...)
            
            ### ⚠️ Lưu Ý:
            - NIPS dùng cho trẻ sơ sinh 0-2 tháng tuổi
            - Trẻ > 2 tháng: Dùng FLACC
            - Đánh giá khi trẻ tỉnh táo (không ngủ sâu)
            - Cân nhắc các yếu tố khác: đói, lạnh, ướt tã, bệnh lý nền
            - Trẻ non tháng có thể có biểu hiện đau khác (thay đổi SpO2, nhịp tim...)
            """)
        
        with st.expander("📚 Tài Liệu Tham Khảo"):
            st.markdown("""
            1. **Lawrence J, Alcock D, McGrath P, Kay J, MacMurray SB, Dulberg C.** The development of a tool to assess neonatal pain. 
               *Neonatal Netw.* 1993;12(6):59-66.
            
            2. **Nguyễn Đăng Bảo Minh.** Đánh giá độ tin cậy và giá trị của thang điểm đau NIPS ở trẻ sơ sinh. 
               *Tạp chí Y học Việt Nam.* 2018.
            """)
    
    st.info("""
    💡 **Điểm quan trọng:**
    
    1. **NIPS 0:** Không đau
    2. **NIPS 1-2:** Đau nhẹ → Non-pharmacological + Paracetamol
    3. **NIPS 3-4:** Đau vừa → Paracetamol + cân nhắc Morphine
    4. **NIPS 5-7:** Đau nặng → Opioid mạnh ngay lập tức
    5. **Mục tiêu:** NIPS ≤ 2
    6. **Đánh giá lại:** Sau 15-30 phút (đau nặng) hoặc 30-60 phút (đau nhẹ/vừa)
    7. **Cảnh báo:** Trẻ sơ sinh dễ bị ức chế hô hấp với opioid → theo dõi sát
    """)

