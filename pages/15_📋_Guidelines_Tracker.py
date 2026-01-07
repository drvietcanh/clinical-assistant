"""
Clinical Guidelines Tracker Module - Optimized UI
Track and monitor clinical practice guidelines updates
Mobile-first design inspired by UpToDate, Medscape, BMJ Best Practice
"""

import streamlit as st
import streamlit.components.v1 as components
import html
from collections import Counter
from datetime import datetime
from utils.page_helper import setup_page, render_standard_footer
from components.ui import render_info_box, render_hero, render_pagination
from guidelines.tracker import (
    search_guidelines,
    get_recent_guidelines,
    check_guideline_updates,
    get_guideline_info,
    get_search_suggestions
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

# ========== ENHANCED CSS - Mobile-First Design ==========
st.markdown("""
<style>
/* Modern Medical Interface - Mobile-First (UpToDate/Medscape/BMJ Style) */
:root {
    --primary-color: #0066CC;
    --primary-hover: #0052a3;
    --text-primary: #212529;
    --text-secondary: #5f6368;
    --bg-card: #ffffff;
    --bg-page: #f8f9fa;
    --border-color: #e0e0e0;
    --shadow-sm: 0 2px 4px rgba(0,0,0,0.08);
    --shadow-md: 0 4px 12px rgba(0,0,0,0.12);
    --shadow-lg: 0 8px 24px rgba(0,0,0,0.16);
    --radius-sm: 8px;
    --radius-md: 12px;
    --radius-lg: 16px;
}

/* Sticky Search Bar */
.sticky-search-container {
    position: sticky;
    top: 0;
    z-index: 100;
    background: white;
    padding: 16px 0;
    margin: -16px 0 16px 0;
    border-bottom: 2px solid var(--border-color);
    box-shadow: var(--shadow-sm);
}

/* Enhanced Search Input */
.enhanced-search-input {
    width: 100%;
    padding: 12px 16px;
    font-size: 1rem;
    border: 2px solid var(--border-color);
    border-radius: var(--radius-md);
    transition: all 0.2s;
}

.enhanced-search-input:focus {
    border-color: var(--primary-color);
    outline: none;
    box-shadow: 0 0 0 3px rgba(0, 102, 204, 0.1);
}

/* Filter Chips */
.filter-chip {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 6px 12px;
    background: #f0f7ff;
    color: var(--primary-color);
    border: 1px solid #d2e3fc;
    border-radius: 20px;
    font-size: 0.85rem;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.2s;
    margin: 4px;
}

.filter-chip:hover {
    background: #e1effe;
    border-color: var(--primary-color);
}

.filter-chip.active {
    background: var(--primary-color);
    color: white;
    border-color: var(--primary-color);
}

.filter-chip-remove {
    margin-left: 4px;
    cursor: pointer;
    font-weight: bold;
}

/* Quick Filter Buttons */
.quick-filter-btn {
    padding: 8px 16px;
    margin: 4px;
    border-radius: var(--radius-sm);
    border: 1px solid var(--border-color);
    background: white;
    color: var(--text-primary);
    font-size: 0.9rem;
    cursor: pointer;
    transition: all 0.2s;
}

.quick-filter-btn:hover {
    background: #f5f5f5;
    border-color: var(--primary-color);
}

.quick-filter-btn.active {
    background: var(--primary-color);
    color: white;
    border-color: var(--primary-color);
}

/* Card Design - Mobile-First */
.guideline-card {
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-md);
    padding: 16px;
    margin-bottom: 16px;
    border-left: 4px solid var(--primary-color);
    transition: all 0.2s ease-in-out;
    box-shadow: var(--shadow-sm);
}

.guideline-card:hover {
    box-shadow: var(--shadow-md);
    transform: translateY(-2px);
    border-color: #b0c4de;
}

/* Mobile: Full width, Desktop: Grid */
@media (min-width: 768px) {
    .guideline-card {
        padding: 20px;
    }
}

/* Typography - Enhanced Hierarchy */
.guideline-title {
    font-family: 'Inter', -apple-system, sans-serif;
    color: var(--primary-color);
    font-size: 1.25rem;
    font-weight: 700;
    margin: 0 0 8px 0;
    line-height: 1.4;
}

@media (min-width: 768px) {
    .guideline-title {
        font-size: 1.5rem;
    }
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
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
}

.guideline-description.expanded {
    display: block;
    -webkit-line-clamp: unset;
}

/* Badges - Enhanced */
.badge {
    display: inline-flex;
    align-items: center;
    padding: 4px 10px;
    border-radius: 6px;
    font-size: 0.75rem;
    font-weight: 600;
    letter-spacing: 0.3px;
    white-space: nowrap;
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

.badge-high-impact {
    background: linear-gradient(135deg, #fff8e1 0%, #ffe082 100%);
    color: #b06000;
    border: 1px solid #ffcc02;
    font-weight: 700;
}

.badge-org {
    background-color: #f1f3f4;
    color: #3c4043;
    border: 1px solid #dadce0;
}

/* Year Indicator */
.year-indicator {
    display: inline-flex;
    align-items: center;
    padding: 2px 8px;
    border-radius: 4px;
    font-size: 0.75rem;
    font-weight: 600;
}

.year-indicator.recent {
    background: #e8f5e9;
    color: #2e7d32;
}

.year-indicator.updated {
    background: #fff3e0;
    color: #ef6c00;
}

.year-indicator.old {
    background: #ffebee;
    color: #c62828;
}

/* Clinical Pearl Box */
.pearl-box {
    background-color: #f8f9fa;
    border-radius: 6px;
    padding: 12px 16px;
    margin-top: 12px;
    border-left: 3px solid #fbbc04;
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

/* Action Buttons - Touch-Friendly */
.action-button {
    min-height: 44px;
    min-width: 44px;
    padding: 10px 16px;
    border-radius: var(--radius-sm);
    font-size: 0.9rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s;
    border: none;
    display: inline-flex;
    align-items: center;
    gap: 6px;
}

.action-link {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    color: var(--primary-color);
    font-size: 0.9rem;
    font-weight: 600;
    text-decoration: none;
    padding: 8px 12px;
    border-radius: var(--radius-sm);
    background-color: #f0f7ff;
    transition: background 0.2s;
    min-height: 44px;
}

.action-link:hover {
    background-color: #e1effe;
    text-decoration: none;
}

/* Mobile Navigation */
@media (max-width: 767px) {
    .guideline-card {
        padding: 12px;
    }
    
    .guideline-title {
        font-size: 1.1rem;
    }
    
    .sticky-search-container {
        padding: 12px 0;
    }
}

/* View Mode Tabs */
.view-mode-tabs {
    display: flex;
    gap: 8px;
    margin-bottom: 16px;
    border-bottom: 2px solid var(--border-color);
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
}

.view-mode-tab {
    padding: 12px 16px;
    border: none;
    background: transparent;
    color: var(--text-secondary);
    font-weight: 500;
    cursor: pointer;
    border-bottom: 2px solid transparent;
    margin-bottom: -2px;
    white-space: nowrap;
    transition: all 0.2s;
}

.view-mode-tab:hover {
    color: var(--primary-color);
}

.view-mode-tab.active {
    color: var(--primary-color);
    border-bottom-color: var(--primary-color);
    font-weight: 600;
}

/* Collapsible Sections */
.collapsible-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 12px;
    background: #f8f9fa;
    border-radius: var(--radius-sm);
    cursor: pointer;
    margin-bottom: 8px;
}

.collapsible-content {
    padding: 12px;
    background: white;
    border-radius: var(--radius-sm);
    margin-top: 8px;
}

/* Statistics Dashboard */
.stats-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    gap: 12px;
    margin-bottom: 24px;
}

.stat-card {
    background: white;
    padding: 16px;
    border-radius: var(--radius-md);
    border: 1px solid var(--border-color);
    text-align: center;
}

.stat-value {
    font-size: 1.5rem;
    font-weight: 700;
    color: var(--primary-color);
    margin-bottom: 4px;
}

.stat-label {
    font-size: 0.85rem;
    color: var(--text-secondary);
}

/* Filter Summary */
.filter-summary {
    padding: 12px 16px;
    background: #f0f7ff;
    border-radius: var(--radius-sm);
    margin-bottom: 16px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 8px;
}

/* Autocomplete Dropdown */
.autocomplete-dropdown {
    position: absolute;
    top: 100%;
    left: 0;
    right: 0;
    background: white;
    border: 1px solid var(--border-color);
    border-radius: var(--radius-sm);
    box-shadow: var(--shadow-md);
    max-height: 300px;
    overflow-y: auto;
    z-index: 1000;
    margin-top: 4px;
}

.autocomplete-item {
    padding: 12px 16px;
    cursor: pointer;
    border-bottom: 1px solid var(--border-color);
    transition: background 0.2s;
}

.autocomplete-item:hover {
    background: #f5f5f5;
}

.autocomplete-item:last-child {
    border-bottom: none;
}
</style>
""", unsafe_allow_html=True)

# ========== CACHING ==========
@st.cache_data(ttl=3600)
def get_cached_all_guidelines():
    """Get all guidelines with caching"""
    return get_all_guidelines()

@st.cache_data(ttl=3600)
def get_cached_years():
    """Get all years with caching"""
    return sorted(set([g.year for g in get_all_guidelines()]), reverse=True)

# ========== SESSION STATE INITIALIZATION ==========
if 'guideline_bookmarks' not in st.session_state:
    st.session_state['guideline_bookmarks'] = []

if 'guideline_recent_history' not in st.session_state:
    st.session_state['guideline_recent_history'] = []

if 'guideline_search_history' not in st.session_state:
    st.session_state['guideline_search_history'] = []

if 'guideline_notes' not in st.session_state:
    st.session_state['guideline_notes'] = {}

# ========== HELPER FUNCTIONS ==========

def add_to_bookmarks(guideline_id: str):
    """Add guideline to bookmarks"""
    if guideline_id not in st.session_state['guideline_bookmarks']:
        st.session_state['guideline_bookmarks'].append(guideline_id)

def remove_from_bookmarks(guideline_id: str):
    """Remove guideline from bookmarks"""
    if guideline_id in st.session_state['guideline_bookmarks']:
        st.session_state['guideline_bookmarks'].remove(guideline_id)

def is_bookmarked(guideline_id: str) -> bool:
    """Check if guideline is bookmarked"""
    return guideline_id in st.session_state['guideline_bookmarks']

def add_to_recent_history(guideline_id: str):
    """Add guideline to recent history (max 20 items)"""
    if guideline_id in st.session_state['guideline_recent_history']:
        st.session_state['guideline_recent_history'].remove(guideline_id)
    st.session_state['guideline_recent_history'].insert(0, guideline_id)
    # Keep only last 20
    st.session_state['guideline_recent_history'] = st.session_state['guideline_recent_history'][:20]

def get_bookmarked_guidelines():
    """Get list of bookmarked guidelines"""
    all_guidelines = get_cached_all_guidelines()
    bookmarked_ids = st.session_state['guideline_bookmarks']
    return [g for g in all_guidelines if g.id in bookmarked_ids]

def get_recent_guidelines_from_history():
    """Get recently viewed guidelines from history"""
    all_guidelines = get_cached_all_guidelines()
    history_ids = st.session_state['guideline_recent_history']
    # Create a dict for quick lookup
    guideline_dict = {g.id: g for g in all_guidelines}
    return [guideline_dict[gid] for gid in history_ids if gid in guideline_dict]

def get_guideline_note(guideline_id: str) -> str:
    """Get user note for a guideline"""
    return st.session_state.get('guideline_notes', {}).get(guideline_id, "")

def set_guideline_note(guideline_id: str, note: str):
    """Set user note for a guideline"""
    if 'guideline_notes' not in st.session_state:
        st.session_state['guideline_notes'] = {}
    if note:
        st.session_state['guideline_notes'][guideline_id] = note
    elif guideline_id in st.session_state['guideline_notes']:
        del st.session_state['guideline_notes'][guideline_id]

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
        "Gastroenterology": ("linear-gradient(135deg, #ffa726 0%, #fb8c00 100%)", "#ffa726"),
        "Oncology": ("linear-gradient(135deg, #ab47bc 0%, #8e24aa 100%)", "#ab47bc"),
        "Rheumatology": ("linear-gradient(135deg, #ef5350 0%, #e53935 100%)", "#ef5350"),
        "Obstetrics": ("linear-gradient(135deg, #ec407a 0%, #c2185b 100%)", "#ec407a"),
        "Dermatology": ("linear-gradient(135deg, #ff7043 0%, #f4511e 100%)", "#ff7043"),
        "Pain Management": ("linear-gradient(135deg, #78909c 0%, #546e7a 100%)", "#78909c"),
        "Urology": ("linear-gradient(135deg, #26a69a 0%, #00897b 100%)", "#26a69a"),
        "Trauma": ("linear-gradient(135deg, #ef5350 0%, #c62828 100%)", "#ef5350"),
        "Toxicology": ("linear-gradient(135deg, #ff6f00 0%, #e65100 100%)", "#ff6f00"),
        "Pediatrics": ("linear-gradient(135deg, #42a5f5 0%, #1e88e5 100%)", "#42a5f5"),
        "Hematology": ("linear-gradient(135deg, #e91e63 0%, #c2185b 100%)", "#e91e63"),
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
        "ASH": "#c62828",
        "ACG": "#1976d2",
        "NCCN": "#0d47a1",
        "ASCO": "#f57c00",
        "ACR": "#388e3c",
        "ACOG": "#0288d1",
        "RCOG": "#7b1fa2",
        "AAD": "#d32f2f",
        "APS": "#00796b",
        "AUA": "#455a64",
        "EAU": "#c62828",
        "ACS": "#1976d2",
        "BTF": "#0d47a1",
        "AANS": "#f57c00",
        "SCCM": "#388e3c",
        "AAP": "#0288d1",
        "AASLD": "#7b1fa2",
        "ATA": "#d32f2f",
        "AHS": "#00796b",
        "AAO": "#455a64",
    }
    for org_key, color in org_colors.items():
        if org_key in organization:
            return color
    return "#616161"


