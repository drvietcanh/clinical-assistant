"""
Scores Module - Clinical Scoring Systems
Main Router - Organized by Specialty

Imports calculators from individual specialty modules
"""

import streamlit as st
from utils.page_helper import setup_page, render_standard_footer
from components.ui import render_info_box, render_hero

from scores.config import SCORES_BY_SPECIALTY
from scores import cardiology, emergency, respiratory, neurology, gi, metabolism, hematology, nephrology, trauma, psychiatry, oncology, surgery, pediatrics, infectious, ent, obstetrics, dermatology, rheumatology, ophthalmology, pain, nursing
from components.scores_favorites import (
    render_favorites_section_in_sidebar,
    render_favorite_button,
    is_favorite
)
from components.scores_dark_mode import init_theme, render_theme_toggle
from components.scores_autocomplete import render_search_with_autocomplete, add_to_recent_searches
from components.scores_related import render_related_calculators
from components.scores_mobile import init_mobile_optimizations

# ========== HELPER FUNCTIONS ==========

def is_daily_use(info: dict) -> bool:
    """Check if calculator is marked as daily use"""
    desc = info.get("desc", "") or ""
    return "DÙNG HÀNG NGÀY" in desc

def global_search(query: str) -> list:
    """
    Search across all specialties
    Returns list of (specialty, score_id, score_info) tuples
    """
    if not query:
        return []
    
    query_lower = query.lower().strip()
    results = []
    
    for specialty, scores in SCORES_BY_SPECIALTY.items():
        for score_id, score_info in scores.items():
            # Search in score_id, name, and description
            if (query_lower in score_id.lower() or 
                query_lower in score_info.get("name", "").lower() or 
                query_lower in (score_info.get("desc", "") or "").lower()):
                results.append((specialty, score_id, score_info))
    
    return results

def get_all_scores_flat():
    """Get all scores as flat list with specialty info"""
    all_scores = []
    for specialty, scores in SCORES_BY_SPECIALTY.items():
        for score_id, score_info in scores.items():
            all_scores.append({
                "specialty": specialty,
                "score_id": score_id,
                "score_info": score_info
            })
    return all_scores

# Standard page setup with mobile optimizations
setup_page(
    page_title="Calculators & Thang điểm",
    page_icon="📊",
    description="Thang điểm và calculators lâm sàng, phân loại theo chuyên khoa",
    mobile_header=True
)

# Initialize dark mode
init_theme()

# Initialize mobile optimizations
init_mobile_optimizations()

# Breadcrumbs
try:
    from components.mobile_page_wrapper import render_breadcrumbs
    render_breadcrumbs([
        ("Trang chủ", "/"),
        ("Thang điểm", None)
    ])
except ImportError:
    pass

