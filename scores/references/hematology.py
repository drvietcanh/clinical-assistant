"""
Calculator References - Hematology
"""
from typing import List, Dict, Any
from components.references import (
    GRADE_HIGH, GRADE_MODERATE, GRADE_LOW,
    EVIDENCE_LEVEL_I, EVIDENCE_LEVEL_IIA, EVIDENCE_LEVEL_IIB,
    STRENGTH_STRONG, STRENGTH_MODERATE
)


HEMATOLOGY_REFERENCES: Dict[str, List[Dict[str, Any]]] = {
        "Wells DVT": [
            {
                "type": "primary",
                "title": "Value of assessment of pretest probability of deep-vein thrombosis in clinical management",
                "authors": "Wells PS, Hirsh J, Anderson DR, et al.",
                "journal": "Lancet",
                "year": 1997,
                "volume": "350",
                "issue": "9094",
                "pages": "1795-1798",
                "doi": "10.1016/S0140-6736(97)08140-3",
                "pmid": "9428249",
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

        "4Ts Score": [
            {
                "type": "primary",
                "title": "The HIT Expert Probability (HEP) Score: a novel pre-test probability model for heparin-induced thrombocytopenia based on broad expert opinion",
                "authors": "Cuker A, Gimotty PA, Crowther MA, Warkentin TE",
                "journal": "Journal of Thrombosis and Haemostasis",
                "year": 2010,
                "volume": "8",
                "issue": "2",
                "pages": "264-269",
                "doi": "10.1111/j.1538-7836.2009.03684.x",
                "pmid": "19922431",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "primary",
                "title": "Evaluation of pretest clinical score (4 T's) for the diagnosis of heparin-induced thrombocytopenia in two clinical settings",
                "authors": "Cuker A, Arepally G, Crowther MA, et al.",
                "journal": "Journal of Thrombosis and Haemostasis",
                "year": 2006,
                "volume": "4",
                "issue": "4",
                "pages": "759-765",
                "doi": "10.1111/j.1538-7836.2006.01787.x",
                "pmid": "16634744",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            }
        ],

        "Padua": [
            {
                "type": "primary",
                "title": "Risk assessment model for prediction of venous thromboembolism in hospitalized medical patients",
                "authors": "Barbar S, Noventa F, Rossetto V, et al.",
                "journal": "Journal of Thrombosis and Haemostasis",
                "year": 2010,
                "volume": "8",
                "issue": "11",
                "pages": "2450-2457",
                "doi": "10.1111/j.1538-7836.2010.04044.x",
                "pmid": "20738765",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "guideline",
                "title": "American Society of Hematology 2018 guidelines for management of venous thromboembolism: prophylaxis for hospitalized and nonhospitalized medical patients",
                "authors": "Schünemann HJ, Cushman M, Burnett AE, et al.",
                "journal": "Blood Advances",
                "year": 2018,
                "volume": "2",
                "issue": "22",
                "pages": "3198-3225",
                "doi": "10.1182/bloodadvances.2018022954",
                "pmid": "30482765",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            }
        ],

        "DIC Score": [
            {
                "type": "guideline",
                "title": "ISTH interim guidance on recognition and management of coagulopathy in COVID-19",
                "authors": "Thachil J, Tang N, Gando S, et al.",
                "journal": "Journal of Thrombosis and Haemostasis",
                "year": 2020,
                "volume": "18",
                "issue": "5",
                "pages": "1023-1026",
                "doi": "10.1111/jth.14810",
                "pmid": "32338827",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "primary",
                "title": "Towards definition, clinical and laboratory criteria, and a scoring system for disseminated intravascular coagulation",
                "authors": "Taylor FB Jr, Toh CH, Hoots WK, Wada H, Levi M",
                "journal": "Thrombosis and Haemostasis",
                "year": 2001,
                "volume": "86",
                "issue": "5",
                "pages": "1327-1330",
                "pmid": "11816725",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            }
        ],

        "Caprini": [
            {
                "type": "primary",
                "title": "Thrombosis risk assessment as a guide to quality patient care",
                "authors": "Caprini JA",
                "journal": "Disease-a-Month",
                "year": 2005,
                "volume": "51",
                "issue": "2-3",
                "pages": "70-78",
                "doi": "10.1016/j.disamonth.2005.02.003",
                "pmid": "15892287",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            }
        ],

}