def get_year_indicator_class(year: int, current_year: int = 2025) -> tuple:
    """Determine year indicator class and color"""
    age = current_year - year
    if age <= 1:
        return ("recent", "#2e7d32", "Mới nhất")
    elif age <= 3:
        return ("updated", "#ef6c00", "Cập nhật")
    else:
        return ("old", "#c62828", "Cần cập nhật")


def render_sticky_search_bar():
    """Render sticky search bar with autocomplete and quick filters"""
    st.markdown('<div class="sticky-search-container">', unsafe_allow_html=True)
    
    # Initialize quick search term
    if 'guidelines_quick_search_term' not in st.session_state:
        st.session_state['guidelines_quick_search_term'] = ""
    
    # Get current search value
    current_search = st.session_state.get('guidelines_search_main', '')
    
    # If quick search was triggered, use that value
    if st.session_state.get('guidelines_quick_search_term'):
        current_search = st.session_state['guidelines_quick_search_term']
        # Clear quick search after using
        st.session_state['guidelines_quick_search_term'] = ""
    
    # Search input with autocomplete suggestions
    col1, col2 = st.columns([4, 1])
    with col1:
        search_query = st.text_input(
            "🔍 Tìm kiếm guidelines",
            value=current_search if current_search else "",
            placeholder="Nhập từ khóa: Heart Failure, Sepsis, AHA, ESC...",
            key="guidelines_search_main",
            help="Tìm kiếm theo tên bệnh, chuyên khoa, tổ chức, hoặc từ khóa bất kỳ"
        )
        
        # Show autocomplete suggestions if query is being typed
        if search_query and len(search_query) >= 2:
            suggestions = get_search_suggestions(search_query, limit=5)
            if suggestions:
                st.caption(f"💡 Gợi ý: {', '.join(suggestions[:3])}")
    
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🔄", help="Xóa tìm kiếm", use_container_width=True, key="clear_search_main"):
            if 'guidelines_search_main' in st.session_state:
                del st.session_state['guidelines_search_main']
            if 'guidelines_quick_search_term' in st.session_state:
                st.session_state['guidelines_quick_search_term'] = ""
            st.rerun()
    
    # Add search to history when search is performed
    if search_query and search_query not in st.session_state.get('guideline_search_history', []):
        st.session_state['guideline_search_history'].insert(0, search_query)
        # Keep only last 10 searches
        st.session_state['guideline_search_history'] = st.session_state['guideline_search_history'][:10]
    
    # Show search history if available and no current query
    if not search_query and st.session_state.get('guideline_search_history'):
        with st.expander("📜 Lịch sử tìm kiếm", expanded=False):
            for hist_term in st.session_state['guideline_search_history'][:5]:
                if st.button(f"🔍 {hist_term}", key=f"hist_{hist_term}", use_container_width=True):
                    st.session_state['guidelines_quick_search_term'] = hist_term
                    st.rerun()
    
    # Quick search chips
    if not search_query:
        quick_searches = ["AHA", "ESC", "IDSA", "Sepsis", "Heart Failure", "Diabetes", "COPD", "KDIGO"]
        st.markdown("**💡 Tìm kiếm nhanh:**")
        cols = st.columns(len(quick_searches))
        for idx, term in enumerate(quick_searches):
            with cols[idx]:
                if st.button(term, key=f"quick_{term}", use_container_width=True):
                    st.session_state['guidelines_quick_search_term'] = term
                    st.rerun()
    
    # Closing div tag no longer needed; removing avoids stray '</div>' rendering
    return search_query


