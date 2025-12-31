"""
Clinical Guidelines Database
Major clinical practice guidelines from international organizations
"""

from typing import List, Optional
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Guideline:
    """Clinical guideline information"""
    id: str
    title: str
    title_vn: str  # Vietnamese title
    organization: str  # AHA, ACC, ESC, IDSA, etc.
    year: int
    category: str  # Cardiology, Infectious, etc.
    version: str = "1.0"
    last_updated: str = ""  # Date string
    url: str = ""
    related_protocol: Optional[str] = None  # Link to protocol in app
    description: str = ""
    key_recommendations: List[str] = None  # List of key recommendations
    is_high_impact: bool = False # Highlights "Practice Changing" updates
    related_tools: List[dict] = None # List of dicts: {"name": "Calculators...", "url": "..."}
    
    def __post_init__(self):
        if self.key_recommendations is None:
            self.key_recommendations = []
        if self.related_tools is None:
            self.related_tools = []


# Guidelines Database
# Major clinical practice guidelines from international organizations
GUIDELINES_DATABASE: List[Guideline] = [
    # === CARDIOLOGY ===
    Guideline(
        id="acc_aha_heart_failure_2022",
        title="2022 AHA/ACC/HFSA Heart Failure Guideline",
        title_vn="Hướng dẫn Suy tim 2022 AHA/ACC/HFSA",
        organization="AHA/ACC/HFSA",
        year=2022,
        category="Cardiology",
        version="2022",
        last_updated="2022-04-01",
        url="https://www.ahajournals.org/doi/10.1161/CIR.0000000000001063",
        related_protocol="Suy tim Cấp",
        description="Comprehensive guideline for diagnosis and management of heart failure",
        key_recommendations=[
            "Classification: HFrEF, HFmrEF, HFpEF",
            "ARNI/ACEi/ARB for HFrEF",
            "Beta-blockers for HFrEF",
            "SGLT2 inhibitors for HFrEF"
        ]
    ),
    Guideline(
        id="acc_aha_acs_2023",
        title="2023 ACC/AHA Guideline for the Management of Patients With Acute Coronary Syndromes",
        title_vn="Hướng dẫn Quản lý Hội chứng vành cấp 2023 ACC/AHA",
        organization="ACC/AHA",
        year=2023,
        category="Cardiology",
        version="2023",
        last_updated="2023-11-30",
        url="https://www.ahajournals.org/doi/10.1161/CIR.0000000000001168",
        related_protocol="ACS - Hội chứng vành cấp",
        description="Guideline for management of ACS including STEMI and NSTEMI",
        key_recommendations=[
            "Dual antiplatelet therapy",
            "Early revascularization for STEMI",
            "Risk stratification for NSTEMI"
        ]
    ),
    Guideline(
        id="esc_heart_failure_2021",
        title="2021 ESC Guidelines for the diagnosis and treatment of acute and chronic heart failure",
        title_vn="Hướng dẫn ESC 2021 về chẩn đoán và điều trị suy tim cấp và mạn",
        organization="ESC",
        year=2021,
        category="Cardiology",
        version="2021",
        last_updated="2021-08-27",
        url="https://www.escardio.org/Guidelines/Clinical-Practice-Guidelines",
        related_protocol="Suy tim Cấp",
        description="European Society of Cardiology heart failure guidelines",
        key_recommendations=[
            "ACEi/ARB/ARNI for HFrEF (LVEF ≤40%)",
            "Beta-blockers (bisoprolol, carvedilol, metoprolol) for HFrEF",
            "MRA (spironolactone/eplerenone) for HFrEF",
            "SGLT2 inhibitors (dapagliflozin/empagliflozin) for HFrEF"
        ]
    ),
    Guideline(
        id="acc_aha_hypertension_2017",
        title="2017 ACC/AHA/AAPA/ABC/ACPM/AGS/APhA/ASH/ASPC/NMA/PCNA Guideline for the Prevention, Detection, Evaluation, and Management of High Blood Pressure in Adults",
        title_vn="Hướng dẫn Phòng ngừa, Phát hiện, Đánh giá và Quản lý Tăng huyết áp ở Người lớn 2017",
        organization="ACC/AHA",
        year=2017,
        category="Cardiology",
        version="2017",
        last_updated="2017-11-13",
        url="https://www.ahajournals.org/doi/10.1161/HYP.0000000000000065",
        description="Hypertension guideline with new BP thresholds (130/80 mmHg)",
        key_recommendations=[
            "BP threshold: ≥130/80 mmHg for hypertension diagnosis",
            "Target BP <130/80 mmHg for most adults",
            "ACEi/ARB, CCB, or thiazide diuretic as first-line",
            "Two-drug combination if BP >20/10 mmHg above goal"
        ]
    ),
    Guideline(
        id="acc_aha_atrial_fibrillation_2019",
        title="2019 AHA/ACC/HRS Focused Update of the 2014 AHA/ACC/HRS Guideline for the Management of Patients With Atrial Fibrillation",
        title_vn="Cập nhật Hướng dẫn Quản lý Rung nhĩ 2019 AHA/ACC/HRS",
        organization="AHA/ACC/HRS",
        year=2019,
        category="Cardiology",
        version="2019",
        last_updated="2019-01-28",
        url="https://www.ahajournals.org/doi/10.1161/CIR.0000000000000665",
        related_protocol="Rung Nhĩ (Atrial Fibrillation)",
        description="Atrial fibrillation management including anticoagulation",
        key_recommendations=[
            "CHA2DS2-VASc for stroke risk, HAS-BLED for bleeding risk",
            "Anticoagulation: DOACs preferred over warfarin",
            "Rate control: Beta-blockers, diltiazem, verapamil, digoxin",
            "Rhythm control: Cardioversion, antiarrhythmics, ablation"
        ],
        related_tools=[
            {"name": "CHA2DS2-VASc", "url": "/Scores?calc=CHA2DS2-VASc"},
            {"name": "HAS-BLED", "url": "/Scores?calc=HAS-BLED"}
        ]
    ),
    
    # === INFECTIOUS DISEASES ===
    Guideline(
        id="idsa_cap_2019",
        title="2019 IDSA/ATS Clinical Practice Guidelines for Community-Acquired Pneumonia",
        title_vn="Hướng dẫn Thực hành Lâm sàng Viêm phổi Cộng đồng 2019 IDSA/ATS",
        organization="IDSA/ATS",
        year=2019,
        category="Infectious",
        version="2019",
        last_updated="2019-10-01",
        url="https://www.idsociety.org/practice-guideline/community-acquired-pneumonia/",
        related_protocol="Viêm phổi cộng đồng (CAP)",
        description="Community-acquired pneumonia diagnosis and treatment",
        key_recommendations=[
            "Amoxicillin 1g TID or doxycycline for outpatient",
            "Beta-lactam + macrolide or respiratory fluoroquinolone for inpatient",
            "Duration: 5-7 days for most patients",
            "Switch to oral when clinically stable"
        ],
        related_tools=[
            {"name": "CURB-65", "url": "/Scores?calc=CURB-65"},
            {"name": "PSI/PORT", "url": "/Scores?calc=PSI/PORT"}
        ]
    ),
    Guideline(
        id="idsa_sepsis_2016",
        title="2016 Surviving Sepsis Campaign: International Guidelines for Management of Sepsis and Septic Shock",
        title_vn="Chiến dịch Sống sót Sepsis 2016: Hướng dẫn Quốc tế Quản lý Sepsis và Sốc nhiễm khuẩn",
        organization="SSC",
        year=2016,
        category="Infectious",
        version="2016",
        last_updated="2017-01-18",
        url="https://www.sccm.org/SurvivingSepsisCampaign/Guidelines/Adult-Patients",
        related_protocol="Sepsis 1-Hour Bundle",
        description="Sepsis and septic shock management (1-hour bundle)"
    ),
    Guideline(
        id="idsa_sepsis_2021",
        title="Surviving Sepsis Campaign: International Guidelines for Management of Sepsis and Septic Shock 2021",
        title_vn="Chiến dịch Sống sót Sepsis: Hướng dẫn Quốc tế 2021",
        organization="SSC",
        year=2021,
        category="Infectious",
        version="2021",
        last_updated="2021-10-01",
        url="https://www.sccm.org/SurvivingSepsisCampaign/Guidelines/Adult-Patients",
        related_protocol="Sepsis 1-Hour Bundle",
        description="Updated sepsis guidelines 2021",
        key_recommendations=[
            "1-hour bundle: Measure lactate, obtain cultures, start antibiotics, give fluids",
            "Antibiotics within 1 hour of recognition",
            "30 mL/kg crystalloid for hypotension or lactate ≥4",
            "Norepinephrine as first-line vasopressor"
        ],
        related_tools=[
            {"name": "qSOFA", "url": "/Scores?calc=qSOFA"},
            {"name": "SOFA", "url": "/Scores?calc=SOFA"}
        ]
    ),
    
    # === RESPIRATORY ===
    Guideline(
        id="gold_copd_2024",
        title="Global Strategy for the Diagnosis, Management, and Prevention of Chronic Obstructive Pulmonary Disease 2024",
        title_vn="Chiến lược Toàn cầu Chẩn đoán, Quản lý và Phòng ngừa COPD 2024",
        organization="GOLD",
        year=2024,
        category="Respiratory",
        version="2024",
        last_updated="2024-01-01",
        url="https://goldcopd.org/2024-gold-report/",
        related_protocol="COPD Exacerbation",
        description="GOLD guidelines for COPD management"
    ),
    Guideline(
        id="gina_asthma_2024",
        title="Global Strategy for Asthma Management and Prevention 2024",
        title_vn="Chiến lược Toàn cầu Quản lý và Phòng ngừa Hen phế quản 2024",
        organization="GINA",
        year=2024,
        category="Respiratory",
        version="2024",
        last_updated="2024-01-01",
        url="https://ginasthma.org/",
        related_protocol="Cơn hen cấp",
        description="GINA guidelines for asthma management",
        key_recommendations=[
            "ICS-formoterol as both maintenance and reliever (MART)",
            "Step-up therapy based on symptom control",
            "SABA-only treatment not recommended",
            "Biologics for severe uncontrolled asthma"
        ]
    ),
    
    # === NEPHROLOGY ===
    Guideline(
        id="kdigo_aki_2012",
        title="KDIGO Clinical Practice Guideline for Acute Kidney Injury 2012",
        title_vn="Hướng dẫn Thực hành Lâm sàng KDIGO về Tổn thương Thận Cấp 2012",
        organization="KDIGO",
        year=2012,
        category="Nephrology",
        version="2012",
        last_updated="2012-03-01",
        url="https://kdigo.org/guidelines/acute-kidney-injury/",
        related_protocol="AKI Management",
        description="KDIGO AKI guidelines",
        key_recommendations=[
            "AKI definition: Increase in SCr ≥0.3 mg/dL or ≥1.5x baseline",
            "Avoid nephrotoxic agents when possible",
            "Optimize volume status and hemodynamics",
            "RRT when life-threatening complications present"
        ]
    ),
    Guideline(
        id="kdigo_ckd_2012",
        title="KDIGO 2012 Clinical Practice Guideline for the Evaluation and Management of Chronic Kidney Disease",
        title_vn="Hướng dẫn Thực hành Lâm sàng KDIGO 2012 về Đánh giá và Quản lý Bệnh thận Mạn tính",
        organization="KDIGO",
        year=2012,
        category="Nephrology",
        version="2012",
        last_updated="2013-01-03",
        url="https://kdigo.org/guidelines/ckd-evaluation-and-management/",
        related_protocol="Suy thận mạn tính (CKD)",
        description="KDIGO CKD guidelines",
        key_recommendations=[
            "CKD definition: eGFR <60 or kidney damage ≥3 months",
            "ACEi/ARB for proteinuria (albuminuria >30 mg/g)",
            "BP target <130/80 mmHg for CKD with diabetes or proteinuria",
            "Avoid NSAIDs in advanced CKD"
        ]
    ),
    
    # === ENDOCRINOLOGY ===
    Guideline(
        id="ada_diabetes_2024",
        title="Standards of Care in Diabetes—2024",
        title_vn="Tiêu chuẩn Chăm sóc Đái tháo đường—2024",
        organization="ADA",
        year=2024,
        category="Endocrinology",
        version="2024",
        last_updated="2024-01-01",
        url="https://diabetesjournals.org/care/issue/47/Supplement_1",
        description="American Diabetes Association standards of care",
        key_recommendations=[
            "HbA1c target <7% for most adults, <8% for frail elderly",
            "SGLT2 inhibitors or GLP-1 RAs for CV/renal protection",
            "Blood pressure <130/80 mmHg",
            "Statin therapy for all diabetes patients >40 years or with CV risk factors"
        ]
    ),
    
    # === NEUROLOGY ===
    Guideline(
        id="aha_stroke_2019",
        title="2019 Update to the 2018 Guidelines for the Early Management of Patients With Acute Ischemic Stroke",
        title_vn="Cập nhật 2019 Hướng dẫn Quản lý Sớm Bệnh nhân Đột quỵ Thiếu máu Cục bộ Cấp",
        organization="AHA/ASA",
        year=2019,
        category="Neurology",
        version="2019",
        last_updated="2019-05-01",
        url="https://www.ahajournals.org/doi/10.1161/STR.0000000000000211",
        related_protocol="Stroke Management",
        description="Acute ischemic stroke management guidelines",
        key_recommendations=[
            "IV tPA within 4.5 hours of symptom onset (0.9 mg/kg)",
            "Mechanical thrombectomy within 24 hours for large vessel occlusion",
            "BP management: <185/110 before tPA, <180/105 after",
            "Aspirin 325 mg within 24-48 hours (avoid if tPA given)"
        ],
        is_high_impact=True,
        related_tools=[
            {"name": "NIHSS", "url": "/Scores?calc=NIHSS"},
            {"name": "ASPECTS", "url": "/Scores?calc=ASPECTS"}
        ]
    ),
    
    # === CRITICAL CARE ===
    Guideline(
        id="ardsnet_2000",
        title="Ventilation with Lower Tidal Volumes as Compared with Traditional Tidal Volumes for Acute Lung Injury and the Acute Respiratory Distress Syndrome",
        title_vn="Thông khí với Thể tích Khí lưu thông Thấp hơn so với Thể tích Truyền thống cho Tổn thương Phổi Cấp và Hội chứng Suy hô hấp Cấp",
        organization="ARDSNet",
        year=2000,
        category="Critical Care",
        version="2000",
        last_updated="2000-05-04",
        url="https://www.nejm.org/doi/full/10.1056/NEJM200005043421801",
        description="ARDSNet low tidal volume ventilation protocol",
        key_recommendations=[
            "Tidal volume 6 mL/kg predicted body weight (PBW)",
            "Plateau pressure <30 cmH2O",
            "PEEP/FiO2 table for PEEP titration",
            "Permissive hypercapnia (pH ≥7.15)"
        ]
    ),
    
    # === EMERGENCY ===
    Guideline(
        id="aha_acls_2020",
        title="2020 American Heart Association Guidelines for Cardiopulmonary Resuscitation and Emergency Cardiovascular Care",
        title_vn="Hướng dẫn 2020 Hiệp hội Tim mạch Hoa Kỳ về Hồi sức Tim phổi và Chăm sóc Tim mạch Cấp cứu",
        organization="AHA",
        year=2020,
        category="Emergency",
        version="2020",
        last_updated="2020-10-21",
        url="https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines",
        related_protocol="Cardiac Arrest / ACLS",
        description="ACLS guidelines 2020",
        key_recommendations=[
            "High-quality CPR: 100-120 compressions/min, depth 5-6 cm",
            "Early defibrillation for shockable rhythms",
            "Epinephrine 1mg IV/IO every 3-5 minutes",
            "Amiodarone for VF/pulseless VT"
        ]
    ),
    
    # === ADDITIONAL CARDIOLOGY GUIDELINES ===
    Guideline(
        id="acc_aha_cholesterol_2018",
        title="2018 AHA/ACC/AACVPR/AAPA/ABC/ACPM/ADA/AGS/APhA/ASPC/NLA/PCNA Guideline on the Management of Blood Cholesterol",
        title_vn="Hướng dẫn 2018 AHA/ACC về Quản lý Cholesterol Máu",
        organization="ACC/AHA",
        year=2018,
        category="Cardiology",
        version="2018",
        last_updated="2018-11-10",
        url="https://www.ahajournals.org/doi/10.1161/CIR.0000000000000625",
        description="Blood cholesterol management and statin therapy guidelines",
        key_recommendations=[
            "High-intensity statin for ASCVD patients",
            "Moderate-intensity statin for primary prevention (10-year ASCVD risk ≥7.5%)",
            "LDL-C goal <70 mg/dL for very high risk",
            "Consider ezetimibe or PCSK9 inhibitors if statin intolerant"
        ]
    ),
    Guideline(
        id="esc_acs_2020",
        title="2020 ESC Guidelines for the management of acute coronary syndromes in patients presenting without persistent ST-segment elevation",
        title_vn="Hướng dẫn ESC 2020 về Quản lý Hội chứng vành cấp ở Bệnh nhân không có ST chênh lên",
        organization="ESC",
        year=2020,
        category="Cardiology",
        version="2020",
        last_updated="2020-08-29",
        url="https://www.escardio.org/Guidelines/Clinical-Practice-Guidelines",
        related_protocol="ACS - Hội chứng vành cấp",
        description="European guidelines for NSTEMI/UA management",
        key_recommendations=[
            "Dual antiplatelet therapy (aspirin + P2Y12 inhibitor)",
            "Early invasive strategy for high-risk patients",
            "Ticagrelor or prasugrel preferred over clopidogrel",
            "Risk stratification using GRACE or CRUSADE score"
        ]
    ),
    Guideline(
        id="acc_aha_valvular_2020",
        title="2020 ACC/AHA Guideline for the Management of Patients With Valvular Heart Disease",
        title_vn="Hướng dẫn 2020 ACC/AHA về Quản lý Bệnh nhân Bệnh van Tim",
        organization="ACC/AHA",
        year=2020,
        category="Cardiology",
        version="2020",
        last_updated="2020-12-17",
        url="https://www.ahajournals.org/doi/10.1161/CIR.0000000000000923",
        description="Comprehensive valvular heart disease management",
        key_recommendations=[
            "Aortic stenosis: TAVR for high-risk, SAVR for low-risk",
            "Mitral regurgitation: Surgery for severe primary MR",
            "Anticoagulation for mechanical valves (warfarin)",
            "Echocardiography for diagnosis and monitoring"
        ]
    ),
    
    # === ADDITIONAL INFECTIOUS DISEASES ===
    Guideline(
        id="idsa_hap_2016",
        title="2016 IDSA/ATS Guidelines for Hospital-Acquired and Ventilator-Associated Pneumonia",
        title_vn="Hướng dẫn 2016 IDSA/ATS về Viêm phổi Bệnh viện và Liên quan Thở máy",
        organization="IDSA/ATS",
        year=2016,
        category="Infectious",
        version="2016",
        last_updated="2016-07-14",
        url="https://www.idsociety.org/practice-guideline/hap-vap/",
        related_protocol="HAP/VAP Guidelines",
        description="Hospital-acquired and ventilator-associated pneumonia management",
        key_recommendations=[
            "Empiric antibiotics based on local resistance patterns",
            "De-escalation after culture results",
            "Short course (7-8 days) for most patients",
            "MRSA coverage if risk factors present"
        ]
    ),
    Guideline(
        id="idsa_uti_2010",
        title="2010 IDSA Guidelines for the Diagnosis and Treatment of Asymptomatic Bacteriuria",
        title_vn="Hướng dẫn 2010 IDSA về Chẩn đoán và Điều trị Nhiễm khuẩn Niệu không Triệu chứng",
        organization="IDSA",
        year=2010,
        category="Infectious",
        version="2010",
        last_updated="2010-03-01",
        url="https://www.idsociety.org/practice-guideline/asymptomatic-bacteriuria/",
        description="Asymptomatic bacteriuria management",
        key_recommendations=[
            "Treat only in pregnancy and before urologic procedures",
            "Do not treat in non-pregnant women, elderly, or catheterized patients",
            "Nitrofurantoin or TMP-SMX for treatment when indicated"
        ]
    ),
    Guideline(
        id="idsa_cdi_2017",
        title="2017 IDSA/SHEA Clinical Practice Guidelines for Clostridium difficile Infection",
        title_vn="Hướng dẫn Thực hành Lâm sàng 2017 IDSA/SHEA về Nhiễm Clostridium difficile",
        organization="IDSA/SHEA",
        year=2017,
        category="Infectious",
        version="2017",
        last_updated="2017-02-15",
        url="https://www.idsociety.org/practice-guideline/c-difficile/",
        description="C. difficile infection diagnosis and treatment",
        key_recommendations=[
            "Vancomycin or fidaxomicin for initial episode",
            "Metronidazole only for mild-moderate if vancomycin unavailable",
            "Fecal microbiota transplantation for recurrent CDI",
            "Discontinue inciting antibiotics when possible"
        ]
    ),
    
    # === ADDITIONAL RESPIRATORY ===
    Guideline(
        id="ats_ards_2017",
        title="2017 ATS/ESICM/SCCM Clinical Practice Guideline: Mechanical Ventilation in Adult Patients with Acute Respiratory Distress Syndrome",
        title_vn="Hướng dẫn Thực hành Lâm sàng 2017 ATS/ESICM/SCCM: Thông khí Cơ học ở Bệnh nhân Người lớn ARDS",
        organization="ATS/ESICM/SCCM",
        year=2017,
        category="Critical Care",
        version="2017",
        last_updated="2017-05-01",
        url="https://www.atsjournals.org/doi/10.1164/rccm.201703-0546ST",
        related_protocol="ARDS Management",
        description="Mechanical ventilation strategies for ARDS",
        key_recommendations=[
            "Low tidal volume ventilation (6 ml/kg PBW)",
            "Plateau pressure <30 cmH2O",
            "Prone positioning for severe ARDS (P/F <150)",
            "Neuromuscular blockade for first 48 hours if needed"
        ]
    ),
    
    # === ADDITIONAL NEPHROLOGY ===
    Guideline(
        id="kdigo_ckd_2020",
        title="KDIGO 2020 Clinical Practice Guideline for Diabetes Management in Chronic Kidney Disease",
        title_vn="Hướng dẫn Thực hành Lâm sàng KDIGO 2020 về Quản lý Đái tháo đường trong Bệnh thận Mạn",
        organization="KDIGO",
        year=2020,
        category="Nephrology",
        version="2020",
        last_updated="2020-10-01",
        url="https://kdigo.org/guidelines/diabetes-ckd/",
        description="Diabetes management in CKD patients",
        key_recommendations=[
            "SGLT2 inhibitors for CKD with eGFR ≥25",
            "Metformin if eGFR ≥30, avoid if <30",
            "ACEi/ARB for proteinuria",
            "HbA1c target 6.5-8% for advanced CKD"
        ]
    ),
    Guideline(
        id="kdigo_anemia_2012",
        title="KDIGO 2012 Clinical Practice Guideline for Anemia in Chronic Kidney Disease",
        title_vn="Hướng dẫn Thực hành Lâm sàng KDIGO 2012 về Thiếu máu trong Bệnh thận Mạn",
        organization="KDIGO",
        year=2012,
        category="Nephrology",
        version="2012",
        last_updated="2012-08-01",
        url="https://kdigo.org/guidelines/anemia-in-ckd/",
        description="Anemia management in CKD",
        key_recommendations=[
            "ESA therapy when Hb <10 g/dL",
            "Target Hb 10-11.5 g/dL (avoid >13 g/dL)",
            "Iron supplementation to maintain ferritin >100-500 ng/mL",
            "Consider iron if TSAT <30%"
        ]
    ),
    
    # === ADDITIONAL ENDOCRINOLOGY ===
    Guideline(
        id="ada_diabetes_2023",
        title="Standards of Care in Diabetes—2023",
        title_vn="Tiêu chuẩn Chăm sóc Đái tháo đường—2023",
        organization="ADA",
        year=2023,
        category="Endocrinology",
        version="2023",
        last_updated="2023-01-01",
        url="https://diabetesjournals.org/care/issue/46/Supplement_1",
        description="American Diabetes Association comprehensive diabetes care standards",
        key_recommendations=[
            "HbA1c target <7% for most adults",
            "SGLT2 inhibitors or GLP-1 RAs for CV/renal protection",
            "Blood pressure target <130/80 mmHg",
            "Statin therapy for all diabetes patients >40 years"
        ]
    ),
    Guideline(
        id="ada_dka_2023",
        title="Hyperglycemic Crises in Adult Patients With Diabetes",
        title_vn="Khủng hoảng Tăng đường huyết ở Bệnh nhân Người lớn Đái tháo đường",
        organization="ADA",
        year=2023,
        category="Endocrinology",
        version="2023",
        last_updated="2023-01-01",
        url="https://diabetesjournals.org/care/issue/46/Supplement_1",
        related_protocol="DKA Protocol",
        description="Diabetic ketoacidosis and hyperosmolar hyperglycemic state management",
        key_recommendations=[
            "IV fluids: 1-1.5L in first hour, then 250-500 mL/h",
            "Regular insulin 0.1 U/kg IV bolus, then 0.1 U/kg/h infusion",
            "Add dextrose when glucose <200 mg/dL",
            "Correct potassium before insulin if K+ <3.3 mEq/L"
        ]
    ),
    
    # === ADDITIONAL NEUROLOGY ===
    Guideline(
        id="aha_stroke_2021",
        title="2021 Guideline for the Prevention of Stroke in Patients With Stroke and Transient Ischemic Attack",
        title_vn="Hướng dẫn 2021 về Phòng ngừa Đột quỵ ở Bệnh nhân Đã từng Đột quỵ và Cơn thiếu máu não thoáng qua",
        organization="AHA/ASA",
        year=2021,
        category="Neurology",
        version="2021",
        last_updated="2021-05-24",
        url="https://www.ahajournals.org/doi/10.1161/STR.0000000000000375",
        related_protocol="Stroke Management",
        description="Secondary stroke prevention guidelines",
        key_recommendations=[
            "Antiplatelet therapy: Aspirin 81-325 mg or clopidogrel",
            "Dual antiplatelet (aspirin + clopidogrel) for 21-90 days after minor stroke/TIA",
            "Anticoagulation for atrial fibrillation (CHA2DS2-VASc ≥2)",
            "Statins for all ischemic stroke/TIA patients"
        ]
    ),
    Guideline(
        id="aha_ich_2022",
        title="2022 Guideline for the Management of Patients With Spontaneous Intracerebral Hemorrhage",
        title_vn="Hướng dẫn 2022 về Quản lý Bệnh nhân Xuất huyết Nội sọ Tự phát",
        organization="AHA/ASA",
        year=2022,
        category="Neurology",
        version="2022",
        last_updated="2022-05-17",
        url="https://www.ahajournals.org/doi/10.1161/STR.0000000000000407",
        description="Intracerebral hemorrhage management",
        key_recommendations=[
            "Blood pressure control: Target SBP <140 mmHg",
            "Reverse anticoagulation if present",
            "Neurosurgical consultation for large hematomas",
            "Seizure prophylaxis not routinely recommended"
        ]
    ),
    
    # === ADDITIONAL CRITICAL CARE ===
    Guideline(
        id="sccm_ventilator_2017",
        title="2017 SCCM/ATS Clinical Practice Guidelines: Liberation from Mechanical Ventilation",
        title_vn="Hướng dẫn Thực hành Lâm sàng 2017 SCCM/ATS: Giải phóng khỏi Thông khí Cơ học",
        organization="SCCM/ATS",
        year=2017,
        category="Critical Care",
        version="2017",
        last_updated="2017-01-15",
        url="https://www.sccm.org/Clinical-Resources/Guidelines/Guidelines",
        related_protocol="Ventilator Weaning",
        description="Ventilator liberation and weaning protocols",
        key_recommendations=[
            "Daily spontaneous breathing trials (SBT)",
            "SBT with pressure support 5-8 cmH2O or T-piece",
            "Early mobilization and physical therapy",
            "Protocol-driven weaning reduces duration"
        ]
    ),
    
    # === ADDITIONAL EMERGENCY ===
    Guideline(
        id="aha_pe_2019",
        title="2019 AHA/ACC/HRS Guideline for the Management of Patients With Atrial Fibrillation",
        title_vn="Hướng dẫn 2019 AHA/ACC/HRS về Quản lý Bệnh nhân Rung nhĩ",
        organization="AHA/ACC/HRS",
        year=2019,
        category="Cardiology",
        version="2019",
        last_updated="2019-01-28",
        url="https://www.ahajournals.org/doi/10.1161/CIR.0000000000000665",
        related_protocol="Rung Nhĩ (Atrial Fibrillation)",
        description="Atrial fibrillation management including rate/rhythm control and anticoagulation",
        key_recommendations=[
            "CHA2DS2-VASc score for stroke risk assessment",
            "Anticoagulation for CHA2DS2-VASc ≥2 (men) or ≥3 (women)",
            "Rate control: Beta-blockers, calcium channel blockers, digoxin",
            "Rhythm control: Cardioversion, antiarrhythmics, ablation"
        ]
    ),
    
    # === LATEST GUIDELINES 2023-2025 ===
    
    # === CARDIOLOGY - LATEST ===
    Guideline(
        id="esc_hypertension_2024",
        title="2024 ESC/ESH Guidelines for the Management of Arterial Hypertension",
        title_vn="Hướng dẫn ESC/ESH 2024 về Quản lý Tăng huyết áp Động mạch",
        organization="ESC/ESH",
        year=2024,
        category="Cardiology",
        version="2024",
        last_updated="2024-08-01",
        url="https://www.escardio.org/Guidelines/Clinical-Practice-Guidelines",
        description="Latest European hypertension guidelines with updated BP targets and treatment strategies",
        key_recommendations=[
            "BP target <140/90 mmHg for most patients, <130/80 if tolerated",
            "Single-pill combination as initial therapy",
            "ACEi/ARB + CCB or thiazide as first-line",
            "SGLT2 inhibitors for diabetes or heart failure"
        ],
        is_high_impact=True,
        related_tools=[
            {"name": "CV Risk Score", "url": "/Scores?calc=cv_risk"}
        ]
    ),
    Guideline(
        id="acc_aha_heart_failure_2023",
        title="2023 ACC/AHA/HFSA Heart Failure Guideline Update",
        title_vn="Cập nhật Hướng dẫn Suy tim 2023 ACC/AHA/HFSA",
        organization="ACC/AHA/HFSA",
        year=2023,
        category="Cardiology",
        version="2023",
        last_updated="2023-04-01",
        url="https://www.ahajournals.org/doi/10.1161/CIR.0000000000001123",
        related_protocol="Suy tim Cấp",
        description="Updated heart failure guidelines with new drug recommendations",
        key_recommendations=[
            "SGLT2 inhibitors (dapagliflozin/empagliflozin) for all HFrEF",
            "Quadruple therapy: ACEi/ARNI + beta-blocker + MRA + SGLT2i",
            "Vericiguat for HFrEF with recent decompensation",
            "Ivabradine for HFrEF with HR >70 on beta-blocker"
        ],
        is_high_impact=True,
        related_tools=[
            {"name": "HFrEF Calculator", "url": "/Scores?calc=hfref"},
            {"name": "MAGGIC Score", "url": "/Scores?calc=maggic"}
        ]
    ),
    Guideline(
        id="esc_heart_failure_2023",
        title="2023 ESC Guidelines for the diagnosis and treatment of acute and chronic heart failure",
        title_vn="Hướng dẫn ESC 2023 về chẩn đoán và điều trị suy tim cấp và mạn",
        organization="ESC",
        year=2023,
        category="Cardiology",
        version="2023",
        last_updated="2023-08-25",
        url="https://www.escardio.org/Guidelines/Clinical-Practice-Guidelines",
        related_protocol="Suy tim Cấp",
        description="European heart failure guidelines 2023",
        key_recommendations=[
            "SGLT2 inhibitors for all HFrEF regardless of diabetes",
            "ARNI preferred over ACEi/ARB for HFrEF",
            "Quadruple therapy as standard of care",
            "HFpEF: SGLT2 inhibitors, consider ARNI"
        ]
    ),
    Guideline(
        id="acc_aha_acs_2024",
        title="2024 ACC/AHA/SCAI Guideline for Coronary Artery Revascularization",
        title_vn="Hướng dẫn ACC/AHA/SCAI 2024 về Tái thông Động mạch Vành",
        organization="ACC/AHA/SCAI",
        year=2024,
        category="Cardiology",
        version="2024",
        last_updated="2024-12-01",
        url="https://www.ahajournals.org/doi/10.1161/CIR.0000000000001168",
        related_protocol="ACS - Hội chứng vành cấp",
        description="Updated coronary revascularization guidelines",
        key_recommendations=[
            "PCI vs CABG based on SYNTAX score and comorbidities",
            "Radial access preferred for PCI",
            "Dual antiplatelet therapy duration based on risk",
            "Complete revascularization for multivessel disease"
        ]
    ),
    
    # === INFECTIOUS DISEASES - LATEST ===
    Guideline(
        id="idsa_sepsis_2024",
        title="Surviving Sepsis Campaign: International Guidelines for Management of Sepsis and Septic Shock 2024",
        title_vn="Chiến dịch Sống sót Sepsis: Hướng dẫn Quốc tế 2024",
        organization="SSC",
        year=2024,
        category="Infectious",
        version="2024",
        last_updated="2024-10-01",
        url="https://www.sccm.org/SurvivingSepsisCampaign/Guidelines/Adult-Patients",
        related_protocol="Sepsis 1-Hour Bundle",
        description="Latest sepsis guidelines 2024",
        key_recommendations=[
            "1-hour bundle: Measure lactate, cultures, antibiotics, fluids",
            "Antibiotics within 1 hour, or immediately if shock",
            "30 mL/kg crystalloid, reassess after each bolus",
            "Norepinephrine as first-line vasopressor"
        ],
        is_high_impact=True,
        related_tools=[
            {"name": "SOFA Score", "url": "/Scores?calc=sofa"},
            {"name": "qSOFA", "url": "/Scores?calc=qsofa"}
        ]
    ),
    Guideline(
        id="idsa_cap_2023",
        title="2023 IDSA/ATS Clinical Practice Guidelines for Community-Acquired Pneumonia",
        title_vn="Hướng dẫn Thực hành Lâm sàng Viêm phổi Cộng đồng 2023 IDSA/ATS",
        organization="IDSA/ATS",
        year=2023,
        category="Infectious",
        version="2023",
        last_updated="2023-11-01",
        url="https://www.idsociety.org/practice-guideline/community-acquired-pneumonia/",
        related_protocol="Viêm phổi cộng đồng (CAP)",
        description="Updated CAP guidelines 2023",
        key_recommendations=[
            "Amoxicillin-clavulanate or doxycycline for outpatient",
            "Beta-lactam + macrolide or respiratory fluoroquinolone for inpatient",
            "Duration: 5 days for most, extend if slow response",
            "Switch to oral when clinically stable"
        ]
    ),
    
    # === RESPIRATORY - LATEST ===
    Guideline(
        id="gold_copd_2025",
        title="Global Strategy for the Diagnosis, Management, and Prevention of Chronic Obstructive Pulmonary Disease 2025",
        title_vn="Chiến lược Toàn cầu Chẩn đoán, Quản lý và Phòng ngừa COPD 2025",
        organization="GOLD",
        year=2025,
        category="Respiratory",
        version="2025",
        last_updated="2025-01-01",
        url="https://goldcopd.org/2025-gold-report/",
        related_protocol="COPD Exacerbation",
        description="Latest GOLD guidelines for COPD management 2025",
        key_recommendations=[
            "LAMA/LABA combination for Group B-D patients",
            "Triple therapy (ICS/LAMA/LABA) for Group E patients",
            "SGLT2 inhibitors for COPD with heart failure",
            "Pulmonary rehabilitation for all symptomatic patients"
        ],
        is_high_impact=True,
        related_tools=[
            {"name": "mMRC", "url": "/Scores?calc=mMRC"},
            {"name": "BODE Index", "url": "/Scores?calc=BODE Index"}
        ]
    ),
    Guideline(
        id="gina_asthma_2025",
        title="Global Strategy for Asthma Management and Prevention 2025",
        title_vn="Chiến lược Toàn cầu Quản lý và Phòng ngừa Hen phế quản 2025",
        organization="GINA",
        year=2025,
        category="Respiratory",
        version="2025",
        last_updated="2025-01-01",
        url="https://ginasthma.org/",
        related_protocol="Cơn hen cấp",
        description="Latest GINA guidelines for asthma management 2025",
        key_recommendations=[
            "ICS-formoterol as maintenance and reliever (MART)",
            "Avoid SABA-only treatment",
            "Biologics for severe uncontrolled asthma",
            "Step-up based on symptom control and exacerbations"
        ],
        is_high_impact=True,
        related_tools=[
            {"name": "Asthma Control Test", "url": "/Scores?calc=ACT"}
        ]
    ),
    
    # === NEPHROLOGY - LATEST ===
    Guideline(
        id="kdigo_ckd_2024",
        title="KDIGO 2024 Clinical Practice Guideline for the Evaluation and Management of Chronic Kidney Disease",
        title_vn="Hướng dẫn Thực hành Lâm sàng KDIGO 2024 về Đánh giá và Quản lý Bệnh thận Mạn",
        organization="KDIGO",
        year=2024,
        category="Nephrology",
        version="2024",
        last_updated="2024-11-01",
        url="https://kdigo.org/guidelines/ckd-evaluation-and-management/",
        description="Latest KDIGO CKD guidelines 2024",
        is_high_impact=True,
        related_tools=[
            {"name": "eGFR", "url": "/Scores?calc=eGFR"},
            {"name": "KDIGO Staging", "url": "/Scores?calc=KDIGO"}
        ],
        related_protocol="Suy thận mạn tính (CKD)",
        key_recommendations=[
            "SGLT2 inhibitors for CKD with eGFR ≥20",
            "ACEi/ARB for proteinuria regardless of diabetes",
            "BP target <120/80 for CKD with proteinuria",
            "Phosphate binders for hyperphosphatemia"
        ]
    ),
    Guideline(
        id="kdigo_aki_2024",
        title="KDIGO 2024 Clinical Practice Guideline for Acute Kidney Injury",
        title_vn="Hướng dẫn Thực hành Lâm sàng KDIGO 2024 về Tổn thương Thận Cấp",
        organization="KDIGO",
        year=2024,
        category="Nephrology",
        version="2024",
        last_updated="2024-03-01",
        url="https://kdigo.org/guidelines/acute-kidney-injury/",
        related_protocol="AKI Management",
        description="Updated AKI guidelines 2024",
        key_recommendations=[
            "AKI definition: Increase in SCr ≥0.3 mg/dL or ≥1.5x baseline",
            "Avoid nephrotoxic agents, optimize volume",
            "RRT when life-threatening complications",
            "Follow-up after AKI for CKD development"
        ]
    ),
    
    # === ENDOCRINOLOGY - LATEST ===
    Guideline(
        id="ada_diabetes_2025",
        title="Standards of Care in Diabetes—2025",
        title_vn="Tiêu chuẩn Chăm sóc Đái tháo đường—2025",
        organization="ADA",
        year=2025,
        category="Endocrinology",
        version="2025",
        last_updated="2025-01-01",
        url="https://diabetesjournals.org/care/issue/48/Supplement_1",
        description="Latest American Diabetes Association standards of care 2025",
        key_recommendations=[
            "HbA1c target <7% for most, <8% for frail elderly",
            "SGLT2 inhibitors or GLP-1 RAs first-line for CV/renal protection",
            "BP target <130/80 mmHg",
            "Statin for all diabetes >40 years or with CV risk"
        ]
    ),
    
    # === NEUROLOGY - LATEST ===
    Guideline(
        id="aha_stroke_2024",
        title="2024 Guidelines for the Early Management of Patients With Acute Ischemic Stroke",
        title_vn="Hướng dẫn 2024 về Quản lý Sớm Bệnh nhân Đột quỵ Thiếu máu Cục bộ Cấp",
        organization="AHA/ASA",
        year=2024,
        category="Neurology",
        version="2024",
        last_updated="2024-05-01",
        url="https://www.ahajournals.org/doi/10.1161/STR.0000000000000458",
        related_protocol="Stroke Management",
        description="Latest acute ischemic stroke management guidelines 2024",
        key_recommendations=[
            "IV tPA within 4.5 hours (0.9 mg/kg), consider up to 9 hours with imaging",
            "Mechanical thrombectomy within 24 hours for large vessel occlusion",
            "Tenecteplase as alternative to alteplase",
            "BP management: <185/110 before tPA, <180/105 after"
        ]
    ),
    Guideline(
        id="aha_ich_2024",
        title="2024 Guideline for the Management of Patients With Spontaneous Intracerebral Hemorrhage",
        title_vn="Hướng dẫn 2024 về Quản lý Bệnh nhân Xuất huyết Nội sọ Tự phát",
        organization="AHA/ASA",
        year=2024,
        category="Neurology",
        version="2024",
        last_updated="2024-05-17",
        url="https://www.ahajournals.org/doi/10.1161/STR.0000000000000460",
        description="Updated ICH management guidelines 2024",
        key_recommendations=[
            "BP control: Target SBP <140 mmHg within 1 hour",
            "Reverse anticoagulation immediately if present",
            "Neurosurgical consultation for large hematomas (>30 mL)",
            "Seizure prophylaxis not routinely recommended"
        ]
    ),
    
    # === CRITICAL CARE - LATEST ===
    Guideline(
        id="sccm_ventilator_2024",
        title="2024 SCCM/ATS Clinical Practice Guidelines: Liberation from Mechanical Ventilation",
        title_vn="Hướng dẫn Thực hành Lâm sàng 2024 SCCM/ATS: Giải phóng khỏi Thông khí Cơ học",
        organization="SCCM/ATS",
        year=2024,
        category="Critical Care",
        version="2024",
        last_updated="2024-01-15",
        url="https://www.sccm.org/Clinical-Resources/Guidelines/Guidelines",
        related_protocol="Ventilator Weaning",
        description="Updated ventilator liberation guidelines 2024",
        key_recommendations=[
            "Daily spontaneous breathing trials (SBT)",
            "SBT with pressure support 5-8 cmH2O or T-piece",
            "Early mobilization and physical therapy",
            "Protocol-driven weaning reduces duration"
        ]
    ),
    
    # === EMERGENCY - LATEST ===
    Guideline(
        id="aha_acls_2025",
        title="2025 American Heart Association Guidelines for Cardiopulmonary Resuscitation and Emergency Cardiovascular Care",
        title_vn="Hướng dẫn 2025 Hiệp hội Tim mạch Hoa Kỳ về Hồi sức Tim phổi và Chăm sóc Tim mạch Cấp cứu",
        organization="AHA",
        year=2025,
        category="Emergency",
        version="2025",
        last_updated="2025-01-01",
        url="https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines",
        related_protocol="Cardiac Arrest / ACLS",
        description="Latest ACLS guidelines 2025",
        key_recommendations=[
            "High-quality CPR: 100-120 compressions/min, depth 5-6 cm",
            "Early defibrillation for shockable rhythms",
            "Epinephrine 1mg IV/IO every 3-5 minutes",
            "Amiodarone for VF/pulseless VT, consider esmolol for refractory VF"
        ]
    ),
    
    # === HEMATOLOGY - NEW ===
    Guideline(
        id="ash_vte_2024",
        title="2024 ASH Clinical Practice Guidelines on Venous Thromboembolism",
        title_vn="Hướng dẫn Thực hành Lâm sàng ASH 2024 về Huyết khối Tĩnh mạch",
        organization="ASH",
        year=2024,
        category="Hematology",
        version="2024",
        last_updated="2024-11-01",
        url="https://www.hematology.org/education/clinicians/guidelines-and-quality-care",
        description="ASH guidelines for VTE prevention and treatment",
        key_recommendations=[
            "DOACs preferred over warfarin for VTE treatment",
            "3 months anticoagulation for provoked VTE",
            "Extended anticoagulation for unprovoked VTE if low bleeding risk",
            "LMWH or DOACs for cancer-associated VTE"
        ]
    ),
    
    # === GASTROENTEROLOGY ===
    Guideline(
        id="acg_ibd_2023",
        title="2023 ACG Clinical Guideline on the Management of Inflammatory Bowel Disease",
        title_vn="Hướng dẫn Lâm sàng ACG 2023 về Quản lý Bệnh viêm ruột",
        organization="ACG",
        year=2023,
        category="Gastroenterology",
        version="2023",
        last_updated="2023-06-01",
        url="https://journals.lww.com/ajg/Fulltext/2023/06000/ACG_Clinical_Guideline_on_the_Management_of.14.aspx",
        related_protocol="IBD Exacerbation (Acute Exacerbation of IBD)",
        description="ACG guidelines for IBD diagnosis and management",
        key_recommendations=[
            "Methotrexate or anti-TNF for moderate to severe Crohn's disease",
            "Vedolizumab or ustekinumab for patients with anti-TNF failure",
            "5-ASA for mild to moderate ulcerative colitis",
            "Biologics for severe UC or steroid-dependent disease"
        ]
    ),
    Guideline(
        id="acg_gerd_2022",
        title="2022 ACG Clinical Guideline for the Diagnosis and Management of Gastroesophageal Reflux Disease",
        title_vn="Hướng dẫn Lâm sàng ACG 2022 về Chẩn đoán và Quản lý Trào ngược Dạ dày Thực quản",
        organization="ACG",
        year=2022,
        category="Gastroenterology",
        version="2022",
        last_updated="2022-01-01",
        url="https://journals.lww.com/ajg/Fulltext/2022/01000/ACG_Clinical_Guideline_for_the_Diagnosis_and.14.aspx",
        related_protocol="Trào Ngược Dạ Dày Thực Quản (GERD)",
        description="ACG guidelines for GERD management",
        key_recommendations=[
            "PPI once daily before first meal for 4-8 weeks",
            "H2RA or PPI on-demand for mild intermittent symptoms",
            "Long-term PPI for severe erosive esophagitis",
            "Endoscopy for alarm symptoms or persistent symptoms despite treatment"
        ]
    ),
    Guideline(
        id="acg_hepatitis_c_2023",
        title="2023 ACG Clinical Guideline: Diagnosis, Management, and Treatment of Hepatitis C",
        title_vn="Hướng dẫn Lâm sàng ACG 2023: Chẩn đoán, Quản lý và Điều trị Viêm gan C",
        organization="ACG",
        year=2023,
        category="Gastroenterology",
        version="2023",
        last_updated="2023-07-01",
        url="https://journals.lww.com/ajg/Fulltext/2023/07000/ACG_Clinical_Guideline__Diagnosis,_Management,.17.aspx",
        related_protocol="Điều trị Viêm Gan C (Hepatitis C Treatment)",
        description="ACG guidelines for hepatitis C treatment",
        key_recommendations=[
            "Universal screening for HCV in adults 18-79 years",
            "Direct-acting antivirals (DAAs) for all patients with HCV",
            "Glecaprevir/pibrentasvir or sofosbuvir/velpatasvir for most genotypes",
            "12 weeks treatment for most patients, 8 weeks for select cases"
        ]
    ),
    
    # === ONCOLOGY ===
    Guideline(
        id="nccn_supportive_care_2024",
        title="2024 NCCN Guidelines for Supportive Care in Oncology",
        title_vn="Hướng dẫn NCCN 2024 về Chăm sóc Hỗ trợ trong Ung thư",
        organization="NCCN",
        year=2024,
        category="Oncology",
        version="2024",
        last_updated="2024-01-01",
        url="https://www.nccn.org/guidelines/category_1",
        description="NCCN guidelines for supportive care including febrile neutropenia, antiemetics, pain",
        key_recommendations=[
            "Empiric broad-spectrum antibiotics for febrile neutropenia",
            "Granulocyte colony-stimulating factor (G-CSF) for high-risk febrile neutropenia",
            "5-HT3 antagonist + dexamethasone for highly emetogenic chemotherapy",
            "Multimodal pain management including opioids and adjuvants"
        ]
    ),
    Guideline(
        id="asco_breast_cancer_2024",
        title="2024 ASCO Clinical Practice Guidelines for Breast Cancer",
        title_vn="Hướng dẫn Thực hành Lâm sàng ASCO 2024 về Ung thư Vú",
        organization="ASCO",
        year=2024,
        category="Oncology",
        version="2024",
        last_updated="2024-03-01",
        url="https://www.asco.org/practice-patients/guidelines/breast-cancer",
        description="ASCO guidelines for breast cancer treatment and management",
        key_recommendations=[
            "Adjuvant endocrine therapy for hormone receptor-positive disease",
            "Trastuzumab for HER2-positive early breast cancer",
            "CDK4/6 inhibitors with endocrine therapy for advanced HR+/HER2- disease",
            "PARP inhibitors for BRCA-mutated metastatic breast cancer"
        ]
    ),
    
    # === RHEUMATOLOGY ===
    Guideline(
        id="acr_ra_2021",
        title="2021 American College of Rheumatology Guideline for the Treatment of Rheumatoid Arthritis",
        title_vn="Hướng dẫn ACR 2021 về Điều trị Viêm khớp Dạng thấp",
        organization="ACR",
        year=2021,
        category="Rheumatology",
        version="2021",
        last_updated="2021-06-01",
        url="https://www.rheumatology.org/Portals/0/Files/ACR_RA_Guideline_2021.pdf",
        related_protocol="RA Flare (Acute Flare of Rheumatoid Arthritis)",
        description="ACR guidelines for rheumatoid arthritis treatment",
        key_recommendations=[
            "Methotrexate as first-line DMARD for most patients",
            "TNF inhibitors or JAK inhibitors for patients with inadequate response to MTX",
            "Triple therapy (MTX + sulfasalazine + hydroxychloroquine) as alternative",
            "Early aggressive treatment to prevent joint damage"
        ]
    ),
    Guideline(
        id="acr_gout_2020",
        title="2020 American College of Rheumatology Guideline for the Management of Gout",
        title_vn="Hướng dẫn ACR 2020 về Quản lý Gout",
        organization="ACR",
        year=2020,
        category="Rheumatology",
        version="2020",
        last_updated="2020-05-01",
        url="https://www.rheumatology.org/Portals/0/Files/Gout_Guideline_2020.pdf",
        related_protocol="Gout Cấp (Acute Gout Management)",
        description="ACR guidelines for gout management",
        key_recommendations=[
            "Colchicine, NSAIDs, or corticosteroids for acute gout",
            "Allopurinol or febuxostat for urate-lowering therapy",
            "Start ULT during acute attack with concurrent anti-inflammatory prophylaxis",
            "Target serum urate <6 mg/dL (<5 mg/dL for tophaceous disease)"
        ]
    ),
    Guideline(
        id="bsr_ankylosing_spondylitis_2023",
        title="2023 BSR Guideline for the Management of Axial Spondyloarthritis",
        title_vn="Hướng dẫn BSR 2023 về Quản lý Viêm cột sống Dính khớp Trục",
        organization="BSR",
        year=2023,
        category="Rheumatology",
        version="2023",
        last_updated="2023-01-01",
        url="https://academic.oup.com/rheumatology/article/62/1/1/6677156",
        related_protocol="Viêm Cột Sống Dính Khớp (Ankylosing Spondylitis)",
        description="BSR guidelines for axial spondyloarthritis including ankylosing spondylitis",
        key_recommendations=[
            "NSAIDs as first-line treatment",
            "TNF inhibitors or IL-17 inhibitors for patients with active disease despite NSAIDs",
            "Physical therapy and exercise as core treatment",
            "Monitor for uveitis, cardiovascular, and pulmonary complications"
        ]
    ),
    
    # === OBSTETRICS ===
    Guideline(
        id="acog_preeclampsia_2023",
        title="2023 ACOG Practice Bulletin: Gestational Hypertension and Preeclampsia",
        title_vn="Thực hành Lâm sàng ACOG 2023: Tăng huyết áp Thai kỳ và Tiền sản giật",
        organization="ACOG",
        year=2023,
        category="Obstetrics",
        version="2023",
        last_updated="2023-01-01",
        url="https://www.acog.org/clinical/clinical-guidance/practice-bulletin/articles/2023/01/gestational-hypertension-and-preeclampsia",
        related_protocol="Tiền Sản Giật (Preeclampsia)",
        description="ACOG guidelines for preeclampsia diagnosis and management",
        key_recommendations=[
            "Blood pressure ≥140/90 mmHg with proteinuria or end-organ dysfunction",
            "Magnesium sulfate for seizure prophylaxis in severe preeclampsia",
            "Delivery at 37 weeks for mild preeclampsia, immediate for severe",
            "Low-dose aspirin (81mg) daily from 12-28 weeks for high-risk patients"
        ]
    ),
    Guideline(
        id="acog_hellp_2022",
        title="2022 ACOG Practice Bulletin: HELLP Syndrome",
        title_vn="Thực hành Lâm sàng ACOG 2022: Hội chứng HELLP",
        organization="ACOG",
        year=2022,
        category="Obstetrics",
        version="2022",
        last_updated="2022-03-01",
        url="https://www.acog.org/clinical/clinical-guidance/practice-bulletin/articles/2022/03/hellp-syndrome",
        related_protocol="HELLP Syndrome",
        description="ACOG guidelines for HELLP syndrome management",
        key_recommendations=[
            "Immediate delivery after maternal stabilization if ≥34 weeks",
            "Expectant management with corticosteroids if <34 weeks if stable",
            "Magnesium sulfate for seizure prophylaxis",
            "Blood pressure control with labetalol or hydralazine"
        ]
    ),
    Guideline(
        id="rcog_postpartum_hemorrhage_2023",
        title="2023 RCOG Guideline: Prevention and Management of Postpartum Haemorrhage",
        title_vn="Hướng dẫn RCOG 2023: Phòng ngừa và Quản lý Xuất huyết Sau sinh",
        organization="RCOG",
        year=2023,
        category="Obstetrics",
        version="2023",
        last_updated="2023-06-01",
        url="https://www.rcog.org.uk/guidance/browse-all-guidance/green-top-guidelines/prevention-and-management-of-postpartum-haemorrhage-green-top-guideline-no-52/",
        related_protocol="Xuất huyết sau sinh (Postpartum Hemorrhage)",
        description="RCOG guidelines for postpartum hemorrhage",
        key_recommendations=[
            "Active management of third stage of labor",
            "Oxytocin 10 units IM after delivery of anterior shoulder",
            "Uterine massage and tranexamic acid 1g IV for PPH",
            "Bimanual compression, balloon tamponade, or surgery if medical management fails"
        ]
    ),
    
    # === DERMATOLOGY ===
    Guideline(
        id="aad_psoriasis_2024",
        title="2024 AAD-NPF Guidelines of Care for the Management and Treatment of Psoriasis",
        title_vn="Hướng dẫn Chăm sóc AAD-NPF 2024 về Quản lý và Điều trị Vảy nến",
        organization="AAD/NPF",
        year=2024,
        category="Dermatology",
        version="2024",
        last_updated="2024-01-01",
        url="https://www.jaad.org/article/S0190-9622(24)00001-1/fulltext",
        related_protocol="Vảy nến (Psoriasis)",
        description="AAD-NPF guidelines for psoriasis management",
        key_recommendations=[
            "Topical corticosteroids for mild psoriasis",
            "Methotrexate, cyclosporine, or acitretin for moderate to severe",
            "Biologics (TNF inhibitors, IL-17/23 inhibitors) for severe or recalcitrant",
            "Phototherapy (NB-UVB or PUVA) as alternative or adjuvant"
        ]
    ),
    Guideline(
        id="aad_atopic_dermatitis_2024",
        title="2024 AAD Guidelines of Care for the Management of Atopic Dermatitis",
        title_vn="Hướng dẫn Chăm sóc AAD 2024 về Quản lý Viêm da Cơ địa",
        organization="AAD",
        year=2024,
        category="Dermatology",
        version="2024",
        last_updated="2024-02-01",
        url="https://www.jaad.org/article/S0190-9622(24)00002-3/fulltext",
        related_protocol="Viêm da cơ địa (Atopic Dermatitis)",
        description="AAD guidelines for atopic dermatitis (eczema) management",
        key_recommendations=[
            "Moisturizers and topical corticosteroids for mild to moderate",
            "Topical calcineurin inhibitors (tacrolimus, pimecrolimus) for sensitive areas",
            "Dupilumab or other biologics for moderate to severe",
            "Avoid triggers, maintain skin barrier with emollients"
        ]
    ),
    Guideline(
        id="aad_sjs_ten_2023",
        title="2023 AAD Guidelines: Management of Stevens-Johnson Syndrome and Toxic Epidermal Necrolysis",
        title_vn="Hướng dẫn AAD 2023: Quản lý Hội chứng Stevens-Johnson và Hoại tử Biểu bì Do độc",
        organization="AAD",
        year=2023,
        category="Dermatology",
        version="2023",
        last_updated="2023-05-01",
        url="https://www.jaad.org/article/S0190-9622(23)00001-2/fulltext",
        related_protocol="Hội chứng Stevens-Johnson (SJS/TEN)",
        description="AAD guidelines for SJS/TEN management",
        key_recommendations=[
            "Immediate discontinuation of suspected drug",
            "Supportive care in burn unit or ICU",
            "IVIG or cyclosporine within 72 hours of onset",
            "Wound care, infection prevention, ophthalmology consultation"
        ]
    ),
    
    # === PAIN MANAGEMENT ===
    Guideline(
        id="aps_opioids_2022",
        title="2022 APS Clinical Practice Guideline for the Use of Opioids in Chronic Non-Cancer Pain",
        title_vn="Hướng dẫn Thực hành Lâm sàng APS 2022 về Sử dụng Opioid trong Đau Mạn tính Không Ung thư",
        organization="APS",
        year=2022,
        category="Pain Management",
        version="2022",
        last_updated="2022-01-01",
        url="https://www.ampainsoc.org/advocacy/clinical-practice-guidelines",
        related_protocol="Quản lý Đau Cấp (Acute Pain Management)",
        description="APS guidelines for opioid use in chronic pain",
        key_recommendations=[
            "Non-opioid therapies first-line",
            "Lowest effective opioid dose if opioids necessary",
            "Morphine equivalent daily dose (MEDD) <90mg for most patients",
            "Regular monitoring, risk assessment, and prescription drug monitoring programs"
        ]
    ),
    
    # === UROLOGY ===
    Guideline(
        id="aua_utis_2022",
        title="2022 AUA/SUFU Guideline: Recurrent Uncomplicated Urinary Tract Infections in Women",
        title_vn="Hướng dẫn AUA/SUFU 2022: Nhiễm trùng Tiết niệu Tái phát Không phức tạp ở Phụ nữ",
        organization="AUA/SUFU",
        year=2022,
        category="Urology",
        version="2022",
        last_updated="2022-04-01",
        url="https://www.auanet.org/guidelines/guidelines/recurrent-uti",
        related_protocol="Nhiễm trùng tiểu / Viêm bể thận",
        description="AUA/SUFU guidelines for recurrent UTIs",
        key_recommendations=[
            "Post-coital or continuous low-dose antibiotics for prophylaxis",
            "Cranberry products or methenamine hippurate as alternatives",
            "Vaginal estrogen for postmenopausal women",
            "Avoid long-term antibiotics when possible"
        ]
    ),
    Guideline(
        id="eau_kidney_stones_2024",
        title="2024 EAU Guidelines on Urolithiasis",
        title_vn="Hướng dẫn EAU 2024 về Sỏi Tiết niệu",
        organization="EAU",
        year=2024,
        category="Urology",
        version="2024",
        last_updated="2024-01-01",
        url="https://uroweb.org/guidelines/urolithiasis",
        related_protocol="Sỏi thận / Cơn đau quặn thận",
        description="EAU guidelines for kidney stones",
        key_recommendations=[
            "ESWL, URS, or PCNL depending on stone size and location",
            "Medical expulsive therapy (tamsulosin) for distal ureteral stones <10mm",
            "Increased fluid intake (>2.5L/day) for prevention",
            "Metabolic evaluation for recurrent stone formers"
        ]
    ),
    
    # === TRAUMA & CRITICAL CARE - NEW ===
    Guideline(
        id="atls_trauma_2018",
        title="ATLS 10th Edition: Advanced Trauma Life Support",
        title_vn="ATLS Phiên bản 10: Hỗ trợ Sự sống Chấn thương Nâng cao",
        organization="ACS",
        year=2018,
        category="Trauma",
        version="10th Ed",
        last_updated="2024-01-01",
        url="https://www.facs.org/quality-programs/trauma/atls",
        related_protocol="Trauma Assessment",
        description="Standard protocol for initial assessment and management of trauma patients",
        key_recommendations=[
            "ABCDE priority: Airway, Breathing, Circulation, Disability, Exposure",
            "Identify and treat life-threatening injuries immediately",
            "Protect cervical spine",
            "Avoid hypothermia"
        ]
    ),
    Guideline(
        id="btf_tbi_2023",
        title="Brain Trauma Foundation Guidelines for Prevention of Secondary Brain Injury",
        title_vn="Hướng dẫn của Brain Trauma Foundation về Phòng ngừa Tổn thương Não Thứ phát",
        organization="BTF",
        year=2023,
        category="Trauma",
        version="4th Ed+",
        last_updated="2023-01-01",
        url="https://braintrauma.org/guidelines",
        related_protocol="Traumatic Brain Injury",
        description="Guidelines for management of severe TBI",
        key_recommendations=[
            "Maintain SBP >100 mmHg (50-69y) or >110 mmHg (15-49y)",
            "CPP target 60-70 mmHg",
            "Avoid prophylactic hyperventilation",
            "Limit steroid use"
        ]
    ),
    Guideline(
        id="aans_sci_2013",
        title="Management of Acute Spinal Cord Injuries",
        title_vn="Quản lý Chấn thương Tủy sống Cấp",
        organization="AANS/CNS",
        year=2013,
        category="Trauma",
        version="2013 (Rev 2024)",
        last_updated="2024-01-01",
        url="https://www.cns.org/guidelines/guidelines-management-acute-cervical-spine-and-spinal-cord-injuries",
        related_protocol="Spinal Cord Injury",
        description="Guidelines for acute spinal cord injury",
        key_recommendations=[
            "Maintain MAP >85-90 mmHg for 7 days",
            "Immobilization and early decompression",
            "Methylprednisolone high-dose is optional/controversial",
            "VTE prophylaxis essential"
        ]
    ),
    Guideline(
        id="sccm_delirium_2018",
        title="SCCM PADIS Guidelines 2018",
        title_vn="Hướng dẫn SCCM PADIS 2018",
        organization="SCCM",
        year=2018,
        category="Critical Care",
        version="2018",
        last_updated="2024-01-01",
        url="https://www.sccm.org/ICULiberation/PADIS-Guidelines",
        related_protocol="Delirium Management",
        description="Guidelines for Pain, Agitation/Sedation, Delirium, Immobility, and Sleep Disruption",
        key_recommendations=[
            "Assess delirium daily with CAM-ICU",
            "ABCDEF Bundle implementation",
            "Avoid benzodiazepines for sedation",
            "Promote early mobility"
        ]
    ),

    # === TOXICOLOGY - NEW ===
    Guideline(
        id="rumack_paracetamol",
        title="Rumack-Matthew Nomogram for Acetaminophen Poisoning",
        title_vn="Biểu đồ Rumack-Matthew cho Ngộ độc Paracetamol",
        organization="Toxicology",
        year=2020,
        category="Toxicology",
        version="2020",
        last_updated="2024-01-01",
        url="https://www.ncbi.nlm.nih.gov/books/NBK441917/",
        related_protocol="Paracetamol Poisoning",
        description="Protocol for NAC treatment in paracetamol overdose",
        key_recommendations=[
            "Quantify acetaminophen level 4-24h post-ingestion",
            "Use nomogram to determine NAC indication",
            "Give NAC within 8 hours for best outcome",
            "Treat if above treatment line"
        ]
    ),
    Guideline(
        id="asam_alcohol_2020",
        title="ASAM Clinical Practice Guideline on Alcohol Withdrawal Management",
        title_vn="Hướng dẫn ASAM về Quản lý Cai rượu",
        organization="ASAM",
        year=2020,
        category="Toxicology",
        version="2020",
        last_updated="2024-01-01",
        url="https://www.asam.org/quality-care/clinical-guidelines/alcohol-withdrawal-management-guideline",
        related_protocol="Alcohol Withdrawal",
        description="Management of alcohol withdrawal syndrome",
        key_recommendations=[
            "Use CIWA-Ar for assessment",
            "Symptom-triggered benzodiazepine therapy preferred",
            "Thiamine prophylaxis for Wernicke's",
            "Monitor for seizures and delirium tremens"
        ]
    ),

    # === PEDIATRICS - NEW ===
    Guideline(
        id="aap_bronchiolitis_2014",
        title="AAP Clinical Practice Guideline: Bronchiolitis",
        title_vn="Hướng dẫn AAP: Viêm tiểu phế quản",
        organization="AAP",
        year=2014,
        category="Pediatrics",
        version="2014 (Rev 2023)",
        last_updated="2023-01-01",
        url="https://publications.aap.org/pediatrics/article/134/5/e1474/32952/Clinical-Practice-Guideline-The-Diagnosis",
        related_protocol="Bronchiolitis",
        description="Management of bronchiolitis in infants",
        key_recommendations=[
            "Diagnosis is clinical",
            "Do not use bronchodilators or steroids routinely",
            "Supportive care (oxygen, hydration) is mainstay",
            "Avoid antibiotics unless bacterial coinfection"
        ]
    ),
    Guideline(
        id="aap_jaundice_2022",
        title="AAP Clinical Practice Guideline Revision: Management of Hyperbilirubinemia",
        title_vn="Hướng dẫn AAP 2022: Quản lý Tăng Bilirubin máu Sơ sinh",
        organization="AAP",
        year=2022,
        category="Pediatrics",
        version="2022",
        last_updated="2024-01-01",
        url="https://publications.aap.org/pediatrics/article/150/3/e2022058859/188722/Clinical-Practice-Guideline-Revision-Management-of",
        related_protocol="Neonatal Jaundice",
        description="Management of hyperbilirubinemia in newborns >35 weeks",
        key_recommendations=[
            "Universal screening for risk of severe hyperbilirubinemia",
            "Revised phototherapy and exchange transfusion thresholds",
            "Follow-up based on risk assessment",
            "Prevention of kernicterus"
        ]
    ),
    Guideline(
        id="aap_febrile_seizures_2019",
        title="AAP Clinical Practice Guideline: Febrile Seizures",
        title_vn="Hướng dẫn AAP: Co giật do sốt",
        organization="AAP",
        year=2019,
        category="Pediatrics",
        version="2019",
        last_updated="2024-01-01",
        url="https://publications.aap.org/pediatrics/article/122/4/895/71542/Febrile-Seizures-Guideline-for-the-Neurodiagnostic",
        related_protocol="Febrile Seizures",
        description="Management of simple febrile seizures",
        key_recommendations=[
            "No routine EEG or neuroimaging for simple febrile seizures",
            "Identify source of fever",
            "Reassurance and education for parents",
            "Antipyretics for comfort, not seizure prevention"
        ]
    ),
    Guideline(
        id="aap_uti_2021",
        title="AAP Clinical Practice Guideline: UTI in Febrile Infants",
        title_vn="Hướng dẫn AAP: Nhiễm trùng tiểu ở trẻ sốt",
        organization="AAP",
        year=2021,
        category="Pediatrics",
        version="2021",
        last_updated="2024-01-01",
        url="https://publications.aap.org/pediatrics/article/128/3/595/30605/Urinary-Tract-Infection-Clinical-Practice",
        related_protocol="Pediatric UTI",
        description="Diagnosis and management of UTI in children",
        key_recommendations=[
            "Catheterized specimen for diagnosis",
            "Renal ultrasound for first febrile UTI",
            "7-14 days antibiotics",
            "VCUG not routine after first UTI"
        ]
    ),

    # === OBSTETRICS - NEW ===
    Guideline(
        id="acog_ectopic_2018",
        title="ACOG Practice Bulletin No. 193: Tubal Ectopic Pregnancy",
        title_vn="Thực hành Lâm sàng ACOG: Thai ngoài tử cung",
        organization="ACOG",
        year=2018,
        category="Obstetrics",
        version="2018 (Rev 2020)",
        last_updated="2020-01-01",
        url="https://www.acog.org/clinical/clinical-guidance/practice-bulletin/articles/2018/03/tubal-ectopic-pregnancy",
        related_protocol="Ectopic Pregnancy",
        description="Management of tubal ectopic pregnancy",
        key_recommendations=[
            "Methotrexate for stable patients with suitable criteria",
            "Surgery for unstable or ruptured cases",
            "Serial hCG monitoring",
            "Rh immunoglobulin for Rh-negative women"
        ]
    ),
    Guideline(
        id="acog_preterm_2019",
        title="ACOG Practice Bulletin No. 234: Management of Preterm Labor",
        title_vn="Thực hành Lâm sàng ACOG: Quản lý Dọa sanh non",
        organization="ACOG",
        year=2019,
        category="Obstetrics",
        version="2021",
        last_updated="2021-08-01",
        url="https://www.acog.org/clinical/clinical-guidance/practice-bulletin/articles/2021/08/management-of-preterm-labor",
        related_protocol="Preterm Labor",
        description="Management of preterm labor <37 weeks",
        key_recommendations=[
            "Corticosteroids for fetal lung maturity (23-34w)",
            "Magnesium sulfate for neuroprotection (<32w)",
            "Tocolysis for 48h to allow steroid effect",
            "GBS prophylaxis"
        ]
    ),

    # === MEDICINE SUBSPECIALTIES - NEW ===
    Guideline(
        id="aasld_hbv_2018",
        title="AASLD 2018 Hepatitis B Guidance",
        title_vn="Hướng dẫn AASLD 2018 về Viêm gan B",
        organization="AASLD",
        year=2018,
        category="Gastroenterology",
        version="2018 (Update 2020)",
        last_updated="2020-01-01",
        url="https://www.aasld.org/practice-guidelines/chronic-hepatitis-b",
        related_protocol="Chronic Hepatitis B",
        description="Management of chronic hepatitis B",
        key_recommendations=[
            "Treat all cirrhotics with viremia",
            "Treat immune-active chronic hepatitis",
            "Entecavir, TDF, or TAF are first-line",
            "HCC surveillance every 6 months"
        ]
    ),
    Guideline(
        id="acg_pancreatitis_2024",
        title="ACG Guidelines: Management of Acute Pancreatitis",
        title_vn="Hướng dẫn ACG: Quản lý Viêm tụy cấp",
        organization="ACG",
        year=2024,
        category="Gastroenterology",
        version="2024",
        last_updated="2024-03-01",
        url="https://journals.lww.com/ajg/Fulltext/2013/09000/ACG_Guideline__Management_of_Acute_Pancreatitis.1.aspx",
        related_protocol="Acute Pancreatitis",
        description="Management of acute pancreatitis",
        key_recommendations=[
            "Aggressive hydration with Lactated Ringer's",
            "Early enteral feeding within 24-48h",
            "No routine prophylactic antibiotics",
            "ERCP for cholangitis"
        ]
    ),
    Guideline(
        id="ata_thyroid_storm_2016",
        title="ATA 2016 Guidelines for Diagnosis and Management of Hyperthyroidism",
        title_vn="Hướng dẫn ATA 2016 về Cường giáp và Bão giáp",
        organization="ATA",
        year=2016,
        category="Endocrinology",
        version="2016",
        last_updated="2024-01-01",
        url="https://www.thyroid.org/professionals/ata-professional-guidelines/",
        related_protocol="Thyroid Storm",
        description="Management of thyroid storm",
        key_recommendations=[
            "Multimodal therapy: Beta-blocker, Thionamide, Iodine, Steroids",
            "PTU preferred in storm",
            "Treat precipitating cause",
            "ICU admission"
        ]
    ),
    Guideline(
        id="ata_myxedema_2014",
        title="ATA 2014 Guidelines for Treatment of Hypothyroidism",
        title_vn="Hướng dẫn ATA 2014 về Suy giáp và Hôn mê phù niêm",
        organization="ATA",
        year=2014,
        category="Endocrinology",
        version="2014",
        last_updated="2024-01-01",
        url="https://www.thyroid.org/professionals/ata-professional-guidelines/",
        related_protocol="Myxedema Coma",
        description="Management of myxedema coma",
        key_recommendations=[
            "Empiric glucocorticoids before thyroid hormone",
            "IV Levothyroxine loading dose",
            "Consider IV Liothyronine (T3)",
            "Active warming and supportive care"
        ]
    ),
    Guideline(
        id="endo_adrenal_2016",
        title="Endocrine Society 2016: Primary Adrenal Insufficiency",
        title_vn="Hội Nội tiết 2016: Suy thượng thận",
        organization="Endocrine Soc",
        year=2016,
        category="Endocrinology",
        version="2016",
        last_updated="2024-01-01",
        url="https://www.endocrine.org/clinical-practice-guidelines/primary-adrenal-insufficiency",
        related_protocol="Adrenal Crisis",
        description="Management of adrenal crisis",
        key_recommendations=[
            "Immediate IV Hydrocortisone 100mg",
            "Fluid resuscitation with saline",
            "Do not wait for cortisol results",
            "Treat precipitating factors"
        ]
    ),
    Guideline(
        id="ahs_migraine_2021",
        title="AHS Consensus Statement: Acute Treatment of Migraine",
        title_vn="Đồng thuận AHS: Điều trị cắt cơn Migraine",
        organization="AHS",
        year=2021,
        category="Neurology",
        version="2021",
        last_updated="2024-01-01",
        url="https://headachejournal.onlinelibrary.wiley.com/doi/full/10.1111/head.14153",
        related_protocol="Acute Migraine",
        description="Acute migraine management",
        key_recommendations=[
            "Stratified care based on severity",
            "NSAIDs for mild-moderate",
            "Triptans for moderate-severe",
            "Avoid opioids"
        ]
    ),
    Guideline(
        id="aao_bppv_2017",
        title="AAO-HNSF Clinical Practice Guideline: BPPV",
        title_vn="Hướng dẫn AAO-HNSF: Chóng mặt tư thế kịch phát lành tính",
        organization="AAO-HNSF",
        year=2017,
        category="Neurology",
        version="2017",
        last_updated="2024-01-01",
        url="https://journals.sagepub.com/doi/full/10.1177/0194599816689667",
        related_protocol="BPPV",
        description="Diagnosis and management of BPPV",
        key_recommendations=[
            "Diagnose with Dix-Hallpike maneuver",
            "Treat with Epley maneuver (Canalith repositioning)",
            "Do not use vestibular suppressants routinely",
            "Imaging not recommended for typical BPPV"
        ]
    ),
    Guideline(
        id="ash_sickle_cell_2020",
        title="ASH 2020 Guidelines for Sickle Cell Disease: Acute Pain",
        title_vn="Hướng dẫn ASH 2020 về Hồng cầu hình liềm: Đau cấp",
        organization="ASH",
        year=2020,
        category="Hematology",
        version="2020",
        last_updated="2024-01-01",
        url="https://www.hematology.org/education/clinicians/guidelines-and-quality-care/sickle-cell-disease-guidelines",
        related_protocol="Sickle Cell Crisis",
        description="Management of vaso-occlusive crisis",
        key_recommendations=[
            "Rapid analgesic initiation (<1 hour)",
            "Individualized opioid dosing",
            "Supportive care",
            "Monitor for acute chest syndrome"
        ]
    ),
]


def get_all_guidelines() -> List[Guideline]:
    """Get all guidelines"""
    return GUIDELINES_DATABASE


def get_guidelines_by_category(category: str) -> List[Guideline]:
    """Get guidelines filtered by category"""
    if not category or category == "All":
        return GUIDELINES_DATABASE
    return [g for g in GUIDELINES_DATABASE if g.category == category]


def get_guidelines_by_organization(organization: str) -> List[Guideline]:
    """Get guidelines filtered by organization"""
    if not organization or organization == "All":
        return GUIDELINES_DATABASE
    return [g for g in GUIDELINES_DATABASE if organization in g.organization]


def get_category_list() -> List[str]:
    """Get list of all categories"""
    categories = set(g.category for g in GUIDELINES_DATABASE)
    return sorted(list(categories))


def get_organization_list() -> List[str]:
    """Get list of all organizations"""
    organizations = set()
    for g in GUIDELINES_DATABASE:
        # Split organizations like "AHA/ACC" into individual orgs
        orgs = g.organization.split("/")
        organizations.update(orgs)
    return sorted(list(organizations))

