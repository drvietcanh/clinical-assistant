"""
Gastroenterology Protocols
Acute pancreatitis and GI emergency protocols
"""

from .acute_pancreatitis import render as render_acute_pancreatitis
from .acute_liver_failure import render as render_acute_liver_failure
from .ibd_exacerbation import render as render_ibd_exacerbation
from .acute_mesenteric_ischemia import render as render_acute_mesenteric_ischemia
from .cholecystitis_cholangitis import render as render_cholecystitis_cholangitis


__all__ = [
    'render_acute_pancreatitis',
    'render_acute_liver_failure',
    'render_ibd_exacerbation',
    'render_acute_mesenteric_ischemia',
    'render_cholecystitis_cholangitis',
]

