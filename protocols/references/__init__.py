"""
Protocol References
Combines all protocol references from category-specific files
"""
from typing import List, Dict, Any
from components.references import (
    GRADE_HIGH, GRADE_MODERATE, GRADE_LOW,
    EVIDENCE_LEVEL_I, EVIDENCE_LEVEL_IIA, EVIDENCE_LEVEL_IIB,
    STRENGTH_STRONG, STRENGTH_MODERATE
)

from .cardiovascular import CARDIOVASCULAR_REFERENCES
from .critical_care import CRITICAL_CARE_REFERENCES
from .emergency import EMERGENCY_REFERENCES
from .gastrointestinal import GASTROINTESTINAL_REFERENCES
from .infectious import INFECTIOUS_REFERENCES
from .metabolic_endocrine import METABOLIC_ENDOCRINE_REFERENCES
from .neurological import NEUROLOGICAL_REFERENCES
from .other import OTHER_REFERENCES
from .renal import RENAL_REFERENCES
from .respiratory import RESPIRATORY_REFERENCES

# Combine all protocol references
PROTOCOL_REFERENCES: Dict[str, List[Dict[str, Any]]] = {
    **CARDIOVASCULAR_REFERENCES,
    **CRITICAL_CARE_REFERENCES,
    **EMERGENCY_REFERENCES,
    **GASTROINTESTINAL_REFERENCES,
    **INFECTIOUS_REFERENCES,
    **METABOLIC_ENDOCRINE_REFERENCES,
    **NEUROLOGICAL_REFERENCES,
    **OTHER_REFERENCES,
    **RENAL_REFERENCES,
    **RESPIRATORY_REFERENCES,
}

def get_references(protocol_name: str) -> List[Dict[str, Any]]:
    """
    Get references for a specific protocol
    
    Args:
        protocol_name: Name of the protocol (e.g., "Sepsis", "ACS", "Stroke")
    
    Returns:
        List of reference dictionaries, empty list if not found
    """
    return PROTOCOL_REFERENCES.get(protocol_name, [])


def has_references(protocol_name: str) -> bool:
    """
    Check if a protocol has references
    
    Args:
        protocol_name: Name of the protocol
    
    Returns:
        True if references exist, False otherwise
    """
    return protocol_name in PROTOCOL_REFERENCES and len(PROTOCOL_REFERENCES[protocol_name]) > 0

