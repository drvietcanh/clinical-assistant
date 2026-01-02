"""
Clinical Guidelines Tracker Module
Track and monitor clinical practice guidelines updates
"""

import streamlit as st
import streamlit.components.v1 as components
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
/* Modern Medical Interface - Clean & Professional (UpToDate/Epocrates Style) */
:root {
    --primary-color: #0066CC;
    --text-primary: #212529;
    --text-secondary: #5f6368;
    --bg-card: #ffffff;
    --border-color: #e0e0e0;
}

/* Card Design - Flat & Clean */
.guideline-card {
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: 8px;
    padding: 20px;
    margin-bottom: 16px;
    border-left: 4px solid #0066CC; /* Default, overridden inline */
    transition: all 0.2s ease-in-out;
}

.guideline-card:hover {
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    transform: translateY(-2px);
    border-color: #b0c4de;
}

/* Typography */
.guideline-title {
    font-family: 'Inter', -apple-system, sans-serif;
    color: var(--primary-color);
    font-size: 1.15rem;
    font-weight: 700;
    margin: 0 0 8px 0;
    line-height: 1.4;
}

.guideline-meta {
    font-size: 0.85rem;
    color: var(--text-secondary);
    margin-bottom: 12px;
    display: flex;
    align-items: center;
    gap: 12px;
    flex-wrap: wrap;
}

.guideline-description {
    color: #333;
    font-size: 0.95rem;
    line-height: 1.6;
    margin: 12px 0;
}

/* Badges - Subtle & Professional */
.badge {
    display: inline-flex;
    align-items: center;
    padding: 3px 10px;
    border-radius: 4px;
    font-size: 0.75rem;
    font-weight: 600;
    letter-spacing: 0.3px;
}

.badge-new {
    background-color: #e8f5e9;
    color: #2e7d32;
    border: 1px solid #c8e6c9;
}

.badge-update {
    background-color: #fff3e0;
    color: #ef6c00;
    border: 1px solid #ffe0b2;
}

.badge-org {
    background-color: #f1f3f4;
    color: #3c4043;
    border: 1px solid #dadce0;
}

/* Clinical Pearl Box */
.pearl-box {
    background-color: #f8f9fa;
    border-radius: 6px;
    padding: 12px 16px;
    margin-top: 12px;
    border-left: 3px solid #fbbc04; /* Amber for insight */
}

.pearl-title {
    font-size: 0.85rem;
    font-weight: 700;
    color: #e37400;
    margin-bottom: 4px;
    display: flex;
    align-items: center;
    gap: 6px;
    text-transform: uppercase;
}

.pearl-content {
    font-size: 0.9rem;
    color: #202124;
    line-height: 1.5;
}

/* Buttons */
.action-link {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    color: #0066CC;
    font-size: 0.9rem;
    font-weight: 600;
    text-decoration: none;
    padding: 6px 12px;
    border-radius: 4px;
    background-color: #f0f7ff;
    transition: background 0.2s;
}

