"""
Diagnosis Module - Differential Diagnosis Generator
Main Router - Imports from diagnosis module
Integrated with Disease Encyclopedia, ICD-10 Lookup, In-Depth Articles, and Patient Education
"""

import streamlit as st
from utils.page_helper import setup_page, render_standard_footer
from components.ui import render_info_box, render_hero, get_paginated_items
from config.theme import COLORS

from diagnosis import render_ddx_interface

# Import Disease Encyclopedia functions
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

# Import ICD-10 Lookup functions
from icd10.search import (
    search_by_name,
    search_by_code,
    search_by_category,
    get_code_info,
    get_all_categories as get_icd10_categories
)

# Import In-Depth Articles functions
from pathlib import Path
import html
import re
from collections import Counter, defaultdict
import streamlit.components.v1 as components
from config.article_protocol_mapping import (
    get_protocol_for_article,
    has_protocol as check_has_protocol,
    get_protocol_deep_link
)

# Import article helper functions (reuse from articles page)
BASE_DIR = Path(__file__).resolve().parent.parent
CONTENT_ARTICLES_DIR = BASE_DIR / "content" / "articles"

def _sanitize_key_articles(text):
    """Sanitize text for Streamlit keys"""
    if not text:
        return "key"
    safe = str(text).encode('ascii', 'ignore').decode('ascii')
    safe = re.sub(r'[^a-zA-Z0-9]', '_', safe)
    safe = re.sub(r'_+', '_', safe).strip('_')
    if safe and safe[0].isdigit():
        safe = f"key_{safe}"
    return safe[:80] if len(safe) > 80 else safe

def _extract_first_h1(content: str, fallback: str = "") -> str:
    """Extract first H1 from markdown"""
    match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    return match.group(1).strip() if match else fallback

def _extract_meta_value(content: str, key: str) -> str:
    """Extract metadata value"""
    pattern = rf'{key}:\s*(.+)'
    match = re.search(pattern, content, re.IGNORECASE | re.MULTILINE)
    return match.group(1).strip() if match else ""

def _extract_guidelines(content: str) -> list:
    """Extract guidelines from content"""
    guidelines = []
    if "Guideline:" in content or "Guidelines:" in content:
        # Simple extraction
        lines = content.split('\n')
        for line in lines:
            if 'guideline' in line.lower() or 'hướng dẫn' in line.lower():
                # Extract guideline names
                matches = re.findall(r'([A-Z]{2,}[/\s]?[A-Z]{2,}[\s]?\d{4})', line)
                guidelines.extend(matches)
    return list(set(guidelines))[:5]  # Limit to 5

def _extract_summary_items(content: str) -> list:
    """Extract summary items"""
    summary = []
    # Look for bullet points or numbered lists
    lines = content.split('\n')
    in_summary = False
    for line in lines:
        if 'summary' in line.lower() or 'tóm tắt' in line.lower():
            in_summary = True
            continue
        if in_summary and (line.strip().startswith('-') or line.strip().startswith('*') or re.match(r'^\d+\.', line.strip())):
            summary.append(line.strip().lstrip('-*').strip())
            if len(summary) >= 5:
                break
        elif in_summary and line.strip() and not line.strip().startswith('#'):
            break
    return summary

@st.cache_data(show_spinner=False)
def get_articles_from_content_tab() -> list[dict]:
    """Auto-discover articles from content/articles/"""
    if not CONTENT_ARTICLES_DIR.exists():
        return []
    
    articles = []
    for path in sorted(CONTENT_ARTICLES_DIR.glob("*.md")):
        try:
            content = path.read_text(encoding="utf-8")
        except Exception:
            continue
        
        title = _extract_first_h1(content, fallback=path.stem)
        last_reviewed = _extract_meta_value(content, "Cập nhật") or ""
        specialty = _extract_meta_value(content, "Chuyên khoa") or "Nội khoa"
        guidelines = _extract_guidelines(content)
        summary = _extract_summary_items(content)
        
        # Check for protocol mapping
        article_id = path.stem
        protocol_info = get_protocol_for_article(article_id)
        has_protocol_mapping = protocol_info is not None
        
        articles.append({
            "id": article_id,
            "title": title,
            "specialty": specialty,
            "keywords": [],
            "path": path,
            "last_reviewed": last_reviewed,
            "guidelines": guidelines,
            "summary": summary,
            "key_points": [],
            "red_flags": [],
            "monitoring": [],
            "special_populations": [],
            "interactions": [],
            "follow_up": "",
            "related_calculators": [],
            "related_protocols": [],
            "has_protocol": has_protocol_mapping,
            "protocol_links": [],
            "protocol_info": protocol_info,
        })
    
    return articles

