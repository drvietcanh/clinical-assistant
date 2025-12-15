"""
Pregnancy & Lactation Safety Database
FDA Pregnancy Categories and Briggs Lactation Risk Categories
"""

from typing import Dict, Optional, List
from enum import Enum


class FDAPregnancyCategory(Enum):
    """FDA Pregnancy Categories (old system, being phased out)"""
    A = "A"  # Controlled studies show no risk
    B = "B"  # No evidence of risk in humans
    C = "C"  # Risk cannot be ruled out
    D = "D"  # Positive evidence of risk
    X = "X"  # Contraindicated in pregnancy


class BriggsLactationCategory(Enum):
    """Briggs Lactation Risk Categories"""
    L1 = "L1"  # Safest
    L2 = "L2"  # Safer
    L3 = "L3"  # Moderately safe
    L4 = "L4"  # Possibly hazardous
    L5 = "L5"  # Contraindicated


class PregnancyRiskLevel(Enum):
    """Simplified pregnancy risk levels"""
    SAFE = "Safe"
    PROBABLY_SAFE = "Probably Safe"
    USE_CAUTION = "Use Caution"
    AVOID = "Avoid"
    CONTRAINDICATED = "Contraindicated"


class LactationRiskLevel(Enum):
    """Simplified lactation risk levels"""
    SAFE = "Safe"
    PROBABLY_SAFE = "Probably Safe"
    USE_CAUTION = "Use Caution"
    AVOID = "Avoid"
    CONTRAINDICATED = "Contraindicated"


