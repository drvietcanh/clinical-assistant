"""
Acute Pain Management Protocol
ASIPP 2017, WHO, CDC
Evidence-based acute pain management
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Acute Pain Management Protocol"""
    st.subheader("💊 Quản lý Đau Cấp")
    st.caption("ASIPP 2017, WHO, CDC - Evidence-based pain management")
    
    st.info("""
    **Quản lý đau cấp:**
    - Đau là triệu chứng phổ biến nhất
    - Cần đánh giá và điều trị đúng cách
    - Multimodal analgesia (đa phương thức) là tiêu chuẩn
    - Mục tiêu: Giảm đau hiệu quả, an toàn, ít tác dụng phụ
    
    **Nguyên tắc:**
    - Đánh giá đau thường xuyên
    - Điều trị sớm
    - Multimodal approach
    - Opioid stewardship
    """)
    
    st.markdown("---")
    
    st.markdown("### 📊 Đánh giá đau")
    
    pain_scale = st.radio(
        "**Thang điểm đau:**",
        ["NRS (0-10)", "VAS (0-100mm)", "FACES (Trẻ em)", "FLACC (Trẻ nhỏ)"],
        key="pain_scale"
    )
    
    st.markdown("---")
    
    if "NRS" in pain_scale:
        render_nrs_scale()
    elif "VAS" in pain_scale:
        render_vas_scale()
    elif "FACES" in pain_scale:
        render_faces_scale()
    else:
        render_flacc_scale()
    
    st.markdown("---")
    
    st.markdown("### 💊 Multimodal Analgesia (Đa Phương Thức)")
    
    st.success("""
    **Nguyên tắc Multimodal Analgesia:**
    - Kết hợp nhiều thuốc với cơ chế khác nhau
    - Giảm liều từng thuốc → Ít tác dụng phụ
    - Hiệu quả tốt hơn so với dùng đơn độc
    
    **Các nhóm thuốc:**
    1. **Opioids** (nếu đau nặng)
    2. **NSAIDs** (ibuprofen, naproxen, ketorolac)
    3. **Acetaminophen** (paracetamol)
    4. **Gabapentinoids** (gabapentin, pregabalin)
    5. **Local anesthetics** (nếu có thể)
    6. **Ketamine** (đau nặng, opioid-sparing)
    """)
    
    st.markdown("---")
    
    st.markdown("### 📊 Phân loại mức độ Đau")
    
    pain_level = st.radio(
        "**Mức độ đau:**",
        ["Nhẹ (1-3)", "Trung bình (4-6)", "Nặng (7-10)"],
        key="pain_level"
    )
    
    st.markdown("---")
    
    if "Nhẹ" in pain_level:
        render_mild_pain()
    elif "Trung bình" in pain_level:
        render_moderate_pain()
    else:
        render_severe_pain()
    
    st.markdown("---")
    
    st.markdown("### 💉 Opioid Dosing & Titration")
    
    st.warning("""
    **Opioid chỉ dùng khi:**
    - Đau nặng (NRS ≥7)
    - Hoặc đau trung bình không đáp ứng với non-opioid
    
    **Thuốc Opioid:**
    
    **1. Morphine (Tiêu chuẩn):**
    - **IV:** 2-5 mg q3-4h (Người Lớn)
    - **PO:** 10-30 mg q4h
    - **PCA:** 1-2 mg bolus, lockout 6-10 phút
    
    **2. Hydromorphone:**
    - **IV:** 0.5-1 mg q3-4h
    - **PO:** 2-4 mg q4h
    - **Mạnh hơn morphine 5-7 lần**
    
    **3. Fentanyl:**
    - **IV:** 25-50 mcg q1-2h
    - **Transdermal:** 12-100 mcg/h (chỉ dùng mạn tính)
    - **Tác dụng nhanh, ngắn**
    
    **4. Oxycodone:**
    - **PO:** 5-15 mg q4-6h
    - **Không có IV**
    - **Thường dùng sau phẫu thuật**
    
    **5. Tramadol:**
    - **PO:** 50-100 mg q4-6h
    - **Opioid yếu, ít nguy cơ**
    - **Max: 400 mg/ngày**
    """)
    
    st.markdown("---")
    
    st.markdown("### 💊 Non-Opioid Alternatives")
    
    st.info("""
    **1. NSAIDs:**
    - **Ibuprofen:** 400-800 mg PO q6-8h
    - **Naproxen:** 250-500 mg PO q12h
    - **Ketorolac:** 15-30 mg IV q6h (max 5 ngày)
    - **Chống chỉ định:** Suy thận, loét dạ dày, chảy máu
    
    **2. Acetaminophen (Paracetamol):**
    - **PO:** 650-1000 mg q4-6h (max 4g/ngày)
    - **IV:** 1000 mg q6h
    - **An toàn, ít tác dụng phụ**
    
    **3. Gabapentinoids:**
    - **Gabapentin:** 300-600 mg PO tid
    - **Pregabalin:** 75-150 mg PO bid
    - **Dùng cho:** Đau thần kinh, đau sau phẫu thuật
    
    **4. Ketamine:**
    - **IV:** 0.1-0.3 mg/kg/h
    - **Opioid-sparing effect**
    - **Dùng cho:** Đau nặng, kháng opioid
    """)
    
    st.markdown("---")
    
    st.markdown("### ⚠️ Opioid Stewardship")
    
    st.error("""
    **Nguyên tắc sử dụng opioid an toàn:**
    
    **1. Đánh giá nguy cơ:**
    - Tiền sử lạm dụng chất
    - Rối loạn tâm thần
    - Tuổi trẻ
    
    **2. Kê đơn hợp lý:**
    - Liều thấp nhất hiệu quả
    - Thời gian ngắn nhất
    - Không kê đơn dự phòng dài hạn
    
    **3. Theo dõi:**
    - Đánh giá đau thường xuyên
    - Đánh giá tác dụng phụ
    - Đánh giá nguy cơ lạm dụng
    
    **4. Giảm dần:**
    - Giảm 10-25% mỗi tuần
    - Không ngừng đột ngột
    - Theo dõi withdrawal
    
    **5. Giáo dục bệnh nhân:**
    - Cách dùng thuốc
    - Tác dụng phụ
    - Nguy cơ lạm dụng
    - Cách bảo quản
    """)
    
    st.markdown("---")
    
    st.markdown("### 📋 Danh sách kiểm tra điều trị")
    
    checklist_items = [
        "✅ Đánh giá đau (NRS/VAS)",
        "✅ Xác định nguyên nhân đau",
        "✅ Chọn thuốc phù hợp với mức độ đau",
        "✅ Bắt đầu với non-opioid (nếu có thể)",
        "✅ Thêm opioid nếu đau nặng",
        "✅ Multimodal approach",
        "✅ Đánh giá lại đau sau điều trị",
        "✅ Điều chỉnh liều theo đáp ứng",
        "✅ Theo dõi tác dụng phụ",
        "✅ Giảm dần opioid khi đau giảm"
    ]
    
    for item in checklist_items:
        st.markdown(f"- {item}")
    
    st.markdown("---")
    
    st.markdown("### 👥 Nhóm bệnh nhân đặc biệt")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Người cao tuổi:**
        - Bắt đầu với liều thấp (giảm 25-50%)
        - Ưu tiên non-opioid
        - Cẩn thận với opioid (nguy cơ té ngã, lú lẫn)
        - Tránh meperidine
        
        **Suy thận:**
        - Tránh NSAIDs nếu CrCl <30
        - Giảm liều morphine (tích lũy)
        - Ưu tiên fentanyl, hydromorphone
        - Tránh codeine, tramadol
        """)
    
    with col2:
        st.markdown("""
        **Suy gan:**
        - Giảm liều opioid (50%)
        - Tránh acetaminophen nếu suy gan nặng
        - Cẩn thận với NSAIDs
        - Ưu tiên fentanyl
        
        **Có thai:**
        - Acetaminophen an toàn
        - NSAIDs: Tránh trong 3 tháng cuối
        - Opioid: Có thể dùng ngắn hạn
        - Tránh codeine, tramadol
        """)
    
    st.markdown("---")
    
    st.markdown("### 🎯 Mục tiêu điều trị")
    
    st.success("""
    **Mục tiêu:**
    - ✅ Giảm đau xuống mức chấp nhận được (NRS ≤3-4)
    - ✅ Cải thiện chức năng
    - ✅ Ít tác dụng phụ
    - ✅ Không lạm dụng
    
    **Đánh giá:**
    - Đánh giá đau trước và sau điều trị
    - Đánh giá chức năng
    - Đánh giá tác dụng phụ
    - Điều chỉnh theo đáp ứng
    """)
    
    st.markdown("---")
    
    # References section
    references = get_references("Acute Pain")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-01-15",
            show_evidence_level=True,
            show_links=True
        )
    
    st.markdown("---")
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất.")


def render_nrs_scale():
    """NRS pain scale"""
    st.info("## 📊 NRS (Numeric Rating Scale)")
    
    st.markdown("""
    **Thang điểm 0-10:**
    - **0:** Không đau
    - **1-3:** Đau nhẹ
    - **4-6:** Đau trung bình
    - **7-10:** Đau nặng
    
    **Ưu điểm:**
    - Dễ sử dụng
    - Nhanh
    - Phù hợp Người Lớn
    
    **Sử dụng:**
    - Hỏi: "Đau của bạn là bao nhiêu từ 0-10?"
    - Đánh giá trước và sau điều trị
    """)


def render_vas_scale():
    """VAS pain scale"""
    st.info("## 📊 VAS (Visual Analog Scale)")
    
    st.markdown("""
    **Thang điểm 0-100mm:**
    - **0mm:** Không đau
    - **1-30mm:** Đau nhẹ
    - **31-70mm:** Đau trung bình
    - **71-100mm:** Đau nặng
    
    **Ưu điểm:**
    - Nhạy cảm
    - Phù hợp nghiên cứu
    
    **Nhược điểm:**
    - Cần thước đo
    - Phức tạp hơn NRS
    """)


def render_faces_scale():
    """FACES pain scale"""
    st.info("## 📊 FACES (Trẻ em)")
    
    st.markdown("""
    **6 khuôn mặt:**
    - Từ cười (0) đến khóc (10)
    
    **Sử dụng:**
    - Trẻ em 3-7 tuổi
    - Người không biết đọc
    - Người có khó khăn giao tiếp
    """)


def render_flacc_scale():
    """FLACC pain scale"""
    st.info("## 📊 FLACC (Trẻ Nhỏ)")
    
    st.markdown("""
    **Đánh giá 5 tiêu chí (mỗi tiêu chí 0-2 điểm):**
    - **F:** Face (Khuôn mặt)
    - **L:** Legs (Chân)
    - **A:** Activity (Hoạt động)
    - **C:** Cry (Khóc)
    - **C:** Consolability (Có thể dỗ)
    
    **Tổng điểm: 0-10**
    
    **Sử dụng:**
    - Trẻ <3 tuổi
    - Trẻ không thể giao tiếp
    """)


def render_mild_pain():
    """Mild pain protocol"""
    st.success("## 🟢 Đau Nhẹ (NRS 1-3)")
    
    st.markdown("""
    **Điều trị:**
    1. **Non-opioid:**
       - Acetaminophen: 650-1000 mg PO q4-6h
       - Hoặc NSAID: Ibuprofen 400-600 mg PO q6-8h
    
    2. **Đánh giá lại:** Sau 1-2 giờ
    
    3. **Nếu không đáp ứng:** Tăng liều hoặc thêm NSAID
    
    **Mục tiêu:** NRS ≤2
    """)


def render_moderate_pain():
    """Moderate pain protocol"""
    st.warning("## 🟡 Đau Trung Bình (NRS 4-6)")
    
    st.markdown("""
    **Điều trị:**
    1. **Multimodal:**
       - Acetaminophen: 1000 mg PO q6h
       - NSAID: Ibuprofen 600-800 mg PO q8h
       - Hoặc Ketorolac: 15-30 mg IV q6h
    
    2. **Nếu không đáp ứng:**
       - Thêm opioid yếu: Tramadol 50-100 mg PO q6h
       - Hoặc Oxycodone 5-10 mg PO q4-6h
    
    3. **Gabapentin:** 300 mg PO tid (nếu đau thần kinh)
    
    4. **Đánh giá lại:** Sau 1 giờ
    
    **Mục tiêu:** NRS ≤3-4
    """)


def render_severe_pain():
    """Severe pain protocol"""
    st.error("## 🔴 Đau Nặng (NRS 7-10)")
    
    st.markdown("""
    **Điều trị:**
    1. **Opioid ngay:**
       - **IV:** Morphine 2-5 mg q3-4h
       - **Hoặc:** Hydromorphone 0.5-1 mg IV q3-4h
       - **Hoặc:** Fentanyl 25-50 mcg IV q1-2h
    
    2. **Multimodal:**
       - Acetaminophen: 1000 mg IV q6h
       - NSAID: Ketorolac 30 mg IV q6h
       - Gabapentin: 300-600 mg PO tid
    
    3. **PCA (nếu có):**
       - Morphine: 1-2 mg bolus, lockout 6-10 phút
    
    4. **Ketamine (nếu kháng opioid):**
       - 0.1-0.3 mg/kg/h IV
    
    5. **Đánh giá lại:** Sau 30 phút
    
    6. **Titration:** Tăng liều nếu không đáp ứng
    
    **Mục tiêu:** NRS ≤4
    """)

