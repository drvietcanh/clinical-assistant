"""
Nephrotic Syndrome Protocol
KDIGO 2021, KDIGO GN 2021, KDIGO 2024, KDIGO 2025
Quản lý hội chứng thận hư
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Nephrotic Syndrome Protocol"""
    st.subheader("💧 Hội Chứng Thận Hư")
    st.caption("KDIGO 2021, KDIGO 2024, KDIGO 2025 - Quản lý hội chứng thận hư ở người lớn và trẻ em")
    
    st.info("""
    **Định nghĩa Hội chứng thận hư:**
    - Protein niệu >3.5 g/24h (hoặc >3.5 g/g creatinine)
    - Albumin huyết thanh <3.0 g/dL
    - Phù
    - Tăng lipid máu
    
    **Nguyên nhân thường gặp tại Việt Nam:**
    - Minimal Change Disease (trẻ em)
    - Membranous Nephropathy (người lớn)
    - FSGS
    - IgA Nephropathy
    - Lupus Nephritis
    """)
    
    st.markdown("---")
    
    scenario = st.radio(
        "Chọn tình huống lâm sàng:",
        [
            "🔍 Chẩn đoán & Đánh giá ban đầu",
            "💊 Điều trị triệu chứng & Hỗ trợ",
            "💉 Điều trị nguyên nhân (Ức chế miễn dịch)",
            "⚠️ Biến chứng & Theo dõi"
        ],
        key="ns_scenario"
    )
    
    st.markdown("---")
    
    if "Chẩn đoán" in scenario:
        render_diagnosis()
    elif "triệu chứng" in scenario:
        render_supportive()
    elif "nguyên nhân" in scenario:
        render_immunosuppression()
    else:
        render_complications()
    
    st.markdown("---")
    references = get_references("Nephrotic Syndrome")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-12-15",
            show_evidence_level=True,
            show_links=True
        )


def render_diagnosis():
    """Diagnosis and initial evaluation"""
    st.success("## 🔍 Chẩn Đoán & Đánh Giá Ban Đầu")
    
    st.markdown("### Tiêu Chuẩn Chẩn Đoán")
    st.info("""
    **Tiêu chuẩn chính:**
    1. Protein niệu >3.5 g/24h (hoặc tỷ số protein/creatinine >3.5)
    2. Albumin huyết thanh <3.0 g/dL
    3. Phù (thường nặng, toàn thân)
    4. Tăng lipid máu (cholesterol, triglyceride)
    
    **Tiêu chuẩn phụ (không bắt buộc):**
    - Lipid niệu (oval fat bodies)
    - Giảm globulin miễn dịch
    - Tăng nguy cơ nhiễm trùng
    """)
    
    st.markdown("---")
    st.markdown("### Đánh Giá Ban Đầu")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Xét Nghiệm Cần Làm")
        st.warning("""
        **Cơ bản:**
        - Tổng phân tích nước tiểu
        - Protein niệu 24h hoặc tỷ số P/Cr
        - Creatinine, eGFR
        - Albumin, protein toàn phần
        - Lipid máu (cholesterol, TG)
        - Điện giải (Na, K, Cl)
        
        **Tìm nguyên nhân:**
        - ANA, anti-dsDNA (nếu nghi lupus)
        - ANCA (nếu nghi vasculitis)
        - Anti-GBM (nếu nghi Goodpasture)
        - Bổ thể (C3, C4)
        - HBsAg, anti-HCV
        - Điện di protein huyết thanh
        """)
    
    with col2:
        st.markdown("#### Hình Ảnh Học")
        st.info("""
        **Siêu âm thận:**
        - Kích thước thận (thường bình thường hoặc to)
        - Độ dày nhu mô
        - Loại trừ tắc nghẽn
        
        **Chỉ định sinh thiết:**
        - Người lớn: luôn cần sinh thiết (trừ khi rõ ràng MCD)
        - Trẻ em: thử steroid trước, sinh thiết nếu không đáp ứng
        - Nghi ngờ nguyên nhân thứ phát
        """)
    
    st.markdown("---")
    st.markdown("### Phân Loại Theo Nguyên Nhân")
    st.success("""
    **Nguyên phát (Primary):**
    - Minimal Change Disease (MCD) - 10-15% người lớn, 80% trẻ em
    - Membranous Nephropathy (MN) - 30-40% người lớn
    - FSGS - 20-30% người lớn
    - Membranoproliferative GN - 5-10%
    
    **Thứ phát (Secondary):**
    - Đái tháo đường
    - Lupus nephritis
    - Amyloidosis
    - Nhiễm trùng (HBV, HCV, HIV, malaria)
    - Thuốc (NSAID, gold, penicillamine)
    - Ung thư (lymphoma, carcinoma)
    """)