def load_article_content_tab(path: Path) -> str:
    """Load article content"""
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return ""

# Import Patient Education functions
from patient_education.data import (
    get_all_topics,
    get_topics_by_category,
    get_category_list as get_pe_category_list
)
from patient_education.display import render_patient_education_content
from components.patient_education import (
    render_topic_grid,
    render_enhanced_search,
    render_category_filters,
    render_enhanced_content,
    render_related_topics,
    render_hero_section,
    filter_topics_by_search
)

# Standard page setup
setup_page(
    page_title="Chẩn đoán phân biệt",
    page_icon="🩺",
    description="Công cụ hỗ trợ tạo danh sách chẩn đoán phân biệt"
)

# ========== SIDEBAR ==========
with st.sidebar:
    st.header("🩺 Chẩn đoán & Bài viết")
    st.caption("Module **Chẩn đoán phân biệt** – sub-module nhóm *🩺 Chẩn đoán & Bài viết*.")
    
    with st.expander("Liên kết trong nhóm Chẩn đoán & Bài viết", expanded=False):
        st.info("💡 **Lưu ý:** Các module Disease Encyclopedia, ICD-10 Lookup, In-Depth Articles và Patient Education đã được tích hợp vào tabs ở nội dung chính. Bạn có thể truy cập trực tiếp từ các tabs.")
        
        st.markdown("**Các tabs có sẵn:**")
        st.markdown("- 🩺 Differential Diagnosis")
        st.markdown("- 📖 Disease Encyclopedia")
        st.markdown("- 🏷️ ICD-10 Lookup")
        st.markdown("- 📚 In-Depth Articles")
        st.markdown("- 👥 Patient Education")
        
        st.markdown("---")
        if st.button("📊 Thang điểm & Scores", use_container_width=True):
            st.switch_page("pages/01_📊_Scores.py")
    
    st.markdown("---")
    render_info_box(
        """
        **Chức năng chính:**
        - Gợi ý danh sách chẩn đoán phân biệt theo triệu chứng và hệ cơ quan
        - Liên kết trực tiếp với calculators và phác đồ điều trị liên quan
        
        **Lưu ý:** Công cụ chỉ hỗ trợ, **không thay thế đánh giá lâm sàng**.
        """,
        type="info",
        title="Thông tin Module"
    )

# ========== MAIN CONTENT ==========

# Main tabs for organizing sub-modules
main_tabs = st.tabs([
    "🩺 Differential Diagnosis",
    "📖 Disease Encyclopedia",
    "🏷️ ICD-10 Lookup",
    "📚 In-Depth Articles",
    "👥 Patient Education"
])

# Tab 1: Differential Diagnosis
with main_tabs[0]:
    render_ddx_interface()

