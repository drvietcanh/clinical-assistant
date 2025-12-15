"""
Validation UI Components
Standardized components for displaying validation errors and warnings
"""

import streamlit as st
from typing import List, Optional


def render_validation_errors(errors: List[str], title: Optional[str] = None) -> None:
    """
    Render validation errors in a standardized format
    
    Args:
        errors: List of error messages
        title: Optional custom title (default: "⚠️ Lỗi validation")
    """
    if errors:
        error_title = title if title else "**⚠️ Lỗi validation:**"
        st.error(error_title)
        for error in errors:
            st.error(f"- {error}")
        st.stop()


def render_validation_warning(warning: str, icon: str = "⚠️") -> None:
    """
    Render a validation warning
    
    Args:
        warning: Warning message
        icon: Optional icon (default: "⚠️")
    """
    st.warning(f"{icon} {warning}")


def render_validation_info(info: str, icon: str = "ℹ️") -> None:
    """
    Render validation information
    
    Args:
        info: Information message
        icon: Optional icon (default: "ℹ️")
    """
    st.info(f"{icon} {info}")


def render_validation_success(message: str, icon: str = "✅") -> None:
    """
    Render a validation success message
    
    Args:
        message: Success message
        icon: Optional icon (default: "✅")
    """
    st.success(f"{icon} {message}")

