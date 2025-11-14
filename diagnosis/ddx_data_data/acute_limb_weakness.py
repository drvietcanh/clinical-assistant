"""DDx Knowledge Base - Data
Differential diagnosis data for common clinical scenarios

NOTE: This file contains only data dictionaries.
Functions are in ddx_data.py"""

# Acute Limb Weakness Differential Diagnosis

ACUTE_LIMB_WEAKNESS_DDX = {
    "Acute Ischemic Stroke": {
        "symptoms": {
            "required": ["acute_limb_weakness", "sudden_onset"],
            "supporting": ["unilateral", "facial_droop", "speech_difficulty", "vision_loss", "ataxia", "sensory_loss", "time_sensitive"],
            "contradictory": ["bilateral", "gradual_onset", "no_focal_deficit"]
        },
        "demographics": {
            "age_risk": {"<40": 0.2, "40-70": 0.6, ">70": 0.8},
            "sex_risk": {"male": 1.2, "female": 1.0}
        },
        "risk_factors": ["hypertension", "diabetes", "atrial_fibrillation", "smoking", "hyperlipidemia", "prior_stroke"],
        "specificity": 0.90,
        "urgency": "emergency",
        "rule_out_first": True,
        "workup": {
            "immediate": ["CT_head", "CT_angiography", "ECG", "CBC", "Coagulation", "Glucose"],
            "within_6h": ["MRI_brain", "Echo", "Carotid_ultrasound", "tPA_if_eligible"],
            "optional": ["MRA", "Cardiac_monitoring"]
        },
        "management_hints": "URGENT! Time is brain! If <4.5h and eligible → tPA. If <24h and large vessel occlusion → Mechanical thrombectomy. Aspirin, statin, blood pressure control. Secondary prevention."
    },
    "Transient Ischemic Attack (TIA)": {
        "symptoms": {
            "required": ["acute_limb_weakness", "transient"],
            "supporting": ["unilateral", "resolves_<24h", "facial_droop", "speech_difficulty", "vision_loss", "ataxia", "no_residual_deficit"],
            "contradictory": ["persistent_deficit", "bilateral"]
        },
        "demographics": {
            "age_risk": {"<40": 0.1, "40-70": 0.6, ">70": 0.8},
            "sex_risk": {"male": 1.2, "female": 1.0}
        },
        "risk_factors": ["hypertension", "diabetes", "atrial_fibrillation", "carotid_stenosis", "smoking", "hyperlipidemia"],
        "specificity": 0.85,
        "urgency": "emergency",
        "rule_out_first": True,
        "workup": {
            "immediate": ["CT_head", "ECG", "CBC", "Coagulation", "ABCD2_score"],
            "within_6h": ["MRI_brain", "Echo", "Carotid_ultrasound", "Holter_monitor"],
            "optional": ["MRA", "Cardiac_catheterization"]
        },
        "management_hints": "URGENT! TIA is a warning sign of impending stroke. Start aspirin immediately. Workup for cause (cardiac, carotid, etc.). Secondary prevention: Antiplatelet, statin, blood pressure control, lifestyle modifications."
    },
    "Intracerebral Hemorrhage": {
        "symptoms": {
            "required": ["acute_limb_weakness", "sudden_onset"],
            "supporting": ["headache", "nausea", "vomiting", "altered_mental_status", "hypertension", "unilateral", "focal_deficit"],
            "contradictory": ["no_headache", "bilateral"]
        },
        "demographics": {
            "age_risk": {"<40": 0.3, "40-70": 0.6, ">70": 0.8},
            "sex_risk": {"male": 1.2, "female": 1.0}
        },
        "risk_factors": ["hypertension", "anticoagulation", "amyloid_angiopathy", "AVM", "aneurysm", "trauma"],
        "specificity": 0.85,
        "urgency": "emergency",
        "rule_out_first": True,
        "workup": {
            "immediate": ["CT_head", "CBC", "Coagulation", "Blood_pressure_control"],
            "within_6h": ["CT_angiography", "MRI_brain", "Neurosurgery_consult"],
            "optional": ["Angiography", "Surgical_intervention"]
        },
        "management_hints": "URGENT! Intracerebral hemorrhage is life-threatening. Control blood pressure (target SBP <140). Reverse anticoagulation if present. Neurosurgery consult. Monitor for expansion. Supportive care."
    },
    "Spinal Cord Compression": {
        "symptoms": {
            "required": ["acute_limb_weakness"],
            "supporting": ["bilateral", "sensory_level", "back_pain", "bowel_bladder_dysfunction", "rapid_progression", "spinal_tenderness"],
            "contradictory": ["unilateral_only", "no_sensory_level"]
        },
        "demographics": {
            "age_risk": {"<40": 0.3, "40-70": 0.6, ">70": 0.7},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["metastatic_cancer", "trauma", "disc_herniation", "spinal_stenosis", "infection", "hematoma"],
        "specificity": 0.80,
        "urgency": "emergency",
        "rule_out_first": True,
        "workup": {
            "immediate": ["MRI_spine", "CT_spine", "Neurology_consult"],
            "within_6h": ["Neurosurgery_consult", "Steroids_if_indicated"],
            "optional": ["Surgical_decompression"]
        },
        "management_hints": "URGENT! Spinal cord compression is a neurosurgical emergency. High-dose steroids (dexamethasone). Urgent MRI. Neurosurgery consult for decompression. Time to treatment critical for outcome."
    },
    "Guillain-Barré Syndrome": {
        "symptoms": {
            "required": ["acute_limb_weakness"],
            "supporting": ["bilateral", "ascending", "recent_infection", "areflexia", "sensory_symptoms", "facial_weakness", "respiratory_weakness"],
            "contradictory": ["unilateral", "descending", "hyperreflexia"]
        },
        "demographics": {
            "age_risk": {"<40": 0.4, "40-70": 0.5, ">70": 0.4},
            "sex_risk": {"male": 1.2, "female": 1.0}
        },
        "risk_factors": ["recent_infection", "Campylobacter", "EBV", "CMV", "surgery", "vaccination"],
        "specificity": 0.75,
        "urgency": "emergency",
        "rule_out_first": True,
        "workup": {
            "immediate": ["LP", "CSF_protein", "Nerve_conduction_study", "EMG", "Respiratory_function"],
            "within_6h": ["IVIG_or_plasma_exchange", "ICU_monitoring"],
            "optional": ["Antibody_testing"]
        },
        "management_hints": "URGENT! Guillain-Barré can progress rapidly to respiratory failure. Monitor respiratory function closely. Treatment: IVIG or plasma exchange. ICU monitoring. Supportive care. Most patients recover but may take months."
    },
    "Myasthenia Gravis": {
        "symptoms": {
            "required": ["limb_weakness"],
            "supporting": ["fatigability", "ptosis", "diplopia", "bulbar_symptoms", "fluctuating", "worse_with_activity", "improves_with_rest"],
            "contradictory": ["fixed_weakness", "no_fluctuation"]
        },
        "demographics": {
            "age_risk": {"<40": 0.5, "40-70": 0.6, ">70": 0.3},
            "sex_risk": {"male": 0.5, "female": 1.5}
        },
        "risk_factors": ["thymoma", "autoimmune_disease", "family_history"],
        "specificity": 0.80,
        "urgency": "urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["AChR_antibodies", "MuSK_antibodies", "Tensilon_test", "EMG"],
            "within_6h": ["CT_chest", "Pulmonary_function"],
            "optional": ["Thymectomy_evaluation"]
        },
        "management_hints": "Treatment: Acetylcholinesterase inhibitors (pyridostigmine), immunosuppression (steroids, azathioprine), IVIG or plasma exchange for crisis. Thymectomy if thymoma. Monitor for myasthenic crisis (respiratory failure)."
    }
}

__all__ = ['ACUTE_LIMB_WEAKNESS_DDX']

