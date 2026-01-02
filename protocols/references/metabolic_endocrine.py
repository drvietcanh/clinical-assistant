"""
Protocol References - Metabolic Endocrine
"""
from typing import List, Dict, Any
from components.references import (
    GRADE_HIGH, GRADE_MODERATE, GRADE_LOW,
    EVIDENCE_LEVEL_I, EVIDENCE_LEVEL_IIA, EVIDENCE_LEVEL_IIB,
    STRENGTH_STRONG, STRENGTH_MODERATE
)


METABOLIC_ENDOCRINE_REFERENCES: Dict[str, List[Dict[str, Any]]] = {
        "DKA": [
            {
                "type": "guideline",
                "title": "Hyperglycemic Crises in Adult Patients With Diabetes",
                "authors": "Kitabchi AE, Umpierrez GE, Miles JM, Fisher JN",
                "journal": "Diabetes Care",
                "year": 2009,
                "volume": "32",
                "issue": "7",
                "pages": "1335-1343",
                "doi": "10.2337/dc09-9032",
                "pmid": "19564476",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "guideline",
                "title": "Standards of Medical Care in Diabetes—2023",
                "authors": "American Diabetes Association",
                "journal": "Diabetes Care",
                "year": 2023,
                "volume": "46",
                "issue": "Supplement_1",
                "pages": "S1-S291",
                "doi": "10.2337/dc23-Sint",
                "pmid": "36507649",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            }
        ],

        "Hyperkalemia": [
            {
                "type": "guideline",
                "title": "KDIGO Clinical Practice Guideline for Acute Kidney Injury",
                "authors": "KDIGO Work Group",
                "journal": "Kidney International Supplements",
                "year": 2012,
                "volume": "2",
                "issue": "1",
                "pages": "1-138",
                "doi": "10.1038/kisup.2012.1",
                "pmid": "25018998",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "primary",
                "title": "Treatment and prevention of hyperkalemia in adults",
                "authors": "Mount DB",
                "journal": "UpToDate",
                "year": 2023,
                "url": "https://www.uptodate.com/contents/treatment-and-prevention-of-hyperkalemia-in-adults",
                "evidence_level": EVIDENCE_LEVEL_IIA,
                "strength": STRENGTH_STRONG
            }
        ],

        "Hyponatremia": [
            {
                "type": "guideline",
                "title": "Clinical practice guideline on diagnosis and treatment of hyponatraemia",
                "authors": "Spasovski G, Vanholder R, Allolio B, et al.",
                "journal": "European Journal of Endocrinology",
                "year": 2014,
                "volume": "170",
                "issue": "3",
                "pages": "G1-G47",
                "doi": "10.1530/EJE-13-1020",
                "pmid": "24569125",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            }
        ],

        "Thyrotoxic Crisis": [
            {
                "type": "guideline",
                "title": "2016 American Thyroid Association Guidelines for Diagnosis and Management of Hyperthyroidism and Other Causes of Thyrotoxicosis",
                "authors": "Ross DS, Burch HB, Cooper DS, et al.",
                "journal": "Thyroid",
                "year": 2016,
                "volume": "26",
                "issue": "10",
                "pages": "1343-1421",
                "doi": "10.1089/thy.2016.0229",
                "pmid": "27521067",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            }
        ],

        "Hypercalcemia": [
            {
                "type": "guideline",
                "title": "Management of Hypercalcemia of Malignancy in Adults",
                "authors": "Stewart AF",
                "journal": "UpToDate",
                "year": 2023,
                "url": "https://www.uptodate.com/contents/management-of-hypercalcemia-of-malignancy-in-adults",
                "evidence_level": EVIDENCE_LEVEL_IIA,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "guideline",
                "title": "Hypercalcemia of malignancy: an update on pathogenesis and management",
                "authors": "Clines GA, Guise TA",
                "journal": "North American Journal of Medical Sciences",
                "year": 2005,
                "volume": "2",
                "issue": "11",
                "pages": "691-699",
                "doi": "10.1097/01.naj.0000171889.27512.7f",
                "pmid": "16301708",
                "evidence_level": EVIDENCE_LEVEL_IIA,
                "strength": STRENGTH_MODERATE
            },
            {
                "type": "primary",
                "title": "Emergency treatment of hypercalcemia",
                "authors": "LeGrand SB, Leskuski D, Zama I",
                "journal": "Emergency Medicine Clinics of North America",
                "year": 2011,
                "volume": "29",
                "issue": "4",
                "pages": "797-807",
                "doi": "10.1016/j.emc.2011.08.007",
                "pmid": "22040707",
                "evidence_level": EVIDENCE_LEVEL_IIA,
                "strength": STRENGTH_MODERATE
            }
        ],

        "Adrenal Crisis": [
            {
                "type": "guideline",
                "title": "Diagnosis and Treatment of Primary Adrenal Insufficiency: An Endocrine Society Clinical Practice Guideline",
                "authors": "Bornstein SR, Allolio B, Arlt W, et al.",
                "journal": "Journal of Clinical Endocrinology & Metabolism",
                "year": 2016,
                "volume": "101",
                "issue": "2",
                "pages": "364-389",
                "doi": "10.1210/jc.2015-1710",
                "pmid": "26760044",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "primary",
                "title": "Adrenal crisis",
                "authors": "Rushworth RL, Torpy DJ, Falhammar H",
                "journal": "The Lancet",
                "year": 2019,
                "volume": "393",
                "issue": "10177",
                "pages": "1655-1667",
                "doi": "10.1016/S0140-6736(19)30324-4",
                "pmid": "30995948",
                "evidence_level": EVIDENCE_LEVEL_IIA,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "review",
                "title": "Treatment of adrenal insufficiency: current approaches and future prospects",
                "authors": "Hahner S, Spinnler C, Fassnacht M, et al.",
                "journal": "Clinical Endocrinology",
                "year": 2014,
                "volume": "81",
                "issue": "2",
                "pages": "199-207",
                "doi": "10.1111/cen.12429",
                "pmid": "24766213",
                "evidence_level": EVIDENCE_LEVEL_IIA,
                "strength": STRENGTH_MODERATE
            }
        ],

        "Hypocalcemia": [
            {
                "type": "guideline",
                "title": "Clinical practice guidelines for hypocalcemia: systematic review and meta-analysis",
                "authors": "Cooper MS, Gittoes NJ",
                "journal": "Clinical Endocrinology",
                "year": 2008,
                "volume": "68",
                "issue": "4",
                "pages": "503-511",
                "doi": "10.1111/j.1365-2265.2007.03066.x",
                "pmid": "18070146",
                "evidence_level": EVIDENCE_LEVEL_IIA,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "primary",
                "title": "Treatment of hypocalcemia",
                "authors": "Shoback D",
                "journal": "UpToDate",
                "year": 2023,
                "url": "https://www.uptodate.com/contents/treatment-of-hypocalcemia",
                "evidence_level": EVIDENCE_LEVEL_IIA,
                "strength": STRENGTH_STRONG
            }
        ],

        "Hypomagnesemia": [
            {
                "type": "primary",
                "title": "Hypomagnesemia: clinical manifestations of magnesium depletion",
                "authors": "Swaminathan R",
                "journal": "UpToDate",
                "year": 2023,
                "url": "https://www.uptodate.com/contents/hypomagnesemia-clinical-manifestations-of-magnesium-depletion",
                "evidence_level": EVIDENCE_LEVEL_IIA,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "review",
                "title": "Magnesium metabolism and its disorders",
                "authors": "Swaminathan R",
                "journal": "Clinical Biochemistry Reviews",
                "year": 2003,
                "volume": "24",
                "issue": "2",
                "pages": "47-66",
                "pmid": "18568054",
                "evidence_level": EVIDENCE_LEVEL_IIA,
                "strength": STRENGTH_MODERATE
            }
        ],

        "Hypophosphatemia": [
            {
                "type": "primary",
                "title": "Hypophosphatemia: clinical manifestations of phosphate depletion",
                "authors": "Gaasbeek A, Meinders AE",
                "journal": "UpToDate",
                "year": 2023,
                "url": "https://www.uptodate.com/contents/hypophosphatemia-clinical-manifestations-of-phosphate-depletion",
                "evidence_level": EVIDENCE_LEVEL_IIA,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "review",
                "title": "Hypophosphatemia: an evidence-based approach to its clinical consequences and management",
                "authors": "Gaasbeek A, Meinders AE",
                "journal": "Nature Clinical Practice Nephrology",
                "year": 2007,
                "volume": "3",
                "issue": "3",
                "pages": "136-153",
                "doi": "10.1038/ncpneph0404",
                "pmid": "17322926",
                "evidence_level": EVIDENCE_LEVEL_IIA,
                "strength": STRENGTH_MODERATE
            }
        ],

        "HHS": [
            {
                "type": "guideline",
                "title": "Hyperglycemic Crises in Adult Patients With Diabetes",
                "authors": "Kitabchi AE, Umpierrez GE, Miles JM, Fisher JN",
                "journal": "Diabetes Care",
                "year": 2009,
                "volume": "32",
                "issue": "7",
                "pages": "1335-1343",
                "doi": "10.2337/dc09-9032",
                "pmid": "19564476",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "guideline",
                "title": "Standards of Medical Care in Diabetes—2023",
                "authors": "American Diabetes Association",
                "journal": "Diabetes Care",
                "year": 2023,
                "volume": "46",
                "issue": "Supplement_1",
                "pages": "S1-S291",
                "doi": "10.2337/dc23-Sint",
                "pmid": "36507649",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            }
        ],

        "Myxedema Coma": [
            {
                "type": "guideline",
                "title": "2014 Guidelines of the American Thyroid Association for the diagnosis and management of thyroid disease during pregnancy and the postpartum",
                "authors": "Stagnaro-Green A, Abalovich M, Alexander E, et al.",
                "journal": "Thyroid",
                "year": 2011,
                "volume": "21",
                "issue": "10",
                "pages": "1081-1125",
                "doi": "10.1089/thy.2011.0087",
                "pmid": "21787128",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "review",
                "title": "Myxedema coma: diagnosis and treatment",
                "authors": "Wartofsky L",
                "journal": "American Family Physician",
                "year": 2000,
                "volume": "62",
                "issue": "11",
                "pages": "2485-2490",
                "pmid": "11130234",
                "evidence_level": EVIDENCE_LEVEL_IIA,
                "strength": STRENGTH_MODERATE
            },
            {
                "type": "primary",
                "title": "Myxedema coma",
                "authors": "Wiersinga WM",
                "journal": "Journal of Intensive Care Medicine",
                "year": 2016,
                "volume": "31",
                "issue": "3",
                "pages": "200-212",
                "doi": "10.1177/0885066614564063",
                "pmid": "25540974",
                "evidence_level": EVIDENCE_LEVEL_IIA,
                "strength": STRENGTH_MODERATE
            }
        ],

        "Hypoglycemia": [
            {
                "type": "guideline",
                "title": "Standards of Medical Care in Diabetes—2024",
                "authors": "American Diabetes Association",
                "journal": "Diabetes Care",
                "year": 2024,
                "volume": "47",
                "issue": "Supplement_1",
                "pages": "S1-S307",
                "doi": "10.2337/dc24-Sint",
                "pmid": "38078579",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "guideline",
                "title": "Management of Hypoglycemia in Adults",
                "authors": "Cryer PE, Axelrod L, Grossman AB, et al.",
                "journal": "Endocrine Practice",
                "year": 2009,
                "volume": "15",
                "issue": "5",
                "pages": "536-544",
                "doi": "10.4158/EP09108.RA",
                "pmid": "19632945",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "review",
                "title": "Hypoglycemia in diabetes",
                "authors": "Cryer PE",
                "journal": "Diabetes Care",
                "year": 2013,
                "volume": "36",
                "issue": "5",
                "pages": "1384-1395",
                "doi": "10.2337/dc12-2482",
                "pmid": "23613542",
                "evidence_level": EVIDENCE_LEVEL_IIA,
                "strength": STRENGTH_STRONG
            }
        ],

}
