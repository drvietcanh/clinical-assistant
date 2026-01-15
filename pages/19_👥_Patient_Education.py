"""
Patient Education Materials Module
Educational materials for patients in simple language
"""

import streamlit as st
from collections import Counter
from utils.page_helper import setup_page, render_standard_footer
from components.page_sidebar import render_standard_sidebar
from components.ui import render_hero
from patient_education.data import (
    get_all_topics,
    get_topics_by_category,
    get_category_list,
)
from patient_education.display import render_patient_education_content
from components.patient_education import (
    render_topic_grid,
    render_enhanced_search,
    render_category_filters,
    render_enhanced_content,
    render_related_topics,
    render_hero_section,
    filter_topics_by_search,
)

# ================== PAGE SHELL (GIỐNG DISEASE ENCYCLOPEDIA) ==================

setup_page(
    page_title="Giáo dục Bệnh nhân",
    page_icon="👥",
    description="Tài liệu giáo dục bệnh nhân với ngôn ngữ đơn giản, dễ hiểu",
)

# Sidebar tối giản – đưa tương tác chính ra khu vực nội dung
filters = render_standard_sidebar(
    title="Giáo dục Bệnh nhân",
    icon="👥",
    description="Tra cứu tài liệu giáo dục với ngôn ngữ đơn giản, dễ giải thích cho bệnh nhân.",
    module_group="📖 Thông tin Y học",
    filters={},
    info_text="""
    **👥 Patient Education**
    - Tờ rơi/tài liệu giải thích bệnh, thuốc, lối sống
    - Dùng ngôn ngữ đơn giản, dễ hiểu
    - Có thể in phát cho bệnh nhân
    
    **💡 Lưu ý:**
    - Không thay thế tư vấn trực tiếp của bác sĩ
    - Cần cá nhân hóa giải thích cho từng bệnh nhân
    """,
)

# Hero giống mô hình Disease Encyclopedia
all_topics = get_all_topics()

render_hero(
    title="Giáo dục Bệnh nhân",
    subtitle="Patient Education",
    description="Tra cứu nhanh tờ rơi/tài liệu giải thích bệnh, thuốc và lối sống để tư vấn cho bệnh nhân.",
    icon="👥",
    gradient=("#4facfe", "#00f2fe"),
)

st.write("")  # spacer

# ================== TRẠNG THÁI ĐIỀU HƯỚNG (VIEW STATE) ==================

if "pe_view" not in st.session_state:
    st.session_state.pe_view = "home"  # home, search, category, detail
if "pe_category" not in st.session_state:
    st.session_state.pe_category = None
if "pe_selected_topic" not in st.session_state:
    st.session_state.pe_selected_topic = None

# ================== THANH TÌM KIẾM TRUNG TÂM ==================

col_search, col_space = st.columns([3, 1])
with col_search:
    search_query = render_enhanced_search(
        all_topics,
        placeholder="Nhập tên bệnh, thuốc, lối sống... (VD: Tăng huyết áp, Amoxicillin, chế độ ăn đái tháo đường)",
        show_filters=True,
        show_suggestions=True,
        key="patient_edu_search",
    )

# Nếu có search → ưu tiên chế độ search
if search_query and search_query.strip():
    st.session_state.pe_view = "search"
elif st.session_state.pe_view == "search" and not (search_query and search_query.strip()):
    # Nếu xoá hết nội dung ô tìm kiếm → quay về home
    st.session_state.pe_view = "home"


def _set_detail_view(topic):
    """Helper: chuyển sang view chi tiết cho một topic."""
    st.session_state.pe_selected_topic = topic
    st.session_state.pe_view = "detail"


# ================== BỘ ĐIỀU KHIỂN VIEW ==================

if st.session_state.pe_view == "search":
    # ----- SEARCH RESULTS VIEW -----
    st.subheader(f"Kết quả tìm kiếm cho: '{search_query}'")

    # Lọc theo search (trên toàn bộ topics)
    topics = filter_topics_by_search(all_topics, search_query)

    if topics:
        st.info(f"📊 Tìm thấy **{len(topics)}** tài liệu phù hợp.")
        st.markdown("")
        
        # Lưới thẻ kết quả – ưu tiên scan nhanh
        render_topic_grid(
            topics,
            columns=3,
            show_preview=True,
            search_query=search_query,
        )
        
        st.markdown("---")
        st.markdown("### 📖 Xem chi tiết")
        st.caption("Chọn tài liệu bên dưới để xem nội dung đầy đủ.")
        
        for idx, topic in enumerate(topics):
            with st.expander(
                f"**{topic.title_vn}** ({topic.category})", expanded=(idx == 0)
            ):
                render_enhanced_content(
                    topic,
                    show_toc=True,
                    show_progress=True,
                    search_query=search_query,
                )
                render_related_topics(topic, all_topics)
                render_patient_education_content(topic)
    else:
        from components.ui import render_info_box as _render_info_box

        _render_info_box(
            "Không tìm thấy tài liệu. Vui lòng thử lại với từ khóa khác hoặc điều chỉnh cách diễn đạt.",
            type="warning",
        )
        if st.button("🔙 Quay lại trang chủ"):
            st.session_state.pe_view = "home"
            st.session_state.pe_selected_topic = None
            st.session_state.pe_category = None
            st.rerun()

