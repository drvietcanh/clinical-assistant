"""
Disease Search Functions
Search and retrieve disease information
"""

from typing import List, Optional
from diseases.data import DISEASES_DATABASE, Disease, get_diseases_by_category


def search_diseases(query: str, category: Optional[str] = None) -> List[Disease]:
    """
    Search diseases by name (English or Vietnamese)
    
    Args:
        query: Search query
        category: Optional category filter
        
    Returns:
        List of matching Disease objects
    """
    if not query:
        return []
    
    query_lower = query.lower().strip()
    
    # Get diseases to search
    diseases_to_search = get_diseases_by_category(category) if category else DISEASES_DATABASE
    
    results = []
    for disease in diseases_to_search:
        # Search in name (English and Vietnamese)
        if (query_lower in disease.name.lower() or 
            query_lower in disease.name_vn.lower() or
            query_lower in disease.definition.lower()):
            results.append(disease)
    
    return results


def get_disease_info(disease_id: str) -> Optional[Disease]:
    """
    Get detailed information about a disease
    
    Args:
        disease_id: Disease ID
        
    Returns:
        Disease object or None
    """
    for disease in DISEASES_DATABASE:
        if disease.id == disease_id:
            return disease
    return None


def get_diseases_by_symptom(symptom: str) -> List[Disease]:
    """
    Get diseases that have a specific symptom
    
    Args:
        symptom: Symptom to search for
        
    Returns:
        List of diseases with that symptom
    """
    if not symptom:
        return []
    
    symptom_lower = symptom.lower().strip()
    results = []
    
    for disease in DISEASES_DATABASE:
        # Check if symptom is in disease symptoms list
        for s in disease.symptoms:
            if symptom_lower in s.lower():
                results.append(disease)
                break
    
    return results

