"""
Lupus Nephritis Protocol
KDIGO 2021 Glomerular Diseases Guideline
Quản lý viêm thận lupus (LN) – biến chứng nặng của SLE
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Lupus Nephritis Protocol - KDIGO 2021"""
    st.subheader("🔬 Lupus Nephritis (Viêm Thận Lupus)")
    st.caption("KDIGO 2021 Glomerular Diseases – Class III, IV, V; Induction & Maintenance")

    st.info(
        """**Điểm chính:**
        - Lupus Nephritis là biến chứng nặng của lupus ban đỏ hệ thống (SLE).
        - Điều trị chia 2 pha: **Induction (3–6 tháng)** và **Maintenance (≥3 năm)**.
        - Thuốc chính: Corticosteroid, Mycophenolate Mofetil (MMF), Cyclophosphamide ± Rituximab.
        - Mục tiêu: Bảo tồn chức năng thận, giảm protein niệu, hạn chế độc tính thuốc.
        """
    )

    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        egfr = st.number_input(
            "eGFR (mL/min/1.73m²)",
            min_value=5.0,
            max_value=150.0,
            value=60.0,
            step=1.0,
            key="ln_egfr",
        )
        proteinuria_24h = st.number_input(
            "Protein niệu 24h (g/24h)",
            min_value=0.0,
            max_value=20.0,
            value=1.5,
            step=0.1,
            key="ln_proteinuria",
        )
    with col2:
        acr = st.number_input(
            "ACR (mg/g)",
            min_value=0.0,
            max_value=5000.0,
            value=800.0,
            step=50.0,
            key="ln_acr",
        )
        sbp = st.number_input(
            "Huyết áp tâm thu (mmHg)",
            min_value=80.0,
            max_value=250.0,
            value=140.0,
            step=5.0,
            key="ln_sbp",
        )

    ln_class = st.selectbox(
        "ISN/RPS class (nếu có sinh thiết):",
        [
            "Chưa sinh thiết",
            "Class II (Mesangial proliferative)",
            "Class III (Focal)",
            "Class IV (Diffuse)",
            "Class V (Membranous)",
            "Class III+V",
            "Class IV+V",
        ],
        key="ln_class",
    )

    st.markdown("---")

    scenario = st.radio(
        "Chọn tình huống lâm sàng:",
        [
            "🔍 Chẩn đoán & Chỉ định sinh thiết",
            "💉 Induction therapy (cảm ứng)",
            "💊 Maintenance therapy (duy trì)",
            "📊 Theo dõi & Đáp ứng",
        ],
        key="ln_scenario",
    )

    st.markdown("---")

    if "Chẩn đoán" in scenario:
        render_diagnosis(egfr, proteinuria_24h, acr)
    elif "Induction" in scenario:
        render_induction(egfr, proteinuria_24h, acr, ln_class)
    elif "Maintenance" in scenario:
        render_maintenance()
    else:
        render_monitoring(egfr, proteinuria_24h, acr)

    st.markdown("---")
    references = get_references("Lupus_Nephritis")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2026-01-15",
            show_evidence_level=True,
            show_links=True,
        )
    else:
        st.markdown("### 📚 Tài liệu tham khảo")
        st.markdown("""
        1. **KDIGO 2021 Clinical Practice Guideline for the Management of Glomerular Diseases – Lupus Nephritis**
           - Kidney Int. 2021;100(4S):S1-S276
           - Website: https://kdigo.org/guidelines/glomerular-diseases/
        
        2. **EULAR/ERA-EDTA recommendations for the management of lupus nephritis**
           - Ann Rheum Dis. 2019;78(6):736-745
        """)


