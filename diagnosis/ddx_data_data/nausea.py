"""DDx Knowledge Base - Data
Differential diagnosis data for common clinical scenarios

NOTE: This file contains only data dictionaries.
Functions are in ddx_data.py"""

# Nausea Differential Diagnosis

NAUSEA_DDX = {
    "Gastroenteritis": {
        "symptoms": {
            "required": ["nausea"],
            "supporting": ["vomiting", "diarrhea", "abdominal_cramping", "fever", "recent_food_exposure", "multiple_contacts"],
            "contradictory": ["no_diarrhea", "no_vomiting", "severe_abdominal_pain"]
        },
        "demographics": {
            "age_risk": {"<40": 0.7, "40-70": 0.5, ">70": 0.4},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["recent_food_exposure", "travel", "contact_with_sick", "poor_hygiene"],
        "specificity": 0.70,
        "urgency": "non_urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["Clinical_assessment", "Hydration_status"],
            "within_6h": ["CBC", "CMP", "Stool_culture_if_severe"],
            "optional": ["Stool_parasites", "C.diff_toxin"]
        },
        "management_hints": "Supportive care: Hydration (oral or IV), antiemetics (ondansetron). Usually self-limited (24-48h). Monitor for dehydration. Consider antibiotics only if bacterial (travel, severe)."
    },
    "Medication-Induced Nausea": {
        "symptoms": {
            "required": ["nausea"],
            "supporting": ["recent_medication_start", "dose_related", "timing_related", "improves_with_stopping"],
            "contradictory": ["no_medications", "chronic_medications_only"]
        },
        "demographics": {
            "age_risk": {"<40": 0.4, "40-70": 0.5, ">70": 0.6},
            "sex_risk": {"male": 0.8, "female": 1.2}
        },
        "risk_factors": ["antibiotics", "chemotherapy", "opioids", "NSAIDs", "metformin", "digoxin", "multiple_medications"],
        "specificity": 0.75,
        "urgency": "non_urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["Medication_review", "Timing_analysis"],
            "within_6h": ["Drug_levels_if_applicable"],
            "optional": []
        },
        "management_hints": "Review medications. Common culprits: antibiotics, opioids, metformin, digoxin, chemotherapy. Consider: dose reduction, timing change, antiemetics (ondansetron), or alternative medication. Do not stop critical medications without consultation."
    },
    "Pregnancy (Morning Sickness)": {
        "symptoms": {
            "required": ["nausea"],
            "supporting": ["morning_worse", "pregnancy", "first_trimester", "no_abdominal_pain", "improves_afternoon"],
            "contradictory": ["male", "post_menopause", "severe_abdominal_pain"]
        },
        "demographics": {
            "age_risk": {"<40": 0.8, "40-70": 0.1, ">70": 0.0},
            "sex_risk": {"male": 0.0, "female": 1.0}
        },
        "risk_factors": ["pregnancy", "first_trimester", "multiple_gestation", "history_hyperemesis"],
        "specificity": 0.85,
        "urgency": "non_urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["Pregnancy_test", "Clinical_assessment"],
            "within_6h": ["Ultrasound_if_hyperemesis"],
            "optional": ["Electrolytes_if_severe"]
        },
        "management_hints": "First-line: Dietary changes (small frequent meals, ginger), doxylamine/pyridoxine. If severe → ondansetron, metoclopramide. Hyperemesis gravidarum → IV hydration, thiamine. Rule out other causes if atypical."
    },
    "Gastroparesis": {
        "symptoms": {
            "required": ["nausea"],
            "supporting": ["early_satiety", "bloating", "postprandial_fullness", "diabetes", "delayed_gastric_emptying", "chronic"],
            "contradictory": ["acute_onset", "no_diabetes"]
        },
        "demographics": {
            "age_risk": {"<40": 0.3, "40-70": 0.6, ">70": 0.7},
            "sex_risk": {"male": 0.7, "female": 1.3}
        },
        "risk_factors": ["diabetes", "gastric_surgery", "scleroderma", "hypothyroidism", "Parkinson_disease", "medications"],
        "specificity": 0.70,
        "urgency": "non_urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["Clinical_assessment", "HbA1c_if_diabetes"],
            "within_6h": ["Gastric_emptying_study"],
            "optional": ["Upper_endoscopy", "Autonomic_testing"]
        },
        "management_hints": "Treatment: Dietary modifications (small frequent meals, low fat/fiber), prokinetics (metoclopramide, domperidone), antiemetics. Optimize diabetes control. Consider gastric electrical stimulation if severe."
    },
    "Peptic Ulcer Disease": {
        "symptoms": {
            "required": ["nausea"],
            "supporting": ["epigastric_pain", "burning_pain", "worse_on_empty_stomach", "relieved_by_food", "NSAID_use", "H.pylori"],
            "contradictory": ["no_abdominal_pain", "severe_acute_pain"]
        },
        "demographics": {
            "age_risk": {"<40": 0.4, "40-70": 0.6, ">70": 0.5},
            "sex_risk": {"male": 1.2, "female": 1.0}
        },
        "risk_factors": ["H.pylori", "NSAID_use", "alcohol", "smoking", "stress", "older_age"],
        "specificity": 0.65,
        "urgency": "urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["H.pylori_test", "Upper_endoscopy_if_alarm_symptoms"],
            "within_6h": ["CBC", "CMP"],
            "optional": ["Upper_endoscopy", "Biopsy"]
        },
        "management_hints": "PPI therapy. H.pylori eradication (triple/quadruple therapy). Avoid NSAIDs. Alarm symptoms (bleeding, weight loss, age >55) → urgent endoscopy. Monitor for complications (bleeding, perforation)."
    },
    "Acute Pancreatitis": {
        "symptoms": {
            "required": ["nausea"],
            "supporting": ["severe_abdominal_pain", "epigastric_pain", "radiating_to_back", "vomiting", "fever", "tenderness"],
            "contradictory": ["no_abdominal_pain", "mild_pain"]
        },
        "demographics": {
            "age_risk": {"<40": 0.4, "40-70": 0.6, ">70": 0.5},
            "sex_risk": {"male": 1.2, "female": 1.0}
        },
        "risk_factors": ["gallstones", "alcohol", "hypertriglyceridemia", "ERCP", "medications", "trauma"],
        "specificity": 0.80,
        "urgency": "urgent",
        "rule_out_first": True,
        "workup": {
            "immediate": ["Lipase", "Amylase", "CBC", "CMP", "CT_abdomen"],
            "within_6h": ["US_abdomen", "ECG"],
            "optional": ["MRI_MRCP", "ERCP_if_indicated"]
        },
        "management_hints": "URGENT! NPO, IV hydration, pain control (opioids), monitor for complications. Supportive care. Treat underlying cause (gallstones, alcohol). Severe → ICU, consider ERCP if biliary obstruction. Monitor for organ failure (Ranson, APACHE)."
    },
    "Migraine": {
        "symptoms": {
            "required": ["nausea"],
            "supporting": ["headache", "unilateral", "throbbing", "photophobia", "phonophobia", "aura", "worse_with_activity"],
            "contradictory": ["no_headache", "bilateral_pressure"]
        },
        "demographics": {
            "age_risk": {"<40": 0.7, "40-70": 0.5, ">70": 0.2},
            "sex_risk": {"male": 0.7, "female": 1.3}
        },
        "risk_factors": ["family_history", "female", "hormonal_changes", "stress", "certain_foods", "sleep_changes"],
        "specificity": 0.75,
        "urgency": "non_urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["Clinical_assessment", "Neurologic_exam"],
            "within_6h": ["CT_head_if_atypical"],
            "optional": ["MRI_if_chronic_or_atypical"]
        },
        "management_hints": "Acute: Triptans, NSAIDs, antiemetics (metoclopramide, ondansetron). Prevention: Beta-blockers, topiramate, amitriptyline. Lifestyle modifications. Rule out secondary causes if atypical features."
    }
}

__all__ = ['NAUSEA_DDX']

