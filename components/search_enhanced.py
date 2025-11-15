"""
Enhanced Search Component with AI Suggestions
Real-time suggestions, search history, fuzzy matching, and smart ranking
"""

import streamlit as st
from config.calculators import ALL_CALCULATORS
from typing import List, Tuple, Dict, Optional
from difflib import SequenceMatcher
import re

# Try to import rapidfuzz for better fuzzy matching
try:
    from rapidfuzz import fuzz, process
    HAS_RAPIDFUZZ = True
except ImportError:
    HAS_RAPIDFUZZ = False
    # Fallback to difflib
    from difflib import SequenceMatcher


# Popular searches tracking (in session state)
def _init_popular_searches():
    """Initialize popular searches tracking"""
    if 'popular_searches' not in st.session_state:
        st.session_state.popular_searches = {}
    if 'search_history' not in st.session_state:
        st.session_state.search_history = []
    if 'calculator_usage' not in st.session_state:
        st.session_state.calculator_usage = {}


def _track_search(query: str):
    """Track search query usage"""
    _init_popular_searches()
    
    if query:
        query_lower = query.lower().strip()
        
        # Track in popular searches
        if query_lower not in st.session_state.popular_searches:
            st.session_state.popular_searches[query_lower] = 0
        st.session_state.popular_searches[query_lower] += 1
        
        # Track in search history (max 20)
        if query_lower not in st.session_state.search_history:
            st.session_state.search_history.insert(0, query_lower)
            if len(st.session_state.search_history) > 20:
                st.session_state.search_history = st.session_state.search_history[:20]


def _track_calculator_usage(calc_id: str):
    """Track calculator usage frequency"""
    _init_popular_searches()
    
    if calc_id not in st.session_state.calculator_usage:
        st.session_state.calculator_usage[calc_id] = 0
    st.session_state.calculator_usage[calc_id] += 1


def _fuzzy_match_rapidfuzz(query: str, text: str) -> float:
    """Enhanced fuzzy matching using rapidfuzz"""
    if not HAS_RAPIDFUZZ:
        return _fuzzy_match_difflib(query, text)
    
    # Use rapidfuzz for better performance and accuracy
    query_lower = query.lower()
    text_lower = text.lower()
    
    # Exact match gets highest score
    if query_lower == text_lower:
        return 1.0
    
    # Starts with query gets high score
    if text_lower.startswith(query_lower):
        return 0.95
    
    # Contains query gets good score
    if query_lower in text_lower:
        return 0.9
    
    # Use rapidfuzz ratio for similarity
    ratio = fuzz.ratio(query_lower, text_lower) / 100.0
    
    # Use partial ratio for substring matching
    partial_ratio = fuzz.partial_ratio(query_lower, text_lower) / 100.0
    
    # Use token sort ratio for word order independence
    token_sort_ratio = fuzz.token_sort_ratio(query_lower, text_lower) / 100.0
    
    # Combined score (weighted)
    combined_score = max(ratio, partial_ratio * 0.8, token_sort_ratio * 0.7)
    
    return combined_score


