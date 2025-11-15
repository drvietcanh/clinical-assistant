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
from .rrt import render_rrt_calculator

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
    'VENTILATOR_ADVANCED_AVAILABLE',
]

