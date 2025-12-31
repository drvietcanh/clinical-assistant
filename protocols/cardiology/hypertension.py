"""
Hypertension Management Protocol
Based on ESC 2024 & AHA 2025 Guidelines
"""

import streamlit as st
from components.phase1_protocol_enhancer import (
    render_protocol_header,
    render_recommendation_with_evidence,
    render_protocol_footer
)
from components.evidence_badge import render_evidence_summary

def render():
    st.subheader("🩸 Tăng Huyết Áp (Hypertension)")
    st.caption("ESC 2024 Guidelines")

    render_protocol_header(
        protocol_name="Hypertension Management",
        guideline_source="ESC 2024 / AHA 2025",
        show_version=True,
        show_evidence_summary=True
    )
    
    render_evidence_summary(
        last_reviewed="2025-01-01",
        last_updated="2025-01-01",
        version="2025",
        guideline_source="ESC 2024 Guidelines"
    )

    st.markdown("### 🎯 Mục tiêu huyết áp (BP Targets)")
    st.info("""
    **Thay đổi quan trọng 2024/2025:** Mục tiêu HA tâm thu tích cực hơn.
    - **Mục tiêu chung:** 120-129 mmHg (nếu dung nạp tốt).
    - **Người cao tuổi / Suy yếu:** Cân nhắc 130-139 mmHg.
    - **HA Tâm trương:** < 80 mmHg.
    """)

    st.markdown("### 💊 Chiến lược điều trị (Drug Strategy)")

    st.markdown("**Bước 1: Khởi trị phối hợp đôi (Dual Combination)**")
    render_recommendation_with_evidence(
        "ACEi/ARB + CCB hoặc Thiazide-like diuretic",
        evidence_level="A",
        citation_indices=[1],
        inline=True
    )

    st.markdown("**Bước 2: Phối hợp ba (Triple Combination)**")
    render_recommendation_with_evidence(
        "ACEi/ARB + CCB + Thiazide-like diuretic",
        evidence_level="A",
        citation_indices=[1],
        inline=True
    )

    st.markdown("**Bước 3: Tăng huyết áp kháng trị**")
    render_recommendation_with_evidence(
        "Thêm Spironolactone (25-50mg) hoặc thuốc khác (BB, Alpha-blocker)",
        evidence_level="B",
        citation_indices=[1, 2],
        inline=True
    )

    st.markdown("### ❤️ Beta-Blockers")
    st.warning("Beta-blockers không phải lựa chọn hàng đầu trừ khi có chỉ định bắt buộc: Suy tim, Sau NMCT, Rung nhĩ, hoặc Phụ nữ có thai.")

    st.markdown("---")
    render_protocol_footer("Hypertension Management")
