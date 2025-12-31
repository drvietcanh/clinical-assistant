"""
Homepage Dashboard for Doctors
Phase 1 UI Modernization - Modern "Smart Dashboard" Design
"""

import streamlit as st
from datetime import datetime

# Import Phase 1 components
try:
    from components.morning_briefing import render_morning_briefing
    from components.quick_actions import render_quick_actions
    from components.recently_used import render_recently_used
    from components.favorites import render_favorites
except ImportError:
    # Fallback if components not available
    render_morning_briefing = None
    render_quick_actions = None
    render_recently_used = None
    render_favorites = None


def render_homepage_doctor():
    """
    Renders the modern "Smart Dashboard" for doctors (Phase 1 - 2025 Design)
    Following the "Calm & Critical" design philosophy
    """
    
    # Section 1: Morning Briefing (Hero Banner)
    if render_morning_briefing:
        render_morning_briefing()
    else:
        # Fallback: Simple greeting
        current_hour = datetime.now().hour
        greeting = "Chào buổi sáng" if 5 <= current_hour < 12 else "Chào buổi chiều" if 12 <= current_hour < 18 else "Chào buổi tối"
        st.markdown(f"## {greeting}, Bác sĩ! 👋")
    
    st.markdown("---")
    
    # Section 2: Quick Actions (4 Big Buttons)
    if render_quick_actions:
        render_quick_actions(max_items=4, layout="cards")
    else:
        # Fallback: Simple buttons
        st.markdown("### ⚡ Truy cập nhanh")
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            if st.button("🧮 Tính CrCl", use_container_width=True):
                st.switch_page("pages/01_📊_Scores.py")
        with col2:
            if st.button("💊 Kháng Sinh", use_container_width=True):
                st.switch_page("pages/02_💊_Antibiotics.py")
        with col3:
            if st.button("⚠️ Tương tác", use_container_width=True):
                st.switch_page("pages/07_💊_Drug_Database.py")
        with col4:
            if st.button("🫁 Hồi sức", use_container_width=True):
                st.switch_page("pages/09_🫁_Critical_Care.py")
    
    st.markdown("---")
    
    # Section 3: Recently Viewed & Favorites (Two columns)
    col_left, col_right = st.columns(2)
    
    with col_left:
        st.markdown("### 🕐 Đã xem gần đây")
        if render_recently_used:
            render_recently_used(max_items=5)
        else:
            # Fallback
            recently_used = st.session_state.get('recently_used', [])
            if recently_used:
                for item in recently_used[:5]:
                    st.markdown(f"- {item}")
            else:
                st.info("Chưa có lịch sử xem")
    
    with col_right:
        st.markdown("### ⭐ Yêu thích")
        if render_favorites:
            render_favorites(max_items=5)
        else:
            # Fallback
            favorites = st.session_state.get('favorites', [])
            if favorites:
                for item in favorites[:5]:
                    st.markdown(f"- {item}")
            else:
                st.info("Chưa có mục yêu thích")
