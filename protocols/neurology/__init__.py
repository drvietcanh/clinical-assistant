"""
Neurology Protocols Module
"""

from .serotonin_syndrome import render as render_serotonin_syndrome
from .neuroleptic_malignant_syndrome import render as render_neuroleptic_malignant_syndrome
from .intracranial_hypertension import render as render_intracranial_hypertension

__all__ = [
    'render_serotonin_syndrome',
    'render_neuroleptic_malignant_syndrome',
    'render_intracranial_hypertension',
]

