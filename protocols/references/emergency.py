"""
Protocol References - Emergency
"""
from typing import List, Dict, Any
from components.references import (
    GRADE_HIGH, GRADE_MODERATE, GRADE_LOW,
    EVIDENCE_LEVEL_I, EVIDENCE_LEVEL_IIA, EVIDENCE_LEVEL_IIB,
    STRENGTH_STRONG, STRENGTH_MODERATE
)


EMERGENCY_REFERENCES: Dict[str, List[Dict[str, Any]]] = {
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

}
