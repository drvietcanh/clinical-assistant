"""
Hepatitis B Treatment Protocol
AASLD 2018, EASL 2017, WHO 2021 Guidelines
Management of chronic hepatitis B infection
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Hepatitis B Treatment Protocol"""
    st.subheader("🫀 Điều trị Viêm Gan B (Hepatitis B Treatment)")
    st.caption("AASLD 2018, EASL 2017, WHO 2021 - Management of chronic hepatitis B infection")
    
    st.info("""
    **Viêm gan B mạn tính:**
    - Tỷ lệ nhiễm ở Việt Nam: ~10-20% dân số
    - Nguyên nhân: HBV (Hepatitis B Virus)
    - Đường lây: Máu, quan hệ tình dục, mẹ sang con
    - Biến chứng: Xơ gan, ung thư gan (HCC)
    
    **Mục tiêu điều trị:**
    - Ức chế HBV DNA về mức không phát hiện được
    - HBeAg seroconversion (nếu HBeAg+)
    - HBsAg loss (mục tiêu lý tưởng)
    - Ngăn ngừa xơ gan và HCC
    """)
    
    st.markdown("---")
    
    st.markdown("### 📊 Đánh giá Ban Đầu")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Xét nghiệm Cần Thiết")
        st.info("""
        **1. HBV Serology:**
        - HBsAg (Surface antigen)
        - HBeAg / Anti-HBe
        - Anti-HBc (Total/IgM)
        - Anti-HBs
        
        **2. HBV DNA (Quantitative):**
        - Đo tải lượng virus
        - Mục tiêu: <20 IU/mL (hoặc không phát hiện)
        
        **3. LFTs:**
        - ALT, AST
        - Bilirubin, ALP, GGT
        
        **4. Đánh giá Gan:**
        - FibroScan / Elastography
        - Ultrasound
        - APRI, FIB-4 scores
        """)
    
    with col2:
        st.markdown("#### Phân loại Bệnh Nhân")
        hbeag_status = st.radio(
            "**HBeAg Status:**",
            ["HBeAg Positive", "HBeAg Negative"],
            key="hbeag_status"
        )
        
        alt_value = st.number_input(
            "**ALT (U/L):**",
            min_value=0,
            max_value=1000,
            value=80,
            key="hb_alt"
        )
        
        hbv_dna = st.number_input(
            "**HBV DNA (IU/mL):**",
            min_value=0,
            max_value=1000000000,
            value=100000,
            format="%d",
            key="hbv_dna"
        )
        
        fibrosis_stage = st.selectbox(
            "**Giai đoạn Xơ Gan:**",
            ["F0-F1 (Không xơ gan)", "F2 (Xơ gan nhẹ)", "F3 (Xơ gan trung bình)", "F4 (Xơ gan nặng/Cirrhosis)"],
            key="fibrosis_stage"
        )
    
    st.markdown("---")
    
    st.markdown("### 💊 Chỉ định Điều trị")
    
    st.markdown("#### ✅ Chỉ định Điều trị (Theo AASLD 2018)")
    
    indication_checklist = st.checkbox("**Bệnh nhân có chỉ định điều trị nếu:**", key="hb_indication")
    
    if indication_checklist:
        st.success("""
        **1. HBeAg Positive:**
        - ALT >2x ULN + HBV DNA >20,000 IU/mL
        - Hoặc ALT tăng + HBV DNA >20,000 IU/mL + Xơ gan (F3-F4)
        
        **2. HBeAg Negative:**
        - ALT >2x ULN + HBV DNA >2,000 IU/mL
        - Hoặc ALT tăng + HBV DNA >2,000 IU/mL + Xơ gan (F3-F4)
        
        **3. Xơ Gan (Cirrhosis):**
        - Bất kỳ mức HBV DNA nào (kể cả <2,000 IU/mL)
        - Cần điều trị ngay cả khi ALT bình thường
        
        **4. Nguy cơ cao HCC:**
        - Nam >40 tuổi, nữ >50 tuổi
        - Tiền sử gia đình HCC
        - HBV DNA >2,000 IU/mL
        """)
    
    st.markdown("---")
    
    st.markdown("### 💉 Thuốc Điều trị")
    
    treatment_choice = st.radio(
        "**Lựa chọn Thuốc:**",
        ["Entecavir (ETV)", "Tenofovir Disoproxil Fumarate (TDF)", "Tenofovir Alafenamide (TAF)", "Lamivudine (LAM) - Không khuyến cáo", "Adefovir (ADV) - Không khuyến cáo"],
        key="hb_treatment"
    )
    
    st.markdown("---")
    
    if "Entecavir" in treatment_choice or "ETV" in treatment_choice:
        render_entecavir()
    elif "TDF" in treatment_choice or "Disoproxil" in treatment_choice:
        render_tenofovir_tdf()
    elif "TAF" in treatment_choice or "Alafenamide" in treatment_choice:
        render_tenofovir_taf()
    elif "Lamivudine" in treatment_choice or "LAM" in treatment_choice:
        render_lamivudine()
    else:
        render_adefovir()
    
    st.markdown("---")
    
    st.markdown("### 📈 Theo dõi Điều trị")
    
    st.markdown("#### Lịch Theo dõi")
    
    with st.expander("📋 Xem lịch theo dõi", expanded=True):
        st.markdown("""
        **Trong 3 tháng đầu:**
        - **LFTs:** Mỗi 4 tuần
        - **HBV DNA:** Mỗi 12 tuần
        - **Creatinine, eGFR:** Mỗi 12 tuần (nếu dùng TDF)
        
        **Sau 3 tháng:**
        - **LFTs:** Mỗi 12 tuần
        - **HBV DNA:** Mỗi 12-24 tuần
        - **HBeAg/Anti-HBe:** Mỗi 24 tuần (nếu HBeAg+)
        - **HBsAg:** Mỗi 24-48 tuần
        - **Creatinine, eGFR:** Mỗi 24 tuần (nếu dùng TDF)
        - **Ultrasound + AFP:** Mỗi 6 tháng (nếu xơ gan hoặc nguy cơ HCC)
        
        **Đánh giá Xơ Gan:**
        - **FibroScan:** Mỗi 12-24 tháng
        - **APRI, FIB-4:** Mỗi 12 tuần
        """)
    
    st.markdown("---")
    
    st.markdown("### 🎯 Đáp Ứng Điều trị")
    
    response_type = st.radio(
        "**Loại Đáp Ứng:**",
        ["Virological Response", "Biochemical Response", "Serological Response", "Complete Response"],
        key="hb_response"
    )
    
    st.markdown("---")
    
    if "Virological" in response_type:
        st.success("""
        **Virological Response:**
        - **Mục tiêu:** HBV DNA <20 IU/mL (hoặc không phát hiện)
        - **Thời gian:** Đạt được trong 24-48 tuần
        - **Tỷ lệ:** 80-90% với ETV/TDF/TAF
        - **Nếu không đạt:** Đánh giá tuân thủ, kháng thuốc
        """)
    elif "Biochemical" in response_type:
        st.success("""
        **Biochemical Response:**
        - **Mục tiêu:** ALT bình thường
        - **Thời gian:** Thường đạt được sau virological response
        - **Tỷ lệ:** 70-80%
        """)
    elif "Serological" in response_type:
        st.success("""
        **Serological Response (HBeAg+):**
        - **Mục tiêu:** HBeAg loss + Anti-HBe+
        - **Thời gian:** 12-24 tháng
        - **Tỷ lệ:** 20-30% mỗi năm
        - **Sau HBeAg seroconversion:** Có thể giảm liều hoặc ngừng (theo dõi)
        """)
    else:
        st.success("""
        **Complete Response:**
        - **Mục tiêu:** HBsAg loss + Anti-HBs+
        - **Thời gian:** 5-10 năm (hiếm)
        - **Tỷ lệ:** 5-10% sau 5 năm
        - **Sau HBsAg loss:** Có thể ngừng điều trị (theo dõi)
        """)
    
    st.markdown("---")
    
    st.markdown("### ⚠️ Kháng Thuốc")
    
    st.warning("""
    **Dấu hiệu Kháng Thuốc:**
    - HBV DNA tăng >1 log sau khi đã giảm
    - HBV DNA không giảm sau 24 tuần
    - ALT tăng lại sau khi đã bình thường
    
    **Xử trí:**
    - **LAM/ADV resistance:** Chuyển sang ETV hoặc TDF/TAF
    - **ETV resistance:** Chuyển sang TDF/TAF
    - **TDF/TAF resistance:** Hiếm, cần genotyping
    
    **Phòng ngừa:**
    - Dùng thuốc có barrier to resistance cao (ETV, TDF, TAF)
    - Tránh LAM/ADV đơn độc
    - Tuân thủ điều trị
    """)
    
    st.markdown("---")
    
    st.markdown("### 👥 Nhóm Bệnh Nhân Đặc Biệt")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Suy thận:**
        - **ETV:** Điều chỉnh liều nếu CrCl <50 mL/min
        - **TDF:** Tránh hoặc giảm liều nếu CrCl <50 mL/min
        - **TAF:** An toàn hơn TDF ở suy thận
        
        **Có Thai:**
        - **TDF:** An toàn trong thai kỳ (Category B)
        - **ETV:** Dữ liệu hạn chế
        - **LAM:** Có thể dùng
        - **Tránh:** ADV, TAF (dữ liệu hạn chế)
        
        **Trẻ em:**
        - **ETV:** ≥2 tuổi, ≥10 kg
        - **TDF:** ≥12 tuổi
        - **LAM:** ≥2 tuổi
        """)
    
    with col2:
        st.markdown("""
        **Xơ Gan:**
        - Điều trị suốt đời
        - Theo dõi HCC mỗi 6 tháng
        - Không ngừng điều trị (nguy cơ reactivation)
        
        **Đồng Nhiễm HIV:**
        - Dùng TDF + emtricitabine (FTC) + ART
        - Tránh LAM đơn độc (nguy cơ resistance)
        
        **Đồng Nhiễm HCV:**
        - Điều trị HCV trước (DAA)
        - Sau đó đánh giá lại HBV
        """)
    
    st.markdown("---")
    
    st.markdown("### 📋 Danh Sách Kiểm tra")
    
    checklist_items = [
        "✅ Xét nghiệm HBV serology đầy đủ",
        "✅ Đo HBV DNA (quantitative)",
        "✅ Đánh giá xơ gan (FibroScan/Elastography)",
        "✅ Xác định chỉ định điều trị",
        "✅ Chọn thuốc phù hợp (ETV/TDF/TAF)",
        "✅ Theo dõi LFTs, HBV DNA định kỳ",
        "✅ Đánh giá đáp ứng điều trị",
        "✅ Theo dõi HCC nếu xơ gan hoặc nguy cơ cao",
        "✅ Đánh giá tuân thủ điều trị",
        "✅ Tư vấn về lây nhiễm và phòng ngừa"
    ]
    
    for item in checklist_items:
        st.markdown(f"- {item}")
    
    st.markdown("---")
    
    st.markdown("### 📚 Tài liệu tham khảo")
    
    st.markdown("""
    1. **AASLD 2018 Guidelines**
       - Terrault NA, et al. Hepatology. 2018
    
    2. **EASL 2017 Guidelines**
       - European Association for the Study of the Liver. J Hepatol. 2017
    
    3. **WHO 2021 Guidelines**
       - World Health Organization. Guidelines for the prevention, care and treatment of persons with chronic hepatitis B infection
    
    4. **UpToDate:** Hepatitis B virus: Overview of management
       - Last updated: 2024
    """)
    
    st.markdown("---")
    
    # References section
    references = get_references("Hepatitis B")
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


def render_entecavir():
    """Entecavir Protocol"""
    st.success("## 💊 Entecavir (ETV) - Baraclude")
    
    st.markdown("### Liều Dùng")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Người lớn (chưa điều trị LAM):**
        - **0.5 mg** uống 1 lần/ngày
        - Uống khi đói (trước hoặc sau ăn 2 giờ)
        
        **Người lớn (đã kháng LAM):**
        - **1.0 mg** uống 1 lần/ngày
        - Uống khi đói
        """)
    
    with col2:
        st.markdown("""
        **Suy thận:**
        - **CrCl ≥50:** 0.5 mg/ngày
        - **CrCl 30-49:** 0.25 mg/ngày
        - **CrCl 10-29:** 0.15 mg/ngày
        - **CrCl <10 hoặc HD:** 0.05 mg/ngày (sau HD)
        
        **Trẻ em:**
        - **≥2 tuổi, ≥10 kg:** 0.015 mg/kg/ngày (max 0.5 mg)
        """)
    
    st.markdown("### Đặc Điểm")
    
    st.info("""
    **Ưu điểm:**
    - Hiệu quả cao (90% đạt HBV DNA <20 IU/mL sau 48 tuần)
    - Barrier to resistance cao
    - An toàn, ít tác dụng phụ
    
    **Nhược điểm:**
    - Cần điều chỉnh liều ở suy thận
    - Uống khi đói
    - Dữ liệu trong thai kỳ hạn chế
    
    **Tác dụng phụ:**
    - Hiếm: Lactic acidosis (ở suy thận nặng)
    - Theo dõi: LFTs, creatinine
    """)


