"""DDx Knowledge Base - Data
Differential diagnosis data for common clinical scenarios

NOTE: This file contains only data dictionaries.
Functions are in ddx_data.py"""

# Fatigue Differential Diagnosis

FATIGUE_DDX = {'Anemia': {'symptoms': {'required': ['fatigue'], 'supporting': ['pale',
    'dyspnea', 'dizziness', 'tachycardia', 'weakness', 'pica'],
    'contradictory': ['normal_Hb', 'no_pale']}, 'demographics': {'age_risk':
    {'<40': 0.4, '40-70': 0.6, '>70': 0.7}, 'sex_risk': {'male': 0.8,
    'female': 1.2}}, 'risk_factors': ['bleeding', 'nutritional_deficiency',
    'chronic_disease', 'malignancy'], 'specificity': 0.75, 'urgency':
    'urgent', 'rule_out_first': True, 'workup': {'immediate': ['CBC',
    'Iron_studies', 'B12_Folate', 'Reticulocyte'], 'within_6h': [],
    'optional': ['Bone_marrow_biopsy']}, 'management_hints':
    'Treat underlying cause. Iron if iron deficiency. B12/folate if deficiency. Transfuse if severe (Hgb <7 or symptomatic).'
    }, 'Hypothyroidism': {'symptoms': {'required': ['fatigue'],
    'supporting': ['weight_gain', 'cold_intolerance', 'constipation',
    'depression', 'dry_skin', 'hair_loss', 'bradycardia'], 'contradictory':
    ['weight_loss', 'tachycardia', 'heat_intolerance']}, 'demographics': {
    'age_risk': {'<40': 0.4, '40-70': 0.7, '>70': 0.6}, 'sex_risk': {'male':
    0.3, 'female': 1.0}}, 'risk_factors': ['autoimmune',
    'iodine_deficiency', 'post_thyroidectomy', 'medications'],
    'specificity': 0.8, 'urgency': 'non_urgent', 'rule_out_first': False,
    'workup': {'immediate': ['TSH', 'Free_T4'], 'within_6h': [], 'optional':
    ['TPO_antibodies', 'Thyroid_US']}, 'management_hints':
    'Levothyroxine replacement. Start low dose (25-50mcg) if elderly or cardiac disease. Monitor TSH every 6-8 weeks until stable.'
    }, 'Depression': {'symptoms': {'required': ['fatigue'], 'supporting': [
    'low_mood', 'anhedonia', 'sleep_disturbance', 'appetite_change',
    'concentration_problems', 'guilt', 'suicidal_ideation'],
    'contradictory': ['normal_mood', 'no_psychiatric_symptoms']},
    'demographics': {'age_risk': {'<40': 0.5, '40-70': 0.6, '>70': 0.5},
    'sex_risk': {'male': 0.7, 'female': 1.0}}, 'risk_factors': ['stress',
    'trauma', 'family_history', 'chronic_disease', 'medications'],
    'specificity': 0.7, 'urgency': 'urgent', 'rule_out_first': False,
    'workup': {'immediate': ['PHQ9', 'Clinical_assessment'], 'within_6h': [
    ], 'optional': ['Psychiatry_referral']}, 'management_hints':
    'SSRI (sertraline, escitalopram). Psychotherapy. If suicidal → Psychiatry consult immediately. Monitor for improvement.'
    }, 'Congestive Heart Failure': {'symptoms': {'required': ['fatigue'],
    'supporting': ['dyspnea', 'edema', 'orthopnea', 'PND',
    'exercise_intolerance', 'jugular_venous_distension'], 'contradictory':
    ['no_dyspnea', 'no_edema']}, 'demographics': {'age_risk': {'<40': 0.2,
    '40-70': 0.6, '>70': 0.8}, 'sex_risk': {'male': 1.0, 'female': 1.0}},
    'risk_factors': ['hypertension', 'CAD', 'diabetes', 'valvular_disease'],
    'specificity': 0.75, 'urgency': 'urgent', 'rule_out_first': True,
    'workup': {'immediate': ['BNP_NT_proBNP', 'Echo', 'CXR', 'ECG'],
    'within_6h': [], 'optional': ['Cardiac_MRI']}, 'management_hints':
    'Diuretics. ACE-I/ARB. Beta-blockers. Treat underlying cause. If severe → Hospital admission.'
    }, 'COPD': {'symptoms': {'required': ['fatigue'], 'supporting': [
    'dyspnea', 'chronic_cough', 'smoking_history', 'exercise_intolerance',
    'wheeze'], 'contradictory': ['no_smoking', 'no_dyspnea']},
    'demographics': {'age_risk': {'<40': 0.2, '40-70': 0.7, '>70': 0.8},
    'sex_risk': {'male': 1.3, 'female': 1.0}}, 'risk_factors': ['smoking',
    'age', 'occupational_exposure'], 'specificity': 0.7, 'urgency':
    'non_urgent', 'rule_out_first': False, 'workup': {'immediate': [
    'Spirometry', 'CXR'], 'within_6h': [], 'optional': ['CT_chest']},
    'management_hints':
    'Bronchodilators. Smoking cessation. Pulmonary rehab. O2 if hypoxemic. Long-term: ICS + LABA.'
    }, 'Chronic Kidney Disease': {'symptoms': {'required': ['fatigue'],
    'supporting': ['edema', 'nausea', 'anemia', 'hypertension',
    'decreased_urine_output'], 'contradictory': ['normal_creatinine',
    'no_edema']}, 'demographics': {'age_risk': {'<40': 0.3, '40-70': 0.6,
    '>70': 0.7}, 'sex_risk': {'male': 1.0, 'female': 1.0}}, 'risk_factors':
    ['diabetes', 'hypertension', 'glomerulonephritis', 'polycystic_kidney'],
    'specificity': 0.7, 'urgency': 'urgent', 'rule_out_first': True,
    'workup': {'immediate': ['Creatinine', 'eGFR', 'Urinalysis',
    'Electrolytes'], 'within_6h': [], 'optional': ['Renal_US', 'Biopsy']},
    'management_hints':
    'Treat underlying cause. Control BP. Manage complications (anemia, bone disease). If advanced → Nephrology consult, prepare for dialysis.'
    }, 'Malignancy': {'symptoms': {'required': ['fatigue'], 'supporting': [
    'weight_loss', 'fever', 'night_sweats', 'lymphadenopathy',
    'organomegaly', 'bleeding'], 'contradictory': ['no_weight_loss',
    'stable_weight']}, 'demographics': {'age_risk': {'<40': 0.2, '40-70': 
    0.5, '>70': 0.6}, 'sex_risk': {'male': 1.0, 'female': 1.0}},
    'risk_factors': ['age', 'smoking', 'family_history', 'exposures'],
    'specificity': 0.6, 'urgency': 'urgent', 'rule_out_first': True,
    'workup': {'immediate': ['CBC', 'CMP', 'CXR', 'CT_chest_abdomen_pelvis'
    ], 'within_6h': [], 'optional': ['Biopsy', 'PET_scan']},
    'management_hints':
    'URGENT workup if red flags (weight loss, night sweats, lymphadenopathy). Oncology consult. Staging if confirmed.'
    }}

__all__ = ['FATIGUE_DDX']
