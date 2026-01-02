"""
Ophthalmology Drugs
Combines all ophthalmology drugs from category-specific files
"""
from typing import Dict, Any

from .anti_glaucoma import ANTI_GLAUCOMA_DRUGS
from .anti_infective import ANTI_INFECTIVE_DRUGS
from .anti_inflammatory import ANTI_INFLAMMATORY_DRUGS
from .antihistamines import ANTIHISTAMINES_DRUGS
from .lubricants import LUBRICANTS_DRUGS
from .mydriatics import MYDRIATICS_DRUGS

# Combine all ophthalmology drugs
OPHTHALMOLOGY_DRUGS: Dict[str, Dict[str, Any]] = {
    **ANTI_GLAUCOMA_DRUGS,
    **ANTI_INFECTIVE_DRUGS,
    **ANTI_INFLAMMATORY_DRUGS,
    **ANTIHISTAMINES_DRUGS,
    **LUBRICANTS_DRUGS,
    **MYDRIATICS_DRUGS,
}

__all__ = ['OPHTHALMOLOGY_DRUGS']
