"""
Sepsis 1-Hour Bundle Protocol
Surviving Sepsis Campaign 2021
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section
from components.protocol_timeline import render_sepsis_1hour_timeline
from components.protocol_progress import render_sepsis_progress
from components.protocol_version import render_version_badge, render_version_history
from components.evidence_badge import (
    render_evidence_badge,
    render_evidence_section,
    render_evidence_summary,
    Citation
)


def render():
    """Sepsis 1-Hour Bundle Protocol"""
    st.subheader("🦠 Sepsis 1-Hour Bundle")
    st.caption("Surviving Sepsis Campaign 2021")
    
    # Version badge
    render_version_badge("Sepsis 1-Hour Bundle")
    
    st.info("""
    **Chẩn đoán Sepsis:**
    - Nhiễm trùng (nghi ngờ hoặc xác định)
    - qSOFA ≥2 hoặc SOFA tăng ≥2 điểm
    - Rối loạn chức năng cơ quan
    """)
    
    st.markdown("---")
    
    st.markdown("### ⏱️ Sepsis 1-Hour Bundle")
    
    # Render timeline visualization
    render_sepsis_1hour_timeline()
    
    st.markdown("---")
    
    # Evidence summary
    render_evidence_summary(
        last_reviewed="2024-10-01",
        last_updated="2024-10-01",
        version="2024",
        guideline_source="Surviving Sepsis Campaign 2021"
    )
    
    st.error("""
    **Thực hiện NGAY trong vòng 1 GIỜ:**
    
    1. ✅ **Đo Lactate** <span style="background: #4caf50; color: white; padding: 2px 6px; border-radius: 4px; font-size: 0.75rem; font-weight: bold;">Level A</span>
       - Lactate >2 mmol/L = septic shock
       - Đo lại sau 2-4h nếu tăng
    
    2. ✅ **Cấy máu trước khi kháng sinh** <span style="background: #4caf50; color: white; padding: 2px 6px; border-radius: 4px; font-size: 0.75rem; font-weight: bold;">Level A</span>
       - 2 bộ cấy máu (từ 2 vị trí khác nhau)
       - Cấy dịch từ ổ nhiễm (nếu có)
    
    3. ✅ **Kháng sinh phổ rộng** <span style="background: #4caf50; color: white; padding: 2px 6px; border-radius: 4px; font-size: 0.75rem; font-weight: bold;">Level A</span>
       - Trong vòng 1 giờ
       - Theo guideline địa phương
       - Liều đủ, đường IV
    
    4. ✅ **Truyền dịch nhanh** <span style="background: #2196f3; color: white; padding: 2px 6px; border-radius: 4px; font-size: 0.75rem; font-weight: bold;">Level B</span>
       - 30 mL/kg crystalloid
       - Trong 3 giờ đầu
       - Ringer Lactate hoặc Normal Saline
    
    5. ✅ **Vasopressor nếu hạ huyết áp** <span style="background: #4caf50; color: white; padding: 2px 6px; border-radius: 4px; font-size: 0.75rem; font-weight: bold;">Level A</span>
       - Nếu MAP <65 mmHg sau truyền dịch
       - Norepinephrine là thuốc đầu tay
       - Mục tiêu MAP ≥65 mmHg
    """, unsafe_allow_html=True)
    
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
    
    # Progress tracking checklist
    render_sepsis_progress("Sepsis 1-Hour Bundle")
    
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
    
    st.markdown("---")
    st.markdown("### 📖 Xem thêm: Sepsis 3-Hour Bundle")
    
    st.info("""
    **💡 Protocol này tập trung vào 1-Hour Bundle.**
    
    **Để xem protocol đầy đủ hơn với:**
    - Corticosteroids trong septic shock
    - Renal Replacement Therapy (RRT)
    - Glucose management
    - VTE prophylaxis
    - Source control chi tiết
    - 3-hour management protocol
    
    **→ Chọn "Sepsis 3-Hour Bundle" trong danh sách protocol**
    """)
    
    st.markdown("---")
    
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

