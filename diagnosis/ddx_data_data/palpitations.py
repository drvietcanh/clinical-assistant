"""DDx Knowledge Base - Data
Differential diagnosis data for common clinical scenarios

NOTE: This file contains only data dictionaries.
Functions are in ddx_data.py"""

# Palpitations Differential Diagnosis

PALPITATIONS_DDX = {
    "Atrial Fibrillation": {
        "symptoms": {
            "required": ["palpitations", "irregular_rhythm"],
            "supporting": ["rapid_heart_rate", "fatigue", "dyspnea", "chest_discomfort", "dizziness", "stroke_risk"],
            "contradictory": ["regular_rhythm"]
        },
        "demographics": {
            "age_risk": {"<40": 0.2, "40-70": 0.5, ">70": 0.8},
            "sex_risk": {"male": 1.2, "female": 1.0}
        },
        "risk_factors": ["hypertension", "heart_failure", "valvular_disease", "thyrotoxicosis", "alcohol", "obesity", "sleep_apnea"],
        "specificity": 0.85,
        "urgency": "urgent",
        "rule_out_first": True,
        "workup": {
            "immediate": ["ECG", "Echo", "Thyroid_function"],
            "within_6h": ["Holter_monitor", "CHADS2_VASc_score", "Anticoagulation_assessment"],
            "optional": ["Cardiac_MRI", "Electrophysiology_study"]
        },
        "management_hints": "Rate control (beta-blockers, calcium channel blockers) or rhythm control (cardioversion, antiarrhythmics). Anticoagulation based on CHA₂DS₂-VASc score. Consider ablation if symptomatic."
    },
    "Supraventricular Tachycardia (SVT)": {
        "symptoms": {
            "required": ["palpitations", "rapid_heart_rate"],
            "supporting": ["sudden_onset", "sudden_termination", "regular_rhythm", "narrow_QRS", "chest_discomfort", "dizziness"],
            "contradictory": ["gradual_onset", "wide_QRS"]
        },
        "demographics": {
            "age_risk": {"<40": 0.6, "40-70": 0.4, ">70": 0.2},
            "sex_risk": {"male": 0.8, "female": 1.2}
        },
        "risk_factors": ["young_age", "Wolff_Parkinson_White", "AVNRT", "caffeine", "alcohol", "stress"],
        "specificity": 0.80,
        "urgency": "urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["ECG", "Vagal_maneuvers"],
            "within_6h": ["Echo", "Holter_monitor", "Electrophysiology_study_if_recurrent"],
            "optional": ["Adenosine_test"]
        },
        "management_hints": "Acute: Vagal maneuvers, adenosine IV. Chronic: Beta-blockers, calcium channel blockers, or flecainide. Consider ablation if recurrent or symptomatic. WPW → Avoid AV node blockers."
    },
    "Premature Ventricular Contractions (PVCs)": {
        "symptoms": {
            "required": ["palpitations"],
            "supporting": ["skipped_beats", "thumping", "irregular", "isolated", "frequent", "exercise_induced"],
            "contradictory": ["sustained_tachycardia"]
        },
        "demographics": {
            "age_risk": {"<40": 0.4, "40-70": 0.5, ">70": 0.6},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["caffeine", "alcohol", "stress", "electrolyte_abnormalities", "heart_disease", "medication"],
        "specificity": 0.70,
        "urgency": "non_urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["ECG", "Echo"],
            "within_6h": ["Holter_monitor", "Electrolytes"],
            "optional": ["Stress_test", "Cardiac_MRI"]
        },
        "management_hints": "Benign PVCs: Reassurance, lifestyle modifications (reduce caffeine, alcohol). If symptomatic: Beta-blockers. If frequent or structural heart disease: Further evaluation, consider ablation."
    },
    "Anxiety / Panic Disorder": {
        "symptoms": {
            "required": ["palpitations"],
            "supporting": ["anxiety", "panic", "chest_tightness", "hyperventilation", "sweating", "tremor", "fear_of_dying", "situational"],
            "contradictory": ["structural_heart_disease", "abnormal_ECG"]
        },
        "demographics": {
            "age_risk": {"<40": 0.6, "40-70": 0.4, ">70": 0.2},
            "sex_risk": {"male": 0.7, "female": 1.3}
        },
        "risk_factors": ["anxiety_disorder", "panic_disorder", "stress", "trauma", "substance_use"],
        "specificity": 0.65,
        "urgency": "non_urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["ECG_to_rule_out_arrhythmia"],
            "within_6h": ["Psychiatric_evaluation"],
            "optional": ["Holter_monitor", "Thyroid_function"]
        },
        "management_hints": "Rule out cardiac causes first. Treatment: Cognitive behavioral therapy (CBT), SSRIs, benzodiazepines (short-term). Reassurance and education important."
    },
    "Hyperthyroidism": {
        "symptoms": {
            "required": ["palpitations"],
            "supporting": ["tachycardia", "weight_loss", "heat_intolerance", "sweating", "tremor", "anxiety", "insomnia", "diarrhea"],
            "contradictory": ["weight_gain", "cold_intolerance"]
        },
        "demographics": {
            "age_risk": {"<40": 0.5, "40-70": 0.6, ">70": 0.4},
            "sex_risk": {"male": 0.3, "female": 1.7}
        },
        "risk_factors": ["Graves_disease", "toxic_nodule", "thyroiditis", "iodine_exposure", "family_history"],
        "specificity": 0.80,
        "urgency": "urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["TSH", "Free_T4", "Free_T3", "ECG"],
            "within_6h": ["Thyroid_antibodies", "Thyroid_ultrasound"],
            "optional": ["Radioactive_iodine_uptake", "Thyroid_scan"]
        },
        "management_hints": "Treatment: Antithyroid drugs (methimazole, PTU), beta-blockers for symptoms. Consider radioactive iodine or surgery. Monitor for thyroid storm (emergency)."
    },
    "Anemia": {
        "symptoms": {
            "required": ["palpitations"],
            "supporting": ["fatigue", "dyspnea", "pale", "tachycardia", "weakness", "dizziness", "low_hemoglobin"],
            "contradictory": ["normal_hemoglobin"]
        },
        "demographics": {
            "age_risk": {"<40": 0.4, "40-70": 0.5, ">70": 0.6},
            "sex_risk": {"male": 0.8, "female": 1.2}
        },
        "risk_factors": ["iron_deficiency", "blood_loss", "chronic_disease", "nutritional_deficiency", "hemolysis"],
        "specificity": 0.70,
        "urgency": "non_urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["CBC", "Iron_studies", "B12", "Folate"],
            "within_6h": ["Reticulocyte_count", "Peripheral_smear"],
            "optional": ["Bone_marrow_biopsy", "Hemolysis_workup"]
        },
        "management_hints": "Treat underlying cause. Iron deficiency → Iron supplementation. B12/folate deficiency → Replacement. Consider transfusion if severe. Address underlying cause (GI bleed, nutritional, etc.)."
    }
}

__all__ = ['PALPITATIONS_DDX']

