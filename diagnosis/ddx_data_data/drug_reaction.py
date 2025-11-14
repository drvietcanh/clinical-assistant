"""DDx Knowledge Base - Data
Differential diagnosis data for common clinical scenarios

NOTE: This file contains only data dictionaries.
Functions are in ddx_data.py"""

# Drug Reaction Differential Diagnosis

DRUG_REACTION_DDX = {'Drug Allergy': {'symptoms': {'required': ['drug_reaction'], 'supporting':
    ['rash', 'urticaria', 'pruritus', 'recent_medication', 'timing_related',
    'angioedema'], 'contradictory': ['no_rash', 'delayed_timing']},
    'demographics': {'age_risk': {'<40': 0.5, '40-70': 0.7, '>70': 0.8},
    'sex_risk': {'male': 1.0, 'female': 1.2}}, 'risk_factors': [
    'multiple_medications', 'prior_allergies', 'specific_drugs'],
    'specificity': 0.75, 'urgency': 'urgent', 'rule_out_first': True,
    'workup': {'immediate': ['Stop_drug', 'CBC', 'Clinical_assessment'],
    'within_6h': [], 'optional': ['Allergy_testing']}, 'management_hints':
    'Stop suspected drug immediately. Antihistamines. Steroids if severe. If anaphylaxis → Epinephrine, ICU.'
    }, 'Drug Toxicity': {'symptoms': {'required': ['drug_reaction'],
    'supporting': ['nausea', 'vomiting', 'confusion', 'seizures',
    'organ_dysfunction', 'overdose', 'high_dose'], 'contradictory': [
    'normal_dose', 'no_symptoms']}, 'demographics': {'age_risk': {'<40': 
    0.4, '40-70': 0.6, '>70': 0.7}, 'sex_risk': {'male': 1.0, 'female': 1.0
    }}, 'risk_factors': ['overdose', 'drug_interactions',
    'renal_hepatic_impairment', 'elderly'], 'specificity': 0.7, 'urgency':
    'emergency', 'rule_out_first': True, 'workup': {'immediate': [
    'Drug_levels', 'CBC', 'CMP', 'ECG', 'Toxicology_screen'], 'within_6h':
    [], 'optional': []}, 'management_hints':
    'URGENT! Stop drug. Supportive care. Specific antidotes if available. Activated charcoal if recent ingestion. Dialysis if indicated.'
    }, 'Stevens-Johnson Syndrome / TEN': {'symptoms': {'required': [
    'drug_reaction'], 'supporting': ['rash', 'target_lesions', 'bulla',
    'mucosal_involvement', 'fever', 'drug_exposure',
    'toxic_epidermal_necrolysis'], 'contradictory': ['mild_rash',
    'no_mucosal']}, 'demographics': {'age_risk': {'<40': 0.5, '40-70': 0.8,
    '>70': 0.7}, 'sex_risk': {'male': 1.0, 'female': 1.0}}, 'risk_factors':
    ['drugs', 'infections', 'genetic_factors'], 'specificity': 0.85,
    'urgency': 'emergency', 'rule_out_first': True, 'workup': {'immediate':
    ['Stop_all_drugs', 'ICU_admit', 'Dermatology_consult', 'Skin_biopsy'],
    'within_6h': [], 'optional': []}, 'management_hints':
    'URGENT! Life-threatening! ICU immediately. Stop all drugs. Dermatology + burn unit. Supportive care. High mortality if >30% BSA.'
    }, 'Anaphylaxis': {'symptoms': {'required': ['drug_reaction'],
    'supporting': ['urticaria', 'angioedema', 'hypotension', 'dyspnea',
    'wheezing', 'rapid_onset', 'shock'], 'contradictory': ['delayed_onset',
    'no_respiratory_cardiovascular']}, 'demographics': {'age_risk': {'<40':
    0.5, '40-70': 0.6, '>70': 0.7}, 'sex_risk': {'male': 1.0, 'female': 1.2
    }}, 'risk_factors': ['prior_allergies', 'atopy', 'specific_drugs'],
    'specificity': 0.9, 'urgency': 'emergency', 'rule_out_first': True,
    'workup': {'immediate': ['Epinephrine', 'IV_access', 'O2', 'ICU'],
    'within_6h': [], 'optional': ['Tryptase']}, 'management_hints':
    'URGENT! Life-threatening! Epinephrine IM immediately. IV fluids. Antihistamines. Steroids. ICU monitoring. Delay → Death.'
    }, 'Serum Sickness': {'symptoms': {'required': ['drug_reaction'],
    'supporting': ['fever', 'rash', 'arthralgia', 'lymphadenopathy',
    'delayed_onset', 'serum_proteins'], 'contradictory': ['immediate_onset',
    'no_fever']}, 'demographics': {'age_risk': {'<40': 0.5, '40-70': 0.6,
    '>70': 0.4}, 'sex_risk': {'male': 1.0, 'female': 1.0}}, 'risk_factors':
    ['serum_proteins', 'monoclonal_antibodies', 'vaccines'], 'specificity':
    0.7, 'urgency': 'urgent', 'rule_out_first': False, 'workup': {
    'immediate': ['CBC', 'ESR_CRP', 'Clinical_assessment'], 'within_6h': [],
    'optional': []}, 'management_hints':
    'Stop drug. Antihistamines. NSAIDs for arthralgia. Steroids if severe. Usually self-limited.'
    }}

__all__ = ['DRUG_REACTION_DDX']
