"""
Scores v2 - Redirect to Scores
This page has been merged into Scores.py with Modern View option
Keeping for backward compatibility - redirects to Scores with Modern View enabled
"""

import streamlit as st

# Set session state to enable Modern View
st.session_state['scores_view_mode'] = 'modern'

# Redirect to the unified Scores page
st.switch_page("pages/01_📊_Scores.py")

# ========== HELPER FUNCTIONS ==========

def global_search(query: str) -> list:
    """Search across all specialties"""
    if not query:
        return []
    
    query_lower = query.lower().strip()
    results = []
    
    for specialty, scores in SCORES_BY_SPECIALTY.items():
        for score_id, score_info in scores.items():
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

# Standard page setup
setup_page(
    page_title="Calculators & Thang điểm",
    page_icon="📊",
    description="Thang điểm và calculators lâm sàng, phân loại theo chuyên khoa",
    mobile_header=True
)

# Initialize
init_theme()
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

# ========== MAIN HEADER ==========
st.title("📊 Calculators & Scores")
st.markdown("**Clinical calculators và thang điểm lâm sàng**")

# ========== ENHANCED SEARCH BAR ==========
col_search1, col_search2 = st.columns([4, 1])
with col_search1:
    global_search_query = render_search_with_autocomplete(
        label="🔍 Tìm kiếm calculators",
        placeholder="Nhập tên, viết tắt hoặc từ khóa... (Ctrl+K để focus)",
        key="global_search_v2"
    )

with col_search2:
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔄 Clear", use_container_width=True):
        st.session_state.global_search_v2 = ""
        st.rerun()

# Global search results
global_results = []
if global_search_query:
    global_results = global_search(global_search_query)
    if global_results:
        st.success(f"✅ Tìm thấy {len(global_results)} kết quả")
        # Show quick results
        with st.expander(f"Kết quả tìm kiếm ({len(global_results)})", expanded=True):
            cols = st.columns(min(3, len(global_results[:9])))
            for idx, (spec, sid, sinfo) in enumerate(global_results[:9]):
                with cols[idx % 3]:
                    if st.button(
                        f"**{sinfo['name']}**\n\n{spec}\n\n{sinfo.get('desc', '')[:50]}...",
                        key=f"search_result_{idx}",
                        use_container_width=True
                    ):
                        st.session_state.selected_specialty = spec
                        st.session_state.selected_score_id = sid
                        st.rerun()

st.markdown("---")

# ========== MAIN CONTENT TABS ==========
tab1, tab2, tab3 = st.tabs(["📋 By Specialty Groups", "⭐ Quick Access", "🔍 All Calculators"])

with tab1:
    st.markdown("### Chọn nhóm chuyên khoa")
    
    # Get all specialty groups
    specialty_groups = get_all_groups()
    
    # Render each group
    for group_id, group_info in sorted(specialty_groups.items(), key=lambda x: x[1].get("priority", 99)):
        render_specialty_group(group_id, group_info, SCORES_BY_SPECIALTY)

with tab2:
    render_quick_access_section()

with tab3:
    st.markdown("### Tất cả Calculators")
    
    # Filters
    col_filter1, col_filter2, col_filter3 = st.columns(3)
    with col_filter1:
        filter_status = st.multiselect(
            "Status:",
            ["✅", "🚧", "📋"],
            default=["✅"],
            key="filter_status_all"
        )
    with col_filter2:
        filter_usage = st.multiselect(
            "Usage:",
            ["⭐ Daily Use", "🆕 New"],
            default=[],
            key="filter_usage_all"
        )
    with col_filter3:
        filter_specialty = st.multiselect(
            "Specialty:",
            list(SCORES_BY_SPECIALTY.keys()),
            default=[],
            key="filter_specialty_all"
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
    
    if filter_specialty:
        all_calculators = [c for c in all_calculators if c["specialty"] in filter_specialty]
    
    # Display in grid
    st.markdown(f"**Hiển thị {len(all_calculators)} calculators**")
    
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
                        key_prefix=f"all_{calc['score_id']}"
                    )

# ========== CALCULATOR DISPLAY ==========
# Check if calculator is selected
selected_specialty = st.session_state.get("selected_specialty")
selected_score_id = st.session_state.get("selected_score_id")

if selected_specialty and selected_score_id:
    st.markdown("---")
    st.markdown("---")
    
    # Display calculator
    score_info = SCORES_BY_SPECIALTY[selected_specialty][selected_score_id]
    
    # Header
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
        render_favorite_button(selected_specialty, selected_score_id, score_info['name'], key_suffix="header_v2")
    
    # Route to appropriate calculator
    specialty = selected_specialty
    
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

else:
    # Show welcome message
    st.markdown("---")
    st.info("""
    👈 **Chọn một calculator từ các tabs phía trên để bắt đầu**
    
    - **By Specialty Groups**: Tìm theo nhóm chuyên khoa
    - **Quick Access**: Most Used, Recent, Favorites
    - **All Calculators**: Xem tất cả với filters
    """)

# Footer
render_standard_footer()
