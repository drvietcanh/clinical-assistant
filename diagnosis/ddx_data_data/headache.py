"""DDx Knowledge Base - Data
Differential diagnosis data for common clinical scenarios

NOTE: This file contains only data dictionaries.
Functions are in ddx_data.py"""

# Headache Differential Diagnosis

HEADACHE_DDX = {'Subarachnoid Hemorrhage': {'symptoms': {'required': ['headache',
    'acute_severe_headache'], 'supporting': ['thunderclap_headache',
    'worst_headache_life', 'neck_stiffness', 'photophobia',
    'nausea_vomiting', 'decreased_consciousness'], 'contradictory': [
    'chronic_gradual_onset', 'tension_type']}, 'demographics': {'age_risk':
    {'<40': 0.4, '40-70': 0.7, '>70': 0.6}, 'sex_risk': {'male': 1.0,
    'female': 1.3}}, 'risk_factors': ['hypertension', 'smoking',
    'cocaine_use', 'family_history_aneurysm', 'polycystic_kidney'],
    'specificity': 0.75, 'urgency': 'emergency', 'rule_out_first': True,
    'workup': {'immediate': ['CT_head', 'LP_if_CT_negative', 'ECG', 'BP'],
    'within_6h': ['Angiography'], 'optional': ['MRI']}, 'management_hints':
    'URGENT! If thunderclap headache → Rule out SAH immediately. Even if CT negative, do LP. Neurosurgery consult if positive.'
    }, 'Meningitis': {'symptoms': {'required': ['headache', 'fever'],
    'supporting': ['neck_stiffness', 'photophobia', 'nausea_vomiting',
    'altered_mental_status', 'rash', 'decreased_consciousness'],
    'contradictory': ['chronic_gradual_onset', 'no_fever',
    'no_neck_stiffness']}, 'demographics': {'age_risk': {'<10': 0.7,
    '10-50': 0.6, '>50': 0.8}, 'sex_risk': {'male': 1.1, 'female': 1.0}},
    'risk_factors': ['immunocompromised', 'elderly', 'young_children',
    'recent_URI', 'bacterial_exposure'], 'specificity': 0.7, 'urgency':
    'emergency', 'rule_out_first': True, 'workup': {'immediate': ['LP',
    'Blood_cultures', 'CT_head_before_LP', 'CBC_chemistries'], 'within_6h':
    ['Antibiotics_immediately'], 'optional': ['CSF_cultures']},
    'management_hints':
    "URGENT! If fever + headache + neck stiffness → Think MENINGITIS. Don't delay antibiotics for CT/LP. Treat empirically."
    }, 'Brain Tumor': {'symptoms': {'required': ['headache'], 'supporting':
    ['new_onset_progressive', 'worse_morning', 'worse_coughing',
    'focal_neurologic_deficit', 'seizures', 'cognitive_changes',
    'papilledema'], 'contradictory': ['acute_thunderclap', 'paroxysmal',
    'chronic_benign']}, 'demographics': {'age_risk': {'<20': 0.4, '20-60': 
    0.6, '>60': 0.8}, 'sex_risk': {'male': 1.0, 'female': 1.0}},
    'risk_factors': ['age', 'radiation_exposure', 'family_history_cancer',
    'immunodeficiency'], 'specificity': 0.65, 'urgency': 'emergency',
    'rule_out_first': True, 'workup': {'immediate': ['CT_head',
    'Neurologic_exam'], 'within_6h': ['MRI_with_contrast'], 'optional': [
    'EEG']}, 'management_hints':
    'If new progressive headache + neurologic symptoms → Image immediately. Neurosurgery consult if mass found.'
    }, 'Migraine': {'symptoms': {'required': ['headache'], 'supporting': [
    'unilateral', 'throbbing_pulsating', 'photophobia', 'phonophobia',
    'nausea', 'aura', 'worse_with_activity', 'family_history_migraine'],
    'contradictory': ['new_worst_headache', 'fever', 'neck_stiffness',
    'focal_deficit']}, 'demographics': {'age_risk': {'<20': 0.3, '20-50': 
    0.7, '>50': 0.4}, 'sex_risk': {'male': 1.0, 'female': 3.0}},
    'risk_factors': ['female', 'family_history', 'hormonal_changes',
    'stress', 'certain_foods'], 'specificity': 0.8, 'urgency': 'non_urgent',
    'rule_out_first': False, 'workup': {'immediate': ['Clinical_diagnosis'],
    'within_6h': [], 'optional': ['CT_if_atypical']}, 'management_hints':
    'Triptans for acute. Prophylaxis if frequent. R/O SAH if first episode or atypical. Usually no imaging needed.'
    }, 'Tension Headache': {'symptoms': {'required': ['headache'],
    'supporting': ['bilateral', 'tightness_pressure', 'chronic_or_episodic',
    'worse_stress', 'no_nausea', 'mild_moderate'], 'contradictory': [
    'acute_thunderclap', 'aura', 'photophobia_phonophobia', 'worse_morning'
    ]}, 'demographics': {'age_risk': {'<20': 0.5, '20-60': 0.7, '>60': 0.5},
    'sex_risk': {'male': 1.0, 'female': 1.5}}, 'risk_factors': ['stress',
    'poor_posture', 'sleep_deprivation'], 'specificity': 0.85, 'urgency':
    'non_urgent', 'rule_out_first': False, 'workup': {'immediate': [
    'Clinical_diagnosis'], 'within_6h': [], 'optional': []},
    'management_hints':
    'Conservative: NSAIDs, rest, stress management. Usually benign. R/O serious causes if new or changing pattern.'
    }, 'Cluster Headache': {'symptoms': {'required': ['headache'],
    'supporting': ['strictly_unilateral', 'orbital_temporal',
    'severe_excruciating', 'autonomic_symptoms', 'ipsilateral_tearing',
    'rhinorrhea', 'frequent_brief_attacks'], 'contradictory': ['bilateral',
    'chronic_daily', 'mild_moderate']}, 'demographics': {'age_risk': {'<20':
    0.3, '20-60': 0.8, '>60': 0.4}, 'sex_risk': {'male': 3.0, 'female': 1.0
    }}, 'risk_factors': ['male', 'smoking', 'alcohol'], 'specificity': 0.75,
    'urgency': 'non_urgent', 'rule_out_first': False, 'workup': {
    'immediate': ['Clinical_diagnosis'], 'within_6h': [], 'optional': [
    'CT_if_atypical']}, 'management_hints':
    'O2 or triptans for acute. Verapamil for prophylaxis. Very severe but usually no serious pathology.'
    }}

__all__ = ['HEADACHE_DDX']
