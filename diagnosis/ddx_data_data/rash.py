"""DDx Knowledge Base - Data
Differential diagnosis data for common clinical scenarios

NOTE: This file contains only data dictionaries.
Functions are in ddx_data.py"""

# Rash Differential Diagnosis

RASH_DDX = {'Drug Reaction': {'symptoms': {'required': ['rash'], 'supporting': [
    'recent_medications', 'maculopapular', 'generalized', 'pruritic',
    'fever', 'eosinophilia', 'timing_related_to_drug'], 'contradictory': [
    'target_lesions', 'bulla', 'scleral_involvement']}, 'demographics': {
    'age_risk': {'<40': 0.5, '40-70': 0.7, '>70': 0.8}, 'sex_risk': {'male':
    1.0, 'female': 1.2}}, 'risk_factors': ['multiple_medications',
    'specific_drugs', 'prior_reactions'], 'specificity': 0.75, 'urgency':
    'urgent', 'rule_out_first': True, 'workup': {'immediate': ['CBC',
    'Drug_history', 'Stop_suspected_drugs'], 'within_6h': [
    'Skin_biopsy_if_severe'], 'optional': []}, 'management_hints':
    'URGENT! Stop suspected medications immediately. Antihistamines. Steroids if severe. R/O SJS/TEN if severe (target lesions, bullae).'
    }, 'Stevens-Johnson Syndrome / TEN': {'symptoms': {'required': ['rash'],
    'supporting': ['target_lesions', 'bulla', 'detachment',
    'mucosal_involvement', 'fever', 'drug_exposure',
    'toxic_epidermal_necrolysis'], 'contradictory': ['maculopapular',
    'localized']}, 'demographics': {'age_risk': {'<40': 0.5, '40-70': 0.8,
    '>70': 0.7}, 'sex_risk': {'male': 1.0, 'female': 1.0}}, 'risk_factors':
    ['drugs', 'infections', 'genetic_factors'], 'specificity': 0.7,
    'urgency': 'emergency', 'rule_out_first': True, 'workup': {'immediate':
    ['Stop_all_drugs', 'ICU_admit', 'Dermatology_consult', 'Hydration'],
    'within_6h': ['Skin_biopsy'], 'optional': []}, 'management_hints':
    'URGENT! Life-threatening! ICU immediately. Stop all drugs. Dermatology + burn unit. Supportive care. High mortality if >30% BSA.'
    }, 'Meningococcal Sepsis': {'symptoms': {'required': ['rash', 'fever'],
    'supporting': ['petechial_purpura', 'rapidly_spreading',
    'unwell_patient', 'neck_stiffness', 'septic_shock', 'meningitis'],
    'contradictory': ['stable_patient', 'localized_rash']}, 'demographics':
    {'age_risk': {'<10': 0.8, '10-30': 0.7, '>30': 0.3}, 'sex_risk': {
    'male': 1.0, 'female': 1.0}}, 'risk_factors': ['young_age',
    'dormitory_living', 'asplenia'], 'specificity': 0.75, 'urgency':
    'emergency', 'rule_out_first': True, 'workup': {'immediate': [
    'Blood_cultures', 'LP', 'Antibiotics_immediately', 'Isolation'],
    'within_6h': ['Close_contacts_prophylaxis'], 'optional': []},
    'management_hints':
    "URGENT! Life-threatening! Don't delay antibiotics. Treat empirically with ceftriaxone. Isolate. Notify public health. Prophylaxis for contacts."
    }, 'Atopic Dermatitis / Eczema': {'symptoms': {'required': ['rash'],
    'supporting': ['pruritic', 'flexural_distribution', 'chronic_recurrent',
    'atopy', 'family_history', 'xerosis'], 'contradictory': ['acute_severe',
    'fever', 'systemic_symptoms']}, 'demographics': {'age_risk': {'<10': 
    0.8, '10-40': 0.5, '>40': 0.3}, 'sex_risk': {'male': 1.0, 'female': 1.0
    }}, 'risk_factors': ['atopy', 'family_history', 'allergies'],
    'specificity': 0.85, 'urgency': 'non_urgent', 'rule_out_first': False,
    'workup': {'immediate': ['Clinical_diagnosis'], 'within_6h': [],
    'optional': ['Patch_testing']}, 'management_hints':
    'Moisturizers, topical steroids, avoid triggers. Usually chronic. Refer dermatology if severe or unresponsive.'
    }}

__all__ = ['RASH_DDX']
