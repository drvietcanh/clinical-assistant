"""
Enhanced fields overrides - Analgesics
"""
from typing import Any, Dict


ANALGESICS_ENHANCED_FIELDS: Dict[str, Dict[str, Any]] = {
        # ======================== SESSION 1: OPIOIDS (STRONG), NSAIDs, PARACETAMOL ========================
        "Fentanyl": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": True,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"respiratory": "High (respiratory depression - can be fatal, especially with transdermal patch - Black Box Warning)", "neurologic": "High (CNS depression, sedation, confusion)", "cardiovascular": "Moderate (hypotension, bradycardia)"},
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Respiratory rate and SpO2 - CRITICAL (continuous monitoring, especially with transdermal patch - Black Box Warning)",
                    "Level of consciousness (GCS) - CRITICAL",
                    "Blood pressure and heart rate - CRITICAL",
                    "Pain score",
                    "Signs of overdose (decreased consciousness, slow breathing, miosis) - CRITICAL",
                    "With transdermal patch: monitor at least 24 hours after removal (accumulation risk) - CRITICAL",
                    "Renal function (CrCl, eGFR) - CRITICAL (accumulation in renal impairment)",
                    "Drug interactions (benzodiazepines, alcohol, CYP3A4 inhibitors - CONTRAINDICATED/AVOID) - CRITICAL"
                ],
                "look_alike_sound_alike": ["Fentanyl", "Duragesic", "Morphine", "Hydromorphone", "Sufentanil"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Respiratory Depression (Can Be Fatal)",
                "FDA Black Box Warning - Addiction, Abuse, and Misuse",
                "FDA Black Box Warning - Transdermal Patch (Not for Opioid-Naive Patients)",
                "FDA Drug Label - Fentanyl (respiratory depression and transdermal patch warnings)",
                "WHO Guidelines - Cancer Pain Management",
                "CDC Opioid Prescribing Guidelines"
            ]
        },

        "Morphine": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": True,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"respiratory": "High (respiratory depression - can be fatal, Black Box Warning)", "neurologic": "High (CNS depression, sedation, confusion)", "cardiovascular": "Moderate (hypotension, bradycardia)", "gastrointestinal": "High (constipation - very common)"},
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Respiratory rate and SpO2 - CRITICAL (Black Box Warning)",
                    "Level of consciousness (GCS) - CRITICAL",
                    "Blood pressure and heart rate - CRITICAL",
                    "Pain score",
                    "Signs of overdose (decreased consciousness, slow breathing, miosis) - CRITICAL",
                    "Constipation (prophylaxis recommended)",
                    "Renal function (CrCl, eGFR) - CRITICAL (accumulation in renal impairment)",
                    "Drug interactions (benzodiazepines, alcohol, MAO inhibitors - CONTRAINDICATED/AVOID) - CRITICAL"
                ],
                "look_alike_sound_alike": ["Morphine", "MS Contin", "Oxycodone", "Hydromorphone"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Respiratory Depression (Can Be Fatal)",
                "FDA Black Box Warning - Addiction, Abuse, and Misuse",
                "FDA Drug Label - Morphine (respiratory depression warnings)",
                "WHO Guidelines - Cancer Pain Management",
                "WHO Guidelines - Palliative Care",
                "CDC Opioid Prescribing Guidelines"
            ]
        },

        "Oxycodone": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": True,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"respiratory": "High (respiratory depression - can be fatal, Black Box Warning)", "neurologic": "High (CNS depression, sedation, confusion)", "cardiovascular": "Moderate (hypotension, bradycardia)", "gastrointestinal": "High (constipation - very common)"},
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Respiratory rate and SpO2 - CRITICAL (Black Box Warning)",
                    "Level of consciousness (GCS) - CRITICAL",
                    "Blood pressure and heart rate - CRITICAL",
                    "Pain score",
                    "Signs of overdose (decreased consciousness, slow breathing, miosis) - CRITICAL",
                    "Constipation (prophylaxis recommended)",
                    "Drug interactions (benzodiazepines, alcohol, CYP3A4 inhibitors - CONTRAINDICATED/AVOID) - CRITICAL"
                ],
                "look_alike_sound_alike": ["Oxycodone", "OxyContin", "Morphine", "Hydrocodone"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Respiratory Depression (Can Be Fatal)",
                "FDA Black Box Warning - Addiction, Abuse, and Misuse",
                "FDA Drug Label - Oxycodone (respiratory depression warnings)",
                "WHO Guidelines - Cancer Pain Management",
                "CDC Opioid Prescribing Guidelines"
            ]
        },

        "Aspirin": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": True,
                "organ_toxicity": {"gastrointestinal": "High (GI bleeding - common, especially with low-dose for cardiac protection)", "hepatic": "High (Reye syndrome in children <12 years - Black Box Warning, fatal)", "neurologic": "High (Reye syndrome in children <12 years - Black Box Warning, fatal)", "renal": "Moderate (renal impairment with long-term use)"},
                "qt_prolongation": False,
                "hepatotoxicity": True,
                "nephrotoxicity": True,
                "requires_monitoring": [
                    "Signs of GI bleeding (hematemesis, melena, abdominal pain) - CRITICAL (especially with low-dose)",
                    "Tinnitus - CRITICAL (early sign of salicylate toxicity)",
                    "Renal function (CrCl, BUN, creatinine) - CRITICAL (with long-term use)",
                    "Blood pressure",
                    "Hepatic function (ALT, AST) - CRITICAL (with long-term use, especially in children)",
                    "INR - CRITICAL (if using with warfarin - increased bleeding risk)",
                    "Age - CRITICAL (contraindicated in children <12 years - Black Box Warning)"
                ],
                "look_alike_sound_alike": ["Aspirin", "ASA", "Acetylsalicylic acid", "Ibuprofen", "Naproxen"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Reye Syndrome (Contraindicated in Children <12 Years)",
                "FDA Black Box Warning - GI Bleeding",
                "AHA/ACC Guidelines - Aspirin for Cardiovascular Disease Prevention",
                "FDA Drug Label - Aspirin (Reye syndrome and GI bleeding warnings)"
            ]
        },

        "Ibuprofen": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": True,
                "organ_toxicity": {"gastrointestinal": "High (GI bleeding, ulceration - common)", "cardiovascular": "Moderate (increased risk of MI, stroke, heart failure - Black Box Warning)", "renal": "Moderate (renal impairment, especially with long-term use or in high-risk patients)", "hepatic": "Low (hepatotoxicity - rare)"},
                "qt_prolongation": False,
                "hepatotoxicity": True,
                "nephrotoxicity": True,
                "requires_monitoring": [
                    "Signs of GI bleeding (hematemesis, melena, abdominal pain) - CRITICAL",
                    "Signs of cardiovascular events (chest pain, dyspnea, signs of heart failure) - CRITICAL (Black Box Warning)",
                    "Renal function (CrCl, BUN, creatinine) - CRITICAL (especially with long-term use or in high-risk patients)",
                    "Blood pressure",
                    "Hepatic function (ALT, AST) - if symptoms of liver injury",
                    "Drug interactions (warfarin, ACE inhibitors, diuretics) - CRITICAL"
                ],
                "look_alike_sound_alike": ["Ibuprofen", "Brufen", "Advil", "Naproxen", "Diclofenac"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Cardiovascular Risk (MI, Stroke, Heart Failure)",
                "FDA Black Box Warning - GI Bleeding",
                "FDA Drug Label - Ibuprofen (cardiovascular and GI warnings)"
            ]
        },

        "Naproxen": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": True,
                "organ_toxicity": {"gastrointestinal": "High (GI bleeding, ulceration - common)", "cardiovascular": "Moderate (increased risk of MI, stroke, heart failure - Black Box Warning)", "renal": "Moderate (renal impairment, especially with long-term use or in high-risk patients)", "hepatic": "Low (hepatotoxicity - rare)"},
                "qt_prolongation": False,
                "hepatotoxicity": True,
                "nephrotoxicity": True,
                "requires_monitoring": [
                    "Signs of GI bleeding (hematemesis, melena, abdominal pain) - CRITICAL",
                    "Signs of cardiovascular events (chest pain, dyspnea, signs of heart failure) - CRITICAL (Black Box Warning)",
                    "Renal function (CrCl, BUN, creatinine) - CRITICAL (especially with long-term use or in high-risk patients)",
                    "Blood pressure",
                    "Hepatic function (ALT, AST) - if symptoms of liver injury",
                    "Drug interactions (warfarin, ACE inhibitors, diuretics) - CRITICAL"
                ],
                "look_alike_sound_alike": ["Naproxen", "Naprosyn", "Aleve", "Ibuprofen", "Diclofenac"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Cardiovascular Risk (MI, Stroke, Heart Failure)",
                "FDA Black Box Warning - GI Bleeding",
                "FDA Drug Label - Naproxen (cardiovascular and GI warnings)"
            ]
        },

        "Paracetamol": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"hepatic": "High (hepatotoxicity - can be fatal with overdose, Black Box Warning)", "renal": "Moderate (nephrotoxicity with overdose)"},
                "qt_prolongation": False,
                "hepatotoxicity": True,
                "nephrotoxicity": True,
                "requires_monitoring": [
                    "Hepatic function (ALT, AST, bilirubin, PT/INR) - CRITICAL (with overdose or high doses, Black Box Warning)",
                    "Signs of hepatotoxicity (jaundice, abdominal pain, nausea, vomiting) - CRITICAL",
                    "Paracetamol level - CRITICAL (if overdose suspected, within 4-24 hours)",
                    "Renal function (CrCl, BUN, creatinine) - CRITICAL (with overdose)",
                    "Drug interactions (alcohol, warfarin, isoniazid) - CRITICAL",
                    "Daily dose - CRITICAL (max 4g/day, lower in hepatic impairment or with alcohol)"
                ],
                "look_alike_sound_alike": ["Paracetamol", "Acetaminophen", "Tylenol", "Panadol"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Hepatotoxicity (Can Be Fatal with Overdose)",
                "FDA Drug Label - Paracetamol (hepatotoxicity warning)",
                "WHO Guidelines - Pain Management",
                "UpToDate - Acetaminophen: Drug Information"
            ]
        },

        # ======================== SESSION 2: OPIOIDS (STRONG, WEAK, PARTIAL AGONISTS), NSAIDs ========================
        "Hydromorphone": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": True,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"respiratory": "High (respiratory depression - can be fatal, Black Box Warning)", "neurologic": "High (CNS depression, sedation, confusion)", "cardiovascular": "Moderate (hypotension, bradycardia)", "gastrointestinal": "High (constipation - very common)"},
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Respiratory rate and SpO2 - CRITICAL (Black Box Warning)",
                    "Level of consciousness (GCS) - CRITICAL",
                    "Blood pressure and heart rate - CRITICAL",
                    "Pain score",
                    "Signs of overdose (decreased consciousness, slow breathing, miosis) - CRITICAL",
                    "Constipation (prophylaxis recommended)",
                    "Dose adjustment - CRITICAL (5x more potent than morphine)"
                ],
                "look_alike_sound_alike": ["Hydromorphone", "Dilaudid", "Morphine", "Oxycodone"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Respiratory Depression (Can Be Fatal)",
                "FDA Black Box Warning - Addiction, Abuse, and Misuse",
                "FDA Drug Label - Hydromorphone (respiratory depression warnings)",
                "WHO Guidelines - Cancer Pain Management",
                "CDC Opioid Prescribing Guidelines"
            ]
        },

        "Methadone": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": True,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"respiratory": "High (respiratory depression - can be fatal, prolonged due to long half-life, Black Box Warning)", "cardiovascular": "High (QT prolongation, torsades de pointes - Black Box Warning)", "neurologic": "High (CNS depression, sedation, confusion, accumulation risk)"},
                "qt_prolongation": True,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Respiratory rate and SpO2 - CRITICAL (Black Box Warning, accumulation risk due to long half-life)",
                    "ECG (QT interval) - CRITICAL (QT prolongation, torsades de pointes risk - Black Box Warning)",
                    "Level of consciousness (GCS) - CRITICAL (accumulation risk)",
                    "Blood pressure and heart rate - CRITICAL",
                    "Pain score",
                    "Signs of accumulation/overdose (increased sedation, decreased respiratory rate) - CRITICAL (especially in first 1-2 weeks)",
                    "Drug interactions (CYP3A4 inhibitors/inducers, QT-prolonging drugs - CONTRAINDICATED/AVOID) - CRITICAL"
                ],
                "look_alike_sound_alike": ["Methadone", "Dolophine", "Morphine"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Respiratory Depression (Can Be Fatal, Accumulation Risk)",
                "FDA Black Box Warning - QT Prolongation and Torsades de Pointes",
                "FDA Black Box Warning - Addiction, Abuse, and Misuse",
                "FDA Drug Label - Methadone (respiratory depression and QT prolongation warnings)",
                "WHO Guidelines - Cancer Pain Management",
                "SAMHSA Guidelines - Opioid Maintenance Therapy"
            ]
        },

        "Codeine": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"respiratory": "Moderate (respiratory depression - especially in ultra-rapid metabolizers or children, Black Box Warning)", "neurologic": "Moderate (CNS depression, sedation)", "gastrointestinal": "High (constipation - very common)"},
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Respiratory rate and SpO2 - CRITICAL (especially in ultra-rapid CYP2D6 metabolizers or children - Black Box Warning)",
                    "Level of consciousness (GCS) - CRITICAL (especially in ultra-rapid metabolizers)",
                    "Pain score",
                    "CYP2D6 metabolizer status - CRITICAL (ultra-rapid metabolizers → overdose risk, poor metabolizers → no effect)",
                    "Constipation (prophylaxis recommended)",
                    "Age - CRITICAL (contraindicated in children <12 years for cough, <18 years after tonsillectomy/adenoidectomy - Black Box Warning)"
                ],
                "look_alike_sound_alike": ["Codeine", "Morphine", "Hydrocodone"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Respiratory Depression (Especially in Ultra-Rapid Metabolizers and Children)",
                "FDA Black Box Warning - Contraindicated in Children <12 Years (Cough) and <18 Years (Post-Tonsillectomy)",
                "FDA Drug Label - Codeine (respiratory depression and CYP2D6 metabolizer warnings)",
                "WHO Guidelines - Pain Management"
            ]
        },

        "Buprenorphine": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"respiratory": "Moderate (respiratory depression - less than full agonists, but still present, Black Box Warning)", "neurologic": "Moderate (CNS depression, sedation)", "gastrointestinal": "High (constipation - very common)"},
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Respiratory rate and SpO2 - CRITICAL (Black Box Warning, less risk than full agonists but still present)",
                    "Level of consciousness (GCS) - CRITICAL",
                    "Pain score",
                    "Signs of overdose (decreased consciousness, slow breathing) - CRITICAL",
                    "Constipation (prophylaxis recommended)",
                    "Drug interactions (benzodiazepines, alcohol, MAO inhibitors - CONTRAINDICATED/AVOID) - CRITICAL",
                    "Naloxone effectiveness - CRITICAL (less effective than with full agonists due to high affinity)"
                ],
                "look_alike_sound_alike": ["Buprenorphine", "Subutex", "Suboxone", "Morphine"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Respiratory Depression (Less Than Full Agonists But Still Present)",
                "FDA Black Box Warning - Addiction, Abuse, and Misuse",
                "FDA Drug Label - Buprenorphine (respiratory depression warnings)",
                "SAMHSA Guidelines - Opioid Maintenance Therapy",
                "WHO Guidelines - Cancer Pain Management"
            ]
        },

        "Hydrocodone": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": False,
                "organ_toxicity": {"respiratory": "Moderate (respiratory depression - especially with high doses or in combination with acetaminophen)", "neurologic": "Moderate (CNS depression, sedation)", "gastrointestinal": "High (constipation - very common)", "hepatic": "Moderate (hepatotoxicity if combined with acetaminophen in high doses)"},
                "qt_prolongation": False,
                "hepatotoxicity": True,
                "nephrotoxicity": False,
                "requires_monitoring": [
                    "Respiratory rate and SpO2 - CRITICAL (especially with high doses)",
                    "Level of consciousness (GCS) - CRITICAL",
                    "Pain score",
                    "Constipation (prophylaxis recommended)",
                    "Hepatic function (ALT, AST) - CRITICAL (if combined with acetaminophen)",
                    "Total acetaminophen dose - CRITICAL (if combined with acetaminophen, max 4g/day)",
                    "Drug interactions (CYP2D6 inhibitors - decreased effect, benzodiazepines, alcohol - increased respiratory depression) - CRITICAL"
                ],
                "look_alike_sound_alike": ["Hydrocodone", "Vicodin", "Oxycodone", "Codeine"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Respiratory Depression",
                "FDA Black Box Warning - Addiction, Abuse, and Misuse",
                "FDA Drug Label - Hydrocodone (respiratory depression warnings)",
                "WHO Guidelines - Pain Management",
                "CDC Opioid Prescribing Guidelines"
            ]
        },

        "Diclofenac": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": True,
                "organ_toxicity": {"gastrointestinal": "High (GI bleeding, ulceration - higher risk than some NSAIDs)", "cardiovascular": "Moderate (increased risk of MI, stroke, heart failure - Black Box Warning)", "renal": "Moderate (renal impairment, especially with long-term use or in high-risk patients)", "hepatic": "Moderate (elevated transaminases - higher risk than some NSAIDs)"},
                "qt_prolongation": False,
                "hepatotoxicity": True,
                "nephrotoxicity": True,
                "requires_monitoring": [
                    "Signs of GI bleeding (hematemesis, melena, abdominal pain) - CRITICAL (higher risk than some NSAIDs)",
                    "Hepatic function (ALT, AST) - CRITICAL (higher risk of elevated transaminases than some NSAIDs)",
                    "Signs of cardiovascular events (chest pain, dyspnea, signs of heart failure) - CRITICAL (Black Box Warning)",
                    "Renal function (CrCl, BUN, creatinine) - CRITICAL (especially with long-term use or in high-risk patients)",
                    "Blood pressure",
                    "Drug interactions (warfarin, ACE inhibitors, digoxin, methotrexate) - CRITICAL"
                ],
                "look_alike_sound_alike": ["Diclofenac", "Voltaren", "Ibuprofen", "Naproxen"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Cardiovascular Risk (MI, Stroke, Heart Failure)",
                "FDA Black Box Warning - GI Bleeding",
                "FDA Drug Label - Diclofenac (cardiovascular and GI warnings)"
            ]
        },

        "Ketorolac": {
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": True,
                "organ_toxicity": {"gastrointestinal": "High (GI bleeding - very high risk, especially with >5 days use, Black Box Warning)", "renal": "High (acute kidney injury - very high risk, especially with >5 days use, Black Box Warning)", "cardiovascular": "Moderate (increased risk of MI, stroke, heart failure - Black Box Warning)"},
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": True,
                "requires_monitoring": [
                    "Renal function (CrCl, BUN, creatinine) - CRITICAL (daily monitoring if >2 days use, Black Box Warning)",
                    "Signs of GI bleeding (hematemesis, melena, abdominal pain) - CRITICAL (very high risk, Black Box Warning)",
                    "Signs of acute kidney injury - CRITICAL (very high risk, Black Box Warning)",
                    "Duration of use - CRITICAL (max 5 days - Black Box Warning)",
                    "Blood pressure",
                    "Drug interactions (warfarin - CONTRAINDICATED, ACE inhibitors, probenecid) - CRITICAL"
                ],
                "look_alike_sound_alike": ["Ketorolac", "Toradol", "Ibuprofen", "Diclofenac"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Maximum 5 Days Use (Contraindicated for Long-Term Use)",
                "FDA Black Box Warning - GI Bleeding (Very High Risk)",
                "FDA Black Box Warning - Acute Kidney Injury (Very High Risk)",
                "FDA Black Box Warning - Cardiovascular Risk (MI, Stroke, Heart Failure)",
                "ISMP High Alert Medications - Ketorolac",
                "FDA Drug Label - Ketorolac (duration, GI, and renal warnings)"
            ]
        },

        "Meloxicam": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": True,
                "organ_toxicity": {"gastrointestinal": "Moderate (GI bleeding - less than non-selective NSAIDs due to COX-2 selectivity)", "cardiovascular": "Moderate (increased risk of MI, stroke, heart failure - Black Box Warning)", "renal": "Moderate (renal impairment, especially with long-term use or in high-risk patients)"},
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": True,
                "requires_monitoring": [
                    "Signs of GI bleeding (hematemesis, melena, abdominal pain) - CRITICAL (less risk than non-selective NSAIDs but still present)",
                    "Signs of cardiovascular events (chest pain, dyspnea, signs of heart failure) - CRITICAL (Black Box Warning)",
                    "Renal function (CrCl, BUN, creatinine) - CRITICAL (especially with long-term use or in high-risk patients)",
                    "Blood pressure",
                    "Drug interactions (warfarin, ACE inhibitors, methotrexate) - CRITICAL"
                ],
                "look_alike_sound_alike": ["Meloxicam", "Mobic", "Celecoxib", "Ibuprofen"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Cardiovascular Risk (MI, Stroke, Heart Failure)",
                "FDA Drug Label - Meloxicam (cardiovascular warnings)"
            ]
        },

        "Celecoxib": {
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "icu_critical_care_only": False,
                "bleeding_risk": True,
                "organ_toxicity": {"cardiovascular": "High (increased risk of MI, stroke, heart failure - Black Box Warning)", "gastrointestinal": "Low (GI bleeding - less than non-selective NSAIDs due to COX-2 selectivity)", "renal": "Moderate (renal impairment, especially with long-term use or in high-risk patients)"},
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": True,
                "requires_monitoring": [
                    "Signs of cardiovascular events (chest pain, dyspnea, signs of heart failure) - CRITICAL (Black Box Warning)",
                    "Signs of GI bleeding (hematemesis, melena, abdominal pain) - CRITICAL (less risk than non-selective NSAIDs but still present)",
                    "Renal function (CrCl, BUN, creatinine) - CRITICAL (especially with long-term use or in high-risk patients)",
                    "Blood pressure",
                    "Drug interactions (warfarin, ACE inhibitors, lithium, methotrexate) - CRITICAL",
                    "Sulfonamide allergy - CRITICAL (contraindicated)"
                ],
                "look_alike_sound_alike": ["Celecoxib", "Celebrex", "Meloxicam", "Etoricoxib"]
            },
            "guideline_tags": [
                "FDA Black Box Warning - Cardiovascular Risk (MI, Stroke, Heart Failure)",
                "FDA Black Box Warning - Sulfonamide Allergy (Contraindicated)",
                "FDA Drug Label - Celecoxib (cardiovascular and sulfonamide allergy warnings)"
            ]
        },
}

__all__ = ['ANALGESICS_ENHANCED_FIELDS']

