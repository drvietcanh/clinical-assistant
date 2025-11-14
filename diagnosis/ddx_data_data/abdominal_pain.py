"""DDx Knowledge Base - Data
Differential diagnosis data for common clinical scenarios

NOTE: This file contains only data dictionaries.
Functions are in ddx_data.py"""

# Abdominal Pain Differential Diagnosis

ABDOMINAL_PAIN_DDX = {'Abdominal Aortic Aneurysm Rupture': {'symptoms': {'required': [
    'abdominal_pain', 'severe'], 'supporting': ['back_pain', 'hypotension',
    'pulsatile_mass', 'syncope'], 'contradictory': []}, 'demographics': {
    'age_risk': {'<40': 0.1, '40-70': 0.5, '>70': 0.8}, 'sex_risk': {'male':
    1.5, 'female': 1.0}}, 'risk_factors': ['age>65', 'male', 'smoking',
    'hypertension', 'family_history'], 'specificity': 0.8, 'urgency':
    'emergency', 'rule_out_first': True, 'workup': {'immediate': [
    'CT_angiography', 'US_abdomen', 'Type_crossmatch'], 'within_6h': [],
    'optional': []}, 'management_hints':
    'SURGICAL EMERGENCY! Immediate vascular surgery consult. Resuscitation while preparing for OR.'
    }, 'Appendicitis': {'symptoms': {'required': ['abdominal_pain'],
    'supporting': ['right_lower_quadrant', 'migration_pain', 'fever',
    'nausea', 'rebound_tenderness', 'mcburney_point'], 'contradictory': []},
    'demographics': {'age_risk': {'<40': 0.7, '40-70': 0.3, '>70': 0.4},
    'sex_risk': {'male': 1.0, 'female': 1.0}}, 'risk_factors': [],
    'specificity': 0.7, 'urgency': 'urgent', 'rule_out_first': False,
    'workup': {'immediate': ['CBC', 'CT_abdomen', 'US_abdomen'],
    'within_6h': [], 'optional': []}, 'management_hints':
    'Surgery consult. Antibiotics pre-op. If perforated → Urgent surgery.'},
    'Cholecystitis': {'symptoms': {'required': ['abdominal_pain'],
    'supporting': ['right_upper_quadrant', 'fever', 'positive_murphy',
    'nausea'], 'contradictory': []}, 'demographics': {'age_risk': {'<40': 
    0.5, '40-70': 0.7, '>70': 0.6}, 'sex_risk': {'male': 0.8, 'female': 1.2
    }}, 'risk_factors': ['female', 'obesity', 'age_40_plus'], 'specificity':
    0.65, 'urgency': 'urgent', 'rule_out_first': False, 'workup': {
    'immediate': ['CBC', 'LFT', 'US_abdomen'], 'within_6h': [], 'optional':
    ['CT_abdomen']}, 'management_hints':
    'Surgery consult. Antibiotics. Cholecystectomy within 24-48h.'}}

__all__ = ['ABDOMINAL_PAIN_DDX']
