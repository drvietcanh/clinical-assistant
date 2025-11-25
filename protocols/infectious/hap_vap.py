"""
Hospital-Acquired Pneumonia (HAP) / Ventilator-Associated Pneumonia (VAP) Guidelines
IDSA/ATS 2016 Guidelines
"""

import streamlit as st


def render():
    """Hospital-Acquired Pneumonia (HAP) / Ventilator-Associated Pneumonia (VAP) Guidelines"""
    st.subheader("🏥 Hospital-Acquired Pneumonia (HAP) / Ventilator-Associated Pneumonia (VAP)")
    st.caption("IDSA/ATS 2016 Guidelines - HAP/VAP Management")
    
    st.info("""
    **Chẩn đoán HAP/VAP khi có:**
    - Triệu chứng hô hấp mới hoặc xấu đi
    - X-quang ngực: thâm nhiễm mới hoặc tiến triển
    - Có yếu tố nguy cơ nhiễm trùng bệnh viện
    - **HAP:** Khởi phát ≥48h sau nhập viện
    - **VAP:** Khởi phát ≥48h sau đặt nội khí quản
    """)
    
    st.markdown("---")
    
    # ========== SECTION 1: RISK STRATIFICATION ==========
    st.markdown("### 📊 Phân Tầng Nguy Cơ MDR (Multidrug-Resistant)")
    
    st.markdown("**Yếu tố nguy cơ MDR:**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.warning("""
        **Yếu tố nguy cơ MDR:**
        - Kháng sinh phổ rộng trong 90 ngày qua
        - Nhập viện ≥5 ngày
        - Tỷ lệ kháng thuốc cao tại địa phương (>10-20%)
        - Suy thận đang lọc máu
        - Suy giảm miễn dịch
        """)
    
    with col2:
        st.error("""
        **Yếu tố nguy cơ MRSA:**
        - Tiền sử MRSA
        - Vết thương phẫu thuật
        - Lọc máu
        - Nhập viện gần đây
        - Kháng sinh gần đây
        """)
    
    st.markdown("---")
    
    # ========== SECTION 2: EMPIRIC ANTIBIOTIC SELECTION ==========
    st.markdown("### 💊 Lựa Chọn Kháng Sinh Thực Nghiệm")
    
    # Risk assessment
    has_mdr_risk = st.checkbox("Có yếu tố nguy cơ MDR", key="hap_mdr_risk")
    has_mrsa_risk = st.checkbox("Có yếu tố nguy cơ MRSA", key="hap_mrsa_risk")
    
    st.markdown("---")
    
    if not has_mdr_risk:
        st.success("""
        ### ✅ Không Có Yếu Tố Nguy Cơ MDR
        
        **Lựa chọn 1:**
        - Ceftriaxone 2g IV QD
        - Hoặc Levofloxacin 750mg IV QD
        - Hoặc Moxifloxacin 400mg IV QD
        - Hoặc Ampicillin-sulbactam 3g IV q6h
        
        **Thêm Vancomycin nếu có yếu tố nguy cơ MRSA:**
        - Vancomycin 15-20mg/kg IV q8-12h (điều chỉnh theo CrCl)
        """)
    else:
        st.error("""
        ### 🚨 Có Yếu Tố Nguy Cơ MDR
        
        **Empiric Therapy (Phổ rộng):**
        
        **Beta-lactam + Aminoglycoside/Fluoroquinolone:**
        - Piperacillin-tazobactam 4.5g IV q6h
        + Gentamicin 5-7mg/kg IV QD (hoặc Tobramycin)
        
        **Hoặc:**
        - Cefepime 2g IV q8h
        + Gentamicin 5-7mg/kg IV QD
        
        **Hoặc:**
        - Meropenem 1g IV q8h
        + Gentamicin 5-7mg/kg IV QD
        
        **Thêm Vancomycin nếu có yếu tố nguy cơ MRSA:**
        - Vancomycin 15-20mg/kg IV q8-12h (điều chỉnh theo CrCl)
        - Hoặc Linezolid 600mg IV q12h (nếu suy thận)
        """)
    
    st.markdown("---")
    
    # ========== SECTION 3: DE-ESCALATION ==========
    st.markdown("### 🔄 Chiến Lược De-escalation")
    
    st.info("""
    **Sau 48-72 giờ, đánh giá lại:**
    
    **Nếu cải thiện và có kháng sinh đồ:**
    1. ✅ **De-escalate:** Chuyển sang kháng sinh phổ hẹp hơn
    2. ✅ **Rút bỏ:** Ngừng kháng sinh không cần thiết
    3. ✅ **Điều chỉnh liều:** Theo kháng sinh đồ
    
    **Nếu không cải thiện:**
    - Xem xét thay đổi kháng sinh
    - Tìm ổ nhiễm trùng khác
    - Xem xét các chẩn đoán khác
    """)
    
    st.markdown("---")
    
    # ========== SECTION 4: DURATION ==========
    st.markdown("### ⏱️ Thời Gian Điều Trị")
    
    st.warning("""
    **Thời gian điều trị:**
    - **HAP/VAP:** 7 ngày (khuyến nghị)
    - **Có thể kéo dài đến 14 ngày** nếu:
      - Nhiễm trùng chậm cải thiện
      - Có biến chứng (áp xe, tràn mủ màng phổi)
      - Vi khuẩn không điển hình (Legionella, Pseudomonas)
    
    **⚠️ Tránh điều trị quá dài:**
    - Tăng nguy cơ kháng thuốc
    - Tăng tác dụng phụ
    - Tăng chi phí
    """)
    
    st.markdown("---")
    
    # ========== SECTION 5: MONITORING ==========
    st.markdown("### 📈 Monitoring")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Hàng ngày:**
        - Dấu hiệu sống (nhiệt độ, mạch, huyết áp, SpO2)
        - Tình trạng hô hấp
        - X-quang ngực (nếu cần)
        
        **Xét nghiệm:**
        - CBC, CRP/Procalcitonin
        - Chức năng thận (nếu dùng aminoglycoside)
        """)
    
    with col2:
        st.markdown("""
        **Dấu hiệu cải thiện:**
        - Hết sốt trong 48-72h
        - Giảm triệu chứng hô hấp
        - Cải thiện X-quang
        
        **Dấu hiệu cảnh báo:**
        - Sốt kéo dài >72h
        - Tình trạng xấu đi
        - Cần xem xét thay đổi kháng sinh
        """)
    
    st.markdown("---")
    
    # ========== SECTION 6: SPECIAL POPULATIONS ==========
    st.markdown("### 👥 Special Populations")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Suy thận:**
        - Điều chỉnh liều theo CrCl
        - Tránh aminoglycoside nếu có thể
        - Dùng beta-lactam + vancomycin
        
        **Suy gan:**
        - Điều chỉnh liều một số thuốc
        - Theo dõi chức năng gan
        """)
    
    with col2:
        st.markdown("""
        **Có thai:**
        - Tránh fluoroquinolone, tetracycline
        - Dùng beta-lactam an toàn
        
        **Dị ứng penicillin:**
        - Dùng fluoroquinolone
        - Hoặc aztreonam + vancomycin
        """)
    
    st.markdown("---")
    
    # ========== SECTION 7: PREVENTION ==========
    st.markdown("### 🛡️ Phòng ngừa VAP")
    
    st.info("""
    **Các biện pháp phòng ngừa VAP:**
    - Nâng đầu giường 30-45 độ
    - Vệ sinh răng miệng thường xuyên
    - Rút nội khí quản sớm khi có thể
    - Tránh thay đổi ống nội khí quản không cần thiết
    - Sử dụng ống nội khí quản có cuff áp lực phù hợp
    - Phòng ngừa loét do tỳ đè
    """)
    
    st.markdown("---")
    
    # ========== SECTION 8: REFERENCES ==========
    st.markdown("### 📚 References")
    
    st.markdown("""
    1. **IDSA/ATS 2016 Guidelines** - Management of Adults with Hospital-acquired and Ventilator-associated Pneumonia
       - Kalil AC, et al. Management of Adults With Hospital-acquired and Ventilator-associated Pneumonia: 2016 Clinical Practice Guidelines by the Infectious Diseases Society of America and the American Thoracic Society. Clin Infect Dis. 2016;63(5):e61-e111.
    
    2. **UpToDate:** Hospital-acquired pneumonia and ventilator-associated pneumonia in adults - Last updated 2024
    
    3. **De-escalation Strategy:**
       - Kuti JL, et al. Optimizing antibiotic pharmacodynamics in clinical practice. Minerva Anestesiol. 2011;77(1):88-95.
    """)
    
    st.markdown("---")
    
    # Footer
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể, kháng sinh đồ địa phương, và guidelines mới nhất.")

