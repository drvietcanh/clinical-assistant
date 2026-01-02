"""
Enhanced fields overrides
Combines all enhanced fields from category-specific files
"""
from typing import Any, Dict

from .antimicrobial import ANTIMICROBIAL_ENHANCED_FIELDS
from .cardiovascular import CARDIOVASCULAR_ENHANCED_FIELDS
from .emergency import EMERGENCY_ENHANCED_FIELDS
from .gastrointestinal import GASTROINTESTINAL_ENHANCED_FIELDS
from .neurological import NEUROLOGICAL_ENHANCED_FIELDS
from .other import OTHER_ENHANCED_FIELDS
from .respiratory import RESPIRATORY_ENHANCED_FIELDS

# Combine all enhanced fields
EXTRA_ENHANCED_FIELDS: Dict[str, Dict[str, Any]] = {
    **ANTIMICROBIAL_ENHANCED_FIELDS,
    **CARDIOVASCULAR_ENHANCED_FIELDS,
    **EMERGENCY_ENHANCED_FIELDS,
    **GASTROINTESTINAL_ENHANCED_FIELDS,
    **NEUROLOGICAL_ENHANCED_FIELDS,
    **OTHER_ENHANCED_FIELDS,
    **RESPIRATORY_ENHANCED_FIELDS,
}

__all__ = ["EXTRA_ENHANCED_FIELDS"]
