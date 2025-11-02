"""
Theme Configuration
Centralized theme system for consistent design across the app
"""

from typing import Dict


# Color Palette
COLORS = {
    "primary": "#0EA5E9",
    "primary_dark": "#0c84c7",
    "primary_light": "#3db8f5",
    
    "success": "#4caf50",
    "success_dark": "#388e3c",
    "success_light": "#81c784",
    
    "warning": "#ff9800",
    "warning_dark": "#f57c00",
    "warning_light": "#ffb74d",
    
    "error": "#f44336",
    "error_dark": "#d32f2f",
    "error_light": "#e57373",
    
    "info": "#2196f3",
    "info_dark": "#1976d2",
    "info_light": "#64b5f6",
    
    "text_primary": "#212121",
    "text_secondary": "#757575",
    "text_disabled": "#bdbdbd",
    
    "background": "#ffffff",
    "background_secondary": "#f5f5f5",
    "surface": "#ffffff",
}


# Module Gradients
MODULE_GRADIENTS = {
    "scores": "linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%)",
    "antibiotics": "linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%)",
    "labs": "linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%)",
    "ventilator": "linear-gradient(135deg, #fce4ec 0%, #f8bbd0 100%)",
    "protocols": "linear-gradient(135deg, #f3e5f5 0%, #e1bee7 100%)",
    "calculators": "linear-gradient(135deg, #e0f2f1 0%, #b2dfdb 100%)",
}


# Module Border Colors
MODULE_BORDERS = {
    "scores": "#1976d2",
    "antibiotics": "#4caf50",
    "labs": "#ff9800",
    "ventilator": "#e91e63",
    "protocols": "#9c27b0",
    "calculators": "#009688",
}


# Spacing System
SPACING = {
    "xs": "0.25rem",    # 4px
    "sm": "0.5rem",     # 8px
    "md": "1rem",       # 16px
    "lg": "1.5rem",     # 24px
    "xl": "2rem",       # 32px
    "xxl": "3rem",      # 48px
}


# Typography
TYPOGRAPHY = {
    "font_family": "'Segoe UI', Tahoma, Geneva, Verdana, sans-serif",
    "font_size_small": "0.875rem",    # 14px
    "font_size_base": "1rem",          # 16px
    "font_size_large": "1.25rem",      # 20px
    "font_size_xlarge": "1.5rem",      # 24px
    "font_weight_normal": "400",
    "font_weight_medium": "500",
    "font_weight_bold": "700",
}


# Border Radius
BORDER_RADIUS = {
    "small": "4px",
    "medium": "8px",
    "large": "12px",
    "xlarge": "16px",
    "round": "50%",
}


# Shadows
SHADOWS = {
    "none": "none",
    "sm": "0 1px 2px rgba(0, 0, 0, 0.05)",
    "md": "0 4px 6px rgba(0, 0, 0, 0.1)",
    "lg": "0 10px 15px rgba(0, 0, 0, 0.1)",
    "xl": "0 20px 25px rgba(0, 0, 0, 0.15)",
}


# Theme Configuration
THEME = {
    "colors": COLORS,
    "module_gradients": MODULE_GRADIENTS,
    "module_borders": MODULE_BORDERS,
    "spacing": SPACING,
    "typography": TYPOGRAPHY,
    "border_radius": BORDER_RADIUS,
    "shadows": SHADOWS,
}


def get_module_style(module_id: str) -> Dict[str, str]:
    """
    Get style configuration for a module
    
    Args:
        module_id: ID of the module (scores, antibiotics, etc.)
    
    Returns:
        Dictionary with gradient and border color
    
    Example:
        >>> style = get_module_style("scores")
        >>> gradient = style["gradient"]
        >>> border = style["border"]
    """
    return {
        "gradient": MODULE_GRADIENTS.get(module_id, MODULE_GRADIENTS["scores"]),
        "border": MODULE_BORDERS.get(module_id, MODULE_BORDERS["scores"]),
    }


def get_color(color_name: str) -> str:
    """Get color by name"""
    return COLORS.get(color_name, COLORS["text_primary"])


def get_spacing(size: str) -> str:
    """Get spacing by size"""
    return SPACING.get(size, SPACING["md"])


__all__ = [
    'THEME',
    'COLORS',
    'MODULE_GRADIENTS',
    'MODULE_BORDERS',
    'SPACING',
    'TYPOGRAPHY',
    'BORDER_RADIUS',
    'SHADOWS',
    'get_module_style',
    'get_color',
    'get_spacing',
]

