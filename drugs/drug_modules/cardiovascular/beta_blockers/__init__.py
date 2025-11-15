"""
Beta-blockers Module
Combines all beta-blocker categories
"""

from .selective import SELECTIVE_BETA_BLOCKERS
from .non_selective import NON_SELECTIVE_BETA_BLOCKERS

# Merge all beta-blocker categories
BETA_BLOCKERS = {
    **SELECTIVE_BETA_BLOCKERS,
    **NON_SELECTIVE_BETA_BLOCKERS,
}

__all__ = ['BETA_BLOCKERS']

