"""
UI Component Library
Reusable UI components for consistent design across the app
"""

from .cards import (
    render_module_card,
    render_calculator_card,
    render_info_card,
)
from .alerts import (
    render_info_alert,
    render_success_alert,
    render_warning_alert,
    render_error_alert,
)
from .inputs import (
    render_number_input_with_unit,
    render_select_with_icon,
    render_multi_select,
)
from .results import (
    render_result_box,
    render_result_card,
    render_metric_display,
)
from .scoring import (
    get_risk_color,
    render_score_result,
    render_score_breakdown,
    render_quick_reference_table,
)

__all__ = [
    # Cards
    'render_module_card',
    'render_calculator_card',
    'render_info_card',
    # Alerts
    'render_info_alert',
    'render_success_alert',
    'render_warning_alert',
    'render_error_alert',
    # Inputs
    'render_number_input_with_unit',
    'render_select_with_icon',
    'render_multi_select',
    # Results
    'render_result_box',
    'render_result_card',
    'render_metric_display',
    # Scoring
    'get_risk_color',
    'render_score_result',
    'render_score_breakdown',
    'render_quick_reference_table',
]