def render_supportive():
    """Supportive care and symptom management"""
    st.warning("## 💊 Điều Trị Triệu Chứng & Hỗ Trợ")
    
    st.markdown("### 1. Kiểm Soát Phù")
    st.success("""
    **Lợi tiểu:**
    - Furosemide 40-80 mg/ngày (có thể tăng đến 160-240 mg/ngày)
    - Spironolactone 25-50 mg/ngày (nếu cần, cẩn thận tăng kali)
    - Metolazone 2.5-5 mg/ngày (nếu phù kháng trị)
    
    **Chế độ ăn:**
    - Hạn chế muối: <2-3 g/ngày
    - Hạn chế nước: 1-1.5 L/ngày (nếu phù nặng)
    
    **Lưu ý:**
    - Theo dõi điện giải, creatinine khi dùng lợi tiểu
    - Tránh giảm thể tích quá mức (nguy cơ AKI)
    - Cân nhắc truyền albumin + furosemide nếu phù nặng, kháng trị
    """)
    
    st.markdown("---")
    st.markdown("### 2. Kiểm Soát Protein Niệu")
    st.info("""
    **ACEi/ARB:**
    - Giảm protein niệu 30-50%
    - Bắt đầu liều thấp, tăng dần đến liều tối đa
    - Mục tiêu: protein niệu <1 g/24h hoặc giảm >50%
    
    **Lưu ý:**
    - Theo dõi creatinine sau 1-2 tuần
    - Tăng creatinine <30% là chấp nhận được
    - Tránh nếu hẹp động mạch thận 2 bên
    """)
    
    st.markdown("---")
    st.markdown("### 3. Điều Trị Tăng Lipid Máu")
    st.warning("""
    **Statin:**
    - Atorvastatin 20-40 mg/ngày HOẶC
    - Rosuvastatin 10-20 mg/ngày
    
    **Mục tiêu:**
    - LDL <100 mg/dL (hoặc <70 nếu nguy cơ tim mạch cao)
    - Theo dõi CK nếu có đau cơ
    
    **Lưu ý:**
    - Tăng lipid thường cải thiện khi protein niệu giảm
    - Có thể cần điều trị lâu dài
    """)
    
    st.markdown("---")
    st.markdown("### 4. Chế Độ Ăn")
    st.success("""
    **Protein:**
    - 0.8-1.0 g/kg/ngày (nếu eGFR >30)
    - 0.6-0.8 g/kg/ngày (nếu eGFR <30)
    - Chất lượng cao (thịt, cá, trứng, sữa)
    
    **Muối:**
    - <2-3 g/ngày (giảm phù, huyết áp)
    
    **Nước:**
    - 1-1.5 L/ngày nếu phù nặng
    - Bình thường nếu không phù
    
    **Tránh:**
    - NSAID (tăng nguy cơ AKI)
    - Contrast (nếu có thể)
    - Thuốc độc thận khác
    """)


def render_immunosuppression():
    """Immunosuppressive therapy based on cause"""
    st.error("## 💉 Điều Trị Nguyên Nhân (Ức Chế Miễn Dịch)")
    
    st.markdown("### Chỉ Định Điều Trị")
    st.warning("""
    **Chỉ định khi:**
    - Hội chứng thận hư nguyên phát (MCD, MN, FSGS)
    - Protein niệu >3.5 g/24h kéo dài
    - Phù nặng, kháng trị
    - Suy thận tiến triển
    
    **Chống chỉ định:**
    - Nhiễm trùng đang hoạt động
    - Suy thận giai đoạn cuối (eGFR <15)
    - Ung thư đang hoạt động
    - Thai kỳ (một số thuốc)
    """)
    
    st.markdown("---")
    st.markdown("### Phác Đồ Theo Nguyên Nhân")
    
    cause = st.selectbox(
        "**Nguyên nhân hội chứng thận hư:**",
        [
            "Minimal Change Disease (MCD)",
            "Membranous Nephropathy (MN)",
            "FSGS",
            "Lupus Nephritis (Class V)",
            "IgA Nephropathy với HCTH",
            "Chưa rõ (chờ sinh thiết)"
        ],
        key="ns_cause"
    )
    
    st.markdown("---")
    
    if "Minimal" in cause:
        render_mcd_treatment()
    elif "Membranous" in cause and "Lupus" not in cause:
        render_mn_treatment()
    elif "FSGS" in cause:
        render_fsgs_treatment()
    elif "Lupus" in cause:
        render_lupus_ns_treatment()
    elif "IgA" in cause:
        render_iga_ns_treatment()
    else:
        render_unknown_treatment()


