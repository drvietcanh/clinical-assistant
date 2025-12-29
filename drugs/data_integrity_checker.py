"""
Data Integrity Checker - Kiểm tra tính toàn vẹn dữ liệu
Phát hiện các vấn đề về tính nhất quán, tham chiếu, và cấu trúc
"""

from typing import Dict, List, Tuple, Set
from collections import defaultdict
import re
from .drug_database import DRUG_DATABASE
from .enhanced_fields_overrides import EXTRA_ENHANCED_FIELDS

# ============================================================================
# INTEGRITY CHECKS - Kiểm tra tính toàn vẹn
# ============================================================================

def check_cross_references() -> List[Dict]:
    """
    Kiểm tra tham chiếu chéo giữa các thuốc
    
    Ví dụ: drug_interactions tham chiếu đến thuốc khác
    """
    issues = []
    all_drug_names = set(DRUG_DATABASE.keys())
    all_drug_names_lower = {name.lower(): name for name in all_drug_names}
    
    for drug_name, drug_data in DRUG_DATABASE.items():
        # Apply overrides
        if drug_name in EXTRA_ENHANCED_FIELDS:
            drug_data = {**drug_data, **EXTRA_ENHANCED_FIELDS[drug_name]}
        
        # Check drug_interactions
        if "drug_interactions" in drug_data and isinstance(drug_data["drug_interactions"], dict):
            for severity in ["major", "moderate", "minor"]:
                interactions = drug_data["drug_interactions"].get(severity, [])
                for interaction in interactions:
                    if isinstance(interaction, dict) and "drug" in interaction:
                        referenced_drug = interaction["drug"]
                        # Extract drug name (might be "Drug A, Drug B" or "Drug A")
                        referenced_names = [d.strip() for d in referenced_drug.split(",")]
                        
                        for ref_name in referenced_names:
                            # Check if drug exists
                            ref_lower = ref_name.lower()
                            if ref_lower not in all_drug_names_lower:
                                # Check if it's a drug class or generic term
                                if not any(keyword in ref_lower for keyword in ["class", "group", "inhibitor", "blocker", "antagonist"]):
                                    issues.append({
                                        "drug": drug_name,
                                        "field": "drug_interactions",
                                        "issue": "broken_reference",
                                        "message": f"Tham chiếu đến thuốc không tồn tại: '{ref_name}'",
                                        "severity": "warning"
                                    })
        
        # Check reversal_agents
        if "reversal_agents" in drug_data and isinstance(drug_data["reversal_agents"], dict):
            if drug_data["reversal_agents"].get("available", False):
                agents = drug_data["reversal_agents"].get("agents", [])
                for agent in agents:
                    if isinstance(agent, str):
                        agent_lower = agent.lower()
                        if agent_lower not in all_drug_names_lower:
                            # Check if it's a known reversal agent
                            known_agents = ["naloxone", "flumazenil", "protamine", "vitamin k", "atropine"]
                            if not any(known in agent_lower for known in known_agents):
                                issues.append({
                                    "drug": drug_name,
                                    "field": "reversal_agents",
                                    "issue": "unknown_agent",
                                    "message": f"Reversal agent không rõ: '{agent}'",
                                    "severity": "info"
                                })
    
    return issues

def check_dosage_consistency() -> List[Dict]:
    """Kiểm tra tính nhất quán của dosage"""
    issues = []
    
    for drug_name, drug_data in DRUG_DATABASE.items():
        if "dosage" not in drug_data:
            continue
        
        dosage = drug_data["dosage"]
        if not isinstance(dosage, dict):
            continue
        
        # Check for common dosage keys
        expected_keys = ["adult", "adult_standard", "adult_po", "adult_iv", "pediatric"]
        has_any = any(key in dosage for key in expected_keys)
        
        if not has_any and len(dosage) > 0:
            # Might be using custom keys
            issues.append({
                "drug": drug_name,
                "field": "dosage",
                "issue": "non_standard_keys",
                "message": f"Dosage sử dụng keys không chuẩn: {list(dosage.keys())}",
                "severity": "info"
            })
        
        # Check for conflicting dosages
        if "adult_po" in dosage and "adult_iv" in dosage:
            po_val = str(dosage["adult_po"]).lower()
            iv_val = str(dosage["adult_iv"]).lower()
            # Check if they're the same (might be error)
            if po_val == iv_val and "po" in po_val:
                issues.append({
                    "drug": drug_name,
                    "field": "dosage",
                    "issue": "possible_duplicate",
                    "message": "adult_po và adult_iv có giá trị giống nhau - có thể là lỗi",
                    "severity": "warning"
                })
    
    return issues

