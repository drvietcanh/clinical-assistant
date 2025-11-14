"""DDx Knowledge Base - Data
Differential diagnosis data for common clinical scenarios

NOTE: This file contains only data dictionaries.
Functions are in ddx_data.py"""

# Electrolyte Disorders Differential Diagnosis

ELECTROLYTE_DISORDERS_DDX = {'Hyponatremia': {'symptoms': {'required': ['electrolyte_disorder'],
    'supporting': ['nausea', 'headache', 'confusion', 'seizures', 'coma',
    'low_Na'], 'contradictory': ['normal_Na', 'high_Na']}, 'demographics':
    {'age_risk': {'<40': 0.4, '40-70': 0.6, '>70': 0.8}, 'sex_risk': {
    'male': 1.0, 'female': 1.0}}, 'risk_factors': ['diuretics', 'SIADH',
    'heart_failure', 'liver_disease', 'renal_disease'], 'specificity': 0.8,
    'urgency': 'emergency', 'rule_out_first': True, 'workup': {'immediate':
    ['Na', 'Osmolality', 'Urine_Na', 'Urine_osmolality', 'TSH', 'Cortisol'],
    'within_6h': [], 'optional': []}, 'management_hints':
    'If severe (<120) or symptomatic → 3% saline. Correct slowly (0.5-1 mEq/L/h) to avoid ODS. Treat underlying cause.'
    }, 'Hypernatremia': {'symptoms': {'required': ['electrolyte_disorder'],
    'supporting': ['thirst', 'confusion', 'seizures', 'coma', 'high_Na',
    'dehydration'], 'contradictory': ['normal_Na', 'low_Na']},
    'demographics': {'age_risk': {'<40': 0.3, '40-70': 0.5, '>70': 0.7},
    'sex_risk': {'male': 1.0, 'female': 1.0}}, 'risk_factors': [
    'dehydration', 'diabetes_insipidus', 'elderly', 'tube_feeding'],
    'specificity': 0.8, 'urgency': 'emergency', 'rule_out_first': True,
    'workup': {'immediate': ['Na', 'Osmolality', 'Urine_osmolality',
    'Volume_status'], 'within_6h': [], 'optional': []}, 'management_hints':
    'If severe (>160) or symptomatic → D5W or 0.45% saline. Correct slowly (0.5-1 mEq/L/h). Treat underlying cause.'
    }, 'Hypokalemia': {'symptoms': {'required': ['electrolyte_disorder'],
    'supporting': ['weakness', 'muscle_cramps', 'arrhythmias', 'low_K',
    'diuretics'], 'contradictory': ['normal_K', 'high_K']}, 'demographics':
    {'age_risk': {'<40': 0.4, '40-70': 0.6, '>70': 0.7}, 'sex_risk': {
    'male': 1.0, 'female': 1.0}}, 'risk_factors': ['diuretics', 'vomiting',
    'diarrhea', 'alkalosis'], 'specificity': 0.8, 'urgency': 'urgent',
    'rule_out_first': True, 'workup': {'immediate': ['K', 'Mg', 'ABG',
    'ECG'], 'within_6h': [], 'optional': ['Urine_K']}, 'management_hints':
    'If severe (<2.5) or symptomatic → IV K (max 20 mEq/h with cardiac monitoring). Check Mg. Treat underlying cause.'
    }, 'Hyperkalemia': {'symptoms': {'required': ['electrolyte_disorder'],
    'supporting': ['weakness', 'arrhythmias', 'ECG_changes', 'high_K',
    'renal_disease'], 'contradictory': ['normal_K', 'low_K']},
    'demographics': {'age_risk': {'<40': 0.3, '40-70': 0.6, '>70': 0.7},
    'sex_risk': {'male': 1.0, 'female': 1.0}}, 'risk_factors': [
    'renal_disease', 'medications', 'acidosis', 'cell_lysis'],
    'specificity': 0.85, 'urgency': 'emergency', 'rule_out_first': True,
    'workup': {'immediate': ['K', 'ECG', 'Creatinine', 'ABG'], 'within_6h':
    [], 'optional': []}, 'management_hints':
    'URGENT if >6.5 or ECG changes! Calcium gluconate (cardioprotection), insulin+glucose, albuterol, kayexalate. Dialysis if severe.'
    }}

__all__ = ['ELECTROLYTE_DISORDERS_DDX']
