"""DDx Knowledge Base - Data
Differential diagnosis data for common clinical scenarios

NOTE: This file contains only data dictionaries.
Functions are in ddx_data.py"""

# Back Pain Differential Diagnosis

BACK_PAIN_DDX = {'Mechanical Back Pain': {'symptoms': {'required': ['back_pain'],
    'supporting': ['worse_with_movement', 'better_with_rest',
    'muscle_spasm', 'no_red_flags', 'gradual_onset'], 'contradictory': [
    'red_flags', 'neurologic_deficit', 'fever']}, 'demographics': {
    'age_risk': {'<40': 0.6, '40-70': 0.7, '>70': 0.6}, 'sex_risk': {'male':
    1.0, 'female': 1.0}}, 'risk_factors': ['heavy_lifting', 'sedentary',
    'obesity', 'poor_posture'], 'specificity': 0.75, 'urgency':
    'non_urgent', 'rule_out_first': False, 'workup': {'immediate': [
    'Clinical_exam'], 'within_6h': [], 'optional': ['X_ray',
    'MRI_if_persistent']}, 'management_hints':
    'NSAIDs. Physical therapy. Activity modification. Usually resolves in 4-6 weeks. If persists >6 weeks → Imaging.'
    }, 'Disc Herniation': {'symptoms': {'required': ['back_pain'],
    'supporting': ['radiating_pain', 'sciatica', 'leg_pain', 'numbness',
    'weakness', 'worse_with_sitting'], 'contradictory': ['no_radiating',
    'no_neurologic']}, 'demographics': {'age_risk': {'<40': 0.6, '40-70': 
    0.7, '>70': 0.4}, 'sex_risk': {'male': 1.2, 'female': 1.0}},
    'risk_factors': ['heavy_lifting', 'repetitive_stress', 'age'],
    'specificity': 0.75, 'urgency': 'urgent', 'rule_out_first': True,
    'workup': {'immediate': ['Neurologic_exam', 'Straight_leg_raise'],
    'within_6h': ['MRI_spine'], 'optional': ['EMG']}, 'management_hints':
    'NSAIDs. Physical therapy. If cauda equina or severe weakness → Urgent surgery. Most improve with conservative treatment.'
    }, 'Spinal Stenosis': {'symptoms': {'required': ['back_pain'],
    'supporting': ['neurogenic_claudication', 'worse_with_walking',
    'better_with_sitting', 'bilateral_symptoms', 'elderly'],
    'contradictory': ['young_age', 'unilateral_only']}, 'demographics': {
    'age_risk': {'<40': 0.1, '40-70': 0.5, '>70': 0.8}, 'sex_risk': {'male':
    1.0, 'female': 1.0}}, 'risk_factors': ['age', 'degenerative_changes',
    'congenital'], 'specificity': 0.8, 'urgency': 'non_urgent',
    'rule_out_first': False, 'workup': {'immediate': ['Clinical_exam'],
    'within_6h': [], 'optional': ['MRI_spine', 'CT_spine']},
    'management_hints':
    'NSAIDs. Physical therapy. Epidural injections. If severe → Surgery (decompression).'
    }, 'Cauda Equina Syndrome': {'symptoms': {'required': ['back_pain'],
    'supporting': ['saddle_anesthesia', 'bowel_bladder_dysfunction',
    'bilateral_leg_weakness', 'severe_pain'], 'contradictory': [
    'no_neurologic', 'unilateral_only']}, 'demographics': {'age_risk': {
    '<40': 0.4, '40-70': 0.6, '>70': 0.5}, 'sex_risk': {'male': 1.0,
    'female': 1.0}}, 'risk_factors': ['disc_herniation', 'tumor', 'trauma'],
    'specificity': 0.85, 'urgency': 'emergency', 'rule_out_first': True,
    'workup': {'immediate': ['Urgent_MRI', 'Neurologic_exam', 'Rectal_exam'
    ], 'within_6h': ['Surgical_consult'], 'optional': []},
    'management_hints':
    'URGENT! Surgical emergency. Decompression within 24-48h. Delay → Permanent deficits. Immediate neurosurgery consult.'
    }, 'Spinal Infection': {'symptoms': {'required': ['back_pain'],
    'supporting': ['fever', 'night_sweats', 'weight_loss',
    'localized_tenderness', 'recent_infection', 'IVDU'], 'contradictory': [
    'no_fever', 'no_red_flags']}, 'demographics': {'age_risk': {'<40': 0.4,
    '40-70': 0.6, '>70': 0.7}, 'sex_risk': {'male': 1.2, 'female': 1.0}},
    'risk_factors': ['IVDU', 'immunocompromised', 'diabetes',
    'recent_surgery'], 'specificity': 0.75, 'urgency': 'emergency',
    'rule_out_first': True, 'workup': {'immediate': ['MRI_spine',
    'Blood_cultures', 'ESR_CRP', 'CBC'], 'within_6h': ['CT_guided_biopsy'],
    'optional': []}, 'management_hints':
    'URGENT! IV antibiotics (empiric: Vancomycin + Ceftriaxone). Surgical debridement if abscess. 6-12 weeks antibiotics.'
    }, 'Malignancy (Spinal)': {'symptoms': {'required': ['back_pain'],
    'supporting': ['night_pain', 'weight_loss', 'fever', 'history_cancer',
    'worse_at_rest', 'constitutional_symptoms'], 'contradictory': [
    'no_red_flags', 'mechanical_pattern']}, 'demographics': {'age_risk': {
    '<40': 0.2, '40-70': 0.5, '>70': 0.7}, 'sex_risk': {'male': 1.0,
    'female': 1.0}}, 'risk_factors': ['history_cancer', 'age', 'smoking'],
    'specificity': 0.7, 'urgency': 'emergency', 'rule_out_first': True,
    'workup': {'immediate': ['MRI_spine', 'CT_chest_abdomen_pelvis', 'CBC',
    'ESR'], 'within_6h': ['Biopsy'], 'optional': ['PET_scan']},
    'management_hints':
    'URGENT workup. Oncology consult. If cord compression → Urgent radiation/surgery. Treat underlying malignancy.'
    }}

__all__ = ['BACK_PAIN_DDX']
