"""
Protocol Routing Configuration
Dictionary-based routing for protocols to replace long if-elif chains
"""

from typing import Callable, Dict, List, Optional, Tuple
# Import all render functions from protocols module
from protocols import (
    render_acute_pulmonary_edema,
    render_tca_overdose,
    render_digoxin_toxicity,
    render_severe_hypoglycemia,
    render_chest_trauma,
    render_abdominal_trauma,
    render_burn_management,
    render_sepsis,
    render_sepsis_3hour,
    render_shock,
    render_stroke,
    render_gi_bleeding,
    render_dka,
    render_electrolytes,
    render_anaphylaxis,
    render_hypertensive_emergency,
    render_status_epilepticus,
    render_opioid_overdose,
    render_alcohol_withdrawal,
    render_paracetamol_overdose,
    render_salicylate_overdose,
    render_carbon_monoxide_poisoning,
    render_organophosphate_poisoning,
    render_toxic_alcohol_poisoning,
    render_malignant_arrhythmias,
    render_pneumothorax,
    render_traumatic_brain_injury,
    render_drowning,
    render_heat_stroke,
    render_hypothermia,
    render_cardiac_arrest,
    render_upper_airway_obstruction,
    render_spinal_cord_injury,
    render_green_pit_viper_bite,
    render_cobra_bite,
    render_krait_bite,
    render_acute_pain,
    render_copd,
    render_asthma,
    render_acute_respiratory_failure,
    render_pulmonary_tb,
    render_severe_influenza,
    render_bronchiolitis,
    render_acs,
    render_stemi,
    render_nstemi,
    render_cardiac_tamponade,
    render_aortic_dissection,
    render_hf,
    render_acute_decompensated_hf,
    render_atrial_fibrillation,
    render_dvt_pe,
    render_bradycardia,
    render_tachycardia,
    render_aki,
    render_uti_pyelonephritis,
    render_nephrolithiasis,
    render_bph_urinary_retention,
    render_chronic_glomerulonephritis,
    render_nephrotic_syndrome,
    render_ckd,
    render_diabetic_nephropathy,
    render_hypertensive_nephrosclerosis,
    render_hepatorenal_syndrome,
    render_emergency_dialysis,
    render_ckd_anemia,
    render_resistant_hypertension_ckd,
    render_blood_pressure_ckd,
    render_iga_nephropathy,
    render_lupus_nephritis,
    render_heart_failure_ckd,
    render_anca_vasculitis,
    render_cap,
    render_hap_vap,
    render_cdiff,
    render_meningitis,
    render_endocarditis,
    render_parasitic_worms,
    render_dengue_fever,
    render_scrub_typhus,
    render_malaria,
    render_thyrotoxic_crisis,
    render_myxedema_coma,
    render_adrenal_crisis,
    render_hhs,
    render_hypoglycemia,
    render_acute_pancreatitis,
    render_acute_liver_failure,
    render_acute_mesenteric_ischemia,
    render_cholecystitis_cholangitis,
    render_acute_appendicitis,
    render_acute_diverticulitis,
    render_acute_intestinal_obstruction,
    render_acute_hepatitis,
    render_acute_colitis,
    render_hepatitis_b,
    render_h_pylori_gastritis,
    render_hepatitis_c,
    render_gerd,
    render_ibs,
    render_cirrhosis,
    render_nafld,
    render_chronic_constipation,
    render_acute_diarrhea,
    render_lower_gi_bleeding,
    render_perforated_peptic_ulcer,
    render_biliary_obstruction,
    render_decompensated_cirrhosis,
    render_transfusion,
    render_anticoagulation_reversal,
    render_itp,
    render_ttp_hus,
    render_dic,
    render_delirium,
    render_sedation,
    render_ards,
    render_ventilator_weaning,
    render_stress_ulcer,
    render_icp_management,
    render_crrt,
    render_tls,
    render_febrile_neutropenia,
    render_hypercalcemia,
    render_ibd_exacerbation,
    render_serotonin_syndrome,
    render_neuroleptic_malignant_syndrome,
    render_intracranial_hypertension,
    render_eclampsia,
    render_postpartum_hemorrhage,
    render_preeclampsia,
    render_hellp_syndrome,
    render_chorioamnionitis,
    render_placental_abruption,
    render_uterine_rupture,
    render_stevens_johnson_syndrome,
    render_atopic_dermatitis,
    render_contact_dermatitis,
    render_acne_vulgaris,
    render_fungal_infections,
    render_scabies,
    render_urticaria,
    render_psoriasis
)
# Import rheumatology functions (some not in main protocols module)
from protocols.rheumatology import (
    render_acute_gout,
    render_ra_flare,
    render_osteoarthritis,
    render_ankylosing_spondylitis,
    render_reactive_arthritis,
    render_psoriatic_arthritis,
    render_sle_arthritis
)


