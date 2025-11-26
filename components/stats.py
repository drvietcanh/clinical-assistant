"""
Stats Component
Display system statistics, updates, and tips
"""

import streamlit as st
from config.calculators import ALL_CALCULATORS


def render_stats():
    """Render system statistics"""
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


def render_updates():
    """Render recent updates section"""
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


def render_tips():
    """Render usage tips"""
    st.subheader("💡 Mẹo sử dụng")
    
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

