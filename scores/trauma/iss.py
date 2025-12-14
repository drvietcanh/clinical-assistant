"""
Injury Severity Score (ISS)
============================

Anatomical scoring system for multiple trauma

Reference:
- Baker SP, et al. The injury severity score: a method for describing patients with
  multiple injuries and evaluating emergency care. J Trauma. 1974;14(3):187-196.
- Copes WS, et al. The Injury Severity Score revisited. J Trauma. 1988;28(1):69-77.

ISS Calculation:
- Based on Abbreviated Injury Scale (AIS)
- 6 body regions assessed
- ISS = sum of squares of 3 highest AIS scores (from different regions)
- Range: 1-75 (ISS of 75 automatically given if any region has AIS 6)

Body Regions:
1. Head/Neck
2. Face
3. Chest
4. Abdomen/Pelvic Contents
5. Extremities/Pelvic Girdle
6. External

Clinical Utility:
- Mortality prediction
- Triage decisions
- Research and quality improvement
- Part of TRISS score
"""

import streamlit as st


def calculate_iss(ais_scores: dict) -> dict:
    """
    Calculate Injury Severity Score
    
    Args:
        ais_scores: Dictionary of AIS scores for each body region
        
    Returns:
        Dictionary containing ISS, mortality estimate, and recommendations
    """
    
    # Check if any AIS is 6 (unsurvivable injury)
    if 6 in ais_scores.values():
        iss = 75
        mortality = ">90%"
        risk_class = "UNSURVIVABLE"
        color = "🔴"
        interpretation = "UNSURVIVABLE INJURY (AIS 6 trong ít nhất 1 vùng)"
    else:
        # Get the three highest scores from DIFFERENT regions
        sorted_scores = sorted(ais_scores.values(), reverse=True)
        top_three = sorted_scores[:3]
        
        # Calculate ISS as sum of squares of top 3
        iss = sum(score ** 2 for score in top_three)
        
        # Estimate mortality based on ISS
        if iss >= 50:
            mortality = ">50%"
            risk_class = "CRITICAL"
            color = "🔴"
            interpretation = "CHẤNthượng CỰC NẶNG"
        elif iss >= 25:
            mortality = "20-50%"
            risk_class = "SEVERE"
            color = "🟠"
            interpretation = "CHẤN THƯƠNG NẶNG"
        elif iss >= 16:
            mortality = "5-20%"
            risk_class = "MODERATE"
            color = "🟡"
            interpretation = "CHẤN THƯƠNG TRUNG BÌNH"
        else:
            mortality = "<5%"
            risk_class = "MINOR"
            color = "🟢"
            interpretation = "CHẤN THƯƠNG NHẸ"
    
    # Management recommendations
    if risk_class == "UNSURVIVABLE" or risk_class == "CRITICAL":
        management = """
        **🔴 Xử trí- Chấn Thương Nguy Kịch:**
        
        1. **HỒI SỨC TÍCH CỰC:**
           - Activate Trauma Team NGAY
           - ABC assessment và resuscitation
           - Massive Transfusion Protocol
           - Damage Control Resuscitation
        
        2. **CHUYỂN VIỆN:**
           - Trauma Center Level I NGAY LẬP TỨC
           - Pre-notification
           - Sẵn sàng phẫu thuật cấp cứu
        
        3. **PHẪU THUẬT:**
           - Damage Control Surgery
           - Kiểm soát chảy máu
           - Kiểm soát nhiễm trùng
           - Đóng tạm thời
        
        4. **HỖ TRỢ TOÀN DIỆN:**
           - ICU monitoring
           - Ventilator support
           - Hemodynamic support
           - Renal support nếu cần
        
        5. **DỰ PHÒNG BIẾN CHỨNG:**
           - DVT prophylaxis
           - Stress ulcer prophylaxis
           - Infection control
           - Nutrition support
        """
    elif risk_class == "SEVERE":
        management = """
        **🟠 Xử trí- Chấn Thương Nặng:**
        
        1. **ĐÁnh GIÁ TOÀN DIỆN:**
           - Primary survey (ABC)
           - Secondary survey (head to toe)
           - FAST exam / CT scan
        
        2. **HỒI SỨC:**
           - IV access × 2
           - Fluid resuscitation
           - Blood products sẵn sàng
        
        3. **CHUYỂN VIỆN:**
           - Trauma Center Level I/II
           - Đội ngũ chuyên khoa đầy đủ
        
        4. **XÉT NGHIỆM:**
           - CBC, chemistry, coags
           - Type & cross
           - Imaging đầy đủ
        
        5. **THEO DÕI SÁT:**
           - Vital signs q15-30min
           - Serial exams
           - Re-assessment liên tục
        """
    elif risk_class == "MODERATE":
        management = """
        **🟡 Xử trí- Chấn Thương Trung Bình:**
        
        1. **Đánh giá:**
           - Complete trauma assessment
           - Imaging phù hợp
           - Xét nghiệm cơ bản
        
        2. **XỬ TRÍ:**
           - Điều trị các tổn thương cụ thể
           - Phẫu thuật nếu cần
           - Theo dõi chặt chẽ
        
        3. **XEM XÉT:**
           - Chuyển trauma center nếu cần
           - Tư vấn chuyên khoa
        
        4. **DỰ PHÒNG:**
           - Tetanus prophylaxis
           - Antibiotic nếu cần
           - Pain management
        """
    else:  # MINOR
        management = """
        **🟢 Xử trí - chấn thương nhẹ:**
        
        1. **Đánh giá:**
           - Khám lâm sàng kỹ
           - Imaging selective
           - Xét nghiệm theo chỉ định
        
        2. **XỬ TRÍ:**
           - Điều trị triệu chứng
           - Chăm sóc vết thương
           - Pain control
        
        3. **Theo dõi:**
           - Tái khám nếu cần
           - Hướng dẫn dấu hiệu cảnh báo
        
        4. **RA VIỆN:**
           - Có thể xuất viện nếu ổn định
           - Follow-up phù hợp
        """
    
    return {
        'iss': iss,
        'mortality': mortality,
        'risk_class': risk_class,
        'color': color,
        'interpretation': interpretation,
        'management': management,
        'ais_scores': ais_scores
    }


