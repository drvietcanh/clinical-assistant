"""
Status Epilepticus Protocol
AES 2016, Neurocritical Care Society
Prolonged or recurrent seizures without recovery
"""

import streamlit as st
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
    """Status Epilepticus Protocol"""
    st.subheader("🧠 Trạng thái động kinh liên tục (Status Epilepticus)")
    st.caption("AES 2016, Neurocritical Care Society - Prolonged seizures management")
    
    # Enhanced header with Phase 1 components
    render_protocol_header(
        protocol_name="Status Epilepticus",
        guideline_source="AES 2016, Neurocritical Care Society",
        show_version=True,
        show_evidence_summary=True
    )
    
    st.error("""
    **⚠️ TRẠNG THÁI ĐỘNG KINH LIÊN TỤC = CẤP CỨU Y TẾ**
    
    **Định nghĩa:**
    - Co giật liên tục ≥5 phút
    - Hoặc ≥2 cơn co giật không hồi phục ý thức giữa các cơn
    
    **Phân loại:**
    - **Đã thiết lập (Established SE):** ≥5 phút
    - **Kháng trị (Refractory SE, RSE):** Không đáp ứng với 2 thuốc chống động kinh
    - **Siêu kháng trị (Super-refractory SE, SRSE):** ≥24 giờ dù đã dùng thuốc mê
    """)
    
    st.markdown("---")
    
    st.markdown("### ⚡ Xử trí ngay lập tức (0-5 phút)")
    
    st.error("""
    **1. ABC (Đường thở, Hô hấp, Tuần hoàn):**
    - Đảm bảo đường thở
    - Oxygen 100%
    - Monitor: BP, HR, SpO2, ECG
    
    **2. Đo đường huyết:**
    - Nếu <60 mg/dL: Dextrose 50% 50 mL IV
    - Hoặc: Thiamine 100 mg IV trước dextrose (nếu nghi ngờ thiếu thiamine)
    
    **3. Thuốc đầu tay - Benzodiazepines:**
    - **Lorazepam:** 0.1 mg/kg IV (max 4 mg) - Ưu tiên
    - **Hoặc:** Midazolam: 0.2 mg/kg IM (max 10 mg)
    - **Hoặc:** Diazepam: 0.15-0.2 mg/kg IV (max 10 mg)
    - **Lặp lại:** Nếu còn co giật sau 5 phút
    """)
    
    st.markdown("---")
    
    st.markdown("### 💊 Thuốc chống động kinh (5-20 phút)")
    
    st.warning("""
    **Nếu vẫn còn co giật sau benzodiazepine:**
    
    **1. Fosphenytoin (Ưu tiên):**
    - **Liều:** 20 mg PE/kg IV (max 1500 mg)
    - **Tốc Độ:** ≤150 mg PE/min
    - **Ưu điểm:** Ít gây kích ứng mạch máu hơn phenytoin
    
    **2. Phenytoin:**
    - **Liều:** 20 mg/kg IV (max 1500 mg)
    - **Tốc Độ:** ≤50 mg/min
    - **Theo dõi:** ECG, huyết áp
    
    **3. Valproate:**
    - **Liều:** 20-40 mg/kg IV (max 3000 mg)
    - **Tốc Độ:** 3-6 mg/kg/min
    - **Chống chỉ định:** Bệnh gan, thiếu hụt enzyme chuyển hóa
    
    **4. Levetiracetam:**
    - **Liều:** 20-60 mg/kg IV (max 4500 mg)
    - **Tốc Độ:** 5-15 phút
    - **Ưu điểm:** Ít tương tác thuốc, an toàn
    """)
    
    st.markdown("---")
    
    st.markdown("### 🔄 Trạng thái động kinh liên tục kháng trị (20-40 phút)")
    
    st.error("""
    **Nếu vẫn còn co giật sau 2 Thuốc chống động kinh:**
    
    **1. Midazolam truyền tĩnh mạch:**
    - **Bolus:** 0.2 mg/kg IV
    - **Truyền:** 0.05-2 mg/kg/h
    - **Mục tiêu:** EEG burst suppression
    
    **2. Propofol:**
    - **Bolus:** 1-2 mg/kg IV
    - **Truyền:** 1-15 mg/kg/h
    - **Cảnh báo:** Propofol infusion syndrome (nếu >48 giờ)
    
    **3. Pentobarbital:**
    - **Bolus:** 5-15 mg/kg IV
    - **Truyền:** 0.5-5 mg/kg/h
    - **Dùng khi:** Midazolam/propofol không hiệu quả
    """)
    
    st.markdown("---")
    
    st.markdown("### 🚨 Trạng thái động kinh liên tục siêu kháng trị (≥40 phút)")
    
    st.error("""
    **Nếu vẫn còn co giật sau thuốc mê:**
    
    **1. Ketamine:**
    - **Bolus:** 1-3 mg/kg IV
    - **Truyền:** 0.5-10 mg/kg/h
    - **Ưu điểm:** Không ức chế hô hấp
    
    **2. Isoflurane/Desflurane:**
    - Gây mê hô hấp
    - Cần bác sĩ gây mê
    
    **3. Các phương pháp khác:**
    - Vagus nerve stimulation
    - Ketogenic diet
    - Hypothermia
    - ECT (electroconvulsive therapy)
    """)
    
    st.markdown("---")
    
    st.markdown("### 📊 Phân loại theo thời gian")
    
    timeline = st.radio(
        "**Thời gian co giật:**",
        ["0-5 phút (Sớm)", "5-20 phút (Đã thiết lập)", "20-40 phút (Kháng trị)", "≥40 phút (Siêu kháng trị)"],
        key="se_timeline"
    )
    
    st.markdown("---")
    
    if "0-5" in timeline:
        render_early_se()
    elif "5-20" in timeline:
        render_established_se()
    elif "20-40" in timeline:
        render_refractory_se()
    else:
        render_super_refractory_se()
    
    st.markdown("---")
    
    st.markdown("### 🔍 Nguyên nhân & điều trị nguyên nhân")
    
    st.info("""
    **Nguyên nhân thường gặp:**
    1. **Ngừng thuốc chống động kinh** (30-40%)
    2. **Đột quỵ** (20-25%)
    3. **Chấn thương đầu** (10-15%)
    4. **Nhiễm trùng CNS** (5-10%)
    5. **Khối u não** (5-10%)
    6. **Rối loạn chuyển hóa** (5-10%)
    7. **Ngộ độc** (5%)
    
    **Xét nghiệm:**
    - CT/MRI não
    - LP (nếu nghi ngờ nhiễm trùng)
    - Điện giải, glucose, chức năng gan/thận
    - Nồng độ thuốc chống động kinh
    - Độc chất học
    """)
    
    st.markdown("---")
    
    st.markdown("### 📋 Danh sách kiểm tra điều trị")
    
    checklist_items = [
        "✅ ABC: Đường thở, Hô hấp, Tuần hoàn",
        "✅ Đo đường huyết (nếu thấp: dextrose)",
        "✅ Thiamine 100 mg IV (nếu nghi ngờ)",
        "✅ Lorazepam 0.1 mg/kg IV (hoặc midazolam IM)",
        "✅ Fosphenytoin 20 mg PE/kg IV (nếu vẫn co giật)",
        "✅ EEG monitoring (nếu có)",
        "✅ Tìm Nguyên nhân (CT, LP, xét nghiệm)",
        "✅ ICU nếu refractory",
        "✅ Theo dõi hô hấp, huyết động"
    ]
    
    for item in checklist_items:
        st.markdown(f"- {item}")
    
    st.markdown("---")
    
    st.markdown("### 👥 Nhóm bệnh nhân đặc biệt")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Trẻ em:**
        - Liều tính theo kg
        - Midazolam IM có thể ưu tiên hơn
        - Cẩn thận với propofol (propofol infusion syndrome)
        
        **Người cao tuổi:**
        - Giảm liều benzodiazepine
        - Cẩn thận với hô hấp
        - Tìm Nguyên nhân (thường là đột quỵ)
        """)
    
    with col2:
        st.markdown("""
        **Có thai:**
        - Tránh valproate, phenytoin nếu có thể
        - Levetiracetam an toàn hơn
        - Theo dõi thai nhi
        
        **Suy gan/thận:**
        - Tránh valproate nếu suy gan
        - Điều chỉnh liều theo chức năng thận
        """)
    
    st.markdown("---")
    
    st.markdown("### 🎯 Mục tiêu điều trị")
    
    st.success("""
    **Mục tiêu:**
    - ✅ Ngừng co giật trong 5-20 phút
    - ✅ Hồi phục ý thức
    - ✅ Tìm và điều trị nguyên nhân
    - ✅ Dự phòng tái phát
    
    **Theo dõi:**
    - EEG nếu có (để phát hiện non-convulsive SE)
    - Hô hấp, huyết động
    - Chức năng thần kinh
    """)
    
    st.markdown("---")
    
    # Enhanced footer with Phase 1 component
    render_protocol_footer("Status Epilepticus")
    
    # Keep existing references as fallback
    references = get_references("Status Epilepticus")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo (Additional)",
            last_updated="2024-01-15",
            show_evidence_level=True,
            show_links=True
        )
    
    st.markdown("---")
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất.")

def render_early_se():
    """Early status epilepticus"""
    st.success("## 🟢 Sớm (0-5 phút)")
    
    st.markdown("""
    **Điều trị:**
    1. ABC, oxygen
    2. Đo đường huyết
    3. **Lorazepam:** 0.1 mg/kg IV (max 4 mg)
       - Hoặc: Midazolam 0.2 mg/kg IM
    
    **Mục tiêu:** Ngừng co giật trong 5 phút
    """)

def render_established_se():
    """Established status epilepticus"""
    st.warning("## 🟡 Đã Thiết Lập (5-20 phút)")
    
    st.markdown("""
    **Điều trị:**
    1. Nếu vẫn co giật sau benzodiazepine:
       - **Fosphenytoin:** 20 mg PE/kg IV
       - Hoặc: Valproate 20-40 mg/kg IV
       - Hoặc: Levetiracetam 20-60 mg/kg IV
    
    2. **Theo dõi:** ECG, huyết áp
    
    **Mục tiêu:** Ngừng co giật trong 20 phút
    """)

def render_refractory_se():
    """Refractory status epilepticus"""
    st.error("## 🔴 Kháng Trị (20-40 phút) - ICU")
    
    st.markdown("""
    **Điều trị:**
    1. **Midazolam truyền tĩnh mạch:**
       - Bolus: 0.2 mg/kg
       - Truyền: 0.05-2 mg/kg/h
    
    2. **Hoặc Propofol:**
       - Bolus: 1-2 mg/kg
       - Truyền: 1-15 mg/kg/h
    
    3. **EEG monitoring:** Để đánh giá hiệu quả
    
    4. **ICU care:** Đặt nội khí quản, monitoring
    
    **Mục tiêu:** EEG burst suppression
    """)

def render_super_refractory_se():
    """Super-refractory status epilepticus"""
    st.error("## ⚫ Siêu Kháng Trị (≥40 phút) - ICU Chuyên Sâu")
    
    st.markdown("""
    **Điều trị:**
    1. **Ketamine:**
       - Bolus: 1-3 mg/kg
       - Truyền: 0.5-10 mg/kg/h
    
    2. **Hoặc Pentobarbital:**
       - Bolus: 5-15 mg/kg
       - Truyền: 0.5-5 mg/kg/h
    
    3. **Các phương pháp khác:**
       - Isoflurane/Desflurane
       - Vagus nerve stimulation
       - Ketogenic diet
       - Hypothermia
    
    4. **Hội chẩn:** Thần kinh, gây mê
    
    **Mục tiêu:** Kiểm soát co giật, Tìm Nguyên nhân
    """)

