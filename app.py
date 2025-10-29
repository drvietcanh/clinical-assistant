"""
Clinical Assistant - Streamlit Version
Main application file

Author: Clinical IT Team
Version: 1.0.0
Date: 2025-10-29
"""

import streamlit as st
import pandas as pd
from pathlib import Path

# ========== PAGE CONFIG ==========
st.set_page_config(
    page_title="Clinical Assistant",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ========== CUSTOM CSS ==========
st.markdown("""
<style>
    /* Main title */
    .main-title {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1976d2;
        margin-bottom: 0;
    }
    
    /* Subtitle */
    .subtitle {
        font-size: 1rem;
        color: #666;
        margin-top: 0;
    }
    
    /* Card-like containers */
    .stAlert {
        border-radius: 10px;
    }
    
    /* Metrics */
    [data-testid="stMetricValue"] {
        font-size: 2rem;
    }
    
    /* Buttons */
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        font-weight: 600;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #f0f2f6;
    }
</style>
""", unsafe_allow_html=True)

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
    - 🫁 **Ventilator** - Cài đặt máy thở
    - 📋 **Protocols** - Phác đồ điều trị
    """)
    
    st.markdown("---")
    
    # Version info
    st.caption("**Version:** 1.0.0")
    st.caption("**Updated:** 2025-10-29")
    
    # Footer
    st.markdown("---")
    st.caption("⚠️ Chỉ mục đích tham khảo")
    st.caption("Không thay thế đánh giá lâm sàng")

# ========== MAIN CONTENT ==========

# Welcome message
st.markdown("""
### 👋 Chào mừng đến với Clinical Assistant!

Hệ thống cung cấp các công cụ lâm sàng dựa trên bằng chứng khoa học:

""")

# Feature cards
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.info("""
    ### 📊 Scores
    - qSOFA
    - SOFA
    - CHA₂DS₂-VASc
    - HAS-BLED
    - CURB-65
    """)

with col2:
    st.success("""
    ### 💊 Antibiotics
    - Liều khởi đầu
    - Điều chỉnh thận
    - Vancomycin TDM
    - TDM aminoglycosides
    """)

with col3:
    st.warning("""
    ### 🫁 Ventilator
    - ARDSNet
    - COPD settings
    - PBW calculation
    - PEEP/FiO₂ table
    """)

with col4:
    st.error("""
    ### 📋 Protocols
    - COPD exacerbation
    - Sepsis bundle
    - DKA management
    - UGIB protocol
    """)

st.markdown("---")

# Quick stats (demo)
st.subheader("📈 Thống Kê Sử Dụng")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Calculators", "15+", "+3 this month")
col2.metric("Active Users", "127", "+12%")
col3.metric("Calculations", "1,847", "+234 this week")
col4.metric("Satisfaction", "4.8/5", "⭐")

st.markdown("---")

# Recent updates
st.subheader("🆕 Cập Nhật Gần Đây")

with st.expander("📅 2025-10-29 - Version 1.0.0"):
    st.markdown("""
    **Mới:**
    - ✅ Chuyển sang Streamlit platform
    - ✅ Giao diện mới hoàn toàn
    - ✅ Auto-deploy từ GitHub
    - ✅ Mobile-responsive tốt hơn
    
    **Đang phát triển:**
    - 🚧 SOFA score calculator
    - 🚧 Vancomycin dosing calculator
    - 🚧 ARDSNet ventilator settings
    """)

with st.expander("📅 2025-10-28 - Beta Release"):
    st.markdown("""
    - Initial data collection
    - qSOFA calculator (demo)
    - Database structure
    """)

st.markdown("---")

# Instructions
st.subheader("📖 Hướng Dẫn Sử Dụng")

st.markdown("""
1. **Chọn module** từ sidebar bên trái
2. **Nhập thông số** bệnh nhân
3. **Nhấn Calculate** để xem kết quả
4. **Đọc giải thích** và tham khảo guideline

**Lưu ý:**
- ⚠️ Công cụ chỉ mang tính tham khảo
- 📚 Luôn xác minh với guideline địa phương
- 🔒 Không nhập thông tin cá nhân bệnh nhân (PHI)
""")

st.markdown("---")

# Data source info
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
5. KHÔNG lưu trữ thông tin bệnh nhân (PHI)

**Phần mềm cung cấp "như hiện có" - Người dùng chịu trách nhiệm về quyết định lâm sàng**
""")

# Footer
st.markdown("---")
st.caption("© 2025 Clinical Assistant | Made with ❤️ for healthcare workers")

