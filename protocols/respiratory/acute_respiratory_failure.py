"""
Acute Respiratory Failure Protocol
ATS/ERS 2017, SCCM 2017
Management of acute respiratory failure (non-ARDS)
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Acute Respiratory Failure Protocol"""
    st.subheader("🫁 Acute Respiratory Failure (Non-ARDS)")
    st.caption("ATS/ERS 2017, SCCM 2017 - Management of acute respiratory failure")
    
    st.warning("""
    **⚠️ ACUTE RESPIRATORY FAILURE = URGENT ASSESSMENT REQUIRED**
    
    **Định nghĩa:**
    - **Type 1 (Hypoxemic):** PaO₂ < 60 mmHg hoặc SpO₂ < 90% với FiO₂ ≥ 0.21
    - **Type 2 (Hypercapnic):** PaCO₂ > 50 mmHg với pH < 7.35
    
    **Triệu chứng:**
    - Khó thở, tăng công thở
    - Tím tái, vã mồ hôi
    - Lú lẫn, kích động
    - Mệt mỏi cơ hô hấp
    """)
    
    st.markdown("---")
    
    # ========== SECTION 1: CLASSIFICATION ==========
    st.markdown("### 📊 Phân Loại")
    
    failure_type = st.radio(
        "**Loại suy hô hấp:**",
        ["Type 1 (Hypoxemic)", "Type 2 (Hypercapnic)", "Mixed (Type 1 + Type 2)"],
        key="respiratory_failure_type"
    )
    
    st.markdown("---")
    
    if failure_type == "Type 1 (Hypoxemic)":
        render_type1_protocol()
    elif failure_type == "Type 2 (Hypercapnic)":
        render_type2_protocol()
    else:
        render_mixed_protocol()
    
    st.markdown("---")
    
    # ========== SECTION 2: CAUSES ==========
    st.markdown("### 🔍 Nguyên Nhân")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Type 1 (Hypoxemic):**
        - **Pneumonia:** Viêm phổi
        - **Pulmonary Embolism:** Thuyên tắc phổi
        - **Heart Failure:** Suy tim (pulmonary edema)
        - **Atelectasis:** Xẹp phổi
        - **ARDS:** (đã có protocol riêng)
        - **Interstitial Lung Disease:** Bệnh phổi kẽ
        - **Pneumothorax:** Tràn khí màng phổi
        
        **Type 2 (Hypercapnic):**
        - **COPD Exacerbation:** Đợt cấp COPD
        - **Asthma:** Hen phế quản
        - **Neuromuscular:** Bệnh thần kinh cơ
        - **CNS Depression:** Ức chế thần kinh trung ương
        - **Chest Wall Deformity:** Biến dạng thành ngực
        """)
    
    with col2:
        st.markdown("""
        **Mixed (Type 1 + Type 2):**
        - **Severe Pneumonia:** Viêm phổi nặng
        - **Severe COPD:** COPD nặng
        - **Neuromuscular Disease:** Bệnh thần kinh cơ nặng
        - **Drug Overdose:** Ngộ độc thuốc
        - **Trauma:** Chấn thương ngực
        """)
    
    st.markdown("---")
    
    # ========== SECTION 3: INITIAL ASSESSMENT ==========
    st.markdown("### ⚡ Đánh Giá Ban Đầu")
    
    with st.expander("🔍 Xem đánh giá ban đầu", expanded=True):
        st.markdown("""
        **1. ABC (Airway, Breathing, Circulation):**
        - **Airway:** Kiểm tra tắc nghẽn, đảm bảo thông thoáng
        - **Breathing:** Đánh giá tần số thở, độ sâu, công thở
        - **Circulation:** Đánh giá mạch, huyết áp, tưới máu
        
        **2. Dấu hiệu nguy hiểm:**
        - Khó thở nặng, không nói được câu
        - Tần số thở < 8 hoặc > 30 lần/phút
        - SpO₂ < 90% với O₂ hỗ trợ
        - Lú lẫn, kích động, hôn mê
        - Mệt mỏi cơ hô hấp
        - Tím tái
        
        **3. Xét nghiệm cần thiết:**
        - **ABG:** Đánh giá PaO₂, PaCO₂, pH, HCO₃⁻
        - **Chest X-ray:** Đánh giá phổi, tim
        - **ECG:** Loại trừ nguyên nhân tim
        - **Labs:** CBC, BNP (nếu nghi ngờ suy tim)
        """)
    
    st.markdown("---")
    
    # ========== SECTION 4: OXYGEN THERAPY ==========
    st.markdown("### 💨 Oxygen Therapy")
    
    with st.expander("📋 Xem liệu pháp oxy", expanded=False):
        st.markdown("""
        **Mục tiêu:**
        - **SpO₂:** 94-98% (Người lớn), 92-96% (COPD)
        - **PaO₂:** 60-100 mmHg
        - **Tránh hyperoxia:** SpO₂ > 98% không cần thiết
        
        **Phương pháp:**
        
        **1. Low-flow systems:**
        - **Nasal cannula:** 1-6 L/min (FiO₂ ~24-44%)
        - **Simple face mask:** 5-10 L/min (FiO₂ ~40-60%)
        - **Partial rebreather:** 10-15 L/min (FiO₂ ~60-80%)
        - **Non-rebreather:** 10-15 L/min (FiO₂ ~80-95%)
        
        **2. High-flow systems:**
        - **High-flow nasal cannula (HFNC):** 20-60 L/min, FiO₂ 0.21-1.0
          - Ưu điểm: Làm ẩm, ấm, PEEP tự nhiên
          - Chỉ định: Type 1, Type 2 nhẹ-trung bình
        
        **3. Non-invasive Ventilation (NIV):**
        - **CPAP:** Áp lực dương liên tục
        - **BiPAP:** Áp lực dương hai mức
          - IPAP: 8-20 cmH₂O
          - EPAP: 4-8 cmH₂O
          - Chỉ định: Type 2, Type 1 do suy tim
        """)
    
    st.markdown("---")
    
    # ========== SECTION 5: INTUBATION CRITERIA ==========
    st.markdown("### 🔌 Chỉ Định Đặt Nội Khí Quản")
    
    with st.expander("⚠️ Xem chỉ định đặt nội khí quản", expanded=False):
        st.markdown("""
        **Chỉ định tuyệt đối:**
        - Ngừng thở
        - Tắc nghẽn đường thở
        - Mất phản xạ bảo vệ đường thở
        - Sốc nặng
        
        **Chỉ định tương đối:**
        - **Type 1:**
          - SpO₂ < 90% với FiO₂ ≥ 0.6
          - PaO₂/FiO₂ < 150
          - Tăng công thở nặng
          - Mệt mỏi cơ hô hấp
        - **Type 2:**
          - pH < 7.25 với PaCO₂ tăng
          - PaCO₂ > 60 mmHg với pH < 7.30
          - Mệt mỏi cơ hô hấp
          - Lú lẫn, hôn mê
        
        **Rapid Sequence Intubation (RSI):**
        - **Pre-oxygenation:** 100% O₂ x 3-5 phút
        - **Induction:** Etomidate 0.3 mg/kg hoặc Propofol 1-2 mg/kg
        - **Paralysis:** Succinylcholine 1-1.5 mg/kg hoặc Rocuronium 0.6-1.2 mg/kg
        - **Cricoid pressure:** Áp dụng trong RSI
        """)
    
    st.markdown("---")
    
    # ========== SECTION 6: VENTILATOR SETTINGS ==========
    st.markdown("### 🫁 Ventilator Settings")
    
    with st.expander("⚙️ Xem cài đặt máy thở", expanded=False):
        st.markdown("""
        **Initial Settings:**
        
        **Mode:** Volume Assist-Control (AC) hoặc Pressure Control (PC)
        
        **Type 1 (Hypoxemic):**
        - **Tidal Volume:** 6-8 mL/kg IBW
        - **Rate:** 12-20 lần/phút
        - **FiO₂:** Bắt đầu 1.0, giảm dần
        - **PEEP:** 5-10 cmH₂O (tăng nếu cần)
        - **I:E ratio:** 1:2
        
        **Type 2 (Hypercapnic):**
        - **Tidal Volume:** 6-8 mL/kg IBW
        - **Rate:** 12-20 lần/phút (tăng nếu cần để giảm CO₂)
        - **FiO₂:** Đủ để SpO₂ 92-96%
        - **PEEP:** 5-8 cmH₂O
        - **I:E ratio:** 1:2-1:3
        
        **Titration:**
        - **FiO₂:** Giảm để SpO₂ 94-98%
        - **PEEP:** Tăng nếu PaO₂/FiO₂ < 200
        - **Rate:** Điều chỉnh để PaCO₂ 35-45 mmHg
        - **Tidal Volume:** Giảm nếu plateau pressure > 30 cmH₂O
        """)
    
    st.markdown("---")
    
    # ========== SECTION 7: MONITORING ==========
    st.markdown("### 📈 Monitoring")
    
    st.markdown("""
    **Theo dõi sát:**
    - **Hô hấp:** Tần số, độ sâu, công thở, SpO₂
    - **ABG:** q4-6h hoặc khi thay đổi điều trị
    - **Chest X-ray:** Hàng ngày hoặc khi có thay đổi
    - **Ventilator:** Peak pressure, plateau pressure, auto-PEEP
    - **Hemodynamics:** BP, HR, CVP (nếu có)
    
    **Mục tiêu:**
    - **SpO₂:** 94-98% (92-96% nếu COPD)
    - **PaO₂:** 60-100 mmHg
    - **PaCO₂:** 35-45 mmHg (hoặc baseline nếu COPD)
    - **pH:** 7.35-7.45
    - **Plateau pressure:** < 30 cmH₂O
    """)
    
    st.markdown("---")
    
    # ========== SECTION 8: WEANING ==========
    st.markdown("### 🔄 Weaning & Extubation")
    
    with st.expander("✅ Xem tiêu chuẩn cai máy thở", expanded=False):
        st.markdown("""
        **Tiêu chuẩn cai máy thở:**
        - Nguyên nhân suy hô hấp đã được điều trị
        - Hemodynamically stable
        - SpO₂ ≥ 90% với FiO₂ ≤ 0.4
        - PEEP ≤ 8 cmH₂O
        - Có phản xạ bảo vệ đường thở
        - Không cần vasopressors liều cao
        
        **Spontaneous Breathing Trial (SBT):**
        - **Mode:** CPAP 5 cmH₂O hoặc T-piece
        - **Thời gian:** 30-120 phút
        - **Theo dõi:** Tần số thở, SpO₂, công thở, ABG
        
        **Tiêu chuẩn extubation:**
        - SBT thành công
        - GCS ≥ 13
        - Có phản xạ ho, nuốt
        - Secretions ít
        """)
    
    st.markdown("---")
    
    # ========== SECTION 9: SPECIAL POPULATIONS ==========
    st.markdown("### 👥 Special Populations")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Người cao tuổi:**
        - Ngưỡng intubation thấp hơn
        - Tỷ lệ biến chứng cao hơn
        - Cần cân nhắc chất lượng cuộc sống
        
        **COPD:**
        - Mục tiêu SpO₂: 92-96% (tránh hyperoxia)
        - Cho phép hypercapnia (pH ≥ 7.25)
        - NIV là lựa chọn đầu tay cho Type 2
        """)
    
    with col2:
        st.markdown("""
        **Trẻ em:**
        - Tidal volume: 5-8 mL/kg
        - Rate: Age-dependent
        - PEEP: 3-5 cmH₂O
        - FiO₂: Bắt đầu 0.4-0.6
        
        **Phụ nữ có thai:**
        - Tăng nhu cầu O₂
        - Giảm FRC
        - Cần intubation sớm hơn
        """)
    
    st.markdown("---")
    
    # ========== SECTION 10: REFERENCES ==========
    render_references_section(get_references("acute_respiratory_failure"))
    
    st.markdown("---")
    
    # Footer
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất.")


