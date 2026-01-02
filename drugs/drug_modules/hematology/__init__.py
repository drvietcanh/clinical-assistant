"""
Hematology Drugs
Combines all hematology drugs from category-specific files
"""
from typing import Dict, Any

from .anticoagulants import ANTICOAGULANTS_DRUGS
from .antiplatelets import ANTIPLATELETS_DRUGS
from .growth_factors import GROWTH_FACTORS_DRUGS
from .hemostatics import HEMOSTATICS_DRUGS
from .other_hematology import OTHER_HEMATOLOGY_DRUGS
from .reversal_agents import REVERSAL_AGENTS_DRUGS
from .thrombolytics import THROMBOLYTICS_DRUGS

# Combine all hematology drugs
HEMATOLOGY_DRUGS: Dict[str, Dict[str, Any]] = {
    **ANTICOAGULANTS_DRUGS,
    **ANTIPLATELETS_DRUGS,
    **GROWTH_FACTORS_DRUGS,
    **HEMOSTATICS_DRUGS,
    **OTHER_HEMATOLOGY_DRUGS,
    **REVERSAL_AGENTS_DRUGS,
    **THROMBOLYTICS_DRUGS,
}

__all__ = ['HEMATOLOGY_DRUGS']
