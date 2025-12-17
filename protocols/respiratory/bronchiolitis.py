"""
Acute Viral Bronchiolitis Protocol
AAP 2014 (updates 2023), WHO 2023
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Acute Viral Bronchiolitis Protocol"""
    st.subheader("👶 Viêm tiểu phế quản (RSV/virus hô hấp)")
    st.caption("AAP 2014 (update 2023) | WHO 2023 - Điều trị hỗ trợ là chính")

    st.info(
        """
        - Thường gặp ở trẻ <2 tuổi, cao điểm mùa đông/đầu năm tại Việt Nam.
        - Nguyên tắc: **hỗ trợ hô hấp & dinh dưỡng**, không lạm dụng kháng sinh/thuốc khí dung.
        """
    )

    st.markdown("### 1️⃣ Đánh giá mức độ nặng")
    col1, col2 = st.columns(2)
    with col1:
        severe_flags = [
            st.checkbox("SpO₂ < 92% khí phòng", key="bronch_spo2"),
            st.checkbox("Thở rên / ngừng thở / chậm nhịp tim", key="bronch_apnea"),
            st.checkbox("Co lõm lồng ngực nặng / thở rít thì thở ra", key="bronch_retract"),
            st.checkbox("Bú kém <50% nhu cầu hoặc mất nước", key="bronch_feed"),
        ]
        risk_flags = [
            st.checkbox("Sinh non <34 tuần / <3 tháng tuổi", key="bronch_preterm"),
            st.checkbox("Tim bẩm sinh, phổi mạn, suy giảm miễn dịch", key="bronch_comorb"),
        ]
    with col2:
        if any(severe_flags):
            st.error("🚨 Nặng – nhập viện, cân nhắc ICU nếu có ngừng thở/SpO₂ rất thấp.")
            severity = "severe"
        elif any(risk_flags):
            st.warning("⚠️ Nguy cơ cao – nên nhập viện hoặc theo dõi sát trong 24 giờ đầu.")
            severity = "moderate"
        else:
            st.success("✅ Nhẹ – có thể theo dõi ngoại trú với hướng dẫn rõ ràng.")
            severity = "mild"

    st.markdown("---")
    st.markdown("### 2️⃣ Điều trị hỗ trợ")
    st.success(
        """
        - **O₂:** nếu SpO₂ < 92%; có thể dùng oxy mũi, HFNC cho trường hợp trung bình-nặng.
        - **Dịch:** ưu tiên uống; nếu bú kém → truyền tĩnh mạch/sonde dạ dày (tránh quá tải).
        - **Hút rửa mũi bằng NaCl 0.9%** trước bú/ngủ giúp cải thiện thông khí.
        - **Cho bú từng ít, nhiều lần**; tư thế đầu cao 30–45°.
        """
    )

    st.warning(
        """
        **Không khuyến cáo thường quy:**
        - ❌ Kháng sinh (trừ khi nghi rõ bội nhiễm vi khuẩn).
        - ❌ Corticosteroid khí dung/toàn thân.
        - ❌ Adrenaline khí dung / Salbutamol (chỉ thử 1 liều nếu hen kèm).
        - ❌ Khí dung nước muối ưu trương thường quy.
        """
    )

    st.markdown("---")
    st.markdown("### 3️⃣ Tiêu chí nhập viện / ICU")
    st.info(
        """
        - SpO₂ < 92% khí phòng hoặc cần HFNC/NIV.
        - Ngừng thở, cơn tím, co lõm nặng.
        - Bú kém, mất nước, không chăm sóc được tại nhà.
        - Bệnh nền nặng (tim bẩm sinh, BPD, suy giảm miễn dịch).
        """
    )

    st.error(
        """
        **ICU / Hỗ trợ cao hơn:**
        - HFNC 1.5–2.5 L/kg/phút, FiO₂ chỉnh để SpO₂ 92–96%.
        - NIV/CPAP nếu HFNC thất bại hoặc tăng CO₂, ngừng thở tái diễn.
        - Đặt nội khí quản khi ngừng thở kéo dài, suy hô hấp tiến triển, không bảo vệ đường thở.
        """
    )

    st.markdown("---")
    st.markdown("### 4️⃣ Giáo dục & theo dõi sau xuất viện")
    st.success(
        """
        - Dấu hiệu cần quay lại: thở nhanh hơn, co lõm ngực, bú kém, ngủ li bì, tím tái.
        - Tiếp tục hút mũi, cho bú từng ít; giữ ấm phòng, tránh khói thuốc.
        - Khuyến cáo tiêm phòng: cúm mùa, RSV (nếu có tại cơ sở), sởi, ho gà.
        """
    )

    st.markdown("---")
    references = get_references("Bronchiolitis")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-12-01",
            show_evidence_level=True,
            show_links=True,
        )

    st.caption("⚠️ Điều trị hỗ trợ là trọng tâm; tránh lạm dụng thuốc và theo dõi sát dấu hiệu suy hô hấp.")

