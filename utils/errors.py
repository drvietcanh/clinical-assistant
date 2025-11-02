"""
Error Handling Utilities
Standardized error handling for calculators and modules
"""

import streamlit as st
from typing import Optional


class CalculatorNotFoundError(Exception):
    """Calculator not found in registry"""
    pass


class InvalidInputError(Exception):
    """Invalid input provided to calculator"""
    pass


class CalculationError(Exception):
    """Error during calculation"""
    pass


def handle_calculator_error(error: Exception, calculator_id: Optional[str] = None):
    """
    Handle calculator errors gracefully
    
    Args:
        error: Exception that occurred
        calculator_id: ID of calculator that failed
    
    Example:
        >>> try:
        ...     render_calculator("ascvd")
        ... except Exception as e:
        ...     handle_calculator_error(e, "ascvd")
    """
    if isinstance(error, CalculatorNotFoundError):
        st.error(f"❌ Calculator not found: `{calculator_id}`")
        st.info("💡 Try searching for similar calculators or check the calculator list.")
        st.markdown("---")
        
    elif isinstance(error, InvalidInputError):
        st.error("❌ Invalid input provided")
        st.warning(f"**Error:** {str(error)}")
        st.info("💡 Please check your inputs and try again.")
        
    elif isinstance(error, CalculationError):
        st.error("❌ Calculation error occurred")
        st.warning(f"**Error:** {str(error)}")
        st.info("💡 This might be due to invalid values. Please verify your inputs.")
        
    else:
        # Generic error
        st.error("❌ An unexpected error occurred")
        st.warning(f"**Error:** {str(error)}")
        st.info("""
        💡 **Troubleshooting:**
        - Check all input values are valid
        - Ensure required fields are filled
        - Try refreshing the page
        - If problem persists, please report this issue
        """)
    
    # Show error details in expander (for debugging)
    with st.expander("🔍 Error Details (For Developers)"):
        st.code(f"""
        Error Type: {type(error).__name__}
        Calculator ID: {calculator_id}
        Error Message: {str(error)}
        """, language="python")


def safe_render_calculator(calculator_func, calculator_id: str):
    """
    Safely render calculator with error handling
    
    Args:
        calculator_func: Function to render calculator
        calculator_id: ID of calculator
    
    Returns:
        True if successful, False if error occurred
    
    Example:
        >>> success = safe_render_calculator(render_ascvd, "ascvd")
    """
    try:
        calculator_func()
        return True
    except CalculatorNotFoundError as e:
        handle_calculator_error(e, calculator_id)
        return False
    except InvalidInputError as e:
        handle_calculator_error(e, calculator_id)
        return False
    except CalculationError as e:
        handle_calculator_error(e, calculator_id)
        return False
    except Exception as e:
        handle_calculator_error(e, calculator_id)
        return False


def validate_age(age: float, min_age: int = 0, max_age: int = 150) -> bool:
    """Validate age input"""
    if not isinstance(age, (int, float)):
        raise InvalidInputError(f"Age must be a number, got {type(age)}")
    if age < min_age or age > max_age:
        raise InvalidInputError(f"Age must be between {min_age} and {max_age}, got {age}")
    return True


def validate_weight(weight: float, min_weight: float = 0.1, max_weight: float = 500) -> bool:
    """Validate weight input"""
    if not isinstance(weight, (int, float)):
        raise InvalidInputError(f"Weight must be a number, got {type(weight)}")
    if weight < min_weight or weight > max_weight:
        raise InvalidInputError(f"Weight must be between {min_weight} and {max_weight} kg, got {weight}")
    return True


def validate_creatinine(creatinine: float, unit: str = "mg/dL") -> bool:
    """Validate creatinine input"""
    if not isinstance(creatinine, (int, float)):
        raise InvalidInputError(f"Creatinine must be a number, got {type(creatinine)}")
    
    if unit == "mg/dL":
        if creatinine < 0.1 or creatinine > 50:
            raise InvalidInputError(f"Creatinine must be between 0.1 and 50 mg/dL, got {creatinine}")
    elif unit == "µmol/L":
        if creatinine < 8.8 or creatinine > 4420:
            raise InvalidInputError(f"Creatinine must be between 8.8 and 4420 µmol/L, got {creatinine}")
    
    return True


__all__ = [
    'CalculatorNotFoundError',
    'InvalidInputError',
    'CalculationError',
    'handle_calculator_error',
    'safe_render_calculator',
    'validate_age',
    'validate_weight',
    'validate_creatinine',
]

