"""
Advanced Drug Search UI Components
Streamlit components for enhanced drug search
"""

import streamlit as st
import time
from typing import List, Dict, Tuple

# Import search functions
try:
    from .search_enhanced import (
        search_drugs,
        get_drug_autocomplete_suggestions,
        search_drugs_with_filters,
        get_search_statistics,
        add_recent_search,
        get_recent_searches,
        highlight_search_term
    )
except ImportError:
    from search_enhanced import (
        search_drugs,
        get_drug_autocomplete_suggestions,
        search_drugs_with_filters,
        get_search_statistics,
        add_recent_search,
        get_recent_searches,
        highlight_search_term
    )


def render_search_bar_with_autocomplete():
    """
    Render search bar with real-time autocomplete
    Returns: (query, selected_drug)
    """
    st.markdown("### 🔍 Tìm Kiếm Thuốc")
    
    # Search input
    col1, col2 = st.columns([4, 1])
    
    with col1:
        query = st.text_input(
            "Nhập tên thuốc (tối thiểu 3 ký tự)",
            placeholder="Ví dụ: Metformin, Atorvastatin, Omeprazole...",
            key="drug_search_query",
            label_visibility="collapsed"
        )
    
    with col2:
        search_button = st.button("🔍 Tìm", use_container_width=True)
    
    # Autocomplete suggestions
    selected_drug = None
    if query and len(query) >= 3:
        with st.spinner("Đang tìm kiếm..."):
            suggestions = get_drug_autocomplete_suggestions(query, limit=10)
            
            if suggestions:
                st.markdown("**Gợi ý:**")
                cols = st.columns(5)
                for idx, suggestion in enumerate(suggestions[:10]):
                    col_idx = idx % 5
                    with cols[col_idx]:
                        if st.button(
                            suggestion,
                            key=f"suggestion_{idx}",
                            use_container_width=True
                        ):
                            selected_drug = suggestion
                            add_recent_search(suggestion)
    
    # Recent searches
    recent = get_recent_searches()
    if recent and not query:
        st.markdown("**Tìm kiếm gần đây:**")
        cols = st.columns(5)
        for idx, recent_query in enumerate(recent[:5]):
            col_idx = idx % 5
            with cols[col_idx]:
                if st.button(
                    f"🕐 {recent_query}",
                    key=f"recent_{idx}",
                    use_container_width=True
                ):
                    selected_drug = recent_query
    
    return query, selected_drug


def render_advanced_filters():
    """
    Render advanced search filters
    Returns: filters dict
    """
    with st.expander("🔧 Bộ Lọc Nâng Cao", expanded=False):
        col1, col2, col3 = st.columns(3)
        
        with col1:
            group_filter = st.selectbox(
                "Nhóm thuốc",
                options=["Tất cả", "Cardiovascular", "Diabetes", "Antimicrobial", 
                        "Gastrointestinal", "Neurological", "Respiratory",
                        "Endocrinology", "Psychiatry", "Oncology"],
                key="group_filter"
            )
        
        with col2:
            route_filter = st.selectbox(
                "Đường dùng",
                options=["Tất cả", "PO", "IV", "IM", "SC", "Topical", "Inhaled"],
                key="route_filter"
            )
        
        with col3:
            pregnancy_safe = st.checkbox(
                "Chỉ thuốc an toàn cho thai kỳ",
                key="pregnancy_safe"
            )
        
        # Indication filter
        indication_filter = st.text_input(
            "Chỉ định (ví dụ: hypertension, diabetes)",
            key="indication_filter"
        )
        
        # Build filters dict
        filters = {}
        if group_filter != "Tất cả":
            filters['group'] = group_filter
        if route_filter != "Tất cả":
            filters['route'] = route_filter
        if pregnancy_safe:
            filters['exclude_pregnancy_x'] = True
        if indication_filter:
            filters['indication'] = indication_filter
        
        return filters


