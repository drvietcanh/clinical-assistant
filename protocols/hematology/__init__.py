"""
Hematology Protocols
Transfusion and anticoagulation protocols
"""

from .transfusion import render as render_transfusion
from .anticoagulation_reversal import render as render_anticoagulation_reversal
from .itp import render as render_itp
from .ttp_hus import render as render_ttp_hus
from .dic import render as render_dic


__all__ = [
    'render_transfusion',
    'render_anticoagulation_reversal',
    'render_itp',
    'render_ttp_hus',
    'render_dic',
]

