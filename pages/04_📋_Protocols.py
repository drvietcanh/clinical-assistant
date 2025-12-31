"""
Protocols Module - Clinical Treatment Protocols
Main Router - Uses routing dictionary for protocol rendering
"""

import streamlit as st
import html
from pathlib import Path
from utils.page_helper import setup_page, render_standard_footer
from components.ui import render_info_box, render_hero
from config.protocol_routing import render_protocol_by_name
from components.protocols_sidebar import render_protocols_sidebar
from components.protocols_article_link import render_article_link
from components.score_links_from_content import render_score_links_from_protocol
from components.protocol_calculators import render_calculator_links
from components.protocol_export import render_export_section
from components.protocol_related import render_related_protocols
from components.protocol_version import render_version_history
from components.protocol_dark_mode import init_theme, render_theme_toggle

# Standard page setup with mobile optimizations
setup_page(
    page_title="Phác đồ điều trị",
    page_icon="📋",
    description="Các phác đồ điều trị chuẩn theo hướng dẫn quốc tế",
    mobile_header=True
)

# Load custom CSS for modern medical interface
try:
    css_file = Path(__file__).parent.parent / "static" / "protocol_custom.css"
    if css_file.exists():
        with open(css_file, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except Exception as e:
    # Silently fail if CSS file not found
    pass

# Initialize and apply theme (dark/light mode)
init_theme()

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
# Only clear if we've successfully rendered the protocol
if use_deep_link and protocol and protocol != "Không có protocol nào":
    # Mark that we've processed the deep link
    if 'protocol_deep_link_processed' not in st.session_state:
        st.session_state['protocol_deep_link_processed'] = True
        # Clear deep link state after first use
        if 'protocol_specialty' in st.session_state:
            del st.session_state['protocol_specialty']
        if 'protocol_to_open' in st.session_state:
            del st.session_state['protocol_to_open']
        if 'protocol_function' in st.session_state:
            del st.session_state['protocol_function']

# Enhanced info display with modern card design
if protocol and protocol != "Không có protocol nào":
    # Extract protocol name (remove emoji if present)
    protocol_display = protocol.split(' ', 1)[1] if ' ' in protocol else protocol
    
    # Enhanced protocol header card
    st.markdown("""
    <style>
    .protocol-header-card {
        background: white;
        color: #202124;
        padding: 24px;
        border-radius: 8px;
        margin-bottom: 24px;
        border-left: 4px solid #007bff;
        border-top: 1px solid #e0e0e0;
        border-right: 1px solid #e0e0e0;
        border-bottom: 1px solid #e0e0e0;
        box-shadow: 0 1px 3px rgba(0,0,0,0.08);
    }
    .protocol-header-card h2 {
        color: #1a73e8 !important;
        border: none !important;
        margin: 0 0 12px 0 !important;
        padding: 0 !important;
        font-size: 26px !important;
        font-weight: 600 !important;
        line-height: 1.4 !important;
    }
    .protocol-meta {
        display: flex;
        gap: 16px;
        flex-wrap: wrap;
        margin-top: 16px;
        align-items: center;
    }
    .protocol-badge-specialty {
        display: inline-flex;
        align-items: center;
        padding: 4px 12px;
        border-radius: 16px;
        background-color: #e8f0fe;
        color: #1967d2;
        font-weight: 500;
        font-size: 0.85rem;
        border: 1px solid #d2e3fc;
    }
    .protocol-badge-source {
        display: inline-flex;
        align-items: center;
        padding: 4px 12px;
        border-radius: 16px;
        background-color: #f1f3f4;
        color: #5f6368;
        font-size: 0.85rem;
        border: 1px solid #dadce0;
    }
    </style>
    """, unsafe_allow_html=True)
    
    header_html = f"""
    <div class="protocol-header-card">
        <h2>📋 {html.escape(protocol_display)}</h2>
        <div class="protocol-meta">
            <span class="protocol-badge-specialty">🏥 {html.escape(specialty)}</span>
            {'<span class="protocol-badge-source">🔗 Mở từ bài viết</span>' if use_deep_link else ''}
        </div>
    </div>
    """
    st.markdown(header_html, unsafe_allow_html=True)
else:
    # Enhanced welcome message
    st.markdown("""
    <div style="background: linear-gradient(135deg, #f0f7ff 0%, #e6f2ff 100%); 
                padding: 24px; border-radius: 12px; border-left: 4px solid #0066CC; 
                margin-bottom: 24px;">
        <h3 style="color: #0066CC; margin-top: 0;">💡 Hướng dẫn sử dụng</h3>
        <p style="margin-bottom: 8px;">Chọn một protocol từ danh sách ở <strong>sidebar bên trái</strong> để xem nội dung chi tiết.</p>
        <p style="margin-bottom: 0;">Bạn có thể:</p>
        <ul style="margin-top: 8px;">
            <li>🔍 Tìm kiếm protocol bằng từ khóa</li>
            <li>🏥 Lọc theo chuyên khoa</li>
            <li>⭐ Đánh dấu yêu thích các protocol thường dùng</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# ========== TABLE OF CONTENTS ==========
# Simple TOC for protocol navigation (only show if protocol exists)
if protocol and protocol != "Không có protocol nào":
    from components.protocol_toc import render_simple_toc
    render_simple_toc()

st.markdown("---")

# render_article_link is now imported from components.protocols_article_link
# render_score_links_from_protocol is now imported from components.score_links_from_content

# Show calculator links and export if protocol exists
if protocol and protocol != "Không có protocol nào":
    render_calculator_links(protocol)
    render_export_section(protocol)

# Route to appropriate protocol using dictionary-based routing
protocol_rendered = render_protocol_by_name(protocol, render_article_link, render_score_links_from_protocol)

# Show related protocols and version history after rendering
if protocol_rendered and protocol and protocol != "Không có protocol nào":
    render_related_protocols(protocol, specialty)
    render_version_history(protocol)

if not protocol_rendered:
    # Default case: Protocol not found
    render_info_box(
        f"""
        **Không tìm thấy protocol tương ứng**
        
        Protocol được chọn: **{protocol}**
        
        Vui lòng:
        - Kiểm tra lại tên protocol
        - Chọn protocol khác từ danh sách
        - Liên hệ admin nếu protocol này nên có trong hệ thống
        """,
        type="warning",
        title="⚠️ Lỗi"
    )
    render_info_box(
        "Hãy chọn một protocol từ danh sách ở sidebar bên trái.",
        type="info",
        icon="💡"
    )

# ========== FOOTER ==========
render_standard_footer(disclaimer=False)
