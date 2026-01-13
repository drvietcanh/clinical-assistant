"""
Global Search Component
Unified search for drugs, calculators, protocols with keyboard shortcut (Ctrl+K)
"""

import streamlit as st
from typing import List, Dict, Tuple, Optional
from drugs.search import search_drugs, get_drug_autocomplete_suggestions
from config.calculators import ALL_CALCULATORS
import re


@st.cache_data(ttl=300, max_entries=200)
def search_calculators(query: str, max_results: int = 5) -> List[Dict]:
    """Search calculators by name or category"""
    if not query:
        return []
    
    query_lower = query.lower().strip()
    results = []
    
    for calc_id, calc_info in ALL_CALCULATORS.items():
        score = 0.0
        name = calc_info.get('name', '')
        category = calc_info.get('category', '')
        
        # Exact match
        if query_lower == name.lower():
            score = 1.0
        # Starts with
        elif name.lower().startswith(query_lower):
            score = 0.9
        # Contains in name
        elif query_lower in name.lower():
            score = 0.8
        # Contains in category
        elif query_lower in category.lower():
            score = 0.6
        
        if score > 0:
            results.append({
                'id': calc_id,
                'name': name,
                'icon': calc_info.get('icon', '📊'),
                'category': category,
                'page': calc_info.get('page', 'Scores'),
                'score': score,
                'type': 'calculator'
            })
    
    # Sort by score
    results.sort(key=lambda x: x['score'], reverse=True)
    return results[:max_results]


def highlight_search_term(text: str, query: str) -> str:
    """Highlight search term in text"""
    if not query or not text:
        return text
    
    pattern = re.compile(re.escape(query), re.IGNORECASE)
    highlighted = pattern.sub(
        lambda m: f'<mark style="background: #FFEB3B; padding: 2px 4px; border-radius: 3px;">{m.group()}</mark>',
        text
    )
    return highlighted


def render_global_search_modal():
    """Render global search modal with keyboard shortcut"""
    # Initialize search state
    if 'global_search_query' not in st.session_state:
        st.session_state.global_search_query = ''
    if 'global_search_focused' not in st.session_state:
        st.session_state.global_search_focused = False
    
    # Keyboard shortcut handler (Ctrl+K or Cmd+K)
    st.markdown("""
    <script>
    document.addEventListener('keydown', function(e) {
        // Ctrl+K or Cmd+K
        if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
            e.preventDefault();
            // Focus on search input
            const searchInput = document.querySelector('input[placeholder*="Tìm kiếm"], input[placeholder*="tìm kiếm"]');
            if (searchInput) {
                searchInput.focus();
                searchInput.select();
            }
        }
    });
    </script>
    """, unsafe_allow_html=True)


def get_search_history(max_items: int = 5) -> List[str]:
    """Get recent search history"""
    if 'global_search_history' not in st.session_state:
        st.session_state.global_search_history = []
    return st.session_state.global_search_history[:max_items]


def add_to_search_history(query: str):
    """Add query to search history"""
    if 'global_search_history' not in st.session_state:
        st.session_state.global_search_history = []
    
    query = query.strip()
    if query and query not in st.session_state.global_search_history:
        st.session_state.global_search_history.insert(0, query)
        # Keep only last 10 searches
        st.session_state.global_search_history = st.session_state.global_search_history[:10]


def render_global_search_bar(placeholder: str = "Tìm kiếm thuốc, thang điểm, guideline... (Ctrl+K)", show_category_filters: bool = True):
    """Render enhanced global search bar with autocomplete, history, and category filters"""
    render_global_search_modal()
    
    # Initialize search state
    if 'global_search_debounced' not in st.session_state:
        st.session_state.global_search_debounced = ''
    if 'search_category_filter' not in st.session_state:
        st.session_state.search_category_filter = 'all'
    
    # Category filters
    if show_category_filters:
        filter_col1, filter_col2 = st.columns([3, 1])
        with filter_col1:
            category_filter = st.radio(
                "Lọc theo:",
                ["Tất cả", "💊 Thuốc", "📊 Calculators", "📋 Protocols"],
                horizontal=True,
                key="search_category_radio",
                label_visibility="collapsed"
            )
            category_map = {
                "Tất cả": "all",
                "💊 Thuốc": "drugs",
                "📊 Calculators": "calculators",
                "📋 Protocols": "protocols"
            }
            st.session_state.search_category_filter = category_map.get(category_filter, "all")
        with filter_col2:
            if st.button("🗑️ Xóa lịch sử", use_container_width=True):
                if 'global_search_history' in st.session_state:
                    st.session_state.global_search_history = []
                st.rerun()
    
    # Search input with enhanced styling
    st.markdown('<div class="search-container">', unsafe_allow_html=True)
    search_query = st.text_input(
        "🔍 Tìm kiếm",
        value=st.session_state.get('global_search_query', ''),
        placeholder=placeholder,
        key="global_search_input",
        label_visibility="collapsed"
    )
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Update session state and add to history if query changed
    if search_query != st.session_state.get('global_search_query', ''):
        st.session_state.global_search_query = search_query
        if search_query and len(search_query.strip()) >= 2:
            add_to_search_history(search_query)
    
    # Show autocomplete suggestions if query exists
    if search_query and len(search_query.strip()) >= 1:
        render_autocomplete_suggestions_enhanced(search_query)
    
    # Show search history if no query
    if not search_query and len(get_search_history()) > 0:
        history = get_search_history()
        st.markdown('<div class="search-history">', unsafe_allow_html=True)
        st.caption("🔍 Tìm kiếm gần đây:")
        history_cols = st.columns(min(5, len(history)))
        for idx, hist_query in enumerate(history[:5]):
            with history_cols[idx]:
                if st.button(
                    f"↩️ {hist_query[:20]}",
                    key=f"history_{idx}",
                    use_container_width=True,
                    help=f"Tìm lại: {hist_query}"
                ):
                    st.session_state.global_search_query = hist_query
                    st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    
    return search_query


