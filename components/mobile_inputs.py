"""
Mobile-Optimized Input Components
Better input types and keyboard optimization for mobile devices
"""

import streamlit as st
from typing import Optional, Union


def mobile_number_input(
    label: str,
    min_value: Optional[float] = None,
    max_value: Optional[float] = None,
    value: Optional[float] = None,
    step: Optional[Union[float, int]] = None,
    key: Optional[str] = None,
    help: Optional[str] = None,
    **kwargs
):
    """
    Mobile-optimized number input with numeric keyboard
    
    Args:
        label: Input label
        min_value: Minimum value
        max_value: Maximum value
        value: Default value
        step: Step size
        key: Unique key
        help: Help text
        **kwargs: Additional st.number_input arguments
    
    Returns:
        Input value
    """
    # Add mobile-specific CSS
    st.markdown(
        """
        <style>
        /* Mobile number input optimization */
        @media (max-width: 768px) {
            .stNumberInput input[type="number"] {
                -webkit-appearance: none;
                -moz-appearance: textfield;
            }
            
            .stNumberInput input[type="number"]::-webkit-inner-spin-button,
            .stNumberInput input[type="number"]::-webkit-outer-spin-button {
                -webkit-appearance: none;
                margin: 0;
            }
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    return st.number_input(
        label,
        min_value=min_value,
        max_value=max_value,
        value=value,
        step=step,
        key=key,
        help=help,
        **kwargs
    )


def mobile_text_input(
    label: str,
    value: str = "",
    max_chars: Optional[int] = None,
    type: str = "default",
    key: Optional[str] = None,
    help: Optional[str] = None,
    placeholder: Optional[str] = None,
    **kwargs
):
    """
    Mobile-optimized text input with appropriate keyboard type
    
    Args:
        label: Input label
        value: Default value
        max_chars: Maximum characters
        type: Input type ("default", "email", "tel", "url", "search")
        key: Unique key
        help: Help text
        placeholder: Placeholder text
        **kwargs: Additional st.text_input arguments
    
    Returns:
        Input value
    """
    # Map input types to mobile keyboard types
    input_type_map = {
        "email": "email",
        "tel": "tel",
        "url": "url",
        "search": "search",
        "default": "text"
    }
    
    input_type = input_type_map.get(type, "text")
    
    # Add mobile-specific attributes via JavaScript
    if key:
        st.markdown(
            f"""
            <script>
            // Set input type for mobile keyboard optimization
            (function() {{
                const input = document.querySelector('input[data-testid*="{key}"]');
                if (input && window.innerWidth <= 768) {{
                    input.type = "{input_type}";
                    input.inputMode = "{input_type}";
                    {'input.maxLength = ' + str(max_chars) + ';' if max_chars else ''}
                }}
            }})();
            </script>
            """,
            unsafe_allow_html=True
        )
    
    return st.text_input(
        label,
        value=value,
        max_chars=max_chars,
        key=key,
        help=help,
        placeholder=placeholder,
        **kwargs
    )


def render_mobile_input_optimizations():
    """
    Add global mobile input optimizations
    """
    st.markdown(
        """
        <style>
        /* Mobile input optimizations */
        @media (max-width: 768px) {
            /* Prevent zoom on input focus (iOS Safari) */
            input[type="text"],
            input[type="number"],
            input[type="email"],
            input[type="tel"],
            input[type="url"],
            input[type="search"],
            select,
            textarea {
                font-size: 16px !important;
            }
            
            /* Better touch targets */
            input, select, textarea {
                min-height: 48px;
                padding: 12px 16px;
            }
            
            /* Remove spinner buttons on number inputs (mobile) */
            input[type="number"]::-webkit-inner-spin-button,
            input[type="number"]::-webkit-outer-spin-button {
                opacity: 1;
                height: 48px;
            }
            
            /* Better autocomplete styling */
            input:-webkit-autofill {
                -webkit-box-shadow: 0 0 0 1000px white inset;
                -webkit-text-fill-color: var(--text-primary);
            }
            
            [data-theme="dark"] input:-webkit-autofill {
                -webkit-box-shadow: 0 0 0 1000px #1e1e1e inset;
                -webkit-text-fill-color: var(--text-primary);
            }
            
            /* Focus states */
            input:focus,
            select:focus,
            textarea:focus {
                outline: 2px solid var(--primary);
                outline-offset: 2px;
            }
        }
        </style>
        """,
        unsafe_allow_html=True
    )

