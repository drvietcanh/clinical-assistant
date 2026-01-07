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
    show_clear_button: bool = True,
    **kwargs
):
    """
    Mobile-optimized text input with appropriate keyboard type
    
    Args:
        label: Input label
        value: Default value
        max_chars: Maximum characters
        type: Input type ("default", "email", "tel", "url", "search", "numeric", "decimal")
        key: Unique key
        help: Help text
        placeholder: Placeholder text
        show_clear_button: Show clear button on mobile
        **kwargs: Additional st.text_input arguments
    
    Returns:
        Input value
    """
    # Map input types to mobile keyboard types and inputmode
    input_type_map = {
        "email": ("email", "email"),
        "tel": ("tel", "tel"),
        "url": ("url", "url"),
        "search": ("search", "search"),
        "numeric": ("text", "numeric"),
        "decimal": ("text", "decimal"),
        "default": ("text", "text")
    }
    
    input_type, input_mode = input_type_map.get(type, ("text", "text"))
    
    # Add mobile-specific attributes via JavaScript
    if key:
        clear_button_script = ""
        if show_clear_button:
            clear_button_script = f"""
            // Add clear button
            const clearBtn = document.createElement('button');
            clearBtn.type = 'button';
            clearBtn.innerHTML = '✕';
            clearBtn.style.cssText = `
                position: absolute;
                right: 8px;
                top: 50%;
                transform: translateY(-50%);
                background: transparent;
                border: none;
                font-size: 18px;
                color: #999;
                cursor: pointer;
                padding: 4px 8px;
                z-index: 10;
                display: none;
            `;
            clearBtn.onclick = function() {{
                input.value = '';
                input.dispatchEvent(new Event('input', {{ bubbles: true }}));
                clearBtn.style.display = 'none';
            }};
            input.parentElement.style.position = 'relative';
            input.parentElement.appendChild(clearBtn);
            
            input.addEventListener('input', function() {{
                clearBtn.style.display = input.value ? 'block' : 'none';
            }});
            """
        
        st.markdown(
            f"""
            <script>
            // Set input type for mobile keyboard optimization
            (function() {{
                const input = document.querySelector('input[data-testid*="{key}"]');
                if (input && window.innerWidth <= 768) {{
                    input.type = "{input_type}";
                    input.setAttribute('inputmode', "{input_mode}");
                    {'input.maxLength = ' + str(max_chars) + ';' if max_chars else ''}
                    input.setAttribute('autocomplete', "{type if type in ['email', 'tel', 'url'] else 'off'}");
                    {clear_button_script}
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
                touch-action: manipulation;
            }
            
            /* Remove spinner buttons on number inputs (mobile) */
            input[type="number"]::-webkit-inner-spin-button,
            input[type="number"]::-webkit-outer-spin-button {
                opacity: 1;
                height: 48px;
                width: 32px;
            }
            
            /* Better autocomplete styling */
            input:-webkit-autofill {
                -webkit-box-shadow: 0 0 0 1000px white inset;
                -webkit-text-fill-color: var(--text-primary, #212529);
                font-size: 16px !important;
            }
            
            [data-theme="dark"] input:-webkit-autofill {
                -webkit-box-shadow: 0 0 0 1000px #1e1e1e inset;
                -webkit-text-fill-color: var(--text-primary, #E5E7EB);
            }
            
            /* Focus states */
            input:focus,
            select:focus,
            textarea:focus {
                outline: 2px solid var(--primary, #2D7DF6);
                outline-offset: 2px;
                border-color: var(--primary, #2D7DF6);
            }
            
            /* Input container for clear button */
            .stTextInput > div > div {
                position: relative;
            }
            
            /* Better select dropdown on mobile */
            select {
                appearance: none;
                background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' viewBox='0 0 12 12'%3E%3Cpath fill='%23666' d='M6 9L1 4h10z'/%3E%3C/svg%3E");
                background-repeat: no-repeat;
                background-position: right 12px center;
                padding-right: 40px;
            }
            
            /* Textarea optimization */
            textarea {
                resize: vertical;
                min-height: 100px;
            }
        }
        </style>
        """,
        unsafe_allow_html=True
    )