elif st.session_state.pe_view == "category":
    # ----- CATEGORY VIEW (DANH SÁCH THEO CHUYÊN KHOA) -----
    cat = st.session_state.pe_category

    col_back, col_title = st.columns([1, 5])
    with col_back:
        if st.button("⬅️ Quay lại", key="pe_cat_back"):
            st.session_state.pe_view = "home"
            st.session_state.pe_category = None
            st.rerun()

    with col_title:
        st.subheader(f"📂 Chuyên khoa / Chủ đề: {cat}")

    if not cat or cat == "Tất cả":
        topics = all_topics
    else:
        topics = get_topics_by_category(cat)

    if topics:
        st.info(f"📊 Có **{len(topics)}** tài liệu trong chủ đề này.")

        # Hiển thị dạng danh sách dọc với preview ngắn
        for topic in topics:
            with st.expander(f"**{topic.title_vn}** ({topic.category})", expanded=False):
                render_enhanced_content(
                    topic,
                    show_toc=True,
                    show_progress=False,
                    search_query=None,
                )
                render_related_topics(topic, all_topics)
                render_patient_education_content(topic)
    else:
        st.info("Hiện chưa có tài liệu cho chủ đề này.")

elif st.session_state.pe_view == "detail":
    # ----- DETAIL VIEW (MỘT TÀI LIỆU) -----
    topic = st.session_state.pe_selected_topic

    col_back, col_title = st.columns([1, 5])
    with col_back:
        if st.button("⬅️ Quay lại", key="pe_detail_back"):
            # Đơn giản: quay lại home. Sau có thể mở rộng nhớ view trước đó.
            st.session_state.pe_view = "home"
            st.session_state.pe_selected_topic = None
            st.rerun()

    if topic:
        st.markdown(
            f"## {topic.title_vn} <span style='font-size: 0.7em; color: gray;'>({topic.category})</span>",
            unsafe_allow_html=True,
        )
        st.markdown("---")
        render_enhanced_content(
            topic,
            show_toc=True,
            show_progress=True,
            search_query=None,
        )
        render_related_topics(topic, all_topics)
        render_patient_education_content(topic)
    else:
        st.error("Không tìm thấy nội dung tài liệu.")
        if st.button("🔙 Quay lại trang chủ", key="pe_detail_back_home"):
            st.session_state.pe_view = "home"
            st.session_state.pe_selected_topic = None
            st.rerun()

else:
    # ================== HOME DASHBOARD ==================

    # A. Tài liệu nổi bật / thường dùng
    st.markdown("### 🔥 Tài liệu Phổ biến")

    # Chọn một số ID/chủ đề thường gặp – tạm thời lọc theo category Disease/Lifestyle/Medication
    featured_topics = [
        t
        for t in all_topics
        if t.category in ("Disease", "Medication", "Lifestyle")
    ][:6]

    feat_cols = st.columns(3)
    for i, topic in enumerate(featured_topics):
        with feat_cols[i % 3]:
            with st.container(border=True):
                st.markdown(f"**{topic.title_vn}**")
                st.caption(topic.category)
                if st.button(
                    "📖 Xem chi tiết", key=f"pe_feat_{i}", use_container_width=True
                ):
                    _set_detail_view(topic)
                    st.rerun()

    # B. Lưới chuyên khoa / chủ đề
    st.markdown("---")
    st.markdown("### 📂 Duyệt theo Chuyên khoa / Chủ đề")

    categories = get_category_list()
    category_counts = Counter(t.category for t in all_topics)

    # Map chuyên khoa → icon + tên tiếng Việt
    category_metadata = {
        "Disease": {"icon": "🩺", "name_vn": "Bệnh lý"},
        "Medication": {"icon": "💊", "name_vn": "Thuốc"},
        "Lifestyle": {"icon": "🏃", "name_vn": "Lối sống"},
        "Procedure": {"icon": "⚕️", "name_vn": "Thủ thuật / Can thiệp"},
        "Cardiovascular": {"icon": "🫀", "name_vn": "Tim mạch"},
        "Respiratory": {"icon": "🫁", "name_vn": "Hô hấp"},
        "Diabetes": {"icon": "🍬", "name_vn": "Đái tháo đường"},
        "Neurological": {"icon": "🧠", "name_vn": "Thần kinh"},
        "Gastrointestinal": {"icon": "🫄", "name_vn": "Tiêu hóa"},
        "Dermatology": {"icon": "👤", "name_vn": "Da liễu"},
        "Infectious": {"icon": "🦠", "name_vn": "Truyền nhiễm"},
        "Other": {"icon": "📋", "name_vn": "Khác"},
    }

    cols = st.columns(4)
    for i, cat in enumerate(categories):
        with cols[i % 4]:
            meta = category_metadata.get(cat, {"icon": "📁", "name_vn": cat})
            base_name = meta["name_vn"]
            icon = meta["icon"]
            count = category_counts.get(cat, 0)
            display_name = f"{base_name} ({count})" if count else base_name

            if st.button(
                f"{icon} {display_name}",
                use_container_width=True,
                key=f"pe_cat_{i}",
            ):
                st.session_state.pe_category = cat
                st.session_state.pe_view = "category"
                st.rerun()

    # C. Thống kê tổng
    st.markdown("---")
    total_topics = len(all_topics)
    st.caption(f"📚 Cơ sở dữ liệu hiện có: **{total_topics}** tài liệu giáo dục bệnh nhân.")

# Footer
render_standard_footer(disclaimer=True)
