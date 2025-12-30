"""
Disease Encyclopedia Module
Comprehensive database of diseases and conditions
"""

from diseases.data import (
    DISEASES_DATABASE,
    Disease,
    get_all_diseases,
    get_diseases_by_category,
    get_category_list,
    CATEGORY_MAPPING
)

from diseases.search import (
    search_diseases,
    get_disease_info,
    get_diseases_by_symptom
)

from diseases.management import (
    get_specialty_statistics,
    get_disease_by_id,
    search_diseases_by_keyword,
    get_diseases_by_icd10,
    get_diseases_by_drug,
    get_specialty_summary,
    export_specialty_data
)

__all__ = [
    'DISEASES_DATABASE',
    'Disease',
    'get_all_diseases',
    'get_diseases_by_category',
    'get_category_list',
    'CATEGORY_MAPPING',
    'search_diseases',
    'get_disease_info',
    'get_diseases_by_symptom',
    'get_specialty_statistics',
    'get_disease_by_id',
    'search_diseases_by_keyword',
    'get_diseases_by_icd10',
    'get_diseases_by_drug',
    'get_specialty_summary',
    'export_specialty_data',
]

