"""
Respiratory Scoring Systems
All respiratory and pulmonary calculators organized by individual files
"""

from .curb65 import render as render_curb65
from .psi_port import render as render_psi_port
from .wells_pe import render as render_wells_pe
from .smartcop import render as render_smartcop
from .bode import render as render_bode
from .perc import render as render_perc
from .ards_berlin import render as render_ards_berlin
from .pesi import render as render_pesi
from .mmrc import render as render_mmrc
from .act import render as render_act
from .murray_lung_injury import render as render_murray_lung_injury
from .gold import render as render_gold
from .spesi import render as render_spesi
from .hestia import render as render_hestia
from .mulbsta import render as render_mulbsta
from .hacor import render as render_hacor
from utils.errors import CalculatorNotFoundError, safe_render_calculator


def render_respiratory_calculator(calculator_id):
    """
    Route to the correct respiratory calculator based on ID
    
    Args:
        calculator_id: The ID of the calculator to render
    """
    calculators = {
        "CURB-65": render_curb65,
        "PSI/PORT": render_psi_port,
        "SMART-COP": render_smartcop,
        "BODE Index": render_bode,
        "Wells PE": render_wells_pe,
        "PERC": render_perc,
        "ARDS Berlin": render_ards_berlin,
        "PESI": render_pesi,
        "mMRC": render_mmrc,
        "ACT": render_act,
        "Murray Lung Injury": render_murray_lung_injury,
        "GOLD": render_gold,
        "sPESI": render_spesi,
        "Hestia": render_hestia,
        "MuLBSTA Score": render_mulbsta,
        "HACOR Score": render_hacor,
    }
    
    calculator_func = calculators.get(calculator_id)
    if calculator_func:
        safe_render_calculator(calculator_func, calculator_id)
    else:
        raise CalculatorNotFoundError(f"Calculator '{calculator_id}' not found in respiratory module")


__all__ = [
    'render_respiratory_calculator',
    'render_curb65',
    'render_psi_port',
    'render_smartcop',
    'render_bode',
    'render_wells_pe',
    'render_perc',
    'render_ards_berlin',
    'render_pesi',
    'render_mmrc',
    'render_act',
]

