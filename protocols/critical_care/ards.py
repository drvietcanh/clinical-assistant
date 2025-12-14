"""
ARDS Management Protocol
Berlin Definition 2012, SCCM Guidelines
Acute Respiratory Distress Syndrome Management
"""

import streamlit as st


def render():
    """ARDS Management Protocol"""
    st.subheader("🫁 ARDS Management Protocol")
    st.caption("Berlin Definition 2012, SCCM Guidelines - Acute Respiratory Distress Syndrome")
    
    st.error("""
    **⚠️ CRITICAL: ARDS là hội chứng suy hô hấp cấp nặng!**
    - **Mortality:** 30-50% (tùy mức độ)
    - **Time to diagnosis:** < 1 tuần từ khi khởi phát
    - **Requires:** ICU care, mechanical ventilation
    """)
    
    st.markdown("---")
    
    # Berlin Definition
    st.markdown("### 📋 Berlin Definition (2012) - Chẩn đoán ARDS")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Tiêu chuẩn chẩn đoán ARDS:**
        
        1. **Khởi phát:** < 7 ngày từ khi có yếu tố nguy cơ
        2. **X-quang:** Bóng mờ 2 bên phổi (không giải thích được bởi tràn dịch, xẹp phổi, hoặc nốt)
        3. **Không phải do suy tim:** Không có bằng chứng suy tim hoặc quá tải dịch
        4. **PaO₂/FiO₂:** ≤300 mmHg với PEEP ≥5 cmH₂O
        """)
    
    with col2:
        st.markdown("#### Phân loại mức độ")
        
        pao2_fio2 = st.number_input(
            "**PaO₂/FiO₂ (mmHg):**",
            min_value=50.0,
            max_value=400.0,
            value=200.0,
            step=10.0,
            key="ards_pao2_fio2",
            help="Với PEEP ≥5 cmH₂O"
        )
        
        if pao2_fio2 > 300:
            st.warning("**Không đủ tiêu chuẩn ARDS** (PaO₂/FiO₂ >300)")
            ards_severity = "None"
        elif pao2_fio2 > 200:
            st.success("**ARDS Nhẹ**")
            st.caption("PaO₂/FiO₂: 201-300 mmHg")
            ards_severity = "Mild"
        elif pao2_fio2 > 100:
            st.warning("**ARDS Trung Bình**")
            st.caption("PaO₂/FiO₂: 101-200 mmHg")
            ards_severity = "Moderate"
        else:
            st.error("**ARDS Nặng**")
            st.caption("PaO₂/FiO₂: ≤100 mmHg")
            ards_severity = "Severe"
    
    st.markdown("---")
    st.markdown("### 1️⃣ Xử tríTức Thì (< 1 Giờ)")
    
    st.error("""
    **ABC - Đường thở, Hô hấp, Tuần hoàn:**
    
    **A - Airway:**
    - Đảm bảo đường thở thông thoáng
    - Cân nhắc đặt nội khí quản nếu:
      * GCS <8
      * Không bảo vệ được đường thở
      * Respiratory failure (PaO₂ <60 mmHg với O₂)
      * Work of breathing tăng (accessory muscles, paradoxical breathing)
    
    **B - Breathing:**
    - **Oxygen therapy:** High-flow nasal cannula (HFNC) hoặc non-invasive ventilation (NIV)
    - **Nếu không đáp ứng:** Đặt nội khí quản và mechanical ventilation
    - **Mục tiêu SpO₂:** 88-95% (cho phép permissive hypoxemia)
    
    **C - Circulation:**
    - **2 đường truyền tĩnh mạch lớn**
    - **Lấy máu ngay:**
      * ABG (PaO₂, PaCO₂, pH, lactate)
      * CBC, PT/INR, aPTT
      * BNP/NT-proBNP (loại trừ suy tim)
      * Cultures (blood, sputum, urine)
      * LFT, Creatinine
    - **ECG**
    """)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Ventilator Management - Lung Protective Strategy")
    
    st.warning("""
    **⚠️ QUAN TRỌNG: Lung Protective Ventilation là nền tảng điều trị ARDS!**
    
    **Mục tiêu:**
    - Giảm VILI (Ventilator-Induced Lung Injury)
    - Giảm mortality
    - Cải thiện kết quả
    """)
    
    tab1, tab2, tab3 = st.tabs(["📊 Ventilator Settings", "💧 Fluid Management", "🔄 Prone Positioning"])
    
    with tab1:
        st.markdown("#### 📊 Ventilator Settings Calculator")
        
        col1, col2 = st.columns(2)
        
        with col1:
            ideal_body_weight = st.number_input(
                "**Ideal Body Weight (kg):**",
                min_value=30.0,
                max_value=150.0,
                value=70.0,
                step=1.0,
                key="ards_ibw",
                help="IBW = 50 + 2.3 × (height in inches - 60) cho nam, 45.5 + 2.3 × (height in inches - 60) cho nữ"
            )
            
            mode = st.selectbox(
                "**Ventilator Mode:**",
                ["Volume Control (VC)", "Pressure Control (PC)", "Pressure Support (PS)"],
                key="ards_mode"
            )
        
        with col2:
            st.markdown("#### 🎯 Lung Protective Targets")
            
            # Calculate tidal volume
            target_tv = ideal_body_weight * 6  # 6 ml/kg IBW
            max_tv = ideal_body_weight * 8  # Max 8 ml/kg
            
            st.metric("**Tidal Volume (Vt):**", f"{target_tv:.0f} ml", help="6 ml/kg IBW (target)")
            st.metric("**Max Vt:**", f"{max_tv:.0f} ml", help="Không vượt quá 8 ml/kg IBW")
            
            target_ppeak = st.number_input(
                "**Plateau Pressure (Pplat) Target:**",
                min_value=20,
                max_value=40,
                value=30,
                step=1,
                key="ards_ppeak",
                help="Mục tiêu: ≤30 cmH₂O"
            )
            
            if target_ppeak > 30:
                st.error("⚠️ **Pplat >30 cmH₂O - Cần giảm Vt!**")
        
        st.markdown("---")
        st.markdown("#### 📋 Ventilator Settings Protocol")
        
        st.success("""
        **Lung Protective Ventilation:**
        
        **1. Tidal Volume (Vt):**
        - **6 ml/kg IBW** (ideal body weight)
        - **Không vượt quá 8 ml/kg IBW**
        - Giảm Vt nếu Pplat >30 cmH₂O
        
        **2. PEEP (Positive End-Expiratory Pressure):**
        - **ARDS Nhẹ:** PEEP 5-8 cmH₂O
        - **ARDS Trung Bình:** PEEP 8-12 cmH₂O
        - **ARDS Nặng:** PEEP 12-16 cmH₂O (có thể cao hơn)
        - **PEEP/FiO₂ Table:** Dùng để điều chỉnh PEEP theo FiO₂
        
        **3. FiO₂:**
        - Bắt đầu với FiO₂ 1.0 (100%)
        - Giảm dần đến mục tiêu SpO₂ 88-95%
        - **Permissive hypoxemia:** Chấp nhận SpO₂ 88-92% nếu không có thiếu máu cơ tim
        
        **4. Nhịp thở (RR):**
        - 16-24 breaths/min
        - Tăng RR nếu cần để duy trì pH >7.20 (permissive hypercapnia)
        
        **5. I:E Ratio:**
        - 1:1 đến 1:2
        - Có thể dùng inverse ratio (2:1) nếu cần
        
        **6. Plateau Pressure (Pplat):**
        - **Mục tiêu: ≤30 cmH₂O**
        - Nếu Pplat >30: Giảm Vt
        - Nếu Pplat >35: Giảm Vt ngay lập tức
        """)
        
        st.markdown("---")
        st.markdown("#### 📊 PEEP/FiO₂ Table")
        
        import pandas as pd
        
        peep_fio2_data = {
            "FiO₂": ["0.3", "0.4", "0.5", "0.6", "0.7", "0.8", "0.9", "1.0"],
            "PEEP (cmH₂O)": ["5", "8", "10", "12", "14", "14", "16", "18"],
            "PaO₂/FiO₂ Target": [">300", "201-300", "151-200", "101-150", "76-100", "51-75", "≤50", "≤50"]
        }
        
        st.dataframe(pd.DataFrame(peep_fio2_data), use_container_width=True, hide_index=True)
        
        st.info("""
        **Cách sử dụng PEEP/FiO₂ Table:**
        1. Bắt đầu với FiO₂ 1.0, PEEP 10-12 cmH₂O
        2. Đo PaO₂/FiO₂ sau 30-60 phút
        3. Điều chỉnh PEEP theo bảng để đạt PaO₂/FiO₂ tốt nhất
        4. Giảm FiO₂ dần khi có thể (mục tiêu FiO₂ <0.6)
        """)
    
    with tab2:
        st.markdown("#### 💧 Fluid Management Strategy")
        
        st.warning("""
        **Conservative Fluid Strategy (FACTT Trial):**
        
        **Mục tiêu:**
        - Giảm pulmonary edema
        - Cải thiện oxygenation
        - Giảm số ngày thở máy
        - Không tăng AKI risk
        
        **Protocol:**
        - **CVP target:** <4 mmHg (hoặc <8 mmHg nếu shock)
        - **PAWP target:** <8 mmHg (nếu có Swan-Ganz)
        - **Urine output:** >0.5 mL/kg/h (nhưng không cần >1 mL/kg/h)
        - **Fluid balance:** Negative hoặc neutral
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Conservative Strategy:**")
            st.success("""
            - **CVP:** <4 mmHg (hoặc <8 nếu shock)
            - **PAWP:** <8 mmHg
            - **Diuretics:** Nếu CVP/PAWP cao
            - **Fluid:** Chỉ bù nếu shock hoặc hypovolemia rõ
            - **Mục tiêu:** Negative balance hoặc neutral
            """)
        
        with col2:
            st.markdown("**Liberal Strategy (chỉ nếu shock):**")
            st.info("""
            - **CVP:** 8-12 mmHg
            - **PAWP:** 12-15 mmHg
            - **Fluid:** Bolus nếu cần
            - **Vasopressors:** Nếu vẫn shock sau fluid
            - **Mục tiêu:** Euvolemia, sau đó chuyển conservative
            """)
        
        st.markdown("---")
        st.markdown("#### 💊 Diuretics Protocol")
        
        st.info("""
        **Nếu CVP/PAWP cao hoặc fluid overload:**
        
        **Furosemide:**
        - **Bolus:** 20-40mg IV
        - **Continuous:** 5-20 mg/h IV
        - **Mục tiêu:** Negative balance 500-1000ml/ngày
        
        **Lưu ý:**
        - Theo dõi creatinine, electrolytes
        - Không dùng nếu hypovolemic
        - Cân nhắc albumin nếu hypoalbuminemia
        """)
    
    with tab3:
        st.markdown("#### 🔄 Prone Positioning")
        
        st.success("""
        **Prone Positioning (PROSEVA Trial):**
        
        **Chỉ định:**
        - **ARDS Nặng:** PaO₂/FiO₂ <150 mmHg
        - **FiO₂ >0.6** với PEEP ≥10 cmH₂O
        - **Early prone:** Trong vòng 36h từ khi ARDS
        
        **Lợi ích:**
        - Cải thiện oxygenation (PaO₂/FiO₂ tăng 20-30%)
        - Giảm mortality (16% vs 33% trong PROSEVA)
        - Giảm VILI (ventilator-induced lung injury)
        
        **Contraindications:**
        - Unstable spine fracture
        - Open abdomen
        - Increased ICP
        - Unstable pelvic fracture
        - Pregnancy (late trimester)
        """)
        
        st.markdown("---")
        st.markdown("#### 📋 Prone Positioning Protocol")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.info("""
            **Trước khi prone:**
            1. Đảm bảo đường thở an toàn (ETT cố định tốt)
            2. Đặt NGT (nếu chưa có)
            3. Đặt Foley catheter
            4. Đặt arterial line (nếu chưa có)
            5. Đảm bảo IV access an toàn
            6. Pre-oxygenate với FiO₂ 1.0
            """)
        
        with col2:
            st.warning("""
            **Trong khi prone:**
            - **Duration:** 16-18 giờ/ngày
            - **Frequency:** Mỗi ngày cho đến khi cải thiện
            - **Monitor:** SpO₂, BP, ETT position
            - **Complications:** Pressure ulcers, ETT dislodgement, line disconnection
            """)
        
        st.markdown("---")
        st.markdown("#### ⏱️ Timing")
        
        st.error("""
        **Early Prone (Trong 36h):**
        - Bắt đầu ngay khi đạt chỉ định
        - Lợi ích tối đa nếu bắt đầu sớm
        - Tiếp tục cho đến khi:
          * PaO₂/FiO₂ >150 mmHg với PEEP ≤10 và FiO₂ ≤0.6
          * Hoặc cải thiện rõ ràng
        """)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Adjunctive Therapies")
    
    tab1, tab2, tab3, tab4 = st.tabs(["💊 Neuromuscular Blockade", "💉 ECMO", "🔄 Recruitment Maneuvers", "💊 Corticosteroids"])
    
    with tab1:
        st.markdown("#### 💊 Neuromuscular Blockade (NMB)")
        
        st.info("""
        **Chỉ định (ROSE Trial):**
        - **ARDS Nặng:** PaO₂/FiO₂ <150 mmHg
        - **Early NMB:** Trong vòng 48h từ khi ARDS
        - **Duration:** 48h continuous
        
        **Lợi ích:**
        - Giảm VILI (ventilator-induced lung injury)
        - Cải thiện patient-ventilator synchrony
        - Giảm mortality (một số nghiên cứu)
        
        **Thuốc:**
        - **Cisatracurium:** 0.15-0.2 mg/kg IV bolus, sau đó 0.15-0.2 mg/kg/h continuous
        - **Rocuronium:** 0.6-1.2 mg/kg IV bolus, sau đó 0.3-0.6 mg/kg/h continuous
        
        **Lưu ý:**
        - Phải có deep sedation (RASS -5)
        - Theo dõi với train-of-four (TOF)
        - Ngừng sau 48h, đánh giá lại
        """)
    
    with tab2:
        st.markdown("#### 💉 ECMO (Extracorporeal Membrane Oxygenation)")
        
        st.warning("""
        **Chỉ định (EOLIA Trial):**
        - **ARDS Nặng:** PaO₂/FiO₂ <80 mmHg với PEEP ≥10 và FiO₂ ≥0.8
        - **Hoặc:** PaO₂/FiO₂ <50 mmHg với PEEP ≥10 và FiO₂ ≥0.8 trong >3h
        - **Hoặc:** pH <7.25 với PaCO₂ >60 mmHg (refractory hypercapnia)
        
        **Contraindications:**
        - Age >65 tuổi (relative)
        - Mechanical ventilation >7 ngày
        - Contraindications cho anticoagulation
        - Severe comorbidities (cancer, end-stage organ failure)
        
        **Lợi ích:**
        - Ultra-lung protective ventilation
        - Có thể giảm mortality trong một số trường hợp
        - Cho phép "lung rest"
        
        **Complications:**
        - Bleeding (major complication)
        - Thrombosis
        - Infection
        - Limb ischemia
        """)
    
    with tab3:
        st.markdown("#### 🔄 Recruitment Maneuvers")
        
        st.info("""
        **Recruitment Maneuvers (RM):**
        
        **Chỉ định:**
        - Severe hypoxemia (PaO₂/FiO₂ <100)
        - After suctioning
        - After disconnection from ventilator
        
        **Methods:**
        1. **Sustained inflation:**
           - PEEP 40-50 cmH₂O × 30-40 giây
           - Sau đó quay về PEEP ban đầu
        2. **Incremental PEEP:**
           - Tăng PEEP từ 5 → 15 → 25 → 35 cmH₂O
           - Mỗi mức 30 giây
           - Sau đó giảm dần
        
        **Lưu ý:**
        - Có thể gây hypotension
        - Có thể gây barotrauma
        - Theo dõi BP, SpO₂ trong khi RM
        - Không dùng nếu có pneumothorax
        """)
    
    with tab4:
        st.markdown("#### 💊 Corticosteroids")
        
        st.warning("""
        **Methylprednisolone (DEXA-ARDS Trial):**
        
        **Chỉ định:**
        - **ARDS:** PaO₂/FiO₂ <200 mmHg
        - **Early:** Trong vòng 14 ngày từ khi ARDS
        - **Duration:** 7-14 ngày
        
        **Liều:**
        - **Methylprednisolone:** 1 mg/kg IV q12h × 3 ngày
        - Sau đó: 1 mg/kg IV q24h × 3 ngày
        - Sau đó: 0.5 mg/kg IV q24h × 3 ngày
        - Sau đó: 0.25 mg/kg IV q24h × 3 ngày
        - Tổng: 14 ngày
        
        **Lợi ích:**
        - Có thể giảm mortality (một số nghiên cứu)
        - Cải thiện oxygenation
        - Giảm số ngày thở máy
        
        **Lưu ý:**
        - Không dùng nếu nghi nhiễm trùng không kiểm soát được
        - Theo dõi glucose, infection
        - Có thể tăng nguy cơ neuromyopathy
        """)
    
    st.markdown("---")
    st.markdown("### 4️⃣ Monitoring")
    
    st.success("""
    **Monitoring Protocol:**
    
    **Continuous:**
    - SpO₂, HR, BP, RR
    - Ventilator parameters (Vt, Pplat, PEEP, FiO₂)
    - ETT position
    
    **Every 1-2 hours:**
    - ABG (PaO₂, PaCO₂, pH, lactate)
    - Plateau pressure (Pplat)
    - Patient-ventilator synchrony
    
    **Every 4-6 hours:**
    - CXR (nếu cần)
    - Fluid balance
    - Urine output
    
    **Daily:**
    - CBC, Creatinine, LFT
    - Cultures (nếu nghi nhiễm trùng)
    - Chest X-ray
    """)
    
    st.markdown("---")
    st.markdown("### 5️⃣ Weaning from Ventilator")
    
    st.info("""
    **Khi nào bắt đầu weaning:**
    
    **Criteria:**
    - PaO₂/FiO₂ >200 mmHg với PEEP ≤8 và FiO₂ ≤0.5
    - Pplat ≤30 cmH₂O
    - Hemodynamically stable (không cần vasopressors hoặc liều thấp)
    - Awake, có thể follow commands
    - Cough adequate
    - Secretions manageable
    
    **Weaning Protocol:**
    - Spontaneous breathing trial (SBT)
    - Pressure support mode
    - T-piece trial
    """)
    
    st.markdown("---")
    st.markdown("### 6️⃣ Prognosis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.warning("""
        **Mortality by Severity:**
        - **ARDS Nhẹ:** 27%
        - **ARDS Trung Bình:** 32%
        - **ARDS Nặng:** 45%
        
        **Factors Associated with Poor Outcome:**
        - Age >65
        - APACHE II >25
        - PaO₂/FiO₂ <100
        - Multiple organ failure
        - Sepsis
        """)
    
    with col2:
        st.info("""
        **Recovery:**
        - Most survivors: Recovery trong 6-12 tháng
        - Lung function: Có thể cải thiện nhưng không hoàn toàn
        - Quality of life: Có thể giảm
        - Long-term complications: ICU-acquired weakness, cognitive impairment
        """)
    
    st.markdown("---")
    st.markdown("### 📚 Tài liệu tham khảo")
    
    st.markdown("""
    1. **Berlin Definition of ARDS** - ARDS Definition Task Force 2012
       - JAMA 2012;307(23):2526-2533
    
    2. **Lung Protective Ventilation** - ARDS Network 2000
       - NEJM 2000;342:1301-1308
    
    3. **Prone Positioning** - PROSEVA Trial 2013
       - NEJM 2013;368:2159-2168
    
    4. **Neuromuscular Blockade** - ROSE Trial 2019
       - NEJM 2019;380:1997-2008
    
    5. **ECMO** - EOLIA Trial 2018
       - NEJM 2018;378:1965-1975
    
    6. **Corticosteroids** - DEXA-ARDS Trial 2020
       - JAMA 2020;323:765-776
    
    7. **UpToDate:** Acute Respiratory Distress Syndrome - Last updated 2024
    """)
    
    st.markdown("---")
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất.")

