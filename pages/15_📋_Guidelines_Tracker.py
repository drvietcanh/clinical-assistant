"""
Clinical Guidelines Tracker Module
Track and monitor clinical practice guidelines updates
"""

import streamlit as st
import html
from collections import Counter
from utils.page_helper import setup_page, render_standard_footer
from components.ui import render_info_box, render_hero, render_pagination
from guidelines.tracker import (
    search_guidelines,
    get_recent_guidelines,
    check_guideline_updates,
    get_guideline_info
)
from guidelines.data import (
    get_all_guidelines,
    get_guidelines_by_category,
    get_guidelines_by_organization,
    get_category_list,
    get_organization_list
)

# Standard page setup
setup_page(
    page_title="Theo dõi Guidelines",
    page_icon="📋",
    description="Theo dõi và cập nhật các hướng dẫn thực hành lâm sàng"
)

# Inject custom CSS for modern UI (inspired by UpToDate, Medscape, BMJ Best Practice)
st.markdown("""
<style>
/* Enhanced Card Design - UpToDate/Medscape style */
.guideline-card {
    background: white;
    border-radius: 12px;
    padding: 24px;
    margin-bottom: 20px;
    box-shadow: 0 2px 12px rgba(0,0,0,0.08);
    border-left: 5px solid #667eea;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    position: relative;
    overflow: hidden;
}
.guideline-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 5px;
    height: 100%;
    background: var(--border-color, #667eea);
    transition: width 0.3s ease;
}
.guideline-card:hover {
    box-shadow: 0 8px 24px rgba(0,0,0,0.12);
    transform: translateY(-4px);
    border-left-width: 6px;
}
.guideline-card:hover::before {
    width: 6px;
}

/* Enhanced Badge Design */
.org-badge {
    display: inline-flex;
    align-items: center;
    padding: 6px 14px;
    border-radius: 20px;
    font-size: 0.8rem;
    font-weight: 600;
    margin-right: 8px;
    margin-bottom: 8px;
    letter-spacing: 0.3px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}
.category-badge {
    display: inline-flex;
    align-items: center;
    padding: 6px 14px;
    border-radius: 20px;
    font-size: 0.8rem;
    font-weight: 500;
    background: linear-gradient(135deg, #f3e5f5 0%, #e1bee7 100%);
    color: #7b1fa2;
    margin-right: 8px;
    margin-bottom: 8px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}
.year-badge {
    display: inline-flex;
    align-items: center;
    padding: 6px 14px;
    border-radius: 20px;
    font-size: 0.85rem;
    font-weight: 700;
    letter-spacing: 0.5px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.15);
    min-width: 60px;
    justify-content: center;
}

/* Evidence Level Badge - BMJ Best Practice style */
.evidence-badge {
    display: inline-flex;
    align-items: center;
    padding: 4px 10px;
    border-radius: 12px;
    font-size: 0.75rem;
    font-weight: 600;
    margin-left: 8px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

/* Status Indicators */
.status-new {
    background: linear-gradient(135deg, #4caf50 0%, #66bb6a 100%);
    color: white;
    padding: 4px 10px;
    border-radius: 12px;
    font-size: 0.75rem;
    font-weight: 600;
    margin-left: 8px;
}
.status-updated {
    background: linear-gradient(135deg, #ff9800 0%, #ffb74d 100%);
    color: white;
    padding: 4px 10px;
    border-radius: 12px;
    font-size: 0.75rem;
    font-weight: 600;
    margin-left: 8px;
}
.status-old {
    background: linear-gradient(135deg, #f44336 0%, #ef5350 100%);
    color: white;
    padding: 4px 10px;
    border-radius: 12px;
    font-size: 0.75rem;
    font-weight: 600;
    margin-left: 8px;
}

/* Quick Action Buttons */
.quick-action-btn {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 8px 16px;
    border-radius: 8px;
    font-size: 0.85rem;
    font-weight: 500;
    text-decoration: none;
    transition: all 0.2s ease;
    border: 1px solid;
}
.quick-action-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0,0,0,0.15);
}

/* Typography Improvements */
.guideline-title {
    font-size: 1.3rem;
    font-weight: 700;
    line-height: 1.4;
    color: #1a1a1a;
    margin: 0 0 12px 0;
    letter-spacing: -0.3px;
}
.guideline-description {
    color: #424242;
    font-size: 0.95rem;
    line-height: 1.6;
    margin: 12px 0;
}

/* Recommendations Box - Enhanced */
.recommendations-box {
    background: linear-gradient(135deg, #f3f6ff 0%, #e8f0fe 100%);
    border-left: 4px solid;
    border-radius: 8px;
    padding: 16px;
    margin: 16px 0;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
}

/* Mobile Responsive */
@media (max-width: 768px) {
    .guideline-card {
        padding: 16px;
    }
    .guideline-title {
        font-size: 1.1rem;
    }
}
</style>
""", unsafe_allow_html=True)

