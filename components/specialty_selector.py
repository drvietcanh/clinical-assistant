"""
Specialty Selector Component
Allows doctors to select their specialty for personalized recommendations
"""

import streamlit as st
from typing import Optional, List, Dict


def get_available_specialties() -> List[Dict[str, str]]:
    """Get list of available specialties with icons"""
    return [
        {"id": None, "name": "Tất cả", "icon": "🌐", "description": "Xem tất cả công cụ"},
        {"id": "ICU", "name": "ICU", "icon": "🫁", "description": "Hồi sức cấp cứu"},
        {"id": "Tim mạch", "name": "Tim mạch", "icon": "❤️", "description": "Tim mạch học"},
        {"id": "Hô hấp", "name": "Hô hấp", "icon": "🫁", "description": "Hô hấp học"},
        {"id": "Nhi", "name": "Nhi khoa", "icon": "👶", "description": "Nhi khoa"},
        {"id": "Nội", "name": "Nội khoa", "icon": "🩺", "description": "Nội khoa tổng quát"},
        {"id": "Ngoại", "name": "Ngoại khoa", "icon": "⚕️", "description": "Ngoại khoa"},
        {"id": "Sản", "name": "Sản khoa", "icon": "🤰", "description": "Sản phụ khoa"},
        {"id": "Cấp cứu", "name": "Cấp cứu", "icon": "🚑", "description": "Cấp cứu y khoa"},
    ]


def render_specialty_selector(
    key: str = "specialty_selector",
    label: str = "Chọn chuyên khoa",
    show_label: bool = True,
    compact: bool = False
) -> Optional[str]:
    """
    Render specialty selector component
    
    Args:
        key: Unique key for the selector
        label: Label text
        show_label: Whether to show label
        compact: Use compact layout for mobile
    
    Returns:
        Selected specialty ID or None
    """
    specialties = get_available_specialties()
    
    # Initialize session state
    if 'user_specialty' not in st.session_state:
        st.session_state.user_specialty = None
    
    # Get current selection index
    current_idx = 0
    current_specialty_id = st.session_state.get('user_specialty', None)
    if current_specialty_id:
        for idx, spec in enumerate(specialties):
            if spec['id'] == current_specialty_id:
                current_idx = idx
                break
    
    # Render selector
    if compact:
        # Compact version for mobile/header
        selected_idx = st.selectbox(
            label,
            range(len(specialties)),
            format_func=lambda x: f"{specialties[x]['icon']} {specialties[x]['name']}",
            index=current_idx,
            key=key,
            label_visibility="collapsed" if not show_label else "visible"
        )
    else:
        # Full version with descriptions
        selected_idx = st.selectbox(
            label,
            range(len(specialties)),
            format_func=lambda x: f"{specialties[x]['icon']} {specialties[x]['name']} - {specialties[x]['description']}",
            index=current_idx,
            key=key,
            label_visibility="visible" if show_label else "collapsed"
        )
    
    # Update session state
    selected_specialty = specialties[selected_idx]
    if selected_specialty['id']:
        st.session_state.user_specialty = selected_specialty['id']
    else:
        st.session_state.user_specialty = None
    
    return st.session_state.user_specialty


def get_specialty_badge(specialty_id: Optional[str] = None) -> str:
    """
    Get specialty badge HTML
    
    Args:
        specialty_id: Specialty ID
    
    Returns:
        HTML string for badge
    """
    if not specialty_id:
        return ""
    
    specialties = get_available_specialties()
    specialty = next((s for s in specialties if s['id'] == specialty_id), None)
    
    if not specialty:
        return ""
    
    return f"""
    <span style="
        display: inline-flex;
        align-items: center;
        gap: 4px;
        padding: 4px 12px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 12px;
        font-size: 0.85rem;
        font-weight: 600;
    ">
        {specialty['icon']} {specialty['name']}
    </span>
    """

