"""
Glasgow-Blatchford Score (GBS)
Đánh giá nguy cơ cần can thiệp trong xuất huyết tiêu hóa trên

Used to identify low-risk patients who can be safely discharged
Score 0 = Very low risk, can discharge
Score ≥1 = Consider admission

Reference:
Blatchford O, et al. A risk score to predict need for treatment for upper-gastrointestinal haemorrhage.
Lancet. 2000;356(9238):1318-21.
"""

import streamlit as st


def _format_num(value: float, decimals: int = 1) -> str:
    """Format số, loại bỏ số 0 thừa"""
    rounded = round(value, decimals)
    if rounded == int(rounded):
        return str(int(rounded))
    return f"{rounded:.{decimals}f}".rstrip('0').rstrip('.')


def calculate_gbs(
    bun_mgdl, hgb, sbp, hr, melena, syncope, liver_disease, heart_failure, gender
):
    """Calculate Glasgow-Blatchford Score"""
    score = 0
    
    # BUN (Blood Urea Nitrogen)
    if bun_mgdl >= 150:  # ≥25 mg/dL
        score += 6
    elif bun_mgdl >= 100:  # 18.2-24.9 mg/dL
        score += 4
    elif bun_mgdl >= 70:  # 12.7-18.1 mg/dL
        score += 3
    elif bun_mgdl >= 39:  # 6.5-12.6 mg/dL
        score += 2
    
    # Hemoglobin
    if gender == "Nam":
        if hgb < 10.0:
            score += 6
        elif hgb < 12.0:
            score += 3
        elif hgb < 13.0:
            score += 1
    else:  # Nữ
        if hgb < 10.0:
            score += 6
        elif hgb < 12.0:
            score += 1
    
    # Systolic BP
    if sbp < 90:
        score += 3
    elif sbp < 100:
        score += 2
    elif sbp < 110:
        score += 1
    
    # Heart Rate
    if hr >= 100:
        score += 1
    
    # Melena
    if melena:
        score += 1
    
    # Syncope
    if syncope:
        score += 2
    
    # Liver disease
    if liver_disease:
        score += 2
    
    # Heart failure
    if heart_failure:
        score += 2
    
    return score


