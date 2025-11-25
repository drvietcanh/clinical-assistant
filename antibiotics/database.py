"""
Antibiotic Database and Lookup Functions - Optimized Version
Tích hợp database kháng sinh với công cụ tra cứu và tính liều
Đã tối ưu: loại bỏ trùng lặp, compact view, expandable details, integrated dosing calculator
"""

import streamlit as st
import pandas as pd
import html
from datetime import datetime
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
from .condition_search import search_by_condition, get_all_conditions
from .recent_calculations import render_recent_calculations_sidebar

def render_database():
    """Unified Antibiotic Database - Search, Browse, Detail View, and Integrated Dosing Calculator"""
    
    # Initialize session state
    if 'antibiotic_favorites' not in st.session_state:
        st.session_state.antibiotic_favorites = []
    
    # Initialize search state safely
    if 'ab_search_main' not in st.session_state:
        st.session_state.ab_search_main = ""
    if 'ab_search_trigger' not in st.session_state:
        st.session_state.ab_search_trigger = None
    if 'recently_viewed_antibiotics' not in st.session_state:
        st.session_state.recently_viewed_antibiotics = []
    
    # Handle search trigger from buttons (before widget is created)
    if st.session_state.ab_search_trigger is not None:
        st.session_state.ab_search_main = st.session_state.ab_search_trigger
        st.session_state.ab_search_trigger = None  # Clear trigger
    
    ab_count = len(ANTIBIOTICS_DATABASE)
    
    # Enhanced header with improved typography hierarchy and visual design
    st.markdown(f"""
    <div style='
        background: linear-gradient(135deg, #0EA5E9 0%, #0288D1 50%, #01579B 100%);
        color: white;
        padding: 30px 25px;
        border-radius: 20px;
        margin-bottom: 30px;
        text-align: center;
        box-shadow: 0 8px 24px rgba(2,136,209,0.25), 0 4px 8px rgba(0,0,0,0.1);
        position: relative;
        overflow: hidden;
    '>
        <div style='position: absolute; top: -50%; right: -10%; width: 300px; height: 300px; background: rgba(255,255,255,0.1); border-radius: 50%; filter: blur(60px);'></div>
        <div style='position: relative; z-index: 1;'>
            <h1 style='margin: 0; color: white; font-size: 2.5em; font-weight: 700; letter-spacing: -0.5px; text-shadow: 0 2px 8px rgba(0,0,0,0.2);'>🔍 Tra Cứu & Dữ Liệu Kháng Sinh</h1>
            <p style='margin: 12px 0 0 0; color: rgba(255,255,255,0.95); font-size: 1.15em; font-weight: 400; line-height: 1.6;'>
                Database <strong style='font-weight: 700; font-size: 1.1em;'>{ab_count}</strong> kháng sinh tiêm truyền thông dụng • Tích hợp tính liều tự động
            </p>
        </div>
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
        # Recently viewed antibiotics
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
        
        # Recent Calculations (Phase 4)
        st.markdown("---")
        st.markdown("### 🧮 Tính liều gần đây")
        
        # Render recent calculations inline (not in sidebar)
        from .recent_calculations import get_recent_calculations, format_calculation_summary, remove_calculation
        recent_calcs = get_recent_calculations(limit=10)
        
        if recent_calcs:
            st.info(f"📊 **{len(recent_calcs)}** calculations gần đây")
            for i, calc in enumerate(recent_calcs):
                summary = format_calculation_summary(calc)
                timestamp = calc.get('timestamp', None)
                
                col1, col2 = st.columns([4, 1])
                with col1:
                    if st.button(
                        f"📋 {summary}",
                        key=f"recent_calc_{calc.get('id', i)}",
                        use_container_width=True
                    ):
                        # Load calculation
                        st.session_state['load_calculation'] = calc
                        st.session_state['view_antibiotic'] = calc.get('antibiotic_name')
                        st.rerun()
                
                with col2:
                    if st.button("🗑️", key=f"del_calc_{calc.get('id', i)}", help="Xóa"):
                        remove_calculation(calc.get('id'))
                        st.rerun()
                
                if timestamp:
                    st.caption(f"⏰ {timestamp.strftime('%d/%m/%Y %H:%M') if isinstance(timestamp, type(datetime.now())) else timestamp}")
                
                if i < len(recent_calcs) - 1:
                    st.markdown("---")
        else:
            st.info("💡 Chưa có calculations nào. Tính liều để lưu vào đây!")
    
    st.markdown("---")
    
    # ========== SEARCH & FILTER SECTION ==========
    st.markdown("""
    <h2 style='font-size: 1.8em; font-weight: 700; color: #1976D2; margin: 30px 0 20px 0; letter-spacing: -0.3px;'>🔍 Tìm kiếm</h2>
    """, unsafe_allow_html=True)
    
    # Condition-based search option
    search_mode = st.radio(
        "Chế độ tìm kiếm:",
        ["🔍 Tên thuốc / Biệt dược", "🏥 Theo bệnh lý"],
        key="search_mode",
        horizontal=True,
        help="Tìm theo tên thuốc hoặc theo bệnh lý lâm sàng"
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Condition-based search
    if search_mode == "🏥 Theo bệnh lý":
        conditions = get_all_conditions()
        condition_map = {
            "Sepsis": "Sepsis / Nhiễm khuẩn huyết",
            "UTI": "UTI / Nhiễm khuẩn tiết niệu",
            "Pneumonia": "Viêm phổi",
            "Meningitis": "Viêm màng não",
            "Intra-abdominal": "Nhiễm khuẩn ổ bụng",
            "Skin_Soft_Tissue": "Nhiễm khuẩn da và mô mềm",
            "Osteomyelitis": "Viêm xương tủy",
            "Endocarditis": "Viêm nội tâm mạc",
            "Cellulitis": "Viêm mô tế bào",
            "Diabetic_Foot": "Nhiễm khuẩn bàn chân ĐTĐ",
            "Prostatitis": "Viêm tuyến tiền liệt"
        }
        
        selected_condition = st.selectbox(
            "Chọn bệnh lý:",
            options=conditions,
            format_func=lambda x: condition_map.get(x, x),
            key="condition_select"
        )
        
        if selected_condition:
            condition_data = search_by_condition(selected_condition)
            if condition_data:
                st.markdown("---")
                st.markdown(f"""
                <div style='
                    background: linear-gradient(135deg, rgba(25,118,210,0.1) 0%, rgba(25,118,210,0.05) 100%);
                    padding: 20px;
                    border-radius: 16px;
                    border-left: 4px solid #1976D2;
                    margin: 20px 0;
                '>
                    <h3 style='font-size: 1.4em; font-weight: 700; color: #1976D2; margin-bottom: 10px;'>🏥 {condition_data['description']}</h3>
                    <p style='color: #666; margin-bottom: 15px;'>{condition_data.get('notes', '')}</p>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown("### 💊 Khuyến cáo điều trị:")
                
                for idx, therapy in enumerate(condition_data.get('empiric_therapy', []), 1):
                    priority_colors = {
                        "First-line": "#4CAF50",
                        "Alternative": "#FF9800",
                        "Add-on": "#2196F3",
                        "Complex UTI": "#9C27B0",
                        "Severe HAP/VAP": "#F44336",
                        "MRSA": "#F44336"
                    }
                    priority_color = priority_colors.get(therapy.get('priority', ''), "#666")
                    
                    with st.expander(f"**{idx}. {therapy['antibiotic']}** - {therapy.get('priority', '')}", expanded=(idx == 1)):
                        st.markdown(f"""
                        <div style='padding: 12px; background: rgba(25,118,210,0.03); border-radius: 8px; margin-bottom: 10px;'>
                            <p style='margin: 5px 0;'><strong>💡 Lý do:</strong> {therapy.get('rationale', '')}</p>
                            <p style='margin: 5px 0;'><strong>💉 Liều dùng:</strong> <span style='color: #1976D2; font-weight: 600;'>{therapy.get('dosing', '')}</span></p>
                            <span style='background: {priority_color}; color: white; padding: 4px 10px; border-radius: 12px; font-size: 0.85em; font-weight: 600;'>{therapy.get('priority', '')}</span>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        # Quick link to antibiotic detail
                        if therapy['antibiotic'] in ANTIBIOTICS_DATABASE:
                            if st.button(f"📖 Xem chi tiết {therapy['antibiotic']}", key=f"condition_{selected_condition}_{idx}"):
                                st.session_state['view_antibiotic'] = therapy['antibiotic']
                                st.rerun()
                
                st.markdown("---")
                return  # Exit early for condition-based search
    
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
        if st.button("🗑️", help="Xóa tìm kiếm", use_container_width=True, key="clear_search_btn"):
            st.session_state.ab_search_trigger = ""
            st.rerun()
    
    # Show autocomplete suggestions in a nicer format
    if search_query and len(search_query) >= 1:
        suggestions = get_antibiotic_autocomplete_suggestions(search_query, max_suggestions=5)
        if suggestions:
            st.markdown("**💡 Gợi ý tìm kiếm:**")
            suggestion_cols = st.columns(min(5, len(suggestions)))
            for idx, suggestion in enumerate(suggestions):
                with suggestion_cols[idx]:
                    # Sanitize suggestion for button key to avoid conflicts
                    safe_key = f"autocomplete_{idx}_{str(suggestion).replace(' ', '_').replace('-', '_').replace('/', '_').replace('(', '').replace(')', '')[:30]}"
                    if st.button(f"💊 {suggestion}", key=safe_key, use_container_width=True):
                        # Ensure suggestion is a valid string
                        if suggestion:
                            # Use trigger instead of direct assignment to avoid widget conflict
                            st.session_state.ab_search_trigger = str(suggestion).strip()
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
                # Sanitize recent for button key to avoid conflicts
                safe_key = f"recent_{idx}_{str(recent).replace(' ', '_').replace('-', '_').replace('/', '_').replace('(', '').replace(')', '')[:30]}"
                if st.button(f"↩️ {recent}", key=safe_key, use_container_width=True):
                    # Ensure recent is a valid string
                    if recent:
                        # Use trigger instead of direct assignment to avoid widget conflict
                        st.session_state.ab_search_trigger = str(recent).strip()
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
    
    # Enhanced Filters (Phase 4 - Task 4.3: Smart Search Enhancement)
    if view_mode == "📋 Duyệt tất cả":
        with st.expander("🔽 **Bộ Lọc Nâng Cao**", expanded=True):
            col1, col2, col3, col4 = st.columns(4)
            
            all_groups = sorted(list(set([ab.get('group', 'Khác') for ab in ANTIBIOTICS_DATABASE.values()])))
            
            with col1:
                filter_group = st.selectbox(
                    "📦 Nhóm kháng sinh:",
                    ["Tất cả"] + all_groups,
                    key="filter_group_main",
                    help="Lọc theo nhóm kháng sinh (Penicillin, Cephalosporin, etc.)"
                )
            
            with col2:
                filter_route = st.selectbox(
                    "💉 Đường dùng:",
                    ["Tất cả", "IV", "IM", "PO"],
                    key="filter_route_main",
                    help="Lọc theo đường dùng (tiêm tĩnh mạch, tiêm bắp, uống)"
                )
            
            with col3:
                filter_aware = st.selectbox(
                    "🏥 AWaRe:",
                    ["Tất cả", "ACCESS", "WATCH", "RESERVE"],
                    key="filter_aware_main",
                    help="Lọc theo phân loại AWaRe của WHO"
                )
            
            with col4:
                # Additional filter: Pregnancy safety
                filter_pregnancy = st.selectbox(
                    "🤰 Thai kỳ:",
                    ["Tất cả", "A", "B", "C", "D", "X"],
                    key="filter_pregnancy_main",
                    help="Lọc theo độ an toàn trong thai kỳ (FDA category)"
                )
            
            # Filter summary
            active_filters = []
            if filter_group != "Tất cả":
                active_filters.append(f"Nhóm: {filter_group}")
            if filter_route != "Tất cả":
                active_filters.append(f"Đường: {filter_route}")
            if filter_aware != "Tất cả":
                active_filters.append(f"AWaRe: {filter_aware}")
            if filter_pregnancy != "Tất cả":
                active_filters.append(f"Thai kỳ: {filter_pregnancy}")
            
            if active_filters:
                st.info(f"🔍 **Đang lọc:** {', '.join(active_filters)}")
    
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
                # Enhanced no results state
                st.markdown(f"""
                <div style='
                    background: linear-gradient(135deg, rgba(255,152,0,0.08) 0%, rgba(255,152,0,0.02) 100%);
                    padding: 25px;
                    border-radius: 16px;
                    border: 2px solid rgba(255,152,0,0.3);
                    margin: 20px 0;
                '>
                    <div style='font-size: 2.5em; margin-bottom: 10px;'>❌</div>
                    <h3 style='font-size: 1.2em; font-weight: 700; color: #FF9800; margin-bottom: 8px;'>Không tìm thấy kết quả</h3>
                    <p style='color: #666; margin: 0;'>Không tìm thấy kết quả nào cho '<strong>{html.escape(search_query)}</strong>'</p>
                </div>
                """, unsafe_allow_html=True)
                
                # Show autocomplete suggestions as fallback
                suggestions = get_antibiotic_autocomplete_suggestions(search_query, max_suggestions=5)
                if suggestions:
                    st.markdown("""
                    <div style='margin: 20px 0 10px 0;'>
                        <strong style='font-size: 1.1em; color: #1976D2;'>💡 Gợi ý tìm kiếm:</strong>
                    </div>
                    """, unsafe_allow_html=True)
                    sugg_cols = st.columns(min(5, len(suggestions)))
                    for idx, suggestion in enumerate(suggestions):
                        with sugg_cols[idx]:
                            # Sanitize suggestion for key
                            safe_sugg_key = f"sugg_{str(suggestion).replace(' ', '_').replace('-', '_').replace('/', '_')}"
                            if st.button(f"💊 {suggestion}", key=safe_sugg_key, use_container_width=True):
                                # Ensure suggestion is a valid string
                                if suggestion:
                                    # Use trigger instead of direct assignment to avoid widget conflict
                                    st.session_state.ab_search_trigger = str(suggestion).strip()
                                    st.rerun()
                else:
                    st.markdown("""
                    <div style='
                        background: rgba(25,118,210,0.05);
                        padding: 15px 20px;
                        border-radius: 12px;
                        border-left: 4px solid #1976D2;
                        margin-top: 15px;
                    '>
                        <strong style='color: #1976D2;'>💡 Gợi ý:</strong> Thử tìm với tên thuốc, biệt dược, nhóm thuốc (ví dụ: <strong>Beta-lactam</strong>), hoặc chỉ định (ví dụ: <strong>MRSA</strong>, <strong>Sepsis</strong>, <strong>UTI</strong>)
                    </div>
                    """, unsafe_allow_html=True)
        else:
            # Enhanced empty state with better design
            st.markdown("""
            <div style='
                background: linear-gradient(135deg, rgba(25,118,210,0.05) 0%, rgba(25,118,210,0.02) 100%);
                padding: 30px;
                border-radius: 16px;
                border: 2px dashed rgba(25,118,210,0.2);
                text-align: center;
                margin: 20px 0;
            '>
                <div style='font-size: 3em; margin-bottom: 15px;'>🔍</div>
                <h3 style='font-size: 1.3em; font-weight: 700; color: #1976D2; margin-bottom: 10px;'>Nhập từ khóa để tìm kiếm</h3>
                <p style='color: #666; font-size: 1em; margin: 0;'>Ví dụ: <strong>Vancomycin</strong>, <strong>Ceftriaxone</strong>, <strong>MRSA</strong>, <strong>Sepsis</strong></p>
            </div>
            """, unsafe_allow_html=True)
            st.markdown("---")
            
            # Show popular/quick links with enhanced design
            st.markdown("""
            <h3 style='font-size: 1.5em; font-weight: 700; color: #1976D2; margin: 25px 0 15px 0;'>⚡ Truy cập nhanh</h3>
            """, unsafe_allow_html=True)
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
            filter_aware if view_mode == "📋 Duyệt tất cả" else "Tất cả",
            filter_pregnancy if view_mode == "📋 Duyệt tất cả" else "Tất cả"
        )
        
        if filtered_ab:
            st.markdown(f"""
            <div style='
                background: linear-gradient(135deg, rgba(76,175,80,0.1) 0%, rgba(76,175,80,0.05) 100%);
                padding: 15px 20px;
                border-radius: 12px;
                border-left: 4px solid #4CAF50;
                margin: 20px 0;
            '>
                <strong style='font-size: 1.1em; color: #2e7d32;'>📋 Hiển thị <span style='font-size: 1.2em;'>{len(filtered_ab)}</span> kháng sinh</strong>
            </div>
            """, unsafe_allow_html=True)
            st.markdown("---")
            
            # Display as compact list with enhanced header
            st.markdown("""
            <h3 style='font-size: 1.5em; font-weight: 700; color: #1976D2; margin: 25px 0 15px 0;'>📚 Danh sách kháng sinh</h3>
            """, unsafe_allow_html=True)
            
            # Group by category for better organization
            groups_dict = {}
            for ab_name, ab_data in filtered_ab.items():
                group = ab_data.get('group', 'Khác')
                if group not in groups_dict:
                    groups_dict[group] = []
                groups_dict[group].append((ab_name, ab_data))
            
            # Display by group with enhanced styling
            for group in sorted(groups_dict.keys()):
                if len(groups_dict) > 1:
                    st.markdown(f"""
                    <h4 style='
                        font-size: 1.3em;
                        font-weight: 700;
                        color: #1976D2;
                        margin: 30px 0 15px 0;
                        padding-bottom: 10px;
                        border-bottom: 2px solid rgba(25,118,210,0.2);
                    '>{group} <span style='font-size: 0.85em; color: #666; font-weight: 500;'>({len(groups_dict[group])} thuốc)</span></h4>
                    """, unsafe_allow_html=True)
                
                for idx, (ab_name, ab_data) in enumerate(sorted(groups_dict[group], key=lambda x: x[0])):
                    render_compact_antibiotic_card(ab_name, ab_data, key_prefix=f"browse_{group}_{idx}_")
                    if idx < len(groups_dict[group]) - 1:
                        st.markdown("<hr style='margin: 8px 0; border: none; border-top: 1px solid #f0f0f0;'>", unsafe_allow_html=True)
                
                if group != list(groups_dict.keys())[-1]:
                    st.markdown("<br>", unsafe_allow_html=True)
        else:
            # Enhanced empty filter state
            st.markdown("""
            <div style='
                background: linear-gradient(135deg, rgba(255,152,0,0.08) 0%, rgba(255,152,0,0.02) 100%);
                padding: 30px;
                border-radius: 16px;
                border: 2px solid rgba(255,152,0,0.3);
                text-align: center;
                margin: 20px 0;
            '>
                <div style='font-size: 3em; margin-bottom: 15px;'>🔍</div>
                <h3 style='font-size: 1.3em; font-weight: 700; color: #FF9800; margin-bottom: 10px;'>Không có kháng sinh nào thỏa mãn bộ lọc</h3>
                <p style='color: #666; margin-bottom: 20px;'>Thử điều chỉnh bộ lọc để xem thêm kết quả</p>
            </div>
            """, unsafe_allow_html=True)
            if st.button("🔄 Xóa bộ lọc", use_container_width=True, type="primary"):
                st.rerun()



def render_antibiotic_lookup():
    """Legacy function - redirects to render_database for backward compatibility"""
    render_database()


