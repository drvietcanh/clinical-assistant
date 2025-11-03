"""
Differential Diagnosis Generator Module
Clinical decision support tool for generating ranked differential diagnoses
"""

from .ddx_generator import generate_ddx, render_ddx_interface
from .ddx_data import (
    get_scenario_data,
    get_all_scenarios,
    get_symptom_matches
)

__all__ = [
    'generate_ddx',
    'render_ddx_interface',
    'get_scenario_data',
    'get_all_scenarios',
    'get_symptom_matches',
]

