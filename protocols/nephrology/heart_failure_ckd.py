"""
Heart Failure in CKD Protocol
KDIGO 2025
Quản lý suy tim ở bệnh nhân CKD - Guideline đầu tiên của KDIGO về chủ đề này
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Heart Failure in CKD Protocol - KDIGO 2025"""
    st.subheader("❤️ Suy Tim Trong CKD (Heart Failure in CKD)")
    st.caption("KDIGO 2025 Clinical Practice Guideline for Heart Failure in CKD - Guideline đầu tiên")
    
    st.info("""
    **KDIGO 2025 - Guideline đầu tiên về Suy tim trong CKD:**
    - 40-50% bệnh nhân suy tim có CKD
    - 30-40% bệnh nhân CKD có suy tim
    - Tỷ lệ tử vong và nhập viện tăng cao khi có cả hai bệnh
    
    **Điểm chính:**
    - Phối hợp giữa Tim mạch và Thận học
    - Điều chỉnh liều thuốc theo eGFR
    - SGLT2 inhibitors là thuốc nền tảng mới
    """)
    
    st.markdown("---")
    
    # Patient information inputs
    col1, col2 = st.columns(2)
    
    with col1:
        ckd_stage = st.selectbox(
            "Giai đoạn CKD:",
            ["G1-G2", "G3a", "G3b", "G4", "G5 (không lọc máu)", "G5D (lọc máu)", "Ghép thận"],
            key="hf_ckd_stage"
        )
        
        egfr = st.number_input(
            "eGFR (mL/min/1.73m²):",
            min_value=5.0,
            max_value=150.0,
            value=45.0,
            step=1.0,
            key="hf_ckd_egfr"
        )
        
        ef = st.number_input(
            "Phân suất tống máu EF (%):",
            min_value=10.0,
            max_value=80.0,
            value=35.0,
            step=1.0,
            key="hf_ckd_ef"
        )
    
    with col2:
        nyha_class = st.selectbox(
            "NYHA Class:",
            ["Class I", "Class II", "Class III", "Class IV"],
            key="hf_ckd_nyha"
        )
        
        current_sbp = st.number_input(
            "Huyết áp tâm thu (mmHg):",
            min_value=80.0,
            max_value=250.0,
            value=120.0,
            step=5.0,
            key="hf_ckd_sbp"
        )
        
        potassium = st.number_input(
            "Kali máu (mEq/L):",
            min_value=2.0,
            max_value=7.0,
            value=4.5,
            step=0.1,
            key="hf_ckd_k"
        )
    
    has_diabetes = st.checkbox("Có đái tháo đường?", key="hf_ckd_dm")
    
    st.markdown("---")
    
    # Scenario selection
    scenario = st.radio(
        "Chọn tình huống lâm sàng:",
        [
            "🔍 Chẩn đoán & Đánh giá",
            "💊 Điều trị HFrEF (EF <40%)",
            "💊 Điều trị HFpEF (EF ≥50%)",
            "📊 Theo dõi & Điều chỉnh"
        ],
        key="hf_ckd_scenario"
    )
    
    st.markdown("---")
    
    if "Chẩn đoán" in scenario:
        render_diagnosis(egfr, ef, nyha_class)
    elif "HFrEF" in scenario:
        render_hfref_treatment(egfr, ef, current_sbp, potassium, has_diabetes)
    elif "HFpEF" in scenario:
        render_hfpef_treatment(egfr, ef, current_sbp, has_diabetes)
    else:
        render_monitoring(egfr, ef, potassium)
    
    st.markdown("---")
    references = get_references("Heart_Failure_CKD")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2026-01-15",
            show_evidence_level=True,
            show_links=True
        )
    else:
        st.markdown("### 📚 Tài liệu tham khảo")
        st.markdown("""
        1. **KDIGO 2025 Clinical Practice Guideline for Heart Failure in CKD**
           - Website: https://kdigo.org/guidelines/heart-failure-in-ckd/
        
        2. **ESC Heart Failure Guidelines 2021**
           - Eur Heart J. 2021;42(36):3599-3726
        
        3. **AHA/ACC/HFSA Heart Failure Guideline 2022**
           - Circulation. 2022;145(18):e895-e1032
        """)


