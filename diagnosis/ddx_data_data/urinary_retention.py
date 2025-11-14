"""DDx Knowledge Base - Data
Differential diagnosis data for common clinical scenarios

NOTE: This file contains only data dictionaries.
Functions are in ddx_data.py"""

# Urinary Retention Differential Diagnosis

URINARY_RETENTION_DDX = {
    "Benign Prostatic Hyperplasia (BPH)": {
        "symptoms": {
            "required": ["urinary_retention"],
            "supporting": ["male", "age_>50", "hesitancy", "weak_stream", "incomplete_emptying", "frequency", "nocturia", "enlarged_prostate"],
            "contradictory": ["female", "young_age"]
        },
        "demographics": {
            "age_risk": {"<40": 0.1, "40-70": 0.6, ">70": 0.9},
            "sex_risk": {"male": 1.0, "female": 0.0}
        },
        "risk_factors": ["age", "male", "family_history", "diabetes", "obesity"],
        "specificity": 0.85,
        "urgency": "urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["Post_void_residual", "Prostate_exam", "PSA", "Urinalysis"],
            "within_6h": ["Uroflowmetry", "Urology_consult"],
            "optional": ["Cystoscopy", "Urodynamics"]
        },
        "management_hints": "Acute retention → Urgent catheterization. Treatment: Alpha-blockers (tamsulosin), 5-alpha-reductase inhibitors (finasteride), or combination. Surgery (TURP) if medical therapy fails or severe."
    },
    "Neurogenic Bladder": {
        "symptoms": {
            "required": ["urinary_retention"],
            "supporting": ["neurologic_disease", "spinal_cord_injury", "diabetes", "multiple_sclerosis", "Parkinson", "stroke", "loss_of_sensation"],
            "contradictory": ["no_neurologic_disease"]
        },
        "demographics": {
            "age_risk": {"<40": 0.4, "40-70": 0.5, ">70": 0.6},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["diabetes", "spinal_cord_injury", "multiple_sclerosis", "stroke", "Parkinson", "peripheral_neuropathy"],
        "specificity": 0.80,
        "urgency": "urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["Post_void_residual", "Neurologic_exam", "Urinalysis"],
            "within_6h": ["Urodynamics", "Urology_consult"],
            "optional": ["MRI_spine", "EMG"]
        },
        "management_hints": "Treatment: Intermittent catheterization, anticholinergics, or botulinum toxin. Treat underlying neurologic condition. Monitor for complications (UTI, renal damage)."
    },
    "Medication-Induced": {
        "symptoms": {
            "required": ["urinary_retention"],
            "supporting": ["medication_use", "anticholinergics", "opioids", "antidepressants", "antihistamines", "recent_medication_start"],
            "contradictory": ["no_medication_use"]
        },
        "demographics": {
            "age_risk": {"<40": 0.3, "40-70": 0.5, ">70": 0.7},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["multiple_medications", "elderly", "anticholinergics", "opioids"],
        "specificity": 0.75,
        "urgency": "urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["Medication_review", "Post_void_residual", "Urinalysis"],
            "within_6h": [],
            "optional": []
        },
        "management_hints": "Review medications. Discontinue or adjust anticholinergics if possible. Acute retention → Catheterization. Consider bethanechol if needed. Most cases resolve with medication adjustment."
    },
    "Spinal Cord Compression": {
        "symptoms": {
            "required": ["urinary_retention"],
            "supporting": ["back_pain", "leg_weakness", "sensory_loss", "bowel_dysfunction", "saddle_anesthesia", "rapid_onset"],
            "contradictory": ["no_neurologic_symptoms"]
        },
        "demographics": {
            "age_risk": {"<40": 0.3, "40-70": 0.6, ">70": 0.7},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["metastatic_cancer", "trauma", "disc_herniation", "spinal_stenosis", "infection"],
        "specificity": 0.85,
        "urgency": "emergency",
        "rule_out_first": True,
        "workup": {
            "immediate": ["MRI_spine", "Neurologic_exam", "Neurosurgery_consult"],
            "within_6h": ["CT_spine", "Steroids_if_indicated"],
            "optional": ["Surgical_decompression"]
        },
        "management_hints": "URGENT! Spinal cord compression is a neurosurgical emergency. High-dose steroids. Urgent MRI. Neurosurgery consult for decompression. Catheterization for retention. Time critical."
    },
    "Urinary Tract Infection": {
        "symptoms": {
            "required": ["urinary_retention"],
            "supporting": ["dysuria", "frequency", "urgency", "fever", "suprapubic_pain", "cloudy_urine", "bacteriuria"],
            "contradictory": ["no_UTI_symptoms", "sterile_urine"]
        },
        "demographics": {
            "age_risk": {"<40": 0.4, "40-70": 0.5, ">70": 0.6},
            "sex_risk": {"male": 0.5, "female": 1.5}
        },
        "risk_factors": ["female", "catheter", "diabetes", "pregnancy", "sexual_activity", "structural_abnormalities"],
        "specificity": 0.70,
        "urgency": "urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["Urinalysis", "Urine_culture", "Post_void_residual"],
            "within_6h": ["Antibiotics", "Catheter_if_needed"],
            "optional": []
        },
        "management_hints": "Treatment: Antibiotics based on culture. Catheterization if retention. Retention may be due to inflammation. Usually resolves with UTI treatment. Consider urology consult if recurrent."
    }
}

__all__ = ['URINARY_RETENTION_DDX']

