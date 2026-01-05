"""
Script to add risk_flags and guideline_tags to drugs missing them
"""
import ast
import os
from pathlib import Path
import re

# Template for risk_flags based on drug category
RISK_FLAGS_TEMPLATES = {
    "antiarrhythmic": {
        "high_alert": True,
        "narrow_therapeutic_index": True,
        "bleeding_risk": False,
        "organ_toxicity": ["cardiac"],
        "qt_prolongation": True,
        "hepatotoxicity": False,
        "nephrotoxicity": False,
        "requires_monitoring": ["ECG", "QT interval"]
    },
    "sglt2_inhibitor": {
        "high_alert": False,
        "narrow_therapeutic_index": False,
        "bleeding_risk": False,
        "organ_toxicity": ["genitourinary"],
        "qt_prolongation": False,
        "hepatotoxicity": False,
        "nephrotoxicity": False,
        "requires_monitoring": ["eGFR", "Genital/urinary infections"]
    },
    "alpha_glucosidase": {
        "high_alert": False,
        "narrow_therapeutic_index": False,
        "bleeding_risk": False,
        "organ_toxicity": [],
        "qt_prolongation": False,
        "hepatotoxicity": False,
        "nephrotoxicity": False,
        "requires_monitoring": ["LFT"]
    },
    "gi_antacid": {
        "high_alert": False,
        "narrow_therapeutic_index": False,
        "bleeding_risk": False,
        "organ_toxicity": [],
        "qt_prolongation": False,
        "hepatotoxicity": False,
        "nephrotoxicity": False,
        "requires_monitoring": []
    },
    "ppi": {
        "high_alert": False,
        "narrow_therapeutic_index": False,
        "bleeding_risk": False,
        "organ_toxicity": [],
        "qt_prolongation": False,
        "hepatotoxicity": False,
        "nephrotoxicity": False,
        "requires_monitoring": ["Magnesium (long-term use)"]
    },
    "jak_inhibitor": {
        "high_alert": True,
        "narrow_therapeutic_index": False,
        "bleeding_risk": False,
        "organ_toxicity": ["infectious", "thrombotic", "malignancy"],
        "qt_prolongation": False,
        "hepatotoxicity": False,
        "nephrotoxicity": False,
        "requires_monitoring": ["CBC", "LFT", "Lipids", "TB screening"]
    },
    "laxative": {
        "high_alert": False,
        "narrow_therapeutic_index": False,
        "bleeding_risk": False,
        "organ_toxicity": [],
        "qt_prolongation": False,
        "hepatotoxicity": False,
        "nephrotoxicity": False,
        "requires_monitoring": ["Electrolytes (long-term use)"]
    },
    "antispasmodic": {
        "high_alert": False,
        "narrow_therapeutic_index": False,
        "bleeding_risk": False,
        "organ_toxicity": [],
        "qt_prolongation": False,
        "hepatotoxicity": False,
        "nephrotoxicity": False,
        "requires_monitoring": []
    },
    "nsaid": {
        "high_alert": False,
        "narrow_therapeutic_index": False,
        "bleeding_risk": True,
        "organ_toxicity": ["GI", "renal", "cardiac"],
        "qt_prolongation": False,
        "hepatotoxicity": True,
        "nephrotoxicity": True,
        "requires_monitoring": ["LFT", "RFT", "GI symptoms"]
    },
    "opioid": {
        "high_alert": True,
        "narrow_therapeutic_index": False,
        "bleeding_risk": False,
        "organ_toxicity": [],
        "qt_prolongation": False,
        "hepatotoxicity": False,
        "nephrotoxicity": False,
        "requires_monitoring": ["Respiratory rate", "Sedation", "Constipation"]
    },
    "antiepileptic": {
        "high_alert": False,
        "narrow_therapeutic_index": False,
        "bleeding_risk": False,
        "organ_toxicity": ["hepatic", "dermatologic"],
        "qt_prolongation": False,
        "hepatotoxicity": True,
        "nephrotoxicity": False,
        "requires_monitoring": ["LFT", "CBC", "Drug levels"]
    },
    "anticholinergic": {
        "high_alert": False,
        "narrow_therapeutic_index": False,
        "bleeding_risk": False,
        "organ_toxicity": [],
        "qt_prolongation": False,
        "hepatotoxicity": False,
        "nephrotoxicity": False,
        "requires_monitoring": []
    },
    "antidote": {
        "high_alert": True,
        "narrow_therapeutic_index": False,
        "bleeding_risk": False,
        "organ_toxicity": [],
        "qt_prolongation": False,
        "hepatotoxicity": False,
        "nephrotoxicity": False,
        "requires_monitoring": []
    },
    "vaccine": {
        "high_alert": False,
        "narrow_therapeutic_index": False,
        "bleeding_risk": False,
        "organ_toxicity": [],
        "qt_prolongation": False,
        "hepatotoxicity": False,
        "nephrotoxicity": False,
        "requires_monitoring": []
    },
    "vitamin": {
        "high_alert": False,
        "narrow_therapeutic_index": False,
        "bleeding_risk": False,
        "organ_toxicity": [],
        "qt_prolongation": False,
        "hepatotoxicity": False,
        "nephrotoxicity": False,
        "requires_monitoring": []
    },
    "default": {
        "high_alert": False,
        "narrow_therapeutic_index": False,
        "bleeding_risk": False,
        "organ_toxicity": [],
        "qt_prolongation": False,
        "hepatotoxicity": False,
        "nephrotoxicity": False,
        "requires_monitoring": []
    }
}

