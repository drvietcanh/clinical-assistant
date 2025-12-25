"""Respiratory Medications
Active module - contains all respiratory drug data"""

# Import all drug categories
from .leukotriene_receptor_antagonists import LEUKOTRIENE_RECEPTOR_ANTAGONISTS_DRUGS
from .short_acting_beta_2_agonists import SHORT_ACTING_BETA_2_AGONISTS_DRUGS
from .long_acting_beta_2_agonist_labas import LONG_ACTING_BETA_2_AGONIST_LABAS_DRUGS
from .anticholinergic_short_actings import ANTICHOLINERGIC_SHORT_ACTINGS_DRUGS
from .anticholinergic_long_actings import ANTICHOLINERGIC_LONG_ACTINGS_DRUGS
from .inhaled_corticosteroid_icss import INHALED_CORTICOSTEROID_ICSS_DRUGS
from .methylxanthines import METHYLXANTHINES_DRUGS
from .respiratory_biologics import RESPIRATORY_BIOLOGICS_DRUGS
from .pde4_inhibitors import PDE4_INHIBITORS_DRUGS
from .combination_inhalers import COMBINATION_INHALERS_DRUGS

# Merge all categories
RESPIRATORY_DRUGS = {
    **LEUKOTRIENE_RECEPTOR_ANTAGONISTS_DRUGS,
    **SHORT_ACTING_BETA_2_AGONISTS_DRUGS,
    **LONG_ACTING_BETA_2_AGONIST_LABAS_DRUGS,
    **ANTICHOLINERGIC_SHORT_ACTINGS_DRUGS,
    **ANTICHOLINERGIC_LONG_ACTINGS_DRUGS,
    **INHALED_CORTICOSTEROID_ICSS_DRUGS,
    **METHYLXANTHINES_DRUGS,
    **RESPIRATORY_BIOLOGICS_DRUGS,
    **PDE4_INHIBITORS_DRUGS,
    **COMBINATION_INHALERS_DRUGS,
}

__all__ = ['RESPIRATORY_DRUGS']
