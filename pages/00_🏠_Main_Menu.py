"""
Main Menu - Enhanced Homepage
Unified entry point with search, favorites, recently used, quick access, and stats
"""

import streamlit as st
from utils.page_helper import setup_page, render_standard_footer
from components.ui import render_info_box, render_hero
from components.main_menu_styles import inject_main_menu_styles
from utils.cache_helpers import compute_usage_stats_snapshot, get_popular_calculators

# Import components
from components.global_search import render_global_search_modal, search_calculators
from components.favorites import render_favorites
from components.recently_used import render_recently_used
from components.quick_access import render_quick_access_menu
from config.calculators import ALL_CALCULATORS

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
        'most_used_calculator': None,
    }

# Custom CSS (centralized in component)
inject_main_menu_styles()

# Hero Section (simplified to avoid raw HTML showing)
st.markdown("### 🏥 Clinical Assistant")
st.caption("Công cụ hỗ trợ lâm sàng toàn diện – Tìm kiếm, tính toán, và truy cập nhanh các công cụ lâm sàng")
st.markdown("---")

# Section 1: Global Search
st.markdown("### 🔍 Tìm kiếm toàn bộ calculators")
search_query = st.text_input(
    "Nhập tên calculator để tìm kiếm...",
    value=st.session_state.global_search_query,
    key="main_menu_search",
    placeholder="Ví dụ: ASCVD, CHA2DS2-VASc, SOFA..."
)

# Render global search modal (for keyboard shortcut)
render_global_search_modal()

# Search results with lightweight debouncing & result caching
if search_query:
    st.session_state.global_search_query = search_query

    if 'last_main_menu_search_query' not in st.session_state:
        st.session_state.last_main_menu_search_query = ""
    if 'main_menu_search_results' not in st.session_state:
        st.session_state.main_menu_search_results = []

    if (
        search_query != st.session_state.last_main_menu_search_query
        and len(search_query.strip()) >= 2
    ):
        results = search_calculators(search_query, max_results=10)
        st.session_state.last_main_menu_search_query = search_query
        st.session_state.main_menu_search_results = results
    else:
        results = st.session_state.main_menu_search_results

    if results:
        st.markdown(f"**Tìm thấy {len(results)} kết quả:**")
        for result in results:
            with st.container():
                col1, col2 = st.columns([1, 4])
                with col1:
                    st.markdown(f"### {result.get('icon', '📊')}")
                with col2:
                    st.markdown(f"**{result['name']}**")
                    st.caption(f"{result.get('category', '')} • {result.get('page', 'Scores')}")
                    if st.button(f"Mở {result['name']}", key=f"open_{result['id']}"):
                        # Navigate to calculator
                        page_map = {
                            'Scores': 'pages/01_📊_Scores.py',
                            'Drugs': 'pages/07_💊_Drug_Database.py',
                            'Protocols': 'pages/04_📋_Protocols.py'
                        }
                        target_page = page_map.get(result.get('page', 'Scores'), 'pages/01_📊_Scores.py')
                        st.switch_page(target_page)
                st.markdown("---")
    else:
        st.info("Không tìm thấy kết quả (cần tối thiểu 2 ký tự). Thử từ khóa khác.")

st.markdown("---")

