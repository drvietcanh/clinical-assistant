"""
Endocrinology Protocols Module
"""

from .thyrotoxic_crisis import render as render_thyrotoxic_crisis
from .myxedema_coma import render as render_myxedema_coma
from .adrenal_crisis import render as render_adrenal_crisis
from .hhs import render as render_hhs

__all__ = [
    'render_thyrotoxic_crisis',
    'render_myxedema_coma',
    'render_adrenal_crisis',
    'render_hhs',
]

