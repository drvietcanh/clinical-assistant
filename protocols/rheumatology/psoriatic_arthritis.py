"""
Psoriatic Arthritis Management Protocol
GRAPPA 2015, GRAPPA 2021, ACR 2018, ACR 2021 Guidelines
Psoriatic Arthritis (Viêm khớp vảy nến) Management
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Psoriatic Arthritis Management Protocol"""
    st.subheader("🦴 Viêm Khớp Vảy Nến (Psoriatic Arthritis) Protocol")
    st.caption("GRAPPA 2015, GRAPPA 2021, ACR 2018, ACR 2021 Guidelines - PsA Management")
    
    st.info("""
    **Psoriatic Arthritis (PsA) là viêm khớp ở bệnh nhân vảy nến**
    - **Prevalence:** 0.1-0.3% dân số, 20-30% bệnh nhân vảy nến
    - **Triệu chứng:** Viêm khớp, viêm gân, viêm cột sống, tổn thương da
    - **Pathophysiology:** Viêm mạn tính, liên quan đến psoriasis
    - **Complications:** Hủy khớp, dính khớp, bệnh tim mạch
    """)
    
    st.markdown("---")
    
    # Disease pattern
    pattern = st.radio(
        "**Kiểu bệnh:**",
        ["Viêm khớp ngoại vi", "Viêm cột sống", "Viêm gân (Enthesitis)", "Dactylitis", "Hỗn hợp"],
        key="psa_pattern"
    )
    
    st.markdown("---")
    
    # Disease activity
    activity = st.radio(
        "**Mức độ hoạt động bệnh:**",
        ["Thấp (Low Activity)", "Trung bình (Moderate Activity)", "Cao (High Activity)"],
        key="psa_activity"
    )
    
    st.markdown("---")
    
    if "Thấp" in activity:
        render_low_activity_psa(pattern)
    elif "Trung bình" in activity:
        render_moderate_activity_psa(pattern)
    else:
        render_high_activity_psa(pattern)


def render_low_activity_psa(pattern):
    """Low Activity PsA Protocol"""
    
    st.success("## ✅ LOW ACTIVITY PSA PROTOCOL")
    
    st.markdown("### 1️⃣ Chẩn đoán")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Clinical Features:**
        - **Viêm khớp:** Không đối xứng hoặc đối xứng
        - **Khớp thường gặp:** Bàn tay, bàn chân, gối
        - **Dactylitis:** "Ngón tay/xúc xích" (sưng toàn bộ ngón)
        - **Enthesitis:** Viêm điểm bám gân (gót chân, khuỷu)
        - **Psoriasis:** Tổn thương da, móng
        
        **Viêm cột sống:**
        - Đau lưng viêm
        - Hạn chế vận động
        """)
    
    with col2:
        st.warning("""
        **Diagnostic:**
        - **CASPAR Criteria:** ≥3 điểm
          * Psoriasis hiện tại/tiền sử/gia đình
          * Dactylitis/enthesitis
          * RF (-)
          * Dactylitis trên X-ray
          * Móng tay thay đổi
        
        **Labs:**
        - RF, CCP (-) (phân biệt với RA)
        - CRP, ESR tăng
        - HLA-B27 (+) trong 20-30% (nếu có viêm cột sống)
        
        **X-ray:**
        - Hủy khớp, "pencil-in-cup"
        - Syndesmophytes (nếu có viêm cột sống)
        """)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Điều trị - First Line")
    
    st.success("""
    **Non-Pharmacological:**
    
    **1. Tập luyện:**
    - Duy trì vận động khớp
    - Strengthening
    - Tránh chấn thương
    
    **2. Vật lý trị liệu:**
    - Tư vấn tư thế
    - Dụng cụ hỗ trợ
    
    **3. Psoriasis:**
    - Điều trị tổn thương da (nếu có)
    - Tránh kích thích da
    """)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Điều trị - Pharmacological")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **NSAIDs (First Line):**
        - **Naproxen:** 500mg PO BID
        - **Diclofenac:** 50mg PO TID
        - **Ibuprofen:** 600-800mg PO TID
        - **Celecoxib:** 200mg PO BID
        
        **PPI:** Cân nhắc nếu có GI risk
        """)
    
    with col2:
        st.warning("""
        **DMARDs (Nếu NSAIDs không đủ):**
        - **Methotrexate:** 10-15mg PO/tuần (ưu tiên)
        - **Sulfasalazine:** 1-2g PO BID
        - **Leflunomide:** 10-20mg PO QD
        
        **Lưu ý:**
        - MTX hiệu quả cho cả viêm khớp và psoriasis
        - Đáp ứng trong 4-12 tuần
        """)