# Tab 2: Disease Encyclopedia
with main_tabs[1]:
    # Helper function to render disease detail
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
                        st.markdown(f"- [{score}](/Scores)")
            
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
    
    # Initialize state for Disease Encyclopedia tab
    if "enc_view" not in st.session_state:
        st.session_state.enc_view = "home"
    if "enc_category" not in st.session_state:
        st.session_state.enc_category = None
    
    # Hero Section
    render_hero(
        title="Bách khoa Bệnh lý",
        subtitle="Disease Encyclopedia",
        description="Tra cứu nhanh thông tin bệnh học, tiêu chuẩn chẩn đoán và phác đồ điều trị.",
        icon="📖",
        gradient=("#4facfe", "#00f2fe")
    )
    
    st.write("")
    
    # Search Bar
    col_search, col_space = st.columns([3, 1])
    with col_search:
        search_query = st.text_input(
            "🔍 Tìm kiếm bệnh lý, triệu chứng:",
            placeholder="Nhập tên bệnh (VD: Sốt xuất huyết, Suy tim) hoặc triệu chứng...",
            key="enc_search_box",
            label_visibility="collapsed"
        )
    
    # Logic Controller
    if search_query:
        st.session_state.enc_view = "search"
    elif st.session_state.enc_view == "search" and not search_query:
        st.session_state.enc_view = "home"
    
    # Render based on state
    if st.session_state.enc_view == "search":
        st.subheader(f"Kết quả tìm kiếm: '{search_query}'")
        
        results = search_diseases(search_query)
        symptom_results = get_diseases_by_symptom(search_query)
        
        combined_results = list({d.id: d for d in (results + symptom_results)}.values())
        
        if combined_results:
            for disease in combined_results:
                with st.expander(f"**{disease.name_vn}** ({disease.name}) - {disease.category}", expanded=False):
                    render_disease_detail_tabs(disease)
        else:
            st.warning("Không tìm thấy kết quả phù hợp. Vui lòng thử từ khóa khác.")
    
    elif st.session_state.enc_view == "category":
        cat = st.session_state.enc_category
        st.subheader(f"📂 Chuyên khoa: {cat}")
        
        diseases = get_diseases_by_category(cat)
        if diseases:
            for disease in diseases:
                with st.expander(f"**{disease.name_vn}** ({disease.name})", expanded=False):
                    render_disease_detail_tabs(disease)
        else:
            st.info("Chưa có dữ liệu cho chuyên khoa này.")
    
    elif st.session_state.enc_view == "detail":
        disease = st.session_state.enc_selected_disease
        if disease:
            render_disease_detail_tabs(disease)
        else:
            st.error("Không tìm thấy thông tin bệnh lý.")
    
    else:
        # Home Dashboard
        st.markdown("### 🔥 Bệnh lý Phổ biến")
        
        common_ids = ["dengue_fever", "hypertension", "type_2_diabetes", "pneumonia", "stroke", "gerd"]
        all_d = get_all_diseases()
        featured_diseases = [d for d in all_d if d.id in common_ids]
        
        feat_cols = st.columns(3)
        for i, disease in enumerate(featured_diseases):
            with feat_cols[i % 3]:
                with st.container(border=True):
                    st.markdown(f"**{disease.name_vn}**")
                    st.caption(f"{disease.name}")
                    if st.button("Xem chi tiết", key=f"feat_btn_{disease.id}"):
                        st.session_state.enc_view = "detail"
                        st.session_state.enc_selected_disease = disease
                        st.rerun()
        
        st.markdown("---")
        st.markdown("### 📂 Duyệt theo Chuyên khoa")
        
        categories = get_category_list()
        category_metadata = {
            "Cardiology": {"icon": "❤️", "name_vn": "Tim mạch"},
            "Respiratory": {"icon": "🫁", "name_vn": "Hô hấp"},
            "Gastroenterology": {"icon": "🤰", "name_vn": "Tiêu hóa"},
            "Neurology": {"icon": "🧠", "name_vn": "Thần kinh"},
            "Endocrinology": {"icon": "🩸", "name_vn": "Nội tiết"},
            "Infectious": {"icon": "🦠", "name_vn": "Truyền nhiễm"},
            "Dermatology": {"icon": "🧴", "name_vn": "Da liễu"},
            "Pediatrics": {"icon": "👶", "name_vn": "Nhi khoa"},
            "Emergency": {"icon": "🚑", "name_vn": "Cấp cứu"},
            "Oncology": {"icon": "🎗️", "name_vn": "Ung bướu"},
        }
        
        cols = st.columns(4)
        for i, cat in enumerate(categories):
            with cols[i % 4]:
                meta = category_metadata.get(cat, {"icon": "📁", "name_vn": cat})
                display_name = meta["name_vn"]
                icon = meta["icon"]
                
                if st.button(f"{icon} {display_name}", use_container_width=True, key=f"enc_cat_{i}"):
                    st.session_state.enc_category = cat
                    st.session_state.enc_view = "category"
                    st.rerun()
        
        st.markdown("---")
        total_diseases = len(get_all_diseases())
        st.caption(f"📚 Cơ sở dữ liệu hiện có: **{total_diseases}** bệnh lý & hội chứng.")

