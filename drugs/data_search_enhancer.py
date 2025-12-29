"""
Data Search Enhancer - Cải thiện tìm kiếm dữ liệu thuốc
Tìm kiếm thông minh, gợi ý, fuzzy matching
"""

from typing import Dict, List, Tuple, Optional
from collections import defaultdict
import re
from difflib import SequenceMatcher
from .drug_database import DRUG_DATABASE
from .enhanced_fields_overrides import EXTRA_ENHANCED_FIELDS

# ============================================================================
# FUZZY SEARCH - Tìm kiếm mờ
# ============================================================================

def similarity(a: str, b: str) -> float:
    """Tính độ tương đồng giữa 2 chuỗi (0-1)"""
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()

def fuzzy_search_drugs(query: str, threshold: float = 0.6, limit: int = 10) -> List[Tuple[str, float, Dict]]:
    """
    Tìm kiếm mờ thuốc theo tên
    
    Args:
        query: Từ khóa tìm kiếm
        threshold: Ngưỡng tương đồng (0-1)
        limit: Số kết quả tối đa
    
    Returns:
        List of (drug_name, similarity_score, drug_data)
    """
    query_lower = query.lower()
    results = []
    
    for drug_name, drug_data in DRUG_DATABASE.items():
        # Check exact match first
        if query_lower in drug_name.lower():
            results.append((drug_name, 1.0, drug_data))
            continue
        
        # Check Vietnamese name
        vn_name = drug_data.get("vietnamese_name", "")
        if query_lower in vn_name.lower():
            results.append((drug_name, 0.9, drug_data))
            continue
        
        # Calculate similarity
        name_sim = similarity(query, drug_name)
        vn_sim = similarity(query, vn_name) if vn_name else 0
        
        max_sim = max(name_sim, vn_sim)
        
        if max_sim >= threshold:
            results.append((drug_name, max_sim, drug_data))
    
    # Sort by similarity
    results.sort(key=lambda x: x[1], reverse=True)
    return results[:limit]

# ============================================================================
# ADVANCED SEARCH - Tìm kiếm nâng cao
# ============================================================================

def search_by_multiple_criteria(
    name: Optional[str] = None,
    group: Optional[str] = None,
    indication: Optional[str] = None,
    administration: Optional[str] = None,
    module: Optional[str] = None,
) -> List[Tuple[str, Dict]]:
    """
    Tìm kiếm theo nhiều tiêu chí
    
    Returns:
        List of (drug_name, drug_data)
    """
    results = []
    
    for drug_name, drug_data in DRUG_DATABASE.items():
        # Apply overrides
        if drug_name in EXTRA_ENHANCED_FIELDS:
            drug_data = {**drug_data, **EXTRA_ENHANCED_FIELDS[drug_name]}
        
        match = True
        
        # Filter by name
        if name:
            name_lower = name.lower()
            if name_lower not in drug_name.lower() and name_lower not in drug_data.get("vietnamese_name", "").lower():
                match = False
        
        # Filter by group
        if match and group:
            drug_group = drug_data.get("group", "").lower()
            if group.lower() not in drug_group:
                match = False
        
        # Filter by indication
        if match and indication:
            indications = drug_data.get("indications", [])
            if not any(indication.lower() in ind.lower() for ind in indications):
                match = False
        
        # Filter by administration
        if match and administration:
            admin_list = drug_data.get("administration", [])
            if administration.upper() not in [a.upper() for a in admin_list]:
                match = False
        
        if match:
            results.append((drug_name, drug_data))
    
    return results

def search_by_field_content(
    field_name: str,
    query: str,
    exact_match: bool = False
) -> List[Tuple[str, str, str]]:
    """
    Tìm kiếm trong nội dung của một field cụ thể
    
    Returns:
        List of (drug_name, field_name, matched_content)
    """
    results = []
    query_lower = query.lower()
    
    for drug_name, drug_data in DRUG_DATABASE.items():
        # Apply overrides
        if drug_name in EXTRA_ENHANCED_FIELDS:
            drug_data = {**drug_data, **EXTRA_ENHANCED_FIELDS[drug_name]}
        
        if field_name not in drug_data:
            continue
        
        value = drug_data[field_name]
        
        # Search in value
        if isinstance(value, str):
            if exact_match:
                if query_lower == value.lower():
                    results.append((drug_name, field_name, value))
            else:
                if query_lower in value.lower():
                    results.append((drug_name, field_name, value))
        
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, str):
                    if exact_match:
                        if query_lower == item.lower():
                            results.append((drug_name, field_name, item))
                    else:
                        if query_lower in item.lower():
                            results.append((drug_name, field_name, item))
        
        elif isinstance(value, dict):
            # Recursive search in dict
            for k, v in value.items():
                if isinstance(v, str):
                    if query_lower in v.lower():
                        results.append((drug_name, f"{field_name}.{k}", v))
                elif isinstance(v, list):
                    for item in v:
                        if isinstance(item, str) and query_lower in item.lower():
                            results.append((drug_name, f"{field_name}.{k}", item))
    
    return results

# ============================================================================
# SEARCH SUGGESTIONS - Gợi ý tìm kiếm
# ============================================================================

def get_search_suggestions(query: str, limit: int = 5) -> List[str]:
    """
    Gợi ý từ khóa tìm kiếm dựa trên query
    
    Returns:
        List of suggested search terms
    """
    query_lower = query.lower()
    suggestions = set()
    
    # Find similar drug names
    for drug_name in DRUG_DATABASE.keys():
        if similarity(query, drug_name) > 0.7:
            suggestions.add(drug_name)
        if len(suggestions) >= limit:
            break
    
    # Find similar Vietnamese names
    for drug_data in DRUG_DATABASE.values():
        vn_name = drug_data.get("vietnamese_name", "")
        if vn_name and similarity(query, vn_name) > 0.7:
            suggestions.add(vn_name)
        if len(suggestions) >= limit * 2:
            break
    
    return list(suggestions)[:limit]

def suggest_corrections(query: str) -> List[str]:
    """
    Gợi ý sửa lỗi chính tả
    
    Returns:
        List of corrected terms
    """
    # Common typos mapping
    typo_map = {
        "metformim": "metformin",
        "amoxicilin": "amoxicillin",
        "paracetamol": "paracetamol",
        "ibuprofen": "ibuprofen",
    }
    
    query_lower = query.lower()
    if query_lower in typo_map:
        return [typo_map[query_lower]]
    
    # Find similar names
    suggestions = []
    for drug_name in DRUG_DATABASE.keys():
        if similarity(query, drug_name) > 0.8:
            suggestions.append(drug_name)
    
    return suggestions[:3]

# ============================================================================
# SEARCH ANALYTICS - Phân tích tìm kiếm
# ============================================================================

def analyze_search_patterns(queries: List[str]) -> Dict:
    """
    Phân tích patterns tìm kiếm
    
    Args:
        queries: List các query đã tìm kiếm
    
    Returns:
        Dict với thống kê
    """
    patterns = {
        "common_terms": defaultdict(int),
        "failed_searches": [],
        "successful_searches": [],
    }
    
    for query in queries:
        # Find matches
        results = fuzzy_search_drugs(query, threshold=0.5)
        
        if results:
            patterns["successful_searches"].append(query)
            # Extract common terms
            words = query.lower().split()
            for word in words:
                if len(word) > 2:  # Ignore short words
                    patterns["common_terms"][word] += 1
        else:
            patterns["failed_searches"].append(query)
    
    return patterns

