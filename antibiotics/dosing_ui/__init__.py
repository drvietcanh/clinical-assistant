"""
Dosing Calculator UI Components
Tách UI rendering khỏi business logic
"""

from .patient_inputs import render_patient_inputs, get_patient_data
from .dosage_display import render_dosage_results, render_renal_adjustment_table
from .warnings_display import render_warnings_section
from .calculator_layout import (
    render_header, 
    render_weight_metrics, 
    render_renal_metrics, 
    render_antibiotic_selection,
    check_imported_values
)

__all__ = [
    'render_patient_inputs',
    'get_patient_data',
    'render_dosage_results',
    'render_renal_adjustment_table',
    'render_warnings_section',
    'render_header',
    'render_weight_metrics',
    'render_renal_metrics',
    'render_antibiotic_selection',
    'check_imported_values',
]

