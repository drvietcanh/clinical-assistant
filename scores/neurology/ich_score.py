"""
ICH Score - Intracerebral Hemorrhage Score
Predicts 30-day mortality in patients with intracerebral hemorrhage

Score Components:
1. GCS score (Glasgow Coma Scale)
2. ICH volume (≥30 cm³)
3. Intraventricular hemorrhage
4. Infratentorial origin of ICH
5. Age ≥80 years

Total score: 0-6 points
- Higher score = Higher mortality risk

Reference:
Hemphill JC 3rd, et al. The ICH score: a simple, reliable grading scale for intracerebral hemorrhage. 
Stroke. 2001;32(4):891-7.
"""

import streamlit as st


def render():
    """Render ICH Score Calculator"""
    
    st.subheader("🧠 ICH Score - Đánh Giá Xuất Huyết Nội Sọ")
    st.caption("Dự đoán tỷ lệ tử vong 30 ngày ở bệnh nhân xuất huyết não")
    
    st.markdown("""
    **ICH Score** là thang điểm đơn giản, đáng tin cậy để phân loại mức độ nghiêm trọng 
    của xuất huyết não tự phát (Intracerebral Hemorrhage).
    """)
    
    st.markdown("---")
    
    # Initialize score
    total_score = 0
    
    # Input section
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 1️⃣ Glasgow Coma Scale (GCS)")
        gcs_options = {
            "13-15 (Nhẹ)": 0,
            "5-12 (Trung bình)": 1,
            "3-4 (Nặng)": 2
        }
        gcs_selection = st.radio(
            "Điểm GCS của bệnh nhân:",
            list(gcs_options.keys()),
            help="GCS đánh giá mức độ ý thức. Điểm càng thấp = tình trạng càng nặng"
        )
        gcs_score = gcs_options[gcs_selection]
        total_score += gcs_score
        
        st.markdown("### 2️⃣ Thể Tích Máu Tụ (ICH Volume)")
        volume_options = {
            "< 30 cm³": 0,
            "≥ 30 cm³": 1
        }
        volume_selection = st.radio(
            "Thể tích xuất huyết trên CT:",
            list(volume_options.keys()),
            help="Thể tích tính theo công thức ABC/2 trên CT scan. ≥30 cm³ là dấu hiệu tiên lượng xấu"
        )
        volume_score = volume_options[volume_selection]
        total_score += volume_score
        
        st.info("""
        **💡 Công thức ABC/2:**
        - A = đường kính lớn nhất (cm)
        - B = đường kính vuông góc với A (cm)
        - C = số lát cắt có máu tụ × độ dày lát cắt (cm)
        - Thể tích ≈ (A × B × C) / 2
        """)
    
    with col2:
        st.markdown("### 3️⃣ Xuất Huyết Não Thất (IVH)")
        ivh_options = {
            "Không": 0,
            "Có": 1
        }
        ivh_selection = st.radio(
            "Có máu trong não thất?",
            list(ivh_options.keys()),
            help="Intraventricular Hemorrhage (IVH) trên CT scan"
        )
        ivh_score = ivh_options[ivh_selection]
        total_score += ivh_score
        
        st.markdown("### 4️⃣ Vị Trí Dưới Lều (Infratentorial)")
        location_options = {
            "Không (Trên lều)": 0,
            "Có (Dưới lều - Tiểu não/Thân não)": 1
        }
        location_selection = st.radio(
            "Vị trí xuất huyết:",
            list(location_options.keys()),
            help="Xuất huyết dưới lều (tiểu não, thân não) có tiên lượng xấu hơn"
        )
        location_score = location_options[location_selection]
        total_score += location_score
        
        st.markdown("### 5️⃣ Tuổi")
        age_options = {
            "< 80 tuổi": 0,
            "≥ 80 tuổi": 1
        }
        age_selection = st.radio(
            "Độ tuổi bệnh nhân:",
            list(age_options.keys()),
            help="Tuổi cao là yếu tố tiên lượng xấu"
        )
        age_score = age_options[age_selection]
        total_score += age_score
    
    # Calculate button
    st.markdown("---")
    if st.button("🧮 Tính ICH Score", type="primary", use_container_width=True):
        st.session_state.total_calculations = st.session_state.get('total_calculations', 0) + 1
        
        # Display result
        st.markdown("---")
        st.markdown("## 📊 KẾT QUẢ")
        
        # Score badge
        score_color = "green" if total_score <= 1 else "orange" if total_score <= 2 else "red"
        st.markdown(f"""
        <div style="background-color: {score_color}; padding: 20px; border-radius: 10px; text-align: center;">
            <h1 style="color: white; margin: 0;">ICH Score: {total_score}</h1>
            <p style="color: white; margin: 0; font-size: 1.2rem;">(0-6 điểm)</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Mortality prediction
        mortality_data = {
            0: {"rate": "0%", "desc": "Rất thấp", "color": "🟢"},
            1: {"rate": "13%", "desc": "Thấp", "color": "🟡"},
            2: {"rate": "26%", "desc": "Trung bình", "color": "🟠"},
            3: {"rate": "72%", "desc": "Cao", "color": "🔴"},
            4: {"rate": "97%", "desc": "Rất cao", "color": "🔴"},
            5: {"rate": "100%", "desc": "Cực cao", "color": "⚫"},
            6: {"rate": "100%", "desc": "Cực cao", "color": "⚫"}
        }
        
        mortality = mortality_data[total_score]
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Tỷ Lệ Tử Vong 30 Ngày", mortality["rate"])
        
        with col2:
            st.metric("Mức Độ Nguy Cơ", mortality["desc"])
        
        with col3:
            st.metric("Điểm Thành Phần", f"GCS:{gcs_score} Vol:{volume_score} IVH:{ivh_score} Loc:{location_score} Age:{age_score}")
        
        st.markdown("---")
        
        # Interpretation and recommendations
        st.markdown("### 📋 ĐÁNH GIÁ & KHUYẾN NGHỊ")
        
        if total_score == 0:
            st.success(f"""
            **{mortality['color']} Tiên lượng TỐT** (ICH Score = 0)
            
            **Tỷ lệ tử vong 30 ngày:** 0%
            
            **Khuyến nghị:**
            - Theo dõi sát tại khoa Thần kinh hoặc ICU
            - Kiểm soát huyết áp mục tiêu: SBP 140-160 mmHg
            - Tránh thuốc chống đông, kháng tiểu cầu trong giai đoạn cấp
            - CT scan kiểm tra sau 24h để đánh giá tiến triển
            - Bắt đầu phục hồi chức năng sớm khi ổn định
            - Tìm nguyên nhân xuất huyết (tăng huyết áp, vỡ phình mạch, dị dạng mạch máu...)
            """)
        
        elif total_score == 1:
            st.success(f"""
            **{mortality['color']} Tiên lượng TƯƠNG ĐỐI TỐT** (ICH Score = 1)
            
            **Tỷ lệ tử vong 30 ngày:** 13%
            
            **Khuyến nghị:**
            - Nhập viện ICU hoặc Stroke Unit
            - Kiểm soát huyết áp chặt chẽ: SBP 140-160 mmHg
            - Đảo ngược tác dụng kháng đông nếu bệnh nhân đang dùng
            - CT scan lặp lại 24h hoặc sớm hơn nếu có diễn biến xấu
            - Theo dõi GCS, dấu hiệu thần kinh mỗi 1-2 giờ
            - Cân nhắc tham vấn phẫu thuật thần kinh nếu có chỉ định
            - Phòng ngừa biến chứng: DVT prophylaxis, stress ulcer prophylaxis
            """)
        
        elif total_score == 2:
            st.warning(f"""
            **{mortality['color']} Tiên lượng TRUNG BÌNH** (ICH Score = 2)
            
            **Tỷ lệ tử vong 30 ngày:** 26%
            
            **Khuyến nghị:**
            - **BẮT BUỘC nhập ICU/Stroke Unit**
            - Theo dõi sát: GCS, pupils, huyết động mỗi 1 giờ
            - Kiểm soát huyết áp tích cực: SBP 140-160 mmHg (nicardipine, labetalol)
            - Đảo ngược kháng đông KHẨN CẤP nếu có (Vit K, PCC, FFP)
            - CT scan lặp lại 6-12 giờ hoặc khi có diễn biến xấu
            - **THAM VẤN PHẪU THUẬT THẦN KINH:** đánh giá chỉ định mổ
            - Cân nhắc đặt ICP monitor nếu GCS ≤8 hoặc có dấu hiệu tăng áp lực nội sọ
            - Phòng ngừa: DVT, stress ulcer, nhiễm trùng phổi
            - Kiểm soát sốt, đường huyết chặt chẽ
            """)
        
        elif total_score == 3:
            st.error(f"""
            **{mortality['color']} Tiên lượng XẤU** (ICH Score = 3)
            
            **Tỷ lệ tử vong 30 ngày:** 72%
            
            **Khuyến nghị:**
            - **KHẨN CẤP - ICU chuyên sâu**
            - Hội chẩn đa chuyên khoa: thần kinh, hồi sức, phẫu thuật thần kinh
            - Kiểm soát huyết áp: SBP 140-160 mmHg
            - Đảo ngược kháng đông NGAY LẬP TỨC
            - **THAM VẤN PHẪU THUẬT THẦN KINH KHẨN CẤP:**
              * Cân nhắc phẫu thuật giảm áp nếu có hiệu ứng chèn ép
              * Dẫn lưu não thất nếu có hydrocephalus do IVH
            - Đặt ICP monitor nếu GCS ≤8
            - Sedation, mechanical ventilation nếu cần bảo vệ đường thở
            - Kiểm soát tăng áp lực nội sọ: nâng đầu 30°, thẩm thấu liệu (mannitol/hypertonic saline)
            - Thảo luận tiên lượng với gia đình
            - Cân nhắc mức độ chăm sóc (goals of care discussion)
            """)
        
        elif total_score == 4:
            st.error(f"""
            **{mortality['color']} Tiên lượng RẤT XẤU** (ICH Score = 4)
            
            **Tỷ lệ tử vong 30 ngày:** 97%
            
            **Khuyến nghị:**
            - **TIÊN LƯỢNG RẤT XẤU - Tử vong gần như chắc chắn**
            - Hội chẩn khẩn cấp đa chuyên khoa
            - **Thảo luận nghiêm túc với gia đình về:**
              * Tiên lượng cực kỳ xấu
              * Mức độ chăm sóc (full code vs DNR/DNI)
              * Comfort care measures
            - Nếu gia đình chọn điều trị tích cực:
              * ICU chuyên sâu, hồi sức tích cực
              * Tham vấn phẫu thuật thần kinh (tỷ lệ thành công rất thấp)
              * Kiểm soát triệu chứng, giảm đau
            - Cân nhắc chăm sóc giảm nhẹ (palliative care consultation)
            - Hỗ trợ tâm lý gia đình
            """)
        
        else:  # Score 5-6
            st.error(f"""
            **{mortality['color']} Tiên lượng CỰC KỲ XẤU** (ICH Score = {total_score})
            
            **Tỷ lệ tử vong 30 ngày:** 100%
            
            **Khuyến nghị:**
            - **TIÊN LƯỢNG CỰC KỲ XẤU - Tử vong gần như chắc chắn**
            - **Thảo luận thẳng thắn với gia đình:**
              * Không có khả năng sống sót
              * Điều trị tích cực không mang lại lợi ích
              * Cân nhắc chăm sóc giảm nhẹ/comfort care
            - **Khuyến nghị mạnh mẽ:**
              * **Palliative care consultation**
              * Comfort measures only
              * Pain management, symptom control
              * Spiritual support
              * Family support
            - Tôn trọng nguyện vọng của bệnh nhân/gia đình
            - Cân nhắc hiến tạng nếu phù hợp và gia đình đồng ý
            - End-of-life care planning
            """)
        
        # Additional notes
        st.markdown("---")
        st.info("""
        **📌 LƯU Ý QUAN TRỌNG:**
        
        1. **ICH Score chỉ là công cụ tiên lượng**, không thay thế đánh giá lâm sàng toàn diện
        2. **Mỗi bệnh nhân là duy nhất** - cân nhắc các yếu tố khác:
           - Tình trạng sức khỏe trước đó
           - Tuổi sinh học vs tuổi thực
           - Ý muốn của bệnh nhân/gia đình
           - Khả năng phục hồi chức năng
        3. **Chỉ định phẫu thuật** phải được đánh giá bởi phẫu thuật thần kinh dựa trên:
           - Vị trí, kích thước máu tụ
           - Hiệu ứng chèn ép (mass effect)
           - Mức độ GCS, xu hướng tiến triển
           - Tuổi, tình trạng chung của bệnh nhân
        4. **Thảo luận goals of care** nên được thực hiện sớm với gia đình, đặc biệt khi ICH Score ≥3
        """)
        
        # Score breakdown
        with st.expander("📊 Chi Tiết Điểm Số"):
            st.markdown(f"""
            | Thành Phần | Giá Trị | Điểm |
            |------------|---------|------|
            | **GCS Score** | {gcs_selection} | {gcs_score} |
            | **ICH Volume** | {volume_selection} | {volume_score} |
            | **Xuất huyết não thất (IVH)** | {ivh_selection} | {ivh_score} |
            | **Vị trí dưới lều** | {location_selection} | {location_score} |
            | **Tuổi ≥80** | {age_selection} | {age_score} |
            | **TỔNG** | | **{total_score}** |
            """)
        
        # Mortality table
        with st.expander("📈 Bảng Tỷ Lệ Tử Vong Theo Điểm"):
            st.markdown("""
            | ICH Score | Tỷ Lệ Tử Vong 30 Ngày | Mức Độ Nguy Cơ |
            |-----------|------------------------|-----------------|
            | 0 | 0% | Rất thấp 🟢 |
            | 1 | 13% | Thấp 🟡 |
            | 2 | 26% | Trung bình 🟠 |
            | 3 | 72% | Cao 🔴 |
            | 4 | 97% | Rất cao 🔴 |
            | 5 | 100% | Cực cao ⚫ |
            | 6 | 100% | Cực cao ⚫ |
            
            **Nguồn:** Hemphill JC 3rd, et al. Stroke. 2001
            """)
        
        # References
        with st.expander("📚 Tài Liệu Tham Khảo"):
            st.markdown("""
            **Primary Reference:**
            - Hemphill JC 3rd, Bonovich DC, Besmertis L, Manley GT, Johnston SC. 
              *The ICH score: a simple, reliable grading scale for intracerebral hemorrhage.* 
              Stroke. 2001 Apr;32(4):891-7. [PMID: 11283388]
            
            **Validation Studies:**
            - Clarke JL, Johnston SC, Farrant M, Bernstein R, Tong D, Hemphill JC 3rd. 
              *External validation of the ICH score.* 
              Neurocrit Care. 2004;1(1):53-60.
            
            - Ruiz-Sandoval JL, Chiquete E, Romero-Vargas S, Padilla-Martínez JJ, González-Cornejo S. 
              *Grading scale for prediction of outcome in primary intracerebral hemorrhages.* 
              Stroke. 2007 May;38(5):1641-4.
            
            **Guidelines:**
            - Greenberg SM, et al. *2022 Guideline for the Management of Patients With Spontaneous Intracerebral Hemorrhage.* 
              Stroke. 2022;53(7):e282-e361.
            
            - Hemphill JC 3rd, et al. *Guidelines for the Management of Spontaneous Intracerebral Hemorrhage.* 
              Stroke. 2015;46(7):2032-60.
            """)
    
    # Educational content
    st.markdown("---")
    st.markdown("### 📖 THÔNG TIN THÊM")
    
    with st.expander("❓ ICH Score là gì?"):
        st.markdown("""
        **ICH Score** là thang điểm lâm sàng được phát triển để dự đoán tỷ lệ tử vong 
        30 ngày ở bệnh nhân xuất huyết não tự phát (spontaneous intracerebral hemorrhage).
        
        **Đặc điểm:**
        - Đơn giản, dễ tính toán
        - Chỉ cần thông tin từ CT scan và khám lâm sàng
        - Độ tin cậy cao, đã được validate trên nhiều dân số
        - Giúp thầy thuốc tư vấn tiên lượng cho gia đình
        - Hỗ trợ quyết định mức độ chăm sóc (level of care)
        
        **Lưu ý:** ICH Score **KHÔNG** dùng để quyết định từ chối điều trị, 
        mà chỉ là công cụ hỗ trợ thảo luận tiên lượng.
        """)
    
    with st.expander("🏥 Xử Trí Xuất Huyết Não - Nguyên Tắc Chung"):
        st.markdown("""
        **1. Hồi sức ban đầu:**
        - ABC: Đảm bảo đường thở, thở, tuần hoàn
        - Đặt nội khí quản nếu GCS ≤8 hoặc không bảo vệ được đường thở
        - Hai đường truyền tĩnh mạch cỡ lớn
        
        **2. Kiểm soát huyết áp:**
        - **Mục tiêu:** SBP 140-160 mmHg (giảm trong 1h đầu)
        - **Thuốc:** Nicardipine IV, Labetalol IV
        - **Tránh:** Giảm huyết áp quá mạnh (có thể gây thiếu máu não)
        
        **3. Đảo ngược tác dụng kháng đông:**
        - **Warfarin:** Vitamin K 10mg IV + PCC hoặc FFP
        - **Dabigatran:** Idarucizumab
        - **Rivaroxaban/Apixaban:** Andexanet alfa (nếu có) hoặc PCC
        - **Heparin:** Protamine sulfate
        
        **4. Kiểm soát tăng áp lực nội sọ:**
        - Nâng đầu giường 30°
        - Tránh tăng áp lực trong ngực (PEEP cao, gắng sức)
        - Sedation, analgesia
        - Thẩm thấu liệu: Mannitol 0.25-1 g/kg hoặc Hypertonic saline 3% 250ml
        - Cân nhắc ICP monitor nếu GCS ≤8
        
        **5. Phẫu thuật:**
        - **Chỉ định:**
          * Máu tụ tiểu não >3cm với xấu đi về thần kinh
          * Hydrocephalus do IVH (dẫn lưu não thất)
          * Máu tụ thùy >30ml, nông (<1cm từ bề mặt), xấu đi
        - **Chống chỉ định:**
          * ICH Score ≥4 (tiên lượng rất xấu)
          * GCS 3-4 với pupils giãn cố định
          * Bệnh lý nền nặng, tuổi quá cao
        
        **6. Phòng ngừa biến chứng:**
        - **DVT prophylaxis:** Pneumatic compression ngay, heparin sau 48h nếu ổn định
        - **Stress ulcer prophylaxis:** PPI hoặc H2 blocker
        - **Nhiễm trùng:** Vệ sinh răng miệng, hút đờm, VAP bundle
        - **Dinh dưỡng:** Bắt đầu sớm (ống ng hoặc đường tĩnh mạch)
        
        **7. Phục hồi chức năng:**
        - Bắt đầu sớm khi ổn định
        - Vật lý trị liệu, ngôn ngữ trị liệu
        - Đánh giá khả năng nuốt trước khi cho ăn uống
        """)
    
    with st.expander("⚠️ Hạn Chế Của ICH Score"):
        st.markdown("""
        **ICH Score có một số hạn chế:**
        
        1. **Tiên lượng tử vong, không tiên lượng chức năng**
           - Không dự đoán mức độ phục hồi chức năng ở người sống sót
           - Không đánh giá chất lượng sống sau xuất huyết
        
        2. **Không bao gồm tất cả các yếu tố tiên lượng**
           - Không tính: vị trí chính xác của máu tụ
           - Không tính: mở rộng máu tụ (hematoma expansion)
           - Không tính: bệnh lý nền (CKD, liver disease...)
        
        3. **Self-fulfilling prophecy**
           - Nguy cơ: bác sĩ có thể từ chối điều trị tích cực ở bệnh nhân điểm cao
           - Dẫn đến: tỷ lệ tử vong cao hơn không phải do bệnh mà do "withdrawal of care"
        
        4. **Cần kết hợp đánh giá lâm sàng toàn diện**
           - Không nên chỉ dựa vào điểm số để quyết định
           - Phải cân nhắc: ý muốn bệnh nhân, tình trạng trước đó, khả năng phục hồi
        
        **⚠️ QUAN TRỌNG:** ICH Score là công cụ hỗ trợ, không phải "quyết định tử hình"!
        """)
    
    # Footer
    st.markdown("---")
    st.caption("📚 Based on: Hemphill JC 3rd, et al. Stroke. 2001;32(4):891-7")
    st.caption("⚠️ For educational purposes only - Always correlate with clinical assessment")
    st.caption("🏥 Validated for spontaneous (non-traumatic) intracerebral hemorrhage")

