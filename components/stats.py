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
    col1.metric("Tổng Calculators", total_calcs, "Sẵn sàng ✓")
    col2.metric("Yêu Thích", total_favorites, f"+{total_favorites}" if total_favorites > 0 else "Thêm thêm")
    col3.metric("Gần Đây", total_recent, "Phiên này")
    col4.metric("Tính toán", session_calcs, "Lần")
    col5.metric("Modules", "5", "Tất cả đang hoạt động ✅")
    
    st.markdown("---")


def render_updates():
    """Render recent updates section"""
    st.subheader("🆕 Cập Nhật Mới Nhất")
    
    with st.expander("📅 2025-10-29 - Version 2.0.0 🔥 MAJOR UPDATE"):
        st.markdown("""
        ### 🎉 Tính Năng Mới:
        
        **1. ✅ Tìm kiếm & Điều hướng:**
        - 🔍 Tìm kiếm toàn cục - Tìm calculator nhanh chóng
        - ⭐ Hệ thống yêu thích - Lưu calculators yêu thích
        - 🕐 Đã sử dụng gần đây - Theo dõi lịch sử sử dụng
        - 🚀 Modules truy cập nhanh - Truy cập nhanh
        
        **2. ✅ Chuyển đổi đơn vị (Đơn vị SI mặc định):**
        - Creatinine: µmol/L ↔ mg/dL
        - Glucose: mmol/L ↔ mg/dL  
        - Cholesterol: mmol/L ↔ mg/dL
        - Triglycerides: mmol/L ↔ mg/dL
        - Bilirubin: µmol/L ↔ mg/dL
        - BUN/Urea: mmol/L ↔ mg/dL
        
        **3. ✅ Việt hóa:**
        - 100% giao diện tiếng Việt
        - Tất cả diễn giải bằng tiếng Việt
        - Hướng dẫn lâm sàng tiếng Việt
        
        **4. ✅ Module Xét nghiệm (9 panel):**
        - CBC, BMP, CMP, LFT
        - Lipid Panel, Cardiac Markers
        - Coagulation, Thyroid, ABG
        - Tự động diễn giải
        
        **5. ✅ Kiến trúc cải tiến:**
        - Thiết kế module 100%
        - Hiệu suất nhanh hơn
        - Trải nghiệm di động tốt hơn
        - UI/UX chuyên nghiệp
        
        ### 🎯 Tiếp theo:
        - 🚧 Kiểm tra tương tác thuốc
        - 🚧 Tạo chẩn đoán phân biệt
        - 🚧 Thêm calculators (70+ đã lên kế hoạch)
        """)
    
    with st.expander("📅 2025-10-28 - Version 1.0.0"):
        st.markdown("""
        - ✅ Triển khai Streamlit ban đầu
        - ✅ Calculators cơ bản (34 công cụ)
        - ✅ Kiến trúc module
        - ✅ Tự động triển khai GitHub
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

