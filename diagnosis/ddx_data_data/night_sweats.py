"""DDx Knowledge Base - Data
Differential diagnosis data for common clinical scenarios

NOTE: This file contains only data dictionaries.
Functions are in ddx_data.py"""

# Night Sweats Differential Diagnosis

NIGHT_SWEATS_DDX = {
    "Tuberculosis": {
        "symptoms": {
            "required": ["night_sweats"],
            "supporting": ["fever", "weight_loss", "cough", "hemoptysis", "fatigue", "anorexia", "chest_pain", "exposure_history"],
            "contradictory": ["no_fever", "no_cough", "no_exposure"]
        },
        "demographics": {
            "age_risk": {"<40": 0.4, "40-70": 0.5, ">70": 0.4},
            "sex_risk": {"male": 1.2, "female": 1.0}
        },
        "risk_factors": ["TB_exposure", "HIV", "immunosuppression", "homelessness", "alcohol", "diabetes", "end_stage_renal_disease"],
        "specificity": 0.85,
        "urgency": "urgent",
        "rule_out_first": True,
        "workup": {
            "immediate": ["Chest_Xray", "Sputum_AFB", "Tuberculin_skin_test", "IGRA", "HIV_test"],
            "within_6h": ["CT_chest", "Sputum_culture"],
            "optional": ["Bronchoscopy", "Biopsy"]
        },
        "management_hints": "URGENT! TB is contagious and requires isolation. Treatment: 4-drug regimen (RIPE) for 6 months. Directly observed therapy (DOT). Contact tracing. Screen for HIV. Monitor for drug resistance."
    },
    "Lymphoma": {
        "symptoms": {
            "required": ["night_sweats"],
            "supporting": ["fever", "weight_loss", "lymphadenopathy", "fatigue", "pruritus", "splenomegaly", "hepatomegaly", "B_symptoms"],
            "contradictory": ["no_fever", "no_weight_loss", "no_lymphadenopathy"]
        },
        "demographics": {
            "age_risk": {"<40": 0.3, "40-70": 0.6, ">70": 0.7},
            "sex_risk": {"male": 1.1, "female": 1.0}
        },
        "risk_factors": ["age", "immunosuppression", "HIV", "EBV", "family_history", "prior_chemotherapy"],
        "specificity": 0.80,
        "urgency": "urgent",
        "rule_out_first": True,
        "workup": {
            "immediate": ["CBC", "LDH", "Chest_Xray", "CT_chest_abdomen_pelvis"],
            "within_6h": ["Lymph_node_biopsy", "Bone_marrow_biopsy"],
            "optional": ["PET_scan", "Flow_cytometry"]
        },
        "management_hints": "URGENT! Lymphoma requires prompt diagnosis and staging. Treatment: Chemotherapy (ABVD for Hodgkin, R-CHOP for NHL), radiation. Prognosis depends on type and stage. Early treatment improves outcomes."
    },
    "HIV Infection": {
        "symptoms": {
            "required": ["night_sweats"],
            "supporting": ["fever", "weight_loss", "lymphadenopathy", "fatigue", "rash", "oral_thrush", "diarrhea", "risk_factors"],
            "contradictory": ["no_risk_factors", "negative_HIV_test"]
        },
        "demographics": {
            "age_risk": {"<40": 0.6, "40-70": 0.4, ">70": 0.2},
            "sex_risk": {"male": 1.2, "female": 0.9}
        },
        "risk_factors": ["unprotected_sex", "IV_drug_use", "MSM", "blood_transfusion", "occupational_exposure"],
        "specificity": 0.75,
        "urgency": "urgent",
        "rule_out_first": True,
        "workup": {
            "immediate": ["HIV_antibody", "HIV_RNA", "CD4_count", "Viral_load"],
            "within_6h": ["CBC", "CMP", "Hepatitis_serology"],
            "optional": ["Genotypic_resistance_testing"]
        },
        "management_hints": "URGENT! HIV requires immediate diagnosis and treatment. Start ART regardless of CD4 count. Monitor CD4 and viral load. Screen for opportunistic infections. Partner notification and testing."
    },
    "Hyperthyroidism": {
        "symptoms": {
            "required": ["night_sweats"],
            "supporting": ["heat_intolerance", "weight_loss", "tachycardia", "tremor", "anxiety", "insomnia", "elevated_T4", "low_TSH"],
            "contradictory": ["normal_thyroid_function", "cold_intolerance"]
        },
        "demographics": {
            "age_risk": {"<40": 0.5, "40-70": 0.4, ">70": 0.3},
            "sex_risk": {"male": 0.3, "female": 1.7}
        },
        "risk_factors": ["Graves_disease", "toxic_nodule", "thyroiditis", "iodine_excess", "autoimmune"],
        "specificity": 0.75,
        "urgency": "non_urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["TSH", "Free_T4", "Free_T3"],
            "within_6h": ["Thyroid_antibodies", "Thyroid_ultrasound"],
            "optional": ["Radioactive_iodine_uptake"]
        },
        "management_hints": "Treatment: Antithyroid medications (methimazole, PTU), beta-blockers for symptoms. Radioactive iodine or surgery if refractory. Night sweats improve with thyroid normalization."
    },
    "Medication-Induced": {
        "symptoms": {
            "required": ["night_sweats"],
            "supporting": ["medication_use", "recent_medication_start", "antidepressants", "antipsychotics", "hormones", "dose_related"],
            "contradictory": ["no_medication_use"]
        },
        "demographics": {
            "age_risk": {"<40": 0.4, "40-70": 0.5, ">70": 0.6},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["antidepressants", "antipsychotics", "hormone_replacement", "tamoxifen", "opioids", "withdrawal"],
        "specificity": 0.70,
        "urgency": "non_urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["Medication_review", "History"],
            "within_6h": [],
            "optional": []
        },
        "management_hints": "Review medications. Reduce dose or discontinue if possible. Switch to alternative medication. Most cases improve with medication adjustment. Consider timing of medication (take earlier in day)."
    },
    "Menopause": {
        "symptoms": {
            "required": ["night_sweats"],
            "supporting": ["hot_flashes", "irregular_periods", "vaginal_dryness", "mood_changes", "age_40_60", "female", "insomnia"],
            "contradictory": ["male", "young_age", "regular_periods"]
        },
        "demographics": {
            "age_risk": {"<40": 0.1, "40-70": 0.8, ">70": 0.3},
            "sex_risk": {"male": 0.0, "female": 1.0}
        },
        "risk_factors": ["age", "female", "surgical_menopause", "chemotherapy", "radiation"],
        "specificity": 0.80,
        "urgency": "non_urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["History", "Physical_exam"],
            "within_6h": ["FSH", "LH", "Estradiol"],
            "optional": []
        },
        "management_hints": "Treatment: Hormone replacement therapy (HRT) if appropriate. Non-hormonal options: SSRIs, gabapentin, clonidine. Lifestyle: Cool environment, cotton clothing, stress reduction. Usually self-limited."
    },
    "Anxiety / Panic Disorder": {
        "symptoms": {
            "required": ["night_sweats"],
            "supporting": ["anxiety", "panic_attacks", "insomnia", "palpitations", "tremor", "hyperventilation", "stress", "psychiatric_history"],
            "contradictory": ["no_anxiety", "no_stress"]
        },
        "demographics": {
            "age_risk": {"<40": 0.5, "40-70": 0.4, ">70": 0.3},
            "sex_risk": {"male": 0.7, "female": 1.3}
        },
        "risk_factors": ["stress", "trauma", "family_history", "substance_use", "medical_illness"],
        "specificity": 0.65,
        "urgency": "non_urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["History", "Psychiatric_evaluation"],
            "within_6h": [],
            "optional": ["Thyroid_function", "CBC"]
        },
        "management_hints": "Treatment: Psychotherapy (CBT), SSRIs, benzodiazepines (short-term). Stress management, relaxation techniques. Address underlying anxiety. Usually improves with treatment."
    },
    "Brucellosis": {
        "symptoms": {
            "required": ["night_sweats"],
            "supporting": ["fever", "weight_loss", "fatigue", "joint_pain", "back_pain", "exposure_to_animals", "unpasteurized_dairy", "endemic_area"],
            "contradictory": ["no_fever", "no_exposure"]
        },
        "demographics": {
            "age_risk": {"<40": 0.5, "40-70": 0.4, ">70": 0.3},
            "sex_risk": {"male": 1.2, "female": 0.9}
        },
        "risk_factors": ["animal_exposure", "unpasteurized_dairy", "occupational", "travel_to_endemic_area"],
        "specificity": 0.70,
        "urgency": "urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["Blood_culture", "Serology", "CBC", "CMP"],
            "within_6h": ["Bone_marrow_culture"],
            "optional": ["PCR"]
        },
        "management_hints": "Treatment: Doxycycline + rifampin or streptomycin for 6 weeks. Monitor for complications (endocarditis, osteomyelitis). Usually curable with appropriate antibiotics."
    }
}

__all__ = ['NIGHT_SWEATS_DDX']

