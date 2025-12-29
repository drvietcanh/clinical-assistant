"""
Auto-generate score mappings for protocols based on protocol names and content.
This script reads all protocols and automatically links relevant scores.
"""

import re
import sys
from pathlib import Path
from typing import Dict, List, Set

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

from scores.config import SCORES_BY_SPECIALTY

PROTOCOLS_DIR = BASE_DIR / "protocols"

# Mapping từ protocol keywords/names đến scores
PROTOCOL_SCORE_KEYWORDS = {
    # Sepsis
    "sepsis": ["SOFA", "qSOFA", "APACHE II", "SAPS II", "SAPS III", "APACHE III", "APACHE IV", "Lactate Clearance", "eGFR", "CrCl", "GCS"],
    "sepsis_3hour": ["SOFA", "qSOFA", "APACHE II", "SAPS II", "eGFR", "CrCl"],
    
    # Stroke
    "stroke": ["NIHSS", "GCS", "mRS", "ICH Score", "ASPECTS", "ABCD2"],
    
    # ACS/Cardiology
    "acs": ["TIMI Risk", "GRACE Score", "HEART Score", "CRUSADE Score", "PRECISE-DAPT", "DAPT Score"],
    "stemi": ["TIMI Risk", "GRACE Score", "Killip"],
    "nstemi": ["TIMI Risk", "GRACE Score", "HEART Score", "CRUSADE Score"],
    "heart_failure": ["NYHA", "Killip", "BNP/NT-proBNP"],
    "acute_decompensated_hf": ["NYHA", "Killip"],
    "atrial_fibrillation": ["CHA2DS2-VASc", "HAS-BLED", "Corrected QT"],
    "dvt_pe": ["Wells PE", "PERC", "PESI", "Wells DVT"],
    "cardiac_tamponade": ["NYHA"],
    "aortic_dissection": ["NYHA"],
    
    # Respiratory
    "ards": ["ARDS Berlin", "SOFA", "APACHE II"],
    "copd": ["BODE Index", "mMRC", "CURB-65"],
    "asthma": ["ACT"],
    "cap": ["CURB-65", "CRB-65 Score", "PSI/PORT", "SMART-COP"],
    "hap_vap": ["SOFA", "APACHE II", "CURB-65"],
    "acute_respiratory_failure": ["ROX Index", "ARDS Berlin", "SOFA"],
    
    # Nephrology
    "aki": ["KDIGO", "RIFLE", "AKIN", "eGFR", "CrCl"],
    "ckd": ["eGFR", "KDIGO"],
    "hepatorenal_syndrome": ["MELD", "MELD-Na", "Child-Pugh"],
    "emergency_dialysis": ["KDIGO", "eGFR"],
    "uti_pyelonephritis": ["eGFR"],
    
    # Gastroenterology
    "acute_pancreatitis": ["BISAP", "Ranson"],
    "acute_liver_failure": ["MELD", "MELD-Na", "Child-Pugh"],
    "decompensated_cirrhosis": ["MELD", "MELD-Na", "Child-Pugh"],
    "cirrhosis": ["MELD", "MELD-Na", "Child-Pugh"],
    "gi_bleeding": ["Glasgow-Blatchford", "Rockall Score", "AIMS65"],
    "lower_gi_bleeding": ["Glasgow-Blatchford", "Rockall Score"],
    "acute_appendicitis": ["Alvarado Score"],
    
    # Emergency
    "dka": ["Anion Gap", "Corrected Sodium", "eGFR", "CrCl"],
    "hhs": ["Anion Gap", "Corrected Sodium", "eGFR", "CrCl"],
    "hypertensive_emergency": ["ASCVD Risk", "SCORE2", "SCORE2-OP"],
    "anaphylaxis": ["BMI/IBW/BSA"],
    "traumatic_brain_injury": ["GCS", "Canadian CT Head"],
    "cardiac_arrest": ["GCS", "APACHE II"],
    "shock": ["SOFA", "Lactate Clearance", "APACHE II"],
    
    # Hematology
    "dic": ["DIC Score", "4Ts Score"],
    "transfusion": ["DIC Score"],
    
    # Obstetrics
    "preeclampsia": ["Preeclampsia", "Bishop Score", "Modified Bishop"],
    "eclampsia": ["Preeclampsia", "Bishop Score"],
    
    # Neurology
    "status_epilepticus": ["GCS"],
    "intracranial_hypertension": ["GCS", "ICH Score"],
    
    # Endocrine
    "hypoglycemia": ["HbA1c"],
    "thyrotoxic_crisis": ["Corrected QT"],
    
    # Infectious
    "meningitis": ["GCS"],
    "endocarditis": ["Duke"],
    
    # Rheumatology
    "acute_gout": ["Gout Diagnostic"],
}


