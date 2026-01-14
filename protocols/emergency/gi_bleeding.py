"""
GI Bleeding Protocol
Upper & Lower GI Bleeding Management
Risk Stratification & Management Steps
"""

import streamlit as st
from scores.gi.glasgow_blatchford import calculate_gbs
from protocols.references_config import get_references
from components.references import render_references_section
from components.evidence_badge import (
    render_evidence_badge,
    render_evidence_summary,
    Citation
)
from components.phase1_protocol_enhancer import (
    render_protocol_header,
    render_recommendation_with_evidence,
    render_protocol_footer
)


def render():
    """GI Bleeding Protocol"""
    st.subheader("🩸 GI Bleeding Protocol")
    st.caption("Upper & Lower GI Bleeding - Risk Stratification & Management")
    
    # Enhanced header with Phase 1 components
    render_protocol_header(
        protocol_name="GI Bleeding",
        guideline_source="ACG 2024, BSG 2021, AASLD 2021",
        show_version=True,
        show_evidence_summary=True
    )
    
    # ACG/BSG Guidelines Summary
    with st.expander("📚 ACG 2024 & BSG 2021 Guidelines - Key Recommendations", expanded=False):
        st.markdown("""
        **ACG 2024 Guidelines for Upper GI Bleeding:**
        
        **Class I Recommendations (Strong Evidence):**
        - Risk stratification using Glasgow-Blatchford Score (GBS) for all patients
        - Early endoscopy (<24h) for high-risk patients (GBS ≥6)
        - PPI therapy before and after endoscopy
        - Endoscopic therapy for high-risk lesions (Forrest Ia, Ib, IIa, IIb)
        
        **BSG 2021 Guidelines:**
        - Risk stratification with GBS and Rockall scores
        - Endoscopy within 24h for all patients
        - Endoscopy <12h for high-risk patients
        - PPI high-dose IV before endoscopy
        - Dual therapy (PPI + endoscopic therapy) for peptic ulcer bleeding
        
        **Key Updates:**
        - GBS preferred over Rockall for pre-endoscopy risk stratification
        - Early endoscopy (<24h) standard of care
        - High-dose PPI (80mg bolus + 8mg/h infusion) before endoscopy
        - Tranexamic acid may be considered in selected patients
        """)
    
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
    """Upper GI Bleeding Protocol - ACG 2024, BSG 2021"""
    
    st.error("## 🚨 UPPER GI BLEEDING (UGIB) PROTOCOL")
    st.error("**CODE GI BLEED - Xử trí khẩn cấp!**")
    
    # ACG 2024 Evidence Badge
    render_evidence_badge(
        level="Class I, Level A",
        recommendation="Risk stratification using Glasgow-Blatchford Score for all patients with UGIB",
        citation=Citation(
            source="ACG 2024 Guidelines",
            title="Management of Patients With Ulcer Bleeding",
            year=2024
        )
    )
    
    st.markdown("### 1️⃣ Đánh giá & Resuscitation (< 30 Phút)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.error("""
        **ABC - Đường thở, Hô hấp, Tuần hoàn:**
        
        **A - Airway:**
        - Đảm bảo đường thở thông thoáng
        - Cân nhắc đặt nội khí quản nếu:
          * GCS <8
          * Nôn máu nhiều
          * Risk aspiration cao
        
        **B - Breathing:**
        - O₂ để duy trì SpO₂ >94%
        - Theo dõi SpO₂ liên tục
        
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
    st.markdown("### 2️⃣ Resuscitation - Bù dịch & Máu")
    
    st.info("""
    **Fluid Resuscitation:**
    
    **Nếu tụt huyết áp hoặc shock:**
    1. **Crystalloid:** NS 0.9% hoặc LR
       - Liều bolus 500-1000ml
       - Đánh giá đáp ứng
       - Lặp lại nếu cần
    
    2. **Blood Products:**
       - **Nếu Hgb <7 g/dL:** Truyền máu
       - **Nếu Hgb 7-10 g/dL:** Tùy tình trạng lâm sàng
       - **Nếu Hgb >10 g/dL:** Thường không cần (trừ khi shock hoặc xuất huyết tiếp)
    
    3. **Phác đồ truyền máu khối lượng lớn (nếu xuất huyết nặng):**
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
    st.markdown("### 3️⃣ Tranexamic Acid (TXA) - Cầm máu")
    
    st.markdown("#### 💉 Tranexamic Acid (TXA) Protocol")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("##### 📊 Tính liều TXA")
        
        weight = st.number_input(
            "**Cân nặng (kg):**",
            min_value=40.0,
            max_value=150.0,
            value=70.0,
            step=0.1,
            key="txa_weight"
        )
        
        # TXA dosing: 1g IV q8h × 3 ngày (HALT-IT trial)
        bolus_dose = 1.0  # g
        maintenance_dose = 1.0  # g q8h
        
        st.metric("**Liều bolus:**", f"{bolus_dose:.0f} g IV", help="Truyền trong 10 phút")
        st.metric("**Liều duy trì:**", f"{maintenance_dose:.0f} g IV q8h", help="× 3 ngày (72 giờ)")
        st.metric("**Tổng thời gian:**", "3 ngày", help="72 giờ")
        
        st.info("""
        **Cách pha:**
        - TXA 1g pha trong 100ml NS
        - Truyền trong 10 phút
        - Lặp lại q8h × 3 ngày
        """)
    
    with col2:
        st.markdown("##### 📋 Chỉ định & Chống chỉ định")
        
        st.success("""
        **✅ Chỉ định TXA trong GI Bleeding:**
        
        **Theo HALT-IT trial (2019):**
        - ✅ Xuất huyết tiêu hóa trên (UGIB) nghi ngờ hoặc xác định
        - ✅ Có thể dùng trong vòng 8 giờ từ khi khởi phát triệu chứng
        - ✅ Có thể dùng cho cả variceal và non-variceal bleeding
        
        **Lợi ích:**
        - Giảm tỷ lệ tử vong do xuất huyết (RR 0.88)
        - Giảm tỷ lệ tái xuất huyết
        - An toàn, không tăng nguy cơ huyết khối trong nghiên cứu
        
        **Cơ chế:**
        - Ức chế plasmin → giảm fibrinolysis
        - Tăng cường hình thành cục máu đông
        """)
        
        st.warning("""
        **⚠️ Chống chỉ định:**
        - ❌ Dị ứng TXA
        - ❌ Huyết khối tĩnh mạch sâu (DVT) hoặc PE đang hoạt động
        - ❌ Tiền sử huyết khối động mạch (MI, stroke) trong 3 tháng
        - ❌ Suy thận nặng (CrCl <30 ml/min) - giảm liều
        - ❌ Động kinh không kiểm soát
        
        **⚠️ Thận trọng:**
        - Suy thận (giảm liều 50% nếu CrCl 30-60)
        - Tiền sử huyết khối
        - Rối loạn đông máu
        """)
        
        st.info("""
        **📊 Liều điều chỉnh theo chức năng thận:**
        - **CrCl >60 ml/min:** 1g q8h (liều chuẩn)
        - **CrCl 30-60 ml/min:** 1g q12h (giảm 50%)
        - **CrCl <30 ml/min:** Không khuyến cáo hoặc 1g q24h
        
        **⏱️ Timing:**
        - Bắt đầu càng sớm càng tốt
        - Tốt nhất trong vòng 3 giờ từ khi khởi phát
        - Có thể dùng đến 8 giờ
        """)
    
    st.markdown("---")
    st.markdown("### 4️⃣ Đảo ngược anticoagulation")
    
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
    st.markdown("### 5️⃣ Phân Luồng: Variceal vs Non-Variceal")
    
    bleeding_source = st.radio(
        "**Nghi ngờ nguyên nhân:**",
        ["Chưa xác định", "Không do giãn tĩnh mạch (PUD, Mallory-Weiss)", "Do giãn tĩnh mạch (Xơ gan/Varices)"],
        key="ugib_source"
    )
    
    st.markdown("---")
    
    if "Không do giãn tĩnh mạch" in bleeding_source or "Chưa xác định" in bleeding_source:
        st.markdown("#### 💊 Xuất huyết không do giãn tĩnh mạch - Phác đồ PPI")
        
        tab1, tab2 = st.tabs(["Tính toán liều PPI IV", "Hướng dẫn điều trị"])
        
        with tab1:
            st.markdown("##### 💉 Tính toán liều cao PPI IV")
            
            col1, col2 = st.columns([1, 2])
            
            with col1:
                ppi_type = st.selectbox(
                    "**Loại PPI:**",
                    ["Pantoprazole", "Omeprazole", "Esomeprazole"],
                    key="ppi_type"
                )
                
                method = st.radio(
                    "**Phương pháp:**",
                    ["Truyền liên tục (Ưu tiên)", "Liều bolus ngắt quãng"],
                    key="ppi_method"
                )
                
                if "Truyền liên tục" in method:
                    st.markdown("**Liều chuẩn:**")
                    st.info("""
                    - **Liều bolus:** 80mg IV trong 30 phút
                    - **Truyền tĩnh mạch:** 8mg/h × 72 giờ
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
                **PPI IV liều cao (Xuất huyết tiêu hóa trên không do giãn tĩnh mạch):**
                
                **Bước 1: Liều bolus**
                - {ppi_type} 80mg IV trong 30 phút
                - Bắt đầu ngay khi chẩn đoán UGIB
                
                **Bước 2: Truyền liên tục (nếu dùng)**
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
            - ❌ Xuất huyết do giãn tĩnh mạch (dùng Octreotide thay vì PPI)
            - ❌ Dị ứng PPI
            """)
    
    if "Do giãn tĩnh mạch" in bleeding_source or "Chưa xác định" in bleeding_source:
        st.markdown("---")
        st.markdown("#### 🩸 Xuất huyết do giãn tĩnh mạch - Phác đồ Octreotide")
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.markdown("##### 💉 Tính liều Octreotide")
            
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
            
            st.metric("**Liều bolus:**", f"{bolus_dose:.0f} mcg IV", help="Truyền trong 5 phút")
            st.metric("**Truyền tĩnh mạch:**", f"{infusion_rate:.0f} mcg/h", help="Tối đa 5 ngày")
            
            st.info("""
            **Cách pha:**
            - Octreotide 1mg (1000mcg) pha trong 50ml NS
            - Nồng độ: 20mcg/ml
            - Tốc độ: {:.1f} ml/h cho 25mcg/h
            """.format(infusion_rate / 20))
        
        with col2:
            st.markdown("##### 📋 Phác đồ xuất huyết do giãn tĩnh mạch")
            
            st.error("""
            **Điều trị xuất huyết do giãn tĩnh mạch:**
            
            1. **Octreotide:**
               - Liều bolus: 50-100mcg IV (truyền trong 5 phút)
               - Truyền tĩnh mạch: 25-50mcg/h × 5 ngày (tối đa)
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
    st.markdown("### 6️⃣ Chỉ định Nội soi - Decision Tree")
    
    st.markdown("#### ⏱️ Tính toán thời điểm nội soi")
    
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
    st.markdown("#### 🔍 Chuẩn bị nội soi")
    
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
        - ✅ Có thể cần đặt nội khí quản nếu nguy cơ cao
        
        **Sau nội soi:**
        - ✅ Theo dõi sát 24-48h
        - ✅ Tiếp tục PPI (nếu non-variceal)
        - ✅ Tiếp tục Octreotide (nếu variceal)
        """)
    
    st.markdown("---")
    st.markdown("### 7️⃣ Quản lý Theo Nguyên nhân")
    
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
        
        st.markdown("---")
        st.markdown("#### 🔧 Kỹ Thuật Cầm Máu Nội Soi Chi tiết")
        
        endo_tab1, endo_tab2, endo_tab3, endo_tab4, endo_tab5 = st.tabs([
            "📎 Hemostatic Clip", 
            "🔥 Thermal Therapy", 
            "💉 Injection Therapy", 
            "🔀 Combination Therapy",
            "📊 Forrest Classification"
        ])
        
        with endo_tab1:
            st.markdown("##### 📎 Hemostatic Clip (Endoscopic Clipping)")
            
            st.success("""
            **Cơ chế:**
            - Kẹp trực tiếp mạch máu đang chảy
            - Tạo áp lực cơ học để cầm máu
            - Ít tổn thương mô xung quanh
            
            **Chỉ định:**
            - ✅ Active bleeding (Forrest Ia, Ib)
            - ✅ Visible vessel (Forrest IIa)
            - ✅ Dieulafoy lesion
            - ✅ Mallory-Weiss tear
            - ✅ Post-polypectomy bleeding
            
            **Kỹ thuật:**
            1. Xác định điểm chảy máu
            2. Rửa sạch bằng nước muối để thấy rõ
            3. Đặt clip vuông góc với mạch máu
            4. Đóng clip chặt, đảm bảo kẹp được mạch máu
            5. Có thể đặt nhiều clip nếu cần
            
            **Ưu điểm:**
            - ✅ Hiệu quả cao (90-95%)
            - ✅ Ít tổn thương mô
            - ✅ Có thể dùng cho nhiều loại tổn thương
            - ✅ An toàn
            
            **Nhược điểm:**
            - ❌ Khó đặt ở một số vị trí (góc, sau dạ dày)
            - ❌ Có thể rơi sau vài ngày
            - ❌ Chi phí cao hơn
            
            **Theo dõi:**
            - Kiểm tra lại sau 24-48h
            - Clip thường tự rơi sau 1-2 tuần
            """)
        
        with endo_tab2:
            st.markdown("##### 🔥 Thermal Therapy")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("**Bipolar Electrocoagulation (BICAP):**")
                st.info("""
                **Cơ chế:**
                - Dòng điện xoay chiều qua mô
                - Tạo nhiệt làm đông máu
                
                **Kỹ thuật:**
                - Đặt probe tiếp xúc với điểm chảy máu
                - Năng lượng: 15-20W
                - Thời gian: 1-2 giây mỗi lần
                - Lặp lại 3-5 lần
                
                **Chỉ định:**
                - Visible vessel (Forrest IIa)
                - Active oozing (Forrest Ib)
                - Small ulcers
                """)
                
                st.markdown("**Monopolar Electrocoagulation:**")
                st.warning("""
                **Ít dùng hơn:**
                - Nguy cơ thủng cao hơn
                - Khó kiểm soát độ sâu
                """)
            
            with col2:
                st.markdown("**Argon Plasma Coagulation (APC):**")
                st.success("""
                **Cơ chế:**
                - Khí argon dẫn dòng điện
                - Đông máu bề mặt, không tiếp xúc
                
                **Kỹ thuật:**
                - Khoảng cách: 2-5mm
                - Năng lượng: 40-60W
                - Lưu lượng khí: 1-2 L/min
                - Quét đều bề mặt
                
                **Chỉ định:**
                - ✅ AVM (Angiodysplasia)
                - ✅ Gastric antral vascular ectasia (GAVE)
                - ✅ Radiation colitis
                - ✅ Superficial bleeding
                
                **Ưu điểm:**
                - ✅ Không tiếp xúc trực tiếp
                - ✅ Đồng đều, kiểm soát tốt
                - ✅ Phù hợp tổn thương rộng
                """)
                
                st.markdown("**Heater Probe:**")
                st.info("""
                **Cơ chế:**
                - Nhiệt trực tiếp từ probe
                - Đông máu + đè ép
                
                **Kỹ thuật:**
                - Đè ép trước khi làm nóng
                - Nhiệt độ: 250°C
                - Thời gian: 1-2 giây
                - Lặp lại 3-5 lần
                """)
        
        with endo_tab3:
            st.markdown("##### 💉 Injection Therapy")
            
            st.markdown("**Epinephrine Injection:**")
            st.success("""
            **Cơ chế:**
            - Co mạch tại chỗ
            - Tạo áp lực cơ học (volume effect)
            - Kích hoạt đông máu
            
            **Kỹ thuật:**
            - **Nồng độ:** 1:10,000 (0.1mg/ml) hoặc 1:20,000
            - **Liều:** 0.5-2ml mỗi điểm
            - **Tổng liều:** 10-20ml (không quá 30ml)
            - **Kỹ thuật:** 4 điểm xung quanh, sau đó vào giữa
            
            **Chỉ định:**
            - ✅ Active bleeding (Forrest Ia, Ib)
            - ✅ Visible vessel (Forrest IIa)
            - ✅ Thường dùng kết hợp với clip hoặc thermal
            
            **Ưu điểm:**
            - ✅ Dễ thực hiện
            - ✅ Hiệu quả tạm thời
            - ✅ Giảm chảy máu để thấy rõ tổn thương
            
            **Nhược điểm:**
            - ❌ Tác dụng ngắn (15-20 phút)
            - ❌ Nên kết hợp với phương pháp khác
            - ❌ Nguy cơ hoại tử nếu tiêm quá nhiều
            """)
            
            st.markdown("---")
            st.markdown("**Sclerosant Injection:**")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("**Ethanol 98%:**")
                st.warning("""
                **Liều:** 0.1-0.2ml mỗi điểm
                **Tổng:** Không quá 1-2ml
                **Nguy cơ:** Hoại tử, thủng
                **Ít dùng:** Chỉ khi không có phương pháp khác
                """)
            
            with col2:
                st.markdown("**Polidocanol:**")
                st.info("""
                **Nồng độ:** 1-3%
                **Liều:** 0.5-1ml mỗi điểm
                **An toàn hơn:** Ít nguy cơ hoại tử
                **Chỉ định:** Variceal bleeding (sclerotherapy)
                """)
        
        with endo_tab4:
            st.markdown("##### 🔀 Combination Therapy (Ưu tiên)")
            
            st.error("""
            **⚠️ QUAN TRỌNG: Combination therapy hiệu quả hơn đơn trị liệu!**
            
            **Tỷ lệ tái xuất huyết:**
            - Epinephrine đơn thuần: 15-20%
            - Clip đơn thuần: 5-10%
            - Combination: 2-5%
            """)
            
            st.markdown("**Các phác đồ kết hợp phổ biến:**")
            
            st.success("""
            **1. Epinephrine + Clip (Ưu tiên nhất):**
            - Bước 1: Tiêm epinephrine xung quanh để giảm chảy máu
            - Bước 2: Đặt clip vào điểm chảy máu
            - Hiệu quả: 95-98%
            
            **2. Epinephrine + Thermal:**
            - Bước 1: Tiêm epinephrine
            - Bước 2: Bipolar electrocoagulation hoặc heater probe
            - Hiệu quả: 90-95%
            
            **3. Clip + Thermal:**
            - Đặt clip trước
            - Sau đó đốt xung quanh để củng cố
            - Hiệu quả: 95%
            
            **4. Triple Therapy (Epinephrine + Clip + Thermal):**
            - Dùng cho trường hợp nặng
            - Hiệu quả: 98-99%
            """)
            
            st.markdown("---")
            st.markdown("**Quy trình chuẩn (Step-by-step):**")
            
            st.info("""
            **Bước 1: Chuẩn bị**
            - Rửa sạch bằng nước muối
            - Xác định điểm chảy máu chính xác
            - Chuẩn bị dụng cụ (clip, injector, thermal probe)
            
            **Bước 2: Injection (nếu cần)**
            - Tiêm epinephrine 1:10,000
            - 4 điểm xung quanh (0.5-1ml mỗi điểm)
            - 1 điểm vào giữa (1-2ml)
            - Đợi 30-60 giây để giảm chảy máu
            
            **Bước 3: Primary hemostasis**
            - Đặt clip vào điểm chảy máu (ưu tiên)
            - Hoặc dùng thermal therapy
            - Đảm bảo cầm máu hoàn toàn
            
            **Bước 4: Củng cố**
            - Nếu dùng clip: Có thể thêm thermal xung quanh
            - Nếu dùng thermal: Có thể đặt clip để củng cố
            
            **Bước 5: Kiểm tra**
            - Quan sát 5-10 phút
            - Đảm bảo không còn chảy máu
            - Rửa lại để xác nhận
            """)
        
        with endo_tab5:
            st.markdown("##### 📊 Forrest Classification")
            
            st.markdown("**Phân loại tổn thương xuất huyết:**")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.error("""
                **Forrest Ia - Active Spurting:**
                - Chảy máu phun thành tia
                - Nguy cơ cao nhất
                - Cần can thiệp ngay
                - Tỷ lệ tái xuất huyết: 55%
                
                **Forrest Ib - Active Oozing:**
                - Chảy máu rỉ rả
                - Nguy cơ cao
                - Cần can thiệp
                - Tỷ lệ tái xuất huyết: 43%
                """)
            
            with col2:
                st.warning("""
                **Forrest IIa - Visible Vessel:**
                - Thấy mạch máu nhưng không chảy
                - Nguy cơ trung bình-cao
                - Nên can thiệp
                - Tỷ lệ tái xuất huyết: 22%
                
                **Forrest IIb - Adherent Clot:**
                - Cục máu đông dính
                - Nguy cơ trung bình
                - Có thể can thiệp
                - Tỷ lệ tái xuất huyết: 10%
                """)
            
            st.success("""
            **Forrest IIc - Hematin Base:**
            - Đáy loét có màu đen (hematin)
            - Nguy cơ thấp
            - Không cần can thiệp
            - Tỷ lệ tái xuất huyết: 5%
            
            **Forrest III - Clean Base:**
            - Đáy loét sạch, không có dấu hiệu xuất huyết
            - Nguy cơ rất thấp
            - Không cần can thiệp
            - Tỷ lệ tái xuất huyết: 0-3%
            """)
            
            st.info("""
            **Khuyến nghị can thiệp:**
            - ✅ **Forrest Ia, Ib:** Bắt buộc can thiệp
            - ✅ **Forrest IIa:** Nên can thiệp
            - ⚠️ **Forrest IIb:** Có thể can thiệp (rửa sạch để đánh giá lại)
            - ❌ **Forrest IIc, III:** Không cần can thiệp
            """)
    
    with tab2:
        st.markdown("#### 🩸 Xuất huyết do giãn tĩnh mạch")
        
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
        
        st.markdown("---")
        st.markdown("#### 🔧 Kỹ Thuật Cầm Máu Nội Soi Cho Varices")
        
        variceal_endo_tab1, variceal_endo_tab2 = st.tabs(["📎 Band Ligation", "💉 Sclerotherapy"])
        
        with variceal_endo_tab1:
            st.markdown("##### 📎 Endoscopic Band Ligation (EBL)")
            
            st.success("""
            **Cơ chế:**
            - Thắt varices bằng dây cao su
            - Gây hoại tử và xơ hóa
            - Giảm nguy cơ tái xuất huyết
            
            **Kỹ thuật:**
            1. Xác định varices đang chảy máu hoặc có nguy cơ cao
            2. Hút varices vào cap
            3. Bắn band để thắt
            4. Có thể đặt nhiều band trong một lần nội soi
            5. Thường đặt từ dưới lên trên
            
            **Chỉ định:**
            - ✅ Variceal bleeding cấp tính
            - ✅ Dự phòng tái phát (secondary prophylaxis)
            - ✅ Varices lớn có nguy cơ cao
            
            **Ưu điểm:**
            - ✅ Hiệu quả cao (90-95% cầm máu)
            - ✅ Ít biến chứng hơn sclerotherapy
            - ✅ Tỷ lệ tái xuất huyết thấp hơn
            - ✅ Ít loét, hẹp thực quản
            
            **Nhược điểm:**
            - ❌ Khó thực hiện nếu varices nhỏ hoặc phẳng
            - ❌ Cần nội soi lại nhiều lần
            - ❌ Có thể gây đau ngực sau thủ thuật
            
            **Theo dõi:**
            - Nội soi lại sau 2-4 tuần
            - Lặp lại cho đến khi hết varices
            - Thường cần 2-4 lần nội soi
            """)
        
        with variceal_endo_tab2:
            st.markdown("##### 💉 Endoscopic Sclerotherapy")
            
            st.info("""
            **Cơ chế:**
            - Tiêm chất gây xơ vào varices
            - Gây viêm và xơ hóa
            - Tắc varices
            
            **Kỹ thuật:**
            1. Xác định varices đang chảy máu
            2. Tiêm sclerosant vào varices
            3. Có thể tiêm intravascular hoặc paravariceal
            4. Thường dùng: Ethanolamine oleate, Polidocanol, hoặc Sodium tetradecyl sulfate
            
            **Chỉ định:**
            - ✅ Variceal bleeding cấp tính (khi không thể band)
            - ✅ Varices nhỏ, phẳng không thể band
            - ✅ Dự phòng tái phát (ít dùng hơn band)
            
            **Liều:**
            - **Ethanolamine oleate:** 1-3ml mỗi varices
            - **Polidocanol:** 1-3ml mỗi varices
            - **Tổng liều:** Không quá 20ml mỗi lần
            
            **Ưu điểm:**
            - ✅ Có thể dùng cho varices nhỏ
            - ✅ Hiệu quả cầm máu tốt (85-90%)
            - ✅ Có thể thực hiện ngay
            
            **Nhược điểm:**
            - ❌ Nhiều biến chứng hơn band ligation
            - ❌ Loét thực quản (20-30%)
            - ❌ Hẹp thực quản (5-10%)
            - ❌ Tỷ lệ tái xuất huyết cao hơn
            
            **Biến chứng:**
            - Loét thực quản
            - Hẹp thực quản
            - Tràn khí màng phổi (hiếm)
            - Nhiễm trùng (hiếm)
            """)
        
        st.markdown("---")
        st.markdown("#### 🚨 TIPS (Transjugular Intrahepatic Portosystemic Shunt) - Chỉ định Chi tiết")
        
        tips_tab1, tips_tab2, tips_tab3 = st.tabs(["📋 Chỉ định", "⚠️ Chống chỉ định", "📊 Đánh giá"])
        
        with tips_tab1:
            st.markdown("##### ✅ Chỉ định TIPS Cho Variceal Bleeding")
            
            st.error("""
            **🚨 CHỈ ĐỊNH KHẨN CẤP (Rescue TIPS):**
            
            **1. Xuất huyết không kiểm soát được:**
            - ✅ Xuất huyết tiếp diễn sau điều trị nội soi
            - ✅ Không thể cầm máu bằng band ligation/sclerotherapy
            - ✅ Xuất huyết nặng, không đáp ứng với medical therapy
            
            **2. Tái xuất huyết sớm:**
            - ✅ Tái xuất huyết trong vòng 5 ngày sau điều trị nội soi
            - ✅ Tái xuất huyết nhiều lần sau điều trị nội soi
            
            **3. Không thể thực hiện nội soi:**
            - ✅ Bệnh nhân không thể chịu đựng nội soi
            - ✅ Không có điều kiện nội soi can thiệp
            - ✅ Varices ở vị trí khó tiếp cận
            """)
            
            st.warning("""
            **⚠️ CHỈ ĐỊNH DỰ PHÒNG (Prophylactic TIPS):**
            
            **Early TIPS (Trong vòng 72 giờ):**
            - ✅ Child-Pugh B với active bleeding tại nội soi
            - ✅ Child-Pugh C (bất kể tình trạng bleeding)
            - ✅ Giảm tỷ lệ tử vong và tái xuất huyết
            
            **Secondary Prophylaxis:**
            - ✅ Tái xuất huyết sau điều trị nội soi + beta-blocker
            - ✅ Không dung nạp beta-blocker
            - ✅ Varices lớn, nguy cơ cao
            """)
            
            st.info("""
            **📊 Tiêu chuẩn Chọn Lựa:**
            
            **Bệnh nhân phù hợp:**
            - ✅ Child-Pugh score: B hoặc C
            - ✅ MELD score: <18 (tốt nhất)
            - ✅ Không có bệnh tim phổi nặng
            - ✅ Không có bệnh não gan nặng (grade 3-4)
            - ✅ Không có nhiễm trùng đang hoạt động
            
            **Timing:**
            - **Early TIPS:** Trong vòng 72 giờ từ khi nhập viện
            - **Rescue TIPS:** Khi điều trị nội soi thất bại
            - **Elective TIPS:** Dự phòng tái phát sau khi ổn định
            """)
        
        with tips_tab2:
            st.markdown("##### ❌ Chống chỉ định TIPS")
            
            st.error("""
            **🚫 CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI:**
            
            - ❌ **Bệnh não gan nặng (Hepatic Encephalopathy grade 3-4):**
              * TIPS làm tăng nguy cơ bệnh não gan
              * Cần điều trị bệnh não gan trước
            
            - ❌ **Nhiễm trùng đang hoạt động:**
              * SBP (Spontaneous Bacterial Peritonitis)
              * Nhiễm trùng huyết
              * Viêm phổi
              * Cần điều trị kháng sinh trước
            
            - ❌ **Bệnh tim phổi nặng:**
              * Suy tim nặng (EF <30%)
              * Tăng áp phổi (PAP >45 mmHg)
              * TIPS làm tăng preload tim
            
            - ❌ **Tắc tĩnh mạch cửa hoàn toàn:**
              * Không thể đặt TIPS
              * Cần đánh giá bằng doppler siêu âm trước
            
            - ❌ **Ung thư gan tiến triển:**
              * HCC lớn hoặc di căn
              * Tiên lượng xấu
            """)
            
            st.warning("""
            **⚠️ CHỐNG CHỈ ĐỊNH TƯƠNG ĐỐI:**
            
            - ⚠️ **Child-Pugh A:**
              * Thường không cần TIPS
              * Điều trị nội soi + beta-blocker đủ
            
            - ⚠️ **MELD >18:**
              * Nguy cơ tử vong sau TIPS cao
              * Cân nhắc ghép gan thay vì TIPS
            
            - ⚠️ **Tuổi >70:**
              * Nguy cơ biến chứng cao hơn
              * Đánh giá từng trường hợp
            
            - ⚠️ **Bệnh thận mạn:**
              * TIPS có thể làm nặng thêm
              * Cân nhắc cẩn thận
            
            - ⚠️ **Đang dùng thuốc chống đông:**
              * Nguy cơ chảy máu
              * Cần đảo ngược trước TIPS
            """)
        
        with tips_tab3:
            st.markdown("##### 📊 Đánh giá Trước TIPS")
            
            st.markdown("**Workup trước TIPS:**")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.success("""
                **1. Đánh giá chức năng gan:**
                - Child-Pugh score
                - MELD score
                - Albumin, bilirubin, PT/INR
                - LFT đầy đủ
                
                **2. Đánh giá giải phẫu:**
                - **Doppler siêu âm:**
                  * Đánh giá tĩnh mạch cửa
                  * Đánh giá tĩnh mạch gan
                  * Đánh giá dòng chảy
                  * Loại trừ tắc hoàn toàn
                
                **3. Đánh giá tim mạch:**
                - ECG
                - Echo tim (nếu cần)
                - Đánh giá chức năng tim
                """)
            
            with col2:
                st.info("""
                **4. Đánh giá thần kinh:**
                - Đánh giá bệnh não gan
                - MMSE hoặc các test tâm thần
                - Loại trừ grade 3-4
                
                **5. Đánh giá nhiễm trùng:**
                - Cấy máu
                - Cấy dịch cổ trướng (nếu có)
                - X-quang ngực
                - Loại trừ nhiễm trùng đang hoạt động
                
                **6. Đánh giá chức năng thận:**
                - Creatinine, BUN
                - CrCl
                - Loại trừ suy thận nặng
                """)
            
            st.markdown("---")
            st.markdown("**Kết quả mong đợi sau TIPS:**")
            
            st.success("""
            **Hiệu quả:**
            - ✅ Cầm máu: 90-95%
            - ✅ Giảm portal pressure: 50-60%
            - ✅ Giảm tái xuất huyết: 70-80%
            - ✅ Cải thiện ascites
            
            **Biến chứng:**
            - ⚠️ Bệnh não gan mới hoặc nặng lên: 20-30%
            - ⚠️ Tắc shunt: 20-30% trong 1 năm
            - ⚠️ Suy tim: 5-10%
            - ⚠️ Nhiễm trùng: 2-5%
            - ⚠️ Tử vong: 5-10% (tùy Child-Pugh)
            
            **Theo dõi sau TIPS:**
            - Siêu âm doppler sau 1 tuần, 1 tháng, 3 tháng, 6 tháng, 1 năm
            - Đánh giá bệnh não gan
            - Điều chỉnh thuốc (lactulose, rifaximin)
            - Điều chỉnh beta-blocker (có thể giảm liều)
            """)
            
            st.markdown("---")
            st.markdown("**So sánh Early TIPS vs Standard Care:**")
            
            st.info("""
            **Early TIPS (Trong 72h):**
            - ✅ Giảm tỷ lệ tử vong: 20% → 10%
            - ✅ Giảm tái xuất huyết: 50% → 10%
            - ✅ Giảm thời gian nằm viện
            - ✅ Chỉ định: Child-Pugh B với active bleeding hoặc Child-Pugh C
            
            **Standard Care (Nội soi + Medical):**
            - Tỷ lệ tử vong: 20-30%
            - Tỷ lệ tái xuất huyết: 30-50%
            - Chỉ định: Child-Pugh A hoặc B không active bleeding
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
        st.markdown("#### 🔍 Nguyên nhân Khác")
        
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
    st.markdown("### 8️⃣ Theo dõi & Dự phòng Tái phát")
    
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
    
    **Nội soi đại tràng khẩn cấp (< 24h):**
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
    st.markdown("### 4️⃣ Quản lý Theo Nguyên nhân")
    
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
        st.markdown("#### 🔍 Nguyên nhân Khác")
        
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
    st.markdown("#### 🩸 Tính toán điểm Glasgow-Blatchford")
    
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
    st.markdown("#### 🩸 Tính toán điểm Rockall")
    
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
    
    1. ✅ **ABC** - Đường thở, Hô hấp, Tuần hoàn
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
    
    # Enhanced footer with Phase 1 component
    render_protocol_footer("GI Bleeding")

