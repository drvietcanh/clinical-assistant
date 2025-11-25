"""
Clinical Assistant - Streamlit Version
Main application file - Refactored with modular components

Author: Clinical IT Team
Version: 2.3.0
Date: 2025-01-30
"""

import streamlit as st
from pathlib import Path

# Import configuration
from config.calculators import ALL_CALCULATORS
from config.app_config import get_module_list_for_navigation, APP_CONFIG
from config.theme import get_module_style

# Import UI components
try:
    from components.search_enhanced import render_search_enhanced as render_search
except ImportError:
    # Fallback to original search
    from components.search import render_search
from components.favorites import render_favorites
from components.recently_used import render_recently_used
from components.stats import render_stats, render_updates, render_tips

# Offline indicator (rendered at top level)
try:
    from components.offline import render_offline_indicator
    render_offline_indicator()
except ImportError:
    pass

# Mobile navigation and optimizations
try:
    from components.mobile_navigation import (
        render_mobile_bottom_nav,
        render_mobile_swipe_gestures,
        render_mobile_optimizations
    )
    from components.mobile_inputs import render_mobile_input_optimizations
    render_mobile_bottom_nav()
    render_mobile_swipe_gestures()
    render_mobile_optimizations()
    render_mobile_input_optimizations()
except ImportError:
    pass