def render_filter_chips(active_filters: dict):
    """Render active filter chips with remove functionality"""
    active_filter_items = {k: v for k, v in active_filters.items() if v and v != "Tất cả"}
    
    if not active_filter_items:
        return
    
    st.markdown("**Bộ lọc đang áp dụng:**")
    
    # Create columns for filter chips
    num_filters = len(active_filter_items)
    cols = st.columns(min(num_filters + 1, 6))  # Max 5 filters + clear all button
    
    col_idx = 0
    for filter_type, filter_value in active_filter_items.items():
        if col_idx < len(cols) - 1:
            with cols[col_idx]:
                # Map filter type to session state key
                filter_key_map = {
                    "Chuyên khoa": "guidelines_category_filter",
                    "Tổ chức": "guidelines_org_filter",
                    "Năm": "guidelines_year_filter",
                    "High Impact": "guidelines_high_impact_filter"
                }
                session_key = filter_key_map.get(filter_type)
                
                if st.button(f"❌ {filter_type}: {filter_value}", key=f"remove_{filter_type}_{col_idx}", use_container_width=True):
                    if session_key and session_key in st.session_state:
                        if filter_type == "High Impact":
                            st.session_state[session_key] = False
                        else:
                            st.session_state[session_key] = "Tất cả"
                    st.rerun()
            col_idx += 1
    
    # Clear all button in last column
    if col_idx < len(cols):
        with cols[col_idx]:
            if st.button("🗑️ Xóa tất cả", key="clear_all_filters", use_container_width=True):
                for filter_type in active_filter_items.keys():
                    filter_key_map = {
                        "Chuyên khoa": "guidelines_category_filter",
                        "Tổ chức": "guidelines_org_filter",
                        "Năm": "guidelines_year_filter",
                        "High Impact": "guidelines_high_impact_filter"
                    }
                    session_key = filter_key_map.get(filter_type)
                    if session_key and session_key in st.session_state:
                        if filter_type == "High Impact":
                            st.session_state[session_key] = False
                        else:
                            st.session_state[session_key] = "Tất cả"
                st.rerun()
    
    st.markdown("---")


