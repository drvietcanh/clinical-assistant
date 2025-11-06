"""
TDM (Therapeutic Drug Monitoring) Module
Tính toán và hướng dẫn TDM cho các thuốc cần theo dõi nồng độ
"""

from .digoxin import render_digoxin_tdm
from .phenytoin import render_phenytoin_tdm
from .lithium import render_lithium_tdm
from .theophylline import render_theophylline_tdm
from .immunosuppressants import render_immunosuppressants_tdm
from .vancomycin_tdm import render_vancomycin_tdm
from .aminoglycosides_tdm import render_aminoglycosides_tdm
from .carbamazepine_tdm import render_carbamazepine_tdm
from .valproic_acid_tdm import render_valproic_acid_tdm

__all__ = [
    'render_digoxin_tdm',
    'render_phenytoin_tdm',
    'render_lithium_tdm',
    'render_theophylline_tdm',
    'render_immunosuppressants_tdm',
    'render_vancomycin_tdm',
    'render_aminoglycosides_tdm',
    'render_carbamazepine_tdm',
    'render_valproic_acid_tdm'
]

