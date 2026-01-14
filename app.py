"""
Clinical Assistant - Streamlit Version
Main application file - Refactored with modular components

Author: Clinical IT Team
Version: 2.3.0
Date: 2025-01-30
"""

import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
import os

# Import configuration
from config.calculators import ALL_CALCULATORS
from config.app_config import APP_CONFIG
from config.user_profile import get_current_profile, set_current_profile, get_profile_label
from utils.analytics_events import track_feature_usage
from utils.cache_helpers import get_module_list_for_navigation_cached
from config.theme import get_module_style
from utils.page_helper import inject_google_analytics

# Import UI components
try:
    from components.search_enhanced import render_search_enhanced as render_search
except ImportError:
    # Fallback to original search
    from components.search import render_search
from components.favorites import render_favorites
from components.recently_used import render_recently_used
from components.homepage_doctor import render_homepage_doctor

# Offline indicator (rendered at top level)
try:
    from components.offline import render_offline_indicator
    render_offline_indicator()
except ImportError:
    pass

# Import Patient Context
from components.patient_context import render_patient_context

# Mobile navigation and optimizations (lazy-init via helper)
def _init_mobile_features():
    try:
        from components.mobile_navigation import (
            render_mobile_bottom_nav,
            render_mobile_swipe_gestures,
            render_mobile_optimizations,
        )
        from components.mobile_inputs import render_mobile_input_optimizations
        from components.mobile_drawer import render_mobile_drawer_styles

        render_mobile_bottom_nav()
        render_mobile_swipe_gestures()
        render_mobile_optimizations()
        render_mobile_input_optimizations()
        render_mobile_drawer_styles()
    except ImportError:
        # Mobile helpers are optional; ignore if not available
        pass

# ========== GOOGLE ANALYTICS (Must be before page config) ==========
# Google Analytics 4 (GA4) tracking
# Cấu hình trong config/app_config.py hoặc set environment variable GOOGLE_ANALYTICS_ID
GOOGLE_ANALYTICS_ID = APP_CONFIG.get("google_analytics_id", "G-XXXXXXXXXX")
# Inject GA globally (works for all Streamlit pages)
inject_google_analytics()

