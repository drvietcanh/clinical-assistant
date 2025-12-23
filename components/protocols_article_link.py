"""
Protocol Article Link Component
Helper function for rendering article links from protocols
"""

import streamlit as st
from config.article_protocol_mapping import get_article_deep_link


def render_article_link(protocol_function: str):
    """
    Render link to related article if exists.
    
    Args:
        protocol_function: Protocol function name (e.g., "render_sepsis")
    """
    try:
        article_info = get_article_deep_link(protocol_function)
        if article_info:
            page_path, article_id = article_info
            with st.expander("📚 Đọc thêm kiến thức chuyên sâu", expanded=False):
                st.markdown(f"""
                **Bài viết chuyên sâu tương ứng:**
                
                Bài viết này cung cấp kiến thức nền tảng, guideline chi tiết, và giải thích sâu hơn về chủ đề này.
                """)
                col1, col2 = st.columns([1, 5])
                with col1:
                    if st.button("📚 Mở bài viết", key=f"article_link_{protocol_function}", use_container_width=True, type="secondary"):
                        st.session_state['article_to_open'] = article_id
                        st.switch_page(page_path)
                with col2:
                    st.caption(f"*Article: `{article_id}`*")
    except Exception as e:
        # Silently fail if mapping lookup fails
        pass

