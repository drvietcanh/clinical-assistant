"""
Protocol References - Critical Care
"""
from typing import List, Dict, Any
from components.references import (
    GRADE_HIGH, GRADE_MODERATE, GRADE_LOW,
    EVIDENCE_LEVEL_I, EVIDENCE_LEVEL_IIA, EVIDENCE_LEVEL_IIB,
    STRENGTH_STRONG, STRENGTH_MODERATE
)


CRITICAL_CARE_REFERENCES: Dict[str, List[Dict[str, Any]]] = {
        "Transfusion": [
            {
                "type": "guideline",
                "title": "Red Blood Cell Transfusion: 2023 AABB International Guidelines",
                "authors": "Carson JL, Stanworth SJ, Dennis JA, et al.",
                "journal": "JAMA",
                "year": 2023,
                "volume": "330",
                "issue": "19",
                "pages": "1892-1902",
                "doi": "10.1001/jama.2023.12914",
                "pmid": "37824164",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "guideline",
                "title": "Guidelines for the use of platelet transfusions",
                "authors": "Estcourt LJ, Birchall J, Allard S, et al.",
                "journal": "British Journal of Haematology",
                "year": 2017,
                "volume": "176",
                "issue": "3",
                "pages": "365-394",
                "doi": "10.1111/bjh.14423",
                "pmid": "28009056",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            }
        ],

        "Delirium": [
            {
                "type": "guideline",
                "title": "Clinical Practice Guidelines for the Prevention and Management of Pain, Agitation/Sedation, Delirium, Immobility, and Sleep Disruption in Adult Patients in the ICU",
                "authors": "Devlin JW, Skrobik Y, Gélinas C, et al.",
                "journal": "Critical Care Medicine",
                "year": 2018,
                "volume": "46",
                "issue": "9",
                "pages": "e825-e873",
                "doi": "10.1097/CCM.0000000000003299",
                "pmid": "30113379",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            }
        ],

        "Ventilator Weaning": [
            {
                "type": "guideline",
                "title": "An Official American Thoracic Society/American College of Chest Physicians Clinical Practice Guideline: Liberation from Mechanical Ventilation in Critically Ill Adults",
                "authors": "Schmidt GA, Girard TD, Kress JP, et al.",
                "journal": "American Journal of Respiratory and Critical Care Medicine",
                "year": 2017,
                "volume": "195",
                "issue": "1",
                "pages": "120-133",
                "doi": "10.1164/rccm.201610-2075ST",
                "pmid": "27762595",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            }
        ],

        "Stress Ulcer": [
            {
                "type": "guideline",
                "title": "ASHP Therapeutic Guidelines on Stress Ulcer Prophylaxis",
                "authors": "ASHP Commission on Therapeutics",
                "journal": "American Journal of Health-System Pharmacy",
                "year": 1999,
                "volume": "56",
                "issue": "4",
                "pages": "347-379",
                "doi": "10.1093/ajhp/56.4.347",
                "pmid": "10079790",
                "evidence_level": EVIDENCE_LEVEL_IIA,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "guideline",
                "title": "Canadian Critical Care Society Clinical Practice Guideline: Stress Ulcer Prophylaxis",
                "authors": "Cook DJ, Guyatt GH, Marshall J, et al.",
                "journal": "Critical Care Medicine",
                "year": 2016,
                "volume": "44",
                "issue": "7",
                "pages": "1395-1405",
                "doi": "10.1097/CCM.0000000000001715",
                "pmid": "27028330",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "primary",
                "title": "Stress ulcer prophylaxis in the intensive care unit",
                "authors": "Barkun AN, Bardou M, Pham CQ, Martel M",
                "journal": "New England Journal of Medicine",
                "year": 2010,
                "volume": "362",
                "issue": "1",
                "pages": "1-11",
                "doi": "10.1056/NEJMra0905447",
                "pmid": "20007663",
                "evidence_level": EVIDENCE_LEVEL_IIA,
                "strength": STRENGTH_STRONG
            }
        ],

        "Sedation": [
            {
                "type": "guideline",
                "title": "Clinical Practice Guidelines for the Prevention and Management of Pain, Agitation/Sedation, Delirium, Immobility, and Sleep Disruption in Adult Patients in the ICU",
                "authors": "Devlin JW, Skrobik Y, Gélinas C, et al.",
                "journal": "Critical Care Medicine",
                "year": 2018,
                "volume": "46",
                "issue": "9",
                "pages": "e825-e873",
                "doi": "10.1097/CCM.0000000000003299",
                "pmid": "30113379",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            }
        ],

        "Intracranial Hypertension": [
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
            },
            {
                "type": "guideline",
                "title": "Management of Intracranial Hypertension",
                "authors": "Brain Trauma Foundation",
                "journal": "Journal of Neurotrauma",
                "year": 2016,
                "volume": "33",
                "issue": "15",
                "pages": "1461-1473",
                "doi": "10.1089/neu.2016.4506",
                "pmid": "27025960",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "review",
                "title": "Elevated intracranial pressure",
                "authors": "Raboel PH, Bartek J Jr, Andresen M, Bellander BM, Romner B",
                "journal": "Critical Care",
                "year": 2012,
                "volume": "16",
                "issue": "2",
                "pages": "216",
                "doi": "10.1186/cc11232",
                "pmid": "22429510",
                "evidence_level": EVIDENCE_LEVEL_IIA,
                "strength": STRENGTH_STRONG
            }
        ],

        "acute_respiratory_failure": [
            {
                "type": "guideline",
                "title": "An Official American Thoracic Society/American College of Chest Physicians Clinical Practice Guideline: Liberation from Mechanical Ventilation in Critically Ill Adults",
                "authors": "Schmidt GA, Girard TD, Kress JP, et al.",
                "journal": "American Journal of Respiratory and Critical Care Medicine",
                "year": 2017,
                "volume": "195",
                "issue": "1",
                "pages": "120-133",
                "doi": "10.1164/rccm.201610-2075ST",
                "pmid": "27762595",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "guideline",
                "title": "Noninvasive Ventilation for Acute Respiratory Failure",
                "authors": "Rochwerg B, Brochard L, Elliott MW, et al.",
                "journal": "European Respiratory Journal",
                "year": 2017,
                "volume": "50",
                "issue": "2",
                "pages": "1602426",
                "doi": "10.1183/13993003.02426-2016",
                "pmid": "28860265",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "guideline",
                "title": "Clinical Practice Guideline: Management of Acute Respiratory Failure",
                "authors": "SCCM Critical Care Guidelines Committee",
                "journal": "Critical Care Medicine",
                "year": 2017,
                "volume": "45",
                "issue": "3",
                "pages": "315-341",
                "doi": "10.1097/CCM.0000000000002254",
                "pmid": "28114151",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "review",
                "title": "Acute respiratory failure",
                "authors": "Roussos C, Koutsoukou A",
                "journal": "European Respiratory Journal",
                "year": 2003,
                "volume": "22",
                "issue": "47_suppl",
                "pages": "3s-14s",
                "doi": "10.1183/09031936.03.00020103",
                "pmid": "14621112",
                "evidence_level": EVIDENCE_LEVEL_IIA,
                "strength": STRENGTH_STRONG
            }
        ],

        "spinal_cord_injury": [
            {
                "type": "guideline",
                "title": "Guidelines for the Management of Acute Cervical Spine and Spinal Cord Injuries",
                "authors": "Ryb GE, Dischinger PC, Ho SM",
                "journal": "Neurosurgery",
                "year": 2013,
                "volume": "72",
                "issue": "Suppl 2",
                "pages": "1-259",
                "doi": "10.1227/NEU.0b013e318276ee40",
                "pmid": "23417184",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "guideline",
                "title": "Spinal injury: assessment and initial management",
                "authors": "NICE Guideline",
                "journal": "National Institute for Health and Care Excellence",
                "year": 2016,
                "url": "https://www.nice.org.uk/guidance/ng41",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "guideline",
                "title": "Early Acute Management in Adults with Spinal Cord Injury: A Clinical Practice Guideline for Health-Care Professionals",
                "authors": "Consortium for Spinal Cord Medicine",
                "journal": "Journal of Spinal Cord Medicine",
                "year": 2008,
                "volume": "31",
                "issue": "4",
                "pages": "403-479",
                "doi": "10.1080/10790268.2008.11760740",
                "pmid": "18959359",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "review",
                "title": "Acute spinal cord injury",
                "authors": "Eckert MJ, Martin MJ",
                "journal": "New England Journal of Medicine",
                "year": 2017,
                "volume": "376",
                "issue": "8",
                "pages": "765-775",
                "doi": "10.1056/NEJMra1603589",
                "pmid": "28225675",
                "evidence_level": EVIDENCE_LEVEL_IIA,
                "strength": STRENGTH_STRONG
            }
        ],

}
