"""
eGFR-based Dosing Lookup Module
Tra cứu liều dùng kháng sinh dựa trên eGFR từ file ab_data_from_xlsx.json
Tích hợp với hệ thống dosing calculator hiện tại
"""

import json
from pathlib import Path
from typing import Optional, Dict, Any

# Mapping tên thuốc giữa ab_data_from_xlsx.json và ANTIBIOTICS_DATABASE
DRUG_NAME_MAPPING = {
    # Meropenem
    "Meropenem": ["Meropenem 1g", "Meropenem 0.5g"],
    "Meropenem 1g": "Meropenem 1g",
    "Meropenem 0.5g": "Meropenem 0.5g",
    
    # Vancomycin
    "Vancomycin": ["Vancomycin 1g", "Vancomycin 0.5g"],
    "Vancomycin 1g": "Vancomycin 1g",
    "Vancomycin 0.5g": "Vancomycin 0.5g",
    
    # Ceftriaxone
    "Ceftriaxone": ["Ceftriaxone 2g", "Ceftriaxone 1g"],
    "Ceftriaxone 1g": "Ceftriaxone 1g",
    "Ceftriaxone 2g": "Ceftriaxone 2g",
    
    # Piperacillin/Tazobactam
    "Piperacillin-Tazobactam": "Piperacillin/Tazobactam 4.5 g",
    "Piperacillin/Tazobactam": "Piperacillin/Tazobactam 4.5 g",
    "Piperacillin/Tazobactam 4.5 g": "Piperacillin/Tazobactam 4.5 g",
    
    # Ampicillin/Sulbactam
    "Ampicillin-Sulbactam": "Ampicillin/Sulbactam 1/0.5g",
    "Ampicillin/Sulbactam": "Ampicillin/Sulbactam 1/0.5g",
    "Ampicillin/Sulbactam 1/0.5g": "Ampicillin/Sulbactam 1/0.5g",
    
    # Cefoperazone/Sulbactam
    "Cefoperazone-Sulbactam": "Cefoperazone/Sulbactam 0.5/0.5g",
    "Cefoperazone/Sulbactam": "Cefoperazone/Sulbactam 0.5/0.5g",
    "Cefoperazone/Sulbactam 0.5/0.5g": "Cefoperazone/Sulbactam 0.5/0.5g",
    
    # Ertapenem
    "Ertapenem": "Ertapenem 1 g",
    "Ertapenem 1 g": "Ertapenem 1 g",
    "Ertapenem 1g": "Ertapenem 1 g",
    
    # Imipenem/cilastatin
    "Imipenem-Cilastatin": "Imipenem/cilastatin 0.5/0.5g",
    "Imipenem/cilastatin": "Imipenem/cilastatin 0.5/0.5g",
    "Imipenem/cilastatin 0.5/0.5g": "Imipenem/cilastatin 0.5/0.5g",
    
    # Fluoroquinolones
    "Ciprofloxacin": "Ciprofloxacin 0.4g",
    "Ciprofloxacin 0.4g": "Ciprofloxacin 0.4g",
    "Levofloxacin": ["Levofloxacin 0.75g", "Levofloxacin 0.5g"],
    "Levofloxacin 0.5g": "Levofloxacin 0.5g",
    "Levofloxacin 0.75g": "Levofloxacin 0.75g",
    "Moxifloxacin": "Moxifloxacin 0.4g",
    "Moxifloxacin 0.4g": "Moxifloxacin 0.4g",
    
    # Glycopeptides
    "Teicoplanin": "Teicoplanin 0.4g",
    "Teicoplanin 0.4g": "Teicoplanin 0.4g",
    
    # Polymyxins
    "Colistin": "Colistin 2 M IU",
    "Colistin 2 M IU": "Colistin 2 M IU",
    
    # Others
    "Metronidazole": "Metronidazole 0.5g",
    "Metronidazole 0.5g": "Metronidazole 0.5g",
    "Linezolid": "Linezolid 0.6g",
    "Linezolid 0.6g": "Linezolid 0.6g",
    "Clindamycin": "Clindamycin 0.6g",
    "Clindamycin 0.6g": "Clindamycin 0.6g",
    "Fosfomycin": "Fosfomycin 1g",
    "Fosfomycin 1g": "Fosfomycin 1g",
    
    # Ceftazidime
    "Ceftazidime": "Ceftazidime 2g",
    "Ceftazidime 2g": "Ceftazidime 2g",
}

# Cache để tránh đọc file nhiều lần
_dosing_data_cache: Optional[Dict[str, Any]] = None
_warnings_data_cache: Optional[Dict[str, Any]] = None


def load_egfr_dosing_data() -> Dict[str, Any]:
    """Load dữ liệu từ ab_data_from_xlsx.json"""
    global _dosing_data_cache
    
    if _dosing_data_cache is not None:
        return _dosing_data_cache
    
    try:
        file_path = Path(__file__).parent.parent / "ab_data_from_xlsx.json"
        with open(file_path, 'r', encoding='utf-8') as f:
            _dosing_data_cache = json.load(f)
        return _dosing_data_cache
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}


def load_warnings_data() -> Dict[str, Any]:
    """Load dữ liệu cảnh báo từ ab_data_warnings.json"""
    global _warnings_data_cache
    
    if _warnings_data_cache is not None:
        return _warnings_data_cache
    
    try:
        file_path = Path(__file__).parent.parent / "ab_data_warnings.json"
        with open(file_path, 'r', encoding='utf-8') as f:
            _warnings_data_cache = json.load(f)
        return _warnings_data_cache
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}


