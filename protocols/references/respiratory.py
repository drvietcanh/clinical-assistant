"""
Protocol References - Respiratory
"""
from typing import List, Dict, Any
from components.references import (
    GRADE_HIGH, GRADE_MODERATE, GRADE_LOW,
    EVIDENCE_LEVEL_I, EVIDENCE_LEVEL_IIA, EVIDENCE_LEVEL_IIB,
    STRENGTH_STRONG, STRENGTH_MODERATE
)


RESPIRATORY_REFERENCES: Dict[str, List[Dict[str, Any]]] = {
        "Pneumothorax": [
            {
                "type": "guideline",
                "title": "British Thoracic Society guideline for pleural disease 2023: pneumothorax",
                "authors": "Hallifax RJ, McKeown E, Sivakumar P, et al.",
                "journal": "Thorax",
                "year": 2023,
                "volume": "78",
                "issue": "12",
                "pages": "1161-1176",
                "doi": "10.1136/thorax-2023-219478",
                "pmid": "37936660",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "guideline",
                "title": "Management of spontaneous pneumothorax: an American College of Chest Physicians Delphi consensus statement",
                "authors": "Baumann MH, Strange C, Heffner JE, et al.",
                "journal": "Chest",
                "year": 2001,
                "volume": "119",
                "issue": "2",
                "pages": "590-602",
                "doi": "10.1378/chest.119.2.590",
                "pmid": "11171742",
                "evidence_level": EVIDENCE_LEVEL_IIB,
                "strength": STRENGTH_STRONG
            }
        ],

        "ARDS": [
            {
                "type": "guideline",
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
            },
            {
                "type": "guideline",
                "title": "An Official American Thoracic Society/European Society of Intensive Care Medicine/Society of Critical Care Medicine Clinical Practice Guideline: Mechanical Ventilation in Adult Patients with Acute Respiratory Distress Syndrome",
                "authors": "Fan E, Del Sorbo L, Goligher EC, et al.",
                "journal": "American Journal of Respiratory and Critical Care Medicine",
                "year": 2017,
                "volume": "195",
                "issue": "9",
                "pages": "1253-1263",
                "doi": "10.1164/rccm.201703-0548ST",
                "pmid": "28459336",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            }
        ],

        "COPD": [
            {
                "type": "guideline",
                "title": "Global Strategy for the Diagnosis, Management, and Prevention of Chronic Obstructive Pulmonary Disease 2023 Report",
                "authors": "GOLD Science Committee",
                "journal": "Global Initiative for Chronic Obstructive Lung Disease",
                "year": 2023,
                "url": "https://goldcopd.org/2023-gold-report-2/",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "guideline",
                "title": "Chronic Obstructive Pulmonary Disease in Over 16s: Diagnosis and Management",
                "authors": "NICE Guideline",
                "journal": "National Institute for Health and Care Excellence",
                "year": 2019,
                "url": "https://www.nice.org.uk/guidance/ng115",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            }
        ],

        "Asthma": [
            {
                "type": "guideline",
                "title": "Global Strategy for Asthma Management and Prevention (2023 update)",
                "authors": "GINA Science Committee",
                "journal": "Global Initiative for Asthma",
                "year": 2023,
                "url": "https://ginasthma.org/2023-gina-main-report/",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "guideline",
                "title": "Asthma: diagnosis, monitoring and chronic asthma management",
                "authors": "NICE Guideline",
                "journal": "National Institute for Health and Care Excellence",
                "year": 2021,
                "url": "https://www.nice.org.uk/guidance/ng80",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            }
        ],

        "Bronchiolitis": [
            {
                "type": "guideline",
                "title": "Clinical Practice Guideline: The Diagnosis, Management, and Prevention of Bronchiolitis",
                "authors": "Ralston SL, Lieberthal AS, Meissner HC, et al.",
                "journal": "Pediatrics",
                "year": 2014,
                "volume": "134",
                "issue": "5",
                "pages": "e1474-e1502",
                "doi": "10.1542/peds.2014-2742",
                "pmid": "25349312",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "guideline",
                "title": "Bronchiolitis in children: diagnosis and management (NG9)",
                "authors": "NICE Guideline",
                "journal": "National Institute for Health and Care Excellence",
                "year": 2021,
                "url": "https://www.nice.org.uk/guidance/ng9",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            }
        ],

}
