"""
Search Component
Global search functionality for calculators
"""

import streamlit as st
from config.calculators import ALL_CALCULATORS


def search_calculators(query):
    """Search calculators by name or category"""
    query = query.lower()
    results = []
    for calc_id, calc_info in ALL_CALCULATORS.items():
        if query in calc_info['name'].lower() or query in calc_info['category'].lower():
            results.append((calc_id, calc_info))
    return results


def render_search():
    """Render enhanced search bar and results"""
    # Header with icon
    st.markdown("### 🔍 Tìm Kiếm Nhanh")
    st.caption("Tìm kiếm trong tất cả calculators, xét nghiệm, và protocols")
    
    # Enhanced search input
    col_search, col_help = st.columns([4, 1])
    with col_search:
        search_query = st.text_input(
            "🔎 Nhập từ khóa...",
            placeholder="Ví dụ: CHA2DS2VASc, troponin, sepsis, SOFA...",
            help="Gõ tên calculator, chuyên khoa, hoặc từ khóa bất kỳ",
            key="search_box",
            label_visibility="collapsed"
        )
    
    if search_query:
        results = search_calculators(search_query)
        if results:
            st.success(f"✅ **{len(results)}** kết quả tìm thấy")
            
            # Display results in modern cards
            num_cols = min(3, len(results))
            cols = st.columns(num_cols)
            
            for idx, (calc_id, calc_info) in enumerate(results[:9]):  # Show max 9 results
                with cols[idx % num_cols]:
                    is_fav = calc_id in st.session_state.favorites
                    fav_icon = "⭐" if is_fav else "☆"
                    fav_color = "#ffd54f" if is_fav else "#e0e0e0"
                    
                    st.markdown(f"""
                    <div class="search-result-card">
                        <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px;">
                            <span style="font-size: 1.5rem;">{calc_info['icon']}</span>
                            <strong style="font-size: 1rem; color: #212121;">{calc_info['name']}</strong>
                        </div>
                        <div style="font-size: 0.85rem; color: #757575; margin-bottom: 12px;">
                            📂 {calc_info['category']}<br/>
                            📄 {calc_info['page']}
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    col_fav, col_go = st.columns([1, 3])
                    with col_fav:
                        if st.button(fav_icon, key=f"fav_search_{calc_id}", help="Thêm/bỏ yêu thích"):
                            if is_fav:
                                from .favorites import remove_from_favorites
                                remove_from_favorites(calc_id)
                                st.success("Đã bỏ khỏi yêu thích")
                            else:
                                from .favorites import add_to_favorites
                                add_to_favorites(calc_id)
                                st.success("Đã thêm vào yêu thích")
                            st.rerun()
                    
                    with col_go:
                        if st.button("▶️ Mở", key=f"open_search_{calc_id}", type="primary", use_container_width=True):
                            from .recently_used import add_to_recently_used
                            add_to_recently_used(calc_id)
                            st.switch_page(calc_info['page'])
        else:
            st.warning(f"""
            **❌ Không tìm thấy kết quả cho: "{search_query}"**
            
            💡 **Gợi ý:**
            - Thử từ khóa khác: tim mạch, cấp cứu, xét nghiệm, thuốc
            - Kiểm tra chính tả
            - Dùng tên tiếng Việt hoặc tiếng Anh
            """)
    
    else:
        # Show suggestions when no search
        st.info("💡 **Mẹo tìm kiếm:** Gõ tên calculator (ví dụ: SOFA, CHA2DS2VASc) hoặc chuyên khoa (ví dụ: tim mạch, cấp cứu)")
    
    st.markdown("---")