def render_diagnosis(egfr: float, proteinuria_24h: float, acr: float) -> None:
    """Diagnosis and biopsy indication"""
    st.success("## 🔍 Chẩn đoán & Chỉ định Sinh thiết")

    st.markdown("### Khi nào nghi ngờ Lupus Nephritis?")
    st.info(
        """**Ở bệnh nhân SLE, nghi ngờ LN khi có:**
        - Protein niệu ≥0.5 g/24h (ACR ≥500 mg/g)
        - Hồng cầu niệu, trụ hồng cầu
        - eGFR giảm không giải thích được
        - Tăng huyết áp mới hoặc xấu đi
        """
    )

    st.markdown("---")
    st.markdown("### Đánh giá hiện tại")
    col1, col2, col3 = st.columns(3)

    with col1:
        if egfr >= 60:
            st.success(f"**eGFR: {egfr} mL/min/1.73m²** – Bình thường/nhẹ")
        elif egfr >= 30:
            st.warning(f"**eGFR: {egfr} mL/min/1.73m²** – Giảm trung bình")
        else:
            st.error(f"**eGFR: {egfr} mL/min/1.73m²** – Giảm nặng")

    with col2:
        if proteinuria_24h < 0.5:
            st.info(f"**Protein niệu: {proteinuria_24h} g/24h** – <0.5 g/24h")
        elif proteinuria_24h < 1.0:
            st.warning(f"**Protein niệu: {proteinuria_24h} g/24h** – 0.5–1 g/24h")
        elif proteinuria_24h < 3.5:
            st.error(f"**Protein niệu: {proteinuria_24h} g/24h** – >1 g/24h (nặng)")
        else:
            st.error(f"**Protein niệu: {proteinuria_24h} g/24h** – Hội chứng thận hư")

    with col3:
        if acr < 500:
            st.info(f"**ACR: {acr} mg/g** – <500 mg/g")
        else:
            st.error(f"**ACR: {acr} mg/g** – ≥500 mg/g (gợi ý LN hoạt động)")

    st.markdown("---")
    st.markdown("### Chỉ định sinh thiết (KDIGO 2021)")

    indication = (proteinuria_24h >= 0.5) or (acr >= 500)
    if indication:
        st.error(
            "**Có chỉ định sinh thiết thận:** Protein niệu ≥0.5 g/24h hoặc ACR ≥500 mg/g ở bệnh nhân SLE."
        )
    else:
        st.warning(
            "Protein niệu <0.5 g/24h: có thể theo dõi sát, nhưng nếu có hồng cầu niệu hoạt tính hoặc eGFR giảm thì vẫn cân nhắc sinh thiết."
        )

    st.info(
        """**Mục tiêu sinh thiết:**
        - Xác định lớp (class) theo ISN/RPS (III, IV, V).
        - Đánh giá mức độ hoạt động vs mạn tính.
        - Hướng dẫn lựa chọn phác đồ induction vs maintenance.
        """
    )


def render_induction(egfr: float, proteinuria_24h: float, acr: float, ln_class: str) -> None:
    """Induction therapy"""
    st.error("## 💉 Induction Therapy (Cảm ứng)")

    st.markdown("### Xác định đối tượng cần induction tích cực")
    high_risk = (proteinuria_24h >= 1.0) or (acr >= 1000) or (egfr < 60)
    if high_risk:
        st.error(
            "Bệnh nhân **nguy cơ cao** (protein niệu ≥1 g/24h, ACR ≥1000 mg/g hoặc eGFR <60) – cần induction tích cực."
        )
    else:
        st.warning(
            "Nguy cơ trung bình/thấp – vẫn cần đánh giá sinh thiết và cân nhắc induction theo class."
        )

    st.markdown("---")
    st.markdown("### Lựa chọn phác đồ theo class")

    if any(c in ln_class for c in ["Class III", "Class IV", "Class III+V", "Class IV+V"]):
        st.success(
            """**Class III/IV (± V) – phác đồ ưu tiên:**

            **Phương án 1: MMF + Corticoid**
            - MMF: 2–3 g/ngày, chia 2 lần.
            - Corticoid:
              - Methylprednisolone 500–1000 mg TM × 1–3 ngày.
              - Sau đó Prednisone 0.5–0.75 mg/kg/ngày (tối đa 40–60 mg), giảm dần 3–6 tháng.

            **Phương án 2: Cyclophosphamide + Corticoid (Euro-Lupus/NIH)**
            - Euro-Lupus: Cyclophosphamide 500 mg TM mỗi 2 tuần × 6 liều.
            - NIH: 0.5–1 g/m² mỗi tháng × 6 liều (cân nhắc độc tính).

            **Cân nhắc Rituximab:**
            - Tái phát nhiều lần hoặc kháng trị.
            """
        )
    elif "Class V" in ln_class:
        st.info(
            """**Class V đơn thuần (membranous):**
            - Nếu protein niệu >1 g/24h hoặc hội chứng thận hư:
              - MMF 2–3 g/ngày + corticoid liều trung bình.
            - Nếu protein niệu nhẹ (<1 g/24h), eGFR ổn định:
              - Điều trị bảo tồn (ACEi/ARB, kiểm soát HA, điều trị SLE toàn thân).
            """
        )
    else:
        st.info(
            "Chưa có sinh thiết hoặc class II: thường không cần induction nặng, ưu tiên điều trị SLE toàn thân và theo dõi sát."
        )

    st.markdown("---")
    st.markdown("### Lưu ý an toàn và dự phòng")
    st.warning(
        """**Dự phòng và theo dõi:**
        - Dự phòng nhiễm trùng cơ hội (PCP) nếu dùng liều corticoid cao + thuốc ức chế miễn dịch.
        - Tiêm chủng trước khi dùng Rituximab/Cyclophosphamide nếu có thể.
        - Theo dõi: công thức máu, men gan, chức năng thận.
        - Tư vấn sinh sản: Cyclophosphamide có nguy cơ gây vô sinh.
        """
    )


