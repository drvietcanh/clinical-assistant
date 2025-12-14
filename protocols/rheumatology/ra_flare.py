"""
Acute Flare of Rheumatoid Arthritis Protocol
ACR 2021 Guidelines, EULAR Recommendations
Management of RA Flare/Exacerbation
"""

import streamlit as st


def render():
    """Acute Flare of Rheumatoid Arthritis Protocol"""
    st.subheader("🦴 Acute Flare of Rheumatoid Arthritis Protocol")
    st.caption("ACR 2021, EULAR Guidelines - RA Flare Management")
    
    st.info("""
    **RA Flare là đợt xấu đi cấp tính các triệu chứng viêm khớp dạng thấp.**
    - **Triệu chứng:** Đau, sưng, cứng khớp tăng đột ngột
    - **Duration:** Vài ngày đến vài tuần
    - **Management:** Điều trị triệu chứng + điều chỉnh DMARDs
    """)
    
    st.markdown("---")
    
    # Assessment
    st.markdown("### 1️⃣ Đánh giá Flare")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Triệu chứng")
        joint_pain = st.checkbox("**Đau khớp tăng**", key="ra_pain")
        joint_swelling = st.checkbox("**Sưng khớp**", key="ra_swelling")
        morning_stiffness = st.checkbox("**Cứng khớp buổi sáng >30 phút**", key="ra_stiffness")
        fatigue = st.checkbox("**Mệt mỏi**", key="ra_fatigue")
        fever = st.checkbox("**Sốt nhẹ**", key="ra_fever")
        
        st.markdown("#### Số Khớp Bị Ảnh Hưởng")
        joint_count = st.number_input(
            "**Số khớp sưng/đau:**",
            min_value=0,
            max_value=68,
            value=5,
            step=1,
            key="ra_joint_count"
        )
    
    with col2:
        st.markdown("#### Đánh giá Mức Độ")
        
        # Calculate severity
        symptoms_count = sum([joint_pain, joint_swelling, morning_stiffness, fatigue, fever])
        
        if joint_count >= 10 or symptoms_count >= 4:
            st.error("## 🚨 FLARE NẶNG")
            st.error("Cần điều trị tích cực")
            severity = "Severe"
        elif joint_count >= 5 or symptoms_count >= 3:
            st.warning("## ⚠️ FLARE TRUNG BÌNH")
            st.warning("Cần điều chỉnh điều trị")
            severity = "Moderate"
        else:
            st.success("## ✅ FLARE NHẸ")
            st.success("Có thể điều trị triệu chứng")
            severity = "Mild"
        
        st.metric("**Số khớp:**", f"{joint_count}")
        st.metric("**Triệu chứng:**", f"{symptoms_count}/5")
    
    st.markdown("---")
    st.markdown("### 2️⃣ Điều trị Flare")
    
    tab1, tab2, tab3 = st.tabs(["💊 Symptomatic Treatment", "🔄 DMARD Adjustment", "💉 Biologics"])
    
    with tab1:
        st.markdown("#### 💊 Điều trị Triệu chứng")
        
        st.success("""
        **NSAIDs (Non-Steroidal Anti-Inflammatory Drugs):**
        
        **Options:**
        - **Naproxen:** 500mg PO BID × 7-14 ngày
        - **Ibuprofen:** 600-800mg PO TID × 7-14 ngày
        - **Diclofenac:** 50mg PO TID × 7-14 ngày
        - **Celecoxib:** 200mg PO BID × 7-14 ngày (nếu có GI risk)
        
        **Contraindications:**
        - CKD (CrCl <30)
        - GI bleeding risk
        - Heart failure
        - Active peptic ulcer
        
        **PPI:** Cân nhắc nếu có GI risk
        """)
        
        st.markdown("---")
        st.markdown("#### 💉 Corticosteroids (Nếu NSAIDs không đủ)")
        
        st.warning("""
        **Corticosteroids cho Flare:**
        
        **Oral:**
        - **Prednisone:** 10-20mg PO QD × 5-7 ngày, sau đó giảm dần
        - **Methylprednisolone:** 4-8mg PO TID × 5-7 ngày
        
        **Intra-articular (nếu mono/pauciarticular):**
        - **Triamcinolone:** 10-40mg (tùy khớp)
        - **Methylprednisolone:** 20-80mg (tùy khớp)
        
        **Lưu ý:**
        - Dùng ngắn hạn (≤2 tuần)
        - Giảm dần liều
        - Monitor glucose, BP
        """)
    
    with tab2:
        st.markdown("#### 🔄 Điều Chỉnh DMARDs")
        
        st.info("""
        **Nếu đang dùng DMARDs:**
        
        **1. Kiểm tra compliance:**
        - Bệnh nhân có uống thuốc đều không?
        - Có tác dụng phụ không?
        
        **2. Điều chỉnh liều:**
        - **Methotrexate:** Có thể tăng liều (7.5mg → 15mg → 20-25mg/tuần)
        - **Sulfasalazine:** Có thể tăng liều (1g → 2g → 3g/ngày)
        - **Leflunomide:** Có thể tăng liều (10mg → 20mg/ngày)
        
        **3. Thêm DMARD:**
        - Nếu đang dùng 1 DMARD: Có thể thêm DMARD thứ 2 (combination therapy)
        - Methotrexate + Sulfasalazine
        - Methotrexate + Hydroxychloroquine
        - Triple therapy: MTX + SSZ + HCQ
        """)
        
        st.markdown("---")
        st.markdown("#### 📋 DMARD Options")
        
        dmard_options = {
            "DMARD": ["Methotrexate", "Sulfasalazine", "Leflunomide", "Hydroxychloroquine", "Azathioprine"],
            "Liều Khởi Đầu": ["7.5-10mg/tuần", "500mg BID", "10mg QD", "200mg BID", "50mg QD"],
            "Liều Tối Đa": ["20-25mg/tuần", "3g/ngày", "20mg QD", "400mg/ngày", "2-3mg/kg/ngày"],
            "Thời Gian Tác Dụng": ["4-12 tuần", "8-12 tuần", "4-12 tuần", "3-6 tháng", "8-12 tuần"]
        }
        
        import pandas as pd
        st.dataframe(pd.DataFrame(dmard_options), use_container_width=True, hide_index=True)
    
    with tab3:
        st.markdown("#### 💉 Biologics (Nếu DMARDs không đủ)")
        
        st.error("""
        **Chỉ định cho Biologics:**
        - Flare nặng, không đáp ứng với DMARDs
        - Đã dùng ≥2 DMARDs (trong đó có MTX) không đáp ứng
        - High disease activity (DAS28 >5.1)
        
        **Options:**
        
        **TNF-α Inhibitors:**
        - **Adalimumab:** 40mg SC q2 weeks
        - **Etanercept:** 50mg SC q week
        - **Infliximab:** 3-5 mg/kg IV q8 weeks
        - **Golimumab:** 50mg SC q month
        - **Certolizumab:** 200mg SC q2 weeks
        
        **Non-TNF Biologics:**
        - **Tocilizumab (IL-6):** 8mg/kg IV q4 weeks hoặc 162mg SC q2 weeks
        - **Rituximab (CD20):** 1000mg IV × 2 (2 tuần apart), lặp lại q6 months
        - **Abatacept (CTLA-4):** 10mg/kg IV q4 weeks hoặc 125mg SC q week
        - **Tofacitinib (JAK):** 5mg PO BID
        
        **Lưu ý:**
        - Cần screening TB, HBV, HCV trước khi dùng
        - Monitor infection
        - Không dùng nếu có infection active
        """)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Monitoring")
    
    st.info("""
    **Theo dõi:**
    - **DAS28:** Đánh giá mỗi 3-6 tháng
    - **CRP, ESR:** Mỗi 3-6 tháng
    - **Joint count:** Mỗi lần khám
    - **Function:** HAQ (Health Assessment Questionnaire)
    
    **Labs (nếu dùng DMARDs/Biologics):**
    - CBC, LFT, Creatinine: Mỗi 1-3 tháng
    - CXR: Trước khi dùng biologics (TB screening)
    - HBV, HCV: Trước khi dùng biologics
    """)
    
    st.markdown("---")
    st.markdown("### 4️⃣ Patient Education")
    
    st.success("""
    **Giáo dục bệnh nhân:**
    - **Rest:** Nghỉ ngơi khớp bị ảnh hưởng
    - **Ice/Heat:** Chườm lạnh hoặc nóng
    - **Exercise:** Tập luyện nhẹ nhàng (không trong lúc flare nặng)
    - **Compliance:** Uống thuốc đều đặn
    - **Follow-up:** Tái khám sau 2-4 tuần
    """)
    
    st.markdown("---")
    st.markdown("### 📚 References")
    
    st.markdown("""
    1. **ACR Guidelines 2021** - Rheumatoid Arthritis Treatment
    2. **EULAR Recommendations 2022** - RA Management
    3. **UpToDate:** Rheumatoid Arthritis Treatment - Last updated 2024
    """)
    
    st.markdown("---")
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể.")