# ========== SIDEBAR ==========
with st.sidebar:
    st.header("📊 Calculators & Scores")
    st.caption("Module **Calculators & Thang điểm** – thuộc nhóm *Calculators & Scores*.")
    
    # Quick navigation giữa các sub-module trong nhóm
    with st.expander("Liên kết trong nhóm Calculators & Scores", expanded=False):
        col_a, col_b = st.columns(2)
        with col_a:
            if st.button("🔬 Labs & Calculators", use_container_width=True):
                st.switch_page("pages/05_🔬_Labs_and_Calculators.py")
        with col_b:
            if st.button("📊 TDM - Nồng độ thuốc", use_container_width=True):
                st.switch_page("pages/08_📊_TDM.py")
    
    st.markdown("---")
    
    # ========== GLOBAL SEARCH WITH AUTOCOMPLETE ==========
    st.subheader("🔍 Tìm kiếm toàn cục")
    global_search_query = render_search_with_autocomplete(
        label="Tìm kiếm tất cả calculators:",
        placeholder="Nhập tên, viết tắt hoặc từ khóa...",
        key="global_search"
    )
    
    # Add to recent searches if query exists
    if global_search_query:
        add_to_recent_searches(global_search_query)
    
    # Global search results
    global_results = []
    if global_search_query:
        global_results = global_search(global_search_query)
        if global_results:
            render_info_box(
                f"Tìm thấy {len(global_results)} kết quả",
                type="success",
                title="Kết quả tìm kiếm"
            )
            # Show first few results
            with st.expander(f"Kết quả tìm kiếm ({len(global_results)})", expanded=True):
                for spec, sid, sinfo in global_results[:10]:  # Show first 10
                    st.markdown(f"**{sinfo['name']}**")
                    st.caption(f"{spec} • {sinfo.get('desc', '')[:60]}...")
        else:
            render_info_box(
                "Không tìm thấy kết quả. Vui lòng thử lại với từ khóa khác.",
                type="warning"
            )
    
    st.markdown("---")
    
    # ========== ADVANCED FILTERS ==========
    with st.expander("🔧 Bộ lọc nâng cao", expanded=False):
        filter_status = st.multiselect(
            "Trạng thái:",
            ["✅", "🚧", "📋"],
            default=[],
            help="Lọc theo trạng thái calculator"
        )
        filter_daily_use = st.checkbox(
            "Chỉ hiển thị calculators dùng hàng ngày ⭐",
            value=False,
            help="Chỉ hiển thị các calculator được đánh dấu 'DÙNG HÀNG NGÀY'"
        )
    
    st.markdown("---")
    
    # ========== SPECIALTY SELECTION ==========
    st.subheader("Chọn chuyên khoa")
    
    # If global search found results, suggest specialty
    suggested_specialty = None
    if global_results:
        # Get most common specialty from results
        specialty_counts = {}
        for spec, _, _ in global_results:
            specialty_counts[spec] = specialty_counts.get(spec, 0) + 1
        if specialty_counts:
            suggested_specialty = max(specialty_counts.items(), key=lambda x: x[1])[0]
    
    specialty_list = list(SCORES_BY_SPECIALTY.keys())
    default_index = 0
    if suggested_specialty and suggested_specialty in specialty_list:
        default_index = specialty_list.index(suggested_specialty)
    
    specialty = st.selectbox(
        "Chuyên khoa:",
        specialty_list,
        index=default_index,
        help="Chọn chuyên khoa để xem calculators"
    )
    
    st.markdown("---")
    
    # ========== SCORE SELECTION ==========
    st.subheader("Thang điểm có sẵn")
    
    # Display scores for selected specialty
    scores_in_specialty = SCORES_BY_SPECIALTY[specialty]

    # Inject CSS fix for text overlap
    from components.scores_css_fix import inject_text_overlap_fix
    inject_text_overlap_fix()
    
    # Local search trong chuyên khoa hiện tại
    local_search_query = st.text_input(
        "Tìm trong chuyên khoa:",
        "",
        placeholder="Tìm kiếm trong chuyên khoa này...",
        key="local_search"
    ).strip()

    # Apply filters
    def matches_local_query(score_id: str, info: dict) -> bool:
        if not local_search_query:
            return True
        q = local_search_query.lower()
        return q in score_id.lower() or q in info.get("name", "").lower() or q in (info.get("desc", "") or "").lower()
    
    def matches_filters(score_id: str, info: dict) -> bool:
        # Status filter
        if filter_status and info.get("status", "") not in filter_status:
            return False
        # Daily use filter
        if filter_daily_use and not is_daily_use(info):
            return False
        return True

    # Filter items
    filtered_items = [
        (k, v) for k, v in scores_in_specialty.items() 
        if matches_local_query(k, v) and matches_filters(k, v)
    ]

    # If global search active, also filter by global results
    if global_search_query and global_results:
        global_score_ids = {sid for _, sid, _ in global_results}
        filtered_items = [(k, v) for k, v in filtered_items if k in global_score_ids]

    # Nếu không có kết quả, hiển thị thông báo và dùng toàn bộ danh sách để tránh lỗi widget
    if not filtered_items and (local_search_query or filter_status or filter_daily_use):
        render_info_box(
            "Không tìm thấy thang điểm phù hợp với bộ lọc. Hiển thị tất cả thang điểm trong chuyên khoa.",
            type="warning"
        )
        filtered_items = list(scores_in_specialty.items())

    # Sort: daily use first, then alphabetically
    sorted_items = sorted(
        filtered_items,
        key=lambda item: (not is_daily_use(item[1]), item[1]["name"]),
    )

    score_options = []
    for score_id, score_info in sorted_items:
        label = f"{score_info['status']} {score_info['name']}"
        if is_daily_use(score_info):
            label += " ⭐"
        score_options.append(label)
    
    if not score_options:
        st.error("Không có calculator nào phù hợp")
        score_options = ["Chọn calculator"]
        selected_score_display = "Chọn calculator"
        selected_score_id = None
    else:
        selected_score_display = st.radio(
            "Calculator:",
            score_options,
            label_visibility="collapsed"
        )
        
        # Extract score_id from selection (dựa trên danh sách đã sắp xếp)
        selected_score_id = None
        for score_id, score_info in sorted_items:
            if score_info['name'] in selected_score_display:
                selected_score_id = score_id
                break
    
    st.markdown("---")
    
    # ========== THEME TOGGLE ==========
    render_theme_toggle()
    
    st.markdown("---")
    
    # ========== FAVORITES SECTION ==========
    render_favorites_section_in_sidebar(SCORES_BY_SPECIALTY)
    
    render_info_box(
        """
        **Chú thích trạng thái calculator:**
        - ✅ Hoàn thành, có thể dùng lâm sàng
        - 🚧 Đang cập nhật/hoàn thiện
        - 📋 Đang trong kế hoạch
        """,
        type="info",
        title="Trạng thái Calculator"
    )
    
    st.markdown("---")
    st.caption(f"**{len([s for specialty_scores in SCORES_BY_SPECIALTY.values() for s in specialty_scores])}** calculators")
    st.caption("**Dựa trên bằng chứng**")

