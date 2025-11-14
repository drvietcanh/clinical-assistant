"""DDx Knowledge Base - Data
Differential diagnosis data for common clinical scenarios

NOTE: This file contains only data dictionaries.
Functions are in ddx_data.py"""

# Swelling (Edema) Differential Diagnosis

SWELLING_DDX = {
    "Heart Failure": {
        "symptoms": {
            "required": ["swelling", "edema"],
            "supporting": ["bilateral_legs", "pitting_edema", "dyspnea", "orthopnea", "PND", "elevated_JVP", "S3", "rales", "cardiomegaly"],
            "contradictory": ["unilateral", "no_cardiac_symptoms"]
        },
        "demographics": {
            "age_risk": {"<40": 0.2, "40-70": 0.5, ">70": 0.8},
            "sex_risk": {"male": 1.1, "female": 1.0}
        },
        "risk_factors": ["hypertension", "CAD", "MI", "diabetes", "atrial_fibrillation", "valvular_disease", "cardiomyopathy"],
        "specificity": 0.85,
        "urgency": "urgent",
        "rule_out_first": True,
        "workup": {
            "immediate": ["BNP", "NT_proBNP", "Chest_Xray", "ECG", "Echo"],
            "within_6h": ["CMP", "Troponin"],
            "optional": ["Cardiac_catheterization"]
        },
        "management_hints": "URGENT! Heart failure requires immediate treatment. Diuretics (furosemide), ACE inhibitors/ARB, beta-blockers. Salt restriction. Monitor daily weights. Treat underlying cause."
    },
    "Deep Vein Thrombosis (DVT)": {
        "symptoms": {
            "required": ["swelling", "edema"],
            "supporting": ["unilateral_leg", "calf_pain", "tenderness", "warmth", "redness", "recent_surgery", "immobility", "cancer", "pregnancy"],
            "contradictory": ["bilateral", "no_pain", "chronic"]
        },
        "demographics": {
            "age_risk": {"<40": 0.3, "40-70": 0.5, ">70": 0.6},
            "sex_risk": {"male": 1.0, "female": 1.2}
        },
        "risk_factors": ["immobility", "surgery", "cancer", "pregnancy", "OCP", "thrombophilia", "prior_DVT", "trauma"],
        "specificity": 0.80,
        "urgency": "urgent",
        "rule_out_first": True,
        "workup": {
            "immediate": ["D_dimer", "Doppler_ultrasound", "Wells_score"],
            "within_6h": ["Anticoagulation_if_positive"],
            "optional": ["CT_venography", "Thrombophilia_panel"]
        },
        "management_hints": "URGENT! DVT requires anticoagulation (DOAC or warfarin). Compression stockings. Elevation. Monitor for PE. Duration: 3-6 months minimum. Consider extended anticoagulation if recurrent or high risk."
    },
    "Lymphedema": {
        "symptoms": {
            "required": ["swelling", "edema"],
            "supporting": ["unilateral_or_bilateral", "non_pitting", "chronic", "skin_thickening", "recurrent_cellulitis", "prior_surgery", "radiation", "cancer"],
            "contradictory": ["pitting", "acute_onset"]
        },
        "demographics": {
            "age_risk": {"<40": 0.3, "40-70": 0.5, ">70": 0.6},
            "sex_risk": {"male": 0.8, "female": 1.2}
        },
        "risk_factors": ["cancer_surgery", "radiation", "lymph_node_dissection", "infection", "congenital", "obesity"],
        "specificity": 0.75,
        "urgency": "non_urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["Physical_exam", "History"],
            "within_6h": ["Lymphoscintigraphy"],
            "optional": ["MRI_lymphangiography"]
        },
        "management_hints": "Treatment: Compression therapy, manual lymphatic drainage, exercise. Elevation. Skin care to prevent infection. Complex decongestive therapy. Usually chronic and progressive."
    },
    "Nephrotic Syndrome": {
        "symptoms": {
            "required": ["swelling", "edema"],
            "supporting": ["bilateral", "pitting_edema", "periorbital_edema", "proteinuria", "hypoalbuminemia", "hyperlipidemia", "anasarca"],
            "contradictory": ["no_proteinuria", "normal_albumin"]
        },
        "demographics": {
            "age_risk": {"<40": 0.4, "40-70": 0.5, ">70": 0.4},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["diabetes", "SLE", "amyloidosis", "membranous_nephropathy", "minimal_change_disease", "FSGS"],
        "specificity": 0.80,
        "urgency": "urgent",
        "rule_out_first": True,
        "workup": {
            "immediate": ["Urinalysis", "24h_urine_protein", "Albumin", "Lipid_panel", "Creatinine"],
            "within_6h": ["Renal_biopsy"],
            "optional": ["ANA", "Complement_levels"]
        },
        "management_hints": "URGENT! Nephrotic syndrome requires workup. Treatment: ACE inhibitors/ARB, diuretics, statins. Corticosteroids if indicated. Salt restriction. Monitor for complications (thrombosis, infection)."
    },
    "Liver Cirrhosis": {
        "symptoms": {
            "required": ["swelling", "edema"],
            "supporting": ["ascites", "peripheral_edema", "jaundice", "spider_angiomata", "palmar_erythema", "hepatosplenomegaly", "elevated_LFTs", "low_albumin"],
            "contradictory": ["normal_LFTs", "normal_albumin"]
        },
        "demographics": {
            "age_risk": {"<40": 0.2, "40-70": 0.6, ">70": 0.7},
            "sex_risk": {"male": 1.3, "female": 0.8}
        },
        "risk_factors": ["alcohol", "hepatitis_B", "hepatitis_C", "NAFLD", "autoimmune_hepatitis", "hemochromatosis"],
        "specificity": 0.85,
        "urgency": "urgent",
        "rule_out_first": True,
        "workup": {
            "immediate": ["LFTs", "Albumin", "PT_INR", "Bilirubin", "Ultrasound_abdomen"],
            "within_6h": ["Hepatitis_serology", "AFP"],
            "optional": ["Liver_biopsy", "CT_abdomen"]
        },
        "management_hints": "URGENT! Cirrhosis requires comprehensive management. Diuretics (spironolactone + furosemide), salt restriction. Paracentesis if tense ascites. Screen for varices, HCC. Consider liver transplant evaluation."
    },
    "Venous Insufficiency": {
        "symptoms": {
            "required": ["swelling", "edema"],
            "supporting": ["bilateral_legs", "pitting_edema", "worse_evening", "varicose_veins", "stasis_dermatitis", "ulceration", "chronic"],
            "contradictory": ["unilateral", "acute_onset", "no_varicose_veins"]
        },
        "demographics": {
            "age_risk": {"<40": 0.2, "40-70": 0.5, ">70": 0.7},
            "sex_risk": {"male": 0.8, "female": 1.2}
        },
        "risk_factors": ["age", "pregnancy", "obesity", "prolonged_standing", "prior_DVT", "family_history"],
        "specificity": 0.75,
        "urgency": "non_urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["Physical_exam", "Doppler_ultrasound"],
            "within_6h": [],
            "optional": ["Venography"]
        },
        "management_hints": "Treatment: Compression stockings, elevation, exercise. Weight loss if obese. Avoid prolonged standing. Venous ablation if severe. Usually chronic but manageable."
    },
    "Medication-Induced Edema": {
        "symptoms": {
            "required": ["swelling", "edema"],
            "supporting": ["medication_use", "recent_medication_start", "CCB", "NSAID", "steroids", "thiazolidinediones", "dose_related"],
            "contradictory": ["no_medication_use"]
        },
        "demographics": {
            "age_risk": {"<40": 0.3, "40-70": 0.5, ">70": 0.6},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["CCB", "NSAID", "steroids", "thiazolidinediones", "pregabalin", "gabapentin", "multiple_medications"],
        "specificity": 0.70,
        "urgency": "non_urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["Medication_review", "Physical_exam"],
            "within_6h": [],
            "optional": []
        },
        "management_hints": "Review medications. Reduce dose or discontinue if possible. Switch to alternative medication. Diuretics may help. Most cases improve with medication adjustment."
    },
    "Hypothyroidism": {
        "symptoms": {
            "required": ["swelling", "edema"],
            "supporting": ["myxedema", "periorbital_edema", "non_pitting", "fatigue", "cold_intolerance", "weight_gain", "elevated_TSH", "low_T4"],
            "contradictory": ["normal_thyroid_function", "pitting_edema"]
        },
        "demographics": {
            "age_risk": {"<40": 0.3, "40-70": 0.5, ">70": 0.6},
            "sex_risk": {"male": 0.3, "female": 1.7}
        },
        "risk_factors": ["Hashimoto_thyroiditis", "prior_thyroid_surgery", "radiation", "iodine_deficiency", "autoimmune"],
        "specificity": 0.75,
        "urgency": "non_urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["TSH", "Free_T4"],
            "within_6h": ["Thyroid_antibodies"],
            "optional": ["Thyroid_ultrasound"]
        },
        "management_hints": "Treatment: Levothyroxine replacement. Start low dose, titrate based on TSH. Edema improves with thyroid replacement. Monitor TSH every 6-8 weeks until stable."
    }
}

__all__ = ['SWELLING_DDX']

