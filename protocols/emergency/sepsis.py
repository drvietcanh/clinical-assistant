"""
Sepsis 1-Hour Bundle Protocol
Surviving Sepsis Campaign 2021
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Sepsis 1-Hour Bundle Protocol"""
    st.subheader("🦠 Sepsis 1-Hour Bundle")
    st.caption("Surviving Sepsis Campaign 2021")
    
    st.info("""
    **Chẩn đoán Sepsis:**
    - Nhiễm trùng (nghi ngờ hoặc xác định)
    - qSOFA ≥2 hoặc SOFA tăng ≥2 điểm
    - Rối loạn chức năng cơ quan
    """)
    
    st.markdown("---")
    
    st.markdown("### ⏱️ Sepsis 1-Hour Bundle")
    
    st.error("""
    **Thực hiện NGAY trong vòng 1 GIỜ:**
    
    1. ✅ **Đo Lactate**
       - Lactate >2 mmol/L = septic shock
       - Đo lại sau 2-4h nếu tăng
    
    2. ✅ **Cấy máu trước khi kháng sinh**
       - 2 bộ cấy máu (từ 2 vị trí khác nhau)
       - Cấy dịch từ ổ nhiễm (nếu có)
    
    3. ✅ **Kháng sinh phổ rộng**
       - Trong vòng 1 giờ
       - Theo guideline địa phương
       - Liều đủ, đường IV
    
    4. ✅ **Truyền dịch nhanh**
       - 30 mL/kg crystalloid
       - Trong 3 giờ đầu
       - Ringer Lactate hoặc Normal Saline
    
    5. ✅ **Vasopressor nếu hạ huyết áp**
       - Nếu MAP <65 mmHg sau truyền dịch
       - Norepinephrine là thuốc đầu tay
       - Mục tiêu MAP ≥65 mmHg
    """)
    
    st.markdown("---")
    
    st.markdown("### 💊 Lựa chọn kháng sinh thực nghiệm")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("""
        **Nhiễm trùng cộng đồng:**
        - Ceftriaxone 2g IV q24h
        + Azithromycin 500mg IV q24h
        
        **Hoặc:**
        - Piperacillin-Tazobactam 4.5g IV q6h
        """)
    
    with col2:
        st.warning("""
        **Nhiễm trùng bệnh viện:**
        - Meropenem 1g IV q8h
        + Vancomycin 15-20mg/kg IV
        
        **Hoặc:**
        - Piperacillin-Tazobactam 4.5g IV q6h
        + Vancomycin
        """)
    
    st.markdown("---")
    
    st.markdown("### 🎯 Mục tiêu điều trị (First 6 Hours)")
    
    st.info("""
    **Resuscitation Goals:**
    - MAP ≥65 mmHg
    - Urine output ≥0.5 mL/kg/h
    - Lactate bình thường hóa
    - ScvO2 ≥70% (nếu đo được)
    
    **Monitoring:**
    - Dấu hiệu sống mỗi 15-30 phút
    - Lactate q2-4h cho đến bình thường
    - Urine output hourly
    - Consider arterial line
    """)
    
    st.markdown("---")
    
    st.markdown("### ⚠️ Vasopressor/Inotrope")
    
    st.error("""
    **Lựa chọn vasopressor:**
    
    **1st line: Norepinephrine**
    - 0.05-2 mcg/kg/min
    - Mục tiêu MAP ≥65 mmHg
    
    **2nd line: Vasopressin**
    - 0.03-0.04 units/min
    - Thêm vào nếu norepinephrine không đủ
    
    **3rd line: Epinephrine**
    - 0.05-2 mcg/kg/min
    - Nếu cần thêm vasopressor
    
    **Inotrope: Dobutamine**
    - 2.5-20 mcg/kg/min
    - Nếu cardiac output thấp
    """)
    
    # References section
    references = get_references("Sepsis")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-01-15",
            show_evidence_level=True,
            show_links=True
        )

