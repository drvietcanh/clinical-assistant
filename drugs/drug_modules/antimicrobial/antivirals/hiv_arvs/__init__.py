"""
HIV Antiretrovirals (ARVs)
Combines all HIV ARVs from category-specific files
"""
from typing import Dict, Any

from .boosters import BOOSTERS_ARVS
from .integrase_inhibitors import INTEGRASE_INHIBITORS_ARVS
from .nnrti import NNRTI_ARVS
from .nrti import NRTI_ARVS
from .protease_inhibitors import PROTEASE_INHIBITORS_ARVS

# Combine all HIV ARVs
HIV_ARVS: Dict[str, Dict[str, Any]] = {
    **BOOSTERS_ARVS,
    **INTEGRASE_INHIBITORS_ARVS,
    **NNRTI_ARVS,
    **NRTI_ARVS,
    **PROTEASE_INHIBITORS_ARVS,
}

__all__ = ['HIV_ARVS']
