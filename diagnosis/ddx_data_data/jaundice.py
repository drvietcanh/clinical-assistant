"""DDx Knowledge Base - Data
Differential diagnosis data for common clinical scenarios

NOTE: This file contains only data dictionaries.
Functions are in ddx_data.py"""

# Jaundice Differential Diagnosis

JAUNDICE_DDX = {
    "Biliary Obstruction": {
        "symptoms": {
            "required": ["jaundice"],
            "supporting": ["dark_urine", "clay_colored_stools", "pruritus", "abdominal_pain", "fever", "elevated_direct_bilirubin", "elevated_alkaline_phosphatase"],
            "contradictory": ["normal_alkaline_phosphatase", "elevated_indirect_bilirubin_only"]
        },
        "demographics": {
            "age_risk": {"<40": 0.3, "40-70": 0.6, ">70": 0.7},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["gallstones", "pancreatic_cancer", "cholangiocarcinoma", "stricture", "pancreatitis"],
        "specificity": 0.85,
        "urgency": "emergency",
        "rule_out_first": True,
        "workup": {
            "immediate": ["LFTs", "Bilirubin_fractionation", "Ultrasound_abdomen", "CT_abdomen"],
            "within_6h": ["MRCP", "ERCP_if_obstruction_confirmed"],
            "optional": ["Endoscopic_ultrasound", "Biopsy"]
        },
        "management_hints": "URGENT! Biliary obstruction can lead to cholangitis (life-threatening). ERCP for decompression. Treat underlying cause (stones, tumor, stricture). Antibiotics if cholangitis suspected."
    },
    "Hepatitis (Viral)": {
        "symptoms": {
            "required": ["jaundice"],
            "supporting": ["fatigue", "nausea", "vomiting", "abdominal_pain", "elevated_ALT_AST", "elevated_both_bilirubin", "fever", "dark_urine"],
            "contradictory": ["normal_ALT_AST"]
        },
        "demographics": {
            "age_risk": {"<40": 0.5, "40-70": 0.4, ">70": 0.3},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["viral_exposure", "travel", "IV_drug_use", "sexual_contact", "blood_transfusion", "alcohol"],
        "specificity": 0.80,
        "urgency": "urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["LFTs", "Viral_hepatitis_panel", "CBC", "Coagulation_studies"],
            "within_6h": ["Ultrasound_liver", "Autoimmune_markers"],
            "optional": ["Liver_biopsy", "Viral_load"]
        },
        "management_hints": "Supportive care. Hepatitis A → Self-limited. Hepatitis B/C → Antiviral therapy if indicated. Monitor for acute liver failure. Avoid hepatotoxic medications."
    },
    "Alcoholic Hepatitis": {
        "symptoms": {
            "required": ["jaundice", "alcohol_use"],
            "supporting": ["elevated_ALT_AST", "AST_>_ALT", "elevated_bilirubin", "ascites", "hepatomegaly", "fever"],
            "contradictory": ["no_alcohol_use", "ALT_>_AST"]
        },
        "demographics": {
            "age_risk": {"<40": 0.3, "40-70": 0.7, ">70": 0.5},
            "sex_risk": {"male": 1.5, "female": 1.0}
        },
        "risk_factors": ["chronic_alcohol_use", "binge_drinking", "malnutrition", "obesity"],
        "specificity": 0.75,
        "urgency": "urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["LFTs", "Bilirubin", "MELD_score", "Maddrey_score", "CBC", "Coagulation"],
            "within_6h": ["Ultrasound_liver", "CT_abdomen"],
            "optional": ["Liver_biopsy"]
        },
        "management_hints": "Stop alcohol immediately. Supportive care. Consider steroids if Maddrey score >32. Monitor for complications (ascites, encephalopathy, varices). Consider liver transplant evaluation if severe."
    },
    "Hemolytic Anemia": {
        "symptoms": {
            "required": ["jaundice"],
            "supporting": ["elevated_indirect_bilirubin", "anemia", "reticulocytosis", "elevated_LDH", "low_haptoglobin", "dark_urine", "splenomegaly"],
            "contradictory": ["elevated_direct_bilirubin", "low_reticulocyte_count"]
        },
        "demographics": {
            "age_risk": {"<40": 0.5, "40-70": 0.4, ">70": 0.3},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["autoimmune", "medication", "infection", "mechanical_hemolysis", "G6PD_deficiency", "sickle_cell"],
        "specificity": 0.80,
        "urgency": "urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["CBC", "Reticulocyte_count", "LDH", "Haptoglobin", "Bilirubin_fractionation", "Peripheral_smear"],
            "within_6h": ["Direct_Coombs_test", "G6PD_level"],
            "optional": ["Hemoglobin_electrophoresis", "Bone_marrow_biopsy"]
        },
        "management_hints": "Treat underlying cause. Autoimmune → Steroids, IVIG, or rituximab. Medication-induced → Stop medication. Supportive care (transfusion if needed). Consider splenectomy if refractory."
    },
    "Gilbert Syndrome": {
        "symptoms": {
            "required": ["jaundice"],
            "supporting": ["mild_jaundice", "elevated_indirect_bilirubin_only", "intermittent", "stress_induced", "fasting_induced", "young_age", "asymptomatic"],
            "contradictory": ["elevated_direct_bilirubin", "severe_jaundice", "symptoms"]
        },
        "demographics": {
            "age_risk": {"<40": 0.8, "40-70": 0.2, ">70": 0.1},
            "sex_risk": {"male": 1.5, "female": 1.0}
        },
        "risk_factors": ["family_history", "fasting", "illness", "stress"],
        "specificity": 0.90,
        "urgency": "non_urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["Bilirubin_fractionation", "LFTs"],
            "within_6h": ["Genetic_testing_if_needed"],
            "optional": []
        },
        "management_hints": "Benign condition. No treatment needed. Reassurance. Bilirubin typically <3-4 mg/dL, indirect only. No hemolysis or liver disease. Genetic condition (UGT1A1 mutation)."
    },
    "Drug-Induced Liver Injury": {
        "symptoms": {
            "required": ["jaundice", "medication_use"],
            "supporting": ["elevated_ALT_AST", "elevated_bilirubin", "recent_medication_start", "rash", "fever", "eosinophilia"],
            "contradictory": ["no_medication_use", "normal_LFTs"]
        },
        "demographics": {
            "age_risk": {"<40": 0.4, "40-70": 0.6, ">70": 0.7},
            "sex_risk": {"male": 0.8, "female": 1.2}
        },
        "risk_factors": ["multiple_medications", "elderly", "alcohol_use", "preexisting_liver_disease", "specific_drugs"],
        "specificity": 0.75,
        "urgency": "urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["LFTs", "Bilirubin", "Stop_suspected_medication", "CBC"],
            "within_6h": ["Ultrasound_liver", "Autoimmune_markers"],
            "optional": ["Liver_biopsy"]
        },
        "management_hints": "Stop suspected medication immediately. Supportive care. Monitor LFTs. Most cases resolve with drug discontinuation. Consider N-acetylcysteine if acetaminophen toxicity. Severe cases may need liver transplant evaluation."
    }
}

__all__ = ['JAUNDICE_DDX']

