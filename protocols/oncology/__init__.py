"""
Oncology Protocols Module
"""

from .tls import render as render_tls
from .febrile_neutropenia import render as render_febrile_neutropenia
from .hypercalcemia import render as render_hypercalcemia

__all__ = [
    'render_tls',
    'render_febrile_neutropenia',
    'render_hypercalcemia',
]

