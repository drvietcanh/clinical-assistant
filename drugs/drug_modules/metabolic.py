"""
Metabolic and Endocrine Medications
Active module - contains all metabolic and endocrine drug data
"""

# Import from split modules
from .metabolic import METABOLIC_DRUGS

__all__ = ['METABOLIC_DRUGS']

# DEPRECATED: This file is kept for backward compatibility
# New code should import from drugs.drug_modules.metabolic directly
