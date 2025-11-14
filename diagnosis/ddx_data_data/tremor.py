"""DDx Knowledge Base - Data
Differential diagnosis data for common clinical scenarios

NOTE: This file contains only data dictionaries.
Functions are in ddx_data.py"""

# Tremor Differential Diagnosis

TREMOR_DDX = {
    "Essential Tremor": {
        "symptoms": {
            "required": ["tremor"],
            "supporting": ["bilateral", "action_tremor", "postural_tremor", "hands", "head", "voice", "improves_with_alcohol", "family_history", "gradual_onset"],
            "contradictory": ["rest_tremor", "unilateral", "rigidity", "bradykinesia"]
        },
        "demographics": {
            "age_risk": {"<40": 0.3, "40-70": 0.6, ">70": 0.7},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["family_history", "age", "genetics"],
        "specificity": 0.80,
        "urgency": "non_urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["Neurologic_exam", "History"],
            "within_6h": ["Thyroid_function"],
            "optional": ["EMG", "MRI_if_atypical"]
        },
        "management_hints": "Treatment: Propranolol, primidone (first-line). Topiramate, gabapentin (second-line). Deep brain stimulation if severe. Avoid caffeine. Usually progressive but benign."
    },
    "Parkinson Disease": {
        "symptoms": {
            "required": ["tremor"],
            "supporting": ["rest_tremor", "pill_rolling", "unilateral_onset", "rigidity", "bradykinesia", "postural_instability", "masked_facies", "shuffling_gait"],
            "contradictory": ["action_tremor_only", "no_rigidity", "no_bradykinesia"]
        },
        "demographics": {
            "age_risk": {"<40": 0.1, "40-70": 0.5, ">70": 0.8},
            "sex_risk": {"male": 1.3, "female": 0.8}
        },
        "risk_factors": ["age", "family_history", "pesticide_exposure", "head_trauma"],
        "specificity": 0.85,
        "urgency": "non_urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["Neurologic_exam", "UPDRS"],
            "within_6h": ["MRI_brain"],
            "optional": ["DaTscan", "PET_scan"]
        },
        "management_hints": "Treatment: Levodopa/carbidopa (gold standard). Dopamine agonists, MAO-B inhibitors. Physical therapy. Deep brain stimulation if advanced. Multidisciplinary care."
    },
    "Medication-Induced Tremor": {
        "symptoms": {
            "required": ["tremor"],
            "supporting": ["medication_use", "recent_medication_start", "dose_related", "action_tremor", "antidepressants", "lithium", "valproate", "antipsychotics"],
            "contradictory": ["no_medication_use"]
        },
        "demographics": {
            "age_risk": {"<40": 0.4, "40-70": 0.5, ">70": 0.6},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["antidepressants", "lithium", "valproate", "antipsychotics", "stimulants", "theophylline", "corticosteroids"],
        "specificity": 0.75,
        "urgency": "non_urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["Medication_review", "Neurologic_exam"],
            "within_6h": [],
            "optional": []
        },
        "management_hints": "Review medications. Reduce dose or discontinue if possible. Switch to alternative medication. Propranolol may help. Most cases improve with medication adjustment."
    },
    "Hyperthyroidism": {
        "symptoms": {
            "required": ["tremor"],
            "supporting": ["action_tremor", "fine_tremor", "anxiety", "tachycardia", "weight_loss", "heat_intolerance", "sweating", "elevated_T4", "low_TSH"],
            "contradictory": ["normal_thyroid_function", "hypothyroid_symptoms"]
        },
        "demographics": {
            "age_risk": {"<40": 0.5, "40-70": 0.4, ">70": 0.3},
            "sex_risk": {"male": 0.3, "female": 1.7}
        },
        "risk_factors": ["Graves_disease", "toxic_nodule", "thyroiditis", "iodine_excess", "autoimmune"],
        "specificity": 0.80,
        "urgency": "non_urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["TSH", "Free_T4", "Free_T3"],
            "within_6h": ["Thyroid_antibodies", "Thyroid_ultrasound"],
            "optional": ["Radioactive_iodine_uptake"]
        },
        "management_hints": "Treatment: Antithyroid medications (methimazole, PTU), beta-blockers for symptoms. Radioactive iodine or surgery if refractory. Tremor improves with thyroid normalization."
    },
    "Cerebellar Tremor": {
        "symptoms": {
            "required": ["tremor"],
            "supporting": ["intention_tremor", "ataxia", "dysmetria", "dysdiadochokinesia", "nystagmus", "dysarthria", "worsens_with_movement"],
            "contradictory": ["no_ataxia", "rest_tremor"]
        },
        "demographics": {
            "age_risk": {"<40": 0.4, "40-70": 0.5, ">70": 0.4},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["stroke", "MS", "tumor", "alcohol", "trauma", "degenerative_diseases"],
        "specificity": 0.80,
        "urgency": "urgent",
        "rule_out_first": True,
        "workup": {
            "immediate": ["MRI_brain", "Neurologic_exam"],
            "within_6h": ["CT_if_MRI_not_available"],
            "optional": ["EMG", "Lumbar_puncture_if_MS_suspected"]
        },
        "management_hints": "URGENT! Cerebellar tremor suggests structural lesion. MRI required. Treatment: Address underlying cause (stroke, tumor, MS). Medications (clonazepam, propranolol) may help. Physical therapy."
    },
    "Wilson Disease": {
        "symptoms": {
            "required": ["tremor"],
            "supporting": ["young_age", "liver_disease", "Kayser_Fleischer_rings", "psychiatric_symptoms", "dystonia", "rigidity", "elevated_urinary_copper", "low_ceruloplasmin"],
            "contradictory": ["old_age", "normal_copper_studies"]
        },
        "demographics": {
            "age_risk": {"<40": 0.8, "40-70": 0.2, ">70": 0.1},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["family_history", "genetics", "young_age"],
        "specificity": 0.70,
        "urgency": "urgent",
        "rule_out_first": True,
        "workup": {
            "immediate": ["Ceruloplasmin", "24h_urinary_copper", "Slit_lamp_exam", "LFTs"],
            "within_6h": ["Liver_biopsy_if_needed"],
            "optional": ["Genetic_testing"]
        },
        "management_hints": "URGENT! Wilson disease is treatable but fatal if untreated. Treatment: Copper chelation (penicillamine, trientine), zinc. Liver transplant if advanced. Lifelong treatment required."
    },
    "Physiologic Tremor": {
        "symptoms": {
            "required": ["tremor"],
            "supporting": ["fine_tremor", "action_tremor", "postural_tremor", "hands", "anxiety", "fatigue", "caffeine", "stress", "normal_exam"],
            "contradictory": ["rest_tremor", "coarse_tremor", "neurologic_abnormalities"]
        },
        "demographics": {
            "age_risk": {"<40": 0.6, "40-70": 0.4, ">70": 0.3},
            "sex_risk": {"male": 1.0, "female": 1.0}
        },
        "risk_factors": ["anxiety", "stress", "fatigue", "caffeine", "hypoglycemia", "hyperthyroidism"],
        "specificity": 0.70,
        "urgency": "non_urgent",
        "rule_out_first": False,
        "workup": {
            "immediate": ["History", "Neurologic_exam"],
            "within_6h": ["Thyroid_function_if_needed"],
            "optional": []
        },
        "management_hints": "Treatment: Address underlying causes (anxiety, stress, caffeine). Usually benign and self-limited. Reassurance. Propranolol if bothersome. No specific treatment needed if mild."
    }
}

__all__ = ['TREMOR_DDX']

