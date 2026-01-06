"""
Main Menu - Enhanced Homepage
Unified entry point with search, favorites, recently used, quick access, and stats
"""

import streamlit as st
from utils.page_helper import setup_page, render_standard_footer
from components.ui import render_info_box, render_hero

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
        'most_used_calculator': None
    }

# Custom CSS
st.markdown("""
<style>
.main-menu-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
}

.search-section {
    margin-bottom: 30px;
}

.stats-card {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 20px;
    border-radius: 12px;
    margin: 10px 0;
}

.stats-card h3 {
    color: white;
    margin: 0;
}

.stats-card p {
    color: rgba(255, 255, 255, 0.9);
    margin: 5px 0;
}

.quick-access-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 15px;
    margin: 20px 0;
}

.category-card {
    background: white;
    border: 1px solid #e0e0e0;
    border-radius: 12px;
    padding: 20px;
    text-align: center;
    cursor: pointer;
    transition: all 0.3s;
}

.category-card:hover {
    box-shadow: 0 4px 16px rgba(0,0,0,0.1);
    transform: translateY(-2px);
}
</style>
""", unsafe_allow_html=True)

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

# Search results
if search_query:
    st.session_state.global_search_query = search_query
    results = search_calculators(search_query, max_results=10)
    
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
        st.info("Không tìm thấy kết quả. Thử từ khóa khác.")

st.markdown("---")

# Section 2: Stats Dashboard
st.markdown("### 📊 Thống kê sử dụng")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="stats-card">
        <h3>📈 Tổng số lần tính</h3>
        <p style="font-size: 24px; font-weight: bold;">{}</p>
    </div>
    """.format(st.session_state.usage_stats.get('total_calculations', 0)), unsafe_allow_html=True)

with col2:
    most_used = st.session_state.usage_stats.get('most_used_calculator')
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
    categories = st.session_state.usage_stats.get('calculations_by_category', {})
    top_category = max(categories.items(), key=lambda x: x[1])[0] if categories else "Chưa có"
    st.markdown("""
    <div class="stats-card">
        <h3>📚 Chuyên khoa phổ biến</h3>
        <p style="font-size: 18px;">{}</p>
    </div>
    """.format(top_category), unsafe_allow_html=True)

st.markdown("---")

# Section 3: Favorites & Recently Used (Two columns)
col_left, col_right = st.columns(2)

with col_left:
    st.markdown("### ⭐ Yêu thích")
    render_favorites(max_items=5)

with col_right:
    st.markdown("### 🕐 Sử dụng gần đây")
    render_recently_used(max_items=5)

st.markdown("---")

# Section 4: Quick Access - Most Popular
st.markdown("### ⚡ Truy cập nhanh - Calculator phổ biến")

# Get most popular calculators (based on usage stats or default)
popular_calculators = [
    'ascvd', 'cha2ds2vasc', 'sofa', 'gcs', 'qsofa', 
    'hasbled', 'heart', 'timi', 'grace'
]

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

# Section 5: Browse by Category
st.markdown("### 📚 Duyệt theo chuyên khoa")

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