def render_diagnosis(egfr: float, ef: float, nyha_class: str) -> None:
    """Diagnosis and evaluation"""
    st.success("## 🔍 Chẩn đoán & Đánh giá")
    
    st.markdown("### Chẩn đoán Suy Tim")
    
    st.info("""
    **Triệu chứng:**
    - Khó thở, phù, mệt mỏi
    - Ho khan, khó thở khi nằm (orthopnea)
    - Tăng cân do giữ nước
    
    **Dấu hiệu:**
    - Ran ẩm phổi, phù ngoại vi
    - Tĩnh mạch cổ nổi, gan to
    - Tiếng tim bất thường (S3, S4)
    """)
    
    st.markdown("---")
    st.markdown("### Xét nghiệm Chẩn đoán")
    
    st.info("""
    **NT-proBNP hoặc BNP:**
    - NT-proBNP >300 pg/mL (hoặc BNP >100 pg/mL) gợi ý suy tim
    - **Lưu ý:** NT-proBNP tăng ở CKD ngay cả không có suy tim
    
    **Echocardiography:**
    - Đánh giá EF, cấu trúc tim, chức năng van
    
    **ECG:**
    - Rối loạn nhịp, dày thất trái
    """)
    
    st.markdown("---")
    st.markdown("### Đánh giá Hiện tại")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if ef < 40:
            st.error(f"**EF: {ef}%** – HFrEF (suy tim giảm phân suất tống máu)")
        elif ef < 50:
            st.warning(f"**EF: {ef}%** – HFmrEF (suy tim phân suất tống máu trung gian)")
        else:
            st.info(f"**EF: {ef}%** – HFpEF (suy tim bảo tồn phân suất tống máu)")
    
    with col2:
        if egfr >= 60:
            st.success(f"**eGFR: {egfr} mL/min/1.73m²** – Bình thường/nhẹ")
        elif egfr >= 30:
            st.warning(f"**eGFR: {egfr} mL/min/1.73m²** – Giảm trung bình")
        else:
            st.error(f"**eGFR: {egfr} mL/min/1.73m²** – Giảm nặng")
    
    with col3:
        if "Class I" in nyha_class or "Class II" in nyha_class:
            st.info(f"**NYHA: {nyha_class}** – Nhẹ-trung bình")
        else:
            st.error(f"**NYHA: {nyha_class}** – Nặng")


def render_hfref_treatment(egfr: float, ef: float, sbp: float, potassium: float, has_diabetes: bool) -> None:
    """HFrEF treatment"""
    st.error("## 💊 Điều trị HFrEF (EF <40%)")
    
    st.markdown("### 4 Trụ Cột Điều trị (KDIGO 2025)")
    
    st.success("""
    **1. SGLT2 Inhibitors (ƯU TIÊN - KDIGO 2025):**
    - **Dapagliflozin:** 10 mg/ngày (nếu eGFR ≥25)
    - **Empagliflozin:** 10-25 mg/ngày (nếu eGFR ≥20)
    - **Lợi ích:** Giảm tử vong, nhập viện, làm chậm tiến triển CKD
    - **Lưu ý:** Có thể dùng ở bệnh nhân không đái tháo đường
    """)
    
    can_use_sglt2 = egfr >= 25
    if can_use_sglt2:
        st.success(f"**Có thể dùng SGLT2 inhibitors** (eGFR: {egfr} mL/min/1.73m² ≥25)")
    else:
        st.warning(f"**Chưa đủ điều kiện SGLT2 inhibitors** (eGFR: {egfr} mL/min/1.73m² <25)")
    
    st.markdown("---")
    st.markdown("### 2. ACEi hoặc ARB")
    
    if egfr >= 30:
        st.success("""
        **Liều đầy đủ:**
        - **ACEi:** Lisinopril 10-40 mg/ngày, Enalapril 5-20 mg/ngày
        - **ARB:** Losartan 50-100 mg/ngày, Valsartan 80-320 mg/ngày
        - Bắt đầu liều thấp, tăng dần đến liều tối đa dung nạp
        """)
    elif egfr >= 15:
        st.warning("""
        **Giảm liều 50%:**
        - eGFR 15-29: Giảm liều ACEi/ARB
        - Theo dõi creatinine và kali máu chặt chẽ
        """)
    else:
        st.error("""
        **Cân nhắc giảm liều hoặc tạm ngừng:**
        - eGFR <15: Cân nhắc giảm liều hoặc tạm ngừng
        - Đánh giá lại sau khi điều chỉnh
        """)
    
    st.markdown("---")
    st.markdown("### 3. Beta-blockers")
    
    st.info("""
    **Lựa chọn:**
    - **Bisoprolol:** 1.25-10 mg/ngày
    - **Metoprolol succinate:** 12.5-200 mg/ngày
    - **Carvedilol:** 3.125-50 mg/ngày
    
    **Lưu ý:**
    - Bắt đầu liều thấp, tăng dần
    - Không điều chỉnh liều theo eGFR
    """)
    
    st.markdown("---")
    st.markdown("### 4. MRA (Mineralocorticoid Receptor Antagonists)")
    
    can_use_mra = egfr >= 30 and potassium < 5.0
    if can_use_mra:
        st.success("""
        **Có thể dùng MRA:**
        - **Spironolactone:** 12.5-50 mg/ngày
        - **Eplerenone:** 25-50 mg/ngày
        - **Finerenone:** 10-20 mg/ngày (nếu có CKD + đái tháo đường type 2)
        
        **Theo dõi:** Kali máu mỗi 1-2 tuần khi bắt đầu
        """)
    else:
        st.error(f"""
        **Chống chỉ định MRA:**
        - eGFR: {egfr} mL/min/1.73m² (cần ≥30)
        - Kali: {potassium} mEq/L (cần <5.0)
        """)
    
    st.markdown("---")
    st.markdown("### Thuốc Bổ sung")
    
    st.info("""
    **ARNI (Sacubitril/Valsartan):**
    - Thay thế ACEi/ARB nếu vẫn còn triệu chứng
    - Liều: 24/26 mg → 49/51 mg → 97/103 mg × 2 lần/ngày
    - Chống chỉ định: eGFR <30 hoặc kali >5.2 mEq/L
    
    **Lợi tiểu:**
    - **Furosemide:** 20-240 mg/ngày (chia 1-2 lần)
    - **Torsemide:** 10-100 mg/ngày
    - Điều chỉnh liều theo eGFR và đáp ứng
    """)


