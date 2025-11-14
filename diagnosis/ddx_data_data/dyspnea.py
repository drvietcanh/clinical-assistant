"""DDx Knowledge Base - Data
Differential diagnosis data for common clinical scenarios

NOTE: This file contains only data dictionaries.
Functions are in ddx_data.py"""

# Dyspnea Differential Diagnosis

DYSPNEA_DDX = {'Pulmonary Embolism': {'symptoms': {'required': ['dyspnea', 'acute_onset'],
    'supporting': ['pleuritic_chest_pain', 'hemoptysis', 'syncope',
    'tachycardia', 'unilateral_leg_swelling', 'recent_immobility'],
    'contradictory': ['gradual_onset', 'productive_cough']}, 'demographics':
    {'age_risk': {'<40': 0.4, '40-70': 0.6, '>70': 0.7}, 'sex_risk': {
    'male': 1.0, 'female': 1.2}}, 'risk_factors': ['recent_surgery',
    'immobility', 'malignancy', 'hypercoagulable', 'OCP'], 'specificity': 
    0.75, 'urgency': 'emergency', 'rule_out_first': True, 'workup': {
    'immediate': ['ECG', 'D_dimer', 'CXR', 'ABG'], 'within_6h': ['CT_PE'],
    'optional': ['Echo', 'VQ_scan']}, 'management_hints':
    'If high probability → Anticoagulation. Massive PE → Consider thrombolysis.'
    }, 'Acute Heart Failure / Pulmonary Edema': {'symptoms': {'required': [
    'dyspnea', 'acute_onset'], 'supporting': ['orthopnea',
    'paroxysmal_nocturnal_dyspnea', 'pink_frothy_sputum', 'edema',
    'jugular_venous_distension', 'crackles'], 'contradictory': []},
    'demographics': {'age_risk': {'<40': 0.2, '40-70': 0.6, '>70': 0.8},
    'sex_risk': {'male': 1.1, 'female': 1.0}}, 'risk_factors': ['CAD',
    'hypertension', 'diabetes', 'atrial_fibrillation', 'valvular_disease'],
    'specificity': 0.7, 'urgency': 'emergency', 'rule_out_first': True,
    'workup': {'immediate': ['CXR', 'ECG', 'BNP_NTproBNP', 'Echo', 'ABG'],
    'within_6h': [], 'optional': []}, 'management_hints':
    'Diuretics. Oxygen. Nitrates if not hypotensive. Treat underlying cause.'
    }, 'Severe Asthma / COPD Exacerbation': {'symptoms': {'required': [
    'dyspnea'], 'supporting': ['wheezing', 'cough', 'chest_tightness',
    'history_asthma_copd', 'triggers'], 'contradictory': []},
    'demographics': {'age_risk': {'<40': 0.7, '40-70': 0.5, '>70': 0.4},
    'sex_risk': {'male': 1.0, 'female': 1.0}}, 'risk_factors': [
    'asthma_history', 'copd_history', 'smoking', 'allergies'],
    'specificity': 0.65, 'urgency': 'emergency', 'rule_out_first': True,
    'workup': {'immediate': ['CXR', 'ABG', 'Peak_flow', 'O2_saturation'],
    'within_6h': [], 'optional': ['CBC', 'Theophylline_level']},
    'management_hints':
    'Bronchodilators. Steroids. Consider BiPAP if severe. Intubation if respiratory failure.'
    }, 'Pneumonia': {'symptoms': {'required': ['dyspnea'], 'supporting': [
    'fever', 'productive_cough', 'pleuritic_pain', 'crackles',
    'consolidation'], 'contradictory': []}, 'demographics': {'age_risk': {
    '<40': 0.5, '40-70': 0.6, '>70': 0.8}, 'sex_risk': {'male': 1.0,
    'female': 1.0}}, 'risk_factors': ['elderly', 'immunocompromised',
    'comorbidities', 'smoking'], 'specificity': 0.6, 'urgency': 'urgent',
    'rule_out_first': False, 'workup': {'immediate': ['CXR', 'CBC', 'CRP',
    'Cultures'], 'within_6h': [], 'optional': ['CT_chest', 'Blood_cultures'
    ]}, 'management_hints':
    'Antibiotics based on severity (CURB-65, PSI). Supportive care.'},
    'Anxiety / Hyperventilation': {'symptoms': {'required': ['dyspnea'],
    'supporting': ['anxiety', 'panic', 'paresthesia', 'chest_tightness',
    'normal_exam', 'normal_cxr'], 'contradictory': ['crackles', 'wheezing',
    'hypoxia']}, 'demographics': {'age_risk': {'<40': 0.7, '40-70': 0.4,
    '>70': 0.2}, 'sex_risk': {'male': 0.8, 'female': 1.2}}, 'risk_factors':
    ['anxiety_disorder', 'panic_disorder', 'stress'], 'specificity': 0.5,
    'urgency': 'non_urgent', 'rule_out_first': False, 'workup': {
    'immediate': ['CXR', 'ECG'], 'within_6h': [], 'optional': []},
    'management_hints':
    'Reassurance. Breathing exercises. Rule out organic causes first.'}}

__all__ = ['DYSPNEA_DDX']
