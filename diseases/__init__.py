"""
Disease Encyclopedia Module
Comprehensive database of diseases and conditions
"""

from diseases.data import (
    DISEASES_DATABASE,
    get_all_diseases,
    get_diseases_by_category,
    get_category_list
)

from diseases.search import (
    search_diseases,
    get_disease_info,
    get_diseases_by_symptom
)

__all__ = [
    'DISEASES_DATABASE',
    'get_all_diseases',
    'get_diseases_by_category',
    'get_category_list',
    'search_diseases',
    'get_disease_info',
    'get_diseases_by_symptom',
]

