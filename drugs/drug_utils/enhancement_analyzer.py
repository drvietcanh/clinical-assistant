"""
Drug Enhancement Analyzer
Analyzes current drug database and identifies gaps in enhanced fields
"""

from typing import Dict, List, Tuple
from .enhanced_fields_template import (
    check_drug_enhancement_status,
    get_priority_fields,
    get_safety_fields,
    get_special_population_fields,
)


def analyze_drug_database(drug_database: dict) -> dict:
    """
    Analyze entire drug database for enhancement status
    
    Args:
        drug_database: Complete drug database dictionary
    
    Returns:
        Analysis results dictionary
    """
    results = {
        "total_drugs": len(drug_database),
        "drugs_analyzed": 0,
        "enhancement_stats": {
            "high_completeness": [],  # > 80%
            "medium_completeness": [],  # 50-80%
            "low_completeness": [],  # < 50%
        },
        "missing_fields_summary": {},
        "priority_drugs": [],  # Drugs missing priority fields
        "safety_critical_drugs": [],  # Drugs missing safety fields
    }
    
    priority_fields = get_priority_fields()
    safety_fields = get_safety_fields()
    
    for drug_name, drug_data in drug_database.items():
        status = check_drug_enhancement_status(drug_data)
        results["drugs_analyzed"] += 1
        
        # Categorize by completeness
        if status["completeness_percent"] >= 80:
            results["enhancement_stats"]["high_completeness"].append({
                "drug": drug_name,
                "completeness": status["completeness_percent"],
            })
        elif status["completeness_percent"] >= 50:
            results["enhancement_stats"]["medium_completeness"].append({
                "drug": drug_name,
                "completeness": status["completeness_percent"],
            })
        else:
            results["enhancement_stats"]["low_completeness"].append({
                "drug": drug_name,
                "completeness": status["completeness_percent"],
            })
        
        # Track missing fields
        for field in status["missing_fields"]:
            if field not in results["missing_fields_summary"]:
                results["missing_fields_summary"][field] = []
            results["missing_fields_summary"][field].append(drug_name)
        
        # Check priority fields
        missing_priority = [f for f in priority_fields if f in status["missing_fields"]]
        if missing_priority:
            results["priority_drugs"].append({
                "drug": drug_name,
                "missing_fields": missing_priority,
            })
        
        # Check safety fields
        missing_safety = [f for f in safety_fields if f in status["missing_fields"]]
        if missing_safety:
            results["safety_critical_drugs"].append({
                "drug": drug_name,
                "missing_fields": missing_safety,
            })
    
    return results


def get_enhancement_priority_list(drug_database: dict, top_n: int = 50) -> List[Tuple[str, float, List[str]]]:
    """
    Get prioritized list of drugs that need enhancement
    
    Args:
        drug_database: Complete drug database
        top_n: Number of drugs to return
    
    Returns:
        List of tuples: (drug_name, completeness_score, missing_priority_fields)
    """
    priority_list = []
    priority_fields = get_priority_fields()
    
    for drug_name, drug_data in drug_database.items():
        status = check_drug_enhancement_status(drug_data)
        
        # Calculate priority score (lower completeness = higher priority)
        # Also prioritize drugs missing critical fields
        missing_priority = [f for f in priority_fields if f in status["missing_fields"]]
        priority_score = 100 - status["completeness_percent"] + (len(missing_priority) * 10)
        
        priority_list.append((
            drug_name,
            priority_score,
            missing_priority,
        ))
    
    # Sort by priority score (descending)
    priority_list.sort(key=lambda x: x[1], reverse=True)
    
    return priority_list[:top_n]


def print_enhancement_report(analysis_results: dict):
    """Print formatted enhancement analysis report"""
    print("=" * 80)
    print("📊 DRUG DATABASE ENHANCEMENT ANALYSIS")
    print("=" * 80)
    print()
    
    print(f"Total Drugs: {analysis_results['total_drugs']}")
    print(f"Drugs Analyzed: {analysis_results['drugs_analyzed']}")
    print()
    
    print("📈 Completeness Distribution:")
    print(f"  High (≥80%): {len(analysis_results['enhancement_stats']['high_completeness'])}")
    print(f"  Medium (50-80%): {len(analysis_results['enhancement_stats']['medium_completeness'])}")
    print(f"  Low (<50%): {len(analysis_results['enhancement_stats']['low_completeness'])}")
    print()
    
    print("🔍 Most Missing Fields:")
    missing_fields = analysis_results['missing_fields_summary']
    sorted_fields = sorted(missing_fields.items(), key=lambda x: len(x[1]), reverse=True)
    for field, drugs in sorted_fields[:10]:
        print(f"  {field}: {len(drugs)} drugs missing")
    print()
    
    print(f"⚠️  Priority Drugs (missing core fields): {len(analysis_results['priority_drugs'])}")
    print(f"🚨 Safety Critical Drugs (missing safety fields): {len(analysis_results['safety_critical_drugs'])}")
    print()


__all__ = [
    'analyze_drug_database',
    'get_enhancement_priority_list',
    'print_enhancement_report',
]

