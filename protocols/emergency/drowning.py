"""
Drowning / Near-Drowning Protocol
ILCOR/ERC 2021 guidance
Airway-first, ventilation priority, hypothermia and aspiration management
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Drowning / Near-Drowning Protocol"""
    st.subheader("🌊 Đuối Nước / Hút Nước (Drowning)")
    st.caption("ILCOR/ERC 2021 – Ưu tiên đường thở, thông khí, xử trí hạ thân nhiệt và ARDS sớm")

    st.error(
        """
        **⚠️ ĐUỐI NƯỚC = CẤP CỨU HỒI SỨC**
        - Nguyên nhân tử vong: thiếu oxy, ngưng tim, hạ thân nhiệt, ARDS.
        - Ưu tiên: **thông khí sớm**, không trì hoãn ép tim nếu ngưng tuần hoàn.
        """
    )

    st.markdown("---")

    # ========== SECTION 1: TÌNH HUỐNG BAN ĐẦU ========== #
    scenario = st.radio(
        "**Tình huống:**",
        [
            "Có mạch, còn tự thở",
            "Có mạch, suy hô hấp / SpO₂ thấp",
            "Không mạch / ngưng thở (CPR)"
        ],
        key="drowning_scenario",
    )

    st.markdown("---")

    if "Không mạch" in scenario:
        render_arrest()
    elif "suy hô hấp" in scenario:
        render_resp_failure()
    else:
        render_mild()

    st.markdown("---")
    render_references_section(get_references("Drowning"))


def render_arrest():
    st.markdown("### 🚨 Không mạch / Ngưng thở")
    st.info(
        """
        - **Bắt đầu CPR ngay**, ưu tiên **5 nhịp thổi cứu ngạt đầu tiên** nếu người lớn; sau đó 30:2 như thường lệ.
        - Oxy 100%; đặt NKQ sớm nếu có thể, chú ý ngừa trào ngược.
        - Sau ROSC: kiểm soát đường thở, thông khí bảo vệ phổi, tránh tăng thông khí.
        - Hạ thân nhiệt: xử trí theo protocol hypothermia (làm ấm chủ động nếu <32°C).
        """
    )


def render_resp_failure():
    st.markdown("### 😮‍💨 Có mạch, suy hô hấp")
    st.info(
        """
        - Oxy cao lưu lượng; CPAP/NIV nếu phù hợp và bệnh nhân hợp tác.
        - Nếu SpO₂ không cải thiện hoặc ý thức giảm → NKQ, thông khí bảo vệ phổi (low tidal volume).
        - Theo dõi phù phổi/ARDS sớm; dịch truyền thận trọng, ưu tiên duy trì huyết động.
        - Cân nhắc kháng sinh chỉ khi nghi hít nước bẩn/biển ô nhiễm hoặc viêm phổi sau hít sặc.
        """
    )


def render_mild():
    st.markdown("### ✅ Có mạch, còn tự thở, nhẹ")
    st.info(
        """
        - Đánh giá SpO₂, tri giác; oxy nếu SpO₂ <94%.
        - Quan sát tối thiểu 4–6 giờ; chụp X-quang nếu ho, khó thở, SpO₂ thấp.
        - Xuất viện nếu không triệu chứng sau quan sát, SpO₂ bình thường, X-quang bình thường.
        """
    )