def render_maintenance() -> None:
    """Maintenance therapy"""
    st.warning("## 💊 Maintenance Therapy (Duy trì)")

    st.info(
        """**Sau khi đạt đáp ứng (hoàn toàn hoặc một phần):**
        - Tiếp tục thuốc duy trì ít nhất **3 năm**.

        **Thuốc duy trì:**
        - MMF: 1–2 g/ngày.
        - Hoặc Azathioprine: 1.5–2 mg/kg/ngày (nếu MMF không dung nạp hoặc phụ nữ muốn mang thai).

        **Corticoid:**
        - Giảm dần đến liều thấp (5–7.5 mg/ngày) và cân nhắc dừng nếu ổn định lâu dài.

        **Theo dõi:**
        - Protein niệu, eGFR mỗi 3–6 tháng.
        - C3, C4, anti-dsDNA (nếu có điều kiện).
        """
    )


def render_monitoring(egfr: float, proteinuria_24h: float, acr: float) -> None:
    """Monitoring and response"""
    st.success("## 📊 Theo dõi & Đáp ứng")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Lịch theo dõi")
        st.info(
            """**Induction (3–6 tháng đầu):**
            - 4–8 tuần/lần: Creatinine/eGFR, protein niệu (UPCR/24h), công thức máu, men gan.

            **Maintenance:**
            - 3–6 tháng/lần: như trên.
            """
        )

    with col2:
        st.markdown("### Đánh giá đáp ứng")
        st.success(
            """**Đáp ứng hoàn toàn:**
            - Protein niệu <0.5–0.7 g/24h.
            - eGFR ổn định/bình thường.

            **Đáp ứng một phần:**
            - Protein niệu giảm ≥50% nhưng vẫn >0.7 g/24h.

            **Không đáp ứng/kháng trị:**
            - Không cải thiện protein niệu hoặc eGFR sau 6–12 tháng.
            - Cân nhắc sinh thiết lại, đổi phác đồ, thêm Rituximab.
            """
        )

    st.markdown("---")
    st.markdown("### Dấu hiệu cảnh báo & tái phát")
    st.error(
        """**Cần đánh giá lại sớm khi:**
        - Protein niệu tăng lại >1 g/24h.
        - eGFR giảm >30% so với nền.
        - Xuất hiện lại hồng cầu niệu hoạt tính.
        """
    )

    st.markdown("---")
    st.markdown("### Điều trị bảo tồn song song")
    st.info(
        """- ACEi/ARB nếu protein niệu ≥0.5 g/24h hoặc tăng HA.
        - Kiểm soát HA <130/80 mmHg (xem protocol Quản lý Huyết áp trong CKD).
        - Statin nếu rối loạn lipid.
        - Hydroxychloroquine cho hầu hết bệnh nhân SLE nếu không chống chỉ định.
        """
    )
