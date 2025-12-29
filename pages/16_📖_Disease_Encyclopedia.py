"""
Disease Encyclopedia Module
Comprehensive information about diseases and conditions
"""

import streamlit as st
from utils.page_helper import setup_page, render_standard_footer
from diseases.search import (
    search_diseases,
    get_disease_info,
    get_diseases_by_symptom
)
from diseases.data import (
    get_all_diseases,
    get_diseases_by_category,
    get_category_list
)

# Standard page setup
setup_page(
    page_title="Bách khoa Bệnh lý",
    page_icon="📖",
    description="Thông tin toàn diện về các bệnh lý phổ biến"
)

# ========== SIDEBAR ==========
with st.sidebar:
    st.header("📖 Bách khoa Bệnh lý")
    st.caption("Module **Bách khoa Bệnh lý** – thông tin chi tiết về các bệnh lý.")
    
    view_mode = st.radio(
        "Chế độ xem:",
        ["Tìm kiếm", "Theo chuyên khoa", "Theo triệu chứng"],
        key="disease_view_mode"
    )
    
    if view_mode == "Theo chuyên khoa":
        category_filter = st.selectbox(
            "Chọn chuyên khoa:",
            ["Tất cả"] + get_category_list(),
            key="disease_category_filter"
        )
    
    st.markdown("---")
    st.info("""
    **📖 Disease Encyclopedia:**
    - Thông tin chi tiết về **bệnh lý phổ biến**
    - **Định nghĩa, nguyên nhân, triệu chứng**
    - **Chẩn đoán và điều trị**
    - **Liên kết** với protocols, scores, drugs
    
    **💡 Lưu ý:**
    - Database hiện tại bao gồm các bệnh phổ biến nhất
    - Thông tin chỉ mang tính tham khảo
    - Luôn tham khảo guidelines mới nhất
    """)

# ========== MAIN CONTENT ==========

st.markdown("## 📖 Bách khoa Bệnh lý")
st.markdown("""
**Thông tin toàn diện về các bệnh lý phổ biến**

Bao gồm: định nghĩa, nguyên nhân, triệu chứng, chẩn đoán, điều trị, và phòng ngừa
""")


def render_disease_detail(disease):
    """Render detailed disease information"""
    # Basic info
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"**Tên tiếng Việt:** {disease.name_vn}")
        st.markdown(f"**Tên tiếng Anh:** {disease.name}")
        st.markdown(f"**Chuyên khoa:** {disease.category}")
    with col2:
        if disease.icd10_codes:
            st.markdown(f"**Mã ICD-10:** {', '.join(disease.icd10_codes)}")
    
    # Definition
    if disease.definition:
        st.markdown("---")
        st.markdown("### 📝 Định nghĩa")
        st.info(disease.definition)
    
    # Causes
    if disease.causes:
        st.markdown("### 🔍 Nguyên nhân")
        for cause in disease.causes:
            st.markdown(f"- {cause}")
    
    # Symptoms
    if disease.symptoms:
        st.markdown("### 🩺 Triệu chứng")
        for symptom in disease.symptoms:
            st.markdown(f"- {symptom}")
    
    # Diagnosis
    if disease.diagnosis:
        st.markdown("### 🔬 Chẩn đoán")
        if disease.diagnosis.get("criteria"):
            st.markdown("**Tiêu chuẩn chẩn đoán:**")
            for criterion in disease.diagnosis["criteria"]:
                st.markdown(f"- {criterion}")
        if disease.diagnosis.get("tests"):
            st.markdown("**Xét nghiệm:**")
            for test in disease.diagnosis["tests"]:
                st.markdown(f"- {test}")
        if disease.diagnosis.get("imaging"):
            st.markdown("**Hình ảnh:**")
            for img in disease.diagnosis["imaging"]:
                st.markdown(f"- {img}")
    
    # Treatment
    if disease.treatment:
        st.markdown("### 💊 Điều trị")
        if disease.treatment.get("general"):
            st.markdown(f"**Tổng quan:** {disease.treatment['general']}")
        if disease.treatment.get("medications"):
            st.markdown("**Thuốc:**")
            for med in disease.treatment["medications"]:
                st.markdown(f"- {med}")
        if disease.treatment.get("procedures"):
            st.markdown("**Thủ thuật/Can thiệp:**")
            for proc in disease.treatment["procedures"]:
                st.markdown(f"- {proc}")
    
    # Prevention
    if disease.prevention:
        st.markdown("### 🛡️ Phòng ngừa")
        for prev in disease.prevention:
            st.markdown(f"- {prev}")
    
    # Complications
    if disease.complications:
        st.markdown("### ⚠️ Biến chứng")
        for comp in disease.complications:
            st.markdown(f"- {comp}")
    
    # Related resources
    st.markdown("---")
    st.markdown("### 🔗 Tài nguyên Liên quan")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if disease.related_scores:
            st.markdown("**📊 Thang điểm:**")
            for score in disease.related_scores:
                st.markdown(f"- {score}")
    
    with col2:
        if disease.related_drugs:
            st.markdown("**💊 Thuốc:**")
            for drug in disease.related_drugs:
                st.markdown(f"- {drug}")
    
    with col3:
        if disease.related_protocols:
            st.markdown("**📋 Phác đồ:**")
            for protocol in disease.related_protocols:
                st.markdown(f"- {protocol}")


