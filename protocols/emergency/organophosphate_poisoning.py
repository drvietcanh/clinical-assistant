"""
Organophosphate Poisoning Protocol
WHO/CDC/AACT guidelines for cholinergic crisis management
Life-threatening cholinergic toxidrome from organophosphate exposure
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Organophosphate Poisoning Protocol"""
    st.subheader("🧪 Ngộ Độc Thuốc Trừ Sâu Phospho Hữu Cơ (Organophosphate)")
    st.caption("WHO, CDC, AACT/EAPCCT – Cholinergic crisis management")

    st.error(
        """
        **⚠️ NGỘ ĐỘC ORGANOPHOSPHATE = CẤP CỨU Y TẾ**

        - Ức chế acetylcholinesterase → Tích tụ ACh → Cơn cholinergic
        - Tử vong do suy hô hấp: tăng tiết, co thắt phế quản, yếu cơ hô hấp
        - Điều trị ưu tiên: **giải độc atropine sớm và đủ liều**, hỗ trợ hô hấp, pralidoxime
        """
    )

    st.markdown("---")

    # ========== SECTION 1: CHẨN ĐOÁN & PHÂN TẦNG ========== #
    st.markdown("### 📋 Chẩn đoán Nhanh")
    st.info(
        """
        **Toxidrome cholinergic (DUMBELS/SLUDGE + nicotinic):**
        - **Muscarinic:** D, U, M, B, E, L, S (Tiêu chảy, Tiểu nhiều, Co đồng tử, Co thắt phế quản, Chảy nước bọt, Chảy nước mắt)
        - **Nicotinic:** Yếu cơ, rung giật cơ, liệt, tăng/loạn nhịp
        - **TKTW:** Lú lẫn, co giật, hôn mê
        """
    )

    severity = st.radio(
        "**Mức độ lâm sàng:**",
        [
            "Nhẹ (tỉnh, tiết dịch ít, không suy hô hấp)",
            "Trung bình (tiết dịch nhiều, co thắt PQ, yếu cơ nhẹ)",
            "Nặng (suy hô hấp, tiết dịch ồ ạt, yếu cơ rõ)",
            "Tối cấp/ICU (hôn mê, co giật, ngưng thở)"
        ],
        key="op_severity",
    )

    st.markdown("---")

    # ========== SECTION 2: XỬ TRÍ BAN ĐẦU ========== #
    st.markdown("### 🏥 Xử trí Ban Đầu (ABCD + Giải Độc)")
    st.warning(
        """
        1) **Đảm bảo an toàn nhân viên**: PPE, tháo bỏ quần áo nhiễm độc, rửa da bằng xà phòng/nước.
        2) **Đường thở – Hô hấp:** Oxy 100%, hút đàm dãi, cân nhắc đặt NKQ nếu tiết dịch nhiều/ yếu cơ.
        3) **Tuần hoàn:** Theo dõi mạch/HA, truyền dịch thận trọng, kiểm soát loạn nhịp.
        4) **Không trì hoãn atropine** để chờ xét nghiệm.
        """
    )

    st.markdown("---")

    # ========== SECTION 3: GIẢI ĐỘC ATROPINE ========== #
    st.markdown("### 💉 Atropine (ưu tiên tuyệt đối)")

    atropine_start = st.number_input(
        "Liều nạp atropine IV (mg) đề xuất khởi đầu:",
        min_value=0.5,
        max_value=10.0,
        value=2.0,
        step=0.5,
        help="Khởi đầu 1–3 mg IV; nhắc lại mỗi 3–5 phút đến khi hết tăng tiết/khò khè.",
    )

    st.info(
        f"""
        **Nguyên tắc:** Tăng nhanh liều đến khi **phổi khô, nhịp >80, HA ổn**.
        - Khởi đầu: {atropine_start:.1f} mg IV (1–3 mg tùy nặng).
        - Nhắc lại: cùng liều mỗi 3–5 phút cho tới khi hết tăng tiết.
        - Duy trì: Truyền tĩnh mạch 10–20% tổng liều nạp mỗi giờ (titration theo triệu chứng).
        - Tránh atropine thiếu liều vì sẽ kéo dài suy hô hấp.
        """
    )

    st.markdown("---")

    # ========== SECTION 4: PRALIDOXIME (2-PAM) ========== #
    st.markdown("### 🧬 Pralidoxime (2-PAM) – tái hoạt AChE")
    weight = st.number_input(
        "Cân nặng (kg):",
        min_value=10.0,
        max_value=200.0,
        value=60.0,
        step=1.0,
        key="op_weight",
    )

    bolus_2pam = weight * 20  # mg/kg (20–30 mg/kg) bolus
    infusion_2pam = weight * 10  # mg/kg/h

    st.success(
        f"""
        **Liều gợi ý (người lớn ≥40 kg):**
        - **Bolus:** {bolus_2pam:.0f} mg IV (20–30 mg/kg) tiêm/ truyền 20–30 phút.
        - **Duy trì:** {infusion_2pam:.0f} mg/giờ (≈10 mg/kg/giờ) trong 24–48 giờ.
        - Nếu không có bơm tiêm điện: lặp bolus mỗi 4–6 giờ.

        **Chỉ định ưu tiên:** yếu cơ, suy hô hấp, ngộ độc nặng, trễ <48 giờ (chưa “aging”).
        """
    )

    st.markdown("---")

    # ========== SECTION 5: HỖ TRỢ & ĐIỀU TRỊ KHÁC ========== #
    st.markdown("### 🛠️ Hỗ trợ Khác")
    st.markdown(
        """
        - **Khử nhiễm:** Cởi bỏ quần áo, rửa da 15 phút; tránh lây nhiễm chéo.
        - **Hô hấp:** Đặt NKQ nếu: SpO₂ <94% dù oxy, tăng tiết không kiểm soát, yếu cơ/PAO2 <60.
        - **Than hoạt:** Nếu uống <1 giờ và tỉnh/đã bảo vệ đường thở; tránh gây hít.
        - **Co giật:** Diazepam 5–10 mg IV; có thể dùng midazolam.
        - **Theo dõi:** ECG liên tục, ABG, lactate, cholinesterase (nếu có), đường huyết, nhiệt độ.
        - **Tránh:** Succinylcholine (kéo dài liệt), thuốc ức chế AChE khác.
        """
    )

    st.markdown("---")

    # ========== SECTION 6: THEO DÕI & TIÊU CHÍ NGỪNG ATROPINE ========== #
    st.markdown("### 📈 Theo dõi & Ngừng Thuốc")
    st.info(
        """
        - Giảm truyền atropine khi hết tăng tiết ≥12–24 giờ, mạch/HA ổn định.
        - Cắt atropine thử: giảm 10–20% mỗi 2–4 giờ; nếu tái tăng tiết → tăng lại.
        - Tiếp tục pralidoxime ít nhất 24–48 giờ hoặc 12 giờ sau ổn định.
        - Cảnh giác hội chứng trung gian (yếu cơ 24–96h), có thể cần kéo dài 2-PAM/hỗ trợ hô hấp.
        """
    )

    st.markdown("---")

    # ========== SECTION 7: ĐỐI TƯỢNG ĐẶC BIỆT ========== #
    st.markdown("### 👥 Đối Tượng Đặc biệt")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            """
            **Trẻ em:** Liều atropine/2-PAM theo mg/kg như trên; ưu tiên hỗ trợ hô hấp sớm.

            **Có thai:** Atropine/2-PAM an toàn tương đối; bảo vệ mẹ ưu tiên cho thai.
            """
        )
    with col2:
        st.markdown(
            """
            **Suy thận:** Tích lũy pralidoxime – cân nhắc giảm tốc độ truyền sau ổn định.

            **Ngộ độc hỗn hợp carbamate:** 2-PAM có thể không cần thiết; dùng khi nghi hỗn hợp OP.
            """
        )

    st.markdown("---")

    # ========== SECTION 8: TÀI LIỆU THAM KHẢO ========== #
    render_references_section(get_references("Organophosphate Poisoning"))


