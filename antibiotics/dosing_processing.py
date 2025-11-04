"""
Antibiotic Dosing Calculator - Processing Functions
Parse dosage text, calculate infusion details
"""

def parse_dosage_text(dosage_text):
    """
    Parse dosage text to extract mg/kg, interval, etc.
    Returns dict with parsed components
    Enhanced parsing with more patterns
    """
    import re
    result = {
        'dose_per_kg': None,
        'total_dose': None,
        'dose_min': None,
        'dose_max': None,
        'interval_hours': None,
        'frequency': None,
        'route': None
    }
    
    # Look for mg/kg pattern (can be range: "15-20mg/kg")
    mg_kg_match = re.search(r'(\d+(?:\.\d+)?)(?:\s*-\s*(\d+(?:\.\d+)?))?\s*mg/kg', dosage_text, re.IGNORECASE)
    if mg_kg_match:
        result['dose_per_kg'] = float(mg_kg_match.group(1))
        if mg_kg_match.group(2):  # Has range
            result['dose_max'] = float(mg_kg_match.group(2))
    
    # Look for total dose (g or mg) - can be range
    # Pattern: "1-2g", "500mg-1g", "1g"
    total_range_match = re.search(r'(\d+(?:\.\d+)?)\s*(g|mg)\s*(?:-|đến|to)\s*(\d+(?:\.\d+)?)\s*(g|mg)', dosage_text, re.IGNORECASE)
    if total_range_match:
        val1 = float(total_range_match.group(1))
        unit1 = total_range_match.group(2).lower()
        val2 = float(total_range_match.group(3))
        unit2 = total_range_match.group(4).lower()
        
        val1_mg = val1 * 1000 if unit1 == 'g' else val1
        val2_mg = val2 * 1000 if unit2 == 'g' else val2
        
        result['dose_min'] = min(val1_mg, val2_mg)
        result['total_dose'] = max(val1_mg, val2_mg)
        result['dose_max'] = max(val1_mg, val2_mg)
    else:
        total_match = re.search(r'(\d+(?:\.\d+)?)\s*(g|mg)', dosage_text, re.IGNORECASE)
        if total_match:
            value = float(total_match.group(1))
            unit = total_match.group(2).lower()
            result['total_dose'] = value * 1000 if unit == 'g' else value
    
    # Look for interval (multiple patterns)
    # "mỗi 8 giờ", "mỗi 8h", "q8h", "mỗi 8-12 giờ"
    interval_match = re.search(r'(?:mỗi|q)\s*(\d+)(?:\s*-\s*(\d+))?\s*(?:giờ|h|hours)', dosage_text, re.IGNORECASE)
    if interval_match:
        interval = int(interval_match.group(1))
        if interval_match.group(2):  # Has range
            interval_max = int(interval_match.group(2))
            result['interval_hours'] = (interval + interval_max) / 2  # Average
        else:
            result['interval_hours'] = interval
    
    # Look for frequency
    # "2 lần/ngày", "x 2 lần/ngày", "bid", "tid", "qid"
    freq_match = re.search(r'(?:x\s*)?(\d+)\s*lần/ngày', dosage_text, re.IGNORECASE)
    if freq_match:
        result['frequency'] = int(freq_match.group(1))
        result['interval_hours'] = 24 / result['frequency']
    else:
        # Check for bid/tid/qid
        if re.search(r'\bbid\b', dosage_text, re.IGNORECASE):
            result['frequency'] = 2
            result['interval_hours'] = 12
        elif re.search(r'\btid\b', dosage_text, re.IGNORECASE):
            result['frequency'] = 3
            result['interval_hours'] = 8
        elif re.search(r'\bqid\b', dosage_text, re.IGNORECASE):
            result['frequency'] = 4
            result['interval_hours'] = 6
    
    # Detect route
    if re.search(r'\bIV\b', dosage_text, re.IGNORECASE):
        result['route'] = 'IV'
    elif re.search(r'\bIM\b', dosage_text, re.IGNORECASE):
        result['route'] = 'IM'
    elif re.search(r'\bPO\b', dosage_text, re.IGNORECASE):
        result['route'] = 'PO'
    
    return result



def calculate_infusion_details(calculated_dose_mg, antibiotic_name, route="IV"):
    """
    Calculate infusion time and concentration
    Returns: dict with infusion_time_minutes, volume_ml, concentration_mg_ml
    """
    # Default infusion parameters by antibiotic
    infusion_params = {
        "Vancomycin": {"time_min": 60, "max_conc_mg_ml": 5, "max_rate_mg_min": 10},
        "Gentamicin": {"time_min": 30, "max_conc_mg_ml": 10, "max_rate_mg_min": 20},
        "Tobramycin": {"time_min": 30, "max_conc_mg_ml": 10, "max_rate_mg_min": 20},
        "Amikacin": {"time_min": 30, "max_conc_mg_ml": 5, "max_rate_mg_min": 20},
        "Piperacillin-Tazobactam": {"time_min": 30, "max_conc_mg_ml": 10, "max_rate_mg_min": 30},
        "Meropenem": {"time_min": 30, "max_conc_mg_ml": 20, "max_rate_mg_min": 50},
        "Imipenem-Cilastatin": {"time_min": 30, "max_conc_mg_ml": 5, "max_rate_mg_min": 25},
        "Ceftriaxone": {"time_min": 30, "max_conc_mg_ml": 40, "max_rate_mg_min": 50},
        "Cefepime": {"time_min": 30, "max_conc_mg_ml": 40, "max_rate_mg_min": 50},
    }
    
    # Get parameters for this antibiotic (or defaults)
    params = infusion_params.get(antibiotic_name, {"time_min": 30, "max_conc_mg_ml": 10, "max_rate_mg_min": 20})
    
    # Calculate concentration (try to use reasonable volume)
    volume_ml = max(50, calculated_dose_mg / params["max_conc_mg_ml"] * 2)  # Use 2x max to be safe
    volume_ml = round(volume_ml / 50) * 50  # Round to nearest 50ml
    concentration_mg_ml = calculated_dose_mg / volume_ml
    
    # Ensure concentration doesn't exceed max
    if concentration_mg_ml > params["max_conc_mg_ml"]:
        volume_ml = round(calculated_dose_mg / params["max_conc_mg_ml"] / 10) * 10  # Round to nearest 10ml
        concentration_mg_ml = calculated_dose_mg / volume_ml
    
    # Calculate infusion time based on rate
    infusion_time_minutes = max(params["time_min"], (calculated_dose_mg / params["max_rate_mg_min"]))
    infusion_time_minutes = round(infusion_time_minutes / 5) * 5  # Round to nearest 5 minutes
    
    return {
        "infusion_time_minutes": infusion_time_minutes,
        "volume_ml": volume_ml,
        "concentration_mg_ml": concentration_mg_ml,
        "infusion_time_hours": infusion_time_minutes / 60
    }



