"""
Mobile-First UI Components
Touch-friendly components optimized for mobile devices
"""

import streamlit as st
from typing import Optional, Callable, List, Dict
import time


def render_mobile_button(
    label: str,
    icon: str = "",
    on_click: Optional[Callable] = None,
    key: Optional[str] = None,
    use_container_width: bool = True,
    type: str = "primary",
    size: str = "large"
):
    """
    Render touch-friendly mobile button
    
    Args:
        label: Button label
        icon: Icon emoji or text
        on_click: Click handler
        key: Unique key
        use_container_width: Use full width
        type: Button type (primary, secondary, danger)
        size: Button size (small, medium, large)
    """
    # Minimum touch target: 44x44px (Apple HIG, Material Design)
    button_styles = {
        "large": {
            "height": "56px",
            "font_size": "18px",
            "padding": "16px 24px"
        },
        "medium": {
            "height": "48px",
            "font_size": "16px",
            "padding": "12px 20px"
        },
        "small": {
            "height": "44px",
            "font_size": "14px",
            "padding": "10px 16px"
        }
    }
    
    type_colors = {
        "primary": {
            "background": "#1f77b4",
            "color": "white",
            "hover": "#1565a0"
        },
        "secondary": {
            "background": "#6c757d",
            "color": "white",
            "hover": "#5a6268"
        },
        "danger": {
            "background": "#dc3545",
            "color": "white",
            "hover": "#c82333"
        }
    }
    
    style = button_styles.get(size, button_styles["large"])
    colors = type_colors.get(type, type_colors["primary"])
    
    button_html = f"""
    <style>
    .mobile-button-{key or 'default'} {{
        min-height: {style['height']};
        font-size: {style['font_size']};
        padding: {style['padding']};
        background-color: {colors['background']};
        color: {colors['color']};
        border: none;
        border-radius: 8px;
        cursor: pointer;
        width: {'100%' if use_container_width else 'auto'};
        transition: all 0.2s;
        font-weight: 500;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 8px;
    }}
    .mobile-button-{key or 'default'}:hover {{
        background-color: {colors['hover']};
        transform: scale(0.98);
    }}
    .mobile-button-{key or 'default'}:active {{
        transform: scale(0.95);
    }}
    </style>
    """
    
    st.markdown(button_html, unsafe_allow_html=True)
    
    display_label = f"{icon} {label}" if icon else label
    
    return st.button(
        display_label,
        key=key,
        use_container_width=use_container_width,
        type=type if type != "danger" else "secondary"
    )


def render_bottom_navigation(items: List[Dict], active_index: int = 0):
    """
    Render bottom navigation bar for mobile
    
    Args:
        items: List of navigation items with 'icon', 'label', 'key'
        active_index: Index of active item
    """
    nav_html = """
    <style>
    .bottom-nav {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        background: white;
        border-top: 1px solid #e0e0e0;
        display: flex;
        justify-content: space-around;
        padding: 8px 0;
        z-index: 1000;
        box-shadow: 0 -2px 8px rgba(0,0,0,0.1);
    }
    .nav-item {
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 8px 16px;
        cursor: pointer;
        text-decoration: none;
        color: #666;
        min-width: 60px;
    }
    .nav-item.active {
        color: #1f77b4;
    }
    .nav-item-icon {
        font-size: 24px;
        margin-bottom: 4px;
    }
    .nav-item-label {
        font-size: 12px;
    }
    </style>
    <div class="bottom-nav">
    """
    
    for idx, item in enumerate(items):
        active_class = "active" if idx == active_index else ""
        nav_html += f"""
        <div class="nav-item {active_class}" onclick="window.location.href='#{item['key']}'">
            <div class="nav-item-icon">{item.get('icon', '')}</div>
            <div class="nav-item-label">{item.get('label', '')}</div>
        </div>
        """
    
    nav_html += "</div>"
    
    st.markdown(nav_html, unsafe_allow_html=True)
    
    # Add spacing at bottom to prevent content from being hidden
    st.markdown("<div style='height: 80px;'></div>", unsafe_allow_html=True)


def render_swipeable_card(content: str, key: str):
    """
    Render swipeable card for mobile
    
    Args:
        content: Card content (HTML)
        key: Unique key
    """
    card_html = f"""
    <style>
    .swipeable-card-{key} {{
        background: white;
        border-radius: 12px;
        padding: 16px;
        margin: 8px 0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        touch-action: pan-y;
        user-select: none;
    }}
    </style>
    <div class="swipeable-card-{key}">
        {content}
    </div>
    """
    
    st.markdown(card_html, unsafe_allow_html=True)


