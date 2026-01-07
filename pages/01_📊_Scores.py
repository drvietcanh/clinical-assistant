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

# Import Geriatrics module
try:
    from scores import geriatrics
    GERIATRICS_AVAILABLE = True
except ImportError:
    GERIATRICS_AVAILABLE = False
from components.scores_favorites import (
    render_favorites_section_in_sidebar,
    render_favorite_button,
    is_favorite
)
from components.scores_dark_mode import init_theme, render_theme_toggle
from components.scores_autocomplete import render_search_with_autocomplete, add_to_recent_searches
from components.scores_related import render_related_calculators
from components.scores_mobile import init_mobile_optimizations
from components.scores_references import render_references

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

# View mode toggle
if 'scores_view_mode' not in st.session_state:
    st.session_state.scores_view_mode = 'classic'  # 'classic' or 'modern'

# Import recent tracking
try:
    from components.scores_recent import add_to_recent
    RECENT_TRACKING_AVAILABLE = True
except ImportError:
    RECENT_TRACKING_AVAILABLE = False
    def add_to_recent(specialty, score_id, score_name):
        pass

# Add toggle button at top
col_toggle1, col_toggle2, col_toggle3 = st.columns([1, 3, 1])
with col_toggle2:
    view_mode = st.radio(
        "View Mode:",
        ["Classic View", "Modern View"],
        index=0 if st.session_state.scores_view_mode == 'classic' else 1,
        horizontal=True,
        key="view_mode_toggle"
    )
    if view_mode == "Modern View":
        st.session_state.scores_view_mode = 'modern'
    else:
        st.session_state.scores_view_mode = 'classic'

st.markdown("---")

# Main tabs: Scores and Labs
main_tab1, main_tab2 = st.tabs(["📊 Clinical Scores", "🔬 Labs & Calculators"])