# ========== MAIN CONTENT ==========

# Display specialty overview with enhanced UI
current_name = SCORES_BY_SPECIALTY[specialty][selected_score_id]['name'] if selected_score_id else "Chọn calculator bên trái"
current_desc = SCORES_BY_SPECIALTY[specialty][selected_score_id].get('desc', '') if selected_score_id else ""

# Enhanced header with favorite button
col_header1, col_header2 = st.columns([4, 1])
with col_header1:
    if selected_score_id:
        render_info_box(
            f"""
            <div>
                <p><strong>📊 Chuyên khoa:</strong> {specialty}</p>
                <p><strong>🔢 Số lượng calculators:</strong> {len(scores_in_specialty)}</p>
                <p><strong>🔬 Đang xem:</strong> {current_name}</p>
                <p><strong>💡 Dùng khi:</strong> {current_desc if current_desc else 'Chọn calculator để xem mô tả chi tiết.'}</p>
            </div>
            """,
            type="info",
            title="Thông tin Calculator"
        )
    else:
        render_info_box(
            f"""
            <div>
                <p><strong>📊 Chuyên khoa:</strong> {specialty}</p>
                <p><strong>🔢 Số lượng calculators:</strong> {len(scores_in_specialty)}</p>
                <p><strong>💡 Hướng dẫn:</strong> Chọn một calculator từ danh sách ở sidebar bên trái để bắt đầu.</p>
            </div>
            """,
            type="info",
            title="Chọn Calculator"
        )

with col_header2:
    if selected_score_id:
        render_favorite_button(specialty, selected_score_id, current_name, key_suffix="header")

# ========== ROUTE TO APPROPRIATE MODULE ==========

# Helper function to render calculator and related
def render_calculator_with_related(specialty_name: str, score_id: str, render_func):
    """Render calculator and show related calculators"""
    if score_id:
        render_func(score_id)
        # Show related calculators
        render_related_calculators(specialty_name, score_id)

# Emergency & Critical Care
if "Cấp cứu" in specialty:
    if selected_score_id:
        emergency.render_emergency_calculator(selected_score_id)
        render_related_calculators(specialty, selected_score_id)

# Cardiology
elif "Tim mạch" in specialty:
    cardiology.render_cardiology_calculator(selected_score_id)

# Respiratory
elif "Hô hấp" in specialty:
    respiratory.render_respiratory_calculator(selected_score_id)

# Neurology
elif "Thần kinh" in specialty:
    neurology.render_neurology_calculator(selected_score_id)

# GI/Hepatology
elif "Tiêu Hóa" in specialty or "Gan" in specialty:
    gi.render_gi_calculator(selected_score_id)

# Metabolism/Endocrinology
elif "Nội tiết" in specialty or "Chuyển hóa" in specialty:
    metabolism.render_metabolism_calculator(selected_score_id)

# Hematology
elif "Huyết học" in specialty or "Đông máu" in specialty:
    hematology.render_hematology_calculator(selected_score_id)

# Nephrology
elif "Thận" in specialty or "Điện giải" in specialty:
    nephrology.render_nephrology_calculator(selected_score_id)

# Trauma
elif "Chấn Thương" in specialty or "Chỉnh Hình" in specialty:
    trauma.render_trauma_calculator(selected_score_id)

