"""
Main Menu Hero Section Component
Modern hero section with welcome banner, quick stats, and announcement banner
"""

import streamlit as st
from datetime import datetime
from config.calculators import ALL_CALCULATORS
from config.app_config import APP_CONFIG


def render_hero_section():
    """Render hero section with greeting, date, and quick stats"""
    # Dynamic greeting based on time of day
    current_hour = datetime.now().hour
    if 5 <= current_hour < 12:
        greeting = "Chào buổi sáng"
        emoji = "🌅"
    elif 12 <= current_hour < 18:
        greeting = "Chào buổi chiều"
        emoji = "☀️"
    else:
        greeting = "Chào buổi tối"
        emoji = "🌙"
    
    # Format date in Vietnamese
    now = datetime.now()
    date_str = f"{now.day} tháng {now.month}, {now.year}"
    day_of_week = ["Thứ hai", "Thứ ba", "Thứ tư", "Thứ năm", "Thứ sáu", "Thứ bảy", "Chủ nhật"][now.weekday()]
    
    # Get stats
    total_calc = st.session_state.get('total_calculations', 0)
    total_fav = len(st.session_state.get('favorites', []))
    total_calculators = len(ALL_CALCULATORS)
    
    # Hero section HTML - properly formatted
    html_content = f"""<div class="hero-section">
<div class="hero-content">
<p class="hero-date">{day_of_week}, {date_str}</p>
<h1 class="hero-greeting">{emoji} {greeting}, Bác sĩ!</h1>
<div class="hero-stats-grid">
<div class="hero-stat-card">
<p class="hero-stat-label">Tổng Calculators</p>
<p class="hero-stat-value">{total_calculators}</p>
</div>
<div class="hero-stat-card">
<p class="hero-stat-label">Tính toán hôm nay</p>
<p class="hero-stat-value">{total_calc}</p>
</div>
<div class="hero-stat-card">
<p class="hero-stat-label">Yêu thích</p>
<p class="hero-stat-value">{total_fav}</p>
</div>
<div class="hero-stat-card">
<p class="hero-stat-label">Phiên bản</p>
<p class="hero-stat-value" style="font-size: 1.5rem;">{APP_CONFIG.get('version', '2.0')}</p>
</div>
</div>
</div>
</div>"""
    st.markdown(html_content, unsafe_allow_html=True)


def render_announcement_banner(announcement_text: str = None, dismissible: bool = True):
    """Render announcement banner with optional dismiss functionality"""
    if announcement_text is None:
        announcement_text = '<strong>🆕 Cập nhật mới:</strong> Đã thêm 712 thuốc với dữ liệu đầy đủ. Giao diện mới hiện đại hơn, tối ưu cho mobile. <a href="#" style="color: white; text-decoration: underline;">Xem chi tiết</a>'
    
    # Clean up announcement text - remove extra whitespace
    announcement_text = announcement_text.strip()
    
    banner_key = "announcement_banner_dismissed"
    
    if dismissible and st.session_state.get(banner_key, False):
        return
    
    col1, col2 = st.columns([10, 1])
    
    with col1:
        # Properly formatted HTML without extra whitespace
        html_content = f'<div class="announcement-banner"><span class="announcement-badge">NEW</span><div class="announcement-content">{announcement_text}</div></div>'
        st.markdown(html_content, unsafe_allow_html=True)
    
    with col2:
        if dismissible:
            if st.button("✕", key="dismiss_announcement", help="Đóng thông báo"):
                st.session_state[banner_key] = True
                st.rerun()


def render_quick_stats_summary():
    """Render quick stats summary cards"""
    total_calculators = len(ALL_CALCULATORS)
    total_favorites = len(st.session_state.get('favorites', []))
    total_recent = len(st.session_state.get('recently_used', []))
    session_calcs = st.session_state.get('total_calculations', 0)
    
    # Count calculators by category
    categories = {}
    for calc_id, calc_info in ALL_CALCULATORS.items():
        category = calc_info.get('category', 'Khác')
        categories[category] = categories.get(category, 0) + 1
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("📊 Calculators", total_calculators, f"{len(categories)} nhóm")
    
    with col2:
        st.metric("⭐ Yêu thích", total_favorites, "Đã lưu" if total_favorites > 0 else "Thêm thêm")
    
    with col3:
        st.metric("🕐 Gần đây", total_recent, "Đã dùng" if total_recent > 0 else "Chưa có")
    
    with col4:
        st.metric("🔢 Tính toán", session_calcs, "Phiên này")
