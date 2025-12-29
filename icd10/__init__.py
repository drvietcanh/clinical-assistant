"""
ICD-10 Code Lookup Module
International Classification of Diseases, 10th Revision
"""

from icd10.data import (
    ICD10_DATABASE,
    get_all_codes,
    get_codes_by_category,
    get_category_list
)

from icd10.search import (
    search_by_name,
    search_by_code,
    search_by_category,
    get_code_info
)

__all__ = [
    'ICD10_DATABASE',
    'get_all_codes',
    'get_codes_by_category',
    'get_category_list',
    'search_by_name',
    'search_by_code',
    'search_by_category',
    'get_code_info',
]