# ========== CACHING ==========
# Cache guidelines data to avoid repeated calls
@st.cache_data(ttl=3600)  # Cache for 1 hour
def get_cached_all_guidelines():
    """Get all guidelines with caching"""
    return get_all_guidelines()

@st.cache_data(ttl=3600)
def get_cached_years():
    """Get all years with caching"""
    return sorted(set([g.year for g in get_all_guidelines()]), reverse=True)

# ========== HELPER FUNCTIONS ==========

def get_category_color(category: str) -> tuple:
    """Trả về màu gradient và border cho từng category"""
    colors = {
        "Cardiology": ("linear-gradient(135deg, #667eea 0%, #764ba2 100%)", "#667eea"),
        "Infectious": ("linear-gradient(135deg, #f093fb 0%, #f5576c 100%)", "#f5576c"),
        "Respiratory": ("linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)", "#4facfe"),
        "Nephrology": ("linear-gradient(135deg, #43e97b 0%, #38f9d7 100%)", "#43e97b"),
        "Endocrinology": ("linear-gradient(135deg, #fa709a 0%, #fee140 100%)", "#fa709a"),
        "Neurology": ("linear-gradient(135deg, #30cfd0 0%, #330867 100%)", "#30cfd0"),
        "Critical Care": ("linear-gradient(135deg, #a8edea 0%, #fed6e3 100%)", "#a8edea"),
        "Emergency": ("linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%)", "#fcb69f"),
    }
    return colors.get(category, ("linear-gradient(135deg, #667eea 0%, #764ba2 100%)", "#667eea"))


def get_org_color(organization: str) -> str:
    """Trả về màu cho organization badge"""
    org_colors = {
        "AHA": "#c62828",
        "ACC": "#1976d2",
        "ESC": "#0d47a1",
        "IDSA": "#f57c00",
        "KDIGO": "#388e3c",
        "GOLD": "#0288d1",
        "GINA": "#7b1fa2",
        "SSC": "#d32f2f",
        "ADA": "#00796b",
        "ATS": "#455a64",
    }
    for org_key, color in org_colors.items():
        if org_key in organization:
            return color
    return "#616161"


def get_evidence_level(year: int, current_year: int = 2025) -> tuple:
    """Determine evidence level and status based on year"""
    age = current_year - year
    if age <= 1:
        return ("Mới nhất", "status-new", "#4caf50")
    elif age <= 3:
        return ("Cập nhật", "status-updated", "#ff9800")
    else:
        return ("Cần cập nhật", "status-old", "#f44336")


