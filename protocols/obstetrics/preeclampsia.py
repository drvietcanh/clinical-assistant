"""
Preeclampsia Protocol
ACOG Guidelines 2024, UpToDate 2024
Hypertensive disorder of pregnancy
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Preeclampsia Management Protocol"""
    st.subheader("🤰 Tiền Sản Giật (Preeclampsia)")
    st.caption("ACOG Guidelines 2024, UpToDate 2024 - Hypertensive disorder of pregnancy")
    
    st.error("""
    **⚠️ TIỀN SẢN GIẬT = BỆNH NẶNG - NGUY HIỂM CHO MẸ VÀ THAI**
    
    **Định nghĩa:**
    - Tăng huyết áp (SBP ≥140 hoặc DBP ≥90) sau 20 tuần
    - VÀ có một trong các dấu hiệu:
      - Protein niệu ≥300 mg/24h
      - HOẶC có dấu hiệu nội tạng (tăng men gan, giảm tiểu cầu, phù phổi)
    
    **Phân loại:**
    - **Nhẹ:** Tăng HA + Protein niệu
    - **Nặng:** Tăng HA + Dấu hiệu nội tạng
    - **Sản giật:** Tiền sản giật + Co giật
    - **HELLP:** Hemolysis, Elevated Liver enzymes, Low Platelets
    """)
    
    st.markdown("---")
    
    st.markdown("### ⚡ Xử trí ngay lập tức (ABC)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.error("""
        **1. AIRWAY & BREATHING**
        
        **Intubation:**
        - Nếu sản giật (co giật)
        - Suy hô hấp
        - Giảm ý thức
        
        **Oxygen:**
        - **High-flow:** 10-15 L/min qua mask
        - **Mục tiêu:** SpO₂ ≥95%
        
        **2. CIRCULATION**
        
        **Monitoring:**
        - **Continuous ECG**
        - **Arterial line** (nếu nặng)
        - **BP, HR:** Mỗi 15-30 phút
        
        **Truyền dịch:**
        - **NS:** 500-1000 mL bolus (thận trọng)
        - **Lưu ý:** Tránh quá tải dịch
        """)
    
    with col2:
        st.warning("""
        **3. FETAL MONITORING**
        
        - **Continuous FHR:** (nếu có thể)
        - **Ultrasound:** (nếu cần)
        - **Đánh giá:** Tình trạng thai nhi
        
        **4. LABS NGAY:**
        - **CBC:** Hct, Hb, Platelets
        - **BMP:** Creatinine, Electrolytes
        - **LFTs:** ALT, AST, Bilirubin
        - **LDH:** (nếu nghi ngờ HELLP)
        - **Urine protein:** (24h hoặc spot)
        """)
    
    st.markdown("---")
    
    st.markdown("### 🔍 Chẩn đoán")
    
    st.info("""
    **Tiêu chuẩn Chẩn đoán:**
    
    **1. Tăng huyết áp:**
    - SBP ≥140 mmHg HOẶC DBP ≥90 mmHg
    - Sau 20 tuần thai
    - Đo 2 lần cách nhau ≥4h
    
    **2. VÀ một trong các dấu hiệu:**
    
    **A. Protein niệu:**
    - ≥300 mg/24h
    - Hoặc Protein/Creatinine ratio ≥0.3
    
    **B. HOẶC dấu hiệu nội tạng:**
    - Tăng men gan (ALT/AST ≥2× bình thường)
    - Giảm tiểu cầu (<100,000/μL)
    - Creatinine tăng (>1.1 mg/dL hoặc tăng gấp đôi)
    - Phù phổi
    - Triệu chứng thần kinh (đau đầu, rối loạn thị giác)
    """)
    
    st.markdown("---")
    
    st.markdown("### 💊 Điều trị")
    
    severity = st.radio(
        "**Mức độ nghiêm trọng:**",
        [
            "Nhẹ (Mild)",
            "Nặng (Severe)",
            "Sản giật (Eclampsia)",
            "HELLP Syndrome"
        ],
        key="preeclampsia_severity"
    )
    
    st.markdown("---")
    
    if "Nhẹ" in severity:
        render_mild_preeclampsia()
    elif "Nặng" in severity:
        render_severe_preeclampsia()
    elif "Sản giật" in severity:
        st.info("Xem protocol **Sản giật (Eclampsia)** trong chuyên khoa Sản khoa")
    else:
        render_hellp()
    
    st.markdown("---")
    
    st.markdown("### 💉 Điều trị Huyết áp")
    
    st.success("""
    **Mục tiêu:**
    - **SBP:** 140-160 mmHg
    - **DBP:** 90-110 mmHg
    - **Tránh:** Hạ huyết áp quá nhanh (ảnh hưởng thai nhi)
    
    **Thuốc:**
    
    **1. Labetalol (Ưu tiên):**
    - **Liều:** 20 mg IV, sau đó 40-80 mg mỗi 10 phút
    - **Duy trì:** 200-400 mg PO bid
    - **Tối đa:** 1200 mg/ngày
    
    **2. Hydralazine:**
    - **Liều:** 5-10 mg IV mỗi 20 phút
    - **Tối đa:** 20 mg mỗi lần
    
    **3. Nifedipine:**
    - **Liều:** 10-20 mg PO, lặp lại sau 30 phút nếu cần
    - **Duy trì:** 30-60 mg PO bid
    
    **4. Magnesium Sulfate:**
    - **Loading:** 4-6 g IV trong 15-20 phút
    - **Duy trì:** 1-2 g/h IV
    - **Mục đích:** Phòng ngừa sản giật
    - **Chỉ định:** Nếu tiền sản giật nặng hoặc sản giật
    """)
    
    st.markdown("---")
    
    st.markdown("### 📋 Điều trị Hỗ trợ")
    
    st.info("""
    **1. Delivery (Lấy thai):**
    
    **Chỉ định:**
    - **≥37 tuần:** Lấy thai
    - **34-36 tuần:** Cân nhắc (nếu nặng)
    - **<34 tuần:** Corticosteroids (trưởng thành phổi) + Lấy thai nếu nặng
    
    **2. Corticosteroids:**
    - **Betamethasone:** 12 mg IM × 2 liều (cách 24h)
    - **Hoặc:** Dexamethasone 6 mg IM × 4 liều (mỗi 12h)
    - **Mục đích:** Trưởng thành phổi thai nhi
    
    **3. Monitoring:**
    - **Mẹ:** BP, HR, triệu chứng (mỗi 1-2h)
    - **Thai:** FHR, movement (mỗi 1-2h)
    - **Labs:** Platelets, LFTs, Creatinine (mỗi 12-24h)
    
    **4. Complications:**
    - Sản giật
    - HELLP Syndrome
    - Suy thận
    - Phù phổi
    - Đột quỵ
    """)
    
    st.markdown("---")
    
    st.markdown("### 📈 Tiên lượng & Theo dõi")
    
    st.info("""
    **Tiên lượng:**
    - **Mẹ:** Tốt nếu điều trị đúng
    - **Thai:** Phụ thuộc vào tuổi thai
    - **Yếu tố nguy cơ:**
      - Chậm trễ điều trị
      - Sản giật
      - HELLP Syndrome
    
    **Theo dõi:**
    - **BP, HR:** Mỗi 1-2h
    - **Triệu chứng:** Mỗi 1-2h
    - **Labs:** Mỗi 12-24h
    - **Thai:** FHR, movement mỗi 1-2h
    
    **Xuất viện:**
    - Huyết áp ổn định
    - Không triệu chứng
    - Labs ổn định
    - Đã lấy thai hoặc ổn định
    - Theo dõi ít nhất 24-48h
    """)
    
    st.markdown("---")
    
    # References
    references = get_references("Preeclampsia")
    if references:
        render_references_section(references)
    else:
        st.markdown("### 📚 References")
        st.markdown("""
        1. **ACOG Guidelines 2024** - American College of Obstetricians and Gynecologists
        2. **UpToDate:** Preeclampsia - Last updated 2024
        3. **Hypertension in Pregnancy** - ACOG Practice Bulletin
        """)
    
    st.markdown("---")
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất.")


def render_mild_preeclampsia():
    """Mild Preeclampsia"""
    st.warning("## ⚠️ TIỀN SẢN GIẬT NHẸ")
    
    st.markdown("""
    **Đặc điểm:**
    - Tăng HA (SBP 140-160, DBP 90-110)
    - Protein niệu
    - Không có dấu hiệu nội tạng
    
    **Điều trị:**
    
    **1. Monitoring:**
    - BP, HR mỗi 4-6h
    - Labs mỗi 1-2 ngày
    - Thai mỗi 1-2 ngày
    
    **2. Điều trị HA:**
    - Nếu SBP ≥150 hoặc DBP ≥100
    - Labetalol, Nifedipine
    
    **3. Delivery:**
    - ≥37 tuần: Lấy thai
    - <37 tuần: Theo dõi sát
    """)


def render_severe_preeclampsia():
    """Severe Preeclampsia"""
    st.error("## 🚨 TIỀN SẢN GIẬT NẶNG - ICU")
    
    st.markdown("""
    **Đặc điểm:**
    - Tăng HA nặng (SBP ≥160, DBP ≥110)
    - Dấu hiệu nội tạng
    - Có thể có triệu chứng
    
    **Điều trị:**
    
    **1. ICU:**
    - Monitoring sát
    - Chuẩn bị lấy thai
    
    **2. Điều trị HA:**
    - Labetalol, Hydralazine
    - Mục tiêu: SBP 140-160, DBP 90-110
    
    **3. Magnesium Sulfate:**
    - Loading: 4-6 g IV
    - Duy trì: 1-2 g/h IV
    - Phòng ngừa sản giật
    
    **4. Delivery:**
    - ≥34 tuần: Lấy thai
    - <34 tuần: Corticosteroids + Lấy thai nếu nặng
    """)


def render_hellp():
    """HELLP Syndrome"""
    st.error("## 🚨🚨 HELLP SYNDROME - ICU")
    
    st.markdown("""
    **Đặc điểm:**
    - **H:** Hemolysis (LDH tăng, Haptoglobin giảm)
    - **EL:** Elevated Liver enzymes (ALT/AST tăng)
    - **LP:** Low Platelets (<100,000/μL)
    
    **Điều trị:**
    
    **1. ICU:**
    - Monitoring sát
    - Chuẩn bị lấy thai
    
    **2. Truyền máu:**
    - **Platelets:** Nếu <50,000/μL và lấy thai
    - **PRBC:** Nếu thiếu máu
    
    **3. Delivery:**
    - **Cấp cứu:** Lấy thai ngay
    - **Không chờ:** Corticosteroids
    
    **4. Monitoring:**
    - Platelets, LFTs mỗi 6-12h
    - Huyết áp, HR mỗi 1-2h
    """)