def _fuzzy_match_difflib(query: str, text: str, threshold: float = 0.6) -> float:
    """
    Simple fuzzy matching using SequenceMatcher (fallback)
    
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
    if query_lower == text_lower:
        return 1.0
    
    # Starts with query gets high score
    if text_lower.startswith(query_lower):
        return 0.95
    
    # Contains query gets good score
    if query_lower in text_lower:
        return 0.9
    
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


def search_calculators_enhanced(
    query: str,
    use_fuzzy: bool = True,
    category_filter: Optional[str] = None,
    boost_recent: bool = True,
    boost_popular: bool = True,
    max_results: int = 20
) -> List[Tuple[str, Dict, float]]:
    """
    Enhanced search with fuzzy matching, smart ranking, and usage tracking
    
    Args:
        query: Search query
        use_fuzzy: Enable fuzzy matching
        category_filter: Filter by category
        boost_recent: Boost recently used calculators
        boost_popular: Boost popular calculators
        max_results: Maximum number of results
    
    Returns:
        List of (calc_id, calc_info, score) tuples sorted by relevance
    """
    if not query:
        return []
    
    query = query.strip()
    query_lower = query.lower()
    results = []
    
    _init_popular_searches()
    
    # Get recently used for boosting
    recently_used = st.session_state.get('recently_used', [])
    calculator_usage = st.session_state.get('calculator_usage', {})
    
    # Choose fuzzy matching function
    fuzzy_func = _fuzzy_match_rapidfuzz if HAS_RAPIDFUZZ else _fuzzy_match_difflib
    
    for calc_id, calc_info in ALL_CALCULATORS.items():
        # Category filter
        if category_filter and calc_info.get('category', '').lower() != category_filter.lower():
            continue
        
        name = calc_info.get('name', '')
        category = calc_info.get('category', '')
        description = calc_info.get('description', '')
        
        # Build searchable text
        searchable_text = f"{name} {category} {description}".lower()
        
        score = 0.0
        
        # Exact match (highest priority) - name
        if query_lower == name.lower():
            score = 1.0
        elif name.lower().startswith(query_lower):
            score = 0.95
        elif query_lower in name.lower():
            score = 0.9
        # Category match
        elif query_lower == category.lower():
            score = 0.85
        elif category.lower().startswith(query_lower):
            score = 0.8
        elif query_lower in category.lower():
            score = 0.75
        # Fuzzy matching
        elif use_fuzzy:
            name_score = fuzzy_func(query, name)
            category_score = fuzzy_func(query, category)
            description_score = fuzzy_func(query, description) if description else 0.0
            
            # Combined score (weighted: name > category > description)
            score = max(name_score, category_score * 0.7, description_score * 0.5)
        
        # Boost recently used
        if boost_recent and calc_id in recently_used:
            score = min(1.0, score + 0.1)
        
        # Boost popular calculators (based on usage frequency)
        if boost_popular and calc_id in calculator_usage:
            usage_count = calculator_usage[calc_id]
            # Logarithmic boost (diminishing returns)
            boost = min(0.15, 0.05 * (1 + (usage_count // 10)))
            score = min(1.0, score + boost)
        
        # Only include if score is above threshold
        if score > 0.3:  # Lower threshold for fuzzy results
            results.append((calc_id, calc_info, score))
    
    # Sort by score (descending)
    results.sort(key=lambda x: x[2], reverse=True)
    
    return results[:max_results]


def get_search_suggestions_enhanced(
    query: str, 
    max_suggestions: int = 10,
    include_popular: bool = True,
    include_history: bool = True
) -> List[Tuple[str, str, float]]:
    """
    Get enhanced search suggestions with real-time matching
    
    Args:
        query: Search query (can be partial)
        max_suggestions: Maximum number of suggestions
        include_popular: Include popular searches
        include_history: Include search history
    
    Returns:
        List of (suggestion_text, suggestion_type, score) tuples
        suggestion_type: 'calculator', 'popular', 'history', 'category'
    """
    if not query or len(query) < 1:
        # Return popular searches and categories
        suggestions = []
        
        # Popular searches
        if include_popular:
            _init_popular_searches()
            popular = st.session_state.get('popular_searches', {})
            sorted_popular = sorted(popular.items(), key=lambda x: x[1], reverse=True)
            for pop_query, count in sorted_popular[:5]:
                suggestions.append((pop_query, 'popular', count))
        
        # Default popular calculators
        default_popular = ["SOFA", "CHA2DS2VASc", "APACHE", "NEWS2", "ASCVD", "eGFR", "CrCl", "HEART Score"]
        for pop in default_popular:
            if not any(s[0].lower() == pop.lower() for s in suggestions):
                suggestions.append((pop, 'popular', 10))
        
        return suggestions[:max_suggestions]
    
    query_lower = query.lower().strip()
    suggestions = []
    
    _init_popular_searches()
    
    # Choose fuzzy matching function
    fuzzy_func = _fuzzy_match_rapidfuzz if HAS_RAPIDFUZZ else _fuzzy_match_difflib
    
    # 1. Calculator name matches
    seen = set()
    for calc_id, calc_info in ALL_CALCULATORS.items():
        name = calc_info.get('name', '')
        category = calc_info.get('category', '')
        
        # Check name match
        name_lower = name.lower()
        if query_lower in name_lower or (len(query) >= 2 and fuzzy_func(query, name) > 0.6):
            if name not in seen:
                suggestions.append((name, 'calculator', fuzzy_func(query, name)))
                seen.add(name)
        
        # Check category match
        if query_lower in category.lower() and category not in seen:
            suggestions.append((category, 'category', fuzzy_func(query, category)))
            seen.add(category)
        
        if len(suggestions) >= max_suggestions:
            break
    
    # 2. Search history matches
    if include_history:
        search_history = st.session_state.get('search_history', [])
        for hist_query in search_history:
            if query_lower in hist_query.lower() and hist_query not in seen:
                score = fuzzy_func(query, hist_query)
                if score > 0.5:
                    suggestions.append((hist_query, 'history', score))
                    seen.add(hist_query)
                    if len(suggestions) >= max_suggestions:
                        break
    
    # 3. Popular searches matches
    if include_popular:
        popular = st.session_state.get('popular_searches', {})
        for pop_query, count in sorted(popular.items(), key=lambda x: x[1], reverse=True):
            if query_lower in pop_query.lower() and pop_query not in seen:
                score = fuzzy_func(query, pop_query)
                if score > 0.5:
                    # Boost by popularity
                    boosted_score = min(1.0, score + 0.1 * min(count / 10, 1.0))
                    suggestions.append((pop_query, 'popular', boosted_score))
                    seen.add(pop_query)
                    if len(suggestions) >= max_suggestions:
                        break
    
    # Sort by score (descending)
    suggestions.sort(key=lambda x: x[2], reverse=True)
    
    return suggestions[:max_suggestions]


def get_all_categories() -> List[str]:
    """Get all unique categories from calculators"""
    categories = set()
    for calc_info in ALL_CALCULATORS.values():
        category = calc_info.get('category', '')
        if category:
            categories.add(category)
    return sorted(list(categories))


def render_search_enhanced():
    """Render enhanced search bar with real-time suggestions, history, and smart ranking"""
    _init_popular_searches()
    
    # Add keyboard shortcut handler
    st.markdown("""
    <script>
    document.addEventListener('keydown', function(e) {
        // Ctrl+K or Cmd+K to focus search
        if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
            e.preventDefault();
            const searchInput = document.querySelector('input[data-baseweb="input"]');
            if (searchInput) {
                searchInput.focus();
                searchInput.select();
            }
        }
        // Esc to clear search
        if (e.key === 'Escape') {
            const searchInput = document.querySelector('input[data-baseweb="input"]');
            if (searchInput && searchInput.value) {
                searchInput.value = '';
                // Trigger change event
                const event = new Event('input', { bubbles: true });
                searchInput.dispatchEvent(event);
            }
        }
    });
    </script>
    """, unsafe_allow_html=True)
    
    # Search controls with better layout
    col_search, col_filter, col_clear = st.columns([5, 1.5, 0.8])
    
    with col_search:
        search_query = st.text_input(
            "🔎 Tìm kiếm...",
            placeholder="Nhập từ khóa (ví dụ: SOFA, CHA2DS2VASc, tim mạch...) - Nhấn Ctrl+K để focus",
            help="Tìm kiếm calculators, drugs, protocols. Hỗ trợ fuzzy matching và real-time suggestions!",
            key="search_box_enhanced",
            label_visibility="collapsed"
        )
        
        # Track search query
        if search_query:
            _track_search(search_query)
    
    with col_filter:
        # Category filter
        all_categories = ["Tất cả"] + get_all_categories()
        selected_category = st.selectbox(
            "Lọc:",
            all_categories,
            index=0,
            key="search_category_filter_enhanced",
            label_visibility="collapsed",
            help="Lọc theo chuyên khoa"
        )
        category_filter = None if selected_category == "Tất cả" else selected_category
    
    with col_clear:
        if st.button("🗑️", help="Xóa tìm kiếm (Esc)", use_container_width=True, key="clear_search_enhanced"):
            st.session_state.search_box_enhanced = ""
            st.rerun()
    
    # Search options
    col_options1, col_options2, col_options3 = st.columns(3)
    with col_options1:
        use_fuzzy = st.checkbox("🔍 Fuzzy", value=True, help="Tìm kết quả tương tự ngay cả khi chính tả không chính xác", key="fuzzy_search")
    with col_options2:
        boost_recent = st.checkbox("⭐ Ưu tiên gần đây", value=True, help="Hiển thị các calculator đã dùng gần đây ở đầu", key="boost_recent")
    with col_options3:
        boost_popular = st.checkbox("🔥 Ưu tiên phổ biến", value=True, help="Hiển thị các calculator phổ biến ở đầu", key="boost_popular")
    
    # Real-time suggestions (when typing)
    if search_query and len(search_query) >= 1:
        suggestions = get_search_suggestions_enhanced(
            search_query,
            max_suggestions=8,
            include_popular=True,
            include_history=True
        )
        
        if suggestions:
            st.markdown("**💡 Gợi ý:**")
            suggestion_cols = st.columns(min(4, len(suggestions)))
            for idx, (suggestion_text, suggestion_type, score) in enumerate(suggestions[:4]):
                with suggestion_cols[idx]:
                    # Icon based on type
                    icon_map = {
                        'calculator': '📊',
                        'popular': '🔥',
                        'history': '🕐',
                        'category': '📁'
                    }
                    icon = icon_map.get(suggestion_type, '💡')
                    
                    if st.button(f"{icon} {suggestion_text}", key=f"suggestion_{idx}_{suggestion_text}", use_container_width=True):
                        st.session_state.search_box_enhanced = suggestion_text
                        _track_search(suggestion_text)
                        st.rerun()
    
    # Display results
    if search_query:
        results = search_calculators_enhanced(
            search_query,
            use_fuzzy=use_fuzzy,
            category_filter=category_filter,
            boost_recent=boost_recent,
            boost_popular=boost_popular,
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
                    
                    # Track calculator view
                    _track_calculator_usage(calc_id)
                    
                    # Map page name to page path
                    page_name = calc_info.get('page', 'Scores')
                    page_path_map = {
                        'Scores': 'pages/01_📊_Scores.py',
                        'Labs': 'pages/05_🔬_Labs_and_Calculators.py',
                        'Antibiotics': 'pages/02_💊_Antibiotics.py',
                        'Drugs': 'pages/07_💊_Drug_Database.py',
                        'Ventilator': 'pages/03_🫁_Ventilator.py',
                        'Critical Care': 'pages/09_🫁_Critical_Care.py',
                        'Protocols': 'pages/04_📋_Protocols.py',
                        'Diagnosis': 'pages/06_🩺_Diagnosis.py',
                    }
                    page_path = page_path_map.get(page_name, 'pages/01_📊_Scores.py')
                    
                    # Use calculator card component
                    try:
                        from components.ui.cards import render_calculator_card
                        render_calculator_card(
                            calc_id=calc_id,
                            name=calc_info['name'],
                            category=calc_info.get('category', ''),
                            icon=calc_info.get('icon', '📊'),
                            page=page_path,  # Use page path, not page name
                            is_favorite=is_fav,
                            is_recent=is_recent,
                            show_favorite_button=True,
                            show_open_button=True
                        )
                    except ImportError:
                        # Fallback to simple display
                        st.markdown(f"### {calc_info.get('icon', '📊')} {calc_info['name']}")
                        st.caption(f"{calc_info.get('category', '')}")
                        if st.button(f"▶️ Mở", key=f"open_{calc_id}", use_container_width=True):
                            # Navigate to calculator page
                            from utils.state import add_to_recently_used
                            add_to_recently_used(calc_id)
                            _track_calculator_usage(calc_id)
                            st.switch_page(page_path)
            
            # Show "show more" if there are more results
            if len(results) > 9:
                st.info(f"💡 Có thêm {len(results) - 9} kết quả. Hãy tinh chỉnh từ khóa để xem thêm.")
        else:
            # Show suggestions when no results
            st.warning(f"""
            **❌ Không tìm thấy kết quả cho: "{search_query}"**
            
            💡 **Thử:**
            - Từ khóa khác: tim mạch, cấp cứu, xét nghiệm, thuốc
            - Kiểm tra chính tả
            - Tắt "Fuzzy" nếu đang bật
            - Thử tìm kiếm phổ biến bên dưới
            """)
    else:
        # Show popular searches and search history when no query
        st.info("💡 **Mẹo tìm kiếm:** Gõ tên calculator (ví dụ: SOFA, CHA2DS2VASc) hoặc chuyên khoa (ví dụ: tim mạch, cấp cứu)")
        
        # Show search history if available
        search_history = st.session_state.get('search_history', [])
        if search_history:
            st.markdown("**🕐 Lịch sử tìm kiếm:**")
            hist_cols = st.columns(min(5, len(search_history)))
            for idx, hist_query in enumerate(search_history[:5]):
                with hist_cols[idx]:
                    if st.button(f"↩️ {hist_query}", key=f"hist_{idx}_{hist_query}", use_container_width=True):
                        st.session_state.search_box_enhanced = hist_query
                        _track_search(hist_query)
                        st.rerun()
            st.markdown("---")
        
        # Popular searches
        _init_popular_searches()
        popular = st.session_state.get('popular_searches', {})
        if popular:
            sorted_popular = sorted(popular.items(), key=lambda x: x[1], reverse=True)
            popular_searches = [q for q, _ in sorted_popular[:5]]
        else:
            popular_searches = ["SOFA", "CHA2DS2VASc", "APACHE", "NEWS2", "ASCVD"]
        
        st.markdown("**🔥 Tìm kiếm phổ biến:**")
        pop_cols = st.columns(5)
        for idx, pop_search in enumerate(popular_searches[:5]):
            with pop_cols[idx]:
                if st.button(pop_search, key=f"pop_search_{idx}_{pop_search}", use_container_width=True):
                    st.session_state.search_box_enhanced = pop_search
                    _track_search(pop_search)
                    st.rerun()
    
    st.markdown("---")

