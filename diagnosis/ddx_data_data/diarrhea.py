"""DDx Knowledge Base - Data
Differential diagnosis data for common clinical scenarios

NOTE: This file contains only data dictionaries.
Functions are in ddx_data.py"""

# Diarrhea Differential Diagnosis

DIARRHEA_DDX = {'Infectious Diarrhea': {'symptoms': {'required': ['diarrhea'],
    'supporting': ['acute_onset', 'fever', 'abdominal_cramps',
    'bloody_stools', 'nausea_vomiting', 'recent_food_exposure',
    'watery_diarrhea'], 'contradictory': ['chronic_course', 'weight_loss',
    'iron_deficiency_anemia']}, 'demographics': {'age_risk': {'<10': 0.8,
    '10-65': 0.6, '>65': 0.7}, 'sex_risk': {'male': 1.0, 'female': 1.0}},
    'risk_factors': ['recent_travel', 'food_contamination',
    'immunocompromised', 'recent_antibiotics'], 'specificity': 0.7,
    'urgency': 'urgent', 'rule_out_first': False, 'workup': {'immediate': [
    'Stool_culture', 'Stool_O_P', 'CBC_chemistries'], 'within_6h': [
    'C_diff_toxin'], 'optional': ['Blood_cultures']}, 'management_hints':
    'Supportive care. Antibiotics only if severe or specific pathogens. Check for dehydration. Consider C. diff if recent antibiotics.'
    }, 'Clostridium difficile Colitis': {'symptoms': {'required': [
    'diarrhea'], 'supporting': ['recent_antibiotics', 'watery_diarrhea',
    'abdominal_cramps', 'fever', 'leukocytosis', 'hospital_stay'],
    'contradictory': ['chronic_weight_loss', 'iron_deficiency']},
    'demographics': {'age_risk': {'<40': 0.3, '40-70': 0.6, '>70': 0.9},
    'sex_risk': {'male': 1.0, 'female': 1.0}}, 'risk_factors': [
    'recent_antibiotics', 'hospital_stay', 'elderly', 'immunosuppression',
    'PPI_use'], 'specificity': 0.75, 'urgency': 'urgent', 'rule_out_first':
    True, 'workup': {'immediate': ['C_diff_toxin', 'CBC_with_diff',
    'Lactate'], 'within_6h': ['CT_abdomen_if_severe'], 'optional': [
    'Metronidazole_or_vancomycin']}, 'management_hints':
    'URGENT! If recent antibiotics + diarrhea → Check C. diff immediately. Metronidazole or vancomycin. Isolate patient. Check for toxic megacolon.'
    }, 'Inflammatory Bowel Disease': {'symptoms': {'required': ['diarrhea',
    'chronic_course'], 'supporting': ['bloody_stools', 'abdominal_pain',
    'weight_loss', 'fatigue', 'fever', 'family_history_ibd',
    'extraintestinal_manifestations'], 'contradictory': ['acute_onset',
    'self_limiting']}, 'demographics': {'age_risk': {'<20': 0.2, '20-40': 
    0.7, '>40': 0.5}, 'sex_risk': {'male': 1.0, 'female': 1.1}},
    'risk_factors': ['family_history', 'smoking', 'age_15_30'],
    'specificity': 0.75, 'urgency': 'urgent', 'rule_out_first': False,
    'workup': {'immediate': ['Colonoscopy', 'CRP_ESR', 'Calprotectin',
    'FBC'], 'within_6h': [], 'optional': ['CT_or_MRI_abdomen',
    'Small_bowel_series']}, 'management_hints':
    'If chronic diarrhea + weight loss + bleeding → Refer gastroenterology. Colonoscopy mandatory. Start immunosuppression if severe.'
    }, 'Irritable Bowel Syndrome': {'symptoms': {'required': ['diarrhea',
    'chronic_course'], 'supporting': ['alternating_constipation_diarrhea',
    'abdominal_bloating', 'relieved_by_defecation', 'mucus_in_stool',
    'stress_related'], 'contradictory': ['fever', 'weight_loss',
    'bloody_stools', 'night_symptoms']}, 'demographics': {'age_risk': {
    '<20': 0.3, '20-50': 0.7, '>50': 0.4}, 'sex_risk': {'male': 1.0,
    'female': 1.5}}, 'risk_factors': ['female', 'stress', 'anxiety',
    'depression'], 'specificity': 0.8, 'urgency': 'non_urgent',
    'rule_out_first': False, 'workup': {'immediate': [
    'Clinical_diagnosis_Rome_criteria'], 'within_6h': [], 'optional': [
    'Colonoscopy_if_alarm_symptoms']}, 'management_hints':
    'Diagnosis of exclusion. Rome criteria. Dietary changes, stress management. Reassurance. R/O organic causes if red flags.'
    }}

__all__ = ['DIARRHEA_DDX']
