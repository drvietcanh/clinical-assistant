"""
Respiratory Protocols
COPD, Asthma, and respiratory emergency protocols organized by individual files
"""

from .copd import render as render_copd
from .asthma import render as render_asthma
from .acute_respiratory_failure import render as render_acute_respiratory_failure
from .pulmonary_tb import render as render_pulmonary_tb
from .pulmonary_tb_vn import render as render_pulmonary_tb_vn
from .severe_influenza import render as render_severe_influenza
from .bronchiolitis import render as render_bronchiolitis


__all__ = [
    'render_copd',
    'render_asthma',
    'render_acute_respiratory_failure',
    'render_pulmonary_tb',
    'render_pulmonary_tb_vn',
    'render_severe_influenza',
    'render_bronchiolitis',
]

