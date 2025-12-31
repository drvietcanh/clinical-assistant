"""
Morning Briefing Component for Homepage Dashboard
Part of Phase 1 UI Modernization
"""

import streamlit as st
from datetime import datetime

def render_morning_briefing():
    """
    Renders dynamic greeting and quick stats for the homepage dashboard
    Following the "Calm & Critical" design philosophy
    """
    
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
    date_str = datetime.now().strftime("%d tháng %m, %Y")
    day_of_week = ["Thứ hai", "Thứ ba", "Thứ tư", "Thứ năm", "Thứ sáu", "Thứ bảy", "Chủ nhật"][datetime.now().weekday()]
    
    # Get values first
    total_calc = st.session_state.get('total_calculations', 0)
    total_fav = len(st.session_state.get('favorites', []))
    
    # Hero section with gradient background
    import textwrap
    st.markdown(textwrap.dedent(f"""
    <div style="
        background: linear-gradient(135deg, #00897B 0%, #00695C 100%);
        padding: 2rem;
        border-radius: 16px;
        margin-bottom: 2rem;
        color: white;
        box-shadow: 0 4px 12px rgba(0, 137, 123, 0.3);
    ">
        <p style="
            color: rgba(255,255,255,0.9);
            font-size: 0.9rem;
            margin-bottom: 0.5rem;
            font-weight: 500;
        ">{day_of_week}, {date_str}</p>
        <h1 style="
            font-size: 2.5rem;
            font-weight: 700;
            margin: 0 0 1.5rem 0;
            letter-spacing: -0.02em;
        ">{emoji} {greeting}, Bác sĩ!</h1>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 1rem;">
            <div style="background: rgba(255,255,255,0.15); padding: 1rem; border-radius: 12px; backdrop-filter: blur(10px);">
                <p style="font-size: 0.85rem; opacity: 0.9; margin: 0;">Tổng tính toán</p>
                <p style="font-size: 2rem; font-weight: 700; margin: 0.25rem 0 0 0;">{total_calc}</p>
            </div>
            <div style="background: rgba(255,255,255,0.15); padding: 1rem; border-radius: 12px; backdrop-filter: blur(10px);">
                <p style="font-size: 0.85rem; opacity: 0.9; margin: 0;">Yêu thích</p>
                <p style="font-size: 2rem; font-weight: 700; margin: 0.25rem 0 0 0;">{total_fav}</p>
            </div>
            <div style="background: rgba(255,255,255,0.15); padding: 1rem; border-radius: 12px; backdrop-filter: blur(10px);">
                <p style="font-size: 0.85rem; opacity: 0.9; margin: 0;">Cập nhật mới</p>
                <p style="font-size: 2rem; font-weight: 700; margin: 0.25rem 0 0 0;">5</p>
            </div>
        </div>
    </div>
    """), unsafe_allow_html=True)
    
    # What's New section
    st.markdown("### 📰 Điểm tin nổi bật")
    st.info("""
    **Cập nhật mới nhất:**
    - 📘 **Guideline 2025:** Đã cập nhật phác đồ điều trị Tăng huyết áp theo JNC 9
    - 💊 **Thuốc mới:** Thêm 712 thuốc với dữ liệu đầy đủ (vượt mục tiêu 666)
    - ⚠️ **Cảnh báo:** Lưu ý tương tác thuốc giữa Clarithromycin và Simvastatin
    - 🎨 **UI/UX:** Giao diện mới hiện đại hơn, tối ưu cho mobile
    """)
