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

