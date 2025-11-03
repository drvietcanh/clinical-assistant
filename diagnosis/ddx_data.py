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

# Map all scenarios
ALL_SCENARIOS = {
    "Chest Pain": CHEST_PAIN_DDX,
    "Dyspnea": DYSPNEA_DDX,
    "Abdominal Pain": ABDOMINAL_PAIN_DDX,
    "Altered Mental Status": ALTERED_MENTAL_STATUS_DDX,
    "Fever": FEVER_DDX,
    "Syncope": SYNCOPE_DDX,
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


def get_scenario_data(scenario_name):
    """Get DDx data for a scenario"""
    return ALL_SCENARIOS.get(scenario_name, {})


def get_all_scenarios():
    """Get list of all available scenarios"""
    return list(ALL_SCENARIOS.keys())


def get_symptom_matches(user_symptoms, diagnosis_symptoms):
    """Calculate symptom matches for a diagnosis"""
    matches = {
        "required": 0,
        "supporting": 0,
        "contradictory": 0
    }
    
    for symptom in user_symptoms:
        symptom_lower = symptom.lower()
        
        # Check required symptoms
        for req in diagnosis_symptoms.get("required", []):
            if symptom_lower in req.lower() or req.lower() in symptom_lower:
                matches["required"] += 1
                break
        
        # Check supporting symptoms
        for sup in diagnosis_symptoms.get("supporting", []):
            if symptom_lower in sup.lower() or sup.lower() in symptom_lower:
                matches["supporting"] += 1
                break
        
        # Check contradictory symptoms
        for contr in diagnosis_symptoms.get("contradictory", []):
            if symptom_lower in contr.lower() or contr.lower() in symptom_lower:
                matches["contradictory"] += 1
                break
    
    return matches

