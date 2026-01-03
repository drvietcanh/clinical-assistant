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
}

__all__ = ['ANALGESICS_ENHANCED_FIELDS']

