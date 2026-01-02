"""
Dashboard Widgets Component
Personalized widgets for unified dashboard
"""

import streamlit as st
from typing import List, Dict, Optional
from datetime import datetime, timedelta


def render_quick_access_widget(max_items: int = 6) -> None:
    """
    Render quick access widget with most-used tools
    
    Args:
        max_items: Maximum number of items to show
    """
    st.markdown("### ⚡ Truy cập nhanh")
    
    # Get most used tools from session state
    calculator_usage = st.session_state.get('calculator_usage', {})
    recently_used = st.session_state.get('recently_used', [])
    
    # Combine and sort by usage
    all_tools = {}
    for calc_id, count in calculator_usage.items():
        all_tools[calc_id] = {'count': count, 'type': 'calculator'}
    
    for item in recently_used:
        if item not in all_tools:
            all_tools[item] = {'count': 1, 'type': 'recent'}
        else:
            all_tools[item]['count'] += 1
    
    # Sort by usage count
    sorted_tools = sorted(all_tools.items(), key=lambda x: x[1]['count'], reverse=True)[:max_items]
    
    if sorted_tools:
        cols = st.columns(min(3, len(sorted_tools)))
        for idx, (tool_id, info) in enumerate(sorted_tools):
            with cols[idx % 3]:
                st.button(
                    f"📊 {tool_id}",
                    key=f"quick_{tool_id}",
                    use_container_width=True
                )
    else:
        st.info("Chưa có công cụ nào được sử dụng. Bắt đầu sử dụng để xem ở đây!")


def render_recent_activity_feed(max_items: int = 10) -> None:
    """
    Render recent activity feed
    
    Args:
        max_items: Maximum number of activities to show
    """
    st.markdown("### 🕐 Hoạt động gần đây")
    
    # Get activity from session state
    activity_log = st.session_state.get('activity_log', [])
    
    if activity_log:
        for activity in activity_log[:max_items]:
            timestamp = activity.get('timestamp', '')
            action = activity.get('action', '')
            item = activity.get('item', '')
            
            st.markdown(f"**{timestamp}** - {action}: **{item}**")
    else:
        st.info("Chưa có hoạt động nào")


def render_personalized_recommendations() -> None:
    """
    Render personalized recommendations based on usage patterns
    """
    st.markdown("### 💡 Gợi ý cho bạn")
    
    # Get usage patterns
    calculator_usage = st.session_state.get('calculator_usage', {})
    favorites = st.session_state.get('favorites', [])
    
    recommendations = []
    
    # Recommend based on specialty usage
    if 'sofa' in calculator_usage or 'qsofa' in calculator_usage:
        recommendations.append({
            'title': '🫁 Critical Care Tools',
            'description': 'Bạn thường dùng scores hồi sức. Xem thêm Critical Care module?',
            'link': 'pages/09_🫁_Critical_Care.py'
        })
    
    if 'cha2ds2vasc' in calculator_usage or 'hasbled' in calculator_usage:
        recommendations.append({
            'title': '❤️ Cardiology Protocols',
            'description': 'Bạn quan tâm tim mạch. Xem protocols tim mạch?',
            'link': 'pages/04_📋_Protocols.py'
        })
    
    if not favorites:
        recommendations.append({
            'title': '⭐ Đánh dấu yêu thích',
            'description': 'Đánh dấu các calculator bạn thường dùng để truy cập nhanh hơn',
            'link': None
        })
    
    if recommendations:
        for rec in recommendations[:3]:
            with st.expander(rec['title'], expanded=False):
                st.markdown(rec['description'])
                if rec['link']:
                    if st.button("Xem ngay", key=f"rec_{rec['title']}"):
                        st.switch_page(rec['link'])
    else:
        st.info("Chưa đủ dữ liệu để đưa ra gợi ý. Tiếp tục sử dụng app để nhận gợi ý!")


def render_statistics_widget() -> None:
    """
    Render statistics widget
    """
    st.markdown("### 📊 Thống kê")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        total_calcs = st.session_state.get('total_calculations', 0)
        st.metric("Tổng tính toán", total_calcs)
    
    with col2:
        favorites_count = len(st.session_state.get('favorites', []))
        st.metric("Yêu thích", favorites_count)
    
    with col3:
        recently_count = len(st.session_state.get('recently_used', []))
        st.metric("Gần đây", recently_count)


def render_dashboard_layout(
    show_quick_access: bool = True,
    show_activity: bool = True,
    show_recommendations: bool = True,
    show_stats: bool = True
) -> None:
    """
    Render complete personalized dashboard layout
    
    Args:
        show_quick_access: Show quick access widget
        show_activity: Show activity feed
        show_recommendations: Show recommendations
        show_stats: Show statistics
    """
    # Two column layout
    col_left, col_right = st.columns([2, 1])
    
    with col_left:
        if show_quick_access:
            render_quick_access_widget()
            st.markdown("---")
        
        if show_activity:
            render_recent_activity_feed()
            st.markdown("---")
        
        if show_recommendations:
            render_personalized_recommendations()
    
    with col_right:
        if show_stats:
            render_statistics_widget()
            st.markdown("---")
        
        # Additional widgets can go here
        st.markdown("### 📌 Ghi chú nhanh")
        notes = st.text_area(
            "Ghi chú:",
            value=st.session_state.get('dashboard_notes', ''),
            height=150,
            key="dashboard_notes_input"
        )
        if notes != st.session_state.get('dashboard_notes', ''):
            st.session_state['dashboard_notes'] = notes


__all__ = [
    'render_quick_access_widget',
    'render_recent_activity_feed',
    'render_personalized_recommendations',
    'render_statistics_widget',
    'render_dashboard_layout',
]

