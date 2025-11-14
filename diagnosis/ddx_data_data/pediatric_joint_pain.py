"""DDx Knowledge Base - Data
Differential diagnosis data for common clinical scenarios

NOTE: This file contains only data dictionaries.
Functions are in ddx_data.py"""

# Pediatric Joint Pain Differential Diagnosis

PEDIATRIC_JOINT_PAIN_DDX = {'Juvenile Idiopathic Arthritis (JIA)': {'symptoms': {'required': [
    'joint_pain'], 'supporting': ['morning_stiffness', 'swelling',
    'multiple_joints', 'chronic', 'fever', 'rash', 'uveitis'],
    'contradictory': ['acute_severe', 'single_joint', 'septic_appearance']},
    'demographics': {'age_risk': {'<16': 1.0, '16-18': 0.8, '>18': 0.0},
    'sex_risk': {'male': 0.7, 'female': 1.0}}, 'risk_factors': [
    'family_history', 'HLA_B27'], 'specificity': 0.75, 'urgency': 'urgent',
    'rule_out_first': False, 'workup': {'immediate': ['CBC', 'ESR_CRP',
    'RF_ANA', 'X_ray_joints'], 'within_6h': [], 'optional': ['HLA_B27',
    'Ophthalmology_screening']}, 'management_hints':
    'NSAIDs. DMARDs (methotrexate). Biologics if severe. Ophthalmology screening (uveitis risk). Rheumatology consult.'
    }, 'Septic Arthritis': {'symptoms': {'required': ['joint_pain'],
    'supporting': ['fever', 'single_joint', 'severe_pain', 'erythema',
    'swelling', 'decreased_range_of_motion', 'toxic_appearance'],
    'contradictory': ['no_fever', 'multiple_joints', 'chronic']},
    'demographics': {'age_risk': {'<5': 0.8, '5-10': 0.6, '>10': 0.4},
    'sex_risk': {'male': 1.2, 'female': 1.0}}, 'risk_factors': [
    'recent_infection', 'immunocompromised', 'sickle_cell'], 'specificity':
    0.85, 'urgency': 'emergency', 'rule_out_first': True, 'workup': {
    'immediate': ['Joint_aspiration', 'Synovial_fluid_analysis',
    'Blood_cultures', 'CBC', 'ESR_CRP'], 'within_6h': ['X_ray',
    'Orthopedic_consult'], 'optional': []}, 'management_hints':
    'URGENT! IV antibiotics (empiric: Vancomycin + Ceftriaxone). Surgical drainage if needed. Delay → Joint destruction.'
    }, 'Reactive Arthritis': {'symptoms': {'required': ['joint_pain'],
    'supporting': ['recent_infection', 'GI_URI_symptoms', 'asymmetric',
    'lower_extremities', 'enthesitis', 'urethritis', 'conjunctivitis'],
    'contradictory': ['no_recent_infection', 'symmetric']}, 'demographics':
    {'age_risk': {'<10': 0.4, '10-18': 0.7, '>18': 0.5}, 'sex_risk': {
    'male': 1.2, 'female': 1.0}}, 'risk_factors': ['recent_infection',
    'HLA_B27'], 'specificity': 0.7, 'urgency': 'urgent', 'rule_out_first': 
    False, 'workup': {'immediate': ['CBC', 'ESR_CRP', 'Stool_culture',
    'Urethral_culture', 'HLA_B27'], 'within_6h': [], 'optional': []},
    'management_hints':
    'NSAIDs. Treat underlying infection. Usually self-limited. If persistent → DMARDs. Rheumatology consult.'
    }, 'Growing Pains': {'symptoms': {'required': ['joint_pain'],
    'supporting': ['bilateral', 'lower_extremities', 'evening_night',
    'no_swelling', 'no_limitation', 'intermittent', 'young_age'],
    'contradictory': ['swelling', 'morning_stiffness', 'fever',
    'single_joint']}, 'demographics': {'age_risk': {'<5': 0.6, '5-10': 0.8,
    '>10': 0.3}, 'sex_risk': {'male': 1.0, 'female': 1.0}}, 'risk_factors':
    ['young_age', 'active_child'], 'specificity': 0.75, 'urgency':
    'non_urgent', 'rule_out_first': False, 'workup': {'immediate': [
    'Clinical_diagnosis'], 'within_6h': [], 'optional': []},
    'management_hints':
    'Reassurance. Massage. Stretching. Usually resolves with age. If atypical features → Further workup.'
    }, 'Osteomyelitis': {'symptoms': {'required': ['joint_pain'],
    'supporting': ['fever', 'localized_pain', 'swelling', 'erythema',
    'decreased_motion', 'recent_trauma', 'toxic_appearance'],
    'contradictory': ['no_fever', 'multiple_sites', 'chronic_mild']},
    'demographics': {'age_risk': {'<5': 0.7, '5-10': 0.6, '>10': 0.4},
    'sex_risk': {'male': 1.2, 'female': 1.0}}, 'risk_factors': [
    'recent_trauma', 'sickle_cell', 'immunocompromised'], 'specificity': 
    0.75, 'urgency': 'emergency', 'rule_out_first': True, 'workup': {
    'immediate': ['X_ray', 'MRI', 'Blood_cultures', 'CBC', 'ESR_CRP'],
    'within_6h': ['Bone_aspiration', 'Orthopedic_consult'], 'optional': []},
    'management_hints':
    'URGENT! IV antibiotics (Vancomycin + Ceftriaxone). Surgical debridement if abscess. 4-6 weeks antibiotics.'
    }}

__all__ = ['PEDIATRIC_JOINT_PAIN_DDX']
