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

    "Malignant Arrhythmias": [
        {
            "type": "guideline",
            "title": "2020 AHA Guidelines for Cardiopulmonary Resuscitation and Emergency Cardiovascular Care",
            "authors": "Panchal AR, Bartos JA, Cabañas JG, et al.",
            "journal": "Circulation",
            "year": 2020,
            "volume": "142",
            "issue": "16_suppl_2",
            "pages": "S366-S468",
            "doi": "10.1161/CIR.0000000000000916",
            "pmid": "33081528",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "guideline",
            "title": "2022 ESC Guidelines for the management of patients with ventricular arrhythmias and the prevention of sudden cardiac death",
            "authors": "Zeppenfeld K, Tfelt-Hansen J, de Riva M, et al.",
            "journal": "European Heart Journal",
            "year": 2022,
            "volume": "43",
            "issue": "40",
            "pages": "3997-4126",
            "doi": "10.1093/eurheartj/ehac262",
            "pmid": "36121656",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],

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

    "Drowning": [
        {
            "type": "guideline",
            "title": "European Resuscitation Council Guidelines 2021: Cardiac arrest in special circumstances (drowning)",
            "authors": "Truhlář A, Deakin CD, Georgiou M, et al.",
            "journal": "Resuscitation",
            "year": 2021,
            "volume": "161",
            "pages": "152-219",
            "doi": "10.1016/j.resuscitation.2021.02.011",
            "pmid": "33773826",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "guideline",
            "title": "ILCOR Consensus on Science with Treatment Recommendations: Drowning",
            "authors": "Sempsrott J, Tipton M, Davids R, et al.",
            "journal": "Resuscitation",
            "year": 2020,
            "volume": "156",
            "pages": "A173-A184",
            "doi": "10.1016/j.resuscitation.2020.09.018",
            "pmid": "33007300",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],

    "Organophosphate Poisoning": [
        {
            "type": "guideline",
            "title": "Guidelines for the management of acute organophosphorus pesticide poisoning",
            "authors": "World Health Organization",
            "journal": "WHO Guidelines",
            "year": 2022,
            "url": "https://apps.who.int/iris/handle/10665/362786",
            "evidence_level": EVIDENCE_LEVEL_IIB,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "review",
            "title": "Management of acute organophosphorus pesticide poisoning",
            "authors": "Eddleston M, Dawson A, Karalliedde L, et al.",
            "journal": "The Lancet",
            "year": 2008,
            "volume": "371",
            "issue": "9612",
            "pages": "597-607",
            "doi": "10.1016/S0140-6736(07)61202-1",
            "pmid": "17706760",
            "evidence_level": EVIDENCE_LEVEL_IIB,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "primary",
            "title": "Pralidoxime in acute organophosphorus poisoning: a randomized controlled trial",
            "authors": "Eddleston M, Szinicz L, Eyer P, et al.",
            "journal": "PLoS Medicine",
            "year": 2009,
            "volume": "6",
            "issue": "6",
            "pages": "e1000104",
            "doi": "10.1371/journal.pmed.1000104",
            "pmid": "19564902",
            "evidence_level": EVIDENCE_LEVEL_IIB,
            "strength": STRENGTH_MODERATE
        }
    ],

    "Toxic Alcohol Poisoning": [
        {
            "type": "guideline",
            "title": "American Academy of Clinical Toxicology Practice Guidelines on the Treatment of Methanol and Ethylene Glycol Poisoning",
            "authors": "Barceloux DG, Bond GR, Krenzelok EP, Cooper H, Vale JA",
            "journal": "Clinical Toxicology",
            "year": 2002,
            "volume": "40",
            "issue": "4",
            "pages": "415-446",
            "doi": "10.1081/CLT-120006745",
            "pmid": "12216995",
            "evidence_level": EVIDENCE_LEVEL_IIB,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "guideline",
            "title": "EXTRIP Workgroup recommendations for methanol and ethylene glycol poisoning",
            "authors": "Salek T, Brown PA, Bouchard J, et al.",
            "journal": "American Journal of Kidney Diseases",
            "year": 2015,
            "volume": "66",
            "issue": "3",
            "pages": "583-590",
            "doi": "10.1053/j.ajkd.2015.05.009",
            "pmid": "26182737",
            "evidence_level": EVIDENCE_LEVEL_IIB,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "primary",
            "title": "Fomepizole for the treatment of ethylene glycol poisoning",
            "authors": "Brent J, McMartin K, Phillips S, et al.",
            "journal": "The New England Journal of Medicine",
            "year": 1999,
            "volume": "340",
            "issue": "11",
            "pages": "832-838",
            "doi": "10.1056/NEJM199903183401102",
            "pmid": "10080846",
            "evidence_level": EVIDENCE_LEVEL_IIB,
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
        },
        {
            "type": "guideline",
            "title": "American Heart Association Guidelines for Cardiopulmonary Resuscitation and Emergency Cardiovascular Care: Opioid-Associated Emergency",
            "authors": "Panchal AR, Bartos JA, Cabañas JG, et al.",
            "journal": "Circulation",
            "year": 2020,
            "volume": "142",
            "issue": "16_suppl_2",
            "pages": "S337-S357",
            "doi": "10.1161/CIR.0000000000000913",
            "pmid": "33081525",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "primary",
            "title": "Opioid overdose",
            "authors": "Rzasa Lynn R, Galinkin JL",
            "journal": "New England Journal of Medicine",
            "year": 2018,
            "volume": "378",
            "issue": "1",
            "pages": "54-63",
            "doi": "10.1056/NEJMra1604339",
            "pmid": "29298149",
            "evidence_level": EVIDENCE_LEVEL_IIA,
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
        },
        {
            "type": "guideline",
            "title": "ACG Clinical Guideline: Management of Crohn's Disease in Adults",
            "authors": "Lichtenstein GR, Loftus EV, Isaacs KL, Regueiro MD, Gerson LB, Sands BE",
            "journal": "American Journal of Gastroenterology",
            "year": 2018,
            "volume": "113",
            "issue": "4",
            "pages": "481-517",
            "doi": "10.1038/ajg.2018.27",
            "pmid": "29610508",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "guideline",
            "title": "ECCO Guidelines on Therapeutics in Ulcerative Colitis: Medical Treatment",
            "authors": "Harbord M, Eliakim R, Bettenworth D, et al.",
            "journal": "Journal of Crohn's and Colitis",
            "year": 2017,
            "volume": "11",
            "issue": "7",
            "pages": "769-784",
            "doi": "10.1093/ecco-jcc/jjx009",
            "pmid": "28158501",
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
    ],
    
    "Serotonin Syndrome": [
        {
            "type": "primary",
            "title": "Hunter Serotonin Toxicity Criteria: a simple and accurate diagnostic decision rule for serotonin toxicity",
            "authors": "Dunkley EJ, Isbister GK, Sibbritt D, Dawson AH, Whyte IM",
            "journal": "QJM",
            "year": 2003,
            "volume": "96",
            "issue": "9",
            "pages": "635-642",
            "doi": "10.1093/qjmed/hcg109",
            "pmid": "12925718",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "primary",
            "title": "The serotonin syndrome",
            "authors": "Sternbach H",
            "journal": "American Journal of Psychiatry",
            "year": 1991,
            "volume": "148",
            "issue": "6",
            "pages": "705-713",
            "doi": "10.1176/ajp.148.6.705",
            "pmid": "2035713",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "review",
            "title": "The serotonin syndrome",
            "authors": "Boyer EW, Shannon M",
            "journal": "New England Journal of Medicine",
            "year": 2005,
            "volume": "352",
            "issue": "11",
            "pages": "1112-1120",
            "doi": "10.1056/NEJMra041867",
            "pmid": "15784664",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "Neuroleptic Malignant Syndrome": [
        {
            "type": "primary",
            "title": "An international consensus study of neuroleptic malignant syndrome diagnostic criteria using the Delphi method",
            "authors": "Gurrera RJ, Caroff SN, Cohen A, et al.",
            "journal": "Journal of Clinical Psychiatry",
            "year": 2011,
            "volume": "72",
            "issue": "9",
            "pages": "1222-1228",
            "doi": "10.4088/JCP.10m06438",
            "pmid": "21208551",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "review",
            "title": "Neuroleptic malignant syndrome",
            "authors": "Strawn JR, Keck PE Jr, Caroff SN",
            "journal": "American Journal of Psychiatry",
            "year": 2007,
            "volume": "164",
            "issue": "6",
            "pages": "870-876",
            "doi": "10.1176/ajp.2007.164.6.870",
            "pmid": "17541044",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "primary",
            "title": "Neuroleptic malignant syndrome",
            "authors": "Bhanushali MJ, Tuite PJ",
            "journal": "The Neurohospitalist",
            "year": 2014,
            "volume": "4",
            "issue": "4",
            "pages": "223-229",
            "doi": "10.1177/1941874414546835",
            "pmid": "25360208",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_MODERATE
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
    
    "Bradycardia": [
        {
            "type": "guideline",
            "title": "2018 ACC/AHA/HRS Guideline on the Evaluation and Management of Patients With Bradycardia and Cardiac Conduction Delay",
            "authors": "Kusumoto FM, Schoenfeld MH, Barrett C, et al.",
            "journal": "Journal of the American College of Cardiology",
            "year": 2019,
            "volume": "74",
            "issue": "7",
            "pages": "e51-e156",
            "doi": "10.1016/j.jacc.2018.10.044",
            "pmid": "30412709",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "guideline",
            "title": "2021 ESC Guidelines on cardiac pacing and cardiac resynchronization therapy",
            "authors": "Glikson M, Nielsen JC, Kronborg MB, et al.",
            "journal": "European Heart Journal",
            "year": 2021,
            "volume": "42",
            "issue": "35",
            "pages": "3427-3520",
            "doi": "10.1093/eurheartj/ehab364",
            "pmid": "34455430",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "Tachycardia": [
        {
            "type": "guideline",
            "title": "2015 ACC/AHA/HRS Guideline for the Management of Adult Patients With Supraventricular Tachycardia",
            "authors": "Page RL, Joglar JA, Caldwell MA, et al.",
            "journal": "Journal of the American College of Cardiology",
            "year": 2016,
            "volume": "67",
            "issue": "13",
            "pages": "e27-e115",
            "doi": "10.1016/j.jacc.2015.08.856",
            "pmid": "26409259",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "guideline",
            "title": "2019 ESC Guidelines for the management of patients with supraventricular tachycardia",
            "authors": "Brugada J, Katritsis DG, Arbelo E, et al.",
            "journal": "European Heart Journal",
            "year": 2020,
            "volume": "41",
            "issue": "5",
            "pages": "655-720",
            "doi": "10.1093/eurheartj/ehz467",
            "pmid": "31504425",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
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
    
    "paracetamol_overdose": [
        {
            "type": "guideline",
            "title": "Acetaminophen poisoning: an evidence-based consensus guideline for out-of-hospital management",
            "authors": "Dart RC, Erdman AR, Olson KR, et al.",
            "journal": "Clinical Toxicology",
            "year": 2006,
            "volume": "44",
            "issue": "1",
            "pages": "1-18",
            "doi": "10.1080/15563650500394571",
            "pmid": "16496488",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "primary",
            "title": "Acetaminophen-induced acute liver failure: results of a United States multicenter, prospective study",
            "authors": "Larson AM, Polson J, Fontana RJ, et al.",
            "journal": "Hepatology",
            "year": 2005,
            "volume": "42",
            "issue": "6",
            "pages": "1364-1372",
            "doi": "10.1002/hep.20948",
            "pmid": "16317692",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "primary",
            "title": "Acetaminophen poisoning and toxicity",
            "authors": "Rumack BH, Matthew H",
            "journal": "Pediatrics",
            "year": 1975,
            "volume": "55",
            "issue": "6",
            "pages": "871-876",
            "pmid": "1134886",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "review",
            "title": "Acetaminophen (paracetamol) poisoning in adults: Pathophysiology, presentation, and diagnosis",
            "authors": "Hodgman MJ, Garrard AR",
            "journal": "UpToDate",
            "year": 2023,
            "url": "https://www.uptodate.com/contents/acetaminophen-paracetamol-poisoning-in-adults-pathophysiology-presentation-and-diagnosis",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "salicylate_overdose": [
        {
            "type": "guideline",
            "title": "Salicylate poisoning: an evidence-based consensus guideline for out-of-hospital management",
            "authors": "Dart RC, Erdman AR, Olson KR, et al.",
            "journal": "Clinical Toxicology",
            "year": 2007,
            "volume": "45",
            "issue": "2",
            "pages": "95-131",
            "doi": "10.1080/15563650600907140",
            "pmid": "17364628",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "primary",
            "title": "Salicylate poisoning",
            "authors": "Dargan PI, Wallace CI, Jones AL",
            "journal": "Postgraduate Medical Journal",
            "year": 2002,
            "volume": "78",
            "issue": "925",
            "pages": "505-506",
            "doi": "10.1136/pmj.78.925.505",
            "pmid": "12357010",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "review",
            "title": "Salicylate (aspirin) poisoning in adults",
            "authors": "Dargan PI, Wallace CI",
            "journal": "UpToDate",
            "year": 2023,
            "url": "https://www.uptodate.com/contents/salicylate-aspirin-poisoning-in-adults",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "carbon_monoxide_poisoning": [
        {
            "type": "guideline",
            "title": "Hyperbaric oxygen therapy for carbon monoxide poisoning",
            "authors": "Weaver LK",
            "journal": "Cochrane Database of Systematic Reviews",
            "year": 2014,
            "volume": "5",
            "pages": "CD002041",
            "doi": "10.1002/14651858.CD002041.pub3",
            "pmid": "24869765",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "primary",
            "title": "Hyperbaric oxygen for acute carbon monoxide poisoning",
            "authors": "Weaver LK, Hopkins RO, Chan KJ, et al.",
            "journal": "New England Journal of Medicine",
            "year": 2002,
            "volume": "347",
            "issue": "14",
            "pages": "1057-1067",
            "doi": "10.1056/NEJMoa013121",
            "pmid": "12362006",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "review",
            "title": "Carbon monoxide poisoning",
            "authors": "Rose JJ, Wang L, Xu Q, et al.",
            "journal": "New England Journal of Medicine",
            "year": 2017,
            "volume": "377",
            "issue": "6",
            "pages": "562-572",
            "doi": "10.1056/NEJMra1608024",
            "pmid": "28792865",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "guideline",
            "title": "Carbon monoxide poisoning",
            "authors": "Hampson NB",
            "journal": "Undersea & Hyperbaric Medicine",
            "year": 2019,
            "volume": "46",
            "issue": "5",
            "pages": "585-595",
            "pmid": "31683360",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "heat_stroke": [
        {
            "type": "guideline",
            "title": "Heat stroke",
            "authors": "Bouchama A, Knochel JP",
            "journal": "New England Journal of Medicine",
            "year": 2002,
            "volume": "346",
            "issue": "25",
            "pages": "1978-1988",
            "doi": "10.1056/NEJMra011089",
            "pmid": "12075060",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "guideline",
            "title": "Exertional heat illness during training and competition",
            "authors": "Casa DJ, Armstrong LE, Ganio MS, Yeargin SW",
            "journal": "Medicine & Science in Sports & Exercise",
            "year": 2007,
            "volume": "39",
            "issue": "3",
            "pages": "556-572",
            "doi": "10.1249/MSS.0b013e31802fa199",
            "pmid": "17473783",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "review",
            "title": "Heat stroke",
            "authors": "Leon LR, Bouchama A",
            "journal": "Comprehensive Physiology",
            "year": 2015,
            "volume": "5",
            "issue": "2",
            "pages": "611-647",
            "doi": "10.1002/cphy.c140017",
            "pmid": "25880507",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "primary",
            "title": "Heat-related illness",
            "authors": "Gaudio FG, Grissom CK",
            "journal": "Emergency Medicine Clinics of North America",
            "year": 2016,
            "volume": "34",
            "issue": "2",
            "pages": "277-292",
            "doi": "10.1016/j.emc.2015.12.002",
            "pmid": "27133242",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_MODERATE
        }
    ],
    
    "hypothermia": [
        {
            "type": "guideline",
            "title": "Accidental hypothermia",
            "authors": "Brown DJ, Brugger H, Boyd J, Paal P",
            "journal": "New England Journal of Medicine",
            "year": 2012,
            "volume": "367",
            "issue": "20",
            "pages": "1930-1938",
            "doi": "10.1056/NEJMra1114208",
            "pmid": "23150960",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "guideline",
            "title": "Accidental hypothermia",
            "authors": "Paal P, Gordon L, Strapazzon G, et al.",
            "journal": "Resuscitation",
            "year": 2016,
            "volume": "105",
            "pages": "188-199",
            "doi": "10.1016/j.resuscitation.2016.05.006",
            "pmid": "27212614",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "review",
            "title": "Accidental hypothermia",
            "authors": "Zafren K, Giesbrecht GG, Danzl DF, et al.",
            "journal": "Wilderness & Environmental Medicine",
            "year": 2014,
            "volume": "25",
            "issue": "4 Suppl",
            "pages": "S66-S85",
            "doi": "10.1016/j.wem.2014.10.010",
            "pmid": "25498264",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "primary",
            "title": "Hypothermia",
            "authors": "Danzi DF",
            "journal": "New England Journal of Medicine",
            "year": 2012,
            "volume": "367",
            "issue": "20",
            "pages": "1930-1938",
            "doi": "10.1056/NEJMra1114208",
            "pmid": "23150960",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "cardiac_arrest": [
        {
            "type": "guideline",
            "title": "2020 American Heart Association Guidelines for Cardiopulmonary Resuscitation and Emergency Cardiovascular Care",
            "authors": "Panchal AR, Bartos JA, Cabañas JG, et al.",
            "journal": "Circulation",
            "year": 2020,
            "volume": "142",
            "issue": "16_suppl_2",
            "pages": "S366-S468",
            "doi": "10.1161/CIR.0000000000000916",
            "pmid": "33081528",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG,
            "url": "https://www.ahajournals.org/doi/10.1161/CIR.0000000000000916"
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
        },
        {
            "type": "guideline",
            "title": "2020 American Heart Association Guidelines for Cardiopulmonary Resuscitation and Emergency Cardiovascular Care: Part 1: Executive Summary",
            "authors": "Merchant RM, Topjian AA, Panchal AR, et al.",
            "journal": "Circulation",
            "year": 2020,
            "volume": "142",
            "issue": "16_suppl_2",
            "pages": "S337-S357",
            "doi": "10.1161/CIR.0000000000000918",
            "pmid": "33081529",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "primary",
            "title": "Targeted Temperature Management for Cardiac Arrest with Nonshockable Rhythm",
            "authors": "Lascarrou JB, Merdji H, Le Gouge A, et al.",
            "journal": "New England Journal of Medicine",
            "year": 2019,
            "volume": "381",
            "issue": "24",
            "pages": "2327-2337",
            "doi": "10.1056/NEJMoa1906661",
            "pmid": "31577396",
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
    
    "upper_airway_obstruction": [
        {
            "type": "guideline",
            "title": "2020 American Heart Association Guidelines for Cardiopulmonary Resuscitation and Emergency Cardiovascular Care: Part 4: Adult Basic and Advanced Life Support",
            "authors": "Panchal AR, Bartos JA, Cabañas JG, et al.",
            "journal": "Circulation",
            "year": 2020,
            "volume": "142",
            "issue": "16_suppl_2",
            "pages": "S366-S468",
            "doi": "10.1161/CIR.0000000000000916",
            "pmid": "33081528",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "guideline",
            "title": "ATLS Advanced Trauma Life Support Student Course Manual",
            "authors": "American College of Surgeons Committee on Trauma",
            "journal": "ATLS",
            "year": 2021,
            "url": "https://www.facs.org/quality-programs/trauma/atls",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "guideline",
            "title": "Management of acute upper airway obstruction",
            "authors": "NICE Guideline",
            "journal": "National Institute for Health and Care Excellence",
            "year": 2015,
            "url": "https://www.nice.org.uk/guidance/ng115",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "review",
            "title": "Acute upper airway obstruction",
            "authors": "Walls RM, Murphy MF",
            "journal": "New England Journal of Medicine",
            "year": 2010,
            "volume": "363",
            "issue": "8",
            "pages": "784-791",
            "doi": "10.1056/NEJMra0910881",
            "pmid": "20818884",
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
    
    "acute_mesenteric_ischemia": [
        {
            "type": "guideline",
            "title": "WSES Guidelines for the management of acute mesenteric ischemia",
            "authors": "Bala M, Kashuk J, Moore EE, et al.",
            "journal": "World Journal of Emergency Surgery",
            "year": 2017,
            "volume": "12",
            "pages": "38",
            "doi": "10.1186/s13017-017-0150-5",
            "pmid": "28828073",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "guideline",
            "title": "The Society for Vascular Surgery practice guidelines on the care of patients with an abdominal aortic aneurysm",
            "authors": "Chaikof EL, Dalman RL, Eskandari MK, et al.",
            "journal": "Journal of Vascular Surgery",
            "year": 2018,
            "volume": "67",
            "issue": "1",
            "pages": "2-77.e2",
            "doi": "10.1016/j.jvs.2017.10.044",
            "pmid": "29268916",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "review",
            "title": "Acute mesenteric ischemia",
            "authors": "Oldenburg WA, Lau LL, Rodenberg TJ, Edmonds HJ, Burger CD",
            "journal": "Archives of Internal Medicine",
            "year": 2004,
            "volume": "164",
            "issue": "10",
            "pages": "1054-1062",
            "doi": "10.1001/archinte.164.10.1054",
            "pmid": "15159262",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "primary",
            "title": "Acute mesenteric ischemia: a clinical review",
            "authors": "Acosta S, Björck M",
            "journal": "European Journal of Vascular and Endovascular Surgery",
            "year": 2015,
            "volume": "49",
            "issue": "4",
            "pages": "460-466",
            "doi": "10.1016/j.ejvs.2014.11.044",
            "pmid": "25577136",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "cholecystitis_cholangitis": [
        {
            "type": "guideline",
            "title": "Tokyo Guidelines 2018: diagnostic criteria and severity grading of acute cholecystitis (with videos)",
            "authors": "Yokoe M, Hata J, Takada T, et al.",
            "journal": "Journal of Hepato-Biliary-Pancreatic Sciences",
            "year": 2018,
            "volume": "25",
            "issue": "1",
            "pages": "41-54",
            "doi": "10.1002/jhbp.515",
            "pmid": "29032610",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "guideline",
            "title": "Tokyo Guidelines 2018: diagnostic criteria and severity grading of acute cholangitis (with videos)",
            "authors": "Kiriyama S, Kozaka K, Takada T, et al.",
            "journal": "Journal of Hepato-Biliary-Pancreatic Sciences",
            "year": 2018,
            "volume": "25",
            "issue": "1",
            "pages": "17-30",
            "doi": "10.1002/jhbp.512",
            "pmid": "29032608",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "guideline",
            "title": "Tokyo Guidelines 2018: flowchart for the management of acute cholecystitis",
            "authors": "Okamoto K, Suzuki K, Takada T, et al.",
            "journal": "Journal of Hepato-Biliary-Pancreatic Sciences",
            "year": 2018,
            "volume": "25",
            "issue": "1",
            "pages": "55-72",
            "doi": "10.1002/jhbp.516",
            "pmid": "29032611",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "review",
            "title": "Acute cholecystitis and cholangitis",
            "authors": "Indar AA, Beckingham IJ",
            "journal": "BMJ",
            "year": 2002,
            "volume": "325",
            "issue": "7365",
            "pages": "639-643",
            "doi": "10.1136/bmj.325.7365.639",
            "pmid": "12242178",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "acute_appendicitis": [
        {
            "type": "guideline",
            "title": "WSES Jerusalem guidelines for diagnosis and treatment of acute appendicitis",
            "authors": "Di Saverio S, Podda M, De Simone B, et al.",
            "journal": "World Journal of Emergency Surgery",
            "year": 2020,
            "volume": "15",
            "pages": "27",
            "doi": "10.1186/s13017-020-00306-7",
            "pmid": "32336245",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "guideline",
            "title": "EAST practice management guidelines for diagnosis and treatment of acute appendicitis",
            "authors": "Snyder MJ, Guthrie M, Cagle S",
            "journal": "Journal of Trauma and Acute Care Surgery",
            "year": 2020,
            "volume": "89",
            "issue": "5",
            "pages": "1006-1015",
            "doi": "10.1097/TA.0000000000002890",
            "pmid": "32769978",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "primary",
            "title": "The Alvarado score for predicting acute appendicitis: a systematic review",
            "authors": "Ohle R, O'Reilly F, O'Brien KK, Fahey T, Dimitrov BD",
            "journal": "BMC Medicine",
            "year": 2011,
            "volume": "9",
            "pages": "139",
            "doi": "10.1186/1741-7015-9-139",
            "pmid": "22118577",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "review",
            "title": "Acute appendicitis: modern understanding of pathogenesis, diagnosis, and management",
            "authors": "Bhangu A, Søreide K, Di Saverio S, Assarsson JH, Drake FT",
            "journal": "The Lancet",
            "year": 2015,
            "volume": "386",
            "issue": "10000",
            "pages": "1278-1287",
            "doi": "10.1016/S0140-6736(15)00275-5",
            "pmid": "26460662",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "acute_diverticulitis": [
        {
            "type": "guideline",
            "title": "The American Society of Colon and Rectal Surgeons Clinical Practice Guidelines for the Treatment of Left-Sided Colonic Diverticulitis",
            "authors": "Hall J, Hardiman K, Lee S, et al.",
            "journal": "Diseases of the Colon & Rectum",
            "year": 2020,
            "volume": "63",
            "issue": "6",
            "pages": "728-747",
            "doi": "10.1097/DCR.0000000000001679",
            "pmid": "32384416",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "guideline",
            "title": "WSES Guidelines for the management of acute left-sided colonic diverticulitis in the emergency setting",
            "authors": "Sartelli M, Weber DG, Kluger Y, et al.",
            "journal": "World Journal of Emergency Surgery",
            "year": 2020,
            "volume": "15",
            "pages": "57",
            "doi": "10.1186/s13017-020-00338-9",
            "pmid": "33028356",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "review",
            "title": "Acute diverticulitis",
            "authors": "Strate LL, Morris AM",
            "journal": "New England Journal of Medicine",
            "year": 2019,
            "volume": "380",
            "issue": "6",
            "pages": "500-509",
            "doi": "10.1056/NEJMra1800468",
            "pmid": "30726687",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "primary",
            "title": "Acute diverticulitis",
            "authors": "Feuerstein JD, Falchuk KR",
            "journal": "Mayo Clinic Proceedings",
            "year": 2016,
            "volume": "91",
            "issue": "10",
            "pages": "1094-1104",
            "doi": "10.1016/j.mayocp.2016.03.012",
            "pmid": "27712639",
            "evidence_level": EVIDENCE_LEVEL_IIA,
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
    
    "H. pylori": [
        {
            "type": "guideline",
            "title": "Management of Helicobacter pylori infection—the Maastricht V/Florence Consensus Report",
            "authors": "Malfertheiner P, Megraud F, O'Morain CA, et al.",
            "journal": "Gut",
            "year": 2017,
            "volume": "66",
            "issue": "6",
            "pages": "6-30",
            "doi": "10.1136/gutjnl-2016-312288",
            "pmid": "27707777",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "guideline",
            "title": "ACG Clinical Guideline: Treatment of Helicobacter pylori Infection",
            "authors": "Chey WD, Leontiadis GI, Howden CW, Moss SF",
            "journal": "American Journal of Gastroenterology",
            "year": 2017,
            "volume": "112",
            "issue": "2",
            "pages": "212-239",
            "doi": "10.1038/ajg.2016.563",
            "pmid": "28071659",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "guideline",
            "title": "AGA Clinical Practice Update on the Management of Refractory Helicobacter pylori Infection: Expert Review",
            "authors": "Shah SC, Iyer PG, Moss SF",
            "journal": "Gastroenterology",
            "year": 2021,
            "volume": "160",
            "issue": "6",
            "pages": "1831-1841",
            "doi": "10.1053/j.gastro.2021.01.073",
            "pmid": "33771385",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "review",
            "title": "Treatment regimens for Helicobacter pylori",
            "authors": "Chey WD, Leontiadis GI",
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
    
    "GERD": [
        {
            "type": "guideline",
            "title": "ACG Clinical Guideline for the Diagnosis and Management of Gastroesophageal Reflux Disease",
            "authors": "Katz PO, Dunbar KB, Schnoll-Sussman FH, et al.",
            "journal": "American Journal of Gastroenterology",
            "year": 2022,
            "volume": "117",
            "issue": "1",
            "pages": "27-56",
            "doi": "10.14309/ajg.0000000000001538",
            "pmid": "34807007",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "guideline",
            "title": "AGA Clinical Practice Update on the Diagnosis and Management of Gastroesophageal Reflux Disease",
            "authors": "Gyawali CP, Kahrilas PJ, Savarino E, et al.",
            "journal": "Gastroenterology",
            "year": 2021,
            "volume": "161",
            "issue": "5",
            "pages": "1325-1337",
            "doi": "10.1053/j.gastro.2021.08.060",
            "pmid": "34593314",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "review",
            "title": "Medical management of gastroesophageal reflux disease in adults",
            "authors": "Kahrilas PJ, Shaheen NJ, Vaezi MF",
            "journal": "UpToDate",
            "year": 2024,
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_MODERATE
        }
    ],
    
    "IBS": [
        {
            "type": "guideline",
            "title": "ACG Clinical Guideline: Management of Irritable Bowel Syndrome",
            "authors": "Lacy BE, Pimentel M, Brenner DM, et al.",
            "journal": "American Journal of Gastroenterology",
            "year": 2021,
            "volume": "116",
            "issue": "1",
            "pages": "17-44",
            "doi": "10.14309/ajg.0000000000001036",
            "pmid": "33315591",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "guideline",
            "title": "Rome IV Criteria for Irritable Bowel Syndrome",
            "authors": "Drossman DA, Hasler WL",
            "journal": "Gastroenterology",
            "year": 2016,
            "volume": "150",
            "issue": "6",
            "pages": "1257-1260",
            "doi": "10.1053/j.gastro.2016.03.035",
            "pmid": "27147121",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "review",
            "title": "Treatment of irritable bowel syndrome",
            "authors": "Lacy BE, Patel NK",
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
    
    "Acute Colitis": [
        {
            "type": "guideline",
            "title": "ACG Clinical Guideline: Diagnosis, treatment, and prevention of acute diarrheal infections in adults",
            "authors": "Riddle MS, DuPont HL, Connor BA",
            "journal": "American Journal of Gastroenterology",
            "year": 2016,
            "volume": "111",
            "issue": "5",
            "pages": "602-622",
            "doi": "10.1038/ajg.2016.126",
            "pmid": "27068718",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "guideline",
            "title": "WSES guidelines for the management of acute left-sided colonic diverticulitis in the emergency setting",
            "authors": "Sartelli M, Weber DG, Kluger Y, et al.",
            "journal": "World Journal of Emergency Surgery",
            "year": 2020,
            "volume": "15",
            "pages": "57",
            "doi": "10.1186/s13017-020-00335-8",
            "pmid": "33062058",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "guideline",
            "title": "ACG Clinical Guideline: Management of acute pancreatitis",
            "authors": "Tenner S, Baillie J, DeWitt J, Vege SS",
            "journal": "American Journal of Gastroenterology",
            "year": 2013,
            "volume": "108",
            "issue": "9",
            "pages": "1400-1415",
            "doi": "10.1038/ajg.2013.218",
            "pmid": "23896955",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "review",
            "title": "Ischemic colitis: Clinical practice in diagnosis and treatment",
            "authors": "Brandt LJ, Feuerstadt P, Longstreth GF, Boley SJ",
            "journal": "World Journal of Gastroenterology",
            "year": 2011,
            "volume": "17",
            "issue": "46",
            "pages": "5117-5125",
            "doi": "10.3748/wjg.v17.i46.5117",
            "pmid": "22158647",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "acute_intestinal_obstruction": [
        {
            "type": "guideline",
            "title": "WSES guidelines for the management of small bowel obstruction",
            "authors": "Ten Broek RPG, Krielen P, Di Saverio S, et al.",
            "journal": "World Journal of Emergency Surgery",
            "year": 2018,
            "volume": "13",
            "pages": "24",
            "doi": "10.1186/s13017-018-0185-2",
            "pmid": "29946347",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "guideline",
            "title": "EAST practice management guidelines for small bowel obstruction",
            "authors": "Maung AA, Johnson DC, Piper GL, et al.",
            "journal": "Journal of Trauma and Acute Care Surgery",
            "year": 2012,
            "volume": "73",
            "issue": "5 Suppl 4",
            "pages": "S362-S369",
            "doi": "10.1097/TA.0b013e31827019de",
            "pmid": "23114489",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "review",
            "title": "Small bowel obstruction",
            "authors": "Catena F, De Simone B, Coccolini F, Di Saverio S, Sartelli M, Ansaloni L",
            "journal": "World Journal of Emergency Surgery",
            "year": 2019,
            "volume": "14",
            "pages": "20",
            "doi": "10.1186/s13017-019-0240-7",
            "pmid": "31080499",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "primary",
            "title": "Large bowel obstruction",
            "authors": "Frago R, Ramirez E, Millan M, Kreisler E, del Valle E, Biondo S",
            "journal": "World Journal of Gastroenterology",
            "year": 2014,
            "volume": "20",
            "issue": "43",
            "pages": "16189-16197",
            "doi": "10.3748/wjg.v20.i43.16189",
            "pmid": "25473173",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_STRONG
        }
    ],

    "green_pit_viper_bite": [
        {
            "type": "guideline",
            "title": "WHO Guidelines for the management of snake-bites",
            "authors": "WHO",
            "journal": "World Health Organization",
            "year": 2016,
            "url": "https://www.who.int/publications/i/item/9789290225300",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "review",
            "title": "Snakebite envenoming",
            "authors": "Gutiérrez JM, Calvete JJ, Habib AG, et al.",
            "journal": "Nature Reviews Disease Primers",
            "year": 2017,
            "volume": "3",
            "pages": "17063",
            "doi": "10.1038/nrdp.2017.63",
            "pmid": "24040916",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],

    "cobra_bite": [
        {
            "type": "guideline",
            "title": "WHO Guidelines for the management of snake-bites",
            "authors": "WHO",
            "journal": "World Health Organization",
            "year": 2016,
            "url": "https://www.who.int/publications/i/item/9789290225300",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "review",
            "title": "Neurotoxic snakebite in Southeast Asia",
            "authors": "Warrell DA",
            "journal": "Clinical Toxicology",
            "year": 2013,
            "volume": "51",
            "issue": "8",
            "pages": "763-770",
            "doi": "10.3109/15563650.2013.838636",
            "pmid": "24040916",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_MODERATE
        }
    ],

    "krait_bite": [
        {
            "type": "guideline",
            "title": "WHO Guidelines for the management of snake-bites",
            "authors": "WHO",
            "journal": "World Health Organization",
            "year": 2016,
            "url": "https://www.who.int/publications/i/item/9789290225300",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "review",
            "title": "Krait bite envenoming",
            "authors": "Warrell DA",
            "journal": "Clinical Toxicology",
            "year": 2013,
            "volume": "51",
            "issue": "8",
            "pages": "763-770",
            "doi": "10.3109/15563650.2013.838636",
            "pmid": "24040916",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_MODERATE
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