# Tab 3: ICD-10 Lookup
with main_tabs[2]:
    # Hero Section
    render_hero(
        title="Tra cứu mã ICD-10",
        subtitle="ICD-10 Code Lookup",
        description="International Classification of Diseases, 10th Revision. Tra cứu mã ICD-10 để hỗ trợ coding và billing trong y tế.",
        icon="🏷️",
        gradient=("#667eea", "#764ba2")
    )
    
    # Search type selector
    search_type = st.radio(
        "Tìm kiếm theo:",
        ["Tên bệnh", "Mã ICD-10", "Chuyên khoa"],
        key="icd10_search_type_tab",
        horizontal=True
    )
    
    st.markdown("---")
    
    # Search interface based on type
    if search_type == "Tên bệnh":
        st.markdown("### 🔍 Tìm kiếm theo tên bệnh")
        
        col1, col2 = st.columns([3, 1])
        with col1:
            query = st.text_input(
                "Nhập tên bệnh (tiếng Việt hoặc tiếng Anh):",
                placeholder="Ví dụ: Đái tháo đường, Diabetes, Pneumonia...",
                key="icd10_name_search_tab"
            )
        with col2:
            category_filter = st.selectbox(
                "Lọc theo chuyên khoa:",
                ["Tất cả"] + get_icd10_categories(),
                key="icd10_category_filter_tab"
            )
        
        if query:
            category = None if category_filter == "Tất cả" else category_filter
            results = search_by_name(query, category)
            
            if results:
                paginated_results = get_paginated_items(results, items_per_page=10, page_key="icd10_name_page_tab")
                
                render_info_box(
                    f"Tìm thấy {len(results)} kết quả",
                    type="success",
                    title="Kết quả tìm kiếm"
                )
                
                for code in paginated_results:
                    with st.expander(f"**{code.code}** - {code.name_vn}", expanded=False):
                        col1, col2 = st.columns(2)
                        with col1:
                            st.markdown(f"**Mã ICD-10:** `{code.code}`")
                            st.markdown(f"**Tên tiếng Việt:** {code.name_vn}")
                            st.markdown(f"**Tên tiếng Anh:** {code.name_en}")
                        with col2:
                            st.markdown(f"**Chuyên khoa:** {code.category}")
                            st.markdown(f"**Chương:** {code.chapter}")
                            if code.block:
                                st.markdown(f"**Block:** {code.block}")
                        if code.notes:
                            render_info_box(
                                code.notes,
                                type="info",
                                title="Ghi chú"
                            )
            else:
                render_info_box(
                    "Không tìm thấy kết quả. Vui lòng thử lại với từ khóa khác.",
                    type="warning"
                )
    
    elif search_type == "Mã ICD-10":
        st.markdown("### 🔍 Tìm kiếm theo mã ICD-10")
        
        code_query = st.text_input(
            "Nhập mã ICD-10:",
            placeholder="Ví dụ: I10, E11.9, A00.0...",
            key="icd10_code_search_tab"
        )
        
        if code_query:
            result = search_by_code(code_query)
            
            if result:
                render_info_box(
                    "Tìm thấy mã ICD-10",
                    type="success",
                    title="Kết quả"
                )
                
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown(f"**Mã ICD-10:** `{result.code}`")
                    st.markdown(f"**Tên tiếng Việt:** {result.name_vn}")
                    st.markdown(f"**Tên tiếng Anh:** {result.name_en}")
                with col2:
                    st.markdown(f"**Chuyên khoa:** {result.category}")
                    st.markdown(f"**Chương:** {result.chapter}")
                    if result.block:
                        st.markdown(f"**Block:** {result.block}")
                
                if result.notes:
                    render_info_box(
                        result.notes,
                        type="info",
                        title="Ghi chú"
                    )
            else:
                render_info_box(
                    f"Không tìm thấy mã ICD-10: {code_query}",
                    type="warning"
                )
    
    else:  # Chuyên khoa
        st.markdown("### 🔍 Tìm kiếm theo chuyên khoa")
        
        selected_category = st.selectbox(
            "Chọn chuyên khoa:",
            get_icd10_categories(),
            key="icd10_category_search_tab"
        )
        
        if selected_category:
            results = search_by_category(selected_category)
            
            if results:
                paginated_results = get_paginated_items(results, items_per_page=10, page_key="icd10_category_page_tab")
                
                render_info_box(
                    f"Tìm thấy {len(results)} mã ICD-10 trong chuyên khoa **{selected_category}**",
                    type="success",
                    title="Kết quả"
                )
                
                for code in paginated_results:
                    with st.expander(f"**{code.code}** - {code.name_vn}", expanded=False):
                        col1, col2 = st.columns(2)
                        with col1:
                            st.markdown(f"**Mã ICD-10:** `{code.code}`")
                            st.markdown(f"**Tên tiếng Việt:** {code.name_vn}")
                            st.markdown(f"**Tên tiếng Anh:** {code.name_en}")
                        with col2:
                            st.markdown(f"**Chuyên khoa:** {code.category}")
                            st.markdown(f"**Chương:** {code.chapter}")
                        if code.notes:
                            render_info_box(
                                code.notes,
                                type="info",
                                title="Ghi chú"
                            )
            else:
                render_info_box(
                    f"Không tìm thấy mã ICD-10 nào trong chuyên khoa {selected_category}",
                    type="warning"
                )
    
    st.markdown("---")
    st.markdown("### 📚 Thông tin về ICD-10")
    st.caption("""
    **ICD-10** (International Classification of Diseases, 10th Revision) là hệ thống phân loại bệnh tật quốc tế được WHO phát triển.
    Sử dụng cho mục đích tham khảo và coding. Cần xác nhận với guidelines chính thức khi sử dụng.
    """)

