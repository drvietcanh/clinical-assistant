"""
Obstetrics and Gynecology Drugs
Combines all OB/GYN drugs from category-specific files
"""
from typing import Dict, Any

from .contraceptives import CONTRACEPTIVES_DRUGS
from .hormone_replacement import HORMONE_REPLACEMENT_DRUGS
from .vaginal_medications import VAGINAL_MEDICATIONS_DRUGS
from .uterotonics import UTEROTONICS_DRUGS

# Combine all OB/GYN drugs
OBSTETRICS_GYNECOLOGY_DRUGS: Dict[str, Dict[str, Any]] = {
    **CONTRACEPTIVES_DRUGS,
    **HORMONE_REPLACEMENT_DRUGS,
    **VAGINAL_MEDICATIONS_DRUGS,
    **UTEROTONICS_DRUGS,
}

__all__ = ['OBSTETRICS_GYNECOLOGY_DRUGS']
