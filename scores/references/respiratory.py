"""
Calculator References - Respiratory
"""
from typing import List, Dict, Any
from components.references import (
    GRADE_HIGH, GRADE_MODERATE, GRADE_LOW,
    EVIDENCE_LEVEL_I, EVIDENCE_LEVEL_IIA, EVIDENCE_LEVEL_IIB,
    STRENGTH_STRONG, STRENGTH_MODERATE
)


RESPIRATORY_REFERENCES: Dict[str, List[Dict[str, Any]]] = {
        "Wells PE": [
            {
                "type": "primary",
                "title": "Derivation of a simple clinical model to categorize patients probability of pulmonary embolism: increasing the models utility with the SimpliRED D-dimer",
                "authors": "Wells PS, Anderson DR, Rodger M, et al.",
                "journal": "Thrombosis and Haemostasis",
                "year": 2000,
                "volume": "83",
                "issue": "3",
                "pages": "416-420",
                "pmid": "10744147",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "guideline",
                "title": "2019 ESC Guidelines for the diagnosis and management of acute pulmonary embolism developed in collaboration with the European Respiratory Society (ERS)",
                "authors": "Konstantinides SV, Meyer G, Becattini C, et al.",
                "journal": "European Heart Journal",
                "year": 2020,
                "volume": "41",
                "issue": "4",
                "pages": "543-603",
                "doi": "10.1093/eurheartj/ehz405",
                "pmid": "31504429",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            }
        ],

        "PERC": [
            {
                "type": "primary",
                "title": "Clinical criteria to prevent unnecessary diagnostic testing in emergency department patients with suspected pulmonary embolism",
                "authors": "Kline JA, Mitchell AM, Kabrhel C, Richman PB, Courtney DM",
                "journal": "Journal of Thrombosis and Haemostasis",
                "year": 2004,
                "volume": "2",
                "issue": "8",
                "pages": "1247-1255",
                "doi": "10.1111/j.1538-7836.2004.00790.x",
                "pmid": "15304025",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "guideline",
                "title": "2019 ESC Guidelines for the diagnosis and management of acute pulmonary embolism",
                "authors": "Konstantinides SV, Meyer G, Becattini C, et al.",
                "journal": "European Heart Journal",
                "year": 2020,
                "volume": "41",
                "issue": "4",
                "pages": "543-603",
                "doi": "10.1093/eurheartj/ehz405",
                "pmid": "31504429",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            }
        ],

        "CURB-65": [
            {
                "type": "primary",
                "title": "Defining community acquired pneumonia severity on presentation to hospital: an international derivation and validation study",
                "authors": "Lim WS, van der Eerden MM, Laing R, et al.",
                "journal": "Thorax",
                "year": 2003,
                "volume": "58",
                "issue": "5",
                "pages": "377-382",
                "doi": "10.1136/thorax.58.5.377",
                "pmid": "12728155",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "guideline",
                "title": "Community-acquired pneumonia in adults: diagnosis and management",
                "authors": "NICE Guideline",
                "journal": "National Institute for Health and Care Excellence",
                "year": 2019,
                "url": "https://www.nice.org.uk/guidance/ng138",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            }
        ],

        "PESI": [
            {
                "type": "primary",
                "title": "A prediction rule to identify low-risk patients with pulmonary embolism",
                "authors": "Aujesky D, Obrosky DS, Stone RA, et al.",
                "journal": "Archives of Internal Medicine",
                "year": 2005,
                "volume": "165",
                "issue": "4",
                "pages": "458-462",
                "doi": "10.1001/archinte.165.4.458",
                "pmid": "15738375",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "guideline",
                "title": "2019 ESC Guidelines for the diagnosis and management of acute pulmonary embolism",
                "authors": "Konstantinides SV, Meyer G, Becattini C, et al.",
                "journal": "European Heart Journal",
                "year": 2020,
                "volume": "41",
                "issue": "4",
                "pages": "543-603",
                "doi": "10.1093/eurheartj/ehz405",
                "pmid": "31504429",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            }
        ],

        "PSI/PORT": [
            {
                "type": "primary",
                "title": "A prediction rule to identify low-risk patients with community-acquired pneumonia",
                "authors": "Fine MJ, Auble TE, Yealy DM, et al.",
                "journal": "New England Journal of Medicine",
                "year": 1997,
                "volume": "336",
                "issue": "4",
                "pages": "243-250",
                "doi": "10.1056/NEJM199701233360402",
                "pmid": "8995086",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "guideline",
                "title": "Community-acquired pneumonia in adults: diagnosis and management",
                "authors": "NICE Guideline",
                "journal": "National Institute for Health and Care Excellence",
                "year": 2019,
                "url": "https://www.nice.org.uk/guidance/ng138",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            }
        ],

        "PERC": [
            {
                "type": "primary",
                "title": "Clinical criteria to prevent unnecessary diagnostic testing in emergency department patients with suspected pulmonary embolism",
                "authors": "Kline JA, Mitchell AM, Kabrhel C, Richman PB, Courtney DM",
                "journal": "Journal of Thrombosis and Haemostasis",
                "year": 2004,
                "volume": "2",
                "issue": "8",
                "pages": "1247-1255",
                "doi": "10.1111/j.1538-7836.2004.00790.x",
                "pmid": "15304025",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "guideline",
                "title": "2019 ESC Guidelines for the diagnosis and management of acute pulmonary embolism",
                "authors": "Konstantinides SV, Meyer G, Becattini C, et al.",
                "journal": "European Heart Journal",
                "year": 2020,
                "volume": "41",
                "issue": "4",
                "pages": "543-603",
                "doi": "10.1093/eurheartj/ehz405",
                "pmid": "31504429",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            }
        ],

        "SMART-COP": [
            {
                "type": "primary",
                "title": "SMART-COP: a tool for predicting the need for intensive respiratory or vasopressor support in community-acquired pneumonia",
                "authors": "Charles PG, Wolfe R, Whitby M, et al.",
                "journal": "Clinical Infectious Diseases",
                "year": 2008,
                "volume": "47",
                "issue": "3",
                "pages": "375-384",
                "doi": "10.1086/589754",
                "pmid": "18558884",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            }
        ],

        "ARDS Berlin": [
            {
                "type": "guideline",
                "title": "The Berlin definition of ARDS: an expanded rationale, justification, and supplementary material",
                "authors": "ARDS Definition Task Force",
                "journal": "Intensive Care Medicine",
                "year": 2012,
                "volume": "38",
                "issue": "10",
                "pages": "1573-1582",
                "doi": "10.1007/s00134-012-2682-3",
                "pmid": "22926653",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "primary",
                "title": "Acute respiratory distress syndrome: the Berlin Definition",
                "authors": "ARDS Definition Task Force",
                "journal": "JAMA",
                "year": 2012,
                "volume": "307",
                "issue": "23",
                "pages": "2526-2533",
                "doi": "10.1001/jama.2012.5669",
                "pmid": "22797452",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            }
        ],

        "BODE Index": [
            {
                "type": "primary",
                "title": "The body-mass index, airflow obstruction, dyspnea, and exercise capacity index in chronic obstructive pulmonary disease",
                "authors": "Celli BR, Cote CG, Marin JM, et al.",
                "journal": "New England Journal of Medicine",
                "year": 2004,
                "volume": "350",
                "issue": "10",
                "pages": "1005-1012",
                "doi": "10.1056/NEJMoa021322",
                "pmid": "15014182",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            }
        ],

}