def render_quick_filters():
    """Render quick filter buttons with better icons and styling"""
    st.markdown("**⚡ Bộ lọc nhanh:**")
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        if st.button("📅 2 năm gần đây", key="quick_last2y", use_container_width=True):
            st.session_state['guidelines_year_filter'] = "2023"
            st.rerun()
    
    with col2:
        if st.button("⭐ High Impact", key="quick_high_impact", use_container_width=True):
            # Filter for high impact guidelines
            st.session_state['guidelines_high_impact_filter'] = True
            st.rerun()
    
    with col3:
        if st.button("❤️ Tim mạch", key="quick_cardio", use_container_width=True):
            st.session_state['guidelines_category_filter'] = "Cardiology"
            st.rerun()
    
    with col4:
        if st.button("🦠 Nhiễm khuẩn", key="quick_infectious", use_container_width=True):
            st.session_state['guidelines_category_filter'] = "Infectious"
            st.rerun()
    
    with col5:
        if st.button("🫁 Hô hấp", key="quick_respiratory", use_container_width=True):
            st.session_state['guidelines_category_filter'] = "Respiratory"
            st.rerun()


def render_enhanced_guideline_card(guideline, index: int, is_mobile: bool = False):
    """Render guideline card using Streamlit native components with enhanced design"""
    gradient, border_color = get_category_color(guideline.category)
    org_color = get_org_color(guideline.organization)
    current_year = 2025
    year_class, year_color, year_label = get_year_indicator_class(guideline.year, current_year)
    
    # Container với border styling và hover effects
    border_color_hex = "#fbbc04" if guideline.is_high_impact else border_color
    card_id = f"guideline_card_{index}"
    st.markdown(f"""
    <div id="{card_id}" style="
        border-left: 4px solid {border_color_hex};
        border-top: 1px solid #e0e0e0;
        border-right: 1px solid #e0e0e0;
        border-bottom: 1px solid #e0e0e0;
        border-radius: 8px;
        padding: 20px;
        margin-bottom: 20px;
        background: white;
        box-shadow: 0 2px 4px rgba(0,0,0,0.08);
        transition: all 0.3s ease;
    ">""", unsafe_allow_html=True)
    
    # Add hover effect via CSS
    st.markdown(f"""
    <style>
        #{card_id}:hover {{
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            transform: translateY(-2px);
            border-left-color: {border_color_hex};
        }}
    </style>
    """, unsafe_allow_html=True)
    
    # Title with better hierarchy
    title_display = guideline.title_vn or guideline.title
    st.markdown(f"### {title_display}")
    
    # Metadata row with color-coded badges
    meta_col1, meta_col2, meta_col3, meta_col4 = st.columns([2.5, 1.2, 1.2, 1])
    
    with meta_col1:
        # Organization with color
        st.markdown(f'<span style="color: {org_color}; font-weight: 600;">{guideline.organization}</span> • <span style="color: #5f6368;">{guideline.year}</span>', unsafe_allow_html=True)
    
    with meta_col2:
        # Status badge with better styling
        if guideline.is_high_impact:
            st.markdown('<span style="background: linear-gradient(135deg, #fff8e1 0%, #ffe082 100%); padding: 4px 8px; border-radius: 4px; font-weight: 700; color: #b06000;">⭐ PRACTICE CHANGING</span>', unsafe_allow_html=True)
        elif guideline.year >= 2023:
            st.markdown('<span style="background: #e8f5e9; padding: 4px 8px; border-radius: 4px; font-weight: 600; color: #2e7d32;">🆕 NEW</span>', unsafe_allow_html=True)
        elif guideline.year >= 2020:
            st.markdown('<span style="background: #fff3e0; padding: 4px 8px; border-radius: 4px; font-weight: 600; color: #ef6c00;">🔄 UPDATED</span>', unsafe_allow_html=True)
    
    with meta_col3:
        # Category with color coding
        st.markdown(f'<span style="color: {border_color}; font-weight: 500; padding: 4px 8px; background: {border_color}20; border-radius: 4px;">📁 {guideline.category}</span>', unsafe_allow_html=True)
    
    with meta_col4:
        # Year indicator with color
        st.markdown(f'<span style="background: {year_color}20; color: {year_color}; padding: 4px 8px; border-radius: 4px; font-weight: 600;">📅 {year_label}</span>', unsafe_allow_html=True)
    
    # Description
    if guideline.description:
        with st.expander("📄 Mô tả", expanded=False):
            st.markdown(guideline.description)
    
    # Key Recommendations
    if guideline.key_recommendations:
        with st.expander("💡 Key Recommendations", expanded=False):
            for rec in guideline.key_recommendations:
                st.markdown(f"- {rec}")
    
    # Actions row
    action_cols = st.columns([1, 1, 1, 1])
    col_idx = 0
    
    # Bookmark button
    with action_cols[col_idx]:
        is_booked = is_bookmarked(guideline.id)
        bookmark_label = "⭐ Đã lưu" if is_booked else "⭐ Lưu"
        button_type = "primary" if is_booked else "secondary"
        if st.button(bookmark_label, key=f"bookmark_{index}", use_container_width=True, type=button_type):
            if is_booked:
                remove_from_bookmarks(guideline.id)
            else:
                add_to_bookmarks(guideline.id)
            st.rerun()
    col_idx += 1
    
    # Protocol link
    if guideline.related_protocol:
        with action_cols[col_idx]:
            if st.button("📋 Protocol", key=f"proto_btn_{index}", use_container_width=True, type="primary"):
                st.session_state['protocol_specialty'] = guideline.category
                st.session_state['protocol_to_open'] = guideline.related_protocol
                st.switch_page("pages/04_📋_Protocols.py")
        col_idx += 1
    
    # Related tools
    if guideline.related_tools:
        for idx_tool, tool in enumerate(guideline.related_tools[:1]):  # Show first tool only
            with action_cols[col_idx]:
                if st.button(f"🧮 {tool['name']}", key=f"tool_btn_{index}_{idx_tool}", use_container_width=True):
                    st.switch_page("pages/01_📊_Scores.py")
            col_idx += 1
    
    # External link
    if guideline.url:
        with action_cols[col_idx]:
            st.markdown(f'<a href="{guideline.url}" target="_blank" style="color: #0066CC; text-decoration: none; font-weight: 600;">🔗 Xem gốc</a>', unsafe_allow_html=True)
    
    # Additional features row
    feature_cols = st.columns([1, 1, 1, 1])
    feat_idx = 0
    
    # Compare versions button
    from guidelines.tracker import compare_guideline_versions
    versions = compare_guideline_versions(guideline.id)
    if versions and versions.get('total_versions', 0) > 1:
        with feature_cols[feat_idx]:
            if st.button("📊 So sánh", key=f"compare_{index}", use_container_width=True):
                st.session_state[f'show_compare_{guideline.id}'] = True
                st.rerun()
        feat_idx += 1
        
        # Show comparison if requested
        if st.session_state.get(f'show_compare_{guideline.id}', False):
            with st.expander("📊 So sánh các phiên bản", expanded=True):
                st.markdown(f"**Phiên bản mới nhất:** {versions['latest'].year}")
                if versions.get('previous'):
                    st.markdown("**Phiên bản trước:**")
                    for prev in versions['previous']:
                        st.markdown(f"- {prev.year}")
                if st.button("Đóng", key=f"close_compare_{index}"):
                    st.session_state[f'show_compare_{guideline.id}'] = False
                    st.rerun()
    
    # User notes
    with feature_cols[feat_idx]:
        current_note = get_guideline_note(guideline.id)
        if st.button("📝 Ghi chú" + (" ✓" if current_note else ""), key=f"note_btn_{index}", use_container_width=True):
            st.session_state[f'show_note_{guideline.id}'] = True
            st.rerun()
    feat_idx += 1
    
    # Show note editor if requested
    if st.session_state.get(f'show_note_{guideline.id}', False):
        current_note = get_guideline_note(guideline.id)
        new_note = st.text_area("Ghi chú của bạn:", value=current_note, key=f"note_input_{index}", height=100)
        note_col1, note_col2 = st.columns([1, 1])
        with note_col1:
            if st.button("💾 Lưu", key=f"save_note_{index}"):
                set_guideline_note(guideline.id, new_note)
                st.session_state[f'show_note_{guideline.id}'] = False
                st.rerun()
        with note_col2:
            if st.button("❌ Đóng", key=f"close_note_{index}"):
                st.session_state[f'show_note_{guideline.id}'] = False
                st.rerun()
    
    # Export button
    with feature_cols[feat_idx]:
        if st.button("📥 Export", key=f"export_{index}", use_container_width=True):
            # Create export data
            import json
            export_data = {
                "title": guideline.title_vn or guideline.title,
                "organization": guideline.organization,
                "year": guideline.year,
                "category": guideline.category,
                "description": guideline.description,
                "key_recommendations": guideline.key_recommendations,
                "url": guideline.url
            }
            st.download_button(
                label="⬇️ Tải JSON",
                data=json.dumps(export_data, indent=2, ensure_ascii=False),
                file_name=f"guideline_{guideline.id}.json",
                mime="application/json",
                key=f"download_{index}"
            )
    feat_idx += 1
    
    # Share link (simplified - just show copy button)
    with feature_cols[feat_idx]:
        if st.button("🔗 Share", key=f"share_{index}", use_container_width=True):
            st.session_state[f'share_url_{guideline.id}'] = f"?guideline={guideline.id}"
            st.info(f"Link: {st.session_state.get('_stcore_host', '')}/Guidelines_Tracker?guideline={guideline.id}")
    
    # Divider for next card
    st.markdown("---")


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
    
    for idx, guideline in enumerate(high_impact[:5]):  # Limit to 5
        render_enhanced_guideline_card(guideline, f"feat_{idx}")