def get_egfr_range(egfr_value: float) -> str:
    """
    Xác định khoảng eGFR từ giá trị eGFR
    
    Args:
        egfr_value: Giá trị eGFR (mL/min/1.73m²)
    
    Returns:
        String key cho khoảng eGFR
    """
    if egfr_value > 80:
        return "eGFR > 80"
    elif egfr_value >= 60:
        return "eGFR từ 60-80"
    elif egfr_value >= 50:
        return "eGFR từ 50-60"
    elif egfr_value >= 40:
        return "eGFR từ 40-50"
    elif egfr_value >= 30:
        return "eGFR từ 30-40"
    elif egfr_value >= 20:
        return "eGFR từ 20-30"
    elif egfr_value >= 10:
        return "eGFR từ 10-20"
    else:
        return "eGFR < 10"


def map_drug_name(drug_name: str) -> Optional[str]:
    """
    Map tên thuốc từ ANTIBIOTICS_DATABASE sang tên trong ab_data_from_xlsx.json
    
    Args:
        drug_name: Tên thuốc từ database
    
    Returns:
        Tên thuốc trong JSON hoặc None nếu không tìm thấy
    """
    # Thử tìm trực tiếp
    if drug_name in DRUG_NAME_MAPPING:
        mapped = DRUG_NAME_MAPPING[drug_name]
        if isinstance(mapped, list):
            # Nếu có nhiều lựa chọn, trả về cái đầu tiên (có thể cải thiện logic sau)
            return mapped[0]
        return mapped
    
    # Thử tìm với các biến thể
    drug_name_lower = drug_name.lower()
    for key, value in DRUG_NAME_MAPPING.items():
        if key.lower() in drug_name_lower or drug_name_lower in key.lower():
            if isinstance(value, list):
                return value[0]
            return value
    
    return None


def lookup_egfr_dosing(
    drug_name: str, 
    egfr_value: float, 
    is_dialysis: bool = False
) -> Optional[str]:
    """
    Tra cứu liều dùng dựa trên eGFR
    
    Args:
        drug_name: Tên thuốc (từ ANTIBIOTICS_DATABASE hoặc trực tiếp)
        egfr_value: Giá trị eGFR (mL/min/1.73m²)
        is_dialysis: Có đang lọc máu không
    
    Returns:
        String mô tả liều dùng hoặc None nếu không tìm thấy
    """
    dosing_data = load_egfr_dosing_data()
    
    if not dosing_data:
        return None
    
    # Map tên thuốc
    mapped_name = map_drug_name(drug_name)
    if not mapped_name:
        # Thử tìm trực tiếp với tên gốc
        mapped_name = drug_name
    
    if mapped_name not in dosing_data:
        return None
    
    drug_dosing = dosing_data[mapped_name]
    
    # Ưu tiên lọc máu nếu có
    if is_dialysis and "Chạy thận" in drug_dosing:
        return drug_dosing["Chạy thận"]
    
    # Tra cứu theo eGFR
    egfr_range = get_egfr_range(egfr_value)
    return drug_dosing.get(egfr_range)


def get_drug_warning(drug_name: str) -> Optional[Dict[str, Any]]:
    """
    Lấy cảnh báo cho thuốc
    
    Args:
        drug_name: Tên thuốc
    
    Returns:
        Dict chứa cảnh báo hoặc None
    """
    warnings_data = load_warnings_data()
    
    if not warnings_data or "warnings" not in warnings_data:
        return None
    
    warnings = warnings_data["warnings"]
    
    # Thử tìm trực tiếp
    if drug_name in warnings:
        return warnings[drug_name]
    
    # Thử với mapping
    mapped_name = map_drug_name(drug_name)
    if mapped_name and mapped_name in warnings:
        return warnings[mapped_name]
    
    return None


def get_drug_note(drug_name: str) -> Optional[str]:
    """
    Lấy ghi chú cho thuốc
    
    Args:
        drug_name: Tên thuốc
    
    Returns:
        String ghi chú hoặc None
    """
    warnings_data = load_warnings_data()
    
    if not warnings_data or "notes" not in warnings_data:
        return None
    
    notes = warnings_data["notes"]
    
    # Thử tìm trực tiếp
    if drug_name in notes:
        return notes[drug_name]
    
    # Thử với mapping
    mapped_name = map_drug_name(drug_name)
    if mapped_name and mapped_name in notes:
        return notes[mapped_name]
    
    return None


def is_drug_in_egfr_database(drug_name: str) -> bool:
    """
    Kiểm tra xem thuốc có trong database eGFR không
    
    Args:
        drug_name: Tên thuốc
    
    Returns:
        True nếu có, False nếu không
    """
    dosing_data = load_egfr_dosing_data()
    
    if not dosing_data:
        return False
    
    mapped_name = map_drug_name(drug_name)
    if not mapped_name:
        mapped_name = drug_name
    
    return mapped_name in dosing_data


def get_all_available_drugs() -> list:
    """
    Lấy danh sách tất cả thuốc có trong database eGFR
    
    Returns:
        List tên thuốc
    """
    dosing_data = load_egfr_dosing_data()
    return list(dosing_data.keys()) if dosing_data else []


# Export functions
__all__ = [
    'lookup_egfr_dosing',
    'get_egfr_range',
    'map_drug_name',
    'get_drug_warning',
    'get_drug_note',
    'is_drug_in_egfr_database',
    'get_all_available_drugs',
    'load_egfr_dosing_data',
    'load_warnings_data'
]

