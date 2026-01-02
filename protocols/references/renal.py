"""
Protocol References - Renal
"""
from typing import List, Dict, Any
from components.references import (
    GRADE_HIGH, GRADE_MODERATE, GRADE_LOW,
    EVIDENCE_LEVEL_I, EVIDENCE_LEVEL_IIA, EVIDENCE_LEVEL_IIB,
    STRENGTH_STRONG, STRENGTH_MODERATE
)


RENAL_REFERENCES: Dict[str, List[Dict[str, Any]]] = {
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

        "UTI/Pyelonephritis": [
            {
                "type": "guideline",
                "title": "EAU Guidelines on Urological Infections 2024",
                "authors": "Bonkat G, Bartoletti R, Bruyère F, et al.",
                "journal": "European Association of Urology",
                "year": 2024,
                "url": "https://uroweb.org/guidelines/urological-infections",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "guideline",
                "title": "Clinical Practice Guideline for Acute Uncomplicated Cystitis and Pyelonephritis in Women",
                "authors": "Gupta K, Hooton TM, Naber KG, et al.",
                "journal": "Clinical Infectious Diseases",
                "year": 2011,
                "volume": "52",
                "issue": "5",
                "pages": "e103-e120",
                "doi": "10.1093/cid/ciq257",
                "pmid": "21292654",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "review",
                "title": "Acute pyelonephritis in adults",
                "authors": "Tunkel AR, Gupta K",
                "journal": "UpToDate",
                "year": 2024,
                "evidence_level": EVIDENCE_LEVEL_IIB,
                "strength": STRENGTH_MODERATE
            }
        ],

        "Nephrolithiasis": [
            {
                "type": "guideline",
                "title": "EAU Guidelines on Urolithiasis 2024",
                "authors": "Türk C, Neisius A, Petřík A, et al.",
                "journal": "European Association of Urology",
                "year": 2024,
                "url": "https://uroweb.org/guidelines/urolithiasis",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "guideline",
                "title": "Surgical Management of Stones: AUA/Endourology Society Guideline",
                "authors": "Assimos D, Krambeck A, Miller NL, et al.",
                "journal": "American Urological Association",
                "year": 2016,
                "doi": "10.1016/j.juro.2016.05.090",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "review",
                "title": "Acute management of kidney stones",
                "authors": "Pearle MS, Goldfarb DS",
                "journal": "UpToDate",
                "year": 2024,
                "evidence_level": EVIDENCE_LEVEL_IIB,
                "strength": STRENGTH_MODERATE
            }
        ],

        "BPH/Urinary Retention": [
            {
                "type": "guideline",
                "title": "EAU Guidelines on Management of Non-neurogenic Male LUTS (incl. BPH) 2024",
                "authors": "Gravas S, Cornu JN, Gacci M, et al.",
                "journal": "European Association of Urology",
                "year": 2024,
                "url": "https://uroweb.org/guidelines/management-of-non-neurogenic-male-luts",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "guideline",
                "title": "Benign Prostatic Hyperplasia (BPH) Guideline",
                "authors": "American Urological Association",
                "journal": "AUA Guideline",
                "year": 2023,
                "url": "https://www.auanet.org",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "review",
                "title": "Medical treatment of benign prostatic hyperplasia",
                "authors": "Roehrborn CG",
                "journal": "UpToDate",
                "year": 2024,
                "evidence_level": EVIDENCE_LEVEL_IIB,
                "strength": STRENGTH_MODERATE
            }
        ],

        "Chronic Glomerulonephritis": [
            {
                "type": "guideline",
                "title": "KDIGO 2021 Clinical Practice Guideline for the Management of Glomerular Diseases",
                "authors": "KDIGO Glomerular Diseases Work Group",
                "journal": "Kidney International",
                "year": 2021,
                "volume": "100",
                "issue": "4S",
                "pages": "S1-S276",
                "doi": "10.1016/j.kint.2021.05.021",
                "pmid": "34556256",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "guideline",
                "title": "KDIGO 2025 Clinical Practice Guideline for the Management of IgA Nephropathy and IgA Vasculitis",
                "authors": "KDIGO 2025 IgA Nephropathy Work Group",
                "journal": "Kidney International",
                "year": 2025,
                "volume": "107",
                "issue": "1S",
                "pages": "S1-S100",
                "doi": "10.1016/j.kint.2024.12.001",
                "pmid": "39848746",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG,
                "url": "https://kdigo.org/guidelines/iga-nephropathy/"
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
                "pmid": "25018975",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "review",
                "title": "Glomerulonephritis",
                "authors": "Couser WG",
                "journal": "The Lancet",
                "year": 1999,
                "volume": "353",
                "issue": "9163",
                "pages": "1509-1515",
                "doi": "10.1016/S0140-6736(98)06195-9",
                "pmid": "10232333",
                "evidence_level": EVIDENCE_LEVEL_IIA,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "review",
                "title": "Chronic glomerulonephritis",
                "authors": "Glassock RJ, Fervenza FC, Hebert L",
                "journal": "UpToDate",
                "year": 2024,
                "evidence_level": EVIDENCE_LEVEL_IIB,
                "strength": STRENGTH_MODERATE
            }
        ],

        "Nephrotic Syndrome": [
            {
                "type": "guideline",
                "title": "KDIGO 2021 Clinical Practice Guideline for the Management of Glomerular Diseases",
                "authors": "KDIGO Glomerular Diseases Work Group",
                "journal": "Kidney International",
                "year": 2021,
                "volume": "100",
                "issue": "4S",
                "pages": "S1-S276",
                "doi": "10.1016/j.kint.2021.05.021",
                "pmid": "34556256",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "guideline",
                "title": "Evidence-based clinical practice guidelines for nephrotic syndrome 2014",
                "authors": "Kodner C",
                "journal": "Pediatric Nephrology",
                "year": 2014,
                "volume": "29",
                "issue": "10",
                "pages": "1993-2005",
                "doi": "10.1007/s00467-014-2809-4",
                "pmid": "24752301",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "review",
                "title": "Nephrotic syndrome in adults",
                "authors": "Kodner C",
                "journal": "American Family Physician",
                "year": 2009,
                "volume": "80",
                "issue": "10",
                "pages": "1129-1134",
                "pmid": "19904897",
                "evidence_level": EVIDENCE_LEVEL_IIA,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "review",
                "title": "Nephrotic syndrome in adults: Diagnosis and management",
                "authors": "Kodner C, Thomas DB",
                "journal": "UpToDate",
                "year": 2024,
                "evidence_level": EVIDENCE_LEVEL_IIB,
                "strength": STRENGTH_MODERATE
            },
            {
                "type": "primary",
                "title": "Rituximab or Cyclosporine in the Treatment of Membranous Nephropathy",
                "authors": "Fervenza FC, Appel GB, Barbour SJ, et al.",
                "journal": "New England Journal of Medicine",
                "year": 2019,
                "volume": "381",
                "issue": "1",
                "pages": "36-47",
                "doi": "10.1056/NEJMoa1814427",
                "pmid": "31269364",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            }
        ],

        "CKD": [
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
                "pmid": "25018975",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "guideline",
                "title": "KDIGO 2021 Clinical Practice Guideline for the Management of Blood Pressure in Chronic Kidney Disease",
                "authors": "KDIGO 2021 Blood Pressure Work Group",
                "journal": "Kidney International",
                "year": 2021,
                "volume": "99",
                "issue": "3S",
                "pages": "S1-S87",
                "doi": "10.1016/j.kint.2020.11.003",
                "pmid": "33637192",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "guideline",
                "title": "KDIGO 2024 Clinical Practice Guideline for the Evaluation and Management of Chronic Kidney Disease",
                "authors": "KDIGO 2024 CKD Work Group",
                "journal": "Kidney International",
                "year": 2024,
                "volume": "105",
                "issue": "4S",
                "pages": "S1-S200",
                "doi": "10.1016/j.kint.2024.01.001",
                "pmid": "38500000",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG,
                "url": "https://kdigo.org/guidelines/ckd-evaluation-and-management/"
            },
            {
                "type": "review",
                "title": "Chronic kidney disease",
                "authors": "Levey AS, Coresh J",
                "journal": "The Lancet",
                "year": 2012,
                "volume": "379",
                "issue": "9811",
                "pages": "165-180",
                "doi": "10.1016/S0140-6736(11)60178-5",
                "pmid": "21840587",
                "evidence_level": EVIDENCE_LEVEL_IIA,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "review",
                "title": "Chronic kidney disease: Definition, epidemiology, and management",
                "authors": "Levey AS, Coresh J",
                "journal": "UpToDate",
                "year": 2024,
                "evidence_level": EVIDENCE_LEVEL_IIB,
                "strength": STRENGTH_MODERATE
            }
        ],

        "Diabetic Nephropathy": [
            {
                "type": "guideline",
                "title": "KDIGO 2020 Clinical Practice Guideline on Diabetes Management in Chronic Kidney Disease",
                "authors": "KDIGO 2020 Diabetes Work Group",
                "journal": "Kidney International",
                "year": 2020,
                "volume": "98",
                "issue": "4S",
                "pages": "S1-S115",
                "doi": "10.1016/j.kint.2020.06.019",
                "pmid": "32998798",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "guideline",
                "title": "KDIGO 2024 Clinical Practice Guideline for Diabetes Management in Chronic Kidney Disease",
                "authors": "KDIGO 2024 Diabetes Work Group",
                "journal": "Kidney International",
                "year": 2024,
                "volume": "105",
                "issue": "4S",
                "pages": "S1-S150",
                "doi": "10.1016/j.kint.2024.01.002",
                "pmid": "38500001",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG,
                "url": "https://kdigo.org/guidelines/diabetes-ckd/"
            },
            {
                "type": "guideline",
                "title": "Standards of Medical Care in Diabetes—2024",
                "authors": "American Diabetes Association",
                "journal": "Diabetes Care",
                "year": 2024,
                "volume": "47",
                "issue": "Supplement_1",
                "pages": "S1-S300",
                "doi": "10.2337/dc24-SINT",
                "pmid": "38078589",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "review",
                "title": "Diabetic kidney disease: Pathogenesis and epidemiology",
                "authors": "Tuttle KR, Bakris GL, Bilous RW, et al.",
                "journal": "Nature Reviews Disease Primers",
                "year": 2018,
                "volume": "4",
                "pages": "17018",
                "doi": "10.1038/nrdp.2017.18",
                "pmid": "29321625",
                "evidence_level": EVIDENCE_LEVEL_IIA,
                "strength": STRENGTH_STRONG
            },
            {
                "type": "review",
                "title": "Diabetic kidney disease: Pathogenesis and treatment",
                "authors": "Tuttle KR, Bakris GL, Bilous RW, et al.",
                "journal": "UpToDate",
                "year": 2024,
                "evidence_level": EVIDENCE_LEVEL_IIB,
                "strength": STRENGTH_MODERATE
            }
        ],

        "Hypertensive Nephrosclerosis": [
            {
                "type": "guideline",
                "title": "KDIGO 2021 Clinical Practice Guideline for the Management of Blood Pressure in Chronic Kidney Disease",
                "authors": "KDIGO 2021 Blood Pressure Work Group",
                "journal": "Kidney International",
                "year": 2021,
                "volume": "99",
                "issue": "3S",
                "pages": "S1-S87",
                "doi": "10.1016/j.kint.2020.11.003",
                "pmid": "33637192",
                "evidence_level": EVIDENCE_LEVEL_I,
                "strength": STRENGTH_STRONG
            },
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
                "type": "review",
                "title": "Hypertensive nephrosclerosis",
                "authors": "Meyrier A",
                "journal": "UpToDate",
                "year": 2024,
                "evidence_level": EVIDENCE_LEVEL_IIB,
                "strength": STRENGTH_MODERATE
            },
            {
                "type": "primary",
                "title": "Hypertensive nephrosclerosis: A cause of end-stage renal disease",
                "authors": "Freedman BI, Iskandar SS, Appel RG",
                "journal": "Nephrology Dialysis Transplantation",
                "year": 1995,
                "volume": "10",
                "issue": "2",
                "pages": "240-244",
                "pmid": "7753456",
                "evidence_level": EVIDENCE_LEVEL_IIA,
                "strength": STRENGTH_MODERATE
            }
        ],

}
