"""DDx Knowledge Base - Data
Differential diagnosis data for common clinical scenarios

NOTE: This file contains only data dictionaries.
Functions are in ddx_data.py"""

# Vision Changes Differential Diagnosis

VISION_CHANGES_DDX = {'Retinal Detachment': {'symptoms': {'required': ['vision_changes'],
    'supporting': ['sudden_vision_loss', 'floaters', 'flashes',
    'curtain_vision', 'no_pain', 'monocular'], 'contradictory': [
    'gradual_onset', 'pain', 'bilateral']}, 'demographics': {'age_risk': {
    '<40': 0.3, '40-70': 0.6, '>70': 0.7}, 'sex_risk': {'male': 1.0,
    'female': 1.0}}, 'risk_factors': ['myopia', 'trauma',
    'previous_detachment', 'diabetes'], 'specificity': 0.8, 'urgency':
    'emergency', 'rule_out_first': True, 'workup': {'immediate': [
    'Ophthalmology_consult', 'Fundoscopy', 'Slit_lamp'], 'within_6h': [
    'Ocular_ultrasound'], 'optional': []}, 'management_hints':
    'URGENT! Ophthalmology consult immediately. Surgical repair (pneumatic retinopexy, scleral buckle, vitrectomy). Delay → Permanent vision loss.'
    }, 'CVA / Stroke': {'symptoms': {'required': ['vision_changes'],
    'supporting': ['sudden_vision_loss', 'homonymous_hemianopia',
    'diplopia', 'neurologic_deficit', 'facial_droop', 'speech_problems'],
    'contradictory': ['gradual_onset', 'no_neurologic']}, 'demographics': {
    'age_risk': {'<40': 0.2, '40-70': 0.6, '>70': 0.8}, 'sex_risk': {'male':
    1.2, 'female': 1.0}}, 'risk_factors': ['hypertension',
    'atrial_fibrillation', 'diabetes', 'smoking', 'age'], 'specificity': 
    0.75, 'urgency': 'emergency', 'rule_out_first': True, 'workup': {
    'immediate': ['CT_head', 'Neurology_consult', 'NIHSS'], 'within_6h': [
    'MRI_brain', 'CTA'], 'optional': []}, 'management_hints':
    'URGENT! If ischemic <4.5h → tPA. If <24h + large vessel → Thrombectomy. Control risk factors.'
    }, 'Glaucoma (Acute Angle Closure)': {'symptoms': {'required': [
    'vision_changes'], 'supporting': ['sudden_vision_loss', 'eye_pain',
    'headache', 'nausea', 'vomiting', 'halos', 'red_eye'], 'contradictory':
    ['no_pain', 'gradual_onset']}, 'demographics': {'age_risk': {'<40': 0.2,
    '40-70': 0.6, '>70': 0.7}, 'sex_risk': {'male': 0.8, 'female': 1.0}},
    'risk_factors': ['hyperopia', 'age', 'family_history',
    'Asian_ethnicity'], 'specificity': 0.8, 'urgency': 'emergency',
    'rule_out_first': True, 'workup': {'immediate': [
    'Ophthalmology_consult', 'IOP_measurement', 'Slit_lamp'], 'within_6h':
    ['Gonioscopy'], 'optional': []}, 'management_hints':
    'URGENT! Lower IOP immediately (timolol, pilocarpine, acetazolamide). Laser iridotomy. Delay → Permanent vision loss.'
    }, 'Migraine Aura': {'symptoms': {'required': ['vision_changes'],
    'supporting': ['scintillating_scotoma', 'zigzag_lines', 'tunnel_vision',
    'headache_follows', 'recurrent', 'no_neurologic_deficit'],
    'contradictory': ['persistent_deficit', 'sudden_onset_severe']},
    'demographics': {'age_risk': {'<40': 0.7, '40-70': 0.5, '>70': 0.2},
    'sex_risk': {'male': 0.5, 'female': 1.0}}, 'risk_factors': [
    'family_history', 'female', 'young_age'], 'specificity': 0.75,
    'urgency': 'non_urgent', 'rule_out_first': False, 'workup': {
    'immediate': ['Clinical_diagnosis'], 'within_6h': [], 'optional': [
    'MRI_if_atypical']}, 'management_hints':
    'Triptans if headache. Avoid triggers. If first episode or atypical → Neuroimaging to rule out stroke/TIA.'
    }, 'Giant Cell Arteritis': {'symptoms': {'required': ['vision_changes'],
    'supporting': ['sudden_vision_loss', 'headache', 'temporal_tenderness',
    'jaw_claudication', 'fever', 'elderly', 'ESR_elevated'],
    'contradictory': ['young_age', 'no_headache']}, 'demographics': {
    'age_risk': {'<50': 0.0, '50-70': 0.6, '>70': 0.8}, 'sex_risk': {'male':
    0.5, 'female': 1.0}}, 'risk_factors': ['age_>50', 'female',
    'polymyalgia_rheumatica'], 'specificity': 0.8, 'urgency': 'emergency',
    'rule_out_first': True, 'workup': {'immediate': ['ESR_CRP',
    'Temporal_artery_biopsy', 'High_dose_steroids'], 'within_6h': [],
    'optional': []}, 'management_hints':
    'URGENT! High-dose steroids (prednisone 60-80mg) immediately to prevent vision loss. Temporal artery biopsy within 1 week.'
    }}

__all__ = ['VISION_CHANGES_DDX']
