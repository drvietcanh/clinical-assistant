"""
Ventilator Module - Mechanical Ventilation Tools
Modular structure for easy maintenance
"""

from .calculators import render_ardsnet, render_initial_settings
from .tables import render_peep_fio2_table
from .comprehensive_calculator import render_comprehensive_calculator
from .abg_integration import (
    render_abg_panel,
    calculate_pf_ratio,
    classify_ards,
    display_abg_summary
)
from .abg_advisor import (
    analyze_abg_for_ventilator,
    recommend_ventilator_adjustments,
    display_abg_recommendations,
    display_ventilator_adjustments
)
from .alerts import check_ventilator_alerts, display_alerts
from .protocols import display_protocol_recommendations
from .compliance import (
    calculate_static_compliance,
    calculate_dynamic_compliance,
    display_compliance_analysis
)
from .auto_peep import (
    estimate_auto_peep,
    display_auto_peep_analysis
)
from .weaning import (
    calculate_rsbi,
    interpret_rsbi,
    assess_weaning_readiness,
    render_weaning_calculator
)

__all__ = [
    'render_ardsnet',
    'render_initial_settings',
    'render_peep_fio2_table',
    'render_comprehensive_calculator',
    'render_abg_panel',
    'calculate_pf_ratio',
    'classify_ards',
    'display_abg_summary',
    'analyze_abg_for_ventilator',
    'recommend_ventilator_adjustments',
    'display_abg_recommendations',
    'display_ventilator_adjustments',
    'check_ventilator_alerts',
    'display_alerts',
    'display_protocol_recommendations',
    'calculate_static_compliance',
    'calculate_dynamic_compliance',
    'display_compliance_analysis',
    'estimate_auto_peep',
    'display_auto_peep_analysis',
    'calculate_rsbi',
    'interpret_rsbi',
    'assess_weaning_readiness',
    'render_weaning_calculator',
]

