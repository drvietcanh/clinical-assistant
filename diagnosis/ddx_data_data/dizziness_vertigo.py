"""DDx Knowledge Base - Data
Differential diagnosis data for common clinical scenarios

NOTE: This file contains only data dictionaries.
Functions are in ddx_data.py"""

# Dizziness / Vertigo Differential Diagnosis

DIZZINESS_VERTIGO_DDX = {
    "Benign Paroxysmal Positional Vertigo (BPPV)": {
        "symptoms": {
            "required": ["vertigo"],
            "supporting": ["positional", "brief_duration", "head_movement_triggered", "nystagmus", "no_hearing_loss", "no_neurologic_symptoms"],
            "contradictory": ["continuous", "hearing_loss", "neurologic_symptoms"]
        },
        "demographics": {
            "age_risk": {"<40": 0.3, "40-70": 0.6, ">70": 0.7},
            "sex_risk": {"male": 0.7, "female": 1.3}
        },
        "risk_factors": ["age", "head_trauma", "vestibular_neuronitis", "migraine"],
        "specificity": 0.85,
        "urgency": "non_urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["Dix_Hallpike_test", "Head_impulse_test"],
            "within_6h": ["Audiometry_if_needed"],
            "optional": ["VNG", "MRI_if_atypical"]
        },
        "management_hints": "Treatment: Epley maneuver (canalith repositioning). Most cases resolve with repositioning maneuvers. Recurrence common. Avoid triggers. Medications (meclizine) for symptoms only."
    },
    "Vestibular Neuritis": {
        "symptoms": {
            "required": ["vertigo"],
            "supporting": ["acute_onset", "continuous", "nausea", "vomiting", "nystagmus", "no_hearing_loss", "recent_viral_illness"],
            "contradictory": ["hearing_loss", "neurologic_symptoms", "positional_only"]
        },
        "demographics": {
            "age_risk": {"<40": 0.5, "40-70": 0.4, ">70": 0.3},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["viral_infection", "herpes_simplex", "recent_URI"],
        "specificity": 0.80,
        "urgency": "non_urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["Head_impulse_test", "Neurologic_exam"],
            "within_6h": ["Audiometry", "VNG"],
            "optional": ["MRI_if_atypical"]
        },
        "management_hints": "Treatment: Supportive care, antiemetics, vestibular suppressants (meclizine, benzodiazepines). Usually self-limited (days to weeks). Vestibular rehabilitation if persistent."
    },
    "Meniere Disease": {
        "symptoms": {
            "required": ["vertigo"],
            "supporting": ["hearing_loss", "tinnitus", "aural_fullness", "episodic", "unilateral", "fluctuating_hearing"],
            "contradictory": ["no_hearing_loss", "bilateral", "continuous"]
        },
        "demographics": {
            "age_risk": {"<40": 0.3, "40-70": 0.6, ">70": 0.4},
            "sex_risk": {"male": 0.8, "female": 1.2}
        },
        "risk_factors": ["age", "family_history", "autoimmune", "allergy"],
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
    "Stroke (Posterior Circulation)": {
        "symptoms": {
            "required": ["vertigo", "dizziness"],
            "supporting": ["acute_onset", "neurologic_symptoms", "ataxia", "dysarthria", "diplopia", "facial_weakness", "crossed_signs"],
            "contradictory": ["isolated_vertigo", "no_neurologic_symptoms"]
        },
        "demographics": {
            "age_risk": {"<40": 0.1, "40-70": 0.5, ">70": 0.8},
            "sex_risk": {"male": 1.2, "female": 1.0}
        },
        "risk_factors": ["hypertension", "diabetes", "atrial_fibrillation", "smoking", "hyperlipidemia", "prior_stroke"],
        "specificity": 0.85,
        "urgency": "emergency",
        "rule_out_first": True,
        "workup": {
            "immediate": ["CT_head", "MRI_brain", "Neurologic_exam", "ECG"],
            "within_6h": ["CT_angiography", "Echo", "tPA_if_eligible"],
            "optional": ["MRA"]
        },
        "management_hints": "URGENT! Posterior circulation stroke can present with isolated vertigo. High suspicion if risk factors present. Time-sensitive treatment (tPA, thrombectomy). Neurologic exam critical."
    },
    "Medication-Induced": {
        "symptoms": {
            "required": ["dizziness", "vertigo"],
            "supporting": ["medication_use", "recent_medication_start", "dose_related", "orthostatic", "antihypertensive", "antidepressant"],
            "contradictory": ["no_medication_use"]
        },
        "demographics": {
            "age_risk": {"<40": 0.3, "40-70": 0.5, ">70": 0.7},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["multiple_medications", "elderly", "antihypertensives", "antidepressants", "anticonvulsants"],
        "specificity": 0.70,
        "urgency": "non_urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["Medication_review", "Orthostatic_vitals"],
            "within_6h": [],
            "optional": []
        },
        "management_hints": "Review medications. Adjust dose or discontinue if possible. Orthostatic hypotension → Adjust antihypertensives, increase fluids. Most cases resolve with medication adjustment."
    },
    "Orthostatic Hypotension": {
        "symptoms": {
            "required": ["dizziness"],
            "supporting": ["orthostatic", "standing_triggered", "lightheadedness", "syncope", "BP_drop", "elderly", "dehydration"],
            "contradictory": ["no_orthostatic", "normal_BP"]
        },
        "demographics": {
            "age_risk": {"<40": 0.2, "40-70": 0.4, ">70": 0.7},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["elderly", "dehydration", "medication", "autonomic_dysfunction", "diabetes", "Parkinson"],
        "specificity": 0.80,
        "urgency": "non_urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["Orthostatic_vitals", "CBC", "Electrolytes"],
            "within_6h": ["Tilt_table_test_if_needed"],
            "optional": ["Autonomic_testing"]
        },
        "management_hints": "Treatment: Increase fluids, salt, compression stockings. Adjust medications. Slow position changes. Consider fludrocortisone or midodrine if severe. Address underlying cause."
    }
}

__all__ = ['DIZZINESS_VERTIGO_DDX']

