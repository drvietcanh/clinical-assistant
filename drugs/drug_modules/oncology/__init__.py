"""Oncology Medications
Active module - contains all oncology drug data"""

# Import all drug categories
from .alkylating_agents import ALKYLATING_AGENTS_DRUGS
from .anthracyclines import ANTHRACYCLINES_DRUGS
from .antimetabolites import ANTIMETABOLITES_DRUGS
from .platinum_compounds import PLATINUM_COMPOUNDS_DRUGS
from .anti_emetic_5_ht3_antagonists import ANTI_EMETIC_5_HT3_ANTAGONISTS_DRUGS

# Merge all categories
ONCOLOGY_DRUGS = {
    **ALKYLATING_AGENTS_DRUGS,
    **ANTHRACYCLINES_DRUGS,
    **ANTIMETABOLITES_DRUGS,
    **PLATINUM_COMPOUNDS_DRUGS,
    **ANTI_EMETIC_5_HT3_ANTAGONISTS_DRUGS,
}

__all__ = ['ONCOLOGY_DRUGS']
