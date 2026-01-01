"""
Theme Configuration
Centralized theme system for consistent design across the app
"""

from typing import Dict


# Color Palette - Standardized for Medical Apps (MDCalc/UpToDate style)
COLORS = {
    # Primary - Medical Blue (UpToDate style)
    "primary": "#1976d2",
    "primary_dark": "#1565c0",
    "primary_light": "#42a5f5",
    
    # Success - Green (Low risk)
    "success": "#4caf50",
    "success_dark": "#388e3c",
    "success_light": "#81c784",
    
    # Warning - Orange (Moderate risk)
    "warning": "#ff9800",
    "warning_dark": "#f57c00",
    "warning_light": "#ffb74d",
    
    # Error - Red (High/Critical risk)
    "error": "#f44336",
    "error_dark": "#d32f2f",
    "error_light": "#e57373",
    
    # Info - Light Blue
    "info": "#03a9f4",
    "info_dark": "#0288d1",
    "info_light": "#4fc3f7",
    
    # Neutral - Grey
    "neutral": "#9e9e9e",
    "neutral_dark": "#757575",
    "neutral_light": "#bdbdbd",
    
    # Text Colors
    "text_primary": "#212121",
    "text_secondary": "#757575",
    "text_disabled": "#bdbdbd",
    
    # Background Colors
    "background": "#ffffff",
    "background_secondary": "#fafafa",
    "surface": "#ffffff",
    "border": "#e0e0e0",
    
    # Score Risk Colors (MDCalc style)
    "risk_low": "#4caf50",        # Green - Low risk (0-6)
    "risk_moderate": "#ff9800",  # Orange - Moderate risk (7-11)
    "risk_high": "#ff5722",      # Deep Orange - High risk (12-14)
    "risk_critical": "#f44336",  # Red - Critical risk (15+)
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


# Typography - Standardized Hierarchy
TYPOGRAPHY = {
    "font_family": "system-ui, -apple-system, 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif",
    # Heading sizes (MDCalc/UpToDate style)
    "h1": "2.5rem",      # 40px - Page titles
    "h2": "1.875rem",   # 30px - Section headers
    "h3": "1.5rem",     # 24px - Subsection headers
    "h4": "1.25rem",    # 20px - Card titles
    # Body sizes
    "font_size_small": "0.875rem",    # 14px - Captions, small text
    "font_size_base": "1rem",          # 16px - Body text
    "font_size_large": "1.25rem",      # 20px - Emphasized text
    "font_size_xlarge": "1.5rem",      # 24px - Large text
    # Font weights
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

