"""
GI Bleeding Protocol
Upper & Lower GI Bleeding Management
Risk Stratification & Management Steps
"""

import streamlit as st


def render():
    """GI Bleeding Protocol"""
    st.subheader("🩸 GI Bleeding Protocol")
    st.caption("Upper & Lower GI Bleeding - Risk Stratification & Management")
    
    st.info("""
    **GI Bleeding phân loại:**
    - **Upper GI (UGIB):** Phía trên ligament of Treitz (duodenum)
    - **Lower GI (LGIB):** Phía dưới ligament of Treitz (jejunum, ileum, colon)
    """)
    
    st.markdown("---")
    
    # Bleeding type selection
    bleeding_type = st.radio(
        "**Loại xuất huyết:**",
        ["Upper GI Bleeding (UGIB)", "Lower GI Bleeding (LGIB)", "Chưa xác định"],
        key="gi_bleeding_type"
    )
    
    st.markdown("---")
    
    if "Upper" in bleeding_type or "UGIB" in bleeding_type:
        render_upper_gi_bleeding()
    elif "Lower" in bleeding_type or "LGIB" in bleeding_type:
        render_lower_gi_bleeding()
    else:
        render_unknown_gi_bleeding()


def render_upper_gi_bleeding():
    """Upper GI Bleeding Protocol"""
    
    st.error("## 🚨 UPPER GI BLEEDING (UGIB) PROTOCOL")
    st.error("**CODE GI BLEED - Xử trí khẩn cấp!**")
    
    st.markdown("### 1️⃣ Đánh Giá & Resuscitation (< 30 Phút)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.error("""
        **ABC - Airway, Breathing, Circulation:**
        
        **A - Airway:**
        - Đảm bảo đường thở thông thoáng
        - Cân nhắc intubation nếu:
          * GCS <8
          * Nôn máu nhiều
          * Risk aspiration cao
        
        **B - Breathing:**
        - O₂ để duy trì SpO₂ >94%
        - Monitor SpO₂ liên tục
        
        **C - Circulation:**
        - **2 đường truyền tĩnh mạch lớn** (16-18G)
        - **Lấy máu ngay:**
          * CBC (Hgb, Hct, Platelet)
          * PT/INR, aPTT
          * Type & Crossmatch (2-4 units)
          * LFT (AST, ALT, bilirubin)
          * Urea/Creatinine
        - **ECG** (loại trừ MI, tìm dấu hiệu thiếu máu)
        """)
    
    with col2:
        st.warning("""
        **Risk Stratification:**
        
        **Glasgow-Blatchford Score (GBS):**
        - Điểm 0-23
        - **GBS ≤1:** Có thể xử trí ngoại trú
        - **GBS ≥2:** Cần nhập viện
        - **GBS ≥6:** Cần can thiệp nội soi
        
        **Rockall Score:**
        - Điểm 0-11
        - Đánh giá nguy cơ tái xuất huyết và tử vong
        - **≥5:** Nguy cơ cao
        
        **Blatchford Score:**
        - Điểm 0-23
        - **≥6:** Cần can thiệp
        """)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Resuscitation - Bù Dịch & Máu")
    
    st.info("""
    **Fluid Resuscitation:**
    
    **Nếu tụt huyết áp hoặc shock:**
    1. **Crystalloid:** NS 0.9% hoặc LR
       - Bolus 500-1000ml
       - Đánh giá đáp ứng
       - Lặp lại nếu cần
    
    2. **Blood Products:**
       - **Nếu Hgb <7 g/dL:** Truyền máu
       - **Nếu Hgb 7-10 g/dL:** Tùy tình trạng lâm sàng
       - **Nếu Hgb >10 g/dL:** Thường không cần (trừ khi shock hoặc xuất huyết tiếp)
    
    3. **Massive Transfusion Protocol (nếu xuất huyết nặng):**
       - RBC:FFP:Platelet = 1:1:1
       - Mục tiêu: Hgb >7, INR <1.5, Platelet >50k
    
    **Mục tiêu:**
    - SBP ≥90 mmHg
    - MAP ≥65 mmHg
    - Hgb >7-8 g/dL
    - INR <1.5 (nếu có)
    - Urine output ≥0.5 ml/kg/h
    """)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Đảo Ngược Anticoagulation")
    
    st.error("""
    **Nếu đang dùng anticoagulation:**
    
    **Warfarin (INR >1.5):**
    - **PCC:** 25-50 U/kg (ưu tiên)
    - Hoặc **FFP:** 10-15 ml/kg
    - **Vitamin K:** 10mg IV
    - Mục tiêu: INR <1.5
    
    **DOAC (Xa inhibitors):**
    - **Andexanet alfa:** Nếu có (Xa inhibitors)
    - **4F-PCC:** 50 U/kg (nếu không có Andexanet)
    
    **DOAC (Dabigatran):**
    - **Idarucizumab:** 5g IV (2 bolus 2.5g)
    
    **Heparin/LMWH:**
    - Dừng ngay
    - Protamine nếu cần thiết
    """)
    
    st.markdown("---")
    st.markdown("### 4️⃣ Điều Trị Dược Lý")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("""
        **PPI (Proton Pump Inhibitor):**
        
        **High-dose IV PPI:**
        - **Pantoprazole 80mg IV bolus**, sau đó **8mg/h infusion × 72h**
        - Hoặc **Omeprazole 80mg IV bolus**, sau đó **8mg/h × 72h**
        - Hoặc **Esomeprazole 80mg IV bolus**, sau đó **8mg/h × 72h**
        
        **Sau đó chuyển PO:**
        - PPI 40mg BID × 4 tuần
        """)
    
    with col2:
        st.warning("""
        **Octreotide (nếu nghi variceal bleeding):**
        
        - **Octreotide 50-100mcg IV bolus**, sau đó **25-50mcg/h infusion**
        - Dùng khi nghi varices (xơ gan, portal HTN)
        - Không dùng thường quy cho non-variceal UGIB
        """)
    
    st.markdown("---")
    st.markdown("### 5️⃣ Chỉ Định Nội Soi")
    
    st.info("""
    **Timing cho EGD (Esophagogastroduodenoscopy):**
    
    **Urgent EGD (< 24h):**
    - ✅ **High-risk:** GBS ≥6, Rockall ≥5
    - ✅ **Xuất huyết tiếp diễn**
    - ✅ **Shock hoặc tụt huyết áp**
    - ✅ **Hgb drop >2 g/dL**
    
    **Early EGD (24-48h):**
    - ✅ Hầu hết trường hợp còn lại
    
    **Chống chỉ định tương đối:**
    - ⚠️ Shock không ổn định (cần resuscitation trước)
    - ⚠️ MI cấp hoặc rối loạn nhịp nặng
    """)
    
    st.markdown("---")
    st.markdown("### 6️⃣ Quản lý theo nguyên nhân")
    
    tab1, tab2, tab3, tab4 = st.tabs(["PUD", "Varices", "Mallory-Weiss", "Khác"])
    
    with tab1:
        st.markdown("#### 💊 Peptic Ulcer Disease (PUD)")
        
        st.success("""
        **Điều trị:**
        
        1. **PPI high-dose** (như trên)
        
        2. **Nội soi can thiệp nếu:**
           - Active bleeding (Forrest Ia, Ib)
           - Visible vessel (Forrest IIa)
           - Clot adherent (Forrest IIb)
        
        3. **Phương pháp cầm máu:**
           - **Clip** (hemostatic clip)
           - **Thermal** (cautery, APC)
           - **Injection** (epinephrine ± sclerosant)
           - **Combination therapy** (ưu tiên)
        
        4. **Sau nội soi:**
           - PPI 40mg BID × 4 tuần
           - Điều trị H. pylori nếu (+)
           - Tránh NSAIDs
        """)
    
    with tab2:
        st.markdown("#### 🩸 Variceal Bleeding")
        
        st.error("""
        **Điều trị khẩn cấp:**
        
        1. **Octreotide** (như trên)
        
        2. **Endoscopic therapy:**
           - **Band ligation** (ưu tiên)
           - **Sclerotherapy** (nếu không band được)
        
        3. **Balloon tamponade (Sengstaken-Blakemore):**
           - Chỉ dùng nếu xuất huyết nặng không cầm được
           - Bridge đến nội soi hoặc TIPS
           - Không để quá 24h
        
        4. **TIPS (Transjugular Intrahepatic Portosystemic Shunt):**
           - Nếu tái xuất huyết sau điều trị nội soi
           - Child-Pugh B hoặc C
        
        5. **Dự phòng tái phát:**
           - Beta-blocker (Propranolol, Nadolol) để giảm portal pressure
           - Band ligation mỗi 2-4 tuần đến hết varices
        """)
    
    with tab3:
        st.markdown("#### 🤮 Mallory-Weiss Tear")
        
        st.info("""
        **Đặc điểm:**
        - Thường tự cầm (85-95%)
        - Liên quan đến nôn/nôn khan
        
        **Điều trị:**
        - **Nếu đang xuất huyết:** Nội soi clip hoặc cautery
        - **Nếu đã cầm:** PPI × 2-4 tuần
        - **Supportive care:** NPO 24h, sau đó chế độ ăn mềm
        """)
    
    with tab4:
        st.markdown("#### 🔍 Nguyên Nhân Khác")
        
        st.warning("""
        **Gastritis/Erosions:**
        - PPI × 4 tuần
        - Tránh NSAIDs, rượu
        
        **Dieulafoy Lesion:**
        - Nội soi clip hoặc cautery
        
        **AVM (Arteriovenous Malformation):**
        - Cautery, APC
        - Có thể cần surgery nếu nhiều hoặc nặng
        
        **Aortoenteric Fistula:**
        - Surgical emergency
        - Cần phẫu thuật ngay
        """)
    
    st.markdown("---")
    st.markdown("### 7️⃣ Theo Dõi & Dự Phòng Tái Phát")
    
    st.success("""
    **Monitoring:**
    - Dấu hiệu sống mỗi 1-2h × 24h
    - Hgb mỗi 6-12h × 24-48h
    - Đánh giá xuất huyết tiếp (nôn máu, phân đen, Hgb drop)
    
    **Dự phòng tái phát:**
    - **PUD:** PPI + điều trị H. pylori + tránh NSAIDs
    - **Varices:** Beta-blocker + band ligation định kỳ
    - **NSAID-related:** PPIs với NSAIDs
    
    **Timing xuất viện:**
    - Ổn định 24-48h
    - Hgb ổn định
    - Không xuất huyết tiếp
    - Đã có kế hoạch điều trị dài hạn
    """)


def render_lower_gi_bleeding():
    """Lower GI Bleeding Protocol"""
    
    st.error("## 🚨 LOWER GI BLEEDING (LGIB) PROTOCOL")
    
    st.markdown("### 1️⃣ Đánh Giá Ban Đầu")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Triệu chứng:**
        - Đi ngoài máu đỏ tươi (hematochezia)
        - Đi ngoài máu đỏ sẫm
        - Máu lẫn phân
        - Chỉ phân máu đơn thuần
        
        **Lưu ý:**
        - UGIB nặng cũng có thể gây hematochezia
        - Cần loại trừ UGIB trước
        """)
    
    with col2:
        st.warning("""
        **Risk Stratification:**
        
        **Nguy cơ thấp:**
        - Hemodynamically stable
        - Hgb ổn định
        - Không có bệnh nền nặng
        - Có thể xử trí ngoại trú
        
        **Nguy cơ cao:**
        - Tụt huyết áp, shock
        - Hgb drop >2 g/dL
        - Xuất huyết tiếp diễn
        - Bệnh nền nặng
        """)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Resuscitation (Tương Tự UGIB)")
    
    st.info("""
    **Tương tự Upper GI Bleeding:**
    - ABC approach
    - 2 đường truyền
    - Lấy máu (CBC, PT/INR, Type & Cross)
    - Bù dịch và máu
    - Đảo ngược anticoagulation nếu cần
    """)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Chỉ Định Colonoscopy")
    
    st.success("""
    **Timing cho Colonoscopy:**
    
    **Urgent Colonoscopy (< 24h):**
    - ✅ Xuất huyết tiếp diễn
    - ✅ Hemodynamically unstable
    - ✅ Hgb drop nhanh
    
    **Early Colonoscopy (24-48h):**
    - ✅ Hầu hết trường hợp
    
    **Chuẩn bị:**
    - **Rapid bowel prep:**
      * Polyethylene glycol 4L trong 3-4h
      * Hoặc chia 2 ngày nếu không urgent
    
    **Chống chỉ định:**
    - ⚠️ Shock không ổn định
    - ⚠️ Peritonitis
    - ⚠️ Toxic megacolon
    """)
    
    st.markdown("---")
    st.markdown("### 4️⃣ Quản Lý Theo Nguyên Nhân")
    
    tab1, tab2, tab3, tab4 = st.tabs(["Diverticular", "Angiodysplasia", "Ischemic Colitis", "Khác"])
    
    with tab1:
        st.markdown("#### 🔴 Diverticular Bleeding")
        
        st.info("""
        **Đặc điểm:**
        - Nguyên nhân phổ biến nhất LGIB (40-50%)
        - Thường tự cầm (80%)
        - Tái phát: 25-30%
        
        **Điều trị:**
        - **Nội soi:**
          * Clip nếu thấy active bleeding
          * Cautery nếu có visible vessel
        - **Surgery:** Nếu xuất huyết nặng, tái phát nhiều lần
        - **Supportive:** Resuscitation, truyền máu nếu cần
        
        **Dự phòng:**
        - High-fiber diet
        - Tránh constipation
        """)
    
    with tab2:
        st.markdown("#### 🩸 Angiodysplasia (AVM)")
        
        st.success("""
        **Đặc điểm:**
        - Nguyên nhân thứ 2 LGIB (20-30%)
        - Thường ở right colon
        - Liên quan tuổi già, CKD
        
        **Điều trị:**
        - **Endoscopic:**
          * APC (Argon Plasma Coagulation)
          * Cautery
          * Clip
        - **Surgery:** Nếu nhiều hoặc nặng
        - **Hormone therapy:** (không còn khuyến cáo)
        
        **Tái phát:** Thường gặp
        """)
    
    with tab3:
        st.markdown("#### ❄️ Ischemic Colitis")
        
        st.warning("""
        **Đặc điểm:**
        - Thường tự giới hạn
        - Liên quan low flow states
        
        **Điều trị:**
        - **Supportive:**
          * NPO
          * IV fluids
          * Antibiotics (nếu có concern infection)
        - **Monitoring:** Lâm sàng, labs
        - **Surgery:** Nếu thủng, hoại tử
        
        **Nguyên nhân:**
        - Low cardiac output
        - Vasopressors
        - Mesenteric ischemia
        """)
    
    with tab4:
        st.markdown("#### 🔍 Nguyên Nhân Khác")
        
        st.info("""
        **Colorectal Cancer:**
        - Cần nội soi để chẩn đoán
        - Surgical management
        
        **IBD (Inflammatory Bowel Disease):**
        - Điều trị IBD
        - Immunosuppression
        
        **Radiation Colitis:**
        - Supportive care
        - Formalin instillation nếu nặng
        
        **Post-polypectomy:**
        - Thường tự cầm
        - Nội soi clip nếu cần
        """)
    
    st.markdown("---")
    st.markdown("### 5️⃣ Can Thiệp Nếu Cần")
    
    st.error("""
    **Angiography với Embolization:**
    - Nếu xuất huyết nặng, nội soi không cầm được
    - Tỷ lệ thành công: 70-90%
    - Risk: Ischemic colitis (10-20%)
    
    **Surgery:**
    - Chỉ định:
      * Xuất huyết nặng không cầm được
      * Tái phát nhiều lần
      * Cancer
    - Subtotal colectomy nếu không xác định được vị trí
    """)


def render_unknown_gi_bleeding():
    """Protocol when bleeding source unknown"""
    
    st.warning("## ⚠️ CHƯA XÁC ĐỊNH NGUỒN XUẤT HUYẾT")
    
    st.error("""
    **Xử trí ngay trong khi đánh giá:**
    
    1. ✅ **ABC** - Airway, Breathing, Circulation
    2. ✅ **2 đường truyền** tĩnh mạch lớn
    3. ✅ **Lấy máu:** CBC, PT/INR, aPTT, Type & Cross
    4. ✅ **Resuscitation** - Bù dịch và máu nếu cần
    5. ✅ **Đảo ngược anticoagulation** nếu đang dùng
    
    **Đánh giá:**
    - **Hematemesis hoặc coffee-ground emesis:** → UGIB
    - **Melena (phân đen):** → Thường UGIB, có thể LGIB
    - **Hematochezia (máu đỏ tươi):** → Thường LGIB, có thể UGIB nếu nặng
    
    **Nếu hematochezia + shock:** Nghi UGIB nặng → EGD trước
    **Nếu hematochezia + stable:** Nghi LGIB → Colonoscopy
    
    **Timeline:**
    - Resuscitation ngay
    - EGD hoặc Colonoscopy trong 24h
    """)

