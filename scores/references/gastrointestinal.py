"""
Calculator References - Gastrointestinal
"""
from typing import List, Dict, Any
from components.references import (
    GRADE_HIGH, GRADE_MODERATE, GRADE_LOW,
    EVIDENCE_LEVEL_I, EVIDENCE_LEVEL_IIA, EVIDENCE_LEVEL_IIB,
    STRENGTH_STRONG, STRENGTH_MODERATE
)


GASTROINTESTINAL_REFERENCES: Dict[str, List[Dict[str, Any]]] = {
        "ROCKALL": [
            {
                "type": "primary",
                "title": "Risk assessment after acute upper gastrointestinal haemorrhage",
                "authors": "Rockall TA, Logan RF, Devlin HB, Northfield TC",
                "journal": "Gut",
                "year": 1996,
                "volume": "38",
                "issue": "3",
                "pages": "316-321",
                "doi": "10.1136/gut.38.3.316",
                "pmid": "8801197",
                "evidence_level": EVIDENCE_LEVEL_IIA,
                "strength": STRENGTH_STRONG
            }
        ],

        "RANSON": [
            {
                "type": "primary",
                "title": "Prognostic signs and the role of operative management in acute pancreatitis",
                "authors": "Ranson JHC, Rifkind KM, Roses DF, Fink SD, Eng K, Spencer FC",
                "journal": "Surgery, Gynecology & Obstetrics",
                "year": 1974,
                "volume": "139",
                "issue": "1",
                "pages": "69-81",
                "pmid": "4834279",
                "evidence_level": EVIDENCE_LEVEL_IIB,
                "strength": STRENGTH_STRONG
            }
        ],

        "MELD": [
            {
                "type": "primary",
                "title": "A model to predict survival in patients with end-stage liver disease",
                "authors": "Kamath PS, Wiesner RH, Malinchoc M, et al.",
                "journal": "Hepatology",
                "year": 2001,
                "volume": "33",
                "issue": "2",
                "pages": "464-470",
                "doi": "10.1053/jhep.2001.22172",
                "pmid": "11172350",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "guideline",
                "title": "AASLD Practice Guidelines: Evaluation of the Patient for Liver Transplantation",
                "authors": "Martin P, DiMartini A, Feng S, Brown R, Fallon M",
                "journal": "Hepatology",
                "year": 2014,
                "volume": "60",
                "issue": "2",
                "pages": "715-735",
                "doi": "10.1002/hep.27272",
                "pmid": "25042480",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            }
        ],

        "Child-Pugh": [
            {
                "type": "primary",
                "title": "Transection of the oesophagus for bleeding oesophageal varices",
                "authors": "Pugh RN, Murray-Lyon IM, Dawson JL, Pietroni MC, Williams R",
                "journal": "British Journal of Surgery",
                "year": 1973,
                "volume": "60",
                "issue": "8",
                "pages": "646-649",
                "doi": "10.1002/bjs.1800600817",
                "pmid": "4541913",
                "evidence_level": EVIDENCE_LEVEL_IIA,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "guideline",
                "title": "AASLD Practice Guidelines: Evaluation of the Patient for Liver Transplantation",
                "authors": "Martin P, DiMartini A, Feng S, Brown R, Fallon M",
                "journal": "Hepatology",
                "year": 2014,
                "volume": "60",
                "issue": "2",
                "pages": "715-735",
                "doi": "10.1002/hep.27272",
                "pmid": "25042480",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            }
        ],

        "BISAP": [
            {
                "type": "primary",
                "title": "A simple bedside score (BISAP) for early identification of patients at high risk of in-hospital mortality in acute pancreatitis",
                "authors": "Wu BU, Johannes RS, Sun X, Tabak Y, Conwell DL, Banks PA",
                "journal": "American Journal of Gastroenterology",
                "year": 2009,
                "volume": "104",
                "issue": "4",
                "pages": "966-971",
                "doi": "10.1038/ajg.2009.28",
                "pmid": "19293784",
                "evidence_level": EVIDENCE_LEVEL_IIA,
                "strength": STRENGTH_MODERATE
            }
        ],

        "Child-Pugh": [
            {
                "type": "primary",
                "title": "Transection of the oesophagus for bleeding oesophageal varices",
                "authors": "Pugh RN, Murray-Lyon IM, Dawson JL, Pietroni MC, Williams R",
                "journal": "British Journal of Surgery",
                "year": 1973,
                "volume": "60",
                "issue": "8",
                "pages": "646-649",
                "doi": "10.1002/bjs.1800600817",
                "pmid": "4541913",
                "evidence_level": EVIDENCE_LEVEL_IIA,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "guideline",
                "title": "AASLD Practice Guidelines: Evaluation of the Patient for Liver Transplantation",
                "authors": "Martin P, DiMartini A, Feng S, Brown R, Fallon M",
                "journal": "Hepatology",
                "year": 2014,
                "volume": "60",
                "issue": "2",
                "pages": "715-735",
                "doi": "10.1002/hep.27272",
                "pmid": "25042480",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            }
        ],

        "Glasgow-Blatchford": [
            {
                "type": "primary",
                "title": "A risk score to predict need for treatment for upper-gastrointestinal haemorrhage",
                "authors": "Blatchford O, Murray WR, Blatchford M",
                "journal": "Lancet",
                "year": 2000,
                "volume": "356",
                "issue": "9238",
                "pages": "1318-1321",
                "doi": "10.1016/S0140-6736(00)02816-6",
                "pmid": "11073021",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "guideline",
                "title": "Management of acute upper and lower gastrointestinal bleeding",
                "authors": "Barkun AN, Bardou M, Kuipers EJ, et al.",
                "journal": "Scandinavian Journal of Gastroenterology",
                "year": 2010,
                "volume": "45",
                "issue": "12",
                "pages": "1332-1341",
                "doi": "10.3109/00365521.2010.517450",
                "pmid": "21073373",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            }
        ],

}
