"""
Gastroenterology Protocols
Acute pancreatitis and GI emergency protocols
"""

from .acute_pancreatitis import render as render_acute_pancreatitis
from .acute_liver_failure import render as render_acute_liver_failure
from .ibd_exacerbation import render as render_ibd_exacerbation
from .acute_mesenteric_ischemia import render as render_acute_mesenteric_ischemia
from .cholecystitis_cholangitis import render as render_cholecystitis_cholangitis
from .acute_appendicitis import render as render_acute_appendicitis
from .acute_diverticulitis import render as render_acute_diverticulitis
from .acute_intestinal_obstruction import render as render_acute_intestinal_obstruction
from .acute_hepatitis import render as render_acute_hepatitis
from .acute_colitis import render as render_acute_colitis


__all__ = [
    'render_acute_pancreatitis',
    'render_acute_liver_failure',
    'render_ibd_exacerbation',
    'render_acute_mesenteric_ischemia',
    'render_cholecystitis_cholangitis',
    'render_acute_appendicitis',
    'render_acute_diverticulitis',
    'render_acute_intestinal_obstruction',
    'render_acute_hepatitis',
    'render_acute_colitis',
]