def render_type1_protocol():
    """Type 1 (Hypoxemic) Protocol"""
    st.error("## 🫁 TYPE 1 (HYPOXEMIC) RESPIRATORY FAILURE")
    
    st.markdown("""
    **Quy trình:**
    
    1. **Oxygen Therapy:**
       - Bắt đầu với nasal cannula 2-4 L/min
       - Tăng lên face mask nếu cần
       - Cân nhắc HFNC nếu SpO₂ < 90% với O₂ thông thường
    
    2. **Nếu SpO₂ vẫn < 90% với FiO₂ ≥ 0.6:**
       - Cân nhắc NIV (CPAP/BiPAP) nếu do suy tim
       - Cân nhắc intubation nếu:
         - PaO₂/FiO₂ < 150
         - Tăng công thở nặng
         - Mệt mỏi cơ hô hấp
    
    3. **Ventilator Settings:**
       - **Mode:** Volume AC hoặc Pressure Control
       - **Tidal Volume:** 6-8 mL/kg IBW
       - **Rate:** 12-20 lần/phút
       - **FiO₂:** Bắt đầu 1.0, giảm dần
       - **PEEP:** 5-10 cmH₂O (tăng nếu cần)
    
    4. **Điều trị nguyên nhân:**
       - **Pneumonia:** Kháng sinh
       - **PE:** Anticoagulation, thrombolytics
       - **Heart Failure:** Diuretics, vasodilators
       - **Atelectasis:** Chest physiotherapy
    """)
    
    st.info("""
    **💡 Mẹo quan trọng:**
    - Type 1 thường do shunt hoặc V/Q mismatch
    - PEEP có thể cải thiện oxygenation
    - Tránh hyperoxia không cần thiết
    - Điều trị nguyên nhân là quan trọng nhất
    """)


