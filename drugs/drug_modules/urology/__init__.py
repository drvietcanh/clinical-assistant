"""
Urology Drugs
Combines all urology drugs from category-specific files
"""
from typing import Dict, Any

from .bph_5_alpha_reductase import BPH_5_ALPHA_REDUCTASE_DRUGS
from .bph_alpha_blockers import BPH_ALPHA_BLOCKERS_DRUGS
from .erectile_dysfunction import ERECTILE_DYSFUNCTION_DRUGS
from .overactive_bladder import OVERACTIVE_BLADDER_DRUGS

# Combine all urology drugs
UROLOGY_DRUGS: Dict[str, Dict[str, Any]] = {
    **BPH_5_ALPHA_REDUCTASE_DRUGS,
    **BPH_ALPHA_BLOCKERS_DRUGS,
    **ERECTILE_DYSFUNCTION_DRUGS,
    **OVERACTIVE_BLADDER_DRUGS,
}

__all__ = ['UROLOGY_DRUGS']
