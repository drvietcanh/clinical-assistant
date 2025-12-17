"""
Severe Influenza / Viral Pneumonia Protocol
WHO 2024, IDSA 2018
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Severe Influenza Protocol"""
    st.subheader("🦠 Cúm mùa nặng / Viêm phổi do cúm")
    st.caption("WHO 2024 | IDSA 2018 - Ưu tiên khởi trị Oseltamivir sớm")

    st.info(
        """
        **Điểm chính:**
        - Bắt đầu **oseltamivir ngay** khi nghi ngờ cúm nặng, không chờ xét nghiệm.
        - Đánh giá nguy cơ diễn tiến nặng: thai kỳ, >65 tuổi, bệnh phổi nền (COPD, hen), béo phì, đái tháo đường, bệnh tim, suy giảm miễn dịch.
        - Phân biệt/điều trị đồng nhiễm vi khuẩn (CAP/HAP) rất thường gặp.
        """
    )

    st.markdown("### 1️⃣ Đánh giá mức độ nặng ban đầu")
    col1, col2 = st.columns(2)
    with col1:
        severe_flags = [
            st.checkbox("SpO₂ < 92% hoặc PaO₂/FiO₂ < 300", key="flu_spo2"),
            st.checkbox("Nhịp thở > 30 lần/phút hoặc co kéo cơ hô hấp phụ", key="flu_rr"),
            st.checkbox("Huyết áp tụt / cần vận mạch", key="flu_bp"),
            st.checkbox("Rối loạn tri giác / lơ mơ", key="flu_gcs"),
            st.checkbox("X-quang/CT viêm phổi lan tỏa hoặc ARDS", key="flu_ards"),
        ]
        risk_flags = [
            st.checkbox("Thai kỳ / hậu sản ≤2 tuần", key="flu_preg"),
            st.checkbox("Bệnh mạn: COPD/hen, tim mạch, đái tháo đường, béo phì", key="flu_comorb"),
            st.checkbox("Suy giảm miễn dịch / dùng corticoid kéo dài", key="flu_immune"),
        ]
    with col2:
        if any(severe_flags):
            st.error("🚨 Cúm nặng/ARDS – nhập viện, cân nhắc ICU và hỗ trợ hô hấp.")
            severity = "severe"
        elif any(risk_flags):
            st.warning("⚠️ Nguy cơ cao – bắt đầu kháng virus sớm, theo dõi sát, cân nhắc nhập viện.")
            severity = "moderate"
        else:
            st.success("✅ Không dấu hiệu nặng – điều trị kháng virus sớm và theo dõi ngoại trú nếu an toàn.")
            severity = "mild"

    st.markdown("---")
    st.markdown("### 2️⃣ Xét nghiệm gợi ý (song song điều trị)")
    with st.expander("📋 Xem xét nghiệm khởi đầu", expanded=False):
        st.markdown(
            """
            - RT-PCR hoặc test nhanh kháng nguyên cúm (không trì hoãn điều trị nếu nghi ngờ cao).
            - CBC, CRP/Procalcitonin (gợi ý bội nhiễm), chức năng gan thận.
            - X-quang ngực; CT khi nghi biến chứng/ARDS.
            - Khí máu động mạch nếu SpO₂ thấp.
            - Cấy đờm/máu trước khi dùng kháng sinh nếu nghi đồng nhiễm.
            """
        )

    st.markdown("---")
    st.markdown("### 3️⃣ Điều trị kháng virus")
    st.success(
        """
        **Oseltamivir (ưu tiên, kể cả sau 48 giờ nếu nặng/nhập viện):**
        - Người lớn: **75 mg PO mỗi 12h x 5 ngày** (có thể 10 ngày nếu bệnh nặng/chậm cải thiện).
        - CrCl 10–30 mL/phút: 75 mg PO mỗi 24h.
        - Phụ nữ mang thai và cho con bú: **an toàn**, dùng liều chuẩn.

        **Thay thế khi không dùng PO/kháng thuốc hiếm gặp:**
        - Zanamivir hít 10 mg mỗi 12h (không dùng nếu hen/COPD nặng).
        - Peramivir IV 600 mg một liều (cân nhắc ở bệnh nhân không uống được, theo phác đồ địa phương).
        """
    )

    st.warning(
        """
        **Không khuyến cáo thường quy:** Corticosteroid toàn thân chỉ dùng khi có chỉ định khác (sốc nhiễm khuẩn, hen/COPD kèm đợt cấp).
        """
    )

    st.markdown("---")
    st.markdown("### 4️⃣ Kháng sinh & điều trị đồng nhiễm")
    st.info(
        """
        - Nghi đồng nhiễm vi khuẩn (sốt cao kéo dài, bạch cầu tăng, đờm mủ, thâm nhiễm thùy): điều trị theo phác đồ **CAP/HAP** tại cơ sở, de-escalation khi có kết quả cấy.
        - Tránh trễ kháng sinh nếu sốc nhiễm khuẩn/ARDS.
        """
    )

    st.markdown("---")
    st.markdown("### 5️⃣ Hỗ trợ hô hấp & ICU")
    st.error(
        """
        - **O₂:** mục tiêu SpO₂ 92–96% (COPD: 88–92%).
        - **HFNC** cho suy hô hấp thiếu oxy; giảm tải đặt nội khí quản.
        - **NIV (BiPAP/CPAP)** nếu tăng CO₂ hoặc khó thở nhiều và còn hợp tác.
        - **Đặt nội khí quản** nếu PaO₂/FiO₂ <150, co kéo cơ hô hấp, sốc, rối loạn tri giác.
        - **ARDS:** thông khí bảo vệ (VT 6 mL/kg, PEEP phù hợp), prone sớm.
        """
    )

    st.markdown("---")
    st.markdown("### 6️⃣ Dự phòng và chăm sóc kèm")
    st.info(
        """
        - Tiêm phòng cúm mùa hàng năm (người ≥6 tháng, ưu tiên nhóm nguy cơ).
        - Điều trị hỗ trợ: bù dịch vừa phải, hạ sốt (paracetamol), dinh dưỡng, phòng huyết khối nếu nhập viện.
        - Cách ly giọt bắn/khẩu trang; nhân viên y tế dùng khẩu trang y tế/N95 trong thủ thuật khí dung.
        """
    )

    st.markdown("---")
    references = get_references("Severe Influenza")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-12-01",
            show_evidence_level=True,
            show_links=True,
        )

    st.caption("⚠️ Ưu tiên khởi trị oseltamivir sớm và kiểm soát hô hấp, cá thể hóa theo tình trạng bệnh nhân và khuyến cáo mới nhất.")