def render_hfpef_treatment(egfr: float, ef: float, sbp: float, has_diabetes: bool) -> None:
    """HFpEF treatment"""
    st.warning("## 💊 Điều trị HFpEF (EF ≥50%)")
    
    st.info("""
    **Thuốc nền tảng:**
    - **SGLT2 inhibitors:** Dapagliflozin hoặc Empagliflozin (lợi ích đã được chứng minh)
    - **ACEi/ARB:** Nếu có tăng huyết áp hoặc đái tháo đường
    - **Lợi tiểu:** Để kiểm soát phù và khó thở
    - **Beta-blockers:** Nếu có rối loạn nhịp hoặc tăng huyết áp
    
    **Lưu ý:**
    - Không có bằng chứng rõ ràng cho ARNI, MRA ở HFpEF đơn thuần
    - Tập trung vào kiểm soát yếu tố nguy cơ (tăng huyết áp, đái tháo đường)
    """)
    
    can_use_sglt2 = egfr >= 25
    if can_use_sglt2:
        st.success(f"**Có thể dùng SGLT2 inhibitors** (eGFR: {egfr} mL/min/1.73m² ≥25)")
    else:
        st.warning(f"**Chưa đủ điều kiện SGLT2 inhibitors** (eGFR: {egfr} mL/min/1.73m² <25)")


def render_monitoring(egfr: float, ef: float, potassium: float) -> None:
    """Monitoring and adjustment"""
    st.success("## 📊 Theo dõi & Điều chỉnh")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Lịch Theo dõi")
        st.info("""
        **Tần suất:**
        - Mỗi 1-2 tuần khi mới bắt đầu điều trị
        - Mỗi 1-3 tháng khi ổn định
        
        **Đánh giá:**
        - Triệu chứng suy tim (khó thở, phù)
        - Cân nặng (tăng cân = giữ nước)
        - Huyết áp, nhịp tim
        - Chức năng thận (creatinine, eGFR)
        """)
    
    with col2:
        st.markdown("### Xét nghiệm")
        st.info("""
        **Thường xuyên:**
        - Creatinine, eGFR: Mỗi 1-3 tháng
        - Điện giải (Na, K): Mỗi 1-3 tháng
        - NT-proBNP: Mỗi 3-6 tháng (nếu có điều kiện)
        """)
    
    st.markdown("---")
    st.markdown("### Cảnh báo")
    
    st.error("""
    **Cần đánh giá lại khi:**
    - Creatinine tăng >30%: Đánh giá lại điều trị
    - Kali >5.5 mEq/L: Giảm liều hoặc ngừng MRA, ACEi/ARB
    - eGFR giảm nhanh: Đánh giá nguyên nhân
    - Triệu chứng suy tim xấu đi: Tăng liều lợi tiểu, đánh giá lại
    """)
