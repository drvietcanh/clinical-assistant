"""
Disease Encyclopedia Module
Comprehensive information about diseases and conditions
"""

import streamlit as st
from utils.page_helper import setup_page, render_standard_footer
from components.ui import render_info_box, render_hero, render_info_card, get_paginated_items
from components.page_sidebar import render_standard_sidebar
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
# Use standard sidebar component
filters = render_standard_sidebar(
    title="Bách khoa Bệnh lý",
    icon="📖",
    description="Thông tin chi tiết về các bệnh lý",
    module_group="📖 Thông tin Y học",
    filters={
        "view_mode": {
            "type": "radio",
            "label": "Chế độ xem:",
            "options": ["Tìm kiếm", "Theo chuyên khoa", "Theo triệu chứng"],
            "default": "Tìm kiếm",
            "key": "disease_view_mode"
        },
        "category": {
            "type": "selectbox",
            "label": "Chọn chuyên khoa:",
            "options": ["Tất cả"] + get_category_list(),
            "default": "Tất cả",
            "key": "disease_category_filter",
            "conditional": "view_mode == 'Theo chuyên khoa'"
        }
    },
    info_text="""
    **📖 Disease Encyclopedia:**
    - Thông tin chi tiết về **bệnh lý phổ biến**
    - **Định nghĩa, nguyên nhân, triệu chứng**
    - **Chẩn đoán và điều trị**
    - **Liên kết** với protocols, scores, drugs
    
    **💡 Lưu ý:**
    - Database hiện tại bao gồm các bệnh phổ biến nhất
    - Thông tin chỉ mang tính tham khảo
    - Luôn tham khảo guidelines mới nhất
    """
)

view_mode = filters.get("view_mode", "Tìm kiếm")
category_filter = filters.get("category", "Tất cả") if view_mode == "Theo chuyên khoa" else None

# ========== MAIN CONTENT ==========

# Use standard hero section
render_hero(
    title="Bách khoa Bệnh lý",
    subtitle="Disease Encyclopedia",
    description="Thông tin toàn diện về các bệnh lý phổ biến: định nghĩa, nguyên nhân, triệu chứng, chẩn đoán, điều trị, và phòng ngừa",
    icon="📖",
    gradient=("#667eea", "#764ba2")
)


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
            # Use pagination
            paginated_results = get_paginated_items(results, items_per_page=10, page_key="disease_search_page")
            
            render_info_box(
                f"Tìm thấy {len(results)} bệnh lý",
                type="success",
                title="Kết quả tìm kiếm"
            )
            
            for disease in paginated_results:
                with st.expander(f"**{disease.name_vn}** ({disease.name})", expanded=False):
                    render_disease_detail(disease)
        else:
            render_info_box(
                "Không tìm thấy bệnh lý. Vui lòng thử lại với từ khóa khác.",
                type="warning",
                title="Không có kết quả"
            )

elif view_mode == "Theo chuyên khoa":
    st.markdown("### 📚 Bệnh lý theo Chuyên khoa")
    
    category = None if category_filter == "Tất cả" else category_filter
    
    diseases = get_diseases_by_category(category) if category else get_all_diseases()
    
    if diseases:
        # Use pagination
        paginated_diseases = get_paginated_items(diseases, items_per_page=10, page_key="disease_category_page")
        
        render_info_box(
            f"Tìm thấy {len(diseases)} bệnh lý",
            type="success",
            title="Kết quả"
        )
        
        for disease in paginated_diseases:
            with st.expander(f"**{disease.name_vn}** ({disease.name})", expanded=False):
                render_disease_detail(disease)
    else:
        render_info_box(
            "Không tìm thấy bệnh lý trong chuyên khoa này.",
            type="warning"
        )

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
            # Use pagination
            paginated_results = get_paginated_items(results, items_per_page=10, page_key="disease_symptom_page")
            
            render_info_box(
                f"Tìm thấy {len(results)} bệnh lý có triệu chứng này",
                type="success",
                title="Kết quả"
            )
            
            for disease in paginated_results:
                with st.expander(f"**{disease.name_vn}** ({disease.name})", expanded=False):
                    render_disease_detail(disease)
        else:
            render_info_box(
                "Không tìm thấy bệnh lý với triệu chứng này.",
                type="warning"
            )


# Additional information
st.markdown("---")
st.markdown("### 📚 Thông tin về Database")
st.markdown("""
**Database hiện tại bao gồm:**

- **Infectious Diseases (Nhiễm khuẩn):** 
  - Pneumonia (Viêm phổi)
  - Sepsis (Nhiễm khuẩn huyết)
  - Tuberculosis (Lao phổi)
  - Dengue Fever (Sốt xuất huyết Dengue)
- **Cardiology (Tim mạch):** 
  - Heart Failure (Suy tim)
  - Myocardial Infarction (Nhồi máu cơ tim)
  - Hypertension (Tăng huyết áp)
  - Atrial Fibrillation (Rung nhĩ)
  - Coronary Artery Disease (Bệnh mạch vành)
  - Valvular Heart Disease (Bệnh van tim)
  - Myocarditis (Viêm cơ tim)
  - Pericarditis (Viêm màng ngoài tim)
  - Dilated Cardiomyopathy (Bệnh cơ tim giãn)
- **Respiratory (Hô hấp):** 
  - COPD (Bệnh phổi tắc nghẽn mạn tính)
  - Asthma (Hen phế quản)
- **Gastroenterology (Tiêu hóa):**
  - Peptic Ulcer Disease (Loét dạ dày tá tràng)
  - GERD (Trào ngược dạ dày thực quản)
  - Hepatitis B (Viêm gan B)
  - Cirrhosis (Xơ gan)
- **Endocrinology (Nội tiết):** 
  - Type 2 Diabetes (Đái tháo đường type 2)
  - Hyperthyroidism (Cường giáp)
  - Hypothyroidism (Suy giáp)
- **Nephrology (Thận):** 
  - AKI (Tổn thương thận cấp)
  - Chronic Kidney Disease (Suy thận mạn)
- **Neurology (Thần kinh):** 
  - Stroke (Đột quỵ)
  - Epilepsy (Động kinh)
- **Rheumatology (Khớp):**
  - Gout (Bệnh gút)
- **Hematology (Huyết học):**
  - Iron Deficiency Anemia (Thiếu máu thiếu sắt)
  - Thrombocytopenia (Giảm tiểu cầu)
- **Dermatology (Da liễu):**
  - Atopic Dermatitis (Viêm da cơ địa)
  - Psoriasis (Vẩy nến)
- **Psychiatry (Tâm thần):**
  - Major Depression (Trầm cảm)
  - Anxiety Disorder (Rối loạn lo âu)
- **Emergency (Cấp cứu):**
  - Anaphylaxis (Phản vệ)
  - Acute Poisoning (Ngộ độc cấp)

**Tính năng:**
- Tìm kiếm theo tên bệnh (tiếng Việt hoặc tiếng Anh)
- Lọc theo chuyên khoa
- Tìm kiếm theo triệu chứng
- Thông tin chi tiết: định nghĩa, nguyên nhân, triệu chứng, chẩn đoán, điều trị
- Liên kết với protocols, scores, drugs, ICD-10 codes

**Lưu ý:** Database sẽ được mở rộng thêm các bệnh lý khác trong tương lai.
""")

# Footer
render_standard_footer(disclaimer=True)

