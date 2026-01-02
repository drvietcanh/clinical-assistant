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
from config.theme import COLORS

# Standard page setup
setup_page(
    page_title="Bách khoa Bệnh lý",
    page_icon="📖",
    description="Thông tin toàn diện về các bệnh lý phổ biến"
)

# ========== HELPER FUNCTIONS ==========

def render_category_card(category_name, icon="📁"):
    """Render a clickable card for a category (using streamlit button for interactivity)"""
    # Using a simple button for now as effectively clickable cards in Streamlit can be tricky without custom components
    # But we can style it or just use button
    return st.button(f"{icon} {category_name}", use_container_width=True, key=f"cat_btn_{category_name}")

def render_disease_detail_tabs(disease):
    """Render detailed disease information using Tabs"""
    
    st.markdown(f"## {disease.name_vn} <span style='font-size: 0.6em; color: gray;'>({disease.name})</span>", unsafe_allow_html=True)
    
    # Quick Info Badges
    st.markdown(f"""
    <div style='margin-bottom: 20px;'>
        <span style='background-color: {COLORS['primary']}20; color: {COLORS['primary']}; padding: 4px 8px; border-radius: 4px; font-weight: bold;'>{disease.category}</span>
        {f"<span style='background-color: #eee; color: #555; padding: 4px 8px; border-radius: 4px; margin-left: 8px;'>ICD-10: {', '.join(disease.icd10_codes)}</span>" if disease.icd10_codes else ""}
    </div>
    """, unsafe_allow_html=True)

    # Tabs
    tab_overview, tab_diagnosis, tab_treatment, tab_resources = st.tabs([
        "📝 Tổng quan & Triệu chứng", 
        "🔬 Chẩn đoán", 
        "💊 Điều trị & Phòng ngừa", 
        "🔗 Tài liệu & Công cụ"
    ])

    with tab_overview:
        col1, col2 = st.columns([2, 1])
        with col1:
            if disease.definition:
                st.markdown("### 📌 Định nghĩa")
                st.info(disease.definition)
            
            if disease.symptoms:
                st.markdown("### 🩺 Triệu chứng lâm sàng")
                for symptom in disease.symptoms:
                    st.markdown(f"- {symptom}")
        
        with col2:
            if disease.causes:
                st.markdown("### 🔍 Nguyên nhân")
                with st.container(border=True):
                    for cause in disease.causes:
                        st.markdown(f"- {cause}")
            
            if disease.complications:
                st.markdown("### ⚠️ Biến chứng")
                with st.container(border=True):
                    for comp in disease.complications:
                        st.markdown(f"- {comp}")

    with tab_diagnosis:
        if disease.diagnosis:
            if disease.diagnosis.get("criteria"):
                st.markdown("### ✅ Tiêu chuẩn chẩn đoán")
                st.success("\n".join([f"- {c}" for c in disease.diagnosis["criteria"]]))
            
            col_d1, col_d2 = st.columns(2)
            with col_d1:
                if disease.diagnosis.get("tests"):
                    st.markdown("### 🧪 Xét nghiệm")
                    for test in disease.diagnosis["tests"]:
                        st.markdown(f"- {test}")
            with col_d2:
                if disease.diagnosis.get("imaging"):
                    st.markdown("### 📷 Chẩn đoán hình ảnh")
                    for img in disease.diagnosis["imaging"]:
                        st.markdown(f"- {img}")
        else:
            st.info("Đang cập nhật thông tin chẩn đoán...")

    with tab_treatment:
        if disease.treatment:
            if disease.treatment.get("general"):
                st.markdown("### 🏥 Nguyên tắc điều trị")
                st.write(disease.treatment['general'])
            
            col_t1, col_t2 = st.columns(2)
            with col_t1:
                if disease.treatment.get("medications"):
                    st.markdown("### 💊 Thuốc")
                    for med in disease.treatment["medications"]:
                        st.markdown(f"- {med}")
            with col_t2:
                if disease.treatment.get("procedures"):
                    st.markdown("### 💉 Thủ thuật / Can thiệp")
                    for proc in disease.treatment["procedures"]:
                        st.markdown(f"- {proc}")
        
        if disease.prevention:
            st.markdown("---")
            st.markdown("### 🛡️ Phòng ngừa")
            for prev in disease.prevention:
                st.markdown(f"- {prev}")

    with tab_resources:
        st.markdown("### 🔗 Công cụ hỗ trợ liên quan")
        
        if not (disease.related_scores or disease.related_drugs or disease.related_protocols):
            st.info("Chưa có liên kết tài nguyên cụ thể cho bệnh lý này.")
        
        col_r1, col_r2, col_r3 = st.columns(3)
        
        with col_r1:
            if disease.related_scores:
                st.markdown("#### 📊 Thang điểm (Scores)")
                for score in disease.related_scores:
                    st.markdown(f"- [{score}](/Scores)") # Placeholder link logic
        
        with col_r2:
            if disease.related_drugs:
                st.markdown("#### 💊 Dược thư (Drugs)")
                for drug in disease.related_drugs:
                    st.markdown(f"- [{drug}](/Drug_Database)")
        
        with col_r3:
            if disease.related_protocols:
                st.markdown("#### 📋 Phác đồ (Protocols)")
                for protocol in disease.related_protocols:
                    st.markdown(f"- [{protocol}](/Protocols)")

