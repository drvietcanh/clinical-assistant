"""
BPH & Acute Urinary Retention Protocol
EAU BPO 2024, AUA BPH 2023
Quản lý LUTS do phì đại TLT và bí tiểu cấp
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """BPH/LUTS and acute urinary retention"""
    st.subheader("🧔‍♂️ Phì đại TLT (BPH) & Bí tiểu cấp")
    st.caption("EAU BPO 2024, AUA BPH 2023 - tiếp cận thường gặp tại Việt Nam")

    st.info("""
    **Tình huống thường gặp:**
    - Nam >50 tuổi, LUTS tiến triển (tiểu yếu, phải rặn, tiểu đêm)
    - Bí tiểu cấp sau uống rượu, dùng kháng histamin/đợt cấp COPD, hậu phẫu
    - Nhiều bệnh nhân có kèm tăng huyết áp, đái tháo đường, suy thận mạn
    """)

    st.markdown("---")

    scenario = st.radio(
        "Chọn tình huống:",
        [
            "🚑 Bí tiểu cấp tại khoa cấp cứu",
            "🏥 LUTS ổn định/ngoại trú (không bí tiểu)"
        ],
        key="bph_scenario"
    )

    st.markdown("---")

    if "Bí tiểu" in scenario:
        render_acute_retention()
    else:
        render_luts_outpatient()

    st.markdown("---")
    references = get_references("BPH/Urinary Retention")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-12-12",
            show_evidence_level=True,
            show_links=True
        )


def render_acute_retention():
    """Acute urinary retention management"""
    st.error("## 🚑 Bí tiểu cấp")

    st.markdown("### Xử trí ngay")
    st.error("""
    - Đặt sonde Foley vô khuẩn (16–18 Fr). Nếu khó: sonde đầu cong (Coudé) hoặc nhờ tiết niệu
    - Giảm đau/lo lắng: Lidocain gel tại chỗ, có thể dùng Midazolam liều thấp nếu cần
    - Nếu không đặt được hoặc nghi chấn thương niệu đạo (máu miệng sáo, sau tai nạn): không cố, chụp niệu đạo ngược dòng và hội chẩn tiết niệu
    """)

    st.markdown("---")
    st.markdown("### Khởi trị thuốc hỗ trợ trước khi rút sonde")
    st.success("""
    - Tamsulosin 0.4 mg uống buổi tối (hoặc Alfuzosin 10 mg)
    - Cân nhắc Finasteride 5 mg/ngày nếu tuyến >30–40 g (tác dụng sau 3–6 tháng)
    - Điều trị nguyên nhân thúc đẩy: nhiễm trùng niệu (kháng sinh theo kháng sinh đồ), táo bón, thuốc gây bí tiểu
    """)

    st.markdown("---")
    st.markdown("### Theo dõi & kế hoạch rút sonde")
    st.warning("""
    - Theo dõi nước tiểu giải áp (risk post-obstructive diuresis). Nếu >200 mL/h >4 giờ → bù dịch, theo dõi điện giải
    - Thử rút sonde (trial without catheter) sau 3–7 ngày khi triệu chứng ổn và đã dùng alpha-blocker ≥3 ngày
    - Thất bại 2 lần hoặc có biến chứng (nhiễm trùng tái diễn, sỏi bàng quang, tiểu máu nặng, suy thận) → chuyển tiết niệu đánh giá can thiệp (TURP/laser)
    """)


def render_luts_outpatient():
    """Chronic LUTS outpatient care"""
    st.success("## 🏥 LUTS ổn định/ngoại trú")

    st.markdown("### Đánh giá")
    st.info("""
    - IPSS, chất lượng sống
    - Khám trực tràng đánh giá kích thước TLT; PSA nếu nghi ngờ ung thư hoặc trước 5-ARI
    - Siêu âm: tồn dư sau tiểu (PVR), thể tích tuyến, loại trừ sỏi/bướu bàng quang
    """)

    st.markdown("---")
    st.markdown("### Điều trị nội khoa")
    st.success("""
    - Alpha-blocker: Tamsulosin 0.4 mg tối hoặc Alfuzosin 10 mg sau ăn
    - 5-ARI (Finasteride/Dutasteride): dùng khi tuyến lớn, kéo dài ≥6 tháng
    - Phối hợp alpha-blocker + 5-ARI nếu LUTS trung bình-nặng và tuyến lớn
    - Chẹn muscarinic hoặc mirabegron nếu triệu chứng kích thích trội và PVR thấp
    """)

    st.markdown("---")
    st.markdown("### Khi cần chuyển tiết niệu")
    st.warning("""
    - Tiểu máu đại thể tái phát, nhiễm trùng niệu tái diễn
    - Suy thận hoặc giãn đài bể thận do bế tắc dưới
    - PVR cao dai dẳng, sỏi bàng quang, tắc nghẽn nặng không đáp ứng thuốc
    """)


