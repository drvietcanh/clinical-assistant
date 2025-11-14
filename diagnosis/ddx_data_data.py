"""
DDx Knowledge Base - Data
Differential diagnosis data for common clinical scenarios

NOTE: This file contains only data dictionaries.
Functions are in ddx_data.py
"""

"""
DDx Knowledge Base
Differential diagnosis data for common clinical scenarios
"""

# Symptom mapping to diagnoses
CHEST_PAIN_DDX = {
    "Acute Myocardial Infarction": {
        "symptoms": {
            "required": ["chest_pain_retrosternal", "chest_pain_crushing"],
            "supporting": ["radiation_left_arm", "radiation_jaw", "diaphoresis", "nausea", "dyspnea", "anxiety"],
            "contradictory": ["pleuritic_pain", "positional_pain", "tenderness"]
        },
        "demographics": {
            "age_risk": {"<40": 0.1, "40-70": 0.6, ">70": 0.8},
            "sex_risk": {"male": 1.3, "female": 1.0}
        },
        "risk_factors": ["diabetes", "hypertension", "smoking", "family_history_cad", "hyperlipidemia", "obesity"],
        "specificity": 0.85,
        "urgency": "emergency",
        "rule_out_first": True,
        "workup": {
            "immediate": ["ECG", "Troponin", "CXR"],
            "within_6h": ["Repeat_Troponin", "Echo"],
            "optional": ["CT_angiography", "Stress_test"]
        },
        "management_hints": "If STEMI → PCI within 90 min. If NSTEMI → Early invasive strategy if high risk."
    },
    "Unstable Angina": {
        "symptoms": {
            "required": ["chest_pain_retrosternal"],
            "supporting": ["radiation", "diaphoresis", "nausea", "dyspnea", "exertional", "rest_pain"],
            "contradictory": ["pleuritic_pain", "positional_pain"]
        },
        "demographics": {
            "age_risk": {"<40": 0.15, "40-70": 0.65, ">70": 0.75},
            "sex_risk": {"male": 1.2, "female": 1.0}
        },
        "risk_factors": ["diabetes", "hypertension", "smoking", "family_history_cad"],
        "specificity": 0.75,
        "urgency": "emergency",
        "rule_out_first": True,
        "workup": {
            "immediate": ["ECG", "Troponin"],
            "within_6h": ["Repeat_Troponin", "Echo"],
            "optional": ["CT_angiography"]
        },
        "management_hints": "Similar to MI. Dual antiplatelet therapy + anticoagulation. Risk stratification with GRACE/TIMI."
    },
    "Aortic Dissection": {
        "symptoms": {
            "required": ["chest_pain_severe"],
            "supporting": ["chest_pain_tearing", "back_pain", "hypertension", "pulse_deficit", "syncope", "neurologic_deficit"],
            "contradictory": []
        },
        "demographics": {
            "age_risk": {"<40": 0.3, "40-70": 0.7, ">70": 0.8},
            "sex_risk": {"male": 1.4, "female": 1.0}
        },
        "risk_factors": ["hypertension", "marfan_syndrome", "connective_tissue_disease", "pregnancy"],
        "specificity": 0.70,
        "urgency": "emergency",
        "rule_out_first": True,
        "workup": {
            "immediate": ["CXR", "ECG", "CT_aortography", "Echo"],
            "within_6h": [],
            "optional": ["MRI"]
        },
        "management_hints": "URGENT! Control BP immediately. Surgical consult. Type A → Surgery. Type B → Medical management."
    },
    "Pulmonary Embolism": {
        "symptoms": {
            "required": ["dyspnea", "chest_pain_pleuritic"],
            "supporting": ["hemoptysis", "syncope", "tachycardia", "unilateral_leg_swelling", "recent_immobility", "malignancy"],
            "contradictory": []
        },
        "demographics": {
            "age_risk": {"<40": 0.4, "40-70": 0.6, ">70": 0.7},
            "sex_risk": {"male": 1.0, "female": 1.2}
        },
        "risk_factors": ["recent_surgery", "immobility", "malignancy", "hypercoagulable", "OCP", "pregnancy", "history_dvt_pe"],
        "specificity": 0.65,
        "urgency": "emergency",
        "rule_out_first": True,
        "workup": {
            "immediate": ["ECG", "D_dimer", "CXR", "ABG"],
            "within_6h": ["CT_PE", "Echo"],
            "optional": ["VQ_scan"]
        },
        "management_hints": "If high probability → Anticoagulation. If low probability + negative D-dimer → Rule out. If intermediate/high → CT-PE."
    },
    "GERD": {
        "symptoms": {
            "required": ["chest_pain_retrosternal", "heartburn"],
            "supporting": ["regurgitation", "worse_lying_down", "after_meals", "relieved_antacids"],
            "contradictory": ["radiation", "diaphoresis", "exertional"]
        },
        "demographics": {
            "age_risk": {"<40": 0.5, "40-70": 0.6, ">70": 0.7},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["obesity", "hiatal_hernia", "pregnancy", "smoking"],
        "specificity": 0.60,
        "urgency": "non_urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": [],
            "within_6h": [],
            "optional": ["Upper_endoscopy", "pH_monitoring"]
        },
        "management_hints": "PPI trial. Lifestyle modifications. Only investigate if red flags or not responding."
    },
    "Costochondritis": {
        "symptoms": {
            "required": ["chest_pain"],
            "supporting": ["chest_wall_tenderness", "reproducible", "worse_movement", "worse_respiration"],
            "contradictory": ["radiation", "diaphoresis", "dyspnea"]
        },
        "demographics": {
            "age_risk": {"<40": 0.6, "40-70": 0.4, ">70": 0.3},
            "sex_risk": {"male": 0.8, "female": 1.2}
        },
        "risk_factors": ["recent_physical_activity", "upper_respiratory_infection"],
        "specificity": 0.55,
        "urgency": "non_urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": [],
            "within_6h": [],
            "optional": ["CXR"]
        },
        "management_hints": "NSAIDs. Usually self-limited. Reassure after ruling out cardiac."
    }
}

DYSPNEA_DDX = {
    "Pulmonary Embolism": {
        "symptoms": {
            "required": ["dyspnea", "acute_onset"],
            "supporting": ["pleuritic_chest_pain", "hemoptysis", "syncope", "tachycardia", "unilateral_leg_swelling", "recent_immobility"],
            "contradictory": ["gradual_onset", "productive_cough"]
        },
        "demographics": {
            "age_risk": {"<40": 0.4, "40-70": 0.6, ">70": 0.7},
            "sex_risk": {"male": 1.0, "female": 1.2}
        },
        "risk_factors": ["recent_surgery", "immobility", "malignancy", "hypercoagulable", "OCP"],
        "specificity": 0.75,
        "urgency": "emergency",
        "rule_out_first": True,
        "workup": {
            "immediate": ["ECG", "D_dimer", "CXR", "ABG"],
            "within_6h": ["CT_PE"],
            "optional": ["Echo", "VQ_scan"]
        },
        "management_hints": "If high probability → Anticoagulation. Massive PE → Consider thrombolysis."
    },
    "Acute Heart Failure / Pulmonary Edema": {
        "symptoms": {
            "required": ["dyspnea", "acute_onset"],
            "supporting": ["orthopnea", "paroxysmal_nocturnal_dyspnea", "pink_frothy_sputum", "edema", "jugular_venous_distension", "crackles"],
            "contradictory": []
        },
        "demographics": {
            "age_risk": {"<40": 0.2, "40-70": 0.6, ">70": 0.8},
            "sex_risk": {"male": 1.1, "female": 1.0}
        },
        "risk_factors": ["CAD", "hypertension", "diabetes", "atrial_fibrillation", "valvular_disease"],
        "specificity": 0.70,
        "urgency": "emergency",
        "rule_out_first": True,
        "workup": {
            "immediate": ["CXR", "ECG", "BNP_NTproBNP", "Echo", "ABG"],
            "within_6h": [],
            "optional": []
        },
        "management_hints": "Diuretics. Oxygen. Nitrates if not hypotensive. Treat underlying cause."
    },
    "Severe Asthma / COPD Exacerbation": {
        "symptoms": {
            "required": ["dyspnea"],
            "supporting": ["wheezing", "cough", "chest_tightness", "history_asthma_copd", "triggers"],
            "contradictory": []
        },
        "demographics": {
            "age_risk": {"<40": 0.7, "40-70": 0.5, ">70": 0.4},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["asthma_history", "copd_history", "smoking", "allergies"],
        "specificity": 0.65,
        "urgency": "emergency",
        "rule_out_first": True,
        "workup": {
            "immediate": ["CXR", "ABG", "Peak_flow", "O2_saturation"],
            "within_6h": [],
            "optional": ["CBC", "Theophylline_level"]
        },
        "management_hints": "Bronchodilators. Steroids. Consider BiPAP if severe. Intubation if respiratory failure."
    },
    "Pneumonia": {
        "symptoms": {
            "required": ["dyspnea"],
            "supporting": ["fever", "productive_cough", "pleuritic_pain", "crackles", "consolidation"],
            "contradictory": []
        },
        "demographics": {
            "age_risk": {"<40": 0.5, "40-70": 0.6, ">70": 0.8},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["elderly", "immunocompromised", "comorbidities", "smoking"],
        "specificity": 0.60,
        "urgency": "urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["CXR", "CBC", "CRP", "Cultures"],
            "within_6h": [],
            "optional": ["CT_chest", "Blood_cultures"]
        },
        "management_hints": "Antibiotics based on severity (CURB-65, PSI). Supportive care."
    },
    "Anxiety / Hyperventilation": {
        "symptoms": {
            "required": ["dyspnea"],
            "supporting": ["anxiety", "panic", "paresthesia", "chest_tightness", "normal_exam", "normal_cxr"],
            "contradictory": ["crackles", "wheezing", "hypoxia"]
        },
        "demographics": {
            "age_risk": {"<40": 0.7, "40-70": 0.4, ">70": 0.2},
            "sex_risk": {"male": 0.8, "female": 1.2}
        },
        "risk_factors": ["anxiety_disorder", "panic_disorder", "stress"],
        "specificity": 0.50,
        "urgency": "non_urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["CXR", "ECG"],
            "within_6h": [],
            "optional": []
        },
        "management_hints": "Reassurance. Breathing exercises. Rule out organic causes first."
    }
}

ABDOMINAL_PAIN_DDX = {
    "Abdominal Aortic Aneurysm Rupture": {
        "symptoms": {
            "required": ["abdominal_pain", "severe"],
            "supporting": ["back_pain", "hypotension", "pulsatile_mass", "syncope"],
            "contradictory": []
        },
        "demographics": {
            "age_risk": {"<40": 0.1, "40-70": 0.5, ">70": 0.8},
            "sex_risk": {"male": 1.5, "female": 1.0}
        },
        "risk_factors": ["age>65", "male", "smoking", "hypertension", "family_history"],
        "specificity": 0.80,
        "urgency": "emergency",
        "rule_out_first": True,
        "workup": {
            "immediate": ["CT_angiography", "US_abdomen", "Type_crossmatch"],
            "within_6h": [],
            "optional": []
        },
        "management_hints": "SURGICAL EMERGENCY! Immediate vascular surgery consult. Resuscitation while preparing for OR."
    },
    "Appendicitis": {
        "symptoms": {
            "required": ["abdominal_pain"],
            "supporting": ["right_lower_quadrant", "migration_pain", "fever", "nausea", "rebound_tenderness", "mcburney_point"],
            "contradictory": []
        },
        "demographics": {
            "age_risk": {"<40": 0.7, "40-70": 0.3, ">70": 0.4},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": [],
        "specificity": 0.70,
        "urgency": "urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["CBC", "CT_abdomen", "US_abdomen"],
            "within_6h": [],
            "optional": []
        },
        "management_hints": "Surgery consult. Antibiotics pre-op. If perforated → Urgent surgery."
    },
    "Cholecystitis": {
        "symptoms": {
            "required": ["abdominal_pain"],
            "supporting": ["right_upper_quadrant", "fever", "positive_murphy", "nausea"],
            "contradictory": []
        },
        "demographics": {
            "age_risk": {"<40": 0.5, "40-70": 0.7, ">70": 0.6},
            "sex_risk": {"male": 0.8, "female": 1.2}
        },
        "risk_factors": ["female", "obesity", "age_40_plus"],
        "specificity": 0.65,
        "urgency": "urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["CBC", "LFT", "US_abdomen"],
            "within_6h": [],
            "optional": ["CT_abdomen"]
        },
        "management_hints": "Surgery consult. Antibiotics. Cholecystectomy within 24-48h."
    }
}

