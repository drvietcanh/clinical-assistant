"""
Drug Database - Lazy Loading Version
Load drug modules only when needed to improve startup performance
"""

from typing import Dict, Any, Optional

# Cache for loaded database
_DRUG_DATABASE_CACHE: Optional[Dict[str, Any]] = None
_DRUG_GROUPS_CACHE: Optional[Dict[str, Any]] = None


def _load_drug_database() -> Dict[str, Any]:
    """Lazy load drug database - only import when first accessed"""
    global _DRUG_DATABASE_CACHE
    
    if _DRUG_DATABASE_CACHE is None:
        # Import only when needed
        from .drug_modules import (
            CARDIOVASCULAR_DRUGS,
            DIABETES_DRUGS,
            GASTROINTESTINAL_DRUGS,
            ANALGESICS_DRUGS,
            RESPIRATORY_DRUGS,
            NEUROLOGICAL_DRUGS,
            HEMATOLOGY_DRUGS,
            SUPPORTIVE_DRUGS,
            ANTIMICROBIAL_DRUGS,
            METABOLIC_DRUGS,
            ONCOLOGY_DRUGS,
            EMERGENCY_DRUGS,
            OTHER_DRUGS,
            UROLOGY_DRUGS,
            CARDIOVASCULAR_OTHER_DRUGS,
            INFECTIOUS_OTHER_DRUGS,
            PSYCHIATRY_OTHER_DRUGS,
            ENDOCRINOLOGY_OTHER_DRUGS,
            MISCELLANEOUS_DRUGS,
        )
        
        # Merge all drug dictionaries
        _DRUG_DATABASE_CACHE = {
            **CARDIOVASCULAR_DRUGS,
            **DIABETES_DRUGS,
            **GASTROINTESTINAL_DRUGS,
            **ANALGESICS_DRUGS,
            **RESPIRATORY_DRUGS,
            **NEUROLOGICAL_DRUGS,
            **HEMATOLOGY_DRUGS,
            **SUPPORTIVE_DRUGS,
            **ANTIMICROBIAL_DRUGS,
            **METABOLIC_DRUGS,
            **ONCOLOGY_DRUGS,
            **EMERGENCY_DRUGS,
            **OTHER_DRUGS,
            **UROLOGY_DRUGS,
            **INFECTIOUS_OTHER_DRUGS,
            **CARDIOVASCULAR_OTHER_DRUGS,
            **PSYCHIATRY_OTHER_DRUGS,
            **ENDOCRINOLOGY_OTHER_DRUGS,
            **MISCELLANEOUS_DRUGS,
        }
    
    return _DRUG_DATABASE_CACHE


def _load_drug_groups() -> Dict[str, Any]:
    """Lazy load drug groups"""
    global _DRUG_GROUPS_CACHE
    
    if _DRUG_GROUPS_CACHE is None:
        from .drug_utils import DRUG_GROUPS
        _DRUG_GROUPS_CACHE = DRUG_GROUPS
    
    return _DRUG_GROUPS_CACHE


class LazyDrugDatabase:
    """Lazy loading wrapper for drug database"""
    
    def __getitem__(self, key: str) -> Any:
        return _load_drug_database()[key]
    
    def __contains__(self, key: str) -> bool:
        return key in _load_drug_database()
    
    def get(self, key: str, default: Any = None) -> Any:
        return _load_drug_database().get(key, default)
    
    def keys(self):
        return _load_drug_database().keys()
    
    def values(self):
        return _load_drug_database().values()
    
    def items(self):
        return _load_drug_database().items()
    
    def __len__(self) -> int:
        return len(_load_drug_database())
    
    def __iter__(self):
        return iter(_load_drug_database())


class LazyDrugGroups:
    """Lazy loading wrapper for drug groups"""
    
    def __getitem__(self, key: str) -> Any:
        return _load_drug_groups()[key]
    
    def __contains__(self, key: str) -> bool:
        return key in _load_drug_groups()
    
    def get(self, key: str, default: Any = None) -> Any:
        return _load_drug_groups().get(key, default)
    
    def keys(self):
        return _load_drug_groups().keys()
    
    def values(self):
        return _load_drug_groups().values()
    
    def items(self):
        return _load_drug_groups().items()
    
    def __len__(self) -> int:
        return len(_load_drug_groups())
    
    def __iter__(self):
        return iter(_load_drug_groups())


# Create lazy instances
DRUG_DATABASE = LazyDrugDatabase()
DRUG_GROUPS = LazyDrugGroups()


def get_total_drugs() -> int:
    """Get total number of drugs (lazy loaded)"""
    return len(DRUG_DATABASE)


# For backward compatibility - provide direct access functions
def get_drug_database() -> Dict[str, Any]:
    """Get drug database (forces load if not already loaded)"""
    return _load_drug_database()


def get_drug_groups() -> Dict[str, Any]:
    """Get drug groups (forces load if not already loaded)"""
    return _load_drug_groups()


__all__ = [
    'DRUG_DATABASE',
    'DRUG_GROUPS',
    'get_total_drugs',
    'get_drug_database',
    'get_drug_groups',
]