# Tab 4: In-Depth Articles
with main_tabs[3]:
    # Hero Section
    render_hero(
        title="Bài viết chuyên sâu",
        subtitle="In-Depth Articles",
        description="Tổng hợp chuyên sâu theo guideline mới nhất, gắn liền calculators/protocols trong ứng dụng.",
        icon="📚",
        gradient=("#667eea", "#764ba2")
    )
    
    # Get articles
    articles = get_articles_from_content_tab()
    
    if articles:
        # Search and filter
        col_search, col_filter = st.columns([3, 1])
        with col_search:
            search_query = st.text_input(
                "🔍 Tìm kiếm bài viết:",
                placeholder="Nhập từ khóa, chuyên khoa...",
                key="articles_search_tab"
            )
        with col_filter:
            specialties_list = list(set([a["specialty"] for a in articles]))
            selected_specialty = st.selectbox(
                "Chuyên khoa:",
                ["Tất cả"] + sorted(specialties_list),
                key="articles_specialty_filter_tab"
            )
        
        # Filter articles
        filtered_articles = articles
        if search_query:
            search_lower = search_query.lower()
            filtered_articles = [
                a for a in filtered_articles
                if search_lower in a["title"].lower() or
                   search_lower in a["specialty"].lower() or
                   any(search_lower in str(s).lower() for s in a.get("summary", []))
            ]
        
        if selected_specialty != "Tất cả":
            filtered_articles = [a for a in filtered_articles if a["specialty"] == selected_specialty]
        
        # Display articles
        if filtered_articles:
            st.info(f"📊 Tìm thấy **{len(filtered_articles)}** bài viết")
            
            for idx, article in enumerate(filtered_articles):
                with st.expander(f"**{article['title']}** - {article['specialty']}", expanded=False):
                    col1, col2 = st.columns([2, 1])
                    with col1:
                        st.markdown(f"**Chuyên khoa:** {article['specialty']}")
                        if article.get('last_reviewed'):
                            st.caption(f"🔄 Cập nhật: {article['last_reviewed']}")
                        if article.get('guidelines'):
                            st.caption(f"📑 Guidelines: {', '.join(article['guidelines'][:3])}")
                    with col2:
                        if article.get('has_protocol'):
                            st.success("📋 Có Protocol")
                    
                    # Summary
                    if article.get('summary'):
                        st.markdown("### 💡 Tóm tắt")
                        for item in article['summary'][:5]:
                            st.markdown(f"- {item}")
                    
                    # Load and display full content
                    st.markdown("---")
                    st.markdown("### 📖 Nội dung đầy đủ")
                    content = load_article_content_tab(article['path'])
                    if content:
                        st.markdown(content)
                    else:
                        st.warning("Không tìm thấy nội dung bài viết.")
                    
                    # Protocol link if available
                    if article.get('has_protocol') and article.get('protocol_info'):
                        st.markdown("---")
                        protocol_info = article['protocol_info']
                        if st.button(
                            "📋 Mở Protocol liên quan",
                            key=f"protocol_btn_tab_{_sanitize_key_articles(article['id'])}_{idx}",
                            use_container_width=True
                        ):
                            st.session_state['protocol_specialty'] = protocol_info.get("specialty_selector")
                            st.session_state['protocol_to_open'] = protocol_info.get("protocol_display")
                            st.session_state['protocol_function'] = protocol_info.get("protocol_function")
                            st.switch_page("pages/04_📋_Protocols.py")
        else:
            st.warning("Không tìm thấy bài viết phù hợp.")
    else:
        st.info("📚 Chưa có bài viết nào. Các bài viết sẽ được tự động phát hiện từ thư mục `content/articles/`.")

