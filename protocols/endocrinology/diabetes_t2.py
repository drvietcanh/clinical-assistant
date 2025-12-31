"""
Type 2 Diabetes Management
Based on ADA 2025 Standards of Care
"""

import streamlit as st
from components.phase1_protocol_enhancer import (
    render_protocol_header,
    render_recommendation_with_evidence,
    render_protocol_footer
)
from components.evidence_badge import render_evidence_summary

def render():
    st.subheader("🍬 Đái tháo đường T2 (Diabetes Type 2)")
    st.caption("ADA 2025 Standards of Care")

    render_protocol_header(
        protocol_name="Type 2 Diabetes Management",
        guideline_source="ADA 2025",
        show_version=True,
        show_evidence_summary=True
    )
    
    render_evidence_summary(
        last_reviewed="2025-01-01",
        last_updated="2025-01-01",
        version="2025",
        guideline_source="ADA 2025 Standards"
    )

    st.markdown("### 💊 Phác đồ điều trị 2025 (Pharmacotherapy)")
    
    st.info("""
    **Thay đổi quan trọng 2025:**
    - Không còn mặc định Metformin là thuốc đầu tay duy nhất.
    - Ưu tiên thuốc bảo vệ Tim-Thận (SGLT2i, GLP-1 RA) **độc lập với mức HbA1c ban đầu** nếu bệnh nhân có nguy cơ cao.
    """)

    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 1. Có bệnh Tim mạch / Thận (ASCVD / HF / CKD)")
        st.success("**Ưu tiên hàng đầu (First-line):**")
        render_recommendation_with_evidence(
            "GLP-1 RA (có lợi ích CV)",
            evidence_level="A",
            citation_indices=[1],
            inline=True
        )
        render_recommendation_with_evidence(
            "SGLT2i (Đặc biệt nếu có Suy tim/CKD)",
            evidence_level="A",
            citation_indices=[1],
            inline=True
        )
        st.caption("*Dùng độc lập với Metformin*")

    with col2:
        st.markdown("#### 2. Không có bệnh Tim mạch / Thận")
        st.info("**Trọng tâm: Kiểm soát đường huyết & Cân nặng**")
        render_recommendation_with_evidence(
            "Metformin + Thay đổi lối sống",
            evidence_level="A",
            citation_indices=[1],
            inline=True
        )
        st.markdown("**Nếu cần giảm cân:**")
        render_recommendation_with_evidence(
            "GLP-1 RA hoặc GIP/GLP-1 (Tirzepatide)",
            evidence_level="A",
            citation_indices=[2],
            inline=True
        )

    st.markdown("---")
    st.markdown("### 🎯 Mục tiêu điều trị")
    st.markdown("- **HbA1c:** < 7.0% (cá thể hóa)")
    st.markdown("- **Huyết áp:** < 130/80 mmHg")
    st.markdown("- **Lipid:** LDL < 70 mg/dL (< 55 nếu nguy cơ rất cao)")

    render_protocol_footer("Type 2 Diabetes Management")
