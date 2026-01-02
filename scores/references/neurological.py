"""
Calculator References - Neurological
"""
from typing import List, Dict, Any
from components.references import (
    GRADE_HIGH, GRADE_MODERATE, GRADE_LOW,
    EVIDENCE_LEVEL_I, EVIDENCE_LEVEL_IIA, EVIDENCE_LEVEL_IIB,
    STRENGTH_STRONG, STRENGTH_MODERATE
)


NEUROLOGICAL_REFERENCES: Dict[str, List[Dict[str, Any]]] = {
        "GCS": [
            {
                "type": "primary",
                "title": "Assessment of coma and impaired consciousness. A practical scale",
                "authors": "Teasdale G, Jennett B",
                "journal": "Lancet",
                "year": 1974,
                "volume": "2",
                "issue": "7872",
                "pages": "81-84",
                "doi": "10.1016/s0140-6736(74)91639-0",
                "pmid": "4136544",
                "evidence_level": EVIDENCE_LEVEL_IIA,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "guideline",
                "title": "The Glasgow Coma Scale at 40 years: standing the test of time",
                "authors": "Teasdale G, Maas A, Lecky F, Manley G, Stocchetti N, Murray G",
                "journal": "Lancet Neurology",
                "year": 2014,
                "volume": "13",
                "issue": "8",
                "pages": "844-854",
                "doi": "10.1016/S1474-4422(14)70120-6",
                "pmid": "25030516",
                "evidence_level": EVIDENCE_LEVEL_IIA,
                "strength": STRENGTH_STRONG
            }
        ],

        "NIHSS": [
            {
                "type": "primary",
                "title": "Measurements of acute cerebral infarction: a clinical examination scale",
                "authors": "Brott T, Adams HP Jr, Olinger CP, et al.",
                "journal": "Stroke",
                "year": 1989,
                "volume": "20",
                "issue": "7",
                "pages": "864-870",
                "doi": "10.1161/01.str.20.7.864",
                "pmid": "2749846",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "guideline",
                "title": "2018 Guidelines for the Early Management of Patients With Acute Ischemic Stroke",
                "authors": "Powers WJ, Rabinstein AA, Ackerson T, et al.",
                "journal": "Stroke",
                "year": 2018,
                "volume": "49",
                "issue": "3",
                "pages": "e46-e110",
                "doi": "10.1161/STR.0000000000000158",
                "pmid": "29367334",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            }
        ],

        "ICH Score": [
            {
                "type": "primary",
                "title": "The ICH score: a simple, reliable grading scale for intracerebral hemorrhage",
                "authors": "Hemphill JC 3rd, Bonovich DC, Besmertis L, Manley GT, Johnston SC",
                "journal": "Stroke",
                "year": 2001,
                "volume": "32",
                "issue": "4",
                "pages": "891-897",
                "doi": "10.1161/01.str.32.4.891",
                "pmid": "11283388",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "guideline",
                "title": "Guidelines for the Management of Spontaneous Intracerebral Hemorrhage",
                "authors": "Hemphill JC 3rd, Greenberg SM, Anderson CS, et al.",
                "journal": "Stroke",
                "year": 2015,
                "volume": "46",
                "issue": "7",
                "pages": "2032-2060",
                "doi": "10.1161/STR.0000000000000069",
                "pmid": "26022637",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            }
        ],

        "Hunt & Hess": [
            {
                "type": "primary",
                "title": "Surgical risk as related to time of intervention in the repair of intracranial aneurysms",
                "authors": "Hunt WE, Hess RM",
                "journal": "Journal of Neurosurgery",
                "year": 1968,
                "volume": "28",
                "issue": "1",
                "pages": "14-20",
                "doi": "10.3171/jns.1968.28.1.0014",
                "pmid": "5635959",
                "evidence_level": EVIDENCE_LEVEL_IIA,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "guideline",
                "title": "Guidelines for the Management of Aneurysmal Subarachnoid Hemorrhage",
                "authors": "Connolly ES Jr, Rabinstein AA, Carhuapoma JR, et al.",
                "journal": "Stroke",
                "year": 2012,
                "volume": "43",
                "issue": "6",
                "pages": "1711-1737",
                "doi": "10.1161/STR.0b013e3182587839",
                "pmid": "22556195",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            }
        ],

        "mRS": [
            {
                "type": "primary",
                "title": "Interobserver agreement for the assessment of handicap in stroke patients",
                "authors": "van Swieten JC, Koudstaal PJ, Visser MC, Schouten HJ, van Gijn J",
                "journal": "Stroke",
                "year": 1988,
                "volume": "19",
                "issue": "5",
                "pages": "604-607",
                "doi": "10.1161/01.str.19.5.604",
                "pmid": "3363593",
                "evidence_level": EVIDENCE_LEVEL_IIA,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "guideline",
                "title": "2018 Guidelines for the Early Management of Patients With Acute Ischemic Stroke",
                "authors": "Powers WJ, Rabinstein AA, Ackerson T, et al.",
                "journal": "Stroke",
                "year": 2018,
                "volume": "49",
                "issue": "3",
                "pages": "e46-e110",
                "doi": "10.1161/STR.0000000000000158",
                "pmid": "29367334",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            }
        ],

        "ABCD2": [
            {
                "type": "primary",
                "title": "A simple score (ABCD) to identify individuals at high early risk of stroke after transient ischaemic attack",
                "authors": "Johnston SC, Rothwell PM, Nguyen-Huynh MN, et al.",
                "journal": "Lancet",
                "year": 2007,
                "volume": "369",
                "issue": "9558",
                "pages": "283-292",
                "doi": "10.1016/S0140-6736(07)60151-0",
                "pmid": "17258669",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "guideline",
                "title": "Guidelines for the Early Management of Patients With Acute Ischemic Stroke: 2019 Update",
                "authors": "Powers WJ, Rabinstein AA, Ackerson T, et al.",
                "journal": "Stroke",
                "year": 2019,
                "volume": "50",
                "issue": "12",
                "pages": "e344-e418",
                "doi": "10.1161/STR.0000000000000211",
                "pmid": "31662037",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            }
        ],

        "Pediatric GCS": [
            {
                "type": "primary",
                "title": "Assessment of coma and impaired consciousness. A practical scale",
                "authors": "Teasdale G, Jennett B",
                "journal": "Lancet",
                "year": 1974,
                "volume": "2",
                "issue": "7872",
                "pages": "81-84",
                "doi": "10.1016/s0140-6736(74)91639-0",
                "pmid": "4136544",
                "evidence_level": EVIDENCE_LEVEL_IIA,
                "strength": STRENGTH_STRONG
            }
        ],

}
