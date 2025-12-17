"""
UTI & Pyelonephritis Protocol
IDSA/EAU 2024 + Bộ Y tế Việt Nam
Quản lý nhiễm trùng đường tiết niệu thường gặp
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """UTI & Pyelonephritis Protocol"""
    st.subheader("🚻 Nhiễm Trùng Tiết Niệu & Viêm Bể Thận")
    st.caption("IDSA/EAU 2024 + hướng dẫn Bộ Y tế - ưu tiên kháng sinh phù hợp đề kháng tại Việt Nam")

    st.info("""
    **Điểm lưu ý tại Việt Nam:**
    - E. coli vẫn chiếm đa số, tỷ lệ ESBL tăng (đặc biệt ở bệnh viện, có sonde)
    - Tránh lạm dụng fluoroquinolone; ưu tiên beta-lactam/cephalosporin phù hợp kháng sinh đồ
    - Cần tầm soát tắc nghẽn (sỏi, u, sonde) vì hay gặp ở bệnh nhân nam lớn tuổi
    """)

    st.markdown("---")

    scenario = st.radio(
        "Chọn tình huống lâm sàng:",
        [
            "💊 Viêm bàng quang không biến chứng (nữ khỏe mạnh)",
            "🔥 Viêm thận - bể thận / UTI có sốt",
            "⚠️ UTI phức tạp (nam, đái tháo đường, thai kỳ, suy thận)",
            "🧪 UTI liên quan sonde tiểu (CAUTI)"
        ],
        key="uti_scenario"
    )

    st.markdown("---")

    if "bàng quang" in scenario:
        render_uncomplicated_cystitis()
    elif "bể thận" in scenario or "sốt" in scenario:
        render_pyelonephritis()
    elif "phức tạp" in scenario:
        render_complicated_uti()
    else:
        render_cauti()

    st.markdown("---")
    references = get_references("UTI/Pyelonephritis")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-12-15",
            show_evidence_level=True,
            show_links=True
        )


def render_uncomplicated_cystitis():
    """Simple cystitis (outpatient)"""
    st.success("## 💊 Viêm bàng quang không biến chứng (nữ trẻ, không bệnh nền)")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Chẩn đoán")
        st.info("""
        - Triệu chứng: tiểu buốt, tiểu rắt, tiểu gấp; không sốt/cơn đau hông lưng
        - Không cần cấy nước tiểu nếu lần đầu, triệu chứng nhẹ
        - Cấy nước tiểu nếu: tái phát nhanh, mang thai, triệu chứng không điển hình
        """)

    with col2:
        st.markdown("### Điều trị khởi đầu")
        st.success("""
        **Kháng sinh ưu tiên (5–7 ngày):**
        - Nitrofurantoin 100 mg x 2 lần/ngày × 5 ngày (tránh nếu CrCl <30)
        - Fosfomycin 3g liều duy nhất (nếu sẵn có)
        - Cefuroxime 500 mg x 2 lần/ngày × 5 ngày
        - Amoxicillin/Clavulanate 875/125 mg x 2 lần/ngày × 5–7 ngày

        **Tránh fluoroquinolone** nếu không cần thiết (kháng cao, tác dụng phụ)
        """)

    st.markdown("---")
    st.markdown("### Theo dõi")
    st.warning("""
    - Nếu không cải thiện sau 48–72h → cấy nước tiểu, đánh giá kháng thuốc
    - Mang thai: ưu tiên beta-lactam; không dùng fluoroquinolone, TMP/SMX trong 3 tháng đầu/cuối
    - Tái phát ≥3 lần/năm → cân nhắc đánh giá phụ khoa, tiết niệu
    """)


def render_pyelonephritis():
    """Febrile UTI / pyelonephritis"""
    st.error("## 🔥 Viêm thận - bể thận / UTI có sốt")

    st.markdown("### Đánh giá ban đầu")
    st.info("""
    - Sinh hiệu, mức độ nặng (qSOFA/SIRS)
    - Cấy máu + cấy nước tiểu trước khi dùng kháng sinh
    - Xét nghiệm: CTM, CRP/Procalcitonin, creatinine, điện giải, lactate nếu nghi sepsis
    - Siêu âm thận/niệu quản nếu đau lưng một bên, nghi tắc nghẽn, có sỏi, hoặc không đáp ứng
    """)

    st.markdown("---")
    st.markdown("### Kháng sinh kinh nghiệm (điều chỉnh theo kháng sinh đồ)")
    st.error("""
    **Ngoại trú hoặc bệnh nhẹ (không nôn, không sepsis):**
    - Ceftriaxone 1–2 g IV/IM liều đầu → chuyển uống sau 24–48h: Cefuroxime 500 mg x 2 lần/ngày hoặc Amoxiclav 875 mg x 2 lần/ngày (7–10 ngày)
    - Nếu có yếu tố ESBL (nhập viện gần đây, dùng kháng sinh gần, sonde, đái tháo đường): Amikacin 15–20 mg/kg IV liều tải + Ceftriaxone hoặc Ertapenem (nếu kháng cao)

    **Nhập viện/bệnh nặng:**
    - Piperacillin/Tazobactam 4.5 g IV mỗi 6h HOẶC
    - Cefepime 2 g IV mỗi 8–12h
    - Nghi ngờ ESBL/đã dùng carbapenem gần đây: Meropenem 1 g IV mỗi 8h
    - Dị ứng beta-lactam: Aztreonam ± Amikacin (cần theo dõi sát)

    **Thời gian:** 7–10 ngày (không biến chứng), 10–14 ngày nếu có ổ áp-xe/tắc nghẽn chưa giải quyết
    """)

    st.markdown("---")
    st.markdown("### Hỗ trợ & chỉ định hội chẩn")
    st.warning("""
    - Truyền dịch đẳng trương nếu tụt huyết áp/mất nước; tránh quá tải ở bệnh nhân suy tim/thận
    - Giảm đau: Paracetamol; tránh NSAID nếu suy thận/giảm tưới máu
    - Hội chẩn tiết niệu nếu: nghi tắc nghẽn (sỏi, u), thận đơn độc, suy thận tiến triển, không đáp ứng sau 48–72h
    - Cân nhắc đặt JJ hoặc dẫn lưu nếu có tắc + nhiễm trùng
    """)


def render_complicated_uti():
    """Complicated UTI (male, DM, CKD, pregnancy)"""
    st.warning("## ⚠️ UTI phức tạp (nam, đái tháo đường, thai kỳ, suy thận, can thiệp tiết niệu)")

    st.markdown("### Chiến lược")
    st.info("""
    - Luôn cấy nước tiểu trước kháng sinh; cân nhắc cấy máu nếu sốt hoặc ớn lạnh
    - Tầm soát tắc nghẽn (siêu âm thận - bàng quang sau tiểu)
    - Điều chỉnh liều theo mức lọc cầu thận
    """)

    st.markdown("---")
    st.markdown("### Kháng sinh gợi ý")
    st.success("""
    - Ceftriaxone 1–2 g IV mỗi 24h hoặc Cefotaxime 1–2 g mỗi 8h
    - Piperacillin/Tazobactam 4.5 g IV mỗi 6h nếu nghi Pseudomonas hoặc có dụng cụ niệu
    - Meropenem 1 g IV mỗi 8h nếu nguy cơ ESBL cao
    - Step-down uống (khi ổn định và có kháng sinh đồ): Amoxiclav, Cefuroxime, hoặc Fluoroquinolone (chỉ khi nhạy và không có chống chỉ định)

    **Thời gian:** 7–10 ngày; 10–14 ngày nếu nam, tiểu máu dai dẳng, hoặc bất thường cấu trúc
    """)

    st.markdown("---")
    st.markdown("### Lưu ý thai kỳ & người già")
    st.warning("""
    - Thai kỳ: tránh fluoroquinolone, aminoglycoside nếu có lựa chọn khác; ưu tiên Cephalosporin/Amoxiclav
    - Người già: nguy cơ kháng thuốc cao, theo dõi độc tính thuốc (aminoglycoside, vancomycin)
    """)


def render_cauti():
    """Catheter-associated UTI"""
    st.info("## 🧪 Nhiễm trùng tiết niệu liên quan sonde (CAUTI)")

    st.markdown("### Xử trí ban đầu")
    st.success("""
    - Thay sonde mới trước khi lấy mẫu cấy (nếu còn chỉ định đặt)
    - Đánh giá lại chỉ định sonde, cân nhắc rút nếu có thể
    - Cấy nước tiểu + máu (nếu sốt/ớn lạnh)
    """)

    st.markdown("---")
    st.markdown("### Kháng sinh kinh nghiệm")
    st.warning("""
    - Bệnh nhẹ, không sepsis: Ceftriaxone 1–2 g IV mỗi 24h HOẶC Cefepime 2 g IV mỗi 12h nếu nguy cơ Pseudomonas
    - Nguy cơ ESBL (thay sonde nhiều lần, nằm ICU kéo dài, kháng sinh gần đây): Ertapenem 1 g IV mỗi 24h hoặc Meropenem 1 g IV mỗi 8h
    - Dị ứng beta-lactam: Aztreonam ± Amikacin (theo dõi chức năng thận)
    - Thời gian: 7 ngày nếu đáp ứng nhanh; 10–14 ngày nếu chậm cải thiện hoặc có tắc nghẽn
    """)

    st.markdown("---")
    st.markdown("### Theo dõi & phòng ngừa")
    st.info("""
    - Theo dõi sốt, huyết áp, nước tiểu mỗi 4–6h trong 24–48h đầu
    - Phòng ngừa: kỹ thuật vô khuẩn, hệ thống kín, túi thấp hơn bàng quang, rút sonde sớm
    """)