def get_all_protocol_functions() -> Dict[str, str]:
    """Get all protocol function names from protocol_routing.py"""
    routing_file = BASE_DIR / "config" / "protocol_routing.py"
    if not routing_file.exists():
        return {}
    
    content = routing_file.read_text(encoding="utf-8")
    
    # Extract render function names from PROTOCOL_ROUTING
    protocol_functions = {}
    
    # Pattern: "article_function": "render_xxx"
    pattern = r'"article_function":\s*"render_(\w+)"'
    matches = re.findall(pattern, content)
    
    for match in matches:
        protocol_functions[f"render_{match}"] = match
    
    # Also extract from "render": render_xxx
    pattern2 = r'"render":\s*(render_\w+)'
    matches2 = re.findall(pattern2, content)
    
    for match in matches2:
        if match.startswith("render_"):
            protocol_id = match.replace("render_", "")
            protocol_functions[match] = protocol_id
    
    return protocol_functions


def find_scores_for_protocol(protocol_id: str, protocol_function: str) -> List[Dict[str, str]]:
    """Find relevant scores for a protocol based on keywords and content."""
    scores = []
    scores_set = set()  # Track added scores to avoid duplicates
    
    # Check keyword mapping first
    protocol_lower = protocol_id.lower()
    for key, score_list in PROTOCOL_SCORE_KEYWORDS.items():
        if key.lower() in protocol_lower or protocol_lower in key.lower():
            for score_name in score_list:
                # Find score in SCORES_BY_SPECIALTY
                found = False
                for specialty, specialty_scores in SCORES_BY_SPECIALTY.items():
                    if score_name in specialty_scores:
                        key_tuple = (score_name, specialty)
                        if key_tuple not in scores_set:
                            scores.append({
                                "score_id": score_name,
                                "specialty": specialty,
                                "reason": "Liên quan đến protocol"
                            })
                            scores_set.add(key_tuple)
                        found = True
                        break
                if not found:
                    # Try partial match
                    for specialty, specialty_scores in SCORES_BY_SPECIALTY.items():
                        for score_id, score_info in specialty_scores.items():
                            if score_name.lower() in score_id.lower() or score_id.lower() in score_name.lower():
                                key_tuple = (score_id, specialty)
                                if key_tuple not in scores_set:
                                    scores.append({
                                        "score_id": score_id,
                                        "specialty": specialty,
                                        "reason": "Liên quan đến protocol"
                                    })
                                    scores_set.add(key_tuple)
                                found = True
                                break
                        if found:
                            break
    
    # Add common scores based on protocol type
    # eGFR/CrCl for protocols that might need renal dosing
    if any(keyword in protocol_lower for keyword in ["aki", "ckd", "nephro", "renal", "dialysis", "uti", "kidney"]):
        for specialty, specialty_scores in SCORES_BY_SPECIALTY.items():
            if "eGFR" in specialty_scores:
                key_tuple = ("eGFR", specialty)
                if key_tuple not in scores_set:
                    scores.append({
                        "score_id": "eGFR",
                        "specialty": specialty,
                        "reason": "Cần để chỉnh liều thuốc"
                    })
                    scores_set.add(key_tuple)
            if "CrCl" in specialty_scores:
                key_tuple = ("CrCl", specialty)
                if key_tuple not in scores_set:
                    scores.append({
                        "score_id": "CrCl",
                        "specialty": specialty,
                        "reason": "Cần để chỉnh liều thuốc"
                    })
                    scores_set.add(key_tuple)
    
    # BMI/IBW/BSA for protocols that might need weight-based dosing
    if any(keyword in protocol_lower for keyword in ["dosing", "dose", "weight", "anaphylaxis", "overdose", "poisoning"]):
        for specialty, specialty_scores in SCORES_BY_SPECIALTY.items():
            if "BMI/IBW/BSA" in specialty_scores:
                key_tuple = ("BMI/IBW/BSA", specialty)
                if key_tuple not in scores_set:
                    scores.append({
                        "score_id": "BMI/IBW/BSA",
                        "specialty": specialty,
                        "reason": "Cần để tính liều theo cân nặng"
                    })
                    scores_set.add(key_tuple)
    
    # GCS for neurological/emergency protocols
    if any(keyword in protocol_lower for keyword in ["stroke", "brain", "neurological", "trauma", "tbi", "seizure", "epilepticus", "meningitis", "encephalitis"]):
        for specialty, specialty_scores in SCORES_BY_SPECIALTY.items():
            if "GCS" in specialty_scores:
                key_tuple = ("GCS", specialty)
                if key_tuple not in scores_set:
                    scores.append({
                        "score_id": "GCS",
                        "specialty": specialty,
                        "reason": "Đánh giá mức độ ý thức"
                    })
                    scores_set.add(key_tuple)
    
    return scores


