"""
Enhanced Search Component
Advanced search with autocomplete and highlighting
"""

import streamlit as st
import re
from typing import List, Optional, Set
from patient_education.models import PatientEducationTopic


def get_search_suggestions(
    query: str,
    topics: List[PatientEducationTopic],
    max_suggestions: int = 5
) -> List[dict]:
    """
    Get search suggestions based on query
    
    Returns:
        List of dicts with 'title', 'category', 'match_type'
    """
    if not query or len(query) < 2:
        return []
    
    query_lower = query.lower()
    suggestions = []
    
    # Exact title matches
    for topic in topics:
        if query_lower in topic.title_vn.lower():
            suggestions.append({
                'title': topic.title_vn,
                'category': topic.category,
                'match_type': 'title'
            })
            if len(suggestions) >= max_suggestions:
                break
    
    # Partial matches if not enough
    if len(suggestions) < max_suggestions:
        for topic in topics:
            if topic.title_vn not in [s['title'] for s in suggestions]:
                words = query_lower.split()
                if any(word in topic.title_vn.lower() for word in words):
                    suggestions.append({
                        'title': topic.title_vn,
                        'category': topic.category,
                        'match_type': 'partial'
                    })
                    if len(suggestions) >= max_suggestions:
                        break
    
    return suggestions[:max_suggestions]


def highlight_search_terms(text: str, query: str) -> str:
    """
    Highlight search terms in text (for markdown)
    
    Args:
        text: Text to highlight
        query: Search query
        
    Returns:
        Text with highlighted terms
    """
    if not query or not text:
        return text
    
    # Split query into words
    words = query.lower().split()
    
    # Highlight each word
    highlighted = text
    for word in words:
        if len(word) >= 2:  # Only highlight words with 2+ characters
            pattern = re.compile(re.escape(word), re.IGNORECASE)
            highlighted = pattern.sub(
                lambda m: f'<mark style="background: #FFF59D; padding: 2px 4px; border-radius: 3px;">{m.group()}</mark>',
                highlighted
            )
    
    return highlighted


def filter_topics_by_search(
    topics: List[PatientEducationTopic],
    query: str
) -> List[PatientEducationTopic]:
    """
    Filter topics by search query
    
    Args:
        topics: List of topics
        query: Search query
        
    Returns:
        Filtered list of topics
    """
    if not query or not query.strip():
        return topics
    
    query_lower = query.lower()
    filtered = []
    
    for topic in topics:
        # Search in title (Vietnamese and English)
        if (query_lower in topic.title_vn.lower() or 
            query_lower in topic.title.lower() or
            query_lower in topic.content.lower()):
            filtered.append(topic)
    
    return filtered


def render_enhanced_search(
    topics: List[PatientEducationTopic],
    placeholder: str = "Tìm kiếm bệnh, thuốc, hướng dẫn...",
    show_filters: bool = True,
    show_suggestions: bool = True,
    key: str = "patient_edu_search"
) -> str:
    """
    Render enhanced search component
    
    Args:
        topics: List of all topics for suggestions
        placeholder: Search placeholder
        show_filters: Show filter buttons
        show_suggestions: Show autocomplete suggestions
        key: Streamlit key
        
    Returns:
        Search query string
    """
    # Search input
    col1, col2 = st.columns([4, 1])
    
    with col1:
        search_query = st.text_input(
            "🔍",
            placeholder=placeholder,
            key=key,
            label_visibility="collapsed"
        )
    
    with col2:
        if show_filters:
            show_advanced = st.button("🔎 Nâng cao", use_container_width=True)
        else:
            show_advanced = False
    
    # Advanced filters (in expander)
    if show_advanced:
        with st.expander("🔎 Tìm kiếm nâng cao", expanded=True):
            col1, col2, col3 = st.columns(3)
            
            with col1:
                category_filter = st.selectbox(
                    "Chủ đề:",
                    ["Tất cả"] + sorted(set(t.category for t in topics)),
                    key=f"{key}_category"
                )
            
            with col2:
                printable_only = st.checkbox(
                    "Chỉ tài liệu có thể in",
                    key=f"{key}_printable"
                )
            
            with col3:
                search_in_content = st.checkbox(
                    "Tìm trong nội dung",
                    value=True,
                    key=f"{key}_content"
                )
            
            # Apply filters
            if category_filter != "Tất cả":
                topics = [t for t in topics if t.category == category_filter]
            if printable_only:
                topics = [t for t in topics if t.printable]
    
    # Show suggestions if query is short
    if show_suggestions and search_query and len(search_query) >= 2:
        suggestions = get_search_suggestions(search_query, topics, max_suggestions=5)
        if suggestions:
            st.caption(f"💡 Gợi ý: {', '.join([s['title'] for s in suggestions[:3]])}")
    
    return search_query


def render_search_stats(
    total: int,
    filtered: int,
    query: Optional[str] = None
):
    """Render search statistics"""
    if query and query.strip():
        if filtered == 0:
            st.warning(f"Không tìm thấy kết quả cho '{query}'. Vui lòng thử từ khóa khác.")
        else:
            st.success(f"Tìm thấy {filtered} / {total} tài liệu cho '{query}'")
    else:
        st.info(f"Hiển thị {filtered} tài liệu")
