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
from components.phase1_protocol_enhancer import (
    render_protocol_header,
    render_recommendation_with_evidence,
    render_protocol_footer
)


def render():
    """Sepsis 1-Hour Bundle Protocol"""
    st.subheader("🦠 Sepsis 1-Hour Bundle")
    st.caption("Surviving Sepsis Campaign 2021")
    
    # Enhanced header with Phase 1 components
    render_protocol_header(
        protocol_name="Sepsis 1-Hour Bundle",
        guideline_source="Surviving Sepsis Campaign 2021",
        show_version=True,
        show_evidence_summary=True
    )
    
    st.info("""
    **Chẩn đoán Sepsis (Sepsis-3):**
    - Nhiễm trùng (nghi ngờ hoặc xác định)
    - Tăng điểm SOFA ≥2 điểm
    - *Lưu ý: qSOFA (nhịp thở ≥22, GCS <15, Huyết áp tâm thu ≤100) chỉ dùng để sàng lọc nhanh, độ nhạy thấp.*
    """)
    
    st.markdown("---")
    
    st.markdown("### ⏱️ Sepsis 1-Hour Bundle")
    
    # Render timeline visualization
    render_sepsis_1hour_timeline()
    
    st.markdown("---")
    
    # Evidence summary
    render_evidence_summary(
        last_reviewed="2025-01-01",
        last_updated="2025-01-01",
        version="2025",
        guideline_source="Surviving Sepsis Campaign 2021 + 2025 Updates"
    )
    
    st.markdown("### ⏱️ Thực hiện NGAY trong vòng 1 GIỜ")
    
    # Enhanced recommendations with evidence levels using Phase 1 component
    render_recommendation_with_evidence(
        "Đo Lactate - Lactate >2 mmol/L = dấu hiệu giảm tưới máu. Đo lại sau 2-4h nếu tăng.",
        evidence_level="A",
        citation_indices=[1],
        inline=False
    )
    
    render_recommendation_with_evidence(
        "Cấy máu trước kháng sinh - 2 bộ (Aerobic + Anaerobic). KHÔNG trì hoãn kháng sinh >45 phút nếu khó lấy ven.",
        evidence_level="A",
        citation_indices=[1],
        inline=False
    )
    
    render_recommendation_with_evidence(
        "Kháng sinh phổ rộng IV - Trong vòng 1 giờ đầu. Cân nhắc MRSA/Pseudomonas nếu có nguy cơ.",
        evidence_level="A",
        citation_indices=[1, 2],
        inline=False
    )
    
    render_recommendation_with_evidence(
        "Bù dịch nhanh 30 mL/kg - Cho tụt huyết áp hoặc Lactate ≥4 mmol/L. Dùng tinh thể cân bằng (Balanced Crystalloids).",
        evidence_level="B",
        citation_indices=[1],
        inline=False
    )
    
    render_recommendation_with_evidence(
        "Vasopressor sớm - Dùng Norepinephrine nếu MAP <65 mmHg trong khi đang bù dịch. Đừng đợi bù đủ 30ml/kg mới bắt đầu.",
        evidence_level="A",
        citation_indices=[1],
        inline=False
    )
    
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
    
    # Enhanced footer with Phase 1 component
    render_protocol_footer("Sepsis 1-Hour Bundle")