ALTERED_MENTAL_STATUS_DDX = {
    "Stroke": {
        "symptoms": {
            "required": ["altered_mental_status", "neurologic_deficit"],
            "supporting": ["focal_deficit", "aphasia", "hemiparesis", "facial_droop", "hypertension"],
            "contradictory": []
        },
        "demographics": {
            "age_risk": {"<40": 0.2, "40-70": 0.6, ">70": 0.8},
            "sex_risk": {"male": 1.1, "female": 1.0}
        },
        "risk_factors": ["hypertension", "diabetes", "atrial_fibrillation", "smoking"],
        "specificity": 0.80,
        "urgency": "emergency",
        "rule_out_first": True,
        "workup": {
            "immediate": ["CT_head", "ECG", "CBC", "PT_INR"],
            "within_6h": ["MRI", "CTA"],
            "optional": []
        },
        "management_hints": "TIME IS BRAIN! If ischemic < 4.5h → tPA. If < 24h → Consider thrombectomy."
    },
    "Intracranial Hemorrhage": {
        "symptoms": {
            "required": ["altered_mental_status", "headache"],
            "supporting": ["hypertension", "vomiting", "focal_deficit", "seizure"],
            "contradictory": []
        },
        "demographics": {
            "age_risk": {"<40": 0.3, "40-70": 0.6, ">70": 0.7},
            "sex_risk": {"male": 1.2, "female": 1.0}
        },
        "risk_factors": ["hypertension", "anticoagulation", "age", "trauma"],
        "specificity": 0.75,
        "urgency": "emergency",
        "rule_out_first": True,
        "workup": {
            "immediate": ["CT_head", "PT_INR", "aPTT"],
            "within_6h": [],
            "optional": []
        },
        "management_hints": "URGENT! Control BP. Reverse anticoagulation. Neurosurgery consult if indicated."
    },
    "Meningitis": {
        "symptoms": {
            "required": ["altered_mental_status", "fever"],
            "supporting": ["headache", "neck_stiffness", "photophobia", "rash", "nuchal_rigidity"],
            "contradictory": []
        },
        "demographics": {
            "age_risk": {"<40": 0.6, "40-70": 0.4, ">70": 0.5},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["age_very_young", "age_elderly", "immunocompromised"],
        "specificity": 0.70,
        "urgency": "emergency",
        "rule_out_first": True,
        "workup": {
            "immediate": ["LP", "Blood_cultures", "CT_head", "CBC", "Cultures"],
            "within_6h": [],
            "optional": []
        },
        "management_hints": "URGENT! Antibiotics BEFORE LP if delay. Dexamethasone if bacterial. CSF analysis critical."
    },
    "Sepsis": {
        "symptoms": {
            "required": ["altered_mental_status", "fever"],
            "supporting": ["hypotension", "tachycardia", "tachypnea", "source_infection", "hypothermia"],
            "contradictory": []
        },
        "demographics": {
            "age_risk": {"<40": 0.4, "40-70": 0.6, ">70": 0.8},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["elderly", "immunocompromised", "comorbidities", "recent_surgery"],
        "specificity": 0.65,
        "urgency": "emergency",
        "rule_out_first": True,
        "workup": {
            "immediate": ["Blood_cultures", "CBC", "Lactate", "Cultures", "CXR"],
            "within_6h": [],
            "optional": []
        },
        "management_hints": "SEPSIS PROTOCOL! 1-hour bundle. Antibiotics within 1h. Fluid resuscitation. Source control."
    },
    "Hypoglycemia": {
        "symptoms": {
            "required": ["altered_mental_status"],
            "supporting": ["diabetes", "sweating", "tremor", "agitation", "glucose_low"],
            "contradictory": []
        },
        "demographics": {
            "age_risk": {"<40": 0.5, "40-70": 0.6, ">70": 0.7},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["diabetes", "insulin", "sulfonylureas", "alcohol"],
        "specificity": 0.70,
        "urgency": "emergency",
        "rule_out_first": True,
        "workup": {
            "immediate": ["Glucose", "CBC", "CMP"],
            "within_6h": [],
            "optional": []
        },
        "management_hints": "Check glucose STAT! If low → D50 50ml IV. If conscious → PO glucose. Monitor glucose q1h."
    }
}

FEVER_DDX = {
    "Sepsis": {
        "symptoms": {
            "required": ["fever"],
            "supporting": ["hypotension", "tachycardia", "tachypnea", "altered_mental_status", "source_infection"],
            "contradictory": []
        },
        "demographics": {
            "age_risk": {"<40": 0.4, "40-70": 0.6, ">70": 0.8},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["elderly", "immunocompromised", "comorbidities"],
        "specificity": 0.70,
        "urgency": "emergency",
        "rule_out_first": True,
        "workup": {
            "immediate": ["Blood_cultures", "CBC", "Lactate", "Cultures", "CXR", "Urine_culture"],
            "within_6h": [],
            "optional": []
        },
        "management_hints": "SEPSIS PROTOCOL! 1-hour bundle. Antibiotics within 1h."
    },
    "Pneumonia": {
        "symptoms": {
            "required": ["fever", "cough"],
            "supporting": ["dyspnea", "productive_cough", "chest_pain", "crackles"],
            "contradictory": []
        },
        "demographics": {
            "age_risk": {"<40": 0.5, "40-70": 0.6, ">70": 0.8},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["elderly", "smoking", "comorbidities"],
        "specificity": 0.65,
        "urgency": "urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["CXR", "CBC", "CRP"],
            "within_6h": ["Blood_cultures", "Sputum_culture"],
            "optional": ["CT_chest"]
        },
        "management_hints": "Antibiotics based on severity (CURB-65, PSI). Community vs hospital acquired."
    },
    "UTI": {
        "symptoms": {
            "required": ["fever"],
            "supporting": ["dysuria", "frequency", "urgency", "suprapubic_pain", "flank_pain"],
            "contradictory": []
        },
        "demographics": {
            "age_risk": {"<40": 0.6, "40-70": 0.5, ">70": 0.7},
            "sex_risk": {"male": 0.5, "female": 1.5}
        },
        "risk_factors": ["female", "catheter", "elderly", "pregnancy"],
        "specificity": 0.60,
        "urgency": "urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["Urinalysis", "Urine_culture"],
            "within_6h": [],
            "optional": ["CBC", "CMP"]
        },
        "management_hints": "Antibiotics. If pyelonephritis → IV antibiotics. Consider imaging if complicated."
    },
    "Viral URI": {
        "symptoms": {
            "required": ["fever"],
            "supporting": ["rhinorrhea", "congestion", "sore_throat", "cough", "myalgia"],
            "contradictory": ["high_fever_prolonged", "severe_symptoms"]
        },
        "demographics": {
            "age_risk": {"<40": 0.7, "40-70": 0.5, ">70": 0.4},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": [],
        "specificity": 0.55,
        "urgency": "non_urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": [],
            "within_6h": [],
            "optional": ["CBC"]
        },
        "management_hints": "Supportive care. Usually self-limited. Rule out bacterial if high fever/prolonged."
    }
}

SYNCOPE_DDX = {
    "Arrhythmia": {
        "symptoms": {
            "required": ["syncope", "sudden"],
            "supporting": ["palpitations", "chest_pain", "history_arrhythmia", "heart_disease"],
            "contradictory": []
        },
        "demographics": {
            "age_risk": {"<40": 0.4, "40-70": 0.6, ">70": 0.7},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["CAD", "heart_failure", "history_arrhythmia", "structural_heart_disease"],
        "specificity": 0.75,
        "urgency": "emergency",
        "rule_out_first": True,
        "workup": {
            "immediate": ["ECG", "Telemetry", "Echo"],
            "within_6h": ["Holter", "Event_monitor"],
            "optional": ["EP_study"]
        },
        "management_hints": "URGENT! Continuous monitoring. If VT/VF → Defibrillation. Consider ICD if recurrent."
    },
    "Pulmonary Embolism": {
        "symptoms": {
            "required": ["syncope"],
            "supporting": ["dyspnea", "chest_pain", "tachycardia", "unilateral_leg_swelling", "recent_immobility"],
            "contradictory": []
        },
        "demographics": {
            "age_risk": {"<40": 0.4, "40-70": 0.6, ">70": 0.7},
            "sex_risk": {"male": 1.0, "female": 1.2}
        },
        "risk_factors": ["recent_surgery", "immobility", "malignancy", "hypercoagulable"],
        "specificity": 0.70,
        "urgency": "emergency",
        "rule_out_first": True,
        "workup": {
            "immediate": ["ECG", "D_dimer", "CXR", "CT_PE"],
            "within_6h": [],
            "optional": ["Echo"]
        },
        "management_hints": "If high probability → Anticoagulation. Massive PE → Consider thrombolysis."
    },
    "Vasovagal Syncope": {
        "symptoms": {
            "required": ["syncope"],
            "supporting": ["trigger", "prodrome", "nausea", "sweating", "pale", "young_age"],
            "contradictory": ["during_exertion", "no_prodrome", "older_age"]
        },
        "demographics": {
            "age_risk": {"<40": 0.8, "40-70": 0.4, ">70": 0.2},
            "sex_risk": {"male": 0.9, "female": 1.1}
        },
        "risk_factors": ["young_age", "anxiety", "stress"],
        "specificity": 0.60,
        "urgency": "non_urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["ECG"],
            "within_6h": [],
            "optional": ["Tilt_test"]
        },
        "management_hints": "Reassurance. Usually benign. Avoid triggers. Consider tilt test if recurrent."
    },
    "Orthostatic Hypotension": {
        "symptoms": {
            "required": ["syncope"],
            "supporting": ["on_standing", "dizziness", "medications", "dehydration", "elderly"],
            "contradictory": []
        },
        "demographics": {
            "age_risk": {"<40": 0.3, "40-70": 0.5, ">70": 0.8},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["elderly", "medications", "dehydration", "autonomic_dysfunction"],
        "specificity": 0.55,
        "urgency": "non_urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["Orthostatic_vitals", "ECG"],
            "within_6h": [],
            "optional": []
        },
        "management_hints": "Volume expansion. Review medications. Compression stockings. Head of bed elevation."
    }
}

# ========== JOINT PAIN DDX ==========
JOINT_PAIN_DDX = {
    "Septic Arthritis": {
        "symptoms": {
            "required": ["joint_pain", "joint_swelling"],
            "supporting": ["fever", "monoarthritis", "erythema", "warm_joint", "reduced_range_motion", "recent_joint_surgery"],
            "contradictory": ["polyarticular_symmetric", "morning_stiffness", "chronic_course"]
        },
        "demographics": {
            "age_risk": {"<20": 0.5, "20-50": 0.6, ">50": 0.7},
            "sex_risk": {"male": 1.1, "female": 1.0}
        },
        "risk_factors": ["diabetes", "IV_drug_use", "joint_surgery", "immunosuppression", "recent_bacteremia"],
        "specificity": 0.75,
        "urgency": "emergency",
        "rule_out_first": True,
        "workup": {
            "immediate": ["Joint_aspiration", "Synovial_WBC", "Gram_stain", "Blood_cultures", "ESR_CRP"],
            "within_6h": ["X_ray_joint"],
            "optional": ["MRI_joint"]
        },
        "management_hints": "URGENT! If fever + monoarthritis → Think SEPTIC immediately! Joint aspiration mandatory. Surgical drainage if required."
    },
    "Gout": {
        "symptoms": {
            "required": ["joint_pain", "joint_swelling"],
            "supporting": ["acute_onset", "first_metatarsophalangeal_mtp", "podagra", "erythema", "unilateral", "tophi", "hyperuricemia"],
            "contradictory": ["symmetric_joints", "morning_stiffness", "chronic_joint_deformity"]
        },
        "demographics": {
            "age_risk": {"<40": 0.4, "40-70": 0.8, ">70": 0.7},
            "sex_risk": {"male": 1.5, "female": 1.0}
        },
        "risk_factors": ["alcohol", "high_purine_diet", "diuretic_use", "obesity", "hypertension", "renal_disease"],
        "specificity": 0.70,
        "urgency": "urgent",
        "rule_out_first": True,
        "workup": {
            "immediate": ["Synovial_fluid_analysis", "Uric_acid", "ESR_CRP"],
            "within_6h": [],
            "optional": ["X_ray_joint"]
        },
        "management_hints": "NSAIDs or colchicine for acute attack. Allopurinol for prophylaxis. Check uric acid, but normal uric acid doesn't rule out gout."
    },
    "Rheumatoid Arthritis Flare": {
        "symptoms": {
            "required": ["joint_pain", "joint_swelling"],
            "supporting": ["morning_stiffness", "polyarticular_symmetric", "small_joints", "wrist_mcp_pip", "rheumatoid_factor", "chronic_course"],
            "contradictory": ["acute_monoarthritis", "first_mtp", "pseudogout_crystals"]
        },
        "demographics": {
            "age_risk": {"<40": 0.3, "40-70": 0.6, ">70": 0.4},
            "sex_risk": {"male": 1.0, "female": 2.5}
        },
        "risk_factors": ["family_history_ra", "smoking", "age_30_50"],
        "specificity": 0.65,
        "urgency": "urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["RF_CCP", "ESR_CRP", "X_ray_hands_feet"],
            "within_6h": [],
            "optional": ["US_joints", "MRI_joints"]
        },
        "management_hints": "If already diagnosed RA → Escalate DMARDs. If new presentation → Rheumatology consult for diagnosis and treatment."
    },
    "Pseudogout (CPPD)": {
        "symptoms": {
            "required": ["joint_pain", "joint_swelling"],
            "supporting": ["knee_wrist", "elderly", "chronic_kidney_disease", "hyperparathyroidism", "acute_onset", "calcification_joints"],
            "contradictory": ["first_mtp", "monosodium_urate"]
        },
        "demographics": {
            "age_risk": {"<40": 0.2, "40-70": 0.5, ">70": 0.8},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["elderly", "hypercalcemia", "hyperparathyroidism", "hemochromatosis", "hypomagnesemia"],
        "specificity": 0.60,
        "urgency": "urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["Synovial_fluid_analysis", "Calcium_Mg_PO4", "ESR_CRP"],
            "within_6h": [],
            "optional": ["X_ray_joint", "Parathyroid"]
        },
        "management_hints": "Similar to gout but different joints (knee > wrist). Calcium pyrophosphate crystals. Check calcium, Mg, PO4."
    },
    "Osteoarthritis": {
        "symptoms": {
            "required": ["joint_pain"],
            "supporting": ["chronic_course", "weight_bearing_joints", "knee_hip_spine", "worse_with_activity", "crepitus", "bone_spurs"],
            "contradictory": ["acute_onset", "fever", "systemic_symptoms", "morning_stiffness_prolonged"]
        },
        "demographics": {
            "age_risk": {"<40": 0.2, "40-70": 0.7, ">70": 0.9},
            "sex_risk": {"male": 1.0, "female": 1.2}
        },
        "risk_factors": ["age", "obesity", "joint_trauma", "repetitive_use", "genetics"],
        "specificity": 0.85,
        "urgency": "non_urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["X_ray_joint"],
            "within_6h": [],
            "optional": []
        },
        "management_hints": "Conservative: NSAIDs, exercise, weight loss. If severe → Joint injection or replacement. Usually self-limited."
    }
}

# ========== HEADACHE DDX ==========
HEADACHE_DDX = {
    "Subarachnoid Hemorrhage": {
        "symptoms": {
            "required": ["headache", "acute_severe_headache"],
            "supporting": ["thunderclap_headache", "worst_headache_life", "neck_stiffness", "photophobia", "nausea_vomiting", "decreased_consciousness"],
            "contradictory": ["chronic_gradual_onset", "tension_type"]
        },
        "demographics": {
            "age_risk": {"<40": 0.4, "40-70": 0.7, ">70": 0.6},
            "sex_risk": {"male": 1.0, "female": 1.3}
        },
        "risk_factors": ["hypertension", "smoking", "cocaine_use", "family_history_aneurysm", "polycystic_kidney"],
        "specificity": 0.75,
        "urgency": "emergency",
        "rule_out_first": True,
        "workup": {
            "immediate": ["CT_head", "LP_if_CT_negative", "ECG", "BP"],
            "within_6h": ["Angiography"],
            "optional": ["MRI"]
        },
        "management_hints": "URGENT! If thunderclap headache → Rule out SAH immediately. Even if CT negative, do LP. Neurosurgery consult if positive."
    },
    "Meningitis": {
        "symptoms": {
            "required": ["headache", "fever"],
            "supporting": ["neck_stiffness", "photophobia", "nausea_vomiting", "altered_mental_status", "rash", "decreased_consciousness"],
            "contradictory": ["chronic_gradual_onset", "no_fever", "no_neck_stiffness"]
        },
        "demographics": {
            "age_risk": {"<10": 0.7, "10-50": 0.6, ">50": 0.8},
            "sex_risk": {"male": 1.1, "female": 1.0}
        },
        "risk_factors": ["immunocompromised", "elderly", "young_children", "recent_URI", "bacterial_exposure"],
        "specificity": 0.70,
        "urgency": "emergency",
        "rule_out_first": True,
        "workup": {
            "immediate": ["LP", "Blood_cultures", "CT_head_before_LP", "CBC_chemistries"],
            "within_6h": ["Antibiotics_immediately"],
            "optional": ["CSF_cultures"]
        },
        "management_hints": "URGENT! If fever + headache + neck stiffness → Think MENINGITIS. Don't delay antibiotics for CT/LP. Treat empirically."
    },
    "Brain Tumor": {
        "symptoms": {
            "required": ["headache"],
            "supporting": ["new_onset_progressive", "worse_morning", "worse_coughing", "focal_neurologic_deficit", "seizures", "cognitive_changes", "papilledema"],
            "contradictory": ["acute_thunderclap", "paroxysmal", "chronic_benign"]
        },
        "demographics": {
            "age_risk": {"<20": 0.4, "20-60": 0.6, ">60": 0.8},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["age", "radiation_exposure", "family_history_cancer", "immunodeficiency"],
        "specificity": 0.65,
        "urgency": "emergency",
        "rule_out_first": True,
        "workup": {
            "immediate": ["CT_head", "Neurologic_exam"],
            "within_6h": ["MRI_with_contrast"],
            "optional": ["EEG"]
        },
        "management_hints": "If new progressive headache + neurologic symptoms → Image immediately. Neurosurgery consult if mass found."
    },
    "Migraine": {
        "symptoms": {
            "required": ["headache"],
            "supporting": ["unilateral", "throbbing_pulsating", "photophobia", "phonophobia", "nausea", "aura", "worse_with_activity", "family_history_migraine"],
            "contradictory": ["new_worst_headache", "fever", "neck_stiffness", "focal_deficit"]
        },
        "demographics": {
            "age_risk": {"<20": 0.3, "20-50": 0.7, ">50": 0.4},
            "sex_risk": {"male": 1.0, "female": 3.0}
        },
        "risk_factors": ["female", "family_history", "hormonal_changes", "stress", "certain_foods"],
        "specificity": 0.80,
        "urgency": "non_urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["Clinical_diagnosis"],
            "within_6h": [],
            "optional": ["CT_if_atypical"]
        },
        "management_hints": "Triptans for acute. Prophylaxis if frequent. R/O SAH if first episode or atypical. Usually no imaging needed."
    },
    "Tension Headache": {
        "symptoms": {
            "required": ["headache"],
            "supporting": ["bilateral", "tightness_pressure", "chronic_or_episodic", "worse_stress", "no_nausea", "mild_moderate"],
            "contradictory": ["acute_thunderclap", "aura", "photophobia_phonophobia", "worse_morning"]
        },
        "demographics": {
            "age_risk": {"<20": 0.5, "20-60": 0.7, ">60": 0.5},
            "sex_risk": {"male": 1.0, "female": 1.5}
        },
        "risk_factors": ["stress", "poor_posture", "sleep_deprivation"],
        "specificity": 0.85,
        "urgency": "non_urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["Clinical_diagnosis"],
            "within_6h": [],
            "optional": []
        },
        "management_hints": "Conservative: NSAIDs, rest, stress management. Usually benign. R/O serious causes if new or changing pattern."
    },
    "Cluster Headache": {
        "symptoms": {
            "required": ["headache"],
            "supporting": ["strictly_unilateral", "orbital_temporal", "severe_excruciating", "autonomic_symptoms", "ipsilateral_tearing", "rhinorrhea", "frequent_brief_attacks"],
            "contradictory": ["bilateral", "chronic_daily", "mild_moderate"]
        },
        "demographics": {
            "age_risk": {"<20": 0.3, "20-60": 0.8, ">60": 0.4},
            "sex_risk": {"male": 3.0, "female": 1.0}
        },
        "risk_factors": ["male", "smoking", "alcohol"],
        "specificity": 0.75,
        "urgency": "non_urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["Clinical_diagnosis"],
            "within_6h": [],
            "optional": ["CT_if_atypical"]
        },
        "management_hints": "O2 or triptans for acute. Verapamil for prophylaxis. Very severe but usually no serious pathology."
    }
}

