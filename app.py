"""
Clinical Assistant - Streamlit Version
Main application file with Search, Favorites & Recently Used

Author: Clinical IT Team
Version: 2.0.0
Date: 2025-10-29
"""

import streamlit as st
import pandas as pd
from pathlib import Path
from datetime import datetime

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

# ========== CALCULATOR REGISTRY ==========
ALL_CALCULATORS = {
    # Scores - Cardiology
    "cha2ds2vasc": {"name": "CHA₂DS₂-VASc", "category": "Tim Mạch", "icon": "❤️", "page": "Scores"},
    "hasbled": {"name": "HAS-BLED", "category": "Tim Mạch", "icon": "❤️", "page": "Scores"},
    "score2": {"name": "SCORE2", "category": "Tim Mạch", "icon": "❤️", "page": "Scores"},
    "score2_op": {"name": "SCORE2-OP", "category": "Tim Mạch", "icon": "❤️", "page": "Scores"},
    "heart": {"name": "HEART Score", "category": "Tim Mạch", "icon": "❤️", "page": "Scores"},
    "timi": {"name": "TIMI", "category": "Tim Mạch", "icon": "❤️", "page": "Scores"},
    "grace": {"name": "GRACE", "category": "Tim Mạch", "icon": "❤️", "page": "Scores"},
    "framingham": {"name": "Framingham", "category": "Tim Mạch", "icon": "❤️", "page": "Scores"},
    
    # Scores - Emergency
    "qsofa": {"name": "qSOFA", "category": "Cấp Cứu", "icon": "🚨", "page": "Scores"},
    "sofa": {"name": "SOFA", "category": "Cấp Cứu", "icon": "🚨", "page": "Scores"},
    "apache2": {"name": "APACHE II", "category": "Cấp Cứu", "icon": "🚨", "page": "Scores"},
    "saps2": {"name": "SAPS II", "category": "Cấp Cứu", "icon": "🚨", "page": "Scores"},
    "mods": {"name": "MODS", "category": "Cấp Cứu", "icon": "🚨", "page": "Scores"},
    
    # Scores - Respiratory
    "curb65": {"name": "CURB-65", "category": "Hô Hấp", "icon": "🫁", "page": "Scores"},
    "psi_port": {"name": "PSI/PORT", "category": "Hô Hấp", "icon": "🫁", "page": "Scores"},
    "wells_pe": {"name": "Wells PE", "category": "Hô Hấp", "icon": "🫁", "page": "Scores"},
    
    # Scores - Neurology
    "gcs": {"name": "GCS", "category": "Thần Kinh", "icon": "🧠", "page": "Scores"},
    "nihss": {"name": "NIHSS", "category": "Thần Kinh", "icon": "🧠", "page": "Scores"},
    "ich_score": {"name": "ICH Score", "category": "Thần Kinh", "icon": "🧠", "page": "Scores"},
    "hunt_hess": {"name": "Hunt & Hess", "category": "Thần Kinh", "icon": "🧠", "page": "Scores"},
    
    # Antibiotics/Drugs
    "crcl": {"name": "CrCl Calculator", "category": "Thuốc", "icon": "💊", "page": "Drugs"},
    "vancomycin": {"name": "Vancomycin Dosing", "category": "Thuốc", "icon": "💊", "page": "Drugs"},
    "aminoglycoside": {"name": "Aminoglycoside", "category": "Thuốc", "icon": "💊", "page": "Drugs"},
    
    # Labs
    "cbc": {"name": "CBC", "category": "Xét Nghiệm", "icon": "🔬", "page": "Labs"},
    "bmp": {"name": "BMP", "category": "Xét Nghiệm", "icon": "🔬", "page": "Labs"},
    "cmp": {"name": "CMP", "category": "Xét Nghiệm", "icon": "🔬", "page": "Labs"},
    "lft": {"name": "LFT", "category": "Xét Nghiệm", "icon": "🔬", "page": "Labs"},
    "lipid": {"name": "Lipid Panel", "category": "Xét Nghiệm", "icon": "🔬", "page": "Labs"},
    "cardiac_markers": {"name": "Cardiac Markers", "category": "Xét Nghiệm", "icon": "🔬", "page": "Labs"},
    "coag": {"name": "Coagulation", "category": "Xét Nghiệm", "icon": "🔬", "page": "Labs"},
    "thyroid": {"name": "Thyroid", "category": "Xét Nghiệm", "icon": "🔬", "page": "Labs"},
    "abg": {"name": "ABG", "category": "Xét Nghiệm", "icon": "🔬", "page": "Labs"},
    
    # Ventilator
    "ardsnet": {"name": "ARDSNet Calculator", "category": "Thở Máy", "icon": "🫁", "page": "Ventilator"},
    "peep_fio2": {"name": "PEEP/FiO2 Table", "category": "Thở Máy", "icon": "🫁", "page": "Ventilator"},
    
    # Protocols
    "sepsis": {"name": "Sepsis Bundle", "category": "Phác Đồ", "icon": "📋", "page": "Protocols"},
    "copd": {"name": "COPD", "category": "Phác Đồ", "icon": "📋", "page": "Protocols"},
    "asthma": {"name": "Asthma", "category": "Phác Đồ", "icon": "📋", "page": "Protocols"},
    "acs": {"name": "ACS", "category": "Phác Đồ", "icon": "📋", "page": "Protocols"},
    "heart_failure": {"name": "Heart Failure", "category": "Phác Đồ", "icon": "📋", "page": "Protocols"},
}

