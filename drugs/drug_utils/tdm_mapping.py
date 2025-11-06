"""
TDM Mapping Utilities
Map drug names from database to TDM config
"""

from drugs.tdm.tdm_config import TDM_DRUGS

# Mapping từ drug database names → TDM config keys
# Case-insensitive matching sẽ được xử lý trong function
DRUG_TO_TDM_MAP = {
    # Exact matches - common drug names
    "Digoxin": "digoxin",
    "Phenytoin": "phenytoin",
    "Lithium": "lithium",
    "Theophylline": "theophylline",
    "Tacrolimus": "tacrolimus",
    "Cyclosporine": "cyclosporine",
    "Cyclosporin": "cyclosporine",  # Alternative spelling
    "Vancomycin": "vancomycin",
    "Carbamazepine": "carbamazepine",
    "Valproic Acid": "valproic_acid",
    "Valproate": "valproic_acid",
    "Sodium Valproate": "valproic_acid",
    
    # Aminoglycosides
    "Amikacin": "amikacin",
    "Gentamicin": "gentamicin",
    "Tobramycin": "tobramycin",
    "Netilmicin": "netilmicin",
    
    # Cardiovascular
    "Amiodarone": "amiodarone",
    "Lidocaine": "lidocaine",
    "Quinidine": "quinidine",
    "Flecainide": "flecainide",
    "Mexiletine": "mexiletine",
    
    # Antiepileptics
    "Phenobarbital": "phenobarbital",
    
    # Immunosuppressants
    "Sirolimus": "sirolimus",
    "Everolimus": "everolimus",
    
    # Antifungals
    "Voriconazole": "voriconazole",
    "Posaconazole": "posaconazole",
    
    # Others
    "Methotrexate": "methotrexate",
    "Isoniazid": "isoniazid",
    "INH": "isoniazid",  # Common abbreviation
}


def get_tdm_info(drug_name: str) -> dict:
    """
    Get TDM info for a drug
    Returns None if drug doesn't have TDM
    
    Args:
        drug_name: Name of the drug (from database)
    
    Returns:
        dict: TDM info from TDM_DRUGS config, or None if not found
    """
    if not drug_name:
        return None
    
    drug_lower = drug_name.lower().strip()
    
    # 1. Check direct mapping first
    if drug_name in DRUG_TO_TDM_MAP:
        tdm_key = DRUG_TO_TDM_MAP[drug_name]
        if tdm_key in TDM_DRUGS:
            return TDM_DRUGS[tdm_key]
    
    # 2. Try case-insensitive match in TDM_DRUGS by name
    for tdm_key, tdm_info in TDM_DRUGS.items():
        if tdm_info['name'].lower() == drug_lower:
            return tdm_info
    
    # 3. Try partial match (drug name contains TDM name or vice versa)
    for tdm_key, tdm_info in TDM_DRUGS.items():
        tdm_name_lower = tdm_info['name'].lower()
        if drug_lower in tdm_name_lower or tdm_name_lower in drug_lower:
            return tdm_info
    
    # 4. Try matching with common variations
    # Remove common suffixes/prefixes
    drug_clean = drug_lower.replace("sodium ", "").replace(" hydrochloride", "").replace(" hcl", "")
    for tdm_key, tdm_info in TDM_DRUGS.items():
        tdm_name_clean = tdm_info['name'].lower().replace("sodium ", "").replace(" hydrochloride", "").replace(" hcl", "")
        if drug_clean == tdm_name_clean:
            return tdm_info
    
    return None


def has_tdm(drug_name: str) -> bool:
    """
    Check if drug has TDM
    
    Args:
        drug_name: Name of the drug
    
    Returns:
        bool: True if drug has TDM, False otherwise
    """
    return get_tdm_info(drug_name) is not None


def get_tdm_calculator_name(drug_name: str) -> str:
    """
    Get the TDM calculator function name for a drug
    Used to route to correct calculator in TDM module
    
    Args:
        drug_name: Name of the drug
    
    Returns:
        str: Calculator name (e.g., "Digoxin", "Phenytoin"), or None
    """
    tdm_info = get_tdm_info(drug_name)
    if not tdm_info:
        return None
    
    # Map to calculator names used in TDM module
    calculator_map = {
        "digoxin": "Digoxin",
        "phenytoin": "Phenytoin",
        "lithium": "Lithium",
        "theophylline": "Theophylline",
        "tacrolimus": "Tacrolimus",
        "cyclosporine": "Tacrolimus",  # Uses immunosuppressants calculator
        "vancomycin": "Vancomycin",
        "carbamazepine": "Carbamazepine",
        "valproic_acid": "Valproic",
        "amikacin": "Amikacin",
        "gentamicin": "Gentamicin",
        "tobramycin": "Tobramycin",
        "netilmicin": "Netilmicin",
    }
    
    tdm_key = None
    for key, info in TDM_DRUGS.items():
        if info == tdm_info:
            tdm_key = key
            break
    
    if tdm_key and tdm_key in calculator_map:
        return calculator_map[tdm_key]
    
    # Default: return drug name from TDM info
    return tdm_info.get('name', None)

