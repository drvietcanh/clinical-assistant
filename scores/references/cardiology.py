"""
Calculator References - Cardiology
"""
from typing import List, Dict, Any
from components.references import (
    GRADE_HIGH, GRADE_MODERATE, GRADE_LOW,
    EVIDENCE_LEVEL_I, EVIDENCE_LEVEL_IIA, EVIDENCE_LEVEL_IIB,
    STRENGTH_STRONG, STRENGTH_MODERATE
)


CARDIOLOGY_REFERENCES: Dict[str, List[Dict[str, Any]]] = {
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

        "EuroSCORE II": [
            {
                "type": "primary",
                "title": "EuroSCORE II",
                "authors": "Nashef SA, Roques F, Sharples LD, et al.",
                "journal": "European Journal of Cardio-Thoracic Surgery",
                "year": 2012,
                "volume": "41",
                "issue": "4",
                "pages": "734-744",
                "doi": "10.1093/ejcts/ezs043",
                "pmid": "22378855",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG,
                "url": "https://academic.oup.com/ejcts/article/41/4/734/284200"
            }
        ],

        "ATRIA Bleeding Risk": [
            {
                "type": "primary",
                "title": "A new risk scheme to predict warfarin-associated hemorrhage: The ATRIA (Anticoagulation and Risk Factors in Atrial Fibrillation) Study",
                "authors": "Fang MC, Go AS, Chang Y, et al.",
                "journal": "Journal of the American College of Cardiology",
                "year": 2011,
                "volume": "58",
                "issue": "4",
                "pages": "395-401",
                "doi": "10.1016/j.jacc.2011.03.031",
                "pmid": "21757117",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            }
        ],

        "ORBIT Bleeding Risk": [
            {
                "type": "primary",
                "title": "The ORBIT bleeding score: a simple bedside score to assess bleeding risk in atrial fibrillation",
                "authors": "O'Brien EC, Simon DN, Thomas LE, et al.",
                "journal": "European Heart Journal",
                "year": 2015,
                "volume": "36",
                "issue": "46",
                "pages": "3258-3264",
                "doi": "10.1093/eurheartj/ehv476",
                "pmid": "26330425",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            }
        ],

        "SAMe-TT₂R₂": [
            {
                "type": "primary",
                "title": "The SAMe-TT2R2 score: a predictor of poor response to warfarin anticoagulation in patients with atrial fibrillation",
                "authors": "Apostolakis S, Sullivan RM, Olshansky B, Lip GY",
                "journal": "American Journal of Medicine",
                "year": 2013,
                "volume": "126",
                "issue": "5",
                "pages": "423.e9-423.e15",
                "doi": "10.1016/j.amjmed.2012.10.020",
                "pmid": "23561641",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            }
        ],

        "Duke Treadmill": [
            {
                "type": "primary",
                "title": "Prognostic value of a treadmill exercise score in outpatients with suspected coronary artery disease",
                "authors": "Mark DB, Shaw L, Harrell FE Jr, et al.",
                "journal": "New England Journal of Medicine",
                "year": 1991,
                "volume": "325",
                "issue": "12",
                "pages": "849-853",
                "doi": "10.1056/NEJM199109193251204",
                "pmid": "1875969",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            }
        ],

}