# ========== DIARRHEA DDX ==========
DIARRHEA_DDX = {
    "Infectious Diarrhea": {
        "symptoms": {
            "required": ["diarrhea"],
            "supporting": ["acute_onset", "fever", "abdominal_cramps", "bloody_stools", "nausea_vomiting", "recent_food_exposure", "watery_diarrhea"],
            "contradictory": ["chronic_course", "weight_loss", "iron_deficiency_anemia"]
        },
        "demographics": {
            "age_risk": {"<10": 0.8, "10-65": 0.6, ">65": 0.7},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["recent_travel", "food_contamination", "immunocompromised", "recent_antibiotics"],
        "specificity": 0.70,
        "urgency": "urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["Stool_culture", "Stool_O_P", "CBC_chemistries"],
            "within_6h": ["C_diff_toxin"],
            "optional": ["Blood_cultures"]
        },
        "management_hints": "Supportive care. Antibiotics only if severe or specific pathogens. Check for dehydration. Consider C. diff if recent antibiotics."
    },
    "Clostridium difficile Colitis": {
        "symptoms": {
            "required": ["diarrhea"],
            "supporting": ["recent_antibiotics", "watery_diarrhea", "abdominal_cramps", "fever", "leukocytosis", "hospital_stay"],
            "contradictory": ["chronic_weight_loss", "iron_deficiency"]
        },
        "demographics": {
            "age_risk": {"<40": 0.3, "40-70": 0.6, ">70": 0.9},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["recent_antibiotics", "hospital_stay", "elderly", "immunosuppression", "PPI_use"],
        "specificity": 0.75,
        "urgency": "urgent",
        "rule_out_first": True,
        "workup": {
            "immediate": ["C_diff_toxin", "CBC_with_diff", "Lactate"],
            "within_6h": ["CT_abdomen_if_severe"],
            "optional": ["Metronidazole_or_vancomycin"]
        },
        "management_hints": "URGENT! If recent antibiotics + diarrhea → Check C. diff immediately. Metronidazole or vancomycin. Isolate patient. Check for toxic megacolon."
    },
    "Inflammatory Bowel Disease": {
        "symptoms": {
            "required": ["diarrhea", "chronic_course"],
            "supporting": ["bloody_stools", "abdominal_pain", "weight_loss", "fatigue", "fever", "family_history_ibd", "extraintestinal_manifestations"],
            "contradictory": ["acute_onset", "self_limiting"]
        },
        "demographics": {
            "age_risk": {"<20": 0.2, "20-40": 0.7, ">40": 0.5},
            "sex_risk": {"male": 1.0, "female": 1.1}
        },
        "risk_factors": ["family_history", "smoking", "age_15_30"],
        "specificity": 0.75,
        "urgency": "urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["Colonoscopy", "CRP_ESR", "Calprotectin", "FBC"],
            "within_6h": [],
            "optional": ["CT_or_MRI_abdomen", "Small_bowel_series"]
        },
        "management_hints": "If chronic diarrhea + weight loss + bleeding → Refer gastroenterology. Colonoscopy mandatory. Start immunosuppression if severe."
    },
    "Irritable Bowel Syndrome": {
        "symptoms": {
            "required": ["diarrhea", "chronic_course"],
            "supporting": ["alternating_constipation_diarrhea", "abdominal_bloating", "relieved_by_defecation", "mucus_in_stool", "stress_related"],
            "contradictory": ["fever", "weight_loss", "bloody_stools", "night_symptoms"]
        },
        "demographics": {
            "age_risk": {"<20": 0.3, "20-50": 0.7, ">50": 0.4},
            "sex_risk": {"male": 1.0, "female": 1.5}
        },
        "risk_factors": ["female", "stress", "anxiety", "depression"],
        "specificity": 0.80,
        "urgency": "non_urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["Clinical_diagnosis_Rome_criteria"],
            "within_6h": [],
            "optional": ["Colonoscopy_if_alarm_symptoms"]
        },
        "management_hints": "Diagnosis of exclusion. Rome criteria. Dietary changes, stress management. Reassurance. R/O organic causes if red flags."
    }
}

