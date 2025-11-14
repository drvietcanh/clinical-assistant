"""DDx Knowledge Base - Data
Differential diagnosis data for common clinical scenarios

NOTE: This file contains only data dictionaries.
Functions are in ddx_data.py"""

# Htn Emergency Differential Diagnosis

HTN_EMERGENCY_DDX = {'Hypertensive Crisis': {'symptoms': {'required': ['severe_hypertension',
    'SBP_>180_or_DBP_>120'], 'supporting': ['chest_pain', 'dyspnea',
    'severe_headache', 'altered_mental_status', 'visual_changes',
    'nausea_vomiting'], 'contradictory': ['normal_bp',
    'asymptomatic_controlled']}, 'demographics': {'age_risk': {'<40': 0.5,
    '40-70': 0.8, '>70': 0.9}, 'sex_risk': {'male': 1.0, 'female': 1.0}},
    'risk_factors': ['preexisting_htn', 'noncompliance_meds', 'new_meds',
    'cocaine_use', 'pregnancy'], 'specificity': 0.8, 'urgency': 'emergency',
    'rule_out_first': True, 'workup': {'immediate': ['BP_monitoring', 'ECG',
    'Chest_X_ray', 'CBC_chemistries', 'Urinalysis'], 'within_6h': ['Echo',
    'Head_CT'], 'optional': ['Renal_US']}, 'management_hints':
    'URGENT! Lower BP gradually (25% in 1h, then target over 2-6h). IV agents. R/O end-organ damage. Labetalol, nicardipine, or nitroprusside.'
    }, 'Renal Emergency': {'symptoms': {'required': ['severe_hypertension'],
    'supporting': ['acute_kidney_injury', 'oliguria', 'flank_pain',
    'hematuria', 'elevated_creatinine'], 'contradictory': [
    'normal_creatinine', 'normal_urine_output']}, 'demographics': {
    'age_risk': {'<40': 0.5, '40-70': 0.8, '>70': 0.9}, 'sex_risk': {'male':
    1.0, 'female': 1.0}}, 'risk_factors': ['preexisting_ckd',
    'renal_artery_stenosis', 'autoimmune_vasculitis'], 'specificity': 0.75,
    'urgency': 'emergency', 'rule_out_first': True, 'workup': {'immediate':
    ['Creatinine_eGFR', 'Urinalysis', 'Renal_US', 'Urine_sediment'],
    'within_6h': ['Renal_biopsy_if_needed'], 'optional': [
    'Renal_angiography']}, 'management_hints':
    'URGENT! Nephrology consult. Lower BP carefully. May need dialysis if severe AKI. Check for renal artery stenosis or glomerulonephritis.'
    }, 'Stroke (Hemorrhagic)': {'symptoms': {'required': [
    'severe_hypertension', 'neurologic_deficit'], 'supporting': [
    'sudden_onset', 'severe_headache', 'nausea_vomiting',
    'altered_consciousness', 'focal_neurologic_signs'], 'contradictory': [
    'normal_exam', 'no_neurologic_findings']}, 'demographics': {'age_risk':
    {'<40': 0.4, '40-70': 0.8, '>70': 0.9}, 'sex_risk': {'male': 1.1,
    'female': 1.0}}, 'risk_factors': ['hypertension', 'anticoagulation',
    'AVM', 'cocaine_use', 'amyloid_angiopathy'], 'specificity': 0.75,
    'urgency': 'emergency', 'rule_out_first': True, 'workup': {'immediate':
    ['Head_CT', 'Neurologic_exam', 'Coagulation_studies'], 'within_6h': [
    'MRI_if_needed', 'Neurosurgery_consult'], 'optional': []},
    'management_hints':
    "URGENT! Don't lower BP too fast if large bleed. Neurosurgery consult. Reverse anticoagulation if bleeding. Monitor ICP."
    }}

__all__ = ['HTN_EMERGENCY_DDX']
