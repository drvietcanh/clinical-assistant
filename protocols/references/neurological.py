"""
Protocol References - Neurological
"""
from typing import List, Dict, Any
from components.references import (
    GRADE_HIGH, GRADE_MODERATE, GRADE_LOW,
    EVIDENCE_LEVEL_I, EVIDENCE_LEVEL_IIA, EVIDENCE_LEVEL_IIB,
    STRENGTH_STRONG, STRENGTH_MODERATE
)


NEUROLOGICAL_REFERENCES: Dict[str, List[Dict[str, Any]]] = {
        "Traumatic Brain Injury": [
            {
                "type": "guideline",
                "title": "Guidelines for the Management of Severe Traumatic Brain Injury, Fourth Edition",
                "authors": "Carney N, Totten AM, O'Reilly C, et al.",
                "journal": "Neurosurgery",
                "year": 2017,
                "volume": "80",
                "issue": "1",
                "pages": "6-15",
                "doi": "10.1227/NEU.0000000000001432",
                "pmid": "27654000",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            }
        ],

        "Stroke": [
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
            },
            {
                "type": "guideline",
                "title": "Guidelines for the Early Management of Patients With Acute Ischemic Stroke: 2019 Update",
                "authors": "Powers WJ, Rabinstein AA, Ackerson T, et al.",
                "journal": "Stroke",
                "year": "2019",
                "volume": "50",
                "issue": "12",
                "pages": "e344-e418",
                "doi": "10.1161/STR.0000000000000211",
                "pmid": "31662037",
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

        "Status Epilepticus": [
            {
                "type": "guideline",
                "title": "Guideline for the Management of Status Epilepticus",
                "authors": "Glauser T, Shinnar S, Gloss D, et al.",
                "journal": "Epilepsy Currents",
                "year": 2016,
                "volume": "16",
                "issue": "1",
                "pages": "48-61",
                "doi": "10.5698/1535-7597-16.1.48",
                "pmid": "26900382",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "guideline",
                "title": "European Resuscitation Council Guidelines 2021: Adult advanced life support",
                "authors": "Soar J, Böttiger BW, Carli P, et al.",
                "journal": "Resuscitation",
                "year": 2021,
                "volume": "161",
                "pages": "115-151",
                "doi": "10.1016/j.resuscitation.2021.02.010",
                "pmid": "33773825",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            }
        ],

}
