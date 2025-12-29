"""
Drug Formulary Information Module
Information about drugs covered by insurance and formularies
"""

from formulary.data import (
    FORMULARY_DATABASE,
    get_all_formulary_drugs,
    get_drugs_by_category,
    get_drugs_by_insurance_type
)

from formulary.search import (
    search_formulary,
    get_drug_formulary_info,
    check_drug_coverage,
    get_generic_alternatives
)

__all__ = [
    'FORMULARY_DATABASE',
    'get_all_formulary_drugs',
    'get_drugs_by_category',
    'get_drugs_by_insurance_type',
    'search_formulary',
    'get_drug_formulary_info',
    'check_drug_coverage',
    'get_generic_alternatives',
]

