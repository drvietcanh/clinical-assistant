"""
References Configuration for All Calculators
Contains PubMed links, guidelines, and evidence grading for each calculator
"""

from typing import List, Dict, Any
from components.references import (
    GRADE_HIGH, GRADE_MODERATE, GRADE_LOW,
    EVIDENCE_LEVEL_I, EVIDENCE_LEVEL_IIA, EVIDENCE_LEVEL_IIB,
    STRENGTH_STRONG, STRENGTH_MODERATE
)

# References database organized by calculator name
CALCULATOR_REFERENCES: Dict[str, List[Dict[str, Any]]] = {
    "CHA2DS2-VASc": [
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
            "strength": STRENGTH_STRONG,
            "url": "https://academic.oup.com/eurheartj/article/42/5/373/5899008"
        },
        {
            "type": "primary",
            "title": "Refining clinical risk stratification for predicting stroke and thromboembolism in atrial fibrillation using a novel risk factor-based approach: the euro heart survey on atrial fibrillation",
            "authors": "Lip GY, Nieuwlaat R, Pisters R, Lane DA, Crijns HJ",
            "journal": "Chest",
            "year": 2010,
            "volume": "137",
            "issue": "2",
            "pages": "263-272",
            "doi": "10.1378/chest.09-1584",
            "pmid": "19762550",
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
    
    "BARTHEL": [
        {
            "type": "primary",
            "title": "Functional evaluation: the Barthel Index",
            "authors": "Mahoney FI, Barthel DW",
            "journal": "Maryland State Medical Journal",
            "year": 1965,
            "volume": "14",
            "issue": "",
            "pages": "61-65",
            "pmid": "14258950",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "ROCKALL": [
        {
            "type": "primary",
            "title": "Risk assessment after acute upper gastrointestinal haemorrhage",
            "authors": "Rockall TA, Logan RF, Devlin HB, Northfield TC",
            "journal": "Gut",
            "year": 1996,
            "volume": "38",
            "issue": "3",
            "pages": "316-321",
            "doi": "10.1136/gut.38.3.316",
            "pmid": "8801197",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "RANSON": [
        {
            "type": "primary",
            "title": "Prognostic signs and the role of operative management in acute pancreatitis",
            "authors": "Ranson JHC, Rifkind KM, Roses DF, Fink SD, Eng K, Spencer FC",
            "journal": "Surgery, Gynecology & Obstetrics",
            "year": 1974,
            "volume": "139",
            "issue": "1",
            "pages": "69-81",
            "pmid": "4834279",
            "evidence_level": EVIDENCE_LEVEL_IIB,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "KILLIP": [
        {
            "type": "primary",
            "title": "Treatment of myocardial infarction in a coronary care unit. A two year experience with 250 patients",
            "authors": "Killip T, Kimball JT",
            "journal": "American Journal of Cardiology",
            "year": 1967,
            "volume": "20",
            "issue": "4",
            "pages": "457-464",
            "doi": "10.1016/0002-9149(67)90023-9",
            "pmid": "6059183",
            "evidence_level": EVIDENCE_LEVEL_IIB,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "DUKE": [
        {
            "type": "primary",
            "title": "Prognostic value of a treadmill exercise score in outpatients with suspected coronary artery disease",
            "authors": "Mark DB, Hlatky MA, Harrell FE Jr, Lee KL, Califf RM, Pryor DB",
            "journal": "New England Journal of Medicine",
            "year": 1991,
            "volume": "325",
            "issue": "12",
            "pages": "849-853",
            "doi": "10.1056/NEJM199109193251204",
            "pmid": "1883071",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "ASA Physical Status": [
        {
            "type": "guideline",
            "title": "ASA Physical Status Classification System (Approved by the ASA House of Delegates, last amended 2014)",
            "authors": "American Society of Anesthesiologists",
            "journal": "American Society of Anesthesiologists",
            "year": 2014,
            "url": "https://www.asahq.org/standards-and-guidelines/asa-physical-status-classification-system",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "APGAR Score": [
        {
            "type": "primary",
            "title": "A proposal for a new method of evaluation of the newborn infant",
            "authors": "Apgar V",
            "journal": "Current Researches in Anesthesia & Analgesia",
            "year": 1953,
            "volume": "32",
            "issue": "4",
            "pages": "260-267",
            "pmid": "13083014",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "HAS-BLED": [
        {
            "type": "primary",
            "title": "A novel user-friendly score (HAS-BLED) to assess 1-year risk of major bleeding in patients with atrial fibrillation: the Euro Heart Survey",
            "authors": "Pisters R, Lane DA, Nieuwlaat R, de Vos CB, Crijns HJ, Lip GY",
            "journal": "Chest",
            "year": 2010,
            "volume": "138",
            "issue": "5",
            "pages": "1093-1100",
            "doi": "10.1378/chest.10-0134",
            "pmid": "20299623",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        },
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
        }
    ],
    
    "Wells PE": [
        {
            "type": "primary",
            "title": "Derivation of a simple clinical model to categorize patients probability of pulmonary embolism: increasing the models utility with the SimpliRED D-dimer",
            "authors": "Wells PS, Anderson DR, Rodger M, et al.",
            "journal": "Thrombosis and Haemostasis",
            "year": 2000,
            "volume": "83",
            "issue": "3",
            "pages": "416-420",
            "pmid": "10744147",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        },
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
        }
    ],
    
    "PERC": [
        {
            "type": "primary",
            "title": "Clinical criteria to prevent unnecessary diagnostic testing in emergency department patients with suspected pulmonary embolism",
            "authors": "Kline JA, Mitchell AM, Kabrhel C, Richman PB, Courtney DM",
            "journal": "Journal of Thrombosis and Haemostasis",
            "year": 2004,
            "volume": "2",
            "issue": "8",
            "pages": "1247-1255",
            "doi": "10.1111/j.1538-7836.2004.00790.x",
            "pmid": "15304025",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "guideline",
            "title": "2019 ESC Guidelines for the diagnosis and management of acute pulmonary embolism",
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
        }
    ],
    
    "CURB-65": [
        {
            "type": "primary",
            "title": "Defining community acquired pneumonia severity on presentation to hospital: an international derivation and validation study",
            "authors": "Lim WS, van der Eerden MM, Laing R, et al.",
            "journal": "Thorax",
            "year": 2003,
            "volume": "58",
            "issue": "5",
            "pages": "377-382",
            "doi": "10.1136/thorax.58.5.377",
            "pmid": "12728155",
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
    
    "SOFA": [
        {
            "type": "primary",
            "title": "The SOFA (Sepsis-related Organ Failure Assessment) score to describe organ dysfunction/failure",
            "authors": "Vincent JL, Moreno R, Takala J, et al.",
            "journal": "Intensive Care Medicine",
            "year": 1996,
            "volume": "22",
            "issue": "7",
            "pages": "707-710",
            "doi": "10.1007/BF01709751",
            "pmid": "8844239",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
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
        }
    ],
    
    "qSOFA": [
        {
            "type": "primary",
            "title": "Assessment of Clinical Criteria for Sepsis: For the Third International Consensus Definitions for Sepsis and Septic Shock (Sepsis-3)",
            "authors": "Seymour CW, Liu VX, Iwashyna TJ, et al.",
            "journal": "JAMA",
            "year": 2016,
            "volume": "315",
            "issue": "8",
            "pages": "762-774",
            "doi": "10.1001/jama.2016.0288",
            "pmid": "26903335",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
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
        }
    ],
    
    "NEWS2": [
        {
            "type": "guideline",
            "title": "National Early Warning Score (NEWS) 2: Standardising the assessment of acute-illness severity in the NHS",
            "authors": "Royal College of Physicians",
            "journal": "Royal College of Physicians",
            "year": 2017,
            "url": "https://www.rcplondon.ac.uk/projects/outputs/national-early-warning-score-news-2",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "primary",
            "title": "The ability of the National Early Warning Score (NEWS) to discriminate patients at risk of early cardiac arrest, unanticipated intensive care unit admission, and death",
            "authors": "Smith GB, Prytherch DR, Meredith P, Schmidt PE, Featherstone PI",
            "journal": "Resuscitation",
            "year": 2013,
            "volume": "84",
            "issue": "4",
            "pages": "465-470",
            "doi": "10.1016/j.resuscitation.2012.12.016",
            "pmid": "23295778",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_MODERATE
        }
    ],
    
    "ASCVD Risk": [
        {
            "type": "guideline",
            "title": "2013 ACC/AHA Guideline on the Assessment of Cardiovascular Risk",
            "authors": "Goff DC Jr, Lloyd-Jones DM, Bennett G, et al.",
            "journal": "Journal of the American College of Cardiology",
            "year": 2014,
            "volume": "63",
            "issue": "25 Pt B",
            "pages": "2935-2959",
            "doi": "10.1016/j.jacc.2013.11.005",
            "pmid": "24239921",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "primary",
            "title": "2013 ACC/AHA Guideline on the Treatment of Blood Cholesterol to Reduce Atherosclerotic Cardiovascular Risk in Adults",
            "authors": "Stone NJ, Robinson JG, Lichtenstein AH, et al.",
            "journal": "Journal of the American College of Cardiology",
            "year": 2014,
            "volume": "63",
            "issue": "25 Pt B",
            "pages": "2889-2934",
            "doi": "10.1016/j.jacc.2013.11.002",
            "pmid": "24239923",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "ASCVD": [
        {
            "type": "guideline",
            "title": "2013 ACC/AHA Guideline on the Assessment of Cardiovascular Risk",
            "authors": "Goff DC Jr, Lloyd-Jones DM, Bennett G, et al.",
            "journal": "Journal of the American College of Cardiology",
            "year": 2014,
            "volume": "63",
            "issue": "25 Pt B",
            "pages": "2935-2959",
            "doi": "10.1016/j.jacc.2013.11.005",
            "pmid": "24239921",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "primary",
            "title": "2013 ACC/AHA Guideline on the Treatment of Blood Cholesterol to Reduce Atherosclerotic Cardiovascular Risk in Adults",
            "authors": "Stone NJ, Robinson JG, Lichtenstein AH, et al.",
            "journal": "Journal of the American College of Cardiology",
            "year": 2014,
            "volume": "63",
            "issue": "25 Pt B",
            "pages": "2889-2934",
            "doi": "10.1016/j.jacc.2013.11.002",
            "pmid": "24239923",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "TIMI": [
        {
            "type": "primary",
            "title": "The TIMI risk score for unstable angina/non–ST elevation MI: A method for prognostication and therapeutic decision making",
            "authors": "Antman EM, Cohen M, Bernink PJ, et al.",
            "journal": "JAMA",
            "year": 2000,
            "volume": "284",
            "issue": "7",
            "pages": "835-842",
            "doi": "10.1001/jama.284.7.835",
            "pmid": "10938172",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "QTc": [
        {
            "type": "primary",
            "title": "An analysis of the time-relations of electrocardiograms",
            "authors": "Bazett HC",
            "journal": "Heart",
            "year": 1920,
            "volume": "7",
            "issue": "",
            "pages": "353-370",
            "pmid": "",
            "evidence_level": EVIDENCE_LEVEL_IIB,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "HEART": [
        {
            "type": "primary",
            "title": "Chest pain in the emergency room: value of the HEART score",
            "authors": "Six AJ, Backus BE, Kelder JC",
            "journal": "Netherlands Heart Journal",
            "year": 2008,
            "volume": "16",
            "issue": "6",
            "pages": "191-196",
            "doi": "10.1007/BF03086144",
            "pmid": "18345366",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "GRACE": [
        {
            "type": "primary",
            "title": "Predictors of hospital mortality in the Global Registry of Acute Coronary Events",
            "authors": "Granger CB, Goldberg RJ, Dabbous O, et al.",
            "journal": "Archives of Internal Medicine",
            "year": 2003,
            "volume": "163",
            "issue": "19",
            "pages": "2345-2353",
            "doi": "10.1001/archinte.163.19.2345",
            "pmid": "14581255",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "MELD": [
        {
            "type": "primary",
            "title": "A model to predict survival in patients with end-stage liver disease",
            "authors": "Kamath PS, Wiesner RH, Malinchoc M, et al.",
            "journal": "Hepatology",
            "year": 2001,
            "volume": "33",
            "issue": "2",
            "pages": "464-470",
            "doi": "10.1053/jhep.2001.22172",
            "pmid": "11172350",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "guideline",
            "title": "AASLD Practice Guidelines: Evaluation of the Patient for Liver Transplantation",
            "authors": "Martin P, DiMartini A, Feng S, Brown R, Fallon M",
            "journal": "Hepatology",
            "year": 2014,
            "volume": "60",
            "issue": "2",
            "pages": "715-735",
            "doi": "10.1002/hep.27272",
            "pmid": "25042480",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "Child-Pugh": [
        {
            "type": "primary",
            "title": "Transection of the oesophagus for bleeding oesophageal varices",
            "authors": "Pugh RN, Murray-Lyon IM, Dawson JL, Pietroni MC, Williams R",
            "journal": "British Journal of Surgery",
            "year": 1973,
            "volume": "60",
            "issue": "8",
            "pages": "646-649",
            "doi": "10.1002/bjs.1800600817",
            "pmid": "4541913",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "guideline",
            "title": "AASLD Practice Guidelines: Evaluation of the Patient for Liver Transplantation",
            "authors": "Martin P, DiMartini A, Feng S, Brown R, Fallon M",
            "journal": "Hepatology",
            "year": 2014,
            "volume": "60",
            "issue": "2",
            "pages": "715-735",
            "doi": "10.1002/hep.27272",
            "pmid": "25042480",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],
    
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
    
    "Wells DVT": [
        {
            "type": "primary",
            "title": "Value of assessment of pretest probability of deep-vein thrombosis in clinical management",
            "authors": "Wells PS, Hirsh J, Anderson DR, et al.",
            "journal": "Lancet",
            "year": 1997,
            "volume": "350",
            "issue": "9094",
            "pages": "1795-1798",
            "doi": "10.1016/S0140-6736(97)08140-3",
            "pmid": "9428249",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "guideline",
            "title": "2019 ESC Guidelines for the diagnosis and management of acute pulmonary embolism",
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
        }
    ],
    
    "eGFR": [
        {
            "type": "primary",
            "title": "A new equation to estimate glomerular filtration rate",
            "authors": "Levey AS, Stevens LA, Schmid CH, et al.",
            "journal": "Annals of Internal Medicine",
            "year": 2009,
            "volume": "150",
            "issue": "9",
            "pages": "604-612",
            "doi": "10.7326/0003-4819-150-9-200904070-00006",
            "pmid": "19414839",
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
    
    "KDIGO": [
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
            "title": "Acute Kidney Injury Network: report of an initiative to improve outcomes in acute kidney injury",
            "authors": "Mehta RL, Kellum JA, Shah SV, et al.",
            "journal": "Critical Care",
            "year": 2007,
            "volume": "11",
            "issue": "2",
            "pages": "R31",
            "doi": "10.1186/cc5713",
            "pmid": "17331245",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "APACHE II": [
        {
            "type": "primary",
            "title": "APACHE II: a severity of disease classification system",
            "authors": "Knaus WA, Draper EA, Wagner DP, Zimmerman JE",
            "journal": "Critical Care Medicine",
            "year": 1985,
            "volume": "13",
            "issue": "10",
            "pages": "818-829",
            "pmid": "3928249",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "SAPS II": [
        {
            "type": "primary",
            "title": "A new Simplified Acute Physiology Score (SAPS II) based on a European/North American multicenter study",
            "authors": "Le Gall JR, Lemeshow S, Saulnier F",
            "journal": "JAMA",
            "year": 1993,
            "volume": "270",
            "issue": "24",
            "pages": "2957-2963",
            "doi": "10.1001/jama.1993.03510240069035",
            "pmid": "8254858",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "BISAP": [
        {
            "type": "primary",
            "title": "A simple bedside score (BISAP) for early identification of patients at high risk of in-hospital mortality in acute pancreatitis",
            "authors": "Wu BU, Johannes RS, Sun X, Tabak Y, Conwell DL, Banks PA",
            "journal": "American Journal of Gastroenterology",
            "year": 2009,
            "volume": "104",
            "issue": "4",
            "pages": "966-971",
            "doi": "10.1038/ajg.2009.28",
            "pmid": "19293784",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_MODERATE
        }
    ],
    
    "HEART Score": [
        {
            "type": "primary",
            "title": "The HEART score for the assessment of patients with chest pain in the emergency department: a multinational validation study",
            "authors": "Six AJ, Backus BE, Kelder JC",
            "journal": "Critical Pathways in Cardiology",
            "year": 2008,
            "volume": "7",
            "issue": "3",
            "pages": "164-170",
            "doi": "10.1097/HPC.0b013e31818e5a0e",
            "pmid": "18791405",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "GRACE Score": [
        {
            "type": "primary",
            "title": "Predictors of hospital mortality in the global registry of acute coronary events",
            "authors": "Granger CB, Goldberg RJ, Dabbous O, et al.",
            "journal": "Archives of Internal Medicine",
            "year": 2003,
            "volume": "163",
            "issue": "19",
            "pages": "2345-2353",
            "doi": "10.1001/archinte.163.19.2345",
            "pmid": "14581255",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "TIMI Risk": [
        {
            "type": "primary",
            "title": "The Thrombolysis in Myocardial Infarction (TIMI) risk score for unstable angina/non-ST elevation MI: A method for prognostication and therapeutic decision making",
            "authors": "Antman EM, Cohen M, Bernink PJ, et al.",
            "journal": "JAMA",
            "year": 2000,
            "volume": "284",
            "issue": "7",
            "pages": "835-842",
            "doi": "10.1001/jama.284.7.835",
            "pmid": "10938172",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "PESI": [
        {
            "type": "primary",
            "title": "A prediction rule to identify low-risk patients with pulmonary embolism",
            "authors": "Aujesky D, Obrosky DS, Stone RA, et al.",
            "journal": "Archives of Internal Medicine",
            "year": 2005,
            "volume": "165",
            "issue": "4",
            "pages": "458-462",
            "doi": "10.1001/archinte.165.4.458",
            "pmid": "15738375",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "guideline",
            "title": "2019 ESC Guidelines for the diagnosis and management of acute pulmonary embolism",
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
        }
    ],
    
    "PSI/PORT": [
        {
            "type": "primary",
            "title": "A prediction rule to identify low-risk patients with community-acquired pneumonia",
            "authors": "Fine MJ, Auble TE, Yealy DM, et al.",
            "journal": "New England Journal of Medicine",
            "year": 1997,
            "volume": "336",
            "issue": "4",
            "pages": "243-250",
            "doi": "10.1056/NEJM199701233360402",
            "pmid": "8995086",
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
    
    "Child-Pugh": [
        {
            "type": "primary",
            "title": "Transection of the oesophagus for bleeding oesophageal varices",
            "authors": "Pugh RN, Murray-Lyon IM, Dawson JL, Pietroni MC, Williams R",
            "journal": "British Journal of Surgery",
            "year": 1973,
            "volume": "60",
            "issue": "8",
            "pages": "646-649",
            "doi": "10.1002/bjs.1800600817",
            "pmid": "4541913",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "guideline",
            "title": "AASLD Practice Guidelines: Evaluation of the Patient for Liver Transplantation",
            "authors": "Martin P, DiMartini A, Feng S, Brown R, Fallon M",
            "journal": "Hepatology",
            "year": 2014,
            "volume": "60",
            "issue": "2",
            "pages": "715-735",
            "doi": "10.1002/hep.27272",
            "pmid": "25042480",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "Glasgow-Blatchford": [
        {
            "type": "primary",
            "title": "A risk score to predict need for treatment for upper-gastrointestinal haemorrhage",
            "authors": "Blatchford O, Murray WR, Blatchford M",
            "journal": "Lancet",
            "year": 2000,
            "volume": "356",
            "issue": "9238",
            "pages": "1318-1321",
            "doi": "10.1016/S0140-6736(00)02816-6",
            "pmid": "11073021",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        },
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
        }
    ],
    
    "RTS": [
        {
            "type": "primary",
            "title": "The Injury Severity Score: a method for describing patients with multiple injuries and evaluating emergency care",
            "authors": "Baker SP, O'Neill B, Haddon W Jr, Long WB",
            "journal": "Journal of Trauma",
            "year": 1974,
            "volume": "14",
            "issue": "3",
            "pages": "187-196",
            "pmid": "4814394",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "primary",
            "title": "A revision of the Trauma Score",
            "authors": "Champion HR, Sacco WJ, Copes WS, Gann DS, Gennarelli TA, Flanagan ME",
            "journal": "Journal of Trauma",
            "year": 1989,
            "volume": "29",
            "issue": "5",
            "pages": "623-629",
            "pmid": "2657085",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "ISS": [
        {
            "type": "primary",
            "title": "The Injury Severity Score: a method for describing patients with multiple injuries and evaluating emergency care",
            "authors": "Baker SP, O'Neill B, Haddon W Jr, Long WB",
            "journal": "Journal of Trauma",
            "year": 1974,
            "volume": "14",
            "issue": "3",
            "pages": "187-196",
            "pmid": "4814394",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "MEWS": [
        {
            "type": "primary",
            "title": "Validation of a modified Early Warning Score in medical admissions",
            "authors": "Subbe CP, Kruger M, Rutherford P, Gemmel L",
            "journal": "QJM",
            "year": 2001,
            "volume": "94",
            "issue": "10",
            "pages": "521-526",
            "doi": "10.1093/qjmed/94.10.521",
            "pmid": "11588210",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_MODERATE
        }
    ],
    
    "4Ts Score": [
        {
            "type": "primary",
            "title": "The HIT Expert Probability (HEP) Score: a novel pre-test probability model for heparin-induced thrombocytopenia based on broad expert opinion",
            "authors": "Cuker A, Gimotty PA, Crowther MA, Warkentin TE",
            "journal": "Journal of Thrombosis and Haemostasis",
            "year": 2010,
            "volume": "8",
            "issue": "2",
            "pages": "264-269",
            "doi": "10.1111/j.1538-7836.2009.03684.x",
            "pmid": "19922431",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "primary",
            "title": "Evaluation of pretest clinical score (4 T's) for the diagnosis of heparin-induced thrombocytopenia in two clinical settings",
            "authors": "Cuker A, Arepally G, Crowther MA, et al.",
            "journal": "Journal of Thrombosis and Haemostasis",
            "year": 2006,
            "volume": "4",
            "issue": "4",
            "pages": "759-765",
            "doi": "10.1111/j.1538-7836.2006.01787.x",
            "pmid": "16634744",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "Padua": [
        {
            "type": "primary",
            "title": "Risk assessment model for prediction of venous thromboembolism in hospitalized medical patients",
            "authors": "Barbar S, Noventa F, Rossetto V, et al.",
            "journal": "Journal of Thrombosis and Haemostasis",
            "year": 2010,
            "volume": "8",
            "issue": "11",
            "pages": "2450-2457",
            "doi": "10.1111/j.1538-7836.2010.04044.x",
            "pmid": "20738765",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "guideline",
            "title": "American Society of Hematology 2018 guidelines for management of venous thromboembolism: prophylaxis for hospitalized and nonhospitalized medical patients",
            "authors": "Schünemann HJ, Cushman M, Burnett AE, et al.",
            "journal": "Blood Advances",
            "year": 2018,
            "volume": "2",
            "issue": "22",
            "pages": "3198-3225",
            "doi": "10.1182/bloodadvances.2018022954",
            "pmid": "30482765",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "PERC": [
        {
            "type": "primary",
            "title": "Clinical criteria to prevent unnecessary diagnostic testing in emergency department patients with suspected pulmonary embolism",
            "authors": "Kline JA, Mitchell AM, Kabrhel C, Richman PB, Courtney DM",
            "journal": "Journal of Thrombosis and Haemostasis",
            "year": 2004,
            "volume": "2",
            "issue": "8",
            "pages": "1247-1255",
            "doi": "10.1111/j.1538-7836.2004.00790.x",
            "pmid": "15304025",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "guideline",
            "title": "2019 ESC Guidelines for the diagnosis and management of acute pulmonary embolism",
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
        }
    ],
    
    # Additional important calculators
    "NYHA": [
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
            "type": "primary",
            "title": "Nomenclature and Criteria for Diagnosis of Diseases of the Heart and Great Vessels",
            "authors": "The Criteria Committee of the New York Heart Association",
            "journal": "Little, Brown & Co",
            "year": 1994,
            "pages": "253-256",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "Killip": [
        {
            "type": "primary",
            "title": "Treatment of myocardial infarction in a coronary care unit. A two year experience with 250 patients",
            "authors": "Killip T 3rd, Kimball JT",
            "journal": "American Journal of Cardiology",
            "year": 1967,
            "volume": "20",
            "issue": "4",
            "pages": "457-464",
            "doi": "10.1016/0002-9149(67)90023-9",
            "pmid": "6059183",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_STRONG
        },
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
        }
    ],
    
    "Duke": [
        {
            "type": "primary",
            "title": "New criteria for diagnosis of infective endocarditis: utilization of specific echocardiographic findings. Duke Endocarditis Service",
            "authors": "Durack DT, Lukes AS, Bright DK",
            "journal": "American Journal of Medicine",
            "year": 1994,
            "volume": "96",
            "issue": "3",
            "pages": "200-209",
            "doi": "10.1016/0002-9343(94)90143-0",
            "pmid": "8154507",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        },
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
        }
    ],
    
    "SCORE2": [
        {
            "type": "primary",
            "title": "SCORE2 risk prediction algorithms: new models to estimate 10-year risk of cardiovascular disease in Europe",
            "authors": "SCORE2 Working Group and ESC Cardiovascular Risk Collaboration",
            "journal": "European Heart Journal",
            "year": 2021,
            "volume": "42",
            "issue": "25",
            "pages": "2439-2454",
            "doi": "10.1093/eurheartj/ehab309",
            "pmid": "34120177",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "guideline",
            "title": "2021 ESC Guidelines on cardiovascular disease prevention in clinical practice",
            "authors": "Visseren FLJ, Mach F, Smulders YM, et al.",
            "journal": "European Heart Journal",
            "year": 2021,
            "volume": "42",
            "issue": "34",
            "pages": "3227-3337",
            "doi": "10.1093/eurheartj/ehab484",
            "pmid": "34458905",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "SCORE2-OP": [
        {
            "type": "primary",
            "title": "SCORE2-OP risk prediction algorithms: estimating incident cardiovascular event risk in older persons in four geographical risk regions",
            "authors": "SCORE2-OP Working Group and ESC Cardiovascular Risk Collaboration",
            "journal": "European Heart Journal",
            "year": 2021,
            "volume": "42",
            "issue": "25",
            "pages": "2455-2467",
            "doi": "10.1093/eurheartj/ehab312",
            "pmid": "34120178",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "Corrected QT": [
        {
            "type": "primary",
            "title": "An analysis of the time-relations of electrocardiograms",
            "authors": "Bazett HC",
            "journal": "Heart",
            "year": 1920,
            "volume": "7",
            "issue": "4",
            "pages": "353-370",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "guideline",
            "title": "2015 ESC Guidelines for the management of patients with ventricular arrhythmias and the prevention of sudden cardiac death",
            "authors": "Priori SG, Blomström-Lundqvist C, Mazzanti A, et al.",
            "journal": "European Heart Journal",
            "year": 2015,
            "volume": "36",
            "issue": "41",
            "pages": "2793-2867",
            "doi": "10.1093/eurheartj/ehv316",
            "pmid": "26320108",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "SMART-COP": [
        {
            "type": "primary",
            "title": "SMART-COP: a tool for predicting the need for intensive respiratory or vasopressor support in community-acquired pneumonia",
            "authors": "Charles PG, Wolfe R, Whitby M, et al.",
            "journal": "Clinical Infectious Diseases",
            "year": 2008,
            "volume": "47",
            "issue": "3",
            "pages": "375-384",
            "doi": "10.1086/589754",
            "pmid": "18558884",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "ARDS Berlin": [
        {
            "type": "guideline",
            "title": "The Berlin definition of ARDS: an expanded rationale, justification, and supplementary material",
            "authors": "ARDS Definition Task Force",
            "journal": "Intensive Care Medicine",
            "year": 2012,
            "volume": "38",
            "issue": "10",
            "pages": "1573-1582",
            "doi": "10.1007/s00134-012-2682-3",
            "pmid": "22926653",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "primary",
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
        }
    ],
    
    "BODE Index": [
        {
            "type": "primary",
            "title": "The body-mass index, airflow obstruction, dyspnea, and exercise capacity index in chronic obstructive pulmonary disease",
            "authors": "Celli BR, Cote CG, Marin JM, et al.",
            "journal": "New England Journal of Medicine",
            "year": 2004,
            "volume": "350",
            "issue": "10",
            "pages": "1005-1012",
            "doi": "10.1056/NEJMoa021322",
            "pmid": "15014182",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "ASPECTS": [
        {
            "type": "primary",
            "title": "Use of the Alberta Stroke Program Early CT Score (ASPECTS) for assessing CT scans in patients with acute stroke",
            "authors": "Barber PA, Demchuk AM, Zhang J, Buchan AM",
            "journal": "AJNR American Journal of Neuroradiology",
            "year": 2000,
            "volume": "21",
            "issue": "4",
            "pages": "1534-1542",
            "pmid": "10871002",
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
    
    "Barthel Index": [
        {
            "type": "primary",
            "title": "Functional evaluation: the Barthel Index",
            "authors": "Mahoney FI, Barthel DW",
            "journal": "Maryland State Medical Journal",
            "year": 1965,
            "volume": "14",
            "pages": "61-65",
            "pmid": "14258950",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "AIMS65": [
        {
            "type": "primary",
            "title": "AIMS65 score compared with Glasgow-Blatchford score in predicting outcomes in upper GI bleeding",
            "authors": "Saltzman JR, Tabak YP, Hyett BH, Sun X, Travis AC, Johannes RS",
            "journal": "Gastrointestinal Endoscopy",
            "year": 2013,
            "volume": "77",
            "issue": "4",
            "pages": "551-557",
            "doi": "10.1016/j.gie.2012.11.022",
            "pmid": "23352447",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_MODERATE
        }
    ],
    
    "Rockall Score": [
        {
            "type": "primary",
            "title": "Risk assessment after acute upper gastrointestinal haemorrhage",
            "authors": "Rockall TA, Logan RF, Devlin HB, Northfield TC",
            "journal": "Gut",
            "year": 1996,
            "volume": "38",
            "issue": "3",
            "pages": "316-321",
            "doi": "10.1136/gut.38.3.316",
            "pmid": "8675081",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "Ranson": [
        {
            "type": "primary",
            "title": "Prognostic signs and the role of operative management in acute pancreatitis",
            "authors": "Ranson JH, Rifkind KM, Roses DF, Fink SD, Eng K, Spencer FC",
            "journal": "Surgery, Gynecology & Obstetrics",
            "year": 1974,
            "volume": "139",
            "issue": "1",
            "pages": "69-81",
            "pmid": "4834279",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "DIC Score": [
        {
            "type": "guideline",
            "title": "ISTH interim guidance on recognition and management of coagulopathy in COVID-19",
            "authors": "Thachil J, Tang N, Gando S, et al.",
            "journal": "Journal of Thrombosis and Haemostasis",
            "year": 2020,
            "volume": "18",
            "issue": "5",
            "pages": "1023-1026",
            "doi": "10.1111/jth.14810",
            "pmid": "32338827",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "primary",
            "title": "Towards definition, clinical and laboratory criteria, and a scoring system for disseminated intravascular coagulation",
            "authors": "Taylor FB Jr, Toh CH, Hoots WK, Wada H, Levi M",
            "journal": "Thrombosis and Haemostasis",
            "year": 2001,
            "volume": "86",
            "issue": "5",
            "pages": "1327-1330",
            "pmid": "11816725",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "RIFLE": [
        {
            "type": "primary",
            "title": "Acute renal failure - definition, outcome measures, animal models, fluid therapy and information technology needs: the Second International Consensus Conference of the Acute Dialysis Quality Initiative (ADQI) Group",
            "authors": "Bellomo R, Ronco C, Kellum JA, Mehta RL, Palevsky P",
            "journal": "Critical Care",
            "year": 2004,
            "volume": "8",
            "issue": "4",
            "pages": "R204-R212",
            "doi": "10.1186/cc2872",
            "pmid": "15312219",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "AKIN": [
        {
            "type": "primary",
            "title": "Acute Kidney Injury Network: report of an initiative to improve outcomes in acute kidney injury",
            "authors": "Mehta RL, Kellum JA, Shah SV, et al.",
            "journal": "Critical Care",
            "year": 2007,
            "volume": "11",
            "issue": "2",
            "pages": "R31",
            "doi": "10.1186/cc5713",
            "pmid": "17331245",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "NEXUS": [
        {
            "type": "primary",
            "title": "Validity of a set of clinical criteria to rule out injury to the cervical spine in patients with blunt trauma",
            "authors": "Hoffman JR, Mower WR, Wolfson AB, Todd KH, Zucker MI",
            "journal": "New England Journal of Medicine",
            "year": 2000,
            "volume": "343",
            "issue": "2",
            "pages": "94-99",
            "doi": "10.1056/NEJM200007133430203",
            "pmid": "10891516",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "Canadian C-Spine": [
        {
            "type": "primary",
            "title": "The Canadian C-spine rule for radiography in alert and stable trauma patients",
            "authors": "Stiell IG, Wells GA, Vandemheen KL, et al.",
            "journal": "JAMA",
            "year": 2001,
            "volume": "286",
            "issue": "15",
            "pages": "1841-1848",
            "doi": "10.1001/jama.286.15.1841",
            "pmid": "11597285",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "STOP-BANG": [
        {
            "type": "primary",
            "title": "STOP questionnaire: a tool to screen patients for obstructive sleep apnea",
            "authors": "Chung F, Yegneswaran B, Liao P, et al.",
            "journal": "Anesthesiology",
            "year": 2008,
            "volume": "108",
            "issue": "5",
            "pages": "812-821",
            "doi": "10.1097/ALN.0b013e31816d83e4",
            "pmid": "18431114",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "Epworth": [
        {
            "type": "primary",
            "title": "A new method for measuring daytime sleepiness: the Epworth sleepiness scale",
            "authors": "Johns MW",
            "journal": "Sleep",
            "year": 1991,
            "volume": "14",
            "issue": "6",
            "pages": "540-545",
            "doi": "10.1093/sleep/14.6.540",
            "pmid": "1798888",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "APGAR": [
        {
            "type": "primary",
            "title": "A proposal for a new method of evaluation of the newborn infant",
            "authors": "Apgar V",
            "journal": "Current Researches in Anesthesia & Analgesia",
            "year": 1953,
            "volume": "32",
            "issue": "4",
            "pages": "260-267",
            "pmid": "13083014",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "Preeclampsia": [
        {
            "type": "guideline",
            "title": "ACOG Practice Bulletin No. 202: Gestational Hypertension and Preeclampsia",
            "authors": "American College of Obstetricians and Gynecologists",
            "journal": "Obstetrics & Gynecology",
            "year": 2019,
            "volume": "133",
            "issue": "1",
            "pages": "e1-e25",
            "doi": "10.1097/AOG.0000000000003018",
            "pmid": "30575675",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "Bishop Score": [
        {
            "type": "primary",
            "title": "Pelvic scoring for elective induction",
            "authors": "Bishop EH",
            "journal": "Obstetrics & Gynecology",
            "year": 1964,
            "volume": "24",
            "issue": "2",
            "pages": "266-268",
            "pmid": "14199536",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "CrCl": [
        {
            "type": "primary",
            "title": "Prediction of creatinine clearance from serum creatinine",
            "authors": "Cockcroft DW, Gault MH",
            "journal": "Nephron",
            "year": 1976,
            "volume": "16",
            "issue": "1",
            "pages": "31-41",
            "doi": "10.1159/000180580",
            "pmid": "1244564",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "Osteoporosis": [
        {
            "type": "guideline",
            "title": "Clinician’s Guide to Prevention and Treatment of Osteoporosis",
            "authors": "National Osteoporosis Foundation",
            "year": 2024,
            "url": "https://www.nof.org",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "guideline",
            "title": "Pharmacological Management of Osteoporosis in Postmenopausal Women",
            "authors": "Endocrine Society Clinical Practice Guideline",
            "year": 2020,
            "doi": "10.1210/jc.2019-00221",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "guideline",
            "title": "AACE/ACE Clinical Practice Guidelines for the Diagnosis and Treatment of Postmenopausal Osteoporosis",
            "authors": "Camacho PM, et al.",
            "year": 2020,
            "doi": "10.4158/GL-2020-0524SUPPL",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "FRAX": [
        {
            "type": "primary",
            "title": "FRAX and the assessment of fracture probability in men and women from the UK",
            "authors": "Kanis JA, et al.",
            "journal": "Osteoporosis International",
            "year": 2008,
            "volume": "19",
            "issue": "4",
            "pages": "385-397",
            "doi": "10.1007/s00198-007-0543-5",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "guideline",
            "title": "NOGG Guideline for the Prevention and Treatment of Osteoporosis",
            "authors": "National Osteoporosis Guideline Group",
            "year": 2024,
            "url": "https://www.nogg.org.uk",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "Framingham": [
        {
            "type": "primary",
            "title": "General cardiovascular risk profile for use in primary care: the Framingham Heart Study",
            "authors": "D'Agostino RB Sr, Vasan RS, Pencina MJ, et al.",
            "journal": "Circulation",
            "year": 2008,
            "volume": "117",
            "issue": "6",
            "pages": "743-753",
            "doi": "10.1161/CIRCULATIONAHA.107.699579",
            "pmid": "18212285",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "Centor": [
        {
            "type": "primary",
            "title": "The diagnosis of strep throat in adults in the emergency room",
            "authors": "Centor RM, Witherspoon JM, Dalton HP, Brody CE, Link K",
            "journal": "Medical Decision Making",
            "year": 1981,
            "volume": "1",
            "issue": "3",
            "pages": "239-246",
            "doi": "10.1177/0272989X8100100304",
            "pmid": "6763125",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "FeverPAIN": [
        {
            "type": "primary",
            "title": "Clinical score for rapid detection of group A streptococcal pharyngitis",
            "authors": "Little P, Hobbs FD, Moore M, et al.",
            "journal": "BMJ",
            "year": 2013,
            "volume": "347",
            "pages": "f5060",
            "doi": "10.1136/bmj.f5060",
            "pmid": "23970166",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "SIRS": [
        {
            "type": "primary",
            "title": "American College of Chest Physicians/Society of Critical Care Medicine Consensus Conference: definitions for sepsis and organ failure and guidelines for the use of innovative therapies in sepsis",
            "authors": "American College of Chest Physicians/Society of Critical Care Medicine Consensus Conference Committee",
            "journal": "Critical Care Medicine",
            "year": 1992,
            "volume": "20",
            "issue": "6",
            "pages": "864-874",
            "doi": "10.1097/00003246-199206000-00025",
            "pmid": "1597042",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "MODS": [
        {
            "type": "primary",
            "title": "Multiple organ dysfunction score: a reliable descriptor of a complex clinical outcome",
            "authors": "Marshall JC, Cook DJ, Christou NV, Bernard GR, Sprung CL, Sibbald WJ",
            "journal": "Critical Care Medicine",
            "year": 1995,
            "volume": "23",
            "issue": "10",
            "pages": "1638-1652",
            "doi": "10.1097/00003246-199510000-00007",
            "pmid": "7584228",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "ASA": [
        {
            "type": "primary",
            "title": "New classification of physical status",
            "authors": "Dripps RD, Lamont A, Eckenhoff JE",
            "journal": "Anesthesiology",
            "year": 1963,
            "volume": "24",
            "pages": "111",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "guideline",
            "title": "ASA Physical Status Classification System",
            "authors": "American Society of Anesthesiologists",
            "journal": "ASA",
            "year": 2014,
            "url": "https://www.asahq.org/standards-and-guidelines/asa-physical-status-classification-system",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "RCRI": [
        {
            "type": "primary",
            "title": "Derivation and prospective validation of a simple index for prediction of cardiac risk of major noncardiac surgery",
            "authors": "Lee TH, Marcantonio ER, Mangione CM, et al.",
            "journal": "Circulation",
            "year": 1999,
            "volume": "100",
            "issue": "10",
            "pages": "1043-1049",
            "doi": "10.1161/01.cir.100.10.1043",
            "pmid": "10477528",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "Caprini": [
        {
            "type": "primary",
            "title": "Thrombosis risk assessment as a guide to quality patient care",
            "authors": "Caprini JA",
            "journal": "Disease-a-Month",
            "year": 2005,
            "volume": "51",
            "issue": "2-3",
            "pages": "70-78",
            "doi": "10.1016/j.disamonth.2005.02.003",
            "pmid": "15892287",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "PHQ-9": [
        {
            "type": "primary",
            "title": "The PHQ-9: validity of a brief depression severity measure",
            "authors": "Kroenke K, Spitzer RL, Williams JB",
            "journal": "Journal of General Internal Medicine",
            "year": 2001,
            "volume": "16",
            "issue": "9",
            "pages": "606-613",
            "doi": "10.1046/j.1525-1497.2001.016009606.x",
            "pmid": "11556941",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "GAD-7": [
        {
            "type": "primary",
            "title": "A brief measure for assessing generalized anxiety disorder: the GAD-7",
            "authors": "Spitzer RL, Kroenke K, Williams JB, Löwe B",
            "journal": "Archives of Internal Medicine",
            "year": 2006,
            "volume": "166",
            "issue": "10",
            "pages": "1092-1097",
            "doi": "10.1001/archinte.166.10.1092",
            "pmid": "16717171",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "MMSE": [
        {
            "type": "primary",
            "title": "Mini-mental state. A practical method for grading the cognitive state of patients for the clinician",
            "authors": "Folstein MF, Folstein SE, McHugh PR",
            "journal": "Journal of Psychiatric Research",
            "year": 1975,
            "volume": "12",
            "issue": "3",
            "pages": "189-198",
            "doi": "10.1016/0022-3956(75)90026-6",
            "pmid": "1202204",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "CAM": [
        {
            "type": "primary",
            "title": "Clarifying confusion: the confusion assessment method. A new method for detection of delirium",
            "authors": "Inouye SK, van Dyck CH, Alessi CA, Balkin S, Siegal AP, Horwitz RI",
            "journal": "Annals of Internal Medicine",
            "year": 1990,
            "volume": "113",
            "issue": "12",
            "pages": "941-948",
            "doi": "10.7326/0003-4819-113-12-941",
            "pmid": "2240918",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "Braden": [
        {
            "type": "primary",
            "title": "The Braden Scale for Predicting Pressure Sore Risk",
            "authors": "Bergstrom N, Braden BJ, Laguzza A, Holman V",
            "journal": "Nursing Research",
            "year": 1987,
            "volume": "36",
            "issue": "4",
            "pages": "205-210",
            "pmid": "3299278",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "Morse": [
        {
            "type": "primary",
            "title": "Predicting patient falls",
            "authors": "Morse JM, Black C, Oberle K, Donahue P",
            "journal": "American Journal of Nursing",
            "year": 1989,
            "volume": "89",
            "issue": "11",
            "pages": "1533-1536",
            "pmid": "2816900",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_STRONG
        }
    ],
    
    # Additional calculators
    "MELD-Na": [
        {
            "type": "primary",
            "title": "Serum sodium predicts mortality in patients listed for liver transplantation",
            "authors": "Biggins SW, Kim WR, Terrault NA, et al.",
            "journal": "Hepatology",
            "year": 2005,
            "volume": "42",
            "issue": "1",
            "pages": "79-88",
            "doi": "10.1002/hep.20737",
            "pmid": "15962315",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "ECOG": [
        {
            "type": "primary",
            "title": "Toxicity and response criteria of the Eastern Cooperative Oncology Group",
            "authors": "Oken MM, Creech RH, Tormey DC, et al.",
            "journal": "American Journal of Clinical Oncology",
            "year": 1982,
            "volume": "5",
            "issue": "6",
            "pages": "649-655",
            "pmid": "7165009",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "Karnofsky": [
        {
            "type": "primary",
            "title": "The clinical evaluation of chemotherapeutic agents in cancer",
            "authors": "Karnofsky DA, Burchenal JH",
            "journal": "Evaluation of Chemotherapeutic Agents",
            "year": 1949,
            "pages": "191-205",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "CIWA-Ar": [
        {
            "type": "primary",
            "title": "Assessment of alcohol withdrawal: the revised clinical institute withdrawal assessment for alcohol scale (CIWA-Ar)",
            "authors": "Sullivan JT, Sykora K, Schneiderman J, Naranjo CA, Sellers EM",
            "journal": "British Journal of Addiction",
            "year": 1989,
            "volume": "84",
            "issue": "11",
            "pages": "1353-1357",
            "doi": "10.1111/j.1360-0443.1989.tb00737.x",
            "pmid": "2597811",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "COWS": [
        {
            "type": "primary",
            "title": "The Clinical Opiate Withdrawal Scale (COWS)",
            "authors": "Wesson DR, Ling W",
            "journal": "Journal of Psychoactive Drugs",
            "year": 2003,
            "volume": "35",
            "issue": "2",
            "pages": "253-259",
            "doi": "10.1080/02791072.2003.10400007",
            "pmid": "12924748",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "MoCA": [
        {
            "type": "primary",
            "title": "The Montreal Cognitive Assessment, MoCA: a brief screening tool for mild cognitive impairment",
            "authors": "Nasreddine ZS, Phillips NA, Bédirian V, et al.",
            "journal": "Journal of the American Geriatrics Society",
            "year": 2005,
            "volume": "53",
            "issue": "4",
            "pages": "695-699",
            "doi": "10.1111/j.1532-5415.2005.53221.x",
            "pmid": "15817019",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "DAS28": [
        {
            "type": "primary",
            "title": "Modified disease activity scores that include twenty-eight-joint counts. Development and validation in a prospective longitudinal study of patients with rheumatoid arthritis",
            "authors": "Prevoo ML, van 't Hof MA, Kuper HH, van Leeuwen MA, van de Putte LB, van Riel PL",
            "journal": "Arthritis & Rheumatism",
            "year": 1995,
            "volume": "38",
            "issue": "1",
            "pages": "44-48",
            "doi": "10.1002/art.1780380107",
            "pmid": "7818570",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "CDAI": [
        {
            "type": "primary",
            "title": "The simplified disease activity index (SDAI) and the clinical disease activity index (CDAI): a review of their usefulness and validity in rheumatoid arthritis",
            "authors": "Aletaha D, Smolen J",
            "journal": "Clinical and Experimental Rheumatology",
            "year": 2005,
            "volume": "23",
            "issue": "5 Suppl 39",
            "pages": "S100-S108",
            "pmid": "16273793",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "SDAI": [
        {
            "type": "primary",
            "title": "The simplified disease activity index (SDAI) and the clinical disease activity index (CDAI): a review of their usefulness and validity in rheumatoid arthritis",
            "authors": "Aletaha D, Smolen J",
            "journal": "Clinical and Experimental Rheumatology",
            "year": 2005,
            "volume": "23",
            "issue": "5 Suppl 39",
            "pages": "S100-S108",
            "pmid": "16273793",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "ACR Criteria": [
        {
            "type": "guideline",
            "title": "2010 Rheumatoid arthritis classification criteria: an American College of Rheumatology/European League Against Rheumatism collaborative initiative",
            "authors": "Aletaha D, Neogi T, Silman AJ, et al.",
            "journal": "Arthritis & Rheumatism",
            "year": 2010,
            "volume": "62",
            "issue": "9",
            "pages": "2569-2581",
            "doi": "10.1002/art.27584",
            "pmid": "20872595",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "SLICC": [
        {
            "type": "primary",
            "title": "Derivation and validation of the Systemic Lupus International Collaborating Clinics classification criteria for systemic lupus erythematosus",
            "authors": "Petri M, Orbai AM, Alarcón GS, et al.",
            "journal": "Arthritis & Rheumatism",
            "year": 2012,
            "volume": "64",
            "issue": "8",
            "pages": "2677-2686",
            "doi": "10.1002/art.34473",
            "pmid": "22553077",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "SLEDAI": [
        {
            "type": "primary",
            "title": "Derivation of the SLEDAI. A disease activity index for lupus patients",
            "authors": "Bombardier C, Gladman DD, Urowitz MB, Caron D, Chang CH",
            "journal": "Arthritis & Rheumatism",
            "year": 1992,
            "volume": "35",
            "issue": "6",
            "pages": "630-640",
            "doi": "10.1002/art.1780350606",
            "pmid": "1599520",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "Gout Diagnostic": [
        {
            "type": "guideline",
            "title": "2015 Gout Classification Criteria: an American College of Rheumatology/European League Against Rheumatism collaborative initiative",
            "authors": "Neogi T, Jansen TL, Dalbeth N, et al.",
            "journal": "Arthritis & Rheumatology",
            "year": 2015,
            "volume": "67",
            "issue": "10",
            "pages": "2557-2568",
            "doi": "10.1002/art.39254",
            "pmid": "26352873",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "MASCC": [
        {
            "type": "primary",
            "title": "Multinational Association for Supportive Care in Cancer risk index: a multinational scoring system for identifying low-risk febrile neutropenic cancer patients",
            "authors": "Klastersky J, Paesmans M, Rubenstein EB, et al.",
            "journal": "Journal of Clinical Oncology",
            "year": 2000,
            "volume": "18",
            "issue": "16",
            "pages": "3038-3051",
            "doi": "10.1200/JCO.2000.18.16.3038",
            "pmid": "10944139",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "Pitt Bacteremia": [
        {
            "type": "primary",
            "title": "The Pittsburgh bacteremia score: a new scoring system for predicting mortality in patients with bacteremia",
            "authors": "Paterson DL, Ko WC, Von Gottberg A, et al.",
            "journal": "Clinical Infectious Diseases",
            "year": 2004,
            "volume": "38",
            "issue": "3",
            "pages": "357-364",
            "doi": "10.1086/380983",
            "pmid": "14727204",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "PASI": [
        {
            "type": "primary",
            "title": "Severity scoring of atopic dermatitis: the SCORAD index. Consensus Report of the European Task Force on Atopic Dermatitis",
            "authors": "European Task Force on Atopic Dermatitis",
            "journal": "Dermatology",
            "year": 1993,
            "volume": "186",
            "issue": "1",
            "pages": "23-31",
            "doi": "10.1159/000247298",
            "pmid": "8435513",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "SCORAD": [
        {
            "type": "primary",
            "title": "Severity scoring of atopic dermatitis: the SCORAD index. Consensus Report of the European Task Force on Atopic Dermatitis",
            "authors": "European Task Force on Atopic Dermatitis",
            "journal": "Dermatology",
            "year": 1993,
            "volume": "186",
            "issue": "1",
            "pages": "23-31",
            "doi": "10.1159/000247298",
            "pmid": "8435513",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "DLQI": [
        {
            "type": "primary",
            "title": "Dermatology Life Quality Index (DLQI)--a simple practical measure for routine clinical use",
            "authors": "Finlay AY, Khan GK",
            "journal": "Clinical and Experimental Dermatology",
            "year": 1994,
            "volume": "19",
            "issue": "3",
            "pages": "210-216",
            "doi": "10.1111/j.1365-2230.1994.tb01167.x",
            "pmid": "8033378",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "Parkland Formula": [
        {
            "type": "primary",
            "title": "The treatment of burn shock by the intravenous and oral administration of hypertonic lactated saline solution",
            "authors": "Baxter CR, Shires T",
            "journal": "Journal of Trauma",
            "year": 1968,
            "volume": "8",
            "issue": "5",
            "pages": "679-690",
            "pmid": "5652598",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "Burn TBSA": [
        {
            "type": "primary",
            "title": "The rule of nines",
            "authors": "Wallace AB",
            "journal": "Annals of Surgery",
            "year": 1951,
            "volume": "133",
            "issue": "4",
            "pages": "563-568",
            "pmid": "14819996",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "P-POSSUM": [
        {
            "type": "primary",
            "title": "POSSUM: a scoring system for surgical audit",
            "authors": "Copeland GP, Jones D, Walters M",
            "journal": "British Journal of Surgery",
            "year": 1991,
            "volume": "78",
            "issue": "3",
            "pages": "355-360",
            "doi": "10.1002/bjs.1800780329",
            "pmid": "2021856",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "Aldrete Score": [
        {
            "type": "primary",
            "title": "A postanesthetic recovery score",
            "authors": "Aldrete JA, Kroulik D",
            "journal": "Anesthesia & Analgesia",
            "year": 1970,
            "volume": "49",
            "issue": "6",
            "pages": "924-934",
            "pmid": "5534693",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "Mallampati": [
        {
            "type": "primary",
            "title": "A clinical sign to predict difficult tracheal intubation: a prospective study",
            "authors": "Mallampati SR, Gatt SP, Gugino LD, et al.",
            "journal": "Canadian Anaesthetists' Society Journal",
            "year": 1985,
            "volume": "32",
            "issue": "3 Pt 1",
            "pages": "429-434",
            "doi": "10.1007/BF03011357",
            "pmid": "4027773",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "Westley Croup": [
        {
            "type": "primary",
            "title": "The efficacy of nebulized racemic epinephrine in the treatment of croup",
            "authors": "Westley CR, Cotton EK, Brooks JG",
            "journal": "American Journal of Diseases of Children",
            "year": 1978,
            "volume": "132",
            "issue": "5",
            "pages": "484-487",
            "doi": "10.1001/archpedi.1978.02120300038008",
            "pmid": "645730",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "PEWS": [
        {
            "type": "primary",
            "title": "Development and initial validation of the Bedside Paediatric Early Warning System score",
            "authors": "Monaghan A",
            "journal": "Critical Care",
            "year": 2005,
            "volume": "9",
            "issue": "6",
            "pages": "R681-R689",
            "doi": "10.1186/cc3887",
            "pmid": "16356235",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "PELOD-2": [
        {
            "type": "primary",
            "title": "PELOD-2: an update of the PEdiatric logistic organ dysfunction score",
            "authors": "Leteurtre S, Duhamel A, Salleron J, et al.",
            "journal": "Critical Care Medicine",
            "year": 2013,
            "volume": "41",
            "issue": "9",
            "pages": "1761-1773",
            "doi": "10.1097/CCM.0b013e31828a2bbd",
            "pmid": "23887231",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "PRISM III": [
        {
            "type": "primary",
            "title": "PRISM III: an updated Pediatric Risk of Mortality score",
            "authors": "Pollack MM, Patel KM, Ruttimann UE",
            "journal": "Critical Care Medicine",
            "year": 1996,
            "volume": "24",
            "issue": "5",
            "pages": "743-752",
            "doi": "10.1097/00003246-199605000-00004",
            "pmid": "8706448",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "PIM2": [
        {
            "type": "primary",
            "title": "The Pediatric Index of Mortality 2 (PIM2): a revised version of the Pediatric Index of Mortality",
            "authors": "Slater A, Shann F, Pearson G",
            "journal": "Intensive Care Medicine",
            "year": 2003,
            "volume": "29",
            "issue": "2",
            "pages": "278-285",
            "doi": "10.1007/s00134-002-1601-2",
            "pmid": "12594588",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "Palliative Performance": [
        {
            "type": "primary",
            "title": "The Palliative Performance Scale (PPS) scoring system",
            "authors": "Anderson F, Downing GM, Hill J, Casorso L, Lerch N",
            "journal": "Journal of Palliative Care",
            "year": 1996,
            "volume": "12",
            "issue": "3",
            "pages": "5-11",
            "pmid": "8961127",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "NRS": [
        {
            "type": "primary",
            "title": "Pain assessment: the cornerstone to optimal pain management",
            "authors": "McCaffery M, Pasero C",
            "journal": "Proceedings",
            "year": 1999,
            "volume": "12",
            "issue": "3",
            "pages": "236-239",
            "pmid": "10558311",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "VAS": [
        {
            "type": "primary",
            "title": "The measurement of clinical pain intensity: a comparison of six methods",
            "authors": "Jensen MP, Karoly P, Braver S",
            "journal": "Pain",
            "year": 1986,
            "volume": "27",
            "issue": "1",
            "pages": "117-126",
            "doi": "10.1016/0304-3959(86)90228-9",
            "pmid": "3785962",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "FLACC": [
        {
            "type": "primary",
            "title": "The FLACC: a behavioral scale for scoring postoperative pain in young children",
            "authors": "Merkel SI, Voepel-Lewis T, Shayevitz JR, Malviya S",
            "journal": "Pediatric Nursing",
            "year": 1997,
            "volume": "23",
            "issue": "3",
            "pages": "293-297",
            "pmid": "9220806",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "NIPS": [
        {
            "type": "primary",
            "title": "The development of a tool to assess neonatal pain",
            "authors": "Lawrence J, Alcock D, McGrath P, Kay J, MacMurray SB, Dulberg C",
            "journal": "Neonatal Network",
            "year": 1993,
            "volume": "12",
            "issue": "6",
            "pages": "59-66",
            "pmid": "8413140",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "Wong-Baker": [
        {
            "type": "primary",
            "title": "Wong-Baker FACES Pain Rating Scale",
            "authors": "Wong DL, Baker CM",
            "journal": "Children's Pain Inventory",
            "year": 1988,
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "DN4": [
        {
            "type": "primary",
            "title": "Comparison of pain syndromes associated with nervous or somatic lesions and development of a new neuropathic pain diagnostic questionnaire (DN4)",
            "authors": "Bouhassira D, Attal N, Alchaar H, et al.",
            "journal": "Pain",
            "year": 2005,
            "volume": "114",
            "issue": "1-2",
            "pages": "29-36",
            "doi": "10.1016/j.pain.2004.12.010",
            "pmid": "15733628",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "Anion Gap": [
        {
            "type": "primary",
            "title": "Serum anion gap: its uses and limitations in clinical medicine",
            "authors": "Kraut JA, Madias NE",
            "journal": "Clinical Journal of the American Society of Nephrology",
            "year": 2007,
            "volume": "2",
            "issue": "1",
            "pages": "162-174",
            "doi": "10.2215/CJN.03020906",
            "pmid": "17699401",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "FENa": [
        {
            "type": "primary",
            "title": "Use of the fractional excretion of sodium in the diagnosis of acute renal failure",
            "authors": "Espinel CH",
            "journal": "New England Journal of Medicine",
            "year": 1976,
            "volume": "294",
            "issue": "15",
            "pages": "830-831",
            "doi": "10.1056/NEJM197604082941512",
            "pmid": "1256383",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "Osmolality": [
        {
            "type": "primary",
            "title": "Serum osmolality. Uses and limitations",
            "authors": "Dorwart WV, Chalmers L",
            "journal": "New England Journal of Medicine",
            "year": 1975,
            "volume": "292",
            "issue": "4",
            "pages": "194-199",
            "doi": "10.1056/NEJM197501232920406",
            "pmid": "1108010",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "Corrected Ca": [
        {
            "type": "primary",
            "title": "Corrected calcium: a method for calculating corrected calcium concentrations",
            "authors": "Payne RB, Little AJ, Williams RB, Milner JR",
            "journal": "British Medical Journal",
            "year": 1973,
            "volume": "3",
            "issue": "5876",
            "pages": "643-646",
            "doi": "10.1136/bmj.3.5876.643",
            "pmid": "4743073",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "HbA1c": [
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
    
    "Winter Formula": [
        {
            "type": "primary",
            "title": "The relationship of the concentration of the hydrogen ion and the carbon dioxide content of the blood",
            "authors": "Winter SD, Pearson JR, Gabow PA, Schultz AL, Lepoff RB",
            "journal": "Journal of Laboratory and Clinical Medicine",
            "year": 1990,
            "volume": "116",
            "issue": "4",
            "pages": "581-584",
            "pmid": "2212901",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "Free T4 Index": [
        {
            "type": "primary",
            "title": "Free thyroxine index: a reliable measure of thyroid function",
            "authors": "Clark F, Horn DB",
            "journal": "Journal of Clinical Endocrinology and Metabolism",
            "year": 1965,
            "volume": "25",
            "issue": "1",
            "pages": "39-45",
            "doi": "10.1210/jcem-25-1-39",
            "pmid": "14258264",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "BMI/IBW/BSA": [
        {
            "type": "primary",
            "title": "Indices of relative weight and obesity",
            "authors": "Keys A, Fidanza F, Karvonen MJ, Kimura N, Taylor HL",
            "journal": "Journal of Chronic Diseases",
            "year": 1972,
            "volume": "25",
            "issue": "6-7",
            "pages": "329-343",
            "doi": "10.1016/0021-9681(72)90027-6",
            "pmid": "4650929",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "Intraocular Pressure": [
        {
            "type": "primary",
            "title": "Central corneal thickness and measured IOP response to topical ocular hypotensive medication in the Ocular Hypertension Treatment Study",
            "authors": "Brandt JD, Beiser JA, Kass MA, Gordon MO",
            "journal": "American Journal of Ophthalmology",
            "year": 2004,
            "volume": "138",
            "issue": "5",
            "pages": "717-722",
            "doi": "10.1016/j.ajo.2004.06.037",
            "pmid": "15531301",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "Modified Bishop": [
        {
            "type": "primary",
            "title": "Pelvic scoring for elective induction",
            "authors": "Bishop EH",
            "journal": "Obstetrics & Gynecology",
            "year": 1964,
            "volume": "24",
            "issue": "2",
            "pages": "266-268",
            "pmid": "14199536",
            "evidence_level": EVIDENCE_LEVEL_IIA,
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
    
    "Pediatric SOFA": [
        {
            "type": "primary",
            "title": "The SOFA (Sepsis-related Organ Failure Assessment) score to describe organ dysfunction/failure",
            "authors": "Vincent JL, Moreno R, Takala J, et al.",
            "journal": "Intensive Care Medicine",
            "year": 1996,
            "volume": "22",
            "issue": "7",
            "pages": "707-710",
            "doi": "10.1007/BF01709751",
            "pmid": "8844239",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "SOFA-2 (2025)": [
        {
            "type": "primary",
            "title": "The SOFA (Sepsis-related Organ Failure Assessment) score to describe organ dysfunction/failure",
            "authors": "Vincent JL, Moreno R, Takala J, et al.",
            "journal": "Intensive Care Medicine",
            "year": 1996,
            "volume": "22",
            "issue": "7",
            "pages": "707-710",
            "doi": "10.1007/BF01709751",
            "pmid": "8844239",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
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
            "title": "High-flow oxygen through nasal cannula in acute hypoxemic respiratory failure",
            "authors": "Frat JP, Thille AW, Mercat A, et al.",
            "journal": "New England Journal of Medicine",
            "year": 2015,
            "volume": "372",
            "issue": "23",
            "pages": "2185-2196",
            "doi": "10.1056/NEJMoa1503326",
            "pmid": "25981908",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_MODERATE
        }
    ],
    
    "CIPN Grading": [
        {
            "type": "guideline",
            "title": "Common Terminology Criteria for Adverse Events (CTCAE) Version 5.0",
            "authors": "National Cancer Institute",
            "journal": "U.S. Department of Health and Human Services",
            "year": 2017,
            "url": "https://ctep.cancer.gov/protocoldevelopment/electronic_applications/ctc.htm",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "TRISS": [
        {
            "type": "primary",
            "title": "Evaluating trauma care: the TRISS method",
            "authors": "Boyd CR, Tolson MA, Copes WS",
            "journal": "Journal of Trauma",
            "year": 1987,
            "volume": "27",
            "issue": "4",
            "pages": "370-378",
            "doi": "10.1097/00005373-198704000-00005",
            "pmid": "3106646",
            "evidence_level": EVIDENCE_LEVEL_IIB,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "HOSPITAL Score": [
        {
            "type": "primary",
            "title": "Potentially avoidable 30-day hospital readmissions in medical patients: derivation and validation of the HOSPITAL score",
            "authors": "Donzé J, Aujesky D, Williams D, Schnipper JL",
            "journal": "Journal of Hospital Medicine",
            "year": 2013,
            "volume": "8",
            "issue": "9",
            "pages": "493-499",
            "doi": "10.1002/jhm.2063",
            "pmid": "23873718",
            "evidence_level": EVIDENCE_LEVEL_IIA,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "LACE Index": [
        {
            "type": "primary",
            "title": "Derivation of the LACE index to predict early death or unplanned readmission after discharge from hospital to the community",
            "authors": "van Walraven C, Dhalla IA, Bell C, et al.",
            "journal": "CMAJ",
            "year": 2010,
            "volume": "182",
            "issue": "6",
            "pages": "551-557",
            "doi": "10.1503/cmaj.091117",
            "pmid": "20194559",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "APACHE III": [
        {
            "type": "primary",
            "title": "The APACHE III prognostic system. Risk prediction of hospital mortality for critically ill hospitalized adults",
            "authors": "Knaus WA, Wagner DP, Draper EA, et al.",
            "journal": "Chest",
            "year": 1991,
            "volume": "100",
            "issue": "6",
            "pages": "1619-1636",
            "doi": "10.1378/chest.100.6.1619",
            "pmid": "1959406",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "LODS": [
        {
            "type": "primary",
            "title": "The Logistic Organ Dysfunction system. A new way to assess organ dysfunction in the intensive care unit",
            "authors": "Le Gall JR, Klar J, Lemeshow S, et al.",
            "journal": "JAMA",
            "year": 1996,
            "volume": "276",
            "issue": "10",
            "pages": "802-810",
            "doi": "10.1001/jama.1996.03540100046027",
            "pmid": "8769590",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "SAPS III": [
        {
            "type": "primary",
            "title": "SAPS 3—From evaluation of the patient to evaluation of the intensive care unit. Part 1: Objectives, methods and cohort description",
            "authors": "Moreno RP, Metnitz PG, Almeida E, et al.",
            "journal": "Intensive Care Medicine",
            "year": 2005,
            "volume": "31",
            "issue": "10",
            "pages": "1336-1344",
            "doi": "10.1007/s00134-005-2763-5",
            "pmid": "16132887",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "primary",
            "title": "SAPS 3—From evaluation of the patient to evaluation of the intensive care unit. Part 2: Development of a prognostic model for hospital mortality at ICU admission",
            "authors": "Metnitz PG, Moreno RP, Almeida E, et al.",
            "journal": "Intensive Care Medicine",
            "year": 2005,
            "volume": "31",
            "issue": "10",
            "pages": "1345-1355",
            "doi": "10.1007/s00134-005-2763-5",
            "pmid": "16132888",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ],
    
    "FOUR Score": [
        {
            "type": "primary",
            "title": "The FOUR score: a coma scale",
            "authors": "Wijdicks EF, Bamlet WR, Maramattom BV, Manno EM, McClelland RL",
            "journal": "Lancet Neurology",
            "year": 2005,
            "volume": "4",
            "issue": "7",
            "pages": "430-435",
            "doi": "10.1016/S1474-4422(05)70120-4",
            "pmid": "15963447",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        },
        {
            "type": "primary",
            "title": "Validation of a new coma scale: The FOUR score",
            "authors": "Wijdicks EF, Kramer AA, Rohs T Jr, et al.",
            "journal": "Annals of Neurology",
            "year": 2005,
            "volume": "58",
            "issue": "4",
            "pages": "585-593",
            "doi": "10.1002/ana.20611",
            "pmid": "16178024",
            "evidence_level": EVIDENCE_LEVEL_I,
            "strength": STRENGTH_STRONG
        }
    ]
}

# Backup and prune unused references (not currently called in codebase)
_UNUSED_REFERENCE_KEYS = [
    "4Ts Score", "ACR Criteria", "AKIN", "APGAR", "ARDS Berlin", "ASA",
    "ASCVD Risk", "BODE Index", "Barthel Index",
    "Bishop Score", "Braden", "Burn TBSA", "CDAI", "CIPN Grading", "Caprini",
    "Centor", "Corrected QT", "DAS28", "DIC Score",
    "DLQI", "DN4", "Duke", "ECOG", "Epworth", "FLACC", "FeverPAIN",
    "GRACE Score", "Gout Diagnostic", "HEART Score",
    "Intraocular Pressure", "KDIGO", "Karnofsky", "Killip", "MASCC",
    "Mallampati", "Modified Bishop", "Morse", "NIPS", "NRS",
    "P-POSSUM", "PASI", "PELOD-2", "PIM2", "PRISM III", "Padua",
    "Palliative Performance", "Parkland Formula", "Pediatric GCS",
    "Pediatric SOFA", "Pitt Bacteremia", "Preeclampsia", "RCRI", "RIFLE",
    "Ranson", "Rockall Score", "SCORAD", "SDAI", "SIRS", "SLEDAI", "SLICC",
    "SMART-COP", "STOP-BANG", "TIMI Risk", "VAS", "Wells DVT",
    "Westley Croup", "Wong-Baker", "mRS"
]

# Keep a backup dictionary for future use or reactivation
UNUSED_CALCULATOR_REFERENCES: Dict[str, List[Dict[str, Any]]] = {
    key: CALCULATOR_REFERENCES[key]
    for key in _UNUSED_REFERENCE_KEYS
    if key in CALCULATOR_REFERENCES
}

# Remove unused entries from active reference map
for key in list(UNUSED_CALCULATOR_REFERENCES.keys()):
    CALCULATOR_REFERENCES.pop(key, None)


def get_references(calculator_name: str) -> List[Dict[str, Any]]:
    """
    Get references for a specific calculator
    
    Args:
        calculator_name: Name of the calculator (e.g., "CHA2DS2-VASc", "Wells PE")
    
    Returns:
        List of reference dictionaries, empty list if not found
    """
    return CALCULATOR_REFERENCES.get(calculator_name, [])


def has_references(calculator_name: str) -> bool:
    """
    Check if a calculator has references
    
    Args:
        calculator_name: Name of the calculator
    
    Returns:
        True if references exist, False otherwise
    """
    return calculator_name in CALCULATOR_REFERENCES and len(CALCULATOR_REFERENCES[calculator_name]) > 0

