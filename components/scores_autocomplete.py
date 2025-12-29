"""
Scores Autocomplete Component
Provides autocomplete and suggestions for search
"""

import streamlit as st
from typing import List, Dict, Tuple, Optional
from scores.config import SCORES_BY_SPECIALTY


def get_all_scores_flat() -> List[Dict]:
    """Get all scores as flat list with metadata"""
    all_scores = []
    for specialty, scores in SCORES_BY_SPECIALTY.items():
        for score_id, score_info in scores.items():
            all_scores.append({
                "specialty": specialty,
                "score_id": score_id,
                "name": score_info.get("name", ""),
                "desc": score_info.get("desc", ""),
                "status": score_info.get("status", "✅"),
                "is_daily_use": "DÙNG HÀNG NGÀY" in (score_info.get("desc", "") or "")
            })
    return all_scores


def search_scores(query: str, limit: int = 10) -> List[Dict]:
    """
    Search scores with fuzzy matching.
    
    Args:
        query: Search query
        limit: Maximum results to return
    
    Returns:
        List of matching scores with relevance score
    """
    if not query or len(query) < 2:
        return []
    
    query_lower = query.lower().strip()
    all_scores = get_all_scores_flat()
    results = []
    
    for score in all_scores:
        relevance = 0
        
        # Exact match in score_id (highest priority)
        if score["score_id"].lower() == query_lower:
            relevance += 100
        elif query_lower in score["score_id"].lower():
            relevance += 50
        
        # Match in name
        if query_lower in score["name"].lower():
            relevance += 30
            # Bonus for starting with query
            if score["name"].lower().startswith(query_lower):
                relevance += 20
        
        # Match in description
        if query_lower in (score["desc"] or "").lower():
            relevance += 10
        
        # Match in specialty
        if query_lower in score["specialty"].lower():
            relevance += 5
        
        # Daily use bonus
        if score["is_daily_use"]:
            relevance += 2
        
        if relevance > 0:
            results.append({
                **score,
                "relevance": relevance
            })
    
    # Sort by relevance (descending)
    results.sort(key=lambda x: x["relevance"], reverse=True)
    
    return results[:limit]


def get_popular_searches() -> List[str]:
    """Get list of popular search terms"""
    return [
        "Wells",
        "CHA2DS2-VASc",
        "SOFA",
        "APACHE",
        "GCS",
        "CURB-65",
        "NEWS2",
        "MEWS",
        "qSOFA",
        "TIMI",
        "GRACE",
        "HAS-BLED",
        "ASCVD",
        "eGFR",
        "BMI"
    ]


def get_recent_searches() -> List[str]:
    """Get recent searches from session state"""
    return st.session_state.get('recent_searches', [])


def add_to_recent_searches(query: str):
    """Add search query to recent searches"""
    if 'recent_searches' not in st.session_state:
        st.session_state['recent_searches'] = []
    
    # Remove if exists
    if query in st.session_state['recent_searches']:
        st.session_state['recent_searches'].remove(query)
    
    # Add to front
    st.session_state['recent_searches'].insert(0, query)
    
    # Keep only last 10
    st.session_state['recent_searches'] = st.session_state['recent_searches'][:10]


def render_autocomplete_suggestions(
    query: str,
    max_suggestions: int = 5
):
    """
    Render autocomplete suggestions based on query.
    
    Args:
        query: Current search query
        max_suggestions: Maximum suggestions to show
    """
    if not query or len(query) < 2:
        # Show popular searches
        popular = get_popular_searches()
        if popular:
            st.caption("💡 Tìm kiếm phổ biến:")
            cols = st.columns(min(5, len(popular)))
            for idx, term in enumerate(popular[:5]):
                with cols[idx % 5]:
                    if st.button(term, key=f"popular_{term}", use_container_width=True):
                        st.session_state['search_query'] = term
                        st.rerun()
        
        # Show recent searches
        recent = get_recent_searches()
        if recent:
            st.caption("🕐 Tìm kiếm gần đây:")
            for term in recent[:5]:
                if st.button(f"🔍 {term}", key=f"recent_{term}", use_container_width=True):
                    st.session_state['search_query'] = term
                    st.rerun()
        return
    
    # Get suggestions
    suggestions = search_scores(query, limit=max_suggestions)
    
    if suggestions:
        st.caption(f"💡 Gợi ý ({len(suggestions)}):")
        for suggestion in suggestions:
            label = f"{suggestion['name']}"
            if suggestion['is_daily_use']:
                label += " ⭐"
            
            if st.button(
                label,
                key=f"suggestion_{suggestion['score_id']}",
                use_container_width=True,
                help=f"{suggestion['specialty']} • {suggestion['desc'][:50]}..."
            ):
                # Set search query and navigate
                st.session_state['search_query'] = suggestion['name']
                st.session_state['navigate_to_specialty'] = suggestion['specialty']
                st.session_state['navigate_to_score'] = suggestion['score_id']
                add_to_recent_searches(suggestion['name'])
                st.rerun()


def render_search_with_autocomplete(
    label: str = "Tìm kiếm",
    placeholder: str = "Nhập từ khóa...",
    key: str = "search"
) -> str:
    """
    Render search input with autocomplete suggestions.
    
    Returns:
        Search query string
    """
    # Get initial value from session state if exists
    initial_value = st.session_state.get(key, "")
    
    # Search input
    query = st.text_input(
        label,
        value=initial_value,
        placeholder=placeholder,
        key=key
    ).strip()
    
    # Show suggestions below
    if query:
        render_autocomplete_suggestions(query)
    else:
        render_autocomplete_suggestions("")  # Show popular/recent
    
    return query