def render_search_results(results: List[Tuple], query: str = ""):
    """
    Render search results with highlighting
    
    Args:
        results: List of (drug_name, drug_data, score) tuples
        query: Search query for highlighting
    """
    if not results:
        st.info("Không tìm thấy kết quả phù hợp.")
        return
    
    st.markdown(f"### 📋 Kết quả ({len(results)} thuốc)")
    
    # Sort options
    sort_by = st.radio(
        "Sắp xếp theo:",
        options=["Độ liên quan", "Tên A-Z", "Nhóm thuốc"],
        horizontal=True,
        key="sort_results"
    )
    
    # Sort results
    if sort_by == "Tên A-Z":
        results = sorted(results, key=lambda x: x[0])
    elif sort_by == "Nhóm thuốc":
        results = sorted(results, key=lambda x: x[1].get('group', ''))
    # Default: already sorted by score
    
    # Display results
    for idx, (drug_name, drug_data, score) in enumerate(results):
        with st.expander(
            f"**{drug_name}** - {drug_data.get('vietnamese_name', '')} "
            f"(Điểm: {score:.2f})",
            expanded=(idx == 0)  # Expand first result
        ):
            render_drug_detail(drug_name, drug_data, query)


def render_drug_detail(drug_name: str, drug_data: Dict, highlight_query: str = ""):
    """
    Render detailed drug information
    
    Args:
        drug_name: Drug name
        drug_data: Drug data dictionary
        highlight_query: Query to highlight in text
    """
    # Basic info
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"**Nhóm:** {drug_data.get('group', 'N/A')}")
        st.markdown(f"**Tên tiếng Việt:** {drug_data.get('vietnamese_name', 'N/A')}")
        
        # Brand names
        brand_names = drug_data.get('brand_names', {})
        if isinstance(brand_names, dict):
            common_brands = brand_names.get('common', [])
            vn_brands = brand_names.get('vietnam', [])
            if common_brands:
                st.markdown(f"**Tên thương mại:** {', '.join(common_brands[:3])}")
            if vn_brands:
                st.markdown(f"**Tên VN:** {', '.join(vn_brands[:3])}")
    
    with col2:
        routes = drug_data.get('administration', [])
        if routes:
            st.markdown(f"**Đường dùng:** {', '.join(routes)}")
        
        pregnancy = drug_data.get('pregnancy_lactation', '')
        if pregnancy:
            if 'Category X' in pregnancy or 'Category D' in pregnancy:
                st.error(f"⚠️ {pregnancy[:50]}...")
            else:
                st.info(f"🤰 {pregnancy[:50]}...")
    
    # Tabs for detailed info
    tabs = st.tabs([
        "📋 Chỉ định",
        "🚫 Chống chỉ định",
        "💊 Liều dùng",
        "⚠️ Tác dụng phụ",
        "🔄 Tương tác",
        "🔬 Cơ chế"
    ])
    
    # Indications
    with tabs[0]:
        indications = drug_data.get('indications', [])
        if indications:
            for ind in indications:
                highlighted = highlight_search_term(ind, highlight_query)
                st.markdown(f"- {highlighted}")
        else:
            st.info("Không có thông tin")
    
    # Contraindications
    with tabs[1]:
        contras = drug_data.get('contraindications', [])
        if contras:
            for contra in contras:
                st.markdown(f"- {contra}")
        else:
            st.info("Không có thông tin")
    
    # Dosage
    with tabs[2]:
        dosage = drug_data.get('dosage', {})
        if isinstance(dosage, dict):
            for key, value in dosage.items():
                st.markdown(f"**{key}:** {value}")
        elif isinstance(dosage, str):
            st.markdown(dosage)
        else:
            st.info("Không có thông tin")
    
    # Side effects
    with tabs[3]:
        side_effects = drug_data.get('side_effects', [])
        if side_effects:
            for se in side_effects:
                st.markdown(f"- {se}")
        else:
            st.info("Không có thông tin")
    
    # Interactions
    with tabs[4]:
        interactions = drug_data.get('interactions', [])
        if interactions:
            for interaction in interactions:
                st.warning(f"⚠️ {interaction}")
        else:
            st.success("Không có tương tác đáng kể")
    
    # Mechanism
    with tabs[5]:
        moa = drug_data.get('mechanism_of_action', '')
        if moa:
            st.markdown(moa)
        else:
            st.info("Không có thông tin")
    
    # Black box warning
    if 'black_box_warnings' in drug_data:
        st.error(f"🚨 **CẢNH BÁO HỘP ĐEN:** {drug_data['black_box_warnings']}")