def render_autocomplete_suggestions_enhanced(query: str, max_suggestions: int = 8):
    """Render enhanced autocomplete suggestions with better UI"""
    if not query or len(query.strip()) < 1:
        return
    
    query_lower = query.lower().strip()
    
    # Get suggestions from calculators
    calc_suggestions = []
    for calc_id, calc_info in ALL_CALCULATORS.items():
        name = calc_info.get('name', '')
        if query_lower in name.lower():
            calc_suggestions.append({
                'id': calc_id,
                'name': name,
                'icon': calc_info.get('icon', '📊'),
                'category': calc_info.get('category', ''),
                'type': 'calculator'
            })
            if len(calc_suggestions) >= max_suggestions // 2:
                break
    
    # Get drug suggestions if available
    drug_suggestions = []
    try:
        drug_suggestions_list = get_drug_autocomplete_suggestions(query, max_suggestions=max_suggestions // 2)
        for drug_name in drug_suggestions_list[:max_suggestions // 2]:
            drug_suggestions.append({
                'name': drug_name,
                'icon': '💊',
                'type': 'drug'
            })
    except Exception:
        pass
    
    # Combine and limit suggestions
    all_suggestions = calc_suggestions[:4] + drug_suggestions[:4]
    
    if all_suggestions:
        st.markdown('<div class="search-suggestions">', unsafe_allow_html=True)
        for idx, suggestion in enumerate(all_suggestions[:max_suggestions]):
            col1, col2 = st.columns([1, 4])
            with col1:
                st.markdown(f'<div style="font-size: 1.5rem; text-align: center;">{suggestion["icon"]}</div>', unsafe_allow_html=True)
            with col2:
                highlighted_name = highlight_search_term(suggestion['name'], query)
                category = suggestion.get('category', '')
                st.markdown(
                    f"""
                    <div class="search-suggestion-item" style="cursor: pointer; padding: 8px 0;">
                        <div class="search-suggestion-name">{highlighted_name}</div>
                        {f'<div class="search-suggestion-category">{category}</div>' if category else ''}
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                if st.button("Chọn", key=f"suggestion_{idx}", use_container_width=True):
                    st.session_state.global_search_query = suggestion['name']
                    st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)


def render_skeleton_loader():
    """Render skeleton loader for search results"""
    st.markdown("""
    <div class="skeleton-loader" style="
        background: var(--card-bg);
        border-radius: 8px;
        padding: 12px;
        margin-bottom: 8px;
        animation: pulse 1.5s ease-in-out infinite;
    ">
        <div style="height: 20px; background: var(--border); border-radius: 4px; margin-bottom: 8px; width: 60%;"></div>
        <div style="height: 16px; background: var(--border); border-radius: 4px; width: 40%;"></div>
    </div>
    <style>
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.5; }
    }
    </style>
    """, unsafe_allow_html=True)


def render_search_results(query: str, max_results_per_category: int = 5, show_loading: bool = False):
    """Render enhanced unified search results with better visual cards"""
    if not query or len(query.strip()) < 1:
        return
    
    query = query.strip()
    category_filter = st.session_state.get('search_category_filter', 'all')
    
    # Show loading skeleton if needed
    if show_loading:
        with st.spinner("Đang tìm kiếm..."):
            render_skeleton_loader()
            return
    
    # Search based on category filter
    drug_results = []
    calc_results = []
    
    if category_filter in ['all', 'drugs']:
        try:
            drug_results = search_drugs(query, max_results=max_results_per_category)
        except Exception:
            pass
    
    if category_filter in ['all', 'calculators']:
        calc_results = search_calculators(query, max_results=max_results_per_category)
    
    # Show results
    has_results = len(drug_results) > 0 or len(calc_results) > 0
    
    if not has_results:
        st.info(f"🔍 Không tìm thấy kết quả cho '{query}'. Thử tìm kiếm với từ khóa khác hoặc xóa bộ lọc.")
        return
    
    # Drug results with enhanced cards
    if drug_results:
        st.markdown("### 💊 Thuốc")
        st.caption(f"Tìm thấy {len(drug_results)} kết quả")
        for drug_name, drug_data in drug_results:
            vn_name = drug_data.get('vietnamese_name', '')
            group = drug_data.get('group', '')
            
            # Highlight search term
            highlighted_name = highlight_search_term(drug_name, query)
            highlighted_vn = highlight_search_term(vn_name, query) if vn_name else ''
            
            col1, col2 = st.columns([4, 1])
            with col1:
                st.markdown(
                    f"""
                    <div class="calculator-card" style="padding: 16px; margin-bottom: 12px;">
                        <div style="display: flex; align-items: center; gap: 12px;">
                            <div style="font-size: 2rem;">💊</div>
                            <div style="flex: 1;">
                                <div style="font-weight: 600; color: var(--text-primary); margin-bottom: 4px; font-size: 1.1rem;">
                                    {highlighted_name}
                                </div>
                                {f'<div style="color: var(--text-secondary); font-size: 0.9em; margin-bottom: 4px;">{highlighted_vn}</div>' if highlighted_vn else ''}
                                <div style="color: var(--text-secondary); font-size: 0.85em;">{group}</div>
                            </div>
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            with col2:
                safe_name = str(drug_name).replace(' ', '_').replace('-', '_').replace('/', '_')
                if st.button('📖 Xem', key=f'search_drug_{safe_name}', use_container_width=True, type="primary"):
                    st.session_state['view_drug_name'] = str(drug_name)
                    st.session_state['selected_drug'] = str(drug_name)
                    st.session_state['show_detail'] = True
                    st.session_state['switch_to_drugs'] = True
                    st.rerun()
    
    # Calculator results with enhanced cards
    if calc_results:
        st.markdown("### 📊 Thang điểm & Công cụ")
        st.caption(f"Tìm thấy {len(calc_results)} kết quả")
        cols = st.columns(min(3, len(calc_results)))
        for idx, calc in enumerate(calc_results[:9]):
            with cols[idx % len(cols)]:
                highlighted_name = highlight_search_term(calc['name'], query)
                is_favorite = calc['id'] in st.session_state.get('favorites', [])
                star_icon = "⭐" if is_favorite else "☆"
                
                st.markdown(
                    f"""
                    <div class="calculator-card" style="text-align: center; padding: 20px; margin-bottom: 12px;">
                        <div class="calculator-card-icon" style="font-size: 3rem; margin-bottom: 12px;">{calc['icon']}</div>
                        <div class="calculator-card-name" style="font-size: 1rem; margin-bottom: 8px;">
                            {highlighted_name}
                        </div>
                        <div class="calculator-card-category" style="font-size: 0.85rem; margin-bottom: 12px;">
                            {calc['category']}
                        </div>
                        <div style="font-size: 1.2rem; opacity: 0.6;">{star_icon}</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                
                # Buttons row
                btn_col1, btn_col2 = st.columns(2)
                with btn_col1:
                    page_path_map = {
                        'Scores': 'pages/01_📊_Scores.py',
                        'Labs': 'pages/05_🔬_Labs_and_Calculators.py',
                        'Drugs': 'pages/07_💊_Drug_Database.py',
                        'Protocols': 'pages/04_📋_Protocols.py',
                    }
                    page_path = page_path_map.get(calc['page'], 'pages/01_📊_Scores.py')
                    
                    if st.button('Mở', key=f'search_calc_{calc["id"]}', use_container_width=True, type="primary"):
                        st.session_state['preset_calculator'] = calc['id']
                        st.session_state['switch_to_scores'] = True
                        st.rerun()
                
                with btn_col2:
                    if st.button(star_icon, key=f'fav_{calc["id"]}', use_container_width=True):
                        from utils.state import add_to_favorites, remove_from_favorites
                        if is_favorite:
                            remove_from_favorites(calc['id'])
                        else:
                            add_to_favorites(calc['id'])
                        st.rerun()


def render_autocomplete_suggestions(query: str, max_suggestions: int = 5):
    """Render autocomplete suggestions dropdown"""
    if not query or len(query) < 1:
        return
    
    # Get drug suggestions
    drug_suggestions = get_drug_autocomplete_suggestions(query, max_suggestions=max_suggestions)
    
    if drug_suggestions:
        st.caption(f"💡 Gợi ý: {', '.join(drug_suggestions[:3])}")

