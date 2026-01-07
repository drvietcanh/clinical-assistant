"""
Antibiotic Stewardship Package
Các module về quản lý kháng sinh: de-escalation, IV to PO, renal dosing, treatment duration, principles
"""

try:
    from .de_escalation import (
        get_de_escalation_guidelines,
        render_de_escalation_view
    )
    from .iv_to_po import (
        get_iv_to_po_criteria,
        get_iv_to_po_drugs,
        render_iv_to_po_view
    )
    from .renal_dosing import (
        get_renal_dosing_summary,
        render_renal_dosing_view
    )
    from .treatment_duration import (
        get_treatment_duration_recommendations,
        render_treatment_duration_view
    )
    from .principles import (
        get_stewardship_principles,
        render_principles_view
    )
    
    __all__ = [
        'get_de_escalation_guidelines',
        'render_de_escalation_view',
        'get_iv_to_po_criteria',
        'get_iv_to_po_drugs',
        'render_iv_to_po_view',
        'get_renal_dosing_summary',
        'render_renal_dosing_view',
        'get_treatment_duration_recommendations',
        'render_treatment_duration_view',
        'get_stewardship_principles',
        'render_principles_view',
    ]
except ImportError as e:
    # Handle import errors gracefully
    __all__ = []
