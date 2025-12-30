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


def normalize_symptom(symptom):
    """Normalize symptom name for matching"""
    if not symptom:
        return ""
    # Convert to lowercase, replace underscores with spaces, strip
    normalized = symptom.lower().replace("_", " ").strip()
    # Remove extra spaces
    normalized = " ".join(normalized.split())
    return normalized


def expand_symptom_aliases(symptom):
    """Expand symptom using aliases"""
    normalized = normalize_symptom(symptom)
    aliases = [normalized]  # Start with normalized symptom
    
    # Check if symptom matches any alias key
    for alias_key, alias_list in SYMPTOM_ALIASES.items():
        alias_key_normalized = normalize_symptom(alias_key)
        # If symptom matches alias key or any value in alias list
        if normalized == alias_key_normalized or normalized in [normalize_symptom(a) for a in alias_list]:
            aliases.extend([normalize_symptom(a) for a in alias_list])
            aliases.append(alias_key_normalized)
    
    # Also check if any alias value matches
    for alias_key, alias_list in SYMPTOM_ALIASES.items():
        for alias_value in alias_list:
            if normalize_symptom(alias_value) == normalized:
                aliases.extend([normalize_symptom(a) for a in alias_list])
                aliases.append(normalize_symptom(alias_key))
    
    # Remove duplicates and return
    return list(set(aliases))


def symptoms_match(user_symptom, diagnosis_symptom):
    """Check if user symptom matches diagnosis symptom (with aliases)"""
    user_normalized = normalize_symptom(user_symptom)
    dx_normalized = normalize_symptom(diagnosis_symptom)
    
    # Exact match
    if user_normalized == dx_normalized:
        return True
    
    # Substring match (one contains the other)
    if user_normalized in dx_normalized or dx_normalized in user_normalized:
        return True
    
    # Check aliases
    user_aliases = expand_symptom_aliases(user_symptom)
    dx_aliases = expand_symptom_aliases(diagnosis_symptom)
    
    # Check if any alias matches
    for ua in user_aliases:
        for da in dx_aliases:
            if ua == da:
                return True
            if ua in da or da in ua:
                return True
    
    return False


def get_symptom_matches(user_symptoms, diagnosis_symptoms):
    """Calculate symptom matches for a diagnosis (improved with aliases)"""
    matches = {
        "required": 0,
        "supporting": 0,
        "contradictory": 0
    }
    
    # Track which symptoms have been matched to avoid double counting
    matched_symptoms = set()
    
    for symptom in user_symptoms:
        if symptom in matched_symptoms:
            continue
        
        # Check required symptoms
        for req in diagnosis_symptoms.get("required", []):
            if symptoms_match(symptom, req):
                matches["required"] += 1
                matched_symptoms.add(symptom)
                break
        
        # If not matched to required, check supporting
        if symptom not in matched_symptoms:
            for sup in diagnosis_symptoms.get("supporting", []):
                if symptoms_match(symptom, sup):
                    matches["supporting"] += 1
                    matched_symptoms.add(symptom)
                    break
        
        # If not matched yet, check contradictory
        if symptom not in matched_symptoms:
            for contr in diagnosis_symptoms.get("contradictory", []):
                if symptoms_match(symptom, contr):
                    matches["contradictory"] += 1
                    matched_symptoms.add(symptom)
                    break
    
    return matches


def suggest_scenarios_from_symptoms(user_symptoms: list) -> list:
    """
    Suggest most relevant scenarios based on user symptoms
    Returns list of (scenario_name, match_score) tuples sorted by score
    
    Args:
        user_symptoms: List of symptom strings (can be Vietnamese or English)
    
    Returns:
        List of tuples (scenario_name, score) sorted by score descending
    """
    if not user_symptoms:
        return []
    
    scenario_scores = {}
    
    for scenario_name, scenario_data in ALL_SCENARIOS.items():
        total_matches = 0
        total_required = 0
        total_supporting = 0
        
        for diagnosis_name, diagnosis_data in scenario_data.items():
            dx_symptoms = diagnosis_data.get("symptoms", {})
            required_symptoms = dx_symptoms.get("required", [])
            supporting_symptoms = dx_symptoms.get("supporting", [])
            
            total_required += len(required_symptoms)
            total_supporting += len(supporting_symptoms)
            
            # Count matches
            matches = get_symptom_matches(user_symptoms, dx_symptoms)
            total_matches += matches["required"] * 3 + matches["supporting"]  # Weight required higher
        
        # Calculate score: ratio of matched symptoms to total symptoms
        total_possible = total_required * 3 + total_supporting
        if total_possible > 0:
            score = (total_matches / total_possible) * 100
            # Also consider number of diagnoses in scenario (more diagnoses = more relevant)
            score *= (1 + len(scenario_data) * 0.1)  # Slight boost for scenarios with more diagnoses
            scenario_scores[scenario_name] = score
    
    # Sort by score descending
    sorted_scenarios = sorted(
        scenario_scores.items(),
        key=lambda x: x[1],
        reverse=True
    )
    
    # Return top scenarios with score > 0
    return [(name, score) for name, score in sorted_scenarios if score > 0]
