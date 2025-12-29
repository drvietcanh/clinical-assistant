"""
Drug Database Statistics and Access Module
Provides statistics and easy access to drugs by category
Current total: 666 drugs (as of reorganization)
"""

from .drug_modules import (
    CARDIOVASCULAR_DRUGS,
    DIABETES_DRUGS,
    GASTROINTESTINAL_DRUGS,
    ANALGESICS_DRUGS,
    RESPIRATORY_DRUGS,
    NEUROLOGICAL_DRUGS,
    HEMATOLOGY_DRUGS,
    SUPPORTIVE_DRUGS,
    ANTIMICROBIAL_DRUGS,
    METABOLIC_DRUGS,
    ENDOCRINOLOGY_DRUGS,
    ONCOLOGY_DRUGS,
    EMERGENCY_DRUGS,
    UROLOGY_DRUGS,
    DERMATOLOGY_DRUGS,
    OPHTHALMOLOGY_DRUGS,
    OBSTETRICS_GYNECOLOGY_DRUGS,
    ENT_ORAL_NASAL_COMBINATIONS_DRUGS,
    MISCELLANEOUS_DRUGS,
)

# Organized drug modules dictionary for easy access
DRUG_MODULES = {
    "Cardiovascular": CARDIOVASCULAR_DRUGS,
    "Diabetes": DIABETES_DRUGS,
    "Gastrointestinal": GASTROINTESTINAL_DRUGS,
    "Analgesics": ANALGESICS_DRUGS,
    "Respiratory": RESPIRATORY_DRUGS,
    "Neurological": NEUROLOGICAL_DRUGS,
    "Hematology": HEMATOLOGY_DRUGS,
    "Supportive": SUPPORTIVE_DRUGS,
    "Antimicrobial": ANTIMICROBIAL_DRUGS,
    "Metabolic": METABOLIC_DRUGS,
    "Endocrinology": ENDOCRINOLOGY_DRUGS,
    "Oncology": ONCOLOGY_DRUGS,
    "Emergency": EMERGENCY_DRUGS,
    "Urology": UROLOGY_DRUGS,
    "Dermatology": DERMATOLOGY_DRUGS,
    "Ophthalmology": OPHTHALMOLOGY_DRUGS,
    "Obstetrics/Gynecology": OBSTETRICS_GYNECOLOGY_DRUGS,
    "ENT/Oral/Nasal": ENT_ORAL_NASAL_COMBINATIONS_DRUGS,
    "Miscellaneous": MISCELLANEOUS_DRUGS,
}

def get_drug_statistics():
    """
    Get statistics about drugs in each module
    
    Returns:
        dict: Statistics with module names, drug counts, and percentages
    """
    stats = {}
    total = 0
    
    for module_name, drugs in DRUG_MODULES.items():
        count = len(drugs)
        total += count
        stats[module_name] = {
            "count": count,
            "drugs": list(drugs.keys())
        }
    
    # Add percentages
    for module_name in stats:
        stats[module_name]["percentage"] = (stats[module_name]["count"] / total * 100) if total > 0 else 0
    
    stats["_total"] = total
    return stats

def get_drugs_by_module(module_name):
    """
    Get all drugs in a specific module
    
    Args:
        module_name (str): Name of the module
        
    Returns:
        dict: Dictionary of drugs in that module, or None if module not found
    """
    return DRUG_MODULES.get(module_name)

def search_drugs(query, module_name=None):
    """
    Search for drugs by name across all modules or within a specific module
    
    Args:
        query (str): Search query (case-insensitive partial match)
        module_name (str, optional): Limit search to specific module
        
    Returns:
        list: List of tuples (drug_name, module_name, drug_data)
    """
    results = []
    query_lower = query.lower()
    
    modules_to_search = {module_name: DRUG_MODULES[module_name]} if module_name else DRUG_MODULES
    
    for mod_name, drugs in modules_to_search.items():
        for drug_name, drug_data in drugs.items():
            if query_lower in drug_name.lower():
                results.append((drug_name, mod_name, drug_data))
    
    return results

def get_module_list():
    """
    Get list of all available module names
    
    Returns:
        list: List of module names
    """
    return list(DRUG_MODULES.keys())

def print_statistics():
    """
    Print formatted statistics about the drug database
    """
    stats = get_drug_statistics()
    total = stats.pop("_total")
    
    print("=" * 60)
    print("DRUG DATABASE STATISTICS")
    print("=" * 60)
    print(f"\nTotal Drugs: {total}\n")
    print(f"{'Module':<30} {'Count':<10} {'Percentage':<10}")
    print("-" * 60)
    
    # Sort by count (descending)
    sorted_stats = sorted(stats.items(), key=lambda x: x[1]["count"], reverse=True)
    
    for module_name, data in sorted_stats:
        print(f"{module_name:<30} {data['count']:<10} {data['percentage']:.1f}%")
    
    print("=" * 60)

if __name__ == "__main__":
    print_statistics()

