"""
Osteoarthritis Management Protocol
ACR 2019, OARSI 2019, OARSI 2023 Guidelines
Osteoarthritis (Viêm khớp thoái hóa) Management
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Osteoarthritis Management Protocol"""
    st.subheader("🦴 Viêm Khớp Thoái Hóa (Osteoarthritis) Protocol")
    st.caption("ACR 2019, OARSI 2019, OARSI 2023 Guidelines - Osteoarthritis Management")
    
    st.info("""
    **Osteoarthritis (OA) là bệnh khớp phổ biến nhất tại Việt Nam**
    - **Prevalence:** 10-15% dân số, tăng theo tuổi
    - **Triệu chứng:** Đau khớp, cứng khớp, giảm vận động
    - **Khớp thường gặp:** Gối, háng, cột sống, bàn tay
    - **Pathophysiology:** Thoái hóa sụn khớp, viêm mức độ thấp
    """)
    
    st.markdown("---")
    
    # Joint selection
    affected_joint = st.radio(
        "**Khớp bị ảnh hưởng:**",
        ["Gối (Knee)", "Háng (Hip)", "Bàn tay (Hand)", "Cột sống (Spine)", "Khác"],
        key="oa_joint"
    )
    
    st.markdown("---")
    
    # Severity selection
    severity = st.radio(
        "**Mức độ nặng:**",
        ["Nhẹ", "Trung bình", "Nặng"],
        key="oa_severity"
    )
    
    st.markdown("---")
    
    if "Nhẹ" in severity:
        render_mild_oa(affected_joint)
    elif "Trung bình" in severity:
        render_moderate_oa(affected_joint)
    else:
        render_severe_oa(affected_joint)


def render_mild_oa(joint):
    """Mild Osteoarthritis Protocol"""
    
    st.success("## ✅ MILD OSTEOARTHRITIS PROTOCOL")
    
    st.markdown("### 1️⃣ Chẩn đoán")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Clinical Features:**
        - **Đau:** Nhẹ, tăng khi vận động, giảm khi nghỉ
        - **Cứng khớp:** <30 phút buổi sáng
        - **Vận động:** Hạn chế nhẹ
        - **X-ray:** Hẹp khe khớp nhẹ, gai xương nhỏ
        
        **Khớp gối:**
        - Đau khi leo cầu thang
        - Crepitus
        - Sưng nhẹ (effusion)
        """)
    
    with col2:
        st.warning("""
        **Diagnostic:**
        - **Clinical:** Dựa trên triệu chứng + X-ray
        - **X-ray:** Kellgren-Lawrence grade 1-2
        - **Labs:** Bình thường (không cần thiết)
        
        **Differential:**
        - RA (nếu đau đối xứng, sưng nhiều)
        - Gout (nếu đau đột ngột)
        - Septic arthritis (nếu sốt, sưng nóng đỏ)
        """)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Điều trị - First Line")
    
    st.success("""
    **Non-Pharmacological (Ưu tiên):**
    
    **1. Giảm cân:**
    - Giảm 5-10% trọng lượng → giảm 50% đau
    - Đặc biệt quan trọng với khớp gối, háng
    
    **2. Tập luyện:**
    - **Aerobic:** Đi bộ, bơi, đạp xe (30 phút/ngày, 5 ngày/tuần)
    - **Strengthening:** Tăng cường cơ quanh khớp
    - **Range of motion:** Duy trì vận động khớp
    
    **3. Vật lý trị liệu:**
    - Tư vấn tư thế, cách vận động
    - Dụng cụ hỗ trợ (gậy, nẹp)
    """)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Điều trị - Pharmacological")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Topical NSAIDs (Ưu tiên):**
        - **Diclofenac gel:** 1% BID-TID
        - **Ketoprofen gel:** 2.5% BID-TID
        - **Hiệu quả:** Tốt cho khớp gối, bàn tay
        - **An toàn:** Ít tác dụng phụ toàn thân
        
        **Acetaminophen:**
        - **500-1000mg PO QID** (max 3-4g/ngày)
        - **Indication:** Đau nhẹ
        - **Lưu ý:** Tránh quá liều (gan)
        """)
    
    with col2:
        st.warning("""
        **Oral NSAIDs (nếu topical không đủ):**
        - **Naproxen:** 250-500mg PO BID
        - **Ibuprofen:** 400-600mg PO TID
        - **Celecoxib:** 100-200mg PO BID (nếu có GI risk)
        
        **Contraindications:**
        - CKD (CrCl <30)
        - GI bleeding risk
        - Heart failure
        - Active peptic ulcer
        
        **PPI:** Cân nhắc nếu dùng NSAIDs lâu dài
        """)
    
    st.markdown("---")
    st.markdown("### 4️⃣ Intra-articular Injection")
    
    st.info("""
    **Corticosteroid Injection:**
    - **Triamcinolone:** 20-40mg (khớp gối), 10-20mg (khớp nhỏ)
    - **Methylprednisolone:** 40-80mg (khớp gối)
    - **Frequency:** Không quá 3-4 lần/năm
    - **Indication:** Đau cấp tính, không đáp ứng với thuốc uống
    
    **Hyaluronic Acid (Viscosupplementation):**
    - **Khớp gối:** 3-5 mũi tiêm (mỗi tuần 1 mũi)
    - **Hiệu quả:** Trung bình, có thể kéo dài 6 tháng
    - **Cost:** Đắt, cân nhắc cost-effectiveness
    """)