# ========== HELPER FUNCTIONS ==========
def add_to_favorites(calc_id):
    """Add calculator to favorites"""
    if calc_id not in st.session_state.favorites:
        st.session_state.favorites.append(calc_id)

def remove_from_favorites(calc_id):
    """Remove calculator from favorites"""
    if calc_id in st.session_state.favorites:
        st.session_state.favorites.remove(calc_id)

def add_to_recently_used(calc_id):
    """Add calculator to recently used (max 10)"""
    if calc_id in st.session_state.recently_used:
        st.session_state.recently_used.remove(calc_id)
    st.session_state.recently_used.insert(0, calc_id)
    st.session_state.recently_used = st.session_state.recently_used[:10]  # Keep only last 10

def search_calculators(query):
    """Search calculators by name or category"""
    query = query.lower()
    results = []
    for calc_id, calc_info in ALL_CALCULATORS.items():
        if query in calc_info['name'].lower() or query in calc_info['category'].lower():
            results.append((calc_id, calc_info))
    return results

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
    - 🔬 **Labs** - Xét nghiệm & giải thích ⭐ NEW
    - 🫁 **Ventilator** - Cài đặt máy thở
    - 📋 **Protocols** - Phác đồ điều trị
    """)
    
    st.markdown("---")
    
    # Version info & Stats
    st.caption("**Version:** 2.0.0 🔥")
    st.caption("**Updated:** 2025-10-29")
    st.caption(f"**Calculators:** {len(ALL_CALCULATORS)}")
    st.caption(f"**Favorites:** {len(st.session_state.favorites)}")
    
    # Footer
    st.markdown("---")
    st.caption("⚠️ Chỉ mục đích tham khảo")
    st.caption("Không thay thế đánh giá lâm sàng")

# ========== MAIN CONTENT ==========

# ========== 1. SEARCH BAR ==========
st.markdown("### 🔍 Tìm Kiếm Nhanh")

search_query = st.text_input(
    "Tìm calculator, xét nghiệm, hoặc phác đồ...",
    placeholder="Ví dụ: CHA2DS2VASc, troponin, sepsis...",
    help="Gõ tên calculator hoặc chuyên khoa để tìm nhanh",
    key="search_box"
)

if search_query:
    results = search_calculators(search_query)
    if results:
        st.success(f"✅ Tìm thấy **{len(results)}** kết quả:")
        
        # Display search results in columns
        cols = st.columns(min(3, len(results)))
        for idx, (calc_id, calc_info) in enumerate(results[:6]):  # Show max 6 results
            with cols[idx % 3]:
                is_fav = calc_id in st.session_state.favorites
                fav_icon = "⭐" if is_fav else "☆"
                
                with st.container():
                    st.markdown(f"""
                    **{calc_info['icon']} {calc_info['name']}**  
                    📂 {calc_info['category']} | 📄 {calc_info['page']}
                    """)
                    
                    col_fav, col_go = st.columns([1, 2])
                    with col_fav:
                        if st.button(fav_icon, key=f"fav_search_{calc_id}"):
                            if is_fav:
                                remove_from_favorites(calc_id)
                            else:
                                add_to_favorites(calc_id)
                            st.rerun()
                    
                    with col_go:
                        if st.button("Mở", key=f"open_search_{calc_id}", type="primary"):
                            add_to_recently_used(calc_id)
                            st.info(f"Đang mở {calc_info['name']} trong module {calc_info['page']}...")
                    
                    st.markdown("---")
    else:
        st.warning(f"❌ Không tìm thấy kết quả cho: **{search_query}**")
        st.caption("💡 Thử tìm với từ khóa khác: tim mạch, cấp cứu, xét nghiệm, thuốc...")

st.markdown("---")

# ========== 2. FAVORITES ==========
st.markdown("### ⭐ Yêu Thích")

if st.session_state.favorites:
    cols = st.columns(min(4, len(st.session_state.favorites)))
    for idx, calc_id in enumerate(st.session_state.favorites[:8]):  # Show max 8
        if calc_id in ALL_CALCULATORS:
            calc_info = ALL_CALCULATORS[calc_id]
            with cols[idx % 4]:
                with st.container():
                    st.markdown(f"""
                    **{calc_info['icon']} {calc_info['name']}**  
                    {calc_info['category']}
                    """)
                    
                    col_remove, col_open = st.columns([1, 2])
                    with col_remove:
                        if st.button("🗑️", key=f"remove_fav_{calc_id}", help="Xóa khỏi yêu thích"):
                            remove_from_favorites(calc_id)
                            st.rerun()
                    
                    with col_open:
                        if st.button("Mở", key=f"open_fav_{calc_id}", type="primary"):
                            add_to_recently_used(calc_id)
                            st.info(f"Mở {calc_info['name']} từ {calc_info['page']}...")
                    
                    st.markdown("---")
else:
    st.info("💡 Chưa có calculator yêu thích. Nhấn ⭐ khi tìm kiếm để thêm vào danh sách!")

st.markdown("---")

# ========== 3. RECENTLY USED ==========
st.markdown("### 🕐 Sử Dụng Gần Đây")

if st.session_state.recently_used:
    cols = st.columns(min(5, len(st.session_state.recently_used)))
    for idx, calc_id in enumerate(st.session_state.recently_used[:5]):  # Show max 5
        if calc_id in ALL_CALCULATORS:
            calc_info = ALL_CALCULATORS[calc_id]
            with cols[idx]:
                is_fav = calc_id in st.session_state.favorites
                fav_icon = "⭐" if is_fav else "☆"
                
                st.markdown(f"""
                **{calc_info['icon']} {calc_info['name']}**  
                {calc_info['category']}
                """)
                
                col_fav, col_open = st.columns([1, 2])
                with col_fav:
                    if st.button(fav_icon, key=f"fav_recent_{calc_id}"):
                        if is_fav:
                            remove_from_favorites(calc_id)
                        else:
                            add_to_favorites(calc_id)
                        st.rerun()
                
                with col_open:
                    if st.button("Mở", key=f"open_recent_{calc_id}", type="secondary"):
                        st.info(f"Mở {calc_info['name']}...")
else:
    st.info("💡 Chưa có lịch sử sử dụng. Bắt đầu dùng calculator để xem lịch sử ở đây!")

st.markdown("---")

# ========== 4. QUICK ACCESS MODULES ==========
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

# Quick stats
st.subheader("📈 Thống Kê Hệ Thống")

# Calculate real stats
total_calcs = len(ALL_CALCULATORS)
total_favorites = len(st.session_state.favorites)
total_recent = len(st.session_state.recently_used)
session_calcs = st.session_state.total_calculations

col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Tổng Calculators", total_calcs, "Ready ✓")
col2.metric("Yêu Thích", total_favorites, f"+{total_favorites}" if total_favorites > 0 else "Add more")
col3.metric("Gần Đây", total_recent, "This session")
col4.metric("Tính Toán", session_calcs, "Times")
col5.metric("Modules", "5", "All active ✅")

st.markdown("---")

# Recent updates
st.subheader("🆕 Cập Nhật Mới Nhất")

with st.expander("📅 2025-10-29 - Version 2.0.0 🔥 MAJOR UPDATE"):
    st.markdown("""
    ### 🎉 Tính Năng Mới:
    
    **1. ✅ Search & Navigation:**
    - 🔍 Global search - Tìm calculator nhanh chóng
    - ⭐ Favorites system - Lưu calculators yêu thích
    - 🕐 Recently used - Theo dõi lịch sử sử dụng
    - 🚀 Quick access modules - Truy cập nhanh
    
    **2. ✅ Unit Conversion (SI Units mặc định):**
    - Creatinine: µmol/L ↔ mg/dL
    - Glucose: mmol/L ↔ mg/dL  
    - Cholesterol: mmol/L ↔ mg/dL
    - Triglycerides: mmol/L ↔ mg/dL
    - Bilirubin: µmol/L ↔ mg/dL
    - BUN/Urea: mmol/L ↔ mg/dL
    
    **3. ✅ Vietnamese Localization:**
    - 100% interface tiếng Việt
    - Tất cả interpretations bằng tiếng Việt
    - Clinical guidance tiếng Việt
    
    **4. ✅ Labs Module (9 panels):**
    - CBC, BMP, CMP, LFT
    - Lipid Panel, Cardiac Markers
    - Coagulation, Thyroid, ABG
    - Auto-interpretation
    
    **5. ✅ Improved Architecture:**
    - 100% modular design
    - Faster performance
    - Better mobile experience
    - Professional UI/UX
    
    ### 🎯 Next:
    - 🚧 Drug interaction checker
    - 🚧 Differential diagnosis generator
    - 🚧 More calculators (70+ planned)
    """)

with st.expander("📅 2025-10-28 - Version 1.0.0"):
    st.markdown("""
    - ✅ Initial Streamlit deployment
    - ✅ Basic calculators (34 tools)
    - ✅ Modular architecture
    - ✅ GitHub auto-deploy
    """)

st.markdown("---")

# Quick tips
st.subheader("💡 Mẹo Sử Dụng")

tip_col1, tip_col2, tip_col3 = st.columns(3)

with tip_col1:
    st.info("""
    **🔍 Tìm Kiếm:**
    - Gõ tên calculator
    - Tìm theo chuyên khoa
    - Ví dụ: "tim mạch", "sepsis"
    """)

with tip_col2:
    st.success("""
    **⭐ Yêu Thích:**
    - Nhấn ⭐ để lưu
    - Truy cập nhanh từ Home
    - Tối đa 8 favorites
    """)

with tip_col3:
    st.warning("""
    **🕐 Lịch Sử:**
    - Tự động lưu 10 gần nhất
    - Xem ngay tại Home
    - Không lưu trữ lâu dài
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
5. KHÔNG lưu trữ thông tin bệnh nhân 

**Phần mềm cung cấp "như hiện có" - Người dùng chịu trách nhiệm về quyết định lâm sàng**
""")

# Footer
st.markdown("---")
st.caption("© 2025 Clinical Assistant | Made with ❤️ for healthcare workers")

