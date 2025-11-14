"""DDx Knowledge Base - Data
Differential diagnosis data for common clinical scenarios

NOTE: This file contains only data dictionaries.
Functions are in ddx_data.py"""

# Vomiting Differential Diagnosis

VOMITING_DDX = {'Intestinal Obstruction': {'symptoms': {'required': ['vomiting',
    'abdominal_distension'], 'supporting': ['absent_bowel_sounds',
    'constipation', 'abdominal_pain', 'bilious_vomiting',
    'high_pitched_bowel_sounds', 'previous_surgery'], 'contradictory': [
    'diarrhea', 'normal_bowel_sounds', 'flatus']}, 'demographics': {
    'age_risk': {'<40': 0.4, '40-70': 0.7, '>70': 0.9}, 'sex_risk': {'male':
    1.0, 'female': 1.0}}, 'risk_factors': ['previous_surgery', 'hernia',
    'tumors', 'adhesions'], 'specificity': 0.8, 'urgency': 'emergency',
    'rule_out_first': True, 'workup': {'immediate': ['Abdominal_XR',
    'CBC_chemistries', 'Abdominal_exam'], 'within_6h': ['CT_abdomen_pelvis'
    ], 'optional': []}, 'management_hints':
    "URGENT! NPO. NG tube. Surgical consult. Don't give laxatives. Check for hernias. May need surgery."
    }, 'Acute Pancreatitis': {'symptoms': {'required': ['vomiting',
    'abdominal_pain'], 'supporting': ['epigastric_pain', 'radiating_back',
    'worse_lying_supine', 'gallstones', 'alcohol',
    'elevated_lipase_amylase'], 'contradictory': ['no_abdominal_pain',
    'normal_enzymes']}, 'demographics': {'age_risk': {'<40': 0.5, '40-70': 
    0.7, '>70': 0.6}, 'sex_risk': {'male': 1.2, 'female': 1.0}},
    'risk_factors': ['gallstones', 'alcohol', 'hypertriglyceridemia',
    'ERCP', 'trauma'], 'specificity': 0.85, 'urgency': 'emergency',
    'rule_out_first': True, 'workup': {'immediate': ['Lipase_amylase',
    'CT_abdomen', 'CBC_chemistries', 'Lactate'], 'within_6h': [
    'ERCP_if_galstones'], 'optional': []}, 'management_hints':
    'URGENT! NPO, IV fluids, pain control. Check lipase (>3x normal). Calculate BISAP or Ranson score. ICU if severe.'
    }, 'Gastroenteritis': {'symptoms': {'required': ['vomiting', 'diarrhea'
    ], 'supporting': ['nausea', 'fever', 'abdominal_cramps',
    'recent_food_exposure', 'multiple_patients'], 'contradictory': [
    'no_diarrhea', 'chronic_symptoms']}, 'demographics': {'age_risk': {
    '<10': 0.9, '10-65': 0.6, '>65': 0.8}, 'sex_risk': {'male': 1.0,
    'female': 1.0}}, 'risk_factors': ['food_contamination',
    'immunocompromised', 'travel'], 'specificity': 0.75, 'urgency':
    'urgent', 'rule_out_first': False, 'workup': {'immediate': [
    'CBC_chemistries', 'Stool_culture'], 'within_6h': [], 'optional': []},
    'management_hints':
    'Supportive care. Hydration. Usually self-limited. Check for dehydration. Antiemetics if severe.'
    }, 'Metabolic Acidosis': {'symptoms': {'required': ['vomiting'],
    'supporting': ['hyperglycemia', 'ketosis', 'DKA',
    'altered_mental_status', 'Kussmaul_breathing', 'polyuria'],
    'contradictory': ['normal_glucose', 'normal_acid_base']},
    'demographics': {'age_risk': {'<40': 0.5, '40-70': 0.8, '>70': 0.9},
    'sex_risk': {'male': 1.0, 'female': 1.0}}, 'risk_factors': ['diabetes',
    'alcohol', 'infection'], 'specificity': 0.7, 'urgency': 'emergency',
    'rule_out_first': True, 'workup': {'immediate': ['Glucose', 'ABG',
    'Ketones', 'Electrolytes'], 'within_6h': ['Insulin_protocol'],
    'optional': []}, 'management_hints':
    'URGENT! If DKA → Insulin drip + fluids. Monitor electrolytes closely. Check for underlying infection.'
    }}

__all__ = ['VOMITING_DDX']
