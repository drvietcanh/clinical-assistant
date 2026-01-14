"""
Topic Card Components
Card-based layout for patient education topics
"""

import streamlit as st
import html
import re
import textwrap
from typing import List, Optional, Callable
from patient_education.models import PatientEducationTopic


# Category icons and colors
CATEGORY_CONFIG = {
    "Disease": {"icon": "🫀", "color": "#E91E63", "bg": "#FCE4EC"},
    "Medication": {"icon": "💊", "color": "#2196F3", "bg": "#E3F2FD"},
    "Lifestyle": {"icon": "🏃", "color": "#4CAF50", "bg": "#E8F5E9"},
    "Procedure": {"icon": "⚕️", "color": "#FF9800", "bg": "#FFF3E0"},
    "Cardiovascular": {"icon": "🫀", "color": "#E91E63", "bg": "#FCE4EC"},
    "Respiratory": {"icon": "🫁", "color": "#00BCD4", "bg": "#E0F7FA"},
    "Diabetes": {"icon": "🍬", "color": "#FFC107", "bg": "#FFF8E1"},
    "Neurological": {"icon": "🧠", "color": "#9C27B0", "bg": "#F3E5F5"},
    "Gastrointestinal": {"icon": "🫄", "color": "#4CAF50", "bg": "#E8F5E9"},
    "Dermatology": {"icon": "👤", "color": "#FF5722", "bg": "#FFEBEE"},
    "Infectious": {"icon": "🦠", "color": "#F44336", "bg": "#FFEBEE"},
    "Other": {"icon": "📋", "color": "#607D8B", "bg": "#ECEFF1"},
}


def get_category_config(category: str) -> dict:
    """Get icon and color for category"""
    return CATEGORY_CONFIG.get(category, {
        "icon": "📄",
        "color": "#757575",
        "bg": "#F5F5F5"
    })


def extract_preview(content: str, max_length: int = 150) -> str:
    """Extract preview text from markdown content.

    - Loại bỏ tiêu đề markdown (kể cả khi có thụt lề).
    - Loại bỏ định dạng **bold**, `code`, [link](url).
    - Lấy đoạn văn bản đầu tiên làm preview.
    """
    if not content:
        return "Không có mô tả."

    # Chuẩn hoá dòng: bỏ thụt lề chung để regex nhận diện đúng tiêu đề
    lines = content.split("\n")
    stripped_lines = [line.lstrip() for line in lines]
    text = "\n".join(stripped_lines)
    
    # Remove markdown headers and formatting
    text = re.sub(r'^\s*#{1,6}\s+', '', text, flags=re.MULTILINE)
    text = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)
    text = re.sub(r'`([^`]+)`', r'\1', text)
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
    
    # Remove any raw HTML tags to avoid broken HTML when embedding into <p>
    # (phòng trường hợp nội dung chứa <div>, <span>, ... được nhập thủ công)
    text = re.sub(r'<[^>]+>', '', text)

    # Get first non-empty paragraph
    paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
    if paragraphs:
        preview = paragraphs[0]
        if len(preview) > max_length:
            preview = preview[:max_length].rsplit(' ', 1)[0] + '...'
        return preview

    return "Không có mô tả."


