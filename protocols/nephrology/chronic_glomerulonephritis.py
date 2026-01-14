"""
Chronic Glomerulonephritis Protocol
KDIGO 2021, KDIGO GN 2021, KDIGO 2024, KDIGO 2025
Quản lý viêm cầu thận mạn tính
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Chronic Glomerulonephritis Protocol"""
    st.subheader("🔬 Viêm Cầu Thận Mạn Tính")
    st.caption("KDIGO 2021, KDIGO 2024, KDIGO 2025 - Quản lý viêm cầu thận mạn tính và tiến triển suy thận")
    
    st.info("""
    **Điểm chính:**
    - Viêm cầu thận mạn là nguyên nhân hàng đầu gây suy thận mạn giai đoạn cuối tại Việt Nam
    - Cần phân loại theo nguyên nhân: IgA nephropathy, FSGS, Membranous, Lupus nephritis, v.v.
    - Mục tiêu: Làm chậm tiến triển, kiểm soát protein niệu, huyết áp, và biến chứng
    """)
    
    st.markdown("---")
    
    scenario = st.radio(
        "Chọn tình huống lâm sàng:",
        [
            "🔍 Chẩn đoán & Phân loại",
            "💊 Điều trị bảo tồn (Conservative)",
            "💉 Điều trị ức chế miễn dịch",
            "📊 Theo dõi & Biến chứng"
        ],
        key="gn_scenario"
    )
    
    st.markdown("---")
    
    if "Chẩn đoán" in scenario:
        render_diagnosis()
    elif "bảo tồn" in scenario:
        render_conservative()
    elif "miễn dịch" in scenario:
        render_immunosuppression()
    else:
        render_monitoring()
    
    st.markdown("---")
    references = get_references("Chronic Glomerulonephritis")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-12-15",
            show_evidence_level=True,
            show_links=True
        )


