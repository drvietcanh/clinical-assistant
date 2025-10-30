"""
4Ts Score for Heparin-Induced Thrombocytopenia (HIT)
=====================================================

Clinical prediction rule to estimate the probability of HIT

Reference:
- Lo GK, et al. Evaluation of pretest clinical score (4 T's) for the diagnosis of 
  heparin-induced thrombocytopenia in two clinical settings. J Thromb Haemost. 2006;4(4):759-765.
- Cuker A, et al. American Society of Hematology 2018 guidelines for management of 
  venous thromboembolism: heparin-induced thrombocytopenia. Blood Adv. 2018;2(22):3360-3392.

Four T's Categories:
1. Thrombocytopenia (severity and timing)
2. Timing of platelet count fall
3. Thrombosis or other sequelae
4. oTher causes of thrombocytopenia

Interpretation:
- 6-8 points: High probability (≥50-80% chance of HIT)
- 4-5 points: Intermediate probability (~10-30% chance of HIT)
- 0-3 points: Low probability (<5% chance of HIT)

Clinical Utility:
- High NPV (negative predictive value) for low scores
- Guides HIT antibody testing
- Informs decision to stop heparin and start alternative anticoagulant
"""

import streamlit as st


def calculate_4ts_score(
    thrombocytopenia_category: int,
    timing_category: int,
    thrombosis_category: int,
    other_causes_category: int
) -> dict:
    """
    Calculate 4Ts Score for HIT
    
    Args:
        thrombocytopenia_category: Score for thrombocytopenia severity (0-2)
        timing_category: Score for timing of platelet fall (0-2)
        thrombosis_category: Score for thrombosis/sequelae (0-2)
        other_causes_category: Score for other causes (0-2)
    
    Returns:
        Dictionary containing score, probability, recommendations, and details
    """
    score = (thrombocytopenia_category + timing_category + 
             thrombosis_category + other_causes_category)
    
    # Determine probability and recommendations
    if score >= 6:
        probability = "XÁC SUẤT CAO (High Probability)"
        probability_range = "50-80%"
        risk_class = "HIGH"
        color = "🔴"
        recommendation = """
        **🔴 Xử Trí Khuyến Cáo - HIGH PROBABILITY:**
        
        1. **DỪNG Heparin NGAY LẬP TỨC:**
           - Dừng TẤT CẢ heparin (UFH, LMWH, heparin flush)
           - Kiểm tra tất cả thuốc/dịch truyền có chứa heparin
           - Không dùng heparin cho bất kỳ mục đích nào
        
        2. **Bắt Đầu Kháng Đông Thay Thế:**
           - **Argatroban** (DTI - direct thrombin inhibitor):
             * Liều: 2 mcg/kg/min IV (giảm 0.5-1 mcg/kg/min nếu suy gan)
             * Theo dõi aPTT (mục tiêu: 1.5-3× baseline)
           - **HOẶC Fondaparinux** (nếu có):
             * <50 kg: 5 mg SC q24h
             * 50-100 kg: 7.5 mg SC q24h
             * >100 kg: 10 mg SC q24h
           - **HOẶC Danaparoid** (nếu có)
        
        3. **XÉT NGHIỆM Xác Định:**
           - **HIT antibody ELISA** (PF4/heparin antibodies)
           - **Serotonin Release Assay (SRA)** - functional assay (gold standard)
           - Đợi kết quả nhưng KHÔNG trì hoãn điều trị
        
        4. **KHÔNG Dùng:**
           - ❌ Warfarin cho đến khi tiểu cầu >150,000/μL (nguy cơ hoại tử da, gangrene)
           - ❌ Truyền tiểu cầu (trừ khi chảy máu đe dọa tính mạng)
        
        5. **Theo Dõi:**
           - Đếm tiểu cầu hàng ngày cho đến khi >150,000
           - Đánh giá huyết khối mới (DVT, PE, động mạch)
           - Siêu âm doppler chi dưới nếu chưa làm
        
        6. **Chuyển Đổi Sang Warfarin:**
           - Chờ tiểu cầu >150,000/μL × 2 ngày
           - Overlap ≥5 ngày + INR 2-3 trong 24h
           - Duy trì kháng đông ≥3 tháng
        """
        
        education = """
        **💡 Diễn Giải - High Probability:**
        - 4Ts ≥6 → HIT có khả năng cao (50-80%)
        - PPV ~70-90% (tùy population)
        - PHẢI dừng heparin và bắt đầu kháng đông thay thế NGAY
        - Đợi xét nghiệm xác nhận nhưng KHÔNG trì hoãn điều trị
        - Nguy cơ huyết khối cao (~30-50%) nếu không điều trị
        """
        
    elif score >= 4:
        probability = "XÁC SUẤT TRUNG BÌNH (Intermediate Probability)"
        probability_range = "10-30%"
        risk_class = "INTERMEDIATE"
        color = "🟡"
        recommendation = """
        **🟡 Xử Trí Khuyến Cáo - INTERMEDIATE PROBABILITY:**
        
        1. **Đánh Giá Kỹ & Quyết Định:**
           - Xem xét DỪNG heparin (khuyến cáo mạnh nếu điểm 5)
           - Nếu điểm = 4 → cân nhắc rủi ro/lợi ích
           - Nếu không thể dừng → giám sát sát tiểu cầu
        
        2. **XÉT NGHIỆM Khẩn:**
           - **HIT antibody ELISA** NGAY
           - Nếu ELISA dương tính → làm functional assay (SRA)
           - Quyết định dựa trên kết quả xét nghiệm
        
        3. **Nếu Quyết Định Dừng Heparin:**
           - Bắt đầu kháng đông thay thế (argatroban/fondaparinux)
           - Theo dõi tiểu cầu hàng ngày
           - Đánh giá huyết khối
        
        4. **Nếu Tiếp Tục Heparin:**
           - Đếm tiểu cầu ít nhất 2 lần/ngày
           - Nếu tiểu cầu giảm >50% hoặc <100,000 → DỪNG NGAY
           - Theo dõi sát triệu chứng huyết khối
        
        5. **Khi Có Kết Quả ELISA:**
           - **Dương tính (OD >1.0):** Xử trí như HIGH probability
           - **Âm tính hoặc yếu (OD <0.4):** Có thể an toàn tiếp tục heparin
           - **Borderline (OD 0.4-1.0):** Cần functional assay
        
        6. **Theo Dõi:**
           - Tiểu cầu hàng ngày cho đến khi có kết quả xét nghiệm
           - Tái đánh giá 4Ts nếu có thay đổi lâm sàng
        """
        
        education = """
        **💡 Diễn Giải - Intermediate Probability:**
        - 4Ts = 4-5 → HIT có thể có (10-30%)
        - Không thể loại trừ hoàn toàn
        - Cần xét nghiệm ELISA để quyết định
        - Nếu ELISA dương tính → xử trí như HIGH
        - Nếu ELISA âm tính → an toàn tiếp tục heparin
        """
        
    else:  # score 0-3
        probability = "XÁC SUẤT THẤP (Low Probability)"
        probability_range = "<5%"
        risk_class = "LOW"
        color = "🟢"
        recommendation = """
        **🟢 Xử Trí Khuyến Cáo - LOW PROBABILITY:**
        
        1. **Đánh Giá:**
           - HIT rất ít có khả năng (NPV ~95-99%)
           - Có thể AN TOÀN tiếp tục heparin
           - Tìm nguyên nhân KHÁC của giảm tiểu cầu
        
        2. **Xét Nghiệm:**
           - Xét nghiệm HIT antibody KHÔNG khuyến cáo (trừ khi nghi ngờ đặc biệt)
           - Nếu vẫn lo lắng → có thể làm ELISA (thường âm tính)
           - Tìm nguyên nhân khác: sepsis, thuốc, DIC, etc.
        
        3. **Nguyên Nhân Khác Cần Xem Xét:**
           - **Sepsis/Infection** (phổ biến nhất)
           - **Thuốc khác:** Vancomycin, linezolid, valproate, H2-blockers, etc.
           - **DIC** (Disseminated Intravascular Coagulation)
           - **TTP/HUS** (Thrombotic Thrombocytopenic Purpura)
           - **Giảm tiểu cầu sau phẫu thuật** (dilutional, consumption)
           - **ITP** (Immune Thrombocytopenic Purpura)
           - **Giảm tiểu cầu do gan/lách to**
        
        4. **Theo Dõi:**
           - Đếm tiểu cầu theo clinical indication
           - Tái đánh giá 4Ts nếu có thay đổi lâm sàng
           - Nếu tiểu cầu tiếp tục giảm → xem xét lại
        
        5. **Lưu Ý:**
           - 4Ts <4 có NPV rất cao → an toàn loại trừ HIT
           - NHƯNG nếu có thay đổi lâm sàng → tính lại 4Ts
           - Không dừng heparin chỉ dựa trên điểm thấp
        """
        
        education = """
        **💡 Diễn Giải - Low Probability:**
        - 4Ts ≤3 → HIT rất ít có khả năng (<5%)
        - NPV ~95-99% → an toàn loại trừ
        - Không cần xét nghiệm HIT antibody
        - Có thể tiếp tục heparin an toàn
        - Tìm nguyên nhân khác của giảm tiểu cầu
        """
    
    # Map categories to descriptions
    category_descriptions = {
        'thrombocytopenia': [
            "0 điểm: Giảm tiểu cầu <30% hoặc nadir <10,000/μL",
            "1 điểm: Giảm 30-50% hoặc nadir 10,000-19,000/μL",
            "2 điểm: Giảm >50% và nadir ≥20,000/μL"
        ],
        'timing': [
            "0 điểm: ≤4 ngày không tiếp xúc heparin gần đây, hoặc không rõ, hoặc >100 ngày",
            "1 điểm: >10 ngày HOẶC ≤1 ngày với tiếp xúc heparin trong 30-100 ngày",
            "2 điểm: 5-10 ngày HOẶC ≤1 ngày với tiếp xúc heparin trong 30 ngày"
        ],
        'thrombosis': [
            "0 điểm: Không có huyết khối, hoại tử da, phản ứng cấp",
            "1 điểm: Huyết khối tiến triển/tái phát, hoặc tổn thương đỏ da không hoại tử, hoặc nghi ngờ huyết khối",
            "2 điểm: Huyết khối MỚI xác định, hoặc hoại tử da, hoặc phản ứng cấp sau bolus heparin"
        ],
        'other_causes': [
            "0 điểm: Có nguyên nhân rõ ràng khác",
            "1 điểm: Có thể có nguyên nhân khác",
            "2 điểm: Không có nguyên nhân nào khác rõ ràng"
        ]
    }
    
    selected_descriptions = [
        category_descriptions['thrombocytopenia'][thrombocytopenia_category],
        category_descriptions['timing'][timing_category],
        category_descriptions['thrombosis'][thrombosis_category],
        category_descriptions['other_causes'][other_causes_category]
    ]
    
    return {
        'score': score,
        'probability': probability,
        'probability_range': probability_range,
        'risk_class': risk_class,
        'recommendation': recommendation,
        'education': education,
        'color': color,
        'details': selected_descriptions
    }


