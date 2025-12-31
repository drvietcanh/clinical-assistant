"""
Traumatic Brain Injury (TBI) Protocol - initial ED/ICU management
Brain Trauma Foundation 4th edition guidance
Focus on airway, CPP, ICP, CT indications, and transfer criteria
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
    """Traumatic Brain Injury Protocol"""
    st.subheader("🧠 Chấn thương Sọ Não (TBI) – Xử trí ban đầu")
    st.caption("Brain Trauma Foundation 4th ed. – ABC, CPP/ICP, chỉ định CT và chuyển tuyến")
    
    # Evidence summary
    render_evidence_summary(
        last_reviewed="2023-09-01",
        last_updated="2023-09-01",
        version="2023",
        guideline_source="Brain Trauma Foundation 4th ed."
    )

    st.error(
        """
        **⚠️ TBI nguy cơ tụt huyết áp/thiếu oxy → tăng tử vong**
        - Mục tiêu: tránh tụt HA (SBP <100-110) và SpO₂ <94%.
        - Đánh giá nhanh GCS, đồng tử, dấu hiệu thoát vị.
        """
    )

    st.markdown("---")

    # ========== SECTION 1: PHÂN TẦNG BAN ĐẦU ========== #
    gcs = st.slider("Điểm GCS", min_value=3, max_value=15, value=14, step=1)
    st.info(
        f"""
        **GCS hiện tại: {gcs}**
        - Nhẹ: 13–15
        - Trung bình: 9–12
        - Nặng: ≤8 (cần bảo vệ đường thở)
        """
    )

    st.markdown("---")

    # ========== SECTION 2: ABC & HUYẾT ĐỘNG ========== #
    st.markdown("### 🏥 ABC & Huyết động")
    st.info(
        """
        - **Airway:** Đặt NKQ nếu GCS ≤8, không bảo vệ được đường thở, hoặc cần kiểm soát CO₂.
        - **Breathing:** Mục tiêu SpO₂ ≥94%, PaCO₂ 35–40 mmHg (tránh tăng thông khí thường quy).
        - **Circulation:** Tránh hạ huyết áp; mục tiêu SBP ≥110 (18-49 tuổi), ≥120 (50-69), ≥100 (<18).
        - Dịch tinh thể đẳng trương; vận mạch nếu cần (norepinephrine).
        """
    )

    st.markdown("---")

    # ========== SECTION 3: ICP/CPP ========== #
    st.markdown("### 🧠 ICP/CPP")
    st.info(
        """
        - Nghi ngờ tăng ICP: GCS giảm, đồng tử giãn, tam chứng Cushing, nôn, tư thế mất não.
        - Biện pháp tạm thời: nâng đầu 30°, cổ thẳng, giảm kích thích; mannitol 0.25–1 g/kg IV bolus **hoặc** hypertonic saline (3% 2 mL/kg) nếu tụt thần kinh.
        - Mục tiêu CPP: 60–70 mmHg (CPP = MAP - ICP). Nếu chưa đặt đo ICP, dùng surrogate: SBP/triệu chứng.
        """
    )

    st.markdown("---")

    # ========== SECTION 4: CHỈ ĐỊNH CT NÃO ========== #
    st.markdown("### 📸 Chỉ định CT Scan Não")
    st.markdown(
        """
        - GCS <15 sau 2 giờ.
        - Nghi vỡ nền sọ/ dấu hiệu sọ (Battle, raccoon eyes, rò dịch).
        - Hai lần nôn, co giật sau chấn thương, thiếu hụt thần kinh khu trú.
        - Cơ chế nặng: té cao >1 m, tai nạn tốc độ cao, bị đánh vào đầu bởi vật tốc độ.
        - Dùng kháng đông/kháng kết tập tiểu cầu hoặc INR cao.
        """
    )

    st.markdown("---")

    # ========== SECTION 5: CHỈ ĐỊNH CHUYỂN PHẪU THUẬT/ICU ========== #
    st.markdown("### 🏥 Chuyển phẫu thuật/ICU")
    st.info(
        """
        - Tụ máu ngoài/dưới màng cứng dày >10 mm, dịch chuyển đường giữa >5 mm.
        - Giảm GCS ≥2 điểm, đồng tử giãn một bên, dấu tăng ICP.
        - Vỡ sọ lún >10 mm, rò dịch não tủy.
        - Cần đặt dẫn lưu/monitor ICP.
        """
    )

    st.markdown("---")

    # ========== SECTION 6: THUỐC & DỰ PHÒNG ========== #
    st.markdown("### 💊 Thuốc & Dự phòng")
    st.markdown(
        """
        - **Co giật sớm (<7 ngày):** Levetiracetam 1 g IV nạp, 500–1,000 mg q12h.
        - **Giảm đau/ an thần:** tránh hạ HA; ưu tiên fentanyl/propofol có kiểm soát huyết áp.
        - **Không dùng steroid** trong TBI.
        - **Dự phòng DVT:** heparin/LMWH khi an toàn, mang tất áp lực; trì hoãn nếu nguy cơ chảy máu cao.
        """
    )

    st.markdown("---")

    # ========== SECTION 7: THEO DÕI ========== #
    st.markdown("### 📈 Theo dõi")
    st.info(
        """
        - GCS/đồng tử mỗi 1 giờ (nặng), sinh hiệu liên tục.
        - Xét nghiệm: điện giải, đường huyết, ABG; lặp CT nếu xấu đi.
        - Tránh sốt, duy trì natri bình thường (tránh hạ natri).
        """
    )

    st.markdown("---")

    render_references_section(get_references("Traumatic Brain Injury"))


