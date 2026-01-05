"""
ANCA Vasculitis Glomerulonephritis Protocol
KDIGO 2021 Glomerular Diseases Guideline
Quản lý viêm mạch ANCA với tổn thương thận - Nguyên nhân quan trọng của RPGN
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """ANCA Vasculitis Protocol - KDIGO 2021"""
    st.subheader("🔬 ANCA Vasculitis Glomerulonephritis")
    st.caption("KDIGO 2021 Glomerular Diseases – GPA, MPA, EGPA; Induction & Maintenance")

    st.info(
        """**Điểm chính:**
        - ANCA vasculitis là nguyên nhân quan trọng của viêm cầu thận tiến triển nhanh (RPGN).
        - Phân loại: GPA (Granulomatosis with Polyangiitis), MPA (Microscopic Polyangiitis), EGPA (Eosinophilic Granulomatosis with Polyangiitis).
        - Điều trị chia 2 pha: **Induction (3-6 tháng)** và **Maintenance (≥18-24 tháng)**.
        - Thuốc chính: Corticosteroid, Rituximab, Cyclophosphamide, Azathioprine.
        - Mục tiêu: Đạt lui bệnh, ngăn tái phát, bảo tồn chức năng thận.
        """
    )

    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        egfr = st.number_input(
            "eGFR (mL/min/1.73m²)",
            min_value=5.0,
            max_value=150.0,
            value=30.0,
            step=1.0,
            key="anca_egfr",
        )
        proteinuria_24h = st.number_input(
            "Protein niệu 24h (g/24h)",
            min_value=0.0,
            max_value=20.0,
            value=1.0,
            step=0.1,
            key="anca_proteinuria",
        )
        anca_type = st.selectbox(
            "Loại ANCA:",
            ["Chưa có", "p-ANCA (MPO-ANCA)", "c-ANCA (PR3-ANCA)", "Cả hai"],
            key="anca_type",
        )
    with col2:
        creatinine = st.number_input(
            "Creatinine (μmol/L)",
            min_value=50.0,
            max_value=1000.0,
            value=200.0,
            step=10.0,
            key="anca_creatinine",
        )
        sbp = st.number_input(
            "Huyết áp tâm thu (mmHg)",
            min_value=80.0,
            max_value=250.0,
            value=140.0,
            step=5.0,
            key="anca_sbp",
        )
        vasculitis_type = st.selectbox(
            "Loại viêm mạch:",
            ["Chưa xác định", "GPA (Granulomatosis with Polyangiitis)", "MPA (Microscopic Polyangiitis)", "EGPA (Eosinophilic Granulomatosis)"],
            key="anca_vasculitis_type",
        )

    has_pulmonary = st.checkbox("Có tổn thương phổi (ho ra máu, viêm phế nang xuất huyết)?", key="anca_pulmonary")
    needs_dialysis = st.checkbox("Cần lọc máu?", key="anca_dialysis")

    st.markdown("---")

    scenario = st.radio(
        "Chọn tình huống lâm sàng:",
        [
            "🔍 Chẩn đoán & Phân loại",
            "💉 Induction therapy (cảm ứng)",
            "💊 Maintenance therapy (duy trì)",
            "📊 Theo dõi & Tái phát",
        ],
        key="anca_scenario",
    )

    st.markdown("---")

    if "Chẩn đoán" in scenario:
        render_diagnosis(egfr, creatinine, proteinuria_24h, anca_type, vasculitis_type, has_pulmonary)
    elif "Induction" in scenario:
        render_induction(egfr, creatinine, has_pulmonary, needs_dialysis)
    elif "Maintenance" in scenario:
        render_maintenance()
    else:
        render_monitoring(egfr, creatinine, proteinuria_24h)

    st.markdown("---")
    references = get_references("ANCA_Vasculitis")
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
        1. **KDIGO 2021 Clinical Practice Guideline for Glomerular Diseases - ANCA Vasculitis**
           - Kidney Int. 2021;100(4S):S1-S276
           - Website: https://kdigo.org/guidelines/glomerular-diseases/
        
        2. **EULAR/ERA-EDTA recommendations for ANCA-associated vasculitis**
           - Ann Rheum Dis. 2016;75(9):1583-1594
        
        3. **UpToDate:** ANCA-associated vasculitis: Treatment and prognosis
           - Last updated: 2025
        """)


