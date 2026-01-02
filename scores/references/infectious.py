"""
Calculator References - Infectious
"""
from typing import List, Dict, Any
from components.references import (
    GRADE_HIGH, GRADE_MODERATE, GRADE_LOW,
    EVIDENCE_LEVEL_I, EVIDENCE_LEVEL_IIA, EVIDENCE_LEVEL_IIB,
    STRENGTH_STRONG, STRENGTH_MODERATE
)


INFECTIOUS_REFERENCES: Dict[str, List[Dict[str, Any]]] = {
        "Centor": [
            {
                "type": "primary",
                "title": "The diagnosis of strep throat in adults in the emergency room",
                "authors": "Centor RM, Witherspoon JM, Dalton HP, Brody CE, Link K",
                "journal": "Medical Decision Making",
                "year": 1981,
                "volume": "1",
                "issue": "3",
                "pages": "239-246",
                "doi": "10.1177/0272989X8100100304",
                "pmid": "6763125",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            }
        ],

        "FeverPAIN": [
            {
                "type": "primary",
                "title": "Clinical score for rapid detection of group A streptococcal pharyngitis",
                "authors": "Little P, Hobbs FD, Moore M, et al.",
                "journal": "BMJ",
                "year": 2013,
                "volume": "347",
                "pages": "f5060",
                "doi": "10.1136/bmj.f5060",
                "pmid": "23970166",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            }
        ],

        "MASCC": [
            {
                "type": "primary",
                "title": "Multinational Association for Supportive Care in Cancer risk index: a multinational scoring system for identifying low-risk febrile neutropenic cancer patients",
                "authors": "Klastersky J, Paesmans M, Rubenstein EB, et al.",
                "journal": "Journal of Clinical Oncology",
                "year": 2000,
                "volume": "18",
                "issue": "16",
                "pages": "3038-3051",
                "doi": "10.1200/JCO.2000.18.16.3038",
                "pmid": "10944139",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            }
        ],

        "Pitt Bacteremia": [
            {
                "type": "primary",
                "title": "The Pittsburgh bacteremia score: a new scoring system for predicting mortality in patients with bacteremia",
                "authors": "Paterson DL, Ko WC, Von Gottberg A, et al.",
                "journal": "Clinical Infectious Diseases",
                "year": 2004,
                "volume": "38",
                "issue": "3",
                "pages": "357-364",
                "doi": "10.1086/380983",
                "pmid": "14727204",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            }
        ],

}