# Tab 5: Patient Education
with main_tabs[4]:
    # Hero Section
    render_hero_section(get_all_topics(), show_featured=True)
    
    # Search Section
    st.markdown("### 🔍 Tìm kiếm")
    all_topics = get_all_topics()
    search_query = render_enhanced_search(
        all_topics,
        placeholder="Tìm kiếm bệnh, thuốc, hướng dẫn...",
        show_filters=True,
        show_suggestions=True,
        key="patient_edu_search_tab"
    )
    
    # Category Filters
    st.markdown("---")
    selected_category = render_category_filters(
        all_topics,
        active_category=None,
        show_counts=True,
        key="patient_edu_category_buttons_tab"
    )
    
    # Get topics based on filters
    if selected_category is not None:
        topics = get_topics_by_category(selected_category)
    else:
        topics = get_all_topics()
    
    # Apply search filter
    if search_query and search_query.strip():
        topics = filter_topics_by_search(topics, search_query)
    
    # Display topics
    st.markdown("---")
    st.markdown("### 📚 Tài liệu")
    
    if topics:
        st.info(f"📊 Tìm thấy **{len(topics)}** tài liệu" + (f" cho '{search_query}'" if search_query else ""))
        
        # Card grid layout
        render_topic_grid(
            topics,
            columns=3,
            show_preview=True,
            search_query=search_query
        )
        
        # Detailed view
        st.markdown("---")
        st.markdown("### 📖 Xem chi tiết")
        
        for topic in topics:
            with st.expander(f"**{topic.title_vn}** ({topic.category})", expanded=False):
                render_enhanced_content(
                    topic,
                    show_toc=True,
                    show_progress=True,
                    search_query=search_query
                )
                render_related_topics(topic, all_topics)
                render_patient_education_content(topic)
                
                if topic.printable:
                    st.markdown("---")
                    render_info_box(
                        "Bạn có thể in tài liệu này để phát cho bệnh nhân. Nhấn Ctrl+P hoặc Cmd+P để in.",
                        type="info",
                        icon="🖨️"
                    )
    else:
        render_info_box(
            "Không tìm thấy tài liệu. Vui lòng thử lại với từ khóa khác hoặc chọn chủ đề khác.",
            type="warning"
        )

# ========== FOOTER ==========
render_standard_footer(disclaimer=True)

