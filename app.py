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

# ========== LOAD CUSTOM CSS ==========
css_file = Path(__file__).parent / "static" / "styles.css"
if css_file.exists():
    with open(css_file, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ========== HEADER ==========
col1, col2 = st.columns([3, 1])

with col1:
    st.markdown('<p class="main-title">🩺 Clinical Assistant</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Hệ thống công cụ hỗ trợ lâm sàng toàn diện</p>', unsafe_allow_html=True)

with col2:
    # Placeholder for hospital logo
    # st.image("assets/logo.png", width=150)
    pass

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
    st.caption("**Version:** 2.1.0 🔥")
    st.caption("**Updated:** 2025-01-30")
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

# 4. Quick Access Modules
st.markdown("### 🚀 Truy Cập Nhanh Modules")

col1, col2, col3, col4, col5 = st.columns(5)

modules = [
    {
        "icon": "📊",
        "title": "Scores",
        "desc": "110 calculators<br/>19 specialties",
        "color": "linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%)",
        "border": "#1976d2",
        "page": "pages/01_📊_Scores.py",
        "key": "quick_scores"
    },
    {
        "icon": "💊",
        "title": "Drugs",
        "desc": "57 antibiotics<br/>TDM & Dosing",
        "color": "linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%)",
        "border": "#4caf50",
        "page": "pages/02_💊_Antibiotics.py",
        "key": "quick_drugs"
    },
    {
        "icon": "🔬",
        "title": "Labs",
        "desc": "9 panels + Calculators<br/>Integrated workflow",
        "color": "linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%)",
        "border": "#ff9800",
        "page": "pages/05_🔬_Labs_and_Calculators.py",
        "key": "quick_labs"
    },
    {
        "icon": "🫁",
        "title": "Ventilator",
        "desc": "ARDSNet<br/>PEEP/FiO₂",
        "color": "linear-gradient(135deg, #fce4ec 0%, #f8bbd0 100%)",
        "border": "#e91e63",
        "page": "pages/03_🫁_Ventilator.py",
        "key": "quick_vent"
    },
    {
        "icon": "📋",
        "title": "Protocols",
        "desc": "5 protocols<br/>Evidence-based",
        "color": "linear-gradient(135deg, #f3e5f5 0%, #e1bee7 100%)",
        "border": "#9c27b0",
        "page": "pages/04_📋_Protocols.py",
        "key": "quick_protocols"
    }
]

columns = [col1, col2, col3, col4, col5]
for idx, (col, module) in enumerate(zip(columns, modules)):
    with col:
        st.markdown(f"""
        <div class="module-card" style="background: {module['color']}; border: 2px solid {module['border']}; text-align: center;">
            <div>
                <div class="module-icon">{module['icon']}</div>
                <div class="module-title">{module['title']}</div>
                <div class="module-desc">{module['desc']}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button(f"{module['icon']} Mở {module['title']}", key=module['key'], use_container_width=True):
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
