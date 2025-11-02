"""
Drugs Module - Drug Database and Interaction Checker
Expanded beyond antibiotics to include all common medications
"""

from .interactions import render_interaction_checker

__all__ = [
    'render_interaction_checker',
]

