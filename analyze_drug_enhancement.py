"""
Analyze Drug Database Enhancement Status
Day 1 Phase 2: Structure Analysis
"""

import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from drugs.drug_database import DRUG_DATABASE
from drugs.drug_utils.enhancement_analyzer import (
    analyze_drug_database,
    get_enhancement_priority_list,
    print_enhancement_report,
)


def main():
    """Run enhancement analysis"""
    print("🔍 Analyzing Drug Database Enhancement Status...")
    print()
    
    # Analyze database
    analysis = analyze_drug_database(DRUG_DATABASE)
    
    # Print report
    print_enhancement_report(analysis)
    
    # Get priority list
    print("=" * 80)
    print("🎯 TOP 30 PRIORITY DRUGS FOR ENHANCEMENT")
    print("=" * 80)
    print()
    
    priority_list = get_enhancement_priority_list(DRUG_DATABASE, top_n=30)
    
    for i, (drug_name, score, missing_fields) in enumerate(priority_list, 1):
        print(f"{i:2d}. {drug_name:30s} | Score: {score:6.1f} | Missing: {', '.join(missing_fields[:3])}")
        if len(missing_fields) > 3:
            print(f"    {'':30s} | {'':6s} |       + {len(missing_fields) - 3} more")
    
    print()
    print("=" * 80)
    print("✅ Analysis Complete")
    print("=" * 80)
    
    return analysis


if __name__ == "__main__":
    analysis = main()
    
    # Save summary
    print()
    print("📊 Summary:")
    print(f"  Total drugs: {analysis['total_drugs']}")
    print(f"  High completeness (≥80%): {len(analysis['enhancement_stats']['high_completeness'])}")
    print(f"  Medium completeness (50-80%): {len(analysis['enhancement_stats']['medium_completeness'])}")
    print(f"  Low completeness (<50%): {len(analysis['enhancement_stats']['low_completeness'])}")
    print(f"  Priority drugs: {len(analysis['priority_drugs'])}")
    print(f"  Safety critical drugs: {len(analysis['safety_critical_drugs'])}")

