"""
RSS News Integration Component
RSS feed integration for medical news
"""

import streamlit as st
from typing import List, Dict, Optional
from datetime import datetime
import xml.etree.ElementTree as ET


def parse_rss_feed(feed_url: str) -> List[Dict[str, str]]:
    """
    Parse RSS feed and return list of news items
    
    Args:
        feed_url: RSS feed URL
    
    Returns:
        List of news item dicts with 'title', 'link', 'description', 'pub_date'
    """
    try:
        import requests
        
        response = requests.get(feed_url, timeout=10)
        response.raise_for_status()
        
        root = ET.fromstring(response.content)
        
        items = []
        for item in root.findall('.//item'):
            title = item.find('title')
            link = item.find('link')
            description = item.find('description')
            pub_date = item.find('pubDate')
            
            items.append({
                'title': title.text if title is not None else 'No title',
                'link': link.text if link is not None else '',
                'description': description.text if description is not None else '',
                'pub_date': pub_date.text if pub_date is not None else ''
            })
        
        return items
    except Exception as e:
        st.error(f"Error parsing RSS feed: {str(e)}")
        return []


def render_rss_news_feed(
    feed_url: str,
    max_items: int = 10,
    title: str = "📰 Medical News",
    feed_key: str = None
) -> None:
    """
    Render RSS news feed
    
    Args:
        feed_url: RSS feed URL
        max_items: Maximum number of items to show
        title: Section title
        feed_key: Unique key for this feed (for button keys)
    """
    st.markdown(f"### {title}")
    
    # Generate unique key for button
    button_key = f"refresh_rss_{feed_key or feed_url.replace('/', '_').replace(':', '_')}"
    
    if st.button("🔄 Làm mới", key=button_key):
        # Clear cache for this specific feed
        cache_key = f"rss_cache_{feed_url}"
        if cache_key in st.session_state:
            del st.session_state[cache_key]
        st.rerun()
    
    # Cache RSS feed
    cache_key = f"rss_cache_{feed_url}"
    if cache_key not in st.session_state:
        with st.spinner("Đang tải tin tức..."):
            items = parse_rss_feed(feed_url)
            st.session_state[cache_key] = {
                'items': items,
                'timestamp': datetime.now()
            }
    
    cached_data = st.session_state.get(cache_key, {})
    items = cached_data.get('items', [])
    timestamp = cached_data.get('timestamp')
    
    if items:
        st.caption(f"Cập nhật lần cuối: {timestamp.strftime('%Y-%m-%d %H:%M:%S') if timestamp else 'N/A'}")
        
        for item in items[:max_items]:
            with st.expander(f"📰 {item['title']}", expanded=False):
                st.markdown(f"**Mô tả:** {item.get('description', 'N/A')[:200]}...")
                if item.get('link'):
                    st.markdown(f"[Đọc thêm]({item['link']})")
                if item.get('pub_date'):
                    st.caption(f"Ngày đăng: {item['pub_date']}")
    else:
        st.info("Không có tin tức hoặc không thể tải RSS feed")


def render_multiple_rss_feeds(
    feeds: Dict[str, str],
    max_items_per_feed: int = 5
) -> None:
    """
    Render multiple RSS feeds
    
    Args:
        feeds: Dict of {feed_name: feed_url}
        max_items_per_feed: Max items per feed
    """
    tabs = st.tabs(list(feeds.keys()))
    
    for idx, (feed_name, feed_url) in enumerate(feeds.items()):
        with tabs[idx]:
            render_rss_news_feed(
                feed_url=feed_url,
                max_items=max_items_per_feed,
                title=f"📰 {feed_name}",
                feed_key=feed_name  # Use feed name as unique key
            )


# Common medical news RSS feeds
MEDICAL_NEWS_FEEDS = {
    "Medscape": "https://www.medscape.com/feeds/rss/headlines",
    "NEJM": "https://www.nejm.org/action/showFeed?type=etoc&feed=rss&jc=nejm",
    "JAMA": "https://jamanetwork.com/rss/site_1/1.xml",
    "BMJ": "https://www.bmj.com/rss/current.xml",
}


__all__ = [
    'parse_rss_feed',
    'render_rss_news_feed',
    'render_multiple_rss_feeds',
    'MEDICAL_NEWS_FEEDS',
]

