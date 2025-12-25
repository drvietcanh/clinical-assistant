"""
Digoxin Toxicity Protocol
AHA/ACC Guidelines 2024, UpToDate 2024
Life-threatening cardiac toxicity
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Digoxin Toxicity Management Protocol"""
    st.subheader("💊 Ngộ Độc Digoxin (Digoxin Toxicity)")
    st.caption("AHA/ACC Guidelines 2024, UpToDate 2024 - Life-threatening cardiac toxicity")
    
    st.error("""
    **⚠️ NGỘ ĐỘC DIGOXIN = CẤP CỨU Y KHOA**
    
    **Triệu chứng Điển Hình:**
    - **Tim mạch:** Loạn nhịp (VT, VF, bradycardia, AV block), rung nhĩ
    - **Thần kinh:** Mệt mỏi, yếu cơ, lú lẫn, rối loạn thị giác (vàng/xanh)
    - **Tiêu hóa:** Buồn nôn, nôn, đau bụng, tiêu chảy
    - **Điện giải:** Hạ K, hạ Mg (làm nặng độc tính)
    
    **Yếu tố nguy cơ:**
    - Suy thận (giảm thải trừ)
    - Hạ K, hạ Mg
    - Tương tác thuốc (amiodarone, verapamil, quinidine)
    - Người cao tuổi
    - Liều cao
    """)
    
    st.markdown("---")
    
    st.markdown("### ⚡ Xử trí ngay lập tức (ABC)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.error("""
        **1. AIRWAY & BREATHING**
        
        **Intubation:**
        - Nếu giảm ý thức nặng
        - Suy hô hấp
        - Co giật
        
        **2. CIRCULATION**
        
        **Monitoring:**
        - **Continuous ECG** (loạn nhịp đột ngột)
        - **Arterial line** (nếu hạ huyết áp)
        - **Central line** (nếu cần inotropes)
        
        **Truyền dịch:**
        - **NS:** Nếu hạ huyết áp
        - Thận trọng (có thể quá tải)
        """)
    
    with col2:
        st.warning("""
        **3. DECONTAMINATION**
        
        **Activated Charcoal:**
        - **Chỉ nếu:** <1-2h sau uống, ý thức tỉnh
        - **Liều:** 50-100 g PO/NG
        - **Chống chỉ định:**
          - Giảm ý thức
          - Không có phản xạ bảo vệ
        
        **4. LABS NGAY:**
        - **Digoxin level:** (quan trọng nhưng không chờ)
        - **ECG:** Loạn nhịp, AV block
        - **Electrolytes:** K, Mg, Ca
        - **Creatinine:** Đánh giá chức năng thận
        - **BUN:** Đánh giá chức năng thận
        """)
    
    st.markdown("---")
    
    st.markdown("### 📊 Đánh giá Mức độ Nghiêm trọng")
    
    # Digoxin level
    digoxin_level = st.number_input(
        "**Nồng độ Digoxin (ng/mL):**",
        min_value=0.0,
        max_value=10.0,
        value=0.0,
        step=0.1,
        help="Nồng độ digoxin trong máu"
    )
    
    if digoxin_level > 0:
        if digoxin_level < 2.0:
            st.success("✅ **Nồng độ điều trị** - Nguy cơ thấp")
        elif digoxin_level < 4.0:
            st.warning("⚠️ **Nồng độ tăng** - Theo dõi sát")
        elif digoxin_level < 6.0:
            st.error("🚨 **Nồng độ độc** - Nguy cơ cao, cần điều trị")
        else:
            st.error("🚨🚨 **Nồng độ rất độc** - Nguy cơ rất cao, điều trị ngay!")
    
    # Potassium level
    potassium = st.number_input(
        "**Nồng độ Kali (mEq/L):**",
        min_value=0.0,
        max_value=10.0,
        value=4.0,
        step=0.1,
        help="Nồng độ kali trong máu"
    )
    
    if potassium < 3.5:
        st.error("🚨 **Hạ K** - Làm nặng độc tính digoxin, bổ sung ngay!")
    elif potassium > 5.5:
        st.warning("⚠️ **Tăng K** - Có thể do độc tính nặng")
    
    # Check for arrhythmia
    has_arrhythmia = st.checkbox("Loạn nhịp tim (VT/VF/bradycardia)", key="dig_arrhythmia")
    has_av_block = st.checkbox("AV block", key="dig_av_block")
    has_hypotension = st.checkbox("Hạ huyết áp", key="dig_hypotension")
    has_hyperkalemia = st.checkbox("Tăng K (>5.5 mEq/L)", key="dig_hyperkalemia")
    
    st.markdown("---")
    
    st.markdown("### 💉 Điều trị Đặc hiệu")
    
    if has_arrhythmia or has_av_block or has_hypotension or has_hyperkalemia:
        st.error("## 🚨 ĐIỀU TRỊ NGỘ ĐỘC NẶNG - DIGIBIND")
        
        st.success("""
        **1. DIGOXIN-SPECIFIC ANTIBODY FRAGMENTS (Digibind/Digifab)**
        
        **Chỉ định:**
        - Loạn nhịp tim đe dọa tính mạng (VT, VF)
        - AV block độ 2-3
        - Hạ huyết áp nặng
        - Tăng K >5.5 mEq/L
        - Nồng độ digoxin >10 ng/mL
        - Suy thận nặng
        
        **Liều:**
        - **Nếu biết lượng uống:**
          - **Số ống = (Lượng uống mg) / 0.6**
          - Làm tròn lên
        
        - **Nếu biết nồng độ:**
          - **Số ống = (Nồng độ ng/mL × Cân nặng kg) / 100**
          - Làm tròn lên
        
        - **Nếu không biết:**
          - **10-20 ống** (người lớn)
          - **5-10 ống** (trẻ em)
        
        **Cách dùng:**
        - Pha trong 50-100 mL NS
        - Truyền IV trong 30 phút
        - Có thể bolus nếu cấp cứu
        
        **Hiệu quả:**
        - Bắt đầu: 30-60 phút
        - Tối đa: 2-4 giờ
        - Cải thiện loạn nhịp, huyết áp
        
        **Lưu ý:**
        - Sau khi dùng Digibind, nồng độ digoxin sẽ tăng (nhưng không hoạt động)
        - Không đo lại nồng độ digoxin sau Digibind
        - Có thể cần lọc máu nếu suy thận
        """)
        
        if has_hyperkalemia:
            st.warning("""
            **2. TĂNG K (Hyperkalemia)**
            
            **Điều trị:**
            - **Digibind:** (ưu tiên, điều trị nguyên nhân)
            - **Calcium:** Thận trọng (có thể làm nặng loạn nhịp)
            - **Insulin + Glucose:** 10 units regular insulin + 50g glucose
            - **Sodium Bicarbonate:** 50-100 mEq IV
            - **Kayexalate:** 15-30 g PO/PR
            
            **Lưu ý:**
            - Tăng K trong ngộ độc digoxin = Dấu hiệu nặng
            - Digibind thường làm giảm K
            - Tránh calcium nếu có loạn nhịp
            """)
        
        if has_arrhythmia:
            st.warning("""
            **3. LOẠN NHỊP TIM**
            
            **VT/VF:**
            - **Defibrillation:** 200J → 300J → 360J
            - **Digibind:** (ưu tiên)
            - **Amiodarone:** 150 mg IV bolus (nếu cần)
            - **Lidocaine:** 1-1.5 mg/kg IV (nếu cần)
            
            **Bradycardia/AV Block:**
            - **Atropine:** 0.5-1 mg IV (có thể không hiệu quả)
            - **Pacing:** Nếu cần
            - **Digibind:** (ưu tiên)
            
            **Rung nhĩ:**
            - **Digibind:** (ưu tiên)
            - **Tránh:** Cardioversion (có thể gây VT/VF)
            """)
        
        if has_hypotension:
            st.warning("""
            **4. HẠ HUYẾT ÁP**
            
            **Điều trị:**
            1. **Digibind:** (ưu tiên)
            2. **Truyền dịch:** NS 500-1000 mL bolus
            3. **Norepinephrine:** 0.05-0.2 mcg/kg/min
               - Tránh dopamine (có thể gây loạn nhịp)
            
            **Lưu ý:**
            - Digibind thường cải thiện huyết áp
            - Tránh truyền dịch quá nhiều
            """)
    else:
        st.info("## ⚠️ ĐIỀU TRỊ HỖ TRỢ - Ngộ độc nhẹ")
        
        st.markdown("""
        **Nếu không có chỉ định Digibind:**
        
        **1. Bổ sung K (Nếu hạ K):**
        - **Mục tiêu:** K 4.0-5.0 mEq/L
        - **Liều:** 20-40 mEq IV (thận trọng)
        - **Theo dõi:** ECG, K level
        
        **2. Bổ sung Mg (Nếu hạ Mg):**
        - **Liều:** 2-4 g MgSO₄ IV
        - **Theo dõi:** Mg level
        
        **3. Theo dõi:**
        - ECG liên tục
        - Digoxin level
        - Điện giải
        - Chức năng thận
        """)
    
    st.markdown("---")
    
    st.markdown("### 📋 Điều trị Hỗ trợ")
    
    st.info("""
    **1. Điều chỉnh Điện giải:**
    - **Hạ K:** Bổ sung K (thận trọng)
    - **Hạ Mg:** Bổ sung Mg
    - **Hạ Ca:** Bổ sung Ca (thận trọng nếu có loạn nhịp)
    
    **2. Chức năng Thận:**
    - Đánh giá creatinine, eGFR
    - Có thể cần lọc máu nếu suy thận nặng
    
    **3. Tương tác Thuốc:**
    - Ngừng các thuốc tương tác:
      - Amiodarone
      - Verapamil, Diltiazem
      - Quinidine
      - Spironolactone
    
    **4. Theo dõi:**
    - **ECG:** Liên tục 24-48h
    - **Digoxin level:** Mỗi 6-12h (trước Digibind)
    - **Điện giải:** Mỗi 6-12h
    - **Chức năng thận:** Mỗi 12-24h
    """)
    
    st.markdown("---")
    
    st.markdown("### ⚠️ Chống chỉ định & Lưu ý")
    
    st.warning("""
    **KHÔNG dùng:**
    
    **1. Cardioversion:**
    - Có thể gây VT/VF
    - Chỉ dùng nếu cấp cứu và đã dùng Digibind
    
    **2. Calcium:**
    - Thận trọng nếu có loạn nhịp
    - Có thể làm nặng loạn nhịp
    
    **3. Class IA Antiarrhythmics:**
    - Procainamide, Quinidine
    - Làm nặng độc tính
    
    **4. Atropine:**
    - Có thể không hiệu quả
    - Dùng thận trọng
    """)
    
    st.markdown("---")
    
    st.markdown("### 📈 Tiên lượng & Theo dõi")
    
    st.info("""
    **Tiên lượng:**
    - **Tử vong:** 5-10% (nếu không điều trị)
    - **Với Digibind:** Tử vong <1%
    - **Yếu tố nguy cơ:**
      - Tăng K >5.5 mEq/L
      - Loạn nhịp nặng
      - Suy thận nặng
      - Người cao tuổi
    
    **Theo dõi:**
    - **ICU:** Ít nhất 24-48h
    - **ECG:** Liên tục 24-48h
    - **Digoxin level:** Mỗi 6-12h (trước Digibind)
    - **Điện giải:** Mỗi 6-12h
    - **Chức năng thận:** Mỗi 12-24h
    
    **Xuất viện:**
    - Không loạn nhịp
    - Huyết áp ổn định
    - Điện giải bình thường
    - Theo dõi ít nhất 24-48h
    """)
    
    st.markdown("---")
    
    st.markdown("### 👥 Điều chỉnh theo Đặc điểm Bệnh nhân")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Người cao tuổi:**
        - Nguy cơ cao hơn
        - Thận trọng với liều digoxin
        - Theo dõi sát chức năng thận
        
        **Suy thận:**
        - Giảm thải trừ digoxin
        - Có thể cần lọc máu
        - Liều Digibind cao hơn
        """)
    
    with col2:
        st.markdown("""
        **Trẻ em:**
        - Liều Digibind: 5-10 ống
        - Thận trọng với truyền dịch
        - Theo dõi sát hơn
        
        **Có thai:**
        - Digibind an toàn
        - Theo dõi thai nhi
        """)
    
    st.markdown("---")
    
    # References
    references = get_references("Digoxin Toxicity")
    if references:
        render_references_section(references)
    else:
        st.markdown("### 📚 References")
        st.markdown("""
        1. **AHA/ACC Guidelines 2024** - American Heart Association
        2. **UpToDate:** Digoxin Toxicity - Last updated 2024
        3. **Goldfrank's Toxicologic Emergencies** - 11th Edition
        """)
    
    st.markdown("---")
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều trị ngộ độc digoxin cần chuyên khoa độc chất. Gọi trung tâm chống độc nếu có.")

