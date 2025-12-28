"""
Drug Compatibility Checker
Check compatibility between drugs for mixing and Y-site administration
"""

import json
from pathlib import Path
from typing import Dict, List, Optional, Tuple


def _load_compatibility_database() -> Dict:
    """Load compatibility database from JSON file."""
    db_path = Path(__file__).parent / "compatibility_database.json"
    try:
        with open(db_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}


COMPATIBILITY_DB = _load_compatibility_database()


def check_compatibility(drug1: str, drug2: str) -> Dict:
    """
    Check compatibility between two drugs.
    
    Args:
        drug1: Name of first drug
        drug2: Name of second drug
    
    Returns:
        Dictionary with compatibility result:
        {
            "is_compatible": bool,
            "status": str,  # "compatible", "incompatible", "conditional"
            "message": str,
            "notes": str,
            "y_site": bool,
            "recommendations": List[str]
        }
    """
    if drug1 == drug2:
        return {
            "is_compatible": True,
            "status": "compatible",
            "message": "Cùng một loại thuốc",
            "notes": "",
            "y_site": True,
            "recommendations": []
        }
    
    compatibility = COMPATIBILITY_DB.get("compatibility", {})
    
    # Check drug1 -> drug2
    drug1_info = compatibility.get(drug1, {})
    drug2_info = compatibility.get(drug2, {})
    
    if not drug1_info or not drug2_info:
        return {
            "is_compatible": None,
            "status": "unknown",
            "message": f"Không có thông tin tương thích cho {drug1} và {drug2}",
            "notes": "Vui lòng tra cứu tài liệu hoặc hỏi dược sĩ",
            "y_site": False,
            "recommendations": ["Tra cứu tài liệu", "Hỏi dược sĩ"]
        }
    
    # Check incompatible list
    drug1_incompatible = drug1_info.get("incompatible", [])
    drug2_incompatible = drug2_info.get("incompatible", [])
    
    if drug2 in drug1_incompatible or drug1 in drug2_incompatible:
        return {
            "is_compatible": False,
            "status": "incompatible",
            "message": f"⚠️ {drug1} và {drug2} KHÔNG TƯƠNG THÍCH",
            "notes": drug1_info.get("notes", "") + " " + drug2_info.get("notes", ""),
            "y_site": False,
            "recommendations": [
                "KHÔNG trộn hai thuốc này",
                "Dùng riêng biệt",
                "Kiểm tra lại compatibility trước khi dùng"
            ]
        }
    
    # Check conditional
    drug1_conditional = drug1_info.get("conditional", {})
    drug2_conditional = drug2_info.get("conditional", {})
    
    if drug2 in drug1_conditional:
        conditional_note = drug1_conditional[drug2]
        return {
            "is_compatible": True,
            "status": "conditional",
            "message": f"⚠️ {drug1} và {drug2} có thể trộn nhưng CẦN THEO DÕI",
            "notes": conditional_note,
            "y_site": True,
            "recommendations": [
                "Có thể trộn nhưng cần theo dõi sát",
                "Kiểm tra màu sắc và độ trong của dung dịch",
                "Theo dõi tác dụng phụ",
                "Ghi chép lại nếu có bất thường"
            ]
        }
    
    if drug1 in drug2_conditional:
        conditional_note = drug2_conditional[drug1]
        return {
            "is_compatible": True,
            "status": "conditional",
            "message": f"⚠️ {drug1} và {drug2} có thể trộn nhưng CẦN THEO DÕI",
            "notes": conditional_note,
            "y_site": True,
            "recommendations": [
                "Có thể trộn nhưng cần theo dõi sát",
                "Kiểm tra màu sắc và độ trong của dung dịch",
                "Theo dõi tác dụng phụ",
                "Ghi chép lại nếu có bất thường"
            ]
        }
    
    # Check compatible list
    drug1_compatible = drug1_info.get("compatible", [])
    drug2_compatible = drug2_info.get("compatible", [])
    
    if drug2 in drug1_compatible or drug1 in drug2_compatible:
        y_site_info = drug1_info.get("y_site", {})
        y_site_compatible = y_site_info.get("compatible", True)
        
        return {
            "is_compatible": True,
            "status": "compatible",
            "message": f"✅ {drug1} và {drug2} TƯƠNG THÍCH",
            "notes": drug1_info.get("notes", ""),
            "y_site": y_site_compatible,
            "recommendations": [
                "Có thể trộn an toàn",
                "Có thể dùng Y-site" if y_site_compatible else "Không nên dùng Y-site",
                "Kiểm tra màu sắc và độ trong sau khi trộn"
            ]
        }
    
    # Default: unknown
    return {
        "is_compatible": None,
        "status": "unknown",
        "message": f"Không rõ tương thích giữa {drug1} và {drug2}",
        "notes": "Vui lòng tra cứu tài liệu",
        "y_site": False,
        "recommendations": ["Tra cứu tài liệu", "Hỏi dược sĩ"]
    }


