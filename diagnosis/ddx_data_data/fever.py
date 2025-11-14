"""DDx Knowledge Base - Data
Differential diagnosis data for common clinical scenarios

NOTE: This file contains only data dictionaries.
Functions are in ddx_data.py"""

# Fever Differential Diagnosis

FEVER_DDX = {'Sepsis': {'symptoms': {'required': ['fever'], 'supporting': [
    'hypotension', 'tachycardia', 'tachypnea', 'altered_mental_status',
    'source_infection'], 'contradictory': []}, 'demographics': {'age_risk':
    {'<40': 0.4, '40-70': 0.6, '>70': 0.8}, 'sex_risk': {'male': 1.0,
    'female': 1.0}}, 'risk_factors': ['elderly', 'immunocompromised',
    'comorbidities'], 'specificity': 0.7, 'urgency': 'emergency',
    'rule_out_first': True, 'workup': {'immediate': ['Blood_cultures',
    'CBC', 'Lactate', 'Cultures', 'CXR', 'Urine_culture'], 'within_6h': [],
    'optional': []}, 'management_hints':
    'SEPSIS PROTOCOL! 1-hour bundle. Antibiotics within 1h.'}, 'Pneumonia':
    {'symptoms': {'required': ['fever', 'cough'], 'supporting': ['dyspnea',
    'productive_cough', 'chest_pain', 'crackles'], 'contradictory': []},
    'demographics': {'age_risk': {'<40': 0.5, '40-70': 0.6, '>70': 0.8},
    'sex_risk': {'male': 1.0, 'female': 1.0}}, 'risk_factors': ['elderly',
    'smoking', 'comorbidities'], 'specificity': 0.65, 'urgency': 'urgent',
    'rule_out_first': False, 'workup': {'immediate': ['CXR', 'CBC', 'CRP'],
    'within_6h': ['Blood_cultures', 'Sputum_culture'], 'optional': [
    'CT_chest']}, 'management_hints':
    'Antibiotics based on severity (CURB-65, PSI). Community vs hospital acquired.'
    }, 'UTI': {'symptoms': {'required': ['fever'], 'supporting': ['dysuria',
    'frequency', 'urgency', 'suprapubic_pain', 'flank_pain'],
    'contradictory': []}, 'demographics': {'age_risk': {'<40': 0.6, '40-70':
    0.5, '>70': 0.7}, 'sex_risk': {'male': 0.5, 'female': 1.5}},
    'risk_factors': ['female', 'catheter', 'elderly', 'pregnancy'],
    'specificity': 0.6, 'urgency': 'urgent', 'rule_out_first': False,
    'workup': {'immediate': ['Urinalysis', 'Urine_culture'], 'within_6h': [
    ], 'optional': ['CBC', 'CMP']}, 'management_hints':
    'Antibiotics. If pyelonephritis → IV antibiotics. Consider imaging if complicated.'
    }, 'Viral URI': {'symptoms': {'required': ['fever'], 'supporting': [
    'rhinorrhea', 'congestion', 'sore_throat', 'cough', 'myalgia'],
    'contradictory': ['high_fever_prolonged', 'severe_symptoms']},
    'demographics': {'age_risk': {'<40': 0.7, '40-70': 0.5, '>70': 0.4},
    'sex_risk': {'male': 1.0, 'female': 1.0}}, 'risk_factors': [],
    'specificity': 0.55, 'urgency': 'non_urgent', 'rule_out_first': False,
    'workup': {'immediate': [], 'within_6h': [], 'optional': ['CBC']},
    'management_hints':
    'Supportive care. Usually self-limited. Rule out bacterial if high fever/prolonged.'
    }}

__all__ = ['FEVER_DDX']
