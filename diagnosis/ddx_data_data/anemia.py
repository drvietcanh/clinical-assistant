"""DDx Knowledge Base - Data
Differential diagnosis data for common clinical scenarios

NOTE: This file contains only data dictionaries.
Functions are in ddx_data.py"""

# Anemia Differential Diagnosis

ANEMIA_DDX = {'Iron Deficiency Anemia': {'symptoms': {'required': ['anemia',
    'microcytic_hypochromic'], 'supporting': ['fatigue', 'pallor', 'pica',
    'brittle_nails', 'hair_loss', 'cheilosis', 'blood_loss'],
    'contradictory': ['macrocytic', 'elevated_ferritin', 'elevated_iron']},
    'demographics': {'age_risk': {'<10': 0.5, '10-50': 0.4, '>50': 0.8},
    'sex_risk': {'male': 1.0, 'female': 2.0}}, 'risk_factors': [
    'menstrual_blood_loss', 'GI_bleeding', 'pregnancy', 'malabsorption',
    'dietary_insufficiency'], 'specificity': 0.85, 'urgency': 'urgent',
    'rule_out_first': False, 'workup': {'immediate': ['FBC', 'Iron_studies',
    'Ferritin', 'TIBC'], 'within_6h': [], 'optional': ['Colonoscopy',
    'Upper_GI_endoscopy', 'Occult_blood_stool']}, 'management_hints':
    'Iron replacement. Investigate source of blood loss (especially GI in elderly). Check dietary intake in children.'
    }, 'Vitamin B12/Folate Deficiency': {'symptoms': {'required': ['anemia',
    'macrocytic_megaloblastic'], 'supporting': ['glossitis',
    'neurologic_symptoms', 'neuropathy', 'dementia', 'dietary_deficiency',
    'malabsorption'], 'contradictory': ['microcytic', 'normal_b12_folate']},
    'demographics': {'age_risk': {'<40': 0.3, '40-70': 0.7, '>70': 0.8},
    'sex_risk': {'male': 1.0, 'female': 1.2}}, 'risk_factors': ['elderly',
    'vegetarian_vegan', 'gastric_surgery', 'Crohn_disease', 'medications'],
    'specificity': 0.75, 'urgency': 'urgent', 'rule_out_first': False,
    'workup': {'immediate': ['FBC', 'B12_Folate_levels',
    'Methylmalonic_acid'], 'within_6h': [], 'optional': ['Schilling_test']},
    'management_hints':
    'Replace deficiencies. B12 injections if severe deficiency or malabsorption. Check for pernicious anemia (intrinsic factor antibodies).'
    }, 'Hemolytic Anemia': {'symptoms': {'required': ['anemia'],
    'supporting': ['jaundice', 'elevated_reticulocytes', 'elevated_ldh',
    'decreased_haptoglobin', 'dark_urine', 'splenomegaly'], 'contradictory':
    ['low_reticulocytes', 'normal_ldh']}, 'demographics': {'age_risk': {
    '<20': 0.5, '20-60': 0.4, '>60': 0.5}, 'sex_risk': {'male': 1.0,
    'female': 1.0}}, 'risk_factors': ['autoimmune', 'medications',
    'infections', 'mechanical_valve', 'thalassemia', 'sickle_cell'],
    'specificity': 0.7, 'urgency': 'urgent', 'rule_out_first': True,
    'workup': {'immediate': ['FBC', 'Reticulocytes', 'LDH', 'Haptoglobin',
    'Coombs_test', 'Bilirubin'], 'within_6h': [], 'optional': [
    'Hemoglobin_electrophoresis']}, 'management_hints':
    'URGENT! If sudden hemolysis → Check Coombs. Stop offending medications. Consider steroids for autoimmune. Monitor closely.'
    }}

__all__ = ['ANEMIA_DDX']
