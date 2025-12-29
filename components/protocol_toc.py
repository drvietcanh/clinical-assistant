"""
Protocol Table of Contents Component
Auto-generate TOC from protocol content
"""

import streamlit as st
import re
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
        
        toc_html += f'''
        <li style="{style} margin-bottom: 0.5rem;">
            <a href="#{header['anchor']}" 
               style="text-decoration: none; color: var(--protocol-primary-blue);"
               onclick="document.getElementById('{header['anchor']}').scrollIntoView({{behavior: 'smooth'}}); return false;">
                {header['text']}
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
        with st.expander("📋 Mục Lục", expanded=False):
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
            # Add anchor ID before header
            result_lines.append(f'<div id="{header["anchor"]}"></div>')
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
    
    with st.expander("📋 Mục Lục", expanded=False):
        for section_name, anchor in protocol_sections:
            st.markdown(
                f'<a href="#{anchor}" style="text-decoration: none; color: var(--protocol-primary-blue); display: block; margin-bottom: 0.5rem;">{section_name}</a>',
                unsafe_allow_html=True
            )