# Display based on view mode
if view_mode == "Tìm kiếm":
    st.markdown("### 🔍 Tìm kiếm Bệnh lý")
    
    search_query = st.text_input(
        "Nhập tên bệnh (tiếng Việt hoặc tiếng Anh):",
        placeholder="Ví dụ: Viêm phổi, Pneumonia, Suy tim...",
        key="disease_search_query"
    )
    
    if search_query:
        results = search_diseases(search_query)
        
        if results:
            st.success(f"✅ Tìm thấy {len(results)} bệnh lý")
            
            for disease in results:
                with st.expander(f"**{disease.name_vn}** ({disease.name})", expanded=False):
                    render_disease_detail(disease)
        else:
            st.warning("Không tìm thấy bệnh lý. Vui lòng thử lại với từ khóa khác.")

elif view_mode == "Theo chuyên khoa":
    st.markdown("### 📚 Bệnh lý theo Chuyên khoa")
    
    category = None if category_filter == "Tất cả" else category_filter
    
    diseases = get_diseases_by_category(category) if category else get_all_diseases()
    
    if diseases:
        st.success(f"✅ Tìm thấy {len(diseases)} bệnh lý")
        
        for disease in diseases:
            with st.expander(f"**{disease.name_vn}** ({disease.name})", expanded=False):
                render_disease_detail(disease)
    else:
        st.warning("Không tìm thấy bệnh lý trong chuyên khoa này.")

else:  # Theo triệu chứng
    st.markdown("### 🩺 Tìm kiếm theo Triệu chứng")
    
    symptom_query = st.text_input(
        "Nhập triệu chứng:",
        placeholder="Ví dụ: Sốt, Ho, Khó thở, Đau ngực...",
        key="disease_symptom_query"
    )
    
    if symptom_query:
        results = get_diseases_by_symptom(symptom_query)
        
        if results:
            st.success(f"✅ Tìm thấy {len(results)} bệnh lý có triệu chứng này")
            
            for disease in results:
                with st.expander(f"**{disease.name_vn}** ({disease.name})", expanded=False):
                    render_disease_detail(disease)
        else:
            st.warning("Không tìm thấy bệnh lý với triệu chứng này.")


# Additional information
st.markdown("---")
st.markdown("### 📚 Thông tin về Database")
st.markdown("""
**Database hiện tại bao gồm:**

- **Infectious Diseases:** Pneumonia, Sepsis
- **Cardiology:** Heart Failure, Myocardial Infarction
- **Respiratory:** COPD
- **Endocrinology:** Type 2 Diabetes
- **Nephrology:** AKI
- **Neurology:** Stroke

**Tính năng:**
- Tìm kiếm theo tên bệnh
- Lọc theo chuyên khoa
- Tìm kiếm theo triệu chứng
- Thông tin chi tiết: định nghĩa, nguyên nhân, triệu chứng, chẩn đoán, điều trị
- Liên kết với protocols, scores, drugs, ICD-10 codes

**Lưu ý:** Database sẽ được mở rộng thêm các bệnh lý khác trong tương lai.
""")

# Footer
render_standard_footer(disclaimer=True)

