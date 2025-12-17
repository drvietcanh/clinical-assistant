"""
Reactive Arthritis Management Protocol
ACR 2019, ACR 2021, EULAR 2016, EULAR 2023 Guidelines
Reactive Arthritis (Viêm khớp phản ứng) Management
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Reactive Arthritis Management Protocol"""
    st.subheader("🦴 Viêm Khớp Phản Ứng (Reactive Arthritis) Protocol")
    st.caption("ACR 2019, ACR 2021, EULAR 2016, EULAR 2023 Guidelines - Reactive Arthritis Management")
    
    st.info("""
    **Reactive Arthritis (ReA) là viêm khớp sau nhiễm khuẩn**
    - **Prevalence:** 0.1-1% sau nhiễm khuẩn
    - **Triệu chứng:** Viêm khớp không đối xứng, thường ở chi dưới
    - **Trigger:** Nhiễm khuẩn đường tiêu hóa, tiết niệu-sinh dục
    - **Pathophysiology:** Phản ứng miễn dịch sau nhiễm khuẩn, HLA-B27 (+)
    - **Duration:** Vài tuần đến vài tháng, có thể tái phát
    """)
    
    st.markdown("---")
    
    # Trigger selection
    trigger = st.radio(
        "**Nguyên nhân khởi phát:**",
        ["Nhiễm khuẩn đường tiêu hóa", "Nhiễm khuẩn tiết niệu-sinh dục", "Không rõ"],
        key="rea_trigger"
    )
    
    st.markdown("---")
    
    # Severity selection
    severity = st.radio(
        "**Mức độ nặng:**",
        ["Nhẹ", "Trung bình", "Nặng"],
        key="rea_severity"
    )
    
    st.markdown("---")
    
    if "Nhẹ" in severity:
        render_mild_rea(trigger)
    elif "Trung bình" in severity:
        render_moderate_rea(trigger)
    else:
        render_severe_rea(trigger)


def render_mild_rea(trigger):
    """Mild Reactive Arthritis Protocol"""
    
    st.success("## ✅ MILD REACTIVE ARTHRITIS PROTOCOL")
    
    st.markdown("### 1️⃣ Chẩn đoán")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Clinical Features:**
        - **Viêm khớp:** Không đối xứng, thường chi dưới
        - **Khớp thường gặp:** Gối, cổ chân, bàn chân
        - **Onset:** 1-4 tuần sau nhiễm khuẩn
        - **Triệu chứng khác:**
          * Viêm gân (enthesitis)
          * Viêm bao gân (dactylitis)
          * Đau lưng viêm (nếu có viêm cột sống)
        
        **Triệu chứng ngoài khớp:**
        - Viêm kết mạc
        - Viêm niệu đạo
        - Tổn thương da (keratoderma)
        """)
    
    with col2:
        st.warning("""
        **Diagnostic:**
        - **Clinical:** Viêm khớp sau nhiễm khuẩn
        - **HLA-B27:** (+) trong 50-80% trường hợp
        - **Labs:** 
          * CRP, ESR tăng
          * RF, ANA (-) (phân biệt với RA, SLE)
        - **X-ray:** Bình thường hoặc viêm nhẹ
        
        **Differential:**
        - RA (đối xứng, RF/CCP (+))
        - Gout (đau đột ngột, tinh thể)
        - Septic arthritis (sốt, cấy máu (+))
        """)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Điều trị - First Line")
    
    st.success("""
    **1. Điều trị nhiễm khuẩn (nếu còn):**
    
    **Nhiễm khuẩn đường tiêu hóa:**
    - **Ciprofloxacin:** 500mg PO BID × 7-10 ngày (nếu còn triệu chứng)
    - **Azithromycin:** 500mg PO QD × 3 ngày
    - **Lưu ý:** Không rõ lợi ích nếu nhiễm khuẩn đã hết
    
    **Nhiễm khuẩn tiết niệu-sinh dục:**
    - **Chlamydia:** Azithromycin 1g PO × 1 hoặc Doxycycline 100mg PO BID × 7 ngày
    - **Gonorrhea:** Ceftriaxone 250mg IM × 1 + Azithromycin 1g PO × 1
    """)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Điều trị - Anti-inflammatory")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **NSAIDs (First Line):**
        - **Naproxen:** 500mg PO BID × 2-4 tuần
        - **Indomethacin:** 50mg PO TID × 2-4 tuần
        - **Diclofenac:** 50mg PO TID × 2-4 tuần
        - **Ibuprofen:** 600-800mg PO TID × 2-4 tuần
        
        **PPI:** Cân nhắc nếu có GI risk
        """)
    
    with col2:
        st.warning("""
        **Corticosteroids (Nếu NSAIDs không đủ):**
        - **Prednisone:** 10-20mg PO QD × 2-4 tuần, sau đó giảm dần
        - **Intra-articular:** Triamcinolone 20-40mg (nếu mono/pauciarticular)
        
        **Lưu ý:**
        - Đa số trường hợp tự khỏi trong vài tuần đến vài tháng
        - Điều trị triệu chứng là chính
        """)


