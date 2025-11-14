"""DDx Knowledge Base - Data
Differential diagnosis data for common clinical scenarios

NOTE: This file contains only data dictionaries.
Functions are in ddx_data.py"""

# Seizure Differential Diagnosis

SEIZURE_DDX = {
    "Status Epilepticus": {
        "symptoms": {
            "required": ["seizure", "prolonged_seizure"],
            "supporting": ["seizure_duration_>5min", "multiple_seizures", "no_recovery_between", "altered_mental_status", "respiratory_distress"],
            "contradictory": ["brief_seizure", "full_recovery"]
        },
        "demographics": {
            "age_risk": {"<40": 0.5, "40-70": 0.6, ">70": 0.7},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["epilepsy", "medication_noncompliance", "brain_injury", "stroke", "infection", "metabolic_disorder"],
        "specificity": 0.85,
        "urgency": "emergency",
        "rule_out_first": True,
        "workup": {
            "immediate": ["Benzodiazepine_IV", "Lorazepam_IV", "ECG", "Glucose", "Electrolytes", "ABG"],
            "within_6h": ["EEG", "CT_head", "LP_if_suspected_infection", "Antiepileptic_levels"],
            "optional": ["MRI_brain", "Toxicology_screen"]
        },
        "management_hints": "URGENT! Status epilepticus is a medical emergency. First-line: Benzodiazepines (lorazepam IV). Second-line: Fosphenytoin, phenobarbital, or valproate. If refractory → ICU, intubation, continuous EEG monitoring. Treat underlying cause."
    },
    "Generalized Tonic-Clonic Seizure": {
        "symptoms": {
            "required": ["seizure", "loss_of_consciousness"],
            "supporting": ["tonic_phase", "clonic_phase", "postictal_state", "tongue_biting", "incontinence", "generalized_onset"],
            "contradictory": ["focal_onset", "no_loss_consciousness"]
        },
        "demographics": {
            "age_risk": {"<40": 0.6, "40-70": 0.5, ">70": 0.4},
            "sex_risk": {"male": 1.1, "female": 1.0}
        },
        "risk_factors": ["epilepsy", "brain_injury", "stroke", "brain_tumor", "genetic_factors", "febrile_seizure_history"],
        "specificity": 0.80,
        "urgency": "urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["ECG", "Glucose", "Electrolytes", "CT_head_if_first_seizure"],
            "within_6h": ["EEG", "MRI_brain_if_first_seizure", "LP_if_suspected_infection"],
            "optional": ["Antiepileptic_levels", "Genetic_testing"]
        },
        "management_hints": "First seizure → Workup for cause. Recurrent → Antiepileptic drugs (AEDs). Start with monotherapy (levetiracetam, lamotrigine, valproate). Monitor drug levels. Consider driving restrictions."
    },
    "Focal Seizure": {
        "symptoms": {
            "required": ["focal_onset", "seizure"],
            "supporting": ["aura", "focal_motor", "focal_sensory", "automatisms", "dyscognitive", "secondary_generalization"],
            "contradictory": ["generalized_onset", "no_focal_features"]
        },
        "demographics": {
            "age_risk": {"<40": 0.5, "40-70": 0.6, ">70": 0.7},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["brain_injury", "stroke", "brain_tumor", "mesial_temporal_sclerosis", "cortical_dysplasia"],
        "specificity": 0.75,
        "urgency": "urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["ECG", "Glucose", "Electrolytes", "CT_head"],
            "within_6h": ["EEG", "MRI_brain_with_epilepsy_protocol"],
            "optional": ["Video_EEG", "PET_scan", "SPECT"]
        },
        "management_hints": "Focal seizures suggest structural brain lesion. MRI with epilepsy protocol essential. Antiepileptic drugs: carbamazepine, oxcarbazepine, or levetiracetam. Consider surgical evaluation if drug-resistant."
    },
    "Syncope (vs Seizure)": {
        "symptoms": {
            "required": ["loss_of_consciousness"],
            "supporting": ["preceding_dizziness", "preceding_nausea", "pale", "sweating", "brief_duration", "rapid_recovery", "situational"],
            "contradictory": ["postictal_state", "tongue_biting", "incontinence", "prolonged_duration"]
        },
        "demographics": {
            "age_risk": {"<40": 0.4, "40-70": 0.5, ">70": 0.6},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["orthostatic_hypotension", "cardiac_arrhythmia", "vasovagal", "medication", "dehydration"],
        "specificity": 0.70,
        "urgency": "urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["ECG", "Orthostatic_vitals", "Glucose", "Electrolytes"],
            "within_6h": ["Echo_if_cardiac_suspected", "Holter_monitor", "Tilt_table_test"],
            "optional": ["EEG_if_uncertain", "Cardiac_catheterization"]
        },
        "management_hints": "Differentiate from seizure: syncope has rapid recovery, no postictal state. Treat underlying cause (arrhythmia, orthostatic hypotension, vasovagal). Consider pacemaker if cardiac syncope."
    },
    "Psychogenic Non-Epileptic Seizure (PNES)": {
        "symptoms": {
            "required": ["seizure_like_episode"],
            "supporting": ["waxing_waning", "asynchronous_movements", "eye_closure", "resistance_to_eye_opening", "prolonged_duration", "no_postictal", "psychiatric_history"],
            "contradictory": ["stereotyped", "tongue_biting", "incontinence", "postictal_state"]
        },
        "demographics": {
            "age_risk": {"<40": 0.6, "40-70": 0.4, ">70": 0.2},
            "sex_risk": {"male": 0.5, "female": 1.5}
        },
        "risk_factors": ["psychiatric_disorder", "trauma_history", "anxiety", "depression", "conversion_disorder"],
        "specificity": 0.65,
        "urgency": "non_urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["EEG_during_episode", "Video_EEG"],
            "within_6h": ["Psychiatric_evaluation"],
            "optional": ["Psychological_testing"]
        },
        "management_hints": "Diagnosis: Video-EEG showing no epileptiform activity during episode. Treatment: Psychotherapy, cognitive behavioral therapy (CBT), psychiatric medications. Avoid antiepileptic drugs. Patient education important."
    },
    "Hypoglycemia-Induced Seizure": {
        "symptoms": {
            "required": ["seizure", "hypoglycemia"],
            "supporting": ["diabetes", "insulin_use", "sulfonylurea_use", "sweating", "tremor", "confusion", "rapid_recovery_after_glucose"],
            "contradictory": ["normal_glucose", "no_diabetes"]
        },
        "demographics": {
            "age_risk": {"<40": 0.3, "40-70": 0.5, ">70": 0.6},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["diabetes", "insulin_use", "sulfonylurea_use", "renal_impairment", "alcohol", "fasting"],
        "specificity": 0.85,
        "urgency": "emergency",
        "rule_out_first": True,
        "workup": {
            "immediate": ["Glucose", "IV_dextrose", "Oral_glucose_if_conscious"],
            "within_6h": ["HbA1c", "C_peptide", "Insulin_levels", "Sulfonylurea_levels"],
            "optional": ["CT_pancreas", "Insulinoma_workup"]
        },
        "management_hints": "URGENT! Check glucose immediately. If hypoglycemic → Give glucose (IV dextrose 50% or oral). Treat underlying cause. Adjust diabetes medications. Educate patient on hypoglycemia recognition and treatment."
    }
}

__all__ = ['SEIZURE_DDX']

