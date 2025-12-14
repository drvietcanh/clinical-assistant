"""
GI Bleeding Protocol
Upper & Lower GI Bleeding Management
Risk Stratification & Management Steps
"""

import streamlit as st
from scores.gi.glasgow_blatchford import calculate_gbs


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
    
    st.markdown("### 1️⃣ Đánh giá & Resuscitation (< 30 Phút)")
    
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
        **Risk Stratification (ưu tiên GBS):**
        
        **Glasgow-Blatchford Score (GBS):** 0-23
        - **GBS 0-1:** Ngoại trú hoặc nhập ngắn, EGD sớm 24h
        - **GBS 2-5:** Nhập viện, EGD trong 24h
        - **GBS ≥6:** Nguy cơ cao → EGD <12h
        
        **Pre-endoscopy Rockall:** 0-7
        - **≥5:** Nguy cơ tái xuất huyết cao, cần EGD sớm
        
        **Sau nội soi:** dùng Rockall đầy đủ để tiên lượng tử vong
        """)
    
    st.markdown("---")
    st.markdown("### 📊 Risk Stratification Calculators")
    
    # Add calculators
    calc_tab1, calc_tab2 = st.tabs(["Glasgow-Blatchford Score (GBS)", "Rockall Score"])
    
    with calc_tab1:
        render_gbs_calculator()
    
    with calc_tab2:
        render_rockall_calculator()
    
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
    st.markdown("### 3️⃣ Đảo ngược anticoagulation")
    
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
    st.markdown("### 4️⃣ Phân Luồng: Variceal vs Non-Variceal")
    
    bleeding_source = st.radio(
        "**Nghi ngờ nguyên nhân:**",
        ["Chưa xác định", "Non-Variceal (PUD, Mallory-Weiss)", "Variceal (Xơ gan/Varices)"],
        key="ugib_source"
    )
    
    st.markdown("---")
    
    if "Non-Variceal" in bleeding_source or "Chưa xác định" in bleeding_source:
        st.markdown("#### 💊 Non-Variceal Bleeding - PPI Protocol")
        
        tab1, tab2 = st.tabs(["IV PPI Dosing Calculator", "Hướng dẫn điều trị"])
        
        with tab1:
            st.markdown("##### 💉 High-Dose IV PPI Calculator")
            
            col1, col2 = st.columns([1, 2])
            
            with col1:
                ppi_type = st.selectbox(
                    "**Loại PPI:**",
                    ["Pantoprazole", "Omeprazole", "Esomeprazole"],
                    key="ppi_type"
                )
                
                method = st.radio(
                    "**Phương pháp:**",
                    ["Continuous Infusion (Ưu tiên)", "Intermittent Bolus"],
                    key="ppi_method"
                )
                
                if method == "Continuous Infusion":
                    st.markdown("**Liều chuẩn:**")
                    st.info("""
                    - **Bolus:** 80mg IV trong 30 phút
                    - **Infusion:** 8mg/h × 72 giờ
                    """)
                    
                    # Calculate infusion
                    infusion_rate = 8.0  # mg/h
                    infusion_volume_per_hour = infusion_rate  # ml/h if 1mg/ml
                    
                    st.metric("**Tốc độ truyền:**", f"{infusion_volume_per_hour:.1f} ml/h", help="Nếu pha 1mg/ml")
                    st.metric("**Thời gian:**", "72 giờ", help="3 ngày")
                    
                    st.markdown("**Cách pha:**")
                    st.success("""
                    - Pantoprazole 80mg pha trong 100ml NS
                    - Tốc độ: 8ml/h (nếu pha 1mg/ml)
                    - Hoặc dùng pump với tốc độ 8mg/h
                    """)
                else:
                    st.markdown("**Liều bolus:**")
                    st.info("""
                    - **Pantoprazole:** 80mg IV q12h
                    - **Hoặc:** 40mg IV q12h
                    - Truyền trong 30 phút
                    """)
            
            with col2:
                st.markdown("##### 📋 Protocol Chi tiết")
                
                st.success("""
                **High-Dose IV PPI (Non-Variceal UGIB):**
                
                **Bước 1: Bolus**
                - {ppi_type} 80mg IV trong 30 phút
                - Bắt đầu ngay khi chẩn đoán UGIB
                
                **Bước 2: Continuous Infusion (nếu dùng)**
                - {ppi_type} 8mg/h × 72 giờ
                - Duy trì pH dạ dày >6
                - Giảm tái xuất huyết
                
                **Bước 3: Sau nội soi**
                - Nếu đã cầm máu: Tiếp tục IV PPI × 72h
                - Sau đó chuyển PO: 40mg BID × 14 ngày
                - Sau đó: 40mg QD × 2-4 tuần
                
                **Lưu ý:**
                - Continuous infusion hiệu quả hơn bolus
                - Dùng trong 72h sau nội soi
                - Chuyển PO khi ổn định
                """.format(ppi_type=ppi_type))
        
        with tab2:
            st.markdown("**Chỉ định:**")
            st.info("""
            - ✅ Peptic Ulcer Disease (PUD)
            - ✅ Mallory-Weiss Tear
            - ✅ Dieulafoy Lesion
            - ✅ Gastritis/Erosions
            - ✅ Stress ulcer
            """)
            
            st.markdown("**Chống chỉ định:**")
            st.warning("""
            - ❌ Variceal bleeding (dùng Octreotide thay vì PPI)
            - ❌ Dị ứng PPI
            """)
    
    if "Variceal" in bleeding_source or "Chưa xác định" in bleeding_source:
        st.markdown("---")
        st.markdown("#### 🩸 Variceal Bleeding - Octreotide Protocol")
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.markdown("##### 💉 Octreotide Dosing")
            
            weight = st.number_input(
                "**Cân nặng (kg):**",
                min_value=40.0,
                max_value=150.0,
                value=70.0,
                step=0.1,
                key="octreotide_weight"
            )
            
            bolus_dose = 50.0  # mcg
            infusion_rate = 25.0  # mcg/h (có thể tăng đến 50mcg/h)
            
            st.metric("**Bolus:**", f"{bolus_dose:.0f} mcg IV", help="Truyền trong 5 phút")
            st.metric("**Infusion:**", f"{infusion_rate:.0f} mcg/h", help="Tối đa 5 ngày")
            
            st.info("""
            **Cách pha:**
            - Octreotide 1mg (1000mcg) pha trong 50ml NS
            - Nồng độ: 20mcg/ml
            - Tốc độ: {:.1f} ml/h cho 25mcg/h
            """.format(infusion_rate / 20))
        
        with col2:
            st.markdown("##### 📋 Variceal Protocol")
            
            st.error("""
            **Variceal Bleeding Management:**
            
            1. **Octreotide:**
               - Bolus: 50-100mcg IV (truyền trong 5 phút)
               - Infusion: 25-50mcg/h × 5 ngày (tối đa)
               - Giảm portal pressure
            
            2. **Kháng sinh dự phòng:**
               - Ceftriaxone 1g IV q24h × 5-7 ngày
               - Hoặc Norfloxacin 400mg PO BID (nếu không có ascites)
               - Dự phòng SBP, spontaneous bacteremia
            
            3. **Tránh PPI thường quy:**
               - Chỉ dùng nếu có loét dạ dày phối hợp
               - PPI không có tác dụng với variceal bleeding
            
            4. **Endoscopic therapy:**
               - Band ligation (ưu tiên)
               - Sclerotherapy (nếu không band được)
            
            5. **Balloon tamponade:**
               - Chỉ dùng nếu xuất huyết nặng không cầm được
               - Bridge đến nội soi hoặc TIPS
            """)
    
    st.markdown("---")
    st.markdown("### 5️⃣ Chỉ định Nội Soi - Decision Tree")
    
    st.markdown("#### ⏱️ Endoscopy Timing Calculator")
    
    # Input for decision
    col1, col2 = st.columns(2)
    
    with col1:
        gbs_score = st.number_input(
            "**GBS Score:**",
            min_value=0,
            max_value=23,
            value=5,
            step=1,
            key="endoscopy_gbs",
            help="Nhập GBS từ calculator trên"
        )
        
        is_shock = st.checkbox("**Shock/Tụt huyết áp**", key="endoscopy_shock")
        is_variceal = st.checkbox("**Nghi variceal bleeding**", key="endoscopy_variceal")
        hgb_drop = st.number_input(
            "**Hgb drop (g/dL):**",
            min_value=0.0,
            max_value=10.0,
            value=0.0,
            step=0.1,
            key="endoscopy_hgb_drop"
        )
        bleeding_continues = st.checkbox("**Xuất huyết tiếp diễn**", key="endoscopy_continues")
    
    with col2:
        is_stable = st.checkbox("**Hồi sức đã ổn định**", key="endoscopy_stable", value=True)
        has_mi = st.checkbox("**MI cấp hoặc rối loạn nhịp nặng**", key="endoscopy_mi")
        
        st.markdown("---")
        
        # Decision logic
        urgency = "Unknown"
        timing = "Unknown"
        recommendation = ""
        
        if has_mi:
            urgency = "Chống chỉ định tương đối"
            timing = "Chờ ổn định tim mạch"
            recommendation = "⚠️ Chống chỉ định tương đối - Chờ ổn định tim mạch trước"
        elif not is_stable:
            urgency = "Chưa sẵn sàng"
            timing = "Ưu tiên hồi sức trước"
            recommendation = "⚠️ Ưu tiên hồi sức - Chờ ổn định hemodynamic"
        elif is_shock or gbs_score >= 6 or is_variceal or (hgb_drop > 2 and bleeding_continues):
            urgency = "Rất khẩn"
            timing = "< 12 giờ"
            recommendation = "🚨 EGD RẤT KHẨN - Trong vòng 12 giờ"
        elif gbs_score >= 2:
            urgency = "Khẩn"
            timing = "< 24 giờ"
            recommendation = "⚠️ EGD KHẨN - Trong vòng 24 giờ"
        else:
            urgency = "Sớm"
            timing = "24-48 giờ"
            recommendation = "✅ EGD SỚM - Trong vòng 24-48 giờ"
        
        st.markdown("### 📊 Kết quả")
        st.metric("**Mức độ khẩn:**", urgency)
        st.metric("**Thời gian:**", timing)
        
        if "Rất khẩn" in urgency:
            st.error(recommendation)
        elif "Khẩn" in urgency:
            st.warning(recommendation)
        else:
            st.info(recommendation)
    
    st.markdown("---")
    st.markdown("#### 📋 Decision Tree Chi tiết")
    
    st.info("""
    **Quyết định thời gian nội soi:**
    
    **🚨 Rất khẩn (< 12h) - Chỉ định:**
    - ✅ GBS ≥6
    - ✅ Shock/Tụt huyết áp (sau hồi sức ổn)
    - ✅ Nghi variceal bleeding
    - ✅ Hgb drop >2 g/dL + xuất huyết tiếp diễn
    - ✅ Active bleeding nặng
    
    **⚠️ Khẩn (< 24h) - Chỉ định:**
    - ✅ GBS 2-5
    - ✅ Hầu hết UGIB còn lại
    - ✅ Đã hồi sức ổn định
    
    **✅ Sớm (24-48h) - Chỉ định:**
    - ✅ GBS 0-1
    - ✅ Ổn định, không xuất huyết tiếp
    
    **❌ Chống chỉ định tương đối:**
    - ❌ Shock chưa ổn định (ưu tiên hồi sức)
    - ❌ MI cấp hoặc rối loạn nhịp nặng
    - ❌ Không có khả năng chịu đựng thủ thuật
    """)
    
    st.markdown("---")
    st.markdown("#### 🔍 Chuẩn Bị Nội Soi")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("""
        **Trước nội soi:**
        - ✅ Hồi sức ổn định (SBP ≥90, MAP ≥65)
        - ✅ 2 đường truyền
        - ✅ Type & Crossmatch (2-4 units sẵn sàng)
        - ✅ NPO ít nhất 4-6 giờ (nếu có thể)
        - ✅ Consent bệnh nhân/gia đình
        - ✅ Anesthesia consult (nếu cần)
        """)
    
    with col2:
        st.warning("""
        **Trong nội soi:**
        - ✅ Monitor: BP, HR, SpO₂ liên tục
        - ✅ Sẵn sàng can thiệp cầm máu
        - ✅ Sẵn sàng truyền máu nếu cần
        - ✅ Có thể cần intubation nếu nguy cơ cao
        
        **Sau nội soi:**
        - ✅ Theo dõi sát 24-48h
        - ✅ Tiếp tục PPI (nếu non-variceal)
        - ✅ Tiếp tục Octreotide (nếu variceal)
        """)
    
    st.markdown("---")
    st.markdown("### 6️⃣ Quản lý Theo Nguyên Nhân")
    
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
        2. **Kháng sinh dự phòng:** Ceftriaxone 1g IV q24h × 5-7 ngày
        
        3. **Endoscopic therapy:**
           - **Band ligation** (ưu tiên)
           - **Sclerotherapy** (nếu không band được)
        
        4. **Balloon tamponade (Sengstaken-Blakemore):**
           - Chỉ dùng nếu xuất huyết nặng không cầm được
           - Bridge đến nội soi hoặc TIPS
           - Không để quá 24h
        
        5. **TIPS (Transjugular Intrahepatic Portosystemic Shunt):**
           - Nếu tái xuất huyết sau điều trị nội soi
           - Child-Pugh B hoặc C
        
        6. **Dự phòng tái phát:**
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
    st.markdown("### 7️⃣ Theo dõi & Dự Phòng Tái Phát")
    
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
    
    st.markdown("### 1️⃣ Đánh giá ban đầu")
    
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
    st.markdown("### 3️⃣ Chỉ định Colonoscopy")
    
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
    st.markdown("### 4️⃣ Quản lý Theo Nguyên Nhân")
    
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
        
        **Nguyên Nhân:**
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


def render_gbs_calculator():
    """Simplified GBS calculator for protocol"""
    st.markdown("#### 🩸 Glasgow-Blatchford Score Calculator")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        gender = st.radio("**Giới tính:**", ["Nam", "Nữ"], horizontal=True, key="gbs_gender")
        
        bun_mgdl = st.number_input(
            "**BUN (mg/dL):**",
            min_value=0.0,
            max_value=200.0,
            value=15.0,
            step=1.0,
            key="gbs_bun",
            help="Bình thường: 7-20 mg/dL"
        )
        
        hgb = st.number_input(
            "**Hemoglobin (g/dL):**",
            min_value=3.0,
            max_value=20.0,
            value=13.0,
            step=0.1,
            key="gbs_hgb"
        )
        
        sbp = st.number_input(
            "**SBP (mmHg):**",
            min_value=50,
            max_value=250,
            value=120,
            step=5,
            key="gbs_sbp"
        )
        
        hr = st.number_input(
            "**Nhịp tim (lần/phút):**",
            min_value=30,
            max_value=200,
            value=80,
            step=5,
            key="gbs_hr"
        )
        
        melena = st.checkbox("**Phân đen (Melena)**", key="gbs_melena")
        syncope = st.checkbox("**Ngất (Syncope)**", key="gbs_syncope")
        liver_disease = st.checkbox("**Bệnh gan**", key="gbs_liver")
        heart_failure = st.checkbox("**Suy tim**", key="gbs_hf")
    
    with col2:
        if st.button("🧮 Tính GBS", type="primary", use_container_width=True, key="calc_gbs"):
            gbs = calculate_gbs(
                bun_mgdl, hgb, sbp, hr, melena, syncope,
                liver_disease, heart_failure, gender
            )
            
            st.markdown("### 📊 Kết quả")
            st.metric("**GBS Score:**", f"{gbs}", help="0-23 điểm")
            
            if gbs == 0:
                st.success("**Nguy cơ rất thấp**")
                st.info("✅ Có thể xuất viện an toàn\n✅ EGD sớm 24h")
            elif gbs <= 1:
                st.success("**Nguy cơ thấp**")
                st.info("✅ Có thể xuất viện sớm\n✅ EGD trong 24h")
            elif gbs <= 5:
                st.warning("**Nguy cơ trung bình**")
                st.info("⚠️ Nhập viện\n⚠️ EGD trong 24h")
            else:
                st.error("**Nguy cơ cao**")
                st.error("🚨 Nhập viện ngay\n🚨 EGD <12h\n🚨 Cần can thiệp sớm")


def render_rockall_calculator():
    """Simplified Rockall calculator for protocol"""
    st.markdown("#### 🩸 Rockall Score Calculator")
    
    version = st.radio(
        "**Phiên bản:**",
        ["Pre-endoscopy (Clinical)", "Complete (Sau nội soi)"],
        key="rockall_version"
    )
    
    is_complete = "Complete" in version
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        age = st.number_input("**Tuổi:**", min_value=0, max_value=120, value=50, step=1, key="rockall_age")
        age_score = 0 if age < 60 else (1 if age < 80 else 2)
        
        sbp = st.number_input("**SBP (mmHg):**", min_value=50, max_value=250, value=120, step=5, key="rockall_sbp")
        hr = st.number_input("**Nhịp tim (lần/phút):**", min_value=30, max_value=200, value=80, step=5, key="rockall_hr")
        
        if sbp >= 100 and hr < 100:
            shock_score = 0
        elif sbp >= 100:
            shock_score = 1
        else:
            shock_score = 2
        
        comorbidity = st.radio(
            "**Bệnh kèm theo:**",
            ["Không có hoặc nhẹ", "Suy tim, bệnh mạch vành", "Suy thận, suy gan, ung thư di căn"],
            key="rockall_comorbidity"
        )
        comorbidity_score = 0 if "Không" in comorbidity else (2 if "Suy tim" in comorbidity else 3)
        
        pre_endo_score = age_score + shock_score + comorbidity_score
        
        if is_complete:
            st.markdown("---")
            st.markdown("**Kết quả nội soi:**")
            diagnosis = st.radio(
                "**Chẩn đoán:**",
                ["Mallory-Weiss/không tổn thương", "Các chẩn đoán khác", "Ung thư"],
                key="rockall_diagnosis"
            )
            diagnosis_score = 0 if "Mallory" in diagnosis else (1 if "Ung thư" in diagnosis else 2)
            
            stigmata = st.radio(
                "**Dấu hiệu xuất huyết:**",
                ["Không có dấu hiệu", "Blood in stomach, visible vessel, clot", "Active bleeding"],
                key="rockall_stigmata"
            )
            stigmata_score = 0 if "Không" in stigmata else (1 if "Active" in stigmata else 2)
            
            total_score = pre_endo_score + diagnosis_score + stigmata_score
        else:
            total_score = pre_endo_score
    
    with col2:
        if st.button("🧮 Tính Rockall", type="primary", use_container_width=True, key="calc_rockall"):
            st.markdown("### 📊 Kết quả")
            st.metric("**Rockall Score:**", f"{total_score}", help="0-7 (pre) hoặc 0-11 (complete)")
            
            if not is_complete:
                if total_score == 0:
                    st.success("**Nguy cơ rất thấp**\nTử vong: 0.2%")
                elif total_score <= 2:
                    st.success("**Nguy cơ thấp**\nTử vong: 0.2-0.5%")
                elif total_score <= 4:
                    st.warning("**Nguy cơ trung bình**\nTử vong: 3-5%")
                else:
                    st.error("**Nguy cơ cao**\nTử vong: 11-25%\n🚨 Cần EGD sớm")
            else:
                if total_score <= 2:
                    st.success("**Nguy cơ rất thấp**\nTử vong: 0.2%")
                elif total_score <= 3:
                    st.success("**Nguy cơ thấp**\nTử vong: 2.9%")
                elif total_score <= 5:
                    st.warning("**Nguy cơ trung bình**\nTử vong: 5.3%")
                elif total_score <= 7:
                    st.error("**Nguy cơ cao**\nTử vong: 10.8%")
                else:
                    st.error("**Nguy cơ rất cao**\nTử vong: 26.7%")


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

