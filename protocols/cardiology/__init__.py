"""
Cardiology Protocols
ACS, Heart Failure, and cardiac emergency protocols organized by individual files
"""

from .acs import render as render_acs
from .heart_failure import render as render_hf


__all__ = [
    'render_acs',
    'render_hf',
]