# Section 2: Stats Dashboard
st.markdown("### 📊 Thống kê sử dụng")
usage_stats = st.session_state.usage_stats
categories_dict = usage_stats.get('calculations_by_category', {})
stats_snapshot = compute_usage_stats_snapshot(
    usage_stats.get('total_calculations', 0),
    usage_stats.get('most_used_calculator'),
    tuple(categories_dict.items()),
)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="stats-card">
        <h3>📈 Tổng số lần tính</h3>
        <p style="font-size: 24px; font-weight: bold;">{}</p>
    </div>
    """.format(stats_snapshot["total_calculations"]), unsafe_allow_html=True)

with col2:
    most_used = stats_snapshot["most_used_id"]
    if most_used and most_used in ALL_CALCULATORS:
        calc_name = ALL_CALCULATORS[most_used].get('name', 'N/A')
    else:
        calc_name = "Chưa có"
    st.markdown("""
    <div class="stats-card">
        <h3>⭐ Calculator dùng nhiều nhất</h3>
        <p style="font-size: 18px;">{}</p>
    </div>
    """.format(calc_name), unsafe_allow_html=True)

with col3:
    top_category = stats_snapshot["top_category"]
    st.markdown("""
    <div class="stats-card">
        <h3>📚 Chuyên khoa phổ biến</h3>
        <p style="font-size: 18px;">{}</p>
    </div>
    """.format(top_category), unsafe_allow_html=True)

st.markdown("---")

# Section 3: Favorites & Recently Used (lazy-ish via mode switch)
view_mode = st.radio(
    "Chọn danh sách hiển thị:",
    ["⭐ Yêu thích", "🕐 Gần đây"],
    horizontal=True,
    key="main_menu_fav_recent_mode",
)

with st.container():
    if view_mode == "⭐ Yêu thích":
        st.markdown("### ⭐ Yêu thích")
        render_favorites(max_items=5)
    else:
        st.markdown("### 🕐 Sử dụng gần đây")
        render_recently_used(max_items=5)

st.markdown("---")

# Section 4: Quick Access - Most Popular
st.markdown("### ⚡ Truy cập nhanh - Calculator phổ biến")

# Get most popular calculators (based on usage stats or default) via cached helper
default_popular = (
    'ascvd', 'cha2ds2vasc', 'sofa', 'gcs', 'qsofa',
    'hasbled', 'heart', 'timi', 'grace',
)
popular_calculators = get_popular_calculators(default_popular)

cols = st.columns(min(4, len(popular_calculators)))
for idx, calc_id in enumerate(popular_calculators[:8]):
    if calc_id in ALL_CALCULATORS:
        calc_info = ALL_CALCULATORS[calc_id]
        with cols[idx % 4]:
            if st.button(
                f"{calc_info.get('icon', '📊')} {calc_info['name']}",
                use_container_width=True,
                key=f"quick_{calc_id}"
            ):
                st.switch_page("pages/01_📊_Scores.py")

st.markdown("---")

# Section 5: Browse by Category (Updated with new navigation structure)
st.markdown("### 📚 Duyệt theo nhóm chính")

# Use new navigation categories
try:
    from config.navigation_config import get_all_categories
    nav_categories = get_all_categories()
    
    # Display main categories (skip home_search as it's the current page)
    main_categories = {
        "drugs_dosing": {"icon": "💊", "title": "Thuốc & Liều dùng", "page": "pages/07_💊_Drug_Database.py"},
        "calculators_scores": {"icon": "📊", "title": "Tính toán & Thang điểm", "page": "pages/01_📊_Scores.py"},
        "critical_care_protocols": {"icon": "🫁", "title": "Hồi sức & Phác đồ", "page": "pages/09_🫁_Critical_Care.py"},
        "diagnosis_reference": {"icon": "🩺", "title": "Chẩn đoán & Tham khảo", "page": "pages/06_🩺_Diagnosis.py"},
        "support_tools": {"icon": "🧭", "title": "Hỗ trợ & Công cụ", "page": "pages/10_🧭_Decision_Support.py"},
    }
    
    cols = st.columns(3)
    for idx, (cat_id, cat_info) in enumerate(main_categories.items()):
        with cols[idx % 3]:
            if st.button(
                f"{cat_info['icon']} {cat_info['title']}",
                key=f"cat_{cat_id}",
                use_container_width=True
            ):
                st.switch_page(cat_info['page'])
except ImportError:
    # Fallback to old categories
    categories = {
        "❤️ Tim Mạch": {"icon": "❤️", "page": "pages/01_📊_Scores.py", "color": "#e74c3c"},
        "🚨 Cấp cứu": {"icon": "🚨", "page": "pages/01_📊_Scores.py", "color": "#e67e22"},
        "🧠 Thần Kinh": {"icon": "🧠", "page": "pages/01_📊_Scores.py", "color": "#3498db"},
        "💊 Thuốc": {"icon": "💊", "page": "pages/07_💊_Drug_Database.py", "color": "#9b59b6"},
        "🔬 Labs": {"icon": "🔬", "page": "pages/05_🔬_Labs_and_Calculators.py", "color": "#1abc9c"},
        "📋 Protocols": {"icon": "📋", "page": "pages/04_📋_Protocols.py", "color": "#f39c12"},
    }
    
    cols = st.columns(3)
    for idx, (cat_name, cat_info) in enumerate(categories.items()):
        with cols[idx % 3]:
            if st.button(
                f"{cat_info['icon']} {cat_name}",
                key=f"cat_{cat_name}",
                use_container_width=True
            ):
                st.switch_page(cat_info['page'])

st.markdown("---")

# Footer
render_standard_footer()