def render_diagnosis():
    """Diagnosis and classification"""
    st.success("## 🔍 Chẩn đoán & Phân loại")
    
    st.markdown("### Tiêu chuẩn Chẩn đoán")
    st.info("""
    **Lâm sàng:**
    - Protein niệu >0.5 g/24h (thường >1 g/24h)
    - Hồng cầu niệu vi thể hoặc đại thể
    - Tăng huyết áp
    - Phù (nếu có hội chứng thận hư)
    - Tiến triển suy thận mạn
    
    **Xét nghiệm:**
    - Tổng phân tích nước tiểu: protein, hồng cầu, trụ hồng cầu
    - Protein niệu 24h hoặc tỷ số protein/creatinine
    - Creatinine, eGFR
    - Bổ thể (C3, C4), ANA, ANCA, anti-GBM nếu nghi ngờ
    """)
    
    st.markdown("---")
    st.markdown("### Chỉ định Sinh Thiết Thận")
    st.warning("""
    **Chỉ định sinh thiết khi:**
    - Protein niệu >1 g/24h kéo dài >3 tháng
    - Hội chứng thận hư (protein >3.5 g/24h)
    - Suy thận tiến triển không rõ nguyên nhân
    - Hồng cầu niệu đại thể tái phát
    - Nghi ngờ lupus nephritis, vasculitis, hoặc bệnh hệ thống
    
    **Chống chỉ định:**
    - Thận đơn độc, rối loạn đông máu nặng
    - Nhiễm trùng đang hoạt động
    - Tăng huyết áp không kiểm soát
    """)
    
    st.markdown("---")
    st.markdown("### Phân loại Theo Nguyên Nhân")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Nguyên phát:**
        - IgA nephropathy (phổ biến nhất)
        - FSGS (Focal Segmental Glomerulosclerosis)
        - Membranous nephropathy
        - Minimal change disease
        - Membranoproliferative GN
        
        **Thứ phát:**
        - Lupus nephritis
        - ANCA vasculitis
        - Diabetic nephropathy
        - Amyloidosis
        """)
    
    with col2:
        st.markdown("""
        **Đặc điểm tại Việt Nam:**
        - IgA nephropathy: 30-40% các trường hợp
        - Lupus nephritis: thường gặp ở nữ trẻ
        - FSGS: tăng dần, liên quan béo phì
        - Membranous: thường gặp ở nam >50 tuổi
        
        **Tiên lượng:**
        - Phụ thuộc loại mô bệnh học
        - Protein niệu >1 g/24h → tiên lượng xấu
        - Tăng huyết áp không kiểm soát → tiến triển nhanh
        """)


def render_conservative():
    """Conservative management"""
    st.warning("## 💊 Điều trị Bảo Tồn (Nền Tảng)")
    
    st.markdown("### 1. Kiểm soát Huyết Áp (KDIGO 2024/2025)")
    st.success("""
    **Mục tiêu:**
    - <130/80 mmHg (nếu protein niệu <1 g/24h)
    - <125/75 mmHg (nếu protein niệu >1 g/24h)
    - **IgA Nephropathy (KDIGO 2025):** ≤120/70 mmHg (giảm mất nephron)
    
    **Thuốc ưu tiên:**
    - **ACEi/ARB:** Liều tối đa dung nạp (Lisinopril 20-40 mg/ngày, Losartan 50-100 mg/ngày)
    - **Lợi tiểu:** Thiazide hoặc Furosemide nếu phù
    - **Bổ sung:** Calcium channel blocker, Beta-blocker nếu cần
    
    **Lưu ý:**
    - Theo dõi creatinine sau 1-2 tuần (tăng <30% là chấp nhận được)
    - Tránh dùng nếu hẹp động mạch thận 2 bên
    - Tránh trong thai kỳ
    - Tất cả bệnh nhân IgAN nên được điều trị bằng liều tối ưu của RASi (KDIGO 2025)
    """)
    
    st.markdown("---")
    st.markdown("### 2. Giảm Protein Niệu")
    st.info("""
    **ACEi/ARB:**
    - Giảm protein niệu 30-50%
    - Bắt đầu liều thấp, tăng dần đến liều tối đa
    - Hiệu quả tốt nhất khi protein niệu >1 g/24h
    
    **SGLT2 inhibitors (nếu có đái tháo đường hoặc CKD):**
    - Dapagliflozin, Empagliflozin
    - Giảm protein niệu, làm chậm tiến triển CKD
    - Chống chỉ định: eGFR <25 mL/min/1.73m²
    """)
    
    st.markdown("---")
    st.markdown("### 3. Chế Độ Ăn & Lối Sống")
    st.warning("""
    **Chế độ ăn:**
    - Protein: 0.8-1.0 g/kg/ngày (nếu eGFR <30: 0.6-0.8 g/kg/ngày)
    - Muối: <2-3 g/ngày (giảm phù, huyết áp)
    - Phosphorus: hạn chế nếu tăng
    - Kali: theo dõi, hạn chế nếu tăng
    
    **Lối sống:**
    - Bỏ thuốc lá
    - Giảm cân nếu béo phì
    - Tập thể dục vừa phải
    - Tránh NSAID, contrast nếu có thể
    """)
    
    st.markdown("---")
    st.markdown("### 4. Điều trị Biến Chứng")
    st.success("""
    **Thiếu máu:**
    - Bổ sung sắt nếu ferritin <100 ng/mL
    - ESA (Erythropoietin) nếu Hb <10 g/dL và thiếu máu do CKD
    
    **Rối loạn xương-khoáng:**
    - Bổ sung Calcitriol/Vitamin D nếu thiếu
    - Phosphate binders nếu tăng phosphate
    - Theo dõi PTH, Ca, PO₄
    
    **Tăng lipid:**
    - Statin nếu LDL >100 mg/dL
    - Mục tiêu LDL <100 mg/dL (hoặc <70 nếu nguy cơ tim mạch cao)
    """)


def render_immunosuppression():
    """Immunosuppressive therapy"""
    st.error("## 💉 Điều trị Ức Chế Miễn dịch")
    
    st.markdown("### Chỉ định")
    st.warning("""
    **Chỉ định khi:**
    - Hội chứng thận hư (protein >3.5 g/24h)
    - Protein niệu >1 g/24h + suy thận tiến triển
    - Lupus nephritis (Class III, IV, V)
    - ANCA vasculitis với tổn thương thận
    - IgA nephropathy với protein >1 g/24h + suy thận tiến triển
    
    **Chống chỉ định:**
    - Nhiễm trùng đang hoạt động
    - Suy thận giai đoạn cuối (eGFR <15)
    - Ung thư đang hoạt động
    - Thai kỳ (một số thuốc)
    """)
    
    st.markdown("---")
    st.markdown("### Phác Đồ Theo Loại Bệnh")
    
    gn_type = st.selectbox(
        "**Loại viêm cầu thận:**",
        [
            "IgA Nephropathy",
            "FSGS (Focal Segmental Glomerulosclerosis)",
            "Membranous Nephropathy",
            "Lupus Nephritis (Class III/IV)",
            "Minimal Change Disease",
            "ANCA Vasculitis"
        ],
        key="gn_type"
    )
    
    st.markdown("---")
    
    if "IgA" in gn_type:
        render_iga_protocol()
    elif "FSGS" in gn_type:
        render_fsgs_protocol()
    elif "Membranous" in gn_type:
        render_membranous_protocol()
    elif "Lupus" in gn_type:
        render_lupus_protocol()
    elif "Minimal" in gn_type:
        render_mcd_protocol()
    else:
        render_anca_protocol()


def render_iga_protocol():
    """IgA Nephropathy protocol (KDIGO 2025)"""
    st.info("""
    **IgA Nephropathy - Phác đồ điều trị (KDIGO 2025):**
    
    **Kiểm soát huyết áp (KDIGO 2025 - MỚI):**
    - Mục tiêu: ≤120/70 mmHg (giảm mất nephron)
    - ACEi/ARB: Liều tối đa dung nạp
    - Tất cả bệnh nhân IgAN nên được điều trị bằng liều tối ưu của RASi
    
    **Protein niệu <1 g/24h:**
    - ACEi/ARB + theo dõi
    - Không cần ức chế miễn dịch
    
    **Protein niệu 1-3 g/24h + eGFR >50:**
    - ACEi/ARB liều tối đa 3-6 tháng
    - Nếu không đáp ứng: Corticosteroid (Prednisone 0.6-1 mg/kg/ngày × 6 tháng, giảm dần)
    
    **Protein niệu >3 g/24h hoặc suy thận tiến triển:**
    - Corticosteroid + Cyclophosphamide hoặc Mycophenolate
    - Hoặc: Corticosteroid + Rituximab (nếu có điều kiện)
    - Hoặc: Budesonide giải phóng mục tiêu (nếu có điều kiện - KDIGO 2025)
    
    **SGLT2 inhibitors (KDIGO 2024/2025):**
    - Có thể xem xét nếu có CKD (eGFR ≥25, protein niệu ≥200 mg/g)
    - Làm chậm tiến triển CKD
    
    **Thời gian điều trị:** 6-12 tháng, theo dõi protein niệu và creatinine
    """)


def render_fsgs_protocol():
    """FSGS protocol"""
    st.info("""
    **FSGS - Phác đồ điều trị:**
    
    **Điều trị đầu tay:**
    - Corticosteroid (Prednisone 1 mg/kg/ngày, tối đa 80 mg) × 4-16 tuần
    - Giảm dần trong 6 tháng nếu đáp ứng
    
    **Không đáp ứng hoặc phụ thuộc steroid:**
    - Cyclosporine 3-5 mg/kg/ngày × 6-12 tháng
    - Hoặc: Tacrolimus 0.1-0.15 mg/kg/ngày
    - Hoặc: Mycophenolate 1-2 g/ngày
    
    **Điều trị cứu vãn:**
    - Rituximab (nếu có điều kiện)
    - Plasmapheresis (nếu nghi ngờ circulating factor)
    
    **Lưu ý:** FSGS kháng steroid có tiên lượng xấu, cần hội chẩn chuyên khoa
    """)


def render_membranous_protocol():
    """Membranous nephropathy protocol"""
    st.info("""
    **Membranous Nephropathy - Phác đồ điều trị:**
    
    **Nguy cơ thấp (protein <4 g/24h, eGFR bình thường):**
    - ACEi/ARB + theo dõi
    - Không cần ức chế miễn dịch ngay
    
    **Nguy cơ cao (protein >4 g/24h hoặc suy thận):**
    - **Phác đồ đầu tay:**
      * Rituximab 1 g × 2 liều (cách 2 tuần) HOẶC
      * Cyclophosphamide + Corticosteroid (6 tháng)
    
    - **Phác đồ thay thế:**
      * Cyclosporine 3-5 mg/kg/ngày × 6-12 tháng
      * Tacrolimus 0.05-0.075 mg/kg/ngày × 6-12 tháng
    
    **Theo dõi:** Protein niệu, creatinine mỗi 3 tháng
    """)


def render_lupus_protocol():
    """Lupus nephritis protocol"""
    st.error("""
    **Lupus Nephritis (Class III/IV) - Phác đồ điều trị:**
    
    **Điều trị tấn công (Induction - 6 tháng):**
    - **Phác đồ đầu tay:**
      * Mycophenolate 2-3 g/ngày HOẶC
      * Cyclophosphamide (IV: 0.5-1 g/m² mỗi tháng × 6 tháng)
    
    - **Corticosteroid:**
      * Methylprednisolone 500-1000 mg IV × 3 ngày (nếu bệnh nặng)
      * Sau đó: Prednisone 0.5-1 mg/kg/ngày, giảm dần
    
    **Điều trị duy trì (Maintenance - 2-3 năm):**
    - Mycophenolate 1-2 g/ngày HOẶC
    - Azathioprine 1-2 mg/kg/ngày
    - Prednisone 5-10 mg/ngày
    
    **Lưu ý:** Cần hội chẩn thận học và thấp khớp học
    """)


def render_mcd_protocol():
    """Minimal Change Disease protocol"""
    st.success("""
    **Minimal Change Disease - Phác đồ điều trị:**
    
    **Điều trị đầu tay:**
    - Corticosteroid (Prednisone 1 mg/kg/ngày, tối đa 80 mg) × 4-8 tuần
    - Giảm dần trong 4-6 tháng
    
    **Tái phát thường xuyên hoặc phụ thuộc steroid:**
    - Cyclosporine 3-5 mg/kg/ngày × 12-24 tháng
    - Hoặc: Tacrolimus 0.1 mg/kg/ngày
    - Hoặc: Mycophenolate 1-2 g/ngày
    
    **Lưu ý:** MCD thường đáp ứng tốt với steroid, tiên lượng tốt
    """)


def render_anca_protocol():
    """ANCA vasculitis protocol"""
    st.error("""
    **ANCA Vasculitis với tổn thương thận - Phác đồ điều trị:**
    
    **Điều trị tấn công (nếu suy thận nặng hoặc cần lọc máu):**
    - Cyclophosphamide (IV: 0.5-1 g/m² mỗi tháng) HOẶC
    - Rituximab 375 mg/m²/tuần × 4 tuần
    
    - **Corticosteroid:**
      * Methylprednisolone 500-1000 mg IV × 3 ngày
      * Sau đó: Prednisone 1 mg/kg/ngày, giảm dần
    
    - **Plasmapheresis:** Nếu suy thận nặng (creatinine >5.7 mg/dL) hoặc xuất huyết phổi
    
    **Điều trị duy trì:**
    - Azathioprine 1-2 mg/kg/ngày HOẶC
    - Rituximab 500 mg mỗi 6 tháng
    
    **Lưu ý:** Cần hội chẩn thận học và thấp khớp học sớm
    """)


def render_monitoring():
    """Monitoring and complications"""
    st.info("## 📊 Theo dõi & Biến Chứng")
    
    st.markdown("### Theo dõi Định Kỳ")
    st.success("""
    **Mỗi 1-3 tháng:**
    - Creatinine, eGFR
    - Protein niệu (tỷ số protein/creatinine hoặc 24h)
    - Huyết áp
    - Điện giải (Na, K)
    
    **Mỗi 6-12 tháng:**
    - Hemoglobin, ferritin
    - Ca, PO₄, PTH, Vitamin D
    - Lipid máu
    - Siêu âm thận (nếu cần)
    
    **Khi dùng ức chế miễn dịch:**
    - Công thức máu mỗi 2-4 tuần
    - Chức năng gan mỗi 1-2 tháng
    - Theo dõi nhiễm trùng
    """)
    
    st.markdown("---")
    st.markdown("### Biến Chứng Cần Theo dõi")
    st.warning("""
    **Suy thận tiến triển:**
    - Chuẩn bị lọc máu khi eGFR <20
    - Tạo cầu nối AV sớm (eGFR 15-20)
    - Tư vấn ghép thận nếu phù hợp
    
    **Biến chứng tim mạch:**
    - Nguy cơ cao do protein niệu, tăng huyết áp
    - Kiểm soát huyết áp, lipid, đường huyết
    - Aspirin nếu có chỉ định
    
    **Nhiễm trùng:**
    - Tăng nguy cơ khi dùng ức chế miễn dịch
    - Tiêm phòng: cúm, phế cầu, COVID-19
    - Prophylaxis PCP nếu dùng steroid + ức chế miễn dịch
    
    **Huyết khối:**
    - Nguy cơ cao nếu hội chứng thận hư
    - Xem xét kháng đông dự phòng nếu albumin <2.5 g/dL
    """)
    
    st.markdown("---")
    st.markdown("### Khi Cần Hội Chẩn")
    st.error("""
    **Hội chẩn thận học khi:**
    - Protein niệu >1 g/24h kéo dài
    - Suy thận tiến triển (eGFR giảm >5 mL/min/năm)
    - Cần sinh thiết thận
    - Cần điều trị ức chế miễn dịch
    - Biến chứng nặng (tăng kali, phù nặng, thiếu máu nặng)
    
    **Hội chẩn đa chuyên khoa:**
    - Lupus nephritis → Thấp khớp học
    - ANCA vasculitis → Thấp khớp học
    - Bệnh hệ thống khác → Chuyên khoa tương ứng
    """)

