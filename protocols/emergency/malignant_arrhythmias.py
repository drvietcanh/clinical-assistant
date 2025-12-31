"""
Malignant Arrhythmias Protocol (VF/pulseless VT, Torsades de Pointes, unstable VT)
AHA/ESC ACLS guidance
Immediate defibrillation, magnesium, antiarrhythmics, and reversible causes
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section
from components.evidence_badge import (
    render_evidence_badge,
    render_evidence_summary,
    Citation
)


def render():
    """Malignant Arrhythmias Protocol"""
    st.subheader("⚡ Rối loạn Nhịp Nguy Hiểm (VF/pVT/Torsades)")
    st.caption("AHA ACLS 2020/2022, ESC 2022 – Sốc điện sớm, MgSO4, tìm Hs & Ts")
    
    # Evidence summary
    render_evidence_summary(
        last_reviewed="2024-11-01",
        last_updated="2024-11-01",
        version="2024",
        guideline_source="AHA ACLS 2020/2022, ESC 2022"
    )

    st.error(
        """
        **⚠️ VF/pVT = CẤP CỨU HỒI SỨC**
        - Tử vong nếu không sốc trong phút đầu.
        - Ưu tiên: **CPR chất lượng + Defibrillation sớm + Adrenaline + Amiodarone**.
        - Torsades de Pointes: **MgSO₄ tĩnh mạch** + Sốc nếu không mạch.
        """
    )

    st.markdown("---")

    # ========== SECTION 1: PHÂN LOẠI TÌNH HUỐNG ========== #
    scenario = st.radio(
        "**Tình huống:**",
        [
            "VF / pVT (không mạch)",
            "Torsades de Pointes không mạch",
            "VT có mạch nhưng huyết động không ổn (unstable VT)",
            "VT có mạch, ổn định (stable VT/monomorphic)"
        ],
        key="malig_arrhythmia_scenario",
    )

    st.markdown("---")

    # ========== SECTION 2: PHÁC ĐỒ CHÍNH ========== #
    if "VF" in scenario or "pVT" in scenario:
        render_vf_pvt()
    elif "Torsades" in scenario:
        render_tdp()
    elif "không ổn" in scenario:
        render_unstable_vt()
    else:
        render_stable_vt()

    st.markdown("---")

    # ========== SECTION 3: Hs & Ts ========== #
    st.markdown("### 🧭 Tìm và xử trí nguyên nhân (Hs & Ts)")
    st.caption("Hypoxia, Hypovolemia, Hydrogen ion (toan), Hypo/HyperK, Hypothermia; Tension PTX, Tamponade, Toxins, Thrombosis (coronary/pulmonary)")

    st.markdown("---")

    # ========== SECTION 4: TÀI LIỆU THAM KHẢO ========== #
    render_references_section(get_references("Malignant Arrhythmias"))


def render_vf_pvt():
    st.markdown("### 🔁 VF/pVT – ACLS")
    st.info(
        """
        1) **CPR ngay**, Oxy, monitor/defib.
        2) **Sốc biphasic** 200J (hoặc theo hãng), sau đó CPR 2 phút.
        3) **Adrenaline 1 mg IV q3-5 phút** bắt đầu sau sốc thứ 2.
        4) **Amiodarone 300 mg IV bolus** sau sốc thứ 3; nhắc 150 mg nếu cần.
        5) Xem xét **lidocaine** nếu không có amiodarone.
        6) Tiếp tục chu kỳ CPR 2 phút + sốc + thuốc.
        """
    )


def render_tdp():
    st.markdown("### 🌀 Torsades de Pointes")
    st.info(
        """
        - Nếu **không mạch**: xử trí như VF/pVT + **MgSO₄ 2 g IV** bolus (10-20 mL D5W).
        - Nếu có mạch nhưng không ổn: **Cardioversion đồng bộ** + MgSO₄.
        - **Tránh** amiodarone (có thể kéo dài QT); có thể dùng lidocaine.
        - Cân nhắc tăng nhịp (isoproterenol hoặc pacing tạm thời) nếu nhịp chậm gây QT dài.
        """
    )


def render_unstable_vt():
    st.markdown("### 🚨 VT có mạch, huyết động không ổn")
    st.error("Cardioversion đồng bộ ngay.")
    st.markdown(
        """
        - Bắt đầu 100J biphasic, tăng dần.
        - Nếu thất bại nhiều lần → chuyển không đồng bộ/sốc nếu thoái hóa VF/pVT.
        - Tiền mê/giảm đau nhanh nếu có thể.
        """
    )


def render_stable_vt():
    st.markdown("### ✅ VT ổn định (monomorphic)")
    st.info(
        """
        - **Amiodarone:** 150 mg IV trong 10 phút, lặp lại nếu cần (tối đa 2.2 g/24h).
        - **Procainamide:** 20-50 mg/phút đến 17 mg/kg, tránh nếu suy tim nặng/QT dài.
        - **Sotalol:** 1.5 mg/kg trong 5 phút (tránh QT dài/suy thận).
        - Theo dõi QT, HA, chuyển nhịp nếu xấu đi.
        """
    )


