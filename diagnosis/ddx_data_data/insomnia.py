"""DDx Knowledge Base - Data
Differential diagnosis data for common clinical scenarios

NOTE: This file contains only data dictionaries.
Functions are in ddx_data.py"""

# Insomnia Differential Diagnosis

INSOMNIA_DDX = {
    "Primary Insomnia": {
        "symptoms": {
            "required": ["insomnia", "difficulty_sleeping"],
            "supporting": ["difficulty_falling_asleep", "difficulty_staying_asleep", "early_morning_awakening", "non_restorative_sleep", "daytime_fatigue", "chronic"],
            "contradictory": ["medical_condition", "medication_use", "substance_use", "psychiatric_disorder"]
        },
        "demographics": {
            "age_risk": {"<40": 0.4, "40-70": 0.6, ">70": 0.5},
            "sex_risk": {"male": 0.8, "female": 1.2}
        },
        "risk_factors": ["stress", "poor_sleep_hygiene", "irregular_schedule", "shift_work", "anxiety", "perfectionism"],
        "specificity": 0.70,
        "urgency": "non_urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["Sleep_history", "Sleep_diary", "Clinical_assessment"],
            "within_6h": ["Polysomnography_if_indicated"],
            "optional": ["Actigraphy", "Sleep_study"]
        },
        "management_hints": "First-line: Cognitive behavioral therapy for insomnia (CBT-I), sleep hygiene education. Medications: Short-term use of zolpidem, eszopiclone, or ramelteon. Avoid long-term benzodiazepines. Address underlying stress/anxiety."
    },
    "Depression": {
        "symptoms": {
            "required": ["insomnia"],
            "supporting": ["depressed_mood", "anhedonia", "early_morning_awakening", "fatigue", "poor_concentration", "appetite_changes", "suicidal_thoughts"],
            "contradictory": ["no_depressive_symptoms", "euthymic_mood"]
        },
        "demographics": {
            "age_risk": {"<40": 0.5, "40-70": 0.6, ">70": 0.7},
            "sex_risk": {"male": 0.7, "female": 1.3}
        },
        "risk_factors": ["family_history", "stress", "trauma", "medical_illness", "substance_use", "previous_episodes"],
        "specificity": 0.75,
        "urgency": "urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["PHQ-9", "Clinical_assessment", "Suicide_risk_assessment"],
            "within_6h": ["CBC", "TSH", "B12", "Folate"],
            "optional": ["Psychiatric_referral"]
        },
        "management_hints": "URGENT if suicidal! Treatment: Antidepressants (SSRIs, SNRIs), psychotherapy (CBT), sleep medications if needed. Monitor for suicide risk. Consider psychiatric referral. Address underlying depression."
    },
    "Anxiety Disorders": {
        "symptoms": {
            "required": ["insomnia"],
            "supporting": ["anxiety", "worry", "difficulty_falling_asleep", "racing_thoughts", "restlessness", "muscle_tension", "panic_attacks"],
            "contradictory": ["no_anxiety", "calm_mood"]
        },
        "demographics": {
            "age_risk": {"<40": 0.6, "40-70": 0.5, ">70": 0.4},
            "sex_risk": {"male": 0.7, "female": 1.3}
        },
        "risk_factors": ["stress", "trauma", "family_history", "medical_illness", "substance_use"],
        "specificity": 0.70,
        "urgency": "non_urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["GAD-7", "Clinical_assessment"],
            "within_6h": ["CBC", "TSH", "CMP"],
            "optional": ["Psychiatric_referral"]
        },
        "management_hints": "Treatment: SSRIs, SNRIs, buspirone, benzodiazepines (short-term). Psychotherapy (CBT). Sleep medications if needed. Address underlying anxiety. Relaxation techniques."
    },
    "Restless Legs Syndrome (RLS)": {
        "symptoms": {
            "required": ["insomnia"],
            "supporting": ["urge_to_move_legs", "uncomfortable_sensations", "worse_at_night", "worse_at_rest", "relieved_by_movement", "periodic_limb_movements"],
            "contradictory": ["no_leg_symptoms", "no_urge_to_move"]
        },
        "demographics": {
            "age_risk": {"<40": 0.3, "40-70": 0.6, ">70": 0.7},
            "sex_risk": {"male": 0.8, "female": 1.2}
        },
        "risk_factors": ["iron_deficiency", "pregnancy", "renal_failure", "diabetes", "family_history", "medications"],
        "specificity": 0.80,
        "urgency": "non_urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["Ferritin", "Iron_studies", "Clinical_assessment"],
            "within_6h": ["CBC", "CMP", "Creatinine"],
            "optional": ["Polysomnography"]
        },
        "management_hints": "Treatment: Dopamine agonists (pramipexole, ropinirole), gabapentin, iron supplementation if deficient. Avoid triggers (caffeine, alcohol). Regular exercise. Address underlying cause (iron deficiency, renal failure)."
    },
    "Obstructive Sleep Apnea (OSA)": {
        "symptoms": {
            "required": ["insomnia"],
            "supporting": ["snoring", "witnessed_apneas", "daytime_sleepiness", "fatigue", "morning_headache", "non_restorative_sleep", "gasping"],
            "contradictory": ["no_snoring", "no_apneas", "restful_sleep"]
        },
        "demographics": {
            "age_risk": {"<40": 0.3, "40-70": 0.6, ">70": 0.7},
            "sex_risk": {"male": 1.5, "female": 1.0}
        },
        "risk_factors": ["obesity", "male", "age", "large_neck", "smoking", "alcohol", "sedatives", "nasal_congestion"],
        "specificity": 0.75,
        "urgency": "non_urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["Epworth_Sleepiness_Scale", "Clinical_assessment"],
            "within_6h": ["Polysomnography", "Home_sleep_test"],
            "optional": ["Sleep_study"]
        },
        "management_hints": "Treatment: CPAP/BiPAP (first-line), weight loss, positional therapy, oral appliances. Avoid alcohol/sedatives. Treat nasal congestion. Severe → consider surgery. Monitor for cardiovascular complications."
    },
    "Medication-Induced Insomnia": {
        "symptoms": {
            "required": ["insomnia"],
            "supporting": ["recent_medication_start", "stimulant_medications", "caffeine", "alcohol_withdrawal", "medication_timing"],
            "contradictory": ["no_medications", "chronic_medications_only"]
        },
        "demographics": {
            "age_risk": {"<40": 0.4, "40-70": 0.5, ">70": 0.6},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["stimulants", "caffeine", "alcohol", "decongestants", "beta_agonists", "corticosteroids", "antidepressants"],
        "specificity": 0.70,
        "urgency": "non_urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["Medication_review", "Timing_analysis"],
            "within_6h": [],
            "optional": []
        },
        "management_hints": "Review medications. Common culprits: stimulants, caffeine, alcohol, decongestants, beta-agonists, corticosteroids. Consider: dose reduction, timing change, or alternative medication. Avoid caffeine/alcohol before bed."
    },
    "Circadian Rhythm Disorders": {
        "symptoms": {
            "required": ["insomnia"],
            "supporting": ["delayed_sleep_phase", "advanced_sleep_phase", "shift_work", "jet_lag", "irregular_schedule", "social_jet_lag"],
            "contradictory": ["regular_schedule", "normal_sleep_timing"]
        },
        "demographics": {
            "age_risk": {"<40": 0.6, "40-70": 0.4, ">70": 0.5},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["shift_work", "travel", "irregular_schedule", "teenagers", "elderly", "blindness"],
        "specificity": 0.75,
        "urgency": "non_urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["Sleep_diary", "Actigraphy", "Clinical_assessment"],
            "within_6h": [],
            "optional": ["Melatonin_levels"]
        },
        "management_hints": "Treatment: Light therapy, melatonin, chronotherapy. Maintain regular sleep schedule. Avoid bright light before bed. Shift work: optimize schedule, consider modafinil. Address underlying schedule issues."
    }
}

__all__ = ['INSOMNIA_DDX']