def render():
    """Render Glasgow-Blatchford Score Calculator"""
    
    st.subheader("🩸 Glasgow-Blatchford Score (GBS)")
    st.caption("Đánh giá nguy cơ xuất huyết tiêu hóa trên cần can thiệp")
    
    st.markdown("""
    **Glasgow-Blatchford Score** giúp xác định bệnh nhân UGIB nguy cơ thấp 
    có thể xuất viện an toàn.
    
    **Ứng dụng:**
    - **GBS = 0:** Nguy cơ rất thấp, có thể xuất viện
    - **GBS ≥ 1:** Cân nhắc nhập viện
    - Dự đoán cần can thiệp (nội soi cầm máu, phẫu thuật, truyền máu)
    """)
    
    st.markdown("---")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📋 Thông Tin Bệnh Nhân")
        
        # Gender
        gender = st.radio(
            "**Giới tính:**",
            ["Nam", "Nữ"],
            horizontal=True
        )
        
        st.markdown("---")
        st.markdown("### 🔬 Xét nghiệm")
        
        # BUN
        st.markdown("#### 1. Urea (BUN)")
        bun_unit = st.radio(
            "Đơn vị:",
            ["mmol/L (SI)", "mg/dL"],
            horizontal=True,
            index=0,
            key="bun_gbs"
        )
        
        if "mmol/L" in bun_unit:
            bun_mmol = st.number_input(
                "BUN (mmol/L):",
                min_value=0.0,
                max_value=70.0,
                value=5.0,
                step=0.1,
                format="%.1f",
                help="Bình thường: 2.5-7.1 mmol/L"
            )
            bun_mgdl = bun_mmol * 2.8
            st.caption(f"≈ {_format_num(bun_mgdl, 1)} mg/dL")
        else:
            bun = st.number_input(
                "BUN (mg/dL):",
                min_value=0.0,
                max_value=200.0,
                value=15.0,
                step=1.0,
                format="%.0f",
                help="Bình thường: 7-20 mg/dL"
            )
            bun_mgdl = bun
            st.caption(f"≈ {_format_num(bun / 2.8, 1)} mmol/L")
        
        # Hemoglobin
        st.markdown("#### 2. Hemoglobin")
        hgb = st.number_input(
            "Hemoglobin (g/dL):",
            min_value=3.0,
            max_value=20.0,
            value=13.0,
            step=0.1,
            help="Nam: 13.5-17.5 g/dL, Nữ: 12.0-15.5 g/dL"
        )
        st.caption(f"≈ {round(hgb * 10)} g/L")
        
        st.markdown("---")
        st.markdown("### 🩺 Sinh hiệu")
        
        # SBP
        sbp = st.number_input(
            "**Huyết áp tâm thu (mmHg):**",
            min_value=50,
            max_value=250,
            value=120,
            step=5
        )
        
        # Heart Rate
        hr = st.number_input(
            "**Nhịp tim (lần/phút):**",
            min_value=30,
            max_value=200,
            value=80,
            step=5
        )
        
        st.markdown("---")
        st.markdown("### 📋 Lâm Sàng")
        
        # Melena
        melena = st.checkbox(
            "**Phân đen (Melena)**",
            help="Phân đen hắc ín (melena) +1 điểm"
        )
        
        # Syncope
        syncope = st.checkbox(
            "**Ngất (Syncope)**",
            help="Có tiền sử ngất +2 điểm"
        )
        
        # Liver disease
        liver_disease = st.checkbox(
            "**Bệnh gan**",
            help="Tiền sử bệnh gan mạn +2 điểm"
        )
        
        # Heart failure
        heart_failure = st.checkbox(
            "**Suy tim**",
            help="Tiền sử suy tim +2 điểm"
        )
        
        st.markdown("---")
        
        if st.button("🧮 Tính Glasgow-Blatchford Score", type="primary", use_container_width=True):
            # Calculate score
            gbs = calculate_gbs(
                bun_mgdl, hgb, sbp, hr, melena, syncope, 
                liver_disease, heart_failure, gender
            )
            
            # Determine risk
            if gbs == 0:
                risk = "RẤT THẤP"
                color = "green"
                recommendation = "Xuất viện an toàn"
                intervention_risk = "<1%"
                mortality = "<0.5%"
            elif gbs <= 1:
                risk = "THẤP"
                color = "green"
                recommendation = "Có thể xuất viện sớm"
                intervention_risk = "~2%"
                mortality = "<0.5%"
            elif gbs <= 3:
                risk = "TRUNG BÌNH THẤP"
                color = "info"
                recommendation = "Nhập viện theo dõi"
                intervention_risk = "~5%"
                mortality = "~1%"
            elif gbs <= 6:
                risk = "TRUNG BÌNH"
                color = "warning"
                recommendation = "Nhập viện, nội soi sớm"
                intervention_risk = "~15%"
                mortality = "~2%"
            else:
                risk = "CAO"
                color = "error"
                recommendation = "Nhập viện/ICU, can thiệp khẩn cấp"
                intervention_risk = ">30%"
                mortality = ">5%"
            
            with col2:
                st.markdown("### 📊 Kết quả")
                
                if color == "green":
                    st.success(f"## GBS = {gbs}")
                    st.success(f"**Nguy cơ {risk}**")
                elif color == "info":
                    st.info(f"## GBS = {gbs}")
                    st.info(f"**Nguy cơ {risk}**")
                elif color == "warning":
                    st.warning(f"## GBS = {gbs}")
                    st.warning(f"**Nguy cơ {risk}**")
                else:
                    st.error(f"## GBS = {gbs}")
                    st.error(f"**Nguy cơ {risk}**")
                
                st.markdown(f"""
                **Nguy cơ can thiệp:** {intervention_risk}
                
                **Tử vong:** {mortality}
                """)
            
            st.markdown("---")
            st.markdown("### 💊 KHUYẾN CÁO XỬ TRÍ")
            
            if gbs == 0:
                st.success(f"""
                **🟢 GBS = 0 - NGUY CƠ RẤT THẤP**
                
                **Nguy cơ:**
                - Cần can thiệp: <1%
                - Tử vong: <0.5%
                
                **Khuyến nghị:**
                
                1. **✅ Có thể XUẤT VIỆN an toàn**
                   - Không cần nội soi cấp cứu
                   - Không cần nhập viện thường quy
                   - Theo dõi ngoại trú
                
                2. **Điều kiện xuất viện:**
                   - Không nôn máu/phân máu đang hoạt động
                   - Sinh hiệu ổn định
                   - Không có comorbidities nặng khác
                   - Có người chăm sóc tại nhà
                   - Có thể quay lại BV nếu cần
                
                3. **Kế hoạch ngoại trú:**
                   - **PPI** liều cao: Omeprazole 40mg BID × 3 ngày, sau đó 20mg daily
                   - **Tái khám** sau 1-2 ngày
                   - **Nội soi** sau 1-2 tuần (không cấp cứu)
                   - **Giáo dục** dấu hiệu cần quay lại: nôn máu, phân đen, chóng mặt
                
                4. **Tư vấn:**
                   - Tránh NSAIDs, aspirin (trừ chỉ định bắt buộc)
                   - Tránh rượu
                   - Ăn nhẹ, dễ tiêu
                   - Test H. pylori và điều trị nếu dương tính
                
                **Lưu ý:** GBS = 0 có độ tin cậy rất cao để loại trừ cần can thiệp.
                """)
            
            elif gbs <= 1:
                st.success(f"""
                **🟢 GBS = {gbs} - NGUY CƠ THẤP**
                
                **Nguy cơ:**
                - Cần can thiệp: ~2%
                - Tử vong: <0.5%
                
                **Khuyến nghị:**
                
                1. **Nhập viện ngắn ngày hoặc Observation Unit:**
                   - Theo dõi 12-24h
                   - Không cần ICU
                
                2. **Điều trị ban đầu:**
                   - **PPI IV:** Pantoprazole 80mg IV bolus, sau đó 8mg/h × 72h
                   - Hoặc Omeprazole 80mg IV bolus, sau đó 8mg/h
                   - **NPO** cho đến khi ổn định
                   - **IV fluid:** Resuscitation nếu cần
                
                3. **Nội soi:**
                   - Không cần URGENT
                   - Có thể làm trong 24h
                   - Hoặc ngoại trú trong vài ngày nếu ổn định
                
                4. **Theo dõi:**
                   - Vital signs q4-6h
                   - CBC lặp lại sau 6-12h
                   - Đánh giá lại cho xuất viện nếu:
                     * Không chảy máu thêm
                     * Hgb ổn định
                     * Sinh hiệu ổn
                
                5. **Xuất viện:**
                   - PPI: Omeprazole 40mg BID × 14 ngày
                   - Tái khám sau 1 tuần
                   - H. pylori test & treat
                
                **Tiên lượng:** Rất tốt. Hầu hết không cần can thiệp.
                """)
            
            elif gbs <= 6:
                st.warning(f"""
                **🟡 GBS = {gbs} - NGUY CƠ TRUNG BÌNH**
                
                **Nguy cơ:**
                - Cần can thiệp: ~{intervention_risk}
                - Tử vong: ~{mortality}
                
                **Khuyến nghị:**
                
                1. **NHẬP VIỆN - Khoa Tiêu Hóa:**
                   - Theo dõi sát
                   - Không nhất thiết ICU (trừ không ổn định)
                
                2. **Hồi sức ban đầu:**
                   - **IV access:** 2 đường truyền cỡ lớn (18G)
                   - **IV fluid:** Crystalloid để duy trì BP
                   - **PPI IV:** Pantoprazole 80mg bolus → 8mg/h × 72h
                   - **NPO** ban đầu
                   - **Transfusion:** Nếu Hgb <7-8 g/dL
                     * Mục tiêu: Hgb >7 g/dL (hoặc >8 nếu CAD)
                     * Tránh transfusion quá mức (tăng áp lực portal)
                
                3. **Nội soi:**
                   - **Nội soi trong 24h**
                   - Không cần siêu khẩn cấp (trừ hemodynamic instability)
                   - Pre-endoscopy: Erythromycin 250mg IV (giúp làm sạch dạ dày)
                
                4. **Theo dõi:**
                   - Vital signs q2-4h
                   - CBC mỗi 6-12h
                   - Đánh giá lại GBS sau resuscitation
                
                5. **Can thiệp nội soi nếu cần:**
                   - **Variceal bleeding:** Band ligation, sclerotherapy
                   - **Peptic ulcer:**
                     * Forrest Ia-IIb: Epinephrine + (thermal/clip)
                     * High-risk stigmata: Combination therapy
                   - **Mallory-Weiss:** Thường tự cầm
                
                6. **Điều trị sau nội soi:**
                   - PPI IV × 72h → chuyển PO
                   - H. pylori test (biopsy/CLO test)
                   - Điều trị theo nguyên nhân
                
                **Tiên lượng:** Trung bình. Phần lớn hồi phục tốt với điều trị.
                """)
            
            else:  # GBS > 6
                st.error(f"""
                **🔴 GBS = {gbs} - NGUY CƠ CAO** 🚨
                
                **Nguy cơ:**
                - Cần can thiệp: >30%
                - Tử vong: >5%
                
                **Khuyến nghị:**
                
                1. **KHẨN CẤP - ICU hoặc High-Dependency Unit:**
                   - Monitoring liên tục
                   - Sẵn sàng can thiệp
                
                2. **Hồi sức tích cực:**
                   
                   **ABC - Airway, Breathing, Circulation:**
                   - **Airway:** Cân nhắc intubation nếu:
                     * Massive hematemesis
                     * Altered mental status
                     * Nguy cơ aspiration cao
                   - **Breathing:** O₂ để duy trì SpO₂ >94%
                   - **Circulation:**
                     * **2 IV lines 18G** (hoặc central line)
                     * **Crystalloid:** Bolus 500ml-1L nhanh
                     * Mục tiêu: MAP >65 mmHg, UO >0.5ml/kg/h
                   
                   **Truyền máu:**
                   - **PRBC:** Nếu Hgb <7 g/dL (hoặc <8 nếu CAD/instability)
                   - **Mục tiêu:** Hgb 7-9 g/dL
                   - **Tránh over-transfusion** (tăng pressure, tăng rebleeding)
                   - **FFP:** Nếu INR >1.5-2.0 và chảy máu active
                   - **Platelet:** Nếu <50,000 và chảy máu active
                   
                   **PPI liều cao:**
                   - **Pantoprazole 80mg IV bolus** → 8mg/h infusion
                   - Bắt đầu NGAY, trước nội soi
                   
                   **Nếu nghi variceal bleeding:**
                   - **Octreotide:** 50µg IV bolus → 50µg/h infusion
                   - Hoặc Terlipressin 2mg IV q4h
                   - **Antibiotic prophylaxis:** Ceftriaxone 1g IV q24h
                   - **Vitamin K:** 10mg IV (nếu bệnh gan)
                
                3. **Nội soi KHẨN CẤP:**
                   - **Trong 12h** (hoặc sớm hơn nếu không ổn định)
                   - Pre-procedure:
                     * NGT aspiration (nếu cần)
                     * Erythromycin 250mg IV (làm sạch dạ dày)
                     * Consent + giải thích nguy cơ
                   - **Sẵn sàng can thiệp:**
                     * Endoscopic hemostasis (injection, thermal, clip)
                     * Band ligation/sclerotherapy (varix)
                
                4. **Nếu thất bại nội soi:**
                   - **Balloon tamponade** (Sengstaken-Blakemore) - tạm thời
                   - **Interventional radiology:** Embolization
                   - **TIPS** (nếu variceal bleeding không kiểm soát)
                   - **Phẫu thuật** (last resort)
                
                5. **Theo dõi sau can thiệp:**
                   - ICU × 24-48h
                   - Vital signs liên tục
                   - CBC q4-6h
                   - NGT output monitoring
                   - PPI IV × 72h
                
                6. **Prophylaxis thứ phát:**
                   - **Nếu variceal bleeding:**
                     * Beta-blocker (Propranolol, Carvedilol)
                     * Band ligation mỗi 2-4 tuần đến obliteration
                   - **Nếu peptic ulcer:**
                     * PPI dài hạn
                     * H. pylori eradication
                     * Tránh NSAIDs
                
                **Tiên lượng:** Xấu. Cần can thiệp tích cực và theo dõi sát.
                Nguy cơ tái chảy máu và tử vong cao.
                """)
            
            # Score breakdown
            st.markdown("---")
            with st.expander("📊 Chi tiết điểm số"):
                st.markdown(f"""
                **Glasgow-Blatchford Score = {gbs}**
                
                **Thành phần:**
                - BUN: {bun_mgdl:.0f} mg/dL
                - Hemoglobin: {hgb:.1f} g/dL ({gender})
                - SBP: {sbp} mmHg
                - Nhịp tim: {hr} bpm
                - Melena: {"Có" if melena else "Không"}
                - Syncope: {"Có" if syncope else "Không"}
                - Bệnh gan: {"Có" if liver_disease else "Không"}
                - Suy tim: {"Có" if heart_failure else "Không"}
                """)
            
            with st.expander("📈 Bảng Chấm Điểm Glasgow-Blatchford"):
                st.markdown("""
                | Yếu Tố | Tiêu Chuẩn | Điểm |
                |--------|-----------|------|
                | **BUN (mg/dL)** | ≥150 (≥25 mmol/L) | 6 |
                | | 100-149.9 (18.2-24.9) | 4 |
                | | 70-99.9 (12.7-18.1) | 3 |
                | | 39-69.9 (6.5-12.6) | 2 |
                | | <39 (<6.5) | 0 |
                | **Hemoglobin (g/dL)** | |
                | Nam | <10.0 | 6 |
                | | 10.0-11.9 | 3 |
                | | 12.0-12.9 | 1 |
                | | ≥13.0 | 0 |
                | Nữ | <10.0 | 6 |
                | | 10.0-11.9 | 1 |
                | | ≥12.0 | 0 |
                | **SBP (mmHg)** | <90 | 3 |
                | | 90-99 | 2 |
                | | 100-109 | 1 |
                | | ≥110 | 0 |
                | **Nhịp tim** | ≥100 bpm | 1 |
                | | <100 bpm | 0 |
                | **Melena** | Có | 1 |
                | **Syncope** | Có | 2 |
                | **Bệnh gan** | Có | 2 |
                | **Suy tim** | Có | 2 |
                
                **Tổng điểm: 0-23**
                """)
            
            with st.expander("🔄 GBS vs Rockall Score"):
                st.markdown("""
                **So sánh hai thang điểm UGIB:**
                
                | Đặc điểm | Glasgow-Blatchford | Rockall |
                |----------|-------------------|---------|
                | **Thời điểm** | Pre-endoscopy | Pre + Post-endoscopy |
                | **Mục đích chính** | Discharge decision | Mortality prediction |
                | **Điểm cắt** | 0 = safe discharge | Không có cutoff rõ |
                | **Can thiệp** | Dự đoán tốt | Dự đoán kém hơn |
                | **Tử vong** | Dự đoán khá | Dự đoán tốt hơn |
                | **Đơn giản** | ✅ Không cần nội soi | ❌ Cần nội soi |
                | **Khuyến nghị** | Use for discharge | Use for prognosis |
                
                **Khuyến nghị sử dụng:**
                - **GBS:** ED/admission decision, identify low-risk
                - **Rockall:** Post-endoscopy prognosis
                - **Kết hợp cả hai** cho đánh giá toàn diện
                """)
            
            with st.expander("📚 Tài liệu tham khảo"):
                st.markdown("""
                **Primary Reference:**
                - Blatchford O, Murray WR, Blatchford M. 
                  *A risk score to predict need for treatment for upper-gastrointestinal haemorrhage.* 
                  Lancet. 2000 Oct 14;356(9238):1318-21. [PMID: 11073021]
                
                **Validation Studies:**
                - Stanley AJ, Ashley D, Dalton HR, et al. 
                  *Outpatient management of patients with low-risk upper-gastrointestinal haemorrhage: multicentre validation and prospective evaluation.* 
                  Lancet. 2009 Jan 3;373(9657):42-7.
                
                - Saltzman JR, Tabak YP, Hyett BH, Sun X, Travis AC, Johannes RS. 
                  *A simple risk score accurately predicts in-hospital mortality, length of stay, and cost in acute upper GI bleeding.* 
                  Gastrointest Endosc. 2011 Dec;74(6):1215-24.
                
                - Bryant RV, Kuo P, Williamson K, et al. 
                  *Performance of the Glasgow-Blatchford score in predicting clinical outcomes and intervention in hospitalized patients with upper GI bleeding.* 
                  Gastrointest Endosc. 2013 Apr;77(4):576-83.
                
                **Guidelines:**
                - Gralnek IM, et al. *Nonvariceal upper gastrointestinal hemorrhage: ESGE Guideline.* 
                  Endoscopy. 2015 Oct;47(10):a1-46.
                
                - Barkun AN, et al. *International consensus recommendations on the management of patients with nonvariceal upper gastrointestinal bleeding.* 
                  Ann Intern Med. 2010 Jan 5;152(1):101-13.
                """)
    
    # Educational content
    st.markdown("---")
    st.markdown("### 📖 THÔNG TIN THÊM")
    
    with st.expander("❓ Glasgow-Blatchford Score là gì?"):
        st.markdown("""
        **Glasgow-Blatchford Score (GBS)** là thang điểm đánh giá nguy cơ 
        ở bệnh nhân xuất huyết tiêu hóa trên (UGIB).
        
        **Đặc điểm:**
        - Không cần nội soi (pre-endoscopy)
        - Dựa vào 8 yếu tố lâm sàng & xét nghiệm
        - Điểm 0-23
        
        **Ưu điểm:**
        - **GBS = 0** có độ tin cậy rất cao (NPV >99%)
        - Giúp discharge an toàn bệnh nhân nguy cơ thấp
        - Giảm chi phí, giảm tải bệnh viện
        - Validated rộng rãi
        
        **Ứng dụng chính:**
        - **Quyết định discharge** (GBS = 0)
        - **Quyết định admission** (GBS ≥1)
        - **Dự đoán cần can thiệp** (endoscopic, surgical, transfusion)
        
        **So với Rockall:**
        - GBS không cần nội soi → Dùng sớm hơn
        - GBS dự đoán can thiệp tốt hơn
        - Rockall dự đoán tử vong tốt hơn
        """)
    
    with st.expander("🩸 Xuất Huyết Tiêu Hóa Trên - Nguyên Nhân"):
        st.markdown("""
        **Nguyên nhân thường gặp UGIB:**
        
        **1. Pepticulcer (35-50%):**
        - Loét dạ dày, tá tràng
        - Liên quan H. pylori, NSAIDs
        - Phân loại Forrest:
          * Ia: Chảy máu phun (arterial)
          * Ib: Chảy máu rỉ (venous)
          * IIa: Mạch máu lộ (visible vessel)
          * IIb: Cục máu bám (adherent clot)
          * IIc: Đáy đen (black base)
          * III: Đã sạch (clean base)
        
        **2. Giãn tĩnh mạch thực quản (15-20%):**
        - Do tăng áp lực tĩnh mạch cửa
        - Xơ gan, thrombosis tĩnh mạch cửa/lách
        - Tử vong cao (10-20% mỗi đợt)
        
        **3. Mallory-Weiss tear (5-10%):**
        - Rách niêm mạc nối thực quản-dạ dày
        - Do nôn mạnh, ho
        - Thường tự cầm
        
        **4. Viêm dạ dày/tá tràng cấp (5-10%):**
        - Stress ulcer
        - NSAIDs, rượu
        
        **5. Dạ dày xuất huyết cấp (GAVE) (5%):**
        - "Watermelon stomach"
        - Bệnh mạch máu
        
        **6. Khác (10-15%):**
        - Ung thư dạ dày
        - Dieulafoy lesion
        - Angiodysplasia
        - Aortoenteric fistula
        """)
    
    with st.expander("💊 Điều trị PPI trong UGIB"):
        st.markdown("""
        **PPI (Proton Pump Inhibitor) trong UGIB:**
        
        **Cơ chế:**
        - Ức chế H⁺/K⁺-ATPase → giảm acid
        - Tạo môi trường pH cao → ổn định cục máu đông
        - Giảm pepsin activity
        
        **Liều trong UGIB:**
        - **IV bolus:** 80mg
        - **Infusion:** 8mg/h × 72h
        - **Sau đó:** PO 40mg BID × 14 ngày
        
        **Thuốc:**
        - Pantoprazole, Omeprazole, Esomeprazole
        - Tương đương nhau về hiệu quả
        
        **Thời điểm:**
        - Bắt đầu TRƯỚC nội soi
        - Tiếp tục sau nội soi 72h
        
        **Bằng chứng:**
        - Giảm rebleeding (NNT=20)
        - Giảm nhu cầu can thiệp
        - Không giảm tử vong (nhưng vẫn khuyến cáo dùng)
        
        **Sau điều trị cấp:**
        - PO 20-40mg daily
        - Thời gian tùy nguyên nhân:
          * H. pylori: Đến khi eradication
          * NSAIDs: Đến khi ngừng NSAIDs hoặc dùng dài hạn
          * Idiopathic: 4-8 tuần
        """)
    
    # Footer
    st.markdown("---")
    st.caption("📚 Based on: Blatchford O, et al. Lancet. 2000;356(9238):1318-21")
    st.caption("⚠️ Score 0 = Very low risk, can safely discharge")
    st.caption("🏥 Best validated score for identifying low-risk UGIB patients")

