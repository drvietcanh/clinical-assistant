"""
Page Helper Utilities
Standardized page setup to reduce boilerplate code
"""

import streamlit as st
import sys
from pathlib import Path
from config.app_config import APP_CONFIG


def inject_google_analytics():
    """
    Inject Google Analytics (GA4) script once per session.
    Works for all Streamlit pages that call setup_page.
    """
    ga_id = APP_CONFIG.get("google_analytics_id", "")
    if not ga_id or ga_id == "G-XXXXXXXXXX":
        return

    # Avoid injecting multiple times in the same session
    if st.session_state.get("_ga_injected"):
        return

    ga_snippet = f"""
    <script async src="https://www.googletagmanager.com/gtag/js?id={ga_id}"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){{dataLayer.push(arguments);}}
      gtag('js', new Date());
      gtag('config', '{ga_id}', {{
        'send_page_view': true,
        'page_path': window.location.pathname + window.location.search
      }});
    </script>
    """
    st.markdown(ga_snippet, unsafe_allow_html=True)
    st.session_state["_ga_injected"] = True


def inject_global_font_css():
    """
    Inject global CSS for proper font rendering across all pages.
    Ensures Vietnamese characters and special characters display correctly.
    """
    # Avoid injecting multiple times in the same session
    if st.session_state.get("_font_css_injected"):
        return
    
    font_css = """
    <style>
    /* Global font settings for proper Vietnamese character display */
    * {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Helvetica Neue', 
                     Arial, 'Noto Sans', sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 
                     'Segoe UI Symbol', 'Noto Color Emoji' !important;
    }
    
    /* Ensure HTML tables have proper font */
    table, .insulin-table, .guideline-card, .dashboard-card {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Helvetica Neue', 
                     Arial, 'Noto Sans', sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 
                     'Segoe UI Symbol', 'Noto Color Emoji' !important;
    }
    
    /* Ensure proper encoding for all text elements */
    body, p, div, span, td, th, li, h1, h2, h3, h4, h5, h6 {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Helvetica Neue', 
                     Arial, 'Noto Sans', sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 
                     'Segoe UI Symbol', 'Noto Color Emoji' !important;
    }
    
    /* Ensure Streamlit components use proper font */
    .stMarkdown, .stText, .stDataFrame, .stTable {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Helvetica Neue', 
                     Arial, 'Noto Sans', sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 
                     'Segoe UI Symbol', 'Noto Color Emoji' !important;
    }
    
    /* Fix input fields font and prevent text overlap */
    .stTextInput > div > div > input,
    .stTextInput label,
    .stTextInput > div > div > div,
    input[type="text"],
    input[type="search"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 
                     'Noto Sans', 'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans',
                     'Helvetica Neue', sans-serif !important;
        font-size: 1rem !important;
        line-height: 1.5 !important;
        letter-spacing: normal !important;
        text-rendering: optimizeLegibility !important;
        -webkit-font-smoothing: antialiased !important;
        -moz-osx-font-smoothing: grayscale !important;
    }
    
    /* Prevent text overlap in input fields */
    .stTextInput > div > div > input {
        padding: 12px 16px !important;
        white-space: nowrap !important;
        overflow: hidden !important;
        text-overflow: ellipsis !important;
    }
    
    /* Fix label positioning */
    .stTextInput label {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 
                     'Noto Sans', 'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans',
                     'Helvetica Neue', sans-serif !important;
        font-weight: 500 !important;
        line-height: 1.4 !important;
        margin-bottom: 0.5rem !important;
        display: block !important;
    }
    
    /* Hide HTML code blocks on mobile - prevent raw HTML from displaying as text */
    @media (max-width: 768px) {
        /* Hide code blocks that contain only HTML tags */
        pre code:contains('</div>'),
        pre code:contains('<div'),
        pre code:contains('<button'),
        pre code:contains('mobile-back-btn'),
        pre code:contains('mobile-header-title'),
        pre code:contains('mobile-header-subtitle') {
            display: none !important;
        }
        
        /* Alternative: Hide empty or minimal code blocks that might be HTML artifacts */
        pre:has(> code:empty),
        code:empty,
        pre code:only-child:empty {
            display: none !important;
        }
        
        /* Hide code blocks that look like HTML (contain angle brackets) */
        pre code {
            display: block;
        }
        
        /* More aggressive: Hide any code block that contains HTML-like content */
        pre code:has-text('</div>'),
        pre code:has-text('<div'),
        pre code:has-text('<button') {
            display: none !important;
            visibility: hidden !important;
            height: 0 !important;
            overflow: hidden !important;
        }
    }
    
    /* JavaScript fallback to hide stray HTML code blocks */
    <script>
    (function() {
        function hideHtmlCodeBlocks() {
            // Find all code blocks
            const codeBlocks = document.querySelectorAll('pre code, code');
            codeBlocks.forEach(block => {
                const text = (block.textContent || '').trim();
                // Hide if it's just HTML tags
                if (text.match(/^<[^>]+>[\s\S]*<\/[^>]+>$/)) {
                    const pre = block.closest('pre');
                    if (pre) {
                        pre.style.display = 'none';
                    } else {
                        block.style.display = 'none';
                    }
                }
                // Hide if it contains mobile header HTML
                if (text.includes('mobile-back-btn') || 
                    text.includes('mobile-header-title') ||
                    text.includes('mobile-header-subtitle')) {
                    const pre = block.closest('pre');
                    if (pre) {
                        pre.style.display = 'none';
                    } else {
                        block.style.display = 'none';
                    }
                }
            });
        }
        
        // Run on page load
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', hideHtmlCodeBlocks);
        } else {
            hideHtmlCodeBlocks();
        }
        
        // Run after a delay to catch dynamically loaded content
        setTimeout(hideHtmlCodeBlocks, 500);
        setTimeout(hideHtmlCodeBlocks, 1000);
    })();
    </script>
    </style>
    """
    st.markdown(font_css, unsafe_allow_html=True)
    st.session_state["_font_css_injected"] = True


