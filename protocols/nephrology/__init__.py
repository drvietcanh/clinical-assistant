"""
Nephrology Protocols
AKI and kidney-related protocols
"""

from .aki import render as render_aki
from .uti_pyelonephritis import render as render_uti_pyelonephritis
from .nephrolithiasis import render as render_nephrolithiasis
from .bph_urinary_retention import render as render_bph_urinary_retention
from .chronic_glomerulonephritis import render as render_chronic_glomerulonephritis
from .nephrotic_syndrome import render as render_nephrotic_syndrome
from .ckd import render as render_ckd
from .diabetic_nephropathy import render as render_diabetic_nephropathy
from .hypertensive_nephrosclerosis import render as render_hypertensive_nephrosclerosis
from .hepatorenal_syndrome import render as render_hepatorenal_syndrome
from .emergency_dialysis import render as render_emergency_dialysis


__all__ = [
    'render_aki',
    'render_uti_pyelonephritis',
    'render_nephrolithiasis',
    'render_bph_urinary_retention',
    'render_chronic_glomerulonephritis',
    'render_nephrotic_syndrome',
    'render_ckd',
    'render_diabetic_nephropathy',
    'render_hypertensive_nephrosclerosis',
    'render_hepatorenal_syndrome',
    'render_emergency_dialysis',
]

