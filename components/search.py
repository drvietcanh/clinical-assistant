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
    """Render search bar and results"""
    st.markdown("### 🔍 Tìm Kiếm Nhanh")
    
    search_query = st.text_input(
        "Tìm calculator, xét nghiệm, hoặc phác đồ...",
        placeholder="Ví dụ: CHA2DS2VASc, troponin, sepsis...",
        help="Gõ tên calculator hoặc chuyên khoa để tìm nhanh",
        key="search_box"
    )
    
    if search_query:
        results = search_calculators(search_query)
        if results:
            st.success(f"✅ Tìm thấy **{len(results)}** kết quả:")
            
            # Display search results in columns
            cols = st.columns(min(3, len(results)))
            for idx, (calc_id, calc_info) in enumerate(results[:6]):  # Show max 6 results
                with cols[idx % 3]:
                    is_fav = calc_id in st.session_state.favorites
                    fav_icon = "⭐" if is_fav else "☆"
                    
                    with st.container():
                        st.markdown(f"""
                        **{calc_info['icon']} {calc_info['name']}**  
                        📂 {calc_info['category']} | 📄 {calc_info['page']}
                        """)
                        
                        col_fav, col_go = st.columns([1, 2])
                        with col_fav:
                            if st.button(fav_icon, key=f"fav_search_{calc_id}"):
                                if is_fav:
                                    from .favorites import remove_from_favorites
                                    remove_from_favorites(calc_id)
                                else:
                                    from .favorites import add_to_favorites
                                    add_to_favorites(calc_id)
                                st.rerun()
                        
                        with col_go:
                            if st.button("Mở", key=f"open_search_{calc_id}", type="primary"):
                                from .recently_used import add_to_recently_used
                                add_to_recently_used(calc_id)
                                st.info(f"Đang mở {calc_info['name']} trong module {calc_info['page']}...")
                        
                        st.markdown("---")
        else:
            st.warning(f"❌ Không tìm thấy kết quả cho: **{search_query}**")
            st.caption("💡 Thử tìm với từ khóa khác: tim mạch, cấp cứu, xét nghiệm, thuốc...")
    
    st.markdown("---")