# Render Scores content based on view mode (inside Scores tab)
with main_tab1:
    if st.session_state.scores_view_mode == 'modern':
        # Import modern view components
        try:
            from scores.ui_scores_view import (
                render_calculator_card,
                render_specialty_group,
                render_quick_access_section,
                is_daily_use
            )
            from scores.specialty_groups import get_all_groups
            
            # Modern View Layout
            st.title("📊 Calculators & Scores")
            st.markdown("**Clinical calculators và thang điểm lâm sàng**")
            
            # Enhanced Search
            col_search1, col_search2 = st.columns([4, 1])
            with col_search1:
                global_search_query = render_search_with_autocomplete(
                    label="🔍 Tìm kiếm calculators",
                    placeholder="Nhập tên, viết tắt hoặc từ khóa...",
                    key="global_search_modern"
                )
            with col_search2:
                st.markdown("<br>", unsafe_allow_html=True)
                if st.button("🔄 Clear", use_container_width=True):
                    st.session_state.global_search_modern = ""
                    st.rerun()
            
            # Search results
            global_results = []
            if global_search_query:
                global_results = global_search(global_search_query)
                if global_results:
                    st.success(f"✅ Tìm thấy {len(global_results)} kết quả")
                    with st.expander(f"Kết quả tìm kiếm ({len(global_results)})", expanded=True):
                        cols = st.columns(min(3, len(global_results[:9])))
                        for idx, (spec, sid, sinfo) in enumerate(global_results[:9]):
                            with cols[idx % 3]:
                                if st.button(
                                    f"**{sinfo['name']}**\n\n{spec}",
                                    key=f"search_result_modern_{idx}",
                                    use_container_width=True
                                ):
                                    st.session_state.selected_specialty = spec
                                    st.session_state.selected_score_id = sid
                                    if RECENT_TRACKING_AVAILABLE:
                                        add_to_recent(spec, sid, sinfo['name'])
                                    st.rerun()
            
            st.markdown("---")
            
            # Main Content Tabs
            tab1, tab2, tab3 = st.tabs(["📋 By Specialty Groups", "⭐ Quick Access", "🔍 All Calculators"])
            
            with tab1:
                st.markdown("### Chọn nhóm chuyên khoa")
                specialty_groups = get_all_groups()
                for group_id, group_info in sorted(specialty_groups.items(), key=lambda x: x[1].get("priority", 99)):
                    render_specialty_group(group_id, group_info, SCORES_BY_SPECIALTY)
            
            with tab2:
                render_quick_access_section()
            
            with tab3:
                st.markdown("### Tất cả Calculators")
                # Filters
                col_filter1, col_filter2 = st.columns(2)
                with col_filter1:
                    filter_status = st.multiselect(
                        "Status:",
                        ["✅", "🚧", "📋"],
                        default=["✅"],
                        key="filter_status_all_modern"
                    )
                with col_filter2:
                    filter_usage = st.multiselect(
                        "Usage:",
                        ["⭐ Daily Use", "🆕 New"],
                        default=[],
                        key="filter_usage_all_modern"
                    )
                
                # Get all calculators
                all_calculators = get_all_scores_flat()
                
                # Apply filters
                if filter_status:
                    all_calculators = [c for c in all_calculators if c["score_info"].get("status") in filter_status]
                
                if filter_usage:
                    filtered = []
                    for calc in all_calculators:
                        if "⭐ Daily Use" in filter_usage and is_daily_use(calc["score_info"]):
                            filtered.append(calc)
                        elif "🆕 New" in filter_usage and ("🆕" in calc["score_info"].get("name", "") or "MỚI" in calc["score_info"].get("desc", "")):
                            filtered.append(calc)
                    if filtered:
                        all_calculators = filtered
                
                st.markdown(f"**Hiển thị {len(all_calculators)} calculators**")
                
                # Display in grid
                num_cols = 3
                for i in range(0, len(all_calculators), num_cols):
                    cols = st.columns(num_cols)
                    for j, col in enumerate(cols):
                        if i + j < len(all_calculators):
                            calc = all_calculators[i + j]
                            with col:
                                render_calculator_card(
                                    calc["score_id"],
                                    calc["score_info"],
                                    calc["specialty"],
                                    key_prefix=f"all_modern_{calc['score_id']}"
                                )
            
            # Calculator Display for Modern View
            selected_specialty = st.session_state.get("selected_specialty")
            selected_score_id = st.session_state.get("selected_score_id")
            
            if selected_specialty and selected_score_id:
                st.markdown("---")
                st.markdown("---")
                
                # Track recent
                if RECENT_TRACKING_AVAILABLE:
                    score_info = SCORES_BY_SPECIALTY[selected_specialty][selected_score_id]
                    add_to_recent(selected_specialty, selected_score_id, score_info['name'])
                
                # Display calculator header
                score_info = SCORES_BY_SPECIALTY[selected_specialty][selected_score_id]
                col_header1, col_header2 = st.columns([4, 1])
                with col_header1:
                    st.markdown(f"""
                    <div style="background: white; padding: 20px; border-radius: 8px; border-left: 4px solid #007bff; box-shadow: 0 1px 3px rgba(0,0,0,0.1); margin-bottom: 20px;">
                        <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 8px;">
                            <span style="background: #e8f0fe; color: #1967d2; padding: 4px 12px; border-radius: 16px; font-size: 0.8em; font-weight: 600;">{selected_specialty}</span>
                            {'<span style="background: #e6fffa; color: #047481; padding: 4px 12px; border-radius: 16px; font-size: 0.8em; font-weight: 600;">⭐ Dùng hàng ngày</span>' if is_daily_use(score_info) else ''}
                        </div>
                        <h2 style="color: #1a73e8; margin: 0 0 10px 0; font-size: 1.5em;">{score_info['name']}</h2>
                        <p style="color: #5f6368; margin: 0; line-height: 1.5;">{score_info.get('desc', '')}</p>
                    </div>
                    """, unsafe_allow_html=True)
                with col_header2:
                    render_favorite_button(selected_specialty, selected_score_id, score_info['name'], key_suffix="header_modern")
                
                # Route to calculator - will be handled at the end of file
                st.session_state.modern_view_calculator_selected = True
                st.session_state.modern_view_specialty = selected_specialty
                st.session_state.modern_view_score_id = selected_score_id
                
        except ImportError as e:
            st.error(f"Modern View components chưa sẵn sàng: {e}")
            st.session_state.scores_view_mode = 'classic'
            st.session_state.modern_view_calculator_selected = False
        else:
            st.session_state.modern_view_calculator_selected = False
    
    # Classic View content (only render if not modern view)
    if st.session_state.scores_view_mode != 'modern':

