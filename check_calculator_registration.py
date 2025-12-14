"""
Script to check calculator registration status
Compares scores/config.py with __init__.py routing dictionaries
"""

import ast
import os
from pathlib import Path
from typing import Dict, List, Set, Tuple

def get_calculators_from_config() -> Dict[str, Dict[str, str]]:
    """Extract calculators from scores/config.py"""
    config_path = Path("scores/config.py")
    if not config_path.exists():
        return {}
    
    with open(config_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Parse SCORES_BY_SPECIALTY
    tree = ast.parse(content)
    scores_by_specialty = {}
    
    for node in ast.walk(tree):
        if isinstance(node, ast.Dict):
            # Try to extract dictionary
            try:
                # This is a simplified parser - may need refinement
                exec(compile(tree, config_path, 'exec'))
                from scores.config import SCORES_BY_SPECIALTY
                return SCORES_BY_SPECIALTY
            except:
                pass
    
    # Fallback: import directly
    try:
        import sys
        sys.path.insert(0, str(Path.cwd()))
        from scores.config import SCORES_BY_SPECIALTY
        return SCORES_BY_SPECIALTY
    except Exception as e:
        print(f"Error importing SCORES_BY_SPECIALTY: {e}")
        return {}


def get_routing_dict_from_init(init_file: Path) -> Dict[str, str]:
    """Extract routing dictionary from __init__.py file"""
    if not init_file.exists():
        return {}
    
    with open(init_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Look for calculators = { ... } pattern
    routing = {}
    
    # Simple regex-like search for dictionary
    import re
    # Find calculators = { ... } block
    pattern = r'calculators\s*=\s*\{([^}]+)\}'
    match = re.search(pattern, content, re.DOTALL)
    
    if match:
        dict_content = match.group(1)
        # Extract key-value pairs
        # Pattern: "Key": render_function,
        kv_pattern = r'["\']([^"\']+)["\']\s*:\s*(\w+)'
        for kv_match in re.finditer(kv_pattern, dict_content):
            key = kv_match.group(1)
            value = kv_match.group(2)
            routing[key] = value
    
    return routing


def check_all_specialties():
    """Check all specialty modules for registration issues"""
    scores_dir = Path("scores")
    if not scores_dir.exists():
        print("scores/ directory not found!")
        return
    
    # Get calculators from config
    scores_by_specialty = get_calculators_from_config()
    
    if not scores_by_specialty:
        print("Could not load SCORES_BY_SPECIALTY from scores/config.py")
        return
    
    print("=" * 80)
    print("CALCULATOR REGISTRATION CHECK")
    print("=" * 80)
    print()
    
    issues = []
    total_calculators = 0
    registered_calculators = 0
    
    # Map specialty names to module directories
    specialty_to_module = {
        "🚨 Cấp cứu & Hồi sức (Emergency & Critical Care)": "emergency",
        "❤️ Tim mạch (Cardiology)": "cardiology",
        "🫁 Hô hấp (Respiratory)": "respiratory",
        "🧠 Thần kinh (Neurology)": "neurology",
        "🩸 Tiêu Hóa - Gan Mật (GI/Hepatology)": "gi",
        "🩺 Huyết Học & Đông máu (Hematology)": "hematology",
        "🧪 Thận - Điện Giải (Nephrology)": "nephrology",
        "🦴 Chấn Thương & Chỉnh Hình (Trauma/Orthopedics)": "trauma",
        "👂 Tai Mũi Họng (ENT)": "ent",
        "👶 Nhi Khoa (Pediatrics)": "pediatrics",
        "🤰 Sản Khoa (Obstetrics)": "obstetrics",
        "💉 Nội tiết - Chuyển hóa (Endocrinology/Metabolism)": "metabolism",
        "🦴 Thấp Khớp - Miễn Dịch (Rheumatology/Immunology)": "rheumatology",
        "🦠 Nhiễm khuẩn (Infectious Disease)": "infectious",
        "🩹 Da Liễu (Dermatology)": "dermatology",
        "🎗️ Ung thư (Oncology)": "oncology",
        "🧠 Tâm Thần - Tâm Lý (Psychiatry/Psychology)": "psychiatry",
        "🔪 Phẫu Thuật & Gây Mê (Surgery/Anesthesia)": "surgery",
        "👁️ Mắt (Ophthalmology)": "ophthalmology",
        "😣 Đánh giá đau (Pain Assessment)": "pain",
        "🛏️ Chăm sóc điều dưỡng (Nursing Care)": "nursing",
    }
    
    for specialty_name, calculators in scores_by_specialty.items():
        module_name = None
        for key, value in specialty_to_module.items():
            if key in specialty_name or specialty_name in key:
                module_name = value
                break
        
        if not module_name:
            # Try to extract from specialty name
            if "Cấp cứu" in specialty_name:
                module_name = "emergency"
            elif "Tim mạch" in specialty_name:
                module_name = "cardiology"
            elif "Hô hấp" in specialty_name:
                module_name = "respiratory"
            elif "Thần kinh" in specialty_name:
                module_name = "neurology"
            elif "Tiêu Hóa" in specialty_name or "Gan" in specialty_name:
                module_name = "gi"
            elif "Huyết Học" in specialty_name:
                module_name = "hematology"
            elif "Thận" in specialty_name:
                module_name = "nephrology"
            elif "Chấn Thương" in specialty_name:
                module_name = "trauma"
            elif "Tai Mũi Họng" in specialty_name or "ENT" in specialty_name:
                module_name = "ent"
            elif "Nhi Khoa" in specialty_name or "Pediatrics" in specialty_name:
                module_name = "pediatrics"
            elif "Sản Khoa" in specialty_name or "Obstetrics" in specialty_name:
                module_name = "obstetrics"
            elif "Nội tiết" in specialty_name or "Metabolism" in specialty_name:
                module_name = "metabolism"
            elif "Thấp Khớp" in specialty_name or "Rheumatology" in specialty_name:
                module_name = "rheumatology"
            elif "Nhiễm khuẩn" in specialty_name or "Infectious" in specialty_name:
                module_name = "infectious"
            elif "Da Liễu" in specialty_name or "Dermatology" in specialty_name:
                module_name = "dermatology"
            elif "Ung thư" in specialty_name or "Oncology" in specialty_name:
                module_name = "oncology"
            elif "Tâm Thần" in specialty_name or "Psychiatry" in specialty_name:
                module_name = "psychiatry"
            elif "Phẫu Thuật" in specialty_name or "Surgery" in specialty_name:
                module_name = "surgery"
            elif "Mắt" in specialty_name or "Ophthalmology" in specialty_name:
                module_name = "ophthalmology"
            elif "đau" in specialty_name or "Pain" in specialty_name:
                module_name = "pain"
            elif "điều dưỡng" in specialty_name or "Nursing" in specialty_name:
                module_name = "nursing"
        
        if not module_name:
            print(f"⚠️  Could not map specialty: {specialty_name}")
            continue
        
        init_file = scores_dir / module_name / "__init__.py"
        if not init_file.exists():
            print(f"❌ Module {module_name} has no __init__.py")
            issues.append((specialty_name, module_name, "NO_INIT_FILE", list(calculators.keys())))
            continue
        
        # Get routing dictionary
        routing = get_routing_dict_from_init(init_file)
        
        # Also try to read the file and parse more carefully
        with open(init_file, 'r', encoding='utf-8') as f:
            init_content = f.read()
            # Look for all string keys in calculators dict
            import re
            calc_dict_pattern = r'calculators\s*=\s*\{([^}]+)\}'
            match = re.search(calc_dict_pattern, init_content, re.DOTALL)
            if match:
                dict_body = match.group(1)
                # Find all "key": value pairs
                kv_pattern = r'["\']([^"\']+)["\']\s*:\s*(\w+)'
                routing = {}
                for m in re.finditer(kv_pattern, dict_body):
                    routing[m.group(1)] = m.group(2)
        
        print(f"\n📊 {specialty_name}")
        print(f"   Module: {module_name}")
        print(f"   Calculators in config: {len(calculators)}")
        print(f"   Calculators in routing: {len(routing)}")
        
        total_calculators += len(calculators)
        
        # Check each calculator
        missing_in_routing = []
        for calc_id, calc_info in calculators.items():
            if calc_id not in routing:
                missing_in_routing.append(calc_id)
            else:
                registered_calculators += 1
        
        if missing_in_routing:
            print(f"   ❌ Missing in routing: {missing_in_routing}")
            issues.append((specialty_name, module_name, "MISSING_IN_ROUTING", missing_in_routing))
        else:
            print(f"   ✅ All calculators registered")
    
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Total calculators in config: {total_calculators}")
    print(f"Registered calculators: {registered_calculators}")
    print(f"Missing registrations: {total_calculators - registered_calculators}")
    
    if issues:
        print(f"\n⚠️  Found {len(issues)} issues:")
        for specialty, module, issue_type, missing in issues:
            print(f"   - {specialty} ({module}): {issue_type}")
            if missing:
                print(f"     Missing: {missing}")
    else:
        print("\n✅ All calculators are properly registered!")
    
    return issues


if __name__ == "__main__":
    check_all_specialties()

