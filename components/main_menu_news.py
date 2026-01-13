"""
Main Menu News & Updates Component
Display latest updates, news feed, and announcements
"""

import streamlit as st
from datetime import datetime


def render_news_updates_section():
    """Render news and updates section"""
    st.markdown("### 📰 Cập nhật & Tin tức")
    
    # Manual updates (can be replaced with RSS feed later)
    updates = [
        {
            'date': '2025-01-06',
            'title': '🆕 Giao diện Main Menu mới',
            'content': 'Trang chủ đã được tối ưu hóa với thiết kế hiện đại, tìm kiếm nâng cao, và nhiều tính năng tiện dụng hơn.',
            'type': 'feature'
        },
        {
            'date': '2025-01-05',
            'title': '💊 Database thuốc mở rộng',
            'content': 'Đã thêm 712 thuốc với dữ liệu đầy đủ về liều dùng, tương tác, và chống chỉ định.',
            'type': 'update'
        },
        {
            'date': '2025-01-04',
            'title': '📊 Thống kê sử dụng mới',
            'content': 'Thêm dashboard thống kê với biểu đồ và phân tích xu hướng sử dụng.',
            'type': 'feature'
        },
        {
            'date': '2025-01-03',
            'title': '🎨 Tối ưu mobile',
            'content': 'Giao diện đã được tối ưu hóa cho thiết bị di động với responsive design.',
            'type': 'improvement'
        },
    ]
    
    # Display updates in expandable sections
    for update in updates[:3]:  # Show latest 3
        with st.expander(f"{update['title']} - {update['date']}", expanded=False):
            st.markdown(update['content'])
            type_emoji = {
                'feature': '✨',
                'update': '🔄',
                'improvement': '🎨',
                'bugfix': '🐛'
            }.get(update['type'], '📌')
            st.caption(f"{type_emoji} {update['type'].title()}")
    
    # Try to load RSS news if available
    try:
        from components.news_logic import fetch_rss_news
        st.markdown("---")
        st.markdown("#### 📡 Tin tức y khoa")
        
        rss_news = fetch_rss_news(max_items=3)
        if rss_news:
            for news_item in rss_news:
                st.markdown(f"**{news_item.get('title', 'N/A')}**")
                st.caption(f"{news_item.get('source', '')} - {news_item.get('date', '')}")
                if news_item.get('summary'):
                    st.markdown(news_item['summary'][:200] + "...")
                if news_item.get('link'):
                    st.markdown(f"[Đọc thêm]({news_item['link']})")
                st.markdown("---")
        else:
            st.info("Không có tin tức mới")
    except ImportError:
        # News logic not available, skip RSS
        pass
    except Exception as e:
        st.caption(f"Không thể tải tin tức: {str(e)}")


def render_announcements():
    """Render important announcements"""
    announcements = [
        {
            'text': '⚠️ Lưu ý: Công cụ này chỉ mục đích hỗ trợ quyết định lâm sàng, không thay thế đánh giá của bác sĩ.',
            'type': 'warning',
            'dismissible': False
        }
    ]
    
    for announcement in announcements:
        if announcement['type'] == 'warning':
            st.warning(announcement['text'])
        elif announcement['type'] == 'info':
            st.info(announcement['text'])
        elif announcement['type'] == 'success':
            st.success(announcement['text'])
