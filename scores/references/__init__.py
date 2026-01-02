"""
References Configuration for All Calculators
Contains PubMed links, guidelines, and evidence grading for each calculator
"""

from typing import List, Dict, Any
from components.references import (
    GRADE_HIGH, GRADE_MODERATE, GRADE_LOW,
    EVIDENCE_LEVEL_I, EVIDENCE_LEVEL_IIA, EVIDENCE_LEVEL_IIB,
    STRENGTH_STRONG, STRENGTH_MODERATE
)

# References database organized by calculator name
CALCULATOR_REFERENCES: Dict[str, List[Dict[str, Any]]] = {
from .cardiology import CARDIOLOGY_REFERENCES
from .emergency import EMERGENCY_REFERENCES
from .gastrointestinal import GASTROINTESTINAL_REFERENCES
from .hematology import HEMATOLOGY_REFERENCES
from .infectious import INFECTIOUS_REFERENCES
from .neurological import NEUROLOGICAL_REFERENCES
from .other import OTHER_REFERENCES
from .renal import RENAL_REFERENCES
from .respiratory import RESPIRATORY_REFERENCES

# Combine all calculator references
CALCULATOR_REFERENCES: Dict[str, List[Dict[str, Any]]] = {
    **CARDIOLOGY_REFERENCES,
    **EMERGENCY_REFERENCES,
    **GASTROINTESTINAL_REFERENCES,
    **HEMATOLOGY_REFERENCES,
    **INFECTIOUS_REFERENCES,
    **NEUROLOGICAL_REFERENCES,
    **OTHER_REFERENCES,
    **RENAL_REFERENCES,
    **RESPIRATORY_REFERENCES,
}

_UNUSED_REFERENCE_KEYS = [
    "4Ts Score", "ACR Criteria", "AKIN", "APGAR", "ARDS Berlin", "ASA",
    "ASCVD Risk", "BODE Index", "Barthel Index",
    "Bishop Score", "Braden", "Burn TBSA", "CDAI", "CIPN Grading", "Caprini",
    "Centor", "Corrected QT", "DAS28", "DIC Score",
    "DLQI", "DN4", "Duke", "ECOG", "Epworth", "FLACC", "FeverPAIN",
    "GRACE Score", "Gout Diagnostic", "HEART Score",
    "Intraocular Pressure", "KDIGO", "Karnofsky", "Killip", "MASCC",
    "Mallampati", "Modified Bishop", "Morse", "NIPS", "NRS",
    "P-POSSUM", "PASI", "PELOD-2", "PIM2", "PRISM III", "Padua",
    "Palliative Performance", "Parkland Formula", "Pediatric GCS",
    "Pediatric SOFA", "Pitt Bacteremia", "Preeclampsia", "RCRI", "RIFLE",
    "Ranson", "Rockall Score", "SCORAD", "SDAI", "SIRS", "SLEDAI", "SLICC",
    "SMART-COP", "STOP-BANG", "TIMI Risk", "VAS", "Wells DVT",
    "Westley Croup", "Wong-Baker", "mRS"
]

# Keep a backup dictionary for future use or reactivation
UNUSED_CALCULATOR_REFERENCES: Dict[str, List[Dict[str, Any]]] = {
    key: CALCULATOR_REFERENCES[key]
    for key in _UNUSED_REFERENCE_KEYS
    if key in CALCULATOR_REFERENCES
}

# Remove unused entries from active reference map
for key in list(UNUSED_CALCULATOR_REFERENCES.keys()):
    CALCULATOR_REFERENCES.pop(key, None)


def get_references(calculator_name: str) -> List[Dict[str, Any]]:
    """
    Get references for a specific calculator
    
    Args:
        calculator_name: Name of the calculator (e.g., "CHA2DS2-VASc", "Wells PE")
    
    Returns:
        List of reference dictionaries, empty list if not found
    """
    return CALCULATOR_REFERENCES.get(calculator_name, [])


def has_references(calculator_name: str) -> bool:
    """
    Check if a calculator has references
    
    Args:
        calculator_name: Name of the calculator
    
    Returns:
        True if references exist, False otherwise
    """
    return calculator_name in CALCULATOR_REFERENCES and len(CALCULATOR_REFERENCES[calculator_name]) > 0

