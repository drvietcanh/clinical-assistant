"""
Tricyclic Antidepressant (TCA) Overdose Protocol
AACT Poison Control Guidelines, UpToDate 2024
Life-threatening overdose with high mortality
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """TCA Overdose Management Protocol"""
    st.subheader("💊 Ngộ Độc TCA (Tricyclic Antidepressant Overdose)")
    st.caption("AACT Poison Control Guidelines, UpToDate 2024 - Life-threatening overdose")
    
    st.error("""
    **⚠️ NGỘ ĐỘC TCA = CẤP CỨU Y KHOA - TỬ VONG CAO**
    
    **Triệu chứng Điển Hình (Anticholinergic + Cardiotoxic):**
    - **Tim mạch:** Loạn nhịp (VT, VF), QRS giãn rộng, hạ huyết áp
    - **Thần kinh:** Giảm ý thức, co giật, hôn mê
    - **Anticholinergic:** Khô miệng, giãn đồng tử, bí tiểu, sốt
    - **Hô hấp:** Suy hô hấp, ngừng thở
    
    **Các TCA thường gặp:**
    - Amitriptyline, Imipramine, Doxepin
    - Nortriptyline, Desipramine
    - Clomipramine
    """)
    
    st.markdown("---")
    
    st.markdown("### ⚡ Xử trí ngay lập tức (ABC)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.error("""
        **1. AIRWAY & BREATHING**
        
        **Intubation:**
        - **Chỉ định sớm** nếu:
          - Giảm ý thức (GCS <8)
          - Suy hô hấp
          - Co giật
          - QRS >100 ms
        
        **Ventilation:**
        - PEEP thấp (tránh hạ huyết áp)
        - Monitor CO₂ (có thể tăng)
        
        **2. CIRCULATION**
        
        **Monitoring:**
        - **Continuous ECG** (loạn nhịp đột ngột)
        - **Arterial line** (hạ huyết áp nhanh)
        - **Central line** (nếu cần inotropes)
        
        **Truyền dịch:**
        - **NS bolus:** 500-1000 mL
        - Thận trọng (có thể làm nặng phù phổi)
        """)
    
    with col2:
        st.warning("""
        **3. DECONTAMINATION**
        
        **Activated Charcoal:**
        - **Chỉ nếu:** <1-2h sau uống, ý thức tỉnh
        - **Liều:** 50-100 g PO/NG
        - **Chống chỉ định:**
          - Giảm ý thức
          - Không có phản xạ bảo vệ đường thở
          - Rối loạn nuốt
        
        **Gastric Lavage:**
        - **Chỉ nếu:** Uống lượng lớn <1h, ý thức tỉnh
        - **Thận trọng:** Có thể gây co giật
        
        **4. LABS NGAY:**
        - **ECG:** QRS width, QT interval
        - **ABG:** pH, CO₂
        - **Electrolytes:** Na, K, Mg
        - **TCA level:** (nếu có, nhưng không chờ kết quả)
        """)
    
    st.markdown("---")
    
    st.markdown("### 📊 Đánh giá Mức độ Nghiêm trọng")
    
    # QRS width assessment
    qrs_width = st.number_input(
        "**QRS width (ms):**",
        min_value=0,
        max_value=300,
        value=0,
        step=10,
        help="Đo QRS width trên ECG"
    )
    
    if qrs_width > 0:
        if qrs_width < 100:
            st.success("✅ **QRS bình thường** - Nguy cơ thấp")
        elif qrs_width < 120:
            st.warning("⚠️ **QRS giãn nhẹ** - Theo dõi sát")
        elif qrs_width < 160:
            st.error("🚨 **QRS giãn trung bình** - Nguy cơ cao, cần điều trị")
        else:
            st.error("🚨🚨 **QRS giãn rộng nặng** - Nguy cơ rất cao, điều trị ngay!")
    
    # GCS assessment
    gcs = st.number_input(
        "**Glasgow Coma Scale:**",
        min_value=3,
        max_value=15,
        value=15,
        step=1,
        help="Đánh giá mức độ ý thức"
    )
    
    if gcs < 8:
        st.error("🚨 **Giảm ý thức nặng** - Cần intubation ngay!")
    elif gcs < 13:
        st.warning("⚠️ **Giảm ý thức** - Theo dõi sát, chuẩn bị intubation")
    
    st.markdown("---")
    
    st.markdown("### 💉 Điều trị Đặc hiệu")
    
    # Check for indications
    has_qrs_widening = st.checkbox("QRS giãn rộng (>100 ms)", key="tca_qrs")
    has_arrhythmia = st.checkbox("Loạn nhịp tim (VT/VF)", key="tca_arrhythmia")
    has_hypotension = st.checkbox("Hạ huyết áp", key="tca_hypotension")
    has_seizure = st.checkbox("Co giật", key="tca_seizure")
    
    st.markdown("---")
    
    if has_qrs_widening or has_arrhythmia:
        st.error("## 🚨 ĐIỀU TRỊ CARDIOTOXICITY")
        
        st.success("""
        **1. SODIUM BICARBONATE (Thuốc đầu tay)**
        
        **Chỉ định:**
        - QRS >100 ms
        - Loạn nhịp tim (VT, VF)
        - Hạ huyết áp
        
        **Liều:**
        - **Bolus:** 1-2 mEq/kg IV (thường 50-100 mEq)
        - **Lặp lại:** Mỗi 3-5 phút nếu QRS vẫn giãn
        - **Truyền liên tục:** 150 mEq trong 1L D5W, 100-200 mL/h
        - **Mục tiêu:** pH 7.50-7.55, QRS <100 ms
        
        **Cơ chế:**
        - Tăng pH → Giảm gắn TCA vào kênh Na⁺
        - Giảm QRS width
        - Cải thiện huyết động
        
        **Theo dõi:**
        - ECG liên tục (QRS width)
        - ABG (pH, CO₂)
        - Điện giải (Na, K)
        """)
        
        if has_arrhythmia:
            st.warning("""
            **2. LOẠN NHỊP TIM**
            
            **VT/VF:**
            - **Defibrillation:** 200J → 300J → 360J
            - **Sodium Bicarbonate:** Tiếp tục
            - **Amiodarone:** 150 mg IV bolus (nếu cần)
            
            **Bradycardia:**
            - **Atropine:** Thường không hiệu quả
            - **Pacing:** Nếu cần
            - **Sodium Bicarbonate:** Tiếp tục
            """)
    
    if has_hypotension:
        st.warning("""
        **3. HẠ HUYẾT ÁP**
        
        **Điều trị:**
        1. **Sodium Bicarbonate:** (ưu tiên)
        2. **Truyền dịch:** NS 500-1000 mL bolus
        3. **Norepinephrine:** 0.05-0.2 mcg/kg/min
           - Tránh dopamine (có thể gây loạn nhịp)
        
        **Lưu ý:**
        - Sodium bicarbonate thường cải thiện huyết áp
        - Tránh truyền dịch quá nhiều
        """)
    
    if has_seizure:
        st.error("""
        **4. CO GIẬT**
        
        **Điều trị:**
        - **Benzodiazepines:**
          - **Lorazepam:** 2-4 mg IV (ưu tiên)
          - **Diazepam:** 5-10 mg IV
          - **Midazolam:** 2-5 mg IV
        
        - **Nếu không đáp ứng:**
          - **Phenobarbital:** 15-20 mg/kg IV
          - **Propofol:** 1-2 mg/kg IV (nếu intubated)
        
        **Lưu ý:**
        - Co giật có thể kéo dài
        - Cần intubation nếu co giật nặng
        - Sodium bicarbonate có thể giúp giảm co giật
        """)
    
    st.markdown("---")
    
    st.markdown("### 📋 Điều trị Hỗ trợ")
    
    st.info("""
    **1. Hạ thân nhiệt (Nếu sốt):**
    - **Paracetamol:** 1 g IV/PO
    - **Cooling:** Tấm lạnh, quạt
    - **Mục tiêu:** Nhiệt độ <38°C
    
    **2. Bí tiểu:**
    - **Foley catheter:** Nếu cần
    - Theo dõi cân bằng nước
    
    **3. Rối loạn điện giải:**
    - **Hạ K:** Bổ sung K
    - **Hạ Mg:** Bổ sung Mg
    
    **4. Theo dõi:**
    - **ECG:** Liên tục 24-48h
    - **QRS width:** Mỗi 1-2h
    - **ABG:** Nếu dùng sodium bicarbonate
    - **TCA level:** (nếu có, nhưng không chờ)
    """)
    
    st.markdown("---")
    
    st.markdown("### ⚠️ Chống chỉ định & Lưu ý")
    
    st.warning("""
    **KHÔNG dùng:**
    
    **1. Class IA/IC Antiarrhythmics:**
    - Procainamide, Flecainide
    - Làm nặng cardiotoxicity
    
    **2. Flumazenil:**
    - Có thể gây co giật
    
    **3. Physostigmine:**
    - Có thể gây co giật, loạn nhịp
    - Chỉ dùng trong trường hợp đặc biệt
    
    **4. Forced Diuresis:**
    - Không hiệu quả
    - Có thể làm nặng hạ huyết áp
    """)
    
    st.markdown("---")
    
    st.markdown("### 📈 Tiên lượng & Theo dõi")
    
    st.info("""
    **Tiên lượng:**
    - **Tử vong:** 2-5% (nếu điều trị đúng)
    - **Yếu tố nguy cơ:**
      - QRS >160 ms
      - Hạ huyết áp nặng
      - Co giật
      - Giảm ý thức nặng
      - Uống lượng lớn
    
    **Theo dõi:**
    - **ICU:** Ít nhất 24h
    - **ECG:** Liên tục 24-48h
    - **QRS:** Mỗi 1-2h (cho đến khi <100 ms)
    - **Huyết áp:** Mỗi 1-2h
    
    **Xuất viện:**
    - QRS <100 ms
    - Huyết áp ổn định
    - Ý thức tỉnh
    - Không loạn nhịp
    - Theo dõi ít nhất 24h
    """)
    
    st.markdown("---")
    
    st.markdown("### 👥 Điều chỉnh theo Đặc điểm Bệnh nhân")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Người cao tuổi:**
        - Nguy cơ cao hơn
        - Thận trọng với sodium bicarbonate (quá tải Na)
        - Theo dõi sát chức năng thận
        
        **Trẻ em:**
        - Liều sodium bicarbonate: 1-2 mEq/kg
        - Thận trọng với truyền dịch
        - Theo dõi sát hơn
        """)
    
    with col2:
        st.markdown("""
        **Suy thận:**
        - Thận trọng với sodium bicarbonate
        - Có thể cần lọc máu
        - Theo dõi sát điện giải
        
        **Có thai:**
        - Sodium bicarbonate an toàn
        - Tránh các thuốc chống chỉ định
        - Theo dõi thai nhi
        """)
    
    st.markdown("---")
    
    # References
    references = get_references("TCA Overdose")
    if references:
        render_references_section(references)
    else:
        st.markdown("### 📚 References")
        st.markdown("""
        1. **AACT Poison Control Guidelines** - American Academy of Clinical Toxicology
        2. **UpToDate:** Tricyclic Antidepressant Poisoning - Last updated 2024
        3. **Goldfrank's Toxicologic Emergencies** - 11th Edition
        """)
    
    st.markdown("---")
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều trị ngộ độc TCA cần chuyên khoa độc chất. Gọi trung tâm chống độc nếu có.")

