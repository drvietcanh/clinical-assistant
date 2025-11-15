"""
Enhanced Fields Schema - All Fields
Merge basic fields, extended fields, functions, and examples
"""

from .basic_fields import BASIC_FIELDS
from .extended_fields import EXTENDED_FIELDS
from .functions import (
    create_enhanced_fields_template,
    validate_enhanced_fields,
    generate_enhanced_fields_guidelines
)
from .examples import EXAMPLE_ENHANCED_FIELDS

# Merge all fields
ENHANCED_FIELDS_SCHEMA = {
    **BASIC_FIELDS,
    **EXTENDED_FIELDS,
}

__all__ = [
    'BASIC_FIELDS',
    'EXTENDED_FIELDS',
    'ENHANCED_FIELDS_SCHEMA',
    'create_enhanced_fields_template',
    'validate_enhanced_fields',
    'generate_enhanced_fields_guidelines',
    'EXAMPLE_ENHANCED_FIELDS',
]

