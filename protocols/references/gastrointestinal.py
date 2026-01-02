"""
Protocol References - Gastrointestinal
"""
from typing import List, Dict, Any
from components.references import (
    GRADE_HIGH, GRADE_MODERATE, GRADE_LOW,
    EVIDENCE_LEVEL_I, EVIDENCE_LEVEL_IIA, EVIDENCE_LEVEL_IIB,
    STRENGTH_STRONG, STRENGTH_MODERATE
)


GASTROINTESTINAL_REFERENCES: Dict[str, List[Dict[str, Any]]] = {
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

}
