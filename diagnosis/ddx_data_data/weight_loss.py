"""DDx Knowledge Base - Data
Differential diagnosis data for common clinical scenarios

NOTE: This file contains only data dictionaries.
Functions are in ddx_data.py"""

# Weight Loss Differential Diagnosis

WEIGHT_LOSS_DDX = {
    "Malignancy": {
        "symptoms": {
            "required": ["unintentional_weight_loss"],
            "supporting": ["rapid_weight_loss", "anorexia", "fatigue", "night_sweats", "lymphadenopathy", "mass", "bleeding", "age_>50"],
            "contradictory": ["intentional_weight_loss", "young_age"]
        },
        "demographics": {
            "age_risk": {"<40": 0.2, "40-70": 0.6, ">70": 0.8},
            "sex_risk": {"male": 1.1, "female": 1.0}
        },
        "risk_factors": ["age", "smoking", "alcohol", "family_history", "prior_cancer", "occupational_exposure"],
        "specificity": 0.75,
        "urgency": "urgent",
        "rule_out_first": True,
        "workup": {
            "immediate": ["CBC", "Comprehensive_metabolic_panel", "Chest_Xray", "CT_chest_abdomen_pelvis"],
            "within_6h": ["Tumor_markers", "PET_scan_if_indicated"],
            "optional": ["Biopsy", "Endoscopy"]
        },
        "management_hints": "URGENT! Unintentional weight loss in older adults often indicates malignancy. Comprehensive workup for primary tumor. Early diagnosis improves outcomes. Consider age-appropriate cancer screening."
    },
    "Hyperthyroidism": {
        "symptoms": {
            "required": ["weight_loss"],
            "supporting": ["increased_appetite", "tachycardia", "palpitations", "heat_intolerance", "sweating", "tremor", "anxiety", "diarrhea"],
            "contradictory": ["decreased_appetite", "cold_intolerance"]
        },
        "demographics": {
            "age_risk": {"<40": 0.5, "40-70": 0.6, ">70": 0.4},
            "sex_risk": {"male": 0.3, "female": 1.7}
        },
        "risk_factors": ["Graves_disease", "toxic_nodule", "thyroiditis", "iodine_exposure", "family_history"],
        "specificity": 0.85,
        "urgency": "urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["TSH", "Free_T4", "Free_T3", "ECG"],
            "within_6h": ["Thyroid_antibodies", "Thyroid_ultrasound"],
            "optional": ["Radioactive_iodine_uptake"]
        },
        "management_hints": "Treatment: Antithyroid drugs (methimazole, PTU), beta-blockers for symptoms. Consider radioactive iodine or surgery. Monitor for thyroid storm. Weight usually normalizes with treatment."
    },
    "Depression": {
        "symptoms": {
            "required": ["weight_loss"],
            "supporting": ["decreased_appetite", "anhedonia", "fatigue", "insomnia", "poor_concentration", "feelings_of_worthlessness", "suicidal_ideation"],
            "contradictory": ["increased_appetite", "no_psychiatric_symptoms"]
        },
        "demographics": {
            "age_risk": {"<40": 0.4, "40-70": 0.5, ">70": 0.6},
            "sex_risk": {"male": 0.7, "female": 1.3}
        },
        "risk_factors": ["prior_depression", "stress", "trauma", "substance_use", "chronic_illness", "medication"],
        "specificity": 0.70,
        "urgency": "non_urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["Psychiatric_evaluation", "PHQ_9", "CBC", "TSH", "B12"],
            "within_6h": [],
            "optional": ["Psychological_testing"]
        },
        "management_hints": "Treatment: Antidepressants (SSRIs, SNRIs), psychotherapy (CBT), lifestyle modifications. Screen for suicidal ideation. Address underlying causes. Weight usually improves with treatment."
    },
    "Diabetes (Uncontrolled)": {
        "symptoms": {
            "required": ["weight_loss"],
            "supporting": ["polyuria", "polydipsia", "polyphagia", "elevated_glucose", "fatigue", "blurred_vision", "increased_appetite"],
            "contradictory": ["normal_glucose", "no_diabetes_symptoms"]
        },
        "demographics": {
            "age_risk": {"<40": 0.5, "40-70": 0.6, ">70": 0.5},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["diabetes", "poor_glucose_control", "medication_noncompliance", "diet", "obesity"],
        "specificity": 0.80,
        "urgency": "urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["Glucose", "HbA1c", "Urinalysis", "Ketones"],
            "within_6h": ["C_peptide", "Autoantibodies_if_type_1_suspected"],
            "optional": []
        },
        "management_hints": "Uncontrolled diabetes causes weight loss due to glucosuria and catabolism. Treatment: Optimize glucose control (insulin, oral medications, diet). Monitor for DKA. Weight stabilizes with good control."
    },
    "Malabsorption": {
        "symptoms": {
            "required": ["weight_loss"],
            "supporting": ["diarrhea", "steatorrhea", "bloating", "abdominal_pain", "deficiency_symptoms", "anemia", "vitamin_deficiencies"],
            "contradictory": ["normal_stools", "no_GI_symptoms"]
        },
        "demographics": {
            "age_risk": {"<40": 0.5, "40-70": 0.4, ">70": 0.3},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["celiac_disease", "Crohn_disease", "pancreatic_insufficiency", "small_bowel_resection", "bacterial_overgrowth"],
        "specificity": 0.75,
        "urgency": "non_urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["CBC", "Iron_studies", "B12", "Folate", "Albumin", "Stool_fat"],
            "within_6h": ["Celiac_antibodies", "Endoscopy_with_biopsy"],
            "optional": ["Small_bowel_series", "Breath_test"]
        },
        "management_hints": "Treat underlying cause. Celiac → Gluten-free diet. Pancreatic insufficiency → Enzyme replacement. Bacterial overgrowth → Antibiotics. Nutritional support. Address deficiencies."
    },
    "Chronic Infection (TB, HIV)": {
        "symptoms": {
            "required": ["weight_loss"],
            "supporting": ["fever", "night_sweats", "fatigue", "cough", "lymphadenopathy", "exposure_history", "immunocompromised"],
            "contradictory": ["no_fever", "no_exposure"]
        },
        "demographics": {
            "age_risk": {"<40": 0.5, "40-70": 0.4, ">70": 0.3},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["TB_exposure", "HIV", "immunocompromised", "travel", "homelessness", "substance_use"],
        "specificity": 0.70,
        "urgency": "urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["CBC", "Chest_Xray", "TB_testing", "HIV_testing"],
            "within_6h": ["Sputum_cultures", "CD4_count_if_HIV"],
            "optional": ["CT_chest", "Biopsy"]
        },
        "management_hints": "TB → Anti-TB therapy (RIPE regimen). HIV → Antiretroviral therapy. Supportive care. Monitor for complications. Public health notification if TB. Weight improves with treatment."
    }
}

__all__ = ['WEIGHT_LOSS_DDX']

