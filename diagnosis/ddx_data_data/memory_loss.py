"""DDx Knowledge Base - Data
Differential diagnosis data for common clinical scenarios

NOTE: This file contains only data dictionaries.
Functions are in ddx_data.py"""

# Memory Loss Differential Diagnosis

MEMORY_LOSS_DDX = {
    "Alzheimer Disease": {
        "symptoms": {
            "required": ["memory_loss"],
            "supporting": ["gradual_onset", "progressive", "short_term_memory", "disorientation", "language_problems", "apraxia", "agnosia", "age_>65", "family_history"],
            "contradictory": ["acute_onset", "focal_neurologic_deficits", "young_age"]
        },
        "demographics": {
            "age_risk": {"<40": 0.0, "40-70": 0.2, ">70": 0.8},
            "sex_risk": {"male": 0.8, "female": 1.2}
        },
        "risk_factors": ["age", "family_history", "APOE4", "diabetes", "hypertension", "head_trauma", "low_education"],
        "specificity": 0.80,
        "urgency": "non_urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["MMSE", "MoCA", "Neurologic_exam", "CBC", "CMP", "TSH", "B12"],
            "within_6h": ["MRI_brain", "CT_if_MRI_not_available"],
            "optional": ["APOE_genotyping", "CSF_biomarkers", "PET_scan"]
        },
        "management_hints": "Treatment: Cholinesterase inhibitors (donepezil, rivastigmine), memantine. Supportive care, safety measures. Caregiver support. Usually progressive. Early diagnosis allows planning."
    },
    "Vascular Dementia": {
        "symptoms": {
            "required": ["memory_loss"],
            "supporting": ["stepwise_decline", "focal_neurologic_deficits", "vascular_risk_factors", "stroke_history", "hypertension", "diabetes", "patchy_cognitive_deficits"],
            "contradictory": ["gradual_onset", "no_vascular_risk_factors"]
        },
        "demographics": {
            "age_risk": {"<40": 0.1, "40-70": 0.4, ">70": 0.7},
            "sex_risk": {"male": 1.2, "female": 1.0}
        },
        "risk_factors": ["hypertension", "diabetes", "stroke", "CAD", "atrial_fibrillation", "smoking", "hyperlipidemia"],
        "specificity": 0.75,
        "urgency": "non_urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["MMSE", "MoCA", "Neurologic_exam", "MRI_brain"],
            "within_6h": ["CT_if_MRI_not_available", "CBC", "CMP", "Lipid_panel"],
            "optional": ["Carotid_ultrasound", "Echo"]
        },
        "management_hints": "Treatment: Vascular risk factor control (BP, diabetes, lipids). Antiplatelet therapy. Cholinesterase inhibitors may help. Prevention is key - control vascular risk factors."
    },
    "Delirium": {
        "symptoms": {
            "required": ["memory_loss", "confusion"],
            "supporting": ["acute_onset", "fluctuating", "inattention", "disorganized_thinking", "altered_consciousness", "medication", "infection", "metabolic"],
            "contradictory": ["chronic", "stable", "no_fluctuation"]
        },
        "demographics": {
            "age_risk": {"<40": 0.2, "40-70": 0.4, ">70": 0.8},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["elderly", "hospitalization", "medication", "infection", "metabolic_disorder", "surgery", "alcohol_withdrawal"],
        "specificity": 0.80,
        "urgency": "urgent",
        "rule_out_first": True,
        "workup": {
            "immediate": ["CAM_ICU", "CBC", "CMP", "Glucose", "ABG", "Chest_Xray", "Urinalysis"],
            "within_6h": ["CT_head", "LP_if_suspected_infection", "Medication_review"],
            "optional": ["EEG", "Toxicology_screen"]
        },
        "management_hints": "URGENT! Delirium is a medical emergency. Treat underlying cause (infection, medication, metabolic). Supportive care, reorientation, family presence. Avoid restraints. Usually reversible if cause treated."
    },
    "Depression (Pseudodementia)": {
        "symptoms": {
            "required": ["memory_loss"],
            "supporting": ["depression", "apathy", "poor_concentration", "psychomotor_retardation", "insomnia", "appetite_changes", "suicidal_ideation", "recent_stress"],
            "contradictory": ["no_depression", "no_psychiatric_symptoms"]
        },
        "demographics": {
            "age_risk": {"<40": 0.4, "40-70": 0.5, ">70": 0.6},
            "sex_risk": {"male": 0.7, "female": 1.3}
        },
        "risk_factors": ["depression", "stress", "trauma", "medical_illness", "medication", "substance_use"],
        "specificity": 0.70,
        "urgency": "non_urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["PHQ9", "Psychiatric_evaluation", "MMSE"],
            "within_6h": ["CBC", "CMP", "TSH", "B12"],
            "optional": ["MRI_if_atypical"]
        },
        "management_hints": "Treatment: Antidepressants (SSRIs), psychotherapy. Memory improves with depression treatment. Differentiate from true dementia - depression is treatable and reversible."
    },
    "Normal Pressure Hydrocephalus (NPH)": {
        "symptoms": {
            "required": ["memory_loss"],
            "supporting": ["gait_apraxia", "urinary_incontinence", "triad", "enlarged_ventricles", "normal_CSF_pressure", "age_>60"],
            "contradictory": ["no_gait_problems", "normal_ventricles"]
        },
        "demographics": {
            "age_risk": {"<40": 0.0, "40-70": 0.3, ">70": 0.6},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["age", "prior_SAH", "meningitis", "head_trauma"],
        "specificity": 0.75,
        "urgency": "urgent",
        "rule_out_first": True,
        "workup": {
            "immediate": ["MRI_brain", "CT_if_MRI_not_available", "Neurologic_exam"],
            "within_6h": ["LP_with_large_volume_tap", "Gait_assessment"],
            "optional": ["CSF_dynamics_study"]
        },
        "management_hints": "URGENT! NPH is potentially reversible. Treatment: Ventriculoperitoneal shunt. Large volume LP as diagnostic and therapeutic trial. Early treatment improves outcomes. Gait improvement is best predictor."
    },
    "Vitamin B12 Deficiency": {
        "symptoms": {
            "required": ["memory_loss"],
            "supporting": ["peripheral_neuropathy", "megaloblastic_anemia", "glossitis", "low_B12", "elevated_MMA", "elevated_homocysteine", "vegetarian_diet"],
            "contradictory": ["normal_B12", "no_anemia"]
        },
        "demographics": {
            "age_risk": {"<40": 0.2, "40-70": 0.4, ">70": 0.6},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["vegetarian_diet", "gastric_surgery", "pernicious_anemia", "Crohn_disease", "elderly", "PPI_use"],
        "specificity": 0.80,
        "urgency": "non_urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["B12", "MMA", "Homocysteine", "CBC", "Folate"],
            "within_6h": ["Intrinsic_factor_antibodies", "Parietal_cell_antibodies"],
            "optional": ["Schilling_test"]
        },
        "management_hints": "Treatment: B12 replacement (IM or high-dose oral). Memory may improve with treatment, especially if caught early. Monitor B12 levels. Usually reversible if treated promptly."
    },
    "Medication-Induced": {
        "symptoms": {
            "required": ["memory_loss"],
            "supporting": ["medication_use", "recent_medication_start", "anticholinergics", "benzodiazepines", "antipsychotics", "antihistamines", "dose_related"],
            "contradictory": ["no_medication_use"]
        },
        "demographics": {
            "age_risk": {"<40": 0.3, "40-70": 0.5, ">70": 0.7},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["anticholinergics", "benzodiazepines", "antipsychotics", "antihistamines", "multiple_medications", "elderly"],
        "specificity": 0.75,
        "urgency": "non_urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["Medication_review", "History"],
            "within_6h": [],
            "optional": []
        },
        "management_hints": "Review medications. Reduce dose or discontinue if possible. Switch to alternative medication. Most cases improve with medication adjustment. Avoid anticholinergics in elderly."
    },
    "Frontotemporal Dementia": {
        "symptoms": {
            "required": ["memory_loss"],
            "supporting": ["behavioral_changes", "personality_changes", "language_problems", "executive_dysfunction", "younger_age", "family_history", "preserved_visuospatial"],
            "contradictory": ["old_age", "no_behavioral_changes", "prominent_memory_loss"]
        },
        "demographics": {
            "age_risk": {"<40": 0.2, "40-70": 0.6, ">70": 0.3},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["family_history", "genetics", "younger_age"],
        "specificity": 0.75,
        "urgency": "non_urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["MMSE", "MoCA", "Neurologic_exam", "MRI_brain"],
            "within_6h": ["Neuropsychological_testing"],
            "optional": ["PET_scan", "Genetic_testing"]
        },
        "management_hints": "Treatment: Supportive care, behavioral management. SSRIs for behavioral symptoms. Usually progressive. Different from Alzheimer - more behavioral and language problems, less memory initially."
    }
}

__all__ = ['MEMORY_LOSS_DDX']

