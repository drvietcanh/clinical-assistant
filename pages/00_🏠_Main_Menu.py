"""
Main Menu - Enhanced Homepage
Modern, optimized homepage with search, favorites, stats, quick actions, and more
"""

import streamlit as st
from utils.page_helper import setup_page, render_standard_footer
from components.main_menu_styles import inject_main_menu_styles

# Import new components
from components.main_menu_hero import render_hero_section, render_announcement_banner, render_quick_stats_summary
from components.global_search import render_global_search_bar, render_search_results
from components.main_menu_quick_actions import render_quick_actions_widget
from components.main_menu_category_browser import render_category_browser
from components.main_menu_stats import render_main_menu_stats
from components.main_menu_recommendations import render_recommendations
from components.main_menu_news import render_news_updates_section
from components.favorites import render_favorites
from components.recently_used import render_recently_used
from components.quick_access import render_quick_access_cards

# Standard page setup
setup_page(
    page_title="Main Menu",
    page_icon="🏠",
    description="Trang chủ với tìm kiếm, yêu thích, gần đây, và truy cập nhanh"
)

# Initialize session state
if 'global_search_query' not in st.session_state:
    st.session_state.global_search_query = ''
if 'favorites' not in st.session_state:
    st.session_state.favorites = []
if 'recently_used' not in st.session_state:
    st.session_state.recently_used = []
if 'usage_stats' not in st.session_state:
    st.session_state.usage_stats = {
        'total_calculations': 0,
        'calculations_by_category': {},
        'calculations_by_calculator': {},
        'most_used_calculator': None,
        'calculations_by_date': [],
    }

# Custom CSS (centralized in component)
inject_main_menu_styles()

# ===== HERO SECTION =====
render_hero_section()

# Announcement banner (dismissible)
render_announcement_banner()

st.markdown("---")

# ===== ENHANCED GLOBAL SEARCH =====
st.markdown("### 🔍 Tìm kiếm toàn bộ calculators")
search_query = render_global_search_bar(
    placeholder="Tìm kiếm thuốc, thang điểm, guideline... (Ctrl+K)",
    show_category_filters=True
)

# Show search results if query exists
if search_query and len(search_query.strip()) >= 2:
    render_search_results(search_query, max_results_per_category=6)

st.markdown("---")

# ===== QUICK ACTIONS WIDGET =====
render_quick_actions_widget(max_items=6)

st.markdown("---")

# ===== QUICK STATS SUMMARY =====
render_quick_stats_summary()

st.markdown("---")

# ===== TABS FOR ORGANIZED CONTENT =====
tab1, tab2, tab3, tab4 = st.tabs([
    "⭐ Yêu thích & Gần đây",
    "📊 Thống kê",
    "💡 Gợi ý",
    "📰 Cập nhật"
])

with tab1:
    # Favorites & Recently Used
    col_left, col_right = st.columns(2)
    
    with col_left:
        render_favorites(max_items=6, show_empty_state=True)
    
    with col_right:
        render_recently_used(max_items=6, show_empty_state=True)
    
    st.markdown("---")
    
    # Quick Access Cards
    st.markdown("### ⚡ Calculator phổ biến")
    render_quick_access_cards(max_items=8, layout="grid")

with tab2:
    # Modern Stats Dashboard
    render_main_menu_stats()

with tab3:
    # Personalized Recommendations
    render_recommendations(max_items=6)
    
    st.markdown("---")
    
    # Category Browser
    render_category_browser()

with tab4:
    # News & Updates
    render_news_updates_section()

st.markdown("---")


# Footer
render_standard_footer()
