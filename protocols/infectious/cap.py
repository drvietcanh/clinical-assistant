"""
Community Acquired Pneumonia (CAP) Management Protocol
IDSA/ATS 2019 Guidelines
"""

import streamlit as st


def render():
    """Community Acquired Pneumonia (CAP) Management Protocol"""
    st.subheader("🫁 Community Acquired Pneumonia (CAP) Management")
    st.caption("IDSA/ATS 2019 Guidelines - Community Acquired Pneumonia")
    
    st.info("""
    **Chẩn đoán CAP khi có:**
    - Triệu chứng hô hấp (ho, khó thở, đau ngực)
    - Dấu hiệu nhiễm trùng (sốt, tăng bạch cầu)
    - X-quang ngực: thâm nhiễm mới
    - Không có yếu tố nguy cơ nhiễm trùng bệnh viện
    """)
    
    st.markdown("---")
    
    # ========== SECTION 1: RISK STRATIFICATION ==========
    st.markdown("### 📊 Phân Tầng Nguy Cơ (Risk Stratification)")
    
    st.markdown("""
    **Sử dụng CURB-65 hoặc PSI (Pneumonia Severity Index) để quyết định:**
    - **Điều trị ngoại trú** (Low risk)
    - **Nhập viện** (Moderate risk)
    - **ICU** (High risk)
    """)
    
    # CURB-65 Calculator
    with st.expander("🔢 Tính CURB-65 Score", expanded=False):
        st.markdown("**CURB-65 Criteria:**")
        
        confusion = st.checkbox("C - Confusion (Lú lẫn)", key="cap_confusion")
        urea = st.checkbox("U - Urea >7 mmol/L", key="cap_urea")
        respiratory = st.checkbox("R - Respiratory rate ≥30/min", key="cap_respiratory")
        bp = st.checkbox("B - Blood pressure <90/60 mmHg", key="cap_bp")
        age = st.checkbox("65 - Age ≥65 tuổi", key="cap_age")
        
        curb65_score = sum([confusion, urea, respiratory, bp, age])
        
        if curb65_score > 0:
            st.markdown(f"**CURB-65 Score: {curb65_score}/5**")
            
            if curb65_score == 0:
                st.success("✅ **Nguy cơ thấp** - Có thể điều trị ngoại trú")
            elif curb65_score <= 2:
                st.warning("⚠️ **Nguy cơ trung bình** - Cân nhắc nhập viện")
            else:
                st.error("🚨 **Nguy cơ cao** - Cần nhập viện, cân nhắc ICU")
    
    st.markdown("---")
    
    # ========== SECTION 2: OUTPATIENT TREATMENT ==========
    st.markdown("### 🏠 Điều Trị Ngoại Trú (Outpatient)")
    
    st.markdown("**Chỉ Định:** CURB-65 = 0-1, PSI Class I-III, không có yếu tố nguy cơ MDR")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("""
        **Không Có Yếu Tố Nguy Cơ Kháng Thuốc:**
        
        **Lựa chọn 1:**
        - Amoxicillin 1g PO TID
        - Hoặc Amoxicillin-clavulanate 875/125mg PO BID
        
        **Lựa chọn 2:**
        - Doxycycline 100mg PO BID
        
        **Lựa chọn 3:**
        - Macrolide (Azithromycin 500mg PO x 1, sau đó 250mg PO QD x 4 ngày)
        - Hoặc Clarithromycin 500mg PO BID
        """)
    
    with col2:
        st.warning("""
        **Có Yếu Tố Nguy Cơ Kháng Thuốc:**
        - COPD, hút thuốc, kháng sinh gần đây
        
        **Lựa chọn:**
        - Amoxicillin-clavulanate 875/125mg PO BID
        + Macrolide (Azithromycin hoặc Clarithromycin)
        
        **Hoặc:**
        - Levofloxacin 750mg PO QD
        - Hoặc Moxifloxacin 400mg PO QD
        """)
    
    st.markdown("---")
    
    # ========== SECTION 3: INPATIENT (NON-ICU) ==========
    st.markdown("### 🏥 Điều Trị Nội Trú (Non-ICU)")
    
    st.markdown("**Chỉ Định:** CURB-65 = 2, PSI Class IV, cần nhập viện nhưng không cần ICU")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("""
        **Không Có Yếu Tố Nguy Cơ MDR:**
        
        **Lựa chọn 1:**
        - Ampicillin-sulbactam 1.5-3g IV q6h
        + Macrolide (Azithromycin 500mg IV QD)
        
        **Lựa chọn 2:**
        - Ceftriaxone 1-2g IV QD
        + Macrolide (Azithromycin 500mg IV QD)
        
        **Lựa chọn 3:**
        - Levofloxacin 750mg IV QD
        - Hoặc Moxifloxacin 400mg IV QD
        """)
    
    with col2:
        st.warning("""
        **Có Yếu Tố Nguy Cơ MDR:**
        - Kháng sinh gần đây, nhập viện gần đây, COPD nặng
        
        **Lựa chọn:**
        - Piperacillin-tazobactam 4.5g IV q6h
        + Macrolide (Azithromycin 500mg IV QD)
        
        **Hoặc:**
        - Ceftriaxone 1-2g IV QD
        + Azithromycin 500mg IV QD
        + Vancomycin (nếu nghi MRSA)
        """)
    
    st.markdown("---")
    
    # ========== SECTION 4: ICU TREATMENT ==========
    st.markdown("### 🚨 Điều Trị ICU")
    
    st.markdown("**Chỉ Định:** CURB-65 ≥3, PSI Class V, suy hô hấp, sốc nhiễm khuẩn")
    
    st.error("""
    **Empiric Therapy (Phổ rộng):**
    
    **Beta-lactam + Macrolide:**
    - Ceftriaxone 2g IV QD
    + Azithromycin 500mg IV QD
    
    **Hoặc:**
    - Piperacillin-tazobactam 4.5g IV q6h
    + Azithromycin 500mg IV QD
    
    **Thêm Vancomycin nếu:**
    - Nghi MRSA (có yếu tố nguy cơ)
    - Vancomycin 15-20mg/kg IV q8-12h (điều chỉnh theo CrCl)
    
    **Hoặc Fluoroquinolone:**
    - Levofloxacin 750mg IV QD
    + Vancomycin (nếu nghi MRSA)
    """)
    
    st.markdown("---")
    
    # ========== SECTION 5: DURATION ==========
    st.markdown("### ⏱️ Thời Gian Điều Trị")
    
    st.info("""
    **Thời gian điều trị:**
    - **Ngoại trú:** 5-7 ngày
    - **Nội trú:** 5-7 ngày (có thể ngắn hơn nếu đáp ứng tốt)
    - **ICU:** 7-10 ngày
    
    **Chuyển từ IV sang PO:**
    - Khi bệnh nhân ổn định (afebrile ≥24h, cải thiện triệu chứng)
    - Chuyển sang cùng loại thuốc hoặc tương đương
    - Ví dụ: Ceftriaxone IV → Amoxicillin-clavulanate PO
    """)
    
    st.markdown("---")
    
    # ========== SECTION 6: MONITORING ==========
    st.markdown("### 📈 Monitoring")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Hàng ngày:**
        - Dấu hiệu sống (nhiệt độ, mạch, huyết áp, SpO2)
        - Triệu chứng hô hấp
        - Tình trạng tổng quát
        
        **Xét nghiệm:**
        - CBC (nếu cần)
        - CRP/Procalcitonin (nếu có)
        """)
    
    with col2:
        st.markdown("""
        **Dấu hiệu cải thiện:**
        - Hết sốt trong 48-72h
        - Giảm triệu chứng hô hấp
        - Cải thiện X-quang (chậm hơn)
        
        **Dấu hiệu cảnh báo:**
        - Sốt kéo dài >72h
        - Tình trạng xấu đi
        - Cần xem xét thay đổi kháng sinh
        """)
    
    st.markdown("---")
    
    # ========== SECTION 7: SPECIAL POPULATIONS ==========
    st.markdown("### 👥 Special Populations")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Người cao tuổi (≥65):**
        - Tăng nguy cơ biến chứng
        - Cân nhắc nhập viện sớm
        - Theo dõi chức năng thận
        
        **Suy thận:**
        - Điều chỉnh liều theo CrCl
        - Tránh aminoglycoside nếu có thể
        """)
    
    with col2:
        st.markdown("""
        **Có thai:**
        - Tránh fluoroquinolone, tetracycline
        - Dùng beta-lactam + macrolide an toàn
        
        **Dị ứng penicillin:**
        - Dùng fluoroquinolone
        - Hoặc clindamycin + macrolide
        """)
    
    st.markdown("---")
    
    # ========== SECTION 8: REFERENCES ==========
    st.markdown("### 📚 References")
    
    st.markdown("""
    1. **IDSA/ATS 2019 Guidelines** - Community-Acquired Pneumonia in Adults
       - Metlay JP, et al. Diagnosis and Treatment of Adults with Community-acquired Pneumonia. An Official Clinical Practice Guideline of the American Thoracic Society and Infectious Diseases Society of America. Am J Respir Crit Care Med. 2019;200(7):e45-e67.
    
    2. **UpToDate:** Community-acquired pneumonia in adults - Last updated 2024
    
    3. **CURB-65 Score:**
       - Lim WS, et al. Defining community acquired pneumonia severity on presentation to hospital: an international derivation and validation study. Thorax. 2003;58(5):377-382.
    """)
    
    st.markdown("---")
    
    # Footer
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể, kháng sinh đồ địa phương, và guidelines mới nhất.")

