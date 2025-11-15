"""DDx Knowledge Base - Data
Differential diagnosis data for common clinical scenarios

NOTE: This file contains only data dictionaries.
Functions are in ddx_data.py"""

# Import all DDX scenarios first
from .chest_pain import CHEST_PAIN_DDX
from .dyspnea import DYSPNEA_DDX
from .abdominal_pain import ABDOMINAL_PAIN_DDX
from .altered_mental_status import ALTERED_MENTAL_STATUS_DDX
from .fever import FEVER_DDX
from .syncope import SYNCOPE_DDX
from .joint_pain import JOINT_PAIN_DDX
from .headache import HEADACHE_DDX
from .diarrhea import DIARRHEA_DDX
from .anemia import ANEMIA_DDX
from .kidney_injury import KIDNEY_INJURY_DDX
from .htn_emergency import HTN_EMERGENCY_DDX
from .vomiting import VOMITING_DDX
from .rash import RASH_DDX
from .cough import COUGH_DDX
from .bleeding import BLEEDING_DDX
from .fatigue import FATIGUE_DDX
from .back_pain import BACK_PAIN_DDX
from .vision_changes import VISION_CHANGES_DDX
from .pediatric_joint_pain import PEDIATRIC_JOINT_PAIN_DDX
from .electrolyte_disorders import ELECTROLYTE_DISORDERS_DDX
from .drug_reaction import DRUG_REACTION_DDX
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

# ALL_SCENARIOS

ALL_SCENARIOS = {'Chest Pain': CHEST_PAIN_DDX, 'Dyspnea': DYSPNEA_DDX, 'Abdominal Pain':
    ABDOMINAL_PAIN_DDX, 'Altered Mental Status': ALTERED_MENTAL_STATUS_DDX,
    'Fever': FEVER_DDX, 'Syncope': SYNCOPE_DDX, 'Joint Pain':
    JOINT_PAIN_DDX, 'Headache': HEADACHE_DDX, 'Diarrhea': DIARRHEA_DDX,
    'Anemia': ANEMIA_DDX, 'Kidney Injury': KIDNEY_INJURY_DDX,
    'Hypertension Emergency': HTN_EMERGENCY_DDX, 'Vomiting': VOMITING_DDX,
    'Rash': RASH_DDX, 'Cough': COUGH_DDX, 'Bleeding': BLEEDING_DDX,
    'Fatigue': FATIGUE_DDX, 'Back Pain': BACK_PAIN_DDX, 'Vision Changes':
    VISION_CHANGES_DDX, 'Pediatric Joint Pain': PEDIATRIC_JOINT_PAIN_DDX,
    'Electrolyte Disorders': ELECTROLYTE_DISORDERS_DDX, 'Drug Reaction':
    DRUG_REACTION_DDX, 'Seizure': SEIZURE_DDX, 'Palpitations': PALPITATIONS_DDX,
    'Jaundice': JAUNDICE_DDX, 'Lymphadenopathy': LYMPHADENOPATHY_DDX,
    'Acute Limb Weakness': ACUTE_LIMB_WEAKNESS_DDX, 'Weight Loss': WEIGHT_LOSS_DDX,
    'Dizziness / Vertigo': DIZZINESS_VERTIGO_DDX, 'Constipation': CONSTIPATION_DDX,
    'Urinary Retention': URINARY_RETENTION_DDX, 'Hearing Loss': HEARING_LOSS_DDX,
    'Tremor': TREMOR_DDX, 'Swelling': SWELLING_DDX, 'Night Sweats': NIGHT_SWEATS_DDX,
    'Memory Loss': MEMORY_LOSS_DDX, 'Nausea': NAUSEA_DDX, 'Insomnia': INSOMNIA_DDX}

__all__ = ['ALL_SCENARIOS']
