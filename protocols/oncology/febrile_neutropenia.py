"""
Febrile Neutropenia Management Protocol
IDSA 2010, ASCO 2018 Guidelines
Management of febrile neutropenia in cancer patients
"""

import streamlit as st


def render():
    """Febrile Neutropenia Management Protocol"""
    st.subheader("🌡️ Febrile Neutropenia Management")
    st.caption("IDSA 2010, ASCO 2018 Guidelines - Management of febrile neutropenia")
    
    st.error("""
    **⚠️ CẤP CỨU - Cần điều trị ngay lập tức**
    
    **Febrile Neutropenia là tình trạng:**
    - Sốt ≥38.3°C (hoặc ≥38.0°C kéo dài >1h)
    - VÀ Neutrophil <500/µL (hoặc <1000/µL và dự kiến giảm <500)
    - Nguy cơ nhiễm trùng huyết đe dọa tính mạng
    - Cần kháng sinh phổ rộng ngay
    """)
    
    st.markdown("---")
    
    # ========== SECTION 1: DEFINITION ==========
    st.markdown("### 📋 Định Nghĩa")
    
    with st.expander("🔍 Xem định nghĩa chi tiết", expanded=True):
        st.markdown("""
        **Febrile Neutropenia khi có:**
        
        **1. Sốt:**
        - Nhiệt độ ≥38.3°C (một lần)
        - Hoặc ≥38.0°C kéo dài >1 giờ
        
        **2. Neutropenia:**
        - Absolute Neutrophil Count (ANC) <500/µL
        - Hoặc <1000/µL và dự kiến giảm <500 trong 48h
        
        **ANC = WBC × (%Neutrophils + %Bands) / 100**
        
        **⚠️ Lưu ý:**
        - Không chờ kết quả cấy máu để bắt đầu kháng sinh
        - Điều trị ngay khi nghi ngờ
        - Tỷ lệ tử vong cao nếu không điều trị kịp thời
        """)
    
    st.markdown("---")
    
    # ========== SECTION 2: RISK STRATIFICATION ==========
    st.markdown("### 📊 Phân Tầng Nguy Cơ (MASCC Score)")
    
    st.markdown("""
    **MASCC (Multinational Association for Supportive Care in Cancer) Risk Index:**
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Tính điểm MASCC:**")
        
        burden = st.selectbox(
            "1. Burden of illness:",
            ["Không có triệu chứng (5 điểm)", "Triệu chứng nhẹ (3 điểm)", "Triệu chứng nặng (0 điểm)"],
            key="mascc_burden"
        )
        burden_score = 5 if "Không có" in burden else (3 if "nhẹ" in burden else 0)
        
        hypotension = st.checkbox("2. Không có hạ huyết áp (5 điểm)", key="mascc_hypotension")
        hypotension_score = 5 if hypotension else 0
        
        copd = st.checkbox("3. Không có COPD (4 điểm)", key="mascc_copd")
        copd_score = 4 if copd else 0
        
        solid_tumor = st.checkbox("4. Solid tumor hoặc không có nấm (4 điểm)", key="mascc_tumor")
        tumor_score = 4 if solid_tumor else 0
        
        dehydration = st.checkbox("5. Không có mất nước (3 điểm)", key="mascc_dehydration")
        dehydration_score = 3 if dehydration else 0
        
        outpatient = st.checkbox("6. Đang điều trị ngoại trú (3 điểm)", key="mascc_outpatient")
        outpatient_score = 3 if outpatient else 0
        
        age = st.checkbox("7. Tuổi <60 (2 điểm)", key="mascc_age")
        age_score = 2 if age else 0
    
    with col2:
        total_score = burden_score + hypotension_score + copd_score + tumor_score + dehydration_score + outpatient_score + age_score
        
        st.markdown("### 📊 Kết Quả:")
        st.metric("MASCC Score", f"{total_score}/26")
        
        if total_score >= 21:
            st.success("""
            **✅ LOW RISK (≥21 điểm):**
            - Tỷ lệ biến chứng: <5%
            - Tỷ lệ tử vong: <1%
            - **Có thể điều trị ngoại trú** (nếu đủ điều kiện)
            """)
        else:
            st.error("""
            **🚨 HIGH RISK (<21 điểm):**
            - Tỷ lệ biến chứng: 10-20%
            - Tỷ lệ tử vong: 5-10%
            - **Cần nhập viện điều trị**
            """)
    
    st.markdown("---")
    
    # ========== SECTION 3: INITIAL EVALUATION ==========
    st.markdown("### 🔍 Đánh Giá Ban Đầu")
    
    st.markdown("""
    **1. History & Physical:**
    - Triệu chứng nhiễm trùng (ho, khó thở, đau bụng, tiểu buốt)
    - Dấu hiệu nhiễm trùng (phát ban, loét miệng, catheter site)
    - Tiền sử nhiễm trùng trước đó
    - Thuốc đang dùng (kháng sinh, antifungals)
    
    **2. Laboratory:**
    - **CBC with differential** (ANC calculation)
    - **Blood cultures** (2 sets: peripheral + catheter nếu có)
    - **CMP** (creatinine, liver function)
    - **CRP, Procalcitonin** (nếu có)
    
    **3. Imaging:**
    - **Chest X-ray** (nếu có triệu chứng hô hấp)
    - **CT scan** (nếu nghi ngờ nhiễm trùng sâu)
    
    **4. Other cultures:**
    - **Urine culture** (nếu có triệu chứng tiết niệu)
    - **Sputum culture** (nếu có ho, đờm)
    - **Stool culture** (nếu có tiêu chảy)
    """)
    
    st.markdown("---")
    
    # ========== SECTION 4: EMPIRIC ANTIBIOTIC THERAPY ==========
    st.markdown("### 💊 Kháng Sinh Điều Trị Ban Đầu (Empiric Therapy)")
    
    st.error("""
    **⚠️ QUAN TRỌNG: Bắt đầu kháng sinh NGAY, không chờ kết quả cấy máu**
    """)
    
    risk_level = st.radio(
        "**Mức độ nguy cơ:**",
        ["High Risk (MASCC <21)", "Low Risk (MASCC ≥21)"],
        key="fn_risk"
    )
    
    st.markdown("---")
    
    if "High" in risk_level:
        render_high_risk_antibiotics()
    else:
        render_low_risk_antibiotics()
    
    st.markdown("---")
    
    # ========== SECTION 5: ANTIFUNGAL THERAPY ==========
    st.markdown("### 🦠 Điều Trị Kháng Nấm (Antifungal Therapy)")
    
    st.markdown("""
    **Empiric antifungal therapy nếu:**
    - Sốt kéo dài >4-7 ngày dù đã dùng kháng sinh phổ rộng
    - Nghi ngờ nấm xâm lấn
    - Nguy cơ cao (AML, allogeneic HSCT, prolonged neutropenia)
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("""
        **Caspofungin (Lựa chọn hàng đầu):**
        - **Loading:** 70mg IV × 1
        - **Maintenance:** 50mg IV/ngày
        - Phổ rộng, ít tác dụng phụ
        
        **Micafungin:**
        - **100mg IV/ngày**
        - Tương tự caspofungin
        
        **Anidulafungin:**
        - **Loading:** 200mg IV × 1
        - **Maintenance:** 100mg IV/ngày
        """)
    
    with col2:
        st.info("""
        **Voriconazole (Nếu nghi ngờ Aspergillus):**
        - **Loading:** 6 mg/kg IV q12h × 2 liều
        - **Maintenance:** 4 mg/kg IV q12h
        - Hoặc 200mg PO BID
        
        **Amphotericin B (Liposomal):**
        - **3-5 mg/kg IV/ngày**
        - Dùng nếu không dung nạp echinocandins
        - Theo dõi độc thận
        """)
    
    st.markdown("---")
    
    # ========== SECTION 6: DURATION OF THERAPY ==========
    st.markdown("### ⏱️ Thời Gian Điều Trị")
    
    st.markdown("""
    **1. Nếu afebrile và ANC >500:**
    - Tiếp tục kháng sinh đến khi ANC >500 và afebrile 24-48h
    - Tổng thời gian: Thường 7-14 ngày
    
    **2. Nếu afebrile nhưng ANC vẫn <500:**
    - Tiếp tục kháng sinh đến khi ANC >500
    - Có thể xuất viện nếu ổn định và low risk
    
    **3. Nếu vẫn sốt:**
    - Đánh giá lại sau 48-72h
    - Thêm/đổi kháng sinh nếu cần
    - Thêm kháng nấm nếu >4-7 ngày
    - Xem xét thêm kháng virus (acyclovir) nếu nghi ngờ
    
    **4. Nếu có nhiễm trùng xác định:**
    - Điều trị theo pathogen
    - Thời gian tùy theo loại nhiễm trùng
    """)
    
    st.markdown("---")
    
    # ========== SECTION 7: OUTPATIENT MANAGEMENT ==========
    st.markdown("### 🏠 Điều Trị Ngoại Trú (Low Risk)")
    
    st.success("""
    **Chỉ định (Tất cả phải thỏa):**
    - MASCC ≥21 (low risk)
    - Không có triệu chứng nặng
    - Không có hạ huyết áp
    - Không có bệnh lý nặng kèm theo
    - Có thể theo dõi sát (tái khám hàng ngày)
    - Có thể liên lạc 24/7
    
    **Regimen:**
    - **Ciprofloxacin 750mg PO BID** + **Amoxicillin-clavulanate 875/125mg PO BID**
    - Hoặc **Levofloxacin 750mg PO QD** (nếu không có penicillin allergy)
    - Hoặc **Ceftriaxone 2g IV/ngày** (có thể tiêm tại nhà)
    
    **Monitoring:**
    - Tái khám hàng ngày
    - Theo dõi nhiệt độ, triệu chứng
    - Xét nghiệm nếu cần
    
    **Nhập viện nếu:**
    - Sốt không hạ sau 48h
    - Triệu chứng nặng lên
    - Không thể uống thuốc
    - Có biến chứng
    """)
    
    st.markdown("---")
    
    # ========== SECTION 8: SPECIAL CONSIDERATIONS ==========
    st.markdown("### 👥 Các Trường Hợp Đặc Biệt")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Penicillin Allergy:**
        - Dùng Aztreonam + Vancomycin
        - Hoặc Ciprofloxacin + Clindamycin
        - Tránh cephalosporins nếu phản ứng nặng
        
        **MRSA Risk:**
        - Thêm Vancomycin
        - Hoặc Linezolid, Daptomycin
        
        **ESBL Risk:**
        - Dùng Carbapenem (Meropenem, Imipenem)
        - Hoặc Ceftazidime-avibactam
        """)
    
    with col2:
        st.markdown("""
        **Pneumonia:**
        - Thêm coverage cho atypical (Azithromycin)
        - Hoặc Levofloxacin/Moxifloxacin
        
        **Abdominal Source:**
        - Thêm Metronidazole (anaerobic coverage)
        - Hoặc Piperacillin-tazobactam
        
        **Catheter-related:**
        - Cân nhắc thay catheter
        - Thêm Vancomycin (coverage S. aureus)
        """)
    
    st.markdown("---")
    
    # ========== SECTION 9: REFERENCES ==========
    st.markdown("### 📚 Tài Liệu Tham Khảo")
    
    st.markdown("""
    1. **IDSA Clinical Practice Guideline** - Management of Cancer Patients with Febrile Neutropenia (2010)
       - Risk stratification
       - Empiric antibiotic therapy
       - Duration of treatment
    
    2. **ASCO Clinical Practice Guideline** - Antimicrobial Prophylaxis for Adult Patients with Cancer (2018)
       - Prevention strategies
       - Treatment protocols
    
    3. **UpToDate:** Febrile Neutropenia - Last updated 2024
       - Clinical features and diagnosis
       - Treatment protocols
    
    4. **Klastersky J, et al.** The Multinational Association for Supportive Care in Cancer risk index: A multinational scoring system for identifying low-risk febrile neutropenic cancer patients.
       J Clin Oncol. 2000;18(16):3038-3051.
    """)
    
    st.markdown("---")
    
    # Footer
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất. Febrile Neutropenia là cấp cứu, cần điều trị kháng sinh ngay lập tức.")


def render_high_risk_antibiotics():
    """High Risk Febrile Neutropenia Antibiotic Regimens"""
    st.error("## 🚨 HIGH RISK - Nhập Viện Điều Trị")
    
    st.markdown("""
    **Regimen 1: Monotherapy (Lựa chọn hàng đầu)**
    
    **Piperacillin-tazobactam:**
    - 4.5g IV q6h
    - Phổ rộng: Gram+, Gram-, Anaerobic
    
    **Hoặc Cefepime:**
    - 2g IV q8h
    - Phổ rộng: Gram+, Gram-
    
    **Hoặc Ceftazidime:**
    - 2g IV q8h
    - Phổ rộng: Gram-, Pseudomonas
    
    **Hoặc Meropenem:**
    - 1g IV q8h
    - Phổ rộng nhất, dùng nếu ESBL risk
    
    **Hoặc Imipenem-cilastatin:**
    - 500mg IV q6h
    - Tương tự meropenem
    """)
    
    st.markdown("---")
    
    st.warning("""
    **Regimen 2: Dual Therapy (Nếu có nguy cơ cao)**
    
    **A. Beta-lactam + Aminoglycoside:**
    - Piperacillin-tazobactam 4.5g IV q6h
    - + Gentamicin 5-7 mg/kg IV/ngày
    - Hoặc Tobramycin, Amikacin
    
    **B. Beta-lactam + Vancomycin (Nếu MRSA risk):**
    - Piperacillin-tazobactam 4.5g IV q6h
    - + Vancomycin 15-20 mg/kg IV q8-12h (trough 15-20)
    
    **C. Beta-lactam + Fluoroquinolone:**
    - Piperacillin-tazobactam 4.5g IV q6h
    - + Ciprofloxacin 400mg IV q8h
    """)
    
    st.info("""
    **Lựa chọn regimen dựa trên:**
    - Local resistance patterns
    - Patient risk factors
    - Previous infections
    - Hospital formulary
    """)


def render_low_risk_antibiotics():
    """Low Risk Febrile Neutropenia Antibiotic Regimens"""
    st.success("## ✅ LOW RISK - Có Thể Điều Trị Ngoại Trú")
    
    st.markdown("""
    **Regimen 1: Oral (Nếu có thể uống):**
    
    **Ciprofloxacin + Amoxicillin-clavulanate:**
    - Ciprofloxacin 750mg PO BID
    - + Amoxicillin-clavulanate 875/125mg PO BID
    
    **Hoặc Levofloxacin:**
    - 750mg PO QD
    - (Nếu không có penicillin allergy)
    """)
    
    st.markdown("---")
    
    st.info("""
    **Regimen 2: IV Outpatient (Nếu không uống được):**
    
    **Ceftriaxone:**
    - 2g IV/ngày
    - Có thể tiêm tại nhà hoặc clinic
    
    **Hoặc Ertapenem:**
    - 1g IV/ngày
    - Phổ rộng hơn
    """)
    
    st.warning("""
    **⚠️ Lưu ý:**
    - Chỉ dùng nếu đủ điều kiện điều trị ngoại trú
    - Phải có khả năng tái khám hàng ngày
    - Phải có khả năng liên lạc 24/7
    - Nhập viện ngay nếu không cải thiện sau 48h
    """)

