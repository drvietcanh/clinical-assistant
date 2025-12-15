"""
Acute Gout Management Protocol
ACR 2020, EULAR 2016 Guidelines
Acute Gout Attack Management
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Acute Gout Management Protocol"""
    st.subheader("🦴 Acute Gout Management Protocol")
    st.caption("ACR 2020, EULAR 2016 - Acute Gout Attack Management")
    
    st.info("""
    **Gout là bệnh viêm khớp do lắng đọng tinh thể monosodium urate (MSU)**
    - **Prevalence:** 3-4% dân số
    - **Acute attack:** Đau dữ dội, khởi phát đột ngột, thường ở khớp bàn chân (podagra)
    - **Duration:** 7-14 ngày nếu không điều trị
    """)
    
    st.markdown("---")
    
    # Severity selection
    severity = st.radio(
        "**Mức độ nặng:**",
        ["Nhẹ (1-3 khớp)", "Trung bình (1-3 khớp, đau nhiều)", "Nặng (≥4 khớp hoặc polyarticular)", "Chưa xác định"],
        key="gout_severity"
    )
    
    st.markdown("---")
    
    if "Nhẹ" in severity:
        render_mild_gout()
    elif "Trung bình" in severity:
        render_moderate_gout()
    elif "Nặng" in severity:
        render_severe_gout()
    else:
        render_unknown_gout()


def render_mild_gout():
    """Mild Gout Attack Protocol"""
    
    st.warning("## ⚠️ MILD GOUT ATTACK PROTOCOL")
    
    st.markdown("### 1️⃣ Chẩn đoán")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Clinical Features:**
        - **Podagra:** Đau khớp bàn chân (MTP1) - classic
        - **Onset:** Đột ngột, thường đêm
        - **Duration:** 7-14 ngày nếu không điều trị
        - **Erythema, swelling, warmth**
        - **Tender to touch**
        
        **Other joints:**
        - Ankle, knee
        - Wrist, elbow
        - Rarely: Shoulder, hip
        """)
    
    with col2:
        st.warning("""
        **Diagnostic:**
        - **Clinical diagnosis:** Classic presentation
        - **Synovial fluid:** MSU crystals (definitive)
        - **Serum uric acid:** Thường ↑ nhưng có thể bình thường trong cơn cấp
        - **X-ray:** Tophi, erosions (chronic)
        
        **Differential:**
        - Pseudogout (calcium pyrophosphate)
        - Septic arthritis
        - Reactive arthritis
        """)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Điều trị - First Line")
    
    st.success("""
    **NSAIDs (Non-Steroidal Anti-Inflammatory Drugs):**
    
    **Options:**
    - **Naproxen:** 500mg PO BID × 7-10 ngày
    - **Indomethacin:** 50mg PO TID × 7-10 ngày
    - **Ibuprofen:** 600-800mg PO TID × 7-10 ngày
    - **Celecoxib:** 200mg PO BID × 7-10 ngày (nếu có GI risk)
    
    **Contraindications:**
    - ⚠️ CKD (CrCl <30)
    - ⚠️ GI bleeding risk
    - ⚠️ Heart failure
    - ⚠️ Active peptic ulcer
    
    **PPI:** Cân nhắc nếu có GI risk
    """)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Điều trị - Alternative")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Colchicine:**
        - **Loading:** 1.2mg PO × 1
        - **Then:** 0.6mg PO q1h (max 1.8mg total)
        - **Hoặc:** 0.6mg PO BID × 7-10 ngày (low-dose)
        - **Contraindications:**
          * CrCl <30
          * Strong CYP3A4/P-gp inhibitors
          * Severe hepatic impairment
        
        **Lưu ý:** Low-dose colchicine (0.6mg BID) hiệu quả tương đương high-dose nhưng ít tác dụng phụ hơn
        """)
    
    with col2:
        st.warning("""
        **Corticosteroids:**
        - **Prednisone:** 30-40mg PO QD × 5-7 ngày, sau đó giảm dần
        - **Hoặc:** Methylprednisolone 4mg PO TID × 5-7 ngày
        - **Indication:** Nếu chống chỉ định NSAIDs/colchicine
        
        **Intra-articular:**
        - **Triamcinolone:** 10-40mg (tùy khớp)
        - Nếu monoarticular, có thể tiêm
        """)
    
    st.markdown("---")
    st.markdown("### 4️⃣ Supportive Care")
    
    st.info("""
    **General:**
    - **Rest:** Nâng cao chi, tránh vận động
    - **Ice:** Chườm lạnh 15-20 phút mỗi 2-3 giờ
    - **Hydration:** Uống nhiều nước
    - **Avoid:** Alcohol, purine-rich foods (tạm thời)
    
    **Pain:**
    - Acetaminophen nếu cần (không giảm viêm nhưng giảm đau)
    """)
    
    st.markdown("---")
    st.markdown("### 5️⃣ Urate-Lowering Therapy (ULT)")
    
    st.warning("""
    **⚠️ QUAN TRỌNG:**
    - **KHÔNG bắt đầu ULT trong cơn cấp**
    - **Chờ cơn cấp hết** (thường 1-2 tuần) trước khi bắt đầu
    - **Nếu đang dùng ULT:** Tiếp tục, không dừng
    
    **Indications cho ULT:**
    - ≥2 cơn gout/năm
    - Tophi
    - Gouty arthritis (chronic)
    - Uric acid >8 mg/dL với symptoms
    """)
    
    st.markdown("---")
    st.markdown("### 6️⃣ Follow-up")
    
    st.success("""
    **Timeline:**
    - Cải thiện trong 24-48h với điều trị
    - Hết hoàn toàn trong 7-14 ngày
    - **Nếu không cải thiện:** Xem xét chẩn đoán lại (septic arthritis?)
    
    **Sau khi hết cơn:**
    - Đánh giá chỉ định ULT
    - Lifestyle modifications
    - Theo dõi uric acid
    """)