def render_statistics_dashboard(guidelines):
    """Hiển thị dashboard thống kê"""
    total = len(guidelines)
    years = [g.year for g in guidelines]
    recent_count = len([y for y in years if y >= 2023])
    high_impact_count = len([g for g in guidelines if getattr(g, 'is_high_impact', False)])
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Tổng số", total)
    with col2:
        st.metric("🆕 Mới nhất (≥2023)", recent_count)
    with col3:
        st.metric("⭐ High Impact", high_impact_count)
    with col4:
        st.metric("🏥 Chuyên khoa", len(set(g.category for g in guidelines)))


# ========== JAVASCRIPT FOR INTERACTIVITY ==========
st.markdown("""
<script>
function toggleDescription(id) {
    const elem = document.getElementById(id);
    if (elem.classList.contains('expanded')) {
        elem.classList.remove('expanded');
        elem.previousElementSibling.textContent = 'Đọc thêm...';
    } else {
        elem.classList.add('expanded');
        elem.previousElementSibling.textContent = 'Thu gọn';
    }
}

function togglePearl(id) {
    const elem = document.getElementById(id);
    const btn = elem.nextElementSibling;
    if (elem.style.display === 'none' || !elem.style.display) {
        elem.style.display = 'block';
        btn.textContent = '💡 Ẩn Key Recommendations';
    } else {
        elem.style.display = 'none';
        btn.textContent = '💡 Xem Key Recommendations';
    }
}

function removeFilter(filterType) {
    // This would need to be handled server-side in Streamlit
    console.log('Remove filter:', filterType);
}
</script>
""", unsafe_allow_html=True)

