"""
ICD-10 Search Functions
Search and retrieve ICD-10 codes by various criteria
"""

from typing import List, Optional
from icd10.data import ICD10_DATABASE, ICD10Code, get_codes_by_category


def search_by_name(query: str, category: Optional[str] = None) -> List[ICD10Code]:
    """
    Search ICD-10 codes by disease name (English or Vietnamese)
    
    Args:
        query: Search query (disease name)
        category: Optional category filter
        
    Returns:
        List of matching ICD10Code objects
    """
    if not query:
        return []
    
    query_lower = query.lower().strip()
    results = []
    
    # Get codes to search (all or filtered by category)
    codes_to_search = get_codes_by_category(category) if category else ICD10_DATABASE
    
    for code in codes_to_search:
        # Search in English name
        if query_lower in code.name_en.lower():
            results.append(code)
        # Search in Vietnamese name
        elif query_lower in code.name_vn.lower():
            results.append(code)
        # Search in code itself
        elif query_lower in code.code.lower():
            results.append(code)
    
    return results


def search_by_code(code_query: str) -> Optional[ICD10Code]:
    """
    Search ICD-10 code by exact code match
    
    Args:
        code_query: ICD-10 code (e.g., "I10", "E11.9")
        
    Returns:
        ICD10Code object if found, None otherwise
    """
    if not code_query:
        return None
    
    code_query = code_query.strip().upper()
    
    # Exact match first
    for code in ICD10_DATABASE:
        if code.code == code_query:
            return code
    
    # Partial match (e.g., "I10" matches "I10")
    for code in ICD10_DATABASE:
        if code.code.startswith(code_query) or code_query.startswith(code.code):
            return code
    
    return None


def search_by_category(category: str) -> List[ICD10Code]:
    """
    Get all ICD-10 codes in a specific category
    
    Args:
        category: Category name (e.g., "Cardiology", "Infectious")
        
    Returns:
        List of ICD10Code objects in that category
    """
    return get_codes_by_category(category)


def get_code_info(code: str) -> Optional[dict]:
    """
    Get detailed information about an ICD-10 code
    
    Args:
        code: ICD-10 code
        
    Returns:
        Dictionary with code information, or None if not found
    """
    icd_code = search_by_code(code)
    if not icd_code:
        return None
    
    return {
        "code": icd_code.code,
        "name_en": icd_code.name_en,
        "name_vn": icd_code.name_vn,
        "category": icd_code.category,
        "chapter": icd_code.chapter,
        "block": icd_code.block,
        "notes": icd_code.notes,
    }


def get_all_categories() -> List[str]:
    """Get list of all available categories"""
    from icd10.data import get_category_list
    return get_category_list()

