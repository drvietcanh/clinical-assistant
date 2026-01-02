"""
Biological Drugs
Combines all biological drugs from category-specific files
"""
from typing import Dict, Any

from .fusion_proteins import FUSION_PROTEINS_DRUGS
from .monoclonal_antibodies import MONOCLONAL_ANTIBODIES_DRUGS
from .other_biological import OTHER_BIOLOGICAL_DRUGS

# Combine all biological drugs
BIOLOGICAL_DRUGS: Dict[str, Dict[str, Any]] = {
    **FUSION_PROTEINS_DRUGS,
    **MONOCLONAL_ANTIBODIES_DRUGS,
    **OTHER_BIOLOGICAL_DRUGS,
}

__all__ = ['BIOLOGICAL_DRUGS']
