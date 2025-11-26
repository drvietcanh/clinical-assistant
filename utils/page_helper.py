"""
Page Helper Utilities
Standardized page setup to reduce boilerplate code
"""

import streamlit as st
import sys
from pathlib import Path


def setup_page(page_title: str, page_icon: str, description: str = "", layout: str = "wide"):
    """
    Standard page setup - reduces boilerplate in all page files
    
    Args:
        page_title: Title of the page (shown in browser tab)
        page_icon: Emoji icon for the page
        description: Optional description shown below title
        layout: Page layout ("wide" or "centered")
    
    Returns:
        None (sets up page configuration)
    
    Example:
        >>> setup_page("Scores", "📊", "Clinical scoring systems by specialty")
    """
    # Add parent directory to path for imports
    parent_dir = Path(__file__).parent.parent
    if str(parent_dir) not in sys.path:
        sys.path.insert(0, str(parent_dir))
    
    # Set page config
    st.set_page_config(
        page_title=f"{page_title} - Clinical Assistant",
        page_icon=page_icon,
        layout=layout
    )
    
    # Render header
    st.title(f"{page_icon} {page_title}")
    if description:
        st.markdown(description)
    st.markdown("---")


def render_standard_footer(disclaimer: bool = True):
    """
    Render standard footer with disclaimer
    
    Args:
        disclaimer: Whether to show disclaimer warning
    
    Example:
        >>> render_standard_footer()
    """
    st.markdown("---")
    
    if disclaimer:
        st.warning("""
        **⚠️ Lưu ý quan trọng:**
        - Công cụ này chỉ mục đích hỗ trợ quyết định lâm sàng
        - KHÔNG thay thế đánh giá lâm sàng của bác sĩ
        - Bác sĩ phải tự xác minh kết quả trước khi áp dụng
        - Tuân thủ chính sách và quy định địa phương
        """)
    
    st.caption("📚 Dữ liệu dựa trên hướng dẫn quốc tế và các nghiên cứu lâm sàng")
    st.caption("⚠️ Chỉ mục đích tham khảo - Luôn xác minh với hướng dẫn của Bộ Y tế, Bệnh viện")
    st.caption("🗂️ Kiến trúc module - Dễ bảo trì và mở rộng")


def render_category_selection(categories: list, default_index: int = 0, key: str = "category"):
    """
    Render standard category selection in sidebar
    
    Args:
        categories: List of category names
        default_index: Default selected index
        key: Unique key for the widget
    
    Returns:
        Selected category string
    
    Example:
        >>> categories = ["Lab Panels", "Calculators"]
        >>> selected = render_category_selection(categories)
    """
    with st.sidebar:
        st.header("📋 Chọn Loại")
        selected = st.radio(
            "Loại công cụ:",
            categories,
            index=default_index,
            key=key
        )
        st.markdown("---")
    
    return selected


def render_info_box(title: str, content: str, icon: str = "ℹ️"):
    """
    Render standard info box
    
    Args:
        title: Title of the info box
        content: Content text
        icon: Icon emoji
    
    Example:
        >>> render_info_box("Instructions", "Enter values and click calculate")
    """
    st.info(f"""
    **{icon} {title}**
    
    {content}
    """)


def render_module_card(title: str, description: str, icon: str, color: str, border: str):
    """
    Render module card (for home page)
    
    Args:
        title: Module title
        description: Module description (can contain HTML)
        icon: Icon emoji
        color: Background gradient
        border: Border color
    
    Returns:
        HTML string for the card
    """
    return f"""
    <div class="module-card" style="background: {color}; border: 2px solid {border}; text-align: center; padding: 1rem; border-radius: 8px; margin: 0.5rem 0;">
        <div>
            <div class="module-icon" style="font-size: 2.5rem; margin-bottom: 0.5rem;">{icon}</div>
            <div class="module-title" style="font-weight: bold; font-size: 1.2rem; margin-bottom: 0.5rem;">{title}</div>
            <div class="module-desc" style="font-size: 0.9rem; color: #666;">{description}</div>
        </div>
    </div>
    """


def render_breadcrumb(items: list):
    """
    Render breadcrumb navigation
    
    Args:
        items: List of (label, page_path) tuples or just labels for non-clickable items
    
    Example:
        >>> render_breadcrumb([("Home", "app.py"), ("Scores", None), "Current Page"])
    """
    if not items:
        return
    
    breadcrumb_html = '<div class="breadcrumb">'
    
    for idx, item in enumerate(items):
        if isinstance(item, tuple):
            label, page_path = item
            if page_path:
                breadcrumb_html += f'<a href="#" onclick="window.location.href=\'{page_path}\'">{label}</a>'
            else:
                breadcrumb_html += f'<span>{label}</span>'
        else:
            breadcrumb_html += f'<span>{item}</span>'
        
        if idx < len(items) - 1:
            breadcrumb_html += '<span class="breadcrumb-separator">›</span>'
    
    breadcrumb_html += '</div>'
    
    st.markdown(breadcrumb_html, unsafe_allow_html=True)
