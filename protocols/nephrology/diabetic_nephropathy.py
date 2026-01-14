"""
Diabetic Nephropathy Protocol
KDIGO 2020, KDIGO 2024, ADA 2024
Quản lý bệnh thận do đái tháo đường - Nguyên nhân hàng đầu CKD tại Việt Nam
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Diabetic Nephropathy Protocol"""
    st.subheader("🍭 Bệnh Thận Do Đái Tháo Đường")
    st.caption("KDIGO 2020, KDIGO 2024, ADA 2024 - Nguyên nhân hàng đầu gây CKD tại Việt Nam (30-40%)")
    
    st.info("""
    **Tình hình tại Việt Nam:**
    - 30-40% bệnh nhân CKD do đái tháo đường
    - Tỷ lệ đái tháo đường tăng nhanh
    - Biến chứng thận thường xuất hiện sau 10-15 năm
    
    **Định nghĩa:**
    - Albumin niệu (ACR ≥30 mg/g) HOẶC
    - eGFR <60 mL/min/1.73m²
    - Ở bệnh nhân đái tháo đường, sau khi loại trừ nguyên nhân khác
    """)
    
    st.markdown("---")
    
    scenario = st.radio(
        "Chọn tình huống lâm sàng:",
        [
            "🔍 Chẩn đoán & Tầm soát",
            "💊 Điều trị bảo tồn (Giai đoạn sớm)",
            "🩸 Điều trị tiến triển (CKD G3-5)",
            "📊 Theo dõi & Phòng ngừa"
        ],
        key="dn_scenario"
    )
    
    st.markdown("---")
    
    if "Chẩn đoán" in scenario:
        render_diagnosis()
    elif "sớm" in scenario:
        render_early_stage()
    elif "tiến triển" in scenario:
        render_advanced()
    else:
        render_monitoring()
    
    st.markdown("---")
    references = get_references("Diabetic Nephropathy")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-12-15",
            show_evidence_level=True,
            show_links=True
        )


def render_diagnosis():
    """Diagnosis and screening"""
    st.success("## 🔍 Chẩn đoán & Tầm Soát")
    
    st.markdown("### Tiêu chuẩn Chẩn đoán")
    st.info("""
    **Bệnh thận do đái tháo đường khi có:**
    1. **Đái tháo đường type 1 hoặc type 2**
    2. **Albumin niệu:**
       - ACR ≥30 mg/g (≥3 mg/mmol) HOẶC
       - Protein niệu 24h ≥30 mg
    3. **Hoặc eGFR <60 mL/min/1.73m²**
    4. **Loại trừ nguyên nhân khác:**
       - Không có bệnh thận khác (viêm cầu thận, tắc nghẽn)
       - Không có bệnh hệ thống (lupus, vasculitis)
    """)
    
    st.markdown("---")
    st.markdown("### Tầm Soát")
    st.warning("""
    **Khi nào tầm soát:**
    - Type 1: Sau 5 năm chẩn đoán
    - Type 2: Ngay khi chẩn đoán (vì có thể đã có biến chứng)
    
    **Xét nghiệm tầm soát:**
    - ACR (albumin/creatinine ratio) - ưu tiên
    - Hoặc protein niệu 24h
    - Creatinine, eGFR
    - Mỗi năm một lần
    
    **Lưu ý:**
    - Tránh lấy mẫu khi có nhiễm trùng tiểu, sốt, tập thể dục nặng
    - Lấy mẫu buổi sáng, đầu tiên
    """)
    
    st.markdown("---")
    st.markdown("### Phân Giai Đoạn")
    st.success("""
    **Giai đoạn 1 (Tăng lọc):**
    - eGFR >90, ACR bình thường
    - Tăng lọc cầu thận
    
    **Giai đoạn 2 (Tổn thương sớm):**
    - eGFR >90, ACR 30-300 mg/g
    - Albumin niệu trung bình
    
    **Giai đoạn 3 (Bệnh thận sớm):**
    - eGFR 30-89, ACR 30-300 mg/g
    - Suy thận mạn nhẹ-trung bình
    
    **Giai đoạn 4 (Bệnh thận nặng):**
    - eGFR 15-29, ACR >300 mg/g
    - Suy thận mạn nặng
    
    **Giai đoạn 5 (ESKD):**
    - eGFR <15
    - Suy thận mạn giai đoạn cuối
    """)
    
    st.markdown("---")
    st.markdown("### Khi Nào Cần Sinh Thiết")
    st.error("""
    **Chỉ định sinh thiết khi:**
    - Protein niệu >3.5 g/24h (hội chứng thận hư)
    - Hồng cầu niệu đại thể
    - Suy thận tiến triển nhanh (<3 tháng)
    - Không có bệnh võng mạc đái tháo đường (nghi ngờ nguyên nhân khác)
    - Triệu chứng không điển hình
    
    **Lưu ý:** Hầu hết bệnh nhân không cần sinh thiết nếu lâm sàng điển hình
    """)


