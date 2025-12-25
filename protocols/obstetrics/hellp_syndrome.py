"""
HELLP Syndrome Protocol
ACOG Guidelines 2024, UpToDate 2024
Life-threatening complication of preeclampsia
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """HELLP Syndrome Management Protocol"""
    st.subheader("🤰 HELLP Syndrome")
    st.caption("ACOG Guidelines 2024, UpToDate 2024 - Life-threatening complication")
    
    st.error("""
    **⚠️ HELLP SYNDROME = CẤP CỨU Y KHOA - TỬ VONG CAO**
    
    **Định nghĩa:**
    - **H:** Hemolysis (Tan máu)
    - **EL:** Elevated Liver enzymes (Tăng men gan)
    - **LP:** Low Platelets (Giảm tiểu cầu)
    
    **Triệu chứng:**
    - Đau bụng trên phải
    - Buồn nôn, nôn
    - Đau đầu
    - Có thể có xuất huyết
    - Có thể có vàng da
    
    **Nguy hiểm:**
    - Vỡ gan (hiếm nhưng tử vong cao)
    - Xuất huyết
    - Suy đa tạng
    """)
    
    st.markdown("---")
    
    st.markdown("### ⚡ Xử trí ngay lập tức (ABC)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.error("""
        **1. AIRWAY & BREATHING**
        
        **Intubation:**
        - Nếu giảm ý thức
        - Suy hô hấp
        - Chuẩn bị phẫu thuật
        
        **Oxygen:**
        - **High-flow:** 10-15 L/min qua mask
        - **Mục tiêu:** SpO₂ ≥95%
        
        **2. CIRCULATION**
        
        **Monitoring:**
        - **Continuous ECG**
        - **Arterial line** (nếu shock)
        - **BP, HR:** Mỗi 15-30 phút
        
        **Truyền dịch:**
        - **NS:** 500-1000 mL bolus (thận trọng)
        - **Lưu ý:** Tránh quá tải dịch
        """)
    
    with col2:
        st.warning("""
        **3. FETAL MONITORING**
        
        - **Continuous FHR:** (nếu có thể)
        - **Đánh giá:** Tình trạng thai nhi
        
        **4. LABS NGAY:**
        - **CBC:** Platelets, Hct, Hb
        - **LFTs:** ALT, AST, Bilirubin
        - **LDH:** (tăng cao)
        - **Haptoglobin:** (giảm)
        - **Coagulation:** PT/INR, aPTT
        - **BMP:** Creatinine, Electrolytes
        """)
    
    st.markdown("---")
    
    st.markdown("### 🔍 Chẩn đoán")
    
    st.info("""
    **Tiêu chuẩn Chẩn đoán:**
    
    **1. Hemolysis:**
    - LDH ≥600 U/L
    - Haptoglobin giảm
    - Bilirubin tăng (gián tiếp)
    - Schistocytes trên peripheral smear
    
    **2. Elevated Liver enzymes:**
    - ALT ≥70 U/L
    - AST ≥70 U/L
    - Hoặc ≥2× bình thường
    
    **3. Low Platelets:**
    - <100,000/μL
    
    **Lưu ý:**
    - Không cần đủ cả 3 tiêu chuẩn
    - Có thể có một phần
    """)
    
    st.markdown("---")
    
    st.markdown("### 💊 Điều trị")
    
    st.error("## 🚨 ĐIỀU TRỊ CẤP CỨU - LẤY THAI NGAY")
    
    st.success("""
    **1. DELIVERY (Lấy thai) - Cấp cứu:**
    
    **Chỉ định:**
    - Tất cả bệnh nhân HELLP
    - **Không chờ:** Corticosteroids
    - **Cấp cứu:** Lấy thai ngay
    
    **Phương pháp:**
    - **C-section:** (ưu tiên, nhanh)
    - **Hoặc:** Induction (nếu có thể)
    
    **2. Magnesium Sulfate:**
    
    - **Loading:** 4-6 g IV trong 15-20 phút
    - **Duy trì:** 1-2 g/h IV
    - **Mục đích:** Phòng ngừa sản giật
    - **Thời gian:** 24h sau lấy thai
    
    **3. Điều trị Huyết áp:**
    
    - **Labetalol:** 20 mg IV, sau đó 40-80 mg mỗi 10 phút
    - **Hoặc:** Hydralazine 5-10 mg IV mỗi 20 phút
    - **Mục tiêu:** SBP 140-160, DBP 90-110
    """)
    
    st.markdown("---")
    
    st.markdown("### 💉 Điều trị Hỗ trợ")
    
    st.info("""
    **1. Truyền máu:**
    
    - **Platelets:**
      - Nếu <50,000/μL và lấy thai
      - Hoặc nếu <20,000/μL (bất kỳ)
      - **Liều:** 1 đơn vị/10 kg
    
    - **PRBC:**
      - Nếu Hct <25% hoặc xuất huyết
      - **Liều:** 2-4 đơn vị
    
    - **FFP:**
      - Nếu rối loạn đông máu
      - **Liều:** 2-4 đơn vị
    
    **2. Monitoring:**
    - **Platelets:** Mỗi 6-12h
    - **LFTs:** Mỗi 6-12h
    - **LDH:** Mỗi 12-24h
    - **Huyết áp, HR:** Mỗi 1-2h
    - **Triệu chứng:** Mỗi 1-2h
    
    **3. Complications:**
    - Vỡ gan (hiếm nhưng tử vong cao)
    - Xuất huyết
    - Suy thận
    - Phù phổi
    """)
    
    st.markdown("---")
    
    st.markdown("### ⚠️ Vỡ Gan")
    
    st.error("## 🚨🚨🚨 VỠ GAN - CẤP CỨU NGOẠI KHOA")
    
    st.markdown("""
    **Triệu chứng:**
    - Đau bụng trên phải dữ dội
    - Hạ huyết áp nặng
    - Shock
    - Có thể có khối máu tụ gan
    
    **Chẩn đoán:**
    - **CT scan:** (nếu ổn định)
    - **FAST:** (nếu cấp cứu)
    - **Lâm sàng:** Nghi ngờ cao
    
    **Điều trị:**
    - **Phẫu thuật cấp cứu:** (nếu vỡ)
    - **Embolization:** (nếu có thể)
    - **Truyền máu:** PRBC, FFP, Platelets
    
    **Tiên lượng:**
    - Tử vong: 50-70%
    - Cần điều trị tích cực
    """)
    
    st.markdown("---")
    
    st.markdown("### 📈 Tiên lượng & Theo dõi")
    
    st.info("""
    **Tiên lượng:**
    - **Mẹ:** Tử vong 1-3% (nếu điều trị đúng)
    - **Thai:** Phụ thuộc vào tuổi thai
    - **Yếu tố nguy cơ:**
      - Chậm trễ lấy thai
      - Vỡ gan
      - Suy đa tạng
    
    **Theo dõi:**
    - **ICU:** Ít nhất 24-48h
    - **Platelets:** Mỗi 6-12h (cho đến khi tăng)
    - **LFTs:** Mỗi 6-12h
    - **Huyết áp, HR:** Mỗi 1-2h
    
    **Cải thiện:**
    - Platelets tăng (sau 24-48h)
    - LFTs giảm (sau 48-72h)
    - LDH giảm (sau 48-72h)
    
    **Xuất viện:**
    - Platelets ≥100,000/μL
    - LFTs cải thiện
    - Huyết áp ổn định
    - Theo dõi ít nhất 48-72h
    """)
    
    st.markdown("---")
    
    # References
    references = get_references("HELLP Syndrome")
    if references:
        render_references_section(references)
    else:
        st.markdown("### 📚 References")
        st.markdown("""
        1. **ACOG Guidelines 2024** - American College of Obstetricians and Gynecologists
        2. **UpToDate:** HELLP Syndrome - Last updated 2024
        3. **Hypertension in Pregnancy** - ACOG Practice Bulletin
        """)
    
    st.markdown("---")
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất.")

