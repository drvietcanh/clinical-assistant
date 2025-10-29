"""
Respiratory Protocols
COPD, Asthma, and respiratory emergency protocols organized by individual files
"""

from .copd import render as render_copd
from .asthma import render as render_asthma


__all__ = [
    'render_copd',
    'render_asthma',
]