def render_moderate_rea(trigger):
    """Moderate Reactive Arthritis Protocol"""
    
    st.warning("## ⚠️ MODERATE REACTIVE ARTHRITIS PROTOCOL")
    
    st.markdown("### 1️⃣ Điều trị - Combination Therapy")
    
    st.warning("""
    **Moderate ReA:** Đau nhiều hơn, nhiều khớp, hạn chế chức năng
    
    **1. Điều trị nhiễm khuẩn (nếu còn):**
    - Như mild protocol
    
    **2. Anti-inflammatory:**
    - **NSAIDs** (full dose)
    - **Corticosteroids** (nếu cần)
    - **DMARDs** (nếu kéo dài >3 tháng)
    """)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Dosing Details")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("""
        **NSAIDs (Full Dose):**
        - **Naproxen:** 500mg PO BID
        - **Indomethacin:** 50-75mg PO TID
        - **Diclofenac:** 50mg PO TID
        - **Duration:** 4-8 tuần hoặc đến khi hết triệu chứng
        
        **PPI:** Nên dùng nếu dùng NSAIDs lâu dài
        """)
    
    with col2:
        st.info("""
        **Corticosteroids:**
        - **Prednisone:** 20-30mg PO QD × 2-4 tuần
        - **Taper:** Giảm 5mg mỗi tuần
        - **Intra-articular:** Triamcinolone 20-40mg (nếu cần)
        
        **DMARDs (Nếu kéo dài >3 tháng):**
        - **Sulfasalazine:** 1-2g PO BID (max 3g/ngày)
        - **Methotrexate:** 10-15mg PO/tuần
        """)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Supportive Care")
    
    st.info("""
    **General:**
    - **Rest:** Nghỉ ngơi khớp bị ảnh hưởng
    - **Ice/Heat:** Chườm lạnh hoặc nóng
    - **Physical therapy:** Sau khi đau giảm
    
    **Monitoring:**
    - Đáp ứng điều trị trong 2-4 tuần
    - Nếu không cải thiện: Xem xét chẩn đoán lại
    """)


def render_severe_rea(trigger):
    """Severe Reactive Arthritis Protocol"""
    
    st.error("## 🚨 SEVERE REACTIVE ARTHRITIS PROTOCOL")
    
    st.markdown("### 1️⃣ Điều trị - Aggressive Management")
    
    st.error("""
    **Severe ReA:** Đau nhiều, nhiều khớp, hạn chế chức năng rõ rệt, kéo dài
    
    **1. Điều trị nhiễm khuẩn (nếu còn):**
    - Như mild/moderate protocol
    
    **2. Anti-inflammatory:**
    - **NSAIDs** (full dose)
    - **Corticosteroids** (high dose)
    - **DMARDs** (nếu kéo dài)
    - **Biologics** (nếu không đáp ứng)
    """)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Dosing Details")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.warning("""
        **NSAIDs (Full Dose):**
        - **Naproxen:** 500mg PO BID
        - **Indomethacin:** 75mg PO TID
        - **Diclofenac:** 50mg PO TID
        
        **Corticosteroids:**
        - **Prednisone:** 30-40mg PO QD × 2-4 tuần
        - **Taper:** Giảm 5mg mỗi tuần
        - **Intra-articular:** Triamcinolone 40mg (nếu cần)
        """)
    
    with col2:
        st.info("""
        **DMARDs (Nếu kéo dài >3 tháng):**
        - **Sulfasalazine:** 2-3g/ngày
        - **Methotrexate:** 15-20mg/tuần
        - **Duration:** 3-6 tháng, đánh giá đáp ứng
        
        **Biologics (Nếu không đáp ứng với DMARDs):**
        - **TNF-α inhibitors:** Adalimumab, Etanercept
        - **Chỉ định:** ReA kéo dài, không đáp ứng với DMARDs
        """)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Monitoring & Complications")
    
    st.warning("""
    **Monitoring:**
    - Đáp ứng điều trị trong 2-4 tuần
    - CRP, ESR: Mỗi 4-8 tuần
    - Joint count, function
    
    **Complications:**
    - **Chronic ReA:** Kéo dài >6 tháng → Cần DMARDs/Biologics
    - **Recurrent:** Tái phát → Điều trị như đợt cấp
    - **Cardiac:** Hiếm (block nhĩ thất)
    - **Eye:** Viêm mống mắt → Khám chuyên khoa mắt
    
    **Labs (nếu dùng DMARDs/Biologics):**
    - CBC, LFT, Creatinine: Mỗi 1-3 tháng
    - TB screening: Trước khi dùng biologics
    """)
    
    st.markdown("---")
    st.markdown("### 4️⃣ Prognosis")
    
    st.info("""
    **Prognosis:**
    - **Acute ReA:** Đa số tự khỏi trong vài tuần đến vài tháng
    - **Chronic ReA:** 15-30% kéo dài >6 tháng
    - **Recurrent:** 15-50% tái phát
    
    **Risk factors cho chronic:**
    - HLA-B27 (+)
    - Viêm khớp nặng
    - Viêm cột sống
    - Không đáp ứng với NSAIDs
    
    **Follow-up:**
    - Tái khám sau 2-4 tuần
    - Đánh giá đáp ứng
    - Nếu không cải thiện: Xem xét DMARDs
    """)
    
    st.markdown("---")
    
    # References section
    references = get_references("Reactive Arthritis")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-01-15",
            show_evidence_level=True,
            show_links=True
        )

