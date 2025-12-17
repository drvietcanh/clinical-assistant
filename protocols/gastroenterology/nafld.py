"""
NAFLD/NASH Management Protocol
AASLD 2018, EASL 2021 Guidelines
Management of non-alcoholic fatty liver disease and steatohepatitis
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """NAFLD/NASH Management Protocol"""
    st.subheader("🫀 Điều trị Bệnh Gan Nhiễm Mỡ Không Do Rượu (NAFLD/NASH)")
    st.caption("AASLD 2018, EASL 2021 - Management of NAFLD and NASH")
    
    st.info("""
    **Bệnh gan nhiễm mỡ không do rượu (NAFLD):**
    - Tỷ lệ ở Việt Nam: ~15-25% dân số (đang tăng)
    - Định nghĩa: Tích tụ mỡ trong gan >5% (không do rượu)
    - Phân loại:
      - **NAFL (Simple Steatosis):** Chỉ có mỡ, không viêm
      - **NASH (Steatohepatitis):** Có mỡ + viêm + tổn thương tế bào gan
    - Nguyên nhân: Béo phì, đái tháo đường, rối loạn lipid máu
    - Biến chứng: Xơ gan, HCC
    
    **Yếu tố nguy cơ:**
    - Béo phì (BMI >25)
    - Đái tháo đường type 2
    - Rối loạn lipid máu
    - Hội chứng chuyển hóa
    """)
    
    st.markdown("---")
    
    st.markdown("### 📊 Chẩn đoán")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Tiêu chuẩn Chẩn đoán")
        st.info("""
        **Chẩn đoán NAFLD khi:**
        1. Có mỡ trong gan (hình ảnh hoặc sinh thiết)
        2. Loại trừ nguyên nhân khác:
           - Rượu (<30g/ngày nam, <20g/ngày nữ)
           - Thuốc (corticosteroid, tamoxifen)
           - Bệnh gan khác (viêm gan B/C, tự miễn)
        
        **Chẩn đoán NASH:**
        - Sinh thiết gan: Mỡ + viêm + tổn thương tế bào
        - Hoặc: Lâm sàng + xét nghiệm + hình ảnh
        """)
        
        diagnosis_method = st.radio(
            "**Phương pháp chẩn đoán:**",
            ["Lâm sàng + Xét nghiệm", "Hình ảnh (US/CT/MRI)", "Sinh thiết gan"],
            key="nafld_diagnosis"
        )
    
    with col2:
        st.markdown("#### Đánh giá")
        bmi = st.number_input(
            "**BMI (kg/m²):**",
            min_value=15.0,
            max_value=50.0,
            value=28.0,
            step=0.1,
            key="nafld_bmi"
        )
        
        has_diabetes = st.checkbox("**Có đái tháo đường**", key="nafld_diabetes")
        
        alt_value = st.number_input(
            "**ALT (U/L):**",
            min_value=0,
            max_value=1000,
            value=60,
            key="nafld_alt"
        )
        
        fibrosis_stage = st.selectbox(
            "**Giai đoạn xơ gan (nếu có):**",
            ["F0 (Không xơ gan)", "F1 (Xơ gan nhẹ)", "F2 (Xơ gan trung bình)", "F3 (Xơ gan nặng)", "F4 (Cirrhosis)", "Chưa đánh giá"],
            key="nafld_fibrosis"
        )
    
    st.markdown("---")
    
    st.markdown("### 💊 Điều trị")
    
    st.markdown("#### 1. Thay Đổi Lối Sống")
    
    st.success("""
    **Giảm cân:**
    - **Mục tiêu:** Giảm 5-10% trọng lượng cơ thể
    - **Tốc độ:** 0.5-1kg/tuần
    - **Phương pháp:** Chế độ ăn + tập thể dục
    
    **Chế độ ăn:**
    - **Calorie restriction:** Giảm 500-1000 kcal/ngày
    - **Mediterranean diet:** Ưu tiên
    - **Tránh:** Đường, fructose, chất béo bão hòa
    - **Tăng:** Chất xơ, omega-3
    
    **Tập thể dục:**
    - **Aerobic:** ≥150 phút/tuần (cường độ vừa)
    - **Resistance training:** 2-3 lần/tuần
    - **Kết hợp:** Tốt nhất
    """)
    
    st.markdown("#### 2. Điều trị Bệnh Đi Kèm")
    
    st.info("""
    **Đái tháo đường:**
    - **Metformin:** Có thể giúp
    - **Pioglitazone:** Có thể cải thiện NASH (nếu không có đái tháo đường)
    - **GLP-1 agonists:** Semaglutide, Liraglutide (có thể giúp)
    - **SGLT2 inhibitors:** Có thể giúp
    
    **Rối loạn lipid máu:**
    - **Statins:** An toàn ở NAFLD, có thể giúp
    - **Omega-3:** Có thể giúp giảm triglyceride
    
    **Tăng huyết áp:**
    - **ACE inhibitors/ARBs:** Ưu tiên
    """)
    
    st.markdown("#### 3. Thuốc Điều trị NASH")
    
    treatment_choice = st.selectbox(
        "**Chọn điều trị:**",
        [
            "Vitamin E (Nếu không có đái tháo đường)",
            "Pioglitazone (Nếu có đái tháo đường hoặc không)",
            "Obeticholic Acid (OCA)",
            "Semaglutide (GLP-1 agonist)"
        ],
        key="nafld_treatment"
    )
    
    st.markdown("---")
    
    if "Vitamin E" in treatment_choice:
        render_vitamin_e()
    elif "Pioglitazone" in treatment_choice:
        render_pioglitazone()
    elif "Obeticholic" in treatment_choice or "OCA" in treatment_choice:
        render_oca()
    else:
        render_semaglutide()
    
    st.markdown("---")
    
    st.markdown("### 📈 Theo dõi")
    
    with st.expander("📋 Xem lịch theo dõi", expanded=True):
        st.markdown("""
        **Theo dõi định kỳ:**
        - **LFTs:** Mỗi 6-12 tháng
        - **BMI, cân nặng:** Mỗi 3-6 tháng
        - **Đường huyết, HbA1c:** Mỗi 3-6 tháng (nếu có đái tháo đường)
        - **Lipid:** Mỗi 6-12 tháng
        
        **Đánh giá xơ gan:**
        - **FibroScan/Elastography:** Mỗi 1-2 năm
        - **APRI, FIB-4:** Mỗi 6-12 tháng
        
        **Tầm soát HCC:**
        - **Nếu xơ gan (F4):** Ultrasound + AFP mỗi 6 tháng
        - **Nếu F3:** Cân nhắc tầm soát
        """)
    
    st.markdown("---")
    
    st.markdown("### ⚠️ Tiên lượng")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("""
        **Tiên lượng tốt:**
        - NAFL (không có viêm)
        - Giảm cân thành công
        - Kiểm soát tốt đái tháo đường
        - Không có xơ gan
        """)
    
    with col2:
        st.warning("""
        **Tiên lượng xấu:**
        - NASH (có viêm)
        - Xơ gan (F3-F4)
        - Không kiểm soát được cân nặng
        - Đái tháo đường không kiểm soát
        - Nguy cơ tiến triển thành xơ gan, HCC
        """)
    
    st.markdown("---")
    
    st.markdown("### 👥 Nhóm Bệnh Nhân Đặc Biệt")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Béo phì nặng (BMI >35):**
        - Cân nhắc phẫu thuật giảm cân (bariatric surgery)
        - Có thể cải thiện NASH đáng kể
        
        **Có thai:**
        - Tránh giảm cân trong thai kỳ
        - Kiểm soát đường huyết
        - Theo dõi sát
        """)
    
    with col2:
        st.markdown("""
        **Trẻ em:**
        - NAFLD đang tăng ở trẻ em
        - Điều trị tương tự (giảm cân, tập thể dục)
        - Cẩn thận với thuốc (dữ liệu hạn chế)
        
        **Người cao tuổi:**
        - Nguy cơ xơ gan cao hơn
        - Cần theo dõi sát
        """)
    
    st.markdown("---")
    
    st.markdown("### 📋 Danh Sách Kiểm tra")
    
    checklist_items = [
        "✅ Chẩn đoán NAFLD/NASH (loại trừ nguyên nhân khác)",
        "✅ Đánh giá xơ gan (FibroScan/Elastography)",
        "✅ Đánh giá bệnh đi kèm (đái tháo đường, rối loạn lipid)",
        "✅ Tư vấn giảm cân (mục tiêu 5-10%)",
        "✅ Tư vấn chế độ ăn (Mediterranean diet)",
        "✅ Tư vấn tập thể dục (≥150 phút/tuần)",
        "✅ Điều trị bệnh đi kèm (đái tháo đường, rối loạn lipid)",
        "✅ Cân nhắc thuốc điều trị NASH (Vitamin E, Pioglitazone)",
        "✅ Theo dõi LFTs, BMI định kỳ",
        "✅ Tầm soát HCC nếu xơ gan"
    ]
    
    for item in checklist_items:
        st.markdown(f"- {item}")
    
    st.markdown("---")
    
    st.markdown("### 📚 Tài liệu tham khảo")
    
    st.markdown("""
    1. **AASLD 2018 Guidelines**
       - Chalasani N, et al. Hepatology. 2018
    
    2. **EASL 2021 Guidelines**
       - European Association for the Study of the Liver. J Hepatol. 2021
    
    3. **UpToDate:** Management of nonalcoholic fatty liver disease in adults
       - Last updated: 2024
    """)
    
    st.markdown("---")
    
    # References section
    references = get_references("NAFLD")
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


