"""
Pulmonary Tuberculosis Protocol
WHO 2024 | National TB Program alignment
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Pulmonary Tuberculosis Protocol"""
    st.subheader("🫁 Lao phổi (Pulmonary Tuberculosis)")
    st.caption("WHO 2024 | CTCLQG Lao & Bệnh phổi - Ưu tiên phát hiện sớm, cách ly và báo cáo")

    st.warning(
        "⚠️ **Báo cáo & kiểm soát lây nhiễm:** Đeo khẩu trang N95/FFP2 cho nhân viên, "
        "đặt phòng áp lực âm nếu có, thông báo Chương trình chống lao và bệnh phổi."
    )

    st.info(
        "**Khi nghi lao phổi:** ho kéo dài >2 tuần, ho ra máu, gầy sút cân, sốt nhẹ chiều, "
        "ra mồ hôi đêm, tiền sử tiếp xúc F0-Lao, X-quang tổn thương dạng thâm nhiễm/ hang/ tổn thương đỉnh phổi."
    )

    st.markdown("### 1️⃣ Phân tầng mức độ & nhập viện")
    col1, col2 = st.columns(2)

    with col1:
        severe_flags = [
            st.checkbox("Khó thở / SpO₂ < 92% dù O₂", key="tb_resp"),
            st.checkbox("Ho ra máu ồ ạt / Hct giảm nhanh", key="tb_hemoptysis"),
            st.checkbox("Nghi lao màng não / lao kê có suy đa cơ quan", key="tb_cns"),
            st.checkbox("Huyết động không ổn định", key="tb_hemo"),
        ]
        high_risk = [
            st.checkbox("HIV dương tính / ức chế miễn dịch", key="tb_hiv"),
            st.checkbox("Suy dinh dưỡng nặng / thai kỳ", key="tb_nutrition"),
            st.checkbox("Trẻ <5 tuổi hoặc người già >65", key="tb_age"),
        ]

    with col2:
        severity_score = sum(severe_flags)
        if severity_score > 0:
            st.error("🚨 Lao phổi nặng – cần nhập viện/ICU và hội chẩn chuyên khoa.")
            severity = "severe"
        elif sum(high_risk) > 0:
            st.warning("⚠️ Lao phổi có yếu tố nguy cơ – nên nhập viện hoặc theo dõi sát.")
            severity = "moderate"
        else:
            st.success("✅ Lao phổi nghi ngờ/ổn định – có thể điều trị ngoại trú theo dõi sát.")
            severity = "mild"

    st.markdown("---")
    st.markdown("### 2️⃣ Chẩn đoán nhanh và xét nghiệm ban đầu")
    with st.expander("📋 Xem gợi ý xét nghiệm", expanded=False):
        st.markdown(
            """
            **Ưu tiên lấy mẫu trước khi dùng kháng sinh:**
            - GeneXpert MTB/RIF hoặc Xpert Ultra từ đờm/NAAT khác (kết quả trong 2 giờ, phát hiện kháng Rifampicin).
            - Soi đờm AFB (≥2 mẫu) + cấy MGIT nếu có.
            - X-quang phổi hoặc CT ngực khi cần phân biệt.
            - HIV test nhanh, công thức máu, chức năng gan thận, đường huyết, HBsAg/anti-HCV.
            - Nếu ho ra máu ồ ạt: chuẩn bị nội soi cầm máu, can thiệp mạch; ưu tiên đặt đường thở an toàn.
            """
        )

    st.markdown("---")
    st.markdown("### 3️⃣ Điều trị lao nhạy cảm thuốc (chuẩn CTCLQG)")
    st.success(
        """
        **Phác đồ chuẩn người lớn (HRZE):**
        - **Tấn công 2 tháng:** Isoniazid (H) + Rifampicin (R) + Pyrazinamide (Z) + Ethambutol (E) **mỗi ngày**.
        - **Duy trì 4 tháng:** Isoniazid (H) + Rifampicin (R) **mỗi ngày**.

        **Liều tham khảo (mg/kg/ngày - tối đa):**
        - H: 4–6 mg/kg (tối đa 300 mg)
        - R: 8–12 mg/kg (tối đa 600 mg)
        - Z: 20–25 mg/kg (tối đa 2 g)
        - E: 15–20 mg/kg (tối đa 1.6 g)

        **Nguyên tắc:**
        - Bắt đầu ngay sau khi lấy mẫu xét nghiệm; không trì hoãn nếu nguy cơ lây lan cao.
        - Dùng thuốc kết hợp cố định liều (FDC) theo cân nặng khi có.
        - Bổ sung Pyridoxine 25–50 mg/ngày (phòng viêm dây thần kinh).
        """
    )

    st.info(
        """
        **Theo dõi & an toàn thuốc:**
        - Chức năng gan: baseline, sau 2–4 tuần; ngừng H/R/Z nếu ALT/AST >5x ULN có triệu chứng.
        - Thị lực màu khi dùng Ethambutol; hỏi mờ mắt mỗi lần tái khám.
        - Tư vấn tuân thủ, không tự ngưng thuốc; cân nhắc DOT khi khả năng tuân thủ thấp.
        """
    )

    st.warning(
        """
        **Nghi ngờ/đã xác định kháng thuốc (MDR/XDR) hoặc không dung nạp:**
        - Tiền sử điều trị lao thất bại/tái phát nhiều lần, tiếp xúc nguồn MDR.
        - Gửi GeneXpert/Rifampicin resistance, nuôi cấy + kháng sinh đồ; hội chẩn chuyên khoa lao.
        - Chuyển tuyến chương trình chống lao để phác đồ có Bedaquiline/Fluoroquinolone theo hướng dẫn.
        """
    )

    if severity == "severe":
        st.error(
            """
            **Hỗ trợ cấp cứu:**
            - O₂ mục tiêu SpO₂ 92–96%; chuẩn bị đặt NKQ nếu suy hô hấp/ho ra máu không kiểm soát.
            - Kiểm soát ho ra máu: nằm đầu cao, ưu tiên nằm nghiêng phổi tổn thương xuống; hội chẩn nội soi/IR.
            - Kháng sinh phối hợp nếu đồng nhiễm vi khuẩn đi kèm (theo kháng sinh đồ địa phương).
            """
        )

    st.markdown("---")
    references = get_references("Pulmonary TB")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-12-01",
            show_evidence_level=True,
            show_links=True,
        )

    st.caption("⚠️ Tuân thủ phác đồ quốc gia, báo cáo chương trình chống lao; cá thể hóa theo tình trạng cụ thể.")