# ========== SIDEBAR (Simplified for Mobile) ==========
with st.sidebar:
    st.header("📋 Theo dõi Guidelines")
    
    # Personalization
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
    st.session_state['my_specialties'] = my_specialties
    
    st.markdown("---")
    
    # View Mode - Tabs style
    view_modes = ["Của tôi", "Tất cả", "Gần đây", "Cần cập nhật", "⭐ Đã lưu", "📜 Lịch sử", "Tìm kiếm"]
    default_index = 0 if my_specialties else 1
    
    view_mode = st.radio(
        "Chế độ xem:",
        view_modes,
        index=default_index,
        key="guidelines_view_mode"
    )
    
    # Show bookmark count
    bookmark_count = len(st.session_state.get('guideline_bookmarks', []))
    if bookmark_count > 0:
        st.caption(f"⭐ {bookmark_count} guidelines đã lưu")
    
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

# Compact Hero
render_hero(
    title="Clinical Guidelines",
    subtitle="📋 Theo dõi, xem và tìm kiếm hướng dẫn lâm sàng",
    description="Theo dõi và cập nhật các hướng dẫn thực hành lâm sàng từ các tổ chức uy tín",
    icon="📋",
    gradient=("#667eea", "#764ba2")
)

# Tabs for different views
tab_tracker, tab_viewer, tab_news = st.tabs(["📋 Tracker", "📖 Viewer", "📰 News"])

# Clear redirect flag if set
if st.session_state.get('guidelines_open_viewer_tab', False):
    st.session_state['guidelines_open_viewer_tab'] = False

# ========== TAB 1: TRACKER ==========
with tab_tracker:
    # Sticky Search Bar
    search_query = render_sticky_search_bar()

    # Quick Filters
    render_quick_filters()

    st.markdown("---")

# Initialize filter variables
category_filter = None
org_filter = None
year_filter = None
sort_by = None

# Filters (moved to top, collapsible)
if view_mode == "Tất cả":
    with st.expander("🔍 Bộ lọc nâng cao", expanded=False):
        col1, col2 = st.columns(2)
        with col1:
            category_filter = st.selectbox(
                "Chuyên khoa:",
                ["Tất cả"] + get_category_list(),
                key="guidelines_category_filter"
            )
            
            all_guidelines = get_all_guidelines()
            years = sorted(set(g.year for g in all_guidelines), reverse=True)
            year_filter = st.selectbox(
                "Năm:",
                ["Tất cả"] + [str(year) for year in years],
                key="guidelines_year_filter"
            )
        
        with col2:
            org_filter = st.selectbox(
                "Tổ chức:",
                ["Tất cả"] + get_organization_list(),
                key="guidelines_org_filter"
            )
            
            sort_by = st.selectbox(
                "Sắp xếp:",
                ["Năm (mới nhất)", "Năm (cũ nhất)", "Tổ chức", "Chuyên khoa"],
                key="guidelines_sort"
            )
    
    # Active filter chips
    active_filters = {
        "Chuyên khoa": category_filter,
        "Tổ chức": org_filter,
        "Năm": year_filter
    }
    # Add high impact filter if active
    if st.session_state.get('guidelines_high_impact_filter', False):
        active_filters["High Impact"] = "Có"
    render_filter_chips(active_filters)

# Display based on view mode
if view_mode == "Của tôi":
    st.markdown("### 👤 Dành cho bạn")
    
    if not my_specialties:
        render_info_box("""
        **👋 Chào mừng bạn!**
        
        Để xem các guidelines phù hợp, hãy chọn **Chuyên khoa quan tâm** ở thanh bên trái.
        """, type="info")
        
        recent = get_recent_guidelines(limit=5)
        render_featured_updates(recent)
        
        st.markdown("#### 🆕 Có thể bạn quan tâm (Mới nhất)")
        for idx, guideline in enumerate(recent):
            if not getattr(guideline, 'is_high_impact', False):
                render_enhanced_guideline_card(guideline, idx)
    else:
        all_guidelines = get_cached_all_guidelines()
        personal_guidelines = [
            g for g in all_guidelines 
            if g.category in my_specialties
        ]
        personal_guidelines.sort(key=lambda x: x.year, reverse=True)
        
        render_featured_updates(personal_guidelines)
        
        if personal_guidelines:
            render_statistics_dashboard(personal_guidelines)
            st.markdown("---")
            
            items_per_page = 20
            start_idx, end_idx, _, _ = render_pagination(
                total_items=len(personal_guidelines),
                items_per_page=items_per_page,
                page_key="guidelines_page_my",
                show_info=True
            )
            
            for idx, guideline in enumerate(personal_guidelines[start_idx:end_idx]):
                render_enhanced_guideline_card(guideline, start_idx + idx)
                # Track view for history
                add_to_recent_history(guideline.id)
        else:
            st.info(f"Chưa có guideline nào cho các chuyên khoa: {', '.join(my_specialties)}")

