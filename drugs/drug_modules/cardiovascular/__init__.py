"""
Cardiovascular Drugs Package
All cardiovascular drug modules organized by therapeutic subgroup
"""

# Import all drug categories
from .other_cv import OTHER_CV_DRUGS

# Merge all categories
CARDIOVASCULAR_DRUGS = {
    **OTHER_CV_DRUGS,
}

__all__ = ['CARDIOVASCULAR_DRUGS']