def render_early_stage():
    """Early stage management (CKD G1-G2)"""
    st.warning("## 💊 Điều trị Bảo Tồn (Giai Đoạn Sớm)")
    
    st.markdown("### 1. Kiểm soát Đường Huyết")
    st.success("""
    **Mục tiêu:**
    - HbA1c <7% (nếu không có nguy cơ hạ đường huyết)
    - HbA1c <8% (nếu nguy cơ hạ đường huyết cao, người già)
    - Đường huyết đói: 80-130 mg/dL
    - Đường huyết sau ăn: <180 mg/dL
    
    **Thuốc ưu tiên (có lợi cho thận):**
    - **SGLT2 inhibitors:**
      * Dapagliflozin 10 mg/ngày (nếu eGFR ≥25)
      * Empagliflozin 10-25 mg/ngày
      * Làm chậm tiến triển CKD, giảm protein niệu
    
    - **GLP-1 agonists:**
      * Liraglutide 0.6-1.8 mg/ngày
      * Semaglutide 0.5-1 mg/tuần
      * Làm chậm tiến triển, giảm biến cố tim mạch
    
    **Tránh:**
    - Metformin nếu eGFR <30 (nguy cơ nhiễm toan lactic)
    - Sulfonylurea nếu eGFR <30 (nguy cơ hạ đường huyết)
    """)
    
    st.markdown("---")
    st.markdown("### 2. Kiểm soát Huyết Áp")
    st.info("""
    **Mục tiêu:**
    - <130/80 mmHg (nếu ACR <30 mg/g)
    - <125/75 mmHg (nếu ACR ≥30 mg/g)
    
    **Thuốc ưu tiên:**
    - **ACEi/ARB:** Liều tối đa dung nạp
      * Lisinopril 20-40 mg/ngày
      * Losartan 50-100 mg/ngày
      * Telmisartan 40-80 mg/ngày
    
    - **Bổ sung nếu cần:**
      * Thiazide hoặc Furosemide (nếu phù)
      * Calcium channel blocker
      * Beta-blocker
    
    **Finerenone (KDIGO 2024 - MỚI):**
    - Chất đối kháng thụ thể mineralocorticoid không steroid
    - Chỉ định: CKD với đái tháo đường type 2 (eGFR ≥25, ACR 30-5000 mg/g)
    - Liều: 10-20 mg/ngày (điều chỉnh theo kali máu)
    - Làm chậm tiến triển CKD, giảm nguy cơ tim mạch
    - Có thể dùng kết hợp với ACEi/ARB và SGLT2i
    - Theo dõi kali máu (nguy cơ tăng kali)
    
    **Lưu ý:**
    - ACEi/ARB làm chậm tiến triển, giảm protein niệu
    - Theo dõi creatinine sau 1-2 tuần
    - Tăng creatinine <30% là chấp nhận được
    """)
    
    st.markdown("---")
    st.markdown("### 3. Giảm Protein Niệu")
    st.warning("""
    **Mục tiêu:**
    - Giảm ACR >30% hoặc <30 mg/g
    
    **Phương pháp:**
    - ACEi/ARB liều tối đa
    - SGLT2 inhibitors
    - Kiểm soát đường huyết tốt
    - Kiểm soát huyết áp tốt
    
    **Lưu ý:**
    - Protein niệu là yếu tố tiên lượng quan trọng
    - Giảm protein niệu → làm chậm tiến triển
    """)