def render_guideline_card(guideline, index: int):
    """Render guideline card với UI đẹp - UpToDate/Medscape style"""
    gradient, border_color = get_category_color(guideline.category)
    org_color = get_org_color(guideline.organization)
    
    # Xác định status và màu sắc
    current_year = 2025
    is_old = guideline.year < 2020
    is_recent = guideline.year >= 2023
    status_text, status_class, status_color = get_evidence_level(guideline.year, current_year)
    
    # Year badge colors - more sophisticated
    if is_recent:
        year_bg = 'linear-gradient(135deg, #4caf50 0%, #66bb6a 100%)'
        year_color = '#ffffff'
    elif guideline.year >= 2020:
        year_bg = 'linear-gradient(135deg, #2196f3 0%, #42a5f5 100%)'
        year_color = '#ffffff'
    else:
        year_bg = 'linear-gradient(135deg, #ff5722 0%, #ff7043 100%)'
        year_color = '#ffffff'
    
    # Build HTML components separately to avoid nested f-string issues
    url_link_html = ""
    if guideline.url:
        url_escaped = html.escape(guideline.url)
        url_link_html = f'''<a href="{url_escaped}" target="_blank" class="quick-action-btn" style="background: {border_color}; color: white; border-color: {border_color};">
                    🔗 Xem guideline đầy đủ
                </a>'''
    
    protocol_html = ""
    if guideline.related_protocol:
        protocol_escaped = html.escape(guideline.related_protocol)
        protocol_html = f'''<span style="color: #616161; font-size: 0.9rem; display: flex; align-items: center; gap: 4px;">
                    📋 <strong>Protocol:</strong> {protocol_escaped}
                </span>'''
    
    last_updated_html = ""
    if guideline.last_updated:
        last_updated_escaped = html.escape(guideline.last_updated)
        last_updated_html = f'''<span style="color: #757575; font-size: 0.85rem; display: flex; align-items: center; gap: 4px;">
                🔄 <span>Cập nhật: {last_updated_escaped}</span>
            </span>'''
    
    # Build HTML using enhanced design
    card_html = f"""
    <div class="guideline-card" style="--border-color: {border_color}; border-left-color: {border_color};">
        <div style="display: flex; justify-content: space-between; align-items: start; margin-bottom: 16px; gap: 16px;">
            <h3 class="guideline-title" style="flex: 1; margin: 0;">
                {html.escape(guideline.title_vn)}
            </h3>
            <div style="display: flex; flex-direction: column; align-items: flex-end; gap: 8px;">
            <span class="year-badge" style="background: {year_bg}; color: {year_color};">
                {guideline.year}
            </span>
                <span class="{status_class}" style="background: {status_color};">
                    {status_text}
                </span>
            </div>
        </div>
        
        <div style="margin-bottom: 16px; display: flex; flex-wrap: wrap; gap: 8px; align-items: center;">
            <span class="org-badge" style="background: {org_color}15; color: {org_color}; border: 2px solid {org_color}40;">
                🏢 {html.escape(guideline.organization)}
            </span>
            <span class="category-badge">
                🩺 {html.escape(guideline.category)}
            </span>
            {f'<span class="evidence-badge" style="background: {border_color}20; color: {border_color}; border: 1px solid {border_color}40;">📊 Evidence-Based</span>' if guideline.key_recommendations else ''}
        </div>
        
        {f'<p class="guideline-description">{html.escape(guideline.description)}</p>' if guideline.description else ''}
        
        {"" if not guideline.key_recommendations else f'''
        <div class="recommendations-box" style="border-left-color: {border_color};">
            <div style="font-weight: 700; color: {border_color}; margin-bottom: 10px; font-size: 0.9rem; display: flex; align-items: center; gap: 6px;">
                <span>⭐</span> <span>Khuyến nghị chính:</span>
            </div>
            <ul style="margin: 0; padding-left: 24px; color: #37474f; font-size: 0.9rem; line-height: 1.8;">
                {''.join([f'<li style="margin-bottom: 8px; padding-left: 4px;">{html.escape(rec)}</li>' for rec in guideline.key_recommendations[:5]])}
            </ul>
        </div>
        '''}
        
        <div style="margin-top: 20px; padding-top: 16px; border-top: 1px solid #e0e0e0; display: flex; gap: 12px; flex-wrap: wrap; align-items: center; justify-content: space-between;">
            <div style="display: flex; gap: 16px; flex-wrap: wrap; align-items: center;">
                {url_link_html if guideline.url else ''}
                {protocol_html if guideline.related_protocol else ''}
            </div>
            {last_updated_html if guideline.last_updated else ''}
        </div>
    </div>
    """
    
    # Render HTML directly
    st.markdown(card_html, unsafe_allow_html=True)
    
    # Protocol deep link button
    if guideline.related_protocol:
        col1, col2 = st.columns([1, 4])
        with col1:
            if st.button(
                "📋 Mở Protocol",
                key=f"protocol_btn_{guideline.id}_{index}",
                use_container_width=True,
                help=f"Mở protocol: {html.escape(guideline.related_protocol)}",
                type="primary"
            ):
                # Store protocol selection in session state
                st.session_state['protocol_specialty'] = guideline.category
                st.session_state['protocol_to_open'] = guideline.related_protocol
                st.switch_page("pages/04_📋_Protocols.py")
        with col2:
            st.caption(f"💡 Có protocol tương ứng: **{html.escape(guideline.related_protocol)}**")
    
    st.markdown("---")