def check_administration_consistency() -> List[Dict]:
    """Kiểm tra tính nhất quán giữa administration và administration_instructions"""
    issues = []
    
    for drug_name, drug_data in DRUG_DATABASE.items():
        if "administration" not in drug_data:
            continue
        
        admin_list = drug_data["administration"]
        if not isinstance(admin_list, list):
            continue
        
        # Check if administration_instructions matches
        if "administration_instructions" in drug_data:
            admin_inst = drug_data["administration_instructions"]
            if isinstance(admin_inst, dict):
                # Check if instructions exist for all administration routes
                for route in admin_list:
                    route_lower = route.lower()
                    if route_lower == "po" and "oral" not in admin_inst:
                        issues.append({
                            "drug": drug_name,
                            "field": "administration_instructions",
                            "issue": "missing_instruction",
                            "message": f"Có 'PO' trong administration nhưng thiếu 'oral' trong administration_instructions",
                            "severity": "info"
                        })
                    elif route_lower == "iv" and "iv" not in admin_inst:
                        issues.append({
                            "drug": drug_name,
                            "field": "administration_instructions",
                            "issue": "missing_instruction",
                            "message": f"Có 'IV' trong administration nhưng thiếu 'iv' trong administration_instructions",
                            "severity": "info"
                        })
    
    return issues

def check_contraindications_structure() -> List[Dict]:
    """Kiểm tra cấu trúc contraindications"""
    issues = []
    
    for drug_name, drug_data in DRUG_DATABASE.items():
        # Check if has both old and new format
        has_list = "contraindications" in drug_data and isinstance(drug_data["contraindications"], list)
        has_dict = "contraindications" in drug_data and isinstance(drug_data["contraindications"], dict)
        has_detail = "contraindications_detail" in drug_data
        
        if (has_list and has_dict) or (has_list and has_detail):
            issues.append({
                "drug": drug_name,
                "field": "contraindications",
                "issue": "multiple_formats",
                "message": "Có cả contraindications (list) và contraindications (dict/detail) - nên chỉ dùng một",
                "severity": "warning"
            })
    
    return issues

def check_enhanced_fields_completeness() -> List[Dict]:
    """Kiểm tra độ đầy đủ của enhanced fields"""
    from .enhanced_fields_index import get_drug_field_status
    
    issues = []
    
    for drug_name in DRUG_DATABASE.keys():
        status = get_drug_field_status(drug_name)
        
        # Count missing core fields
        missing_core = [f for f, has in status.items() 
                       if not has and f in ["mechanism_of_action", "monitoring", "precautions", 
                                           "pharmacokinetics", "storage", "black_box_warnings"]]
        
        if missing_core:
            issues.append({
                "drug": drug_name,
                "field": "enhanced_fields",
                "issue": "missing_core_fields",
                "message": f"Thiếu {len(missing_core)} core fields: {', '.join(missing_core)}",
                "severity": "warning"
            })
    
    return issues

def check_all_integrity() -> Dict:
    """Chạy tất cả kiểm tra tính toàn vẹn"""
    all_issues = []
    
    all_issues.extend(check_cross_references())
    all_issues.extend(check_dosage_consistency())
    all_issues.extend(check_administration_consistency())
    all_issues.extend(check_contraindications_structure())
    all_issues.extend(check_enhanced_fields_completeness())
    
    # Group by severity
    by_severity = defaultdict(list)
    by_drug = defaultdict(list)
    by_issue_type = defaultdict(int)
    
    for issue in all_issues:
        by_severity[issue["severity"]].append(issue)
        by_drug[issue["drug"]].append(issue)
        by_issue_type[issue["issue"]] += 1
    
    return {
        "total_issues": len(all_issues),
        "by_severity": {k: len(v) for k, v in by_severity.items()},
        "by_issue_type": dict(by_issue_type),
        "drugs_affected": len(by_drug),
        "issues": all_issues,
        "summary": {
            "errors": len(by_severity.get("error", [])),
            "warnings": len(by_severity.get("warning", [])),
            "info": len(by_severity.get("info", [])),
        }
    }

