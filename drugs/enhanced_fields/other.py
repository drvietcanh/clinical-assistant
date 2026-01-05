"""
Enhanced fields overrides - Other
"""
from typing import Any, Dict


OTHER_ENHANCED_FIELDS: Dict[str, Dict[str, Any]] = {
        "5-Fluorouracil": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "look_alike_sound_alike": [],
                "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
                "requires_double_check": True,
                "icu_critical_care_only": False,
            },
        },

        "Adenosine": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": True,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "cardiac": "High (AV block - can be severe, bradycardia - can be severe, Black Box Warning)",
                    "respiratory": "Moderate (bronchospasm - can be severe in asthma/COPD, Black Box Warning)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "ECG - CRITICAL (continuous monitoring, AV block can be severe, Black Box Warning)",
                    "Heart rate - CRITICAL (bradycardia can be severe, Black Box Warning)",
                    "Blood pressure - CRITICAL (hypotension can occur)",
                    "Respiratory rate and SpO2 - CRITICAL (bronchospasm can be severe in asthma/COPD, Black Box Warning)",
                    "Administration technique - CRITICAL (must inject IV bolus RAPIDLY in 1-2 seconds into large vein, then flush immediately with 10-20ml NS)",
                    "Drug interactions (dipyridamole - reduce dose 50-75%, theophylline/caffeine - may need higher dose) - CRITICAL",
                    "Half-life - CRITICAL (<10 seconds, very short, effects usually resolve within seconds to minutes)"
                ],
                "look_alike_sound_alike": ["Adenosine", "Adenocard", "Adenosine"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - AV Block (Can Be Severe)",
                "FDA Black Box Warning - Bradycardia (Can Be Severe)",
                "FDA Black Box Warning - Bronchospasm (Can Be Severe in Asthma/COPD)",
                "FDA Drug Label - Adenosine (Adenocard)",
                "ACC/AHA/ESC Guidelines - Supraventricular Tachycardia",
                "AHA ACLS Guidelines - SVT Management"
            ]
        },

        "Alteplase": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": True,
                "bleeding_risk": True,
                "organ_toxicity": {
                    "hematologic": "High (bleeding - very common, can be severe and life-threatening, intracranial hemorrhage can be fatal, Black Box Warning)",
                    "neurologic": "High (intracranial hemorrhage - can be fatal, Black Box Warning)",
                    "cardiovascular": "Low (reperfusion arrhythmias - rare)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Signs of bleeding (GI bleeding, intracranial hemorrhage, injection site bleeding) - CRITICAL (very common, can be severe and life-threatening, Black Box Warning)",
                    "Intracranial hemorrhage (headache, altered mental status, focal neurological deficits) - CRITICAL (can be fatal, Black Box Warning)",
                    "Blood pressure - CRITICAL (maintain <185/110 mmHg before and during infusion, Black Box Warning)",
                    "Neurological exam - CRITICAL (every 15 minutes during infusion, every hour for 6 hours after, then every 2 hours for 18 hours)",
                    "CBC (hemoglobin, hematocrit) - CRITICAL (if signs of bleeding)",
                    "Time from symptom onset - CRITICAL (must be within 3-4.5 hours for stroke, within 12 hours for MI, Black Box Warning)",
                    "Contraindications check - CRITICAL (intracranial hemorrhage, recent stroke, recent surgery, active bleeding, Black Box Warning)"
                ],
                "look_alike_sound_alike": ["Alteplase", "tPA", "Activase", "Tenecteplase", "Reteplase"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Bleeding (Very Common, Can Be Severe and Life-Threatening)",
                "FDA Black Box Warning - Intracranial Hemorrhage (Can Be Fatal)",
                "FDA Black Box Warning - Time Window (Must Be Within 3-4.5 Hours for Stroke)",
                "FDA Drug Label - Alteplase (Activase)",
                "AHA/ASA Guidelines - Acute Ischemic Stroke",
                "AHA/ACC Guidelines - ST-Elevation Myocardial Infarction (STEMI)",
                "ESC Guidelines - Acute Coronary Syndrome"
            ]
        },

        "Amikacin": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": True,
                "look_alike_sound_alike": [],
                "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
                "requires_double_check": False,
                "icu_critical_care_only": False,
            },
        },

        "Amiodarone": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": True,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "pulmonary": "High (interstitial pneumonitis - can be fatal, Black Box Warning)",
                    "hepatic": "High (hepatotoxicity - can be fatal, Black Box Warning)",
                    "cardiac": "High (arrhythmias - can be fatal, Black Box Warning, QT prolongation, torsades de pointes)",
                    "endocrine": "High (thyroid dysfunction - hyperthyroidism or hypothyroidism, very common)",
                    "ophthalmic": "Moderate (corneal deposits, cataracts, very common)",
                    "dermatologic": "Moderate (photosensitivity, blue-gray skin discoloration, very common)"
                },
                "qt_prolongation": True,
                "hepatotoxicity": True,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Pulmonary function (chest X-ray, PFT) - CRITICAL (every 6 months, interstitial pneumonitis can be fatal, Black Box Warning)",
                    "Hepatic function (ALT, AST, bilirubin) - CRITICAL (every 3-6 months, hepatotoxicity can be fatal, Black Box Warning)",
                    "ECG (QT interval) - CRITICAL (QT prolongation is normal but QTc >500ms or increase >60ms is dangerous, Black Box Warning)",
                    "Thyroid function (TSH, FT4, FT3) - CRITICAL (every 6 months, hyperthyroidism or hypothyroidism very common)",
                    "Ophthalmologic exam - CRITICAL (every 6-12 months, corneal deposits, cataracts very common)",
                    "Electrolytes (K+, Mg2+) - CRITICAL (must be normal before use, hypokalemia/hypomagnesemia increase torsades risk)",
                    "Drug interactions (digoxin - reduce dose 50%, warfarin - reduce dose 30-50%, statins - reduce dose 50%, QT-prolonging drugs - CONTRAINDICATED) - CRITICAL",
                    "Half-life - CRITICAL (50-60 days, very long, effects persist after discontinuation)"
                ],
                "look_alike_sound_alike": ["Amiodarone", "Cordarone", "Dronedarone", "Sotalol"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Pulmonary Toxicity (Interstitial Pneumonitis, Can Be Fatal)",
                "FDA Black Box Warning - Hepatotoxicity (Can Be Fatal)",
                "FDA Black Box Warning - Arrhythmias (Can Be Fatal, QT Prolongation)",
                "FDA Black Box Warning - Only for Life-Threatening Arrhythmias",
                "FDA Drug Label - Amiodarone (Cordarone)",
                "ACC/AHA Guidelines - Arrhythmias",
                "ESC Guidelines - Arrhythmias"
            ]
        },

        "Apixaban": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": True,
                "organ_toxicity": {
                    "hematologic": "High (bleeding - very common, can be severe and life-threatening, Black Box Warning)",
                    "hepatic": "Low (hepatotoxicity - elevated transaminases, rare)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": True,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Signs of bleeding (GI bleeding, intracranial hemorrhage, post-surgical bleeding) - CRITICAL (very common, can be severe and life-threatening, Black Box Warning)",
                    "Creatinine - CRITICAL (for dose adjustment, reduce dose if ≥2 factors: age ≥80, weight ≤60kg, Cr ≥1.5mg/dL)",
                    "Hepatic function (ALT, AST) - CRITICAL (rare hepatotoxicity)",
                    "Drug interactions (CYP3A4/P-gp inhibitors/inducers - CONTRAINDICATED/AVOID strong inhibitors) - CRITICAL",
                    "Hepatic impairment - CRITICAL (contraindicated in Child-Pugh C)",
                    "Andexanet alfa availability - CRITICAL (antidote for bleeding, if available)"
                ],
                "look_alike_sound_alike": ["Apixaban", "Eliquis", "Rivaroxaban", "Edoxaban", "Dabigatran"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Bleeding (Very Common, Can Be Severe and Life-Threatening)",
                "FDA Black Box Warning - No Specific Antidote (Before Andexanet Alfa)",
                "FDA Drug Label - Apixaban (Eliquis)",
                "AHA/ACC/HRS Guidelines - Atrial Fibrillation Stroke Prevention",
                "CHEST Guidelines - VTE Treatment and Prophylaxis",
                "ESC Guidelines - Atrial Fibrillation"
            ]
        },

        "Aspirin": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "look_alike_sound_alike": [],
                "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
                "requires_double_check": True,
                "icu_critical_care_only": False,
            },
        },

        "Azathioprine": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": True,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "hematologic": "High (myelosuppression - very common, can be severe, Black Box Warning)",
                    "hepatic": "High (hepatotoxicity - can be severe, Black Box Warning)",
                    "oncologic": "Moderate (increased risk of malignancies - lymphoma, skin cancer, Black Box Warning)",
                    "gastrointestinal": "Moderate (pancreatitis - rare but serious)",
                    "infectious": "High (increased risk of serious infections - Black Box Warning)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": True,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "TPMT (thiopurine methyltransferase) genotype - CRITICAL (before treatment, TPMT deficiency increases toxicity, Black Box Warning)",
                    "CBC (myelosuppression) - CRITICAL (very common, can be severe, Black Box Warning, weekly for first month, then monthly)",
                    "Hepatic function (ALT, AST, bilirubin) - CRITICAL (hepatotoxicity can be severe, Black Box Warning)",
                    "Signs of pancreatitis (severe abdominal pain, nausea, vomiting) - CRITICAL (rare but serious)",
                    "Signs of infection (fever, chills) - CRITICAL (increased risk of serious infections, Black Box Warning)",
                    "Signs of malignancies (lymphoma, skin cancer) - CRITICAL (increased risk, Black Box Warning)",
                    "Drug interactions (allopurinol - CONTRAINDICATED, increases toxicity, Black Box Warning)",
                    "Dose reduction - CRITICAL (reduce dose 50-75% if TPMT deficiency or with allopurinol)"
                ],
                "look_alike_sound_alike": ["Azathioprine", "Imuran", "Mercaptopurine", "Cyclophosphamide"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Myelosuppression (Very Common, Can Be Severe)",
                "FDA Black Box Warning - Hepatotoxicity (Can Be Severe)",
                "FDA Black Box Warning - Increased Risk of Malignancies (Lymphoma, Skin Cancer)",
                "FDA Black Box Warning - Increased Risk of Serious Infections",
                "FDA Black Box Warning - TPMT Testing Required (Before Treatment)",
                "FDA Black Box Warning - Allopurinol Interaction (Contraindicated)",
                "FDA Drug Label - Azathioprine (Imuran)",
                "ACR Guidelines - Rheumatoid Arthritis",
                "KDIGO Guidelines - Kidney Disease"
            ]
        },

        "Carbamazepine": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": True,
                "look_alike_sound_alike": [],
                "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
                "requires_double_check": False,
                "icu_critical_care_only": False,
            },
        },

        "Carboplatin": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "look_alike_sound_alike": [],
                "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
                "requires_double_check": True,
                "icu_critical_care_only": False,
            },
        },

        "Cisplatin": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "look_alike_sound_alike": [],
                "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
                "requires_double_check": True,
                "icu_critical_care_only": False,
            },
        },

        "Clopidogrel": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": True,
                "organ_toxicity": {
                    "hematologic": "High (bleeding - very common, can be severe and life-threatening, Black Box Warning)",
                    "hematologic_ttp": "Low (thrombotic thrombocytopenic purpura - TTP, rare but dangerous)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Signs of bleeding (epistaxis, gingival bleeding, melena, hematemesis, injection site bleeding) - CRITICAL (very common, can be severe and life-threatening, Black Box Warning)",
                    "Major bleeding (GI bleeding, intracranial hemorrhage, post-surgical bleeding) - CRITICAL (Black Box Warning)",
                    "Thrombotic thrombocytopenic purpura (TTP) - CRITICAL (fever, anemia, thrombocytopenia, neurological symptoms - rare but dangerous)",
                    "Platelet count - CRITICAL (if signs of bleeding or TTP)",
                    "CYP2C19 genotype - CRITICAL (poor metabolizers may have reduced response, consider prasugrel or ticagrelor)",
                    "Drug interactions (PPIs - omeprazole/esomeprazole may reduce efficacy, warfarin - increases bleeding risk) - CRITICAL"
                ],
                "look_alike_sound_alike": ["Clopidogrel", "Plavix", "Prasugrel", "Ticagrelor"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Bleeding (Very Common, Can Be Severe and Life-Threatening)",
                "FDA Black Box Warning - CYP2C19 Poor Metabolizers (May Have Reduced Response)",
                "FDA Drug Label - Clopidogrel (Plavix)",
                "ACC/AHA Guidelines - Acute Coronary Syndrome",
                "ACC/AHA Guidelines - Dual Antiplatelet Therapy (DAPT)",
                "ESC Guidelines - Cardiovascular Disease Prevention"
            ]
        },

        "Codeine": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "look_alike_sound_alike": [],
                "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
                "requires_double_check": True,
                "icu_critical_care_only": False,
            },
        },

        "Cyclophosphamide": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "look_alike_sound_alike": [],
                "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
                "requires_double_check": True,
                "icu_critical_care_only": False,
            },
        },

        "Cyclosporine": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": True,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "renal": "High (nephrotoxicity - very common, dose-dependent, can be severe, Black Box Warning)",
                    "cardiovascular": "High (hypertension - very common, Black Box Warning)",
                    "metabolic": "High (hyperlipidemia - very common)",
                    "dermatologic": "Moderate (gingival hyperplasia, hirsutism - very common)",
                    "hepatic": "Low (hepatotoxicity - rare)",
                    "oncologic": "Moderate (increased risk of malignancies - lymphoma, skin cancer, Black Box Warning)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": True,
                "nephrotoxicity": True,
                "requires_monitoring": [
                    "Cyclosporine trough levels - CRITICAL (narrow therapeutic index, TDM required, target varies by indication, Black Box Warning)",
                    "Renal function (CrCl, BUN, creatinine) - CRITICAL (nephrotoxicity very common, dose-dependent, Black Box Warning)",
                    "Blood pressure - CRITICAL (hypertension very common, Black Box Warning)",
                    "Lipid profile (cholesterol, triglycerides) - CRITICAL (hyperlipidemia very common)",
                    "Hepatic function (ALT, AST, bilirubin) - CRITICAL (rare hepatotoxicity)",
                    "Signs of gingival hyperplasia - CRITICAL (very common)",
                    "Signs of hirsutism - CRITICAL (very common)",
                    "Signs of malignancies (lymphoma, skin cancer) - CRITICAL (increased risk, Black Box Warning)",
                    "Drug interactions (CYP3A4 inhibitors/inducers - CRITICAL, grapefruit juice - increases levels, Black Box Warning)",
                    "Formulation - CRITICAL (Neoral modified and Sandimmune non-modified are NOT interchangeable)"
                ],
                "look_alike_sound_alike": ["Cyclosporine", "Neoral", "Sandimmune", "Tacrolimus", "Cyclophosphamide"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Nephrotoxicity (Very Common, Dose-Dependent)",
                "FDA Black Box Warning - Hypertension (Very Common)",
                "FDA Black Box Warning - Increased Risk of Malignancies (Lymphoma, Skin Cancer)",
                "FDA Black Box Warning - Neoral and Sandimmune NOT Interchangeable",
                "FDA Drug Label - Cyclosporine (Neoral, Sandimmune)",
                "KDIGO Guidelines - Kidney Transplant",
                "AST Guidelines - Organ Transplant"
            ]
        },

        "Dabigatran": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": True,
                "organ_toxicity": {
                    "hematologic": "High (bleeding - very common, can be severe and life-threatening, Black Box Warning)",
                    "gastrointestinal": "Moderate (GI bleeding - more common than other DOACs)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Signs of bleeding (GI bleeding - more common than other DOACs, intracranial hemorrhage, post-surgical bleeding) - CRITICAL (very common, can be severe and life-threatening, Black Box Warning)",
                    "Creatinine - CRITICAL (for dose adjustment, contraindicated if CrCl <30, reduce dose if CrCl 30-50)",
                    "Drug interactions (P-gp inhibitors/inducers - CONTRAINDICATED/AVOID strong inhibitors) - CRITICAL",
                    "Renal function - CRITICAL (contraindicated in CrCl <30, reduce dose in CrCl 30-50)",
                    "Idarucizumab availability - CRITICAL (antidote for bleeding, Praxbind)"
                ],
                "look_alike_sound_alike": ["Dabigatran", "Pradaxa", "Apixaban", "Rivaroxaban", "Edoxaban"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Bleeding (Very Common, Can Be Severe and Life-Threatening)",
                "FDA Black Box Warning - GI Bleeding (More Common Than Other DOACs)",
                "FDA Black Box Warning - Renal Impairment (Contraindicated in CrCl <30)",
                "FDA Drug Label - Dabigatran (Pradaxa)",
                "AHA/ACC/HRS Guidelines - Atrial Fibrillation Stroke Prevention",
                "CHEST Guidelines - VTE Treatment and Prophylaxis",
                "ESC Guidelines - Atrial Fibrillation",
                "Idarucizumab (Praxbind) - Antidote for Dabigatran"
            ]
        },

        "Digoxin": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": True,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "cardiac": "High (arrhythmias - can be fatal, AV block, Black Box Warning)",
                    "gastrointestinal": "Moderate (nausea, vomiting - common in toxicity)",
                    "neurologic": "Moderate (visual disturbances - yellow-green vision, confusion - common in toxicity)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Digoxin levels - CRITICAL (target 0.8-2.0 ng/mL, narrow therapeutic index, Black Box Warning)",
                    "ECG (arrhythmias, AV block) - CRITICAL (can be fatal, Black Box Warning)",
                    "Electrolytes (K+, Mg2+) - CRITICAL (hypokalemia/hypomagnesemia increase toxicity risk, Black Box Warning)",
                    "Renal function (CrCl, eGFR) - CRITICAL (digoxin eliminated renally, half-life increases from 36h to 4-6 days in renal failure)",
                    "Signs of toxicity (nausea, vomiting, visual disturbances - yellow-green vision, confusion, arrhythmias) - CRITICAL (can be fatal)",
                    "Drug interactions (amiodarone - reduce digoxin dose 50%, verapamil/diltiazem - reduce dose 25-50%, quinidine - reduce dose 50%, diuretics - maintain K+ >4.0 mEq/L) - CRITICAL",
                    "Digibind/digoxin immune fab availability - CRITICAL (antidote for severe toxicity)"
                ],
                "look_alike_sound_alike": ["Digoxin", "Lanoxin", "Digitoxin"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Arrhythmias (Can Be Fatal)",
                "FDA Black Box Warning - Narrow Therapeutic Index (TDM Required)",
                "FDA Black Box Warning - WPW with AF (Contraindicated)",
                "FDA Drug Label - Digoxin (Lanoxin)",
                "AHA/ACC/HFSA Guidelines - Heart Failure",
                "AHA/ACC Guidelines - Atrial Fibrillation",
                "ESC Guidelines - Heart Failure",
                "Digibind (Digoxin Immune Fab) - Antidote for Severe Toxicity"
            ]
        },

        "Dipyridamole": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": True,
                "organ_toxicity": {
                    "cardiovascular": "Moderate (vasodilation - can cause headache, hypotension, especially with IV form)",
                    "hematologic": "Low (bleeding - less common than other antiplatelets)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Signs of bleeding (epistaxis, gingival bleeding, melena) - CRITICAL (less common than other antiplatelets but can occur)",
                    "Headache - CRITICAL (very common, due to vasodilation, may decrease with time or dose reduction)",
                    "Blood pressure - CRITICAL (hypotension can occur, especially with IV form)",
                    "Heart rate - CRITICAL (tachycardia can occur due to vasodilation)",
                    "Drug interactions (aspirin - used together, warfarin - increases bleeding risk) - CRITICAL"
                ],
                "look_alike_sound_alike": ["Dipyridamole", "Persantine", "Dipyridamole"]
            },
            "guideline_tags": [
                "AHA/ASA Guidelines - Stroke Secondary Prevention",
                "ESC Guidelines - Antiplatelet Therapy (Secondary Prevention)",
                "FDA Drug Label - Dipyridamole (Persantine)"
            ]
        },

        "Dobutamine": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": True,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "cardiac": "High (arrhythmias - very common, tachycardia, can be serious, myocardial ischemia - especially in CAD)",
                    "cardiovascular": "Moderate (hypotension - can occur due to vasodilation, especially at higher doses)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "ECG - CRITICAL (continuous monitoring, arrhythmias very common, myocardial ischemia risk)",
                    "Heart rate - CRITICAL (tachycardia very common, can be serious)",
                    "Blood pressure - CRITICAL (hypotension can occur due to vasodilation, especially at higher doses)",
                    "Cardiac output and hemodynamics - CRITICAL (if available, monitor response to therapy)",
                    "Signs of myocardial ischemia (chest pain, ST changes) - CRITICAL (especially in CAD patients)",
                    "Arrhythmias (atrial fibrillation, ventricular arrhythmias) - CRITICAL (very common, can be serious)",
                    "Infusion site - CRITICAL (extravasation can cause tissue necrosis, use central line if possible)",
                    "Drug interactions (beta-blockers - may antagonize effects, MAOIs - may increase effects) - CRITICAL"
                ],
                "look_alike_sound_alike": ["Dobutamine", "Dobutrex", "Dopamine", "Dobutamine"]
            },
            "guideline_tags": [
                "AHA/ACC Guidelines - Heart Failure",
                "AHA/ACC Guidelines - Cardiogenic Shock",
                "SCCM Guidelines - Shock Management",
                "ESC Guidelines - Heart Failure",
                "FDA Drug Label - Dobutamine (Dobutrex)"
            ]
        },

        "Docetaxel": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "look_alike_sound_alike": [],
                "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
                "requires_double_check": True,
                "icu_critical_care_only": False,
            },
        },

        "Dopamine": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": True,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "cardiac": "High (arrhythmias, tachycardia - very common, especially at higher doses >10 mcg/kg/min)",
                    "peripheral": "High (peripheral ischemia, tissue necrosis - especially with extravasation)",
                    "renal": "Moderate (renal effects - low dose may improve, high dose may worsen)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Blood pressure - CRITICAL (continuous monitoring, dose-dependent effects)",
                    "ECG - CRITICAL (continuous monitoring, arrhythmias, tachycardia very common)",
                    "Heart rate - CRITICAL (tachycardia very common, especially at higher doses >10 mcg/kg/min)",
                    "Peripheral perfusion - CRITICAL (peripheral ischemia, tissue necrosis risk)",
                    "Extravasation - CRITICAL (can cause severe tissue necrosis, use central line)",
                    "Renal function (urine output, creatinine) - CRITICAL (dose-dependent effects)",
                    "Dose-dependent effects - CRITICAL (low dose <5 mcg/kg/min: renal, medium 5-10: cardiac, high >10: vasoconstriction)"
                ],
                "look_alike_sound_alike": ["Dopamine", "Dobutamine", "Dopamine", "Epinephrine"]
            },
            "guideline_tags": [
                "SSC Guidelines - Septic Shock Management (Not First-Line, Consider Norepinephrine)",
                "AHA ACLS Guidelines - Shock Management",
                "FDA Drug Label - Dopamine",
                "ISMP High Alert Medications"
            ]
        },

        "Doxorubicin": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "look_alike_sound_alike": [],
                "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
                "requires_double_check": True,
                "icu_critical_care_only": False,
            },
        },

        "Dronedarone": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": True,
                "look_alike_sound_alike": [],
                "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
                "requires_double_check": True,
                "icu_critical_care_only": False,
            },
        },

        "Edoxaban": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": True,
                "organ_toxicity": {
                    "hematologic": "High (bleeding - very common, can be severe and life-threatening, Black Box Warning)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Signs of bleeding (GI bleeding, intracranial hemorrhage, post-surgical bleeding) - CRITICAL (very common, can be severe and life-threatening, Black Box Warning)",
                    "Creatinine - CRITICAL (for dose adjustment, contraindicated if CrCl >95, reduce dose if CrCl 50-95)",
                    "Drug interactions (P-gp inhibitors - reduce dose if used with verapamil, quinidine, dronedarone) - CRITICAL",
                    "Renal function - CRITICAL (contraindicated if CrCl >95, reduce dose in CrCl 50-95)"
                ],
                "look_alike_sound_alike": ["Edoxaban", "Savaysa", "Apixaban", "Rivaroxaban", "Dabigatran"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Bleeding (Very Common, Can Be Severe and Life-Threatening)",
                "FDA Black Box Warning - No Specific Antidote",
                "FDA Drug Label - Edoxaban (Savaysa)",
                "AHA/ACC/HRS Guidelines - Atrial Fibrillation Stroke Prevention",
                "CHEST Guidelines - VTE Treatment and Prophylaxis",
                "ESC Guidelines - Atrial Fibrillation"
            ]
        },

        "Enoxaparin": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": True,
                "organ_toxicity": {
                    "hematologic": "High (bleeding - very common, can be severe and life-threatening, Black Box Warning; heparin-induced thrombocytopenia - HIT - rare but serious, can cause thrombosis)",
                    "hepatic": "Low (elevated transaminases - rare)",
                    "metabolic": "Moderate (hyperkalemia - can occur, especially with prolonged use)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Anti-Xa levels - CRITICAL (for therapeutic dosing, target 0.5-1.0 IU/mL 4 hours after dose, Black Box Warning)",
                    "Platelet count - CRITICAL (before starting, then every 2-3 days for first 2 weeks, HIT risk, Black Box Warning)",
                    "Signs of heparin-induced thrombocytopenia (HIT) - CRITICAL (thrombocytopenia, new thrombosis - rare but serious, can cause thrombosis, Black Box Warning)",
                    "Signs of bleeding (GI bleeding, intracranial hemorrhage, injection site bleeding) - CRITICAL (very common, can be severe and life-threatening, Black Box Warning)",
                    "Renal function (creatinine, eGFR) - CRITICAL (dose adjustment needed if CrCl <30, accumulation risk)",
                    "Serum potassium - CRITICAL (hyperkalemia can occur, especially with prolonged use)",
                    "Protamine sulfate availability - CRITICAL (antidote for bleeding, 1mg protamine per 1mg enoxaparin, partial reversal)"
                ],
                "look_alike_sound_alike": ["Enoxaparin", "Lovenox", "Heparin", "Dalteparin", "Fondaparinux"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Bleeding (Very Common, Can Be Severe and Life-Threatening)",
                "FDA Black Box Warning - Heparin-Induced Thrombocytopenia (HIT - Rare but Serious, Can Cause Thrombosis)",
                "ISMP High Alert Medications",
                "FDA Drug Label - Enoxaparin (Lovenox)",
                "ACCP Guidelines - Antithrombotic Therapy",
                "CHEST Guidelines - VTE Treatment and Prophylaxis"
            ]
        },

        "Epinephrine": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "cardiac": "High (tachycardia, arrhythmias, hypertension, myocardial ischemia - can be fatal, especially with IV in cardiac patients)",
                    "cerebrovascular": "High (intracranial hemorrhage risk with high doses, especially in hypertensive patients)",
                    "metabolic": "High (hyperglycemia, lactic acidosis - especially with high doses)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "ECG - CRITICAL (continuous monitoring, tachycardia, arrhythmias, myocardial ischemia risk)",
                    "Blood pressure - CRITICAL (hypertension, can cause intracranial hemorrhage)",
                    "Heart rate - CRITICAL (tachycardia very common)",
                    "Signs of myocardial ischemia (chest pain, ST changes) - CRITICAL (especially in cardiac patients)",
                    "Blood glucose - CRITICAL (hyperglycemia, especially with high doses)",
                    "Lactate levels - CRITICAL (lactic acidosis risk with high doses)",
                    "Extravasation - CRITICAL (can cause tissue necrosis, use central line if possible)",
                    "Administration route - CRITICAL (IM for anaphylaxis, IV for cardiac arrest, subcutaneous for local effects)"
                ],
                "look_alike_sound_alike": ["Epinephrine", "Adrenalin", "Norepinephrine", "Phenylephrine"]
            },
            "guideline_tags": [
                "AHA ACLS Guidelines - Cardiac Arrest",
                "AHA ACLS Guidelines - Anaphylaxis",
                "FDA Drug Label - Epinephrine (Adrenalin)",
                "WHO Essential Medicines List",
                "ISMP High Alert Medications"
            ]
        },

        "Ethosuximide": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": True,
                "look_alike_sound_alike": [],
                "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
                "requires_double_check": False,
                "icu_critical_care_only": False,
            },
        },

        "Fentanyl": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "look_alike_sound_alike": [],
                "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
                "requires_double_check": True,
                "icu_critical_care_only": False,
            },
        },

        "Flecainide": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": True,
                "look_alike_sound_alike": [],
                "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
                "requires_double_check": True,
                "icu_critical_care_only": False,
            },
        },

        "Fondaparinux": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "look_alike_sound_alike": [],
                "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
                "requires_double_check": True,
                "icu_critical_care_only": False,
            },
        },

        "Gabapentin": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": True,
                "look_alike_sound_alike": [],
                "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
                "requires_double_check": False,
                "icu_critical_care_only": False,
            },
        },

        "Gemcitabine": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "look_alike_sound_alike": [],
                "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
                "requires_double_check": True,
                "icu_critical_care_only": False,
            },
        },

        "Gentamicin": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": True,
                "look_alike_sound_alike": [],
                "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
                "requires_double_check": False,
                "icu_critical_care_only": False,
            },
        },

        "Granisetron": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "look_alike_sound_alike": [],
                "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
                "requires_double_check": True,
                "icu_critical_care_only": False,
            },
        },

        "Heparin": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": True,
                "organ_toxicity": {
                    "hematologic": "High (bleeding - very common, can be severe and life-threatening, Black Box Warning; heparin-induced thrombocytopenia - HIT - rare but serious, can cause thrombosis)",
                    "hepatic": "Low (elevated transaminases - rare)",
                    "metabolic": "Moderate (hyperkalemia - can occur, especially with prolonged use)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "aPTT (activated partial thromboplastin time) - CRITICAL (for unfractionated heparin, target 1.5-2.5x control, Black Box Warning)",
                    "Anti-Xa levels - CRITICAL (alternative monitoring for unfractionated heparin, target 0.3-0.7 IU/mL)",
                    "Platelet count - CRITICAL (before starting, then every 2-3 days for first 2 weeks, HIT risk, Black Box Warning)",
                    "Signs of heparin-induced thrombocytopenia (HIT) - CRITICAL (thrombocytopenia, new thrombosis - rare but serious, can cause thrombosis, Black Box Warning)",
                    "Signs of bleeding (GI bleeding, intracranial hemorrhage, injection site bleeding) - CRITICAL (very common, can be severe and life-threatening, Black Box Warning)",
                    "Serum potassium - CRITICAL (hyperkalemia can occur, especially with prolonged use)",
                    "Protamine sulfate availability - CRITICAL (antidote for bleeding, 1mg protamine per 100 units heparin)",
                    "Hepatic function (ALT, AST) - CRITICAL (rare elevated transaminases)"
                ],
                "look_alike_sound_alike": ["Heparin", "Hep-Lock", "Enoxaparin", "Dalteparin", "Fondaparinux"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Bleeding (Very Common, Can Be Severe and Life-Threatening)",
                "FDA Black Box Warning - Heparin-Induced Thrombocytopenia (HIT - Rare but Serious, Can Cause Thrombosis)",
                "ISMP High Alert Medications",
                "FDA Drug Label - Heparin",
                "ACCP Guidelines - Antithrombotic Therapy",
                "CHEST Guidelines - VTE Treatment and Prophylaxis"
            ]
        },

        "Hydrocodone": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "look_alike_sound_alike": [],
                "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
                "requires_double_check": True,
                "icu_critical_care_only": False,
            },
        },

        "Hydromorphone": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "look_alike_sound_alike": [],
                "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
                "requires_double_check": True,
                "icu_critical_care_only": False,
            },
        },

        "Ifosfamide": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "look_alike_sound_alike": [],
                "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
                "requires_double_check": True,
                "icu_critical_care_only": False,
            },
        },

        "Insulin": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "look_alike_sound_alike": [],
                "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
                "requires_double_check": True,
                "icu_critical_care_only": False,
            },
        },

        "Irinotecan": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "look_alike_sound_alike": [],
                "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
                "requires_double_check": True,
                "icu_critical_care_only": False,
            },
        },

        "Lacosamide": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": True,
                "look_alike_sound_alike": [],
                "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
                "requires_double_check": False,
                "icu_critical_care_only": False,
            },
        },

        "Lamotrigine": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": True,
                "look_alike_sound_alike": [],
                "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
                "requires_double_check": False,
                "icu_critical_care_only": False,
            },
        },

        "Levetiracetam": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": True,
                "look_alike_sound_alike": [],
                "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
                "requires_double_check": False,
                "icu_critical_care_only": False,
            },
        },

        "Lidocaine": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": True,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "cardiac": "Moderate (arrhythmias - when used IV for arrhythmias, can cause bradycardia, AV block, asystole)",
                    "neurologic": "High (local anesthetic systemic toxicity - LAST - CNS toxicity: perioral numbness, metallic taste, tinnitus, seizures, coma - with high doses or IV injection)",
                    "hematologic": "Low (methemoglobinemia - rare, with prilocaine)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "ECG - CRITICAL (when used IV for arrhythmias, monitor for bradycardia, AV block, asystole)",
                    "Signs of LAST (local anesthetic systemic toxicity) - CRITICAL (CNS: perioral numbness, metallic taste, tinnitus, seizures, coma; Cardiac: hypotension, bradycardia, arrhythmias, cardiac arrest - with high doses or IV injection)",
                    "Blood pressure and heart rate - CRITICAL (cardiotoxicity can occur with high doses or IV injection)",
                    "Mental status - CRITICAL (CNS toxicity: seizures, coma with high doses)",
                    "Maximum dose - CRITICAL (4.5 mg/kg without epinephrine, 7 mg/kg with epinephrine, do NOT use epinephrine in fingers, toes, penis, nose, ears)",
                    "Lipid emulsion 20% (Intralipid) - CRITICAL (antidote for LAST, should be available when using high doses)",
                    "Injection site - CRITICAL (pain on injection, can cause thrombophlebitis)"
                ],
                "look_alike_sound_alike": ["Lidocaine", "Xylocaine", "Bupivacaine", "Ropivacaine"]
            },
            "guideline_tags": [
                "ASA Guidelines - Local Anesthetic Systemic Toxicity (LAST)",
                "AHA ACLS Guidelines - Antiarrhythmic Therapy",
                "FDA Drug Label - Lidocaine (Xylocaine)"
            ]
        },

        "Methotrexate": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": True,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "hepatic": "High (hepatotoxicity - can be severe and fatal, especially with long-term use, Black Box Warning)",
                    "hematologic": "High (myelosuppression - very common, can be severe and fatal, Black Box Warning)",
                    "pulmonary": "High (pneumonitis - can be fatal, Black Box Warning)",
                    "dermatologic": "High (severe skin reactions - SJS/TEN - rare but fatal, Black Box Warning)",
                    "gastrointestinal": "High (mucositis, GI ulceration - very common, can be severe)",
                    "renal": "Moderate (nephrotoxicity - can occur, especially with high doses)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": True,
                "nephrotoxicity": True,
                "requires_monitoring": [
                    "CBC (myelosuppression) - CRITICAL (very common, can be severe and fatal, Black Box Warning, weekly for first month, then monthly)",
                    "Hepatic function (ALT, AST, bilirubin) - CRITICAL (hepatotoxicity can be severe and fatal, especially with long-term use, Black Box Warning, every 4-8 weeks)",
                    "Pulmonary symptoms (cough, dyspnea, fever) - CRITICAL (pneumonitis can be fatal, Black Box Warning)",
                    "Chest X-ray or CT - CRITICAL (if signs of pneumonitis)",
                    "Signs of severe skin reactions (rash, fever, mucosal lesions) - CRITICAL (SJS/TEN - rare but fatal, Black Box Warning)",
                    "Renal function (creatinine, eGFR) - CRITICAL (nephrotoxicity can occur, especially with high doses)",
                    "Folic acid supplementation - CRITICAL (required to reduce toxicity, 1-5mg daily or weekly)",
                    "Drug interactions (NSAIDs, probenecid, penicillins - increase methotrexate levels, increase toxicity) - CRITICAL",
                    "Dose and frequency - CRITICAL (rheumatology: weekly dosing, oncology: different dosing, do NOT confuse)"
                ],
                "look_alike_sound_alike": ["Methotrexate", "MTX", "Methotrexate sodium", "Folic acid"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Hepatotoxicity (Can Be Severe and Fatal, Especially with Long-Term Use)",
                "FDA Black Box Warning - Myelosuppression (Very Common, Can Be Severe and Fatal)",
                "FDA Black Box Warning - Pneumonitis (Can Be Fatal)",
                "FDA Black Box Warning - Severe Skin Reactions (SJS/TEN - Rare but Fatal)",
                "ACR Guidelines - Rheumatoid Arthritis",
                "ACR Guidelines - Psoriatic Arthritis",
                "FDA Drug Label - Methotrexate"
            ]
        },

        "Morphine": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "look_alike_sound_alike": [],
                "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
                "requires_double_check": True,
                "icu_critical_care_only": False,
            },
        },

        "Mycophenolate": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "teratogenic": "High (teratogenicity - severe birth defects, REMS program, Black Box Warning)",
                    "hematologic": "High (myelosuppression - neutropenia, anemia, thrombocytopenia - very common, can be severe, Black Box Warning)",
                    "oncologic": "High (increased risk of infections and malignancies - lymphoma, skin cancer, Black Box Warning)",
                    "gastrointestinal": "High (severe diarrhea, nausea, vomiting - very common, dose-limiting)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Pregnancy test (REMS program) - CRITICAL (before treatment, teratogenicity risk, Black Box Warning)",
                    "Contraception - CRITICAL (effective contraception required, teratogenicity risk, Black Box Warning)",
                    "CBC (myelosuppression) - CRITICAL (very common, can be severe, Black Box Warning, weekly for first month, then monthly)",
                    "Signs of infection (fever, chills, CMV, BK virus) - CRITICAL (increased risk of serious infections, Black Box Warning)",
                    "Signs of malignancies (lymphoma, skin cancer) - CRITICAL (increased risk, Black Box Warning)",
                    "Gastrointestinal symptoms (diarrhea, nausea, vomiting) - CRITICAL (very common, dose-limiting, may need dose reduction)",
                    "Formulation - CRITICAL (CellCept and Myfortic are NOT interchangeable, different dosing)"
                ],
                "look_alike_sound_alike": ["Mycophenolate", "Mycophenolate mofetil", "CellCept", "Myfortic", "Azathioprine"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Teratogenicity (Severe Birth Defects, REMS Program)",
                "FDA Black Box Warning - Myelosuppression (Very Common, Can Be Severe)",
                "FDA Black Box Warning - Increased Risk of Infections and Malignancies",
                "FDA Black Box Warning - CellCept and Myfortic NOT Interchangeable",
                "FDA Drug Label - Mycophenolate (CellCept, Myfortic)",
                "KDIGO Guidelines - Kidney Transplant",
                "ACR Guidelines - Lupus Nephritis"
            ]
        },

        "Naloxone": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "look_alike_sound_alike": [],
                "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
                "requires_double_check": True,
                "icu_critical_care_only": False,
            },
        },

        "Norepinephrine": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": True,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "cardiac": "High (arrhythmias, myocardial ischemia - especially in cardiac patients)",
                    "peripheral": "High (peripheral ischemia, tissue necrosis - especially with extravasation, Black Box Warning)",
                    "renal": "Moderate (renal ischemia - can worsen acute kidney injury)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Blood pressure - CRITICAL (continuous monitoring, target MAP 65-70 mmHg in septic shock)",
                    "ECG - CRITICAL (continuous monitoring, arrhythmias, myocardial ischemia risk)",
                    "Peripheral perfusion - CRITICAL (peripheral ischemia, tissue necrosis risk, Black Box Warning)",
                    "Extravasation - CRITICAL (can cause severe tissue necrosis, use central line, Black Box Warning)",
                    "Renal function (urine output, creatinine) - CRITICAL (renal ischemia risk, can worsen AKI)",
                    "Lactate levels - CRITICAL (tissue ischemia marker)",
                    "Administration route - CRITICAL (central line preferred, avoid peripheral if possible, Black Box Warning)"
                ],
                "look_alike_sound_alike": ["Norepinephrine", "Levophed", "Epinephrine", "Dopamine"]
            },
            "guideline_tags": [
                "SSC Guidelines - Septic Shock Management",
                "AHA ACLS Guidelines - Shock Management",
                "FDA Black Box Warning - Extravasation (Can Cause Severe Tissue Necrosis)",
                "FDA Drug Label - Norepinephrine (Levophed)",
                "ISMP High Alert Medications"
            ]
        },

        "Oxaliplatin": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "look_alike_sound_alike": [],
                "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
                "requires_double_check": True,
                "icu_critical_care_only": False,
            },
        },

        "Oxcarbazepine": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": True,
                "look_alike_sound_alike": [],
                "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
                "requires_double_check": False,
                "icu_critical_care_only": False,
            },
        },

        "Oxycodone": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "look_alike_sound_alike": [],
                "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
                "requires_double_check": True,
                "icu_critical_care_only": False,
            },
        },

        "Paclitaxel": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "look_alike_sound_alike": [],
                "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
                "requires_double_check": True,
                "icu_critical_care_only": False,
            },
        },

        "Palonosetron": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "look_alike_sound_alike": [],
                "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
                "requires_double_check": True,
                "icu_critical_care_only": False,
            },
        },

        "Perampanel": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": True,
                "look_alike_sound_alike": [],
                "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
                "requires_double_check": False,
                "icu_critical_care_only": False,
            },
        },

        "Phenobarbital": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": True,
                "look_alike_sound_alike": [],
                "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
                "requires_double_check": False,
                "icu_critical_care_only": False,
            },
        },

        "Phenytoin": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": True,
                "look_alike_sound_alike": [],
                "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
                "requires_double_check": False,
                "icu_critical_care_only": False,
            },
        },

        "Prasugrel": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": True,
                "organ_toxicity": {
                    "hematologic": "High (bleeding - very common, can be severe and life-threatening, Black Box Warning)",
                    "hematologic_thrombotic": "Moderate (thrombotic thrombocytopenic purpura - TTP, rare but dangerous)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Signs of bleeding (epistaxis, gingival bleeding, melena, hematemesis, injection site bleeding) - CRITICAL (very common, can be severe and life-threatening, Black Box Warning)",
                    "Major bleeding (GI bleeding, intracranial hemorrhage, post-surgical bleeding) - CRITICAL (Black Box Warning)",
                    "Thrombotic thrombocytopenic purpura (TTP) - CRITICAL (fever, anemia, thrombocytopenia, neurological symptoms - rare but dangerous)",
                    "Platelet count - CRITICAL (if signs of bleeding or TTP)",
                    "Age and weight - CRITICAL (contraindicated if age ≥75 years or weight <60kg, Black Box Warning, increased bleeding risk)",
                    "History of stroke/TIA - CRITICAL (contraindicated if history of stroke or TIA, Black Box Warning, increased bleeding risk)"
                ],
                "look_alike_sound_alike": ["Prasugrel", "Effient", "Clopidogrel", "Ticagrelor"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Bleeding (Very Common, Can Be Severe and Life-Threatening)",
                "FDA Black Box Warning - Contraindicated in Age ≥75 Years or Weight <60kg (Increased Bleeding Risk)",
                "FDA Black Box Warning - Contraindicated in History of Stroke or TIA (Increased Bleeding Risk)",
                "FDA Drug Label - Prasugrel (Effient)",
                "ACC/AHA Guidelines - Acute Coronary Syndrome",
                "ACC/AHA Guidelines - Dual Antiplatelet Therapy (DAPT)",
                "ESC Guidelines - Cardiovascular Disease Prevention"
            ]
        },

        "Pregabalin": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": True,
                "look_alike_sound_alike": [],
                "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
                "requires_double_check": False,
                "icu_critical_care_only": False,
            },
        },

        "Primidone": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": True,
                "look_alike_sound_alike": [],
                "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
                "requires_double_check": False,
                "icu_critical_care_only": False,
            },
        },

        "Procainamide": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": True,
                "look_alike_sound_alike": [],
                "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
                "requires_double_check": True,
                "icu_critical_care_only": False,
            },
        },

        "Propafenone": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": True,
                "look_alike_sound_alike": [],
                "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
                "requires_double_check": True,
                "icu_critical_care_only": False,
            },
        },

        "Protamine": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "look_alike_sound_alike": [],
                "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
                "requires_double_check": True,
                "icu_critical_care_only": False,
            },
        },

        "Rivaroxaban": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": True,
                "organ_toxicity": {
                    "hematologic": "High (bleeding - very common, can be severe and life-threatening, Black Box Warning)",
                    "hepatic": "Low (hepatotoxicity - elevated transaminases, rare)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Signs of bleeding (GI bleeding, intracranial hemorrhage, post-surgical bleeding) - CRITICAL (very common, can be severe and life-threatening, Black Box Warning)",
                    "Creatinine - CRITICAL (for dose adjustment, contraindicated if CrCl <30, reduce dose if CrCl 15-30)",
                    "Hepatic function (ALT, AST) - CRITICAL (rare hepatotoxicity, contraindicated in Child-Pugh C)",
                    "Drug interactions (CYP3A4/P-gp inhibitors/inducers - CONTRAINDICATED/AVOID strong inhibitors) - CRITICAL",
                    "Hepatic impairment - CRITICAL (contraindicated in Child-Pugh C)",
                    "Andexanet alfa availability - CRITICAL (antidote for bleeding, if available)"
                ],
                "look_alike_sound_alike": ["Rivaroxaban", "Xarelto", "Apixaban", "Edoxaban", "Dabigatran"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Bleeding (Very Common, Can Be Severe and Life-Threatening)",
                "FDA Black Box Warning - No Specific Antidote (Before Andexanet Alfa)",
                "FDA Drug Label - Rivaroxaban (Xarelto)",
                "AHA/ACC/HRS Guidelines - Atrial Fibrillation Stroke Prevention",
                "CHEST Guidelines - VTE Treatment and Prophylaxis",
                "ESC Guidelines - Atrial Fibrillation"
            ]
        },

        "Tacrolimus": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": True,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "renal": "High (nephrotoxicity - very common, dose-dependent, can be severe and irreversible, Black Box Warning)",
                    "neurologic": "High (neurotoxicity - seizures, encephalopathy, tremor, confusion - can be severe, Black Box Warning)",
                    "metabolic": "High (post-transplant diabetes mellitus - NODAT - very common, Black Box Warning)",
                    "oncologic": "High (increased risk of infections and malignancies - lymphoma, skin cancer, Black Box Warning)",
                    "cardiovascular": "Moderate (hypertension, hyperkalemia - common)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": True,
                "requires_monitoring": [
                    "Tacrolimus trough levels - CRITICAL (narrow therapeutic index, TDM required, target varies by indication, Black Box Warning)",
                    "Renal function (CrCl, BUN, creatinine) - CRITICAL (nephrotoxicity very common, dose-dependent, can be severe and irreversible, Black Box Warning)",
                    "Neurological status (seizures, encephalopathy, tremor, confusion) - CRITICAL (neurotoxicity can be severe, Black Box Warning)",
                    "Blood glucose and HbA1c - CRITICAL (post-transplant diabetes - NODAT - very common, Black Box Warning)",
                    "Blood pressure - CRITICAL (hypertension common)",
                    "Serum potassium - CRITICAL (hyperkalemia common)",
                    "Signs of infection (fever, chills) - CRITICAL (increased risk of serious infections, Black Box Warning)",
                    "Signs of malignancies (lymphoma, skin cancer) - CRITICAL (increased risk, Black Box Warning)",
                    "Drug interactions (CYP3A4 inhibitors/inducers - CRITICAL, grapefruit juice - increases levels, Black Box Warning)"
                ],
                "look_alike_sound_alike": ["Tacrolimus", "Prograf", "Advagraf", "Cyclosporine", "Pimecrolimus"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Nephrotoxicity (Very Common, Dose-Dependent, Can Be Severe and Irreversible)",
                "FDA Black Box Warning - Neurotoxicity (Seizures, Encephalopathy - Can Be Severe)",
                "FDA Black Box Warning - Post-Transplant Diabetes Mellitus (NODAT - Very Common)",
                "FDA Black Box Warning - Increased Risk of Infections and Malignancies",
                "FDA Black Box Warning - TDM Required (Narrow Therapeutic Index)",
                "KDIGO Guidelines - Kidney Transplant",
                "AST Guidelines - Solid Organ Transplant",
                "FDA Drug Label - Tacrolimus (Prograf, Advagraf)"
            ]
        },

        "Theophylline": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": True,
                "look_alike_sound_alike": [],
                "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
                "requires_double_check": False,
                "icu_critical_care_only": False,
            },
        },

        "Ticagrelor": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": True,
                "organ_toxicity": {
                    "hematologic": "High (bleeding - very common, can be severe and life-threatening, Black Box Warning)",
                    "respiratory": "Moderate (dyspnea - very common, usually mild but can be severe)",
                    "cardiac": "Moderate (bradycardia - can occur, especially with AV block)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Signs of bleeding (epistaxis, gingival bleeding, melena, hematemesis, injection site bleeding) - CRITICAL (very common, can be severe and life-threatening, Black Box Warning)",
                    "Major bleeding (GI bleeding, intracranial hemorrhage, post-surgical bleeding) - CRITICAL (Black Box Warning)",
                    "Respiratory symptoms (dyspnea) - CRITICAL (very common, usually mild but can be severe)",
                    "ECG - CRITICAL (bradycardia, AV block can occur)",
                    "Heart rate - CRITICAL (bradycardia can occur)",
                    "Drug interactions (CYP3A4 inhibitors/inducers - CONTRAINDICATED strong inhibitors, avoid moderate inhibitors) - CRITICAL",
                    "Aspirin dose - CRITICAL (do NOT exceed 100mg/day, Black Box Warning, increases bleeding risk)"
                ],
                "look_alike_sound_alike": ["Ticagrelor", "Brilinta", "Clopidogrel", "Prasugrel"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Bleeding (Very Common, Can Be Severe and Life-Threatening)",
                "FDA Black Box Warning - Aspirin Dose (Do NOT Exceed 100mg/Day)",
                "FDA Drug Label - Ticagrelor (Brilinta)",
                "ACC/AHA Guidelines - Acute Coronary Syndrome",
                "ACC/AHA Guidelines - Dual Antiplatelet Therapy (DAPT)",
                "ESC Guidelines - Cardiovascular Disease Prevention"
            ]
        },

        "Ticlopidine": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "look_alike_sound_alike": [],
                "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
                "requires_double_check": True,
                "icu_critical_care_only": False,
            },
        },

        "Tobramycin": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": True,
                "look_alike_sound_alike": [],
                "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
                "requires_double_check": False,
                "icu_critical_care_only": False,
            },
        },

        "Topiramate": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": True,
                "look_alike_sound_alike": [],
                "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
                "requires_double_check": False,
                "icu_critical_care_only": False,
            },
        },

        "Tramadol": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "look_alike_sound_alike": [],
                "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
                "requires_double_check": True,
                "icu_critical_care_only": False,
            },
        },

        "Valproate": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": True,
                "look_alike_sound_alike": [],
                "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
                "requires_double_check": False,
                "icu_critical_care_only": False,
            },
        },

        "Vancomycin": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": True,
                "look_alike_sound_alike": [],
                "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
                "requires_double_check": False,
                "icu_critical_care_only": False,
            },
        },

        "Vasopressin": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": True,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "cardiac": "High (myocardial ischemia, decreased cardiac output - especially in cardiac patients)",
                    "peripheral": "High (peripheral ischemia, tissue necrosis - especially with extravasation)",
                    "renal": "Moderate (renal ischemia - can worsen acute kidney injury)",
                    "gastrointestinal": "Moderate (mesenteric ischemia - rare but serious)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Blood pressure - CRITICAL (continuous monitoring)",
                    "ECG - CRITICAL (continuous monitoring, myocardial ischemia risk)",
                    "Peripheral perfusion - CRITICAL (peripheral ischemia, tissue necrosis risk)",
                    "Extravasation - CRITICAL (can cause severe tissue necrosis, use central line)",
                    "Renal function (urine output, creatinine) - CRITICAL (renal ischemia risk)",
                    "Signs of mesenteric ischemia (abdominal pain, distension) - CRITICAL (rare but serious)",
                    "Cardiac output - CRITICAL (can decrease, especially in cardiac patients)",
                    "Administration route - CRITICAL (central line preferred, avoid peripheral if possible)"
                ],
                "look_alike_sound_alike": ["Vasopressin", "Pitressin", "Desmopressin", "Terlipressin"]
            },
            "guideline_tags": [
                "SSC Guidelines - Septic Shock Management (Adjunctive Therapy)",
                "AHA ACLS Guidelines - Shock Management",
                "FDA Drug Label - Vasopressin (Pitressin)",
                "ISMP High Alert Medications"
            ]
        },

        "Vitamin K": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "look_alike_sound_alike": [],
                "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
                "requires_double_check": True,
                "icu_critical_care_only": False,
            },
        },

        "Warfarin": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": True,
                "icu_critical_care_only": False,
                "bleeding_risk": True,
                "organ_toxicity": {
                    "hematologic": "High (bleeding - very common, can be severe and life-threatening, Black Box Warning)",
                    "dermatologic": "Moderate (skin necrosis - rare but serious, warfarin-induced skin necrosis)",
                    "fetal": "High (teratogenicity - Black Box Warning, contraindicated in pregnancy)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "INR - CRITICAL (target 2.0-3.0 for most indications, 2.5-3.5 for mechanical heart valves, Black Box Warning)",
                    "Signs of bleeding (GI bleeding, intracranial hemorrhage, post-surgical bleeding) - CRITICAL (very common, can be severe and life-threatening, Black Box Warning)",
                    "Drug interactions (many drugs affect warfarin - CRITICAL, check before starting/stopping any medication)",
                    "Diet (vitamin K intake - CRITICAL, maintain consistent intake)",
                    "Alcohol intake - CRITICAL (increases bleeding risk)",
                    "Hepatic function (ALT, AST) - CRITICAL (warfarin metabolism affected by liver function)",
                    "Vitamin K availability - CRITICAL (antidote for bleeding)"
                ],
                "look_alike_sound_alike": ["Warfarin", "Coumadin", "Jantoven", "Acenocoumarol"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Bleeding (Very Common, Can Be Severe and Life-Threatening)",
                "FDA Black Box Warning - Teratogenicity (Contraindicated in Pregnancy)",
                "FDA Black Box Warning - INR Monitoring Required",
                "FDA Drug Label - Warfarin (Coumadin)",
                "AHA/ACC/HRS Guidelines - Atrial Fibrillation Stroke Prevention",
                "CHEST Guidelines - VTE Treatment and Prophylaxis",
                "ESC Guidelines - Atrial Fibrillation",
                "ACCP Guidelines - Antithrombotic Therapy"
            ]
        },

        "Zonisamide": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": True,
                "look_alike_sound_alike": [],
                "organ_toxicity": {'hepatic': 'unknown', 'renal': 'unknown', 'cardiac': 'unknown', 'hematologic': 'unknown'},
                "requires_double_check": False,
                "icu_critical_care_only": False,
            },
        },

        "Enalapril": {
            "guideline_tags": {
                "who_atc": "C09AA02",
                "ahfs_category": "24.08.08 ACE Inhibitors",
                "vietnam_essential_medicines": True,
                "international_guidelines": [
                    {
                        "source": "ESC 2021 Heart Failure",
                        "recommendation": "ACE inhibitor first-line therapy for HFrEF if tolerated",
                        "context": "Heart failure with reduced ejection fraction (HFrEF), NYHA II–III",
                    },
                    {
                        "source": "ACC/AHA 2017 Hypertension Guideline",
                        "recommendation": "One of the first-line options for hypertension",
                        "context": "Primary hypertension, non-black, with or without diabetes",
                    },
                ],
                "vn_guidelines": [
                    {
                        "source": "BYT – Hướng dẫn chẩn đoán và điều trị tăng huyết áp 2020",
                        "recommendation": "Một trong các lựa chọn hàng đầu điều trị tăng huyết áp",
                        "context": "Tăng huyết áp nguyên phát không biến chứng, ưu tiên bệnh nhân có đái tháo đường hoặc bệnh thận mạn",
                    }
                ],
                "clinical_tags": [
                    "first_line_htn",
                    "hfref_mortality_benefit",
                    "ckd_proteinuria_bp_control",
                ],
            },
            "availability_vietnam": {
                "status": "common",
                "level_of_care": ["district", "provincial", "central"],
                "insurance_coverage": "bhyt_full",
                "brand_examples": ["Enalapril STADA", "Renitec"],
                "notes": "Rất phổ biến trong điều trị tăng huyết áp và suy tim; thường có trong danh mục BHYT.",
            },
        },

        "Lisinopril": {
            "guideline_tags": {
                "who_atc": "C09AA03",
                "ahfs_category": "24.08.08 ACE Inhibitors",
                "vietnam_essential_medicines": True,
                "international_guidelines": [
                    {
                        "source": "ESC 2021 Heart Failure",
                        "recommendation": "ACE inhibitor first-line therapy for HFrEF if ARNI not available",
                        "context": "Heart failure with reduced ejection fraction (HFrEF), NYHA II–III",
                    }
                ],
                "vn_guidelines": [
                    {
                        "source": "BYT – Hướng dẫn chẩn đoán và điều trị suy tim 2015",
                        "recommendation": "Thuốc nền tảng trong điều trị suy tim HFrEF cùng với beta-blocker và mineralocorticoid receptor antagonist",
                        "context": "Suy tim mạn HFrEF, NYHA II–IV",
                    }
                ],
                "clinical_tags": [
                    "first_line_htn",
                    "hfref_mortality_benefit",
                ],
            },
            "availability_vietnam": {
                "status": "common",
                "level_of_care": ["provincial", "central"],
                "insurance_coverage": "bhyt_full",
                "brand_examples": ["Zestril", "Lisinopril STADA"],
                "notes": "Có mặt ở hầu hết bệnh viện tuyến tỉnh trở lên; một số nơi dùng Enalapril hoặc Perindopril thay thế.",
            },
        },

        "Ramipril": {
            "guideline_tags": {
                "who_atc": "C09AA05",
                "ahfs_category": "24.08.08 ACE Inhibitors",
                "vietnam_essential_medicines": False,
                "international_guidelines": [
                    {
                        "source": "HOPE Study / ESC Prevention Guidelines",
                        "recommendation": "ACE inhibitor to reduce CV events in high-risk patients",
                        "context": "Secondary prevention in patients with high cardiovascular risk (coronary artery disease, diabetes, prior stroke)",
                    }
                ],
                "vn_guidelines": [],
                "clinical_tags": [
                    "cv_risk_reduction",
                    "htn_high_risk",
                ],
            },
            "availability_vietnam": {
                "status": "limited",
                "level_of_care": ["provincial", "central", "private"],
                "insurance_coverage": "bhyt_partial",
                "brand_examples": ["Tritace", "Altace"],
                "notes": "Phổ biến hơn ở bệnh viện tuyến cuối và phòng khám tư nhân; dùng cho bệnh nhân nguy cơ tim mạch cao.",
            },
        },

        "Perindopril": {
            "guideline_tags": {
                "who_atc": "C09AA04",
                "ahfs_category": "24.08.08 ACE Inhibitors",
                "vietnam_essential_medicines": False,
                "international_guidelines": [
                    {
                        "source": "EUROPA / PROGRESS Trials",
                        "recommendation": "Reduction of CV events in stable coronary artery disease and stroke prevention",
                        "context": "Stable CAD; prior stroke or TIA with hypertension",
                    }
                ],
                "vn_guidelines": [],
                "clinical_tags": [
                    "htn",
                    "stable_coronary_disease",
                    "stroke_prevention",
                ],
            },
            "availability_vietnam": {
                "status": "common",
                "level_of_care": ["district", "provincial", "central", "private"],
                "insurance_coverage": "bhyt_full",
                "brand_examples": ["Coversyl", "Perindopril STADA"],
                "notes": "Được sử dụng rộng rãi trong điều trị tăng huyết áp và phòng ngừa biến cố tim mạch.",
            },
        },

        "Losartan": {
            "guideline_tags": {
                "who_atc": "C09CA01",
                "ahfs_category": "24.08.06 Angiotensin II Receptor Blockers",
                "vietnam_essential_medicines": True,
                "international_guidelines": [
                    {
                        "source": "ACC/AHA 2017 Hypertension Guideline",
                        "recommendation": "ARB as alternative first-line when ACE inhibitors not tolerated",
                        "context": "Primary hypertension, ACE inhibitor intolerance (e.g. cough, angioedema)",
                    }
                ],
                "vn_guidelines": [
                    {
                        "source": "BYT – Hướng dẫn chẩn đoán và điều trị tăng huyết áp 2020",
                        "recommendation": "Lựa chọn khi không dung nạp ACEI hoặc cần bảo vệ thận",
                        "context": "Tăng huyết áp có đái tháo đường hoặc bệnh thận mạn",
                    }
                ],
                "clinical_tags": [
                    "first_line_htn_alt_acei",
                    "ckd_diabetic_nephropathy",
                ],
            },
            "availability_vietnam": {
                "status": "common",
                "level_of_care": ["district", "provincial", "central"],
                "insurance_coverage": "bhyt_full",
                "brand_examples": ["Losartan STADA", "Cozaar"],
                "notes": "Rất phổ biến; thường dùng cho tăng huyết áp có đái tháo đường hoặc bệnh thận mạn.",
            },
        },

        "Valsartan": {
            "guideline_tags": {
                "who_atc": "C09CA03",
                "ahfs_category": "24.08.06 Angiotensin II Receptor Blockers",
                "vietnam_essential_medicines": False,
                "international_guidelines": [
                    {
                        "source": "ESC 2021 Heart Failure",
                        "recommendation": "ARB as alternative when ACEI not tolerated; part of ARNI when combined with sacubitril",
                        "context": "HFrEF patients unable to take ACEI, or ARNI where available",
                    }
                ],
                "vn_guidelines": [],
                "clinical_tags": [
                    "hfref_alt_acei",
                    "htn",
                ],
            },
            "availability_vietnam": {
                "status": "common",
                "level_of_care": ["provincial", "central", "private"],
                "insurance_coverage": "bhyt_full",
                "brand_examples": ["Diovan", "Valsartan STADA"],
                "notes": "Được sử dụng rộng rãi, đặc biệt trong suy tim và tăng huyết áp kháng trị.",
            },
        },

        "Spironolactone": {
            "guideline_tags": {
                "who_atc": "C03DA01",
                "ahfs_category": "24.08.04 Aldosterone Antagonists",
                "vietnam_essential_medicines": True,
                "international_guidelines": [
                    {
                        "source": "ESC 2021 Heart Failure",
                        "recommendation": "Mineralocorticoid receptor antagonist to reduce mortality",
                        "context": "HFrEF with persistent symptoms despite ACEI/ARB/ARNI and beta-blocker",
                    }
                ],
                "vn_guidelines": [],
                "clinical_tags": [
                    "hfref_mortality_benefit",
                    "hyperaldosteronism",
                ],
            },
            "availability_vietnam": {
                "status": "common",
                "level_of_care": ["district", "provincial", "central"],
                "insurance_coverage": "bhyt_full",
                "brand_examples": ["Spironolactone STADA", "Aldactone"],
                "notes": "Sẵn có ở đa số bệnh viện; thường dùng trong suy tim, xơ gan cổ trướng, hội chứng cường aldosterone.",
            },
        },

        "Metformin": {
            "guideline_tags": {
                "who_atc": "A10BA02",
                "ahfs_category": "68.20.08 Biguanides",
                "vietnam_essential_medicines": True,
                "international_guidelines": [
                    {
                        "source": "ADA 2024 Standards of Care",
                        "recommendation": "Initial pharmacologic therapy for most adults with type 2 diabetes",
                        "context": "Type 2 diabetes without contraindications; often combined with lifestyle changes",
                    }
                ],
                "vn_guidelines": [
                    {
                        "source": "BYT – Hướng dẫn chẩn đoán và điều trị đái tháo đường typ 2",
                        "recommendation": "Thuốc đầu tay trong điều trị đái tháo đường typ 2 nếu không chống chỉ định",
                        "context": "ĐTĐ typ 2, không suy thận nặng hoặc chống chỉ định khác",
                    }
                ],
                "clinical_tags": [
                    "first_line_t2dm",
                    "weight_neutral_or_loss",
                    "low_hypoglycemia_risk",
                ],
            },
            "availability_vietnam": {
                "status": "common",
                "level_of_care": ["district", "provincial", "central", "private"],
                "insurance_coverage": "bhyt_full",
                "brand_examples": ["Metformin STADA", "Glucophage"],
                "notes": "Thuốc nền tảng trong điều trị ĐTĐ typ 2, rất dễ tiếp cận tại Việt Nam.",
            },
        },

        "Empagliflozin": {
            "guideline_tags": {
                "who_atc": "A10BK03",
                "ahfs_category": "68.20.32 Sodium-Glucose Co-Transporter 2 (SGLT2) Inhibitors",
                "vietnam_essential_medicines": False,
                "international_guidelines": [
                    {
                        "source": "ADA 2024 Standards of Care",
                        "recommendation": "Preferred add-on in patients with ASCVD, HF, or CKD",
                        "context": "Type 2 diabetes with established ASCVD, HF, or CKD",
                    },
                    {
                        "source": "ESC 2021 Heart Failure",
                        "recommendation": "Core therapy for HFrEF regardless of diabetes",
                        "context": "Heart failure with reduced ejection fraction (HFrEF)",
                    },
                ],
                "vn_guidelines": [],
                "clinical_tags": [
                    "t2dm_with_ascvd",
                    "hfref_mortality_benefit",
                    "ckd_progression_slowing",
                ],
            },
            "availability_vietnam": {
                "status": "limited",
                "level_of_care": ["provincial", "central", "private"],
                "insurance_coverage": "bhyt_partial",
                "brand_examples": ["Jardiance"],
                "notes": "Thường có tại bệnh viện tuyến tỉnh/trung ương và phòng khám tư; chi phí cao hơn, BHYT chi trả một phần tuỳ hạng mục.",
            },
        },

        "Dapagliflozin": {
            "guideline_tags": {
                "who_atc": "A10BK01",
                "ahfs_category": "68.20.32 Sodium-Glucose Co-Transporter 2 (SGLT2) Inhibitors",
                "vietnam_essential_medicines": False,
                "international_guidelines": [
                    {
                        "source": "ADA 2024 Standards of Care",
                        "recommendation": "Add-on therapy in patients with HF or CKD",
                        "context": "Type 2 diabetes with heart failure or CKD",
                    },
                    {
                        "source": "ESC 2021 Heart Failure",
                        "recommendation": "Core therapy for HFrEF, beneficial in HFpEF as well",
                        "context": "Heart failure (HFrEF/HFpEF), with or without diabetes",
                    },
                ],
                "vn_guidelines": [],
                "clinical_tags": [
                    "t2dm_with_hf",
                    "hf_mortality_benefit",
                    "ckd_progression_slowing",
                ],
            },
            "availability_vietnam": {
                "status": "limited",
                "level_of_care": ["provincial", "central", "private"],
                "insurance_coverage": "bhyt_partial",
                "brand_examples": ["Forxiga"],
                "notes": "Tương tự Empagliflozin, chủ yếu có ở tuyến trên và cơ sở tư nhân.",
            },
        },

        "Insulin": {
            "guideline_tags": {
                "who_atc": "A10AB",
                "ahfs_category": "68.20.04 Insulins",
                "vietnam_essential_medicines": True,
                "international_guidelines": [
                    {
                        "source": "ADA 2024 Standards of Care",
                        "recommendation": "Mandatory in type 1 diabetes; add-on in type 2 when oral therapy inadequate",
                        "context": "Type 1 diabetes; type 2 diabetes with severe hyperglycemia or catabolic symptoms",
                    }
                ],
                "vn_guidelines": [
                    {
                        "source": "BYT – Hướng dẫn chẩn đoán và điều trị đái tháo đường typ 1 và typ 2",
                        "recommendation": "Bắt buộc trong ĐTĐ typ 1; chỉ định khi ĐTĐ typ 2 không kiểm soát với thuốc uống",
                        "context": "ĐTĐ typ 1; ĐTĐ typ 2 thất bại điều trị bằng thuốc uống",
                    }
                ],
                "clinical_tags": [
                    "mandatory_t1dm",
                    "add_on_t2dm_severe",
                    "high_hypoglycemia_risk",
                ],
            },
            "availability_vietnam": {
                "status": "common",
                "level_of_care": ["district", "provincial", "central"],
                "insurance_coverage": "bhyt_full",
                "brand_examples": ["Insulin Mixtard", "Actrapid", "Lantus", "Levemir"],
                "notes": "Insulin nền và hỗn hợp có rộng rãi; một số analog mới có thể giới hạn tại bệnh viện tuyến trên.",
            },
        },

        "Warfarin": {
            "guideline_tags": {
                "who_atc": "B01AA03",
                "ahfs_category": "20.12.04 Coumarin Anticoagulants",
                "vietnam_essential_medicines": True,
                "international_guidelines": [
                    {
                        "source": "ESC 2020 Atrial Fibrillation Guideline",
                        "recommendation": "Alternative to DOACs when DOACs contraindicated or not available",
                        "context": "Non-valvular atrial fibrillation with CHA2DS2-VASc ≥2 in men / ≥3 in women",
                    }
                ],
                "vn_guidelines": [],
                "clinical_tags": [
                    "stroke_prevention_af",
                    "vte_treatment",
                    "mechanical_valve_mandatory",
                ],
            },
            "availability_vietnam": {
                "status": "common",
                "level_of_care": ["district", "provincial", "central"],
                "insurance_coverage": "bhyt_full",
                "brand_examples": ["Warfarin STADA", "Coumadin"],
                "notes": "Rất phổ biến; cần theo dõi INR chặt chẽ, thường gắn với phòng khám chống đông.",
            },
        },

        "Rivaroxaban": {
            "guideline_tags": {
                "who_atc": "B01AF01",
                "ahfs_category": "20.12.16 Direct Factor Xa Inhibitors",
                "vietnam_essential_medicines": False,
                "international_guidelines": [
                    {
                        "source": "ESC 2020 Atrial Fibrillation Guideline",
                        "recommendation": "Preferred over VKAs in eligible non-valvular AF patients",
                        "context": "Non-valvular AF with CHA2DS2-VASc ≥2 in men / ≥3 in women",
                    }
                ],
                "vn_guidelines": [],
                "clinical_tags": [
                    "stroke_prevention_af",
                    "vte_treatment",
                ],
            },
            "availability_vietnam": {
                "status": "limited",
                "level_of_care": ["provincial", "central", "private"],
                "insurance_coverage": "bhyt_partial",
                "brand_examples": ["Xarelto"],
                "notes": "Chi phí cao, chủ yếu dùng ở bệnh viện tuyến trên và cơ sở tư nhân; BHYT chi trả giới hạn.",
            },
        },

        "Apixaban": {
            "guideline_tags": {
                "who_atc": "B01AF02",
                "ahfs_category": "20.12.16 Direct Factor Xa Inhibitors",
                "vietnam_essential_medicines": False,
                "international_guidelines": [
                    {
                        "source": "ESC 2020 Atrial Fibrillation Guideline",
                        "recommendation": "Preferred DOAC option with favorable bleeding profile",
                        "context": "Non-valvular AF; VTE treatment and secondary prevention",
                    }
                ],
                "vn_guidelines": [],
                "clinical_tags": [
                    "stroke_prevention_af",
                    "vte_treatment",
                    "lower_major_bleeding_risk",
                ],
            },
            "availability_vietnam": {
                "status": "limited",
                "level_of_care": ["provincial", "central", "private"],
                "insurance_coverage": "bhyt_partial",
                "brand_examples": ["Eliquis"],
                "notes": "Tương tự Rivaroxaban; thường được dùng khi cần ưu tiên an toàn chảy máu.",
            },
        },

        "Dabigatran": {
            "guideline_tags": {
                "who_atc": "B01AE07",
                "ahfs_category": "20.12.20 Direct Thrombin Inhibitors",
                "vietnam_essential_medicines": False,
                "international_guidelines": [
                    {
                        "source": "ESC 2020 Atrial Fibrillation Guideline",
                        "recommendation": "DOAC alternative to VKAs for stroke prevention in AF",
                        "context": "Non-valvular AF; prevention of stroke and systemic embolism",
                    }
                ],
                "vn_guidelines": [],
                "clinical_tags": [
                    "stroke_prevention_af",
                    "vte_treatment",
                ],
            },
            "availability_vietnam": {
                "status": "limited",
                "level_of_care": ["provincial", "central", "private"],
                "insurance_coverage": "bhyt_partial",
                "brand_examples": ["Pradaxa"],
                "notes": "Có mặt chủ yếu tại bệnh viện tuyến tỉnh/trung ương và một số cơ sở tư nhân.",
            },
        },

        "Enoxaparin": {
            "guideline_tags": {
                "who_atc": "B01AB05",
                "ahfs_category": "20.12.08 Low Molecular Weight Heparins",
                "vietnam_essential_medicines": True,
                "international_guidelines": [
                    {
                        "source": "ESC / ACC Guidelines on ACS and VTE",
                        "recommendation": "Parenteral anticoagulant of choice in many ACS and VTE settings",
                        "context": "ACS management; treatment and prophylaxis of DVT/PE",
                    }
                ],
                "vn_guidelines": [],
                "clinical_tags": [
                    "vte_treatment",
                    "vte_prophylaxis",
                    "acs_management",
                ],
            },
            "availability_vietnam": {
                "status": "common",
                "level_of_care": ["district", "provincial", "central"],
                "insurance_coverage": "bhyt_full",
                "brand_examples": ["Clexane"],
                "notes": "Được dùng rộng rãi trong dự phòng và điều trị huyết khối; thường sẵn có tại các khoa nội và ngoại.",
            },
        },

        "Epinephrine": {
            "availability_vietnam": {
                "status": "common",
                "level_of_care": ["district", "provincial", "central"],
                "insurance_coverage": "bhyt_full",
                "brand_examples": ["Adrenalin"],
                "notes": "Thuốc cấp cứu thiết yếu cho sốc phản vệ, ngừng tim; luôn có sẵn tại khoa cấp cứu và hồi sức.",
            },
        },

        "Norepinephrine": {
            "availability_vietnam": {
                "status": "common",
                "level_of_care": ["provincial", "central"],
                "insurance_coverage": "bhyt_full",
                "brand_examples": ["Norepinephrine Bitartrate"],
                "notes": "Dùng chủ yếu tại ICU/HSTC cho sốc nhiễm trùng và sốc khác; thường không có ở tuyến xã.",
            },
        },

        "Dopamine": {
            "availability_vietnam": {
                "status": "common",
                "level_of_care": ["district", "provincial", "central"],
                "insurance_coverage": "bhyt_full",
                "brand_examples": ["Dopamine hydrochloride"],
                "notes": "Vẫn được sử dụng ở nhiều bệnh viện, dù xu hướng hiện nay ưu tiên norepinephrine.",
            },
        },

        "Dobutamine": {
            "availability_vietnam": {
                "status": "common",
                "level_of_care": ["provincial", "central"],
                "insurance_coverage": "bhyt_full",
                "brand_examples": ["Dobutamine"],
                "notes": "Có sẵn tại ICU/HSTC cho suy tim cấp và sốc tim.",
            },
        },

        "Vasopressin": {
            "availability_vietnam": {
                "status": "limited",
                "level_of_care": ["provincial", "central"],
                "insurance_coverage": "bhyt_partial",
                "brand_examples": ["Vasopressin injection"],
                "notes": "Thường có tại khoa hồi sức tuyến cuối; dùng phối hợp trong sốc nặng kháng catecholamine.",
            },
        },

        "Adenosine": {
            "availability_vietnam": {
                "status": "common",
                "level_of_care": ["provincial", "central"],
                "insurance_coverage": "bhyt_full",
                "brand_examples": ["Adenocor"],
                "notes": "Thuốc cấp cứu loạn nhịp trên thất; thường có tại phòng cấp cứu, can thiệp tim mạch.",
            },
        },

        "Amiodarone": {
            "availability_vietnam": {
                "status": "common",
                "level_of_care": ["district", "provincial", "central"],
                "insurance_coverage": "bhyt_full",
                "brand_examples": ["Cordarone", "Amiodarone STADA"],
                "notes": "Rất phổ biến cho loạn nhịp thất và trên thất nặng; có cả dạng PO và IV.",
            },
        },

        "Lidocaine": {
            "availability_vietnam": {
                "status": "common",
                "level_of_care": ["district", "provincial", "central"],
                "insurance_coverage": "bhyt_full",
                "brand_examples": ["Lidocaine 2%", "Xylocaine"],
                "notes": "Luôn có cho gây tê tại chỗ; dạng IV dùng cho loạn nhịp thất thường có tại ICU/cấp cứu.",
            },
        },

        "Naloxone": {
            "availability_vietnam": {
                "status": "common",
                "level_of_care": ["district", "provincial", "central"],
                "insurance_coverage": "bhyt_full",
                "brand_examples": ["Naloxone injection"],
                "notes": "Thuốc cấp cứu quá liều opioid; nên có sẵn tại tất cả khoa cấp cứu và GMHS.",
            },
        },

        "Protamine": {
            "availability_vietnam": {
                "status": "common",
                "level_of_care": ["provincial", "central"],
                "insurance_coverage": "bhyt_full",
                "brand_examples": ["Protamine sulfate"],
                "notes": "Có tại phòng mổ, ICU, tim mạch can thiệp để đảo ngược heparin.",
            },
        },

        "Vitamin K": {
            "availability_vietnam": {
                "status": "common",
                "level_of_care": ["district", "provincial", "central"],
                "insurance_coverage": "bhyt_full",
                "brand_examples": ["Vitamin K1"],
                "notes": "Rộng rãi; dùng điều trị thiếu vitamin K và đảo ngược tác dụng warfarin.",
            },
        },

        "Morphine": {
            "availability_vietnam": {
                "status": "common",
                "level_of_care": ["district", "provincial", "central"],
                "insurance_coverage": "bhyt_full",
                "brand_examples": ["Morphin sulphate"],
                "notes": "Thuốc gây nghiện được quản lý chặt chẽ; có ở khoa GMHS, ICU và điều trị đau.",
            },
        },

        "Fentanyl": {
            "availability_vietnam": {
                "status": "common",
                "level_of_care": ["provincial", "central"],
                "insurance_coverage": "bhyt_full",
                "brand_examples": ["Fentanyl citrate", "Durogesic patch"],
                "notes": "Dạng tiêm dùng trong GMHS và ICU; dạng miếng dán chủ yếu tại các đơn vị đau mạn tính/tuyến trên.",
            },
        },

        "Hydromorphone": {
            "availability_vietnam": {
                "status": "rare",
                "level_of_care": ["central", "private"],
                "insurance_coverage": "no_bhyt",
                "brand_examples": [],
                "notes": "Ít phổ biến; nếu có thường ở bệnh viện tuyến cuối hoặc cơ sở tư nhân chuyên sâu về giảm đau.",
            },
        },

        "Oxycodone": {
            "availability_vietnam": {
                "status": "limited",
                "level_of_care": ["central", "private"],
                "insurance_coverage": "bhyt_partial",
                "brand_examples": ["OxyContin"],
                "notes": "Có ở một số bệnh viện lớn cho điều trị đau ung thư; quản lý nghiêm ngặt như morphine.",
            },
        },

        "Codeine": {
            "availability_vietnam": {
                "status": "common",
                "level_of_care": ["district", "provincial", "central", "private"],
                "insurance_coverage": "bhyt_full",
                "brand_examples": ["Paracetamol-codeine combinations"],
                "notes": "Thường có trong các chế phẩm phối hợp giảm đau và ho; quản lý theo quy định với opioid yếu.",
            },
        },

        "Tramadol": {
            "availability_vietnam": {
                "status": "common",
                "level_of_care": ["district", "provincial", "central"],
                "insurance_coverage": "bhyt_full",
                "brand_examples": ["Tramadol STADA", "Tramal"],
                "notes": "Dùng rất phổ biến cho đau trung bình–nặng; cần lưu ý lạm dụng và tác dụng phụ thần kinh.",
            },
        },

        "Gentamicin": {
            "availability_vietnam": {
                "status": "common",
                "level_of_care": ["district", "provincial", "central"],
                "insurance_coverage": "bhyt_full",
                "brand_examples": ["Gentamicin injection"],
                "notes": "Kháng sinh kinh điển, chi phí rẻ; cần thận trọng độc tính thận và tai.",
            },
        },

        "Amikacin": {
            "availability_vietnam": {
                "status": "common",
                "level_of_care": ["district", "provincial", "central"],
                "insurance_coverage": "bhyt_full",
                "brand_examples": ["Amikacin injection"],
                "notes": "Thường dùng trong nhiễm khuẩn nặng Gram âm; thường có sẵn tại khoa hồi sức và nội.",
            },
        },

        "Tobramycin": {
            "availability_vietnam": {
                "status": "limited",
                "level_of_care": ["provincial", "central"],
                "insurance_coverage": "bhyt_full",
                "brand_examples": ["Tobramycin injection", "Nebulized formulations (tùy cơ sở)"],
                "notes": "Ít phổ biến hơn Gentamicin/Amikacin; một số trung tâm hô hấp dùng dạng hít cho bệnh nhân đặc biệt.",
            },
        },

        "Vancomycin": {
            "availability_vietnam": {
                "status": "common",
                "level_of_care": ["district", "provincial", "central"],
                "insurance_coverage": "bhyt_full",
                "brand_examples": ["Vancomycin injection"],
                "notes": "Kháng sinh quan trọng điều trị MRSA; thường yêu cầu hội chẩn nhiễm khuẩn và monitor chức năng thận.",
            },
        },

    # ======================== BATCH 1: 30 DRUGS MISSING 2 FIELDS (Session 4) ========================
        "Ramipril": {
            "contraindications_detail": {
                "tuyệt_đối": ['Dị ứng ramipril hoặc các ACE inhibitor khác', 'Có thai (tất cả các tam cá nguyệt) - gây dị tật thai nhi', 'Hẹp động mạch thận 2 bên hoặc hẹp động mạch thận ở thận đơn độc', 'Phù mạch trước đây với ACE inhibitor'],
                "tương_đối": ['Suy thận nặng (CrCl <30) - cần giảm liều', 'Suy gan - thận trọng', 'Hẹp van động mạch chủ nặng', 'Tăng kali máu', 'Dùng với kali-sparing diuretics hoặc kali bổ sung'],
            },
            "reversal_agents": {
                "available": False,
                "agents": [],
                "notes": "Không có thuốc giải độc đặc hiệu; điều trị hỗ trợ triệu chứng.",
            },
        },

        "Perindopril": {
            "contraindications_detail": {
                "tuyệt_đối": ['Dị ứng perindopril hoặc các ACE inhibitor khác', 'Có thai (tất cả các tam cá nguyệt)', 'Hẹp động mạch thận 2 bên', 'Phù mạch trước đây với ACE inhibitor'],
                "tương_đối": ['Suy thận nặng (CrCl <30) - cần giảm liều', 'Suy gan - thận trọng', 'Tăng kali máu', 'Dùng với kali-sparing diuretics'],
            },
            "reversal_agents": {
                "available": False,
                "agents": [],
                "notes": "Không có thuốc giải độc đặc hiệu; điều trị hỗ trợ triệu chứng.",
            },
        },

        "Valsartan": {
            "contraindications_detail": {
                "tuyệt_đối": [],
                "tương_đối": [],
            },
            "reversal_agents": {
                "available": False,
                "agents": [],
                "notes": "Không có thuốc giải độc đặc hiệu; điều trị hỗ trợ triệu chứng.",
            },
        },

        "Metoprolol": {
            "contraindications_detail": {
                "tuyệt_đối": ['Hen phế quản nặng', 'Block nhĩ thất độ 2-3', 'Suy tim cấp không bù', 'Nhịp tim chậm nặng (<50 bpm)', 'Sốc tim', 'Hội chứng sick sinus (trừ khi có máy tạo nhịp)'],
                "tương_đối": ['COPD (thận trọng, có thể dùng liều thấp)', 'Đái tháo đường (che dấu triệu chứng hạ đường huyết)', 'Bệnh mạch máu ngoại biên (có thể làm nặng)', 'Suy gan (giảm chuyển hóa)', 'Dùng với verapamil/diltiazem (tăng nguy cơ block AV)'],
            },
            "renal_adjustment": {
                "normal": "Không đổi liều",
                "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
                "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
                "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
            },
        },

        "Nebivolol": {
            "black_box_warnings": None,
            "contraindications_detail": {
                "tuyệt_đối": ['Hen phế quản nặng - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI', 'Block nhĩ thất độ 2-3 - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI', 'Suy tim cấp không bù - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI', 'Nhịp tim chậm nặng (<60 bpm) - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI', 'Suy gan nặng - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI'],
                "tương_đối": ['Suy thận nặng (CrCl <30) - thận trọng, khởi đầu 2.5mg/ngày, tối đa 10mg/ngày', 'Suy thận trung bình (CrCl 30-60) - thận trọng, khởi đầu 2.5mg/ngày', 'COPD - thận trọng (selective beta-1, ít ảnh hưởng hơn non-selective)', 'Đái tháo đường - che dấu triệu chứng hạ đường huyết', 'Dùng với verapamil/diltiazem - tăng nguy cơ block nhĩ thất'],
            },
        },

        "Propranolol": {
            "contraindications_detail": {
                "tuyệt_đối": ['Hen phế quản', 'Suy tim cấp', 'Block nhĩ thất độ 2-3', 'Nhịp tim chậm nặng (<50 bpm)', 'Sốc tim', 'Hội chứng sick sinus (trừ khi có máy tạo nhịp)'],
                "tương_đối": ['COPD (thận trọng, có thể dùng liều thấp nhưng nguy cơ co thắt phế quản cao hơn)', 'Đái tháo đường (che dấu triệu chứng hạ đường huyết)', 'Bệnh mạch máu ngoại biên (có thể làm nặng)', 'Suy gan (giảm chuyển hóa, extensive first-pass)', 'Dùng với verapamil/diltiazem (tăng nguy cơ block AV)'],
            },
            "renal_adjustment": {
                "normal": "Không đổi liều",
                "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
                "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
                "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
            },
        },

        "Atorvastatin": {
            "contraindications_detail": {
                "tuyệt_đối": ['Bệnh gan hoạt động (active liver disease) - tăng men gan kéo dài, viêm gan', 'Có thai (pregnancy) - FDA category X, gây dị tật thai nhi', 'Cho con bú (lactation) - bài tiết vào sữa mẹ', 'Tiêu cơ vân đang hoạt động (active myopathy/rhabdomyolysis)', 'Dị ứng với atorvastatin hoặc bất kỳ thành phần nào', 'Dùng cùng cyclosporine, itraconazole, ketoconazole (tăng nguy cơ tiêu cơ vân nghiêm trọng)'],
                "tương_đối": ['Suy thận - thận trọng, giảm liều nếu cần', 'Suy gan - thận trọng, theo dõi men gan thường xuyên', 'Uống rượu nhiều - tăng nguy cơ viêm gan', 'Bệnh nhân Châu Á - tăng nồng độ atorvastatin, có thể cần liều thấp hơn', 'Người cao tuổi - tăng nguy cơ đau cơ, tiêu cơ vân', 'Đái tháo đường - statins có thể tăng đường huyết nhẹ', 'Bệnh tuyến giáp - tăng nguy cơ đau cơ', 'Dùng cùng thuốc ức chế CYP3A4 - giảm liều atorvastatin'],
            },
            "renal_adjustment": {
                "normal": "Không đổi liều",
                "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
                "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
                "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
            },
        },

        "Simvastatin": {
            "contraindications_detail": {
                "tuyệt_đối": ['Bệnh gan hoạt động (active liver disease) - tăng men gan kéo dài, viêm gan', 'Có thai (pregnancy) - FDA category X, gây dị tật thai nhi', 'Cho con bú (lactation) - bài tiết vào sữa mẹ', 'Tiêu cơ vân đang hoạt động (active myopathy/rhabdomyolysis)', 'Dị ứng với simvastatin hoặc bất kỳ thành phần nào', 'Dùng cùng cyclosporine, itraconazole, ketoconazole (tăng nguy cơ tiêu cơ vân nghiêm trọng)', 'Dùng grapefruit juice'],
                "tương_đối": ['Suy thận - thận trọng, giảm liều nếu cần', 'Suy gan - thận trọng, theo dõi men gan thường xuyên', 'Uống rượu nhiều - tăng nguy cơ viêm gan', 'Người cao tuổi - tăng nguy cơ đau cơ, tiêu cơ vân', 'Đái tháo đường - statins có thể tăng đường huyết nhẹ', 'Bệnh tuyến giáp - tăng nguy cơ đau cơ', 'Dùng cùng thuốc ức chế CYP3A4 - giảm liều simvastatin', 'Liều cao (>40mg/ngày) - tăng nguy cơ tiêu cơ vân'],
            },
            "renal_adjustment": {
                "normal": "Không đổi liều",
                "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
                "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
                "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
            },
        },

        "Pravastatin": {
            "contraindications_detail": {
                "tuyệt_đối": ['Bệnh gan hoạt động', 'Có thai', 'Cho con bú', 'Tiêu cơ vân đang hoạt động'],
                "tương_đối": ['Suy thận nặng - cần điều chỉnh liều', 'Dùng với cyclosporine - giảm liều', 'Dùng với gemfibrozil - tránh dùng chung'],
            },
            "renal_adjustment": {
                "normal": "Không đổi liều",
                "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
                "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
                "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
            },
        },

        "Fluvastatin": {
            "contraindications_detail": {
                "tuyệt_đối": ['Bệnh gan hoạt động', 'Có thai', 'Cho con bú', 'Tiêu cơ vân đang hoạt động'],
                "tương_đối": ['Suy thận nặng - thận trọng', 'Dùng với cyclosporine - giảm liều', 'Dùng với gemfibrozil - tránh dùng chung'],
            },
            "renal_adjustment": {
                "normal": "Không đổi liều",
                "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
                "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
                "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
            },
        },

        "Pitavastatin": {
            "contraindications_detail": {
                "tuyệt_đối": ['Bệnh gan hoạt động', 'Có thai', 'Cho con bú', 'Tiêu cơ vân đang hoạt động'],
                "tương_đối": ['Suy thận nặng - thận trọng', 'Dùng với cyclosporine - giảm liều tối đa 1mg/ngày', 'Dùng với gemfibrozil - tránh dùng chung'],
            },
            "renal_adjustment": {
                "normal": "Không đổi liều",
                "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
                "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
                "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
            },
        },

        "Ezetimibe": {
            "black_box_warnings": None,
            "contraindications_detail": {
                "tuyệt_đối": ['Dị ứng ezetimibe'],
                "tương_đối": ['Bệnh gan hoạt động (khi dùng với statin) - chống chỉ định statin, nhưng có thể dùng ezetimibe đơn trị', 'Có thai (khi dùng với statin) - statin chống chỉ định trong thai kỳ', 'Dùng với cyclosporine - giảm liều ezetimibe xuống 5mg/ngày', 'Dùng với fibrates - tăng nguy cơ sỏi mật'],
            },
        },

        "Amiodarone": {
            "contraindications_detail": {
                "tuyệt_đối": ['Block nhĩ thất độ 2-3 không có máy tạo nhịp', 'Rối loạn chức năng tuyến giáp không kiểm soát được', 'Bệnh phổi mạn tính nặng (COPD, ILD)', 'Bệnh gan nặng (Child-Pugh C)', 'Có thai (category D)', 'Hạ K+ hoặc Mg2+ nặng (tăng nguy cơ torsades de pointes)'],
                "tương_đối": ['Suy thận nặng (thận trọng, theo dõi chức năng thận)', 'Nhịp tim chậm (tăng nguy cơ block AV)', 'Bệnh phổi nhẹ (theo dõi chức năng phổi chặt chẽ)', 'Rối loạn chức năng tuyến giáp nhẹ (theo dõi TSH chặt chẽ)', 'Đang dùng warfarin hoặc digoxin (cần giảm liều)'],
            },
            "renal_adjustment": {
                "normal": "Không đổi liều",
                "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
                "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
                "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
            },
        },

        "Flecainide": {
            "contraindications_detail": {
                "tuyệt_đối": ['Bệnh tim cấu trúc (suy tim, bệnh mạch vành, bệnh van tim)', 'Block nhĩ thất độ 2-3', 'Hội chứng Brugada', 'QT kéo dài', 'Suy thận nặng (CrCl <30)'],
                "tương_đối": ['Suy thận (CrCl 30-50) - giảm liều 25-50%', 'Block nhĩ thất độ 1 - có thể làm nặng block', 'Dùng với amiodarone - tăng nồng độ flecainide', 'Dùng với beta-blockers, verapamil, diltiazem - tăng nguy cơ block AV'],
            },
            "renal_adjustment": {
                "normal": "Không đổi liều",
                "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
                "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
                "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
            },
        },

        "Propafenone": {
            "contraindications_detail": {
                "tuyệt_đối": ['Bệnh tim cấu trúc (suy tim, bệnh mạch vành, bệnh van tim)', 'Block nhĩ thất độ 2-3', 'Hội chứng Brugada', 'QT kéo dài', 'Suy gan nặng', 'Suy thận nặng (CrCl <30)'],
                "tương_đối": ['Suy gan - giảm liều 25-50%', 'Suy thận (CrCl 30-50) - giảm liều 25-50%', 'Block nhĩ thất độ 1 - có thể làm nặng block', 'Dùng với amiodarone - tăng nồng độ propafenone', 'Dùng với beta-blockers - tăng nguy cơ block AV'],
            },
            "renal_adjustment": {
                "normal": "Không đổi liều",
                "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
                "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
                "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
            },
        },

        "Dronedarone": {
            "contraindications_detail": {
                "tuyệt_đối": ['Suy tim nặng (NYHA class IV) hoặc suy tim không ổn định - CHỐNG CHỈ ĐỊNH (tăng nguy cơ tử vong)', 'Bệnh gan nặng - CHỐNG CHỈ ĐỊNH', 'Block nhĩ thất độ 2-3 không có máy tạo nhịp', 'Nhịp chậm <50 bpm', 'QT prolongation nặng', 'Dùng với CYP3A4 inhibitors mạnh'],
                "tương_đối": ['Suy tim nhẹ đến trung bình (NYHA class I-III) - thận trọng', 'Suy gan nhẹ đến trung bình - thận trọng, theo dõi chặt chẽ', 'Suy thận - tăng creatinine có thể xảy ra (không phải suy thận thực sự)', 'Dùng với digoxin - giảm liều digoxin 50%', 'Dùng với warfarin - theo dõi INR'],
            },
            "renal_adjustment": {
                "normal": "Không đổi liều",
                "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
                "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
                "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
            },
        },

        "Procainamide": {
            "contraindications_detail": {
                "tuyệt_đối": ['Dị ứng procainamide', 'Block nhĩ thất độ 2-3 không có máy tạo nhịp', 'Suy tim nặng', 'Lupus ban đỏ hệ thống đang hoạt động'],
                "tương_đối": ['Suy thận nặng - NAPA tích lũy, giảm liều', 'Suy gan nặng - thận trọng', 'Block nhĩ thất độ 1 - thận trọng', 'QT prolongation - tăng nguy cơ rối loạn nhịp tim'],
            },
            "renal_adjustment": {
                "normal": "Không đổi liều",
                "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
                "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
                "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
            },
        },

        "Adenosine": {
            "black_box_warnings": None,
            "contraindications_detail": {
                "tuyệt_đối": ['Block nhĩ thất độ 2-3 (AV block) không có máy tạo nhịp', 'Hội chứng sick sinus (sick sinus syndrome) không có máy tạo nhịp', 'Hen phế quản nặng hoặc co thắt phế quản nặng', 'Dị ứng adenosine', 'Rung nhĩ/rung thất (không phải chỉ định)'],
                "tương_đối": ['Block AV độ 1 - thận trọng, có thể làm nặng', 'Hen phế quản nhẹ đến trung bình - thận trọng, có thể gây co thắt phế quản', 'Suy tim - thận trọng, có thể gây ngừng tim kéo dài', 'Suy thận nặng - không cần điều chỉnh liều nhưng thận trọng', 'Dùng với dipyridamole - giảm liều 50-75%', 'Dùng với theophylline/caffeine - có thể không hiệu quả', 'Nhịp tim chậm (<50 bpm) - thận trọng, có thể gây ngừng tim'],
            },
        },

        "Ibutilide": {
            "contraindications_detail": {
                "tuyệt_đối": ['Dị ứng ibutilide', 'QT kéo dài (QTc >440ms) - CHỐNG CHỈ ĐỊNH', 'Torsades de pointes - CHỐNG CHỈ ĐỊNH', 'Hạ kali máu, hạ magie máu - CHỐNG CHỈ ĐỊNH (phải điều chỉnh trước)', 'Dùng với thuốc kéo dài QT - CHỐNG CHỈ ĐỊNH'],
                "tương_đối": ['Suy tim nặng - thận trọng', 'Dùng với digoxin - tăng nguy cơ rối loạn nhịp tim', 'Dùng với beta-blockers - tăng nguy cơ nhịp tim chậm'],
            },
            "renal_adjustment": {
                "normal": "Không đổi liều",
                "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
                "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
                "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
            },
        },

        "Amlodipine": {
            "contraindications_detail": {
                "tuyệt_đối": ['Dị ứng amlodipine hoặc dihydropyridine calcium channel blockers', 'Sốc tim', 'Suy tim mất bù nặng (NYHA class IV)'],
                "tương_đối": ['Hẹp van động mạch chủ nặng - có thể gây suy tim', 'Suy gan - giảm chuyển hóa, tăng nồng độ', 'Suy tim nhẹ đến trung bình - thận trọng', 'Phù ngoại biên - tác dụng phụ thường gặp nhưng không nguy hiểm'],
            },
            "renal_adjustment": {
                "normal": "Không đổi liều",
                "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
                "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
                "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
            },
        },

        "Furosemide": {
            "contraindications_detail": {
                "tuyệt_đối": ['Vô niệu', 'Mất nước nặng', 'Hạ kali máu nặng', 'Dị ứng sulfonamide', 'Dị ứng furosemide'],
                "tương_đối": ['Suy thận nặng - có thể cần liều cao hơn (nhưng thận trọng với IV liều cao - nguy cơ điếc)', 'Suy gan nặng - thận trọng (thải một phần qua gan)', 'Hạ natri máu - điều chỉnh trước khi dùng', 'Hạ magie máu - bù magie trước khi dùng', 'Dùng với digoxin - tăng nguy cơ ngộ độc digoxin', 'Dùng với aminoglycosides - tăng nguy cơ điếc', 'Dùng với lithium - tăng nồng độ lithium'],
            },
            "renal_adjustment": {
                "normal": "Không đổi liều",
                "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
                "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
                "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
            },
        },

        "Bumetanide": {
            "contraindications_detail": {
                "tuyệt_đối": ['Vô niệu', 'Mất nước nặng', 'Hạ kali máu nặng', 'Dị ứng sulfonamide'],
                "tương_đối": ['Suy thận nặng - có thể cần liều cao hơn nhưng thận trọng', 'Suy gan nặng - thận trọng', 'Đang dùng digoxin - tăng nguy cơ ngộ độc digoxin'],
            },
            "renal_adjustment": {
                "normal": "Không đổi liều",
                "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
                "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
                "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
            },
        },

        "Torsemide": {
            "contraindications_detail": {
                "tuyệt_đối": ['Vô niệu', 'Mất nước nặng', 'Hạ kali máu nặng', 'Dị ứng sulfonamide'],
                "tương_đối": ['Suy thận nặng - có thể cần liều cao hơn nhưng thận trọng', 'Suy gan nặng - thận trọng', 'Đang dùng digoxin - tăng nguy cơ ngộ độc digoxin'],
            },
            "renal_adjustment": {
                "normal": "Không đổi liều",
                "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
                "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
                "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
            },
        },

        "Chlorthalidone": {
            "contraindications_detail": {
                "tuyệt_đối": ['Dị ứng chlorthalidone hoặc sulfonamide', 'Vô niệu', 'Hạ kali máu nặng không kiểm soát', 'Suy gan nặng'],
                "tương_đối": ['Suy thận (CrCl <30) - giảm hiệu quả, tăng nguy cơ tác dụng phụ', 'Hạ kali máu - có thể làm nặng', 'Hạ natri máu - có thể làm nặng', 'Đái tháo đường - có thể tăng đường huyết', 'Gout - có thể tăng acid uric, gây cơn gout', 'Người cao tuổi - tăng nguy cơ hạ natri máu, té ngã', 'Dùng với digoxin - tăng nguy cơ ngộ độc digoxin', 'Dùng với lithium - tăng nguy cơ độc tính lithium'],
            },
            "renal_adjustment": {
                "normal": "Không đổi liều",
                "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
                "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
                "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
            },
        },

        "Warfarin": {
            "contraindications_detail": {
                "tuyệt_đối": ['Chảy máu đang hoạt động', 'Có thai (3 tháng đầu và cuối - category X)', 'Bệnh gan nặng (Child-Pugh C)', 'Thiếu protein C hoặc S bẩm sinh (tăng nguy cơ hoại tử da)', 'Không tuân thủ điều trị'],
                "tương_đối": ['Bệnh gan nhẹ-trung bình (thận trọng, theo dõi chức năng gan)', 'Suy thận nặng (thận trọng)', 'Người già (>75 tuổi - tăng nguy cơ chảy máu)', 'Tiền sử loét dạ dày tá tràng (tăng nguy cơ chảy máu)', 'Đang dùng aspirin/NSAIDs (tăng nguy cơ chảy máu)', 'Rối loạn đông máu (hemophilia, von Willebrand disease)'],
            },
            "renal_adjustment": {
                "normal": "Không đổi liều",
                "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
                "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
                "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
            },
        },

        "Clopidogrel": {
            "contraindications_detail": {
                "tuyệt_đối": ['Chảy máu đang hoạt động', 'Xuất huyết nội sọ đang hoạt động', 'Dị ứng clopidogrel'],
                "tương_đối": ['Nguy cơ chảy máu cao (loét dạ dày, xuất huyết gần đây) - thận trọng', 'Suy gan nặng - thận trọng', 'Suy thận nặng - thận trọng', 'Phẫu thuật lớn - cần ngừng trước phẫu thuật', 'Poor metabolizers CYP2C19 - có thể giảm đáp ứng, cân nhắc dùng prasugrel/ticagrelor'],
            },
            "renal_adjustment": {
                "normal": "Không đổi liều",
                "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
                "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
                "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
            },
        },

        "Ticagrelor": {
            "contraindications_detail": {
                "tuyệt_đối": ['Chảy máu đang hoạt động', 'Xuất huyết nội sọ đang hoạt động', 'Dị ứng ticagrelor', 'Dùng strong CYP3A4 inhibitors (ketoconazole, itraconazole, clarithromycin, ritonavir)'],
                "tương_đối": ['Suy gan nặng - chống chỉ định', 'Nguy cơ chảy máu cao (loét dạ dày, xuất huyết gần đây) - thận trọng', 'Tiền sử nhịp tim chậm hoặc block nhĩ thất - tăng nguy cơ bradycardia', 'Suy thận nặng - thận trọng', 'Phẫu thuật lớn - cần ngừng trước phẫu thuật'],
            },
            "renal_adjustment": {
                "normal": "Không đổi liều",
                "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
                "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
                "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
            },
        },

        "Prasugrel": {
            "contraindications_detail": {
                "tuyệt_đối": ['Chảy máu đang hoạt động', 'Tiền sử TIA hoặc đột quỵ', 'Dị ứng prasugrel'],
                "tương_đối": ['Tuổi ≥75 (trừ nguy cơ cao) - tăng nguy cơ chảy máu, cân nhắc liều 5mg/ngày', 'Cân nặng <60kg (trừ nguy cơ cao) - tăng nguy cơ chảy máu, cân nhắc liều 5mg/ngày', 'Nguy cơ chảy máu cao (loét dạ dày, xuất huyết gần đây) - thận trọng', 'Phẫu thuật lớn - cần ngừng trước phẫu thuật', 'Suy gan nặng - thận trọng', 'Suy thận nặng - thận trọng'],
            },
            "renal_adjustment": {
                "normal": "Không đổi liều",
                "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
                "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
                "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
            },
        },

        "Enoxaparin": {
            "contraindications_detail": {
                "tuyệt_đối": ['Chảy máu đang hoạt động', 'Giảm tiểu cầu do heparin (HIT) đang hoạt động hoặc tiền sử', 'Dị ứng heparin/enoxaparin'],
                "tương_đối": ['Suy thận nặng (CrCl <30) - giảm liều hoặc dùng UFH thay thế', 'Nguy cơ chảy máu cao (loét dạ dày, xuất huyết gần đây) - thận trọng', 'Phẫu thuật lớn - cần ngừng trước phẫu thuật', 'Có thai - tương đối an toàn nhưng thận trọng'],
            },
            "renal_adjustment": {
                "normal": "Không đổi liều",
                "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
                "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
                "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
            },
        },

        "Rivaroxaban": {
            "contraindications_detail": {
                "tuyệt_đối": ['Chảy máu đang hoạt động', 'Suy thận nặng (CrCl <15) - chống chỉ định', 'Dị ứng rivaroxaban', 'Dùng CYP3A4 và P-gp inhibitors mạnh (ketoconazole, ritonavir)'],
                "tương_đối": ['Suy thận (CrCl 15-50) - giảm liều (15mg x 1 lần/ngày cho AFib)', 'Nguy cơ chảy máu cao (loét dạ dày, xuất huyết gần đây) - thận trọng', 'Phẫu thuật lớn - cần ngừng trước phẫu thuật', 'Có thai - tránh dùng'],
            },
            "renal_adjustment": {
                "normal": "Không đổi liều",
                "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
                "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
                "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
            },
        },

    # ======================== BATCH 2: 30 DRUGS (31-60) ========================
        "Apixaban": {
            "contraindications_detail": {
                "tuyệt_đối": ['Chảy máu đang hoạt động', 'Suy thận nặng (CrCl <15) - chống chỉ định', 'Dị ứng apixaban', 'Dùng CYP3A4 và P-gp inhibitors mạnh (ketoconazole, ritonavir)'],
                "tương_đối": ['Suy thận (CrCl 15-30) - thận trọng, có thể cần giảm liều', 'Nguy cơ chảy máu cao (loét dạ dày, xuất huyết gần đây) - thận trọng', 'Phẫu thuật lớn - cần ngừng trước phẫu thuật', 'Có thai - tránh dùng'],
            },
            "renal_adjustment": {
                "normal": "Không đổi liều",
                "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
                "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
                "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
            },
        },

        "Dabigatran": {
            "contraindications_detail": {
                "tuyệt_đối": ['Chảy máu đang hoạt động', 'Suy thận nặng (CrCl <30) - chống chỉ định', 'Dị ứng dabigatran', 'Dùng P-gp inhibitors mạnh (ketoconazole, dronedarone)'],
                "tương_đối": ['Suy thận (CrCl 30-50) - giảm liều (110mg x 2 lần/ngày)', 'Nguy cơ chảy máu cao (loét dạ dày, xuất huyết gần đây) - thận trọng', 'Phẫu thuật lớn - cần ngừng trước phẫu thuật', 'Có thai - tránh dùng'],
            },
            "renal_adjustment": {
                "normal": "Không đổi liều",
                "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
                "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
                "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
            },
        },

        "Edoxaban": {
            "contraindications_detail": {
                "tuyệt_đối": ['Chảy máu đang hoạt động', 'Suy thận nặng (CrCl <15) - chống chỉ định', 'Dị ứng edoxaban'],
                "tương_đối": ['Suy thận (CrCl 15-50) - giảm liều xuống 30mg x 1 lần/ngày', 'Cân nặng ≤60kg - giảm liều xuống 30mg x 1 lần/ngày', 'Nguy cơ chảy máu cao (loét dạ dày, xuất huyết gần đây) - thận trọng', 'Phẫu thuật lớn - cần ngừng trước phẫu thuật', 'Có thai - tránh dùng'],
            },
            "renal_adjustment": {
                "normal": "Không đổi liều",
                "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
                "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
                "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
            },
        },

        "Alirocumab": {
            "contraindications_detail": {
                "tuyệt_đối": ['Dị ứng với alirocumab hoặc bất kỳ thành phần nào', 'Dị ứng với protein tái tổ hợp'],
                "tương_đối": ['Suy gan nặng - chưa có dữ liệu đầy đủ', 'Suy thận nặng - không cần chỉnh liều nhưng thận trọng'],
            },
            "renal_adjustment": {
                "normal": "Không đổi liều",
                "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
                "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
                "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
            },
            "hepatic_adjustment": {
                "mild": "Không cần chỉnh liều.",
                "moderate": "Thận trọng, chưa có dữ liệu đầy đủ.",
                "severe": "Thiếu dữ liệu; cân nhắc thuốc khác nếu có thể.",
                "notes": "Alirocumab là monoclonal antibody, không chuyển hóa qua gan nhưng thải trừ qua hệ thống reticuloendothelial.",
            },
            "reversal_agents": {
                "available": False,
                "agents": [],
                "notes": "Không có thuốc giải độc đặc hiệu. Half-life rất dài (17-20 ngày), tác dụng sẽ giảm dần theo thời gian.",
            },
        },

        "Evolocumab": {
            "contraindications_detail": {
                "tuyệt_đối": ['Dị ứng với evolocumab hoặc bất kỳ thành phần nào', 'Dị ứng với protein tái tổ hợp'],
                "tương_đối": ['Suy gan nặng - chưa có dữ liệu đầy đủ', 'Suy thận nặng - không cần chỉnh liều nhưng thận trọng'],
            },
            "renal_adjustment": {
                "normal": "Không đổi liều",
                "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
                "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
                "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
            },
            "hepatic_adjustment": {
                "mild": "Không cần chỉnh liều.",
                "moderate": "Thận trọng, chưa có dữ liệu đầy đủ.",
                "severe": "Thiếu dữ liệu; cân nhắc thuốc khác nếu có thể.",
                "notes": "Evolocumab là monoclonal antibody, không chuyển hóa qua gan nhưng thải trừ qua hệ thống reticuloendothelial.",
            },
            "reversal_agents": {
                "available": False,
                "agents": [],
                "notes": "Không có thuốc giải độc đặc hiệu. Half-life rất dài (11-17 ngày), tác dụng sẽ giảm dần theo thời gian.",
            },
        },

        "Inclisiran": {
            "contraindications_detail": {
                "tuyệt_đối": ['Dị ứng với inclisiran hoặc bất kỳ thành phần nào'],
                "tương_đối": ['Suy gan nặng - chưa có dữ liệu đầy đủ', 'Suy thận nặng - không cần chỉnh liều nhưng thận trọng'],
            },
            "renal_adjustment": {
                "normal": "Không đổi liều",
                "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
                "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
                "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
            },
            "hepatic_adjustment": {
                "mild": "Không cần chỉnh liều.",
                "moderate": "Thận trọng, chưa có dữ liệu đầy đủ.",
                "severe": "Thiếu dữ liệu; cân nhắc thuốc khác nếu có thể.",
                "notes": "Inclisiran là siRNA, không chuyển hóa qua gan nhưng thải trừ qua hệ thống nội bào.",
            },
            "reversal_agents": {
                "available": False,
                "agents": [],
                "notes": "Không có thuốc giải độc đặc hiệu. Tác dụng kéo dài 6 tháng sau liều thứ 2.",
            },
        },

        "Sitagliptin": {
            "black_box_warnings": None,
            "contraindications_detail": {
                "tuyệt_đối": ['Đái tháo đường type 1', 'Nhiễm toan ceton do đái tháo đường', 'Dị ứng sitagliptin', 'Viêm tụy cấp đang diễn ra'],
                "tương_đối": ['Suy thận nặng (CrCl <30) - cần giảm liều (25mg/ngày)', 'Suy thận trung bình (CrCl 30-50) - cần giảm liều (50mg/ngày)', 'Tiền sử viêm tụy cấp - tăng nguy cơ', 'Tiền sử suy tim - tăng nhẹ nguy cơ suy tim', 'Đau khớp nghiêm trọng - ngừng thuốc nếu xảy ra'],
            },
        },

        "Linagliptin": {
            "black_box_warnings": None,
            "contraindications_detail": {
                "tuyệt_đối": ['Đái tháo đường type 1', 'Nhiễm toan ceton do đái tháo đường', 'Dị ứng linagliptin hoặc DPP-4 inhibitor'],
                "tương_đối": ['Suy thận - không cần điều chỉnh liều (ưu điểm)', 'Suy gan - thận trọng', 'Có thai - category B, an toàn'],
            },
        },

        "Saxagliptin": {
            "black_box_warnings": None,
            "contraindications_detail": {
                "tuyệt_đối": ['Đái tháo đường type 1', 'Nhiễm toan ceton do đái tháo đường', 'Dị ứng saxagliptin hoặc DPP-4 inhibitor'],
                "tương_đối": ['Suy thận - cần điều chỉnh liều (CrCl ≤50 → 2.5mg/ngày)', 'Suy gan - thận trọng', 'Có thai - category B, an toàn'],
            },
        },

        "Alogliptin": {
            "black_box_warnings": None,
            "contraindications_detail": {
                "tuyệt_đối": ['Đái tháo đường type 1', 'Nhiễm toan ceton do đái tháo đường', 'Dị ứng alogliptin hoặc DPP-4 inhibitor'],
                "tương_đối": ['Suy thận - cần điều chỉnh liều (CrCl 30-60 → 12.5mg/ngày, CrCl <30 → 6.25mg/ngày)', 'Suy gan - thận trọng', 'Có thai - category B, an toàn'],
            },
        },

        "Insulin": {
            "contraindications_detail": {
                "tuyệt_đối": ['Hạ đường huyết (hypoglycemia) - không được dùng khi đường huyết thấp', 'Dị ứng insulin hoặc bất kỳ thành phần nào trong chế phẩm insulin', 'Hôn mê do hạ đường huyết - không được dùng insulin cho đến khi hồi phục'],
                "tương_đối": ['Suy thận - giảm clearance insulin, giảm liều insulin', 'Suy gan - giảm gluconeogenesis, tăng nguy cơ hạ đường huyết, giảm liều insulin', 'Suy tim - thận trọng, có thể cần điều chỉnh liều', 'Người cao tuổi - tăng nguy cơ hạ đường huyết, cần liều thấp hơn', 'Bệnh nhân không có khả năng tự quản lý - cần người chăm sóc', 'Bệnh nhân không có khả năng nhận biết hạ đường huyết - tăng nguy cơ', 'Thai kỳ - điều chỉnh liều thường xuyên (tăng nhu cầu trong tam cá nguyệt 2-3)'],
            },
            "renal_adjustment": {
                "normal": "Không đổi liều",
                "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
                "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
                "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
            },
        },

        "Empagliflozin": {
            "black_box_warnings": None,
            "contraindications_detail": {
                "tuyệt_đối": ['Đái tháo đường type 1', 'Nhiễm toan ceton do đái tháo đường', 'Suy thận nặng (eGFR <20)', 'Đang lọc máu', 'Dị ứng empagliflozin'],
                "tương_đối": ['Nhiễm trùng đường tiết niệu tái phát - tăng nguy cơ nhiễm trùng', 'Suy tim nặng - tăng nguy cơ mất nước', 'Người cao tuổi - tăng nguy cơ mất nước, hạ huyết áp', 'Dùng diuretics - tăng nguy cơ mất nước', 'Nhiễm trùng đường sinh dục tái phát - tăng nguy cơ nhiễm trùng'],
            },
        },

        "Dapagliflozin": {
            "black_box_warnings": None,
            "contraindications_detail": {
                "tuyệt_đối": ['Đái tháo đường type 1', 'Nhiễm toan ceton do đái tháo đường', 'Suy thận nặng (eGFR <25)', 'Đang lọc máu', 'Dị ứng dapagliflozin'],
                "tương_đối": ['Nhiễm trùng đường tiết niệu tái phát - tăng nguy cơ nhiễm trùng', 'Suy tim nặng - tăng nguy cơ mất nước', 'Người cao tuổi - tăng nguy cơ mất nước, hạ huyết áp', 'Dùng diuretics - tăng nguy cơ mất nước', 'Nhiễm trùng đường sinh dục tái phát - tăng nguy cơ nhiễm trùng'],
            },
        },

        "Glibenclamide": {
            "contraindications_detail": {
                "tuyệt_đối": ['Đái tháo đường type 1', 'Nhiễm toan ceton do đái tháo đường', 'Dị ứng glibenclamide hoặc sulfonylurea', 'Suy thận nặng (CrCl <30) - tăng nguy cơ hạ đường huyết nghiêm trọng'],
                "tương_đối": ['Suy gan nặng - tăng nguy cơ hạ đường huyết', 'Người cao tuổi - tăng nguy cơ hạ đường huyết', 'Suy thận trung bình (CrCl 30-60) - giảm liều, theo dõi sát', 'Có thai - có thể gây hạ đường huyết ở trẻ sơ sinh', 'Bỏ bữa thường xuyên - tăng nguy cơ hạ đường huyết', 'Uống rượu - tăng nguy cơ hạ đường huyết nghiêm trọng', 'Dùng beta-blocker - che dấu triệu chứng hạ đường huyết'],
            },
            "renal_adjustment": {
                "normal": "Không đổi liều",
                "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
                "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
                "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
            },
        },

        "Gliclazide": {
            "contraindications_detail": {
                "tuyệt_đối": ['Đái tháo đường type 1', 'Nhiễm toan ceton do đái tháo đường', 'Dị ứng gliclazide hoặc sulfonylurea', 'Suy thận nặng (CrCl <30) - tăng nguy cơ hạ đường huyết'],
                "tương_đối": ['Suy gan nặng - tăng nguy cơ hạ đường huyết', 'Người cao tuổi - tăng nguy cơ hạ đường huyết', 'Suy thận trung bình (CrCl 30-60) - giảm liều, theo dõi sát', 'Có thai - có thể gây hạ đường huyết ở trẻ sơ sinh', 'Bỏ bữa thường xuyên - tăng nguy cơ hạ đường huyết', 'Uống rượu - tăng nguy cơ hạ đường huyết'],
            },
            "renal_adjustment": {
                "normal": "Không đổi liều",
                "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
                "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
                "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
            },
        },

        "Acarbose": {
            "black_box_warnings": None,
            "contraindications_detail": {
                "tuyệt_đối": ['Đái tháo đường type 1', 'Nhiễm toan ceton do đái tháo đường', 'Bệnh viêm ruột (Crohn, viêm loét đại tràng)', 'Tắc ruột', 'Suy gan nặng', 'Suy thận nặng (CrCl <25) - CHỐNG CHỈ ĐỊNH', 'Dị ứng acarbose'],
                "tương_đối": ['Suy thận trung bình (CrCl 25-60) - thận trọng, có thể cần giảm liều', 'Suy gan nhẹ-trung bình - thận trọng', 'Có thai - category B, an toàn'],
            },
        },

        "Miglitol": {
            "black_box_warnings": None,
            "contraindications_detail": {
                "tuyệt_đối": ['Đái tháo đường type 1', 'Nhiễm toan ceton do đái tháo đường', 'Bệnh viêm ruột (Crohn, viêm loét đại tràng)', 'Tắc ruột', 'Suy thận nặng (CrCl <25) - CHỐNG CHỈ ĐỊNH', 'Dị ứng miglitol'],
                "tương_đối": ['Suy thận trung bình (CrCl 25-60) - thận trọng, có thể cần giảm liều', 'Có thai - category B, an toàn'],
            },
        },

        "Loperamide": {
            "contraindications_detail": {
                "tuyệt_đối": ['Dị ứng loperamide', 'Tiêu chảy nhiễm khuẩn nặng (C. difficile, E. coli O157:H7) - có thể giữ vi khuẩn trong ruột', 'Viêm đại tràng giả mạc - có thể làm nặng thêm', 'Tắc ruột cơ học', 'Trẻ em <2 tuổi - nguy cơ ức chế hô hấp', 'Liều cao với CYP3A4 inhibitors - CHỐNG CHỈ ĐỊNH'],
                "tương_đối": ['Suy gan nặng - giảm liều, tăng nguy cơ tích lũy', 'Suy thận nặng - giảm liều, tăng nguy cơ tích lũy', 'Tiêu chảy nhiễm khuẩn nhẹ - thận trọng, đã điều trị kháng sinh', 'Trẻ em 2-6 tuổi - thận trọng, giảm liều', 'Đang dùng opioids - tăng nguy cơ tác dụng phụ'],
            },
            "renal_adjustment": {
                "normal": "Không đổi liều",
                "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
                "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
                "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
            },
        },

        "Bismuth subsalicylate": {
            "contraindications_detail": {
                "tuyệt_đối": ['Dị ứng aspirin hoặc salicylates', 'Trẻ em <12 tuổi - nguy cơ hội chứng Reye (nguy hiểm tính mạng)', 'Dùng aspirin hoặc thuốc chống đông (warfarin) - tăng nguy cơ chảy máu nghiêm trọng', 'Suy thận nặng - tích lũy bismuth và salicylate'],
                "tương_đối": ['Suy thận nhẹ đến trung bình - thận trọng, tích lũy bismuth và salicylate', 'Loét dạ dày - salicylate có thể kích ứng', 'Mang thai - salicylate có thể ảnh hưởng thai nhi', 'Dùng với tetracycline, quinolone - giảm hấp thu, cần cách xa 2 giờ'],
            },
            "renal_adjustment": {
                "normal": "Không đổi liều",
                "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
                "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
                "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
            },
        },

        "Cimetidine": {
            "contraindications_detail": {
                "tuyệt_đối": ['Dị ứng cimetidine hoặc H2 blocker khác'],
                "tương_đối": ['Suy thận nặng (CrCl <30) - cần giảm liều 75%', 'Suy gan nặng - thận trọng', 'Người già - tăng nguy cơ lú lẫn', 'Dùng với warfarin, theophylline, phenytoin, lidocaine - tăng nguy cơ độc tính', 'Nhiễm C. difficile - tăng nguy cơ nhẹ'],
            },
            "reversal_agents": {
                "available": False,
                "agents": [],
                "notes": "Không có thuốc giải độc đặc hiệu; điều trị hỗ trợ triệu chứng.",
            },
        },

        "Sucralfate": {
            "contraindications_detail": {
                "tuyệt_đối": ['Dị ứng sucralfate', 'Suy thận nặng (CrCl <30) - CHỐNG CHỈ ĐỊNH do tích tụ nhôm'],
                "tương_đối": ['Suy thận trung bình (CrCl 30-60) - thận trọng, giảm liều, theo dõi chức năng thận', 'Táo bón nặng - có thể làm nặng thêm', 'Đang dùng nhiều thuốc - tăng nguy cơ tương tác hấp thu'],
            },
            "reversal_agents": {
                "available": False,
                "agents": [],
                "notes": "Không có thuốc giải độc đặc hiệu; điều trị hỗ trợ triệu chứng.",
            },
        },

        "Lansoprazole": {
            "contraindications_detail": {
                "tuyệt_đối": ['Dị ứng lansoprazole hoặc PPI khác', 'Dùng cùng atazanavir (HIV protease inhibitor)'],
                "tương_đối": ['Suy gan nặng (Child-Pugh C) - giảm liều tối đa 15mg/ngày', 'Suy thận nặng (CrCl <30) - không cần chỉnh liều nhưng thận trọng', 'Loãng xương - tăng nguy cơ gãy xương khi dùng lâu dài', 'Nhiễm C. difficile - tăng nguy cơ', 'Thiếu vitamin B12 - bổ sung nếu dùng lâu dài', 'Thiếu magnesium - bổ sung nếu dùng lâu dài'],
            },
            "reversal_agents": {
                "available": False,
                "agents": [],
                "notes": "Không có thuốc giải độc đặc hiệu; điều trị hỗ trợ triệu chứng.",
            },
        },

        "Esomeprazole": {
            "contraindications_detail": {
                "tuyệt_đối": ['Dị ứng esomeprazole hoặc PPI khác', 'Dùng cùng atazanavir (HIV protease inhibitor)'],
                "tương_đối": ['Suy gan nặng (Child-Pugh C) - giảm liều tối đa 20mg/ngày', 'Suy thận nặng (CrCl <30) - không cần chỉnh liều nhưng thận trọng', 'Loãng xương - tăng nguy cơ gãy xương khi dùng lâu dài', 'Nhiễm C. difficile - tăng nguy cơ', 'Thiếu vitamin B12 - bổ sung nếu dùng lâu dài', 'Thiếu magnesium - bổ sung nếu dùng lâu dài'],
            },
            "reversal_agents": {
                "available": False,
                "agents": [],
                "notes": "Không có thuốc giải độc đặc hiệu; điều trị hỗ trợ triệu chứng.",
            },
        },

        "Metoclopramide": {
            "contraindications_detail": {
                "tuyệt_đối": ['Dị ứng metoclopramide', 'Tắc ruột cơ học', 'Xuất huyết tiêu hóa', 'Thủng dạ dày-ruột', 'Pheochromocytoma (tăng nguy cơ tăng huyết áp)', 'Rối loạn vận động (Parkinson, dystonia, tardive dyskinesia)'],
                "tương_đối": ['Suy thận (CrCl <30) - giảm liều 50-75%', 'Suy gan nặng - thận trọng, có thể giảm liều', 'Trẻ em và thanh niên - tăng nguy cơ dystonia, parkinsonism', 'Epilepsy - có thể làm nặng co giật', 'Đang dùng SSRI/SNRI - tăng nguy cơ hội chứng serotonin', 'Đang dùng antipsychotics - tăng nguy cơ rối loạn vận động'],
            },
            "reversal_agents": {
                "available": False,
                "agents": [],
                "notes": "Không có thuốc giải độc đặc hiệu; điều trị hỗ trợ triệu chứng.",
            },
        },

        "Domperidone": {
            "contraindications_detail": {
                "tuyệt_đối": ['Dị ứng domperidone', 'Chảy máu dạ dày', 'Tắc ruột cơ học', 'Prolactinoma', 'Dùng với các thuốc kéo dài QT - CHỐNG CHỈ ĐỊNH tuyệt đối', 'QT kéo dài (QTc >450ms ở nam, >470ms ở nữ) - CHỐNG CHỈ ĐỊNH'],
                "tương_đối": ['Suy thận nặng (CrCl <30) - giảm liều 50%', 'Suy gan nặng - giảm liều, tăng nguy cơ QT kéo dài', 'Hạ kali, hạ magie - tăng nguy cơ QT kéo dài', 'Người già - thận trọng, giảm liều', 'Rối loạn nhịp tim - thận trọng'],
            },
            "reversal_agents": {
                "available": False,
                "agents": [],
                "notes": "Không có thuốc giải độc đặc hiệu; điều trị hỗ trợ triệu chứng.",
            },
        },

        "Ondansetron": {
            "contraindications_detail": {
                "tuyệt_đối": ['Dị ứng ondansetron', 'Dùng với apomorphine - CHỐNG CHỈ ĐỊNH tuyệt đối', 'QT kéo dài (QTc >450ms ở nam, >470ms ở nữ) - CHỐNG CHỈ ĐỊNH'],
                "tương_đối": ['Suy gan nặng - giảm liều 50% (tối đa 8mg/ngày)', 'Hạ kali, hạ magie - tăng nguy cơ QT kéo dài, bổ sung trước khi dùng', 'Đang dùng thuốc kéo dài QT - thận trọng, giảm liều', 'Người già - thận trọng, giảm liều', 'Rối loạn nhịp tim - thận trọng'],
            },
            "reversal_agents": {
                "available": False,
                "agents": [],
                "notes": "Không có thuốc giải độc đặc hiệu; điều trị hỗ trợ triệu chứng.",
            },
        },

        "Vonoprazan": {
            "contraindications_detail": {
                "tuyệt_đối": ['Dị ứng vonoprazan hoặc PCAB'],
                "tương_đối": ['Suy gan nặng', 'Loãng xương'],
            },
            "renal_adjustment": {
                "normal": "Không đổi liều",
                "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
                "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
                "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
            },
            "hepatic_adjustment": {
                "mild": "Không cần chỉnh liều.",
                "moderate": "Thận trọng.",
                "severe": "Thận trọng, có thể giảm liều.",
                "notes": "Vonoprazan chuyển hóa qua gan.",
            },
            "reversal_agents": {
                "available": False,
                "agents": [],
                "notes": "Không có thuốc giải độc đặc hiệu.",
            },
        },

        "Tegoprazan": {
            "contraindications_detail": {
                "tuyệt_đối": ['Dị ứng tegoprazan hoặc PCAB'],
                "tương_đối": ['Suy gan nặng', 'Loãng xương'],
            },
            "renal_adjustment": {
                "normal": "Không đổi liều",
                "30_60": "Có thể cần giảm liều, theo dõi chức năng thận",
                "under_30": "Giảm liều hoặc tránh dùng nếu có lựa chọn khác",
                "hemodialysis": "Có thể cần bổ sung sau lọc máu (tùy thuốc)",
            },
            "hepatic_adjustment": {
                "mild": "Không cần chỉnh liều.",
                "moderate": "Thận trọng.",
                "severe": "Thận trọng, có thể giảm liều.",
                "notes": "Tegoprazan chuyển hóa qua gan.",
            },
            "reversal_agents": {
                "available": False,
                "agents": [],
                "notes": "Không có thuốc giải độc đặc hiệu.",
            },
        },

        "Lactulose": {
            "black_box_warnings": None,
            "drug_interactions": {
                "major": [],
                "moderate": [],
                "minor": [],
            },
        },

        "Polyethylene glycol 3350": {
            "black_box_warnings": None,
            "drug_interactions": {
                "major": [],
                "moderate": [],
                "minor": [],
            },
        },

        "Istradefylline": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với istradefylline hoặc bất kỳ thành phần nào",
                ],
                "tương_đối": [
                    "Suy gan vừa-nặng - thận trọng",
                    "Suy thận nặng (CrCl <30) - thận trọng",
                    "Bệnh nhân cao tuổi - tăng nguy cơ tác dụng phụ",
                ],
            },
            "reversal_agents": {
                "available": False,
                "agents": [],
                "notes": "Không có thuốc giải độc đặc hiệu. Xử trí quá liều chủ yếu là hỗ trợ triệu chứng và ngừng thuốc.",
            },
        },

        "Lamotrigine": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với lamotrigine",
                ],
                "tương_đối": [
                    "Suy thận nặng (CrCl <30) - thận trọng, có thể cần giảm liều",
                    "Suy gan vừa-nặng - cần giảm liều",
                    "Có thai - thận trọng, cân nhắc lợi ích/nguy cơ",
                    "Đang cho con bú - thận trọng",
                    "Tiền sử phát ban nặng do thuốc",
                ],
            },
            "renal_adjustment": {
                "normal": "Không đổi liều",
                "30_60": "Không đổi liều",
                "under_30": "Thận trọng, có thể cần giảm liều",
                "hemodialysis": "Có thể cần bổ sung liều sau mỗi lần lọc máu",
            },
        },

        "Levetiracetam": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với levetiracetam hoặc bất kỳ thành phần nào",
                ],
                "tương_đối": [
                    "Suy thận nặng (CrCl <30) - cần giảm liều",
                    "Suy gan nặng - thận trọng",
                    "Bệnh nhân cao tuổi - tăng nguy cơ tác dụng phụ",
                    "Có thai - thận trọng",
                    "Đang cho con bú - thận trọng",
                    "Tiền sử rối loạn tâm thần - tăng nguy cơ kích động, trầm cảm",
                ],
            },
            "reversal_agents": {
                "available": False,
                "agents": [],
                "notes": "Không có thuốc giải độc đặc hiệu. Xử trí quá liều chủ yếu là hỗ trợ triệu chứng và ngừng thuốc.",
            },
        },

        "Levodopa/Carbidopa": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với levodopa, carbidopa hoặc bất kỳ thành phần nào",
                    "Đang dùng hoặc đã dùng MAO inhibitor không chọn lọc trong vòng 14 ngày",
                    "Glaucoma góc đóng không được điều trị",
                ],
                "tương_đối": [
                    "Suy thận nặng (CrCl <30) - thận trọng",
                    "Suy gan vừa-nặng - thận trọng",
                    "Bệnh tim mạch - thận trọng, có thể gây rối loạn nhịp tim",
                    "Loét dạ dày tá tràng - thận trọng",
                    "Tiền sử rối loạn tâm thần - tăng nguy cơ ảo giác, rối loạn tâm thần",
                    "Có thai - thận trọng",
                    "Đang cho con bú - thận trọng",
                ],
            },
            "renal_adjustment": {
                "normal": "Không đổi liều",
                "30_60": "Không đổi liều",
                "under_30": "Thận trọng, có thể cần giảm liều",
                "hemodialysis": "Không đổi liều",
            },
        },

        "Lorazepam": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với lorazepam hoặc benzodiazepine",
                    "Bệnh nhược cơ nặng",
                    "Hội chứng ngưng thở khi ngủ nặng",
                    "Suy hô hấp nặng",
                ],
                "tương_đối": [
                    "Suy thận nặng (CrCl <30) - thận trọng",
                    "Suy gan vừa-nặng - cần giảm liều",
                    "Bệnh nhân cao tuổi - tăng nguy cơ tác dụng phụ, giảm liều",
                    "Có thai - tránh dùng trong tam cá nguyệt đầu, thận trọng sau đó",
                    "Đang cho con bú - thận trọng",
                    "Tiền sử lạm dụng chất",
                    "Trầm cảm nặng - có thể tăng nguy cơ tự tử",
                ],
            },
            "renal_adjustment": {
                "normal": "Không đổi liều",
                "30_60": "Không đổi liều",
                "under_30": "Thận trọng, có thể tích tụ",
                "hemodialysis": "Không đổi liều",
            },
        },

        "Memantine": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với memantine hoặc bất kỳ thành phần nào",
                ],
                "tương_đối": [
                    "Suy thận nặng (CrCl <30) - cần giảm liều",
                    "Suy gan vừa-nặng - thận trọng",
                    "Rối loạn nhịp tim, block nhĩ thất",
                    "Động kinh hoặc tiền sử động kinh",
                    "Có thai - thận trọng",
                    "Đang cho con bú - thận trọng",
                ],
            },
            "renal_adjustment": {
                "normal": "Không đổi liều",
                "30_60": "Giảm liều 50%",
                "under_30": "Giảm liều 50%",
                "hemodialysis": "Không đổi liều",
            },
        },

        "Opicapone": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với opicapone hoặc bất kỳ thành phần nào",
                    "Pheochromocytoma",
                    "Đang dùng non-selective MAO inhibitor",
                ],
                "tương_đối": [
                    "Suy gan vừa-nặng - thận trọng",
                    "Suy thận nặng (CrCl <30) - thận trọng",
                    "Rối loạn nhịp tim",
                    "Có thai - thận trọng",
                    "Đang cho con bú - thận trọng",
                ],
            },
            "reversal_agents": {
                "available": False,
                "agents": [],
                "notes": "Không có thuốc giải độc đặc hiệu. Xử trí quá liều chủ yếu là hỗ trợ triệu chứng và ngừng thuốc.",
            },
        },

        "Phenobarbital": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với phenobarbital hoặc barbiturate",
                    "Porphyria cấp tính",
                    "Suy hô hấp nặng",
                ],
                "tương_đối": [
                    "Suy thận nặng (CrCl <30) - thận trọng",
                    "Suy gan vừa-nặng - cần giảm liều",
                    "Bệnh nhân cao tuổi - tăng nguy cơ tác dụng phụ, giảm liều",
                    "Có thai - thận trọng, có thể gây dị tật bẩm sinh",
                    "Đang cho con bú - thận trọng",
                    "Tiền sử lạm dụng chất",
                    "Trầm cảm nặng - có thể tăng nguy cơ tự tử",
                ],
            },
            "reversal_agents": {
                "available": False,
                "agents": [],
                "notes": "Không có thuốc giải độc đặc hiệu. Xử trí quá liều chủ yếu là hỗ trợ hô hấp, huyết động và ngừng thuốc.",
            },
        },

        "Phenytoin": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với phenytoin hoặc bất kỳ thành phần nào",
                ],
                "tương_đối": [
                    "Suy thận nặng (CrCl <30) - thận trọng",
                    "Suy gan vừa-nặng - cần giảm liều",
                    "Bệnh nhân cao tuổi - tăng nguy cơ tác dụng phụ",
                    "Có thai - thận trọng, có thể gây dị tật bẩm sinh",
                    "Đang cho con bú - thận trọng",
                    "Rối loạn nhịp tim, block nhĩ thất",
                    "Tiền sử phát ban nặng do thuốc",
                ],
            },
            "reversal_agents": {
                "available": False,
                "agents": [],
                "notes": "Không có thuốc giải độc đặc hiệu. Xử trí quá liều chủ yếu là hỗ trợ triệu chứng, theo dõi nồng độ trong máu và ngừng thuốc.",
            },
        },

        "Piracetam": {
            "black_box_warnings": None,
            "reversal_agents": {
                "available": False,
                "agents": [],
                "notes": "Không có thuốc giải độc đặc hiệu. Xử trí quá liều chủ yếu là hỗ trợ triệu chứng.",
            },
        },

        "Pregabalin": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với pregabalin hoặc bất kỳ thành phần nào",
                ],
                "tương_đối": [
                    "Suy thận nặng (CrCl <30) - cần giảm liều",
                    "Suy gan vừa-nặng - thận trọng",
                    "Bệnh nhân cao tuổi - tăng nguy cơ tác dụng phụ",
                    "Có thai - thận trọng",
                    "Đang cho con bú - thận trọng",
                    "Tiền sử lạm dụng chất - có nguy cơ nghiện",
                    "Suy tim sung huyết - thận trọng",
                ],
            },
            "reversal_agents": {
                "available": False,
                "agents": [],
                "notes": "Không có thuốc giải độc đặc hiệu. Xử trí quá liều chủ yếu là hỗ trợ triệu chứng và ngừng thuốc.",
            },
        },

        "Rimegepant": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với rimegepant hoặc bất kỳ thành phần nào",
                    "Đang dùng thuốc ức chế CYP3A4 mạnh (ketoconazole, itraconazole, clarithromycin) - CHỐNG CHỈ ĐỊNH tuyệt đối",
                ],
                "tương_đối": [
                    "Suy gan vừa-nặng - thận trọng, có thể cần giảm liều",
                    "Suy thận nặng (CrCl <30) - thận trọng",
                    "Bệnh tim mạch - thận trọng",
                    "Có thai - thận trọng",
                    "Đang cho con bú - thận trọng",
                ],
            },
            "reversal_agents": {
                "available": False,
                "agents": [],
                "notes": "Không có thuốc giải độc đặc hiệu. Xử trí quá liều chủ yếu là hỗ trợ triệu chứng và ngừng thuốc.",
            },
        },

        "Rivastigmine": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với rivastigmine hoặc bất kỳ thành phần nào",
                ],
                "tương_đối": [
                    "Suy thận nặng (CrCl <30) - thận trọng",
                    "Suy gan vừa-nặng - thận trọng",
                    "Rối loạn nhịp tim, block nhĩ thất",
                    "Bệnh phổi tắc nghẽn mạn tính (COPD) nặng",
                    "Động kinh hoặc tiền sử động kinh",
                    "Loét dạ dày tá tràng - thận trọng",
                ],
            },
            "renal_adjustment": {
                "normal": "Không đổi liều",
                "30_60": "Không đổi liều",
                "under_30": "Thận trọng, có thể cần giảm liều",
                "hemodialysis": "Không đổi liều",
            },
        },

        "Ropinirole": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với ropinirole hoặc bất kỳ thành phần nào",
                ],
                "tương_đối": [
                    "Suy thận nặng (CrCl <30) - thận trọng",
                    "Suy gan vừa-nặng - thận trọng",
                    "Hạ huyết áp tư thế - thận trọng",
                    "Rối loạn nhịp tim",
                    "Tiền sử rối loạn tâm thần - tăng nguy cơ ảo giác, rối loạn tâm thần",
                    "Buồn ngủ ban ngày quá mức, rối loạn giấc ngủ",
                    "Có thai - thận trọng",
                    "Đang cho con bú - thận trọng",
                ],
            },
            "renal_adjustment": {
                "normal": "Không đổi liều",
                "30_60": "Không đổi liều",
                "under_30": "Thận trọng, có thể cần giảm liều",
                "hemodialysis": "Không đổi liều",
            },
        },

        "Tizanidine": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với tizanidine hoặc bất kỳ thành phần nào",
                ],
                "tương_đối": [
                    "Suy thận nặng (CrCl <30) - cần giảm liều",
                    "Suy gan vừa-nặng - cần giảm liều",
                    "Bệnh nhân cao tuổi - tăng nguy cơ tác dụng phụ, giảm liều",
                    "Hạ huyết áp - thận trọng",
                    "Có thai - thận trọng",
                    "Đang cho con bú - thận trọng",
                ],
            },
            "renal_adjustment": {
                "normal": "Không đổi liều",
                "30_60": "Không đổi liều",
                "under_30": "Giảm liều, thận trọng",
                "hemodialysis": "Không đổi liều",
            },
        },

        "Topiramate": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với topiramate hoặc bất kỳ thành phần nào",
                ],
                "tương_đối": [
                    "Suy thận nặng (CrCl <30) - cần giảm liều",
                    "Suy gan vừa-nặng - thận trọng",
                    "Sỏi thận - tăng nguy cơ sỏi thận",
                    "Tăng nhãn áp - thận trọng",
                    "Có thai - thận trọng, có thể gây dị tật bẩm sinh",
                    "Đang cho con bú - thận trọng",
                    "Rối loạn chuyển hóa acid-base",
                ],
            },
            "renal_adjustment": {
                "normal": "Không đổi liều",
                "30_60": "Không đổi liều",
                "under_30": "Giảm liều 50%",
                "hemodialysis": "Có thể cần bổ sung liều sau mỗi lần lọc máu",
            },
        },

        "Ubrogepant": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với ubrogepant hoặc bất kỳ thành phần nào",
                    "Đang dùng thuốc ức chế CYP3A4 mạnh (ketoconazole, itraconazole, clarithromycin) - CHỐNG CHỈ ĐỊNH tuyệt đối",
                ],
                "tương_đối": [
                    "Suy gan vừa-nặng - thận trọng, có thể cần giảm liều",
                    "Suy thận nặng (CrCl <30) - thận trọng",
                    "Bệnh tim mạch - thận trọng",
                    "Có thai - thận trọng",
                    "Đang cho con bú - thận trọng",
                ],
            },
            "reversal_agents": {
                "available": False,
                "agents": [],
                "notes": "Không có thuốc giải độc đặc hiệu. Xử trí quá liều chủ yếu là hỗ trợ triệu chứng và ngừng thuốc.",
            },
        },

        "Valproate": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với valproate hoặc bất kỳ thành phần nào",
                    "Bệnh gan nặng hoặc rối loạn chức năng gan nặng",
                    "Rối loạn chu trình urea",
                    "Bệnh ty thể (mitochondrial disease)",
                ],
                "tương_đối": [
                    "Suy thận nặng (CrCl <30) - thận trọng, có thể cần giảm liều",
                    "Suy gan vừa - thận trọng, theo dõi chức năng gan sát",
                    "Có thai - thận trọng, có thể gây dị tật bẩm sinh và giảm IQ ở trẻ",
                    "Đang cho con bú - thận trọng",
                    "Rối loạn đông máu - tăng nguy cơ chảy máu",
                    "Tiền sử viêm tụy - tăng nguy cơ viêm tụy",
                ],
            },
            "renal_adjustment": {
                "normal": "Không đổi liều",
                "30_60": "Không đổi liều",
                "under_30": "Thận trọng, có thể cần giảm liều",
                "hemodialysis": "Có thể cần bổ sung liều sau mỗi lần lọc máu",
            },
        },

        "Vinpocetine": {
            "black_box_warnings": None,
            "reversal_agents": {
                "available": False,
                "agents": [],
                "notes": "Không có thuốc giải độc đặc hiệu. Xử trí quá liều chủ yếu là hỗ trợ triệu chứng.",
            },
        },

    # ======================== END BATCH 2 ========================
        "Abaloparatide": {
            "interactions": ['Chưa có báo cáo tương tác thuốc đáng kể'],
        },

        "Alirocumab": {
            "overdose_management": {
                "symptoms": ['Cần đánh giá lâm sàng'],
                "antidote": 'Không có antidote đặc hiệu',
                "treatment": ['Chưa có báo cáo quá liều. Nếu tiêm quá liều, theo dõi các tác dụng phụ và điều trị hỗ trợ.'],
                "monitoring": 'Theo dõi dấu hiệu sinh tồn và triệu chứng',
            },
            "administration_instructions": {
                "oral": {
                    "with_food": 'Tiêm dưới da (bụng, đùi, hoặc cánh tay). Để ở nhiệt độ phòng 30 phút trước khi tiêm. Không lắc. Luân phiên vị trí tiêm. Có thể tự tiêm sau khi được hướng dẫn.',
                    "timing": 'Theo chỉ định của bác sĩ',
                },
                "iv": {
                    "reconstitution": 'N/A',
                    "infusion_rate": 'N/A',
                    "compatibility": [],
                    "incompatibility": [],
                    "notes": 'N/A',
                },
            },
        },

        "Amlodipine/Olmesartan": {
            "interactions": ['Chưa có báo cáo tương tác thuốc đáng kể'],
        },

        "Calcitonin": {
            "interactions": ['Chưa có báo cáo tương tác thuốc đáng kể'],
        },

        "Enalapril": {
            "guideline_tags": ['C09AA02', '24.08.08 ACE Inhibitors', 'vietnam_essential_medicines: True', {'source': 'ESC 2021 Heart Failure', 'recommendation': 'ACE inhibitor first-line therapy for HFrEF if tolerated', 'context': 'Heart failure with reduced ejection fraction (HFrEF), NYHA II–III'}, {'source': 'ACC/AHA 2017 Hypertension Guideline', 'recommendation': 'One of the first-line options for hypertension', 'context': 'Primary hypertension, non-black, with or without diabetes'}, {'source': 'BYT – Hướng dẫn chẩn đoán và điều trị tăng huyết áp 2020', 'recommendation': 'Một trong các lựa chọn hàng đầu điều trị tăng huyết áp', 'context': 'Tăng huyết áp nguyên phát không biến chứng, ưu tiên bệnh nhân có đái tháo đường hoặc bệnh thận mạn'}, 'first_line_htn', 'hfref_mortality_benefit', 'ckd_proteinuria_bp_control'],
        },

        "Evolocumab": {
            "overdose_management": {
                "symptoms": ['Cần đánh giá lâm sàng'],
                "antidote": 'Không có antidote đặc hiệu',
                "treatment": ['Chưa có báo cáo quá liều. Nếu tiêm quá liều, theo dõi các tác dụng phụ và điều trị hỗ trợ.'],
                "monitoring": 'Theo dõi dấu hiệu sinh tồn và triệu chứng',
            },
            "administration_instructions": {
                "oral": {
                    "with_food": 'Tiêm dưới da (bụng, đùi, hoặc cánh tay). Để ở nhiệt độ phòng 30 phút trước khi tiêm. Không lắc. Luân phiên vị trí tiêm. Có thể tự tiêm sau khi được hướng dẫn.',
                    "timing": 'Theo chỉ định của bác sĩ',
                },
                "iv": {
                    "reconstitution": 'N/A',
                    "infusion_rate": 'N/A',
                    "compatibility": [],
                    "incompatibility": [],
                    "notes": 'N/A',
                },
            },
        },

        "Inclisiran": {
            "overdose_management": {
                "symptoms": ['Cần đánh giá lâm sàng'],
                "antidote": 'Không có antidote đặc hiệu',
                "treatment": ['Chưa có báo cáo quá liều. Nếu tiêm quá liều, theo dõi các tác dụng phụ và điều trị hỗ trợ.'],
                "monitoring": 'Theo dõi dấu hiệu sinh tồn và triệu chứng',
            },
            "administration_instructions": {
                "oral": {
                    "with_food": 'Tiêm dưới da (bụng, đùi, hoặc cánh tay). Để ở nhiệt độ phòng 30 phút trước khi tiêm. Không lắc. Luân phiên vị trí tiêm. Có thể tự tiêm sau khi được hướng dẫn. Lịch tiêm: Liều đầu tiên, sau đó liều thứ 2 sau 3 tháng, sau đó mỗi 6 tháng.',
                    "timing": 'Theo chỉ định của bác sĩ',
                },
                "iv": {
                    "reconstitution": 'N/A',
                    "infusion_rate": 'N/A',
                    "compatibility": [],
                    "incompatibility": [],
                    "notes": 'N/A',
                },
            },
        },

        "Lisinopril": {
            "guideline_tags": ['C09AA03', '24.08.08 ACE Inhibitors', 'vietnam_essential_medicines: True', {'source': 'ESC 2021 Heart Failure', 'recommendation': 'ACE inhibitor first-line therapy for HFrEF if ARNI not available', 'context': 'Heart failure with reduced ejection fraction (HFrEF), NYHA II–III'}, {'source': 'BYT – Hướng dẫn chẩn đoán và điều trị suy tim 2015', 'recommendation': 'Thuốc nền tảng trong điều trị suy tim HFrEF cùng với beta-blocker và mineralocorticoid receptor antagonist', 'context': 'Suy tim mạn HFrEF, NYHA II–IV'}, 'first_line_htn', 'hfref_mortality_benefit'],
        },

        "Losartan": {
            "guideline_tags": ['C09CA01', '24.08.06 Angiotensin II Receptor Blockers', 'vietnam_essential_medicines: True', {'source': 'ACC/AHA 2017 Hypertension Guideline', 'recommendation': 'ARB as alternative first-line when ACE inhibitors not tolerated', 'context': 'Primary hypertension, ACE inhibitor intolerance (e.g. cough, angioedema)'}, {'source': 'BYT – Hướng dẫn chẩn đoán và điều trị tăng huyết áp 2020', 'recommendation': 'Lựa chọn khi không dung nạp ACEI hoặc cần bảo vệ thận', 'context': 'Tăng huyết áp có đái tháo đường hoặc bệnh thận mạn'}, 'first_line_htn_alt_acei', 'ckd_diabetic_nephropathy'],
        },

        "Metformin": {
            "guideline_tags": ['A10BA02', '68.20.08 Biguanides', 'vietnam_essential_medicines: True', {'source': 'ADA 2024 Standards of Care', 'recommendation': 'Initial pharmacologic therapy for most adults with type 2 diabetes', 'context': 'Type 2 diabetes without contraindications; often combined with lifestyle changes'}, {'source': 'BYT – Hướng dẫn chẩn đoán và điều trị đái tháo đường typ 2', 'recommendation': 'Thuốc đầu tay trong điều trị đái tháo đường typ 2 nếu không chống chỉ định', 'context': 'ĐTĐ typ 2, không suy thận nặng hoặc chống chỉ định khác'}, 'first_line_t2dm', 'weight_neutral_or_loss', 'low_hypoglycemia_risk'],
        },

        "Romosozumab": {
            "interactions": ['Chưa có báo cáo tương tác thuốc đáng kể'],
        },

        "Spironolactone": {
            "guideline_tags": ['C03DA01', '24.08.04 Aldosterone Antagonists', 'vietnam_essential_medicines: True', {'source': 'ESC 2021 Heart Failure', 'recommendation': 'Mineralocorticoid receptor antagonist to reduce mortality', 'context': 'HFrEF with persistent symptoms despite ACEI/ARB/ARNI and beta-blocker'}, 'hfref_mortality_benefit', 'hyperaldosteronism'],
        },

        "Tegoprazan": {
            "overdose_management": {
                "symptoms": ['Cần đánh giá lâm sàng'],
                "antidote": 'Không có antidote đặc hiệu',
                "treatment": ['Triệu chứng: Buồn nôn, nôn, đau bụng. Điều trị: Hỗ trợ, rửa dạ dày nếu mới uống.'],
                "monitoring": 'Theo dõi dấu hiệu sinh tồn và triệu chứng',
            },
            "administration_instructions": {
                "oral": {
                    "with_food": 'Uống với hoặc không có thức ăn. Nuốt nguyên viên, không nhai hoặc nghiền.',
                    "timing": 'Theo chỉ định của bác sĩ',
                },
                "iv": {
                    "reconstitution": 'N/A',
                    "infusion_rate": 'N/A',
                    "compatibility": [],
                    "incompatibility": [],
                    "notes": 'Chỉ có dạng uống',
                },
            },
        },

        "Vonoprazan": {
            "overdose_management": {
                "symptoms": ['Cần đánh giá lâm sàng'],
                "antidote": 'Không có antidote đặc hiệu',
                "treatment": ['Triệu chứng: Buồn nôn, nôn, đau bụng. Điều trị: Hỗ trợ, rửa dạ dày nếu mới uống. Không có chất đối kháng đặc hiệu.'],
                "monitoring": 'Theo dõi dấu hiệu sinh tồn và triệu chứng',
            },
            "administration_instructions": {
                "oral": {
                    "with_food": 'Uống với hoặc không có thức ăn. Không cần uống trước bữa ăn như PPI. Nuốt nguyên viên, không nhai hoặc nghiền.',
                    "timing": 'Theo chỉ định của bác sĩ',
                },
                "iv": {
                    "reconstitution": 'N/A',
                    "infusion_rate": 'N/A',
                    "compatibility": [],
                    "incompatibility": [],
                    "notes": 'Chỉ có dạng uống',
                },
            },
        },

    # ======================== BATCH 5: ENDOCRINE DRUGS ========================
        "Levothyroxine": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": True,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "cardiac": "High (cardiac events - angina, arrhythmias, myocardial infarction, cardiac failure - with over-replacement or in patients with cardiovascular disease, Black Box Warning)",
                    "endocrine": "High (thyrotoxicosis - with over-replacement)",
                    "skeletal": "Moderate (bone loss - with over-replacement in postmenopausal women)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "TSH levels - CRITICAL (target TSH 0.5-2.5 mIU/L, monitor 6-8 weeks after dose changes, then every 6-12 months)",
                    "Free T4 levels - CRITICAL (monitor with TSH, target upper half of normal range)",
                    "ECG - CRITICAL (if cardiac symptoms or in patients with cardiovascular disease, cardiac events risk with over-replacement, Black Box Warning)",
                    "Signs of cardiac events (chest pain, palpitations, dyspnea) - CRITICAL (with over-replacement or in patients with cardiovascular disease, Black Box Warning)",
                    "Signs of thyrotoxicosis (tachycardia, weight loss, heat intolerance, tremor) - CRITICAL (with over-replacement)",
                    "Start with low dose in elderly or cardiovascular disease - CRITICAL (Black Box Warning, increased risk of cardiac events)",
                    "Drug interactions (iron, calcium, antacids, PPIs, cholestyramine - separate by 4 hours) - CRITICAL (decrease absorption)",
                    "Pregnancy - CRITICAL (dose usually needs to be increased by 25-50%)"
                ],
                "look_alike_sound_alike": ["Levothyroxine", "Synthroid", "Levoxyl", "Liothyronine"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Cardiac Events (Angina, Arrhythmias, Myocardial Infarction, Cardiac Failure with Over-Replacement or in Cardiovascular Disease)",
                "ATA Guidelines - Hypothyroidism Treatment",
                "FDA Drug Label - Levothyroxine (Synthroid, Levoxyl)"
            ]
        },

        "Methimazole": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "hematologic": "High (agranulocytosis - rare but fatal, Black Box Warning)",
                    "hepatic": "High (hepatotoxicity - rare but serious, can be fatal)",
                    "dermatologic": "High (severe skin reactions - SJS/TEN - rare but fatal, Black Box Warning)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": True,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Complete blood count (CBC) - CRITICAL (before, every 2-4 weeks for first 3 months, then periodically, agranulocytosis risk, Black Box Warning)",
                    "Signs of agranulocytosis (fever, sore throat, mouth ulcers, infection) - CRITICAL (rare but fatal, Black Box Warning, discontinue immediately if suspected)",
                    "Liver function tests (ALT, AST, bilirubin) - CRITICAL (before, periodically, hepatotoxicity risk, can be fatal)",
                    "Signs of severe skin reactions (rash, fever, mucosal lesions) - CRITICAL (SJS/TEN - rare but fatal, Black Box Warning, discontinue immediately if suspected)",
                    "Thyroid function (TSH, T4, T3) - CRITICAL (monitor treatment response)",
                    "Signs of hypothyroidism (fatigue, weight gain, cold intolerance) - CRITICAL (with over-treatment)"
                ],
                "look_alike_sound_alike": ["Methimazole", "Tapazole", "Propylthiouracil", "Carbimazole"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Agranulocytosis (Rare but Fatal)",
                "FDA Black Box Warning - Severe Skin Reactions (SJS/TEN - Rare but Fatal)",
                "ATA Guidelines - Hyperthyroidism Treatment",
                "FDA Drug Label - Methimazole (Tapazole)"
            ]
        },

        "Propylthiouracil": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với propylthiouracil",
                ],
                "tương_đối": [
                    "Suy gan nặng - nguy cơ viêm gan",
                    "Giảm bạch cầu - nguy cơ agranulocytosis",
                    "Có thai (3 tháng đầu) - thận trọng",
                    "Đang cho con bú - thận trọng",
                    "Người cao tuổi - tăng nguy cơ tác dụng phụ",
                ],
            },
        },

        "Hydrocortisone": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "endocrine": "High (adrenal insufficiency - can be fatal if stopped abruptly after long-term use, Black Box Warning)",
                    "metabolic": "High (hyperglycemia - very common, can cause steroid-induced diabetes)",
                    "cardiovascular": "High (hypertension - very common, fluid retention)",
                    "skeletal": "High (osteoporosis - very common with long-term use)",
                    "gastrointestinal": "High (peptic ulcer disease - increased risk, especially with NSAIDs)",
                    "immunologic": "High (increased risk of serious infections - Black Box Warning)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Blood glucose - CRITICAL (hyperglycemia very common, can cause steroid-induced diabetes)",
                    "Blood pressure - CRITICAL (hypertension very common, fluid retention)",
                    "Signs of infection - CRITICAL (increased risk of serious infections, Black Box Warning)",
                    "Signs of adrenal insufficiency (fatigue, weakness, hypotension, hyponatremia) - CRITICAL (if stopped abruptly after >2 weeks use, can be fatal, Black Box Warning)",
                    "Bone density (DEXA scan) - CRITICAL (if long-term use >3 months, osteoporosis risk)",
                    "Signs of peptic ulcer (abdominal pain, melena, hematemesis) - CRITICAL (increased risk, especially with NSAIDs)",
                    "Weight and fluid retention - CRITICAL (Cushingoid appearance - moon face, buffalo hump)",
                    "Taper schedule - CRITICAL (must taper gradually if used >2 weeks to avoid adrenal insufficiency, Black Box Warning)"
                ],
                "look_alike_sound_alike": ["Hydrocortisone", "Cortisol", "Prednisone", "Methylprednisolone"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Adrenal Insufficiency (Can Be Fatal If Stopped Abruptly After Long-Term Use)",
                "FDA Black Box Warning - Increased Risk of Serious Infections",
                "FDA Drug Label - Hydrocortisone",
                "Endocrine Society Guidelines - Adrenal Insufficiency"
            ]
        },

        "Dexamethasone": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "endocrine": "High (adrenal insufficiency - can be fatal if stopped abruptly after long-term use, Black Box Warning)",
                    "metabolic": "High (hyperglycemia - very common, can cause steroid-induced diabetes)",
                    "cardiovascular": "High (hypertension - very common)",
                    "skeletal": "High (osteoporosis - very common with long-term use)",
                    "gastrointestinal": "High (peptic ulcer disease - increased risk, especially with NSAIDs)",
                    "immunologic": "High (increased risk of serious infections - Black Box Warning)",
                    "neuropsychiatric": "Moderate (psychosis, mania, depression - especially with high doses)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Blood glucose - CRITICAL (hyperglycemia very common, can cause steroid-induced diabetes)",
                    "Blood pressure - CRITICAL (hypertension very common)",
                    "Signs of infection - CRITICAL (increased risk of serious infections, Black Box Warning)",
                    "Signs of adrenal insufficiency (fatigue, weakness, hypotension, hyponatremia) - CRITICAL (if stopped abruptly after >2 weeks use, can be fatal, Black Box Warning)",
                    "Bone density (DEXA scan) - CRITICAL (if long-term use >3 months, osteoporosis risk)",
                    "Signs of peptic ulcer (abdominal pain, melena, hematemesis) - CRITICAL (increased risk, especially with NSAIDs)",
                    "Neuropsychiatric symptoms - CRITICAL (psychosis, mania, depression - especially with high doses)",
                    "Taper schedule - CRITICAL (must taper gradually if used >2 weeks to avoid adrenal insufficiency, Black Box Warning)",
                    "Long half-life - CRITICAL (36-72 hours, effects persist long after discontinuation)"
                ],
                "look_alike_sound_alike": ["Dexamethasone", "Decadron", "Prednisone", "Methylprednisolone"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Adrenal Insufficiency (Can Be Fatal If Stopped Abruptly After Long-Term Use)",
                "FDA Black Box Warning - Increased Risk of Serious Infections",
                "FDA Drug Label - Dexamethasone (Decadron)",
                "WHO Guidelines - COVID-19 Treatment (Severe Cases)"
            ]
        },

    # ======================== BATCH 6: ANTIHISTAMINE & ANTIVIRAL ========================
        "Diphenhydramine": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với diphenhydramine hoặc antihistamine",
                    "Trẻ sơ sinh <2 tháng tuổi",
                ],
                "tương_đối": [
                    "Bệnh nhược cơ - tăng yếu cơ",
                    "Tăng nhãn áp góc đóng",
                    "Loét dạ dày tá tràng",
                    "Tắc nghẽn đường tiết niệu",
                    "Bệnh tim mạch - tăng nguy cơ rối loạn nhịp",
                    "Có thai - thận trọng",
                    "Đang cho con bú - thận trọng",
                    "Người cao tuổi - tăng nguy cơ tác dụng phụ",
                ],
            },
        },

        "Loratadine": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với loratadine",
                ],
                "tương_đối": [
                    "Suy gan nặng - giảm liều",
                    "Suy thận nặng - thận trọng",
                    "Có thai - thận trọng",
                    "Đang cho con bú - thận trọng",
                ],
            },
        },

        "Chlorpheniramine": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với chlorpheniramine hoặc antihistamine",
                    "Trẻ sơ sinh <2 tháng tuổi",
                ],
                "tương_đối": [
                    "Bệnh nhược cơ - tăng yếu cơ",
                    "Tăng nhãn áp góc đóng",
                    "Loét dạ dày tá tràng",
                    "Tắc nghẽn đường tiết niệu",
                    "Bệnh tim mạch - tăng nguy cơ rối loạn nhịp",
                    "Có thai - thận trọng",
                    "Đang cho con bú - thận trọng",
                    "Người cao tuổi - tăng nguy cơ tác dụng phụ",
                ],
            },
        },

        "Acyclovir": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với acyclovir",
                ],
                "tương_đối": [
                    "Suy thận nặng (CrCl <25) - giảm liều",
                    "Mất nước - tăng nguy cơ độc tính thận",
                    "Có thai - thận trọng",
                    "Đang cho con bú - thận trọng",
                    "Người cao tuổi - tăng nguy cơ độc tính thận",
                ],
            },
        },

        "Valacyclovir": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với valacyclovir hoặc acyclovir",
                ],
                "tương_đối": [
                    "Suy thận nặng (CrCl <30) - giảm liều",
                    "Mất nước - tăng nguy cơ độc tính thận",
                    "Suy gan nặng - thận trọng",
                    "Có thai - thận trọng",
                    "Đang cho con bú - thận trọng",
                    "Người cao tuổi - tăng nguy cơ độc tính thận",
                ],
            },
        },

    # ======================== BATCH 7: MIXED IMPORTANT DRUGS ========================
        "5-Fluorouracil": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với 5-fluorouracil",
                    "Suy thận nặng (CrCl <30)",
                    "Suy gan nặng",
                    "Thiếu DPD (dihydropyrimidine dehydrogenase)",
                    "Có thai",
                    "Đang cho con bú",
                ],
                "tương_đối": [
                    "Suy thận vừa (CrCl 30-60) - giảm liều",
                    "Suy gan vừa - thận trọng",
                    "Người cao tuổi - tăng nguy cơ độc tính",
                    "Bệnh tim mạch - tăng nguy cơ thiếu máu cơ tim",
                ],
            },
        },

        "Abiraterone": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với abiraterone",
                    "Suy gan nặng",
                    "Có thai",
                ],
                "tương_đối": [
                    "Suy gan vừa - thận trọng",
                    "Suy thận nặng - thận trọng",
                    "Bệnh tim mạch - tăng nguy cơ",
                    "Đang cho con bú - thận trọng",
                ],
            },
        },

        "Acebutolol": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với acebutolol hoặc beta-blocker",
                    "Suy tim nặng không được điều trị",
                    "Block nhĩ thất độ 2-3 không có máy tạo nhịp",
                    "Sick sinus syndrome không có máy tạo nhịp",
                    "Nhịp tim chậm nặng (<50 bpm)",
                    "Sốc tim",
                    "Hen suyễn nặng hoặc COPD nặng",
                ],
                "tương_đối": [
                    "Suy tim vừa - cần điều trị trước",
                    "Nhịp tim chậm vừa (50-60 bpm)",
                    "Block nhĩ thất độ 1",
                    "Bệnh mạch máu ngoại biên",
                    "Đái tháo đường - che dấu triệu chứng hạ đường huyết",
                    "Suy thận nặng (CrCl <30) - giảm liều",
                    "Có thai - thận trọng",
                    "Đang cho con bú - thận trọng",
                ],
            },
        },

        "Aclidinium": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với aclidinium",
                    "Tăng nhãn áp góc đóng",
                ],
                "tương_đối": [
                    "Tăng nhãn áp góc mở - thận trọng",
                    "Bệnh tim mạch - thận trọng",
                    "Tắc nghẽn đường tiết niệu",
                    "Có thai - thận trọng",
                    "Đang cho con bú - thận trọng",
                ],
            },
        },

        "Acyclovir eye drops": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với acyclovir",
                ],
                "tương_đối": [
                    "Tổn thương giác mạc nặng",
                    "Nhiễm trùng mắt không được điều trị",
                    "Có thai - thận trọng",
                    "Đang cho con bú - thận trọng",
                ],
            },
        },

        "Acyclovir eye ointment": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với acyclovir",
                ],
                "tương_đối": [
                    "Tổn thương giác mạc nặng",
                    "Nhiễm trùng mắt không được điều trị",
                    "Có thai - thận trọng",
                    "Đang cho con bú - thận trọng",
                ],
            },
        },

        "Adalimumab": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với adalimumab",
                    "Nhiễm trùng nặng đang hoạt động",
                    "Suy tim nặng (NYHA III-IV)",
                ],
                "tương_đối": [
                    "Nhiễm trùng vừa - cần điều trị trước",
                    "Suy tim vừa - thận trọng",
                    "Bệnh thần kinh đã biết",
                    "Ung thư - tăng nguy cơ",
                    "Có thai - thận trọng",
                    "Đang cho con bú - thận trọng",
                ],
            },
        },

        "Albendazole": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với albendazole",
                    "Có thai",
                ],
                "tương_đối": [
                    "Suy gan nặng - thận trọng",
                    "Suy thận nặng - thận trọng",
                    "Giảm bạch cầu - nguy cơ giảm thêm",
                    "Đang cho con bú - thận trọng",
                ],
            },
        },

        "Alemtuzumab": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với alemtuzumab",
                    "Nhiễm trùng nặng đang hoạt động",
                    "HIV dương tính",
                ],
                "tương_đối": [
                    "Nhiễm trùng vừa - cần điều trị trước",
                    "Bệnh tự miễn - tăng nguy cơ",
                    "Ung thư - tăng nguy cơ",
                    "Có thai - thận trọng",
                    "Đang cho con bú - thận trọng",
                ],
            },
        },

        "Alfuzosin": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với alfuzosin",
                    "Suy gan nặng",
                    "Hạ huyết áp nặng",
                ],
                "tương_đối": [
                    "Suy gan vừa - thận trọng",
                    "Hạ huyết áp",
                    "Bệnh tim mạch - thận trọng",
                    "Có thai - không áp dụng",
                    "Đang cho con bú - không áp dụng",
                ],
            },
        },

        "Anastrozole": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với anastrozole",
                    "Phụ nữ tiền mãn kinh",
                    "Có thai",
                ],
                "tương_đối": [
                    "Suy gan nặng - thận trọng",
                    "Suy thận nặng - thận trọng",
                    "Loãng xương - tăng nguy cơ",
                    "Đang cho con bú - không áp dụng",
                ],
            },
        },

        "Anidulafungin": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với anidulafungin hoặc echinocandin",
                ],
                "tương_đối": [
                    "Suy gan nặng - thận trọng",
                    "Suy thận nặng - không cần giảm liều",
                    "Có thai - thận trọng",
                    "Đang cho con bú - thận trọng",
                ],
            },
        },

        "Anifrolumab": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với anifrolumab",
                    "Nhiễm trùng nặng đang hoạt động",
                ],
                "tương_đối": [
                    "Nhiễm trùng vừa - cần điều trị trước",
                    "Bệnh tự miễn khác - tăng nguy cơ",
                    "Ung thư - tăng nguy cơ",
                    "Có thai - thận trọng",
                    "Đang cho con bú - thận trọng",
                ],
            },
        },

        "Aripiprazole": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với aripiprazole",
                ],
                "tương_đối": [
                    "Bệnh tim mạch - tăng nguy cơ kéo dài QT",
                    "Suy gan nặng - giảm liều",
                    "Suy thận nặng - thận trọng",
                    "Động kinh - có thể gây co giật",
                    "Đái tháo đường - tăng nguy cơ tăng đường huyết",
                    "Có thai - thận trọng",
                    "Đang cho con bú - thận trọng",
                ],
            },
        },

        "Artemether-lumefantrine": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với artemether hoặc lumefantrine",
                    "Rối loạn nhịp tim nặng",
                    "Có thai (3 tháng đầu)",
                ],
                "tương_đối": [
                    "Bệnh tim mạch - tăng nguy cơ kéo dài QT",
                    "Suy gan nặng - thận trọng",
                    "Suy thận nặng - thận trọng",
                    "Có thai (3 tháng giữa và cuối) - thận trọng",
                    "Đang cho con bú - thận trọng",
                ],
            },
        },

    # ======================== BATCH 8: MIXED IMPORTANT DRUGS (CONTINUED) ========================
        "Artesunate": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với artesunate",
                    "Có thai (3 tháng đầu)",
                ],
                "tương_đối": [
                    "Suy gan nặng - thận trọng",
                    "Suy thận nặng - thận trọng",
                    "Bệnh tim mạch - thận trọng",
                    "Có thai (3 tháng giữa và cuối) - thận trọng",
                    "Đang cho con bú - thận trọng",
                ],
            },
        },

        "Artificial tears (Carboxymethylcellulose)": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với carboxymethylcellulose hoặc thành phần",
                ],
                "tương_đối": [
                    "Nhiễm trùng mắt đang hoạt động",
                    "Tổn thương giác mạc nặng",
                ],
            },
        },

        "Azelaic acid topical": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với azelaic acid",
                ],
                "tương_đối": [
                    "Da bị kích ứng nặng",
                    "Vết thương hở tại vùng điều trị",
                    "Có thai - thận trọng",
                    "Đang cho con bú - thận trọng",
                ],
            },
        },

        "Azelastine eye drops": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với azelastine",
                ],
                "tương_đối": [
                    "Nhiễm trùng mắt đang hoạt động",
                    "Tổn thương giác mạc",
                    "Đeo kính áp tròng mềm",
                    "Có thai - thận trọng",
                    "Đang cho con bú - thận trọng",
                ],
            },
        },

        "Benzoyl peroxide topical": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với benzoyl peroxide",
                ],
                "tương_đối": [
                    "Da bị kích ứng nặng",
                    "Vết thương hở tại vùng điều trị",
                    "Da nhạy cảm với ánh sáng",
                    "Có thai - thận trọng",
                    "Đang cho con bú - thận trọng",
                ],
            },
        },

        "Betamethasone": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với betamethasone hoặc corticosteroid",
                    "Nhiễm trùng hệ thống không được điều trị",
                    "Nhiễm nấm toàn thân",
                ],
                "tương_đối": [
                    "Đái tháo đường - tăng đường huyết",
                    "Tăng huyết áp",
                    "Loãng xương",
                    "Loét dạ dày tá tràng",
                    "Suy tim nặng",
                    "Suy gan nặng",
                    "Suy thận nặng",
                    "Có thai - thận trọng, có thể gây dị tật",
                    "Đang cho con bú - thận trọng",
                    "Trẻ em - ảnh hưởng đến tăng trưởng",
                ],
            },
        },

        "Ceftazidime": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với ceftazidime hoặc cephalosporin",
                    "Tiền sử phản ứng phản vệ với beta-lactam",
                ],
                "tương_đối": [
                    "Dị ứng với penicillin - thận trọng",
                    "Suy thận nặng (CrCl <30) - giảm liều",
                    "Suy gan nặng - thận trọng",
                    "Có thai - thận trọng",
                    "Đang cho con bú - thận trọng",
                ],
            },
        },

        "Celecoxib": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với celecoxib hoặc sulfonamide",
                    "Tiền sử hen suyễn do aspirin/NSAID",
                    "Loét dạ dày tá tràng đang hoạt động",
                    "Xuất huyết tiêu hóa đang hoạt động",
                    "Suy tim nặng (NYHA III-IV)",
                    "Có thai (3 tháng cuối)",
                ],
                "tương_đối": [
                    "Tiền sử loét dạ dày tá tràng",
                    "Suy thận nặng (CrCl <30) - thận trọng",
                    "Suy gan nặng - thận trọng",
                    "Suy tim vừa - thận trọng",
                    "Tăng huyết áp không kiểm soát",
                    "Đang dùng thuốc chống đông",
                    "Có thai (1-2 tháng đầu và giữa) - thận trọng",
                    "Đang cho con bú - thận trọng",
                ],
            },
        },

    # ======================== BATCH PRIORITY: CONTRAINDICATIONS_DETAIL ========================
        "Digoxin": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với digoxin hoặc digitalis glycosides",
                    "Block nhĩ-thất độ 2-3 không có máy tạo nhịp",
                    "Hội chứng Wolff-Parkinson-White (WPW) với rung nhĩ",
                    "Rối loạn nhịp thất nặng (ventricular fibrillation, ventricular tachycardia không kiểm soát)",
                ],
                "tương_đối": [
                    "Suy thận mức độ vừa-nặng (cần giảm liều và theo dõi nồng độ)",
                    "Suy tim cấp mất bù (cần ổn định trước khi dùng)",
                    "Hạ kali máu, hạ magie máu (tăng nguy cơ độc tính)",
                    "Nhịp tim chậm <60 lần/phút (trừ khi có máy tạo nhịp)",
                ],
            },
        },

        "Fentanyl": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với fentanyl hoặc opioid",
                    "Suy hô hấp nặng không có hỗ trợ thở máy",
                    "Bệnh nhân đang dùng MAO inhibitors (trong vòng 14 ngày)",
                ],
                "tương_đối": [
                    "Suy hô hấp mạn tính, COPD nặng (cần thận trọng, theo dõi sát)",
                    "Tăng áp lực nội sọ, chấn thương sọ não",
                    "Suy gan nặng (giảm chuyển hóa, tăng nguy cơ tích tụ)",
                    "Phụ nữ có thai (category C, tránh dùng kéo dài)",
                ],
            },
        },

        "Hydromorphone": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với hydromorphone hoặc opioid",
                    "Suy hô hấp nặng không có hỗ trợ thở máy",
                    "Tắc ruột cơ học, liệt ruột",
                ],
                "tương_đối": [
                    "Suy hô hấp mạn tính, COPD nặng",
                    "Tăng áp lực nội sọ",
                    "Suy gan nặng (giảm chuyển hóa)",
                    "Suy thận nặng (tích tụ chất chuyển hóa)",
                ],
            },
        },

        "Insulin Regular": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với insulin hoặc bất kỳ thành phần nào",
                    "Hạ đường huyết nặng đang diễn ra",
                ],
                "tương_đối": [
                    "Suy thận nặng (cần điều chỉnh liều, theo dõi sát)",
                    "Suy gan nặng (giảm chuyển hóa glucose, tăng nguy cơ hạ đường huyết)",
                    "Bệnh nhân không có khả năng tự theo dõi đường huyết",
                ],
            },
        },

        "Nitroglycerin": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với nitroglycerin hoặc nitrate",
                    "Hạ huyết áp nặng (systolic <90 mmHg)",
                    "Thiếu máu cơ tim cấp do hẹp động mạch chủ nặng",
                    "Viêm màng ngoài tim co thắt",
                    "Đang dùng phosphodiesterase-5 inhibitors (sildenafil, tadalafil, vardenafil) - nguy cơ hạ huyết áp đe dọa tính mạng",
                ],
                "tương_đối": [
                    "Hạ huyết áp nhẹ-vừa (theo dõi sát, có thể cần giảm liều)",
                    "Thiếu máu nặng (giảm tải oxy)",
                    "Tăng áp lực nội sọ",
                    "Suy thận nặng (tích tụ chất chuyển hóa)",
                ],
            },
        },

        "Phenylephrine": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với phenylephrine",
                    "Tăng huyết áp nặng không kiểm soát",
                    "Bệnh mạch vành không ổn định, nhồi máu cơ tim cấp",
                ],
                "tương_đối": [
                    "Tăng huyết áp vừa (theo dõi sát)",
                    "Bệnh mạch vành, rối loạn nhịp tim",
                    "Cường giáp (tăng nhạy cảm với catecholamine)",
                    "Bệnh nhân đang dùng MAO inhibitors",
                ],
            },
        },

        "Vasopressin": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với vasopressin",
                ],
                "tương_đối": [
                    "Bệnh mạch vành (có thể gây co mạch vành, thiếu máu cơ tim)",
                    "Bệnh mạch máu ngoại biên nặng",
                    "Suy thận nặng (giảm tưới máu thận)",
                    "Hạ natri máu nặng (vasopressin có thể làm nặng thêm)",
                ],
            },
        },

        "Milrinone": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với milrinone",
                    "Rối loạn nhịp thất nặng không kiểm soát",
                ],
                "tương_đối": [
                    "Hạ huyết áp nặng (milrinone có thể gây giãn mạch)",
                    "Rối loạn nhịp nhĩ hoặc thất (tăng nguy cơ)",
                    "Suy thận nặng (giảm thải trừ, tăng nguy cơ tích tụ)",
                    "Bệnh mạch vành không ổn định",
                ],
            },
        },

        "Nesiritide": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với nesiritide",
                    "Hạ huyết áp nặng (systolic <90 mmHg)",
                    "Sốc tim",
                ],
                "tương_đối": [
                    "Hạ huyết áp vừa (theo dõi sát)",
                    "Bệnh mạch vành không ổn định",
                    "Suy thận nặng (giảm thải trừ)",
                    "Hẹp van động mạch chủ nặng",
                ],
            },
        },

        "Clevidipine": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với clevidipine hoặc soy/egg (chứa trong dung dịch)",
                    "Suy gan nặng",
                ],
                "tương_đối": [
                    "Suy thận nặng (theo dõi sát)",
                    "Bệnh mạch vành không ổn định (có thể gây phản xạ nhịp nhanh)",
                    "Hạ huyết áp nhẹ-vừa (theo dõi sát)",
                ],
            },
        },

        "Nitroprusside": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với nitroprusside",
                    "Thiếu máu cơ tim cấp do hẹp động mạch chủ nặng",
                    "Thiếu hụt bẩm sinh cytochrome b5 reductase (nguy cơ nhiễm độc cyanide)",
                ],
                "tương_đối": [
                    "Suy thận nặng (tích tụ thiocyanate, nguy cơ độc tính)",
                    "Suy gan nặng (giảm chuyển hóa cyanide)",
                    "Thiếu vitamin B12 (tăng nguy cơ nhiễm độc cyanide)",
                    "Tăng áp lực nội sọ",
                ],
            },
        },

        "Rocuronium": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với rocuronium hoặc aminosteroid neuromuscular blocking agents",
                ],
                "tương_đối": [
                    "Bệnh nhược cơ (myasthenia gravis) - cần giảm liều mạnh",
                    "Rối loạn chức năng thần kinh cơ khác",
                    "Suy thận nặng (kéo dài thời gian tác dụng)",
                    "Suy gan nặng (kéo dài thời gian tác dụng)",
                ],
            },
        },

        "Succinylcholine": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với succinylcholine",
                    "Tiền sử hoặc nguy cơ tăng kali máu nặng (bỏng nặng, chấn thương lớn, liệt tủy sống, bệnh cơ)",
                    "Bệnh nhược cơ (myasthenia gravis) - có thể gây block kéo dài",
                    "Rối loạn di truyền pseudocholinesterase (block kéo dài, nguy cơ ngừng thở)",
                ],
                "tương_đối": [
                    "Tăng nhãn áp (có thể làm tăng áp lực nội nhãn)",
                    "Tăng áp lực nội sọ",
                    "Bệnh cơ di truyền (malignant hyperthermia, Duchenne muscular dystrophy)",
                    "Suy gan nặng (giảm chuyển hóa)",
                ],
            },
        },

        "Vecuronium": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với vecuronium hoặc aminosteroid neuromuscular blocking agents",
                ],
                "tương_đối": [
                    "Bệnh nhược cơ (myasthenia gravis) - cần giảm liều mạnh",
                    "Rối loạn chức năng thần kinh cơ khác",
                    "Suy thận nặng (kéo dài thời gian tác dụng)",
                    "Suy gan nặng (kéo dài thời gian tác dụng)",
                ],
            },
        },

        "Thiopental": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với thiopental hoặc barbiturate",
                    "Porphyria cấp (có thể gây cơn porphyria)",
                    "Suy hô hấp nặng không có hỗ trợ thở máy",
                ],
                "tương_đối": [
                    "Suy hô hấp mạn tính",
                    "Suy tim nặng (có thể gây hạ huyết áp)",
                    "Suy gan nặng (kéo dài thời gian tác dụng)",
                    "Suy thận nặng (tích tụ)",
                ],
            },
        },

    # ======================== BATCH PRIORITY: REVERSAL_AGENTS ========================
        "Alteplase": {
            "reversal_agents": {
                "available": False,
                "agents": [],
                "notes": "Không có thuốc giải độc đặc hiệu cho alteplase. Xử trí: ngừng truyền ngay, hỗ trợ huyết động, truyền máu và các chế phẩm máu nếu chảy máu nặng. Có thể cân nhắc tranexamic acid hoặc aminocaproic acid trong trường hợp chảy máu đe dọa tính mạng (theo guideline chuyên ngành).",
            },
        },

    # ======================== BATCH 2: CONTRAINDICATIONS_DETAIL ========================
        "Cefepime": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với cefepime hoặc cephalosporin",
                    "Dị ứng nặng với penicillin (phản ứng chéo có thể xảy ra)",
                ],
                "tương_đối": [
                    "Suy thận nặng (cần điều chỉnh liều)",
                    "Tiền sử viêm đại tràng do Clostridium difficile",
                    "Rối loạn đông máu (cefepime có thể gây giảm prothrombin)",
                ],
            },
        },

        "Cefotaxime": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với cefotaxime hoặc cephalosporin",
                    "Dị ứng nặng với penicillin",
                ],
                "tương_đối": [
                    "Suy thận nặng (cần điều chỉnh liều)",
                    "Tiền sử viêm đại tràng do C. difficile",
                    "Rối loạn đông máu",
                ],
            },
        },

        "Cefuroxime": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với cefuroxime hoặc cephalosporin",
                    "Dị ứng nặng với penicillin",
                ],
                "tương_đối": [
                    "Suy thận nặng (cần điều chỉnh liều)",
                    "Tiền sử viêm đại tràng do C. difficile",
                ],
            },
        },

        "Cephalexin": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với cephalexin hoặc cephalosporin",
                    "Dị ứng nặng với penicillin",
                ],
                "tương_đối": [
                    "Suy thận nặng (cần điều chỉnh liều)",
                    "Tiền sử viêm đại tràng do C. difficile",
                ],
            },
        },

        "Caspofungin": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với caspofungin hoặc echinocandin",
                ],
                "tương_đối": [
                    "Suy gan nặng (cần điều chỉnh liều)",
                    "Đang dùng cyclosporine (tăng nguy cơ độc tính gan)",
                ],
            },
        },

        "Cisplatin": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với cisplatin hoặc platinum compounds",
                    "Suy thận nặng (eGFR <30 mL/min)",
                    "Giảm thính lực nặng",
                ],
                "tương_đối": [
                    "Suy thận vừa (cần điều chỉnh liều và theo dõi sát)",
                    "Suy tim, bệnh mạch vành",
                    "Giảm bạch cầu hoặc tiểu cầu nặng",
                    "Bệnh thần kinh ngoại biên",
                ],
            },
        },

        "Carboplatin": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với carboplatin hoặc platinum compounds",
                    "Suy thận nặng (eGFR <30 mL/min)",
                ],
                "tương_đối": [
                    "Suy thận vừa (cần điều chỉnh liều theo AUC)",
                    "Giảm bạch cầu hoặc tiểu cầu nặng",
                    "Suy gan nặng",
                ],
            },
        },

        "Baclofen": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với baclofen",
                ],
                "tương_đối": [
                    "Suy thận nặng (tăng nguy cơ độc tính, cần giảm liều)",
                    "Động kinh không kiểm soát",
                    "Rối loạn tâm thần",
                    "Loét dạ dày tá tràng",
                ],
            },
        },

        "Bupropion": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với bupropion",
                    "Động kinh hoặc tiền sử động kinh",
                    "Đang dùng MAO inhibitors (trong vòng 14 ngày)",
                    "Rối loạn ăn uống (anorexia nervosa, bulimia nervosa)",
                ],
                "tương_đối": [
                    "Tiền sử động kinh hoặc yếu tố nguy cơ co giật",
                    "Chấn thương đầu, u não",
                    "Rối loạn gan nặng",
                    "Tăng huyết áp không kiểm soát",
                ],
            },
        },

        "Buprenorphine": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với buprenorphine hoặc opioid",
                    "Suy hô hấp nặng không có hỗ trợ thở máy",
                    "Đang dùng MAO inhibitors (trong vòng 14 ngày)",
                ],
                "tương_đối": [
                    "Suy hô hấp mạn tính, COPD nặng",
                    "Suy gan nặng (giảm chuyển hóa)",
                    "Tăng áp lực nội sọ",
                    "Phụ nữ có thai (category C)",
                ],
            },
        },

        "Candesartan": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với candesartan hoặc ARB",
                    "Phụ nữ có thai (tháng 2-3, category D)",
                    "Hẹp động mạch thận hai bên hoặc một bên ở bệnh nhân một thận",
                ],
                "tương_đối": [
                    "Suy thận nặng (theo dõi chức năng thận)",
                    "Hạ huyết áp",
                    "Tăng kali máu",
                    "Hẹp động mạch thận một bên",
                ],
            },
        },

        "Benazepril": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với benazepril hoặc ACE inhibitor",
                    "Phụ nữ có thai (tháng 2-3, category D)",
                    "Phù mạch do ACE inhibitor trước đó",
                    "Hẹp động mạch thận hai bên hoặc một bên ở bệnh nhân một thận",
                ],
                "tương_đối": [
                    "Suy thận nặng (theo dõi chức năng thận)",
                    "Hạ huyết áp",
                    "Tăng kali máu",
                    "Bệnh mô liên kết (tăng nguy cơ neutropenia)",
                ],
            },
        },

        "Canagliflozin": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với canagliflozin hoặc SGLT2 inhibitor",
                    "Suy thận nặng (eGFR <30 mL/min)",
                    "Nhiễm toan ceton do đái tháo đường",
                ],
                "tương_đối": [
                    "Suy thận vừa (eGFR 30-60, cần điều chỉnh liều)",
                    "Suy tim nặng",
                    "Nhiễm trùng đường tiết niệu tái phát",
                    "Nhiễm nấm sinh dục",
                ],
            },
        },

        "Chlorpromazine": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với chlorpromazine hoặc phenothiazine",
                    "Coma do thuốc ức chế thần kinh trung ương",
                    "Giảm bạch cầu nặng",
                ],
                "tương_đối": [
                    "Bệnh tim mạch nặng",
                    "Động kinh",
                    "Bệnh gan",
                    "Parkinson",
                    "Glaucoma góc đóng",
                ],
            },
        },

        "Chloroquine": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với chloroquine",
                    "Bệnh võng mạc do chloroquine",
                    "Rối loạn nhịp tim nặng",
                ],
                "tương_đối": [
                    "Bệnh gan nặng",
                    "Bệnh thận nặng",
                    "Bệnh cơ (myopathy)",
                    "Bệnh máu (porphyria)",
                    "Rối loạn tâm thần",
                ],
            },
        },

    # ======================== BATCH 3: CONTRAINDICATIONS_DETAIL ========================
        "Codeine": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với codeine hoặc opioid",
                    "Suy hô hấp nặng không có hỗ trợ thở máy",
                    "Đang dùng MAO inhibitors (trong vòng 14 ngày)",
                ],
                "tương_đối": [
                    "Suy hô hấp mạn tính, COPD nặng",
                    "Tăng áp lực nội sọ",
                    "Suy gan nặng (giảm chuyển hóa)",
                    "Suy thận nặng",
                ],
            },
        },

        "Dipyridamole": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với dipyridamole",
                ],
                "tương_đối": [
                    "Hạ huyết áp nặng",
                    "Bệnh mạch vành không ổn định",
                    "Suy tim nặng",
                    "Rối loạn đông máu",
                ],
            },
        },

        "Disopyramide": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với disopyramide",
                    "Suy tim nặng, sốc tim",
                    "Block nhĩ-thất độ 2-3 không có máy tạo nhịp",
                    "Suy thận nặng (eGFR <30 mL/min)",
                ],
                "tương_đối": [
                    "Suy tim vừa",
                    "Suy thận vừa (cần điều chỉnh liều)",
                    "Bệnh mạch vành",
                    "Glaucoma góc đóng",
                ],
            },
        },

        "Dofetilide": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với dofetilide",
                    "Suy thận nặng (CrCl <20 mL/min)",
                    "QT kéo dài (QTc >500 ms)",
                    "Đang dùng thuốc gây kéo dài QT",
                ],
                "tương_đối": [
                    "Suy thận vừa (cần điều chỉnh liều)",
                    "QT kéo dài nhẹ-vừa",
                    "Rối loạn điện giải (hạ kali, hạ magie)",
                ],
            },
        },

        "Doxazosin": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với doxazosin hoặc alpha-blocker",
                ],
                "tương_đối": [
                    "Hạ huyết áp nặng",
                    "Suy gan nặng",
                    "Suy thận nặng",
                ],
            },
        },

        "Eplerenone": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với eplerenone",
                    "Suy thận nặng (CrCl <30 mL/min)",
                    "Tăng kali máu nặng (>5.5 mEq/L)",
                    "Đang dùng thuốc ức chế CYP3A4 mạnh (ketoconazole, itraconazole)",
                ],
                "tương_đối": [
                    "Suy thận vừa (theo dõi kali máu)",
                    "Tăng kali máu nhẹ-vừa",
                    "Suy gan nặng",
                ],
            },
        },

        "Felodipine": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với felodipine hoặc dihydropyridine calcium channel blocker",
                ],
                "tương_đối": [
                    "Hạ huyết áp nặng",
                    "Suy gan nặng (tăng nồng độ)",
                    "Suy tim nặng",
                ],
            },
        },

        "Fenofibrate": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với fenofibrate hoặc fibrate",
                    "Bệnh gan hoạt động",
                    "Suy thận nặng (eGFR <30 mL/min)",
                    "Bệnh túi mật",
                ],
                "tương_đối": [
                    "Suy gan vừa",
                    "Suy thận vừa (cần điều chỉnh liều)",
                    "Rối loạn chức năng tuyến giáp",
                ],
            },
        },

        "Filgrastim": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "hematologic": "Moderate (splenic rupture - rare but serious, can be fatal)",
                    "pulmonary": "Moderate (acute respiratory distress syndrome - ARDS - rare but serious)",
                    "skeletal": "Moderate (bone pain - very common, can be severe)",
                    "hematologic_sickle": "High (sickle cell crisis - in patients with sickle cell disease, can be fatal)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "CBC (white blood cell count) - CRITICAL (monitor for leukocytosis, discontinue if WBC >100,000/mm³)",
                    "Signs of splenic rupture (left upper quadrant pain, shoulder pain) - CRITICAL (rare but serious, can be fatal)",
                    "Pulmonary symptoms (dyspnea, hypoxia) - CRITICAL (ARDS rare but serious)",
                    "Bone pain - CRITICAL (very common, can be severe, may need analgesics)",
                    "Sickle cell disease - CRITICAL (contraindicated, can cause sickle cell crisis, can be fatal)",
                    "Signs of sickle cell crisis (severe pain, fever) - CRITICAL (if used in sickle cell disease, can be fatal)"
                ],
                "look_alike_sound_alike": ["Filgrastim", "Neupogen", "Pegfilgrastim", "Sargramostim"]
            },
            "guideline_tags": [
                "FDA Drug Label - Filgrastim (Neupogen)",
                "ASCO Guidelines - Myeloid Growth Factors",
                "NCCN Guidelines - Supportive Care"
            ]
        },

        "Fludrocortisone": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với fludrocortisone hoặc corticosteroid",
                    "Nhiễm nấm hệ thống không điều trị",
                ],
                "tương_đối": [
                    "Suy tim nặng",
                    "Tăng huyết áp nặng",
                    "Phù nề",
                    "Loãng xương",
                ],
            },
        },

        "Fosphenytoin": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với fosphenytoin hoặc phenytoin",
                    "Block nhĩ-thất độ 2-3",
                ],
                "tương_đối": [
                    "Suy gan nặng (giảm chuyển hóa)",
                    "Suy thận nặng",
                    "Bệnh tim",
                    "Rối loạn chức năng tuyến giáp",
                ],
            },
        },

        "Ganciclovir": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với ganciclovir",
                ],
                "tương_đối": [
                    "Suy thận nặng (cần điều chỉnh liều)",
                    "Giảm bạch cầu hoặc tiểu cầu nặng",
                    "Suy gan nặng",
                ],
            },
        },

        "Gemfibrozil": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với gemfibrozil hoặc fibrate",
                    "Bệnh gan hoạt động",
                    "Suy thận nặng (eGFR <30 mL/min)",
                    "Bệnh túi mật",
                ],
                "tương_đối": [
                    "Suy gan vừa",
                    "Suy thận vừa",
                    "Rối loạn chức năng tuyến giáp",
                ],
            },
        },

        "Glimepiride": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với glimepiride hoặc sulfonylurea",
                    "Đái tháo đường type 1",
                    "Nhiễm toan ceton do đái tháo đường",
                    "Suy thận nặng (eGFR <30 mL/min)",
                ],
                "tương_đối": [
                    "Suy gan nặng (tăng nguy cơ hạ đường huyết)",
                    "Suy thận vừa (cần điều chỉnh liều)",
                    "Người cao tuổi (tăng nguy cơ hạ đường huyết)",
                ],
            },
        },

        "Hydralazine": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với hydralazine",
                    "Bệnh mạch vành nặng",
                    "Nhồi máu cơ tim cấp",
                ],
                "tương_đối": [
                    "Suy tim nặng",
                    "Bệnh mạch vành",
                    "Suy gan nặng",
                    "Suy thận nặng",
                ],
            },
        },

    # ======================== BATCH 4: CONTRAINDICATIONS_DETAIL ========================
        "Hydrocodone": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với hydrocodone hoặc opioid",
                    "Suy hô hấp nặng không có hỗ trợ thở máy",
                    "Đang dùng MAO inhibitors (trong vòng 14 ngày)",
                ],
                "tương_đối": [
                    "Suy hô hấp mạn tính, COPD nặng",
                    "Tăng áp lực nội sọ",
                    "Suy gan nặng (giảm chuyển hóa)",
                    "Suy thận nặng",
                ],
            },
        },

        "Hydroxyzine": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với hydroxyzine hoặc piperazine",
                    "Phụ nữ có thai sớm (category C)",
                ],
                "tương_đối": [
                    "Suy gan nặng",
                    "Suy thận nặng",
                    "Bệnh tim",
                    "Glaucoma góc đóng",
                ],
            },
        },

        "Indapamide": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với indapamide hoặc sulfonamide",
                    "Suy thận nặng (eGFR <30 mL/min)",
                    "Tăng kali máu nặng",
                ],
                "tương_đối": [
                    "Suy gan nặng",
                    "Suy thận vừa (theo dõi điện giải)",
                    "Đái tháo đường",
                    "Gout",
                ],
            },
        },

        "Indomethacin": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với indomethacin hoặc NSAID",
                    "Loét dạ dày tá tràng tiến triển",
                    "Suy thận nặng",
                    "Suy tim nặng",
                ],
                "tương_đối": [
                    "Suy thận vừa",
                    "Suy gan vừa",
                    "Tăng huyết áp",
                    "Bệnh mạch vành",
                ],
            },
        },

        "Irbesartan": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với irbesartan hoặc ARB",
                    "Phụ nữ có thai (tháng 2-3, category D)",
                    "Hẹp động mạch thận hai bên hoặc một bên ở bệnh nhân một thận",
                ],
                "tương_đối": [
                    "Suy thận nặng (theo dõi chức năng thận)",
                    "Hạ huyết áp",
                    "Tăng kali máu",
                ],
            },
        },

        "Isosorbide mononitrate": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với isosorbide mononitrate hoặc nitrate",
                    "Hạ huyết áp nặng (systolic <90 mmHg)",
                    "Thiếu máu cơ tim cấp do hẹp động mạch chủ nặng",
                    "Đang dùng phosphodiesterase-5 inhibitors",
                ],
                "tương_đối": [
                    "Hạ huyết áp nhẹ-vừa",
                    "Thiếu máu nặng",
                    "Tăng áp lực nội sọ",
                ],
            },
        },

        "Isradipine": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với isradipine hoặc dihydropyridine calcium channel blocker",
                ],
                "tương_đối": [
                    "Hạ huyết áp nặng",
                    "Suy gan nặng",
                    "Suy tim nặng",
                ],
            },
        },

        "Ivabradine": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với ivabradine",
                    "Nhịp tim chậm <60 lần/phút",
                    "Suy tim cấp",
                    "Hạ huyết áp nặng",
                ],
                "tương_đối": [
                    "Suy thận nặng (CrCl <15 mL/min)",
                    "Suy gan vừa-nặng",
                    "Rối loạn nhịp tim",
                ],
            },
        },

        "Ketoprofen": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với ketoprofen hoặc NSAID",
                    "Loét dạ dày tá tràng tiến triển",
                    "Suy thận nặng",
                    "Suy tim nặng",
                ],
                "tương_đối": [
                    "Suy thận vừa",
                    "Suy gan vừa",
                    "Tăng huyết áp",
                    "Bệnh mạch vành",
                ],
            },
        },

        "Ketorolac": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với ketorolac hoặc NSAID",
                    "Loét dạ dày tá tràng tiến triển",
                    "Suy thận nặng",
                    "Chảy máu đang hoạt động",
                    "Phẫu thuật bắc cầu động mạch vành",
                ],
                "tương_đối": [
                    "Suy thận vừa",
                    "Suy gan vừa",
                    "Người cao tuổi (>65 tuổi)",
                    "Rối loạn đông máu",
                ],
            },
        },

        "Labetalol": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với labetalol hoặc beta-blocker",
                    "Block nhĩ-thất độ 2-3 không có máy tạo nhịp",
                    "Suy tim mất bù cấp",
                    "Hen phế quản nặng",
                ],
                "tương_đối": [
                    "Nhịp tim chậm",
                    "Hạ huyết áp",
                    "Suy tim vừa",
                    "COPD vừa",
                ],
            },
        },

        "Lacosamide": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với lacosamide",
                ],
                "tương_đối": [
                    "Suy thận nặng (CrCl <30 mL/min, cần điều chỉnh liều)",
                    "Suy gan nặng",
                    "Rối loạn nhịp tim",
                    "Bệnh tim",
                ],
            },
        },

        "Lisinopril": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với lisinopril hoặc ACE inhibitor",
                    "Phụ nữ có thai (tháng 2-3, category D)",
                    "Phù mạch do ACE inhibitor trước đó",
                    "Hẹp động mạch thận hai bên hoặc một bên ở bệnh nhân một thận",
                ],
                "tương_đối": [
                    "Suy thận nặng (theo dõi chức năng thận)",
                    "Hạ huyết áp",
                    "Tăng kali máu",
                    "Bệnh mô liên kết",
                ],
            },
        },

        "Losartan": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với losartan hoặc ARB",
                    "Phụ nữ có thai (tháng 2-3, category D)",
                    "Hẹp động mạch thận hai bên hoặc một bên ở bệnh nhân một thận",
                ],
                "tương_đối": [
                    "Suy thận nặng (theo dõi chức năng thận)",
                    "Hạ huyết áp",
                    "Tăng kali máu",
                ],
            },
        },

        "Lovastatin": {
            "contraindications_detail": {
                "tuyệt_đối": [
                    "Dị ứng với lovastatin hoặc statin",
                    "Bệnh gan hoạt động",
                    "Phụ nữ có thai hoặc cho con bú",
                    "Đang dùng thuốc ức chế CYP3A4 mạnh (cyclosporine, itraconazole, ketoconazole)",
                ],
                "tương_đối": [
                    "Suy gan vừa",
                    "Suy thận nặng",
                    "Rối loạn chức năng tuyến giáp",
                    "Tiền sử bệnh cơ",
                ],
            },
        },

    # ======================== BATCH 5: PREGNANCY & LACTATION SAFETY ========================
        "Metformin": {
            "pregnancy_lactation": {
                "fda_category": "B",
                "pregnancy_details": (
                    "Thường được xem là an toàn và hiệu quả trong thai kỳ, đặc biệt cho đái tháo đường thai kỳ (GDM) và PCOS. "
                    "Không thấy bằng chứng gây quái thai. Tuy nhiên, insulin vẫn là lựa chọn đầu tay chính thức trong nhiều hướng dẫn."
                ),
                "lactation": {
                    "safety": "Compatible",
                    "details": "Bài tiết vào sữa mẹ với lượng rất nhỏ (0.1-1% liều mẹ). Không ghi nhận tác dụng phụ ở trẻ bú mẹ.",
                    "recommendation": "Có thể sử dụng. An toàn khi cho con bú.",
                },
            },
        },

        "Amlodipine": {
            "pregnancy_lactation": {
                "fda_category": "C",
                "pregnancy_details": (
                    "Chưa có nghiên cứu đầy đủ trên người. Trên động vật có ghi nhận độc tính khi dùng liều cao. "
                    "Chỉ sử dụng khi lợi ích vượt trội nguy cơ. Nifedipine hoặc Methyldopa thường được ưu tiên hơn cho tăng huyết áp thai kỳ."
                ),
                "lactation": {
                    "safety": "Caution",
                    "details": "Chưa rõ mức độ bài tiết vào sữa mẹ. Các thuốc chẹn kênh canxi khác (như Nifedipine) có thông tin an toàn rõ ràng hơn.",
                    "recommendation": "Thận trọng. Cân nhắc chuyển sang thuốc an toàn hơn nếu có thể, hoặc theo dõi trẻ.",
                },
            },
        },

        "Atorvastatin": {
            "pregnancy_lactation": {
                "fda_category": "X",
                "pregnancy_details": (
                    "CHỐNG CHỈ ĐỊNH. Statin can thiệp vào tổng hợp cholesterol cần thiết cho sự phát triển của thai nhi. "
                    "Ngưng thuốc ngay lập tức nếu phát hiện có thai."
                ),
                "lactation": {
                    "safety": "Avoid",
                    "details": "Có khả năng bài tiết vào sữa mẹ và gây ảnh hưởng đến chuyển hóa lipid của trẻ.",
                    "recommendation": "Không sử dụng. Ngưng cho con bú hoặc ngưng thuốc.",
                },
            },
        },

        "Cephalexin": {
            "pregnancy_lactation": {
                "fda_category": "B",
                "pregnancy_details": (
                    "An toàn. Được sử dụng rộng rãi trong thai kỳ để điều trị nhiễm trùng tiểu và hô hấp. Không có bằng chứng gây hại."
                ),
                "lactation": {
                    "safety": "Compatible",
                    "details": "Bài tiết vào sữa mẹ lượng nhỏ. An toàn cho trẻ bú mẹ.",
                    "recommendation": "Có thể sử dụng. Theo dõi tiêu chảy ở trẻ.",
                },
            },
        },

        "Omeprazole": {
            "pregnancy_lactation": {
                "fda_category": "C",
                "pregnancy_details": (
                    "Dữ liệu lớn trên người không cho thấy nguy cơ dị tật. Tuy nhiên FDA xếp loại C do một số nghiên cứu động vật. "
                    "Thường được dùng khi các thuốc kháng H2 không hiệu quả."
                ),
                "lactation": {
                    "safety": "Compatible",
                    "details": "Bài tiết vào sữa mẹ lượng nhỏ (khoảng 7% liều mẹ). Bị phá hủy phần lớn bởi acid dạ dày của trẻ.",
                    "recommendation": "Có thể sử dụng. Được coi là an toàn.",
                },
            },
        },

        "Loratadine": {
            "pregnancy_lactation": {
                "fda_category": "B",
                "pregnancy_details": (
                    "An toàn. Là lựa chọn thuốc kháng histamin thế hệ 2 ưu tiên trong thai kỳ.",
                ),
                "lactation": {
                    "safety": "Compatible",
                    "details": "Bài tiết vào sữa mẹ lượng rất nhỏ. AAP xếp vào nhóm thuốc an toàn.",
                    "recommendation": "Có thể sử dụng.",
                },
            },
        },

    # ======================== SESSION 5: CORTICOSTEROIDS & SSRIs ========================
        "Prednisone": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "endocrine": "High (adrenal insufficiency - can be fatal if stopped abruptly after long-term use, Black Box Warning)",
                    "metabolic": "High (hyperglycemia - very common, can cause steroid-induced diabetes)",
                    "cardiovascular": "High (hypertension - very common)",
                    "skeletal": "High (osteoporosis - very common with long-term use)",
                    "gastrointestinal": "High (peptic ulcer disease - increased risk, especially with NSAIDs)",
                    "immunologic": "High (increased risk of serious infections - Black Box Warning)",
                    "ophthalmic": "Moderate (cataracts, glaucoma - with long-term use)",
                    "dermatologic": "Moderate (Cushingoid appearance - moon face, buffalo hump, striae)",
                    "neuropsychiatric": "Moderate (psychosis, mania, depression - especially with high doses)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Blood glucose - CRITICAL (hyperglycemia very common, can cause steroid-induced diabetes)",
                    "Blood pressure - CRITICAL (hypertension very common)",
                    "Signs of infection - CRITICAL (increased risk of serious infections, Black Box Warning)",
                    "Signs of adrenal insufficiency (fatigue, weakness, hypotension, hyponatremia) - CRITICAL (if stopped abruptly after >2 weeks use, can be fatal, Black Box Warning)",
                    "Bone density (DEXA scan) - CRITICAL (if long-term use >3 months, osteoporosis risk)",
                    "Signs of peptic ulcer (abdominal pain, melena, hematemesis) - CRITICAL (increased risk, especially with NSAIDs)",
                    "Weight and Cushingoid appearance - CRITICAL (moon face, buffalo hump, striae - very common)",
                    "Ophthalmologic exam - CRITICAL (if long-term use, cataracts, glaucoma risk)",
                    "Neuropsychiatric symptoms - CRITICAL (psychosis, mania, depression - especially with high doses)",
                    "Taper schedule - CRITICAL (must taper gradually if used >2 weeks to avoid adrenal insufficiency, Black Box Warning)"
                ],
                "look_alike_sound_alike": ["Prednisone", "Prednisolone", "Methylprednisolone", "Dexamethasone"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Adrenal Insufficiency (Can Be Fatal If Stopped Abruptly After Long-Term Use)",
                "FDA Black Box Warning - Increased Risk of Serious Infections",
                "FDA Drug Label - Prednisone",
                "ACR Guidelines - Rheumatoid Arthritis",
                "GINA Guidelines - Asthma Management",
                "GOLD Guidelines - COPD Management",
                "KDIGO Guidelines - Kidney Disease"
            ]
        },

        "Methylprednisolone": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "endocrine": "High (adrenal insufficiency - can be fatal if stopped abruptly after long-term use, Black Box Warning)",
                    "metabolic": "High (hyperglycemia - very common, can cause steroid-induced diabetes, especially with high-dose pulse therapy)",
                    "cardiovascular": "High (hypertension - very common)",
                    "skeletal": "High (osteoporosis - very common with long-term use)",
                    "gastrointestinal": "High (peptic ulcer disease - increased risk, especially with NSAIDs)",
                    "immunologic": "High (increased risk of serious infections - Black Box Warning)",
                    "neuropsychiatric": "High (psychosis, mania, depression - especially with high-dose pulse therapy)",
                    "ophthalmic": "Moderate (cataracts, glaucoma - with long-term use)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Blood glucose - CRITICAL (hyperglycemia very common, especially with high-dose pulse therapy)",
                    "Blood pressure - CRITICAL (hypertension very common)",
                    "Signs of infection - CRITICAL (increased risk of serious infections, Black Box Warning)",
                    "Signs of adrenal insufficiency (fatigue, weakness, hypotension, hyponatremia) - CRITICAL (if stopped abruptly after >2 weeks use, can be fatal, Black Box Warning)",
                    "Neuropsychiatric symptoms - CRITICAL (psychosis, mania, depression - especially with high-dose pulse therapy)",
                    "Bone density (DEXA scan) - CRITICAL (if long-term use >3 months, osteoporosis risk)",
                    "Signs of peptic ulcer (abdominal pain, melena, hematemesis) - CRITICAL (increased risk, especially with NSAIDs)",
                    "Taper schedule - CRITICAL (must taper gradually if used >2 weeks to avoid adrenal insufficiency, Black Box Warning)",
                    "High-dose pulse therapy monitoring - CRITICAL (monitor for hyperglycemia, psychosis, infections)"
                ],
                "look_alike_sound_alike": ["Methylprednisolone", "Solu-Medrol", "Medrol", "Prednisone", "Prednisolone"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Adrenal Insufficiency (Can Be Fatal If Stopped Abruptly After Long-Term Use)",
                "FDA Black Box Warning - Increased Risk of Serious Infections",
                "FDA Drug Label - Methylprednisolone (Solu-Medrol, Medrol)",
                "ACR Guidelines - Rheumatoid Arthritis",
                "KDIGO Guidelines - Lupus Nephritis",
                "AANS/CNS Guidelines - Spinal Cord Injury"
            ]
        },

        "Dexamethasone": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "endocrine": "High (adrenal insufficiency - can be fatal if stopped abruptly after long-term use, Black Box Warning)",
                    "metabolic": "High (hyperglycemia - very common, can cause steroid-induced diabetes)",
                    "cardiovascular": "High (hypertension - very common)",
                    "skeletal": "High (osteoporosis - very common with long-term use)",
                    "gastrointestinal": "High (peptic ulcer disease - increased risk, especially with NSAIDs)",
                    "immunologic": "High (increased risk of serious infections - Black Box Warning)",
                    "ophthalmic": "Moderate (cataracts, glaucoma - with long-term use)",
                    "neuropsychiatric": "Moderate (psychosis, mania, depression - especially with high doses)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Blood glucose - CRITICAL (hyperglycemia very common, can cause steroid-induced diabetes)",
                    "Blood pressure - CRITICAL (hypertension very common)",
                    "Signs of infection - CRITICAL (increased risk of serious infections, Black Box Warning)",
                    "Signs of adrenal insufficiency (fatigue, weakness, hypotension, hyponatremia) - CRITICAL (if stopped abruptly after >2 weeks use, can be fatal, Black Box Warning)",
                    "Bone density (DEXA scan) - CRITICAL (if long-term use >3 months, osteoporosis risk)",
                    "Signs of peptic ulcer (abdominal pain, melena, hematemesis) - CRITICAL (increased risk, especially with NSAIDs)",
                    "Taper schedule - CRITICAL (must taper gradually if used >2 weeks to avoid adrenal insufficiency, Black Box Warning)",
                    "Long half-life - CRITICAL (36-72 hours, longer than prednisone, effects persist longer)"
                ],
                "look_alike_sound_alike": ["Dexamethasone", "Decadron", "Prednisone", "Methylprednisolone"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Adrenal Insufficiency (Can Be Fatal If Stopped Abruptly After Long-Term Use)",
                "FDA Black Box Warning - Increased Risk of Serious Infections",
                "FDA Drug Label - Dexamethasone (Decadron)",
                "WHO Guidelines - COVID-19 Treatment (Severe Cases)",
                "ACR Guidelines - Rheumatoid Arthritis",
                "KDIGO Guidelines - Kidney Disease"
            ]
        },

        "Citalopram": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "cardiac": "High (QT prolongation - can be serious, Black Box Warning, dose limit 40mg/day, 20mg/day if >60 years old)",
                    "neuropsychiatric": "High (suicidal ideation and behavior - increased risk in children, adolescents, and young adults <24 years, Black Box Warning)"
                },
                "qt_prolongation": True,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Mood and depressive/anxiety symptoms - CRITICAL (periodic assessment)",
                    "Signs of suicidal ideation and behavior - CRITICAL (increased risk in first few weeks, especially in <24 years old, Black Box Warning)",
                    "ECG (QT interval) - CRITICAL (if dose >40mg/day or in elderly >60 years, QT prolongation risk, Black Box Warning)",
                    "Signs of serotonin syndrome (if used with other serotonergic drugs) - CRITICAL",
                    "INR (if used with warfarin) - CRITICAL (may increase bleeding risk)",
                    "Signs of withdrawal when discontinuing - CRITICAL",
                    "Dose limit - CRITICAL (max 40mg/day, 20mg/day if >60 years old, Black Box Warning)",
                    "Drug interactions (MAO inhibitors - CONTRAINDICATED, QT-prolonging drugs - AVOID, warfarin - monitor INR) - CRITICAL"
                ],
                "look_alike_sound_alike": ["Citalopram", "Celexa", "Escitalopram", "Lexapro"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Suicidal Ideation and Behavior (Increased Risk in Children, Adolescents, and Young Adults <24 Years)",
                "FDA Black Box Warning - QT Prolongation (Dose Limit 40mg/Day, 20mg/Day If >60 Years Old)",
                "FDA Drug Label - Citalopram (Celexa)",
                "APA Guidelines - Depression Treatment",
                "NICE Guidelines - Depression Treatment"
            ]
        },

        "Sertraline": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "neuropsychiatric": "High (suicidal ideation and behavior - increased risk in children, adolescents, and young adults <24 years, Black Box Warning)",
                    "hepatic": "Low (hepatotoxicity - rare but can occur)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": True,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Mood and depressive/anxiety symptoms - CRITICAL (periodic assessment)",
                    "Signs of suicidal ideation and behavior - CRITICAL (increased risk in first few weeks, especially in <24 years old, Black Box Warning)",
                    "Hepatic function (ALT, AST) - CRITICAL (if symptoms of liver injury, rare hepatotoxicity)",
                    "Signs of serotonin syndrome (if used with other serotonergic drugs) - CRITICAL",
                    "INR (if used with warfarin) - CRITICAL (may increase bleeding risk)",
                    "Signs of withdrawal when discontinuing - CRITICAL",
                    "Drug interactions (MAO inhibitors - CONTRAINDICATED, warfarin - monitor INR) - CRITICAL"
                ],
                "look_alike_sound_alike": ["Sertraline", "Zoloft", "Citalopram", "Escitalopram"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Suicidal Ideation and Behavior (Increased Risk in Children, Adolescents, and Young Adults <24 Years)",
                "FDA Drug Label - Sertraline (Zoloft)",
                "APA Guidelines - Depression Treatment",
                "NICE Guidelines - Depression Treatment"
            ]
        },

    # ======================== SESSION 6: SSRIs, SNRIs, TCAs & STATINS ========================
        "Fluoxetine": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "neuropsychiatric": "High (suicidal ideation and behavior - increased risk in children, adolescents, and young adults <24 years, Black Box Warning)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Mood and depressive/anxiety symptoms - CRITICAL (periodic assessment)",
                    "Signs of suicidal ideation and behavior - CRITICAL (increased risk in first few weeks, especially in <24 years old, Black Box Warning)",
                    "Signs of serotonin syndrome (if used with other serotonergic drugs) - CRITICAL",
                    "Long half-life - CRITICAL (4-6 days, active metabolite norfluoxetine 4-16 days, effects persist long after discontinuation)",
                    "Drug interactions (MAO inhibitors - CONTRAINDICATED, CYP2D6 inhibitors - may increase levels) - CRITICAL"
                ],
                "look_alike_sound_alike": ["Fluoxetine", "Prozac", "Citalopram", "Sertraline"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Suicidal Ideation and Behavior (Increased Risk in Children, Adolescents, and Young Adults <24 Years)",
                "FDA Drug Label - Fluoxetine (Prozac)",
                "APA Guidelines - Depression Treatment",
                "NICE Guidelines - Depression Treatment"
            ]
        },

        "Escitalopram": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "neuropsychiatric": "High (suicidal ideation and behavior - increased risk in children, adolescents, and young adults <24 years, Black Box Warning)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Mood and depressive/anxiety symptoms - CRITICAL (periodic assessment)",
                    "Signs of suicidal ideation and behavior - CRITICAL (increased risk in first few weeks, especially in <24 years old, Black Box Warning)",
                    "Signs of serotonin syndrome (if used with other serotonergic drugs) - CRITICAL",
                    "INR (if used with warfarin) - CRITICAL (may increase bleeding risk)",
                    "Drug interactions (MAO inhibitors - CONTRAINDICATED, warfarin - monitor INR) - CRITICAL"
                ],
                "look_alike_sound_alike": ["Escitalopram", "Lexapro", "Citalopram", "Celexa"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Suicidal Ideation and Behavior (Increased Risk in Children, Adolescents, and Young Adults <24 Years)",
                "FDA Drug Label - Escitalopram (Lexapro)",
                "APA Guidelines - Depression Treatment",
                "NICE Guidelines - Depression Treatment"
            ]
        },

        "Venlafaxine": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "neuropsychiatric": "High (suicidal ideation and behavior - increased risk in children, adolescents, and young adults <24 years, Black Box Warning)",
                    "cardiovascular": "Moderate (hypertension - dose-dependent, especially at higher doses >225mg/day)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Mood and depressive/anxiety symptoms - CRITICAL (periodic assessment)",
                    "Signs of suicidal ideation and behavior - CRITICAL (increased risk in first few weeks, especially in <24 years old, Black Box Warning)",
                    "Blood pressure - CRITICAL (hypertension risk, especially at higher doses >225mg/day)",
                    "Heart rate - CRITICAL (tachycardia can occur)",
                    "Signs of serotonin syndrome (if used with other serotonergic drugs) - CRITICAL",
                    "Signs of withdrawal when discontinuing - CRITICAL (withdrawal syndrome common if stopped abruptly)",
                    "Drug interactions (MAO inhibitors - CONTRAINDICATED) - CRITICAL"
                ],
                "look_alike_sound_alike": ["Venlafaxine", "Effexor", "Desvenlafaxine", "Pristiq"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Suicidal Ideation and Behavior (Increased Risk in Children, Adolescents, and Young Adults <24 Years)",
                "FDA Drug Label - Venlafaxine (Effexor)",
                "APA Guidelines - Depression Treatment",
                "NICE Guidelines - Depression Treatment"
            ]
        },

        "Duloxetine": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "neuropsychiatric": "High (suicidal ideation and behavior - increased risk in children, adolescents, and young adults <24 years, Black Box Warning)",
                    "hepatic": "Moderate (hepatotoxicity - rare but serious, contraindicated in severe hepatic impairment, Black Box Warning)",
                    "cardiovascular": "Moderate (hypertension - dose-dependent)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": True,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Mood and depressive/anxiety symptoms - CRITICAL (periodic assessment)",
                    "Signs of suicidal ideation and behavior - CRITICAL (increased risk in first few weeks, especially in <24 years old, Black Box Warning)",
                    "Hepatic function (ALT, AST) - CRITICAL (hepatotoxicity risk, contraindicated in severe hepatic impairment, Black Box Warning)",
                    "Blood pressure - CRITICAL (hypertension risk, especially at higher doses)",
                    "Signs of serotonin syndrome (if used with other serotonergic drugs) - CRITICAL",
                    "Signs of withdrawal when discontinuing - CRITICAL (withdrawal syndrome common if stopped abruptly)",
                    "Drug interactions (MAO inhibitors - CONTRAINDICATED) - CRITICAL"
                ],
                "look_alike_sound_alike": ["Duloxetine", "Cymbalta", "Venlafaxine", "Effexor"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Suicidal Ideation and Behavior (Increased Risk in Children, Adolescents, and Young Adults <24 Years)",
                "FDA Black Box Warning - Severe Hepatic Impairment (Contraindicated)",
                "FDA Drug Label - Duloxetine (Cymbalta)",
                "APA Guidelines - Depression Treatment",
                "NICE Guidelines - Depression Treatment"
            ]
        },

        "Amitriptyline": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": True,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "cardiac": "High (arrhythmias, AV block, QT prolongation - can be fatal in overdose, Black Box Warning)",
                    "neuropsychiatric": "High (suicidal ideation and behavior - increased risk in children, adolescents, and young adults <24 years, Black Box Warning, overdose can be fatal)",
                    "anticholinergic": "High (dry mouth, constipation, urinary retention, blurred vision, confusion - very common)"
                },
                "qt_prolongation": True,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "ECG - CRITICAL (before starting and periodically, QT prolongation, AV block risk, Black Box Warning)",
                    "Heart rate and blood pressure - CRITICAL (arrhythmias, orthostatic hypotension)",
                    "Mood and depressive symptoms - CRITICAL (periodic assessment)",
                    "Signs of suicidal ideation and behavior - CRITICAL (increased risk in first few weeks, especially in <24 years old, Black Box Warning)",
                    "Signs of overdose (tachycardia, arrhythmias, seizures, coma) - CRITICAL (can be fatal, Black Box Warning)",
                    "Anticholinergic symptoms (dry mouth, constipation, urinary retention, blurred vision) - CRITICAL (very common)",
                    "Drug interactions (MAO inhibitors - CONTRAINDICATED, quinidine/cimetidine - increase levels) - CRITICAL",
                    "Prescribe limited quantities - CRITICAL (overdose can be fatal, Black Box Warning)"
                ],
                "look_alike_sound_alike": ["Amitriptyline", "Elavil", "Nortriptyline", "Imipramine"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Suicidal Ideation and Behavior (Increased Risk in Children, Adolescents, and Young Adults <24 Years)",
                "FDA Black Box Warning - Overdose Can Be Fatal (Cardiac Arrhythmias, Seizures, Coma)",
                "FDA Drug Label - Amitriptyline (Elavil)",
                "APA Guidelines - Depression Treatment",
                "NICE Guidelines - Depression Treatment"
            ]
        },

        "Atorvastatin": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "musculoskeletal": "High (myopathy, rhabdomyolysis - rare but serious, can cause acute kidney injury, Black Box Warning)",
                    "hepatic": "Moderate (hepatotoxicity - elevated transaminases, rare but can occur)",
                    "metabolic": "Low (new-onset diabetes - slight increase in risk)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": True,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Muscle symptoms (myalgia, weakness) - CRITICAL (if severe, check CK, rhabdomyolysis risk, Black Box Warning)",
                    "Creatine kinase (CK) - CRITICAL (if muscle symptoms, stop if CK >10x ULN, Black Box Warning)",
                    "Hepatic function (ALT, AST) - CRITICAL (before starting, then if symptoms, hepatotoxicity risk)",
                    "Lipid profile (LDL, HDL, triglycerides) - CRITICAL (after 4-12 weeks, assess response)",
                    "Blood glucose - CRITICAL (new-onset diabetes risk, slight increase)",
                    "Drug interactions (CYP3A4 inhibitors - increase levels, fibrates - increase rhabdomyolysis risk, grapefruit juice - avoid) - CRITICAL",
                    "Pregnancy test - CRITICAL (contraindicated in pregnancy, Black Box Warning)"
                ],
                "look_alike_sound_alike": ["Atorvastatin", "Lipitor", "Simvastatin", "Rosuvastatin"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Myopathy and Rhabdomyolysis (Can Cause Acute Kidney Injury)",
                "FDA Black Box Warning - Teratogenicity (Contraindicated in Pregnancy)",
                "FDA Drug Label - Atorvastatin (Lipitor)",
                "ACC/AHA 2018 Cholesterol Guidelines",
                "ESC/EAS Guidelines for Dyslipidaemias 2019"
            ]
        },

        "Simvastatin": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "musculoskeletal": "High (myopathy, rhabdomyolysis - higher risk than atorvastatin, especially with 80mg dose, Black Box Warning)",
                    "hepatic": "Moderate (hepatotoxicity - elevated transaminases, rare but can occur)",
                    "metabolic": "Low (new-onset diabetes - slight increase in risk)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": True,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Muscle symptoms (myalgia, weakness) - CRITICAL (if severe, check CK, rhabdomyolysis risk, Black Box Warning)",
                    "Creatine kinase (CK) - CRITICAL (if muscle symptoms, stop if CK >10x ULN, Black Box Warning)",
                    "Hepatic function (ALT, AST) - CRITICAL (before starting, then if symptoms, hepatotoxicity risk)",
                    "Lipid profile (LDL, HDL, triglycerides) - CRITICAL (after 4 weeks, assess response)",
                    "Dose limit - CRITICAL (80mg dose NOT recommended except in patients stable on 80mg for >12 months, Black Box Warning)",
                    "Drug interactions (CYP3A4 inhibitors - increase levels significantly, amiodarone - limit to ≤20mg/day, diltiazem/verapamil - limit to ≤10mg/day, fibrates - increase rhabdomyolysis risk, grapefruit juice - avoid) - CRITICAL",
                    "Pregnancy test - CRITICAL (contraindicated in pregnancy, Black Box Warning)"
                ],
                "look_alike_sound_alike": ["Simvastatin", "Zocor", "Atorvastatin", "Lovastatin"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Myopathy and Rhabdomyolysis (Higher Risk, Especially with 80mg Dose)",
                "FDA Black Box Warning - 80mg Dose NOT Recommended (Except in Patients Stable on 80mg for >12 Months)",
                "FDA Black Box Warning - Teratogenicity (Contraindicated in Pregnancy)",
                "FDA Drug Label - Simvastatin (Zocor)",
                "FDA Drug Safety Communication - Simvastatin 80mg",
                "ACC/AHA 2018 Cholesterol Guidelines"
            ]
        },

    # ======================== SESSION 7: SSRIs, TCAs & STATINS (continued) ========================
        "Paroxetine": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "neuropsychiatric": "High (suicidal ideation and behavior - increased risk in children, adolescents, and young adults <24 years, Black Box Warning)",
                    "teratogenic": "High (teratogenicity - FDA category D, increased risk of cardiac defects, cleft lip/palate, Black Box Warning)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Mood and depressive/anxiety symptoms - CRITICAL (periodic assessment)",
                    "Signs of suicidal ideation and behavior - CRITICAL (increased risk in first few weeks, especially in <24 years old, Black Box Warning)",
                    "Signs of withdrawal when discontinuing - CRITICAL (withdrawal syndrome more common than other SSRIs due to short half-life)",
                    "Signs of serotonin syndrome (if used with other serotonergic drugs) - CRITICAL",
                    "INR (if used with warfarin) - CRITICAL (may increase bleeding risk)",
                    "Weight - CRITICAL (weight gain more common than other SSRIs)",
                    "Pregnancy test - CRITICAL (FDA category D, teratogenicity risk, Black Box Warning)",
                    "Drug interactions (MAO inhibitors - CONTRAINDICATED, CYP2D6 substrates - paroxetine is strong CYP2D6 inhibitor, warfarin - monitor INR) - CRITICAL"
                ],
                "look_alike_sound_alike": ["Paroxetine", "Paxil", "Citalopram", "Sertraline"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Suicidal Ideation and Behavior (Increased Risk in Children, Adolescents, and Young Adults <24 Years)",
                "FDA Black Box Warning - Teratogenicity (FDA Category D - Increased Risk of Cardiac Defects, Cleft Lip/Palate)",
                "FDA Drug Label - Paroxetine (Paxil)",
                "APA Guidelines - Depression Treatment",
                "NICE Guidelines - Depression Treatment"
            ]
        },

        "Fluvoxamine": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "neuropsychiatric": "High (suicidal ideation and behavior - increased risk in children, adolescents, and young adults <24 years, Black Box Warning)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Mood and depressive/anxiety/OCD symptoms - CRITICAL (periodic assessment)",
                    "Signs of suicidal ideation and behavior - CRITICAL (increased risk in first few weeks, especially in <24 years old, Black Box Warning)",
                    "Signs of serotonin syndrome (if used with other serotonergic drugs) - CRITICAL",
                    "INR (if used with warfarin) - CRITICAL (may increase bleeding risk)",
                    "Drug interactions - CRITICAL (MAO inhibitors - CONTRAINDICATED, tizanidine - CONTRAINDICATED, alosetron - CONTRAINDICATED, theophylline/caffeine - increase levels significantly, clozapine/olanzapine - increase levels, warfarin - monitor INR)",
                    "CYP450 interactions - CRITICAL (strong CYP1A2, CYP2C9, CYP3A4 inhibitor - many drug interactions)"
                ],
                "look_alike_sound_alike": ["Fluvoxamine", "Luvox", "Fluoxetine", "Paroxetine"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Suicidal Ideation and Behavior (Increased Risk in Children, Adolescents, and Young Adults <24 Years)",
                "FDA Drug Label - Fluvoxamine (Luvox)",
                "APA Guidelines - Depression Treatment",
                "NICE Guidelines - Depression Treatment"
            ]
        },

        "Nortriptyline": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": True,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "cardiac": "High (arrhythmias, AV block, QT prolongation - can be fatal in overdose, Black Box Warning)",
                    "neuropsychiatric": "High (suicidal ideation and behavior - increased risk in children, adolescents, and young adults <24 years, Black Box Warning, overdose can be fatal)",
                    "anticholinergic": "Moderate (dry mouth, constipation, urinary retention, blurred vision - less than amitriptyline)"
                },
                "qt_prolongation": True,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "ECG - CRITICAL (before starting and periodically, QT prolongation, AV block risk, Black Box Warning)",
                    "Heart rate and blood pressure - CRITICAL (arrhythmias, orthostatic hypotension)",
                    "Mood and depressive symptoms - CRITICAL (periodic assessment)",
                    "Signs of suicidal ideation and behavior - CRITICAL (increased risk in first few weeks, especially in <24 years old, Black Box Warning)",
                    "Signs of overdose (tachycardia, arrhythmias, seizures, coma) - CRITICAL (can be fatal, Black Box Warning)",
                    "Anticholinergic symptoms (dry mouth, constipation, urinary retention, blurred vision) - CRITICAL (less than amitriptyline but still common)",
                    "Drug interactions (MAO inhibitors - CONTRAINDICATED, quinidine/cimetidine - increase levels) - CRITICAL",
                    "Prescribe limited quantities - CRITICAL (overdose can be fatal, Black Box Warning)"
                ],
                "look_alike_sound_alike": ["Nortriptyline", "Pamelor", "Amitriptyline", "Imipramine"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Suicidal Ideation and Behavior (Increased Risk in Children, Adolescents, and Young Adults <24 Years)",
                "FDA Black Box Warning - Overdose Can Be Fatal (Cardiac Arrhythmias, Seizures, Coma)",
                "FDA Drug Label - Nortriptyline (Pamelor)",
                "APA Guidelines - Depression Treatment",
                "NICE Guidelines - Depression Treatment"
            ]
        },

        "Rosuvastatin": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "musculoskeletal": "High (myopathy, rhabdomyolysis - rare but serious, can cause acute kidney injury, Black Box Warning)",
                    "hepatic": "Moderate (hepatotoxicity - elevated transaminases, rare but can occur)",
                    "renal": "Moderate (proteinuria, hematuria - with high dose 40mg)",
                    "metabolic": "Low (new-onset diabetes - slight increase in risk)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": True,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Muscle symptoms (myalgia, weakness) - CRITICAL (if severe, check CK, rhabdomyolysis risk, Black Box Warning)",
                    "Creatine kinase (CK) - CRITICAL (if muscle symptoms, stop if CK >10x ULN, Black Box Warning)",
                    "Hepatic function (ALT, AST) - CRITICAL (before starting, then if symptoms, hepatotoxicity risk)",
                    "Renal function (proteinuria, hematuria) - CRITICAL (with 40mg dose, monitor for proteinuria)",
                    "Lipid profile (LDL, HDL, triglycerides) - CRITICAL (after 4-12 weeks, assess response)",
                    "Blood glucose - CRITICAL (new-onset diabetes risk, slight increase)",
                    "Asian patients - CRITICAL (consider starting dose 5mg, higher exposure)",
                    "Drug interactions (cyclosporine - limit to 5mg/day, gemfibrozil - avoid or limit to 10mg/day, warfarin - monitor INR) - CRITICAL",
                    "Pregnancy test - CRITICAL (contraindicated in pregnancy, Black Box Warning)"
                ],
                "look_alike_sound_alike": ["Rosuvastatin", "Crestor", "Atorvastatin", "Simvastatin"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Myopathy and Rhabdomyolysis (Can Cause Acute Kidney Injury)",
                "FDA Black Box Warning - Teratogenicity (Contraindicated in Pregnancy)",
                "FDA Drug Label - Rosuvastatin (Crestor)",
                "ACC/AHA 2018 Cholesterol Guidelines",
                "ESC/EAS Guidelines for Dyslipidaemias 2019",
                "JUPITER Study"
            ]
        },

    # ======================== SESSION 8: VASOPRESSORS, TCAs & STATINS (continued) ========================
        "Clomipramine": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": True,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "cardiac": "High (arrhythmias, AV block, QT prolongation - can be fatal in overdose, Black Box Warning)",
                    "neuropsychiatric": "High (suicidal ideation and behavior - increased risk in children, adolescents, and young adults <24 years, Black Box Warning, overdose can be fatal)",
                    "anticholinergic": "High (dry mouth, constipation, urinary retention, blurred vision - very common)",
                    "serotonergic": "High (serotonin syndrome - if used with SSRIs/MAOIs, Black Box Warning)"
                },
                "qt_prolongation": True,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "ECG - CRITICAL (before starting and periodically, QT prolongation, AV block risk, Black Box Warning)",
                    "Heart rate and blood pressure - CRITICAL (arrhythmias, orthostatic hypotension)",
                    "Mood and OCD symptoms - CRITICAL (periodic assessment, Y-BOCS score if available)",
                    "Signs of suicidal ideation and behavior - CRITICAL (increased risk in first few weeks, especially in <24 years old, Black Box Warning)",
                    "Signs of overdose (tachycardia, arrhythmias, seizures, coma) - CRITICAL (can be fatal, Black Box Warning)",
                    "Signs of serotonin syndrome (fever, agitation, tremor, hyperreflexia) - CRITICAL (if used with SSRIs/MAOIs, Black Box Warning)",
                    "Anticholinergic symptoms (dry mouth, constipation, urinary retention, blurred vision) - CRITICAL (very common)",
                    "Drug interactions (MAO inhibitors - CONTRAINDICATED, SSRIs - CONTRAINDICATED, quinidine/cimetidine - increase levels) - CRITICAL",
                    "Prescribe limited quantities - CRITICAL (overdose can be fatal, Black Box Warning)"
                ],
                "look_alike_sound_alike": ["Clomipramine", "Anafranil", "Amitriptyline", "Imipramine"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Suicidal Ideation and Behavior (Increased Risk in Children, Adolescents, and Young Adults <24 Years)",
                "FDA Black Box Warning - Overdose Can Be Fatal (Cardiac Arrhythmias, Seizures, Coma)",
                "FDA Black Box Warning - Serotonin Syndrome (If Used with SSRIs/MAOIs)",
                "FDA Drug Label - Clomipramine (Anafranil)",
                "APA Guidelines - OCD Treatment",
                "NICE Guidelines - OCD Treatment"
            ]
        },

        "Pravastatin": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "musculoskeletal": "Moderate (myopathy, rhabdomyolysis - rare but serious, lower risk than other statins)",
                    "hepatic": "Moderate (hepatotoxicity - elevated transaminases, rare but can occur)",
                    "metabolic": "Low (new-onset diabetes - slight increase in risk)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": True,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Muscle symptoms (myalgia, weakness) - CRITICAL (if severe, check CK, rhabdomyolysis risk)",
                    "Creatine kinase (CK) - CRITICAL (if muscle symptoms, stop if CK >10x ULN)",
                    "Hepatic function (ALT, AST) - CRITICAL (before starting, then if symptoms, hepatotoxicity risk)",
                    "Lipid profile (LDL, HDL, triglycerides) - CRITICAL (after 4-12 weeks, assess response)",
                    "Blood glucose - CRITICAL (new-onset diabetes risk, slight increase)",
                    "Drug interactions (cyclosporine - reduce dose, gemfibrozil - avoid or reduce dose) - CRITICAL (fewer interactions than other statins - not metabolized by CYP450)",
                    "Pregnancy test - CRITICAL (contraindicated in pregnancy)"
                ],
                "look_alike_sound_alike": ["Pravastatin", "Pravachol", "Atorvastatin", "Simvastatin"]
            },
            "guideline_tags": [
                "FDA Drug Label - Pravastatin (Pravachol)",
                "ACC/AHA 2018 Cholesterol Guidelines",
                "ESC/EAS Guidelines for Dyslipidaemias 2019"
            ]
        },

        "Lovastatin": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "musculoskeletal": "High (myopathy, rhabdomyolysis - rare but serious, especially with drug interactions, Black Box Warning)",
                    "hepatic": "Moderate (hepatotoxicity - elevated transaminases, rare but can occur)",
                    "metabolic": "Low (new-onset diabetes - slight increase in risk)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": True,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Muscle symptoms (myalgia, weakness) - CRITICAL (if severe, check CK, rhabdomyolysis risk, Black Box Warning)",
                    "Creatine kinase (CK) - CRITICAL (if muscle symptoms, stop if CK >10x ULN, Black Box Warning)",
                    "Hepatic function (ALT, AST) - CRITICAL (before starting, then if symptoms, hepatotoxicity risk)",
                    "Lipid profile (LDL, HDL, triglycerides) - CRITICAL (after 4-12 weeks, assess response)",
                    "Blood glucose - CRITICAL (new-onset diabetes risk, slight increase)",
                    "Drug interactions (CYP3A4 inhibitors - increase levels significantly, amiodarone - limit dose, diltiazem/verapamil - limit dose, fibrates - increase rhabdomyolysis risk, grapefruit juice - avoid) - CRITICAL",
                    "Pregnancy test - CRITICAL (contraindicated in pregnancy, Black Box Warning)"
                ],
                "look_alike_sound_alike": ["Lovastatin", "Mevacor", "Simvastatin", "Atorvastatin"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Myopathy and Rhabdomyolysis (Especially with Drug Interactions)",
                "FDA Black Box Warning - Teratogenicity (Contraindicated in Pregnancy)",
                "FDA Drug Label - Lovastatin (Mevacor)",
                "ACC/AHA 2018 Cholesterol Guidelines"
            ]
        },

        # ======================== PHASE 6: ANESTHESIA DRUGS ========================
        "Propofol": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "cardiovascular": "High (hypotension - very common, especially with rapid injection or hypovolemia)",
                    "respiratory": "High (apnea - very common, requires immediate respiratory support)",
                    "metabolic": "High (propofol infusion syndrome - rare but fatal, Black Box Warning: metabolic acidosis, rhabdomyolysis, cardiac failure, hyperlipidemia, hepatomegaly, with prolonged high-dose infusion >48 hours)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Blood pressure - CRITICAL (hypotension very common, especially with rapid injection or hypovolemia)",
                    "Respiratory rate and SpO2 - CRITICAL (apnea very common, requires immediate respiratory support)",
                    "ECG - CRITICAL (monitor for arrhythmias, especially with propofol infusion syndrome)",
                    "Signs of propofol infusion syndrome - CRITICAL (metabolic acidosis, rhabdomyolysis, cardiac failure, hyperlipidemia, hepatomegaly - Black Box Warning, with prolonged high-dose infusion >48 hours)",
                    "Creatine kinase (CK) - CRITICAL (if prolonged infusion, monitor for rhabdomyolysis)",
                    "Arterial blood gas (ABG) - CRITICAL (if prolonged infusion, monitor for metabolic acidosis)",
                    "Liver function tests - CRITICAL (if prolonged infusion, monitor for hepatomegaly)",
                    "Lipid panel - CRITICAL (if prolonged infusion, monitor for hyperlipidemia)",
                    "Injection site - CRITICAL (pain on injection common, can mix with lidocaine)",
                    "Do NOT exceed 4 mg/kg/hour for sedation - CRITICAL (Black Box Warning, increased risk of propofol infusion syndrome)"
                ],
                "look_alike_sound_alike": ["Propofol", "Diprivan", "Fospropofol"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Propofol Infusion Syndrome (Metabolic Acidosis, Rhabdomyolysis, Cardiac Failure with Prolonged High-Dose Infusion)",
                "ISMP High Alert Medications",
                "ASA Guidelines - Sedation and Anesthesia",
                "FDA Drug Label - Propofol (Diprivan)"
            ]
        },

        "Etomidate": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "endocrine": "High (adrenal suppression - inhibits cortisol synthesis, can cause adrenal insufficiency, especially with repeated doses or prolonged infusion)",
                    "cardiovascular": "Low (minimal cardiovascular effects - advantage over other induction agents)",
                    "respiratory": "Moderate (apnea - common but less than propofol)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Respiratory rate and SpO2 - CRITICAL (apnea common, requires respiratory support)",
                    "Blood pressure - CRITICAL (minimal effects, but monitor)",
                    "Adrenal function - CRITICAL (if repeated doses or prolonged infusion, monitor for adrenal insufficiency)",
                    "Cortisol levels - CRITICAL (if repeated doses or prolonged infusion, especially in sepsis or critical illness)",
                    "Signs of adrenal insufficiency (hypotension, hyponatremia, hyperkalemia) - CRITICAL (if repeated doses or prolonged infusion)",
                    "Injection site - CRITICAL (pain on injection common, can cause thrombophlebitis)"
                ],
                "look_alike_sound_alike": ["Etomidate", "Amidate", "Propofol"]
            },
            "guideline_tags": [
                "FDA Drug Label - Etomidate (Amidate)",
                "ASA Guidelines - Sedation and Anesthesia",
                "SCCM Guidelines - Critical Care Sedation (Note: Adrenal suppression concern)"
            ]
        },

        "Ketamine": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "cardiovascular": "Moderate (hypertension, tachycardia - common, due to sympathetic stimulation)",
                    "neurologic": "High (emergence reactions - hallucinations, nightmares, delirium - common, especially in adults)",
                    "respiratory": "Low (minimal respiratory depression - advantage, but can cause laryngospasm)",
                    "ophthalmic": "Moderate (increased intraocular pressure - transient)",
                    "intracranial": "Moderate (increased intracranial pressure - transient, controversial)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Blood pressure - CRITICAL (hypertension common, due to sympathetic stimulation)",
                    "Heart rate - CRITICAL (tachycardia common, due to sympathetic stimulation)",
                    "Mental status - CRITICAL (emergence reactions - hallucinations, nightmares, delirium - common, especially in adults)",
                    "Respiratory rate and SpO2 - CRITICAL (minimal respiratory depression, but can cause laryngospasm)",
                    "Intraocular pressure - CRITICAL (increased IOP transient, avoid in open eye injury)",
                    "Intracranial pressure - CRITICAL (increased ICP transient, controversial, avoid in increased ICP)",
                    "Salivary secretions - CRITICAL (increased secretions, can use atropine or glycopyrrolate)",
                    "Premedication with benzodiazepine - CRITICAL (to reduce emergence reactions, especially in adults)"
                ],
                "look_alike_sound_alike": ["Ketamine", "Ketalar", "Esketamine"]
            },
            "guideline_tags": [
                "FDA Drug Label - Ketamine (Ketalar)",
                "ASA Guidelines - Sedation and Anesthesia",
                "ACEP Guidelines - Procedural Sedation"
            ]
        },

        "Bupivacaine": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": True,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "cardiac": "High (cardiotoxicity - very high, ventricular arrhythmias, cardiac arrest - difficult to treat, Black Box Warning for IV use)",
                    "neurologic": "High (local anesthetic systemic toxicity - LAST - CNS toxicity: perioral numbness, metallic taste, tinnitus, seizures, coma)",
                    "hematologic": "Low (methemoglobinemia - rare, with prilocaine)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "ECG - CRITICAL (cardiotoxicity very high, ventricular arrhythmias, cardiac arrest - difficult to treat, Black Box Warning)",
                    "Signs of LAST (local anesthetic systemic toxicity) - CRITICAL (CNS: perioral numbness, metallic taste, tinnitus, seizures, coma; Cardiac: hypotension, bradycardia, ventricular arrhythmias, cardiac arrest)",
                    "Blood pressure and heart rate - CRITICAL (cardiotoxicity can cause severe hypotension, bradycardia, cardiac arrest)",
                    "Mental status - CRITICAL (CNS toxicity: seizures, coma)",
                    "Lipid emulsion 20% (Intralipid) - CRITICAL (MUST be available when using bupivacaine, antidote for LAST)",
                    "Maximum dose - CRITICAL (2 mg/kg without epinephrine, 3 mg/kg with epinephrine, Black Box Warning for IV use)",
                    "Do NOT use for IV regional anesthesia (Bier block) - CRITICAL (Black Box Warning, very high risk of cardiotoxicity)"
                ],
                "look_alike_sound_alike": ["Bupivacaine", "Marcaine", "Lidocaine", "Ropivacaine"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Cardiotoxicity (Ventricular Arrhythmias, Cardiac Arrest - Difficult to Treat)",
                "FDA Black Box Warning - Do NOT Use for IV Regional Anesthesia (Bier Block)",
                "ISMP High Alert Medications",
                "ASA Guidelines - Local Anesthetic Systemic Toxicity (LAST)",
                "FDA Drug Label - Bupivacaine (Marcaine)"
            ]
        },

        "Succinylcholine": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "cardiac": "High (hyperkalemia - can cause cardiac arrest, Black Box Warning; bradycardia - common, especially with repeated doses or in children)",
                    "metabolic": "High (malignant hyperthermia - rare but fatal, Black Box Warning)",
                    "musculoskeletal": "Moderate (myalgia - common, especially in ambulatory patients)",
                    "ophthalmic": "Moderate (increased intraocular pressure - transient)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "ECG - CRITICAL (hyperkalemia can cause cardiac arrest, Black Box Warning)",
                    "Serum potassium - CRITICAL (hyperkalemia can cause cardiac arrest, especially in burns, trauma, spinal cord injury, immobility, myopathies, Black Box Warning)",
                    "Signs of malignant hyperthermia - CRITICAL (hyperthermia, muscle rigidity, hypercapnia, tachycardia, arrhythmias - rare but fatal, Black Box Warning)",
                    "Temperature - CRITICAL (if signs of malignant hyperthermia)",
                    "End-tidal CO2 - CRITICAL (if signs of malignant hyperthermia - increased CO2)",
                    "Heart rate - CRITICAL (bradycardia common, especially with repeated doses or in children)",
                    "Intraocular pressure - CRITICAL (increased IOP transient, avoid in open eye injury)",
                    "Dantrolene availability - CRITICAL (antidote for malignant hyperthermia, must be available)",
                    "Pseudocholinesterase deficiency screening - CRITICAL (if prolonged paralysis, genetic deficiency can cause prolonged block)"
                ],
                "look_alike_sound_alike": ["Succinylcholine", "Suxamethonium", "Anectine", "Rocuronium"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Hyperkalemia (Can Cause Cardiac Arrest)",
                "FDA Black Box Warning - Malignant Hyperthermia (Rare but Fatal)",
                "ISMP High Alert Medications",
                "ASA Guidelines - Rapid Sequence Intubation",
                "FDA Drug Label - Succinylcholine (Anectine)"
            ]
        },

        "Rocuronium": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "respiratory": "High (apnea - complete paralysis, requires mechanical ventilation)",
                    "allergic": "Moderate (anaphylaxis - rare but can occur)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Respiratory rate and SpO2 - CRITICAL (complete paralysis, requires mechanical ventilation)",
                    "TOF (Train-of-Four) monitoring - CRITICAL (to assess neuromuscular blockade depth)",
                    "Signs of anaphylaxis - CRITICAL (rare but can occur)",
                    "Renal function - CRITICAL (prolonged duration in renal impairment)",
                    "Hepatic function - CRITICAL (prolonged duration in hepatic impairment)",
                    "Reversal agent availability - CRITICAL (Sugammadex or Neostigmine + Atropine must be available)"
                ],
                "look_alike_sound_alike": ["Rocuronium", "Zemuron", "Esmeron", "Vecuronium", "Succinylcholine"]
            },
            "guideline_tags": [
                "ASA Guidelines - Neuromuscular Blockade",
                "FDA Drug Label - Rocuronium (Zemuron, Esmeron)"
            ]
        },

        "Vecuronium": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "respiratory": "High (apnea - complete paralysis, requires mechanical ventilation)",
                    "allergic": "Moderate (anaphylaxis - rare but can occur)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Respiratory rate and SpO2 - CRITICAL (complete paralysis, requires mechanical ventilation)",
                    "TOF (Train-of-Four) monitoring - CRITICAL (to assess neuromuscular blockade depth)",
                    "Signs of anaphylaxis - CRITICAL (rare but can occur)",
                    "Renal function - CRITICAL (prolonged duration in renal impairment)",
                    "Hepatic function - CRITICAL (prolonged duration in hepatic impairment, vecuronium metabolized in liver)",
                    "Reversal agent availability - CRITICAL (Neostigmine + Atropine must be available, Sugammadex can also be used)"
                ],
                "look_alike_sound_alike": ["Vecuronium", "Norcuron", "Rocuronium", "Succinylcholine"]
            },
            "guideline_tags": [
                "ASA Guidelines - Neuromuscular Blockade",
                "FDA Drug Label - Vecuronium (Norcuron)"
            ]
        },

        # ======================== PHASE 6: PSYCHIATRY DRUGS ========================
        "Haloperidol": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "neurologic": "High (extrapyramidal symptoms - EPS - very common; tardive dyskinesia - can be irreversible; neuroleptic malignant syndrome - NMS - rare but fatal)",
                    "cardiac": "High (QT prolongation, torsades de pointes - can be fatal, especially with IV use or high doses)",
                    "metabolic": "Moderate (increased mortality in elderly with dementia - Black Box Warning)"
                },
                "qt_prolongation": True,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "ECG (QT interval) - CRITICAL (before and during treatment, especially with IV use or high doses, QT prolongation can cause torsades de pointes, can be fatal)",
                    "Signs of extrapyramidal symptoms (EPS) - CRITICAL (dystonia, parkinsonism, akathisia - very common)",
                    "Signs of tardive dyskinesia - CRITICAL (involuntary movements of face, tongue, limbs - can be irreversible, monitor periodically)",
                    "Signs of neuroleptic malignant syndrome (NMS) - CRITICAL (hyperthermia, muscle rigidity, altered mental status, autonomic instability - rare but fatal)",
                    "Temperature - CRITICAL (if signs of NMS)",
                    "Creatine kinase (CK) - CRITICAL (if signs of NMS - elevated CK)",
                    "Mortality in elderly with dementia - CRITICAL (Black Box Warning, increased risk of death)",
                    "Complete blood count - CRITICAL (rare leukopenia, agranulocytosis)",
                    "Drug interactions (QT-prolonging drugs - amiodarone, macrolides, ondansetron - increase QT prolongation risk) - CRITICAL"
                ],
                "look_alike_sound_alike": ["Haloperidol", "Haldol", "Risperidone", "Olanzapine"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Increased Mortality in Elderly with Dementia",
                "ISMP High Alert Medications",
                "APA Guidelines - Schizophrenia Treatment",
                "FDA Drug Label - Haloperidol (Haldol)"
            ]
        },

        "Risperidone": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "metabolic": "High (increased mortality in elderly with dementia - Black Box Warning; hyperglycemia, diabetes - common; weight gain - common; hyperprolactinemia - common)",
                    "neurologic": "Moderate (extrapyramidal symptoms - less than typical antipsychotics but can occur; tardive dyskinesia - can be irreversible)",
                    "cardiac": "Moderate (QT prolongation - less than typical antipsychotics but can occur)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Mortality in elderly with dementia - CRITICAL (Black Box Warning, increased risk of death)",
                    "Blood glucose and HbA1c - CRITICAL (hyperglycemia, diabetes - common, monitor periodically)",
                    "Weight - CRITICAL (weight gain - common, monitor periodically)",
                    "Prolactin levels - CRITICAL (hyperprolactinemia - common, can cause galactorrhea, menstrual disorders)",
                    "ECG (QT interval) - CRITICAL (if risk factors for QT prolongation)",
                    "Signs of extrapyramidal symptoms (EPS) - CRITICAL (less common than typical antipsychotics but can occur)",
                    "Signs of tardive dyskinesia - CRITICAL (can be irreversible, monitor periodically)",
                    "Signs of neuroleptic malignant syndrome (NMS) - CRITICAL (rare but fatal)",
                    "Lipid panel - CRITICAL (dyslipidemia can occur, monitor periodically)"
                ],
                "look_alike_sound_alike": ["Risperidone", "Risperdal", "Olanzapine", "Quetiapine"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Increased Mortality in Elderly with Dementia",
                "APA Guidelines - Schizophrenia Treatment",
                "FDA Drug Label - Risperidone (Risperdal)"
            ]
        },

        "Olanzapine": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "metabolic": "High (increased mortality in elderly with dementia - Black Box Warning; hyperglycemia, diabetes - common; weight gain - very common; dyslipidemia - common)",
                    "neurologic": "Low (extrapyramidal symptoms - less than typical antipsychotics; tardive dyskinesia - can occur)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Mortality in elderly with dementia - CRITICAL (Black Box Warning, increased risk of death)",
                    "Blood glucose and HbA1c - CRITICAL (hyperglycemia, diabetes - common, monitor periodically)",
                    "Weight - CRITICAL (weight gain - very common, monitor periodically)",
                    "Lipid panel - CRITICAL (dyslipidemia - common, monitor periodically)",
                    "Signs of extrapyramidal symptoms (EPS) - CRITICAL (less common than typical antipsychotics)",
                    "Signs of tardive dyskinesia - CRITICAL (can be irreversible, monitor periodically)",
                    "Signs of neuroleptic malignant syndrome (NMS) - CRITICAL (rare but fatal)"
                ],
                "look_alike_sound_alike": ["Olanzapine", "Zyprexa", "Risperidone", "Quetiapine"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Increased Mortality in Elderly with Dementia",
                "APA Guidelines - Schizophrenia Treatment",
                "FDA Drug Label - Olanzapine (Zyprexa)"
            ]
        },

        "Quetiapine": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "metabolic": "High (increased mortality in elderly with dementia - Black Box Warning; hyperglycemia, diabetes - common; weight gain - common; dyslipidemia - common)",
                    "neurologic": "Low (extrapyramidal symptoms - less than typical antipsychotics; tardive dyskinesia - can occur)",
                    "cardiac": "Moderate (QT prolongation - can occur, especially with high doses)",
                    "ophthalmic": "Moderate (cataracts - rare but can occur)"
                },
                "qt_prolongation": True,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Mortality in elderly with dementia - CRITICAL (Black Box Warning, increased risk of death)",
                    "ECG (QT interval) - CRITICAL (especially with high doses, QT prolongation can occur)",
                    "Blood glucose and HbA1c - CRITICAL (hyperglycemia, diabetes - common, monitor periodically)",
                    "Weight - CRITICAL (weight gain - common, monitor periodically)",
                    "Lipid panel - CRITICAL (dyslipidemia - common, monitor periodically)",
                    "Ophthalmic exam - CRITICAL (cataracts - rare but can occur, monitor periodically)",
                    "Signs of extrapyramidal symptoms (EPS) - CRITICAL (less common than typical antipsychotics)",
                    "Signs of tardive dyskinesia - CRITICAL (can be irreversible, monitor periodically)"
                ],
                "look_alike_sound_alike": ["Quetiapine", "Seroquel", "Olanzapine", "Risperidone"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Increased Mortality in Elderly with Dementia",
                "APA Guidelines - Schizophrenia Treatment",
                "FDA Drug Label - Quetiapine (Seroquel)"
            ]
        },

        "Lithium": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": True,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "renal": "High (nephrogenic diabetes insipidus - common; chronic kidney disease - can occur with long-term use)",
                    "neurologic": "High (neurotoxicity - tremor, ataxia, confusion, seizures, coma - with toxicity)",
                    "thyroid": "High (hypothyroidism - common; goiter - can occur)",
                    "cardiac": "Moderate (ECG changes - T-wave flattening/inversion, can occur)",
                    "endocrine": "Moderate (hyperparathyroidism - can occur with long-term use)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": True,
                "requires_monitoring": [
                    "Serum lithium levels - CRITICAL (therapeutic range 0.6-1.2 mEq/L, toxic >1.5 mEq/L, monitor every 3-6 months, more frequently during dose changes or if toxicity suspected)",
                    "Renal function (creatinine, eGFR) - CRITICAL (nephrogenic diabetes insipidus - common, chronic kidney disease - can occur with long-term use, monitor every 6-12 months)",
                    "Thyroid function (TSH, T4) - CRITICAL (hypothyroidism - common, goiter - can occur, monitor every 6-12 months)",
                    "Signs of neurotoxicity - CRITICAL (tremor, ataxia, confusion, seizures, coma - with toxicity)",
                    "ECG - CRITICAL (T-wave flattening/inversion can occur, monitor if cardiac symptoms)",
                    "Parathyroid hormone and calcium - CRITICAL (hyperparathyroidism - can occur with long-term use, monitor periodically)",
                    "Fluid and electrolyte balance - CRITICAL (dehydration increases lithium levels, risk of toxicity)",
                    "Drug interactions (diuretics, ACE inhibitors, NSAIDs - increase lithium levels, risk of toxicity) - CRITICAL"
                ],
                "look_alike_sound_alike": ["Lithium", "Lithobid", "Eskalith"]
            },
            "guideline_tags": [
                "ISMP High Alert Medications",
                "APA Guidelines - Bipolar Disorder Treatment",
                "FDA Drug Label - Lithium (Lithobid, Eskalith)"
            ]
        },

        # ======================== PHASE 6: ENDOCRINOLOGY - BISPHOSPHONATES ========================
        "Alendronate": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "gastrointestinal": "High (esophageal irritation, ulceration - common if not taken correctly)",
                    "skeletal": "High (osteonecrosis of the jaw - ONJ - rare but serious, Black Box Warning; atypical femur fractures - rare but serious, Black Box Warning)",
                    "metabolic": "Moderate (hypocalcemia, hypophosphatemia - can occur)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Signs of esophageal irritation (dysphagia, odynophagia, retrosternal pain) - CRITICAL (common if not taken correctly, must take with full glass of water, remain upright 30 minutes)",
                    "Dental exam - CRITICAL (before starting, ONJ risk, Black Box Warning)",
                    "Signs of osteonecrosis of the jaw (ONJ) - CRITICAL (jaw pain, swelling, loose teeth, exposed bone - rare but serious, Black Box Warning)",
                    "Signs of atypical femur fractures - CRITICAL (thigh or groin pain - rare but serious, Black Box Warning)",
                    "Serum calcium and phosphorus - CRITICAL (before and periodically, hypocalcemia risk)",
                    "Renal function (creatinine, eGFR) - CRITICAL (contraindicated if CrCl <35 ml/min)",
                    "Bone density (DEXA scan) - CRITICAL (before and after 1-2 years, monitor treatment response)",
                    "Administration technique - CRITICAL (must take on empty stomach, 30 minutes before food/medications, with full glass of water, remain upright 30 minutes)"
                ],
                "look_alike_sound_alike": ["Alendronate", "Fosamax", "Risedronate", "Ibandronate"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Osteonecrosis of the Jaw (ONJ - Rare but Serious)",
                "FDA Black Box Warning - Atypical Femur Fractures (Rare but Serious)",
                "NOF Guidelines - Osteoporosis Treatment",
                "FDA Drug Label - Alendronate (Fosamax)"
            ]
        },

        "Zoledronic acid": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "renal": "High (renal impairment - can be serious, Black Box Warning)",
                    "skeletal": "High (osteonecrosis of the jaw - ONJ - rare but serious, Black Box Warning; atypical femur fractures - rare but serious, Black Box Warning)",
                    "metabolic": "High (hypocalcemia - common, can be severe, Black Box Warning)",
                    "neurologic": "Moderate (acute phase reaction - flu-like symptoms - very common after first infusion)",
                    "ophthalmic": "Moderate (uveitis, scleritis - rare but can occur)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": True,
                "requires_monitoring": [
                    "Renal function (creatinine, eGFR) - CRITICAL (before each infusion, renal impairment risk, Black Box Warning, do NOT use if CrCl <35 ml/min for osteoporosis, <30 ml/min for cancer)",
                    "Serum calcium - CRITICAL (before and after infusion, hypocalcemia common and can be severe, Black Box Warning, ensure adequate calcium and vitamin D supplementation)",
                    "Serum phosphorus and magnesium - CRITICAL (before and after infusion, can be decreased)",
                    "Dental exam - CRITICAL (before starting, ONJ risk, Black Box Warning)",
                    "Signs of osteonecrosis of the jaw (ONJ) - CRITICAL (jaw pain, swelling, loose teeth, exposed bone - rare but serious, Black Box Warning)",
                    "Signs of atypical femur fractures - CRITICAL (thigh or groin pain - rare but serious, Black Box Warning)",
                    "Acute phase reaction - CRITICAL (fever, chills, myalgia, arthralgia - very common after first infusion, usually resolves within 24-72 hours)",
                    "Infusion rate - CRITICAL (must infuse over at least 15 minutes, Black Box Warning, rapid infusion increases renal impairment risk)",
                    "Hydration - CRITICAL (ensure adequate hydration before and after infusion, reduces renal impairment risk)"
                ],
                "look_alike_sound_alike": ["Zoledronic acid", "Zoledronate", "Zometa", "Reclast", "Alendronate"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Renal Impairment (Can Be Serious)",
                "FDA Black Box Warning - Hypocalcemia (Common, Can Be Severe)",
                "FDA Black Box Warning - Osteonecrosis of the Jaw (ONJ - Rare but Serious)",
                "FDA Black Box Warning - Atypical Femur Fractures (Rare but Serious)",
                "NOF Guidelines - Osteoporosis Treatment",
                "FDA Drug Label - Zoledronic acid (Zometa, Reclast)"
            ]
        },

        # ======================== PHASE 6: OBSTETRICS & GYNECOLOGY ========================
        "Oxytocin": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "reproductive": "High (uterine hyperstimulation - can cause uterine rupture, fetal distress, Black Box Warning)",
                    "cardiovascular": "Moderate (hypotension - common with rapid IV bolus, tachycardia - reflex)",
                    "metabolic": "High (water intoxication, hyponatremia - with prolonged high-dose infusion with hypotonic solutions, can cause seizures, coma, death)",
                    "neurologic": "High (seizures, coma - with water intoxication/hyponatremia)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Uterine contractions (frequency, intensity, duration) - CRITICAL (monitor continuously, hyperstimulation can cause uterine rupture, fetal distress, Black Box Warning)",
                    "Fetal heart rate - CRITICAL (if used during labor, monitor continuously, fetal distress risk with hyperstimulation)",
                    "Blood pressure and heart rate - CRITICAL (hypotension common with rapid IV bolus, tachycardia can occur)",
                    "Serum sodium - CRITICAL (if prolonged high-dose infusion, water intoxication/hyponatremia risk, can cause seizures, coma, death)",
                    "Fluid intake/output - CRITICAL (if prolonged infusion, monitor for water intoxication)",
                    "Signs of uterine rupture (severe abdominal pain, fetal distress, maternal shock) - CRITICAL (Black Box Warning)",
                    "Infusion rate - CRITICAL (do NOT give rapid IV bolus, must use controlled infusion pump, Black Box Warning)",
                    "Solution type - CRITICAL (do NOT use hypotonic solutions for prolonged infusion, use isotonic solutions to prevent hyponatremia)"
                ],
                "look_alike_sound_alike": ["Oxytocin", "Pitocin", "Syntocinon", "Vasopressin"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Uterine Hyperstimulation (Can Cause Uterine Rupture, Fetal Distress)",
                "ACOG Guidelines - Postpartum Hemorrhage",
                "ACOG Guidelines - Labor Induction and Augmentation",
                "WHO Guidelines - Prevention and Treatment of Postpartum Hemorrhage",
                "FDA Drug Label - Oxytocin (Pitocin)"
            ]
        },

        # ======================== PHASE 7: UROLOGY DRUGS ========================
        "Sildenafil": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "cardiovascular": "High (hypotension - can be severe and fatal with nitrates, Black Box Warning)",
                    "ophthalmic": "Moderate (non-arteritic anterior ischemic optic neuropathy - NAION - rare but can cause vision loss)",
                    "otologic": "Moderate (sudden hearing loss - rare but can occur)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Blood pressure - CRITICAL (hypotension can be severe and fatal with nitrates, Black Box Warning)",
                    "Nitrate use - CRITICAL (ABSOLUTELY CONTRAINDICATED with nitrates - nitroglycerin, isosorbide - can cause severe hypotension, death, Black Box Warning)",
                    "Signs of vision loss (NAION) - CRITICAL (sudden vision loss in one or both eyes - rare but can occur, stop immediately if present)",
                    "Signs of hearing loss - CRITICAL (sudden hearing loss - rare but can occur, stop immediately if present)",
                    "Cardiovascular status - CRITICAL (contraindicated in unstable cardiovascular disease, recent MI/stroke)",
                    "Drug interactions (alpha-blockers - separate by 4-6 hours, CYP3A4 inhibitors - reduce dose) - CRITICAL",
                    "Administration timing - CRITICAL (30-60 minutes before sexual activity, do NOT use more than once daily)"
                ],
                "look_alike_sound_alike": ["Sildenafil", "Viagra", "Tadalafil", "Vardenafil", "Avanafil"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Contraindicated with Nitrates (Can Cause Severe Hypotension, Death)",
                "FDA Black Box Warning - Vision Loss (NAION - Rare but Can Occur)",
                "FDA Black Box Warning - Hearing Loss (Sudden Hearing Loss - Rare but Can Occur)",
                "AUA Guidelines - Erectile Dysfunction Management",
                "FDA Drug Label - Sildenafil (Viagra)"
            ]
        },

        "Tamsulosin": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "cardiovascular": "Moderate (orthostatic hypotension - common, syncope - rare but can occur)",
                    "reproductive": "Moderate (retrograde ejaculation - common)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Blood pressure (especially orthostatic hypotension) - CRITICAL (common, can cause syncope)",
                    "BPH symptoms (difficulty urinating, weak stream, nocturia, urgency) - CRITICAL (monitor treatment response)",
                    "Signs of syncope - CRITICAL (rare but can occur, especially with first dose or dose increase)",
                    "Signs of retrograde ejaculation - CRITICAL (common, counsel patient)",
                    "Drug interactions (PDE-5 inhibitors - separate by 4-6 hours, antihypertensives - monitor BP) - CRITICAL",
                    "Administration - CRITICAL (take after same meal each day, do NOT crush or chew capsule)"
                ],
                "look_alike_sound_alike": ["Tamsulosin", "Flomax", "Alfuzosin", "Silodosin"]
            },
            "guideline_tags": [
                "AUA Guidelines - Benign Prostatic Hyperplasia Management",
                "FDA Drug Label - Tamsulosin (Flomax)"
            ]
        },

        "Finasteride": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "reproductive": "High (sexual dysfunction - decreased libido, erectile dysfunction, ejaculation disorders - common; persistent sexual dysfunction - can persist after discontinuation)",
                    "endocrine": "Moderate (decreased PSA - expected, can mask prostate cancer)",
                    "psychiatric": "Low (depression - rare but can occur)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Sexual function (libido, erectile function, ejaculation) - CRITICAL (sexual dysfunction common, can persist after discontinuation)",
                    "PSA levels - CRITICAL (decreased PSA expected, can mask prostate cancer, double PSA for interpretation)",
                    "Prostate exam - CRITICAL (periodically, decreased PSA can mask prostate cancer)",
                    "Mental health (depression) - CRITICAL (rare but can occur)",
                    "Pregnancy exposure - CRITICAL (contraindicated in women, can cause birth defects if exposed to male semen)"
                ],
                "look_alike_sound_alike": ["Finasteride", "Propecia", "Proscar", "Dutasteride"]
            },
            "guideline_tags": [
                "FDA Drug Label - Finasteride (Propecia, Proscar)",
                "AUA Guidelines - Benign Prostatic Hyperplasia Management",
                "FDA Warning - Sexual Dysfunction (Can Persist After Discontinuation)"
            ]
        },

        "Tadalafil": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "cardiovascular": "High (hypotension - can be severe and fatal with nitrates, Black Box Warning)",
                    "ophthalmic": "Moderate (non-arteritic anterior ischemic optic neuropathy - NAION - rare but can cause vision loss)",
                    "otologic": "Moderate (sudden hearing loss - rare but can occur)",
                    "musculoskeletal": "Moderate (back pain, myalgia - common, especially with daily dosing)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Blood pressure - CRITICAL (hypotension can be severe and fatal with nitrates, Black Box Warning)",
                    "Nitrate use - CRITICAL (ABSOLUTELY CONTRAINDICATED with nitrates - nitroglycerin, isosorbide - can cause severe hypotension, death, Black Box Warning)",
                    "Signs of vision loss (NAION) - CRITICAL (sudden vision loss in one or both eyes - rare but can occur, stop immediately if present)",
                    "Signs of hearing loss - CRITICAL (sudden hearing loss - rare but can occur, stop immediately if present)",
                    "Musculoskeletal symptoms (back pain, myalgia) - CRITICAL (common, especially with daily dosing)",
                    "Cardiovascular status - CRITICAL (contraindicated in unstable cardiovascular disease, recent MI/stroke)",
                    "Drug interactions (alpha-blockers - separate by 4-6 hours, CYP3A4 inhibitors - reduce dose) - CRITICAL",
                    "Long half-life - CRITICAL (17.5 hours, effects persist longer than sildenafil, do NOT use more than once daily)"
                ],
                "look_alike_sound_alike": ["Tadalafil", "Cialis", "Sildenafil", "Vardenafil"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Contraindicated with Nitrates (Can Cause Severe Hypotension, Death)",
                "FDA Black Box Warning - Vision Loss (NAION - Rare but Can Occur)",
                "FDA Black Box Warning - Hearing Loss (Sudden Hearing Loss - Rare but Can Occur)",
                "AUA Guidelines - Erectile Dysfunction Management",
                "FDA Drug Label - Tadalafil (Cialis)"
            ]
        },

        "Oxybutynin": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "neurologic": "Moderate (cognitive impairment - especially in elderly, anticholinergic effects)",
                    "ophthalmic": "Moderate (blurred vision, dry eyes - common)",
                    "urinary": "Moderate (urinary retention - can occur, especially with BPH)",
                    "gastrointestinal": "Moderate (constipation, dry mouth - very common)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Mental status (cognitive function) - CRITICAL (cognitive impairment especially in elderly, anticholinergic effects)",
                    "Urinary symptoms - CRITICAL (urinary retention can occur, especially with BPH)",
                    "Gastrointestinal symptoms (constipation, dry mouth) - CRITICAL (very common)",
                    "Ophthalmic symptoms (blurred vision, dry eyes) - CRITICAL (common)",
                    "Drug interactions (other anticholinergics - additive effects, cholinesterase inhibitors - antagonistic) - CRITICAL"
                ],
                "look_alike_sound_alike": ["Oxybutynin", "Ditropan", "Tolterodine", "Solifenacin"]
            },
            "guideline_tags": [
                "AUA Guidelines - Overactive Bladder Management",
                "FDA Drug Label - Oxybutynin (Ditropan)"
            ]
        },

        # ======================== PHASE 7: IMMUNOLOGY - mTOR INHIBITORS ========================
        "Sirolimus": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": True,
                "icu_critical_care_only": False,
                "bleeding_risk": True,
                "organ_toxicity": {
                    "pulmonary": "High (pneumonitis - rare but serious, can be fatal, Black Box Warning)",
                    "hematologic": "High (bone marrow suppression - thrombocytopenia, leukopenia - common, can be severe, Black Box Warning)",
                    "metabolic": "High (hyperlipidemia - very common)",
                    "oncologic": "High (increased risk of infections and malignancies - lymphoma, skin cancer, Black Box Warning)",
                    "renal": "Moderate (nephrotoxicity - when used with cyclosporine)",
                    "wound_healing": "Moderate (impaired wound healing - can occur)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": True,
                "requires_monitoring": [
                    "Sirolimus trough levels - CRITICAL (narrow therapeutic index, TDM required, target 4-12 ng/ml, Black Box Warning)",
                    "Pulmonary symptoms (cough, dyspnea, fever) - CRITICAL (pneumonitis rare but serious, can be fatal, Black Box Warning)",
                    "Chest X-ray or CT - CRITICAL (if signs of pneumonitis)",
                    "CBC (myelosuppression) - CRITICAL (thrombocytopenia, leukopenia common, can be severe, Black Box Warning)",
                    "Lipid profile (cholesterol, triglycerides) - CRITICAL (hyperlipidemia very common)",
                    "Renal function (creatinine, eGFR) - CRITICAL (nephrotoxicity risk, especially with cyclosporine)",
                    "Signs of infection (fever, chills) - CRITICAL (increased risk of serious infections, Black Box Warning)",
                    "Signs of malignancies (lymphoma, skin cancer) - CRITICAL (increased risk, Black Box Warning)",
                    "Wound healing - CRITICAL (impaired wound healing can occur, especially after surgery)",
                    "Drug interactions (CYP3A4 inhibitors/inducers - CRITICAL, grapefruit juice - increases levels, cyclosporine - increases nephrotoxicity) - CRITICAL"
                ],
                "look_alike_sound_alike": ["Sirolimus", "Rapamune", "Tacrolimus", "Everolimus"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Increased Risk of Infections and Malignancies",
                "FDA Black Box Warning - Pneumonitis (Rare but Serious, Can Be Fatal)",
                "FDA Black Box Warning - Myelosuppression (Thrombocytopenia, Leukopenia - Common, Can Be Severe)",
                "KDIGO Guidelines - Kidney Transplant",
                "AST Guidelines - Solid Organ Transplant",
                "FDA Drug Label - Sirolimus (Rapamune)"
            ]
        },

        "Everolimus": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": True,
                "icu_critical_care_only": False,
                "bleeding_risk": True,
                "organ_toxicity": {
                    "pulmonary": "High (pneumonitis - rare but serious, can be fatal, Black Box Warning)",
                    "hematologic": "High (bone marrow suppression - thrombocytopenia, leukopenia - common, can be severe, Black Box Warning)",
                    "metabolic": "High (hyperlipidemia - very common, hyperglycemia - common)",
                    "oncologic": "High (increased risk of infections and malignancies - lymphoma, skin cancer, Black Box Warning)",
                    "wound_healing": "Moderate (impaired wound healing - can occur)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Everolimus trough levels - CRITICAL (narrow therapeutic index, TDM required, target 3-8 ng/ml for transplant, Black Box Warning)",
                    "Pulmonary symptoms (cough, dyspnea, fever) - CRITICAL (pneumonitis rare but serious, can be fatal, Black Box Warning)",
                    "Chest X-ray or CT - CRITICAL (if signs of pneumonitis)",
                    "CBC (myelosuppression) - CRITICAL (thrombocytopenia, leukopenia common, can be severe, Black Box Warning)",
                    "Lipid profile (cholesterol, triglycerides) - CRITICAL (hyperlipidemia very common)",
                    "Blood glucose and HbA1c - CRITICAL (hyperglycemia common)",
                    "Signs of infection (fever, chills) - CRITICAL (increased risk of serious infections, Black Box Warning)",
                    "Signs of malignancies (lymphoma, skin cancer) - CRITICAL (increased risk, Black Box Warning)",
                    "Wound healing - CRITICAL (impaired wound healing can occur, especially after surgery)",
                    "Drug interactions (CYP3A4 inhibitors/inducers - CRITICAL, grapefruit juice - increases levels) - CRITICAL"
                ],
                "look_alike_sound_alike": ["Everolimus", "Afinitor", "Zortress", "Sirolimus"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Increased Risk of Infections and Malignancies",
                "FDA Black Box Warning - Pneumonitis (Rare but Serious, Can Be Fatal)",
                "FDA Black Box Warning - Myelosuppression (Thrombocytopenia, Leukopenia - Common, Can Be Severe)",
                "KDIGO Guidelines - Kidney Transplant",
                "NCCN Guidelines - Renal Cell Carcinoma",
                "NCCN Guidelines - Breast Cancer",
                "FDA Drug Label - Everolimus (Afinitor, Zortress)"
            ]
        },

        # ======================== PHASE 7: OTHER SPECIALIZED - GROWTH FACTORS ========================
        "Pegfilgrastim": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "hematologic": "Moderate (splenic rupture - rare but serious, can be fatal)",
                    "pulmonary": "Moderate (acute respiratory distress syndrome - ARDS - rare but serious)",
                    "skeletal": "Moderate (bone pain - very common, can be severe)",
                    "hematologic_sickle": "High (sickle cell crisis - in patients with sickle cell disease, can be fatal)"
                },
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "CBC (white blood cell count) - CRITICAL (monitor for leukocytosis, discontinue if WBC >100,000/mm³)",
                    "Signs of splenic rupture (left upper quadrant pain, shoulder pain) - CRITICAL (rare but serious, can be fatal)",
                    "Pulmonary symptoms (dyspnea, hypoxia) - CRITICAL (ARDS rare but serious)",
                    "Bone pain - CRITICAL (very common, can be severe, may need analgesics)",
                    "Sickle cell disease - CRITICAL (contraindicated, can cause sickle cell crisis, can be fatal)",
                    "Timing of administration - CRITICAL (give 24 hours after chemotherapy completion, do NOT give within 14 days before or 24 hours after chemotherapy)",
                    "Signs of sickle cell crisis (severe pain, fever) - CRITICAL (if used in sickle cell disease, can be fatal)"
                ],
                "look_alike_sound_alike": ["Pegfilgrastim", "Neulasta", "Filgrastim", "Sargramostim"]
            },
            "guideline_tags": [
                "FDA Drug Label - Pegfilgrastim (Neulasta)",
                "ASCO Guidelines - Myeloid Growth Factors",
                "NCCN Guidelines - Supportive Care"
            ]
        },

        "Hydroxychloroquine": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {
                    "ophthalmic": "High (retinal toxicity - can be irreversible and lead to vision loss, Black Box Warning)",
                    "cardiac": "High (QT prolongation, torsades de pointes, ventricular arrhythmias, cardiac arrest - can be fatal, Black Box Warning)",
                    "neurologic": "Moderate (psychosis, seizures - rare but can occur)",
                    "dermatologic": "Moderate (severe skin reactions - rare but can occur)",
                    "hematologic": "Low (myelosuppression - rare)"
                },
                "qt_prolongation": True,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Ophthalmologic exam - CRITICAL (baseline, then every 12 months, retinal toxicity can be irreversible and lead to vision loss, Black Box Warning)",
                    "Visual field testing - CRITICAL (baseline, then every 12 months, retinal toxicity)",
                    "ECG (QT interval) - CRITICAL (before and during treatment, QT prolongation can cause torsades de pointes, ventricular arrhythmias, cardiac arrest, can be fatal, Black Box Warning)",
                    "Signs of cardiac events (palpitations, dizziness, syncope, irregular heartbeat) - CRITICAL (QT prolongation can cause fatal arrhythmias, Black Box Warning)",
                    "Electrolytes (potassium, magnesium) - CRITICAL (must be normal before use, hypokalemia/hypomagnesemia increase arrhythmia risk)",
                    "Mental status - CRITICAL (psychosis, seizures rare but can occur)",
                    "Signs of severe skin reactions (rash, fever, mucosal lesions) - CRITICAL (rare but can occur)",
                    "CBC - CRITICAL (rare myelosuppression)",
                    "Drug interactions (QT-prolonging drugs - CONTRAINDICATED, digoxin - monitor levels) - CRITICAL",
                    "Maximum daily dose - CRITICAL (do NOT exceed 5mg/kg actual body weight, Black Box Warning, increases retinal toxicity risk)"
                ],
                "look_alike_sound_alike": ["Hydroxychloroquine", "Plaquenil", "Chloroquine", "Quinine"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Retinal Toxicity (Can Be Irreversible and Lead to Vision Loss)",
                "FDA Black Box Warning - QT Prolongation (Can Cause Fatal Arrhythmias)",
                "FDA Black Box Warning - Maximum Daily Dose (Do NOT Exceed 5mg/kg Actual Body Weight)",
                "ACR Guidelines - Systemic Lupus Erythematosus",
                "ACR Guidelines - Rheumatoid Arthritis",
                "FDA Drug Label - Hydroxychloroquine (Plaquenil)"
            ]
        },

}