def render_quick_action_bar(actions: List[Dict], columns: int = 4):
    """
    Render quick action bar with large touch targets
    
    Args:
        actions: List of actions with 'icon', 'label', 'on_click', 'key'
        columns: Number of columns
    """
    cols = st.columns(columns)
    
    for idx, action in enumerate(actions):
        with cols[idx % columns]:
            if st.button(
                f"{action.get('icon', '')}\n{action.get('label', '')}",
                key=action.get('key', f"quick_action_{idx}"),
                use_container_width=True,
                help=action.get('tooltip', '')
            ):
                if action.get('on_click'):
                    action['on_click']()


def render_mobile_form_field(
    label: str,
    input_type: str = "text",
    key: Optional[str] = None,
    value: Optional[str] = None,
    placeholder: Optional[str] = None,
    required: bool = False
):
    """
    Render mobile-optimized form field
    
    Args:
        label: Field label
        input_type: Input type (text, number, select, etc.)
        key: Unique key
        value: Default value
        placeholder: Placeholder text
        required: Is required field
    """
    field_html = f"""
    <style>
    .mobile-form-field-{key or 'default'} {{
        margin-bottom: 20px;
    }}
    .mobile-form-label {{
        font-size: 16px;
        font-weight: 500;
        margin-bottom: 8px;
        display: block;
        color: #333;
    }}
    .mobile-form-input {{
        width: 100%;
        min-height: 48px;
        font-size: 16px;
        padding: 12px 16px;
        border: 2px solid #e0e0e0;
        border-radius: 8px;
        box-sizing: border-box;
    }}
    .mobile-form-input:focus {{
        border-color: #1f77b4;
        outline: none;
    }}
    </style>
    <div class="mobile-form-field-{key or 'default'}">
        <label class="mobile-form-label">
            {label}
            {(' <span style="color: red;">*</span>' if required else '')}
        </label>
    </div>
    """
    
    st.markdown(field_html, unsafe_allow_html=True)
    
    if input_type == "text":
        return st.text_input(
            "",
            value=value,
            placeholder=placeholder,
            key=key,
            label_visibility="collapsed"
        )
    elif input_type == "number":
        return st.number_input(
            "",
            value=float(value) if value else 0.0,
            key=key,
            label_visibility="collapsed"
        )
    elif input_type == "select":
        return st.selectbox(
            "",
            options=[],
            key=key,
            label_visibility="collapsed"
        )


def render_responsive_grid(items: List[Dict], columns_desktop: int = 4, columns_tablet: int = 2, columns_mobile: int = 1):
    """
    Render responsive grid layout
    
    Args:
        items: List of items to display
        columns_desktop: Number of columns on desktop
        columns_tablet: Number of columns on tablet
        columns_mobile: Number of columns on mobile
    """
    grid_html = f"""
    <style>
    .responsive-grid {{
        display: grid;
        grid-template-columns: repeat({columns_desktop}, 1fr);
        gap: 16px;
    }}
    @media (max-width: 768px) {{
        .responsive-grid {{
            grid-template-columns: repeat({columns_mobile}, 1fr);
        }}
    }}
    @media (min-width: 769px) and (max-width: 1024px) {{
        .responsive-grid {{
            grid-template-columns: repeat({columns_tablet}, 1fr);
        }}
    }}
    </style>
    <div class="responsive-grid">
    """
    
    for item in items:
        grid_html += f"<div>{item.get('content', '')}</div>"
    
    grid_html += "</div>"
    
    st.markdown(grid_html, unsafe_allow_html=True)


def detect_mobile_device() -> bool:
    """Detect if user is on mobile device"""
    # Simple detection based on user agent (if available)
    # In Streamlit, we can use session state or query params
    user_agent = st.query_params.get("user_agent", "")
    return any(mobile in user_agent.lower() for mobile in ["mobile", "android", "iphone", "ipad"])


def render_mobile_optimized_layout():
    """Render mobile-optimized layout wrapper"""
    is_mobile = detect_mobile_device()
    
    if is_mobile:
        st.markdown("""
        <style>
        .main {
            padding: 8px;
        }
        .stButton>button {
            min-height: 48px;
            font-size: 16px;
        }
        input, select, textarea {
            font-size: 16px !important;
        }
        </style>
        """, unsafe_allow_html=True)
