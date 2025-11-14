"""DDx Knowledge Base - Data
Differential diagnosis data for common clinical scenarios

NOTE: This file contains only data dictionaries.
Functions are in ddx_data.py"""

# Kidney Injury Differential Diagnosis

KIDNEY_INJURY_DDX = {'Acute Kidney Injury (Prerenal)': {'symptoms': {'required': [
    'acute_kidney_injury', 'increased_creatinine'], 'supporting': [
    'dehydration', 'hypotension', 'reduced_urine_output',
    'volume_depletion', 'congestive_heart_failure', 'liver_disease'],
    'contradictory': ['nephritic_sediment', 'proteinuria_heavy', 'casts']},
    'demographics': {'age_risk': {'<40': 0.3, '40-70': 0.6, '>70': 0.8},
    'sex_risk': {'male': 1.0, 'female': 1.0}}, 'risk_factors': [
    'dehydration', 'heart_failure', 'liver_disease', 'sepsis',
    'hypotension', 'medications'], 'specificity': 0.75, 'urgency':
    'emergency', 'rule_out_first': True, 'workup': {'immediate': [
    'Creatinine_eGFR', 'Urinalysis', 'FENa', 'FeUrea', 'CBC',
    'Electrolytes'], 'within_6h': ['Renal_US'], 'optional': []},
    'management_hints':
    'URGENT! If volume depleted → Fluids. Treat underlying cause (HF, sepsis, etc.). FENa <1% suggests prerenal.'
    }, 'Acute Tubular Necrosis': {'symptoms': {'required': [
    'acute_kidney_injury', 'increased_creatinine'], 'supporting': [
    'ischemia', 'nephrotoxins', 'contrast_induced', 'myoglobinuria',
    'pigmented_granular_casts', 'FENa_>1'], 'contradictory': [
    'prerenal_FENa', 'nephritic_urine']}, 'demographics': {'age_risk': {
    '<40': 0.3, '40-70': 0.7, '>70': 0.9}, 'sex_risk': {'male': 1.0,
    'female': 1.0}}, 'risk_factors': ['ischemia', 'sepsis', 'contrast',
    'aminoglycosides', 'myoglobin', 'hypotension'], 'specificity': 0.7,
    'urgency': 'emergency', 'rule_out_first': True, 'workup': {'immediate':
    ['Creatinine_eGFR', 'Urinalysis', 'FENa', 'CK_if_rhabdo',
    'Urine_microscopy'], 'within_6h': ['Renal_US'], 'optional': []},
    'management_hints':
    'URGENT! Supportive care. R/O cause (contrast, meds, rhabdo). Usually reversible. Consider dialysis if severe.'
    }, 'Post-Renal Obstruction': {'symptoms': {'required': [
    'acute_kidney_injury', 'increased_creatinine'], 'supporting': [
    'reduced_urine_output', 'hesitancy', 'frequency', 'dribbling',
    'flank_pain', 'hydronephrosis'], 'contradictory': [
    'normal_urine_output', 'no_obstruction_imaging']}, 'demographics': {
    'age_risk': {'<40': 0.4, '40-70': 0.7, '>70': 0.8}, 'sex_risk': {'male':
    1.2, 'female': 1.0}}, 'risk_factors': ['BPH', 'prostate_cancer',
    'nephrolithiasis', 'tumors', 'strictures'], 'specificity': 0.75,
    'urgency': 'emergency', 'rule_out_first': True, 'workup': {'immediate':
    ['Creatinine_eGFR', 'Renal_US', 'Post_void_residual'], 'within_6h': [
    'CT_abdomen_pelvis', 'Urology_consult'], 'optional': []},
    'management_hints':
    'URGENT! Catheterize immediately if retention. US to confirm obstruction. Urology consult. Relief of obstruction usually curative.'
    }, 'Glomerulonephritis': {'symptoms': {'required': [
    'acute_kidney_injury', 'increased_creatinine'], 'supporting': [
    'proteinuria', 'hematuria', 'hypertension', 'edema',
    'hypocomplementemia', 'nephritic_sediment', 'RBC_casts'],
    'contradictory': ['no_proteinuria', 'no_casts']}, 'demographics': {
    'age_risk': {'<20': 0.5, '20-60': 0.6, '>60': 0.4}, 'sex_risk': {'male':
    1.0, 'female': 1.0}}, 'risk_factors': ['infections',
    'autoimmune_diseases', 'medications', 'malignancy'], 'specificity': 0.7,
    'urgency': 'emergency', 'rule_out_first': True, 'workup': {'immediate':
    ['Urinalysis', 'UPCR', 'C3_C4', 'ANA_dsDNA', 'ANCA', 'Anti_GBM'],
    'within_6h': ['Renal_biopsy'], 'optional': []}, 'management_hints':
    'URGENT! Nephrology consult immediately. Biopsy if severe. High-dose steroids + immunosuppression usually indicated.'
    }}

__all__ = ['KIDNEY_INJURY_DDX']
