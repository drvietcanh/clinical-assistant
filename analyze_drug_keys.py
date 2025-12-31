import sys
import os

# Add parent directory to path to import modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from drugs.drug_modules import ALL_DRUGS

def is_suspicious(key, value):
    issues = []
    # Check key format
    if not isinstance(key, str):
        issues.append("Non-string key")
    elif key[0].islower():
        issues.append("Starts with lowercase")
    elif "_" in key:
        issues.append("Contains underscore")
    
    # Check value structure
    if not isinstance(value, dict):
        issues.append(f"Value is not dict (is {type(value).__name__})")
    elif "brand_name" not in value and "generic_name" not in value and "vietnamese_name" not in value:
        # Check if it looks like a drug object (usually has names, dosages, etc.)
        # Some simple drugs might just have 'description', but usually they have a name field.
        if "description" not in value:
             issues.append("Missing common name/description fields")

    return issues

print(f"Total entries in ALL_DRUGS: {len(ALL_DRUGS)}")
print("="*60)
print(f"{'KEY':<30} | {'ISSUES'}")
print("="*60)

suspicious_count = 0
for key, value in ALL_DRUGS.items():
    issues = is_suspicious(key, value)
    if issues or True: # Print checks for everything first to verify my heuristics
        if issues:
            suspicious_count += 1
            print(f"{key:<30} | {', '.join(issues)}")

print("="*60)
print(f"Found {suspicious_count} suspicious entries.")
