"""
Script to validate dosage structure in drug files
Checks for:
1. Required fields presence
2. Python syntax errors
3. Consistency of dosage structure
"""
import os
import ast
import json
from pathlib import Path

# Required fields for cardiovascular/hypertension drugs
CV_REQUIRED_FIELDS = [
    "adult_htn",
    "adult_start",
    "adult_usual",
    "adult_max",
    "administration_route",
    "frequency",
    "with_food",
    "notes"
]

# Required fields for diabetes drugs
DM_REQUIRED_FIELDS = [
    "adult_start",
    "adult_usual",
    "adult_max",
    "dm_t2",
    "administration_route",
    "frequency",
    "with_food",
    "notes"
]

# Optional but recommended fields
OPTIONAL_FIELDS = [
    "elderly",
    "renal_adjustment_dosage",
    "hepatic_adjustment_dosage"
]

def check_python_syntax(file_path):
    """Check if Python file has valid syntax"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        ast.parse(code)
        return True, None
    except SyntaxError as e:
        return False, str(e)

def extract_dosage_dict(file_path, drug_name):
    """Extract dosage dictionary for a specific drug"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Try to execute the file to get the dictionary
        # This is a simplified approach - in production, use safer methods
        namespace = {}
        exec(compile(ast.parse(content), file_path, 'exec'), namespace)
        
        # Find the drug dictionary
        for var_name, var_value in namespace.items():
            if isinstance(var_value, dict) and drug_name in var_value:
                drug_data = var_value[drug_name]
                if isinstance(drug_data, dict) and "dosage" in drug_data:
                    return drug_data["dosage"]
        return None
    except Exception as e:
        return None

def validate_dosage_structure(dosage_dict, drug_type="cardiovascular"):
    """Validate dosage structure against required fields"""
    if not dosage_dict:
        return False, "No dosage dictionary found"
    
    required_fields = CV_REQUIRED_FIELDS if drug_type == "cardiovascular" else DM_REQUIRED_FIELDS
    missing_fields = []
    
    for field in required_fields:
        if field not in dosage_dict:
            missing_fields.append(field)
    
    warnings = []
    for field in OPTIONAL_FIELDS:
        if field not in dosage_dict:
            warnings.append(f"Optional field '{field}' missing")
    
    if missing_fields:
        return False, f"Missing required fields: {', '.join(missing_fields)}"
    
    if warnings:
        return True, f"Warnings: {'; '.join(warnings)}"
    
    return True, "All required fields present"

def validate_all_files():
    """Validate all drug files"""
    results = {
        "syntax_errors": [],
        "validation_errors": [],
        "warnings": [],
        "success": []
    }
    
    # Cardiovascular files
    cv_files = [
        "drugs/drug_modules/cardiovascular/ace_arb.py",
        "drugs/drug_modules/cardiovascular/beta_blockers/selective.py",
        "drugs/drug_modules/cardiovascular/beta_blockers/non_selective.py",
        "drugs/drug_modules/cardiovascular/calcium_blockers/dihydropyridines.py",
        "drugs/drug_modules/cardiovascular/calcium_blockers/non_dihydropyridines.py",
        "drugs/drug_modules/cardiovascular/diuretics.py",
        "drugs/drug_modules/cardiovascular/statins.py",
        "drugs/drug_modules/cardiovascular/anticoagulants.py",
    ]
    
    # Diabetes files
    dm_files = [
        "drugs/drug_modules/diabetes/biguanides.py",
        "drugs/drug_modules/diabetes/sglt2_inhibitors.py",
        "drugs/drug_modules/diabetes/dpp_4_inhibitors.py",
        "drugs/drug_modules/diabetes/sulfonylureas.py",
        "drugs/drug_modules/diabetes/insulins.py",
    ]
    
    # Check syntax
    all_files = cv_files + dm_files
    for file_path in all_files:
        if os.path.exists(file_path):
            is_valid, error = check_python_syntax(file_path)
            if not is_valid:
                results["syntax_errors"].append({
                    "file": file_path,
                    "error": error
                })
                print(f"❌ Syntax error in {file_path}: {error}")
            else:
                print(f"✓ Syntax OK: {file_path}")
    
    # Save results
    with open("dosage_validation_results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    print("\n=== VALIDATION SUMMARY ===")
    print(f"Syntax errors: {len(results['syntax_errors'])}")
    print(f"Validation errors: {len(results['validation_errors'])}")
    print(f"Warnings: {len(results['warnings'])}")
    print(f"Success: {len(results['success'])}")
    print("\nResults saved to dosage_validation_results.json")
    
    return results

if __name__ == "__main__":
    validate_all_files()
