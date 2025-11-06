"""
Antibiotic Database and Lookup Functions - Optimized Version
Tích hợp database kháng sinh với công cụ tra cứu và tính liều
Đã tối ưu: loại bỏ trùng lặp, compact view, expandable details, integrated dosing calculator
"""

import streamlit as st
import pandas as pd
from .antibiotics_data import ANTIBIOTICS_DATABASE
from .database_search import (
    search_antibiotics,
    get_antibiotic_autocomplete_suggestions,
    get_recent_searches,
    add_to_recent_searches,
    filter_antibiotics
)
from .database_display import (
    render_compact_antibiotic_card,
    display_antibiotic_info,
    _sanitize_key
)
from .database_calculator import render_quick_dosing_calculator
from .database_export import _render_antibiotic_export

def render_database():
    """Unified Antibiotic Database - Search, Browse, Detail View, and Integrated Dosing Calculator"""
    
    # Initialize session state
    if 'antibiotic_favorites' not in st.session_state:
        st.session_state.antibiotic_favorites = []
    if 'recently_viewed_antibiotics' not in st.session_state:
        st.session_state.recently_viewed_antibiotics = []
    
    ab_count = len(ANTIBIOTICS_DATABASE)
    
    # Modern header with gradient
    st.markdown(f"""
    <div style='
        background: linear-gradient(135deg, #0EA5E9 0%, #0288D1 100%);
        color: white;
        padding: 25px;
        border-radius: 15px;
        margin-bottom: 25px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    '>
        <h1 style='margin: 0; color: white; font-size: 2.2em;'>🔍 Tra Cứu & Dữ Liệu Kháng Sinh</h1>
        <p style='margin: 10px 0 0 0; color: rgba(255,255,255,0.9); font-size: 1.1em;'>
            Database <strong>{ab_count}</strong> kháng sinh tiêm truyền thông dụng • Tích hợp tính liều tự động
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Quick info and tabs
    tab_info, tab_favorites, tab_recent = st.tabs(["ℹ️ Database", "⭐ Yêu thích", "🕐 Gần đây"])
    
    with tab_info:
        st.info(f"""
        **Cơ sở dữ liệu bao gồm:**
        - ✅ {ab_count} kháng sinh tiêm truyền (IV/IM) thông dụng tại Việt Nam
        - ✅ Tên biệt dược và tên chung
        - ✅ Liều dùng chi tiết (người lớn, trẻ em, nhiễm khuẩn nặng)
        - ✅ Điều chỉnh theo chức năng thận/gan
        - ✅ Chỉ định, chống chỉ định, tác dụng phụ
        - ✅ Tương tác thuốc và phân loại AWaRe
        - ✅ Dựa trên guidelines: IDSA, ASHP, WHO AWaRe 2023
        """)
    
    with tab_favorites:
        favorites = st.session_state.antibiotic_favorites
        if favorites:
            st.success(f"Bạn có **{len(favorites)}** kháng sinh yêu thích")
            st.markdown("---")
            for ab_name in favorites:
                if ab_name in ANTIBIOTICS_DATABASE:
                    # Sanitize ab_name for key_prefix to avoid session state errors
                    safe_ab_name = _sanitize_key(ab_name)
                    render_compact_antibiotic_card(ab_name, ANTIBIOTICS_DATABASE[ab_name], key_prefix=f"fav_{safe_ab_name}_")
                    st.markdown("<br>", unsafe_allow_html=True)
        else:
            st.info("💡 Chưa có kháng sinh yêu thích. Nhấn ☆ trên card để thêm vào danh sách yêu thích!")
    
    with tab_recent:
        recent = st.session_state.recently_viewed_antibiotics
        if recent:
            st.success(f"Đã xem **{len(recent)}** kháng sinh gần đây")
            st.markdown("---")
            for ab_name in recent:
                if ab_name in ANTIBIOTICS_DATABASE:
                    # Sanitize ab_name for key_prefix to avoid session state errors
                    safe_ab_name = _sanitize_key(ab_name)
                    render_compact_antibiotic_card(ab_name, ANTIBIOTICS_DATABASE[ab_name], key_prefix=f"recent_{safe_ab_name}_")
                    st.markdown("<br>", unsafe_allow_html=True)
        else:
            st.info("💡 Chưa có kháng sinh nào được xem gần đây")
    
    st.markdown("---")
    
    # ========== SEARCH & FILTER SECTION ==========
    st.markdown("### 🔍 Tìm Kiếm")
    
    # Enhanced search with better UI
    col_search, col_clear = st.columns([5, 1])
    
    with col_search:
        search_query = st.text_input(
            "🔍 Tìm kiếm kháng sinh:",
            placeholder="Nhập tên thuốc, biệt dược, nhóm, hoặc chỉ định...",
            key="ab_search_main",
            help="Tìm kiếm theo tên kháng sinh, tên biệt dược, nhóm thuốc, hoặc chỉ định lâm sàng",
            label_visibility="collapsed"
        )
    
    with col_clear:
        if st.button("🗑️", help="Xóa tìm kiếm", use_container_width=True):
            st.session_state.ab_search_main = ""
            st.rerun()
    
    # Show autocomplete suggestions in a nicer format
    if search_query and len(search_query) >= 1:
        suggestions = get_antibiotic_autocomplete_suggestions(search_query, max_suggestions=5)
        if suggestions:
            st.markdown("**💡 Gợi ý tìm kiếm:**")
            suggestion_cols = st.columns(min(5, len(suggestions)))
            for idx, suggestion in enumerate(suggestions):
                with suggestion_cols[idx]:
                    if st.button(f"💊 {suggestion}", key=f"autocomplete_{suggestion}", use_container_width=True):
                        st.session_state.ab_search_main = suggestion
                        add_to_recent_searches(suggestion)
                        st.rerun()
            st.markdown("<br>", unsafe_allow_html=True)
    
    # Recent searches (when no query)
    recent_searches = get_recent_searches()
    if recent_searches and not search_query:
        st.markdown("**🕐 Tìm kiếm gần đây:**")
        recent_cols = st.columns(min(5, len(recent_searches)))
        for idx, recent in enumerate(recent_searches[:5]):
            with recent_cols[idx]:
                if st.button(f"↩️ {recent}", key=f"recent_search_{recent}", use_container_width=True):
                    st.session_state.ab_search_main = recent
                    st.rerun()
        st.markdown("<br>", unsafe_allow_html=True)
    
    # View mode selector
    view_mode = st.radio(
        "Chế độ:",
        ["🔍 Tìm kiếm", "📋 Duyệt tất cả"],
        key="view_mode",
        help="Chế độ tìm kiếm hoặc duyệt toàn bộ danh sách",
        horizontal=True
    )
    
    # Filters (only for browse mode)
    if view_mode == "📋 Duyệt tất cả":
        st.markdown("**🔽 Bộ lọc:**")
        col1, col2, col3 = st.columns(3)
        
        all_groups = sorted(list(set([ab.get('group', 'Khác') for ab in ANTIBIOTICS_DATABASE.values()])))
        
        with col1:
            filter_group = st.selectbox(
                "Nhóm:",
                ["Tất cả"] + all_groups,
                key="filter_group_main"
            )
        
        with col2:
            filter_route = st.selectbox(
                "Đường dùng:",
                ["Tất cả", "IV", "IM", "PO"],
                key="filter_route_main"
            )
        
        with col3:
            filter_aware = st.selectbox(
                "AWaRe:",
                ["Tất cả", "ACCESS", "WATCH", "RESERVE"],
                key="filter_aware_main"
            )
    
    st.markdown("---")
    
    # ========== RESULTS SECTION ==========
    
    # Handle view antibiotic from session state
    if 'view_antibiotic' in st.session_state:
        selected_ab = st.session_state['view_antibiotic']
        if selected_ab in ANTIBIOTICS_DATABASE:
            st.markdown("### 📖 Thông tin chi tiết")
            display_antibiotic_info(selected_ab, ANTIBIOTICS_DATABASE[selected_ab])
            st.markdown("---")
            if st.button("⬅️ Quay lại danh sách"):
                del st.session_state['view_antibiotic']
                st.rerun()
            return
    
    # Search mode
    if view_mode == "🔍 Tìm kiếm":
        if search_query:
            # Add to recent searches
            add_to_recent_searches(search_query)
            
            results = search_antibiotics(search_query)
            
            if results:
                st.success(f"✅ Tìm thấy **{len(results)}** kết quả cho '{search_query}'")
                st.markdown("---")
                
                # Display compact list
                for idx, (ab_name, ab_data) in enumerate(results):
                    render_compact_antibiotic_card(ab_name, ab_data, key_prefix=f"search_{idx}_")
                    if idx < len(results) - 1:
                        st.markdown("<hr style='margin: 10px 0; border: none; border-top: 1px solid #e0e0e0;'>", unsafe_allow_html=True)
            else:
                st.warning(f"❌ Không tìm thấy kết quả nào cho '{search_query}'")
                
                # Show autocomplete suggestions as fallback
                suggestions = get_antibiotic_autocomplete_suggestions(search_query, max_suggestions=5)
                if suggestions:
                    st.info("💡 **Gợi ý tìm kiếm:**")
                    sugg_cols = st.columns(min(5, len(suggestions)))
                    for idx, suggestion in enumerate(suggestions):
                        with sugg_cols[idx]:
                            # Sanitize suggestion for key
                            safe_sugg_key = f"sugg_{str(suggestion).replace(' ', '_').replace('-', '_').replace('/', '_')}"
                            if st.button(suggestion, key=safe_sugg_key, use_container_width=True):
                                st.session_state.ab_search_main = str(suggestion)
                                st.rerun()
                else:
                    st.info("💡 **Gợi ý:** Thử tìm với tên thuốc, biệt dược, nhóm thuốc (ví dụ: Beta-lactam), hoặc chỉ định (ví dụ: MRSA, Sepsis, UTI)")
        else:
            # Empty state with popular searches
            st.info("👆 **Nhập từ khóa để tìm kiếm** (ví dụ: Vancomycin, Ceftriaxone, MRSA, Sepsis)")
            st.markdown("---")
            
            # Show popular/quick links
            st.markdown("### ⚡ Truy cập nhanh:")
            popular = ["Vancomycin", "Ceftriaxone", "Piperacillin-Tazobactam", "Meropenem", "Levofloxacin"]
            cols = st.columns(len(popular))
            for col, ab_name in zip(cols, popular):
                if ab_name in ANTIBIOTICS_DATABASE:
                    with col:
                        # Sanitize ab_name for key
                        safe_quick_name = str(ab_name).replace(" ", "_").replace("-", "_").replace("/", "_")
                        if st.button(f"💊 {ab_name}", key=f"quick_{safe_quick_name}", use_container_width=True):
                            st.session_state['view_antibiotic'] = str(ab_name)
                            add_to_recent_searches(ab_name)
                            st.rerun()
    
    # Browse mode
    else:
        # Apply filters
        filtered_ab = filter_antibiotics(
            filter_group if view_mode == "📋 Duyệt tất cả" else "Tất cả",
            filter_route if view_mode == "📋 Duyệt tất cả" else "Tất cả",
            filter_aware if view_mode == "📋 Duyệt tất cả" else "Tất cả"
        )
        
        if filtered_ab:
            st.success(f"📋 Hiển thị **{len(filtered_ab)}** kháng sinh")
            st.markdown("---")
            
            # Display as compact list
            st.markdown("### 📚 Danh sách kháng sinh:")
            
            # Group by category for better organization
            groups_dict = {}
            for ab_name, ab_data in filtered_ab.items():
                group = ab_data.get('group', 'Khác')
                if group not in groups_dict:
                    groups_dict[group] = []
                groups_dict[group].append((ab_name, ab_data))
            
            # Display by group
            for group in sorted(groups_dict.keys()):
                if len(groups_dict) > 1:
                    st.markdown(f"#### {group} ({len(groups_dict[group])} thuốc)")
                
                for idx, (ab_name, ab_data) in enumerate(sorted(groups_dict[group], key=lambda x: x[0])):
                    render_compact_antibiotic_card(ab_name, ab_data, key_prefix=f"browse_{group}_{idx}_")
                    if idx < len(groups_dict[group]) - 1:
                        st.markdown("<hr style='margin: 8px 0; border: none; border-top: 1px solid #f0f0f0;'>", unsafe_allow_html=True)
                
                if group != list(groups_dict.keys())[-1]:
                    st.markdown("<br>", unsafe_allow_html=True)
        else:
            st.warning("❌ Không có kháng sinh nào thỏa mãn bộ lọc")
            if st.button("🔄 Xóa bộ lọc"):
                st.rerun()



def render_antibiotic_lookup():
    """Legacy function - redirects to render_database for backward compatibility"""
    render_database()


