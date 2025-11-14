"""DDx Knowledge Base - Data
Differential diagnosis data for common clinical scenarios

NOTE: This file contains only data dictionaries.
Functions are in ddx_data.py"""

# SYMPTOM_ALIASES

SYMPTOM_ALIASES = {'chest_pain': ['chest_pain', 'cp', 'chest discomfort'],
    'chest_pain_retrosternal': ['retrosternal', 'substernal',
    'central chest'], 'chest_pain_crushing': ['crushing', 'pressure',
    'squeezing'], 'chest_pain_pleuritic': ['pleuritic', 'worse breathing',
    'worse inspiration'], 'chest_pain_tearing': ['tearing', 'ripping'],
    'radiation_left_arm': ['radiation', 'radiates', 'left arm'],
    'diaphoresis': ['sweating', 'sweaty', 'diaphoresis'], 'dyspnea': [
    'shortness of breath', 'sob', 'dyspnea', 'difficulty breathing'],
    'acute_onset': ['acute', 'sudden', 'abrupt'], 'fever': ['fever',
    'febrile', 'temperature'], 'cough': ['cough', 'coughing'],
    'productive_cough': ['productive cough', 'sputum', 'phlegm'],
    'seizure': ['seizure', 'convulsion', 'fit', 'epilepsy'],
    'palpitations': ['palpitations', 'heart_racing', 'irregular_heartbeat', 'skipped_beats'],
    'jaundice': ['jaundice', 'yellow_skin', 'yellow_eyes', 'icterus'],
    'lymphadenopathy': ['lymphadenopathy', 'swollen_lymph_nodes', 'enlarged_lymph_nodes'],
    'acute_limb_weakness': ['limb_weakness', 'arm_weakness', 'leg_weakness', 'paralysis', 'hemiparesis'],
    'weight_loss': ['weight_loss', 'unintentional_weight_loss', 'wasting'],
    'dizziness': ['dizziness', 'lightheadedness', 'unsteady'],
    'vertigo': ['vertigo', 'spinning', 'room_spinning'],
    'constipation': ['constipation', 'difficulty_passing_stool', 'infrequent_bowel_movements'],
    'urinary_retention': ['urinary_retention', 'cannot_urinate', 'bladder_outlet_obstruction']}

__all__ = ['SYMPTOM_ALIASES']
