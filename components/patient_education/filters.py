"""
Category Filter Components
Quick filters for patient education topics
"""

import streamlit as st
from typing import List, Optional
from patient_education.models import PatientEducationTopic
from patient_education.data import get_category_list


def get_category_counts(topics: List[PatientEducationTopic]) -> dict:
    """Get count of topics per category"""
    counts = {}
    for topic in topics:
        category = topic.category
        counts[category] = counts.get(category, 0) + 1
    return counts


def render_category_filters(
    topics: List[PatientEducationTopic],
    active_category: Optional[str] = None,
    show_counts: bool = True,
    key: str = "category_filter"
) -> Optional[str]:
    """
    Render pill-style category filters
    
    Args:
        topics: List of all topics
        active_category: Currently active category
        show_counts: Show count badges
        key: Streamlit key
        
    Returns:
        Selected category or None
    """
    categories = get_category_list()
    counts = get_category_counts(topics)
    
    # Add "All" option
    all_count = len(topics)
    categories_with_all = ["Tất cả"] + categories
    
    # Render as buttons
    st.markdown("**📂 Chủ đề:**")
    
    # Use columns for responsive layout
    cols = st.columns(min(len(categories_with_all), 6))
    
    selected = None
    
    for i, category in enumerate(categories_with_all):
        col_idx = i % len(cols)
        with cols[col_idx]:
            if category == "Tất cả":
                label = f"Tất cả ({all_count})" if show_counts else "Tất cả"
                if st.button(
                    label,
                    key=f"{key}_{category}",
                    use_container_width=True,
                    type="primary" if active_category is None else "secondary"
                ):
                    selected = None
            else:
                count = counts.get(category, 0)
                label = f"{category} ({count})" if show_counts else category
                if st.button(
                    label,
                    key=f"{key}_{category}",
                    use_container_width=True,
                    type="primary" if active_category == category else "secondary"
                ):
                    selected = category
    
    return selected


def render_quick_filters(
    topics: List[PatientEducationTopic],
    key: str = "quick_filters"
) -> dict:
    """
    Render quick filter buttons
    
    Returns:
        Dict with filter states
    """
    st.markdown("**⚡ Lọc nhanh:**")
    
    col1, col2, col3 = st.columns(3)
    
    filters = {}
    
    with col1:
        filters['printable_only'] = st.checkbox(
            "🖨️ Có thể in",
            key=f"{key}_printable"
        )
    
    with col2:
        filters['recent'] = st.checkbox(
            "🆕 Mới nhất",
            key=f"{key}_recent"
        )
    
    with col3:
        filters['popular'] = st.checkbox(
            "⭐ Phổ biến",
            key=f"{key}_popular"
        )
    
    return filters
