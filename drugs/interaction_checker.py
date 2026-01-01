"""
Drug Interaction Checker
Algorithm to check interactions between multiple drugs
"""

from typing import List, Dict, Tuple
from itertools import combinations

try:
    from .drug_interactions import (
        DRUG_INTERACTIONS,
        SEVERITY_MAJOR,
        SEVERITY_MODERATE,
        SEVERITY_MINOR,
        get_interaction,
        get_all_interactions_for_drug
    )
except ImportError:
    from drug_interactions import (
        DRUG_INTERACTIONS,
        SEVERITY_MAJOR,
        SEVERITY_MODERATE,
        SEVERITY_MINOR,
        get_interaction,
        get_all_interactions_for_drug
    )


class DrugInteractionChecker:
    """
    Check drug-drug interactions for a list of medications
    """
    
    def __init__(self):
        self.interactions_db = DRUG_INTERACTIONS
    
    def check_pair(self, drug1: str, drug2: str) -> Dict:
        """
        Check interaction between two drugs
        
        Args:
            drug1: First drug name
            drug2: Second drug name
        
        Returns:
            Interaction dict or None
        """
        return get_interaction(drug1, drug2)
    
    def check_multiple(self, drug_list: List[str]) -> List[Dict]:
        """
        Check interactions for multiple drugs
        
        Args:
            drug_list: List of drug names
        
        Returns:
            List of interaction dicts with drug pairs
        """
        if len(drug_list) < 2:
            return []
        
        interactions = []
        
        # Check all pairs
        for drug1, drug2 in combinations(drug_list, 2):
            interaction = self.check_pair(drug1, drug2)
            if interaction:
                interactions.append({
                    'drug1': drug1,
                    'drug2': drug2,
                    'severity': interaction['severity'],
                    'effect': interaction['effect'],
                    'mechanism': interaction['mechanism'],
                    'management': interaction['management'],
                    'references': interaction['references']
                })
        
        # Sort by severity (Major > Moderate > Minor)
        severity_order = {SEVERITY_MAJOR: 0, SEVERITY_MODERATE: 1, SEVERITY_MINOR: 2}
        interactions.sort(key=lambda x: severity_order[x['severity']])
        
        return interactions
    
    def check_new_drug(self, current_drugs: List[str], new_drug: str) -> List[Dict]:
        """
        Check if adding a new drug will cause interactions
        
        Args:
            current_drugs: List of current medications
            new_drug: New drug to add
        
        Returns:
            List of interactions with the new drug
        """
        interactions = []
        
        for current_drug in current_drugs:
            interaction = self.check_pair(current_drug, new_drug)
            if interaction:
                interactions.append({
                    'drug1': current_drug,
                    'drug2': new_drug,
                    'severity': interaction['severity'],
                    'effect': interaction['effect'],
                    'mechanism': interaction['mechanism'],
                    'management': interaction['management'],
                    'references': interaction['references']
                })
        
        # Sort by severity
        severity_order = {SEVERITY_MAJOR: 0, SEVERITY_MODERATE: 1, SEVERITY_MINOR: 2}
        interactions.sort(key=lambda x: severity_order[x['severity']])
        
        return interactions
    
    def get_summary(self, drug_list: List[str]) -> Dict:
        """
        Get summary of interactions
        
        Args:
            drug_list: List of drug names
        
        Returns:
            Summary dict with counts and risk level
        """
        interactions = self.check_multiple(drug_list)
        
        major_count = sum(1 for i in interactions if i['severity'] == SEVERITY_MAJOR)
        moderate_count = sum(1 for i in interactions if i['severity'] == SEVERITY_MODERATE)
        minor_count = sum(1 for i in interactions if i['severity'] == SEVERITY_MINOR)
        
        # Determine overall risk level
        if major_count > 0:
            risk_level = "HIGH"
            risk_color = "red"
        elif moderate_count > 0:
            risk_level = "MODERATE"
            risk_color = "orange"
        elif minor_count > 0:
            risk_level = "LOW"
            risk_color = "yellow"
        else:
            risk_level = "NONE"
            risk_color = "green"
        
        return {
            'total_interactions': len(interactions),
            'major': major_count,
            'moderate': moderate_count,
            'minor': minor_count,
            'risk_level': risk_level,
            'risk_color': risk_color,
            'has_major': major_count > 0,
            'has_moderate': moderate_count > 0,
            'interactions': interactions
        }
    
    def generate_report(self, drug_list: List[str]) -> str:
        """
        Generate a text report of interactions
        
        Args:
            drug_list: List of drug names
        
        Returns:
            Formatted text report
        """
        summary = self.get_summary(drug_list)
        
        report = []
        report.append("=" * 60)
        report.append("DRUG INTERACTION REPORT")
        report.append("=" * 60)
        report.append(f"\nMedications ({len(drug_list)}):")
        for i, drug in enumerate(drug_list, 1):
            report.append(f"  {i}. {drug}")
        
        report.append(f"\nRisk Level: {summary['risk_level']}")
        report.append(f"Total Interactions: {summary['total_interactions']}")
        report.append(f"  - Major: {summary['major']}")
        report.append(f"  - Moderate: {summary['moderate']}")
        report.append(f"  - Minor: {summary['minor']}")
        
        if summary['interactions']:
            report.append("\n" + "=" * 60)
            report.append("DETAILED INTERACTIONS")
            report.append("=" * 60)
            
            for idx, interaction in enumerate(summary['interactions'], 1):
                report.append(f"\n{idx}. {interaction['drug1']} + {interaction['drug2']}")
                report.append(f"   Severity: {interaction['severity']}")
                report.append(f"   Effect: {interaction['effect']}")
                report.append(f"   Mechanism: {interaction['mechanism']}")
                report.append(f"   Management: {interaction['management']}")
                report.append(f"   References: {', '.join(interaction['references'])}")
        else:
            report.append("\nNo interactions found.")
        
        report.append("\n" + "=" * 60)
        
        return "\n".join(report)
    
    def get_recommendations(self, drug_list: List[str]) -> List[str]:
        """
        Get clinical recommendations based on interactions
        
        Args:
            drug_list: List of drug names
        
        Returns:
            List of recommendation strings
        """
        summary = self.get_summary(drug_list)
        recommendations = []
        
        if summary['has_major']:
            recommendations.append(
                "⚠️ MAJOR INTERACTIONS DETECTED - Avoid combination if possible"
            )
            recommendations.append(
                "Consider alternative medications or consult specialist"
            )
        
        if summary['has_moderate']:
            recommendations.append(
                "⚠️ MODERATE INTERACTIONS - Monitor patient closely"
            )
            recommendations.append(
                "Adjust doses as needed and watch for adverse effects"
            )
        
        if summary['total_interactions'] == 0:
            recommendations.append(
                "✅ No known interactions detected"
            )
        
        # Add specific management from interactions
        for interaction in summary['interactions']:
            if interaction['severity'] == SEVERITY_MAJOR:
                recommendations.append(
                    f"• {interaction['drug1']} + {interaction['drug2']}: "
                    f"{interaction['management'][:100]}..."
                )
        
        return recommendations


