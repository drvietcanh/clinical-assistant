"""
APACHE II Lookup Tables & Generic Lookup Functions
Optimized scoring using lookup tables
"""


def lookup_score(value: float, thresholds: list, default_score: int = 0) -> int:
    """
    Generic lookup function for APACHE II scoring
    
    Args:
        value: Value to look up
        thresholds: List of (threshold, score) tuples, sorted descending
        default_score: Score if value is below all thresholds
    
    Returns:
        Score based on value
    """
    for threshold, score in thresholds:
        if value >= threshold:
            return score
    return default_score


def lookup_score_reverse(value: float, thresholds: list, default_score: int = 0) -> int:
    """
    Lookup for values where lower is worse (e.g., PaO2, pH when low)
    
    Args:
        value: Value to look up
        thresholds: List of (threshold, score) tuples, sorted ascending
        default_score: Score if value is above all thresholds
    
    Returns:
        Score based on value
    """
    for threshold, score in reversed(thresholds):
        if value <= threshold:
            return score
    return default_score


# Temperature scoring - Special case (both high and low are bad)
TEMP_THRESHOLDS_HIGH = [
    (41.0, 4),
    (39.0, 3),
    (38.5, 1),
    (36.0, 0),
]

TEMP_THRESHOLDS_LOW = [
    (34.0, 1),
    (32.0, 2),
    (30.0, 3),
]

def get_temp_score(temp: float) -> int:
    """Temperature score using lookup tables"""
    # High temperatures
    if temp >= 36.0:
        return lookup_score(temp, TEMP_THRESHOLDS_HIGH, default_score=0)
    # Low temperatures
    else:
        score = lookup_score(temp, TEMP_THRESHOLDS_LOW, default_score=4)
        return score


# MAP scoring lookup
MAP_THRESHOLDS = [
    (160.0, 4),
    (130.0, 3),
    (110.0, 2),
    (70.0, 0),
    (50.0, 2),
]

def get_map_score(map_val: float) -> int:
    """MAP score using lookup table"""
    return lookup_score(map_val, MAP_THRESHOLDS, default_score=4)


# Heart rate scoring lookup
HR_THRESHOLDS_HIGH = [
    (180.0, 4),
    (140.0, 3),
    (110.0, 2),
    (70.0, 0),
]

HR_THRESHOLDS_LOW = [
    (55.0, 2),
    (40.0, 3),
]

def get_hr_score(hr: float) -> int:
    """Heart rate score using lookup tables"""
    if hr >= 70.0:
        return lookup_score(hr, HR_THRESHOLDS_HIGH, default_score=0)
    else:
        return lookup_score(hr, HR_THRESHOLDS_LOW, default_score=4)


# Respiratory rate scoring lookup
RR_THRESHOLDS = [
    (50.0, 4),
    (35.0, 3),
    (25.0, 1),
    (12.0, 0),
    (10.0, 1),
    (6.0, 2),
]

def get_rr_score(rr: float) -> int:
    """Respiratory rate score using lookup table"""
    return lookup_score(rr, RR_THRESHOLDS, default_score=4)


# pH scoring - Special case (both high and low are bad)
PH_THRESHOLDS_HIGH = [
    (7.7, 4),
    (7.6, 3),
    (7.5, 1),
    (7.33, 0),
]

PH_THRESHOLDS_LOW = [
    (7.25, 2),
    (7.15, 3),
]

def get_ph_score(ph: float) -> int:
    """Arterial pH score using lookup tables"""
    if ph >= 7.33:
        return lookup_score(ph, PH_THRESHOLDS_HIGH, default_score=0)
    else:
        return lookup_score(ph, PH_THRESHOLDS_LOW, default_score=4)


# Sodium scoring lookup
NA_THRESHOLDS = [
    (180.0, 4),
    (160.0, 3),
    (155.0, 2),
    (150.0, 1),
    (130.0, 0),
    (120.0, 2),
    (111.0, 3),
]