elif view_mode == "Tất cả":
    st.markdown("### 📚 Tất cả Guidelines")
    
    # Show featured if no filters
    if (st.session_state.get('guidelines_category_filter', 'Tất cả') == 'Tất cả' and
        st.session_state.get('guidelines_org_filter', 'Tất cả') == 'Tất cả'):
        render_featured_updates(get_cached_all_guidelines())
        st.markdown("---")
    
    # Apply filters
    category = None if category_filter == "Tất cả" else category_filter
    org = None if org_filter == "Tất cả" else org_filter
    year = None if year_filter == "Tất cả" else int(year_filter) if year_filter else None
    high_impact_only = st.session_state.get('guidelines_high_impact_filter', False)
    
    guidelines = get_cached_all_guidelines()
    
    # Apply filters
    if category:
        guidelines = [g for g in guidelines if g.category == category]
    if org:
        guidelines = [g for g in guidelines if org in g.organization]
    if year:
        guidelines = [g for g in guidelines if g.year == year]
    if high_impact_only:
        guidelines = [g for g in guidelines if getattr(g, 'is_high_impact', False)]
    
    # Sort
    if sort_by == "Năm (mới nhất)":
        guidelines.sort(key=lambda x: x.year, reverse=True)
    elif sort_by == "Năm (cũ nhất)":
        guidelines.sort(key=lambda x: x.year)
    elif sort_by == "Tổ chức":
        guidelines.sort(key=lambda x: x.organization)
    elif sort_by == "Chuyên khoa":
        guidelines.sort(key=lambda x: x.category)
    
    if guidelines:
        render_statistics_dashboard(guidelines)
        st.markdown("---")
        st.success(f"✅ Tìm thấy {len(guidelines)} guidelines")
        
        items_per_page = 20
        start_idx, end_idx, _, _ = render_pagination(
            total_items=len(guidelines),
            items_per_page=items_per_page,
            page_key="guidelines_page_all",
            show_info=True
        )
        
        for idx, guideline in enumerate(guidelines[start_idx:end_idx]):
            render_enhanced_guideline_card(guideline, start_idx + idx)
            # Track view for history
            add_to_recent_history(guideline.id)
    else:
        st.warning("Không tìm thấy guidelines với bộ lọc đã chọn.")

elif view_mode == "Gần đây":
    st.markdown("### 🆕 Guidelines Gần Đây")
    
    recent = get_recent_guidelines(limit=100, min_year=2020)
    
    if recent:
        render_statistics_dashboard(recent)
        st.markdown("---")
        st.success(f"✅ Tìm thấy {len(recent)} guidelines gần đây (từ 2020)")
        
        items_per_page = 20
        start_idx, end_idx, _, _ = render_pagination(
            total_items=len(recent),
            items_per_page=items_per_page,
            page_key="guidelines_page_recent",
            show_info=True
        )
        
        for idx, guideline in enumerate(recent[start_idx:end_idx]):
            render_enhanced_guideline_card(guideline, start_idx + idx)
            # Track view for history
            add_to_recent_history(guideline.id)
    else:
        st.warning("Không tìm thấy guidelines gần đây.")

elif view_mode == "Cần cập nhật":
    st.markdown("### ⚠️ Guidelines cần cập nhật")
    st.info("Guidelines cũ hơn 2020 có thể cần được cập nhật. Vui lòng kiểm tra phiên bản mới nhất.")
    
    old_guidelines = check_guideline_updates(year_threshold=2020)
    old_guidelines.sort(key=lambda x: x.year)
    
    if old_guidelines:
        render_statistics_dashboard(old_guidelines)
        st.markdown("---")
        st.warning(f"⚠️ Tìm thấy {len(old_guidelines)} guidelines có thể cần cập nhật")
        
        items_per_page = 20
        start_idx, end_idx, _, _ = render_pagination(
            total_items=len(old_guidelines),
            items_per_page=items_per_page,
            page_key="guidelines_page_old",
            show_info=True
        )
        
        for idx, guideline in enumerate(old_guidelines[start_idx:end_idx]):
            render_enhanced_guideline_card(guideline, start_idx + idx)
            # Track view for history
            add_to_recent_history(guideline.id)
    else:
        st.success("✅ Tất cả guidelines đều gần đây (từ 2020 trở lên).")

elif view_mode == "⭐ Đã lưu":
    st.markdown("### ⭐ Guidelines Đã Lưu")
    
    bookmarked = get_bookmarked_guidelines()
    
    if bookmarked:
        render_statistics_dashboard(bookmarked)
        st.markdown("---")
        st.success(f"✅ Bạn đã lưu {len(bookmarked)} guidelines")
        
        items_per_page = 20
        start_idx, end_idx, _, _ = render_pagination(
            total_items=len(bookmarked),
            items_per_page=items_per_page,
            page_key="guidelines_page_bookmarked",
            show_info=True
        )
        
        for idx, guideline in enumerate(bookmarked[start_idx:end_idx]):
            render_enhanced_guideline_card(guideline, f"bookmarked_{start_idx + idx}")
            # Track view for history
            add_to_recent_history(guideline.id)
    else:
        st.info("💡 Bạn chưa lưu guideline nào. Click nút '⭐ Lưu' trên bất kỳ guideline nào để lưu.")

elif view_mode == "📜 Lịch sử":
    st.markdown("### 📜 Lịch Sử Xem Gần Đây")
    
    recent_history = get_recent_guidelines_from_history()
    
    if recent_history:
        render_statistics_dashboard(recent_history)
        st.markdown("---")
        st.success(f"✅ {len(recent_history)} guidelines đã xem gần đây")
        
        items_per_page = 20
        start_idx, end_idx, _, _ = render_pagination(
            total_items=len(recent_history),
            items_per_page=items_per_page,
            page_key="guidelines_page_history",
            show_info=True
        )
        
        for idx, guideline in enumerate(recent_history[start_idx:end_idx]):
            render_enhanced_guideline_card(guideline, f"history_{start_idx + idx}")
    else:
        st.info("💡 Chưa có lịch sử xem. Các guideline bạn xem sẽ được lưu ở đây.")

