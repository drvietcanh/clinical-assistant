"""
Oncology Drugs Package
All cancer treatment medications organized by drug class
"""

# Import basic oncology only for now (other modules may have different variable names)
from .basic_oncology import ONCOLOGY_DRUGS

# Export all oncology drugs
__all__ = ['ONCOLOGY_DRUGS']
