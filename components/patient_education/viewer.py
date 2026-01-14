"""
Enhanced Content Viewer
Content display with TOC, reading progress, and navigation
"""

import streamlit as st
import re
from typing import List, Optional
from patient_education.models import PatientEducationTopic


def extract_headings(content: str) -> List[dict]:
    """
    Extract headings from markdown content
    
    Returns:
        List of dicts with 'level', 'text', 'id'
    """
    headings = []
    lines = content.split('\n')
    
    for line in lines:
        # Match markdown headings
        match = re.match(r'^(#{1,6})\s+(.+)$', line.strip())
        if match:
            level = len(match.group(1))
            text = match.group(2).strip()
            # Remove markdown formatting
            text = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)
            text = re.sub(r'`([^`]+)`', r'\1', text)
            
            # Create ID from text
            heading_id = re.sub(r'[^\w\s-]', '', text.lower())
            heading_id = re.sub(r'[-\s]+', '-', heading_id)
            
            headings.append({
                'level': level,
                'text': text,
                'id': heading_id
            })
    
    return headings


def render_table_of_contents(headings: List[dict], key: str = "toc"):
    """
    Render table of contents sidebar
    
    Args:
        headings: List of heading dicts
        key: Streamlit key
    """
    if not headings:
        return
    
    st.sidebar.markdown("### 📑 Mục lục")
    
    for heading in headings:
        level = heading['level']
        text = heading['text']
        indent = (level - 1) * 20
        
        # Truncate long headings
        display_text = text if len(text) <= 40 else text[:37] + "..."
        
        st.sidebar.markdown(
            f'<div style="margin-left: {indent}px; margin-bottom: 8px;">'
            f'<a href="#{heading["id"]}" style="color: #2196F3; text-decoration: none; font-size: 0.9rem;">{display_text}</a>'
            f'</div>',
            unsafe_allow_html=True
        )


def render_reading_progress(current_section: int, total_sections: int):
    """
    Render reading progress indicator
    
    Args:
        current_section: Current section number
        total_sections: Total number of sections
    """
    if total_sections == 0:
        return
    
    progress = (current_section / total_sections) * 100
    
    st.markdown(f"""
    <div style="
        background: #f0f0f0;
        border-radius: 10px;
        height: 8px;
        margin: 16px 0;
        overflow: hidden;
    ">
        <div style="
            background: linear-gradient(90deg, #2196F3, #21CBF3);
            height: 100%;
            width: {progress}%;
            transition: width 0.3s ease;
        "></div>
    </div>
    <div style="text-align: center; color: #616161; font-size: 0.85rem; margin-top: 4px;">
        Đã đọc: {current_section}/{total_sections} phần ({int(progress)}%)
    </div>
    """, unsafe_allow_html=True)


def render_enhanced_content(
    topic: PatientEducationTopic,
    show_toc: bool = True,
    show_progress: bool = True,
    search_query: Optional[str] = None
):
    """
    Render enhanced content with TOC and progress
    
    Args:
        topic: PatientEducationTopic object
        show_toc: Show table of contents
        show_progress: Show reading progress
        search_query: Search query for highlighting
    """
    # Extract headings
    headings = extract_headings(topic.content)
    
    # Show TOC in sidebar
    if show_toc and headings:
        render_table_of_contents(headings)
    
    # Title
    st.markdown(f"# {topic.title_vn}")
    
    # Badges
    from .cards import get_category_config
    config = get_category_config(topic.category)
    
    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        st.markdown(f"""
        <span style="
            background: {config['bg']};
            color: {config['color']};
            padding: 6px 16px;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 600;
        ">{config['icon']} {topic.category}</span>
        """, unsafe_allow_html=True)
    
    with col2:
        if topic.printable:
            st.markdown("🖨️ **Có thể in**")
    
    with col3:
        # Share button (placeholder)
        # Use a unique key per topic to avoid duplicate element ID errors when rendering in loops
        if st.button(
            "🔗 Chia sẻ",
            key=f"share_topic_{topic.id}",
            use_container_width=True,
        ):
            st.info("Link chia sẻ: [URL sẽ được tạo]")
    
    st.markdown("---")
    
    # Content with highlighted search terms
    if search_query and search_query.strip():
        from components.patient_education.search import highlight_search_terms
        highlighted_content = highlight_search_terms(topic.content, search_query)
        st.markdown(highlighted_content, unsafe_allow_html=True)
    else:
        st.markdown(topic.content)
    
    # Reading progress
    if show_progress and headings:
        st.markdown("---")
        render_reading_progress(1, len(headings))  # Placeholder - would track actual reading
    
    # Print section
    if topic.printable:
        st.markdown("---")
        st.markdown("### 🖨️ In tài liệu")
        st.info("Nhấn **Ctrl+P** (Windows) hoặc **Cmd+P** (Mac) để in tài liệu này.")
        
        # Use a unique key per topic for the print preview button as well
        if st.button(
            "📄 Xem bản in",
            key=f"print_preview_{topic.id}",
            use_container_width=True,
        ):
            st.info("Mở Print Preview trong trình duyệt để xem bản in.")
