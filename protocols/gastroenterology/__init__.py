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
from .hepatitis_b import render as render_hepatitis_b
from .h_pylori_gastritis import render as render_h_pylori_gastritis
from .hepatitis_c import render as render_hepatitis_c
from .gerd import render as render_gerd
from .ibs import render as render_ibs
from .cirrhosis import render as render_cirrhosis
from .nafld import render as render_nafld
from .chronic_constipation import render as render_chronic_constipation
from .acute_diarrhea import render as render_acute_diarrhea
from .lower_gi_bleeding import render as render_lower_gi_bleeding
from .perforated_peptic_ulcer import render as render_perforated_peptic_ulcer
from .biliary_obstruction import render as render_biliary_obstruction
from .decompensated_cirrhosis import render as render_decompensated_cirrhosis


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
    'render_hepatitis_b',
    'render_h_pylori_gastritis',
    'render_hepatitis_c',
    'render_gerd',
    'render_ibs',
    'render_cirrhosis',
    'render_nafld',
    'render_chronic_constipation',
    'render_acute_diarrhea',
    'render_lower_gi_bleeding',
    'render_perforated_peptic_ulcer',
    'render_biliary_obstruction',
    'render_decompensated_cirrhosis',
]

