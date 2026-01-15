"""
Critical Care Module
Fluid therapy, vasopressors, transfusion, sedation, scoring systems, ventilator, ARDS, sepsis, shock, and RRT protocols
"""

from .fluids import render_fluid_calculator
from .vasopressors import render_vasopressor_guide
from .transfusion import render_transfusion_calculator
from .sedation import render_sedation_calculator
from .scoring import render_scoring_calculator
from .dashboard import render_critical_care_dashboard
from .ventilator import render_ventilator_calculator
from .ards import render_ards_protocols
from .sepsis import render_sepsis_protocols
from .shock import render_shock_management
from .rrt import (
    render_rrt_calculator,
    calculate_crrt_dosing,
    calculate_ihd_dosing,
    calculate_sled_dosing,
    calculate_anticoagulation_rrt
)
from .scenarios import render_scenarios_calculator
from .dirc import render_dirc_calculator, DIRCCalculator
from .patient_dashboard import render_patient_dashboard
from .clinical_alerts import render_clinical_alerts, render_alerts_summary
from .emergency import render_emergency_protocols
from .quick_reference import render_quick_reference
from .hemodynamics import render_hemodynamics
from .fluid_balance import render_fluid_balance
from .drug_compatibility import render_drug_compatibility
from .vietnamese_protocols import render_vietnamese_protocols
from .dashboard_mobile import render_mobile_dashboard
from .dashboard_builder import render_dashboard_builder
from .multi_patient_view import render_multi_patient_view
from .analytics import render_analytics_dashboard

# Import comprehensive ventilator calculator from ventilator module
try:
    from ventilator import render_comprehensive_calculator, render_ardsnet, render_initial_settings, render_peep_fio2_table
    from ventilator.weaning import render_weaning_calculator as render_weaning_calculator_advanced
    VENTILATOR_ADVANCED_AVAILABLE = True
except ImportError:
    VENTILATOR_ADVANCED_AVAILABLE = False
    render_comprehensive_calculator = None
    render_ardsnet = None
    render_initial_settings = None
    render_peep_fio2_table = None
    render_weaning_calculator_advanced = None

__all__ = [
    'render_fluid_calculator',
    'render_vasopressor_guide',
    'render_transfusion_calculator',
    'render_sedation_calculator',
    'render_scoring_calculator',
    'render_critical_care_dashboard',
    'render_ventilator_calculator',
    'render_ards_protocols',
    'render_sepsis_protocols',
    'render_shock_management',
    'render_rrt_calculator',
    'calculate_crrt_dosing',
    'calculate_ihd_dosing',
    'calculate_sled_dosing',
    'calculate_anticoagulation_rrt',
    'render_scenarios_calculator',
    'render_dirc_calculator',
    'DIRCCalculator',
    'render_patient_dashboard',
    'render_clinical_alerts',
    'render_alerts_summary',
    'render_emergency_protocols',
    'render_quick_reference',
    'render_hemodynamics',
    'render_fluid_balance',
    'render_drug_compatibility',
    'render_vietnamese_protocols',
    'render_mobile_dashboard',
    'render_dashboard_builder',
    'render_multi_patient_view',
    'render_analytics_dashboard',
    'VENTILATOR_ADVANCED_AVAILABLE',
]

