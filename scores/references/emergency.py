"""
Calculator References - Emergency
"""
from typing import List, Dict, Any
from components.references import (
    GRADE_HIGH, GRADE_MODERATE, GRADE_LOW,
    EVIDENCE_LEVEL_I, EVIDENCE_LEVEL_IIA, EVIDENCE_LEVEL_IIB,
    STRENGTH_STRONG, STRENGTH_MODERATE
)


EMERGENCY_REFERENCES: Dict[str, List[Dict[str, Any]]] = {
        "SOFA": [
            {
                "type": "primary",
                "title": "The SOFA (Sepsis-related Organ Failure Assessment) score to describe organ dysfunction/failure",
                "authors": "Vincent JL, Moreno R, Takala J, et al.",
                "journal": "Intensive Care Medicine",
                "year": 1996,
                "volume": "22",
                "issue": "7",
                "pages": "707-710",
                "doi": "10.1007/BF01709751",
                "pmid": "8844239",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "guideline",
                "title": "The Third International Consensus Definitions for Sepsis and Septic Shock (Sepsis-3)",
                "authors": "Singer M, Deutschman CS, Seymour CW, et al.",
                "journal": "JAMA",
                "year": 2016,
                "volume": "315",
                "issue": "8",
                "pages": "801-810",
                "doi": "10.1001/jama.2016.0287",
                "pmid": "26903338",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            }
        ],

        "qSOFA": [
            {
                "type": "primary",
                "title": "Assessment of Clinical Criteria for Sepsis: For the Third International Consensus Definitions for Sepsis and Septic Shock (Sepsis-3)",
                "authors": "Seymour CW, Liu VX, Iwashyna TJ, et al.",
                "journal": "JAMA",
                "year": 2016,
                "volume": "315",
                "issue": "8",
                "pages": "762-774",
                "doi": "10.1001/jama.2016.0288",
                "pmid": "26903335",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "guideline",
                "title": "The Third International Consensus Definitions for Sepsis and Septic Shock (Sepsis-3)",
                "authors": "Singer M, Deutschman CS, Seymour CW, et al.",
                "journal": "JAMA",
                "year": 2016,
                "volume": "315",
                "issue": "8",
                "pages": "801-810",
                "doi": "10.1001/jama.2016.0287",
                "pmid": "26903338",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            }
        ],

        "NEWS2": [
            {
                "type": "guideline",
                "title": "National Early Warning Score (NEWS) 2: Standardising the assessment of acute-illness severity in the NHS",
                "authors": "Royal College of Physicians",
                "journal": "Royal College of Physicians",
                "year": 2017,
                "url": "https://www.rcplondon.ac.uk/projects/outputs/national-early-warning-score-news-2",
                "evidence_level": EVIDENCE_LEVEL_IIA,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "primary",
                "title": "The ability of the National Early Warning Score (NEWS) to discriminate patients at risk of early cardiac arrest, unanticipated intensive care unit admission, and death",
                "authors": "Smith GB, Prytherch DR, Meredith P, Schmidt PE, Featherstone PI",
                "journal": "Resuscitation",
                "year": 2013,
                "volume": "84",
                "issue": "4",
                "pages": "465-470",
                "doi": "10.1016/j.resuscitation.2012.12.016",
                "pmid": "23295778",
                "evidence_level": EVIDENCE_LEVEL_IIA,
                "strength": STRENGTH_MODERATE
            }
        ],

        "APACHE II": [
            {
                "type": "primary",
                "title": "APACHE II: a severity of disease classification system",
                "authors": "Knaus WA, Draper EA, Wagner DP, Zimmerman JE",
                "journal": "Critical Care Medicine",
                "year": 1985,
                "volume": "13",
                "issue": "10",
                "pages": "818-829",
                "pmid": "3928249",
                "evidence_level": EVIDENCE_LEVEL_IIA,
                "strength": STRENGTH_STRONG
            }
        ],

        "SAPS II": [
            {
                "type": "primary",
                "title": "A new Simplified Acute Physiology Score (SAPS II) based on a European/North American multicenter study",
                "authors": "Le Gall JR, Lemeshow S, Saulnier F",
                "journal": "JAMA",
                "year": 1993,
                "volume": "270",
                "issue": "24",
                "pages": "2957-2963",
                "doi": "10.1001/jama.1993.03510240069035",
                "pmid": "8254858",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            }
        ],

        "RTS": [
            {
                "type": "primary",
                "title": "The Injury Severity Score: a method for describing patients with multiple injuries and evaluating emergency care",
                "authors": "Baker SP, O'Neill B, Haddon W Jr, Long WB",
                "journal": "Journal of Trauma",
                "year": 1974,
                "volume": "14",
                "issue": "3",
                "pages": "187-196",
                "pmid": "4814394",
                "evidence_level": EVIDENCE_LEVEL_IIA,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "primary",
                "title": "A revision of the Trauma Score",
                "authors": "Champion HR, Sacco WJ, Copes WS, Gann DS, Gennarelli TA, Flanagan ME",
                "journal": "Journal of Trauma",
                "year": 1989,
                "volume": "29",
                "issue": "5",
                "pages": "623-629",
                "pmid": "2657085",
                "evidence_level": EVIDENCE_LEVEL_IIA,
                "strength": STRENGTH_STRONG
            }
        ],

        "ISS": [
            {
                "type": "primary",
                "title": "The Injury Severity Score: a method for describing patients with multiple injuries and evaluating emergency care",
                "authors": "Baker SP, O'Neill B, Haddon W Jr, Long WB",
                "journal": "Journal of Trauma",
                "year": 1974,
                "volume": "14",
                "issue": "3",
                "pages": "187-196",
                "pmid": "4814394",
                "evidence_level": EVIDENCE_LEVEL_IIA,
                "strength": STRENGTH_STRONG
            }
        ],

        "MEWS": [
            {
                "type": "primary",
                "title": "Validation of a modified Early Warning Score in medical admissions",
                "authors": "Subbe CP, Kruger M, Rutherford P, Gemmel L",
                "journal": "QJM",
                "year": 2001,
                "volume": "94",
                "issue": "10",
                "pages": "521-526",
                "doi": "10.1093/qjmed/94.10.521",
                "pmid": "11588210",
                "evidence_level": EVIDENCE_LEVEL_IIA,
                "strength": STRENGTH_MODERATE
            }
        ],

        "SIRS": [
            {
                "type": "primary",
                "title": "American College of Chest Physicians/Society of Critical Care Medicine Consensus Conference: definitions for sepsis and organ failure and guidelines for the use of innovative therapies in sepsis",
                "authors": "American College of Chest Physicians/Society of Critical Care Medicine Consensus Conference Committee",
                "journal": "Critical Care Medicine",
                "year": 1992,
                "volume": "20",
                "issue": "6",
                "pages": "864-874",
                "doi": "10.1097/00003246-199206000-00025",
                "pmid": "1597042",
                "evidence_level": EVIDENCE_LEVEL_IIA,
                "strength": STRENGTH_STRONG
            }
        ],

        "PELOD-2": [
            {
                "type": "primary",
                "title": "PELOD-2: an update of the PEdiatric logistic organ dysfunction score",
                "authors": "Leteurtre S, Duhamel A, Salleron J, et al.",
                "journal": "Critical Care Medicine",
                "year": 2013,
                "volume": "41",
                "issue": "9",
                "pages": "1761-1773",
                "doi": "10.1097/CCM.0b013e31828a2bbd",
                "pmid": "23887231",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            }
        ],

        "PRISM III": [
            {
                "type": "primary",
                "title": "PRISM III: an updated Pediatric Risk of Mortality score",
                "authors": "Pollack MM, Patel KM, Ruttimann UE",
                "journal": "Critical Care Medicine",
                "year": 1996,
                "volume": "24",
                "issue": "5",
                "pages": "743-752",
                "doi": "10.1097/00003246-199605000-00004",
                "pmid": "8706448",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            }
        ],

        "PIM2": [
            {
                "type": "primary",
                "title": "The Pediatric Index of Mortality 2 (PIM2): a revised version of the Pediatric Index of Mortality",
                "authors": "Slater A, Shann F, Pearson G",
                "journal": "Intensive Care Medicine",
                "year": 2003,
                "volume": "29",
                "issue": "2",
                "pages": "278-285",
                "doi": "10.1007/s00134-002-1601-2",
                "pmid": "12594588",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            }
        ],

}