def render_advanced():
    """Advanced stage management (CKD G3-5)"""
    st.error("## 🩸 Điều trị Giai Đoạn Tiến Triển (CKD G3-5)")
    
    st.markdown("### 1. Điều chỉnh Thuốc Đái Tháo Đường")
    st.warning("""
    **eGFR 30-45:**
    - SGLT2 inhibitors: Có thể dùng (Dapagliflozin, Empagliflozin)
    - GLP-1 agonists: An toàn
    - Metformin: Giảm liều, theo dõi
    - DPP-4 inhibitors: An toàn (trừ Saxagliptin)
    
    **eGFR 15-30:**
    - SGLT2 inhibitors: Dapagliflozin (nếu eGFR ≥25)
    - GLP-1 agonists: An toàn
    - Metformin: Tránh (nguy cơ nhiễm toan lactic)
    - DPP-4 inhibitors: An toàn
    - Insulin: Điều chỉnh liều
    
    **eGFR <15:**
    - Chỉ dùng: GLP-1 agonists, DPP-4 inhibitors, Insulin
    - Tránh: Metformin, SGLT2 inhibitors
    """)
    
    st.markdown("---")
    st.markdown("### 2. Điều trị Biến Chứng CKD")
    st.info("""
    **Thiếu máu:**
    - Bổ sung sắt nếu ferritin <100 ng/mL
    - ESA nếu Hb <10 g/dL
    - Mục tiêu Hb: 10-12 g/dL
    
    **Rối loạn xương-khoáng:**
    - Vitamin D, Calcitriol
    - Phosphate binders nếu PO₄ >5.5 mg/dL
    
    **Toan chuyển hóa:**
    - Bicarbonate nếu HCO₃ <22 mEq/L
    
    **Tăng lipid:**
    - Statin (mục tiêu LDL <100 mg/dL)
    """)
    
    st.markdown("---")
    st.markdown("### 3. Chuẩn Bị Lọc Máu")
    st.success("""
    **Bắt đầu chuẩn bị khi:**
    - eGFR <30
    - eGFR <20: Chuẩn bị tích cực
    
    **Tư vấn:**
    - Lọc máu chu kỳ hoặc lọc màng bụng
    - Ghép thận (nếu phù hợp)
    - Chăm sóc bảo tồn (nếu không muốn lọc máu)
    
    **Chuẩn bị:**
    - Tạo AV fistula sớm (eGFR 15-20)
    - Đánh giá đa chuyên khoa
    """)
    
    st.markdown("---")
    st.markdown("### 4. Chế Độ Ăn")
    st.warning("""
    **Protein:**
    - eGFR >30: 0.8-1.0 g/kg/ngày
    - eGFR <30: 0.6-0.8 g/kg/ngày
    
    **Muối:**
    - <2-3 g/ngày
    
    **Phosphorus:**
    - Hạn chế nếu tăng (eGFR <30)
    
    **Kali:**
    - Theo dõi, hạn chế nếu tăng
    
    **Carbohydrate:**
    - Điều chỉnh theo đường huyết
    - Chọn chỉ số đường huyết thấp
    """)


def render_monitoring():
    """Monitoring and prevention"""
    st.info("## 📊 Theo dõi & Phòng ngừa")
    
    st.markdown("### Theo dõi Định Kỳ")
    st.success("""
    **Mỗi 3-6 tháng:**
    - ACR (albumin/creatinine ratio)
    - Creatinine, eGFR
    - HbA1c
    - Huyết áp
    - Điện giải (Na, K)
    
    **Mỗi 6-12 tháng:**
    - Hemoglobin (nếu eGFR <30)
    - Ca, PO₄, PTH (nếu eGFR <30)
    - Lipid máu
    - Siêu âm thận (nếu cần)
    
    **Mỗi năm:**
    - Đánh giá toàn diện
    - Khám mắt (bệnh võng mạc đái tháo đường)
    - Khám bàn chân (bệnh thần kinh đái tháo đường)
    """)
    
    st.markdown("---")
    st.markdown("### Phòng ngừa Tiến Triển")
    st.warning("""
    **Kiểm soát tốt:**
    - Đường huyết: HbA1c <7%
    - Huyết áp: <130/80 (hoặc <125/75 nếu protein niệu)
    - Protein niệu: Giảm >30% hoặc <30 mg/g
    
    **Thuốc bảo vệ thận:**
    - ACEi/ARB liều tối đa
    - SGLT2 inhibitors (nếu phù hợp)
    - GLP-1 agonists (nếu phù hợp)
    
    **Lối sống:**
    - Chế độ ăn lành mạnh
    - Tập thể dục đều đặn
    - Bỏ thuốc lá
    - Giảm cân nếu béo phì
    """)
    
    st.markdown("---")
    st.markdown("### Khi Cần Hội Chẩn")
    st.error("""
    **Hội chẩn thận học khi:**
    - eGFR <30
    - Protein niệu >1 g/24h
    - Suy thận tiến triển nhanh
    - Cần chuẩn bị lọc máu
    - Biến chứng nặng
    
    **Hội chẩn nội tiết:**
    - Đường huyết khó kiểm soát
    - Cần điều chỉnh thuốc đái tháo đường
    - Biến chứng đái tháo đường khác
    """)

