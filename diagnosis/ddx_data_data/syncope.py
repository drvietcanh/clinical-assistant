"""DDx Knowledge Base - Data
Differential diagnosis data for common clinical scenarios

NOTE: This file contains only data dictionaries.
Functions are in ddx_data.py"""

# Syncope Differential Diagnosis

SYNCOPE_DDX = {'Arrhythmia': {'symptoms': {'required': ['syncope', 'sudden'],
    'supporting': ['palpitations', 'chest_pain', 'history_arrhythmia',
    'heart_disease'], 'contradictory': []}, 'demographics': {'age_risk': {
    '<40': 0.4, '40-70': 0.6, '>70': 0.7}, 'sex_risk': {'male': 1.0,
    'female': 1.0}}, 'risk_factors': ['CAD', 'heart_failure',
    'history_arrhythmia', 'structural_heart_disease'], 'specificity': 0.75,
    'urgency': 'emergency', 'rule_out_first': True, 'workup': {'immediate':
    ['ECG', 'Telemetry', 'Echo'], 'within_6h': ['Holter', 'Event_monitor'],
    'optional': ['EP_study']}, 'management_hints':
    'URGENT! Continuous monitoring. If VT/VF → Defibrillation. Consider ICD if recurrent.'
    }, 'Pulmonary Embolism': {'symptoms': {'required': ['syncope'],
    'supporting': ['dyspnea', 'chest_pain', 'tachycardia',
    'unilateral_leg_swelling', 'recent_immobility'], 'contradictory': []},
    'demographics': {'age_risk': {'<40': 0.4, '40-70': 0.6, '>70': 0.7},
    'sex_risk': {'male': 1.0, 'female': 1.2}}, 'risk_factors': [
    'recent_surgery', 'immobility', 'malignancy', 'hypercoagulable'],
    'specificity': 0.7, 'urgency': 'emergency', 'rule_out_first': True,
    'workup': {'immediate': ['ECG', 'D_dimer', 'CXR', 'CT_PE'], 'within_6h':
    [], 'optional': ['Echo']}, 'management_hints':
    'If high probability → Anticoagulation. Massive PE → Consider thrombolysis.'
    }, 'Vasovagal Syncope': {'symptoms': {'required': ['syncope'],
    'supporting': ['trigger', 'prodrome', 'nausea', 'sweating', 'pale',
    'young_age'], 'contradictory': ['during_exertion', 'no_prodrome',
    'older_age']}, 'demographics': {'age_risk': {'<40': 0.8, '40-70': 0.4,
    '>70': 0.2}, 'sex_risk': {'male': 0.9, 'female': 1.1}}, 'risk_factors':
    ['young_age', 'anxiety', 'stress'], 'specificity': 0.6, 'urgency':
    'non_urgent', 'rule_out_first': False, 'workup': {'immediate': ['ECG'],
    'within_6h': [], 'optional': ['Tilt_test']}, 'management_hints':
    'Reassurance. Usually benign. Avoid triggers. Consider tilt test if recurrent.'
    }, 'Orthostatic Hypotension': {'symptoms': {'required': ['syncope'],
    'supporting': ['on_standing', 'dizziness', 'medications', 'dehydration',
    'elderly'], 'contradictory': []}, 'demographics': {'age_risk': {'<40': 
    0.3, '40-70': 0.5, '>70': 0.8}, 'sex_risk': {'male': 1.0, 'female': 1.0
    }}, 'risk_factors': ['elderly', 'medications', 'dehydration',
    'autonomic_dysfunction'], 'specificity': 0.55, 'urgency': 'non_urgent',
    'rule_out_first': False, 'workup': {'immediate': ['Orthostatic_vitals',
    'ECG'], 'within_6h': [], 'optional': []}, 'management_hints':
    'Volume expansion. Review medications. Compression stockings. Head of bed elevation.'
    }}

__all__ = ['SYNCOPE_DDX']