def render_moderate_oa(joint):
    """Moderate Osteoarthritis Protocol"""
    
    st.warning("## ⚠️ MODERATE OSTEOARTHRITIS PROTOCOL")
    
    st.markdown("### 1️⃣ Điều trị - Combination Therapy")
    
    st.warning("""
    **Moderate OA:** Cần kết hợp nhiều phương pháp
    
    **1. Non-Pharmacological (Tiếp tục):**
    - Giảm cân (nếu thừa cân)
    - Tập luyện (aerobic + strengthening)
    - Vật lý trị liệu
    - Dụng cụ hỗ trợ
    
    **2. Pharmacological:**
    - **Topical NSAIDs** + **Oral NSAIDs** (nếu cần)
    - **Hoặc:** Acetaminophen + NSAIDs
    """)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Dosing Details")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("""
        **NSAIDs:**
        - **Naproxen:** 500mg PO BID (max 1000mg/ngày)
        - **Ibuprofen:** 600-800mg PO TID (max 2400mg/ngày)
        - **Diclofenac:** 50mg PO TID (max 150mg/ngày)
        - **Celecoxib:** 200mg PO BID (nếu có GI risk)
        
        **PPI:** Nên dùng nếu dùng NSAIDs lâu dài
        """)
    
    with col2:
        st.info("""
        **Duloxetine (SNRI):**
        - **30-60mg PO QD**
        - **Indication:** Đau mạn tính, đặc biệt khớp gối
        - **Mechanism:** Giảm đau trung ương
        - **Side effects:** Buồn nôn, chóng mặt (thường tự hết)
        """)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Intra-articular Injection")
    
    st.warning("""
    **Corticosteroid Injection:**
    - **Triamcinolone:** 40mg (khớp gối), 20-30mg (khớp háng)
    - **Frequency:** Mỗi 3-4 tháng (không quá 4 lần/năm)
    - **Indication:** Đau cấp tính, flare
    
    **Hyaluronic Acid:**
    - **Khớp gối:** Cân nhắc nếu không đáp ứng với steroid
    - **3-5 mũi tiêm** (mỗi tuần 1 mũi)
    """)
    
    st.markdown("---")
    st.markdown("### 4️⃣ Monitoring")
    
    st.info("""
    **Theo dõi:**
    - Đáp ứng điều trị (giảm đau, cải thiện chức năng)
    - Tác dụng phụ NSAIDs (GI, renal)
    - X-ray: Mỗi 1-2 năm (nếu cần)
    
    **Labs:**
    - Creatinine, eGFR: Mỗi 3-6 tháng (nếu dùng NSAIDs)
    - CBC: Nếu dùng NSAIDs lâu dài
    """)


def render_severe_oa(joint):
    """Severe Osteoarthritis Protocol"""
    
    st.error("## 🚨 SEVERE OSTEOARTHRITIS PROTOCOL")
    
    st.markdown("### 1️⃣ Điều trị - Aggressive Management")
    
    st.error("""
    **Severe OA:** Đau nhiều, hạn chế chức năng rõ rệt
    
    **1. Non-Pharmacological (Tiếp tục):**
    - Tất cả các biện pháp như moderate
    - Tăng cường vật lý trị liệu
    - Dụng cụ hỗ trợ (gậy, nẹp, giày chỉnh hình)
    
    **2. Pharmacological:**
    - **NSAIDs** (nếu không chống chỉ định)
    - **Duloxetine** (nếu đau mạn tính)
    - **Opioids** (nếu cần, ngắn hạn)
    """)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Dosing Details")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.warning("""
        **NSAIDs (Full Dose):**
        - **Naproxen:** 500mg PO BID
        - **Ibuprofen:** 800mg PO TID
        - **Diclofenac:** 50mg PO TID
        - **Celecoxib:** 200mg PO BID
        
        **PPI:** Bắt buộc nếu dùng NSAIDs lâu dài
        
        **Duloxetine:**
        - **60mg PO QD**
        - Có thể kết hợp với NSAIDs
        """)
    
    with col2:
        st.info("""
        **Opioids (Nếu cần, ngắn hạn):**
        - **Tramadol:** 50-100mg PO QID (max 400mg/ngày)
        - **Codeine:** 30-60mg PO QID
        - **Lưu ý:** 
          * Chỉ dùng ngắn hạn
          * Theo dõi tác dụng phụ
          * Tránh lạm dụng
        """)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Intra-articular Injection")
    
    st.success("""
    **Corticosteroid Injection:**
    - **Triamcinolone:** 40-60mg (khớp gối), 40mg (khớp háng)
    - **Frequency:** Mỗi 3 tháng (không quá 4 lần/năm)
    - **Indication:** Đau cấp tính, flare
    
    **Hyaluronic Acid:**
    - **Khớp gối:** Cân nhắc nếu không đáp ứng
    - **3-5 mũi tiêm**
    """)
    
    st.markdown("---")
    st.markdown("### 4️⃣ Surgical Referral")
    
    st.error("""
    **Chỉ định phẫu thuật:**
    
    **Khớp gối/Háng:**
    - Đau nhiều, không đáp ứng với điều trị nội khoa
    - Hạn chế chức năng rõ rệt (không đi lại được)
    - X-ray: Kellgren-Lawrence grade 3-4
    - **Total Joint Replacement:** Cân nhắc nếu:
      * Tuổi >50-60
      * Không có chống chỉ định phẫu thuật
      * Bệnh nhân đồng ý
    
    **Timing:**
    - Không nên trì hoãn quá lâu (cơ yếu, khó phục hồi)
    - Cân nhắc sớm nếu đau nhiều, hạn chế chức năng
    """)
    
    st.markdown("---")
    st.markdown("### 5️⃣ Monitoring & Follow-up")
    
    st.warning("""
    **Monitoring:**
    - Đáp ứng điều trị (VAS pain score, function)
    - Tác dụng phụ (NSAIDs, opioids)
    - X-ray: Mỗi 1-2 năm
    
    **Labs:**
    - Creatinine, eGFR: Mỗi 3 tháng (nếu dùng NSAIDs)
    - CBC, LFT: Mỗi 6 tháng (nếu dùng NSAIDs lâu dài)
    
    **Follow-up:**
    - Tái khám mỗi 3-6 tháng
    - Đánh giá chỉ định phẫu thuật
    """)
    
    st.markdown("---")
    
    # References section
    references = get_references("Osteoarthritis")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-01-15",
            show_evidence_level=True,
            show_links=True
        )

