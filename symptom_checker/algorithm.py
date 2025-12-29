"""
Symptom Checker Algorithm
Analyze symptoms and suggest diagnoses with probability
"""

from typing import List, Dict, Tuple
from symptom_checker.data import (
    get_symptom_diagnosis_mapping,
    get_urgent_symptoms,
    SYMPTOM_DATABASE
)


def analyze_symptoms(symptom_list: List[str]) -> List[Dict]:
    """
    Analyze a list of symptoms and return suggested diagnoses with probability
    
    Args:
        symptom_list: List of symptom names
        
    Returns:
        List of diagnosis suggestions with probability scores
    """
    if not symptom_list:
        return []
    
    # Get DDx mapping
    ddx_mapping = get_symptom_diagnosis_mapping()
    if not ddx_mapping:
        return []
    
    # Normalize symptoms
    normalized_symptoms = [s.lower().strip() for s in symptom_list]
    
    # Score each diagnosis
    diagnosis_scores = {}
    
    for scenario_name, scenario_data in ddx_mapping.items():
        score = 0.0
        required_count = 0
        supporting_count = 0
        
        symptoms_data = scenario_data.get('symptoms', {})
        required_symptoms = symptoms_data.get('required', [])
        supporting_symptoms = symptoms_data.get('supporting', [])
        contradictory_symptoms = symptoms_data.get('contradictory', [])
        
        # Check required symptoms (higher weight)
        for req_symptom in required_symptoms:
            if matches_symptom(req_symptom, normalized_symptoms):
                required_count += 1
                score += 3.0  # High weight for required symptoms
        
        # Check supporting symptoms
        for sup_symptom in supporting_symptoms:
            if matches_symptom(sup_symptom, normalized_symptoms):
                supporting_count += 1
                score += 1.0  # Lower weight for supporting symptoms
        
        # Check contradictory symptoms (reduce score)
        for contra_symptom in contradictory_symptoms:
            if matches_symptom(contra_symptom, normalized_symptoms):
                score -= 2.0  # Penalty for contradictory symptoms
        
        # Calculate probability (normalize to 0-1)
        total_possible = len(required_symptoms) * 3.0 + len(supporting_symptoms) * 1.0
        if total_possible > 0:
            probability = max(0.0, min(1.0, score / total_possible))
        else:
            probability = 0.0
        
        # Only include if has some required symptoms or high supporting score
        if required_count > 0 or (supporting_count >= 2 and probability > 0.3):
            diagnosis_scores[scenario_name] = {
                'diagnosis': scenario_name,
                'probability': probability,
                'required_matched': required_count,
                'supporting_matched': supporting_count,
                'total_required': len(required_symptoms),
                'total_supporting': len(supporting_symptoms),
                'data': scenario_data
            }
    
    # Sort by probability (descending)
    results = sorted(
        diagnosis_scores.values(),
        key=lambda x: x['probability'],
        reverse=True
    )
    
    # Return top 10
    return results[:10]


def matches_symptom(symptom_key: str, user_symptoms: List[str]) -> bool:
    """Check if symptom_key matches any user symptom"""
    symptom_lower = symptom_key.lower().replace('_', ' ')
    
    for user_symptom in user_symptoms:
        user_lower = user_symptom.lower().replace('_', ' ')
        
        # Exact match
        if symptom_lower == user_lower:
            return True
        
        # Substring match
        if symptom_lower in user_lower or user_lower in symptom_lower:
            return True
        
        # Check aliases (simple version)
        if check_aliases(symptom_key, user_symptom):
            return True
    
    return False


def check_aliases(symptom_key: str, user_symptom: str) -> bool:
    """Check if symptom matches through aliases"""
    try:
        from diagnosis.ddx_data_data import SYMPTOM_ALIASES
        
        symptom_lower = symptom_key.lower()
        user_lower = user_symptom.lower()
        
        # Check if symptom_key is in aliases
        if symptom_lower in SYMPTOM_ALIASES:
            aliases = [a.lower() for a in SYMPTOM_ALIASES[symptom_lower]]
            if user_lower in aliases:
                return True
        
        # Check reverse
        for key, aliases in SYMPTOM_ALIASES.items():
            if symptom_lower == key.lower():
                aliases_lower = [a.lower() for a in aliases]
                if user_lower in aliases_lower:
                    return True
    except ImportError:
        pass
    
    return False


def get_diagnosis_suggestions(symptom_list: List[str]) -> List[Dict]:
    """Get diagnosis suggestions (alias for analyze_symptoms)"""
    return analyze_symptoms(symptom_list)


def calculate_severity(symptom_list: List[str]) -> str:
    """
    Calculate overall severity based on symptoms
    
    Returns:
        'mild', 'moderate', 'severe', or 'critical'
    """
    if not symptom_list:
        return 'mild'
    
    urgent_symptoms = get_urgent_symptoms()
    normalized_symptoms = [s.lower().strip() for s in symptom_list]
    
    # Check for urgent symptoms
    has_urgent = any(s in urgent_symptoms for s in normalized_symptoms)
    if has_urgent:
        return 'critical'
    
    # Count severe symptoms
    severe_count = sum(1 for s in SYMPTOM_DATABASE 
                      if s.name.lower() in normalized_symptoms and s.severity == 'severe')
    if severe_count >= 2:
        return 'severe'
    elif severe_count >= 1:
        return 'moderate'
    
    return 'mild'


def check_urgency(symptom_list: List[str]) -> Tuple[bool, str]:
    """
    Check if symptoms require urgent care
    
    Returns:
        (is_urgent, urgency_message)
    """
    severity = calculate_severity(symptom_list)
    
    urgent_symptoms = get_urgent_symptoms()
    normalized_symptoms = [s.lower().strip() for s in symptom_list]
    has_urgent = any(s in urgent_symptoms for s in normalized_symptoms)
    
    if severity == 'critical' or has_urgent:
        return True, "⚠️ CẦN ĐẾN CẤP CỨU NGAY LẬP TỨC"
    elif severity == 'severe':
        return True, "⚠️ Cần được đánh giá sớm (trong vài giờ)"
    elif severity == 'moderate':
        return False, "ℹ️ Có thể đợi đánh giá trong 24-48 giờ"
    else:
        return False, "✅ Có thể theo dõi tại nhà"