def render():
    """Render 4Ts Score calculator in Streamlit"""
    
    st.title("🩸 4Ts Score - Heparin-Induced Thrombocytopenia (HIT)")
    st.markdown("**Đánh giá xác suất giảm tiểu cầu do heparin**")
    
    # Educational information
    with st.expander("ℹ️ Thông Tin & Cách Sử Dụng"):
        st.markdown("""
        ### 📋 Giới Thiệu
        
        **4Ts Score** là thang điểm lâm sàng để:
        - Đánh giá xác suất tiền test của HIT (Heparin-Induced Thrombocytopenia)
        - Hướng dẫn quyết định dừng heparin và xét nghiệm
        - Phân tầng nguy cơ trước khi có kết quả xét nghiệm
        
        **HIT** là biến chứng nghiêm trọng:
        - Tỷ lệ: 0.1-1% (UFH), 0.01-0.1% (LMWH)
        - Nguy cơ huyết khối: 30-50% nếu không điều trị
        - Tử vong: ~10-20%
        
        ### 🎯 4 Thành Phần (4 T's)
        
        1. **T**hrombocytopenia: Mức độ giảm tiểu cầu
        2. **T**iming: Thời gian xuất hiện giảm tiểu cầu
        3. **T**hrombosis: Huyết khối hoặc biến chứng khác
        4. o**T**her causes: Các nguyên nhân khác
        
        ### 📊 Phân Tầng Nguy Cơ
        
        | Điểm 4Ts | Phân Loại | Xác Suất HIT | Xử Trí |
        |----------|-----------|--------------|--------|
        | 6-8 | High | 50-80% | Dừng heparin NGAY, kháng đông thay thế |
        | 4-5 | Intermediate | 10-30% | Cân nhắc dừng, xét nghiệm ELISA |
        | 0-3 | Low | <5% | An toàn tiếp tục, tìm nguyên nhân khác |
        
        ### ⚠️ Lưu Ý Quan Trọng
        
        - **4Ts HIGH (≥6):** DỪNG heparin NGAY + bắt đầu alternative anticoagulant
        - **KHÔNG truyền tiểu cầu** (trừ chảy máu đe dọa tính mạng)
        - **KHÔNG dùng warfarin** cho đến khi tiểu cầu >150,000/μL
        - **Functional assay (SRA)** là gold standard nhưng mất thời gian
        
        ### 📚 Tài Liệu Tham Khảo
        
        - Lo GK, et al. *J Thromb Haemost* 2006;4:759-765
        - Cuker A, et al. *Blood Adv* 2018;2:3360-3392
        - ASH 2018 Guidelines for Management of HIT
        """)
    
    st.divider()
    
    # Input section
    st.subheader("📝 Nhập Thông Tin 4 Thành Phần")
    
    # 1. Thrombocytopenia
    st.markdown("#### 1️⃣ Thrombocytopenia - Mức Độ Giảm Tiểu Cầu")
    thrombocytopenia_category = st.radio(
        "Chọn mức độ giảm tiểu cầu:",
        options=[2, 1, 0],
        format_func=lambda x: [
            "2 điểm: Giảm >50% VÀ nadir ≥20,000/μL",
            "1 điểm: Giảm 30-50% HOẶC nadir 10,000-19,000/μL",
            "0 điểm: Giảm <30% HOẶC nadir <10,000/μL"
        ][2-x],
        key="thrombocytopenia",
        help="% giảm = (Tiểu cầu cao nhất - Tiểu cầu thấp nhất) / Tiểu cầu cao nhất × 100%"
    )
    
    st.divider()
    
    # 2. Timing
    st.markdown("#### 2️⃣ Timing - Thời Gian Xuất Hiện Giảm Tiểu Cầu")
    st.caption("Tính từ khi BẮT ĐẦU heparin đến khi tiểu cầu giảm")
    
    timing_category = st.radio(
        "Chọn thời gian xuất hiện:",
        options=[2, 1, 0],
        format_func=lambda x: [
            "2 điểm: 5-10 ngày SAU khi bắt đầu heparin\nHOẶC ≤1 ngày (nếu có tiếp xúc heparin trong 30 ngày gần đây)",
            "1 điểm: >10 ngày sau khi bắt đầu heparin\nHOẶC ≤1 ngày (nếu có tiếp xúc heparin trong 30-100 ngày trước)",
            "0 điểm: ≤4 ngày (không có tiếp xúc heparin gần đây)\nHOẶC >100 ngày\nHOẶC không rõ thời gian"
        ][2-x],
        key="timing",
        help="Thời gian điển hình của HIT: 5-10 ngày. Nếu đã tiếp xúc heparin trước đó → có thể xuất hiện sớm hơn (<24h)"
    )
    
    st.divider()
    
    # 3. Thrombosis
    st.markdown("#### 3️⃣ Thrombosis - Huyết Khối hoặc Biến Chứng Khác")
    thrombosis_category = st.radio(
        "Chọn tình trạng huyết khối/biến chứng:",
        options=[2, 1, 0],
        format_func=lambda x: [
            "2 điểm: Huyết khối MỚI được xác định (DVT, PE, động mạch)\nHOẶC hoại tử da tại vị trí tiêm\nHOẶC phản ứng cấp tính sau bolus heparin",
            "1 điểm: Huyết khối tiến triển/tái phát\nHOẶC tổn thương da đỏ (chưa hoại tử)\nHOẶC nghi ngờ huyết khối chưa xác định",
            "0 điểm: KHÔNG có huyết khối, hoại tử da, hoặc phản ứng cấp"
        ][2-x],
        key="thrombosis",
        help="HIT thường đi kèm huyết khối (30-50%). Huyết khối có thể xuất hiện TRƯỚC khi tiểu cầu giảm rõ rệt."
    )
    
    st.divider()
    
    # 4. Other causes
    st.markdown("#### 4️⃣ oTher Causes - Các Nguyên Nhân Khác")
    st.caption("Đánh giá khả năng có nguyên nhân KHÁC gây giảm tiểu cầu")
    
    other_causes_category = st.radio(
        "Đánh giá các nguyên nhân khác:",
        options=[2, 1, 0],
        format_func=lambda x: [
            "2 điểm: KHÔNG có nguyên nhân nào khác rõ ràng",
            "1 điểm: CÓ THỂ có nguyên nhân khác (sepsis, thuốc, DIC, etc.)",
            "0 điểm: CÓ nguyên nhân RÕ RÀNG khác (ví dụ: sepsis nặng, phẫu thuật lớn, thuốc gây giảm TC rõ)"
        ][2-x],
        key="other_causes",
        help="Nguyên nhân khác: Sepsis, thuốc (vancomycin, linezolid), DIC, TTP/HUS, phẫu thuật, dilutional"
    )
    
    st.divider()
    
    # Calculate button
    if st.button("🧮 Tính Toán 4Ts Score", type="primary", use_container_width=True):
        result = calculate_4ts_score(
            thrombocytopenia_category=thrombocytopenia_category,
            timing_category=timing_category,
            thrombosis_category=thrombosis_category,
            other_causes_category=other_causes_category
        )
        
        # Display results
        st.subheader("📊 Kết Quả")
        
        # Score box
        col_r1, col_r2 = st.columns([1, 2])
        
        with col_r1:
            st.metric(
                label="**4Ts Score**",
                value=f"{result['score']} điểm"
            )
        
        with col_r2:
            st.markdown(f"### {result['color']} {result['probability']}")
            st.markdown(f"**Xác suất HIT: {result['probability_range']}**")
        
        # Details
        with st.expander("📋 Chi Tiết Tính Điểm", expanded=True):
            st.markdown("**Các thành phần đã chọn:**")
            for i, detail in enumerate(result['details'], 1):
                st.markdown(f"{i}. {detail}")
        
        # Recommendations
        st.markdown("---")
        st.markdown(result['recommendation'])
        
        # Education
        with st.expander("💡 Diễn Giải Kết Quả"):
            st.markdown(result['education'])
        
        # Additional clinical context
        if result['risk_class'] in ['HIGH', 'INTERMEDIATE']:
            st.error("""
            **🚨 CẢNH BÁO QUAN TRỌNG:**
            
            - HIT là cấp cứu huyết học - có thể gây huyết khối đe dọa tính mạng/chi
            - Nếu 4Ts ≥4 → cân nhắc DỪNG heparin và xét nghiệm NGAY
            - KHÔNG truyền tiểu cầu (có thể làm tăng nguy cơ huyết khối)
            - KHÔNG dùng warfarin khi tiểu cầu thấp (nguy cơ hoại tử da, gangrene tứ chi)
            """)
        
        st.info("""
        **🔬 Xét Nghiệm HIT:**
        
        1. **ELISA (PF4/Heparin Antibodies):**
           - Nhanh (vài giờ), nhạy cao
           - OD >1.0: Dương tính mạnh
           - OD 0.4-1.0: Borderline (cần functional assay)
           - OD <0.4: Âm tính
        
        2. **Functional Assay (SRA - Serotonin Release Assay):**
           - Gold standard, đặc hiệu cao
           - Mất 1-3 ngày
           - Xác nhận chẩn đoán cuối cùng
        
        **Chiến Lược:**
        - 4Ts ≥6 → Dừng heparin NGAY + bắt đầu alternative (đợi ELISA để xác nhận)
        - 4Ts 4-5 → Làm ELISA, quyết định dựa trên kết quả
        - 4Ts ≤3 → Không cần xét nghiệm, tìm nguyên nhân khác
        """)
        
        # Save to session state
        st.session_state['four_ts_result'] = result
        
        # Warning
        st.warning("""
        ⚠️ **Lưu Ý Y Khoa:**
        - Thang điểm 4Ts là công cụ hỗ trợ, cần kết hợp với xét nghiệm và đánh giá lâm sàng
        - Quyết định dừng heparin và điều trị thay thế thuộc về bác sĩ điều trị
        - Khi nghi ngờ HIT → tư vấn huyết học ngay
        """)
    
    # Quick reference
    with st.expander("📖 Bảng Tham Khảo Nhanh - Alternative Anticoagulants"):
        st.markdown("""
        ### Thuốc Kháng Đông Thay Thế Cho HIT
        
        #### 1. Argatroban (DTI - Direct Thrombin Inhibitor)
        - **Liều:** 2 mcg/kg/min IV continuous
          - Suy gan: 0.5-1 mcg/kg/min
        - **Theo dõi:** aPTT (mục tiêu 1.5-3× baseline, thường 60-80s)
        - **Ưu điểm:** Phổ biến, bài tiết qua gan
        - **Nhược điểm:** Tăng INR → khó chuyển warfarin
        
        #### 2. Fondaparinux (Factor Xa Inhibitor)
        - **Liều:**
          - <50 kg: 5 mg SC q24h
          - 50-100 kg: 7.5 mg SC q24h
          - >100 kg: 10 mg SC q24h
        - **Ưu điểm:** SC, không cần monitor
        - **Nhược điểm:** Bài tiết thận (tránh nếu CrCl <30)
        
        #### 3. Danaparoid (nếu có)
        - **Liều:** 2,500 U IV bolus, sau đó 400 U/h × 4h, sau đó 300 U/h × 4h, sau đó 200 U/h
        - **Nhược điểm:** Khó kiếm, bài tiết thận
        
        #### 4. DOACs (Direct Oral Anticoagulants) - OFF-LABEL
        - **Rivaroxaban, Apixaban:** Một số evidence nhưng chưa approved chính thức
        - Có thể xem xét nếu không có alternative khác
        
        ### Chuyển Đổi Sang Warfarin
        
        1. **Chờ tiểu cầu >150,000/μL** × 2 ngày liên tiếp
        2. **Bắt đầu warfarin:** 5 mg/ngày (hoặc liều thấp hơn nếu người già)
        3. **Overlap ≥5 ngày** + INR 2-3 trong 24h
        4. **Duy trì kháng đông:** ≥3 tháng (6-12 tháng nếu có huyết khối)
        
        ### Lưu Ý Quan Trọng
        
        - ❌ **KHÔNG dùng warfarin khi tiểu cầu thấp** → nguy cơ warfarin-induced limb gangrene
        - ❌ **KHÔNG truyền tiểu cầu** (trừ chảy máu đe dọa tính mạng)
        - ✅ **Theo dõi tiểu cầu hàng ngày** cho đến khi >150,000/μL
        - ✅ **Đánh giá huyết khối** (siêu âm doppler chi dưới, CT PE nếu cần)
        """)