def render_tenofovir_tdf():
    """Tenofovir Disoproxil Fumarate Protocol"""
    st.success("## 💊 Tenofovir Disoproxil Fumarate (TDF) - Viread")
    
    st.markdown("### Liều Dùng")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Người lớn:**
        - **300 mg** uống 1 lần/ngày
        - Uống với thức ăn (tăng hấp thu)
        
        **Trẻ em:**
        - **≥12 tuổi:** 300 mg/ngày
        """)
    
    with col2:
        st.markdown("""
        **Suy thận:**
        - **CrCl ≥50:** 300 mg/ngày
        - **CrCl 30-49:** 300 mg mỗi 48 giờ
        - **CrCl 10-29:** 300 mg mỗi 72-96 giờ
        - **CrCl <10 hoặc HD:** 300 mg sau mỗi lần HD
        
        **Lưu ý:**
        - Theo dõi creatinine, eGFR, phosphate
        - Nguy cơ độc thận (hiếm)
        """)
    
    st.markdown("### Đặc Điểm")
    
    st.info("""
    **Ưu điểm:**
    - Hiệu quả cao (90% đạt HBV DNA <20 IU/mL)
    - Barrier to resistance rất cao
    - An toàn trong thai kỳ (Category B)
    - Có thể dùng với thức ăn
    
    **Nhược điểm:**
    - Nguy cơ độc thận, giảm mật độ xương (dài hạn)
    - Cần theo dõi creatinine, phosphate
    
    **Tác dụng phụ:**
    - Độc thận (hiếm, thường ở suy thận)
    - Giảm mật độ xương (dài hạn)
    - Theo dõi: Creatinine, eGFR, phosphate, BMD
    """)


def render_tenofovir_taf():
    """Tenofovir Alafenamide Protocol"""
    st.success("## 💊 Tenofovir Alafenamide (TAF) - Vemlidy")
    
    st.markdown("### Liều Dùng")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Người lớn:**
        - **25 mg** uống 1 lần/ngày
        - Uống với thức ăn (tăng hấp thu)
        
        **Trẻ em:**
        - **≥12 tuổi, ≥35 kg:** 25 mg/ngày
        """)
    
    with col2:
        st.markdown("""
        **Suy thận:**
        - **CrCl ≥15:** 25 mg/ngày
        - **CrCl <15 hoặc HD:** Chưa có dữ liệu
        
        **Lưu ý:**
        - An toàn hơn TDF ở suy thận
        - Ít ảnh hưởng đến mật độ xương
        """)
    
    st.markdown("### Đặc Điểm")
    
    st.info("""
    **Ưu điểm:**
    - Hiệu quả tương đương TDF
    - An toàn hơn TDF ở suy thận
    - Ít ảnh hưởng đến mật độ xương
    - Barrier to resistance rất cao
    
    **Nhược điểm:**
    - Giá cao hơn TDF
    - Dữ liệu trong thai kỳ hạn chế
    
    **Tác dụng phụ:**
    - Ít hơn TDF
    - Theo dõi: LFTs, creatinine (ít cần hơn TDF)
    """)


def render_lamivudine():
    """Lamivudine Protocol (Not Recommended)"""
    st.warning("## ⚠️ Lamivudine (LAM) - Không Khuyến cáo")
    
    st.error("""
    **Lý do không khuyến cáo:**
    - Tỷ lệ kháng thuốc cao (70% sau 5 năm)
    - Barrier to resistance thấp
    - Hiện tại: Chỉ dùng khi không có lựa chọn khác
    
    **Nếu bắt buộc dùng:**
    - **Liều:** 100 mg uống 1 lần/ngày
    - **Theo dõi:** HBV DNA sát (mỗi 12 tuần)
    - **Chuyển sang:** ETV hoặc TDF/TAF nếu kháng thuốc
    """)


def render_adefovir():
    """Adefovir Protocol (Not Recommended)"""
    st.warning("## ⚠️ Adefovir (ADV) - Không Khuyến cáo")
    
    st.error("""
    **Lý do không khuyến cáo:**
    - Hiệu quả thấp hơn ETV/TDF/TAF
    - Nguy cơ độc thận
    - Tỷ lệ kháng thuốc cao
    
    **Hiện tại:**
    - Không còn được khuyến cáo
    - Chỉ dùng trong trường hợp đặc biệt
    """)