def render_performance_comparison():
    """
    Render performance comparison between old and new search
    """
    with st.expander("⚡ So sánh Performance", expanded=False):
        st.markdown("### Benchmark: Old vs New Search")
        
        test_query = st.text_input(
            "Test query:",
            value="met",
            key="perf_test_query"
        )
        
        if st.button("Run Benchmark"):
            # Old search (legacy)
            start = time.time()
            from search_enhanced import search_drugs_legacy
            old_results = search_drugs_legacy(test_query, max_results=20)
            old_time = (time.time() - start) * 1000  # ms
            
            # New search (fast)
            start = time.time()
            from search_enhanced import search_drugs_fast
            new_results = search_drugs_fast(test_query, max_results=20)
            new_time = (time.time() - start) * 1000  # ms
            
            # Display results
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric(
                    "Old Search",
                    f"{old_time:.2f}ms",
                    f"{len(old_results)} results"
                )
            
            with col2:
                st.metric(
                    "New Search",
                    f"{new_time:.2f}ms",
                    f"{len(new_results)} results"
                )
            
            with col3:
                speedup = old_time / new_time if new_time > 0 else 0
                st.metric(
                    "Speedup",
                    f"{speedup:.1f}x",
                    "faster ⚡"
                )


def render_search_statistics():
    """Render search index statistics"""
    with st.expander("📊 Thống Kê Database", expanded=False):
        stats = get_search_statistics()
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Tổng số thuốc", stats.get('total_drugs', 0))
            st.metric("Nhóm thuốc", stats.get('total_groups', 0))
        
        with col2:
            st.metric("Từ khóa chỉ định", stats.get('total_indications', 0))
            st.metric("Tên thương mại", stats.get('total_brands', 0))
        
        with col3:
            st.metric("Đường dùng", stats.get('total_routes', 0))
            indexed = "✅ Yes" if stats.get('indexed') else "❌ No"
            st.metric("Indexed", indexed)


def render_complete_search_page():
    """
    Complete search page with all components
    Main entry point for drug search UI
    """
    st.title("🔍 Tìm Kiếm Thuốc Nâng Cao")
    
    # Search bar with autocomplete
    query, selected_drug = render_search_bar_with_autocomplete()
    
    # Use selected drug from autocomplete/recent
    if selected_drug:
        query = selected_drug
    
    # Advanced filters
    filters = render_advanced_filters()
    
    # Performance comparison
    render_performance_comparison()
    
    # Statistics
    render_search_statistics()
    
    # Perform search
    if query:
        add_recent_search(query)
        
        with st.spinner("Đang tìm kiếm..."):
            start_time = time.time()
            
            if filters:
                # Advanced search with filters
                filters['query'] = query  # Add query to filters
                results = search_drugs_with_filters(filters)
            else:
                # Simple search
                results = search_drugs(query, max_results=50)
            
            search_time = (time.time() - start_time) * 1000
        
        # Show search time
        st.caption(f"⏱️ Thời gian tìm kiếm: {search_time:.2f}ms")
        
        # Render results
        render_search_results(results, query)


# ==================== EXPORTS ====================

__all__ = [
    'render_search_bar_with_autocomplete',
    'render_advanced_filters',
    'render_search_results',
    'render_drug_detail',
    'render_performance_comparison',
    'render_search_statistics',
    'render_complete_search_page'
]


# ==================== MAIN ====================

if __name__ == "__main__":
    # Run as standalone Streamlit app
    render_complete_search_page()