def render_type2_protocol():
    """Type 2 (Hypercapnic) Protocol"""
    st.warning("## ⚠️ TYPE 2 (HYPERCAPNIC) RESPIRATORY FAILURE")
    
    st.markdown("""
    **Quy trình:**
    
    1. **Oxygen Therapy:**
       - Mục tiêu SpO₂: 92-96% (tránh hyperoxia)
       - Bắt đầu với nasal cannula 1-2 L/min
       - Tăng từ từ nếu cần
    
    2. **NIV (Non-invasive Ventilation):**
       - **Chỉ định:** pH < 7.35 với PaCO₂ > 45 mmHg
       - **Mode:** BiPAP
       - **IPAP:** 8-20 cmH₂O
       - **EPAP:** 4-8 cmH₂O
       - **FiO₂:** Đủ để SpO₂ 92-96%
    
    3. **Nếu NIV thất bại hoặc chống chỉ định:**
       - Cân nhắc intubation nếu:
         - pH < 7.25
         - PaCO₂ > 60 mmHg với pH < 7.30
         - Mệt mỏi cơ hô hấp
         - Lú lẫn, hôn mê
    
    4. **Ventilator Settings:**
       - **Mode:** Volume AC hoặc Pressure Control
       - **Tidal Volume:** 6-8 mL/kg IBW
       - **Rate:** 12-20 lần/phút (tăng nếu cần)
       - **FiO₂:** Đủ để SpO₂ 92-96%
       - **PEEP:** 5-8 cmH₂O
    
    5. **Điều trị nguyên nhân:**
       - **COPD:** Bronchodilators, corticosteroids
       - **Asthma:** Bronchodilators, corticosteroids
       - **Neuromuscular:** Điều trị bệnh nền
       - **CNS Depression:** Điều trị nguyên nhân
    """)
    
    st.info("""
    **💡 Mẹo quan trọng:**
    - NIV là lựa chọn đầu tay cho Type 2
    - Cho phép hypercapnia nhẹ (pH ≥ 7.25)
    - Tránh hyperoxia (có thể làm giảm drive thở)
    - Điều chỉnh PaCO₂ từ từ (tránh alkalosis)
    """)


