"""
Protocol Table of Contents Component
Auto-generate TOC from protocol content
"""

import streamlit as st
import re
import html
from typing import List, Dict, Tuple


def extract_headers_from_markdown(content: str) -> List[Dict[str, str]]:
    """
    Extract headers from markdown content.
    
    Args:
        content: Markdown content string
        
    Returns:
        List of dicts with 'level', 'text', 'anchor' keys
    """
    headers = []
    # Pattern to match markdown headers: ### Header or ## Header
    pattern = r'^(#{1,6})\s+(.+)$'
    
    for line in content.split('\n'):
        match = re.match(pattern, line.strip())
        if match:
            level = len(match.group(1))  # Number of # symbols
            text = match.group(2).strip()
            # Remove emojis for anchor (keep for display)
            anchor = re.sub(r'[^\w\s-]', '', text.lower())
            anchor = re.sub(r'[-\s]+', '-', anchor)
            headers.append({
                'level': level,
                'text': text,
                'anchor': anchor
            })
    
    return headers


def generate_toc_from_headers(headers: List[Dict[str, str]]) -> str:
    """
    Generate HTML TOC from headers list.
    
    Args:
        headers: List of header dicts
        
    Returns:
        HTML string for TOC
    """
    if not headers:
        return ""
    
    toc_html = '<div class="protocol-toc">'
    toc_html += '<h4 style="margin-top: 0; margin-bottom: 1rem;">📋 Mục Lục</h4>'
    toc_html += '<ul style="list-style: none; padding-left: 0;">'
    
    for header in headers:
        indent = (header['level'] - 2) * 20  # Indent based on level (h2 = 0, h3 = 20px, etc.)
        style = f'margin-left: {indent}px;' if indent > 0 else ''
        # Sanitize anchor for HTML ID attribute
        safe_anchor = "".join(c if c.isalnum() or c in ('_', '-') else '_' for c in header['anchor'])
        
        toc_html += f'''
        <li style="{style} margin-bottom: 0.5rem;">
            <a href="#{safe_anchor}" 
               style="text-decoration: none; color: var(--protocol-primary-blue);"
               onclick="document.getElementById('{safe_anchor}').scrollIntoView({{behavior: 'smooth'}}); return false;">
                {html.escape(header['text'])}
            </a>
        </li>
        '''
    
    toc_html += '</ul></div>'
    return toc_html


def render_toc(headers: List[Dict[str, str]] = None, content: str = None):
    """
    Render Table of Contents.
    
    Args:
        headers: Optional pre-extracted headers list
        content: Optional markdown content to extract headers from
    """
    if headers is None:
        if content:
            headers = extract_headers_from_markdown(content)
        else:
            st.warning("⚠️ Không có nội dung để tạo mục lục")
            return
    
    if not headers:
        return
    
    # Generate and render TOC
    toc_html = generate_toc_from_headers(headers)
    
    if toc_html:
        # Enhanced TOC with better styling
        st.markdown("""
        <style>
        .protocol-toc {
            background: #f8f9fa;
            border: 1px solid #dee2e6;
            border-radius: 8px;
            padding: 16px;
            margin: 16px 0;
        }
        .protocol-toc h4 {
            color: #0066CC;
            margin: 0 0 12px 0;
            font-size: 18px;
            font-weight: 600;
        }
        .protocol-toc ul {
            margin: 0;
            padding-left: 0;
        }
        .protocol-toc li {
            margin-bottom: 8px;
        }
        .protocol-toc a {
            color: #0066CC;
            text-decoration: none;
            transition: color 0.2s ease;
            display: block;
            padding: 6px 8px;
            border-radius: 4px;
        }
        .protocol-toc a:hover {
            color: #004499;
            background: #e6f2ff;
        }
        </style>
        """, unsafe_allow_html=True)
        
        with st.expander("📋 Mục Lục", expanded=True):
            st.markdown(toc_html, unsafe_allow_html=True)


def add_anchors_to_content(content: str, headers: List[Dict[str, str]] = None) -> str:
    """
    Add anchor IDs to headers in content for TOC navigation.
    
    Args:
        content: Original markdown content
        headers: Optional pre-extracted headers
        
    Returns:
        Content with anchor IDs added
    """
    if headers is None:
        headers = extract_headers_from_markdown(content)
    
    if not headers:
        return content
    
    # Add anchor IDs to headers
    lines = content.split('\n')
    result_lines = []
    header_idx = 0
    
    for line in lines:
        match = re.match(r'^(#{1,6})\s+(.+)$', line.strip())
        if match and header_idx < len(headers):
            header = headers[header_idx]
            # Sanitize anchor for HTML ID attribute
            safe_anchor = "".join(c if c.isalnum() or c in ('_', '-') else '_' for c in header["anchor"])
            # Add anchor ID before header
            result_lines.append(f'<div id="{safe_anchor}"></div>')
            result_lines.append(line)
            header_idx += 1
        else:
            result_lines.append(line)
    
    return '\n'.join(result_lines)


def render_simple_toc(protocol_sections: List[Tuple[str, str]] = None):
    """
    Render simple TOC from predefined sections.
    Useful when protocol structure is known.
    
    Args:
        protocol_sections: List of (section_name, icon) tuples
    """
    if not protocol_sections:
        # Default sections for most protocols
        protocol_sections = [
            ("📋 Diagnostic Criteria", "diagnostic"),
            ("📊 Risk Stratification", "risk"),
            ("💊 Treatment Algorithm", "treatment"),
            ("💉 Dosing Information", "dosing"),
            ("📈 Monitoring", "monitoring"),
            ("👥 Special Populations", "special"),
            ("📚 References", "references")
        ]
    
    # Enhanced TOC styling
    st.markdown("""
    <style>
    .protocol-toc-simple {
        background: #f8f9fa;
        border: 1px solid #dee2e6;
        border-radius: 8px;
        padding: 16px;
    }
    .protocol-toc-simple a {
        color: #0066CC;
        text-decoration: none;
        display: block;
        padding: 8px 12px;
        margin-bottom: 6px;
        border-radius: 4px;
        transition: all 0.2s ease;
    }
    .protocol-toc-simple a:hover {
        background: #e6f2ff;
        color: #004499;
        transform: translateX(4px);
    }
    </style>
    """, unsafe_allow_html=True)
    
    with st.expander("📋 Mục Lục", expanded=True):
        st.markdown('<div class="protocol-toc-simple">', unsafe_allow_html=True)
        for section_name, anchor in protocol_sections:
            # Sanitize anchor for HTML ID attribute
            safe_anchor = "".join(c if c.isalnum() or c in ('_', '-') else '_' for c in str(anchor))
            st.markdown(
                f'<a href="#{safe_anchor}">{html.escape(section_name)}</a>',
                unsafe_allow_html=True
            )
        st.markdown('</div>', unsafe_allow_html=True)

