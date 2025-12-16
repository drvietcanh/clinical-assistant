"""
SOFA Score Lookup Tables & Functions
Optimized scoring using lookup tables
"""


def lookup_score_descending(value: float, thresholds: list, default_score: int = 0) -> int:
    """
    Generic lookup function for values where higher is better (descending thresholds)
    
    Args:
        value: Value to look up
        thresholds: List of (threshold, score) tuples, sorted descending
        default_score: Score if value is below all thresholds
    
    Returns:
        Score based on value
    
    Example:
        thresholds = [(400, 0), (300, 1), (200, 2), (100, 3)]
        value = 250 -> returns 1 (because 250 >= 200 but < 300)
    """
    for threshold, score in thresholds:
        if value >= threshold:
            return score
    return default_score


def lookup_score_ascending(value: float, thresholds: list, default_score: int = 0) -> int:
    """
    Generic lookup function for values where lower is better (ascending thresholds)
    
    Args:
        value: Value to look up
        thresholds: List of (threshold, score) tuples, sorted ascending
        default_score: Score if value is above all thresholds
    
    Returns:
        Score based on value
    
    Example:
        thresholds = [(1.2, 0), (2.0, 1), (6.0, 2), (12.0, 3)]
        value = 3.5 -> returns 2 (because 3.5 >= 2.0 but < 6.0)
    """
    for threshold, score in thresholds:
        if value < threshold:
            return score
    return default_score


# 1. RESPIRATORY (PaO2/FiO2) - Higher is better
# Thresholds: >= 400 = 0, >= 300 = 1, >= 200 = 2, >= 100 = 3, < 100 = 4
RESPIRATORY_THRESHOLDS = [
    (400.0, 0),
    (300.0, 1),
    (200.0, 2),
    (100.0, 3),
]

def get_respiratory_score(pao2_fio2: float) -> int:
    """Calculate SOFA respiratory score from PaO2/FiO2 ratio"""
    return lookup_score_descending(pao2_fio2, RESPIRATORY_THRESHOLDS, default_score=4)


# 2. COAGULATION (Platelets) - Higher is better
# Thresholds: >= 150 = 0, >= 100 = 1, >= 50 = 2, >= 20 = 3, < 20 = 4
COAGULATION_THRESHOLDS = [
    (150.0, 0),
    (100.0, 1),
    (50.0, 2),
    (20.0, 3),
]

def get_coagulation_score(platelets: float) -> int:
    """Calculate SOFA coagulation score from platelet count"""
    return lookup_score_descending(platelets, COAGULATION_THRESHOLDS, default_score=4)


# 3. LIVER (Bilirubin) - Lower is better
# Thresholds: < 1.2 = 0, < 2.0 = 1, < 6.0 = 2, < 12.0 = 3, >= 12.0 = 4
LIVER_THRESHOLDS = [
    (1.2, 0),
    (2.0, 1),
    (6.0, 2),
    (12.0, 3),
]

def get_liver_score(bilirubin: float) -> int:
    """Calculate SOFA liver score from bilirubin"""
    return lookup_score_ascending(bilirubin, LIVER_THRESHOLDS, default_score=4)


# 4. CENTRAL NERVOUS SYSTEM (GCS) - Higher is better
# Thresholds: 15 = 0, 13-14 = 1, 10-12 = 2, 6-9 = 3, 3-5 = 4
CNS_THRESHOLDS = [
    (15, 0),
    (13, 1),
    (10, 2),
    (6, 3),
]

def get_cns_score(gcs: int) -> int:
    """Calculate SOFA CNS score from GCS"""
    return lookup_score_descending(float(gcs), [(t, s) for t, s in CNS_THRESHOLDS], default_score=4)


# 5. RENAL (Creatinine) - Lower is better
# Thresholds: < 1.2 = 0, < 2.0 = 1, < 3.5 = 2, < 5.0 = 3, >= 5.0 = 4
RENAL_CREATININE_THRESHOLDS = [
    (1.2, 0),
    (2.0, 1),
    (3.5, 2),
    (5.0, 3),
]

def get_renal_creatinine_score(creatinine: float) -> int:
    """Calculate SOFA renal score from creatinine"""
    return lookup_score_ascending(creatinine, RENAL_CREATININE_THRESHOLDS, default_score=4)


# 6. RENAL (Urine Output) - Higher is better
# Thresholds: >= 500 = 0, >= 200 = 3, < 200 = 4
# Note: Urine output has non-standard thresholds (0, then jumps to 3, then 4)
RENAL_URINE_OUTPUT_THRESHOLDS = [
    (500.0, 0),
    (200.0, 3),
]

def get_renal_urine_output_score(urine_output: float) -> int:
    """Calculate SOFA renal score from urine output"""
    return lookup_score_descending(urine_output, RENAL_URINE_OUTPUT_THRESHOLDS, default_score=4)


def get_renal_score(creatinine: float, urine_output: float) -> tuple[int, str]:
    """
    Calculate SOFA renal score from both creatinine and urine output
    Uses the higher (worse) score
    
    Returns:
        Tuple of (score, detail_string)
    """
    renal_by_cr = get_renal_creatinine_score(creatinine)
    renal_by_uo = get_renal_urine_output_score(urine_output)
    
    score = max(renal_by_cr, renal_by_uo)
    
    if renal_by_uo > renal_by_cr:
        detail = f"**Thận:** UO = {urine_output:.0f} mL/24h → {score} điểm"
    else:
        detail = f"**Thận:** Creatinine = {creatinine:.1f} mg/dL → {score} điểm"
    
    return score, detail





















