"""
Drug Formulary Module
Insurance coverage and formulary information (BHYT)
"""

from typing import Dict, Optional, List
from enum import Enum
from dataclasses import dataclass


class FormularyStatus(Enum):
    """Formulary status"""
    COVERED = "covered"  # Covered by insurance
    PARTIAL = "partial"  # Partially covered
    NOT_COVERED = "not_covered"  # Not covered
    PRIOR_AUTH = "prior_auth"  # Requires prior authorization
    GENERIC_ONLY = "generic_only"  # Only generic covered


@dataclass
class FormularyInfo:
    """Formulary information for a drug"""
    status: FormularyStatus
    coverage_percentage: Optional[float] = None  # 0-100
    requires_prior_auth: bool = False
    generic_available: bool = False
    alternative_drugs: List[str] = None
    notes: Optional[str] = None
    last_updated: Optional[str] = None


# Formulary data structure
# Format: {drug_name: FormularyInfo}
FORMULARY_DATA = {
    # Example structure - to be populated with actual data
    # "Paracetamol": FormularyInfo(
    #     status=FormularyStatus.COVERED,
    #     coverage_percentage=100,
    #     generic_available=True
    # )
}


def get_formulary_info(drug_name: str) -> Optional[FormularyInfo]:
    """
    Get formulary information for a drug
    
    Args:
        drug_name: Drug name
    
    Returns:
        FormularyInfo or None
    """
    return FORMULARY_DATA.get(drug_name)


def get_formulary_status_badge(status: FormularyStatus) -> str:
    """
    Get HTML badge for formulary status
    
    Args:
        status: Formulary status
    
    Returns:
        HTML badge string
    """
    colors = {
        FormularyStatus.COVERED: "#4caf50",
        FormularyStatus.PARTIAL: "#ff9800",
        FormularyStatus.NOT_COVERED: "#f44336",
        FormularyStatus.PRIOR_AUTH: "#2196f3",
        FormularyStatus.GENERIC_ONLY: "#9c27b0",
    }
    
    labels = {
        FormularyStatus.COVERED: "BHYT chi trả",
        FormularyStatus.PARTIAL: "BHYT chi trả một phần",
        FormularyStatus.NOT_COVERED: "Không BHYT",
        FormularyStatus.PRIOR_AUTH: "Cần xác nhận",
        FormularyStatus.GENERIC_ONLY: "Chỉ generic",
    }
    
    color = colors.get(status, "#757575")
    label = labels.get(status, "Không xác định")
    
    return f'<span style="background: {color}; color: white; padding: 4px 8px; border-radius: 4px; font-size: 0.75rem; font-weight: 600;">{label}</span>'


__all__ = [
    'FormularyStatus',
    'FormularyInfo',
    'FORMULARY_DATA',
    'get_formulary_info',
    'get_formulary_status_badge',
]

