"""DDx Knowledge Base - Data
Differential diagnosis data for common clinical scenarios

NOTE: This file contains only data dictionaries.
Functions are in ddx_data.py"""

# Bleeding Differential Diagnosis

BLEEDING_DDX = {'Upper GI Bleeding': {'symptoms': {'required': ['bleeding'], 'supporting':
    ['hematemesis', 'melena', 'coffee_ground_vomiting', 'abdominal_pain',
    'dizziness', 'syncope', 'hypotension'], 'contradictory': [
    'hematochezia_only', 'no_hematemesis_melena']}, 'demographics': {
    'age_risk': {'<40': 0.3, '40-70': 0.6, '>70': 0.8}, 'sex_risk': {'male':
    1.2, 'female': 1.0}}, 'risk_factors': ['NSAIDs', 'alcohol',
    'peptic_ulcer', 'varices', 'anticoagulants'], 'specificity': 0.85,
    'urgency': 'emergency', 'rule_out_first': True, 'workup': {'immediate':
    ['CBC', 'Coagulation', 'Type_cross', 'IV_access', 'EGD'], 'within_6h':
    ['EGD_with_intervention'], 'optional': ['CT_angiography']},
    'management_hints':
    'URGENT! Resuscitate first (IV fluids, blood if needed). PPI (omeprazole 80mg IV). If varices → Octreotide. EGD within 24h. Rockall/Blatchford score.'
    }, 'Lower GI Bleeding': {'symptoms': {'required': ['bleeding'],
    'supporting': ['hematochezia', 'bright_red_blood', 'abdominal_pain',
    'dizziness', 'syncope'], 'contradictory': ['hematemesis', 'melena_only'
    ]}, 'demographics': {'age_risk': {'<40': 0.3, '40-70': 0.6, '>70': 0.7},
    'sex_risk': {'male': 1.0, 'female': 1.0}}, 'risk_factors': [
    'diverticulosis', 'angiodysplasia', 'colitis', 'polyps',
    'anticoagulants'], 'specificity': 0.75, 'urgency': 'emergency',
    'rule_out_first': True, 'workup': {'immediate': ['CBC', 'Coagulation',
    'Type_cross', 'IV_access'], 'within_6h': ['Colonoscopy',
    'CT_angiography'], 'optional': ['Tagged_RBC_scan']}, 'management_hints':
    'Resuscitate. Most stop spontaneously. Colonoscopy if stable. If massive → CT angiography → embolization. Surgery if refractory.'
    }, 'Hemoptysis': {'symptoms': {'required': ['bleeding', 'cough'],
    'supporting': ['bloody_sputum', 'hemoptysis', 'dyspnea', 'chest_pain',
    'fever', 'weight_loss'], 'contradictory': ['hematemesis', 'no_cough']},
    'demographics': {'age_risk': {'<40': 0.4, '40-70': 0.6, '>70': 0.7},
    'sex_risk': {'male': 1.2, 'female': 1.0}}, 'risk_factors': ['smoking',
    'TB', 'lung_cancer', 'bronchiectasis', 'anticoagulants'], 'specificity':
    0.8, 'urgency': 'emergency', 'rule_out_first': True, 'workup': {
    'immediate': ['CXR', 'CBC', 'Coagulation', 'Chest_CT'], 'within_6h': [
    'Bronchoscopy'], 'optional': ['CT_angiography']}, 'management_hints':
    'URGENT if massive (>500ml/24h). Position patient (bleeding side down). O2. If massive → Intubation, bronchoscopy, embolization. Treat underlying cause.'
    }, 'Hematuria': {'symptoms': {'required': ['bleeding'], 'supporting': [
    'bloody_urine', 'hematuria', 'dysuria', 'frequency', 'flank_pain',
    'colicky_pain'], 'contradictory': ['no_urinary_symptoms']},
    'demographics': {'age_risk': {'<40': 0.4, '40-70': 0.6, '>70': 0.7},
    'sex_risk': {'male': 1.2, 'female': 1.0}}, 'risk_factors': ['UTI',
    'stones', 'malignancy', 'glomerulonephritis', 'anticoagulants'],
    'specificity': 0.75, 'urgency': 'urgent', 'rule_out_first': True,
    'workup': {'immediate': ['Urinalysis', 'Urine_culture', 'CBC',
    'Creatinine'], 'within_6h': ['CT_KUB', 'Cystoscopy'], 'optional': [
    'Renal_biopsy']}, 'management_hints':
    'If >40 years → Full urologic workup (CT, cystoscopy) to rule out malignancy. If <40 + UTI → Treat UTI first. If glomerular → Nephrology consult.'
    }, 'Menorrhagia': {'symptoms': {'required': ['bleeding'], 'supporting':
    ['heavy_menstrual_bleeding', 'prolonged_periods', 'anemia', 'fatigue',
    'clots'], 'contradictory': ['male', 'no_menstrual_history']},
    'demographics': {'age_risk': {'<20': 0.4, '20-50': 0.7, '>50': 0.5},
    'sex_risk': {'male': 0.0, 'female': 1.0}}, 'risk_factors': ['fibroids',
    'polyps', 'coagulopathy', 'hormonal_imbalance', 'IUD'], 'specificity': 
    0.7, 'urgency': 'urgent', 'rule_out_first': False, 'workup': {
    'immediate': ['CBC', 'Coagulation', 'Pregnancy_test'], 'within_6h': [
    'Pelvic_US'], 'optional': ['Endometrial_biopsy', 'Hysteroscopy']},
    'management_hints':
    'If severe anemia → Transfuse. Hormonal treatment (OCP, progestin). Tranexamic acid. If structural → Surgery. Rule out malignancy if >40.'
    }}

__all__ = ['BLEEDING_DDX']