def render_moderate_activity_psa(pattern):
    """Moderate Activity PsA Protocol"""
    
    st.warning("## ⚠️ MODERATE ACTIVITY PSA PROTOCOL")
    
    st.markdown("### 1️⃣ Điều trị - Combination Therapy")
    
    st.warning("""
    **Moderate Activity:** Đau nhiều, nhiều khớp, hạn chế chức năng
    
    **1. Non-Pharmacological (Tiếp tục):**
    - Tập luyện
    - Vật lý trị liệu
    - Điều trị psoriasis
    
    **2. Pharmacological:**
    - **NSAIDs** (full dose)
    - **DMARDs** (bắt buộc)
    - **Corticosteroids** (nếu cần, ngắn hạn)
    """)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Dosing Details")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("""
        **NSAIDs (Full Dose):**
        - **Naproxen:** 500mg PO BID
        - **Diclofenac:** 50mg PO TID
        - **Ibuprofen:** 800mg PO TID
        
        **PPI:** Nên dùng nếu dùng NSAIDs lâu dài
        """)
    
    with col2:
        st.info("""
        **DMARDs:**
        - **Methotrexate:** 15-20mg PO/tuần (ưu tiên)
        - **Sulfasalazine:** 2-3g/ngày
        - **Leflunomide:** 20mg PO QD
        - **Duration:** 4-12 tuần để đánh giá đáp ứng
        
        **Corticosteroids (Ngắn hạn):**
        - **Prednisone:** 10-20mg PO QD × 2-4 tuần
        - **Intra-articular:** Triamcinolone 20-40mg (nếu cần)
        """)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Intra-articular Injection")
    
    st.warning("""
    **Corticosteroid Injection:**
    - **Triamcinolone:** 20-40mg (tùy khớp)
    - **Frequency:** Mỗi 3-6 tháng (nếu cần)
    - **Indication:** Đau khu trú, không đáp ứng với thuốc uống
    """)


def render_high_activity_psa(pattern):
    """High Activity PsA Protocol"""
    
    st.error("## 🚨 HIGH ACTIVITY PSA PROTOCOL")
    
    st.markdown("### 1️⃣ Điều trị - Aggressive Management")
    
    st.error("""
    **High Activity:** Đau nhiều, nhiều khớp, hạn chế chức năng rõ rệt, không đáp ứng với DMARDs
    
    **1. Non-Pharmacological (Tiếp tục):**
    - Tập luyện
    - Vật lý trị liệu
    - Điều trị psoriasis
    
    **2. Pharmacological:**
    - **DMARDs** (full dose)
    - **Biologics** (TNF-α inhibitors hoặc IL-17/IL-23 inhibitors)
    - **Small molecule inhibitors** (JAK inhibitors)
    """)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Biologics - TNF-α Inhibitors")
    
    st.warning("""
    **Chỉ định cho Biologics:**
    - Không đáp ứng với ≥1 DMARD (thường MTX)
    - High disease activity
    - Hủy khớp tiến triển
    
    **Options:**
    
    **TNF-α Inhibitors:**
    - **Adalimumab:** 40mg SC q2 weeks
    - **Etanercept:** 50mg SC q week
    - **Infliximab:** 5 mg/kg IV q8 weeks
    - **Golimumab:** 50mg SC q month
    - **Certolizumab:** 200mg SC q2 weeks
    
    **Lưu ý:**
    - Hiệu quả tốt cho cả viêm khớp và psoriasis
    - Đáp ứng trong 2-4 tuần
    - Cần screening TB, HBV, HCV
    """)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Biologics - IL-17/IL-23 Inhibitors")
    
    st.info("""
    **IL-17 Inhibitors (Nếu TNF-α không đủ hoặc chống chỉ định):**
    - **Secukinumab:** 150-300mg SC q4 weeks (loading: 0, 1, 2, 4 weeks)
    - **Ixekizumab:** 80mg SC q2 weeks (loading: 0, 2, 4 weeks)
    - **Brodalumab:** 210mg SC q2 weeks
    
    **IL-23 Inhibitors:**
    - **Guselkumab:** 100mg SC q8 weeks (loading: 0, 4 weeks)
    - **Risankizumab:** 150mg SC q12 weeks (loading: 0, 4 weeks)
    
    **Lưu ý:**
    - Đặc biệt hiệu quả với psoriasis
    - Có thể dùng nếu TNF-α không đủ
    """)
    
    st.markdown("---")
    st.markdown("### 4️⃣ Small Molecule Inhibitors")
    
    st.success("""
    **JAK Inhibitors:**
    - **Tofacitinib:** 5mg PO BID
    - **Upadacitinib:** 15mg PO QD
    
    **PDE4 Inhibitor:**
    - **Apremilast:** 30mg PO BID (sau khi tăng dần)
    
    **Lưu ý:**
    - Oral, tiện lợi hơn biologics
    - Hiệu quả tốt với viêm khớp và psoriasis
    - Cần monitoring (JAK inhibitors: CBC, LFT, lipid)
    """)
    
    st.markdown("---")
    st.markdown("### 5️⃣ Dosing Details")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.warning("""
        **DMARDs (Tiếp tục hoặc bắt đầu):**
        - **Methotrexate:** 15-20mg/tuần
        - **Sulfasalazine:** 2-3g/ngày
        - **Leflunomide:** 20mg QD
        
        **Có thể kết hợp với biologics** (đặc biệt MTX)
        """)
    
    with col2:
        st.info("""
        **NSAIDs (Nếu cần):**
        - **Naproxen:** 500mg PO BID
        - **Diclofenac:** 50mg PO TID
        
        **Corticosteroids (Ngắn hạn):**
        - **Prednisone:** 10-20mg PO QD (nếu cần)
        - **Intra-articular:** Triamcinolone 20-40mg
        """)
    
    st.markdown("---")
    st.markdown("### 6️⃣ Screening Trước Khi Dùng Biologics")
    
    st.error("""
    **Bắt buộc trước khi dùng Biologics:**
    
    **1. TB Screening:**
    - **TST (PPD)** hoặc **IGRA (QuantiFERON)**
    - **CXR:** Nếu TST/IGRA (+)
    - **Nếu có TB tiềm ẩn:** Điều trị dự phòng 9 tháng (INH)
    
    **2. HBV Screening:**
    - **HBsAg, Anti-HBc, Anti-HBs**
    - **Nếu HBsAg (+):** Điều trị kháng virus
    
    **3. HCV Screening:**
    - **Anti-HCV**
    - **Nếu (+):** Đánh giá và điều trị
    
    **4. Labs:**
    - CBC, LFT, Creatinine
    - CRP, ESR
    """)
    
    st.markdown("---")
    st.markdown("### 7️⃣ Monitoring")
    
    st.warning("""
    **Monitoring:**
    - **Disease activity:** DAS28, PASI (nếu có psoriasis)
    - **CRP, ESR:** Mỗi 3-6 tháng
    - **Joint count, function**
    - **X-ray:** Mỗi 1-2 năm (đánh giá hủy khớp)
    
    **Labs (nếu dùng Biologics/JAK inhibitors):**
    - CBC, LFT, Creatinine: Mỗi 3 tháng
    - Lipid (nếu dùng JAK inhibitors): Mỗi 3-6 tháng
    - TB symptoms: Mỗi lần khám
    
    **Side Effects:**
    - Infection (đặc biệt TB, nấm)
    - Injection site reactions
    - Allergic reactions
    - Malignancy (hiếm)
    """)
    
    st.markdown("---")
    st.markdown("### 8️⃣ Complications")
    
    st.info("""
    **Complications cần theo dõi:**
    
    **1. Hủy khớp:**
    - Tiến triển hủy khớp (pencil-in-cup)
    - Cần điều trị tích cực để ngăn chặn
    
    **2. Cardiovascular:**
    - Tăng nguy cơ bệnh tim mạch
    - Theo dõi BP, lipid, glucose
    
    **3. Metabolic syndrome:**
    - Tăng nguy cơ
    - Theo dõi và điều trị
    
    **4. Uveitis:**
    - Viêm mống mắt
    - Khám chuyên khoa mắt nếu có triệu chứng
    """)
    
    st.markdown("---")
    
    # References section
    references = get_references("Psoriatic Arthritis")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-01-15",
            show_evidence_level=True,
            show_links=True
        )

