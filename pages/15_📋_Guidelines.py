"""
Unified Guidelines Page
Combines Guidelines Tracker and Guideline Viewer functionality
"""

import streamlit as st
from utils.page_helper import setup_page, render_standard_footer

# Standard page setup
setup_page(
    page_title="Guidelines",
    page_icon="📋",
    description="Theo dõi, xem và tìm kiếm clinical guidelines"
)

# Hero Section
st.markdown("### 📋 Clinical Guidelines")
st.caption("Theo dõi, xem và tìm kiếm các hướng dẫn thực hành lâm sàng từ các tổ chức quốc tế")

st.markdown("---")

# Tabs for different views
tab1, tab2, tab3 = st.tabs(["📋 Tracker", "📖 Viewer", "📰 News"])

with tab1:
    # Guidelines Tracker functionality - redirect to original page
    st.info("📋 **Guidelines Tracker** - Theo dõi và cập nhật guidelines")
    st.markdown("""
    Chức năng Guidelines Tracker cho phép bạn:
    - Tìm kiếm và lọc guidelines theo tổ chức, chuyên khoa, năm
    - Theo dõi các guidelines mới và cập nhật
    - Xem chi tiết từng guideline với clinical pearls
    """)
    
    if st.button("Mở Guidelines Tracker", use_container_width=True, type="primary"):
        st.switch_page("pages/15_📋_Guidelines_Tracker.py")

with tab2:
    # Guideline Viewer functionality - redirect to original page
    st.info("📖 **Guideline Viewer** - Xem và tìm kiếm guidelines với decision trees")
    st.markdown("""
    Chức năng Guideline Viewer cho phép bạn:
    - Xem guidelines với decision trees
    - Tìm kiếm và lọc guidelines
    - Xem thống kê và insights
    """)
    
    if st.button("Mở Guideline Viewer", use_container_width=True, type="primary"):
        st.switch_page("pages/18_📖_Guideline_Viewer.py")

with tab3:
    # Medical News (integrated from Medical News page)
    try:
        from components.news_logic import get_medical_news
        st.markdown("### 📰 Tin tức Y khoa")
        st.caption("Cập nhật từ Bộ Y Tế, WHO và các tổ chức uy tín")
        
        with st.spinner("Đang tải tin tức..."):
            news_data = get_medical_news()
        
        if news_data:
            for item in news_data[:10]:  # Show top 10
                with st.expander(f"📰 {item.get('title', 'Không có tiêu đề')}"):
                    st.markdown(f"**Nguồn:** {item.get('source', 'N/A')}")
                    st.markdown(f"**Ngày:** {item.get('date', 'N/A')}")
                    st.markdown(item.get('summary', 'Không có tóm tắt'))
                    if item.get('link'):
                        st.markdown(f"[Đọc thêm →]({item['link']})")
        else:
            st.info("Không có tin tức mới.")
    except Exception as e:
        st.error(f"Lỗi tải tin tức: {e}")
        if st.button("Mở Medical News", use_container_width=True):
            st.switch_page("pages/10_📰_Medical_News.py")

st.markdown("---")

# Footer
render_standard_footer()
