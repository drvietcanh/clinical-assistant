"""
References Configuration for All Protocols
Contains PubMed links, guidelines, and evidence grading for each protocol
"""

from typing import List, Dict, Any
from components.references import (
    GRADE_HIGH, GRADE_MODERATE, GRADE_LOW,
    EVIDENCE_LEVEL_I, EVIDENCE_LEVEL_IIA, EVIDENCE_LEVEL_IIB,
    STRENGTH_STRONG, STRENGTH_MODERATE
)

# References database organized by protocol name
PROTOCOL_REFERENCES: Dict[str, List[Dict[str, Any]]] = {
    "Sepsis": [
        {
            "type": "guideline",
            "title": "Surviving Sepsis Campaign: International Guidelines for Management of Sepsis and Septic Shock 2021",
            "authors": "Evans L, Rhodes A, Alhazzani W, et al.",
            "journal": "Critical Care Medicine",
            "year": 2021,
            "volume": "49",
            "issue": "11",
            "pages": "e1063-e1143",
            "doi": "10.1097/CCM.0000000000005337",
            "pmid": "34605781",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG,
            "url": "https://www.sccm.org/SurvivingSepsisCampaign"
        },
        {
            "type": "guideline",
            "title": "The Third International Consensus Definitions for Sepsis and Septic Shock (Sepsis-3)",
            "authors": "Singer M, Deutschman CS, Seymour CW, et al.",
            "journal": "JAMA",
            "year": 2016,
            "volume": "315",
            "issue": "8",
            "pages": "801-810",
            "doi": "10.1001/jama.2016.0287",
            "pmid": "26903338",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "guideline",
            "title": "IDSA Clinical Practice Guidelines for the Management of Sepsis",
            "authors": "Rhodes A, Evans LE, Alhazzani W, et al.",
            "journal": "Clinical Infectious Diseases",
            "year": 2017,
            "volume": "65",
            "issue": "9",
            "pages": "e61-e111",
            "doi": "10.1093/cid/cix353",
            "pmid": "28922862",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "Sepsis 3-Hour": [
        {
            "type": "guideline",
            "title": "Surviving Sepsis Campaign: International Guidelines for Management of Sepsis and Septic Shock 2021",
            "authors": "Evans L, Rhodes A, Alhazzani W, et al.",
            "journal": "Critical Care Medicine",
            "year": 2021,
            "volume": "49",
            "issue": "11",
            "pages": "e1063-e1143",
            "doi": "10.1097/CCM.0000000000005337",
            "pmid": "34605781",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG,
            "url": "https://www.sccm.org/SurvivingSepsisCampaign"
        }
    ],
    
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
    
    "Shock": [
        {
            "type": "guideline",
            "title": "Surviving Sepsis Campaign: International Guidelines for Management of Sepsis and Septic Shock 2021",
            "authors": "Evans L, Rhodes A, Alhazzani W, et al.",
            "journal": "Critical Care Medicine",
            "year": 2021,
            "volume": "49",
            "issue": "11",
            "pages": "e1063-e1143",
            "doi": "10.1097/CCM.0000000000005337",
            "pmid": "34605781",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "primary",
            "title": "Shock: diagnosis and management",
            "authors": "Vincent JL, De Backer D",
            "journal": "Critical Care",
            "year": 2013,
            "volume": "17",
            "issue": "5",
            "pages": "239",
            "doi": "10.1186/cc12710",
            "pmid": "24093228",
            "evidence_level": EVIDENCE_LEVEL_IIA,
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
        }
    ],
    
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
    
    "AKI": [
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
            "type": "guideline",
            "title": "KDIGO 2012 Clinical Practice Guideline for the Evaluation and Management of Chronic Kidney Disease",
            "authors": "KDIGO 2012 Clinical Practice Guideline",
            "journal": "Kidney International Supplements",
            "year": 2013,
            "volume": "3",
            "issue": "1",
            "pages": "1-150",
            "doi": "10.1038/kisup.2012.73",
            "pmid": "25018998",
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
    
    "Anaphylaxis": [
        {
            "type": "guideline",
            "title": "Anaphylaxis—a 2020 practice parameter update, systematic review, and Grading of Recommendations, Assessment, Development and Evaluation (GRADE) analysis",
            "authors": "Shaker MS, Wallace DV, Golden DBK, et al.",
            "journal": "Journal of Allergy and Clinical Immunology",
            "year": 2020,
            "volume": "145",
            "issue": "4",
            "pages": "1082-1123",
            "doi": "10.1016/j.jaci.2020.01.017",
            "pmid": "32001253",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "guideline",
            "title": "World Allergy Organization Anaphylaxis Guidance 2020",
            "authors": "Cardona V, Ansotegui IJ, Ebisawa M, et al.",
            "journal": "World Allergy Organization Journal",
            "year": 2020,
            "volume": "13",
            "issue": "10",
            "pages": "100472",
            "doi": "10.1016/j.waojou.2020.100472",
            "pmid": "33024588",
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
        }
    ],
    
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
    
    "GI Bleeding": [
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
        },
        {
            "type": "guideline",
            "title": "ACG Clinical Guideline: Upper Gastrointestinal and Ulcer Bleeding",
            "authors": "Laine L, Barkun AN, Saltzman JR, et al.",
            "journal": "American Journal of Gastroenterology",
            "year": 2021,
            "volume": "116",
            "issue": "5",
            "pages": "899-917",
            "doi": "10.14309/ajg.0000000000001245",
            "pmid": "33929377",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "Acute Pancreatitis": [
        {
            "type": "guideline",
            "title": "American Gastroenterological Association Institute Guideline on Initial Management of Acute Pancreatitis",
            "authors": "Crockett SD, Wani S, Gardner TB, Falck-Ytter Y, Barkun AN",
            "journal": "Gastroenterology",
            "year": 2018,
            "volume": "154",
            "issue": "4",
            "pages": "1096-1101",
            "doi": "10.1053/j.gastro.2018.01.032",
            "pmid": "29409760",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "guideline",
            "title": "IAP/APA evidence-based guidelines for the management of acute pancreatitis",
            "authors": "Working Group IAP/APA Acute Pancreatitis Guidelines",
            "journal": "Pancreatology",
            "year": 2013,
            "volume": "13",
            "issue": "4 Suppl 2",
            "pages": "e1-e15",
            "doi": "10.1016/j.pan.2013.07.063",
            "pmid": "24054878",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "Acute Liver Failure": [
        {
            "type": "guideline",
            "title": "AASLD Position Paper: The Management of Acute Liver Failure",
            "authors": "Lee WM, Stravitz RT, Larson AM",
            "journal": "Hepatology",
            "year": 2012,
            "volume": "56",
            "issue": "3",
            "pages": "965-967",
            "doi": "10.1002/hep.25681",
            "pmid": "22535299",
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
    
    "Myxedema Coma": [
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
        }
    ],
    
    "Opioid Overdose": [
        {
            "type": "guideline",
            "title": "Management of Opioid Overdose",
            "authors": "World Health Organization",
            "journal": "WHO Guidelines",
            "year": 2014,
            "url": "https://www.who.int/publications/i/item/9789241548816",
            "evidence_level": EVIDENCE_LEVEL_I,
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
        }
    ],
    
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
    
    "IBD Exacerbation": [
        {
            "type": "guideline",
            "title": "ACG Clinical Guideline: Ulcerative Colitis in Adults",
            "authors": "Rubin DT, Ananthakrishnan AN, Siegel CA, Sauer BG, Long MD",
            "journal": "American Journal of Gastroenterology",
            "year": 2019,
            "volume": "114",
            "issue": "3",
            "pages": "384-413",
            "doi": "10.14309/ajg.0000000000000152",
            "pmid": "30840605",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
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
        }
    ],
    
    "Acute Liver Failure": [
        {
            "type": "guideline",
            "title": "AASLD Position Paper: The Management of Acute Liver Failure",
            "authors": "Lee WM, Stravitz RT, Larson AM",
            "journal": "Hepatology",
            "year": 2012,
            "volume": "56",
            "issue": "3",
            "pages": "965-967",
            "doi": "10.1002/hep.25681",
            "pmid": "22535299",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "guideline",
            "title": "EASL Clinical Practical Guidelines on the management of acute (fulminant) liver failure",
            "authors": "European Association for the Study of the Liver",
            "journal": "Journal of Hepatology",
            "year": 2017,
            "volume": "66",
            "issue": "5",
            "pages": "1047-1081",
            "doi": "10.1016/j.jhep.2016.12.003",
            "pmid": "28417882",
            "evidence_level": EVIDENCE_LEVEL_I,
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
    ]
}


def get_references(protocol_name: str) -> List[Dict[str, Any]]:
    """
    Get references for a specific protocol
    
    Args:
        protocol_name: Name of the protocol (e.g., "Sepsis", "ACS", "Stroke")
    
    Returns:
        List of reference dictionaries, empty list if not found
    """
    return PROTOCOL_REFERENCES.get(protocol_name, [])


def has_references(protocol_name: str) -> bool:
    """
    Check if a protocol has references
    
    Args:
        protocol_name: Name of the protocol
    
    Returns:
        True if references exist, False otherwise
    """
    return protocol_name in PROTOCOL_REFERENCES and len(PROTOCOL_REFERENCES[protocol_name]) > 0