def render_mixed_protocol():
    """Mixed (Type 1 + Type 2) Protocol"""
    st.error("## 🚨 MIXED (TYPE 1 + TYPE 2) RESPIRATORY FAILURE")
    
    st.markdown("""
    **Quy trình:**
    
    1. **Oxygen Therapy:**
       - Bắt đầu với face mask hoặc HFNC
       - Mục tiêu SpO₂: 94-98%
       - Cẩn thận với hyperoxia (đặc biệt nếu COPD)
    
    2. **NIV:**
       - Cân nhắc nếu:
         - Type 2 component nhẹ-trung bình
         - Không có chống chỉ định
       - **Mode:** BiPAP
       - **IPAP:** 10-20 cmH₂O
       - **EPAP:** 6-10 cmH₂O
    
    3. **Intubation:**
       - Chỉ định sớm hơn nếu:
         - Type 1 nặng (PaO₂/FiO₂ < 150)
         - Type 2 nặng (pH < 7.25)
         - Mệt mỏi cơ hô hấp
    
    4. **Ventilator Settings:**
       - **Mode:** Volume AC hoặc Pressure Control
       - **Tidal Volume:** 6-8 mL/kg IBW
       - **Rate:** 14-20 lần/phút
       - **FiO₂:** Bắt đầu 0.6-1.0, giảm dần
       - **PEEP:** 5-10 cmH₂O
    
    5. **Điều trị nguyên nhân:**
       - Điều trị cả Type 1 và Type 2 components
       - Cân nhắc bronchodilators nếu có component tắc nghẽn
    """)
    
    st.info("""
    **💡 Mẹo quan trọng:**
    - Mixed failure có tiên lượng xấu hơn
    - Cần cân bằng giữa oxygenation và ventilation
    - Intubation sớm có thể cần thiết
    - Điều trị nguyên nhân là quan trọng nhất
    """)