# Protocol routing configuration
# Format: {
#     "protocol_id": {
#         "keywords": [list of keywords to match],
#         "render": render_function,
#         "has_article": bool,
#         "article_function": "render_xxx" (if has_article),
#         "priority": int (higher = checked first, for special cases),
#         "exclude_keywords": [keywords that should NOT be present],
#         "require_all": bool (if True, all keywords must match)
#     }
# }
PROTOCOL_ROUTING: Dict[str, Dict] = {
    # Emergency - High priority (check first)
    "cardiac_arrest": {
        "keywords": ["Cardiac Arrest", "ACLS", "cardiac arrest", "acls"],
        "render": render_cardiac_arrest,
        "has_article": False,
        "priority": 10
    },
    "sepsis_1hour": {
        "keywords": ["Sepsis 1-Hour", "Sepsis 1 Hour"],
        "render": render_sepsis,
        "has_article": True,
        "article_function": "render_sepsis",
        "priority": 9
    },
    "sepsis_3hour": {
        "keywords": ["Sepsis 3-Hour", "Sepsis 3 Hour"],
        "render": render_sepsis_3hour,
        "has_article": False,
        "priority": 9
    },
    "sepsis": {
        "keywords": ["Sepsis"],
        "render": render_sepsis,
        "has_article": True,
        "article_function": "render_sepsis",
        "priority": 8
    },
    "stroke": {
        "keywords": ["Stroke"],
        "render": render_stroke,
        "has_article": True,
        "article_function": "render_stroke",
        "priority": 10
    },
    "anaphylaxis": {
        "keywords": ["Anaphylaxis", "anaphylaxis"],
        "render": render_anaphylaxis,
        "has_article": True,
        "article_function": "render_anaphylaxis",
        "priority": 10
    },
    "upper_airway": {
        "keywords": ["Upper Airway", "Tắc Nghẽn Đường Thở", "upper airway", "airway obstruction"],
        "render": render_upper_airway_obstruction,
        "has_article": False,
        "priority": 10
    },
    "spinal_cord": {
        "keywords": ["Spinal Cord", "Chấn Thương Tủy", "spinal cord", "tủy sống"],
        "render": render_spinal_cord_injury,
        "has_article": False,
        "priority": 10
    },
    "shock": {
        "keywords": ["Sốc"],
        "render": render_shock,
        "has_article": False,
        "priority": 8
    },
    "gi_bleeding": {
        "keywords": ["GI Bleeding", "GI"],
        "render": render_gi_bleeding,
        "has_article": False,
        "priority": 8
    },
    "dka": {
        "keywords": ["DKA"],
        "render": render_dka,
        "has_article": False,
        "priority": 8
    },
    "electrolytes": {
        "keywords": ["Electrolyte"],
        "render": render_electrolytes,
        "has_article": False,
        "priority": 8
    },
    "hypertensive_emergency": {
        "keywords": ["Tăng Huyết áp", "Hypertensive", "hypertensive"],
        "render": render_hypertensive_emergency,
        "has_article": False,
        "priority": 8
    },
    "status_epilepticus": {
        "keywords": ["Status Epilepticus", "status epilepticus", "Epilepticus", "Trạng thái động kinh"],
        "render": render_status_epilepticus,
        "has_article": False,
        "priority": 8
    },
    "opioid_overdose": {
        "keywords": ["Opioid", "opioid", "Naloxone", "naloxone"],
        "render": render_opioid_overdose,
        "has_article": False,
        "priority": 8
    },
    "alcohol_withdrawal": {
        "keywords": ["Alcohol", "alcohol", "Cai rượu", "cai rượu", "Rượu"],
        "render": render_alcohol_withdrawal,
        "has_article": False,
        "priority": 8
    },
    "paracetamol_overdose": {
        "keywords": ["Paracetamol", "paracetamol", "Acetaminophen", "acetaminophen"],
        "render": render_paracetamol_overdose,
        "has_article": False,
        "priority": 8
    },
    "salicylate_overdose": {
        "keywords": ["Salicylate", "salicylate", "Aspirin", "aspirin"],
        "render": render_salicylate_overdose,
        "has_article": False,
        "priority": 8
    },
    "carbon_monoxide": {
        "keywords": ["Carbon Monoxide", "carbon monoxide", "CO", "Carbon"],
        "render": render_carbon_monoxide_poisoning,
        "has_article": False,
        "priority": 8
    },
    "organophosphate": {
        "keywords": ["Organophosphate", "organophosphate"],
        "render": render_organophosphate_poisoning,
        "has_article": False,
        "priority": 8
    },
    "toxic_alcohol": {
        "keywords": ["Alcohol Độc Hại", "Methanol", "Ethylene Glycol", "toxic alcohol"],
        "render": render_toxic_alcohol_poisoning,
        "has_article": False,
        "priority": 8
    },
    "malignant_arrhythmias": {
        "keywords": ["Loạn nhịp nguy hiểm", "Malignant Arrhythmias", "malignant arrhythmias"],
        "render": render_malignant_arrhythmias,
        "has_article": False,
        "priority": 8
    },
    "pneumothorax": {
        "keywords": ["Pneumothorax", "pneumothorax", "Tràn khí màng phổi"],
        "render": render_pneumothorax,
        "has_article": False,
        "priority": 8
    },
    "traumatic_brain_injury": {
        "keywords": ["Traumatic Brain Injury", "Chấn thương sọ não", "traumatic brain injury"],
        "render": render_traumatic_brain_injury,
        "has_article": False,
        "priority": 8
    },
    "drowning": {
        "keywords": ["Drowning", "drowning", "Đuối nước"],
        "render": render_drowning,
        "has_article": False,
        "priority": 8
    },
    "heat_stroke": {
        "keywords": ["Heat Stroke", "Sốc Nhiệt", "heat stroke"],
        "render": render_heat_stroke,
        "has_article": False,
        "priority": 8
    },
    "hypothermia": {
        "keywords": ["Hypothermia", "hypothermia", "Hạ thân nhiệt"],
        "render": render_hypothermia,
        "has_article": False,
        "priority": 8
    },
    "green_pit_viper": {
        "keywords": ["Rắn Lục Xanh", "green pit viper", "lục xanh đuôi đỏ"],
        "render": render_green_pit_viper_bite,
        "has_article": False,
        "priority": 8
    },
    "cobra": {
        "keywords": ["Rắn Hổ Mang", "cobra", "hổ mang"],
        "render": render_cobra_bite,
        "has_article": False,
        "priority": 8
    },
    "krait": {
        "keywords": ["Rắn Cạp Nia", "krait", "cạp nia"],
        "render": render_krait_bite,
        "has_article": False,
        "priority": 8
    },
    "acute_pulmonary_edema": {
        "keywords": ["Phù Phổi Cấp", "Acute Pulmonary Edema", "acute pulmonary edema", "phù phổi cấp"],
        "render": render_acute_pulmonary_edema,
        "has_article": False,
        "priority": 8
    },
    "tca_overdose": {
        "keywords": ["Ngộ Độc TCA", "TCA Overdose", "Tricyclic Antidepressant", "tca overdose", "ngộ độc tca"],
        "render": render_tca_overdose,
        "has_article": False,
        "priority": 8
    },
    "digoxin_toxicity": {
        "keywords": ["Ngộ Độc Digoxin", "Digoxin Toxicity", "digoxin toxicity", "ngộ độc digoxin"],
        "render": render_digoxin_toxicity,
        "has_article": False,
        "priority": 8
    },
    "severe_hypoglycemia": {
        "keywords": ["Hạ Đường Huyết Cấp Cứu", "Severe Hypoglycemia", "severe hypoglycemia", "hạ đường huyết cấp cứu"],
        "render": render_severe_hypoglycemia,
        "has_article": False,
        "priority": 8
    },
    "chest_trauma": {
        "keywords": ["Chấn thương ngực", "Chest Trauma", "chest trauma", "chấn thương ngực"],
        "render": render_chest_trauma,
        "has_article": False,
        "priority": 9
    },
    "abdominal_trauma": {
        "keywords": ["Chấn thương bụng", "Abdominal Trauma", "abdominal trauma", "chấn thương bụng"],
        "render": render_abdominal_trauma,
        "has_article": False,
        "priority": 9
    },
    "burn_management": {
        "keywords": ["Bỏng", "Burn", "burn", "Burn Management"],
        "render": render_burn_management,
        "has_article": False,
        "priority": 9
    },
    
    # Respiratory
    "acute_respiratory_failure": {
        "keywords": ["Respiratory Failure", "Suy Hô Hấp", "respiratory failure"],
        "render": render_acute_respiratory_failure,
        "has_article": False,
        "priority": 8
    },
    "copd": {
        "keywords": ["COPD"],
        "render": render_copd,
        "has_article": True,
        "article_function": "render_copd",
        "priority": 8
    },
    "asthma": {
        "keywords": ["Hen"],
        "render": render_asthma,
        "has_article": False,
        "priority": 8
    },
    "cap": {
        "keywords": ["Viêm phổi cộng đồng", "CAP"],
        "render": render_cap,
        "has_article": True,
        "article_function": "render_cap",
        "priority": 8
    },
    "severe_influenza": {
        "keywords": ["Cúm", "influenza"],
        "render": render_severe_influenza,
        "has_article": False,
        "priority": 8
    },
    "pulmonary_tb": {
        "keywords": ["Lao phổi", "tuberculosis"],
        "render": render_pulmonary_tb,
        "has_article": False,
        "priority": 8
    },
    "bronchiolitis": {
        "keywords": ["Tiểu phế quản", "bronchiolitis"],
        "render": render_bronchiolitis,
        "has_article": False,
        "priority": 8
    },
    
    # Cardiology
    "stemi": {
        "keywords": ["STEMI", "stemi", "ST-Elevation", "ST Elevation"],
        "render": render_stemi,
        "has_article": False,
        "priority": 10
    },
    "nstemi": {
        "keywords": ["NSTEMI", "nstemi", "Non-ST-Elevation", "Non ST Elevation"],
        "render": render_nstemi,
        "has_article": False,
        "priority": 10
    },
    "cardiac_tamponade": {
        "keywords": ["Chèn Ép Tim", "Cardiac Tamponade", "cardiac tamponade", "chèn ép tim"],
        "render": render_cardiac_tamponade,
        "has_article": False,
        "priority": 10
    },
    "aortic_dissection": {
        "keywords": ["Bóc Tách Động Mạch Chủ", "Aortic Dissection", "aortic dissection", "bóc tách"],
        "render": render_aortic_dissection,
        "has_article": False,
        "priority": 10
    },
    "acs": {
        "keywords": ["ACS"],
        "render": render_acs,
        "has_article": True,
        "article_function": "render_acs",
        "priority": 10
    },
    "heart_failure": {
        "keywords": ["Suy tim"],
        "exclude_keywords": ["Mất Bù", "ADHF"],
        "render": render_hf,
        "has_article": True,
        "article_function": "render_hf",
        "priority": 9
    },
    "acute_decompensated_hf": {
        "keywords": ["ADHF", "Mất Bù", "acute decompensated"],
        "render": render_acute_decompensated_hf,
        "has_article": True,
        "article_function": "render_acute_decompensated_hf",
        "priority": 10
    },
    "atrial_fibrillation": {
        "keywords": ["Rung Nhĩ", "Atrial Fibrillation", "atrial fibrillation", "AF"],
        "render": render_atrial_fibrillation,
        "has_article": True,
        "article_function": "render_atrial_fibrillation",
        "priority": 8
    },
    "dvt_pe": {
        "keywords": ["DVT", "PE", "dvt", "pe", "Huyết Khối", "Thuyên Tắc"],
        "render": render_dvt_pe,
        "has_article": True,
        "article_function": "render_dvt_pe",
        "priority": 8
    },
    "bradycardia": {
        "keywords": ["Bradycardia", "bradycardia", "Nhịp chậm"],
        "render": render_bradycardia,
        "has_article": False,
        "priority": 8
    },
    "tachycardia": {
        "keywords": ["Tachycardia", "tachycardia", "Nhịp nhanh"],
        "render": render_tachycardia,
        "has_article": False,
        "priority": 8
    },
    
    # Nephrology
    "aki": {
        "keywords": ["AKI"],
        "render": render_aki,
        "has_article": True,
        "article_function": "render_aki",
        "priority": 10
    },
    "hepatorenal_syndrome": {
        "keywords": ["Hội Chứng Gan Thận", "Hepatorenal Syndrome", "hepatorenal syndrome", "hội chứng gan thận"],
        "render": render_hepatorenal_syndrome,
        "has_article": False,
        "priority": 9
    },
    "emergency_dialysis": {
        "keywords": ["Lọc Máu Cấp Cứu", "Emergency Dialysis", "emergency dialysis", "lọc máu"],
        "render": render_emergency_dialysis,
        "has_article": False,
        "priority": 9
    },
    "uti_pyelonephritis": {
        "keywords": ["Nhiễm trùng tiểu", "bể thận", "UTI"],
        "render": render_uti_pyelonephritis,
        "has_article": False,
        "priority": 8
    },
    "nephrolithiasis": {
        "keywords": ["Sỏi thận", "quặn thận", "renal colic"],
        "render": render_nephrolithiasis,
        "has_article": False,
        "priority": 8
    },
    "bph_urinary_retention": {
        "keywords": ["BPH", "Bí tiểu", "bph"],
        "render": render_bph_urinary_retention,
        "has_article": False,
        "priority": 8
    },
    "chronic_glomerulonephritis": {
        "keywords": ["Viêm cầu thận mạn", "Glomerulonephritis", "glomerulonephritis"],
        "render": render_chronic_glomerulonephritis,
        "has_article": False,
        "priority": 8
    },
    "nephrotic_syndrome": {
        "keywords": ["Hội chứng thận hư", "Nephrotic", "nephrotic"],
        "render": render_nephrotic_syndrome,
        "has_article": False,
        "priority": 8
    },
    "ckd": {
        "keywords": ["Suy thận mạn", "CKD", "ckd"],
        "render": render_ckd,
        "has_article": False,
        "priority": 8
    },
    "ckd_anemia": {
        "keywords": ["Thiếu Máu Trong CKD", "KDIGO 2026", "thiếu máu", "anemia", "CKD anemia"],
        "render": render_ckd_anemia,
        "has_article": True,
        "article_function": "render_ckd_anemia",
        "priority": 8
    },
    "resistant_hypertension_ckd": {
        "keywords": ["Tăng Huyết Áp Kháng Trị", "resistant hypertension", "CKD", "tăng huyết áp kháng trị"],
        "render": render_resistant_hypertension_ckd,
        "has_article": True,
        "article_function": "render_resistant_hypertension_ckd",
        "priority": 8
    },
    "blood_pressure_ckd": {
        "keywords": ["Quản Lý Huyết Áp Trong CKD", "Blood Pressure", "KDIGO 2021", "huyết áp trong CKD"],
        "render": render_blood_pressure_ckd,
        "has_article": True,
        "article_function": "render_blood_pressure_ckd",
        "priority": 8
    },
    "iga_nephropathy": {
        "keywords": ["IgA Nephropathy", "IgAN", "Bệnh thận IgA", "KDIGO 2021", "glomerulonephritis"],
        "render": render_iga_nephropathy,
        "has_article": True,
        "article_function": "render_iga_nephropathy",
        "priority": 8
    },
    "lupus_nephritis": {
        "keywords": ["Lupus Nephritis", "viêm thận lupus", "SLE nephritis", "KDIGO 2021", "lupus nephritis"],
        "render": render_lupus_nephritis,
        "has_article": True,
        "article_function": "render_lupus_nephritis",
        "priority": 8
    },
    "anca_vasculitis": {
        "keywords": ["ANCA vasculitis", "viêm mạch ANCA", "GPA", "MPA", "EGPA", "KDIGO 2021", "ANCA"],
        "render": render_anca_vasculitis,
        "has_article": True,
        "article_function": "render_anca_vasculitis",
        "priority": 8
    },
    "heart_failure_ckd": {
        "keywords": ["Suy Tim Trong CKD", "Heart Failure CKD", "cardiorenal", "KDIGO 2025", "suy tim CKD"],
        "render": render_heart_failure_ckd,
        "has_article": True,
        "article_function": "render_heart_failure_ckd",
        "priority": 9
    },
    "diabetic_nephropathy": {
        "keywords": ["đái tháo đường", "Diabetic", "diabetic"],
        "render": render_diabetic_nephropathy,
        "has_article": False,
        "priority": 8
    },
    "hypertensive_nephrosclerosis": {
        "keywords": ["tăng huyết áp", "Hypertensive", "hypertensive", "Nephrosclerosis"],
        "render": render_hypertensive_nephrosclerosis,
        "has_article": False,
        "priority": 7
    },
    
    # Infectious
    "hap_vap": {
        "keywords": ["HAP", "VAP"],
        "render": render_hap_vap,
        "has_article": False,
        "priority": 8
    },
    "cdiff": {
        "keywords": ["C. diff", "cdiff"],
        "render": render_cdiff,
        "has_article": False,
        "priority": 8
    },
    "meningitis": {
        "keywords": ["Meningitis", "meningitis", "Encephalitis", "encephalitis"],
        "render": render_meningitis,
        "has_article": False,
        "priority": 8
    },
    "endocarditis": {
        "keywords": ["Endocarditis", "endocarditis", "Viêm nội tâm mạc"],
        "render": render_endocarditis,
        "has_article": False,
        "priority": 8
    },
    "dengue": {
        "keywords": ["Dengue", "dengue", "Sốt Xuất Huyết", "sốt xuất huyết"],
        "render": render_dengue_fever,
        "has_article": False,
        "priority": 8
    },
    "scrub_typhus": {
        "keywords": ["Sốt Mò", "Scrub Typhus", "scrub typhus", "sốt mò"],
        "render": render_scrub_typhus,
        "has_article": False,
        "priority": 8
    },
    "malaria": {
        "keywords": ["Sốt Rét", "Malaria", "malaria", "sốt rét"],
        "render": render_malaria,
        "has_article": False,
        "priority": 8
    },
    "parasitic_worms": {
        "keywords": ["Ký sinh Trùng", "Parasitic", "parasitic", "Giun Sán", "giun sán"],
        "render": render_parasitic_worms,
        "has_article": False,
        "priority": 8
    },
    
    # Endocrinology
    "thyrotoxic_crisis": {
        "keywords": ["Thyrotoxic", "thyrotoxic"],
        "render": render_thyrotoxic_crisis,
        "has_article": False,
        "priority": 8
    },
    "myxedema_coma": {
        "keywords": ["Myxedema", "myxedema"],
        "render": render_myxedema_coma,
        "has_article": False,
        "priority": 8
    },
    "adrenal_crisis": {
        "keywords": ["Adrenal", "adrenal"],
        "render": render_adrenal_crisis,
        "has_article": False,
        "priority": 8
    },
    "hhs": {
        "keywords": ["HHS", "Hyperosmolar", "hyperosmolar"],
        "render": render_hhs,
        "has_article": False,
        "priority": 8
    },
    "hypoglycemia": {
        "keywords": ["Hypoglycemia", "hypoglycemia", "Hạ đường huyết"],
        "render": render_hypoglycemia,
        "has_article": False,
        "priority": 8
    },
    
    # Gastroenterology
    "acute_pancreatitis": {
        "keywords": ["Pancreatitis", "pancreatitis", "Tụy"],
        "render": render_acute_pancreatitis,
        "has_article": False,
        "priority": 8
    },
    "acute_liver_failure": {
        "keywords": ["Liver Failure", "liver failure", "Suy gan"],
        "render": render_acute_liver_failure,
        "has_article": False,
        "priority": 8
    },
    "acute_mesenteric_ischemia": {
        "keywords": ["Mesenteric Ischemia", "Thiếu Máu Mạc Treo", "mesenteric ischemia", "mạc treo"],
        "render": render_acute_mesenteric_ischemia,
        "has_article": False,
        "priority": 8
    },
    "cholecystitis_cholangitis": {
        "keywords": ["Cholecystitis", "Cholangitis", "Túi Mật", "Đường Mật", "cholecystitis", "cholangitis"],
        "render": render_cholecystitis_cholangitis,
        "has_article": False,
        "priority": 8
    },
    "acute_appendicitis": {
        "keywords": ["Appendicitis", "Ruột Thừa", "appendicitis", "ruột thừa"],
        "render": render_acute_appendicitis,
        "has_article": False,
        "priority": 8
    },
    "acute_diverticulitis": {
        "keywords": ["Diverticulitis", "Túi Thừa", "diverticulitis", "túi thừa"],
        "render": render_acute_diverticulitis,
        "has_article": False,
        "priority": 8
    },
    "acute_intestinal_obstruction": {
        "keywords": ["Intestinal Obstruction", "Tắc Ruột", "intestinal obstruction", "tắc ruột"],
        "render": render_acute_intestinal_obstruction,
        "has_article": False,
        "priority": 8
    },
    "acute_hepatitis": {
        "keywords": ["Hepatitis", "Viêm Gan Cấp", "hepatitis"],
        "exclude_keywords": ["B", "C", "Viral"],
        "require_all": False,
        "render": render_acute_hepatitis,
        "has_article": False,
        "priority": 7
    },
    "acute_colitis": {
        "keywords": ["Colitis", "Viêm Đại Tràng Cấp", "colitis"],
        "exclude_keywords": ["IBD"],
        "require_all": False,
        "render": render_acute_colitis,
        "has_article": False,
        "priority": 7
    },
    "ibd_exacerbation": {
        "keywords": ["IBD", "ibd", "Crohn", "Colitis"],
        "render": render_ibd_exacerbation,
        "has_article": False,
        "priority": 8
    },
    "hepatitis_b": {
        "keywords": ["Hepatitis B", "Viêm Gan B", "hepatitis b", "viêm gan b"],
        "render": render_hepatitis_b,
        "has_article": False,
        "priority": 9
    },
    "h_pylori_gastritis": {
        "keywords": ["H. pylori", "pylori", "HP (+)", "HP dương", "Viêm Loét Dạ Dày HP"],
        "render": render_h_pylori_gastritis,
        "has_article": False,
        "priority": 8
    },
    "hepatitis_c": {
        "keywords": ["Hepatitis C", "Viêm Gan C", "hepatitis c", "viêm gan c"],
        "render": render_hepatitis_c,
        "has_article": False,
        "priority": 9
    },
    "gerd": {
        "keywords": ["GERD", "Trào Ngược", "gerd", "trào ngược", "Gastroesophageal Reflux"],
        "render": render_gerd,
        "has_article": False,
        "priority": 8
    },
    "ibs": {
        "keywords": ["IBS", "Ruột Kích Thích", "ibs", "ruột kích thích", "Irritable Bowel"],
        "render": render_ibs,
        "has_article": False,
        "priority": 8
    },
    "cirrhosis": {
        "keywords": ["Cirrhosis", "Xơ Gan", "cirrhosis", "xơ gan"],
        "render": render_cirrhosis,
        "has_article": False,
        "priority": 8
    },
    "nafld": {
        "keywords": ["NAFLD", "NASH", "Gan Nhiễm Mỡ", "nafld", "nash", "gan nhiễm mỡ"],
        "render": render_nafld,
        "has_article": False,
        "priority": 8
    },
    "chronic_constipation": {
        "keywords": ["Táo Bón", "Constipation", "táo bón", "constipation"],
        "render": render_chronic_constipation,
        "has_article": False,
        "priority": 8
    },
    "acute_diarrhea": {
        "keywords": ["Tiêu Chảy", "Diarrhea", "tiêu chảy", "diarrhea"],
        "render": render_acute_diarrhea,
        "has_article": False,
        "priority": 8
    },
    "lower_gi_bleeding": {
        "keywords": ["Xuất Huyết Tiêu Hóa Dưới", "Lower GI Bleeding", "lower gi bleeding", "xuất huyết tiêu hóa dưới"],
        "render": render_lower_gi_bleeding,
        "has_article": False,
        "priority": 9
    },
    "perforated_peptic_ulcer": {
        "keywords": ["Thủng Dạ Dày Tá Tràng", "Perforated Peptic Ulcer", "perforated peptic ulcer", "thủng dạ dày"],
        "render": render_perforated_peptic_ulcer,
        "has_article": False,
        "priority": 10
    },
    "biliary_obstruction": {
        "keywords": ["Tắc Mật", "Biliary Obstruction", "biliary obstruction", "tắc mật"],
        "render": render_biliary_obstruction,
        "has_article": False,
        "priority": 9
    },
    "decompensated_cirrhosis": {
        "keywords": ["Xơ Gan Mất Bù", "Decompensated Cirrhosis", "decompensated cirrhosis", "xơ gan mất bù"],
        "render": render_decompensated_cirrhosis,
        "has_article": False,
        "priority": 9
    },
    
    # Critical Care
    "delirium": {
        "keywords": ["Delirium", "delirium", "Quản lý Delirium"],
        "render": render_delirium,
        "has_article": False,
        "priority": 8
    },
    "sedation": {
        "keywords": ["Sedation", "sedation", "An thần", "Giảm đau ICU"],
        "render": render_sedation,
        "has_article": False,
        "priority": 8
    },
    "ards": {
        "keywords": ["ARDS", "ards"],
        "render": render_ards,
        "has_article": True,
        "article_function": "render_ards",
        "priority": 10
    },
    "ventilator_weaning": {
        "keywords": ["Ventilator Weaning", "weaning", "Cai Máy"],
        "render": render_ventilator_weaning,
        "has_article": False,
        "priority": 8
    },
    "stress_ulcer": {
        "keywords": ["Stress Ulcer", "stress ulcer", "SUP"],
        "render": render_stress_ulcer,
        "has_article": False,
        "priority": 8
    },
    "icp_management": {
        "keywords": ["Quản Lý Áp Lực Nội Sọ", "ICP Management", "icp management", "áp lực nội sọ"],
        "render": render_icp_management,
        "has_article": False,
        "priority": 10
    },
    "crrt": {
        "keywords": ["CRRT", "crrt", "Continuous Renal Replacement", "Lọc Máu Liên Tục"],
        "render": render_crrt,
        "has_article": False,
        "priority": 9
    },
    
    # Hematology
    "transfusion": {
        "keywords": ["Transfusion", "transfusion", "Truyền Máu"],
        "render": render_transfusion,
        "has_article": False,
        "priority": 8
    },
    "anticoagulation_reversal": {
        "keywords": ["Anticoagulation", "anticoagulation", "Đảo Ngược", "Chống Đông"],
        "render": render_anticoagulation_reversal,
        "has_article": False,
        "priority": 8
    },
    "itp": {
        "keywords": ["ITP", "itp", "Giảm Tiểu Cầu", "Immune Thrombocytopenic"],
        "render": render_itp,
        "has_article": False,
        "priority": 8
    },
    "ttp_hus": {
        "keywords": ["TTP", "HUS", "ttp", "hus", "Thrombotic Thrombocytopenic", "Hemolytic Uremic"],
        "render": render_ttp_hus,
        "has_article": False,
        "priority": 9
    },
    "dic": {
        "keywords": ["DIC", "dic", "Disseminated Intravascular", "Đông máu rải rác"],
        "render": render_dic,
        "has_article": False,
        "priority": 9
    },
    
    # Oncology
    "tls": {
        "keywords": ["Tumor Lysis", "TLS", "tls"],
        "render": render_tls,
        "has_article": False,
        "priority": 8
    },
    "febrile_neutropenia": {
        "keywords": ["Febrile Neutropenia", "neutropenia"],
        "render": render_febrile_neutropenia,
        "has_article": False,
        "priority": 8
    },
    "hypercalcemia": {
        "keywords": ["Hypercalcemia", "hypercalcemia"],
        "render": render_hypercalcemia,
        "has_article": False,
        "priority": 8
    },
    
    # Pain Management
    "acute_pain": {
        "keywords": ["Đau", "Pain", "pain"],
        "render": render_acute_pain,
        "has_article": False,
        "priority": 8
    },
    
    # Rheumatology
    "acute_gout": {
        "keywords": ["Gout", "gout"],
        "render": render_acute_gout,
        "has_article": True,
        "article_function": "render_acute_gout",
        "priority": 8
    },
    "ra_flare": {
        "keywords": ["RA Flare", "rheumatoid arthritis", "RA"],
        "render": render_ra_flare,
        "has_article": False,
        "priority": 8
    },
    "osteoarthritis": {
        "keywords": ["Osteoarthritis", "osteoarthritis", "Thoái Hóa", "thoái hóa"],
        "render": render_osteoarthritis,
        "has_article": False,
        "priority": 8
    },
    "ankylosing_spondylitis": {
        "keywords": ["Ankylosing Spondylitis", "ankylosing", "Dính Khớp", "dính khớp"],
        "render": render_ankylosing_spondylitis,
        "has_article": False,
        "priority": 8
    },
    "reactive_arthritis": {
        "keywords": ["Reactive Arthritis", "reactive arthritis", "Phản Ứng", "phản ứng"],
        "render": render_reactive_arthritis,
        "has_article": False,
        "priority": 8
    },
    "psoriatic_arthritis": {
        "keywords": ["Psoriatic Arthritis", "psoriatic", "Vảy Nến", "vảy nến"],
        "render": render_psoriatic_arthritis,
        "has_article": False,
        "priority": 8
    },
    "sle_arthritis": {
        "keywords": ["SLE Arthritis", "sle arthritis", "Lupus"],
        "require_all": False,
        "render": render_sle_arthritis,
        "has_article": False,
        "priority": 7
    },
    
    # Neurology
    "serotonin_syndrome": {
        "keywords": ["Serotonin", "serotonin"],
        "render": render_serotonin_syndrome,
        "has_article": False,
        "priority": 8
    },
    "neuroleptic_malignant_syndrome": {
        "keywords": ["Neuroleptic", "neuroleptic", "NMS", "ác tính do thuốc an thần"],
        "render": render_neuroleptic_malignant_syndrome,
        "has_article": False,
        "priority": 8
    },
    "intracranial_hypertension": {
        "keywords": ["Intracranial", "intracranial", "Tăng áp lực nội sọ"],
        "render": render_intracranial_hypertension,
        "has_article": False,
        "priority": 8
    },
    
    # Obstetrics
    "eclampsia": {
        "keywords": ["Eclampsia", "eclampsia", "Sản giật"],
        "render": render_eclampsia,
        "has_article": False,
        "priority": 8
    },
    "postpartum_hemorrhage": {
        "keywords": ["Postpartum", "postpartum", "Xuất huyết sau sinh"],
        "render": render_postpartum_hemorrhage,
        "has_article": False,
        "priority": 8
    },
    "preeclampsia": {
        "keywords": ["Tiền Sản Giật", "Preeclampsia", "preeclampsia", "tiền sản giật"],
        "render": render_preeclampsia,
        "has_article": False,
        "priority": 9
    },
    "hellp_syndrome": {
        "keywords": ["HELLP", "hellp", "HELLP Syndrome", "hellp syndrome"],
        "render": render_hellp_syndrome,
        "has_article": False,
        "priority": 10
    },
    "chorioamnionitis": {
        "keywords": ["Nhiễm Trùng Ối", "Chorioamnionitis", "chorioamnionitis", "nhiễm trùng ối"],
        "render": render_chorioamnionitis,
        "has_article": False,
        "priority": 10
    },
    "placental_abruption": {
        "keywords": ["Nhau Bong Non", "Placental Abruption", "placental abruption", "nhau bong non"],
        "render": render_placental_abruption,
        "has_article": False,
        "priority": 10
    },
    "uterine_rupture": {
        "keywords": ["Vỡ Tử Cung", "Uterine Rupture", "uterine rupture", "vỡ tử cung"],
        "render": render_uterine_rupture,
        "has_article": False,
        "priority": 10
    },
    
    # Dermatology
    "stevens_johnson": {
        "keywords": ["Stevens", "stevens", "SJS", "TEN"],
        "render": render_stevens_johnson_syndrome,
        "has_article": False,
        "priority": 8
    },
    "atopic_dermatitis": {
        "keywords": ["Viêm da cơ địa", "Atopic Dermatitis", "atopic dermatitis", "Eczema"],
        "render": render_atopic_dermatitis,
        "has_article": False,
        "priority": 8
    },
    "contact_dermatitis": {
        "keywords": ["Viêm da tiếp xúc", "Contact Dermatitis", "contact dermatitis"],
        "render": render_contact_dermatitis,
        "has_article": False,
        "priority": 8
    },
    "acne_vulgaris": {
        "keywords": ["Mụn trứng cá", "Acne", "acne", "Acne Vulgaris"],
        "render": render_acne_vulgaris,
        "has_article": False,
        "priority": 8
    },
    "fungal_infections": {
        "keywords": ["Nhiễm nấm da", "Fungal", "fungal", "Nấm da", "Lang ben"],
        "render": render_fungal_infections,
        "has_article": False,
        "priority": 8
    },
    "scabies": {
        "keywords": ["Ghẻ", "Scabies", "scabies"],
        "render": render_scabies,
        "has_article": False,
        "priority": 8
    },
    "urticaria": {
        "keywords": ["Mề đay", "Urticaria", "urticaria"],
        "render": render_urticaria,
        "has_article": False,
        "priority": 8
    },
    "psoriasis": {
        "keywords": ["Vảy nến", "Psoriasis", "psoriasis"],
        "render": render_psoriasis,
        "has_article": False,
        "priority": 8
    },
}


