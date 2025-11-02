"""
Input Components
Standardized input components with units and validation
"""

import streamlit as st
from typing import Optional, List, Tuple, Dict
from config.theme import THEME


def render_number_input_with_unit(
    label: str,
    key: str,
    min_value: Optional[float] = None,
    max_value: Optional[float] = None,
    value: Optional[float] = None,
    step: Optional[float] = None,
    unit_options: Optional[List[Tuple[str, str]]] = None,
    default_unit: Optional[str] = None,
    format: Optional[str] = None,
    help_text: Optional[str] = None,
    required: bool = False,
    **kwargs
) -> Tuple[float, str]:
    """
    Render a number input with unit selection
    
    Args:
        label: Input label
        key: Unique key for the widget
        min_value: Minimum allowed value
        max_value: Maximum allowed value
        value: Default value
        step: Step size for number input
        unit_options: List of (unit_name, unit_label) tuples
        default_unit: Default unit selection
        format: Format string for number (e.g., "%.1f", "%.0f")
        help_text: Help text to display
        required: Whether input is required
        **kwargs: Additional arguments passed to st.number_input
    
    Returns:
        Tuple of (value, unit)
    
    Example:
        >>> value, unit = render_number_input_with_unit(
        ...     "Creatinine", "creatinine",
        ...     min_value=0.1, max_value=50,
        ...     unit_options=[("mg/dL", "mg/dL"), ("µmol/L", "µmol/L")],
        ...     default_unit="µmol/L",
        ...     format="%.1f"
        ... )
    """
    col1, col2 = st.columns([3, 1])
    
    with col1:
        number_input = st.number_input(
            label + (" *" if required else ""),
            min_value=min_value,
            max_value=max_value,
            value=value,
            step=step,
            format=format,
            help=help_text,
            key=f"{key}_value",
            **kwargs
        )
    
    with col2:
        if unit_options:
            unit_labels = [label for _, label in unit_options]
            unit_values = [value for value, _ in unit_options]
            
            default_idx = 0
            if default_unit:
                for idx, (val, _) in enumerate(unit_options):
                    if val == default_unit:
                        default_idx = idx
                        break
            
            unit_label = st.selectbox(
                "Đơn vị",
                unit_labels,
                index=default_idx,
                key=f"{key}_unit",
                label_visibility="collapsed"
            )
            
            # Get unit value
            unit_idx = unit_labels.index(unit_label)
            unit = unit_values[unit_idx]
        else:
            unit = None
    
    return number_input, unit


def render_select_with_icon(
    label: str,
    options: List[Tuple[str, str, str]],  # (value, label, icon)
    key: str,
    default_index: int = 0,
    help_text: Optional[str] = None,
    **kwargs
) -> str:
    """
    Render a selectbox with icons
    
    Args:
        label: Select label
        options: List of (value, label, icon) tuples
        key: Unique key for the widget
        default_index: Default selected index
        help_text: Help text
        **kwargs: Additional arguments
    
    Returns:
        Selected value
    
    Example:
        >>> value = render_select_with_icon(
        ...     "Gender", 
        ...     [("M", "Male", "👨"), ("F", "Female", "👩")],
        ...     "gender"
        ... )
    """
    # Format options with icons
    formatted_options = [f"{icon} {label}" for _, label, icon in options]
    values = [value for value, _, _ in options]
    
    selected_label = st.selectbox(
        label,
        formatted_options,
        index=default_index,
        help=help_text,
        key=key,
        **kwargs
    )
    
    # Get selected value
    selected_idx = formatted_options.index(selected_label)
    return values[selected_idx]


def render_multi_select(
    label: str,
    options: List[Tuple[str, str]],  # (value, label)
    key: str,
    default: Optional[List[str]] = None,
    help_text: Optional[str] = None,
    **kwargs
) -> List[str]:
    """
    Render a multi-select component
    
    Args:
        label: Select label
        options: List of (value, label) tuples
        key: Unique key
        default: Default selected values
        help_text: Help text
        **kwargs: Additional arguments
    
    Returns:
        List of selected values
    
    Example:
        >>> selected = render_multi_select(
        ...     "Symptoms",
        ...     [("fever", "Fever"), ("cough", "Cough")],
        ...     "symptoms"
        ... )
    """
    labels = [label for _, label in options]
    values = [value for value, _ in options]
    
    default_indices = []
    if default:
        default_indices = [values.index(v) for v in default if v in values]
    
    selected_labels = st.multiselect(
        label,
        labels,
        default=default_indices,
        help=help_text,
        key=key,
        **kwargs
    )
    
    # Convert back to values
    selected = []
    for label in selected_labels:
        idx = labels.index(label)
        selected.append(values[idx])
    
    return selected


def render_boolean_toggle(
    label: str,
    key: str,
    default: bool = False,
    help_text: Optional[str] = None,
    **kwargs
) -> bool:
    """
    Render a boolean toggle/checkbox
    
    Args:
        label: Toggle label
        key: Unique key
        default: Default value
        help_text: Help text
        **kwargs: Additional arguments
    
    Returns:
        Boolean value
    
    Example:
        >>> diabetes = render_boolean_toggle("Type 2 Diabetes", "diabetes")
    """
    return st.checkbox(
        label,
        value=default,
        help=help_text,
        key=key,
        **kwargs
    )

