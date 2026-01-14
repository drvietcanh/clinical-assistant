"""
Antibiotics Module - Dosing and TDM Tools
Modular structure for easy maintenance
"""

from .crcl import render as render_crcl
from .vancomycin import render as render_vancomycin
from .aminoglycoside import render as render_aminoglycoside
from .database import render_antibiotic_lookup, render_database
from .dosing_calculator import render_dosing_calculator
from .multi_dosing_comparison import render_multi_comparison

# Phase 1: New features
try:
    from .allergy_checker import render_allergy_checker
    from .spectrum_charts import render_spectrum_charts, render_spectrum_chart_inline
    ALLERGY_CHECKER_AVAILABLE = True
    SPECTRUM_CHARTS_AVAILABLE = True
except ImportError:
    ALLERGY_CHECKER_AVAILABLE = False
    SPECTRUM_CHARTS_AVAILABLE = False
    render_allergy_checker = None
    render_spectrum_charts = None
    render_spectrum_chart_inline = None

# Phase 2: Advanced features
try:
    from .pkpd_calculators import render_pkpd_calculator
    from .cost_comparison import render_cost_comparison
    PKPD_AVAILABLE = True
    COST_COMPARISON_AVAILABLE = True
except ImportError:
    PKPD_AVAILABLE = False
    COST_COMPARISON_AVAILABLE = False
    render_pkpd_calculator = None
    render_cost_comparison = None

# Phase 4: Integration features
try:
    from .formulary import render_formulary_checker, get_formulary_status
    from .analytics import render_analytics, log_usage, get_usage_stats
    FORMULARY_AVAILABLE = True
    ANALYTICS_AVAILABLE = True
except ImportError:
    FORMULARY_AVAILABLE = False
    ANALYTICS_AVAILABLE = False
    render_formulary_checker = None
    get_formulary_status = None
    render_analytics = None
    log_usage = None
    get_usage_stats = None

__all__ = [
    'render_crcl',
    'render_vancomycin',
    'render_aminoglycoside',
    'render_antibiotic_lookup',
    'render_database',
    'render_dosing_calculator',
    'render_multi_comparison',
    'render_allergy_checker',
    'render_spectrum_charts',
    'render_spectrum_chart_inline',
    'render_pkpd_calculator',
    'render_cost_comparison',
    'render_formulary_checker',
    'get_formulary_status',
    'render_analytics',
    'log_usage',
    'get_usage_stats',
]

