"""
Gastroenterology Protocols
Acute pancreatitis and GI emergency protocols
"""

from .acute_pancreatitis import render as render_acute_pancreatitis
from .acute_liver_failure import render as render_acute_liver_failure
from .ibd_exacerbation import render as render_ibd_exacerbation


__all__ = [
    'render_acute_pancreatitis',
    'render_acute_liver_failure',
    'render_ibd_exacerbation',
]

