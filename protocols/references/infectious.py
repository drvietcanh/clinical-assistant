"""
Protocol References - Infectious
"""
from typing import List, Dict, Any
from components.references import (
    GRADE_HIGH, GRADE_MODERATE, GRADE_LOW,
    EVIDENCE_LEVEL_I, EVIDENCE_LEVEL_IIA, EVIDENCE_LEVEL_IIB,
    STRENGTH_STRONG, STRENGTH_MODERATE
)


INFECTIOUS_REFERENCES: Dict[str, List[Dict[str, Any]]] = {
        "CAP": [
            {
                "type": "guideline",
                "title": "Diagnosis and Treatment of Adults with Community-acquired Pneumonia. An Official Clinical Practice Guideline of the American Thoracic Society and Infectious Diseases Society of America",
                "authors": "Metlay JP, Waterer GW, Long AC, et al.",
                "journal": "American Journal of Respiratory and Critical Care Medicine",
                "year": 2019,
                "volume": "200",
                "issue": "7",
                "pages": "e45-e67",
                "doi": "10.1164/rccm.201908-1581ST",
                "pmid": "31573350",
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

        "HAP/VAP": [
            {
                "type": "guideline",
                "title": "Management of Adults With Hospital-acquired and Ventilator-associated Pneumonia: 2016 Clinical Practice Guidelines by the Infectious Diseases Society of America and the American Thoracic Society",
                "authors": "Kalli AC, Metersky ML, Klompas M, et al.",
                "journal": "Clinical Infectious Diseases",
                "year": 2016,
                "volume": "63",
                "issue": "5",
                "pages": "e61-e111",
                "doi": "10.1093/cid/ciw353",
                "pmid": "27418577",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            }
        ],

        "Meningitis": [
            {
                "type": "guideline",
                "title": "Clinical practice guidelines for the management of bacterial meningitis",
                "authors": "Tunkel AR, Hartman BJ, Kaplan SL, et al.",
                "journal": "Clinical Infectious Diseases",
                "year": 2004,
                "volume": "39",
                "issue": "9",
                "pages": "1267-1284",
                "doi": "10.1086/425368",
                "pmid": "15494903",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "guideline",
                "title": "IDSA Practice Guidelines for Bacterial Meningitis",
                "authors": "Tunkel AR, Hasbun R, Bhimraj A, et al.",
                "journal": "Clinical Infectious Diseases",
                "year": 2017,
                "volume": "65",
                "issue": "10",
                "pages": "e1-e94",
                "doi": "10.1093/cid/cix319",
                "pmid": "28522569",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            }
        ],

        "Severe Influenza": [
            {
                "type": "guideline",
                "title": "Clinical Practice Guidelines by the Infectious Diseases Society of America: 2018 Update on Diagnosis, Treatment, Chemoprophylaxis, and Institutional Outbreak Management of Seasonal Influenza",
                "authors": "Uyeki TM, Bernstein HH, Bradley JS, et al.",
                "journal": "Clinical Infectious Diseases",
                "year": 2019,
                "volume": "68",
                "issue": "6",
                "pages": "e1-e47",
                "doi": "10.1093/cid/ciy866",
                "pmid": "30566567",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "guideline",
                "title": "Clinical management of seasonal influenza, interim guidance",
                "authors": "World Health Organization",
                "journal": "WHO Publication",
                "year": 2024,
                "url": "https://www.who.int/publications/i/item/WHO-2019-nCoV-clinical-2024",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            }
        ],

        "Pulmonary TB": [
            {
                "type": "guideline",
                "title": "WHO consolidated guidelines on tuberculosis: module 4: treatment - 2024 update",
                "authors": "World Health Organization",
                "journal": "WHO Publication",
                "year": 2024,
                "url": "https://www.who.int/publications/i/item/9789240094239",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "guideline",
                "title": "WHO operational handbook on tuberculosis: module 4: treatment - 2023 update",
                "authors": "World Health Organization",
                "journal": "WHO Publication",
                "year": 2023,
                "url": "https://www.who.int/publications/i/item/9789240061729",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            }
        ],

        "Febrile Neutropenia": [
            {
                "type": "guideline",
                "title": "Clinical Practice Guideline for the Use of Antimicrobial Agents in Neutropenic Patients with Cancer: 2010 Update by the Infectious Diseases Society of America",
                "authors": "Freifeld AG, Bow EJ, Sepkowitz KA, et al.",
                "journal": "Clinical Infectious Diseases",
                "year": 2011,
                "volume": "52",
                "issue": "4",
                "pages": "e56-e93",
                "doi": "10.1093/cid/cir073",
                "pmid": "21258094",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            }
        ],

        "C. diff": [
            {
                "type": "guideline",
                "title": "Clinical Practice Guidelines for Clostridium difficile Infection in Adults and Children: 2017 Update by the Infectious Diseases Society of America (IDSA) and Society for Healthcare Epidemiology of America (SHEA)",
                "authors": "McDonald LC, Gerding DN, Johnson S, et al.",
                "journal": "Clinical Infectious Diseases",
                "year": 2018,
                "volume": "66",
                "issue": "7",
                "pages": "e1-e48",
                "doi": "10.1093/cid/cix1085",
                "pmid": "29462280",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "guideline",
                "title": "European Society of Clinical Microbiology and Infectious Diseases: 2021 update on the treatment guidance document for Clostridioides difficile infection in adults",
                "authors": "van Prehn J, Reigadas E, Vogelzang EH, et al.",
                "journal": "Clinical Microbiology and Infection",
                "year": 2021,
                "volume": "27",
                "issue": "Suppl 2",
                "pages": "S1-S21",
                "doi": "10.1016/j.cmi.2021.09.038",
                "pmid": "34678455",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "primary",
                "title": "Clostridium difficile infection",
                "authors": "Leffler DA, Lamont JT",
                "journal": "New England Journal of Medicine",
                "year": 2015,
                "volume": "372",
                "issue": "16",
                "pages": "1539-1548",
                "doi": "10.1056/NEJMra1403772",
                "pmid": "25875259",
                "evidence_level": EVIDENCE_LEVEL_IIA,
                "strength": STRENGTH_STRONG
            }
        ],

        "Infective Endocarditis": [
            {
                "type": "guideline",
                "title": "2015 ESC Guidelines for the management of infective endocarditis",
                "authors": "Habib G, Lancellotti P, Antunes MJ, et al.",
                "journal": "European Heart Journal",
                "year": 2015,
                "volume": "36",
                "issue": "44",
                "pages": "3075-3128",
                "doi": "10.1093/eurheartj/ehv319",
                "pmid": "26320109",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "guideline",
                "title": "Infective Endocarditis in Adults: Diagnosis, Antimicrobial Therapy, and Management of Complications",
                "authors": "Baddour LM, Wilson WR, Bayer AS, et al.",
                "journal": "Circulation",
                "year": 2015,
                "volume": "132",
                "issue": "15",
                "pages": "1435-1486",
                "doi": "10.1161/CIR.0000000000000296",
                "pmid": "26373316",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "guideline",
                "title": "Prevention of Infective Endocarditis: Guidelines from the American Heart Association",
                "authors": "Wilson W, Taubert KA, Gewitz M, et al.",
                "journal": "Circulation",
                "year": 2007,
                "volume": "116",
                "issue": "15",
                "pages": "1736-1754",
                "doi": "10.1161/CIRCULATIONAHA.106.183095",
                "pmid": "17446442",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            }
        ],

        "Hepatitis B": [
            {
                "type": "guideline",
                "title": "AASLD 2018 Hepatitis B Guidance: Update on prevention, diagnosis, and treatment of chronic hepatitis B",
                "authors": "Terrault NA, Lok ASF, McMahon BJ, et al.",
                "journal": "Hepatology",
                "year": 2018,
                "volume": "67",
                "issue": "4",
                "pages": "1560-1599",
                "doi": "10.1002/hep.29800",
                "pmid": "29405329",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG,
                "url": "https://aasldpubs.onlinelibrary.wiley.com/doi/full/10.1002/hep.29800"
            },
            {
                "type": "guideline",
                "title": "EASL 2017 Clinical Practice Guidelines on the management of hepatitis B virus infection",
                "authors": "European Association for the Study of the Liver",
                "journal": "Journal of Hepatology",
                "year": 2017,
                "volume": "67",
                "issue": "2",
                "pages": "370-398",
                "doi": "10.1016/j.jhep.2017.03.021",
                "pmid": "28427875",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "guideline",
                "title": "WHO Guidelines for the prevention, care and treatment of persons with chronic hepatitis B infection",
                "authors": "World Health Organization",
                "journal": "WHO Guidelines",
                "year": 2021,
                "url": "https://www.who.int/publications/i/item/9789240027077",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "review",
                "title": "Hepatitis B virus: Overview of management",
                "authors": "Lok ASF, McMahon BJ",
                "journal": "UpToDate",
                "year": 2024,
                "evidence_level": EVIDENCE_LEVEL_IIA,
                "strength": STRENGTH_MODERATE
            }
        ],

        "Hepatitis C": [
            {
                "type": "guideline",
                "title": "HCV Guidance: Recommendations for Testing, Managing, and Treating Hepatitis C",
                "authors": "AASLD/IDSA HCV Guidance Panel",
                "journal": "Hepatology",
                "year": 2023,
                "url": "https://www.hcvguidelines.org",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "guideline",
                "title": "EASL Recommendations on Treatment of Hepatitis C",
                "authors": "European Association for the Study of the Liver",
                "journal": "Journal of Hepatology",
                "year": 2023,
                "volume": "79",
                "issue": "2",
                "pages": "214-239",
                "doi": "10.1016/j.jhep.2023.05.007",
                "pmid": "37562533",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "guideline",
                "title": "WHO Guidelines for the care and treatment of persons diagnosed with chronic hepatitis C virus infection",
                "authors": "World Health Organization",
                "journal": "WHO Guidelines",
                "year": 2022,
                "url": "https://www.who.int/publications/i/item/9789240051662",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "review",
                "title": "Treatment of chronic hepatitis C virus infection",
                "authors": "Lok ASF, Terrault NA",
                "journal": "UpToDate",
                "year": 2024,
                "evidence_level": EVIDENCE_LEVEL_IIA,
                "strength": STRENGTH_MODERATE
            }
        ],

        "Acute Hepatitis": [
            {
                "type": "guideline",
                "title": "AASLD Position Paper: The diagnosis and management of non-alcoholic fatty liver disease",
                "authors": "Chalasani N, Younossi Z, Lavine JE, et al.",
                "journal": "Hepatology",
                "year": 2018,
                "volume": "67",
                "issue": "1",
                "pages": "328-357",
                "doi": "10.1002/hep.29367",
                "pmid": "28714183",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "guideline",
                "title": "EASL Clinical Practice Guidelines: Drug-induced liver injury",
                "authors": "European Association for the Study of the Liver",
                "journal": "Journal of Hepatology",
                "year": 2019,
                "volume": "70",
                "issue": "6",
                "pages": "1222-1261",
                "doi": "10.1016/j.jhep.2019.02.014",
                "pmid": "30926241",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "guideline",
                "title": "AASLD Practice Guidelines: Diagnosis and management of autoimmune hepatitis",
                "authors": "Manns MP, Czaja AJ, Gorham JD, et al.",
                "journal": "Hepatology",
                "year": 2010,
                "volume": "51",
                "issue": "6",
                "pages": "2193-2213",
                "doi": "10.1002/hep.23584",
                "pmid": "20513004",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "review",
                "title": "Drug-induced liver injury",
                "authors": "Björnsson ES",
                "journal": "Nature Reviews Disease Primers",
                "year": 2019,
                "volume": "5",
                "pages": "58",
                "doi": "10.1038/s41572-019-0105-0",
                "pmid": "31420555",
                "evidence_level": EVIDENCE_LEVEL_IIA,
                "strength": STRENGTH_STRONG
            }
        ],

        "dengue_fever": [
            {
                "type": "guideline",
                "title": "Dengue: Guidelines for diagnosis, treatment, prevention and control",
                "authors": "WHO",
                "journal": "World Health Organization",
                "year": 2009,
                "url": "https://www.who.int/publications/i/item/9789241547871",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "guideline",
                "title": "Handbook for Clinical Management of Dengue",
                "authors": "WHO",
                "journal": "World Health Organization",
                "year": 2012,
                "url": "https://www.who.int/publications/i/item/9789241504713",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "guideline",
                "title": "Hướng dẫn chẩn đoán và điều trị sốt xuất huyết Dengue",
                "authors": "Bộ Y tế Việt Nam",
                "journal": "Quyết định 3705/QĐ-BYT",
                "year": 2019,
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            }
        ],

}
