"""
Systemic Lupus Erythematosus - Arthritis Management Protocol
EULAR 2019, EULAR 2023, ACR 2021, ACR 2023 Guidelines
SLE Arthritis (Lupus ban đỏ hệ thống - viêm khớp) Management
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """SLE Arthritis Management Protocol"""
    st.subheader("🦴 Lupus Ban Đỏ Hệ Thống - Viêm Khớp (SLE Arthritis) Protocol")
    st.caption("EULAR 2019, EULAR 2023, ACR 2021, ACR 2023 Guidelines - SLE Arthritis Management")
    
    st.info("""
    **SLE Arthritis là viêm khớp ở bệnh nhân lupus ban đỏ hệ thống**
    - **Prevalence:** 70-90% bệnh nhân SLE có viêm khớp
    - **Triệu chứng:** Đau khớp, sưng khớp, cứng khớp, thường đối xứng
    - **Pathophysiology:** Viêm mạn tính, tự miễn, ANA (+)
    - **Characteristics:** Non-erosive (không hủy khớp), Jaccoud's arthropathy
    - **Complications:** Viêm khớp mạn tính, biến dạng khớp (hiếm)
    """)
    
    st.markdown("---")
    
    # Disease activity
    activity = st.radio(
        "**Mức độ hoạt động bệnh:**",
        ["Thấp (Low Activity)", "Trung bình (Moderate Activity)", "Cao (High Activity)"],
        key="sle_activity"
    )
    
    st.markdown("---")
    
    # Systemic involvement
    systemic = st.checkbox("**Có tổn thương cơ quan khác (thận, thần kinh, máu)?**", key="sle_systemic")
    
    st.markdown("---")
    
    if "Thấp" in activity:
        render_low_activity_sle(systemic)
    elif "Trung bình" in activity:
        render_moderate_activity_sle(systemic)
    else:
        render_high_activity_sle(systemic)


def render_low_activity_sle(systemic):
    """Low Activity SLE Arthritis Protocol"""
    
    st.success("## ✅ LOW ACTIVITY SLE ARTHRITIS PROTOCOL")
    
    st.markdown("### 1️⃣ Chẩn đoán")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Clinical Features:**
        - **Viêm khớp:** Đối xứng, thường bàn tay, cổ tay, gối
        - **Đau:** Nhẹ đến trung bình
        - **Sưng:** Nhẹ, có thể không rõ
        - **Cứng khớp:** Buổi sáng <30 phút
        - **Non-erosive:** Không hủy khớp (phân biệt với RA)
        
        **Triệu chứng khác:**
        - Phát ban (butterfly rash)
        - Nhạy cảm ánh sáng
        - Mệt mỏi
        - Sốt nhẹ
        """)
    
    with col2:
        st.warning("""
        **Diagnostic:**
        - **ACR/SLICC Criteria:** ≥4 tiêu chuẩn
          * Phát ban
          * Viêm khớp
          * ANA (+)
          * Anti-dsDNA, Anti-Sm (+)
          * Tổn thương thận, thần kinh, máu
        
        **Labs:**
        - **ANA:** (+) trong 95-100%
        - **Anti-dsDNA:** (+) trong 70%
        - **Anti-Sm:** (+) trong 30% (đặc hiệu)
        - **Complement (C3, C4):** Giảm trong hoạt động bệnh
        - **CRP, ESR:** Tăng
        
        **X-ray:**
        - Bình thường hoặc viêm nhẹ
        - Không hủy khớp (phân biệt với RA)
        """)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Điều trị - First Line")
    
    st.success("""
    **Non-Pharmacological:**
    
    **1. Lifestyle:**
    - **Tránh ánh nắng:** Dùng kem chống nắng, mặc quần áo che
    - **Nghỉ ngơi:** Tránh mệt mỏi quá mức
    - **Tập luyện:** Nhẹ nhàng, tránh chấn thương
    
    **2. Vật lý trị liệu:**
    - Duy trì vận động khớp
    - Strengthening
    - Tư vấn tư thế
    """)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Điều trị - Pharmacological")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **NSAIDs (First Line):**
        - **Naproxen:** 250-500mg PO BID
        - **Ibuprofen:** 400-600mg PO TID
        - **Diclofenac:** 50mg PO TID
        - **Celecoxib:** 100-200mg PO BID
        
        **Lưu ý:**
        - Cẩn thận với bệnh nhân có tổn thương thận
        - Theo dõi chức năng thận
        """)
    
    with col2:
        st.warning("""
        **Antimalarials (Quan trọng):**
        - **Hydroxychloroquine:** 200-400mg PO QD
        - **Chloroquine:** 250mg PO QD
        - **Indication:** Tất cả bệnh nhân SLE (trừ chống chỉ định)
        - **Benefits:**
          * Giảm viêm khớp
          * Giảm flare
          * Giảm nguy cơ bệnh tim mạch
          * Giảm nguy cơ đông máu
        - **Duration:** Dùng lâu dài
        """)
    
    st.markdown("---")
    st.markdown("### 4️⃣ Monitoring")
    
    st.info("""
    **Monitoring:**
    - Đáp ứng điều trị
    - Tác dụng phụ NSAIDs (thận, GI)
    - Tác dụng phụ antimalarials (mắt: mỗi 6-12 tháng)
    
    **Labs:**
    - Creatinine, eGFR: Mỗi 3-6 tháng
    - CBC, LFT: Mỗi 6 tháng
    - ANA, Anti-dsDNA, Complement: Mỗi 6-12 tháng
    """)


def render_moderate_activity_sle(systemic):
    """Moderate Activity SLE Arthritis Protocol"""
    
    st.warning("## ⚠️ MODERATE ACTIVITY SLE ARTHRITIS PROTOCOL")
    
    st.markdown("### 1️⃣ Điều trị - Combination Therapy")
    
    st.warning("""
    **Moderate Activity:** Đau nhiều, sưng khớp, hạn chế chức năng
    
    **1. Non-Pharmacological (Tiếp tục):**
    - Lifestyle
    - Vật lý trị liệu
    
    **2. Pharmacological:**
    - **Antimalarials** (bắt buộc)
    - **NSAIDs** (nếu cần)
    - **Corticosteroids** (nếu cần, ngắn hạn)
    - **DMARDs** (nếu không đáp ứng)
    """)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Dosing Details")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("""
        **Antimalarials (Tiếp tục):**
        - **Hydroxychloroquine:** 400mg PO QD
        - **Chloroquine:** 250mg PO QD
        - **Duration:** Lâu dài
        
        **NSAIDs (Nếu cần):**
        - **Naproxen:** 500mg PO BID
        - **Ibuprofen:** 600-800mg PO TID
        - **Lưu ý:** Cẩn thận với tổn thương thận
        """)
    
    with col2:
        st.info("""
        **Corticosteroids (Ngắn hạn):**
        - **Prednisone:** 10-20mg PO QD × 2-4 tuần
        - **Taper:** Giảm dần
        - **Intra-articular:** Triamcinolone 20-40mg (nếu cần)
        
        **DMARDs (Nếu không đáp ứng):**
        - **Methotrexate:** 10-15mg PO/tuần
        - **Azathioprine:** 50-100mg PO QD
        - **Mycophenolate:** 1-2g PO BID
        """)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Monitoring")
    
    st.warning("""
    **Monitoring:**
    - Đáp ứng điều trị
    - Tác dụng phụ (NSAIDs, corticosteroids, DMARDs)
    - Tổn thương cơ quan khác (nếu có)
    
    **Labs:**
    - Creatinine, eGFR: Mỗi 3 tháng
    - CBC, LFT: Mỗi 3 tháng (nếu dùng DMARDs)
    - ANA, Anti-dsDNA, Complement: Mỗi 3-6 tháng
    - Urinalysis, proteinuria: Mỗi 3-6 tháng (nếu có tổn thương thận)
    """)


def render_high_activity_sle(systemic):
    """High Activity SLE Arthritis Protocol"""
    
    st.error("## 🚨 HIGH ACTIVITY SLE ARTHRITIS PROTOCOL")
    
    if systemic:
        st.error("""
        **⚠️ CẢNH BÁO: Có tổn thương cơ quan khác**
        
        **Cần đánh giá ngay:**
        - **Thận:** Viêm thận lupus (lupus nephritis)
        - **Thần kinh:** Viêm não, đột quỵ
        - **Máu:** Giảm tiểu cầu, thiếu máu, giảm bạch cầu
        - **Tim:** Viêm màng ngoài tim, viêm cơ tim
        
        **Điều trị:** Cần điều trị tích cực với corticosteroids + immunosuppressants
        """)
    
    st.markdown("### 1️⃣ Điều trị - Aggressive Management")
    
    st.error("""
    **High Activity:** Đau nhiều, sưng khớp nhiều, hạn chế chức năng rõ rệt
    
    **1. Non-Pharmacological (Tiếp tục):**
    - Lifestyle
    - Vật lý trị liệu
    
    **2. Pharmacological:**
    - **Antimalarials** (bắt buộc)
    - **Corticosteroids** (high dose)
    - **DMARDs/Immunosuppressants** (bắt buộc)
    - **Biologics** (nếu không đáp ứng)
    """)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Dosing Details")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.warning("""
        **Antimalarials (Tiếp tục):**
        - **Hydroxychloroquine:** 400mg PO QD
        - **Chloroquine:** 250mg PO QD
        - **Duration:** Lâu dài
        
        **Corticosteroids:**
        - **Prednisone:** 20-40mg PO QD × 2-4 tuần
        - **Taper:** Giảm 5mg mỗi 1-2 tuần
        - **Methylprednisolone:** 40-60mg IV q24h (nếu nặng, không uống được)
        - **Intra-articular:** Triamcinolone 40mg (nếu cần)
        """)
    
    with col2:
        st.info("""
        **DMARDs/Immunosuppressants:**
        - **Methotrexate:** 15-20mg PO/tuần
        - **Azathioprine:** 100-150mg PO QD (1-2mg/kg/ngày)
        - **Mycophenolate:** 2-3g/ngày
        - **Cyclophosphamide:** 500-1000mg IV q month (nếu có tổn thương thận/thần kinh nặng)
        
        **Lưu ý:**
        - Cần monitoring chặt chẽ
        - Tác dụng phụ: Nhiễm trùng, giảm bạch cầu, gan, thận
        """)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Biologics (Nếu không đáp ứng)")
    
    st.success("""
    **Belimumab (Anti-BLyS):**
    - **10 mg/kg IV q4 weeks** (loading: 0, 2, 4 weeks)
    - **Hoặc:** 200mg SC q week
    - **Indication:** SLE hoạt động, không đáp ứng với standard therapy
    - **Benefits:** Giảm flare, giảm corticosteroids
    
    **Anifrolumab (Anti-IFN-α):**
    - **300mg IV q4 weeks**
    - **Indication:** SLE hoạt động, không đáp ứng
    - **Benefits:** Giảm hoạt động bệnh
    
    **Lưu ý:**
    - Đắt tiền
    - Cần screening TB, HBV, HCV
    - Theo dõi infection
    """)
    
    st.markdown("---")
    st.markdown("### 4️⃣ Monitoring & Complications")
    
    st.warning("""
    **Monitoring:**
    - **Disease activity:** SLEDAI, BILAG
    - **CRP, ESR:** Mỗi 1-3 tháng
    - **ANA, Anti-dsDNA, Complement:** Mỗi 3 tháng
    - **Joint count, function**
    
    **Labs (nếu dùng DMARDs/Immunosuppressants):**
    - CBC: Mỗi 1-2 tuần (nếu dùng azathioprine/cyclophosphamide), sau đó mỗi 1-3 tháng
    - LFT, Creatinine: Mỗi 1-3 tháng
    - Urinalysis, proteinuria: Mỗi 1-3 tháng
    
    **Complications:**
    - **Infection:** Tăng nguy cơ (đặc biệt với immunosuppressants)
    - **Osteoporosis:** Do corticosteroids → Bổ sung calcium, vitamin D
    - **Cardiovascular:** Tăng nguy cơ → Theo dõi BP, lipid, glucose
    - **Thận:** Lupus nephritis → Theo dõi chặt chẽ
    - **Thần kinh:** Viêm não, đột quỵ → Khám thần kinh nếu có triệu chứng
    """)
    
    st.markdown("---")
    st.markdown("### 5️⃣ Special Considerations")
    
    st.info("""
    **Pregnancy:**
    - **Antimalarials:** An toàn, tiếp tục dùng
    - **Corticosteroids:** Có thể dùng (low dose)
    - **DMARDs:** Tránh (MTX, azathioprine có thể dùng nếu cần)
    - **Biologics:** Belimumab không khuyến cáo
    
    **Vaccination:**
    - **Live vaccines:** Tránh nếu đang dùng immunosuppressants
    - **Inactivated vaccines:** An toàn, khuyến cáo (flu, pneumococcal)
    - **COVID-19:** Khuyến cáo tiêm
    
    **Sun protection:**
    - Bắt buộc (tránh flare)
    - Kem chống nắng SPF ≥30
    - Mặc quần áo che
    """)
    
    st.markdown("---")
    
    # References section
    references = get_references("SLE Arthritis")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-01-15",
            show_evidence_level=True,
            show_links=True
        )

