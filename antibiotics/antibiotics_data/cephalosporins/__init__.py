"""
Cephalosporins - All Generations
Merge all cephalosporin generations and special types
"""

from .generation_1 import GENERATION_1
from .generation_2 import GENERATION_2
from .generation_3 import GENERATION_3
from .generation_4 import GENERATION_4
from .generation_5 import GENERATION_5
from .cephamycins import CEPHAMYCINS
from .beta_lactamase_inhibitors import BETA_LACTAMASE_INHIBITORS

# Merge all cephalosporins
CEPHALOSPORINS = {
    **GENERATION_1,
    **GENERATION_2,
    **GENERATION_3,
    **GENERATION_4,
    **GENERATION_5,
    **CEPHAMYCINS,
    **BETA_LACTAMASE_INHIBITORS,
}

__all__ = [
    'GENERATION_1',
    'GENERATION_2',
    'GENERATION_3',
    'GENERATION_4',
    'GENERATION_5',
    'CEPHAMYCINS',
    'BETA_LACTAMASE_INHIBITORS',
    'CEPHALOSPORINS',
]

