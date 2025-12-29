"""
Medical News & Updates Module
Aggregates and displays latest medical news from RSS feeds
"""

import streamlit as st
from utils.page_helper import setup_page, render_standard_footer
from news.aggregator import (
    fetch_latest_news,
    get_news_by_category,
    get_cached_news
)
from news.rss_feeds import get_all_categories

# Standard page setup
setup_page(
    page_title="Tin tức y khoa",
    page_icon="📰",
    description="Tin tức y khoa mới nhất từ các nguồn uy tín"
)

# ========== SIDEBAR ==========
with st.sidebar:
    st.header("📰 Tin tức y khoa")
    st.caption("Module **Tin tức y khoa** – cập nhật tin tức và nghiên cứu mới nhất.")
    
    # Category filter
    categories = ["Tất cả"] + get_all_categories()
    selected_category = st.selectbox(
        "Lọc theo chuyên khoa:",
        categories,
        key="news_category_filter"
    )
    
    # Number of items
    num_items = st.slider(
        "Số lượng tin:",
        min_value=10,
        max_value=50,
        value=20,
        step=5,
        key="news_num_items"
    )
    
    # Refresh button
    if st.button("🔄 Làm mới", use_container_width=True):
        st.cache_data.clear()
        st.rerun()
    
    st.markdown("---")
    st.info("""
    **📰 Medical News & Updates:**
    - Tin tức y khoa từ **Medscape**, **Healthline**, **Medical News Today**
    - Nghiên cứu mới từ **PubMed**
    - Cập nhật từ **NEJM**
    - Phân loại theo chuyên khoa
    
    **💡 Lưu ý:**
    - Tin tức được cập nhật tự động từ RSS feeds
    - Cache 1 giờ để tối ưu hiệu suất
    - Click vào tiêu đề để đọc bài viết đầy đủ
    """)

# ========== MAIN CONTENT ==========

st.markdown("## 📰 Tin tức y khoa mới nhất")
st.markdown("""
**Cập nhật tin tức và nghiên cứu y khoa từ các nguồn uy tín**

Tin tức được tổng hợp từ các nguồn: Medscape, Healthline, Medical News Today, PubMed, NEJM
""")

# Loading indicator
with st.spinner("Đang tải tin tức..."):
    # Fetch news
    category = None if selected_category == "Tất cả" else selected_category
    news_items = fetch_latest_news(limit=num_items, category=category)

if news_items:
    st.success(f"✅ Tìm thấy {len(news_items)} tin tức")
    
    # Display news items
    for i, item in enumerate(news_items, 1):
        with st.container():
            # News card
            col1, col2 = st.columns([4, 1])
            
            with col1:
                st.markdown(f"### {i}. {item['title']}")
                
                # Summary
                summary = item.get('summary', '')
                if summary:
                    # Clean HTML tags from summary
                    import re
                    summary_clean = re.sub('<[^<]+?>', '', summary)
                    summary_clean = summary_clean[:300] + "..." if len(summary_clean) > 300 else summary_clean
                    st.markdown(summary_clean)
                
                # Metadata
                metadata_cols = st.columns(4)
                with metadata_cols[0]:
                    st.caption(f"📅 {item.get('published', 'N/A')}")
                with metadata_cols[1]:
                    st.caption(f"📰 {item.get('source', 'Unknown')}")
                with metadata_cols[2]:
                    category_badge = item.get('category', 'General')
                    st.caption(f"🏷️ {category_badge}")
                with metadata_cols[3]:
                    if item.get('link'):
                        st.markdown(f"[🔗 Đọc thêm]({item['link']})")
            
            st.markdown("---")
else:
    st.warning("Không tìm thấy tin tức. Vui lòng thử lại sau.")
    st.info("💡 Có thể do lỗi kết nối hoặc RSS feeds tạm thời không khả dụng.")

# Additional information
st.markdown("---")
st.markdown("### 📚 Nguồn tin tức")
st.markdown("""
**Các nguồn tin tức được sử dụng:**

1. **Medscape** - Tin tức y khoa toàn diện
   - General Medical News
   - Cardiology, Infectious Diseases, Oncology, Neurology

2. **Healthline** - Tin tức sức khỏe

3. **Medical News Today** - Tin tức y khoa

4. **PubMed** - Nghiên cứu mới nhất từ cơ sở dữ liệu y khoa

5. **NEJM** - New England Journal of Medicine updates

**Lưu ý:**
- Tin tức được cập nhật tự động từ RSS feeds
- Cache 1 giờ để tối ưu hiệu suất
- Click vào link "Đọc thêm" để đọc bài viết đầy đủ trên website gốc
- Một số RSS feeds có thể yêu cầu đăng nhập để đọc bài viết đầy đủ
""")

# Footer
render_standard_footer(disclaimer=True)