# ========== PAGE CONFIG ==========
st.set_page_config(
    page_title="Trợ lý lâm sàng",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ========== VIEWPORT & META TAGS FOR MOBILE ==========
st.markdown(
    """
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes, viewport-fit=cover">
    <meta name="theme-color" content="#2D7DF6">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="default">
    <meta name="apple-mobile-web-app-title" content="Trợ lý lâm sàng">
    <meta name="mobile-web-app-capable" content="yes">
    <meta name="format-detection" content="telephone=no">
    """,
    unsafe_allow_html=True
)

# ========== INITIALIZE SESSION STATE ==========
if 'favorites' not in st.session_state:
    st.session_state.favorites = []

if 'recently_used' not in st.session_state:
    st.session_state.recently_used = []

if 'total_calculations' not in st.session_state:
    st.session_state.total_calculations = 0

# ========== DARK MODE STATE ==========
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False

# ========== LOAD CUSTOM CSS ==========
css_file = Path(__file__).parent / "static" / "styles.css"
if css_file.exists():
    with open(css_file, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ========== PWA SUPPORT - OFFLINE MODE ==========
# Inject manifest and service worker
static_dir = Path(__file__).parent / "static"
manifest_file = static_dir / "manifest.json"
offline_js_file = static_dir / "offline.js"

if manifest_file.exists():
    st.markdown(
        """
        <link rel="manifest" href="/static/manifest.json">
        """,
        unsafe_allow_html=True
    )

if offline_js_file.exists():
    with open(offline_js_file, "r", encoding="utf-8") as f:
        st.markdown(f"<script>{f.read()}</script>", unsafe_allow_html=True)

# Apply dark mode
if st.session_state.dark_mode:
    st.markdown(
        """
        <script>
        document.documentElement.setAttribute('data-theme', 'dark');
        </script>
        """,
        unsafe_allow_html=True
    )
else:
    st.markdown(
        """
        <script>
        document.documentElement.setAttribute('data-theme', 'light');
        </script>
        """,
        unsafe_allow_html=True
    )

# Initialize mobile features after basic config so it can use theme/state
_init_mobile_features()

# ========== HEADER ==========
col1, col2 = st.columns([3, 2])

with col1:
    st.markdown('<p class="main-title">🩺 Trợ lý lâm sàng</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Hệ thống công cụ hỗ trợ lâm sàng toàn diện</p>', unsafe_allow_html=True)

with col2:
    header_col1, header_col2 = st.columns(2)

    # Profile toggle: Nội / ICU
    with header_col1:
        current_profile = get_current_profile()
        profile_label_to_value = {"Nội": "noi", "ICU": "icu"}
        value_to_profile_label = {v: k for k, v in profile_label_to_value.items()}
        selected_label = st.selectbox(
            "Chuyên khoa",
            options=list(profile_label_to_value.keys()),
            index=list(profile_label_to_value.values()).index(current_profile),
            key="profile_select",
        )
        selected_profile = profile_label_to_value[selected_label]
        if selected_profile != current_profile:
            set_current_profile(selected_profile)
            # Track profile switch for analytics
            try:
                track_feature_usage(f"profile_switch_{selected_profile}")
            except Exception:
                pass
            st.rerun()

    # Dark mode toggle
    with header_col2:
        dark_mode_label = "🌙 Dark" if not st.session_state.dark_mode else "☀️ Light"
        if st.button(dark_mode_label, key="dark_mode_toggle", use_container_width=True):
            st.session_state.dark_mode = not st.session_state.dark_mode
            st.rerun()

st.markdown("---")

# ========== SIDEBAR ==========
with st.sidebar:
    st.header("📋 Điều hướng")
    
    # Patient Context (New 2025 Feature)
    render_patient_context()
    st.sidebar.markdown("---")
    
    # New collapsible navigation
    try:
        from components.sidebar_navigation import render_sidebar_navigation_simple
        render_sidebar_navigation_simple()
    except ImportError:
        # Fallback to old navigation
        st.subheader("⚡ Truy cập nhanh Modules")
        module_quick_links = [
            ("📊 Calculators & Scores", "pages/01_📊_Scores.py"),
            ("💊 Thuốc & Liều dùng", "pages/07_💊_Drug_Database.py"),
            ("🫁 Hồi sức & Quy trình", "pages/09_🫁_Critical_Care.py"),
            ("🧭 Hỗ trợ quyết định", "pages/10_🧭_Decision_Support.py"),
            ("🩺 Chẩn đoán & Bài viết", "pages/06_🩺_Diagnosis.py"),
            ("💉 Tiêm chủng", "pages/11_💉_Vaccination.py"),
        ]
        
        for link_name, link_page in module_quick_links:
            if st.button(link_name, key=f"quick_{link_name}", use_container_width=True):
                st.switch_page(link_page)
    
    st.markdown("---")
    
    # Keyboard Shortcuts
    with st.expander("⌨️ Phím tắt", expanded=False):
        st.markdown("""
        - **Ctrl+K** - Tập trung vào ô tìm kiếm
        - **Esc** - Xóa tìm kiếm
        - **/** - Tìm kiếm nhanh
        """)
    
    st.markdown("---")
    
    # Version info & Stats
    st.caption(f"**Phiên bản:** {APP_CONFIG['version']} 🔥")
    st.caption(f"**Cập nhật:** {APP_CONFIG['last_updated']}")
    st.caption(f"**Calculators:** {len(ALL_CALCULATORS)}")
    st.caption(f"**Yêu thích:** {len(st.session_state.favorites)}")
    
    # PWA/Offline Info
    try:
        from components.offline import render_pwa_info, render_offline_status
        with st.expander("📱 PWA & Chế độ ngoại tuyến", expanded=False):
            render_offline_status()
            render_pwa_info()
    except ImportError:
        pass
    
    # Developer Tools và Clear Cache (luôn hiện trên Streamlit Cloud)
    # Check URL parameter để clear cache
    if st.query_params.get("clear_cache") == "true":
        st.cache_data.clear()
        st.cache_resource.clear()
        st.query_params.clear()
        st.rerun()
    
    # Developer Tools (hiện khi development hoặc khi enable trong secrets)
    show_dev_tools = (
        os.getenv("STREAMLIT_ENV") == "development" or 
        st.secrets.get("show_dev_tools", False) or
        st.query_params.get("dev_tools") == "true"  # Enable từ URL: ?dev_tools=true
    )
    
    if show_dev_tools:
        st.markdown("---")
        with st.expander("🛠️ Developer Tools", expanded=False):
            col1, col2, col3 = st.columns(3)
            with col1:
                if st.button("🔄 Rerun App"):
                    st.rerun()
            with col2:
                if st.button("🗑️ Clear Cache"):
                    st.cache_data.clear()
                    st.cache_resource.clear()
                    st.success("✅ Cache cleared!")
                    st.rerun()
            with col3:
                if st.button("🔄 Reset Session"):
                    for key in list(st.session_state.keys()):
                        del st.session_state[key]
                    st.cache_data.clear()
                    st.cache_resource.clear()
                    st.success("✅ Session reset!")
                    st.rerun()
    
    # Nút Clear Cache luôn hiện (không cần dev tools)
    st.markdown("---")
    if st.sidebar.button("🗑️ Clear Cache", help="Xóa cache của Streamlit"):
        st.cache_data.clear()
        st.cache_resource.clear()
        st.success("✅ Cache cleared!")
        st.rerun()
    
    # Footer
    st.markdown("---")
    st.caption("⚠️ Chỉ mục đích tham khảo")
    st.caption("Không thay thế đánh giá lâm sàng")

# ========== MAIN CONTENT ==========

# Use new homepage design for doctors if available
if render_homepage_doctor:
    # Render new homepage layout
    render_homepage_doctor()
    
    # Search Component (integrated into homepage)
    render_search()
    
    st.markdown("---")
    
    # Keep tabs for additional content
    tab1, tab2, tab3 = st.tabs(["🚀 Tất cả Modules", "⭐ Yêu Thích & Gần Đây", "📊 Thống Kê & Cập Nhật"])
else:
    # Fallback to original design
    # Hero Section with Search
    st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                padding: 2rem; 
                border-radius: 16px; 
                margin-bottom: 2rem;
                color: white;">
        <h2 style="color: white; margin-bottom: 0.5rem;">🔍 Tìm kiếm nhanh</h2>
        <p style="color: rgba(255,255,255,0.9); margin: 0;">Nhấn <kbd style="background: rgba(255,255,255,0.2); padding: 4px 8px; border-radius: 4px;">Ctrl+K</kbd> để focus vào ô tìm kiếm</p>
    </div>
    """, unsafe_allow_html=True)

    # Search Component
    render_search()

    st.markdown("---")
    
    # Tabs for better organization
    tab1, tab2, tab3 = st.tabs(["🚀 Truy Cập Nhanh", "⭐ Yêu Thích & Gần Đây", "📊 Thống Kê & Cập Nhật"])

with tab1:
    st.markdown("### 📚 Tất cả modules")
    st.caption("Chọn module để bắt đầu. Modules được nhóm theo chức năng.")
    
    # Group modules by category (cached)
    modules = get_module_list_for_navigation_cached()
    # Ẩn tất cả sub-items khỏi trang chủ, chỉ hiển thị các trang chính
    # Sub-items có thể truy cập qua sidebar navigation hoặc từ trang chính của chúng
    try:
        from config.navigation_config import NAVIGATION_SUB_ITEMS
        sub_item_ids = set(NAVIGATION_SUB_ITEMS.keys())
        modules = [m for m in modules if m.get("id") not in sub_item_ids]
    except ImportError:
        # Fallback: chỉ ẩn antibiotics như trước
        modules = [m for m in modules if m.get("id") != "antibiotics"]
    
    # Use new navigation structure if available
    try:
        from config.app_config import get_modules_grouped_by_category
        from config.navigation_config import get_all_categories
        
        categorized_modules = get_modules_grouped_by_category()
        nav_categories = get_all_categories()
        
        # Map category IDs to display names
        category_display_map = {}
        for cat_id, cat_info in nav_categories.items():
            category_display_map[cat_id] = cat_info.title
        
        # Also include uncategorized if exists
        if 'uncategorized' in categorized_modules:
            uncategorized = categorized_modules.pop('uncategorized')
        else:
            uncategorized = []
    except ImportError:
        # Fallback to old structure
        categories = {
            "📊 Calculators & Scores": ["scores", "labs", "tdm"],
            "💊 Thuốc & Liều dùng": ["drug_database", "antibiotics", "pill_identifier"],
            "🫁 Hồi sức & Quy trình": ["critical_care", "ventilator", "protocols", "guidelines_tracker"],
            "🧭 Hỗ trợ quyết định": ["phase2_features"],
            "🩺 Chẩn đoán & Bài viết": ["diagnosis", "in_depth_articles", "icd10_lookup", "disease_encyclopedia", "patient_education"],
            "💉 Tiêm chủng": ["vaccination"],
        }
        
        categorized_modules = {cat: [] for cat in categories.keys()}
        uncategorized = []
        category_display_map = {}
        
        # Categorize modules
        for module in modules:
            module_id = module.get('id', module['key'].replace('quick_', ''))
            categorized = False
            for cat_name, cat_ids in categories.items():
                if module_id in cat_ids:
                    categorized_modules[cat_name].append(module)
                    categorized = True
                    break
            if not categorized:
                uncategorized.append(module)
    
    # Display modules by category
    for cat_id, cat_modules in categorized_modules.items():
        if cat_modules:
            # Use display name if available, otherwise use ID
            cat_name = category_display_map.get(cat_id, cat_id.replace('_', ' ').title())
            st.markdown(f"#### {cat_name}")
            st.caption(f"{len(cat_modules)} module")
            
            # Use responsive columns
            num_cols = min(3, len(cat_modules))
            cols = st.columns(num_cols)

            for idx, module in enumerate(cat_modules):
                with cols[idx % num_cols]:
                    # Get style from theme
                    module_id = module.get('id', module['key'].replace('quick_', ''))
                    style = get_module_style(module_id)
                    gradient = style.get('gradient', module.get('color', style['gradient']))
                    border = style.get('border', module.get('border', style['border']))
                    
                    # Enhanced card with hover effect
                    card_html = f"""
                    <div class="module-card" 
                         style="background: {gradient}; 
                                border: 2px solid {border}; 
                                text-align: center; 
                                padding: 1.5rem; 
                                border-radius: 12px; 
                                margin: 0.5rem 0; 
                                cursor: pointer; 
                                transition: all 0.3s ease;
                                box-shadow: 0 2px 8px rgba(0,0,0,0.1);"
                         onmouseover="this.style.transform='translateY(-4px)'; this.style.boxShadow='0 4px 12px rgba(0,0,0,0.15)';"
                         onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 2px 8px rgba(0,0,0,0.1)';">
                        <div class="module-icon" style="font-size: 3rem; margin-bottom: 0.5rem;">{module['icon']}</div>
                        <div class="module-title" style="font-weight: bold; font-size: 1.1rem; margin-bottom: 0.5rem; color: #212121;">{module['title']}</div>
                        <div class="module-desc" style="font-size: 0.85rem; color: #666; line-height: 1.4;">{module['desc']}</div>
                    </div>
                    """
                    components.html(card_html, height=200, scrolling=False)

                    # Use a dedicated container per card to minimize re-renders
                    with st.container():
                        if st.button(
                            f"▶️ Mở {module['title']}",
                            key=f"{cat_name}_{module['key']}",
                            use_container_width=True,
                            type="primary",
                        ):
                            st.switch_page(module['page'])
            
            st.markdown("---")
    
    # Display uncategorized modules if any
    if uncategorized:
        st.markdown("#### 📦 Khác")
        num_cols = min(3, len(uncategorized))
        cols = st.columns(num_cols)
        for idx, module in enumerate(uncategorized):
            with cols[idx % num_cols]:
                module_id = module.get('id', module['key'].replace('quick_', ''))
                style = get_module_style(module_id)
                gradient = style.get('gradient', module.get('color', style['gradient']))
                border = style.get('border', module.get('border', style['border']))
                
                card_html = f"""
                <div class="module-card" 
                     style="background: {gradient}; 
                            border: 2px solid {border}; 
                            text-align: center; 
                            padding: 1.5rem; 
                            border-radius: 12px; 
                            margin: 0.5rem 0; 
                            cursor: pointer; 
                            transition: all 0.3s ease;
                            box-shadow: 0 2px 8px rgba(0,0,0,0.1);"
                     onmouseover="this.style.transform='translateY(-4px)'; this.style.boxShadow='0 4px 12px rgba(0,0,0,0.15)';"
                     onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 2px 8px rgba(0,0,0,0.1)';">
                    <div class="module-icon" style="font-size: 3rem; margin-bottom: 0.5rem;">{module['icon']}</div>
                    <div class="module-title" style="font-weight: bold; font-size: 1.1rem; margin-bottom: 0.5rem; color: #212121;">{module['title']}</div>
                    <div class="module-desc" style="font-size: 0.85rem; color: #666; line-height: 1.4;">{module['desc']}</div>
                </div>
                """
                components.html(card_html, height=200, scrolling=False)
                
                if st.button(f"▶️ Mở {module['title']}", key=f"other_{module['key']}", use_container_width=True, type="primary"):
                    st.switch_page(module['page'])

with tab2:
    st.markdown("### ⭐ Yêu Thích & Gần Đây")
    st.caption("Các calculator bạn đã đánh dấu và sử dụng gần đây")

    # Chỉ render nội dung khi người dùng thật sự mở tab 2
    with st.container():
        render_favorites()
        render_recently_used()

with tab3:
    st.markdown("### 📊 Thống Kê & Cập Nhật")
    st.caption("Thống kê hệ thống, cập nhật mới nhất và mẹo sử dụng")

    # Analytics Dashboard Toggle (imports kept local để giảm chi phí import global)
    try:
        from components.analytics import render_analytics_dashboard
        from components.stats import render_stats, render_updates, render_tips

        analytics_tab, stats_tab = st.tabs(["📊 Phân tích sử dụng", "📈 Thống kê hệ thống"])

        with analytics_tab:
            render_analytics_dashboard()

        with stats_tab:
            # Stats
            render_stats()

            # Updates
            render_updates()

            # Tips
            render_tips()
    except ImportError:
        try:
            from components.stats import render_stats, render_updates, render_tips

            # Stats
            render_stats()

            # Updates
            render_updates()

            # Tips
            render_tips()
        except ImportError:
            st.info("Stats module tạm thời không khả dụng.")

# 8. Data source info
with st.expander("📚 Nguồn dữ liệu & Tài liệu tham khảo"):
    st.markdown("""
    **Guidelines Chính:**
    - Sepsis-3 (JAMA 2016) - qSOFA, SOFA definitions
    - GOLD 2025 - COPD management
    - IDSA/ATS 2016 - HAP/VAP guidelines
    - ARDSNet 2000 - Low tidal volume ventilation
    - ASHP/IDSA 2020 - Vancomycin guidelines
    - ESC 2020 - Atrial fibrillation (CHA₂DS₂-VASc)
    
    **Cập nhật:** Chu kỳ rà soát hàng quý
    
    **Đóng góp:**
    - GitHub: [Report issues](https://github.com/YOUR_REPO/issues)
    - Email: clinical-it@hospital.com
    """)

# Disclaimer
st.markdown("---")
st.warning("""
**⚠️ QUAN TRỌNG - DISCLAIMER:**

1. Công cụ này CHỈ mục đích hỗ trợ quyết định lâm sàng
2. KHÔNG thay thế đánh giá lâm sàng của bác sĩ
3. Bác sĩ phải tự xác minh kết quả trước khi áp dụng
4. Tuân thủ chính sách và quy định địa phương
5. KHÔNG lưu trữ thông tin bệnh nhân 

**Phần mềm cung cấp "như hiện có" - Người dùng chịu trách nhiệm về quyết định lâm sàng**
""")

# ========== GOOGLE ANALYTICS STATS ==========
# Hiển thị thống kê lượt truy cập từ Google Analytics
try:
    from components.google_analytics_widget import render_google_analytics_counter
    render_google_analytics_counter()
except ImportError:
    pass

# Footer
st.markdown("---")
st.caption("© 2025 Trợ lý lâm sàng | Được tạo với ❤️ cho nhân viên y tế")
