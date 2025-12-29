"""
Drug Formulary Database
Information about drugs covered by insurance (BHYT) and formularies
"""

from typing import List, Optional
from dataclasses import dataclass, field


@dataclass
class FormularyDrug:
    """Formulary drug information"""
    drug_name: str
    generic_name: str
    brand_names: List[str] = field(default_factory=list)
    category: str = ""  # Drug category
    insurance_coverage: str = "BHYT"  # BHYT, Private, Both, None
    coverage_type: str = ""  # Full coverage, Partial, Prior authorization required
    generic_available: bool = True
    price_range: str = ""  # Price range in VND
    notes: str = ""
    alternatives: List[str] = field(default_factory=list)  # Alternative drugs


# Formulary Database
# Common drugs with BHYT coverage information
FORMULARY_DATABASE: List[FormularyDrug] = [
    # === ANTIBIOTICS ===
    FormularyDrug(
        drug_name="Amoxicillin",
        generic_name="Amoxicillin",
        brand_names=["Amoxicillin", "Amoxiclav"],
        category="Antibiotics",
        insurance_coverage="BHYT",
        coverage_type="Full coverage",
        generic_available=True,
        price_range="10,000 - 50,000 VNĐ",
        notes="Có trong danh mục BHYT, không cần prior authorization"
    ),
    FormularyDrug(
        drug_name="Azithromycin",
        generic_name="Azithromycin",
        brand_names=["Azithromycin", "Zithromax"],
        category="Antibiotics",
        insurance_coverage="BHYT",
        coverage_type="Full coverage",
        generic_available=True,
        price_range="50,000 - 150,000 VNĐ"
    ),
    FormularyDrug(
        drug_name="Ceftriaxone",
        generic_name="Ceftriaxone",
        brand_names=["Ceftriaxone", "Rocephin"],
        category="Antibiotics",
        insurance_coverage="BHYT",
        coverage_type="Full coverage",
        generic_available=True,
        price_range="100,000 - 300,000 VNĐ"
    ),
    
    # === CARDIOVASCULAR ===
    FormularyDrug(
        drug_name="Amlodipine",
        generic_name="Amlodipine",
        brand_names=["Amlodipine", "Norvasc"],
        category="Cardiovascular",
        insurance_coverage="BHYT",
        coverage_type="Full coverage",
        generic_available=True,
        price_range="20,000 - 80,000 VNĐ"
    ),
    FormularyDrug(
        drug_name="Atenolol",
        generic_name="Atenolol",
        brand_names=["Atenolol", "Tenormin"],
        category="Cardiovascular",
        insurance_coverage="BHYT",
        coverage_type="Full coverage",
        generic_available=True,
        price_range="15,000 - 60,000 VNĐ"
    ),
    FormularyDrug(
        drug_name="Enalapril",
        generic_name="Enalapril",
        brand_names=["Enalapril", "Vasotec"],
        category="Cardiovascular",
        insurance_coverage="BHYT",
        coverage_type="Full coverage",
        generic_available=True,
        price_range="25,000 - 100,000 VNĐ"
    ),
    FormularyDrug(
        drug_name="Losartan",
        generic_name="Losartan",
        brand_names=["Losartan", "Cozaar"],
        category="Cardiovascular",
        insurance_coverage="BHYT",
        coverage_type="Full coverage",
        generic_available=True,
        price_range="30,000 - 120,000 VNĐ"
    ),
    FormularyDrug(
        drug_name="Atorvastatin",
        generic_name="Atorvastatin",
        brand_names=["Atorvastatin", "Lipitor"],
        category="Cardiovascular",
        insurance_coverage="BHYT",
        coverage_type="Full coverage",
        generic_available=True,
        price_range="50,000 - 200,000 VNĐ"
    ),
    
    # === DIABETES ===
    FormularyDrug(
        drug_name="Metformin",
        generic_name="Metformin",
        brand_names=["Metformin", "Glucophage"],
        category="Endocrinology",
        insurance_coverage="BHYT",
        coverage_type="Full coverage",
        generic_available=True,
        price_range="20,000 - 80,000 VNĐ"
    ),
    FormularyDrug(
        drug_name="Gliclazide",
        generic_name="Gliclazide",
        brand_names=["Gliclazide", "Diamicron"],
        category="Endocrinology",
        insurance_coverage="BHYT",
        coverage_type="Full coverage",
        generic_available=True,
        price_range="30,000 - 100,000 VNĐ"
    ),
    FormularyDrug(
        drug_name="Insulin",
        generic_name="Insulin",
        brand_names=["Insulin", "Humulin", "Novolin"],
        category="Endocrinology",
        insurance_coverage="BHYT",
        coverage_type="Full coverage",
        generic_available=False,
        price_range="200,000 - 500,000 VNĐ",
        notes="Có trong danh mục BHYT, cần đơn thuốc"
    ),
    
    # === GI ===
    FormularyDrug(
        drug_name="Omeprazole",
        generic_name="Omeprazole",
        brand_names=["Omeprazole", "Losec"],
        category="GI",
        insurance_coverage="BHYT",
        coverage_type="Full coverage",
        generic_available=True,
        price_range="30,000 - 120,000 VNĐ"
    ),
    FormularyDrug(
        drug_name="Ranitidine",
        generic_name="Ranitidine",
        brand_names=["Ranitidine", "Zantac"],
        category="GI",
        insurance_coverage="BHYT",
        coverage_type="Full coverage",
        generic_available=True,
        price_range="20,000 - 80,000 VNĐ"
    ),
    
    # === ANALGESICS ===
    FormularyDrug(
        drug_name="Paracetamol",
        generic_name="Paracetamol",
        brand_names=["Paracetamol", "Tylenol", "Panadol"],
        category="Analgesics",
        insurance_coverage="BHYT",
        coverage_type="Full coverage",
        generic_available=True,
        price_range="5,000 - 30,000 VNĐ"
    ),
    FormularyDrug(
        drug_name="Ibuprofen",
        generic_name="Ibuprofen",
        brand_names=["Ibuprofen", "Advil", "Brufen"],
        category="Analgesics",
        insurance_coverage="BHYT",
        coverage_type="Full coverage",
        generic_available=True,
        price_range="10,000 - 50,000 VNĐ"
    ),
    
    # === ANTICOAGULANTS ===
    FormularyDrug(
        drug_name="Warfarin",
        generic_name="Warfarin",
        brand_names=["Warfarin", "Coumadin"],
        category="Anticoagulants",
        insurance_coverage="BHYT",
        coverage_type="Full coverage",
        generic_available=True,
        price_range="20,000 - 80,000 VNĐ",
        notes="Cần theo dõi INR định kỳ"
    ),
    
    # === Examples of drugs NOT covered or requiring prior auth ===
    FormularyDrug(
        drug_name="Dabigatran",
        generic_name="Dabigatran",
        brand_names=["Pradaxa"],
        category="Anticoagulants",
        insurance_coverage="Private",
        coverage_type="Prior authorization required",
        generic_available=False,
        price_range="500,000 - 1,000,000 VNĐ",
        notes="Không có trong danh mục BHYT cơ bản, cần prior authorization",
        alternatives=["Warfarin"]
    ),
    FormularyDrug(
        drug_name="Rivaroxaban",
        generic_name="Rivaroxaban",
        brand_names=["Xarelto"],
        category="Anticoagulants",
        insurance_coverage="Private",
        coverage_type="Prior authorization required",
        generic_available=False,
        price_range="600,000 - 1,200,000 VNĐ",
        notes="Không có trong danh mục BHYT cơ bản",
        alternatives=["Warfarin"]
    ),
]


def get_all_formulary_drugs() -> List[FormularyDrug]:
    """Get all formulary drugs"""
    return FORMULARY_DATABASE


def get_drugs_by_category(category: str) -> List[FormularyDrug]:
    """Get drugs filtered by category"""
    if not category or category == "All":
        return FORMULARY_DATABASE
    return [d for d in FORMULARY_DATABASE if d.category == category]


def get_drugs_by_insurance_type(insurance_type: str) -> List[FormularyDrug]:
    """Get drugs filtered by insurance coverage type"""
    if not insurance_type or insurance_type == "All":
        return FORMULARY_DATABASE
    return [d for d in FORMULARY_DATABASE if insurance_type in d.insurance_coverage]


def get_category_list() -> List[str]:
    """Get list of all categories"""
    categories = set(d.category for d in FORMULARY_DATABASE)
    return sorted(list(categories))

