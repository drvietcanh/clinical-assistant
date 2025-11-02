"""
Enhanced Search Component
Global search with fuzzy matching, category filters, and smart suggestions
"""

import streamlit as st
from config.calculators import ALL_CALCULATORS
from typing import List, Tuple, Dict
from difflib import SequenceMatcher


def _fuzzy_match(query: str, text: str, threshold: float = 0.6) -> float:
    """
    Simple fuzzy matching using SequenceMatcher
    
    Args:
        query: Search query
        text: Text to match against
        threshold: Minimum similarity threshold
    
    Returns:
        Similarity score (0-1)
    """
    query_lower = query.lower()
    text_lower = text.lower()
    
    # Exact match gets highest score
    if query_lower in text_lower:
        return 1.0
    
    # Word-level matching
    query_words = query_lower.split()
    text_words = text_lower.split()
    
    word_matches = sum(1 for qw in query_words if any(qw in tw or tw in qw for tw in text_words))
    word_score = word_matches / len(query_words) if query_words else 0
    
    # Character-level similarity
    char_score = SequenceMatcher(None, query_lower, text_lower).ratio()
    
    # Combined score (weighted)
    combined_score = (word_score * 0.6 + char_score * 0.4)
    
    return combined_score if combined_score >= threshold else 0.0


def search_calculators(
    query: str,
    use_fuzzy: bool = True,
    category_filter: str = None,
    boost_recent: bool = True,
    max_results: int = 20
) -> List[Tuple[str, Dict, float]]:
    """
    Enhanced search with fuzzy matching and category filtering
    
    Args:
        query: Search query
        use_fuzzy: Enable fuzzy matching
        category_filter: Filter by category
        boost_recent: Boost recently used calculators
        max_results: Maximum number of results
    
    Returns:
        List of (calc_id, calc_info, score) tuples sorted by relevance
    """
    if not query:
        return []
    
    query = query.strip()
    query_lower = query.lower()
    results = []
    
    # Get recently used for boosting
    recently_used = st.session_state.get('recently_used', [])
    
    for calc_id, calc_info in ALL_CALCULATORS.items():
        # Category filter
        if category_filter and calc_info.get('category', '').lower() != category_filter.lower():
            continue
        
        name = calc_info.get('name', '')
        category = calc_info.get('category', '')
        
        score = 0.0
        
        # Exact match (highest priority)
        if query_lower in name.lower():
            score = 1.0
        elif query_lower in category.lower():
            score = 0.9
        # Fuzzy matching
        elif use_fuzzy:
            name_score = _fuzzy_match(query, name)
            category_score = _fuzzy_match(query, category)
            score = max(name_score, category_score * 0.7)
        
        # Boost recently used
        if boost_recent and calc_id in recently_used:
            score = min(1.0, score + 0.1)
        
        # Only include if score is above threshold
        if score > 0.3:  # Lower threshold for fuzzy results
            results.append((calc_id, calc_info, score))
    
    # Sort by score (descending)
    results.sort(key=lambda x: x[2], reverse=True)
    
    return results[:max_results]


def get_search_suggestions(query: str, max_suggestions: int = 5) -> List[str]:
    """
    Get search suggestions based on query
    
    Args:
        query: Search query
        max_suggestions: Maximum suggestions
    
    Returns:
        List of suggested search terms
    """
    if not query or len(query) < 2:
        # Popular searches
        return ["SOFA", "CHA2DS2VASc", "APACHE", "NEWS2", "ASCVD"]
    
    query_lower = query.lower()
    suggestions = []
    
    # Find similar calculator names
    seen = set()
    for calc_id, calc_info in ALL_CALCULATORS.items():
        name = calc_info.get('name', '')
        if query_lower in name.lower() and name not in seen:
            suggestions.append(name)
            seen.add(name)
            if len(suggestions) >= max_suggestions:
                break
    
    return suggestions


def get_all_categories() -> List[str]:
    """Get all unique categories from calculators"""
    categories = set()
    for calc_info in ALL_CALCULATORS.values():
        category = calc_info.get('category', '')
        if category:
            categories.add(category)
    return sorted(list(categories))


