"""
SOFA Score (Sequential Organ Failure Assessment)
=================================================

Multi-organ dysfunction assessment for ICU patients

Reference:
- Vincent JL, et al. The SOFA (Sepsis-related Organ Failure Assessment) score to
  describe organ dysfunction/failure. Intensive Care Med. 1996;22(7):707-710.
- Singer M, et al. The Third International Consensus Definitions for Sepsis and
  Septic Shock (Sepsis-3). JAMA. 2016;315(8):801-810.

SOFA Components (6 organ systems):
1. Respiratory: PaO₂/FiO₂ ratio
2. Coagulation: Platelets
3. Liver: Bilirubin
4. Cardiovascular: Mean arterial pressure (MAP) or vasopressors
5. Central Nervous System: Glasgow Coma Scale
6. Renal: Creatinine or urine output

Score: 0-4 points per organ system → Total: 0-24 points

Clinical Utility:
- Assess organ dysfunction severity
- Monitor disease progression
- Predict mortality in ICU
- Sepsis-3 definition: SOFA ≥2 = sepsis
"""

import streamlit as st


def calculate_sofa(
    pao2_fio2: float,
    platelets: float,
    bilirubin: float,
    map_value: float,
    use_vasopressor: bool,
    vasopressor_type: str,
    vasopressor_dose: float,
    gcs: int,
    creatinine: float,
    urine_output: float
) -> dict:
    """
    Calculate SOFA Score
    
    Args:
        pao2_fio2: PaO2/FiO2 ratio (mmHg)
        platelets: Platelet count (×10³/μL)
        bilirubin: Total bilirubin (mg/dL)
        map_value: Mean arterial pressure (mmHg)
        use_vasopressor: Whether patient is on vasopressors
        vasopressor_type: Type of vasopressor (dopamine/dobutamine/epi/norepi)
        vasopressor_dose: Vasopressor dose (mcg/kg/min)
        gcs: Glasgow Coma Scale
        creatinine: Serum creatinine (mg/dL)
        urine_output: Urine output (mL/day)
    
    Returns:
        Dictionary containing SOFA score, subscores, interpretation
    """
    
    subscores = {}
    details = []
    
    # 1. RESPIRATORY (PaO2/FiO2)
    if pao2_fio2 >= 400:
        subscores['respiratory'] = 0
        details.append(f"**Hô hấp:** PaO₂/FiO₂ = {pao2_fio2:.0f} → 0 điểm")
    elif pao2_fio2 >= 300:
        subscores['respiratory'] = 1
        details.append(f"**Hô hấp:** PaO₂/FiO₂ = {pao2_fio2:.0f} → 1 điểm")
    elif pao2_fio2 >= 200:
        subscores['respiratory'] = 2
        details.append(f"**Hô hấp:** PaO₂/FiO₂ = {pao2_fio2:.0f} → 2 điểm")
    elif pao2_fio2 >= 100:
        subscores['respiratory'] = 3
        details.append(f"**Hô hấp:** PaO₂/FiO₂ = {pao2_fio2:.0f} → 3 điểm")
    else:
        subscores['respiratory'] = 4
        details.append(f"**Hô hấp:** PaO₂/FiO₂ = {pao2_fio2:.0f} → 4 điểm")
    
    # 2. COAGULATION (Platelets)
    if platelets >= 150:
        subscores['coagulation'] = 0
        details.append(f"**Đông máu:** Tiểu cầu = {platelets:.0f} → 0 điểm")
    elif platelets >= 100:
        subscores['coagulation'] = 1
        details.append(f"**Đông máu:** Tiểu cầu = {platelets:.0f} → 1 điểm")
    elif platelets >= 50:
        subscores['coagulation'] = 2
        details.append(f"**Đông máu:** Tiểu cầu = {platelets:.0f} → 2 điểm")
    elif platelets >= 20:
        subscores['coagulation'] = 3
        details.append(f"**Đông máu:** Tiểu cầu = {platelets:.0f} → 3 điểm")
    else:
        subscores['coagulation'] = 4
        details.append(f"**Đông máu:** Tiểu cầu = {platelets:.0f} → 4 điểm")
    
    # 3. LIVER (Bilirubin)
    if bilirubin < 1.2:
        subscores['liver'] = 0
        details.append(f"**Gan:** Bilirubin = {bilirubin:.1f} → 0 điểm")
    elif bilirubin < 2.0:
        subscores['liver'] = 1
        details.append(f"**Gan:** Bilirubin = {bilirubin:.1f} → 1 điểm")
    elif bilirubin < 6.0:
        subscores['liver'] = 2
        details.append(f"**Gan:** Bilirubin = {bilirubin:.1f} → 2 điểm")
    elif bilirubin < 12.0:
        subscores['liver'] = 3
        details.append(f"**Gan:** Bilirubin = {bilirubin:.1f} → 3 điểm")
    else:
        subscores['liver'] = 4
        details.append(f"**Gan:** Bilirubin = {bilirubin:.1f} → 4 điểm")
    
    # 4. CARDIOVASCULAR
    if use_vasopressor:
        # On vasopressor
        if vasopressor_type == "Dopamine" and vasopressor_dose < 5:
            subscores['cardiovascular'] = 2
            details.append(f"**Tim mạch:** Dopamine <5 mcg/kg/min → 2 điểm")
        elif vasopressor_type == "Dopamine" and vasopressor_dose <= 15:
            subscores['cardiovascular'] = 3
            details.append(f"**Tim mạch:** Dopamine 5-15 mcg/kg/min → 3 điểm")
        elif vasopressor_type == "Dopamine" and vasopressor_dose > 15:
            subscores['cardiovascular'] = 4
            details.append(f"**Tim mạch:** Dopamine >15 mcg/kg/min → 4 điểm")
        elif vasopressor_type == "Dobutamine":
            subscores['cardiovascular'] = 2
            details.append(f"**Tim mạch:** Dobutamine (any dose) → 2 điểm")
        elif vasopressor_type in ["Epinephrine", "Norepinephrine"]:
            if vasopressor_dose <= 0.1:
                subscores['cardiovascular'] = 3
                details.append(f"**Tim mạch:** Epi/Norepi ≤0.1 mcg/kg/min → 3 điểm")
            else:
                subscores['cardiovascular'] = 4
                details.append(f"**Tim mạch:** Epi/Norepi >0.1 mcg/kg/min → 4 điểm")
    else:
        # No vasopressor - use MAP
        if map_value >= 70:
            subscores['cardiovascular'] = 0
            details.append(f"**Tim mạch:** MAP = {map_value:.0f} mmHg → 0 điểm")
        else:
            subscores['cardiovascular'] = 1
            details.append(f"**Tim mạch:** MAP = {map_value:.0f} mmHg → 1 điểm")
    
    # 5. CENTRAL NERVOUS SYSTEM (GCS)
    if gcs == 15:
        subscores['cns'] = 0
        details.append(f"**Thần kinh:** GCS = 15 → 0 điểm")
    elif gcs >= 13:
        subscores['cns'] = 1
        details.append(f"**Thần kinh:** GCS = 13-14 → 1 điểm")
    elif gcs >= 10:
        subscores['cns'] = 2
        details.append(f"**Thần kinh:** GCS = 10-12 → 2 điểm")
    elif gcs >= 6:
        subscores['cns'] = 3
        details.append(f"**Thần kinh:** GCS = 6-9 → 3 điểm")
    else:
        subscores['cns'] = 4
        details.append(f"**Thần kinh:** GCS = 3-5 → 4 điểm")
    
    # 6. RENAL
    if creatinine < 1.2:
        renal_by_cr = 0
    elif creatinine < 2.0:
        renal_by_cr = 1
    elif creatinine < 3.5:
        renal_by_cr = 2
    elif creatinine < 5.0:
        renal_by_cr = 3
    else:
        renal_by_cr = 4
    
    if urine_output >= 500:
        renal_by_uo = 0
    elif urine_output >= 200:
        renal_by_uo = 3
    else:
        renal_by_uo = 4
    
    subscores['renal'] = max(renal_by_cr, renal_by_uo)
    
    if renal_by_uo > renal_by_cr:
        details.append(f"**Thận:** UO = {urine_output:.0f} mL/24h → {subscores['renal']} điểm")
    else:
        details.append(f"**Thận:** Creatinine = {creatinine:.1f} mg/dL → {subscores['renal']} điểm")
    
    # Calculate total
    total_score = sum(subscores.values())
    
    # Interpretation
    if total_score == 0:
        interpretation = "Không có suy cơ quan"
        mortality = "<10%"
        risk_class = "LOW"
        color = "🟢"
    elif total_score <= 6:
        interpretation = "Suy cơ quan nhẹ"
        mortality = "~10-20%"
        risk_class = "MILD"
        color = "🟡"
    elif total_score <= 11:
        interpretation = "Suy cơ quan trung bình"
        mortality = "~20-40%"
        risk_class = "MODERATE"
        color = "🟠"
    elif total_score <= 14:
        interpretation = "Suy cơ quan nặng"
        mortality = "~40-60%"
        risk_class = "SEVERE"
        color = "🔴"
    else:
        interpretation = "Suy cơ quan rất nặng"
        mortality = ">60%"
        risk_class = "CRITICAL"
        color = "🔴"
    
    # Management based on score
    if total_score >= 2:
        sepsis_note = f"""
        **⚠️ SOFA ≥2 điểm:**
        - Đáp ứng tiêu chuẩn **SEPSIS-3** (nếu có nhiễm trùng/nghi ngờ nhiễm trùng)
        - Cần đánh giá và xử trí nhiễm trùng huyết NGAY
        - Xem xét Sepsis Bundle (SSC 2021)
        """
    else:
        sepsis_note = ""
    
    return {
        'total_score': total_score,
        'subscores': subscores,
        'interpretation': interpretation,
        'mortality': mortality,
        'risk_class': risk_class,
        'color': color,
        'details': details,
        'sepsis_note': sepsis_note
    }


