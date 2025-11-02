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
    
    - 📊 **Scores** - Thang điểm lâm sàng
    - 💊 **Antibiotics** - Liều kháng sinh
    - 🔬 **Labs** - Xét nghiệm & giải thích ⭐ NEW
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

with col1:
    with st.container():
        st.markdown("""
        <div style="text-align: center; padding: 20px; background-color: #e3f2fd; border-radius: 10px;">
            <h2>📊</h2>
            <h4>Scores</h4>
            <p style="font-size: 0.85em;">34 calculators<br/>8 specialties</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("📊 Mở Scores", key="quick_scores", use_container_width=True):
            st.switch_page("pages/01_📊_Scores.py")

with col2:
    with st.container():
        st.markdown("""
        <div style="text-align: center; padding: 20px; background-color: #e8f5e9; border-radius: 10px;">
            <h2>💊</h2>
            <h4>Drugs</h4>
            <p style="font-size: 0.85em;">TDM & Dosing<br/>3 calculators</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("💊 Mở Drugs", key="quick_drugs", use_container_width=True):
            st.switch_page("pages/02_💊_Antibiotics.py")

with col3:
    with st.container():
        st.markdown("""
        <div style="text-align: center; padding: 20px; background-color: #fff3e0; border-radius: 10px;">
            <h2>🔬</h2>
            <h4>Labs</h4>
            <p style="font-size: 0.85em;">9 panels<br/>Unit conversion</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🔬 Mở Labs", key="quick_labs", use_container_width=True):
            st.switch_page("pages/05_🔬_Labs.py")

with col4:
    with st.container():
        st.markdown("""
        <div style="text-align: center; padding: 20px; background-color: #fce4ec; border-radius: 10px;">
            <h2>🫁</h2>
            <h4>Ventilator</h4>
            <p style="font-size: 0.85em;">ARDSNet<br/>PEEP/FiO₂</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🫁 Mở Ventilator", key="quick_vent", use_container_width=True):
            st.switch_page("pages/03_🫁_Ventilator.py")

with col5:
    with st.container():
        st.markdown("""
        <div style="text-align: center; padding: 20px; background-color: #f3e5f5; border-radius: 10px;">
            <h2>📋</h2>
            <h4>Protocols</h4>
            <p style="font-size: 0.85em;">5 protocols<br/>Evidence-based</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("📋 Mở Protocols", key="quick_protocols", use_container_width=True):
            st.switch_page("pages/04_📋_Protocols.py")

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