def render_vitamin_e():
    """Vitamin E Treatment"""
    st.success("## 💊 Vitamin E")
    
    st.markdown("### Liều Dùng")
    
    st.info("""
    **Vitamin E:**
    - **Liều:** 800 IU/ngày
    - **Chỉ định:** NASH (sinh thiết xác nhận) + không có đái tháo đường
    - **Thời gian:** Dài hạn
    
    **Hiệu quả:**
    - Cải thiện NASH (viêm, tổn thương tế bào)
    - Không cải thiện xơ gan
    
    **Tác dụng phụ:**
    - Tăng nguy cơ xuất huyết (liều cao)
    - Tăng nguy cơ ung thư tuyến tiền liệt (nam giới)
    
    **Lưu ý:**
    - Không dùng nếu có đái tháo đường
    - Không dùng nếu đang dùng warfarin
    """)


def render_pioglitazone():
    """Pioglitazone Treatment"""
    st.success("## 💊 Pioglitazone")
    
    st.markdown("### Liều Dùng")
    
    st.info("""
    **Pioglitazone:**
    - **Liều:** 30-45mg/ngày
    - **Chỉ định:** NASH (sinh thiết xác nhận) + có hoặc không có đái tháo đường
    - **Thời gian:** Dài hạn
    
    **Hiệu quả:**
    - Cải thiện NASH (viêm, tổn thương tế bào)
    - Cải thiện xơ gan (một phần)
    - Cải thiện đái tháo đường
    
    **Tác dụng phụ:**
    - Tăng cân
    - Phù
    - Tăng nguy cơ gãy xương (phụ nữ)
    - Tăng nguy cơ suy tim (nếu có bệnh tim)
    
    **Lưu ý:**
    - Chống chỉ định ở suy tim
    - Theo dõi cân nặng, phù
    """)