# Psychiatry
elif "Tâm Thần" in specialty or "Tâm Lý" in specialty:
    psychiatry.render_psychiatry_calculator(selected_score_id)

# Oncology
elif "Ung thư" in specialty:
    oncology.render_oncology_calculator(selected_score_id)

# Surgery
elif "Phẫu Thuật" in specialty or "Gây Mê" in specialty:
    surgery.render_surgery_calculator(selected_score_id)

# Pediatrics
elif "Nhi Khoa" in specialty:
    pediatrics.render_pediatrics_calculator(selected_score_id)

# Infectious Disease
elif "Nhiễm khuẩn" in specialty:
    infectious.render_infectious_calculator(selected_score_id)

# ENT
elif "Tai Mũi Họng" in specialty or "ENT" in specialty:
    ent.render_ent_calculator(selected_score_id)

# Obstetrics
elif "Sản khoa" in specialty or "Obstetrics" in specialty:
    obstetrics.render_obstetrics_calculator(selected_score_id)

# Dermatology
elif "Da Liễu" in specialty or "Dermatology" in specialty:
    dermatology.render_dermatology_calculator(selected_score_id)

# Rheumatology
elif "Thấp Khớp" in specialty or "Miễn Dịch" in specialty:
    rheumatology.render_rheumatology_calculator(selected_score_id)

# Ophthalmology
elif "Mắt" in specialty or "Ophthalmology" in specialty:
    ophthalmology.render_ophthalmology_calculator(selected_score_id)

# Pain Assessment
elif "Đánh giá đau" in specialty or "Pain" in specialty:
    pain.render_pain_calculator(selected_score_id)

# Nursing Care
elif "Chăm sóc điều dưỡng" in specialty or "Nursing" in specialty:
    if selected_score_id:
        nursing.render_nursing_calculator(selected_score_id)
        render_related_calculators(specialty, selected_score_id)

# Show related calculators for all rendered calculators
if selected_score_id and specialty in SCORES_BY_SPECIALTY:
    # Check if calculator was rendered (not in "Other specialties" case)
    if (("Cấp cứu" in specialty) or ("Tim mạch" in specialty) or 
        ("Hô hấp" in specialty) or ("Thần kinh" in specialty) or
        ("Tiêu Hóa" in specialty or "Gan" in specialty) or
        ("Nội tiết" in specialty or "Chuyển hóa" in specialty) or
        ("Huyết học" in specialty or "Đông máu" in specialty) or
        ("Thận" in specialty or "Điện giải" in specialty) or
        ("Chấn Thương" in specialty or "Chỉnh Hình" in specialty) or
        ("Tâm Thần" in specialty or "Tâm Lý" in specialty) or
        ("Ung thư" in specialty) or
        ("Phẫu Thuật" in specialty or "Gây Mê" in specialty) or
        ("Nhi Khoa" in specialty) or
        ("Nhiễm khuẩn" in specialty) or
        ("Tai Mũi Họng" in specialty or "ENT" in specialty) or
        ("Sản khoa" in specialty or "Obstetrics" in specialty) or
        ("Da Liễu" in specialty or "Dermatology" in specialty) or
        ("Thấp Khớp" in specialty or "Miễn Dịch" in specialty) or
        ("Mắt" in specialty or "Ophthalmology" in specialty) or
        ("Đánh giá đau" in specialty or "Pain" in specialty) or
        ("Chăm sóc điều dưỡng" in specialty or "Nursing" in specialty)):
        # Related calculators already shown in individual sections above
        pass

# Other specialties - show placeholder for now
else:
    score_info = scores_in_specialty[selected_score_id]
    st.subheader(f"📋 {score_info['name']}")
    st.caption(score_info['desc'])
    
    if score_info['status'] == "✅":
        st.success("✅ Đã hoàn thành - Đang trong module riêng")
    elif score_info['status'] == "🚧":
        st.warning("🚧 Đang phát triển - Sắp ra mắt")
    else:
        st.info("📋 Trong kế hoạch phát triển")
    
    st.markdown("---")
    st.markdown(f"""
    **Mô tả:** {score_info['desc']}
    
    Calculator này sẽ sớm được triển khai trong module chuyên khoa tương ứng.
    """)
    
    # Show related calculators
    if selected_score_id:
        render_related_calculators(specialty, selected_score_id)

# ========== FOOTER ==========
render_standard_footer(disclaimer=False)
