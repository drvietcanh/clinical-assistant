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


def render_global_search_bar(placeholder: str = "Tìm kiếm thuốc, thang điểm, guideline... (Ctrl+K)"):
    """Render global search bar with autocomplete and debounce"""
    render_global_search_modal()
    
    # Initialize debounced search state
    if 'global_search_debounced' not in st.session_state:
        st.session_state.global_search_debounced = ''
    
    # Search input with debounce JavaScript (only add once)
    if 'debounce_script_added' not in st.session_state:
        st.session_state.debounce_script_added = True
        st.markdown("""
        <script>
        // Debounce function
        function debounce(func, wait) {
            let timeout;
            return function executedFunction(...args) {
                const later = () => {
                    clearTimeout(timeout);
                    func(...args);
                };
                clearTimeout(timeout);
                timeout = setTimeout(later, wait);
            };
        }
        
        // Initialize debounce for search input
        window.addEventListener('load', function() {
            const searchInput = document.querySelector('input[placeholder*="Tìm kiếm"], input[placeholder*="tìm kiếm"]');
            if (searchInput) {
                const debouncedSearch = debounce(function() {
                    // Trigger Streamlit rerun after debounce
                    const event = new Event('input', { bubbles: true });
                    searchInput.dispatchEvent(event);
                }, 300); // 300ms debounce
                
                searchInput.addEventListener('input', debouncedSearch);
            }
        });
        </script>
        """, unsafe_allow_html=True)
    
    # Search input
    search_query = st.text_input(
        "🔍 Tìm kiếm",
        value=st.session_state.get('global_search_query', ''),
        placeholder=placeholder,
        key="global_search_input",
        label_visibility="collapsed"
    )
    
    # Update session state and add to history if query changed
    if search_query != st.session_state.get('global_search_query', ''):
        st.session_state.global_search_query = search_query
        if search_query and len(search_query.strip()) >= 2:
            add_to_search_history(search_query)
    
    # Show search history if no query
    if not search_query and len(get_search_history()) > 0:
        history = get_search_history()
        st.caption("🔍 Tìm kiếm gần đây:")
        history_cols = st.columns(min(5, len(history)))
        for idx, hist_query in enumerate(history[:5]):
            with history_cols[idx]:
                if st.button(f"↩️ {hist_query[:15]}", key=f"history_{idx}", use_container_width=True):
                    st.session_state.global_search_query = hist_query
                    st.rerun()
    
    return search_query


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
    """Render unified search results for drugs, calculators, and protocols"""
    if not query or len(query.strip()) < 1:
        return
    
    query = query.strip()
    
    # Show loading skeleton if needed
    if show_loading:
        with st.spinner("Đang tìm kiếm..."):
            render_skeleton_loader()
            return
    
    # Search drugs
    drug_results = search_drugs(query, max_results=max_results_per_category)
    
    # Search calculators
    calc_results = search_calculators(query, max_results=max_results_per_category)
    
    # Show results
    has_results = len(drug_results) > 0 or len(calc_results) > 0
    
    if not has_results:
        st.info(f"🔍 Không tìm thấy kết quả cho '{query}'. Thử tìm kiếm với từ khóa khác.")
        return
    
    # Drug results
    if drug_results:
        st.markdown("### 💊 Thuốc")
        for drug_name, drug_data in drug_results:
            vn_name = drug_data.get('vietnamese_name', '')
            group = drug_data.get('group', '')
            
            # Highlight search term
            highlighted_name = highlight_search_term(drug_name, query)
            highlighted_vn = highlight_search_term(vn_name, query) if vn_name else ''
            
            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown(
                    f"""
                    <div style="padding: 12px; background: var(--card-bg); border-radius: 8px; margin-bottom: 8px; border: 1px solid var(--border);">
                        <div style="font-weight: 600; color: var(--primary); margin-bottom: 4px;">
                            {highlighted_name}
                        </div>
                        {f'<div style="color: var(--text-secondary); font-size: 0.9em; margin-bottom: 4px;">{highlighted_vn}</div>' if highlighted_vn else ''}
                        <div style="color: var(--text-secondary); font-size: 0.85em;">{group}</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            with col2:
                safe_name = str(drug_name).replace(' ', '_').replace('-', '_').replace('/', '_')
                if st.button('📖 Xem', key=f'search_drug_{safe_name}', use_container_width=True):
                    st.session_state['selected_drug'] = str(drug_name)
                    st.session_state['show_detail'] = True
                    st.session_state['switch_to_drugs'] = True
                    st.rerun()
    
    # Calculator results
    if calc_results:
        st.markdown("### 📊 Thang điểm & Công cụ")
        cols = st.columns(min(3, len(calc_results)))
        for idx, calc in enumerate(calc_results[:6]):
            with cols[idx % len(cols)]:
                highlighted_name = highlight_search_term(calc['name'], query)
                st.markdown(
                    f"""
                    <div style="padding: 12px; background: var(--card-bg); border-radius: 8px; margin-bottom: 8px; border: 1px solid var(--border); text-align: center;">
                        <div style="font-size: 2rem; margin-bottom: 4px;">{calc['icon']}</div>
                        <div style="font-weight: 600; font-size: 0.9em; color: var(--primary);">
                            {highlighted_name}
                        </div>
                        <div style="color: var(--text-secondary); font-size: 0.75em; margin-top: 4px;">
                            {calc['category']}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                
                # Button to navigate
                page_path_map = {
                    'Scores': 'pages/01_📊_Scores.py',
                    'Labs': 'pages/05_🔬_Labs_and_Calculators.py',
                    'Drugs': 'pages/07_💊_Drug_Database.py',
                    'Protocols': 'pages/04_📋_Protocols.py',
                }
                page_path = page_path_map.get(calc['page'], 'pages/01_📊_Scores.py')
                
                if st.button('Mở', key=f'search_calc_{calc["id"]}', use_container_width=True):
                    st.session_state['preset_calculator'] = calc['id']
                    st.session_state['switch_to_scores'] = True
                    st.rerun()


def render_autocomplete_suggestions(query: str, max_suggestions: int = 5):
    """Render autocomplete suggestions dropdown"""
    if not query or len(query) < 1:
        return
    
    # Get drug suggestions
    drug_suggestions = get_drug_autocomplete_suggestions(query, max_suggestions=max_suggestions)
    
    if drug_suggestions:
        st.caption(f"💡 Gợi ý: {', '.join(drug_suggestions[:3])}")

