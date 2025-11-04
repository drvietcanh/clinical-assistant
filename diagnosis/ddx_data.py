"""
DDx Knowledge Base
Differential diagnosis data for common clinical scenarios

NOTE: Data dictionaries đã được tách ra file ddx_data_data.py
File này chứa functions và import data để giữ backward compatibility
"""

from .ddx_data_data import (
    CHEST_PAIN_DDX,
    DYSPNEA_DDX,
    ABDOMINAL_PAIN_DDX,
    ALTERED_MENTAL_STATUS_DDX,
    FEVER_DDX,
    SYNCOPE_DDX,
    JOINT_PAIN_DDX,
    HEADACHE_DDX,
    DIARRHEA_DDX,
    ANEMIA_DDX,
    KIDNEY_INJURY_DDX,
    HTN_EMERGENCY_DDX,
    VOMITING_DDX,
    RASH_DDX,
    ALL_SCENARIOS,
    SYMPTOM_ALIASES
)

def get_scenario_data(scenario_name):
    """Get DDx data for a scenario"""
    return ALL_SCENARIOS.get(scenario_name, {})


def get_all_scenarios():
    """Get list of all available scenarios"""
    return list(ALL_SCENARIOS.keys())


def get_symptom_matches(user_symptoms, diagnosis_symptoms):
    """Calculate symptom matches for a diagnosis"""
    matches = {
        "required": 0,
        "supporting": 0,
        "contradictory": 0
    }
    
    for symptom in user_symptoms:
        symptom_lower = symptom.lower()
        
        # Check required symptoms
        for req in diagnosis_symptoms.get("required", []):
            if symptom_lower in req.lower() or req.lower() in symptom_lower:
                matches["required"] += 1
                break
        
        # Check supporting symptoms
        for sup in diagnosis_symptoms.get("supporting", []):
            if symptom_lower in sup.lower() or sup.lower() in symptom_lower:
                matches["supporting"] += 1
                break
        
        # Check contradictory symptoms
        for contr in diagnosis_symptoms.get("contradictory", []):
            if symptom_lower in contr.lower() or contr.lower() in symptom_lower:
                matches["contradictory"] += 1
                break
    
    return matches