def render():
    """Render SOFA Score calculator in Streamlit"""
    
    st.title("🏥 SOFA Score")
    st.markdown("**Sequential Organ Failure Assessment - Đánh giá suy đa cơ quan**")
    
    # Educational information
    with st.expander("ℹ️ Thông Tin & Cách Sử Dụng"):
        st.markdown("""
        ### 📋 Giới Thiệu
        
        **SOFA (Sequential Organ Failure Assessment)** là thang điểm:
        - Đánh giá mức độ suy cơ quan ở bệnh nhân ICU
        - Dự đoán tử vong
        - Theo dõi diễn tiến bệnh
        - **Sepsis-3 definition:** SOFA ≥2 = Sepsis
        
        ### 🎯 6 Hệ Cơ Quan
        
        1. **Hô hấp:** PaO₂/FiO₂ ratio
        2. **Đông máu:** Tiểu cầu
        3. **Gan:** Bilirubin
        4. **Tim mạch:** MAP hoặc vasopressor
        5. **Thần kinh:** Glasgow Coma Scale
        6. **Thận:** Creatinine hoặc nước tiểu
        
        Mỗi hệ: 0-4 điểm → Tổng: 0-24 điểm
        
        ### 📊 Điểm & Tử Vong
        
        | SOFA Score | Tử Vong ICU |
        |------------|-------------|
        | 0-6 | <20% |
        | 7-11 | 20-40% |
        | 12-14 | 40-60% |
        | ≥15 | >60% |
        
        ### ⚠️ Sepsis-3 Criteria
        
        **Sepsis = Nhiễm trùng + SOFA ≥2**
        
        - Tăng SOFA ≥2 điểm so với baseline
        - Nếu không biết baseline → giả định = 0
        - qSOFA dùng để screening ngoài ICU
        
        ### 📚 Tài Liệu Tham Khảo
        
        - Vincent JL, et al. *Intensive Care Med* 1996;22:707-710
        - Singer M, et al. *JAMA* 2016;315:801-810 (Sepsis-3)
        """)
    
    st.divider()
    
    # Input section
    st.subheader("📝 Nhập Thông Số 6 Hệ Cơ Quan")
    
    # Respiratory
    st.markdown("#### 1️⃣ Hô Hấp (Respiratory)")
    col1, col2 = st.columns(2)
    with col1:
        pao2 = st.number_input("PaO₂ (mmHg)", 0.0, 700.0, 100.0, 1.0, help="Áp lực oxy máu động mạch")
    with col2:
        fio2 = st.number_input("FiO₂ (%)", 21.0, 100.0, 21.0, 1.0, help="Nồng độ oxy hít vào")
    
    pao2_fio2 = (pao2 / fio2) * 100 if fio2 > 0 else 0
    st.caption(f"💡 PaO₂/FiO₂ = {pao2_fio2:.0f} mmHg")
    
    st.divider()
    
    # Coagulation
    st.markdown("#### 2️⃣ Đông Máu (Coagulation)")
    platelets = st.number_input("Tiểu cầu (×10³/μL)", 0.0, 500.0, 200.0, 1.0)
    
    st.divider()
    
    # Liver
    st.markdown("#### 3️⃣ Gan (Liver)")
    bilirubin = st.number_input("Bilirubin toàn phần (mg/dL)", 0.0, 30.0, 1.0, 0.1)
    st.caption("💡 Chuyển đổi: μmol/L ÷ 17.1 = mg/dL")
    
    st.divider()
    
    # Cardiovascular
    st.markdown("#### 4️⃣ Tim Mạch (Cardiovascular)")
    use_vasopressor = st.checkbox("**Bệnh nhân đang dùng thuốc vận mạch (vasopressor)**")
    
    if use_vasopressor:
        col3, col4 = st.columns(2)
        with col3:
            vasopressor_type = st.selectbox(
                "Loại thuốc",
                ["Dopamine", "Dobutamine", "Epinephrine", "Norepinephrine"]
            )
        with col4:
            vasopressor_dose = st.number_input(
                "Liều (mcg/kg/min)",
                0.0, 50.0, 5.0, 0.1,
                help="Liều thuốc vận mạch"
            )
        map_value = 70.0  # Default when on vasopressor
    else:
        map_value = st.number_input("MAP - Mean Arterial Pressure (mmHg)", 0.0, 200.0, 70.0, 1.0)
        vasopressor_type = ""
        vasopressor_dose = 0.0
        st.caption("💡 MAP = (SBP + 2×DBP) / 3")
    
    st.divider()
    
    # Central Nervous System
    st.markdown("#### 5️⃣ Thần Kinh (CNS)")
    gcs = st.number_input("Glasgow Coma Scale (GCS)", 3, 15, 15, 1)
    st.caption("3 (tệ nhất) → 15 (bình thường)")
    
    st.divider()
    
    # Renal
    st.markdown("#### 6️⃣ Thận (Renal)")
    col5, col6 = st.columns(2)
    with col5:
        creatinine = st.number_input("Creatinine (mg/dL)", 0.0, 20.0, 1.0, 0.1)
        st.caption("💡 μmol/L ÷ 88.4 = mg/dL")
    with col6:
        urine_output = st.number_input("Nước tiểu 24h (mL)", 0.0, 5000.0, 1500.0, 10.0)
    
    st.divider()
    
    # Calculate button
    if st.button("🧮 Tính SOFA Score", type="primary", use_container_width=True):
        result = calculate_sofa(
            pao2_fio2=pao2_fio2,
            platelets=platelets,
            bilirubin=bilirubin,
            map_value=map_value,
            use_vasopressor=use_vasopressor,
            vasopressor_type=vasopressor_type,
            vasopressor_dose=vasopressor_dose,
            gcs=gcs,
            creatinine=creatinine,
            urine_output=urine_output
        )
        
        # Display results
        st.subheader("📊 Kết Quả")
        
        # Score box
        col_r1, col_r2 = st.columns([1, 2])
        
        with col_r1:
            st.metric(
                label="**SOFA Score**",
                value=f"{result['total_score']} điểm"
            )
            st.caption("0-24 điểm (cao = nặng hơn)")
        
        with col_r2:
            st.markdown(f"### {result['color']} {result['interpretation']}")
            st.markdown(f"**Tử vong ước tính: {result['mortality']}**")
        
        # Subscores table
        with st.expander("📋 Điểm Từng Hệ Cơ Quan", expanded=True):
            cols = st.columns(6)
            organs = [
                ("Hô hấp", "respiratory"),
                ("Đông máu", "coagulation"),
                ("Gan", "liver"),
                ("Tim mạch", "cardiovascular"),
                ("Thần kinh", "cns"),
                ("Thận", "renal")
            ]
            
            for col, (name, key) in zip(cols, organs):
                with col:
                    st.metric(name, f"{result['subscores'][key]}")
            
            st.markdown("---")
            st.markdown("**Chi tiết tính điểm:**")
            for detail in result['details']:
                st.markdown(f"- {detail}")
        
        # Sepsis note
        if result['sepsis_note']:
            st.warning(result['sepsis_note'])
        
        # Interpretation & Management
        st.info("""
        **📌 Diễn Giải SOFA:**
        
        - **Tăng SOFA ≥2 điểm** trong 24-48h → xấu đi, nguy cơ tử vong tăng
        - **SOFA cao liên tục** → tiên lượng xấu
        - **SOFA giảm** → đáp ứng điều trị tốt
        
        **Theo dõi:**
        - Tính SOFA hàng ngày để đánh giá diễn tiến
        - So sánh với baseline để xác định Sepsis (Sepsis-3)
        """)
        
        if result['total_score'] >= 11:
            st.error("""
            **🚨 SOFA SCORE CAO:**
            
            - Bệnh nhân có suy đa cơ quan NẶNG
            - Nguy cơ tử vong CAO (>40%)
            - Cần hồi sức tích cực
            - Xem xét mức độ chăm sóc và tiên lượng
            - Thảo luận với gia đình về mục tiêu điều trị
            """)
        
        # Management recommendations
        st.markdown("---")
        st.markdown("### 💊 Khuyến Cáo Xử Trí")
        
        recommendations = []
        
        if result['subscores']['respiratory'] >= 3:
            recommendations.append("""
            **Hô hấp (PaO₂/FiO₂ <200):**
            - Xem xét đặt nội khí quản + thở máy
            - ARDSNet protocol nếu ARDS
            - Lung protective ventilation
            """)
        
        if result['subscores']['coagulation'] >= 2:
            recommendations.append("""
            **Đông máu (Tiểu cầu <100):**
            - Tìm nguyên nhân (DIC, sepsis, thuốc, HIT)
            - Xem xét truyền tiểu cầu nếu chảy máu hoặc thủ thuật
            - Tránh thuốc ảnh hưởng tiểu cầu
            """)
        
        if result['subscores']['liver'] >= 2:
            recommendations.append("""
            **Gan (Bilirubin >2):**
            - Đánh giá chức năng gan (ALT, AST, PT/INR)
            - Loại trừ viêm gan, tắc mật
            - Điều chỉnh liều thuốc
            """)
        
        if result['subscores']['cardiovascular'] >= 2:
            recommendations.append("""
            **Tim mạch (MAP thấp/cần vasopressor):**
            - Hồi sức dịch nếu hypovolemia
            - Vasopressor: Norepinephrine first-line
            - Mục tiêu MAP ≥65 mmHg
            - Echo đánh giá chức năng tim
            - Xem xét inotrope nếu cardiac dysfunction
            """)
        
        if result['subscores']['cns'] >= 2:
            recommendations.append("""
            **Thần kinh (GCS <13):**
            - Bảo vệ đường thở
            - CT đầu nếu cần
            - Loại trừ nguyên nhân: infection, metabolic, structural
            - Sedation scoring nếu đang an thần
            """)
        
        if result['subscores']['renal'] >= 2:
            recommendations.append("""
            **Thận (Cr >2 hoặc UO <500 mL/24h):**
            - Đánh giá theo KDIGO AKI criteria
            - Tìm nguyên nhân: pre-renal/intrinsic/post-renal
            - Điều chỉnh liều thuốc
            - Theo dõi điện giải (K, PO4)
            - Xem xét RRT nếu chỉ định
            """)
        
        if recommendations:
            for rec in recommendations:
                st.markdown(rec)
        else:
            st.success("✅ Không có cơ quan nào suy nặng - tiếp tục theo dõi")
        
        # Save to session state
        st.session_state['sofa_result'] = result
        
        # Warning
        st.warning("""
        ⚠️ **Lưu Ý Y Khoa:**
        - SOFA là công cụ đánh giá, không phải chẩn đoán
        - Cần kết hợp với lâm sàng và xét nghiệm khác
        - SOFA không dự đoán chính xác 100% - chỉ là ước tính
        - Quyết định điều trị cuối cùng thuộc về bác sĩ điều trị
        """)
    
    # Quick reference
    with st.expander("📖 Bảng SOFA Scoring Chi Tiết"):
        st.markdown("""
        ### SOFA Scoring Table
        
        | Hệ Cơ Quan | 0 | 1 | 2 | 3 | 4 |
        |------------|---|---|---|---|---|
        | **Hô hấp** PaO₂/FiO₂ (mmHg) | ≥400 | <400 | <300 | <200 | <100 |
        | **Đông máu** Platelets (×10³/μL) | ≥150 | <150 | <100 | <50 | <20 |
        | **Gan** Bilirubin (mg/dL) | <1.2 | 1.2-1.9 | 2.0-5.9 | 6.0-11.9 | ≥12 |
        | **Tim mạch** | MAP≥70 | MAP<70 | Dopa <5* hoặc Dobu | Dopa 5-15* hoặc Epi/Norepi ≤0.1** | Dopa >15* hoặc Epi/Norepi >0.1** |
        | **Thần kinh** GCS | 15 | 13-14 | 10-12 | 6-9 | 3-5 |
        | **Thận** Cr (mg/dL) hoặc UO | <1.2 | 1.2-1.9 | 2.0-3.4 | 3.5-4.9 hoặc <500 mL/d | ≥5.0 hoặc <200 mL/d |
        
        \* Dopamine liều (mcg/kg/min)  
        \*\* Epinephrine/Norepinephrine liều (mcg/kg/min)
        
        ### Sepsis-3 Definitions
        
        - **Sepsis:** Nhiễm trùng + SOFA ≥2 điểm
        - **Septic Shock:** Sepsis + Vasopressor để duy trì MAP ≥65 + Lactate >2 mmol/L
        
        ### Delta SOFA
        
        - Tính thay đổi SOFA so với baseline (nếu biết)
        - Nếu không biết baseline → giả định = 0
        - Tăng ≥2 điểm = có ý nghĩa lâm sàng
        """)