else:  # Tìm kiếm
    st.markdown("### 🔍 Tìm kiếm Guidelines")
    
    if search_query:
        results = search_guidelines(search_query)
        results.sort(key=lambda x: x.year, reverse=True)
        
        if results:
            render_statistics_dashboard(results)
            st.markdown("---")
            st.success(f"✅ Tìm thấy {len(results)} kết quả cho '{search_query}'")
            
            items_per_page = 20
            start_idx, end_idx, _, _ = render_pagination(
                total_items=len(results),
                items_per_page=items_per_page,
                page_key="guidelines_page_search",
                show_info=True
            )
            
            for idx, guideline in enumerate(results[start_idx:end_idx]):
                render_enhanced_guideline_card(guideline, start_idx + idx)
                # Track view for history
                add_to_recent_history(guideline.id)
        else:
            st.warning("Không tìm thấy kết quả. Vui lòng thử lại với từ khóa khác.")
            st.info("💡 Gợi ý: Thử tìm kiếm theo tên bệnh, chuyên khoa, hoặc tên tổ chức (VD: AHA, ESC, IDSA)")
    else:
        st.info("💡 Nhập từ khóa vào thanh tìm kiếm phía trên để bắt đầu")

    # Additional information
    st.markdown("---")
    st.markdown("### 📚 Thông tin về Guidelines")
    st.markdown("""
    **Các tổ chức guidelines chính:**

    1. **AHA/ACC** - American Heart Association / American College of Cardiology
    2. **ESC** - European Society of Cardiology
    3. **IDSA** - Infectious Diseases Society of America
    4. **KDIGO** - Kidney Disease: Improving Global Outcomes
    5. **GOLD** - Global Initiative for Chronic Obstructive Lung Disease
    6. **GINA** - Global Initiative for Asthma
    7. **SSC** - Surviving Sepsis Campaign
    8. **ADA** - American Diabetes Association

    **Lưu ý:** Guidelines được cập nhật thường xuyên. Luôn tham khảo phiên bản mới nhất từ website chính thức.
    """)

# ========== TAB 2: VIEWER ==========
with tab_viewer:
    # Import viewer components
    try:
        from components.guideline_viewer import (
            render_guideline_viewer,
            render_guideline_filters,
            render_guideline_search_bar,
            render_guideline_statistics
        )
        from components.decision_tree import render_guideline_decision_tree
        
        # Initialize session state for viewer
        if 'guideline_viewer_show_details' not in st.session_state:
            st.session_state.guideline_viewer_show_details = False
        
        # Statistics Section
        render_guideline_statistics()
        
        st.markdown("---")
        
        # Filters - Use sidebar filters
        try:
            filters = render_guideline_filters()
        except Exception as e:
            # Fallback to default filters if sidebar filters fail
            st.warning(f"Không thể load filters từ sidebar: {e}")
            filters = {
                "category": st.session_state.get("guideline_category_filter", "All"),
                "organization": st.session_state.get("guideline_organization_filter", "All"),
                "year_min": st.session_state.get("guideline_year_min"),
                "year_max": st.session_state.get("guideline_year_max"),
                "high_impact_only": st.session_state.get("guideline_high_impact", False)
            }
        
        st.markdown("---")
        
        # Search Bar
        viewer_search_query = render_guideline_search_bar()
        
        st.markdown("---")
        
        # Main Content: Guideline Viewer
        render_guideline_viewer(
            search_query=viewer_search_query,
            category_filter=filters.get("category", "All"),
            organization_filter=filters.get("organization", "All"),
            year_min=filters.get("year_min"),
            year_max=filters.get("year_max"),
            show_details=st.session_state.guideline_viewer_show_details
        )
        
        st.markdown("---")
        
        # Decision Trees Section
        st.markdown("### 🌳 Clinical Decision Trees")
        st.info("💡 Decision trees sẽ được hiển thị khi xem chi tiết guideline có sẵn decision tree.")
        
        # Example: Show decision tree for heart failure guidelines
        example_guideline_id = "acc_aha_heart_failure_2022"
        if st.checkbox("Hiển thị ví dụ Decision Tree (Heart Failure)", key="show_example_tree"):
            render_guideline_decision_tree(example_guideline_id)
            
    except ImportError as e:
        st.error(f"Lỗi import viewer components: {e}")
        st.info("💡 Vui lòng kiểm tra lại các components cần thiết.")

# ========== TAB 3: NEWS ==========
with tab_news:
    # Medical News (integrated from Medical News page)
    st.markdown("### 📰 Tin tức Y khoa")
    st.caption("Cập nhật từ Bộ Y Tế, WHO và các tổ chức uy tín")
    
    try:
        from components.news_logic import get_medical_news
        
        with st.spinner("Đang tải tin tức..."):
            news_data = get_medical_news()
        
        if news_data:
            for item in news_data[:10]:  # Show top 10
                with st.expander(f"📰 {item.get('title', 'Không có tiêu đề')}"):
                    st.markdown(f"**Nguồn:** {item.get('source', 'N/A')}")
                    st.markdown(f"**Ngày:** {item.get('date', 'N/A')}")
                    st.markdown(item.get('summary', 'Không có tóm tắt'))
                    if item.get('link'):
                        st.markdown(f"[Đọc thêm →]({item['link']})")
        else:
            st.info("Không có tin tức mới.")
    except ImportError:
        st.warning("Component news_logic không khả dụng.")
        if st.button("Mở Medical News", use_container_width=True):
            st.switch_page("pages/10_📰_Medical_News.py")
    except Exception as e:
        st.error(f"Lỗi tải tin tức: {e}")
        if st.button("Mở Medical News", use_container_width=True):
            st.switch_page("pages/10_📰_Medical_News.py")

# Footer
render_standard_footer(disclaimer=True)
