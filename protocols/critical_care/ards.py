"""
ARDS Management Protocol
Berlin Definition 2012, SCCM Guidelines
Acute Respiratory Distress Syndrome Management
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section
from components.evidence_badge import (
    render_evidence_badge,
    render_evidence_summary,
    Citation
)


def render():
    """ARDS Management Protocol"""
    st.subheader("🫁 ARDS Management Protocol")
    st.caption("Berlin Definition 2012, SCCM Guidelines - Acute Respiratory Distress Syndrome")
    
    # Evidence summary
    render_evidence_summary(
        last_reviewed="2024-03-01",
        last_updated="2024-03-01",
        version="2024",
        guideline_source="SCCM/ESICM 2024"
    )
    
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
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📊 Ventilator Settings", 
        "💧 Fluid Management", 
        "🔄 Prone Positioning",
        "💉 Neuromuscular Blockade",
        "🩸 ECMO"
    ])
    
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
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "💊 Neuromuscular Blockade", 
        "💉 ECMO", 
        "🔄 Recruitment Maneuvers", 
        "💊 Corticosteroids",
        "💨 Inhaled Nitric Oxide (iNO)"
    ])
    
    with tab1:
        st.markdown("#### 💊 Neuromuscular Blockade (NMB)")
        
        st.warning("""
        **⚠️ QUAN TRỌNG: NMB chỉ dùng khi có deep sedation (RASS -5)!**
        - Phải đảm bảo patient không thể cảm nhận đau đớn
        - Phải có monitoring TOF (train-of-four)
        - Chỉ dùng trong ARDS nặng, early phase (<48h)
        """)
        
        st.markdown("---")
        st.markdown("##### 📋 Chỉ định NMB (ROSE Trial)")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.success("""
            **Chỉ định:**
            - **ARDS Nặng:** PaO₂/FiO₂ <150 mmHg
            - **Early NMB:** Trong vòng 48h từ khi ARDS
            - **Duration:** 48h continuous infusion
            - **Mục tiêu:** Giảm VILI, cải thiện synchrony
            
            **Lợi ích:**
            - Giảm VILI (ventilator-induced lung injury)
            - Cải thiện patient-ventilator synchrony
            - Giảm barotrauma risk
            - Có thể giảm mortality trong ARDS nặng
            """)
        
        with col2:
            st.error("""
            **Contraindications:**
            - Không có deep sedation
            - ARDS >48h (late phase)
            - Neuromuscular disease (myasthenia gravis, etc.)
            - Allergy to NMB
            - Không có monitoring TOF
            - Severe hepatic failure (với rocuronium)
            """)
        
        st.markdown("---")
        st.markdown("##### 💉 Cisatracurium - Thuốc Ưu Tiên")
        
        st.info("""
        **Cisatracurium là thuốc ưu tiên cho ARDS:**
        - **Hofmann elimination:** Không phụ thuộc gan/thận
        - **An toàn:** Ít tác dụng phụ
        - **Predictable:** Thời gian tác dụng ổn định
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Dosing Calculator:**")
            
            patient_weight = st.number_input(
                "**Cân nặng (kg):**",
                min_value=40.0,
                max_value=150.0,
                value=70.0,
                step=1.0,
                key="nmb_weight"
            )
            
            # Calculate dosing
            bolus_dose = patient_weight * 0.15  # 0.15 mg/kg
            bolus_dose_max = patient_weight * 0.2  # 0.2 mg/kg
            continuous_rate = patient_weight * 0.15  # 0.15 mg/kg/h
            continuous_rate_max = patient_weight * 0.2  # 0.2 mg/kg/h
            
            st.markdown("---")
            st.markdown("**📊 Liều Cisatracurium:**")
            st.metric("**Bolus Dose:**", f"{bolus_dose:.1f} - {bolus_dose_max:.1f} mg", 
                     help="0.15-0.2 mg/kg IV bolus")
            st.metric("**Continuous Rate:**", f"{continuous_rate:.1f} - {continuous_rate_max:.1f} mg/h",
                     help="0.15-0.2 mg/kg/h continuous infusion")
            
            st.info("""
            **Protocol:**
            1. **Bolus:** 0.15-0.2 mg/kg IV
            2. **Immediately start:** Continuous infusion 0.15-0.2 mg/kg/h
            3. **Duration:** 48h
            4. **Titrate:** Dựa trên TOF monitoring
            """)
        
        with col2:
            st.markdown("**Monitoring Protocol:**")
            
            st.markdown("**1. Train-of-Four (TOF) Monitoring:**")
            st.checkbox("✅ Đặt TOF monitor trước khi bắt đầu", key="tof_setup")
            st.checkbox("✅ Đo TOF mỗi 1-2 giờ", key="tof_monitor")
            st.checkbox("✅ Mục tiêu: 1-2 twitches (25-50% response)", key="tof_target")
            
            st.markdown("---")
            st.markdown("**2. Clinical Monitoring:**")
            st.checkbox("✅ Deep sedation (RASS -5)", key="nmb_sedation")
            st.checkbox("✅ Plateau pressure (Pplat)", key="nmb_pplat")
            st.checkbox("✅ Patient-ventilator synchrony", key="nmb_sync")
            st.checkbox("✅ ABG mỗi 2-4 giờ", key="nmb_abg")
            
            st.markdown("---")
            st.markdown("**3. Complications Watch:**")
            st.warning("""
            - **Critical illness myopathy:** Theo dõi weakness sau khi ngừng
            - **Prolonged paralysis:** Nếu TOF không hồi phục
            - **Accidental awareness:** Đảm bảo deep sedation
            """)
        
        st.markdown("---")
        st.markdown("##### 📋 Cisatracurium Dosing Protocol")
        
        st.success("""
        **Step-by-Step Protocol:**
        
        **1. Pre-NMB Checklist:**
        - ✅ Deep sedation đạt (RASS -5)
        - ✅ TOF monitor đã đặt
        - ✅ ARDS nặng (PaO₂/FiO₂ <150)
        - ✅ ARDS <48h từ khi khởi phát
        - ✅ Không có contraindications
        
        **2. Bolus Dose:**
        - **Cisatracurium:** 0.15-0.2 mg/kg IV bolus
        - Ví dụ: 70kg → 10.5-14 mg IV bolus
        
        **3. Continuous Infusion:**
        - **Start immediately:** 0.15-0.2 mg/kg/h
        - Ví dụ: 70kg → 10.5-14 mg/h
        - **Titrate:** Dựa trên TOF (mục tiêu 1-2 twitches)
        
        **4. Duration:**
        - **48h continuous**
        - Không kéo dài >48h nếu không cần thiết
        
        **5. Weaning:**
        - Ngừng infusion sau 48h
        - Đánh giá lại nhu cầu
        - Theo dõi recovery (TOF 4/4)
        """)
        
        st.markdown("---")
        st.markdown("##### 🔄 Alternative: Rocuronium")
        
        st.info("""
        **Rocuronium (nếu không có cisatracurium):**
        
        **Dosing:**
        - **Bolus:** 0.6-1.2 mg/kg IV
        - **Continuous:** 0.3-0.6 mg/kg/h
        
        **Lưu ý:**
        - Phụ thuộc gan/thận
        - Thời gian tác dụng dài hơn
        - Có thể tích lũy ở suy gan/thận
        """)
        
        st.markdown("---")
        st.markdown("##### ⏱️ Timing & Duration")
        
        st.error("""
        **QUAN TRỌNG về Timing:**
        
        **Early NMB (<48h):**
        - Bắt đầu ngay khi đạt chỉ định
        - Lợi ích tối đa nếu bắt đầu sớm
        - Không đợi đến khi ARDS nặng hơn
        
        **Duration:**
        - **48h continuous** (không ngắt quãng)
        - Đánh giá lại sau 48h
        - Không kéo dài >48h trừ khi có chỉ định đặc biệt
        
        **When to Stop:**
        - Sau 48h
        - PaO₂/FiO₂ cải thiện >150
        - Hoặc không còn lợi ích
        """)
    
    with tab2:
        st.markdown("#### 💉 ECMO (Extracorporeal Membrane Oxygenation)")
        
        st.error("""
        **🚨 ECMO là biện pháp cứu cánh cho ARDS nặng không đáp ứng điều trị thông thường!**
        - **Chỉ định:** ARDS nặng, refractory hypoxemia/hypercapnia
        - **Timing:** Sớm (<7 ngày thở máy) để có kết quả tốt nhất
        - **Requires:** Trung tâm ECMO chuyên biệt, team có kinh nghiệm
        """)
        
        st.markdown("---")
        st.markdown("##### 📋 Chỉ định ECMO (EOLIA Trial Criteria)")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Chỉ định ECMO khi có MỘT trong các tiêu chuẩn sau:**")
            
            st.markdown("**1. Refractory Hypoxemia:**")
            st.checkbox("PaO₂/FiO₂ <80 mmHg", key="ecmo_hypox1")
            st.checkbox("Với PEEP ≥10 cmH₂O", key="ecmo_peep1")
            st.checkbox("Với FiO₂ ≥0.8", key="ecmo_fio2_1")
            
            st.markdown("---")
            st.markdown("**2. Severe Hypoxemia:**")
            st.checkbox("PaO₂/FiO₂ <50 mmHg", key="ecmo_hypox2")
            st.checkbox("Với PEEP ≥10 cmH₂O", key="ecmo_peep2")
            st.checkbox("Với FiO₂ ≥0.8", key="ecmo_fio2_2")
            st.checkbox("Kéo dài >3 giờ", key="ecmo_duration")
        
        with col2:
            st.markdown("**3. Refractory Hypercapnia:**")
            st.checkbox("pH <7.25", key="ecmo_ph")
            st.checkbox("Với PaCO₂ >60 mmHg", key="ecmo_paco2")
            st.checkbox("Mặc dù đã tối ưu ventilator", key="ecmo_vent")
            
            st.markdown("---")
            st.markdown("**4. Additional Considerations:**")
            st.checkbox("Đã thử prone positioning", key="ecmo_prone")
            st.checkbox("Đã thử NMB", key="ecmo_nmb")
            st.checkbox("Đã tối ưu lung protective ventilation", key="ecmo_lpv")
            st.checkbox("ARDS <7 ngày", key="ecmo_early")
        
        st.markdown("---")
        st.markdown("##### ✅ ECMO Eligibility Checklist")
        
        eligibility_col1, eligibility_col2 = st.columns(2)
        
        with eligibility_col1:
            st.markdown("**Inclusion Criteria:**")
            st.success("""
            ✅ **Age:** <65 tuổi (relative, có thể xem xét đến 70)
            ✅ **ARDS duration:** <7 ngày thở máy
            ✅ **Reversible lung disease:** Nguyên nhân có thể hồi phục
            ✅ **No severe comorbidities:**
               - Không có cancer tiến triển
               - Không có end-stage organ failure
               - Không có severe brain injury
            ✅ **Good pre-morbid function:** Có thể hồi phục
            ✅ **Family support:** Gia đình đồng ý
            """)
        
        with eligibility_col2:
            st.markdown("**Exclusion Criteria (Contraindications):")
            st.error("""
            ❌ **Absolute:**
            - Age >75 tuổi
            - Mechanical ventilation >14 ngày
            - Severe brain injury (GCS <5, không hồi phục)
            - End-stage cancer
            - Severe comorbidities không hồi phục
            
            ❌ **Relative:**
            - Contraindications cho anticoagulation
            - Severe peripheral vascular disease
            - Morbid obesity (BMI >40)
            - Severe frailty
            - No family support
            """)
        
        st.markdown("---")
        st.markdown("##### 📞 ECMO Referral Process")
        
        st.warning("""
        **QUAN TRỌNG: Refer sớm khi có dấu hiệu cần ECMO!**
        - Đừng đợi đến khi bệnh nhân quá nặng
        - ECMO team cần thời gian để đánh giá và chuẩn bị
        - Early referral = Better outcomes
        """)
        
        st.markdown("**Step 1: Early Recognition**")
        st.info("""
        **Dấu hiệu sớm cần ECMO:**
        - PaO₂/FiO₂ <100 và đang giảm dần
        - Cần FiO₂ >0.8 và PEEP >12
        - Plateau pressure >30 cmH₂O mặc dù đã giảm Vt
        - pH <7.30 với PaCO₂ >50
        - Đã thử prone positioning nhưng không cải thiện
        """)
        
        st.markdown("**Step 2: Contact ECMO Center**")
        st.success("""
        **Thông tin cần cung cấp khi refer:**
        
        **Patient Demographics:**
        - Age, gender, weight
        - Comorbidities
        - Pre-morbid function
        
        **ARDS Information:**
        - Nguyên nhân ARDS
        - Thời gian từ khi khởi phát
        - Thời gian thở máy
        - Berlin severity (Mild/Moderate/Severe)
        
        **Current Status:**
        - PaO₂/FiO₂ hiện tại
        - Ventilator settings (Vt, PEEP, FiO₂, Pplat)
        - ABG (pH, PaCO₂, PaO₂, lactate)
        - Hemodynamics (BP, HR, vasopressors)
        - Organ function (creatinine, bilirubin, etc.)
        
        **Treatments Tried:**
        - Prone positioning (số lần, kết quả)
        - NMB (đã dùng chưa, kết quả)
        - Corticosteroids
        - Other adjunctive therapies
        """)
        
        st.markdown("**Step 3: ECMO Team Assessment**")
        st.info("""
        **ECMO team sẽ đánh giá:**
        - Eligibility criteria
        - Reversibility of lung disease
        - Overall prognosis
        - Technical feasibility
        - Resource availability
        
        **Decision:**
        - Accept for ECMO
        - Continue current management
        - Reassess later
        """)
        
        st.markdown("**Step 4: Transfer Preparation**")
        st.warning("""
        **Nếu được chấp nhận ECMO:**
        - Stabilize patient trước khi transfer
        - Ensure adequate IV access
        - Ensure ETT secure
        - Prepare transfer team
        - Coordinate with receiving center
        """)
        
        st.markdown("---")
        st.markdown("##### 🔄 ECMO Types")
        
        ecmo_type = st.radio(
            "**Loại ECMO:**",
            ["VV-ECMO (Venovenous)", "VA-ECMO (Venous-Arterial)"],
            key="ecmo_type"
        )
        
        if ecmo_type == "VV-ECMO (Venovenous)":
            st.success("""
            **VV-ECMO - Ưu tiên cho ARDS:**
            
            **Chỉ định:**
            - ARDS với refractory hypoxemia/hypercapnia
            - Hemodynamically stable (không cần cardiac support)
            
            **Cannulation:**
            - Femoral vein → Internal jugular vein
            - Hoặc: Dual-lumen cannula (Avalon, etc.)
            
            **Advantages:**
            - Preserves native cardiac function
            - Lower complication rate
            - Easier to manage
            
            **Limitations:**
            - Không hỗ trợ tim
            - Cần native cardiac function tốt
            """)
        else:
            st.warning("""
            **VA-ECMO - Cho ARDS + Cardiac Failure:**
            
            **Chỉ định:**
            - ARDS + severe cardiac failure
            - ARDS + cardiogenic shock
            - Refractory to VV-ECMO
            
            **Cannulation:**
            - Femoral vein → Femoral artery
            - Hoặc: Central cannulation
            
            **Advantages:**
            - Hỗ trợ cả hô hấp và tim
            - Có thể dùng khi cardiac failure
            
            **Disadvantages:**
            - Higher complication rate
            - Limb ischemia risk
            - More complex management
            """)
        
        st.markdown("---")
        st.markdown("##### ⚠️ ECMO Complications")
        
        st.error("""
        **Major Complications:**
        
        **1. Bleeding (Most Common):**
        - Do anticoagulation required
        - Cannulation site bleeding
        - GI bleeding
        - Intracranial hemorrhage
        - **Prevention:** Careful anticoagulation monitoring
        
        **2. Thrombosis:**
        - Circuit thrombosis
        - Cannula thrombosis
        - **Prevention:** Adequate anticoagulation
        
        **3. Infection:**
        - Cannula site infection
        - Bloodstream infection
        - **Prevention:** Aseptic technique, monitoring
        
        **4. Limb Ischemia (VA-ECMO):**
        - Distal limb ischemia
        - **Prevention:** Distal perfusion catheter
        
        **5. Neurologic:**
        - Stroke
        - Intracranial hemorrhage
        - **Prevention:** Careful anticoagulation
        
        **6. Technical:**
        - Circuit failure
        - Cannula dislodgement
        - Oxygenator failure
        """)
        
        st.markdown("---")
        st.markdown("##### 📊 ECMO Outcomes")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.info("""
            **EOLIA Trial Results:**
            - **60-day mortality:** 35% (ECMO) vs 46% (control)
            - **Crossover:** 28% control → ECMO
            - **Complications:** Higher với ECMO
            
            **Key Points:**
            - Early ECMO (<7 days) = Better outcomes
            - Younger age = Better outcomes
            - Reversible cause = Better outcomes
            """)
        
        with col2:
            st.warning("""
            **Factors Associated with Poor Outcome:**
            - Age >60
            - Mechanical ventilation >7 days
            - Multiple organ failure
            - Non-reversible cause
            - Severe comorbidities
            
            **Recovery:**
            - Most survivors: Recovery trong 6-12 tháng
            - Long-term complications possible
            - Quality of life có thể giảm
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
        
        st.markdown("##### 🦠 COVID-19 ARDS - Dexamethasone Protocol")
        
        st.error("""
        **⚠️ QUAN TRỌNG: Dexamethasone là tiêu chuẩn vàng cho COVID-19 ARDS!**
        - **RECOVERY Trial:** Giảm mortality 35% ở bệnh nhân thở máy
        - **Chỉ định:** COVID-19 ARDS cần thở máy hoặc O₂
        - **Timing:** Sớm khi có chỉ định
        """)
        
        covid_ards = st.checkbox("**Bệnh nhân có COVID-19 ARDS?**", key="covid_ards")
        
        if covid_ards:
            st.markdown("---")
            st.markdown("**📋 COVID-19 ARDS Corticosteroid Protocol (RECOVERY Trial)**")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("**Chỉ định Dexamethasone:**")
                st.success("""
                ✅ **COVID-19 confirmed** (PCR positive)
                ✅ **ARDS** (Berlin criteria)
                ✅ **Cần O₂ support:**
                   - Thở máy (invasive/non-invasive)
                   - High-flow O₂
                   - O₂ >4 L/min
                ✅ **Không có contraindications**
                """)
                
                st.markdown("---")
                st.markdown("""
                **Contraindications:**
                ❌ **Active uncontrolled infection** (non-COVID)
                ❌ **Severe hyperglycemia** không kiểm soát được
                ❌ **Active GI bleeding**
                ❌ **Allergy to corticosteroids**
                """)
            
            with col2:
                st.markdown("**Dexamethasone Dosing Calculator:**")
                
                patient_weight_covid = st.number_input(
                    "**Cân nặng (kg):**",
                    min_value=40.0,
                    max_value=150.0,
                    value=70.0,
                    step=1.0,
                    key="covid_weight"
                )
                
                o2_support = st.selectbox(
                    "**Mức độ hỗ trợ O₂:**",
                    ["Thở máy (invasive)", "Non-invasive ventilation", "High-flow O₂", "O₂ >4 L/min"],
                    key="covid_o2"
                )
                
                # Dexamethasone dose: 6 mg/day for all (RECOVERY trial)
                dex_dose = 6.0  # Fixed dose regardless of weight
                
                st.markdown("---")
                st.markdown("**📊 Liều Dexamethasone:**")
                st.metric("**Daily Dose:**", f"{dex_dose:.0f} mg/day", 
                         help="6 mg/day IV hoặc PO (RECOVERY Trial)")
                st.metric("**Duration:**", "10 ngày", 
                         help="Hoặc đến khi xuất viện, tùy cái nào ngắn hơn")
                
                st.info("""
                **RECOVERY Trial Protocol:**
                - **Dose:** 6 mg/day (không phụ thuộc cân nặng)
                - **Route:** IV hoặc PO (tương đương)
                - **Duration:** 10 ngày hoặc đến khi xuất viện
                """)
            
            st.markdown("---")
            st.markdown("**📋 Dexamethasone Protocol Details:**")
            
            st.success("""
            **RECOVERY Trial - Dexamethasone Protocol:**
            
            **1. Indication:**
            - COVID-19 ARDS cần O₂ support
            - Thở máy (invasive/non-invasive)
            - High-flow O₂
            - O₂ >4 L/min
            
            **2. Dosing:**
            - **Dexamethasone:** 6 mg/day
            - **Route:** IV hoặc PO (tương đương)
            - **Timing:** Một lần/ngày (có thể chia 2 lần)
            - **Duration:** 10 ngày hoặc đến khi xuất viện
            
            **3. Results (RECOVERY Trial):**
            - **Thở máy:** Giảm mortality 35% (29.3% vs 41.4%)
            - **O₂ support:** Giảm mortality 20%
            - **No O₂:** Không có lợi ích, có thể có hại
            
            **4. Monitoring:**
            - Blood glucose (tăng nguy cơ hyperglycemia)
            - Signs of infection
            - GI bleeding
            - Blood pressure
            """)
            
            st.markdown("---")
            st.markdown("**⚠️ Lưu ý đặc biệt cho COVID-19:**")
            
            st.warning("""
            **1. Timing:**
            - Bắt đầu sớm khi có chỉ định
            - Không đợi đến khi ARDS nặng
            - Có thể dùng cùng lúc với remdesivir, tocilizumab
            
            **2. Hyperglycemia:**
            - COVID-19 + steroids → Tăng nguy cơ hyperglycemia
            - Theo dõi glucose thường xuyên
            - Có thể cần insulin
            
            **3. Infection Risk:**
            - Steroids ức chế miễn dịch
            - Theo dõi signs of secondary infection
            - Điều trị nhiễm trùng nếu có
            
            **4. Tapering:**
            - RECOVERY trial: Không cần taper (10 ngày rồi ngừng)
            - Nếu dùng >10 ngày: Có thể cần taper
            """)
        
        st.markdown("---")
        st.markdown("---")
        st.markdown("##### 💊 Non-COVID-19 ARDS - Methylprednisolone Protocol")
        
        st.markdown("**📋 DEXA-ARDS Trial Protocol (Non-COVID-19 ARDS):**")
        
        non_covid_ards = st.checkbox("**Bệnh nhân có Non-COVID-19 ARDS?**", key="non_covid_ards")
        
        if non_covid_ards:
            st.warning("""
            **⚠️ Lưu ý: Methylprednisolone cho non-COVID-19 ARDS có bằng chứng yếu hơn!**
            - DEXA-ARDS trial: Có thể có lợi ích nhưng không rõ ràng như COVID-19
            - Cân nhắc cẩn thận
            - Không dùng nếu nghi nhiễm trùng không kiểm soát được
            """)
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("**Chỉ định Methylprednisolone:**")
                st.info("""
                ✅ **Non-COVID-19 ARDS**
                ✅ **PaO₂/FiO₂ <200 mmHg**
                ✅ **Early:** Trong vòng 14 ngày từ khi ARDS
                ✅ **Không có uncontrolled infection**
                ✅ **Không có contraindications**
                """)
            
            with col2:
                st.markdown("**Methylprednisolone Dosing Calculator:**")
                
                patient_weight_non_covid = st.number_input(
                    "**Cân nặng (kg):**",
                    min_value=40.0,
                    max_value=150.0,
                    value=70.0,
                    step=1.0,
                    key="non_covid_weight"
                )
                
                # Calculate dosing
                mp_dose_day1_3 = patient_weight_non_covid * 1.0  # 1 mg/kg q12h
                mp_dose_day4_6 = patient_weight_non_covid * 1.0  # 1 mg/kg q24h
                mp_dose_day7_9 = patient_weight_non_covid * 0.5  # 0.5 mg/kg q24h
                mp_dose_day10_12 = patient_weight_non_covid * 0.25  # 0.25 mg/kg q24h
                
                st.markdown("---")
                st.markdown("**📊 Liều Methylprednisolone:**")
                st.metric("**Ngày 1-3:**", f"{mp_dose_day1_3:.0f} mg q12h", 
                         help="1 mg/kg IV q12h")
                st.metric("**Ngày 4-6:**", f"{mp_dose_day4_6:.0f} mg q24h", 
                         help="1 mg/kg IV q24h")
                st.metric("**Ngày 7-9:**", f"{mp_dose_day7_9:.0f} mg q24h", 
                         help="0.5 mg/kg IV q24h")
                st.metric("**Ngày 10-12:**", f"{mp_dose_day10_12:.0f} mg q24h", 
                         help="0.25 mg/kg IV q24h")
            
            st.markdown("---")
            st.markdown("**📋 DEXA-ARDS Trial Protocol:**")
            
            st.info("""
            **Methylprednisolone Protocol (14 ngày):**
            
            **Days 1-3:**
            - Methylprednisolone: 1 mg/kg IV q12h
            - Ví dụ: 70kg → 70mg IV q12h
            
            **Days 4-6:**
            - Methylprednisolone: 1 mg/kg IV q24h
            - Ví dụ: 70kg → 70mg IV q24h
            
            **Days 7-9:**
            - Methylprednisolone: 0.5 mg/kg IV q24h
            - Ví dụ: 70kg → 35mg IV q24h
            
            **Days 10-12:**
            - Methylprednisolone: 0.25 mg/kg IV q24h
            - Ví dụ: 70kg → 17.5mg IV q24h
            
            **Total Duration:** 12 ngày (có thể kéo dài đến 14 ngày)
            
            **Lợi ích (DEXA-ARDS Trial):**
            - Có thể giảm mortality (không rõ ràng)
            - Cải thiện oxygenation
            - Giảm số ngày thở máy
            
            **Lưu ý:**
            - Không dùng nếu nghi nhiễm trùng không kiểm soát được
            - Theo dõi glucose, infection
            - Có thể tăng nguy cơ neuromyopathy
            - Bằng chứng yếu hơn so với COVID-19
            """)
        
        st.markdown("---")
        st.markdown("##### 📊 So sánh Corticosteroids cho ARDS")
        
        import pandas as pd
        comparison_data = {
            "Thuốc": ["Dexamethasone", "Methylprednisolone"],
            "Chỉ định": ["COVID-19 ARDS", "Non-COVID-19 ARDS"],
            "Liều": ["6 mg/day", "1 mg/kg/day (tapering)"],
            "Duration": ["10 ngày", "12-14 ngày"],
            "Bằng chứng": ["Mạnh (RECOVERY)", "Yếu (DEXA-ARDS)"],
            "Giảm mortality": ["35% (thở máy)", "Không rõ ràng"]
        }
        
        st.dataframe(pd.DataFrame(comparison_data), use_container_width=True, hide_index=True)
        
        st.markdown("---")
        st.markdown("##### ⚠️ Monitoring & Complications")
        
        st.error("""
        **Monitoring Protocol:**
        
        **1. Blood Glucose:**
        - Check mỗi 6-12 giờ
        - Steroids → Hyperglycemia
        - Có thể cần insulin
        
        **2. Infection:**
        - Monitor signs of infection
        - Steroids ức chế miễn dịch
        - Có thể che dấu signs of infection
        
        **3. GI Complications:**
        - GI bleeding risk
        - Peptic ulcer risk
        - Cân nhắc PPI
        
        **4. Other:**
        - Blood pressure
        - Electrolytes (hypokalemia)
        - Fluid retention
        - Mood changes
        """)
    
    with tab5:
        st.markdown("#### 💨 Inhaled Nitric Oxide (iNO) - Rescue Therapy")
        
        st.warning("""
        **⚠️ QUAN TRỌNG: iNO KHÔNG routine - Chỉ dùng như rescue therapy!**
        
        **Evidence:**
        - **Không cải thiện mortality** trong ARDS
        - **Có thể cải thiện oxygenation** tạm thời
        - **Chi phí cao**
        - **Có thể có tác dụng phụ**
        """)
        
        st.markdown("---")
        st.markdown("##### 📋 Chỉ định iNO (Rescue Therapy)")
        
        use_ino = st.radio(
            "**Có chỉ định iNO?**",
            [
                "Có (Refractory hypoxemia - Rescue)",
                "Không (Routine không khuyến cáo)",
                "Không chắc chắn"
            ],
            key="ards_ino"
        )
        
        if use_ino == "Có (Refractory hypoxemia - Rescue)":
            st.error("""
            **🚨 CHỈ ĐỊNH iNO - RESCUE THERAPY:**
            
            **Chỉ định:**
            - **Refractory hypoxemia:** PaO₂/FiO₂ <100 mmHg
            - **Đã thử:** Lung protective ventilation, PEEP optimization, prone positioning
            - **Không đáp ứng:** Với các biện pháp trên
            - **Bridge therapy:** Trong khi chờ ECMO hoặc cải thiện
            - **Severe right heart failure:** Do ARDS (có thể giúp giảm PVR)
            
            **Liều:**
            - **Bắt đầu:** 5-10 ppm (parts per million)
            - **Titrate:** Tăng đến 20-40 ppm nếu cần
            - **Mục tiêu:** Cải thiện PaO₂/FiO₂ ≥20%
            - **Tối đa:** 40 ppm (không vượt quá)
            
            **Cách dùng:**
            - **Inhaled:** Qua ventilator circuit
            - **Monitoring:** NO và NO₂ levels liên tục
            - **Duration:** Ngắn hạn (24-48h), đánh giá lại thường xuyên
            
            **⚠️ Tác dụng phụ:**
            - **Methemoglobinemia:** Check MetHb mỗi 12-24h
            - **NO₂ toxicity:** Monitor NO₂ <2 ppm
            - **Renal toxicity:** Hiếm
            - **Rebound hypoxemia:** Khi ngừng iNO
            
            **Weaning:**
            - Giảm dần liều (5 ppm → 2.5 ppm → 1 ppm → 0)
            - Đánh giá đáp ứng sau mỗi lần giảm
            - Nếu PaO₂/FiO₂ giảm >20% → tăng lại liều
            - Tránh ngừng đột ngột (rebound effect)
            """)
            
            # iNO calculator
            col1, col2 = st.columns(2)
            
            with col1:
                current_pao2_fio2 = st.number_input(
                    "**PaO₂/FiO₂ hiện tại (mmHg):**",
                    min_value=50.0,
                    max_value=300.0,
                    value=80.0,
                    step=5.0,
                    key="ino_pao2_fio2"
                )
                
                ino_dose = st.number_input(
                    "**Liều iNO (ppm):**",
                    min_value=0.0,
                    max_value=40.0,
                    value=10.0,
                    step=1.0,
                    key="ino_dose"
                )
            
            with col2:
                st.markdown("**📊 Đánh giá đáp ứng:**")
                
                if current_pao2_fio2 < 100:
                    improvement_needed = 100 - current_pao2_fio2
                    st.warning(f"**Cần cải thiện:** ≥{improvement_needed:.0f} mmHg")
                    st.info("**Mục tiêu:** PaO₂/FiO₂ tăng ≥20% sau 30-60 phút")
                else:
                    st.success("**PaO₂/FiO₂ đã >100** - Có thể không cần iNO")
                
                if ino_dose > 0:
                    st.metric("**Liều iNO:**", f"{ino_dose:.0f} ppm")
                    if ino_dose > 40:
                        st.error("**⚠️ Liều quá cao!** Tối đa 40 ppm")
                    elif ino_dose > 20:
                        st.warning("**⚠️ Liều cao** - Theo dõi MetHb và NO₂ sát")
                    else:
                        st.success("**✅ Liều trong phạm vi an toàn**")
        
        elif use_ino == "Không (Routine không khuyến cáo)":
            st.success("""
            **✅ KHÔNG CẦN iNO:**
            
            **Lý do:**
            - iNO không cải thiện mortality trong ARDS
            - Chi phí cao
            - Có thể có tác dụng phụ
            - Chỉ dùng như rescue therapy khi thực sự cần
            
            **Ưu tiên điều trị:**
            1. Lung protective ventilation
            2. PEEP optimization
            3. Prone positioning
            4. Neuromuscular blockade (nếu cần)
            5. ECMO (nếu đủ chỉ định)
            
            **iNO chỉ dùng khi:**
            - Đã thử tất cả các biện pháp trên
            - Vẫn còn refractory hypoxemia
            - Cần bridge therapy
            """)
        
        else:  # Không chắc chắn
            st.info("""
            **Đánh giá lại:**
            - PaO₂/FiO₂ có <100 mmHg?
            - Đã thử lung protective ventilation, PEEP, prone?
            - Có refractory hypoxemia thực sự?
            - Có thể dùng ECMO không?
            
            **Nếu PaO₂/FiO₂ >100:** Không cần iNO
            **Nếu PaO₂/FiO₂ <100 và đã thử tất cả:** Cân nhắc iNO như rescue
            """)
        
        st.markdown("---")
        st.markdown("##### ⚠️ Monitoring iNO")
        
        st.warning("""
        **Monitoring khi dùng iNO:**
        
        **Continuous:**
        - **NO level:** Trong circuit (target: 5-40 ppm)
        - **NO₂ level:** <2 ppm (nguy hiểm nếu >2 ppm)
        - **SpO₂, PaO₂/FiO₂:** Đánh giá đáp ứng
        
        **Every 12-24h:**
        - **Methemoglobin (MetHb):** <5% (nguy hiểm nếu >10%)
        - **ABG:** PaO₂, PaCO₂, pH
        
        **Nếu MetHb >5%:**
        - Giảm liều iNO
        - Cân nhắc methylene blue nếu MetHb >10%
        - Có thể cần ngừng iNO
        
        **Nếu NO₂ >2 ppm:**
        - Giảm liều iNO ngay
        - Kiểm tra delivery system
        - Có thể cần ngừng iNO
        """)
        
        st.markdown("---")
        st.markdown("##### 🔄 Weaning iNO")
        
        st.info("""
        **Khi nào wean iNO:**
        - PaO₂/FiO₂ đã cải thiện và ổn định
        - Có thể duy trì oxygenation mà không cần iNO
        - Hoặc đã có ECMO
        
        **Weaning Protocol:**
        1. **Giảm dần liều:** 40 → 20 → 10 → 5 → 2.5 → 1 → 0 ppm
        2. **Mỗi bước:** Giảm 50% liều
        3. **Đánh giá:** Sau mỗi bước, đợi 30-60 phút
        4. **Nếu PaO₂/FiO₂ giảm >20%:** Tăng lại liều trước đó
        5. **Nếu ổn định:** Tiếp tục giảm
        
        **⚠️ Tránh:**
        - Ngừng đột ngột (rebound hypoxemia)
        - Giảm quá nhanh
        - Không theo dõi đáp ứng
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
    
    # References section
    references = get_references("ARDS")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-01-15",
            show_evidence_level=True,
            show_links=True
        )
    
    st.markdown("---")
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất.")

