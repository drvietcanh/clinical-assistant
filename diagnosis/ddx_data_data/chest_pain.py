"""DDx Knowledge Base - Data
Differential diagnosis data for common clinical scenarios

NOTE: This file contains only data dictionaries.
Functions are in ddx_data.py"""

# Chest Pain Differential Diagnosis

CHEST_PAIN_DDX = {'Acute Myocardial Infarction': {'symptoms': {'required': [
    'chest_pain_retrosternal', 'chest_pain_crushing'], 'supporting': [
    'radiation_left_arm', 'radiation_jaw', 'diaphoresis', 'nausea',
    'dyspnea', 'anxiety'], 'contradictory': ['pleuritic_pain',
    'positional_pain', 'tenderness']}, 'demographics': {'age_risk': {'<40':
    0.1, '40-70': 0.6, '>70': 0.8}, 'sex_risk': {'male': 1.3, 'female': 1.0
    }}, 'risk_factors': ['diabetes', 'hypertension', 'smoking',
    'family_history_cad', 'hyperlipidemia', 'obesity'], 'specificity': 0.85,
    'urgency': 'emergency', 'rule_out_first': True, 'workup': {'immediate':
    ['ECG', 'Troponin', 'CXR'], 'within_6h': ['Repeat_Troponin', 'Echo'],
    'optional': ['CT_angiography', 'Stress_test']}, 'management_hints':
    'If STEMI → PCI within 90 min. If NSTEMI → Early invasive strategy if high risk.'
    }, 'Unstable Angina': {'symptoms': {'required': [
    'chest_pain_retrosternal'], 'supporting': ['radiation', 'diaphoresis',
    'nausea', 'dyspnea', 'exertional', 'rest_pain'], 'contradictory': [
    'pleuritic_pain', 'positional_pain']}, 'demographics': {'age_risk': {
    '<40': 0.15, '40-70': 0.65, '>70': 0.75}, 'sex_risk': {'male': 1.2,
    'female': 1.0}}, 'risk_factors': ['diabetes', 'hypertension', 'smoking',
    'family_history_cad'], 'specificity': 0.75, 'urgency': 'emergency',
    'rule_out_first': True, 'workup': {'immediate': ['ECG', 'Troponin'],
    'within_6h': ['Repeat_Troponin', 'Echo'], 'optional': ['CT_angiography'
    ]}, 'management_hints':
    'Similar to MI. Dual antiplatelet therapy + anticoagulation. Risk stratification with GRACE/TIMI.'
    }, 'Aortic Dissection': {'symptoms': {'required': ['chest_pain_severe'],
    'supporting': ['chest_pain_tearing', 'back_pain', 'hypertension',
    'pulse_deficit', 'syncope', 'neurologic_deficit'], 'contradictory': []},
    'demographics': {'age_risk': {'<40': 0.3, '40-70': 0.7, '>70': 0.8},
    'sex_risk': {'male': 1.4, 'female': 1.0}}, 'risk_factors': [
    'hypertension', 'marfan_syndrome', 'connective_tissue_disease',
    'pregnancy'], 'specificity': 0.7, 'urgency': 'emergency',
    'rule_out_first': True, 'workup': {'immediate': ['CXR', 'ECG',
    'CT_aortography', 'Echo'], 'within_6h': [], 'optional': ['MRI']},
    'management_hints':
    'URGENT! Control BP immediately. Surgical consult. Type A → Surgery. Type B → Medical management.'
    }, 'Pulmonary Embolism': {'symptoms': {'required': ['dyspnea',
    'chest_pain_pleuritic'], 'supporting': ['hemoptysis', 'syncope',
    'tachycardia', 'unilateral_leg_swelling', 'recent_immobility',
    'malignancy'], 'contradictory': []}, 'demographics': {'age_risk': {
    '<40': 0.4, '40-70': 0.6, '>70': 0.7}, 'sex_risk': {'male': 1.0,
    'female': 1.2}}, 'risk_factors': ['recent_surgery', 'immobility',
    'malignancy', 'hypercoagulable', 'OCP', 'pregnancy', 'history_dvt_pe'],
    'specificity': 0.65, 'urgency': 'emergency', 'rule_out_first': True,
    'workup': {'immediate': ['ECG', 'D_dimer', 'CXR', 'ABG'], 'within_6h':
    ['CT_PE', 'Echo'], 'optional': ['VQ_scan']}, 'management_hints':
    'If high probability → Anticoagulation. If low probability + negative D-dimer → Rule out. If intermediate/high → CT-PE.'
    }, 'GERD': {'symptoms': {'required': ['chest_pain_retrosternal',
    'heartburn'], 'supporting': ['regurgitation', 'worse_lying_down',
    'after_meals', 'relieved_antacids'], 'contradictory': ['radiation',
    'diaphoresis', 'exertional']}, 'demographics': {'age_risk': {'<40': 0.5,
    '40-70': 0.6, '>70': 0.7}, 'sex_risk': {'male': 1.0, 'female': 1.0}},
    'risk_factors': ['obesity', 'hiatal_hernia', 'pregnancy', 'smoking'],
    'specificity': 0.6, 'urgency': 'non_urgent', 'rule_out_first': False,
    'workup': {'immediate': [], 'within_6h': [], 'optional': [
    'Upper_endoscopy', 'pH_monitoring']}, 'management_hints':
    'PPI trial. Lifestyle modifications. Only investigate if red flags or not responding.'
    }, 'Costochondritis': {'symptoms': {'required': ['chest_pain'],
    'supporting': ['chest_wall_tenderness', 'reproducible',
    'worse_movement', 'worse_respiration'], 'contradictory': ['radiation',
    'diaphoresis', 'dyspnea']}, 'demographics': {'age_risk': {'<40': 0.6,
    '40-70': 0.4, '>70': 0.3}, 'sex_risk': {'male': 0.8, 'female': 1.2}},
    'risk_factors': ['recent_physical_activity',
    'upper_respiratory_infection'], 'specificity': 0.55, 'urgency':
    'non_urgent', 'rule_out_first': False, 'workup': {'immediate': [],
    'within_6h': [], 'optional': ['CXR']}, 'management_hints':
    'NSAIDs. Usually self-limited. Reassure after ruling out cardiac.'}}

__all__ = ['CHEST_PAIN_DDX']