.action-link:hover {
    background-color: #e1effe;
    text-decoration: none;
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
    """Render guideline card với UI sạch, hiện đại, tối ưu cho đọc (UpToDate style)"""
    gradient, border_color = get_category_color(guideline.category)
    org_color = get_org_color(guideline.organization)
    
    # Xác định status
    current_year = 2025
    is_recent = guideline.year >= 2023
    
    status_html = ""
    if guideline.is_high_impact:
         status_html = '<span class="badge" style="background: #e8f0fe; color: #1967d2; border: 1px solid #d2e3fc;">⭐ PRACTICE CHANGING</span>'
    elif is_recent:
        status_html = '<span class="badge badge-new">NEW</span>'
    elif guideline.year >= 2020:
        status_html = '<span class="badge badge-update">UPDATED</span>'
    
    # Build HTML
    card_html_parts = []
    
    # Card Start (Add gold border left for high impact)
    border_style = "border-left-color: #fbbc04;" if guideline.is_high_impact else f"border-left-color: {border_color};"
    card_html_parts.append(f'<div class="guideline-card" style="{border_style}">')
    
    # Header: Title & Status
    card_html_parts.append(f'<div style="display: flex; justify-content: space-between; align-items: flex-start; gap: 12px;">')
    card_html_parts.append(f'<h3 class="guideline-title">{html.escape(guideline.title_vn or guideline.title_en)}</h3>')
    card_html_parts.append(status_html)
    card_html_parts.append('</div>')
    
    # Meta: Org, Year, Category
    card_html_parts.append('<div class="guideline-meta">')
    card_html_parts.append(f'<span class="badge badge-org" style="color: {org_color}; border-color: {org_color}40;">{html.escape(guideline.organization)}</span>')
    card_html_parts.append(f'<span>{guideline.year}</span>')
    card_html_parts.append(f'<span style="color: {border_color}; font-weight: 500;">{html.escape(guideline.category)}</span>')
    card_html_parts.append('</div>')
    
    # Description
    if guideline.description:
        card_html_parts.append(f'<div class="guideline-description">{html.escape(guideline.description)}</div>')
    
    # Clinical Pearl (Key Recommendations)
    if guideline.key_recommendations:
        card_html_parts.append('<div class="pearl-box">')
        card_html_parts.append('<div class="pearl-title">💡 Clinical Pearl</div>')
        card_html_parts.append('<div class="pearl-content"><ul style="margin: 0; padding-left: 20px;">')
        for rec in guideline.key_recommendations[:3]: # Limit to 3 for brevity
            card_html_parts.append(f'<li style="margin-bottom: 4px;">{html.escape(rec)}</li>')
        card_html_parts.append('</ul></div>')
        card_html_parts.append('</div>')
    
    # Actions Footer
    card_html_parts.append('<div style="margin-top: 16px; display: flex; gap: 12px; align-items: center; flex-wrap: wrap;">')
    
    if guideline.url:
        card_html_parts.append(f'<a href="{html.escape(guideline.url)}" target="_blank" class="action-link">🔗 Xem Guideline gốc</a>')
        
    if guideline.related_protocol:
         card_html_parts.append(f'<span style="font-size: 0.85rem; color: #5f6368; margin-left: auto;">📋 Protocol: <strong>{html.escape(guideline.related_protocol)}</strong></span>')

    card_html_parts.append('</div>') # End Footer
    card_html_parts.append('</div>') # End Card
    
    components.html(''.join(card_html_parts), height=0, scrolling=False)
    
    # Interactive Buttons (Protocol + Tools)
    if guideline.related_protocol or guideline.related_tools:
        cols = st.columns([1, 1, 3])
        
        # 1. Protocol Button
        with cols[0]:
            if guideline.related_protocol:
                if st.button(
                    f"📋 Mở Protocol",
                    key=f"proto_btn_{index}",
                    type="primary",
                    use_container_width=True
                ):
                    st.session_state['protocol_specialty'] = guideline.category
                    st.session_state['protocol_to_open'] = guideline.related_protocol
                    st.switch_page("pages/04_📋_Protocols.py")
        
        # 2. Related Tools Buttons
        if guideline.related_tools:
            # We can only show one primary "Tool" button easily in this layout, or list them. 
            # For simplicity, let's just show the first tool or a generic "Tools"
            # Since we can't easily deep link to other pages with args (except standard query params which streamlit handles poorly without full page reload), 
            # we'll simulation "Open Tool" if it points to Scores.
             for idx_tool, tool in enumerate(guideline.related_tools):
                 with cols[1]:
                     # This is a bit hacky for multiple tools, but fine for 1-2. 
                     # Ideally we'd have them in the HTML but deep linking in Streamlit from HTML iframe is hard.
                     if st.button(f"🧮 {tool['name']}", key=f"tool_btn_{index}_{idx_tool}", use_container_width=True):
                         st.switch_page("pages/01_📊_Scores.py") # Simple redirect for now


def render_featured_updates(guidelines):
    """Render section for high impact updates"""
    high_impact = [g for g in guidelines if getattr(g, 'is_high_impact', False)]
    if not high_impact:
        return

    st.markdown("""
    <div style="background: linear-gradient(135deg, #fff8e1 0%, #ffffff 100%); 
                border-left: 4px solid #fbbc04; padding: 16px; border-radius: 8px; margin-bottom: 24px;">
        <h3 style="margin: 0 0 12px 0; color: #b06000; display: flex; align-items: center; gap: 8px; font-size: 1.1rem;">
            <span>⭐</span> Practice Changing Updates
        </h3>
        <p style="margin: 0; color: #5f6368; font-size: 0.9rem;">
            Những cập nhật quan trọng có ảnh hưởng trực tiếp đến thực hành lâm sàng.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Show high impact cards
    for idx, guideline in enumerate(high_impact):
        render_guideline_card(guideline, f"feat_{idx}")



def render_statistics_dashboard(guidelines):
    """Hiển thị dashboard thống kê clean"""
    total = len(guidelines)
    years = [g.year for g in guidelines]
    recent_count = len([y for y in years if y >= 2023])
    
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.metric("Tổng số", total)
    with col2: st.metric("🆕 Mới nhất (≥2023)", recent_count)
    with col3: st.metric("📅 Năm cập nhật", f"{min(years) if years else '-'} - {max(years) if years else '-'}")
    with col4: st.metric("🏥 Chuyên khoa", len(set(g.category for g in guidelines)))

# ========== SIDEBAR ==========
with st.sidebar:
    st.header("📋 Theo dõi Guidelines")
    
    # 1. Personalization Section
    st.subheader("👤 Cá nhân hóa")
    if 'my_specialties' not in st.session_state:
        st.session_state['my_specialties'] = []
        
    my_specialties = st.multiselect(
        "Chuyên khoa quan tâm:",
        options=get_category_list(),
        default=st.session_state.get('my_specialties', []),
        key='pref_specialties',
        help="Chọn chuyên khoa để lọc nhanh trong tab 'Của tôi'"
    )
    # Save to session (auto-handled by key, but explicit update for logic)
    st.session_state['my_specialties'] = my_specialties

    st.markdown("---")
    
    # 2. View Mode
    view_modes = ["Của tôi", "Tất cả", "Gần đây", "Cần cập nhật", "Tìm kiếm"]
    # If no specialties selected, default to "Tất cả" or show tip
    default_index = 0 if my_specialties else 1
    
    view_mode = st.radio(
        "Chế độ xem:",
        view_modes,
        index=default_index,
        key="guidelines_view_mode"
    )
    
    # Filters (only show for relevant modes)
    # Initialize filter variables to avoid NameError
    category_filter = None
    org_filter = None
    year_filter = None
    sort_by = None
    
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
        
        # Year filter - get unique years from guidelines
        all_guidelines = get_all_guidelines()
        years = sorted(set(g.year for g in all_guidelines), reverse=True)
        year_filter = st.selectbox(
            "Lọc theo năm:",
            ["Tất cả"] + [str(year) for year in years],
            key="guidelines_year_filter"
        )
        
        # Sort options
        sort_by = st.selectbox(
            "Sắp xếp theo:",
            ["Năm (mới nhất)", "Năm (cũ nhất)", "Tổ chức", "Chuyên khoa"],
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
# Display based on view mode
if view_mode == "Của tôi":
    st.markdown("### 👤 Dành cho bạn")
    
    if not my_specialties:
        render_info_box("""
        **👋 Chào mừng bạn!**
        
        Để xem các guidelines phù hợp, hãy chọn **Chuyên khoa quan tâm** ở thanh bên trái.
        """, type="info")
        
        # Fallback to recent guidelines but show featured first
        recent = get_recent_guidelines(limit=5)
        render_featured_updates(recent)
        
        st.markdown("#### 🆕 Có thể bạn quan tâm (Mới nhất)")
        for idx, guideline in enumerate(recent):
            if not getattr(guideline, 'is_high_impact', False):
                render_guideline_card(guideline, idx)
            
    else:
        # Get guidelines for selected specialties
        all_guidelines = get_cached_all_guidelines()
        personal_guidelines = [
            g for g in all_guidelines 
            if g.category in my_specialties
        ]
        # Sort by year desc
        personal_guidelines.sort(key=lambda x: x.year, reverse=True)
        
        # Show featured updates for these specialties
        render_featured_updates(personal_guidelines)
        
        if personal_guidelines:
            render_statistics_dashboard(personal_guidelines)
            st.markdown("---")
            
            # Pagination
            items_per_page = 20
            start_idx, end_idx, _, _ = render_pagination(
                total_items=len(personal_guidelines),
                items_per_page=items_per_page,
                page_key="guidelines_page_my",
                show_info=True
            )
            
            for idx, guideline in enumerate(personal_guidelines[start_idx:end_idx]):
                 # Optional: Filter out if already shown in featured? 
                 # Let's keep them for completeness in the list but maybe distinctive style?
                 # For now, just render them all.
                render_guideline_card(guideline, start_idx + idx)
        else:
            st.info(f"Chưa có guideline nào cho các chuyên khoa: {', '.join(my_specialties)}")

elif view_mode == "Tất cả":
    st.markdown("### 📚 Tất cả Guidelines")
    
    # Show featured updates if no heavy filtering (Category/Org) is applied
    if st.session_state.get('guidelines_category_filter', 'Tất cả') == 'Tất cả' and \
       st.session_state.get('guidelines_org_filter', 'Tất cả') == 'Tất cả':
        render_featured_updates(get_cached_all_guidelines())
        st.markdown("---")
    
    # Apply filters (optimized - start with all guidelines and filter down)
    # Only apply filters if they are defined (in "Tất cả" mode)
    category = None
    org = None
    year = None
    
    if view_mode == "Tất cả" and year_filter is not None:
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
    st.markdown("### ⚠️ Guidelines cần cập nhật")
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
            # Delete the key to reset widget value (can't set directly when widget uses the key)
            if 'guidelines_search_query' in st.session_state:
                del st.session_state['guidelines_search_query']
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

