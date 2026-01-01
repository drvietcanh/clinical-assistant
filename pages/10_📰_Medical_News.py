"""
Medical News Page
Displays curated medical news and updates.
"""

import streamlit as st
from utils.page_helper import setup_page, render_standard_footer
from components.news_logic import get_medical_news
import webbrowser

# Standard page setup with mobile optimizations
setup_page(
    page_title="Tin tức Y khoa",
    page_icon="📰",
    description="Cập nhật hướng dẫn điều trị và tin tức y tế mới nhất",
    mobile_header=True
)

st.title("📰 Tin tức Y khoa")
st.caption("Cập nhật từ Bộ Y Tế, WHO và các tổ chức uy tín.")

# Fetch Data
with st.spinner("Đang tải tin tức..."):
    news_data = get_medical_news()

# UI Layout
tab1, tab2 = st.tabs(["🇻🇳 Tin Việt Nam (Nỗi bật)", "🌍 Tin Quốc tế (Mới nhất)"])

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
        
    if valid_news:
        for item in valid_news:
            render_news_card(item)
    else:
        if not errors:
             st.info("Đang cập nhật tin quốc tế...")

# Sidebar
with st.sidebar:
    st.success("Tự động cập nhật mỗi giờ.")
    st.markdown("---")
    st.markdown("**Nguồn:**")
    st.markdown("- Cục Y tế dự phòng (VNCDC)")
    st.markdown("- Bộ Y tế Việt Nam (MOH)")
    st.markdown("- WHO & CDC US")

render_standard_footer()