def check_multiple_compatibility(drugs: List[str]) -> Dict:
    """
    Check compatibility of multiple drugs.
    
    Args:
        drugs: List of drug names
    
    Returns:
        Dictionary with compatibility matrix and summary:
        {
            "drugs": List[str],
            "matrix": Dict[Tuple[str, str], Dict],
            "all_compatible": bool,
            "incompatible_pairs": List[Tuple[str, str]],
            "conditional_pairs": List[Tuple[str, str]],
            "recommendations": List[str]
        }
    """
    if len(drugs) < 2:
        return {
            "drugs": drugs,
            "matrix": {},
            "all_compatible": True,
            "incompatible_pairs": [],
            "conditional_pairs": [],
            "recommendations": []
        }
    
    matrix = {}
    incompatible_pairs = []
    conditional_pairs = []
    
    # Check all pairs
    for i, drug1 in enumerate(drugs):
        for j, drug2 in enumerate(drugs):
            if i < j:  # Only check upper triangle
                result = check_compatibility(drug1, drug2)
                matrix[(drug1, drug2)] = result
                
                if result["status"] == "incompatible":
                    incompatible_pairs.append((drug1, drug2))
                elif result["status"] == "conditional":
                    conditional_pairs.append((drug1, drug2))
    
    # Generate recommendations
    recommendations = []
    
    if incompatible_pairs:
        recommendations.append("⚠️ CÓ THUỐC KHÔNG TƯƠNG THÍCH - KHÔNG NÊN TRỘN")
        for pair in incompatible_pairs:
            recommendations.append(f"  - {pair[0]} và {pair[1]} không tương thích")
    
    if conditional_pairs:
        recommendations.append("⚠️ CÓ THUỐC CẦN THEO DÕI KHI TRỘN")
        for pair in conditional_pairs:
            recommendations.append(f"  - {pair[0]} và {pair[1]} cần theo dõi")
    
    if not incompatible_pairs and not conditional_pairs:
        recommendations.append("✅ TẤT CẢ THUỐC TƯƠNG THÍCH")
        recommendations.append("  - Có thể trộn an toàn")
        recommendations.append("  - Có thể dùng Y-site")
    
    return {
        "drugs": drugs,
        "matrix": matrix,
        "all_compatible": len(incompatible_pairs) == 0,
        "incompatible_pairs": incompatible_pairs,
        "conditional_pairs": conditional_pairs,
        "recommendations": recommendations
    }


def get_compatible_drugs(drug_name: str) -> List[str]:
    """
    Get list of compatible drugs for a given drug.
    
    Args:
        drug_name: Name of drug
    
    Returns:
        List of compatible drug names
    """
    compatibility = COMPATIBILITY_DB.get("compatibility", {})
    drug_info = compatibility.get(drug_name, {})
    return drug_info.get("compatible", [])


def get_incompatible_drugs(drug_name: str) -> List[str]:
    """
    Get list of incompatible drugs for a given drug.
    
    Args:
        drug_name: Name of drug
    
    Returns:
        List of incompatible drug names
    """
    compatibility = COMPATIBILITY_DB.get("compatibility", {})
    drug_info = compatibility.get(drug_name, {})
    return drug_info.get("incompatible", [])