# Pregnancy Safety Database
PREGNANCY_SAFETY: Dict[str, Dict] = {
    # Analgesics
    "Paracetamol": {
        "fda_category": FDAPregnancyCategory.B,
        "risk_level": PregnancyRiskLevel.SAFE,
        "trimester_specific": {
            "first": "Safe - No known risk",
            "second": "Safe - No known risk",
            "third": "Safe - No known risk"
        },
        "notes": "Drug of choice for pain/fever in pregnancy. Use at lowest effective dose.",
        "references": ["Briggs GG, et al. Drugs in Pregnancy and Lactation. 12th ed."]
    },
    "Ibuprofen": {
        "fda_category": FDAPregnancyCategory.C,
        "risk_level": PregnancyRiskLevel.USE_CAUTION,
        "trimester_specific": {
            "first": "Avoid if possible - Risk of miscarriage",
            "second": "Use with caution - Monitor",
            "third": "CONTRAINDICATED - Risk of premature closure of ductus arteriosus"
        },
        "notes": "Avoid in 3rd trimester. Use lowest dose, shortest duration if needed in 1st/2nd trimester.",
        "references": ["ACOG Practice Bulletin No. 189"]
    },
    "Aspirin": {
        "fda_category": FDAPregnancyCategory.C,
        "risk_level": PregnancyRiskLevel.USE_CAUTION,
        "trimester_specific": {
            "first": "Avoid high doses - Risk of miscarriage",
            "second": "Low dose (81mg) may be used for preeclampsia prevention",
            "third": "Low dose may be used. High dose contraindicated."
        },
        "notes": "Low dose aspirin (81mg) may be recommended for preeclampsia prevention. High dose (>150mg) contraindicated.",
        "references": ["ACOG Practice Bulletin No. 202"]
    },
    
    # Antibiotics
    "Penicillin": {
        "fda_category": FDAPregnancyCategory.B,
        "risk_level": PregnancyRiskLevel.SAFE,
        "trimester_specific": {
            "first": "Safe - No known risk",
            "second": "Safe - No known risk",
            "third": "Safe - No known risk"
        },
        "notes": "Drug of choice for many infections in pregnancy.",
        "references": ["Briggs GG, et al. Drugs in Pregnancy and Lactation."]
    },
    "Amoxicillin": {
        "fda_category": FDAPregnancyCategory.B,
        "risk_level": PregnancyRiskLevel.SAFE,
        "trimester_specific": {
            "first": "Safe - No known risk",
            "second": "Safe - No known risk",
            "third": "Safe - No known risk"
        },
        "notes": "Widely used in pregnancy. No known teratogenic effects.",
        "references": ["Briggs GG, et al. Drugs in Pregnancy and Lactation."]
    },
    "Cephalexin": {
        "fda_category": FDAPregnancyCategory.B,
        "risk_level": PregnancyRiskLevel.SAFE,
        "trimester_specific": {
            "first": "Safe - No known risk",
            "second": "Safe - No known risk",
            "third": "Safe - No known risk"
        },
        "notes": "Safe in all trimesters.",
        "references": ["Briggs GG, et al. Drugs in Pregnancy and Lactation."]
    },
    "Azithromycin": {
        "fda_category": FDAPregnancyCategory.B,
        "risk_level": PregnancyRiskLevel.PROBABLY_SAFE,
        "trimester_specific": {
            "first": "Probably safe - Limited data",
            "second": "Probably safe - Limited data",
            "third": "Probably safe - Limited data"
        },
        "notes": "Limited data but appears safe. Used for chlamydia in pregnancy.",
        "references": ["CDC STI Treatment Guidelines 2021"]
    },
    "Ciprofloxacin": {
        "fda_category": FDAPregnancyCategory.C,
        "risk_level": PregnancyRiskLevel.AVOID,
        "trimester_specific": {
            "first": "AVOID - Risk of arthropathy",
            "second": "AVOID - Risk of arthropathy",
            "third": "AVOID - Risk of arthropathy"
        },
        "notes": "Contraindicated due to risk of arthropathy in fetus. Use alternative if possible.",
        "references": ["Briggs GG, et al. Drugs in Pregnancy and Lactation."]
    },
    "Doxycycline": {
        "fda_category": FDAPregnancyCategory.D,
        "risk_level": PregnancyRiskLevel.CONTRAINDICATED,
        "trimester_specific": {
            "first": "CONTRAINDICATED - Risk of skeletal defects",
            "second": "CONTRAINDICATED - Risk of tooth discoloration",
            "third": "CONTRAINDICATED - Risk of tooth discoloration"
        },
        "notes": "Contraindicated in pregnancy. Causes tooth discoloration and skeletal defects.",
        "references": ["Briggs GG, et al. Drugs in Pregnancy and Lactation."]
    },
    
    # Cardiovascular
    "Metoprolol": {
        "fda_category": FDAPregnancyCategory.C,
        "risk_level": PregnancyRiskLevel.USE_CAUTION,
        "trimester_specific": {
            "first": "Use with caution - Monitor",
            "second": "Use with caution - Monitor fetal growth",
            "third": "Use with caution - Monitor for bradycardia, hypoglycemia"
        },
        "notes": "May cause fetal bradycardia, hypoglycemia, IUGR. Monitor closely.",
        "references": ["ACOG Practice Bulletin No. 203"]
    },
    "Atenolol": {
        "fda_category": FDAPregnancyCategory.D,
        "risk_level": PregnancyRiskLevel.AVOID,
        "trimester_specific": {
            "first": "AVOID - Risk of IUGR",
            "second": "AVOID - Risk of IUGR",
            "third": "AVOID - Risk of IUGR"
        },
        "notes": "Avoid in pregnancy. Associated with IUGR. Use alternative beta-blocker.",
        "references": ["Briggs GG, et al. Drugs in Pregnancy and Lactation."]
    },
    "Lisinopril": {
        "fda_category": FDAPregnancyCategory.D,
        "risk_level": PregnancyRiskLevel.CONTRAINDICATED,
        "trimester_specific": {
            "first": "CONTRAINDICATED - Risk of fetal malformations",
            "second": "CONTRAINDICATED - Risk of oligohydramnios, renal failure",
            "third": "CONTRAINDICATED - Risk of oligohydramnios, renal failure"
        },
        "notes": "ACE inhibitors contraindicated in 2nd and 3rd trimester. Discontinue immediately if pregnancy detected.",
        "references": ["ACOG Practice Bulletin No. 203"]
    },
    "Warfarin": {
        "fda_category": FDAPregnancyCategory.D,
        "risk_level": PregnancyRiskLevel.USE_CAUTION,
        "trimester_specific": {
            "first": "AVOID - Risk of warfarin embryopathy",
            "second": "Use with caution - Risk of CNS malformations",
            "third": "Use with caution - Risk of bleeding"
        },
        "notes": "Avoid in 1st trimester. May use in 2nd/3rd trimester with close monitoring. Consider LMWH as alternative.",
        "references": ["ACOG Practice Bulletin No. 196"]
    },
    
    # Anticoagulants
    "Enoxaparin": {
        "fda_category": FDAPregnancyCategory.B,
        "risk_level": PregnancyRiskLevel.SAFE,
        "trimester_specific": {
            "first": "Safe - No known risk",
            "second": "Safe - No known risk",
            "third": "Safe - No known risk"
        },
        "notes": "LMWH does not cross placenta. Safe in all trimesters. Preferred over warfarin.",
        "references": ["ACOG Practice Bulletin No. 196"]
    },
    "Heparin": {
        "fda_category": FDAPregnancyCategory.C,
        "risk_level": PregnancyRiskLevel.SAFE,
        "trimester_specific": {
            "first": "Safe - Does not cross placenta",
            "second": "Safe - Does not cross placenta",
            "third": "Safe - Does not cross placenta"
        },
        "notes": "Does not cross placenta. Safe but requires monitoring. LMWH preferred.",
        "references": ["ACOG Practice Bulletin No. 196"]
    },
    
    # Antidiabetics
    "Metformin": {
        "fda_category": FDAPregnancyCategory.B,
        "risk_level": PregnancyRiskLevel.SAFE,
        "trimester_specific": {
            "first": "Safe - Used for PCOS, GDM",
            "second": "Safe - Used for GDM",
            "third": "Safe - Used for GDM"
        },
        "notes": "Safe in pregnancy. Used for gestational diabetes and PCOS.",
        "references": ["ADA Standards of Medical Care in Diabetes 2023"]
    },
    "Insulin": {
        "fda_category": FDAPregnancyCategory.B,
        "risk_level": PregnancyRiskLevel.SAFE,
        "trimester_specific": {
            "first": "Safe - Drug of choice",
            "second": "Safe - Drug of choice",
            "third": "Safe - Drug of choice"
        },
        "notes": "Drug of choice for diabetes in pregnancy. Does not cross placenta.",
        "references": ["ADA Standards of Medical Care in Diabetes 2023"]
    },
    
    # Antiemetics
    "Ondansetron": {
        "fda_category": FDAPregnancyCategory.B,
        "risk_level": PregnancyRiskLevel.PROBABLY_SAFE,
        "trimester_specific": {
            "first": "Probably safe - Some concern about cardiac defects",
            "second": "Safe - No known risk",
            "third": "Safe - No known risk"
        },
        "notes": "Widely used for hyperemesis. Some studies suggest small increased risk of cardiac defects in 1st trimester.",
        "references": ["ACOG Practice Bulletin No. 189"]
    },
    "Metoclopramide": {
        "fda_category": FDAPregnancyCategory.B,
        "risk_level": PregnancyRiskLevel.SAFE,
        "trimester_specific": {
            "first": "Safe - No known risk",
            "second": "Safe - No known risk",
            "third": "Safe - No known risk"
        },
        "notes": "Safe in all trimesters. Used for hyperemesis.",
        "references": ["Briggs GG, et al. Drugs in Pregnancy and Lactation."]
    },
    
    # Antihypertensives
    "Methyldopa": {
        "fda_category": FDAPregnancyCategory.B,
        "risk_level": PregnancyRiskLevel.SAFE,
        "trimester_specific": {
            "first": "Safe - No known risk",
            "second": "Safe - Drug of choice for hypertension",
            "third": "Safe - Drug of choice for hypertension"
        },
        "notes": "Drug of choice for hypertension in pregnancy. Safe in all trimesters.",
        "references": ["ACOG Practice Bulletin No. 203"]
    },
    "Labetalol": {
        "fda_category": FDAPregnancyCategory.C,
        "risk_level": PregnancyRiskLevel.SAFE,
        "trimester_specific": {
            "first": "Safe - No known risk",
            "second": "Safe - Commonly used",
            "third": "Safe - Commonly used"
        },
        "notes": "Commonly used for hypertension in pregnancy. Safe in all trimesters.",
        "references": ["ACOG Practice Bulletin No. 203"]
    },
    
    # Antidepressants
    "Sertraline": {
        "fda_category": FDAPregnancyCategory.C,
        "risk_level": PregnancyRiskLevel.USE_CAUTION,
        "trimester_specific": {
            "first": "Use with caution - Some risk of cardiac defects",
            "second": "Use with caution - Monitor",
            "third": "Use with caution - Risk of withdrawal in neonate"
        },
        "notes": "SSRIs may cause cardiac defects, persistent pulmonary hypertension. Risk of withdrawal in neonate. Benefits may outweigh risks.",
        "references": ["ACOG Practice Bulletin No. 211"]
    },
    "Fluoxetine": {
        "fda_category": FDAPregnancyCategory.C,
        "risk_level": PregnancyRiskLevel.USE_CAUTION,
        "trimester_specific": {
            "first": "Use with caution - Some risk of cardiac defects",
            "second": "Use with caution - Monitor",
            "third": "Use with caution - Risk of withdrawal in neonate"
        },
        "notes": "SSRIs may cause cardiac defects, persistent pulmonary hypertension. Risk of withdrawal in neonate.",
        "references": ["ACOG Practice Bulletin No. 211"]
    },
    
    # Anticonvulsants
    "Phenytoin": {
        "fda_category": FDAPregnancyCategory.D,
        "risk_level": PregnancyRiskLevel.USE_CAUTION,
        "trimester_specific": {
            "first": "Use with caution - Risk of teratogenicity",
            "second": "Use with caution - Monitor",
            "third": "Use with caution - Risk of bleeding in neonate"
        },
        "notes": "Risk of fetal hydantoin syndrome, neural tube defects. Use lowest effective dose. Folic acid supplementation essential.",
        "references": ["ACOG Practice Bulletin No. 200"]
    },
    "Valproic Acid": {
        "fda_category": FDAPregnancyCategory.D,
        "risk_level": PregnancyRiskLevel.AVOID,
        "trimester_specific": {
            "first": "AVOID - High risk of neural tube defects",
            "second": "AVOID - Risk of malformations",
            "third": "AVOID - Risk of cognitive deficits"
        },
        "notes": "High risk of neural tube defects (1-2%), cognitive deficits. Avoid if possible. Use alternative anticonvulsant.",
        "references": ["ACOG Practice Bulletin No. 200"]
    },
    
    # Thyroid
    "Levothyroxine": {
        "fda_category": FDAPregnancyCategory.A,
        "risk_level": PregnancyRiskLevel.SAFE,
        "trimester_specific": {
            "first": "Safe - Essential for fetal development",
            "second": "Safe - Essential for fetal development",
            "third": "Safe - Essential for fetal development"
        },
        "notes": "Safe and essential in pregnancy. Dose may need to be increased by 25-50%.",
        "references": ["ATA Guidelines for Thyroid Disease in Pregnancy"]
    },
    
    # Gastrointestinal
    "Omeprazole": {
        "fda_category": FDAPregnancyCategory.C,
        "risk_level": PregnancyRiskLevel.PROBABLY_SAFE,
        "trimester_specific": {
            "first": "Probably safe - Limited data",
            "second": "Probably safe - Limited data",
            "third": "Probably safe - Limited data"
        },
        "notes": "Limited data but appears safe. Used for GERD in pregnancy.",
        "references": ["Briggs GG, et al. Drugs in Pregnancy and Lactation."]
    },
    "Ranitidine": {
        "fda_category": FDAPregnancyCategory.B,
        "risk_level": PregnancyRiskLevel.SAFE,
        "trimester_specific": {
            "first": "Safe - No known risk",
            "second": "Safe - No known risk",
            "third": "Safe - No known risk"
        },
        "notes": "Safe in all trimesters. Used for GERD in pregnancy.",
        "references": ["Briggs GG, et al. Drugs in Pregnancy and Lactation."]
    },
}


