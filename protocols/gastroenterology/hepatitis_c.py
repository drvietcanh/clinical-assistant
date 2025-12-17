"""
Hepatitis C Treatment Protocol
AASLD/IDSA 2023, EASL 2023, WHO 2022 Guidelines
Management of chronic hepatitis C infection with DAA therapy
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Hepatitis C Treatment Protocol"""
    st.subheader("🫀 Điều trị Viêm Gan C (Hepatitis C Treatment)")
    st.caption("AASLD/IDSA 2023, EASL 2023, WHO 2022 - DAA therapy for chronic hepatitis C")
    
    st.info("""
    **Viêm gan C mạn tính:**
    - Tỷ lệ nhiễm ở Việt Nam: ~2-4% dân số
    - Nguyên nhân: HCV (Hepatitis C Virus)
    - Đường lây: Máu (chủ yếu), quan hệ tình dục (hiếm)
    - Biến chứng: Xơ gan, ung thư gan (HCC)
    
    **Điều trị hiện đại (DAA):**
    - Tỷ lệ thành công: >95% (SVR12)
    - Thời gian: 8-12 tuần (ngắn)
    - An toàn, ít tác dụng phụ
    - Không cần interferon (trước đây)
    """)
    
    st.markdown("---")
    
    st.markdown("### 📊 Đánh giá Ban Đầu")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Xét nghiệm Cần Thiết")
        st.info("""
        **1. HCV Serology:**
        - Anti-HCV (screening)
        - HCV RNA (quantitative) - xác nhận
        - HCV Genotype (1-6) - quan trọng cho điều trị
        
        **2. LFTs:**
        - ALT, AST
        - Bilirubin, ALP, GGT
        
        **3. Đánh giá Gan:**
        - FibroScan / Elastography
        - APRI, FIB-4 scores
        - Ultrasound (nếu xơ gan)
        
        **4. Đồng Nhiễm:**
        - HBsAg, Anti-HIV
        - Nếu có: Điều trị đồng thời
        """)
    
    with col2:
        st.markdown("#### Phân loại Bệnh Nhân")
        genotype = st.selectbox(
            "**HCV Genotype:**",
            ["Genotype 1", "Genotype 2", "Genotype 3", "Genotype 4", "Genotype 5", "Genotype 6", "Chưa xác định"],
            key="hcv_genotype"
        )
        
        fibrosis_stage = st.selectbox(
            "**Giai đoạn Xơ Gan:**",
            ["F0-F1 (Không xơ gan)", "F2 (Xơ gan nhẹ)", "F3 (Xơ gan trung bình)", "F4 (Xơ gan nặng/Cirrhosis)"],
            key="hcv_fibrosis"
        )
        
        treatment_history = st.radio(
            "**Tiền sử điều trị:**",
            ["Chưa điều trị (Treatment-naive)", "Đã điều trị thất bại (Treatment-experienced)"],
            key="hcv_treatment_history"
        )
        
        cirrhosis_status = st.checkbox("**Có xơ gan (Cirrhosis)**", key="hcv_cirrhosis")
    
    st.markdown("---")
    
    st.markdown("### 💊 Phác Đồ Điều trị DAA")
    
    st.markdown("#### Lựa Chọn Phác Đồ")
    
    if "Genotype 1" in genotype:
        render_genotype_1(cirrhosis_status, treatment_history)
    elif "Genotype 2" in genotype:
        render_genotype_2(cirrhosis_status, treatment_history)
    elif "Genotype 3" in genotype:
        render_genotype_3(cirrhosis_status, treatment_history)
    elif "Genotype 4" in genotype:
        render_genotype_4(cirrhosis_status, treatment_history)
    elif "Genotype 6" in genotype:
        render_genotype_6(cirrhosis_status, treatment_history)
    else:
        render_unknown_genotype()
    
    st.markdown("---")
    
    st.markdown("### 📋 Phác Đồ Chi Tiết")
    
    protocol_choice = st.selectbox(
        "**Chọn phác đồ:**",
        [
            "Glecaprevir/Pibrentasvir (Mavyret) - 8 tuần",
            "Sofosbuvir/Velpatasvir (Epclusa) - 12 tuần",
            "Sofosbuvir/Ledipasvir (Harvoni) - 12 tuần",
            "Sofosbuvir/Daclatasvir - 12 tuần",
            "Elbasvir/Grazoprevir (Zepatier) - 12 tuần"
        ],
        key="hcv_protocol"
    )
    
    st.markdown("---")
    
    if "Mavyret" in protocol_choice or "Glecaprevir" in protocol_choice:
        render_mavyret()
    elif "Epclusa" in protocol_choice or "Velpatasvir" in protocol_choice:
        render_epclusa()
    elif "Harvoni" in protocol_choice or "Ledipasvir" in protocol_choice:
        render_harvoni()
    elif "Daclatasvir" in protocol_choice:
        render_sofosbuvir_daclatasvir()
    else:
        render_zepatier()
    
    st.markdown("---")
    
    st.markdown("### 📈 Theo dõi Điều trị")
    
    st.markdown("#### Lịch Theo dõi")
    
    with st.expander("📋 Xem lịch theo dõi", expanded=True):
        st.markdown("""
        **Trong điều trị:**
        - **LFTs:** Mỗi 4 tuần (nếu cần)
        - **HCV RNA:** Không cần (trừ khi có vấn đề)
        - **Clinical:** Đánh giá tác dụng phụ
        
        **Sau điều trị:**
        - **HCV RNA:** Sau 12 tuần (SVR12) - QUAN TRỌNG
        - **LFTs:** Sau 12 tuần, sau 24 tuần
        - **HBsAg:** Nếu đồng nhiễm HBV
        - **Ultrasound + AFP:** Mỗi 6 tháng (nếu xơ gan)
        
        **SVR12 (Sustained Virological Response):**
        - HCV RNA không phát hiện được sau 12 tuần
        - Tỷ lệ: >95% với DAA
        - Có nghĩa là: Đã chữa khỏi (cure)
        """)
    
    st.markdown("---")
    
    st.markdown("### ⚠️ Tác Dụng Phụ & Tương Tác")
    
    st.warning("""
    **Tác dụng phụ thường gặp:**
    - Mệt mỏi, đau đầu (nhẹ)
    - Buồn nôn, tiêu chảy (hiếm)
    - Phát ban (hiếm)
    
    **Tương tác thuốc quan trọng:**
    - **PPI:** Giảm hấp thu Ledipasvir - tránh hoặc giảm liều
    - **Rifampin, Carbamazepine:** Giảm nồng độ DAA
    - **Amiodarone:** Nguy cơ nhịp chậm nặng với Sofosbuvir
    - **Warfarin:** Theo dõi INR
    
    **Chống chỉ định:**
    - Suy gan nặng (Child-Pugh C) - một số DAA
    - Dùng với một số thuốc (xem danh sách)
    """)
    
    st.markdown("---")
    
    st.markdown("### 👥 Nhóm Bệnh Nhân Đặc Biệt")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Xơ Gan:**
        - Điều trị được, nhưng cần chọn DAA phù hợp
        - Một số DAA chống chỉ định ở Child-Pugh C
        - Theo dõi HCC sau điều trị (vẫn có nguy cơ)
        
        **Đồng Nhiễm HIV:**
        - Điều trị được, không cần điều chỉnh
        - Tương tác với ART cần kiểm tra
        - Tỷ lệ thành công tương đương
        
        **Đồng Nhiễm HBV:**
        - Điều trị HCV trước
        - Theo dõi HBV reactivation
        - Có thể cần điều trị HBV sau
        """)
    
    with col2:
        st.markdown("""
        **Suy Thận:**
        - **Sofosbuvir:** Tránh nếu eGFR <30
        - **Glecaprevir/Pibrentasvir:** An toàn ở suy thận
        - **Elbasvir/Grazoprevir:** An toàn ở suy thận
        
        **Có Thai:**
        - Dữ liệu hạn chế
        - Cân nhắc hoãn điều trị sau sinh
        - Tư vấn về nguy cơ/lợi ích
        
        **Trẻ Em:**
        - Một số DAA được phê duyệt cho trẻ em
        - Liều tính theo kg
        - Tỷ lệ thành công cao
        """)
    
    st.markdown("---")
    
    st.markdown("### 📋 Danh Sách Kiểm tra")
    
    checklist_items = [
        "✅ Xét nghiệm HCV RNA (quantitative)",
        "✅ Xác định HCV Genotype",
        "✅ Đánh giá xơ gan (FibroScan/Elastography)",
        "✅ Kiểm tra đồng nhiễm (HBV, HIV)",
        "✅ Đánh giá tương tác thuốc",
        "✅ Chọn phác đồ DAA phù hợp",
        "✅ Tư vấn về tuân thủ điều trị",
        "✅ Theo dõi HCV RNA sau 12 tuần (SVR12)",
        "✅ Theo dõi HCC nếu xơ gan",
        "✅ Tư vấn về tái nhiễm và phòng ngừa"
    ]
    
    for item in checklist_items:
        st.markdown(f"- {item}")
    
    st.markdown("---")
    
    st.markdown("### 📚 Tài liệu tham khảo")
    
    st.markdown("""
    1. **AASLD/IDSA 2023 Guidelines**
       - HCV Guidance: Recommendations for Testing, Managing, and Treating Hepatitis C
    
    2. **EASL 2023 Guidelines**
       - EASL Recommendations on Treatment of Hepatitis C
    
    3. **WHO 2022 Guidelines**
       - Guidelines for the care and treatment of persons diagnosed with chronic hepatitis C virus infection
    
    4. **UpToDate:** Treatment of chronic hepatitis C virus infection
       - Last updated: 2024
    """)
    
    st.markdown("---")
    
    # References section
    references = get_references("Hepatitis C")
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


def render_genotype_1(cirrhosis, treatment_history):
    """Genotype 1 Treatment"""
    st.success("## 💊 Điều trị Genotype 1")
    
    if cirrhosis:
        st.warning("""
        **Xơ gan (Cirrhosis):**
        - **Glecaprevir/Pibrentasvir:** 8 tuần (nếu không điều trị trước)
        - **Sofosbuvir/Velpatasvir:** 12 tuần
        - **Sofosbuvir/Ledipasvir:** 12 tuần
        - **Elbasvir/Grazoprevir:** 12 tuần (nếu không có resistance)
        """)
    else:
        st.info("""
        **Không xơ gan:**
        - **Glecaprevir/Pibrentasvir:** 8 tuần (ưu tiên)
        - **Sofosbuvir/Velpatasvir:** 12 tuần
        - **Sofosbuvir/Ledipasvir:** 12 tuần
        - **Elbasvir/Grazoprevir:** 12 tuần
        """)


def render_genotype_2(cirrhosis, treatment_history):
    """Genotype 2 Treatment"""
    st.success("## 💊 Điều trị Genotype 2")
    
    st.info("""
    **Phác đồ ưu tiên:**
    - **Glecaprevir/Pibrentasvir:** 8 tuần (không xơ gan) hoặc 12 tuần (xơ gan)
    - **Sofosbuvir/Velpatasvir:** 12 tuần
    - **Sofosbuvir + Ribavirin:** 12 tuần (nếu không có DAA khác)
    """)


def render_genotype_3(cirrhosis, treatment_history):
    """Genotype 3 Treatment"""
    st.success("## 💊 Điều trị Genotype 3")
    
    st.warning("""
    **Genotype 3: Khó điều trị hơn**
    
    **Phác đồ ưu tiên:**
    - **Glecaprevir/Pibrentasvir:** 8 tuần (không xơ gan) hoặc 12 tuần (xơ gan)
    - **Sofosbuvir/Velpatasvir:** 12 tuần
    - **Sofosbuvir/Velpatasvir + Ribavirin:** 12 tuần (nếu xơ gan + đã điều trị trước)
    """)


def render_genotype_4(cirrhosis, treatment_history):
    """Genotype 4 Treatment"""
    st.success("## 💊 Điều trị Genotype 4")
    
    st.info("""
    **Phác đồ ưu tiên:**
    - **Glecaprevir/Pibrentasvir:** 8 tuần (không xơ gan) hoặc 12 tuần (xơ gan)
    - **Sofosbuvir/Velpatasvir:** 12 tuần
    - **Sofosbuvir/Ledipasvir:** 12 tuần
    - **Elbasvir/Grazoprevir:** 12 tuần
    """)


def render_genotype_6(cirrhosis, treatment_history):
    """Genotype 6 Treatment (Common in Vietnam)"""
    st.success("## 💊 Điều trị Genotype 6 (Phổ Biến Ở Việt Nam)")
    
    st.info("""
    **Genotype 6: Phổ biến ở Việt Nam và Đông Nam Á**
    
    **Phác đồ ưu tiên:**
    - **Glecaprevir/Pibrentasvir:** 8 tuần (không xơ gan) hoặc 12 tuần (xơ gan)
    - **Sofosbuvir/Velpatasvir:** 12 tuần
    - **Sofosbuvir/Ledipasvir:** 12 tuần
    """)


def render_unknown_genotype():
    """Unknown Genotype Treatment"""
    st.warning("## ⚠️ Chưa Xác Định Genotype")
    
    st.info("""
    **Phác đồ Pan-genotypic (cho tất cả genotype):**
    - **Glecaprevir/Pibrentasvir:** 8 tuần (không xơ gan) hoặc 12 tuần (xơ gan)
    - **Sofosbuvir/Velpatasvir:** 12 tuần
    
    **Lưu ý:**
    - Nên xác định genotype trước khi điều trị
    - Pan-genotypic phù hợp nếu không có genotype
    """)


def render_mavyret():
    """Glecaprevir/Pibrentasvir Protocol"""
    st.success("## 💊 Glecaprevir/Pibrentasvir (Mavyret)")
    
    st.markdown("### Liều Dùng")
    
    st.info("""
    **Thành phần:**
    - **Glecaprevir:** 100mg
    - **Pibrentasvir:** 40mg
    
    **Liều:**
    - **3 viên** uống 1 lần/ngày (tổng: 300mg/120mg)
    - Uống với thức ăn
    
    **Thời gian:**
    - **Không xơ gan:** 8 tuần
    - **Xơ gan (F4):** 12 tuần
    - **Đã điều trị trước:** 12 tuần
    """)
    
    st.markdown("### Đặc Điểm")
    
    st.success("""
    **Ưu điểm:**
    - Pan-genotypic (tất cả genotype 1-6)
    - Thời gian ngắn (8 tuần)
    - Hiệu quả cao (>95% SVR12)
    - An toàn ở suy thận
    
    **Nhược điểm:**
    - Nhiều viên (3 viên/ngày)
    - Chống chỉ định ở Child-Pugh C
    - Tương tác với một số thuốc
    
    **Tác dụng phụ:**
    - Mệt mỏi, đau đầu (nhẹ)
    - Buồn nôn (hiếm)
    """)


def render_epclusa():
    """Sofosbuvir/Velpatasvir Protocol"""
    st.success("## 💊 Sofosbuvir/Velpatasvir (Epclusa)")
    
    st.markdown("### Liều Dùng")
    
    st.info("""
    **Thành phần:**
    - **Sofosbuvir:** 400mg
    - **Velpatasvir:** 100mg
    
    **Liều:**
    - **1 viên** uống 1 lần/ngày
    - Uống với hoặc không với thức ăn
    
    **Thời gian:**
    - **12 tuần** (hầu hết trường hợp)
    - **12 tuần + Ribavirin** (nếu genotype 3 + xơ gan + đã điều trị trước)
    """)
    
    st.markdown("### Đặc Điểm")
    
    st.success("""
    **Ưu điểm:**
    - Pan-genotypic (tất cả genotype 1-6)
    - 1 viên/ngày (tiện lợi)
    - Hiệu quả cao (>95% SVR12)
    - An toàn, ít tác dụng phụ
    
    **Nhược điểm:**
    - Tránh ở suy thận nặng (eGFR <30)
    - Tương tác với Amiodarone (nguy cơ nhịp chậm)
    
    **Tác dụng phụ:**
    - Mệt mỏi, đau đầu (nhẹ)
    - Buồn nôn (hiếm)
    """)


def render_harvoni():
    """Sofosbuvir/Ledipasvir Protocol"""
    st.success("## 💊 Sofosbuvir/Ledipasvir (Harvoni)")
    
    st.markdown("### Liều Dùng")
    
    st.info("""
    **Thành phần:**
    - **Sofosbuvir:** 400mg
    - **Ledipasvir:** 90mg
    
    **Liều:**
    - **1 viên** uống 1 lần/ngày
    - Uống với hoặc không với thức ăn
    
    **Thời gian:**
    - **12 tuần** (hầu hết trường hợp)
    - **8 tuần** (nếu không xơ gan + HCV RNA <6 million IU/mL)
    """)
    
    st.markdown("### Đặc Điểm")
    
    st.info("""
    **Ưu điểm:**
    - Hiệu quả cao với genotype 1, 4, 5, 6
    - 1 viên/ngày
    - An toàn
    
    **Nhược điểm:**
    - Không hiệu quả với genotype 2, 3
    - Tương tác với PPI (giảm hấp thu Ledipasvir)
    - Tránh ở suy thận nặng
    
    **Lưu ý PPI:**
    - Giảm liều PPI hoặc tránh dùng
    - Nếu cần: Dùng PPI cách xa Harvoni 4 giờ
    """)


def render_sofosbuvir_daclatasvir():
    """Sofosbuvir + Daclatasvir Protocol"""
    st.success("## 💊 Sofosbuvir + Daclatasvir")
    
    st.markdown("### Liều Dùng")
    
    st.info("""
    **Thành phần:**
    - **Sofosbuvir:** 400mg x 1 lần/ngày
    - **Daclatasvir:** 60mg x 1 lần/ngày
    
    **Liều:**
    - Uống riêng (2 loại thuốc)
    - Uống với hoặc không với thức ăn
    
    **Thời gian:**
    - **12 tuần** (hầu hết trường hợp)
    - **12 tuần + Ribavirin** (nếu genotype 3 + xơ gan)
    """)
    
    st.markdown("### Đặc Điểm")
    
    st.info("""
    **Ưu điểm:**
    - Pan-genotypic
    - Hiệu quả cao
    - Giá có thể thấp hơn (generic)
    
    **Nhược điểm:**
    - 2 loại thuốc riêng
    - Tránh ở suy thận nặng
    """)


def render_zepatier():
    """Elbasvir/Grazoprevir Protocol"""
    st.success("## 💊 Elbasvir/Grazoprevir (Zepatier)")
    
    st.markdown("### Liều Dùng")
    
    st.info("""
    **Thành phần:**
    - **Elbasvir:** 50mg
    - **Grazoprevir:** 100mg
    
    **Liều:**
    - **1 viên** uống 1 lần/ngày
    - Uống với hoặc không với thức ăn
    
    **Thời gian:**
    - **12 tuần** (genotype 1, 4)
    - **16 tuần** (nếu có resistance)
    """)
    
    st.markdown("### Đặc Điểm")
    
    st.info("""
    **Ưu điểm:**
    - Hiệu quả với genotype 1, 4
    - 1 viên/ngày
    - An toàn ở suy thận
    
    **Nhược điểm:**
    - Chỉ cho genotype 1, 4
    - Cần test resistance trước (genotype 1a)
    - Chống chỉ định ở Child-Pugh B, C
    """)

