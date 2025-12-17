"""
Respiratory Protocols
COPD, Asthma, and respiratory emergency protocols organized by individual files
"""

from .copd import render as render_copd
from .asthma import render as render_asthma
from .acute_respiratory_failure import render as render_acute_respiratory_failure
from .pulmonary_tb import render as render_pulmonary_tb
from .severe_influenza import render as render_severe_influenza
from .bronchiolitis import render as render_bronchiolitis


__all__ = [
    'render_copd',
    'render_asthma',
    'render_acute_respiratory_failure',
    'render_pulmonary_tb',
    'render_severe_influenza',
    'render_bronchiolitis',
]

