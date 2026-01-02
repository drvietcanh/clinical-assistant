"""
Dermatology Drugs
Combines all dermatology drugs from category-specific files
"""
from typing import Dict, Any

from .other_topical import OTHER_TOPICAL_DRUGS
from .topical_antiacne import TOPICAL_ANTIACNE_DRUGS
from .topical_antibiotics import TOPICAL_ANTIBIOTICS_DRUGS
from .topical_antifungals import TOPICAL_ANTIFUNGALS_DRUGS
from .topical_corticosteroids import TOPICAL_CORTICOSTEROIDS_DRUGS
from .topical_retinoids import TOPICAL_RETINOIDS_DRUGS

# Combine all dermatology drugs
DERMATOLOGY_DRUGS: Dict[str, Dict[str, Any]] = {
    **OTHER_TOPICAL_DRUGS,
    **TOPICAL_ANTIACNE_DRUGS,
    **TOPICAL_ANTIBIOTICS_DRUGS,
    **TOPICAL_ANTIFUNGALS_DRUGS,
    **TOPICAL_CORTICOSTEROIDS_DRUGS,
    **TOPICAL_RETINOIDS_DRUGS,
}

__all__ = ['DERMATOLOGY_DRUGS']
