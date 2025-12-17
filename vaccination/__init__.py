"""
Vaccination Module - Comprehensive Vaccine Information
Includes vaccine schedules, prices, and information for Vietnam
"""

from vaccination.vaccine_data import (
    VACCINES_CHILDREN,
    VACCINES_ADULTS,
    VACCINE_SCHEDULES,
    VACCINE_PRICES,
    get_vaccine_by_name,
    get_vaccines_by_category,
    get_schedule_by_age_group
)

from vaccination.render import (
    render_vaccination_home,
    render_vaccine_search,
    render_vaccine_detail,
    render_schedule_viewer,
    render_price_comparison,
    render_general_info
)

__all__ = [
    'VACCINES_CHILDREN',
    'VACCINES_ADULTS',
    'VACCINE_SCHEDULES',
    'VACCINE_PRICES',
    'get_vaccine_by_name',
    'get_vaccines_by_category',
    'get_schedule_by_age_group',
    'render_vaccination_home',
    'render_vaccine_search',
    'render_vaccine_detail',
    'render_schedule_viewer',
    'render_price_comparison',
    'render_general_info',
]

