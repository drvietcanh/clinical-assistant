"""
Drugs Module - Drug Database and Interaction Checker
Expanded beyond antibiotics to include all common medications
"""

from .interactions import render_interaction_checker
from .drug_info import render_drug_database
from .iv_compatibility import render_iv_compatibility_checker
from .visual_comparison import render_visual_comparison
from .dosing_schedule import render_dosing_schedule_generator

__all__ = [
    'render_interaction_checker',
    'render_drug_database',
    'render_iv_compatibility_checker',
    'render_visual_comparison',
    'render_dosing_schedule_generator',
]