# ========== ANEMIA DDX ==========
ANEMIA_DDX = {
    "Iron Deficiency Anemia": {
        "symptoms": {
            "required": ["anemia", "microcytic_hypochromic"],
            "supporting": ["fatigue", "pallor", "pica", "brittle_nails", "hair_loss", "cheilosis", "blood_loss"],
            "contradictory": ["macrocytic", "elevated_ferritin", "elevated_iron"]
        },
        "demographics": {
            "age_risk": {"<10": 0.5, "10-50": 0.4, ">50": 0.8},
            "sex_risk": {"male": 1.0, "female": 2.0}
        },
        "risk_factors": ["menstrual_blood_loss", "GI_bleeding", "pregnancy", "malabsorption", "dietary_insufficiency"],
        "specificity": 0.85,
        "urgency": "urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["FBC", "Iron_studies", "Ferritin", "TIBC"],
            "within_6h": [],
            "optional": ["Colonoscopy", "Upper_GI_endoscopy", "Occult_blood_stool"]
        },
        "management_hints": "Iron replacement. Investigate source of blood loss (especially GI in elderly). Check dietary intake in children."
    },
    "Vitamin B12/Folate Deficiency": {
        "symptoms": {
            "required": ["anemia", "macrocytic_megaloblastic"],
            "supporting": ["glossitis", "neurologic_symptoms", "neuropathy", "dementia", "dietary_deficiency", "malabsorption"],
            "contradictory": ["microcytic", "normal_b12_folate"]
        },
        "demographics": {
            "age_risk": {"<40": 0.3, "40-70": 0.7, ">70": 0.8},
            "sex_risk": {"male": 1.0, "female": 1.2}
        },
        "risk_factors": ["elderly", "vegetarian_vegan", "gastric_surgery", "Crohn_disease", "medications"],
        "specificity": 0.75,
        "urgency": "urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["FBC", "B12_Folate_levels", "Methylmalonic_acid"],
            "within_6h": [],
            "optional": ["Schilling_test"]
        },
        "management_hints": "Replace deficiencies. B12 injections if severe deficiency or malabsorption. Check for pernicious anemia (intrinsic factor antibodies)."
    },
    "Hemolytic Anemia": {
        "symptoms": {
            "required": ["anemia"],
            "supporting": ["jaundice", "elevated_reticulocytes", "elevated_ldh", "decreased_haptoglobin", "dark_urine", "splenomegaly"],
            "contradictory": ["low_reticulocytes", "normal_ldh"]
        },
        "demographics": {
            "age_risk": {"<20": 0.5, "20-60": 0.4, ">60": 0.5},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["autoimmune", "medications", "infections", "mechanical_valve", "thalassemia", "sickle_cell"],
        "specificity": 0.70,
        "urgency": "urgent",
        "rule_out_first": True,
        "workup": {
            "immediate": ["FBC", "Reticulocytes", "LDH", "Haptoglobin", "Coombs_test", "Bilirubin"],
            "within_6h": [],
            "optional": ["Hemoglobin_electrophoresis"]
        },
        "management_hints": "URGENT! If sudden hemolysis → Check Coombs. Stop offending medications. Consider steroids for autoimmune. Monitor closely."
    }
}