def get_na_score(na: float) -> int:
    """Sodium score using lookup table"""
    return lookup_score(na, NA_THRESHOLDS, default_score=4)


# Potassium scoring lookup
K_THRESHOLDS_HIGH = [
    (7.0, 4),
    (6.0, 3),
    (5.5, 1),
    (3.5, 0),
]

K_THRESHOLDS_LOW = [
    (3.0, 1),
    (2.5, 2),
]

def get_k_score(k: float) -> int:
    """Potassium score using lookup tables"""
    if k >= 3.5:
        return lookup_score(k, K_THRESHOLDS_HIGH, default_score=0)
    else:
        return lookup_score(k, K_THRESHOLDS_LOW, default_score=4)


# Creatinine scoring lookup
CR_THRESHOLDS = [
    (3.5, 4),
    (2.0, 3),
    (1.5, 2),
    (0.6, 0),
]

def get_cr_score(cr: float, has_arf: bool) -> int:
    """Creatinine score using lookup table (doubled if ARF)"""
    base_score = lookup_score(cr, CR_THRESHOLDS, default_score=2)
    return base_score * 2 if has_arf else base_score


# Hematocrit scoring lookup
HCT_THRESHOLDS = [
    (60.0, 4),
    (50.0, 2),
    (46.0, 1),
    (30.0, 0),
    (20.0, 2),
]

def get_hct_score(hct: float) -> int:
    """Hematocrit score using lookup table"""
    return lookup_score(hct, HCT_THRESHOLDS, default_score=4)


# WBC scoring lookup
WBC_THRESHOLDS = [
    (40.0, 4),
    (20.0, 2),
    (15.0, 1),
    (3.0, 0),
    (1.0, 2),
]

def get_wbc_score(wbc: float) -> int:
    """WBC score using lookup table"""
    return lookup_score(wbc, WBC_THRESHOLDS, default_score=4)


# Age scoring lookup
AGE_THRESHOLDS = [
    (75, 6),
    (65, 5),
    (55, 3),
    (45, 2),
]

def get_age_score(age: int) -> int:
    """Age score using lookup table"""
    return lookup_score(age, AGE_THRESHOLDS, default_score=0)


# Oxygenation - Special case (logic based on FiO2)
def get_oxygenation_score(fio2: float, pao2: float, paco2: float, ph: float) -> int:
    """Oxygenation score - A-a gradient if FiO2≥50%, else PaO2"""
    if fio2 >= 50:  # Use A-a gradient
        # A-a gradient = [(FiO2 × (Patm - PH2O)) - (PaCO2/0.8)] - PaO2
        # Simplified: ≈ (FiO2 × 713) - (PaCO2/0.8) - PaO2
        aa_gradient = (fio2 * 7.13) - (paco2 / 0.8) - pao2
        
        AA_GRADIENT_THRESHOLDS = [
            (500, 4),
            (350, 3),
            (200, 2),
        ]
        return lookup_score(aa_gradient, AA_GRADIENT_THRESHOLDS, default_score=0)
    else:  # Use PaO2 (lower is worse)
        PAO2_THRESHOLDS = [
            (70, 0),
            (60, 1),
            (55, 3),
        ]
        return lookup_score_reverse(pao2, PAO2_THRESHOLDS, default_score=4)


# Chronic health score - Simple logic
def get_chronic_health_score(
    has_chronic: bool,
    is_post_emergency_surgery: bool,
    is_nonsurgical: bool
) -> int:
    """Chronic health points"""
    if not has_chronic:
        return 0
    
    if is_nonsurgical or is_post_emergency_surgery:
        return 5
    else:  # Elective post-op
        return 2


# GCS score - Simple calculation
def get_gcs_score(gcs: int) -> int:
    """Glasgow Coma Scale score (15 - GCS)"""
    return 15 - gcs