def render_diagnosis(egfr: float, creatinine: float, proteinuria_24h: float, anca_type: str, vasculitis_type: str, has_pulmonary: bool) -> None:
    """Diagnosis and classification"""
    st.success("## 🔍 Chẩn đoán & Phân loại")

    st.markdown("### Khi nào nghi ngờ ANCA Vasculitis?")
    st.info(
        """**Nghi ngờ khi có:**
        - Suy thận cấp hoặc tiến triển nhanh (RPGN)
        - Hồng cầu niệu, protein niệu
        - Triệu chứng hệ thống: sốt, mệt mỏi, sụt cân
        - Tổn thương đa cơ quan: phổi, da, khớp, thần kinh
        """
    )

    st.markdown("---")
    st.markdown("### Xét nghiệm Chẩn đoán")

    st.info(
        """**ANCA:**
        - **p-ANCA (MPO-ANCA):** Thường gặp trong MPA và EGPA
        - **c-ANCA (PR3-ANCA):** Thường gặp trong GPA
        - Độ nhạy: 80-90%, độ đặc hiệu: 90-95%
        
        **Xét nghiệm khác:**
        - Creatinine, eGFR (thường giảm nhanh)
        - Protein niệu, hồng cầu niệu
        - Công thức máu (thiếu máu, tăng bạch cầu)
        - CRP, ESR tăng cao
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
        elif egfr >= 15:
            st.error(f"**eGFR: {egfr} mL/min/1.73m²** – Giảm nặng")
        else:
            st.error(f"**eGFR: {egfr} mL/min/1.73m²** – Suy thận giai đoạn cuối")

    with col2:
        if creatinine < 200:
            st.info(f"**Creatinine: {creatinine} μmol/L** – Bình thường/tăng nhẹ")
        elif creatinine < 500:
            st.warning(f"**Creatinine: {creatinine} μmol/L** – Tăng trung bình")
        else:
            st.error(f"**Creatinine: {creatinine} μmol/L** – Tăng nặng (cân nhắc plasma exchange)")

    with col3:
        if proteinuria_24h < 0.5:
            st.info(f"**Protein niệu: {proteinuria_24h} g/24h** – Nhẹ")
        elif proteinuria_24h < 1.0:
            st.warning(f"**Protein niệu: {proteinuria_24h} g/24h** – Trung bình")
        else:
            st.error(f"**Protein niệu: {proteinuria_24h} g/24h** – Nặng")

    st.markdown("---")
    st.markdown("### Chỉ định Sinh thiết Thận")

    st.warning(
        """**Chỉ định sinh thiết khi:**
        - Suy thận cấp hoặc tiến triển nhanh
        - Protein niệu hoặc hồng cầu niệu
        - Nghi ngờ ANCA vasculitis
        
        **Đặc điểm mô bệnh học:**
        - Viêm cầu thận tiến triển nhanh (RPGN)
        - Hoại tử cầu thận
        - Trụ tế bào (crescents)
        - Thiếu lắng đọng phức hợp miễn dịch (pauci-immune)
        """
    )


def render_induction(egfr: float, creatinine: float, has_pulmonary: bool, needs_dialysis: bool) -> None:
    """Induction therapy"""
    st.error("## 💉 Induction Therapy (Cảm ứng)")

    st.markdown("### Phác đồ Chuẩn")

    st.success(
        """**Corticosteroid:**
        - **Methylprednisolone:** 500-1000 mg tĩnh mạch × 1-3 ngày
        - Sau đó **Prednisone:** 1 mg/kg/ngày (tối đa 60-80 mg) × 4-6 tuần
        - Giảm dần liều trong 3-6 tháng
        """
    )

    st.markdown("---")
    st.markdown("### Thuốc Ức chế Miễn dịch")

    st.info(
        """**Phương án 1: Rituximab (ƯU TIÊN - KDIGO 2021):**
        - **Rituximab:** 375 mg/m²/tuần × 4 tuần
        - Hoặc: 1000 mg × 2 liều cách nhau 2 tuần
        - **Ưu điểm:** Hiệu quả tương đương cyclophosphamide, ít độc tính hơn
        - **Chỉ định:** Bệnh nhân mới chẩn đoán hoặc tái phát
        
        **Phương án 2: Cyclophosphamide:**
        - **Cyclophosphamide:** 15 mg/kg tĩnh mạch mỗi 2-3 tuần × 3-6 liều
        - Hoặc: 1.5-2 mg/kg/ngày đường uống × 3-6 tháng
        - **Lưu ý:** Nguy cơ độc tính cao (nhiễm trùng, giảm bạch cầu, vô sinh)
        """
    )

    st.markdown("---")
    st.markdown("### Plasma Exchange (Plasmapheresis)")

    needs_plasma_exchange = (creatinine > 500) or needs_dialysis or has_pulmonary

    if needs_plasma_exchange:
        st.error(
            """**CÓ CHỈ ĐỊNH Plasma Exchange:**
            - Suy thận cấp nặng (creatinine >500 μmol/L hoặc cần lọc máu)
            - Xuất huyết phổi nặng
            
            **Phác đồ:**
            - 7 lần trong 14 ngày, mỗi lần thay 60 mL/kg
            - Kết hợp với Rituximab/Cyclophosphamide + Corticosteroid
            """
        )
    else:
        st.info(
            """**Chưa có chỉ định Plasma Exchange:**
            - Chỉ định khi creatinine >500 μmol/L, cần lọc máu, hoặc xuất huyết phổi nặng
            """
        )

    st.markdown("---")
    st.markdown("### Lưu ý An toàn")

    st.warning(
        """**Dự phòng và theo dõi:**
        - Dự phòng nhiễm trùng cơ hội (PCP) nếu dùng liều corticoid cao + thuốc ức chế miễn dịch
        - Tiêm chủng trước khi dùng Rituximab/Cyclophosphamide nếu có thể
        - Theo dõi: công thức máu, men gan, chức năng thận
        - Tư vấn sinh sản: Cyclophosphamide có nguy cơ gây vô sinh
        """
    )


def render_maintenance() -> None:
    """Maintenance therapy"""
    st.warning("## 💊 Maintenance Therapy (Duy trì)")

    st.info(
        """**Sau khi đạt lui bệnh:**
        - Tiếp tục thuốc duy trì ít nhất **18-24 tháng**
        
        **Thuốc duy trì:**
        - **Azathioprine:** 1.5-2 mg/kg/ngày
        - Hoặc **Mycophenolate Mofetil:** 1-2 g/ngày
        - Hoặc **Rituximab:** 500-1000 mg mỗi 6 tháng × 2 năm
        
        **Corticosteroid:**
        - Giảm dần đến liều thấp (5-7.5 mg/ngày)
        - Cố gắng dừng sau 12-18 tháng
        
        **Tiêu chuẩn lui bệnh:**
        - Không có triệu chứng lâm sàng
        - eGFR ổn định hoặc cải thiện
        - ANCA âm tính hoặc giảm đáng kể
        """
    )


def render_monitoring(egfr: float, creatinine: float, proteinuria_24h: float) -> None:
    """Monitoring and relapse"""
    st.success("## 📊 Theo dõi & Tái phát")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Lịch theo dõi")
        st.info(
            """**Tần suất:**
            - Mỗi 1-2 tuần trong induction
            - Mỗi 1-3 tháng trong maintenance
            
            **Đánh giá:**
            - Triệu chứng lâm sàng
            - Chức năng thận (creatinine, eGFR)
            - ANCA titer
            - Công thức máu, men gan
            """
        )

    with col2:
        st.markdown("### Dấu hiệu tái phát")
        st.error(
            """**Cảnh báo:**
            - Triệu chứng mới xuất hiện
            - eGFR giảm không giải thích được
            - ANCA titer tăng
            - Protein niệu hoặc hồng cầu niệu tăng
            
            **Xử trí:**
            - Đánh giá lại mức độ bệnh
            - Cân nhắc tăng liều hoặc đổi phác đồ
            - Có thể cần induction lại
            """
        )

    st.markdown("---")
    st.markdown("### Tình huống đặc biệt")

    st.info(
        """**Bệnh nhân cao tuổi:**
        - Giảm liều cyclophosphamide
        - Ưu tiên Rituximab (ít độc tính hơn)
        - Theo dõi nhiễm trùng chặt chẽ
        
        **Phụ nữ mang thai:**
        - Tránh cyclophosphamide, mycophenolate
        - Ưu tiên: Azathioprine + corticoid liều thấp
        - Rituximab: Cân nhắc cẩn thận
        
        **Bệnh nhân nhiễm trùng:**
        - Điều trị nhiễm trùng trước khi bắt đầu ức chế miễn dịch
        - Dự phòng nhiễm trùng cơ hội (PCP, nấm)
        """
    )
