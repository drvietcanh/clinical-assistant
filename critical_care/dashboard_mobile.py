"""
Mobile-Optimized Dashboard for Critical Care
Responsive dashboard optimized for mobile devices
"""

import streamlit as st
from components.ui.mobile_components import (
    render_mobile_button,
    render_bottom_navigation,
    render_quick_action_bar,
    detect_mobile_device
)
from components.ui.dark_mode import apply_theme_styles, render_theme_switcher
from critical_care.dashboard import render_critical_care_dashboard
from critical_care.clinical_alerts import render_alerts_summary


def render_mobile_dashboard():
    """Render mobile-optimized dashboard"""
    apply_theme_styles()
    
    is_mobile = detect_mobile_device()
    
    # Theme switcher in sidebar
    with st.sidebar:
        render_theme_switcher()
    
    # Mobile-specific layout
    if is_mobile:
        st.markdown("""
        <style>
        .main {
            padding: 8px;
        }
        .stButton>button {
            min-height: 48px;
            font-size: 16px;
            width: 100%;
        }
        input, select, textarea {
            font-size: 16px !important;
        }
        .stMetric {
            padding: 12px;
        }
        </style>
        """, unsafe_allow_html=True)
    
    # Main dashboard content
    st.markdown("## 🏠 Critical Care Dashboard")
    
    # Alerts summary - Mobile optimized
    alerts_summary = render_alerts_summary()
    if alerts_summary and alerts_summary.get('total', 0) > 0:
        if is_mobile:
            # Stack vertically on mobile
            st.metric("🚨 Nghiêm trọng", alerts_summary.get('critical', 0))
            st.metric("⚠️ Cảnh báo", alerts_summary.get('warning', 0))
            st.metric("ℹ️ Thông tin", alerts_summary.get('info', 0))
            st.metric("📊 Tổng cộng", alerts_summary.get('total', 0))
        else:
            # Horizontal layout on desktop
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("🚨 Nghiêm trọng", alerts_summary.get('critical', 0))
            with col2:
                st.metric("⚠️ Cảnh báo", alerts_summary.get('warning', 0))
            with col3:
                st.metric("ℹ️ Thông tin", alerts_summary.get('info', 0))
            with col4:
                st.metric("📊 Tổng cộng", alerts_summary.get('total', 0))
    
    st.markdown("---")
    
    # Quick actions - Mobile optimized
    st.markdown("### ⚡ Truy cập nhanh")
    
    if is_mobile:
        # Single column on mobile
        quick_actions = [
            {"icon": "💧", "label": "Fluid Therapy", "key": "fluid", "tooltip": "Tính toán dịch truyền"},
            {"icon": "💉", "label": "Vasopressors", "key": "vaso", "tooltip": "Hướng dẫn liều"},
            {"icon": "🫁", "label": "Ventilator", "key": "vent", "tooltip": "Quản lý máy thở"},
            {"icon": "💤", "label": "Sedation", "key": "sed", "tooltip": "An thần & giảm đau"},
            {"icon": "🦠", "label": "Sepsis", "key": "sepsis", "tooltip": "Protocol nhiễm trùng huyết"},
            {"icon": "📊", "label": "Scoring", "key": "score", "tooltip": "Hệ thống đánh giá"},
        ]
        
        render_quick_action_bar(quick_actions, columns=2)
    else:
        # Use standard dashboard for desktop
        render_critical_care_dashboard()
    
    st.markdown("---")
    
    # Bottom navigation for mobile
    if is_mobile:
        nav_items = [
            {"icon": "🏠", "label": "Dashboard", "key": "dashboard"},
            {"icon": "🫁", "label": "Ventilator", "key": "ventilator"},
            {"icon": "📊", "label": "Scoring", "key": "scoring"},
            {"icon": "⚙️", "label": "Settings", "key": "settings"}
        ]
        
        # Note: Bottom navigation requires JavaScript, simplified version here
        st.markdown("### 📱 Navigation")
        cols = st.columns(4)
        for idx, item in enumerate(nav_items):
            with cols[idx]:
                if st.button(item['icon'], key=f"nav_{item['key']}", use_container_width=True):
                    st.session_state['critical_care_tool_selection'] = item['label']
                    st.rerun()
