"""DDx Knowledge Base - Data
Differential diagnosis data for common clinical scenarios

NOTE: This file contains only data dictionaries.
Functions are in ddx_data.py"""

# Joint Pain Differential Diagnosis

JOINT_PAIN_DDX = {'Septic Arthritis': {'symptoms': {'required': ['joint_pain',
    'joint_swelling'], 'supporting': ['fever', 'monoarthritis', 'erythema',
    'warm_joint', 'reduced_range_motion', 'recent_joint_surgery'],
    'contradictory': ['polyarticular_symmetric', 'morning_stiffness',
    'chronic_course']}, 'demographics': {'age_risk': {'<20': 0.5, '20-50': 
    0.6, '>50': 0.7}, 'sex_risk': {'male': 1.1, 'female': 1.0}},
    'risk_factors': ['diabetes', 'IV_drug_use', 'joint_surgery',
    'immunosuppression', 'recent_bacteremia'], 'specificity': 0.75,
    'urgency': 'emergency', 'rule_out_first': True, 'workup': {'immediate':
    ['Joint_aspiration', 'Synovial_WBC', 'Gram_stain', 'Blood_cultures',
    'ESR_CRP'], 'within_6h': ['X_ray_joint'], 'optional': ['MRI_joint']},
    'management_hints':
    'URGENT! If fever + monoarthritis → Think SEPTIC immediately! Joint aspiration mandatory. Surgical drainage if required.'
    }, 'Gout': {'symptoms': {'required': ['joint_pain', 'joint_swelling'],
    'supporting': ['acute_onset', 'first_metatarsophalangeal_mtp',
    'podagra', 'erythema', 'unilateral', 'tophi', 'hyperuricemia'],
    'contradictory': ['symmetric_joints', 'morning_stiffness',
    'chronic_joint_deformity']}, 'demographics': {'age_risk': {'<40': 0.4,
    '40-70': 0.8, '>70': 0.7}, 'sex_risk': {'male': 1.5, 'female': 1.0}},
    'risk_factors': ['alcohol', 'high_purine_diet', 'diuretic_use',
    'obesity', 'hypertension', 'renal_disease'], 'specificity': 0.7,
    'urgency': 'urgent', 'rule_out_first': True, 'workup': {'immediate': [
    'Synovial_fluid_analysis', 'Uric_acid', 'ESR_CRP'], 'within_6h': [],
    'optional': ['X_ray_joint']}, 'management_hints':
    "NSAIDs or colchicine for acute attack. Allopurinol for prophylaxis. Check uric acid, but normal uric acid doesn't rule out gout."
    }, 'Rheumatoid Arthritis Flare': {'symptoms': {'required': [
    'joint_pain', 'joint_swelling'], 'supporting': ['morning_stiffness',
    'polyarticular_symmetric', 'small_joints', 'wrist_mcp_pip',
    'rheumatoid_factor', 'chronic_course'], 'contradictory': [
    'acute_monoarthritis', 'first_mtp', 'pseudogout_crystals']},
    'demographics': {'age_risk': {'<40': 0.3, '40-70': 0.6, '>70': 0.4},
    'sex_risk': {'male': 1.0, 'female': 2.5}}, 'risk_factors': [
    'family_history_ra', 'smoking', 'age_30_50'], 'specificity': 0.65,
    'urgency': 'urgent', 'rule_out_first': False, 'workup': {'immediate': [
    'RF_CCP', 'ESR_CRP', 'X_ray_hands_feet'], 'within_6h': [], 'optional':
    ['US_joints', 'MRI_joints']}, 'management_hints':
    'If already diagnosed RA → Escalate DMARDs. If new presentation → Rheumatology consult for diagnosis and treatment.'
    }, 'Pseudogout (CPPD)': {'symptoms': {'required': ['joint_pain',
    'joint_swelling'], 'supporting': ['knee_wrist', 'elderly',
    'chronic_kidney_disease', 'hyperparathyroidism', 'acute_onset',
    'calcification_joints'], 'contradictory': ['first_mtp',
    'monosodium_urate']}, 'demographics': {'age_risk': {'<40': 0.2, '40-70':
    0.5, '>70': 0.8}, 'sex_risk': {'male': 1.0, 'female': 1.0}},
    'risk_factors': ['elderly', 'hypercalcemia', 'hyperparathyroidism',
    'hemochromatosis', 'hypomagnesemia'], 'specificity': 0.6, 'urgency':
    'urgent', 'rule_out_first': False, 'workup': {'immediate': [
    'Synovial_fluid_analysis', 'Calcium_Mg_PO4', 'ESR_CRP'], 'within_6h': [
    ], 'optional': ['X_ray_joint', 'Parathyroid']}, 'management_hints':
    'Similar to gout but different joints (knee > wrist). Calcium pyrophosphate crystals. Check calcium, Mg, PO4.'
    }, 'Osteoarthritis': {'symptoms': {'required': ['joint_pain'],
    'supporting': ['chronic_course', 'weight_bearing_joints',
    'knee_hip_spine', 'worse_with_activity', 'crepitus', 'bone_spurs'],
    'contradictory': ['acute_onset', 'fever', 'systemic_symptoms',
    'morning_stiffness_prolonged']}, 'demographics': {'age_risk': {'<40': 
    0.2, '40-70': 0.7, '>70': 0.9}, 'sex_risk': {'male': 1.0, 'female': 1.2
    }}, 'risk_factors': ['age', 'obesity', 'joint_trauma', 'repetitive_use',
    'genetics'], 'specificity': 0.85, 'urgency': 'non_urgent',
    'rule_out_first': False, 'workup': {'immediate': ['X_ray_joint'],
    'within_6h': [], 'optional': []}, 'management_hints':
    'Conservative: NSAIDs, exercise, weight loss. If severe → Joint injection or replacement. Usually self-limited.'
    }}

__all__ = ['JOINT_PAIN_DDX']
