"""
Enhanced fields overrides - Diabetes
"""
from typing import Any, Dict


DIABETES_ENHANCED_FIELDS: Dict[str, Dict[str, Any]] = {
        # ======================== SESSION 1: BIGUANIDES & INSULINS ========================
        "Metformin": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"metabolic": "High (lactic acidosis - rare but serious)", "renal": "High (contraindicated if CrCl <30)"},
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": True,
                "requires_monitoring": [
                    "Renal function (creatinine, eGFR) - CRITICAL (every 3-6 months)",
                    "Lactate levels if symptoms of lactic acidosis (muscle pain, dyspnea, abdominal pain)",
                    "Vitamin B12 levels (every 1-2 years with long-term use)",
                    "HbA1c (every 3 months)",
                    "Blood glucose (fasting and postprandial)"
                ],
                "look_alike_sound_alike": ["Metformin", "Metformin XR", "Glucophage"]
            },
            "guideline_tags": [
                "ADA Standards of Medical Care in Diabetes",
                "AACE/ACE Comprehensive Diabetes Management Algorithm",
                "EASD/ADA Type 2 Diabetes Management Consensus",
                "UKPDS Study - Metformin Cardiovascular Benefits",
                "FDA Drug Safety Communication - Metformin and Contrast Media",
                "FDA Black Box Warning - Lactic Acidosis"
            ]
        },

        "Insulin": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": True,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {},
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Blood glucose - CRITICAL (before meals, 2 hours postprandial, bedtime)",
                    "HbA1c (every 3 months, target <7% or individualized)",
                    "Signs of hypoglycemia (tremor, sweating, tachycardia, hunger, confusion, seizures, coma) - CRITICAL",
                    "Signs of hyperglycemia (polydipsia, polyuria, fatigue, blurred vision)",
                    "Weight (insulin can cause weight gain)",
                    "Renal function (decreased insulin clearance in renal impairment)",
                    "Injection site (rotate sites to avoid lipodystrophy)"
                ],
                "look_alike_sound_alike": ["Insulin", "Insulin glargine", "Insulin lispro", "Insulin aspart", "Insulin detemir", "Insulin degludec"]
            },
            "guideline_tags": [
                "ADA Standards of Medical Care in Diabetes",
                "AACE/ACE Comprehensive Diabetes Management Algorithm",
                "EASD/ADA Type 2 Diabetes Management Consensus",
                "ADA Type 1 Diabetes Management Guidelines",
                "ADA Inpatient Glycemic Control Guidelines",
                "ISMP High Alert Medications - Insulin",
                "FDA Drug Label - Insulin (hypoglycemia warning)"
            ]
        },

        # ======================== SESSION 1: SULFONYLUREAS ========================
        "Glibenclamide": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {},
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Blood glucose - CRITICAL (hypoglycemia risk)",
                    "HbA1c (every 3 months)",
                    "Signs of hypoglycemia (tremor, sweating, tachycardia, hunger, confusion, seizures, coma) - CRITICAL",
                    "Renal function (CrCl, eGFR) - increased hypoglycemia risk in renal impairment",
                    "Hepatic function (ALT, AST) - increased hypoglycemia risk in hepatic impairment",
                    "Weight (sulfonylureas can cause weight gain)",
                    "Drug interactions (warfarin - increased INR, beta-blockers - mask hypoglycemia symptoms)"
                ],
                "look_alike_sound_alike": ["Glibenclamide", "Glyburide", "Daonil"]
            },
            "guideline_tags": [
                "ADA Standards of Medical Care in Diabetes",
                "AACE/ACE Comprehensive Diabetes Management Algorithm",
                "EASD/ADA Type 2 Diabetes Management Consensus",
                "FDA Drug Label - Glyburide (hypoglycemia warning)"
            ]
        },

        "Glipizide": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {},
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Blood glucose - CRITICAL (hypoglycemia risk)",
                    "HbA1c (every 3 months)",
                    "Signs of hypoglycemia (tremor, sweating, tachycardia, hunger, confusion, seizures, coma) - CRITICAL",
                    "Renal function (CrCl, eGFR) - increased hypoglycemia risk in renal impairment",
                    "Hepatic function (ALT, AST) - increased hypoglycemia risk in hepatic impairment",
                    "Weight (sulfonylureas can cause weight gain)"
                ],
                "look_alike_sound_alike": ["Glipizide", "Glipizide XL", "Glibenclamide"]
            },
            "guideline_tags": [
                "ADA Standards of Medical Care in Diabetes",
                "AACE/ACE Comprehensive Diabetes Management Algorithm",
                "EASD/ADA Type 2 Diabetes Management Consensus",
                "FDA Drug Label - Glipizide (hypoglycemia warning)"
            ]
        },

        "Glimepiride": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {},
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Blood glucose - CRITICAL (hypoglycemia risk)",
                    "HbA1c (every 3 months)",
                    "Signs of hypoglycemia (tremor, sweating, tachycardia, hunger, confusion, seizures, coma) - CRITICAL",
                    "Renal function (CrCl, eGFR) - increased hypoglycemia risk in renal impairment",
                    "Hepatic function (ALT, AST) - increased hypoglycemia risk in hepatic impairment",
                    "Weight (sulfonylureas can cause weight gain)"
                ],
                "look_alike_sound_alike": ["Glimepiride", "Amaryl", "Glibenclamide"]
            },
            "guideline_tags": [
                "ADA Standards of Medical Care in Diabetes",
                "AACE/ACE Comprehensive Diabetes Management Algorithm",
                "EASD/ADA Type 2 Diabetes Management Consensus",
                "FDA Drug Label - Glimepiride (hypoglycemia warning)"
            ]
        },

        # ======================== SESSION 1: SGLT2 INHIBITORS ========================
        "Empagliflozin": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"genitourinary": "Moderate (genital mycotic infections, UTI)", "metabolic": "Moderate (euglycemic DKA risk)"},
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Blood glucose (HbA1c, glucose) - but hypoglycemia risk is low",
                    "Signs of euglycemic DKA (nausea, vomiting, abdominal pain, dyspnea) - CRITICAL (can occur with normal glucose)",
                    "Genital mycotic infections (especially in women)",
                    "Urinary tract infections",
                    "Volume status (dehydration, hypotension risk, especially with diuretics)",
                    "Renal function (eGFR) - contraindicated if eGFR <20",
                    "Foot examination (increased risk of lower limb amputation in some studies)"
                ],
                "look_alike_sound_alike": ["Empagliflozin", "Canagliflozin", "Dapagliflozin"]
            },
            "guideline_tags": [
                "ADA Standards of Medical Care in Diabetes",
                "AACE/ACE Comprehensive Diabetes Management Algorithm",
                "EASD/ADA Type 2 Diabetes Management Consensus",
                "EMPA-REG OUTCOME Trial - Cardiovascular Benefits",
                "FDA Drug Label - Empagliflozin (euglycemic DKA warning)",
                "FDA Drug Safety Communication - SGLT2 Inhibitors and Euglycemic DKA"
            ]
        },

        "Canagliflozin": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"genitourinary": "Moderate (genital mycotic infections, UTI)", "metabolic": "Moderate (euglycemic DKA risk)", "lower_limb": "Moderate (increased risk of lower limb amputation)"},
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Blood glucose (HbA1c, glucose) - but hypoglycemia risk is low",
                    "Signs of euglycemic DKA (nausea, vomiting, abdominal pain, dyspnea) - CRITICAL (can occur with normal glucose)",
                    "Genital mycotic infections (especially in women)",
                    "Urinary tract infections",
                    "Volume status (dehydration, hypotension risk, especially with diuretics)",
                    "Renal function (eGFR) - contraindicated if eGFR <30",
                    "Foot examination - CRITICAL (increased risk of lower limb amputation)",
                    "Signs of lower limb infection or ulceration"
                ],
                "look_alike_sound_alike": ["Canagliflozin", "Empagliflozin", "Dapagliflozin"]
            },
            "guideline_tags": [
                "ADA Standards of Medical Care in Diabetes",
                "AACE/ACE Comprehensive Diabetes Management Algorithm",
                "EASD/ADA Type 2 Diabetes Management Consensus",
                "CANVAS Program - Cardiovascular Benefits",
                "FDA Black Box Warning - Lower Limb Amputation",
                "FDA Drug Label - Canagliflozin (euglycemic DKA and amputation warnings)"
            ]
        },

        "Dapagliflozin": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"genitourinary": "Moderate (genital mycotic infections, UTI)", "metabolic": "Moderate (euglycemic DKA risk)"},
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Blood glucose (HbA1c, glucose) - but hypoglycemia risk is low",
                    "Signs of euglycemic DKA (nausea, vomiting, abdominal pain, dyspnea) - CRITICAL (can occur with normal glucose)",
                    "Genital mycotic infections (especially in women)",
                    "Urinary tract infections",
                    "Volume status (dehydration, hypotension risk, especially with diuretics)",
                    "Renal function (eGFR) - contraindicated if eGFR <25",
                    "Foot examination (increased risk of lower limb amputation in some studies)"
                ],
                "look_alike_sound_alike": ["Dapagliflozin", "Empagliflozin", "Canagliflozin"]
            },
            "guideline_tags": [
                "ADA Standards of Medical Care in Diabetes",
                "AACE/ACE Comprehensive Diabetes Management Algorithm",
                "EASD/ADA Type 2 Diabetes Management Consensus",
                "DECLARE-TIMI 58 Trial - Cardiovascular Benefits",
                "FDA Drug Label - Dapagliflozin (euglycemic DKA warning)"
            ]
        },

        # ======================== SESSION 1: GLP-1 RECEPTOR AGONISTS ========================
        "Liraglutide": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"gastrointestinal": "High (nausea, vomiting, diarrhea - very common ~40%)", "pancreatic": "Moderate (acute pancreatitis risk)", "thyroid": "Moderate (medullary thyroid carcinoma risk - contraindicated)"},
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Blood glucose (HbA1c, glucose)",
                    "Signs of acute pancreatitis (severe abdominal pain, nausea, vomiting) - CRITICAL",
                    "Gastrointestinal symptoms (nausea, vomiting, diarrhea) - very common, usually improves over time",
                    "Thyroid examination (medullary thyroid carcinoma risk - contraindicated in personal/family history)",
                    "Weight (weight loss is expected effect)",
                    "Heart rate (slight increase possible)"
                ],
                "look_alike_sound_alike": ["Liraglutide", "Victoza", "Saxenda", "Semaglutide"]
            },
            "guideline_tags": [
                "ADA Standards of Medical Care in Diabetes",
                "AACE/ACE Comprehensive Diabetes Management Algorithm",
                "EASD/ADA Type 2 Diabetes Management Consensus",
                "LEADER Trial - Cardiovascular Benefits",
                "FDA Black Box Warning - Thyroid C-Cell Tumors (medullary thyroid carcinoma)",
                "FDA Drug Label - Liraglutide (pancreatitis and thyroid cancer warnings)"
            ]
        },

        "Semaglutide": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"gastrointestinal": "High (nausea, vomiting, diarrhea - very common ~40%)", "pancreatic": "Moderate (acute pancreatitis risk)", "thyroid": "Moderate (medullary thyroid carcinoma risk - contraindicated)"},
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Blood glucose (HbA1c, glucose)",
                    "Signs of acute pancreatitis (severe abdominal pain, nausea, vomiting) - CRITICAL",
                    "Gastrointestinal symptoms (nausea, vomiting, diarrhea) - very common, usually improves over time",
                    "Thyroid examination (medullary thyroid carcinoma risk - contraindicated in personal/family history)",
                    "Weight (weight loss is expected effect)",
                    "Heart rate (slight increase possible)"
                ],
                "look_alike_sound_alike": ["Semaglutide", "Ozempic", "Wegovy", "Rybelsus", "Liraglutide"]
            },
            "guideline_tags": [
                "ADA Standards of Medical Care in Diabetes",
                "AACE/ACE Comprehensive Diabetes Management Algorithm",
                "EASD/ADA Type 2 Diabetes Management Consensus",
                "SUSTAIN-6 Trial - Cardiovascular Benefits",
                "FDA Black Box Warning - Thyroid C-Cell Tumors (medullary thyroid carcinoma)",
                "FDA Drug Label - Semaglutide (pancreatitis and thyroid cancer warnings)"
            ]
        },

}

__all__ = ["DIABETES_ENHANCED_FIELDS"]

