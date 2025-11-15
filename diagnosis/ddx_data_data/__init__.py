"""DDx Knowledge Base - Data
Differential diagnosis data for common clinical scenarios

NOTE: This file contains only data dictionaries.
Functions are in ddx_data.py"""

# Import all DDX scenarios
from .abdominal_pain import ABDOMINAL_PAIN_DDX
from .altered_mental_status import ALTERED_MENTAL_STATUS_DDX
from .anemia import ANEMIA_DDX
from .back_pain import BACK_PAIN_DDX
from .bleeding import BLEEDING_DDX
from .chest_pain import CHEST_PAIN_DDX
from .cough import COUGH_DDX
from .diarrhea import DIARRHEA_DDX
from .drug_reaction import DRUG_REACTION_DDX
from .dyspnea import DYSPNEA_DDX
from .electrolyte_disorders import ELECTROLYTE_DISORDERS_DDX
from .fatigue import FATIGUE_DDX
from .fever import FEVER_DDX
from .headache import HEADACHE_DDX
from .htn_emergency import HTN_EMERGENCY_DDX
from .joint_pain import JOINT_PAIN_DDX
from .kidney_injury import KIDNEY_INJURY_DDX
from .pediatric_joint_pain import PEDIATRIC_JOINT_PAIN_DDX
from .rash import RASH_DDX
from .syncope import SYNCOPE_DDX
from .vision_changes import VISION_CHANGES_DDX
from .vomiting import VOMITING_DDX
from .seizure import SEIZURE_DDX
from .palpitations import PALPITATIONS_DDX
from .jaundice import JAUNDICE_DDX
from .lymphadenopathy import LYMPHADENOPATHY_DDX
from .acute_limb_weakness import ACUTE_LIMB_WEAKNESS_DDX
from .weight_loss import WEIGHT_LOSS_DDX
from .dizziness_vertigo import DIZZINESS_VERTIGO_DDX
from .constipation import CONSTIPATION_DDX
from .urinary_retention import URINARY_RETENTION_DDX
from .hearing_loss import HEARING_LOSS_DDX
from .tremor import TREMOR_DDX
from .swelling import SWELLING_DDX
from .night_sweats import NIGHT_SWEATS_DDX
from .memory_loss import MEMORY_LOSS_DDX
from .nausea import NAUSEA_DDX
from .insomnia import INSOMNIA_DDX
from .all_scenarios import ALL_SCENARIOS
from .symptom_aliases import SYMPTOM_ALIASES

# Export all
__all__ = [
    'ABDOMINAL_PAIN_DDX',
    'ALL_SCENARIOS',
    'ALTERED_MENTAL_STATUS_DDX',
    'ANEMIA_DDX',
    'BACK_PAIN_DDX',
    'BLEEDING_DDX',
    'CHEST_PAIN_DDX',
    'COUGH_DDX',
    'DIARRHEA_DDX',
    'DRUG_REACTION_DDX',
    'DYSPNEA_DDX',
    'ELECTROLYTE_DISORDERS_DDX',
    'FATIGUE_DDX',
    'FEVER_DDX',
    'HEADACHE_DDX',
    'HTN_EMERGENCY_DDX',
    'JOINT_PAIN_DDX',
    'KIDNEY_INJURY_DDX',
    'PEDIATRIC_JOINT_PAIN_DDX',
    'RASH_DDX',
    'SYMPTOM_ALIASES',
    'SYNCOPE_DDX',
    'VISION_CHANGES_DDX',
    'VOMITING_DDX',
    'SEIZURE_DDX',
    'PALPITATIONS_DDX',
    'JAUNDICE_DDX',
    'LYMPHADENOPATHY_DDX',
    'ACUTE_LIMB_WEAKNESS_DDX',
    'WEIGHT_LOSS_DDX',
    'DIZZINESS_VERTIGO_DDX',
    'CONSTIPATION_DDX',
    'URINARY_RETENTION_DDX',
    'HEARING_LOSS_DDX',
    'TREMOR_DDX',
    'SWELLING_DDX',
    'NIGHT_SWEATS_DDX',
    'MEMORY_LOSS_DDX',
    'NAUSEA_DDX',
    'INSOMNIA_DDX',
]