def render_statistics_dashboard(guidelines):
    """Hiển thị dashboard thống kê"""
    total = len(guidelines)
    categories = Counter([g.category for g in guidelines])
    organizations = Counter([g.organization for g in guidelines])
    years = [g.year for g in guidelines]
    recent_count = len([y for y in years if y >= 2020])
    old_count = len([y for y in years if y < 2020])
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.metric("📋 Tổng số", total)
    with col2:
        st.metric("🩺 Chuyên khoa", len(categories))
    with col3:
        st.metric("🏢 Tổ chức", len(organizations))
    with col4:
        st.metric("🆕 Gần đây (≥2020)", recent_count)
    with col5:
        st.metric("⚠️ Cần cập nhật (<2020)", old_count)


# ========== SIDEBAR ==========
with st.sidebar:
    st.header("📋 Theo dõi Guidelines")
    st.caption("Module **Theo dõi Guidelines** – theo dõi các hướng dẫn thực hành lâm sàng.")
    
    view_mode = st.radio(
        "Chế độ xem:",
        ["Tất cả", "Gần đây", "Cần cập nhật", "Tìm kiếm"],
        key="guidelines_view_mode"
    )
    
    # Filters
    if view_mode == "Tất cả":
        category_filter = st.selectbox(
            "Lọc theo chuyên khoa:",
            ["Tất cả"] + get_category_list(),
            key="guidelines_category_filter"
        )
        
        org_filter = st.selectbox(
            "Lọc theo tổ chức:",
            ["Tất cả"] + get_organization_list(),
            key="guidelines_org_filter"
        )
        
        # Year filter (using cached data)
        all_years = get_cached_years()
        year_filter = st.selectbox(
            "Lọc theo năm:",
            ["Tất cả"] + [str(y) for y in all_years],
            key="guidelines_year_filter"
        )
        
        # Sort options
        sort_by = st.selectbox(
            "Sắp xếp theo:",
            ["Năm (mới nhất)", "Năm (cũ nhất)", "Tổ chức", "Chuyên khoa", "Tên"],
            key="guidelines_sort"
        )
    
    st.markdown("---")
    render_info_box(
        """
    **📋 Guidelines Tracker:**
    - Theo dõi **guidelines** từ các tổ chức uy tín
    - **AHA/ACC**, **ESC**, **IDSA**, **KDIGO**, **GOLD**, **GINA**, etc.
    - Liên kết với **protocols** trong app
    - Cảnh báo guidelines **cần cập nhật**
    
    **💡 Lưu ý:**
    - Guidelines được cập nhật thường xuyên
    - Luôn tham khảo phiên bản mới nhất
    - Click vào link để xem guideline đầy đủ
        """,
        type="info",
        title="Thông tin Module"
    )

# ========== MAIN CONTENT ==========

# Enhanced Hero section using standard component
render_hero(
    title="Clinical Guidelines Tracker",
    subtitle="📋 Theo dõi hướng dẫn lâm sàng",
    description="Theo dõi và cập nhật các hướng dẫn thực hành lâm sàng từ các tổ chức uy tín: AHA/ACC, ESC, IDSA, KDIGO, GOLD, GINA, SSC, ADA, và nhiều tổ chức khác",
    icon="📋",
    gradient=("#667eea", "#764ba2")
)