# Guideline tags templates
GUIDELINE_TAGS_TEMPLATES = {
    "antiarrhythmic": [
        "AHA/ACC/HRS 2019 Arrhythmia Guidelines",
        "ESC 2020 Atrial Fibrillation Guidelines"
    ],
    "sglt2_inhibitor": [
        "ADA 2024 Standards of Care - Diabetes",
        "AACE/ACE 2023 Type 2 Diabetes Guidelines",
        "FDA Black Box Warning - Fournier's Gangrene (rare)"
    ],
    "alpha_glucosidase": [
        "ADA 2024 Standards of Care - Diabetes",
        "AACE/ACE 2023 Type 2 Diabetes Guidelines"
    ],
    "gi_antacid": [
        "ACG 2017 GERD Guidelines",
        "FDA - Over-the-counter antacids"
    ],
    "ppi": [
        "ACG 2017 GERD Guidelines",
        "FDA - Long-term PPI use monitoring"
    ],
    "jak_inhibitor": [
        "FDA Black Box Warning - Serious infections, thrombosis, malignancy, MACE",
        "ACR 2021 Rheumatoid Arthritis Guidelines"
    ],
    "laxative": [
        "ACG 2013 Constipation Guidelines",
        "FDA - Laxative safety"
    ],
    "nsaid": [
        "ACR 2021 Osteoarthritis Guidelines",
        "FDA Black Box Warning - Cardiovascular and GI risks"
    ],
    "opioid": [
        "CDC 2022 Opioid Prescribing Guidelines",
        "FDA Black Box Warning - Opioid addiction, abuse, misuse"
    ],
    "antiepileptic": [
        "AAN 2018 Epilepsy Guidelines",
        "FDA - Antiepileptic drug safety"
    ],
    "default": [
        "FDA Drug Information",
        "UpToDate Drug Information"
    ]
}

def categorize_drug(drug_name, group=""):
    """Categorize drug to determine which template to use"""
    name_lower = drug_name.lower()
    group_lower = group.lower()
    
    # Antiarrhythmics
    if any(x in name_lower for x in ["adenosine", "amiodarone", "disopyramide", "dofetilide", 
                                      "dronedarone", "flecainide", "ibutilide", "procainamide", 
                                      "propafenone", "quinidine", "sotalol"]) or "antiarrhythmic" in group_lower:
        return "antiarrhythmic"
    
    # SGLT2 inhibitors
    if any(x in name_lower for x in ["empagliflozin", "dapagliflozin", "canagliflozin"]) or "sglt2" in group_lower:
        return "sglt2_inhibitor"
    
    # Alpha-glucosidase inhibitors
    if any(x in name_lower for x in ["acarbose", "miglitol"]) or "alpha_glucosidase" in group_lower:
        return "alpha_glucosidase"
    
    # GI antacids
    if any(x in name_lower for x in ["aluminum", "magnesium", "calcium carbonate", "bismuth"]):
        return "gi_antacid"
    
    # PPIs
    if any(x in name_lower for x in ["dexlansoprazole", "ilaprazole", "tegoprazan", "vonoprazan"]) or "ppi" in group_lower:
        return "ppi"
    
    # JAK inhibitors
    if any(x in name_lower for x in ["baricitinib", "upadacitinib", "tofacitinib"]):
        return "jak_inhibitor"
    
    # Laxatives
    if any(x in name_lower for x in ["lactulose", "polyethylene", "senna"]):
        return "laxative"
    
    # Antispasmodics
    if any(x in name_lower for x in ["hyoscine", "mebeverine", "trimebutine", "simethicone"]):
        return "antispasmodic"
    
    # NSAIDs
    if any(x in name_lower for x in ["celecoxib", "etoricoxib", "indomethacin", "ketoprofen", "nimesulide"]):
        return "nsaid"
    
    # Opioids
    if any(x in name_lower for x in ["buprenorphine", "hydrocodone", "tapentadol", "meperidine", "oxycodone", "codeine"]):
        return "opioid"
    
    # Antiepileptics
    if any(x in name_lower for x in ["fosphenytoin", "lacosamide", "lamotrigine", "levetiracetam", "phenobarbital"]):
        return "antiepileptic"
    
    # Antidotes
    if any(x in name_lower for x in ["naloxone", "naltrexone", "pralidoxime", "acetylcysteine"]):
        return "antidote"
    
    # Vaccines
    if "vaccine" in name_lower or "antitoxin" in name_lower or "antivenom" in name_lower:
        return "vaccine"
    
    # Vitamins
    if any(x in name_lower for x in ["vitamin", "thiamine", "pyridoxine", "cyanocobalamin", "ascorbic"]):
        return "vitamin"
    
    return "default"

