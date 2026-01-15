"""Gastrointestinal Drugs
Active module - contains all gastrointestinal drug data"""

# Import all drug categories
from .antacids import ANTACIDS_DRUGS
from .antidiarrheals import ANTIDIARRHEALS_DRUGS
from .h2_receptor_antagonists import H2_RECEPTOR_ANTAGONISTS_DRUGS
from .mucosal_protectants import MUCOSAL_PROTECTANTS_DRUGS
from .proton_pump_inhibitors import PROTON_PUMP_INHIBITORS_DRUGS
from .proton_pump_inhibitor_ppis import PROTON_PUMP_INHIBITOR_PPIS_DRUGS
# ppis.py đã được hợp nhất vào proton_pump_inhibitors.py
from .prokinetic_antiemetics import PROKINETIC_ANTIEMETICS_DRUGS
from .antiemetic_5_ht3_antagonists import ANTIEMETIC_5_HT3_ANTAGONISTS_DRUGS
from .pcab import PCAB_DRUGS
from .jak_inhibitors import JAK_INHIBITORS_DRUGS
from .ibd_5asa import IBD_5ASA_DRUGS
from .laxatives import LAXATIVES_DRUGS
from .antispasmodics import ANTISPASMODICS_DRUGS
from .antiflatulents import ANTIFLATULENTS_DRUGS
from .ibs_drugs import IBS_DRUGS
from .digestive_enzymes import DIGESTIVE_ENZYMES_DRUGS
from .other_gi_drugs import OTHER_GI_DRUGS
from .fixed_dose_combinations import GASTROINTESTINAL_FIXED_DOSE_COMBINATIONS

# Merge all categories
GASTROINTESTINAL_DRUGS = {
    **ANTACIDS_DRUGS,
    **ANTIDIARRHEALS_DRUGS,
    **H2_RECEPTOR_ANTAGONISTS_DRUGS,
    **MUCOSAL_PROTECTANTS_DRUGS,
    **PROTON_PUMP_INHIBITORS_DRUGS,
    **PROTON_PUMP_INHIBITOR_PPIS_DRUGS,
    # PPIS_DRUGS đã được hợp nhất vào PROTON_PUMP_INHIBITORS_DRUGS
    **PROKINETIC_ANTIEMETICS_DRUGS,
    **ANTIEMETIC_5_HT3_ANTAGONISTS_DRUGS,
    **PCAB_DRUGS,
    **JAK_INHIBITORS_DRUGS,
    **LAXATIVES_DRUGS,
    **ANTISPASMODICS_DRUGS,
    **ANTIFLATULENTS_DRUGS,
    **IBD_5ASA_DRUGS,
    **IBS_DRUGS,
    **DIGESTIVE_ENZYMES_DRUGS,
    **OTHER_GI_DRUGS,
    **GASTROINTESTINAL_FIXED_DOSE_COMBINATIONS,
}

__all__ = ["GASTROINTESTINAL_DRUGS"]