# Display based on view mode
if view_mode == "Tất cả":
    st.markdown("### 📚 Tất cả Guidelines")
    
    # Apply filters (optimized - start with all guidelines and filter down)
    category = None if category_filter == "Tất cả" else category_filter
    org = None if org_filter == "Tất cả" else org_filter
    year = None if year_filter == "Tất cả" else int(year_filter)
    
    # Start with all guidelines (cached)
    guidelines = get_cached_all_guidelines()
    
    # Apply filters efficiently (single pass)
    if category:
        guidelines = [g for g in guidelines if g.category == category]
    if org:
        guidelines = [g for g in guidelines if org in g.organization]
    if year:
        guidelines = [g for g in guidelines if g.year == year]
    
    # Sort guidelines
    if sort_by == "Năm (mới nhất)":
        guidelines.sort(key=lambda x: x.year, reverse=True)
    elif sort_by == "Năm (cũ nhất)":
        guidelines.sort(key=lambda x: x.year)
    elif sort_by == "Tổ chức":
        guidelines.sort(key=lambda x: x.organization)
    elif sort_by == "Chuyên khoa":
        guidelines.sort(key=lambda x: x.category)
    elif sort_by == "Tên":
        guidelines.sort(key=lambda x: x.title_vn)
    
    # Statistics dashboard
    if guidelines:
        render_statistics_dashboard(guidelines)
        st.markdown("---")
        st.success(f"✅ Tìm thấy {len(guidelines)} guidelines")
        
        # Pagination using standard component
        items_per_page = 20
        start_idx, end_idx, _, _ = render_pagination(
            total_items=len(guidelines),
            items_per_page=items_per_page,
            page_key="guidelines_page_all",
            show_info=True
        )
        paginated_guidelines = guidelines[start_idx:end_idx]
        
        # Display guidelines with cards
        for idx, guideline in enumerate(paginated_guidelines):
            render_guideline_card(guideline, start_idx + idx)
    else:
        st.warning("Không tìm thấy guidelines với bộ lọc đã chọn.")

elif view_mode == "Gần đây":
    st.markdown("### 🆕 Guidelines Gần Đây")
    
    recent = get_recent_guidelines(limit=100, min_year=2020)  # Increased limit
    
    if recent:
        render_statistics_dashboard(recent)
        st.markdown("---")
        st.success(f"✅ Tìm thấy {len(recent)} guidelines gần đây (từ 2020)")
        
        # Pagination using standard component
        items_per_page = 20
        start_idx, end_idx, _, _ = render_pagination(
            total_items=len(recent),
            items_per_page=items_per_page,
            page_key="guidelines_page_recent",
            show_info=True
        )
        paginated_recent = recent[start_idx:end_idx]
        
        for idx, guideline in enumerate(paginated_recent):
            render_guideline_card(guideline, start_idx + idx)
    else:
        st.warning("Không tìm thấy guidelines gần đây.")

elif view_mode == "Cần cập nhật":
    st.markdown("### ⚠️ Guidelines Cần Cập Nhật")
    st.info("Guidelines cũ hơn 2020 có thể cần được cập nhật. Vui lòng kiểm tra phiên bản mới nhất.")
    
    old_guidelines = check_guideline_updates(year_threshold=2020)
    old_guidelines.sort(key=lambda x: x.year)  # Sort by year (oldest first)
    
    if old_guidelines:
        render_statistics_dashboard(old_guidelines)
        st.markdown("---")
        st.warning(f"⚠️ Tìm thấy {len(old_guidelines)} guidelines có thể cần cập nhật")
        
        # Pagination using standard component
        items_per_page = 20
        start_idx, end_idx, _, _ = render_pagination(
            total_items=len(old_guidelines),
            items_per_page=items_per_page,
            page_key="guidelines_page_old",
            show_info=True
        )
        paginated_old = old_guidelines[start_idx:end_idx]
        
        for idx, guideline in enumerate(paginated_old):
            render_guideline_card(guideline, start_idx + idx)
    else:
        st.success("✅ Tất cả guidelines đều gần đây (từ 2020 trở lên).")

