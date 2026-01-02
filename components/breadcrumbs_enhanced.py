"""
Enhanced Breadcrumbs Component
Breadcrumbs with navigation category awareness
"""

import streamlit as st
from typing import List, Tuple, Optional
from config.app_config import get_module_info
from config.navigation_config import get_category_by_module_id, get_category_info


def render_breadcrumbs_enhanced(
    items: List[Tuple[str, Optional[str]]],
    show_category: bool = True,
    current_module_id: Optional[str] = None
) -> None:
    """
    Render enhanced breadcrumbs with category awareness
    
    Args:
        items: List of (label, url) tuples. Last item should have url=None
        show_category: Whether to show category in breadcrumbs
        current_module_id: Current module ID to determine category
    """
    if len(items) <= 1:
        return
    
    # Add category if available and show_category is True
    breadcrumb_items = []
    
    # Add Home
    breadcrumb_items.append(("Trang chủ", "/"))
    
    # Add category if we have current_module_id
    if show_category and current_module_id:
        category = get_category_by_module_id(current_module_id)
        if category:
            breadcrumb_items.append((category.title, None))  # Category is not clickable
    
    # Add custom items
    for label, url in items:
        breadcrumb_items.append((label, url))
    
    # Build breadcrumb HTML
    breadcrumb_html = '''
    <nav class="breadcrumb-nav-enhanced" aria-label="Breadcrumb" style="margin-bottom: 1rem;">
        <ol style="list-style: none; padding: 0; margin: 0; display: flex; flex-wrap: wrap; align-items: center; gap: 0.5rem; font-size: 0.9rem;">
    '''
    
    for idx, (label, url) in enumerate(breadcrumb_items):
        is_last = idx == len(breadcrumb_items) - 1
        
        breadcrumb_html += '<li style="display: flex; align-items: center;">'
        
        if url and not is_last:
            breadcrumb_html += f'''
                <a href="{url}" 
                   style="color: var(--primary, #1976d2); 
                          text-decoration: none; 
                          transition: color 0.2s;
                          display: flex;
                          align-items: center;">
                    {label}
                </a>
            '''
        else:
            breadcrumb_html += f'''
                <span style="color: var(--text-primary, #212121); 
                            font-weight: {'600' if is_last else '400'};
                            display: flex;
                            align-items: center;">
                    {label}
                </span>
            '''
        
        if not is_last:
            breadcrumb_html += '''
                <span style="margin: 0 0.5rem; color: var(--text-secondary, #666);">/</span>
            '''
        
        breadcrumb_html += '</li>'
    
    breadcrumb_html += '''
        </ol>
    </nav>
    <style>
    .breadcrumb-nav-enhanced a:hover {
        color: var(--primary-hover, #1565c0);
        text-decoration: underline;
    }
    
    @media (max-width: 768px) {
        .breadcrumb-nav-enhanced {
            font-size: 0.85rem;
        }
        
        .breadcrumb-nav-enhanced ol {
            gap: 0.25rem;
        }
    }
    </style>
    '''
    
    st.markdown(breadcrumb_html, unsafe_allow_html=True)


def get_breadcrumbs_for_module(module_id: str) -> List[Tuple[str, Optional[str]]]:
    """
    Generate breadcrumbs for a module automatically
    
    Args:
        module_id: Module ID
    
    Returns:
        List of (label, url) tuples for breadcrumbs
    """
    module_info = get_module_info(module_id)
    if not module_info:
        return [("Trang chủ", "/")]
    
    breadcrumbs = [("Trang chủ", "/")]
    
    # Add category
    category = get_category_by_module_id(module_id)
    if category:
        breadcrumbs.append((category.title, None))
    
    # Add current module (not clickable)
    breadcrumbs.append((module_info.title, None))
    
    return breadcrumbs

