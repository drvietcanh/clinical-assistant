"""
Antibiotics Module - Optimized UI
Modern interface with tabs: By Infection, By Drug Class, Stewardship
Integrated with existing database and comparison tools
"""

import streamlit as st
from utils.page_helper import setup_page, render_standard_footer
from components.ui import render_info_box

from antibiotics import (
    render_database,
    render_multi_comparison
)
from antibiotics.comparison import render_comparison
from antibiotics.treatment_algorithms import render_algorithms_page
from antibiotics.update_notifications import get_unread_updates_count, render_whats_new

# Import new UI components
try:
    from antibiotics.ui_antibiotics_view import (
        render_antibiotics_by_infection_view,
        render_antibiotics_by_drug_class_view,
        render_stewardship_view
    )
    NEW_UI_AVAILABLE = True
except ImportError:
    NEW_UI_AVAILABLE = False

# Standard page setup
setup_page(
    page_title="Kháng sinh (chuyên sâu)",
    page_icon="💊",
    description="Module chuyên sâu về kháng sinh: phác đồ điều trị, so sánh và dữ liệu chi tiết"
)

# Hero section - optimized design
st.markdown("""
<style>
.hero-section {
    background: linear-gradient(135deg, #4caf50 0%, #2e7d32 100%);
    color: white;
    padding: 25px 30px;
    border-radius: 20px;
    margin-bottom: 25px;
    text-align: center;
    box-shadow: 0 8px 24px rgba(76,175,80,0.25), 0 4px 8px rgba(0,0,0,0.1);
    position: relative;
    overflow: hidden;
}

@media (max-width: 768px) {
    .hero-section {
        padding: 15px 15px !important;
        margin-bottom: 20px !important;
    }
    
    .hero-section h1 {
        font-size: 2em !important;
        margin: 0 !important;
    }
    
    .hero-section p {
        font-size: 1em !important;
        margin: 12px 0 0 0 !important;
    }
}
</style>

<div class="hero-section">
    <div style='position: relative; z-index: 1;'>
        <h1 style='margin: 0; color: white; font-size: 2.4em; font-weight: 700; letter-spacing: -0.5px; text-shadow: 0 2px 8px rgba(0,0,0,0.2);'>💊 Kháng sinh (Chuyên sâu)</h1>
        <p style='margin: 15px 0 0 0; color: rgba(255,255,255,0.95); font-size: 1.2em; font-weight: 400; line-height: 1.6;'>
            Phác đồ điều trị • So sánh kháng sinh • Dữ liệu chi tiết
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

# ========== SIDEBAR ==========
with st.sidebar:
    st.header("💊 Kháng sinh")
    # Show unread updates badge if any
    try:
        unread_count = get_unread_updates_count()
    except Exception:
        unread_count = 0
    if unread_count > 0:
        st.caption(f"Module chuyên sâu về kháng sinh  •  🆕 {unread_count} cập nhật mới")
    else:
        st.caption("Module chuyên sâu về kháng sinh")
    
    # Quick navigation to tabs
    st.markdown("### 🧭 Điều hướng")
    nav_col1, nav_col2 = st.columns(2)
    with nav_col1:
        if st.button("🦠 Nhiễm trùng", use_container_width=True, help="Tab Theo Nhiễm Trùng"):
            st.session_state.antibiotics_tab = 0
            st.rerun()
    with nav_col2:
        if st.button("💊 Thuốc", use_container_width=True, help="Tab Theo Nhóm Thuốc"):
            st.session_state.antibiotics_tab = 1
            st.rerun()
    
    nav_col3, nav_col4 = st.columns(2)
    with nav_col3:
        if st.button("🔄 Quản lý", use_container_width=True, help="Tab Quản lý Kháng sinh"):
            st.session_state.antibiotics_tab = 2
            st.rerun()
    with nav_col4:
        if st.button("🔍 Tìm kiếm", use_container_width=True, help="Tab Công cụ"):
            st.session_state.antibiotics_tab = 3
            st.rerun()
    
    st.markdown("---")

    # Quick view: What's new for Antibiotics
    with st.expander("🆕 Có gì mới trong Kháng sinh?", expanded=False):
        try:
            render_whats_new()
        except Exception:
            st.info("Không thể tải danh sách cập nhật.")
    
    # Quick links
    with st.expander("🔗 Liên kết nhanh", expanded=False):
        col1, col2 = st.columns(2)
        with col1:
            if st.button("💊 Drug Database", use_container_width=True):
                st.switch_page("pages/07_💊_Drug_Database.py")
        with col2:
            if st.button("📊 TDM", use_container_width=True):
                st.switch_page("pages/08_📊_TDM.py")
    
    st.markdown("---")
    
    # Info box - optimized
    render_info_box(
        """
    **📚 Căn cứ khoa học:**
    - IDSA/ATS Guidelines 2019
    - Sanford Guide 2025
    - Surviving Sepsis Campaign 2021
    - WHO AWaRe Classification
        """,
        type="info",
        title="Thông tin"
    )

# ========== MAIN CONTENT ==========

# Inject Antibiotics CSS styles
st.markdown("""
<link rel="stylesheet" href="static/antibiotics_styles.css">
""", unsafe_allow_html=True)

# Inject print-friendly CSS
try:
    from antibiotics.export import inject_print_css
    inject_print_css()
except ImportError:
    pass

# Mobile styles and advanced features injection
try:
    from antibiotics.mobile_ui import (
        inject_mobile_styles,
        inject_swipe_gestures,
        inject_pull_to_refresh,
        inject_card_swipe_actions,
        inject_quick_actions_menu,
        inject_pwa_support,
        inject_offline_indicator
    )
    from antibiotics.performance import (
        inject_lazy_loading,
        inject_image_lazy_loading,
        inject_performance_monitoring
    )
    
    inject_mobile_styles()
    inject_swipe_gestures()
    inject_pull_to_refresh()
    inject_card_swipe_actions()
    inject_quick_actions_menu()
    inject_pwa_support()
    inject_offline_indicator()
    inject_lazy_loading()
    inject_image_lazy_loading()
    inject_performance_monitoring()
except ImportError:
    pass

# Main tabs for new UI with mobile optimization
if NEW_UI_AVAILABLE:
    # Mobile-optimized tabs
    st.markdown("""
    <style>
    @media (max-width: 768px) {
        .stTabs {
            overflow-x: auto;
            -webkit-overflow-scrolling: touch;
            scrollbar-width: none; /* Firefox */
            -ms-overflow-style: none; /* IE/Edge */
        }
        
        .stTabs::-webkit-scrollbar {
            display: none; /* Chrome/Safari */
        }
        
        .stTabs [role="tab"] {
            min-width: 120px;
            padding: 12px 16px;
            font-size: 0.95em;
            white-space: nowrap;
        }
        
        .stTabs [role="tab"][aria-selected="true"] {
            border-bottom: 3px solid #1976D2;
            font-weight: 600;
        }
    }
    </style>
    """, unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4 = st.tabs([
        "🦠 Theo Nhiễm Trùng",
        "💊 Theo Nhóm Thuốc",
        "🔄 Quản lý Kháng sinh",
        "🔧 Công cụ"
    ])
    
    with tab1:
        # Mobile bottom nav và FAB
        try:
            from antibiotics.mobile_ui import render_mobile_bottom_nav, render_mobile_fab
            render_mobile_bottom_nav(current_tab="infection")
            render_mobile_fab()
        except ImportError:
            pass
        
        render_antibiotics_by_infection_view()
    
    with tab2:
        try:
            from antibiotics.mobile_ui import render_mobile_bottom_nav
            render_mobile_bottom_nav(current_tab="drugs")
        except ImportError:
            pass
        
        render_antibiotics_by_drug_class_view()
    
    with tab3:
        try:
            from antibiotics.mobile_ui import render_mobile_bottom_nav
            render_mobile_bottom_nav(current_tab="stewardship")
        except ImportError:
            pass
        
        render_stewardship_view()
    
    with tab4:
        try:
            from antibiotics.mobile_ui import render_mobile_bottom_nav
            render_mobile_bottom_nav(current_tab="search")
        except ImportError:
            pass
        
        # Optimized Tools tab with card-based layout
        st.markdown("### 🔧 Công cụ")
        st.caption("Các công cụ tra cứu, so sánh và tính toán kháng sinh")
        
        # Card-based layout for tools
        st.markdown("""
        <style>
        .tool-card {
            background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
            border: 2px solid #e0e0e0;
            border-radius: 16px;
            padding: 24px;
            margin-bottom: 20px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            transition: all 0.3s ease;
            cursor: pointer;
        }
        
        .tool-card:hover {
            border-color: #1976D2;
            box-shadow: 0 6px 16px rgba(25,118,210,0.2);
            transform: translateY(-2px);
        }
        
        .tool-card h3 {
            margin: 0 0 8px 0;
            color: #1976D2;
            font-size: 1.4em;
        }
        
        .tool-card p {
            margin: 0;
            color: #666;
            font-size: 0.95em;
        }
        
        @media (max-width: 768px) {
            .tool-card {
                padding: 16px !important;
                margin-bottom: 16px !important;
            }
        }
        </style>
        """, unsafe_allow_html=True)
        
        # Section 1: Tra cứu & Dữ liệu
        st.markdown("#### 🔍 Tra cứu & Dữ liệu")
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="tool-card">
                <h3>💊 Drug Database</h3>
                <p>Tra cứu thông tin chi tiết về kháng sinh: chỉ định, liều dùng, tương tác, chống chỉ định</p>
            </div>
            """, unsafe_allow_html=True)
            if st.button("Mở Drug Database", key="tool_db", use_container_width=True):
                render_database()
        
        with col2:
            st.markdown("""
            <div class="tool-card">
                <h3>🔍 Global Search</h3>
                <p>Tìm kiếm toàn cục trong toàn bộ hệ thống: thuốc, phác đồ, bài viết</p>
            </div>
            """, unsafe_allow_html=True)
            if st.button("Mở Global Search", key="tool_global_search", use_container_width=True):
                st.switch_page("pages/20_🔍_Global_Search.py")
        
        st.markdown("---")
        
        # Section 2: So sánh
        st.markdown("#### 🔬 So sánh")
        col3, col4 = st.columns(2)
        
        with col3:
            st.markdown("""
            <div class="tool-card">
                <h3>📊 So sánh Nhiều Kháng sinh</h3>
                <p>So sánh nhiều kháng sinh cùng lúc: phổ tác dụng, liều dùng, tác dụng phụ</p>
            </div>
            """, unsafe_allow_html=True)
            if st.button("Mở Multi Comparison", key="tool_multi", use_container_width=True):
                render_multi_comparison()
        
        with col4:
            st.markdown("""
            <div class="tool-card">
                <h3>⚖️ So sánh Side-by-Side</h3>
                <p>So sánh chi tiết 2 kháng sinh: bảng so sánh đầy đủ các thông số</p>
            </div>
            """, unsafe_allow_html=True)
            if st.button("Mở Side-by-Side", key="tool_side_by_side", use_container_width=True):
                render_comparison()
        
        st.markdown("---")
        
        # Section 3: Tính toán
        st.markdown("#### 🧮 Tính toán")
        col5, col6 = st.columns(2)
        
        with col5:
            st.markdown("""
            <div class="tool-card">
                <h3>📊 TDM Calculator</h3>
                <p>Tính toán liều và theo dõi nồng độ: Vancomycin, Aminoglycoside</p>
            </div>
            """, unsafe_allow_html=True)
            if st.button("Mở TDM", key="tool_tdm", use_container_width=True):
                st.switch_page("pages/08_📊_TDM.py")
        
        with col6:
            st.markdown("""
            <div class="tool-card">
                <h3>🧮 Dosing Calculator</h3>
                <p>Tính liều kháng sinh: theo cân nặng, chức năng thận, tuổi</p>
            </div>
            """, unsafe_allow_html=True)
            if st.button("Mở Dosing Calculator", key="tool_dosing", use_container_width=True):
                st.switch_page("pages/07_💊_Drug_Database.py")
        
        st.markdown("---")
        
        # Section 4: Phác đồ
        st.markdown("#### 📋 Phác đồ")
        col7, col8 = st.columns(2)
        
        with col7:
            st.markdown("""
            <div class="tool-card">
                <h3>🔄 Treatment Algorithms</h3>
                <p>Phác đồ điều trị theo từng loại nhiễm trùng: CAP, HAP, UTI, Sepsis</p>
            </div>
            """, unsafe_allow_html=True)
            if st.button("Mở Algorithms", key="tool_algorithms", use_container_width=True):
                render_algorithms_page()
        
        with col8:
            st.markdown("""
            <div class="tool-card">
                <h3>🧙 Antibiotic Wizard</h3>
                <p>Trợ lý chọn kháng sinh: nhập thông tin lâm sàng để nhận đề xuất</p>
            </div>
            """, unsafe_allow_html=True)
            if st.button("Mở Wizard", key="tool_wizard", use_container_width=True):
                st.session_state.show_wizard = True
                st.rerun()
        
        st.markdown("---")
        
        # Section 5: Phase 1 New Features
        st.markdown("#### 🆕 Tính Năng Mới (Phase 1)")
        col9, col10 = st.columns(2)
        
        with col9:
            st.markdown("""
            <div class="tool-card">
                <h3>🔍 Allergy Checker</h3>
                <p>Kiểm tra phản ứng chéo giữa các beta-lactam và kháng sinh khác</p>
            </div>
            """, unsafe_allow_html=True)
            if st.button("Mở Allergy Checker", key="tool_allergy", use_container_width=True):
                try:
                    from antibiotics.allergy_checker import render_allergy_checker
                    render_allergy_checker()
                except ImportError:
                    st.error("Tính năng Allergy Checker chưa khả dụng")
        
        with col10:
            st.markdown("""
            <div class="tool-card">
                <h3>📊 Spectrum Charts</h3>
                <p>Biểu đồ phổ tác dụng trực quan cho kháng sinh</p>
            </div>
            """, unsafe_allow_html=True)
            if st.button("Mở Spectrum Charts", key="tool_spectrum", use_container_width=True):
                try:
                    from antibiotics.spectrum_charts import render_spectrum_charts
                    render_spectrum_charts()
                except ImportError:
                    st.error("Tính năng Spectrum Charts chưa khả dụng")
        
        st.markdown("---")
        
        # Section 6: Phase 2 Advanced Features
        st.markdown("#### 🚀 Tính Năng Nâng Cao (Phase 2)")
        col11, col12 = st.columns(2)
        
        with col11:
            st.markdown("""
            <div class="tool-card">
                <h3>🧮 PK/PD Calculator</h3>
                <p>Tính toán AUC/MIC, Time above MIC, Cmax/MIC</p>
            </div>
            """, unsafe_allow_html=True)
            if st.button("Mở PK/PD Calculator", key="tool_pkpd", use_container_width=True):
                try:
                    from antibiotics.pkpd_calculators import render_pkpd_calculator
                    render_pkpd_calculator()
                except ImportError:
                    st.error("Tính năng PK/PD Calculator chưa khả dụng")
        
        with col12:
            st.markdown("""
            <div class="tool-card">
                <h3>💰 Cost Comparison</h3>
                <p>So sánh chi phí điều trị giữa các kháng sinh</p>
            </div>
            """, unsafe_allow_html=True)
            if st.button("Mở Cost Comparison", key="tool_cost", use_container_width=True):
                try:
                    from antibiotics.cost_comparison import render_cost_comparison
                    render_cost_comparison()
                except ImportError:
                    st.error("Tính năng Cost Comparison chưa khả dụng")
        
        st.markdown("---")

        # Section: What's New specific to Antibiotics
        st.markdown("#### 🆕 Có gì mới trong Module Kháng sinh?")
        st.caption("Xem nhanh các cập nhật gần đây cho riêng module Kháng sinh.")
        if st.button("Mở danh sách cập nhật", key="tool_antibiotics_whats_new", use_container_width=True):
            try:
                render_whats_new()
            except Exception:
                st.error("Không thể tải danh sách cập nhật.")
        
        st.markdown("---")
        
        # Section 7: Phase 3 Educational Features
        st.markdown("#### 📚 Tính Năng Giáo Dục (Phase 3)")
        col13, col14 = st.columns(2)
        
        with col13:
            st.markdown("""
            <div class="tool-card">
                <h3>📝 Quizzes</h3>
                <p>Câu hỏi trắc nghiệm về kháng sinh: liều dùng, phổ tác dụng, PK/PD</p>
            </div>
            """, unsafe_allow_html=True)
            if st.button("Mở Quizzes", key="tool_quizzes", use_container_width=True):
                try:
                    from antibiotics.education.quizzes import render_quizzes
                    render_quizzes()
                except ImportError:
                    st.error("Tính năng Quizzes chưa khả dụng")
        
        with col14:
            st.markdown("""
            <div class="tool-card">
                <h3>📚 Case Studies</h3>
                <p>Tình huống lâm sàng thực tế để học cách sử dụng kháng sinh</p>
            </div>
            """, unsafe_allow_html=True)
            if st.button("Mở Case Studies", key="tool_cases", use_container_width=True):
                try:
                    from antibiotics.education.case_studies import render_case_studies
                    render_case_studies()
                except ImportError:
                    st.error("Tính năng Case Studies chưa khả dụng")
        
        st.markdown("---")
        
        # Section 9: Patient Education & Toxicity Management
        st.markdown("#### 👥 Giáo Dục Bệnh Nhân & Xử Trí Độc Tính")
        col15, col16 = st.columns(2)
        
        with col15:
            st.markdown("""
            <div class="tool-card">
                <h3>📚 Patient Education</h3>
                <p>Tài liệu hướng dẫn dùng thuốc cho bệnh nhân: cách dùng, tác dụng phụ, cảnh báo</p>
            </div>
            """, unsafe_allow_html=True)
            if st.button("Mở Patient Education", key="tool_patient_edu", use_container_width=True):
                try:
                    from antibiotics.patient_education import render_patient_education_checker
                    render_patient_education_checker()
                except ImportError:
                    st.error("Tính năng Patient Education chưa khả dụng")
        
        with col16:
            st.markdown("""
            <div class="tool-card">
                <h3>⚠️ Toxicity Management</h3>
                <p>Hướng dẫn xử trí độc tính: triệu chứng, theo dõi, xử trí, phòng ngừa</p>
            </div>
            """, unsafe_allow_html=True)
            if st.button("Mở Toxicity Management", key="tool_toxicity", use_container_width=True):
                try:
                    from antibiotics.toxicity_management import render_toxicity_checker
                    render_toxicity_checker()
                except ImportError:
                    st.error("Tính năng Toxicity Management chưa khả dụng")
        
        st.markdown("---")
        
        # Section 8: Phase 4 Integration Features
        st.markdown("#### 🔗 Tích Hợp & Phân tích (Phase 4)")
        col15, col16, col17 = st.columns(3)
        
        with col15:
            st.markdown("""
            <div class="tool-card">
                <h3>🏥 Formulary Checker</h3>
                <p>Kiểm tra kháng sinh có trong formulary và tình trạng hạn chế</p>
            </div>
            """, unsafe_allow_html=True)
            if st.button("Mở Formulary", key="tool_formulary", use_container_width=True):
                try:
                    from antibiotics.formulary import render_formulary_checker
                    render_formulary_checker()
                except ImportError:
                    st.error("Tính năng Formulary chưa khả dụng")
        
        with col16:
            st.markdown("""
            <div class="tool-card">
                <h3>📊 Analytics</h3>
                <p>Theo dõi lịch sử sử dụng và thống kê về kháng sinh</p>
            </div>
            """, unsafe_allow_html=True)
            if st.button("Mở Analytics", key="tool_analytics", use_container_width=True):
                try:
                    from antibiotics.analytics import render_analytics
                    render_analytics()
                except ImportError:
                    st.error("Tính năng Analytics chưa khả dụng")
        
        with col17:
            st.markdown("""
            <div class="tool-card">
                <h3>📴 Offline Mode</h3>
                <p>Chế độ offline và PWA support</p>
            </div>
            """, unsafe_allow_html=True)
            if st.button("ℹ️ Thông tin PWA", key="tool_pwa_info", use_container_width=True):
                st.info("""
                **PWA (Progressive Web App) Features:**
                - Cài đặt như ứng dụng trên điện thoại
                - Hoạt động offline (một phần)
                - Tải nhanh hơn với caching
                - Thông báo khi có cập nhật
                
                **Để cài đặt:**
                - Trên Chrome/Edge: Nhấn menu → "Cài đặt ứng dụng"
                - Trên Safari iOS: Nhấn Share → "Thêm vào Màn hình chính"
                """)

        st.markdown("---")

        # Section 10: Antibiogram (Phase 1)
        st.markdown("#### 🧫 Antibiogram (Phase 1)")
        st.caption("Kháng thuốc theo bệnh viện (demo) để hỗ trợ chọn kháng sinh kinh nghiệm")
        if st.button("Mở Antibiogram", key="tool_antibiogram", use_container_width=True):
            try:
                from antibiotics.antibiogram import render_antibiogram_view
                render_antibiogram_view()
            except ImportError:
                st.error("Tính năng Antibiogram chưa khả dụng")
else:
    # Fallback to old UI if new components not available
    st.warning("⚠️ New UI components not available. Using legacy interface.")
    
    # Default to database view if new UI not available
    render_database()

# ========== FOOTER ==========
render_standard_footer(disclaimer=False)

