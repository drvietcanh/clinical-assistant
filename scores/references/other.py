"""
Calculator References - Other
"""
from typing import List, Dict, Any
from components.references import (
    GRADE_HIGH, GRADE_MODERATE, GRADE_LOW,
    EVIDENCE_LEVEL_I, EVIDENCE_LEVEL_IIA, EVIDENCE_LEVEL_IIB,
    STRENGTH_STRONG, STRENGTH_MODERATE
)


OTHER_REFERENCES: Dict[str, List[Dict[str, Any]]] = {
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
        ],

}
