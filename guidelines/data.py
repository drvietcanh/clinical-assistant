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
    
    def __post_init__(self):
        if self.key_recommendations is None:
            self.key_recommendations = []


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
        description="European Society of Cardiology heart failure guidelines"
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
        description="Hypertension guideline with new BP thresholds (130/80 mmHg)"
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
        description="Atrial fibrillation management including anticoagulation"
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
        description="Community-acquired pneumonia diagnosis and treatment"
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
        description="Updated sepsis guidelines 2021"
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
        description="GINA guidelines for asthma management"
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
        description="KDIGO AKI guidelines"
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
        description="KDIGO CKD guidelines"
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
        description="American Diabetes Association standards of care"
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
        description="Acute ischemic stroke management guidelines"
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
        description="ARDSNet low tidal volume ventilation protocol"
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
        description="ACLS guidelines 2020"
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

