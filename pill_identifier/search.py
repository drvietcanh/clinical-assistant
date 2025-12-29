"""
Pill Identifier Search Functions
Search pills by physical characteristics
"""

from typing import List, Optional, Dict
from pill_identifier.data import PILL_DATABASE, Pill


def search_pills_by_attributes(
    color: Optional[str] = None,
    shape: Optional[str] = None,
    imprint: Optional[str] = None,
    size: Optional[str] = None
) -> List[Pill]:
    """
    Search pills by physical attributes
    
    Args:
        color: Pill color
        shape: Pill shape
        imprint: Text/numbers on pill
        size: Pill size
        
    Returns:
        List of matching Pill objects
    """
    results = PILL_DATABASE
    
    # Filter by color
    if color and color != "All":
        results = [p for p in results if p.color.lower() == color.lower()]
    
    # Filter by shape
    if shape and shape != "All":
        results = [p for p in results if p.shape.lower() == shape.lower()]
    
    # Filter by imprint (partial match)
    if imprint:
        imprint_lower = imprint.lower().strip()
        results = [p for p in results if imprint_lower in p.imprint.lower()]
    
    # Filter by size
    if size and size != "All":
        results = [p for p in results if p.size.lower() == size.lower()]
    
    return results


def get_pill_info(drug_name: str) -> Optional[Pill]:
    """
    Get pill information by drug name
    
    Args:
        drug_name: Drug name
        
    Returns:
        Pill object or None
    """
    drug_name_lower = drug_name.lower().strip()
    
    for pill in PILL_DATABASE:
        if (drug_name_lower == pill.drug_name.lower() or
            drug_name_lower == pill.generic_name.lower()):
            return pill
    
    return None