def render_search():
    """Render enhanced search bar with fuzzy matching, filters, and suggestions"""
    # Header
    st.markdown("### 🔍 Tìm Kiếm Nhanh")
    st.caption("Tìm kiếm trong tất cả calculators, xét nghiệm, và protocols")
    
    # Search controls
    col_search, col_filter = st.columns([4, 1])
    
    with col_search:
        search_query = st.text_input(
            "🔎 Nhập từ khóa...",
            placeholder="Ví dụ: CHA2DS2VASc, troponin, sepsis, SOFA...",
            help="Gõ tên calculator, chuyên khoa, hoặc từ khóa bất kỳ",
            key="search_box",
            label_visibility="collapsed"
        )
    
    with col_filter:
        # Category filter
        all_categories = ["Tất cả"] + get_all_categories()
        selected_category = st.selectbox(
            "Lọc theo:",
            all_categories,
            index=0,
            key="search_category_filter",
            label_visibility="collapsed"
        )
        category_filter = None if selected_category == "Tất cả" else selected_category
    
    # Search options
    with st.expander("⚙️ Tùy chọn tìm kiếm", expanded=False):
        use_fuzzy = st.checkbox("Tìm kiếm mờ (Fuzzy)", value=True, help="Tìm kết quả tương tự ngay cả khi chính tả không chính xác")
        boost_recent = st.checkbox("Ưu tiên đã dùng gần đây", value=True, help="Hiển thị các calculator đã dùng gần đây ở đầu")
    
    # Display results
    if search_query:
        results = search_calculators(
            search_query,
            use_fuzzy=use_fuzzy,
            category_filter=category_filter,
            boost_recent=boost_recent,
            max_results=20
        )
        
        if results:
            st.success(f"✅ **{len(results)}** kết quả tìm thấy")
            
            # Display results using calculator cards
            num_cols = min(3, len(results))
            cols = st.columns(num_cols)
            
            for idx, (calc_id, calc_info, score) in enumerate(results[:9]):  # Show max 9 results
                with cols[idx % num_cols]:
                    is_fav = calc_id in st.session_state.get('favorites', [])
                    is_recent = calc_id in st.session_state.get('recently_used', [])
                    
                    # Use new calculator card component
                    from .ui.cards import render_calculator_card
                    render_calculator_card(
                        calc_id=calc_id,
                        name=calc_info['name'],
                        category=calc_info.get('category', ''),
                        icon=calc_info.get('icon', '📊'),
                        page=calc_info.get('page', 'Scores'),
                        is_favorite=is_fav,
                        is_recent=is_recent,
                        show_favorite_button=True,
                        show_open_button=True
                    )
            
            # Show "show more" if there are more results
            if len(results) > 9:
                st.info(f"💡 Có thêm {len(results) - 9} kết quả. Hãy tinh chỉnh từ khóa để xem thêm.")
        else:
            # Show suggestions when no results
            suggestions = get_search_suggestions(search_query)
            if suggestions:
                st.warning(f"""
                **❌ Không tìm thấy kết quả cho: "{search_query}"**
                
                💡 **Gợi ý tìm kiếm:**
                """)
                # Show suggestions as clickable buttons
                suggestion_cols = st.columns(min(5, len(suggestions)))
                for idx, suggestion in enumerate(suggestions[:5]):
                    with suggestion_cols[idx]:
                        if st.button(suggestion, key=f"suggestion_{idx}", use_container_width=True):
                            st.session_state.search_box = suggestion
                            st.rerun()
            else:
                st.warning(f"""
                **❌ Không tìm thấy kết quả cho: "{search_query}"**
                
                💡 **Thử:**
                - Từ khóa khác: tim mạch, cấp cứu, xét nghiệm, thuốc
                - Kiểm tra chính tả
                - Tắt "Tìm kiếm mờ" nếu đang bật
                """)
    else:
        # Show popular searches and suggestions when no query
        popular_searches = ["SOFA", "CHA2DS2VASc", "APACHE", "NEWS2", "ASCVD"]
        
        st.info("💡 **Mẹo tìm kiếm:** Gõ tên calculator (ví dụ: SOFA, CHA2DS2VASc) hoặc chuyên khoa (ví dụ: tim mạch, cấp cứu)")
        
        st.markdown("**🔝 Tìm kiếm phổ biến:**")
        pop_cols = st.columns(5)
        for idx, pop_search in enumerate(popular_searches):
            with pop_cols[idx]:
                if st.button(pop_search, key=f"pop_search_{idx}", use_container_width=True):
                    st.session_state.search_box = pop_search
                    st.rerun()
    
    st.markdown("---")