# ========== PAGE CONFIG ==========
st.set_page_config(
    page_title="Clinical Assistant",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
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
        <meta name="theme-color" content="#1976d2">
        <meta name="apple-mobile-web-app-capable" content="yes">
        <meta name="apple-mobile-web-app-status-bar-style" content="default">
        <meta name="apple-mobile-web-app-title" content="Clinical Assistant">
        """,
        unsafe_allow_html=True
    )

if offline_js_file.exists():
    with open(offline_js_file, "r", encoding="utf-8") as f:
        st.markdown(f"<script>{f.read()}</script>", unsafe_allow_html=True)

# ========== GOOGLE ANALYTICS ==========
# Google Analytics 4 (GA4) tracking
# Cấu hình trong config/app_config.py hoặc set environment variable GOOGLE_ANALYTICS_ID
GOOGLE_ANALYTICS_ID = APP_CONFIG.get("google_analytics_id", "G-XXXXXXXXXX")

if GOOGLE_ANALYTICS_ID and GOOGLE_ANALYTICS_ID != "G-XXXXXXXXXX":
    st.markdown(
        f"""
        <!-- Google tag (gtag.js) -->
        <script async src="https://www.googletagmanager.com/gtag/js?id={GOOGLE_ANALYTICS_ID}"></script>
        <script>
          window.dataLayer = window.dataLayer || [];
          function gtag(){{dataLayer.push(arguments);}}
          gtag('js', new Date());
          gtag('config', '{GOOGLE_ANALYTICS_ID}');
        </script>
        """,
        unsafe_allow_html=True
    )

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

# ========== HEADER ==========
col1, col2 = st.columns([3, 1])

with col1:
    st.markdown('<p class="main-title">🩺 Clinical Assistant</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Hệ thống công cụ hỗ trợ lâm sàng toàn diện</p>', unsafe_allow_html=True)

with col2:
    # Dark mode toggle
    dark_mode_label = "🌙 Dark" if not st.session_state.dark_mode else "☀️ Light"
    if st.button(dark_mode_label, key="dark_mode_toggle"):
        st.session_state.dark_mode = not st.session_state.dark_mode
        st.rerun()

st.markdown("---")

# ========== SIDEBAR ==========
with st.sidebar:
    st.header("📋 Navigation")
    
    # Quick Links Section
    st.subheader("⚡ Quick Links")
    quick_links = [
        ("📊 Scores", "pages/01_📊_Scores.py"),
        ("🔬 Labs", "pages/05_🔬_Labs_and_Calculators.py"),
        ("💊 Thuốc", "pages/07_💊_Drug_Database.py"),
        ("🫁 Hồi Sức", "pages/09_🫁_Critical_Care.py"),
    ]
    
    for link_name, link_page in quick_links:
        if st.button(link_name, key=f"quick_{link_name}", use_container_width=True):
            st.switch_page(link_page)
    
    st.markdown("---")
    
    st.info("""
    **📚 Tất Cả Modules:**
    
    **📊 Tính Toán:**
    - Scores (110 calculators)
    - Labs & Calculators
    - TDM
    
    **💊 Thuốc:**
    - Tra Cứu Thuốc
    - Antibiotics
    
    **🫁 Hồi Sức:**
    - Critical Care (bao gồm Ventilator Management)
    
    **📋 Hướng Dẫn:**
    - Protocols
    - Diagnosis
    """)
    
    st.markdown("---")
    
    # Keyboard Shortcuts
    with st.expander("⌨️ Keyboard Shortcuts"):
        st.markdown("""
        - **Ctrl+K** - Focus search
        - **Esc** - Clear search
        - **/** - Quick search
        """)
    
    st.markdown("---")
    
    # Version info & Stats
    st.caption(f"**Version:** {APP_CONFIG['version']} 🔥")
    st.caption(f"**Updated:** {APP_CONFIG['last_updated']}")
    st.caption(f"**Calculators:** {len(ALL_CALCULATORS)}")
    st.caption(f"**Favorites:** {len(st.session_state.favorites)}")
    
    # PWA/Offline Info
    try:
        from components.offline import render_pwa_info, render_offline_status
        with st.expander("📱 PWA & Offline", expanded=False):
            render_offline_status()
            render_pwa_info()
    except ImportError:
        pass
    
    # Footer
    st.markdown("---")
    st.caption("⚠️ Chỉ mục đích tham khảo")
    st.caption("Không thay thế đánh giá lâm sàng")

# ========== MAIN CONTENT ==========

# Hero Section with Search
st.markdown("""
<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
            padding: 2rem; 
            border-radius: 16px; 
            margin-bottom: 2rem;
            color: white;">
    <h2 style="color: white; margin-bottom: 0.5rem;">🔍 Tìm Kiếm Nhanh</h2>
    <p style="color: rgba(255,255,255,0.9); margin: 0;">Nhấn <kbd style="background: rgba(255,255,255,0.2); padding: 4px 8px; border-radius: 4px;">Ctrl+K</kbd> để focus vào ô tìm kiếm</p>
</div>
""", unsafe_allow_html=True)

# Search Component
render_search()

st.markdown("---")

# Tabs for better organization
tab1, tab2, tab3 = st.tabs(["🚀 Truy Cập Nhanh", "⭐ Yêu Thích & Gần Đây", "📊 Thống Kê & Cập Nhật"])

with tab1:
    st.markdown("### 📚 Tất Cả Modules")
    st.caption("Chọn module để bắt đầu. Modules được nhóm theo chức năng.")
    
    # Group modules by category
    modules = get_module_list_for_navigation()
    
    # Define categories
    categories = {
        "📊 Tính Toán & Scores": ["scores", "labs", "tdm"],
        "💊 Thuốc & Điều Trị": ["antibiotics", "drug_database"],
        "🫁 Hồi Sức & Cấp Cứu": ["ventilator", "critical_care"],
        "📋 Hướng Dẫn & Chẩn Đoán": ["protocols", "diagnosis"]
    }
    
    # Organize modules by category
    categorized_modules = {cat: [] for cat in categories.keys()}
    uncategorized = []
    
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
    for cat_name, cat_modules in categorized_modules.items():
        if cat_modules:
            st.markdown(f"#### {cat_name}")
            st.caption(f"{len(cat_modules)} modules")
            
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
                    st.markdown(card_html, unsafe_allow_html=True)
                    
                    if st.button(f"▶️ Mở {module['title']}", key=f"{cat_name}_{module['key']}", use_container_width=True, type="primary"):
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
                st.markdown(card_html, unsafe_allow_html=True)
                
                if st.button(f"▶️ Mở {module['title']}", key=f"other_{module['key']}", use_container_width=True, type="primary"):
                    st.switch_page(module['page'])

with tab2:
    st.markdown("### ⭐ Yêu Thích & Gần Đây")
    st.caption("Các calculator bạn đã đánh dấu và sử dụng gần đây")
    
    # Favorites
    render_favorites()
    
    # Recently Used
    render_recently_used()

with tab3:
    st.markdown("### 📊 Thống Kê & Thông Tin")
    st.caption("Thống kê hệ thống, cập nhật mới nhất và mẹo sử dụng")
    
    # Analytics Dashboard Toggle
    try:
        from components.analytics import render_analytics_dashboard
        analytics_tab, stats_tab = st.tabs(["📊 Usage Analytics", "📈 System Stats"])
        
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
        # Stats
        render_stats()
        
        # Updates
        render_updates()
        
        # Tips
        render_tips()

# 8. Data source info
with st.expander("📚 Nguồn Dữ Liệu & Tài Liệu Tham Khảo"):
    st.markdown("""
    **Guidelines Chính:**
    - Sepsis-3 (JAMA 2016) - qSOFA, SOFA definitions
    - GOLD 2025 - COPD management
    - IDSA/ATS 2016 - HAP/VAP guidelines
    - ARDSNet 2000 - Low tidal volume ventilation
    - ASHP/IDSA 2020 - Vancomycin guidelines
    - ESC 2020 - Atrial fibrillation (CHA₂DS₂-VASc)
    
    **Cập nhật:** Quarterly review cycle
    
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
st.caption("© 2025 Clinical Assistant | Made with ❤️ for healthcare workers")