else:  # Tìm kiếm
    st.markdown("### 🔍 Tìm kiếm Guidelines")
    
    # Enhanced search with suggestions
    col1, col2 = st.columns([3, 1])
    with col1:
        search_query = st.text_input(
            "🔍 Nhập từ khóa tìm kiếm:",
            placeholder="Ví dụ: Heart failure, Sepsis, Diabetes, Hypertension, AHA, ESC...",
            key="guidelines_search_query",
            help="Tìm kiếm theo tên bệnh, chuyên khoa, tổ chức, hoặc từ khóa bất kỳ"
        )
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)  # Spacing
        if st.button("🔄 Xóa", use_container_width=True, help="Xóa từ khóa tìm kiếm"):
            st.session_state['guidelines_search_query'] = ""
            st.rerun()
    
    # Quick search suggestions
    if not search_query:
        st.markdown("""
        <div style="background: #f5f5f5; padding: 1rem; border-radius: 8px; margin-top: 1rem;">
            <div style="font-size: 0.85rem; color: #616161; margin-bottom: 8px; font-weight: 600;">
                💡 Gợi ý tìm kiếm:
            </div>
            <div style="display: flex; flex-wrap: wrap; gap: 8px;">
                <span style="background: white; padding: 6px 12px; border-radius: 16px; font-size: 0.8rem; 
                            color: #1976d2; border: 1px solid #1976d2; cursor: pointer;">Heart Failure</span>
                <span style="background: white; padding: 6px 12px; border-radius: 16px; font-size: 0.8rem; 
                            color: #1976d2; border: 1px solid #1976d2; cursor: pointer;">Sepsis</span>
                <span style="background: white; padding: 6px 12px; border-radius: 16px; font-size: 0.8rem; 
                            color: #1976d2; border: 1px solid #1976d2; cursor: pointer;">Diabetes</span>
                <span style="background: white; padding: 6px 12px; border-radius: 16px; font-size: 0.8rem; 
                            color: #1976d2; border: 1px solid #1976d2; cursor: pointer;">AHA</span>
                <span style="background: white; padding: 6px 12px; border-radius: 16px; font-size: 0.8rem; 
                            color: #1976d2; border: 1px solid #1976d2; cursor: pointer;">KDIGO</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    if search_query:
        results = search_guidelines(search_query)
        results.sort(key=lambda x: x.year, reverse=True)  # Sort by year (newest first)
        
        if results:
            render_statistics_dashboard(results)
            st.markdown("---")
            st.success(f"✅ Tìm thấy {len(results)} kết quả cho '{search_query}'")
            
            # Pagination using standard component
            items_per_page = 20
            start_idx, end_idx, _, _ = render_pagination(
                total_items=len(results),
                items_per_page=items_per_page,
                page_key="guidelines_page_search",
                show_info=True
            )
            paginated_results = results[start_idx:end_idx]
            
            for idx, guideline in enumerate(paginated_results):
                render_guideline_card(guideline, start_idx + idx)
        else:
            st.warning("Không tìm thấy kết quả. Vui lòng thử lại với từ khóa khác.")
            st.info("💡 Gợi ý: Thử tìm kiếm theo tên bệnh, chuyên khoa, hoặc tên tổ chức (VD: AHA, ESC, IDSA)")

# Additional information
st.markdown("---")
st.markdown("### 📚 Thông tin về Guidelines")
st.markdown("""
**Các tổ chức guidelines chính:**

1. **AHA/ACC** - American Heart Association / American College of Cardiology
   - Cardiology guidelines (Heart failure, ACS, Hypertension, Atrial fibrillation)

2. **ESC** - European Society of Cardiology
   - European cardiology guidelines

3. **IDSA** - Infectious Diseases Society of America
   - Infectious diseases guidelines (Pneumonia, Sepsis)

4. **KDIGO** - Kidney Disease: Improving Global Outcomes
   - Nephrology guidelines (AKI, CKD)

5. **GOLD** - Global Initiative for Chronic Obstructive Lung Disease
   - COPD guidelines

6. **GINA** - Global Initiative for Asthma
   - Asthma guidelines

7. **SSC** - Surviving Sepsis Campaign
   - Sepsis and septic shock guidelines

8. **ADA** - American Diabetes Association
   - Diabetes guidelines

**Lưu ý:**
- Guidelines được cập nhật thường xuyên
- Luôn tham khảo phiên bản mới nhất từ website chính thức
- Một số guidelines có thể có phiên bản cập nhật không được liệt kê ở đây
- Click vào link để xem guideline đầy đủ và phiên bản mới nhất
""")

# Footer
render_standard_footer(disclaimer=True)

