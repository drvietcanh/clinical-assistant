"""
Score Links from Content Component
Helper function for rendering score links from articles and protocols
"""

import streamlit as st
from config.article_protocol_score_mapping import (
    get_scores_for_article,
    get_scores_for_protocol,
    get_score_info,
    has_scores
)


def render_score_links_from_article(article_id: str):
    """
    Render links to related scores from an article.
    
    Args:
        article_id: Article ID (filename without .md extension)
    """
    try:
        scores = get_scores_for_article(article_id)
        if not scores:
            return
        
        with st.expander("📊 Scores liên quan", expanded=False):
            st.markdown("""
            **Các scores/calculators hữu ích cho chủ đề này:**
            
            Click vào link để mở trực tiếp calculator tương ứng.
            """)
            
            for score_info in scores:
                score_id = score_info.get("score_id")
                specialty = score_info.get("specialty")
                reason = score_info.get("reason", "")
                
                # Get score details
                score_details = get_score_info(score_id, specialty)
                if not score_details:
                    continue
                
                score_name = score_details.get("name", score_id)
                score_desc = score_details.get("desc", "")
                
                col1, col2 = st.columns([3, 1])
                
                with col1:
                    st.markdown(f"**{score_name}**")
                    if score_desc:
                        st.caption(score_desc)
                    if reason:
                        st.caption(f"💡 {reason}")
                
                with col2:
                    if st.button("🔗 Mở", key=f"score_link_{article_id}_{score_id}", use_container_width=True, type="secondary"):
                        st.session_state['auto_select_score'] = score_id
                        st.session_state['auto_select_specialty'] = specialty
                        st.switch_page("pages/01_📊_Scores.py")
                
                st.markdown("---")
                
    except Exception as e:
        # Silently fail if mapping lookup fails
        pass


def render_score_links_from_protocol(protocol_function: str):
    """
    Render links to related scores from a protocol.
    
    Args:
        protocol_function: Protocol function name (e.g., "render_sepsis")
    """
    try:
        scores = get_scores_for_protocol(protocol_function)
        if not scores:
            return
        
        with st.expander("📊 Scores liên quan", expanded=False):
            st.markdown("""
            **Các scores/calculators hữu ích cho protocol này:**
            
            Click vào link để mở trực tiếp calculator tương ứng.
            """)
            
            for score_info in scores:
                score_id = score_info.get("score_id")
                specialty = score_info.get("specialty")
                reason = score_info.get("reason", "")
                
                # Get score details
                score_details = get_score_info(score_id, specialty)
                if not score_details:
                    continue
                
                score_name = score_details.get("name", score_id)
                score_desc = score_details.get("desc", "")
                
                col1, col2 = st.columns([3, 1])
                
                with col1:
                    st.markdown(f"**{score_name}**")
                    if score_desc:
                        st.caption(score_desc)
                    if reason:
                        st.caption(f"💡 {reason}")
                
                with col2:
                    if st.button("🔗 Mở", key=f"score_link_{protocol_function}_{score_id}", use_container_width=True, type="secondary"):
                        st.session_state['auto_select_score'] = score_id
                        st.session_state['auto_select_specialty'] = specialty
                        st.switch_page("pages/01_📊_Scores.py")
                
                st.markdown("---")
                
    except Exception as e:
        # Silently fail if mapping lookup fails
        pass

