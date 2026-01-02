"""
Natural Language Processing for Search
Basic NLP utilities for improving search queries
"""

import re
from typing import List, Dict, Tuple, Optional


def normalize_query(query: str) -> str:
    """
    Normalize search query
    
    Args:
        query: Raw search query
    
    Returns:
        Normalized query
    """
    if not query:
        return ""
    
    # Lowercase
    query = query.lower().strip()
    
    # Remove extra whitespace
    query = re.sub(r'\s+', ' ', query)
    
    # Remove special characters except Vietnamese characters
    query = re.sub(r'[^\w\sàáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđ]', '', query)
    
    return query


def extract_keywords(query: str) -> List[str]:
    """
    Extract keywords from query
    
    Args:
        query: Search query
    
    Returns:
        List of keywords
    """
    normalized = normalize_query(query)
    # Split by whitespace and filter out stop words
    stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'của', 'và', 'hoặc', 'trong', 'với'}
    keywords = [word for word in normalized.split() if word not in stop_words and len(word) > 1]
    return keywords


def expand_medical_terms(query: str) -> List[str]:
    """
    Expand medical terms with synonyms
    
    Args:
        query: Search query
    
    Returns:
        List of expanded terms including synonyms
    """
    # Medical term synonyms mapping
    synonyms = {
        'thuốc': ['drug', 'medication', 'medicine'],
        'kháng sinh': ['antibiotic', 'antibiotics', 'antimicrobial'],
        'tính liều': ['dosing', 'dose calculation', 'dosage'],
        'tương tác': ['interaction', 'drug interaction'],
        'chống chỉ định': ['contraindication', 'contraindications'],
        'tác dụng phụ': ['side effect', 'adverse effect'],
        'thang điểm': ['score', 'scoring', 'calculator'],
        'phác đồ': ['protocol', 'guideline', 'treatment protocol'],
        'hồi sức': ['critical care', 'icu', 'intensive care'],
        'thở máy': ['ventilator', 'mechanical ventilation'],
    }
    
    expanded = [query]
    query_lower = query.lower()
    
    for term, syns in synonyms.items():
        if term in query_lower:
            for syn in syns:
                expanded.append(query_lower.replace(term, syn))
        # Also check reverse
        for syn in syns:
            if syn in query_lower:
                expanded.append(query_lower.replace(syn, term))
    
    return list(set(expanded))


def parse_search_intent(query: str) -> Dict[str, any]:
    """
    Parse search intent from query
    
    Args:
        query: Search query
    
    Returns:
        Dict with intent information
    """
    intent = {
        'type': 'general',  # 'drug', 'calculator', 'protocol', 'general'
        'keywords': extract_keywords(query),
        'filters': {},
        'original_query': query
    }
    
    query_lower = query.lower()
    
    # Detect drug search
    drug_indicators = ['thuốc', 'drug', 'medication', 'medicine', 'kháng sinh', 'antibiotic']
    if any(indicator in query_lower for indicator in drug_indicators):
        intent['type'] = 'drug'
    
    # Detect calculator search
    calc_indicators = ['tính', 'calculator', 'score', 'thang điểm', 'tính toán']
    if any(indicator in query_lower for indicator in calc_indicators):
        intent['type'] = 'calculator'
    
    # Detect protocol search
    protocol_indicators = ['phác đồ', 'protocol', 'guideline', 'điều trị']
    if any(indicator in query_lower for indicator in protocol_indicators):
        intent['type'] = 'protocol'
    
    # Extract filters
    if 'theo thận' in query_lower or 'renal' in query_lower:
        intent['filters']['renal'] = True
    
    if 'nhi khoa' in query_lower or 'pediatric' in query_lower:
        intent['filters']['pediatric'] = True
    
    if 'thai kỳ' in query_lower or 'pregnancy' in query_lower:
        intent['filters']['pregnancy'] = True
    
    return intent


def improve_search_query(query: str) -> str:
    """
    Improve search query with NLP
    
    Args:
        query: Original query
    
    Returns:
        Improved query
    """
    # Normalize
    normalized = normalize_query(query)
    
    # Expand medical terms
    expanded = expand_medical_terms(normalized)
    
    # Use the most relevant expansion (for now, return original normalized)
    return normalized


# Export
__all__ = [
    'normalize_query',
    'extract_keywords',
    'expand_medical_terms',
    'parse_search_intent',
    'improve_search_query',
]

