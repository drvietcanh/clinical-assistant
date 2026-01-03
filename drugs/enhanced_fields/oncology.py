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

    # ======================== SESSION 2: ADDITIONAL ONCOLOGY DRUGS ========================
    "Oxaliplatin": {
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": False,
            "organ_toxicity": {
                "neurologic": "High (cold-induced neuropathy - very common, characteristic, and peripheral neuropathy - cumulative)",
                "hematologic": "Moderate (myelosuppression - less than cisplatin)",
                "gastrointestinal": "Moderate (nausea, vomiting, diarrhea)",
                "allergic": "Low (allergic reactions - rare)"
            },
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": [
                "Cold-induced neuropathy - CRITICAL (numbness, tingling, electric shock sensation when touching cold - very common, characteristic, avoid cold for 3-7 days after infusion)",
                "Peripheral neuropathy (numbness, tingling, loss of sensation) - CRITICAL (cumulative)",
                "CBC (myelosuppression) - CRITICAL (before each cycle, less than cisplatin)",
                "Renal function (CrCl, BUN, creatinine) - CRITICAL (before each cycle, for dose adjustment)",
                "Hepatic function (ALT, AST) - CRITICAL (before each cycle)",
                "Signs of allergic reactions (rash, dyspnea) - CRITICAL (rare)",
                "Extravasation during infusion - CRITICAL",
                "Avoid cold exposure - CRITICAL (no cold drinks, no touching cold objects, wear warm clothes, gloves, socks for 3-7 days after infusion)"
            ],
            "look_alike_sound_alike": ["Oxaliplatin", "Eloxatin", "Cisplatin", "Carboplatin"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Cold-Induced Neuropathy (Avoid Cold for 3-7 Days After Infusion)",
            "FDA Black Box Warning - Peripheral Neuropathy (Cumulative)",
            "FDA Drug Label - Oxaliplatin (Eloxatin)",
            "NCCN Guidelines - Colorectal Cancer Treatment (FOLFOX Protocol)",
            "ASCO Guidelines - Chemotherapy Toxicity Management"
        ]
    },

    "Vincristine": {
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": True,
            "icu_critical_care_only": False,
            "bleeding_risk": False,
            "organ_toxicity": {
                "neurologic": "High (peripheral neuropathy - very common, cumulative, can be irreversible, Black Box Warning)",
                "gastrointestinal": "High (constipation - very common, can be severe, ileus, Black Box Warning)",
                "autonomic": "Moderate (autonomic neuropathy - hypotension, urinary retention, very common)",
                "metabolic": "Low (SIADH - hyponatremia, rare)",
                "hematologic": "Low (myelosuppression - less than other agents)"
            },
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": [
                "Peripheral neuropathy (numbness, tingling, weakness) - CRITICAL (very common, cumulative, can be irreversible, Black Box Warning)",
                "Constipation - CRITICAL (very common, can be severe, ileus, Black Box Warning, prophylactic laxatives recommended)",
                "Autonomic neuropathy (hypotension, urinary retention) - CRITICAL (very common)",
                "CBC (myelosuppression) - CRITICAL (less than other agents, but still monitor)",
                "Hepatic function (ALT, AST) - CRITICAL (metabolized via CYP3A4)",
                "Sodium levels - CRITICAL (SIADH - rare)",
                "Signs of seizures - CRITICAL (rare)",
                "Drug interactions (L-asparaginase - use vincristine before, azole antifungals - increase neurotoxicity, CYP3A4 inhibitors/inducers) - CRITICAL",
                "INTRATHECAL ADMINISTRATION - CRITICAL (FATAL - NEVER administer intrathecally, Black Box Warning)"
            ],
            "look_alike_sound_alike": ["Vincristine", "Oncovin", "Vinblastine", "Vindesine"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Intrathecal Administration (FATAL - Never Administer Intrathecally)",
            "FDA Black Box Warning - Peripheral Neuropathy (Very Common, Cumulative, Can Be Irreversible)",
            "FDA Black Box Warning - Constipation (Very Common, Can Be Severe, Ileus)",
            "FDA Drug Label - Vincristine (Oncovin)",
            "NCCN Guidelines - Cancer Treatment",
            "ASCO Guidelines - Chemotherapy Toxicity Management",
            "ISMP High Alert Medications - Vincristine (Intrathecal Error Prevention)"
        ]
    },

    "Etoposide": {
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": False,
            "organ_toxicity": {
                "hematologic": "High (myelosuppression - very common and severe, dose-limiting, Black Box Warning)",
                "oncologic": "Moderate (secondary malignancies - AML, rare but serious, with high doses, Black Box Warning)",
                "hepatic": "Low (hepatotoxicity - elevated transaminases, rare)",
                "allergic": "Low (hypersensitivity reactions - rare)"
            },
            "qt_prolongation": False,
            "hepatotoxicity": True,
            "nephrotoxicity": False,
            "requires_monitoring": [
                "CBC (myelosuppression) - CRITICAL (very common and severe, dose-limiting, Black Box Warning, before and between cycles)",
                "Signs of infection (fever, chills) - CRITICAL (due to neutropenia)",
                "Signs of bleeding - CRITICAL (due to thrombocytopenia)",
                "Hepatic function (ALT, AST, bilirubin) - CRITICAL (before and during treatment, rare)",
                "Signs of hypersensitivity reactions - CRITICAL (rare)",
                "Signs of secondary malignancies (AML) - CRITICAL (rare but serious, with high doses, Black Box Warning)",
                "Drug interactions (cisplatin - increases myelosuppression, warfarin - increases bleeding risk, CYP3A4 inhibitors/inducers) - CRITICAL",
                "Renal function (CrCl) - CRITICAL (for dose adjustment, reduce dose 25-50% if CrCl <30-60)"
            ],
            "look_alike_sound_alike": ["Etoposide", "VP-16", "Etopophos", "Teniposide"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Myelosuppression (Very Common and Severe, Dose-Limiting)",
            "FDA Black Box Warning - Secondary Malignancies (AML, Rare But Serious, With High Doses)",
            "FDA Drug Label - Etoposide (VP-16, Etopophos)",
            "NCCN Guidelines - Small Cell Lung Cancer, Testicular Cancer",
            "ASCO Guidelines - Chemotherapy Toxicity Management"
        ]
    },

    "Irinotecan": {
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": False,
            "organ_toxicity": {
                "gastrointestinal": "High (diarrhea - very common, can be severe and dangerous, early cholinergic and late toxicity, Black Box Warning)",
                "hematologic": "High (myelosuppression - very common)",
                "autonomic": "Moderate (cholinergic syndrome - sweating, rhinorrhea, salivation, early, very common)",
                "hepatic": "Low (hepatotoxicity - elevated transaminases, rare)"
            },
            "qt_prolongation": False,
            "hepatotoxicity": True,
            "nephrotoxicity": False,
            "requires_monitoring": [
                "Diarrhea - CRITICAL (very common, can be severe and dangerous, early cholinergic and late toxicity, Black Box Warning, treat early with loperamide or atropine)",
                "Cholinergic syndrome (sweating, rhinorrhea, salivation) - CRITICAL (early, very common, treat with atropine)",
                "Premedication with atropine - CRITICAL (to reduce cholinergic syndrome)",
                "CBC (myelosuppression) - CRITICAL (very common, before each cycle)",
                "Signs of infection (fever, chills) - CRITICAL (due to neutropenia)",
                "Signs of bleeding - CRITICAL (due to thrombocytopenia)",
                "Hepatic function (ALT, AST, bilirubin) - CRITICAL (before and during treatment, rare)",
                "UGT1A1 genotype - CRITICAL (UGT1A1*28 polymorphism increases toxicity, consider dose reduction)",
                "Drug interactions (5-FU - increases myelosuppression and diarrhea) - CRITICAL"
            ],
            "look_alike_sound_alike": ["Irinotecan", "Camptosar", "CPT-11", "Topotecan"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Diarrhea (Very Common, Can Be Severe and Dangerous, Early and Late)",
            "FDA Black Box Warning - Cholinergic Syndrome (Requires Atropine Premedication)",
            "FDA Drug Label - Irinotecan (Camptosar)",
            "NCCN Guidelines - Colorectal Cancer Treatment (FOLFIRI Protocol)",
            "ASCO Guidelines - Chemotherapy Toxicity Management"
        ]
    },

    "5-Fluorouracil": {
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": True,
            "icu_critical_care_only": False,
            "bleeding_risk": False,
            "organ_toxicity": {
                "gastrointestinal": "High (stomatitis, diarrhea - very common, can be severe, Black Box Warning)",
                "hematologic": "High (myelosuppression - very common, Black Box Warning)",
                "metabolic": "High (DPD deficiency - can cause severe toxicity and death, Black Box Warning)",
                "cardiac": "Low (cardiotoxicity - rare but dangerous)",
                "neurologic": "Low (neurotoxicity - rare)"
            },
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": [
                "DPD (dihydropyrimidine dehydrogenase) testing - CRITICAL (before treatment if possible, DPD deficiency can cause severe toxicity and death, Black Box Warning)",
                "CBC (myelosuppression) - CRITICAL (very common, Black Box Warning, before and between cycles)",
                "Signs of stomatitis (oral mucositis) - CRITICAL (very common, can be severe)",
                "Signs of diarrhea - CRITICAL (very common, can be severe, treat early)",
                "Signs of cardiotoxicity (chest pain, dyspnea, arrhythmias) - CRITICAL (rare but dangerous)",
                "Hepatic function (ALT, AST, bilirubin) - CRITICAL (before and during treatment)",
                "Signs of infection (fever, chills) - CRITICAL (due to neutropenia)",
                "Signs of bleeding - CRITICAL (due to thrombocytopenia)",
                "Drug interactions (leucovorin - increases efficacy and toxicity, methotrexate - increases toxicity, warfarin - increases bleeding risk) - CRITICAL",
                "Uridine triacetate (Vistogard) - CRITICAL (antidote for overdose due to DPD deficiency, use within 96 hours)"
            ],
            "look_alike_sound_alike": ["5-Fluorouracil", "5-FU", "Fluorouracil", "Capecitabine"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - DPD Deficiency (Can Cause Severe Toxicity and Death, Test Before Treatment)",
            "FDA Black Box Warning - Myelosuppression (Very Common)",
            "FDA Black Box Warning - Stomatitis and Diarrhea (Very Common, Can Be Severe)",
            "FDA Drug Label - 5-Fluorouracil",
            "NCCN Guidelines - Colorectal Cancer Treatment",
            "ASCO Guidelines - Chemotherapy Toxicity Management",
            "Uridine Triacetate (Vistogard) - Antidote for 5-FU Overdose"
        ]
    },

    "Gemcitabine": {
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": False,
            "organ_toxicity": {
                "hematologic": "Moderate (myelosuppression - very common)",
                "pulmonary": "Moderate (interstitial pneumonitis - rare but dangerous, can be fatal)",
                "hepatic": "Low (hepatotoxicity - elevated transaminases, rare)",
                "systemic": "Moderate (flu-like syndrome - fever, chills, very common)",
                "dermatologic": "Low (rash, pruritus, common)"
            },
            "qt_prolongation": False,
            "hepatotoxicity": True,
            "nephrotoxicity": False,
            "requires_monitoring": [
                "CBC (myelosuppression) - CRITICAL (very common, before each cycle)",
                "Interstitial pneumonitis (dyspnea, cough, fever) - CRITICAL (rare but dangerous, can be fatal)",
                "Flu-like syndrome (fever, chills) - CRITICAL (very common, usually self-limiting)",
                "Hepatic function (ALT, AST, bilirubin) - CRITICAL (before and during treatment, rare)",
                "Signs of infection (fever, chills) - CRITICAL (due to neutropenia, distinguish from flu-like syndrome)",
                "Signs of bleeding - CRITICAL (due to thrombocytopenia)",
                "Drug interactions (cisplatin - increases myelosuppression, warfarin - may increase anticoagulation) - CRITICAL"
            ],
            "look_alike_sound_alike": ["Gemcitabine", "Gemzar", "5-Fluorouracil", "Capecitabine"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Interstitial Pneumonitis (Rare But Dangerous, Can Be Fatal)",
            "FDA Drug Label - Gemcitabine (Gemzar)",
            "NCCN Guidelines - Pancreatic Cancer, NSCLC Treatment",
            "ASCO Guidelines - Chemotherapy Toxicity Management"
        ]
    },

    "Bevacizumab": {
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": True,
            "organ_toxicity": {
                "hemorrhagic": "High (bleeding - very common, can be severe and life-threatening, Black Box Warning)",
                "gastrointestinal": "High (GI perforation - rare but dangerous, can be fatal, Black Box Warning)",
                "wound_healing": "High (wound healing impairment - very common, Black Box Warning, contraindicated recent surgery within 28 days)",
                "cardiovascular": "High (arterial thrombosis - rare but dangerous, venous thrombosis - common, Black Box Warning)",
                "renal": "High (proteinuria - very common, can be severe, Black Box Warning)",
                "cardiovascular_hypertension": "High (hypertension - very common, Black Box Warning)",
                "neurologic": "Low (posterior reversible encephalopathy syndrome - PRES, rare but dangerous)"
            },
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": [
                "Bleeding - CRITICAL (very common, can be severe and life-threatening, Black Box Warning, stop immediately if severe bleeding)",
                "GI perforation (abdominal pain, vomiting, fever) - CRITICAL (rare but dangerous, can be fatal, Black Box Warning, stop immediately)",
                "Wound healing - CRITICAL (very common, Black Box Warning, contraindicated recent surgery within 28 days and open wounds)",
                "Blood pressure - CRITICAL (hypertension very common, Black Box Warning, monitor each cycle)",
                "Proteinuria - CRITICAL (very common, can be severe, Black Box Warning, monitor each cycle, stop if >3.5g/24h)",
                "Arterial thrombosis (chest pain, dyspnea, stroke symptoms) - CRITICAL (rare but dangerous, Black Box Warning)",
                "Venous thrombosis (leg swelling, pain) - CRITICAL (common)",
                "Cardiac function (heart failure) - CRITICAL (rare)",
                "PRES (headache, seizures, visual disturbances) - CRITICAL (rare but dangerous, stop immediately)",
                "Infusion-related reactions - CRITICAL (rare, monitor during first 30 minutes)"
            ],
            "look_alike_sound_alike": ["Bevacizumab", "Avastin", "Ramucirumab", "Aflibercept"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Bleeding (Very Common, Can Be Severe and Life-Threatening)",
            "FDA Black Box Warning - GI Perforation (Rare But Dangerous, Can Be Fatal)",
            "FDA Black Box Warning - Wound Healing Impairment (Contraindicated Recent Surgery Within 28 Days)",
            "FDA Black Box Warning - Arterial Thrombosis (Rare But Dangerous)",
            "FDA Black Box Warning - Hypertension (Very Common)",
            "FDA Black Box Warning - Proteinuria (Very Common, Can Be Severe)",
            "FDA Drug Label - Bevacizumab (Avastin)",
            "NCCN Guidelines - Colorectal Cancer, NSCLC, Renal Cell Carcinoma Treatment",
            "ASCO Guidelines - Targeted Therapy Toxicity Management"
        ]
    },

    "Abiraterone": {
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": False,
            "organ_toxicity": {
                "cardiac": "High (cardiotoxicity - heart failure, arrhythmias, very common and dangerous, Black Box Warning)",
                "metabolic": "High (hypokalemia - very common, can be severe, Black Box Warning)",
                "hepatic": "High (hepatotoxicity - elevated transaminases, very common, Black Box Warning, contraindicated in severe hepatic impairment)",
                "cardiovascular_hypertension": "High (hypertension - very common)",
                "fluid_retention": "High (fluid retention, edema - very common)"
            },
            "qt_prolongation": False,
            "hepatotoxicity": True,
            "nephrotoxicity": False,
            "requires_monitoring": [
                "Cardiac function (LVEF) - CRITICAL (before treatment and every 3 months, very common and dangerous, Black Box Warning)",
                "Potassium levels - CRITICAL (before treatment and every 2 weeks for first 3 months, very common, can be severe, Black Box Warning)",
                "Hepatic function (ALT, AST, bilirubin) - CRITICAL (before treatment and every 2 weeks for first 3 months, very common, Black Box Warning, contraindicated in severe hepatic impairment)",
                "Blood pressure - CRITICAL (hypertension very common, monitor each cycle)",
                "Fluid retention (edema, weight gain) - CRITICAL (very common)",
                "Prednisone use - CRITICAL (must be used concomitantly to reduce side effects, Black Box Warning)",
                "Food interactions - CRITICAL (must take on empty stomach, 1 hour before or 2 hours after meals, food increases absorption 10-fold)",
                "Drug interactions (CYP3A4 inhibitors/inducers) - CRITICAL"
            ],
            "look_alike_sound_alike": ["Abiraterone", "Zytiga", "Enzalutamide", "Apalutamide"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Cardiotoxicity (Very Common and Dangerous)",
            "FDA Black Box Warning - Hypokalemia (Very Common, Can Be Severe)",
            "FDA Black Box Warning - Hepatotoxicity (Very Common, Contraindicated in Severe Hepatic Impairment)",
            "FDA Black Box Warning - Must Use Concomitantly with Prednisone",
            "FDA Drug Label - Abiraterone (Zytiga)",
            "NCCN Guidelines - Prostate Cancer Treatment (Castration-Resistant)",
            "ASCO Guidelines - Hormone Therapy Toxicity Management"
        ]
    },
}

__all__ = ['ONCOLOGY_ENHANCED_FIELDS']

