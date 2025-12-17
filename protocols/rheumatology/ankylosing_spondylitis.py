"""
Ankylosing Spondylitis Management Protocol
ASAS 2016, ASAS 2022, ACR 2019, ACR 2021 Guidelines
Ankylosing Spondylitis (Viêm cột sống dính khớp) Management
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Ankylosing Spondylitis Management Protocol"""
    st.subheader("🦴 Viêm Cột Sống Dính Khớp (Ankylosing Spondylitis) Protocol")
    st.caption("ASAS 2016, ASAS 2022, ACR 2019, ACR 2021 Guidelines - AS Management")
    
    st.info("""
    **Ankylosing Spondylitis (AS) là bệnh viêm khớp cột sống mạn tính**
    - **Prevalence:** 0.1-0.5% dân số, nam > nữ (3:1)
    - **Triệu chứng:** Đau lưng viêm, cứng khớp buổi sáng, hạn chế vận động
    - **Pathophysiology:** Viêm khớp cùng-chậu, cột sống, HLA-B27 (+)
    - **Complications:** Dính khớp, gù lưng, viêm mống mắt, bệnh tim
    """)
    
    st.markdown("---")
    
    # Disease activity
    activity = st.radio(
        "**Mức độ hoạt động bệnh:**",
        ["Thấp (Low Activity)", "Trung bình (Moderate Activity)", "Cao (High Activity)"],
        key="as_activity"
    )
    
    st.markdown("---")
    
    if "Thấp" in activity:
        render_low_activity_as()
    elif "Trung bình" in activity:
        render_moderate_activity_as()
    else:
        render_high_activity_as()


def render_low_activity_as():
    """Low Activity AS Protocol"""
    
    st.success("## ✅ LOW ACTIVITY AS PROTOCOL")
    
    st.markdown("### 1️⃣ Chẩn đoán")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Clinical Features:**
        - **Đau lưng viêm:** Đau lưng dưới, khởi phát <40 tuổi
        - **Onset:** Từ từ, >3 tháng
        - **Cải thiện:** Vận động, không cải thiện khi nghỉ
        - **Cứng khớp:** Buổi sáng >30 phút
        - **HLA-B27:** (+) trong 80-90% trường hợp
        
        **Khám:**
        - Hạn chế vận động cột sống
        - Schober test (+)
        - Chest expansion giảm
        """)
    
    with col2:
        st.warning("""
        **Diagnostic:**
        - **Modified NY Criteria:** Đau lưng viêm + ≥1 trong:
          * HLA-B27 (+)
          * Viêm khớp cùng-chậu trên X-ray/MRI
          * Đáp ứng với NSAIDs
          * Tiền sử gia đình AS
        
        **X-ray:**
        - Khớp cùng-chậu: Hẹp, mờ, dính
        - Cột sống: Syndesmophytes, "bamboo spine"
        
        **MRI:**
        - Viêm khớp cùng-chậu sớm (trước khi X-ray thấy)
        """)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Điều trị - First Line")
    
    st.success("""
    **Non-Pharmacological (Quan trọng):**
    
    **1. Tập luyện:**
    - **Stretching:** Duy trì vận động cột sống
    - **Strengthening:** Cơ lưng, cơ bụng
    - **Posture:** Tư thế đúng, tránh gù
    - **Frequency:** Hàng ngày, 30-60 phút
    
    **2. Vật lý trị liệu:**
    - Tư vấn tư thế
    - Tập luyện chuyên biệt
    - Dụng cụ hỗ trợ (nếu cần)
    
    **3. Lifestyle:**
    - Tránh hút thuốc (tăng tiến triển)
    - Nằm nệm cứng
    - Tránh gối cao
    """)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Điều trị - Pharmacological")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **NSAIDs (First Line):**
        - **Naproxen:** 500mg PO BID
        - **Indomethacin:** 50-75mg PO BID-TID
        - **Diclofenac:** 50mg PO TID
        - **Celecoxib:** 200mg PO BID
        
        **Lưu ý:**
        - Dùng liên tục (không chỉ khi đau)
        - Đáp ứng tốt với NSAIDs là đặc trưng của AS
        - Nếu đáp ứng: Tiếp tục dùng lâu dài
        """)
    
    with col2:
        st.warning("""
        **Contraindications:**
        - CKD (CrCl <30)
        - GI bleeding risk
        - Heart failure
        - Active peptic ulcer
        
        **PPI:** Cân nhắc nếu dùng NSAIDs lâu dài
        
        **Monitoring:**
        - Creatinine, eGFR: Mỗi 3-6 tháng
        - CBC: Mỗi 6 tháng
        """)


