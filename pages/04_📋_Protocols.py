"""
Protocols Module - Clinical Treatment Protocols
Main Router - Uses routing dictionary for protocol rendering
"""

import streamlit as st
from utils.page_helper import setup_page, render_standard_footer
from config.protocol_routing import render_protocol_by_name
from components.protocols_sidebar import render_protocols_sidebar
from components.protocols_article_link import render_article_link
from components.score_links_from_content import render_score_links_from_protocol

# Standard page setup with mobile optimizations
setup_page(
    page_title="Phác đồ điều trị",
    page_icon="📋",
    description="Các phác đồ điều trị chuẩn theo hướng dẫn quốc tế",
    mobile_header=True
)

# Breadcrumbs
try:
    from components.mobile_page_wrapper import render_breadcrumbs
    render_breadcrumbs([
        ("Trang chủ", "/"),
        ("Guideline", None)
    ])
except ImportError:
    pass

# ========== SIDEBAR ==========
with st.sidebar:
    specialty, protocol, use_deep_link = render_protocols_sidebar()

# ========== MAIN CONTENT ==========

# Clear deep link state after using it (to prevent re-triggering on refresh)
if use_deep_link:
    if 'protocol_specialty' in st.session_state:
        del st.session_state['protocol_specialty']
    if 'protocol_to_open' in st.session_state:
        del st.session_state['protocol_to_open']
    if 'protocol_function' in st.session_state:
        del st.session_state['protocol_function']

# Show info with deep link indicator if applicable
info_text = f"""
**Chuyên khoa:** {specialty}

**Phác đồ đang xem:** {protocol.split(' ', 1)[1] if ' ' in protocol else protocol}
"""
if use_deep_link:
    info_text += "\n\n*🔗 Đã tự động mở từ bài viết chuyên sâu*"

st.info(info_text)

st.markdown("---")

# render_article_link is now imported from components.protocols_article_link
# render_score_links_from_protocol is now imported from components.score_links_from_content

# Route to appropriate protocol using dictionary-based routing
protocol_rendered = render_protocol_by_name(protocol, render_article_link, render_score_links_from_protocol)

if not protocol_rendered:
    # Default case: Protocol not found
    st.warning(f"""
    ⚠️ **Không tìm thấy protocol tương ứng**
    
    Protocol được chọn: **{protocol}**
    
    Vui lòng:
    - Kiểm tra lại tên protocol
    - Chọn protocol khác từ danh sách
    - Liên hệ admin nếu protocol này nên có trong hệ thống
    """)
    st.info("💡 **Gợi ý:** Hãy chọn một protocol từ danh sách ở sidebar bên trái.")

# ========== FOOTER ==========
render_standard_footer(disclaimer=False)
