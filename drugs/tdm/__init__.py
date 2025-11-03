"""
TDM (Therapeutic Drug Monitoring) Module
Tính toán và hướng dẫn TDM cho các thuốc cần theo dõi nồng độ
"""

from .digoxin import render_digoxin_tdm
from .phenytoin import render_phenytoin_tdm
from .lithium import render_lithium_tdm
from .theophylline import render_theophylline_tdm
from .immunosuppressants import render_immunosuppressants_tdm

__all__ = [
    'render_digoxin_tdm',
    'render_phenytoin_tdm',
    'render_lithium_tdm',
    'render_theophylline_tdm',
    'render_immunosuppressants_tdm'
]

