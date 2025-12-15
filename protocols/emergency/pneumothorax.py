"""
Pneumothorax Protocol
Tension pneumothorax & spontaneous pneumothorax management
Based on BTS 2023, ACCP guidance
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Pneumothorax Protocol"""
    st.subheader("🫁 Tràn Khí Màng Phổi (Tension & Spontaneous)")
    st.caption("BTS 2023, ACCP – Giải áp khẩn cấp, dẫn lưu, theo dõi/quan sát")

    st.error(
        """
        **⚠️ TENSION PNEUMOTHORAX = CẤP CỨU**
        - Chẩn đoán lâm sàng, **không chờ X-quang** nếu nghi ngờ cao.
        - Giải áp kim ngay → đặt ống dẫn lưu ngực.
        """
    )

    st.markdown("---")

    # ========== SECTION 1: PHÂN LOẠI ========== #
    scenario = st.radio(
        "**Tình huống:**",
        [
            "Tension pneumothorax (nguy kịch)",
            "Spontaneous pneumothorax – ổn định",
            "Spontaneous pneumothorax – không ổn định / to"
        ],
        key="pntx_scenario",
    )

    st.markdown("---")

    if "Tension" in scenario:
        render_tension()
    elif "không ổn định" in scenario or "to" in scenario:
        render_unstable_sp()
    else:
        render_stable_sp()

    st.markdown("---")
    render_references_section(get_references("Pneumothorax"))


def render_tension():
    st.markdown("### 🚨 Tension Pneumothorax – Xử trí ngay")
    st.info(
        """
        1) **Giải áp kim ngay** (không chờ X-quang):
           - Vị trí ưu tiên: KLS 4-5 đường nách giữa với catheter 14-16G.
           - Hoặc: KLS 2 đường giữa đòn (ít ưu tiên hơn, dày thành ngực).
        2) **Đặt ống dẫn lưu** (ICS 4-5 đường nách giữa) càng sớm càng tốt.
        3) Oxy 100%, theo dõi SpO₂, HA, nhịp tim.
        4) Tìm và xử trí nguyên nhân (thủ thuật xâm lấn, chấn thương, barotrauma).
        """
    )


def render_unstable_sp():
    st.markdown("### ⚠️ Spontaneous PTX – Không ổn định / lớn")
    st.info(
        """
        - Đặt ống dẫn lưu ngực (ICS 4-5 MAL).
        - Oxy 15 L/phút để tăng hấp thu khí.
        - Theo dõi kín, đánh giá rò khí, chụp X-quang sau đặt ống.
        - Cân nhắc van Heimlich nếu không có hệ thống dẫn lưu nước.
        """
    )


def render_stable_sp():
    st.markdown("### ✅ Spontaneous PTX – Ổn định (nhỏ)")
    st.info(
        """
        - **Quan sát + Oxy** nếu nhỏ, không triệu chứng, lần đầu.
        - **Chọc hút (aspiration)** nếu PTX vừa, triệu chứng nhẹ.
        - Tái đánh giá X-quang sau 4-6 giờ; nếu xấu → đặt ống dẫn lưu.
        - Hẹn tái khám, dặn tránh bay/lặn cho tới khi khỏi hoàn toàn.
        """
    )


