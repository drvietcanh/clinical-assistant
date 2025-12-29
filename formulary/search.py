"""
Formulary Search Functions
Search and retrieve formulary drug information
"""

from typing import List, Optional
from formulary.data import (
    FORMULARY_DATABASE,
    get_drugs_by_category,
    get_drugs_by_insurance_type,
    FormularyDrug
)


def search_formulary(query: str, category: Optional[str] = None, insurance_type: Optional[str] = None) -> List[FormularyDrug]:
    """
    Search formulary drugs
    
    Args:
        query: Search query (drug name)
        category: Optional category filter
        insurance_type: Optional insurance type filter
        
    Returns:
        List of matching FormularyDrug objects
    """
    if not query:
        return []
    
    query_lower = query.lower().strip()
    
    # Get drugs to search
    drugs_to_search = FORMULARY_DATABASE
    if category:
        drugs_to_search = get_drugs_by_category(category)
    if insurance_type:
        drugs_to_search = [d for d in drugs_to_search if insurance_type in d.insurance_coverage]
    
    results = []
    for drug in drugs_to_search:
        # Search in drug name, generic name, and brand names
        if (query_lower in drug.drug_name.lower() or
            query_lower in drug.generic_name.lower() or
            any(query_lower in brand.lower() for brand in drug.brand_names)):
            results.append(drug)
    
    return results


def get_drug_formulary_info(drug_name: str) -> Optional[FormularyDrug]:
    """
    Get formulary information for a specific drug
    
    Args:
        drug_name: Drug name
        
    Returns:
        FormularyDrug object or None
    """
    drug_name_lower = drug_name.lower().strip()
    
    for drug in FORMULARY_DATABASE:
        if (drug_name_lower == drug.drug_name.lower() or
            drug_name_lower == drug.generic_name.lower() or
            any(drug_name_lower == brand.lower() for brand in drug.brand_names)):
            return drug
    
    return None


def check_drug_coverage(drug_name: str, insurance_type: str = "BHYT") -> Optional[dict]:
    """
    Check if a drug is covered by insurance
    
    Args:
        drug_name: Drug name
        insurance_type: Insurance type (BHYT, Private, etc.)
        
    Returns:
        Dictionary with coverage information or None
    """
    drug = get_drug_formulary_info(drug_name)
    if not drug:
        return None
    
    is_covered = insurance_type in drug.insurance_coverage
    
    return {
        "drug_name": drug.drug_name,
        "generic_name": drug.generic_name,
        "is_covered": is_covered,
        "coverage_type": drug.coverage_type if is_covered else "Not covered",
        "insurance_type": drug.insurance_coverage,
        "generic_available": drug.generic_available,
        "price_range": drug.price_range,
        "notes": drug.notes,
        "alternatives": drug.alternatives
    }


def get_generic_alternatives(brand_name: str) -> List[FormularyDrug]:
    """
    Get generic alternatives for a brand name drug
    
    Args:
        brand_name: Brand name drug
        
    Returns:
        List of generic alternatives
    """
    # Find the drug
    drug = get_drug_formulary_info(brand_name)
    if not drug or not drug.generic_available:
        return []
    
    # Return generic version
    return [drug] if drug.generic_available else []

