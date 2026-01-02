"""
Unified Filter Component
Standard filter panel for all pages
"""

import streamlit as st
from typing import Dict, List, Any, Optional, Callable


def render_filter_panel(
    filters_config: Dict[str, Dict],
    on_filter_change: Optional[Callable] = None,
    title: str = "🔍 Lọc",
    collapsible: bool = True
) -> Dict[str, Any]:
    """
    Standard filter panel
    
    Args:
        filters_config: Dict of filter configs
            Example: {
                'category': {
                    'type': 'selectbox',
                    'label': 'Danh mục',
                    'options': ['All', 'A', 'B', 'C'],
                    'default': 'All'
                },
                'price_range': {
                    'type': 'slider',
                    'label': 'Khoảng giá',
                    'min': 0,
                    'max': 1000,
                    'default': (0, 1000)
                }
            }
        on_filter_change: Callback when filter changes
        title: Filter panel title
        collapsible: Show in expander
    
    Returns:
        Dict of current filter values
    """
    filter_values = {}
    
    if collapsible:
        with st.expander(title, expanded=False):
            filter_values = _render_filters(filters_config, on_filter_change)
    else:
        st.markdown(f"### {title}")
        filter_values = _render_filters(filters_config, on_filter_change)
    
    return filter_values


def _render_filters(
    filters_config: Dict[str, Dict],
    on_filter_change: Optional[Callable] = None
) -> Dict[str, Any]:
    """Internal function to render filters"""
    filter_values = {}
    
    for filter_name, filter_config in filters_config.items():
        filter_type = filter_config.get('type', 'selectbox')
        filter_key = f"filter_{filter_name}"
        
        if filter_type == 'selectbox':
            options = filter_config.get('options', [])
            default_idx = 0
            if 'default' in filter_config:
                try:
                    default_idx = options.index(filter_config['default'])
                except ValueError:
                    default_idx = 0
            
            value = st.selectbox(
                filter_config.get('label', filter_name),
                options=options,
                index=default_idx,
                key=filter_key
            )
            filter_values[filter_name] = value
        
        elif filter_type == 'multiselect':
            options = filter_config.get('options', [])
            default = filter_config.get('default', [])
            
            value = st.multiselect(
                filter_config.get('label', filter_name),
                options=options,
                default=default,
                key=filter_key
            )
            filter_values[filter_name] = value
        
        elif filter_type == 'slider':
            min_val = filter_config.get('min', 0)
            max_val = filter_config.get('max', 100)
            default = filter_config.get('default', (min_val, max_val))
            
            if isinstance(default, tuple):
                value = st.slider(
                    filter_config.get('label', filter_name),
                    min_value=min_val,
                    max_value=max_val,
                    value=default,
                    key=filter_key
                )
            else:
                value = st.slider(
                    filter_config.get('label', filter_name),
                    min_value=min_val,
                    max_value=max_val,
                    value=default,
                    key=filter_key
                )
            filter_values[filter_name] = value
        
        elif filter_type == 'text_input':
            default = filter_config.get('default', '')
            placeholder = filter_config.get('placeholder', '')
            
            value = st.text_input(
                filter_config.get('label', filter_name),
                value=default,
                placeholder=placeholder,
                key=filter_key
            )
            filter_values[filter_name] = value
        
        elif filter_type == 'checkbox':
            default = filter_config.get('default', False)
            
            value = st.checkbox(
                filter_config.get('label', filter_name),
                value=default,
                key=filter_key
            )
            filter_values[filter_name] = value
    
    # Call callback if provided
    if on_filter_change:
        try:
            on_filter_change(filter_values)
        except Exception:
            pass
    
    return filter_values


def apply_filters(items: List[Any], filters: Dict[str, Any], filter_func: Callable) -> List[Any]:
    """
    Apply filters to items using custom filter function
    
    Args:
        items: List of items to filter
        filters: Filter values dict
        filter_func: Function that takes (item, filters) and returns bool
    
    Returns:
        Filtered items
    """
    if not filters:
        return items
    
    filtered = []
    for item in items:
        if filter_func(item, filters):
            filtered.append(item)
    
    return filtered


__all__ = [
    'render_filter_panel',
    'apply_filters',
]