def render_mcd_treatment():
    """MCD treatment protocol"""
    st.success("""
    **Minimal Change Disease - Phác đồ điều trị:**
    
    **Điều trị đầu tay:**
    - **Corticosteroid:**
      * Prednisone 1 mg/kg/ngày (tối đa 80 mg) × 4-8 tuần
      * Sau đó giảm dần trong 4-6 tháng
    
    - **Đáp ứng:** Thường đáp ứng trong 2-4 tuần
    
    **Tái phát thường xuyên hoặc phụ thuộc steroid:**
    - Cyclosporine 3-5 mg/kg/ngày × 12-24 tháng HOẶC
    - Tacrolimus 0.1 mg/kg/ngày × 12-24 tháng HOẶC
    - Mycophenolate 1-2 g/ngày × 12-24 tháng
    
    **Lưu ý:**
    - MCD thường đáp ứng tốt với steroid
    - Tiên lượng tốt, ít tiến triển suy thận
    - Trẻ em đáp ứng tốt hơn người lớn
    """)


def render_mn_treatment():
    """Membranous nephropathy treatment"""
    st.info("""
    **Membranous Nephropathy - Phác đồ điều trị:**
    
    **Đánh giá nguy cơ:**
    - Nguy cơ thấp: protein <4 g/24h, eGFR bình thường → ACEi/ARB + theo dõi
    - Nguy cơ cao: protein >4 g/24h hoặc suy thận → cần điều trị
    
    **Phác đồ đầu tay (nguy cơ cao):**
    - **Rituximab:** 1 g × 2 liều (cách 2 tuần) HOẶC
    - **Cyclophosphamide + Corticosteroid:**
      * Cyclophosphamide 2-2.5 mg/kg/ngày × 6 tháng
      * Prednisone 0.5 mg/kg/ngày × 6 tháng
    
    **Phác đồ thay thế:**
    - Cyclosporine 3-5 mg/kg/ngày × 6-12 tháng HOẶC
    - Tacrolimus 0.05-0.075 mg/kg/ngày × 6-12 tháng
    
    **Theo dõi:** Protein niệu, creatinine mỗi 3 tháng
    """)


def render_fsgs_treatment():
    """FSGS treatment protocol"""
    st.warning("""
    **FSGS - Phác đồ điều trị:**
    
    **Điều trị đầu tay:**
    - **Corticosteroid:**
      * Prednisone 1 mg/kg/ngày (tối đa 80 mg) × 4-16 tuần
      * Giảm dần trong 6 tháng nếu đáp ứng
    
    - **Đáp ứng:** Đánh giá sau 4-6 tháng
    
    **Không đáp ứng hoặc phụ thuộc steroid:**
    - Cyclosporine 3-5 mg/kg/ngày × 6-12 tháng HOẶC
    - Tacrolimus 0.1-0.15 mg/kg/ngày × 6-12 tháng HOẶC
    - Mycophenolate 1-2 g/ngày × 6-12 tháng
    
    **Điều trị cứu vãn:**
    - Rituximab (nếu có điều kiện)
    - Plasmapheresis (nếu nghi ngờ circulating factor)
    
    **Lưu ý:** FSGS kháng steroid có tiên lượng xấu, cần hội chẩn chuyên khoa
    """)


def render_lupus_ns_treatment():
    """Lupus nephritis with nephrotic syndrome"""
    st.error("""
    **Lupus Nephritis (Class V - Membranous) - Phác đồ điều trị:**
    
    **Nếu chỉ có Class V (không có Class III/IV):**
    - ACEi/ARB + Hydroxychloroquine
    - Corticosteroid (Prednisone 0.5 mg/kg/ngày) × 6 tháng
    - Nếu không đáp ứng: Cyclosporine hoặc Mycophenolate
    
    **Nếu có Class V + Class III/IV:**
    - Điều trị như Class III/IV (xem protocol viêm cầu thận mạn)
    - Mycophenolate 2-3 g/ngày HOẶC Cyclophosphamide
    - Corticosteroid liều cao
    
    **Lưu ý:** Cần hội chẩn thận học và thấp khớp học
    """)


def render_iga_ns_treatment():
    """IgA nephropathy with nephrotic syndrome"""
    st.info("""
    **IgA Nephropathy với Hội chứng thận hư - Phác đồ điều trị:**
    
    **Điều trị:**
    - ACEi/ARB liều tối đa
    - Corticosteroid (Prednisone 0.6-1 mg/kg/ngày) × 6 tháng
    - Nếu không đáp ứng: Cyclophosphamide hoặc Mycophenolate
    
    **Lưu ý:**
    - IgA với HCTH ít gặp
    - Cần sinh thiết để xác nhận
    - Tiên lượng phụ thuộc mô bệnh học
    """)


