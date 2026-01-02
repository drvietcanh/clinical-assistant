"""
Protocol References - Other
"""
from typing import List, Dict, Any
from components.references import (
    GRADE_HIGH, GRADE_MODERATE, GRADE_LOW,
    EVIDENCE_LEVEL_I, EVIDENCE_LEVEL_IIA, EVIDENCE_LEVEL_IIB,
    STRENGTH_STRONG, STRENGTH_MODERATE
)


OTHER_REFERENCES: Dict[str, List[Dict[str, Any]]] = {
        "Acute Pain": [
            {
                "type": "guideline",
                "title": "Management of Postoperative Pain: A Clinical Practice Guideline",
                "authors": "Chou R, Gordon DB, de Leon-Casasola OA, et al.",
                "journal": "Journal of Pain",
                "year": 2016,
                "volume": "17",
                "issue": "2",
                "pages": "131-157",
                "doi": "10.1016/j.jpain.2015.12.008",
                "pmid": "26827847",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "guideline",
                "title": "ASIPP Guidelines for Responsible Opioid Prescribing in Chronic Non-Cancer Pain: Part I - Evidence Assessment",
                "authors": "Manchikanti L, Abdi S, Atluri S, et al.",
                "journal": "Pain Physician",
                "year": 2012,
                "volume": "15",
                "issue": "3 Suppl",
                "pages": "S1-S65",
                "pmid": "22786448",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "guideline",
                "title": "World Health Organization Guidelines for the Pharmacological and Radiotherapeutic Management of Cancer Pain in Adults and Adolescents",
                "authors": "World Health Organization",
                "journal": "WHO Guidelines",
                "year": 2018,
                "url": "https://www.who.int/publications/i/item/9789241550390",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            }
        ],

        "RA Flare": [
            {
                "type": "guideline",
                "title": "2015 American College of Rheumatology Guideline for the Treatment of Rheumatoid Arthritis",
                "authors": "Singh JA, Saag KG, Bridges SL Jr, et al.",
                "journal": "Arthritis & Rheumatology",
                "year": 2016,
                "volume": "68",
                "issue": "1",
                "pages": "1-26",
                "doi": "10.1002/art.39480",
                "pmid": "26545940",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "guideline",
                "title": "EULAR recommendations for the management of rheumatoid arthritis with synthetic and biological disease-modifying antirheumatic drugs: 2022 update",
                "authors": "Smolen JS, Landewé RBM, Bergstra SA, et al.",
                "journal": "Annals of the Rheumatic Diseases",
                "year": 2023,
                "volume": "82",
                "issue": "1",
                "pages": "3-18",
                "doi": "10.1136/ard-2022-223356",
                "pmid": "36270658",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "primary",
                "title": "Management of rheumatoid arthritis flares",
                "authors": "Caporali R, Scirè CA",
                "journal": "Clinical and Experimental Rheumatology",
                "year": 2019,
                "volume": "37",
                "issue": "5 Suppl 121",
                "pages": "S137-S141",
                "pmid": "31621563",
                "evidence_level": EVIDENCE_LEVEL_IIA,
                "strength": STRENGTH_MODERATE
            }
        ],

        "Acute Gout": [
            {
                "type": "guideline",
                "title": "2012 American College of Rheumatology Guidelines for Management of Gout. Part 2: Therapy and Antiinflammatory Prophylaxis of Acute Gouty Arthritis",
                "authors": "Khanna D, Fitzgerald JD, Khanna PP, et al.",
                "journal": "Arthritis Care & Research",
                "year": 2012,
                "volume": "64",
                "issue": "10",
                "pages": "1447-1461",
                "doi": "10.1002/acr.21773",
                "pmid": "23024029",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            }
        ],

        "TLS": [
            {
                "type": "guideline",
                "title": "Guidelines for the Management of Tumor Lysis Syndrome in Adults and Children with Malignancy",
                "authors": "Cairo MS, Coiffier B, Reiter A, Younes A",
                "journal": "Clinical Lymphoma, Myeloma & Leukemia",
                "year": 2010,
                "volume": "10",
                "issue": "Suppl 1",
                "pages": "S2-S9",
                "doi": "10.3816/CLML.2010.s.001",
                "pmid": "20630878",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "guideline",
                "title": "Tumor Lysis Syndrome: A Systematic Review of Case Series and Case Reports",
                "authors": "Wilson FP, Berns JS",
                "journal": "Oncology",
                "year": 2012,
                "volume": "26",
                "issue": "12",
                "pages": "1142-1147",
                "pmid": "23268260",
                "evidence_level": EVIDENCE_LEVEL_IIA,
                "strength": STRENGTH_MODERATE
            },
            {
                "type": "primary",
                "title": "Tumor lysis syndrome: current therapeutic strategy and management",
                "authors": "Cairo MS, Bishop M",
                "journal": "The Lancet Oncology",
                "year": 2004,
                "volume": "5",
                "issue": "11",
                "pages": "684-692",
                "doi": "10.1016/S1470-2045(04)01609-5",
                "pmid": "15522661",
                "evidence_level": EVIDENCE_LEVEL_IIA,
                "strength": STRENGTH_STRONG
            }
        ],

        "Alcohol Withdrawal": [
            {
                "type": "guideline",
                "title": "The ASAM Clinical Practice Guideline on Alcohol Withdrawal Management",
                "authors": "American Society of Addiction Medicine",
                "journal": "Journal of Addiction Medicine",
                "year": 2020,
                "volume": "14",
                "issue": "3S Suppl 1",
                "pages": "1-72",
                "doi": "10.1097/ADM.0000000000000668",
                "pmid": "32511109",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "guideline",
                "title": "Management of alcohol withdrawal delirium. An evidence-based practice guideline",
                "authors": "Mayo-Smith MF",
                "journal": "Archives of Internal Medicine",
                "year": 2004,
                "volume": "164",
                "issue": "13",
                "pages": "1405-1412",
                "doi": "10.1001/archinte.164.13.1405",
                "pmid": "15249349",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            }
        ],

        "Eclampsia": [
            {
                "type": "guideline",
                "title": "ACOG Practice Bulletin No. 222: Gestational Hypertension and Preeclampsia",
                "authors": "American College of Obstetricians and Gynecologists",
                "journal": "Obstetrics & Gynecology",
                "year": 2020,
                "volume": "135",
                "issue": "6",
                "pages": "e237-e260",
                "doi": "10.1097/AOG.0000000000003891",
                "pmid": "32443079",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "guideline",
                "title": "WHO Recommendations for Prevention and Treatment of Pre-eclampsia and Eclampsia",
                "authors": "World Health Organization",
                "journal": "WHO Guidelines",
                "year": 2011,
                "url": "https://www.who.int/publications/i/item/9789241548335",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "review",
                "title": "Eclampsia: a neurological perspective",
                "authors": "Cipolla MJ",
                "journal": "Journal of the Neurological Sciences",
                "year": 2008,
                "volume": "271",
                "issue": "1-2",
                "pages": "158-167",
                "doi": "10.1016/j.jns.2008.03.027",
                "pmid": "18479717",
                "evidence_level": EVIDENCE_LEVEL_IIA,
                "strength": STRENGTH_MODERATE
            }
        ],

        "Postpartum Hemorrhage": [
            {
                "type": "guideline",
                "title": "ACOG Practice Bulletin No. 183: Postpartum Hemorrhage",
                "authors": "American College of Obstetricians and Gynecologists",
                "journal": "Obstetrics & Gynecology",
                "year": 2017,
                "volume": "130",
                "issue": "4",
                "pages": "e168-e186",
                "doi": "10.1097/AOG.0000000000002351",
                "pmid": "28937571",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "guideline",
                "title": "WHO Recommendations for the Prevention and Treatment of Postpartum Haemorrhage",
                "authors": "World Health Organization",
                "journal": "WHO Guidelines",
                "year": 2012,
                "url": "https://www.who.int/publications/i/item/9789241548552",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "review",
                "title": "Postpartum hemorrhage: prevention and treatment",
                "authors": "Mousa HA, Blum J, Abou El Senoun G, Shakur H, Alfirevic Z",
                "journal": "American Journal of Obstetrics and Gynecology",
                "year": 2015,
                "volume": "212",
                "issue": "6",
                "pages": "795-807",
                "doi": "10.1016/j.ajog.2015.01.024",
                "pmid": "25637840",
                "evidence_level": EVIDENCE_LEVEL_IIA,
                "strength": STRENGTH_STRONG
            }
        ],

        "Stevens-Johnson Syndrome": [
            {
                "type": "primary",
                "title": "SCORTEN: a severity-of-illness score for toxic epidermal necrolysis",
                "authors": "Bastuji-Garin S, Fouchard N, Bertocchi M, Roujeau JC, Revuz J, Wolkenstein P",
                "journal": "Journal of Investigative Dermatology",
                "year": 2000,
                "volume": "115",
                "issue": "2",
                "pages": "149-153",
                "doi": "10.1046/j.1523-1747.2000.00061.x",
                "pmid": "10951229",
                "evidence_level": EVIDENCE_LEVEL_IIA,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "review",
                "title": "Stevens-Johnson Syndrome and Toxic Epidermal Necrolysis: A Concise Review with a Comprehensive Summary of Therapeutic Interventions Emphasizing Supportive Measures",
                "authors": "Schneider JA, Cohen PR",
                "journal": "Advances in Therapy",
                "year": 2017,
                "volume": "34",
                "issue": "6",
                "pages": "1235-1244",
                "doi": "10.1007/s12325-017-0530-y",
                "pmid": "28526982",
                "evidence_level": EVIDENCE_LEVEL_IIA,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "guideline",
                "title": "Toxic epidermal necrolysis and Stevens-Johnson syndrome",
                "authors": "Harr T, French LE",
                "journal": "Orphanet Journal of Rare Diseases",
                "year": 2010,
                "volume": "5",
                "pages": "39",
                "doi": "10.1186/1750-1172-5-39",
                "pmid": "21162721",
                "evidence_level": EVIDENCE_LEVEL_IIA,
                "strength": STRENGTH_MODERATE
            }
        ],

}