# ========== SIDEBAR ==========
filters = render_standard_sidebar(
    title="Bách khoa Bệnh lý",
    icon="📖",
    description="Tra cứu thông tin bệnh lý, chẩn đoán và điều trị.",
    module_group="📖 Thông tin Y học",
    filters={} # Minimal filters in sidebar, move main interaction to main area
)

# ========== MAIN CONTENT ==========

# 1. Hero Search Section
render_hero(
    title="Bách khoa Bệnh lý",
    subtitle="Disease Encyclopedia",
    description="Tra cứu nhanh thông tin bệnh học, tiêu chuẩn chẩn đoán và phác đồ điều trị.",
    icon="📖",
    gradient=("#4facfe", "#00f2fe") # Fresh blue gradient
)

st.write("") # Spacer

# Search Bar (Centralized)
col_search, col_space = st.columns([3, 1])
with col_search:
    search_query = st.text_input(
        "🔍 Tìm kiếm bệnh lý, triệu chứng:",
        placeholder="Nhập tên bệnh (VD: Sốt xuất huyết, Suy tim) hoặc triệu chứng...",
        key="main_search_box",
        label_visibility="collapsed"
    )

# 2. Logic Controller
# Determine what to show: Search Results, Selected Category, or Home Dashboard

# State management for navigation (simple version)
if "enc_view" not in st.session_state:
    st.session_state.enc_view = "home" # home, category, search
if "enc_category" not in st.session_state:
    st.session_state.enc_category = None

# If search query exists, it overrides everything
if search_query:
    st.session_state.enc_view = "search"
elif st.session_state.enc_view == "search" and not search_query:
    st.session_state.enc_view = "home"

# Render Layout based on State
if st.session_state.enc_view == "search":
    st.subheader(f"Kết quả tìm kiếm: '{search_query}'")
    
    # Search logic
    results = search_diseases(search_query)
    symptom_results = get_diseases_by_symptom(search_query)
    
    # Merge unique results
    combined_results = list({d.id: d for d in (results + symptom_results)}.values())
    
    if combined_results:
        for disease in combined_results:
            with st.expander(f"**{disease.name_vn}** ({disease.name}) - {disease.category}", expanded=False):
                render_disease_detail_tabs(disease)
    else:
        st.warning("Không tìm thấy kết quả phù hợp. Vui lòng thử từ khóa khác.")
        if st.button("🔙 Quay lại trang chủ"):
            st.session_state.enc_view = "home"
            st.rerun()

elif st.session_state.enc_view == "category":
    # Show Category View
    cat = st.session_state.enc_category
    col_back, col_title = st.columns([1, 5])
    with col_back:
        if st.button("⬅️ Quay lại"):
            st.session_state.enc_view = "home"
            st.session_state.enc_category = None
            st.rerun()
    with col_title:
        st.subheader(f"📂 Chuyên khoa: {cat}")
    
    diseases = get_diseases_by_category(cat)
    if diseases:
        for disease in diseases:
             with st.expander(f"**{disease.name_vn}** ({disease.name})", expanded=False):
                render_disease_detail_tabs(disease)
    else:
        st.info("Chưa có dữ liệu cho chuyên khoa này.")

else:
    # === HOME DASHBOARD ===
    
    # A. Featured / Common Conditions (Optional)
    # st.markdown("### 🔥 Bệnh lý phổ biến")
    # ...
    
    # B. Category Grid
    st.markdown("### 📂 Duyệt theo Chuyên khoa")
    
    categories = get_category_list()
    # Simple icon mapping
    cat_icons = {
        "Cardiology": "❤️", "Respiratory": "🫁", "Gastroenterology": "🥨",
        "Nurology": "🧠", "Endocrinology": "🩸", "Infectious Diseases": "🦠",
        "Dermatology": "🧴", "Pediatrics": "👶", "Emergency": "🚑"
    }
    
    # Creating a grid of buttons
    cols = st.columns(4)
    for i, cat in enumerate(categories):
        with cols[i % 4]:
            icon = cat_icons.get(cat, "📁")
            # Translation for display if needed, keeping English key for data
            display_name = cat 
            
            if st.button(f"{icon} {display_name}", use_container_width=True, key=f"cat_{i}"):
                st.session_state.enc_category = cat
                st.session_state.enc_view = "category"
                st.rerun()
    
    # C. A-Z Index Quick Links (Visual only for now, can implement filtering later)
    st.markdown("---")
    st.markdown("### 🔤 Tra cứu A-Z")
    
    az_cols = st.columns(13) # 26 letters / 2 rows roughly
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    selected_letter = None
    
    # Simple A-Z filter buttons
    # This renders a lot of buttons, might clutter but requested "A-Z Index"
    # To save space, maybe display just available letters? 
    # For now, let's keep it simple: List styling
    st.caption("Chọn chữ cái đầu của tên bệnh (Tiếng Anh/Việt)")
    
    # D. Statistics footer
    st.markdown("---")
    total_diseases = len(get_all_diseases())
    st.caption(f"📚 Cơ sở dữ liệu hiện có: **{total_diseases}** bệnh lý & hội chứng.")

# Footer
render_standard_footer(disclaimer=True)