def inject_dom_cleanup_js():
    """
    Inject small JS snippet to clean stray raw HTML closing tags (e.g., lone '</div>')
    that may appear in the rendered UI due to markdown/HTML edge cases.
    """
    if st.session_state.get("_dom_cleanup_injected"):
        return

    cleanup_js = """
    <script>
    function cleanStrayHtmlClosers() {
        try {
            const selectors = ['p', 'div', 'span', 'code', 'pre', 'li'];
            selectors.forEach(sel => {
                document.querySelectorAll(sel).forEach(el => {
                    const text = (el.textContent || '').trim();
                    if (text === '</div>' || text === '<div>' ||
                        text === '&lt;/div&gt;' || text === '&lt;div&gt;') {
                        el.style.display = 'none';
                    }
                });
            });
        } catch (e) {
            // fail silently
        }
    }
    if (document.readyState === 'complete') {
        cleanStrayHtmlClosers();
    } else {
        window.addEventListener('load', cleanStrayHtmlClosers);
    }
    setTimeout(cleanStrayHtmlClosers, 1000);
    </script>
    """
    st.markdown(cleanup_js, unsafe_allow_html=True)
    st.session_state["_dom_cleanup_injected"] = True


def setup_page(page_title: str, page_icon: str, description: str = "", layout: str = "wide", mobile_header: bool = True):
    """
    Standard page setup - reduces boilerplate in all page files
    Now with mobile optimizations
    
    Args:
        page_title: Title of the page (shown in browser tab)
        page_icon: Emoji icon for the page
        description: Optional description shown below title
        layout: Page layout ("wide" or "centered")
        mobile_header: Show mobile-optimized header (default: True)
    
    Returns:
        None (sets up page configuration)
    
    Example:
        >>> setup_page("Scores", "📊", "Clinical scoring systems by specialty")
    """
    # Inject GA as early as possible on every page
    inject_google_analytics()
    
    # Inject global font CSS and DOM cleanup helpers
    inject_global_font_css()
    inject_dom_cleanup_js()
    
    # Inject mobile optimizations CSS
    inject_mobile_optimizations_css()

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
    
    # Render mobile header if enabled
    if mobile_header:
        try:
            from components.mobile_page_wrapper import render_mobile_page_header
            render_mobile_page_header(
                title=page_title,
                icon=page_icon,
                subtitle=description if description else None,
                show_back_button=True,
                back_url="/"
            )
        except ImportError:
            # Fallback to standard header if component not available
            pass
    
    # Render standard header (hidden on mobile if mobile_header is True)
    header_style = """
    <style>
    @media (max-width: 768px) {
        h1:first-of-type {
            display: none; /* Hide standard title on mobile if mobile header is shown */
        }
    }
    </style>
    """ if mobile_header else ""
    
    st.markdown(header_style, unsafe_allow_html=True)
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
