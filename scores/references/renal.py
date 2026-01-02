"""
Calculator References - Renal
"""
from typing import List, Dict, Any
from components.references import (
    GRADE_HIGH, GRADE_MODERATE, GRADE_LOW,
    EVIDENCE_LEVEL_I, EVIDENCE_LEVEL_IIA, EVIDENCE_LEVEL_IIB,
    STRENGTH_STRONG, STRENGTH_MODERATE
)


RENAL_REFERENCES: Dict[str, List[Dict[str, Any]]] = {
        "eGFR": [
            {
                "type": "primary",
                "title": "A new equation to estimate glomerular filtration rate",
                "authors": "Levey AS, Stevens LA, Schmid CH, et al.",
                "journal": "Annals of Internal Medicine",
                "year": 2009,
                "volume": "150",
                "issue": "9",
                "pages": "604-612",
                "doi": "10.7326/0003-4819-150-9-200904070-00006",
                "pmid": "19414839",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "guideline",
                "title": "KDIGO 2012 Clinical Practice Guideline for the Evaluation and Management of Chronic Kidney Disease",
                "authors": "KDIGO 2012 Clinical Practice Guideline",
                "journal": "Kidney International Supplements",
                "year": 2013,
                "volume": "3",
                "issue": "1",
                "pages": "1-150",
                "doi": "10.1038/kisup.2012.73",
                "pmid": "25018998",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            }
        ],

        "KDIGO": [
            {
                "type": "guideline",
                "title": "KDIGO Clinical Practice Guideline for Acute Kidney Injury",
                "authors": "KDIGO Work Group",
                "journal": "Kidney International Supplements",
                "year": 2012,
                "volume": "2",
                "issue": "1",
                "pages": "1-138",
                "doi": "10.1038/kisup.2012.1",
                "pmid": "25018998",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "primary",
                "title": "Acute Kidney Injury Network: report of an initiative to improve outcomes in acute kidney injury",
                "authors": "Mehta RL, Kellum JA, Shah SV, et al.",
                "journal": "Critical Care",
                "year": 2007,
                "volume": "11",
                "issue": "2",
                "pages": "R31",
                "doi": "10.1186/cc5713",
                "pmid": "17331245",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            }
        ],

        "RIFLE": [
            {
                "type": "primary",
                "title": "Acute renal failure - definition, outcome measures, animal models, fluid therapy and information technology needs: the Second International Consensus Conference of the Acute Dialysis Quality Initiative (ADQI) Group",
                "authors": "Bellomo R, Ronco C, Kellum JA, Mehta RL, Palevsky P",
                "journal": "Critical Care",
                "year": 2004,
                "volume": "8",
                "issue": "4",
                "pages": "R204-R212",
                "doi": "10.1186/cc2872",
                "pmid": "15312219",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            }
        ],

        "AKIN": [
            {
                "type": "primary",
                "title": "Acute Kidney Injury Network: report of an initiative to improve outcomes in acute kidney injury",
                "authors": "Mehta RL, Kellum JA, Shah SV, et al.",
                "journal": "Critical Care",
                "year": 2007,
                "volume": "11",
                "issue": "2",
                "pages": "R31",
                "doi": "10.1186/cc5713",
                "pmid": "17331245",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            }
        ],

}
