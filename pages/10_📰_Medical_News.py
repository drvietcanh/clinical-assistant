"""
Medical News Page
Displays curated medical news and updates.
"""

import streamlit as st
from utils.page_helper import setup_page, render_standard_footer
from components.news_logic import get_medical_news, check_for_new_news, load_news_config
from datetime import datetime
import os

# RSS Feed integration
try:
    from components.rss_news import render_rss_news_feed, render_multiple_rss_feeds, MEDICAL_NEWS_FEEDS
    RSS_AVAILABLE = True
except ImportError:
    RSS_AVAILABLE = False

# Standard page setup with mobile optimizations
setup_page(
    page_title="Tin tức Y khoa",
    page_icon="📰",
    description="Cập nhật hướng dẫn điều trị và tin tức y tế mới nhất",
    mobile_header=True
)

# Load configuration
config = load_news_config()

# Header with refresh button
col_title, col_refresh = st.columns([4, 1])

with col_title:
    st.title("📰 Tin tức Y khoa")
    st.caption("Cập nhật từ Bộ Y Tế, WHO và các tổ chức uy tín.")

with col_refresh:
    st.markdown("<br>", unsafe_allow_html=True)  # Spacing
    if st.button("🔄 Làm mới", use_container_width=True, help="Làm mới tất cả tin tức"):
        # Clear cache
        st.cache_data.clear()
        st.rerun()

# Check if we should auto-refresh
force_refresh = False
if "last_news_update" not in st.session_state:
    force_refresh = True
else:
    last_update = st.session_state.last_news_update
    cache_ttl_minutes = config.get("cache_ttl_minutes", 5)
    time_diff = (datetime.now() - last_update).total_seconds() / 60
    if time_diff > cache_ttl_minutes:
        force_refresh = True

# Fetch Data
with st.spinner("Đang tải tin tức..."):
    news_data = get_medical_news(force_refresh=force_refresh)
    st.session_state.last_news_update = datetime.now()

# Display metadata
metadata = news_data.get("metadata", {})
new_items_count = metadata.get("new_items_count", 0)
last_updated = metadata.get("last_updated")
storage_enabled = metadata.get("storage_enabled", False)

# Show badges and info
info_cols = st.columns(3)
with info_cols[0]:
    if new_items_count > 0:
        st.success(f"✨ {new_items_count} tin mới")
    else:
        st.info("📰 Đã cập nhật")

with info_cols[1]:
    if last_updated:
        try:
            last_update_dt = datetime.fromisoformat(last_updated)
            time_ago = datetime.now() - last_update_dt
            if time_ago.total_seconds() < 3600:
                minutes_ago = int(time_ago.total_seconds() / 60)
                st.caption(f"🕐 Cập nhật: {minutes_ago} phút trước")
            else:
                hours_ago = int(time_ago.total_seconds() / 3600)
                st.caption(f"🕐 Cập nhật: {hours_ago} giờ trước")
        except:
            st.caption(f"🕐 Cập nhật: {last_updated[:10]}")
    else:
        st.caption("🕐 Đang tải...")

with info_cols[2]:
    if storage_enabled:
        st.caption("💾 Lưu trữ: Bật")
    else:
        st.caption("💾 Lưu trữ: Tắt")

# UI Layout
if RSS_AVAILABLE:
    tab1, tab2, tab3 = st.tabs(["🇻🇳 Tin Việt Nam (Nổi bật)", "🌍 Tin Quốc tế (Mới nhất)", "📡 RSS Feeds"])
else:
    tab1, tab2 = st.tabs(["🇻🇳 Tin Việt Nam (Nổi bật)", "🌍 Tin Quốc tế (Mới nhất)"])

# Add filter/search for international news
with tab2:
    filter_col1, filter_col2 = st.columns([3, 1])
    
    with filter_col1:
        search_query = st.text_input("🔍 Tìm kiếm trong tin tức", placeholder="Nhập từ khóa...", key="news_search")
    
    with filter_col2:
        filter_option = st.selectbox(
            "Lọc theo",
            ["Tất cả", "Hôm nay", "Tuần này", "Tháng này"],
            key="news_filter"
        )

def render_news_card(item):
    """Render a single news item as a card"""
    # Simple Card Style
    st.markdown(f"""
    <div style="
        background-color: white;
        padding: 1.25rem;
        border-radius: 10px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        border-left: 4px solid #007bff;
        transition: transform 0.2s;
    ">
        <div style="font-size: 0.9rem; color: #666; margin-bottom: 5px;">
            📅 {item.get('date', 'N/A')} | 🏛️ {item.get('source', 'Unknown')}
        </div>
        <h4 style="margin: 0 0 10px 0; color: #2c3e50; font-weight: 700; line-height: 1.4;">
            {item.get('title', 'No Title')}
        </h4>
        <p style="color: #444; font-size: 0.95rem; margin-bottom: 12px; line-height: 1.5;">
            {item.get('summary', item.get('description', '')[:150] + '...')}
        </p>
        <a href="{item.get('link')}" target="_blank" style="
            text-decoration: none; 
            color: #007bff; 
            font-weight: 600; 
            font-size: 0.9rem;
            display: inline-flex;
            align-items: center;
        ">
            Đọc tiếp ➡️
        </a>
    </div>
    """, unsafe_allow_html=True)

