"""
Obstetrics & Gynecology Protocols Module
"""

from .eclampsia import render as render_eclampsia
from .postpartum_hemorrhage import render as render_postpartum_hemorrhage

__all__ = [
    'render_eclampsia',
    'render_postpartum_hemorrhage',
]

