"""
Cirrhosis Management Protocol
AASLD 2021, EASL 2018 Guidelines
Management of cirrhosis and its complications
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Cirrhosis Management Protocol"""
    st.subheader("🫀 Quản lý Xơ Gan (Cirrhosis Management)")
    st.caption("AASLD 2021, EASL 2018 - Management of cirrhosis and complications")
    
    st.info("""
    **Xơ gan (Cirrhosis):**
    - Tỷ lệ ở Việt Nam: ~2-5% dân số (ước tính)
    - Định nghĩa: Tổn thương gan mạn tính, không hồi phục, thay thế mô gan bằng mô xơ
    - Nguyên nhân: Viêm gan B/C, rượu, NAFLD, viêm gan tự miễn
    - Biến chứng: Cổ trướng, xuất huyết tiêu hóa, bệnh não gan, HCC
    
    **Phân loại:**
    - **Compensated:** Chưa có biến chứng
    - **Decompensated:** Có biến chứng (cổ trướng, xuất huyết, bệnh não gan)
    """)
    
    st.markdown("---")
    
    st.markdown("### 📊 Đánh giá Ban Đầu")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Chẩn đoán")
        st.info("""
        **Lâm sàng:**
        - Tiền sử: Viêm gan B/C, rượu, béo phì
        - Triệu chứng: Mệt mỏi, vàng da, cổ trướng
        - Khám: Gan to/nhỏ, lách to, dấu hiệu tăng áp lực tĩnh mạch cửa
        
        **Xét nghiệm:**
        - LFTs: ALT, AST, Bilirubin, ALP, GGT
        - Chức năng gan: Albumin, PT/INR
        - Công thức máu: Giảm tiểu cầu (tăng áp lực tĩnh mạch cửa)
        - AFP: Tầm soát HCC
        
        **Hình ảnh:**
        - Ultrasound: Gan nhỏ, bờ không đều, cổ trướng
        - FibroScan/Elastography: Đo độ cứng gan
        - CT/MRI: Đánh giá cấu trúc, HCC
        """)
    
    with col2:
        st.markdown("#### Phân loại")
        cirrhosis_stage = st.selectbox(
            "**Giai đoạn xơ gan:**",
            ["Compensated (Chưa mất bù)", "Decompensated (Đã mất bù)"],
            key="cirrhosis_stage"
        )
        
        child_pugh = st.selectbox(
            "**Child-Pugh Score:**",
            ["A (5-6 điểm)", "B (7-9 điểm)", "C (10-15 điểm)", "Chưa đánh giá"],
            key="child_pugh"
        )
        
        meld_score = st.number_input(
            "**MELD Score:**",
            min_value=6,
            max_value=40,
            value=15,
            key="meld_score"
        )
        
        etiology = st.selectbox(
            "**Nguyên nhân:**",
            ["Viêm gan B", "Viêm gan C", "Rượu", "NAFLD/NASH", "Viêm gan tự miễn", "Khác"],
            key="cirrhosis_etiology"
        )
    
    st.markdown("---")
    
    st.markdown("### 💊 Điều trị Nguyên nhân")
    
    if "Viêm gan B" in etiology:
        st.warning("""
        **Điều trị viêm gan B:**
        - **Entecavir:** 0.5-1.0 mg/ngày
        - **Tenofovir (TDF/TAF):** 300mg/25mg/ngày
        - **Mục tiêu:** Ức chế HBV DNA
        - **Theo dõi:** HBV DNA, LFTs mỗi 3-6 tháng
        """)
    elif "Viêm gan C" in etiology:
        st.warning("""
        **Điều trị viêm gan C:**
        - **DAA therapy:** Glecaprevir/Pibrentasvir, Sofosbuvir/Velpatasvir
        - **Mục tiêu:** SVR12 (chữa khỏi)
        - **Lưu ý:** Chọn DAA phù hợp với Child-Pugh
        """)
    elif "Rượu" in etiology:
        st.warning("""
        **Điều trị:**
        - **Bỏ rượu hoàn toàn:** Quan trọng nhất
        - **Hỗ trợ cai rượu:** Nếu cần
        - **Vitamin B1, B12, Folate:** Bổ sung
        """)
    elif "NAFLD" in etiology or "NASH" in etiology:
        st.warning("""
        **Điều trị:**
        - **Giảm cân:** 5-10% trọng lượng cơ thể
        - **Kiểm soát đái tháo đường:** Nếu có
        - **Vitamin E:** 800 IU/ngày (nếu không có đái tháo đường)
        - **Pioglitazone:** Có thể xem xét
        """)
    else:
        st.info("""
        **Điều trị theo nguyên nhân:**
        - Viêm gan tự miễn: Corticosteroids
        - Wilson: Penicillamine, Trientine
        - Hemochromatosis: Chích máu
        """)
    
    st.markdown("---")
    
    st.markdown("### 🔴 Quản lý Biến Chứng")
    
    complication = st.selectbox(
        "**Biến chứng:**",
        [
            "Cổ trướng (Ascites)",
            "Xuất huyết tiêu hóa (Variceal Bleeding)",
            "Bệnh não gan (Hepatic Encephalopathy)",
            "Hội chứng gan thận (HRS)",
            "Nhiễm trùng (SBP)",
            "Ung thư gan (HCC)"
        ],
        key="cirrhosis_complication"
    )
    
    st.markdown("---")
    
    if "Cổ trướng" in complication or "Ascites" in complication:
        render_ascites()
    elif "Xuất huyết" in complication or "Variceal" in complication:
        render_variceal_bleeding()
    elif "Bệnh não" in complication or "Encephalopathy" in complication:
        render_hepatic_encephalopathy()
    elif "Hội chứng gan thận" in complication or "HRS" in complication:
        render_hepatorenal_syndrome()
    elif "Nhiễm trùng" in complication or "SBP" in complication:
        render_spontaneous_bacterial_peritonitis()
    else:
        render_hcc()
    
    st.markdown("---")
    
    st.markdown("### 📋 Theo dõi & Tầm Soát")
    
    with st.expander("📋 Xem lịch theo dõi", expanded=True):
        st.markdown("""
        **Theo dõi định kỳ:**
        - **LFTs, Albumin, PT/INR:** Mỗi 3-6 tháng
        - **Công thức máu:** Mỗi 3-6 tháng
        - **AFP:** Mỗi 6 tháng (tầm soát HCC)
        - **Ultrasound + AFP:** Mỗi 6 tháng (tầm soát HCC)
        - **Endoscopy:** Mỗi 1-3 năm (tầm soát giãn tĩnh mạch thực quản)
        
        **Tầm soát HCC:**
        - **Bắt đầu:** Khi chẩn đoán xơ gan
        - **Tần suất:** Mỗi 6 tháng
        - **Phương pháp:** Ultrasound + AFP
        - **Nếu có khối u:** CT/MRI với contrast
        
        **Tầm soát giãn tĩnh mạch thực quản:**
        - **Bắt đầu:** Khi chẩn đoán xơ gan
        - **Tần suất:** Mỗi 1-3 năm (tùy Child-Pugh)
        - **Nếu có giãn:** Điều trị dự phòng
        """)
    
    st.markdown("---")
    
    st.markdown("### 👥 Nhóm Bệnh Nhân Đặc Biệt")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Xơ gan Compensated:**
        - Tiên lượng tốt hơn
        - Tập trung điều trị nguyên nhân
        - Tầm soát biến chứng
        - Tránh thuốc độc gan
        
        **Xơ gan Decompensated:**
        - Tiên lượng xấu hơn
        - Quản lý biến chứng tích cực
        - Đánh giá transplant
        - MELD score để ưu tiên transplant
        """)
    
    with col2:
        st.markdown("""
        **Có thai:**
        - Nguy cơ cao cho mẹ và thai nhi
        - Theo dõi sát
        - Tránh thuốc độc gan
        - Cân nhắc chấm dứt thai kỳ nếu nặng
        
        **Trẻ em:**
        - Nguyên nhân thường khác (bẩm sinh, rối loạn chuyển hóa)
        - Điều trị theo nguyên nhân
        - Cân nhắc transplant sớm
        """)
    
    st.markdown("---")
    
    st.markdown("### 📋 Danh Sách Kiểm tra")
    
    checklist_items = [
        "✅ Chẩn đoán xơ gan (lâm sàng, xét nghiệm, hình ảnh)",
        "✅ Xác định nguyên nhân và điều trị",
        "✅ Đánh giá Child-Pugh và MELD score",
        "✅ Tầm soát HCC (Ultrasound + AFP mỗi 6 tháng)",
        "✅ Tầm soát giãn tĩnh mạch thực quản (Endoscopy)",
        "✅ Quản lý biến chứng nếu có",
        "✅ Tránh thuốc độc gan",
        "✅ Tiêm phòng (Hepatitis A, B, Pneumococcus, Influenza)",
        "✅ Đánh giá transplant nếu decompensated",
        "✅ Tư vấn về chế độ ăn và lối sống"
    ]
    
    for item in checklist_items:
        st.markdown(f"- {item}")
    
    st.markdown("---")
    
    st.markdown("### 📚 Tài liệu tham khảo")
    
    st.markdown("""
    1. **AASLD 2021 Guidelines**
       - Management of cirrhosis and its complications
    
    2. **EASL 2018 Guidelines**
       - EASL Clinical Practice Guidelines for the management of patients with decompensated cirrhosis
    
    3. **UpToDate:** Cirrhosis in adults: Overview of complications, general management, and prognosis
       - Last updated: 2024
    """)
    
    st.markdown("---")
    
    # References section
    references = get_references("Cirrhosis")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-01-15",
            show_evidence_level=True,
            show_links=True
        )
    
    st.markdown("---")
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất.")


def render_ascites():
    """Ascites Management"""
    st.error("## 🔴 Cổ Trướng (Ascites)")
    
    st.markdown("### Điều trị")
    
    st.warning("""
    **1. Hạn chế muối:**
    - **<2g/ngày** (88 mEq/ngày)
    - Quan trọng nhất
    
    **2. Hạn chế nước:**
    - Chỉ khi Na <125 mEq/L
    - Thường không cần
    
    **3. Lợi tiểu:**
    - **Spironolactone:** 100-400mg/ngày (tăng dần)
    - **Furosemide:** 40-160mg/ngày (nếu cần)
    - **Tỷ lệ:** Spironolactone:Furosemide = 100:40
    
    **4. Paracentesis:**
    - Nếu cổ trướng nhiều, khó thở
    - Truyền Albumin: 6-8g/L dịch rút ra
    """)
    
    st.markdown("### Theo dõi")
    
    st.info("""
    - **Cân nặng:** Mỗi ngày
    - **Điện giải:** Na, K mỗi 3-7 ngày
    - **Creatinine:** Mỗi 3-7 ngày
    - **Mục tiêu:** Giảm 0.5-1kg/ngày (nếu phù)
    """)


def render_variceal_bleeding():
    """Variceal Bleeding Management"""
    st.error("## 🔴 Xuất huyết Giãn Tĩnh Mạch Thực Quản")
    
    st.markdown("### Dự Phòng Sơ Cấp")
    
    st.warning("""
    **Nếu có giãn tĩnh mạch thực quản:**
    - **Non-selective beta blocker:** Propranolol, Nadolol
    - **Liều:** Giảm nhịp tim 25% hoặc 50-55 bpm
    - **Hoặc:** Endoscopic variceal ligation (EVL)
    """)
    
    st.markdown("### Điều trị Cấp cứu")
    
    st.error("""
    **1. Hồi sức:**
    - Truyền máu (Hb <7g/dL)
    - Truyền FFP nếu INR >1.5
    
    **2. Thuốc:**
    - **Octreotide:** 50mcg bolus, sau đó 50mcg/h
    - **Terlipressin:** 2mg q6h (nếu có)
    
    **3. Endoscopy:**
    - Trong vòng 12 giờ
    - Band ligation hoặc sclerotherapy
    
    **4. Dự phòng thứ phát:**
    - Beta blocker + EVL
    """)


def render_hepatic_encephalopathy():
    """Hepatic Encephalopathy Management"""
    st.error("## 🔴 Bệnh Não Gan (Hepatic Encephalopathy)")
    
    st.markdown("### Điều trị")
    
    st.warning("""
    **1. Điều trị nguyên nhân:**
    - Nhiễm trùng (SBP)
    - Xuất huyết tiêu hóa
    - Táo bón
    - Thuốc (benzodiazepine, opioid)
    
    **2. Lactulose:**
    - **Liều:** 15-30mL x 2-4 lần/ngày
    - **Mục tiêu:** 2-3 lần đại tiện/ngày
    
    **3. Rifaximin:**
    - **Liều:** 550mg x 2 lần/ngày
    - **Phối hợp:** Với Lactulose
    
    **4. Hỗ trợ:**
    - Hạn chế protein (tạm thời)
    - Bổ sung BCAA nếu cần
    """)


def render_hepatorenal_syndrome():
    """Hepatorenal Syndrome Management"""
    st.error("## 🔴 Hội Chứng Gan Thận (HRS)")
    
    st.markdown("### Chẩn đoán")
    
    st.info("""
    **Tiêu chuẩn:**
    - Xơ gan + cổ trướng
    - Creatinine >1.5 mg/dL hoặc tăng >50%
    - Không cải thiện sau 2 ngày ngừng lợi tiểu + truyền Albumin
    - Loại trừ: Nhiễm trùng, thuốc, bệnh thận khác
    """)
    
    st.markdown("### Điều trị")
    
    st.warning("""
    **1. Terlipressin:**
    - **Liều:** 0.5-2mg q6h
    - **Phối hợp:** Albumin 1g/kg/ngày
    
    **2. Norepinephrine:**
    - Nếu không có Terlipressin
    - **Liều:** 0.5-3mg/h
    
    **3. Transplant:**
    - Chỉ định nếu đáp ứng
    """)


def render_spontaneous_bacterial_peritonitis():
    """SBP Management"""
    st.error("## 🔴 Viêm Phúc Mạc Tự Phát (SBP)")
    
    st.markdown("### Chẩn đoán")
    
    st.info("""
    **Paracentesis:**
    - PMN >250 cells/mm³
    - Cấy dịch cổ trướng
    """)
    
    st.markdown("### Điều trị")
    
    st.warning("""
    **1. Kháng sinh:**
    - **Cefotaxime:** 2g q8h x 5 ngày
    - **Hoặc:** Ceftriaxone 2g q24h x 5 ngày
    
    **2. Albumin:**
    - **Ngày 1:** 1.5g/kg
    - **Ngày 3:** 1g/kg
    
    **3. Dự phòng:**
    - **Norfloxacin:** 400mg/ngày (nếu có nguy cơ)
    """)


def render_hcc():
    """HCC Screening and Management"""
    st.error("## 🔴 Ung Thư Gan (HCC)")
    
    st.markdown("### Tầm Soát")
    
    st.info("""
    **Phương pháp:**
    - **Ultrasound + AFP:** Mỗi 6 tháng
    - **Bắt đầu:** Khi chẩn đoán xơ gan
    
    **Tiêu chuẩn chẩn đoán:**
    - Khối u >1cm + AFP >200 ng/mL
    - Hoặc: CT/MRI với contrast (arterial enhancement + washout)
    """)
    
    st.markdown("### Điều trị")
    
    st.warning("""
    **Theo giai đoạn (BCLC):**
    - **Early (A):** Resection, RFA, TACE, Transplant
    - **Intermediate (B):** TACE
    - **Advanced (C):** Sorafenib, Lenvatinib
    - **Terminal (D):** Hỗ trợ
    """)