def render_moderate_gout():
    """Moderate Gout Attack Protocol"""
    
    st.error("## 🚨 MODERATE GOUT ATTACK PROTOCOL")
    
    st.markdown("### 1️⃣ Điều trị - Combination Therapy")
    
    st.warning("""
    **Moderate attack:** Có thể cần combination therapy
    
    **Option 1: NSAID + Colchicine**
    - **Naproxen:** 500mg PO BID
    - **+ Colchicine:** 0.6mg PO BID (low-dose)
    - **Duration:** 7-10 ngày
    
    **Option 2: Corticosteroid + Colchicine**
    - **Prednisone:** 30-40mg PO QD
    - **+ Colchicine:** 0.6mg PO BID
    - **Duration:** 5-7 ngày, sau đó giảm dần prednisone
    
    **Option 3: NSAID + Corticosteroid**
    - Nếu đau nhiều, có thể kết hợp
    - **Lưu ý:** Tăng nguy cơ GI bleeding
    """)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Dosing Details")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("""
        **NSAIDs:**
        - **Naproxen:** 500mg PO BID (max 1000mg/day)
        - **Indomethacin:** 50mg PO TID (max 200mg/day)
        - **Ibuprofen:** 600-800mg PO TID (max 2400mg/day)
        - **Duration:** 7-10 ngày
        
        **PPI:** Nên dùng nếu có GI risk
        """)
    
    with col2:
        st.info("""
        **Colchicine (Low-Dose):**
        - **0.6mg PO BID** × 7-10 ngày
        - **Hiệu quả:** Tương đương high-dose
        - **Tác dụng phụ:** Ít hơn nhiều
        
        **Corticosteroids:**
        - **Prednisone:** 30-40mg PO QD × 5-7 ngày
        - **Taper:** Giảm 5-10mg mỗi 2-3 ngày
        - **Total duration:** 10-14 ngày
        """)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Supportive Care (Tương Tự Mild)")
    
    st.info("""
    - Rest, ice, elevation
    - Hydration
    - Avoid triggers
    - Pain management
    """)
    
    st.markdown("---")
    st.markdown("### 4️⃣ Monitoring")
    
    st.warning("""
    **Theo dõi:**
    - Đáp ứng điều trị trong 24-48h
    - Tác dụng phụ (GI, renal)
    - Nếu không cải thiện: Xem xét chẩn đoán lại
    
    **Labs:**
    - Uric acid (sau khi hết cơn)
    - Renal function (nếu dùng NSAIDs/colchicine)
    """)


def render_severe_gout():
    """Severe Gout Attack Protocol"""
    
    st.error("## 🚨🚨 SEVERE GOUT ATTACK PROTOCOL")
    
    st.markdown("### 1️⃣ Điều trị - Aggressive Combination")
    
    st.error("""
    **Severe attack (≥4 khớp hoặc polyarticular):**
    
    **Option 1: Corticosteroid + Colchicine**
    - **Prednisone:** 40-60mg PO QD × 5-7 ngày
    - **+ Colchicine:** 0.6mg PO BID
    - **Taper:** Giảm dần prednisone trong 10-14 ngày
    
    **Option 2: IV Corticosteroid (nếu không uống được)**
    - **Methylprednisolone:** 40-60mg IV q24h × 3-5 ngày
    - **+ Colchicine:** 0.6mg PO BID (nếu có thể)
    
    **Option 3: IL-1 Inhibitor (nếu refractory)**
    - **Anakinra:** 100mg SC q24h × 3 ngày
    - **Hoặc Canakinumab:** 150mg SC × 1 liều
    - **Chỉ dùng nếu:** Không đáp ứng với standard therapy
    """)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Dosing Details")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.warning("""
        **High-Dose Corticosteroids:**
        - **Prednisone:** 40-60mg PO QD
        - **Duration:** 5-7 ngày
        - **Taper:** 
          * Day 8-10: 30mg QD
          * Day 11-13: 20mg QD
          * Day 14-16: 10mg QD
          * Stop
        
        **Lưu ý:**
        - Theo dõi glucose (diabetes)
        - Theo dõi BP
        - GI protection (PPI)
        """)
    
    with col2:
        st.info("""
        **Colchicine:**
        - **0.6mg PO BID** (low-dose, an toàn hơn)
        - **Duration:** 7-10 ngày
        - **Contraindications:**
          * CrCl <30
          * Strong CYP3A4 inhibitors
          * Severe hepatic impairment
        
        **IL-1 Inhibitors:**
        - **Anakinra:** 100mg SC q24h × 3 ngày
        - **Canakinumab:** 150mg SC × 1 liều
        - **Expensive, chỉ dùng nếu refractory**
        """)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Supportive Care")
    
    st.success("""
    - **Rest:** Nghỉ ngơi, tránh vận động
    - **Ice:** Chườm lạnh các khớp
    - **Elevation:** Nâng cao chi
    - **Hydration:** Uống nhiều nước
    - **Pain:** Acetaminophen nếu cần
    """)
    
    st.markdown("---")
    st.markdown("### 4️⃣ Monitoring & Complications")
    
    st.warning("""
    **Monitoring:**
    - Đáp ứng điều trị trong 24-48h
    - Tác dụng phụ (steroids, colchicine)
    - Glucose, BP (nếu dùng steroids)
    - Renal function
    
    **Complications:**
    - **Refractory:** Không đáp ứng → Xem xét IL-1 inhibitor
    - **Infection:** Loại trừ septic arthritis
    - **Chronic tophaceous:** Cần ULT sau khi hết cơn
    """)
    
    st.markdown("---")
    st.markdown("### 5️⃣ Urate-Lowering Therapy")
    
    st.info("""
    **Sau khi hết cơn (1-2 tuần):**
    
    **Indications:**
    - ≥2 cơn/năm
    - Tophi
    - Chronic gouty arthritis
    - Uric acid >8 mg/dL
    
    **Options:**
    - **Allopurinol:** 100mg PO QD, tăng dần đến mục tiêu uric acid <6 mg/dL
    - **Febuxostat:** 40mg PO QD, tăng đến 80mg nếu cần
    - **Probenecid:** Nếu under-excretor
    - **Pegloticase:** Nếu refractory
    
    **⚠️ Lưu ý:** Bắt đầu ULT với colchicine prophylaxis (0.6mg BID) để tránh flare
    """)


def render_unknown_gout():
    """Protocol when severity unknown"""
    
    st.warning("## ⚠️ CHƯA XÁC ĐỊNH MỨC ĐỘ GOUT")
    
    st.error("""
    **Đánh giá ngay:**
    
    1. ✅ **Clinical features:** Podagra? Onset đột ngột? Erythema, swelling?
    2. ✅ **Number of joints:** Monoarticular vs polyarticular?
    3. ✅ **Severity of pain:** Nhẹ, trung bình, nặng?
    4. ✅ **Synovial fluid:** Nếu có thể (MSU crystals)
    5. ✅ **Serum uric acid:** (có thể bình thường trong cơn)
    6. ✅ **Differential:** Septic arthritis? Pseudogout?
    
    **Điều trị empiric:**
    - **NSAID:** Naproxen 500mg BID (nếu không chống chỉ định)
    - **Hoặc Colchicine:** 0.6mg BID (low-dose)
    - **Hoặc Prednisone:** 30-40mg QD (nếu chống chỉ định NSAIDs)
    
    **Timeline:**
    - Đánh giá trong 1h
    - Bắt đầu điều trị ngay
    - Điều chỉnh theo đáp ứng
    """)
    
    st.markdown("---")
    
    # References section
    references = get_references("Acute Gout")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-01-15",
            show_evidence_level=True,
            show_links=True
        )

