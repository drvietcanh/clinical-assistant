"""
Nephrolithiasis / Renal Colic Protocol
EAU Urolithiasis 2024, AUA 2022
Quản lý sỏi thận/niệu quản cấp tính thường gặp
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Nephrolithiasis / Renal Colic Protocol"""
    st.subheader("🪨 Sỏi thận / Cơn đau quặn thận")
    st.caption("EAU Urolithiasis 2024, AUA 2022 - ưu tiên đánh giá tắc nghẽn & nhiễm trùng sớm")

    st.info("""
    **Điểm chính:**
    - Tam chứng nguy hiểm: sốt, đau quặn thận, tắc nghẽn → xử trí như nhiễm trùng đường niệu tắc nghẽn (cấp cứu)
    - NSAID là giảm đau hàng đầu; giảm nhu động niệu quản tốt hơn opioid
    - Đánh giá kích thước/ vị trí sỏi để quyết định tống xuất tự nhiên hay can thiệp
    """)

    st.markdown("---")

    scenario = st.radio(
        "Tình huống lâm sàng:",
        [
            "🙂 Cơn đau quặn thận không sốt, ổn định",
            "🔥 Nghi tắc nghẽn + nhiễm trùng/AKI",
            "⚠️ Nguy cơ cao (thận đơn độc, có thai, suy thận mạn)"
        ],
        key="stone_scenario"
    )

    st.markdown("---")

    if "ổn định" in scenario:
        render_uncomplicated_colic()
    elif "tắc nghẽn" in scenario or "nhiễm trùng" in scenario:
        render_obstructed_infected()
    else:
        render_high_risk()

    st.markdown("---")
    references = get_references("Nephrolithiasis")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-12-10",
            show_evidence_level=True,
            show_links=True
        )


def render_uncomplicated_colic():
    """Stable renal colic without infection"""
    st.success("## 🙂 Cơn đau quặn thận không sốt, không nhiễm trùng")

    st.markdown("### Chẩn đoán ban đầu")
    st.info("""
    - Khám: ấn đau hông lưng, không dấu nhiễm trùng
    - Xét nghiệm: tổng phân tích nước tiểu (hồng cầu vi thể), creatinine, điện giải
    - Hình ảnh: siêu âm tại giường (dịch quanh thận, giãn đài bể) ± X-quang KUB; CT không cản quang nếu nghi ngờ cao/đau kéo dài
    """)

    st.markdown("---")
    st.markdown("### Giảm đau & hỗ trợ")
    st.warning("""
    - NSAID: Diclofenac 75 mg IM hoặc 50 mg uống mỗi 8 giờ; Ketorolac 15–30 mg IV/IM (tránh nếu suy thận/giảm thể tích)
    - Opioid cứu vãn: Morphine 2–4 mg IV mỗi 5–10 phút nếu đau không kiểm soát
    - Chống nôn: Ondansetron 4–8 mg IV/PO
    - Hydration: truyền dịch vừa phải nếu mất nước; tránh over-hydration
    """)

    st.markdown("---")
    st.markdown("### Chiến lược tống xuất sỏi")
    st.success("""
    - Sỏi <5 mm, không tắc nặng: theo dõi ngoại trú + giảm đau
    - Sỏi 5–10 mm: thêm thuốc giãn cơ trơn/expulsive
      * Tamsulosin 0.4 mg uống buổi tối × 4–6 tuần (nếu không chống chỉ định)
    - Dặn bệnh nhân: lọc nước tiểu để thu sỏi, quay lại nếu sốt/tiểu ít/đau tăng
    - Tái khám: 1–2 tuần; đánh giá lại hình ảnh nếu chưa tiểu được sỏi hoặc đau kéo dài
    """)

    st.markdown("---")
    st.markdown("### Khi cần can thiệp sớm")
    st.info("""
    - Kích thước >10 mm hoặc không di chuyển sau 4–6 tuần
    - Đau không kiểm soát dù tối ưu thuốc
    - Giãn đài bể thận tăng, chức năng thận giảm
    - Nghề nghiệp cần bảo đảm (phi công, lái xe đường dài) → cân nhắc can thiệp
    """)


def render_obstructed_infected():
    """Obstructed infected stone (urologic emergency)"""
    st.error("## 🔥 Tắc nghẽn + nhiễm trùng/AKI (cấp cứu tiết niệu)")

    st.markdown("### Xử trí ngay tại khoa cấp cứu")
    st.error("""
    - Hồi sức: đường truyền lớn, truyền dịch đẳng trương, kiểm soát huyết áp
    - Kháng sinh tĩnh mạch sớm (theo phác đồ UTI nặng): Piperacillin/Tazobactam hoặc Meropenem nếu nguy cơ ESBL
    - Cấy máu + nước tiểu trước kháng sinh
    - Đau: tránh NSAID nếu tụt huyết áp/suy thận; dùng opioid liều thấp
    """)

    st.markdown("---")
    st.markdown("### Giải áp đường tiểu khẩn cấp")
    st.warning("""
    - Đặt JJ niệu quản hoặc mở thận ra da (PCN) càng sớm càng tốt
    - Chỉ định tuyệt đối: sốt/sepsis + tắc, thận đơn độc, creatinine tăng nhanh, vô niệu, thai kỳ có tắc
    - Sau giải áp, tiếp tục kháng sinh 10–14 ngày, trì hoãn tán sỏi khi nhiễm trùng đã kiểm soát
    """)


def render_high_risk():
    """High risk populations"""
    st.warning("## ⚠️ Nhóm nguy cơ cao / đặc biệt")

    st.markdown("### Thận đơn độc, ghép thận, suy thận mạn")
    st.info("""
    - Ngưỡng nhập viện thấp; theo dõi sát diuresis, creatinine
    - Hạn chế NSAID; ưu tiên giảm đau bằng opioid liều thấp + acetaminophen
    - Hội chẩn thận/tiết niệu sớm, cân nhắc giải áp nếu tắc một phần
    """)

    st.markdown("---")
    st.markdown("### Thai kỳ")
    st.success("""
    - Chẩn đoán: siêu âm ưu tiên; tránh CT
    - Giảm đau: Paracetamol; tránh NSAID tam cá nguyệt 3; opioid ngắn hạn nếu cần
    - Quản lý tắc nghẽn: đặt JJ/PCN an toàn hơn phẫu thuật khi đang nhiễm trùng
    """)

    st.markdown("---")
    st.markdown("### Phòng ngừa tái phát (tư vấn ngắn gọn)")
    st.info("""
    - Uống đủ nước: mục tiêu nước tiểu 2–2.5 L/ngày
    - Giảm muối, hạn chế protein động vật quá mức
    - Bổ sung citrate (chanh) nếu sỏi canxi tái phát
    - Theo dõi chuyển hóa: Ca, uric, citrate niệu nếu tái phát nhiều lần
    """)


