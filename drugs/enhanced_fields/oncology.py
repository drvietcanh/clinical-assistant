"""Enhanced fields for Oncology drugs - Risk Flags and Guideline Tags"""

from typing import Dict, Any

# ======================== SESSION 1: PRIORITY ONCOLOGY DRUGS ========================
# Focus on drugs with Black Box Warnings and high toxicity profiles

ONCOLOGY_ENHANCED_FIELDS: Dict[str, Dict[str, Any]] = {
    "Cisplatin": {
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": True,
            "icu_critical_care_only": False,
            "bleeding_risk": False,
            "organ_toxicity": {
                "renal": "High (nephrotoxicity - most common and serious, Black Box Warning, requires hydration)",
                "neurologic": "High (peripheral neuropathy - can be permanent, cumulative)",
                "otologic": "High (ototoxicity - can be permanent, cumulative)",
                "hematologic": "High (myelosuppression - can be severe)",
                "gastrointestinal": "High (severe nausea and vomiting - very common)",
                "metabolic": "High (hypomagnesemia - very common, requires supplementation)",
                "cardiac": "Low (cardiotoxicity - rare)"
            },
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": True,
            "requires_monitoring": [
                "Renal function (CrCl, BUN, creatinine) - CRITICAL (before and after each cycle, Black Box Warning)",
                "Urine output during and after infusion - CRITICAL (ensure >100ml/hour)",
                "Hearing (audiometry) - CRITICAL (before and periodically, can be permanent)",
                "Peripheral neuropathy (numbness, tingling, weakness) - CRITICAL (can be permanent, cumulative)",
                "CBC (myelosuppression) - CRITICAL (before each cycle)",
                "Magnesium levels - CRITICAL (hypomagnesemia very common, requires supplementation)",
                "Signs of severe nausea and vomiting - CRITICAL (very common, need strong antiemetics)",
                "Pre-hydration and post-hydration - CRITICAL (1-2L NS before and after to reduce nephrotoxicity)",
                "ECG (if symptoms of cardiotoxicity - rare)"
            ],
            "look_alike_sound_alike": ["Cisplatin", "Platinol", "Carboplatin", "Oxaliplatin"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Nephrotoxicity (Requires Hydration)",
            "FDA Black Box Warning - Ototoxicity (Can Be Permanent)",
            "FDA Black Box Warning - Peripheral Neuropathy (Can Be Permanent)",
            "NCCN Guidelines - Cancer Treatment",
            "FDA Drug Label - Cisplatin (Platinol)",
            "ASCO Guidelines - Chemotherapy Toxicity Management"
        ]
    },

    "Carboplatin": {
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": True,
            "icu_critical_care_only": False,
            "bleeding_risk": False,
            "organ_toxicity": {
                "hematologic": "High (myelosuppression - dose-limiting toxicity, more than cisplatin)",
                "renal": "Moderate (nephrotoxicity - less than cisplatin, but still present)",
                "neurologic": "Low (peripheral neuropathy - less than cisplatin)",
                "otologic": "Low (ototoxicity - less than cisplatin)",
                "gastrointestinal": "Moderate (nausea and vomiting - less than cisplatin)"
            },
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": True,
            "requires_monitoring": [
                "CBC (myelosuppression) - CRITICAL (dose-limiting toxicity, more than cisplatin, before each cycle)",
                "Renal function (CrCl, BUN, creatinine) - CRITICAL (for dose calculation using Calvert formula, before each cycle)",
                "Platelet count - CRITICAL (thrombocytopenia is dose-limiting)",
                "ANC (absolute neutrophil count) - CRITICAL (neutropenia is dose-limiting)",
                "Signs of infection (fever, chills) - CRITICAL (due to neutropenia)",
                "Signs of bleeding - CRITICAL (due to thrombocytopenia)",
                "Peripheral neuropathy (numbness, tingling) - CRITICAL (less than cisplatin but still present)",
                "Hearing (audiometry) - CRITICAL (less than cisplatin but still present)"
            ],
            "look_alike_sound_alike": ["Carboplatin", "Paraplatin", "Cisplatin", "Oxaliplatin"]
        },
        "guideline_tags": [
            "FDA Drug Label - Carboplatin (Paraplatin)",
            "NCCN Guidelines - Cancer Treatment",
            "ASCO Guidelines - Chemotherapy Toxicity Management",
            "Calvert Formula - Carboplatin Dosing"
        ]
    },

    "Doxorubicin": {
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": True,
            "icu_critical_care_only": False,
            "bleeding_risk": False,
            "organ_toxicity": {
                "cardiac": "High (cardiotoxicity - heart failure, arrhythmias, cumulative, irreversible, Black Box Warning)",
                "hematologic": "High (myelosuppression - can be severe)",
                "dermatologic": "High (extravasation - can cause skin necrosis, Black Box Warning)",
                "gastrointestinal": "Moderate (nausea, vomiting, mucositis)",
                "reproductive": "High (infertility - can be permanent)"
            },
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": [
                "Cardiac function (echo, MUGA scan - EF) - CRITICAL (before each cycle, Black Box Warning)",
                "ECG - CRITICAL (before and during treatment)",
                "Cumulative dose - CRITICAL (max 450-550mg/m² to avoid cardiotoxicity, Black Box Warning)",
                "CBC (myelosuppression) - CRITICAL (before each cycle)",
                "Hepatic function (ALT, AST, bilirubin) - CRITICAL (before each cycle)",
                "Signs of heart failure (dyspnea, edema, fatigue) - CRITICAL (can occur late, after years)",
                "Extravasation during infusion - CRITICAL (red skin, pain - can cause necrosis, Black Box Warning)",
                "Urine color (red - normal, not blood)"
            ],
            "look_alike_sound_alike": ["Doxorubicin", "Adriamycin", "Daunorubicin", "Epirubicin"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Cardiotoxicity (Heart Failure, Cumulative Dose Limit 450-550mg/m²)",
            "FDA Black Box Warning - Extravasation (Can Cause Skin Necrosis)",
            "FDA Drug Label - Doxorubicin (Adriamycin)",
            "NCCN Guidelines - Cancer Treatment",
            "ASCO Guidelines - Cardiotoxicity Management",
            "ESMO Guidelines - Anthracycline Cardiotoxicity"
        ]
    },

    "Cyclophosphamide": {
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": True,
            "icu_critical_care_only": False,
            "bleeding_risk": False,
            "organ_toxicity": {
                "urologic": "High (hemorrhagic cystitis - very common and dangerous, Black Box Warning)",
                "hematologic": "High (myelosuppression - can be severe, Black Box Warning)",
                "reproductive": "High (infertility - can be permanent, Black Box Warning)",
                "oncologic": "Moderate (secondary malignancies - rare, Black Box Warning)",
                "cardiac": "Moderate (cardiotoxicity - with high doses)",
                "metabolic": "Moderate (tumor lysis syndrome - with high doses)"
            },
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": [
                "CBC (myelosuppression) - CRITICAL (before and after each cycle, Black Box Warning)",
                "Signs of hemorrhagic cystitis (hematuria, dysuria, frequency) - CRITICAL (very common and dangerous, Black Box Warning)",
                "Urine output - CRITICAL (ensure >2-3L/day to prevent hemorrhagic cystitis)",
                "Renal function (CrCl, BUN, creatinine) - CRITICAL (for dose adjustment)",
                "Hepatic function (ALT, AST) - CRITICAL (needs liver to metabolize to active form)",
                "Signs of infection (fever, chills) - CRITICAL (due to neutropenia)",
                "Signs of bleeding - CRITICAL (due to thrombocytopenia)",
                "Tumor lysis syndrome (uric acid, potassium, phosphate) - CRITICAL (with high doses)",
                "Signs of cardiotoxicity (tachycardia, heart failure) - CRITICAL (with high doses)",
                "Mesna use - CRITICAL (for high doses to protect bladder)"
            ],
            "look_alike_sound_alike": ["Cyclophosphamide", "Endoxan", "Cytoxan", "Ifosfamide"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Hemorrhagic Cystitis (Requires Hydration and Mesna)",
            "FDA Black Box Warning - Myelosuppression (Can Be Severe)",
            "FDA Black Box Warning - Infertility (Can Be Permanent)",
            "FDA Black Box Warning - Secondary Malignancies (Rare)",
            "FDA Drug Label - Cyclophosphamide (Cytoxan)",
            "NCCN Guidelines - Cancer Treatment",
            "ASCO Guidelines - Chemotherapy Toxicity Management"
        ]
    },

    "Docetaxel": {
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": False,
            "organ_toxicity": {
                "allergic": "High (hypersensitivity reactions - very common and dangerous, can be fatal, Black Box Warning)",
                "neurologic": "High (peripheral neuropathy - very common, cumulative, can be irreversible)",
                "hematologic": "High (myelosuppression - very common)",
                "fluid_retention": "High (fluid retention - very common, cumulative, can be severe, Black Box Warning)",
                "hepatic": "Moderate (hepatotoxicity - elevated transaminases, very common)",
                "dermatologic": "Moderate (rash, nail changes - very common)"
            },
            "qt_prolongation": False,
            "hepatotoxicity": True,
            "nephrotoxicity": False,
            "requires_monitoring": [
                "Hypersensitivity reactions - CRITICAL (monitor during first 30 minutes of infusion, very common and dangerous, Black Box Warning)",
                "Premedication with dexamethasone - CRITICAL (8mg PO BID x 3 days, starting 1 day before, to reduce hypersensitivity and fluid retention)",
                "CBC (myelosuppression) - CRITICAL (before each cycle, very common)",
                "Peripheral neuropathy (numbness, tingling, weakness) - CRITICAL (very common, cumulative, can be irreversible)",
                "Fluid retention (weight gain, peripheral edema, pleural effusion, ascites) - CRITICAL (very common, cumulative, can be severe, Black Box Warning)",
                "Hepatic function (ALT, AST) - CRITICAL (before and during treatment, very common)",
                "Signs of infection (fever, chills) - CRITICAL (due to neutropenia)",
                "Signs of bleeding - CRITICAL (due to thrombocytopenia)",
                "Drug interactions (CYP3A4 inhibitors/inducers, ketoconazole - CONTRAINDICATED) - CRITICAL",
                "Hepatic impairment - CRITICAL (CONTRAINDICATED in moderate/severe hepatic impairment)"
            ],
            "look_alike_sound_alike": ["Docetaxel", "Taxotere", "Paclitaxel", "Taxol"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Hypersensitivity Reactions (Very Common, Can Be Fatal, Requires Premedication)",
            "FDA Black Box Warning - Fluid Retention (Very Common, Cumulative, Can Be Severe)",
            "FDA Black Box Warning - Peripheral Neuropathy (Very Common, Cumulative, Can Be Irreversible)",
            "FDA Black Box Warning - Hepatic Impairment (Contraindicated in Moderate/Severe)",
            "FDA Drug Label - Docetaxel (Taxotere)",
            "NCCN Guidelines - Cancer Treatment",
            "ASCO Guidelines - Chemotherapy Toxicity Management"
        ]
    },

    "Paclitaxel": {
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": False,
            "organ_toxicity": {
                "allergic": "High (hypersensitivity reactions - very common and dangerous, can be fatal, Black Box Warning)",
                "neurologic": "High (peripheral neuropathy - very common, cumulative, can be irreversible)",
                "hematologic": "High (myelosuppression - very common)",
                "cardiac": "Low (cardiotoxicity - bradycardia, arrhythmias, rare but dangerous)",
                "hepatic": "Low (hepatotoxicity - elevated transaminases, rare)"
            },
            "qt_prolongation": False,
            "hepatotoxicity": True,
            "nephrotoxicity": False,
            "requires_monitoring": [
                "Hypersensitivity reactions - CRITICAL (monitor during first 30 minutes of infusion, very common and dangerous, Black Box Warning)",
                "Premedication with dexamethasone, diphenhydramine, H2 blocker - CRITICAL (to reduce hypersensitivity, Black Box Warning)",
                "CBC (myelosuppression) - CRITICAL (before each cycle, very common)",
                "Peripheral neuropathy (numbness, tingling, weakness) - CRITICAL (very common, cumulative, can be irreversible)",
                "Cardiac monitoring (ECG, heart rate) - CRITICAL (bradycardia, arrhythmias - rare but dangerous)",
                "Signs of infection (fever, chills) - CRITICAL (due to neutropenia)",
                "Signs of bleeding - CRITICAL (due to thrombocytopenia)",
                "Hepatic function (ALT, AST) - CRITICAL (before and during treatment, rare)",
                "Drug interactions (CYP2C8 inhibitors, cisplatin - use paclitaxel before cisplatin) - CRITICAL"
            ],
            "look_alike_sound_alike": ["Paclitaxel", "Taxol", "Docetaxel", "Taxotere"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Hypersensitivity Reactions (Very Common, Can Be Fatal, Requires Premedication)",
            "FDA Black Box Warning - Peripheral Neuropathy (Very Common, Cumulative, Can Be Irreversible)",
            "FDA Drug Label - Paclitaxel (Taxol)",
            "NCCN Guidelines - Cancer Treatment",
            "ASCO Guidelines - Chemotherapy Toxicity Management"
        ]
    },

    "Methotrexate": {
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": True,
            "icu_critical_care_only": False,
            "bleeding_risk": False,
            "organ_toxicity": {
                "hematologic": "High (myelosuppression - can be severe, Black Box Warning)",
                "hepatic": "High (hepatotoxicity - can be severe, especially with high doses or long-term use, Black Box Warning)",
                "renal": "High (nephrotoxicity - can be severe, especially with high doses, Black Box Warning)",
                "pulmonary": "High (pneumonitis - interstitial lung disease, can be fatal, Black Box Warning)",
                "neurologic": "High (neurotoxicity - especially with intrathecal administration, can be fatal, Black Box Warning)",
                "dermatologic": "Moderate (mucositis, skin reactions)",
                "gastrointestinal": "Moderate (nausea, vomiting, diarrhea)"
            },
            "qt_prolongation": False,
            "hepatotoxicity": True,
            "nephrotoxicity": True,
            "requires_monitoring": [
                "CBC (myelosuppression) - CRITICAL (before and after each cycle, Black Box Warning)",
                "Renal function (CrCl, BUN, creatinine) - CRITICAL (before and after each cycle, especially with high doses, Black Box Warning)",
                "Hepatic function (ALT, AST, bilirubin) - CRITICAL (before and periodically, especially with long-term use, Black Box Warning)",
                "Methotrexate levels - CRITICAL (with high doses, to guide leucovorin rescue)",
                "Leucovorin rescue - CRITICAL (with high doses, to prevent toxicity, Black Box Warning)",
                "Signs of pneumonitis (dyspnea, cough, fever) - CRITICAL (can be fatal, Black Box Warning)",
                "Signs of neurotoxicity (headache, confusion, seizures) - CRITICAL (especially with intrathecal administration, can be fatal, Black Box Warning)",
                "Urine pH - CRITICAL (maintain >7.0 with high doses to prevent nephrotoxicity)",
                "Hydration - CRITICAL (with high doses to prevent nephrotoxicity)",
                "Signs of infection (fever, chills) - CRITICAL (due to neutropenia)",
                "Signs of bleeding - CRITICAL (due to thrombocytopenia)"
            ],
            "look_alike_sound_alike": ["Methotrexate", "MTX", "Trexall", "Rheumatrex"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Myelosuppression (Can Be Severe)",
            "FDA Black Box Warning - Hepatotoxicity (Can Be Severe, Especially with High Doses or Long-Term Use)",
            "FDA Black Box Warning - Nephrotoxicity (Can Be Severe, Especially with High Doses)",
            "FDA Black Box Warning - Pneumonitis (Interstitial Lung Disease, Can Be Fatal)",
            "FDA Black Box Warning - Neurotoxicity (Especially with Intrathecal Administration, Can Be Fatal)",
            "FDA Black Box Warning - Leucovorin Rescue Required (With High Doses)",
            "FDA Drug Label - Methotrexate",
            "NCCN Guidelines - Cancer Treatment",
            "ASCO Guidelines - Chemotherapy Toxicity Management"
        ]
    },

    "Erlotinib": {
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": False,
            "organ_toxicity": {
                "pulmonary": "High (interstitial lung disease - ILD, rare but dangerous, can be fatal, Black Box Warning)",
                "dermatologic": "High (rash - very common 75-90%, acneiform rash, characteristic)",
                "hepatic": "Moderate (hepatotoxicity - elevated transaminases, common)",
                "gastrointestinal": "Moderate (diarrhea - common)",
                "hematologic": "Low (bleeding - rare)"
            },
            "qt_prolongation": False,
            "hepatotoxicity": True,
            "nephrotoxicity": False,
            "requires_monitoring": [
                "Interstitial lung disease (ILD) - CRITICAL (dyspnea, cough, fever - rare but dangerous, can be fatal, Black Box Warning)",
                "Rash (acneiform) - CRITICAL (very common 75-90%, characteristic, may indicate treatment response)",
                "Hepatic function (ALT, AST, bilirubin) - CRITICAL (before and monthly for first 3 months, common)",
                "Signs of diarrhea - CRITICAL (common)",
                "Signs of bleeding - CRITICAL (rare)",
                "INR - CRITICAL (if used with warfarin)",
                "Drug interactions (CYP3A4 inhibitors/inducers, CYP1A2 inhibitors, smoking) - CRITICAL",
                "Food interactions - CRITICAL (take 1 hour before or 2 hours after meals, food increases absorption and toxicity)"
            ],
            "look_alike_sound_alike": ["Erlotinib", "Tarceva", "Gefitinib", "Afatinib"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Interstitial Lung Disease (ILD, Rare But Dangerous, Can Be Fatal)",
            "FDA Drug Label - Erlotinib (Tarceva)",
            "NCCN Guidelines - NSCLC Treatment (EGFR Mutation Positive)",
            "ASCO Guidelines - Targeted Therapy Toxicity Management"
        ]
    },
}

__all__ = ['ONCOLOGY_ENHANCED_FIELDS']

