"""
Respiratory Protocols
COPD, Asthma, and respiratory emergency protocols organized by individual files
"""

from .copd import render as render_copd
from .asthma import render as render_asthma
from .acute_respiratory_failure import render as render_acute_respiratory_failure


__all__ = [
    'render_copd',
    'render_asthma',
    'render_acute_respiratory_failure',
]