def render_oca():
    """Obeticholic Acid Treatment"""
    st.info("## 💊 Obeticholic Acid (OCA)")
    
    st.markdown("### Liều Dùng")
    
    st.info("""
    **Obeticholic Acid:**
    - **Liều:** 25mg/ngày (tăng dần từ 5mg)
    - **Chỉ định:** NASH với xơ gan (F2-F3)
    - **Thời gian:** Dài hạn
    
    **Hiệu quả:**
    - Cải thiện xơ gan
    - Cải thiện NASH
    
    **Tác dụng phụ:**
    - Ngứa (phổ biến)
    - Tăng cholesterol LDL
    - Tăng nguy cơ sỏi mật
    
    **Lưu ý:**
    - Đắt tiền
    - Cần theo dõi cholesterol
    """)


def render_semaglutide():
    """Semaglutide Treatment"""
    st.info("## 💊 Semaglutide (GLP-1 Agonist)")
    
    st.markdown("### Liều Dùng")
    
    st.info("""
    **Semaglutide:**
    - **Liều:** 0.25-1mg/tuần (tiêm dưới da)
    - **Chỉ định:** NASH + béo phì/đái tháo đường
    - **Thời gian:** Dài hạn
    
    **Hiệu quả:**
    - Giảm cân đáng kể
    - Cải thiện NASH
    - Cải thiện đái tháo đường
    
    **Tác dụng phụ:**
    - Buồn nôn, nôn (thường gặp)
    - Tiêu chảy
    - Nguy cơ viêm tụy (hiếm)
    
    **Lưu ý:**
    - Bắt đầu liều thấp, tăng dần
    - Theo dõi tác dụng phụ
    """)

