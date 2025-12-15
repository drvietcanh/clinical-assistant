"""
Toxic Alcohol (Methanol / Ethylene Glycol) Poisoning Protocol
AACT/EAPCCT, ACEP, Goldfrank guidelines
High-mortality metabolic acidosis; antidote = fomepizole/ethanol + dialysis
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Toxic Alcohol Poisoning Protocol"""
    st.subheader("🥃 Ngộ Độc Cồn Độc (Methanol / Ethylene Glycol)")
    st.caption("AACT/EAPCCT, ACEP – Fomepizole/ethanol + lọc máu, xử trí toan nặng")

    st.error(
        """
        **⚠️ NGỘ ĐỘC CỒN ĐỘC = CẤP CỨU Y TẾ**

        - Methanol → formic acid → độc thị giác, toan chuyển hóa khoảng trống anion cao.
        - Ethylene glycol → glycolic/oxalic acid → suy thận cấp, tinh thể oxalat.
        - Antidote: **ức chế alcohol dehydrogenase (fomepizole/ethanol)** + **lọc máu** khi nặng.
        """
    )

    st.markdown("---")

    # ========== SECTION 1: ĐÁNH GIÁ TOAN – KHOẢNG TRỐNG ========== #
    st.markdown("### 📊 Đánh Giá Toan Chuyển Hóa")

    na = st.number_input("Na (mEq/L)", min_value=100.0, max_value=180.0, value=140.0, step=0.5)
    cl = st.number_input("Cl (mEq/L)", min_value=70.0, max_value=140.0, value=103.0, step=0.5)
    hco3 = st.number_input("HCO₃⁻ (mEq/L)", min_value=5.0, max_value=35.0, value=12.0, step=0.5)
    ag = na - cl - hco3
    st.info(f"**Anion gap ước tính:** {ag:.1f} mEq/L (bình thường ~8–12)")

    st.caption("Osmol gap >10 mOsm/kg + anion gap cao gợi ý ngộ độc cồn độc.")

    st.markdown("---")

    # ========== SECTION 2: PHÂN LOẠI MỨC ĐỘ ========== #
    severity = st.radio(
        "**Mức độ lâm sàng:**",
        [
            "Nguy cơ/ nghi ngờ (pH ≥7.35, chưa toan, không triệu chứng)",
            "Trung bình (toan nhẹ-vừa, có buồn nôn/ đau đầu/ nhìn mờ)",
            "Nặng (pH <7.25, lactate/anion gap cao, tổn thương thị giác hoặc suy thận)",
            "Tối cấp/ICU (pH <7.10, sốc, hôn mê, cần lọc máu khẩn)"
        ],
        key="ta_severity",
    )

    st.markdown("---")

    # ========== SECTION 3: ANTIDOTE – ỨC CHẾ ADH ========== #
    st.markdown("### 💊 Antidote: Fomepizole (ưu tiên) hoặc Ethanol")

    weight = st.number_input("Cân nặng (kg):", min_value=10.0, max_value=200.0, value=60.0, step=1.0, key="ta_weight")
    fomepizole_loading = weight * 15  # mg/kg
    fomepizole_maintenance = weight * 10  # mg/kg q12h (q4h khi lọc)

    st.success(
        f"""
        **Fomepizole (khuyến cáo ưu tiên):**
        - Liều nạp: **{fomepizole_loading:.0f} mg IV** (15 mg/kg).
        - Duy trì: **{fomepizole_maintenance:.0f} mg IV q12h** (sau 48h: q24h).
        - Nếu đang lọc máu: chuyển **q4h** trong lọc.
        """
    )

    st.warning(
        """
        **Nếu không có fomepizole → dùng ethanol (ít ưu tiên, khó kiểm soát):**
        - Liều nạp: 8–10 mL/kg ethanol 10% IV.
        - Duy trì: 1–2 mL/kg/giờ (tăng 50% nếu bệnh nhân nghiện rượu).
        - Theo dõi đường huyết, ý thức, hít sặc.
        """
    )

    st.markdown("---")

    # ========== SECTION 4: CHỈ ĐỊNH LỌC MÁU ========== #
    st.markdown("### 🩸 Chỉ Định Lọc Máu (Hemodialysis)")
    st.info(
        """
        **Chỉ định mạnh:**
        - pH <7.25 hoặc HCO₃⁻ <15 mEq/L.
        - Tổn thương thị giác (methanol) hoặc suy thận cấp/thiểu niệu (ethylene glycol).
        - Nồng độ methanol/EG ≥50 mg/dL (hoặc ≥20 mg/dL + triệu chứng/toan).
        - Khoảng trống anion rất cao, lactate tăng, hoặc không đáp ứng điều trị ban đầu.
        """
    )

    st.markdown("---")

    # ========== SECTION 5: BICARBONATE & HỖ TRỢ ========== #
    st.markdown("### 🛠️ Điều Trị Hỗ Trợ")
    st.markdown(
        """
        - **NaHCO₃:** Nếu pH <7.30 hoặc HCO₃⁻ <18; bolus 1–2 mEq/kg, sau đó truyền duy trì, mục tiêu pH >7.30.
        - **Thiamine 100 mg IV** + **Pyridoxine 50 mg IV** (ethylene glycol) để chuyển hóa ít độc hơn.
        - **Folate 50 mg IV q6h** (methanol) giúp chuyển hóa formate.
        - **Hỗ trợ hô hấp/tuần hoàn:** Oxy, truyền dịch, vận mạch khi cần.
        - **Không than hoạt** (không hiệu quả), tránh gây nôn.
        """
    )

    st.markdown("---")

    # ========== SECTION 6: THEO DÕI ========== #
    st.markdown("### 📈 Theo Dõi")
    st.info(
        """
        - Khí máu, HCO₃⁻, lactate, anion gap mỗi 2–4 giờ.
        - Điện giải, calci (ethylene glycol gây hạ Ca²⁺), creatinine mỗi 4–6 giờ.
        - Đường huyết khi dùng ethanol/insulin.
        - Thị lực (methanol), nước tiểu/tinh thể oxalat (ethylene glycol).
        - Điều chỉnh liều fomepizole khi lọc máu (q4h).
        """
    )

    st.markdown("---")

    # ========== SECTION 7: ĐỐI TƯỢNG ĐẶC BIỆT ========== #
    st.markdown("### 👥 Đối Tượng Đặc Biệt")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            """
            **Có thai:** Fomepizole an toàn tương đối; lọc máu khi có chỉ định để bảo vệ mẹ & thai.

            **Trẻ em:** Dùng cùng liều mg/kg; theo dõi đường huyết sát nếu dùng ethanol.
            """
        )
    with col2:
        st.markdown(
            """
            **Suy thận/suy gan:** Ưu tiên fomepizole; lọc máu sớm với ethylene glycol.

            **Nghiện rượu:** Tăng nhu cầu ethanol duy trì; ưu tiên chuyển sang fomepizole nếu có.
            """
        )

    st.markdown("---")

    # ========== SECTION 8: TÀI LIỆU THAM KHẢO ========== #
    render_references_section(get_references("Toxic Alcohol Poisoning"))


