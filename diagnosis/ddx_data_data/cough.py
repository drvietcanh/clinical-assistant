"""DDx Knowledge Base - Data
Differential diagnosis data for common clinical scenarios

NOTE: This file contains only data dictionaries.
Functions are in ddx_data.py"""

# Cough Differential Diagnosis

COUGH_DDX = {'Community Acquired Pneumonia (CAP)': {'symptoms': {'required': ['cough'],
    'supporting': ['productive_cough', 'fever', 'dyspnea', 'chest_pain',
    'sputum_purulent', 'chills', 'malaise'], 'contradictory': [
    'chronic_cough', 'no_fever', 'no_sputum']}, 'demographics': {'age_risk':
    {'<5': 0.6, '5-65': 0.5, '>65': 0.8}, 'sex_risk': {'male': 1.0,
    'female': 1.0}}, 'risk_factors': ['age_>65', 'smoking', 'COPD',
    'immunocompromised', 'nursing_home', 'alcoholism'], 'specificity': 0.75,
    'urgency': 'urgent', 'rule_out_first': True, 'workup': {'immediate': [
    'CXR', 'CBC', 'CRP', 'Blood_cultures'], 'within_6h': ['Sputum_culture',
    'ABG_if_severe'], 'optional': ['Procalcitonin', 'CT_chest']},
    'management_hints':
    'CURB-65 score for severity. If CURB-65 ≥2 → Hospital admission. Empiric antibiotics: Amoxicillin-clavulanate or Azithromycin. If severe → Ceftriaxone + Azithromycin.'
    }, 'COPD Exacerbation': {'symptoms': {'required': ['cough',
    'chronic_cough'], 'supporting': ['productive_cough', 'increased_sputum',
    'dyspnea', 'wheeze', 'history_copd', 'smoking_history'],
    'contradictory': ['acute_onset', 'no_smoking_history', 'young_age']},
    'demographics': {'age_risk': {'<40': 0.2, '40-70': 0.7, '>70': 0.8},
    'sex_risk': {'male': 1.3, 'female': 1.0}}, 'risk_factors': ['smoking',
    'age', 'occupational_exposure', 'alpha1_antitrypsin_deficiency'],
    'specificity': 0.8, 'urgency': 'urgent', 'rule_out_first': False,
    'workup': {'immediate': ['CXR', 'ABG', 'PEFR', 'CBC'], 'within_6h': [
    'Sputum_culture', 'ECG'], 'optional': ['CT_chest', 'Echo']},
    'management_hints':
    'Bronchodilators (SABA + LABA). Systemic steroids. Antibiotics if purulent sputum. O2 to target SpO2 88-92%. Consider NIV if hypercapnic.'
    }, 'Congestive Heart Failure (CHF)': {'symptoms': {'required': ['cough',
    'dyspnea'], 'supporting': ['orthopnea', 'paroxysmal_nocturnal_dyspnea',
    'edema', 'fatigue', 'weight_gain', 'jugular_venous_distension'],
    'contradictory': ['no_dyspnea', 'no_edema']}, 'demographics': {
    'age_risk': {'<40': 0.2, '40-70': 0.6, '>70': 0.8}, 'sex_risk': {'male':
    1.0, 'female': 1.0}}, 'risk_factors': ['hypertension', 'CAD',
    'diabetes', 'valvular_disease', 'cardiomyopathy'], 'specificity': 0.7,
    'urgency': 'urgent', 'rule_out_first': True, 'workup': {'immediate': [
    'CXR', 'BNP_NT_proBNP', 'ECG', 'Echo'], 'within_6h': ['Troponin',
    'Electrolytes'], 'optional': ['CT_chest']}, 'management_hints':
    'Diuretics (furosemide). ACE-I/ARB. Beta-blockers if stable. O2. If severe → NIV or intubation. Treat underlying cause.'
    }, 'Asthma': {'symptoms': {'required': ['cough'], 'supporting': [
    'wheeze', 'dyspnea', 'chest_tightness', 'nocturnal_symptoms',
    'exercise_induced', 'atopy', 'family_history'], 'contradictory': [
    'chronic_productivity', 'smoking_history_long']}, 'demographics': {
    'age_risk': {'<20': 0.7, '20-50': 0.6, '>50': 0.4}, 'sex_risk': {'male':
    1.0, 'female': 1.2}}, 'risk_factors': ['atopy', 'family_history',
    'allergies', 'viral_infections'], 'specificity': 0.75, 'urgency':
    'urgent', 'rule_out_first': False, 'workup': {'immediate': ['PEFR',
    'CXR', 'O2_saturation'], 'within_6h': ['ABG_if_severe', 'Spirometry'],
    'optional': ['Allergy_testing']}, 'management_hints':
    'SABA (salbutamol). Systemic steroids if moderate-severe. O2. If severe → IV magnesium, consider intubation. Long-term: ICS + LABA.'
    }, 'GERD': {'symptoms': {'required': ['cough'], 'supporting': [
    'heartburn', 'regurgitation', 'worse_lying_down', 'worse_after_meals',
    'chronic_cough', 'hoarseness', 'nocturnal_cough'], 'contradictory': [
    'fever', 'productive_cough', 'dyspnea']}, 'demographics': {'age_risk':
    {'<40': 0.4, '40-70': 0.6, '>70': 0.5}, 'sex_risk': {'male': 1.0,
    'female': 1.0}}, 'risk_factors': ['obesity', 'pregnancy',
    'hiatal_hernia', 'smoking', 'alcohol'], 'specificity': 0.7, 'urgency':
    'non_urgent', 'rule_out_first': False, 'workup': {'immediate': [
    'Clinical_diagnosis'], 'within_6h': [], 'optional': ['Upper_endoscopy',
    'pH_monitoring']}, 'management_hints':
    'PPI trial (omeprazole 40mg BID). Lifestyle: Elevate head, avoid late meals, weight loss. If persistent → Endoscopy.'
    }, 'Post-nasal Drip': {'symptoms': {'required': ['cough'], 'supporting':
    ['nasal_congestion', 'rhinorrhea', 'throat_clearing', 'chronic_cough',
    'worse_lying_down', 'allergic_symptoms'], 'contradictory': ['fever',
    'productive_cough', 'dyspnea']}, 'demographics': {'age_risk': {'<40': 
    0.5, '40-70': 0.6, '>70': 0.4}, 'sex_risk': {'male': 1.0, 'female': 1.0
    }}, 'risk_factors': ['allergies', 'sinusitis', 'rhinitis'],
    'specificity': 0.65, 'urgency': 'non_urgent', 'rule_out_first': False,
    'workup': {'immediate': ['Clinical_diagnosis'], 'within_6h': [],
    'optional': ['Sinus_CT', 'Allergy_testing']}, 'management_hints':
    'Nasal steroids. Antihistamines. Nasal irrigation. Treat underlying rhinitis/sinusitis.'
    }}

__all__ = ['COUGH_DDX']