def generate_protocol_score_mapping() -> Dict[str, List[Dict[str, str]]]:
    """Generate complete mapping of protocols to scores."""
    protocol_functions = get_all_protocol_functions()
    mapping = {}
    
    for protocol_function, protocol_id in protocol_functions.items():
        scores = find_scores_for_protocol(protocol_id, protocol_function)
        if scores:
            mapping[protocol_function] = scores
    
    return mapping


def update_mapping_file():
    """Update the article_protocol_score_mapping.py file with protocol mappings."""
    mapping = generate_protocol_score_mapping()
    
    mapping_file = BASE_DIR / "config" / "article_protocol_score_mapping.py"
    
    # Read existing file
    content = mapping_file.read_text(encoding="utf-8")
    
    # Find PROTOCOL_TO_SCORES section
    start_marker = "# Mapping: protocol_function -> list of score IDs"
    end_marker = "def get_scores_for_article"
    
    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker)
    
    if start_idx == -1 or end_idx == -1:
        print("Could not find PROTOCOL_TO_SCORES section")
        return
    
    # Generate new PROTOCOL_TO_SCORES dict
    new_section = f"""# Mapping: protocol_function -> list of score IDs
PROTOCOL_TO_SCORES: Dict[str, List[Dict[str, str]]] = {{
"""
    
    for protocol_function, scores in sorted(mapping.items()):
        new_section += f'    "{protocol_function}": [\n'
        for score in scores:
            new_section += f'        {{"score_id": "{score["score_id"]}", "specialty": "{score["specialty"]}", "reason": "{score["reason"]}"}},\n'
        new_section += "    ],\n\n"
    
    new_section += "}\n\n\n"
    
    # Replace section
    new_content = content[:start_idx] + new_section + content[end_idx:]
    
    # Write back
    mapping_file.write_text(new_content, encoding="utf-8")
    print(f"Updated {mapping_file}")
    print(f"Added {len(mapping)} protocol mappings")


if __name__ == "__main__":
    update_mapping_file()
    print("\nDone! Protocol score mappings have been updated.")

