"""
Clinical Assistant - Streamlit Version
Main application file - Refactored with modular components

Author: Clinical IT Team
Version: 2.1.0
Date: 2025-01-30
"""

import streamlit as st
from pathlib import Path

# Import configuration
from config.calculators import ALL_CALCULATORS
from config.app_config import get_module_list_for_navigation, APP_CONFIG
from config.theme import get_module_style

# Import UI components
from components.search import render_search
from components.favorites import render_favorites
from components.recently_used import render_recently_used
from components.stats import render_stats, render_updates, render_tips

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
    st.info("""
    **Chọn module bên trái** để bắt đầu:
    
    - 📊 **Scores** - Thang điểm lâm sàng (110 calculators)
    - 💊 **Antibiotics** - Liều kháng sinh & TDM
    - 🔬 **Labs & Calculators** - Xét nghiệm + Tính toán ⭐ INTEGRATED
    - 🫁 **Ventilator** - Cài đặt máy thở
    - 📋 **Protocols** - Phác đồ điều trị
    """)
    
    st.markdown("---")
    
    # Version info & Stats
    st.caption(f"**Version:** {APP_CONFIG['version']} 🔥")
    st.caption(f"**Updated:** {APP_CONFIG['last_updated']}")
    st.caption(f"**Calculators:** {len(ALL_CALCULATORS)}")
    st.caption(f"**Favorites:** {len(st.session_state.favorites)}")
    
    # Footer
    st.markdown("---")
    st.caption("⚠️ Chỉ mục đích tham khảo")
    st.caption("Không thay thế đánh giá lâm sàng")

# ========== MAIN CONTENT ==========

# 1. Search
render_search()

# 2. Favorites
render_favorites()

# 3. Recently Used
render_recently_used()

# 4. Quick Access Modules - Enhanced with beautiful cards
st.markdown("### 🚀 Truy Cập Nhanh Modules")
st.caption("Chọn module để bắt đầu tính toán")

# Get modules from unified config
modules = get_module_list_for_navigation()

# Use responsive columns (5 on desktop, fewer on mobile)
num_cols = min(5, len(modules))
cols = st.columns(num_cols)

for idx, (col, module) in enumerate(zip(cols, modules)):
    with col:
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
        
        if st.button(f"▶️ Mở {module['title']}", key=module['key'], use_container_width=True, type="primary"):
            st.switch_page(module['page'])

st.markdown("---")

# 5. Stats
render_stats()

# 6. Updates
render_updates()

# 7. Tips
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

# Footer
st.markdown("---")
st.caption("© 2025 Clinical Assistant | Made with ❤️ for healthcare workers")
