"""
Protocol References - Cardiovascular
"""
from typing import List, Dict, Any
from components.references import (
    GRADE_HIGH, GRADE_MODERATE, GRADE_LOW,
    EVIDENCE_LEVEL_I, EVIDENCE_LEVEL_IIA, EVIDENCE_LEVEL_IIB,
    STRENGTH_STRONG, STRENGTH_MODERATE
)


CARDIOVASCULAR_REFERENCES: Dict[str, List[Dict[str, Any]]] = {
        "ACS": [
            {
                "type": "guideline",
                "title": "2020 ESC Guidelines for the management of acute coronary syndromes in patients presenting without persistent ST-segment elevation",
                "authors": "Collet JP, Thiele H, Barbato E, et al.",
                "journal": "European Heart Journal",
                "year": 2021,
                "volume": "42",
                "issue": "14",
                "pages": "1289-1367",
                "doi": "10.1093/eurheartj/ehaa575",
                "pmid": "32860058",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "guideline",
                "title": "2017 ESC Guidelines for the management of acute myocardial infarction in patients presenting with ST-segment elevation",
                "authors": "Ibanez B, James S, Agewall S, et al.",
                "journal": "European Heart Journal",
                "year": 2018,
                "volume": "39",
                "issue": "2",
                "pages": "119-177",
                "doi": "10.1093/eurheartj/ehx393",
                "pmid": "28886621",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "guideline",
                "title": "2021 AHA/ACC/ASE/CHEST/SAEM/SCCT/SCMR Guideline for the Evaluation and Diagnosis of Chest Pain",
                "authors": "Gulati M, Levy PD, Mukherjee D, et al.",
                "journal": "Journal of the American College of Cardiology",
                "year": 2021,
                "volume": "78",
                "issue": "22",
                "pages": "e187-e285",
                "doi": "10.1016/j.jacc.2021.07.053",
                "pmid": "34756653",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            }
        ],

        "Heart Failure": [
            {
                "type": "guideline",
                "title": "2021 ESC Guidelines for the diagnosis and treatment of acute and chronic heart failure",
                "authors": "McDonagh TA, Metra M, Adamo M, et al.",
                "journal": "European Heart Journal",
                "year": 2021,
                "volume": "42",
                "issue": "36",
                "pages": "3599-3726",
                "doi": "10.1093/eurheartj/ehab368",
                "pmid": "34447992",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "guideline",
                "title": "2022 AHA/ACC/HFSA Guideline for the Management of Heart Failure",
                "authors": "Heidenreich PA, Bozkurt B, Aguilar D, et al.",
                "journal": "Journal of the American College of Cardiology",
                "year": 2022,
                "volume": "79",
                "issue": "17",
                "pages": "e263-e421",
                "doi": "10.1016/j.jacc.2021.12.012",
                "pmid": "35379503",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            }
        ],

        "Atrial Fibrillation": [
            {
                "type": "guideline",
                "title": "2020 ESC/EACTS Guidelines for the management of atrial fibrillation",
                "authors": "Hindricks G, Potpara T, Dagres N, et al.",
                "journal": "European Heart Journal",
                "year": 2021,
                "volume": "42",
                "issue": "5",
                "pages": "373-498",
                "doi": "10.1093/eurheartj/ehaa612",
                "pmid": "32860505",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "guideline",
                "title": "2019 AHA/ACC/HRS Focused Update of the 2014 AHA/ACC/HRS Guideline for the Management of Patients With Atrial Fibrillation",
                "authors": "January CT, Wann LS, Calkins H, et al.",
                "journal": "Journal of the American College of Cardiology",
                "year": 2019,
                "volume": "74",
                "issue": "1",
                "pages": "104-132",
                "doi": "10.1016/j.jacc.2019.01.011",
                "pmid": "30703431",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            }
        ],

        "DVT/PE": [
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
            },
            {
                "type": "guideline",
                "title": "Antithrombotic Therapy for VTE Disease: Second Update of the CHEST Guideline and Expert Panel Report",
                "authors": "Stevens SM, Woller SC, Kreuziger LB, et al.",
                "journal": "Chest",
                "year": 2021,
                "volume": "160",
                "issue": "6",
                "pages": "e545-e608",
                "doi": "10.1016/j.chest.2021.07.055",
                "pmid": "34352278",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            }
        ],

        "Anticoagulation Reversal": [
            {
                "type": "guideline",
                "title": "2017 ACC Expert Consensus Decision Pathway on Management of Bleeding in Patients on Oral Anticoagulants",
                "authors": "Tomaselli GF, Mahaffey KW, Cuker A, et al.",
                "journal": "Journal of the American College of Cardiology",
                "year": 2017,
                "volume": "70",
                "issue": "24",
                "pages": "3042-3067",
                "doi": "10.1016/j.jacc.2017.09.1085",
                "pmid": "29157377",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            }
        ],

        "Hypertensive Emergency": [
            {
                "type": "guideline",
                "title": "2017 ACC/AHA/AAPA/ABC/ACPM/AGS/APhA/ASH/ASPC/NMA/PCNA Guideline for the Prevention, Detection, Evaluation, and Management of High Blood Pressure in Adults",
                "authors": "Whelton PK, Carey RM, Aronow WS, et al.",
                "journal": "Journal of the American College of Cardiology",
                "year": 2018,
                "volume": "71",
                "issue": "19",
                "pages": "e127-e248",
                "doi": "10.1016/j.jacc.2017.11.006",
                "pmid": "29146535",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "guideline",
                "title": "2014 Evidence-Based Guideline for the Management of High Blood Pressure in Adults: Report from the Panel Members Appointed to the Eighth Joint National Committee (JNC 8)",
                "authors": "James PA, Oparil S, Carter BL, et al.",
                "journal": "JAMA",
                "year": 2014,
                "volume": "311",
                "issue": "5",
                "pages": "507-520",
                "doi": "10.1001/jama.2013.284427",
                "pmid": "24352797",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "review",
                "title": "Hypertensive Crises: Hypertensive Urgencies and Emergencies",
                "authors": "Varon J, Marik PE",
                "journal": "Cardiology Clinics",
                "year": 2006,
                "volume": "24",
                "issue": "1",
                "pages": "135-146",
                "doi": "10.1016/j.ccl.2005.09.001",
                "pmid": "16326264",
                "evidence_level": EVIDENCE_LEVEL_IIA,
                "strength": STRENGTH_MODERATE
            }
        ],

        "acute_decompensated_hf": [
            {
                "type": "guideline",
                "title": "2021 ESC Guidelines for the diagnosis and treatment of acute and chronic heart failure",
                "authors": "McDonagh TA, Metra M, Adamo M, et al.",
                "journal": "European Heart Journal",
                "year": 2021,
                "volume": "42",
                "issue": "36",
                "pages": "3599-3726",
                "doi": "10.1093/eurheartj/ehab368",
                "pmid": "34447992",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "guideline",
                "title": "2022 AHA/ACC/HFSA Guideline for the Management of Heart Failure",
                "authors": "Heidenreich PA, Bozkurt B, Aguilar D, et al.",
                "journal": "Journal of the American College of Cardiology",
                "year": "2022",
                "volume": "79",
                "issue": "17",
                "pages": "e263-e421",
                "doi": "10.1016/j.jacc.2021.12.012",
                "pmid": "35379503",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "guideline",
                "title": "Acute Heart Failure: Diagnosis and Management",
                "authors": "NICE Guideline",
                "journal": "National Institute for Health and Care Excellence",
                "year": 2014,
                "url": "https://www.nice.org.uk/guidance/cg187",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "review",
                "title": "Acute decompensated heart failure: update on new and emerging evidence and directions for future research",
                "authors": "Gheorghiade M, Follath F, Ponikowski P, et al.",
                "journal": "Journal of Cardiac Failure",
                "year": 2013,
                "volume": "19",
                "issue": "6",
                "pages": "371-389",
                "doi": "10.1016/j.cardfail.2013.04.012",
                "pmid": "23743484",
                "evidence_level": EVIDENCE_LEVEL_IIA,
                "strength": STRENGTH_STRONG
            }
        ],

}
