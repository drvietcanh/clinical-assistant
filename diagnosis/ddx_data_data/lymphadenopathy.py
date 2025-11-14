"""DDx Knowledge Base - Data
Differential diagnosis data for common clinical scenarios

NOTE: This file contains only data dictionaries.
Functions are in ddx_data.py"""

# Lymphadenopathy Differential Diagnosis

LYMPHADENOPATHY_DDX = {
    "Reactive Lymphadenopathy": {
        "symptoms": {
            "required": ["lymphadenopathy"],
            "supporting": ["tender", "soft", "mobile", "recent_infection", "fever", "localized", "resolves_with_time"],
            "contradictory": ["hard", "fixed", "rapid_growth", "generalized"]
        },
        "demographics": {
            "age_risk": {"<40": 0.7, "40-70": 0.5, ">70": 0.3},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["recent_infection", "viral_illness", "bacterial_infection", "local_inflammation"],
        "specificity": 0.70,
        "urgency": "non_urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["CBC", "Physical_exam"],
            "within_6h": ["ESR_CRP", "Infection_workup_if_indicated"],
            "optional": ["Ultrasound", "Biopsy_if_persistent"]
        },
        "management_hints": "Benign reactive lymphadenopathy usually resolves spontaneously. Treat underlying infection if present. Monitor if persistent. Biopsy if >4-6 weeks, >2cm, or concerning features."
    },
    "Lymphoma": {
        "symptoms": {
            "required": ["lymphadenopathy"],
            "supporting": ["hard", "rubbery", "non_tender", "rapid_growth", "generalized", "B_symptoms", "night_sweats", "weight_loss", "fever"],
            "contradictory": ["tender", "soft", "localized_only"]
        },
        "demographics": {
            "age_risk": {"<40": 0.4, "40-70": 0.6, ">70": 0.5},
            "sex_risk": {"male": 1.2, "female": 1.0}
        },
        "risk_factors": ["immunocompromised", "EBV_infection", "family_history", "autoimmune_disease", "HIV"],
        "specificity": 0.85,
        "urgency": "urgent",
        "rule_out_first": True,
        "workup": {
            "immediate": ["CBC", "LDH", "CT_chest_abdomen_pelvis", "Excisional_biopsy"],
            "within_6h": ["Bone_marrow_biopsy", "PET_scan"],
            "optional": ["Flow_cytometry", "Genetic_testing"]
        },
        "management_hints": "URGENT! Lymphoma requires prompt diagnosis and staging. Excisional biopsy (not FNA) for diagnosis. Staging with PET scan. Treatment: Chemotherapy, radiation, or immunotherapy based on type and stage."
    },
    "Infection (Viral/Bacterial/TB)": {
        "symptoms": {
            "required": ["lymphadenopathy"],
            "supporting": ["tender", "fever", "recent_exposure", "travel_history", "tuberculosis_risk", "HIV_risk", "localized", "draining_sinus"],
            "contradictory": ["no_fever", "no_exposure"]
        },
        "demographics": {
            "age_risk": {"<40": 0.6, "40-70": 0.4, ">70": 0.3},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["viral_infection", "bacterial_infection", "tuberculosis", "HIV", "travel", "immunocompromised"],
        "specificity": 0.75,
        "urgency": "urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["CBC", "ESR_CRP", "Cultures", "Chest_Xray"],
            "within_6h": ["TB_testing", "HIV_testing", "Viral_serologies"],
            "optional": ["Biopsy_with_cultures", "PCR_testing"]
        },
        "management_hints": "Treat underlying infection. Viral → Supportive care. Bacterial → Antibiotics. TB → Anti-TB therapy. HIV → Antiretroviral therapy. Consider biopsy if diagnosis uncertain."
    },
    "Metastatic Cancer": {
        "symptoms": {
            "required": ["lymphadenopathy"],
            "supporting": ["hard", "fixed", "non_tender", "rapid_growth", "known_cancer", "weight_loss", "localized_to_drainage_area"],
            "contradictory": ["tender", "soft", "mobile"]
        },
        "demographics": {
            "age_risk": {"<40": 0.2, "40-70": 0.6, ">70": 0.8},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["known_cancer", "smoking", "alcohol", "age", "family_history"],
        "specificity": 0.80,
        "urgency": "urgent",
        "rule_out_first": True,
        "workup": {
            "immediate": ["CBC", "Imaging", "FNA_or_biopsy"],
            "within_6h": ["PET_scan", "Primary_tumor_search"],
            "optional": ["Immunohistochemistry", "Genetic_testing"]
        },
        "management_hints": "URGENT! Metastatic cancer requires staging and treatment planning. Identify primary tumor. Biopsy for confirmation. Treatment: Surgery, chemotherapy, radiation, or immunotherapy based on primary and stage."
    },
    "Autoimmune Disease (SLE, RA)": {
        "symptoms": {
            "required": ["lymphadenopathy"],
            "supporting": ["joint_pain", "rash", "fever", "fatigue", "autoimmune_features", "generalized", "soft", "mobile"],
            "contradictory": ["no_autoimmune_features", "hard", "fixed"]
        },
        "demographics": {
            "age_risk": {"<40": 0.6, "40-70": 0.5, ">70": 0.3},
            "sex_risk": {"male": 0.3, "female": 1.7}
        },
        "risk_factors": ["SLE", "rheumatoid_arthritis", "Sjogren_syndrome", "family_history", "female"],
        "specificity": 0.70,
        "urgency": "non_urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["CBC", "ESR_CRP", "ANA", "RF", "Anti_CCP"],
            "within_6h": ["Autoimmune_panel", "Complement_levels"],
            "optional": ["Biopsy_if_uncertain"]
        },
        "management_hints": "Treat underlying autoimmune disease. SLE → Hydroxychloroquine, steroids, immunosuppressants. RA → DMARDs, biologics. Lymphadenopathy usually resolves with disease control."
    },
    "Drug Reaction": {
        "symptoms": {
            "required": ["lymphadenopathy", "medication_use"],
            "supporting": ["rash", "fever", "eosinophilia", "recent_medication_start", "generalized", "soft", "tender"],
            "contradictory": ["no_medication_use", "hard", "fixed"]
        },
        "demographics": {
            "age_risk": {"<40": 0.5, "40-70": 0.6, ">70": 0.7},
            "sex_risk": {"male": 0.8, "female": 1.2}
        },
        "risk_factors": ["multiple_medications", "specific_drugs", "allergy_history"],
        "specificity": 0.75,
        "urgency": "urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["CBC", "Stop_suspected_medication", "CBC_with_differential"],
            "within_6h": ["Drug_reaction_evaluation"],
            "optional": ["Biopsy_if_DRESS_suspected"]
        },
        "management_hints": "Stop suspected medication immediately. Supportive care. Monitor for DRESS syndrome (drug reaction with eosinophilia and systemic symptoms). Most cases resolve with drug discontinuation."
    }
}

__all__ = ['LYMPHADENOPATHY_DDX']

