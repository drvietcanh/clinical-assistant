"""
TDM Configuration
Cấu hình cho tất cả các thuốc TDM
"""

TDM_DRUGS = {
    # Aminoglycosides
    "amikacin": {
        "name": "Amikacin",
        "icon": "💉",
        "category": "Aminoglycoside",
        "therapeutic_range": "Peak: 20-30 mg/L, Trough: < 5 mg/L",
        "target_min": 20.0,
        "target_max": 30.0,
        "trough_max": 5.0,
        "toxic_threshold": 35.0,
        "unit": "mg/L",
        "sampling_time": "Peak (30-60 min post-dose) & Trough (pre-dose)",
        "half_life_hours": 2.0,
        "module": "aminoglycosides"
    },
    "gentamicin": {
        "name": "Gentamicin",
        "icon": "💉",
        "category": "Aminoglycoside",
        "therapeutic_range": "Peak: 5-10 mg/L, Trough: < 1 mg/L",
        "target_min": 5.0,
        "target_max": 10.0,
        "trough_max": 1.0,
        "toxic_threshold": 12.0,
        "unit": "mg/L",
        "sampling_time": "Peak (30-60 min post-dose) & Trough (pre-dose)",
        "half_life_hours": 2.0,
        "module": "aminoglycosides"
    },
    "tobramycin": {
        "name": "Tobramycin",
        "icon": "💉",
        "category": "Aminoglycoside",
        "therapeutic_range": "Peak: 5-10 mg/L, Trough: < 1 mg/L",
        "target_min": 5.0,
        "target_max": 10.0,
        "trough_max": 1.0,
        "toxic_threshold": 12.0,
        "unit": "mg/L",
        "sampling_time": "Peak (30-60 min post-dose) & Trough (pre-dose)",
        "half_life_hours": 2.0,
        "module": "aminoglycosides"
    },
    "netilmicin": {
        "name": "Netilmicin",
        "icon": "💉",
        "category": "Aminoglycoside",
        "therapeutic_range": "Peak: 5-10 mg/L, Trough: < 1 mg/L",
        "target_min": 5.0,
        "target_max": 10.0,
        "trough_max": 1.0,
        "toxic_threshold": 12.0,
        "unit": "mg/L",
        "sampling_time": "Peak (30-60 min post-dose) & Trough (pre-dose)",
        "half_life_hours": 2.0,
        "module": "aminoglycosides"
    },
    
    # Vancomycin
    "vancomycin": {
        "name": "Vancomycin",
        "icon": "💊",
        "category": "Glycopeptide",
        "therapeutic_range": "Trough: 10-20 mg/L (AUC: 400-600 mg·h/L)",
        "target_min": 10.0,
        "target_max": 20.0,
        "trough_max": 20.0,
        "toxic_threshold": 25.0,
        "unit": "mg/L",
        "sampling_time": "Trough (pre-dose) hoặc AUC",
        "half_life_hours": 6.0,
        "module": "vancomycin"
    },
    
    # Antiepileptics
    "carbamazepine": {
        "name": "Carbamazepine",
        "icon": "🧠",
        "category": "Antiepileptic",
        "therapeutic_range": "4-12 mg/L",
        "target_min": 4.0,
        "target_max": 12.0,
        "toxic_threshold": 15.0,
        "unit": "mg/L",
        "sampling_time": "Trough (pre-dose)",
        "half_life_hours": 12.0,
        "module": "antiepileptics"
    },
    "phenobarbital": {
        "name": "Phenobarbital",
        "icon": "🧠",
        "category": "Antiepileptic",
        "therapeutic_range": "15-40 mg/L",
        "target_min": 15.0,
        "target_max": 40.0,
        "toxic_threshold": 50.0,
        "unit": "mg/L",
        "sampling_time": "Trough (pre-dose)",
        "half_life_hours": 100.0,
        "module": "antiepileptics"
    },
    "phenytoin": {
        "name": "Phenytoin",
        "icon": "🧠",
        "category": "Antiepileptic",
        "therapeutic_range": "10-20 mg/L (total), 1-2 mg/L (free)",
        "target_min": 10.0,
        "target_max": 20.0,
        "toxic_threshold": 25.0,
        "unit": "mg/L",
        "sampling_time": "Trough (pre-dose)",
        "half_life_hours": 22.0,
        "module": "antiepileptics"
    },
    "valproic_acid": {
        "name": "Valproic Acid",
        "icon": "🧠",
        "category": "Antiepileptic",
        "therapeutic_range": "50-100 mg/L",
        "target_min": 50.0,
        "target_max": 100.0,
        "toxic_threshold": 150.0,
        "unit": "mg/L",
        "sampling_time": "Trough (pre-dose)",
        "half_life_hours": 12.0,
        "module": "antiepileptics"
    },
    
    # Cardiovascular
    "digoxin": {
        "name": "Digoxin",
        "icon": "💚",
        "category": "Cardiovascular",
        "therapeutic_range": "0.5-0.9 ng/mL (HF), 0.5-1.0 ng/mL (AF)",
        "target_min": 0.5,
        "target_max": 0.9,
        "toxic_threshold": 2.0,
        "unit": "ng/mL",
        "sampling_time": "Trough (≥ 6-8 hours post-dose)",
        "half_life_hours": 36.0,
        "module": "cardiovascular"
    },
    "amiodarone": {
        "name": "Amiodarone",
        "icon": "❤️",
        "category": "Cardiovascular",
        "therapeutic_range": "1.0-2.5 mg/L",
        "target_min": 1.0,
        "target_max": 2.5,
        "toxic_threshold": 3.0,
        "unit": "mg/L",
        "sampling_time": "Trough (pre-dose)",
        "half_life_hours": 50.0,
        "module": "cardiovascular"
    },
    "lidocaine": {
        "name": "Lidocaine",
        "icon": "❤️",
        "category": "Cardiovascular",
        "therapeutic_range": "1.5-5.0 mg/L",
        "target_min": 1.5,
        "target_max": 5.0,
        "toxic_threshold": 6.0,
        "unit": "mg/L",
        "sampling_time": "Peak (during infusion)",
        "half_life_hours": 1.5,
        "module": "cardiovascular"
    },
    "quinidine": {
        "name": "Quinidine",
        "icon": "❤️",
        "category": "Cardiovascular",
        "therapeutic_range": "2-5 mg/L",
        "target_min": 2.0,
        "target_max": 5.0,
        "toxic_threshold": 6.0,
        "unit": "mg/L",
        "sampling_time": "Trough (pre-dose)",
        "half_life_hours": 6.0,
        "module": "cardiovascular"
    },
    "flecainide": {
        "name": "Flecainide",
        "icon": "❤️",
        "category": "Cardiovascular",
        "therapeutic_range": "0.2-1.0 mg/L",
        "target_min": 0.2,
        "target_max": 1.0,
        "toxic_threshold": 1.5,
        "unit": "mg/L",
        "sampling_time": "Trough (pre-dose)",
        "half_life_hours": 14.0,
        "module": "cardiovascular"
    },
    "mexiletine": {
        "name": "Mexiletine",
        "icon": "❤️",
        "category": "Cardiovascular",
        "therapeutic_range": "0.5-2.0 mg/L",
        "target_min": 0.5,
        "target_max": 2.0,
        "toxic_threshold": 3.0,
        "unit": "mg/L",
        "sampling_time": "Trough (pre-dose)",
        "half_life_hours": 10.0,
        "module": "cardiovascular"
    },
    
    # Respiratory
    "theophylline": {
        "name": "Theophylline",
        "icon": "🫁",
        "category": "Respiratory",
        "therapeutic_range": "10-20 mg/L",
        "target_min": 10.0,
        "target_max": 20.0,
        "toxic_threshold": 25.0,
        "unit": "mg/L",
        "sampling_time": "Trough (pre-dose)",
        "half_life_hours": 8.0,
        "module": "respiratory"
    },
    
    # Psychiatry
    "lithium": {
        "name": "Lithium",
        "icon": "💊",
        "category": "Psychiatry",
        "therapeutic_range": "0.6-1.2 mmol/L (acute), 0.4-0.8 mmol/L (maintenance)",
        "target_min": 0.6,
        "target_max": 1.2,
        "toxic_threshold": 1.5,
        "unit": "mmol/L",
        "sampling_time": "Trough (12 hours post-dose)",
        "half_life_hours": 24.0,
        "module": "psychiatry"
    },
    
    # Immunosuppressants
    "cyclosporine": {
        "name": "Cyclosporine",
        "icon": "🩸",
        "category": "Immunosuppressant",
        "therapeutic_range": "Trough: 100-200 ng/mL (varies by indication)",
        "target_min": 100.0,
        "target_max": 200.0,
        "toxic_threshold": 300.0,
        "unit": "ng/mL",
        "sampling_time": "Trough (pre-dose)",
        "half_life_hours": 19.0,
        "module": "immunosuppressants"
    },
    "tacrolimus": {
        "name": "Tacrolimus",
        "icon": "🩸",
        "category": "Immunosuppressant",
        "therapeutic_range": "Trough: 5-15 ng/mL (varies by indication)",
        "target_min": 5.0,
        "target_max": 15.0,
        "toxic_threshold": 20.0,
        "unit": "ng/mL",
        "sampling_time": "Trough (pre-dose)",
        "half_life_hours": 12.0,
        "module": "immunosuppressants"
    },
    "sirolimus": {
        "name": "Sirolimus",
        "icon": "🩸",
        "category": "Immunosuppressant",
        "therapeutic_range": "Trough: 4-12 ng/mL",
        "target_min": 4.0,
        "target_max": 12.0,
        "toxic_threshold": 15.0,
        "unit": "ng/mL",
        "sampling_time": "Trough (pre-dose)",
        "half_life_hours": 60.0,
        "module": "immunosuppressants"
    },
    "everolimus": {
        "name": "Everolimus",
        "icon": "🩸",
        "category": "Immunosuppressant",
        "therapeutic_range": "Trough: 3-8 ng/mL",
        "target_min": 3.0,
        "target_max": 8.0,
        "toxic_threshold": 12.0,
        "unit": "ng/mL",
        "sampling_time": "Trough (pre-dose)",
        "half_life_hours": 30.0,
        "module": "immunosuppressants"
    },
    
    # Antifungals
    "voriconazole": {
        "name": "Voriconazole",
        "icon": "🦠",
        "category": "Antifungal",
        "therapeutic_range": "Trough: 1-5.5 mg/L",
        "target_min": 1.0,
        "target_max": 5.5,
        "toxic_threshold": 6.0,
        "unit": "mg/L",
        "sampling_time": "Trough (pre-dose)",
        "half_life_hours": 6.0,
        "module": "antifungals"
    },
    "posaconazole": {
        "name": "Posaconazole",
        "icon": "🦠",
        "category": "Antifungal",
        "therapeutic_range": "Trough: > 0.7 mg/L (prophylaxis), > 1.0 mg/L (treatment)",
        "target_min": 0.7,
        "target_max": 1.0,
        "toxic_threshold": 3.0,
        "unit": "mg/L",
        "sampling_time": "Trough (pre-dose)",
        "half_life_hours": 35.0,
        "module": "antifungals"
    },
    
    # Others
    "methotrexate": {
        "name": "Methotrexate",
        "icon": "🎗️",
        "category": "Oncology/Rheumatology",
        "therapeutic_range": "TDM for rescue: < 0.1 μmol/L at 48h",
        "target_min": 0.0,
        "target_max": 0.1,
        "toxic_threshold": 0.1,
        "unit": "μmol/L",
        "sampling_time": "48 hours post-dose (for rescue)",
        "half_life_hours": 8.0,
        "module": "oncology"
    },
    "isoniazid": {
        "name": "Isoniazid",
        "icon": "🦠",
        "category": "Antitubercular",
        "therapeutic_range": "Peak: 3-6 mg/L",
        "target_min": 3.0,
        "target_max": 6.0,
        "toxic_threshold": 8.0,
        "unit": "mg/L",
        "sampling_time": "Peak (1-2 hours post-dose)",
        "half_life_hours": 1.5,
        "module": "antitubercular"
    }
}


def get_drugs_by_category() -> dict:
    """Get drugs grouped by category"""
    categories = {}
    for drug_id, drug_info in TDM_DRUGS.items():
        category = drug_info["category"]
        if category not in categories:
            categories[category] = []
        categories[category].append((drug_id, drug_info))
    return categories


def get_all_drugs() -> dict:
    """Get all TDM drugs"""
    return TDM_DRUGS