def render_unknown_treatment():
    """Treatment while waiting for biopsy"""
    st.warning("""
    **Chưa rõ nguyên nhân (chờ sinh thiết) - Xử trí tạm thời:**
    
    **Điều trị hỗ trợ:**
    - ACEi/ARB (nếu không chống chỉ định)
    - Lợi tiểu để giảm phù
    - Statin nếu tăng lipid
    - Chế độ ăn hạn chế muối, protein vừa phải
    
    **Tránh:**
    - Không dùng ức chế miễn dịch trước khi có chẩn đoán
    - Tránh NSAID, contrast
    
    **Sinh thiết sớm:**
    - Người lớn: nên sinh thiết sớm để có chẩn đoán
    - Trẻ em: có thể thử steroid trước (nếu nghi MCD)
    """)


def render_complications():
    """Complications and monitoring"""
    st.error("## ⚠️ Biến Chứng & Theo Dõi")
    
    st.markdown("### Biến Chứng Cần Theo Dõi")
    
    st.markdown("#### 1. Nhiễm Trùng")
    st.warning("""
    **Nguy cơ cao do:**
    - Giảm globulin miễn dịch
    - Phù → vết thương khó lành
    - Ức chế miễn dịch
    
    **Phòng ngừa:**
    - Tiêm phòng: cúm, phế cầu, COVID-19
    - Prophylaxis PCP (Trimethoprim/Sulfamethoxazole) nếu dùng steroid + ức chế miễn dịch
    - Vệ sinh da, tránh nhiễm trùng da
    
    **Điều trị:**
    - Kháng sinh sớm nếu nghi nhiễm trùng
    - Cân nhắc tạm ngừng ức chế miễn dịch nếu nhiễm trùng nặng
    """)
    
    st.markdown("---")
    st.markdown("#### 2. Huyết Khối")
    st.error("""
    **Nguy cơ cao do:**
    - Mất protein chống đông (antithrombin III)
    - Tăng đông máu
    - Giảm vận động (do phù)
    
    **Triệu chứng:**
    - DVT, PE
    - Huyết khối tĩnh mạch thận
    - Huyết khối động mạch (hiếm)
    
    **Phòng ngừa:**
    - Xem xét kháng đông dự phòng nếu albumin <2.5 g/dL
    - Vận động sớm, tránh bất động
    - Bù dịch đầy đủ
    
    **Điều trị:**
    - Kháng đông ngay nếu có huyết khối
    - Heparin/LMWH → Warfarin/Direct oral anticoagulant
    """)
    
    st.markdown("---")
    st.markdown("#### 3. Suy Thận Cấp")
    st.info("""
    **Nguyên nhân:**
    - Giảm thể tích (lợi tiểu quá mức)
    - Huyết khối tĩnh mạch thận
    - Tắc nghẽn (cục máu đông)
    - Độc thận (thuốc, contrast)
    
    **Xử trí:**
    - Bù dịch cẩn thận
    - Đánh giá nguyên nhân (siêu âm, CT)
    - Tránh lợi tiểu quá mức
    - Hội chẩn thận học nếu cần
    """)
    
    st.markdown("---")
    st.markdown("#### 4. Rối Loạn Điện Giải")
    st.warning("""
    **Tăng kali:**
    - Do suy thận, giảm aldosterone
    - Tránh ACEi/ARB nếu kali >5.5
    - Lợi tiểu giữ kali (Spironolactone) cẩn thận
    
    **Hạ natri:**
    - Do phù, giữ nước
    - Hạn chế nước nếu phù nặng
    
    **Tăng phosphate:**
    - Nếu suy thận
    - Phosphate binders nếu cần
    """)
    
    st.markdown("---")
    st.markdown("### Theo Dõi Định Kỳ")
    st.success("""
    **Mỗi 1-2 tuần (khi mới chẩn đoán hoặc đang điều trị tích cực):**
    - Protein niệu (tỷ số P/Cr)
    - Creatinine, eGFR
    - Albumin
    - Huyết áp
    - Cân nặng (đánh giá phù)
    
    **Mỗi 1-3 tháng (khi ổn định):**
    - Protein niệu 24h
    - Creatinine, eGFR
    - Albumin, lipid
    - Điện giải
    
    **Mỗi 6-12 tháng:**
    - Hemoglobin, ferritin
    - Ca, PO₄, PTH, Vitamin D
    - Siêu âm thận (nếu cần)
    """)
    
    st.markdown("---")
    st.markdown("### Khi Cần Hội Chẩn")
    st.error("""
    **Hội chẩn thận học khi:**
    - Protein niệu >3.5 g/24h kéo dài >3 tháng
    - Không đáp ứng với điều trị ban đầu
    - Cần sinh thiết thận
    - Cần điều trị ức chế miễn dịch
    - Biến chứng nặng (huyết khối, nhiễm trùng, suy thận)
    - Suy thận tiến triển
    
    **Hội chẩn đa chuyên khoa:**
    - Lupus nephritis → Thấp khớp học
    - Bệnh hệ thống khác → Chuyên khoa tương ứng
    """)

