"""DDx Knowledge Base - Data
Differential diagnosis data for common clinical scenarios

NOTE: This file contains only data dictionaries.
Functions are in ddx_data.py"""

# Hearing Loss Differential Diagnosis

HEARING_LOSS_DDX = {
    "Presbycusis (Age-Related Hearing Loss)": {
        "symptoms": {
            "required": ["hearing_loss"],
            "supporting": ["bilateral", "gradual_onset", "high_frequency", "age_>60", "difficulty_understanding_speech", "tinnitus"],
            "contradictory": ["unilateral", "sudden_onset", "young_age"]
        },
        "demographics": {
            "age_risk": {"<40": 0.1, "40-70": 0.4, ">70": 0.9},
            "sex_risk": {"male": 1.2, "female": 1.0}
        },
        "risk_factors": ["age", "noise_exposure", "smoking", "diabetes", "hypertension", "genetics"],
        "specificity": 0.85,
        "urgency": "non_urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["Audiometry", "Physical_exam"],
            "within_6h": ["Tympanometry"],
            "optional": ["MRI_if_atypical"]
        },
        "management_hints": "Treatment: Hearing aids, assistive listening devices. Noise protection. Regular audiometry monitoring. Address communication strategies. Consider cochlear implants if severe."
    },
    "Noise-Induced Hearing Loss": {
        "symptoms": {
            "required": ["hearing_loss"],
            "supporting": ["noise_exposure", "bilateral", "high_frequency", "gradual_onset", "tinnitus", "occupational", "recreational"],
            "contradictory": ["no_noise_exposure", "sudden_onset"]
        },
        "demographics": {
            "age_risk": {"<40": 0.6, "40-70": 0.5, ">70": 0.3},
            "sex_risk": {"male": 1.3, "female": 0.8}
        },
        "risk_factors": ["occupational_noise", "loud_music", "firearms", "construction", "military", "lack_of_protection"],
        "specificity": 0.80,
        "urgency": "non_urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["Audiometry", "History_of_exposure"],
            "within_6h": ["Tympanometry"],
            "optional": []
        },
        "management_hints": "Treatment: Hearing protection (earplugs, earmuffs). Hearing aids if needed. Noise avoidance. Prevention is key - protect hearing in noisy environments. Irreversible but preventable."
    },
    "Sudden Sensorineural Hearing Loss (SSNHL)": {
        "symptoms": {
            "required": ["hearing_loss"],
            "supporting": ["sudden_onset", "unilateral", "sensorineural", "within_72h", "tinnitus", "vertigo", "fullness"],
            "contradictory": ["gradual_onset", "bilateral", "conductive"]
        },
        "demographics": {
            "age_risk": {"<40": 0.4, "40-70": 0.5, ">70": 0.4},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["viral_infection", "autoimmune", "vascular", "trauma", "stress"],
        "specificity": 0.85,
        "urgency": "urgent",
        "rule_out_first": True,
        "workup": {
            "immediate": ["Audiometry", "MRI_with_contrast", "Physical_exam", "Neurologic_exam"],
            "within_6h": ["CBC", "ESR", "Autoimmune_panel", "Viral_serology"],
            "optional": ["VNG", "ABR"]
        },
        "management_hints": "URGENT! Time-sensitive treatment. High-dose steroids (prednisone 1mg/kg/day) within 2 weeks of onset. Consider intratympanic steroids. Rule out acoustic neuroma (MRI). Prognosis better with early treatment."
    },
    "Otitis Media (Acute/Chronic)": {
        "symptoms": {
            "required": ["hearing_loss"],
            "supporting": ["ear_pain", "ear_discharge", "fever", "conductive", "tympanic_membrane_abnormal", "fluid_in_middle_ear"],
            "contradictory": ["no_ear_pain", "sensorineural", "normal_tympanic_membrane"]
        },
        "demographics": {
            "age_risk": {"<40": 0.6, "40-70": 0.3, ">70": 0.2},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["URI", "allergies", "smoking_exposure", "daycare", "eustachian_tube_dysfunction", "cleft_palate"],
        "specificity": 0.75,
        "urgency": "non_urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["Otoscopy", "Tympanometry", "Physical_exam"],
            "within_6h": ["Audiometry"],
            "optional": ["CT_if_chronic_or_complications"]
        },
        "management_hints": "Treatment: Antibiotics if bacterial (amoxicillin-clavulanate). Decongestants, nasal steroids. Myringotomy if persistent. Tympanostomy tubes if recurrent. Usually resolves with treatment."
    },
    "Meniere Disease": {
        "symptoms": {
            "required": ["hearing_loss"],
            "supporting": ["vertigo", "tinnitus", "aural_fullness", "episodic", "unilateral", "fluctuating", "low_frequency"],
            "contradictory": ["no_vertigo", "bilateral", "continuous"]
        },
        "demographics": {
            "age_risk": {"<40": 0.3, "40-70": 0.6, ">70": 0.4},
            "sex_risk": {"male": 0.8, "female": 1.2}
        },
        "risk_factors": ["age", "family_history", "autoimmune", "allergy", "migraine"],
        "specificity": 0.75,
        "urgency": "non_urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["Audiometry", "Neurologic_exam"],
            "within_6h": ["VNG", "Electrocochleography"],
            "optional": ["MRI_to_rule_out_acoustic_neuroma"]
        },
        "management_hints": "Treatment: Low-salt diet, diuretics, vestibular suppressants for acute attacks. Consider intratympanic steroids or gentamicin if severe. Surgical options if refractory."
    },
    "Acoustic Neuroma (Vestibular Schwannoma)": {
        "symptoms": {
            "required": ["hearing_loss"],
            "supporting": ["unilateral", "gradual_onset", "sensorineural", "tinnitus", "vertigo", "facial_weakness", "imbalance"],
            "contradictory": ["bilateral", "sudden_onset", "conductive"]
        },
        "demographics": {
            "age_risk": {"<40": 0.2, "40-70": 0.6, ">70": 0.5},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["NF2", "radiation_exposure", "age"],
        "specificity": 0.80,
        "urgency": "urgent",
        "rule_out_first": True,
        "workup": {
            "immediate": ["MRI_with_contrast", "Audiometry", "ABR"],
            "within_6h": ["Neurologic_exam", "Facial_nerve_testing"],
            "optional": ["CT_if_MRI_contraindicated"]
        },
        "management_hints": "URGENT! Acoustic neuroma is a benign tumor but can cause serious complications. MRI required for diagnosis. Treatment: Observation (small), surgery, or radiation. Monitor for growth and symptoms."
    },
    "Ototoxic Medications": {
        "symptoms": {
            "required": ["hearing_loss"],
            "supporting": ["medication_use", "recent_medication_start", "dose_related", "bilateral", "tinnitus", "aminoglycosides", "cisplatin", "loop_diuretics"],
            "contradictory": ["no_medication_use"]
        },
        "demographics": {
            "age_risk": {"<40": 0.3, "40-70": 0.5, ">70": 0.6},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["aminoglycosides", "cisplatin", "loop_diuretics", "high_doses", "renal_failure", "dehydration"],
        "specificity": 0.75,
        "urgency": "non_urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["Medication_review", "Audiometry"],
            "within_6h": ["Renal_function"],
            "optional": []
        },
        "management_hints": "Review medications. Discontinue or reduce dose if possible. Monitor hearing during treatment. Consider alternative medications. Some ototoxicity may be reversible if caught early."
    }
}

__all__ = ['HEARING_LOSS_DDX']

