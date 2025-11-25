"""
Enhanced Drug Fields Template
Standard template for all enhanced drug fields
Used to ensure consistency across all drugs
"""

# Standard enhanced fields structure
ENHANCED_FIELDS_TEMPLATE = {
    # Core fields (should be present in all drugs)
    "mechanism_of_action": {
        "primary": str,  # Short description
        "detailed": str,  # Detailed mechanism
        "target": str,  # Target receptor/enzyme
    },
    
    "pharmacokinetics": {
        "half_life": str,
        "onset": str,
        "duration": str,
        "protein_binding": str,
        "clearance": str,
        "bioavailability": str,  # Optional
        "metabolism": str,  # Optional (e.g., CYP enzymes)
        "excretion": str,  # Optional
    },
    
    "monitoring": {
        "labs": list,  # List of lab tests
        "vital_signs": list,  # List of vital signs
        "clinical": list,  # Clinical monitoring
        "frequency": str,  # Monitoring frequency
    },
    
    "precautions": list,  # List of precautions
    
    "storage": str,  # Storage instructions
    
    # Safety fields
    "black_box_warnings": list,  # List of black box warnings
    
    "contraindications": {
        "tuyệt_đối": list,  # Absolute contraindications
        "tương_đối": list,  # Relative contraindications
    },
    
    "overdose_management": {
        "symptoms": list,
        "antidote": str,  # Antidote if available
        "treatment": list,  # Treatment steps
    },
    
    "reversal_agents": list,  # Reversal agents if available
    
    # Special populations
    "pediatric_dosing": {
        "neonates": str,  # < 1 month
        "infants": str,  # 1 month - 2 years
        "children": str,  # 2-12 years
        "adolescents": str,  # 12-18 years
        "notes": str,  # Additional notes
    },
    
    "geriatric_dosing": {
        "considerations": str,
        "dose_adjustment": str,
        "monitoring": str,
    },
    
    "pregnancy_lactation": {
        "fda_category": str,  # A, B, C, D, X
        "pregnancy_details": str,
        "lactation": {
            "safety": str,  # Compatible, Caution, Contraindicated
            "details": str,
            "recommendation": str,
        },
    },
    
    "renal_adjustment": {
        "normal": str,  # CrCl > 60
        "30_60": str,  # CrCl 30-60
        "under_30": str,  # CrCl < 30
        "dialysis": str,  # If applicable
    },
    
    "hepatic_adjustment": {
        "mild": str,  # Mild hepatic impairment
        "moderate": str,  # Moderate hepatic impairment
        "severe": str,  # Severe hepatic impairment
        "notes": str,  # Additional notes
    },
    
    # Localization
    "brand_names": {
        "vietnam": list,  # Vietnamese brand names
        "common": list,  # Common international brands
    },
    
    "cost_estimate": {
        "unit": str,  # VND, USD, etc.
        "range": str,  # Price range
        "note": str,  # Additional notes
    },
    
    # Enhanced interactions (already in drug_interactions field)
    "drug_interactions": {
        "major": list,  # List of major interactions
        "moderate": list,  # List of moderate interactions
        "minor": list,  # List of minor interactions
    },
}


def get_enhanced_fields_list():
    """Get list of all enhanced field names"""
    return list(ENHANCED_FIELDS_TEMPLATE.keys())


def check_drug_enhancement_status(drug_data: dict) -> dict:
    """
    Check which enhanced fields are present in a drug
    
    Args:
        drug_data: Drug data dictionary
    
    Returns:
        Dictionary with field status
    """
    status = {
        "total_fields": len(ENHANCED_FIELDS_TEMPLATE),
        "present_fields": 0,
        "missing_fields": [],
        "present_field_names": [],
        "completeness_percent": 0.0,
    }
    
    for field_name in ENHANCED_FIELDS_TEMPLATE.keys():
        if field_name in drug_data and drug_data[field_name] is not None:
            status["present_fields"] += 1
            status["present_field_names"].append(field_name)
        else:
            status["missing_fields"].append(field_name)
    
    if status["total_fields"] > 0:
        status["completeness_percent"] = (
            status["present_fields"] / status["total_fields"] * 100
        )
    
    return status


def get_priority_fields():
    """Get list of priority fields that should be added first"""
    return [
        "mechanism_of_action",
        "pharmacokinetics",
        "monitoring",
        "black_box_warnings",
        "precautions",
        "storage",
        "brand_names",
        "cost_estimate",
    ]


def get_safety_fields():
    """Get list of safety-related fields"""
    return [
        "black_box_warnings",
        "contraindications",
        "overdose_management",
        "reversal_agents",
    ]


def get_special_population_fields():
    """Get list of special population fields"""
    return [
        "pediatric_dosing",
        "geriatric_dosing",
        "pregnancy_lactation",
        "renal_adjustment",
        "hepatic_adjustment",
    ]


__all__ = [
    'ENHANCED_FIELDS_TEMPLATE',
    'get_enhanced_fields_list',
    'check_drug_enhancement_status',
    'get_priority_fields',
    'get_safety_fields',
    'get_special_population_fields',
]

