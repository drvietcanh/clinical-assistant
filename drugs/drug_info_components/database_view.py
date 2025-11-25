"""Drug Info - Database View (main database page)"""

import streamlit as st
import pandas as pd
from ..drug_database import DRUG_DATABASE

# Check if drug is antibiotic
try:
    from antibiotics.antibiotics_data import ANTIBIOTICS_DATABASE
except ImportError:
    ANTIBIOTICS_DATABASE = {}
from .card_components import render_compact_drug_card
from .detail_view import display_drug_info

def render_drug_database():
    """Main function to render drug database page with search and browse"""
    from .search import search_drugs, search_drugs_with_filters, get_drug_autocomplete_suggestions, get_recent_searches, add_recent_search, search_by_group, save_search, get_saved_searches, load_saved_search, delete_saved_search
    from ..drug_database import DRUG_GROUPS
    drug_count = len(DRUG_DATABASE)
    st.markdown(
        f"""
    <div style='
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 25px;
        border-radius: 15px;
        margin-bottom: 25px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    '>
        <h1 style='margin: 0; color: white; font-size: 2.2em;'>💊 Tra Cứu Dữ Liệu Thuốc</h1>
        <p style='margin: 10px 0 0 0; color: rgba(255,255,255,0.9); font-size: 1.1em;'>
            Database <strong>{drug_count}</strong> thuốc phổ biến • Tất cả chuyên khoa
        </p>
    </div>
    """
        , unsafe_allow_html=True)
    with st.expander('ℹ️ Thông tin về database', expanded=False):
        st.info(
            f"""
        **Cơ sở dữ liệu bao gồm:**
        - ✅ {drug_count} thuốc phổ biến tại Việt Nam
        - ✅ Tim mạch, Đái tháo đường, Tiêu hóa, Giảm đau, và nhiều nhóm khác
        - ✅ Tên biệt dược và tên chung
        - ✅ Liều dùng chi tiết
        - ✅ Điều chỉnh theo chức năng thận
        - ✅ Chỉ định, chống chỉ định, tác dụng phụ, tương tác
        """
            )
    if 'drug_comparison_list' in st.session_state and st.session_state[
        'drug_comparison_list']:
        comparison_list = st.session_state['drug_comparison_list']
        st.markdown('### 🔄 Danh Sách So Sánh')
        col_list, col_btn = st.columns([3, 1])
        with col_list:
            comparison_str = ', '.join([f'**{drug}**' for drug in
                comparison_list])
            st.info(f'📊 Đã chọn {len(comparison_list)} thuốc: {comparison_str}'
                )
        with col_btn:
            if st.button('📊 Mở So Sánh', use_container_width=True, type=
                'primary'):
                st.session_state['switch_to_comparison'] = True
                st.session_state['preset_comparison_drugs'
                    ] = comparison_list.copy()
                st.rerun()
        if st.button('🗑️ Xóa danh sách', key='clear_comparison'):
            st.session_state['drug_comparison_list'] = []
            st.rerun()
        st.markdown('---')
    st.markdown('### 🔍 Tìm kiếm thuốc')
    if 'drug_search_selected' in st.session_state:
        selected_value = st.session_state.pop('drug_search_selected')
        st.info(f'🔍 Đang tìm: **{selected_value}**')
        st.session_state['_auto_search_trigger'] = selected_value
    saved_searches = get_saved_searches()
    if saved_searches:
        st.markdown('**⭐ Saved Searches:**')
        saved_cols = st.columns(min(len(saved_searches), 5))
        for idx, (name, saved_data) in enumerate(list(saved_searches.items(
            ))[:5]):
            with saved_cols[idx]:
                if st.button(f'⭐ {name}', key=f'saved_{name}',
                    use_container_width=True):
                    query, filters = load_saved_search(name)
                    st.session_state['drug_search_input'] = query or ''
                    st.session_state['drug_filters'] = filters or {}
                    st.session_state['_auto_search_trigger'] = query or ''
                    st.rerun()
    col1, col2 = st.columns([3, 1])
    with col1:
        search_query = st.text_input('Nhập tên thuốc, nhóm, hoặc chỉ định',
            key='drug_search_input', placeholder=
            'Ví dụ: Metformin, Omeprazole, tăng huyết áp...', value=st.
            session_state.get('drug_search_input', ''))
    with col2:
        st.markdown('<br>', unsafe_allow_html=True)
        search_button = st.button('🔍 Tìm', use_container_width=True)
    with st.expander('🔍 Advanced Filters', expanded=False):
        col1, col2, col3 = st.columns(3)
        if 'drug_filters' not in st.session_state:
            st.session_state['drug_filters'] = {}
        filters = st.session_state['drug_filters']
        with col1:
            filter_groups = st.multiselect('Nhóm thuốc', options=list(
                DRUG_GROUPS.keys()), default=filters.get('groups', []), key
                ='filter_groups')
            filter_routes = st.multiselect('Đường dùng', options=['PO', 'IV',
                'IM', 'SC', 'Inhalation', 'Rectal', 'Topical'], default=
                filters.get('routes', []), key='filter_routes')
        with col2:
            filter_pregnancy = st.selectbox('Phân loại thai kỳ', options=[
                'Tất cả', 'A', 'B', 'C', 'D', 'X'], index=0 if filters.get(
                'pregnancy', 'Tất cả') == 'Tất cả' else ['A', 'B', 'C', 'D', 'X']
                .index(filters.get('pregnancy', 'Tất cả')) + 1 if filters.get(
                'pregnancy', 'Tất cả') in ['A', 'B', 'C', 'D', 'X'] else 0,
                key='filter_pregnancy')
            filter_monitoring = st.checkbox('Cần theo dõi', value=
                filters.get('requires_monitoring', False), key=
                'filter_monitoring')
        with col3:
            filter_renal = st.checkbox('Có điều chỉnh theo thận', value=
                filters.get('has_renal_adjustment', False), key='filter_renal')
            filter_black_box = st.checkbox('Có cảnh báo Black Box', value=
                filters.get('has_black_box', False), key='filter_black_box')
        # Convert 'Tất cả' back to 'All' for internal processing
        pregnancy_value = 'All' if filter_pregnancy == 'Tất cả' else filter_pregnancy
        st.session_state['drug_filters'] = {'groups': filter_groups,
            'routes': filter_routes, 'pregnancy': pregnancy_value,
            'requires_monitoring': filter_monitoring,
            'has_renal_adjustment': filter_renal, 'has_black_box':
            filter_black_box}
        col_save1, col_save2 = st.columns([2, 1])
        with col_save1:
            save_search_name = st.text_input('Lưu tìm kiếm với tên:', key=
                'save_search_name', placeholder='Ví dụ: Tìm kiếm của tôi')
        with col_save2:
            st.markdown('<br>', unsafe_allow_html=True)
            if st.button('💾 Lưu Tìm Kiếm', key='save_search_btn',
                use_container_width=True):
                if save_search_name:
                    save_search(save_search_name, search_query, st.
                        session_state['drug_filters'])
                    st.success(f'✅ Đã lưu: {save_search_name}')
                    st.rerun()
                else:
                    st.warning('Vui lòng nhập tên cho tìm kiếm')
    if search_query and len(search_query) >= 1:
        suggestions = get_drug_autocomplete_suggestions(search_query,
            max_suggestions=5)
        if suggestions:
            st.markdown('**Gợi ý:**')
            suggestion_cols = st.columns(min(5, len(suggestions)))
            for idx, suggestion in enumerate(suggestions[:5]):
                with suggestion_cols[idx]:
                    safe_suggestion_key = (
                        f"suggest_{str(suggestion).replace(' ', '_').replace('-', '_').replace('/', '_')}"
                        )
                    if st.button(f'💊 {suggestion}', key=safe_suggestion_key,
                        use_container_width=True):
                        st.session_state['drug_search_selected'] = str(
                            suggestion)
                        st.rerun()
    recent = get_recent_searches()
    if recent:
        st.markdown('**Tìm kiếm gần đây:**')
        recent_cols = st.columns(min(len(recent), 5))
        for idx, recent_query in enumerate(recent[:5]):
            with recent_cols[idx]:
                safe_recent_key = (
                    f"recent_{str(recent_query).replace(' ', '_').replace('-', '_').replace('/', '_')}"
                    )
                if st.button(f'↩️ {recent_query}', key=safe_recent_key,
                    use_container_width=True):
                    st.session_state['drug_search_selected'] = str(recent_query
                        )
                    st.rerun()
    st.markdown('---')
    auto_search_query = None
    if '_auto_search_trigger' in st.session_state:
        auto_search_query = st.session_state.pop('_auto_search_trigger')
    effective_query = auto_search_query if auto_search_query else search_query
    filters = st.session_state.get('drug_filters', {})
    if effective_query or search_button or any(filters.values()):
        if effective_query:
            add_recent_search(effective_query)
        results = search_drugs_with_filters(effective_query, filters)
        if results:
            st.markdown(f'### 📊 Kết quả tìm kiếm ({len(results)} thuốc)')
            page_size = 20
            page_key = 'drug_results_page'
            if page_key not in st.session_state:
                st.session_state[page_key] = 0
            current_page = st.session_state[page_key]
            start_idx = current_page * page_size
            end_idx = start_idx + page_size
            page_results = results[start_idx:end_idx]
            for drug_name, drug_data in page_results:
                render_compact_drug_card(drug_name, drug_data, search_query
                    =effective_query)
                selected_key = 'selected_drug'
                show_detail_key = 'show_detail'
                if st.session_state.get(selected_key
                    ) == drug_name and st.session_state.get(show_detail_key,
                    False):
                    display_drug_info(drug_name, drug_data)
                    safe_close_key = (
                        f"close_{str(drug_name).replace(' ', '_').replace('-', '_').replace('/', '_')}"
                        )
                    if st.button('✖️ Đóng', key=safe_close_key):
                        if selected_key in st.session_state:
                            del st.session_state[selected_key]
                        if show_detail_key in st.session_state:
                            st.session_state[show_detail_key] = False
                        st.rerun()
            if len(results) > page_size:
                total_pages = (len(results) + page_size - 1) // page_size
                st.markdown('---')
                col_prev, col_info, col_next = st.columns([1, 2, 1])
                with col_prev:
                    if st.button('◀️ Trước', disabled=current_page == 0,
                        use_container_width=True):
                        st.session_state[page_key] = max(0, current_page - 1)
                        st.rerun()
                with col_info:
                    st.markdown(
                        f'**Trang {current_page + 1}/{total_pages}** ({start_idx + 1}-{min(end_idx, len(results))} / {len(results)} thuốc)'
                        , unsafe_allow_html=True)
                with col_next:
                    if st.button('Tiếp ▶️', disabled=current_page >= 
                        total_pages - 1, use_container_width=True):
                        st.session_state[page_key] = min(total_pages - 1, 
                            current_page + 1)
                        st.rerun()
            elif page_key in st.session_state:
                st.session_state[page_key] = 0
        else:
            st.warning(
                'Không tìm thấy thuốc nào. Thử tìm kiếm với từ khóa khác.')
            st.markdown('**Gợi ý:**')
            st.info(
                """- Thử tìm bằng tên chung (generic name)
- Tìm theo nhóm thuốc (ví dụ: Cardiovascular, Diabetes)
- Tìm theo chỉ định (ví dụ: tăng huyết áp, đái tháo đường)"""
                )
    else:
        st.markdown('### 📚 Duyệt theo nhóm thuốc')
        selected_group = st.selectbox('Chọn nhóm thuốc:', ['Tất cả'] + list
            (DRUG_GROUPS.keys()), key='browse_group')
        if selected_group == 'Tất cả':
            all_drugs = list(DRUG_DATABASE.items())
            st.markdown(f'### 💊 Tất cả thuốc ({len(all_drugs)})')
        else:
            all_drugs = search_by_group(selected_group)
            st.markdown(f'### 💊 {selected_group} ({len(all_drugs)})')
        page_size = 20
        page_key = 'drug_browse_page'
        if page_key not in st.session_state:
            st.session_state[page_key] = 0
        current_page = st.session_state[page_key]
        start_idx = current_page * page_size
        end_idx = start_idx + page_size
        page_drugs = all_drugs[start_idx:end_idx]
        for drug_name, drug_data in page_drugs:
            render_compact_drug_card(drug_name, drug_data, search_query='')
            selected_key = 'selected_drug'
            show_detail_key = 'show_detail'
            if st.session_state.get(selected_key
                ) == drug_name and st.session_state.get(show_detail_key, False
                ):
                display_drug_info(drug_name, drug_data)
                safe_close_key = (
                    f"close_{str(drug_name).replace(' ', '_').replace('-', '_').replace('/', '_')}"
                    )
                if st.button('✖️ Đóng', key=safe_close_key):
                    if selected_key in st.session_state:
                        del st.session_state[selected_key]
                    if show_detail_key in st.session_state:
                        st.session_state[show_detail_key] = False
                    st.rerun()
        if len(all_drugs) > page_size:
            total_pages = (len(all_drugs) + page_size - 1) // page_size
            st.markdown('---')
            col_prev, col_info, col_next = st.columns([1, 2, 1])
            with col_prev:
                if st.button('◀️ Trước', disabled=current_page == 0, key=
                    'browse_prev', use_container_width=True):
                    st.session_state[page_key] = max(0, current_page - 1)
                    st.rerun()
            with col_info:
                st.markdown(
                    f'**Trang {current_page + 1}/{total_pages}** ({start_idx + 1}-{min(end_idx, len(all_drugs))} / {len(all_drugs)} thuốc)'
                    , unsafe_allow_html=True)
            with col_next:
                if st.button('Tiếp ▶️', disabled=current_page >= 
                    total_pages - 1, key='browse_next', use_container_width
                    =True):
                    st.session_state[page_key] = min(total_pages - 1, 
                        current_page + 1)
                    st.rerun()