def render_moderate_activity_as():
    """Moderate Activity AS Protocol"""
    
    st.warning("## ⚠️ MODERATE ACTIVITY AS PROTOCOL")
    
    st.markdown("### 1️⃣ Điều trị - Combination Therapy")
    
    st.warning("""
    **Moderate Activity:** Đau nhiều hơn, hạn chế chức năng
    
    **1. Non-Pharmacological (Tiếp tục):**
    - Tập luyện tích cực hơn
    - Vật lý trị liệu
    - Tư thế, lifestyle
    
    **2. Pharmacological:**
    - **NSAIDs** (full dose, liên tục)
    - **DMARDs** (nếu có viêm khớp ngoại vi)
    - **Corticosteroids** (nếu cần, ngắn hạn)
    """)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Dosing Details")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("""
        **NSAIDs (Full Dose):**
        - **Naproxen:** 500mg PO BID
        - **Indomethacin:** 75mg PO BID-TID
        - **Diclofenac:** 50mg PO TID
        - **Celecoxib:** 200mg PO BID
        
        **PPI:** Nên dùng nếu dùng NSAIDs lâu dài
        """)
    
    with col2:
        st.info("""
        **DMARDs (Nếu có viêm khớp ngoại vi):**
        - **Sulfasalazine:** 1-2g PO BID (max 3g/ngày)
        - **Methotrexate:** 10-15mg PO/tuần (nếu SSZ không đủ)
        - **Lưu ý:** DMARDs không hiệu quả cho đau lưng/viêm khớp cùng-chậu
        
        **Corticosteroids (Ngắn hạn):**
        - **Prednisone:** 10-20mg PO QD × 2-4 tuần
        - **Taper:** Giảm dần
        """)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Intra-articular Injection")
    
    st.warning("""
    **Corticosteroid Injection:**
    - **Khớp cùng-chậu:** Triamcinolone 40-60mg (mỗi bên)
    - **Khớp ngoại vi:** Triamcinolone 10-40mg (tùy khớp)
    - **Frequency:** Mỗi 3-6 tháng (nếu cần)
    - **Indication:** Đau khu trú, không đáp ứng với thuốc uống
    """)


def render_high_activity_as():
    """High Activity AS Protocol"""
    
    st.error("## 🚨 HIGH ACTIVITY AS PROTOCOL")
    
    st.markdown("### 1️⃣ Điều trị - Aggressive Management")
    
    st.error("""
    **High Activity:** Đau nhiều, hạn chế chức năng rõ rệt, không đáp ứng với NSAIDs
    
    **1. Non-Pharmacological (Tiếp tục):**
    - Tập luyện tích cực
    - Vật lý trị liệu
    - Tư thế, lifestyle
    
    **2. Pharmacological:**
    - **NSAIDs** (full dose, liên tục)
    - **Biologics (TNF-α inhibitors)** - Chỉ định chính
    - **DMARDs** (nếu có viêm khớp ngoại vi)
    """)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Biologics - TNF-α Inhibitors")
    
    st.warning("""
    **Chỉ định cho Biologics:**
    - Đau lưng viêm nhiều, không đáp ứng với ≥2 NSAIDs (mỗi loại ≥2 tuần)
    - BASDAI ≥4 (hoặc đánh giá lâm sàng tương đương)
    - CRP tăng hoặc MRI thấy viêm hoạt động
    
    **Options:**
    
    **TNF-α Inhibitors:**
    - **Adalimumab:** 40mg SC q2 weeks
    - **Etanercept:** 50mg SC q week
    - **Infliximab:** 5 mg/kg IV q8 weeks
    - **Golimumab:** 50mg SC q month
    - **Certolizumab:** 200mg SC q2 weeks
    
    **Lưu ý:**
    - Hiệu quả tốt với đau lưng viêm, viêm khớp cùng-chậu
    - Đáp ứng trong 2-4 tuần
    - Cần screening TB, HBV, HCV trước khi dùng
    """)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Dosing Details")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("""
        **NSAIDs (Tiếp tục):**
        - **Naproxen:** 500mg PO BID
        - **Indomethacin:** 75mg PO BID-TID
        - **Diclofenac:** 50mg PO TID
        
        **Có thể giảm liều NSAIDs** sau khi biologics có hiệu quả
        """)
    
    with col2:
        st.info("""
        **DMARDs (Nếu có viêm khớp ngoại vi):**
        - **Sulfasalazine:** 2-3g/ngày
        - **Methotrexate:** 15-20mg/tuần
        - **Lưu ý:** Không hiệu quả cho đau lưng/viêm khớp cùng-chậu
        """)
    
    st.markdown("---")
    st.markdown("### 4️⃣ Screening Trước Khi Dùng Biologics")
    
    st.error("""
    **Bắt buộc trước khi dùng Biologics:**
    
    **1. TB Screening:**
    - **TST (PPD)** hoặc **IGRA (QuantiFERON)**
    - **CXR:** Nếu TST/IGRA (+)
    - **Nếu có TB tiềm ẩn:** Điều trị dự phòng 9 tháng (INH) trước khi dùng biologics
    
    **2. HBV Screening:**
    - **HBsAg, Anti-HBc, Anti-HBs**
    - **Nếu HBsAg (+):** Điều trị kháng virus (entecavir/tenofovir) trước và trong khi dùng biologics
    
    **3. HCV Screening:**
    - **Anti-HCV**
    - **Nếu (+):** Đánh giá và điều trị nếu cần
    
    **4. Labs:**
    - CBC, LFT, Creatinine
    - CRP, ESR
    """)
    
    st.markdown("---")
    st.markdown("### 5️⃣ Monitoring")
    
    st.warning("""
    **Monitoring:**
    - **BASDAI:** Mỗi 3-6 tháng (đánh giá đáp ứng)
    - **CRP, ESR:** Mỗi 3-6 tháng
    - **Function:** BASFI (Bath Ankylosing Spondylitis Functional Index)
    - **X-ray/MRI:** Mỗi 1-2 năm (đánh giá tiến triển)
    
    **Labs (nếu dùng Biologics):**
    - CBC, LFT, Creatinine: Mỗi 3 tháng
    - TB symptoms: Mỗi lần khám
    
    **Side Effects (Biologics):**
    - Infection (đặc biệt TB, nấm)
    - Injection site reactions
    - Allergic reactions
    - Malignancy (hiếm)
    """)
    
    st.markdown("---")
    st.markdown("### 6️⃣ Complications")
    
    st.info("""
    **Complications cần theo dõi:**
    
    **1. Uveitis (Viêm mống mắt):**
    - Triệu chứng: Đau mắt, đỏ mắt, nhạy cảm ánh sáng
    - Điều trị: Corticosteroid nhỏ mắt, khám chuyên khoa mắt
    
    **2. Cardiovascular:**
    - Tăng nguy cơ bệnh tim mạch
    - Theo dõi BP, lipid, glucose
    
    **3. Osteoporosis:**
    - Tăng nguy cơ loãng xương
    - DEXA scan: Mỗi 2 năm
    - Bổ sung calcium, vitamin D
    
    **4. Dính khớp:**
    - Tiến triển dính khớp (bamboo spine)
    - Tập luyện để duy trì vận động
    """)
    
    st.markdown("---")
    
    # References section
    references = get_references("Ankylosing Spondylitis")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-01-15",
            show_evidence_level=True,
            show_links=True
        )

