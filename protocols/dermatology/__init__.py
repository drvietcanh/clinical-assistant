"""
Dermatology Protocols Module
"""

from .stevens_johnson_syndrome import render as render_stevens_johnson_syndrome
from .atopic_dermatitis import render as render_atopic_dermatitis
from .contact_dermatitis import render as render_contact_dermatitis
from .acne_vulgaris import render as render_acne_vulgaris
from .fungal_infections import render as render_fungal_infections
from .scabies import render as render_scabies
from .urticaria import render as render_urticaria
from .psoriasis import render as render_psoriasis

__all__ = [
    'render_stevens_johnson_syndrome',
    'render_atopic_dermatitis',
    'render_contact_dermatitis',
    'render_acne_vulgaris',
    'render_fungal_infections',
    'render_scabies',
    'render_urticaria',
    'render_psoriasis',
]

