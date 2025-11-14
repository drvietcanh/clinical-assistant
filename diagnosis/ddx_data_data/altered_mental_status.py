"""DDx Knowledge Base - Data
Differential diagnosis data for common clinical scenarios

NOTE: This file contains only data dictionaries.
Functions are in ddx_data.py"""

# Altered Mental Status Differential Diagnosis

ALTERED_MENTAL_STATUS_DDX = {'Stroke': {'symptoms': {'required': ['altered_mental_status',
    'neurologic_deficit'], 'supporting': ['focal_deficit', 'aphasia',
    'hemiparesis', 'facial_droop', 'hypertension'], 'contradictory': []},
    'demographics': {'age_risk': {'<40': 0.2, '40-70': 0.6, '>70': 0.8},
    'sex_risk': {'male': 1.1, 'female': 1.0}}, 'risk_factors': [
    'hypertension', 'diabetes', 'atrial_fibrillation', 'smoking'],
    'specificity': 0.8, 'urgency': 'emergency', 'rule_out_first': True,
    'workup': {'immediate': ['CT_head', 'ECG', 'CBC', 'PT_INR'],
    'within_6h': ['MRI', 'CTA'], 'optional': []}, 'management_hints':
    'TIME IS BRAIN! If ischemic < 4.5h → tPA. If < 24h → Consider thrombectomy.'
    }, 'Intracranial Hemorrhage': {'symptoms': {'required': [
    'altered_mental_status', 'headache'], 'supporting': ['hypertension',
    'vomiting', 'focal_deficit', 'seizure'], 'contradictory': []},
    'demographics': {'age_risk': {'<40': 0.3, '40-70': 0.6, '>70': 0.7},
    'sex_risk': {'male': 1.2, 'female': 1.0}}, 'risk_factors': [
    'hypertension', 'anticoagulation', 'age', 'trauma'], 'specificity': 
    0.75, 'urgency': 'emergency', 'rule_out_first': True, 'workup': {
    'immediate': ['CT_head', 'PT_INR', 'aPTT'], 'within_6h': [], 'optional':
    []}, 'management_hints':
    'URGENT! Control BP. Reverse anticoagulation. Neurosurgery consult if indicated.'
    }, 'Meningitis': {'symptoms': {'required': ['altered_mental_status',
    'fever'], 'supporting': ['headache', 'neck_stiffness', 'photophobia',
    'rash', 'nuchal_rigidity'], 'contradictory': []}, 'demographics': {
    'age_risk': {'<40': 0.6, '40-70': 0.4, '>70': 0.5}, 'sex_risk': {'male':
    1.0, 'female': 1.0}}, 'risk_factors': ['age_very_young', 'age_elderly',
    'immunocompromised'], 'specificity': 0.7, 'urgency': 'emergency',
    'rule_out_first': True, 'workup': {'immediate': ['LP', 'Blood_cultures',
    'CT_head', 'CBC', 'Cultures'], 'within_6h': [], 'optional': []},
    'management_hints':
    'URGENT! Antibiotics BEFORE LP if delay. Dexamethasone if bacterial. CSF analysis critical.'
    }, 'Sepsis': {'symptoms': {'required': ['altered_mental_status',
    'fever'], 'supporting': ['hypotension', 'tachycardia', 'tachypnea',
    'source_infection', 'hypothermia'], 'contradictory': []},
    'demographics': {'age_risk': {'<40': 0.4, '40-70': 0.6, '>70': 0.8},
    'sex_risk': {'male': 1.0, 'female': 1.0}}, 'risk_factors': ['elderly',
    'immunocompromised', 'comorbidities', 'recent_surgery'], 'specificity':
    0.65, 'urgency': 'emergency', 'rule_out_first': True, 'workup': {
    'immediate': ['Blood_cultures', 'CBC', 'Lactate', 'Cultures', 'CXR'],
    'within_6h': [], 'optional': []}, 'management_hints':
    'SEPSIS PROTOCOL! 1-hour bundle. Antibiotics within 1h. Fluid resuscitation. Source control.'
    }, 'Hypoglycemia': {'symptoms': {'required': ['altered_mental_status'],
    'supporting': ['diabetes', 'sweating', 'tremor', 'agitation',
    'glucose_low'], 'contradictory': []}, 'demographics': {'age_risk': {
    '<40': 0.5, '40-70': 0.6, '>70': 0.7}, 'sex_risk': {'male': 1.0,
    'female': 1.0}}, 'risk_factors': ['diabetes', 'insulin',
    'sulfonylureas', 'alcohol'], 'specificity': 0.7, 'urgency': 'emergency',
    'rule_out_first': True, 'workup': {'immediate': ['Glucose', 'CBC',
    'CMP'], 'within_6h': [], 'optional': []}, 'management_hints':
    'Check glucose STAT! If low → D50 50ml IV. If conscious → PO glucose. Monitor glucose q1h.'
    }}

__all__ = ['ALTERED_MENTAL_STATUS_DDX']