# Lactation Safety Database
LACTATION_SAFETY: Dict[str, Dict] = {
    # Analgesics
    "Paracetamol": {
        "briggs_category": BriggsLactationCategory.L1,
        "risk_level": LactationRiskLevel.SAFE,
        "notes": "Compatible with breastfeeding. Minimal excretion in milk.",
        "references": ["Briggs GG, et al. Drugs in Pregnancy and Lactation."]
    },
    "Ibuprofen": {
        "briggs_category": BriggsLactationCategory.L2,
        "risk_level": LactationRiskLevel.SAFE,
        "notes": "Compatible with breastfeeding. Minimal excretion in milk.",
        "references": ["Briggs GG, et al. Drugs in Pregnancy and Lactation."]
    },
    "Aspirin": {
        "briggs_category": BriggsLactationCategory.L3,
        "risk_level": LactationRiskLevel.USE_CAUTION,
        "notes": "Low dose (81mg) probably safe. High dose may cause Reye syndrome in infant. Avoid high doses.",
        "references": ["Briggs GG, et al. Drugs in Pregnancy and Lactation."]
    },
    
    # Antibiotics
    "Penicillin": {
        "briggs_category": BriggsLactationCategory.L2,
        "risk_level": LactationRiskLevel.SAFE,
        "notes": "Compatible with breastfeeding. Minimal excretion in milk.",
        "references": ["Briggs GG, et al. Drugs in Pregnancy and Lactation."]
    },
    "Amoxicillin": {
        "briggs_category": BriggsLactationCategory.L2,
        "risk_level": LactationRiskLevel.SAFE,
        "notes": "Compatible with breastfeeding.",
        "references": ["Briggs GG, et al. Drugs in Pregnancy and Lactation."]
    },
    "Ciprofloxacin": {
        "briggs_category": BriggsLactationCategory.L3,
        "risk_level": LactationRiskLevel.USE_CAUTION,
        "notes": "Excreted in milk. May cause arthropathy in infant. Use with caution.",
        "references": ["Briggs GG, et al. Drugs in Pregnancy and Lactation."]
    },
    "Doxycycline": {
        "briggs_category": BriggsLactationCategory.L3,
        "risk_level": LactationRiskLevel.USE_CAUTION,
        "notes": "Excreted in milk. May cause tooth discoloration. Short courses probably safe.",
        "references": ["Briggs GG, et al. Drugs in Pregnancy and Lactation."]
    },
    
    # Cardiovascular
    "Metoprolol": {
        "briggs_category": BriggsLactationCategory.L2,
        "risk_level": LactationRiskLevel.SAFE,
        "notes": "Compatible with breastfeeding. Monitor infant for bradycardia, hypoglycemia.",
        "references": ["Briggs GG, et al. Drugs in Pregnancy and Lactation."]
    },
    "Lisinopril": {
        "briggs_category": BriggsLactationCategory.L3,
        "risk_level": LactationRiskLevel.USE_CAUTION,
        "notes": "Excreted in milk. Monitor infant for hypotension. Probably safe but use with caution.",
        "references": ["Briggs GG, et al. Drugs in Pregnancy and Lactation."]
    },
    "Warfarin": {
        "briggs_category": BriggsLactationCategory.L2,
        "risk_level": LactationRiskLevel.SAFE,
        "notes": "Compatible with breastfeeding. Does not cause anticoagulation in infant.",
        "references": ["Briggs GG, et al. Drugs in Pregnancy and Lactation."]
    },
    
    # Anticoagulants
    "Enoxaparin": {
        "briggs_category": BriggsLactationCategory.L2,
        "risk_level": LactationRiskLevel.SAFE,
        "notes": "Compatible with breastfeeding. Large molecule, minimal excretion in milk.",
        "references": ["Briggs GG, et al. Drugs in Pregnancy and Lactation."]
    },
    "Heparin": {
        "briggs_category": BriggsLactationCategory.L1,
        "risk_level": LactationRiskLevel.SAFE,
        "notes": "Compatible with breastfeeding. Does not cross into milk.",
        "references": ["Briggs GG, et al. Drugs in Pregnancy and Lactation."]
    },
    
    # Antidiabetics
    "Metformin": {
        "briggs_category": BriggsLactationCategory.L2,
        "risk_level": LactationRiskLevel.SAFE,
        "notes": "Compatible with breastfeeding. Minimal excretion in milk.",
        "references": ["Briggs GG, et al. Drugs in Pregnancy and Lactation."]
    },
    "Insulin": {
        "briggs_category": BriggsLactationCategory.L1,
        "risk_level": LactationRiskLevel.SAFE,
        "notes": "Compatible with breastfeeding. Does not cross into milk.",
        "references": ["Briggs GG, et al. Drugs in Pregnancy and Lactation."]
    },
    
    # Antiemetics
    "Ondansetron": {
        "briggs_category": BriggsLactationCategory.L2,
        "risk_level": LactationRiskLevel.SAFE,
        "notes": "Compatible with breastfeeding. Minimal excretion in milk.",
        "references": ["Briggs GG, et al. Drugs in Pregnancy and Lactation."]
    },
    "Metoclopramide": {
        "briggs_category": BriggsLactationCategory.L2,
        "risk_level": LactationRiskLevel.SAFE,
        "notes": "Compatible with breastfeeding. May increase milk production.",
        "references": ["Briggs GG, et al. Drugs in Pregnancy and Lactation."]
    },
    
    # Antihypertensives
    "Methyldopa": {
        "briggs_category": BriggsLactationCategory.L2,
        "risk_level": LactationRiskLevel.SAFE,
        "notes": "Compatible with breastfeeding.",
        "references": ["Briggs GG, et al. Drugs in Pregnancy and Lactation."]
    },
    "Labetalol": {
        "briggs_category": BriggsLactationCategory.L2,
        "risk_level": LactationRiskLevel.SAFE,
        "notes": "Compatible with breastfeeding. Monitor infant for bradycardia, hypotension.",
        "references": ["Briggs GG, et al. Drugs in Pregnancy and Lactation."]
    },
    
    # Antidepressants
    "Sertraline": {
        "briggs_category": BriggsLactationCategory.L2,
        "risk_level": LactationRiskLevel.SAFE,
        "notes": "Compatible with breastfeeding. Preferred SSRI during lactation.",
        "references": ["Briggs GG, et al. Drugs in Pregnancy and Lactation."]
    },
    "Fluoxetine": {
        "briggs_category": BriggsLactationCategory.L2,
        "risk_level": LactationRiskLevel.SAFE,
        "notes": "Compatible with breastfeeding. Monitor infant for irritability, poor feeding.",
        "references": ["Briggs GG, et al. Drugs in Pregnancy and Lactation."]
    },
    
    # Anticonvulsants
    "Phenytoin": {
        "briggs_category": BriggsLactationCategory.L2,
        "risk_level": LactationRiskLevel.SAFE,
        "notes": "Compatible with breastfeeding. Monitor infant for sedation, poor feeding.",
        "references": ["Briggs GG, et al. Drugs in Pregnancy and Lactation."]
    },
    "Valproic Acid": {
        "briggs_category": BriggsLactationCategory.L2,
        "risk_level": LactationRiskLevel.SAFE,
        "notes": "Compatible with breastfeeding. Monitor infant for sedation, poor feeding.",
        "references": ["Briggs GG, et al. Drugs in Pregnancy and Lactation."]
    },
    
    # Thyroid
    "Levothyroxine": {
        "briggs_category": BriggsLactationCategory.L1,
        "risk_level": LactationRiskLevel.SAFE,
        "notes": "Compatible with breastfeeding. Minimal excretion in milk.",
        "references": ["Briggs GG, et al. Drugs in Pregnancy and Lactation."]
    },
    
    # Gastrointestinal
    "Omeprazole": {
        "briggs_category": BriggsLactationCategory.L2,
        "risk_level": LactationRiskLevel.SAFE,
        "notes": "Compatible with breastfeeding. Minimal excretion in milk.",
        "references": ["Briggs GG, et al. Drugs in Pregnancy and Lactation."]
    },
    "Ranitidine": {
        "briggs_category": BriggsLactationCategory.L2,
        "risk_level": LactationRiskLevel.SAFE,
        "notes": "Compatible with breastfeeding.",
        "references": ["Briggs GG, et al. Drugs in Pregnancy and Lactation."]
    },
}


def get_pregnancy_safety(drug_name: str) -> Optional[Dict]:
    """
    Get pregnancy safety information for a drug
    
    Args:
        drug_name: Name of the drug
    
    Returns:
        Dictionary with pregnancy safety information or None
    """
    return PREGNANCY_SAFETY.get(drug_name)


def get_lactation_safety(drug_name: str) -> Optional[Dict]:
    """
    Get lactation safety information for a drug
    
    Args:
        drug_name: Name of the drug
    
    Returns:
        Dictionary with lactation safety information or None
    """
    return LACTATION_SAFETY.get(drug_name)


def get_safety_summary(drug_name: str) -> Dict:
    """
    Get combined pregnancy and lactation safety summary
    
    Args:
        drug_name: Name of the drug
    
    Returns:
        Dictionary with both pregnancy and lactation safety
    """
    pregnancy = get_pregnancy_safety(drug_name)
    lactation = get_lactation_safety(drug_name)
    
    return {
        "drug_name": drug_name,
        "pregnancy": pregnancy,
        "lactation": lactation,
        "has_data": pregnancy is not None or lactation is not None
    }

