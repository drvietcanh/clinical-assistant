"""
Card Components
Reusable card components for modules, calculators, and info display
"""

import streamlit as st
from typing import Optional, Dict
from config.theme import get_module_style, THEME


def render_module_card(
    title: str,
    description: str,
    icon: str,
    module_id: Optional[str] = None,
    gradient: Optional[str] = None,
    border: Optional[str] = None,
    onclick: Optional[str] = None,
    **kwargs
) -> str:
    """
    Render a module card with consistent styling
    
    Args:
        title: Module title
        description: Module description
        icon: Icon emoji or HTML
        module_id: Module ID for theme lookup (e.g., "scores", "antibiotics")
        gradient: Custom gradient override
        border: Custom border color override
        onclick: Optional JavaScript onclick handler
        **kwargs: Additional HTML attributes
    
    Returns:
        HTML string for the card
    
    Example:
        >>> card_html = render_module_card(
        ...     "Scores", "Clinical scoring systems", "📊", module_id="scores"
        ... )
        >>> st.markdown(card_html, unsafe_allow_html=True)
    """
    # Get style from theme if module_id provided
    if module_id:
        style = get_module_style(module_id)
        gradient = gradient or style['gradient']
        border = border or style['border']
    else:
        gradient = gradient or THEME['module_gradients']['scores']
        border = border or THEME['module_borders']['scores']
    
    # Build additional attributes
    attrs = " ".join([f'{k}="{v}"' for k, v in kwargs.items()])
    onclick_attr = f'onclick="{onclick}"' if onclick else ''
    
    card_html = f"""
    <div class="module-card" 
         style="background: {gradient}; border: 2px solid {border}; text-align: center; padding: 1.5rem; border-radius: 12px; margin: 0.5rem 0; cursor: pointer; transition: all 0.3s ease; {attrs}"
         {onclick_attr}>
        <div class="module-icon" style="font-size: 2.5rem; margin-bottom: 0.5rem;">{icon}</div>
        <div class="module-title" style="font-weight: bold; font-size: 1.2rem; margin-bottom: 0.5rem; color: {THEME['colors']['text_primary']};">{title}</div>
        <div class="module-desc" style="font-size: 0.9rem; color: {THEME['colors']['text_secondary']}; line-height: 1.5;">{description}</div>
    </div>
    """
    
    return card_html


def render_calculator_card(
    calc_id: str,
    name: str,
    category: str,
    icon: str,
    page: str,
    is_favorite: bool = False,
    is_recent: bool = False,
    show_favorite_button: bool = True,
    show_open_button: bool = True,
    **kwargs
) -> None:
    """
    Render a calculator card with favorite and open buttons
    
    Args:
        calc_id: Calculator ID
        name: Calculator name
        category: Category name
        icon: Icon emoji
        page: Page to navigate to
        is_favorite: Whether calculator is favorited
        is_recent: Whether calculator was recently used
        show_favorite_button: Show favorite button
        show_open_button: Show open button
        **kwargs: Additional styling options
    
    Example:
        >>> render_calculator_card(
        ...     "sofa", "SOFA Score", "Emergency", "🚨", "Scores",
        ...     is_favorite=True
        ... )
    """
    # Card styling based on state
    card_class = "search-result-card"
    if is_favorite:
        card_class = "favorite-card"
    elif is_recent:
        card_class = "recent-card"
    
    # Render card
    st.markdown(f"""
    <div class="{card_class}">
        <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px;">
            <span style="font-size: 1.5rem;">{icon}</span>
            <strong style="font-size: 1rem; color: {THEME['colors']['text_primary']};">{name}</strong>
        </div>
        <div style="font-size: 0.85rem; color: {THEME['colors']['text_secondary']}; margin-bottom: 12px;">
            📂 {category}<br/>
            📄 {page}
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Action buttons
    if show_favorite_button or show_open_button:
        col1, col2 = st.columns([1, 3]) if show_favorite_button and show_open_button else ([1], [1])
        
        # Favorite button
        if show_favorite_button:
            with col1:
                fav_icon = "⭐" if is_favorite else "☆"
                if st.button(fav_icon, key=f"fav_card_{calc_id}", help="Thêm/bỏ yêu thích"):
                    if is_favorite:
                        from components.favorites import remove_from_favorites
                        remove_from_favorites(calc_id)
                        st.success("Đã bỏ khỏi yêu thích")
                    else:
                        from components.favorites import add_to_favorites
                        add_to_favorites(calc_id)
                        st.success("Đã thêm vào yêu thích")
                    st.rerun()
        
        # Open button
        if show_open_button:
            with col2:
                if st.button("▶️ Mở", key=f"open_card_{calc_id}", type="primary", use_container_width=True):
                    from components.recently_used import add_to_recently_used
                    add_to_recently_used(calc_id)
                    st.switch_page(page)


def render_info_card(
    title: str,
    content: str,
    icon: str = "ℹ️",
    color: str = "info",
    border_left: bool = True,
    **kwargs
) -> str:
    """
    Render an information card
    
    Args:
        title: Card title
        content: Card content (supports HTML)
        icon: Icon emoji
        color: Color theme (info, success, warning, error)
        border_left: Show left border accent
        **kwargs: Additional HTML attributes
    
    Returns:
        HTML string for the card
    
    Example:
        >>> card_html = render_info_card(
        ...     "Instructions", "Enter patient values", "📝", "info"
        ... )
        >>> st.markdown(card_html, unsafe_allow_html=True)
    """
    # Get color from theme
    color_map = {
        "info": THEME['colors']['info'],
        "success": THEME['colors']['success'],
        "warning": THEME['colors']['warning'],
        "error": THEME['colors']['error'],
    }
    accent_color = color_map.get(color, THEME['colors']['info'])
    
    # Build attributes
    attrs = " ".join([f'{k}="{v}"' for k, v in kwargs.items()])
    border_style = f"border-left: 4px solid {accent_color};" if border_left else ""
    
    card_html = f"""
    <div class="info-card" 
         style="background: {THEME['colors']['background_secondary']}; padding: 1rem; border-radius: 8px; margin: 1rem 0; {border_style} {attrs}">
        <div style="display: flex; align-items: start; gap: 12px;">
            <span style="font-size: 1.5rem;">{icon}</span>
            <div style="flex: 1;">
                <strong style="color: {THEME['colors']['text_primary']}; font-size: 1rem; display: block; margin-bottom: 0.5rem;">{title}</strong>
                <div style="color: {THEME['colors']['text_secondary']}; font-size: 0.9rem; line-height: 1.6;">{content}</div>
            </div>
        </div>
    </div>
    """
    
    return card_html

