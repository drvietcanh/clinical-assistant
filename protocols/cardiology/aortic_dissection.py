"""
Aortic Dissection Protocol
AHA/ACC Guidelines 2024, ESC Guidelines 2024
Life-threatening condition requiring immediate treatment
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section
from components.evidence_badge import (
    render_evidence_badge,
    render_evidence_summary,
    Citation
)


def render():
    """Aortic Dissection Management Protocol"""
    st.subheader("💔 Bóc Tách Động Mạch Chủ (Aortic Dissection)")
    st.caption("AHA/ACC Guidelines 2024, ESC Guidelines 2024 - Life-threatening condition")
    
    # Evidence summary
    render_evidence_summary(
        last_reviewed="2024-03-01",
        last_updated="2024-03-01",
        version="2024",
        guideline_source="AHA/ACC 2024, ESC 2024"
    )
    
    st.error("""
    **⚠️ BÓC TÁCH ĐỘNG MẠCH CHỦ = CẤP CỨU Y KHOA - TỬ VONG CAO**
    
    **Định nghĩa:**
    - Rách lớp nội mạc động mạch chủ
    - Máu chảy vào giữa các lớp → Tách thành 2 lớp
    - Có thể vỡ → Tử vong nhanh
    
    **Phân loại (Stanford):**
    - **Type A:** Liên quan đến động mạch chủ lên (cần phẫu thuật cấp cứu)
    - **Type B:** Chỉ động mạch chủ xuống (có thể điều trị nội khoa)
    
    **Triệu chứng Điển Hình:**
    - **Đau ngực/lưng:** Đột ngột, dữ dội, "xé rách"
    - **Hạ huyết áp hoặc tăng huyết áp**
    - **Mạch yếu/chênh lệch**
    - **Triệu chứng thần kinh** (nếu ảnh hưởng mạch máu não)
    """)
    
    st.markdown("---")
    
    st.markdown("### ⚡ Xử trí ngay lập tức (ABC)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.error("""
        **1. AIRWAY & BREATHING**
        
        **Intubation:**
        - Nếu giảm ý thức
        - Suy hô hấp
        - Chuẩn bị trước phẫu thuật
        
        **Oxygen:**
        - **High-flow:** 10-15 L/min qua mask
        - **Mục tiêu:** SpO₂ ≥95%
        
        **2. CIRCULATION**
        
        **Monitoring:**
        - **Continuous ECG**
        - **Arterial line** (theo dõi BP liên tục)
        - **BP ở cả 2 tay** (phát hiện chênh lệch)
        - **BP, HR:** Mỗi 5 phút
        """)
    
    with col2:
        st.warning("""
        **3. ỔN ĐỊNH HUYẾT ÁP (Quan trọng!)**
        
        **Mục tiêu:**
        - **SBP:** 100-120 mmHg
        - **HR:** <60 bpm
        - **Tránh:** Tăng huyết áp (làm nặng bóc tách)
        
        **4. VENOUS ACCESS**
        
        - **2 đường tĩnh mạch lớn**
        - Chuẩn bị thuốc cấp cứu
        
        **5. IMAGING NGAY:**
        - **CT scan:** (ưu tiên)
        - **Echo:** (nếu có)
        - **MRI:** (nếu cần)
        """)
    
    st.markdown("---")
    
    st.markdown("### 🔍 Chẩn đoán")
    
    dissection_type = st.radio(
        "**Loại bóc tách (Stanford Classification):**",
        [
            "Type A - Động mạch chủ lên (Cần phẫu thuật cấp cứu)",
            "Type B - Động mạch chủ xuống (Có thể điều trị nội khoa)"
        ],
        key="aortic_dissection_type"
    )
    
    st.markdown("---")
    
    st.markdown("### 💊 Điều trị Thuốc (Ổn định Huyết áp)")
    
    st.error("## 🚨 ỔN ĐỊNH HUYẾT ÁP - ƯU TIÊN")
    
    st.success("""
    **1. BETA-BLOCKERS (Thuốc đầu tay)**
    
    **Esmolol (Ưu tiên - tác dụng ngắn):**
    - **Liều:** 500 mcg/kg IV bolus
    - **Duy trì:** 50-300 mcg/kg/min
    - **Lợi ích:** Tác dụng ngắn, dễ điều chỉnh
    
    **Hoặc Metoprolol:**
    - **Liều:** 5 mg IV mỗi 5 phút (tối đa 15 mg)
    - **Duy trì:** 25-50 mg PO bid
    
    **Hoặc Labetalol:**
    - **Liều:** 20 mg IV, sau đó 40-80 mg mỗi 10 phút
    - **Duy trì:** 200-400 mg PO bid
    
    **Mục tiêu:**
    - **HR:** <60 bpm
    - **SBP:** 100-120 mmHg
    
    **2. VASODILATORS (Nếu cần thêm)**
    
    **Nitroprusside:**
    - **Liều:** 0.25-0.5 mcg/kg/min
    - **Tăng dần:** 0.5 mcg/kg/min mỗi 5 phút
    - **Tối đa:** 10 mcg/kg/min
    - **Lưu ý:** Chỉ dùng SAU khi đã dùng beta-blocker
    
    **Hoặc Nicardipine:**
    - **Liều:** 5-15 mg/h IV
    - **Tăng dần:** 2.5 mg/h mỗi 5-15 phút
    
    **Lưu ý:**
    - **KHÔNG dùng vasodilator đơn độc** (làm tăng HR, nặng bóc tách)
    - **Luôn dùng beta-blocker trước**
    """)
    
    st.markdown("---")
    
    if "Type A" in dissection_type:
        render_type_a()
    else:
        render_type_b()
    
    st.markdown("---")
    
    st.markdown("### 📋 Điều trị Hỗ trợ")
    
    st.info("""
    **1. Pain Management:**
    - **Morphine:** 2-5 mg IV (mỗi 2-4h)
    - **Fentanyl:** 50-100 mcg IV (mỗi 1-2h)
    - **Mục đích:** Giảm đau, giảm stress
    
    **2. Monitoring:**
    - **Huyết áp:** Mỗi 5 phút (mục tiêu 100-120 mmHg)
    - **HR:** Mỗi 5 phút (mục tiêu <60 bpm)
    - **Mạch:** Đánh giá chênh lệch
    - **Thần kinh:** Đánh giá chức năng
    - **Thận:** Urine output, Creatinine
    
    **3. Labs:**
    - **CBC, BMP, Coagulation**
    - **Troponin:** (loại trừ ACS)
    - **D-dimer:** (có thể tăng)
    
    **4. Imaging:**
    - **CT scan:** (ưu tiên, xác định chẩn đoán)
    - **Echo:** (đánh giá van động mạch chủ)
    - **MRI:** (nếu cần)
    """)
    
    st.markdown("---")
    
    st.markdown("### ⚠️ Biến chứng")
    
    with st.expander("📋 Xem các biến chứng thường gặp", expanded=False):
        st.markdown("""
        **Tim mạch:**
        - Vỡ động mạch chủ (tử vong nhanh)
        - Hở van động mạch chủ
        - Nhồi máu cơ tim (tắc mạch vành)
        - Chèn ép tim (hemopericardium)
        
        **Thần kinh:**
        - Đột quỵ (tắc mạch não)
        - Tổn thương tủy sống
        - Tổn thương dây thần kinh
        
        **Khác:**
        - Suy thận (tắc mạch thận)
        - Thiếu máu chi (tắc mạch ngoại vi)
        - Xuất huyết (vỡ)
        """)
    
    st.markdown("---")
    
    st.markdown("### 📈 Tiên lượng & Theo dõi")
    
    st.info("""
    **Tiên lượng:**
    - **Type A:** Tử vong 1-2%/giờ nếu không phẫu thuật
    - **Type B:** Tử vong 10-20% (nếu điều trị đúng)
    - **Yếu tố nguy cơ:**
      - Chậm trễ điều trị
      - Vỡ động mạch chủ
      - Biến chứng nặng
    
    **Theo dõi:**
    - **ICU:** Ít nhất 24-48h
    - **Huyết áp, HR:** Mỗi 5-15 phút (cho đến khi ổn định)
    - **Mạch:** Đánh giá chênh lệch
    - **Thần kinh:** Đánh giá chức năng
    - **CT scan:** Theo dõi (nếu cần)
    
    **Xuất viện:**
    - Huyết áp ổn định
    - Không biến chứng
    - Đã điều trị (phẫu thuật hoặc nội khoa)
    - Theo dõi ít nhất 48-72h
    """)
    
    st.markdown("---")
    
    # References
    references = get_references("Aortic Dissection")
    if references:
        render_references_section(references)
    else:
        st.markdown("### 📚 References")
        st.markdown("""
        1. **AHA/ACC Guidelines 2024** - American Heart Association
        2. **ESC Guidelines 2024** - European Society of Cardiology
        3. **UpToDate:** Aortic Dissection - Last updated 2024
        """)
    
    st.markdown("---")
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất.")


def render_type_a():
    """Type A Dissection"""
    st.error("## 🚨🚨🚨 TYPE A - PHẪU THUẬT CẤP CỨU")
    
    st.markdown("""
    **Đặc điểm:**
    - Liên quan đến động mạch chủ lên
    - Nguy cơ vỡ cao
    - Có thể ảnh hưởng van động mạch chủ
    - Có thể ảnh hưởng mạch vành
    
    **Điều trị:**
    
    **1. Ổn định Huyết áp:**
    - Beta-blocker + Vasodilator
    - Mục tiêu: SBP 100-120 mmHg, HR <60 bpm
    
    **2. Phẫu thuật (Cấp cứu):**
    - **Chỉ định:** Tất cả Type A
    - **Thời gian:** Càng sớm càng tốt
    - **Mục tiêu:** Sửa chữa động mạch chủ lên
    
    **3. Monitoring:**
    - Huyết áp, HR (mỗi 5 phút)
    - Thần kinh
    - Thận
    - Chuẩn bị phẫu thuật
    
    **Tiên lượng:**
    - Tử vong: 1-2%/giờ nếu không phẫu thuật
    - Với phẫu thuật: Tử vong 10-20%
    """)


def render_type_b():
    """Type B Dissection"""
    st.warning("## ⚠️ TYPE B - ĐIỀU TRỊ NỘI KHOA (Có thể)")
    
    st.markdown("""
    **Đặc điểm:**
    - Chỉ động mạch chủ xuống
    - Nguy cơ vỡ thấp hơn
    - Có thể điều trị nội khoa
    
    **Điều trị:**
    
    **1. Ổn định Huyết áp:**
    - Beta-blocker + Vasodilator
    - Mục tiêu: SBP 100-120 mmHg, HR <60 bpm
    
    **2. Điều trị Nội khoa (Nếu ổn định):**
    - Ổn định huyết áp
    - Pain management
    - Monitoring sát
    - CT scan theo dõi
    
    **3. Chỉ định Phẫu thuật/Endovascular:**
    - Vỡ hoặc đe dọa vỡ
    - Thiếu máu chi
    - Suy thận
    - Đau tái phát
    - Tăng kích thước
    
    **4. Endovascular Repair (TEVAR):**
    - Nếu có chỉ định
    - Ít xâm lấn hơn phẫu thuật
    - Kết quả tốt
    
    **Tiên lượng:**
    - Tử vong: 10-20% (nếu điều trị đúng)
    - Với điều trị nội khoa: Tử vong 5-10%
    """)