# ========== KIDNEY INJURY DDX ==========
KIDNEY_INJURY_DDX = {
    "Acute Kidney Injury (Prerenal)": {
        "symptoms": {
            "required": ["acute_kidney_injury", "increased_creatinine"],
            "supporting": ["dehydration", "hypotension", "reduced_urine_output", "volume_depletion", "congestive_heart_failure", "liver_disease"],
            "contradictory": ["nephritic_sediment", "proteinuria_heavy", "casts"]
        },
        "demographics": {
            "age_risk": {"<40": 0.3, "40-70": 0.6, ">70": 0.8},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["dehydration", "heart_failure", "liver_disease", "sepsis", "hypotension", "medications"],
        "specificity": 0.75,
        "urgency": "emergency",
        "rule_out_first": True,
        "workup": {
            "immediate": ["Creatinine_eGFR", "Urinalysis", "FENa", "FeUrea", "CBC", "Electrolytes"],
            "within_6h": ["Renal_US"],
            "optional": []
        },
        "management_hints": "URGENT! If volume depleted → Fluids. Treat underlying cause (HF, sepsis, etc.). FENa <1% suggests prerenal."
    },
    "Acute Tubular Necrosis": {
        "symptoms": {
            "required": ["acute_kidney_injury", "increased_creatinine"],
            "supporting": ["ischemia", "nephrotoxins", "contrast_induced", "myoglobinuria", "pigmented_granular_casts", "FENa_>1"],
            "contradictory": ["prerenal_FENa", "nephritic_urine"]
        },
        "demographics": {
            "age_risk": {"<40": 0.3, "40-70": 0.7, ">70": 0.9},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["ischemia", "sepsis", "contrast", "aminoglycosides", "myoglobin", "hypotension"],
        "specificity": 0.70,
        "urgency": "emergency",
        "rule_out_first": True,
        "workup": {
            "immediate": ["Creatinine_eGFR", "Urinalysis", "FENa", "CK_if_rhabdo", "Urine_microscopy"],
            "within_6h": ["Renal_US"],
            "optional": []
        },
        "management_hints": "URGENT! Supportive care. R/O cause (contrast, meds, rhabdo). Usually reversible. Consider dialysis if severe."
    },
    "Post-Renal Obstruction": {
        "symptoms": {
            "required": ["acute_kidney_injury", "increased_creatinine"],
            "supporting": ["reduced_urine_output", "hesitancy", "frequency", "dribbling", "flank_pain", "hydronephrosis"],
            "contradictory": ["normal_urine_output", "no_obstruction_imaging"]
        },
        "demographics": {
            "age_risk": {"<40": 0.4, "40-70": 0.7, ">70": 0.8},
            "sex_risk": {"male": 1.2, "female": 1.0}
        },
        "risk_factors": ["BPH", "prostate_cancer", "nephrolithiasis", "tumors", "strictures"],
        "specificity": 0.75,
        "urgency": "emergency",
        "rule_out_first": True,
        "workup": {
            "immediate": ["Creatinine_eGFR", "Renal_US", "Post_void_residual"],
            "within_6h": ["CT_abdomen_pelvis", "Urology_consult"],
            "optional": []
        },
        "management_hints": "URGENT! Catheterize immediately if retention. US to confirm obstruction. Urology consult. Relief of obstruction usually curative."
    },
    "Glomerulonephritis": {
        "symptoms": {
            "required": ["acute_kidney_injury", "increased_creatinine"],
            "supporting": ["proteinuria", "hematuria", "hypertension", "edema", "hypocomplementemia", "nephritic_sediment", "RBC_casts"],
            "contradictory": ["no_proteinuria", "no_casts"]
        },
        "demographics": {
            "age_risk": {"<20": 0.5, "20-60": 0.6, ">60": 0.4},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["infections", "autoimmune_diseases", "medications", "malignancy"],
        "specificity": 0.70,
        "urgency": "emergency",
        "rule_out_first": True,
        "workup": {
            "immediate": ["Urinalysis", "UPCR", "C3_C4", "ANA_dsDNA", "ANCA", "Anti_GBM"],
            "within_6h": ["Renal_biopsy"],
            "optional": []
        },
        "management_hints": "URGENT! Nephrology consult immediately. Biopsy if severe. High-dose steroids + immunosuppression usually indicated."
    }
}

# ========== HTN EMERGENCY DDX ==========
HTN_EMERGENCY_DDX = {
    "Hypertensive Crisis": {
        "symptoms": {
            "required": ["severe_hypertension", "SBP_>180_or_DBP_>120"],
            "supporting": ["chest_pain", "dyspnea", "severe_headache", "altered_mental_status", "visual_changes", "nausea_vomiting"],
            "contradictory": ["normal_bp", "asymptomatic_controlled"]
        },
        "demographics": {
            "age_risk": {"<40": 0.5, "40-70": 0.8, ">70": 0.9},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["preexisting_htn", "noncompliance_meds", "new_meds", "cocaine_use", "pregnancy"],
        "specificity": 0.80,
        "urgency": "emergency",
        "rule_out_first": True,
        "workup": {
            "immediate": ["BP_monitoring", "ECG", "Chest_X_ray", "CBC_chemistries", "Urinalysis"],
            "within_6h": ["Echo", "Head_CT"],
            "optional": ["Renal_US"]
        },
        "management_hints": "URGENT! Lower BP gradually (25% in 1h, then target over 2-6h). IV agents. R/O end-organ damage. Labetalol, nicardipine, or nitroprusside."
    },
    "Renal Emergency": {
        "symptoms": {
            "required": ["severe_hypertension"],
            "supporting": ["acute_kidney_injury", "oliguria", "flank_pain", "hematuria", "elevated_creatinine"],
            "contradictory": ["normal_creatinine", "normal_urine_output"]
        },
        "demographics": {
            "age_risk": {"<40": 0.5, "40-70": 0.8, ">70": 0.9},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["preexisting_ckd", "renal_artery_stenosis", "autoimmune_vasculitis"],
        "specificity": 0.75,
        "urgency": "emergency",
        "rule_out_first": True,
        "workup": {
            "immediate": ["Creatinine_eGFR", "Urinalysis", "Renal_US", "Urine_sediment"],
            "within_6h": ["Renal_biopsy_if_needed"],
            "optional": ["Renal_angiography"]
        },
        "management_hints": "URGENT! Nephrology consult. Lower BP carefully. May need dialysis if severe AKI. Check for renal artery stenosis or glomerulonephritis."
    },
    "Stroke (Hemorrhagic)": {
        "symptoms": {
            "required": ["severe_hypertension", "neurologic_deficit"],
            "supporting": ["sudden_onset", "severe_headache", "nausea_vomiting", "altered_consciousness", "focal_neurologic_signs"],
            "contradictory": ["normal_exam", "no_neurologic_findings"]
        },
        "demographics": {
            "age_risk": {"<40": 0.4, "40-70": 0.8, ">70": 0.9},
            "sex_risk": {"male": 1.1, "female": 1.0}
        },
        "risk_factors": ["hypertension", "anticoagulation", "AVM", "cocaine_use", "amyloid_angiopathy"],
        "specificity": 0.75,
        "urgency": "emergency",
        "rule_out_first": True,
        "workup": {
            "immediate": ["Head_CT", "Neurologic_exam", "Coagulation_studies"],
            "within_6h": ["MRI_if_needed", "Neurosurgery_consult"],
            "optional": []
        },
        "management_hints": "URGENT! Don't lower BP too fast if large bleed. Neurosurgery consult. Reverse anticoagulation if bleeding. Monitor ICP."
    }
}

# ========== VOMITING DDX ==========
VOMITING_DDX = {
    "Intestinal Obstruction": {
        "symptoms": {
            "required": ["vomiting", "abdominal_distension"],
            "supporting": ["absent_bowel_sounds", "constipation", "abdominal_pain", "bilious_vomiting", "high_pitched_bowel_sounds", "previous_surgery"],
            "contradictory": ["diarrhea", "normal_bowel_sounds", "flatus"]
        },
        "demographics": {
            "age_risk": {"<40": 0.4, "40-70": 0.7, ">70": 0.9},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["previous_surgery", "hernia", "tumors", "adhesions"],
        "specificity": 0.80,
        "urgency": "emergency",
        "rule_out_first": True,
        "workup": {
            "immediate": ["Abdominal_XR", "CBC_chemistries", "Abdominal_exam"],
            "within_6h": ["CT_abdomen_pelvis"],
            "optional": []
        },
        "management_hints": "URGENT! NPO. NG tube. Surgical consult. Don't give laxatives. Check for hernias. May need surgery."
    },
    "Acute Pancreatitis": {
        "symptoms": {
            "required": ["vomiting", "abdominal_pain"],
            "supporting": ["epigastric_pain", "radiating_back", "worse_lying_supine", "gallstones", "alcohol", "elevated_lipase_amylase"],
            "contradictory": ["no_abdominal_pain", "normal_enzymes"]
        },
        "demographics": {
            "age_risk": {"<40": 0.5, "40-70": 0.7, ">70": 0.6},
            "sex_risk": {"male": 1.2, "female": 1.0}
        },
        "risk_factors": ["gallstones", "alcohol", "hypertriglyceridemia", "ERCP", "trauma"],
        "specificity": 0.85,
        "urgency": "emergency",
        "rule_out_first": True,
        "workup": {
            "immediate": ["Lipase_amylase", "CT_abdomen", "CBC_chemistries", "Lactate"],
            "within_6h": ["ERCP_if_galstones"],
            "optional": []
        },
        "management_hints": "URGENT! NPO, IV fluids, pain control. Check lipase (>3x normal). Calculate BISAP or Ranson score. ICU if severe."
    },
    "Gastroenteritis": {
        "symptoms": {
            "required": ["vomiting", "diarrhea"],
            "supporting": ["nausea", "fever", "abdominal_cramps", "recent_food_exposure", "multiple_patients"],
            "contradictory": ["no_diarrhea", "chronic_symptoms"]
        },
        "demographics": {
            "age_risk": {"<10": 0.9, "10-65": 0.6, ">65": 0.8},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["food_contamination", "immunocompromised", "travel"],
        "specificity": 0.75,
        "urgency": "urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["CBC_chemistries", "Stool_culture"],
            "within_6h": [],
            "optional": []
        },
        "management_hints": "Supportive care. Hydration. Usually self-limited. Check for dehydration. Antiemetics if severe."
    },
    "Metabolic Acidosis": {
        "symptoms": {
            "required": ["vomiting"],
            "supporting": ["hyperglycemia", "ketosis", "DKA", "altered_mental_status", "Kussmaul_breathing", "polyuria"],
            "contradictory": ["normal_glucose", "normal_acid_base"]
        },
        "demographics": {
            "age_risk": {"<40": 0.5, "40-70": 0.8, ">70": 0.9},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["diabetes", "alcohol", "infection"],
        "specificity": 0.70,
        "urgency": "emergency",
        "rule_out_first": True,
        "workup": {
            "immediate": ["Glucose", "ABG", "Ketones", "Electrolytes"],
            "within_6h": ["Insulin_protocol"],
            "optional": []
        },
        "management_hints": "URGENT! If DKA → Insulin drip + fluids. Monitor electrolytes closely. Check for underlying infection."
    }
}

# ========== RASH DDX ==========
RASH_DDX = {
    "Drug Reaction": {
        "symptoms": {
            "required": ["rash"],
            "supporting": ["recent_medications", "maculopapular", "generalized", "pruritic", "fever", "eosinophilia", "timing_related_to_drug"],
            "contradictory": ["target_lesions", "bulla", "scleral_involvement"]
        },
        "demographics": {
            "age_risk": {"<40": 0.5, "40-70": 0.7, ">70": 0.8},
            "sex_risk": {"male": 1.0, "female": 1.2}
        },
        "risk_factors": ["multiple_medications", "specific_drugs", "prior_reactions"],
        "specificity": 0.75,
        "urgency": "urgent",
        "rule_out_first": True,
        "workup": {
            "immediate": ["CBC", "Drug_history", "Stop_suspected_drugs"],
            "within_6h": ["Skin_biopsy_if_severe"],
            "optional": []
        },
        "management_hints": "URGENT! Stop suspected medications immediately. Antihistamines. Steroids if severe. R/O SJS/TEN if severe (target lesions, bullae)."
    },
    "Stevens-Johnson Syndrome / TEN": {
        "symptoms": {
            "required": ["rash"],
            "supporting": ["target_lesions", "bulla", "detachment", "mucosal_involvement", "fever", "drug_exposure", "toxic_epidermal_necrolysis"],
            "contradictory": ["maculopapular", "localized"]
        },
        "demographics": {
            "age_risk": {"<40": 0.5, "40-70": 0.8, ">70": 0.7},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["drugs", "infections", "genetic_factors"],
        "specificity": 0.70,
        "urgency": "emergency",
        "rule_out_first": True,
        "workup": {
            "immediate": ["Stop_all_drugs", "ICU_admit", "Dermatology_consult", "Hydration"],
            "within_6h": ["Skin_biopsy"],
            "optional": []
        },
        "management_hints": "URGENT! Life-threatening! ICU immediately. Stop all drugs. Dermatology + burn unit. Supportive care. High mortality if >30% BSA."
    },
    "Meningococcal Sepsis": {
        "symptoms": {
            "required": ["rash", "fever"],
            "supporting": ["petechial_purpura", "rapidly_spreading", "unwell_patient", "neck_stiffness", "septic_shock", "meningitis"],
            "contradictory": ["stable_patient", "localized_rash"]
        },
        "demographics": {
            "age_risk": {"<10": 0.8, "10-30": 0.7, ">30": 0.3},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["young_age", "dormitory_living", "asplenia"],
        "specificity": 0.75,
        "urgency": "emergency",
        "rule_out_first": True,
        "workup": {
            "immediate": ["Blood_cultures", "LP", "Antibiotics_immediately", "Isolation"],
            "within_6h": ["Close_contacts_prophylaxis"],
            "optional": []
        },
        "management_hints": "URGENT! Life-threatening! Don't delay antibiotics. Treat empirically with ceftriaxone. Isolate. Notify public health. Prophylaxis for contacts."
    },
    "Atopic Dermatitis / Eczema": {
        "symptoms": {
            "required": ["rash"],
            "supporting": ["pruritic", "flexural_distribution", "chronic_recurrent", "atopy", "family_history", "xerosis"],
            "contradictory": ["acute_severe", "fever", "systemic_symptoms"]
        },
        "demographics": {
            "age_risk": {"<10": 0.8, "10-40": 0.5, ">40": 0.3},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["atopy", "family_history", "allergies"],
        "specificity": 0.85,
        "urgency": "non_urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["Clinical_diagnosis"],
            "within_6h": [],
            "optional": ["Patch_testing"]
        },
        "management_hints": "Moisturizers, topical steroids, avoid triggers. Usually chronic. Refer dermatology if severe or unresponsive."
    }
}

# Cough (Ho)
COUGH_DDX = {
    "Community Acquired Pneumonia (CAP)": {
        "symptoms": {
            "required": ["cough"],
            "supporting": ["productive_cough", "fever", "dyspnea", "chest_pain", "sputum_purulent", "chills", "malaise"],
            "contradictory": ["chronic_cough", "no_fever", "no_sputum"]
        },
        "demographics": {
            "age_risk": {"<5": 0.6, "5-65": 0.5, ">65": 0.8},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["age_>65", "smoking", "COPD", "immunocompromised", "nursing_home", "alcoholism"],
        "specificity": 0.75,
        "urgency": "urgent",
        "rule_out_first": True,
        "workup": {
            "immediate": ["CXR", "CBC", "CRP", "Blood_cultures"],
            "within_6h": ["Sputum_culture", "ABG_if_severe"],
            "optional": ["Procalcitonin", "CT_chest"]
        },
        "management_hints": "CURB-65 score for severity. If CURB-65 ≥2 → Hospital admission. Empiric antibiotics: Amoxicillin-clavulanate or Azithromycin. If severe → Ceftriaxone + Azithromycin."
    },
    "COPD Exacerbation": {
        "symptoms": {
            "required": ["cough", "chronic_cough"],
            "supporting": ["productive_cough", "increased_sputum", "dyspnea", "wheeze", "history_copd", "smoking_history"],
            "contradictory": ["acute_onset", "no_smoking_history", "young_age"]
        },
        "demographics": {
            "age_risk": {"<40": 0.2, "40-70": 0.7, ">70": 0.8},
            "sex_risk": {"male": 1.3, "female": 1.0}
        },
        "risk_factors": ["smoking", "age", "occupational_exposure", "alpha1_antitrypsin_deficiency"],
        "specificity": 0.80,
        "urgency": "urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["CXR", "ABG", "PEFR", "CBC"],
            "within_6h": ["Sputum_culture", "ECG"],
            "optional": ["CT_chest", "Echo"]
        },
        "management_hints": "Bronchodilators (SABA + LABA). Systemic steroids. Antibiotics if purulent sputum. O2 to target SpO2 88-92%. Consider NIV if hypercapnic."
    },
    "Congestive Heart Failure (CHF)": {
        "symptoms": {
            "required": ["cough", "dyspnea"],
            "supporting": ["orthopnea", "paroxysmal_nocturnal_dyspnea", "edema", "fatigue", "weight_gain", "jugular_venous_distension"],
            "contradictory": ["no_dyspnea", "no_edema"]
        },
        "demographics": {
            "age_risk": {"<40": 0.2, "40-70": 0.6, ">70": 0.8},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["hypertension", "CAD", "diabetes", "valvular_disease", "cardiomyopathy"],
        "specificity": 0.70,
        "urgency": "urgent",
        "rule_out_first": True,
        "workup": {
            "immediate": ["CXR", "BNP_NT_proBNP", "ECG", "Echo"],
            "within_6h": ["Troponin", "Electrolytes"],
            "optional": ["CT_chest"]
        },
        "management_hints": "Diuretics (furosemide). ACE-I/ARB. Beta-blockers if stable. O2. If severe → NIV or intubation. Treat underlying cause."
    },
    "Asthma": {
        "symptoms": {
            "required": ["cough"],
            "supporting": ["wheeze", "dyspnea", "chest_tightness", "nocturnal_symptoms", "exercise_induced", "atopy", "family_history"],
            "contradictory": ["chronic_productivity", "smoking_history_long"]
        },
        "demographics": {
            "age_risk": {"<20": 0.7, "20-50": 0.6, ">50": 0.4},
            "sex_risk": {"male": 1.0, "female": 1.2}
        },
        "risk_factors": ["atopy", "family_history", "allergies", "viral_infections"],
        "specificity": 0.75,
        "urgency": "urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["PEFR", "CXR", "O2_saturation"],
            "within_6h": ["ABG_if_severe", "Spirometry"],
            "optional": ["Allergy_testing"]
        },
        "management_hints": "SABA (salbutamol). Systemic steroids if moderate-severe. O2. If severe → IV magnesium, consider intubation. Long-term: ICS + LABA."
    },
    "GERD": {
        "symptoms": {
            "required": ["cough"],
            "supporting": ["heartburn", "regurgitation", "worse_lying_down", "worse_after_meals", "chronic_cough", "hoarseness", "nocturnal_cough"],
            "contradictory": ["fever", "productive_cough", "dyspnea"]
        },
        "demographics": {
            "age_risk": {"<40": 0.4, "40-70": 0.6, ">70": 0.5},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["obesity", "pregnancy", "hiatal_hernia", "smoking", "alcohol"],
        "specificity": 0.70,
        "urgency": "non_urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["Clinical_diagnosis"],
            "within_6h": [],
            "optional": ["Upper_endoscopy", "pH_monitoring"]
        },
        "management_hints": "PPI trial (omeprazole 40mg BID). Lifestyle: Elevate head, avoid late meals, weight loss. If persistent → Endoscopy."
    },
    "Post-nasal Drip": {
        "symptoms": {
            "required": ["cough"],
            "supporting": ["nasal_congestion", "rhinorrhea", "throat_clearing", "chronic_cough", "worse_lying_down", "allergic_symptoms"],
            "contradictory": ["fever", "productive_cough", "dyspnea"]
        },
        "demographics": {
            "age_risk": {"<40": 0.5, "40-70": 0.6, ">70": 0.4},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["allergies", "sinusitis", "rhinitis"],
        "specificity": 0.65,
        "urgency": "non_urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["Clinical_diagnosis"],
            "within_6h": [],
            "optional": ["Sinus_CT", "Allergy_testing"]
        },
        "management_hints": "Nasal steroids. Antihistamines. Nasal irrigation. Treat underlying rhinitis/sinusitis."
    }
}

# Bleeding (Chảy Máu)
BLEEDING_DDX = {
    "Upper GI Bleeding": {
        "symptoms": {
            "required": ["bleeding"],
            "supporting": ["hematemesis", "melena", "coffee_ground_vomiting", "abdominal_pain", "dizziness", "syncope", "hypotension"],
            "contradictory": ["hematochezia_only", "no_hematemesis_melena"]
        },
        "demographics": {
            "age_risk": {"<40": 0.3, "40-70": 0.6, ">70": 0.8},
            "sex_risk": {"male": 1.2, "female": 1.0}
        },
        "risk_factors": ["NSAIDs", "alcohol", "peptic_ulcer", "varices", "anticoagulants"],
        "specificity": 0.85,
        "urgency": "emergency",
        "rule_out_first": True,
        "workup": {
            "immediate": ["CBC", "Coagulation", "Type_cross", "IV_access", "EGD"],
            "within_6h": ["EGD_with_intervention"],
            "optional": ["CT_angiography"]
        },
        "management_hints": "URGENT! Resuscitate first (IV fluids, blood if needed). PPI (omeprazole 80mg IV). If varices → Octreotide. EGD within 24h. Rockall/Blatchford score."
    },
    "Lower GI Bleeding": {
        "symptoms": {
            "required": ["bleeding"],
            "supporting": ["hematochezia", "bright_red_blood", "abdominal_pain", "dizziness", "syncope"],
            "contradictory": ["hematemesis", "melena_only"]
        },
        "demographics": {
            "age_risk": {"<40": 0.3, "40-70": 0.6, ">70": 0.7},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["diverticulosis", "angiodysplasia", "colitis", "polyps", "anticoagulants"],
        "specificity": 0.75,
        "urgency": "emergency",
        "rule_out_first": True,
        "workup": {
            "immediate": ["CBC", "Coagulation", "Type_cross", "IV_access"],
            "within_6h": ["Colonoscopy", "CT_angiography"],
            "optional": ["Tagged_RBC_scan"]
        },
        "management_hints": "Resuscitate. Most stop spontaneously. Colonoscopy if stable. If massive → CT angiography → embolization. Surgery if refractory."
    },
    "Hemoptysis": {
        "symptoms": {
            "required": ["bleeding", "cough"],
            "supporting": ["bloody_sputum", "hemoptysis", "dyspnea", "chest_pain", "fever", "weight_loss"],
            "contradictory": ["hematemesis", "no_cough"]
        },
        "demographics": {
            "age_risk": {"<40": 0.4, "40-70": 0.6, ">70": 0.7},
            "sex_risk": {"male": 1.2, "female": 1.0}
        },
        "risk_factors": ["smoking", "TB", "lung_cancer", "bronchiectasis", "anticoagulants"],
        "specificity": 0.80,
        "urgency": "emergency",
        "rule_out_first": True,
        "workup": {
            "immediate": ["CXR", "CBC", "Coagulation", "Chest_CT"],
            "within_6h": ["Bronchoscopy"],
            "optional": ["CT_angiography"]
        },
        "management_hints": "URGENT if massive (>500ml/24h). Position patient (bleeding side down). O2. If massive → Intubation, bronchoscopy, embolization. Treat underlying cause."
    },
    "Hematuria": {
        "symptoms": {
            "required": ["bleeding"],
            "supporting": ["bloody_urine", "hematuria", "dysuria", "frequency", "flank_pain", "colicky_pain"],
            "contradictory": ["no_urinary_symptoms"]
        },
        "demographics": {
            "age_risk": {"<40": 0.4, "40-70": 0.6, ">70": 0.7},
            "sex_risk": {"male": 1.2, "female": 1.0}
        },
        "risk_factors": ["UTI", "stones", "malignancy", "glomerulonephritis", "anticoagulants"],
        "specificity": 0.75,
        "urgency": "urgent",
        "rule_out_first": True,
        "workup": {
            "immediate": ["Urinalysis", "Urine_culture", "CBC", "Creatinine"],
            "within_6h": ["CT_KUB", "Cystoscopy"],
            "optional": ["Renal_biopsy"]
        },
        "management_hints": "If >40 years → Full urologic workup (CT, cystoscopy) to rule out malignancy. If <40 + UTI → Treat UTI first. If glomerular → Nephrology consult."
    },
    "Menorrhagia": {
        "symptoms": {
            "required": ["bleeding"],
            "supporting": ["heavy_menstrual_bleeding", "prolonged_periods", "anemia", "fatigue", "clots"],
            "contradictory": ["male", "no_menstrual_history"]
        },
        "demographics": {
            "age_risk": {"<20": 0.4, "20-50": 0.7, ">50": 0.5},
            "sex_risk": {"male": 0.0, "female": 1.0}
        },
        "risk_factors": ["fibroids", "polyps", "coagulopathy", "hormonal_imbalance", "IUD"],
        "specificity": 0.70,
        "urgency": "urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["CBC", "Coagulation", "Pregnancy_test"],
            "within_6h": ["Pelvic_US"],
            "optional": ["Endometrial_biopsy", "Hysteroscopy"]
        },
        "management_hints": "If severe anemia → Transfuse. Hormonal treatment (OCP, progestin). Tranexamic acid. If structural → Surgery. Rule out malignancy if >40."
    }
}

# Fatigue (Mệt Mỏi)
FATIGUE_DDX = {
    "Anemia": {
        "symptoms": {
            "required": ["fatigue"],
            "supporting": ["pale", "dyspnea", "dizziness", "tachycardia", "weakness", "pica"],
            "contradictory": ["normal_Hb", "no_pale"]
        },
        "demographics": {
            "age_risk": {"<40": 0.4, "40-70": 0.6, ">70": 0.7},
            "sex_risk": {"male": 0.8, "female": 1.2}
        },
        "risk_factors": ["bleeding", "nutritional_deficiency", "chronic_disease", "malignancy"],
        "specificity": 0.75,
        "urgency": "urgent",
        "rule_out_first": True,
        "workup": {
            "immediate": ["CBC", "Iron_studies", "B12_Folate", "Reticulocyte"],
            "within_6h": [],
            "optional": ["Bone_marrow_biopsy"]
        },
        "management_hints": "Treat underlying cause. Iron if iron deficiency. B12/folate if deficiency. Transfuse if severe (Hgb <7 or symptomatic)."
    },
    "Hypothyroidism": {
        "symptoms": {
            "required": ["fatigue"],
            "supporting": ["weight_gain", "cold_intolerance", "constipation", "depression", "dry_skin", "hair_loss", "bradycardia"],
            "contradictory": ["weight_loss", "tachycardia", "heat_intolerance"]
        },
        "demographics": {
            "age_risk": {"<40": 0.4, "40-70": 0.7, ">70": 0.6},
            "sex_risk": {"male": 0.3, "female": 1.0}
        },
        "risk_factors": ["autoimmune", "iodine_deficiency", "post_thyroidectomy", "medications"],
        "specificity": 0.80,
        "urgency": "non_urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["TSH", "Free_T4"],
            "within_6h": [],
            "optional": ["TPO_antibodies", "Thyroid_US"]
        },
        "management_hints": "Levothyroxine replacement. Start low dose (25-50mcg) if elderly or cardiac disease. Monitor TSH every 6-8 weeks until stable."
    },
    "Depression": {
        "symptoms": {
            "required": ["fatigue"],
            "supporting": ["low_mood", "anhedonia", "sleep_disturbance", "appetite_change", "concentration_problems", "guilt", "suicidal_ideation"],
            "contradictory": ["normal_mood", "no_psychiatric_symptoms"]
        },
        "demographics": {
            "age_risk": {"<40": 0.5, "40-70": 0.6, ">70": 0.5},
            "sex_risk": {"male": 0.7, "female": 1.0}
        },
        "risk_factors": ["stress", "trauma", "family_history", "chronic_disease", "medications"],
        "specificity": 0.70,
        "urgency": "urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["PHQ9", "Clinical_assessment"],
            "within_6h": [],
            "optional": ["Psychiatry_referral"]
        },
        "management_hints": "SSRI (sertraline, escitalopram). Psychotherapy. If suicidal → Psychiatry consult immediately. Monitor for improvement."
    },
    "Congestive Heart Failure": {
        "symptoms": {
            "required": ["fatigue"],
            "supporting": ["dyspnea", "edema", "orthopnea", "PND", "exercise_intolerance", "jugular_venous_distension"],
            "contradictory": ["no_dyspnea", "no_edema"]
        },
        "demographics": {
            "age_risk": {"<40": 0.2, "40-70": 0.6, ">70": 0.8},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["hypertension", "CAD", "diabetes", "valvular_disease"],
        "specificity": 0.75,
        "urgency": "urgent",
        "rule_out_first": True,
        "workup": {
            "immediate": ["BNP_NT_proBNP", "Echo", "CXR", "ECG"],
            "within_6h": [],
            "optional": ["Cardiac_MRI"]
        },
        "management_hints": "Diuretics. ACE-I/ARB. Beta-blockers. Treat underlying cause. If severe → Hospital admission."
    },
    "COPD": {
        "symptoms": {
            "required": ["fatigue"],
            "supporting": ["dyspnea", "chronic_cough", "smoking_history", "exercise_intolerance", "wheeze"],
            "contradictory": ["no_smoking", "no_dyspnea"]
        },
        "demographics": {
            "age_risk": {"<40": 0.2, "40-70": 0.7, ">70": 0.8},
            "sex_risk": {"male": 1.3, "female": 1.0}
        },
        "risk_factors": ["smoking", "age", "occupational_exposure"],
        "specificity": 0.70,
        "urgency": "non_urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["Spirometry", "CXR"],
            "within_6h": [],
            "optional": ["CT_chest"]
        },
        "management_hints": "Bronchodilators. Smoking cessation. Pulmonary rehab. O2 if hypoxemic. Long-term: ICS + LABA."
    },
    "Chronic Kidney Disease": {
        "symptoms": {
            "required": ["fatigue"],
            "supporting": ["edema", "nausea", "anemia", "hypertension", "decreased_urine_output"],
            "contradictory": ["normal_creatinine", "no_edema"]
        },
        "demographics": {
            "age_risk": {"<40": 0.3, "40-70": 0.6, ">70": 0.7},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["diabetes", "hypertension", "glomerulonephritis", "polycystic_kidney"],
        "specificity": 0.70,
        "urgency": "urgent",
        "rule_out_first": True,
        "workup": {
            "immediate": ["Creatinine", "eGFR", "Urinalysis", "Electrolytes"],
            "within_6h": [],
            "optional": ["Renal_US", "Biopsy"]
        },
        "management_hints": "Treat underlying cause. Control BP. Manage complications (anemia, bone disease). If advanced → Nephrology consult, prepare for dialysis."
    },
    "Malignancy": {
        "symptoms": {
            "required": ["fatigue"],
            "supporting": ["weight_loss", "fever", "night_sweats", "lymphadenopathy", "organomegaly", "bleeding"],
            "contradictory": ["no_weight_loss", "stable_weight"]
        },
        "demographics": {
            "age_risk": {"<40": 0.2, "40-70": 0.5, ">70": 0.6},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["age", "smoking", "family_history", "exposures"],
        "specificity": 0.60,
        "urgency": "urgent",
        "rule_out_first": True,
        "workup": {
            "immediate": ["CBC", "CMP", "CXR", "CT_chest_abdomen_pelvis"],
            "within_6h": [],
            "optional": ["Biopsy", "PET_scan"]
        },
        "management_hints": "URGENT workup if red flags (weight loss, night sweats, lymphadenopathy). Oncology consult. Staging if confirmed."
    }
}

# Back Pain (Đau Lưng)
BACK_PAIN_DDX = {
    "Mechanical Back Pain": {
        "symptoms": {
            "required": ["back_pain"],
            "supporting": ["worse_with_movement", "better_with_rest", "muscle_spasm", "no_red_flags", "gradual_onset"],
            "contradictory": ["red_flags", "neurologic_deficit", "fever"]
        },
        "demographics": {
            "age_risk": {"<40": 0.6, "40-70": 0.7, ">70": 0.6},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["heavy_lifting", "sedentary", "obesity", "poor_posture"],
        "specificity": 0.75,
        "urgency": "non_urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["Clinical_exam"],
            "within_6h": [],
            "optional": ["X_ray", "MRI_if_persistent"]
        },
        "management_hints": "NSAIDs. Physical therapy. Activity modification. Usually resolves in 4-6 weeks. If persists >6 weeks → Imaging."
    },
    "Disc Herniation": {
        "symptoms": {
            "required": ["back_pain"],
            "supporting": ["radiating_pain", "sciatica", "leg_pain", "numbness", "weakness", "worse_with_sitting"],
            "contradictory": ["no_radiating", "no_neurologic"]
        },
        "demographics": {
            "age_risk": {"<40": 0.6, "40-70": 0.7, ">70": 0.4},
            "sex_risk": {"male": 1.2, "female": 1.0}
        },
        "risk_factors": ["heavy_lifting", "repetitive_stress", "age"],
        "specificity": 0.75,
        "urgency": "urgent",
        "rule_out_first": True,
        "workup": {
            "immediate": ["Neurologic_exam", "Straight_leg_raise"],
            "within_6h": ["MRI_spine"],
            "optional": ["EMG"]
        },
        "management_hints": "NSAIDs. Physical therapy. If cauda equina or severe weakness → Urgent surgery. Most improve with conservative treatment."
    },
    "Spinal Stenosis": {
        "symptoms": {
            "required": ["back_pain"],
            "supporting": ["neurogenic_claudication", "worse_with_walking", "better_with_sitting", "bilateral_symptoms", "elderly"],
            "contradictory": ["young_age", "unilateral_only"]
        },
        "demographics": {
            "age_risk": {"<40": 0.1, "40-70": 0.5, ">70": 0.8},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["age", "degenerative_changes", "congenital"],
        "specificity": 0.80,
        "urgency": "non_urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["Clinical_exam"],
            "within_6h": [],
            "optional": ["MRI_spine", "CT_spine"]
        },
        "management_hints": "NSAIDs. Physical therapy. Epidural injections. If severe → Surgery (decompression)."
    },
    "Cauda Equina Syndrome": {
        "symptoms": {
            "required": ["back_pain"],
            "supporting": ["saddle_anesthesia", "bowel_bladder_dysfunction", "bilateral_leg_weakness", "severe_pain"],
            "contradictory": ["no_neurologic", "unilateral_only"]
        },
        "demographics": {
            "age_risk": {"<40": 0.4, "40-70": 0.6, ">70": 0.5},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["disc_herniation", "tumor", "trauma"],
        "specificity": 0.85,
        "urgency": "emergency",
        "rule_out_first": True,
        "workup": {
            "immediate": ["Urgent_MRI", "Neurologic_exam", "Rectal_exam"],
            "within_6h": ["Surgical_consult"],
            "optional": []
        },
        "management_hints": "URGENT! Surgical emergency. Decompression within 24-48h. Delay → Permanent deficits. Immediate neurosurgery consult."
    },
    "Spinal Infection": {
        "symptoms": {
            "required": ["back_pain"],
            "supporting": ["fever", "night_sweats", "weight_loss", "localized_tenderness", "recent_infection", "IVDU"],
            "contradictory": ["no_fever", "no_red_flags"]
        },
        "demographics": {
            "age_risk": {"<40": 0.4, "40-70": 0.6, ">70": 0.7},
            "sex_risk": {"male": 1.2, "female": 1.0}
        },
        "risk_factors": ["IVDU", "immunocompromised", "diabetes", "recent_surgery"],
        "specificity": 0.75,
        "urgency": "emergency",
        "rule_out_first": True,
        "workup": {
            "immediate": ["MRI_spine", "Blood_cultures", "ESR_CRP", "CBC"],
            "within_6h": ["CT_guided_biopsy"],
            "optional": []
        },
        "management_hints": "URGENT! IV antibiotics (empiric: Vancomycin + Ceftriaxone). Surgical debridement if abscess. 6-12 weeks antibiotics."
    },
    "Malignancy (Spinal)": {
        "symptoms": {
            "required": ["back_pain"],
            "supporting": ["night_pain", "weight_loss", "fever", "history_cancer", "worse_at_rest", "constitutional_symptoms"],
            "contradictory": ["no_red_flags", "mechanical_pattern"]
        },
        "demographics": {
            "age_risk": {"<40": 0.2, "40-70": 0.5, ">70": 0.7},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["history_cancer", "age", "smoking"],
        "specificity": 0.70,
        "urgency": "emergency",
        "rule_out_first": True,
        "workup": {
            "immediate": ["MRI_spine", "CT_chest_abdomen_pelvis", "CBC", "ESR"],
            "within_6h": ["Biopsy"],
            "optional": ["PET_scan"]
        },
        "management_hints": "URGENT workup. Oncology consult. If cord compression → Urgent radiation/surgery. Treat underlying malignancy."
    }
}

# Vision Changes (Thay Đổi Thị Lực)
VISION_CHANGES_DDX = {
    "Retinal Detachment": {
        "symptoms": {
            "required": ["vision_changes"],
            "supporting": ["sudden_vision_loss", "floaters", "flashes", "curtain_vision", "no_pain", "monocular"],
            "contradictory": ["gradual_onset", "pain", "bilateral"]
        },
        "demographics": {
            "age_risk": {"<40": 0.3, "40-70": 0.6, ">70": 0.7},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["myopia", "trauma", "previous_detachment", "diabetes"],
        "specificity": 0.80,
        "urgency": "emergency",
        "rule_out_first": True,
        "workup": {
            "immediate": ["Ophthalmology_consult", "Fundoscopy", "Slit_lamp"],
            "within_6h": ["Ocular_ultrasound"],
            "optional": []
        },
        "management_hints": "URGENT! Ophthalmology consult immediately. Surgical repair (pneumatic retinopexy, scleral buckle, vitrectomy). Delay → Permanent vision loss."
    },
    "CVA / Stroke": {
        "symptoms": {
            "required": ["vision_changes"],
            "supporting": ["sudden_vision_loss", "homonymous_hemianopia", "diplopia", "neurologic_deficit", "facial_droop", "speech_problems"],
            "contradictory": ["gradual_onset", "no_neurologic"]
        },
        "demographics": {
            "age_risk": {"<40": 0.2, "40-70": 0.6, ">70": 0.8},
            "sex_risk": {"male": 1.2, "female": 1.0}
        },
        "risk_factors": ["hypertension", "atrial_fibrillation", "diabetes", "smoking", "age"],
        "specificity": 0.75,
        "urgency": "emergency",
        "rule_out_first": True,
        "workup": {
            "immediate": ["CT_head", "Neurology_consult", "NIHSS"],
            "within_6h": ["MRI_brain", "CTA"],
            "optional": []
        },
        "management_hints": "URGENT! If ischemic <4.5h → tPA. If <24h + large vessel → Thrombectomy. Control risk factors."
    },
    "Glaucoma (Acute Angle Closure)": {
        "symptoms": {
            "required": ["vision_changes"],
            "supporting": ["sudden_vision_loss", "eye_pain", "headache", "nausea", "vomiting", "halos", "red_eye"],
            "contradictory": ["no_pain", "gradual_onset"]
        },
        "demographics": {
            "age_risk": {"<40": 0.2, "40-70": 0.6, ">70": 0.7},
            "sex_risk": {"male": 0.8, "female": 1.0}
        },
        "risk_factors": ["hyperopia", "age", "family_history", "Asian_ethnicity"],
        "specificity": 0.80,
        "urgency": "emergency",
        "rule_out_first": True,
        "workup": {
            "immediate": ["Ophthalmology_consult", "IOP_measurement", "Slit_lamp"],
            "within_6h": ["Gonioscopy"],
            "optional": []
        },
        "management_hints": "URGENT! Lower IOP immediately (timolol, pilocarpine, acetazolamide). Laser iridotomy. Delay → Permanent vision loss."
    },
    "Migraine Aura": {
        "symptoms": {
            "required": ["vision_changes"],
            "supporting": ["scintillating_scotoma", "zigzag_lines", "tunnel_vision", "headache_follows", "recurrent", "no_neurologic_deficit"],
            "contradictory": ["persistent_deficit", "sudden_onset_severe"]
        },
        "demographics": {
            "age_risk": {"<40": 0.7, "40-70": 0.5, ">70": 0.2},
            "sex_risk": {"male": 0.5, "female": 1.0}
        },
        "risk_factors": ["family_history", "female", "young_age"],
        "specificity": 0.75,
        "urgency": "non_urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["Clinical_diagnosis"],
            "within_6h": [],
            "optional": ["MRI_if_atypical"]
        },
        "management_hints": "Triptans if headache. Avoid triggers. If first episode or atypical → Neuroimaging to rule out stroke/TIA."
    },
    "Giant Cell Arteritis": {
        "symptoms": {
            "required": ["vision_changes"],
            "supporting": ["sudden_vision_loss", "headache", "temporal_tenderness", "jaw_claudication", "fever", "elderly", "ESR_elevated"],
            "contradictory": ["young_age", "no_headache"]
        },
        "demographics": {
            "age_risk": {"<50": 0.0, "50-70": 0.6, ">70": 0.8},
            "sex_risk": {"male": 0.5, "female": 1.0}
        },
        "risk_factors": ["age_>50", "female", "polymyalgia_rheumatica"],
        "specificity": 0.80,
        "urgency": "emergency",
        "rule_out_first": True,
        "workup": {
            "immediate": ["ESR_CRP", "Temporal_artery_biopsy", "High_dose_steroids"],
            "within_6h": [],
            "optional": []
        },
        "management_hints": "URGENT! High-dose steroids (prednisone 60-80mg) immediately to prevent vision loss. Temporal artery biopsy within 1 week."
    }
}

# Pediatric Joint Pain (Đau Khớp Nhi)
PEDIATRIC_JOINT_PAIN_DDX = {
    "Juvenile Idiopathic Arthritis (JIA)": {
        "symptoms": {
            "required": ["joint_pain"],
            "supporting": ["morning_stiffness", "swelling", "multiple_joints", "chronic", "fever", "rash", "uveitis"],
            "contradictory": ["acute_severe", "single_joint", "septic_appearance"]
        },
        "demographics": {
            "age_risk": {"<16": 1.0, "16-18": 0.8, ">18": 0.0},
            "sex_risk": {"male": 0.7, "female": 1.0}
        },
        "risk_factors": ["family_history", "HLA_B27"],
        "specificity": 0.75,
        "urgency": "urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["CBC", "ESR_CRP", "RF_ANA", "X_ray_joints"],
            "within_6h": [],
            "optional": ["HLA_B27", "Ophthalmology_screening"]
        },
        "management_hints": "NSAIDs. DMARDs (methotrexate). Biologics if severe. Ophthalmology screening (uveitis risk). Rheumatology consult."
    },
    "Septic Arthritis": {
        "symptoms": {
            "required": ["joint_pain"],
            "supporting": ["fever", "single_joint", "severe_pain", "erythema", "swelling", "decreased_range_of_motion", "toxic_appearance"],
            "contradictory": ["no_fever", "multiple_joints", "chronic"]
        },
        "demographics": {
            "age_risk": {"<5": 0.8, "5-10": 0.6, ">10": 0.4},
            "sex_risk": {"male": 1.2, "female": 1.0}
        },
        "risk_factors": ["recent_infection", "immunocompromised", "sickle_cell"],
        "specificity": 0.85,
        "urgency": "emergency",
        "rule_out_first": True,
        "workup": {
            "immediate": ["Joint_aspiration", "Synovial_fluid_analysis", "Blood_cultures", "CBC", "ESR_CRP"],
            "within_6h": ["X_ray", "Orthopedic_consult"],
            "optional": []
        },
        "management_hints": "URGENT! IV antibiotics (empiric: Vancomycin + Ceftriaxone). Surgical drainage if needed. Delay → Joint destruction."
    },
    "Reactive Arthritis": {
        "symptoms": {
            "required": ["joint_pain"],
            "supporting": ["recent_infection", "GI_URI_symptoms", "asymmetric", "lower_extremities", "enthesitis", "urethritis", "conjunctivitis"],
            "contradictory": ["no_recent_infection", "symmetric"]
        },
        "demographics": {
            "age_risk": {"<10": 0.4, "10-18": 0.7, ">18": 0.5},
            "sex_risk": {"male": 1.2, "female": 1.0}
        },
        "risk_factors": ["recent_infection", "HLA_B27"],
        "specificity": 0.70,
        "urgency": "urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["CBC", "ESR_CRP", "Stool_culture", "Urethral_culture", "HLA_B27"],
            "within_6h": [],
            "optional": []
        },
        "management_hints": "NSAIDs. Treat underlying infection. Usually self-limited. If persistent → DMARDs. Rheumatology consult."
    },
    "Growing Pains": {
        "symptoms": {
            "required": ["joint_pain"],
            "supporting": ["bilateral", "lower_extremities", "evening_night", "no_swelling", "no_limitation", "intermittent", "young_age"],
            "contradictory": ["swelling", "morning_stiffness", "fever", "single_joint"]
        },
        "demographics": {
            "age_risk": {"<5": 0.6, "5-10": 0.8, ">10": 0.3},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["young_age", "active_child"],
        "specificity": 0.75,
        "urgency": "non_urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["Clinical_diagnosis"],
            "within_6h": [],
            "optional": []
        },
        "management_hints": "Reassurance. Massage. Stretching. Usually resolves with age. If atypical features → Further workup."
    },
    "Osteomyelitis": {
        "symptoms": {
            "required": ["joint_pain"],
            "supporting": ["fever", "localized_pain", "swelling", "erythema", "decreased_motion", "recent_trauma", "toxic_appearance"],
            "contradictory": ["no_fever", "multiple_sites", "chronic_mild"]
        },
        "demographics": {
            "age_risk": {"<5": 0.7, "5-10": 0.6, ">10": 0.4},
            "sex_risk": {"male": 1.2, "female": 1.0}
        },
        "risk_factors": ["recent_trauma", "sickle_cell", "immunocompromised"],
        "specificity": 0.75,
        "urgency": "emergency",
        "rule_out_first": True,
        "workup": {
            "immediate": ["X_ray", "MRI", "Blood_cultures", "CBC", "ESR_CRP"],
            "within_6h": ["Bone_aspiration", "Orthopedic_consult"],
            "optional": []
        },
        "management_hints": "URGENT! IV antibiotics (Vancomycin + Ceftriaxone). Surgical debridement if abscess. 4-6 weeks antibiotics."
    }
}

# Electrolyte Disorders (Rối Loạn Điện Giải)
ELECTROLYTE_DISORDERS_DDX = {
    "Hyponatremia": {
        "symptoms": {
            "required": ["electrolyte_disorder"],
            "supporting": ["nausea", "headache", "confusion", "seizures", "coma", "low_Na"],
            "contradictory": ["normal_Na", "high_Na"]
        },
        "demographics": {
            "age_risk": {"<40": 0.4, "40-70": 0.6, ">70": 0.8},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["diuretics", "SIADH", "heart_failure", "liver_disease", "renal_disease"],
        "specificity": 0.80,
        "urgency": "emergency",
        "rule_out_first": True,
        "workup": {
            "immediate": ["Na", "Osmolality", "Urine_Na", "Urine_osmolality", "TSH", "Cortisol"],
            "within_6h": [],
            "optional": []
        },
        "management_hints": "If severe (<120) or symptomatic → 3% saline. Correct slowly (0.5-1 mEq/L/h) to avoid ODS. Treat underlying cause."
    },
    "Hypernatremia": {
        "symptoms": {
            "required": ["electrolyte_disorder"],
            "supporting": ["thirst", "confusion", "seizures", "coma", "high_Na", "dehydration"],
            "contradictory": ["normal_Na", "low_Na"]
        },
        "demographics": {
            "age_risk": {"<40": 0.3, "40-70": 0.5, ">70": 0.7},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["dehydration", "diabetes_insipidus", "elderly", "tube_feeding"],
        "specificity": 0.80,
        "urgency": "emergency",
        "rule_out_first": True,
        "workup": {
            "immediate": ["Na", "Osmolality", "Urine_osmolality", "Volume_status"],
            "within_6h": [],
            "optional": []
        },
        "management_hints": "If severe (>160) or symptomatic → D5W or 0.45% saline. Correct slowly (0.5-1 mEq/L/h). Treat underlying cause."
    },
    "Hypokalemia": {
        "symptoms": {
            "required": ["electrolyte_disorder"],
            "supporting": ["weakness", "muscle_cramps", "arrhythmias", "low_K", "diuretics"],
            "contradictory": ["normal_K", "high_K"]
        },
        "demographics": {
            "age_risk": {"<40": 0.4, "40-70": 0.6, ">70": 0.7},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["diuretics", "vomiting", "diarrhea", "alkalosis"],
        "specificity": 0.80,
        "urgency": "urgent",
        "rule_out_first": True,
        "workup": {
            "immediate": ["K", "Mg", "ABG", "ECG"],
            "within_6h": [],
            "optional": ["Urine_K"]
        },
        "management_hints": "If severe (<2.5) or symptomatic → IV K (max 20 mEq/h with cardiac monitoring). Check Mg. Treat underlying cause."
    },
    "Hyperkalemia": {
        "symptoms": {
            "required": ["electrolyte_disorder"],
            "supporting": ["weakness", "arrhythmias", "ECG_changes", "high_K", "renal_disease"],
            "contradictory": ["normal_K", "low_K"]
        },
        "demographics": {
            "age_risk": {"<40": 0.3, "40-70": 0.6, ">70": 0.7},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["renal_disease", "medications", "acidosis", "cell_lysis"],
        "specificity": 0.85,
        "urgency": "emergency",
        "rule_out_first": True,
        "workup": {
            "immediate": ["K", "ECG", "Creatinine", "ABG"],
            "within_6h": [],
            "optional": []
        },
        "management_hints": "URGENT if >6.5 or ECG changes! Calcium gluconate (cardioprotection), insulin+glucose, albuterol, kayexalate. Dialysis if severe."
    }
}

# Drug Reaction (Tác Dụng Phụ Thuốc)
DRUG_REACTION_DDX = {
    "Drug Allergy": {
        "symptoms": {
            "required": ["drug_reaction"],
            "supporting": ["rash", "urticaria", "pruritus", "recent_medication", "timing_related", "angioedema"],
            "contradictory": ["no_rash", "delayed_timing"]
        },
        "demographics": {
            "age_risk": {"<40": 0.5, "40-70": 0.7, ">70": 0.8},
            "sex_risk": {"male": 1.0, "female": 1.2}
        },
        "risk_factors": ["multiple_medications", "prior_allergies", "specific_drugs"],
        "specificity": 0.75,
        "urgency": "urgent",
        "rule_out_first": True,
        "workup": {
            "immediate": ["Stop_drug", "CBC", "Clinical_assessment"],
            "within_6h": [],
            "optional": ["Allergy_testing"]
        },
        "management_hints": "Stop suspected drug immediately. Antihistamines. Steroids if severe. If anaphylaxis → Epinephrine, ICU."
    },
    "Drug Toxicity": {
        "symptoms": {
            "required": ["drug_reaction"],
            "supporting": ["nausea", "vomiting", "confusion", "seizures", "organ_dysfunction", "overdose", "high_dose"],
            "contradictory": ["normal_dose", "no_symptoms"]
        },
        "demographics": {
            "age_risk": {"<40": 0.4, "40-70": 0.6, ">70": 0.7},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["overdose", "drug_interactions", "renal_hepatic_impairment", "elderly"],
        "specificity": 0.70,
        "urgency": "emergency",
        "rule_out_first": True,
        "workup": {
            "immediate": ["Drug_levels", "CBC", "CMP", "ECG", "Toxicology_screen"],
            "within_6h": [],
            "optional": []
        },
        "management_hints": "URGENT! Stop drug. Supportive care. Specific antidotes if available. Activated charcoal if recent ingestion. Dialysis if indicated."
    },
    "Stevens-Johnson Syndrome / TEN": {
        "symptoms": {
            "required": ["drug_reaction"],
            "supporting": ["rash", "target_lesions", "bulla", "mucosal_involvement", "fever", "drug_exposure", "toxic_epidermal_necrolysis"],
            "contradictory": ["mild_rash", "no_mucosal"]
        },
        "demographics": {
            "age_risk": {"<40": 0.5, "40-70": 0.8, ">70": 0.7},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["drugs", "infections", "genetic_factors"],
        "specificity": 0.85,
        "urgency": "emergency",
        "rule_out_first": True,
        "workup": {
            "immediate": ["Stop_all_drugs", "ICU_admit", "Dermatology_consult", "Skin_biopsy"],
            "within_6h": [],
            "optional": []
        },
        "management_hints": "URGENT! Life-threatening! ICU immediately. Stop all drugs. Dermatology + burn unit. Supportive care. High mortality if >30% BSA."
    },
    "Anaphylaxis": {
        "symptoms": {
            "required": ["drug_reaction"],
            "supporting": ["urticaria", "angioedema", "hypotension", "dyspnea", "wheezing", "rapid_onset", "shock"],
            "contradictory": ["delayed_onset", "no_respiratory_cardiovascular"]
        },
        "demographics": {
            "age_risk": {"<40": 0.5, "40-70": 0.6, ">70": 0.7},
            "sex_risk": {"male": 1.0, "female": 1.2}
        },
        "risk_factors": ["prior_allergies", "atopy", "specific_drugs"],
        "specificity": 0.90,
        "urgency": "emergency",
        "rule_out_first": True,
        "workup": {
            "immediate": ["Epinephrine", "IV_access", "O2", "ICU"],
            "within_6h": [],
            "optional": ["Tryptase"]
        },
        "management_hints": "URGENT! Life-threatening! Epinephrine IM immediately. IV fluids. Antihistamines. Steroids. ICU monitoring. Delay → Death."
    },
    "Serum Sickness": {
        "symptoms": {
            "required": ["drug_reaction"],
            "supporting": ["fever", "rash", "arthralgia", "lymphadenopathy", "delayed_onset", "serum_proteins"],
            "contradictory": ["immediate_onset", "no_fever"]
        },
        "demographics": {
            "age_risk": {"<40": 0.5, "40-70": 0.6, ">70": 0.4},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["serum_proteins", "monoclonal_antibodies", "vaccines"],
        "specificity": 0.70,
        "urgency": "urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["CBC", "ESR_CRP", "Clinical_assessment"],
            "within_6h": [],
            "optional": []
        },
        "management_hints": "Stop drug. Antihistamines. NSAIDs for arthralgia. Steroids if severe. Usually self-limited."
    }
}

# Map all scenarios
ALL_SCENARIOS = {
    "Chest Pain": CHEST_PAIN_DDX,
    "Dyspnea": DYSPNEA_DDX,
    "Abdominal Pain": ABDOMINAL_PAIN_DDX,
    "Altered Mental Status": ALTERED_MENTAL_STATUS_DDX,
    "Fever": FEVER_DDX,
    "Syncope": SYNCOPE_DDX,
    "Joint Pain": JOINT_PAIN_DDX,
    "Headache": HEADACHE_DDX,
    "Diarrhea": DIARRHEA_DDX,
    "Anemia": ANEMIA_DDX,
    "Kidney Injury": KIDNEY_INJURY_DDX,
    "Hypertension Emergency": HTN_EMERGENCY_DDX,
    "Vomiting": VOMITING_DDX,
    "Rash": RASH_DDX,
    "Cough": COUGH_DDX,
    "Bleeding": BLEEDING_DDX,
    "Fatigue": FATIGUE_DDX,
    "Back Pain": BACK_PAIN_DDX,
    "Vision Changes": VISION_CHANGES_DDX,
    "Pediatric Joint Pain": PEDIATRIC_JOINT_PAIN_DDX,
    "Electrolyte Disorders": ELECTROLYTE_DISORDERS_DDX,
    "Drug Reaction": DRUG_REACTION_DDX,
}

# Symptom aliases for matching
SYMPTOM_ALIASES = {
    "chest_pain": ["chest_pain", "cp", "chest discomfort"],
    "chest_pain_retrosternal": ["retrosternal", "substernal", "central chest"],
    "chest_pain_crushing": ["crushing", "pressure", "squeezing"],
    "chest_pain_pleuritic": ["pleuritic", "worse breathing", "worse inspiration"],
    "chest_pain_tearing": ["tearing", "ripping"],
    "radiation_left_arm": ["radiation", "radiates", "left arm"],
    "diaphoresis": ["sweating", "sweaty", "diaphoresis"],
    "dyspnea": ["shortness of breath", "sob", "dyspnea", "difficulty breathing"],
    "acute_onset": ["acute", "sudden", "abrupt"],
    "fever": ["fever", "febrile", "temperature"],
    "cough": ["cough", "coughing"],
    "productive_cough": ["productive cough", "sputum", "phlegm"],
}


