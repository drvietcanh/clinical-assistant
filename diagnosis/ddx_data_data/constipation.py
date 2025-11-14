"""DDx Knowledge Base - Data
Differential diagnosis data for common clinical scenarios

NOTE: This file contains only data dictionaries.
Functions are in ddx_data.py"""

# Constipation Differential Diagnosis

CONSTIPATION_DDX = {
    "Functional Constipation": {
        "symptoms": {
            "required": ["constipation"],
            "supporting": ["chronic", "infrequent_bowel_movements", "hard_stools", "straining", "incomplete_evacuation", "no_alarm_symptoms"],
            "contradictory": ["blood_in_stool", "weight_loss", "anemia", "family_history_colon_cancer"]
        },
        "demographics": {
            "age_risk": {"<40": 0.5, "40-70": 0.4, ">70": 0.3},
            "sex_risk": {"male": 0.7, "female": 1.3}
        },
        "risk_factors": ["low_fiber_diet", "inadequate_fluids", "sedentary_lifestyle", "ignoring_urge", "stress"],
        "specificity": 0.70,
        "urgency": "non_urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["History", "Physical_exam"],
            "within_6h": ["CBC_if_alarm_symptoms"],
            "optional": ["Colonoscopy_if_age_>50_or_alarm_symptoms"]
        },
        "management_hints": "Treatment: Increase fiber, fluids, exercise. Laxatives if needed (osmotic: polyethylene glycol, stimulant: senna). Biofeedback for pelvic floor dysfunction. Lifestyle modifications."
    },
    "Bowel Obstruction": {
        "symptoms": {
            "required": ["constipation"],
            "supporting": ["abdominal_distension", "abdominal_pain", "nausea", "vomiting", "no_flatus", "no_bowel_sounds", "acute_onset"],
            "contradictory": ["flatus", "normal_bowel_sounds", "chronic"]
        },
        "demographics": {
            "age_risk": {"<40": 0.3, "40-70": 0.5, ">70": 0.7},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["prior_surgery", "adhesions", "hernia", "tumor", "volvulus", "intussusception"],
        "specificity": 0.85,
        "urgency": "emergency",
        "rule_out_first": True,
        "workup": {
            "immediate": ["Abdominal_Xray", "CT_abdomen", "CBC", "Electrolytes"],
            "within_6h": ["Surgery_consult", "NG_tube"],
            "optional": ["Contrast_study"]
        },
        "management_hints": "URGENT! Bowel obstruction is a surgical emergency. NPO, NG tube decompression, IV fluids. Surgery consult. Monitor for strangulation (fever, tachycardia, peritonitis)."
    },
    "Hypothyroidism": {
        "symptoms": {
            "required": ["constipation"],
            "supporting": ["fatigue", "cold_intolerance", "weight_gain", "dry_skin", "hair_loss", "bradycardia", "elevated_TSH"],
            "contradictory": ["normal_TSH", "hyperthyroid_symptoms"]
        },
        "demographics": {
            "age_risk": {"<40": 0.3, "40-70": 0.5, ">70": 0.6},
            "sex_risk": {"male": 0.3, "female": 1.7}
        },
        "risk_factors": ["Hashimoto_thyroiditis", "prior_thyroid_surgery", "radiation", "iodine_deficiency", "autoimmune"],
        "specificity": 0.80,
        "urgency": "non_urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["TSH", "Free_T4"],
            "within_6h": ["Thyroid_antibodies"],
            "optional": ["Thyroid_ultrasound"]
        },
        "management_hints": "Treatment: Levothyroxine replacement. Start low dose, titrate based on TSH. Constipation improves with thyroid replacement. Monitor TSH every 6-8 weeks until stable."
    },
    "Medication-Induced": {
        "symptoms": {
            "required": ["constipation"],
            "supporting": ["medication_use", "opioids", "anticholinergics", "calcium_channel_blockers", "iron", "recent_medication_start"],
            "contradictory": ["no_medication_use"]
        },
        "demographics": {
            "age_risk": {"<40": 0.3, "40-70": 0.5, ">70": 0.7},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["opioid_use", "multiple_medications", "elderly", "anticholinergics"],
        "specificity": 0.75,
        "urgency": "non_urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["Medication_review"],
            "within_6h": [],
            "optional": []
        },
        "management_hints": "Review medications. Opioids → Add laxatives (docusate, senna). Consider opioid rotation or reduction. Anticholinergics → Adjust if possible. Prophylactic laxatives if on opioids."
    },
    "Colorectal Cancer": {
        "symptoms": {
            "required": ["constipation"],
            "supporting": ["blood_in_stool", "change_in_bowel_habits", "narrow_stools", "weight_loss", "anemia", "age_>50", "family_history"],
            "contradictory": ["young_age", "no_alarm_symptoms"]
        },
        "demographics": {
            "age_risk": {"<40": 0.1, "40-70": 0.5, ">70": 0.8},
            "sex_risk": {"male": 1.1, "female": 1.0}
        },
        "risk_factors": ["age", "family_history", "polyps", "IBD", "diet", "smoking", "alcohol"],
        "specificity": 0.80,
        "urgency": "urgent",
        "rule_out_first": True,
        "workup": {
            "immediate": ["CBC", "FOBT", "Colonoscopy"],
            "within_6h": ["CT_colonography_if_colonoscopy_not_available"],
            "optional": ["CEA", "CT_staging"]
        },
        "management_hints": "URGENT! Colorectal cancer screening important. Colonoscopy for diagnosis and staging. Early detection improves outcomes. Surgical resection primary treatment. Consider chemotherapy/radiation based on stage."
    }
}

__all__ = ['CONSTIPATION_DDX']