with tab1:
    local_news = news_data.get("local", [])
    if local_news:
        for item in local_news:
            render_news_card(item)
    else:
        st.info("Chưa có tin mới.")

with tab2:
    intl_news = news_data.get("international", [])
    
    # Filter out error items if any for cleaner UI, show error as toast/warning
    valid_news = [n for n in intl_news if not n.get("error")]
    errors = [n for n in intl_news if n.get("error")]
    
    if errors:
        st.warning(f"⚠️ {errors[0]['summary']}")
    
    # Apply search filter
    if search_query:
        search_lower = search_query.lower()
        valid_news = [
            n for n in valid_news
            if search_lower in n.get("title", "").lower() or search_lower in n.get("summary", "").lower()
        ]
    
    # Apply date filter
    if filter_option != "Tất cả":
        from datetime import datetime, timedelta
        now = datetime.now()
        
        if filter_option == "Hôm nay":
            cutoff = now.replace(hour=0, minute=0, second=0, microsecond=0)
        elif filter_option == "Tuần này":
            cutoff = now - timedelta(days=now.weekday())
            cutoff = cutoff.replace(hour=0, minute=0, second=0, microsecond=0)
        elif filter_option == "Tháng này":
            cutoff = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        else:
            cutoff = None
        
        if cutoff:
            filtered_news = []
            for n in valid_news:
                date_str = n.get("pub_date") or n.get("date", "")
                if date_str:
                    try:
                        try:
                            from dateutil import parser
                            item_date = parser.parse(date_str)
                        except ImportError:
                            # Fallback to simple datetime parsing
                            try:
                                item_date = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
                            except:
                                item_date = None
                        
                        if item_date and item_date >= cutoff:
                            filtered_news.append(n)
                        elif item_date is None:
                            # If can't parse, include it
                            filtered_news.append(n)
                    except:
                        # If can't parse, include it
                        filtered_news.append(n)
                else:
                    # If no date, include it
                    filtered_news.append(n)
            valid_news = filtered_news
    
    # Show count
    if search_query or filter_option != "Tất cả":
        st.caption(f"Hiển thị {len(valid_news)}/{len([n for n in intl_news if not n.get('error')])} tin tức")
    
    if valid_news:
        for item in valid_news:
            render_news_card(item)
    else:
        if not errors:
            if search_query or filter_option != "Tất cả":
                st.info("Không tìm thấy tin tức phù hợp với bộ lọc.")
            else:
                st.info("Đang cập nhật tin quốc tế...")

# RSS Feeds tab
if RSS_AVAILABLE:
    with tab3:
        st.markdown("### 📡 RSS Feeds từ Tạp chí Y khoa Quốc tế")
        st.info("Tin tức từ các tạp chí y khoa hàng đầu thế giới")
        
        # Render multiple RSS feeds
        render_multiple_rss_feeds(
            feeds=MEDICAL_NEWS_FEEDS,
            max_items_per_feed=5
        )

# Sidebar
with st.sidebar:
    cache_ttl = config.get("cache_ttl_minutes", 5)
    st.success(f"Tự động cập nhật mỗi {cache_ttl} phút.")
    
    # Show storage stats if available
    try:
        from components.news_storage import get_feed_stats
        stats = get_feed_stats()
        if stats.get("total_items", 0) > 0:
            st.markdown("---")
            st.markdown("**📊 Thống kê:**")
            st.caption(f"Tổng số tin: {stats.get('total_items', 0)}")
            st.caption(f"Số nguồn: {stats.get('total_feeds', 0)}")
            if stats.get("newest_item"):
                st.caption(f"Tin mới nhất: {stats.get('newest_item', '')[:10]}")
    except:
        pass
    
    st.markdown("---")
    st.markdown("**Nguồn:**")
    st.markdown("- Cục Y tế dự phòng (VNCDC)")
    st.markdown("- Bộ Y tế Việt Nam (MOH)")
    st.markdown("- WHO & CDC US")
    if RSS_AVAILABLE:
        st.markdown("---")
        st.markdown("**RSS Feeds:**")
        st.markdown("- Medscape")
        st.markdown("- NEJM")
        st.markdown("- JAMA")
        st.markdown("- BMJ")
    
    # Settings expander
    with st.expander("⚙️ Cài đặt", expanded=False):
        st.caption(f"Cache TTL: {cache_ttl} phút")
        st.caption(f"Giữ lịch sử: {config.get('keep_history_days', 30)} ngày")
        st.caption(f"Số tin tối đa: {config.get('max_total_items', 50)}")
        
        if st.button("🗑️ Xóa cache", use_container_width=True):
            st.cache_data.clear()
            if "last_news_update" in st.session_state:
                del st.session_state.last_news_update
            st.success("✅ Đã xóa cache!")
            st.rerun()

render_standard_footer()