# Convenience functions
def check_drug_interactions(drug_list: List[str]) -> List[Dict]:
    """
    Quick function to check interactions
    
    Args:
        drug_list: List of drug names
    
    Returns:
        List of interaction dicts
    """
    checker = DrugInteractionChecker()
    return checker.check_multiple(drug_list)


def check_adding_drug(current_drugs: List[str], new_drug: str) -> List[Dict]:
    """
    Quick function to check if adding a drug causes interactions
    
    Args:
        current_drugs: Current medication list
        new_drug: New drug to add
    
    Returns:
        List of interactions
    """
    checker = DrugInteractionChecker()
    return checker.check_new_drug(current_drugs, new_drug)


def get_interaction_summary(drug_list: List[str]) -> Dict:
    """
    Quick function to get interaction summary
    
    Args:
        drug_list: List of drug names
    
    Returns:
        Summary dict
    """
    checker = DrugInteractionChecker()
    return checker.get_summary(drug_list)


# Example usage
if __name__ == "__main__":
    # Example 1: Check multiple drugs
    print("Example 1: Multiple drug check")
    print("-" * 60)
    
    medications = ["Warfarin", "Aspirin", "Metformin"]
    checker = DrugInteractionChecker()
    
    summary = checker.get_summary(medications)
    print(f"Risk Level: {summary['risk_level']}")
    print(f"Total Interactions: {summary['total_interactions']}")
    
    for interaction in summary['interactions']:
        print(f"\n[!] {interaction['drug1']} + {interaction['drug2']}")
        print(f"   Severity: {interaction['severity']}")
        print(f"   Effect: {interaction['effect']}")
    
    # Example 2: Check adding new drug
    print("\n\n" + "=" * 60)
    print("Example 2: Adding new drug")
    print("-" * 60)
    
    current = ["Warfarin", "Metformin"]
    new = "Aspirin"
    
    new_interactions = checker.check_new_drug(current, new)
    
    if new_interactions:
        print(f"[!] WARNING: Adding {new} will cause {len(new_interactions)} interaction(s):")
        for interaction in new_interactions:
            print(f"\n  * {interaction['drug1']} + {interaction['drug2']}")
            print(f"    Severity: {interaction['severity']}")
            print(f"    Effect: {interaction['effect']}")
    else:
        print(f"[OK] No interactions with {new}")
    
    # Example 3: Generate report
    print("\n\n" + "=" * 60)
    print("Example 3: Full Report")
    print("-" * 60)
    
    report = checker.generate_report(medications)
    print(report)
    
    # Example 4: Get recommendations
    print("\n\n" + "=" * 60)
    print("Example 4: Clinical Recommendations")
    print("-" * 60)
    
    recommendations = checker.get_recommendations(medications)
    for rec in recommendations:
        print(rec)


__all__ = [
    'DrugInteractionChecker',
    'check_drug_interactions',
    'check_adding_drug',
    'get_interaction_summary'
]
