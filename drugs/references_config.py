"""
References Configuration for Drug Database
Contains general references for drug information sources
"""

from typing import List, Dict, Any
from components.references import (
    GRADE_HIGH, GRADE_MODERATE, GRADE_LOW,
    EVIDENCE_LEVEL_I, EVIDENCE_LEVEL_IIA, EVIDENCE_LEVEL_IIB,
    STRENGTH_STRONG, STRENGTH_MODERATE
)

# General references for drug database
DRUG_DATABASE_REFERENCES: List[Dict[str, Any]] = [
    {
        "type": "database",
        "title": "UpToDate - Clinical Decision Support",
        "authors": "Wolters Kluwer",
        "journal": "UpToDate",
        "year": 2024,
        "url": "https://www.uptodate.com",
        "evidence_level": EVIDENCE_LEVEL_I,
        "strength": STRENGTH_STRONG,
        "description": "Comprehensive drug information, dosing, interactions, and clinical decision support"
    },
    {
        "type": "database",
        "title": "Micromedex - Drug Information",
        "authors": "IBM Watson Health",
        "journal": "Micromedex",
        "year": 2024,
        "url": "https://www.micromedexsolutions.com",
        "evidence_level": EVIDENCE_LEVEL_I,
        "strength": STRENGTH_STRONG,
        "description": "Evidence-based drug information, dosing, interactions, and toxicology"
    },
    {
        "type": "database",
        "title": "Lexicomp - Drug Information",
        "authors": "Wolters Kluwer",
        "journal": "Lexicomp",
        "year": 2024,
        "url": "https://www.lexicomp.com",
        "evidence_level": EVIDENCE_LEVEL_I,
        "strength": STRENGTH_STRONG,
        "description": "Comprehensive drug reference with dosing, interactions, and clinical information"
    },
    {
        "type": "guideline",
        "title": "FDA - Drugs@FDA",
        "authors": "U.S. Food and Drug Administration",
        "journal": "FDA",
        "year": 2024,
        "url": "https://www.accessdata.fda.gov/scripts/cder/daf/",
        "evidence_level": EVIDENCE_LEVEL_I,
        "strength": STRENGTH_STRONG,
        "description": "Official FDA drug information, labeling, and approval data"
    },
    {
        "type": "guideline",
        "title": "WHO Model List of Essential Medicines",
        "authors": "World Health Organization",
        "journal": "WHO",
        "year": 2023,
        "url": "https://www.who.int/publications/i/item/WHO-MHP-HPS-EML-2023.02",
        "evidence_level": EVIDENCE_LEVEL_I,
        "strength": STRENGTH_STRONG,
        "description": "WHO Essential Medicines List with evidence-based recommendations"
    },
    {
        "type": "database",
        "title": "Drugs.com - Drug Information",
        "authors": "Drugs.com",
        "journal": "Drugs.com",
        "year": 2024,
        "url": "https://www.drugs.com",
        "evidence_level": EVIDENCE_LEVEL_IIA,
        "strength": STRENGTH_MODERATE,
        "description": "Consumer and professional drug information database"
    },
    {
        "type": "guideline",
        "title": "AHFS Drug Information",
        "authors": "American Society of Health-System Pharmacists",
        "journal": "AHFS",
        "year": 2024,
        "url": "https://www.ahfsdruginformation.com",
        "evidence_level": EVIDENCE_LEVEL_I,
        "strength": STRENGTH_STRONG,
        "description": "Comprehensive drug information reference for healthcare professionals"
    },
    {
        "type": "guideline",
        "title": "Medscape Drug Reference",
        "authors": "WebMD",
        "journal": "Medscape",
        "year": 2024,
        "url": "https://reference.medscape.com/drugs",
        "evidence_level": EVIDENCE_LEVEL_IIA,
        "strength": STRENGTH_MODERATE,
        "description": "Drug information, dosing, interactions, and clinical reference"
    }
]

# Drug class-specific references
DRUG_CLASS_REFERENCES: Dict[str, List[Dict[str, Any]]] = {
    "Antibiotics": [
        {
            "type": "guideline",
            "title": "IDSA Treatment Guidelines",
            "authors": "Infectious Diseases Society of America",
            "journal": "Clinical Infectious Diseases",
            "year": 2024,
            "url": "https://www.idsociety.org/practice-guideline/",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "guideline",
            "title": "Sanford Guide to Antimicrobial Therapy",
            "authors": "Sanford JP",
            "journal": "Antimicrobial Therapy",
            "year": 2024,
            "url": "https://www.sanfordguide.com",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],
    "Anticoagulants": [
        {
            "type": "guideline",
            "title": "2021 ACC/AHA/ASE/CHEST/SAEM/SCCT/SCMR Guideline for the Evaluation and Diagnosis of Chest Pain",
            "authors": "Gulati M, et al.",
            "journal": "Journal of the American College of Cardiology",
            "year": 2021,
            "volume": "78",
            "issue": "22",
            "pages": "e187-e285",
            "doi": "10.1016/j.jacc.2021.07.053",
            "pmid": "34756653",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],
    "Antidiabetics": [
        {
            "type": "guideline",
            "title": "Standards of Medical Care in Diabetes—2024",
            "authors": "American Diabetes Association",
            "journal": "Diabetes Care",
            "year": 2024,
            "volume": "47",
            "issue": "Supplement_1",
            "pages": "S1-S291",
            "doi": "10.2337/dc24-Sint",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],
    "Cardiovascular": [
        {
            "type": "guideline",
            "title": "2020 ESC/ESH Guidelines for the management of arterial hypertension",
            "authors": "Williams B, et al.",
            "journal": "European Heart Journal",
            "year": 2018,
            "volume": "39",
            "issue": "33",
            "pages": "3021-3104",
            "doi": "10.1093/eurheartj/ehy339",
            "pmid": "30165516",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ]
}


def get_drug_references(drug_class: str = None) -> List[Dict[str, Any]]:
    """
    Get references for drug database
    
    Args:
        drug_class: Optional drug class to get class-specific references
    
    Returns:
        List of reference dictionaries
    """
    references = DRUG_DATABASE_REFERENCES.copy()
    
    if drug_class and drug_class in DRUG_CLASS_REFERENCES:
        references.extend(DRUG_CLASS_REFERENCES[drug_class])
    
    return references


def has_drug_references(drug_class: str = None) -> bool:
    """
    Check if drug references exist
    
    Args:
        drug_class: Optional drug class to check
    
    Returns:
        True if references exist, False otherwise
    """
    if drug_class and drug_class in DRUG_CLASS_REFERENCES:
        return True
    return len(DRUG_DATABASE_REFERENCES) > 0