def render():
    """Render ISS calculator in Streamlit"""
    
    st.title("🦴 Injury Severity Score (ISS)")
    st.markdown("**Đánh giá mức độ nặng đa chấn thương dựa trên giải phẫu**")
    
    # Educational information
    with st.expander("ℹ️ Thông tin & cách sử dụng"):
        st.markdown("""
        ### 📋 Giới Thiệu
        
        **Injury Severity Score (ISS)** là:
        - Thang điểm giải phẫu cho đa chấn thương
        - Dựa trên Abbreviated Injury Scale (AIS)
        - Đánh giá 6 vùng cơ thể
        - Dự đoán tử vong
        
        ### 🎯 6 Vùng Cơ Thể
        
        1. **Head/Neck** (Đầu/Cổ)
        2. **Face** (Mặt)
        3. **Chest** (Ngực)
        4. **Abdomen/Pelvic Contents** (Bụng/Nội tạng chậu)
        5. **Extremities/Pelvic Girdle** (Chi/Khung chậu)
        6. **External** (Ngoài - da, burns)
        
        ### 📊 Abbreviated Injury Scale (AIS)
        
        | AIS | Mô tả | Ví Dụ |
        |-----|-------|-------|
        | **0** | Không tổn thương | - |
        | **1** | Minor | Bầm tím, vết trầy |
        | **2** | Moderate | Gãy xương đơn giản |
        | **3** | Serious | Gãy xương đùi |
        | **4** | Severe | Hemopneumothorax, gãy xương chậu phức tạp |
        | **5** | Critical | Rách gan độ III-IV, chấn thương sọ não nặng |
        | **6** | Unsurvivable | Tổn thương không thể sống sót |
        
        ### 🧮 Công thức ISS
        
        **ISS = A² + B² + C²**
        
        Trong đó A, B, C là 3 điểm AIS CAO NHẤT từ 3 VÙNG KHÁC NHAU
        
        **Lưu ý:**
        - Chỉ lấy điểm cao nhất từ MỖI vùng
        - Nếu có AIS = 6 ở bất kỳ vùng nào → ISS = 75 tự động
        - ISS tối đa = 75 (5² + 5² + 5²)
        
        ### 📈 Phân tầng Nguy cơ
        
        | ISS | Phân Loại | Tử vong | Xử trí|
        |-----|-----------|---------|--------|
        | 1-8 | Minor | <1% | Outpatient có thể |
        | 9-15 | Moderate | <5% | Admit, theo dõi |
        | 16-24 | Serious | 5-20% | ICU, chuyên khoa |
        | 25-49 | Severe | 20-50% | Trauma center, ICU |
        | 50-75 | Critical | >50% | Hồi sức tích cực |
        | 75 (AIS 6) | Unsurvivable | >90% | Palliative care |
        
        ### 📚 Tài liệu tham khảo
        
        - Baker SP, et al. *J Trauma* 1974;14:187-196
        - Copes WS, et al. *J Trauma* 1988;28:69-77
        """)
    
    st.divider()
    
    # Input section
    st.subheader("📝 Nhập AIS Score Cho từng vùng")
    
    st.info("""
    **Hướng dẫn:** Chọn điểm AIS (0-6) cho MỖI vùng cơ thể dựa trên tổn thương nặng nhất trong vùng đó.
    """)
    
    # Create two columns for input
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Vùng 1-3")
        
        ais_head = st.select_slider(
            "**1. Head/Neck (Đầu/Cổ)**",
            options=[0, 1, 2, 3, 4, 5, 6],
            value=0,
            help="Não, sọ, cột sống cổ"
        )
        
        ais_face = st.select_slider(
            "**2. Face (Mặt)**",
            options=[0, 1, 2, 3, 4, 5, 6],
            value=0,
            help="Mặt, mắt, tai, mũi, miệng"
        )
        
        ais_chest = st.select_slider(
            "**3. Chest (Ngực)**",
            options=[0, 1, 2, 3, 4, 5, 6],
            value=0,
            help="Lồng ngực, phổi, tim, mạch máu lớn, thực quản"
        )
    
    with col2:
        st.markdown("#### Vùng 4-6")
        
        ais_abdomen = st.select_slider(
            "**4. Abdomen/Pelvis (Bụng/Chậu)**",
            options=[0, 1, 2, 3, 4, 5, 6],
            value=0,
            help="Gan, lách, thận, ruột, bàng quang, sinh dục"
        )
        
        ais_extremities = st.select_slider(
            "**5. Extremities/Pelvic Girdle (Chi/Khung chậu)**",
            options=[0, 1, 2, 3, 4, 5, 6],
            value=0,
            help="Tay, chân, khung chậu, xương, mạch máu ngoại vi"
        )
        
        ais_external = st.select_slider(
            "**6. External (Bề mặt)**",
            options=[0, 1, 2, 3, 4, 5, 6],
            value=0,
            help="Da, bỏng, vết thương ngoài"
        )
    
    st.divider()
    
    # Calculate button
    if st.button("🧮 Tính ISS & Tiên lượng", type="primary", use_container_width=True):
        ais_scores = {
            'Head/Neck': ais_head,
            'Face': ais_face,
            'Chest': ais_chest,
            'Abdomen/Pelvis': ais_abdomen,
            'Extremities': ais_extremities,
            'External': ais_external
        }
        
        result = calculate_iss(ais_scores)
        
        # Display results
        st.subheader("📊 Kết quả")
        
        # Score box
        col_r1, col_r2 = st.columns([1, 2])
        
        with col_r1:
            st.metric(
                label="**Injury Severity Score**",
                value=result['iss']
            )
            st.caption("1-75 (cao = nặng hơn)")
        
        with col_r2:
            st.markdown(f"### {result['color']} {result['interpretation']}")
            st.markdown(f"**Tỷ lệ tử vong ước tính: {result['mortality']}**")
        
        # Calculation details
        with st.expander("📋 Chi tiết tính toán", expanded=True):
            st.markdown("**AIS Scores theo vùng:**")
            sorted_regions = sorted(result['ais_scores'].items(), key=lambda x: x[1], reverse=True)
            
            for region, score in sorted_regions:
                if score > 0:
                    st.markdown(f"- **{region}:** AIS {score}")
            
            st.markdown("")
            
            # Show calculation
            top_three = sorted([score for score in result['ais_scores'].values()], reverse=True)[:3]
            
            if result['iss'] == 75 and 6 in result['ais_scores'].values():
                st.markdown("**Tính ISS:**")
                st.markdown(f"- Có tổn thương AIS 6 (unsurvivable) → ISS = 75 tự động")
            else:
                st.markdown("**Tính ISS:**")
                st.markdown(f"- 3 điểm AIS cao nhất (từ 3 vùng khác nhau): {top_three[0]}, {top_three[1]}, {top_three[2]}")
                st.markdown(f"- ISS = {top_three[0]}² + {top_three[1]}² + {top_three[2]}²")
                st.markdown(f"- ISS = {top_three[0]**2} + {top_three[1]**2} + {top_three[2]**2}")
                st.markdown(f"- **ISS = {result['iss']}**")
        
        # Management
        st.markdown("---")
        st.markdown("### 💊 Xử trí & quản lý")
        st.markdown(result['management'])
        
        # Additional info
        st.info("""
        **📌 Lưu ý quan trọng:**
        
        - **ISS** là thang điểm GIẢI PHẪU (anatomical), đánh giá tổn thương cơ thể
        - **RTS** là thang điểm SINH LÝ (physiological), đánh giá chức năng sống
        - **TRISS = ISS + RTS + Age** → tiên lượng chính xác nhất
        - ISS ≥16 = "Major Trauma" → cần trauma center
        - ISS ≥25 = "Severe Trauma" → tử vong cao
        """)
        
        if result['risk_class'] in ['CRITICAL', 'UNSURVIVABLE', 'SEVERE']:
            st.error("""
            **🚨 CHẤN THƯƠNG NẶNG/NGUY KỊCH:**
            
            - Bệnh nhân có nguy cơ tử vong CAO
            - Cần chuyển Trauma Center Level I NGAY
            - Activate Trauma Team
            - Chuẩn bị phẫu thuật cấp cứu
            - ICU care và hỗ trợ toàn diện
            - Damage control resuscitation/surgery
            """)
        
        # Save to session state
        st.session_state['iss_result'] = result
        
        # Warning
        st.warning("""
        ⚠️ **Lưu ý y khoa:**
        - ISS đòi hỏi kiến thức về AIS - cần đào tạo để đánh giá chính xác
        - ISS là công cụ hỗ trợ, không thay thế đánh giá lâm sàng
        - Kết hợp ISS với RTS để có TRISS score (tiên lượng tốt hơn)
        - Quyết định điều trị cuối cùng thuộc về bác sĩ điều trị
        """)
    
    # AIS quick reference
    with st.expander("📖 Bảng tham khảo Nhanh - Ví Dụ AIS"):
        st.markdown("""
        ### Ví dụ AIS theo từng vùng
        
        #### 1. Head/Neck
        - **AIS 1:** Headache, không mất ý thức
        - **AIS 2:** Chấn động não (concussion) < 1h
        - **AIS 3:** Xuất huyết nội sọ nhỏ, GCS 12-13
        - **AIS 4:** Xuất huyết nội sọ lớn, GCS 8-11
        - **AIS 5:** Xuất huyết nội sọ lớn + midline shift, GCS 3-7
        - **AIS 6:** Tổn thương thân não không thể sống
        
        #### 2. Face
        - **AIS 1:** Vết trầy, bầm tím mặt
        - **AIS 2:** Gãy xương mũi, hàm đơn giản
        - **AIS 3:** Gãy xương hàm phức tạp
        - **AIS 4:** Gãy xương mặt nặng + tổn thương mắt
        
        #### 3. Chest
        - **AIS 1:** Bầm tím thành ngực
        - **AIS 2:** 1-2 xương sườn gãy
        - **AIS 3:** Hemothorax/Pneumothorax đơn độc, ≥3 xương sườn gãy
        - **AIS 4:** Flail chest, hemopneumothorax lớn
        - **AIS 5:** Rách tim, đứt động mạch chủ lớn
        - **AIS 6:** Tổn thương động mạch chủ không thể sửa
        
        #### 4. Abdomen/Pelvis
        - **AIS 1:** Bầm tím thành bụng
        - **AIS 2:** Rách lách/gan độ I-II (minor)
        - **AIS 3:** Rách lách/gan độ III, rách thận, gãy xương chậu ổn định
        - **AIS 4:** Rách gan độ IV, rách thận nặng, gãy xương chậu không ổn định
        - **AIS 5:** Rách gan/lách độ V, rách ruột lớn, chảy máu sau phúc mạc nặng
        - **AIS 6:** Đứt động mạch chủ bụng lớn
        
        #### 5. Extremities/Pelvic Girdle
        - **AIS 1:** Bầm tím, bong gân nhẹ
        - **AIS 2:** Gãy xương đơn giản (quay, trụ, mác, chày)
        - **AIS 3:** Gãy xương đùi, gãy 2 xương cẳng chân
        - **AIS 4:** Gãy xương đùi + mạch máu, đứt gần hoàn toàn
        - **AIS 5:** Đứt hoàn toàn chi + mạch máu lớn
        
        #### 6. External
        - **AIS 1:** Trầy da nhỏ, bỏng độ I <10% TBSA
        - **AIS 2:** Vết thương da, bỏng độ II 10-20% TBSA
        - **AIS 3:** Bỏng độ II 20-30% TBSA hoặc độ III 10-20%
        - **AIS 4:** Bỏng độ II 30-50% TBSA hoặc độ III 20-30%
        - **AIS 5:** Bỏng độ II >50% TBSA hoặc độ III >30%
        
        **Lưu ý:** Đây là ví dụ đơn giản hóa. AIS dictionary đầy đủ có hàng nghìn mã tổn thương.
        """)