# Initialize dark mode (runs for both views)
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
            st.info("🔬 Labs & Calculators đã tích hợp vào tab Labs")
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
    
    # Simple markdown to avoid any HTML rendering quirks
    st.info(
        "**Chú thích trạng thái calculator:**\n"
        "- ✅ Hoàn thành, có thể dùng lâm sàng\n"
        "- 🚧 Đang cập nhật/hoàn thiện\n"
        "- 📋 Đang trong kế hoạch"
    )
    
    st.markdown("---")
    st.caption(f"**{len([s for specialty_scores in SCORES_BY_SPECIALTY.values() for s in specialty_scores])}** calculators")
    st.caption("**Dựa trên bằng chứng**")

        # Display specialty overview with enhanced UI
        current_name = SCORES_BY_SPECIALTY[specialty][selected_score_id]['name'] if selected_score_id else "Chọn calculator bên trái"
    current_desc = SCORES_BY_SPECIALTY[specialty][selected_score_id].get('desc', '') if selected_score_id else ""

    # Enhanced header with favorite button using Modern UI
    col_header1, col_header2 = st.columns([4, 1])
    with col_header1:
    if selected_score_id:
        st.markdown(f"""
        <div style="background: white; padding: 20px; border-radius: 8px; border-left: 4px solid #007bff; box-shadow: 0 1px 3px rgba(0,0,0,0.1); margin-bottom: 20px;">
            <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 8px;">
                <span style="background: #e8f0fe; color: #1967d2; padding: 4px 12px; border-radius: 16px; font-size: 0.8em; font-weight: 600;">{specialty}</span>
                {'<span style="background: #e6fffa; color: #047481; padding: 4px 12px; border-radius: 16px; font-size: 0.8em; font-weight: 600;">⭐ Dùng hàng ngày</span>' if is_daily_use(SCORES_BY_SPECIALTY[specialty][selected_score_id]) else ''}
            </div>
            <h2 style="color: #1a73e8; margin: 0 0 10px 0; font-size: 1.5em;">{current_name}</h2>
            <p style="color: #5f6368; margin: 0; line-height: 1.5;">{current_desc}</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div style="background: #f8f9fa; padding: 20px; border-radius: 8px; border: 1px dashed #ced4da; margin-bottom: 20px; text-align: center;">
            <p style="color: #6c757d; margin: 0;">👈 Chọn một calculator từ danh sách bên trái để bắt đầu</p>
            <div style="margin-top: 10px;">
                <span style="background: #e9ecef; color: #495057; padding: 4px 12px; border-radius: 16px; font-size: 0.85em;">{len(scores_in_specialty)} calculators</span>
                <span style="background: #e9ecef; color: #495057; padding: 4px 12px; border-radius: 16px; font-size: 0.85em;">{specialty}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col_header2:
        if selected_score_id:
            render_favorite_button(specialty, selected_score_id, current_name, key_suffix="header")

    # ========== ROUTE TO APPROPRIATE MODULE ==========

    # Helper function to render calculator and related
    def render_calculator_with_related(specialty_name: str, score_id: str, render_func):
    """Render calculator and show related calculators"""
    if score_id:
        # Track recent
        if RECENT_TRACKING_AVAILABLE:
            score_info = SCORES_BY_SPECIALTY[specialty_name][score_id]
            add_to_recent(specialty_name, score_id, score_info['name'])
        
        render_func(score_id)
        # Verify if specialty/score info is available to pass to render_references
        # It's better to modify render_related_calculators or add it here if we have access to score_info
        # We need to look up score_info from global SCORES_BY_SPECIALTY
        from scores.config import SCORES_BY_SPECIALTY
        if specialty_name in SCORES_BY_SPECIALTY and score_id in SCORES_BY_SPECIALTY[specialty_name]:
            score_info = SCORES_BY_SPECIALTY[specialty_name][score_id]
            render_references(score_info)
            
            # Show related calculators
            render_related_calculators(specialty_name, score_id)

    # Track recent when calculator is selected
    if selected_score_id and RECENT_TRACKING_AVAILABLE:
        score_info = SCORES_BY_SPECIALTY[specialty][selected_score_id]
        add_to_recent(specialty, selected_score_id, score_info['name'])

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

    # Geriatrics
    elif "Lão khoa" in specialty or "Geriatrics" in specialty:
        if selected_score_id and GERIATRICS_AVAILABLE:
            geriatrics.render_geriatrics_calculator(selected_score_id)
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
    
    # ========== MODERN VIEW CALCULATOR ROUTING ==========
    # Handle calculator rendering for Modern View
    if st.session_state.get('modern_view_calculator_selected', False):
    modern_specialty = st.session_state.get('modern_view_specialty')
    modern_score_id = st.session_state.get('modern_view_score_id')
    
    if modern_specialty and modern_score_id:
        # Track recent
        if RECENT_TRACKING_AVAILABLE:
            score_info = SCORES_BY_SPECIALTY[modern_specialty][modern_score_id]
            add_to_recent(modern_specialty, modern_score_id, score_info['name'])
        
        # Route to appropriate calculator (same logic as classic view)
        specialty = modern_specialty
        selected_score_id = modern_score_id
        
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
        
        # Geriatrics
        elif "Lão khoa" in specialty or "Geriatrics" in specialty:
            if selected_score_id and GERIATRICS_AVAILABLE:
                geriatrics.render_geriatrics_calculator(selected_score_id)
                render_related_calculators(specialty, selected_score_id)
    
    # End of Classic View content in main_tab1

# ========== LABS TAB CONTENT ==========
with main_tab2:
    # Import Labs functionality
    try:
        from labs import (
            render_cbc,
            render_bmp,
            render_cmp,
            render_lft,
            render_lipid,
            render_cardiac_markers,
            render_coag,
            render_thyroid,
            render_abg,
            render_trend_analysis,
            render_panel_calculator
        )
        from scores.metabolism.bmi_ibw_bsa import render as render_bmi_ibw_bsa
        from scores.metabolism.osmolality import render as render_osmolality
        from scores.metabolism.anion_gap import render as render_anion_gap
        from scores.metabolism.corrected_calcium import render as render_corrected_calcium
        from scores.metabolism.fena import render as render_fena
        from scores.metabolism.hba1c_eag import render as render_hba1c_eag
        from scores.metabolism.winter_formula import render as render_winter_formula
        from scores.metabolism.free_t4_index import render as render_free_t4_index
        from scores.nephrology.egfr import render as render_egfr
        
        st.title("🔬 Labs & Calculators")
        st.markdown("**Tra cứu giá trị xét nghiệm, giải thích kết quả và tính toán công thức lâm sàng**")
        
        # Sidebar for Labs
        with st.sidebar:
            st.markdown("---")
            st.subheader("🔬 Labs & Calculators")
            st.caption("Module **Xét nghiệm & Calculators** – đã tích hợp vào Scores.")
            
            category = st.radio(
                "Loại công cụ:",
                [
                    "🧮 Calculators",
                    "🔬 Lab Panels",
                    "📈 Lab Enhancement",
                    "🔄 Unit Converter"
                ],
                index=0,
                key="labs_category"
            )
            
            st.markdown("---")
            
            if category == "🧮 Calculators":
                calculator_type = st.selectbox(
                    "Calculator:",
                    [
                        "📏 BMI | IBW | BSA",
                        "🧪 eGFR/GFR Calculator",
                        "💧 Osmolality & Gap",
                        "⚖️ Anion Gap",
                        "🦴 Corrected Calcium",
                        "🧪 FENa",
                        "📊 HbA1c ↔ eAG",
                        "🌡️ Winter Formula",
                        "🔬 Free T4 Index",
                        "💊 Lipid Panel Calculator"
                    ],
                    key="labs_calculator"
                )
            elif category == "🔬 Lab Panels":
                lab_panel = st.selectbox(
                    "Lab Panel:",
                    [
                        "🩸 CBC - Complete Blood Count",
                        "🧪 BMP - Basic Metabolic Panel",
                        "🧪 CMP - Comprehensive Metabolic Panel",
                        "🫀 LFT - Liver Function Tests",
                        "❤️ Cardiac Markers",
                        "🩸 Coagulation Panel",
                        "🦋 Thyroid Function Tests",
                        "💨 ABG - Arterial Blood Gas"
                    ],
                    key="labs_panel"
                )
            elif category == "📈 Lab Enhancement":
                enhancement_type = st.selectbox(
                    "Tính năng:",
                    [
                        "📈 Lab Trend Analysis",
                        "🧮 Lab Panel Calculator"
                    ],
                    key="labs_enhancement"
                )
        
        # Main content routing
        if category == "🧮 Calculators":
            st.info(f"**Calculator:** {calculator_type}")
            st.markdown("---")
            
            if "BMI" in calculator_type or "IBW" in calculator_type or "BSA" in calculator_type:
                render_bmi_ibw_bsa()
            elif "eGFR" in calculator_type or "GFR" in calculator_type:
                render_egfr()
            elif "Osmolality" in calculator_type:
                render_osmolality()
            elif "Anion Gap" in calculator_type:
                render_anion_gap()
            elif "Corrected" in calculator_type or "Calcium" in calculator_type:
                render_corrected_calcium()
            elif "FENa" in calculator_type:
                render_fena()
            elif "HbA1c" in calculator_type or "eAG" in calculator_type:
                render_hba1c_eag()
            elif "Winter" in calculator_type:
                render_winter_formula()
            elif "T4" in calculator_type or "Free" in calculator_type:
                render_free_t4_index()
            elif "Lipid" in calculator_type:
                render_lipid()
        
        elif category == "🔬 Lab Panels":
            st.info(f"**Lab Panel:** {lab_panel.split(' - ')[1] if ' - ' in lab_panel else lab_panel}")
            st.markdown("---")
            
            if "CBC" in lab_panel:
                render_cbc()
            elif "BMP" in lab_panel and "CMP" not in lab_panel:
                render_bmp()
            elif "CMP" in lab_panel:
                render_cmp()
            elif "LFT" in lab_panel or "Liver" in lab_panel:
                render_lft()
            elif "Cardiac" in lab_panel:
                render_cardiac_markers()
            elif "Coag" in lab_panel:
                render_coag()
            elif "Thyroid" in lab_panel:
                render_thyroid()
            elif "ABG" in lab_panel:
                render_abg()
        
        elif category == "📈 Lab Enhancement":
            if "Trend Analysis" in enhancement_type:
                render_trend_analysis()
            elif "Panel Calculator" in enhancement_type:
                render_panel_calculator()
        
        elif category == "🔄 Unit Converter":
            try:
                from components.unit_converter_enhanced import render_enhanced_unit_converter
                render_enhanced_unit_converter()
            except ImportError:
                st.info("Unit Converter đang được phát triển")
        
        st.markdown("---")
        st.warning("""
        **⚠️ Lưu ý quan trọng về Lab:**
        - Khoảng giá trị tham chiếu có thể khác nhau giữa các phòng xét nghiệm
        - Luôn so sánh với khoảng giá trị của phòng xét nghiệm địa phương bạn
        - Giá trị nguy kịch cần đối chiếu lâm sàng ngay lập tức
        """)
        
    except ImportError as e:
        st.error(f"Không thể tải module Labs: {e}")
        st.info("Vui lòng kiểm tra module labs hoặc truy cập trang Labs riêng biệt.")
        if st.button("Mở trang Labs riêng"):
            st.switch_page("pages/05_🔬_Labs_and_Calculators.py")

# ========== FOOTER ==========
render_standard_footer(disclaimer=False)