def render_topic_card(
    topic: PatientEducationTopic,
    show_preview: bool = True,
    compact: bool = False,
    search_query: Optional[str] = None,
    on_click: Optional[Callable] = None
):
    """
    Render a topic as a card
    
    Args:
        topic: PatientEducationTopic object
        show_preview: Show preview text
        compact: Compact mode
        search_query: Search query for highlighting
        on_click: Click handler (not used in Streamlit, but for future)
    """
    config = get_category_config(topic.category)
    preview = extract_preview(topic.content) if show_preview else ""
    
    # Highlight search terms if provided
    if search_query and search_query.strip():
        title_display = highlight_text(topic.title_vn, search_query)
        preview_display = highlight_text(preview, search_query) if preview else ""
    else:
        title_display = html.escape(topic.title_vn)
        preview_display = html.escape(preview) if preview else ""
    
    # Badges
    badges_html = f"""
<span style="
    background: {config['bg']};
    color: {config['color']};
    padding: 4px 12px;
    border-radius: 12px;
    font-size: 0.75rem;
    font-weight: 600;
    margin-right: 8px;
">{config['icon']} {html.escape(topic.category)}</span>
"""
    
    if topic.printable:
        badges_html += """
<span style="
    background: #E8F5E9;
    color: #2E7D32;
    padding: 4px 12px;
    border-radius: 12px;
    font-size: 0.75rem;
    font-weight: 600;
">🖨️ Có thể in</span>
"""
    
    # Card HTML
    card_height = "auto" if not compact else "200px"
    card_html = f"""
<div style="
    background: white;
    border: 1px solid #e0e0e0;
    border-left: 4px solid {config['color']};
    border-radius: 12px;
    padding: 20px;
    margin-bottom: 20px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    transition: all 0.3s ease;
    height: {card_height};
    display: flex;
    flex-direction: column;
    cursor: pointer;
" 
onmouseover="this.style.boxShadow='0 4px 12px rgba(0,0,0,0.15)'; this.style.transform='translateY(-2px)'"
onmouseout="this.style.boxShadow='0 2px 8px rgba(0,0,0,0.08)'; this.style.transform='translateY(0)'"
>
    <div style="display: flex; align-items: center; margin-bottom: 12px;">
        <span style="font-size: 2rem; margin-right: 12px;">{config['icon']}</span>
        <h3 style="
            margin: 0;
            font-size: 1.2rem;
            font-weight: 700;
            color: #1a1a1a;
            flex: 1;
        ">{title_display}</h3>
    </div>
    
    <div style="margin-bottom: 12px;">
        {badges_html}
    </div>
    
    {f'<p style="color: #616161; font-size: 0.9rem; line-height: 1.6; margin: 0 0 16px 0;">{preview_display}</p>' if preview and show_preview else ''}
    
    <div style="margin-top: auto; display: flex; gap: 8px; padding-top: 12px; border-top: 1px solid #f0f0f0;">
        <span style="
            background: {config['color']};
            color: white;
            padding: 8px 16px;
            border-radius: 8px;
            font-size: 0.85rem;
            font-weight: 600;
            display: inline-block;
        ">📖 Đọc thêm</span>
        {f'<span style="background: #F5F5F5; color: #616161; padding: 8px 16px; border-radius: 8px; font-size: 0.85rem;">🖨️ In</span>' if topic.printable else ''}
    </div>
</div>
"""
    # Đảm bảo không còn thụt lề đầu dòng để Markdown không xem như code block
    card_html = textwrap.dedent(card_html).strip()
    badges_html = textwrap.dedent(badges_html).strip()
    
    st.markdown(card_html, unsafe_allow_html=True)


def highlight_text(text: str, query: str) -> str:
    """Highlight search terms in text (internal use)"""
    if not query or not text:
        return html.escape(text)
    
    escaped_text = html.escape(text)
    escaped_query = html.escape(query)
    
    # Case-insensitive highlight
    pattern = re.compile(re.escape(escaped_query), re.IGNORECASE)
    highlighted = pattern.sub(
        lambda m: f'<mark style="background: #FFF59D; padding: 2px 4px; border-radius: 3px;">{m.group()}</mark>',
        escaped_text
    )
    return highlighted


def render_topic_grid(
    topics: List[PatientEducationTopic],
    columns: int = 3,
    show_preview: bool = True,
    search_query: Optional[str] = None
):
    """
    Render topics in a grid layout
    
    Args:
        topics: List of PatientEducationTopic objects
        columns: Number of columns (1-3)
        show_preview: Show preview text
        search_query: Search query for highlighting
    """
    if not topics:
        st.info("Không có tài liệu nào.")
        return
    
    # Responsive columns
    col_width = {
        1: "100%",
        2: "48%",
        3: "31%"
    }.get(columns, "31%")
    
    # CSS for grid
    st.markdown(f"""
    <style>
    .topic-grid {{
        display: flex;
        flex-wrap: wrap;
        gap: 20px;
        margin-bottom: 20px;
    }}
    .topic-card-wrapper {{
        flex: 0 0 calc({col_width} - 20px);
        min-width: 280px;
    }}
    @media (max-width: 768px) {{
        .topic-card-wrapper {{
            flex: 0 0 100%;
        }}
    }}
    </style>
    """, unsafe_allow_html=True)
    
    # Render cards
    for i, topic in enumerate(topics):
        with st.container():
            render_topic_card(
                topic,
                show_preview=show_preview,
                search_query=search_query
            )