def match_protocol(protocol_name: str) -> Optional[Tuple[str, Dict]]:
    """
    Match protocol name to routing configuration.
    
    Args:
        protocol_name: The protocol name to match
        
    Returns:
        Tuple of (protocol_id, config) or None if not found
    """
    protocol_lower = protocol_name.lower()
    
    # Sort by priority (higher first)
    sorted_routes = sorted(
        PROTOCOL_ROUTING.items(),
        key=lambda x: x[1].get("priority", 0),
        reverse=True
    )
    
    for protocol_id, config in sorted_routes:
        keywords = config.get("keywords", [])
        exclude_keywords = config.get("exclude_keywords", [])
        require_all = config.get("require_all", False)
        
        # Check exclude keywords first
        if exclude_keywords:
            if any(excl.lower() in protocol_lower for excl in exclude_keywords):
                continue
        
        # Check include keywords
        if require_all:
            # All keywords must match
            if all(kw.lower() in protocol_lower for kw in keywords):
                return (protocol_id, config)
        else:
            # Any keyword matches
            if any(kw.lower() in protocol_lower or kw.lower() in protocol_name for kw in keywords):
                return (protocol_id, config)
    
    return None


def render_protocol_by_name(protocol_name: str, render_article_link_func: Callable, render_score_link_func: Callable = None):
    """
    Render protocol based on name using routing dictionary.
    
    Args:
        protocol_name: The protocol name to render
        render_article_link_func: Function to render article link
        render_score_link_func: Optional function to render score links
    """
    match_result = match_protocol(protocol_name)
    
    if match_result:
        protocol_id, config = match_result
        render_func = config.get("render")
        has_article = config.get("has_article", False)
        article_function = config.get("article_function")
        
        # Get protocol_function from config or extract from render function name
        protocol_function = config.get("protocol_function")
        if not protocol_function and render_func:
            # Extract function name from render function
            protocol_function = render_func.__name__ if hasattr(render_func, '__name__') else None
        
        # Render article link if exists
        if has_article and article_function:
            render_article_link_func(article_function)
        
        # Render protocol
        if render_func:
            render_func()
            
            # Render score links if function provided and protocol_function exists
            if render_score_link_func and protocol_function:
                render_score_link_func(protocol_function)
            
            return True
    
    return False