def format_risk_flags(risk_flags_dict):
    """Format risk_flags dictionary as Python code"""
    lines = ["            \"risk_flags\": {"]
    for key, value in risk_flags_dict.items():
        if isinstance(value, list):
            value_str = "[" + ", ".join(f'"{v}"' if isinstance(v, str) else str(v) for v in value) + "]"
        elif isinstance(value, bool):
            value_str = str(value)
        elif isinstance(value, str):
            value_str = f'"{value}"'
        else:
            value_str = str(value)
        lines.append(f'                "{key}": {value_str},')
    lines.append("            },")
    return "\n".join(lines)

def format_guideline_tags(guideline_tags_list):
    """Format guideline_tags list as Python code"""
    if not guideline_tags_list:
        return '            "guideline_tags": [],'
    
    lines = ["            \"guideline_tags\": ["]
    for tag in guideline_tags_list:
        lines.append(f'                "{tag}",')
    lines.append("            ]")
    return "\n".join(lines)

def add_risk_flags_to_file(file_path, drug_name, dry_run=True):
    """Add risk_flags and guideline_tags to a drug in a file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if already has both
        if '"risk_flags"' in content and '"guideline_tags"' in content:
            # Check if this specific drug has them
            drug_pattern = f'"{re.escape(drug_name)}"'
            if re.search(drug_pattern, content):
                # Find the drug entry
                drug_start = content.find(f'"{drug_name}"')
                if drug_start != -1:
                    # Check if risk_flags exists in this drug's entry
                    drug_end = content.find('},', drug_start)
                    if drug_end != -1:
                        drug_entry = content[drug_start:drug_end]
                        if '"risk_flags"' in drug_entry and '"guideline_tags"' in drug_entry:
                            return False, "Already has both fields"
        
        # Get drug group from content
        group_match = re.search(rf'"{re.escape(drug_name)}".*?"group":\s*"([^"]+)"', content, re.DOTALL)
        group = group_match.group(1) if group_match else ""
        
        # Categorize drug
        category = categorize_drug(drug_name, group)
        risk_flags = RISK_FLAGS_TEMPLATES.get(category, RISK_FLAGS_TEMPLATES["default"]).copy()
        guideline_tags = GUIDELINE_TAGS_TEMPLATES.get(category, GUIDELINE_TAGS_TEMPLATES["default"]).copy()
        
        # Find drug entry
        drug_pattern = f'"{re.escape(drug_name)}":\\s*\\{{'
        match = re.search(drug_pattern, content)
        if not match:
            return False, f"Drug {drug_name} not found in file"
        
        drug_start = match.start()
        # Find the end of this drug's dictionary
        brace_count = 0
        in_string = False
        escape_next = False
        i = drug_start
        while i < len(content):
            char = content[i]
            if escape_next:
                escape_next = False
                i += 1
                continue
            if char == '\\':
                escape_next = True
                i += 1
                continue
            if char == '"' and not escape_next:
                in_string = not in_string
            if not in_string:
                if char == '{':
                    brace_count += 1
                elif char == '}':
                    brace_count -= 1
                    if brace_count == 0:
                        drug_end = i + 1
                        break
            i += 1
        else:
            return False, f"Could not find end of drug entry for {drug_name}"
        
        drug_entry = content[drug_start:drug_end]
        
        # Check if already has risk_flags or guideline_tags
        has_rf = '"risk_flags"' in drug_entry
        has_gt = '"guideline_tags"' in drug_entry
        
        if has_rf and has_gt:
            return False, "Already has both fields"
        
        # Find insertion point (before the closing brace)
        # Look for the last field before closing brace
        last_comma = drug_entry.rfind(',')
        if last_comma == -1:
            # No comma, insert before closing brace
            insert_pos = drug_entry.rfind('}')
        else:
            insert_pos = last_comma + 1
        
        # Format the new fields
        new_fields = []
        if not has_rf:
            new_fields.append(format_risk_flags(risk_flags))
        if not has_gt:
            new_fields.append(format_guideline_tags(guideline_tags))
        
        new_content = (
            drug_entry[:insert_pos] + 
            ("\n" if insert_pos < len(drug_entry) - 1 else "") +
            "\n".join(new_fields) +
            drug_entry[insert_pos:]
        )
        
        if not dry_run:
            # Create backup
            backup_path = str(file_path) + ".backup"
            with open(backup_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            # Write updated content
            updated_content = content[:drug_start] + new_content + content[drug_end:]
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
        
        return True, f"Would add {category} template" if dry_run else f"Added {category} template"
        
    except Exception as e:
        return False, f"Error: {str(e)}"

def find_drug_file(drug_name):
    """Find the file containing a drug"""
    drugs_dir = Path("drugs/drug_modules")
    
    for file_path in drugs_dir.rglob("*.py"):
        if file_path.name == "__init__.py" or file_path.name.endswith(".backup"):
            continue
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                if f'"{drug_name}"' in content or f"'{drug_name}'" in content:
                    return file_path
        except:
            continue
    
    return None

def main():
    """Main function"""
    import sys
    
    # Read missing drugs from report
    missing_drugs = []
    try:
        with open("missing_risk_flags_direct_report.txt", 'r', encoding='utf-8') as f:
            content = f.read()
            # Extract drug names from "MISSING BOTH" section
            in_missing_both = False
            for line in content.split('\n'):
                if "MISSING BOTH" in line:
                    in_missing_both = True
                    continue
                if "MISSING ONLY" in line:
                    in_missing_both = False
                    continue
                if in_missing_both and line.strip() and not line.startswith("="):
                    missing_drugs.append(line.strip())
    except FileNotFoundError:
        print("Error: missing_risk_flags_direct_report.txt not found. Run check_missing_risk_flags_direct.py first.")
        return
    
    # Also add drugs missing only guideline_tags
    try:
        with open("missing_risk_flags_direct_report.txt", 'r', encoding='utf-8') as f:
            content = f.read()
            in_missing_gt = False
            for line in content.split('\n'):
                if "MISSING ONLY GUIDELINE_TAGS" in line:
                    in_missing_gt = True
                    continue
                if in_missing_gt and line.strip() and not line.startswith("="):
                    missing_drugs.append(line.strip())
    except:
        pass
    
    dry_run = "--execute" not in sys.argv
    
    if dry_run:
        print("DRY RUN MODE - No files will be modified")
        print("Add --execute flag to actually modify files\n")
    else:
        print("EXECUTE MODE - Files will be modified\n")
    
    print(f"Processing {len(missing_drugs)} drugs...\n")
    
    success_count = 0
    fail_count = 0
    skip_count = 0
    
    for drug_name in missing_drugs:
        file_path = find_drug_file(drug_name)
        if not file_path:
            print(f"❌ {drug_name}: File not found")
            fail_count += 1
            continue
        
        success, message = add_risk_flags_to_file(file_path, drug_name, dry_run=dry_run)
        if success:
            print(f"✅ {drug_name}: {message}")
            success_count += 1
        elif "Already has" in message:
            print(f"⏭️  {drug_name}: {message}")
            skip_count += 1
        else:
            print(f"❌ {drug_name}: {message}")
            fail_count += 1
    
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    print(f"Total: {len(missing_drugs)}")
    print(f"Success: {success_count}")
    print(f"Skipped: {skip_count}")
    print(f"Failed: {fail_count}")

if __name__ == "__main__":
    main()

